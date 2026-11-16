# Full optimisation grids

Every design point evaluated by the Lantern optimiser, in grid order, including points that fail a limit. Fixed parameters are those of configuration B (see [../../README.md](../../README.md)). All values are model estimates.

| File | Rows | Grid |
|---|---|---|
| `grid-wide.csv` | 20,736 | D 100–400 mm (20 mm steps); neck 0–800 mm (100 mm); disc ratio 1.0–2.4 (0.2); shells xps2, xps3, xps5 (glass-skinned); pulley 12, 16, 20, 24, 30, 36 teeth |
| `grid-fine.csv` | 30,855 | D 200–300 mm (10 mm); neck 0–800 mm (50 mm); disc ratio 1.4–2.4 (0.1); same shells; pulley 10, 12, 14, 16, 20 teeth |

To regenerate them:

```bash
python3 tools/lantern_calc.py sweep --csv designs/lantern-250/calculator-output/grid/grid-wide.csv
```

```bash
python3 tools/lantern_calc.py sweep --D-min 0.20 --D-max 0.30 --D-step 0.01 --neck-step 0.05 --disc-min 1.4 --disc-step 0.1 --teeth 10,12,14,16,20 --csv designs/lantern-250/calculator-output/grid/grid-fine.csv
```

## Columns

Values marked "4.5" are at a 4.5 m/s wind, locked on, at the model's optimum generator load.

| Column | Meaning |
|---|---|
| `rank` | Rank among passing designs by `p_elec_4p5_W`; blank if the design fails a limit |
| `passes` | `yes` if every limit is met |
| `failed_limits` | Which limits fail: `Reynolds` (Re > 120,000 at 7 m/s), `hinge moment` (> 150 N·m at 25 m/s), `skin stress` (> 40 MPa), `height`, `generator too weak` (cannot provide the optimum damping) |
| `D_mm`, `neck_mm` | Tube diameter; hinge to tube bottom |
| `disc_ratio`, `disc_dia_mm` | End-disc diameter ÷ tube diameter (1.0 = no discs); disc diameter |
| `shell`, `shell_kg_m2` | Shell option and its areal mass |
| `pulley_teeth`, `gear_ratio` | GT2 pulley on the generator; resulting ratio from a 100 mm arc |
| `total_height_m` | Tube plus neck |
| `p_elec_4p5_W`, `p_elec_low_4p5_W` | Electrical power, central and low case (half) |
| `p_mech_4p5_W`, `eta_mech_4p5` | Mechanical power and capture efficiency against wind through D × L |
| `annual_kWh`, `annual_low_kWh`, `site_mean_wind` | Yearly energy, central and low case, for a Rayleigh site with this mean wind |
| `mass_ratio` | Structural inertia ÷ displaced-air inertia about the hinge |
| `inertia_total_kgm2`, `swinging_mass_kg` | Including added air and the generator rotor seen through the belt |
| `swing_deg_4p5`, `top_swing_mm_4p5` | Hinge swing amplitude; swing at the top of the tube |
| `peak_torque_4p5_Nm`, `top_accel_4p5_g` | Peak harvesting torque at the hinge; top-of-tube acceleration |
| `parasitic_zeta_4p5` | Damping ratio from friction and losses |
| `spring_rate_N_mm` | Each of the two tuning springs, for a 3–7 m/s range over a 140 mm carriage |
| `circuit_R_4p5_ohm`, `copper_eff_4p5`, `emf_peak_4p5_V`, `gen_peak_rpm_4p5` | Generator operating point |
| `Re_at_Umax` | Reynolds number at 7 m/s |
| `storm_hinge_moment_Nm`, `skin_stress_MPa` | 25 m/s survival checks |

Failing designs still have their output computed, so you can see what each limit costs. The end-disc benefit comes from an assumed end-loss model, and every figure from the models in [../../physics.md](../../physics.md). Treat the ranking as a guide to what to test.
