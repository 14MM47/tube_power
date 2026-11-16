# Lantern sweep: ranked by central-case annual energy at a 4.5 m/s site, survival requirement 25 m/s

22440 combinations: D 0.2-0.3 m, neck 0.0-0.8 m, disc ratio 1.4-2.4, shells xps2-single, xps3-single, xps3-sandwich, xps5-sandwich, xps5-storm, pulley teeth [10, 12, 16, 20], neck tube sized automatically.  
6441 pass all limits. Rejected (a design can fail several): Reynolds 10200, operating loads 4159, survival 10504

| Rank | Score (kWh/yr) | D (mm) | Neck (mm) | Neck tube | Disc ratio | Shell | Teeth | Gear | Mass ratio | Mech eff 4.5 | Swing 4.5 (deg) | Cut-in | Survives to | Re at U_max |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 9.37 | 250 | 800 | 35x32 | 2.0 | xps3-sandwich | 10 | 31.4 | 5.65 | 19.0 % | 6.4 | 1.6 | 25.1 (hub) | 116667 |
| 2 | 9.33 | 250 | 750 | 30x28 | 2.0 | xps3-sandwich | 10 | 31.4 | 5.51 | 18.8 % | 6.6 | 1.6 | 25.6 (hub) | 116667 |
| 3 | 9.32 | 250 | 800 | 35x32 | 2.2 | xps3-sandwich | 10 | 31.4 | 5.97 | 18.9 % | 6.4 | 1.6 | 25.1 (hub) | 116667 |
| 4 | 9.27 | 250 | 750 | 30x28 | 2.2 | xps3-sandwich | 10 | 31.4 | 5.84 | 18.7 % | 6.6 | 1.6 | 25.6 (hub) | 116667 |
| 5 | 9.23 | 250 | 700 | 30x28 | 2.0 | xps3-sandwich | 10 | 31.4 | 5.54 | 18.5 % | 6.8 | 1.6 | 26.1 (hub) | 116667 |
| 6 | 9.18 | 250 | 700 | 30x28 | 2.2 | xps3-sandwich | 10 | 31.4 | 5.87 | 18.3 % | 6.8 | 1.6 | 26.1 (hub) | 116667 |
| 7 | 9.12 | 250 | 650 | 30x28 | 2.0 | xps3-sandwich | 10 | 31.4 | 5.58 | 18.1 % | 7.0 | 1.7 | 26.6 (hub) | 116667 |
| 8 | 9.11 | 250 | 800 | 35x32 | 2.0 | xps5-sandwich | 10 | 31.4 | 7.15 | 18.5 % | 6.3 | 1.6 | 25.1 (hub) | 116667 |
| 9 | 9.09 | 250 | 800 | 35x32 | 2.0 | xps3-sandwich | 12 | 26.2 | 5.48 | 19.4 % | 6.5 | 1.6 | 25.1 (hub) | 116667 |
| 10 | 9.09 | 250 | 750 | 30x28 | 2.0 | xps3-sandwich | 12 | 26.2 | 5.33 | 19.1 % | 6.7 | 1.6 | 25.6 (hub) | 116667 |

## Sensitivity around the best design (one variable at a time)

| Variable | Value | Score | vs best |
|---|---|---|---|
| D (mm) | 200 | 7.34 | -22 % |
| D (mm) | 210 | 7.76 | -17 % |
| D (mm) | 220 | 8.17 | -13 % |
| D (mm) | 230 | 8.58 | -9 % |
| D (mm) | 240 | 8.98 | -4 % |
| D (mm) | 250 | 9.37 | +0 % |
| D (mm) | 260 | 9.80 | +5 % (fails Reynolds, survival) |
| D (mm) | 270 | 10.19 | +9 % (fails Reynolds, survival) |
| D (mm) | 280 | 10.57 | +13 % (fails Reynolds, survival) |
| D (mm) | 290 | 10.94 | +17 % (fails Reynolds, survival) |
| D (mm) | 300 | 11.32 | +21 % (fails Reynolds, survival) |
| Neck (mm) | 0 | 5.43 | -42 % |
| Neck (mm) | 100 | 6.27 | -33 % |
| Neck (mm) | 200 | 7.05 | -25 % |
| Neck (mm) | 300 | 7.69 | -18 % |
| Neck (mm) | 400 | 8.23 | -12 % |
| Neck (mm) | 500 | 8.66 | -8 % |
| Neck (mm) | 600 | 8.99 | -4 % |
| Neck (mm) | 700 | 9.23 | -2 % |
| Neck (mm) | 800 | 9.37 | +0 % |
| Disc ratio | 1.4 | 8.12 | -13 % |
| Disc ratio | 1.6 | 8.56 | -9 % |
| Disc ratio | 1.8 | 8.99 | -4 % |
| Disc ratio | 2 | 9.37 | +0 % |
| Disc ratio | 2.2 | 9.32 | -1 % |
| Disc ratio | 2.4 | 9.25 | -1 % (fails survival) |
| Pulley teeth | 10 | 9.37 | +0 % |
| Pulley teeth | 12 | 9.09 | -3 % |
| Pulley teeth | 16 | 8.19 | -13 % (fails operating loads) |
| Pulley teeth | 20 | 6.90 | -26 % (fails operating loads) |
| Shell | xps2-single | 9.73 | +4 % (fails survival) |
| Shell | xps3-single | 9.59 | +2 % (fails survival) |
| Shell | xps3-sandwich | 9.37 | +0 % |
| Shell | xps5-sandwich | 9.11 | -3 % |
| Shell | xps5-storm | 9.04 | -4 % |

Best: shell xps3-sandwich. Full report for it follows.

# Lantern calculator report

Tube 250 mm x 1000 mm, neck 800 mm (35x32 mm carbon), end discs 500 mm, shell 0.211 kg/m^2 (sandwich, 3 mm core), survival requirement 25 m/s

Constraint check: all pass

## Operating summary

- Cut-in (starts and produces >10 mW): 1.6 m/s with kick-start
- Tracking: 2-7 m/s; power-capped at 7.73 W up to 8.0 m/s; braked above that
- Survives (parked, braked) up to **25.1 m/s**, limited by the hub. Requirement: 25 m/s. Per part: neck 46, skin 33, wall 35, discs 34, hub 25
- Worst while swinging: neck 16%, neck fatigue 31%, skin 32%, voltage 32%, generator heat 58%, neck mode 66%
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
| generator | 0.0592 |
| Structural total | 0.6027 |
| Air moving with the tube | 0.1066 |
| **Total** | **0.7093** |
| Mass ratio (structural / displaced air) | 5.65 |

- Gear ratio: 31.4:1 (100 mm arc to 10-tooth GT2 pulley)
- Mode-shape factor gamma: 1.244
- Effective length after end losses: 1.000 m
- Gravity (destabilising) stiffness: 4.31 N m/rad

## Tuning

Two opposing springs, each 18.62 N/mm.

| Wind (m/s) | Tune f_n (Hz) | Stiffness (N m/rad) | Carriage below hinge (mm) |
|---|---|---|---|
| 2.0 | 1.45 | 63.6 | 41.3 |
| 3.0 | 2.18 | 137.6 | 60.8 |
| 4.0 | 2.91 | 241.3 | 80.5 |
| 4.5 | 3.27 | 304.2 | 90.4 |
| 5.0 | 3.64 | 374.6 | 100.3 |
| 6.0 | 4.36 | 537.5 | 120.1 |
| 7.0 | 5.09 | 730.1 | 140.0 |

Carriage moves about 19.8 mm per 1 m/s between 4 and 6 m/s.

## Operating points while tracking (model central case)

| Wind | Re | Swing f (Hz) | Wind power (W) | Mech (W) | Elec (W) | Elec low case (W) | Mech eff | Swing (deg) | Peak torque (N m) | Gen zeta | Parasitic zeta | Circuit R (ohm) | Copper eff | EMF peak (V) | Gen peak rpm | Top accel (g) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2.0 | 33333 | 1.60 | 1.2 | 0.15 | 0.12 | 0.06 | 12.3 % | 5.0 | 0.35 | 0.033 | 0.0212 | 358 | 97 % | 10.4 | 261 | 1.6 |
| 3.0 | 50000 | 2.40 | 4.1 | 0.70 | 0.55 | 0.28 | 17.0 % | 6.0 | 0.89 | 0.031 | 0.0107 | 253 | 95 % | 18.9 | 474 | 4.4 |
| 4.5 | 75000 | 3.60 | 14.0 | 2.66 | 2.04 | 1.02 | 19.0 % | 6.4 | 2.10 | 0.030 | 0.0072 | 172 | 93 % | 30.2 | 760 | 10.5 |
| 6.0 | 100000 | 4.80 | 33.1 | 6.53 | 4.89 | 2.44 | 19.8 % | 6.6 | 3.79 | 0.030 | 0.0061 | 130 | 91 % | 41.2 | 1036 | 19.1 |
| 7.0 | 116667 | 5.60 | 52.5 | 10.50 | 7.73 | 3.86 | 20.0 % | 6.6 | 5.18 | 0.030 | 0.0057 | 112 | 89 % | 48.4 | 1217 | 26.2 |

At 4.5 m/s: tube swings +/-90 mm at the bottom, +/-146 mm mid-height, +/-202 mm at the top; generator swings +/-202 deg. Friction: bushings 0.102 N m, generator drag 0.126 N m (at the hinge).

## Wind envelope, 1-40 m/s

Utilisation = load / allowable for each part (over 100% fails). Neck, skin and hub combine drag with the swing's inertia; wall is ovalling of the shell under wind pressure; discs is gust lift on the end discs. Parked modes use drag coefficient 1.2; swinging modes 2.0.

| Wind (m/s) | Mode | Re | Flow | Tuned to (Hz) | Carriage (mm) | Swing (±°) | Elec (W) | Top accel (g) | EMF (V) | Neck | Neck fatigue | Skin | Wall | Discs | Hub | Worst |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | idle | 16,667 | tested | 5.09 | 140 | 0.0 | 0.00 | 0.0 | 0 | 0% | 0% | 0% | 0% | 0% | 0% | hub 0% |
| 2 | tracking | 33,333 | tested | 1.45 | 41 | 5.0 | 0.12 | 1.6 | 10 | 1% | 2% | 2% | 0% | 0% | 1% | neck mode 17% |
| 2.5 | tracking | 41,667 | tested | 1.82 | 51 | 5.7 | 0.29 | 2.9 | 15 | 2% | 3% | 3% | 0% | 1% | 2% | neck mode 21% |
| 3 | tracking | 50,000 | tested | 2.18 | 61 | 6.0 | 0.55 | 4.4 | 19 | 3% | 5% | 5% | 1% | 1% | 2% | neck mode 25% |
| 4 | tracking | 66,667 | tested | 2.91 | 80 | 6.3 | 1.41 | 8.2 | 27 | 5% | 10% | 10% | 1% | 1% | 4% | neck mode 33% |
| 4.5 | tracking | 75,000 | tested | 3.27 | 90 | 6.4 | 2.04 | 10.5 | 30 | 6% | 12% | 13% | 2% | 2% | 5% | neck mode 37% |
| 5 | tracking | 83,333 | tested | 3.64 | 100 | 6.5 | 2.82 | 13.1 | 34 | 8% | 15% | 16% | 2% | 2% | 7% | neck mode 41% |
| 6 | tracking | 100,000 | tested | 4.36 | 120 | 6.6 | 4.89 | 19.1 | 41 | 11% | 22% | 23% | 3% | 3% | 10% | neck mode 50% |
| 7 | tracking | 116,667 | tested | 5.09 | 140 | 6.6 | 7.73 | 26.2 | 48 | 16% | 31% | 32% | 4% | 4% | 13% | neck mode 58% |
| 7.5 | power-capped | 125,000 | beyond tested | 5.09 | 140 | 4.9 | 7.73 | 22.5 | 39 | 14% | 26% | 28% | 4% | 5% | 15% | neck mode 62% |
| 8 | braked | 133,333 | beyond tested | 5.09 | 140 | 0.5 | 0.00 | 2.3 | 0 | 3% | 3% | 7% | 5% | 6% | 10% | generator heat 12% |
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
- As designed: generates 1.6-8.0 m/s, peak 7.73 W, braked above
- Kept generating within every limit: generates 1.8-11.0 m/s, peak 28.19 W at 11 m/s; nothing above 12.0 m/s
- Yearly energy, central case (kWh): 3.5 m/s site: as designed 6.6, within limits 8.0; 4.5 m/s site: as designed 9.4, within limits 15.7; 5.5 m/s site: as designed 10.2, within limits 23.2; 6.5 m/s site: as designed 9.8, within limits 28.1

| Wind (m/s) | Re | Flow | Wind through tube (W) | Model potential (W) | Within limits (W) | Within limits: what governs | As designed (W) | As designed: mode |
|---|---|---|---|---|---|---|---|---|
| 1 | 16,667 | tested | 0.2 | 0.00 | 0.00 | idle | 0.00 | idle |
| 2 | 33,333 | tested | 1.2 | 0.12 | 0.13 | unconstrained | 0.12 | tracking |
| 3 | 50,000 | tested | 4.1 | 0.55 | 0.56 | unconstrained | 0.55 | tracking |
| 4 | 66,667 | tested | 9.8 | 1.41 | 1.42 | unconstrained | 1.41 | tracking |
| 4.5 | 75,000 | tested | 14.0 | 2.04 | 2.06 | unconstrained | 2.04 | tracking |
| 5 | 83,333 | tested | 19.1 | 2.82 | 2.84 | unconstrained | 2.82 | tracking |
| 6 | 100,000 | tested | 33.1 | 4.89 | 4.94 | unconstrained | 4.89 | tracking |
| 7 | 116,667 | tested | 52.5 | 7.73 | 7.81 | unconstrained | 7.73 | tracking |
| 8 | 133,333 | beyond tested | 78.4 | 11.43 | 11.57 | unconstrained | 0.00 | braked |
| 9 | 150,000 | beyond tested | 111.6 | 16.08 | 16.31 | unconstrained | 0.00 | braked |
| 10 | 166,667 | beyond tested | 153.1 | 21.75 | 22.14 | unconstrained | 0.00 | braked |
| 11 | 183,333 | beyond tested | 203.8 | 28.51 | 28.19 | limited by skin | 0.00 | braked |
| 12 | 200,000 | beyond tested | 264.6 | 36.41 | 0.00 | braked (generator heat) | 0.00 | braked |
| 13 | 216,667 | drag crisis | 336.4 | 45.50 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 14 | 233,333 | drag crisis | 420.2 | 55.82 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 15 | 250,000 | drag crisis | 516.8 | 67.40 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 17.5 | 291,667 | drag crisis | 820.7 | 101.92 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 20 | 333,333 | drag crisis | 1,225.0 | 144.39 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 25 | 416,667 | drag crisis | 2,392.6 | 251.40 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 30 | 500,000 | drag crisis | 4,134.4 | 381.09 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 35 | 583,333 | drag crisis | 6,565.2 | 520.17 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 40 | 666,667 | drag crisis | 9,800.0 | 649.36 | 0.00 | braked (drag crisis) | 0.00 | braked |

## Structure at the survival requirement (25 m/s, parked and braked)

- Drag on the tube 115 N; bending moment at tube base 57 N m, at the hinge 149 N m (hub built for 150)
- Neck stress 118 MPa (allowable 400); skin stress at tube base 23.4 MPa (allowable 40)
- Shell ovalling 2.99 N m/m against a wall capacity of 6.00 N m/m
- End-disc gust utilisation 55%
- Hinge bushing load 998 N each
- Post base moment with hinge at 3 m: 554 N m (size the post to your local wind code)
- Swing cycles per year at 30 % duty: 3.1e+07

## Annual energy (very rough)

Rayleigh wind at hub height, power curve from the envelope above (tracking, then capped at 7.73 W, braked from 8.0 m/s), 50 % of swinging time assumed locked on. Low case = 0.5 x central.

| Site mean wind | Low (kWh/yr) | Central (kWh/yr) |
|---|---|---|
| 3.0 m/s | 2.3 | 4.6 |
| 3.5 m/s | 3.3 | 6.6 |
| 4.5 m/s | 4.7 | 9.4 |
| 5.5 m/s | 5.1 | 10.2 |

