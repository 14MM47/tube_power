# Lantern 330-G calculator output

Produced by [`tools/galloping_calc.py`](../../../tools/galloping_calc.py) with the defaults (Lantern 330-G). All values are model estimates; see [../physics.md](../physics.md).

| File | Contents | Command |
|---|---|---|
| `report-330G.md` | Full report: masses, inertia, envelope, power curve, structure, yearly energy | `python3 tools/galloping_calc.py` |
| `envelope-330G.md`, `.csv` | Mode, pitch, swing, frequency, output and every utilisation from 0.5 to 45 m/s in 0.5 m/s steps | `python3 tools/galloping_calc.py envelope --from 0.5 --step 0.5 --to 45 --csv envelope-330G.csv` |
| `curve-330G.md`, `.csv` | Electrical power from 0.5 to 40 m/s, with Lantern 250-B and 250-C kept generating for comparison | `python3 tools/galloping_calc.py curve --compare --from 0.5 --step 0.5 --to 40 --csv curve-330G.csv` |
| `sweep-wide.md` | Wide grid search, 4,320 designs, hubs 500 and 800 N·m | see [grid/README.md](grid/README.md) |
| `sweep-fine.md` | Fine grid search around the optimum, 960 designs | see [grid/README.md](grid/README.md) |
| `sweep-relaxed.md` | Sensitivity: aspect ratio down to 2.5, hub up to 1,200 N·m | `python3 tools/galloping_calc.py sweep --AR_min 2.5 --D-min 0.30 --D-max 0.40 --D-step 0.025 --neck-min 0.4 --neck-max 0.8 --neck-step 0.2 --plate-min 2.0 --plate-max 2.0 --shells xps10-storm --teeth 10,12 --ftop 4 --gens 8108 --hubs 800,1200` |
| [`grid/`](grid/) | Every grid point of both searches as CSV | |
