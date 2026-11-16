# Lantern calculator report

Tube 250 mm x 1000 mm, neck 800 mm (30x28 mm carbon), end discs 500 mm, shell 0.211 kg/m^2 (sandwich, 3 mm core), survival requirement 25 m/s

Constraint check: all pass

## Operating summary

- Cut-in (starts and produces >10 mW): 1.6 m/s with kick-start
- Tracking: 2-7 m/s; power-capped at 7.41 W up to 8.0 m/s; braked above that
- Survives (parked, braked) up to **25.1 m/s**, limited by the hub. Requirement: 25 m/s. Per part: neck 33, skin 33, wall 35, discs 34, hub 25
- Worst while swinging: neck 30%, neck fatigue 59%, skin 32%, voltage 27%, generator heat 83%

## Masses (kg)

| Part | Mass |
|---|---|
| Tube shell incl. rings and seams | 0.186 |
| End discs, each | 0.041 |
| Bottom spider | 0.015 |
| Neck tube | 0.113 |
| Hub, axle, carriage, belt arc | 0.150 |
| **Total swinging mass** | **0.547** |

## Inertia about the hinge (kg m^2)

| Part | Inertia |
|---|---|
| shell | 0.3293 |
| discs | 0.1620 |
| spider | 0.0096 |
| neck | 0.0241 |
| hub | 0.0007 |
| generator | 0.0411 |
| Structural total | 0.5669 |
| Air moving with the tube | 0.1066 |
| **Total** | **0.6736** |
| Mass ratio (structural / displaced air) | 5.32 |

- Gear ratio: 26.2:1 (100 mm arc to 12-tooth GT2 pulley)
- Mode-shape factor gamma: 1.244
- Effective length after end losses: 1.000 m
- Gravity (destabilising) stiffness: 3.99 N m/rad

## Tuning

Two opposing springs, each 17.68 N/mm.

| Wind (m/s) | Tune f_n (Hz) | Stiffness (N m/rad) | Carriage below hinge (mm) |
|---|---|---|---|
| 2.0 | 1.45 | 60.2 | 41.3 |
| 3.0 | 2.18 | 130.6 | 60.8 |
| 4.0 | 2.91 | 229.0 | 80.5 |
| 4.5 | 3.27 | 288.8 | 90.4 |
| 5.0 | 3.64 | 355.6 | 100.3 |
| 6.0 | 4.36 | 510.3 | 120.1 |
| 7.0 | 5.09 | 693.2 | 140.0 |

Carriage moves about 19.8 mm per 1 m/s between 4 and 6 m/s.

## Operating points while tracking (model central case)

| Wind | Re | Swing f (Hz) | Wind power (W) | Mech (W) | Elec (W) | Elec low case (W) | Mech eff | Swing (deg) | Peak torque (N m) | Gen zeta | Parasitic zeta | Circuit R (ohm) | Copper eff | EMF peak (V) | Gen peak rpm | Top accel (g) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2.0 | 33333 | 1.60 | 1.2 | 0.17 | 0.13 | 0.07 | 13.8 % | 5.3 | 0.36 | 0.034 | 0.0184 | 254 | 95 % | 9.3 | 233 | 1.7 |
| 3.0 | 50000 | 2.40 | 4.1 | 0.73 | 0.56 | 0.28 | 17.7 % | 6.2 | 0.90 | 0.033 | 0.0100 | 177 | 93 % | 16.1 | 405 | 4.5 |
| 4.5 | 75000 | 3.60 | 14.0 | 2.71 | 2.01 | 1.01 | 19.4 % | 6.5 | 2.11 | 0.032 | 0.0070 | 120 | 90 % | 25.5 | 641 | 10.6 |
| 6.0 | 100000 | 4.80 | 33.1 | 6.62 | 4.74 | 2.37 | 20.0 % | 6.6 | 3.81 | 0.032 | 0.0060 | 90 | 87 % | 34.6 | 870 | 19.3 |
| 7.0 | 116667 | 5.60 | 52.5 | 10.63 | 7.41 | 3.70 | 20.2 % | 6.7 | 5.20 | 0.032 | 0.0057 | 78 | 85 % | 40.6 | 1021 | 26.4 |

At 4.5 m/s: tube swings +/-91 mm at the bottom, +/-148 mm mid-height, +/-205 mm at the top; generator swings +/-170 deg. Friction: bushings 0.102 N m, generator drag 0.105 N m (at the hinge).

## Wind envelope, 1-40 m/s

Utilisation = load / allowable for each part (over 100% fails). Neck, skin and hub combine drag with the swing's inertia; wall is ovalling of the shell under wind pressure; discs is gust lift on the end discs. Parked modes use drag coefficient 1.2; swinging modes 2.0.

| Wind (m/s) | Mode | Re | Flow | Tuned to (Hz) | Carriage (mm) | Swing (±°) | Elec (W) | Top accel (g) | EMF (V) | Neck | Neck fatigue | Skin | Wall | Discs | Hub | Worst |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | idle | 16,667 | tested | 5.09 | 140 | 0.0 | 0.00 | 0.0 | 0 | 0% | 0% | 0% | 0% | 0% | 0% | hub 0% |
| 2 | tracking | 33,333 | tested | 1.45 | 41 | 5.3 | 0.13 | 1.7 | 9 | 2% | 4% | 2% | 0% | 0% | 1% | voltage 6% |
| 2.5 | tracking | 41,667 | tested | 1.82 | 51 | 5.9 | 0.30 | 3.0 | 13 | 3% | 7% | 4% | 0% | 1% | 2% | voltage 9% |
| 3 | tracking | 50,000 | tested | 2.18 | 61 | 6.2 | 0.56 | 4.5 | 16 | 5% | 10% | 5% | 1% | 1% | 2% | voltage 11% |
| 4 | tracking | 66,667 | tested | 2.91 | 80 | 6.4 | 1.40 | 8.3 | 22 | 10% | 19% | 10% | 1% | 1% | 4% | neck fatigue 19% |
| 4.5 | tracking | 75,000 | tested | 3.27 | 90 | 6.5 | 2.01 | 10.6 | 26 | 12% | 24% | 13% | 2% | 2% | 5% | neck fatigue 24% |
| 5 | tracking | 83,333 | tested | 3.64 | 100 | 6.5 | 2.76 | 13.2 | 29 | 15% | 30% | 16% | 2% | 2% | 7% | neck fatigue 30% |
| 6 | tracking | 100,000 | tested | 4.36 | 120 | 6.6 | 4.74 | 19.3 | 35 | 22% | 43% | 23% | 3% | 3% | 10% | neck fatigue 43% |
| 7 | tracking | 116,667 | tested | 5.09 | 140 | 6.7 | 7.41 | 26.4 | 41 | 30% | 59% | 32% | 4% | 4% | 13% | neck fatigue 59% |
| 7.5 | power-capped | 125,000 | beyond tested | 5.09 | 140 | 5.2 | 7.41 | 23.7 | 34 | 28% | 53% | 29% | 4% | 5% | 15% | generator heat 59% |
| 8 | braked | 133,333 | beyond tested | 5.09 | 140 | 1.0 | 0.00 | 5.2 | 0 | 8% | 12% | 9% | 5% | 6% | 10% | generator heat 41% |
| 9 | braked | 150,000 | beyond tested | 5.09 | 140 | 0.0 | 0.00 | 0.0 | 0 | 8% | 0% | 8% | 6% | 7% | 13% | hub 13% |
| 10 | braked | 166,667 | beyond tested | 5.09 | 140 | 0.0 | 0.00 | 0.0 | 0 | 9% | 0% | 9% | 8% | 9% | 16% | hub 16% |
| 12 | braked | 200,000 | beyond tested | 5.09 | 140 | 0.0 | 0.00 | 0.0 | 0 | 13% | 0% | 13% | 11% | 13% | 23% | hub 23% |
| 15 | braked | 250,000 | drag crisis | 5.09 | 140 | 0.0 | 0.00 | 0.0 | 0 | 21% | 0% | 21% | 18% | 20% | 36% | hub 36% |
| 20 | braked | 333,333 | drag crisis | 5.09 | 140 | 0.0 | 0.00 | 0.0 | 0 | 37% | 0% | 37% | 32% | 35% | 64% | hub 64% |
| 25 | braked | 416,667 | drag crisis | 5.09 | 140 | 0.0 | 0.00 | 0.0 | 0 | 58% | 0% | 58% | 50% | 55% | 100% | hub 100% |
| 30 | braked | 500,000 | drag crisis | 5.09 | 140 | 0.0 | 0.00 | 0.0 | 0 | 84% | 0% | 84% | 72% | 79% | 143% | hub 143% **FAIL** |
| 35 | braked | 583,333 | drag crisis | 5.09 | 140 | 0.0 | 0.00 | 0.0 | 0 | 114% | 0% | 115% | 98% | 107% | 195% | hub 195% **FAIL** |
| 40 | braked | 666,667 | drag crisis | 5.09 | 140 | 0.0 | 0.00 | 0.0 | 0 | 149% | 0% | 150% | 128% | 140% | 255% | hub 255% **FAIL** |

## Structure at the survival requirement (25 m/s, parked and braked)

- Drag on the tube 115 N; bending moment at tube base 57 N m, at the hinge 149 N m (hub built for 150)
- Neck stress 234 MPa (allowable 400); skin stress at tube base 23.4 MPa (allowable 40)
- Shell ovalling 2.99 N m/m against a wall capacity of 6.00 N m/m
- End-disc gust utilisation 55%
- Hinge bushing load 998 N each
- Post base moment with hinge at 3 m: 554 N m (size the post to your local wind code)
- Swing cycles per year at 30 % duty: 3.1e+07

## Annual energy (very rough)

Rayleigh wind at hub height, power curve from the envelope above (tracking, then capped at 7.41 W, braked from 8.0 m/s), 50 % of swinging time assumed locked on. Low case = 0.5 x central.

| Site mean wind | Low (kWh/yr) | Central (kWh/yr) |
|---|---|---|
| 3.0 m/s | 2.3 | 4.6 |
| 3.5 m/s | 3.2 | 6.5 |
| 4.5 m/s | 4.6 | 9.1 |
| 5.5 m/s | 5.0 | 9.9 |

