# Lantern power curve, 1-40 m/s

Model potential: the model's output if the tube stayed tuned and locked on with the best generator load and nothing failed (not achievable). Within limits: the most the machine can deliver with every part within its limits, retuning as far as the neck's bending mode allows and riding the lock-on tail beyond that. As designed: the default control (track to 7 m/s, cap to 8 m/s, brake above).

- Neck-tube bending mode about 16.0 Hz, so the swing must stay below 10.6 Hz: retuning is possible up to 13.3 m/s
- As designed: generates 1.6-8.0 m/s, peak 6.97 W, braked above
- Kept generating within every limit: generates 1.8-11.0 m/s, peak 26.30 W at 11 m/s; nothing above 12.0 m/s
- Yearly energy, central case (kWh): 3.5 m/s site: as designed 5.9, within limits 7.2; 4.5 m/s site: as designed 8.5, within limits 14.0; 5.5 m/s site: as designed 9.2, within limits 20.3; 6.5 m/s site: as designed 8.9, within limits 24.1

| Wind (m/s) | Re | Flow | Wind through tube (W) | Model potential (W) | Within limits (W) | Within limits: what governs | As designed (W) | As designed: mode |
|---|---|---|---|---|---|---|---|---|
| 1 | 16,667 | tested | 0.2 | 0.00 | 0.00 | idle | 0.00 | idle |
| 2 | 33,333 | tested | 1.2 | 0.10 | 0.11 | unconstrained | 0.10 | tracking |
| 3 | 50,000 | tested | 4.1 | 0.49 | 0.50 | unconstrained | 0.49 | tracking |
| 4 | 66,667 | tested | 9.8 | 1.27 | 1.28 | unconstrained | 1.27 | tracking |
| 5 | 83,333 | tested | 19.1 | 2.54 | 2.57 | unconstrained | 2.54 | tracking |
| 6 | 100,000 | tested | 33.1 | 4.41 | 4.46 | unconstrained | 4.41 | tracking |
| 7 | 116,667 | tested | 52.5 | 6.97 | 7.06 | unconstrained | 6.97 | tracking |
| 8 | 133,333 | beyond tested | 78.4 | 10.31 | 10.45 | unconstrained | 0.00 | braked |
| 9 | 150,000 | beyond tested | 111.6 | 14.49 | 14.72 | unconstrained | 0.00 | braked |
| 10 | 166,667 | beyond tested | 153.1 | 19.58 | 19.99 | unconstrained | 0.00 | braked |
| 11 | 183,333 | beyond tested | 203.8 | 25.64 | 26.30 | unconstrained | 0.00 | braked |
| 12 | 200,000 | beyond tested | 264.6 | 32.71 | 0.00 | braked (generator heat) | 0.00 | braked |
| 13 | 216,667 | drag crisis | 336.4 | 40.82 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 14 | 233,333 | drag crisis | 420.2 | 50.02 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 15 | 250,000 | drag crisis | 516.8 | 60.30 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 16 | 266,667 | drag crisis | 627.2 | 71.70 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 17 | 283,333 | drag crisis | 752.3 | 84.19 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 18 | 300,000 | drag crisis | 893.0 | 97.78 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 19 | 316,667 | drag crisis | 1,050.3 | 112.44 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 20 | 333,333 | drag crisis | 1,225.0 | 128.15 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 21 | 350,000 | drag crisis | 1,418.1 | 144.88 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 22 | 366,667 | drag crisis | 1,630.5 | 162.56 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 23 | 383,333 | drag crisis | 1,863.1 | 181.16 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 24 | 400,000 | drag crisis | 2,116.8 | 200.60 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 25 | 416,667 | drag crisis | 2,392.6 | 220.81 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 26 | 433,333 | drag crisis | 2,691.3 | 241.71 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 27 | 450,000 | drag crisis | 3,014.0 | 263.20 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 28 | 466,667 | drag crisis | 3,361.4 | 285.19 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 29 | 483,333 | drag crisis | 3,734.6 | 307.56 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 30 | 500,000 | drag crisis | 4,134.4 | 330.20 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 31 | 516,667 | drag crisis | 4,561.7 | 352.97 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 32 | 533,333 | drag crisis | 5,017.6 | 375.74 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 33 | 550,000 | drag crisis | 5,502.9 | 398.35 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 34 | 566,667 | drag crisis | 6,018.4 | 420.66 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 35 | 583,333 | drag crisis | 6,565.2 | 442.49 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 36 | 600,000 | drag crisis | 7,144.2 | 463.68 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 37 | 616,667 | drag crisis | 7,756.2 | 484.03 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 38 | 633,333 | drag crisis | 8,402.3 | 503.36 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 39 | 650,000 | drag crisis | 9,083.2 | 521.45 | 0.00 | braked (drag crisis) | 0.00 | braked |
| 40 | 666,667 | drag crisis | 9,800.0 | 538.11 | 0.00 | braked (drag crisis) | 0.00 | braked |
