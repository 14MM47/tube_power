# Lantern calculator report

Tube 250 mm x 1000 mm, neck 400 mm (25x23 mm carbon), end discs 400 mm, shell 0.211 kg/m^2 (sandwich, 3 mm core), survival requirement 25 m/s

Constraint check: all pass

## Operating summary

- Cut-in (starts and produces >10 mW): 1.6 m/s with kick-start
- Tracking: 2-7 m/s; power-capped at 5.86 W up to 8.0 m/s; braked above that
- Survives (parked, braked) up to **30.1 m/s**, limited by the hub. Requirement: 25 m/s. Per part: neck 32, skin 33, wall 35, discs 56, hub 30
- Worst while swinging: neck 26%, neck fatigue 49%, skin 27%, voltage 27%, generator heat 64%

## Masses (kg)

| Part | Mass |
|---|---|
| Tube shell incl. rings and seams | 0.186 |
| End discs, each | 0.027 |
| Bottom spider | 0.015 |
| Neck tube | 0.047 |
| Hub, axle, carriage, belt arc | 0.150 |
| **Total swinging mass** | **0.450** |

## Inertia about the hinge (kg m^2)

| Part | Inertia |
|---|---|
| shell | 0.1659 |
| discs | 0.0567 |
| spider | 0.0024 |
| neck | 0.0025 |
| hub | 0.0007 |
| generator | 0.0231 |
| Structural total | 0.2514 |
| Air moving with the tube | 0.0537 |
| **Total** | **0.3051** |
| Mass ratio (structural / displaced air) | 4.68 |

- Gear ratio: 19.6:1 (100 mm arc to 16-tooth GT2 pulley)
- Mode-shape factor gamma: 1.277
- Effective length after end losses: 0.900 m
- Gravity (destabilising) stiffness: 2.26 N m/rad

## Tuning

Two opposing springs, each 8.02 N/mm.

| Wind (m/s) | Tune f_n (Hz) | Stiffness (N m/rad) | Carriage below hinge (mm) |
|---|---|---|---|
| 2.0 | 1.45 | 27.7 | 41.6 |
| 3.0 | 2.18 | 59.6 | 61.0 |
| 4.0 | 2.91 | 104.2 | 80.6 |
| 4.5 | 3.27 | 131.3 | 90.5 |
| 5.0 | 3.64 | 161.5 | 100.3 |
| 6.0 | 4.36 | 231.6 | 120.2 |
| 7.0 | 5.09 | 314.5 | 140.0 |

Carriage moves about 19.8 mm per 1 m/s between 4 and 6 m/s.

## Operating points while tracking (model central case)

| Wind | Re | Swing f (Hz) | Wind power (W) | Mech (W) | Elec (W) | Elec low case (W) | Mech eff | Swing (deg) | Peak torque (N m) | Gen zeta | Parasitic zeta | Circuit R (ohm) | Copper eff | EMF peak (V) | Gen peak rpm | Top accel (g) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2.0 | 33333 | 1.60 | 1.2 | 0.12 | 0.10 | 0.05 | 10.0 % | 6.7 | 0.23 | 0.039 | 0.0242 | 280 | 96 % | 8.7 | 219 | 1.7 |
| 3.0 | 50000 | 2.40 | 4.1 | 0.56 | 0.43 | 0.22 | 13.5 % | 7.9 | 0.59 | 0.037 | 0.0126 | 197 | 94 % | 15.6 | 392 | 4.5 |
| 4.5 | 75000 | 3.60 | 14.0 | 2.09 | 1.57 | 0.79 | 15.0 % | 8.5 | 1.39 | 0.037 | 0.0085 | 134 | 91 % | 24.9 | 627 | 10.8 |
| 6.0 | 100000 | 4.80 | 33.1 | 5.14 | 3.73 | 1.87 | 15.5 % | 8.6 | 2.51 | 0.036 | 0.0073 | 101 | 88 % | 33.9 | 853 | 19.6 |
| 7.0 | 116667 | 5.60 | 52.5 | 8.26 | 5.86 | 2.93 | 15.7 % | 8.7 | 3.43 | 0.036 | 0.0068 | 87 | 86 % | 39.9 | 1002 | 26.8 |

At 4.5 m/s: tube swings +/-60 mm at the bottom, +/-134 mm mid-height, +/-208 mm at the top; generator swings +/-166 deg. Friction: bushings 0.087 N m, generator drag 0.079 N m (at the hinge).

## Wind envelope, 1-40 m/s

Utilisation = load / allowable for each part (over 100% fails). Neck, skin and hub combine drag with the swing's inertia; wall is ovalling of the shell under wind pressure; discs is gust lift on the end discs. Parked modes use drag coefficient 1.2; swinging modes 2.0.

| Wind (m/s) | Mode | Re | Flow | Tuned to (Hz) | Carriage (mm) | Swing (±°) | Elec (W) | Top accel (g) | EMF (V) | Neck | Neck fatigue | Skin | Wall | Discs | Hub | Worst |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | idle | 16,667 | tested | 5.09 | 140 | 0.0 | 0.00 | 0.0 | 0 | 0% | 0% | 0% | 0% | 0% | 0% | hub 0% |
| 2 | tracking | 33,333 | tested | 1.45 | 42 | 6.7 | 0.10 | 1.7 | 9 | 2% | 3% | 2% | 0% | 0% | 1% | voltage 6% |
| 2.5 | tracking | 41,667 | tested | 1.82 | 51 | 7.5 | 0.23 | 3.0 | 12 | 3% | 5% | 3% | 0% | 0% | 1% | voltage 8% |
| 3 | tracking | 50,000 | tested | 2.18 | 61 | 7.9 | 0.43 | 4.5 | 16 | 4% | 8% | 5% | 1% | 0% | 2% | voltage 10% |
| 4 | tracking | 66,667 | tested | 2.91 | 81 | 8.4 | 1.09 | 8.4 | 22 | 8% | 15% | 9% | 1% | 1% | 3% | neck fatigue 15% |
| 4.5 | tracking | 75,000 | tested | 3.27 | 90 | 8.5 | 1.57 | 10.8 | 25 | 10% | 20% | 11% | 2% | 1% | 4% | neck fatigue 20% |
| 5 | tracking | 83,333 | tested | 3.64 | 100 | 8.5 | 2.17 | 13.4 | 28 | 13% | 25% | 14% | 2% | 1% | 5% | neck fatigue 25% |
| 6 | tracking | 100,000 | tested | 4.36 | 120 | 8.6 | 3.73 | 19.6 | 34 | 19% | 36% | 20% | 3% | 1% | 7% | neck fatigue 36% |
| 7 | tracking | 116,667 | tested | 5.09 | 140 | 8.7 | 5.86 | 26.8 | 40 | 26% | 49% | 27% | 4% | 2% | 9% | neck fatigue 49% |
| 7.5 | power-capped | 125,000 | beyond tested | 5.09 | 140 | 6.7 | 5.86 | 23.7 | 33 | 24% | 44% | 25% | 4% | 2% | 10% | generator heat 46% |
| 8 | braked | 133,333 | beyond tested | 5.09 | 140 | 1.0 | 0.00 | 4.1 | 0 | 7% | 7% | 7% | 5% | 2% | 7% | generator heat 21% |
| 9 | braked | 150,000 | beyond tested | 5.09 | 140 | 0.0 | 0.00 | 0.0 | 0 | 8% | 0% | 8% | 6% | 3% | 9% | hub 9% |
| 10 | braked | 166,667 | beyond tested | 5.09 | 140 | 0.0 | 0.00 | 0.0 | 0 | 10% | 0% | 9% | 8% | 3% | 11% | hub 11% |
| 12 | braked | 200,000 | beyond tested | 5.09 | 140 | 0.0 | 0.00 | 0.0 | 0 | 14% | 0% | 13% | 11% | 5% | 16% | hub 16% |
| 15 | braked | 250,000 | drag crisis | 5.09 | 140 | 0.0 | 0.00 | 0.0 | 0 | 21% | 0% | 21% | 18% | 7% | 25% | hub 25% |
| 20 | braked | 333,333 | drag crisis | 5.09 | 140 | 0.0 | 0.00 | 0.0 | 0 | 38% | 0% | 37% | 32% | 13% | 44% | hub 44% |
| 25 | braked | 416,667 | drag crisis | 5.09 | 140 | 0.0 | 0.00 | 0.0 | 0 | 59% | 0% | 58% | 50% | 20% | 69% | hub 69% |
| 30 | braked | 500,000 | drag crisis | 5.09 | 140 | 0.0 | 0.00 | 0.0 | 0 | 86% | 0% | 84% | 72% | 28% | 99% | hub 99% |
| 35 | braked | 583,333 | drag crisis | 5.09 | 140 | 0.0 | 0.00 | 0.0 | 0 | 116% | 0% | 115% | 98% | 39% | 135% | hub 135% **FAIL** |
| 40 | braked | 666,667 | drag crisis | 5.09 | 140 | 0.0 | 0.00 | 0.0 | 0 | 152% | 0% | 150% | 128% | 51% | 176% | hub 176% **FAIL** |

## Structure at the survival requirement (25 m/s, parked and braked)

- Drag on the tube 115 N; bending moment at tube base 57 N m, at the hinge 103 N m (hub built for 150)
- Neck stress 238 MPa (allowable 400); skin stress at tube base 23.4 MPa (allowable 40)
- Shell ovalling 2.99 N m/m against a wall capacity of 6.00 N m/m
- End-disc gust utilisation 20%
- Hinge bushing load 1036 N each
- Post base moment with hinge at 3 m: 508 N m (size the post to your local wind code)
- Swing cycles per year at 30 % duty: 3.1e+07

## Annual energy (very rough)

Rayleigh wind at hub height, power curve from the envelope above (tracking, then capped at 5.86 W, braked from 8.0 m/s), 50 % of swinging time assumed locked on. Low case = 0.5 x central.

| Site mean wind | Low (kWh/yr) | Central (kWh/yr) |
|---|---|---|
| 3.0 m/s | 1.8 | 3.6 |
| 3.5 m/s | 2.5 | 5.1 |
| 4.5 m/s | 3.6 | 7.2 |
| 5.5 m/s | 3.9 | 7.8 |

