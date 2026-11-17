"""Fast vectorised preview renderer (numpy z-buffer, orthographic, flat shading, outlines).

Every triangle of every posed item is rasterised in chunks with numpy; a
z-buffer keeps the nearest, the colour comes from the material legend,
shading is a two-sided Lambert term with ambient light, and outlines are
drawn where the part id, the depth or the facet normal jumps. Placeholder
envelopes are drawn pale. The image is rendered at twice the size and
averaged down for clean edges.
"""
from __future__ import annotations

import math
from pathlib import Path

import numpy as np

from .materials import LEGEND

VIEWS = {
    #        forward (camera looks along this), up
    "iso": ((1.0, 1.0, -0.75), (0, 0, 1)),
    "iso_rear": ((-0.55, 1.0, -0.5), (0, 0, 1)),    # from +X, -Y: the generator and belt side
    "front": ((1.0, 0.0, 0.0), (0, 0, 1)),     # from upwind (-X) looking downwind
    "side": ((0.0, 1.0, 0.0), (0, 0, 1)),      # from -Y: +X to the right, wind from the left
    "top": ((0.0, 0.0, -1.0), (0, 1, 0)),
    "bottom": ((0.0, 0.0, 1.0), (0, -1, 0)),
}


def _basis(forward, up):
    f = np.asarray(forward, float)
    f /= np.linalg.norm(f)
    u = np.asarray(up, float)
    r = np.cross(f, u)
    r /= np.linalg.norm(r)
    u = np.cross(r, f)
    return r, u, f


def _gather(meshes):
    vs, fs, tri_item = [], [], []
    off = 0
    for k, (v, f) in enumerate(meshes):
        if len(f) == 0:
            continue
        vs.append(v)
        fs.append(f + off)
        tri_item.append(np.full(len(f), k, np.int32))
        off += len(v)
    return np.vstack(vs), np.vstack(fs), np.concatenate(tri_item)


def rasterise(meshes, colors, view, extent=None, size=(1600, 1200), ss=2, light=None):
    """Render ``meshes`` [(V, F), ...] with per-mesh RGB ``colors``; returns an (H, W, 3) float image."""
    fwd, up = VIEWS[view] if isinstance(view, str) else view
    r, u, f = _basis(fwd, up)
    V, F, T = _gather(meshes)
    sx, sy, sz = V @ r, V @ u, V @ f
    W, H = size[0] * ss, size[1] * ss
    if extent is not None:
        lo, hi = np.asarray(extent[0], float), np.asarray(extent[1], float)
        corners = np.array([[x, y, z] for x in (lo[0], hi[0]) for y in (lo[1], hi[1]) for z in (lo[2], hi[2])])
        cx, cy = corners @ r, corners @ u
    else:
        cx, cy = sx, sy
    x0, x1, y0, y1 = cx.min(), cx.max(), cy.min(), cy.max()
    margin = 0.04
    scale = min(W * (1 - 2 * margin) / max(x1 - x0, 1e-9), H * (1 - 2 * margin) / max(y1 - y0, 1e-9))
    ox = W / 2 - scale * (x0 + x1) / 2
    oy = H / 2 + scale * (y0 + y1) / 2
    px = sx * scale + ox
    py = -sy * scale + oy
    # per-triangle data
    a, b, c = F[:, 0], F[:, 1], F[:, 2]
    e1 = V[b] - V[a]
    e2 = V[c] - V[a]
    n = np.cross(e1, e2)
    nn = np.linalg.norm(n, axis=1)
    good = nn > 1e-12
    n[good] /= nn[good, None]
    L1 = -f + 0.35 * u - 0.25 * r if light is None else np.asarray(light, float)
    L1 /= np.linalg.norm(L1)
    L2 = np.array([0.3, -0.5, 0.8])
    L2 /= np.linalg.norm(L2)
    shade = 0.38 + 0.52 * np.abs(n @ L1) + 0.10 * np.abs(n @ L2)
    X = np.stack([px[a], px[b], px[c]], 1)
    Y = np.stack([py[a], py[b], py[c]], 1)
    Z = np.stack([sz[a], sz[b], sz[c]], 1)
    area2 = (X[:, 1] - X[:, 0]) * (Y[:, 2] - Y[:, 0]) - (X[:, 2] - X[:, 0]) * (Y[:, 1] - Y[:, 0])
    vis = good & (n @ f < 1e-9)                 # back faces of closed solids are hidden anyway
    vis &= (X.max(1) >= 0) & (X.min(1) < W) & (Y.max(1) >= 0) & (Y.min(1) < H)
    vis &= np.abs(area2) > 1e-9
    idx = np.nonzero(vis)[0]
    sgn = np.sign(area2[idx])
    # depth plane per triangle: z = Z0 + gx (x - X0) + gy (y - Y0)
    dX1, dY1, dZ1 = X[idx, 1] - X[idx, 0], Y[idx, 1] - Y[idx, 0], Z[idx, 1] - Z[idx, 0]
    dX2, dY2, dZ2 = X[idx, 2] - X[idx, 0], Y[idx, 2] - Y[idx, 0], Z[idx, 2] - Z[idx, 0]
    ar = area2[idx]
    gx = (dZ1 * dY2 - dY1 * dZ2) / ar
    gy = (dX1 * dZ2 - dX2 * dZ1) / ar
    # edge i -> j as  A x + B(y) >= 0  (sign-normalised so the inside is positive)
    edges = []
    for i0, j0 in ((0, 1), (1, 2), (2, 0)):
        xi, yi, xj, yj = X[idx, i0], Y[idx, i0], X[idx, j0], Y[idx, j0]
        A = -sgn * (yj - yi)
        Bk = sgn * (xj - xi)                    # B(y) = Bk (y - yi) + (-A) xi ... below
        edges.append((A, Bk, xi, yi))
    y_lo = np.clip(np.ceil(Y[idx].min(1) - 0.5), 0, H - 1).astype(np.int64)
    y_hi = np.clip(np.floor(Y[idx].max(1) - 0.5), 0, H - 1).astype(np.int64)
    rows = np.maximum(y_hi - y_lo + 1, 0)
    zbuf = np.full(W * H, np.inf)
    tbuf = np.full(W * H, -1, np.int64)
    rbudget = 3_000_000
    rc = np.cumsum(rows)
    start = 0
    while start < len(idx):
        base = rc[start - 1] if start else 0
        end = max(int(np.searchsorted(rc, base + rbudget, side="right")), start + 1)
        k = np.arange(start, end)
        nr = rows[start:end]
        kr = np.repeat(k, nr)
        yr = y_lo[kr] + (np.arange(nr.sum()) - np.repeat(np.cumsum(nr) - nr, nr))
        yc = yr + 0.5
        xl = np.full(len(kr), -np.inf)
        xr = np.full(len(kr), np.inf)
        empty = np.zeros(len(kr), bool)
        for A, Bk, xi, yi in edges:
            Ak = A[kr]
            Bv = Bk[kr] * (yc - yi[kr]) - Ak * xi[kr]      # E = A x + Bv
            pos = Ak > 1e-12
            neg = Ak < -1e-12
            zer = ~(pos | neg)
            with np.errstate(divide="ignore", invalid="ignore"):
                bnd = -Bv / Ak
            xl = np.where(pos, np.maximum(xl, bnd), xl)
            xr = np.where(neg, np.minimum(xr, bnd), xr)
            empty |= zer & (Bv < 0)
        xs = np.clip(np.ceil(xl - 0.5), 0, W)
        xe = np.clip(np.floor(xr - 0.5), -1, W - 1)
        cntp = np.where(empty, 0, np.maximum(xe - xs + 1, 0)).astype(np.int64)
        tot = int(cntp.sum())
        if tot:
            kp = np.repeat(kr, cntp)
            xp = np.repeat(xs.astype(np.int64), cntp) + (np.arange(tot) - np.repeat(np.cumsum(cntp) - cntp, cntp))
            yp = np.repeat(yr, cntp)
            dep = Z[idx[kp], 0] + gx[kp] * (xp + 0.5 - X[idx[kp], 0]) + gy[kp] * (yp + 0.5 - Y[idx[kp], 0])
            pix = yp * W + xp
            order = np.argsort(-dep, kind="stable")
            pix, dep, kp = pix[order], dep[order], kp[order]
            better = dep < zbuf[pix]
            zbuf[pix[better]] = dep[better]
            tbuf[pix[better]] = idx[kp[better]]
        start = end
    img = np.ones((H * W, 3))
    hit = tbuf >= 0
    cols = np.asarray(colors, float)
    img[hit] = cols[T[tbuf[hit]]] * shade[tbuf[hit], None]
    img = img.reshape(H, W, 3)
    # outlines: item change, depth jump, crease
    item = np.where(hit, T[np.maximum(tbuf, 0)], -1).reshape(H, W)
    dep = np.where(hit, zbuf, np.nan).reshape(H, W)
    nrm = np.zeros((H * W, 3))
    nrm[hit] = n[tbuf[hit]]
    nrm = nrm.reshape(H, W, 3)
    edge = np.zeros((H, W), bool)
    dthr = 4.0 / scale + 1.5
    for dy, dx in ((0, 1), (1, 0)):
        ia, ib = item[: H - dy, : W - dx], item[dy:, dx:]
        da, db = dep[: H - dy, : W - dx], dep[dy:, dx:]
        na, nb = nrm[: H - dy, : W - dx], nrm[dy:, dx:]
        e = ia != ib
        with np.errstate(invalid="ignore"):
            e |= np.abs(da - db) > dthr
        crease = np.abs(np.sum(na * nb, axis=2)) < 0.82
        e |= crease & (ia >= 0)
        edge[: H - dy, : W - dx] |= e
    img[edge] *= 0.25
    if ss > 1:
        img = img.reshape(H // ss, ss, W // ss, ss, 3).mean(axis=(1, 3))
    return img, {"scale": scale / ss, "basis": (r, u, f)}


def item_color(it):
    rgb = np.array(LEGEND[it.material_key].rgb)
    if it.placeholder:
        rgb = 0.45 * rgb + 0.55
    return rgb


def render_items(items, view, out_png, extent=None, size=(1600, 1200), title="", mesh_fn=None,
                 note="", legend=True):
    """Render posed Items to a PNG with a title and a material legend."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.patches import Patch

    meshes, cols, used, ph = [], [], {}, False
    for it in items:
        v, f = mesh_fn(it)
        if len(f) == 0:
            continue
        if extent is not None:
            lo, hi = np.asarray(extent[0]), np.asarray(extent[1])
            if np.any(v.max(0) < lo - 1) or np.any(v.min(0) > hi + 1):
                continue
        meshes.append((v, f))
        cols.append(item_color(it))
        used[it.material_key] = True
        ph |= it.placeholder
    img, info = rasterise(meshes, cols, view, extent, size)
    dpi = 100
    fig_w = size[0] / dpi + (3.3 if legend else 0)
    fig = plt.figure(figsize=(fig_w, size[1] / dpi + 0.5), dpi=dpi)
    ax = fig.add_axes([0, 0, size[0] / dpi / fig_w, size[1] / (size[1] + 50)])
    ax.imshow(np.clip(img, 0, 1), interpolation="nearest")
    ax.set_axis_off()
    # scale bar
    px_per_mm = info["scale"]
    bar = 100.0 if px_per_mm * 100 < size[0] / 4 else 50.0
    if px_per_mm * bar < 30:
        bar = 500.0
    x0, y0 = 40, size[1] - 40
    ax.plot([x0, x0 + bar * px_per_mm], [y0, y0], color="k", lw=3)
    ax.text(x0, y0 - 12, f"{bar:.0f} mm", fontsize=10)
    _axes_triad(ax, info["basis"], size)
    fig.text(0.01, 1 - 0.3 / (size[1] / dpi + 0.5), title, fontsize=13, weight="bold", va="top")
    if note:
        fig.text(0.01, 0.005, note, fontsize=8, va="bottom", color="#333")
    if legend:
        keys = [k for k in LEGEND if k in used]
        handles = [Patch(facecolor=LEGEND[k].hex, edgecolor="#222", label=LEGEND[k].label) for k in keys]
        if ph:
            handles.append(Patch(facecolor="#e8e8e8", edgecolor="#888", label="pale: placeholder envelope"))
        lax = fig.add_axes([size[0] / dpi / fig_w, 0.05, 1 - size[0] / dpi / fig_w, 0.9])
        lax.set_axis_off()
        lax.legend(handles=handles, loc="upper left", fontsize=9, frameon=False, title="Materials",
                   title_fontsize=10)
    out_png = Path(out_png)
    out_png.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_png, dpi=dpi)
    plt.close(fig)
    return out_png


def _axes_triad(ax, basis, size):
    r, u, f = basis
    ox, oy = size[0] - 70, size[1] - 60
    for vec, lab, col in (((1, 0, 0), "X", "#c0392b"), ((0, 1, 0), "Y", "#27ae60"), ((0, 0, 1), "Z", "#2c5fb3")):
        v = np.array(vec, float)
        dx, dy = v @ r, -(v @ u)
        if math.hypot(dx, dy) < 0.15:
            ax.text(ox, oy, lab + ("⊙" if v @ f < 0 else "⊗"), color=col, fontsize=10, ha="center", va="center")
            continue
        ax.annotate("", xy=(ox + 40 * dx, oy + 40 * dy), xytext=(ox, oy),
                    arrowprops=dict(arrowstyle="->", color=col, lw=2))
        ax.text(ox + 50 * dx, oy + 50 * dy, lab, color=col, fontsize=10, ha="center", va="center")
