# Design history: from a bladeless mast to Lantern 250 and 330-G

This records how the design evolved, step by step, and what each step taught. The earlier designs' figures come from hand calculations made in conversation with an earlier version of the same models. Treat them as estimates, as for everything else here.

## 0. Starting question: can you buy a small domestic bladeless turbine?

No, as of November 2026.
- Vortex Bladeless's 1 m Nano (~3 W) and 2.75 m Tacoma (~100 W) remain prototypes. Earlier promised sale dates passed.
- Aeromine is rooftop-commercial only (50 kW-plus installations).
- Katrick, Halcium and O-Wind are in development. SheerWind INVELOX went bankrupt in 2018.
- Marketplace "bladeless vortex" turbines are mostly ordinary vertical-axis turbines with blades.

The research on building one is in [../research/](../research/). Its headline finding: every documented home or student bladeless build produced microwatts to ~50 mW. None reached 1 W.

## 1. Tuned mast with a mechanical rectifier (250 mm × 1.5 m)

**Idea (from the brief):** a mast pivoted near its base, with a lower lever feeding a mechanical coupling that turns X/Y wobble into rotation of one generator.

**Design:**
- Ø250 mm × 1.5 m mast, ≤1 kg, tuned to 3.6 Hz at 4.5 m/s, swinging about ±4.8°.
- Joystick-style X/Y yokes feed two one-way-clutch rectifiers on a shared belt to one coreless generator, at about 50–100:1.
- Estimate: ~0.5–2 W electrical while locked on.

**Lessons:**
- A lever below the pivot trades force for stroke. It doesn't add energy.
- Match the generator's **resistance** (damping), not the stroke. Best damping ratio is ~0.02–0.05. Fixed-stroke cranks and cams don't work: they can't start from a small swing and they have dead centres.
- **Gearing rules** for G, the ratio from hinge to generator:
  - damping seen by the mast ∝ G²
  - friction seen by the mast ∝ G
  - reflected inertia ∝ G²
  - voltage ∝ G
- No flywheel. Use a soft start. Ball bearings at small rocking angles get damaged (false brinelling). Expect about 10⁸ cycles a year.
- One generator can only resist one axis at a time. So use **a single swing axis aligned by a tail vane**, or two generators.

## 2. 40 mm PVC pipe

**Design:** cheap 40 mm PVC pipe as the mast.

**Findings:**
- Vortices shed at f = 5 × U Hz, so 15–30 Hz.
- Mass ratio ≈ 217, so the optimum generator damping ratio (~0.0008) is below almost any mechanism's friction.
- PVC is floppy. Its own bending frequency is ~11/a² Hz for arm length a, which caps each arm at ~0.3 m.
- Best bare design: centre pivot, 0.6 m, **0.02–0.08 W** mechanical at 4.5 m/s. A clutch rectifier would use more power than it delivers.

**Fix:** slide on 25 mm-wall foam pipe insulation (Ø92 mm). Mass ratio falls to ~61. 1.0 m, centre pivot, **0.15–0.35 W** mechanical at 4.5 m/s. Capstan drive at 30:1 to a coreless generator.

**Lessons:**
- Mass ratio decides everything in air.
- A centre pivot puts two arms in the wind and balances the inertial loads.
- Pipe stiffness limits arm length.

## 3. 40 mm carbon tube (best material for a fixed 40 mm diameter)

**Design:** 40 × 39 mm thin-wall carbon tube, 1.67 m, centre pivot, cross-spring flexure hinge, die-spring tuning (16.7 mm of carriage per m/s), 40:1 capstan drive.

**Result:** ~0.26 W mechanical / ~0.2 W electrical at 4.5 m/s.

**Lessons:**
- For a thin tube, bending frequency depends only on stiffness-to-weight (E/ρ) and radius, not on wall thickness. So pick the stiffest-per-weight material, then the thinnest wall that survives.
- **Capture efficiency ≈ 16% / (1 + 1.07 m* ζ_p)^5.7**, where ζ_p is the damping ratio from friction and losses. Halving the mass ratio roughly doubles the output when friction is realistic.

## 4. Mechanical coupling vs contactless generators (40 mm carbon mast)

| Method | Electrical at 4.5 m/s |
|---|---|
| Loudspeaker-motor voice coil at the hinge (contactless) | 0.30–0.37 W |
| Capstan and rotary generator | 0.20 W |
| One-way-clutch rectifier | ~0.10 W |
| Piezo, triboelectric, electret | milliwatts |

**Lesson:** high frequency with small force favours a direct magnet-and-coil generator. Low frequency with large force favours gearing. Vortex itself moved from piezo (2010 patent) to magnets and coils (2016).

## 5. First principles: Lantern 250

**Brief:** only the 1 m tube height fixed; everything else open.

**Reasoning:**
- Only diameter adds wind.
- A fat, ultralight tube gets the mass ratio down to ~4. That makes friction cheap and tuning forgiving.
- Reynolds number (≤120,000, the tested range) caps the diameter at ~250 mm.
- End discs, a neck below the tube, one vane-aligned axis, and belt gearing (low frequency, high torque) follow from there.

**Configuration A** (as first worked out): 400 mm neck, Ø400 mm discs, 19.6:1. **1.6 W** electrical at 4.5 m/s, model central case.

**Then:**
- **Structural corrections:** glass-skinned shell; single carbon-tube neck instead of thin rods; stronger hinge.
- **Calculator and grid search** over 31,000 combinations. The optimum hits the Reynolds limit for diameter and the storm-moment limit for neck length.

**Configuration B** (recommended): 800 mm neck, Ø500 mm discs, 26:1. **2.05 W** electrical at 4.5 m/s, central case, at that stage (single-skin shell).

See [../designs/lantern-250/](../designs/lantern-250/).

## 6. Handling 2 m/s to 40 m/s: operating modes and configuration C

**Brief:** handle every wind speed from about 2 m/s up to 40 m/s.

**What changed:**
- **The calculator now checks every wind speed from calm to 40 m/s.** It picks the operating mode at each speed:
  - idle,
  - tracking (2–7 m/s),
  - power-capped (7–8 m/s),
  - braked (8 m/s and above).
- **At each speed it checks every part:** neck (peak and fatigue), skin, shell-wall ovalling, end-disc gust lift, hub, voltage and generator heat. It also reports cut-in and survival wind speeds.
- **The new wall and disc checks exposed a weakness.** A shell with an outer glass skin only would survive just ~15 m/s. B now has glass on both faces, survives 25 m/s, and gives 2.01 W at 4.5 m/s, down from 2.05 W.
- **Capping above 7 m/s by over-loading the generator heats its windings,** so the brake comes in at 8 m/s.
- **A kick-start was added:** the controller briefly drives the motor to start the swing. It brings cut-in down from ~2.1 to ~1.6 m/s.
- **The earlier claim that the tube drops out of lock-on and protects itself was withdrawn.** At a low mass ratio the lock-on band is wide, so protection comes from a fail-safe brake.
- **Configuration C was found by a grid search requiring 40 m/s survival:**
  - 5 mm sandwich shell with a thickened outer skin near the base,
  - 600 mm × 35 × 32 mm carbon neck,
  - hub built for 350 N·m.

  It gives **1.84 W** at 4.5 m/s, about 9% less than B, and survives to about 42 m/s.

## 7. Electrical power to 40 m/s, and the neck's bending mode

**Brief:** see electrical power for the best designs all the way to 40 m/s.

**What changed:**
- **A `curve` command and a chart on the grid page.** For any design they show four curves to 40 m/s:
  - as designed,
  - kept generating within every limit,
  - the model's potential (if it stayed locked on and nothing failed),
  - the wind passing the tube.
- **A keep-generating control option.** It retunes as far as the neck allows, then picks the generator load that gives the most power with every part within limits.
- **A neck bending-mode check.** The neck and tube must bend at least 1.5 × faster than the swing.
  - The 30 × 28 mm neck first specified for B bends at ~9.6 Hz, which caps the swing at 8 m/s. B now has a 35 × 32 mm neck (~14.5 Hz, retuning possible to 12 m/s) at a cost of ~0.5% of output.
  - The grid search's earlier winners used 25 × 23 mm necks, which fail this check. The grids were regenerated.

**Result:** a VIV tube generates nothing above about 11 m/s, whatever the control. The generator's heat limit, the neck's bending mode and the drag crisis (Reynolds number above 200,000) all stop it there, even though the model's potential reaches hundreds of watts. Keeping it generating to ~11 m/s adds ~60% to yearly energy at a 4.5 m/s site, in untested flow.

## 8. A galloping version that keeps generating to 40 m/s: Lantern 330-G

**Brief:** design a galloping version that keeps generating up to 40 m/s.

**Model.** A new calculator, `tools/galloping_calc.py`:
- quasi-steady galloping with Parkinson's cubic side-force curve (square: A1 = 2.3, A3 = 18), by harmonic balance for the hinged prism, with Coulomb friction;
- checked against a time-step simulation to within 1%.

At every wind speed the controller chooses three things, within every limit:
- the pitch of the prism about its own axis;
- the generator load;
- the swing frequency (the lowest that keeps the swing at ±15°).

**What the physics says:**
- **Galloping power doesn't depend on mass or swing frequency.** So the prism can be sturdy (mass ratio 10), and the frequency is chosen for the loads: U/(fD) ≈ 22 at every wind, where the theory is valid.
- **A square captures at most ~4% of the wind passing it.** The light round tube captures 15–20% at its tuned speed. Galloping makes up for it only by working at every wind speed.
- **Pitch is a natural throttle.** The effective slope A1 − 3A3β² reaches zero at 11.8°. At 45° the square is stable and the side force vanishes, so the machine can be switched off aerodynamically.
- **Changes from the vortex designs:**
  - ball bearings instead of polymer bushings (storm drag made bushing friction prohibitive, and the ±15° swing removes the false-brinelling worry);
  - a 100 W-class generator (the 5208 overheats before holding 20 W).

**Search.**
- 5,280 designs. Hub strength was the main lever: 4.2 kWh/yr at a 4.5 m/s site with a 500 N·m hub, 6.2 with 800.
- Width went to the assumed aspect-ratio limit (330 mm on 1 m). Relaxing it and strengthening the hub further adds only 5%, because the end plates then limit storm survival.

**Result: Lantern 330-G.**
- 2.5 m/s cut-in. 0.40 W at 4.5 m/s, 5.5 W at 10 m/s, 20 W held by pitch from 15.5 to 40 m/s.
- Survives 46.7 m/s feathered.
- Yearly energy beats 250-B as designed above about a 5 m/s site mean, and 250-B kept generating above about 7 m/s.
- The biggest unknown is turbulence: 20% off A1 costs 40% of the energy. So the first build step is a static side-force test.

## 9. The most power from 15 to 40 m/s: Lantern 330-GH

**Brief:** why the pitch regulation? Design for the maximum possible power between 15 and 40 m/s.

**Why 330-G pitched.** Only to hold its 20 W rating. That was a choice made because yearly energy at ordinary sites hardly depends on it, not a physical limit. At 40 m/s the prism could supply about 270 W through 330-G's small generator. Pitch only ever throws galloping power away, so it is worth having only where a part would otherwise go past its limit.

**What runs out first without the cap:**
- the generator (it can't absorb the load without overheating);
- the belt (~130 N·m at the hinge);
- the springs (force rises with the square of frequency).

The calculator gained a belt-tension check, larger generator presets, heavier necks, and sweep options for drive, swing and spring force.

**Search.** 5,184 designs, ranked by average power from 15 to 40 m/s. Best average by generator:

| Generator | Best average |
|---|---|
| 8108 outrunner | 68 W |
| 6374 outrunner | 117 W |
| Direct-drive e-bike hub motor | 152 W |

The other choices that mattered:
- springs 3 kN instead of 1.5 kN: +19%;
- 330 mm prism instead of 300 mm: +10%;
- 1,200 N·m hub with an 800 mm neck: +5%;
- swing ±20–25° instead of ±15°: +4%.

**Result: Lantern 330-GH.**
- **Drive:** hub motor, HTD 8M belt on a 275 mm arc (9.8:1), ±25° swing, 3 kN springs, 800 mm neck, 1,200 N·m hub.
- **Output:** no part reaches its limit below 40 m/s, so the prism stays face-on and the pitch drive becomes a two-position feather. Average **152 W from 15 to 40 m/s**, **384 W at 40 m/s**, about 3% of the wind passing the prism. That is essentially all this prism's galloping can give after losses.
- **Cost:** a 6.1 m/s cut-in, set by the hub motor's drag. It makes more energy over a year than 330-G only above about an 8 m/s site mean. A 6374 outrunner is the middle option (117 W average, 3.6 m/s cut-in).

## Progression in one table

| Design | Mass ratio | Electrical at 4.5 m/s (central) |
|---|---|---|
| 40 mm PVC, bare | ~217 | ~0.01–0.06 W |
| 40 mm PVC + foam sleeve | ~61 | ~0.1–0.25 W |
| 40 mm carbon, capstan | ~69 | ~0.2 W |
| 40 mm carbon, voice coil | ~69 | ~0.3–0.37 W |
| Lantern 250-A (with all later corrections) | 4.7 | 1.57 W |
| **Lantern 250-B** (survives 25 m/s) | **5.5** | **2.00 W** |
| **Lantern 250-C** (survives 40 m/s) | **7.7** | **1.84 W** |
| **Lantern 330-G** (galloping; generates to 40 m/s, 20 W from 15.5 m/s) | **10** | **0.40 W** |
| **Lantern 330-GH** (galloping; average 152 W from 15 to 40 m/s, 384 W at 40 m/s) | **12** | below cut-in (6.1 m/s) |
