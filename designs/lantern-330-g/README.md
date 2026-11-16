# Lantern 330-G

**The galloping version: a 330 mm square prism, 1 m tall, that swings across the wind and keeps generating from about 2.5 m/s all the way to 40 m/s.**

A square section gallops: once it moves sideways, the wind it sees comes from the side it is moving towards, and a square's side force then pushes it further the same way. There is no lock-on band to track and no Reynolds-number limit, and the output keeps rising with the wind. Above 15.5 m/s a pitch drive turns the prism a few degrees on its own axis to hold the 20 W rating. Above 40 m/s, or on any fault, a spring turns it 45° (feathered), where a square neither gallops nor pushes sideways.

The name follows the family: the number is the cross-section width in millimetres, and G is for galloping.

> **Status: concept design, not built or tested.** Every number is an engineering estimate from the models in [physics.md](physics.md), reproduced by [`tools/galloping_calc.py`](../../tools/galloping_calc.py). Only the square's galloping coefficients are well established, and they come from smooth wind-tunnel flow. **Build the static side-force test in [build-and-test.md](build-and-test.md) first.**

Related documents:
- [physics.md](physics.md): the galloping model, the controller and every check
- [build-and-test.md](build-and-test.md): static side-force test, parts, build order, control software, tests, safety
- [calculator-output/](calculator-output/): report, envelope and power curve (0.5–45 m/s), sweeps, full grids
- [../lantern-250/](../lantern-250/): the vortex-shedding designs 250-A, B and C, which share the hinge, belt, spring carriage and yaw head

---

## 1. Summary

| | **330-G (galloping)** | 250-B (vortex shedding) | 250-C (vortex shedding, all-weather) |
|---|---|---|---|
| Body | 330 × 330 mm square prism, 1,000 mm tall; 10 mm glass-faced foam panels; 660 mm square end plates | Ø250 × 1,000 mm tube, 3 mm sandwich, Ø500 mm discs | Ø250 × 1,000 mm, 5 mm storm shell, Ø500 mm discs |
| Neck, hub | 600 mm, 50 × 47 mm carbon; pitch drive at the neck foot; hub built for 800 N·m on ball bearings | 800 mm, 35 × 32 mm; hub 150 N·m | 600 mm, 35 × 32 mm; hub 350 N·m |
| Swinging mass / mass ratio | 2.2 kg / 10 | 0.63 kg / 5.5 | 0.86 kg / 7.7 |
| Generator | 8108-size pancake outrunner (~100 W class), 26:1 belt | 5208 gimbal motor, 26:1 | same |
| **Generates** | **2.5–40 m/s without a gap** | 1.6–8 m/s as designed; 1.8–10.8 m/s kept generating | 1.6–8 m/s; 1.8–11 m/s kept generating |
| Electrical at 4.5 m/s | 0.40 W | 2.0 W | 1.8 W |
| Electrical at 10 m/s | 5.5 W | 20.5 W (kept generating) | 20.0 W (kept generating) |
| Electrical at 15–40 m/s | 18 W at 15 m/s, then **20 W held to 40 m/s** | nothing (braked) | nothing (braked) |
| Survives | 46.7 m/s feathered and braked | 25 m/s | 42 m/s |
| Yearly energy, 4.5 m/s-mean site | **6.2 kWh** (low case 3.1) | 9.1 as designed; 14.7 kept generating | 8.5; 14.0 |
| Yearly energy, 6.5 m/s-mean site | **19.0 kWh** (low case 9.5) | 9.5; 24.3 | 8.9; 24.1 |
| Yearly energy, 7.5 m/s-mean site | **27.8 kWh** | 8.6; 25.3 | 8.1; 25.5 |

**What this says, on the model's central figures:**

- **Galloping is the only way here to generate above about 11 m/s.** The vortex tubes stop there whatever the control: generator heat, the neck's bending mode and the drag crisis. 330-G delivers its full rating from 15.5 m/s to 40 m/s.
- **Below about 11 m/s the vortex tube is far better.** A light round tube tuned to the wind captures 15–20% of the wind passing it. A galloping square captures at most about 4% (the frictionless ceiling for this geometry), so at 4.5 m/s it makes a fifth of 250-B's output despite being 30% wider.
- **Which wins depends on the site.**
  - Against 250-B as designed (braking at 8 m/s), 330-G makes more energy wherever the mean wind is above about 5 m/s.
  - Against 250-B kept generating to 11 m/s (an option that runs the round tube in untested flow), 330-G only pulls ahead above about a 7 m/s mean.
  - At a 4.5 m/s site, winds above 11 m/s give 330-G only a tenth of its energy. At a 6.5 m/s site they give nearly half.
- **Galloping has practical virtues the numbers don't show.**
  - Output does not depend on mass, so the prism is built sturdy (10 mm panels, mass ratio 10).
  - The controller has no narrow band to find: it holds the swing at ±15° and the generator at maximum power.
  - It can be **switched off aerodynamically**: feathered, it is stable however the brake behaves.
  - Sharp corners make it insensitive to Reynolds number.
- **The biggest unknown is turbulence.** If ground-level gusts cut the side-force slope A1 by 20%, yearly energy falls about 40% (to 3.7 kWh at a 4.5 m/s site). That is why the static test comes first.

For scale: a 100 W solar panel gives roughly 90–150 kWh a year. Like the rest of the project, this is a physics and mechanism experiment.

```bash
python3 tools/galloping_calc.py curve --compare     # 330-G against 250-B and 250-C, 1-40 m/s
```

The same curves, with a "Compare with" overlay, are on the [Lantern Design Grid page](https://claude.ai/artifact/7coCWJAdK3jhA8j6H4RN1b) (private until shared).

---

## 2. Brief

- Same envelope as Lantern 250: 1 m of swinging body, everything else free.
- **Keep generating from light wind all the way to 40 m/s**, with every part within its limits at every wind speed.
- Survive gusts above the 40 m/s cut-out: requirement 45 m/s, feathered and braked.
- Buildable at home: foam and glass, carbon tube, hobby motors and electronics, a steel post.

---

## 3. Why it looks like this

1. **Galloping, because it has no upper band.** Vortex shedding only drives a tube near its tuned frequency, and above ~11 m/s nothing holds together. A galloping body is driven by its own motion, so it works at any wind above onset, and quasi-steady theory gets *more* reliable as the wind rises.
2. **A square, because its coefficients are known.** For a square in smooth flow, A1 = 2.3 and A3 = 18 are well established. Literature values for other sections could not be verified:
   - With the quoted values for a 30° isosceles triangle, the same geometry would make about 25% more energy (7.9 kWh at a 4.5 m/s site), but cut in later (4 m/s). With a guessed parked drag of 1.9 it would also fail the 45 m/s survival check.
   - The quoted D-section values are too weak to beat friction at all.

   The triangle is worth putting on the static rig next to the square (`--section-preset triangle-30`).
3. **Mass doesn't matter, so build it strong.** In quasi-steady galloping the power depends only on the aerodynamics, the friction and the generator load, not on the mass. The prism uses 10 mm glass-faced foam and 660 mm end plates without losing output. Mass still sets inertial loads and the neck's bending frequency, which the calculator checks.
4. **Wide, up to an assumed aspect-ratio limit.** Output scales with face width and there is no Reynolds-number cap for sharp corners. The sweep pushes the width to the assumed minimum aspect ratio of 3 (330 mm on a 1 m prism). Allowing 2.5 adds only 5%, because the end plates then limit storm survival.
5. **A neck, for the same reason as on 250-B.** Hinging 600 mm below the prism makes its bottom move almost as fast as its top. That brings the capture ceiling from 56% to 80% of a prism moving bodily sideways.
6. **Frequency set by the swing, not by the wind.** Power doesn't depend on swing frequency, but swing angle, inertial loads and fatigue do. The controller picks the lowest frequency that keeps the swing at the design ±15°. That puts U/(fD) at about 22 at every wind, where the theory holds. It runs from 0.37 Hz at 3 m/s to 3.7 Hz at 40 m/s.
7. **Pitch to regulate, feather to stop.** Turning a square a few degrees about its own axis weakens its galloping steeply: the effective slope is A1 − 3 A3 β², zero at 11.8°. At 45° it is stable and the side force vanishes by symmetry. This is the galloping equivalent of blade pitch control on a turbine.
8. **A bigger generator, a stronger hub, ball bearings.**
   - The rated load at the hinge (~4.5 N·m·s/rad) needs a ~100 W-class motor. The 5208 gimbal motor overheats before it can hold 20 W.
   - Storm drag on a 330 mm square sets the hub at 800 N·m.
   - The swing is always about ±15°, so sealed ball bearings replace the polymer bushings without the false-brinelling risk of small rocking motions.

---

## 4. General arrangement

```
          ┌───────────────┐   end plate 660 × 660 (10 mm glass-faced foam)
          │ ┌───────────┐ │
          │ │           │ │   square prism 330 × 330 × 1000
          │ │ ─ ─ ─ ─ ─ │ │   four flat panels, bulkheads every 250 mm
 wind →   │ │           │ │   face-on to the wind when generating,
          │ │ ─ ─ ─ ─ ─ │ │   turned 45° (feathered) above 40 m/s
          │ │           │ │
          │ └─────┬─────┘ │   swings ±15° across the wind
          └───────┼───────┘
                  │          neck: 600 mm, 50 × 47 mm carbon tube
             ┌────┴────┐     pitch drive: neck foot turns in two bearings,
             │  PITCH  │     worm gearmotor; spring + clutch feather it on power loss
        ┌────┴────●────┴────┐ hinge: 25 mm axle INTO the wind, two 6005-2RS bearings
        │  ◄▮▮══╪══▮▮►      │ 300 mm apart; hub built for 800 N·m
        │       │           │ spring carriage 15–140 mm below hinge (0.12–4 Hz)
        │   ⌒ arc R100 ⌒    │ GT2 belt → 12-tooth pulley → 8108 generator (26:1)
        │     [GEN]         │
        └────────┬──────────┘
     tail vane ◄═╪   yaw bearing
                 │   guyed steel post, hinge ~3 m above ground
```

View from the side, wind from the left; in operation the prism rocks in and out of the page.

---

## 5. Parts, masses and inertia

From [calculator-output/report-330G.md](calculator-output/report-330G.md).

| Part | Construction | Mass |
|---|---|---|
| Prism | Four 330 × 1,000 mm panels of 10 mm extruded polystyrene with ~25 g/m² glass tissue in epoxy on both faces; outer skin built up to ~0.15 mm near the base; three internal bulkheads (half weight, lightening holes); glass tape on the corners | 0.71 kg |
| End plates, each | 660 mm square, same panel | 0.20 kg |
| Bottom spider | Neck socket in the bottom bulkhead | 0.02 kg |
| Neck | 50 × 47 mm roll-wrapped carbon tube, 600 mm | 0.21 kg |
| Hub assembly | 25 mm axle, two bearings, spring lever and carriage, belt arc, pitch bearings, gearmotor, return spring and clutch | ~0.87 kg |
| **Total swinging** | | **2.22 kg** |

| Inertia about the hinge (kg·m²) | |
|---|---|
| Prism | 0.92 |
| End plates | 0.60 |
| Neck, spider, hub | 0.04 |
| Generator rotor through the 26:1 belt | 0.17 |
| Air moving with the prism | 0.16 |
| **Total** | **1.89** |

---

## 6. Operating modes from calm to 45 m/s

| Wind | Mode | What happens |
|---|---|---|
| Below ~2.5 m/s | Idle | Face-on, generator open. Too little wind to beat bearing and generator drag |
| 2.5–15.5 m/s | **Generating** | Kick-start at onset. Generator load tracks maximum power. Carriage moves to keep the swing at ±15°: 0.37 Hz at 3 m/s, 2 Hz at 15 m/s. Output 0.06 W at 3 m/s, 0.40 W at 4.5, 5.5 W at 10, 18 W at 15 |
| 15.5–40 m/s | **Rated (pitch-regulated)** | Pitch rises from 0 to 10° to hold 20 W, with the generator near maximum-power load. Swing falls from ±15° to ±9° as a steady lean (up to 6°) takes up part of the stroke; frequency rises to 3.7 Hz |
| Above 40 m/s, or on fault | **Feathered** | Pitch to 45° and generator shorted. The spring and clutch do this without power |
| To 46.7 m/s | Survive | Limited by the end plates' gust lift; the hub is at 47 m/s |

From [calculator-output/envelope-330G.md](calculator-output/envelope-330G.md) (utilisation = load ÷ allowable):

| Wind (m/s) | Mode | Pitch | Swing | Frequency | Electrical | Neck | Fatigue | Hub | Springs | Worst |
|---|---|---|---|---|---|---|---|---|---|---|
| 3 | generating | 0° | ±15° | 0.37 Hz | 0.06 W | 0% | 0% | 1% | 10% | quasi-steady 82% |
| 4.5 | generating | 0° | ±15° | 0.60 Hz | 0.40 W | 1% | 1% | 1% | 14% | quasi-steady 88% |
| 10 | generating | 0° | ±15° | 1.37 Hz | 5.45 W | 5% | 6% | 6% | 27% | quasi-steady 90% |
| 15 | generating | 0° | ±15° | 2.06 Hz | 18.1 W | 12% | 13% | 13% | 39% | quasi-steady 91% |
| 20 | rated | 6.6° | ±12.6° | 2.60 Hz | 20.0 W | 18% | 17% | 20% | 49% | quasi-steady 86% |
| 30 | rated | 9.2° | ±10.4° | 3.12 Hz | 20.0 W | 34% | 20% | 41% | 59% | quasi-steady 69% |
| 40 | rated | 10.0° | ±8.8° | 3.66 Hz | 20.0 W | 57% | 24% | 71% | 69% | end plates 73% |
| 45 | feathered | 45° | — | — | 0 | 69% | — | 93% | — | end plates 93% |

The quasi-steady line shows how close the swing frequency is to the highest at which the galloping theory is trusted. The controller's frequency rule keeps it below 100%.

---

## 7. Structure

| | Feathered at 45 m/s | Generating at 40 m/s |
|---|---|---|
| Drag on the prism | 675 N | 517 N |
| Moment at the hinge (hub built for 800 N·m) | 743 N·m | 569 N·m |
| Neck stress (allowable 400 MPa) | 276 MPa | — |
| Panel bending (capacity 20 N·m/m) | 10.9 N·m/m | — |
| End-plate gust utilisation | 93% | 73% |
| Each hinge bearing | 2.5 kN | — |
| Spring force | — | 1.03 kN (limit 1.5 kN) |
| Post base moment, hinge at 3 m | **3.0 kN·m** | 2.3 kN·m |
| Pitch-drive torque | ~13.5 N·m | — |

The post needs proper engineering: for example a 114 mm × 6 mm steel tube with guys, sized to your local wind code.

**Panel options tried by the sweep:**
- 5 mm glass-faced foam fails at the prism base: too little outer skin.
- 4 mm twin-wall polypropylene ("corflute") fails panel bending at 45 m/s with bulkheads every 250 mm. With bulkheads every 200 mm it passes every check and gives 6.1 kWh at a 4.5 m/s site, within 2% of the foam version. It is a cheap, weatherproof option worth trying on the static rig (`--shell corflute4 --bulkhead_pitch 0.2`).

---

## 8. Drive, generator and electronics

- **Belt:** GT2 from a 100 mm-radius arc on the hub to a 12-tooth pulley: 26.2:1.
- **Generator:** 8108-size pancake outrunner, ~100 W class, wound for about 0.2 V·s/rad. The calculator assumes 0.8 Ω, 0.01 N·m drag and a 20 W heat limit (measure yours).
  - At its busiest (around 15–17 m/s) it peaks at about 1,200 rpm and 26 V EMF, and never dissipates more than 4 W.
  - Its drag through the belt (0.26 N·m at the hinge) is most of the friction that sets the 2.5 m/s cut-in.
- **Electronics:**
  - Three-phase active bridge (rectifies, and motors for the kick-start), with maximum-power tracking into a 24 V LiFePO₄ battery.
  - Normally-closed brake.
  - Pitch motor driver and encoder, hinge angle encoder (swing amplitude is the carriage loop's input), anemometer, temperature sensor, logging.
  - Rate everything to at least 60 V.

---

## 9. Optimisation

Two grid searches with `tools/galloping_calc.py sweep`. Every design had to:
- generate without a gap from 10 m/s to the 40 m/s cut-out;
- reach its 20 W rating by 25 m/s and hold it to 40 m/s;
- survive 45 m/s feathered.

Designs were ranked by yearly energy at a 4.5 m/s site. Full results are in [calculator-output/](calculator-output/), every grid point in [calculator-output/grid/](calculator-output/grid/).

| Search | Grid | Pass | Best |
|---|---|---|---|
| Wide | D 200–325 mm, neck 0–800 mm, end plates 1.5–2.0 × D, four panel types, 10/12/16 teeth, both generators, hubs 500 and 800 N·m: 4,320 designs | 750 | 325 mm, 600 mm neck, 2.0 × plates, 10 mm panels, 8108, 12 teeth, 800 N·m: 6.07 kWh |
| Fine | D 300–330 mm, neck 400–800 mm, plates 1.75–2.0, two panel types, 10–16 teeth, spring tops 3/4/6 Hz, 800 N·m: 960 designs | 475 | 320 mm with 700 mm neck: 6.18 kWh; **330 mm with 600 mm neck: 6.17 kWh** (chosen: shorter, more storm margin) |

What the searches showed:

| Finding | Effect |
|---|---|
| Hub strength is the main lever | Best with a 500 N·m hub: 4.2 kWh. With 800 N·m: 6.1 kWh. A 1,200 N·m hub adds only 5%, because the end plates then limit survival |
| The 5208 gimbal motor | Starts lower but overheats: no 5208 design holds 20 W to 40 m/s |
| Wider is better up to the aspect-ratio limit | 300 mm: 5.9 kWh; 330 mm: 6.2 kWh. Relaxing the limit to 2.5 adds ~5% |
| Spring range top | 3 or 4 Hz equally good; 6 Hz raises the lowest frequency and the cut-in |
| Gear ratio | 10–14 teeth within 2%: more teeth start lower, fewer hold the rating more easily |

As with the vortex designs, the optimiser presses against the edges of the model: here the assumed aspect-ratio limit and the hub rating. Treat the result as the shape to test, not a guarantee.

---

## 10. Risks and unknowns

1. **Turbulence near the ground.** Smooth-flow coefficients may overstate the galloping drive. Each 10% off A1 costs about 20% of yearly energy.
2. **The side-force curve at large angles** and any hysteresis. The prism top reaches ~21° of flow angle at the best load; the cubic fit is trusted to 23°.
3. **Finite span.** A 1 m prism with 660 mm end plates is assumed to behave two-dimensionally; the end-plate benefit comes from an assumed end-loss model.
4. **The feathered state.** It assumes the 45° diamond is galloping-stable with Cd 1.65. Some studies report vortex-induced vibration at 45°; the shorted generator damps it. Check this in the static test.
5. **Lean under pitch.** The steady side force while pitched leans the prism up to 6°. The time-domain check suggests the real lean is about 20% smaller than the calculator's.
6. **Generator constants.** The 8108 values are typical for the class, not measured.
7. **Post and foundation.** A 3 kN·m base moment is a real structure. Use a tilt-down guyed post and local wind-code checks.

---

## 11. Reproducing the numbers

```bash
python3 tools/galloping_calc.py                                  # full report for 330-G
```

```bash
python3 tools/galloping_calc.py envelope --from 0.5 --step 0.5 --to 45   # every limit, every wind
```

```bash
python3 tools/galloping_calc.py curve --compare                  # power 1-40 m/s with 250-B and 250-C
```

```bash
python3 tools/galloping_calc.py report --turb_factor 0.8         # turbulence sensitivity
```

```bash
python3 tools/galloping_calc.py sweep --hubs 500,800 --csv grid.csv   # grid search (about 10 minutes on 4 cores)
```
