"""Interference and clearance checks at the SPEC poses.

For each pose in SPEC section 1 the checker poses every item, prefilters
pairs by bounding box, and measures each candidate pair's overlap volume on
meshes with manifold3d. A pair that overlaps by more than ``OVERLAP_MM3`` and
is not an intended contact (``ALLOW``) is confirmed with an exact OCC boolean
on the B-rep; only an exact overlap above the limit is reported as an
interference (mesh chords make equal-diameter fits look like slivers).

Pairs checked:

- ``swing``: a frame-S or frame-P part against a frame-A part (every pose);
- ``pitch``: a frame-P part against a frame-S part (every pose);
- ``carriage``: a part on the spring carriage against the rest of frame S
  (every pose; the carriage also moves along the lever);
- ``carriage_internal``: parts riding together on the carriage (every pose,
  overlap only: the forks and springs are re-solved for each swing);
- ``belt``: the belt (rebuilt per pose) against frame-A parts (every pose);
- ``static``: parts in the same frame that do not move relative to each
  other (the first pose only).

Clearances: every moving pair closer than ``CLEARANCE_MIN`` (3 mm, SPEC 4)
is listed, with the intended running gaps marked; and the SPEC 4 named pairs
are measured with exact B-rep distances.
"""
from __future__ import annotations

import json
import re
import time
from dataclasses import dataclass
from pathlib import Path

import numpy as np

from . import assembly
from . import printed
from . import layout as L
from . import mesh as meshmod
from .item import Item

OVERLAP_MM3 = 1.0


@dataclass(frozen=True)
class Rule:
    a: str
    b: str
    reason: str

    def match(self, ia: Item, ib: Item) -> bool:
        la, lb = _key(ia), _key(ib)
        return (re.search(self.a, la) and re.search(self.b, lb)) or \
            (re.search(self.a, lb) and re.search(self.b, la))


def _key(it: Item) -> str:
    return f"{it.id} {it.name} {it.tag}"


#: Intended contacts and nested fits: overlap allowed, with the reason.
ALLOW = [
    Rule(r"^B19 ", r"^P03 ", "belt teeth in the arc's toothed rim (belt drawn as a plain 1.38 mm band)"),
    Rule(r"^B19 ", r"^P04 ", "belt end clamped under its clamp"),
    Rule(r"^B19 ", r"^B20 ", "belt teeth in the pulley grooves (belt drawn as a plain band)"),
    Rule(r"^B19 ", r"^B21 ", "belt back on the idler (rolling contact)"),
    Rule(r"^B03 ", r"^B04 ", "worm in mesh with the worm wheel"),
    Rule(r"^P13 ", r"^M08 ", "magnet holder pressed into the pitch shaft's end bore"),
    Rule(r"^B09 .*pitch", r"^P13 ", "magnet in its holder"),
    Rule(r"^B09 .*generator", r"^P08 ", "magnet in its holder"),
    Rule(r"^B09 .*hinge", r"^P15 ", "magnet in its cap"),
    Rule(r"^B08 .*pitch", r"^P12 ", "encoder board on its stand"),
    Rule(r"^B08 .*generator", r"^P07 ", "encoder board in its mount"),
    Rule(r"^B08 .*hinge", r"^P14 ", "encoder board in its cup"),
    Rule(r"^M07 ", r"^P0[12] ", "neck bonded in its socket"),
    Rule(r"^M0[35] ", r"^P0[12] ", "spider bonded to the bottom end plate; collar bonded to bulkhead 1"),
    Rule(r"^B07 ", r"^P11 ", "gearmotor clamped in its bracket"),
    Rule(r"^M15 ", r"^P11 ", "bracket saddle on the pitch housing over the window"),
    Rule(r"^B04 ", r"^P11 ", "worm shaft in the bracket's F695 bearing"),
    Rule(r"^B15 |^M19 ", r"^P10 ", "stepper and its mount bolted to the lever"),
    Rule(r"^B22 ", r"^P06 ", "idler bolt in the bracket's insert"),
    Rule(r"^B23 ", r"^P0[58] ", "generator bolted to its mount; magnet holder on its rear shaft"),
    Rule(r"^P05 ", r"^P07 ", "encoder mount clamped to the generator mount"),
    Rule(r"^M31 ", r"^P16 ", "bumper on its stop post"),
    Rule(r"^M4[123] ", r"^P17 ", "vane and boom clamped by the vane clamps"),
    Rule(r"^M4[45] ", r"^P1[89] |^P24 ", "tube in its socket or clip"),
    Rule(r"^B29 ", r"^P19 |^M45 ", "anemometer spigot in its mount and the mast bore"),
    Rule(r"^P23 ", r"^M38 |^B27 ", "holder in the post bore; slip ring in its holder"),
    Rule(r"^B3[234] ", r"^P2[012] ", "cable gland through its wall hole"),
    Rule(r"^M4[78] ", r"^P20 ", "PCB on the enclosure bosses"),
    Rule(r"^P2[012] ", r"^P2[012] ", "enclosure base, lid and gasket"),
    Rule(r"^P2[01] ", r"^M32 ", "enclosure on the base plate"),
    Rule(r"^P09 ", r"^P0[56] ", "guard fixed to the generator mount and idler bracket"),
    Rule(r"^P03 ", r"^M26 |^P04 ", "arc web bolted to the hanger; clamps bolted to the arc"),
    Rule(r"^P14 ", r"^M28 ", "cup bolted to the retainer"),
    Rule(r"^P15 ", r"^M12 ", "cap on the stub axle's end face"),
    Rule(r"^B18 ", r"^M29 ", "roller on its reaction plate (rolling contact)"),
    Rule(r"^P12 ", r"^M10 ", "stand on the hub top plate"),
    Rule(r"^P0[56] ", r"^M32 ", "upright's foot on the base plate"),
    Rule(r"^M62 ", r"^M15 ", "latch stem guide bush pressed into the housing wall"),
    Rule(r"^M61 ", r"^M58 |^B42 |^B06 |^M62 ", "trip stem: M4 end in the hook bridge, nuts on its M6 thread, end in the plunger, in its guide"),
    Rule(r"^M64 ", r"^B44 ", "feathered: the stop lug presses into the PU buffer (beta 42..48)"),
]

#: Moving pairs allowed closer than 3 mm (SPEC 4), with the reason.
NEAR = ALLOW + [
    Rule(r"^B01 ", r"^M28 ", "hinge nut to fixed retainer: 1 mm running gap (DEVIATION D2)"),
    Rule(r"^M1[24] ", r"^M28 ", "axle and spacer through the retainer bore: labyrinth gap"),
    Rule(r"^M1[234] |^B01 |^B24 .*inner", r"^B24 |^M27 ", "hinge bearing: inner and outer rings"),
    Rule(r"^B09 .*hinge", r"^B08 .*hinge|^P14 ", "encoder air gap 1.5 mm (SPEC 6)"),
    Rule(r"^B09 .*pitch|^P13 ", r"^B08 .*pitch|^P12 ", "encoder air gap 1.5 mm (SPEC 6)"),
    Rule(r"^P15 ", r"^P14 |^B08 .*hinge", "magnet cap inside the encoder cup"),
    Rule(r"^B02 |^M09 |^M08 ", r"^B02 |^M1[67] ", "pitch bearing rings, spacer and housing"),
    Rule(r"^M24 ", r"^M29 ", "fork 3 mm from the reaction plate at the roller"),
    Rule(r"^M25 ", r"^P16 ", "striker lands on the bumpers at theta = +/-20 (SPEC 3.5)"),
    Rule(r"^P0[34] ", r"^B21 ", "arc rim to idler flanges: >= 0.3 mm axially (SPEC 4)"),
    Rule(r"^P0[34] ", r"^P09 ", "arc and clamps inside the guard"),
    Rule(r"^B03 |^M51 ", r"^B04 |^P11 ", "worm drive"),
    Rule(r"^B40 |^M53 ", r"^M58 ", "trip hook 1.5 +/- 0.2 mm outside the tab roller (latch.md 5; least gaps in latch_check)"),
    Rule(r"^M51 ", r"^M57 ", "carrier lug passes the wheel-stop blocks (lands on them only at wheel -7 / +50 deg)"),
    Rule(r"^M64 ", r"^M65 |^B44 ", "feather-stop lug between its blocks: lands on them at beta -3 and on the buffer from +42"),
    Rule(r"^M52 ", r"^M15 ", "pawl tail 2.2 mm inside the housing wall (latch.md 5)"),
    Rule(r"^M5[46] |^M60 ", r"^M58 ", "hook bridge 3 mm over the latch top plate and pin heads"),
    Rule(r"^B19 ", r"^P0[349] ", "belt on the arc"),
    Rule(r"^B13 ", r"^M21 |^B12 ", "lead screw through the carriage's clearance bore and its nut"),
    Rule(r"^M08 ", r"^B08 .*pitch", "encoder board under the shaft end: IC top Z 42.5, shaft end Z 45 (SPEC 3.2, 3.3)"),
    Rule(r"^B10 ", r"^B11 |^M22 ", "linear block on its rail"),
    Rule(r"^M19 ", r"^M2[12] |^B11 ", "carriage runs beside the lever"),
]


def _rule_for(rules, a: Item, b: Item):
    for r in rules:
        if r.match(a, b):
            return r
    return None


def _pair_category(a: Item, b: Item) -> str | None:
    fa, fb = a.frame, b.frame
    if {fa, fb} == {"A", "S"} or {fa, fb} == {"A", "P"}:
        return "swing"
    if {fa, fb} == {"S", "P"}:
        return "pitch"
    if fa == fb == "S" and a.carriage and b.carriage:
        return "carriage_internal"
    if fa == fb == "S" and (a.carriage or b.carriage):
        return "carriage"
    if fa == fb == "A" and (a.pose_dependent or b.pose_dependent):
        return "belt"
    if fa == fb:
        return "static"
    return None


@dataclass
class _Posed:
    it: Item
    m: np.ndarray
    lo: np.ndarray
    hi: np.ndarray
    man: object


def _pose_items(items: list[Item], theta: float, beta: float) -> list[_Posed]:
    out = []
    for it in items:
        m = assembly.pose_matrix(it.frame, theta, beta)
        v, f = meshmod.mesh(it.shape, it.tol)
        if len(v) == 0:
            continue
        pv = meshmod.transform(v, m)
        man = meshmod.manifold(it.shape, it.tol)
        out.append(_Posed(it, m, pv.min(0), pv.max(0), man))
    return out


def _overlap_mesh(pa: _Posed, pb: _Posed) -> float | None:
    if pa.man is None or pb.man is None:
        return None
    a = pa.man.transform(meshmod.m3x4(pa.m))
    b = pb.man.transform(meshmod.m3x4(pb.m))
    return float((a ^ b).volume())


def _posed_shape(it: Item, theta: float, beta: float):
    loc = assembly.pose_location(it.frame, theta, beta)
    return it.shape if loc is None else loc * it.shape


def exact_overlap(a: Item, b: Item, theta: float, beta: float) -> float | None:
    """Exact common volume of two posed items (OCC boolean), or None if OCC fails."""
    from OCP.BRepAlgoAPI import BRepAlgoAPI_Common
    from OCP.BRepGProp import BRepGProp
    from OCP.GProp import GProp_GProps
    try:
        sa, sb = _posed_shape(a, theta, beta), _posed_shape(b, theta, beta)
        op = BRepAlgoAPI_Common(sa.wrapped, sb.wrapped)
        op.Build()
        if not op.IsDone():
            return None
        props = GProp_GProps()
        BRepGProp.VolumeProperties_s(op.Shape(), props)
        return abs(float(props.Mass()))
    except Exception:  # noqa: BLE001
        return None


def exact_distance(a, b) -> float | None:
    try:
        return float(a.distance_to(b))
    except Exception:  # noqa: BLE001
        return None


def _gap_mesh(pa: _Posed, pb: _Posed, search: float) -> float | None:
    if pa.man is None or pb.man is None:
        return None
    a = pa.man.transform(meshmod.m3x4(pa.m))
    b = pb.man.transform(meshmod.m3x4(pb.m))
    try:
        return float(a.min_gap(b, search))
    except Exception:  # noqa: BLE001
        return None


def check_pose(items: list[Item], theta: float, beta: float, *, static: bool,
               exact_budget_s: float = 40.0, clearance: bool = True) -> dict:
    t0 = time.time()
    posed = _pose_items(items, theta, beta)
    n = len(posed)
    lo = np.array([p.lo for p in posed])
    hi = np.array([p.hi for p in posed])
    marg = L.CLEARANCE_MIN if clearance else 0.0
    ov = np.all((lo[:, None, :] <= hi[None, :, :] + marg) & (hi[:, None, :] >= lo[None, :, :] - marg), axis=2)
    ii, jj = np.nonzero(np.triu(ov, 1))
    interferences, allowed, placeholder_hits, close = [], [], [], []
    exact_used = 0.0
    n_pairs = 0
    for i, j in zip(ii.tolist(), jj.tolist()):
        pa, pb = posed[i], posed[j]
        a, b = pa.it, pb.it
        cat = _pair_category(a, b)
        if cat is None or (cat == "static" and not static):
            continue
        box_overlap = bool(np.all((pa.lo <= pb.hi) & (pa.hi >= pb.lo)))
        rec = {"a": a.label, "b": b.label, "frames": f"{a.frame}/{b.frame}", "category": cat}
        if box_overlap:
            n_pairs += 1
            vol = _overlap_mesh(pa, pb)
            if vol is None or vol > OVERLAP_MM3:
                rec["mesh_mm3"] = None if vol is None else round(vol, 2)
                rule = _rule_for(ALLOW, a, b)
                if rule is not None:
                    rec["reason"] = rule.reason
                    allowed.append(rec)
                    continue
                ex = None
                if exact_used < exact_budget_s:
                    t = time.time()
                    ex = exact_overlap(a, b, theta, beta)
                    exact_used += time.time() - t
                rec["exact_mm3"] = None if ex is None else round(ex, 2)
                if ex is not None and ex <= OVERLAP_MM3:
                    continue
                if a.placeholder or b.placeholder:
                    placeholder_hits.append(rec)
                else:
                    interferences.append(rec)
                continue
        if clearance and cat in ("swing", "pitch", "carriage"):
            gap = _gap_mesh(pa, pb, L.CLEARANCE_MIN)
            if gap is not None and gap < L.CLEARANCE_MIN - 1e-6:
                rule = _rule_for(NEAR, a, b)
                rec["gap_mesh"] = round(gap, 2)
                rec["intended"] = rule.reason if rule else None
                rec["placeholder"] = a.placeholder or b.placeholder
                close.append(rec)
    return {
        "theta": theta, "beta": beta, "items": n, "pairs_tested": n_pairs,
        "interferences": interferences, "allowed": allowed, "placeholder_overlaps": placeholder_hits,
        "close": close, "seconds": round(time.time() - t0, 1),
    }


# ------------------------------------------------------- SPEC 4 named pairs
def _sel(items, pattern):
    return [it for it in items if re.search(pattern, _key(it))]


def _probe_can():
    from .geom import cyl_x
    gy, gz = L.GEN_AXIS_YZ
    return Item("probe", "Generator can (probe)", cyl_x(L.GEN_CAN_D, L.GEN_CAN_X, gy, gz), "bought_elec", "A")


NAMED = [
    # name, selector a, selector b, designed value text, kind, minimum required (or None)
    ("Spring carriage / hub side plate -X", r"^M21 ", r"^M11 .*-X", "8 mm", "carriage_r", 8.0),
    ("Carriage spring OD / -X hub side plate", r"^B17 ", r"^M11 .*-X", "6.5 mm", "carriage_r", 6.5),
    ("Reaction plate / spring roller", r"^B18 ", r"^M29 ", "contact (rolling)", "poses", 0.0),
    ("Stepper / reaction plate", r"^B15 ", r"^M29 ", "44 mm at theta 20", "poses", 40.0),
    ("Belt arc / idler bracket P06 (whole parts)", r"^P03 ", r"^P06 ",
     ">= 16 mm web to P06 radially; the rim corner (X 89.5, R 99.7) is ~10.9 from P06 by the SPEC numbers", "poses", 3.0),
    ("Belt arc rim / idler flanges", r"^P03 ", r"^B21 ", ">= 0.3 mm axially", "poses", 0.3),
    ("Hanger / P06 top", r"^M26 ", r"^P06 ", ">= 48 mm", "poses", 48.0),
    ("Generator can / belt", "probe:can", r"^B19 ", "3 mm", "poses", 3.0),
    ("Striker / bumpers P16", r"^M25 ", r"^P16 ", "touch at theta +/-20 only", "poses", None),
    ("Striker / stop posts", r"^M25 ", r"^M31 ", ">= 3 mm", "poses", 3.0),
    ("Gearmotor / cheeks", r"^B07 ", r"^M27 ", ">= 75 mm (SPEC 4; the SPEC geometry gives 76.9 at theta -20)", "poses", 75.0),
    ("Prism panels / anemometer mast", r"^M0[12] ", r"^M45 ", "> 400 mm", "poses", 400.0),
    ("End plates / anemometer and mast", r"^M0[56] ", r"^M45 |^B29 ", "(not in SPEC 4)", "poses", None),
]


def named_clearances(poses=None, include_printed=True) -> list[dict]:
    poses = poses or L.POSES
    out = []
    cache = {}

    def items_at(theta, r):
        k = (theta, r)
        if k not in cache:
            cache[k] = assembly.collect(theta, r, include_printed)[0]
        return cache[k]

    for name, sa, sb, designed, kind, req in NAMED:
        runs = []
        if kind == "carriage_r":
            cases = [(0.0, 0.0, r) for r in (L.CARRIAGE_R_RANGE[0], L.CARRIAGE_R_DEFAULT, L.CARRIAGE_R_RANGE[1])]
        else:
            cases = [(t, b, L.CARRIAGE_R_DEFAULT) for t, b in poses]
        missing = None
        for theta, beta, r in cases:
            its = items_at(theta, r)
            A = [_probe_can()] if sa == "probe:can" else _sel(its, sa)
            B = _sel(its, sb)
            if not A or not B:
                missing = sa if not A else sb
                break
            best = None
            for a in A:
                pa = _posed_shape(a, theta, beta)
                for b in B:
                    d = exact_distance(pa, _posed_shape(b, theta, beta))
                    if d is not None and (best is None or d < best[0]):
                        best = (d, a.label, b.label)
            if best:
                runs.append({"theta": theta, "beta": beta, "carriage_r": r, "distance": round(best[0], 2),
                             "a": best[1], "b": best[2],
                             "placeholder": any(x.placeholder for x in A + B)})
        if missing or not runs:
            out.append({"pair": name, "designed": designed, "status": "not measured",
                        "detail": f"no item matches {missing}"})
            continue
        worst = min(runs, key=lambda r: r["distance"])
        status = "info"
        if req is not None:
            status = "ok" if worst["distance"] >= req - 0.05 else "BELOW"
        if name.startswith("Striker / bumpers"):
            at_stop = [r for r in runs if abs(abs(r["theta"]) - L.THETA_STOP) < 1e-6]
            others = [r for r in runs if abs(abs(r["theta"]) - L.THETA_STOP) >= 1e-6]
            ok = all(r["distance"] < 1.0 for r in at_stop) and all(r["distance"] >= L.CLEARANCE_MIN for r in others)
            status = "ok" if ok else "CHECK"
        if worst.get("placeholder"):
            status += " (placeholder)"
        out.append({"pair": name, "designed": designed, "min": worst["distance"], "at": worst,
                    "status": status, "runs": runs})
    return out


# ----------------------------------------------------------- feather latch
def _latch_cases():
    """(case, wheel beta, shaft beta, released, hook pull along -X (mm), hook turn about the stem axis (deg)).

    latch.md section 5 (revision B): every latched angle the shaft stops allow (-3..+48), every
    wheel angle the wheel stops allow with the latch released (-7..+50), the hook pulled to the end
    of its stroke against a released sear, and the hook at its position tolerance against a latched one.
    """
    out = [(f"latched at {b:+d}", float(b), float(b), False, 0.0, 0.0) for b in range(-3, 49)]
    out += [(f"released, wheel at {b:+d}, shaft feathered", float(b), 45.0, True, 0.0, 0.0) for b in range(-7, 51)]
    out += [(f"released at {b:+d}, hook at the end of its stroke", float(b), 45.0, True, L.LATCH_SOLENOID[4], 0.0)
            for b in (-3, 0, 15, 30, 40, 48)]
    for b in (-3, 15, 30, 40, 48):
        for rot in (-L.HOOK_ROT_TOL, L.HOOK_ROT_TOL):
            out.append((f"latched at {b:+d}, hook turned {rot:+.0f} deg and 0.2 mm in", float(b), float(b), False,
                        0.2, rot))
    return out


LATCH_CASES = _latch_cases()

#: Latch pairs allowed closer than 3 mm in latch_check, with the least gap each must keep (mm) and why
#: (SPEC 4 latch table). A pair closer than its least gap, or touching when it has none, is reported.
LATCH_NEAR = [
    (r"^B40 ", r"^M58 ", 1.0, "trip hook outside the tab roller: 1.5 +/- 0.2 mm radial running gap (1.0 with the hook turned 2 deg and 0.2 mm in)"),
    (r"^M53 ", r"^M58 ", 2.0, "sear yoke under the hook arc (2.4 with the hook at its tolerance)"),
    (r"^M56 |^M54 Tab roller pin|^M54 Sear pin|^M60 ", r"^M58 ", 2.5, "hook bridge 3 mm over the top plate and pin heads (2.8 with the hook turned 2 deg)"),
    (r"^M51 ", r"^M57 ", 0.0, "carrier lug lands on the wheel-stop blocks at wheel -7 / +50 (0.1 mm drawn)"),
    (r"^B03 |^M51 ", r"^B04 ", 0.0, "worm drive (mesh)"),
    (r"^B36 ", r"^M08 |^B39 ", 0.0, "wheel bush: bore on the shaft, flange on the retaining ring"),
    (r"^B37 ", r"^M50 ", 0.0, "pawl roller on the load flank (latched) or riding on the collar OD (re-engaging)"),
    (r"^M54 Pawl pivot pin", r"^M50 ", 0.3, "pawl pivot pin passes the collar OD (0.4 mm)"),
    (r"^B36 |^M52 ", r"^M50 ", 0.4, "bush 0.5 mm axial float under the collar; pawl nose cheeks 0.5 mm over and under it"),
    (r"^M53 |^M60 |^B38 |^M54 Sear", r"^M08 |^M50 ", 1.5, "sear, its roller, pin and stop beside the shaft and collar (1.7 with the sear tripped)"),
    (r"^M52 ", r"^M08 ", 2.0, "pawl tail beside the shaft with the pawl open 30 deg (2.4)"),
    (r"^B03 |^M51 ", r"^M08 ", 2.5, "wheel and carrier bores over the bush (3.0)"),
    (r"^M52 ", r"^M15 ", 2.0, "pawl tail inside the housing wall (2.2)"),
    (r"^B37 ", r"^M15 ", 2.5, "opened pawl roller inside the housing wall (2.9)"),
]


def _latch_rule(a, b):
    for pa, pb, gmin, why in LATCH_NEAR:
        if (re.search(pa, _key(a)) and re.search(pb, _key(b))) or (re.search(pa, _key(b)) and re.search(pb, _key(a))):
            return gmin, why
    return None


def latch_check(include_printed: bool = True, log=print) -> list[dict]:
    """Interference and clearance of the latch with the wheel and the shaft at different angles.

    Parts on the worm wheel (``extra['latch'] == 'wheel'``) are turned by the wheel angle, in the
    released cases with the pawl open and the sear tripped; every other frame-P part is turned
    by the shaft angle; frame-S parts stay put, except the trip hook and stem, which are pulled
    along -X and turned about the stem axis where the case says. Only pairs that move relative
    to each other are checked. A pair closer than 3 mm is intended only if it has a LATCH_NEAR
    rule and keeps that rule's least gap.
    """
    from build123d import Pos, Rot
    from . import structure
    its, _ = assembly.collect(0.0, L.CARRIAGE_R_DEFAULT, include_printed)
    near = [it for it in its if it.frame in ("S", "P")]
    released = {(i, n): shp for i, n, shp, _, _ in structure.latch_wheel_shapes(L.PAWL_OPEN_DEG, L.SEAR_TRIP_DEG)}
    _, sy, sz, _ = L.TRIP_STEM
    out = []

    def rz(deg):
        m = np.eye(4)
        b = np.radians(deg)
        m[:2, :2] = [[np.cos(b), -np.sin(b)], [np.sin(b), np.cos(b)]]
        return m

    def hook_m(dx, rot):
        m = np.eye(4)
        r = np.radians(rot)
        c_, s_ = np.cos(r), np.sin(r)
        m[1:3, 1:3] = [[c_, -s_], [s_, c_]]
        m[1:3, 3] = np.array([sy, sz]) - m[1:3, 1:3] @ np.array([sy, sz])
        m[0, 3] = -dx
        return m

    meshed = {}
    for case, bw, bs, rel, hdx, hrot in LATCH_CASES:
        t0 = time.time()
        posed = []
        for k, it in enumerate(near):
            role = "S" if it.frame == "S" else ("W" if it.extra.get("latch") == "wheel" or it.id == "B03" else "P")
            shp = it.shape
            use_rel = role == "W" and rel and (it.id, it.name) in released
            if use_rel:
                shp = released[(it.id, it.name)]
            moved = role == "S" and it.id in ("M58", "M61")
            if role == "S":
                m = hook_m(hdx, hrot) if moved else np.eye(4)
            else:
                m = rz(bw if role == "W" else bs)
            key = (k, use_rel)
            if key not in meshed:
                v, _ = meshmod.mesh(shp, it.tol)
                meshed[key] = (v, meshmod.manifold(shp, it.tol) if len(v) else None)
            v, man = meshed[key]
            if len(v) == 0:
                continue
            pv = meshmod.transform(v, m)
            occ = Rot(0, 0, bw if role == "W" else bs) * shp if role != "S" else (
                Pos(-hdx, 0, 0) * Pos(0, sy, sz) * Rot(hrot, 0, 0) * Pos(0, -sy, -sz) * shp if moved else shp)
            posed.append((role, it, occ, m, pv.min(0), pv.max(0), man))
        inter, close = [], []
        for i in range(len(posed)):
            ra, a, oa, ma, loa, hia, mana = posed[i]
            for j in range(i + 1, len(posed)):
                rb, b, ob, mb, lob, hib, manb = posed[j]
                if ra == rb or "W" not in (ra, rb):
                    continue
                if not (np.all(loa <= hib + L.CLEARANCE_MIN) and np.all(hia >= lob - L.CLEARANCE_MIN)):
                    continue
                if mana is None or manb is None:
                    continue
                A = mana.transform(meshmod.m3x4(ma))
                B = manb.transform(meshmod.m3x4(mb))
                rec = {"a": a.label, "b": b.label}
                vol = float((A ^ B).volume())
                if vol > OVERLAP_MM3 and _rule_for(ALLOW, a, b) is None:
                    try:
                        from OCP.BRepAlgoAPI import BRepAlgoAPI_Common
                        from OCP.BRepGProp import BRepGProp
                        from OCP.GProp import GProp_GProps
                        op = BRepAlgoAPI_Common(oa.wrapped, ob.wrapped)
                        op.Build()
                        props = GProp_GProps()
                        BRepGProp.VolumeProperties_s(op.Shape(), props)
                        ex = abs(float(props.Mass()))
                    except Exception:  # noqa: BLE001
                        ex = None
                    rec["mesh_mm3"], rec["exact_mm3"] = round(vol, 2), None if ex is None else round(ex, 2)
                    if ex is None or ex > OVERLAP_MM3:
                        inter.append(rec)
                        continue
                    vol = 0.0
                if vol > OVERLAP_MM3:
                    continue
                try:
                    gap = float(A.min_gap(B, L.CLEARANCE_MIN))
                except Exception:  # noqa: BLE001
                    gap = None
                if gap is not None and gap < L.CLEARANCE_MIN - 1e-6:
                    rule = _latch_rule(a, b)
                    ok = rule is not None and gap >= rule[0] - 0.05
                    rec.update(gap_mesh=round(gap, 2), least=None if rule is None else rule[0],
                               intended=rule[1] if ok else None, placeholder=a.placeholder or b.placeholder)
                    close.append(rec)
        r = {"case": case, "beta_wheel": bw, "beta_shaft": bs, "released": rel, "hook_pull": hdx, "hook_turn": hrot,
             "interferences": inter, "close": close, "seconds": round(time.time() - t0, 1)}
        out.append(r)
        if log:
            bad = [c for c in close if not c["intended"]]
            if inter or bad:
                log(f"latch: {case}: {len(inter)} interferences, {len(bad)} gaps below their least ({r['seconds']} s)")
            for c in inter:
                log(f"  INTERFERENCE {c['a']} x {c['b']} {c.get('exact_mm3')} mm3")
            for c in bad:
                log(f"  gap {c['gap_mesh']} mm {c['a']} x {c['b']} (least {c['least']})")
    if log:
        log(f"latch: {len(out)} cases, {sum(len(r['interferences']) for r in out)} interferences, "
            f"{sum(1 for r in out for c in r['close'] if not c['intended'])} gaps below their least")
    return out


# ------------------------------------------------------------------- driver
def check(items: list[Item] | None = None, poses=None, carriage_r: float = L.CARRIAGE_R_DEFAULT,
          include_printed: bool = True, named: bool = True, log=print) -> dict:
    """Interference and clearance check at every pose (SPEC section 1).

    ``items``: unposed items to use for the pose-independent parts (the
    carriage and belt are always rebuilt per pose); default: collect them.
    """
    poses = poses or L.POSES
    t0 = time.time()
    results = []
    base = None
    if items is not None:
        base = [it.copy(shape=it.extra.get("unposed", it.shape)) for it in items if not it.pose_dependent]
    for k, (theta, beta) in enumerate(poses):
        its, info = assembly.collect(theta, carriage_r, include_printed)
        if base is not None:
            its = base + [it for it in its if it.pose_dependent]
        r = check_pose(its, theta, beta, static=(k == 0))
        r["belt"] = {kk: info["belt"][kk] for kk in ("leave_arc_phi", "rejoin_arc_phi", "on_arc_margin_deg",
                                                    "pulley_wrap_deg", "pitch_length", "source")}
        results.append(r)
        if log:
            log(f"pose theta {theta:+.0f} beta {beta:+.0f}: {len(r['interferences'])} interferences, "
                f"{len(r['placeholder_overlaps'])} placeholder overlaps, {len(r['allowed'])} intended contacts, "
                f"{sum(1 for c in r['close'] if not c['intended'])} unexplained gaps < 3 mm ({r['seconds']} s)")
    # extra carriage positions at theta 0 (the carriage runs r 15..140)
    extra = []
    for r_ in (L.CARRIAGE_R_RANGE[0], L.CARRIAGE_R_RANGE[1]):
        its, _ = assembly.collect(0.0, r_, include_printed)
        cr = check_pose([i for i in its if i.frame == "S"], 0.0, 0.0, static=False)
        cr["carriage_r"] = r_
        extra.append(cr)
        if log:
            log(f"carriage r {r_:.0f} at theta 0: {len(cr['interferences'])} interferences")
    lt = latch_check(include_printed, log=log)
    nm = named_clearances(poses, include_printed) if named else []
    _, prep = assembly.printed_items()
    out = {
        "poses": results,
        "carriage_range": extra,
        "named_clearances": nm,
        "placeholders": prep.placeholders if prep else [],
        "printed_loaded": prep.loaded if prep else [],
        "printed_log": prep.log if prep else [],
        "deviations": L.DEVIATIONS,
        "assumed": L.ASSUMED,
        "overlap_limit_mm3": OVERLAP_MM3,
        "clearance_min_mm": L.CLEARANCE_MIN,
        "seconds": round(time.time() - t0, 1),
    }
    out["latch"] = lt
    out["summary"] = {
        "interferences": sum(len(r["interferences"]) for r in results) + sum(len(r["interferences"]) for r in extra)
        + sum(len(r["interferences"]) for r in lt),
        "placeholder_overlaps": sum(len(r["placeholder_overlaps"]) for r in results),
        "unexplained_close": sum(1 for r in results + lt for c in r["close"] if not c["intended"] and not c["placeholder"]),
        "named_below": [n["pair"] for n in nm if str(n.get("status", "")).startswith(("BELOW", "CHECK"))],
        "placeholders": len(out["placeholders"]),
    }
    return out


def write_report(res: dict, md_path, json_path):
    md_path, json_path = Path(md_path), Path(json_path)
    json_path.write_text(json.dumps(res, indent=1, default=str))
    s = res["summary"]
    lines = ["# Lantern 330-G interference and clearance report", "",
             "Generated by `python3 -m l330g check` (or `build`). Poses from SPEC section 1; "
             f"overlap limit {res['overlap_limit_mm3']} mm³; clearance target {res['clearance_min_mm']} mm (SPEC 4).", "",
             f"- Interferences (exact overlap > {res['overlap_limit_mm3']} mm³, not an intended contact): **{s['interferences']}**",
             f"- Overlaps involving placeholder envelopes (printed part not built yet): {s['placeholder_overlaps']}",
             f"- Moving pairs closer than 3 mm with no stated reason: {s['unexplained_close']}",
             f"- SPEC 4 named pairs below their designed value: {', '.join(s['named_below']) or 'none'}",
             f"- Printed parts still placeholders: {s['placeholders']} of {len(printed.SPEC_TABLE)}",
             f"- Run time: {res['seconds']} s", ""]
    lines += ["## Poses", "", "| theta | beta | interferences | placeholder overlaps | intended contacts | gaps < 3 mm (unexplained) | belt on-arc margin | pulley wrap |",
              "|---|---|---|---|---|---|---|---|"]
    for r in res["poses"]:
        unexp = sum(1 for c in r["close"] if not c["intended"])
        lines.append(f"| {r['theta']:+.0f} | {r['beta']:+.0f} | {len(r['interferences'])} | {len(r['placeholder_overlaps'])} | "
                     f"{len(r['allowed'])} | {len(r['close'])} ({unexp}) | {r['belt']['on_arc_margin_deg']:.1f}° | {r['belt']['pulley_wrap_deg']:.0f}° |")
    lines.append("")
    for r in res["poses"] + res["carriage_range"]:
        if r["interferences"]:
            tag = f"theta {r['theta']:+.0f}, beta {r['beta']:+.0f}" + (f", carriage r {r['carriage_r']:.0f}" if "carriage_r" in r else "")
            lines += [f"### Interferences at {tag}", "", "| A | B | frames | category | exact mm³ | mesh mm³ |", "|---|---|---|---|---|---|"]
            for c in r["interferences"]:
                lines.append(f"| {c['a']} | {c['b']} | {c['frames']} | {c['category']} | {c.get('exact_mm3')} | {c.get('mesh_mm3')} |")
            lines.append("")
    if res.get("latch"):
        lines += ["## Feather latch: wheel and shaft angles (theta 0)", "",
                  "The worm wheel and the pitch shaft turn together only while latched. These cases pose the parts on the "
                  "wheel and the parts on the shaft separately (latch.md section 5).", "",
                  "| Case | wheel | shaft | interferences | gaps < 3 mm (unexplained) |", "|---|---|---|---|---|"]
        for r in res["latch"]:
            unexp = sum(1 for c in r["close"] if not c["intended"])
            lines.append(f"| {r['case']} | {r['beta_wheel']:+.0f} | {r['beta_shaft']:+.0f} | {len(r['interferences'])} | "
                         f"{len(r['close'])} ({unexp}) |")
            for c in r["interferences"]:
                lines.append(f"| INTERFERENCE | | | {c['a']} x {c['b']} | {c.get('exact_mm3')} mm3 |")
        lines.append("")
    lines += ["## SPEC 4 named clearances (exact B-rep distance, worst pose)", "",
              "| Pair | Designed | Measured min (mm) | At | Status |", "|---|---|---|---|---|"]
    for n in res["named_clearances"]:
        if "min" in n:
            at = n["at"]
            where = f"theta {at['theta']:+.0f}, beta {at['beta']:+.0f}" + (f", r {at['carriage_r']:.0f}" if at['carriage_r'] != L.CARRIAGE_R_DEFAULT else "")
            lines.append(f"| {n['pair']} | {n['designed']} | {n['min']:.2f} | {where} | {n['status']} |")
        else:
            lines.append(f"| {n['pair']} | {n['designed']} | — | — | {n['status']}: {n.get('detail', '')} |")
    lines.append("")
    first = res["poses"][0]
    if first["placeholder_overlaps"]:
        lines += ["## Overlaps involving placeholder envelopes (theta 0, beta 0)", "",
                  "These go away or change when the printed part is built.", "",
                  "| A | B | category | exact mm³ |", "|---|---|---|---|"]
        for c in first["placeholder_overlaps"]:
            lines.append(f"| {c['a']} | {c['b']} | {c['category']} | {c.get('exact_mm3')} |")
        lines.append("")
    lines += ["## Moving pairs closer than 3 mm", "", "| Pose | A | B | mesh gap (mm) | Reason |", "|---|---|---|---|---|"]
    for r in res["poses"]:
        for c in r["close"]:
            lines.append(f"| {r['theta']:+.0f}/{r['beta']:+.0f} | {c['a']} | {c['b']} | {c['gap_mesh']} | {c['intended'] or ('placeholder' if c['placeholder'] else '**unexplained**')} |")
    lines.append("")
    lines += ["## Intended contacts at theta 0, beta 0", "", "| A | B | reason |", "|---|---|---|"]
    for c in first["allowed"]:
        lines.append(f"| {c['a']} | {c['b']} | {c['reason']} |")
    lines.append("")
    lines += ["## Printed parts", ""]
    for p in res["printed_loaded"]:
        lines.append(f"- {p['id']} `{p['module']}`: {p['copies']} placed, frame {p['frame']}, {p['material']} ({p['source']})")
    for p in res["placeholders"]:
        lines.append(f"- {p['id']} `{p['module']}`: PLACEHOLDER ({p['reason']})")
    for l_ in res["printed_log"]:
        lines.append(f"- log: {l_}")
    lines += ["", "## Deviations from SPEC numbers (also reported as SPEC issues)", ""]
    for k, v in res["deviations"].items():
        lines.append(f"- **{k}** {v}")
    lines += ["", "## ASSUMED details (VERIFY)", ""]
    for k, v in res["assumed"].items():
        lines.append(f"- **{k}** {v}")
    md_path.write_text("\n".join(lines) + "\n")
    return md_path
