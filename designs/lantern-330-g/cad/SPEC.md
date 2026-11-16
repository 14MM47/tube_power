# Lantern 330-G CAD: layout contract

This file is the single source of truth for the 330-G mechanical layout. Every part, printed or not, is placed from the numbers here. If a part needs a number that is not here, add it here first.

- Design being modelled: **Lantern 330-G** ([../README.md](../README.md)): 330 mm square prism, 1,000 mm tall, 600 mm neck, pitch drive, 8108 generator on a 26.2:1 GT2 9 mm belt, ±15° design swing inside ±20° stops.
- 330-GH shares the prism, end plates, head and post. Its differences are listed in section 9, not modelled.
- Units: millimetres, degrees. All numbers not taken from the design documents are **ASSUMED** and listed in section 10 (VERIFY).

## 1. Frames

| Frame | Moves with | Definition |
|---|---|---|
| **A** assembly (= **H**, head) | the yaw head | Origin on the hinge axis, midway between the two hinge bearings. **+X downwind** (the tail vane side; the hinge axle points into the wind along X). **+Z up**. **+Y** completes a right-handed set. Ground is Z = −3000. |
| **S** swinging | the hub, neck and prism | A rotated by the swing angle θ about the X axis through the origin: p_A = R_x(θ) p_S. θ = 0 is upright. Design swing ±15°, rubber stops at ±20°. |
| **P** pitching | the neck and prism | S rotated by the pitch angle β about the neck axis (X = 0, Y = 0, along Z_S): p_S = R_z(β) p_P. β = 0 is face-on (faces normal to X and Y), β = 45° is feathered. Internal stops at −3° and +48°. |

All positions below are in **A at θ = 0, β = 0**. The "Frame" column says which frame the part moves with.

Poses the assembly must render and pass interference checks in: (θ, β) = (0, 0), (+20, 0), (−20, 0), (0, 45), (+15, 10), (−15, 10).

## 2. General arrangement (side view, wind from the left)

```
 Z
1610 ┌──────────────── top end plate 660 sq ───────────────┐
1600   ├──┤ prism 330 sq, panels 600..1600, bulkheads 850 / 1100 / 1350
 850   │  ├ neck top collar (P02) at bulkhead 1; neck tube ends here
 600 ┌─┴──┴──────────── bottom end plate 660 sq ───────────┐  590..600
     │      spider (P01) on the plate, inside the prism
     │   neck: CFRP 50/47, Z 275..850
 275   ┌┴┐ neck-foot insert / shoulder
 250 ┌─┴─┴─┐ pitch housing Ø110, Z 35..265 (cap 250..265)
     │ M  W│ worm, worm wheel, clutch, torsion spring, encoder (P12/P13)
  35 ├─────┴──────────── hub top plate Z 20..35 ───────────┤
   0 ●═══ stub axles, 6005-2RS bearings at X = ±150 in the cheeks
     lever X −71..−59 │ spring carriage, springs ±Y, rollers on reaction plates
     belt arc X 80.5..89.5 (P03), R 99.95 pitch, pulley at Z −128
−128            [GEN 8108] (P05), idlers (P06)
−280 ════ head base plate Z −295..−280 ════  enclosure (P20/P21) at X −355..−185
−307 ── yaw flange ── yaw shaft Ø50 ── yaw housing (post top) ── slip ring (P23)
−3000 ground
```

## 3. Swinging and pitching body (frames S and P)

### 3.1 Prism (frame P)

| Item | Material | Geometry (frame A at β = 0) |
|---|---|---|
| Four panels | GFRP-faced XPS sandwich (10 mm XPS, ~25 g/m² glass tissue in epoxy each face) | Z 600..1600. Panels on the ±X faces: X ∈ [155,165] and [−165,−155], Y ∈ [−165,165]. Panels on the ±Y faces: Y ∈ [155,165] and [−165,−155], X ∈ [−155,155]. Corners glass-taped. |
| Three bulkheads | same sandwich | 310 × 310 × 10, centred, Z ∈ [845,855], [1095,1105], [1345,1355]. Lightening holes: four Ø80 on a 200 mm square pitch. Bulkhead 1 (Z 850) also has a central Ø80 hole for the neck top collar (P02). |
| Two end plates | same sandwich | 660 × 660 × 10, centred. Bottom Z ∈ [590,600] with a central Ø51 hole for the neck. Top Z ∈ [1600,1610]. |
| Neck spider **P01** | printed | On the bottom end plate's top face (Z = 600) inside the prism; grips the neck. Must stay ≥ 5 mm inside the panels' inner faces (|X|, |Y| ≤ 150) and below Z 700. |
| Neck top collar **P02** | printed | Under and through bulkhead 1: socket for the neck's top end, flange bonded to the bulkhead's underside (Z = 845), cap closing the tube. |

### 3.2 Neck (frame P)

| Item | Material | Geometry |
|---|---|---|
| Neck tube | CFRP, roll-wrapped, mostly 0° fibres | OD 50, ID 47, Z 275..850, axis X = Y = 0. Passes through the bottom end plate (Z 590..600). |
| Neck-foot insert and shaft | Aluminium 6082-T6 (one piece) | Insert OD 47 bonded inside the neck, Z 275..335. Shoulder OD 56, Z 265..275. Shaft OD 35 at the bearings, Z 45..265. Bottom end face Z = 45 has a Ø12 × 8 deep bore into which the pitch magnet holder **P13** is pressed; P13's magnet face is at Z = 44. |

### 3.3 Hub and pitch drive (frame S, except where stated)

| Item | Material | Geometry |
|---|---|---|
| Hub top plate | Aluminium 6082-T6 | X ∈ [−135,135], Y ∈ [−60,60], Z ∈ [20,35]. Inside the pitch housing's footprint it has 2 × M3 tapped holes at (X ±32, Y 0) for **P12** and a Ø12 cable hole at (X 0, Y −40). |
| Hub side plates (2) | Aluminium 6082-T6 | X ∈ [−135,−123] and [123,135], Y ∈ [−40,40], Z ∈ [−35,20]; bolted under the top plate. Stub-axle bore at (Y 0, Z 0). |
| Stub axles (2) | Stainless steel 316 | Ø25 on the bearing seat, X ∈ [−172,−123] and [123,172]; Ø30 flange on the side plate's inner face, axial nut outboard of each bearing (X 164..170). The −X stub's end face (X = −172) has 2 × M3 tapped holes at Y = ±8 and carries the hinge magnet cap **P15** (a Ø24 disc, magnet on the axis). |
| Pitch housing tube | Aluminium 6082-T6 | OD 110, ID 100, Z 35..250, axis Z through (0,0). Worm window cut through the +X wall, centred Y = 37, Z = 160, 36 wide (Y) × 30 tall (Z). |
| Pitch housing cap | Aluminium 6082-T6 | Ø110 × 15, Z 250..265; houses the upper bearing. |
| Lower bearing seat | Aluminium 6082-T6 | Ring OD 100 (bonded/pinned in the tube), ID 55, Z 55..67; houses the lower bearing. |
| Pitch bearings (2) | bought, bearing steel | 6907-2RS (35 × 55 × 10): upper Z 252..262, lower Z 56..66. |
| Worm wheel | bought, bronze | Module 1, 60 teeth (pitch Ø60, OD 62), face 10, Z 155..165, rides on the clutch. |
| Worm | bought, steel | Module 1, single start, pitch Ø14 (OD 16), axis along X at (Y 37, Z 160), length 30 at X −15..15; shaft Ø5 continues +X through the window to the gearmotor coupling. |
| EM clutch | bought | Ø60 × 25, Z 170..195, coaxial with the shaft; locks the worm wheel to the shaft when energised. |
| Torsion spring | spring steel | Ø60 coil, Z 90..140, drives the shaft towards β = 45°. |
| Pitch gearmotor | bought (JGA25-370 class, 12 V) | Ø25 gearbox + Ø24.4 motor, axis along X at (Y 37, Z 160), X 62..135 (gearbox face at X = 62, 2 × M3 at ±8.5 mm in Y about the shaft, shaft Ø4 D-cut 12 long). Held by **P11**. |
| Pitch encoder | bought AS5047P breakout (section 6) | Inside the housing under the shaft end; IC top face at Z = 42.5 (1.5 mm below the magnet face). Held by **P12** standing on the hub top plate (Z = 35); lead out through the Ø12 cable hole. |
| Lever | Aluminium 6082-T6 flat bar | X ∈ [−71,−59], Y ∈ [−20,20], Z ∈ [−215,20]; bolted under the top plate with an angle. |
| Linear rail | bought MGN12 rail + MGN12H block | Rail on the lever's −X face: X ∈ [−79,−71], Y ∈ [−6,6], Z ∈ [−175,10]. Block X ∈ [−92,−79]. |
| Spring carriage | Aluminium 6082-T6 | Body X ∈ [−115,−92], Y ∈ [−25,25], 40 tall in Z centred on the spring axis Z = −r, r ∈ [15,140]. Default render r = 80. Holds the T8 nut on the lead-screw axis. |
| Lead screw | bought T8 × 2 mm lead, stainless | Axis (X −104, Y 0), Z −185..5. Top end in a KFL08 flange bearing under the top plate (Z 8..20). |
| Stepper | bought NEMA-17, 48 mm body | Shaft axis (X −104, Y 0) pointing +Z; face at Z = −205, body Z −253..−205; flexible coupler Z −205..−185. Held by **P10** on the lever. |
| Springs (2) | spring steel | Compression, OD 25, axis along ±Y at (X −104, Z −r), from \|Y\| = 25 to the roller fork. ~31 N/mm each (design 30.8), preloaded; free length VERIFY. |
| Spring rods, roller forks (2) | stainless / aluminium | Rod Ø10 from the carriage side face; fork carries a Ø20 × 10 roller (bought cam follower) with its axle at \|Y\| = 140, roller X ∈ [−109,−99], contact at \|Y\| = 150. |
| Stop striker | Aluminium 6082-T6 | X ∈ [−59,−40], Y ∈ [−20,20], Z ∈ [−200,−180], on the lever's +X face. |
| Belt-arc hanger | Aluminium 6082-T6 | X ∈ [95,103], Y ∈ [−30,30], Z ∈ [−45,20], under the top plate. Three M5 tapped holes along X at (Y,Z) = (−20,−35), (20,−35), (0,5). |
| Belt arc **P03** + belt clamps **P04** | printed | Sector about the X axis. Belt centre plane X = 85, belt 9 wide (X 80.5..89.5). Toothed rim with GT2 pitch radius **99.95** (314-tooth circle), sector ±45° about −Z. Web X ∈ [87,95] bolted to the hanger's −X face (X = 95). |

### 3.4 Belt and drive path (frame A)

The belt runs in the X = 85 plane in an omega: tooth side on the arc, off the arc onto two smooth idlers that touch its back, down round the generator pulley (tooth side), back up over the second idler and onto the arc. Belt ends are clamped to the arc by P04 near ±40°.

| Item | Material | Geometry |
|---|---|---|
| Belt | bought GT2, 9 mm, glass-cord neoprene | 2 mm pitch, 1.38 mm thick. |
| Generator pulley | bought aluminium, GT2 12-tooth, 9 mm belt, flanged | Pitch radius 3.82, centre (Y 0, Z −128), on the generator shaft, belt plane X 85. |
| Idlers (2) | bought, smooth flanged GT2 idlers for 9 mm belt (bore 5, contact Ø ~13, flanges Ø ~18) | Centres at about (Y ±15, Z −109); exact positions set by P06's author so the belt back clears the arc and wraps the pulley ≥ 150°. Cantilevered on M5 shoulder bolts from the +X side. |
| Generator | bought 8108-size pancake outrunner (section 6) | Axis along X at (Y 0, Z −128). Rotor can Ø88, X ∈ [48,76]; stator mount face at X = 43 (mounts on **P05**'s +X face with 4 × M3 on a Ø30 PCD); output shaft from the can's +X face to X = 92 carrying the pulley; rear shaft Ø5 protrudes to X = 38 and carries the magnet holder **P08** (magnet face at X = 35.5). |
| Generator mount **P05** | printed | Stands on the base plate (Z = −280), upright X ∈ [35,43], holds the generator face at X = 43. The 4 motor screws and a Ø22 centre clearance hole are in vertical slots (±5 mm) for belt tension. |
| Idler bracket **P06** | printed | Stands on the base plate, upright X ∈ [93,101], top edge an arc of R ≥ 110 about the X axis so the swinging arc and hanger never touch it; carries both idler bolts. |
| Generator encoder mount **P07** | printed | Clamped against P05's −X face (X = 35) by the same 4 motor screws, so it moves with the motor when the belt is tensioned. Holds the encoder board with its IC top face at X = 34.0, facing +X, and covers it. |
| Belt guard **P09** | printed | Fixed to P05 and P06; covers the arc's sweep (R ≤ 106 for ±65° about −Z, i.e. the ±45° sector plus ±20° swing) and the pulley, open at the top for the hanger. |

### 3.5 Hinge (frame A)

| Item | Material | Geometry |
|---|---|---|
| Cheeks (2) | Aluminium 6082-T6, 20 mm | X ∈ [−160,−140] and [140,160], Y ∈ [−160,160], Z ∈ [−280,50]; Ø47 H7 bearing bore at (Y 0, Z 0). |
| Hinge bearings (2) | bought 6005-2RS (25 × 47 × 12) | Centred at X = ±150. |
| Bearing retainers (2) | Aluminium | Rings OD 80, ID 30, 4 thick on the cheeks' outer faces: X ∈ [160,164] and [−164,−160]; 4 × M5 on a Ø64 PCD. |
| Hinge encoder mount **P14** + magnet cap **P15** | printed | P15: Ø24 × 6 disc on the −X stub end face, X ∈ [−178,−172], 2 × M3; magnet face at X = −178.5. P14: a cup bolted with the −X retainer's 4 × M5 (longer bolts, Ø64 PCD), enclosing the stub end, nut and P15, holding the encoder board with its IC top face at X = −180.0 facing +X; cable exit with a grommet. |
| Reaction plates (2) | Aluminium 6082-T6, 10 mm | X ∈ [−125,−85], Y ∈ [150,160] and [−160,−150], Z ∈ [−280,10]; joined to the −X cheek by spacer blocks X ∈ [−140,−125]. |
| Stop posts (2) | Aluminium 30 × 30 × 3 square tube | X ∈ [−58,−32] (26 wide with bumper base), \|Y\| ∈ [99,124], Z ∈ [−280,−150]. |
| End-stop bumpers **P16** (2) | printed TPU 95A | On the posts' inner faces: \|Y\| ∈ [84,99], X ∈ [−56,−34], Z ∈ [−195,−160]. The striker's edge touches them at θ = ±20° (it reaches \|Y\| = 83.8 at Z ≈ −172). |

### 3.6 Head, yaw and post (frame A)

| Item | Material | Geometry |
|---|---|---|
| Head base plate | Aluminium 6082-T6, 15 mm | X ∈ [−360,230], Y ∈ [−170,170], Z ∈ [−295,−280]. |
| Yaw flange | Steel S355, galvanised | Ø160 × 12, Z −307..−295, bolted under the base plate (6 × M10). |
| Yaw shaft | Steel S355, galvanised | Tube OD 50, ID 38, Z −640..−307, welded to the flange. Hollow for cables. |
| Yaw housing (post top) | Steel S355, galvanised | Tube OD 114.3 × 6, Z −560..−320, flanged to the post at Z −560. Bearing seats inside. |
| Yaw bearings (2) | bought tapered roller 32010 (50 × 80 × 20) | Z −345..−325 and Z −545..−525. |
| Slip ring | bought capsule, 6 channels × 2 A minimum (section 6) | Rotor clamped to the yaw shaft's bottom end; stator held by **P23** inside the post bore, Z −700..−640. |
| Slip-ring holder **P23** | printed | Fits the post bore (ID 102.3), Z −720..−640; held by one M6 bolt through the post wall; locates the stator flange; guides cables down. |
| Post | Steel S355, galvanised | Tube OD 114.3 × 6, Z −2985..−560. Base plate 300 × 300 × 15 at Z −3000..−2985. Guy collar at Z −1000 (ring OD 140 × 20, three lugs). Guys are not modelled. |
| Tail boom | Aluminium 6063-T6 tube | OD 40 × 2, axis Y 0, Z −260, X 150..920; two U-bolt saddles on the base plate at X 170 and 215. |
| Tail vane | PP twin-wall (corflute) 4 mm (or 1.5 mm aluminium) | Two halves in the Y = 0 plane (Y ∈ [−2,2]), X ∈ [480,900]: upper Z ∈ [−239.5,−140], lower Z ∈ [−380,−280.5]; the boom runs in the 41 mm gap between them. 0.10 m² overall. |
| Vane clamps **P17** (6 halves) | printed | At X = 520, 690 and 860, two identical halves per station, split on the Y = 0 plane: they close round the boom and sandwich both vane halves between them, held by M5 bolts through the vane. |
| Anemometer boom | Aluminium 6063-T6 tube | OD 25 × 2, axis Y 120, Z −260, X −650..−200; U-bolt saddles on the base plate at X −300 and −230. |
| Anemometer mast | Aluminium 6063-T6 tube | OD 25 × 2, axis (X −650, Y 120), Z −260..150. |
| Anemometer tee **P18** | printed | Joins boom and mast at (X −650, Y 120, Z −260). |
| Anemometer mount **P19** | printed | Mast top (Z 150): socket for the anemometer's Ø20 spigot. |
| Anemometer | bought 3-cup, reed switch | Body Ø50 × 80 on the spigot; cups on a Ø180 circle at Z ≈ 260. |
| Dump resistor | bought aluminium-clad 50 W, 10 Ω | 72 × 50 × 30 (with flanges), under the base plate: X ∈ [−300,−228], Y ∈ [−25,25], Z ∈ [−325,−295]; the plate is its heatsink. |
| Electronics enclosure **P20** base, **P21** lid, **P22** gasket | printed | Outer X ∈ [−355,−185], Y ∈ [−75,75], Z ∈ [−280,−215] (170 × 150 × 65 including lid). Holds the controller PCB (section 7). Cable glands: 3 × M20 on the −Y wall, 4 × M16 on the +Y wall, one M12 vent on the −X wall. |
| Battery | bought 24 V LiFePO₄ (8S, ~20 Ah) with its own BMS, in a weatherproof box | Box 300 × 200 × 250 on the ground at X ∈ [250,550], Y ∈ [−100,100], Z ∈ [−3000,−2750]. |
| Cable clips **P24** (3) | printed | Saddles held by a stainless cable tie, carrying the anemometer cable along its boom (X −350 and −500) and mast (Z −50). Tube diameter is a parameter (default 25). |

## 4. Swinging envelope (for clearance checks)

With θ ∈ [−20°, 20°] every S and P part must clear every A part by ≥ 3 mm, and with β ∈ [−3°, 48°] every P part must clear every S part by ≥ 3 mm. The known close spots, with the clearance designed in:

| Pair | Designed clearance |
|---|---|
| Spring carriage / hub side plate (X −115 vs −123) | 8 mm |
| Carriage spring OD / −X hub side plate | 6.5 mm |
| Reaction plate / spring roller | contact by design (rolling); the roller is the only part that touches |
| Stepper corner at θ = 20° (\|Y\| ≈ 106) / reaction plate (\|Y\| 150) | 44 mm |
| Belt arc web (R ≤ 94, X 87..95) / idler bracket P06 (R ≥ 110, X 93..101) | ≥ 16 mm radially |
| Belt arc rim (X 80.5..89.5) / idler flanges (X < 80.5 or > 89.5) | ≥ 0.3 mm axially, and the flanges stay outside R 100 |
| Hanger (Z ≥ −52 at θ = ±20°) / P06 top | ≥ 48 mm |
| Generator can (X 48..76) / belt plane (X ≥ 79) | 3 mm |
| Generator can / −X face of the arc rim | none needed: the can is at X ≤ 76 |
| Striker / stop posts | touches the bumpers at θ = ±20° only |
| Gearmotor (X 62..135, Z 160) / cheeks (Z ≤ 50) | ≥ 100 mm |
| Prism corner (r = 233 when feathered) / anemometer mast (X −650) | > 400 mm |

## 5. Printed parts

All printed parts live in the 3dprint repo under `parts/lantern330g/`, one module per part, to the part contract in that repo's `PLAN.md` §4.1. Each module also exposes, for the assembly:

- `ASSEMBLY_FRAME`: `"A"`, `"S"` or `"P"`;
- `placements(**kw) -> list[Location]`: where each copy of the part (as built by `part()`, in its print orientation) goes in that frame, at θ = 0 and β = 0, using the numbers in this file.

Printer: Bambu Lab X2D, 0.4 mm hardened nozzle, bed limit 246 × 246 × 260 mm (5 mm margin). Walls ≥ 1.2 mm (hard minimum 0.84). Overhangs ≤ 45° and bridges ≤ 20 mm unless declared in `PRINT['supported']` with a `why`. Horizontal holes as teardrops. M3/M4/M5 threads in printed parts use brass heat-set inserts fitted from the accessible side; bores per the insert maker (VERIFY on the fit coupon).

| ID | Module | Material | Qty | Frame | Function |
|---|---|---|---|---|---|
| P01 | `neck_spider` | ASA | 1 | P | Neck socket and four arms, bonded to the bottom end plate inside the prism. Printed with arms on the bed diagonals so it fits 246 mm. |
| P02 | `neck_top_collar` | ASA | 1 | P | Neck top socket, cap and flange at bulkhead 1. |
| P03 | `belt_arc` | PAHT-CF | 1 | S | GT2-toothed sector, pitch R 99.95, ±45°, bolts to the hanger. |
| P04 | `belt_clamp` | PAHT-CF | 2 | S | Toothed clamp for each belt end, 2 × M4 into heat-set inserts in P03. |
| P05 | `generator_mount` | PAHT-CF | 1 | A | Upright holding the 8108; slotted for belt tension; foot bolted to the base plate. |
| P06 | `idler_bracket` | PAHT-CF | 1 | A | Upright carrying both idler bolts from the +X side. |
| P07 | `gen_encoder_mount` | ASA | 1 | A | Encoder board behind the generator's rear shaft. |
| P08 | `gen_magnet_holder` | ASA | 1 | A* | Diametric magnet on the generator's rear shaft end (*turns with the rotor; static pose for the assembly). |
| P09 | `belt_guard` | ASA | 1 | A | Guard over the arc sweep and the pulley. |
| P10 | `stepper_mount` | PAHT-CF | 1 | S | NEMA-17 on the lever bottom, coaxial with the lead screw. |
| P11 | `pitch_gearmotor_bracket` | PAHT-CF | 1 | S | Saddle on the pitch housing over the worm window; clamps the gearmotor, holds a worm-shaft bearing (F695), seals the window. |
| P12 | `pitch_encoder_mount` | ASA | 1 | S | Stand on the hub top plate inside the pitch housing. |
| P13 | `pitch_magnet_holder` | ASA | 1 | P | Pressed into the neck-foot shaft's bottom end. |
| P14 | `hinge_encoder_mount` | ASA | 1 | A | Bracket and cover on the −X bearing retainer. |
| P15 | `hinge_magnet_cap` | ASA | 1 | S | Cap on the −X stub axle end carrying the magnet. |
| P16 | `end_stop_bumper` | TPU 95A | 2 | A | Bumpers on the stop posts. |
| P17 | `vane_clamp` | ASA | 6 | A | Clamp halves holding both vane halves to the tail boom (3 stations × 2). |
| P18 | `anemometer_tee` | ASA | 1 | A | Boom-to-mast tee, Ø25 tubes, clamp screws. |
| P19 | `anemometer_mount` | ASA | 1 | A | Mast-top socket for the anemometer spigot. |
| P20 | `enclosure_base` | ASA | 1 | A | Controller enclosure base: PCB bosses, gland holes, feet. |
| P21 | `enclosure_lid` | ASA | 1 | A | Lid with gasket groove and screw bosses. |
| P22 | `enclosure_gasket` | TPU 95A | 1 | A | Flat gasket in the lid groove. |
| P23 | `slip_ring_holder` | ASA | 1 | A | Slip-ring stator holder inside the post bore. |
| P24 | `cable_clip` | ASA | 3 | A | Cable saddle on a tube, held by a cable tie (default Ø25). |

Printed-material notes:
- **ASA**: UV-stable, outdoor parts and covers. Needs the X2D's heated chamber.
- **PAHT-CF** (Bambu PA12-CF class): loaded drive parts; low moisture uptake for a nylon; dry before printing.
- **TPU 95A**: bumpers and gasket.
- No profiles exist yet in the 3dprint repo for these three filaments (it has PLA and PETG). PETG is an acceptable stand-in for a bench prototype of the ASA and PAHT-CF parts, not for the outdoor build.

## 6. Bought parts used as interfaces (all VERIFY against the part in hand)

| Part | Modelled as |
|---|---|
| 8108 pancake outrunner | Can Ø88 × 28 (X 48..76); stator mount face Ø60 at X = 43 with 4 × M3 on a Ø30 PCD and a Ø16 centre relief; output shaft Ø5 from the can's +X face; rear shaft Ø5 protruding 5 mm behind the mount face. Ke ≈ 0.2 V·s/rad, R ≈ 0.8 Ω. **Note: a 12-tooth GT2 pulley limits the shaft to 5 mm (OD 7.1); many 8108 motors have 6–8 mm shafts or bolt-on rotors. If yours does, use a 16-tooth pulley with a 133 mm arc to keep 26.2:1.** |
| AS5047P encoder breakout | PCB 25.4 × 25.4 × 1.6 with 4 × Ø2.5 holes on a 20.3 mm square; IC centred on the top face; 6-pin 1.25 mm JST-GH lead out of one edge. Magnet Ø6 × 2.5 diametric N35, air gap 1.5 mm. |
| NEMA-17 stepper | 42.3 square, 48 long, M3 on a 31 mm square, Ø22 × 2 pilot, Ø5 shaft. |
| JGA25-370 gearmotor | Gearbox Ø25 × 21, motor Ø24.4 × 31, face with 2 × M3 at ±8.5 mm, shaft Ø4 D × 12. |
| F695 bearing | 5 × 13 × 4 with Ø15 × 1 flange. |
| 6005-2RS | 25 × 47 × 12. |
| 6907-2RS | 35 × 55 × 10. |
| Slip ring | Capsule body Ø22 × 35, flange Ø44 × 3 with 3 × Ø3.4 on a Ø34 PCD, rotor bore none (rotor leads out the top), stator leads out the bottom. |
| Anemometer | Ø20 spigot × 60 on the underside, body Ø50 × 80. |
| Cable glands | M20 × 1.5 (hole 20.5, hex 24) and M16 × 1.5 (hole 16.5, hex 20), nylon, with lock nuts. |
| Heat-set inserts | M3 × 5.7 (bore Ø4.0 × 6.5), M4 × 8.1 (Ø5.6 × 9), M5 × 9.5 (Ø6.4 × 10.5). |

## 7. Controller PCB envelope (shared with the pcb repo)

The board is designed in `14MM47/pcb`, `hardware/lantern-330g-controller/`.

- Outline **130 × 100 mm**, 1.6 mm, 4-layer. Board-local origin at one corner, x along the 130 mm edge.
- Mounting holes: 4 × Ø3.2 (M3) at (4,4), (126,4), (4,96), (126,96), keep-out Ø7.
- **Power connectors on the y = 0 edge** (battery, generator, dump resistor), facing the enclosure's −Y wall.
- **Signal connectors on the y = 100 edge** (encoders, stepper, pitch motor, clutch, limit switches, anemometer, temperature, RS-485), facing the +Y wall.
- USB-C and microSD on the x = 130 edge (reached with the lid off).
- Components on the top side only, ≤ 25 mm tall. Nothing on the bottom except test pads.
- In the enclosure: board on 6 mm standoffs, board bottom at Z = −269 (floor top Z −275), board centre at (X −270, Y 0), board x along assembly +X, board y along assembly +Y.

## 8. Material legend (assembly colours and labels)

| Key | Label | Colour (sRGB hex) |
|---|---|---|
| `asa` | ASA, 3D printed | #F28C28 |
| `paht_cf` | PAHT-CF, 3D printed | #7A3FB0 |
| `tpu` | TPU 95A, 3D printed | #19A7A0 |
| `sandwich` | GFRP-faced XPS sandwich | #EDE6D3 |
| `cfrp` | CFRP tube | #2B2B2B |
| `alu` | Aluminium 6082-T6 / 6063-T6 | #B9C0C8 |
| `stainless` | Stainless steel 316 | #8E99A3 |
| `steel` | Steel S355, galvanised | #6D7B88 |
| `bearing` | Bearings (bought) | #4E5964 |
| `spring` | Spring steel | #3E5A78 |
| `belt` | GT2 belt (neoprene, glass cord) | #3A2A20 |
| `bronze` | Bronze / brass (worm wheel) | #B0793B |
| `bought_elec` | Motors, sensors, slip ring (bought) | #3B3F45 |
| `pcb` | FR-4 PCB | #2E7D32 |
| `pp` | PP twin-wall (vane) | #F5F5F2 |
| `battery` | Battery box (bought) | #556B2F |

## 9. 330-GH differences (not modelled)

800 mm neck; hub and post head for 1,200 N·m; two-position feather (electromagnetic latch, torsion spring to a 45° stop) instead of the worm, wheel, gearmotor and clutch; ±30° stops and ±25° swing; ~51 N/mm die springs; HTD 8M 20 mm belt on a 275 mm arc with a 22-tooth pulley; direct-drive hub motor. P03, P04, P05, P06, P09, P11 and P16 would be redesigned; the rest carry over.

## 10. ASSUMED / VERIFY

| # | Item | Why it is assumed |
|---|---|---|
| V1 | The whole hub, pitch-drive and spring-carriage arrangement (stub axles, cradle, lever, rollers on reaction plates) | The design documents give the function, not the mechanism. |
| V2 | Neck extends 250 mm into the prism to bulkhead 1 (tube 575 long, +~0.04 kg over the 600 mm budget) and the spider and collar weigh more than the 20 g budget | A single bonded socket at the base cannot carry the ~340 N·m storm moment into a foam bulkhead. |
| V3 | 8108 dimensions, shaft and bolt pattern; 12-tooth pulley fit | Typical class values only. |
| V4 | Spring OD 25, free length, preload | Rate (30.8 N/mm) and force (≤ 1.5 kN) are from the calculator; the geometry is not. |
| V5 | Idler size and positions | Set by P06's author against the clearances in section 4. |
| V6 | Encoder breakout, slip ring, anemometer, gearmotor, clutch dimensions | Generic parts. |
| V7 | End-stop energy: the ±20° stops may see ~60 J in a fault | TPU bumpers are for the prototype; a production stop needs a sized rubber buffer. |
| V8 | Clutch hold power (power-to-engage, needed whenever the prism is not feathered) | Probably several watts; see the controller's peak-and-hold driver and the README note. |
