# Lantern sweep: ranked by electrical power at 4.5 m/s, survival requirement 25 m/s

28800 combinations: D 0.1-0.4 m, neck 0.0-0.8 m, disc ratio 1.0-2.4, shells xps2-single, xps3-single, xps3-sandwich, xps5-sandwich, xps5-storm, pulley teeth [10, 12, 16, 20, 24], neck tube sized automatically.  
5743 pass all limits. Rejected (a design can fail several): Reynolds 14400, operating loads 10128, survival 18030

| Rank | Score (W) | D (mm) | Neck (mm) | Neck tube | Disc ratio | Shell | Teeth | Gear | Mass ratio | Mech eff 4.5 | Swing 4.5 (deg) | Cut-in | Survives to | Re at U_max |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1.96 | 240 | 800 | 25x23 | 2.0 | xps3-sandwich | 10 | 31.4 | 5.66 | 19.0 % | 6.2 | 1.6 | 25.6 (hub) | 112000 |
| 2 | 1.95 | 240 | 800 | 25x23 | 2.2 | xps3-sandwich | 10 | 31.4 | 5.98 | 18.9 % | 6.1 | 1.6 | 25.6 (hub) | 112000 |
| 3 | 1.93 | 240 | 800 | 25x23 | 2.4 | xps3-sandwich | 10 | 31.4 | 6.34 | 18.7 % | 6.1 | 1.6 | 25.1 (discs) | 112000 |
| 4 | 1.93 | 240 | 800 | 25x23 | 2.0 | xps3-sandwich | 12 | 26.2 | 5.48 | 19.3 % | 6.2 | 1.6 | 25.6 (hub) | 112000 |
| 5 | 1.92 | 240 | 800 | 25x23 | 2.2 | xps3-sandwich | 12 | 26.2 | 5.80 | 19.2 % | 6.2 | 1.6 | 25.6 (hub) | 112000 |
| 6 | 1.91 | 240 | 700 | 25x23 | 2.0 | xps3-sandwich | 10 | 31.4 | 5.73 | 18.3 % | 6.5 | 1.7 | 26.6 (hub) | 112000 |
| 7 | 1.90 | 240 | 800 | 25x23 | 2.4 | xps3-sandwich | 12 | 26.2 | 6.15 | 19.1 % | 6.2 | 1.6 | 25.1 (discs) | 112000 |
| 8 | 1.90 | 240 | 800 | 30x28 | 2.0 | xps5-sandwich | 10 | 31.4 | 7.24 | 18.4 % | 6.0 | 1.6 | 25.6 (hub) | 112000 |
| 9 | 1.90 | 240 | 700 | 25x23 | 2.2 | xps3-sandwich | 10 | 31.4 | 6.06 | 18.2 % | 6.5 | 1.7 | 26.6 (hub) | 112000 |
| 10 | 1.90 | 240 | 700 | 25x23 | 2.0 | xps3-sandwich | 12 | 26.2 | 5.51 | 18.7 % | 6.6 | 1.6 | 26.6 (hub) | 112000 |
| 11 | 1.88 | 240 | 700 | 25x23 | 2.4 | xps3-sandwich | 10 | 31.4 | 6.42 | 18.1 % | 6.5 | 1.7 | 25.1 (discs) | 112000 |
| 12 | 1.88 | 240 | 700 | 25x23 | 2.2 | xps3-sandwich | 12 | 26.2 | 5.84 | 18.6 % | 6.6 | 1.6 | 26.6 (hub) | 112000 |
| 13 | 1.88 | 240 | 800 | 30x28 | 2.0 | xps5-storm | 10 | 31.4 | 7.65 | 18.3 % | 6.0 | 1.6 | 25.6 (hub) | 112000 |
| 14 | 1.88 | 240 | 800 | 30x28 | 2.2 | xps5-sandwich | 10 | 31.4 | 7.68 | 18.3 % | 6.0 | 1.6 | 25.6 (hub) | 112000 |
| 15 | 1.87 | 240 | 800 | 25x23 | 1.8 | xps3-sandwich | 10 | 31.4 | 5.37 | 18.2 % | 6.2 | 1.6 | 25.6 (hub) | 112000 |

## Sensitivity around the best design (one variable at a time)

| Variable | Value | Score | vs best |
|---|---|---|---|
| D (mm) | 100 | 0.61 | -69 % (fails survival, operating loads) |
| D (mm) | 140 | 1.01 | -48 % (fails survival) |
| D (mm) | 180 | 1.40 | -28 % |
| D (mm) | 220 | 1.78 | -9 % |
| D (mm) | 260 | 2.14 | +9 % (fails Reynolds, survival) |
| D (mm) | 300 | 2.48 | +27 % (fails Reynolds, survival) |
| D (mm) | 340 | 2.81 | +44 % (fails Reynolds, survival, operating loads) |
| D (mm) | 380 | 3.13 | +60 % (fails Reynolds, survival, operating loads) |
| Neck (mm) | 0 | 1.04 | -47 % |
| Neck (mm) | 100 | 1.23 | -37 % |
| Neck (mm) | 200 | 1.40 | -28 % |
| Neck (mm) | 300 | 1.55 | -21 % |
| Neck (mm) | 400 | 1.67 | -15 % |
| Neck (mm) | 500 | 1.77 | -10 % |
| Neck (mm) | 600 | 1.85 | -6 % |
| Neck (mm) | 700 | 1.91 | -2 % |
| Neck (mm) | 800 | 1.96 | +0 % |
| Disc ratio | 1 | 1.53 | -22 % |
| Disc ratio | 1.2 | 1.61 | -18 % |
| Disc ratio | 1.4 | 1.70 | -13 % |
| Disc ratio | 1.6 | 1.79 | -9 % |
| Disc ratio | 1.8 | 1.87 | -4 % |
| Disc ratio | 2 | 1.96 | +0 % |
| Disc ratio | 2.2 | 1.95 | -1 % |
| Disc ratio | 2.4 | 1.93 | -1 % |
| Pulley teeth | 10 | 1.96 | +0 % |
| Pulley teeth | 12 | 1.93 | -1 % |
| Pulley teeth | 16 | 1.81 | -8 % (fails operating loads) |
| Pulley teeth | 20 | 1.62 | -17 % (fails operating loads) |
| Pulley teeth | 24 | 1.37 | -30 % (fails operating loads) |
| Shell | xps2-single | 2.03 | +4 % (fails survival) |
| Shell | xps3-single | 2.00 | +2 % (fails survival) |
| Shell | xps3-sandwich | 1.96 | +0 % |
| Shell | xps5-sandwich | 1.90 | -3 % |
| Shell | xps5-storm | 1.88 | -4 % |

Best: shell xps3-sandwich. Full report for it follows.

# Lantern calculator report

Tube 240 mm x 1000 mm, neck 800 mm (25x23 mm carbon), end discs 480 mm, shell 0.211 kg/m^2 (sandwich, 3 mm core), survival requirement 25 m/s

Constraint check: all pass

## Operating summary

- Cut-in (starts and produces >10 mW): 1.6 m/s with kick-start
- Tracking: 2-7 m/s; power-capped at 7.45 W up to 8.0 m/s; braked above that
- Survives (parked, braked) up to **25.6 m/s**, limited by the hub. Requirement: 25 m/s. Per part: neck 28, skin 32, wall 37, discs 35, hub 26
- Worst while swinging: neck 44%, neck fatigue 85%, skin 34%, voltage 32%, generator heat 53%

## Masses (kg)

| Part | Mass |
|---|---|
| Tube shell incl. rings and seams | 0.179 |
| End discs, each | 0.038 |
| Bottom spider | 0.015 |
| Neck tube | 0.093 |
| Hub, axle, carriage, belt arc | 0.150 |
| **Total swinging mass** | **0.514** |

## Inertia about the hinge (kg m^2)

| Part | Inertia |
|---|---|
| shell | 0.3176 |
| discs | 0.1492 |
| spider | 0.0096 |
| neck | 0.0199 |
| hub | 0.0007 |
| generator | 0.0592 |
| Structural total | 0.5563 |
| Air moving with the tube | 0.0983 |
| **Total** | **0.6546** |
| Mass ratio (structural / displaced air) | 5.66 |

- Gear ratio: 31.4:1 (100 mm arc to 10-tooth GT2 pulley)
- Mode-shape factor gamma: 1.244
- Effective length after end losses: 1.000 m
- Gravity (destabilising) stiffness: 3.74 N m/rad

## Tuning

Two opposing springs, each 18.64 N/mm.

| Wind (m/s) | Tune f_n (Hz) | Stiffness (N m/rad) | Carriage below hinge (mm) |
|---|---|---|---|
| 2.0 | 1.52 | 63.1 | 41.1 |
| 3.0 | 2.27 | 137.2 | 60.7 |
| 4.0 | 3.03 | 241.0 | 80.4 |
| 4.5 | 3.41 | 304.1 | 90.3 |
| 5.0 | 3.79 | 374.5 | 100.2 |
| 6.0 | 4.55 | 537.7 | 120.1 |
| 7.0 | 5.30 | 730.5 | 140.0 |

Carriage moves about 19.8 mm per 1 m/s between 4 and 6 m/s.

## Operating points while tracking (model central case)

| Wind | Re | Swing f (Hz) | Wind power (W) | Mech (W) | Elec (W) | Elec low case (W) | Mech eff | Swing (deg) | Peak torque (N m) | Gen zeta | Parasitic zeta | Circuit R (ohm) | Copper eff | EMF peak (V) | Gen peak rpm | Top accel (g) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2.0 | 32000 | 1.67 | 1.2 | 0.14 | 0.11 | 0.06 | 12.0 % | 4.7 | 0.33 | 0.033 | 0.0219 | 372 | 97 % | 10.2 | 257 | 1.6 |
| 3.0 | 48000 | 2.50 | 4.0 | 0.67 | 0.53 | 0.26 | 16.9 % | 5.7 | 0.85 | 0.031 | 0.0109 | 263 | 95 % | 18.8 | 472 | 4.5 |
| 4.5 | 72000 | 3.75 | 13.4 | 2.54 | 1.96 | 0.98 | 19.0 % | 6.2 | 2.01 | 0.030 | 0.0073 | 179 | 93 % | 30.2 | 759 | 10.9 |
| 6.0 | 96000 | 5.00 | 31.8 | 6.27 | 4.71 | 2.35 | 19.7 % | 6.3 | 3.63 | 0.030 | 0.0061 | 135 | 91 % | 41.2 | 1035 | 19.9 |
| 7.0 | 112000 | 5.83 | 50.4 | 10.08 | 7.45 | 3.73 | 20.0 % | 6.3 | 4.97 | 0.030 | 0.0057 | 116 | 90 % | 48.4 | 1216 | 27.3 |

At 4.5 m/s: tube swings +/-86 mm at the bottom, +/-140 mm mid-height, +/-194 mm at the top; generator swings +/-193 deg. Friction: bushings 0.097 N m, generator drag 0.126 N m (at the hinge).

## Wind envelope, 1-40 m/s

Utilisation = load / allowable for each part (over 100% fails). Neck, skin and hub combine drag with the swing's inertia; wall is ovalling of the shell under wind pressure; discs is gust lift on the end discs. Parked modes use drag coefficient 1.2; swinging modes 2.0.

| Wind (m/s) | Mode | Re | Flow | Tuned to (Hz) | Carriage (mm) | Swing (±°) | Elec (W) | Top accel (g) | EMF (V) | Neck | Neck fatigue | Skin | Wall | Discs | Hub | Worst |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | idle | 16,000 | tested | 5.30 | 140 | 0.0 | 0.00 | 0.0 | 0 | 0% | 0% | 0% | 0% | 0% | 0% | hub 0% |
| 2 | tracking | 32,000 | tested | 1.52 | 41 | 4.7 | 0.11 | 1.6 | 10 | 3% | 5% | 2% | 0% | 0% | 1% | voltage 7% |
| 2.5 | tracking | 40,000 | tested | 1.89 | 51 | 5.4 | 0.28 | 3.0 | 15 | 5% | 9% | 4% | 0% | 1% | 2% | voltage 10% |
| 3 | tracking | 48,000 | tested | 2.27 | 61 | 5.7 | 0.53 | 4.5 | 19 | 7% | 14% | 6% | 1% | 1% | 2% | neck fatigue 14% |
| 4 | tracking | 64,000 | tested | 3.03 | 80 | 6.1 | 1.35 | 8.5 | 26 | 14% | 26% | 11% | 1% | 1% | 4% | neck fatigue 26% |
| 4.5 | tracking | 72,000 | tested | 3.41 | 90 | 6.2 | 1.96 | 10.9 | 30 | 18% | 34% | 14% | 1% | 2% | 5% | neck fatigue 34% |
| 5 | tracking | 80,000 | tested | 3.79 | 100 | 6.2 | 2.71 | 13.6 | 34 | 22% | 42% | 17% | 2% | 2% | 6% | neck fatigue 42% |
| 6 | tracking | 96,000 | tested | 4.55 | 120 | 6.3 | 4.71 | 19.9 | 41 | 32% | 62% | 25% | 3% | 3% | 9% | neck fatigue 62% |
| 7 | tracking | 112,000 | tested | 5.30 | 140 | 6.3 | 7.45 | 27.3 | 48 | 44% | 85% | 34% | 4% | 4% | 12% | neck fatigue 85% |
| 7.5 | power-capped | 120,000 | tested | 5.30 | 140 | 4.7 | 7.45 | 23.3 | 39 | 38% | 73% | 30% | 4% | 5% | 14% | neck fatigue 73% |
| 8 | braked | 128,000 | beyond tested | 5.30 | 140 | 0.4 | 0.00 | 2.2 | 0 | 9% | 7% | 7% | 5% | 5% | 10% | hub 10% |
| 9 | braked | 144,000 | beyond tested | 5.30 | 140 | 0.0 | 0.00 | 0.0 | 0 | 11% | 0% | 8% | 6% | 7% | 12% | hub 12% |
| 10 | braked | 160,000 | beyond tested | 5.30 | 140 | 0.0 | 0.00 | 0.0 | 0 | 13% | 0% | 10% | 7% | 8% | 15% | hub 15% |
| 12 | braked | 192,000 | beyond tested | 5.30 | 140 | 0.0 | 0.00 | 0.0 | 0 | 19% | 0% | 14% | 11% | 12% | 22% | hub 22% |
| 15 | braked | 240,000 | drag crisis | 5.30 | 140 | 0.0 | 0.00 | 0.0 | 0 | 30% | 0% | 22% | 17% | 18% | 34% | hub 34% |
| 20 | braked | 320,000 | drag crisis | 5.30 | 140 | 0.0 | 0.00 | 0.0 | 0 | 53% | 0% | 39% | 29% | 32% | 61% | hub 61% |
| 25 | braked | 400,000 | drag crisis | 5.30 | 140 | 0.0 | 0.00 | 0.0 | 0 | 82% | 0% | 61% | 46% | 51% | 96% | hub 96% |
| 30 | braked | 480,000 | drag crisis | 5.30 | 140 | 0.0 | 0.00 | 0.0 | 0 | 119% | 0% | 88% | 66% | 73% | 138% | hub 138% **FAIL** |
| 35 | braked | 560,000 | drag crisis | 5.30 | 140 | 0.0 | 0.00 | 0.0 | 0 | 161% | 0% | 119% | 90% | 99% | 187% | hub 187% **FAIL** |
| 40 | braked | 640,000 | drag crisis | 5.30 | 140 | 0.0 | 0.00 | 0.0 | 0 | 211% | 0% | 156% | 118% | 129% | 245% | hub 245% **FAIL** |

## Structure at the survival requirement (25 m/s, parked and braked)

- Drag on the tube 110 N; bending moment at tube base 55 N m, at the hinge 143 N m (hub built for 150)
- Neck stress 329 MPa (allowable 400); skin stress at tube base 24.4 MPa (allowable 40)
- Shell ovalling 2.76 N m/m against a wall capacity of 6.00 N m/m
- End-disc gust utilisation 51%
- Hinge bushing load 958 N each
- Post base moment with hinge at 3 m: 534 N m (size the post to your local wind code)
- Swing cycles per year at 30 % duty: 3.2e+07

## Annual energy (very rough)

Rayleigh wind at hub height, power curve from the envelope above (tracking, then capped at 7.45 W, braked from 8.0 m/s), 50 % of swinging time assumed locked on. Low case = 0.5 x central.

| Site mean wind | Low (kWh/yr) | Central (kWh/yr) |
|---|---|---|
| 3.0 m/s | 2.2 | 4.4 |
| 3.5 m/s | 3.2 | 6.3 |
| 4.5 m/s | 4.5 | 9.0 |
| 5.5 m/s | 4.9 | 9.8 |

