# Lantern 330-G CAD

The 3D model of the [Lantern 330-G](../README.md) galloping wind generator: every part, which material it is made of, which parts are 3D printed, and checks that the parts clear each other as the machine swings and pitches.

- **[SPEC.md](SPEC.md) is the contract.** It fixes the frames, the coordinates and size of every part, the materials and colours, the bought-part interfaces and the controller PCB envelope. Code reads its numbers from `l330g/layout.py`, which copies them one for one. Where a number is missing from SPEC.md, `layout.py` lists it as ASSUMED (a VERIFY item). Where SPEC numbers conflict with each other, `layout.py` lists the smallest change that resolves it as a DEVIATION.
- **Printed parts** (P01 to P24) live in the 3dprint repo, `parts/lantern330g/`, one module per part. The assembly loads them from there. Until a part's module exists and builds, the assembly draws a pale placeholder envelope at its SPEC position.
- **Everything else** (structure, bought parts, belt, PCB placeholder) is modelled here, in `l330g/structure.py`.

## Running it

From this directory (`designs/lantern-330-g/cad`), with python3, build123d, trimesh, manifold3d, numpy and matplotlib installed:

```bash
python3 -m l330g build                    # upright, face-on: STEP, GLB, BOM, previews, check at all six poses
```

```bash
python3 -m l330g build --pose 20,0        # swung to the +20° stop
```

```bash
python3 -m l330g build --no-printed --quick   # structure only; check the build pose only
```

```bash
python3 -m l330g check                    # interference and clearance check at the six SPEC poses
```

`check` exits 1 if it finds a real interference. A full `build` takes about two minutes.

Outputs go to `out/`, which is not committed (see [out/README.md](out/README.md)):

| File | Contents |
|---|---|
| `lantern330g_t+0_b+0.step` | Assembly STEP, one named and coloured child per part, e.g. `P03 belt_arc [PAHT-CF, printed]`, `M27 Hinge cheek 20 mm +X [Aluminium 6082-T6]` |
| `lantern330g_t+0_b+0.glb` | The same as a GLB for viewers: one node per part, PBR colour from the legend, node extras `{id, name, material_key, material_label, printed, bought, frame, group}` |
| `bom.csv`, `bom.json` | Bill of materials: id, name, material, printed Y/N, bought Y/N, quantity, mass estimate |
| `interference.md`, `.json` | Overlaps and clearances at the six poses, the SPEC 4 named clearances, placeholders, deviations, assumptions |
| `preview_*.png` | Shaded previews coloured by material: iso, front, side, top, bottom, hub close-ups, the whole machine |

Environment variables: `LANTERN_3DPRINT` points at the 3dprint checkout (default: the `3dprint` directory beside `tube_power`), and `LANTERN_PCB` at the pcb checkout (default: `pcb` beside it).

## Frames (SPEC section 1)

| Frame | Moves with | Definition |
|---|---|---|
| A | the yaw head | Origin on the hinge axis between the hinge bearings. +X downwind (tail side), +Z up, ground at Z = −3000 |
| S | hub, neck, prism | A rotated by the swing angle θ about X: p_A = R_x(θ) p_S. Design ±15°, stops ±20° |
| P | neck and prism | S rotated by the pitch angle β about the neck axis: p_S = R_z(β) p_P. β = 45° is feathered |

Each part carries its frame. `assembly.build(theta, beta, carriage_r)` poses frame-S parts by R_x(θ) and frame-P parts by R_x(θ) R_z(β). Three things are rebuilt for each pose:

- the spring carriage, at its position r along the lever (15 to 140 mm, default 80);
- the springs, forks and rollers, solved so both rollers stay on their reaction plates;
- the belt, whose clamped ends turn with the arc while its free spans stay fixed.

The six check poses are (θ, β) = (0, 0), (±20, 0), (0, 45) and (±15, 10).

## Part numbers and materials

- **P01 to P24:** printed parts (SPEC section 5): ASA orange, PAHT-CF purple, TPU teal.
- **M-numbers:** made parts: sandwich panels, CFRP neck, aluminium plates, steel weldments, PP vane.
- **B-numbers:** bought parts: bearings, belt, motors, sensors, glands, battery.

Colours follow the SPEC section 8 legend. The BOM masses use the densities in `l330g/materials.py`; the sandwich, PP twin-wall, bought electrical parts and the battery box use effective densities.

## The package

| Module | Job |
|---|---|
| `layout.py` | every SPEC number as a named constant, plus the ASSUMED and DEVIATIONS lists |
| `materials.py` | the SPEC section 8 legend, with densities for the mass estimate |
| `structure.py` | every non-printed part, as build123d solids at their SPEC positions |
| `belt.py` | the belt's omega path in the X = 85 plane (from `parts/lantern330g/belt_path.json` when P06's author writes it, else SPEC 3.4) and the belt solid |
| `printed.py` | finds and loads the printed parts, with placeholder envelopes for missing ones |
| `assembly.py` | posing, and the STEP, GLB and BOM exports |
| `interference.py` | overlap check (manifold3d meshes, confirmed with exact OCC booleans), clearances, SPEC 4 named pairs |
| `render.py` | the numpy z-buffer renderer for the previews |
| `mesh.py`, `geom.py`, `item.py` | tessellation, small modelling helpers, the `Item` record |

## How the check works

- Every pair whose parts move relative to each other is tested at each pose:
  - S or P against A;
  - P against S;
  - the carriage against the rest of S;
  - the belt against the head.
- Parts that never move relative to each other are tested once, at θ = 0, β = 0.
- Pairs are prefiltered by bounding box, and overlap volumes come from manifold3d.
- An overlap above 1 mm³ is checked again with an exact OCC boolean before it is reported.
- Intended contacts and nested fits are listed with a reason in `interference.ALLOW`, e.g. "belt teeth in the arc's toothed rim" or "magnet in its holder".
- Moving pairs closer than 3 mm are listed. The intended running gaps (bearing labyrinths, encoder air gaps) are marked with their reason.
