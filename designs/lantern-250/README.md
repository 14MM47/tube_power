# Lantern 250

**A 1 m tall bladeless wind generator: a light 250 mm foam drum that swings in the wind and drives one small generator through a toothed belt.**

The name comes from its look: a thin, pale cylinder with a disc at each end, like a paper lantern on a stick. The number is the tube diameter in millimetres.

> **Status: concept design, not built or tested.** Every number here is an engineering estimate from the models in [physics.md](physics.md), reproduced by [`tools/lantern_calc.py`](../../tools/lantern_calc.py). The low-case figures assume real gusty wind halves the model's output.

Related documents:
- [physics.md](physics.md): the models, equations and their limits
- [build-and-test.md](build-and-test.md): build order, test plan, safety
- [calculator-output/](calculator-output/): saved calculator reports and optimisation runs
- [../../docs/design-history.md](../../docs/design-history.md): the designs that led here
- [../../research/](../../research/): the research this rests on

---

## 1. Summary

| | **Lantern 250-B (recommended)** | Lantern 250-A (first version) |
|---|---|---|
| Tube | Ø250 × 1,000 mm foam shell with glass-tissue skin | same |
| End discs | Ø500 mm (2.0 × tube diameter) | Ø400 mm (1.6 ×) |
| Neck (hinge to tube bottom) | 800 mm, 30 × 28 mm carbon tube | 400 mm, 25 × 23 mm carbon tube |
| Overall height above the hinge | 1.8 m | 1.4 m |
| Drive | GT2 belt, 100 mm arc to 12-tooth pulley, 26:1 | 16-tooth pulley, 19.6:1 |
| Generator | 5208-size brushless gimbal motor | same |
| Swinging mass | 0.49 kg | 0.40 kg |
| Tuning range | 3–7 m/s, ~20 mm of spring-carriage travel per 1 m/s | same |
| **Electrical power at 4.5 m/s** | **2.05 W** (low case 1.0 W) | 1.60 W (low case 0.8 W) |
| Electrical power at 6 m/s | 4.8 W (low case 2.4 W) | 3.8 W (low case 1.9 W) |
| Energy at a 4.5 m/s-mean site | ~11 kWh/yr (low case ~5) | ~8 kWh/yr (low case ~4) |

Configuration B came out of a grid search over 31,000 combinations of diameter, neck length, disc size, shell material and gear ratio ([section 12](#12-optimisation-results)). A is the version first worked out in conversation, with the structural corrections in [section 15](#15-changes-from-the-version-discussed-in-conversation). The hub is designed so the neck, discs and pulley can be swapped, so **both can be built and compared on the same rig**.

For scale: a 100 W solar panel gives roughly 90–150 kWh a year. The Lantern is a physics and mechanism project, not a cheaper source of energy.

---

## 2. Design brief

- Tube height limited to 1 m. Nothing else fixed: diameter, material, mounting, transducer and energy-transfer method all free.
- Maximise electrical output at realistic domestic winds (3–7 m/s at about 3 m above ground).
- Buildable at home with model-making materials and common 3D-printer and hobby-electronics parts.
- Survive a 25 m/s gust.

---

## 3. Why it looks like this

The design follows from first principles, not from copying the commercial oscillating mast.

1. **Only diameter adds wind.** The wind power passing a tube is ½ρU³·D·L. With L fixed at 1 m, a fatter tube catches proportionally more.
2. **Mass ratio is what limits a vibrating tube in air.** Mass ratio is tube mass divided by the mass of air it displaces. In air it is normally in the hundreds, and then even small friction swamps the useful damping (efficiency falls as 1/(1 + 1.07 × mass ratio × friction damping)^5.7, [physics.md §6](physics.md#6-optimum-generator-load-and-efficiency)). Skin mass grows with diameter but displaced air grows with diameter squared, so **a fat, light tube has a low mass ratio**: about 4 here, against about 70 for a 40 mm carbon mast and 217 for 40 mm PVC pipe.
3. **A low mass ratio fixes the other problems at once.**
   - The best generator damping ratio rises to ~0.04, so ordinary bushing and generator friction (~0.008) costs little.
   - The swing frequency can stretch by roughly 20% to follow the wind (Govardhan & Williamson's low-mass-ratio result), so tuning is forgiving.
4. **Reynolds number caps the diameter.** The best measured efficiencies for oscillating cylinders (Michigan's VIVACE, 22–28%) were at Reynolds numbers of 30,000–120,000. A 250 mm tube reaches 117,000 at 7 m/s. Larger diameters are untested ground ([section 12](#12-optimisation-results)).
5. **A tube only four diameters tall needs end discs.** They stop air spilling round the ends and weakening the vortices.
6. **A neck makes the swing more even along the tube.** With the hinge below the tube, the bottom moves almost as much as the top, so more of the tube works near its best amplitude. In the model, an 800 mm neck gives 85% of the output of perfectly parallel motion, against 56% for a hinge at the tube's base.
7. **Low frequency and high torque favour gearing.** The tube swings at 2–6 Hz with up to ~5 N·m at the hinge, ten times the torque of a slim mast. A belt to a small rotary generator beats a direct magnet-and-coil generator at this size, and the mechanical losses are a small share.
8. **One swing axis, aligned by a tail vane.** A single generator can only resist motion along one axis. A vane keeps the hinge axle pointing into the wind so the tube always swings across it. This also matches the one-axis setup used in almost all published tests.

---

## 4. General arrangement

```
            ┌─────────┐   end disc Ø500 (B) / Ø400 (A)
            │░░░░░░░░░│
            │░░░░░░░░░│   tube Ø250 × 1000
            │░░░░░░░░░│   3 mm XPS foam, glass-tissue skin,
   wind →   │░░░░░░░░░│   4 internal foam rings
            │░░░░░░░░░│
            │░░░░░░░░░│   swings ±~6.6° across the wind
            └────┬────┘   end disc + bottom spider
                 │
                 │        neck: 30×28 carbon tube, 800 mm (B)
                 │
        ┌────────●────────┐  hinge: 12 mm axle, two bushings 150 mm apart,
        │  ◄▮▮══╪══▮▮►    │  axle points INTO the wind
        │       │         │  spring carriage 60–140 mm below hinge (tuning)
        │   ⌒ arc R100 ⌒  │  GT2 belt → 12-tooth pulley → generator (26:1)
        │      [GEN]      │
        └────────┬────────┘
     tail vane ◄═╪  yaw bearing
                 │  post, hinge ~3 m above ground
```

View is from the side, wind from the left. In operation the tube rocks in and out of the page.

---

## 5. Parts, masses and inertia (configuration B)

| Part | Specification | Mass |
|---|---|---|
| Tube shell | Ø250 × 1,000 mm, 3 mm extruded polystyrene (model-aircraft foam, ~37 kg/m³), skinned with ~25 g/m² glass tissue in epoxy; seams taped | 0.146 kg incl. rings and seams |
| Internal rings | Four foam rings keep the tube round | (included) |
| End discs | Ø500 mm, 3 mm XPS with carbon-strip stiffeners, glued square to the tube | 0.031 kg each |
| Bottom spider | Joins the tube's bottom ring to the neck | 0.015 kg |
| Neck | 30 × 28 mm carbon tube, 800 mm | 0.113 kg |
| Hub assembly | Hub, 12 mm axle, spring carriage, belt arc | ~0.15 kg (near the axle) |
| **Total swinging mass** | | **0.49 kg** |

| Inertia about the hinge | kg·m² |
|---|---|
| Shell | 0.260 |
| End discs | 0.123 |
| Spider, neck, hub | 0.034 |
| Generator rotor seen through the 26:1 belt | 0.041 |
| **Structural total** | **0.458** |
| Air moving with the tube (added mass) | 0.107 |
| **Total** | **0.565** |
| Mass ratio (structural ÷ displaced air) | **4.3** |

Configuration A: total inertia 0.256 kg·m², mass ratio 3.8.

---

## 6. Structure

Survival case: 25 m/s gust, drag coefficient 1.2.

| Item | B | A |
|---|---|---|
| Drag on the tube | 115 N | 115 N |
| Bending moment at the tube base | 57 N·m | 57 N·m |
| Bending moment at the hinge | 149 N·m | 103 N·m |
| Glass-skin stress at the tube base | 23 MPa | 23 MPa |
| Neck tube stress | 234 MPa (30 × 28 carbon) | 238 MPa (25 × 23 carbon) |
| Load on each hinge bushing | ~1,000 N (150 mm apart) | ~1,030 N (100 mm apart) |

Points to note:
- **The glass skin is essential.** Bare 3 mm foam would see about 0.39 MPa at the tube base in a 25 m/s gust, which is roughly its strength. The skin carries the bending load at ~23 MPa, well inside glass-epoxy limits.
- **The neck must be a tube, not thin rods.** Three 4 mm carbon rods (the first idea) would buckle in about 10 m/s of wind.
- **Neck stress has a safety factor of about 3–4** on typical carbon tube strength. Use roll-wrapped tube with mostly lengthwise fibres.
- **Hinge moment design limit: 150 N·m.** It sets the maximum neck length in the optimiser.
- **No lean in steady wind.** The hinge axle points into the wind, so drag acts along the axle, not about it. Drag loads the bushings, head and post, not the springs.
- **The tube protects itself from over-speed.** Above about 1.2 × the tuned wind speed, a round tube drops out of lock-on and the swing collapses. Rubber end stops at ±14° catch gust buffeting.
- **The tips accelerate hard.** The top of the tube reaches about 11 g at 4.5 m/s and 27 g at 7 m/s, so nothing heavy goes at the ends.
- **Fatigue:** about 3 × 10⁷ swing cycles a year at 30% running time.

---

## 7. Hinge, yaw head and mounting

- **Hinge:** single axis, 12 mm stainless axle, two polymer plain bushings 150 mm apart (A: 10 mm axle, 100 mm apart).
  - Plain bushings, not ball bearings: the small rocking angle damages ball bearings over time (the balls dent the races without rolling far).
  - Bushing friction at 4.5 m/s is about 0.10 N·m at the hinge, roughly 5% of the harvesting torque.
- **Axle orientation:** pointing into the wind, so the tube swings across it.
- **Yaw head:** a yaw bearing at the post top with a tail vane on a ~0.6 m boom (about 0.05–0.1 m² of vane) keeps the axle aligned. The vane sits below the tube in clean air.
- **Height:** hinge about 3 m above ground, so the tube spans roughly 3.8–4.8 m (B) or 3.4–4.4 m (A). Higher is better: power rises with the cube of wind speed.
- **Cables:** a slip ring at the yaw bearing, or let the cable twist with an untwist routine.
- **Gravity:** the swinging mass sits above the hinge and slightly destabilises it (3.2 N·m/rad for B). The springs overcome this, and calibration absorbs it.

---

## 8. Tuning

The tube must be tuned so its swing frequency matches the vortex-shedding frequency at the current wind.

**Rule:** still-air natural frequency f_n = U ÷ (5.5 × D), which is 0.73 × U for D = 0.25 m. The 5.5 is the reduced velocity U/(f_n·D) where power peaks; calibrate it on the real rig.

**Mechanism:**
- Two opposing springs act on a carriage that slides along a lever below the hinge.
- Their stiffness about the hinge is 2 × spring rate × r², where r is the carriage's distance from the hinge. So frequency rises in proportion to r, and **the carriage position is a linear wind-speed scale**.
- Springs: two, each **14.8 N/mm** for B (6.7 N/mm for A), preloaded more than their travel at the ±14° stops (~35 mm at r = 140 mm).
- Carriage drive: T8 lead screw with 2 mm per turn (holds position without power) and a small stepper motor.

| Wind (m/s) | Tune to f_n (Hz) | Stiffness needed, B (N·m/rad) | Carriage below hinge (mm) |
|---|---|---|---|
| 3.0 | 2.18 | 109 | 61 |
| 4.0 | 2.91 | 191 | 80 |
| 4.5 | 3.27 | 242 | 90 |
| 5.0 | 3.64 | 297 | 100 |
| 6.0 | 4.36 | 428 | 120 |
| 7.0 | 5.09 | 581 | 140 |

That is about **20 mm of carriage per 1 m/s**, the same for A and B. The lock-on band is probably about ±20–25% of the tuned speed (estimate; measure it), so ±5–10 mm of carriage error is tolerable.

**Control:**
1. A cup anemometer at hub height gives a 2-minute average wind speed, which sets the target carriage position from a calibration table.
2. Extremum seeking trims the position (step a few mm, keep the direction that raises harvested power).
3. Retune only when the average leaves the band. Each 1 m/s retune costs a few joules.

---

## 9. Drive and generator

**Belt drive:**
- A GT2 toothed belt is clamped to a 100 mm-radius arc on the hub and wraps a 12-tooth pulley on the generator (26:1).
- At 4.5 m/s the generator swings back and forth ±172°, peaking about 650 rpm.
- Belt backlash at the reversals is a tiny fraction of the stroke.
- A capstan drive (Dyneema line wrapped on a drum) is a zero-backlash alternative.

**Generator:**
- A 5208-size brushless gimbal motor. Assumed values (check the datasheet): Ke ≈ 0.38 V·s/rad, winding resistance ≈ 12 Ω, rotor inertia ≈ 6 × 10⁻⁵ kg·m².
- It has no brushes to wear, and a high voltage constant, so it makes useful voltage at low speed.

| At 4.5 m/s (B) | Value |
|---|---|
| Peak hinge torque | 2.1 N·m |
| Generator damping ratio (optimum) | 0.040 |
| Total circuit resistance for that damping | ~120 Ω (≈108 Ω external load) |
| Copper efficiency | 90% |
| Peak back-EMF | ~26 V |

**Three motor checks before committing:**
1. **Cogging torque.** Cogging is the magnetic "notchiness" felt when turning the shaft by hand. Multiplied by 26, it appears at the hinge and sets a start-up threshold. The vortex lift moment at small swing is only about 0.5 N·m at 3 m/s and 1.2 N·m at 4.5 m/s. **Cogging at the motor shaft should be under ~5 mN·m.** If it's higher, use a coreless or slotless motor (no cogging) or a lower gear ratio.
2. **Drag torque** (bearings plus iron losses). Assumed 4 mN·m, which is ~0.1 N·m at the hinge.
3. **Reflected inertia.** The rotor inertia × gear ratio² must stay a small part of the total (it is 7% for B).

**Why this layout:**

| Option | Verdict at this size |
|---|---|
| **Belt and rotary generator** | Friction a small share of a ~2 N·m torque; a cheap, efficient generator |
| Magnet and coil at the hinge (loudspeaker-type) | Needs a large, heavy motor for ~5 N·m at under 1 m/s of coil speed |
| One-way-clutch rectifier and rotary generator | Possible, but adds friction and wear for no gain in output |
| Piezo, triboelectric, electret | Milliwatts; not competitive |

---

## 10. Electronics and control

- **Rectifier:** three-phase synchronous (active) rectifier from the generator; Schottky diodes will do at ~26 V peak.
- **MPPT converter:** adjusts the effective load. The generator's load *is* the tube's damping, so the converter tunes damping. Perturb-and-observe on harvested power about every 5–10 s (the swing settles in about 1 s).
- **Storage:** 12.8 V LiFePO₄ battery or a supercapacitor bank.
- **Soft start:** let the swing build before applying load.
- **Brake:** shorting the three phases gives a damping ratio around 0.4, which stops the swing. Use it for storms and maintenance.
- **Over-voltage:** at the end stops in strong gusts the open-circuit voltage can reach ~85 V peak. Rate the rectifier and converter input for at least 100 V and add a clamp, or brake automatically above a voltage threshold.
- **Controller:** a low-power microcontroller runs MPPT, the tuning stepper, the brake and logging (wind speed, generator voltage and frequency, harvested power).

---

## 11. Expected performance

Model central case while locked on. Low case = half.

**Configuration B**

| Wind | 3 m/s | 4.5 m/s | 6 m/s | 7 m/s |
|---|---|---|---|---|
| Reynolds number | 50,000 | 75,000 | 100,000 | 117,000 |
| Swing frequency | 2.4 Hz | 3.6 Hz | 4.8 Hz | 5.6 Hz |
| Wind power through the tube | 4.1 W | 14.0 W | 33.1 W | 52.5 W |
| Mechanical capture | 0.75 W (18%) | 2.76 W (20%) | 6.75 W (20%) | 10.8 W (21%) |
| **Electrical, central** | **0.57 W** | **2.05 W** | **4.83 W** | **7.55 W** |
| Electrical, low case | 0.29 W | 1.03 W | 2.42 W | 3.78 W |
| Hinge swing | ±6.2° | ±6.6° | ±6.7° | ±6.7° |
| Peak hinge torque | 0.91 N·m | 2.13 N·m | 3.84 N·m | 5.24 N·m |
| Generator peak rpm / EMF | 410 / 16 V | 650 / 26 V | 880 / 35 V | 1,030 / 41 V |

Tube swing at 4.5 m/s: ±92 mm at the bottom, ±150 mm mid-height, ±207 mm at the top.

**Configuration A** electrical, central (low case): 0.44 (0.22) W at 3 m/s, 1.60 (0.80) W at 4.5 m/s, 3.80 (1.90) W at 6 m/s, 5.97 (2.98) W at 7 m/s. Hinge swing ±8.0–8.8°.

**Annual energy.** Rayleigh wind distribution at hub height, half the in-band time locked on.

| Site mean wind | B central | B low | A central | A low |
|---|---|---|---|---|
| 3.5 m/s | 6.9 kWh | 3.5 kWh | 5.4 kWh | 2.7 kWh |
| 4.5 m/s | 10.7 kWh | 5.3 kWh | 8.4 kWh | 4.2 kWh |
| 5.5 m/s | 12.2 kWh | 6.1 kWh | 9.6 kWh | 4.8 kWh |

---

## 12. Optimisation results

`python3 tools/lantern_calc.py sweep` searches a grid and ranks every design that passes the limits. Full outputs are in [calculator-output/](calculator-output/).

**Variables:**
- Diameter 100–400 mm
- Neck length 0–800 mm
- End-disc ratio 1.0 (none) to 2.4
- Shell material: 2, 3 or 5 mm foam, all glass-skinned
- Pulley 10–36 teeth

**Limits:**
- Reynolds number at 7 m/s ≤ 120,000 (the tested range of the evidence)
- Hinge storm moment ≤ 150 N·m
- Skin stress ≤ 40 MPa
- Total height ≤ 2 m
- Generator strong enough to provide the optimum damping

**Best design:** 250 mm diameter, 800 mm neck, discs 2.0 × diameter, lightest shell, 10-tooth pulley: 2.11 W at 4.5 m/s. Configuration B uses the 3 mm shell (−1%, more robust) and a 12-tooth pulley (−2%, a common part).

**What limits each variable** (changing one at a time from the best design):

| Variable | Effect | What stops it |
|---|---|---|
| Diameter | +4% per 10 mm | The Reynolds limit at 250 mm. With the limit relaxed to 200,000 and a stronger hinge, the model keeps climbing to 3.35 W at 400 mm ([sweep-relaxed-limits.md](calculator-output/sweep-relaxed-limits.md)) |
| Neck length | 0 mm −46%, 400 mm −14%, 600 mm −5% | The 150 N·m storm limit at 800 mm |
| End discs | none −22%, 1.6 × −9% | Flat beyond 2.0 ×. **This follows directly from the assumed end-loss model (no loss at 2.0 ×) and must be tested.** |
| Pulley teeth | 16 teeth −8%, 20 −18% | 10 teeth is the smallest practical GT2 pulley. More gearing raises copper efficiency but adds reflected inertia and friction |
| Shell | 2, 3, 5 mm foam within 3% | Robustness, not power |

**How far to trust it.** The optimiser always pushes to whichever edge the model rewards. The diameter and neck results follow from well-understood physics (more wind, more even swing). The disc result is only as good as the end-loss assumption. Ranking by annual energy instead of power at 4.5 m/s gives the same winner (11.2 kWh/yr at a 4.5 m/s site).

**Full grids.** Every combination evaluated, including those that fail a limit and the reason, is in [calculator-output/grid/](calculator-output/grid/):
- `grid-wide.csv`: 20,736 rows covering D 100–400 mm.
- `grid-fine.csv`: 30,855 rows covering D 200–300 mm in 10 mm steps.

Each row has 35 columns: power, annual energy, mass ratio, swing, torque, generator values and structural checks. Column definitions are in the folder's README.

---

## 13. Alternatives considered and set aside

| Idea | Why not (for now) |
|---|---|
| Galloping cross-section (triangle, D-section) | No tuning needed and power keeps rising with wind. Quasi-steady theory gives ceilings of about 25% (triangle) and 54% (D-section), but measured magnet-and-coil galloping efficiency is very low (0.045% in one wind-tunnel test) and it needs storm parking. Worth a later experiment |
| Roughness strips on the round tube | Gave Michigan's 28% in water and extends output above the tuned band. A cheap second-stage experiment; needs wider stops and the brake |
| Flapping wing with pitch control | A two-wing water prototype measured 40%. A 1 m wing sweeping ±0.5 m could give ~16 W at 4.5 m/s, but it isn't a tube |
| Two swing axes, no vane | Needs a second belt and generator; one axis is simpler and matches the published tests |
| Slim stiff masts (PVC, carbon, 40 mm) | High mass ratio; 0.02–0.35 W ([design history](../../docs/design-history.md)) |

---

## 14. Risks and unknowns

1. **No outdoor test of a low-mass-ratio tube exists.** Turbulence and wind-direction changes could cut output well below even the low case.
2. **The amplitude model is used outside its calibration.** The Skop–Griffin relation was fitted to high-mass-ratio data. Its zero-friction limits (16% for a base-hinged tube, 29% for parallel motion) match published theory and measurements, but at a mass ratio of 4 it is an extrapolation.
3. **End-disc and end-loss behaviour is assumed** (half a diameter lost per bare end, none at discs of 2 × diameter).
4. **Reynolds behaviour in gusty air:** the 120,000 limit comes from smooth-flow water tests.
5. **Generator cogging** may stop the tube starting in light wind. Measure before building.
6. **Durability:** the foam shell and skin under 3 × 10⁷ cycles a year plus UV; belt life at the reversals; bushing wear.
7. **Noise:** a 2–6 Hz swing is silent, but the belt and pulley may whine. Untested.

---

## 15. Changes from the version discussed in conversation

| Item | In conversation | Here | Why |
|---|---|---|---|
| Shell | Bare 3 mm foam | Glass-tissue skin added | Bare foam is at its strength limit at 25 m/s |
| Neck | Three 4 mm carbon rods | One 25 × 23 (A) or 30 × 28 (B) mm carbon tube | Rods would buckle at ~10 m/s |
| Hinge axle | 8 mm | 10–12 mm, bushings 100–150 mm apart | ~1 kN per bushing in a storm |
| Total inertia (A) | ~0.20 kg·m² | 0.256 kg·m² | Skin, stiffer discs, generator rotor seen through the belt |
| Springs (A) | 5.4 N/mm | 6.7 N/mm | Follows from the inertia |
| Wind power at 4.5 m/s | 13.7 W | 14.0 W | Arithmetic correction |
| Annual energy (A) | 5–20 kWh | 4–8 kWh | Computed properly from a wind distribution |
| Configuration B | — | Added | From the optimiser |
| Cogging and over-voltage checks | — | Added | Start-up threshold and open-circuit voltage at the stops |
