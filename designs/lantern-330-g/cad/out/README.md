# out/ (generated, not committed)

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
