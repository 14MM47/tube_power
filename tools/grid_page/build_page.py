#!/usr/bin/env python3
"""Build the Lantern design-grid page from the repository's calculators and grid CSVs.

    python3 tools/grid_page/build_page.py            # writes build/grid-page/
    python3 -m http.server -d build/grid-page 8000   # then open http://localhost:8000/lantern-grid.html

The page shows electrical power from 1 to 40 m/s for the vortex-shedding
configurations (Lantern 250-A, B, C), the galloping versions (330-G, 330-GH)
and the best design in each Lantern 250 grid, then every point of the four
Lantern 250 optimisation grids. The fine 25 m/s grid and the power curves are
inlined into lantern-grid.html; the other three grids load from JSON files
next to it. Standard library only.
"""
import argparse
import csv
import json
import os
import sys
from dataclasses import replace

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(REPO, "tools"))
import lantern_calc as lc  # noqa: E402
import galloping_calc as gc  # noqa: E402

# ---------------------------------------------------------------- grid JSON

FAIL_BITS = {"Reynolds": 1, "survival": 2, "operating loads": 4, "height": 8, "generator too weak": 16}
SHELLS = ["xps2-single", "xps3-single", "xps3-sandwich", "xps5-sandwich", "xps5-storm"]
LIMITS = ["neck", "skin", "wall", "discs", "hub"]
NECKS = ["25x23", "30x28", "35x32", "40x37", "50x47"]
KEYS = ("D", "N", "R", "S", "T", "F", "P", "A", "E", "M", "W", "G", "Re", "Sv", "Sl", "Ci", "Nk",
        "Sp", "V", "H", "Q", "Ms", "Fa", "Rt", "Rpm")

def build(src, dst):
    """One grid CSV to compact column-array JSON."""
    cols = {k: [] for k in KEYS}
    with open(src) as fh:
        for r in csv.DictReader(fh):
            fails = 0
            for name in filter(None, (s.strip() for s in r["failed_limits"].split(";"))):
                fails |= FAIL_BITS[name]
            add = lambda k, v: cols[k].append(v)
            add("D", int(r["D_mm"])); add("N", int(r["neck_mm"])); add("R", round(float(r["disc_ratio"]) * 10))
            add("S", SHELLS.index(r["shell"])); add("T", int(r["pulley_teeth"])); add("F", fails)
            add("P", round(float(r["p_elec_4p5_W"]) * 1000)); add("A", round(float(r["annual_kWh"]) * 100))
            add("E", round(float(r["eta_mech_4p5"]) * 1000)); add("M", round(float(r["mass_ratio"]) * 100))
            add("W", round(float(r["swing_deg_4p5"]) * 10)); add("G", round(float(r["top_accel_4p5_g"]) * 10))
            add("Re", round(float(r["Re_at_Umax"]) / 100)); add("Sv", round(float(r["survival_ms"]) * 10))
            add("Sl", LIMITS.index(r["survival_limit"]))
            ci = r["cut_in_ms"]; add("Ci", round(float(ci) * 10) if ci not in ("", "nan") else 0)
            add("Nk", NECKS.index(r["neck_tube"])); add("Sp", round(float(r["spring_rate_N_mm"]) * 10))
            add("V", round(float(r["emf_peak_4p5_V"]) * 10)); add("H", round(float(r["storm_hinge_moment_Nm"])))
            add("Q", round(float(r["peak_torque_4p5_Nm"]) * 100)); add("Ms", round(float(r["swinging_mass_kg"]) * 1000))
            add("Fa", round(float(r["max_neck_fatigue_util"]) * 100)); add("Rt", round(float(r["circuit_R_4p5_ohm"])))
            add("Rpm", int(r["gen_peak_rpm_4p5"]))
    with open(dst, "w") as fh:
        json.dump({"n": len(cols["D"]), "cols": cols}, fh, separators=(",", ":"))
    print(dst, len(cols["D"]))


# ---------------------------------------------------------------- curve helpers

GRID = os.path.join(REPO, "designs", "lantern-250", "calculator-output", "grid") + os.sep
SPEEDS = [round(0.5 * i, 1) for i in range(1, 81)]
NECK_DIMS = {f"{od*1000:.0f}x{idd*1000:.0f}": (od, idd) for od, idd in lc.NECK_TUBES}
SHELL_TXT = {"xps2-single": "2 mm foam, outer skin", "xps3-single": "3 mm foam, outer skin",
             "xps3-sandwich": "3 mm sandwich shell", "xps5-sandwich": "5 mm sandwich shell", "xps5-storm": "5 mm storm shell"}
notes = []

def note_idx(s):
    if s not in notes:
        notes.append(s)
    return notes.index(s)

def describe(d, shell):
    od, idd = d.neck_od, d.neck_id
    discs = "no end discs" if d.disc_ratio <= 1 else f"{d.disc_ratio:.1f}× discs"
    return (f"{d.D*1000:.0f} mm tube, {d.neck*1000:.0f} mm neck ({od*1000:.0f} × {idd*1000:.0f} mm), {discs}, "
            f"{SHELL_TXT[shell]}, {d.pulley_teeth}-tooth pulley; survives {lc.survival(d)[0]:.1f} m/s")

def from_grid(name, base_cfg):
    rows = list(csv.DictReader(open(GRID + name + ".csv")))
    r = min((x for x in rows if x["passes"] == "yes"), key=lambda x: int(x["rank"]))
    od, idd = NECK_DIMS[r["neck_tube"]]
    d = replace(lc.Design(), **lc.CONFIGS[base_cfg])
    d = replace(d, D=int(r["D_mm"]) / 1000, neck=int(r["neck_mm"]) / 1000, disc_ratio=float(r["disc_ratio"]),
                pulley_teeth=int(r["pulley_teeth"]), neck_od=od, neck_id=idd, **lc.SHELLS[r["shell"]])
    return d, r["shell"]

def curve(id_, name, d, shell, short):
    rows = lc.curve_rows(d, SPEEDS)
    lim = replace(d, keep_generating=1)
    rated = replace(d, keep_generating=0)
    fine = lc.curve_rows(d, [round(0.5 + 0.25 * i, 2) for i in range(159)])
    lim_on = [r["U"] for r in fine if r["within_limits_W"] > 0.01]
    pk = max(fine, key=lambda r: r["within_limits_W"])
    after = [r for r in fine if r["U"] > max(lim_on) and r["within_limits_W"] <= 0.01]
    stop = after[0]["within_limits_note"] if after else "n/a"
    stop = {"braked (generator heat)": "the generator's heat limit", "braked (drag crisis)": "the drag crisis (Re above 200,000)",
            "braked (neck mode)": "the neck's bending mode", "braked (tuning range)": "the end of the tuning range"}.get(stop, ("the " + stop[len("limited by "):] + " limit") if stop.startswith("limited by ") else stop)
    des_from, des_to = lc.cut_in(rated), lc.brake_speed(rated)
    return {
        "id": id_, "name": name, "short": short, "D": round(d.D * 1000),
        "desc": describe(d, shell),
        "wind": [round(r["wind_W"], 3) for r in rows],
        "pot": [round(r["potential_W"], 3) for r in rows],
        "lim": [round(r["within_limits_W"], 3) for r in rows],
        "des": [round(r["as_designed_W"], 3) for r in rows],
        "note": [note_idx(r["within_limits_note"]) for r in rows],
        "summary": {
            "des_from": des_from, "des_to": des_to, "des_peak": max(r["as_designed_W"] for r in rows),
            "lim_from": min(lim_on), "lim_to": max(lim_on), "lim_peak": pk["within_limits_W"], "lim_peak_u": pk["U"],
            "lim_stop": stop,
            "annual_des": lc.annual_energy(rated, 4.5), "annual_lim": lc.annual_energy(lim, 4.5),
        },
    }

GSHELL = {"xps5": "5 mm glass-faced foam panels", "xps6-storm": "6 mm glass-faced foam panels",
          "xps10-storm": "10 mm glass-faced foam panels", "corflute4": "4 mm twin-wall polypropylene panels"}


GEN_TXT = {"8108": "8108 outrunner", "6374": "6374 outrunner", "hub500": "e-bike hub motor", "5208": "5208 gimbal motor"}


def gcurve(id_, name, d, short):
    rows = gc.curve_rows(d, SPEEDS)
    surv, part, _ = gc.survival(d)
    ci = gc.cut_in(d)
    capped = d.P_rated < 1e4
    rated_at = next(U / 4 for U in range(4, 161) if
                    (lambda s: s["mode"] in gc.SWINGING and s["op"]["p_elec"] >= 0.995 * d.P_rated)(gc.operate(d, U / 4))) if capped else 0
    mid = [r["elec_W"] for r in rows if 15 <= r["U"] <= 40 and float(r["U"]).is_integer()]
    m = gc.masses(d)
    desc = (f"{d.D*1000:.0f} mm square prism, {d.neck*1000:.0f} mm neck ({d.neck_od*1000:.0f} × {d.neck_id*1000:.0f} mm), "
            f"{m['plate_side']*1000:.0f} mm end plates, {GSHELL.get(gc_shell(d), 'custom panels')}, {GEN_TXT.get(d.gen, d.gen + ' generator')}, "
            f"{d.belt} belt {d.arc_radius*1000:.0f} mm arc to {d.pulley_teeth} teeth ({gc.gear_ratio(d):.1f}:1), swing ±{d.swing_design_deg:g}°, "
            + (f"rated {d.P_rated:g} W" if capped else "no power cap, face-on or feathered"))
    return {
        "id": id_, "name": name, "short": short, "kind": "gallop", "D": round(d.D * 1000), "desc": desc,
        "wind": [round(r["wind_W"], 3) for r in rows],
        "pot": [round(r["potential_W"], 3) for r in rows],
        "lim": [round(r["elec_W"], 3) for r in rows],
        "des": [round(r["elec_W"], 3) for r in rows],
        "pitch": [round(r["pitch_deg"], 1) for r in rows],
        "freq": [round(r["f_Hz"], 2) for r in rows],
        "note": [note_idx(r["note"]) for r in rows],
        "summary": {"from": ci, "to": gc.generates_to(d, ci, 0.5), "rated": d.P_rated if capped else 0, "rated_at": rated_at,
                    "mean_15_40": sum(mid) / len(mid), "p40": rows[-1]["elec_W"],
                    "survival": surv, "survival_part": part, "annual": gc.annual_energy(d, 4.5)},
    }


def gc_shell(d):
    for k, v in gc.SHELLS.items():
        if abs(v["shell_areal"] - d.shell_areal) < 1e-9 and abs(v["panel_cap"] - d.panel_cap) < 1e-9:
            return k
    return ""



# ---------------------------------------------------------------- power curves

def build_curves():
    notes.clear()
    designs = []
    B = lc.Design(); C = replace(lc.Design(), **lc.CONFIGS["C"]); A = replace(lc.Design(), **lc.CONFIGS["A"])
    designs.append(curve("B", "Configuration B (best output, survives 25 m/s)", B, "xps3-sandwich", "250-B vortex"))
    designs.append(curve("C", "Configuration C (all-weather, survives 40 m/s)", C, "xps5-storm", "250-C vortex"))
    designs.append(gcurve("G", "Galloping 330-G (generates to 40 m/s, rated 20 W)", gc.GDesign(), "330-G galloping"))
    GH = gc.design_from(argparse.Namespace(config="GH", shell=None, generator=None, section_preset=None, belt_preset=None))
    designs.append(gcurve("GH", "Galloping 330-GH (most power 15-40 m/s)", GH, "330-GH galloping"))
    for gname, cfg, label, short in (("grid-fine-25", "B", "Best in fine grid, survive 25 m/s", "Fine grid best, 25 m/s"),
                                     ("grid-fine-40", "C", "Best in fine grid, survive 40 m/s", "Fine grid best, 40 m/s"),
                                     ("grid-wide-25", "B", "Best in wide grid, survive 25 m/s", "Wide grid best, 25 m/s"),
                                     ("grid-wide-40", "C", "Best in wide grid, survive 40 m/s", "Wide grid best, 40 m/s")):
        d, shell = from_grid(gname, cfg)
        designs.append(curve(gname, label, d, shell, short))
    designs.append(curve("A", "Configuration A (first version)", A, "xps3-sandwich", "250-A vortex"))
    return {"speeds": SPEEDS, "notes": notes, "designs": designs}


def main():
    p = argparse.ArgumentParser(description="Build the Lantern design-grid page")
    p.add_argument("--out", default=os.path.join(REPO, "build", "grid-page"))
    out = p.parse_args().out
    os.makedirs(out, exist_ok=True)
    for name in ("grid-fine-25", "grid-fine-40", "grid-wide-25", "grid-wide-40"):
        build(GRID + name + ".csv", os.path.join(out, name + ".json"))
    curves = build_curves()
    with open(os.path.join(out, "curves.json"), "w") as fh:
        json.dump(curves, fh, separators=(",", ":"))
    src = open(os.path.join(HERE, "lantern-grid.src.html")).read()
    page = (src.replace("__FINE25__", open(os.path.join(out, "grid-fine-25.json")).read(), 1)
               .replace("__CURVES__", json.dumps(curves, separators=(",", ":")), 1))
    assert "__FINE25__" not in page and "__CURVES__" not in page
    with open(os.path.join(out, "lantern-grid.html"), "w") as fh:
        fh.write('<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" '
                 'content="width=device-width, initial-scale=1, viewport-fit=cover"><style>[hidden]{display:none!important}'
                 'body{margin:0}</style></head><body>' + page + "</body></html>")
    for x in curves["designs"]:
        s = x["summary"]
        print(x["id"], "|", x["name"])
    print("wrote", out)


if __name__ == "__main__":
    main()
