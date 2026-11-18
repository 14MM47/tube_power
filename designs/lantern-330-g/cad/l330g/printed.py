"""Loader for the printed parts (P01..P25) from the 3dprint checkout.

For every ``parts/lantern330g/<module>.py`` whose name does not start with
``_``, the loader imports the module, takes the part as built by ``part()``
with its defaults (or the committed ``<module>.step`` when that file is newer
than the ``.py``), and places one copy per ``placements()`` entry in the
module's ``ASSEMBLY_FRAME`` (SPEC section 5).

A part whose module is missing, fails to import, fails to build or has no
placements is replaced by a translucent placeholder envelope at its SPEC
position (``PLACEHOLDERS`` below), flagged ``placeholder=True``, and the reason
is logged in ``LoadReport``.

The checkout is found from the environment variable ``LANTERN_3DPRINT``, else
it is the ``3dprint`` directory beside the ``tube_power`` repo.
"""
from __future__ import annotations

import hashlib
import importlib
import importlib.util
import math
import os
import re
import sys
import time
import traceback
from dataclasses import dataclass, field
from pathlib import Path

import numpy as np
from build123d import Location, Pos, Rot

from . import layout as L
from .geom import box, cyl_x, cyl_z, sector_prism_x, tube_x, tube_z
from .item import Item
from .materials import key_for_print_material

#: SPEC section 5 table: P-number -> (module, material key, qty, frame)
SPEC_TABLE = {
    "P01": ("neck_spider", "asa", 1, "P"),
    "P02": ("neck_top_collar", "asa", 1, "P"),
    "P03": ("belt_arc", "paht_cf", 1, "S"),
    "P04": ("belt_clamp", "paht_cf", 2, "S"),
    "P05": ("generator_mount", "paht_cf", 1, "A"),
    "P06": ("idler_bracket", "paht_cf", 1, "A"),
    "P07": ("gen_encoder_mount", "asa", 1, "A"),
    "P08": ("gen_magnet_holder", "asa", 1, "A"),
    "P09": ("belt_guard", "asa", 1, "A"),
    "P10": ("stepper_mount", "paht_cf", 1, "S"),
    "P11": ("pitch_gearmotor_bracket", "paht_cf", 1, "S"),
    "P12": ("pitch_encoder_mount", "asa", 1, "S"),
    "P13": ("pitch_magnet_holder", "asa", 1, "P"),
    "P14": ("hinge_encoder_mount", "asa", 1, "A"),
    "P15": ("hinge_magnet_cap", "asa", 1, "S"),
    "P16": ("end_stop_bumper", "tpu", 2, "A"),
    "P17": ("vane_clamp", "asa", 6, "A"),
    "P18": ("anemometer_tee", "asa", 1, "A"),
    "P19": ("anemometer_mount", "asa", 1, "A"),
    "P20": ("enclosure_base", "asa", 1, "A"),
    "P21": ("enclosure_lid", "asa", 1, "A"),
    "P22": ("enclosure_gasket", "tpu", 1, "A"),
    "P23": ("slip_ring_holder", "asa", 1, "A"),
    "P24": ("cable_clip", "asa", 3, "A"),
    "P25": ("latch_solenoid_cover", "asa", 1, "S"),
}
MODULE_TO_P = {v[0]: k for k, v in SPEC_TABLE.items()}

GROUPS = {
    "P01": "prism", "P02": "prism", "P03": "drive", "P04": "drive", "P05": "drive", "P06": "drive",
    "P07": "drive", "P08": "drive", "P09": "drive", "P10": "hub", "P11": "pitch", "P12": "pitch",
    "P13": "pitch", "P14": "hinge", "P15": "hinge", "P16": "hinge", "P17": "tail",
    "P18": "anemometer", "P19": "anemometer", "P20": "electrical", "P21": "electrical",
    "P22": "electrical", "P23": "yaw", "P24": "anemometer",
    "P25": "pitch",
}


def threedprint_root() -> Path:
    env = os.environ.get("LANTERN_3DPRINT")
    if env:
        return Path(env)
    return Path(__file__).resolve().parents[5] / "3dprint"


def parts_dir() -> Path:
    return threedprint_root() / "parts" / "lantern330g"


# ----------------------------------------------------------- placeholder envelopes
def _arc_pt(r, phi):
    a = math.radians(phi)
    return r * math.sin(a), -r * math.cos(a)


def _placeholder_shapes(pid: str) -> list:
    """Envelope shapes (already placed) for one SPEC P-number; one per copy."""
    if pid == "P01":
        s = tube_z(70, L.NECK_OD, (600, 690))
        for a in (45, 135, 225, 315):
            s = s + Pos(0, 0, 0) * Rot(0, 0, a) * box((34, 140), (-8, 8), (600, 612))
        return [s - cyl_z(L.NECK_OD, (590, 700))]
    if pid == "P02":
        s = tube_z(60, L.NECK_OD, (790, 845)) + tube_z(140, L.NECK_OD, (842, 845)) \
            + tube_z(L.BULKHEAD_HOLE_D, L.NECK_OD, (845, 850)) + cyl_z(L.BULKHEAD_HOLE_D, (850, 855))
        return [s]
    if pid == "P03":
        rim_in = L.ARC_PITCH_R - L.GT2_PLD
        rim = sector_prism_x(94.0, rim_in, -L.ARC_SECTOR, L.ARC_SECTOR, L.BELT_X)
        web = sector_prism_x(30.0, 94.0, -L.ARC_SECTOR, L.ARC_SECTOR, L.ARC_WEB_X)
        tab = box(L.ARC_WEB_X, L.HANGER_Y, (-45.0, 12.0))
        return [rim + web + tab]
    if pid == "P04":
        out = []
        r0 = L.ARC_PITCH_R + 0.376
        for phi in (40.0, -40.0):
            b = box((80.0, 95.0), (-10, 10), (-(r0 + 3.0), -r0))
            out.append(Rot(phi, 0, 0) * b)
        return out
    if pid == "P05":
        gy, gz = L.GEN_AXIS_YZ
        s = box(L.P05_UPRIGHT_X, (-50, 50), (-280, -70)) + box((15, 43), (-50, 50), (-280, -272))
        return [s - cyl_x(22.0, (30, 50), gy, gz)]
    if pid == "P06":
        s = box(L.P06_UPRIGHT_X, (-45, 45), (-280, -95)) - cyl_x(2 * L.P06_TOP_R_MIN, (90, 105))
        return [s]
    if pid == "P07":
        gy, gz = L.GEN_AXIS_YZ
        s = box((26, 35), (gy - 20, gy + 20), (gz - 20, gz + 20)) - box((28, 36), (gy - 16, gy + 16), (gz - 16, gz + 16))
        return [s]
    if pid == "P08":
        gy, gz = L.GEN_AXIS_YZ
        s = cyl_x(12, (L.GEN_MAGNET_FACE_X, 42), gy, gz) - cyl_x(5, (L.GEN_REAR_SHAFT_END_X, 43), gy, gz) \
            - cyl_x(6, (L.GEN_MAGNET_FACE_X - 1, L.GEN_MAGNET_FACE_X + L.MAGNET[1]), gy, gz)
        return [s]
    if pid == "P09":
        # band over the arc's sweep, open where the belt runs down to the idlers and pulley
        s = sector_prism_x(L.P09_R_MAX, L.P09_R_MAX + 3, 25.0, L.P09_HALF_ANGLE, (78, 92)) + \
            sector_prism_x(L.P09_R_MAX, L.P09_R_MAX + 3, -L.P09_HALF_ANGLE, -25.0, (78, 92))
        return [s]
    if pid == "P10":
        s = box((-126, -71), (-24, 24), (-205, -199)) - cyl_z(24, (-210, -190), *L.STEPPER_XY)
        s = s + box((-79, -71), (-20, 20), (-215, -199))
        return [s]
    if pid == "P11":
        wy, wz = L.WORM_AXIS_YZ
        s = box((38, 62), (wy - 22, wy + 22), (wz - 20, wz + 20)) - cyl_z(L.PITCH_HOUSING_OD, (130, 190)) \
            - cyl_x(12, (30, 70), wy, wz)
        s = s + tube_x(33, L.GEARBOX_D, (62, 80), wy, wz)
        return [s]
    if pid == "P12":
        z1 = L.PITCH_ENCODER_IC_TOP_Z - 1.0 - L.ENCODER_PCB[2]
        return [box((-16, 16), (-16, 16), (L.HUB_TOP_Z[1], z1)) - box((-10, 10), (-10, 10), (30, 45))]
    if pid == "P13":
        z = L.PITCH_MAGNET_FACE_Z
        return [cyl_z(L.PITCH_SHAFT_BORE_D, (z, L.PITCH_SHAFT_Z[0] + L.PITCH_SHAFT_BORE_DEPTH))
                - cyl_z(L.MAGNET[0], (z - 1, z + L.MAGNET[1]))]
    if pid == "P14":
        x0 = L.RETAINER_X[0]
        return [cyl_x(L.RETAINER_OD, (-190, -L.RETAINER_X[1])) - cyl_x(56, (-186, -L.RETAINER_X[1] + 1))]
    if pid == "P15":
        return [cyl_x(L.P15_D, L.P15_X) - cyl_x(L.MAGNET[0], (L.P15_X[0] - 1, L.HINGE_MAGNET_FACE_X + L.MAGNET[1]))]
    if pid == "P16":
        return [box(L.BUMPER_X, sorted((s * L.BUMPER_Y[0], s * L.BUMPER_Y[1])), L.BUMPER_Z) for s in (1, -1)]
    if pid == "P17":
        out = []
        ty, tz = L.TAIL_BOOM_YZ
        for x in L.VANE_CLAMP_X:
            for s in (1, -1):
                b = box((x - 15, x + 15), sorted((s * L.VANE_T / 2, s * 26)), (tz - 30, tz + 30)) \
                    - cyl_x(L.TAIL_BOOM_OD, (x - 20, x + 20), ty, tz)
                out.append(b)
        return out
    if pid == "P18":
        x, y, z = L.ANEMO_TEE
        st = L.TEE_SOCKET_STOP
        s = box((x - 22, x + st + 20), (y - 18, y + 18), (z - 18, z + st + 20)) \
            - cyl_x(L.ANEMO_BOOM_OD, (x + st, x + st + 21), y, z) - cyl_z(L.ANEMO_BOOM_OD, (z + st, z + st + 21), x, y)
        return [s]
    if pid == "P19":
        x, y = L.ANEMO_MAST_XY
        zt = L.ANEMO_MAST_TOP_Z
        s = cyl_z(34, (zt - 25, L.ANEMO_BODY_BOTTOM_Z), x, y) - cyl_z(L.ANEMO_BOOM_OD, (zt - 26, zt), x, y) \
            - cyl_z(L.ANEMO_SPIGOT[0], (zt - 1, L.ANEMO_BODY_BOTTOM_Z + 1), x, y)
        return [s]
    if pid == "P20":
        x0, x1 = L.ENCL_X
        y0, y1 = L.ENCL_Y
        w = L.ENCL_WALL_T
        zt = -225.0
        s = box(L.ENCL_X, L.ENCL_Y, (L.ENCL_Z[0], zt)) - box((x0 + w, x1 - w), (y0 + w, y1 - w), (L.ENCL_FLOOR_TOP_Z, zt + 1))
        cx, cy = L.PCB_CENTRE_XY
        bx0, by0 = cx - L.PCB_W / 2, cy - L.PCB_H / 2
        for hx, hy in L.PCB_HOLES:
            s = s + tube_z(7.0, 2.5, (L.ENCL_FLOOR_TOP_Z, L.PCB_BOTTOM_Z), bx0 + hx, by0 + hy)
        from .geom import cyl_y
        for gx in L.GLAND_M20_X:
            s = s - cyl_y(L.GLAND_M20[0], (y0 - 1, y0 + w + 1), gx, L.GLAND_Z)
        for gx in L.GLAND_M16_X:
            s = s - cyl_y(L.GLAND_M16[0], (y1 - w - 1, y1 + 1), gx, L.GLAND_Z)
        s = s - cyl_x(12.5, (x0 - 1, x0 + w + 1), *L.GLAND_VENT_YZ)
        return [s]
    if pid == "P21":
        x0, x1 = L.ENCL_X
        y0, y1 = L.ENCL_Y
        w = L.ENCL_WALL_T
        return [box(L.ENCL_X, L.ENCL_Y, (-225.0, L.ENCL_Z[1])) - box((x0 + w, x1 - w), (y0 + w, y1 - w), (-226.0, L.ENCL_Z[1] - 3))]
    if pid == "P22":
        x0, x1 = L.ENCL_X
        y0, y1 = L.ENCL_Y
        w = L.ENCL_WALL_T
        return [box((x0 + 0.5, x1 - 0.5), (y0 + 0.5, y1 - 0.5), (-225.0, -224.0))
                - box((x0 + w - 0.5, x1 - w + 0.5), (y0 + w - 0.5, y1 - w + 0.5), (-226.0, -223.0))]
    if pid == "P23":
        z0, z1 = L.P23_Z
        return [tube_z(L.POST_BORE, 46, (z0, -692.0)) + tube_z(L.POST_BORE, 94, (-692.0, -645.0))]
    if pid == "P24":
        ay, az = L.ANEMO_BOOM_YZ
        r = L.ANEMO_BOOM_OD / 2
        out = [box((x - 8, x + 8), (ay - 8, ay + 8), (az + r, az + r + 7)) for x in L.CABLE_CLIP_BOOM_X]
        mx, my = L.ANEMO_MAST_XY
        z = L.CABLE_CLIP_MAST_Z
        out.append(box((mx + r, mx + r + 7), (my - 8, my + 8), (z - 8, z + 8)))
        return out
    if pid == "P25":
        (x0, x1), (y0, y1), (z0, z1), w = L.P25_ENVELOPE
        shell = box((x0, x1), (y0, y1), (z0, z1)) - box((x0 + w, x1 + 1), (y0 + w, y1 - w), (z0 + w, z1 - w))
        return [shell - cyl_z(L.PITCH_HOUSING_OD, (z0 - 1, z1 + 1))]
    raise KeyError(pid)


def placeholder_items(pid: str, reason: str) -> list[Item]:
    mod, mat, qty, frame = SPEC_TABLE[pid]
    shapes = _placeholder_shapes(pid)
    out = []
    for k, s in enumerate(shapes):
        tag = f"#{k + 1}" if len(shapes) > 1 else ""
        out.append(Item(id=pid, name=mod, shape=s, material_key=mat, frame=frame, printed=True,
                        group=GROUPS[pid], tag=tag, placeholder=True, module=mod, tol=0.1,
                        note=f"placeholder envelope: {reason}"))
    return out


# ------------------------------------------------------------------- loading
@dataclass
class LoadReport:
    root: str = ""
    loaded: list[dict] = field(default_factory=list)
    placeholders: list[dict] = field(default_factory=list)
    log: list[str] = field(default_factory=list)


def _import_module(path: Path):
    root = threedprint_root()
    if str(root) not in sys.path:
        sys.path.insert(0, str(root))
    name = f"parts.lantern330g.{path.stem}"
    try:
        if name in sys.modules:
            return importlib.reload(sys.modules[name])
        return importlib.import_module(name)
    except ModuleNotFoundError as e:
        if not str(e.name or "").startswith("parts"):
            raise
    spec = importlib.util.spec_from_file_location(f"l330g_printed_{path.stem}", path)
    mod = importlib.util.module_from_spec(spec)
    sys.path.insert(0, str(path.parent))
    try:
        spec.loader.exec_module(mod)
    finally:
        sys.path.remove(str(path.parent))
    return mod


def _pid_from(mod, stem: str) -> str | None:
    doc = (mod.__doc__ or "").strip()
    head = "\n".join(doc.splitlines()[:3])
    m = re.search(r"\bP(\d{2})\b", head)
    if m:
        return "P" + m.group(1)
    return MODULE_TO_P.get(stem)


def _as_location(p) -> Location:
    if isinstance(p, Location):
        return p
    if hasattr(p, "location") and isinstance(p.location, Location):
        return p.location
    a = np.asarray(p, dtype=float)
    if a.shape == (4, 4):
        from OCP.gp import gp_Trsf
        t = gp_Trsf()
        t.SetValues(*a[0], *a[1], *a[2])
        return Location(t)
    if a.shape == (3,):
        return Location(tuple(a))
    if isinstance(p, (tuple, list)) and len(p) == 2:
        return Location(tuple(p[0]), tuple(p[1]))
    raise TypeError(f"cannot read a placement from {type(p).__name__}")


def _cache_dir() -> Path:
    d = Path(__file__).resolve().parents[1] / "out" / ".cache" / "printed"
    d.mkdir(parents=True, exist_ok=True)
    return d


def _build_shape(mod, py: Path, report: LoadReport):
    """part() with defaults, or the committed STEP when it is newer than the .py."""
    from build123d import export_brep, import_brep, import_step
    step = py.with_suffix(".step")
    if step.exists() and step.stat().st_mtime >= py.stat().st_mtime:
        return import_step(str(step)), f"STEP {step.name}"
    h = hashlib.sha1(py.read_bytes()).hexdigest()[:12]
    lib = py.parent / "_lib"
    if lib.exists():
        for f in sorted(lib.glob("*.py")):
            h = hashlib.sha1((h + f.read_text()).encode()).hexdigest()[:12]
    cache = _cache_dir() / f"{py.stem}-{h}.brep"
    if cache.exists():
        return import_brep(str(cache)), f"part() (cached {cache.name})"
    t = time.time()
    shp = mod.part()
    if hasattr(shp, "part") and not hasattr(shp, "wrapped"):
        shp = shp.part
    try:
        export_brep(shp, str(cache))
    except Exception:  # noqa: BLE001
        pass
    return shp, f"part() built in {time.time() - t:.1f} s"


def load(include_placeholders: bool = True) -> tuple[list[Item], LoadReport]:
    """All printed parts as placed Items (frame coordinates at theta = beta = 0)."""
    rep = LoadReport(root=str(threedprint_root()))
    items: list[Item] = []
    found: set[str] = set()
    d = parts_dir()
    mods = sorted(p for p in d.glob("*.py") if not p.name.startswith("_")) if d.exists() else []
    for py in mods:
        stem = py.stem
        try:
            mod = _import_module(py)
        except Exception as e:  # noqa: BLE001
            rep.log.append(f"{stem}: import failed: {e!r}")
            pid = MODULE_TO_P.get(stem)
            if pid:
                rep.placeholders.append({"id": pid, "module": stem, "reason": f"import failed: {e!r}"})
                found.add(pid)
                if include_placeholders:
                    items += placeholder_items(pid, "import failed")
            continue
        pid = _pid_from(mod, stem)
        if pid is None or pid not in SPEC_TABLE:
            rep.log.append(f"{stem}: not a SPEC section 5 part; skipped")
            continue
        found.add(pid)
        try:
            frame = getattr(mod, "ASSEMBLY_FRAME", SPEC_TABLE[pid][3])
            frame = str(frame).strip().upper()[:1]
            mat = key_for_print_material(getattr(mod, "PRINT", {}).get("material", SPEC_TABLE[pid][1]))
            shp, how = _build_shape(mod, py, rep)
            if not hasattr(mod, "placements"):
                raise AttributeError("module has no placements()")
            locs = [_as_location(p) for p in mod.placements()]
            if not locs:
                raise ValueError("placements() returned nothing")
            for k, loc in enumerate(locs):
                tag = f"#{k + 1}" if len(locs) > 1 else ""
                items.append(Item(id=pid, name=stem, shape=loc * shp, material_key=mat, frame=frame,
                                  printed=True, group=GROUPS.get(pid, "printed"), tag=tag, module=stem,
                                  tol=0.05, note=how))
            rep.loaded.append({"id": pid, "module": stem, "copies": len(locs), "frame": frame,
                               "material": mat, "source": how})
            if len(locs) != SPEC_TABLE[pid][2]:
                rep.log.append(f"{stem}: {len(locs)} placements, SPEC qty {SPEC_TABLE[pid][2]}")
        except Exception:  # noqa: BLE001
            tb = traceback.format_exc(limit=2).strip().splitlines()[-1]
            rep.log.append(f"{stem}: build failed: {tb}")
            rep.placeholders.append({"id": pid, "module": stem, "reason": f"build failed: {tb}"})
            if include_placeholders:
                items += placeholder_items(pid, "build failed")
    for pid, (mod, _, _, _) in SPEC_TABLE.items():
        if pid not in found:
            rep.placeholders.append({"id": pid, "module": mod, "reason": "module not written yet"})
            if include_placeholders:
                items += placeholder_items(pid, "module not written yet")
    return items, rep
