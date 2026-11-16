# Lantern G calculator report

square prism 330 mm x 1000 mm, neck 800 mm (50x47 mm carbon), end plates 660 mm square, panels 0.460 kg/m^2 (capacity 20 N m/m), generator hub500, HTD8M-20 belt, 275 mm arc to 22-tooth pulley (9.8:1), springs to 4 Hz (3000 N each), swing ±25°, no power cap, hub 1200 N m, survival requirement 45 m/s

Constraint check: all pass

## Operating summary

- Cut-in (starts with kick-start and makes >10 mW): 6.1 m/s; generates without a gap to **40.0 m/s**; feathers above 40 m/s
- No power cap. Mean electrical output from 15 to 40 m/s **152.4 W**; 18.3 W at 15 m/s, 383.6 W at 40 m/s. No pitch regulation: face-on to cut-out, then feathered
- Survives feathered (45°) and braked up to **46.7 m/s**, limited by the end plates. Requirement 45 m/s. Per part: neck 50, skin 72, panels 61, end plates 47, hub 53
- Swing frequency range 0.24-4.00 Hz (spring carriage 15-140 mm); neck-and-prism bending mode 13.0 Hz
- Quasi-steady theory trusted from U/(fD) = 20; vortex-shedding resonance would be at U/(fD) = 7.7
- Yearly energy, central case (kWh): 3.5 m/s site 0.6; 4.5 m/s site 2.6; 5.5 m/s site 7.1; 6.5 m/s site 14.4; 7.5 m/s site 25.2

## Masses (kg)

| Part | Mass |
|---|---|
| Prism panels, 3 bulkheads, corner tapes | 0.712 |
| End plates, each (660 mm square) | 0.200 |
| Bottom spider | 0.020 |
| Neck tube | 0.283 |
| Hub, axle, carriage, belt arc, pitch drive | 0.997 |
| **Total swinging mass** | **2.414** |

## Inertia about the hinge (kg m^2)

| Part | Inertia |
|---|---|
| shell | 1.2632 |
| plates | 0.7920 |
| spider | 0.0128 |
| neck | 0.0605 |
| hub | 0.0049 |
| generator | 0.7711 |
| Air moving with the prism | 0.2211 |
| **Total** | **3.1255** |
| Mass ratio (structural / displaced air) | 12.28 |

- Gear ratio 9.8:1 (275 mm arc to 22-tooth HTD8M-20 pulley); generator damping at the hinge up to 180.7 N m s/rad (terminals shorted)
- Span factor after end losses 1.000; frictionless capture ceiling A1² I2² / (6 A3 I4 L) = 4.15 % of the wind through the prism
- Gravity (destabilising) stiffness 15.5 N m/rad; two springs of 50.76 N/mm each
- Panel bending per unit dynamic pressure 8.80 x 10^-3 m^2 (bulkheads every 0.250 m)

## Wind envelope

Utilisation = load / allowable (over 100% fails). The controller keeps every one at or under 100% while generating; above cut-out the prism is feathered (45°) and braked. Stroke = swing plus steady lean against the design stroke; quasi-steady = how close the swing frequency is to the highest the galloping model is trusted at.

| Wind (m/s) | Mode | Pitch (°) | Swing f (Hz) | U/(fD) | Swing (±°) | Lean (°) | Elec (W) | Gen load (N m s/rad) | EMF (V) | Gen heat (W) | Neck | Fatigue | Skin | Panels | Hub | Stroke | Springs | Belt | Worst |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | idle (below quasi-steady range) | 0.0 | - | - | 0.0 | 0.0 | 0.00 | 0.00 | 0 | 0.0 | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0% | end plates 0% |
| 2 | idle (friction) | 0.0 | - | - | 0.0 | 0.0 | 0.00 | 0.00 | 0 | 0.0 | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0% | end plates 0% |
| 3 | idle (friction) | 0.0 | - | - | 0.0 | 0.0 | 0.00 | 0.00 | 0 | 0.0 | 0% | 0% | 0% | 0% | 0% | 0% | 0% | 0% | end plates 0% |
| 4 | idle (friction) | 0.0 | - | - | 0.0 | 0.0 | 0.00 | 0.00 | 0 | 0.0 | 1% | 0% | 0% | 0% | 1% | 0% | 0% | 0% | end plates 1% |
| 4.5 | idle (friction) | 0.0 | - | - | 0.0 | 0.0 | 0.00 | 0.00 | 0 | 0.0 | 1% | 0% | 0% | 1% | 1% | 0% | 0% | 0% | end plates 1% |
| 5 | idle (friction) | 0.0 | - | - | 0.0 | 0.0 | 0.00 | 0.00 | 0 | 0.0 | 1% | 0% | 0% | 1% | 1% | 0% | 0% | 0% | end plates 1% |
| 6 | generating | 0.0 | 0.36 | 51 | 25.0 | 0.0 | 0.01 | 0.01 | 7 | 0.0 | 2% | 1% | 1% | 1% | 2% | 100% | 13% | 1% | flow angle 74% |
| 7 | generating | 0.0 | 0.45 | 47 | 25.0 | 0.0 | 0.57 | 0.92 | 9 | 0.0 | 3% | 2% | 1% | 1% | 2% | 100% | 15% | 1% | flow angle 79% |
| 8 | generating | 0.0 | 0.53 | 46 | 25.0 | 0.0 | 1.42 | 1.63 | 11 | 0.0 | 3% | 2% | 2% | 2% | 3% | 100% | 16% | 2% | flow angle 82% |
| 10 | generating | 0.0 | 0.69 | 44 | 25.0 | 0.0 | 4.11 | 2.83 | 14 | 0.1 | 5% | 4% | 3% | 3% | 5% | 100% | 20% | 3% | flow angle 85% |
| 12 | generating | 0.0 | 0.84 | 43 | 25.0 | 0.0 | 8.37 | 3.87 | 17 | 0.2 | 8% | 5% | 4% | 4% | 7% | 100% | 24% | 4% | flow angle 87% |
| 15 | generating | 0.0 | 1.07 | 42 | 25.0 | 0.0 | 18.30 | 5.32 | 22 | 0.7 | 12% | 9% | 6% | 6% | 10% | 100% | 29% | 6% | flow angle 88% |
| 17.5 | generating | 0.0 | 1.26 | 42 | 25.0 | 0.0 | 30.44 | 6.46 | 25 | 1.3 | 17% | 12% | 8% | 8% | 14% | 100% | 34% | 8% | flow angle 89% |
| 20 | generating | 0.0 | 1.44 | 42 | 25.0 | 0.0 | 46.68 | 7.57 | 29 | 2.4 | 22% | 15% | 10% | 11% | 18% | 100% | 38% | 11% | flow angle 89% |
| 25 | generating | 0.0 | 1.81 | 42 | 25.0 | 0.0 | 93.49 | 9.74 | 37 | 6.3 | 34% | 24% | 16% | 17% | 29% | 100% | 47% | 17% | flow angle 89% |
| 30 | generating | 0.0 | 2.18 | 42 | 25.0 | 0.0 | 162.76 | 11.87 | 44 | 13.5 | 49% | 35% | 23% | 24% | 41% | 100% | 57% | 24% | flow angle 90% |
| 35 | generating | 0.0 | 2.54 | 42 | 25.0 | 0.0 | 258.29 | 13.97 | 51 | 25.5 | 67% | 48% | 32% | 33% | 56% | 100% | 66% | 33% | flow angle 90% |
| 40 | generating | 0.0 | 2.91 | 42 | 25.0 | 0.0 | 383.65 | 16.06 | 59 | 44.0 | 88% | 63% | 42% | 43% | 74% | 100% | 75% | 43% | generator speed 93% |
| 45 | feathered (cut-out) | 45.0 | - | - | 0.0 | 0.0 | 0.00 | 0.00 | 0 | 0.0 | 82% | 0% | 39% | 55% | 73% | 0% | 0% | 0% | end plates 93% |

## Power from 1 to 40 m/s

| Wind (m/s) | Wind through prism (W) | Potential face-on (W) | Electrical (W) | Low case (W) | What governs | Pitch (°) | Swing (±°) | Swing f (Hz) |
|---|---|---|---|---|---|---|---|---|
| 1 | 0.2 | 0.00 | 0.00 | 0.00 | idle (below quasi-steady range) | 0.0 | 0.0 | - |
| 2 | 1.6 | 0.00 | 0.00 | 0.00 | idle (friction) | 0.0 | 0.0 | - |
| 3 | 5.5 | 0.00 | 0.00 | 0.00 | idle (friction) | 0.0 | 0.0 | - |
| 4 | 12.9 | 0.00 | 0.00 | 0.00 | idle (friction) | 0.0 | 0.0 | - |
| 4.5 | 18.4 | 0.00 | 0.00 | 0.00 | idle (friction) | 0.0 | 0.0 | - |
| 5 | 25.3 | 0.00 | 0.00 | 0.00 | idle (friction) | 0.0 | 0.0 | - |
| 6 | 43.7 | 0.01 | 0.01 | 0.00 | unconstrained | 0.0 | 25.0 | 0.36 |
| 7 | 69.3 | 0.57 | 0.57 | 0.29 | unconstrained | 0.0 | 25.0 | 0.45 |
| 8 | 103.5 | 1.42 | 1.42 | 0.71 | unconstrained | 0.0 | 25.0 | 0.53 |
| 9 | 147.3 | 2.59 | 2.59 | 1.30 | unconstrained | 0.0 | 25.0 | 0.61 |
| 10 | 202.1 | 4.11 | 4.11 | 2.06 | unconstrained | 0.0 | 25.0 | 0.69 |
| 11 | 269.0 | 6.03 | 6.03 | 3.01 | unconstrained | 0.0 | 25.0 | 0.77 |
| 12 | 349.3 | 8.37 | 8.37 | 4.18 | unconstrained | 0.0 | 25.0 | 0.84 |
| 13 | 444.1 | 11.17 | 11.17 | 5.58 | unconstrained | 0.0 | 25.0 | 0.92 |
| 14 | 554.6 | 14.47 | 14.47 | 7.23 | unconstrained | 0.0 | 25.0 | 0.99 |
| 15 | 682.2 | 18.30 | 18.30 | 9.15 | unconstrained | 0.0 | 25.0 | 1.07 |
| 17.5 | 1,083.3 | 30.44 | 30.44 | 15.22 | unconstrained | 0.0 | 25.0 | 1.26 |
| 20 | 1,617.0 | 46.68 | 46.68 | 23.34 | unconstrained | 0.0 | 25.0 | 1.44 |
| 25 | 3,158.2 | 93.49 | 93.49 | 46.74 | unconstrained | 0.0 | 25.0 | 1.81 |
| 30 | 5,457.4 | 162.76 | 162.76 | 81.38 | unconstrained | 0.0 | 25.0 | 2.18 |
| 35 | 8,666.1 | 258.29 | 258.29 | 129.14 | unconstrained | 0.0 | 25.0 | 2.54 |
| 40 | 12,936.0 | 383.65 | 383.65 | 191.82 | unconstrained | 0.0 | 25.0 | 2.91 |

## Structure at the survival requirement (45 m/s, feathered and braked)

- Drag 675 N; moment at the hinge 878 N m (hub built for 1200)
- Neck stress 326 MPa (allowable 400); skin stress at prism base 15.5 MPa (allowable 40)
- Panel bending 10.9 N m/m against 20; end-plate gust utilisation 93%
- Bushing load 2938 N each; pitch-drive torque about 13.5 N m
- Post base moment with the hinge at 3 m: 3157 N m
- Generating at 40 m/s: drag 679 N, hinge moment 883 N m, post base 3120 N m, spring force 2263 N over ±45 mm, belt tension 475 N (allowable 1100)

## Annual energy (very rough)

Rayleigh wind at hub height, the power curve above, 80 % of the model output achieved (yaw lag, gusts, restarts). Low case = 0.5 x central.

| Site mean wind | Low (kWh/yr) | Central (kWh/yr) |
|---|---|---|
| 3.5 m/s | 0.3 | 0.6 |
| 4.5 m/s | 1.3 | 2.6 |
| 5.5 m/s | 3.5 | 7.1 |
| 6.5 m/s | 7.2 | 14.4 |
| 7.5 m/s | 12.6 | 25.2 |

