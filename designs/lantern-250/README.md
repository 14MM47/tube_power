# Lantern 250

**A 1 m tall bladeless wind generator: a light 250 mm foam drum that swings in the wind and drives one small generator through a toothed belt.** It generates from about 2 m/s to 8 m/s. Configuration C survives 40 m/s.

The name comes from its look: a thin, pale cylinder with a disc at each end, like a paper lantern on a stick. The number is the tube diameter in millimetres.

> **Status: concept design, not built or tested.** Every number here is an engineering estimate from the models in [physics.md](physics.md), reproduced by [`tools/lantern_calc.py`](../../tools/lantern_calc.py). The low case assumes real gusty wind halves the model's output.

Related documents:
- [physics.md](physics.md): the models, equations and their limits
- [build-and-test.md](build-and-test.md): build order, test plan, safety
- [calculator-output/](calculator-output/): saved reports, wind envelopes (1–40 m/s) and optimisation runs
- [../../docs/design-history.md](../../docs/design-history.md): the designs that led here
- [../../research/](../../research/): the research this rests on

---

## 1. Summary

| | **B: best output** | **C: all-weather (unattended)** | A: first version |
|---|---|---|---|
| Use | Attended, or lowered for storms over 25 m/s | Left up year-round, survives 40 m/s | Reference |
| Tube | Ø250 × 1,000 mm, 3 mm foam, glass both faces | Ø250 × 1,000 mm, 5 mm foam, glass both faces, outer skin thickened near the base | as B |
| End discs | Ø500 mm, built like the shell | Ø500 mm, built like the shell | Ø400 mm |
| Neck (hinge to tube bottom) | 800 mm, 30 × 28 mm carbon | 600 mm, 35 × 32 mm carbon | 400 mm, 25 × 23 mm |
| Hub and hinge | 12 mm axle, bushings 150 mm apart, built for 150 N·m | 16 mm axle, bushings 200 mm apart, built for 350 N·m | 10 mm axle, 100 mm apart, 150 N·m |
| Drive | GT2 belt, 26:1 (12-tooth pulley) | same | 19.6:1 (16-tooth) |
| Generator | 5208-size brushless gimbal motor | same | same |
| Swinging mass / mass ratio | 0.55 kg / 5.3 | 0.86 kg / 7.7 | 0.45 kg / 4.7 |
| Generates | 1.6–8 m/s | 1.6–8 m/s | 1.6–8 m/s |
| **Electrical at 4.5 m/s** | **2.0 W** (low case 1.0) | **1.8 W** (low case 0.9) | 1.6 W (low case 0.8) |
| Electrical at 7 m/s (rated) | 7.4 W | 7.0 W | 5.9 W |
| Survives, parked and braked | **25 m/s** (limited by hub) | **42 m/s** (limited by hub) | 30 m/s (limited by hub) |
| Energy at a 4.5 m/s-mean site | ~9 kWh/yr (low case ~5) | ~8.5 kWh/yr (low case ~4) | ~7 kWh/yr (low case ~4) |

B and C came out of grid searches over tens of thousands of designs: B with a 25 m/s survival requirement, C with 40 m/s ([section 13](#13-optimisation-results)). A is the version first worked out in conversation, with every later correction applied.

For scale: a 100 W solar panel gives roughly 90–150 kWh a year. The Lantern is a physics and mechanism project, not a cheaper source of energy.

**To check any design at every wind speed from calm to 40 m/s:**

```bash
python3 tools/lantern_calc.py envelope --config C
```

---

## 2. Design brief

- Tube height limited to 1 m. Nothing else fixed: diameter, material, mounting, transducer and energy-transfer method all free.
- Maximise electrical output at realistic domestic winds (2–8 m/s at about 3 m above ground).
- Handle the full range from about 2 m/s to 40 m/s: generate where it can, protect itself where it can't, and survive the rest.
- Buildable at home with model-making materials and common 3D-printer and hobby-electronics parts.

---

## 3. Why it looks like this

The design follows from first principles, not from copying the commercial oscillating mast.

1. **Only diameter adds wind.** The wind power passing a tube is ½ρU³·D·L. With L fixed at 1 m, a fatter tube catches proportionally more.
2. **Mass ratio is what limits a vibrating tube in air.** Mass ratio is tube mass divided by the mass of air it displaces. In air it is normally in the hundreds, and then even small friction swamps the useful damping. Efficiency falls as 1/(1 + 1.07 × mass ratio × friction damping)^5.7 ([physics.md §6](physics.md#6-optimum-generator-load-and-efficiency)). Skin mass grows with diameter but displaced air grows with diameter squared, so **a fat, light tube has a low mass ratio**: about 5 here, against about 70 for a 40 mm carbon mast and 217 for 40 mm PVC pipe.
3. **A low mass ratio fixes the other problems at once.**
   - The best generator damping ratio rises to ~0.03, so ordinary bushing and generator friction (~0.007) costs little.
   - The swing frequency can stretch by roughly 20% to follow the wind (Govardhan & Williamson's low-mass-ratio result), so tuning is forgiving.
4. **Reynolds number caps the diameter.** The best measured efficiencies for oscillating cylinders (Michigan's VIVACE, 22–28%) were at Reynolds numbers of 30,000–120,000. A 250 mm tube reaches 117,000 at 7 m/s. Larger diameters are untested ground ([section 13](#13-optimisation-results)).
5. **A tube only four diameters tall needs end discs.** They stop air spilling round the ends and weakening the vortices.
6. **A neck makes the swing more even along the tube.** With the hinge below the tube, the bottom moves almost as much as the top, so more of the tube works near its best amplitude. An 800 mm neck reaches 85% of the output of perfectly parallel motion, against 56% for a hinge at the tube's base.
7. **Low frequency and high torque favour gearing.** The tube swings at 1.6–6 Hz with up to ~5 N·m at the hinge, ten times the torque of a slim mast. A belt to a small rotary generator beats a direct magnet-and-coil generator at this size, and the mechanical losses are a small share.
8. **One swing axis, aligned by a tail vane.** A single generator can only resist motion along one axis. A vane keeps the hinge axle pointing into the wind so the tube always swings across it. This also matches the one-axis setup used in almost all published tests.
9. **Generate over a narrow band, survive a wide one.** At 40 m/s the wind passing the tube carries about 10 kW, and every load grows with the square of wind speed. So the machine harvests up to about 8 m/s and then brakes. Strength for storms comes from a stiffer shell wall, a stronger neck and hub, and nothing that has to keep working.

---

## 4. General arrangement

```
            ┌─────────┐   end disc Ø500
            │░░░░░░░░░│
            │░░░░░░░░░│   tube Ø250 × 1000
            │░░░░░░░░░│   foam core with glass on both faces,
   wind →   │░░░░░░░░░│   internal rings
            │░░░░░░░░░│
            │░░░░░░░░░│   swings ±~7° across the wind
            └────┬────┘   end disc + bottom spider
                 │
                 │        neck: 800 mm (B) / 600 mm (C) carbon tube
                 │
        ┌────────●────────┐  hinge: axle points INTO the wind
        │  ◄▮▮══╪══▮▮►    │  spring carriage 40–140 mm below hinge (tuning)
        │       │         │
        │   ⌒ arc R100 ⌒  │  GT2 belt → 12-tooth pulley → generator (26:1)
        │      [GEN]      │
        └────────┬────────┘
     tail vane ◄═╪  yaw bearing
                 │  guyed post, hinge ~3 m above ground
```

View is from the side, wind from the left. In operation the tube rocks in and out of the page.

---

## 5. Parts, masses and inertia

| Part | B | C |
|---|---|---|
| Tube shell (incl. rings, seams) | 3 mm extruded polystyrene (model-aircraft foam, ~37 kg/m³), ~25 g/m² glass tissue in epoxy **on both faces**: 0.186 kg | 5 mm foam, glass both faces, outer skin built up to ~0.15 mm effective at the base and tapering upward: 0.285 kg |
| End discs, each | Ø500 mm, same construction as the shell: 0.041 kg | Ø500 mm, 5 mm sandwich: 0.056 kg |
| Bottom spider | 0.015 kg | 0.015 kg |
| Neck | 30 × 28 mm carbon, 800 mm: 0.113 kg | 35 × 32 mm carbon, 600 mm: 0.147 kg |
| Hub assembly | ~0.15 kg | ~0.30 kg (16 mm axle, wider bushings) |
| **Total swinging mass** | **0.547 kg** | **0.859 kg** |

| Inertia about the hinge (kg·m²) | B | C |
|---|---|---|
| Shell | 0.329 | 0.369 |
| End discs | 0.162 | 0.165 |
| Spider, neck, hub | 0.035 | 0.025 |
| Generator rotor seen through the 26:1 belt | 0.041 | 0.041 |
| **Structural total** | **0.567** | **0.600** |
| Air moving with the tube | 0.107 | 0.078 |
| **Total** | **0.674** | **0.678** |
| Mass ratio | **5.3** | **7.7** |

---

## 6. Operating modes and the wind envelope

The controller chooses a mode from the wind speed (2-minute average for tuning, a few seconds for braking):

| Wind | Mode | What happens |
|---|---|---|
| Below ~1.6 m/s | Idle | Not enough wind to keep the tube swinging. Electronics asleep, carriage parked at its stiffest |
| ~1.6–2 m/s | Tracking (lower edge) | Carriage at its softest; lock-on reaches about 20% below the tuned speed |
| 2–7 m/s | **Tracking** | Carriage moved about 20 mm per 1 m/s to keep the tube tuned. MPPT controller sets the generator load for the most power |
| 7–8 m/s | **Power-capped** | Carriage held at its stiffest. Controller raises the generator load to hold output at the 7 m/s value (7.4 W for B), which shrinks the swing |
| 8 m/s and above | **Braked** | Generator phases shorted (or through a braking resistor). Carriage at its stiffest. Above about 8.4 m/s the vortices can't lock on to the tube in any case |
| Up to 25 m/s (B) or 42 m/s (C) | Survive | Braked and parked. Structure carries drag and gust loads |

**Starting.** At 2 m/s the wind's initial push on a still tube is only ~0.2 N·m. Generator drag (~0.1 N·m at the hinge) plus cogging (~0.13 N·m) is about the same. So the controller **kick-starts**: the active rectifier is a three-phase bridge, so it can briefly drive the motor and push the tube into swinging. With kick-start, cut-in is about 1.6 m/s; without it, about 2.1 m/s (B) or 2.3 m/s (C). Light winds add little energy (extending tuning from 3 down to 2 m/s adds about 0.1 kWh a year), so this matters more for responsiveness than output.

**Why brake at 8 m/s, not higher.**
- Above 7 m/s the flow is beyond the tested evidence (Reynolds number over 120,000).
- Holding power at the 7 m/s value means extra generator load, which heats the windings. The model reaches the assumed 5 W limit near 8.4 m/s.
- If left to run at full output, the loads climb fast. For B at 10 m/s: about 20 W, but a 155 N·m cyclic bending moment in the neck (it is 75 N·m at 7 m/s), 54 g at the top of the tube and 59 V peak.

**Configuration B envelope** (excerpt from [calculator-output/envelope-B.md](calculator-output/envelope-B.md)). Utilisation is load divided by allowable; over 100% fails.

| Wind (m/s) | Mode | Swing | Electrical | Top accel. | Neck fatigue | Worst part |
|---|---|---|---|---|---|---|
| 2 | tracking | ±5.3° | 0.13 W | 1.7 g | 4% | voltage 6% |
| 4.5 | tracking | ±6.5° | 2.01 W | 10.6 g | 24% | neck fatigue 24% |
| 7 | tracking | ±6.7° | 7.41 W | 26.4 g | 59% | neck fatigue 59% |
| 7.5 | power-capped | ±5.2° | 7.41 W | 23.7 g | 53% | generator heat 59% |
| 10 | braked | — | 0 | — | — | hub 16% |
| 20 | braked | — | 0 | — | — | hub 64% |
| 25 | braked | — | 0 | — | — | **hub 100%** |
| 30 | braked | — | 0 | — | — | **hub 143%: fails** |

**Configuration C envelope** (excerpt from [calculator-output/envelope-C.md](calculator-output/envelope-C.md)):

| Wind (m/s) | Mode | Electrical | Neck | Skin | Wall (ovalling) | Discs | Hub |
|---|---|---|---|---|---|---|---|
| 4.5 | tracking | 1.84 W | 7% | 6% | 1% | 1% | 2% |
| 7 | tracking | 6.97 W | 18% | 15% | 2% | 3% | 5% |
| 20 | braked | 0 | 16% | 12% | 19% | 21% | 23% |
| 30 | braked | 0 | 36% | 28% | 43% | 47% | 52% |
| 40 | braked | 0 | 64% | 50% | 77% | 84% | 92% |

C's per-part survival winds: hub 42, discs 44, wall 46, neck 50, skin 57 m/s.

**Correction to the earlier version of this document.** It said a round tube "drops out of lock-on above about 1.2 × the tuned speed and protects itself". At a mass ratio of 4–8 the lock-on band is wider than in typical air tests. That helps harvesting, but it means the tube cannot be relied on to stop itself. **Protection comes from the brake and the stiff carriage setting.** The rule that the brake must engage when power is lost (fail-safe) follows from this.

---

## 7. Structure

Survival case: parked and braked, drag coefficient 1.2 at every wind speed (no credit taken for the lower drag of the "drag crisis" above Re ≈ 200,000).

| At the survival wind | B at 25 m/s | C at 40 m/s |
|---|---|---|
| Drag on the tube | 115 N | 294 N |
| Bending moment at the tube base | 57 N·m | 147 N·m |
| Bending moment at the hinge | 149 N·m (hub built for 150) | 323 N·m (hub built for 350) |
| Neck stress (allowable 400 MPa) | 234 MPa | 255 MPa |
| Skin stress at the tube base (allowable 40 MPa) | 23 MPa | 20 MPa |
| Shell ovalling, demand / wall capacity | 3.0 / 6.0 N·m/m | 7.7 / 10.0 N·m/m |
| End-disc gust lift, utilisation | 55% | 84% |
| Load on each hinge bushing | ~1,000 N | ~1,600 N |
| Post base moment, hinge at 3 m | ~550 N·m | ~1,360 N·m |

Points to note:
- **The shell needs glass on both faces.** At 40 m/s the sides of the tube see about −2 kPa of suction, and the windward face +1 kPa, which squeezes the tube oval. A single-skin foam wall has little resistance to that. With an outer skin only, B would survive just 15 m/s (wall and discs both limit). The inner skin adds about 40 g to B's shell and costs ~2% of output.
- **End discs see gust lift.** A ~10° gust hitting a 500 mm disc pushes it with ~210 N at 40 m/s. Discs are built like the shell wall, and C's 5 mm sandwich keeps them at 84% of capacity.
- **The neck must be a tube, not thin rods.** Three 4 mm carbon rods (the first idea) would buckle in about 10 m/s of wind. The calculator's grid search picks the lightest standard tube that survives the storm requirement and the swing fatigue.
- **Neck fatigue governs while swinging.** The swing bends the neck about 3 × 10⁷ times a year. For B the cyclic stress peaks at 59% of the assumed 200 MPa allowable, at 7 m/s.
- **Never lock the hinge rigidly in a storm.** Locked, the neck and tube vibrate at about 11 Hz, and vortices match that at about 13 m/s. Leave the hinge on its springs, with the generator braked.
- **Drag acts along the hinge axle**, not about it, because the axle points into the wind. It loads the bushings, hub and post, not the springs.
- **The post** must be designed to local wind codes for the moments above. For C, use a guyed post.

---

## 8. Hinge, yaw head and mounting

- **Hinge:** single axis on polymer plain bushings, not ball bearings: the small rocking angle damages ball bearings over time (the balls dent the races without rolling far).
  - B: 12 mm stainless axle, bushings 150 mm apart; friction ~0.10 N·m at 4.5 m/s, about 5% of the harvesting torque.
  - C: 16 mm axle, bushings 200 mm apart.
- **Axle orientation:** pointing into the wind, so the tube swings across it.
- **Yaw head:** a yaw bearing at the post top with a tail vane on a ~0.6 m boom (0.05–0.1 m² of vane) keeps the axle aligned. The vane sits below the tube in clean air. Add some yaw friction or damping so gusts don't slew the head violently.
- **Height:** hinge about 3 m above ground. Power rises with the cube of wind speed, so higher is better.
- **Cables:** a slip ring at the yaw bearing, or let the cable twist with an untwist routine.
- **End stops:** rubber, at ±14°.

---

## 9. Tuning

The tube must be tuned so its swing frequency matches the vortex-shedding frequency at the current wind.

**Rule:** still-air natural frequency f_n = U ÷ (5.5 × D), which is 0.73 × U for D = 0.25 m. The 5.5 is the reduced velocity U/(f_n·D) where power peaks; calibrate it on the real rig.

**Mechanism:**
- Two opposing springs act on a carriage that slides along a lever below the hinge.
- Their stiffness about the hinge is 2 × spring rate × r², where r is the carriage's distance from the hinge. So frequency rises in proportion to r, and **the carriage position is a linear wind-speed scale**.
- Springs: two, each **17.7 N/mm** for B (17.8 for C, 8.0 for A), preloaded more than their travel at the ±14° stops (~35 mm at r = 140 mm).
- Carriage drive: T8 lead screw with 2 mm per turn (holds position without power) and a small stepper motor.

| Wind (m/s) | Tune to f_n (Hz) | Stiffness needed, B (N·m/rad) | Carriage below hinge (mm) |
|---|---|---|---|
| 2.0 | 1.45 | 60 | 41 |
| 3.0 | 2.18 | 131 | 61 |
| 4.0 | 2.91 | 229 | 80 |
| 4.5 | 3.27 | 289 | 90 |
| 5.0 | 3.64 | 356 | 100 |
| 6.0 | 4.36 | 510 | 120 |
| 7.0 | 5.09 | 693 | 140 |

That is about **20 mm of carriage per 1 m/s**, the same for A, B and C. The lock-on band is probably about ±20% of the tuned speed (estimate; measure it), so ±5–10 mm of carriage error is tolerable.

**Control:**
1. A cup anemometer at hub height gives a 2-minute average wind speed, which sets the target carriage position from a calibration table.
2. Extremum seeking trims the position (step a few mm, keep the direction that raises harvested power).
3. Retune only when the average leaves the band. Each 1 m/s retune costs a few joules.
4. Above 7 m/s the carriage parks at its stiffest (140 mm) and stays there through braking and storms.

---

## 10. Drive and generator

**Belt drive:**
- A GT2 toothed belt is clamped to a 100 mm-radius arc on the hub and wraps a 12-tooth pulley on the generator (26:1).
- At 4.5 m/s the generator swings back and forth ±170°, peaking about 640 rpm.
- Belt backlash at the reversals is a tiny fraction of the stroke.
- A capstan drive (Dyneema line wrapped on a drum) is a zero-backlash alternative.

**Generator:**
- A 5208-size brushless gimbal motor. Assumed values (check the datasheet): Ke ≈ 0.38 V·s/rad, winding resistance ≈ 12 Ω, rotor inertia ≈ 6 × 10⁻⁵ kg·m².
- It has no brushes to wear, and a high voltage constant, so it makes useful voltage at low speed.

| B at 4.5 m/s | Value |
|---|---|
| Peak hinge torque | 2.1 N·m |
| Generator damping ratio (optimum) | 0.032 |
| Total circuit resistance for that damping | ~120 Ω (≈108 Ω external load) |
| Copper efficiency | 90% |
| Peak back-EMF | ~26 V |

**Motor checks before committing:**
1. **Cogging torque.** Cogging is the magnetic "notchiness" felt when turning the shaft by hand. Multiplied by 26, it appears at the hinge. With kick-start it matters less, but keep it under ~5 mN·m at the shaft.
2. **Drag torque** (bearings plus iron losses). Assumed 4 mN·m, which is ~0.1 N·m at the hinge.
3. **Heat.** Winding loss reaches ~4 W in the power-capped band (assumed limit 5 W).
4. **Reflected inertia.** The rotor inertia × gear ratio² must stay a small part of the total (it is 6% for B).

**Why this layout:**

| Option | Verdict at this size |
|---|---|
| **Belt and rotary generator** | Friction a small share of a ~2 N·m torque; a cheap, efficient generator |
| Magnet and coil at the hinge (loudspeaker-type) | Needs a large, heavy motor for ~5 N·m at under 1 m/s of coil speed |
| One-way-clutch rectifier and rotary generator | Possible, but adds friction and wear for no gain in output |
| Piezo, triboelectric, electret | Milliwatts; not competitive |

---

## 11. Electronics and control

- **Bridge:** three-phase active (MOSFET) bridge. It rectifies when generating and drives the motor for the kick-start.
- **MPPT converter:** adjusts the effective load. The generator's load *is* the tube's damping, so the converter tunes damping. Perturb-and-observe on harvested power about every 5–10 s (the swing settles in about 1 s). Use a converter with very low standby draw, because output at 2–3 m/s is only 0.1–0.6 W.
- **Power cap (7–8 m/s):** the converter switches from maximum-power to constant-power mode.
- **Brake:** shorting the phases (or switching in a braking resistor, which keeps the heat out of the motor) gives a damping ratio around 0.4. It is applied at 8 m/s, on over-voltage, on loss of power, and for maintenance. **Use normally-closed contacts so the brake engages when unpowered.**
- **Over-voltage:** if the brake fails in strong wind, open-circuit voltage at the end stops can pass 100 V. Rate the electronics for at least 150 V (the calculator checks this) and add a clamp.
- **Storage:** 12.8 V LiFePO₄ battery or a supercapacitor bank.
- **Sensors:** cup anemometer, generator voltage and frequency, harvested power, temperature (brake when icing is likely: an iced, lopsided tube can start galloping, like iced power lines).
- **Controller:** a low-power microcontroller runs the mode logic, MPPT, tuning stepper, brake and logging.

---

## 12. Expected performance

Model central case while swinging. Low case = half.

| Electrical power | 2 m/s | 3 m/s | 4.5 m/s | 6 m/s | 7 m/s | 7–8 m/s |
|---|---|---|---|---|---|---|
| **B** | 0.13 W | 0.56 W | **2.01 W** | 4.74 W | 7.41 W | capped 7.41 W |
| **C** | 0.10 W | 0.49 W | **1.84 W** | 4.41 W | 6.97 W | capped 6.97 W |
| A | 0.10 W | 0.43 W | 1.57 W | 3.73 W | 5.86 W | capped 5.86 W |

| B in detail | 3 m/s | 4.5 m/s | 6 m/s | 7 m/s |
|---|---|---|---|---|
| Wind power through the tube | 4.1 W | 14.0 W | 33.1 W | 52.5 W |
| Mechanical capture | 0.73 W (18%) | 2.71 W (19%) | 6.62 W (20%) | 10.6 W (20%) |
| Hinge swing | ±6.2° | ±6.5° | ±6.6° | ±6.7° |
| Peak hinge torque | 0.90 N·m | 2.11 N·m | 3.81 N·m | 5.20 N·m |
| Generator peak rpm / EMF | 405 / 16 V | 640 / 26 V | 870 / 35 V | 1,020 / 41 V |

B's tube swing at 4.5 m/s: ±91 mm at the bottom, ±148 mm mid-height, ±205 mm at the top.

**Annual energy.** Rayleigh wind distribution at hub height, power curve from the operating modes above, half the swinging time locked on.

| Site mean wind | B central | B low | C central | C low | A central |
|---|---|---|---|---|---|
| 3.5 m/s | 6.5 kWh | 3.2 kWh | 5.9 kWh | 3.0 kWh | 5.1 kWh |
| 4.5 m/s | 9.1 kWh | 4.6 kWh | 8.5 kWh | 4.2 kWh | 7.2 kWh |
| 5.5 m/s | 9.9 kWh | 5.0 kWh | 9.2 kWh | 4.6 kWh | 7.8 kWh |

Annual energy rises slowly above a 4.5 m/s site mean because output is capped at 7 m/s and braked from 8 m/s.

---

## 13. Optimisation results

`python3 tools/lantern_calc.py sweep` searches a grid and ranks every design that passes the limits. Full outputs and the complete grids are in [calculator-output/](calculator-output/).

**Variables:**
- Diameter 100–400 mm
- Neck length 0–800 mm
- End-disc ratio 1.0 (none) to 2.4
- Shell: five constructions (2, 3 or 5 mm foam; outer skin only, both faces, or storm-thickened)
- Pulley 10–24 teeth
- Neck tube: sized automatically to the lightest standard carbon tube that passes

**Limits:**
- Reynolds number at 7 m/s ≤ 120,000 (the tested range of the evidence)
- Survives the storm requirement parked and braked (neck, skin, wall, discs, hub)
- Swinging loads (neck fatigue and peak, skin, voltage, generator heat) within limits up to the brake speed
- Total height ≤ 2 m
- Generator strong enough to provide the optimum damping

**Results** (fine grid: D 200–300 mm in 10 mm steps, 22,440 designs per survival requirement):

| Survival requirement | Best design in the grid | Electrical at 4.5 m/s | Configuration chosen |
|---|---|---|---|
| 25 m/s | 250 mm, 800 mm neck (25 × 23 tube), 2.0× discs, 3 mm sandwich shell, 10-tooth pulley | 2.05 W | **B**: same, but a 30 × 28 neck for margin (neck survives 33 m/s) and a 12-tooth pulley (common part): 2.01 W |
| 40 m/s | 250 mm, 650 mm neck (35 × 32 tube), 2.0× discs, 5 mm storm shell, 10-tooth pulley | 1.87 W | **C**: 600 mm neck and 12-tooth pulley: 1.84 W |
| 25 m/s, ranked by yearly energy at a 4.5 m/s site | Same as the power winner | 9.4 kWh/yr | — |
| Relaxed: Reynolds ≤ 200,000 and hub built for 250 N·m | 400 mm, 500 mm neck, 5 mm sandwich shell | 2.98 W | Untested territory ([sweep-relaxed-limits.md](calculator-output/sweep-relaxed-limits.md)) |

**Surviving 40 m/s instead of 25 m/s costs about 9% of output at 4.5 m/s.** The storm shell and stronger neck add mass, and the hub limit forces a shorter neck.

**What limits each variable** (25 m/s requirement, changing one at a time from the best design):

| Variable | Effect | What stops it |
|---|---|---|
| Diameter | +4% per 10 mm | The Reynolds limit at 250 mm (larger sizes also fail survival at the hub) |
| Neck length | 0 mm −46%, 400 mm −14%, 600 mm −5% | The hub's 150 N·m storm limit at 800 mm |
| End discs | 1.4× −14%, 1.6× −9%, 1.8× −4% | Flat beyond 2.0×; 2.4× fails survival (disc gust lift). **The gain follows directly from the assumed end-loss model and must be tested.** |
| Pulley teeth | 12 teeth −2%, 16 −8%, 20 −18% | 10 teeth is the smallest practical GT2 pulley |
| Shell | Single-skin shells +2–3% but fail survival (wall ovalling at ~15 m/s); 5 mm sandwich −3%, storm shell −4% | Survival requirement |

**How far to trust it.** The optimiser always pushes to whichever edge the model rewards. The diameter and neck results follow from well-understood physics (more wind, more even swing). The disc result is only as good as the end-loss assumption.

**Full grids.** Every combination evaluated, including those that fail a limit and the reason, is in [calculator-output/grid/](calculator-output/grid/), for both survival requirements. Column definitions are in that folder's README.

---

## 14. Alternatives considered and set aside

| Idea | Why not (for now) |
|---|---|
| Galloping cross-section (triangle, D-section) | No tuning needed and power keeps rising with wind. Quasi-steady theory gives ceilings of about 25% (triangle) and 54% (D-section), but measured magnet-and-coil galloping efficiency is very low (0.045% in one wind-tunnel test) and it needs storm parking. Worth a later experiment |
| Roughness strips on the round tube | Gave Michigan's 28% in water and extends output above the tuned band. A cheap second-stage experiment; needs wider stops and the brake |
| Flapping wing with pitch control | A two-wing water prototype measured 40%. A 1 m wing sweeping ±0.5 m could give ~16 W at 4.5 m/s, but it isn't a tube |
| Generating above 8 m/s | Output would keep rising (~20 W at 10 m/s for B), but neck fatigue, generator heat, voltage and tip acceleration all rise faster, and the flow is beyond the tested range |
| Locking the hinge in storms | The locked neck resonates with vortices at ~13 m/s. Brake on the springs instead |
| Two swing axes, no vane | Needs a second belt and generator; one axis is simpler and matches the published tests |
| Slim stiff masts (PVC, carbon, 40 mm) | High mass ratio; 0.02–0.35 W ([design history](../../docs/design-history.md)) |

---

## 15. Risks and unknowns

1. **No outdoor test of a low-mass-ratio tube exists.** Turbulence and wind-direction changes could cut output well below even the low case.
2. **The amplitude model is used outside its calibration.** The Skop–Griffin relation was fitted to high-mass-ratio data. Its zero-friction limits (16% for a base-hinged tube, 29% for parallel motion) match published theory and measurements, but at a mass ratio of 5–8 it is an extrapolation.
3. **The lock-on band width is assumed** (±20%). It sets the power-capped band and where the brake must take over.
4. **End-disc and end-loss behaviour is assumed** (half a diameter lost per bare end, none at discs of 2 × diameter).
5. **Storm behaviour above Re ≈ 200,000** (12–40 m/s for this tube): the "drag crisis" lowers drag and weakens vortex shedding for smooth cylinders, but turbulence, roughness and the end discs change that. The structural checks take no credit for it. The neck's second bending mode may fall in the 15–30 Hz range, where shedding at 20–40 m/s could reach it and the brake barely damps it. Tap-test the built rig.
6. **Wall ovalling and disc gust models are simple estimates** (ring bending under the pressure distribution; flat-plate lift for a 10° gust).
7. **Generator cogging and heat.** Measure cogging and drag before building; the 5 W winding limit is assumed.
8. **Durability:** shell and skin under 3 × 10⁷ swing cycles a year plus UV and hail; belt life at the reversals; bushing wear.
9. **Icing:** ice changes the shape and can cause galloping. Brake when icing is likely.

---

## 16. Changes from earlier versions

| Item | Before | Now | Why |
|---|---|---|---|
| Wind range | 3–7 m/s generating, 25 m/s survival | 1.6–8 m/s generating, 25 m/s (B) or 42 m/s (C) survival | Brief extended to 2–40 m/s |
| Configuration C | — | Added: all-weather, from a 40 m/s grid search | Survives 40 m/s unattended |
| Shell wall | Outer glass skin only | Glass on both faces | The new wall-ovalling check limits a single-skin shell to ~15 m/s |
| End discs | 3 mm foam with carbon strips | Built like the shell wall | The new gust-lift check |
| Operating modes | Tracking only | Idle, tracking, power-capped, braked; kick-start | Defined for every wind speed |
| Self-protection | "Drops out of lock-on above 1.2 × tuned speed" | Brake and stiff carriage protect it; brake is fail-safe | Low mass ratio widens the lock-on band |
| B figures | 2.05 W at 4.5 m/s; 10.7 kWh/yr | 2.01 W; 9.1 kWh/yr | Heavier sandwich shell and discs; cap at 7 m/s, brake at 8 m/s |
| Neck tube in the grid search | Fixed | Sized automatically per design | Survival and fatigue checks |
| Earlier corrections (still applied) | Three 4 mm rods; 8 mm axle; bare foam shell | Carbon tube neck; 10–16 mm axle; glass-skinned shell | Buckling, bushing loads, skin stress |
