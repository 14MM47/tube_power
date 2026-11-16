#!/usr/bin/env python3
"""Check tools/galloping_calc.py's harmonic balance against a time-step simulation.

The calculator finds the steady swing of the hinged prism by averaging the
galloping force over a cycle (harmonic balance). This script instead
integrates the equation of motion directly, with the quasi-steady side force
evaluated along the span at every step, Coulomb friction and the same
spring and generator load. It then compares swing rate, swing amplitude,
lean and generator power with the calculator at a few operating points.

    python3 tools/galloping_timestep_check.py

Standard library only. Takes about ten seconds.
"""

from __future__ import annotations

import argparse
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import galloping_calc as g  # noqa: E402


def simulate(d: g.GDesign, U: float, op: dict, t_end: float = 60.0, dt: float = 1e-3, n_strips: int = 40) -> dict:
    """Integrate I θ'' + c θ' + T sign(θ') + k θ = M_aero(θ') for the calculator's operating point."""
    I = g.inertias(d)["total"]
    k = I * op["w"] ** 2
    c = op["c_s"] + op["c_e"]
    T = op["T"]
    beta = op["beta"]
    span = g.span_factor(d)
    r1, r2 = g.r1(d), g.r2(d)
    dr = (r2 - r1) / n_strips
    rs = [r1 + (i + 0.5) * dr for i in range(n_strips)]
    q = 0.5 * g.RHO * U**2

    def cy(a: float) -> float:
        return (d.A1 * d.turb_factor) * a - d.A3 * a**3

    def accel(th: float, td: float) -> float:
        m_aero = sum(q * d.D * cy(beta + td * r / U) * r * dr for r in rs) * span
        fric = math.copysign(T, td) if abs(td) > 1e-6 else 0.0
        return (m_aero - c * td - fric - k * th) / I

    th, td, t = 0.15, 0.0, 0.0
    v_max, e_gen, t_avg, th_hi, th_lo = 0.0, 0.0, 0.0, -9.0, 9.0
    while t < t_end:
        k1 = (td, accel(th, td))
        k2 = (td + 0.5 * dt * k1[1], accel(th + 0.5 * dt * k1[0], td + 0.5 * dt * k1[1]))
        k3 = (td + 0.5 * dt * k2[1], accel(th + 0.5 * dt * k2[0], td + 0.5 * dt * k2[1]))
        k4 = (td + dt * k3[1], accel(th + dt * k3[0], td + dt * k3[1]))
        th += dt / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0])
        td += dt / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])
        t += dt
        if t > t_end - 15.0:
            v_max = max(v_max, abs(td))
            e_gen += op["c_e"] * td * td * dt
            t_avg += dt
            th_hi, th_lo = max(th_hi, th), min(th_lo, th)
    return {"V": v_max, "p_mech": e_gen / t_avg, "swing_deg": math.degrees((th_hi - th_lo) / 2),
            "lean_deg": math.degrees((th_hi + th_lo) / 2)}


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--quick", action="store_true", help="shorter runs, coarser span")
    args = p.parse_args()
    ns = lambda c: argparse.Namespace(config=c, shell=None, generator=None, section_preset=None, belt_preset=None)
    cases = [("330-G", "G", 10.0), ("330-G", "G", 30.0), ("330-GH", "GH", 20.0), ("330-GH", "GH", 40.0)]
    print("| Design | Wind (m/s) | Pitch (°) | Swing rate V: calculator / simulated (rad/s) | "
          "Generator power: calculator / simulated (W) | Swing: calculator / simulated (±°) | "
          "Lean: calculator / simulated (°) |")
    print("|---|---|---|---|---|---|---|")
    for name, cfg, U in cases:
        d = g.design_from(ns(cfg))
        st = g.operate(d, U)
        op = st["op"]
        sim = simulate(d, U, op, t_end=30.0 if args.quick else 60.0, n_strips=20 if args.quick else 40)
        print(f"| {name} | {U:g} | {math.degrees(op['beta']):.1f} | {op['V']:.3f} / {sim['V']:.3f} | "
              f"{op['p_mech']:.2f} / {sim['p_mech']:.2f} | {op['theta_deg']:.2f} / {sim['swing_deg']:.2f} | "
              f"{op['lean_deg']:.2f} / {sim['lean_deg']:.2f} |")


if __name__ == "__main__":
    main()
