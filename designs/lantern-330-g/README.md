# Lantern 330-G

**The galloping version: a 330 mm square prism, 1 m tall, that swings across the wind and keeps generating from about 2.5 m/s all the way to 40 m/s.**

A square section gallops: once it moves sideways, the wind it sees comes from the side it is moving towards, and a square's side force then pushes it further the same way. There is no lock-on band to track and no Reynolds-number limit, and the output keeps rising with the wind. Above 15.5 m/s a pitch drive turns the prism a few degrees on its own axis to hold the 20 W rating. Above 40 m/s, or on any fault, a spring turns it 45° (feathered), where a square neither gallops nor pushes sideways.

The name follows the family: the number is the cross-section width in millimetres, and G is for galloping.

**Two versions share the prism:**
- **330-G** is rated 20 W and pitch-regulated. It gives the most yearly energy at ordinary sites.
- **330-GH** is built for the most power from 15 to 40 m/s ([section 11](#11-lantern-330-gh-the-most-power-from-15-to-40-ms)). It has no power cap and no pitch regulation: an e-bike hub motor on a heavy belt, a ±25° swing and heavier springs. It averages 152 W from 15 to 40 m/s and reaches 384 W at 40 m/s, but only starts at about 6 m/s.

> **Status: concept design, not built or tested.** Every number is an engineering estimate from the models in [physics.md](physics.md), reproduced by [`tools/galloping_calc.py`](../../tools/galloping_calc.py). Only the square's galloping coefficients are well established, and they come from smooth wind-tunnel flow. **Build the static side-force test in [build-and-test.md](build-and-test.md) first.**

Related documents:
- [physics.md](physics.md): the galloping model, the controller and every check
- [build-and-test.md](build-and-test.md): static side-force test, parts, build order, control software, tests, safety
- [calculator-output/](calculator-output/): report, envelope and power curve (0.5–45 m/s), sweeps, full grids
- [../lantern-250/](../lantern-250/): the vortex-shedding designs 250-A, B and C, which share the hinge, belt, spring carriage and yaw head

---

## 1. Summary

| | **330-G (galloping, rated 20 W)** | **330-GH (galloping, most power 15–40 m/s)** | 250-B (vortex shedding) | 250-C (vortex shedding, all-weather) |
|---|---|---|---|---|
| Body | 330 × 330 mm square prism, 1,000 mm tall; 10 mm glass-faced foam panels; 660 mm square end plates | same prism | Ø250 × 1,000 mm tube, 3 mm sandwich, Ø500 mm discs | Ø250 × 1,000 mm, 5 mm storm shell, Ø500 mm discs |
| Neck, hub | 600 mm, 50 × 47 mm carbon; pitch drive at the neck foot; hub built for 800 N·m on ball bearings | 800 mm, 50 × 47 mm; two-position feather (face-on or 45°); hub 1,200 N·m | 800 mm, 35 × 32 mm; hub 150 N·m | 600 mm, 35 × 32 mm; hub 350 N·m |
| Swinging mass / mass ratio | 2.2 kg / 10 | 2.4 kg / 12 | 0.63 kg / 5.5 | 0.86 kg / 7.7 |
| Generator and drive | 8108-size pancake outrunner (~100 W class), GT2 9 mm belt, 26:1; swing ±15° | Direct-drive e-bike hub motor (~500 W class), HTD 8M 20 mm belt, 9.8:1; swing ±25°; 3 kN springs | 5208 gimbal motor, 26:1 | same |
| **Generates** | **2.5–40 m/s without a gap** | **6.1–40 m/s without a gap** | 1.6–8 m/s as designed; 1.8–10.8 m/s kept generating | 1.6–8 m/s; 1.8–11 m/s kept generating |
| Electrical at 4.5 m/s | 0.40 W | 0 (below cut-in) | 2.0 W | 1.8 W |
| Electrical at 10 m/s | 5.5 W | 4.1 W | 20.5 W (kept generating) | 20.0 W (kept generating) |
| Electrical at 15–40 m/s | 18 W at 15 m/s, then **20 W held to 40 m/s** | 18 W at 15, 47 at 20, 93 at 25, 163 at 30, **384 W at 40 m/s**; **152 W average** | nothing (braked) | nothing (braked) |
| Survives | 46.7 m/s feathered and braked | 46.7 m/s | 25 m/s | 42 m/s |
| Yearly energy, 4.5 m/s-mean site | **6.2 kWh** (low case 3.1) | 2.6 | 9.1 as designed; 14.7 kept generating | 8.5; 14.0 |
| Yearly energy, 6.5 m/s-mean site | **19.0 kWh** (low case 9.5) | 14.4 | 9.5; 24.3 | 8.9; 24.1 |
| Yearly energy, 7.5 m/s-mean site | **27.8 kWh** | 25.2 | 8.6; 25.3 | 8.1; 25.5 |
| Yearly energy, 9 m/s-mean site | 42.0 kWh | **48.9** | 7.2; 24.1 | — |

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

## 11. Lantern 330-GH: the most power from 15 to 40 m/s

### Why 330-G pitches, and why 330-GH doesn't

330-G's pitch regulation exists only to hold its **20 W rating**. That rating was a choice, not a limit. It was picked because yearly energy at ordinary sites hardly depends on it: winds above 15 m/s blow for about an hour a year at a 4.5 m/s site.

At 40 m/s the same prism could deliver about 270 W through its small generator. 330-G throws away more than 90% of that so the 8108 motor and a 9 mm belt can stay small and cool.

Pitch is only worth having where some part would otherwise go past its limit. So the high-wind design asks a different question: **which parts would stop the prism delivering all its galloping power, and what does it take to upgrade them?**

The calculator answers it with the cap removed. In order, the parts that run out are:

| Part | Why it runs out | Upgrade in 330-GH |
|---|---|---|
| Generator | The best load at 40 m/s is ~16 N·m·s/rad at the hinge. An 8108 motor would lose most of its power as heat at that load, and a 5208 cannot get near it. | Direct-drive e-bike hub motor (~500 W class): torque constant ~0.75 N·m/A, so it can absorb ~180 N·m·s/rad at a 9.8:1 ratio. It runs at 750 rpm, 59 V peak and 44 W of heat at 40 m/s |
| Belt | Peak torque at the hinge reaches ~130 N·m; a 9 mm GT2 belt on a 100 mm arc would see ~1.3 kN | HTD 8M 20 mm belt on a 275 mm-radius arc: 475 N peak against ~1,100 N allowable |
| Springs and stroke | Holding the swing to ±15° needs a high frequency at 40 m/s, and spring force rises as the square of frequency | ±25° design swing (stops at ±30°) and 3 kN springs (~51 N/mm, ±45 mm travel at full stiffness); the frequency stays at or below 2.9 Hz |
| Hub and neck | A longer neck makes the prism move more evenly (capture ceiling 4.15% instead of 3.9%) but raises the storm moment | 800 mm neck, hub built for 1,200 N·m |

**With those upgrades no limit is reached below 40 m/s.** The neck peaks at 88% of its allowable and the generator speed at 93%, both at 40 m/s. So the controller never needs pitch:
- it loads the generator for maximum power;
- it moves the spring carriage to hold the swing at ±25°;
- the prism stays face-on.

Continuous pitch control would add exactly nothing (the sweep checked: 152.4 W with or without it). **330-GH replaces the pitch drive with a two-position feather:** latched face-on, released by a spring to 45° above 40 m/s, on any fault or on loss of power.

The feather still matters, for two reasons:
- **A belt or wiring failure.** The shorted hub motor alone would stop the prism galloping in any wind (its damping is about five times what it takes at 45 m/s), but only while the belt and wiring are intact.
- **Storm drag.** Feathered, the prism has 21% less drag, which the neck needs to survive 45 m/s.

### What it produces

From [calculator-output/report-330GH.md](calculator-output/report-330GH.md) and [envelope-330GH.md](calculator-output/envelope-330GH.md):

| Wind (m/s) | Swing | Frequency | Electrical | Neck | Hub | Springs | Belt | Generator heat | Closest limit |
|---|---|---|---|---|---|---|---|---|---|
| 7 | ±25° | 0.45 Hz | 0.57 W | 3% | 2% | 15% | 1% | 0 W | flow angle 79% |
| 10 | ±25° | 0.69 Hz | 4.1 W | 5% | 5% | 20% | 3% | 0.1 W | flow angle 85% |
| 15 | ±25° | 1.07 Hz | 18.3 W | 12% | 10% | 29% | 6% | 0.7 W | flow angle 88% |
| 20 | ±25° | 1.44 Hz | 46.7 W | 22% | 18% | 38% | 11% | 2.4 W | flow angle 89% |
| 25 | ±25° | 1.81 Hz | 93.5 W | 34% | 29% | 47% | 17% | 6.3 W | flow angle 89% |
| 30 | ±25° | 2.18 Hz | 163 W | 49% | 41% | 57% | 24% | 13.5 W | flow angle 90% |
| 35 | ±25° | 2.54 Hz | 258 W | 67% | 56% | 66% | 33% | 25.5 W | flow angle 90% |
| 40 | ±25° | 2.91 Hz | **384 W** | 88% | 74% | 75% | 43% | 44 W | generator speed 93% |
| 45 | feathered | — | 0 | 82% | 73% | — | — | — | end plates 93% |

The flow-angle line shows the galloping model working at its own optimum: the prism top meets the wind at about 21°, inside the range the side-force fit is trusted to.

At every wind from 15 to 40 m/s, 330-GH delivers about 3% of the wind passing the prism as electricity. That is the square's frictionless galloping ceiling (4.15% with the 800 mm neck) less belt, copper and converter losses.

**This is the most this prism can give.** More would need one of:
- a wider prism (the assumed aspect-ratio limit of 3 already sets 330 mm);
- a stronger side-force curve (the unverified triangle section could add ~25%);
- more neck and hub, at a few per cent per step.

### The price

| | 330-G | 330-GH |
|---|---|---|
| Average output, 15–40 m/s | 19.9 W | **152 W** (7.7×) |
| Output at 40 m/s | 20 W | **384 W** |
| Cut-in | 2.5 m/s | 6.1 m/s (the hub motor's drag, ~2.4 N·m at the hinge) |
| Output at 10 m/s | 5.5 W | 4.1 W |
| Hours a year above 15 m/s (Rayleigh) | 1 at a 4.5 m/s site, 380 at 7.5, 990 at 9 | same |
| Yearly energy, 4.5 / 7.5 / 9 m/s site | 6.2 / 27.8 / 42.0 kWh | 2.6 / 25.2 / **48.9** kWh |
| Post base moment, 40–45 m/s | 3.0 kN·m | 3.2 kN·m |
| Prism top swing | ±0.4 m | ±0.76 m (the top is 4.8 m up) |

Winds above 25 m/s are storm events: about an hour a year even at a 7.5 m/s-mean site, and about 20 hours at 9 m/s.

So 330-GH only makes **more energy over a year** than 330-G at very exposed sites, with a mean wind above about 8 m/s. Below that, the hub motor's drag costs more in the 3–8 m/s winds than the high-wind gain returns.

A middle option, a 6374-size outrunner on an HTD 5M belt (`--generator 6374 --belt HTD5M-15 --arc_radius 0.25 --pulley_teeth 14`), averages 117 W from 15 to 40 m/s. It starts at 3.6 m/s and gives the most yearly energy of the three at sites with a 7.5–9 m/s mean (28.8 kWh at 7.5 m/s, 50.8 kWh at 9 m/s).

### Search

`sweep --objective high` ranked 5,184 designs by average electrical power from 15 to 40 m/s, every one with no power cap. Each had to:
- generate without a gap to 40 m/s;
- keep every part within its limits;
- survive 45 m/s feathered.

Results are in [calculator-output/sweep-high-wind.md](calculator-output/sweep-high-wind.md) and [grid/grid-high-wind.csv](calculator-output/grid/grid-high-wind.csv).

| Choice | Best average, 15–40 m/s |
|---|---|
| 8108 outrunner / 6374 outrunner / hub motor | 68 / 117 / **152 W** |
| Springs 1.5 kN / 3 kN | 128 / 152 W |
| Swing ±15° / ±20° / ±25° | 146 / 152 / 152 W |
| Hub 800 N·m (600 mm neck) / 1,200 N·m (800 mm neck) | 145 / 152 W |
| Prism 300 / 330 mm | 139 / 152 W |

The top design used a 300 mm arc (10.7:1) with continuous pitch, and reached its generator's speed limit just below 40 m/s. A 275 mm arc (9.8:1) gives the same average without ever pitching, so that is 330-GH.

---

## 12. Reproducing the numbers

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

```bash
python3 tools/galloping_calc.py report --config GH               # 330-GH, the most power from 15 to 40 m/s
```

```bash
python3 tools/galloping_calc.py curve --config GH --compare      # 330-GH power 1-40 m/s with 250-B and 250-C
```
