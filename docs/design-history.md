# Design history: from a bladeless mast to Lantern 250

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
