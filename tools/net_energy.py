#!/usr/bin/env python3
"""Yearly NET energy of Lantern 330-G after the controller's own draw.

The calculator's yearly energy (tools/galloping_calc.py, annual_energy) is the
generator's electrical output only. This script recomputes it from the
published power curve (designs/lantern-330-g/calculator-output/curve-330G.csv)
and subtracts what the controller itself draws:

- a RUNNING draw while generating (MCU awake, encoders, gate drivers, pitch
  and carriage loops): the machine only generates in winds where the credited
  output exceeds this draw (start/park on net power), and is parked otherwise;
- an IDLE draw while parked (MCU in Stop mode, woken by anemometer pulses;
  or, for comparison, a power-to-engage pitch clutch held through idle).

Method, the same as the calculator: Rayleigh wind at hub height with the
given mean, 0.25 m/s bins (bin midpoints, curve interpolated linearly between
its 0.5 m/s points), 80 % of the model output credited ("avail"), cut-out at
40 m/s (feathered and parked above). The running draw is not derated.

Standard library only. Examples::

    python3 tools/net_energy.py
    python3 tools/net_energy.py --sites 4.5,6.5 --run 0.2,0.5,1,2 --idle 0.004
    python3 tools/net_energy.py --sites 4.5 --run 0.2 --idle 2      # clutch held through idle
"""
from __future__ import annotations

import argparse
import csv
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CURVE = ROOT / "designs" / "lantern-330-g" / "calculator-output" / "curve-330G.csv"


def load_curve(path: Path = CURVE) -> list[tuple[float, float]]:
    with open(path, newline="") as f:
        return [(float(r["U"]), float(r["elec_W"])) for r in csv.DictReader(f)]


def power_at(curve, u: float) -> float:
    """Electrical output (W) at wind u, linear between the curve's points; 0 below the first."""
    if u <= curve[0][0]:
        return 0.0
    for (u0, p0), (u1, p1) in zip(curve, curve[1:]):
        if u0 <= u <= u1:
            return p0 + (u - u0) / (u1 - u0) * (p1 - p0)
    return curve[-1][1]


def rayleigh(u: float, mean: float) -> float:
    return math.pi * u / (2 * mean**2) * math.exp(-math.pi * u**2 / (4 * mean**2))


def yearly(curve, mean: float, run_w: float = 0.0, idle_w: float = 0.0, *,
           avail: float = 0.8, step: float = 0.25, cut_out: float = 40.0) -> dict:
    """Net kWh/yr and the share of the year generating, for one site and one pair of draws."""
    e_gen = e_run = e_idle = 0.0
    t_gen = 0.0
    u = step / 2.0
    while u < cut_out:
        w = rayleigh(u, mean) * step
        p = avail * power_at(curve, u)
        if p - run_w > 0.0:                     # start/park on net power
            e_gen += p * w
            e_run += run_w * w
            t_gen += w
        else:
            e_idle += idle_w * w
        u += step
    # winds above cut-out: feathered and parked
    above = math.exp(-math.pi * cut_out**2 / (4 * mean**2))
    e_idle += idle_w * above
    k = 8760.0 / 1000.0
    return {"gross_kWh": e_gen * k, "run_kWh": e_run * k, "idle_kWh": e_idle * k,
            "net_kWh": (e_gen - e_run - e_idle) * k, "generating_share": t_gen}


def break_even(curve, run_w: float, avail: float = 0.8) -> float | None:
    """Lowest wind (m/s, to 0.05) at which the credited output exceeds the running draw."""
    u = 0.0
    while u <= 40.0:
        if avail * power_at(curve, u) > run_w:
            return round(u, 2)
        u += 0.05
    return None


def _floats(s: str) -> list[float]:
    return [float(x) for x in s.split(",") if x.strip()]


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--sites", default="4.5,6.5", help="site mean winds, m/s (default 4.5,6.5)")
    ap.add_argument("--run", default="0,0.2,0.5,1,2", help="running draws while generating, W")
    ap.add_argument("--idle", default="0,0.004,2", help="idle draws while parked, W "
                    "(0.004: MCU in Stop mode; 2: a pitch clutch held through idle)")
    ap.add_argument("--avail", type=float, default=0.8, help="share of the model output credited (default 0.8)")
    ap.add_argument("--curve", default=str(CURVE))
    a = ap.parse_args(argv)
    curve = load_curve(Path(a.curve))
    sites, runs, idles = _floats(a.sites), _floats(a.run), _floats(a.idle)

    print(f"Lantern 330-G net yearly energy (kWh/yr) from {Path(a.curve).name}; Rayleigh, "
          f"{int(round(100 * a.avail))} % credited, 0.25 m/s bins, cut-out 40 m/s.")
    print("Generates only where the credited output exceeds the running draw; idle draw applies otherwise.\n")
    head = "| Site mean | Running draw | Break-even wind | Generating | " + \
        " | ".join(f"idle {i:g} W" for i in idles) + " |"
    print(head)
    print("|" + "---|" * (4 + len(idles)))
    for m in sites:
        for r in runs:
            cells = []
            share = None
            for i in idles:
                y = yearly(curve, m, r, i, avail=a.avail)
                share = y["generating_share"]
                cells.append(f"{y['net_kWh']:.1f}")
            be = break_even(curve, r, a.avail) if r > 0 else None
            print(f"| {m:g} m/s | {r:g} W | {'-' if be is None else f'{be:.2f} m/s'} | "
                  f"{100 * share:.0f} % of the year | " + " | ".join(cells) + " |")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
