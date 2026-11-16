# Lantern 330-G: build and test plan

Build in this order: first measure the side-force curve of the section, then build the swinging machine.

The galloping model rests on two numbers, A1 and A3, measured in smooth wind-tunnel flow. Turbulence near the ground can cut the output by 40% or more (see [physics.md](physics.md), section 10). A cheap static test on a car roof settles most of that before you build anything that moves.

## 1. Static side-force test (do this first)

**Rig:**
- Make one 330 mm × 1.0 m prism with its end plates.
- Mount it upright on a vertical axle above a car roof rack, at least 0.6 m above the roof, with the axle on two bearings so it can be set to any angle.
- Hold it at angle with a pointer and a protractor plate.
- Measure the sideways force with a load cell (a 5–20 kg bar cell and an HX711 board) on a short lever, and the airspeed with a pitot tube or vane anemometer ahead of the car, at least 1 m from the roof.

**Run:**
- Drive a private road at steady speeds: 8, 11 and 14 m/s, both directions, on a calm day.
- At each speed log the force at angles from −25° to +25° in 2.5° steps, then at 45°.
- Repeat on a gusty day: you want the turbulent-flow curve too.

**Reduce:**
- C_y(α) = F / (½ ρ U² D L).
- Fit C_y = A1 α − A3 α³ over −15° to +15°.
- Note where the curve peaks and where it crosses zero.
- Check the force at 45° is small and that the slope there is negative (stable).

**Decide:**
- Run `python3 tools/galloping_calc.py report --A1 <fit> --A3 <fit>` and, with the gusty-day fit, the `--turb_factor` that matches.
- If the measured A1 is well below 2.3, compare against Lantern 250-B for your site before building the swinging machine.

The same rig answers the end-plate question: test with and without plates.

## 2. Parts

No prices are given; check current suppliers. Masses and ratings come from `tools/galloping_calc.py report`.

| Group | Item | Notes |
|---|---|---|
| Prism | 10 mm extruded polystyrene (XPS) board, ~2.4 m², ~25 g/m² glass tissue and laminating epoxy on both faces | Four 330 × 1,000 mm panels, three bulkheads and two 660 mm square end plates. Build the outer skin up to ~3 layers over the bottom third. Alternative: 4 mm twin-wall polypropylene with bulkheads every 200 mm |
| | Glass tape (50 mm) | All four corners, inside and out |
| Neck | Roll-wrapped carbon tube, mostly lengthwise fibres, 50 × 47 mm, 600 mm | Bonded into the spider at the bottom bulkhead |
| Pitch drive | Two small ball bearings carrying the neck foot inside the hub; worm gear and DC gearmotor; magnetic angle encoder; torsion spring towards 45°; electromagnetic clutch (power to engage) | Fail-safe: losing power releases the clutch and the spring feathers the prism. Torque about 14 N m at 45 m/s |
| Hinge | 25 mm stainless axle, two sealed deep-groove ball bearings (6005-2RS) 300 mm apart | Hub and post head built for 800 N m; each bearing carries ~2.5 kN at 45 m/s |
| | Rubber end stops | ±20° |
| Springs | Two compression springs, ~31 N/mm each, ~40 mm usable travel, fatigue-rated, working force up to ~1.1 kN | Carriage 15–140 mm below the hinge, T8 lead screw and NEMA-17 stepper as on 250-B |
| Drive | GT2 belt on a 100 mm-radius arc on the hub; pulley to suit the generator | |
| Generator | 8108-size pancake outrunner, ~100 W class, wound for ~24 V (about 0.2 V s/rad) | Measure Ke, winding resistance and spin-down drag before fitting |
| Head | Yaw bearing, tail vane ~0.1 m² on a ~0.7 m boom | Slip ring or cable-untwist routine |
| Post | Steel tube for a ~3 m hinge height (e.g. 114 × 6 mm), guyed, ideally tilt-down | Base moment about 3.0 kN m at 45 m/s, 2.3 kN m generating at 40 m/s. Size to your local wind code |
| Electronics | Three-phase active bridge (rectifies and motors for the kick-start); MPPT converter into a 24 V LiFePO₄ battery; normally-closed brake relay or MOSFETs; voltage clamp; microcontroller; hinge angle encoder; anemometer | Parts rated ≥ 60 V |

## 3. Build order

1. **Panels.** Laminate the inner skin flat, cut the four panels, bond them at the corners round the bulkheads on a square jig, then tape the corners and laminate the outer skin.
2. **End plates and spider.** Fit the end plates square, then bond the neck socket into the bottom bulkhead.
3. **Hub.**
   - Pitch bearings and drive inside a tube that is the hub's swinging arm.
   - The hinge axle and bearings, the spring lever and carriage, the belt arc and the stops.
4. **Generator mount.** Adjustable for belt tension. Check the belt tracks through ±20°.
5. **Head and post.** Check that the vane aligns the head in light wind with the prism fitted and feathered.
6. **Electronics and software** (section 5).

## 4. Bench checks

| Check | How | Pass |
|---|---|---|
| Generator | Spin with a drill at known rpm: open-circuit voltage, winding resistance; time a spin-down | Ke, R and drag close to the preset, or update them in the calculator |
| Hinge friction | Swing with the belt off and the springs disconnected (prism hanging down); time the decay | Friction below ~0.1 N m at the hinge |
| Pitch drive | Drive 0–45° and back; cut power at 0° | Feathers to 45° on its own within ~2 s |
| Springs | Set the carriage at several positions; pluck; log the frequency | Matches the calculator's carriage table; never statically unstable (the prism must not fall over at the lowest setting) |
| Neck mode | Lock the hinge, tap the prism, log the ring-down | About 17 Hz expected; must exceed 1.5 × the top spring frequency (6 Hz) |
| Brake | Pluck, then short the generator; cut power while swinging | Swing dies within a few cycles |

## 5. Control software

- **Idle.** Face-on, generator open, until the wind exceeds about 3.5 m/s for 30 s. Then kick-start: drive the motor at the carriage's current frequency for a few cycles.
- **Generating.**
  - The generator load follows maximum power: hill-climb on measured power.
  - The carriage holds the swing at ±15°: move out (stiffer) if the swing exceeds it, in if it is smaller. This one loop keeps the frequency where the model wants it.
- **Rated.** Above 20 W, a slow loop on output power raises the pitch, keeping the generator load near maximum-power. Rate-limit pitch to a few degrees per second.
- **Feathered.** Pitch to 45° and short the generator:
  - when the 3-second gust exceeds 42 m/s or the 1-minute mean exceeds 40 m/s;
  - on over-voltage, icing (temperature below 2 °C with rain), loss of the swing sensor, or a battery fault;
  - on loss of power (spring and clutch).

  Return to service after 10 minutes below 35 m/s.

## 6. Outdoor tests

1. **Onset.** Generator open, carriage set low: log swing against wind to find the onset speed. Compare with the calculator's cut-in.
2. **Load sweep.** At steady wind, step the generator load to find the power peak. Compare with the calculator's best load.
3. **Power curve.**
   - Log electrical output, wind, pitch, swing and frequency for weeks, and bin by 0.5 m/s.
   - Plot it against the calculator's curve and against the turbulence intensity of each bin.
4. **Pitch regulation.** In strong wind, log how steadily pitch holds 20 W, the lean and the swing.
5. **Storms.** Feathered behaviour in gales: motion, loads on the stops, generator voltage.

Use the calculator to keep the model honest: put every measured value back into `tools/galloping_calc.py` (each design field is a `--name value` option) and re-run.

```bash
python3 tools/galloping_calc.py                          # Lantern 330-G report
```

```bash
python3 tools/galloping_calc.py curve --compare          # power 1-40 m/s, with 250-B and 250-C
```

```bash
python3 tools/galloping_calc.py envelope --step 0.5 --csv envelope.csv   # every limit, every wind
```

```bash
python3 tools/galloping_calc.py report --A1 1.9 --A3 15 --turb_factor 1.0   # your measured section
```

```bash
python3 tools/galloping_calc.py sweep --site 6.0          # best design for a 6 m/s site
```

## 7. Safety

- The prism swings ±15° at the hinge: about ±0.4 m at its top, 4.6 m above ground, at up to 3.7 Hz in strong wind. Keep people and branches clear.
- The post carries about 3 kN m at its base in a 45 m/s storm. Guy it, and lower the head for all work.
- Never rely on the brake alone: the feather spring is the primary protection, the shorted generator the second.
- Belt arc, springs and carriage carry hundreds of newtons: guard them.
- Check local planning rules for a moving structure of this height.
