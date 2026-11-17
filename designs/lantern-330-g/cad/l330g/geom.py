"""Small build123d helpers: boxes and cylinders from coordinate ranges, tubes, springs.

All take ranges in assembly coordinates so the structure code reads like
SPEC.md: ``box((-71, -59), (-20, 20), (-215, 20))``.
"""
from __future__ import annotations

import math

from build123d import (Box, Circle, Compound, Cylinder, Helix, Location, Plane, Polyline,
                       Pos, Rot, Sphere, extrude, make_face, sweep)


def _c(r):
    return (r[0] + r[1]) / 2.0, abs(r[1] - r[0])


def box(xr, yr, zr):
    """Axis-aligned box spanning the three (lo, hi) ranges."""
    (cx, dx), (cy, dy), (cz, dz) = _c(xr), _c(yr), _c(zr)
    return Pos(cx, cy, cz) * Box(dx, dy, dz)


def cyl_z(d, zr, x=0.0, y=0.0):
    cz, h = _c(zr)
    return Pos(x, y, cz) * Cylinder(d / 2.0, h)


def cyl_x(d, xr, y=0.0, z=0.0):
    cx, h = _c(xr)
    return Pos(cx, y, z) * Rot(0, 90, 0) * Cylinder(d / 2.0, h)


def cyl_y(d, yr, x=0.0, z=0.0):
    cy, h = _c(yr)
    return Pos(x, cy, z) * Rot(90, 0, 0) * Cylinder(d / 2.0, h)


def tube_z(od, id_, zr, x=0.0, y=0.0):
    return cyl_z(od, zr, x, y) - cyl_z(id_, (zr[0] - 1, zr[1] + 1), x, y)


def tube_x(od, id_, xr, y=0.0, z=0.0):
    return cyl_x(od, xr, y, z) - cyl_x(id_, (xr[0] - 1, xr[1] + 1), y, z)


def tube_y(od, id_, yr, x=0.0, z=0.0):
    return cyl_y(od, yr, x, z) - cyl_y(id_, (yr[0] - 1, yr[1] + 1), x, z)


def hex_prism_x(af, xr, y=0.0, z=0.0):
    """Hexagon (across flats ``af``) extruded along X over ``xr``."""
    r = af / math.sqrt(3.0)
    pts = [(r * math.cos(math.radians(30 + 60 * i)), r * math.sin(math.radians(30 + 60 * i)))
           for i in range(6)]
    face = make_face(Polyline(*pts, close=True))
    solid = extrude(face, abs(xr[1] - xr[0]))
    return Pos(min(xr), y, z) * Rot(0, 90, 0) * solid


def hex_prism_y(af, yr, x=0.0, z=0.0):
    r = af / math.sqrt(3.0)
    pts = [(r * math.cos(math.radians(60 * i)), r * math.sin(math.radians(60 * i))) for i in range(6)]
    face = make_face(Polyline(*pts, close=True))
    solid = extrude(face, abs(yr[1] - yr[0]))
    # extrude runs along +Z; Rot(-90,0,0) maps +Z to +Y
    return Pos(x, min(yr), z) * Rot(-90, 0, 0) * solid


def hex_prism_z(af, zr, x=0.0, y=0.0):
    r = af / math.sqrt(3.0)
    pts = [(r * math.cos(math.radians(60 * i)), r * math.sin(math.radians(60 * i))) for i in range(6)]
    face = make_face(Polyline(*pts, close=True))
    return Pos(x, y, min(zr)) * extrude(face, abs(zr[1] - zr[0]))


def helix_z(mean_d, wire_d, length, coils):
    """Helical coil along +Z from Z = 0 to ``length`` (wire centreline inside that span)."""
    usable = length - wire_d
    pitch = usable / coils
    h = Helix(pitch=pitch, height=usable, radius=mean_d / 2.0)
    prof = Plane(origin=h.position_at(0), z_dir=h.tangent_at(0)) * Circle(wire_d / 2.0)
    s = sweep(prof, h, is_frenet=True)
    return Pos(0, 0, wire_d / 2.0) * s


def spring_y(mean_d, wire_d, y0, y1, coils, x=0.0, z=0.0):
    """Compression spring along Y from ``y0`` to ``y1`` (either order)."""
    L = abs(y1 - y0)
    s = helix_z(mean_d, wire_d, L, coils)
    if y1 >= y0:
        return Pos(x, y0, z) * Rot(-90, 0, 0) * s
    return Pos(x, y0, z) * Rot(90, 0, 0) * s


def spring_z(mean_d, wire_d, zr, coils, x=0.0, y=0.0):
    return Pos(x, y, min(zr)) * helix_z(mean_d, wire_d, abs(zr[1] - zr[0]), coils)


def ring_z(od, id_, zr, x=0.0, y=0.0):
    return tube_z(od, id_, zr, x, y)


def ring_x(od, id_, xr, y=0.0, z=0.0):
    return tube_x(od, id_, xr, y, z)


def sector_prism_x(r_in, r_out, a0, a1, xr, n=48):
    """Annular sector about the X axis, angles in degrees measured from -Z towards +Y."""
    pts = []
    for i in range(n + 1):
        a = math.radians(a0 + (a1 - a0) * i / n)
        pts.append((r_out * math.sin(a), -r_out * math.cos(a)))
    for i in range(n, -1, -1):
        a = math.radians(a0 + (a1 - a0) * i / n)
        pts.append((r_in * math.sin(a), -r_in * math.cos(a)))
    face = make_face(Polyline(*pts, close=True))
    solid = extrude(face, abs(xr[1] - xr[0]))
    # face drawn in XY as (Y, Z); map local x->Y, y->Z, extrude z->X
    return Location((min(xr), 0, 0)) * _yz_to_world(solid)


def _yz_to_world(shape):
    """Map a shape drawn with local (x, y, z) = (Y, Z, X) into world coordinates."""
    # local x -> world Y, local y -> world Z, local z -> world X
    return Rot(0, 90, 90) * shape


def polygon_prism_x(pts_yz, xr):
    """Prism along X of a closed (Y, Z) polygon."""
    face = make_face(Polyline(*pts_yz, close=True))
    solid = extrude(face, abs(xr[1] - xr[0]))
    return Location((min(xr), 0, 0)) * _yz_to_world(solid)


def compound(shapes, label=""):
    shapes = [s for s in shapes if s is not None]
    c = Compound(children=list(shapes)) if len(shapes) > 1 else shapes[0]
    return c


def sphere(r, at=(0, 0, 0)):
    return Pos(*at) * Sphere(r)
