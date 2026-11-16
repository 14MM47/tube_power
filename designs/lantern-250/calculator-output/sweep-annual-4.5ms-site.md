# Lantern sweep: ranked by central-case annual energy at a 4.5 m/s site

5346 combinations: D 0.2-0.3 m, neck 0.0-0.8 m, disc ratio 1.4-2.4, shells xps2-glass, xps3-glass, xps5-glass, pulley teeth [10, 12, 16].  
2916 pass all limits. Rejected (a design can fail several): Reynolds 2430, hinge moment 486

| Rank | Score (kWh/yr) | D (mm) | Neck (mm) | Disc ratio | Shell | Teeth | Gear | Mass ratio | Mech eff 4.5 | Swing 4.5 (deg) | Re at U_max |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 11.15 | 250 | 800 | 2.0 | xps2-glass | 10 | 31.4 | 3.98 | 19.7 % | 6.5 | 116667 |
| 2 | 11.10 | 250 | 800 | 2.2 | xps2-glass | 10 | 31.4 | 4.23 | 19.6 % | 6.5 | 116667 |
| 3 | 11.05 | 250 | 800 | 2.0 | xps3-glass | 10 | 31.4 | 4.47 | 19.5 % | 6.5 | 116667 |
| 4 | 11.04 | 250 | 800 | 2.4 | xps2-glass | 10 | 31.4 | 4.50 | 19.5 % | 6.5 | 116667 |
| 5 | 11.00 | 250 | 800 | 2.2 | xps3-glass | 10 | 31.4 | 4.71 | 19.4 % | 6.5 | 116667 |
| 6 | 10.97 | 250 | 700 | 2.0 | xps2-glass | 10 | 31.4 | 4.03 | 19.0 % | 6.9 | 116667 |
| 7 | 10.94 | 250 | 800 | 2.4 | xps3-glass | 10 | 31.4 | 4.98 | 19.3 % | 6.5 | 116667 |
| 8 | 10.92 | 250 | 700 | 2.2 | xps2-glass | 10 | 31.4 | 4.28 | 18.9 % | 6.9 | 116667 |
| 9 | 10.87 | 250 | 700 | 2.0 | xps3-glass | 10 | 31.4 | 4.52 | 18.8 % | 6.9 | 116667 |
| 10 | 10.86 | 250 | 700 | 2.4 | xps2-glass | 10 | 31.4 | 4.55 | 18.8 % | 6.9 | 116667 |
| 11 | 10.85 | 250 | 800 | 2.0 | xps5-glass | 10 | 31.4 | 5.43 | 19.1 % | 6.4 | 116667 |
| 12 | 10.82 | 250 | 700 | 2.2 | xps3-glass | 10 | 31.4 | 4.76 | 18.7 % | 6.9 | 116667 |
| 13 | 10.80 | 250 | 800 | 2.2 | xps5-glass | 10 | 31.4 | 5.68 | 19.0 % | 6.4 | 116667 |
| 14 | 10.76 | 250 | 800 | 2.0 | xps2-glass | 12 | 26.2 | 3.81 | 20.0 % | 6.6 | 116667 |
| 15 | 10.76 | 250 | 700 | 2.4 | xps3-glass | 10 | 31.4 | 5.04 | 18.6 % | 6.9 | 116667 |

## Sensitivity around the best design (one variable at a time)

| Variable | Value | Score | vs best |
|---|---|---|---|
| D (mm) | 200 | 8.83 | -21 % |
| D (mm) | 210 | 9.31 | -17 % |
| D (mm) | 220 | 9.78 | -12 % |
| D (mm) | 230 | 10.24 | -8 % |
| D (mm) | 240 | 10.70 | -4 % |
| D (mm) | 250 | 11.15 | +0 % |
| D (mm) | 260 | 11.60 | +4 % (fails Reynolds, hinge moment) |
| D (mm) | 270 | 12.04 | +8 % (fails Reynolds, hinge moment) |
| D (mm) | 280 | 12.47 | +12 % (fails Reynolds, hinge moment) |
| D (mm) | 290 | 12.90 | +16 % (fails Reynolds, hinge moment) |
| D (mm) | 300 | 13.32 | +19 % (fails Reynolds, hinge moment) |
| Neck (mm) | 0 | 6.62 | -41 % |
| Neck (mm) | 100 | 7.62 | -32 % |
| Neck (mm) | 200 | 8.50 | -24 % |
| Neck (mm) | 300 | 9.24 | -17 % |
| Neck (mm) | 400 | 9.85 | -12 % |
| Neck (mm) | 500 | 10.33 | -7 % |
| Neck (mm) | 600 | 10.70 | -4 % |
| Neck (mm) | 700 | 10.97 | -2 % |
| Neck (mm) | 800 | 11.15 | +0 % |
| Disc ratio | 1.4 | 9.59 | -14 % |
| Disc ratio | 1.6 | 10.12 | -9 % |
| Disc ratio | 1.8 | 10.64 | -5 % |
| Disc ratio | 2 | 11.15 | +0 % |
| Disc ratio | 2.2 | 11.10 | -0 % |
| Disc ratio | 2.4 | 11.04 | -1 % |
| Pulley teeth | 10 | 11.15 | +0 % |
| Pulley teeth | 12 | 10.76 | -3 % |
| Pulley teeth | 16 | 9.57 | -14 % |
| Shell | xps2-glass | 11.15 | +0 % |
| Shell | xps3-glass | 11.05 | -1 % |
| Shell | xps5-glass | 10.85 | -3 % |

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

