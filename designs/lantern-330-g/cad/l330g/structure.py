"""Every non-printed part of the Lantern 330-G, as build123d solids at their SPEC positions.

Parts are modelled at concept level with recognisable detail: the prism's
sandwich panels with butt-jointed corners, the bulkheads' lightening holes,
the hollow neck, the hub plates, stub axles with flanges and nuts, the pitch
housing with its worm window, bearings as inner and outer rings, a toothed
worm wheel and threaded worm, helical springs, a NEMA-17 of the standard
shape, the 8108 generator, the hinge cheeks and the head, yaw and post.

Positions are in frame A at theta = 0, beta = 0 (SPEC section 1). Every
number comes from ``layout`` (SPEC.md, its ASSUMED list or its DEVIATIONS).

Three groups depend on the pose and are built by their own functions:

- ``carriage_items(r, theta)``: the spring carriage, its rail block and spacer,
  T8 nut, spring rods, springs, roller forks and rollers. The rollers are kept
  on the reaction plates at every swing (both springs preloaded, ASSUMED A8),
  so the springs and forks are re-solved for each theta.
- ``belt_item(theta)``: the belt, whose clamped ends turn with the arc.
- everything else: ``static_items()``.
"""
from __future__ import annotations

import math
import os
from functools import lru_cache
from pathlib import Path

from build123d import (Align, Axis, Box, Cylinder, Polyline, Pos, Rot, Sphere, Torus,
                       extrude, fillet, make_face)

from . import belt as beltmod
from . import layout as L
from .geom import (box, cyl_x, cyl_y, cyl_z, hex_prism_x, hex_prism_y, hex_prism_z,
                   polygon_prism_x, spring_y, spring_z, tube_x, tube_y, tube_z)
from .item import Item
from .materials import ALU_6063, ALU_6082

S_T20 = math.sin(math.radians(L.THETA_STOP))
C_T20 = math.cos(math.radians(L.THETA_STOP))


def _mirror_x(shape):
    from build123d import Plane, mirror
    return mirror(shape, Plane.YZ)


def _mirror_y(shape):
    from build123d import Plane, mirror
    return mirror(shape, Plane.XZ)


def _fuse(*shapes):
    out = shapes[0]
    for s in shapes[1:]:
        out = out + s
    return out


class _Collector:
    def __init__(self):
        self.items: list[Item] = []

    def add(self, id_, name, shape, mat, frame, *, group, tag="", bought=False, tol=0.1, **kw):
        it = Item(id=id_, name=name, shape=shape, material_key=mat, frame=frame, bought=bought,
                  group=group, tag=tag, tol=tol, **kw)
        self.items.append(it)
        return it


# =============================================================== 3.1 Prism (P)
def _prism(c: _Collector):
    zr = L.PANEL_Z
    o, i = L.PANEL_OUT, L.PANEL_IN
    for sx, tag in ((1, "+X"), (-1, "-X")):
        c.add("M01", "Prism panel, X face", box(sorted((sx * i, sx * o)), (-o, o), zr),
              "sandwich", "P", group="prism", tag=tag, tol=0.5)
    for sy, tag in ((1, "+Y"), (-1, "-Y")):
        c.add("M02", "Prism panel, Y face", box((-i, i), sorted((sy * i, sy * o)), zr),
              "sandwich", "P", group="prism", tag=tag, tol=0.5)
    h = L.BULKHEAD_W / 2
    p = L.BULKHEAD_HOLE_PITCH / 2
    for k, zc in enumerate(L.BULKHEAD_ZC):
        zr_b = (zc - L.BULKHEAD_T / 2, zc + L.BULKHEAD_T / 2)
        b = box((-h, h), (-h, h), zr_b)
        for x in (-p, p):
            for y in (-p, p):
                b = b - cyl_z(L.BULKHEAD_HOLE_D, (zr_b[0] - 1, zr_b[1] + 1), x, y)
        if k == 0:
            b = b - cyl_z(L.BULKHEAD_HOLE_D, (zr_b[0] - 1, zr_b[1] + 1))
            c.add("M03", "Bulkhead 1 (neck collar)", b, "sandwich", "P", group="prism",
                  tag=f"Z {zc:.0f}", tol=0.3)
        else:
            c.add("M04", "Bulkhead", b, "sandwich", "P", group="prism", tag=f"Z {zc:.0f}", tol=0.3)
    e = L.END_PLATE_W / 2
    bot = box((-e, e), (-e, e), L.BOTTOM_PLATE_Z) - cyl_z(L.NECK_HOLE_D, (580, 610))
    c.add("M05", "End plate, bottom", bot, "sandwich", "P", group="prism", tol=0.5)
    c.add("M06", "End plate, top", box((-e, e), (-e, e), L.TOP_PLATE_Z), "sandwich", "P",
          group="prism", tol=0.5)


# ================================================================ 3.2 Neck (P)
def _neck(c: _Collector):
    c.add("M07", "Neck tube 50/47", tube_z(L.NECK_OD, L.NECK_ID, L.NECK_Z), "cfrp", "P",
          group="neck", tol=0.1)
    foot = _fuse(cyl_z(L.INSERT_OD, L.INSERT_Z), cyl_z(L.SHOULDER_OD, L.SHOULDER_Z),
                 cyl_z(L.PITCH_SHAFT_OD, L.PITCH_SHAFT_Z))
    z0 = L.PITCH_SHAFT_Z[0]
    foot = foot - cyl_z(L.PITCH_SHAFT_BORE_D, (z0 - 1, z0 + L.PITCH_SHAFT_BORE_DEPTH))
    c.add("M08", "Neck-foot insert and pitch shaft", foot, "alu", "P", group="neck",
          material_label=ALU_6082, tol=0.05)
    od, ln = L.SHAFT_SPACER
    zt = L.PITCH_BEARING_UPPER_Z[1]
    c.add("M09", "Pitch shaft spacer", tube_z(od, L.PITCH_SHAFT_OD, (zt, zt + ln)), "alu", "P",
          group="pitch", material_label=ALU_6082, tol=0.05)


# ======================================================= 3.3 Hub and pitch (S)
def _hub(c: _Collector):
    top = box(L.HUB_TOP_X, L.HUB_TOP_Y, L.HUB_TOP_Z)
    for x, y in L.HUB_TOP_M3_XY:
        top = top - cyl_z(2.5, (L.HUB_TOP_Z[0] - 1, L.HUB_TOP_Z[1] + 1), x, y)
    hx, hy, hd = L.HUB_TOP_CABLE_HOLE
    top = top - cyl_z(hd, (L.HUB_TOP_Z[0] - 1, L.HUB_TOP_Z[1] + 1), hx, hy)
    # bolt holes for the side plates, lever angle, hanger and KFL08 (M5 clearance)
    for x in (-129.0, 129.0):
        for y in (-30.0, 30.0):
            top = top - cyl_z(5.5, (L.HUB_TOP_Z[0] - 1, L.HUB_TOP_Z[1] + 1), x, y)
    for x, y in [(-42.0, -12.0), (-42.0, 12.0), (99.0, -20.0), (99.0, 20.0),
                 (L.LEADSCREW_XY[0], -L.KFL08[2] / 2), (L.LEADSCREW_XY[0], L.KFL08[2] / 2)]:
        top = top - cyl_z(5.5, (L.HUB_TOP_Z[0] - 1, L.HUB_TOP_Z[1] + 1), x, y)
    c.add("M10", "Hub top plate", top, "alu", "S", group="hub", material_label=ALU_6082, tol=0.1)

    for sx, tag in ((1, "+X"), (-1, "-X")):
        xr = sorted((sx * L.SIDE_PLATE_X[0], sx * L.SIDE_PLATE_X[1]))
        sp = box(xr, L.SIDE_PLATE_Y, L.SIDE_PLATE_Z) - cyl_x(L.STUB_D, (xr[0] - 1, xr[1] + 1))
        for y in (-30.0, 30.0):
            sp = sp - cyl_z(5.0, (L.SIDE_PLATE_Z[1] - 12, L.SIDE_PLATE_Z[1] + 1), sx * 129.0, y)
        c.add("M11", "Hub side plate", sp, "alu", "S", group="hub", tag=tag,
              material_label=ALU_6082, tol=0.1)

    # stub axles with their flanges, spacers and nuts
    b_in, b_out = (L.HINGE_BEARING_XC - L.HINGE_BEARING[2] / 2,
                   L.HINGE_BEARING_XC + L.HINGE_BEARING[2] / 2)        # 144, 156
    for sx, tag in ((1, "+X"), (-1, "-X")):
        def X(a, b):
            return tuple(sorted((sx * a, sx * b)))
        stub = _fuse(cyl_x(L.STUB_D, X(*L.STUB_X)),
                     cyl_x(L.STUB_FLANGE_D, X(L.STUB_X[0] - L.STUB_FLANGE_T, L.STUB_X[0])))
        if sx < 0:
            xe = -L.STUB_X[1]
            for y in L.STUB_END_M3_Y:
                stub = stub - cyl_x(2.5, (xe - 1, xe + 6), y, 0)
        c.add("M12", "Stub axle 25", stub, "stainless", "S", group="hub", tag=tag, tol=0.05)
        c.add("M13", "Axle spacer, inboard", tube_x(L.HINGE_INNER_RING_OD, L.STUB_D,
              X(L.SIDE_PLATE_X[1], b_in)), "stainless", "S", group="hub", tag=tag, tol=0.05)
        c.add("M14", "Axle spacer, outboard", tube_x(29.0, L.STUB_D, X(b_out, L.STUB_NUT_X[0])),
              "stainless", "S", group="hub", tag=tag, tol=0.05)
        nut = tube_x(L.STUB_NUT_OD, L.STUB_D, X(*L.STUB_NUT_X))
        for a in range(4):
            ang = math.radians(45 + 90 * a)
            r = L.STUB_NUT_OD / 2
            nut = nut - Pos(sx * sum(L.STUB_NUT_X) / 2, r * math.cos(ang), r * math.sin(ang)) * \
                Rot(ang * 180 / math.pi, 0, 0) * Box(7, 5, 5)
        c.add("B01", "Axle nut KM5 (M25x1.5)", nut, "stainless", "S", group="hub", tag=tag,
              bought=True, tol=0.05)

    # pitch housing, cap, lower seat
    hw, hh = L.WORM_WINDOW_WH
    wy, wz = L.WORM_WINDOW_YZ
    housing = tube_z(L.PITCH_HOUSING_OD, L.PITCH_HOUSING_ID, L.PITCH_HOUSING_Z)
    housing = housing - box((20, 60), (wy - hw / 2, wy + hw / 2), (wz - hh / 2, wz + hh / 2))
    _, sy, sz, _ = L.TRIP_STEM
    housing = housing - cyl_x(L.HOUSING_STEM_HOLE_D, (-60.0, -40.0), sy, sz)     # latch trip-stem guide bush
    sfd, sfx = L.STEM_SPOT_FACE
    housing = housing - cyl_x(sfd, (-60.0, sfx), sy, sz)                         # spot face for its flange
    pphi, pw, pz = L.INSPECTION_PORT
    housing = housing - Rot(0, 0, pphi) * box((L.PITCH_HOUSING_ID / 2 - 5, L.PITCH_HOUSING_OD / 2 + 5),
                                              (-pw / 2, pw / 2), pz)            # latch inspection port
    for ph, zb in L.SADDLE_BOLTS:                                                # M4 tapped, solenoid bracket
        housing = housing - _radial_x(3.3, L.PITCH_HOUSING_ID / 2 - 1, L.PITCH_HOUSING_OD / 2 + 1, ph, zb)
    c.add("M15", "Pitch housing tube", housing, "alu", "S", group="pitch",
          material_label=ALU_6082, tol=0.1)
    z0, z1 = L.CAP_Z
    ub0, ub1 = L.PITCH_BEARING_UPPER_Z
    cap = cyl_z(L.CAP_D, L.CAP_Z) - cyl_z(L.CAP_LIP_ID, (z0 - 1, ub0)) \
        - cyl_z(L.PITCH_BEARING[1], (ub0, ub1)) - cyl_z(L.CAP_TOP_BORE_D, (ub1, z1 + 1))
    for a in range(6):
        ang = math.radians(30 + 60 * a)
        cap = cap - cyl_z(4.5, (z0 - 1, z1 + 1), 50 * math.cos(ang) * 0.94, 50 * math.sin(ang) * 0.94)
    c.add("M16", "Pitch housing cap", cap, "alu", "S", group="pitch", material_label=ALU_6082,
          tol=0.05)
    s0, s1 = L.LOWER_SEAT_Z
    seat = cyl_z(L.LOWER_SEAT_OD, L.LOWER_SEAT_Z) - cyl_z(L.LOWER_SEAT_ID, (s0 + 1, s1 + 1)) \
        - cyl_z(L.SEAT_LIP_ID, (s0 - 1, s0 + 2))
    c.add("M17", "Lower pitch-bearing seat", seat, "alu", "S", group="pitch",
          material_label=ALU_6082, tol=0.05)

    d, D, _ = L.PITCH_BEARING
    for zr, tag in ((L.PITCH_BEARING_UPPER_Z, "upper"), (L.PITCH_BEARING_LOWER_Z, "lower")):
        c.add("B02", "Pitch bearing 6907-2RS", tube_z(D, L.PITCH_OUTER_RING_ID, zr), "bearing", "S",
              group="pitch", tag=tag, bought=True, tol=0.05, note="outer ring")
        c.add("B02", "Pitch bearing 6907-2RS", tube_z(L.PITCH_INNER_RING_OD, d, zr), "bearing", "P",
              group="pitch", tag=tag + " inner ring", bought=True, bom=False, tol=0.05,
              note="inner ring (counted with the outer ring)")

    c.add("B03", "Worm wheel m1 z60", _worm_wheel(), "bronze", "P", group="pitch", bought=True,
          tol=0.05)
    c.add("B04", "Worm m1 single start with shaft", _worm(), "steel", "S", group="pitch",
          bought=True, material_label="Steel (worm)", tol=0.05)
    cx0, cx1 = L.COUPLING_X
    wy, wz = L.WORM_AXIS_YZ
    coupling = cyl_x(L.COUPLING_D, L.COUPLING_X, wy, wz) \
        - cyl_x(L.WORM_SHAFT_D, (cx0 - 1, (cx0 + cx1) / 2), wy, wz) \
        - cyl_x(L.GEARMOTOR_SHAFT[0], ((cx0 + cx1) / 2, cx1 + 1), wy, wz)
    c.add("B05", "Shaft coupling 5-4", coupling, "alu", "S", group="pitch", bought=True,
          material_label="Aluminium (coupling)", tol=0.05)
    _latch(c)
    c.add("M18", "Torsion spring (feather), wire 7", spring_z(L.TORSION_SPRING_D - L.TORSION_SPRING_WIRE,
          L.TORSION_SPRING_WIRE, L.TORSION_SPRING_Z, 10),
          "spring", "P", group="pitch", tol=0.1)
    c.add("B07", "Pitch gearmotor JGA25-370", _gearmotor(), "bought_elec", "S", group="pitch",
          bought=True, tol=0.05)

    # lever, angle, rail, lead screw, KFL08, stepper, coupler, striker, hanger
    lever = box(L.LEVER_X, L.LEVER_Y, L.LEVER_Z)
    for z in (-160.0, -100.0, -40.0, 0.0):
        lever = lever - cyl_x(3.0, (L.LEVER_X[0] - 1, L.LEVER_X[0] + 6), 0, z)     # rail M3
    for z in (-207.0,):
        for y in (-12.0, 12.0):
            lever = lever - cyl_x(4.0, (L.LEVER_X[0] - 1, L.LEVER_X[1] + 1), y, z)    # P10 bolts
    for y in (-12.0, 12.0):
        lever = lever - cyl_x(5.0, (L.LEVER_X[1] - 10, L.LEVER_X[1] + 1), y, 5.0)      # angle bolts
    c.add("M19", "Spring lever", lever, "alu", "S", group="hub", material_label=ALU_6082, tol=0.1)
    leg, t = L.LEVER_ANGLE
    x1 = L.LEVER_X[1]
    angle = _fuse(box((x1, x1 + t), L.LEVER_Y, (L.HUB_TOP_Z[0] - leg, L.HUB_TOP_Z[0])),
                  box((x1, x1 + leg), L.LEVER_Y, (L.HUB_TOP_Z[0] - t, L.HUB_TOP_Z[0])))
    for y in (-12.0, 12.0):
        angle = angle - cyl_x(5.5, (x1 - 1, x1 + t + 1), y, 5.0)
        angle = angle - cyl_z(5.5, (L.HUB_TOP_Z[0] - t - 1, L.HUB_TOP_Z[0] + 1), -42.0, y)
    c.add("M20", "Lever angle 25x25x4", angle, "alu", "S", group="hub", material_label=ALU_6082,
          tol=0.05)
    rail = box(L.RAIL_X, L.RAIL_Y, L.RAIL_Z)
    rail = rail - box((L.RAIL_X[0] - 1, L.RAIL_X[0] + 1.2), (-1.5, 1.5), (L.RAIL_Z[0] - 1, L.RAIL_Z[1] + 1))
    for z in range(int(L.RAIL_Z[0]) + 15, int(L.RAIL_Z[1]), 25):
        rail = rail - cyl_x(6.0, (L.RAIL_X[0] - 1, L.RAIL_X[0] + 3.5), 0, z)
    c.add("B10", "Linear rail MGN12", rail, "bearing", "S", group="hub", bought=True, tol=0.05)
    lx, ly = L.LEADSCREW_XY
    screw = cyl_z(L.LEADSCREW_D, (L.LEADSCREW_BOTTOM_Z, L.LEADSCREW_JOURNAL_TOP_Z), lx, ly)
    c.add("B13", "Lead screw T8x2", screw, "stainless", "S", group="hub", bought=True, tol=0.05)
    kl, kw, kp, kb = L.KFL08
    k0, k1 = L.KFL08_Z
    flange = Pos(lx, ly, k1 - 2.5) * Box(kw, kl - kw, 5) + cyl_z(kw, (k1 - 5, k1), lx, ly - (kl - kw) / 2) \
        + cyl_z(kw, (k1 - 5, k1), lx, ly + (kl - kw) / 2)
    kfl = flange + cyl_z(kb, (k0, k1 - 5), lx, ly)
    kfl = kfl - cyl_z(L.LEADSCREW_D, (k0 - 1, k1 + 1), lx, ly)
    for yy in (-kp / 2, kp / 2):
        kfl = kfl - cyl_z(5.0, (k1 - 6, k1 + 1), lx, ly + yy)
    c.add("B14", "Flange bearing KFL08", kfl, "bearing", "S", group="hub", bought=True, tol=0.05)
    c.add("B15", "Stepper NEMA-17 48 mm", _nema17(), "bought_elec", "S", group="hub", bought=True,
          tol=0.05)
    cz0, cz1 = L.COUPLER_Z
    cm = (cz0 + cz1) / 2
    coupler = cyl_z(L.COUPLER_D, L.COUPLER_Z, lx, ly) - cyl_z(L.NEMA17_SHAFT_D, (cz0 - 1, cm), lx, ly) \
        - cyl_z(L.LEADSCREW_D, (cm, cz1 + 1), lx, ly)
    for zz in (cz0 + 5, cz0 + 8, cz1 - 8, cz1 - 5):
        coupler = coupler - tube_z(L.COUPLER_D + 2, 12, (zz - 0.6, zz + 0.6), lx, ly)
    c.add("B16", "Flexible coupler 5-8", coupler, "alu", "S", group="hub", bought=True,
          material_label="Aluminium (coupler)", tol=0.05)
    c.add("M25", "Stop striker", _striker(), "alu", "S", group="hub", material_label=ALU_6082,
          tol=0.05)
    hanger = box(L.HANGER_X, L.HANGER_Y, L.HANGER_Z)
    for y, z in L.HANGER_M5_YZ:
        hanger = hanger - cyl_x(5.0, (L.HANGER_X[0] - 1, L.HANGER_X[1] + 1), y, z)
    for y in (-20.0, 20.0):
        hanger = hanger - cyl_z(5.0, (L.HANGER_Z[1] - 10, L.HANGER_Z[1] + 1), 99.0, y)
    c.add("M26", "Belt-arc hanger", hanger, "alu", "S", group="hub", material_label=ALU_6082,
          tol=0.05)

    # encoder boards and magnets
    c.add("B08", "Encoder breakout AS5047P", _encoder_board("z", L.PITCH_ENCODER_IC_TOP_Z, (0, 0)),
          "pcb", "S", group="pitch", tag="pitch", bought=True, tol=0.05)
    md, mt = L.MAGNET
    c.add("B09", "Magnet 6x2.5 diametric N35", cyl_z(md, (L.PITCH_MAGNET_FACE_Z, L.PITCH_MAGNET_FACE_Z + mt)),
          "bought_elec", "P", group="pitch", tag="pitch", bought=True,
          material_label="NdFeB magnet N35", tol=0.02)
    hm = L.HINGE_MAGNET_FACE_X
    c.add("B09", "Magnet 6x2.5 diametric N35", cyl_x(md, (hm, hm + mt)), "bought_elec", "S",
          group="hinge", tag="hinge", bought=True, material_label="NdFeB magnet N35", tol=0.02)


# ------------------------------------------------- zero-hold feather latch
def _pol(r, phi):
    a = math.radians(phi)
    return (r * math.cos(a), r * math.sin(a))


def _sector_z(r_in, r_out, a0, a1, zr, n=48):
    """Annular sector about the Z axis, angles in degrees from +X towards +Y."""
    pts = [_pol(r_out, a0 + (a1 - a0) * i / n) for i in range(n + 1)]
    pts += [_pol(r_in, a0 + (a1 - a0) * i / n) for i in range(n, -1, -1)]
    return Pos(0, 0, min(zr)) * extrude(make_face(Polyline(*pts, close=True)), abs(zr[1] - zr[0]))


def _link(p0, p1, w, zr):
    """Flat bar of width w from p0 to p1 (XY), rounded ends, over zr."""
    dx, dy = p1[0] - p0[0], p1[1] - p0[1]
    ln = math.hypot(dx, dy)
    cz, h = (zr[0] + zr[1]) / 2, abs(zr[1] - zr[0])
    bar = Pos((p0[0] + p1[0]) / 2, (p0[1] + p1[1]) / 2, cz) * Rot(0, 0, math.degrees(math.atan2(dy, dx))) * Box(ln, w, h)
    return bar + cyl_z(w, zr, *p0) + cyl_z(w, zr, *p1)


def _about(shape, centre, deg):
    """Rotate a shape about the vertical axis through ``centre`` (XY)."""
    if not deg:
        return shape
    return Pos(centre[0], centre[1], 0) * Rot(0, 0, deg) * Pos(-centre[0], -centre[1], 0) * shape


def latch_geometry() -> dict:
    """Key points of the latch in frame P at beta = 0 (latch.md section 2)."""
    _, _, _, (rr, pr) = L.LATCH_ROLLER
    c1 = _pol(rr, pr)
    a = math.radians(pr)
    et = (-math.sin(a), math.cos(a))
    p = (c1[0] + L.PAWL_ARM_A * et[0], c1[1] + L.PAWL_ARM_A * et[1])
    _, _, tail_end, rt = L.PAWL_TAIL
    t = _pol(rt, tail_end)
    d = (t[0] - p[0], t[1] - p[1])
    b = math.hypot(*d)
    v = (-d[1] / b, d[0] / b)                    # tail's direction of motion as the pawl opens
    c2 = (t[0] + 8.05 * v[0], t[1] + 8.05 * v[1])
    sp = (c2[0] + L.SEAR_L2 * v[0], c2[1] + L.SEAR_L2 * v[1])
    return {"roller": c1, "pivot": p, "tail": t, "v": v, "b": b, "sear_roller": c2, "sear_pivot": sp}


def _box_uv(c, u_deg, su, sv, zr):
    """Box centred at c (XY) with its local X along u_deg, sizes su x sv, over zr."""
    cz, h = (zr[0] + zr[1]) / 2, abs(zr[1] - zr[0])
    return Pos(c[0], c[1], cz) * Rot(0, 0, u_deg) * Box(su, sv, h)


def latch_slot_cut(zr):
    """The collar's slot: planar load flank 30 deg from radial, the roller seated on it (latch.md 2)."""
    _, _, _, (rr, pr) = L.LATCH_ROLLER
    rod = L.LATCH_ROLLER[0]
    a = math.radians(pr)
    rhat, that = (math.cos(a), math.sin(a)), (-math.sin(a), math.cos(a))
    fl = math.radians(L.LATCH_NOTCH_FLANK)
    n = (math.cos(fl) * that[0] + math.sin(fl) * rhat[0], math.cos(fl) * that[1] + math.sin(fl) * rhat[1])
    f = (-math.sin(fl) * that[0] + math.cos(fl) * rhat[0], -math.sin(fl) * that[1] + math.cos(fl) * rhat[1])
    c1 = _pol(rr, pr)
    pc = (c1[0] - (rod / 2 + 0.02) * n[0], c1[1] - (rod / 2 + 0.02) * n[1])     # contact point on the flank
    w, bot = L.LATCH_SLOT
    lf = 40.0
    centre = (pc[0] + w / 2 * n[0] + (lf / 2 - bot) * f[0], pc[1] + w / 2 * n[1] + (lf / 2 - bot) * f[1])
    return _box_uv(centre, math.degrees(math.atan2(n[1], n[0])), w, lf, zr)


def latch_wheel_shapes(pawl_open: float = 0.0, sear_trip: float = 0.0) -> list[tuple]:
    """(id, name, shape, material, label) for the parts that turn with the worm wheel.

    ``pawl_open`` and ``sear_trip`` (degrees) pose the pawl about its pivot and the
    sear about its pin: 0, 0 is latched; PAWL_OPEN_DEG, SEAR_TRIP_DEG is released.
    """
    g = latch_geometry()
    c1, p, t, v, c2, sp = g["roller"], g["pivot"], g["tail"], g["v"], g["sear_roller"], g["sear_pivot"]
    fd = (-v[1], v[0])                       # along the tail face, towards the closing side
    od, idd = LATCH_CARRIER_OD_ID()
    z0, z1 = L.LATCH_CARRIER[1]
    carrier = tube_z(od, idd, (z0, z1))
    ri, ro, lphi, lw = L.CARRIER_LUG
    lug = Pos(0, 0, 0) * Rot(0, 0, lphi) * box((ri - 1, ro), (-lw / 2, lw / 2), (z0, z1))
    carrier = carrier + lug
    sx, sy = L.PAWL_STRAP[0]
    post_xy = _pol(sx, sy)
    for xy, dd in ((p, L.PAWL_PIN_D), (post_xy, 8.0)):
        carrier = carrier - cyl_z(dd, (z0 - 1, z1 + 1), *xy)
    nb, rb, _, dh = L.WHEEL_JOINT
    for a in range(nb):
        carrier = carrier - cyl_z(dh, (z0 - 1, z1 + 1), *_pol(rb, 360.0 * a / nb))
    # pawl: nose (straddles collar and roller), pivot boss, tail arm above the collar
    nz0, nz1 = L.PAWL_NOSE_Z
    rz0, rz1 = L.LATCH_ROLLER[2]
    nri, nro, (na0, na1) = L.PAWL_NOSE
    nose = _sector_z(nri, nro, na0, na1, (nz0, nz1))
    nose = nose - _sector_z(nri - 1, nro + 3, na0 - 1, na1 + 1, (rz0 - 0.2, rz1 + 0.2))
    nose = nose + _link(_pol(35.0, 140.0), p, 12.0, (rz1 + 0.2, nz1))
    nose = nose + _link(_pol(35.0, 140.0), p, 12.0, (nz0, rz0 - 0.2))
    bz0, bz1 = L.PAWL_BOSS_GAP_Z                   # no boss beside the collar: the pin passes its OD 0.4 mm
    boss = cyl_z(12.0, (nz0, bz0), *p) + cyl_z(12.0, (bz1, L.PAWL_TAIL_Z[1]), *p)
    tz = L.PAWL_TAIL_Z
    tri, tro, tail_end, _ = L.PAWL_TAIL
    ts = L.PAWL_TAIL_START
    # tail: an arc at R 38..47.5 (clear of the shaft when the pawl is open 30 deg), with a foot behind
    # the end face that carries the sear contact at R 36
    tail = _sector_z(tri, tro, ts, tail_end + 12.0, tz) + _link(_pol((tri + tro) / 2, ts), p, 10.0, tz)
    fdep, fout = L.PAWL_FOOT
    trm = L.PAWL_TAIL_TRIM
    fc = (t[0] - fdep / 2 * v[0] + (trm - fout) / 2 * fd[0], t[1] - fdep / 2 * v[1] + (trm - fout) / 2 * fd[1])
    tail = tail + _box_uv(fc, math.degrees(math.atan2(v[1], v[0])), fdep, fout + trm, tz)
    ang = math.degrees(math.atan2(v[1], v[0]))
    cut = Pos(t[0] + 50 * v[0], t[1] + 50 * v[1], (tz[0] + tz[1]) / 2) * Rot(0, 0, ang) * Box(100, 200, 20)
    tail = tail - cut
    # trim the end face on the closing side: the sear stop limits the roller to the contact +/- 0.25 mm
    tr = L.PAWL_TAIL_TRIM
    tail = tail - _box_uv((t[0] + (tr + 10) * fd[0] - 2 * v[0], t[1] + (tr + 10) * fd[1] - 2 * v[1]),
                          math.degrees(math.atan2(fd[1], fd[0])), 20.0, 20.0, (tz[0] - 1, tz[1] + 1))
    pawl = nose + boss + tail
    pawl = pawl - cyl_z(L.PAWL_PIN_D, (nz0 - 1, tz[1] + 1), *p) - cyl_z(5.0, (nz0 - 1, nz1 + 1), *c1)
    rod, rpin, rzr, _ = L.LATCH_ROLLER
    roller = tube_z(rod, rpin, rzr, *c1)
    roller_pin = cyl_z(rpin, (nz0, nz1), *c1)
    pawl, roller, roller_pin = (_about(x, p, pawl_open) for x in (pawl, roller, roller_pin))
    sz = L.PAWL_STRAP[1]
    tz0, tz1 = L.LATCH_TOP_PLATE[2]
    strap = _link(p, post_xy, 12.0, sz) - cyl_z(L.PAWL_PIN_D, (sz[0] - 1, sz[1] + 1), *p) \
        - cyl_z(8.0, (sz[0] - 1, sz[1] + 1), *post_xy)
    pawl_pin = cyl_z(L.PAWL_PIN_D, (z0, sz[1]), *p)
    post = cyl_z(8.0, (z0, tz1), *post_xy)
    # sear: needle-bush boss, arm to the roller pin, arm via the elbow to the tab yoke and its roller
    sz0, sz1 = L.SEAR_Z
    pin_d, boss_d, boss_z = L.SEAR_PIVOT
    elbow = _pol(*L.SEAR_ELBOW)
    (tx0, tx1), (ty0, ty1), tzr = L.SEAR_TAB
    q = ((tx0 + tx1) / 2, 0.0)
    sear = _link(sp, c2, 9.0, (sz0, sz1)) + _link(sp, elbow, 8.0, (sz0, sz1)) + _link(elbow, q, 8.0, (sz0, sz1)) \
        + cyl_z(boss_d, boss_z, *sp) + cyl_z(12.0, (sz0, sz1), *c2) + box((tx0, tx1), (ty0, ty1), tzr)
    (kx0, kx1), kz = L.SEAR_TAB_SLOT
    sear = sear - box((kx0, kx1 + 1), (ty0 - 1, ty1 + 1), kz)
    sear = sear - cyl_z(boss_d - 4.0, (boss_z[0] - 1, boss_z[1] + 1), *sp)
    trd, trp, (trx, try_), trz = L.TAB_ROLLER
    sear = sear - cyl_z(trp, (tzr[0] - 1, tzr[1] + 1), trx, try_)
    sod, sid, szr = L.SEAR_ROLLER
    sear_roller = tube_z(sod, sid, szr, *c2)
    sear_roller_pin = cyl_z(sid, (szr[0] - 0.6, sz1), *c2) + cyl_z(10.0, (szr[0] - 0.6, szr[0]), *c2)
    sear = sear - cyl_z(sid, (sz0 - 1, sz1 + 1), *c2)
    tab_roller = tube_z(trd, trp, trz, trx, try_)
    tab_pin = cyl_z(trp, tzr, trx, try_)
    sear, sear_roller, sear_roller_pin, tab_roller, tab_pin = (
        _about(x, sp, sear_trip) for x in (sear, sear_roller, sear_roller_pin, tab_roller, tab_pin))
    sear_pin = cyl_z(pin_d, (sz0, tz1), *sp)
    needle_bush = tube_z(boss_d - 4.0, pin_d, boss_z, *sp)
    # sear stop: hardened eccentric sleeve on a shoulder screw hanging from the top plate, bearing on the
    # closing side of the sear's roller arm (latch.md 2: sets the 0.15 +/- 0.05 mm engagement)
    arm, sd_, gap, szz = L.SEAR_STOP
    st = (sp[0] - arm * v[0] + (4.5 + sd_ / 2 + gap) * fd[0], sp[1] - arm * v[1] + (4.5 + sd_ / 2 + gap) * fd[1])
    stop = cyl_z(sd_, szz, *st) + cyl_z(4.0, (szz[1], tz1), *st)
    # top plate: from beyond the sear stop round past +X to the strap post (clear of the tripped sear)
    pri, pro, _, a_start = L.LATCH_TOP_PLATE
    top = _sector_z(pri, pro, a_start, sy + 4.0, (tz0, tz1)) + _link(_pol(26.0, sy), post_xy, 10.0, (tz0, tz1))
    top = top - cyl_z(pin_d, (tz0 - 1, tz1 + 1), *sp) - cyl_z(8.0, (tz0 - 1, tz1 + 1), *post_xy) \
        - cyl_z(4.0, (tz0 - 1, tz1 + 1), *st)
    bid, bod, bzr = L.WHEEL_BUSH
    fod, fzr = L.WHEEL_BUSH_FLANGE
    bush = tube_z(bod, bid, bzr) + tube_z(fod, bid, fzr)
    q42 = "Steel 42CrMo4 QT"
    return [
        ("B36", "Wheel bush, sintered bronze, flanged 35/41", bush, "bronze", "Sintered bronze (bought)"),
        ("M51", "Latch carrier", carrier, "steel", q42),
        ("M52", "Latch pawl", pawl, "steel", q42 + ", nitrocarburised + post-oxidised"),
        ("B37", "Pawl roller NATV 5-PP (corrosion-protected)", roller, "bearing", None),
        ("M54", "Pawl roller pin", roller_pin, "stainless", "Stainless 17-4PH H900"),
        ("M54", "Pawl pivot pin", pawl_pin, "stainless", "Stainless 17-4PH H900"),
        ("M55", "Pawl strap and post", strap + post, "steel", q42),
        ("M53", "Latch sear", sear, "steel", q42 + ", nitrocarburised + post-oxidised"),
        ("B38", "Sear roller INA RSTO 5", sear_roller, "bearing", "Needle track roller (bought)"),
        ("M54", "Sear roller pin, hardened", sear_roller_pin, "steel", "Steel 100Cr6, 60 HRC"),
        ("B40", "Tab roller 683-2RS stainless", tab_roller, "bearing", "Stainless bearing (bought)"),
        ("M54", "Tab roller pin", tab_pin, "stainless", "Stainless 17-4PH H900"),
        ("M54", "Sear pin, hardened", sear_pin, "steel", "Steel 100Cr6, 60 HRC"),
        ("B41", "Sear pivot needle bush HK0609", needle_bush, "bearing", "Needle bush (bought)"),
        ("M60", "Sear stop, eccentric sleeve on shoulder screw", stop, "steel", "Steel 100Cr6, 60 HRC"),
        ("M56", "Latch top plate", top, "steel", q42),
    ]


def LATCH_CARRIER_OD_ID():
    return L.LATCH_CARRIER[0], L.WHEEL_BUSH[1]


def _radial_x(d, r0, r1, phi, z):
    """Cylinder of diameter d along the radial direction phi (frame S, degrees), from R r0 to r1 at height z."""
    return Rot(0, 0, phi) * cyl_x(d, (r0, r1), 0.0, z)


def _latch(c: _Collector):
    """The zero-hold feather latch (SPEC 3.3, latch.md revision B) in place of the clutch."""
    for id_, name, shp, mat, lab in latch_wheel_shapes():
        it = c.add(id_, name, shp, mat, "P", group="pitch", tol=0.05, bought=id_.startswith("B"),
                   material_label=lab)
        it.extra["latch"] = "wheel"
    cod, czr = L.LATCH_COLLAR
    r_sh = L.PITCH_SHAFT_OD / 2
    collar = tube_z(cod, L.PITCH_SHAFT_OD, czr) - latch_slot_cut((czr[0] - 1, czr[1] + 1))
    for sy_ in (1, -1):        # two keyways A 10 x 8 (3.3 deep in the collar), at +/-Y
        collar = collar - box((-5.0, 5.0), tuple(sorted((sy_ * (r_sh - 1), sy_ * (r_sh + 3.3)))), (czr[0] - 1, czr[1] + 1))
    it = c.add("M50", "Latch collar (one slot)", collar, "steel", "P", group="pitch", tol=0.05,
               material_label="Steel 18CrNiMo7-6, case-hardened 58-62 HRC, CHD >= 0.6")
    it.extra["latch"] = "shaft"
    rod_, rzr = L.RETAINING_RING
    it = c.add("B39", "Retaining ring DIN 471-35", tube_z(rod_, L.PITCH_SHAFT_OD, rzr), "spring", "P",
               group="pitch", bought=True, tol=0.05)
    it.extra["latch"] = "shaft"
    # feather stop: keyed collar with a lug on the shaft (frame P), blocks and a PU buffer on the housing (frame S)
    lri, lro, lphi, lw = L.FEATHER_LUG
    fz = L.FEATHER_STOP_Z
    stop_collar = tube_z(2 * lri + 0.2, L.PITCH_SHAFT_OD, fz) + _sector_z(lri, lro, lphi - lw / 2, lphi + lw / 2, fz)
    it = c.add("M64", "Feather-stop collar and lug", stop_collar, "steel", "P", group="pitch", tol=0.05,
               material_label="Steel 42CrMo4 QT")
    it.extra["latch"] = "shaft"
    bri, bro, bphis = L.FEATHER_BLOCKS
    fblocks = None
    for a0_, a1_ in bphis:
        b = _sector_z(bri, bro, a0_, a1_, fz)
        fblocks = b if fblocks is None else fblocks + b
    c.add("M65", "Feather-stop blocks (-3 and +48 deg)", fblocks, "steel", "S", group="pitch", tol=0.05,
          material_label="Steel 42CrMo4 QT", count=2)
    ubi, ubo, (ua0, ua1), uz = L.FEATHER_BUFFER
    c.add("B44", "Feather-stop buffer, PU 90 Shore A", _sector_z(ubi, ubo, ua0, ua1, uz), "spring", "S",
          group="pitch", bought=True, material_label="Polyurethane 90 Shore A (VERIFY V8 h)", tol=0.05)
    # frame S: wheel stops, trip hook, stem, guide, nuts, return spring, solenoid and its bracket
    ri, ro, phis, wdeg, bz = L.WHEEL_STOP_BLOCKS
    blocks = None
    for ph in phis:
        b = _sector_z(ri, ro, ph - wdeg / 2, ph + wdeg / 2, bz)
        blocks = b if blocks is None else blocks + b
    c.add("M57", "Wheel stop blocks", blocks, "steel", "S", group="pitch", tol=0.05,
          material_label="Steel 42CrMo4 QT", count=2)
    hri, hro, (ha0, ha1), hz = L.TRIP_HOOK
    rri, rro, (ra0, ra1), rz = L.TRIP_RISER
    sd, sy, sz, (sx0, sx1) = L.TRIP_STEM
    hook = _sector_z(hri, hro, ha0, ha1, hz) + _sector_z(rri, rro, ra0, ra1, rz) + box(*L.TRIP_BRIDGE)
    bx0_, bx1_ = L.TRIP_BRIDGE[0]
    hook = hook - cyl_x(4.0, (bx0_ - 1, bx1_ + 1), sy, sz)          # M4 tapped hole for the stem end
    c.add("M58", "Trip hook (arc, riser and bridge)", hook, "stainless", "S", group="pitch", tol=0.05,
          material_label="Stainless 17-4PH H900, hook face nitrided")
    stem = cyl_x(sd, (sx0, sx1), sy, sz) - box((sx0 - 1, sx1 + 1), (sy + sd / 2 - 0.5, sy + sd / 2 + 1), (sz - sd, sz + sd))
    stem = stem + cyl_x(4.0, (sx1, bx1_), sy, sz)
    c.add("M61", "Trip stem (D-flat, M4 end)", stem, "stainless", "S", group="pitch", tol=0.05,
          material_label="Stainless 17-4PH H900")
    god, (gx0, gx1), gfd, gft = L.STEM_GUIDE
    guide = tube_x(god, sd + 0.1, (gx0, gx1), sy, sz) + tube_x(gfd, sd + 0.1, (gx0 - gft, gx0), sy, sz)
    c.add("M62", "Stem guide bush, D-bore", guide, "bronze", "S", group="pitch", tol=0.05,
          material_label="Bronze CuSn8, D-bore (anti-rotation), greased seal")
    nx0, nx1 = L.STEM_NUTS_X
    c.add("B42", "Out-stop nut and lock nut M6 (A4)", tube_x(10.0, sd, (nx0, nx1), sy, sz), "stainless", "S",
          group="pitch", bought=True, tol=0.05, count=2)
    sx0r, sx1r = L.RETURN_SPRING_X
    c.add("B43", "Return spring and washer (1 N at trip)",
          tube_x(18.0, 14.5, (sx0r - 0.5, sx1r - 1.0), sy, sz) + tube_x(18.0, sd + 0.4, (sx1r - 1.0, sx1r), sy, sz),
          "spring", "S", group="pitch", bought=True, tol=0.05)
    dd, ln, (bx0, bx1), pd, pout = L.LATCH_SOLENOID
    sol = cyl_x(dd, (bx0, bx1), sy, sz) + cyl_x(pd, (bx1, bx1 + pout), sy, sz) - cyl_x(sd, (bx1 - 5, bx1 + pout + 1), sy, sz)
    c.add("B06", "Latch solenoid Guardian LT8x16-I-12D", sol, "bought_elec", "S", group="pitch", bought=True,
          tol=0.05)
    # bracket: front plate, two side flanges, and a saddle on the tube OD bolted with 2 x M4 into the wall
    fx0, fx1 = L.SOLENOID_BRACKET_X
    (sa0, sa1), szr, st_ = L.SOLENOID_SADDLE
    r_out = L.PITCH_HOUSING_OD / 2
    br = box((fx0, fx1), (sy - 22, sy + 22), (sz - 15, sz + 15)) - cyl_x(14.0, (fx0 - 1, fx1 + 1), sy, sz)
    for yy in (sy - 22, sy + 19):
        xo = -math.sqrt((r_out + st_ / 2) ** 2 - (yy + 1.5) ** 2)
        br = br + box((fx1, xo), (yy, yy + 3), (sz - 15, sz + 15))
    br = br + _sector_z(r_out, r_out + st_, sa0, sa1, szr)
    sfd, sfx = L.STEM_SPOT_FACE
    br = br - cyl_x(sfd, (-70.0, sfx + 5), sy, sz)
    for ph, zb in L.SADDLE_BOLTS:
        br = br - _radial_x(4.5, r_out - 1, r_out + st_ + 1, ph, zb)
    c.add("M59", "Solenoid bracket with saddle", br, "alu", "S", group="pitch", material_label=ALU_6082, tol=0.05)
    # inspection port cover (gasketed), over the port on the +X/-Y side of the housing
    (pa0, pa1), pz, pt = L.PORT_COVER
    c.add("M63", "Inspection-port cover (gasketed)", _sector_z(r_out, r_out + pt, pa0, pa1, pz), "alu", "S",
          group="pitch", material_label=ALU_6082, tol=0.05)


def _worm_wheel():
    n = L.WORM_WHEEL_TEETH
    m = L.WORM_WHEEL_MODULE
    ro = L.WORM_WHEEL_OD / 2
    rr = L.WORM_WHEEL_PITCH_D / 2 - 1.25 * m
    pts = []
    for k in range(n):
        a0 = 2 * math.pi * k / n
        da = 2 * math.pi / n
        for frac, r in ((0.0, rr), (0.18, rr), (0.32, ro), (0.68, ro), (0.82, rr)):
            a = a0 + frac * da
            pts.append((r * math.cos(a), r * math.sin(a)))
    face = make_face(Polyline(*pts, close=True))
    z0, z1 = L.WORM_WHEEL_Z
    wheel = Pos(0, 0, z0) * extrude(face, z1 - z0)
    hod, hln = L.WHEEL_HUB
    wheel = wheel + cyl_z(hod, (z1, z1 + hln))
    wheel = wheel - cyl_z(L.WHEEL_BORE, (z0 - 1, z1 + hln + 1))
    nb, rb, tap, _ = L.WHEEL_JOINT            # matches the carrier's clearance holes (structure.latch_wheel_shapes)
    for a in range(nb):
        ang = math.radians(360.0 * a / nb)
        wheel = wheel - cyl_z(tap, (z0 - 1, z1 + hln + 1), rb * math.cos(ang), rb * math.sin(ang))
    return wheel


def _worm():
    from build123d import Helix, sweep
    wy, wz = L.WORM_AXIS_YZ
    x0, x1 = L.WORM_X
    root_r = L.WORM_PITCH_D / 2 - 1.25
    tip_r = L.WORM_OD / 2
    lead = math.pi * L.WORM_WHEEL_MODULE
    length = x1 - x0
    core = Pos(0, 0, 0) * Cylinder(root_r, length, align=(Align.CENTER, Align.CENTER, Align.MIN))
    h = Helix(pitch=lead, height=length - 1.6, radius=root_r - 0.2)
    prof_pts = [(root_r - 0.2, -0.75), (tip_r, -0.3), (tip_r, 0.3), (root_r - 0.2, 0.75)]
    from build123d import Vector, Wire, Face
    pts3 = [Vector(r, 0, z) for r, z in prof_pts]
    prof = Face(Wire.make_polygon(pts3, close=True))
    try:
        thread = sweep(prof, h, is_frenet=True)
        worm = core + Pos(0, 0, 0.8) * thread
        if not worm.is_valid:
            raise ValueError
    except Exception:  # noqa: BLE001
        worm = core
        for k in range(int(length / lead)):
            worm = worm + cyl_z(2 * tip_r, (k * lead + 0.6, k * lead + 1.4))
    worm = worm + Pos(0, 0, 0) * cyl_z(L.WORM_SHAFT_D, (L.WORM_SHAFT_X[0] - x0, L.WORM_SHAFT_X[1] - x0))
    # local Z (0..length) -> world X (x0..x1) at (Y wy, Z wz)
    return Pos(x0, wy, wz) * Rot(0, 90, 0) * worm


def _gearmotor():
    wy, wz = L.GEARMOTOR_AXIS_YZ
    g0 = L.GEARMOTOR_X[0]
    g1 = g0 + L.GEARBOX_L
    m1 = g1 + L.GEARMOTOR_MOTOR_L
    gm = cyl_x(L.GEARBOX_D, (g0, g1), wy, wz) + cyl_x(L.GEARMOTOR_MOTOR_D, (g1, m1), wy, wz) \
        + cyl_x(L.GEARMOTOR_TAIL_D, (m1, L.GEARMOTOR_X[1]), wy, wz)
    for y in (-L.GEARMOTOR_FACE_M3_Y, L.GEARMOTOR_FACE_M3_Y):
        gm = gm - cyl_x(3.0, (g0 - 1, g0 + 5), wy + y, wz)
    gm = gm - tube_x(L.GEARBOX_D + 2, L.GEARBOX_D - 1, (g1 - 0.8, g1), wy, wz)
    sd, sl = L.GEARMOTOR_SHAFT
    shaft = cyl_x(sd, (g0 - sl, g0), wy, wz) - box((g0 - sl - 1, g0 - 2), (wy + sd / 2 - 0.5, wy + sd), (wz - sd, wz + sd))
    gm = gm + shaft
    # solder tabs on the tail
    gm = gm + box((L.GEARMOTOR_X[1] - 4, L.GEARMOTOR_X[1]), (wy - 1, wy + 1), (wz + 8, wz + 13))
    return gm


def _nema17():
    w = L.NEMA17_W / 2
    ch = L.STEPPER_CHAMFER
    pts = [(w - ch, -w), (w, -w + ch), (w, w - ch), (w - ch, w), (-w + ch, w), (-w, w - ch),
           (-w, -w + ch), (-w + ch, -w)]
    face = make_face(Polyline(*pts, close=True))
    lx, ly = L.STEPPER_XY
    z0, z1 = L.STEPPER_BODY_Z
    body = Pos(lx, ly, z0) * extrude(face, z1 - z0)
    # the two end caps are proud of the laminated stator by a little: show a groove
    for zz in (z0 + 8, z1 - 8):
        groove = Pos(lx, ly, zz) * extrude(make_face(Polyline(*[(x * 1.04, y * 1.04) for x, y in pts], close=True)), 0.8) \
            - Pos(lx, ly, zz) * extrude(make_face(Polyline(*[(x * 0.985, y * 0.985) for x, y in pts], close=True)), 0.8)
        body = body - groove
    h = L.NEMA17_HOLE_SQ / 2
    for x in (-h, h):
        for y in (-h, h):
            body = body - cyl_z(3.0, (z1 - 4.5, z1 + 1), lx + x, ly + y)
    pd, pt = L.NEMA17_PILOT
    body = body + cyl_z(pd, (z1, z1 + pt), lx, ly)
    shaft_top = L.COUPLER_Z[0] + (L.COUPLER_Z[1] - L.COUPLER_Z[0]) / 2 - 0.5
    shaft = cyl_z(L.NEMA17_SHAFT_D, (z1 + pt, shaft_top), lx, ly)
    shaft = shaft - box((lx + 2.0, lx + 3), (ly - 3, ly + 3), (z1 + pt + 1, shaft_top + 1))
    body = body + shaft
    body = body + box((lx - w - 2.5, lx - w + 0.5), (ly - 8, ly + 8), (z0 + 1, z0 + 9))
    return body


def _striker():
    y0, y1 = L.STRIKER_Y
    z0, z1 = L.STRIKER_Z
    if not L.STRIKER_CHAMFER:
        return box(L.STRIKER_X, L.STRIKER_Y, L.STRIKER_Z)
    reach = L.STRIKER_REACH_Y
    zc = -(reach - y1 * C_T20) / S_T20          # where the chamfer meets the side face
    yc = (reach + z0 * S_T20) / C_T20           # where it meets the bottom face
    pts = [(y0, z1), (y1, z1), (y1, zc), (yc, z0), (-yc, z0), (y0, zc)]
    s = polygon_prism_x(pts, L.STRIKER_X)
    for y in (-10.0, 10.0):
        s = s - cyl_x(5.0, (L.STRIKER_X[0] - 1, L.STRIKER_X[0] + 10), y, (z0 + z1) / 2)
    return s


def _encoder_board(axis: str, ic_top: float, centre, facing: int = 1):
    """AS5047P breakout: 25.4 square board, IC centred on the top face, JST-GH on one edge.

    ``axis`` is the board normal ('z' or 'x'); the IC faces ``facing`` along it,
    with its top face at ``ic_top``. ``centre`` is the board centre in the
    other two coordinates ((X, Y) for 'z', (Y, Z) for 'x').
    """
    bw, _, bt = L.ENCODER_PCB
    h = L.ENCODER_HOLE_SQ / 2
    ic_t = 1.0
    top = ic_top - ic_t
    # local build: board normal +Z, board top at z = 0, IC on top
    board = Pos(0, 0, -bt / 2) * Box(bw, bw, bt)
    for x in (-h, h):
        for y in (-h, h):
            board = board - Pos(x, y, -bt / 2) * Cylinder(L.ENCODER_HOLE_D / 2, bt + 2)
    ic = Pos(0, 0, ic_t / 2) * Box(5.0, 6.4, ic_t)
    # JST-GH on the back face: on the top face its 4.25 mm would hit the magnet-side parts (ASSUMED A21)
    jst = Pos(0, bw / 2 - 2.5, -bt - 2.125) * Box(9.0, 4.5, 4.25)
    caps = Pos(-6.5, 0, 0.4) * Box(1.6, 0.8, 0.8) + Pos(6.5, 0, 0.4) * Box(1.6, 0.8, 0.8)
    part = board + ic + jst + caps
    if axis == "z":
        return Pos(centre[0], centre[1], top) * part
    # normal along +X: local +Z -> world +X (facing +1)
    return Pos(top, centre[0], centre[1]) * Rot(0, 90, 0) * part


# ============================================================= drive (frame A)
def _drive(c: _Collector, g):
    py, pz = g.pulley_c
    tip_d = 2 * (g.pulley_r - L.GT2_PLD)
    pulley = cyl_x(tip_d, (L.BELT_X[0] - 0.5, L.BELT_X[1] + 0.5), py, pz) \
        + cyl_x(L.PULLEY_FLANGE_D, (L.BELT_X[0] - 1.5, L.BELT_X[0] - 0.5), py, pz) \
        + cyl_x(L.PULLEY_FLANGE_D, (L.BELT_X[1] + 0.5, L.BELT_X[1] + 1.5), py, pz) \
        + cyl_x(10.0, (L.BELT_X[1] + 1.5, L.GEN_OUT_SHAFT_END_X), py, pz)
    pulley = pulley - cyl_x(L.GEN_SHAFT_D, (L.BELT_X[0] - 2, L.GEN_OUT_SHAFT_END_X + 1), py, pz)
    c.add("B20", "GT2 pulley 12T 9 mm, bore 5", pulley, "alu", "A", group="drive", bought=True,
          material_label="Aluminium (pulley)", tol=0.03)
    i0, i1 = L.IDLER_X
    ft = L.IDLER_FLANGE_T
    cr = g.idler_contact_r
    for k, (iy, iz) in enumerate(g.idlers):
        tag = "+Y" if iy >= 0 else "-Y"
        idl = cyl_x(2 * cr, (i0, i1), iy, iz) + cyl_x(L.IDLER_FLANGE_D, (i0 - ft, i0), iy, iz) \
            + cyl_x(L.IDLER_FLANGE_D, (i1, i1 + ft), iy, iz)
        idl = idl - cyl_x(L.IDLER_BORE, (i0 - ft - 1, i1 + ft + 1), iy, iz)
        c.add("B21", "Smooth idler GT2 9 mm, bore 5", idl, "bearing", "A", group="drive", tag=tag,
              bought=True, tol=0.03)
        b0, b1 = L.IDLER_BOLT_X
        bolt = cyl_x(L.IDLER_BORE, (i0 - ft, b1), iy, iz) + cyl_x(8.5, (b0, i0 - ft), iy, iz)
        bolt = bolt - hex_prism_x(4.0, (b0 - 0.1, b0 + 1.2), iy, iz)
        c.add("B22", "Idler bolt M5", bolt, "stainless", "A", group="drive", tag=tag, bought=True,
              tol=0.03)
    c.add("B23", "Generator 8108 outrunner", _generator(), "bought_elec", "A", group="drive",
          bought=True, tol=0.05)
    gy, gz = L.GEN_AXIS_YZ
    c.add("B08", "Encoder breakout AS5047P",
          _encoder_board("x", L.GEN_ENCODER_IC_TOP_X, (gy, gz)), "pcb", "A", group="drive",
          tag="generator", bought=True, tol=0.05)
    md, mt = L.MAGNET
    gm = L.GEN_MAGNET_FACE_X
    c.add("B09", "Magnet 6x2.5 diametric N35", cyl_x(md, (gm, gm + mt), gy, gz), "bought_elec", "A",
          group="drive", tag="generator", bought=True, material_label="NdFeB magnet N35", tol=0.02)


def _generator():
    gy, gz = L.GEN_AXIS_YZ
    f0 = L.GEN_MOUNT_FACE_X
    c0, c1 = L.GEN_CAN_X
    stator = cyl_x(L.GEN_MOUNT_FACE_D, (f0, c0 - 1.0), gy, gz) \
        - cyl_x(L.GEN_CENTRE_RELIEF_D, (f0 - 1, c0), gy, gz)
    for a in range(4):
        ang = math.radians(45 + 90 * a)
        r = L.GEN_M3_PCD / 2
        stator = stator - cyl_x(3.0, (f0 - 1, f0 + 3.5), gy + r * math.cos(ang), gz + r * math.sin(ang))
    can = cyl_x(L.GEN_CAN_D, (c0, c1), gy, gz)
    can = can - tube_x(L.GEN_CAN_D + 2, L.GEN_CAN_D - 1.2, (c0 + 6, c0 + 7.2), gy, gz)
    for a in range(6):
        ang = math.radians(60 * a)
        can = can - cyl_x(9.0, (c1 - 1.2, c1 + 1), gy + 26 * math.cos(ang), gz + 26 * math.sin(ang))
    shaft = cyl_x(L.GEN_SHAFT_D, (c1, L.GEN_OUT_SHAFT_END_X), gy, gz) \
        + cyl_x(L.GEN_SHAFT_D, (L.GEN_REAR_SHAFT_END_X, c0), gy, gz)
    return stator + can + shaft


# =============================================================== 3.5 Hinge (A)
def _hinge(c: _Collector):
    d, D, B = L.HINGE_BEARING
    for sx, tag in ((1, "+X"), (-1, "-X")):
        def X(a, b):
            return tuple(sorted((sx * a, sx * b)))
        xr = X(*L.CHEEK_X)
        cheek = box(xr, L.CHEEK_Y, L.CHEEK_Z)
        top_edges = cheek.edges().filter_by(Axis.X).group_by(Axis.Z)[-1]
        cheek = fillet(top_edges, L.CHEEK_TOP_R)
        cheek = cheek - cyl_x(L.CHEEK_BORE_D, (xr[0] - 1, xr[1] + 1))
        for a in range(4):
            ang = math.radians(45 + 90 * a)
            r = L.RETAINER_PCD / 2
            cheek = cheek - cyl_x(5.0, X(L.CHEEK_X[1] - 12, L.CHEEK_X[1] + 0.5), r * math.cos(ang), r * math.sin(ang))
        # base bolts and a lightening window below the bearing
        cheek = cheek - box((xr[0] - 1, xr[1] + 1), (-90, 90), (-235, -110))
        for y in (-130.0, -60.0, 60.0, 130.0):
            cheek = cheek - cyl_z(6.0, (L.CHEEK_Z[0] - 1, L.CHEEK_Z[0] + 16), sx * 150.0, y)
        c.add("M27", "Hinge cheek 20 mm", cheek, "alu", "A", group="hinge", tag=tag,
              material_label=ALU_6082, tol=0.1)
        xc = sx * L.HINGE_BEARING_XC
        bx = (xc - B / 2, xc + B / 2)
        c.add("B24", "Hinge bearing 6005-2RS", tube_x(D, L.HINGE_OUTER_RING_ID, bx), "bearing", "A",
              group="hinge", tag=tag, bought=True, tol=0.05, note="outer ring")
        c.add("B24", "Hinge bearing 6005-2RS", tube_x(L.HINGE_INNER_RING_OD, d, bx), "bearing", "S",
              group="hinge", tag=tag + " inner ring", bought=True, bom=False, tol=0.05,
              note="inner ring (counted with the outer ring)")
        ret = tube_x(L.RETAINER_OD, L.RETAINER_ID, X(*L.RETAINER_X))
        for a in range(4):
            ang = math.radians(45 + 90 * a)
            r = L.RETAINER_PCD / 2
            ret = ret - cyl_x(5.5, X(L.RETAINER_X[0] - 1, L.RETAINER_X[1] + 1), r * math.cos(ang), r * math.sin(ang))
        c.add("M28", "Bearing retainer", ret, "alu", "A", group="hinge", tag=tag,
              material_label=ALU_6082, tol=0.05)
        if sx > 0:
            bolts = None
            for a in range(4):
                ang = math.radians(45 + 90 * a)
                r = L.RETAINER_PCD / 2
                y, z = r * math.cos(ang), r * math.sin(ang)
                b = cyl_x(8.5, (L.RETAINER_X[1], L.RETAINER_X[1] + 5), y, z) \
                    + cyl_x(5.0, (L.CHEEK_X[1] - 10, L.RETAINER_X[1]), y, z)
                b = b - hex_prism_x(4.0, (L.RETAINER_X[1] + 2, L.RETAINER_X[1] + 5.1), y, z)
                bolts = b if bolts is None else bolts + b
            c.add("B25", "Socket screw M5x16", bolts, "stainless", "A", group="hinge", tag="+X retainer",
                  bought=True, count=4, tol=0.05)
    c.add("B08", "Encoder breakout AS5047P",
          _encoder_board("x", L.HINGE_ENCODER_IC_TOP_X, (0.0, 0.0)), "pcb", "A", group="hinge",
          tag="hinge", bought=True, tol=0.05)

    for sy, tag in ((1, "+Y"), (-1, "-Y")):
        def Y(a, b):
            return tuple(sorted((sy * a, sy * b)))
        rp = box(L.REACTION_PLATE_X, Y(*L.REACTION_PLATE_Y), L.REACTION_PLATE_Z)
        c.add("M29", "Reaction plate 10 mm", rp, "alu", "A", group="hinge", tag=tag,
              material_label=ALU_6082, tol=0.1)
        for zr, zt in (((-280.0, -240.0), "low"), ((-30.0, 10.0), "high")):
            blk = box(L.SPACER_BLOCK_X, Y(*L.REACTION_PLATE_Y), zr)
            c.add("M30", "Spacer block", blk, "alu", "A", group="hinge", tag=f"{tag} {zt}",
                  material_label=ALU_6082, tol=0.1)
        w = L.STOP_POST_WALL
        yr = Y(*L.STOP_POST_Y)
        post = box(L.STOP_POST_X, yr, L.STOP_POST_Z) - box(
            (L.STOP_POST_X[0] + w, L.STOP_POST_X[1] - w), (yr[0] + w, yr[1] - w),
            (L.STOP_POST_Z[0] - 1, L.STOP_POST_Z[1] - w))
        c.add("M31", "Stop post 26x25x3", post, "alu", "A", group="hinge", tag=tag,
              material_label=ALU_6082, tol=0.1)


# ======================================================= 3.6 Head, yaw, post (A)
def _head(c: _Collector):
    bz = L.BASE_PLATE_Z
    plate = box(L.BASE_PLATE_X, L.BASE_PLATE_Y, bz)
    zc = (bz[0] - 1, bz[1] + 1)
    yx, yy = L.YAW_AXIS_XY
    plate = plate - cyl_z(L.YAW_SHAFT_ID, zc, yx, yy)
    for a in range(L.YAW_FLANGE_BOLTS):
        ang = math.radians(30 + 60 * a)
        plate = plate - cyl_z(10.5, zc, yx + 65 * math.cos(ang), yy + 65 * math.sin(ang))
    for x in L.TAIL_SADDLE_X:
        for y in (-23.0, 23.0):
            plate = plate - cyl_z(6.5, zc, x, y)
    for x in L.ANEMO_SADDLE_X:
        for y in (L.ANEMO_BOOM_YZ[0] - 15.5, L.ANEMO_BOOM_YZ[0] + 15.5):
            plate = plate - cyl_z(6.5, zc, x, y)
    for x in (L.DUMP_X[0] + 4, L.DUMP_X[1] - 4):
        for y in (-20.0, 20.0):
            plate = plate - cyl_z(5.0, (bz[0] - 1, bz[0] + 10), x, y)
    for x in (-150.0, 150.0):
        for y in (-130.0, -60.0, 60.0, 130.0):
            plate = plate - cyl_z(6.5, zc, x, y)
    c.add("M32", "Head base plate 15 mm", plate, "alu", "A", group="head",
          material_label=ALU_6082, tol=0.2)

    fz = L.YAW_FLANGE_Z
    flange = cyl_z(L.YAW_FLANGE_D, fz, yx, yy) - cyl_z(L.YAW_SHAFT_ID, (fz[0] - 1, fz[1] + 1), yx, yy)
    for a in range(L.YAW_FLANGE_BOLTS):
        ang = math.radians(30 + 60 * a)
        flange = flange - cyl_z(10.5, (fz[0] - 1, fz[1] + 1), yx + 65 * math.cos(ang), yy + 65 * math.sin(ang))
    c.add("M33", "Yaw flange 160x12", flange, "steel", "A", group="yaw", tol=0.1)
    c.add("M34", "Yaw shaft 50x6", tube_z(L.YAW_SHAFT_OD, L.YAW_SHAFT_ID, L.YAW_SHAFT_Z, yx, yy),
          "steel", "A", group="yaw", tol=0.1)
    hz = L.YAW_HOUSING_Z
    hid = L.YAW_HOUSING_OD - 2 * L.YAW_HOUSING_WALL
    fd, ft = L.YAW_HOUSING_FLANGE
    housing = tube_z(L.YAW_HOUSING_OD, hid, hz, yx, yy) + tube_z(fd, L.YAW_HOUSING_OD - 0.01, (hz[0], hz[0] + ft), yx, yy)
    for a in range(6):
        ang = math.radians(60 * a)
        housing = housing - cyl_z(13.0, (hz[0] - 1, hz[0] + ft + 1), yx + 80 * math.cos(ang), yy + 80 * math.sin(ang))
    c.add("M35", "Yaw housing (post top)", housing, "steel", "A", group="yaw", tol=0.1)
    d, D, T = L.YAW_BEARING
    for k, zr in enumerate(L.YAW_BEARING_Z):
        lip = (zr[1], zr[1] + 3) if k == 0 else (zr[0] - 3, zr[0])
        seat = tube_z(hid, D, zr, yx, yy) + tube_z(hid, L.YAW_SEAT_LIP_ID, lip, yx, yy)
        c.add("M36", "Yaw bearing seat", seat, "steel", "A", group="yaw", tag=("upper", "lower")[k], tol=0.1)
        brg = tube_z(D, L.YAW_CUP_ID, zr, yx, yy) + tube_z(L.YAW_CONE_OD, d, zr, yx, yy) \
            + tube_z(L.YAW_CUP_ID - 1.0, L.YAW_CONE_OD + 1.0, (zr[0] + 2, zr[1] - 2), yx, yy)
        c.add("B26", "Yaw bearing 32010 (tapered roller)", brg, "bearing", "A", group="yaw",
              tag=("upper", "lower")[k], bought=True, tol=0.1)

    sd, sl = L.SLIP_RING_BODY
    fd2, ft2, pcd = L.SLIP_RING_FLANGE
    z0 = L.SLIP_RING_Z[0]
    body_bot = z0 + 12.0
    body = cyl_z(sd, (body_bot, body_bot + sl), yx, yy) + cyl_z(14.0, (body_bot + sl, L.SLIP_RING_Z[1]), yx, yy)
    fl = cyl_z(fd2, (body_bot - ft2, body_bot), yx, yy)
    for a in range(3):
        ang = math.radians(90 + 120 * a)
        fl = fl - cyl_z(3.4, (body_bot - ft2 - 1, body_bot + 1), yx + pcd / 2 * math.cos(ang), yy + pcd / 2 * math.sin(ang))
    leads = cyl_z(8.0, (z0, body_bot - ft2), yx, yy)
    c.add("B27", "Slip ring capsule 6 x 2 A", body + fl + leads, "bought_elec", "A", group="yaw",
          bought=True, tol=0.05)
    sz1 = L.YAW_SHAFT_Z[0]
    clamp = tube_z(L.YAW_SHAFT_ID, 14.0, (sz1 - 10, sz1 + 10), yx, yy)
    c.add("M37", "Slip-ring rotor clamp", clamp, "alu", "A", group="yaw", material_label=ALU_6082, tol=0.05)

    # post, base plate and guy collar
    pfd, pft = L.POST_FLANGE
    post = tube_z(L.POST_OD, L.POST_BORE, L.POST_Z, yx, yy) + tube_z(pfd, L.POST_OD - 0.01, (L.POST_Z[1] - pft, L.POST_Z[1]), yx, yy)
    for a in range(6):
        ang = math.radians(60 * a)
        post = post - cyl_z(13.0, (L.POST_Z[1] - pft - 1, L.POST_Z[1] + 1), yx + 80 * math.cos(ang), yy + 80 * math.sin(ang))
    c.add("M38", "Post 114.3x6 with top flange", post, "steel", "A", group="post", tol=0.3)
    bw, bt = L.POST_BASE
    base = box((yx - bw / 2, yx + bw / 2), (yy - bw / 2, yy + bw / 2), (L.GROUND_Z, L.GROUND_Z + bt))
    for x in (-115.0, 115.0):
        for y in (-115.0, 115.0):
            base = base - cyl_z(22.0, (L.GROUND_Z - 1, L.GROUND_Z + bt + 1), yx + x, yy + y)
    for a in range(4):
        gus = Pos(yx, yy, 0) * Rot(0, 0, 45 + 90 * a) * box((L.POST_OD / 2, 140.0), (-5, 5), (L.GROUND_Z + bt, L.GROUND_Z + bt + 100))
        base = base + gus
    c.add("M39", "Post base plate 300x300x15 with gussets", base, "steel", "A", group="post", tol=0.3)
    cod, ch = L.GUY_COLLAR
    gz = L.GUY_COLLAR_Z
    collar = tube_z(cod, L.POST_OD, (gz - ch / 2, gz + ch / 2), yx, yy)
    for a in range(3):
        lug = Pos(yx, yy, 0) * Rot(0, 0, 90 + 120 * a) * (
            box((cod / 2 - 2, cod / 2 + 38), (-6, 6), (gz - ch / 2, gz + ch / 2))
            - cyl_y(13.0, (-7, 7), cod / 2 + 25, gz))
        collar = collar + lug
    c.add("M40", "Guy collar with three lugs", collar, "steel", "A", group="post", tol=0.2)

    # tail boom, U-bolts, vane
    ty, tz = L.TAIL_BOOM_YZ
    c.add("M41", "Tail boom 40x2", tube_x(L.TAIL_BOOM_OD, L.TAIL_BOOM_OD - 2 * L.TAIL_BOOM_WALL,
          L.TAIL_BOOM_X, ty, tz), "alu", "A", group="tail", material_label=ALU_6063, tol=0.1)
    tr = L.TAIL_BOOM_OD / 2
    for x in L.TAIL_SADDLE_X:
        sw = L.TAIL_SADDLE_W / 2
        # the boom rests on the plate (its underside is at the plate's top face), so the
        # saddle is a cradle split under the tube: two wings hugging its lower sides
        sad = box((x - sw, x + sw), (ty - tr - 12, ty + tr + 12), (L.BASE_PLATE_Z[1], tz - tr + 14)) \
            - cyl_x(L.TAIL_BOOM_OD, (x - sw - 1, x + sw + 1), ty, tz) \
            - box((x - sw - 1, x + sw + 1), (ty - 8, ty + 8), (L.BASE_PLATE_Z[1] - 1, tz))
        for y in (ty - tr - L.UBOLT_D / 2, ty + tr + L.UBOLT_D / 2):
            sad = sad - cyl_z(6.5, (L.BASE_PLATE_Z[1] - 1, tz), x, y)
        c.add("M49", "Tail-boom saddle", sad, "alu", "A", group="tail", tag=f"X {x:.0f}",
              material_label=ALU_6082, tol=0.05)
        c.add("B28", "U-bolt M6 for 40 mm tube, with nuts", _ubolt(x, ty, tz, tr), "stainless", "A",
              group="tail", tag=f"X {x:.0f}", bought=True, tol=0.05)
    c.add("M42", "Tail vane half, upper", box(L.VANE_X, (-L.VANE_T / 2, L.VANE_T / 2), L.VANE_UPPER_Z),
          "pp", "A", group="tail", tol=0.2)
    c.add("M43", "Tail vane half, lower", box(L.VANE_X, (-L.VANE_T / 2, L.VANE_T / 2), L.VANE_LOWER_Z),
          "pp", "A", group="tail", tol=0.2)

    # anemometer boom, mast, saddles, U-bolts, anemometer
    ay, az = L.ANEMO_BOOM_YZ
    ax0 = L.ANEMO_TEE[0] + L.TEE_SOCKET_STOP
    aid = L.ANEMO_BOOM_OD - 2 * L.ANEMO_BOOM_WALL
    c.add("M44", "Anemometer boom 25x2", tube_x(L.ANEMO_BOOM_OD, aid, (ax0, L.ANEMO_BOOM_X_SPEC[1]), ay, az),
          "alu", "A", group="anemometer", material_label=ALU_6063, tol=0.05)
    mx, my = L.ANEMO_MAST_XY
    mz0 = L.ANEMO_TEE[2] + L.TEE_SOCKET_STOP
    c.add("M45", "Anemometer mast 25x2", tube_z(L.ANEMO_BOOM_OD, aid, (mz0, L.ANEMO_MAST_TOP_Z), mx, my),
          "alu", "A", group="anemometer", material_label=ALU_6063, tol=0.05)
    r = L.ANEMO_BOOM_OD / 2
    for x in L.ANEMO_SADDLE_X:
        sw = L.SADDLE_W / 2
        sad = box((x - sw, x + sw), (ay - 18, ay + 18), (L.BASE_PLATE_Z[1], az - r + 3)) \
            - cyl_x(L.ANEMO_BOOM_OD, (x - sw - 1, x + sw + 1), ay, az)
        for y in (ay - 15.5, ay + 15.5):
            sad = sad - cyl_z(6.5, (L.BASE_PLATE_Z[1] - 1, az), x, y)
        c.add("M46", "Anemometer-boom saddle", sad, "alu", "A", group="anemometer", tag=f"X {x:.0f}",
              material_label=ALU_6082, tol=0.05)
        c.add("B35", "U-bolt M6 for 25 mm tube, with nuts", _ubolt(x, ay, az, r), "stainless", "A", group="anemometer",
              tag=f"X {x:.0f}", bought=True, tol=0.05)
    c.add("B29", "Anemometer, 3-cup with reed switch", _anemometer(), "bought_elec", "A",
          group="anemometer", bought=True, tol=0.1)

    # dump resistor, battery
    dx0, dx1 = L.DUMP_X
    dz0, dz1 = L.DUMP_Z
    res = box(L.DUMP_X, L.DUMP_Y, (dz1 - 3, dz1))
    for x in (dx0 + 4, dx1 - 4):
        for y in (-20.0, 20.0):
            res = res - cyl_z(4.5, (dz1 - 4, dz1 + 1), x, y)
    bodyr = box((dx0 + 11, dx1 - 11), (-15, 15), (dz0 + 4, dz1 - 3))
    for k in range(-2, 3):
        bodyr = bodyr - box((dx0 + 10, dx1 - 10), (k * 6 - 1, k * 6 + 1), (dz0 + 3, dz0 + 12))
    core = cyl_x(14.0, (dx0 + 11, dx1 - 11), 0, dz0 + 18)
    res = res + bodyr + core
    res = res + box((dx0 + 5, dx0 + 11), (-4, 4), (dz0 + 15, dz0 + 21)) + box((dx1 - 11, dx1 - 5), (-4, 4), (dz0 + 15, dz0 + 21))
    c.add("B30", "Dump resistor 50 W 10 ohm, aluminium clad", res, "bought_elec", "A", group="electrical",
          bought=True, tol=0.1)
    bx0, bx1 = L.BATTERY_X
    by0, by1 = L.BATTERY_Y
    bz0, bz1 = L.BATTERY_Z
    batt = box((bx0 + 2, bx1 - 2), (by0 + 2, by1 - 2), (bz0, bz1 - 20)) + box(L.BATTERY_X, L.BATTERY_Y, (bz1 - 20, bz1))
    for x in (bx0 + 40, bx1 - 40):
        batt = batt + cyl_z(20.0, (bz1, bz1 + 12), x, 0) - cyl_z(8.0, (bz1 + 2, bz1 + 13), x, 0)
    c.add("B31", "Battery 24 V LiFePO4 8S 20 Ah in weatherproof box", batt, "battery", "A",
          group="electrical", bought=True, tol=0.5)


def _ubolt(x, yc, zc, tube_r):
    """M6 U-bolt round a tube on the base plate, legs through the plate, nuts underneath."""
    rb = tube_r + L.UBOLT_D / 2
    wd = L.UBOLT_D
    torus = Pos(x, yc, zc) * Rot(0, 90, 0) * Torus(rb, wd / 2)
    torus = torus - box((x - 10, x + 10), (yc - rb - 10, yc + rb + 10), (zc - rb - 10, zc))
    pz = L.BASE_PLATE_Z
    legs = cyl_z(wd, (pz[0] - 8, zc), x, yc - rb) + cyl_z(wd, (pz[0] - 8, zc), x, yc + rb)
    nuts = hex_prism_z(10.0, (pz[0] - 5, pz[0]), x, yc - rb) + hex_prism_z(10.0, (pz[0] - 5, pz[0]), x, yc + rb)
    nuts = nuts - cyl_z(wd, (pz[0] - 6, pz[0] + 1), x, yc - rb) - cyl_z(wd, (pz[0] - 6, pz[0] + 1), x, yc + rb)
    plate = box((x - 8, x + 8), (yc - rb - 7, yc + rb + 7), (pz[0] - 8, pz[0] - 5))
    plate = plate - cyl_z(wd, (pz[0] - 9, pz[0] - 4), x, yc - rb) - cyl_z(wd, (pz[0] - 9, pz[0] - 4), x, yc + rb)
    return torus + legs + nuts + plate


def _anemometer():
    mx, my = L.ANEMO_MAST_XY
    sd, sl = L.ANEMO_SPIGOT
    bd, bh = L.ANEMO_BODY
    zb = L.ANEMO_BODY_BOTTOM_Z
    a = cyl_z(sd, (zb - sl, zb), mx, my) + cyl_z(bd, (zb, zb + bh), mx, my)
    a = a - tube_z(bd + 2, bd - 2, (zb + 12, zb + 13), mx, my)
    zc = L.ANEMO_CUP_Z
    a = a + cyl_z(30.0, (zb + bh, zb + bh + 8), mx, my)
    rc = L.ANEMO_CUP_CIRCLE_D / 2
    cup_r = 25.0
    for k in range(3):
        ang = 90 + 120 * k
        arm = Pos(mx, my, zc) * Rot(0, 0, ang) * Pos((rc - cup_r + 14) / 2, 0, 0) * Rot(0, 90, 0) * \
            Cylinder(2.0, rc - cup_r - 14 + 2)
        shell = Sphere(cup_r) - Sphere(cup_r - 1.5)
        shell = shell - Pos(cup_r, 0, 0) * Box(2 * cup_r, 2 * cup_r + 2, 2 * cup_r + 2)
        cup = Pos(mx, my, zc) * Rot(0, 0, ang) * Pos(rc, 0, 0) * Rot(0, 0, 90) * shell
        a = a + arm + cup
    return a


# ======================================================== electrical (frame A)
def _electrical(c: _Collector):
    cx, cy = L.PCB_CENTRE_XY
    x0, y0 = cx - L.PCB_W / 2, cy - L.PCB_H / 2
    zb = L.PCB_BOTTOM_Z
    zt = zb + L.PCB_T
    board = box((x0, x0 + L.PCB_W), (y0, y0 + L.PCB_H), (zb, zt))
    for hx, hy in L.PCB_HOLES:
        board = board - cyl_z(L.PCB_HOLE_D, (zb - 1, zt + 1), x0 + hx, y0 + hy)
    step = _pcb_step()
    if step is not None:
        shp, path = step
        c.add("M47", "Controller PCB 130x100", shp, "pcb", "A", group="electrical", tol=0.1,
              note=f"from {path}")
    else:
        c.add("M47", "Controller PCB 130x100 (placeholder)", board, "pcb", "A", group="electrical",
              placeholder=True, tol=0.1, note="replaced by the pcb repo's STEP when one exists")
    comps = []
    for k in range(3):                                   # power terminal blocks, y = 0 edge
        xs = x0 + 20 + 32 * k
        comps.append(box((xs, xs + 16), (y0 + 0.5, y0 + 11), (zt, zt + 14)))
    for k in range(9):                                   # signal headers, y = 100 edge
        xs = x0 + 8 + 13.5 * k
        comps.append(box((xs, xs + 10), (y0 + L.PCB_H - 7, y0 + L.PCB_H - 0.5), (zt, zt + 8)))
    comps.append(box((x0 + L.PCB_W - 7.5, x0 + L.PCB_W + 0.5), (cy + 5, cy + 14), (zt, zt + 3.2)))  # USB-C
    comps.append(box((x0 + L.PCB_W - 15, x0 + L.PCB_W), (cy - 20, cy - 6), (zt, zt + 1.8)))       # microSD
    for k in range(3):                                   # bulk capacitors
        comps.append(cyl_z(10.0, (zt, zt + 20), x0 + 22 + 14 * k, y0 + 30))
    comps.append(box((x0 + 70, x0 + 82), (y0 + 22, y0 + 34), (zt, zt + 8)))     # inductor
    comps.append(box((x0 + 88, x0 + 98), (cy + 12, cy + 22), (zt, zt + 1.6)))   # MCU
    for k in range(6):                                   # bridge MOSFETs
        xs = x0 + 18 + 10 * k
        comps.append(box((xs, xs + 7), (y0 + 46, y0 + 56), (zt, zt + 4.5)))
    from functools import reduce
    comp = reduce(lambda a, b: a + b, comps)
    if step is None:
        c.add("M48", "Controller PCB components (placeholder)", comp, "bought_elec", "A", group="electrical",
              placeholder=True, tol=0.1, note="representative blocks, <= 25 mm tall (ASSUMED A20)")

    # cable glands on the enclosure walls
    gz = L.GLAND_Z
    w = L.ENCL_WALL_T
    hole20, hex20 = L.GLAND_M20
    hole16, hex16 = L.GLAND_M16
    ey0, ey1 = L.ENCL_Y
    for x in L.GLAND_M20_X:
        g = hex_prism_y(hex20, (ey0 - 7, ey0), x, gz) + cyl_y(22.0, (ey0 - 19, ey0 - 7), x, gz) \
            + cyl_y(20.0, (ey0, ey0 + w), x, gz) + hex_prism_y(hex20, (ey0 + w, ey0 + w + 5), x, gz)
        g = g - cyl_y(9.0, (ey0 - 20, ey0 + w + 6), x, gz)
        c.add("B32", "Cable gland M20x1.5", g, "bought_elec", "A", group="electrical", tag=f"X {x:.0f}",
              bought=True, material_label="Nylon cable gland", tol=0.05)
    for x in L.GLAND_M16_X:
        g = hex_prism_y(hex16, (ey1, ey1 + 6), x, gz) + cyl_y(18.0, (ey1 + 6, ey1 + 16), x, gz) \
            + cyl_y(16.0, (ey1 - w, ey1), x, gz) + hex_prism_y(hex16, (ey1 - w - 5, ey1 - w), x, gz)
        g = g - cyl_y(6.0, (ey1 - w - 6, ey1 + 17), x, gz)
        c.add("B33", "Cable gland M16x1.5", g, "bought_elec", "A", group="electrical", tag=f"X {x:.0f}",
              bought=True, material_label="Nylon cable gland", tol=0.05)
    ex0 = L.ENCL_X[0]
    vy, vz = L.GLAND_VENT_YZ
    v = hex_prism_x(15.0, (ex0 - 6, ex0), vy, vz) + cyl_x(14.0, (ex0 - 14, ex0 - 6), vy, vz) \
        + cyl_x(12.0, (ex0, ex0 + w), vy, vz) + hex_prism_x(15.0, (ex0 + w, ex0 + w + 4), vy, vz)
    c.add("B34", "Breather vent M12x1.5", v, "bought_elec", "A", group="electrical", bought=True,
          material_label="Nylon breather vent", tol=0.05)


def _pcb_root():
    env = os.environ.get("LANTERN_PCB")
    if env:
        return Path(env)
    return Path(__file__).resolve().parents[5] / "pcb"


def _pcb_step():
    """The controller board from the pcb repo, placed per SPEC 7, or None.

    KiCad exports the board with its bottom face at z = 0 and the board
    outline in +x, +y from the board origin; the board's lower-left corner
    goes to (X -335, Y -50) and its bottom to Z -269.
    """
    d = _pcb_root() / "hardware" / "lantern-330g-controller"
    steps = sorted(list(d.glob("*.step")) + list(d.glob("*.stp")) + list(d.glob("*/*.step")))
    if not steps:
        return None
    from build123d import import_step
    path = steps[0]
    try:
        shp = import_step(str(path))
    except Exception:  # noqa: BLE001
        return None
    bb = shp.bounding_box()
    cx, cy = L.PCB_CENTRE_XY
    x0, y0 = cx - L.PCB_W / 2, cy - L.PCB_H / 2
    # align the board outline (the bbox may include connectors overhanging an edge)
    dx = x0 - bb.min.X if abs(bb.size.X - L.PCB_W) < 3 else cx - (bb.min.X + bb.max.X) / 2
    dy = y0 - bb.min.Y if abs(bb.size.Y - L.PCB_H) < 3 else cy - (bb.min.Y + bb.max.Y) / 2
    zb = 0.0 if -3.0 <= bb.min.Z <= 0.1 else bb.min.Z
    shp = Pos(dx, dy, L.PCB_BOTTOM_Z - zb) * shp
    return shp, str(path)


# ================================================================== carriage (S)
def roller_offset(theta: float, r: float, side: int) -> float:
    """|Y_S| of a roller axle so the roller touches its reaction plate at swing theta.

    The roller centre in frame S is (X -104, Y_S = side * s, Z_S = -r); in
    frame A its Y is side*s*cos(theta) + r*sin(theta), which must equal
    side * (contact Y - roller radius).
    """
    th = math.radians(theta)
    yc = L.ROLLER_CONTACT_Y - L.ROLLER_D / 2
    return (yc - side * r * math.sin(th)) / math.cos(th)


def carriage_items(r: float = L.CARRIAGE_R_DEFAULT, theta: float = 0.0) -> list[Item]:
    """Spring carriage and everything riding on it, at carriage position r and swing theta."""
    c = _Collector()
    zc = -r
    kw = dict(group="carriage", carriage=True, pose_dependent=True)
    body = box(L.CARRIAGE_X, L.CARRIAGE_Y, (zc - L.CARRIAGE_H / 2, zc + L.CARRIAGE_H / 2))
    lx, ly = L.LEADSCREW_XY
    body = body - cyl_z(10.5, (zc - 30, zc + 30), lx, ly)
    for y in (-8.0, 8.0):
        body = body - cyl_x(5.0, (L.CARRIAGE_X[1] - 10, L.CARRIAGE_X[1] + 1), y, zc - 12)
        body = body - cyl_x(5.0, (L.CARRIAGE_X[1] - 10, L.CARRIAGE_X[1] + 1), y, zc + 12)
    for sy in (-1, 1):
        body = body - cyl_y(L.ROD_D, sorted((sy * (L.SPRING_INNER_Y - 12), sy * (L.SPRING_INNER_Y + 1))), lx, zc)
    c.add("M21", "Spring carriage", body, "alu", "S", material_label=ALU_6082, tol=0.05, **kw)
    bl = 45.4
    blk = box(L.BLOCK_X, (-13.5, 13.5), (zc - bl / 2, zc + bl / 2)) - box(
        (L.BLOCK_X[1] - 5.0, L.BLOCK_X[1] + 1), (-6.5, 6.5), (zc - bl / 2 - 1, zc + bl / 2 + 1))
    c.add("B11", "Linear block MGN12H", blk, "bearing", "S", bought=True, tol=0.05, **kw)
    c.add("M22", "Block spacer 8 mm", box(L.BLOCK_SPACER_X, (-13.5, 13.5), (zc - bl / 2 + 2, zc + bl / 2 - 2)),
          "alu", "S", material_label=ALU_6082, tol=0.05, **kw)
    zb = zc - L.CARRIAGE_H / 2
    nut = cyl_z(22.0, (zb - 3.5, zb), lx, ly) + cyl_z(10.2, (zb, zb + 11.5), lx, ly)
    nut = nut - cyl_z(L.LEADSCREW_D, (zb - 5, zb + 13), lx, ly)
    for a in range(4):
        ang = math.radians(45 + 90 * a)
        nut = nut - cyl_z(3.5, (zb - 4, zb + 1), lx + 8 * math.cos(ang), ly + 8 * math.sin(ang))
    c.add("B12", "Lead-screw nut T8 (brass)", nut, "bronze", "S", bought=True,
          material_label="Brass (lead-screw nut)", tol=0.05, **kw)

    fx0, fx1 = L.ROLLER_X[0] - L.FORK_PLATE_T, L.ROLLER_X[1] + L.FORK_PLATE_T   # -113, -95
    for side, tag in ((1, "+Y"), (-1, "-Y")):
        s = roller_offset(theta, r, side)

        def Y(a, b):
            return tuple(sorted((side * a, side * b)))
        rod = cyl_y(L.ROD_D, Y(L.SPRING_INNER_Y - 10, L.ROD_END_Y), lx, zc)
        c.add("M23", "Spring rod 10", rod, "stainless", "S", tag=tag, tol=0.05, **kw)
        bridge_in = s - L.FORK_BACK
        so, sl = L.SLEEVE
        fork = box((lx - 13, lx + 13), Y(bridge_in, bridge_in + 5), (zc - 13, zc + 13))
        for xr in ((fx0, L.ROLLER_X[0]), (L.ROLLER_X[1], fx1)):
            cheek = box(xr, Y(bridge_in + 5, s), (zc - 7, zc + 7)) + cyl_x(14.0, xr, side * s, zc)
            cheek = cheek - cyl_x(6.0, (xr[0] - 1, xr[1] + 1), side * s, zc)
            fork = fork + cheek
        fork = fork + tube_y(so, L.ROD_D + 0.4, Y(bridge_in - sl, bridge_in + 0.01), lx, zc)
        fork = fork - cyl_y(L.ROD_D + 0.4, Y(bridge_in - 1, bridge_in + 6), lx, zc)
        c.add("M24", "Roller fork with sleeve", fork, "alu", "S", tag=tag, material_label=ALU_6082,
              tol=0.05, **kw)
        sp = spring_y(L.SPRING_OD - L.SPRING_WIRE_D, L.SPRING_WIRE_D, side * L.SPRING_INNER_Y,
                      side * bridge_in, L.SPRING_COILS, x=lx, z=zc)
        c.add("B17", "Compression spring OD 25, ~31 N/mm", sp, "spring", "S", tag=tag, bought=True,
              tol=0.1, **kw)
        roller = cyl_x(L.ROLLER_D, L.ROLLER_X, side * s, zc) + cyl_x(6.0, (fx0 - 1.5, fx1 + 1.5), side * s, zc) \
            - tube_x(L.ROLLER_D + 1, L.ROLLER_D - 2, (L.ROLLER_X[0] - 0.1, L.ROLLER_X[0] + 0.6), side * s, zc)
        roller = roller + hex_prism_x(10.0, (fx1 + 1.5, fx1 + 5.5), side * s, zc) - cyl_x(6.0, (fx1 + 1.4, fx1 + 6), side * s, zc)
        c.add("B18", "Cam-follower roller 20x10", roller, "bearing", "S", tag=tag, bought=True,
              tol=0.05, **kw)
    return c.items


def belt_item(theta: float = 0.0, g=None) -> tuple[Item, dict]:
    shp, info = beltmod.solid(theta, g)
    it = Item(id="B19", name="GT2 belt 9 mm", shape=shp, material_key="belt", frame="A", bought=True,
              group="drive", pose_dependent=True, tol=0.05,
              note=f"pitch length {info['pitch_length']:.1f} mm between clamps")
    return it, info


@lru_cache(maxsize=2)
def _static_cached(geom_key: str) -> tuple[Item, ...]:
    c = _Collector()
    g = beltmod.load_geometry()
    _prism(c)
    _neck(c)
    _hub(c)
    _drive(c, g)
    _hinge(c)
    _head(c)
    _electrical(c)
    return tuple(c.items)


def static_items() -> list[Item]:
    """Every non-printed part that does not depend on the pose (frame-A coordinates at rest)."""
    g = beltmod.load_geometry()
    key = f"{g.source}|{g.idlers}|{g.pulley_c}|{g.idler_contact_r}"
    return [it.copy() for it in _static_cached(key)]


def items(theta: float = 0.0, carriage_r: float = L.CARRIAGE_R_DEFAULT) -> list[Item]:
    """All non-printed items for a pose (unposed: positions at theta = beta = 0, except the
    pose-dependent carriage and belt, which are solved for theta)."""
    out = static_items() + carriage_items(carriage_r, theta)
    b, _ = belt_item(theta)
    out.append(b)
    return out
