# Lantern power curve, 1-40 m/s

Model potential: the model's output if the tube stayed tuned and locked on with the best generator load and nothing failed (not achievable). Within limits: the most the machine can deliver with every part within its limits, retuning as far as the neck's bending mode allows and riding the lock-on tail beyond that. As designed: the default control (track to 7 m/s, cap to 8 m/s, brake above).

- Neck-tube bending mode about 13.6 Hz, so the swing must stay below 9.1 Hz: retuning is possible up to 11.4 m/s
- As designed: generates 1.6-8.0 m/s, peak 5.86 W, braked above
- Kept generating within every limit: generates 1.8-9.8 m/s, peak 15.08 W at 9.75 m/s; nothing above 12.0 m/s
- Yearly energy, central case (kWh): 3.5 m/s site: as designed 5.1, within limits 6.0; 4.5 m/s site: as designed 7.2, within limits 10.6; 5.5 m/s site: as designed 7.8, within limits 13.8; 6.5 m/s site: as designed 7.5, within limits 15.1

| Wind (m/s) | Re | Flow | Wind through tube (W) | Model potential (W) | Within limits (W) | Within limits: what governs | As designed (W) | As designed: mode |
|---|---|---|---|---|---|---|---|---|
| 1 | 16,667 | tested | 0.2 | 0.00 | 0.00 | idle | 0.00 | idle |
| 2 | 33,333 | tested | 1.2 | 0.10 | 0.10 | unconstrained | 0.10 | tracking |
| 3 | 50,000 | tested | 4.1 | 0.43 | 0.44 | unconstrained | 0.43 | tracking |
| 4 | 66,667 | tested | 9.8 | 1.09 | 1.10 | unconstrained | 1.09 | tracking |
| 5 | 83,333 | tested | 19.1 | 2.17 | 2.19 | unconstrained | 2.17 | tracking |
| 6 | 100,000 | tested | 33.1 | 3.73 | 3.78 | unconstrained | 3.73 | tracking |
| 7 | 116,667 | tested | 52.5 | 5.86 | 5.95 | unconstrained | 5.86 | tracking |
| 8 | 133,333 | beyond tested | 78.4 | 8.62 | 8.80 | unconstrained | 0.00 | braked |
| 9 | 150,000 | beyond tested | 111.6 | 12.04 | 12.37 | unconstrained | 0.00 | braked |
| 10 | 166,667 | beyond tested | 153.1 | 16.18 | 0.00 | limited by generator heat | 0.00 | braked |
| 11 | 183,333 | beyond tested | 203.8 | 21.07 | 0.00 | braked (generator heat) | 0.00 | braked |
| 12 | 200,000 | beyond tested | 264.6 | 26.72 | 0.00 | braked (generator heat) | 0.00 | braked |
| 13 | 216,667 | drag crisis | 336.4 | 33.15 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 14 | 233,333 | drag crisis | 420.2 | 40.36 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 15 | 250,000 | drag crisis | 516.8 | 48.34 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 16 | 266,667 | drag crisis | 627.2 | 57.08 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 17 | 283,333 | drag crisis | 752.3 | 66.54 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 18 | 300,000 | drag crisis | 893.0 | 76.69 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 19 | 316,667 | drag crisis | 1,050.3 | 87.49 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 20 | 333,333 | drag crisis | 1,225.0 | 98.87 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 21 | 350,000 | drag crisis | 1,418.1 | 110.78 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 22 | 366,667 | drag crisis | 1,630.5 | 123.14 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 23 | 383,333 | drag crisis | 1,863.1 | 135.85 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 24 | 400,000 | drag crisis | 2,116.8 | 148.83 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 25 | 416,667 | drag crisis | 2,392.6 | 161.98 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 26 | 433,333 | drag crisis | 2,691.3 | 175.17 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 27 | 450,000 | drag crisis | 3,014.0 | 188.28 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 28 | 466,667 | drag crisis | 3,361.4 | 201.19 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 29 | 483,333 | drag crisis | 3,734.6 | 213.74 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 30 | 500,000 | drag crisis | 4,134.4 | 225.79 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 31 | 516,667 | drag crisis | 4,561.7 | 237.17 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 32 | 533,333 | drag crisis | 5,017.6 | 247.71 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 33 | 550,000 | drag crisis | 5,502.9 | 257.23 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 34 | 566,667 | drag crisis | 6,018.4 | 265.53 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 35 | 583,333 | drag crisis | 6,565.2 | 272.42 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 36 | 600,000 | drag crisis | 7,144.2 | 277.68 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 37 | 616,667 | drag crisis | 7,756.2 | 281.10 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 38 | 633,333 | drag crisis | 8,402.3 | 282.43 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 39 | 650,000 | drag crisis | 9,083.2 | 281.45 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 40 | 666,667 | drag crisis | 9,800.0 | 277.91 | 0.00 | braked (drag crisis) | 0.00 | braked |
