# Lantern sweep: ranked by electrical power at 4.5 m/s

10368 combinations: D 0.1-0.4 m, neck 0.0-0.8 m, disc ratio 1.0-2.4, shells xps2-glass, xps3-glass, xps5-glass, pulley teeth [10, 12, 16].  
8424 pass all limits. Rejected (a design can fail several): skin stress 1944

| Rank | Score (W) | D (mm) | Neck (mm) | Disc ratio | Shell | Teeth | Gear | Mass ratio | Mech eff 4.5 | Swing 4.5 (deg) | Re at U_max |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 3.35 | 400 | 800 | 2.0 | xps2-glass | 10 | 31.4 | 2.65 | 20.5 % | 10.7 | 186667 |
| 2 | 3.34 | 400 | 800 | 2.2 | xps2-glass | 10 | 31.4 | 2.90 | 20.4 % | 10.7 | 186667 |
| 3 | 3.33 | 400 | 800 | 2.0 | xps3-glass | 10 | 31.4 | 2.95 | 20.4 % | 10.7 | 186667 |
| 4 | 3.32 | 400 | 800 | 2.4 | xps2-glass | 10 | 31.4 | 3.18 | 20.3 % | 10.7 | 186667 |
| 5 | 3.32 | 400 | 800 | 2.2 | xps3-glass | 10 | 31.4 | 3.20 | 20.3 % | 10.7 | 186667 |
| 6 | 3.30 | 400 | 700 | 2.0 | xps2-glass | 10 | 31.4 | 2.68 | 19.8 % | 11.4 | 186667 |
| 7 | 3.30 | 400 | 800 | 2.4 | xps3-glass | 10 | 31.4 | 3.48 | 20.2 % | 10.6 | 186667 |
| 8 | 3.30 | 400 | 800 | 2.0 | xps5-glass | 10 | 31.4 | 3.56 | 20.1 % | 10.6 | 186667 |

## Sensitivity around the best design (one variable at a time)

| Variable | Value | Score | vs best |
|---|---|---|---|
| D (mm) | 100 | 0.65 | -81 % (fails skin stress) |
| D (mm) | 140 | 1.06 | -68 % (fails skin stress) |
| D (mm) | 180 | 1.45 | -57 % |
| D (mm) | 220 | 1.83 | -45 % |
| D (mm) | 260 | 2.20 | -35 % |
| D (mm) | 300 | 2.54 | -24 % |
| D (mm) | 340 | 2.88 | -14 % |
| D (mm) | 380 | 3.20 | -5 % |
| Neck (mm) | 0 | 2.02 | -40 % |
| Neck (mm) | 100 | 2.31 | -31 % |
| Neck (mm) | 200 | 2.57 | -23 % |
| Neck (mm) | 300 | 2.79 | -17 % |
| Neck (mm) | 400 | 2.97 | -11 % |
| Neck (mm) | 500 | 3.11 | -7 % |
| Neck (mm) | 600 | 3.22 | -4 % |
| Neck (mm) | 700 | 3.30 | -2 % |
| Neck (mm) | 800 | 3.35 | +0 % |
| Disc ratio | 1 | 2.06 | -39 % |
| Disc ratio | 1.2 | 2.31 | -31 % |
| Disc ratio | 1.4 | 2.58 | -23 % |
| Disc ratio | 1.6 | 2.84 | -15 % |
| Disc ratio | 1.8 | 3.10 | -8 % |
| Disc ratio | 2 | 3.35 | +0 % |
| Disc ratio | 2.2 | 3.34 | -0 % |
| Disc ratio | 2.4 | 3.32 | -1 % |
| Pulley teeth | 10 | 3.35 | +0 % |
| Pulley teeth | 12 | 3.20 | -5 % |
| Pulley teeth | 16 | 2.77 | -17 % |
| Shell | xps2-glass | 3.35 | +0 % |
| Shell | xps3-glass | 3.33 | -1 % |
| Shell | xps5-glass | 3.30 | -2 % |

Best: shell xps2-glass. Full report for it follows.

# Lantern calculator report

Tube 400 mm x 1000 mm, neck 800 mm, end discs 800 mm, shell 0.124 kg/m^2, height/diameter 2.5

Constraint check: all pass

## Masses (kg)

| Part | Mass |
|---|---|
| Tube shell incl. rings and seams | 0.176 |
| End discs, each | 0.080 |
| Bottom spider | 0.015 |
| Neck tube | 0.113 |
| Hub, axle, carriage, belt arc | 0.150 |
| **Total swinging mass** | **0.615** |

## Inertia about the hinge (kg m^2)

| Part | Inertia |
|---|---|
| shell | 0.3118 |
| discs | 0.3185 |
| spider | 0.0096 |
| neck | 0.0241 |
| hub | 0.0007 |
| generator | 0.0592 |
| Structural total | 0.7239 |
| Air moving with the tube | 0.2730 |
| **Total** | **0.9969** |
| Mass ratio (structural / displaced air) | 2.65 |

- Gear ratio: 31.4:1 (100 mm arc to 10-tooth GT2 pulley)
- Mode-shape factor gamma: 1.244
- Effective length after end losses: 1.000 m
- Gravity (destabilising) stiffness: 4.85 N m/rad

## Tuning

Two opposing springs, each 10.29 N/mm.

| Wind (m/s) | Tune f_n (Hz) | Stiffness (N m/rad) | Carriage below hinge (mm) |
|---|---|---|---|
| 3.0 | 1.36 | 78.0 | 61.6 |
| 4.0 | 1.82 | 135.0 | 81.0 |
| 4.5 | 2.05 | 169.5 | 90.8 |
| 5.0 | 2.27 | 208.1 | 100.6 |
| 6.0 | 2.73 | 297.6 | 120.3 |
| 7.0 | 3.18 | 403.3 | 140.0 |

Carriage moves about 19.6 mm per 1 m/s between 4 and 6 m/s.

## Operating points (locked on, model central case)

| Wind | Re | Swing f (Hz) | Wind power (W) | Mech (W) | Elec (W) | Elec low case (W) | Mech eff | Swing (deg) | Peak torque (N m) | Gen zeta | Parasitic zeta | Circuit R (ohm) | Copper eff | EMF peak (V) | Gen peak rpm | Top accel (g) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 3.0 | 80000 | 1.50 | 6.6 | 1.27 | 0.97 | 0.48 | 19.2 % | 10.3 | 1.49 | 0.064 | 0.0140 | 162 | 93 % | 20.3 | 510 | 2.9 |
| 4.5 | 120000 | 2.25 | 22.3 | 4.57 | 3.35 | 1.68 | 20.5 % | 10.7 | 3.45 | 0.064 | 0.0097 | 109 | 89 % | 31.6 | 794 | 6.9 |
| 6.0 | 160000 | 3.00 | 52.9 | 11.07 | 7.80 | 3.90 | 20.9 % | 10.9 | 6.19 | 0.063 | 0.0083 | 82 | 85 % | 42.7 | 1072 | 12.4 |
| 7.0 | 186667 | 3.50 | 84.0 | 17.71 | 12.12 | 6.06 | 21.1 % | 10.9 | 8.45 | 0.063 | 0.0078 | 71 | 83 % | 50.0 | 1257 | 16.9 |

At 4.5 m/s: tube swings +/-152 mm at the bottom, +/-246 mm mid-height, +/-341 mm at the top; generator swings +/-337 deg. Friction: bushings 0.160 N m, generator drag 0.126 N m (at the hinge).

## Structure

- Survival drag at 25 m/s: 184 N
- Bending moment at tube base 92 N m, at hinge 239 N m
- Glass-skin stress at tube base 14.6 MPa (bare foam would see 0.24 MPa, about its strength)
- Neck 30x28 mm carbon tube stress 374 MPa
- Three 4 mm carbon rods (first chat version) would buckle at 19 N; their load is 255 N at 10 m/s and 1592 N at 25 m/s
- Hinge bushing load at 25 m/s: 1592 N each
- Swing cycles per year at 30 % duty: 1.9e+07

## Annual energy (very rough)

Rayleigh wind at hub height, tuning band 3.0-7.0 m/s +/-20 %, 50 % of in-band time locked on. Low case = 0.5 x central.

| Site mean wind | Low (kWh/yr) | Central (kWh/yr) |
|---|---|---|
| 3.5 m/s | 5.6 | 11.3 |
| 4.5 m/s | 8.6 | 17.2 |
| 5.5 m/s | 9.9 | 19.7 |

