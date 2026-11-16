# tube_power

Design work on a home-scale **bladeless wind generator**: a tube that swings in the wind instead of spinning blades.

The current design is **Lantern 250**:
- a light Ø250 × 1,000 mm foam drum with a disc at each end,
- on a carbon neck and a single-axis hinge that a tail vane keeps aligned with the wind,
- swinging across the wind and driving one small generator through a toothed belt.

The swing stays in step with the wind by sliding a spring carriage along a lever below the hinge, about 20 mm per 1 m/s of wind speed.

> **Status: concept design, not built or tested.** All performance figures are model estimates. The low case assumes real gusty wind halves them.

| Lantern 250-B (recommended) | |
|---|---|
| Tube | Ø250 × 1,000 mm, 3 mm foam with glass-tissue skin, Ø500 mm end discs |
| Neck and hinge | 800 mm carbon neck; hinge axle points into the wind; hinge ~3 m above ground |
| Swinging mass | 0.49 kg (mass ratio ~4.3) |
| Drive | GT2 belt, 26:1, to a 5208-size brushless gimbal motor |
| Tuning range | 3–7 m/s |
| **Electrical power at 4.5 m/s** | **~2.0 W** (low case ~1.0 W) |
| Electrical power at 6 m/s | ~4.8 W (low case ~2.4 W) |
| Energy at a 4.5 m/s-mean site | ~11 kWh/yr (low case ~5) |

For scale, a 100 W solar panel gives roughly 90–150 kWh a year. This is a physics and mechanism project. The aim of a first build is to measure a power curve, which nobody has published for a tube like this.

## Repository map

| Path | Contents |
|---|---|
| [designs/lantern-250/README.md](designs/lantern-250/README.md) | Full design specification: reasoning, configurations A and B, parts, structure, tuning, drive, electronics, performance, optimisation, risks |
| [designs/lantern-250/physics.md](designs/lantern-250/physics.md) | Every model and equation used, with confidence levels and references |
| [designs/lantern-250/build-and-test.md](designs/lantern-250/build-and-test.md) | Parts list, build order, bench and outdoor tests, safety |
| [designs/lantern-250/calculator-output/](designs/lantern-250/calculator-output/) | Saved calculator reports and optimisation sweeps |
| [docs/design-history.md](docs/design-history.md) | Earlier designs (tuned mast with mechanical rectifier, 40 mm PVC, 40 mm carbon, contactless generators) and what each taught |
| [research/](research/) | Research report and notes on bladeless turbines, DIY builds, patents and academic work |
| [tools/lantern_calc.py](tools/lantern_calc.py) | Design calculator and grid-search optimiser (Python 3, standard library only) |

## Calculator

Report for the recommended configuration:

```bash
python3 tools/lantern_calc.py
```

Report for the first configuration:

```bash
python3 tools/lantern_calc.py report --config A
```

Override any parameter, for example a 200 mm tube with your measured motor:

```bash
python3 tools/lantern_calc.py report --D 0.2 --Ke 0.30 --R_coil 9
```

Grid search over diameter, neck length, end-disc size, shell material and gear ratio, ranked by power at 4.5 m/s:

```bash
python3 tools/lantern_calc.py sweep
```

Rank by yearly energy for your site's mean wind speed instead:

```bash
python3 tools/lantern_calc.py sweep --objective annual --site 4.0
```

The optimiser pushes to whatever edge the model rewards. The diameter is capped by the Reynolds-number range covered by the evidence, and the neck by the hinge's storm-moment limit. Read [section 12 of the specification](designs/lantern-250/README.md#12-optimisation-results) before trusting a sweep result.
