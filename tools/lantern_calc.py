#!/usr/bin/env python3
"""Lantern design calculator and optimiser.

Reproduces every number in designs/lantern-250/ from the parameters below,
and can search a grid of dimensions for the highest-output design.

    python3 tools/lantern_calc.py                  # full report for Lantern 250-B
    python3 tools/lantern_calc.py report --config A
    python3 tools/lantern_calc.py report --D 0.2   # report for a 200 mm tube
    python3 tools/lantern_calc.py sweep            # grid search, ranked by power
    python3 tools/lantern_calc.py sweep --objective annual --site 4.5

All results are engineering estimates from simple models (see
designs/lantern-250/physics.md). None of them has been measured, and an
optimiser will happily exploit any weakness in the model, so treat the
"best" design as a starting point for testing, not a guarantee.
Standard library only.
"""

from __future__ import annotations

import argparse
import itertools
import math
from dataclasses import dataclass, fields, replace

RHO = 1.225  # air density, kg/m^3
NU = 1.5e-5  # kinematic viscosity of air, m^2/s
G0 = 9.81  # gravity, m/s^2

# Shell options, areal mass in kg/m^2 (foam at ~37 kg/m^3 plus ~50 g/m^2
# of glass tissue and epoxy, which carries the storm bending load)
SHELLS = {
    "xps2-glass": 0.124,
    "xps3-glass": 0.161,
    "xps5-glass": 0.235,
}


@dataclass(frozen=True)
class Design:
    """Defaults are Lantern 250-B, the recommended configuration."""

    # Geometry
    D: float = 0.25  # tube diameter, m
    L: float = 1.00  # tube length (the 1 m height limit), m
    neck: float = 0.80  # hinge axis to bottom of tube, m

    # Tube shell
    shell_areal: float = 0.161  # kg/m^2 (see SHELLS)
    rings_mass: float = 0.012  # four internal foam rings, kg
    seams_mass: float = 0.008  # tape and glue, kg

    # End discs: ratio 1.0 means no discs
    disc_ratio: float = 2.0  # disc diameter / tube diameter
    disc_areal: float = 0.16  # 3 mm XPS + carbon-strip stiffeners, kg/m^2
    end_loss_D: float = 0.5  # span lost per bare end, in diameters (assumed)
    disc_full_ratio: float = 2.0  # disc ratio that removes the end loss (assumed)

    # Neck and hub
    spider_mass: float = 0.015  # bottom-ring-to-neck spider, kg
    neck_od: float = 0.030  # carbon neck tube outside diameter, m
    neck_id: float = 0.028  # carbon neck tube inside diameter, m
    carbon_density: float = 1550.0  # kg/m^3
    carbon_E: float = 100e9  # Pa
    hub_mass: float = 0.15  # hub, axle, spring carriage, belt arc, kg
    hub_radius: float = 0.07  # effective radius of hub mass, m

    # Flow
    St: float = 0.2  # Strouhal number
    Ca: float = 1.0  # added-mass coefficient
    Cd_viv: float = 2.0  # mean drag coefficient while oscillating (for bushing loads)

    # Drive: GT2 belt from an arc on the hub to a pulley on the generator
    arc_radius: float = 0.100  # m
    pulley_teeth: int = 12
    belt_pitch: float = 0.002  # m
    belt_eff: float = 0.97

    # Generator: 5208-size brushless gimbal motor (check your datasheet)
    gen_rotor_J: float = 6e-5  # kg m^2 (assumed)
    Ke: float = 0.38  # V s/rad = N m/A
    R_coil: float = 12.0  # ohm
    gen_drag: float = 0.004  # bearing + iron-loss drag torque, N m (assumed)
    conv_eff: float = 0.85  # rectifier + MPPT converter

    # Losses
    zeta_struct: float = 0.003  # foam/epoxy hysteresis, springs, air (assumed)
    bush_span: float = 0.15  # distance between hinge bushings, m
    axle_d: float = 0.012  # hinge axle diameter, m
    bush_mu: float = 0.15  # polymer bushing friction coefficient

    # Tuning
    Ustar: float = 5.5  # target U/(f_n D) at the tuned wind speed
    U_tune_min: float = 3.0  # m/s
    U_tune_max: float = 7.0  # m/s
    r_spring_max: float = 0.140  # spring carriage furthest from hinge, m

    # Structure and limits
    U_storm: float = 25.0  # survival gust, m/s
    Cd_storm: float = 1.2
    skin_t: float = 0.05e-3  # effective glass-skin thickness, m
    skin_allow: float = 40e6  # allowable skin stress, Pa
    M_hinge_max: float = 150.0  # survival moment the hinge and neck are built for, N m
    Re_max: float = 1.2e5  # highest Re at U_tune_max (tested range of the evidence)
    R_margin: float = 1.2  # circuit resistance must exceed this x coil resistance
    max_total_height: float = 2.0  # tube + neck limit, m

    # Planning
    derate: float = 0.5  # low case = derate x model (turbulence, detuning)
    lock_factor: float = 0.5  # share of in-band time actually locked on
    duty: float = 0.30  # share of the year spent swinging


# Named configurations. B is the default; A is the version first worked out
# in conversation (with its structural corrections applied).
CONFIGS = {
    "A": dict(neck=0.40, disc_ratio=1.6, pulley_teeth=16, neck_od=0.025, neck_id=0.023,
              bush_span=0.10, axle_d=0.010),
    "B": {},
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
    m["swinging"] = shell + 2 * disc + d.spider_mass + m["neck"] + d.hub_mass
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


# ---------------------------------------------------------------- tuning


def f_natural(d: Design, U: float) -> float:
    """Still-air natural frequency to tune for (added mass included), Hz."""
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


def evaluate(d: Design, U: float) -> dict[str, float]:
    """Locked-on operating point at wind speed U with the optimum generator load.

    Amplitude from the Skop-Griffin relation with the hinged mode shape;
    friction converted to an equivalent damping ratio; generator damping set
    to the value that maximises extracted power. See physics.md.
    """
    I = inertias(d)
    Is, ms = I["structural"], I["mass_ratio"]
    w = 2.0 * math.pi * d.St * U / d.D  # oscillation (shedding) frequency
    a = 0.43 * 2.0 * math.pi**3 * d.St**2 * ms  # S_G = a * zeta
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
    for _ in range(60):
        c_fric = 4.0 * t_fric / (math.pi * theta * w)
        zp = d.zeta_struct + c_fric / (2.0 * Is * w)
        ze = (1.0 + a * zp) / (5.7 * a)
        a_top = d.D * 1.29 * gam / (1.0 + a * (zp + ze)) ** 3.35
        new = math.atan(a_top / top)
        if abs(new - theta) < 1e-7:
            theta = new
            break
        theta = 0.5 * (theta + new)

    span_factor = effective_length(d) / d.L
    p_mech = ze * Is * w**3 * theta**2 * span_factor
    c_e = 2.0 * ze * Is * w
    r_total = G**2 * d.Ke**2 / c_e
    copper = 1.0 - d.R_coil / r_total
    p_elec = p_mech * d.belt_eff * max(copper, 0.0) * d.conv_eff
    pw = wind_power(d, U)
    return {
        "U": U,
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
        "emf_peak": d.Ke * G * theta * w,
        "gen_rpm_peak": G * theta * w * 60.0 / (2.0 * math.pi),
        "gen_swing_deg": math.degrees(theta) * G,
        "top_accel_g": theta * w**2 * top / G0,
    }


def annual_energy(d: Design, mean_wind: float, n: int = 40) -> float:
    """Central-case kWh/yr for a Rayleigh wind distribution at hub height."""
    lo, hi = 0.8 * d.U_tune_min, 1.2 * d.U_tune_max
    du = (hi - lo) / n
    total = 0.0
    for i in range(n):
        U = lo + (i + 0.5) * du
        pdf = math.pi * U / (2 * mean_wind**2) * math.exp(-math.pi * U**2 / (4 * mean_wind**2))
        total += evaluate(d, U)["p_elec"] * pdf * du
    return total * d.lock_factor * 8760.0 / 1000.0


# ---------------------------------------------------------------- structure


def structure(d: Design) -> dict[str, float]:
    F = 0.5 * RHO * d.U_storm**2 * d.Cd_storm * d.D * d.L
    m_base = F * d.L / 2.0
    m_hinge = F * (d.neck + d.L / 2.0)
    R = d.D / 2.0
    I_neck = math.pi / 64.0 * (d.neck_od**4 - d.neck_id**4)
    rod_I = math.pi * 0.004**4 / 64.0
    rod_force = m_hinge / (1.5 * 0.10)
    return {
        "storm_drag": F,
        "m_base": m_base,
        "m_hinge": m_hinge,
        "skin_stress": m_base / (math.pi * R**2 * d.skin_t),
        "foam_only_stress": m_base / (math.pi * R**2 * 0.003),
        "neck_stress": m_hinge * (d.neck_od / 2.0) / I_neck if d.neck > 0 else 0.0,
        "rod_buckle": math.pi**2 * d.carbon_E * rod_I / max(d.neck, 1e-6) ** 2,
        "rod_force_storm": rod_force,
        "rod_force_10": rod_force * (10.0 / d.U_storm) ** 2,
        "bush_storm": m_hinge / d.bush_span,
    }


def constraint_failures(d: Design) -> list[str]:
    fails = []
    if d.U_tune_max * d.D / NU > d.Re_max:
        fails.append("Reynolds")
    s = structure(d)
    if s["m_hinge"] > d.M_hinge_max:
        fails.append("hinge moment")
    if s["skin_stress"] > d.skin_allow:
        fails.append("skin stress")
    if d.neck + d.L > d.max_total_height:
        fails.append("height")
    if evaluate(d, 4.5)["R_total"] < d.R_margin * d.R_coil:
        fails.append("generator too weak")
    return fails


# ---------------------------------------------------------------- output


def f2(x: float, nd: int = 2) -> str:
    return f"{x:.{nd}f}"


def report(d: Design) -> str:
    o: list[str] = []
    m = masses(d)
    I = inertias(d)
    G = gear_ratio(d)
    o.append("# Lantern calculator report\n")
    o.append(
        f"Tube {d.D*1000:.0f} mm x {d.L*1000:.0f} mm, neck {d.neck*1000:.0f} mm, "
        f"end discs {m['disc_dia']*1000:.0f} mm, shell {d.shell_areal:.3f} kg/m^2, "
        f"height/diameter {d.L/d.D:.1f}\n"
    )
    fails = constraint_failures(d)
    o.append("Constraint check: " + ("all pass" if not fails else "FAILS " + ", ".join(fails)) + "\n")

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
    ks = spring_rate(d)
    o.append(f"Two opposing springs, each {f2(ks/1000,2)} N/mm.\n")
    o.append("| Wind (m/s) | Tune f_n (Hz) | Stiffness (N m/rad) | Carriage below hinge (mm) |\n|---|---|---|---|")
    for U in (3.0, 4.0, 4.5, 5.0, 6.0, 7.0):
        o.append(f"| {U} | {f2(f_natural(d,U))} | {f2(k_required(d,U),1)} | {f2(1000*carriage_radius(d,U),1)} |")
    slope = 1000 * (carriage_radius(d, 6.0) - carriage_radius(d, 4.0)) / 2.0
    o.append(f"\nCarriage moves about {f2(slope,1)} mm per 1 m/s between 4 and 6 m/s.\n")

    o.append("## Operating points (locked on, model central case)\n")
    o.append(
        "| Wind | Re | Swing f (Hz) | Wind power (W) | Mech (W) | Elec (W) | Elec low case (W) | "
        "Mech eff | Swing (deg) | Peak torque (N m) | Gen zeta | Parasitic zeta | "
        "Circuit R (ohm) | Copper eff | EMF peak (V) | Gen peak rpm | Top accel (g) |"
    )
    o.append("|" + "---|" * 17)
    for U in (3.0, 4.5, 6.0, 7.0):
        e = evaluate(d, U)
        o.append(
            f"| {U} | {e['Re']:.0f} | {f2(e['f_osc'])} | {f2(e['p_wind'],1)} | {f2(e['p_mech'],2)} | "
            f"{f2(e['p_elec'],2)} | {f2(d.derate*e['p_elec'],2)} | {f2(100*e['eta_mech'],1)} % | "
            f"{f2(e['theta_deg'],1)} | {f2(e['torque_peak'])} | {f2(e['zeta_e'],3)} | {f2(e['zeta_par'],4)} | "
            f"{f2(e['R_total'],0)} | {f2(100*e['copper'],0)} % | {f2(e['emf_peak'],1)} | "
            f"{f2(e['gen_rpm_peak'],0)} | {f2(e['top_accel_g'],1)} |"
        )
    e = evaluate(d, 4.5)
    o.append(
        f"\nAt 4.5 m/s: tube swings +/-{e['a_bot']*1000:.0f} mm at the bottom, +/-{e['a_mid']*1000:.0f} mm "
        f"mid-height, +/-{e['a_top']*1000:.0f} mm at the top; generator swings +/-{e['gen_swing_deg']:.0f} deg. "
        f"Friction: bushings {f2(e['t_bush'],3)} N m, generator drag {f2(e['t_gen'],3)} N m (at the hinge).\n"
    )

    o.append("## Structure\n")
    s = structure(d)
    o.append(f"- Survival drag at {d.U_storm:.0f} m/s: {f2(s['storm_drag'],0)} N")
    o.append(f"- Bending moment at tube base {f2(s['m_base'],0)} N m, at hinge {f2(s['m_hinge'],0)} N m")
    o.append(
        f"- Glass-skin stress at tube base {f2(s['skin_stress']/1e6,1)} MPa "
        f"(bare foam would see {f2(s['foam_only_stress']/1e6,2)} MPa, about its strength)"
    )
    o.append(f"- Neck {d.neck_od*1000:.0f}x{d.neck_id*1000:.0f} mm carbon tube stress {f2(s['neck_stress']/1e6,0)} MPa")
    o.append(
        f"- Three 4 mm carbon rods (first chat version) would buckle at {f2(s['rod_buckle'],0)} N; "
        f"their load is {f2(s['rod_force_10'],0)} N at 10 m/s and {f2(s['rod_force_storm'],0)} N at {d.U_storm:.0f} m/s"
    )
    o.append(f"- Hinge bushing load at {d.U_storm:.0f} m/s: {f2(s['bush_storm'],0)} N each")
    cyc = f_natural(d, 4.5) * d.duty * 365.25 * 24 * 3600
    o.append(f"- Swing cycles per year at {int(100*d.duty)} % duty: {cyc:.1e}\n")

    o.append("## Annual energy (very rough)\n")
    o.append(
        f"Rayleigh wind at hub height, tuning band {d.U_tune_min}-{d.U_tune_max} m/s +/-20 %, "
        f"{int(100*d.lock_factor)} % of in-band time locked on. Low case = {d.derate} x central.\n"
    )
    o.append("| Site mean wind | Low (kWh/yr) | Central (kWh/yr) |\n|---|---|---|")
    for V in (3.5, 4.5, 5.5):
        E = annual_energy(d, V)
        o.append(f"| {V} m/s | {f2(d.derate*E,1)} | {f2(E,1)} |")
    o.append("")
    return "\n".join(o)


def frange(lo: float, hi: float, step: float) -> list[float]:
    n = int(round((hi - lo) / step))
    return [round(lo + i * step, 6) for i in range(n + 1)]


def sweep(base: Design, args: argparse.Namespace) -> str:
    Ds = frange(args.D_min, args.D_max, args.D_step)
    necks = frange(args.neck_min, args.neck_max, args.neck_step)
    discs = frange(args.disc_min, args.disc_max, args.disc_step)
    shells = args.shells.split(",")
    teeth = [int(t) for t in args.teeth.split(",")]

    def score(d: Design) -> float:
        if args.objective == "annual":
            return annual_energy(d, args.site, n=24)
        return evaluate(d, args.wind)["p_elec"]

    results = []
    rejected: dict[str, int] = {}
    total = 0
    for D, nk, dr, sh, t in itertools.product(Ds, necks, discs, shells, teeth):
        total += 1
        d = replace(base, D=D, neck=nk, disc_ratio=dr, shell_areal=SHELLS[sh], pulley_teeth=t)
        fails = constraint_failures(d)
        if fails:
            for f in fails:
                rejected[f] = rejected.get(f, 0) + 1
            continue
        results.append((score(d), d, sh))
    results.sort(key=lambda r: r[0], reverse=True)

    unit = "kWh/yr" if args.objective == "annual" else "W"
    what = (
        f"central-case annual energy at a {args.site} m/s site"
        if args.objective == "annual"
        else f"electrical power at {args.wind} m/s"
    )
    o = [f"# Lantern sweep: ranked by {what}\n"]
    o.append(
        f"{total} combinations: D {Ds[0]}-{Ds[-1]} m, neck {necks[0]}-{necks[-1]} m, "
        f"disc ratio {discs[0]}-{discs[-1]}, shells {', '.join(shells)}, pulley teeth {teeth}.  "
    )
    o.append(f"{len(results)} pass all limits. Rejected (a design can fail several): " +
             (", ".join(f"{k} {v}" for k, v in sorted(rejected.items())) or "none") + "\n")
    if not results:
        return "\n".join(o)

    o.append(f"| Rank | Score ({unit}) | D (mm) | Neck (mm) | Disc ratio | Shell | Teeth | Gear | "
             "Mass ratio | Mech eff 4.5 | Swing 4.5 (deg) | Re at U_max |")
    o.append("|" + "---|" * 12)
    for i, (sc, d, sh) in enumerate(results[: args.top], 1):
        e = evaluate(d, 4.5)
        o.append(
            f"| {i} | {f2(sc,2)} | {d.D*1000:.0f} | {d.neck*1000:.0f} | {f2(d.disc_ratio,1)} | {sh} | "
            f"{d.pulley_teeth} | {f2(gear_ratio(d),1)} | {f2(inertias(d)['mass_ratio'],2)} | "
            f"{f2(100*e['eta_mech'],1)} % | {f2(e['theta_deg'],1)} | {d.U_tune_max*d.D/NU:.0f} |"
        )

    best_score, best, best_shell = results[0]
    o.append("\n## Sensitivity around the best design (one variable at a time)\n")
    o.append("| Variable | Value | Score | vs best |\n|---|---|---|---|")
    probes = [
        ("D (mm)", "D", Ds, 1000),
        ("Neck (mm)", "neck", necks, 1000),
        ("Disc ratio", "disc_ratio", discs, 1),
        ("Pulley teeth", "pulley_teeth", teeth, 1),
    ]
    for label, attr, values, scale in probes:
        for v in values[:: max(1, len(values) // 6)]:
            d = replace(best, **{attr: v})
            fails = constraint_failures(d)
            sc = score(d)
            note = f"{100*(sc/best_score-1):+.0f} %" + (f" (fails {', '.join(fails)})" if fails else "")
            o.append(f"| {label} | {v*scale:g} | {f2(sc,2)} | {note} |")
    for sh in shells:
        d = replace(best, shell_areal=SHELLS[sh])
        sc = score(d)
        o.append(f"| Shell | {sh} | {f2(sc,2)} | {100*(sc/best_score-1):+.0f} % |")
    o.append(f"\nBest: shell {best_shell}. Full report for it follows.\n")
    o.append(report(best))
    return "\n".join(o)


def add_design_args(p: argparse.ArgumentParser) -> None:
    p.add_argument("--config", choices=sorted(CONFIGS), default="B",
                   help="named starting configuration (default B)")
    for f in fields(Design):
        p.add_argument(f"--{f.name}", type=float, default=None, help=f"default {f.default}")


def design_from(args: argparse.Namespace) -> Design:
    over = dict(CONFIGS[getattr(args, "config", "B")])
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
    ps = sub.add_parser("sweep", help="grid search for the highest-output design")
    add_design_args(ps)
    ps.add_argument("--objective", choices=("power", "annual"), default="power")
    ps.add_argument("--wind", type=float, default=4.5, help="wind speed for --objective power")
    ps.add_argument("--site", type=float, default=4.5, help="site mean wind for --objective annual")
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
    ps.add_argument("--teeth", default="12,16,20,24,30,36")
    ps.add_argument("--top", type=int, default=15)
    args = p.parse_args()
    d = design_from(args) if args.cmd else Design()
    if args.cmd == "sweep":
        print(sweep(d, args))
    else:
        print(report(d))


if __name__ == "__main__":
    main()
