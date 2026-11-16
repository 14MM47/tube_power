# Full optimisation grids

Every design point evaluated by the Lantern optimiser, in grid order, including points that fail a limit. All values are model estimates.

There are two grids for each survival requirement:
- **25 m/s** grids use configuration B's fixed hardware: hub built for 150 N·m, 12 mm axle with bushings 150 mm apart, 0.15 kg hub.
- **40 m/s** grids use configuration C's: hub built for 350 N·m, 16 mm axle with bushings 200 mm apart, 0.30 kg hub.

In every grid the end discs are built like the shell, and the neck tube is sized automatically: the lightest standard carbon tube that survives the requirement and the swing fatigue.

| File | Rows | Survival requirement | Grid |
|---|---|---|---|
| `grid-wide-25.csv` | 28,800 | 25 m/s | D 100–400 mm (20 mm steps); neck 0–800 mm (100 mm); disc ratio 1.0–2.4 (0.2); five shells; pulley 10, 12, 16, 20, 24 teeth |
| `grid-wide-40.csv` | 28,800 | 40 m/s | as above |
| `grid-fine-25.csv` | 22,440 | 25 m/s | D 200–300 mm (10 mm); neck 0–800 mm (50 mm); disc ratio 1.4–2.4 (0.2); five shells; pulley 10, 12, 16, 20 teeth |
| `grid-fine-40.csv` | 22,440 | 40 m/s | as above |

| Grid | Designs that pass | Best design | Electrical at 4.5 m/s | Yearly energy, 4.5 m/s site |
|---|---|---|---|---|
| Wide, 25 m/s | 5,743 | 240 mm, 800 mm neck, 2.0× discs, 3 mm sandwich, 10 teeth | 1.96 W | 9.0 kWh |
| Fine, 25 m/s | 6,440 | 250 mm, 800 mm neck, 2.0× discs, 3 mm sandwich, 10 teeth | 2.05 W | 9.4 kWh |
| Wide, 40 m/s | 1,767 | 240 mm, 700 mm neck, 2.0× discs, storm shell, 10 teeth | 1.81 W | 8.4 kWh |
| Fine, 40 m/s | 1,597 | 250 mm, 650 mm neck, 2.0× discs, storm shell, 10 teeth | 1.87 W | 8.7 kWh |

**Shell constructions:**

| Shell | Areal mass | Construction |
|---|---|---|
| `xps2-single` | 0.124 kg/m² | 2 mm foam, outer glass skin only |
| `xps3-single` | 0.161 kg/m² | 3 mm foam, outer glass skin only |
| `xps3-sandwich` | 0.211 kg/m² | 3 mm foam, glass both faces (configuration B) |
| `xps5-sandwich` | 0.285 kg/m² | 5 mm foam, glass both faces |
| `xps5-storm` | 0.315 kg/m² | 5 mm foam, glass both faces, outer skin built up near the base (configuration C) |

To regenerate the grids (each takes a few minutes):

```bash
python3 tools/lantern_calc.py sweep --csv designs/lantern-250/calculator-output/grid/grid-wide-25.csv
```

```bash
python3 tools/lantern_calc.py sweep --config C --csv designs/lantern-250/calculator-output/grid/grid-wide-40.csv
```

```bash
python3 tools/lantern_calc.py sweep --D-min 0.20 --D-max 0.30 --D-step 0.01 --neck-step 0.05 --disc-min 1.4 --teeth 10,12,16,20 --csv designs/lantern-250/calculator-output/grid/grid-fine-25.csv
```

```bash
python3 tools/lantern_calc.py sweep --config C --D-min 0.20 --D-max 0.30 --D-step 0.01 --neck-step 0.05 --disc-min 1.4 --teeth 10,12,16,20 --csv designs/lantern-250/calculator-output/grid/grid-fine-40.csv
```

## Columns

Values marked "4.5" are at a 4.5 m/s wind, locked on, at the model's optimum generator load.

| Column | Meaning |
|---|---|
| `rank` | Rank among passing designs by `p_elec_4p5_W`; blank if the design fails a limit |
| `passes` | `yes` if every limit is met |
| `failed_limits` | Which limits fail: `Reynolds` (Re > 120,000 at 7 m/s), `survival` (fails before the required storm wind, parked and braked), `operating loads` (neck fatigue or peak, skin, voltage or generator heat over the limit while swinging), `height`, `generator too weak` (cannot provide the optimum damping) |
| `D_mm`, `neck_mm` | Tube diameter; hinge to tube bottom |
| `disc_ratio`, `disc_dia_mm` | End-disc diameter ÷ tube diameter (1.0 = no discs); disc diameter |
| `shell`, `shell_kg_m2` | Shell construction and its areal mass |
| `pulley_teeth`, `gear_ratio` | GT2 pulley on the generator; resulting ratio from a 100 mm arc |
| `neck_tube` | Carbon neck tube chosen, outside × inside diameter in mm |
| `total_height_m` | Tube plus neck |
| `p_elec_4p5_W`, `p_elec_low_4p5_W` | Electrical power, central and low case (half) |
| `p_mech_4p5_W`, `eta_mech_4p5` | Mechanical power and capture efficiency against wind through D × L |
| `annual_kWh`, `annual_low_kWh`, `site_mean_wind` | Yearly energy, central and low case, for a Rayleigh site with this mean wind, using the operating modes (tracking to 7 m/s, capped to 8 m/s, then braked) |
| `cut_in_ms` | Lowest wind at which it starts (with kick-start) and makes more than 10 mW |
| `rated_W`, `brake_ms` | Power cap (the output at 7 m/s) and brake wind speed |
| `survival_ms`, `survival_limit` | Highest wind it survives parked and braked, and the part that limits it (neck, skin, wall, discs or hub) |
| `mass_ratio` | Structural inertia ÷ displaced-air inertia about the hinge |
| `inertia_total_kgm2`, `swinging_mass_kg` | Including added air and the generator rotor seen through the belt |
| `swing_deg_4p5`, `top_swing_mm_4p5` | Hinge swing amplitude; swing at the top of the tube |
| `peak_torque_4p5_Nm`, `top_accel_4p5_g` | Peak harvesting torque at the hinge; top-of-tube acceleration |
| `parasitic_zeta_4p5` | Damping ratio from friction and losses |
| `spring_rate_N_mm` | Each of the two tuning springs, for a 2–7 m/s range over a 140 mm carriage |
| `circuit_R_4p5_ohm`, `copper_eff_4p5`, `emf_peak_4p5_V`, `gen_peak_rpm_4p5` | Generator operating point |
| `Re_at_Umax` | Reynolds number at 7 m/s |
| `max_neck_fatigue_util` | Highest neck fatigue utilisation while swinging (1.0 = at the allowable) |
| `storm_hinge_moment_Nm` | Drag moment at the hinge at the survival requirement |

Failing designs still have their output computed, so you can see what each limit costs. The end-disc benefit comes from an assumed end-loss model, and every figure from the models in [../../physics.md](../../physics.md). Treat the ranking as a guide to what to test.
