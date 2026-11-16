# Lantern sweep: ranked by electrical power at 4.5 m/s, survival requirement 25 m/s

22440 combinations: D 0.2-0.3 m, neck 0.0-0.8 m, disc ratio 1.4-2.4, shells xps2-single, xps3-single, xps3-sandwich, xps5-sandwich, xps5-storm, pulley teeth [10, 12, 16, 20], neck tube sized automatically.  
6440 pass all limits. Rejected (a design can fail several): Reynolds 10200, operating loads 4162, survival 10504

| Rank | Score (W) | D (mm) | Neck (mm) | Neck tube | Disc ratio | Shell | Teeth | Gear | Mass ratio | Mech eff 4.5 | Swing 4.5 (deg) | Cut-in | Survives to | Re at U_max |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 2.05 | 250 | 800 | 25x23 | 2.0 | xps3-sandwich | 10 | 31.4 | 5.45 | 19.1 % | 6.4 | 1.6 | 25.1 (hub) | 116667 |
| 2 | 2.03 | 250 | 800 | 25x23 | 2.2 | xps3-sandwich | 10 | 31.4 | 5.77 | 19.0 % | 6.4 | 1.6 | 25.1 (hub) | 116667 |
| 3 | 2.02 | 250 | 750 | 25x23 | 2.0 | xps3-sandwich | 10 | 31.4 | 5.48 | 18.8 % | 6.6 | 1.6 | 25.6 (hub) | 116667 |
| 4 | 2.01 | 250 | 800 | 25x23 | 2.0 | xps3-sandwich | 12 | 26.2 | 5.28 | 19.4 % | 6.5 | 1.6 | 25.1 (hub) | 116667 |
| 5 | 2.01 | 250 | 750 | 25x23 | 2.2 | xps3-sandwich | 10 | 31.4 | 5.80 | 18.7 % | 6.6 | 1.6 | 25.6 (hub) | 116667 |
| 6 | 2.00 | 250 | 800 | 25x23 | 2.2 | xps3-sandwich | 12 | 26.2 | 5.60 | 19.3 % | 6.5 | 1.6 | 25.1 (hub) | 116667 |
| 7 | 2.00 | 250 | 750 | 25x23 | 2.0 | xps3-sandwich | 12 | 26.2 | 5.29 | 19.1 % | 6.7 | 1.6 | 25.6 (hub) | 116667 |
| 8 | 2.00 | 250 | 700 | 25x23 | 2.0 | xps3-sandwich | 10 | 31.4 | 5.51 | 18.5 % | 6.8 | 1.6 | 26.1 (hub) | 116667 |
| 9 | 1.99 | 250 | 800 | 30x28 | 2.0 | xps5-sandwich | 10 | 31.4 | 6.99 | 18.6 % | 6.3 | 1.6 | 25.1 (hub) | 116667 |
| 10 | 1.99 | 250 | 750 | 25x23 | 2.2 | xps3-sandwich | 12 | 26.2 | 5.62 | 19.0 % | 6.7 | 1.6 | 25.6 (hub) | 116667 |
| 11 | 1.99 | 250 | 700 | 25x23 | 2.2 | xps3-sandwich | 10 | 31.4 | 5.84 | 18.4 % | 6.8 | 1.6 | 26.1 (hub) | 116667 |
| 12 | 1.98 | 250 | 700 | 25x23 | 2.0 | xps3-sandwich | 12 | 26.2 | 5.31 | 18.8 % | 6.9 | 1.6 | 26.1 (hub) | 116667 |
| 13 | 1.97 | 250 | 800 | 30x28 | 2.0 | xps5-storm | 10 | 31.4 | 7.38 | 18.4 % | 6.3 | 1.6 | 25.1 (hub) | 116667 |
| 14 | 1.97 | 250 | 800 | 30x28 | 2.2 | xps5-sandwich | 10 | 31.4 | 7.42 | 18.4 % | 6.3 | 1.6 | 25.1 (hub) | 116667 |
| 15 | 1.97 | 250 | 650 | 25x23 | 2.0 | xps3-sandwich | 10 | 31.4 | 5.56 | 18.1 % | 7.0 | 1.7 | 26.6 (hub) | 116667 |

## Sensitivity around the best design (one variable at a time)

| Variable | Value | Score | vs best |
|---|---|---|---|
| D (mm) | 200 | 1.59 | -22 % |
| D (mm) | 210 | 1.68 | -18 % |
| D (mm) | 220 | 1.78 | -13 % |
| D (mm) | 230 | 1.87 | -9 % |
| D (mm) | 240 | 1.96 | -4 % |
| D (mm) | 250 | 2.05 | +0 % |
| D (mm) | 260 | 2.14 | +4 % (fails Reynolds, survival) |
| D (mm) | 270 | 2.22 | +9 % (fails Reynolds, survival) |
| D (mm) | 280 | 2.31 | +13 % (fails Reynolds, survival) |
| D (mm) | 290 | 2.40 | +17 % (fails Reynolds, survival) |
| D (mm) | 300 | 2.48 | +21 % (fails Reynolds, survival) |
| Neck (mm) | 0 | 1.11 | -46 % |
| Neck (mm) | 100 | 1.30 | -36 % |
| Neck (mm) | 200 | 1.48 | -28 % |
| Neck (mm) | 300 | 1.63 | -21 % |
| Neck (mm) | 400 | 1.75 | -14 % |
| Neck (mm) | 500 | 1.85 | -9 % |
| Neck (mm) | 600 | 1.93 | -5 % |
| Neck (mm) | 700 | 2.00 | -2 % |
| Neck (mm) | 800 | 2.05 | +0 % |
| Disc ratio | 1.4 | 1.77 | -14 % |
| Disc ratio | 1.6 | 1.86 | -9 % |
| Disc ratio | 1.8 | 1.96 | -4 % |
| Disc ratio | 2 | 2.05 | +0 % |
| Disc ratio | 2.2 | 2.03 | -1 % |
| Disc ratio | 2.4 | 2.02 | -1 % (fails survival) |
| Pulley teeth | 10 | 2.05 | +0 % |
| Pulley teeth | 12 | 2.01 | -2 % |
| Pulley teeth | 16 | 1.88 | -8 % (fails operating loads) |
| Pulley teeth | 20 | 1.67 | -18 % (fails operating loads) |
| Shell | xps2-single | 2.12 | +3 % (fails survival) |
| Shell | xps3-single | 2.09 | +2 % (fails survival) |
| Shell | xps3-sandwich | 2.05 | +0 % |
| Shell | xps5-sandwich | 1.99 | -3 % |
| Shell | xps5-storm | 1.97 | -4 % |

Best: shell xps3-sandwich. Full report for it follows.

# Lantern calculator report

Tube 250 mm x 1000 mm, neck 800 mm (25x23 mm carbon), end discs 500 mm, shell 0.211 kg/m^2 (sandwich, 3 mm core), survival requirement 25 m/s

Constraint check: all pass

## Operating summary

- Cut-in (starts and produces >10 mW): 1.6 m/s with kick-start
- Tracking: 2-7 m/s; power-capped at 7.76 W up to 8.0 m/s; braked above that
- Survives (parked, braked) up to **25.1 m/s**, limited by the hub. Requirement: 25 m/s. Per part: neck 27, skin 33, wall 35, discs 34, hub 25
- Worst while swinging: neck 44%, neck fatigue 86%, skin 32%, voltage 32%, generator heat 58%

## Masses (kg)

| Part | Mass |
|---|---|
| Tube shell incl. rings and seams | 0.186 |
| End discs, each | 0.041 |
| Bottom spider | 0.015 |
| Neck tube | 0.093 |
| Hub, axle, carriage, belt arc | 0.150 |
| **Total swinging mass** | **0.527** |

## Inertia about the hinge (kg m^2)

| Part | Inertia |
|---|---|
| shell | 0.3293 |
| discs | 0.1620 |
| spider | 0.0096 |
| neck | 0.0199 |
| hub | 0.0007 |
| generator | 0.0592 |
| Structural total | 0.5809 |
| Air moving with the tube | 0.1066 |
| **Total** | **0.6875** |
| Mass ratio (structural / displaced air) | 5.45 |

- Gear ratio: 31.4:1 (100 mm arc to 10-tooth GT2 pulley)
- Mode-shape factor gamma: 1.244
- Effective length after end losses: 1.000 m
- Gravity (destabilising) stiffness: 3.91 N m/rad

## Tuning

Two opposing springs, each 18.04 N/mm.

| Wind (m/s) | Tune f_n (Hz) | Stiffness (N m/rad) | Carriage below hinge (mm) |
|---|---|---|---|
| 2.0 | 1.45 | 61.3 | 41.2 |
| 3.0 | 2.18 | 133.1 | 60.7 |
| 4.0 | 2.91 | 233.6 | 80.5 |
| 4.5 | 3.27 | 294.6 | 90.4 |
| 5.0 | 3.64 | 362.8 | 100.3 |
| 6.0 | 4.36 | 520.7 | 120.1 |
| 7.0 | 5.09 | 707.4 | 140.0 |

Carriage moves about 19.8 mm per 1 m/s between 4 and 6 m/s.

## Operating points while tracking (model central case)

| Wind | Re | Swing f (Hz) | Wind power (W) | Mech (W) | Elec (W) | Elec low case (W) | Mech eff | Swing (deg) | Peak torque (N m) | Gen zeta | Parasitic zeta | Circuit R (ohm) | Copper eff | EMF peak (V) | Gen peak rpm | Top accel (g) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2.0 | 33333 | 1.60 | 1.2 | 0.15 | 0.12 | 0.06 | 12.4 % | 5.0 | 0.35 | 0.034 | 0.0216 | 359 | 97 % | 10.4 | 262 | 1.6 |
| 3.0 | 50000 | 2.40 | 4.1 | 0.71 | 0.55 | 0.28 | 17.1 % | 6.0 | 0.89 | 0.032 | 0.0109 | 253 | 95 % | 18.9 | 475 | 4.4 |
| 4.5 | 75000 | 3.60 | 14.0 | 2.67 | 2.05 | 1.02 | 19.1 % | 6.4 | 2.10 | 0.031 | 0.0073 | 172 | 93 % | 30.3 | 762 | 10.5 |
| 6.0 | 100000 | 4.80 | 33.1 | 6.56 | 4.91 | 2.45 | 19.8 % | 6.6 | 3.79 | 0.031 | 0.0062 | 130 | 91 % | 41.3 | 1038 | 19.1 |
| 7.0 | 116667 | 5.60 | 52.5 | 10.54 | 7.76 | 3.88 | 20.1 % | 6.6 | 5.19 | 0.031 | 0.0058 | 112 | 89 % | 48.5 | 1220 | 26.2 |

At 4.5 m/s: tube swings +/-90 mm at the bottom, +/-147 mm mid-height, +/-203 mm at the top; generator swings +/-202 deg. Friction: bushings 0.101 N m, generator drag 0.126 N m (at the hinge).

## Wind envelope, 1-40 m/s

Utilisation = load / allowable for each part (over 100% fails). Neck, skin and hub combine drag with the swing's inertia; wall is ovalling of the shell under wind pressure; discs is gust lift on the end discs. Parked modes use drag coefficient 1.2; swinging modes 2.0.

| Wind (m/s) | Mode | Re | Flow | Tuned to (Hz) | Carriage (mm) | Swing (±°) | Elec (W) | Top accel (g) | EMF (V) | Neck | Neck fatigue | Skin | Wall | Discs | Hub | Worst |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | idle | 16,667 | tested | 5.09 | 140 | 0.0 | 0.00 | 0.0 | 0 | 0% | 0% | 0% | 0% | 0% | 0% | hub 0% |
| 2 | tracking | 33,333 | tested | 1.45 | 41 | 5.0 | 0.12 | 1.6 | 10 | 3% | 5% | 2% | 0% | 0% | 1% | voltage 7% |
| 2.5 | tracking | 41,667 | tested | 1.82 | 51 | 5.7 | 0.29 | 2.9 | 15 | 5% | 9% | 3% | 0% | 1% | 2% | voltage 10% |
| 3 | tracking | 50,000 | tested | 2.18 | 61 | 6.0 | 0.55 | 4.4 | 19 | 7% | 14% | 5% | 1% | 1% | 2% | neck fatigue 14% |
| 4 | tracking | 66,667 | tested | 2.91 | 80 | 6.3 | 1.42 | 8.2 | 27 | 14% | 27% | 10% | 1% | 1% | 4% | neck fatigue 27% |
| 4.5 | tracking | 75,000 | tested | 3.27 | 90 | 6.4 | 2.05 | 10.5 | 30 | 18% | 34% | 13% | 2% | 2% | 5% | neck fatigue 34% |
| 5 | tracking | 83,333 | tested | 3.64 | 100 | 6.5 | 2.83 | 13.1 | 34 | 22% | 43% | 16% | 2% | 2% | 7% | neck fatigue 43% |
| 6 | tracking | 100,000 | tested | 4.36 | 120 | 6.6 | 4.91 | 19.1 | 41 | 32% | 62% | 23% | 3% | 3% | 10% | neck fatigue 62% |
| 7 | tracking | 116,667 | tested | 5.09 | 140 | 6.6 | 7.76 | 26.2 | 49 | 44% | 86% | 32% | 4% | 4% | 13% | neck fatigue 86% |
| 7.5 | power-capped | 125,000 | beyond tested | 5.09 | 140 | 5.0 | 7.76 | 22.5 | 39 | 39% | 74% | 28% | 4% | 5% | 15% | neck fatigue 74% |
| 8 | braked | 133,333 | beyond tested | 5.09 | 140 | 0.5 | 0.00 | 2.3 | 0 | 10% | 8% | 7% | 5% | 6% | 10% | generator heat 12% |
| 9 | braked | 150,000 | beyond tested | 5.09 | 140 | 0.0 | 0.00 | 0.0 | 0 | 11% | 0% | 8% | 6% | 7% | 13% | hub 13% |
| 10 | braked | 166,667 | beyond tested | 5.09 | 140 | 0.0 | 0.00 | 0.0 | 0 | 14% | 0% | 9% | 8% | 9% | 16% | hub 16% |
| 12 | braked | 200,000 | beyond tested | 5.09 | 140 | 0.0 | 0.00 | 0.0 | 0 | 20% | 0% | 13% | 11% | 13% | 23% | hub 23% |
| 15 | braked | 250,000 | drag crisis | 5.09 | 140 | 0.0 | 0.00 | 0.0 | 0 | 31% | 0% | 21% | 18% | 20% | 36% | hub 36% |
| 20 | braked | 333,333 | drag crisis | 5.09 | 140 | 0.0 | 0.00 | 0.0 | 0 | 55% | 0% | 37% | 32% | 35% | 64% | hub 64% |
| 25 | braked | 416,667 | drag crisis | 5.09 | 140 | 0.0 | 0.00 | 0.0 | 0 | 86% | 0% | 58% | 50% | 55% | 100% | hub 100% |
| 30 | braked | 500,000 | drag crisis | 5.09 | 140 | 0.0 | 0.00 | 0.0 | 0 | 124% | 0% | 84% | 72% | 79% | 143% | hub 143% **FAIL** |
| 35 | braked | 583,333 | drag crisis | 5.09 | 140 | 0.0 | 0.00 | 0.0 | 0 | 168% | 0% | 115% | 98% | 107% | 195% | hub 195% **FAIL** |
| 40 | braked | 666,667 | drag crisis | 5.09 | 140 | 0.0 | 0.00 | 0.0 | 0 | 220% | 0% | 150% | 128% | 140% | 255% | hub 255% **FAIL** |

## Structure at the survival requirement (25 m/s, parked and braked)

- Drag on the tube 115 N; bending moment at tube base 57 N m, at the hinge 149 N m (hub built for 150)
- Neck stress 343 MPa (allowable 400); skin stress at tube base 23.4 MPa (allowable 40)
- Shell ovalling 2.99 N m/m against a wall capacity of 6.00 N m/m
- End-disc gust utilisation 55%
- Hinge bushing load 998 N each
- Post base moment with hinge at 3 m: 554 N m (size the post to your local wind code)
- Swing cycles per year at 30 % duty: 3.1e+07

## Annual energy (very rough)

Rayleigh wind at hub height, power curve from the envelope above (tracking, then capped at 7.76 W, braked from 8.0 m/s), 50 % of swinging time assumed locked on. Low case = 0.5 x central.

| Site mean wind | Low (kWh/yr) | Central (kWh/yr) |
|---|---|---|
| 3.0 m/s | 2.3 | 4.6 |
| 3.5 m/s | 3.3 | 6.6 |
| 4.5 m/s | 4.7 | 9.4 |
| 5.5 m/s | 5.1 | 10.3 |

