# Lantern sweep: ranked by electrical power at 4.5 m/s, survival requirement 40 m/s

28800 combinations: D 0.1-0.4 m, neck 0.0-0.8 m, disc ratio 1.0-2.4, shells xps2-single, xps3-single, xps3-sandwich, xps5-sandwich, xps5-storm, pulley teeth [10, 12, 16, 20, 24], neck tube sized automatically.  
1767 pass all limits. Rejected (a design can fail several): Reynolds 14400, operating loads 10681, survival 26490

| Rank | Score (W) | D (mm) | Neck (mm) | Neck tube | Disc ratio | Shell | Teeth | Gear | Mass ratio | Mech eff 4.5 | Swing 4.5 (deg) | Cut-in | Survives to | Re at U_max |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1.81 | 240 | 700 | 35x32 | 2.0 | xps5-storm | 10 | 31.4 | 8.19 | 17.4 % | 6.3 | 1.7 | 40.7 (hub) | 112000 |
| 2 | 1.80 | 240 | 700 | 35x32 | 2.0 | xps5-storm | 12 | 26.2 | 7.98 | 17.8 % | 6.4 | 1.6 | 40.7 (hub) | 112000 |
| 3 | 1.75 | 240 | 600 | 35x32 | 2.0 | xps5-storm | 10 | 31.4 | 8.26 | 16.7 % | 6.7 | 1.8 | 42.5 (hub) | 112000 |
| 4 | 1.75 | 240 | 600 | 35x32 | 2.0 | xps5-storm | 12 | 26.2 | 8.01 | 17.1 % | 6.8 | 1.6 | 42.5 (hub) | 112000 |
| 5 | 1.74 | 240 | 700 | 35x32 | 1.8 | xps5-storm | 10 | 31.4 | 7.79 | 16.7 % | 6.4 | 1.7 | 40.7 (hub) | 112000 |
| 6 | 1.73 | 240 | 700 | 35x32 | 1.8 | xps5-storm | 12 | 26.2 | 7.58 | 17.1 % | 6.4 | 1.6 | 40.7 (hub) | 112000 |
| 7 | 1.70 | 240 | 600 | 35x32 | 2.0 | xps5-storm | 16 | 19.6 | 7.76 | 17.6 % | 6.9 | 1.6 | 42.5 (hub) | 112000 |
| 8 | 1.69 | 240 | 500 | 35x32 | 2.0 | xps5-storm | 12 | 26.2 | 8.09 | 16.3 % | 7.2 | 1.7 | 44.5 (hub) | 112000 |
| 9 | 1.68 | 240 | 600 | 35x32 | 1.8 | xps5-storm | 10 | 31.4 | 7.85 | 16.0 % | 6.7 | 1.8 | 42.5 (hub) | 112000 |
| 10 | 1.68 | 240 | 600 | 35x32 | 1.8 | xps5-storm | 12 | 26.2 | 7.60 | 16.4 % | 6.8 | 1.7 | 42.5 (hub) | 112000 |
| 11 | 1.68 | 240 | 500 | 35x32 | 2.0 | xps5-storm | 10 | 31.4 | 8.39 | 15.9 % | 7.1 | 1.8 | 44.5 (hub) | 112000 |
| 12 | 1.68 | 220 | 800 | 35x32 | 2.0 | xps5-storm | 10 | 31.4 | 8.90 | 17.7 % | 5.4 | 1.7 | 40.8 (hub) | 102667 |
| 13 | 1.66 | 240 | 700 | 35x32 | 1.6 | xps5-storm | 10 | 31.4 | 7.44 | 16.0 % | 6.4 | 1.8 | 40.7 (hub) | 112000 |
| 14 | 1.66 | 220 | 800 | 35x32 | 2.2 | xps5-storm | 10 | 31.4 | 9.33 | 17.5 % | 5.4 | 1.7 | 40.8 (hub) | 102667 |
| 15 | 1.66 | 220 | 800 | 35x32 | 2.0 | xps5-storm | 12 | 26.2 | 8.68 | 18.0 % | 5.5 | 1.6 | 40.8 (hub) | 102667 |

## Sensitivity around the best design (one variable at a time)

| Variable | Value | Score | vs best |
|---|---|---|---|
| D (mm) | 100 | 0.50 | -73 % (fails survival) |
| D (mm) | 140 | 0.89 | -51 % |
| D (mm) | 180 | 1.27 | -30 % |
| D (mm) | 220 | 1.63 | -10 % |
| D (mm) | 260 | 1.99 | +10 % (fails Reynolds, survival) |
| D (mm) | 300 | 2.33 | +29 % (fails Reynolds, survival) |
| D (mm) | 340 | 2.66 | +47 % (fails Reynolds, survival) |
| D (mm) | 380 | 2.98 | +64 % (fails Reynolds, survival, operating loads) |
| Neck (mm) | 0 | 0.98 | -46 % |
| Neck (mm) | 100 | 1.16 | -36 % |
| Neck (mm) | 200 | 1.33 | -27 % |
| Neck (mm) | 300 | 1.47 | -19 % |
| Neck (mm) | 400 | 1.59 | -13 % |
| Neck (mm) | 500 | 1.68 | -7 % |
| Neck (mm) | 600 | 1.75 | -3 % |
| Neck (mm) | 700 | 1.81 | +0 % |
| Neck (mm) | 800 | 1.86 | +2 % (fails survival) |
| Disc ratio | 1 | 1.44 | -21 % |
| Disc ratio | 1.2 | 1.50 | -17 % |
| Disc ratio | 1.4 | 1.59 | -13 % |
| Disc ratio | 1.6 | 1.66 | -8 % |
| Disc ratio | 1.8 | 1.74 | -4 % |
| Disc ratio | 2 | 1.81 | +0 % |
| Disc ratio | 2.2 | 1.80 | -1 % (fails survival) |
| Disc ratio | 2.4 | 1.78 | -2 % (fails survival) |
| Pulley teeth | 10 | 1.81 | +0 % |
| Pulley teeth | 12 | 1.80 | -1 % |
| Pulley teeth | 16 | 1.71 | -5 % (fails operating loads) |
| Pulley teeth | 20 | 1.57 | -13 % (fails operating loads) |
| Pulley teeth | 24 | 1.38 | -24 % (fails operating loads) |
| Shell | xps2-single | 1.95 | +8 % (fails survival) |
| Shell | xps3-single | 1.92 | +6 % (fails survival) |
| Shell | xps3-sandwich | 1.88 | +4 % (fails survival) |
| Shell | xps5-sandwich | 1.83 | +1 % (fails survival) |
| Shell | xps5-storm | 1.81 | +0 % |

Best: shell xps5-storm. Full report for it follows.

# Lantern calculator report

Tube 240 mm x 1000 mm, neck 700 mm (35x32 mm carbon), end discs 480 mm, shell 0.315 kg/m^2 (sandwich, 5 mm core), survival requirement 40 m/s

Constraint check: all pass

## Operating summary

- Cut-in (starts and produces >10 mW): 1.7 m/s with kick-start
- Tracking: 2-7 m/s; power-capped at 7.01 W up to 8.0 m/s; braked above that
- Survives (parked, braked) up to **40.7 m/s**, limited by the hub. Requirement: 40 m/s. Per part: neck 49, skin 55, wall 48, discs 45, hub 41
- Worst while swinging: neck 19%, neck fatigue 38%, skin 16%, voltage 33%, generator heat 43%, neck mode 70%
- Neck-tube bending mode about 14.3 Hz (swing must stay below 9.5 Hz, reached at 11.5 m/s)

## Masses (kg)

| Part | Mass |
|---|---|
| Tube shell incl. rings and seams | 0.276 |
| End discs, each | 0.052 |
| Bottom spider | 0.015 |
| Neck tube | 0.171 |
| Hub, axle, carriage, belt arc | 0.300 |
| **Total swinging mass** | **0.865** |

## Inertia about the hinge (kg m^2)

| Part | Inertia |
|---|---|
| shell | 0.4197 |
| discs | 0.1758 |
| spider | 0.0073 |
| neck | 0.0280 |
| hub | 0.0015 |
| generator | 0.0592 |
| Structural total | 0.6915 |
| Air moving with the tube | 0.0844 |
| **Total** | **0.7759** |
| Mass ratio (structural / displaced air) | 8.19 |

- Gear ratio: 31.4:1 (100 mm arc to 10-tooth GT2 pulley)
- Mode-shape factor gamma: 1.253
- Effective length after end losses: 1.000 m
- Gravity (destabilising) stiffness: 5.15 N m/rad

## Tuning

Two opposing springs, each 22.11 N/mm.

| Wind (m/s) | Tune f_n (Hz) | Stiffness (N m/rad) | Carriage below hinge (mm) |
|---|---|---|---|
| 2.0 | 1.52 | 75.5 | 41.3 |
| 3.0 | 2.27 | 163.4 | 60.8 |
| 4.0 | 3.03 | 286.4 | 80.5 |
| 4.5 | 3.41 | 361.2 | 90.4 |
| 5.0 | 3.79 | 444.7 | 100.3 |
| 6.0 | 4.55 | 638.0 | 120.1 |
| 7.0 | 5.30 | 866.6 | 140.0 |

Carriage moves about 19.8 mm per 1 m/s between 4 and 6 m/s.

## Operating points while tracking (model central case)

| Wind | Re | Swing f (Hz) | Wind power (W) | Mech (W) | Elec (W) | Elec low case (W) | Mech eff | Swing (deg) | Peak torque (N m) | Gen zeta | Parasitic zeta | Circuit R (ohm) | Copper eff | EMF peak (V) | Gen peak rpm | Top accel (g) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2.0 | 32000 | 1.67 | 1.2 | 0.11 | 0.09 | 0.05 | 9.8 % | 4.5 | 0.28 | 0.023 | 0.0193 | 419 | 97 % | 9.8 | 247 | 1.5 |
| 3.0 | 48000 | 2.50 | 4.0 | 0.60 | 0.48 | 0.24 | 15.1 % | 5.8 | 0.75 | 0.022 | 0.0094 | 302 | 96 % | 19.0 | 479 | 4.3 |
| 4.5 | 72000 | 3.75 | 13.4 | 2.34 | 1.81 | 0.91 | 17.4 % | 6.3 | 1.80 | 0.021 | 0.0063 | 206 | 94 % | 31.0 | 780 | 10.6 |
| 6.0 | 96000 | 5.00 | 31.8 | 5.79 | 4.41 | 2.20 | 18.2 % | 6.5 | 3.25 | 0.021 | 0.0054 | 156 | 92 % | 42.5 | 1068 | 19.4 |
| 7.0 | 112000 | 5.83 | 50.4 | 9.33 | 7.01 | 3.50 | 18.5 % | 6.6 | 4.45 | 0.021 | 0.0051 | 134 | 91 % | 50.0 | 1257 | 26.6 |

At 4.5 m/s: tube swings +/-78 mm at the bottom, +/-133 mm mid-height, +/-188 mm at the top; generator swings +/-199 deg. Friction: bushings 0.096 N m, generator drag 0.126 N m (at the hinge).

## Wind envelope, 1-40 m/s

Utilisation = load / allowable for each part (over 100% fails). Neck, skin and hub combine drag with the swing's inertia; wall is ovalling of the shell under wind pressure; discs is gust lift on the end discs. Parked modes use drag coefficient 1.2; swinging modes 2.0.

| Wind (m/s) | Mode | Re | Flow | Tuned to (Hz) | Carriage (mm) | Swing (±°) | Elec (W) | Top accel (g) | EMF (V) | Neck | Neck fatigue | Skin | Wall | Discs | Hub | Worst |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | idle | 16,000 | tested | 5.30 | 140 | 0.0 | 0.00 | 0.0 | 0 | 0% | 0% | 0% | 0% | 0% | 0% | hub 0% |
| 2 | tracking | 32,000 | tested | 1.52 | 41 | 4.5 | 0.09 | 1.5 | 10 | 1% | 2% | 1% | 0% | 0% | 0% | neck mode 17% |
| 2.5 | tracking | 40,000 | tested | 1.89 | 51 | 5.4 | 0.24 | 2.8 | 15 | 2% | 4% | 2% | 0% | 0% | 1% | neck mode 22% |
| 3 | tracking | 48,000 | tested | 2.27 | 61 | 5.8 | 0.48 | 4.3 | 19 | 3% | 6% | 3% | 0% | 0% | 1% | neck mode 26% |
| 4 | tracking | 64,000 | tested | 3.03 | 80 | 6.2 | 1.25 | 8.3 | 27 | 6% | 12% | 5% | 1% | 1% | 2% | neck mode 35% |
| 4.5 | tracking | 72,000 | tested | 3.41 | 90 | 6.3 | 1.81 | 10.6 | 31 | 8% | 15% | 6% | 1% | 1% | 2% | neck mode 39% |
| 5 | tracking | 80,000 | tested | 3.79 | 100 | 6.4 | 2.52 | 13.3 | 35 | 10% | 19% | 8% | 1% | 1% | 3% | neck mode 44% |
| 6 | tracking | 96,000 | tested | 4.55 | 120 | 6.5 | 4.41 | 19.4 | 43 | 14% | 28% | 12% | 2% | 2% | 4% | neck mode 52% |
| 7 | tracking | 112,000 | tested | 5.30 | 140 | 6.6 | 7.01 | 26.6 | 50 | 19% | 38% | 16% | 2% | 2% | 5% | neck mode 61% |
| 7.5 | power-capped | 120,000 | tested | 5.30 | 140 | 4.8 | 7.01 | 22.5 | 39 | 17% | 32% | 14% | 2% | 3% | 6% | neck mode 65% |
| 8 | braked | 128,000 | beyond tested | 5.30 | 140 | 0.3 | 0.00 | 1.4 | 0 | 3% | 2% | 2% | 3% | 3% | 4% | generator heat 4% |
| 9 | braked | 144,000 | beyond tested | 5.30 | 140 | 0.0 | 0.00 | 0.0 | 0 | 3% | 0% | 3% | 4% | 4% | 5% | hub 5% |
| 10 | braked | 160,000 | beyond tested | 5.30 | 140 | 0.0 | 0.00 | 0.0 | 0 | 4% | 0% | 3% | 4% | 5% | 6% | hub 6% |
| 12 | braked | 192,000 | beyond tested | 5.30 | 140 | 0.0 | 0.00 | 0.0 | 0 | 6% | 0% | 5% | 6% | 7% | 9% | hub 9% |
| 15 | braked | 240,000 | drag crisis | 5.30 | 140 | 0.0 | 0.00 | 0.0 | 0 | 9% | 0% | 7% | 10% | 11% | 14% | hub 14% |
| 20 | braked | 320,000 | drag crisis | 5.30 | 140 | 0.0 | 0.00 | 0.0 | 0 | 17% | 0% | 13% | 18% | 19% | 24% | hub 24% |
| 25 | braked | 400,000 | drag crisis | 5.30 | 140 | 0.0 | 0.00 | 0.0 | 0 | 26% | 0% | 20% | 28% | 30% | 38% | hub 38% |
| 30 | braked | 480,000 | drag crisis | 5.30 | 140 | 0.0 | 0.00 | 0.0 | 0 | 38% | 0% | 29% | 40% | 44% | 54% | hub 54% |
| 35 | braked | 560,000 | drag crisis | 5.30 | 140 | 0.0 | 0.00 | 0.0 | 0 | 51% | 0% | 40% | 54% | 59% | 74% | hub 74% |
| 40 | braked | 640,000 | drag crisis | 5.30 | 140 | 0.0 | 0.00 | 0.0 | 0 | 67% | 0% | 52% | 71% | 78% | 97% | hub 97% |

## Power from 1 to 40 m/s

Model potential = output if the tube stayed tuned and locked on with nothing failing (not achievable). Within limits = the most it can deliver with every part within limits, retuning as far as the neck's bending mode allows. As designed = the default control.

- Neck-tube bending mode about 14.3 Hz, so the swing must stay below 9.5 Hz: retuning is possible up to 11.5 m/s
- As designed: generates 1.7-8.0 m/s, peak 7.01 W, braked above
- Kept generating within every limit: generates 1.8-11.2 m/s, peak 24.96 W at 10.75 m/s; nothing above 12.5 m/s
- Yearly energy, central case (kWh): 3.5 m/s site: as designed 5.9, within limits 7.1; 4.5 m/s site: as designed 8.4, within limits 14.0; 5.5 m/s site: as designed 9.2, within limits 20.4; 6.5 m/s site: as designed 8.8, within limits 24.4

| Wind (m/s) | Re | Flow | Wind through tube (W) | Model potential (W) | Within limits (W) | Within limits: what governs | As designed (W) | As designed: mode |
|---|---|---|---|---|---|---|---|---|
| 1 | 16,000 | tested | 0.1 | 0.00 | 0.00 | idle | 0.00 | idle |
| 2 | 32,000 | tested | 1.2 | 0.09 | 0.10 | unconstrained | 0.09 | tracking |
| 3 | 48,000 | tested | 4.0 | 0.48 | 0.48 | unconstrained | 0.48 | tracking |
| 4 | 64,000 | tested | 9.4 | 1.25 | 1.26 | unconstrained | 1.25 | tracking |
| 4.5 | 72,000 | tested | 13.4 | 1.81 | 1.83 | unconstrained | 1.81 | tracking |
| 5 | 80,000 | tested | 18.4 | 2.52 | 2.54 | unconstrained | 2.52 | tracking |
| 6 | 96,000 | tested | 31.8 | 4.41 | 4.44 | unconstrained | 4.41 | tracking |
| 7 | 112,000 | tested | 50.4 | 7.01 | 7.07 | unconstrained | 7.01 | tracking |
| 8 | 128,000 | beyond tested | 75.3 | 10.41 | 10.52 | unconstrained | 0.00 | braked |
| 9 | 144,000 | beyond tested | 107.2 | 14.71 | 14.88 | unconstrained | 0.00 | braked |
| 10 | 160,000 | beyond tested | 147.0 | 19.98 | 20.24 | unconstrained | 0.00 | braked |
| 11 | 176,000 | beyond tested | 195.7 | 26.30 | 1.80 | limited by generator heat | 0.00 | braked |
| 12 | 192,000 | beyond tested | 254.0 | 33.73 | 0.00 | braked (generator heat) | 0.00 | braked |
| 13 | 208,000 | drag crisis | 323.0 | 42.32 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 14 | 224,000 | drag crisis | 403.4 | 52.14 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 15 | 240,000 | drag crisis | 496.1 | 63.22 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 17.5 | 280,000 | drag crisis | 787.8 | 96.68 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 20 | 320,000 | drag crisis | 1,176.0 | 138.64 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 25 | 400,000 | drag crisis | 2,296.9 | 248.19 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 30 | 480,000 | drag crisis | 3,969.0 | 389.36 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 35 | 560,000 | drag crisis | 6,302.6 | 555.23 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 40 | 640,000 | drag crisis | 9,408.0 | 734.41 | 0.00 | braked (drag crisis) | 0.00 | braked |

## Structure at the survival requirement (40 m/s, parked and braked)

- Drag on the tube 282 N; bending moment at tube base 141 N m, at the hinge 339 N m (hub built for 350)
- Neck stress 267 MPa (allowable 400); skin stress at tube base 20.8 MPa (allowable 40)
- Shell ovalling 7.06 N m/m against a wall capacity of 10.00 N m/m
- End-disc gust utilisation 78%
- Hinge bushing load 1698 N each
- Post base moment with hinge at 3 m: 1338 N m (size the post to your local wind code)
- Swing cycles per year at 30 % duty: 3.2e+07

## Annual energy (very rough)

Rayleigh wind at hub height, power curve from the envelope above (tracking, then capped at 7.01 W, braked from 8.0 m/s), 50 % of swinging time assumed locked on. Low case = 0.5 x central.

| Site mean wind | Low (kWh/yr) | Central (kWh/yr) |
|---|---|---|
| 3.0 m/s | 2.0 | 4.1 |
| 3.5 m/s | 2.9 | 5.9 |
| 4.5 m/s | 4.2 | 8.4 |
| 5.5 m/s | 4.6 | 9.2 |

