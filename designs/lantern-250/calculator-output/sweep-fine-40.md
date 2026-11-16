# Lantern sweep: ranked by electrical power at 4.5 m/s, survival requirement 40 m/s

22440 combinations: D 0.2-0.3 m, neck 0.0-0.8 m, disc ratio 1.4-2.4, shells xps2-single, xps3-single, xps3-sandwich, xps5-sandwich, xps5-storm, pulley teeth [10, 12, 16, 20], neck tube sized automatically.  
1597 pass all limits. Rejected (a design can fail several): Reynolds 10200, operating loads 4104, survival 20140

| Rank | Score (W) | D (mm) | Neck (mm) | Neck tube | Disc ratio | Shell | Teeth | Gear | Mass ratio | Mech eff 4.5 | Swing 4.5 (deg) | Cut-in | Survives to | Re at U_max |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1.87 | 250 | 650 | 35x32 | 2.0 | xps5-storm | 10 | 31.4 | 7.91 | 17.2 % | 6.8 | 1.7 | 40.7 (hub) | 116667 |
| 2 | 1.86 | 250 | 650 | 35x32 | 2.0 | xps5-storm | 12 | 26.2 | 7.69 | 17.6 % | 6.9 | 1.6 | 40.7 (hub) | 116667 |
| 3 | 1.84 | 250 | 600 | 35x32 | 2.0 | xps5-storm | 10 | 31.4 | 7.95 | 16.9 % | 7.0 | 1.7 | 41.6 (hub) | 116667 |
| 4 | 1.84 | 250 | 600 | 35x32 | 2.0 | xps5-storm | 12 | 26.2 | 7.71 | 17.2 % | 7.1 | 1.6 | 41.6 (hub) | 116667 |
| 5 | 1.81 | 240 | 700 | 35x32 | 2.0 | xps5-storm | 10 | 31.4 | 8.19 | 17.4 % | 6.3 | 1.7 | 40.7 (hub) | 112000 |
| 6 | 1.81 | 250 | 550 | 35x32 | 2.0 | xps5-storm | 12 | 26.2 | 7.74 | 16.8 % | 7.3 | 1.6 | 42.6 (hub) | 116667 |
| 7 | 1.80 | 250 | 550 | 35x32 | 2.0 | xps5-storm | 10 | 31.4 | 8.00 | 16.5 % | 7.3 | 1.8 | 42.6 (hub) | 116667 |
| 8 | 1.80 | 240 | 700 | 35x32 | 2.0 | xps5-storm | 12 | 26.2 | 7.98 | 17.8 % | 6.4 | 1.6 | 40.7 (hub) | 112000 |
| 9 | 1.79 | 250 | 650 | 35x32 | 1.8 | xps5-storm | 10 | 31.4 | 7.50 | 16.5 % | 6.9 | 1.7 | 40.7 (hub) | 116667 |
| 10 | 1.79 | 240 | 650 | 35x32 | 2.0 | xps5-storm | 10 | 31.4 | 8.22 | 17.1 % | 6.5 | 1.7 | 41.5 (hub) | 112000 |
| 11 | 1.78 | 250 | 650 | 35x32 | 1.8 | xps5-storm | 12 | 26.2 | 7.29 | 16.8 % | 6.9 | 1.6 | 40.7 (hub) | 116667 |
| 12 | 1.78 | 240 | 650 | 35x32 | 2.0 | xps5-storm | 12 | 26.2 | 7.99 | 17.5 % | 6.6 | 1.6 | 41.5 (hub) | 112000 |
| 13 | 1.77 | 250 | 500 | 35x32 | 2.0 | xps5-storm | 12 | 26.2 | 7.79 | 16.4 % | 7.6 | 1.7 | 43.6 (discs) | 116667 |
| 14 | 1.77 | 250 | 600 | 35x32 | 2.0 | xps5-storm | 16 | 19.6 | 7.48 | 17.7 % | 7.2 | 1.6 | 41.6 (hub) | 116667 |
| 15 | 1.76 | 250 | 500 | 35x32 | 2.0 | xps5-storm | 10 | 31.4 | 8.07 | 16.0 % | 7.5 | 1.8 | 43.6 (discs) | 116667 |

## Sensitivity around the best design (one variable at a time)

| Variable | Value | Score | vs best |
|---|---|---|---|
| D (mm) | 200 | 1.43 | -24 % |
| D (mm) | 210 | 1.52 | -19 % |
| D (mm) | 220 | 1.61 | -14 % |
| D (mm) | 230 | 1.70 | -9 % |
| D (mm) | 240 | 1.79 | -5 % |
| D (mm) | 250 | 1.87 | +0 % |
| D (mm) | 260 | 1.96 | +5 % (fails Reynolds, survival) |
| D (mm) | 270 | 2.05 | +9 % (fails Reynolds, survival) |
| D (mm) | 280 | 2.13 | +14 % (fails Reynolds, survival) |
| D (mm) | 290 | 2.22 | +18 % (fails Reynolds, survival) |
| D (mm) | 300 | 2.30 | +23 % (fails Reynolds, survival) |
| Neck (mm) | 0 | 1.04 | -44 % |
| Neck (mm) | 100 | 1.23 | -34 % |
| Neck (mm) | 200 | 1.40 | -25 % |
| Neck (mm) | 300 | 1.55 | -17 % |
| Neck (mm) | 400 | 1.67 | -11 % |
| Neck (mm) | 500 | 1.76 | -6 % |
| Neck (mm) | 600 | 1.84 | -2 % |
| Neck (mm) | 700 | 1.90 | +2 % (fails survival) |
| Neck (mm) | 800 | 1.95 | +4 % (fails survival) |
| Disc ratio | 1.4 | 1.63 | -13 % |
| Disc ratio | 1.6 | 1.71 | -9 % |
| Disc ratio | 1.8 | 1.79 | -4 % |
| Disc ratio | 2 | 1.87 | +0 % |
| Disc ratio | 2.2 | 1.86 | -1 % (fails survival) |
| Disc ratio | 2.4 | 1.84 | -2 % (fails survival) |
| Pulley teeth | 10 | 1.87 | +0 % |
| Pulley teeth | 12 | 1.86 | -1 % |
| Pulley teeth | 16 | 1.78 | -5 % (fails operating loads) |
| Pulley teeth | 20 | 1.64 | -13 % (fails operating loads) |
| Shell | xps2-single | 2.01 | +7 % (fails survival) |
| Shell | xps3-single | 1.98 | +6 % (fails survival) |
| Shell | xps3-sandwich | 1.94 | +4 % (fails survival) |
| Shell | xps5-sandwich | 1.89 | +1 % (fails survival) |
| Shell | xps5-storm | 1.87 | +0 % |

Best: shell xps5-storm. Full report for it follows.

# Lantern calculator report

Tube 250 mm x 1000 mm, neck 650 mm (35x32 mm carbon), end discs 500 mm, shell 0.315 kg/m^2 (sandwich, 5 mm core), survival requirement 40 m/s

Constraint check: all pass

## Operating summary

- Cut-in (starts and produces >10 mW): 1.7 m/s with kick-start
- Tracking: 2-7 m/s; power-capped at 7.25 W up to 8.0 m/s; braked above that
- Survives (parked, braked) up to **40.7 m/s**, limited by the hub. Requirement: 40 m/s. Per part: neck 49, skin 57, wall 46, discs 44, hub 41
- Worst while swinging: neck 19%, neck fatigue 37%, skin 15%, voltage 35%, generator heat 43%

## Masses (kg)

| Part | Mass |
|---|---|
| Tube shell incl. rings and seams | 0.285 |
| End discs, each | 0.056 |
| Bottom spider | 0.015 |
| Neck tube | 0.159 |
| Hub, axle, carriage, belt arc | 0.300 |
| **Total swinging mass** | **0.871** |

## Inertia about the hinge (kg m^2)

| Part | Inertia |
|---|---|
| shell | 0.4012 |
| discs | 0.1777 |
| spider | 0.0063 |
| neck | 0.0224 |
| hub | 0.0015 |
| generator | 0.0592 |
| Structural total | 0.6684 |
| Air moving with the tube | 0.0845 |
| **Total** | **0.7529** |
| Mass ratio (structural / displaced air) | 7.91 |

- Gear ratio: 31.4:1 (100 mm arc to 10-tooth GT2 pulley)
- Mode-shape factor gamma: 1.257
- Effective length after end losses: 1.000 m
- Gravity (destabilising) stiffness: 5.09 N m/rad

## Tuning

Two opposing springs, each 19.78 N/mm.

| Wind (m/s) | Tune f_n (Hz) | Stiffness (N m/rad) | Carriage below hinge (mm) |
|---|---|---|---|
| 2.0 | 1.45 | 68.0 | 41.4 |
| 3.0 | 2.18 | 146.6 | 60.9 |
| 4.0 | 2.91 | 256.6 | 80.5 |
| 4.5 | 3.27 | 323.5 | 90.4 |
| 5.0 | 3.64 | 398.1 | 100.3 |
| 6.0 | 4.36 | 571.1 | 120.1 |
| 7.0 | 5.09 | 775.5 | 140.0 |

Carriage moves about 19.8 mm per 1 m/s between 4 and 6 m/s.

## Operating points while tracking (model central case)

| Wind | Re | Swing f (Hz) | Wind power (W) | Mech (W) | Elec (W) | Elec low case (W) | Mech eff | Swing (deg) | Peak torque (N m) | Gen zeta | Parasitic zeta | Circuit R (ohm) | Copper eff | EMF peak (V) | Gen peak rpm | Top accel (g) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2.0 | 33333 | 1.60 | 1.2 | 0.12 | 0.09 | 0.05 | 9.6 % | 4.8 | 0.28 | 0.024 | 0.0200 | 436 | 97 % | 10.1 | 255 | 1.4 |
| 3.0 | 50000 | 2.40 | 4.1 | 0.62 | 0.49 | 0.25 | 15.0 % | 6.3 | 0.75 | 0.022 | 0.0097 | 314 | 96 % | 19.7 | 496 | 4.2 |
| 4.5 | 75000 | 3.60 | 14.0 | 2.41 | 1.87 | 0.94 | 17.2 % | 6.8 | 1.79 | 0.022 | 0.0065 | 215 | 94 % | 32.2 | 808 | 10.2 |
| 6.0 | 100000 | 4.80 | 33.1 | 5.97 | 4.56 | 2.28 | 18.0 % | 7.0 | 3.24 | 0.022 | 0.0055 | 162 | 93 % | 44.0 | 1107 | 18.7 |
| 7.0 | 116667 | 5.60 | 52.5 | 9.62 | 7.25 | 3.62 | 18.3 % | 7.1 | 4.43 | 0.022 | 0.0051 | 140 | 91 % | 51.8 | 1302 | 25.7 |

At 4.5 m/s: tube swings +/-78 mm at the bottom, +/-138 mm mid-height, +/-197 mm at the top; generator swings +/-214 deg. Friction: bushings 0.096 N m, generator drag 0.126 N m (at the hinge).

## Wind envelope, 1-40 m/s

Utilisation = load / allowable for each part (over 100% fails). Neck, skin and hub combine drag with the swing's inertia; wall is ovalling of the shell under wind pressure; discs is gust lift on the end discs. Parked modes use drag coefficient 1.2; swinging modes 2.0.

| Wind (m/s) | Mode | Re | Flow | Tuned to (Hz) | Carriage (mm) | Swing (±°) | Elec (W) | Top accel (g) | EMF (V) | Neck | Neck fatigue | Skin | Wall | Discs | Hub | Worst |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | idle | 16,667 | tested | 5.09 | 140 | 0.0 | 0.00 | 0.0 | 0 | 0% | 0% | 0% | 0% | 0% | 0% | hub 0% |
| 2 | tracking | 33,333 | tested | 1.45 | 41 | 4.8 | 0.09 | 1.4 | 10 | 1% | 2% | 1% | 0% | 0% | 0% | voltage 7% |
| 2.5 | tracking | 41,667 | tested | 1.82 | 51 | 5.8 | 0.25 | 2.7 | 15 | 2% | 4% | 2% | 0% | 0% | 1% | voltage 10% |
| 3 | tracking | 50,000 | tested | 2.18 | 61 | 6.3 | 0.49 | 4.2 | 20 | 3% | 6% | 2% | 0% | 0% | 1% | voltage 13% |
| 4 | tracking | 66,667 | tested | 2.91 | 81 | 6.7 | 1.29 | 8.0 | 28 | 6% | 11% | 5% | 1% | 1% | 2% | voltage 19% |
| 4.5 | tracking | 75,000 | tested | 3.27 | 90 | 6.8 | 1.87 | 10.2 | 32 | 7% | 15% | 6% | 1% | 1% | 2% | voltage 21% |
| 5 | tracking | 83,333 | tested | 3.64 | 100 | 6.9 | 2.61 | 12.8 | 36 | 9% | 18% | 7% | 1% | 1% | 3% | voltage 24% |
| 6 | tracking | 100,000 | tested | 4.36 | 120 | 7.0 | 4.56 | 18.7 | 44 | 14% | 27% | 11% | 2% | 2% | 4% | voltage 29% |
| 7 | tracking | 116,667 | tested | 5.09 | 140 | 7.1 | 7.25 | 25.7 | 52 | 19% | 37% | 15% | 2% | 3% | 5% | neck fatigue 37% |
| 7.5 | power-capped | 125,000 | beyond tested | 5.09 | 140 | 5.2 | 7.25 | 21.6 | 41 | 16% | 31% | 13% | 3% | 3% | 6% | generator heat 31% |
| 8 | braked | 133,333 | beyond tested | 5.09 | 140 | 0.2 | 0.00 | 1.1 | 0 | 3% | 2% | 2% | 3% | 3% | 4% | hub 4% |
| 9 | braked | 150,000 | beyond tested | 5.09 | 140 | 0.0 | 0.00 | 0.0 | 0 | 3% | 0% | 3% | 4% | 4% | 5% | hub 5% |
| 10 | braked | 166,667 | beyond tested | 5.09 | 140 | 0.0 | 0.00 | 0.0 | 0 | 4% | 0% | 3% | 5% | 5% | 6% | hub 6% |
| 12 | braked | 200,000 | beyond tested | 5.09 | 140 | 0.0 | 0.00 | 0.0 | 0 | 6% | 0% | 4% | 7% | 8% | 9% | hub 9% |
| 15 | braked | 250,000 | drag crisis | 5.09 | 140 | 0.0 | 0.00 | 0.0 | 0 | 9% | 0% | 7% | 11% | 12% | 14% | hub 14% |
| 20 | braked | 333,333 | drag crisis | 5.09 | 140 | 0.0 | 0.00 | 0.0 | 0 | 17% | 0% | 12% | 19% | 21% | 24% | hub 24% |
| 25 | braked | 416,667 | drag crisis | 5.09 | 140 | 0.0 | 0.00 | 0.0 | 0 | 26% | 0% | 19% | 30% | 33% | 38% | hub 38% |
| 30 | braked | 500,000 | drag crisis | 5.09 | 140 | 0.0 | 0.00 | 0.0 | 0 | 37% | 0% | 28% | 43% | 47% | 54% | hub 54% |
| 35 | braked | 583,333 | drag crisis | 5.09 | 140 | 0.0 | 0.00 | 0.0 | 0 | 51% | 0% | 38% | 59% | 64% | 74% | hub 74% |
| 40 | braked | 666,667 | drag crisis | 5.09 | 140 | 0.0 | 0.00 | 0.0 | 0 | 67% | 0% | 50% | 77% | 84% | 97% | hub 97% |

## Structure at the survival requirement (40 m/s, parked and braked)

- Drag on the tube 294 N; bending moment at tube base 147 N m, at the hinge 338 N m (hub built for 350)
- Neck stress 267 MPa (allowable 400); skin stress at tube base 20.0 MPa (allowable 40)
- Shell ovalling 7.66 N m/m against a wall capacity of 10.00 N m/m
- End-disc gust utilisation 84%
- Hinge bushing load 1695 N each
- Post base moment with hinge at 3 m: 1373 N m (size the post to your local wind code)
- Swing cycles per year at 30 % duty: 3.1e+07

## Annual energy (very rough)

Rayleigh wind at hub height, power curve from the envelope above (tracking, then capped at 7.25 W, braked from 8.0 m/s), 50 % of swinging time assumed locked on. Low case = 0.5 x central.

| Site mean wind | Low (kWh/yr) | Central (kWh/yr) |
|---|---|---|
| 3.0 m/s | 2.1 | 4.2 |
| 3.5 m/s | 3.0 | 6.1 |
| 4.5 m/s | 4.3 | 8.7 |
| 5.5 m/s | 4.7 | 9.5 |

