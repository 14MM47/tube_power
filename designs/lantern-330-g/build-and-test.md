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
| Pitch drive | Two small ball bearings carrying the neck foot inside the hub; worm gear and DC gearmotor; magnetic angle encoder; torsion spring towards 45°; zero-hold feather latch with a 12 V trip solenoid ([cad/latch.md](cad/latch.md)) | Fail-safe: the controller fires the latch release from a stored-energy reservoir on command, on loss of the keep-alive or on loss of supply, and the spring feathers the prism. No power is needed to hold either state. Torque about 14 N m at 45 m/s |
| Hinge | 25 mm stainless axle, two sealed deep-groove ball bearings (6005-2RS) 300 mm apart | Hub and post head built for 800 N m; each bearing carries ~2.5 kN at 45 m/s |
| | Rubber end stops | ±20° |
| Springs | Two compression springs, ~31 N/mm each, ~40 mm usable travel, fatigue-rated, working force up to ~1.1 kN | Carriage 15–140 mm below the hinge, T8 lead screw and NEMA-17 stepper as on 250-B |
| Drive | GT2 9 mm belt on a 100 mm-radius arc on the hub; 12-tooth pulley on the generator (26:1) | Peak tension ~160 N |
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
| Pitch drive | Drive 0–48° and back; check the gearmotor current against the spring torque | Encoder follows the command within 1°; current matches the spring (18.5 N·m at 45°, 26.2 at 0°) |
| Latch trip | Latched at β = 0, 15, 30 and 40°: remove the supply and let the board fire from its reservoir | β passes 44° within 0.5 s of the pulse, at every angle |
| Latch trip force | Latched and loaded at β = 0 (spring only): spring balance on the tab roller through the port; then the reduced-current pulse (1.33 A) | ≤ 3.8 N radial at the dynamic load (scale by the actual torque: about 2.2 N at the spring-only load); trips at 1.33 A |
| Latch re-engagement | Run the re-engagement procedure (cad/latch.md section 6) three times from the feathered stop | Latches every time; the shaft follows the wheel within 1° on the way back to 0° |
| Latch settings | Feeler gauge through the port | Sear engagement 0.15 ± 0.05 mm; hook gap 1.5 ± 0.2 mm; spring torque at 0° 26.2 N·m ± 3 % |
| Springs | Set the carriage at several positions; pluck; log the frequency | Matches the calculator's carriage table; never statically unstable (the prism must not fall over at the lowest setting) |
| Neck mode | Lock the hinge, tap the prism, log the ring-down | About 17 Hz expected; must exceed 1.5 × the top spring frequency (6 Hz) |
| Brake | Pluck, then short the generator; cut power while swinging | Swing dies within a few cycles |

## 5. Control software

- **Parked** (calm, or net output negative). Feathered to 45° by the torsion spring with the latch released, generator shorted by the normally-on brake, MCU in Stop mode, woken by anemometer pulses (about 4 mW for the board). Nothing is powered to hold this state.
- **Restart.** When the 1–2 min mean wind is above break-even with the controller's running draw (about 4 m/s at 0.2 W) **and** the battery is above its restart reserve:
  - re-engage the latch with the worm (cad/latch.md section 6; pass only if the shaft follows the wheel within 1° on the way to 0°);
  - pitch to 0°, open the brake and kick-start: drive the motor at the carriage's current frequency for a few cycles.
  - Loads are shed at a higher battery level than the restart reserve, so the controller can always restart.
- **Generating.**
  - The generator load follows maximum power: hill-climb on measured power.
  - The carriage holds the swing at ±15°: move out (stiffer) if the swing exceeds it, in if it is smaller. This one loop keeps the frequency where the model wants it.
- **Park on net power.** After about 5 min of negative net output, drive the latched shaft to 40° with the worm and fire the latch: first the 1.33 A margin-test pulse, then full current if it has not tripped in 0.5 s (log "trip margin low").
- **Rated.** Above 20 W, a slow loop on output power raises the pitch, keeping the generator load near maximum-power. Rate-limit pitch to a few degrees per second.
- **Every pitch move:** compare the gearmotor current with the expected spring torque; a drop means a broken spring: pitch to 45° latched with the worm and stay parked.
- **Feathered.** Pitch to 45° and short the generator:
  - when the 3-second gust exceeds 42 m/s or the 1-minute mean exceeds 40 m/s;
  - on over-voltage, icing risk (temperature at or below +3 °C with rain or high humidity, so the latch is released before ice can form on the trip parts), loss of the swing sensor, or a battery fault;
  - on loss of power or keep-alive (latch released from the reservoir; spring).
  - If β has not passed 44° within 0.5 s of the pulse: two more pulses 2 s apart, then feather with the worm, keep the brake on and log a fault.

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

## 7. Building 330-GH (most power from 15 to 40 m/s) instead

330-GH shares the prism, end plates, panels and post. Changes from the parts list above:

| Group | 330-GH | Why |
|---|---|---|
| Neck | 50 × 47 mm carbon, **800 mm** | Better capture; storm moment taken by the stronger hub |
| Hinge and hub | Built for **1,200 N·m**; 25 mm axle, two 6005-2RS bearings 300 mm apart (~2.9 kN each at 45 m/s) | Longer neck |
| Feather | **Two-position**: a pivot at the neck foot latched face-on by an electromagnetic latch (power to hold), with a torsion spring to a 45° stop | No pitch regulation is needed; the feather is the storm and fault stop |
| Stops and stroke | Rubber stops at **±30°**; design swing ±25° | Lower frequency, so lower spring and inertial loads at high wind |
| Springs | Two heavy die springs, **~51 N/mm, ~3 kN working force, ±45 mm travel** at the outer carriage position | Frequency up to 2.9 Hz with the larger swing |
| Drive | **HTD 8M 20 mm** belt on a **275 mm-radius** arc, 22-tooth pulley (9.8:1) | Peak tension ~475 N (~130 N·m at the hinge) |
| Generator | **Direct-drive e-bike hub motor**, ~500 W class (~0.75 V·s/rad, ~0.3 Ω) | Absorbs the full galloping load at 40 m/s: ~750 rpm, 59 V peak, 44 W of heat |
| Electronics | Rated **≥ 100 V**; MPPT converter for ~400 W peak into a 48 V battery or a dump load | |

Measure the hub motor's spin-down drag before fitting it. At ~0.25 N·m it sets the 6 m/s cut-in, and any more raises it.

```bash
python3 tools/galloping_calc.py report --config GH --gen_drag 0.4 --Ke 0.7 --R_coil 0.35   # your measured hub motor
```

## 8. Safety

- The prism swings ±15° at the hinge: about ±0.4 m at its top, 4.6 m above ground, at up to 3.7 Hz in strong wind. 330-GH swings ±25°: about ±0.76 m at its top, 4.8 m up, with ~27 g at the top at 40 m/s. Keep people and branches clear.
- The post carries about 3 kN m at its base in a 45 m/s storm. Guy it, and lower the head for all work.
- Never rely on the brake alone: the feather spring is the primary protection, the shorted generator the second.
- Belt arc, springs and carriage carry hundreds of newtons: guard them.
- Check local planning rules for a moving structure of this height.
