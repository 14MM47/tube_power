# Lantern calculator report

Tube 250 mm x 1000 mm, neck 800 mm, end discs 500 mm, shell 0.161 kg/m^2, height/diameter 4.0

Constraint check: all pass

## Masses (kg)

| Part | Mass |
|---|---|
| Tube shell incl. rings and seams | 0.146 |
| End discs, each | 0.031 |
| Bottom spider | 0.015 |
| Neck tube | 0.113 |
| Hub, axle, carriage, belt arc | 0.150 |
| **Total swinging mass** | **0.487** |

## Inertia about the hinge (kg m^2)

| Part | Inertia |
|---|---|
| shell | 0.2597 |
| discs | 0.1229 |
| spider | 0.0096 |
| neck | 0.0241 |
| hub | 0.0007 |
| generator | 0.0411 |
| Structural total | 0.4581 |
| Air moving with the tube | 0.1066 |
| **Total** | **0.5648** |
| Mass ratio (structural / displaced air) | 4.30 |

- Gear ratio: 26.2:1 (100 mm arc to 12-tooth GT2 pulley)
- Mode-shape factor gamma: 1.244
- Effective length after end losses: 1.000 m
- Gravity (destabilising) stiffness: 3.23 N m/rad

## Tuning

Two opposing springs, each 14.82 N/mm.

| Wind (m/s) | Tune f_n (Hz) | Stiffness (N m/rad) | Carriage below hinge (mm) |
|---|---|---|---|
| 3.0 | 2.18 | 109.4 | 60.7 |
| 4.0 | 2.91 | 191.9 | 80.5 |
| 4.5 | 3.27 | 242.0 | 90.4 |
| 5.0 | 3.64 | 298.1 | 100.3 |
| 6.0 | 4.36 | 427.8 | 120.1 |
| 7.0 | 5.09 | 581.1 | 140.0 |

Carriage moves about 19.8 mm per 1 m/s between 4 and 6 m/s.

## Operating points (locked on, model central case)

| Wind | Re | Swing f (Hz) | Wind power (W) | Mech (W) | Elec (W) | Elec low case (W) | Mech eff | Swing (deg) | Peak torque (N m) | Gen zeta | Parasitic zeta | Circuit R (ohm) | Copper eff | EMF peak (V) | Gen peak rpm | Top accel (g) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 3.0 | 50000 | 2.40 | 4.1 | 0.75 | 0.57 | 0.29 | 18.1 % | 6.2 | 0.91 | 0.040 | 0.0115 | 178 | 93 % | 16.3 | 410 | 4.5 |
| 4.5 | 75000 | 3.60 | 14.0 | 2.76 | 2.05 | 1.03 | 19.8 % | 6.6 | 2.13 | 0.040 | 0.0079 | 120 | 90 % | 25.8 | 648 | 10.8 |
| 6.0 | 100000 | 4.80 | 33.1 | 6.75 | 4.83 | 2.42 | 20.4 % | 6.7 | 3.84 | 0.039 | 0.0067 | 91 | 87 % | 35.0 | 880 | 19.5 |
| 7.0 | 116667 | 5.60 | 52.5 | 10.83 | 7.55 | 3.78 | 20.6 % | 6.7 | 5.24 | 0.039 | 0.0063 | 78 | 85 % | 41.1 | 1032 | 26.7 |

At 4.5 m/s: tube swings +/-92 mm at the bottom, +/-150 mm mid-height, +/-207 mm at the top; generator swings +/-172 deg. Friction: bushings 0.101 N m, generator drag 0.105 N m (at the hinge).

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
| 3.5 m/s | 3.5 | 6.9 |
| 4.5 m/s | 5.3 | 10.7 |
| 5.5 m/s | 6.1 | 12.2 |

