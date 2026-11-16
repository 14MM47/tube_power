# Lantern G optimisation grids

Every design point evaluated by `tools/galloping_calc.py sweep`, passing or not. All values are model estimates.

Every design must:
- generate without a gap from 10 m/s up to the 40 m/s cut-out;
- reach its 20 W rating by 25 m/s and hold it to 40 m/s;
- survive 45 m/s feathered and braked.

Designs that pass are ranked by central-case yearly energy at a 4.5 m/s-mean site. The neck tube is the lightest standard carbon tube that survives the storm and whose bending mode clears 1.5 × the top spring frequency.

| File | Rows | Grid |
|---|---|---|
| `grid-wide.csv` | 4,320 | D 200–325 mm (25 mm steps); neck 0–800 mm (200 mm); end plates 1.5, 1.75, 2.0 × D; panels xps5, xps6-storm, xps10-storm, corflute4; pulley 10, 12, 16 teeth; spring top 4 Hz; generators 5208 and 8108; hubs 500 and 800 N·m |
| `grid-fine.csv` | 960 | D 300–330 mm (10 mm); neck 400–800 mm (100 mm); plates 1.75, 2.0; panels xps6-storm, xps10-storm; pulley 10, 12, 14, 16 teeth; spring top 3, 4, 6 Hz; generator 8108; hub 800 N·m |

```bash
python3 tools/galloping_calc.py sweep --D-min 0.2 --D-max 0.325 --D-step 0.025 --neck-min 0 --neck-max 0.8 --neck-step 0.2 --plate-min 1.5 --plate-max 2.0 --plate-step 0.25 --teeth 10,12,16 --ftop 4 --hubs 500,800 --csv designs/lantern-330-g/calculator-output/grid/grid-wide.csv
```

```bash
python3 tools/galloping_calc.py sweep --D-min 0.3 --D-max 0.33 --D-step 0.01 --neck-min 0.4 --neck-max 0.8 --neck-step 0.1 --plate-min 1.75 --plate-max 2.0 --plate-step 0.25 --shells xps6-storm,xps10-storm --teeth 10,12,14,16 --ftop 3,4,6 --gens 8108 --hubs 800 --csv designs/lantern-330-g/calculator-output/grid/grid-fine.csv
```

The sweep uses all CPU cores (`--workers` to change); the wide grid takes about 10 minutes on four.

## Columns

| Column | Meaning |
|---|---|
| `rank` | Rank among passing designs by `annual_kWh`; blank if the design fails |
| `passes`, `failed_limits` | `survival` (fails before 45 m/s feathered), `stops before cut-out` (no output somewhere between 10 and 40 m/s), `does not hold rating` (below 95% of 20 W somewhere above the wind where it first reaches it, or not reached by 25 m/s), `aspect ratio`, `height`, `spring range` |
| `D_mm`, `neck_mm` | Prism face width; hinge to prism bottom |
| `plate_ratio`, `plate_mm` | End-plate side ÷ face width; end-plate side |
| `shell`, `shell_kg_m2` | Panel construction and its areal mass |
| `generator`, `pulley_teeth`, `gear_ratio` | Generator preset; GT2 pulley teeth; ratio from a 100 mm arc |
| `f_spring_top_Hz` | Swing frequency with the spring carriage furthest out |
| `neck_tube`, `total_height_m` | Carbon neck, outside × inside mm; prism plus neck |
| `annual_kWh`, `annual_low_kWh`, `site_mean_wind`, `annual_6_kWh` | Yearly energy (Rayleigh wind, 80% of model output achieved) at the ranking site and at a 6 m/s site; low case is half |
| `p_elec_*_W` | Electrical output at 4.5, 7, 10, 15, 20 and 40 m/s |
| `min_p_20_40_W` | Lowest output from 20 to 40 m/s |
| `cut_in_ms`, `generates_to_ms` | Lowest wind making more than 10 mW; highest wind reached without a gap (2.5 m/s steps) |
| `rated_W`, `hub_Nm` | Power rating; hub moment rating |
| `survival_ms`, `survival_limit` | Survival wind feathered and braked, and the part that limits it |
| `swinging_mass_kg`, `inertia_total_kgm2` | Including the pitch drive; inertia including air and the generator rotor |
| `f_min_Hz`, `neck_mode_Hz`, `spring_rate_N_mm` | Lowest spring frequency; neck-and-prism bending frequency; each of the two springs |
