# Lantern design-grid page

The source of the interactive page published as the [Lantern Design Grid](https://claude.ai/artifact/7coCWJAdK3jhA8j6H4RN1b) (private until its owner shares it). Everything on it comes from this repository: the calculators in `tools/` and the grid CSVs in `designs/lantern-250/calculator-output/grid/`.

**What it shows:**
- **Electrical power from 1 to 40 m/s.** The curves cover Lantern 250-A, B and C (vortex shedding), 330-G and 330-GH (galloping), and the best design in each Lantern 250 grid. A "Compare with" menu overlays any second design. The table and hover readout give the mode and the limit that governs at each wind speed.
- **Every point of the four Lantern 250 optimisation grids.** These are shown as a heat map and a sortable table, with filters for shell, end discs, pulley and neck, and the best passing design highlighted.

**Building it:**

```bash
python3 tools/grid_page/build_page.py
```

This writes `build/grid-page/`:
- `lantern-grid.html`, with the fine 25 m/s grid and the power curves inlined;
- `grid-fine-40.json`, `grid-wide-25.json` and `grid-wide-40.json`, which the page loads from beside it;
- `curves.json`, kept for reference.

Serve the folder rather than opening the file directly, so the browser allows the JSON loads:

```bash
python3 -m http.server -d build/grid-page 8000
```

Then open http://localhost:8000/lantern-grid.html.

| File | Role |
|---|---|
| `lantern-grid.src.html` | Page template: markup, styles and script. `__FINE25__` and `__CURVES__` are replaced with data at build time |
| `build_page.py` | Converts the grid CSVs to compact column JSON, computes the power curves with `lantern_calc.py` and `galloping_calc.py`, and inlines them |

Rebuild after changing a calculator or regenerating a grid; `build/` is not committed. The page uses no external scripts and follows light and dark mode.
