# Lantern sweep: ranked by electrical power at 4.5 m/s, survival requirement 25 m/s

28800 combinations: D 0.1-0.4 m, neck 0.0-0.8 m, disc ratio 1.0-2.4, shells xps2-single, xps3-single, xps3-sandwich, xps5-sandwich, xps5-storm, pulley teeth [10, 12, 16, 20, 24], neck tube sized automatically.  
5745 pass all limits. Rejected (a design can fail several): Reynolds 14400, operating loads 10114, survival 18030

| Rank | Score (W) | D (mm) | Neck (mm) | Neck tube | Disc ratio | Shell | Teeth | Gear | Mass ratio | Mech eff 4.5 | Swing 4.5 (deg) | Cut-in | Survives to | Re at U_max |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1.95 | 240 | 800 | 35x32 | 2.0 | xps3-sandwich | 10 | 31.4 | 5.88 | 18.9 % | 6.1 | 1.6 | 25.6 (hub) | 112000 |
| 2 | 1.94 | 240 | 800 | 35x32 | 2.2 | xps3-sandwich | 10 | 31.4 | 6.20 | 18.8 % | 6.1 | 1.6 | 25.6 (hub) | 112000 |
| 3 | 1.92 | 240 | 800 | 35x32 | 2.4 | xps3-sandwich | 10 | 31.4 | 6.56 | 18.7 % | 6.1 | 1.6 | 25.1 (discs) | 112000 |
| 4 | 1.92 | 240 | 800 | 35x32 | 2.0 | xps3-sandwich | 12 | 26.2 | 5.70 | 19.2 % | 6.2 | 1.6 | 25.6 (hub) | 112000 |
| 5 | 1.91 | 240 | 800 | 35x32 | 2.2 | xps3-sandwich | 12 | 26.2 | 6.02 | 19.1 % | 6.2 | 1.6 | 25.6 (hub) | 112000 |
| 6 | 1.91 | 240 | 700 | 30x28 | 2.0 | xps3-sandwich | 10 | 31.4 | 5.76 | 18.3 % | 6.5 | 1.7 | 26.6 (hub) | 112000 |
| 7 | 1.90 | 240 | 700 | 30x28 | 2.2 | xps3-sandwich | 10 | 31.4 | 6.09 | 18.2 % | 6.5 | 1.7 | 26.6 (hub) | 112000 |
| 8 | 1.90 | 240 | 800 | 35x32 | 2.4 | xps3-sandwich | 12 | 26.2 | 6.37 | 19.0 % | 6.2 | 1.6 | 25.1 (discs) | 112000 |
| 9 | 1.89 | 240 | 700 | 30x28 | 2.0 | xps3-sandwich | 12 | 26.2 | 5.55 | 18.7 % | 6.6 | 1.6 | 26.6 (hub) | 112000 |
| 10 | 1.89 | 240 | 800 | 35x32 | 2.0 | xps5-sandwich | 10 | 31.4 | 7.42 | 18.4 % | 6.0 | 1.6 | 25.6 (hub) | 112000 |
| 11 | 1.88 | 240 | 700 | 30x28 | 2.4 | xps3-sandwich | 10 | 31.4 | 6.45 | 18.1 % | 6.5 | 1.7 | 25.1 (discs) | 112000 |
| 12 | 1.88 | 240 | 700 | 30x28 | 2.2 | xps3-sandwich | 12 | 26.2 | 5.87 | 18.6 % | 6.6 | 1.6 | 26.6 (hub) | 112000 |
| 13 | 1.88 | 240 | 800 | 35x32 | 2.0 | xps5-storm | 10 | 31.4 | 7.83 | 18.2 % | 6.0 | 1.6 | 25.6 (hub) | 112000 |
| 14 | 1.87 | 240 | 800 | 35x32 | 2.2 | xps5-sandwich | 10 | 31.4 | 7.86 | 18.2 % | 6.0 | 1.6 | 25.6 (hub) | 112000 |
| 15 | 1.87 | 240 | 800 | 30x28 | 1.8 | xps3-sandwich | 10 | 31.4 | 5.41 | 18.2 % | 6.2 | 1.6 | 25.6 (hub) | 112000 |

## Sensitivity around the best design (one variable at a time)

| Variable | Value | Score | vs best |
|---|---|---|---|
| D (mm) | 100 | 0.60 | -69 % (fails survival, operating loads) |
| D (mm) | 140 | 1.00 | -49 % (fails survival) |
| D (mm) | 180 | 1.39 | -29 % |
| D (mm) | 220 | 1.77 | -9 % |
| D (mm) | 260 | 2.13 | +10 % (fails Reynolds, survival) |
| D (mm) | 300 | 2.48 | +27 % (fails Reynolds, survival) |
| D (mm) | 340 | 2.81 | +44 % (fails Reynolds, survival, operating loads) |
| D (mm) | 380 | 3.13 | +61 % (fails Reynolds, survival, operating loads) |
| Neck (mm) | 0 | 1.04 | -46 % |
| Neck (mm) | 100 | 1.23 | -37 % |
| Neck (mm) | 200 | 1.40 | -28 % |
| Neck (mm) | 300 | 1.55 | -21 % |
| Neck (mm) | 400 | 1.67 | -14 % |
| Neck (mm) | 500 | 1.77 | -9 % |
| Neck (mm) | 600 | 1.85 | -5 % |
| Neck (mm) | 700 | 1.91 | -2 % |
| Neck (mm) | 800 | 1.95 | +0 % |
| Disc ratio | 1 | 1.53 | -21 % |
| Disc ratio | 1.2 | 1.61 | -17 % |
| Disc ratio | 1.4 | 1.70 | -13 % |
| Disc ratio | 1.6 | 1.79 | -8 % |
| Disc ratio | 1.8 | 1.87 | -4 % |
| Disc ratio | 2 | 1.95 | +0 % |
| Disc ratio | 2.2 | 1.94 | -1 % |
| Disc ratio | 2.4 | 1.92 | -1 % |
| Pulley teeth | 10 | 1.95 | +0 % |
| Pulley teeth | 12 | 1.92 | -1 % |
| Pulley teeth | 16 | 1.80 | -8 % (fails operating loads) |
| Pulley teeth | 20 | 1.61 | -17 % (fails operating loads) |
| Pulley teeth | 24 | 1.37 | -30 % (fails operating loads) |
| Shell | xps2-single | 2.03 | +4 % (fails survival) |
| Shell | xps3-single | 2.00 | +2 % (fails survival) |
| Shell | xps3-sandwich | 1.95 | +0 % |
| Shell | xps5-sandwich | 1.89 | -3 % |
| Shell | xps5-storm | 1.88 | -4 % |

Best: shell xps3-sandwich. Full report for it follows.

# Lantern calculator report

Tube 240 mm x 1000 mm, neck 800 mm (35x32 mm carbon), end discs 480 mm, shell 0.211 kg/m^2 (sandwich, 3 mm core), survival requirement 25 m/s

Constraint check: all pass

## Operating summary

- Cut-in (starts and produces >10 mW): 1.6 m/s with kick-start
- Tracking: 2-7 m/s; power-capped at 7.42 W up to 8.0 m/s; braked above that
- Survives (parked, braked) up to **25.6 m/s**, limited by the hub. Requirement: 25 m/s. Per part: neck 47, skin 32, wall 37, discs 35, hub 26
- Worst while swinging: neck 16%, neck fatigue 30%, skin 34%, voltage 32%, generator heat 53%, neck mode 67%
- Neck-tube bending mode about 14.9 Hz (swing must stay below 9.9 Hz, reached at 11.9 m/s)

## Masses (kg)

| Part | Mass |
|---|---|
| Tube shell incl. rings and seams | 0.179 |
| End discs, each | 0.038 |
| Bottom spider | 0.015 |
| Neck tube | 0.196 |
| Hub, axle, carriage, belt arc | 0.150 |
| **Total swinging mass** | **0.616** |

## Inertia about the hinge (kg m^2)

| Part | Inertia |
|---|---|
| shell | 0.3176 |
| discs | 0.1492 |
| spider | 0.0096 |
| neck | 0.0418 |
| hub | 0.0007 |
| generator | 0.0592 |
| Structural total | 0.5781 |
| Air moving with the tube | 0.0983 |
| **Total** | **0.6764** |
| Mass ratio (structural / displaced air) | 5.88 |

- Gear ratio: 31.4:1 (100 mm arc to 10-tooth GT2 pulley)
- Mode-shape factor gamma: 1.244
- Effective length after end losses: 1.000 m
- Gravity (destabilising) stiffness: 4.14 N m/rad

## Tuning

Two opposing springs, each 19.26 N/mm.

| Wind (m/s) | Tune f_n (Hz) | Stiffness (N m/rad) | Carriage below hinge (mm) |
|---|---|---|---|
| 2.0 | 1.52 | 65.4 | 41.2 |
| 3.0 | 2.27 | 142.1 | 60.7 |
| 4.0 | 3.03 | 249.4 | 80.5 |
| 4.5 | 3.41 | 314.5 | 90.3 |
| 5.0 | 3.79 | 387.3 | 100.3 |
| 6.0 | 4.55 | 555.9 | 120.1 |
| 7.0 | 5.30 | 755.1 | 140.0 |

Carriage moves about 19.8 mm per 1 m/s between 4 and 6 m/s.

## Operating points while tracking (model central case)

| Wind | Re | Swing f (Hz) | Wind power (W) | Mech (W) | Elec (W) | Elec low case (W) | Mech eff | Swing (deg) | Peak torque (N m) | Gen zeta | Parasitic zeta | Circuit R (ohm) | Copper eff | EMF peak (V) | Gen peak rpm | Top accel (g) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2.0 | 32000 | 1.67 | 1.2 | 0.14 | 0.11 | 0.06 | 11.9 % | 4.7 | 0.33 | 0.032 | 0.0214 | 371 | 97 % | 10.2 | 256 | 1.6 |
| 3.0 | 48000 | 2.50 | 4.0 | 0.67 | 0.52 | 0.26 | 16.8 % | 5.7 | 0.85 | 0.030 | 0.0107 | 263 | 95 % | 18.7 | 470 | 4.5 |
| 4.5 | 72000 | 3.75 | 13.4 | 2.53 | 1.95 | 0.97 | 18.9 % | 6.1 | 2.01 | 0.029 | 0.0071 | 179 | 93 % | 30.1 | 757 | 10.9 |
| 6.0 | 96000 | 5.00 | 31.8 | 6.24 | 4.69 | 2.34 | 19.6 % | 6.3 | 3.63 | 0.029 | 0.0060 | 135 | 91 % | 41.1 | 1032 | 19.8 |
| 7.0 | 112000 | 5.83 | 50.4 | 10.03 | 7.42 | 3.71 | 19.9 % | 6.3 | 4.96 | 0.029 | 0.0056 | 116 | 90 % | 48.3 | 1213 | 27.2 |

At 4.5 m/s: tube swings +/-86 mm at the bottom, +/-140 mm mid-height, +/-193 mm at the top; generator swings +/-193 deg. Friction: bushings 0.098 N m, generator drag 0.126 N m (at the hinge).

## Wind envelope, 1-40 m/s

Utilisation = load / allowable for each part (over 100% fails). Neck, skin and hub combine drag with the swing's inertia; wall is ovalling of the shell under wind pressure; discs is gust lift on the end discs. Parked modes use drag coefficient 1.2; swinging modes 2.0.

| Wind (m/s) | Mode | Re | Flow | Tuned to (Hz) | Carriage (mm) | Swing (±°) | Elec (W) | Top accel (g) | EMF (V) | Neck | Neck fatigue | Skin | Wall | Discs | Hub | Worst |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | idle | 16,000 | tested | 5.30 | 140 | 0.0 | 0.00 | 0.0 | 0 | 0% | 0% | 0% | 0% | 0% | 0% | hub 0% |
| 2 | tracking | 32,000 | tested | 1.52 | 41 | 4.7 | 0.11 | 1.6 | 10 | 1% | 2% | 2% | 0% | 0% | 1% | neck mode 17% |
| 2.5 | tracking | 40,000 | tested | 1.89 | 51 | 5.4 | 0.27 | 2.9 | 15 | 2% | 3% | 4% | 0% | 1% | 2% | neck mode 21% |
| 3 | tracking | 48,000 | tested | 2.27 | 61 | 5.7 | 0.52 | 4.5 | 19 | 3% | 5% | 6% | 1% | 1% | 2% | neck mode 25% |
| 4 | tracking | 64,000 | tested | 3.03 | 80 | 6.0 | 1.35 | 8.5 | 26 | 5% | 9% | 11% | 1% | 1% | 4% | neck mode 34% |
| 4.5 | tracking | 72,000 | tested | 3.41 | 90 | 6.1 | 1.95 | 10.9 | 30 | 6% | 12% | 14% | 1% | 2% | 5% | neck mode 38% |
| 5 | tracking | 80,000 | tested | 3.79 | 100 | 6.2 | 2.70 | 13.6 | 34 | 8% | 15% | 17% | 2% | 2% | 6% | neck mode 42% |
| 6 | tracking | 96,000 | tested | 4.55 | 120 | 6.3 | 4.69 | 19.8 | 41 | 11% | 22% | 25% | 3% | 3% | 9% | neck mode 50% |
| 7 | tracking | 112,000 | tested | 5.30 | 140 | 6.3 | 7.42 | 27.2 | 48 | 16% | 30% | 34% | 4% | 4% | 12% | neck mode 59% |
| 7.5 | power-capped | 120,000 | tested | 5.30 | 140 | 4.7 | 7.42 | 23.3 | 39 | 14% | 26% | 29% | 4% | 5% | 14% | neck mode 63% |
| 8 | braked | 128,000 | beyond tested | 5.30 | 140 | 0.4 | 0.00 | 2.2 | 0 | 3% | 2% | 7% | 5% | 5% | 10% | hub 10% |
| 9 | braked | 144,000 | beyond tested | 5.30 | 140 | 0.0 | 0.00 | 0.0 | 0 | 4% | 0% | 8% | 6% | 7% | 12% | hub 12% |
| 10 | braked | 160,000 | beyond tested | 5.30 | 140 | 0.0 | 0.00 | 0.0 | 0 | 5% | 0% | 10% | 7% | 8% | 15% | hub 15% |
| 12 | braked | 192,000 | beyond tested | 5.30 | 140 | 0.0 | 0.00 | 0.0 | 0 | 7% | 0% | 14% | 11% | 12% | 22% | hub 22% |
| 15 | braked | 240,000 | drag crisis | 5.30 | 140 | 0.0 | 0.00 | 0.0 | 0 | 10% | 0% | 22% | 17% | 18% | 34% | hub 34% |
| 20 | braked | 320,000 | drag crisis | 5.30 | 140 | 0.0 | 0.00 | 0.0 | 0 | 18% | 0% | 39% | 29% | 32% | 61% | hub 61% |
| 25 | braked | 400,000 | drag crisis | 5.30 | 140 | 0.0 | 0.00 | 0.0 | 0 | 28% | 0% | 61% | 46% | 51% | 96% | hub 96% |
| 30 | braked | 480,000 | drag crisis | 5.30 | 140 | 0.0 | 0.00 | 0.0 | 0 | 41% | 0% | 88% | 66% | 73% | 138% | hub 138% **FAIL** |
| 35 | braked | 560,000 | drag crisis | 5.30 | 140 | 0.0 | 0.00 | 0.0 | 0 | 55% | 0% | 119% | 90% | 99% | 187% | hub 187% **FAIL** |
| 40 | braked | 640,000 | drag crisis | 5.30 | 140 | 0.0 | 0.00 | 0.0 | 0 | 72% | 0% | 156% | 118% | 129% | 245% | hub 245% **FAIL** |

## Power from 1 to 40 m/s

Model potential = output if the tube stayed tuned and locked on with nothing failing (not achievable). Within limits = the most it can deliver with every part within limits, retuning as far as the neck's bending mode allows. As designed = the default control.

- Neck-tube bending mode about 14.9 Hz, so the swing must stay below 9.9 Hz: retuning is possible up to 11.9 m/s
- As designed: generates 1.6-8.0 m/s, peak 7.42 W, braked above
- Kept generating within every limit: generates 1.8-11.0 m/s, peak 28.05 W at 11 m/s; nothing above 12.5 m/s
- Yearly energy, central case (kWh): 3.5 m/s site: as designed 6.3, within limits 7.6; 4.5 m/s site: as designed 9.0, within limits 15.1; 5.5 m/s site: as designed 9.8, within limits 22.3; 6.5 m/s site: as designed 9.4, within limits 27.0

| Wind (m/s) | Re | Flow | Wind through tube (W) | Model potential (W) | Within limits (W) | Within limits: what governs | As designed (W) | As designed: mode |
|---|---|---|---|---|---|---|---|---|
| 1 | 16,000 | tested | 0.1 | 0.00 | 0.00 | idle | 0.00 | idle |
| 2 | 32,000 | tested | 1.2 | 0.11 | 0.12 | unconstrained | 0.11 | tracking |
| 3 | 48,000 | tested | 4.0 | 0.52 | 0.53 | unconstrained | 0.52 | tracking |
| 4 | 64,000 | tested | 9.4 | 1.35 | 1.36 | unconstrained | 1.35 | tracking |
| 4.5 | 72,000 | tested | 13.4 | 1.95 | 1.97 | unconstrained | 1.95 | tracking |
| 5 | 80,000 | tested | 18.4 | 2.70 | 2.72 | unconstrained | 2.70 | tracking |
| 6 | 96,000 | tested | 31.8 | 4.69 | 4.73 | unconstrained | 4.69 | tracking |
| 7 | 112,000 | tested | 50.4 | 7.42 | 7.50 | unconstrained | 7.42 | tracking |
| 8 | 128,000 | beyond tested | 75.3 | 10.98 | 11.12 | unconstrained | 0.00 | braked |
| 9 | 144,000 | beyond tested | 107.2 | 15.46 | 15.68 | unconstrained | 0.00 | braked |
| 10 | 160,000 | beyond tested | 147.0 | 20.94 | 21.28 | unconstrained | 0.00 | braked |
| 11 | 176,000 | beyond tested | 195.7 | 27.47 | 28.05 | unconstrained | 0.00 | braked |
| 12 | 192,000 | beyond tested | 254.0 | 35.12 | 0.00 | braked (generator heat) | 0.00 | braked |
| 13 | 208,000 | drag crisis | 323.0 | 43.93 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 14 | 224,000 | drag crisis | 403.4 | 53.95 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 15 | 240,000 | drag crisis | 496.1 | 65.21 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 17.5 | 280,000 | drag crisis | 787.8 | 98.88 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 20 | 320,000 | drag crisis | 1,176.0 | 140.50 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 25 | 400,000 | drag crisis | 2,296.9 | 246.32 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 30 | 480,000 | drag crisis | 3,969.0 | 376.66 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 35 | 560,000 | drag crisis | 6,302.6 | 520.05 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 40 | 640,000 | drag crisis | 9,408.0 | 659.51 | 0.00 | braked (drag crisis) | 0.00 | braked |

## Structure at the survival requirement (25 m/s, parked and braked)

- Drag on the tube 110 N; bending moment at tube base 55 N m, at the hinge 143 N m (hub built for 150)
- Neck stress 113 MPa (allowable 400); skin stress at tube base 24.4 MPa (allowable 40)
- Shell ovalling 2.76 N m/m against a wall capacity of 6.00 N m/m
- End-disc gust utilisation 51%
- Hinge bushing load 959 N each
- Post base moment with hinge at 3 m: 534 N m (size the post to your local wind code)
- Swing cycles per year at 30 % duty: 3.2e+07

## Annual energy (very rough)

Rayleigh wind at hub height, power curve from the envelope above (tracking, then capped at 7.42 W, braked from 8.0 m/s), 50 % of swinging time assumed locked on. Low case = 0.5 x central.

| Site mean wind | Low (kWh/yr) | Central (kWh/yr) |
|---|---|---|
| 3.0 m/s | 2.2 | 4.4 |
| 3.5 m/s | 3.1 | 6.3 |
| 4.5 m/s | 4.5 | 9.0 |
| 5.5 m/s | 4.9 | 9.8 |

