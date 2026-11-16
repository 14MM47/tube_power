# tube_power

Design work on a home-scale **bladeless wind generator**: a tube that swings in the wind instead of spinning blades.

The current design is **Lantern 250**:
- a light Ø250 × 1,000 mm foam drum with a disc at each end,
- on a carbon neck and a single-axis hinge that a tail vane keeps aligned with the wind,
- swinging across the wind and driving one small generator through a toothed belt.

It generates from about 1.6 m/s to 8 m/s as designed (to about 11 m/s with the keep-generating option), brakes itself above that, and in configuration C survives 40 m/s.

The swing stays in step with the wind by sliding a spring carriage along a lever below the hinge, about 20 mm per 1 m/s of wind speed.

> **Status: concept design, not built or tested.** All performance figures are model estimates. The low case assumes real gusty wind halves them.

| | **B: best output** | **C: all-weather** |
|---|---|---|
| Tube | Ø250 × 1,000 mm, 3 mm foam, glass both faces, Ø500 mm end discs | Ø250 × 1,000 mm, 5 mm foam, glass both faces (thicker near the base), Ø500 mm end discs |
| Neck and hub | 800 mm, 35 × 32 mm carbon neck; hub built for 150 N·m | 600 mm, 35 × 32 mm carbon neck; hub built for 350 N·m |
| Swinging mass / mass ratio | 0.63 kg / 5.5 | 0.86 kg / 7.7 |
| Drive | GT2 belt, 26:1, to a 5208-size brushless gimbal motor | same |
| Generates | ~1.6–8 m/s (tracking to 7, capped to 8, braked above) | same |
| **Electrical power at 4.5 m/s** | **~2.0 W** (low case ~1.0 W) | **~1.8 W** (low case ~0.9 W) |
| Electrical power at 7 m/s (rated) | ~7.4 W | ~7.0 W |
| Survives, parked and braked | 25 m/s | 42 m/s |
| Kept generating within limits | to ~10.8 m/s, peak ~24 W | to ~11 m/s, peak ~26 W |
| Energy at a 4.5 m/s-mean site | ~9 kWh/yr as designed; ~15 kWh/yr kept generating | ~8.5 kWh/yr as designed; ~14 kWh/yr kept generating |

For scale, a 100 W solar panel gives roughly 90–150 kWh a year. This is a physics and mechanism project. The aim of a first build is to measure a power curve, which nobody has published for a tube like this.

## Galloping version: Lantern 330-G

A vortex-shedding tube generates nothing above about 11 m/s, whatever the control. **Lantern 330-G** keeps generating to 40 m/s by galloping instead:
- a 330 mm square prism, 1 m tall, with 660 mm square end plates;
- on a 600 mm carbon neck and the same kind of hinge, spring carriage, belt and yaw head;
- with a pitch drive that turns the prism on its own axis.

A square's side force pushes it the way it is already moving, so it extracts energy at any wind above onset, with no lock-on band. It generates from about 2.5 m/s and reaches its 20 W rating at 15.5 m/s. Above that, pitching it up to 10° holds 20 W all the way to 40 m/s. Above 40 m/s, or on any fault, a spring turns it 45° (feathered), where it neither gallops nor pushes sideways. It survives 46.7 m/s.

| Site mean wind | 330-G (galloping) | 250-B as designed | 250-B kept generating |
|---|---|---|---|
| 4.5 m/s | 6.2 kWh/yr | 9.1 | 14.7 |
| 6.5 m/s | 19.0 | 9.5 | 24.3 |
| 7.5 m/s | 27.8 | 8.6 | 25.3 |

Galloping catches only ~4% of the wind passing it, against 15–20% for the light round tube at its tuned speed. So 330-G wins only at windy sites, and the smooth-flow coefficients it rests on may be optimistic in gusty air. See [designs/lantern-330-g/](designs/lantern-330-g/).

**Lantern 330-GH** is the same prism built for the most power from 15 to 40 m/s, with no power cap and no pitch regulation. Its upgrades:
- a direct-drive e-bike hub motor;
- an HTD 8M belt on a 275 mm arc;
- a ±25° swing with 3 kN springs;
- an 800 mm neck on a 1,200 N·m hub.

Nothing reaches its limit below 40 m/s, so the prism simply stays face-on, with a spring feather to 45° for storms and faults. It averages **152 W from 15 to 40 m/s** (330-G: 20 W), with 47 W at 20 m/s, 163 W at 30 and **384 W at 40 m/s**. The cost is a 6 m/s cut-in. It only beats 330-G over a year where the mean wind is above about 8 m/s, because winds above 25 m/s blow for about an hour a year even at a 7.5 m/s site.

```bash
python3 tools/galloping_calc.py curve --config GH --compare
```

## Repository map

| Path | Contents |
|---|---|
| [designs/lantern-250/README.md](designs/lantern-250/README.md) | Full design specification: reasoning, configurations A, B and C, operating modes from 2 to 40 m/s, parts, structure, tuning, drive, electronics, performance, optimisation, risks |
| [designs/lantern-250/physics.md](designs/lantern-250/physics.md) | Every model and equation used, with confidence levels and references |
| [designs/lantern-250/build-and-test.md](designs/lantern-250/build-and-test.md) | Parts list, build order, bench and outdoor tests, safety |
| [designs/lantern-250/calculator-output/](designs/lantern-250/calculator-output/) | Reports, 1–40 m/s wind envelopes and 1–40 m/s power curves for A, B and C; optimisation sweeps |
| [designs/lantern-250/calculator-output/grid/](designs/lantern-250/calculator-output/grid/) | Full optimisation grids as CSV: 102,480 design points for 25 m/s and 40 m/s survival, passing and failing, 41 columns each |
| [designs/lantern-330-g/](designs/lantern-330-g/) | The galloping version that generates to 40 m/s: specification, physics, build and test plan (static side-force test first), calculator output and grids |
| [docs/design-history.md](docs/design-history.md) | Earlier designs (tuned mast with mechanical rectifier, 40 mm PVC, 40 mm carbon, contactless generators) and what each taught |
| [research/](research/) | Research report and notes on bladeless turbines, DIY builds, patents and academic work |
| [tools/lantern_calc.py](tools/lantern_calc.py) | Design calculator, wind-envelope checker and grid-search optimiser (Python 3, standard library only) |
| [tools/galloping_calc.py](tools/galloping_calc.py) | The same for the galloping versions (330-G, and 330-GH with `--config GH`): every limit from 1 to 45 m/s, parallel grid search |
| [tools/galloping_timestep_check.py](tools/galloping_timestep_check.py) | Checks the galloping calculator against a direct time-step simulation of the swinging prism |
| [tools/grid_page/](tools/grid_page/) | Source and build script for the interactive design-grid page (power curves 1–40 m/s with a compare overlay, and every grid point) |

## Calculator

Report for the recommended configuration (B), including its wind envelope:

```bash
python3 tools/lantern_calc.py
```

Mode, power and every structural and electrical limit at each wind speed from 1 to 40 m/s, here for the all-weather configuration:

```bash
python3 tools/lantern_calc.py envelope --config C
```

Electrical power at every wind speed from 1 to 40 m/s: as designed, kept generating within every limit, the model's potential, and the wind passing the tube:

```bash
python3 tools/lantern_calc.py curve --config C
```

The same in 0.5 m/s steps, saved as CSV:

```bash
python3 tools/lantern_calc.py curve --config C --from 0.5 --step 0.5 --to 40 --csv curve.csv
```

Run any command with the keep-generating control instead of the default cap-and-brake:

```bash
python3 tools/lantern_calc.py envelope --config C --keep_generating 1
```

Override any parameter, for example a 200 mm tube with your measured motor:

```bash
python3 tools/lantern_calc.py report --D 0.2 --Ke 0.30 --R_coil 9
```

Grid search over diameter, neck length, end-disc size, shell construction and gear ratio, ranked by power at 4.5 m/s, for designs that survive 25 m/s:

```bash
python3 tools/lantern_calc.py sweep
```

The same for designs that survive 40 m/s (configuration C's hub):

```bash
python3 tools/lantern_calc.py sweep --config C
```

Any other survival requirement, ranked by yearly energy at your site's mean wind speed:

```bash
python3 tools/lantern_calc.py sweep --config C --U_storm 35 --objective annual --site 4.0
```

Save every grid point, passing or not, to a CSV file:

```bash
python3 tools/lantern_calc.py sweep --csv grid.csv
```

The optimiser pushes to whatever edge the model rewards:
- The diameter is capped by the Reynolds-number range covered by the evidence.
- The neck is capped by the hub's storm-moment limit.

Read [section 13 of the specification](designs/lantern-250/README.md#13-optimisation-results) before trusting a sweep result.

### Galloping calculator

Report for Lantern 330-G, its power from 1 to 40 m/s beside 250-B and 250-C, and a grid search for your site:

```bash
python3 tools/galloping_calc.py
```

```bash
python3 tools/galloping_calc.py curve --compare
```

```bash
python3 tools/galloping_calc.py sweep --site 6.0 --hubs 500,800 --csv grid.csv
```

Put your measured side-force coefficients in with `--A1` and `--A3`, and test turbulence sensitivity with `--turb_factor 0.8`.
