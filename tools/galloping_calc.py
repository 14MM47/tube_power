#!/usr/bin/env python3
"""Lantern G (galloping) design calculator and optimiser, calm to 40 m/s.

A square-section prism on a hinged neck gallops: its own sideways motion
tilts the wind it sees, and a square's side force then pushes the same way
as the motion, so it extracts energy at any wind above onset with no
lock-on band. Power grows roughly with wind cubed, so the machine needs a
throttle: the prism turns on its own axis (pitch) a few degrees to weaken
the galloping, and turns 45 degrees (feathered) to stop it altogether.

    python3 tools/galloping_calc.py                      # report for Lantern 250-G
    python3 tools/galloping_calc.py envelope              # every limit, 1-40 m/s
    python3 tools/galloping_calc.py curve --compare       # power 1-40 m/s, with the VIV designs
    python3 tools/galloping_calc.py sweep                 # best design that generates to 40 m/s
    python3 tools/galloping_calc.py sweep --site 6 --csv grid.csv

Model: quasi-steady galloping with a cubic side-force curve
C_y = A1*alpha - A3*alpha^3 (Parkinson), harmonic balance for the hinged
mode, Coulomb friction, and the same structural checks as
tools/lantern_calc.py adapted to a flat-sided prism. See
designs/lantern-250-g/physics.md. Only the square's coefficients are well
established; everything is an estimate until measured. Standard library only.
"""

from __future__ import annotations

import argparse
import csv
import itertools
import math
import os
import sys
from dataclasses import dataclass, fields, replace
from functools import lru_cache

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lantern_calc import G0, NECK_TUBES, NU, RHO, frange  # noqa: E402

# Panel constructions for the flat-sided prism. panel_cap is the allowable
# bending moment per unit width of a panel (N m/m); skin_t and skin_allow
# give the prism's overall bending strength at its base. End plates are
# built the same way.
SHELLS = {
    # extruded polystyrene (~37 kg/m^3) with glass tissue + epoxy (~0.05 kg/m^2 per face)
    "xps5": dict(shell_areal=0.285, panel_cap=10.0, panel_oneway=0, skin_t=0.05e-3, skin_allow=40e6),
    "xps6-storm": dict(shell_areal=0.352, panel_cap=12.0, panel_oneway=0, skin_t=0.15e-3, skin_allow=40e6),
    "xps10-storm": dict(shell_areal=0.46, panel_cap=20.0, panel_oneway=0, skin_t=0.15e-3, skin_allow=40e6),
    # 4 mm twin-wall polypropylene sign board, flutes vertical (spans between bulkheads)
    "corflute4": dict(shell_areal=0.70, panel_cap=19.0, panel_oneway=1, skin_t=0.70e-3, skin_allow=12e6),
}

# Generators. Ke in V s/rad (= N m/A) and R_coil in ohm for the rectified
# three-phase machine; gen_drag is bearing and iron-loss drag at the shaft.
# Values are assumed for the size class: measure your motor.
GENERATORS = {
    "5208": dict(Ke=0.38, R_coil=12.0, gen_rotor_J=6e-5, gen_drag=0.004, gen_cogging=0.005,
                 gen_heat_max=5.0, gen_rpm_max=1500.0),
    "8108": dict(Ke=0.20, R_coil=0.80, gen_rotor_J=2.5e-4, gen_drag=0.010, gen_cogging=0.02,
                 gen_heat_max=20.0, gen_rpm_max=3000.0),
}

# Galloping coefficients (smooth flow). Only the square's are well established.
SECTIONS = {
    "square": dict(A1=2.3, A3=18.0, alpha_cap=0.40, Cd0=2.1, Cd_min=1.45, beta_cdmin=0.227,
                   Cd_feather=1.65, St=0.13, Ca=1.19),
    # Uncertain values read from literature summaries; for sensitivity only.
    "triangle-30": dict(A1=2.9, A3=6.2, alpha_cap=0.30, Cd0=1.9, Cd_min=1.6, beta_cdmin=0.2,
                        Cd_feather=1.9, St=0.15, Ca=1.0),
    "d-section": dict(A1=0.79, A3=0.19, alpha_cap=0.30, Cd0=1.6, Cd_min=1.5, beta_cdmin=0.2,
                      Cd_feather=1.6, St=0.2, Ca=1.0),
}

# Maximum bending moment in a simply supported plate under uniform pressure,
# coefficient x p x a^2 (a = short side), by aspect ratio b/a (Timoshenko, nu = 0.3).
PLATE_BETA = [(1.0, 0.0479), (1.2, 0.0627), (1.4, 0.0755), (1.6, 0.0862), (1.8, 0.0948),
              (2.0, 0.1017), (3.0, 0.1189), (4.0, 0.1235), (5.0, 0.1246), (1e9, 0.125)]


@dataclass(frozen=True)
class GDesign:
    """Defaults are Lantern 250-G, the recommended galloping configuration."""

    # Geometry
    D: float = 0.25  # prism face width (square section), m
    L: float = 1.00  # prism height (the 1 m limit), m
    neck: float = 0.40  # hinge axis to bottom of prism, m
    section: str = "square"

    # Galloping and flow coefficients (see SECTIONS)
    A1: float = 2.3  # side-force slope
    A3: float = 18.0  # cubic softening
    alpha_cap: float = 0.40  # largest velocity angle at the prism top the fit is trusted to, rad
    Cd0: float = 2.1  # drag, face on
    Cd_min: float = 1.45  # drag minimum
    beta_cdmin: float = 0.227  # pitch at the drag minimum, rad (13 deg)
    Cd_feather: float = 1.65  # drag when feathered (45 deg), on face width
    St: float = 0.13  # Strouhal number (vortex shedding, for reporting)
    Ca: float = 1.19  # added mass / (rho pi D^2 / 4)
    Ustar_min: float = 20.0  # quasi-steady theory only trusted at U/(f D) at or above this
    turb_factor: float = 1.0  # multiplier on A1 for site turbulence (1 = smooth-flow data)

    # Prism panels (see SHELLS)
    shell_areal: float = 0.352  # kg/m^2
    panel_cap: float = 12.0  # allowable panel bending moment, N m/m
    panel_oneway: int = 0  # 1 = panel spans one way between bulkheads (corrugated board)
    skin_t: float = 0.15e-3  # outer skin thickness at the prism base, m
    skin_allow: float = 40e6  # Pa
    bulkhead_pitch: float = 0.25  # spacing of internal bulkheads, m
    bulkhead_frac: float = 0.5  # bulkhead mass as a fraction of a full D x D panel (lightening holes)
    seams_mass: float = 0.03  # corner tapes and glue, kg
    panel_cp: float = 2.0  # net pressure coefficient for panel bending

    # End plates: square, side = plate_ratio x D; 1.0 = plain end caps
    plate_ratio: float = 1.6
    end_loss_D: float = 0.5  # span lost per bare end, in face widths (assumed)
    plate_full_ratio: float = 2.0  # plate ratio that removes the end loss (assumed)
    gust_CL: float = 1.1  # end-plate lift coefficient in a gust

    # Neck, hub and pitch drive
    spider_mass: float = 0.02  # kg
    neck_od: float = 0.040  # m
    neck_id: float = 0.037  # m
    carbon_density: float = 1550.0  # kg/m^3
    carbon_E: float = 100e9  # Pa
    hub_mass: float = 0.45  # hub, axle, spring carriage, belt arc, kg
    pitch_mass: float = 0.30  # pitch bearings, gearmotor, return spring and clutch, kg
    hub_radius: float = 0.07  # m
    CM_pitch: float = 0.10  # aerodynamic moment coefficient about the prism axis (assumed)

    # Drive
    arc_radius: float = 0.100  # m
    pulley_teeth: int = 12
    belt_pitch: float = 0.002  # m
    belt_eff: float = 0.97

    # Generator (see GENERATORS)
    gen: str = "8108"
    Ke: float = 0.20
    R_coil: float = 0.80
    gen_rotor_J: float = 2.5e-4
    gen_drag: float = 0.010
    gen_cogging: float = 0.02
    gen_heat_max: float = 20.0
    gen_rpm_max: float = 3000.0
    conv_eff: float = 0.85
    R_margin: float = 1.2  # circuit resistance must exceed this x coil resistance

    # Losses
    zeta_struct: float = 0.003
    bush_span: float = 0.25  # distance between the two hinge bearings, m
    axle_d: float = 0.020  # m
    bush_mu: float = 0.005  # deep-groove ball bearings (rolling friction referred to the axle)
    hinge_drag: float = 0.05  # bearing seal drag, both bearings, N m

    # Springs: two opposing springs on a carriage below the hinge
    r_spring_min: float = 0.015  # m
    r_spring_max: float = 0.140  # m
    f_spring_top: float = 3.0  # swing frequency with the carriage furthest out, Hz
    swing_stop_deg: float = 20.0  # rubber end stops, deg
    swing_design_deg: float = 15.0  # swing plus static lean allowed in operation, deg
    spring_force_max: float = 1500.0  # per-spring force limit, N

    # Control
    P_rated: float = 20.0  # electrical power cap, W
    U_cut_out: float = 40.0  # feather above this wind, m/s
    pitch_step: float = 0.005  # controller search step, rad
    beta_feather: float = 0.785  # 45 deg
    kick_start: int = 1

    # Limits
    U_storm: float = 45.0  # survival requirement, feathered and braked, m/s
    neck_allow: float = 400e6
    neck_fatigue_allow: float = 200e6
    M_hinge_max: float = 500.0  # N m
    V_max: float = 60.0  # electronics voltage rating, V
    mode_margin: float = 1.5
    max_total_height: float = 2.0
    AR_min: float = 3.0  # prism height / face width, smallest allowed

    # Site and post
    hub_height: float = 3.0
    head_area: float = 0.04
    vane_area: float = 0.10
    derate: float = 0.5  # low case = derate x central
    avail: float = 0.8  # share of time the model output is achieved (yaw lag, gusts, restarts)


CONFIGS = {"G": {}}

# ---------------------------------------------------------------- geometry


def r1(d: GDesign) -> float:
    return d.neck


def r2(d: GDesign) -> float:
    return d.neck + d.L


@lru_cache(maxsize=4096)
def span_int(d: GDesign, n: int) -> float:
    """Integral of r^n over the prism span."""
    return (r2(d) ** (n + 1) - r1(d) ** (n + 1)) / (n + 1)


@lru_cache(maxsize=4096)
def gear_ratio(d: GDesign) -> float:
    return d.arc_radius / (d.pulley_teeth * d.belt_pitch / (2.0 * math.pi))


@lru_cache(maxsize=4096)
def span_factor(d: GDesign) -> float:
    if d.plate_ratio <= 1.0:
        e = d.end_loss_D
    else:
        e = d.end_loss_D * max(0.0, 1.0 - (d.plate_ratio - 1.0) / (d.plate_full_ratio - 1.0))
    return max(0.0, d.L - 2.0 * e * d.D) / d.L


@lru_cache(maxsize=4096)
def c_max(d: GDesign) -> float:
    """Largest generator damping at the hinge (terminals shorted), N m s/rad."""
    return gear_ratio(d) ** 2 * d.Ke**2 / d.R_coil


@lru_cache(maxsize=4096)
def masses(d: GDesign) -> dict[str, float]:
    n_bulk = max(0, round(d.L / d.bulkhead_pitch) - 1)
    bulk = n_bulk * d.bulkhead_frac * d.shell_areal * d.D**2
    shell = d.shell_areal * 4.0 * d.D * d.L + bulk + d.seams_mass
    side = max(d.plate_ratio, 1.0) * d.D
    plate = d.shell_areal * side**2
    neck_lin = d.carbon_density * math.pi / 4.0 * (d.neck_od**2 - d.neck_id**2)
    m = {
        "shell": shell, "bulkheads": bulk, "n_bulk": n_bulk, "plate_each": plate, "plate_side": side,
        "spider": d.spider_mass, "neck": neck_lin * d.neck, "neck_lin": neck_lin,
        "hub": d.hub_mass + d.pitch_mass,
    }
    m["above"] = shell + 2 * plate + d.spider_mass + m["neck"]
    m["swinging"] = m["above"] + m["hub"]
    return m


@lru_cache(maxsize=4096)
def inertias(d: GDesign) -> dict[str, float]:
    m = masses(d)
    a, b = r1(d), r2(d)
    parts = {
        "shell": m["shell"] * span_int(d, 2) / d.L,
        "plates": m["plate_each"] * (a**2 + b**2) + 2 * m["plate_each"] * m["plate_side"] ** 2 / 12.0,
        "spider": m["spider"] * a**2,
        "neck": m["neck_lin"] * d.neck**3 / 3.0,
        "hub": m["hub"] * d.hub_radius**2,
        "generator": d.gen_rotor_J * gear_ratio(d) ** 2,
    }
    structural = sum(parts.values())
    displaced = RHO * d.D**2 * span_int(d, 2)
    added = d.Ca * RHO * math.pi * d.D**2 / 4.0 * span_int(d, 2)
    parts.update(
        above=parts["shell"] + parts["plates"] + parts["spider"] + parts["neck"],
        structural=structural, displaced=displaced, added=added, total=structural + added,
        mass_ratio=structural / displaced,
    )
    return parts


@lru_cache(maxsize=4096)
def gravity_stiffness(d: GDesign) -> float:
    m = masses(d)
    a, b = r1(d), r2(d)
    return G0 * (m["shell"] * (a + d.L / 2) + m["plate_each"] * (a + b) + m["spider"] * a
                 + m["neck"] * d.neck / 2)


def neck_I(d: GDesign) -> float:
    return math.pi / 64.0 * (d.neck_od**4 - d.neck_id**4)


@lru_cache(maxsize=4096)
def neck_mode_freq(d: GDesign) -> float:
    """First bending frequency of neck + prism with the hinge held rigid, Hz (as lantern_calc)."""
    m = masses(d)
    a = max(d.neck, 1e-3)
    e = d.L / 2.0
    EI = d.carbon_E * neck_I(d)
    k11, k12, k22 = 12 * EI / a**3, -6 * EI / a**2, 4 * EI / a
    m_air = d.Ca * RHO * math.pi * d.D**2 / 4.0 * d.L
    mt = m["shell"] + 2 * m["plate_each"] + m_air
    J = ((m["shell"] + m_air) * d.L**2 / 12.0 + 2 * m["plate_each"] * e**2
         + 2 * m["plate_each"] * m["plate_side"] ** 2 / 12.0)
    m11 = mt + m["spider"] + 0.24 * m["neck"]
    m12, m22 = mt * e, mt * e**2 + J
    A = m11 * m22 - m12**2
    B = -(k11 * m22 + k22 * m11 - 2 * k12 * m12)
    C = k11 * k22 - k12**2
    w2 = (-B - math.sqrt(B * B - 4 * A * C)) / (2 * A)
    return math.sqrt(w2) / (2.0 * math.pi)


def plate_beta(ratio: float) -> float:
    for (x0, y0), (x1, y1) in zip(PLATE_BETA, PLATE_BETA[1:]):
        if ratio <= x1:
            return y0 + (y1 - y0) * (max(ratio, 1.0) - x0) / (x1 - x0)
    return 0.125


@lru_cache(maxsize=4096)
def panel_moment_per_q(d: GDesign) -> float:
    """Panel bending moment per unit width per unit dynamic pressure, m^2."""
    s = d.L / (masses(d)["n_bulk"] + 1)
    if d.panel_oneway:
        return d.panel_cp * s**2 / 8.0
    a, b = min(d.D, s), max(d.D, s)
    return d.panel_cp * plate_beta(b / a) * a**2


# ---------------------------------------------------------------- springs


@lru_cache(maxsize=4096)
def omega_range(d: GDesign) -> tuple[float, float]:
    """Lowest and highest swing frequency the spring carriage can give, rad/s."""
    I = inertias(d)["total"]
    kg = gravity_stiffness(d)
    w_top = 2.0 * math.pi * d.f_spring_top
    k_s = (I * w_top**2 + kg) / (2.0 * d.r_spring_max**2)
    k_min = 2.0 * k_s * d.r_spring_min**2
    w_min = math.sqrt(max(k_min - kg, 0.0) / I)
    return max(w_min, 2.0 * math.pi * 0.1), w_top


@lru_cache(maxsize=4096)
def spring_rate(d: GDesign) -> float:
    I = inertias(d)["total"]
    w_top = 2.0 * math.pi * d.f_spring_top
    return (I * w_top**2 + gravity_stiffness(d)) / (2.0 * d.r_spring_max**2)


def carriage_radius(d: GDesign, w: float) -> float:
    k = inertias(d)["total"] * w**2 + gravity_stiffness(d)
    return math.sqrt(max(k, 0.0) / (2.0 * spring_rate(d)))


# ---------------------------------------------------------------- aerodynamics


def wind_power(d: GDesign, U: float) -> float:
    return 0.5 * RHO * U**3 * d.D * d.L


def cd_pitch(d: GDesign, beta: float) -> float:
    b = abs(beta)
    if b <= d.beta_cdmin:
        return d.Cd0 + (d.Cd_min - d.Cd0) * b / d.beta_cdmin
    if b >= d.beta_feather:
        return d.Cd_feather
    return d.Cd_min + (d.Cd_feather - d.Cd_min) * (b - d.beta_cdmin) / (d.beta_feather - d.beta_cdmin)


def cy_static(d: GDesign, beta: float) -> float:
    """Steady side-force coefficient at pitch beta (cubic fit; zero when feathered)."""
    if beta >= d.beta_feather - 1e-9:
        return 0.0
    return max(d.A1 * d.turb_factor * beta - d.A3 * beta**3, -0.5)


def a1_eff(d: GDesign, beta: float) -> float:
    return d.A1 * d.turb_factor - 3.0 * d.A3 * beta**2


def aero_coeffs(d: GDesign, U: float, beta: float) -> tuple[float, float]:
    """Harmonic-balance coefficients: aerodynamic power = a V^2 - b V^4 (V = peak hinge rate)."""
    k = span_factor(d)
    a = 0.25 * RHO * U * d.D * a1_eff(d, beta) * span_int(d, 2) * k
    b = 3.0 / 16.0 * RHO * d.D * d.A3 * span_int(d, 4) * k / U
    return a, b


def amplitude(a: float, b: float, c: float, T: float) -> float:
    """Stable swing rate V from (a - c/2) V - b V^3 - (2/pi) T = 0 (largest root), else 0."""
    A = a - c / 2.0
    if A <= 0.0 or b <= 0.0:
        return 0.0
    k = 2.0 * T / math.pi
    if k <= 0.0:
        return math.sqrt(A / b)
    p, q = -A / b, k / b
    if 4 * p**3 + 27 * q**2 >= 0.0:
        return 0.0
    m = 2.0 * math.sqrt(-p / 3.0)
    # largest real root of V^3 + p V + q = 0: m cos( acos( (3q/(2p)) sqrt(-3/p) ) / 3 )
    arg = max(-1.0, min(1.0, (3.0 * q / (2.0 * p)) * math.sqrt(-3.0 / p)))
    return m * math.cos(math.acos(arg) / 3.0)


def friction(d: GDesign, U: float, beta: float) -> tuple[float, float]:
    """Coulomb friction torque at the hinge (bushings, generator drag), N m."""
    G = gear_ratio(d)
    q = 0.5 * RHO * U**2
    drag = q * cd_pitch(d, beta) * d.D * d.L
    side = q * abs(cy_static(d, beta)) * d.D * d.L
    m_drag = drag * (d.neck + d.L / 2.0)
    weight = masses(d)["swinging"] * G0
    t_bush = d.bush_mu * (2.0 * m_drag / d.bush_span + weight + side) * d.axle_d / 2.0
    return t_bush + d.hinge_drag, d.gen_drag * G


# ---------------------------------------------------------------- operating point


def context(d: GDesign, U: float, beta: float) -> tuple:
    """Everything about wind U and pitch beta that does not depend on the generator load."""
    I = inertias(d)["total"]
    a, b = aero_coeffs(d, U, beta)
    t_bush, t_gen = friction(d, U, beta)
    q = 0.5 * RHO * U**2
    M0 = q * abs(cy_static(d, beta)) * d.D * span_factor(d) * span_int(d, 1)
    w_lo, w_top = omega_range(d)
    w_hi = min(w_top, 2.0 * math.pi * neck_mode_freq(d) / d.mode_margin,
               2.0 * math.pi * U / (d.Ustar_min * d.D))
    eff = d.belt_eff * d.conv_eff
    return (a, b, t_bush + t_gen, M0, I, w_lo, w_hi, math.radians(d.swing_design_deg),
            2.0 * d.zeta_struct * I, c_max(d), eff, t_bush, t_gen)


def omega_for(cx: tuple, V: float) -> tuple[float, float]:
    """Lowest swing frequency keeping swing + static lean within the design stroke: (omega, needed)."""
    M0, I, w_lo, w_hi, th = cx[3], cx[4], cx[5], cx[6], cx[7]
    if V <= 0.0:
        need = 0.0
    elif M0 > 1e-9:
        c = M0 / I
        need = 2.0 * c / (-V + math.sqrt(V * V + 4.0 * c * th))
    else:
        need = V / th
    w = max(need, w_lo)
    if w > w_hi:
        w = max(w_hi, w_lo)
    return w, need


def quick(cx: tuple, c_e: float) -> tuple[float, float, float, float]:
    """(V, omega, needed omega, electrical power) for generator damping c_e."""
    a, b, T, zI, cm, eff = cx[0], cx[1], cx[2], cx[8], cx[9], cx[10]
    w = cx[5]
    V = 0.0
    need = 0.0
    for _ in range(2):
        V = amplitude(a, b, zI * w + c_e, T)
        w, need = omega_for(cx, V)
    p_mech = 0.5 * c_e * V * V
    return V, w, need, p_mech * eff * max(1.0 - c_e / cm, 0.0)


def state(d: GDesign, U: float, beta: float, c_e: float, cx: tuple | None = None) -> dict:
    """Swing at wind U, pitch beta and generator damping c_e (N m s/rad at the hinge)."""
    cx = cx or context(d, U, beta)
    a, b, T, M0, I, w_lo, w_hi, th_d, zI, cm, eff, t_bush, t_gen = cx
    V, w, need, p_elec = quick(cx, c_e)
    G = gear_ratio(d)
    p_mech = 0.5 * c_e * V**2
    copper = 1.0 - c_e / cm if cm > 0 else 0.0
    k_net = I * w**2
    theta = V / w if w > 0 else 0.0
    lean = M0 / k_net if k_net > 0 else 0.0
    f = w / (2.0 * math.pi)
    pw = wind_power(d, U)
    return {
        "U": U, "beta": beta, "c_e": c_e, "c_s": zI * w, "V": V,
        "w": w, "f": f, "w_need": need, "w_hi": w_hi, "theta": theta, "lean": lean,
        "theta_deg": math.degrees(theta), "lean_deg": math.degrees(lean),
        "Ustar": U / (f * d.D) if f > 0 else math.inf,
        "alpha_top": V * r2(d) / U if U > 0 else 0.0,
        "a": a, "b": b, "T": T, "t_bush": t_bush, "t_gen": t_gen, "M0": M0,
        "p_wind": pw, "p_mech": p_mech, "p_elec": p_elec,
        "eta_mech": p_mech / pw if U > 0 else 0.0,
        "eta_elec": p_elec / pw if U > 0 else 0.0,
        "copper": copper, "R_total": G**2 * d.Ke**2 / c_e if c_e > 0 else math.inf,
        "emf_peak": d.Ke * G * V, "gen_heat": p_mech * d.belt_eff * (c_e / cm if cm > 0 else 1.0),
        "gen_rpm_peak": G * V * 60.0 / (2.0 * math.pi),
        "a_top": r2(d) * math.tan(theta), "top_accel_g": theta * w**2 * r2(d) / G0,
    }


def best_ce(d: GDesign, U: float, beta: float, cx: tuple | None = None) -> float:
    """Generator damping giving the most mechanical power at this pitch (golden section)."""
    cx = cx or context(d, U, beta)
    a = cx[0]
    if a <= 0:
        return 0.0

    def pm(c: float) -> float:
        return 0.5 * c * quick(cx, c)[0] ** 2

    lo, hi = 0.0, 2.0 * a
    g = (math.sqrt(5) - 1) / 2
    x1, x2 = hi - g * (hi - lo), lo + g * (hi - lo)
    f1, f2_ = pm(x1), pm(x2)
    for _ in range(26):
        if f1 < f2_:
            lo, x1, f1 = x1, x2, f2_
            x2 = lo + g * (hi - lo)
            f2_ = pm(x2)
        else:
            hi, x2, f2_ = x2, x1, f1
            x1 = hi - g * (hi - lo)
            f1 = pm(x1)
    return 0.5 * (lo + hi)


def ce_for_V(cx: tuple, V: float, w: float) -> float:
    """Generator damping that holds the swing rate at V (overdamped side)."""
    a, b, T, zI = cx[0], cx[1], cx[2], cx[8]
    if V <= 0:
        return math.inf
    return 2.0 * (a - b * V**2 - 2.0 * T / (math.pi * V)) - zI * w


SWINGING = ("generating", "limited")


def loads(d: GDesign, U: float, op: dict | None, mode: str) -> dict:
    """Structural and electrical loads at wind U. op None = parked (feathered when U is high)."""
    m = masses(d)
    I = inertias(d)
    q = 0.5 * RHO * U**2
    swinging = op is not None and mode in SWINGING
    beta = op["beta"] if swinging else d.beta_feather
    Cd = cd_pitch(d, beta)
    F = q * Cd * d.D * d.L
    side = q * cy_static(d, beta) * d.D * d.L if swinging else 0.0
    lever = d.neck + d.L / 2.0
    m_drag_hinge = F * lever
    m_side_hinge = abs(side) * lever
    th = op["theta"] if swinging else 0.0
    w = op["w"] if swinging else 0.0
    V = op["V"] if swinging else 0.0
    a, b = r1(d), r2(d)
    # neck root, swing plane: steady side force + inertial (in phase) and aerodynamic (quadrature) parts
    m_inert = I["above"] * th * w**2
    m_aero = (op["c_e"] + op["c_s"]) * V + 4.0 * op["T"] / math.pi if swinging else 0.0
    m_cyc = math.hypot(m_inert, m_aero)
    c = d.neck_od / 2.0
    In = neck_I(d)
    neck_peak = math.hypot(m_drag_hinge, m_side_hinge + m_cyc) * c / In
    neck_cyc = m_cyc * c / In
    # prism base
    mu_s = m["shell"] / d.L
    m_base_cyc = (mu_s * th * w**2 * ((b**3 - a**3) / 3.0 - a * (b**2 - a**2) / 2.0)
                  + m["plate_each"] * th * w**2 * b * (b - a))
    m_base = math.hypot(F * d.L / 2.0, abs(side) * d.L / 2.0 + m_base_cyc)
    skin = m_base / (4.0 / 3.0 * d.skin_t * d.D**2)
    panel = q * panel_moment_per_q(d) / d.panel_cap
    if d.plate_ratio > 1.0:
        wd = (m["plate_side"] - d.D) / 2.0
        plate = d.gust_CL * q * wd**2 / 2.0 / d.panel_cap
    else:
        plate = 0.0
    r_cg = (m["shell"] * (a + d.L / 2) + m["plate_each"] * (a + b) + m["spider"] * a
            + m["neck"] * d.neck / 2) / max(m["above"], 1e-9)
    f_inertial = m["above"] * th * w**2 * r_cg
    bushing = m_drag_hinge / d.bush_span + 0.5 * (m["swinging"] * G0 + f_inertial + abs(side))
    head_drag = q * (1.2 * d.head_area + 0.2 * d.vane_area)
    post_moment = F * (d.hub_height + lever) + head_drag * d.hub_height
    pitch_torque = d.CM_pitch * q * d.D**2 * d.L
    utils = {
        "neck": neck_peak / d.neck_allow,
        "neck fatigue": neck_cyc / d.neck_fatigue_allow,
        "skin": skin / d.skin_allow,
        "panels": panel,
        "end plates": plate,
        "hub": m_drag_hinge / d.M_hinge_max,
    }
    spring_N = 0.0
    if swinging:
        k_s = spring_rate(d)
        r_c = carriage_radius(d, w)
        spring_N = k_s * r_c * (th + op["lean"])
        utils.update({
            "stroke": (th + op["lean"]) / math.radians(d.swing_design_deg),
            "springs": spring_N / d.spring_force_max,
            "neck mode": d.mode_margin * op["f"] / neck_mode_freq(d),
            "quasi-steady": d.Ustar_min * op["f"] * d.D / U,
            "flow angle": op["alpha_top"] / d.alpha_cap,
            "voltage": op["emf_peak"] / d.V_max,
            "generator heat": op["gen_heat"] / d.gen_heat_max,
            "generator speed": op["gen_rpm_peak"] / d.gen_rpm_max,
            "generator load": op["c_e"] * d.R_margin / c_max(d),
        })
    # the frequency rule always uses the whole design stroke, so the stroke only governs when exceeded
    pick = {k: v for k, v in utils.items() if k != "stroke" or v > 1.0001}
    worst = max(pick, key=pick.get)
    return {
        "q": q, "drag": F, "side": side, "m_drag_hinge": m_drag_hinge, "m_inert": m_inert, "m_aero": m_aero,
        "neck_peak_MPa": neck_peak / 1e6, "neck_cyc_MPa": neck_cyc / 1e6, "skin_MPa": skin / 1e6,
        "panel_moment": q * panel_moment_per_q(d), "bushing_N": bushing, "post_moment": post_moment,
        "head_drag": head_drag, "pitch_torque": pitch_torque, "spring_N": spring_N,
        "top_accel_g": th * w**2 * b / G0, "utils": utils, "worst": worst, "worst_util": utils[worst],
    }


def operate(d: GDesign, U: float) -> dict:
    """Best operating point at wind U with every part within limits.

    Scans pitch from face-on upwards. At each pitch it tries the generator
    load that maximises power and heavier loads that hold the swing, flow
    angle or output down to a limit; it keeps the highest electrical output
    that respects every limit and the power rating.
    """
    out: dict = {"U": U, "op": None, "limit": "", "lo": None}
    if U <= 0.3:
        out["mode"] = "calm"
        return out
    if U > d.U_cut_out:
        out["mode"] = "feathered"
        out["limit"] = "cut-out"
        return out
    w_lo, w_top = omega_range(d)
    if w_lo > 2.0 * math.pi * U / (d.Ustar_min * d.D):
        out["mode"] = "idle"
        out["limit"] = "below quasi-steady range"
        return out
    best = None
    best_pe = -1.0
    first_limit = ""
    cm = c_max(d) / d.R_margin
    n = int(math.sqrt(max(d.A1 * d.turb_factor, 0.0) / (3.0 * d.A3)) / d.pitch_step) + 1
    for i in range(n + 1):
        beta = i * d.pitch_step
        cx = context(d, U, beta)
        ce0 = best_ce(d, U, beta, cx)
        V0, w0, need0, pe0 = quick(cx, ce0)
        if V0 <= 0.0:
            if i == 0:
                first_limit = "friction"
            break
        if pe0 < best_pe * 0.995:
            break
        cands = [ce0]
        if 0 < ce0 < cm:
            cands += [ce0 * (cm / ce0) ** (k / 6.0) for k in range(1, 7)]
            # loads that hold the flow angle, the stroke at the highest frequency, and the rating
            cands.append(ce_for_V(cx, d.alpha_cap * U / r2(d), w0))
            I, th, w_hi, M0 = cx[4], cx[7], cx[6], cx[3]
            lean = M0 / (I * w_hi**2) if w_hi > 0 else th
            if th > lean:
                cands.append(ce_for_V(cx, (th - lean) * w_hi * 0.999, w_hi))
            if pe0 > d.P_rated and quick(cx, cm)[3] < d.P_rated:
                lo_c, hi_c = ce0, cm
                for _ in range(30):
                    mid = 0.5 * (lo_c + hi_c)
                    if quick(cx, mid)[3] > d.P_rated:
                        lo_c = mid
                    else:
                        hi_c = mid
                cands.append(hi_c)
        for ce in cands:
            if not (ce > 0) or ce > cm or math.isinf(ce):
                continue
            V, w, need, pe = quick(cx, ce)
            if V <= 0:
                continue
            if not (i == 0 and ce == ce0) and (pe > d.P_rated * 1.0001 or pe < best_pe * 0.995):
                continue
            op = state(d, U, beta, ce, cx)
            lo = loads(d, U, op, "generating")
            if i == 0 and ce == ce0:
                first_limit = lo["worst"] if lo["worst_util"] > 1 else ("power rating" if pe > d.P_rated else "")
            if lo["worst_util"] > 1.0 or pe > d.P_rated * 1.0001:
                continue
            # at the rating many pitch/load pairs give the same output: prefer the lightest generator
            # load (pitch-regulated, lowest copper loss, furthest from losing the swing in a lull)
            at_rating = pe >= 0.995 * d.P_rated
            if (best is None or (pe > best_pe and not (at_rating and best_pe >= 0.995 * d.P_rated))
                    or (at_rating and best_pe >= 0.995 * d.P_rated and ce < best[0]["c_e"])):
                best, best_pe = (op, lo), max(pe, best_pe)
    if best is None:
        # too little wind to beat friction: wait face-on; otherwise feather to stay within limits
        out["mode"] = "idle" if first_limit == "friction" else "feathered"
        out["limit"] = first_limit or "no feasible point"
        return out
    op, lo = best
    out["op"], out["lo"] = op, lo
    if op["beta"] > 0 or op["p_elec"] < 0.99 * potential(d, U):
        out["mode"] = "limited"
        out["limit"] = "power rating" if op["p_elec"] >= 0.995 * d.P_rated else lo["worst"]
    else:
        out["mode"] = "generating"
    return out


def potential(d: GDesign, U: float) -> float:
    """Electrical output face-on at the best load if nothing limited it (not achievable at high wind)."""
    cx = context(d, U, 0.0)
    return quick(cx, best_ce(d, U, 0.0, cx))[3]


def survival(d: GDesign) -> tuple[float, str, dict]:
    """Highest wind each part survives feathered and braked."""
    ref = 10.0
    lo = loads(d, ref, None, "feathered")
    winds = {}
    for k in ("neck", "skin", "panels", "end plates", "hub"):
        u = lo["utils"][k]
        winds[k] = ref / math.sqrt(u) if u > 0 else 99.0
    k = min(winds, key=winds.get)
    return min(winds[k], 99.0), k, winds


def curve(d: GDesign, speeds) -> list[dict]:
    return [operate(d, U) for U in speeds]


def cut_in(d: GDesign) -> float:
    U = 0.5
    while U <= d.U_cut_out:
        st = operate(d, U)
        if st["mode"] in SWINGING and st["op"]["p_elec"] > 0.01:
            return U
        U = round(U + 0.1, 2)
    return math.nan


def generates_to(d: GDesign, start: float, step: float = 1.0) -> float:
    """Highest wind up to cut-out reached without a gap in output, starting from start."""
    U = start
    last = math.nan
    while True:
        st = operate(d, U)
        if st["mode"] in SWINGING and st["op"]["p_elec"] > 0.01:
            last = U
        else:
            break
        if U >= d.U_cut_out - 1e-9:
            break
        U = min(round(U + step, 3), d.U_cut_out)
    return last


def annual_energy(d: GDesign, mean_wind: float, step: float = 0.25, cache: dict | None = None) -> float:
    total = 0.0
    U = step / 2.0
    while U < d.U_cut_out:
        pdf = math.pi * U / (2 * mean_wind**2) * math.exp(-math.pi * U**2 / (4 * mean_wind**2))
        if cache is not None and U in cache:
            p = cache[U]
        else:
            st = operate(d, U)
            p = st["op"]["p_elec"] if st["mode"] in SWINGING else 0.0
            if cache is not None:
                cache[U] = p
        total += p * pdf * step
        U += step
    return total * d.avail * 8760.0 / 1000.0


def size_neck(d: GDesign) -> GDesign:
    """Lightest standard neck tube that survives U_storm feathered and whose bending
    mode clears the top of the spring range by the margin."""
    for od, idd in NECK_TUBES:
        t = replace(d, neck_od=od, neck_id=idd)
        if survival(t)[2]["neck"] >= d.U_storm and neck_mode_freq(t) >= d.mode_margin * d.f_spring_top:
            return t
    od, idd = NECK_TUBES[-1]
    return replace(d, neck_od=od, neck_id=idd)


def constraint_failures(d: GDesign, gen_to: float | None = None) -> list[str]:
    fails = []
    if d.L / d.D < d.AR_min - 1e-9:
        fails.append("aspect ratio")
    if d.neck + d.L > d.max_total_height:
        fails.append("height")
    if survival(d)[0] < d.U_storm:
        fails.append("survival")
    if neck_mode_freq(d) < d.mode_margin * d.f_spring_top:
        fails.append("spring range")
    g = generates_to(d, 10.0) if gen_to is None else gen_to
    if not (g >= d.U_cut_out - 1e-9):
        fails.append("stops before cut-out")
    return fails


# ---------------------------------------------------------------- output


def f2(x: float, nd: int = 2) -> str:
    return f"{x:.{nd}f}"


def pct(u: float) -> str:
    return f"{100*u:.0f}%"


ENVELOPE_SPEEDS = [1, 2, 3, 4, 4.5, 5, 6, 7, 8, 10, 12, 15, 17.5, 20, 25, 30, 35, 40, 45]
CURVE_SPEEDS = [1, 2, 3, 4, 4.5, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17.5, 20, 25, 30, 35, 40]
U_KEYS = ["neck", "neck fatigue", "skin", "panels", "end plates", "hub", "stroke", "springs", "neck mode",
          "quasi-steady", "flow angle", "voltage", "generator heat", "generator speed", "generator load"]


def envelope_rows(d: GDesign, speeds) -> list[dict]:
    rows = []
    for U in speeds:
        st = operate(d, U)
        op = st["op"]
        sw = st["mode"] in SWINGING
        lo = st["lo"] if sw else loads(d, U, None, st["mode"])
        rows.append({
            "U": U, "mode": st["mode"], "limit": st["limit"],
            "pitch_deg": math.degrees(op["beta"]) if sw else (45.0 if st["mode"] == "feathered" else 0.0),
            "f_Hz": op["f"] if sw else 0.0, "Ustar": op["Ustar"] if sw else 0.0,
            "carriage_mm": 1000 * carriage_radius(d, op["w"]) if sw else 0.0,
            "swing_deg": op["theta_deg"] if sw else 0.0, "lean_deg": op["lean_deg"] if sw else 0.0,
            "top_swing_mm": 1000 * op["a_top"] if sw else 0.0,
            "p_mech": op["p_mech"] if sw else 0.0, "p_elec": op["p_elec"] if sw else 0.0,
            "eta_elec": op["eta_elec"] if sw else 0.0,
            "gen_load": op["c_e"] if sw else 0.0, "copper": op["copper"] if sw else 0.0,
            "emf": op["emf_peak"] if sw else 0.0, "heat": op["gen_heat"] if sw else 0.0,
            "rpm": op["gen_rpm_peak"] if sw else 0.0,
            "drag": lo["drag"], "hinge_moment": lo["m_drag_hinge"], "post_moment": lo["post_moment"],
            "spring_N": lo["spring_N"], "top_g": lo["top_accel_g"],
            **{"u_" + k: lo["utils"].get(k, 0.0) for k in U_KEYS},
            "worst": lo["worst"], "worst_util": lo["worst_util"],
        })
    return rows


def envelope_table(d: GDesign, speeds) -> list[str]:
    o = ["| Wind (m/s) | Mode | Pitch (°) | Swing f (Hz) | U/(fD) | Swing (±°) | Lean (°) | Elec (W) | "
         "Gen load (N m s/rad) | EMF (V) | Gen heat (W) | Neck | Fatigue | Skin | Panels | Hub | Stroke | "
         "Springs | Worst |",
         "|" + "---|" * 19]
    for r in envelope_rows(d, speeds):
        sw = r["mode"] in SWINGING
        o.append(
            f"| {r['U']:g} | {r['mode']}{(' (' + r['limit'] + ')') if r['limit'] else ''} | {f2(r['pitch_deg'],1)} | "
            f"{f2(r['f_Hz']) if sw else '-'} | {f2(r['Ustar'],0) if sw else '-'} | {f2(r['swing_deg'],1)} | "
            f"{f2(r['lean_deg'],1)} | {f2(r['p_elec'],2)} | {f2(r['gen_load'],2)} | {f2(r['emf'],0)} | "
            f"{f2(r['heat'],1)} | {pct(r['u_neck'])} | {pct(r['u_neck fatigue'])} | {pct(r['u_skin'])} | "
            f"{pct(r['u_panels'])} | {pct(r['u_hub'])} | {pct(r['u_stroke'])} | {pct(r['u_springs'])} | "
            f"{r['worst']} {pct(r['worst_util'])}{' **FAIL**' if r['worst_util'] > 1.0001 else ''} |"
        )
    return o


def write_rows_csv(rows: list[dict], path: str) -> None:
    with open(path, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        for r in rows:
            w.writerow({k: (round(v, 4) if isinstance(v, float) else v) for k, v in r.items()})


def viv_curves(speeds) -> dict[str, list[float]]:
    """Lantern 250-B and -C (VIV) electrical power, kept generating within limits."""
    import lantern_calc as lc
    out = {}
    for name in ("B", "C"):
        d = replace(lc.design_from(argparse.Namespace(config=name, shell=None)), keep_generating=1)
        vals = []
        for U in speeds:
            st = lc.operate(d, U)
            vals.append(st["op"]["p_elec"] if st["mode"] in lc.SWINGING and st["op"] else 0.0)
        out[name] = vals
    return out


def curve_rows(d: GDesign, speeds, compare: bool = False) -> list[dict]:
    viv = viv_curves(speeds) if compare else {}
    rows = []
    for i, U in enumerate(speeds):
        st = operate(d, U)
        sw = st["mode"] in SWINGING
        if sw:
            note = ("limited by " + st["limit"]) if st["mode"] == "limited" else "unconstrained"
        else:
            note = st["mode"] + (f" ({st['limit']})" if st["limit"] else "")
        r = {
            "U": U, "wind_W": wind_power(d, U), "potential_W": potential(d, U) if U > 0.3 else 0.0,
            "elec_W": st["op"]["p_elec"] if sw else 0.0, "elec_low_W": d.derate * st["op"]["p_elec"] if sw else 0.0,
            "mode": st["mode"], "note": note,
            "pitch_deg": math.degrees(st["op"]["beta"]) if sw else (45.0 if st["mode"] == "feathered" else 0.0),
            "swing_deg": st["op"]["theta_deg"] if sw else 0.0, "f_Hz": st["op"]["f"] if sw else 0.0,
        }
        for k, v in viv.items():
            r[f"viv_{k}_W"] = v[i]
        rows.append(r)
    return rows


def summary_lines(d: GDesign) -> list[str]:
    surv, part, winds = survival(d)
    ci = cut_in(d)
    gto = generates_to(d, max(ci, 1.0) if ci == ci else 10.0, 0.5)
    w_lo, w_top = omega_range(d)
    rated_at = next((U / 4 for U in range(4, 4 * int(d.U_cut_out) + 1)
                     if (lambda s: s["mode"] in SWINGING and s["op"]["p_elec"] >= 0.995 * d.P_rated)(operate(d, U / 4))),
                    math.nan)
    return [
        f"- Cut-in (starts with kick-start and makes >10 mW): {f2(ci,1)} m/s; generates without a gap to "
        f"**{f2(gto,1)} m/s**; feathers above {d.U_cut_out:g} m/s",
        f"- Rated {d.P_rated:g} W electrical, reached at {f2(rated_at,2)} m/s; pitch holds it above that",
        f"- Survives feathered (45°) and braked up to **{f2(surv,1)} m/s**, limited by the {part}. "
        f"Requirement {d.U_storm:g} m/s. Per part: " + ", ".join(f"{k} {f2(v,0)}" for k, v in winds.items()),
        f"- Swing frequency range {f2(w_lo/(2*math.pi),2)}-{f2(w_top/(2*math.pi),2)} Hz (spring carriage "
        f"{d.r_spring_min*1000:.0f}-{d.r_spring_max*1000:.0f} mm); neck-and-prism bending mode "
        f"{f2(neck_mode_freq(d),1)} Hz",
        f"- Quasi-steady theory trusted from U/(fD) = {d.Ustar_min:g}; vortex-shedding resonance would be at "
        f"U/(fD) = {f2(1/d.St,1)}",
    ]


def curve_summary(d: GDesign) -> list[str]:
    o = summary_lines(d)
    o.append("- Yearly energy, central case (kWh): " + "; ".join(
        f"{V} m/s site {f2(annual_energy(d, V),1)}" for V in (3.5, 4.5, 5.5, 6.5)))
    return o


def curve_table(d: GDesign, speeds, compare: bool = False) -> list[str]:
    head = ("| Wind (m/s) | Wind through prism (W) | Potential face-on (W) | Electrical (W) | Low case (W) | "
            "What governs | Pitch (°) | Swing (±°) | Swing f (Hz) |")
    sep = "|" + "---|" * 9
    if compare:
        head += " VIV 250-B kept generating (W) | VIV 250-C kept generating (W) |"
        sep += "---|---|"
    o = [head, sep]
    for r in curve_rows(d, speeds, compare):
        line = (f"| {r['U']:g} | {r['wind_W']:,.1f} | {r['potential_W']:,.2f} | {r['elec_W']:.2f} | "
                f"{r['elec_low_W']:.2f} | {r['note']} | {f2(r['pitch_deg'],1)} | {f2(r['swing_deg'],1)} | "
                f"{f2(r['f_Hz']) if r['f_Hz'] else '-'} |")
        if compare:
            line += f" {r['viv_B_W']:.2f} | {r['viv_C_W']:.2f} |"
        o.append(line)
    return o


def curve_report(d: GDesign, step: float, top: float, start: float, compare: bool) -> str:
    n = int(round((top - start) / step))
    speeds = [round(start + i * step, 3) for i in range(n + 1)]
    o = [f"# Lantern G power curve, {start:g}-{top:g} m/s\n",
         "Electrical: the most the machine delivers with every part within its limits and the output at or "
         "below its rating, pitching the prism and loading the generator as needed. Potential face-on: the "
         "model's output with no pitch and no limits (not achievable at high wind). Low case = "
         f"{d.derate} x electrical.\n"]
    o += curve_summary(d)
    o.append("")
    o += curve_table(d, speeds, compare)
    return "\n".join(o)


def describe(d: GDesign) -> str:
    m = masses(d)
    return (f"{d.section} prism {d.D*1000:.0f} mm x {d.L*1000:.0f} mm, neck {d.neck*1000:.0f} mm "
            f"({d.neck_od*1000:.0f}x{d.neck_id*1000:.0f} mm carbon), end plates {m['plate_side']*1000:.0f} mm square, "
            f"panels {d.shell_areal:.3f} kg/m^2 (capacity {d.panel_cap:g} N m/m), generator {d.gen}, "
            f"{d.pulley_teeth}-tooth pulley ({f2(gear_ratio(d),1)}:1), springs to {d.f_spring_top:g} Hz, "
            f"rated {d.P_rated:g} W, survival requirement {d.U_storm:g} m/s")


def report(d: GDesign) -> str:
    o: list[str] = []
    m = masses(d)
    I = inertias(d)
    G = gear_ratio(d)
    o.append("# Lantern G calculator report\n")
    o.append(describe(d) + "\n")
    fails = constraint_failures(d)
    o.append("Constraint check: " + ("all pass" if not fails else "FAILS " + ", ".join(fails)) + "\n")
    o.append("## Operating summary\n")
    o += curve_summary(d)
    o.append("")

    o.append("## Masses (kg)\n\n| Part | Mass |\n|---|---|")
    o.append(f"| Prism panels, {m['n_bulk']} bulkheads, corner tapes | {f2(m['shell'],3)} |")
    o.append(f"| End plates, each ({m['plate_side']*1000:.0f} mm square) | {f2(m['plate_each'],3)} |")
    o.append(f"| Bottom spider | {f2(m['spider'],3)} |")
    o.append(f"| Neck tube | {f2(m['neck'],3)} |")
    o.append(f"| Hub, axle, carriage, belt arc, pitch drive | {f2(m['hub'],3)} |")
    o.append(f"| **Total swinging mass** | **{f2(m['swinging'],3)}** |\n")
    o.append("## Inertia about the hinge (kg m^2)\n\n| Part | Inertia |\n|---|---|")
    for k in ("shell", "plates", "spider", "neck", "hub", "generator"):
        o.append(f"| {k} | {f2(I[k],4)} |")
    o.append(f"| Air moving with the prism | {f2(I['added'],4)} |")
    o.append(f"| **Total** | **{f2(I['total'],4)}** |")
    o.append(f"| Mass ratio (structural / displaced air) | {f2(I['mass_ratio'],2)} |\n")
    a, b = aero_coeffs(d, 10.0, 0.0)
    eta_max = d.A1**2 * span_int(d, 2) ** 2 / (6 * d.A3 * span_int(d, 4) * d.L) * span_factor(d)
    o.append(
        f"- Gear ratio {f2(G,1)}:1 ({d.arc_radius*1000:.0f} mm arc to {d.pulley_teeth}-tooth GT2 pulley); "
        f"generator damping at the hinge up to {f2(c_max(d),1)} N m s/rad (terminals shorted)\n"
        f"- Span factor after end losses {f2(span_factor(d),3)}; frictionless capture ceiling "
        f"A1² I2² / (6 A3 I4 L) = {f2(100*eta_max,2)} % of the wind through the prism\n"
        f"- Gravity (destabilising) stiffness {f2(gravity_stiffness(d),1)} N m/rad; two springs of "
        f"{f2(spring_rate(d)/1000,2)} N/mm each\n"
        f"- Panel bending per unit dynamic pressure {f2(panel_moment_per_q(d)*1000,2)} x 10^-3 m^2 "
        f"(bulkheads every {f2(d.L/(m['n_bulk']+1),3)} m)\n"
    )

    o.append("## Wind envelope\n")
    o.append("Utilisation = load / allowable (over 100% fails). The controller keeps every one at or under 100% "
             "while generating; above cut-out the prism is feathered (45°) and braked. Stroke = swing plus "
             "steady lean against the design stroke; quasi-steady = how close the swing frequency is to the "
             "highest the galloping model is trusted at.\n")
    o += envelope_table(d, ENVELOPE_SPEEDS)
    o.append("")
    o.append("## Power from 1 to 40 m/s\n")
    o += curve_table(d, CURVE_SPEEDS)
    o.append("")

    o.append(f"## Structure at the survival requirement ({d.U_storm:g} m/s, feathered and braked)\n")
    lo = loads(d, d.U_storm, None, "feathered")
    o.append(f"- Drag {f2(lo['drag'],0)} N; moment at the hinge {f2(lo['m_drag_hinge'],0)} N m "
             f"(hub built for {d.M_hinge_max:g})")
    o.append(f"- Neck stress {f2(lo['neck_peak_MPa'],0)} MPa (allowable {d.neck_allow/1e6:.0f}); skin stress at "
             f"prism base {f2(lo['skin_MPa'],1)} MPa (allowable {d.skin_allow/1e6:.0f})")
    o.append(f"- Panel bending {f2(lo['panel_moment'],1)} N m/m against {d.panel_cap:g}; end-plate gust "
             f"utilisation {pct(lo['utils']['end plates'])}")
    o.append(f"- Bushing load {f2(lo['bushing_N'],0)} N each; pitch-drive torque about {f2(lo['pitch_torque'],1)} N m")
    o.append(f"- Post base moment with the hinge at {d.hub_height:g} m: {f2(lo['post_moment'],0)} N m")
    st = operate(d, d.U_cut_out)
    if st["mode"] in SWINGING:
        l2 = st["lo"]
        o.append(f"- Generating at {d.U_cut_out:g} m/s: drag {f2(l2['drag'],0)} N, hinge moment "
                 f"{f2(l2['m_drag_hinge'],0)} N m, post base {f2(l2['post_moment'],0)} N m, "
                 f"spring force {f2(l2['spring_N'],0)} N")
    o.append("")
    o.append("## Annual energy (very rough)\n")
    o.append(f"Rayleigh wind at hub height, the power curve above, {int(100*d.avail)} % of the model output "
             f"achieved (yaw lag, gusts, restarts). Low case = {d.derate} x central.\n")
    o.append("| Site mean wind | Low (kWh/yr) | Central (kWh/yr) |\n|---|---|---|")
    for V in (3.5, 4.5, 5.5, 6.5, 7.5):
        E = annual_energy(d, V)
        o.append(f"| {V} m/s | {f2(d.derate*E,1)} | {f2(E,1)} |")
    o.append("")
    return "\n".join(o)


def envelope_report(d: GDesign, step: float, top: float, start: float) -> str:
    n = int(round((top - start) / step))
    speeds = [round(start + i * step, 3) for i in range(n + 1)]
    o = [f"# Lantern G wind envelope, {start:g}-{top:g} m/s\n", describe(d) + "\n"]
    o += summary_lines(d)
    o.append("")
    o += envelope_table(d, speeds)
    return "\n".join(o)


# ---------------------------------------------------------------- sweep

GRID_COLUMNS = [
    "rank", "passes", "failed_limits", "D_mm", "neck_mm", "plate_ratio", "plate_mm", "shell", "shell_kg_m2",
    "generator", "pulley_teeth", "gear_ratio", "f_spring_top_Hz", "neck_tube", "total_height_m",
    "annual_kWh", "annual_low_kWh", "site_mean_wind", "annual_6_kWh",
    "p_elec_4p5_W", "p_elec_7_W", "p_elec_10_W", "p_elec_15_W", "p_elec_20_W", "p_elec_40_W",
    "min_p_20_40_W", "cut_in_ms", "generates_to_ms", "rated_W", "hub_Nm", "survival_ms", "survival_limit",
    "swinging_mass_kg", "inertia_total_kgm2", "f_min_Hz", "neck_mode_Hz", "spring_rate_N_mm",
]


def evaluate(args_tuple) -> dict:
    """Build and score one grid point (top-level so multiprocessing can call it)."""
    base, D, nk, pr, sh, t, ft, gen, hub, site, neck_auto, hold = args_tuple
    d = replace(base, D=D, neck=nk, plate_ratio=pr, pulley_teeth=t, f_spring_top=ft, gen=gen,
                M_hinge_max=hub, hub_mass=base.hub_mass * (hub / 500.0) ** 0.5,
                **SHELLS[sh], **GENERATORS[gen])
    if neck_auto:
        d = size_neck(d)
    cache: dict = {}

    def pe(U: float) -> float:
        st = operate(d, U)
        return st["op"]["p_elec"] if st["mode"] in SWINGING else 0.0

    pts = {U: pe(U) for U in (4.5, 7.0)}
    high = [(U, pe(U)) for U in frange(10.0, d.U_cut_out, 2.5)]
    pts.update(high)
    gto = math.nan
    for U, p in high:
        if p <= 0.01:
            break
        gto = U
    fails = constraint_failures(d, gen_to=gto)
    if hold:
        reached = [U for U, p in high if p >= 0.95 * d.P_rated]
        if not reached or reached[0] > 25.0 or any(p < 0.95 * d.P_rated for U, p in high if U >= reached[0]):
            fails.append("does not hold rating")
    ann = annual_energy(d, site, step=0.5, cache=cache)
    ann6 = annual_energy(d, 6.0, step=0.5, cache=cache)
    surv, part, _ = survival(d)
    w_lo, _ = omega_range(d)
    m = masses(d)
    return {
        "passes": "yes" if not fails else "no", "failed_limits": "; ".join(fails),
        "D_mm": round(D * 1000), "neck_mm": round(nk * 1000), "plate_ratio": round(pr, 2),
        "plate_mm": round(m["plate_side"] * 1000), "shell": sh, "shell_kg_m2": d.shell_areal,
        "generator": gen, "pulley_teeth": t, "gear_ratio": round(gear_ratio(d), 2), "f_spring_top_Hz": ft,
        "neck_tube": f"{d.neck_od*1000:.0f}x{d.neck_id*1000:.0f}", "total_height_m": round(d.neck + d.L, 3),
        "annual_kWh": round(ann, 3), "annual_low_kWh": round(d.derate * ann, 3), "site_mean_wind": site,
        "annual_6_kWh": round(ann6, 3),
        "p_elec_4p5_W": round(pts[4.5], 3), "p_elec_7_W": round(pts[7.0], 3), "p_elec_10_W": round(pts[10.0], 3),
        "p_elec_15_W": round(pts[15.0], 3), "p_elec_20_W": round(pts[20.0], 3), "p_elec_40_W": round(pts[40.0], 3),
        "min_p_20_40_W": round(min(p for U, p in high if U >= 20.0), 3), "hub_Nm": hub,
        "cut_in_ms": round(cut_in(d), 1) if pts[4.5] > 0 or pts[7.0] > 0 else "",
        "generates_to_ms": gto, "rated_W": d.P_rated, "survival_ms": round(surv, 1), "survival_limit": part,
        "swinging_mass_kg": round(m["swinging"], 3), "inertia_total_kgm2": round(inertias(d)["total"], 4),
        "f_min_Hz": round(w_lo / (2 * math.pi), 3), "neck_mode_Hz": round(neck_mode_freq(d), 2),
        "spring_rate_N_mm": round(spring_rate(d) / 1000, 2),
    }


def sweep(base: GDesign, args: argparse.Namespace) -> str:
    Ds = frange(args.D_min, args.D_max, args.D_step)
    necks = frange(args.neck_min, args.neck_max, args.neck_step)
    plates = frange(args.plate_min, args.plate_max, args.plate_step)
    shells = args.shells.split(",")
    teeth = [int(t) for t in args.teeth.split(",")]
    ftops = [float(x) for x in args.ftop.split(",")]
    gens = args.gens.split(",")
    hubs = [float(x) for x in args.hubs.split(",")]
    jobs = [(base, D, nk, pr, sh, t, ft, g, hb, args.site, args.neck_auto, args.hold_rated)
            for D, nk, pr, sh, t, ft, g, hb in itertools.product(Ds, necks, plates, shells, teeth, ftops, gens, hubs)]
    if args.workers > 1:
        import multiprocessing as mp
        with mp.Pool(args.workers) as pool:
            rows = pool.map(evaluate, jobs, chunksize=4)
    else:
        rows = [evaluate(j) for j in jobs]
    key = "annual_kWh" if args.objective == "annual" else "p_elec_" + args.wind_key + "_W"
    passing = sorted((r for r in rows if r["passes"] == "yes"), key=lambda r: r[key], reverse=True)
    for i, r in enumerate(passing, 1):
        r["rank"] = i
    if args.csv:
        with open(args.csv, "w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=GRID_COLUMNS)
            w.writeheader()
            for r in rows:
                w.writerow({c: r.get(c, "") for c in GRID_COLUMNS})
    rejected: dict[str, int] = {}
    for r in rows:
        for f in filter(None, r["failed_limits"].split("; ")):
            rejected[f] = rejected.get(f, 0) + 1
    what = (f"central-case annual energy at a {args.site} m/s site" if args.objective == "annual"
            else f"electrical power at {args.wind_key.replace('p', '.')} m/s")
    o = [f"# Lantern G sweep: ranked by {what}; must generate to {base.U_cut_out:g} m/s and survive "
         f"{base.U_storm:g} m/s feathered\n"]
    o.append(f"{len(rows)} combinations: D {Ds[0]}-{Ds[-1]} m, neck {necks[0]}-{necks[-1]} m, plate ratio "
             f"{plates[0]}-{plates[-1]}, panels {', '.join(shells)}, pulley teeth {teeth}, spring top {ftops} Hz, "
             f"generators {', '.join(gens)}, hubs {hubs} N m, rated {base.P_rated:g} W"
             f"{' (must reach it by 25 m/s and hold it to cut-out)' if args.hold_rated else ''}"
             f"{', neck tube sized automatically' if args.neck_auto else ''}.  ")
    o.append(f"{len(passing)} pass every limit. Rejected (a design can fail several): " +
             (", ".join(f"{k} {v}" for k, v in sorted(rejected.items())) or "none") + "\n")
    if not passing:
        return "\n".join(o)
    o.append("| Rank | Annual (kWh, site) | Annual 6 m/s site | D | Neck | Neck tube | Plates | Panels | Gen | "
             "Teeth | Spring top (Hz) | Hub (N m) | 4.5 m/s (W) | 10 m/s (W) | 20 m/s (W) | 40 m/s (W) | Cut-in | Survives |")
    o.append("|" + "---|" * 18)
    for r in passing[: args.top]:
        o.append(f"| {r['rank']} | {r['annual_kWh']} | {r['annual_6_kWh']} | {r['D_mm']} | {r['neck_mm']} | "
                 f"{r['neck_tube']} | {r['plate_ratio']} | {r['shell']} | {r['generator']} | {r['pulley_teeth']} | {r['hub_Nm']:g} | "
                 f"{r['f_spring_top_Hz']:g} | {r['p_elec_4p5_W']} | {r['p_elec_10_W']} | {r['p_elec_20_W']} | "
                 f"{r['p_elec_40_W']} | {r['cut_in_ms']} | {r['survival_ms']} ({r['survival_limit']}) |")
    return "\n".join(o)


# ---------------------------------------------------------------- CLI


def add_design_args(p: argparse.ArgumentParser) -> None:
    p.add_argument("--config", choices=sorted(CONFIGS), default="G")
    p.add_argument("--shell", choices=sorted(SHELLS), default=None, help="panel construction preset")
    p.add_argument("--generator", choices=sorted(GENERATORS), default=None, help="generator preset")
    p.add_argument("--section-preset", dest="section_preset", choices=sorted(SECTIONS), default=None,
                   help="cross-section coefficients (only 'square' is well established)")
    for f in fields(GDesign):
        if f.name in ("section", "gen"):
            continue
        p.add_argument(f"--{f.name}", type=float, default=None, help=f"default {f.default}")


def design_from(args: argparse.Namespace) -> GDesign:
    over = dict(CONFIGS[getattr(args, "config", "G")])
    if getattr(args, "shell", None):
        over.update(SHELLS[args.shell])
    if getattr(args, "generator", None):
        over.update(GENERATORS[args.generator], gen=args.generator)
    if getattr(args, "section_preset", None):
        over.update(SECTIONS[args.section_preset], section=args.section_preset)
    for f in fields(GDesign):
        v = getattr(args, f.name, None)
        if v is not None and f.name not in ("section", "gen"):
            over[f.name] = int(v) if f.type in ("int", int) else v
    return replace(GDesign(), **over)


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = p.add_subparsers(dest="cmd")
    pr = sub.add_parser("report", help="full report for one design (default)")
    add_design_args(pr)
    pe = sub.add_parser("envelope", help="mode, pitch, power and every limit at each wind speed")
    add_design_args(pe)
    pc = sub.add_parser("curve", help="electrical power from 1 to 40 m/s")
    add_design_args(pc)
    pc.add_argument("--compare", action="store_true", help="add Lantern 250-B and -C (VIV) kept generating")
    for q in (pe, pc):
        q.add_argument("--from", dest="start", type=float, default=1.0)
        q.add_argument("--to", dest="top", type=float, default=40.0)
        q.add_argument("--step", type=float, default=1.0)
        q.add_argument("--csv", default=None, help="also write the rows to this CSV file")
    ps = sub.add_parser("sweep", help="grid search for the best design that generates to 40 m/s")
    add_design_args(ps)
    ps.add_argument("--objective", choices=("annual", "power"), default="annual")
    ps.add_argument("--wind-key", dest="wind_key", default="10", help="for --objective power: 4p5, 7, 10, 15, 20, 40")
    ps.add_argument("--site", type=float, default=4.5)
    ps.add_argument("--D-min", dest="D_min", type=float, default=0.20)
    ps.add_argument("--D-max", dest="D_max", type=float, default=0.33)
    ps.add_argument("--D-step", dest="D_step", type=float, default=0.025)
    ps.add_argument("--neck-min", dest="neck_min", type=float, default=0.0)
    ps.add_argument("--neck-max", dest="neck_max", type=float, default=0.8)
    ps.add_argument("--neck-step", dest="neck_step", type=float, default=0.2)
    ps.add_argument("--plate-min", dest="plate_min", type=float, default=1.0)
    ps.add_argument("--plate-max", dest="plate_max", type=float, default=2.0)
    ps.add_argument("--plate-step", dest="plate_step", type=float, default=0.5)
    ps.add_argument("--shells", default=",".join(SHELLS))
    ps.add_argument("--teeth", default="10,12,16,20")
    ps.add_argument("--ftop", default="2,3,4,6", help="spring-range tops to try, Hz")
    ps.add_argument("--gens", default=",".join(GENERATORS))
    ps.add_argument("--hubs", default="500", help="hub moment ratings to try, N m")
    ps.add_argument("--no-hold-rated", dest="hold_rated", action="store_false",
                    help="do not require the rating to be reached by 25 m/s and held to cut-out")
    ps.add_argument("--no-neck-auto", dest="neck_auto", action="store_false")
    ps.add_argument("--workers", type=int, default=os.cpu_count() or 1)
    ps.add_argument("--top", type=int, default=15)
    ps.add_argument("--csv", default=None, help="also write every grid point to this CSV file")
    args = p.parse_args()
    d = design_from(args) if args.cmd else GDesign()
    if args.cmd == "sweep":
        print(sweep(d, args))
    elif args.cmd in ("curve", "envelope"):
        n = int(round((args.top - args.start) / args.step))
        speeds = [round(args.start + i * args.step, 3) for i in range(n + 1)]
        if args.cmd == "curve":
            if args.csv:
                write_rows_csv(curve_rows(d, speeds, args.compare), args.csv)
            print(curve_report(d, args.step, args.top, args.start, args.compare))
        else:
            if args.csv:
                write_rows_csv(envelope_rows(d, speeds), args.csv)
            print(envelope_report(d, args.step, args.top, args.start))
    else:
        print(report(d))


if __name__ == "__main__":
    main()
