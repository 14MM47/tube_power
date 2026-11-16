# Lantern power curve, 1-40 m/s

Model potential: the model's output if the tube stayed tuned and locked on with the best generator load and nothing failed (not achievable). Within limits: the most the machine can deliver with every part within its limits, retuning as far as the neck's bending mode allows and riding the lock-on tail beyond that. As designed: the default control (track to 7 m/s, cap to 8 m/s, brake above).

- Neck-tube bending mode about 14.5 Hz, so the swing must stay below 9.6 Hz: retuning is possible up to 12.0 m/s
- As designed: generates 1.6-8.0 m/s, peak 7.38 W, braked above
- Kept generating within every limit: generates 1.8-10.8 m/s, peak 23.58 W at 10.5 m/s; nothing above 12.0 m/s
- Yearly energy, central case (kWh): 3.5 m/s site: as designed 6.4, within limits 7.7; 4.5 m/s site: as designed 9.1, within limits 14.7; 5.5 m/s site: as designed 9.9, within limits 20.8; 6.5 m/s site: as designed 9.5, within limits 24.3

| Wind (m/s) | Re | Flow | Wind through tube (W) | Model potential (W) | Within limits (W) | Within limits: what governs | As designed (W) | As designed: mode |
|---|---|---|---|---|---|---|---|---|
| 1 | 16,667 | tested | 0.2 | 0.00 | 0.00 | idle | 0.00 | idle |
| 2 | 33,333 | tested | 1.2 | 0.13 | 0.14 | unconstrained | 0.13 | tracking |
| 3 | 50,000 | tested | 4.1 | 0.56 | 0.57 | unconstrained | 0.56 | tracking |
| 4 | 66,667 | tested | 9.8 | 1.40 | 1.41 | unconstrained | 1.40 | tracking |
| 5 | 83,333 | tested | 19.1 | 2.75 | 2.79 | unconstrained | 2.75 | tracking |
| 6 | 100,000 | tested | 33.1 | 4.72 | 4.79 | unconstrained | 4.72 | tracking |
| 7 | 116,667 | tested | 52.5 | 7.38 | 7.53 | unconstrained | 7.38 | tracking |
| 8 | 133,333 | beyond tested | 78.4 | 10.81 | 11.10 | unconstrained | 0.00 | braked |
| 9 | 150,000 | beyond tested | 111.6 | 15.04 | 15.56 | unconstrained | 0.00 | braked |
| 10 | 166,667 | beyond tested | 153.1 | 20.14 | 20.50 | unconstrained | 0.00 | braked |
| 11 | 183,333 | beyond tested | 203.8 | 26.11 | 0.00 | braked (generator heat) | 0.00 | braked |
| 12 | 200,000 | beyond tested | 264.6 | 32.98 | 0.00 | braked (generator heat) | 0.00 | braked |
| 13 | 216,667 | drag crisis | 336.4 | 40.73 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 14 | 233,333 | drag crisis | 420.2 | 49.36 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 15 | 250,000 | drag crisis | 516.8 | 58.84 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 16 | 266,667 | drag crisis | 627.2 | 69.12 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 17 | 283,333 | drag crisis | 752.3 | 80.15 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 18 | 300,000 | drag crisis | 893.0 | 91.85 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 19 | 316,667 | drag crisis | 1,050.3 | 104.15 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 20 | 333,333 | drag crisis | 1,225.0 | 116.93 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 21 | 350,000 | drag crisis | 1,418.1 | 130.10 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 22 | 366,667 | drag crisis | 1,630.5 | 143.52 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 23 | 383,333 | drag crisis | 1,863.1 | 157.06 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 24 | 400,000 | drag crisis | 2,116.8 | 170.56 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 25 | 416,667 | drag crisis | 2,392.6 | 183.85 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 26 | 433,333 | drag crisis | 2,691.3 | 196.75 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 27 | 450,000 | drag crisis | 3,014.0 | 209.07 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 28 | 466,667 | drag crisis | 3,361.4 | 220.60 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 29 | 483,333 | drag crisis | 3,734.6 | 231.12 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 30 | 500,000 | drag crisis | 4,134.4 | 240.39 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 31 | 516,667 | drag crisis | 4,561.7 | 248.16 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 32 | 533,333 | drag crisis | 5,017.6 | 254.16 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 33 | 550,000 | drag crisis | 5,502.9 | 258.12 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 34 | 566,667 | drag crisis | 6,018.4 | 259.75 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 35 | 583,333 | drag crisis | 6,565.2 | 258.74 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 36 | 600,000 | drag crisis | 7,144.2 | 254.78 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 37 | 616,667 | drag crisis | 7,756.2 | 247.52 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 38 | 633,333 | drag crisis | 8,402.3 | 236.63 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 39 | 650,000 | drag crisis | 9,083.2 | 221.73 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 40 | 666,667 | drag crisis | 9,800.0 | 202.47 | 0.00 | braked (drag crisis) | 0.00 | braked |
