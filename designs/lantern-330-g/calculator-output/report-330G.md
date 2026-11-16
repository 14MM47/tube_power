# Lantern G calculator report

square prism 330 mm x 1000 mm, neck 600 mm (50x47 mm carbon), end plates 660 mm square, panels 0.460 kg/m^2 (capacity 20 N m/m), generator 8108, 12-tooth pulley (26.2:1), springs to 4 Hz, rated 20 W, survival requirement 45 m/s

Constraint check: all pass

## Operating summary

- Cut-in (starts with kick-start and makes >10 mW): 2.5 m/s; generates without a gap to **40.0 m/s**; feathers above 40 m/s
- Rated 20 W electrical, reached at 15.50 m/s; pitch holds it above that
- Survives feathered (45°) and braked up to **46.7 m/s**, limited by the end plates. Requirement 45 m/s. Per part: neck 54, skin 72, panels 61, end plates 47, hub 47
- Swing frequency range 0.12-4.00 Hz (spring carriage 15-140 mm); neck-and-prism bending mode 16.7 Hz
- Quasi-steady theory trusted from U/(fD) = 20; vortex-shedding resonance would be at U/(fD) = 7.7
- Yearly energy, central case (kWh): 3.5 m/s site 2.7; 4.5 m/s site 6.2; 5.5 m/s site 11.6; 6.5 m/s site 19.0

## Masses (kg)

| Part | Mass |
|---|---|
| Prism panels, 3 bulkheads, corner tapes | 0.712 |
| End plates, each (660 mm square) | 0.200 |
| Bottom spider | 0.020 |
| Neck tube | 0.213 |
| Hub, axle, carriage, belt arc, pitch drive | 0.870 |
| **Total swinging mass** | **2.216** |

## Inertia about the hinge (kg m^2)

| Part | Inertia |
|---|---|
| shell | 0.9213 |
| plates | 0.5996 |
| spider | 0.0072 |
| neck | 0.0255 |
| hub | 0.0043 |
| generator | 0.1713 |
| Air moving with the prism | 0.1613 |
| **Total** | **1.8905** |
| Mass ratio (structural / displaced air) | 10.02 |

- Gear ratio 26.2:1 (100 mm arc to 12-tooth GT2 pulley); generator damping at the hinge up to 34.3 N m s/rad (terminals shorted)
- Span factor after end losses 1.000; frictionless capture ceiling A1² I2² / (6 A3 I4 L) = 3.94 % of the wind through the prism
- Gravity (destabilising) stiffness 12.8 N m/rad; two springs of 30.79 N/mm each
- Panel bending per unit dynamic pressure 8.80 x 10^-3 m^2 (bulkheads every 0.250 m)

## Wind envelope

Utilisation = load / allowable (over 100% fails). The controller keeps every one at or under 100% while generating; above cut-out the prism is feathered (45°) and braked. Stroke = swing plus steady lean against the design stroke; quasi-steady = how close the swing frequency is to the highest the galloping model is trusted at.

| Wind (m/s) | Mode | Pitch (°) | Swing f (Hz) | U/(fD) | Swing (±°) | Lean (°) | Elec (W) | Gen load (N m s/rad) | EMF (V) | Gen heat (W) | Neck | Fatigue | Skin | Panels | Hub | Stroke | Springs | Worst |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | idle (friction) | 0.0 | - | - | 0.0 | 0.0 | 0.00 | 0.00 | 0 | 0.0 | 0% | 0% | 0% | 0% | 0% | 0% | 0% | end plates 0% |
| 2 | idle (friction) | 0.0 | - | - | 0.0 | 0.0 | 0.00 | 0.00 | 0 | 0.0 | 0% | 0% | 0% | 0% | 0% | 0% | 0% | end plates 0% |
| 3 | generating | 0.0 | 0.37 | 24 | 15.0 | 0.0 | 0.06 | 0.41 | 3 | 0.0 | 0% | 0% | 0% | 0% | 1% | 100% | 10% | quasi-steady 82% |
| 4 | generating | 0.0 | 0.52 | 23 | 15.0 | 0.0 | 0.25 | 0.84 | 5 | 0.0 | 1% | 1% | 0% | 0% | 1% | 100% | 12% | quasi-steady 87% |
| 4.5 | generating | 0.0 | 0.60 | 23 | 15.0 | 0.0 | 0.40 | 1.03 | 5 | 0.0 | 1% | 1% | 1% | 1% | 1% | 100% | 14% | quasi-steady 88% |
| 5 | generating | 0.0 | 0.67 | 23 | 15.0 | 0.0 | 0.58 | 1.21 | 6 | 0.0 | 1% | 1% | 1% | 1% | 1% | 100% | 15% | quasi-steady 88% |
| 6 | generating | 0.0 | 0.81 | 22 | 15.0 | 0.0 | 1.09 | 1.56 | 7 | 0.1 | 2% | 2% | 1% | 1% | 2% | 100% | 17% | quasi-steady 89% |
| 7 | generating | 0.0 | 0.95 | 22 | 15.0 | 0.0 | 1.80 | 1.89 | 8 | 0.1 | 3% | 3% | 1% | 1% | 3% | 100% | 19% | quasi-steady 90% |
| 8 | generating | 0.0 | 1.09 | 22 | 15.0 | 0.0 | 2.75 | 2.21 | 9 | 0.2 | 3% | 4% | 2% | 2% | 4% | 100% | 22% | quasi-steady 90% |
| 10 | generating | 0.0 | 1.37 | 22 | 15.0 | 0.0 | 5.45 | 2.84 | 12 | 0.6 | 5% | 6% | 3% | 3% | 6% | 100% | 27% | quasi-steady 90% |
| 12 | generating | 0.0 | 1.65 | 22 | 15.0 | 0.0 | 9.42 | 3.46 | 14 | 1.2 | 8% | 8% | 4% | 4% | 8% | 100% | 32% | quasi-steady 91% |
| 15 | generating | 0.0 | 2.06 | 22 | 15.0 | 0.0 | 18.12 | 4.37 | 18 | 3.1 | 12% | 13% | 7% | 6% | 13% | 100% | 39% | quasi-steady 91% |
| 17.5 | limited (power rating) | 4.6 | 2.33 | 23 | 13.3 | 1.7 | 20.00 | 4.86 | 18 | 3.9 | 15% | 15% | 8% | 8% | 16% | 100% | 44% | quasi-steady 88% |
| 20 | limited (power rating) | 6.6 | 2.60 | 23 | 12.6 | 2.4 | 20.00 | 4.32 | 19 | 3.4 | 18% | 17% | 10% | 11% | 20% | 100% | 49% | quasi-steady 86% |
| 25 | limited (power rating) | 8.3 | 2.86 | 26 | 11.4 | 3.6 | 20.00 | 4.36 | 19 | 3.4 | 25% | 19% | 14% | 17% | 29% | 100% | 54% | quasi-steady 76% |
| 30 | limited (power rating) | 9.2 | 3.12 | 29 | 10.4 | 4.6 | 20.00 | 4.42 | 19 | 3.5 | 34% | 20% | 19% | 24% | 41% | 100% | 59% | quasi-steady 69% |
| 35 | limited (power rating) | 9.7 | 3.43 | 31 | 9.6 | 5.4 | 20.00 | 4.20 | 19 | 3.3 | 45% | 23% | 26% | 33% | 55% | 100% | 65% | quasi-steady 65% |
| 40 | limited (power rating) | 10.0 | 3.66 | 33 | 8.8 | 6.2 | 20.00 | 4.54 | 18 | 3.6 | 57% | 24% | 32% | 43% | 71% | 100% | 69% | end plates 73% |
| 45 | feathered (cut-out) | 45.0 | - | - | 0.0 | 0.0 | 0.00 | 0.00 | 0 | 0.0 | 69% | 0% | 39% | 55% | 93% | 0% | 0% | end plates 93% |

## Power from 1 to 40 m/s

| Wind (m/s) | Wind through prism (W) | Potential face-on (W) | Electrical (W) | Low case (W) | What governs | Pitch (°) | Swing (±°) | Swing f (Hz) |
|---|---|---|---|---|---|---|---|---|
| 1 | 0.2 | 0.00 | 0.00 | 0.00 | idle (friction) | 0.0 | 0.0 | - |
| 2 | 1.6 | 0.00 | 0.00 | 0.00 | idle (friction) | 0.0 | 0.0 | - |
| 3 | 5.5 | 0.06 | 0.06 | 0.03 | unconstrained | 0.0 | 15.0 | 0.37 |
| 4 | 12.9 | 0.25 | 0.25 | 0.13 | unconstrained | 0.0 | 15.0 | 0.52 |
| 4.5 | 18.4 | 0.40 | 0.40 | 0.20 | unconstrained | 0.0 | 15.0 | 0.60 |
| 5 | 25.3 | 0.58 | 0.58 | 0.29 | unconstrained | 0.0 | 15.0 | 0.67 |
| 6 | 43.7 | 1.09 | 1.09 | 0.55 | unconstrained | 0.0 | 15.0 | 0.81 |
| 7 | 69.3 | 1.80 | 1.80 | 0.90 | unconstrained | 0.0 | 15.0 | 0.95 |
| 8 | 103.5 | 2.75 | 2.75 | 1.37 | unconstrained | 0.0 | 15.0 | 1.09 |
| 9 | 147.3 | 3.96 | 3.96 | 1.98 | unconstrained | 0.0 | 15.0 | 1.23 |
| 10 | 202.1 | 5.45 | 5.45 | 2.73 | unconstrained | 0.0 | 15.0 | 1.37 |
| 11 | 269.0 | 7.27 | 7.27 | 3.63 | unconstrained | 0.0 | 15.0 | 1.51 |
| 12 | 349.3 | 9.42 | 9.42 | 4.71 | unconstrained | 0.0 | 15.0 | 1.65 |
| 13 | 444.1 | 11.93 | 11.93 | 5.96 | unconstrained | 0.0 | 15.0 | 1.79 |
| 14 | 554.6 | 14.82 | 14.82 | 7.41 | unconstrained | 0.0 | 15.0 | 1.93 |
| 15 | 682.2 | 18.12 | 18.12 | 9.06 | unconstrained | 0.0 | 15.0 | 2.06 |
| 17.5 | 1,083.3 | 28.25 | 20.00 | 10.00 | limited by power rating | 4.6 | 13.3 | 2.33 |
| 20 | 1,617.0 | 41.26 | 20.00 | 10.00 | limited by power rating | 6.6 | 12.6 | 2.60 |
| 25 | 3,158.2 | 76.75 | 20.00 | 10.00 | limited by power rating | 8.3 | 11.4 | 2.86 |
| 30 | 5,457.4 | 126.16 | 20.00 | 10.00 | limited by power rating | 9.2 | 10.4 | 3.12 |
| 35 | 8,666.1 | 189.69 | 20.00 | 10.00 | limited by power rating | 9.7 | 9.6 | 3.43 |
| 40 | 12,936.0 | 266.60 | 20.00 | 10.00 | limited by power rating | 10.0 | 8.8 | 3.66 |

## Structure at the survival requirement (45 m/s, feathered and braked)

- Drag 675 N; moment at the hinge 743 N m (hub built for 800)
- Neck stress 276 MPa (allowable 400); skin stress at prism base 15.5 MPa (allowable 40)
- Panel bending 10.9 N m/m against 20; end-plate gust utilisation 93%
- Bushing load 2487 N each; pitch-drive torque about 13.5 N m
- Post base moment with the hinge at 3 m: 3022 N m
- Generating at 40 m/s: drag 517 N, hinge moment 569 N m, post base 2320 N m, spring force 1033 N

## Annual energy (very rough)

Rayleigh wind at hub height, the power curve above, 80 % of the model output achieved (yaw lag, gusts, restarts). Low case = 0.5 x central.

| Site mean wind | Low (kWh/yr) | Central (kWh/yr) |
|---|---|---|
| 3.5 m/s | 1.3 | 2.7 |
| 4.5 m/s | 3.1 | 6.2 |
| 5.5 m/s | 5.8 | 11.6 |
| 6.5 m/s | 9.5 | 19.0 |
| 7.5 m/s | 13.9 | 27.8 |

