"""Every number in the Lantern 330-G layout, as named constants.

This module is the single source of numbers for the ``l330g`` package. Each
constant comes from ``../SPEC.md`` (cited by section) unless it is listed in
``ASSUMED`` (a modelling detail the SPEC does not give, to be measured or
agreed: a VERIFY entry) or in ``DEVIATIONS`` (a place where the SPEC numbers
conflict with each other and the model changes one of them by the smallest
amount that removes the conflict).

Units are millimetres and degrees. Positions are in frame A at theta = 0,
beta = 0 (SPEC section 1). Pairs are (low, high) ranges; for parts mirrored in
X or Y the +X or +Y copy is given.
"""
from __future__ import annotations

# ---------------------------------------------------------------- 1. Frames
GROUND_Z = -3000.0
THETA_DESIGN = 15.0           # design swing, +/-
THETA_STOP = 20.0             # rubber stops, +/-
BETA_FACE_ON = 0.0
BETA_FEATHER = 45.0
BETA_STOPS = (-3.0, 48.0)
#: (theta, beta) poses that must render and pass the interference check.
POSES = [(0.0, 0.0), (20.0, 0.0), (-20.0, 0.0), (0.0, 45.0), (15.0, 10.0), (-15.0, 10.0)]

# ------------------------------------------------------- 3.1 Prism (frame P)
PRISM_OUTER = 330.0
PANEL_T = 10.0
PANEL_Z = (600.0, 1600.0)
PANEL_OUT = 165.0             # outer faces at |X|, |Y| = 165
PANEL_IN = 155.0              # inner faces at |X|, |Y| = 155
BULKHEAD_W = 310.0
BULKHEAD_T = 10.0
BULKHEAD_ZC = (850.0, 1100.0, 1350.0)   # centres; Z ranges are +/- 5
BULKHEAD_HOLE_D = 80.0
BULKHEAD_HOLE_PITCH = 200.0   # four holes on a 200 mm square
END_PLATE_W = 660.0
END_PLATE_T = 10.0
BOTTOM_PLATE_Z = (590.0, 600.0)
TOP_PLATE_Z = (1600.0, 1610.0)
NECK_HOLE_D = 51.0            # in the bottom end plate
SPIDER_MAX_ABS_XY = 150.0     # P01 stays inside |X|, |Y| <= 150
SPIDER_MAX_Z = 700.0
COLLAR_FLANGE_Z = 845.0       # P02 flange on bulkhead 1's underside

# ------------------------------------------------------- 3.2 Neck (frame P)
NECK_OD = 50.0
NECK_ID = 47.0
NECK_Z = (275.0, 850.0)
INSERT_OD = 47.0
INSERT_Z = (275.0, 335.0)
SHOULDER_OD = 56.0
SHOULDER_Z = (265.0, 275.0)
PITCH_SHAFT_OD = 35.0
PITCH_SHAFT_Z = (45.0, 265.0)
PITCH_SHAFT_BORE_D = 12.0
PITCH_SHAFT_BORE_DEPTH = 8.0
PITCH_MAGNET_FACE_Z = 44.0

# ------------------------------------------- 3.3 Hub and pitch drive (frame S)
HUB_TOP_X = (-135.0, 135.0)
HUB_TOP_Y = (-60.0, 60.0)
HUB_TOP_Z = (20.0, 35.0)
HUB_TOP_M3_XY = [(32.0, 0.0), (-32.0, 0.0)]
HUB_TOP_CABLE_HOLE = (0.0, -40.0, 12.0)         # X, Y, diameter
SIDE_PLATE_X = (123.0, 135.0)                    # and mirrored
SIDE_PLATE_Y = (-40.0, 40.0)
SIDE_PLATE_Z = (-35.0, 20.0)
STUB_D = 25.0
STUB_X = (123.0, 172.0)                          # and mirrored
STUB_FLANGE_D = 30.0
STUB_NUT_X_SPEC = (164.0, 170.0)                 # see DEVIATIONS D2
STUB_END_M3_Y = (-8.0, 8.0)
PITCH_HOUSING_OD = 110.0
PITCH_HOUSING_ID = 100.0
PITCH_HOUSING_Z = (35.0, 250.0)
WORM_WINDOW_YZ = (37.0, 160.0)
WORM_WINDOW_WH = (36.0, 30.0)                    # Y width, Z height
CAP_D = 110.0
CAP_Z = (250.0, 265.0)
LOWER_SEAT_OD = 100.0
LOWER_SEAT_ID = 55.0
LOWER_SEAT_Z = (55.0, 67.0)
PITCH_BEARING = (35.0, 55.0, 10.0)               # 6907-2RS d, D, B
PITCH_BEARING_UPPER_Z = (252.0, 262.0)
PITCH_BEARING_LOWER_Z = (56.0, 66.0)
WORM_WHEEL_MODULE = 1.0
WORM_WHEEL_TEETH = 60
WORM_WHEEL_PITCH_D = 60.0
WORM_WHEEL_OD = 62.0
WORM_WHEEL_Z = (155.0, 165.0)
WORM_PITCH_D = 14.0
WORM_OD = 16.0
WORM_AXIS_YZ = (37.0, 160.0)
WORM_X = (-15.0, 15.0)
WORM_SHAFT_D = 5.0
CLUTCH_D = 60.0
CLUTCH_Z = (170.0, 195.0)
TORSION_SPRING_D = 60.0
TORSION_SPRING_Z = (90.0, 140.0)
GEARMOTOR_AXIS_YZ = (37.0, 160.0)
GEARMOTOR_X = (62.0, 135.0)
GEARBOX_D = 25.0
GEARBOX_L = 21.0
GEARMOTOR_MOTOR_D = 24.4
GEARMOTOR_MOTOR_L = 31.0
GEARMOTOR_FACE_M3_Y = 8.5
GEARMOTOR_SHAFT = (4.0, 12.0)                    # D-cut diameter, length
PITCH_ENCODER_IC_TOP_Z = 42.5
LEVER_X = (-71.0, -59.0)
LEVER_Y = (-20.0, 20.0)
LEVER_Z = (-215.0, 20.0)
RAIL_X = (-79.0, -71.0)
RAIL_Y = (-6.0, 6.0)
RAIL_Z = (-175.0, 10.0)
BLOCK_X_SPEC = (-92.0, -79.0)                    # see DEVIATIONS D5
CARRIAGE_X = (-115.0, -92.0)
CARRIAGE_Y = (-25.0, 25.0)
CARRIAGE_H = 40.0
CARRIAGE_R_RANGE = (15.0, 140.0)
CARRIAGE_R_DEFAULT = 80.0
LEADSCREW_XY = (-104.0, 0.0)
LEADSCREW_Z_SPEC = (-185.0, 5.0)                 # exposed thread; see ASSUMED A6
LEADSCREW_D = 8.0
LEADSCREW_LEAD = 2.0
KFL08_Z = (8.0, 20.0)
STEPPER_XY = (-104.0, 0.0)
STEPPER_FACE_Z = -205.0
STEPPER_BODY_Z = (-253.0, -205.0)
COUPLER_Z_SPEC = (-205.0, -185.0)                # see DEVIATIONS D3
NEMA17_W = 42.3
NEMA17_L = 48.0
NEMA17_HOLE_SQ = 31.0
NEMA17_PILOT = (22.0, 2.0)
NEMA17_SHAFT_D = 5.0
SPRING_OD = 25.0
SPRING_RATE = 30.8                                # N/mm, design (SPEC: ~31)
SPRING_INNER_Y = 25.0                             # springs start at |Y| = 25
ROD_D = 10.0
ROLLER_D = 20.0
ROLLER_W = 10.0
ROLLER_AXLE_Y = 140.0
ROLLER_X = (-109.0, -99.0)
ROLLER_CONTACT_Y = 150.0
STRIKER_X = (-59.0, -40.0)
STRIKER_Y = (-20.0, 20.0)
STRIKER_Z = (-200.0, -180.0)
STRIKER_REACH_Y = 83.8                            # SPEC 3.5: reach at theta = +/-20
HANGER_X = (95.0, 103.0)
HANGER_Y = (-30.0, 30.0)
HANGER_Z = (-45.0, 20.0)
HANGER_M5_YZ = [(-20.0, -35.0), (20.0, -35.0), (0.0, 5.0)]
BELT_PLANE_X = 85.0
BELT_W = 9.0
BELT_X = (80.5, 89.5)
ARC_PITCH_R = 99.95
ARC_TEETH_CIRCLE = 314
ARC_SECTOR = 45.0                                 # +/- about -Z
ARC_WEB_X = (87.0, 95.0)

# ------------------------------------------------ 3.4 Belt and drive (frame A)
BELT_PITCH = 2.0
BELT_T = 1.38
GT2_PLD = 0.254               # pitch line to tooth land (GT2 2 mm)
GT2_TOOTH_H = 0.75
PULLEY_PITCH_R = 3.82
PULLEY_TEETH = 12
PULLEY_YZ = (0.0, -128.0)
IDLER_YZ = [(15.0, -109.0), (-15.0, -109.0)]
IDLER_BORE = 5.0
IDLER_CONTACT_D = 13.0
IDLER_FLANGE_D = 18.0
GEN_AXIS_YZ = (0.0, -128.0)
GEN_CAN_D = 88.0
GEN_CAN_X = (48.0, 76.0)
GEN_MOUNT_FACE_X = 43.0
GEN_MOUNT_FACE_D = 60.0
GEN_M3_PCD = 30.0
GEN_CENTRE_RELIEF_D = 16.0
GEN_SHAFT_D = 5.0
GEN_OUT_SHAFT_END_X = 92.0
GEN_REAR_SHAFT_END_X = 38.0
GEN_MAGNET_FACE_X = 35.5
GEN_ENCODER_IC_TOP_X = 34.0
P05_UPRIGHT_X = (35.0, 43.0)
P06_UPRIGHT_X = (93.0, 101.0)
P06_TOP_R_MIN = 110.0
P09_R_MAX = 106.0
P09_HALF_ANGLE = 65.0

# ------------------------------------------------------- 3.5 Hinge (frame A)
CHEEK_X = (140.0, 160.0)                          # and mirrored
CHEEK_Y = (-160.0, 160.0)
CHEEK_Z = (-280.0, 50.0)
CHEEK_BORE_D = 47.0
HINGE_BEARING = (25.0, 47.0, 12.0)                # 6005-2RS d, D, B
HINGE_BEARING_XC = 150.0
RETAINER_OD = 80.0
RETAINER_ID = 30.0
RETAINER_X = (160.0, 164.0)
RETAINER_PCD = 64.0
P15_X = (-178.0, -172.0)
P15_D = 24.0
HINGE_MAGNET_FACE_X = -178.5
HINGE_ENCODER_IC_TOP_X = -180.0
REACTION_PLATE_X = (-125.0, -85.0)
REACTION_PLATE_Y = (150.0, 160.0)                 # and mirrored
REACTION_PLATE_Z = (-280.0, 10.0)
SPACER_BLOCK_X = (-140.0, -125.0)
STOP_POST_X = (-58.0, -32.0)
STOP_POST_Y = (99.0, 124.0)                       # |Y|
STOP_POST_Z = (-280.0, -150.0)
STOP_POST_WALL = 3.0
BUMPER_Y = (84.0, 99.0)                           # |Y|
BUMPER_X = (-56.0, -34.0)
BUMPER_Z = (-195.0, -160.0)

# ------------------------------------------------ 3.6 Head, yaw, post (frame A)
BASE_PLATE_X = (-360.0, 230.0)
BASE_PLATE_Y = (-170.0, 170.0)
BASE_PLATE_Z = (-295.0, -280.0)
YAW_FLANGE_D = 160.0
YAW_FLANGE_Z = (-307.0, -295.0)
YAW_FLANGE_BOLTS = 6                              # M10
YAW_SHAFT_OD = 50.0
YAW_SHAFT_ID = 38.0
YAW_SHAFT_Z = (-640.0, -307.0)
YAW_HOUSING_OD = 114.3
YAW_HOUSING_WALL = 6.0
YAW_HOUSING_Z = (-560.0, -320.0)
YAW_BEARING = (50.0, 80.0, 20.0)                  # 32010 d, D, T
YAW_BEARING_Z = [(-345.0, -325.0), (-545.0, -525.0)]
SLIP_RING_Z = (-700.0, -640.0)
SLIP_RING_BODY = (22.0, 35.0)                     # diameter, length
SLIP_RING_FLANGE = (44.0, 3.0, 34.0)              # diameter, thickness, PCD
P23_Z = (-720.0, -640.0)
POST_OD = 114.3
POST_WALL = 6.0
POST_BORE = 102.3
POST_Z = (-2985.0, -560.0)
POST_BASE = (300.0, 15.0)                         # square, thickness; Z -3000..-2985
GUY_COLLAR_Z = -1000.0
GUY_COLLAR = (140.0, 20.0)                        # OD, height
TAIL_BOOM_OD = 40.0
TAIL_BOOM_WALL = 2.0
TAIL_BOOM_YZ = (0.0, -260.0)
TAIL_BOOM_X_SPEC = (150.0, 920.0)                 # see DEVIATIONS D1
TAIL_SADDLE_X = (170.0, 215.0)
VANE_T = 4.0
VANE_X = (480.0, 900.0)
VANE_UPPER_Z = (-239.5, -140.0)
VANE_LOWER_Z = (-380.0, -280.5)
VANE_CLAMP_X = (520.0, 690.0, 860.0)
ANEMO_BOOM_OD = 25.0
ANEMO_BOOM_WALL = 2.0
ANEMO_BOOM_YZ = (120.0, -260.0)
ANEMO_BOOM_X_SPEC = (-650.0, -200.0)              # see ASSUMED A12
ANEMO_SADDLE_X = (-300.0, -230.0)
ANEMO_MAST_XY = (-650.0, 120.0)
ANEMO_MAST_Z_SPEC = (-260.0, 150.0)               # see ASSUMED A12
ANEMO_TEE = (-650.0, 120.0, -260.0)
ANEMO_MAST_TOP_Z = 150.0
ANEMO_BODY = (50.0, 80.0)                         # diameter, height
ANEMO_SPIGOT = (20.0, 60.0)
ANEMO_CUP_CIRCLE_D = 180.0
ANEMO_CUP_Z = 260.0
DUMP_X = (-300.0, -228.0)
DUMP_Y = (-25.0, 25.0)
DUMP_Z = (-325.0, -295.0)
ENCL_X = (-355.0, -185.0)
ENCL_Y = (-75.0, 75.0)
ENCL_Z = (-280.0, -215.0)
BATTERY_X = (250.0, 550.0)
BATTERY_Y = (-100.0, 100.0)
BATTERY_Z = (-3000.0, -2750.0)
CABLE_CLIP_BOOM_X = (-350.0, -500.0)
CABLE_CLIP_MAST_Z = -50.0

# ------------------------------------------------ 4. Swinging envelope
CLEARANCE_MIN = 3.0

# ------------------------------------------------ 6. Bought interface parts
ENCODER_PCB = (25.4, 25.4, 1.6)
ENCODER_HOLE_SQ = 20.3
ENCODER_HOLE_D = 2.5
MAGNET = (6.0, 2.5)                               # diameter, thickness
ENCODER_AIR_GAP = 1.5
F695 = (5.0, 13.0, 4.0, 15.0, 1.0)                # d, D, B, flange D, flange t
GLAND_M20 = (20.5, 24.0)                          # hole, hex
GLAND_M16 = (16.5, 20.0)

# ------------------------------------------------ 7. Controller PCB envelope
PCB_W = 130.0                                     # board x, along assembly +X
PCB_H = 100.0                                     # board y, along assembly +Y
PCB_T = 1.6
PCB_HOLES = [(4.0, 4.0), (126.0, 4.0), (4.0, 96.0), (126.0, 96.0)]
PCB_HOLE_D = 3.2
PCB_COMPONENT_MAX_H = 25.0
PCB_BOTTOM_Z = -269.0
PCB_CENTRE_XY = (-270.0, 0.0)
PCB_STANDOFF_H = 6.0
ENCL_FLOOR_TOP_Z = -275.0

# ---------------------------------------------------------------------------
# ASSUMED details: numbers the SPEC does not give. Each is a VERIFY entry.
# ---------------------------------------------------------------------------
YAW_AXIS_XY = (0.0, 0.0)                          # A1
STUB_FLANGE_T = 4.0                               # A2
STUB_NUT_OD = 38.0                                # A2 (KM5 round nut, M25 x 1.5)
HINGE_INNER_RING_OD = 32.0                        # A3 bearing rings as modelled
HINGE_OUTER_RING_ID = 40.0
PITCH_INNER_RING_OD = 40.5
PITCH_OUTER_RING_ID = 49.5
YAW_CONE_OD = 60.0
YAW_CUP_ID = 68.0
CAP_LIP_ID = 47.0                                 # A4 cap and seat lips
CAP_TOP_BORE_D = 64.0
SEAT_LIP_ID = 47.0
SHAFT_SPACER = (43.0, 3.0)                        # A4 OD, length (Z 262..265)
WHEEL_HUB = (40.0, 5.0)                           # A5 worm-wheel hub to the clutch
LEADSCREW_JOURNAL_TOP_Z = 18.0                    # A6 machined ends of the screw
LEADSCREW_BOTTOM_Z = -193.0                       # A6
KFL08 = (48.0, 27.0, 37.0, 22.0)                  # A7 length, width, bolt pitch, boss D
SPRING_WIRE_D = 4.0                               # A8 (gives ~31 N/mm with ~9 coils)
SPRING_COILS = 9.0
ROD_END_Y = 105.0                                 # A8 rod fixed in the carriage
SLEEVE = (14.0, 60.0)                             # A8 fork sleeve OD, length
FORK_BACK = 18.0                                  # A8 fork bridge, from the axle
FORK_PLATE_T = 4.0
STEPPER_CHAMFER = 4.5                             # A9 NEMA-17 body corner chamfer
COUPLER_D = 19.0                                  # A9
GEARMOTOR_TAIL_D = 22.0                           # A10 rear encoder/terminal cap
COUPLING_D = 10.0                                 # A10 worm-shaft to gearmotor coupling
COUPLING_X = (43.0, 61.0)
WORM_SHAFT_X = (-25.0, 49.0)
IDLER_X = (80.2, 89.8)                            # A11 contact width between flanges
IDLER_FLANGE_T = 1.0
IDLER_BOLT_X = (77.5, 97.0)
PULLEY_FLANGE_D = 13.0
TEE_SOCKET_STOP = 15.0                            # A12 tubes stop short of P18's centre
ANEMO_BODY_BOTTOM_Z = 180.0                       # A13
BELT_END_PHI = 43.0                               # A14 belt ends under P04
GLAND_Z = -250.0                                  # A15 gland heights and X positions
GLAND_M20_X = (-310.0, -270.0, -230.0)
GLAND_M16_X = (-315.0, -285.0, -255.0, -225.0)
GLAND_VENT_YZ = (0.0, -245.0)
ENCL_WALL_T = 3.0                                 # A15 assumed P20 wall
YAW_HOUSING_FLANGE = (200.0, 12.0)                # A16 OD, thickness
YAW_SEAT_LIP_ID = 70.0
SADDLE_W = 24.0                                   # A17 U-bolt saddles
TAIL_SADDLE_W = 18.0                              # A17 (X 161..179 at X 170 clears the cheek)
UBOLT_D = 6.0
LEVER_ANGLE = (25.0, 4.0)                         # A18 angle leg, thickness
CHEEK_TOP_R = 40.0                                # A19 cheek top corner radius
POST_FLANGE = (200.0, 12.0)                       # A16 post top flange

ASSUMED = {
    "A1": "Yaw axis at X = 0, Y = 0 (SPEC 3.6 gives the yaw parts' Z ranges and diameters but no XY).",
    "A2": "Stub-axle flange 4 thick (X 119..123 on the -X stub); axial nut is a KM5 round nut, OD 38.",
    "A3": "Bearings drawn as an inner and an outer ring only (6005: 25/32 and 40/47; 6907: 35/40.5 and 49.5/55; 32010: 50/60 and 68/80).",
    "A4": "Pitch-housing cap: lip ID 47 under the upper bearing (Z 250..252), bearing bore 55 (Z 252..262), clearance bore 64 above (Z 262..265); lower seat lip ID 47 at Z 55..56; shaft spacer OD 43 at Z 262..265 carries the shoulder load onto the upper inner ring.",
    "A5": "Worm wheel has a hub OD 40 from its top face (Z 165) to the clutch (Z 170); bore 36 so it can turn on the shaft when the clutch is off.",
    "A6": "Lead screw: SPEC Z -185..5 is the threaded length; machined Ø8 ends continue down into the coupler (to Z -193) and up through the KFL08 (to Z 18).",
    "A7": "KFL08 drawn as a 48 x 27 x 5 two-bolt flange (37 mm bolt pitch, long axis along Y) with a Ø22 boss, Z 8..20.",
    "A8": "Spring wire Ø4, mean coil Ø21, ~9 active coils (~31 N/mm); spring rod Ø10 fixed in the carriage from |Y| 25 to 105; each fork slides on its rod on a Ø14 x 60 sleeve; fork bridge 18 behind the roller axle. Both springs are preloaded so both rollers stay on their plates at every pose (the roller positions are solved per pose).",
    "A9": "NEMA-17 body corners chamfered 4.5; flexible coupler Ø19.",
    "A10": "Gearmotor: gearbox X 62..83, motor X 83..114, rear encoder/terminal cap Ø22 X 114..135; worm shaft Ø5 X -25..49; gearmotor shaft Ø4 X 50..62; coupling Ø10 X 43..61.",
    "A11": "Idlers: contact Ø13 over X 80.2..89.8, flanges Ø18 x 1 outside that, on Ø5 bolts X 77.5..97 into P06.",
    "A12": "Anemometer boom and mast both run to P18's centre in the SPEC, which would make them intersect; each is modelled stopping 15 mm short, inside P18's sockets (boom X -635..-200, mast Z -245..150).",
    "A13": "Anemometer body Z 180..260 (spigot Z 120..180, entering the mast bore through P19); cups Ø50 on Ø180 at Z 260.",
    "A14": "Belt ends at phi = +/-43 deg on the arc (under the P04 clamps).",
    "A15": "Enclosure glands at Z -250: M20 at X -310, -270, -230 on the -Y wall; M16 at X -315, -285, -255, -225 on the +Y wall; M12 vent at Y 0, Z -245 on the -X wall; wall 3 mm. Agree with P20.",
    "A16": "Yaw housing bottom flange and post top flange Ø200 x 12, meeting at Z -560; bearing seats are rings ID 80 with a lip ID 70.",
    "A17": "U-bolt saddles: 24 wide aluminium blocks (18 wide on the tail boom, so the one at X 170 clears the +X cheek at X 160); U-bolts M6. The tail boom rests on the plate (its underside is the plate's top face, SPEC 3.6), so its saddles are cradles split under the tube.",
    "A18": "Lever bolted to the top plate through an aluminium angle 25 x 4 on its +X face.",
    "A19": "Cheek top corners rounded R40; four M5 holes on Ø64 PCD for the retainer.",
    "A21": "Encoder breakouts carry their JST-GH connector on the back face, at one edge: on the IC side its 4.25 mm height would hit the shaft (pitch), P15 (hinge) or P05 (generator), which are 1.5 to 3.5 mm from the board. P07, P12 and P14 must leave 4.5 mm behind the board at that edge.",
    "A22": "Detail features the SPEC does not give are drawn for recognition only: bolt holes and their positions in the plates, the cheeks' lightening windows and base bolts, nut slots, grooves on bought parts, the base-plate hole pattern, the post's anchor holes and gussets, the guy-collar lugs, the dump resistor's and battery box's shapes. Dimension them from the parts in hand.",
    "A20": "Controller PCB components drawn as representative blocks (terminal blocks, headers, USB-C, capacitors, MCU, inductor, MOSFETs) until the pcb repo provides a STEP.",
}

# ---------------------------------------------------------------------------
# DEVIATIONS: SPEC numbers that conflict with each other. The model changes
# the one named here; each is also reported as a SPEC issue.
# ---------------------------------------------------------------------------
TAIL_BOOM_X = (161.0, 920.0)                      # D1
STUB_NUT_X = (165.0, 170.0)                       # D2
COUPLER_Z = (-202.0, -185.0)                      # D3
STRIKER_CHAMFER = True                            # D4
BLOCK_X = (-84.0, -74.0)                          # D5 real MGN12H; spacer -92..-84
BLOCK_SPACER_X = (-92.0, -84.0)                   # D5
STOP_POST_SECTION = (26.0, 25.0)                  # D6

DEVIATIONS = {
    "D1": "Tail boom: SPEC X 150..920, but the +X cheek occupies X 140..160 at the boom (Y 0, Z -280..-240). Modelled X 161..920.",
    "D2": "Hinge axial nut: SPEC X 164..170 puts the turning nut (frame S) face to face with the fixed retainer (X 160..164, frame A). Modelled X 165..170 (1 mm running gap) with an inner-ring spacer through the retainer bore.",
    "D3": "Stepper coupler: SPEC Z -205..-185 overlaps the NEMA-17's Ø22 x 2 pilot (Z -205..-203). Modelled Z -202..-185.",
    "D4": "Stop striker: with square corners its bottom outer edge (Y 20, Z -200) reaches |Y| 87.2 at theta 20, 3.2 mm into the bumpers (|Y| 84). SPEC's 83.8 is the mid-height (Z -190) point. The striker's bottom outer edges are chamfered so the chamfer lands flat at |Y| 83.8 at theta +/-20 (contact Z -182..-172).",
    "D5": "MGN12H block: SPEC X -92..-79 places the block wholly beyond the rail top, but an MGN12H is 13 high from the rail base, so on a rail X -79..-71 its top face is at X -84. Modelled a real block (X -84..-74, wrapping the rail) plus an 8 mm aluminium spacer X -92..-84, keeping the SPEC carriage position.",
    "D6": "Stop posts: SPEC says 30 x 30 x 3 square tube but gives a 26 (X) x 25 (Y) envelope. Modelled 26 x 25 x 3 rectangular tube filling the envelope.",
}
