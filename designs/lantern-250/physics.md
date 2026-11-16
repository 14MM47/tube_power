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
| U | Wind speed | 3–7 m/s |
| D | Tube diameter | 0.25 m |
| L | Tube length | 1.0 m |
| r₁, r₂ | Distance from hinge to bottom and top of the tube | 0.8 m, 1.8 m |
| St | Strouhal number | 0.2 |
| I_s | Structural inertia about the hinge (incl. generator rotor through the belt) | 0.458 kg·m² |
| I_a | Added (air) inertia | 0.107 kg·m² |
| m* | Mass ratio = I_s ÷ displaced-air inertia | 4.3 |
| θ | Hinge swing amplitude | ~0.115 rad (6.6°) |
| ω | Swing angular frequency | 2π × 3.6 rad/s at 4.5 m/s |
| ζ_e, ζ_p | Damping ratio from the generator; from everything else | 0.040, ~0.008 |
| G | Belt ratio | 26.2 |
| K_e | Generator voltage constant (= torque constant in SI) | 0.38 V·s/rad |

## 2. Wind power (established)

P_wind = ½ ρ U³ D L

Efficiency η is always quoted against this: the wind passing through the tube's frontal area, D × L. End discs are not counted. Other papers define efficiency differently (some include the swept band), so compare published percentages with care.

## 3. Vortex shedding and tuning (established; U* calibrated)

- A round tube sheds vortices alternately from each side at f_s = St · U / D, with St ≈ 0.2 for Reynolds numbers of roughly 300 to 200,000.
- The tube locks on when its natural frequency f_n is close to f_s.
- Power peaks at a reduced velocity U* = U / (f_n D) of about 5–6. The design uses **U* = 5.5**, so f_n = U / (5.5 D). This is a starting value: calibrate it on the rig.
- The calculator uses f_s for the swing frequency when computing power, and f_n for tuning.

Stiffness needed about the hinge:

k = (I_s + I_a) (2π f_n)² + k_g

where k_g = Σ m g h is the destabilising stiffness of the mass above the hinge (about 3 N·m/rad for B).

Two opposing springs of rate k_s at distance r below the hinge give k = 2 k_s r². So f_n ∝ r, and the carriage position is linear in wind speed.

## 4. Added mass and mass ratio (established)

- Air moving with the tube adds I_a = C_a ρ (π D²/4) ∫ r² dr over the tube length, with C_a = 1 (potential flow).
- The mass ratio is defined on the same r²-weighted basis: m* = I_s ÷ [ρ (π D²/4) ∫ r² dr].
- For a uniform shell of areal mass σ, the shell part alone is m* ≈ 4σ/(ρD). A fatter tube of the same skin therefore has a lower mass ratio.

**Low mass ratio (established, Govardhan & Williamson 2000):**
- The lower-branch frequency ratio is f* = √((m* + C_a)/(m* − 0.54)). At m* = 4.3 that is 1.19, so the swing frequency can rise about 19% above f_n while staying locked on.
- The synchronisation range widens as m* falls, and below about 0.54 it never ends.

This is why the Lantern's tuning is forgiving.

## 5. Swing amplitude (fitted)

The Skop–Griffin relation (as given in Blevins, *Flow-Induced Vibration*) gives the peak amplitude:

A_top / D = 1.29 γ / (1 + 0.43 S_G)^3.35

with:
- **S_G = 2π³ St² m* ζ**, where ζ = ζ_e + ζ_p. At St = 0.2, S_G = 2.48 m* ζ.
- **γ = √(∫φ² / ∫φ⁴)**, the mode-shape factor for mode shape φ = r / r₂. γ = 1 for parallel motion, 1.29 for a tube hinged at its base, 1.244 for B.

**Caution.** The relation was fitted to data at high mass ratios. It is used here at m* ≈ 4, which is an extrapolation. It does reproduce the published zero-friction efficiency limits (section 6), which gives some confidence.

## 6. Optimum generator load and efficiency

Power taken by the generator:

P = ζ_e I_s ω³ θ², with θ = A_top / r₂ and ω = 2π St U / D

Substituting the amplitude relation and maximising over ζ_e gives a closed form. Write x_p = m* ζ_p. Then:

- **Optimum generator damping:** m* ζ_e = (1 + 1.066 x_p) / 6.076
- **Best efficiency:** η_max = 0.289 Γ / (1 + 1.066 x_p)^5.7, multiplied by L_eff / L (section 9)

where Γ = (∫φ²)² / (L ∫φ⁴) is the share of parallel-motion output a hinged tube can reach:

| Neck (hinge below tube) | Γ |
|---|---|
| 0 (hinged at the base) | 0.556 |
| 0.4 m | 0.743 |
| 0.8 m | 0.847 |
| 1.0 m | 0.878 |
| Parallel motion | 1.000 |

**Checks against the literature:**
- With no friction, the model gives 29% for parallel motion and 16% for a base-hinged tube.
- Published values: theory for an elastically mounted cylinder 17–23% (arXiv 1407.5432; Ocean Engineering 2023). Michigan VIVACE measured 22%, and 28% with roughness strips (water).
- The Glasgow wake-oscillator model of a Vortex-style mast gives a 6% peak.

The model sits at the optimistic end, which is why the design quotes a **low case of half the model**.

**The key consequence:** efficiency depends on the product m* × ζ_p. A slim mast in air (m* = 70–220) loses most of its output to a damping ratio of 0.002–0.008. The Lantern at m* ≈ 4 hardly notices it.

## 7. Friction as damping (established method; values assumed)

Coulomb friction torque T_f becomes an equivalent viscous damping c = 4 T_f / (π θ ω), so ζ_f = c / (2 I_s ω). The calculator iterates, because θ depends on ζ. Friction sources at the hinge:

| Source | Model | B at 4.5 m/s |
|---|---|---|
| Hinge bushings | μ × (2 × drag moment ÷ bushing span + weight) × axle radius. Drag coefficient while swinging 2.0; μ = 0.15 | 0.10 N·m |
| Generator bearing and iron losses | 4 mN·m (assumed) × G | 0.10 N·m |
| Structure, springs, air | ζ = 0.003 (assumed) | — |
| **Total parasitic damping ratio** | | **ζ_p ≈ 0.008** |

Cogging torque is a magnetic spring, not a loss, so it is not in this table. It sets a start-up threshold instead ([README §9](README.md#9-drive-and-generator)).

## 8. Generator and gearing (established)

**Damping provided about the hinge:**

c_e = G² K_e² / (R_coil + R_load)

**Optimum circuit resistance:** R_total = G² K_e² / c_e, with c_e = 2 ζ_e I_s ω.

**Electrical output:**
- Copper efficiency = 1 − R_coil / R_total.
- Electrical power = mechanical power × belt efficiency (0.97) × copper efficiency × converter efficiency (0.85).

**Peak values:**
- Back-EMF = K_e G θ ω
- Generator speed = G θ ω

**Gearing trade-off.** A higher G raises copper efficiency (R_total ∝ G²). Against that:
- reflected rotor inertia grows as G²,
- friction seen at the hinge grows as G,
- the generator's rotation per swing grows.

In the sweep the optimum is the smallest practical GT2 pulley (10–12 teeth) on a 100 mm arc.

**Small vs large oscillators.** Direct magnet-and-coil generators suit small, fast oscillators: the 40 mm masts at ~22 Hz and ~0.1 N·m. Gearing suits slow, high-torque ones, like the Lantern at 2–6 Hz and 1–5 N·m.

## 9. End losses (assumed)

A tube only four diameters tall loses vortex strength near bare ends. The calculator models this as an effective length:

L_eff = L − 2 e D, where e = 0.5 × max(0, 1 − (disc ratio − 1)/(2.0 − 1))

- Half a diameter is lost per bare end.
- The loss falls linearly to zero at end discs of twice the tube diameter.

Published support is qualitative only:
- End plates suppress free-end effects (arXiv 2508.19050).
- Tubes shorter than 2 diameters stop shedding altogether when fixed, but still vibrate when free (Zhao & Cheng).

The disc results in the optimiser follow directly from this assumption.

## 10. Reynolds-number limit (established boundary of evidence)

The best measured oscillating-cylinder efficiencies cover Re = UD/ν ≈ 30,000–120,000 (VIVACE). Smooth cylinders change behaviour approaching the drag crisis (Re ≈ 200,000–300,000), and turbulence brings that on earlier.

The design limit is **Re ≤ 120,000 at the top tuned wind speed (7 m/s)**, which caps D at about 257 mm.

This is a limit on evidence, not a proven physical ceiling. Relaxing it is the obvious route to more power, and the obvious thing to test with roughness strips.

## 11. Structure (established)

- Survival drag: F = ½ ρ U_s² C_d D L with U_s = 25 m/s and C_d = 1.2.
- Moments: F L / 2 at the tube base, F (neck + L / 2) at the hinge.
- Skin stress: M / (π R² t) with an effective glass-skin thickness of t = 0.05 mm. The foam core prevents skin wrinkling, with an estimated wrinkling stress of about 60 MPa.
- Neck stress: M c / I.
- Euler buckling of a pinned rod: π² E I / L².
- Tip acceleration: θ ω² r₂.

## 12. Annual energy (method established; inputs assumed)

- Electrical power is integrated over a Rayleigh wind distribution with the site mean at hub height.
- Only winds from 0.8 × 3 m/s to 1.2 × 7 m/s count (the tuning range plus an assumed ±20% lock-on band).
- The result is multiplied by 0.5 for time lost to gusts, direction changes and retuning (assumed).
- The low case halves it again.

## 13. Key references

- Govardhan & Williamson (2000), *J. Fluid Mech.*: low-mass-ratio frequency response and critical mass ratio. [doi:10.1017/S0022112000001233](https://www.doi.org/10.1017/S0022112000001233)
- Ding, Bernitsas et al. (2016), *Renewable Energy*: VIVACE single cylinder with roughness strips, 28% measured. [Tethys summary](https://tethys-engineering.pnnl.gov/publications/numerical-simulation-experimental-validation-energy-harvesting-single-cylinder-vivace)
- VIVACE US DOE final report. [OSTI 896401](https://www.osti.gov/servlets/purl/896401)
- VIV harvesting efficiency optimum. [arXiv 1407.5432](https://arxiv.org/html/1407.5432)
- Barrero-Gil, Alonso & Sanz-Andrés (2010), *J. Sound Vib.*: galloping efficiency by cross-section. [UPM open access](https://oa.upm.es/7294/2/INVE_MEM_2010_78822.pdf)
- Hémon et al. (2017), *J. Fluids Struct.*: galloping prisms in a wind tunnel. [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0889974616303590)
- Breen, Mallik & Adhikari (2025), *Renewable Energy* 254:123549: Vortex-style mast model, 6% peak. [Glasgow eprint](https://eprints.gla.ac.uk/357207)
- Kinsey et al. (2010): oscillating-hydrofoil prototype, 40%. [FEDSM 2010 PDF](https://flair.monash.edu.au/intranet/proceedings/fedsm_icnmm2010/data/pdfs/trk-1/FEDSM-ICNMM2010-30869.pdf)
- Blevins, *Flow-Induced Vibration* (2nd ed.): Skop–Griffin amplitude relation and mode-shape factors.

Several of these pages could not be opened in full during the research, so their figures come from abstracts and search summaries. See [../../research/README.md](../../research/README.md).
