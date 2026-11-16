# Lantern 250: build and test plan

Build the rig so configurations A and B are interchangeable: two neck lengths, two disc sizes, 12- and 16-tooth pulleys, two spring sets. Then let measurements decide. Configuration C (all-weather) uses a heavier shell, neck and hub; build it once B has proved the concept, or build B's hub to C's strength from the start. The goal of the first build is a **measured power curve** (electrical output against wind speed into a known load). Nobody has published one for a small bladeless tube of this kind.

## 1. Parts

No prices are given; check current suppliers.

| Group | Item | Notes |
|---|---|---|
| Tube | Extruded polystyrene sheet (model-aircraft foam, e.g. Depron-type): 3 mm for A/B, 5 mm for C; ~1.5 m² | Shell and discs |
| | ~25 g/m² glass tissue (surfacing veil) and laminating epoxy, **on both faces** | Skins carry storm bending and resist ovalling. For C, build the outer skin up to ~3 layers over the bottom third of the tube |
| | Foam for four internal rings (C: carbon-capped rings) | Keep the tube round |
| Neck | Roll-wrapped carbon tube, mostly lengthwise fibres: 30 × 28 mm, 0.8 m (B); 35 × 32 mm, 0.6 m (C); 25 × 23 mm, 0.4 m (A) | Bonded into hub and spider sockets |
| Hub and hinge | Stainless axle and two flanged polymer plain bushings: 12 mm, 150 mm apart (B); 16 mm, 200 mm apart (C) | Hub built for 150 N·m (B) or 350 N·m (C) |
| | Rubber end-stop blocks | ±14° |
| Tuning | Two compression springs, 17.7 N/mm (B), 17.8 N/mm (C), 8.0 N/mm (A), ~35 mm usable travel | Fatigue-rated (die springs are a good choice) |
| | T8 lead screw (2 mm per turn), nut, linear guide, NEMA-17 stepper | Carriage 60–140 mm below the hinge |
| Drive | GT2 belt (6 mm or 9 mm wide), clamped round a 100 mm-radius arc on the hub | |
| | 12-tooth and 16-tooth GT2 pulleys to suit the motor shaft | |
| Generator | 5208-size brushless gimbal motor | Check cogging before buying several (section 3) |
| Head | Yaw bearing (lazy-Susan or two ball bearings), tail-vane boom ~0.6 m, vane 0.05–0.1 m² | |
| | Slip ring or cable-untwist routine | |
| Post | Steel tube for a ~3 m hinge height, guyed, ideally tilt-down | Base moment ~550 N·m at 25 m/s (B), ~1,360 N·m at 40 m/s (C), from the calculator. Size to your local wind code |
| Electronics | Three-phase active (MOSFET) bridge that can rectify and also drive the motor for the kick-start; MPPT buck-boost converter with very low standby draw; 12.8 V LiFePO₄ or supercapacitors; microcontroller; **normally-closed** relay or MOSFETs for the brake, plus a small braking resistor (~2–5 Ω, 20 W); voltage clamp; everything rated ≥ 150 V | |
| Instruments | Cup anemometer at hub height, current and voltage sensing, temperature sensor (icing), optional IMU or Hall sensor for swing angle, data logging | |

## 2. Build order

1. **Shell.**
   - Laminate glass tissue on the inside face of the foam sheet first, while it is flat.
   - Roll the foam round the four rings (use a 250 mm former) and tape the seam.
   - Laminate glass tissue over the outside with minimal epoxy (roll and blot). For C, add two more layers over the bottom third, tapering out.
   - Target: about 186 g including rings for B, 285 g for C.
2. **Discs.**
   - Cut Ø500 mm (and Ø400 mm for A) discs from the same glass-faced foam and fit them square to the tube ends.
   - Make them removable at first, so you can test with and without.
3. **Spider and neck.**
   - Bond a socket for the neck into a spider that grips the bottom ring.
   - Make the neck-to-hub joint a clamp, so necks can be swapped.
4. **Hub, hinge and stops.**
   - Mount the hinge with its axle pointing into the wind.
   - Fit the lever below the hinge with the spring carriage and lead screw.
   - Fit the belt arc and the end stops.
5. **Generator mount.**
   - Make it adjustable for belt tension.
   - Check that the belt tracks over the full ±14° swing.
6. **Head and post.**
   - Fit the yaw bearing and tail vane.
   - Check that the vane aligns the head in light wind before the tube is fitted.
7. **Electronics.** Fit the bridge, MPPT, storage, brake, clamp and logging. Make the brake fail-safe: phases shorted (or on the braking resistor) when unpowered.
8. **Control software.** Implement the operating modes in the specification (section 6): idle, kick-start, tracking, power cap from 7 m/s, brake from 8 m/s or on over-voltage, icing or loss of power.

## 3. Bench checks before going outdoors

| Check | How | Pass |
|---|---|---|
| Generator cogging | Torque wrench or a lever and luggage scale on the motor shaft, unconnected | < ~5 mN·m at the shaft (< ~0.13 N·m at the hinge through 26:1) |
| Generator constants | Spin it at known rpm (drill), measure open-circuit voltage and winding resistance | Ke near 0.38 V·s/rad; if not, recompute the load with the calculator |
| Hinge friction | Swing the tube freely with no belt and springs disconnected; time the decay | Parasitic damping ratio < 0.01 |
| Mass and inertia | Weigh parts; swing as a pendulum about the hinge (tube hanging down) | Within ~15% of the calculator |
| Still-air frequency | Set the carriage, pluck the tube, log generator open-circuit voltage frequency | Matches the carriage scale; build the real f_n(r) table |
| Damping with load | Pluck with a fixed resistor (~110 Ω) on the generator; measure the decay | Generator damping ratio near 0.03 |
| Kick-start | In still air, command a short drive burst at the tuned frequency | Tube reaches a few degrees of swing within a few cycles |
| Brake | Pluck, then apply the brake; also cut power with the tube swinging | Swing stops within a few cycles; brake engages with power removed |
| Neck modes | Lock the tube by hand, tap the neck and record the ring-down (phone accelerometer) | Note any mode between 10 and 35 Hz; vortices reach it at roughly 1.25 × frequency m/s |

Update `tools/lantern_calc.py` parameters with the measured values and re-run before outdoor tests.

## 4. Outdoor tests

1. **Lock-on map, generator open-circuit.**
   - Fix the carriage at a few positions. For each, log swing amplitude against 1-minute average wind speed.
   - This finds the real U* and the width of the lock-on band.
2. **Load sweep.** At steady wind inside the band, step the load resistance and find the power peak. This is the optimum generator damping.
3. **Power curve.**
   - With MPPT and automatic tuning running, log electrical power, wind speed and swing for weeks.
   - Bin by wind speed (0.5 m/s bins) and plot. **This is the key result.**
4. **A/B comparisons**, each over several windy days with the other settings fixed:
   - 400 mm vs 800 mm neck
   - Ø400 vs Ø500 mm discs, and no discs
   - 12- vs 16-tooth pulley
   - Roughness strips on and off. Michigan's passive turbulence control used thin strips at about ±20–60° from the front stagnation point. Here the head turns with the wind, so the strips stay correctly placed.
5. **Mode transitions.** Log the cap and brake engaging in rising wind (7–9 m/s), and check winding temperature in the capped band against the assumed 5 W limit.
6. **Storms.** Log tube motion and generator voltage while braked in strong wind. Compare drag, bushing and post loads with the calculator envelope.
7. **Endurance.** Inspect the skin, belt, bushings and springs monthly, and after every storm.

A useful trick for repeatable wind: a roof-rack rig driven at a steady speed on a private road. Mind the safety.

## 5. Calculator workflow

```bash
python3 tools/lantern_calc.py                       # configuration B report
```

```bash
python3 tools/lantern_calc.py report --config C     # configuration C (all-weather) report
```

```bash
python3 tools/lantern_calc.py envelope --config C   # mode, power and every limit at 1-40 m/s
```

```bash
python3 tools/lantern_calc.py envelope --from 0.5 --step 0.5 --to 40 --csv curve.csv   # fine power curve
```

```bash
python3 tools/lantern_calc.py sweep --config C      # best design that survives 40 m/s
```

```bash
python3 tools/lantern_calc.py report --config A     # configuration A report
```

```bash
python3 tools/lantern_calc.py report --Ke 0.30 --R_coil 9 --gen_rotor_J 4e-5   # your measured motor
```

```bash
python3 tools/lantern_calc.py sweep                 # grid search, ranked by power at 4.5 m/s
```

```bash
python3 tools/lantern_calc.py sweep --objective annual --site 4.0   # ranked by yearly energy at your site
```

```bash
python3 tools/lantern_calc.py sweep --Re_max 2e5 --M_hinge_max 250  # explore beyond the tested range
```

```bash
python3 tools/lantern_calc.py sweep --csv grid.csv                  # save every grid point to CSV
```

Every design field can be overridden with `--name value`. Run `--help` on either command to list them.

## 6. Safety

- **Height and falling parts:** the tube is light, but the hub, generator and post top are not. Lower the head for all work. Guy the post.
- **Storms:** the controller brakes from 8 m/s. Configuration B is built for 25 m/s: lower it (tilt-down post) or remove the tube when stronger gusts are forecast. Configuration C is built for 40 m/s parked and braked; still inspect it after every storm. Never lock the hinge rigidly.
- **Voltage:** if the brake fails, open-circuit voltage at the end stops can pass 100 V. Treat the generator side as hazardous, clamp it, and rate parts for at least 150 V.
- **Pinch points:** the belt arc and spring carriage move with up to ~5 N·m of torque. Guard them.
- **Battery:** fuse at the battery and use a LiFePO₄ charge controller.
- **Neighbours and planning:** a 4–5 m swinging object may need permission where you live. Check local rules.
