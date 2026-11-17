"""Tessellation of build123d shapes into numpy meshes and manifold3d solids.

Meshes are made from the unposed shape and cached by shape identity, so one
tessellation serves every pose: posing a mesh is a 4 x 4 matrix on its
vertices.
"""
from __future__ import annotations

import numpy as np

_CACHE: dict[int, tuple] = {}


def _tess_face_arrays(shape, tol: float, ang: float = 0.3):
    """Vertices and triangles of every face of ``shape`` (vertices merged per solid by position)."""
    from OCP.BRep import BRep_Tool
    from OCP.BRepMesh import BRepMesh_IncrementalMesh
    from OCP.TopAbs import TopAbs_FACE, TopAbs_REVERSED
    from OCP.TopExp import TopExp_Explorer
    from OCP.TopLoc import TopLoc_Location
    from OCP.TopoDS import TopoDS

    w = shape.wrapped
    BRepMesh_IncrementalMesh(w, tol, False, ang, True)
    verts, tris = [], []
    off = 0
    exp = TopExp_Explorer(w, TopAbs_FACE)
    while exp.More():
        face = TopoDS.Face(exp.Current())
        loc = TopLoc_Location()
        tri = BRep_Tool.Triangulation_s(face, loc)
        exp.Next()
        if tri is None:
            continue
        n = tri.NbNodes()
        trsf = loc.Transformation()
        pts = np.empty((n, 3))
        for i in range(1, n + 1):
            p = tri.Node(i).Transformed(trsf)
            pts[i - 1] = (p.X(), p.Y(), p.Z())
        m = tri.NbTriangles()
        t = np.empty((m, 3), dtype=np.int64)
        for i in range(1, m + 1):
            a, b, c = tri.Triangle(i).Get()
            t[i - 1] = (a - 1, b - 1, c - 1)
        if face.Orientation() == TopAbs_REVERSED:
            t = t[:, ::-1]
        verts.append(pts)
        tris.append(t + off)
        off += n
    if not verts:
        return np.zeros((0, 3)), np.zeros((0, 3), dtype=np.int64)
    return np.vstack(verts), np.vstack(tris)


def _merge(v, f, digits=6):
    if len(v) == 0:
        return v, f
    key = np.round(v, digits)
    uniq, inv = np.unique(key, axis=0, return_inverse=True)
    inv = inv.reshape(-1)
    f2 = inv[f]
    keep = (f2[:, 0] != f2[:, 1]) & (f2[:, 1] != f2[:, 2]) & (f2[:, 0] != f2[:, 2])
    return uniq.astype(float), f2[keep]


def solids_of(shape):
    try:
        sol = list(shape.solids())
    except Exception:  # noqa: BLE001
        sol = []
    return sol if sol else [shape]


def mesh_parts(shape, tol: float):
    """List of (vertices, faces) per solid of ``shape`` (unposed), cached."""
    k = id(shape)
    hit = _CACHE.get(k)
    if hit is not None and hit[0] is shape and hit[1] == tol:
        return hit[2]
    parts = []
    for s in solids_of(shape):
        v, f = _tess_face_arrays(s, tol)
        v, f = _merge(v, f)
        if len(f):
            parts.append((v, f))
    _CACHE[k] = (shape, tol, parts)
    return parts


def mesh(shape, tol: float):
    """One (vertices, faces) for the whole shape."""
    parts = mesh_parts(shape, tol)
    if not parts:
        return np.zeros((0, 3)), np.zeros((0, 3), dtype=np.int64)
    vs, fs, off = [], [], 0
    for v, f in parts:
        vs.append(v)
        fs.append(f + off)
        off += len(v)
    return np.vstack(vs), np.vstack(fs)


def transform(v, m):
    if m is None:
        return v
    return v @ m[:3, :3].T + m[:3, 3]


_MCACHE: dict[int, tuple] = {}


def manifold(shape, tol: float):
    """A manifold3d.Manifold of the shape (union of its solids), or None if any piece is not a valid volume."""
    import manifold3d as m3
    k = id(shape)
    hit = _MCACHE.get(k)
    if hit is not None and hit[0] is shape and hit[1] == tol:
        return hit[2]
    ms = []
    ok = True
    for v, f in mesh_parts(shape, tol):
        mm = m3.Manifold(m3.Mesh(vert_properties=np.asarray(v, np.float32), tri_verts=np.asarray(f, np.uint32)))
        if mm.status() != m3.Error.NoError or mm.is_empty():
            ok = False
            continue
        ms.append(mm)
    if not ms:
        res = None
    elif len(ms) == 1:
        res = ms[0]
    else:
        res = m3.Manifold.batch_boolean(ms, m3.OpType.Add)
    if not ok and res is not None:
        res = res  # keep the valid pieces; caller is told via .extra
    _MCACHE[k] = (shape, tol, res, ok)
    return res


def manifold_ok(shape, tol: float) -> bool:
    manifold(shape, tol)
    return _MCACHE[id(shape)][3]


def m3x4(m):
    """manifold3d wants a 3 x 4 affine matrix."""
    return np.asarray(m[:3, :], dtype=np.float64)
