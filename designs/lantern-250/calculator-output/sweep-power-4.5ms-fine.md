# Lantern sweep: ranked by electrical power at 4.5 m/s

30855 combinations: D 0.2-0.3 m, neck 0.0-0.8 m, disc ratio 1.4-2.4, shells xps2-glass, xps3-glass, xps5-glass, pulley teeth [10, 12, 14, 16, 20].  
16830 pass all limits. Rejected (a design can fail several): Reynolds 14025, hinge moment 2475

| Rank | Score (W) | D (mm) | Neck (mm) | Disc ratio | Shell | Teeth | Gear | Mass ratio | Mech eff 4.5 | Swing 4.5 (deg) | Re at U_max |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 2.11 | 250 | 800 | 2.0 | xps2-glass | 10 | 31.4 | 3.98 | 19.7 % | 6.5 | 116667 |
| 2 | 2.10 | 250 | 800 | 2.1 | xps2-glass | 10 | 31.4 | 4.10 | 19.6 % | 6.5 | 116667 |
| 3 | 2.10 | 250 | 800 | 2.2 | xps2-glass | 10 | 31.4 | 4.23 | 19.6 % | 6.5 | 116667 |
| 4 | 2.09 | 250 | 800 | 2.3 | xps2-glass | 10 | 31.4 | 4.36 | 19.5 % | 6.5 | 116667 |
| 5 | 2.09 | 250 | 800 | 2.0 | xps3-glass | 10 | 31.4 | 4.47 | 19.5 % | 6.5 | 116667 |
| 6 | 2.08 | 250 | 800 | 2.4 | xps2-glass | 10 | 31.4 | 4.50 | 19.5 % | 6.5 | 116667 |
| 7 | 2.08 | 250 | 750 | 2.0 | xps2-glass | 10 | 31.4 | 4.00 | 19.4 % | 6.7 | 116667 |
| 8 | 2.08 | 250 | 800 | 2.1 | xps3-glass | 10 | 31.4 | 4.59 | 19.4 % | 6.5 | 116667 |
| 9 | 2.08 | 250 | 750 | 2.1 | xps2-glass | 10 | 31.4 | 4.12 | 19.3 % | 6.7 | 116667 |
| 10 | 2.08 | 250 | 800 | 2.2 | xps3-glass | 10 | 31.4 | 4.71 | 19.4 % | 6.5 | 116667 |
| 11 | 2.07 | 250 | 750 | 2.2 | xps2-glass | 10 | 31.4 | 4.25 | 19.3 % | 6.7 | 116667 |
| 12 | 2.07 | 250 | 800 | 2.0 | xps2-glass | 12 | 26.2 | 3.81 | 20.0 % | 6.6 | 116667 |
| 13 | 2.07 | 250 | 800 | 2.3 | xps3-glass | 10 | 31.4 | 4.84 | 19.3 % | 6.5 | 116667 |
| 14 | 2.07 | 250 | 750 | 2.3 | xps2-glass | 10 | 31.4 | 4.38 | 19.2 % | 6.7 | 116667 |
| 15 | 2.07 | 250 | 800 | 2.1 | xps2-glass | 12 | 26.2 | 3.93 | 20.0 % | 6.6 | 116667 |

## Sensitivity around the best design (one variable at a time)

| Variable | Value | Score | vs best |
|---|---|---|---|
| D (mm) | 200 | 1.64 | -22 % |
| D (mm) | 210 | 1.74 | -17 % |
| D (mm) | 220 | 1.83 | -13 % |
| D (mm) | 230 | 1.92 | -9 % |
| D (mm) | 240 | 2.02 | -4 % |
| D (mm) | 250 | 2.11 | +0 % |
| D (mm) | 260 | 2.20 | +4 % (fails Reynolds, hinge moment) |
| D (mm) | 270 | 2.28 | +8 % (fails Reynolds, hinge moment) |
| D (mm) | 280 | 2.37 | +13 % (fails Reynolds, hinge moment) |
| D (mm) | 290 | 2.46 | +17 % (fails Reynolds, hinge moment) |
| D (mm) | 300 | 2.54 | +21 % (fails Reynolds, hinge moment) |
| Neck (mm) | 0 | 1.15 | -46 % |
| Neck (mm) | 100 | 1.34 | -36 % |
| Neck (mm) | 200 | 1.52 | -28 % |
| Neck (mm) | 300 | 1.68 | -20 % |
| Neck (mm) | 400 | 1.80 | -14 % |
| Neck (mm) | 500 | 1.91 | -9 % |
| Neck (mm) | 600 | 1.99 | -5 % |
| Neck (mm) | 700 | 2.06 | -2 % |
| Neck (mm) | 800 | 2.11 | +0 % |
| Disc ratio | 1.4 | 1.81 | -14 % |
| Disc ratio | 1.5 | 1.86 | -12 % |
| Disc ratio | 1.6 | 1.91 | -9 % |
| Disc ratio | 1.7 | 1.96 | -7 % |
| Disc ratio | 1.8 | 2.01 | -5 % |
| Disc ratio | 1.9 | 2.06 | -2 % |
| Disc ratio | 2 | 2.11 | +0 % |
| Disc ratio | 2.1 | 2.10 | -0 % |
| Disc ratio | 2.2 | 2.10 | -0 % |
| Disc ratio | 2.3 | 2.09 | -1 % |
| Disc ratio | 2.4 | 2.08 | -1 % |
| Pulley teeth | 10 | 2.11 | +0 % |
| Pulley teeth | 12 | 2.07 | -2 % |
| Pulley teeth | 14 | 2.01 | -4 % |
| Pulley teeth | 16 | 1.93 | -8 % |
| Pulley teeth | 20 | 1.72 | -18 % |
| Shell | xps2-glass | 2.11 | +0 % |
| Shell | xps3-glass | 2.09 | -1 % |
| Shell | xps5-glass | 2.05 | -3 % |

Best: shell xps2-glass. Full report for it follows.

# Lantern calculator report

Tube 250 mm x 1000 mm, neck 800 mm, end discs 500 mm, shell 0.124 kg/m^2, height/diameter 4.0

Constraint check: all pass

## Masses (kg)

| Part | Mass |
|---|---|
| Tube shell incl. rings and seams | 0.117 |
| End discs, each | 0.031 |
| Bottom spider | 0.015 |
| Neck tube | 0.113 |
| Hub, axle, carriage, belt arc | 0.150 |
| **Total swinging mass** | **0.458** |

## Inertia about the hinge (kg m^2)

| Part | Inertia |
|---|---|
| shell | 0.2082 |
| discs | 0.1229 |
| spider | 0.0096 |
| neck | 0.0241 |
| hub | 0.0007 |
| generator | 0.0592 |
| Structural total | 0.4247 |
| Air moving with the tube | 0.1066 |
| **Total** | **0.5313** |
| Mass ratio (structural / displaced air) | 3.98 |

- Gear ratio: 31.4:1 (100 mm arc to 10-tooth GT2 pulley)
- Mode-shape factor gamma: 1.244
- Effective length after end losses: 1.000 m
- Gravity (destabilising) stiffness: 2.86 N m/rad

## Tuning

Two opposing springs, each 13.94 N/mm.

| Wind (m/s) | Tune f_n (Hz) | Stiffness (N m/rad) | Carriage below hinge (mm) |
|---|---|---|---|
| 3.0 | 2.18 | 102.7 | 60.7 |
| 4.0 | 2.91 | 180.4 | 80.4 |
| 4.5 | 3.27 | 227.5 | 90.3 |
| 5.0 | 3.64 | 280.2 | 100.3 |
| 6.0 | 4.36 | 402.3 | 120.1 |
| 7.0 | 5.09 | 546.5 | 140.0 |

Carriage moves about 19.8 mm per 1 m/s between 4 and 6 m/s.

## Operating points (locked on, model central case)

| Wind | Re | Swing f (Hz) | Wind power (W) | Mech (W) | Elec (W) | Elec low case (W) | Mech eff | Swing (deg) | Peak torque (N m) | Gen zeta | Parasitic zeta | Circuit R (ohm) | Copper eff | EMF peak (V) | Gen peak rpm | Top accel (g) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 3.0 | 50000 | 2.40 | 4.1 | 0.73 | 0.57 | 0.29 | 17.6 % | 6.1 | 0.90 | 0.044 | 0.0136 | 255 | 95 % | 19.3 | 484 | 4.5 |
| 4.5 | 75000 | 3.60 | 14.0 | 2.74 | 2.11 | 1.05 | 19.7 % | 6.5 | 2.13 | 0.043 | 0.0088 | 173 | 93 % | 30.8 | 775 | 10.7 |
| 6.0 | 100000 | 4.80 | 33.1 | 6.74 | 5.05 | 2.52 | 20.4 % | 6.7 | 3.83 | 0.043 | 0.0073 | 131 | 91 % | 42.0 | 1055 | 19.5 |
| 7.0 | 116667 | 5.60 | 52.5 | 10.83 | 7.98 | 3.99 | 20.6 % | 6.7 | 5.25 | 0.042 | 0.0068 | 112 | 89 % | 49.3 | 1239 | 26.7 |

At 4.5 m/s: tube swings +/-92 mm at the bottom, +/-149 mm mid-height, +/-206 mm at the top; generator swings +/-205 deg. Friction: bushings 0.101 N m, generator drag 0.126 N m (at the hinge).

## Structure

- Survival drag at 25 m/s: 115 N
- Bending moment at tube base 57 N m, at hinge 149 N m
- Glass-skin stress at tube base 23.4 MPa (bare foam would see 0.39 MPa, about its strength)
- Neck 30x28 mm carbon tube stress 234 MPa
- Three 4 mm carbon rods (first chat version) would buckle at 19 N; their load is 159 N at 10 m/s and 995 N at 25 m/s
- Hinge bushing load at 25 m/s: 995 N each
- Swing cycles per year at 30 % duty: 3.1e+07

## Annual energy (very rough)

Rayleigh wind at hub height, tuning band 3.0-7.0 m/s +/-20 %, 50 % of in-band time locked on. Low case = 0.5 x central.

| Site mean wind | Low (kWh/yr) | Central (kWh/yr) |
|---|---|---|
| 3.5 m/s | 3.6 | 7.2 |
| 4.5 m/s | 5.6 | 11.2 |
| 5.5 m/s | 6.4 | 12.8 |

