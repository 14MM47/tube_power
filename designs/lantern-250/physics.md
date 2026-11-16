# Lantern 250: physics and models

This file explains every model used in [`tools/lantern_calc.py`](../../tools/lantern_calc.py), with the assumptions behind each one. Section numbers are referenced from the [design specification](README.md).

**Confidence key**
- **Established:** textbook or well-replicated results.
- **Fitted:** empirical fits used outside their data range.
- **Assumed:** engineering judgement that needs testing.

## 1. Notation

| Symbol | Meaning | Lantern 250-B |
|---|---|---|
| ρ | Air density | 1.225 kg/m³ |
| ν | Kinematic viscosity of air | 1.5 × 10⁻⁵ m²/s |
| U | Wind speed | 0–40 m/s |
| q | Dynamic pressure, ½ρU² | 980 Pa at 40 m/s |
| D | Tube diameter | 0.25 m |
| L | Tube length | 1.0 m |
| r₁, r₂ | Distance from hinge to bottom and top of the tube | 0.8 m, 1.8 m |
| St | Strouhal number | 0.2 |
| I_s | Structural inertia about the hinge (incl. generator rotor through the belt) | 0.585 kg·m² |
| I_a | Added (air) inertia | 0.107 kg·m² |
| m* | Mass ratio = I_s ÷ displaced-air inertia | 5.5 |
| θ | Hinge swing amplitude | ~0.113 rad (6.5°) at 4.5 m/s |
| ω | Swing angular frequency | 2π × 3.6 rad/s at 4.5 m/s |
| ζ_e, ζ_p | Damping ratio from the generator; from everything else | 0.031, ~0.007 at 4.5 m/s |
| G | Belt ratio | 26.2 |
| K_e | Generator voltage constant (= torque constant in SI) | 0.38 V·s/rad |

## 2. Wind power (established)

P_wind = ½ ρ U³ D L

Efficiency η is always quoted against this: the wind passing through the tube's frontal area, D × L. End discs are not counted. Other papers define efficiency differently (some include the swept band), so compare published percentages with care.

## 3. Vortex shedding and tuning (established; U* calibrated)

- A round tube sheds vortices alternately from each side at f_s = St · U / D, with St ≈ 0.2 for Reynolds numbers of roughly 300 to 200,000.
- The tube locks on when its natural frequency f_n is close to f_s.
- Power peaks at a reduced velocity U* = U / (f_n D) of about 5–6. The design uses **U* = 5.5**, so f_n = U / (5.5 D). This is a starting value: calibrate it on the rig.
- The calculator uses f_s for the swing frequency when computing power, and f_n for tuning. Outside the tuning range f_n is held at the end of the range.

Stiffness needed about the hinge:

k = (I_s + I_a) (2π f_n)² + k_g

where k_g = Σ m g h is the destabilising stiffness of the mass above the hinge (about 4 N·m/rad for B).

Two opposing springs of rate k_s at distance r below the hinge give k = 2 k_s r². So f_n ∝ r, and the carriage position is linear in wind speed.

## 4. Added mass and mass ratio (established)

- Air moving with the tube adds I_a = C_a ρ (π D²/4) ∫ r² dr over the tube length, with C_a = 1 (potential flow).
- The mass ratio is defined on the same r²-weighted basis: m* = I_s ÷ [ρ (π D²/4) ∫ r² dr].
- For a uniform shell of areal mass σ, the shell part alone is m* ≈ 4σ/(ρD). A fatter tube of the same skin therefore has a lower mass ratio.

**Low mass ratio (established, Govardhan & Williamson 2000):**
- The lower-branch frequency ratio is f* = √((m* + C_a)/(m* − 0.54)). At m* = 5.5 that is 1.15, so the swing frequency can rise about 15% above f_n while staying locked on.
- The synchronisation range widens as m* falls, and below about 0.54 it never ends.

This is why the Lantern's tuning is forgiving, and also why it cannot rely on dropping out of lock-on for protection (section 9).

## 5. Swing amplitude (fitted)

The Skop–Griffin relation (as given in Blevins, *Flow-Induced Vibration*) gives the peak amplitude:

A_top / D = 1.29 γ / (1 + 0.43 S_G)^3.35

with:
- **S_G = 2π³ St² m* ζ**, where ζ = ζ_e + ζ_p. At St = 0.2, S_G = 2.48 m* ζ.
- **γ = √(∫φ² / ∫φ⁴)**, the mode-shape factor for mode shape φ = r / r₂. γ = 1 for parallel motion, 1.29 for a tube hinged at its base, 1.244 for B.

**Caution.** The relation was fitted to data at high mass ratios. It is used here at m* ≈ 5, which is an extrapolation. It does reproduce the published zero-friction efficiency limits (section 6), which gives some confidence.

## 6. Optimum generator load and efficiency

Power taken by the generator:

P = ζ_e I_s ω³ θ², with θ = A_top / r₂ and ω = 2π St U / D

Substituting the amplitude relation and maximising over ζ_e gives a closed form. Write x_p = m* ζ_p. Then:

- **Optimum generator damping:** m* ζ_e = (1 + 1.066 x_p) / 6.076
- **Best efficiency:** η_max = 0.289 Γ / (1 + 1.066 x_p)^5.7, multiplied by L_eff / L (section 11)

where Γ = (∫φ²)² / (L ∫φ⁴) is the share of parallel-motion output a hinged tube can reach:

| Neck (hinge below tube) | Γ |
|---|---|
| 0 (hinged at the base) | 0.556 |
| 0.4 m | 0.743 |
| 0.6 m | 0.804 |
| 0.8 m | 0.847 |
| 1.0 m | 0.878 |
| Parallel motion | 1.000 |

**Checks against the literature:**
- With no friction, the model gives 29% for parallel motion and 16% for a base-hinged tube.
- Published values: theory for an elastically mounted cylinder 17–23% (arXiv 1407.5432; Ocean Engineering 2023). Michigan VIVACE measured 22%, and 28% with roughness strips (water).
- The Glasgow wake-oscillator model of a Vortex-style mast gives a 6% peak.

The model sits at the optimistic end, which is why the design quotes a **low case of half the model**.

**The key consequence:** efficiency depends on the product m* × ζ_p. A slim mast in air (m* = 70–220) loses most of its output to a damping ratio of 0.002–0.008. The Lantern at m* ≈ 5.5 hardly notices it.

## 7. Friction as damping (established method; values assumed)

Coulomb friction torque T_f becomes an equivalent viscous damping c = 4 T_f / (π θ ω), so ζ_f = c / (2 I_s ω). The calculator iterates, because θ depends on ζ. Friction sources at the hinge:

| Source | Model | B at 4.5 m/s |
|---|---|---|
| Hinge bushings | μ × (2 × drag moment ÷ bushing span + weight) × axle radius. Drag coefficient while swinging 2.0; μ = 0.15 | 0.10 N·m |
| Generator bearing and iron losses | 4 mN·m (assumed) × G | 0.10 N·m |
| Structure, springs, air | ζ = 0.003 (assumed) | — |
| **Total parasitic damping ratio** | | **ζ_p ≈ 0.007** |

Cogging torque is a magnetic spring, not a loss, so it is not in this table. It counts in the start-up check (section 9).

## 8. Generator and gearing (established)

**Damping provided about the hinge:**

c_e = G² K_e² / (R_coil + R_load)

**Optimum circuit resistance:** R_total = G² K_e² / c_e, with c_e = 2 ζ_e I_s ω.

**Electrical output:**
- Copper efficiency = 1 − R_coil / R_total.
- Electrical power = mechanical power × belt efficiency (0.97) × copper efficiency × converter efficiency (0.85).
- Winding heat = I_peak² R_coil / 2, with I_peak = K_e G θ ω / R_total.

**Peak values:**
- Back-EMF = K_e G θ ω
- Generator speed = G θ ω

**Gearing trade-off.** A higher G raises copper efficiency (R_total ∝ G²). Against that:
- reflected rotor inertia grows as G²,
- friction seen at the hinge grows as G,
- the generator's rotation per swing grows.

In the sweep the optimum is the smallest practical GT2 pulley (10–12 teeth) on a 100 mm arc.

**Small vs large oscillators.** Direct magnet-and-coil generators suit small, fast oscillators: the 40 mm masts at ~22 Hz and ~0.1 N·m. Gearing suits slow, high-torque ones, like the Lantern at 1.6–6 Hz and 1–5 N·m.

## 9. Operating modes across 0–40 m/s

The calculator's `operate()` follows these control rules at each wind speed U.

| Mode | Condition (defaults) | Model |
|---|---|---|
| Idle | U below 0.8 × lowest tuned speed (1.6 m/s), or the start-up check fails | No swing, no output |
| Tracking | 1.6 m/s ≤ U ≤ 7 m/s | f_n set to the wind (clipped to 2–7 m/s); optimum generator load (section 6) |
| Power-capped | 7 m/s < U < 8 m/s (brake speed) | f_n held at the 7 m/s setting. If the optimum output exceeds the rated power (output at 7 m/s), generator damping is raised by bisection until output equals the cap. If even near-short-circuit damping can't hold it, the mode becomes braked |
| Braked | U ≥ 8 m/s | Generator damping set by a shorted or resistor-loaded winding: c = G²K_e²/(R_coil + R_brake). Within the assumed lock-on reach (up to 1.2 × 7 = 8.4 m/s) a residual swing is computed with that damping; above it the tube is assumed not to lock on |

**Start-up check (assumed values).**
- A still tube feels a fluctuating lift moment M = ½ρU² C_L D L_eff (r₁ + L/2), with C_L = 0.3.
- It starts if that exceeds bushing friction plus generator drag × G, plus cogging × G when there is no kick-start.
- With kick-start the motor pushes the tube into swinging, and cogging (a conservative magnetic spring) no longer stops it.

**Lock-on reach (assumed ±20%).** At low mass ratio the synchronisation range is wider than in typical air tests (section 4). The lock-on reach therefore cannot be relied on to stop the swing. The brake does that.

**Why the default caps and then brakes (model results for B).** Holding output at the 7 m/s value by raising generator damping increases winding current. Winding heat reaches the assumed 5 W limit near 8.4 m/s, so the brake speed is set at 8 m/s.

**Keep-generating control (`keep_generating = 1`).** The alternative control in `operate_limits()`:
- **Retuning:** the tube may retune up to the lower of `U_tune_ext_max` (default 40 m/s) and the neck-mode limit (section 12a), with springs assumed rebuilt for the stiffness that needs.
- **Lock-on tail:** beyond that it rides the lock-on tail to +20%.
- **Generator load:** at each wind it searches generator damping from 0.2× to well above the optimum, up to the near-short-circuit maximum. It keeps the highest electrical output whose swinging loads are all at or under 100%: neck peak, fatigue and bending mode; skin; wall; discs; hub; voltage; generator heat. Running below the optimum damping cuts winding current, which is how it keeps the generator cool at higher winds.
- **Where it stops:**
  - no damping satisfies every limit (for B and C the generator's heat limit, at about 11–12 m/s),
  - the Reynolds number passes `Re_harvest_max` (200,000, which is 12 m/s for a 250 mm tube),
  - the wind is beyond the lock-on reach of the highest tuning.

**Model potential.** The output from `solve()` at the optimum load with no limits at all, assuming the tube stays tuned and locked on at every wind speed. It is a reference line, not an achievable output. It flattens above ~30 m/s because even this generator's short-circuit damping can't absorb the swing efficiently.

## 10. Reynolds-number regimes (established boundary of evidence)

| Re = UD/ν | For D = 250 mm | Behaviour | Treatment |
|---|---|---|---|
| ≤ 120,000 | ≤ 7 m/s | Range of the best measured oscillating-cylinder efficiencies (VIVACE) | "tested": design range |
| 120,000–200,000 | 7–12 m/s | Subcritical, but no harvesting data | "beyond tested"; capped then braked |
| > 200,000 | > 12 m/s | Approaching and inside the drag crisis: drag falls (C_d ~0.3–0.7 for smooth cylinders) and shedding becomes weaker and less regular. Roughness and turbulence move the crisis earlier | Structure uses C_d = 1.2 throughout (no credit) |

The design limit is **Re ≤ 120,000 at the top tuned wind speed (7 m/s)**, which caps D at about 257 mm. This is a limit on evidence, not a proven physical ceiling.

## 11. End losses (assumed)

A tube only four diameters tall loses vortex strength near bare ends. The calculator models this as an effective length:

L_eff = L − 2 e D, where e = 0.5 × max(0, 1 − (disc ratio − 1)/(2.0 − 1))

- Half a diameter is lost per bare end.
- The loss falls linearly to zero at end discs of twice the tube diameter.

Published support is qualitative only:
- End plates suppress free-end effects (arXiv 2508.19050).
- Tubes shorter than 2 diameters stop shedding altogether when fixed, but still vibrate when free (Zhao & Cheng).

The disc results in the optimiser follow directly from this assumption.

## 12. Structural checks at every wind speed

Each check gives a utilisation (load ÷ allowable). Over 100% fails. The drag coefficient is 2.0 while swinging (VIV raises mean drag) and 1.2 when parked.

| Check | Load | Allowable (default) | Confidence |
|---|---|---|---|
| **Neck, peak** | √(M_drag² + M_swing²) × c / I, where M_drag = F (r₁ + L/2) is about the cross-wind axis and M_swing = I_above θ ω² is the swing's inertia about the hinge axis (perpendicular, so they add as vectors) | 400 MPa (carbon, ~40% of strength) | Established method; allowable assumed |
| **Neck, fatigue** | M_swing × c / I | 200 MPa cyclic amplitude for ~10⁸ cycles | Assumed |
| **Neck mode** | 1.5 × swing frequency ÷ neck-tube bending frequency (section 12a) | 1.0 | Approximate model |
| **Skin** (tube bending at its base) | √(M_drag,base² + M_swing,base²) / (π R² t_skin), with M_drag,base = F L/2 and the swing moment from the shell and top disc above the base | 40 MPa (glass tissue on foam) | Established method; allowable assumed |
| **Wall** (ovalling) | k q R² per unit length, k = 0.5. Ring bending from the cos 2θ part of the pressure round a cylinder (front +1 q, sides about −1 to −2 q); amplitude taken as 1.5 q, giving M = 1.5 q R²/3. Internal rings ignored (conservative) | Sandwich: σ_skin × t_inner × core thickness. Single skin: σ_foam × core²/2 with σ_foam = 0.25 MPa | Assumed |
| **Discs** (gust lift) | C_L q w²/2 per unit length at the disc root, C_L = 1.1 (flat plate, ~10° gust inflow), w = disc overhang beyond the tube | Same wall formula as the disc's construction | Assumed |
| **Hub** | M_drag at the hinge | M_hinge_max: what the hub, bushings and post head are built for (150 N·m for B, 350 for C) | Design input |
| **Voltage** | Peak EMF while swinging | 150 V electronics rating | Design input |
| **Generator heat** | Winding loss while swinging or braking | 5 W | Assumed |

Also reported: bushing load (drag moment ÷ bushing span, plus half the weight and swing inertia force); post base moment F (h_hub + r₁ + L/2) + head drag × h_hub; top-of-tube acceleration θ ω² r₂.

**12a. Neck bending mode (approximate).** The swing is modelled as a rigid tube rocking on its hinge. That holds only while the neck and tube's own bending frequency stays well above the swing frequency.
- **Model:** the neck is a cantilever from a rigid hinge, with the tube as a rigid body on its tip: mass plus added air, rotary inertia, centre L/2 above the tip. That gives a 2 × 2 eigenproblem for sideways movement and rotation at the neck tip. Holding the hinge rigid gives a lower bound on the real second mode.
- **Check:** utilisation = 1.5 × swing frequency ÷ bending frequency, so the swing must stay below two-thirds of the bending frequency.
- **Results:**
  - B's 35 × 32 mm, 800 mm neck: 14.5 Hz, so retuning is capped at 12 m/s.
  - C's 35 × 32 mm, 600 mm neck: 16 Hz, so 13 m/s.
  - The 30 × 28 mm neck first specified for B: 9.6 Hz, only 8 m/s, which is why it was changed.
- **Locked hinge:** with the hinge locked the same mode is reached by vortices at about 1.25 × its frequency (m/s), so a locked neck would resonate in moderate winds.

**Survival wind.** Parked and braked, every check above scales with q (U²). So each part's survival wind is 10 m/s ÷ √(utilisation at 10 m/s). The design's survival wind is the lowest of the neck, skin, wall, disc and hub values.

**Neck sizing in the grid search.** For each design the calculator picks the lightest of five standard carbon tubes (25×23 to 50×47 mm) whose neck survival wind meets the requirement and whose fatigue and bending-mode utilisations stay under 100% up to the brake speed.

## 13. Annual energy (method established; inputs assumed)

- Electrical power from the operating-mode envelope (section 9) is integrated over a Rayleigh wind distribution with the site mean at hub height.
- Only swinging modes count. With the default control, power is capped from 7 to 8 m/s and zero when braked. With the keep-generating control, the integral runs to the highest wind it can harvest.
- The result is multiplied by 0.5 for time lost to gusts, direction changes and retuning (assumed).
- The low case halves it again.

## 14. Key references

- Govardhan & Williamson (2000), *J. Fluid Mech.*: low-mass-ratio frequency response and critical mass ratio. [doi:10.1017/S0022112000001233](https://www.doi.org/10.1017/S0022112000001233)
- Ding, Bernitsas et al. (2016), *Renewable Energy*: VIVACE single cylinder with roughness strips, 28% measured. [Tethys summary](https://tethys-engineering.pnnl.gov/publications/numerical-simulation-experimental-validation-energy-harvesting-single-cylinder-vivace)
- VIVACE US DOE final report. [OSTI 896401](https://www.osti.gov/servlets/purl/896401)
- VIV harvesting efficiency optimum. [arXiv 1407.5432](https://arxiv.org/html/1407.5432)
- Barrero-Gil, Alonso & Sanz-Andrés (2010), *J. Sound Vib.*: galloping efficiency by cross-section. [UPM open access](https://oa.upm.es/7294/2/INVE_MEM_2010_78822.pdf)
- Hémon et al. (2017), *J. Fluids Struct.*: galloping prisms in a wind tunnel. [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0889974616303590)
- Breen, Mallik & Adhikari (2025), *Renewable Energy* 254:123549: Vortex-style mast model, 6% peak. [Glasgow eprint](https://eprints.gla.ac.uk/357207)
- Kinsey et al. (2010): oscillating-hydrofoil prototype, 40%. [FEDSM 2010 PDF](https://flair.monash.edu.au/intranet/proceedings/fedsm_icnmm2010/data/pdfs/trk-1/FEDSM-ICNMM2010-30869.pdf)
- Blevins, *Flow-Induced Vibration* (2nd ed.): Skop–Griffin amplitude relation, mode-shape factors, ring and shell formulas.

Several of these pages could not be opened in full during the research, so their figures come from abstracts and search summaries. See [../../research/README.md](../../research/README.md).
