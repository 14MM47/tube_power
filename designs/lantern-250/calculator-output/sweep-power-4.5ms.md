# Lantern sweep: ranked by electrical power at 4.5 m/s

20736 combinations: D 0.1-0.4 m, neck 0.0-0.8 m, disc ratio 1.0-2.4, shells xps2-glass, xps3-glass, xps5-glass, pulley teeth [12, 16, 20, 24, 30, 36].  
6456 pass all limits. Rejected (a design can fail several): Reynolds 10368, generator too weak 623, hinge moment 3888, skin stress 3888

| Rank | Score (W) | D (mm) | Neck (mm) | Disc ratio | Shell | Teeth | Gear | Mass ratio | Mech eff 4.5 | Swing 4.5 (deg) | Re at U_max |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1.99 | 240 | 800 | 2.0 | xps2-glass | 12 | 26.2 | 3.97 | 19.9 % | 6.3 | 112000 |
| 2 | 1.98 | 240 | 800 | 2.2 | xps2-glass | 12 | 26.2 | 4.21 | 19.8 % | 6.3 | 112000 |
| 3 | 1.97 | 240 | 800 | 2.0 | xps3-glass | 12 | 26.2 | 4.47 | 19.7 % | 6.3 | 112000 |
| 4 | 1.97 | 240 | 800 | 2.4 | xps2-glass | 12 | 26.2 | 4.48 | 19.7 % | 6.3 | 112000 |
| 5 | 1.96 | 240 | 800 | 2.2 | xps3-glass | 12 | 26.2 | 4.72 | 19.6 % | 6.3 | 112000 |
| 6 | 1.95 | 240 | 700 | 2.0 | xps2-glass | 12 | 26.2 | 3.99 | 19.3 % | 6.7 | 112000 |
| 7 | 1.95 | 240 | 800 | 2.4 | xps3-glass | 12 | 26.2 | 4.98 | 19.5 % | 6.2 | 112000 |
| 8 | 1.94 | 240 | 700 | 2.2 | xps2-glass | 12 | 26.2 | 4.24 | 19.2 % | 6.7 | 112000 |
| 9 | 1.93 | 240 | 700 | 2.0 | xps3-glass | 12 | 26.2 | 4.49 | 19.1 % | 6.7 | 112000 |
| 10 | 1.93 | 240 | 700 | 2.4 | xps2-glass | 12 | 26.2 | 4.51 | 19.1 % | 6.7 | 112000 |
| 11 | 1.93 | 240 | 800 | 2.0 | xps5-glass | 12 | 26.2 | 5.48 | 19.3 % | 6.2 | 112000 |
| 12 | 1.92 | 240 | 700 | 2.2 | xps3-glass | 12 | 26.2 | 4.74 | 19.0 % | 6.6 | 112000 |
| 13 | 1.92 | 240 | 800 | 2.2 | xps5-glass | 12 | 26.2 | 5.72 | 19.2 % | 6.2 | 112000 |
| 14 | 1.91 | 240 | 700 | 2.4 | xps3-glass | 12 | 26.2 | 5.02 | 18.9 % | 6.6 | 112000 |
| 15 | 1.91 | 240 | 800 | 2.4 | xps5-glass | 12 | 26.2 | 5.99 | 19.1 % | 6.2 | 112000 |

## Sensitivity around the best design (one variable at a time)

| Variable | Value | Score | vs best |
|---|---|---|---|
| D (mm) | 100 | 0.68 | -66 % (fails skin stress) |
| D (mm) | 140 | 1.08 | -46 % (fails skin stress) |
| D (mm) | 180 | 1.46 | -27 % |
| D (mm) | 220 | 1.82 | -9 % |
| D (mm) | 260 | 2.15 | +8 % (fails Reynolds, hinge moment) |
| D (mm) | 300 | 2.48 | +25 % (fails Reynolds, hinge moment) |
| D (mm) | 340 | 2.78 | +40 % (fails Reynolds, hinge moment) |
| D (mm) | 380 | 3.07 | +54 % (fails Reynolds, hinge moment) |
| Neck (mm) | 0 | 1.15 | -42 % |
| Neck (mm) | 100 | 1.33 | -33 % |
| Neck (mm) | 200 | 1.49 | -25 % |
| Neck (mm) | 300 | 1.63 | -18 % |
| Neck (mm) | 400 | 1.74 | -12 % |
| Neck (mm) | 500 | 1.83 | -8 % |
| Neck (mm) | 600 | 1.90 | -4 % |
| Neck (mm) | 700 | 1.95 | -2 % |
| Neck (mm) | 800 | 1.99 | +0 % |
| Disc ratio | 1 | 1.54 | -22 % |
| Disc ratio | 1.2 | 1.63 | -18 % |
| Disc ratio | 1.4 | 1.72 | -13 % |
| Disc ratio | 1.6 | 1.81 | -9 % |
| Disc ratio | 1.8 | 1.90 | -4 % |
| Disc ratio | 2 | 1.99 | +0 % |
| Disc ratio | 2.2 | 1.98 | -0 % |
| Disc ratio | 2.4 | 1.97 | -1 % |
| Pulley teeth | 12 | 1.99 | +0 % |
| Pulley teeth | 16 | 1.86 | -6 % |
| Pulley teeth | 20 | 1.67 | -16 % |
| Pulley teeth | 24 | 1.42 | -29 % |
| Pulley teeth | 30 | 0.94 | -53 % |
| Pulley teeth | 36 | 0.34 | -83 % (fails generator too weak) |
| Shell | xps2-glass | 1.99 | +0 % |
| Shell | xps3-glass | 1.97 | -1 % |
| Shell | xps5-glass | 1.93 | -3 % |

Best: shell xps2-glass. Full report for it follows.

# Lantern calculator report

Tube 240 mm x 1000 mm, neck 800 mm, end discs 480 mm, shell 0.124 kg/m^2, height/diameter 4.2

Constraint check: all pass

## Masses (kg)

| Part | Mass |
|---|---|
| Tube shell incl. rings and seams | 0.113 |
| End discs, each | 0.029 |
| Bottom spider | 0.015 |
| Neck tube | 0.113 |
| Hub, axle, carriage, belt arc | 0.150 |
| **Total swinging mass** | **0.449** |

## Inertia about the hinge (kg m^2)

| Part | Inertia |
|---|---|
| shell | 0.2013 |
| discs | 0.1132 |
| spider | 0.0096 |
| neck | 0.0241 |
| hub | 0.0007 |
| generator | 0.0411 |
| Structural total | 0.3900 |
| Air moving with the tube | 0.0983 |
| **Total** | **0.4883** |
| Mass ratio (structural / displaced air) | 3.97 |

- Gear ratio: 26.2:1 (100 mm arc to 12-tooth GT2 pulley)
- Mode-shape factor gamma: 1.244
- Effective length after end losses: 1.000 m
- Gravity (destabilising) stiffness: 2.75 N m/rad

## Tuning

Two opposing springs, each 13.90 N/mm.

| Wind (m/s) | Tune f_n (Hz) | Stiffness (N m/rad) | Carriage below hinge (mm) |
|---|---|---|---|
| 3.0 | 2.27 | 102.3 | 60.7 |
| 4.0 | 3.03 | 179.8 | 80.4 |
| 4.5 | 3.41 | 226.8 | 90.3 |
| 5.0 | 3.79 | 279.3 | 100.2 |
| 6.0 | 4.55 | 401.0 | 120.1 |
| 7.0 | 5.30 | 544.8 | 140.0 |

Carriage moves about 19.8 mm per 1 m/s between 4 and 6 m/s.

## Operating points (locked on, model central case)

| Wind | Re | Swing f (Hz) | Wind power (W) | Mech (W) | Elec (W) | Elec low case (W) | Mech eff | Swing (deg) | Peak torque (N m) | Gen zeta | Parasitic zeta | Circuit R (ohm) | Copper eff | EMF peak (V) | Gen peak rpm | Top accel (g) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 3.0 | 48000 | 2.50 | 4.0 | 0.72 | 0.55 | 0.28 | 18.1 % | 6.0 | 0.88 | 0.044 | 0.0125 | 185 | 94 % | 16.3 | 410 | 4.7 |
| 4.5 | 72000 | 3.75 | 13.4 | 2.67 | 1.99 | 0.99 | 19.9 % | 6.3 | 2.05 | 0.043 | 0.0084 | 125 | 90 % | 25.9 | 650 | 11.2 |
| 6.0 | 96000 | 5.00 | 31.8 | 6.52 | 4.69 | 2.35 | 20.5 % | 6.4 | 3.69 | 0.043 | 0.0070 | 95 | 87 % | 35.1 | 883 | 20.3 |
| 7.0 | 112000 | 5.83 | 50.4 | 10.46 | 7.35 | 3.67 | 20.7 % | 6.5 | 5.05 | 0.043 | 0.0066 | 81 | 85 % | 41.2 | 1036 | 27.9 |

At 4.5 m/s: tube swings +/-89 mm at the bottom, +/-144 mm mid-height, +/-199 mm at the top; generator swings +/-165 deg. Friction: bushings 0.097 N m, generator drag 0.105 N m (at the hinge).

## Structure

- Survival drag at 25 m/s: 110 N
- Bending moment at tube base 55 N m, at hinge 143 N m
- Glass-skin stress at tube base 24.4 MPa (bare foam would see 0.41 MPa, about its strength)
- Neck 30x28 mm carbon tube stress 224 MPa
- Three 4 mm carbon rods (first chat version) would buckle at 19 N; their load is 153 N at 10 m/s and 956 N at 25 m/s
- Hinge bushing load at 25 m/s: 956 N each
- Swing cycles per year at 30 % duty: 3.2e+07

## Annual energy (very rough)

Rayleigh wind at hub height, tuning band 3.0-7.0 m/s +/-20 %, 50 % of in-band time locked on. Low case = 0.5 x central.

| Site mean wind | Low (kWh/yr) | Central (kWh/yr) |
|---|---|---|
| 3.5 m/s | 3.4 | 6.7 |
| 4.5 m/s | 5.2 | 10.4 |
| 5.5 m/s | 5.9 | 11.9 |

