# Lantern calculator report

Tube 250 mm x 1000 mm, neck 400 mm, end discs 400 mm, shell 0.161 kg/m^2, height/diameter 4.0

Constraint check: all pass

## Masses (kg)

| Part | Mass |
|---|---|
| Tube shell incl. rings and seams | 0.146 |
| End discs, each | 0.020 |
| Bottom spider | 0.015 |
| Neck tube | 0.047 |
| Hub, axle, carriage, belt arc | 0.150 |
| **Total swinging mass** | **0.398** |

## Inertia about the hinge (kg m^2)

| Part | Inertia |
|---|---|
| shell | 0.1308 |
| discs | 0.0430 |
| spider | 0.0024 |
| neck | 0.0025 |
| hub | 0.0007 |
| generator | 0.0231 |
| Structural total | 0.2026 |
| Air moving with the tube | 0.0537 |
| **Total** | **0.2563** |
| Mass ratio (structural / displaced air) | 3.77 |

- Gear ratio: 19.6:1 (100 mm arc to 16-tooth GT2 pulley)
- Mode-shape factor gamma: 1.277
- Effective length after end losses: 0.900 m
- Gravity (destabilising) stiffness: 1.80 N m/rad

## Tuning

Two opposing springs, each 6.74 N/mm.

| Wind (m/s) | Tune f_n (Hz) | Stiffness (N m/rad) | Carriage below hinge (mm) |
|---|---|---|---|
| 3.0 | 2.18 | 50.0 | 60.9 |
| 4.0 | 2.91 | 87.4 | 80.6 |
| 4.5 | 3.27 | 110.2 | 90.4 |
| 5.0 | 3.64 | 135.6 | 100.3 |
| 6.0 | 4.36 | 194.5 | 120.1 |
| 7.0 | 5.09 | 264.1 | 140.0 |

Carriage moves about 19.8 mm per 1 m/s between 4 and 6 m/s.

## Operating points (locked on, model central case)

| Wind | Re | Swing f (Hz) | Wind power (W) | Mech (W) | Elec (W) | Elec low case (W) | Mech eff | Swing (deg) | Peak torque (N m) | Gen zeta | Parasitic zeta | Circuit R (ohm) | Copper eff | EMF peak (V) | Gen peak rpm | Top accel (g) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 3.0 | 50000 | 2.40 | 4.1 | 0.57 | 0.44 | 0.22 | 13.7 % | 8.0 | 0.60 | 0.046 | 0.0147 | 197 | 94 % | 15.8 | 397 | 4.6 |
| 4.5 | 75000 | 3.60 | 14.0 | 2.13 | 1.60 | 0.80 | 15.3 % | 8.6 | 1.40 | 0.045 | 0.0098 | 134 | 91 % | 25.2 | 633 | 10.9 |
| 6.0 | 100000 | 4.80 | 33.1 | 5.23 | 3.80 | 1.90 | 15.8 % | 8.7 | 2.53 | 0.045 | 0.0082 | 101 | 88 % | 34.3 | 861 | 19.8 |
| 7.0 | 116667 | 5.60 | 52.5 | 8.40 | 5.97 | 2.98 | 16.0 % | 8.8 | 3.46 | 0.045 | 0.0077 | 87 | 86 % | 40.3 | 1012 | 27.1 |

At 4.5 m/s: tube swings +/-60 mm at the bottom, +/-135 mm mid-height, +/-211 mm at the top; generator swings +/-168 deg. Friction: bushings 0.087 N m, generator drag 0.079 N m (at the hinge).

## Structure

- Survival drag at 25 m/s: 115 N
- Bending moment at tube base 57 N m, at hinge 103 N m
- Glass-skin stress at tube base 23.4 MPa (bare foam would see 0.39 MPa, about its strength)
- Neck 25x23 mm carbon tube stress 238 MPa
- Three 4 mm carbon rods (first chat version) would buckle at 78 N; their load is 110 N at 10 m/s and 689 N at 25 m/s
- Hinge bushing load at 25 m/s: 1034 N each
- Swing cycles per year at 30 % duty: 3.1e+07

## Annual energy (very rough)

Rayleigh wind at hub height, tuning band 3.0-7.0 m/s +/-20 %, 50 % of in-band time locked on. Low case = 0.5 x central.

| Site mean wind | Low (kWh/yr) | Central (kWh/yr) |
|---|---|---|
| 3.5 m/s | 2.7 | 5.4 |
| 4.5 m/s | 4.2 | 8.4 |
| 5.5 m/s | 4.8 | 9.6 |

