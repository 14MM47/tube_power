"""Assemble the Lantern 330-G at a pose and export it (STEP, GLB, BOM).

Frames (SPEC section 1): p_A = R_x(theta) p_S and p_S = R_z(beta) p_P, so a
part in frame P is posed by R_x(theta) R_z(beta), one in frame S by
R_x(theta), and one in frame A not at all. The spring carriage and the belt
are rebuilt for each pose (``structure.carriage_items``, ``structure.belt_item``).
"""
from __future__ import annotations

import copy
import csv
import json
import math
from collections import OrderedDict
from pathlib import Path

import numpy as np

from . import layout as L
from . import mesh as meshmod
from . import printed as printedmod
from . import structure
from .item import Item
from .materials import LEGEND

_PRINTED_CACHE: dict = {}


def pose_matrix(frame: str, theta: float = 0.0, beta: float = 0.0) -> np.ndarray:
    """4 x 4 matrix taking frame coordinates (at rest) to frame A at (theta, beta)."""
    m = np.eye(4)
    if frame == "A":
        return m
    t = math.radians(theta)
    rx = np.array([[1, 0, 0], [0, math.cos(t), -math.sin(t)], [0, math.sin(t), math.cos(t)]])
    if frame == "S":
        m[:3, :3] = rx
        return m
    b = math.radians(beta)
    rz = np.array([[math.cos(b), -math.sin(b), 0], [math.sin(b), math.cos(b), 0], [0, 0, 1]])
    m[:3, :3] = rx @ rz
    return m


def pose_location(frame: str, theta: float = 0.0, beta: float = 0.0):
    from build123d import Rot
    if frame == "A":
        return None
    if frame == "S":
        return Rot(theta, 0, 0)
    return Rot(theta, 0, 0) * Rot(0, 0, beta)


def printed_items(include_placeholders: bool = True):
    key = include_placeholders
    if key not in _PRINTED_CACHE:
        _PRINTED_CACHE[key] = printedmod.load(include_placeholders)
    items, rep = _PRINTED_CACHE[key]
    return [it.copy() for it in items], rep


def collect(theta: float = 0.0, carriage_r: float = L.CARRIAGE_R_DEFAULT, include_printed: bool = True):
    """Unposed items for a pose: static structure, carriage and belt solved for theta, printed parts."""
    items = structure.static_items() + structure.carriage_items(carriage_r, theta)
    belt, binfo = structure.belt_item(theta)
    items.append(belt)
    prep = None
    if include_printed:
        p, prep = printed_items()
        items += p
    info = {"theta": theta, "carriage_r": carriage_r, "belt": binfo, "printed": prep}
    return items, info


def apply_pose(items: list[Item], theta: float, beta: float) -> list[Item]:
    out = []
    for it in items:
        m = pose_matrix(it.frame, theta, beta)
        loc = pose_location(it.frame, theta, beta)
        shp = it.shape if loc is None else loc * it.shape
        n = it.copy(shape=shp)
        n.extra = dict(it.extra, matrix=m, unposed=it.shape, theta=theta, beta=beta)
        out.append(n)
    return out


def build(theta_deg: float = 0.0, beta_deg: float = 0.0, carriage_r: float = L.CARRIAGE_R_DEFAULT,
          include_printed: bool = True) -> list[Item]:
    """The whole machine at a pose, as a list of posed Items."""
    items, info = collect(theta_deg, carriage_r, include_printed)
    posed = apply_pose(items, theta_deg, beta_deg)
    for it in posed:
        it.extra["build_info"] = info
    return posed


# ------------------------------------------------------------------- exports
def unique_labels(items: list[Item]) -> list[str]:
    seen: dict[str, int] = {}
    out = []
    for it in items:
        lab = it.label
        if lab in seen:
            seen[lab] += 1
            lab = f"{lab} ({seen[lab]})"
        else:
            seen[lab] = 1
        out.append(lab)
    return out


def export_step(items: list[Item], path) -> Path:
    """Assembly STEP: one named, coloured child per item."""
    from build123d import Color, Compound, export_step as _export
    path = Path(path)
    children = []
    for it, lab in zip(items, unique_labels(items)):
        child = copy.copy(it.shape)          # shallow: shares the OCC shape, own label and colour
        child.label = lab
        r, g, b = LEGEND[it.material_key].rgb
        child.color = Color(r, g, b, 0.45 if it.placeholder else 1.0)
        children.append(child)
    asm = Compound(children=children, label="Lantern 330-G")
    path.parent.mkdir(parents=True, exist_ok=True)
    _export(asm, str(path))
    return path


def item_mesh(it: Item, posed: bool = True):
    """(vertices, faces) of an item, posed by its matrix if it has one."""
    shp = it.extra.get("unposed", it.shape)
    v, f = meshmod.mesh(shp, it.tol)
    m = it.extra.get("matrix") if posed else None
    if m is not None and shp is not it.shape:
        v = meshmod.transform(v, m)
    return v, f


def item_meta(it: Item) -> dict:
    return {
        "id": it.id, "name": it.name, "tag": it.tag, "material_key": it.material_key,
        "material_label": it.mat_label, "printed": it.printed, "bought": it.bought,
        "frame": it.frame, "group": it.group, "placeholder": it.placeholder,
    }


def export_glb(items: list[Item], path) -> Path:
    """GLB with one node per item, PBR base colour from the legend, node extras with the metadata."""
    import trimesh
    from trimesh.visual.material import PBRMaterial
    path = Path(path)
    scene = trimesh.Scene()
    for it, lab in zip(items, unique_labels(items)):
        v, f = item_mesh(it)
        if len(f) == 0:
            continue
        r, g, b = LEGEND[it.material_key].rgb
        alpha = 0.45 if it.placeholder else 1.0
        mat = PBRMaterial(name=it.material_key, baseColorFactor=[r, g, b, alpha],
                          metallicFactor=0.6 if it.material_key in ("alu", "steel", "stainless", "bearing", "spring", "bronze") else 0.0,
                          roughnessFactor=0.5, alphaMode="BLEND" if it.placeholder else "OPAQUE",
                          doubleSided=False)
        tm = trimesh.Trimesh(vertices=v, faces=f, process=False)
        tm.visual = trimesh.visual.TextureVisuals(material=mat)
        scene.add_geometry(tm, node_name=lab, geom_name=lab, metadata=item_meta(it))
    path.parent.mkdir(parents=True, exist_ok=True)
    data = trimesh.exchange.gltf.export_glb(scene, include_normals=True)
    path.write_bytes(data)
    return path


def bom_rows(items: list[Item]) -> list[dict]:
    rows: "OrderedDict[tuple, dict]" = OrderedDict()
    masses: dict[str, float] = {}
    for it in items:
        if not it.bom:
            # inner rings etc.: add their mass to the parent line
            k = (it.id, it.name)
            masses[k] = masses.get(k, 0.0) + _mass(it)
            continue
        k = (it.id, it.name)
        if k not in rows:
            rows[k] = {"id": it.id, "name": it.name, "material": it.mat_label,
                       "material_key": it.material_key, "printed": "Y" if it.printed else "N",
                       "bought": "Y" if it.bought else "N", "qty": 0, "mass_g_each": 0.0,
                       "mass_g_total": 0.0, "frame": it.frame, "group": it.group,
                       "placeholder": "Y" if it.placeholder else "N", "note": it.note}
        rows[k]["qty"] += it.count
        rows[k]["mass_g_total"] += _mass(it)
    for k, extra in masses.items():
        if k in rows:
            rows[k]["mass_g_total"] += extra
    out = []
    for r in rows.values():
        r["mass_g_each"] = round(r["mass_g_total"] / max(r["qty"], 1), 1)
        r["mass_g_total"] = round(r["mass_g_total"], 1)
        out.append(r)
    return sorted(out, key=lambda r: (r["id"][0] != "P", r["id"][0] != "M", r["id"]))


def _mass(it: Item) -> float:
    try:
        vol = float(it.shape.volume)  # mm³
    except Exception:  # noqa: BLE001
        return 0.0
    return vol / 1000.0 * LEGEND[it.material_key].density


def mass_properties(items: list[Item]) -> dict:
    """Mass, centre of mass and inertia about the hinge axis (X through the origin) of the
    swinging parts (frames S and P), from the exact B-rep and the legend densities."""
    from OCP.BRepGProp import BRepGProp
    from OCP.GProp import GProp_GProps
    m_tot, mz, ixx = 0.0, 0.0, 0.0
    by_group: dict[str, float] = {}
    for it in items:
        if it.frame not in ("S", "P"):
            continue
        shp = it.extra.get("unposed", it.shape)
        rho = LEGEND[it.material_key].density / 1000.0          # g/mm³
        props = GProp_GProps()
        try:
            BRepGProp.VolumeProperties_s(shp.wrapped, props)
        except Exception:  # noqa: BLE001
            continue
        v = props.Mass()
        c = props.CentreOfMass()
        mi = props.MatrixOfInertia()
        m = v * rho
        m_tot += m
        mz += m * c.Z()
        ixx += (mi.Value(1, 1) + v * (c.Y() ** 2 + c.Z() ** 2)) * rho
        by_group[it.group] = by_group.get(it.group, 0.0) + m
    return {
        "swinging_mass_kg": round(m_tot / 1000.0, 3),
        "swinging_com_z_mm": round(mz / m_tot, 1) if m_tot else None,
        "swinging_inertia_about_hinge_kgm2": round(ixx * 1e-9, 4),
        "swinging_mass_by_group_kg": {k: round(v / 1000.0, 3) for k, v in sorted(by_group.items(), key=lambda kv: -kv[1])},
        "note": "theta = beta = 0; excludes the generator rotor reflected through the belt and the air moving with the prism",
    }


def export_bom(items: list[Item], csv_path, json_path) -> list[dict]:
    rows = bom_rows(items)
    csv_path, json_path = Path(csv_path), Path(json_path)
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    cols = ["id", "name", "material", "printed", "bought", "qty", "mass_g_each", "mass_g_total",
            "frame", "group", "placeholder", "note"]
    with open(csv_path, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow(r)
    totals = {
        "items": len(rows),
        "mass_g_all": round(sum(r["mass_g_total"] for r in rows), 1),
        "mass_g_printed": round(sum(r["mass_g_total"] for r in rows if r["printed"] == "Y"), 1),
    }
    totals.update(mass_properties(items))
    json_path.write_text(json.dumps({"rows": rows, "totals": totals}, indent=1))
    return rows
