# Lantern sweep: ranked by electrical power at 4.5 m/s, survival requirement 25 m/s

17280 combinations: D 0.1-0.4 m, neck 0.0-0.8 m, disc ratio 1.0-2.4, shells xps2-single, xps3-single, xps3-sandwich, xps5-sandwich, xps5-storm, pulley teeth [10, 12, 16], neck tube sized automatically.  
6670 pass all limits. Rejected (a design can fail several): operating loads 3770, survival 9477

| Rank | Score (W) | D (mm) | Neck (mm) | Neck tube | Disc ratio | Shell | Teeth | Gear | Mass ratio | Mech eff 4.5 | Swing 4.5 (deg) | Cut-in | Survives to | Re at U_max |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 2.98 | 400 | 500 | 30x28 | 2.0 | xps5-sandwich | 10 | 31.4 | 5.09 | 17.4 % | 12.6 | 1.6 | 27.2 (discs) | 186667 |
| 2 | 2.97 | 400 | 500 | 30x28 | 2.0 | xps5-storm | 10 | 31.4 | 5.33 | 17.3 % | 12.5 | 1.6 | 27.2 (discs) | 186667 |
| 3 | 2.94 | 380 | 600 | 30x28 | 2.0 | xps5-sandwich | 10 | 31.4 | 5.17 | 18.2 % | 11.2 | 1.6 | 28.5 (hub) | 177333 |
| 4 | 2.92 | 380 | 600 | 30x28 | 2.0 | xps5-storm | 10 | 31.4 | 5.42 | 18.1 % | 11.2 | 1.6 | 28.5 (hub) | 177333 |
| 5 | 2.84 | 400 | 400 | 25x23 | 2.0 | xps5-sandwich | 10 | 31.4 | 5.22 | 16.4 % | 13.4 | 1.6 | 25.6 (neck) | 186667 |
| 6 | 2.83 | 380 | 500 | 30x28 | 2.0 | xps5-sandwich | 10 | 31.4 | 5.26 | 17.3 % | 11.9 | 1.6 | 28.7 (discs) | 177333 |
| 7 | 2.83 | 400 | 400 | 25x23 | 2.0 | xps5-storm | 10 | 31.4 | 5.46 | 16.3 % | 13.4 | 1.6 | 25.6 (neck) | 186667 |
| 8 | 2.82 | 380 | 500 | 30x28 | 2.0 | xps5-storm | 10 | 31.4 | 5.52 | 17.2 % | 11.9 | 1.6 | 28.7 (discs) | 177333 |

## Sensitivity around the best design (one variable at a time)

| Variable | Value | Score | vs best |
|---|---|---|---|
| D (mm) | 100 | 0.47 | -84 % (fails survival, operating loads) |
| D (mm) | 140 | 0.83 | -72 % (fails survival, operating loads) |
| D (mm) | 180 | 1.19 | -60 % |
| D (mm) | 220 | 1.54 | -48 % |
| D (mm) | 260 | 1.88 | -37 % |
| D (mm) | 300 | 2.21 | -26 % |
| D (mm) | 340 | 2.53 | -15 % |
| D (mm) | 380 | 2.83 | -5 % |
| Neck (mm) | 0 | 1.92 | -36 % |
| Neck (mm) | 100 | 2.20 | -26 % |
| Neck (mm) | 200 | 2.45 | -18 % |
| Neck (mm) | 300 | 2.67 | -11 % |
| Neck (mm) | 400 | 2.84 | -5 % |
| Neck (mm) | 500 | 2.98 | +0 % |
| Neck (mm) | 600 | 3.09 | +4 % (fails operating loads) |
| Neck (mm) | 700 | 3.16 | +6 % (fails operating loads) |
| Neck (mm) | 800 | 3.21 | +8 % (fails operating loads) |
| Disc ratio | 1 | 1.87 | -37 % |
| Disc ratio | 1.2 | 2.08 | -30 % |
| Disc ratio | 1.4 | 2.32 | -22 % |
| Disc ratio | 1.6 | 2.54 | -15 % |
| Disc ratio | 1.8 | 2.77 | -7 % |
| Disc ratio | 2 | 2.98 | +0 % |
| Disc ratio | 2.2 | 2.95 | -1 % (fails survival) |
| Disc ratio | 2.4 | 2.92 | -2 % (fails survival) |
| Pulley teeth | 10 | 2.98 | +0 % |
| Pulley teeth | 12 | 2.92 | -2 % (fails operating loads) |
| Pulley teeth | 16 | 2.72 | -9 % (fails operating loads) |
| Shell | xps2-single | 3.13 | +5 % (fails survival) |
| Shell | xps3-single | 3.10 | +4 % (fails survival) |
| Shell | xps3-sandwich | 3.05 | +2 % (fails survival) |
| Shell | xps5-sandwich | 2.98 | +0 % |
| Shell | xps5-storm | 2.97 | -0 % |

Best: shell xps5-sandwich. Full report for it follows.

# Lantern calculator report

Tube 400 mm x 1000 mm, neck 500 mm (30x28 mm carbon), end discs 800 mm, shell 0.285 kg/m^2 (sandwich, 5 mm core), survival requirement 25 m/s

Constraint check: all pass

## Operating summary

- Cut-in (starts and produces >10 mW): 1.6 m/s with kick-start
- Tracking: 2-7 m/s; power-capped at 11.22 W up to 8.0 m/s; braked above that
- Survives (parked, braked) up to **27.2 m/s**, limited by the discs. Requirement: 25 m/s. Per part: neck 29, skin 41, wall 29, discs 27, hub 29
- Worst while swinging: neck 35%, neck fatigue 67%, skin 19%, voltage 39%, generator heat 84%

## Masses (kg)

| Part | Mass |
|---|---|
| Tube shell incl. rings and seams | 0.378 |
| End discs, each | 0.143 |
| Bottom spider | 0.015 |
| Neck tube | 0.071 |
| Hub, axle, carriage, belt arc | 0.150 |
| **Total swinging mass** | **0.900** |

## Inertia about the hinge (kg m^2)

| Part | Inertia |
|---|---|
| shell | 0.4097 |
| discs | 0.3696 |
| spider | 0.0037 |
| neck | 0.0059 |
| hub | 0.0007 |
| generator | 0.0592 |
| Structural total | 0.8488 |
| Air moving with the tube | 0.1668 |
| **Total** | **1.0156** |
| Mass ratio (structural / displaced air) | 5.09 |

- Gear ratio: 31.4:1 (100 mm arc to 10-tooth GT2 pulley)
- Mode-shape factor gamma: 1.269
- Effective length after end losses: 1.000 m
- Gravity (destabilising) stiffness: 6.77 N m/rad

## Tuning

Two opposing springs, each 10.53 N/mm.

| Wind (m/s) | Tune f_n (Hz) | Stiffness (N m/rad) | Carriage below hinge (mm) |
|---|---|---|---|
| 2.0 | 0.91 | 39.9 | 43.5 |
| 3.0 | 1.36 | 81.3 | 62.1 |
| 4.0 | 1.82 | 139.3 | 81.3 |
| 4.5 | 2.05 | 174.5 | 91.0 |
| 5.0 | 2.27 | 213.9 | 100.8 |
| 6.0 | 2.73 | 305.0 | 120.4 |
| 7.0 | 3.18 | 412.7 | 140.0 |

Carriage moves about 19.5 mm per 1 m/s between 4 and 6 m/s.

## Operating points while tracking (model central case)

| Wind | Re | Swing f (Hz) | Wind power (W) | Mech (W) | Elec (W) | Elec low case (W) | Mech eff | Swing (deg) | Peak torque (N m) | Gen zeta | Parasitic zeta | Circuit R (ohm) | Copper eff | EMF peak (V) | Gen peak rpm | Top accel (g) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2.0 | 53333 | 1.00 | 2.0 | 0.24 | 0.19 | 0.10 | 12.3 % | 10.3 | 0.43 | 0.036 | 0.0197 | 374 | 97 % | 13.4 | 337 | 1.1 |
| 3.0 | 80000 | 1.50 | 6.6 | 1.05 | 0.82 | 0.41 | 15.8 % | 11.9 | 1.07 | 0.034 | 0.0106 | 261 | 95 % | 23.4 | 587 | 2.8 |
| 4.5 | 120000 | 2.25 | 22.3 | 3.88 | 2.98 | 1.49 | 17.4 % | 12.6 | 2.50 | 0.034 | 0.0073 | 177 | 93 % | 37.0 | 931 | 6.7 |
| 6.0 | 160000 | 3.00 | 52.9 | 9.48 | 7.11 | 3.56 | 17.9 % | 12.8 | 4.50 | 0.033 | 0.0063 | 133 | 91 % | 50.3 | 1263 | 12.1 |
| 7.0 | 186667 | 3.50 | 84.0 | 15.21 | 11.22 | 5.61 | 18.1 % | 12.9 | 6.15 | 0.033 | 0.0059 | 114 | 90 % | 59.0 | 1483 | 16.6 |

At 4.5 m/s: tube swings +/-111 mm at the bottom, +/-223 mm mid-height, +/-334 mm at the top; generator swings +/-395 deg. Friction: bushings 0.127 N m, generator drag 0.126 N m (at the hinge).

## Wind envelope, 1-40 m/s

Utilisation = load / allowable for each part (over 100% fails). Neck, skin and hub combine drag with the swing's inertia; wall is ovalling of the shell under wind pressure; discs is gust lift on the end discs. Parked modes use drag coefficient 1.2; swinging modes 2.0.

| Wind (m/s) | Mode | Re | Flow | Tuned to (Hz) | Carriage (mm) | Swing (±°) | Elec (W) | Top accel (g) | EMF (V) | Neck | Neck fatigue | Skin | Wall | Discs | Hub | Worst |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | idle | 26,667 | tested | 3.18 | 140 | 0.0 | 0.00 | 0.0 | 0 | 0% | 0% | 0% | 0% | 0% | 0% | discs 0% |
| 2 | tracking | 53,333 | tested | 0.91 | 44 | 10.3 | 0.19 | 1.1 | 13 | 2% | 4% | 1% | 0% | 1% | 1% | voltage 9% |
| 2.5 | tracking | 66,667 | tested | 1.14 | 53 | 11.3 | 0.44 | 1.9 | 19 | 4% | 8% | 2% | 1% | 1% | 1% | voltage 12% |
| 3 | tracking | 80,000 | tested | 1.36 | 62 | 11.9 | 0.82 | 2.8 | 23 | 6% | 11% | 3% | 1% | 1% | 2% | voltage 16% |
| 4 | tracking | 106,667 | tested | 1.82 | 81 | 12.4 | 2.07 | 5.2 | 33 | 11% | 21% | 6% | 2% | 2% | 3% | voltage 22% |
| 4.5 | tracking | 120,000 | tested | 2.05 | 91 | 12.6 | 2.98 | 6.7 | 37 | 14% | 27% | 8% | 2% | 3% | 4% | neck fatigue 27% |
| 5 | tracking | 133,333 | tested | 2.27 | 101 | 12.7 | 4.11 | 8.3 | 41 | 18% | 34% | 10% | 3% | 3% | 5% | neck fatigue 34% |
| 6 | tracking | 160,000 | tested | 2.73 | 120 | 12.8 | 7.11 | 12.1 | 50 | 25% | 49% | 14% | 4% | 5% | 7% | neck fatigue 49% |
| 7 | tracking | 186,667 | tested | 3.18 | 140 | 12.9 | 11.22 | 16.6 | 59 | 35% | 67% | 19% | 6% | 7% | 10% | neck fatigue 67% |
| 7.5 | power-capped | 200,000 | tested | 3.18 | 140 | 9.6 | 11.22 | 14.2 | 47 | 31% | 57% | 17% | 7% | 8% | 11% | generator heat 60% |
| 8 | braked | 213,333 | drag crisis | 3.18 | 140 | 0.8 | 0.00 | 1.4 | 0 | 8% | 6% | 4% | 8% | 9% | 8% | generator heat 16% |
| 9 | braked | 240,000 | drag crisis | 3.18 | 140 | 0.0 | 0.00 | 0.0 | 0 | 9% | 0% | 5% | 10% | 11% | 10% | discs 11% |
| 10 | braked | 266,667 | drag crisis | 3.18 | 140 | 0.0 | 0.00 | 0.0 | 0 | 11% | 0% | 6% | 12% | 13% | 12% | discs 13% |
| 12 | braked | 320,000 | drag crisis | 3.18 | 140 | 0.0 | 0.00 | 0.0 | 0 | 17% | 0% | 8% | 18% | 19% | 17% | discs 19% |
| 15 | braked | 400,000 | drag crisis | 3.18 | 140 | 0.0 | 0.00 | 0.0 | 0 | 26% | 0% | 13% | 28% | 30% | 26% | discs 30% |
| 20 | braked | 533,333 | drag crisis | 3.18 | 140 | 0.0 | 0.00 | 0.0 | 0 | 46% | 0% | 23% | 49% | 54% | 47% | discs 54% |
| 25 | braked | 666,667 | drag crisis | 3.18 | 140 | 0.0 | 0.00 | 0.0 | 0 | 72% | 0% | 37% | 77% | 84% | 74% | discs 84% |
| 30 | braked | 800,000 | drag crisis | 3.18 | 140 | 0.0 | 0.00 | 0.0 | 0 | 103% | 0% | 53% | 110% | 121% | 106% | discs 121% **FAIL** |
| 35 | braked | 933,333 | drag crisis | 3.18 | 140 | 0.0 | 0.00 | 0.0 | 0 | 141% | 0% | 72% | 150% | 165% | 144% | discs 165% **FAIL** |
| 40 | braked | 1,066,667 | drag crisis | 3.18 | 140 | 0.0 | 0.00 | 0.0 | 0 | 184% | 0% | 94% | 196% | 216% | 188% | discs 216% **FAIL** |

## Structure at the survival requirement (25 m/s, parked and braked)

- Drag on the tube 184 N; bending moment at tube base 92 N m, at the hinge 184 N m (hub built for 250)
- Neck stress 287 MPa (allowable 400); skin stress at tube base 14.6 MPa (allowable 40)
- Shell ovalling 7.66 N m/m against a wall capacity of 10.00 N m/m
- End-disc gust utilisation 84%
- Hinge bushing load 1229 N each
- Post base moment with hinge at 3 m: 795 N m (size the post to your local wind code)
- Swing cycles per year at 30 % duty: 1.9e+07

## Annual energy (very rough)

Rayleigh wind at hub height, power curve from the envelope above (tracking, then capped at 11.22 W, braked from 8.0 m/s), 50 % of swinging time assumed locked on. Low case = 0.5 x central.

| Site mean wind | Low (kWh/yr) | Central (kWh/yr) |
|---|---|---|
| 3.0 m/s | 3.4 | 6.8 |
| 3.5 m/s | 4.8 | 9.6 |
| 4.5 m/s | 6.8 | 13.7 |
| 5.5 m/s | 7.4 | 14.9 |

