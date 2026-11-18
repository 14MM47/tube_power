# Lantern 330-G: zero-hold feather latch

Design note for the pitch-drive latch that replaces the power-to-engage electromagnetic clutch (owner's decision, 17 Nov 2026). Positions and part numbers are in [SPEC.md](SPEC.md) section 3.3. Every number below comes from [`tools/feather_latch_calc.py`](../../../tools/feather_latch_calc.py) or from the CAD layout in [`l330g/layout.py`](l330g/layout.py).

> **Status: concept design, revision B (18 Nov 2026).** Revision B applies the 17 Nov design review (section 11 lists each finding and what was done). The latch geometry passes the CAD check at every latched and released angle (section 5). **One item blocks a build:** the module-1 worm set and the JGA25 gearmotor cannot carry the latch torque (section 10). Friction values, the spring and the pitch moment are catalogue or assumed numbers; section 8 lists what to verify.

## 1. What it has to do

| Requirement | How it is met |
|---|---|
| Hold the shaft to the worm wheel with **no power**, at every latched angle from β = −3° to +48° (the shaft's stops) | A spring-engaged roller pawl in a single slot in a collar on the shaft, held by a roller sear that is a toggle set by a hard stop. Nothing is energised while it holds |
| Hold the worst pitch torque under galloping and end-stop impacts, without creeping or bouncing out | Sized for 48.3 N·m dynamic and 121 N·m strength (section 3). In the generating range the latch load never reverses, even with the dynamic factor; the pawl and sear are mass-balanced |
| Release with a **small** solenoid | Two stages. The pawl turns 1,557 N at the slot into 258 N on the sear; the sear needs a 3.8 N radial push at its tab roller (7.8 N at the solenoid in the worst case) |
| Trip at **every latched angle**, including a planned park at 40° | The hook is an arc concentric with the shaft (frame S, φ −12..58°). It pushes the tab roller radially at any β from −3 to +48 (section 3) |
| Solenoid **stationary**, no wires on turning parts | The solenoid sits outside the housing (frame S); a guided stem carries the hook |
| Fail safe | Losing power, the keep-alive (SAFE_OK) or the command fires the release from a stored-energy reservoir; the torsion spring feathers |
| Re-engage with the worm | The gearmotor drives the wheel round to the feathered shaft until the pawl drops in, then pitches back to 0° (section 6) |
| Assemble and inspect | The latch stack goes onto the shaft before the cap; the hook goes in through a gasketed inspection port, which also gives access for the yearly checks (section 5) |
| Space | Latch Z 150.5..216 at OD 86 (hook to 225, feather stop 229..238) inside ID 100. It extends the old Ø60, Z 170..195 clutch envelope. The solenoid is outside (section 4 says why) |

## 2. The mechanism

The **worm wheel** (bronze, 60 teeth) turns freely on a flanged bronze bush on the Ø35 shaft. A steel **carrier** disc is bolted to its hub (6 × M4 at R 25 plus 2 dowels) and carries the pawl and the sear. A steel **collar** keyed to the shaft (two A 10 × 8 keys) has one slot.

- **Stage 1, roller pawl.** A track roller (NATV 5-PP, Ø16, corrosion-protected) on the pawl's nose sits in the collar's slot at R 31.
  - The slot has a **planar load flank 30° from radial**. The roller touches it at R 27.87, and the flank runs on 2.7 mm to the collar's OD 61. The edge has a 0.5 mm radius, which leaves 2.2 mm of flat flank beyond the contact centre (the contact ellipse is 0.4 mm wide at the dynamic load). The contact normal passes through the roller centre, 26.85 mm from the shaft axis.
  - The torsion spring and the wind turn the shaft towards +β. The flank pushes the roller along the tangent, and that force runs straight into the pawl pivot (R 34.9, φ 158.3).
  - The flank also pushes the roller outward with tan 30° of that force (0.58×). That push acts 16 mm from the pivot and tries to open the pawl. The tail, 55.75 mm from the pivot, holds it, so the sear sees 16/55.75 of the outward push: **258 N at the dynamic load**.
  - The collar is case-hardened 18CrNiMo7-6 (58–62 HRC, case depth ≥ 0.6 mm), because the crowned roller makes a point contact (section 3).
  - To release, the roller must lift 8 mm to clear the flank's corner, so the pawl opens 30°. The pawl's tail is an arc at R 38..47.5 (Z 192..200) with a short foot behind its end face. Opened 30°, it still clears the shaft by 2.4 mm. The pivot boss stops above and below the collar, so the Ø8 pin passes the collar OD with 0.4 mm to spare.
- **Stage 2, roller sear (a toggle).** A needle track roller (INA RSTO 5, Ø16) on the sear bears on the tail's end face (contact at R 36, φ 262).
  - The sear pivots on a hardened Ø6 pin in a drawn-cup needle bush (HK0609), 16 mm behind the roller, on the line of the force.
  - A hard **sear stop** sets the roller 0.15 ± 0.05 mm on the closing side of that line (positive engagement): a hardened eccentric sleeve on a shoulder screw from the top plate, bearing on the sear's roller arm 10 mm from the pivot. The load and a 15 N·mm reset spring both push the sear closed, and the stop takes it (14 N at the strength load). Without the stop the sear would be an inverted pendulum: any offset would grow until something else stopped it.
  - Adjust the eccentric to set the engagement and lock it; it is checked yearly with a feeler gauge.
- **Trip.** The hook pushes a small roller on the sear's tab (683-2RS stainless, Ø7, on the yoke at X 39.6 in frame P) radially inwards. The sear turns until its roller has rolled 0.5 mm past dead centre (0.74 mm of radial travel at the tab roller). The load then opens it, the tail pushes past, and the pawl opens.
  - After release the sear swings about 31.5° and the pawl opens 30°. The roller clears the collar and the shaft runs to the feather stop under the spring.
- **Hook, stem and solenoid (frame S).**
  - The hook is an arc concentric with the shaft: R 44.6..46.6, φ −12..58°, Z 207..211, 1.5 ± 0.2 mm outside the tab roller.
  - A riser at φ 57..63 and a bridge (X 17..25, Y 20..42, Z 219..225) join it to the stem's M4 end. The hook part comes off the stem, so it can be fitted through the inspection port.
  - The **stem** (Ø6, D-flat) runs along X at (Y 24, Z 222) through a **D-bore bronze guide bush** pressed into the housing wall. The bush stops the hook turning (the check allows ±2°) and carries a greased lip seal.
  - Outside, an M6 **out-stop nut and lock nut** bear on the guide's flange and set the rest position: hook gap 1.5 ± 0.2 mm, plunger gap 4.4 mm. A **return spring** (1 N at the trip position) holds them there.
  - Because the arc is concentric with the shaft, its push on the tab roller is radial at every β, and the lever arm about the sear pivot is constant (23.8 mm). The hook only has to travel further at large β, by 1/cos β along X.
- **Feather stop.** A keyed collar on the shaft (Z 229..238) carries a lug (R 24..46, 20° wide at φ 180).
  - The lug lands on steel blocks on the housing at β −3° and +48°.
  - A PU 90 Shore A buffer on the +48° block takes it from +42°. The spring settles the prism on the buffer at about 45°.

Plan view at Z ≈ 180–225, frame P at β = 0, looking down. +X is downwind; the solenoid is outside on −X.

```
                          +Y
                           ^        bridge X17..25 Y20..42 (Z 219..225) -- riser φ57..63
           strap post o    |                                              \
           (R38, 108°)  \  |    top plate R22..30 (Z 213..216)              ) hook arc R44.6..46.6
       pawl roller (O)   \ |                                               )  φ -12..58 (frame S)
      (R31, 131°)  slot>  P|  pivot (R34.9, 158°), boss above/below collar )
    collar OD61 ---------+ |                                                )
                         | |                                     tab roller o  X 39.6 (sear)
  stem Ø6 Y24 ===========|=|=========================> M4 into the bridge
  guide bush in wall --->+ + shaft Ø35 -------------------------------------------> +X
  (D-bore, -X side)       \|                          _/  sear arm via (R38, -20°)
             pawl tail     \       stop [e]         _/
           R38..47.5 arc    \       (10 mm arm)   S   sear pivot (R28.7, 304°), HK0609
            (Z 192..200)     \                (o)    RSTO 5 roller, 16 mm from S
                         foot + end face at (R36, 262°)
```

Side view at the shaft, Z ranges:

```
 Z 229-238     [ feather-stop collar + lug ]  blocks at -3 / +48, PU buffer from +42 (frame S)
 Z 219-225     [ hook bridge ]  stem Ø6 at Y 24, Z 222 ==> guide bush in the -X wall ==> solenoid (outside)
 Z 213-216     [ top plate ]  carries the sear pin, the sear stop and the strap post
 Z 207-211                     hook arc (frame S)  ( tab roller 683 Z 207.5..210.5 )
 Z 201.5-205.5 [ sear plate ][ tab yoke 201.5..212.8 ]
 Z 192-200     [ pawl tail ]  (o) sear roller RSTO 5, Z 193.2..201
 Z 179.5-190.5 [ collar (shaft), 2 keys ](O) pawl roller 179..191 between the nose cheeks 177..193
 Z 171-176     [ carrier disc OD 86 ] lug at 270°  |wheel-stop blocks at 255° and 328° (frame S)|
 Z 165-171     [ wheel hub OD 58 ]  6 × M4 at R 25 + 2 dowels
 Z 155-165     [ worm wheel OD 62 ]  worm Ø16 at Y 37, Z 160
 Z 152-155     [ bush flange ]  retaining ring DIN 471-35 at Z 150.5..152
 Z 70-145      torsion spring, Ø7 wire, mean Ø76 (OD 83)
```

Materials:
- Carrier, pawl, sear, strap, top plate and feather-stop parts: 42CrMo4 QT (≈ 300 HB). The pawl and the sear are nitrocarburised and post-oxidised for wear and corrosion.
- Collar: 18CrNiMo7-6, case-hardened.
- Pins: 17-4PH H900. The sear's pin and roller pin are 100Cr6 at 60 HRC, because they are needle raceways.
- Rollers: NATV 5-PP (corrosion-protected), RSTO 5 (corrosion-protected), 683-2RS stainless; HK0609 and a DU bush for the pivots.
- Hook: 17-4PH H900, hook face nitrided.
- Guide bush: CuSn8.
- Solenoid bracket: 6082-T6.
- The only printed part is the weather cover **P25**.

**Printed parts in the load path:** the latch has none. The worm's thrust is reacted in the printed P11 bracket today, and that is one of the blocking items in section 10.

## 3. Load case

| Quantity | Value | Source |
|---|---|---|
| Torsion spring | **Ø7 music wire on a mean Ø76** (OD 83, about 9.8 active turns, Z 70..145). 18.5 N·m at 45°, rate 0.17 N·m/°: 23.6 at +15°, 26.2 at 0°, 26.7 at −3°. Indexed anchor sets ±3 % at assembly; acceptance band ±5 % | ASSUMED here (V8 a) |
| Feather requirement | Spring at 45°, −5 % = 17.6 N·m ≥ 1.25 × 13.5 = 16.9 N·m (1.30×) | Review M10 |
| Spring stress | 893 MPa at −3° (+5 %) against 0.78 Sut = 1,301 MPa (1.46×); Goodman n = 1.40 for the park/restart cycle 45° ↔ 0° | The old Ø5.5 spring reached 1,324 MPa against 1,347: no margin |
| Aerodynamic pitch moment, CM q D² L | 10.7 N·m at 40 m/s, **13.5 N·m at 45 m/s** | Calculator, CM_pitch = 0.10 (assumed there; V8 b) |
| Static hold torque | 26.7 × 1.05 + 13.5 = **41.5 N·m** | Spring at −3° (+5 %) plus a 45 m/s gust while a feather request is pending |
| Dynamic hold torque | 28.0 + 1.5 × 13.5 = **48.3 N·m** | Factor 1.5 on the aerodynamic part, for gusts and galloping at up to 3.7 Hz |
| Strength design | 2.5 × 48.3 = **121 N·m**, no yield | Safety factor 2.5 |
| Least latch torque, generating range | 23.6 × 0.95 − 1.5 × 13.5 = **+2.2 N·m** | Spring −5 % at +15°, the dynamic aerodynamic moment against it. It never reverses, so there is no rattle or hammering in the slot while generating |
| Pitch moves above +30° in a 45 m/s gust | −0.3 N·m at +30°, −3.2 at +48° | Reverses onto the slot's back flank, which pushes the roller in: no sear load. This happens only during a powered worm feather in a storm (rare); planned parks run in light wind |

Accelerations at the latch (Z_S = 185 mm above the hinge):

| Case | Tangential (along Y_S) | Centripetal (−Z_S) |
|---|---|---|
| Generating at 40 m/s, ±8.8° at 3.66 Hz | 15.0 m/s² (1.5 g) | 2.3 m/s² |
| ±15° at 2.06 Hz | 8.1 m/s² (0.8 g) | 2.1 m/s² |
| ±20° (to the stops) at 3.7 Hz | 34.9 m/s² (3.6 g) | 12.2 m/s² |
| Fault: 60 J into the stops (V7), 4 mm bumper deflection | **558 m/s² (57 g)**, peak | — |

What they do to the latch:

- **The pawl and sear turn about axes parallel to Z.** They are balanced about their pivots to 0.5 mm. At 57 g the sear's imbalance moment is 1.7 N·mm against a 16.2 N·mm closing moment at the least latch load (margin 10). The closing direction is taken by the stop.
- **The hook cannot turn or creep.** The D-bore guide stops it turning about the stem. The out-stop nut and the 1 N return spring hold it out against 3.6 g of swing acceleration, which mostly acts across the stem anyway. A trip needs 7.8 N at the solenoid in the worst case.
- **The swing does not couple into pitch.** The prism is square, so its two transverse inertias are equal and the swing puts no torque on the pitch axis.

### Stage 1, roller pawl

| Load | Torque | Roller normal | Tangential (into the pivot) | Outward push | Sear force F2 |
|---|---|---|---|---|---|
| static | 41.5 N·m | 1,546 N | 1,339 N | 773 N | 222 N |
| dynamic | 48.3 N·m | 1,797 N | 1,557 N | 899 N | 258 N |
| strength | 121 N·m | 4,493 N | 3,891 N | 2,247 N | 645 N |
| least | 2.2 N·m | 80 N | 70 N | 40 N | 11.5 N |

Contact and strength:

- **Flank contact.** The NATV outer ring is crowned (R ≈ 500, ASSUMED), so the contact is an ellipse.
  - At the mean load (spring at 5°): p_max 1,186 MPa.
  - At the dynamic load: 1,447 MPa, with a 5.8 × 0.41 mm ellipse and maximum shear 0.16 mm deep.
  - At the strength load: 1,964 MPa.
  - Case-hardened 18CrNiMo7-6 has a contact-fatigue limit of about 1,500 MPa and a static limit of about 4,000 MPa. A case depth of at least 0.6 mm is well over twice the depth of maximum shear.
- **Roller.** The roller needs a static rating of at least 4.5 kN (V8 e).
- **Roller pin.** Ø5 in double shear: 114 MPa at the strength load.
- **Pawl pivot.** The Ø8 pin is carried by the carrier and the strap. Shear is 39 MPa; bearing on the DU bush is 44 MPa over 11 mm (the boss stops beside the collar).
- **Pawl tail.** The arm is 9.5 × 8 mm at its root. Bending is 107 MPa at the dynamic load and 267 MPa at the strength load (Rp0.2 ≥ 650).

**Release after the sear lets go.** The opening moment is 899 N × 16 mm = 14.4 N·m. Friction at the pawl pivot opposes it:

| Pawl pivot | Friction moment | Margin |
|---|---|---|
| DU bush, lubricated (μ 0.05) | 0.36 N·m | 40 |
| DU bush, dry or worn (μ 0.25) | 1.80 N·m | 8 |
| Corroded steel pin (μ 0.7, a failure) | 5.03 N·m | 2.9 |

If the pawl roller is **seized**, it slides on the flank. At the least latch load it still releases up to μ ≈ 0.5. Clean, greased or dry steel is 0.12–0.45, so it releases; corroded steel at μ 0.6 does not (section 7).

### Hold path beyond the carrier (blocking, section 10)

The hold torque runs carrier → 6 × M4 and 2 dowels → wheel hub → the module-1 bronze teeth → the worm → its axial thrust bearing.

| Load | Torque | Wheel tooth force (pitch R 30) | Lewis stress, m 1, face 10, y 0.125 |
|---|---|---|---|
| spring only, −3° (+5 %) | 28.0 N·m | 933 N | 238 MPa |
| static | 41.5 N·m | 1,383 N | 352 MPa |
| dynamic | 48.3 N·m | 1,608 N | 410 MPa |
| strength | 121 N·m | 4,021 N | 1,024 MPa |

- **Worm wheel.** Cast CuSn12 has Rp0.2 ≈ 140 MPa and a bending fatigue limit of about 60–90 MPa. **The m1 × z60 set cannot carry even the spring torque.**
- **Worm thrust.** The worm's axial thrust equals the tooth force. Today it is reacted by an F695 seated in the printed P11.
- **Self-locking.** The 4.09° lead needs μ > 0.071.
- **Gearmotor.** Driving the spring (27.5 N·m at 0°) through 60:1 needs 0.85–1.11 N·m at the gearmotor (μ 0.06–0.10). That is beyond a JGA25-370.
- **Carrier joint.** 6 × M4 8.8 at R 25 into 16 mm of thread in the wheel, plus 2 dowels: 804 N per bolt at the strength load (M4 8.8 shear about 3.4 kN). Friction grip is about 90 N·m.
- **Collar keys.** 2 × A 10 × 8 × 11, 5 mm into the 6082 shaft: 25 MPa bearing at the dynamic load, 63 MPa at the strength load (yield 260).

### Stage 2, roller sear, and the trip force

- **Sear roller.** INA RSTO 5 (C0 ≈ 3.6 kN, VERIFY): s0 14 at the dynamic load, 5.6 at the strength load.
- **Sear pivot.** HK0609 on a hardened Ø6 pin (C0 ≈ 1.9 kN): s0 7.4 and 2.9. The old 625-2RS and 2 × MR85 had s0 ≈ 0.5 at the strength load.

The trip moment about the sear pivot has four parts:
- F2 × engagement (the stop's maximum, 0.20 mm);
- the roller's bearing friction. It acts at the contact, so its moment is M_b × (L2 + R)/R = 3 × M_b;
- the pivot's friction;
- the reset spring.

The hook pushes the tab roller radially, 23.83 mm from the sear pivot at every β:

| Condition (dynamic load, F2 = 258 N, engagement 0.20 mm) | Trip moment | Radial push on the tab roller |
|---|---|---|
| New (μ_b 0.0025) | 77 N·mm | 3.24 N |
| **Aged, seal drag (μ_b 0.005): design case** | 90 N·mm | **3.78 N** |
| Sear roller seized, sliding on a greased face (μ 0.12): a failure | 814 N·mm | 34 N: does not trip |
| Sear roller seized, dry or corroded (μ 0.6): a failure | 3,786 N·mm | 159 N: does not trip |

To get from the push on the tab roller to the pull at the solenoid, add:
- the stem guide's friction (DU-class, μ 0.2 aged), from the hook contact's offset from the stem axis and the radial push's Y component at β ≠ 0;
- the plunger's PTFE friction (μ 0.25 aged);
- the 1 N return spring;
- 0.3 N of seal drag.

The pull is evaluated at the smallest hook gap (1.3 mm), where the load is picked up at the largest plunger gap:

| β | Hook stroke used (reserve of the 4.4) | Plunger gap at pick-up | Needed at the solenoid | Available at 1.90 A | Margin | Margin if guide μ 0.4, plunger μ 0.5 |
|---|---|---|---|---|---|---|
| −3° | 2.45 mm (1.95) | 3.10 mm | 6.38 N | 15.0 N | 2.35 | 1.98 |
| 0° | 2.44 mm (1.96) | 3.10 mm | 6.57 N | 15.0 N | 2.28 | 1.89 |
| +15° | 2.53 mm (1.87) | 3.05 mm | 7.31 N | 15.1 N | 2.07 | 1.58 |
| +30° | 2.82 mm (1.58) | 2.90 mm | 7.78 N | 15.6 N | **2.00** | 1.43 |
| +40° | 3.19 mm (1.21) | 2.70 mm | 7.93 N | 16.2 N | 2.04 | 1.40 |
| +48° | 3.65 mm (0.75) | 2.46 mm | 7.88 N | 17.0 N | 2.15 | 1.43 |

A 2.0× margin at every β needs 1.91 A, so the pulse is **current-regulated at 1.94 A ± 2 %**. At the 4.4 mm rest gap the coil pulls 12.4 N against the 1 N return spring.

Plain sliding sears were rejected because of the seized-roller rows: even greased, a sliding contact needs 34 N. The rolling contacts are what make a small solenoid possible, so their seizure is a failure mode with its own inspection item (section 7).

## 4. Solenoid

**Guardian Electric LT8x16-I-12D** (part A420-064851-00): a long-life DC tubular pull solenoid.

- Size Ø25.4 × 50.8 mm, plunger Ø11.1 mm.
- Stainless guide tube and PTFE-coated plunger, rated 10 million cycles.
- 12 V, 6.2 Ω ±5 %, 24.4 W, 25 % duty.
- Datasheet pull force at 12 V and 20 °C (25 % row): 22.2 N at 1.27 mm, 15.3 N at 3.18 mm, 9.7 N at 6.35 mm, 7.0 N at 9.5 mm.
- Source: the Guardian Electric LT8x16 datasheet (guardian-electric.com; Farnell copy farnell.com/datasheets/2722902.pdf). Stocked by Farnell/element14 and Newark.

**Sizing.**
- Force scales as (I / 1.94 A)². Regulating the current makes the force independent of coil temperature and supply sag, and the driver absorbs both.
- The regulated pulse is 1.94 A ± 2 % for 100 ms. That is 28 W in a hot coil for 0.1 s, at under 5 % duty for three pulses 2 s apart.
- The margins are in the table above.
- An unregulated pulse straight from a 13.5 V bus gives only 1.75 A into a hot coil and cable, below the 1.91 A needed, so it is not acceptable.

**Why it is outside the housing.**

- Inside the Ø100 housing, the Ø35 shaft leaves an annulus 32 mm wide. A vertical LT8x16 only fits at R 33–36 mm, where its plunger would hang into the latch. A horizontal one does not fit at all.
- The smaller solenoids that do fit (Guardian LT6x12, T8x9) give less than half the force or the work needed for a 2× margin.
- Outside, on the −X side at (Y 24, Z 222) with its axis along X, the solenoid is clear of the gearmotor (+X), the hinge cheeks and the swing envelope.
- **Mounting.** The bracket is an aluminium front plate with two flanges and a 3 mm saddle shaped to the tube OD. It is bolted with 2 × M4 into tapped holes in the tube wall (φ 136° and 168°, Z 222). A spot face on the tube takes the guide-bush flange.
- **Weather cover.** The ASA cover **P25** is gasketed to the tube over the solenoid, bracket, nuts and spring. It holds a desiccant sachet and has a cable gland underneath.
- **Cable.** The cable is a 0.5 mm² pair. It runs down the −X side of the housing under clips, through the hub with the gearmotor and encoder cables, and across the hinge in a service loop to an M16 gland on P20's +Y wall. The loop, with the driver's MOSFET and sense resistor, is at most 0.2 Ω.

## 5. CAD, assembly and checks

The parts are in `l330g/structure.py` (`_latch`, `latch_wheel_shapes`):

| Group | Parts | Frame |
|---|---|---|
| On the shaft | Collar M50 (slot, 2 keys), retaining ring B39, feather-stop collar and lug M64 | P |
| On the wheel | Bush B36, carrier M51, pawl M52, pawl roller B37, pins M54, strap and post M55, sear M53, sear roller B38, tab roller B40, needle bush B41, sear stop M60, top plate M56 | P, tagged `extra['latch'] = 'wheel'` |
| Stationary | Wheel-stop blocks M57, hook M58, stem M61, guide bush M62, nuts B42, return spring B43, solenoid B06, bracket M59, port cover M63, feather-stop blocks M65, buffer B44 | S |
| Printed | Weather cover P25: a placeholder envelope (X −126..−48, Y −2..50, Z 202..242) until the 3dprint module exists | S |

`python3 -m l330g check` runs the six SPEC poses as before. These cover β = 0, 10 and 45 with the latch engaged. It then runs `latch_check()`, which poses the wheel and the shaft separately, and the hook where the case says:

| Cases | Wheel | Shaft | Hook |
|---|---|---|---|
| Latched, 1° steps (52 cases) | −3..+48 | = wheel | at rest |
| Released, shaft feathered, pawl open 30°, sear swung 31.5°, 1° steps (58 cases) | −7..+50 (wheel stops) | 45° | at rest |
| Released, hook at the end of its 4.4 mm stroke | −3, 0, 15, 30, 40, 48 | 45° | pulled 4.4 mm |
| Latched, hook at its tolerance | −3, 15, 30, 40, 48 | = wheel | turned ±2° about the stem and 0.2 mm in |

A pair closer than 3 mm passes only if it has its own rule and keeps that rule's least gap. These are the latch's designed running gaps (SPEC section 4):

| Pair | Least gap kept | Drawn |
|---|---|---|
| Hook / tab roller | 1.0 mm | 1.5 ± 0.2 (1.0 at the hook's tolerance) |
| Hook / sear yoke | 2.0 mm | 2.4 at the tolerance |
| Hook bridge / top plate and pin heads | 2.5 mm | 3.0 (2.8 at the tolerance) |
| Carrier lug / wheel-stop blocks | contact at −7° and +50° | 0.1 drawn at the stops |
| Pawl pivot pin / collar OD | 0.3 mm | 0.4 |
| Bush / collar (axial float); pawl nose cheeks / collar | 0.4 mm | 0.5 |
| Sear, its roller, pin and stop / shaft and collar | 1.5 mm | 1.7 with the sear tripped |
| Opened pawl tail / shaft | 2.0 mm | 2.4 |
| Wheel and carrier bores / shaft | 2.5 mm | 3.0 |
| Pawl tail / housing wall | 2.0 mm | 2.2 |
| Opened pawl roller / housing wall | 2.5 mm | 2.9 |
| Worm / wheel, bush / shaft and ring, pawl roller / flank | contact (mesh, bearing, rolling) | — |

Result (`out/interference.md`, 18 Nov 2026): **0 interferences and 0 gaps below their least in all 126 latch cases**, and 0 interferences, 0 unexplained gaps under 3 mm and no named pair below its design value at the six SPEC poses. `python3 -m l330g check` exits 0.

**Assembly order** (the cap is captive on the shaft above the shoulder, so the latch goes in from the top before it):

1. Torsion spring onto the shaft, its lower leg into the housing anchor.
2. On the shaft, from below the latch: retaining ring, then the wheel stack (bush, wheel, carrier, pawl with roller, sear with roller, stop, strap, top plate) pre-assembled on the bench. Then the collar and its keys, the feather-stop collar, the upper bearing and the cap.
3. Lower the shaft and stack into the tube. The wheel-stop blocks and the feather-stop blocks are already screwed to the tube. Fit the cap; index the spring's upper leg.
4. Worm and its bearings through the worm window; then P11 and the gearmotor.
5. Hook through the inspection port, held up to the stem axis.
6. Guide bush into the wall (pressed, with its seal), stem through it, M4 end into the hook bridge (thread-locked).
7. Return spring, washer, out-stop nut and lock nut, then the solenoid and bracket. Set the 1.5 mm hook gap through the port with a feeler gauge and lock the nuts.
8. Set the sear engagement with the eccentric stop (0.15 ± 0.05 mm, feeler gauge through the port), lock it, close the port, fit P25.

The **inspection port** (φ −40°, 50 mm wide, Z 195..235, gasketed aluminium cover) is on the +X/−Y side, clear of P11 (φ 4..86°). Through it one can reach the tab, the sear roller and its stop, the slot, the hook and its joint. The yearly checks in section 7 are done through it without opening the cap.

## 6. Release, parking and re-engagement

**Release.**

- **Fault, storm or loss of power:** the board fires one regulated 100 ms pulse from its reservoir (section 9). The spring feathers from wherever the shaft is. From the −3° stop in a storm, the spring (+5 %) does 19.9 J and the pitch moment can add up to 11.3 J: 31 J into the buffer (V8 h).
- **Planned park** (negative net output, light wind): the worm drives the latched shaft to 40°, then the board fires. The hook reaches the tab at any latched β, so the spring moves only the last 5° (1.7 J). Every park therefore tests the trip.
  - The **first pulse of a planned park is a reduced-current margin test** (1.33 A). At the park load it gives 1.5× the force needed, so a trip at 1.33 A proves at least 2× force headroom at full current.
  - If it does not trip within 0.5 s, the board fires at full current and logs "trip margin low".

The encoder must see β pass 44° within 0.5 s of the pulse. If it does not:

1. Fire up to two more full-current pulses, 2 s apart.
2. Then feather with the worm. The latched shaft goes to 45° with the wheel; the worm is a second, powered way to feather.
3. Log a fault and keep the brake on.

**Re-engagement.**

1. Check the shaft encoder (P13/P12) reads the feather stop and the solenoid is off.
2. Drive the gearmotor +β slowly, current-limited to about 30 % of stall. The wheel moves at about 5°/s. Its angle is estimated from the shaft angle logged at the last release plus run time; a Hall encoder on the gearmotor would make it exact (recommended).
3. The roller rides on the collar and drops into the **single slot** when the wheel reaches the shaft angle. A 1 mm × 30° lead-in on the slot's trailing edge widens the capture window to about ±2°, and the pawl spring must drop the roller in under 50 ms (V8 i). The sear spring then snaps the sear back onto its stop behind the tail.
   - With one slot there is no wrong position: the wheel can only travel −7°..+50° between its stops, and the only place it can latch is wheel = shaft.
4. Keep driving +β a few degrees. The encoder moving with the motor is a **hint** of engagement. A current spike with no encoder motion at the +50° wheel stop means it did not latch: back off 10° and retry up to 3 times, then stay parked and log a fault.
5. **Pass/fail:** reverse to 0°. The encoder must follow the commanded wheel motion within 1°, against the spring's full torque.
   - If the shaft stays at 45°, or springs back during the move, the pawl bounced or the sear did not reset. The latch load opens an unheld pawl at once, so this test also checks the sear. Repeat from step 2.
6. Release the brake and kick-start.

**Broken-spring detection.** On every pitch move the gearmotor current must match the expected spring torque. A broken spring shows at once as a drop in current. If it does, pitch to 45° latched with the worm and stay parked.

**Icing.** The controller parks (with a trip) when the temperature falls to +3 °C in rain or high humidity, before any ice can form on the trip parts.

## 7. Failure modes

| Failure | Effect on feathering | Detected by | Inspection |
|---|---|---|---|
| Solenoid coil open, or driver dead | No electrical trip | The board's coil-continuity and resistance test; the encoder at the next park | — |
| Solenoid coil shorted | No trip; the reservoir would dump into the short | The driver's current limit and resistance test; no release at the next park | — |
| Reservoir flat or a capacitor aged | No trip on loss of supply | The board's reservoir voltage and ESR test before each planned park | Board item |
| **Both trip paths fail with no power** (solenoid and reservoir) | **Stays latched at the last β and keeps galloping, braked by the shorted generator.** This is the one case with no aerodynamic stop | Logged at the next park | The board's reservoir test, plus a margin test at every park |
| Torsion spring broken | Releases but does not feather: the prism floats in pitch | Gearmotor current on every pitch move; the encoder after a trip | **Annual:** torque at 0° with a torque wrench (26.2 N·m ± 5 %) |
| Spring weak or relaxed | Below 16.9 N·m at 45° it may not feather in a 45 m/s gust | Annual torque check | Replace outside ± 5 % |
| Ice on the trip parts | Can stop a release | Pre-emptive park at +3 °C; trip-time alarm; worm feather as the fallback | Stem inside the greased guide seal and P25; desiccant in P25 and the cap |
| Corrosion of pins, rollers or the flank | Raises trip force. **A seized sear roller stops the trip** (34 N or more against about 15 N available); a seized pawl roller still releases up to μ ≈ 0.5 | Reduced-current test at every park; trip time | **Annual:** spin all three rollers by hand; spring-balance trip force at the tab roller latched at β = 0 (about 2.2 N radial at the spring-only load, alarm above 3.0 N); grease the flank |
| False brinelling of the sear roller or pivot | Rising trip friction | Reduced-current test at every park | Rated well above the load (s0 ≥ 2.9 at the strength load) |
| Wear of the slot flank, the tail face, the sear stop or its contact | Changes the engagement and the release | Trip time and test current | **Annual, or every 5,000 parks:** feeler-check the engagement (0.15 ± 0.05 mm, reset the eccentric); check the stop's lock; inspect the flank and the lip radius for spalling (replica or profile gauge) |
| Hook loose on the stem, or the out-stop nut moved | Hook gap wrong: no trip (gap too big) or a jam (gap too small) | Trip time at every park | **Annual:** hook gap 1.5 ± 0.2 mm with a feeler gauge through the port; lock-nut and thread-lock marks |
| Debris in the housing | Can jam the pawl or the sear | Failed trip or failed re-engage | Housing sealed (cap, port cover, P11 window seal, guide seal) |
| Misassembly: sear stop set to negative engagement | The sear opens under load: a spurious feather (safe), and it will not latch | Re-engagement step 5 fails | Set with a feeler gauge; latch, load by hand at β = 0, confirm it holds and trips at the reduced current |
| Misassembly: collar keyed wrongly | Latches at the wrong shaft angle | Encoder against the wheel estimate after re-engagement (± 2°) | Mark the collar and keyways |
| Pawl spring or sear spring broken | Pawl spring: will not drop in (safe, stays parked). Sear spring: the load alone still holds the sear on its stop (11.5 N × 0.10 mm = 1.2 N·mm at the least load), with no margin against a 57 g shock; a shock trip would be a safe feather | Re-engagement fails, or spurious feathers | Annual visual |
| Spurious trip (electrical noise, a shock) | Feathers: safe, loses output | Logged | — |

**Needing an interval:**

- **Every planned park, automatic:** a reduced-current margin trip.
- **Before each planned park, automatic:** the board's reservoir and coil tests.
- **Annual, through the port:**
  - spring torque;
  - trip force at the tab roller;
  - sear engagement and its stop;
  - hook gap;
  - rollers;
  - the flank and its lip;
  - grease;
  - the desiccant.

## 8. VERIFY

These are also SPEC V8 (a)–(k).

1. **(a)** The torsion spring: 18.5 N·m at 45°, 0.17 N·m/°, ±3 % as assembled, Ø7 music wire on a mean Ø76.
   - Check its fatigue life for about 5,000 parks a year (Goodman 1.40 calculated).
   - Check that the body (about 76 mm with the legs) fits Z 70..145.
2. **(b)** The pitch moment coefficient (CM 0.10), on the static rig, at β = 0–15° and on the way to 45°. The feather requirement (spring ≥ 1.25 × peak moment at every β) is checked against the measured CM(β).
3. **(c)** The trip force:
   - the radial push at the tab roller, latched and loaded: 3.24 N new and 3.78 N aged at the dynamic load (scale by the actual torque);
   - the pull at the solenoid stem, measured with the guide and plunger fitted: at most 7.8 N at any β.
4. **(d)** The solenoid's force-stroke at 1.90 A between 2.4 and 3.1 mm of gap, and its pull-in time at 1.94 A (the 100 ms pulse assumes well under 50 ms).
5. **(e)** Static ratings:
   - NATV 5-PP: at least 4.5 kN;
   - RSTO 5: about 3.6 kN;
   - HK0609 on a 60 HRC pin: about 1.9 kN;
   - also the NATV crown radius (R 500 assumed) and the collar's flank contact at 1,447 MPa dynamic.
6. **(f)** The sear engagement as set by the stop (0.15 ± 0.05 mm) and its stability under vibration.
7. **(g)** The worm's self-locking under galloping vibration while latched. This is part of the pitch-drive redesign in section 10.
8. **(h)** The feather-stop buffer: 31 J (a storm trip from −3°, spring plus pitch moment) as a rare case, and about 2 J × 5,000 parks a year. The drawn PU pad (8 × 7 mm face, 6° deep) is a placeholder and must be sized.
9. **(i)** The whole layout on a 1:1 prototype:
   - pawl opening 30°, sear swing 31.5°;
   - the springs, the strap and the top plate;
   - the slot's lead-in and a pawl drop time under 50 ms;
   - grease retention;
   - fitting the hook through the port.
10. **(j)** The guide bush: rotational play no more than ±2° (the check's tolerance), and the friction of its seal.
11. **(k)** The hub mass with the latch and the heavier spring (section 10).

## 9. Board requirement (for the controller in the pcb repo)

| Item | Requirement |
|---|---|
| Solenoid | Guardian LT8x16-I-12D, 12 V DC pull, one coil, no polarity |
| Coil resistance | 6.2 Ω ± 5 % at 20 °C (**5.89–6.51 Ω cold**); **7.53 Ω worst at 60 °C** |
| Drive | **Current-regulated** (buck or linear) switch with a freewheel path. Regulate **1.94 A ± 2 %** (at least 1.90 A) for the whole pulse. Short-circuit current limit about 3 A. Fire on command, on loss of SAFE_OK (the keep-alive) and on loss of supply, from a stored-energy reservoir, with the fire path independent of the MCU |
| Pulse | **100 ms**. Up to 3 full-current pulses 2 s apart per event. Plus a **reduced-current test pulse of 1.33 A ± 2 %**, 100 ms, on command (the first pulse of a planned park) |
| Compliance (minimum at the end of the pulse) | The driver must still deliver 1.98 A at the end of the pulse into the hot coil plus the 0.2 Ω loop: **≥ 15.3 V at the driver output**, which is ≥ 14.3 V at the coil terminals at 1.90 A with the coil at 60 °C. The reservoir must stay **≥ 16.8 V** (1.5 V of driver headroom) at the end of the third pulse |
| Energy | 3.03 J per pulse into the hot coil and loop (2.38 J cold). From the store at 85 % driver efficiency: 3.56 J per pulse, **10.7 J for 3 pulses** |
| Reservoir example | 27 V nominal down to 16.8 V: C ≥ 48 mF, **≥ 60 mF** allowing −20 % capacitance at end of life. An unregulated store straight onto the coil is **not** acceptable: 13.5 V gives only 1.75 A into the hot coil |
| Cable | 0.5 mm² pair. Loop including MOSFET, sense resistor and connectors **≤ 0.2 Ω**. Connector on the signal edge (y = 100) |
| Latch-engaged switch | **None.** The shaft encoder (P13/P12) and the gearmotor current detect engagement and release (section 6) |
| Diagnostics | Coil continuity and resistance (a small sense current); the coil current during each pulse (to confirm the regulation and the reduced test); reservoir voltage and ESR before each planned park; the time from pulse to β > 44° from the encoder (alarm above 0.5 s); the gearmotor current for engagement and broken-spring detection. A Hall encoder input for the pitch gearmotor is recommended |

## 10. Open issues

1. **BLOCKING: the pitch drive's worm set, worm thrust and gearmotor (review M7, I5).** The hold torque passes through the worm teeth whatever the latch does, because the latch couples the shaft to the wheel and the self-locking worm holds the wheel.
   - The m1 × z60 bronze set with a 10 mm face is at 238 MPa under the spring alone, against Rp0.2 ≈ 140. The pitch drive needs re-sizing for 48.3 N·m (fatigue) and 121 N·m (no yield) at the wheel. Options: a larger module with a wider face, or a throated wheel, chosen from a catalogue rating.
   - The worm's thrust (up to 4 kN at the strength load) needs an angular-contact or thrust pair seated in the aluminium housing or a metal bracket, not in the printed P11.
   - The gearmotor needs at least 1.1 N·m at the worm at the pitch speed. A JGA25-370 cannot do it.
   - This changes the worm window, P11 (3dprint repo) and the gearmotor, so it is left to the owner. The latch itself is independent of it.
2. The torsion spring (V8 a) and the pitch moment (V8 b) are assumed.
3. **Hub mass (review I9).** The CAD BOM gives 0.9 kg of latch parts, and the Ø7 spring is 0.72 kg (the old Ø5.5 spring was about 0.29 kg). That is about 1.3 kg more on the pitch drive than the calculator's 0.30 kg `pitch_mass`. The mass sits 0.1–0.25 m above the hinge, so it adds only about 0.03–0.05 kg·m² to the 1.89 kg·m² inertia, but the swinging mass, the gravity term and the README's mass lines must be re-run with the real figure (`tools/galloping_calc.py`, not changed here).
4. P25 is a placeholder envelope until the 3dprint module is written.
5. The feather-stop buffer is a placeholder (V8 h).

## 11. Revision B: what the 17 Nov review changed

| Finding | What was done |
|---|---|
| M1 sear without a stop | Hard eccentric sear stop at a 10 mm arm sets the engagement to 0.15 ± 0.05 mm; the calculator takes e from it |
| M2 edge contact in a round pocket | Planar 30° flank in a collar enlarged to OD 61; crowned-roller Hertz check; case-hardened 18CrNiMo7-6 |
| M3, I1 planned parks could not trip | Hook made a concentric arc covering every latched β (−3..+48); parks fire at 40° |
| M4 trip force underestimated | Roller friction moment × (L2+R)/R; a roller on the tab removes hook sliding; guide and plunger side-load friction added; trip force evaluated over β |
| M5 sear bearings overloaded | RSTO 5 track roller and an HK0609 needle bush on hardened pins |
| M6 latch load reversal | Stiffer spring: no reversal in the generating range with the 1.5 dynamic factor |
| M7, I5 worm teeth, thrust and joint | Carrier joint and keys redone and checked; the worm set and gearmotor are a blocking open issue (section 10) |
| M8 reservoir did not give 3 pulses | Current-regulated drive sized for 3 pulses against the hot coil (section 9) |
| M9, I3 hook unguided | D-bore guide (anti-rotation), out-stop nut, modelled return spring, hook-tolerance cases in the check |
| M10 spring margin and stress | Ø7 spring, 1.30× feather margin at −5 %, 1.46× static stress margin |
| M11 self-test at half load | A reduced-current margin trip at every planned park |
| M12 ice and corrosion | Pre-emptive park at +3 °C; guide seal; corrosion-protected rollers and post-oxidised parts |
| M13 buffer energy | Spring plus pitch moment: 31 J (V8 h) |
| M14 weak engagement detection | Step 5 is the pass/fail; slot lead-in; gearmotor-current spring check; Hall encoder recommended |
| I2 riser in the tab's path | Riser moved beyond every latched tab angle; latch check sweeps every degree |
| I4 no assembly or service route | Hook split from the stem; inspection port; assembly order |
| I6 build-and-test idle | Rewritten to parked idle, net-power start and the latch tests |
| I7 margin over β | Constant arm with the concentric hook; table over β |
| I8 stops and ranges | Feather stop modelled (−3, +48, buffer); one latched range everywhere |
| I9 README wording and mass | Wording fixed; mass flagged (section 10) |
| I10 parts outside the housing | P25 placeholder registered; bracket saddle bolted; cable route and loop resistance specified |
| I11 blanket clearance rules | Pair-specific least gaps (section 5) |
| I12 coupling and gearmotor/cheeks | Coupling X 43..56 as P11 is built; SPEC 4 value corrected to what the geometry gives |

Revision B also fixed two faults that the revised geometry introduced and the check found:
- the pawl's pivot boss cut into the larger collar;
- the old R 32..43 tail swept through the shaft once the pawl opened 30°.
