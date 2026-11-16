# Lantern calculator report

Tube 250 mm x 1000 mm, neck 800 mm (35x32 mm carbon), end discs 500 mm, shell 0.211 kg/m^2 (sandwich, 3 mm core), survival requirement 25 m/s

Constraint check: all pass

## Operating summary

- Cut-in (starts and produces >10 mW): 1.6 m/s with kick-start
- Tracking: 2-7 m/s; power-capped at 7.38 W up to 8.0 m/s; braked above that
- Survives (parked, braked) up to **25.1 m/s**, limited by the hub. Requirement: 25 m/s. Per part: neck 46, skin 33, wall 35, discs 34, hub 25
- Worst while swinging: neck 16%, neck fatigue 31%, skin 32%, voltage 27%, generator heat 82%, neck mode 66%
- Neck-tube bending mode about 14.5 Hz (swing must stay below 9.6 Hz, reached at 12.0 m/s)

## Masses (kg)

| Part | Mass |
|---|---|
| Tube shell incl. rings and seams | 0.186 |
| End discs, each | 0.041 |
| Bottom spider | 0.015 |
| Neck tube | 0.196 |
| Hub, axle, carriage, belt arc | 0.150 |
| **Total swinging mass** | **0.629** |

## Inertia about the hinge (kg m^2)

| Part | Inertia |
|---|---|
| shell | 0.3293 |
| discs | 0.1620 |
| spider | 0.0096 |
| neck | 0.0418 |
| hub | 0.0007 |
| generator | 0.0411 |
| Structural total | 0.5846 |
| Air moving with the tube | 0.1066 |
| **Total** | **0.6912** |
| Mass ratio (structural / displaced air) | 5.48 |

- Gear ratio: 26.2:1 (100 mm arc to 12-tooth GT2 pulley)
- Mode-shape factor gamma: 1.244
- Effective length after end losses: 1.000 m
- Gravity (destabilising) stiffness: 4.31 N m/rad

## Tuning

Two opposing springs, each 18.15 N/mm.

| Wind (m/s) | Tune f_n (Hz) | Stiffness (N m/rad) | Carriage below hinge (mm) |
|---|---|---|---|
| 2.0 | 1.45 | 62.0 | 41.3 |
| 3.0 | 2.18 | 134.2 | 60.8 |
| 4.0 | 2.91 | 235.3 | 80.5 |
| 4.5 | 3.27 | 296.6 | 90.4 |
| 5.0 | 3.64 | 365.2 | 100.3 |
| 6.0 | 4.36 | 523.9 | 120.1 |
| 7.0 | 5.09 | 711.6 | 140.0 |

Carriage moves about 19.8 mm per 1 m/s between 4 and 6 m/s.

## Operating points while tracking (model central case)

| Wind | Re | Swing f (Hz) | Wind power (W) | Mech (W) | Elec (W) | Elec low case (W) | Mech eff | Swing (deg) | Peak torque (N m) | Gen zeta | Parasitic zeta | Circuit R (ohm) | Copper eff | EMF peak (V) | Gen peak rpm | Top accel (g) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2.0 | 33333 | 1.60 | 1.2 | 0.17 | 0.13 | 0.07 | 13.7 % | 5.3 | 0.36 | 0.033 | 0.0181 | 254 | 95 % | 9.2 | 232 | 1.7 |
| 3.0 | 50000 | 2.40 | 4.1 | 0.73 | 0.56 | 0.28 | 17.6 % | 6.1 | 0.90 | 0.032 | 0.0099 | 177 | 93 % | 16.1 | 404 | 4.5 |
| 4.5 | 75000 | 3.60 | 14.0 | 2.70 | 2.00 | 1.00 | 19.4 % | 6.5 | 2.11 | 0.031 | 0.0069 | 120 | 90 % | 25.5 | 640 | 10.6 |
| 6.0 | 100000 | 4.80 | 33.1 | 6.60 | 4.72 | 2.36 | 20.0 % | 6.6 | 3.80 | 0.031 | 0.0059 | 90 | 87 % | 34.6 | 868 | 19.2 |
| 7.0 | 116667 | 5.60 | 52.5 | 10.59 | 7.38 | 3.69 | 20.2 % | 6.6 | 5.20 | 0.031 | 0.0056 | 78 | 85 % | 40.6 | 1019 | 26.3 |

At 4.5 m/s: tube swings +/-91 mm at the bottom, +/-148 mm mid-height, +/-204 mm at the top; generator swings +/-170 deg. Friction: bushings 0.102 N m, generator drag 0.105 N m (at the hinge).

## Wind envelope, 1-40 m/s

Utilisation = load / allowable for each part (over 100% fails). Neck, skin and hub combine drag with the swing's inertia; wall is ovalling of the shell under wind pressure; discs is gust lift on the end discs. Parked modes use drag coefficient 1.2; swinging modes 2.0.

| Wind (m/s) | Mode | Re | Flow | Tuned to (Hz) | Carriage (mm) | Swing (±°) | Elec (W) | Top accel (g) | EMF (V) | Neck | Neck fatigue | Skin | Wall | Discs | Hub | Worst |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | idle | 16,667 | tested | 5.09 | 140 | 0.0 | 0.00 | 0.0 | 0 | 0% | 0% | 0% | 0% | 0% | 0% | hub 0% |
| 2 | tracking | 33,333 | tested | 1.45 | 41 | 5.3 | 0.13 | 1.7 | 9 | 1% | 2% | 2% | 0% | 0% | 1% | neck mode 17% |
| 2.5 | tracking | 41,667 | tested | 1.82 | 51 | 5.8 | 0.30 | 3.0 | 13 | 2% | 3% | 4% | 0% | 1% | 2% | neck mode 21% |
| 3 | tracking | 50,000 | tested | 2.18 | 61 | 6.1 | 0.56 | 4.5 | 16 | 3% | 5% | 5% | 1% | 1% | 2% | neck mode 25% |
| 4 | tracking | 66,667 | tested | 2.91 | 80 | 6.4 | 1.40 | 8.3 | 22 | 5% | 10% | 10% | 1% | 1% | 4% | neck mode 33% |
| 4.5 | tracking | 75,000 | tested | 3.27 | 90 | 6.5 | 2.00 | 10.6 | 25 | 6% | 12% | 13% | 2% | 2% | 5% | neck mode 37% |
| 5 | tracking | 83,333 | tested | 3.64 | 100 | 6.5 | 2.75 | 13.2 | 29 | 8% | 15% | 16% | 2% | 2% | 7% | neck mode 41% |
| 6 | tracking | 100,000 | tested | 4.36 | 120 | 6.6 | 4.72 | 19.2 | 35 | 12% | 22% | 23% | 3% | 3% | 10% | neck mode 50% |
| 7 | tracking | 116,667 | tested | 5.09 | 140 | 6.6 | 7.38 | 26.3 | 41 | 16% | 31% | 32% | 4% | 4% | 13% | neck mode 58% |
| 7.5 | power-capped | 125,000 | beyond tested | 5.09 | 140 | 5.2 | 7.38 | 23.6 | 34 | 14% | 28% | 29% | 4% | 5% | 15% | neck mode 62% |
| 8 | braked | 133,333 | beyond tested | 5.09 | 140 | 1.0 | 0.00 | 5.2 | 0 | 4% | 6% | 9% | 5% | 6% | 10% | generator heat 41% |
| 9 | braked | 150,000 | beyond tested | 5.09 | 140 | 0.0 | 0.00 | 0.0 | 0 | 4% | 0% | 8% | 6% | 7% | 13% | hub 13% |
| 10 | braked | 166,667 | beyond tested | 5.09 | 140 | 0.0 | 0.00 | 0.0 | 0 | 5% | 0% | 9% | 8% | 9% | 16% | hub 16% |
| 12 | braked | 200,000 | beyond tested | 5.09 | 140 | 0.0 | 0.00 | 0.0 | 0 | 7% | 0% | 13% | 11% | 13% | 23% | hub 23% |
| 15 | braked | 250,000 | drag crisis | 5.09 | 140 | 0.0 | 0.00 | 0.0 | 0 | 11% | 0% | 21% | 18% | 20% | 36% | hub 36% |
| 20 | braked | 333,333 | drag crisis | 5.09 | 140 | 0.0 | 0.00 | 0.0 | 0 | 19% | 0% | 37% | 32% | 35% | 64% | hub 64% |
| 25 | braked | 416,667 | drag crisis | 5.09 | 140 | 0.0 | 0.00 | 0.0 | 0 | 29% | 0% | 58% | 50% | 55% | 100% | hub 100% |
| 30 | braked | 500,000 | drag crisis | 5.09 | 140 | 0.0 | 0.00 | 0.0 | 0 | 42% | 0% | 84% | 72% | 79% | 143% | hub 143% **FAIL** |
| 35 | braked | 583,333 | drag crisis | 5.09 | 140 | 0.0 | 0.00 | 0.0 | 0 | 58% | 0% | 115% | 98% | 107% | 195% | hub 195% **FAIL** |
| 40 | braked | 666,667 | drag crisis | 5.09 | 140 | 0.0 | 0.00 | 0.0 | 0 | 75% | 0% | 150% | 128% | 140% | 255% | hub 255% **FAIL** |

## Power from 1 to 40 m/s

Model potential = output if the tube stayed tuned and locked on with nothing failing (not achievable). Within limits = the most it can deliver with every part within limits, retuning as far as the neck's bending mode allows. As designed = the default control.

- Neck-tube bending mode about 14.5 Hz, so the swing must stay below 9.6 Hz: retuning is possible up to 12.0 m/s
- As designed: generates 1.6-8.0 m/s, peak 7.38 W, braked above
- Kept generating within every limit: generates 1.8-10.8 m/s, peak 23.58 W at 10.5 m/s; nothing above 12.0 m/s
- Yearly energy, central case (kWh): 3.5 m/s site: as designed 6.4, within limits 7.7; 4.5 m/s site: as designed 9.1, within limits 14.7; 5.5 m/s site: as designed 9.9, within limits 20.8; 6.5 m/s site: as designed 9.5, within limits 24.3

| Wind (m/s) | Re | Flow | Wind through tube (W) | Model potential (W) | Within limits (W) | Within limits: what governs | As designed (W) | As designed: mode |
|---|---|---|---|---|---|---|---|---|
| 1 | 16,667 | tested | 0.2 | 0.00 | 0.00 | idle | 0.00 | idle |
| 2 | 33,333 | tested | 1.2 | 0.13 | 0.14 | unconstrained | 0.13 | tracking |
| 3 | 50,000 | tested | 4.1 | 0.56 | 0.57 | unconstrained | 0.56 | tracking |
| 4 | 66,667 | tested | 9.8 | 1.40 | 1.41 | unconstrained | 1.40 | tracking |
| 4.5 | 75,000 | tested | 14.0 | 2.00 | 2.03 | unconstrained | 2.00 | tracking |
| 5 | 83,333 | tested | 19.1 | 2.75 | 2.79 | unconstrained | 2.75 | tracking |
| 6 | 100,000 | tested | 33.1 | 4.72 | 4.79 | unconstrained | 4.72 | tracking |
| 7 | 116,667 | tested | 52.5 | 7.38 | 7.53 | unconstrained | 7.38 | tracking |
| 8 | 133,333 | beyond tested | 78.4 | 10.81 | 11.10 | unconstrained | 0.00 | braked |
| 9 | 150,000 | beyond tested | 111.6 | 15.04 | 15.56 | unconstrained | 0.00 | braked |
| 10 | 166,667 | beyond tested | 153.1 | 20.14 | 20.50 | unconstrained | 0.00 | braked |
| 11 | 183,333 | beyond tested | 203.8 | 26.11 | 0.00 | braked (generator heat) | 0.00 | braked |
| 12 | 200,000 | beyond tested | 264.6 | 32.98 | 0.00 | braked (generator heat) | 0.00 | braked |
| 13 | 216,667 | drag crisis | 336.4 | 40.73 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 14 | 233,333 | drag crisis | 420.2 | 49.36 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 15 | 250,000 | drag crisis | 516.8 | 58.84 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 17.5 | 291,667 | drag crisis | 820.7 | 85.92 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 20 | 333,333 | drag crisis | 1,225.0 | 116.93 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 25 | 416,667 | drag crisis | 2,392.6 | 183.85 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 30 | 500,000 | drag crisis | 4,134.4 | 240.39 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 35 | 583,333 | drag crisis | 6,565.2 | 258.74 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 40 | 666,667 | drag crisis | 9,800.0 | 202.47 | 0.00 | braked (drag crisis) | 0.00 | braked |

## Structure at the survival requirement (25 m/s, parked and braked)

- Drag on the tube 115 N; bending moment at tube base 57 N m, at the hinge 149 N m (hub built for 150)
- Neck stress 118 MPa (allowable 400); skin stress at tube base 23.4 MPa (allowable 40)
- Shell ovalling 2.99 N m/m against a wall capacity of 6.00 N m/m
- End-disc gust utilisation 55%
- Hinge bushing load 998 N each
- Post base moment with hinge at 3 m: 554 N m (size the post to your local wind code)
- Swing cycles per year at 30 % duty: 3.1e+07

## Annual energy (very rough)

Rayleigh wind at hub height, power curve from the envelope above (tracking, then capped at 7.38 W, braked from 8.0 m/s), 50 % of swinging time assumed locked on. Low case = 0.5 x central.

| Site mean wind | Low (kWh/yr) | Central (kWh/yr) |
|---|---|---|
| 3.0 m/s | 2.3 | 4.5 |
| 3.5 m/s | 3.2 | 6.4 |
| 4.5 m/s | 4.5 | 9.1 |
| 5.5 m/s | 4.9 | 9.9 |

