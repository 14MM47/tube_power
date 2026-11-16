# Lantern 330-G: the physics and the model

This explains every formula in [`tools/galloping_calc.py`](../../tools/galloping_calc.py). The structural parts follow the VIV design's model ([../lantern-250/physics.md](../lantern-250/physics.md)), adapted to a flat-sided prism. Nothing here has been measured on this machine.

## 1. Galloping, and how it differs from vortex shedding

A square prism in a steady wind feels a sideways force when the wind comes at it slightly from one side. For small angles the force points the same way as the angle, which is the opposite of what a streamlined body does: the flow separates at the front corners and reattaches on the side the wind leans towards, sucking the prism that way.

When the prism moves sideways at speed v, it sees the wind arriving at angle α = v/U from the side it is moving towards. The side force then pushes it further the way it is already moving. That is negative damping. Once it beats the friction and the generator's load, the swing grows until the force-versus-angle curve flattens and turns over at large angles. This is **galloping**.

| | Vortex shedding (Lantern 250-A/B/C) | Galloping (Lantern 330-G) |
|---|---|---|
| What drives it | Vortices shed alternately at f = St U / D | The prism's own motion tilting the wind it sees |
| Wind range | A lock-on band around the tuned speed; the springs must follow the wind | Every wind above onset; no band |
| Mass ratio | Decides everything: output falls steeply as the structure gets heavier | Does not enter the power at all (quasi-steady theory) |
| Output against wind | Large at low wind for a light tube; stops above ~11 m/s (generator heat, neck mode, drag crisis) | Small at low wind; grows roughly as U³ until a power rating, then held by pitch to 40 m/s |
| Reynolds number | Round tube: drag crisis above ~200,000 | Sharp corners fix separation: little Reynolds-number effect |
| Can it be switched off aerodynamically? | No: a fail-safe brake is the only protection | Yes: turned 45° the square is stable and the side force vanishes |

## 2. The side-force curve

The quasi-steady model treats the moving prism as if it were still, with the wind at the angle α its motion creates. The side force per unit length is

  F_y = ½ ρ U² D C_y(α),  C_y(α) = A1 α − A3 α³

with D the face width. For a square in smooth flow, **A1 = 2.3 and A3 = 18**, the cubic fit used in most galloping energy-harvesting studies (another reported fit: 2.2961 and 18.714). It matches the measured curve's start and its turn: the cubic peaks at 11.8° and crosses zero at 20.5°, where the measured square curve also turns over. Parkinson and Smith's seventh-order polynomial for the square is more detailed, but this model uses the cubic throughout.

Other sections are in the calculator for sensitivity runs only: an isosceles triangle with a 30° apex (A1 = 2.9, A3 = 6.2) and a D-section (A1 = 0.79, A3 = 0.19). Those values came from literature summaries whose sources could not be checked, and their drag tables in the calculator are guesses.
- On 330-G's geometry, the triangle gives about 25% more yearly energy than the square, with a flow-angle cap of 0.30 rad, but cuts in later.
- The D-section's A1 is too small to overcome friction.

Measure before choosing.

The theory only holds when the swing is slow compared with vortex shedding. The calculator requires **U/(fD) ≥ 20** (vortex resonance for a square is at U/(fD) = 1/St ≈ 7.7) and keeps the flow angle at the prism top below 0.40 rad (23°).

## 3. The hinged prism: harmonic balance

The prism swings about a horizontal hinge axis that points into the wind, so it moves across the wind. A point at height r above the hinge moves at v = θ̇ r. With θ = Θ sin ωt and peak hinge rate V = Θω, averaging the side force's work over a cycle gives the aerodynamic power

  P_aero = a V² − b V⁴

  a = ¼ ρ U D A1 I₂ k,  b = (3/16) ρ D A3 I₄ k / U

where I₂ = ∫ r² dr and I₄ = ∫ r⁴ dr over the prism span (neck to neck + L), and k is the span factor for end losses (section 7).

The machine absorbs ½ c V² in damping (c = generator plus structural) and (2/π) T V in Coulomb friction T (bearings, generator drag). The steady swing satisfies

  (a − c/2) V − b V³ = (2/π) T

The calculator takes the largest root, which is the stable one. Without friction:

- V² = (a − c/2) / b
- the best generator load is c_e = a − c_s/2
- the most power is P = (a − c_s/2)² / (4b)

With no friction at all, the share of the wind through the prism (½ ρ U³ D L) that can be captured is

  η = A1² I₂² / (6 A3 I₄ L) × k

That is 4.9% for a prism translating sideways, and less for a hinged one: I₂²/(I₄ L) is 0.56 with no neck and 0.80 with 330-G's 600 mm neck. 330-G's ceiling is 3.9% (its end plates remove the end loss). That is roughly a fifth of what the light VIV tube reaches at its tuned speed. Galloping makes up for it only by working at every wind speed.

A time-step simulation of the hinged prism with the full force distribution along its span agrees with this harmonic balance to within 1% on power and swing, face-on and pitched. While pitched, the simulated steady lean is about 20% smaller than the calculator's, because the α² term reduces the mean side force. The calculator ignores that reduction, which errs on the safe side.

Two things do **not** appear in the power:
- **The prism's mass.** It sets the frequency for a given spring, and the inertial loads, but not the energy. So the prism can be built sturdy.
- **The swing frequency.** For a given swing rate V the power is the same at any frequency. The frequency only decides how big the swing angle is (Θ = V/ω).

At the optimum, the flow angle at the prism top is α_top = V r₂ / U ≈ 0.37 rad (21°) for the square with a 600 mm neck. That is inside the range the cubic is trusted at.

## 4. Choosing the swing frequency

Because frequency does not change the power but does change everything else, the controller sets it from the swing it wants. It picks the **lowest frequency that keeps swing plus static lean within the design stroke** (±15°, inside ±20° rubber stops):

  V/ω + M₀/(I ω²) ≤ θ_design

M₀ is the steady side-force moment when the prism is pitched (section 5), and I is the total inertia including air and the generator rotor.

Low frequency keeps the inertial loads (∝ Θω²), the spring forces and the fatigue cycles down. It also keeps the theory valid: the frequency lands at U/(fD) ≈ 22 at every wind, above the required 20.

The frequency comes from two springs on a carriage below the hinge, as in Lantern 250-B, but with a longer travel (15–140 mm). At its lowest the springs barely beat gravity, since the upright prism is an inverted pendulum. Limits:
- the top of the spring range;
- the neck-and-prism bending mode ÷ 1.5;
- U/(fD) ≥ 20.

In practice the control is simple: **adjust the carriage until the swing is ±15°**.

## 5. Throttling by pitch, and feathering

Above the rating the controller turns the prism about its own vertical axis by a pitch angle β. The wind then meets it at mean angle β, and the swing adds small angles around that. Expanding the cubic about β:

  C_y(β + α) − C_y(β) = (A1 − 3 A3 β²) α − 3 A3 β α² − A3 α³

The α² term does no work over a symmetric cycle. So pitch simply replaces A1 with

  A1_eff(β) = A1 − 3 A3 β²

which falls to zero at β = 11.8° for the square. A few degrees of pitch cut the power steeply.

Pitch has costs:
- It adds a **steady side force** C_y(β) q D L, which leans the prism over by M₀/(Iω²) and eats into the stroke.
- It changes the drag. Drag on a square falls from C_d = 2.1 face-on to about 1.45 at 13°. The model takes 1.65 at 45° (drag referred to the face width throughout).

**Feathered** means turned to 45°. The diamond orientation is symmetric, so the steady side force is zero, and it does not gallop. Above the 40 m/s cut-out, or on any fault, the pitch drive feathers the prism and the generator is shorted.

The controller searches pitch from 0 upwards in 0.3° steps. At each pitch it tries:
- the generator load giving the most power;
- heavier loads (overdamping) that hold the swing, the flow angle or the output down to a limit.

It keeps the highest output that respects every limit and the rating. When many pitch-and-load pairs give the rated output, it chooses the lightest generator load. That is classic pitch regulation: least copper loss, and furthest from the point where friction would stop the swing in a lull.

## 6. Generator and drive

The generator's damping at the hinge is c_e = G² Ke² / R_total, through a belt of ratio G. Its largest value (terminals shorted) is c_max = G² Ke² / R_coil, and its copper efficiency is 1 − c_e / c_max. The calculator checks:
- winding heat (copper loss);
- peak speed;
- peak EMF;
- that the circuit resistance stays above 1.2 × the coil's.

Two generator classes are modelled. Their values are **assumed** for the size class, so measure your motor:

| Preset | Ke (V s/rad) | R (Ω) | Rotor J (kg m²) | Drag at shaft (N m) | Heat limit (W) | Max rpm |
|---|---|---|---|---|---|---|
| `5208` gimbal motor (as Lantern 250-B) | 0.38 | 12 | 6 × 10⁻⁵ | 0.004 | 5 | 1,500 |
| `8108` pancake outrunner, ~100 W class, wound for ~24 V | 0.20 | 0.8 | 2.5 × 10⁻⁴ | 0.010 | 20 | 3,000 |

The trade is between drag at low wind (drag × G is friction at the hinge, which sets the cut-in) and the load needed at high wind (c_max must be several times the optimum load to keep copper losses down).

The hinge runs on **two sealed deep-groove ball bearings**, not polymer bushings. Rolling friction (μ = 0.005 at the axle) plus 0.05 N m of seal drag is a tiny fraction of what bushings would give under storm drag. The usual worry with ball bearings on a rocking shaft, false brinelling, is much smaller here: the swing is always about ±15°, far larger than the ball spacing angle.

## 7. Mass, inertia and end losses

The prism has four flat panels (face width D, height L), internal bulkheads every 250 mm (half-weight, with lightening holes) and corner tapes. Square end plates of side `plate_ratio` × D close the ends. Inertia about the hinge is summed as for the VIV tube. Added air inertia uses 1.19 × ρπD²/4 per unit length, the potential-flow value for a square.

End losses use the same assumption as the VIV design: half a face width of span lost at each bare end, recovered linearly by end plates up to twice the face width.

## 8. Structural checks (each as a utilisation, 100% = at the allowable)

| Check | Model |
|---|---|
| Neck (peak) | √(M_drag² + (M_side + M_cyc)²) at the neck root ÷ section modulus, against 400 MPa. M_cyc combines the inertial moment I_above Θ ω² with the aerodynamic moment (c V + 4T/π) in quadrature |
| Neck fatigue | M_cyc ÷ section modulus against 200 MPa |
| Skin | Bending at the prism base (drag, steady side force, inertia) ÷ (4/3) t D², the thin-walled square box with the outer skin only, against the panel material's allowable |
| Panels | Net pressure 2.0 q on a panel simply supported on the corners and bulkheads: M = β(b/a) p a² (Timoshenko's plate coefficients; one-way spanning p s²/8 for corrugated board) against the panel's capacity |
| End plates | Gust lift C_L = 1.1 on the overhang, as a cantilever |
| Hub | Drag moment at the hinge against the hub's rating (800 N m for 330-G) |
| Stroke | (swing + lean) ÷ design stroke |
| Springs | Spring force at full stroke against 1,500 N |
| Neck mode | 1.5 × swing frequency ÷ neck-and-prism bending frequency |
| Quasi-steady | 20 × f D / U (must stay ≤ 1, i.e. U/(fD) ≥ 20) |
| Flow angle | α_top ÷ 0.40 rad |
| Generator | Heat, speed, voltage, load (as section 6) |

**Survival** is checked feathered and braked. All parked loads scale with q, so each part's survival wind is 10 m/s ÷ √(utilisation at 10 m/s). The requirement is 45 m/s, a margin over the 40 m/s cut-out.

## 9. Yearly energy

Yearly energy is integrated over a Rayleigh wind distribution at hub height. The calculator credits **80% of the model output** for yaw lag, gusts and restarts after lulls; the low case is half of central. There is no lock-on factor (the VIV designs use 0.5), because galloping has no band to fall out of.

## 10. What is uncertain, in order of importance

1. **Turbulence.** The coefficients are smooth-flow values. Garden-height wind has 15–25% turbulence, which flattens a square's side-force curve. With A1 cut by 20% (`--turb_factor 0.8`) the yearly energy at a 4.5 m/s site falls from 6.2 to 3.7 kWh (−40%), and cut-in rises from 2.5 to 3.0 m/s. This is the single biggest unknown.
2. **The side-force curve itself** beyond ~15°, and its hysteresis. The square's onset is reliable; the cubic's large-angle shape less so.
3. **Finite span.** A 1 m prism with end plates is assumed close to two-dimensional.
4. **The feathered orientation.** 45° is assumed stable with Cd = 1.65; check it in the static test.
5. **Generator constants and drag**, which set the cut-in.
6. **Panel pressures** near the leading corners at 40 m/s.

The first build step is therefore a **static side-force test**. Mount the prism on a car-roof rig with a load cell, measure C_y against angle from −25° to +25° at a few speeds, then put the fitted A1 and A3 into the calculator.
