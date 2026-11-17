"""Command line: build, export and check the Lantern 330-G assembly.

Run from ``designs/lantern-330-g/cad``::

    python3 -m l330g build [--pose THETA,BETA] [--no-printed] [--out DIR] [--carriage-r R] [--quick]
    python3 -m l330g check [--no-printed] [--out DIR]

``build`` writes to ``out/``: the assembly STEP and GLB, the BOM (CSV and
JSON), the interference report (Markdown and JSON) and preview PNGs. With
``--quick`` the interference check runs at the build pose only.
``check`` runs the interference and clearance check at the six SPEC poses
and exits 1 if any real interference is found.
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

from . import assembly
from . import interference
from . import layout as L
from . import render

CAD_DIR = Path(__file__).resolve().parents[1]
DEFAULT_OUT = CAD_DIR / "out"

OUT_README = """# out/ (generated, not committed)

Everything here is written by `python3 -m l330g build` and `python3 -m l330g check`,
run from `designs/lantern-330-g/cad`. Only this README is committed.

| File | What it is |
|---|---|
| `lantern330g_<pose>.step` | Assembly STEP: one named, coloured child per part, e.g. `P03 belt_arc [PAHT-CF, printed]` |
| `lantern330g_<pose>.glb` | The same as a GLB: one node per part, PBR colour from the material legend, node extras `{id, name, material_key, material_label, printed, bought, frame, group}` |
| `bom.csv`, `bom.json` | Bill of materials: id, name, material, printed, bought, quantity, mass estimate |
| `interference.md`, `interference.json` | Interference and clearance report at the six SPEC poses |
| `preview_*.png` | Quick shaded previews (iso, front, side, top, bottom, a hub close-up, the full height), coloured by material |
| `.cache/` | Built printed parts, keyed by their source hash |

`<pose>` is `t+0_b+0` for theta 0, beta 0 (upright, face-on).
"""


def _ensure_out(out: Path):
    out.mkdir(parents=True, exist_ok=True)
    gi = out / ".gitignore"
    if not gi.exists():
        gi.write_text("*\n!.gitignore\n!README.md\n")
    rd = out / "README.md"
    if not rd.exists() or rd.read_text() != OUT_README:
        rd.write_text(OUT_README)


def _pose_tag(theta, beta):
    return f"t{theta:+.0f}_b{beta:+.0f}"


#: Preview framings (3D boxes in frame A, mm).
FRAMES = {
    "machine": ((-760, -500, -700), (930, 500, 1650)),
    "hub": ((-380, -190, -340), (240, 190, 290)),
    "full": ((-760, -500, -3000), (930, 500, 1650)),
}


def previews(items, out: Path, theta, beta, log=print):
    tag = f"theta {theta:+.0f}°, beta {beta:+.0f}°"
    note = "Lantern 330-G. Frame A: +X downwind, +Z up, origin on the hinge axis. Colours: SPEC section 8 legend."
    jobs = [
        ("iso", "iso", "machine", "Isometric"),
        ("front", "front", "machine", "Front (from upwind, looking +X)"),
        ("side", "side", "machine", "Side (from -Y, wind from the left)"),
        ("top", "top", "machine", "Top"),
        ("bottom", "bottom", "machine", "Bottom"),
        ("hub_iso", "iso", "hub", "Hub, hinge and head, isometric"),
        ("hub_rear", "iso_rear", "hub", "Hub, hinge and head, from downwind"),
        ("hub_side", "side", "hub", "Hub, hinge and head, side"),
        ("full_iso", "iso", "full", "Whole machine"),
    ]
    paths = []
    for name, view, frame, title in jobs:
        t = time.time()
        p = render.render_items(items, view, out / f"preview_{name}.png", extent=FRAMES[frame],
                                title=f"{title}: {tag}", mesh_fn=assembly.item_mesh, note=note)
        paths.append(p)
        if log:
            log(f"  preview {p.name} ({time.time() - t:.1f} s)")
    return paths


def cmd_build(a):
    out = Path(a.out) if a.out else DEFAULT_OUT
    _ensure_out(out)
    theta, beta = a.pose
    t0 = time.time()
    items = assembly.build(theta, beta, a.carriage_r, include_printed=not a.no_printed)
    print(f"built {len(items)} items at theta {theta:+.0f}, beta {beta:+.0f} ({time.time() - t0:.1f} s)")
    info = items[0].extra.get("build_info", {})
    prep = info.get("printed")
    if prep is not None:
        print(f"printed parts: {len(prep.loaded)} loaded, {len(prep.placeholders)} placeholders")
        for line in prep.log:
            print("  ", line)
    tag = _pose_tag(theta, beta)
    t = time.time()
    p = assembly.export_step(items, out / f"lantern330g_{tag}.step")
    print(f"STEP {p.name} ({time.time() - t:.1f} s)")
    t = time.time()
    p = assembly.export_glb(items, out / f"lantern330g_{tag}.glb")
    print(f"GLB {p.name} ({time.time() - t:.1f} s)")
    rows = assembly.export_bom(items, out / "bom.csv", out / "bom.json")
    tot = json.loads((out / "bom.json").read_text())["totals"]
    print(f"BOM {len(rows)} lines; mass estimate {tot['mass_g_all'] / 1000:.1f} kg, printed "
          f"{tot['mass_g_printed'] / 1000:.2f} kg; swinging (S+P) {tot['swinging_mass_kg']:.2f} kg, "
          f"centre of mass Z {tot['swinging_com_z_mm']:.0f} mm, inertia about the hinge "
          f"{tot['swinging_inertia_about_hinge_kgm2']:.3f} kg m2")
    previews(items, out, theta, beta)
    poses = [(theta, beta)] if a.quick else L.POSES
    res = interference.check(poses=poses, carriage_r=a.carriage_r, include_printed=not a.no_printed,
                             named=not a.quick)
    interference.write_report(res, out / "interference.md", out / "interference.json")
    _summary(res)
    print(f"done in {time.time() - t0:.0f} s; outputs in {out}")
    return 0


def _summary(res):
    s = res["summary"]
    print(f"interferences: {s['interferences']}; placeholder overlaps: {s['placeholder_overlaps']}; "
          f"unexplained gaps < 3 mm: {s['unexplained_close']}; named pairs below design: "
          f"{', '.join(s['named_below']) or 'none'} ({res['seconds']} s)")
    for r in res["poses"] + res["carriage_range"]:
        for c in r["interferences"]:
            print(f"  INTERFERENCE theta {r['theta']:+.0f} beta {r['beta']:+.0f}: {c['a']} x {c['b']} "
                  f"{c.get('exact_mm3')} mm3 ({c['category']})")


def cmd_check(a):
    out = Path(a.out) if a.out else DEFAULT_OUT
    _ensure_out(out)
    res = interference.check(include_printed=not a.no_printed)
    interference.write_report(res, out / "interference.md", out / "interference.json")
    _summary(res)
    print(f"report: {out / 'interference.md'}")
    return 1 if res["summary"]["interferences"] else 0


def _pose(s):
    t, b = (float(x) for x in s.split(","))
    return t, b


def main(argv=None):
    ap = argparse.ArgumentParser(prog="python3 -m l330g", description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    b = sub.add_parser("build", help="build, export and check the assembly")
    b.add_argument("--pose", type=_pose, default=(0.0, 0.0), metavar="THETA,BETA")
    b.add_argument("--no-printed", action="store_true", help="leave the printed parts out")
    b.add_argument("--out", default=None)
    b.add_argument("--carriage-r", type=float, default=L.CARRIAGE_R_DEFAULT)
    b.add_argument("--quick", action="store_true", help="check the build pose only")
    c = sub.add_parser("check", help="interference and clearance check at the six SPEC poses")
    c.add_argument("--no-printed", action="store_true")
    c.add_argument("--out", default=None)
    a = ap.parse_args(argv)
    return {"build": cmd_build, "check": cmd_check}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
