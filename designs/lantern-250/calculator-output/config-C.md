# Lantern calculator report

Tube 250 mm x 1000 mm, neck 600 mm (35x32 mm carbon), end discs 500 mm, shell 0.315 kg/m^2 (sandwich, 5 mm core), survival requirement 40 m/s

Constraint check: all pass

## Operating summary

- Cut-in (starts and produces >10 mW): 1.6 m/s with kick-start
- Tracking: 2-7 m/s; power-capped at 6.97 W up to 8.0 m/s; braked above that
- Survives (parked, braked) up to **41.6 m/s**, limited by the hub. Requirement: 40 m/s. Per part: neck 50, skin 57, wall 46, discs 44, hub 42
- Worst while swinging: neck 18%, neck fatigue 35%, skin 15%, voltage 30%, generator heat 56%

## Masses (kg)

| Part | Mass |
|---|---|
| Tube shell incl. rings and seams | 0.285 |
| End discs, each | 0.056 |
| Bottom spider | 0.015 |
| Neck tube | 0.147 |
| Hub, axle, carriage, belt arc | 0.300 |
| **Total swinging mass** | **0.859** |

## Inertia about the hinge (kg m^2)

| Part | Inertia |
|---|---|
| shell | 0.3691 |
| discs | 0.1652 |
| spider | 0.0054 |
| neck | 0.0176 |
| hub | 0.0015 |
| generator | 0.0411 |
| Structural total | 0.5999 |
| Air moving with the tube | 0.0778 |
| **Total** | **0.6777** |
| Mass ratio (structural / displaced air) | 7.71 |

- Gear ratio: 26.2:1 (100 mm arc to 12-tooth GT2 pulley)
- Mode-shape factor gamma: 1.261
- Effective length after end losses: 1.000 m
- Gravity (destabilising) stiffness: 4.81 N m/rad

## Tuning

Two opposing springs, each 17.81 N/mm.

| Wind (m/s) | Tune f_n (Hz) | Stiffness (N m/rad) | Carriage below hinge (mm) |
|---|---|---|---|
| 2.0 | 1.45 | 61.4 | 41.5 |
| 3.0 | 2.18 | 132.2 | 60.9 |
| 4.0 | 2.91 | 231.2 | 80.6 |
| 4.5 | 3.27 | 291.3 | 90.4 |
| 5.0 | 3.64 | 358.6 | 100.3 |
| 6.0 | 4.36 | 514.2 | 120.1 |
| 7.0 | 5.09 | 698.2 | 140.0 |

Carriage moves about 19.8 mm per 1 m/s between 4 and 6 m/s.

## Operating points while tracking (model central case)

| Wind | Re | Swing f (Hz) | Wind power (W) | Mech (W) | Elec (W) | Elec low case (W) | Mech eff | Swing (deg) | Peak torque (N m) | Gen zeta | Parasitic zeta | Circuit R (ohm) | Copper eff | EMF peak (V) | Gen peak rpm | Top accel (g) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2.0 | 33333 | 1.60 | 1.2 | 0.13 | 0.10 | 0.05 | 10.6 % | 5.4 | 0.28 | 0.024 | 0.0177 | 336 | 96 % | 9.4 | 235 | 1.5 |
| 3.0 | 50000 | 2.40 | 4.1 | 0.63 | 0.49 | 0.25 | 15.2 % | 6.6 | 0.72 | 0.023 | 0.0091 | 239 | 95 % | 17.3 | 436 | 4.3 |
| 4.5 | 75000 | 3.60 | 14.0 | 2.41 | 1.84 | 0.92 | 17.2 % | 7.1 | 1.71 | 0.022 | 0.0063 | 163 | 93 % | 28.0 | 703 | 10.4 |
| 6.0 | 100000 | 4.80 | 33.1 | 5.93 | 4.41 | 2.21 | 17.9 % | 7.3 | 3.09 | 0.022 | 0.0054 | 123 | 90 % | 38.2 | 959 | 18.9 |
| 7.0 | 116667 | 5.60 | 52.5 | 9.54 | 6.97 | 3.49 | 18.2 % | 7.3 | 4.23 | 0.022 | 0.0051 | 106 | 89 % | 44.9 | 1128 | 25.9 |

At 4.5 m/s: tube swings +/-75 mm at the bottom, +/-137 mm mid-height, +/-200 mm at the top; generator swings +/-186 deg. Friction: bushings 0.092 N m, generator drag 0.105 N m (at the hinge).

## Wind envelope, 1-40 m/s

Utilisation = load / allowable for each part (over 100% fails). Neck, skin and hub combine drag with the swing's inertia; wall is ovalling of the shell under wind pressure; discs is gust lift on the end discs. Parked modes use drag coefficient 1.2; swinging modes 2.0.

| Wind (m/s) | Mode | Re | Flow | Tuned to (Hz) | Carriage (mm) | Swing (±°) | Elec (W) | Top accel (g) | EMF (V) | Neck | Neck fatigue | Skin | Wall | Discs | Hub | Worst |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | idle | 16,667 | tested | 5.09 | 140 | 0.0 | 0.00 | 0.0 | 0 | 0% | 0% | 0% | 0% | 0% | 0% | hub 0% |
| 2 | tracking | 33,333 | tested | 1.45 | 42 | 5.4 | 0.10 | 1.5 | 9 | 1% | 2% | 1% | 0% | 0% | 0% | voltage 6% |
| 2.5 | tracking | 41,667 | tested | 1.82 | 51 | 6.2 | 0.26 | 2.8 | 14 | 2% | 4% | 2% | 0% | 0% | 1% | voltage 9% |
| 3 | tracking | 50,000 | tested | 2.18 | 61 | 6.6 | 0.49 | 4.3 | 17 | 3% | 6% | 2% | 0% | 0% | 1% | voltage 12% |
| 4 | tracking | 66,667 | tested | 2.91 | 81 | 7.0 | 1.27 | 8.1 | 25 | 6% | 11% | 5% | 1% | 1% | 2% | voltage 16% |
| 4.5 | tracking | 75,000 | tested | 3.27 | 90 | 7.1 | 1.84 | 10.4 | 28 | 7% | 14% | 6% | 1% | 1% | 2% | voltage 19% |
| 5 | tracking | 83,333 | tested | 3.64 | 100 | 7.2 | 2.54 | 12.9 | 31 | 9% | 17% | 7% | 1% | 1% | 2% | voltage 21% |
| 6 | tracking | 100,000 | tested | 4.36 | 120 | 7.3 | 4.41 | 18.9 | 38 | 13% | 25% | 11% | 2% | 2% | 3% | voltage 25% |
| 7 | tracking | 116,667 | tested | 5.09 | 140 | 7.3 | 6.97 | 25.9 | 45 | 18% | 35% | 15% | 2% | 3% | 5% | neck fatigue 35% |
| 7.5 | power-capped | 125,000 | beyond tested | 5.09 | 140 | 5.5 | 6.97 | 22.4 | 36 | 16% | 30% | 13% | 3% | 3% | 5% | generator heat 40% |
| 8 | braked | 133,333 | beyond tested | 5.09 | 140 | 0.6 | 0.00 | 2.6 | 0 | 3% | 4% | 2% | 3% | 3% | 4% | generator heat 13% |
| 9 | braked | 150,000 | beyond tested | 5.09 | 140 | 0.0 | 0.00 | 0.0 | 0 | 3% | 0% | 3% | 4% | 4% | 5% | hub 5% |
| 10 | braked | 166,667 | beyond tested | 5.09 | 140 | 0.0 | 0.00 | 0.0 | 0 | 4% | 0% | 3% | 5% | 5% | 6% | hub 6% |
| 12 | braked | 200,000 | beyond tested | 5.09 | 140 | 0.0 | 0.00 | 0.0 | 0 | 6% | 0% | 4% | 7% | 8% | 8% | hub 8% |
| 15 | braked | 250,000 | drag crisis | 5.09 | 140 | 0.0 | 0.00 | 0.0 | 0 | 9% | 0% | 7% | 11% | 12% | 13% | hub 13% |
| 20 | braked | 333,333 | drag crisis | 5.09 | 140 | 0.0 | 0.00 | 0.0 | 0 | 16% | 0% | 12% | 19% | 21% | 23% | hub 23% |
| 25 | braked | 416,667 | drag crisis | 5.09 | 140 | 0.0 | 0.00 | 0.0 | 0 | 25% | 0% | 19% | 30% | 33% | 36% | hub 36% |
| 30 | braked | 500,000 | drag crisis | 5.09 | 140 | 0.0 | 0.00 | 0.0 | 0 | 36% | 0% | 28% | 43% | 47% | 52% | hub 52% |
| 35 | braked | 583,333 | drag crisis | 5.09 | 140 | 0.0 | 0.00 | 0.0 | 0 | 49% | 0% | 38% | 59% | 64% | 71% | hub 71% |
| 40 | braked | 666,667 | drag crisis | 5.09 | 140 | 0.0 | 0.00 | 0.0 | 0 | 64% | 0% | 50% | 77% | 84% | 92% | hub 92% |

## Structure at the survival requirement (40 m/s, parked and braked)

- Drag on the tube 294 N; bending moment at tube base 147 N m, at the hinge 323 N m (hub built for 350)
- Neck stress 255 MPa (allowable 400); skin stress at tube base 20.0 MPa (allowable 40)
- Shell ovalling 7.66 N m/m against a wall capacity of 10.00 N m/m
- End-disc gust utilisation 84%
- Hinge bushing load 1621 N each
- Post base moment with hinge at 3 m: 1358 N m (size the post to your local wind code)
- Swing cycles per year at 30 % duty: 3.1e+07

## Annual energy (very rough)

Rayleigh wind at hub height, power curve from the envelope above (tracking, then capped at 6.97 W, braked from 8.0 m/s), 50 % of swinging time assumed locked on. Low case = 0.5 x central.

| Site mean wind | Low (kWh/yr) | Central (kWh/yr) |
|---|---|---|
| 3.0 m/s | 2.1 | 4.2 |
| 3.5 m/s | 3.0 | 5.9 |
| 4.5 m/s | 4.2 | 8.5 |
| 5.5 m/s | 4.6 | 9.2 |

