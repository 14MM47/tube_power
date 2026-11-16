#!/usr/bin/env python3
"""Lantern design calculator and optimiser, calm to 40 m/s.

Reproduces every number in designs/lantern-250/ from the parameters below.
For any design it works out, at every wind speed, what the machine does
(idle, tracking, power-capped, braked), what it produces, and how close each
part is to its limit. It can also search a grid of dimensions for the
highest-output design that survives a chosen storm wind.

    python3 tools/lantern_calc.py                       # report for Lantern 250-B
    python3 tools/lantern_calc.py report --config C     # the all-weather version
    python3 tools/lantern_calc.py envelope --config C   # every wind speed, 1-40 m/s
    python3 tools/lantern_calc.py envelope --step 0.5 --to 40 --csv curve.csv
    python3 tools/lantern_calc.py sweep                 # best design surviving 25 m/s
    python3 tools/lantern_calc.py sweep --config C      # best design surviving 40 m/s
    python3 tools/lantern_calc.py sweep --objective annual --site 4.5 --csv grid.csv

All results are engineering estimates from simple models (see
designs/lantern-250/physics.md). None has been measured, and an optimiser
will exploit any weakness in the model, so treat the "best" design as a
starting point for testing. Standard library only.
"""

from __future__ import annotations

import argparse
import csv
import itertools
import math
from dataclasses import dataclass, fields, replace

RHO = 1.225  # air density, kg/m^3
NU = 1.5e-5  # kinematic viscosity of air, m^2/s
G0 = 9.81  # gravity, m/s^2

# Shell constructions. Areal masses: extruded polystyrene ~37 kg/m^3, each
# glass-tissue skin with epoxy ~0.05 kg/m^2. "single" has an outer skin only,
# "sandwich" has glass on both faces, "storm" also thickens the outer skin
# near the tube base. End discs are built the same way as the shell.
SHELLS = {
    "xps2-single": dict(shell_areal=0.124, shell_core_t=0.002, shell_sandwich=0, skin_t=0.05e-3,
                        disc_areal=0.124, disc_core_t=0.002, disc_sandwich=0),
    "xps3-single": dict(shell_areal=0.161, shell_core_t=0.003, shell_sandwich=0, skin_t=0.05e-3,
                        disc_areal=0.161, disc_core_t=0.003, disc_sandwich=0),
    "xps3-sandwich": dict(shell_areal=0.211, shell_core_t=0.003, shell_sandwich=1, skin_t=0.05e-3,
                          disc_areal=0.211, disc_core_t=0.003, disc_sandwich=1),
    "xps5-sandwich": dict(shell_areal=0.285, shell_core_t=0.005, shell_sandwich=1, skin_t=0.05e-3,
                          disc_areal=0.285, disc_core_t=0.005, disc_sandwich=1),
    "xps5-storm": dict(shell_areal=0.315, shell_core_t=0.005, shell_sandwich=1, skin_t=0.15e-3,
                       disc_areal=0.285, disc_core_t=0.005, disc_sandwich=1),
}

# Standard roll-wrapped carbon tubes for the neck (outside, inside diameter, m)
NECK_TUBES = [(0.025, 0.023), (0.030, 0.028), (0.035, 0.032), (0.040, 0.037), (0.050, 0.047)]


@dataclass(frozen=True)
class Design:
    """Defaults are Lantern 250-B, the recommended configuration."""

    # Geometry
    D: float = 0.25  # tube diameter, m
    L: float = 1.00  # tube length (the 1 m height limit), m
    neck: float = 0.80  # hinge axis to bottom of tube, m

    # Tube shell (see SHELLS)
    shell_areal: float = 0.211  # kg/m^2
    shell_core_t: float = 0.003  # foam core thickness, m
    shell_sandwich: int = 1  # 1 = glass skin on both faces
    skin_t: float = 0.05e-3  # effective outer glass-skin thickness at the tube base, m
    inner_skin_t: float = 0.05e-3  # effective inner skin thickness (sandwich only), m
    rings_mass: float = 0.012  # internal rings, kg
    seams_mass: float = 0.008  # tape and glue, kg

    # End discs: ratio 1.0 means no discs
    disc_ratio: float = 2.0  # disc diameter / tube diameter
    disc_areal: float = 0.211  # kg/m^2
    disc_core_t: float = 0.003  # m
    disc_sandwich: int = 1
    end_loss_D: float = 0.5  # span lost per bare end, in diameters (assumed)
    disc_full_ratio: float = 2.0  # disc ratio that removes the end loss (assumed)

    # Neck and hub
    spider_mass: float = 0.015  # bottom-ring-to-neck spider, kg
    neck_od: float = 0.035  # carbon neck tube outside diameter, m
    neck_id: float = 0.032  # carbon neck tube inside diameter, m
    carbon_density: float = 1550.0  # kg/m^3
    carbon_E: float = 100e9  # Pa
    hub_mass: float = 0.15  # hub, axle, spring carriage, belt arc, kg
    hub_radius: float = 0.07  # effective radius of hub mass, m

    # Flow
    St: float = 0.2  # Strouhal number
    Ca: float = 1.0  # added-mass coefficient
    Cd_viv: float = 2.0  # mean drag coefficient while swinging
    Cd_storm: float = 1.2  # drag coefficient when parked (conservative: no drag-crisis credit)
    CL_start: float = 0.3  # lift coefficient on a still tube (start-up check)
    gust_CL: float = 1.1  # end-disc lift coefficient for a ~10 deg gust inflow

    # Drive: GT2 belt from an arc on the hub to a pulley on the generator
    arc_radius: float = 0.100  # m
    pulley_teeth: int = 12
    belt_pitch: float = 0.002  # m
    belt_eff: float = 0.97

    # Generator: 5208-size brushless gimbal motor (check your datasheet)
    gen_rotor_J: float = 6e-5  # kg m^2 (assumed)
    Ke: float = 0.38  # V s/rad = N m/A
    R_coil: float = 12.0  # ohm
    gen_drag: float = 0.004  # bearing + iron-loss drag at the motor shaft, N m (assumed)
    gen_cogging: float = 0.005  # cogging torque at the motor shaft, N m (measure it)
    conv_eff: float = 0.85  # rectifier + MPPT converter
    R_brake: float = 0.0  # external braking resistor, ohm (0 = phases shorted)
    kick_start: int = 1  # 1 = controller motors the generator briefly to start the swing

    # Losses
    zeta_struct: float = 0.003  # foam/epoxy hysteresis, springs, air (assumed)
    bush_span: float = 0.15  # distance between hinge bushings, m
    axle_d: float = 0.012  # hinge axle diameter, m
    bush_mu: float = 0.15  # polymer bushing friction coefficient

    # Tuning and control
    Ustar: float = 5.5  # target U/(f_n D) at the tuned wind speed
    U_tune_min: float = 2.0  # m/s
    U_tune_max: float = 7.0  # m/s
    r_spring_max: float = 0.140  # spring carriage furthest from hinge, m
    lock_band: float = 0.2  # lock-on reaches this fraction beyond the tuned speed (assumed)
    P_rated: float = 0.0  # electrical power cap, W (0 = output at U_tune_max)
    U_brake: float = 8.0  # brake at and above this wind, m/s (0 = U_tune_max x (1 + lock_band))
    keep_generating: int = 0  # 0 = cap at rated power then brake; 1 = keep generating within every limit
    U_tune_ext_max: float = 40.0  # highest wind the keep-generating control may retune to (springs rebuilt)
    Re_harvest_max: float = 2.0e5  # no harvesting credit above this Re (drag crisis; shedding unreliable)
    mode_margin: float = 1.5  # neck-tube bending frequency must exceed this x swing frequency

    # Limits
    U_storm: float = 25.0  # survival requirement (parked and braked), m/s
    skin_allow: float = 40e6  # glass-skin allowable stress, Pa
    foam_allow: float = 0.25e6  # foam allowable bending stress, Pa
    oval_k: float = 0.5  # shell ovalling moment = oval_k x q x R^2 per unit length (assumed)
    neck_allow: float = 400e6  # carbon neck allowable peak stress, Pa
    neck_fatigue_allow: float = 200e6  # carbon neck allowable cyclic stress amplitude, Pa
    M_hinge_max: float = 150.0  # moment the hub, bushings and post head are built for, N m
    Re_max: float = 1.2e5  # highest Re at U_tune_max (tested range of the evidence)
    R_margin: float = 1.2  # circuit resistance must exceed this x coil resistance
    max_total_height: float = 2.0  # tube + neck limit, m
    V_max: float = 150.0  # electronics voltage rating, V
    gen_heat_max: float = 5.0  # generator winding dissipation limit, W (assumed)

    # Site, post and planning
    hub_height: float = 3.0  # hinge height above ground, m
    head_area: float = 0.03  # frontal area of hub, generator and yaw head, m^2
    vane_area: float = 0.08  # tail vane area, m^2
    derate: float = 0.5  # low case = derate x model (turbulence, detuning)
    lock_factor: float = 0.5  # share of in-band time actually locked on
    duty: float = 0.30  # share of the year spent swinging


# Named configurations. B is the default.
CONFIGS = {
    "A": dict(neck=0.40, disc_ratio=1.6, pulley_teeth=16, neck_od=0.025, neck_id=0.023,
              bush_span=0.10, axle_d=0.010),
    "B": {},
    "C": dict(**SHELLS["xps5-storm"], disc_ratio=2.0, neck=0.60, neck_od=0.035, neck_id=0.032,
              rings_mass=0.03, hub_mass=0.30, bush_span=0.20, axle_d=0.016,
              U_storm=40.0, M_hinge_max=350.0),
}


# ---------------------------------------------------------------- geometry


def r1(d: Design) -> float:
    return d.neck


def r2(d: Design) -> float:
    return d.neck + d.L


def cube_span(d: Design) -> float:
    return (r2(d) ** 3 - r1(d) ** 3) / 3.0


def gear_ratio(d: Design) -> float:
    return d.arc_radius / (d.pulley_teeth * d.belt_pitch / (2.0 * math.pi))


def effective_length(d: Design) -> float:
    if d.disc_ratio <= 1.0:
        e = d.end_loss_D
    else:
        e = d.end_loss_D * max(0.0, 1.0 - (d.disc_ratio - 1.0) / (d.disc_full_ratio - 1.0))
    return max(0.0, d.L - 2.0 * e * d.D)


def mode_gamma(d: Design) -> float:
    """Skop-Griffin mode-shape factor for a linear (hinged) mode, top = 1."""
    a, b = r1(d), r2(d)
    i2 = (b**3 - a**3) / (3 * b**2)
    i4 = (b**5 - a**5) / (5 * b**4)
    return math.sqrt(i2 / i4)


def masses(d: Design) -> dict[str, float]:
    shell = d.shell_areal * math.pi * d.D * d.L + d.rings_mass + d.seams_mass
    disc_dia = d.disc_ratio * d.D
    disc = d.disc_areal * math.pi * disc_dia**2 / 4.0 if d.disc_ratio > 1.0 else 0.0
    neck_lin = d.carbon_density * math.pi / 4.0 * (d.neck_od**2 - d.neck_id**2)
    m = {
        "shell": shell,
        "disc_each": disc,
        "disc_dia": disc_dia,
        "spider": d.spider_mass,
        "neck": neck_lin * d.neck,
        "neck_lin": neck_lin,
        "hub": d.hub_mass,
    }
    m["above"] = shell + 2 * disc + d.spider_mass + m["neck"]
    m["swinging"] = m["above"] + d.hub_mass
    return m


def inertias(d: Design, include_generator: bool = True) -> dict[str, float]:
    m = masses(d)
    a, b = r1(d), r2(d)
    rd = m["disc_dia"] / 2.0
    parts = {
        "shell": m["shell"] * cube_span(d) / d.L,
        "discs": m["disc_each"] * (a**2 + b**2) + 2 * m["disc_each"] * rd**2 / 4.0,
        "spider": m["spider"] * a**2,
        "neck": m["neck_lin"] * d.neck**3 / 3.0,
        "hub": m["hub"] * d.hub_radius**2,
        "generator": d.gen_rotor_J * gear_ratio(d) ** 2 if include_generator else 0.0,
    }
    structural = sum(parts.values())
    displaced = RHO * math.pi * d.D**2 / 4.0 * cube_span(d)
    parts.update(
        above=parts["shell"] + parts["discs"] + parts["spider"] + parts["neck"],
        structural=structural,
        displaced=displaced,
        added=d.Ca * displaced,
        total=structural + d.Ca * displaced,
        mass_ratio=structural / displaced,
    )
    return parts


def gravity_stiffness(d: Design) -> float:
    m = masses(d)
    a, b = r1(d), r2(d)
    moment = (
        m["shell"] * (a + d.L / 2.0)
        + m["disc_each"] * (a + b)
        + m["spider"] * a
        + m["neck"] * d.neck / 2.0
    )
    return moment * G0


def neck_I(d: Design) -> float:
    return math.pi / 64.0 * (d.neck_od**4 - d.neck_id**4)


def neck_mode_freq(d: Design) -> float:
    """First bending frequency of neck + tube with the hinge held rigid, Hz.

    Two degrees of freedom at the neck tip (sideways movement and rotation);
    the tube is a rigid body (with its added air) whose centre is L/2 above
    the neck tip. Holding the hinge rigid gives a lower bound on the real
    second mode, so the check is conservative.
    """
    m = masses(d)
    a = max(d.neck, 1e-3)
    e = d.L / 2.0
    EI = d.carbon_E * neck_I(d)
    k11, k12, k22 = 12 * EI / a**3, -6 * EI / a**2, 4 * EI / a
    m_air = d.Ca * RHO * math.pi * d.D**2 / 4.0 * d.L
    mt = m["shell"] + 2 * m["disc_each"] + m_air
    J = ((m["shell"] + m_air) * d.L**2 / 12.0 + 2 * m["disc_each"] * e**2
         + 2 * m["disc_each"] * (m["disc_dia"] / 2.0) ** 2 / 4.0)
    m11 = mt + m["spider"] + 0.24 * m["neck"]
    m12, m22 = mt * e, mt * e**2 + J
    A = m11 * m22 - m12**2
    B = -(k11 * m22 + k22 * m11 - 2 * k12 * m12)
    C = k11 * k22 - k12**2
    w2 = (-B - math.sqrt(B * B - 4 * A * C)) / (2 * A)
    return math.sqrt(w2) / (2.0 * math.pi)


def structural_tuning_limit(d: Design) -> float:
    """Highest wind at which the swing stays below neck-mode frequency / margin, m/s."""
    return neck_mode_freq(d) * d.D / (d.St * d.mode_margin)


def wall_capacity(d: Design, core_t: float, sandwich: int) -> float:
    """Bending capacity of the shell or disc wall per unit length, N m/m."""
    if sandwich:
        return d.skin_allow * d.inner_skin_t * core_t
    return d.foam_allow * core_t**2 / 2.0


# ---------------------------------------------------------------- tuning


def f_natural(d: Design, U: float) -> float:
    """Still-air natural frequency to tune for (added mass included), Hz."""
    U = min(max(U, d.U_tune_min), d.U_tune_max)
    return U / (d.Ustar * d.D)


def k_required(d: Design, U: float) -> float:
    w = 2.0 * math.pi * f_natural(d, U)
    return inertias(d)["total"] * w**2 + gravity_stiffness(d)


def spring_rate(d: Design) -> float:
    """Rate of each of the two opposing springs, N/m."""
    return k_required(d, d.U_tune_max) / (2.0 * d.r_spring_max**2)


def carriage_radius(d: Design, U: float) -> float:
    return math.sqrt(k_required(d, U) / (2.0 * spring_rate(d)))


# ---------------------------------------------------------------- performance


def wind_power(d: Design, U: float) -> float:
    return 0.5 * RHO * U**3 * d.D * d.L


def solve(d: Design, U: float, ze_fixed: float | None = None) -> dict[str, float]:
    """Locked-on swing at wind speed U.

    With ze_fixed=None the generator damping is the value that maximises
    extracted power; otherwise it is ze_fixed. Amplitude from the
    Skop-Griffin relation with the hinged mode shape; friction converted to an
    equivalent damping ratio. See physics.md.
    """
    I = inertias(d)
    Is, ms = I["structural"], I["mass_ratio"]
    w = 2.0 * math.pi * d.St * U / d.D
    a = 0.43 * 2.0 * math.pi**3 * d.St**2 * ms
    gam = mode_gamma(d)
    G = gear_ratio(d)
    top = r2(d)
    weight = masses(d)["swinging"] * G0
    drag = 0.5 * RHO * U**2 * d.Cd_viv * d.D * d.L
    m_drag = drag * (d.neck + d.L / 2.0)
    t_bush = d.bush_mu * (2.0 * m_drag / d.bush_span + weight) * d.axle_d / 2.0
    t_gen = d.gen_drag * G
    t_fric = t_bush + t_gen

    theta = math.radians(8.0)
    zp = ze = 0.0
    for _ in range(80):
        c_fric = 4.0 * t_fric / (math.pi * max(theta, 1e-6) * w)
        zp = d.zeta_struct + c_fric / (2.0 * Is * w)
        ze = ze_fixed if ze_fixed is not None else (1.0 + a * zp) / (5.7 * a)
        a_top = d.D * 1.29 * gam / (1.0 + a * (zp + ze)) ** 3.35
        new = math.atan(a_top / top)
        if abs(new - theta) < 1e-8:
            theta = new
            break
        theta = 0.5 * (theta + new)

    span_factor = effective_length(d) / d.L
    p_mech = ze * Is * w**3 * theta**2 * span_factor
    c_e = 2.0 * ze * Is * w
    r_total = G**2 * d.Ke**2 / c_e if c_e > 0 else math.inf
    copper = 1.0 - d.R_coil / r_total
    p_elec = p_mech * d.belt_eff * max(copper, 0.0) * d.conv_eff
    emf = d.Ke * G * theta * w
    i_pk = emf / r_total if r_total > 0 else 0.0
    pw = wind_power(d, U)
    return {
        "U": U,
        "w": w,
        "theta": theta,
        "f_osc": w / (2.0 * math.pi),
        "f_n": f_natural(d, U),
        "Re": U * d.D / NU,
        "p_wind": pw,
        "p_mech": p_mech,
        "p_elec": p_elec,
        "eta_mech": p_mech / pw,
        "eta_elec": p_elec / pw,
        "theta_deg": math.degrees(theta),
        "a_top": top * math.tan(theta),
        "a_mid": (d.neck + d.L / 2.0) * math.tan(theta),
        "a_bot": d.neck * math.tan(theta),
        "zeta_e": ze,
        "zeta_par": zp,
        "t_bush": t_bush,
        "t_gen": t_gen,
        "torque_peak": c_e * theta * w,
        "R_total": r_total,
        "R_load": r_total - d.R_coil,
        "copper": copper,
        "emf_peak": emf,
        "gen_heat": i_pk**2 / 2.0 * d.R_coil,
        "gen_rpm_peak": G * theta * w * 60.0 / (2.0 * math.pi),
        "gen_swing_deg": math.degrees(theta) * G,
        "top_accel_g": theta * w**2 * top / G0,
    }


# Backwards-compatible name
evaluate = solve


def lock_top(d: Design) -> float:
    return d.U_tune_max * (1.0 + d.lock_band)


def brake_speed(d: Design) -> float:
    return d.U_brake if d.U_brake > 0 else lock_top(d)


def rated_power(d: Design) -> float:
    return d.P_rated if d.P_rated > 0 else solve(d, d.U_tune_max)["p_elec"]


def start_check(d: Design, U: float) -> tuple[bool, float, float]:
    """Can the still tube start swinging? Returns (ok, lift moment, resisting torque)."""
    lever = d.neck + d.L / 2.0
    m_lift = 0.5 * RHO * U**2 * d.CL_start * d.D * effective_length(d) * lever
    G = gear_ratio(d)
    weight = masses(d)["swinging"] * G0
    drag = 0.5 * RHO * U**2 * d.Cd_storm * d.D * d.L
    t_bush = d.bush_mu * (2.0 * drag * lever / d.bush_span + weight) * d.axle_d / 2.0
    t_static = t_bush + d.gen_drag * G + (0.0 if d.kick_start else d.gen_cogging * G)
    return m_lift > t_static, m_lift, t_static


def extended_tuning_max(d: Design) -> float:
    """Highest wind the keep-generating control can tune to: springs permitting, neck mode limiting."""
    return max(d.U_tune_min, min(d.U_tune_ext_max, structural_tuning_limit(d)))


def harvest_reach(d: Design) -> float:
    """Highest wind at which the keep-generating control can still lock on and harvest."""
    return min(extended_tuning_max(d) * (1.0 + d.lock_band), d.Re_harvest_max * NU / d.D)


def operate_limits(d: Design, U: float) -> dict:
    """Keep-generating control: the most electrical power at wind U with every part within limits.

    Retunes up to extended_tuning_max(), then rides the lock-on tail. At each
    wind it searches generator damping (below and above the optimum) for the
    highest output whose swinging loads all stay at or under 100%.
    """
    out: dict = {"U": U, "op": None, "limit": ""}
    ok, m_lift, t_static = start_check(d, U)
    if U < d.U_tune_min * (1.0 - d.lock_band) or not ok:
        out["mode"] = "idle"
        return out
    u_tune = extended_tuning_max(d)
    if U > harvest_reach(d):
        out["mode"] = "braked"
        if U * d.D / NU > d.Re_harvest_max:
            out["limit"] = "drag crisis"
        elif u_tune < d.U_tune_ext_max and u_tune == structural_tuning_limit(d):
            out["limit"] = "neck mode"
        else:
            out["limit"] = "tuning range"
        return out
    opt = solve(d, U)
    G = gear_ratio(d)
    Is = inertias(d)["structural"]
    ze0 = opt["zeta_e"]
    ze_max = (G**2 * d.Ke**2 / d.R_coil) / (2.0 * Is * opt["w"]) * 0.999
    cands = [ze0 * f for f in (0.2, 0.3, 0.45, 0.6, 0.75, 0.9)]
    n = 22
    cands += [ze0 * (ze_max / ze0) ** (i / (n - 1)) for i in range(n)] if ze_max > ze0 else [ze0]
    mode = "tracking" if U <= u_tune else "lock-on tail"
    best = None
    worst_at_opt = ""
    for ze in cands:
        op = opt if ze == ze0 else solve(d, U, ze_fixed=ze)
        lo = loads(d, U, {"mode": mode, "op": op})
        if ze == ze0:
            worst_at_opt = lo["worst"]
        if lo["worst_util"] <= 1.0 and (best is None or op["p_elec"] > best[0]["p_elec"]):
            best = (op, lo)
    if best is None:
        out["mode"] = "braked"
        out["limit"] = worst_at_opt
        return out
    op, lo = best
    out["op"] = op
    out["mode"] = mode
    if op["p_elec"] < 0.99 * opt["p_elec"]:
        out["limit"] = lo["worst"]
    return out


def operate(d: Design, U: float) -> dict:
    """Operating mode and swing at wind speed U, following the control rules."""
    out: dict = {"U": U, "op": None}
    if U <= 0:
        out["mode"] = "calm"
        return out
    if d.keep_generating:
        return operate_limits(d, U)
    G = gear_ratio(d)
    Is = inertias(d)["structural"]
    if U >= brake_speed(d):
        out["mode"] = "braked"
        if U <= lock_top(d):
            w = 2.0 * math.pi * d.St * U / d.D
            c_b = G**2 * d.Ke**2 / (d.R_coil + d.R_brake)
            op = solve(d, U, ze_fixed=c_b / (2.0 * Is * w))
            op["brake_heat"] = op["p_mech"]
            op["p_elec"] = 0.0
            out["op"] = op
        return out
    ok, m_lift, t_static = start_check(d, U)
    out["lift"], out["resist"] = m_lift, t_static
    if U < d.U_tune_min * (1.0 - d.lock_band) or not ok:
        out["mode"] = "idle"
        return out
    if U > lock_top(d):
        out["mode"] = "out of lock-on"
        return out
    op = solve(d, U)
    if U <= d.U_tune_max:
        out["mode"] = "tracking"
        out["op"] = op
        return out
    cap = rated_power(d)
    out["mode"] = "power-capped"
    if op["p_elec"] > cap:
        lo = op["zeta_e"]
        w = op["w"]
        hi = (G**2 * d.Ke**2 / d.R_coil) / (2.0 * Is * w) * 0.999
        if solve(d, U, ze_fixed=hi)["p_elec"] > cap:
            out["mode"] = "braked"
            return out
        for _ in range(40):
            mid = 0.5 * (lo + hi)
            if solve(d, U, ze_fixed=mid)["p_elec"] > cap:
                lo = mid
            else:
                hi = mid
        op = solve(d, U, ze_fixed=hi)
    out["op"] = op
    return out


SWINGING = ("tracking", "power-capped", "lock-on tail")


def loads(d: Design, U: float, state: dict | None = None) -> dict:
    """Structural and electrical loads at wind speed U for the given state."""
    st = state if state is not None else operate(d, U)
    op = st.get("op")
    swinging = op is not None
    m = masses(d)
    I = inertias(d)
    q = 0.5 * RHO * U**2
    Cd = d.Cd_viv if swinging and st["mode"] in SWINGING else d.Cd_storm
    F = q * Cd * d.D * d.L
    m_drag_hinge = F * (d.neck + d.L / 2.0)
    m_drag_base = F * d.L / 2.0
    th = op["theta"] if swinging else 0.0
    w = op["w"] if swinging else 0.0
    a, b = r1(d), r2(d)
    m_cyc_neck = I["above"] * th * w**2
    mu_s = m["shell"] / d.L
    m_cyc_base = mu_s * th * w**2 * ((b**3 - a**3) / 3.0 - a * (b**2 - a**2) / 2.0) + m["disc_each"] * th * w**2 * b * (b - a)
    c = d.neck_od / 2.0
    In = neck_I(d)
    R = d.D / 2.0
    neck_peak = math.hypot(m_drag_hinge, m_cyc_neck) * c / In
    neck_cyc = m_cyc_neck * c / In
    skin = math.hypot(m_drag_base, m_cyc_base) / (math.pi * R**2 * d.skin_t)
    wall_dem = d.oval_k * q * R**2
    wall_cap = wall_capacity(d, d.shell_core_t, d.shell_sandwich)
    if d.disc_ratio > 1.0:
        wd = (m["disc_dia"] - d.D) / 2.0
        disc_dem = d.gust_CL * q * wd**2 / 2.0
        disc_util = disc_dem / wall_capacity(d, d.disc_core_t, d.disc_sandwich)
    else:
        disc_util = 0.0
    r_cg = (m["shell"] * (a + d.L / 2) + m["disc_each"] * (a + b) + m["spider"] * a + m["neck"] * d.neck / 2) / max(m["above"], 1e-9)
    f_inertial = m["above"] * th * w**2 * r_cg
    bushing = m_drag_hinge / d.bush_span + 0.5 * (m["swinging"] * G0 + f_inertial)
    head_drag = q * (1.2 * d.head_area + 0.2 * d.vane_area)
    post_moment = F * (d.hub_height + d.neck + d.L / 2.0) + head_drag * d.hub_height
    emf = op["emf_peak"] if swinging and st["mode"] in SWINGING else 0.0
    heat = (op.get("brake_heat", op["gen_heat"]) if swinging else 0.0)
    utils = {
        "neck": neck_peak / d.neck_allow,
        "neck fatigue": neck_cyc / d.neck_fatigue_allow,
        "skin": skin / d.skin_allow,
        "wall": wall_dem / wall_cap,
        "discs": disc_util,
        "hub": m_drag_hinge / d.M_hinge_max,
        "voltage": emf / d.V_max,
        "generator heat": heat / d.gen_heat_max,
        "neck mode": (d.mode_margin * op["f_osc"] / neck_mode_freq(d)) if swinging and st["mode"] in SWINGING else 0.0,
    }
    worst = max(utils, key=utils.get)
    return {
        "q": q, "drag": F, "m_drag_hinge": m_drag_hinge, "m_drag_base": m_drag_base,
        "m_cyc_neck": m_cyc_neck, "m_cyc_base": m_cyc_base,
        "neck_peak_MPa": neck_peak / 1e6, "neck_cyc_MPa": neck_cyc / 1e6, "skin_MPa": skin / 1e6,
        "wall_demand": wall_dem, "wall_capacity": wall_cap, "bushing_N": bushing,
        "post_moment": post_moment, "head_drag": head_drag, "emf": emf, "heat": heat,
        "top_accel_g": (th * w**2 * b / G0) if swinging else 0.0,
        "utils": utils, "worst": worst, "worst_util": utils[worst],
    }


def survival(d: Design) -> tuple[float, str, dict]:
    """Highest parked, braked wind each part survives. Returns (wind, limiting part, per-part winds)."""
    ref = 10.0
    lo = loads(d, ref, {"mode": "braked", "op": None})
    winds = {}
    for k in ("neck", "skin", "wall", "discs", "hub"):
        u = lo["utils"][k]
        winds[k] = ref / math.sqrt(u) if u > 0 else 99.0
    k = min(winds, key=winds.get)
    return min(winds[k], 99.0), k, winds


def operating_peak(d: Design) -> dict:
    """Worst utilisations while swinging, from tracking up to the brake speed."""
    speeds = [4.5, d.U_tune_max]
    ub = brake_speed(d)
    if ub > d.U_tune_max:
        speeds += [d.U_tune_max + (ub - d.U_tune_max) * f for f in (0.5, 0.99)]
    worst: dict[str, float] = {}
    for U in speeds:
        st = operate(d, U)
        if st["mode"] not in SWINGING:
            continue
        for k, v in loads(d, U, st)["utils"].items():
            if k in ("neck fatigue", "neck", "skin", "voltage", "generator heat", "neck mode"):
                worst[k] = max(worst.get(k, 0.0), v)
    return worst


def cut_in(d: Design) -> float:
    U = 0.5
    while U < brake_speed(d):
        st = operate(d, U)
        if st["mode"] in SWINGING and st["op"]["p_elec"] > 0.01:
            return U
        U += 0.1
    return math.nan


def annual_energy(d: Design, mean_wind: float, step: float = 0.25) -> float:
    """Central-case kWh/yr for a Rayleigh wind distribution at hub height."""
    total = 0.0
    U = step / 2.0
    top = harvest_reach(d) + step if d.keep_generating else brake_speed(d)
    while U < top:
        pdf = math.pi * U / (2 * mean_wind**2) * math.exp(-math.pi * U**2 / (4 * mean_wind**2))
        st = operate(d, U)
        if st["mode"] in SWINGING:
            total += st["op"]["p_elec"] * pdf * step
        U += step
    return total * d.lock_factor * 8760.0 / 1000.0


def constraint_failures(d: Design) -> list[str]:
    fails = []
    if d.U_tune_max * d.D / NU > d.Re_max:
        fails.append("Reynolds")
    if survival(d)[0] < d.U_storm:
        fails.append("survival")
    if any(v > 1.0 for v in operating_peak(d).values()):
        fails.append("operating loads")
    if d.neck + d.L > d.max_total_height:
        fails.append("height")
    if solve(d, 4.5)["R_total"] < d.R_margin * d.R_coil:
        fails.append("generator too weak")
    return fails


def size_neck(d: Design) -> Design:
    """Lightest standard neck tube that survives U_storm and the operating fatigue."""
    for od, idd in NECK_TUBES:
        t = replace(d, neck_od=od, neck_id=idd)
        surv, part, winds = survival(t)
        peak = operating_peak(t)
        if (winds["neck"] >= d.U_storm and peak.get("neck fatigue", 0.0) <= 1.0
                and peak.get("neck mode", 0.0) <= 1.0):
            return t
    od, idd = NECK_TUBES[-1]
    return replace(d, neck_od=od, neck_id=idd)


# ---------------------------------------------------------------- output


def f2(x: float, nd: int = 2) -> str:
    return f"{x:.{nd}f}"


def pct(u: float) -> str:
    return f"{100*u:.0f}%"


ENVELOPE_SPEEDS = [1, 2, 2.5, 3, 4, 4.5, 5, 6, 7, 7.5, 8, 9, 10, 12, 15, 20, 25, 30, 35, 40]


def envelope_rows(d: Design, speeds) -> list[dict]:
    rows = []
    for U in speeds:
        st = operate(d, U)
        lo = loads(d, U, st)
        op = st["op"]
        sw = st["mode"] in SWINGING
        rows.append({
            "U": U, "mode": st["mode"], "Re": U * d.D / NU,
            "f_n": f_natural(d, U) if sw else f_natural(d, d.U_tune_max),
            "carriage_mm": 1000 * (carriage_radius(d, U) if sw else d.r_spring_max),
            "swing_deg": op["theta_deg"] if op else 0.0,
            "p_elec": op["p_elec"] if op and sw else 0.0,
            "top_g": lo["top_accel_g"], "emf": lo["emf"], "heat": lo["heat"],
            "drag": lo["drag"], "bushing_N": lo["bushing_N"], "post_moment": lo["post_moment"],
            **{"u_" + k: v for k, v in lo["utils"].items()},
            "worst": lo["worst"], "worst_util": lo["worst_util"],
        })
    return rows


def regime(Re: float, d: Design) -> str:
    if Re <= d.Re_max:
        return "tested"
    if Re <= 2.0e5:
        return "beyond tested"
    return "drag crisis"


def envelope_table(d: Design, speeds) -> list[str]:
    o = ["| Wind (m/s) | Mode | Re | Flow | Tuned to (Hz) | Carriage (mm) | Swing (±°) | Elec (W) | Top accel (g) | "
         "EMF (V) | Neck | Neck fatigue | Skin | Wall | Discs | Hub | Worst |",
         "|" + "---|" * 17]
    for r in envelope_rows(d, speeds):
        o.append(
            f"| {r['U']:g} | {r['mode']} | {r['Re']:,.0f} | {regime(r['Re'], d)} | {f2(r['f_n'])} | {r['carriage_mm']:.0f} | "
            f"{f2(r['swing_deg'],1)} | {f2(r['p_elec'],2)} | {f2(r['top_g'],1)} | {f2(r['emf'],0)} | "
            f"{pct(r['u_neck'])} | {pct(r['u_neck fatigue'])} | {pct(r['u_skin'])} | {pct(r['u_wall'])} | "
            f"{pct(r['u_discs'])} | {pct(r['u_hub'])} | {r['worst']} {pct(r['worst_util'])}{' **FAIL**' if r['worst_util'] > 1 else ''} |"
        )
    return o


CURVE_SPEEDS = [1, 2, 3, 4, 4.5, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17.5, 20, 25, 30, 35, 40]


def curve_rows(d: Design, speeds) -> list[dict]:
    """Power at each wind: wind through the tube, model potential, within limits, and as designed."""
    rated = replace(d, keep_generating=0)
    lim = replace(d, keep_generating=1)
    rows = []
    for U in speeds:
        a = operate(rated, U)
        b = operate(lim, U)
        pa = a["op"]["p_elec"] if a["mode"] in SWINGING and a["op"] else 0.0
        pb = b["op"]["p_elec"] if b["mode"] in SWINGING and b["op"] else 0.0
        if b["mode"] in SWINGING:
            why = ("limited by " + b["limit"]) if b["limit"] else "unconstrained"
        else:
            why = b["mode"] + (f" ({b['limit']})" if b.get("limit") else "")
        rows.append({
            "U": U,
            "Re": U * d.D / NU,
            "wind_W": wind_power(d, U),
            "potential_W": solve(d, U)["p_elec"],
            "within_limits_W": pb,
            "within_limits_mode": b["mode"],
            "within_limits_note": why,
            "within_limits_swing_deg": b["op"]["theta_deg"] if b["op"] and b["mode"] in SWINGING else 0.0,
            "as_designed_W": pa,
            "as_designed_mode": a["mode"],
        })
    return rows


def curve_summary(d: Design) -> list[str]:
    lim = replace(d, keep_generating=1)
    rated = replace(d, keep_generating=0)
    rows = curve_rows(d, [round(0.5 + 0.25 * i, 2) for i in range(159)])
    pk = max(rows, key=lambda r: r["within_limits_W"])
    gen = [r["U"] for r in rows if r["within_limits_W"] > 0.01]
    return [
        f"- Neck-tube bending mode about {f2(neck_mode_freq(d),1)} Hz, so the swing must stay below "
        f"{f2(neck_mode_freq(d)/d.mode_margin,1)} Hz: retuning is possible up to {f2(extended_tuning_max(d),1)} m/s",
        f"- As designed: generates {f2(cut_in(rated),1)}-{f2(brake_speed(rated),1)} m/s, peak {f2(rated_power(rated),2)} W, braked above",
        f"- Kept generating within every limit: generates {f2(min(gen),1) if gen else 'n/a'}-{f2(max(gen),1) if gen else 'n/a'} m/s, "
        f"peak {f2(pk['within_limits_W'],2)} W at {pk['U']:g} m/s; nothing above {f2(harvest_reach(lim),1)} m/s",
        "- Yearly energy, central case (kWh): " + "; ".join(
            f"{V} m/s site: as designed {f2(annual_energy(rated, V),1)}, within limits {f2(annual_energy(lim, V),1)}"
            for V in (3.5, 4.5, 5.5, 6.5)),
    ]


def curve_table(d: Design, speeds) -> list[str]:
    o = ["| Wind (m/s) | Re | Flow | Wind through tube (W) | Model potential (W) | Within limits (W) | "
         "Within limits: what governs | As designed (W) | As designed: mode |",
         "|" + "---|" * 9]
    for r in curve_rows(d, speeds):
        o.append(
            f"| {r['U']:g} | {r['Re']:,.0f} | {regime(r['Re'], d)} | {r['wind_W']:,.1f} | {r['potential_W']:,.2f} | "
            f"{r['within_limits_W']:.2f} | {r['within_limits_note']} | {r['as_designed_W']:.2f} | {r['as_designed_mode']} |"
        )
    return o


def curve_report(d: Design, step: float, top: float, start: float) -> str:
    n = int(round((top - start) / step))
    speeds = [round(start + i * step, 3) for i in range(n + 1)]
    o = [f"# Lantern power curve, {start:g}-{top:g} m/s\n",
         "Model potential: the model's output if the tube stayed tuned and locked on with the best generator "
         "load and nothing failed (not achievable). Within limits: the most the machine can deliver with every "
         "part within its limits, retuning as far as the neck's bending mode allows and riding the lock-on tail "
         "beyond that. As designed: the default control (track to 7 m/s, cap to 8 m/s, brake above).\n"]
    o += curve_summary(d)
    o.append("")
    o += curve_table(d, speeds)
    return "\n".join(o)


def write_curve_csv(d: Design, path: str, step: float, top: float, start: float) -> None:
    n = int(round((top - start) / step))
    rows = curve_rows(d, [round(start + i * step, 3) for i in range(n + 1)])
    with open(path, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        for r in rows:
            w.writerow({k: (round(v, 4) if isinstance(v, float) else v) for k, v in r.items()})


def summary_lines(d: Design) -> list[str]:
    surv, part, winds = survival(d)
    ci = cut_in(d)
    op = operating_peak(d)
    return [
        f"- Cut-in (starts and produces >10 mW): {f2(ci,1)} m/s"
        + (" with kick-start" if d.kick_start else " without kick-start"),
        f"- Tracking: {d.U_tune_min:g}-{d.U_tune_max:g} m/s; power-capped at {f2(rated_power(d),2)} W up to "
        f"{f2(brake_speed(d),1)} m/s; braked above that",
        f"- Survives (parked, braked) up to **{f2(surv,1)} m/s**, limited by the {part}. "
        f"Requirement: {d.U_storm:g} m/s. Per part: " + ", ".join(f"{k} {f2(v,0)}" for k, v in winds.items()),
        "- Worst while swinging: " + (", ".join(f"{k} {pct(v)}" for k, v in op.items()) or "n/a"),
        f"- Neck-tube bending mode about {f2(neck_mode_freq(d),1)} Hz (swing must stay below "
        f"{f2(neck_mode_freq(d)/d.mode_margin,1)} Hz, reached at {f2(structural_tuning_limit(d),1)} m/s)",
    ]


def report(d: Design) -> str:
    o: list[str] = []
    m = masses(d)
    I = inertias(d)
    G = gear_ratio(d)
    o.append("# Lantern calculator report\n")
    o.append(
        f"Tube {d.D*1000:.0f} mm x {d.L*1000:.0f} mm, neck {d.neck*1000:.0f} mm "
        f"({d.neck_od*1000:.0f}x{d.neck_id*1000:.0f} mm carbon), end discs {m['disc_dia']*1000:.0f} mm, "
        f"shell {d.shell_areal:.3f} kg/m^2 ({'sandwich' if d.shell_sandwich else 'single skin'}, "
        f"{d.shell_core_t*1000:.0f} mm core), survival requirement {d.U_storm:g} m/s\n"
    )
    fails = constraint_failures(d)
    o.append("Constraint check: " + ("all pass" if not fails else "FAILS " + ", ".join(fails)) + "\n")

    o.append("## Operating summary\n")
    o += summary_lines(d)
    o.append("")

    o.append("## Masses (kg)\n\n| Part | Mass |\n|---|---|")
    o.append(f"| Tube shell incl. rings and seams | {f2(m['shell'],3)} |")
    o.append(f"| End discs, each | {f2(m['disc_each'],3)} |")
    o.append(f"| Bottom spider | {f2(m['spider'],3)} |")
    o.append(f"| Neck tube | {f2(m['neck'],3)} |")
    o.append(f"| Hub, axle, carriage, belt arc | {f2(m['hub'],3)} |")
    o.append(f"| **Total swinging mass** | **{f2(m['swinging'],3)}** |\n")

    o.append("## Inertia about the hinge (kg m^2)\n\n| Part | Inertia |\n|---|---|")
    for k in ("shell", "discs", "spider", "neck", "hub", "generator"):
        o.append(f"| {k} | {f2(I[k],4)} |")
    o.append(f"| Structural total | {f2(I['structural'],4)} |")
    o.append(f"| Air moving with the tube | {f2(I['added'],4)} |")
    o.append(f"| **Total** | **{f2(I['total'],4)}** |")
    o.append(f"| Mass ratio (structural / displaced air) | {f2(I['mass_ratio'],2)} |\n")
    o.append(
        f"- Gear ratio: {f2(G,1)}:1 ({d.arc_radius*1000:.0f} mm arc to {d.pulley_teeth}-tooth GT2 pulley)\n"
        f"- Mode-shape factor gamma: {f2(mode_gamma(d),3)}\n"
        f"- Effective length after end losses: {f2(effective_length(d),3)} m\n"
        f"- Gravity (destabilising) stiffness: {f2(gravity_stiffness(d),2)} N m/rad\n"
    )

    o.append("## Tuning\n")
    o.append(f"Two opposing springs, each {f2(spring_rate(d)/1000,2)} N/mm.\n")
    o.append("| Wind (m/s) | Tune f_n (Hz) | Stiffness (N m/rad) | Carriage below hinge (mm) |\n|---|---|---|---|")
    for U in (2.0, 3.0, 4.0, 4.5, 5.0, 6.0, 7.0):
        o.append(f"| {U} | {f2(f_natural(d,U))} | {f2(k_required(d,U),1)} | {f2(1000*carriage_radius(d,U),1)} |")
    slope = 1000 * (carriage_radius(d, 6.0) - carriage_radius(d, 4.0)) / 2.0
    o.append(f"\nCarriage moves about {f2(slope,1)} mm per 1 m/s between 4 and 6 m/s.\n")

    o.append("## Operating points while tracking (model central case)\n")
    o.append(
        "| Wind | Re | Swing f (Hz) | Wind power (W) | Mech (W) | Elec (W) | Elec low case (W) | "
        "Mech eff | Swing (deg) | Peak torque (N m) | Gen zeta | Parasitic zeta | "
        "Circuit R (ohm) | Copper eff | EMF peak (V) | Gen peak rpm | Top accel (g) |"
    )
    o.append("|" + "---|" * 17)
    for U in (2.0, 3.0, 4.5, 6.0, 7.0):
        e = solve(d, U)
        o.append(
            f"| {U} | {e['Re']:.0f} | {f2(e['f_osc'])} | {f2(e['p_wind'],1)} | {f2(e['p_mech'],2)} | "
            f"{f2(e['p_elec'],2)} | {f2(d.derate*e['p_elec'],2)} | {f2(100*e['eta_mech'],1)} % | "
            f"{f2(e['theta_deg'],1)} | {f2(e['torque_peak'])} | {f2(e['zeta_e'],3)} | {f2(e['zeta_par'],4)} | "
            f"{f2(e['R_total'],0)} | {f2(100*e['copper'],0)} % | {f2(e['emf_peak'],1)} | "
            f"{f2(e['gen_rpm_peak'],0)} | {f2(e['top_accel_g'],1)} |"
        )
    e = solve(d, 4.5)
    o.append(
        f"\nAt 4.5 m/s: tube swings +/-{e['a_bot']*1000:.0f} mm at the bottom, +/-{e['a_mid']*1000:.0f} mm "
        f"mid-height, +/-{e['a_top']*1000:.0f} mm at the top; generator swings +/-{e['gen_swing_deg']:.0f} deg. "
        f"Friction: bushings {f2(e['t_bush'],3)} N m, generator drag {f2(e['t_gen'],3)} N m (at the hinge).\n"
    )

    o.append("## Wind envelope, 1-40 m/s\n")
    o.append("Utilisation = load / allowable for each part (over 100% fails). Neck, skin and hub combine drag "
             "with the swing's inertia; wall is ovalling of the shell under wind pressure; discs is gust lift "
             "on the end discs. Parked modes use drag coefficient "
             f"{d.Cd_storm}; swinging modes {d.Cd_viv}.\n")
    o += envelope_table(d, ENVELOPE_SPEEDS)
    o.append("")

    o.append("## Power from 1 to 40 m/s\n")
    o.append("Model potential = output if the tube stayed tuned and locked on with nothing failing (not achievable). "
             "Within limits = the most it can deliver with every part within limits, retuning as far as the neck's "
             "bending mode allows. As designed = the default control.\n")
    o += curve_summary(d)
    o.append("")
    o += curve_table(d, CURVE_SPEEDS)
    o.append("")

    o.append(f"## Structure at the survival requirement ({d.U_storm:g} m/s, parked and braked)\n")
    lo = loads(d, d.U_storm, {"mode": "braked", "op": None})
    o.append(f"- Drag on the tube {f2(lo['drag'],0)} N; bending moment at tube base {f2(lo['m_drag_base'],0)} N m, "
             f"at the hinge {f2(lo['m_drag_hinge'],0)} N m (hub built for {d.M_hinge_max:g})")
    o.append(f"- Neck stress {f2(lo['neck_peak_MPa'],0)} MPa (allowable {d.neck_allow/1e6:.0f}); "
             f"skin stress at tube base {f2(lo['skin_MPa'],1)} MPa (allowable {d.skin_allow/1e6:.0f})")
    o.append(f"- Shell ovalling {f2(lo['wall_demand'],2)} N m/m against a wall capacity of {f2(lo['wall_capacity'],2)} N m/m")
    o.append(f"- End-disc gust utilisation {pct(lo['utils']['discs'])}")
    o.append(f"- Hinge bushing load {f2(lo['bushing_N'],0)} N each")
    o.append(f"- Post base moment with hinge at {d.hub_height:g} m: {f2(lo['post_moment'],0)} N m (size the post to your local wind code)")
    cyc = f_natural(d, 4.5) * d.duty * 365.25 * 24 * 3600
    o.append(f"- Swing cycles per year at {int(100*d.duty)} % duty: {cyc:.1e}\n")

    o.append("## Annual energy (very rough)\n")
    o.append(
        f"Rayleigh wind at hub height, power curve from the envelope above (tracking, then capped at "
        f"{f2(rated_power(d),2)} W, braked from {f2(brake_speed(d),1)} m/s), "
        f"{int(100*d.lock_factor)} % of swinging time assumed locked on. Low case = {d.derate} x central.\n"
    )
    o.append("| Site mean wind | Low (kWh/yr) | Central (kWh/yr) |\n|---|---|---|")
    for V in (3.0, 3.5, 4.5, 5.5):
        E = annual_energy(d, V)
        o.append(f"| {V} m/s | {f2(d.derate*E,1)} | {f2(E,1)} |")
    o.append("")
    return "\n".join(o)


def envelope_report(d: Design, step: float, top: float, start: float) -> str:
    n = int(round((top - start) / step))
    speeds = [round(start + i * step, 3) for i in range(n + 1)]
    o = [f"# Lantern wind envelope, {start:g}-{top:g} m/s\n"]
    o += summary_lines(d)
    o.append("")
    o += envelope_table(d, speeds)
    return "\n".join(o)


def write_envelope_csv(d: Design, path: str, step: float, top: float, start: float) -> None:
    n = int(round((top - start) / step))
    rows = envelope_rows(d, [round(start + i * step, 3) for i in range(n + 1)])
    with open(path, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        for r in rows:
            w.writerow({k: (round(v, 4) if isinstance(v, float) else v) for k, v in r.items()})


# ---------------------------------------------------------------- sweep


def frange(lo: float, hi: float, step: float) -> list[float]:
    n = int(round((hi - lo) / step))
    return [round(lo + i * step, 6) for i in range(n + 1)]


GRID_COLUMNS = [
    "rank", "passes", "failed_limits",
    "D_mm", "neck_mm", "disc_ratio", "disc_dia_mm", "shell", "shell_kg_m2",
    "pulley_teeth", "gear_ratio", "neck_tube", "total_height_m",
    "p_elec_4p5_W", "p_elec_low_4p5_W", "p_mech_4p5_W", "eta_mech_4p5",
    "annual_kWh", "annual_low_kWh", "site_mean_wind",
    "cut_in_ms", "rated_W", "brake_ms", "survival_ms", "survival_limit",
    "mass_ratio", "inertia_total_kgm2", "swinging_mass_kg", "swing_deg_4p5",
    "top_swing_mm_4p5", "peak_torque_4p5_Nm", "top_accel_4p5_g", "parasitic_zeta_4p5",
    "spring_rate_N_mm", "circuit_R_4p5_ohm", "copper_eff_4p5", "emf_peak_4p5_V",
    "gen_peak_rpm_4p5", "Re_at_Umax", "max_neck_fatigue_util", "storm_hinge_moment_Nm",
]


def grid_row(d: Design, shell: str, fails: list[str], site: float, annual: float) -> dict:
    e = solve(d, 4.5)
    I = inertias(d)
    surv, part, _ = survival(d)
    lo = loads(d, d.U_storm, {"mode": "braked", "op": None})
    return {
        "passes": "yes" if not fails else "no",
        "failed_limits": "; ".join(fails),
        "D_mm": round(d.D * 1000),
        "neck_mm": round(d.neck * 1000),
        "disc_ratio": round(d.disc_ratio, 2),
        "disc_dia_mm": round(d.disc_ratio * d.D * 1000) if d.disc_ratio > 1.0 else 0,
        "shell": shell,
        "shell_kg_m2": d.shell_areal,
        "pulley_teeth": d.pulley_teeth,
        "gear_ratio": round(gear_ratio(d), 2),
        "neck_tube": f"{d.neck_od*1000:.0f}x{d.neck_id*1000:.0f}",
        "total_height_m": round(d.neck + d.L, 3),
        "p_elec_4p5_W": round(e["p_elec"], 4),
        "p_elec_low_4p5_W": round(d.derate * e["p_elec"], 4),
        "p_mech_4p5_W": round(e["p_mech"], 4),
        "eta_mech_4p5": round(e["eta_mech"], 4),
        "annual_kWh": round(annual, 3),
        "annual_low_kWh": round(d.derate * annual, 3),
        "site_mean_wind": site,
        "cut_in_ms": round(cut_in(d), 1),
        "rated_W": round(rated_power(d), 3),
        "brake_ms": round(brake_speed(d), 2),
        "survival_ms": round(surv, 1),
        "survival_limit": part,
        "mass_ratio": round(I["mass_ratio"], 3),
        "inertia_total_kgm2": round(I["total"], 4),
        "swinging_mass_kg": round(masses(d)["swinging"], 3),
        "swing_deg_4p5": round(e["theta_deg"], 2),
        "top_swing_mm_4p5": round(e["a_top"] * 1000, 1),
        "peak_torque_4p5_Nm": round(e["torque_peak"], 3),
        "top_accel_4p5_g": round(e["top_accel_g"], 2),
        "parasitic_zeta_4p5": round(e["zeta_par"], 5),
        "spring_rate_N_mm": round(spring_rate(d) / 1000, 2),
        "circuit_R_4p5_ohm": round(e["R_total"], 1),
        "copper_eff_4p5": round(e["copper"], 3),
        "emf_peak_4p5_V": round(e["emf_peak"], 1),
        "gen_peak_rpm_4p5": round(e["gen_rpm_peak"]),
        "Re_at_Umax": round(d.U_tune_max * d.D / NU),
        "max_neck_fatigue_util": round(operating_peak(d).get("neck fatigue", 0.0), 3),
        "storm_hinge_moment_Nm": round(lo["m_drag_hinge"], 1),
    }


def write_grid_csv(path: str, rows: list[dict], objective: str) -> None:
    key = "annual_kWh" if objective == "annual" else "p_elec_4p5_W"
    passing = sorted((r for r in rows if r["passes"] == "yes"), key=lambda r: r[key], reverse=True)
    for i, r in enumerate(passing, 1):
        r["rank"] = i
    with open(path, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=GRID_COLUMNS)
        w.writeheader()
        for r in rows:
            w.writerow({c: r.get(c, "") for c in GRID_COLUMNS})


def sweep(base: Design, args: argparse.Namespace) -> str:
    Ds = frange(args.D_min, args.D_max, args.D_step)
    necks = frange(args.neck_min, args.neck_max, args.neck_step)
    discs = frange(args.disc_min, args.disc_max, args.disc_step)
    shells = args.shells.split(",")
    teeth = [int(t) for t in args.teeth.split(",")]

    def build(D, nk, dr, sh, t) -> Design:
        d = replace(base, D=D, neck=nk, disc_ratio=dr, pulley_teeth=t, **SHELLS[sh])
        return size_neck(d) if args.neck_auto else d

    def score(d: Design) -> float:
        if args.objective == "annual":
            return annual_energy(d, args.site, step=0.5)
        return solve(d, args.wind)["p_elec"]

    results = []
    rows: list[dict] = []
    rejected: dict[str, int] = {}
    total = 0
    for D, nk, dr, sh, t in itertools.product(Ds, necks, discs, shells, teeth):
        total += 1
        d = build(D, nk, dr, sh, t)
        fails = constraint_failures(d)
        for f in fails:
            rejected[f] = rejected.get(f, 0) + 1
        if args.csv:
            ann = annual_energy(d, args.site, step=0.5)
            rows.append(grid_row(d, sh, fails, args.site, ann))
        if fails:
            continue
        results.append((score(d), d, sh))
    results.sort(key=lambda r: r[0], reverse=True)
    if args.csv:
        write_grid_csv(args.csv, rows, args.objective)

    unit = "kWh/yr" if args.objective == "annual" else "W"
    what = (f"central-case annual energy at a {args.site} m/s site" if args.objective == "annual"
            else f"electrical power at {args.wind} m/s")
    o = [f"# Lantern sweep: ranked by {what}, survival requirement {base.U_storm:g} m/s\n"]
    o.append(
        f"{total} combinations: D {Ds[0]}-{Ds[-1]} m, neck {necks[0]}-{necks[-1]} m, "
        f"disc ratio {discs[0]}-{discs[-1]}, shells {', '.join(shells)}, pulley teeth {teeth}"
        f"{', neck tube sized automatically' if args.neck_auto else ''}.  "
    )
    o.append(f"{len(results)} pass all limits. Rejected (a design can fail several): " +
             (", ".join(f"{k} {v}" for k, v in sorted(rejected.items())) or "none") + "\n")
    if not results:
        return "\n".join(o)

    o.append(f"| Rank | Score ({unit}) | D (mm) | Neck (mm) | Neck tube | Disc ratio | Shell | Teeth | Gear | "
             "Mass ratio | Mech eff 4.5 | Swing 4.5 (deg) | Cut-in | Survives to | Re at U_max |")
    o.append("|" + "---|" * 15)
    for i, (sc, d, sh) in enumerate(results[: args.top], 1):
        e = solve(d, 4.5)
        surv, part, _ = survival(d)
        o.append(
            f"| {i} | {f2(sc,2)} | {d.D*1000:.0f} | {d.neck*1000:.0f} | {d.neck_od*1000:.0f}x{d.neck_id*1000:.0f} | "
            f"{f2(d.disc_ratio,1)} | {sh} | {d.pulley_teeth} | {f2(gear_ratio(d),1)} | {f2(inertias(d)['mass_ratio'],2)} | "
            f"{f2(100*e['eta_mech'],1)} % | {f2(e['theta_deg'],1)} | {f2(cut_in(d),1)} | {f2(surv,1)} ({part}) | "
            f"{d.U_tune_max*d.D/NU:.0f} |"
        )

    best_score, best, best_shell = results[0]
    o.append("\n## Sensitivity around the best design (one variable at a time)\n")
    o.append("| Variable | Value | Score | vs best |\n|---|---|---|---|")
    probes = [("D (mm)", "D", Ds, 1000), ("Neck (mm)", "neck", necks, 1000),
              ("Disc ratio", "disc_ratio", discs, 1), ("Pulley teeth", "pulley_teeth", teeth, 1)]
    for label, attr, values, scale in probes:
        for v in values[:: max(1, len(values) // 6)]:
            d = replace(best, **{attr: v})
            d = size_neck(d) if args.neck_auto else d
            fails = constraint_failures(d)
            sc = score(d)
            note = f"{100*(sc/best_score-1):+.0f} %" + (f" (fails {', '.join(fails)})" if fails else "")
            o.append(f"| {label} | {v*scale:g} | {f2(sc,2)} | {note} |")
    for sh in shells:
        d = replace(best, **SHELLS[sh])
        d = size_neck(d) if args.neck_auto else d
        fails = constraint_failures(d)
        sc = score(d)
        note = f"{100*(sc/best_score-1):+.0f} %" + (f" (fails {', '.join(fails)})" if fails else "")
        o.append(f"| Shell | {sh} | {f2(sc,2)} | {note} |")
    o.append(f"\nBest: shell {best_shell}. Full report for it follows.\n")
    o.append(report(best))
    return "\n".join(o)


# ---------------------------------------------------------------- CLI


def add_design_args(p: argparse.ArgumentParser) -> None:
    p.add_argument("--config", choices=sorted(CONFIGS), default="B",
                   help="named starting configuration (default B)")
    p.add_argument("--shell", choices=sorted(SHELLS), default=None,
                   help="apply a shell construction preset (also sets the end discs)")
    for f in fields(Design):
        p.add_argument(f"--{f.name}", type=float, default=None, help=f"default {f.default}")


def design_from(args: argparse.Namespace) -> Design:
    over = dict(CONFIGS[getattr(args, "config", "B")])
    if getattr(args, "shell", None):
        over.update(SHELLS[args.shell])
    for f in fields(Design):
        v = getattr(args, f.name, None)
        if v is not None:
            over[f.name] = int(v) if f.type in ("int", int) else v
    return replace(Design(), **over)


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = p.add_subparsers(dest="cmd")
    pr = sub.add_parser("report", help="full report for one design (default)")
    add_design_args(pr)
    pe = sub.add_parser("envelope", help="mode, power and every limit at each wind speed")
    add_design_args(pe)
    pe.add_argument("--from", dest="start", type=float, default=1.0)
    pe.add_argument("--to", dest="top", type=float, default=40.0)
    pe.add_argument("--step", type=float, default=1.0)
    pe.add_argument("--csv", default=None, help="also write the envelope to this CSV file")
    pc = sub.add_parser("curve", help="electrical power from 1 to 40 m/s: as designed, within limits, potential")
    add_design_args(pc)
    pc.add_argument("--from", dest="start", type=float, default=1.0)
    pc.add_argument("--to", dest="top", type=float, default=40.0)
    pc.add_argument("--step", type=float, default=1.0)
    pc.add_argument("--csv", default=None, help="also write the curve to this CSV file")
    ps = sub.add_parser("sweep", help="grid search for the highest-output design")
    add_design_args(ps)
    ps.add_argument("--objective", choices=("power", "annual"), default="power")
    ps.add_argument("--wind", type=float, default=4.5, help="wind speed for --objective power")
    ps.add_argument("--site", type=float, default=4.5, help="site mean wind for annual energy")
    ps.add_argument("--D-min", dest="D_min", type=float, default=0.10)
    ps.add_argument("--D-max", dest="D_max", type=float, default=0.40)
    ps.add_argument("--D-step", dest="D_step", type=float, default=0.02)
    ps.add_argument("--neck-min", dest="neck_min", type=float, default=0.0)
    ps.add_argument("--neck-max", dest="neck_max", type=float, default=0.8)
    ps.add_argument("--neck-step", dest="neck_step", type=float, default=0.1)
    ps.add_argument("--disc-min", dest="disc_min", type=float, default=1.0)
    ps.add_argument("--disc-max", dest="disc_max", type=float, default=2.4)
    ps.add_argument("--disc-step", dest="disc_step", type=float, default=0.2)
    ps.add_argument("--shells", default=",".join(SHELLS))
    ps.add_argument("--teeth", default="10,12,16,20,24")
    ps.add_argument("--no-neck-auto", dest="neck_auto", action="store_false",
                    help="keep the configuration's neck tube instead of sizing it per design")
    ps.add_argument("--top", type=int, default=15)
    ps.add_argument("--csv", default=None,
                    help="also write every grid point (passing or not) to this CSV file")
    args = p.parse_args()
    d = design_from(args) if args.cmd else Design()
    if args.cmd == "sweep":
        print(sweep(d, args))
    elif args.cmd == "curve":
        if args.csv:
            write_curve_csv(d, args.csv, args.step, args.top, args.start)
        print(curve_report(d, args.step, args.top, args.start))
    elif args.cmd == "envelope":
        if args.csv:
            write_envelope_csv(d, args.csv, args.step, args.top, args.start)
        print(envelope_report(d, args.step, args.top, args.start))
    else:
        print(report(d))


if __name__ == "__main__":
    main()
