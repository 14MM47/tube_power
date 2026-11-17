"""The GT2 belt's omega path in the X = 85 plane, and the belt solid.

The belt runs (SPEC 3.4): tooth side on the arc (pitch R 99.95, frame S), off
the arc onto idler 1 (back side on the idler), down round the generator pulley
(tooth side), up over idler 2 (back side) and back onto the arc. Its ends are
clamped to the arc (P04) at phi = +/-BELT_END_PHI, where phi is measured about
the X axis from -Z towards +Y.

The arc is axisymmetric about X, so the tangent points where the belt leaves
and rejoins the arc are fixed in frame A; only the clamped ends turn with the
swing: at swing theta they sit at phi = +/-BELT_END_PHI + theta.

Idler and pulley centres come from ``parts/lantern330g/belt_path.json`` in the
3dprint checkout when that file exists (written by P06's author), otherwise
from SPEC 3.4.
"""
from __future__ import annotations

import json
import math
import os
from dataclasses import dataclass, field
from pathlib import Path

import numpy as np

from . import layout as L

# Belt section relative to the pitch line (GT2 2 mm): the back is +0.376 mm on
# the back side, the tooth tips -1.004 mm on the tooth side; total 1.38 mm.
BACK_OFF = L.BELT_T - L.GT2_TOOTH_H - L.GT2_PLD     # 0.376
TOOTH_OFF = L.GT2_PLD + L.GT2_TOOTH_H               # 1.004


@dataclass
class Circle2:
    name: str
    c: tuple[float, float]       # (Y, Z)
    r: float                     # pitch-line radius
    side: int                    # +1: centre on the left of travel, -1: on the right


@dataclass
class BeltGeometry:
    source: str
    arc_r: float
    pulley_c: tuple[float, float]
    pulley_r: float
    idlers: list[tuple[float, float]]
    idler_contact_r: float
    plane_x: float = L.BELT_PLANE_X
    width: float = L.BELT_W
    notes: list[str] = field(default_factory=list)


def _threedprint_root() -> Path:
    env = os.environ.get("LANTERN_3DPRINT")
    if env:
        return Path(env)
    here = Path(__file__).resolve()
    # .../tube_power/designs/lantern-330-g/cad/l330g/belt.py -> .../3dprint
    return here.parents[5] / "3dprint"


def _point(v):
    """Read a (Y, Z) point from a dict or a list in several plausible spellings."""
    if isinstance(v, dict):
        for k in ("yz", "centre_yz", "center_yz", "centre", "center", "c", "xyz"):
            if k in v:
                return _point(v[k])
        if "y" in v and "z" in v:
            return float(v["y"]), float(v["z"])
        if "Y" in v and "Z" in v:
            return float(v["Y"]), float(v["Z"])
        return None
    if isinstance(v, (list, tuple)) and len(v) in (2, 3) and all(isinstance(x, (int, float)) for x in v):
        return (float(v[0]), float(v[1])) if len(v) == 2 else (float(v[1]), float(v[2]))
    return None


def load_geometry() -> BeltGeometry:
    """Belt geometry from belt_path.json if present, else SPEC 3.4 defaults."""
    g = BeltGeometry(
        source="SPEC 3.4 defaults",
        arc_r=L.ARC_PITCH_R,
        pulley_c=L.PULLEY_YZ,
        pulley_r=L.PULLEY_PITCH_R,
        idlers=list(L.IDLER_YZ),
        idler_contact_r=L.IDLER_CONTACT_D / 2.0,
    )
    path = _threedprint_root() / "parts" / "lantern330g" / "belt_path.json"
    if not path.exists():
        return g
    try:
        data = json.loads(path.read_text())
    except Exception as e:  # noqa: BLE001
        g.notes.append(f"belt_path.json unreadable ({e}); using SPEC defaults")
        return g
    idl = None
    for k, v in data.items():
        if "idler" in k.lower() and isinstance(v, list) and len(v) >= 2:
            pts = [_point(x) for x in v]
            if all(p is not None for p in pts):
                idl = pts[:2]
                for x in v:
                    if isinstance(x, dict):
                        for rk in ("contact_r", "r", "radius"):
                            if rk in x:
                                g.idler_contact_r = float(x[rk])
                        for dk in ("contact_d", "d", "diameter"):
                            if dk in x:
                                g.idler_contact_r = float(x[dk]) / 2.0
                break
    for k, v in data.items():
        if "pulley" in k.lower():
            p = _point(v)
            if p is not None:
                g.pulley_c = p
            if isinstance(v, dict):
                for rk in ("pitch_r", "pitch_radius", "r"):
                    if rk in v:
                        g.pulley_r = float(v[rk])
    for k in ("idler_contact_r", "idler_r"):
        if k in data:
            g.idler_contact_r = float(data[k])
    if "idler_contact_d" in data:
        g.idler_contact_r = float(data["idler_contact_d"]) / 2.0
    for k in ("arc_pitch_r", "arc_r"):
        if k in data:
            g.arc_r = float(data[k])
    if idl is None:
        g.notes.append("belt_path.json has no idler centres I could read; using SPEC defaults")
        return g
    # put idler 1 (the +Y one) first: the belt leaves the +Y side of the arc first
    idl = sorted(idl, key=lambda p: -p[0])
    g.idlers = idl
    g.source = f"{path.name} ({path.parent})"
    return g


def _tangent(c1: Circle2, c2: Circle2):
    """Tangent line leaving c1 and arriving at c2 with each centre on its stated side."""
    p1, p2 = np.asarray(c1.c, float), np.asarray(c2.c, float)
    D = p2 - p1
    Ln = float(np.linalg.norm(D))
    Dh = D / Ln
    Dp = np.array([-Dh[1], Dh[0]])
    k = c2.side * c2.r - c1.side * c1.r
    a = k / Ln
    if abs(a) >= 1:
        raise ValueError(f"no tangent between {c1.name} and {c2.name}")
    n = a * Dh + math.sqrt(1 - a * a) * Dp
    return p1 - c1.side * c1.r * n, p2 - c2.side * c2.r * n, n


def _phi(p):
    """Angle about X from -Z towards +Y, degrees."""
    return math.degrees(math.atan2(p[0], -p[1]))


def _on_arc(r, phi_deg):
    a = math.radians(phi_deg)
    return np.array([r * math.sin(a), -r * math.cos(a)])


@dataclass
class Segment:
    kind: str                 # "arc" or "line"
    p0: np.ndarray
    p1: np.ndarray
    circle: Circle2 | None = None
    sweep: float = 0.0        # radians, signed: + is counter-clockwise in (Y, Z)

    def length(self):
        if self.kind == "line":
            return float(np.linalg.norm(self.p1 - self.p0))
        return abs(self.sweep) * self.circle.r


def circles(g: BeltGeometry) -> list[Circle2]:
    back_r = g.idler_contact_r + BACK_OFF
    return [
        Circle2("arc", (0.0, 0.0), g.arc_r, -1),
        Circle2("idler1", g.idlers[0], back_r, +1),
        Circle2("pulley", g.pulley_c, g.pulley_r, -1),
        Circle2("idler2", g.idlers[1], back_r, +1),
        Circle2("arc", (0.0, 0.0), g.arc_r, -1),
    ]


def path(theta: float = 0.0, g: BeltGeometry | None = None, end_phi: float = L.BELT_END_PHI):
    """Pitch-line path in frame A at swing ``theta``: a list of Segments, plus a summary."""
    g = g or load_geometry()
    cs = circles(g)
    tans = [_tangent(a, b) for a, b in zip(cs[:-1], cs[1:])]
    start = _on_arc(g.arc_r, end_phi + theta)
    end = _on_arc(g.arc_r, -end_phi + theta)
    segs: list[Segment] = []
    entry = start
    for i, c in enumerate(cs):
        exit_ = tans[i][0] if i < len(tans) else end
        cc = np.asarray(c.c, float)
        a0 = math.atan2(*(entry - cc)[::-1])
        a1 = math.atan2(*(exit_ - cc)[::-1])
        if c.side > 0:
            sw = (a1 - a0) % (2 * math.pi)
        else:
            sw = -((a0 - a1) % (2 * math.pi))
        segs.append(Segment("arc", entry, exit_, c, sw))
        if i < len(tans):
            segs.append(Segment("line", tans[i][0], tans[i][1]))
            entry = tans[i][1]
    leave = _phi(tans[0][0])
    rejoin = _phi(tans[-1][1])
    wrap_pulley = abs(segs[4].sweep)
    info = {
        "source": g.source,
        "theta": theta,
        "leave_arc_phi": leave,
        "rejoin_arc_phi": rejoin,
        "end_phi": end_phi,
        "on_arc_margin_deg": min(end_phi + theta - leave, rejoin - (-end_phi + theta)),
        "pulley_wrap_deg": math.degrees(wrap_pulley),
        "idler_wrap_deg": [math.degrees(abs(segs[2].sweep)), math.degrees(abs(segs[6].sweep))],
        "pitch_length": sum(s.length() for s in segs),
        "idlers": [list(p) for p in g.idlers],
        "pulley": list(g.pulley_c),
        "notes": list(g.notes),
    }
    info["teeth"] = info["pitch_length"] / L.BELT_PITCH
    if info["on_arc_margin_deg"] < 0:
        raise ValueError(f"belt end passes its tangent point at theta {theta}: {info}")
    return segs, info


def _offset_point(seg: Segment, t: float, w: float):
    """Point at parameter t (0..1) of a segment, offset w along the left normal."""
    if seg.kind == "line":
        d = (seg.p1 - seg.p0) / np.linalg.norm(seg.p1 - seg.p0)
        n = np.array([-d[1], d[0]])
        return seg.p0 + t * (seg.p1 - seg.p0) + w * n
    c = np.asarray(seg.circle.c, float)
    a0 = math.atan2(*(seg.p0 - c)[::-1])
    a = a0 + t * seg.sweep
    r = seg.circle.r - seg.circle.side * w
    return c + r * np.array([math.cos(a), math.sin(a)])


def solid(theta: float = 0.0, g: BeltGeometry | None = None):
    """Belt solid (a plain 9 x 1.38 band; teeth not drawn) in frame A at swing theta."""
    from build123d import Edge, Face, Wire, extrude, Vector

    segs, info = path(theta, g)
    x0 = L.BELT_X[0]

    def P(p):
        return Vector(x0, float(p[0]), float(p[1]))

    def edges_for(w, reverse=False):
        out = []
        seq = segs[::-1] if reverse else segs
        for s in seq:
            if s.kind == "line" or abs(s.sweep) < 1e-9:
                a, b = _offset_point(s, 0, w), _offset_point(s, 1, w)
                if reverse:
                    a, b = b, a
                if np.linalg.norm(b - a) > 1e-6:
                    out.append(Edge.make_line(P(a), P(b)))
            else:
                a, m, b = (_offset_point(s, t, w) for t in (0, 0.5, 1))
                if reverse:
                    a, b = b, a
                out.append(Edge.make_three_point_arc(P(a), P(m), P(b)))
        return out

    back = edges_for(+BACK_OFF)
    tooth = edges_for(-TOOTH_OFF, reverse=True)
    cap_end = Edge.make_line(back[-1].end_point(), tooth[0].start_point())
    cap_start = Edge.make_line(tooth[-1].end_point(), back[0].start_point())
    wire = Wire(back + [cap_end] + tooth + [cap_start])
    face = Face(wire)
    return extrude(face, L.BELT_W, dir=(1, 0, 0)), info
