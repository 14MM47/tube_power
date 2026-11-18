#!/usr/bin/env python3
"""Load case, hold path, trip force and solenoid/reservoir sizing for the Lantern 330-G zero-hold feather latch.

Reproduces every number in designs/lantern-330-g/cad/latch.md (revision B, after the 17 Nov 2026 design
review). Standard library only.

    python3 tools/feather_latch_calc.py

Mechanism (latch.md section 2): a roller pawl on the worm-wheel carrier sits in a single slot in a collar
keyed to the pitch shaft (stage 1). The slot has a planar load flank 30 deg from radial. The pawl's tail is
held by a roller sear (stage 2). The sear is a toggle: an adjustable stop holds its roller 0.15 +/- 0.05 mm
on the closing side of the dead-centre line, so the load holds it shut; the trip only has to push it past
dead centre, after which the load opens it. A stationary pull solenoid outside the pitch housing trips the
sear through a hook arc (frame S, concentric with the shaft) that bears on a small roller on the sear's tab
at every latched pitch angle from -3 to +48 deg.
"""
from __future__ import annotations

import math

G0 = 9.81
RHO = 1.225
E_STEEL = 206e3            # MPa
NU = 0.3

# ------------------------------------------------------------------ load case
CM_PITCH = 0.10            # calculator: aerodynamic moment coefficient about the prism axis (assumed there; V8 b)
D, LP = 0.330, 1.000       # prism face width and height, m
U_DESIGN = 45.0            # gust during a feather request at the 40 m/s cut-out (README "pitch-drive torque ~13.5")
DYN = 1.5                  # dynamic factor on the aerodynamic part (gusts, galloping at 3.7 Hz, stop impacts)
SF_STRENGTH = 2.5          # strength factor on the dynamic hold torque (no yield)
FEATHER_SF = 1.25          # spring torque at 45 deg >= 1.25 x the peak pitch moment (review M10)

# torsion spring (review M6/M10): Ø7 music wire, mean Ø76, indexed anchor sets the preload at assembly
T_SPRING_45 = 18.5         # N m at 45 deg (nominal)
K_SPRING = 0.17            # N m per degree
SPRING_TOL = 0.05          # +/- acceptance band (set to +/-3 % at assembly with the indexed anchor; annual check +/-5 %)
WIRE_D = 7.0               # mm, EN 10270-1 DH / ASTM A228 music wire
COIL_DM = 76.0             # mm, mean coil diameter
SUT_A, SUT_M = 2211.0, 0.145   # Sut = A / d^m (MPa, mm), music wire (Shigley table 10-4)

BETA_GEN = (-3.0, 15.0)    # latched range while generating: internal stop -3 .. top of the pitch-control range
BETA_MOVE = (-3.0, 48.0)   # latched range during pitch moves (planned park drive, restart, powered worm feather)


def spring_torque(beta, f=1.0):
    return f * (T_SPRING_45 + K_SPRING * (45.0 - beta))


def aero_moment(U):
    return CM_PITCH * 0.5 * RHO * U**2 * D**2 * LP


# ------------------------------------------------------------ swing dynamics
Z_LATCH = 0.185            # m, latch height above the hinge axis in frame S
I_HINGE = 1.89             # kg m2 about the hinge (README section 5)
E_STOP = 60.0              # J, fault energy into the +/-20 deg stops (SPEC V7)
R_STRIKER = 0.19           # m, striker contact radius about the hinge
STOP_DEFLECTION = 0.004    # m, effective bumper deflection (TPU 95A, 15 mm thick; ASSUMED)

# ---------------------------------------------------------------- stage 1 geometry (layout.py)
R_ROLLER_C = 31.0          # mm, pawl-roller centre radius, latched (LATCH_ROLLER)
R_ROLLER = 8.0             # mm, NATV 5-PP outer radius
FLANK_DEG = 30.0           # load flank, degrees from radial (contact normal 30 deg from tangential)
COLLAR_OD = 61.0           # mm (review M2: real planar flank, contact >= 2 mm from the edge radius)
EDGE_R = 0.5               # mm, edge radius where the flank meets the OD (outside the contact zone)
A_PAWL = 16.0              # mm, arm of the roller's radial force about the pawl pivot
B_PAWL = 55.75             # mm, arm of the sear force about the pawl pivot (|tail - pivot|)
R_PAWL_PIN = 4.0           # mm, pawl pivot pin radius (DU bush)
TAIL_SECTION = (9.5, 8.0)  # mm, pawl tail arm in-plane depth (R 38..47.5) x thickness (Z 192..200)
TAIL_ROOT = 6.0            # mm, from the pivot to the tail's root at the boss
OPEN_TAIL_GAP = 2.44       # mm, opened pawl tail to the shaft (CAD, latch_check)
CROWN_R = 500.0            # mm, NATV outer-ring crown radius (catalogue profile; ASSUMED, V8 e)
FLANK_LEN = 11.0           # mm, collar height = flank length along Z

# ---------------------------------------------------------------- stage 2 geometry
L2 = 16.0                  # mm, sear pivot to sear-roller centre
R_SEAR_ROLLER = 8.0        # mm, INA RSTO 5 (Fw 7, D 16, B 7.8) yoke-type needle track roller
FW_SEAR_ROLLER = 7.0       # mm, its hardened pin (raceway)
C0_SEAR_ROLLER = 3600.0    # N, RSTO 5 basic static rating (catalogue class; VERIFY V8 e)
C0_SEAR_PIVOT = 1900.0     # N, HK0609 drawn-cup needle bush on a hardened Ø6 pin (catalogue class; VERIFY V8 e)
FW_SEAR_PIVOT = 6.0
E2 = (0.10, 0.15, 0.20)    # mm, sear positive engagement set by the stop: min, nominal, max
STOP_ARM = 10.0            # mm, sear pivot to the stop contact on the sear-roller arm (clear of the roller-pin boss)
TRIP_OVERTRAVEL = 0.30     # mm, roller travel past dead centre that the trip must give (then the load opens it)
K_SEAR_SPRING = 15.0       # N mm, sear reset spring moment
L_TAB = 23.83              # mm, distance from the sear pivot to the radial line through the tab roller (constant
                           #     with beta: the hook arc is concentric with the shaft, so its push is radial)
R_TAB_ROLLER = 3.5         # mm, 683-2RS stainless (3 x 7 x 3) on the tab
TAB_ROLLER_DRAG = 0.3      # N mm, its seal drag (aged)
R_HOOK = 44.6              # mm, hook arc inner radius (frame S); roller outer radius 43.1
HOOK_GAP = (1.3, 1.5, 1.7) # mm, radial running gap hook to tab roller (min, nominal, max; set by the stem thread)
S_REST = 4.4               # mm, plunger gap at rest (set by the out-stop nut)
STEM_YZ = (24.0, 222.0)    # stem axis (Y, Z) in frame S
CONTACT_Z = 209.0          # hook contact height
X_GUIDE, X_PLUNGER = -47.0, -82.0   # centres of the wall guide bush and of the plunger's bearing in its tube
RETURN_SPRING = 1.0        # N, return spring at the trip position (holds the hook out against 3.6 g of swing)
SEAL_DRAG = 0.3            # N, greased stem seal in the guide bush

# ------------------------------------------------------------------ solenoid
# Guardian Electric LT8x16-I-12D (A420-064851-00): 12 V DC, 6.2 ohm +/-5 %, 24.4 W, 25 % duty.
# Typical pull force @ 20 C, 25 % row (= 12 V on this coil, 1.94 A): stroke in -> N.
SOL_R20 = 6.2
SOL_TOL = 0.05
SOL_V_RATED = 12.0
SOL_CURVE = [(0.050, 22.2), (0.125, 15.3), (0.250, 9.7), (0.375, 7.0), (0.500, 4.2), (0.625, 2.8), (0.750, 0.8)]
ALPHA_CU = 0.00393
T_HOT = 60.0
I_REG = 1.94               # A, regulated pulse current (= the 25 % duty rated current, 12 V / 6.2 ohm)
I_REG_TOL = 0.02           # +/- regulation tolerance
R_LOOP = 0.20              # ohm: cable loop 2 x ~1.5 m of 0.5 mm2 (0.10) + MOSFET + sense resistor + connectors
PULSE_S = 0.100
PULSES = 3
BUCK_EFF = 0.85


def sol_force(gap_mm, current_a):
    """Pull force at a gap, scaled from the 12 V row as (I / I_rated)^2 (log-linear between points)."""
    pts = [(25.4 * s, f) for s, f in SOL_CURVE]
    if gap_mm <= pts[0][0]:
        f = pts[0][1]
    else:
        f = pts[-1][1]
        for (g0, f0), (g1, f1) in zip(pts, pts[1:]):
            if g0 <= gap_mm <= g1:
                f = f0 * (f1 / f0) ** ((gap_mm - g0) / (g1 - g0))
                break
    i_rated = SOL_V_RATED / SOL_R20
    return f * (current_a / i_rated) ** 2


def hertz_point(w, rx, ry):
    """Elliptical Hertz contact of a crowned roller on a flat (Hamrock-Brewe). Returns p_max, a, b (MPa, mm)."""
    e_ = E_STEEL / (1 - NU**2)
    rp = 1.0 / (1.0 / rx + 1.0 / ry)
    alpha = ry / rx
    k = 1.0339 * alpha**0.636
    eps = 1.0003 + 0.5968 / alpha
    a = (6 * k**2 * eps * w * rp / (math.pi * e_)) ** (1 / 3)
    b = (6 * eps * w * rp / (math.pi * k * e_)) ** (1 / 3)
    return 3 * w / (2 * math.pi * a * b), a, b


def hertz_line(w, r, length):
    e_ = E_STEEL / (1 - NU**2)
    b = math.sqrt(8 * w * r / (math.pi * length * e_))
    return 2 * w / (math.pi * b * length), b


def stage1(T):
    """Forces at the slot for a latch torque T (N m). The contact normal passes through the roller centre."""
    arm = R_ROLLER_C * math.cos(math.radians(FLANK_DEG))          # mm, moment arm of the contact normal
    N = T * 1000 / arm
    F1 = N * math.cos(math.radians(FLANK_DEG))                     # along the tangent: into the pawl pivot
    Fr = N * math.sin(math.radians(FLANK_DEG))                     # outward: opens the pawl
    F2 = Fr * A_PAWL / B_PAWL
    return N, F1, Fr, F2


def trip_moment(F2, e2, mu_b, drag):
    """Opening moment the trip must give at the sear pivot (N mm): toggle offset, roller, pivot, reset spring."""
    m_e = F2 * e2
    m_roll = (mu_b * F2 * FW_SEAR_ROLLER / 2 + drag) * (L2 + R_SEAR_ROLLER) / R_SEAR_ROLLER
    m_piv = mu_b * F2 * FW_SEAR_PIVOT / 2 + drag
    return m_e + m_roll + m_piv + K_SEAR_SPRING, (m_e, m_roll, m_piv)


def solenoid_force_needed(m_trip, phi_deg, mu_g, mu_p):
    """Pull at the solenoid for a trip moment, with the hook contact at angle phi (frame S)."""
    fn = m_trip / L_TAB + TAB_ROLLER_DRAG / R_TAB_ROLLER * 34.0 / L_TAB     # normal push on the tab roller
    ph = math.radians(phi_deg)
    fx, fy = fn * math.cos(ph), fn * math.sin(ph)
    xc, yc = R_HOOK * math.cos(ph), R_HOOK * math.sin(ph)
    d = math.hypot(yc - STEM_YZ[0], CONTACT_Z - STEM_YZ[1])            # offset of the contact from the stem axis
    s = X_GUIDE - X_PLUNGER
    r_couple = fx * d / s
    r_g = r_couple + fy * (xc - X_PLUNGER) / s
    r_p = r_couple + fy * (xc - X_GUIDE) / s
    return fx + mu_g * r_g + mu_p * r_p + RETURN_SPRING + SEAL_DRAG, fn


def main():
    o = print
    sp_tol = 1.0 + SPRING_TOL
    sm_tol = 1.0 - SPRING_TOL
    m40, m45 = aero_moment(40.0), aero_moment(U_DESIGN)
    o("== Torsion spring and load case (review M6, M10)")
    o(f"spring torque (nominal): {spring_torque(45):.1f} N m at 45, {spring_torque(15):.2f} at 15, "
      f"{spring_torque(0):.2f} at 0, {spring_torque(-3):.2f} at -3 deg; band +/-{100 * SPRING_TOL:.0f} %")
    o(f"aero pitch moment CM q D^2 L: {m40:.1f} N m at 40 m/s, {m45:.1f} at 45 m/s; x{DYN}: {DYN * m45:.2f}")
    t_feather = spring_torque(45, sm_tol)
    o(f"feather: spring at 45 deg, -{100 * SPRING_TOL:.0f} %: {t_feather:.1f} N m vs {FEATHER_SF} x {m45:.1f} = "
      f"{FEATHER_SF * m45:.1f} -> margin {t_feather / m45:.2f} x the peak pitch moment")
    t_hold_s = spring_torque(BETA_GEN[0], sp_tol)
    t_static = t_hold_s + m45
    t_dyn = t_hold_s + DYN * m45
    t_ult = SF_STRENGTH * t_dyn
    o(f"hold torque (spring +{100 * SPRING_TOL:.0f} % at {BETA_GEN[0]:+.0f}): static {t_static:.1f}, dynamic "
      f"{t_dyn:.1f} (x{DYN} on aero), strength {t_ult:.0f} N m (x{SF_STRENGTH})")
    least = spring_torque(BETA_GEN[1], sm_tol) - DYN * m45
    o(f"least latch torque, generating range (spring -{100 * SPRING_TOL:.0f} % at {BETA_GEN[1]:+.0f}, aero x{DYN} "
      f"against it): {least:.2f} N m -> {'never reverses' if least > 0 else 'REVERSES'}")
    for b in (30.0, 48.0):
        lm = spring_torque(b, sm_tol) - DYN * m45
        o(f"  during pitch moves at {b:+.0f} deg in a 45 m/s gust: {lm:+.2f} N m "
          f"({'reverses onto the reverse flank (pushes the roller in; no sear load)' if lm < 0 else 'no reversal'})")
    # spring stress
    sut = SUT_A / WIRE_D**SUT_M
    c = COIL_DM / WIRE_D
    ki = (4 * c * c - c - 1) / (4 * c * (c - 1))
    sig = lambda t: ki * 32 * t * 1000 / (math.pi * WIRE_D**3)
    s_max, s_45, s_0 = sig(spring_torque(-3, sp_tol)), sig(spring_torque(45, sm_tol)), sig(spring_torque(0, sp_tol))
    allow = 0.78 * sut
    # Goodman, bending, unpeened (Shigley: Zimmerli Ssa 241 / Ssm 379 MPa -> Sr = 2 Ssa / 0.577)
    sr = 2 * 241 / 0.577
    se = (sr / 2) / (1 - (sr / 2) / sut)
    sa, sm = (s_0 - s_45) / 2, (s_0 + s_45) / 2
    n_g = 1 / (sa / se + sm / sut)
    n_turns = E_STEEL * WIRE_D**4 / (10.8 * COIL_DM * K_SPRING * 1000 * 360)
    o(f"spring: Ø{WIRE_D} wire, mean Ø{COIL_DM:.0f} (OD {COIL_DM + WIRE_D:.1f}), C {c:.1f}, Ki {ki:.3f}, "
      f"~{n_turns:.1f} active turns (body ~{(n_turns + 1) * WIRE_D:.0f} mm); Sut {sut:.0f} MPa")
    o(f"  bending stress {s_45:.0f} MPa at 45 (-5 %), {s_0:.0f} at 0, {s_max:.0f} at -3 (+5 %); static allowable "
      f"0.78 Sut = {allow:.0f} -> margin {allow / s_max:.2f}; Goodman (park/restart cycle 45 <-> 0, infinite life) "
      f"n = {n_g:.2f}")
    o("  (old spring: Ø5.5 wire, 14.0 N m at 45 -> 1,324 MPa at 20 N m against ~1,347 allowable: no margin)")

    def work(b0, b1, f=1.0):
        n = 200
        db = (b1 - b0) / n
        return sum(spring_torque(b0 + (k + 0.5) * db, f) * math.radians(db) for k in range(n))
    aero_w = m45 * math.radians(48 - (-3))
    o("feather-stop energy (review M13): spring work to the stop, +5 % spring; plus up to "
      f"{m45:.1f} N m of pitch moment acting with it in a storm:")
    for b0, why in ((-3.0, "storm/fault trip at the -3 stop"), (0.0, "monthly full-load trip at beta 0"),
                    (40.0, "planned park, fired at 40 deg")):
        ws = work(b0, 45.0, sp_tol)
        wa = m45 * math.radians(45 - b0)
        o(f"  from {b0:+.0f} ({why}): spring {ws:.1f} J" + (f", + aero {wa:.1f} J = {ws + wa:.1f} J in a storm"
                                                              if b0 < 10 else " (low wind at a park)"))
    o(f"  design the buffer for {work(-3, 45, sp_tol) + aero_w:.0f} J (rare) and ~2 J x ~5,000 parks/yr")

    o("\n== Accelerations at the latch (Z_S = 185 mm above the hinge)")
    for name, amp, f in (("generating 40 m/s, +/-8.8 deg at 3.66 Hz", 8.8, 3.66),
                         ("+/-15 deg at 2.06 Hz (15 m/s)", 15.0, 2.06),
                         ("+/-20 deg (stops) at 3.7 Hz", 20.0, 3.7)):
        w = 2 * math.pi * f
        th = math.radians(amp)
        at = th * w**2 * Z_LATCH
        ac = (th * w) ** 2 * Z_LATCH
        o(f"{name}: tangential {at:.1f} m/s2 ({at / G0:.1f} g, along Y_S), centripetal {ac:.1f} m/s2 (along -Z_S)")
    w0 = math.sqrt(2 * E_STOP / I_HINGE)
    alpha = w0**2 / (STOP_DEFLECTION / R_STRIKER)
    a_imp = alpha * Z_LATCH
    o(f"end-stop impact, {E_STOP:.0f} J into a {1000 * STOP_DEFLECTION:.0f} mm bumper: {a_imp:.0f} m/s2 "
      f"({a_imp / G0:.0f} g) along Y_S at the latch")

    o("\n== Stage 1: roller pawl on the planar load flank (review M2)")
    arm = R_ROLLER_C * math.cos(math.radians(FLANK_DEG))
    # contact point and flank length to the OD
    ct, cr = -R_ROLLER * math.cos(math.radians(FLANK_DEG)), R_ROLLER_C - R_ROLLER * math.sin(math.radians(FLANK_DEG))
    rc = math.hypot(ct, cr)
    ft, fr_ = -math.sin(math.radians(FLANK_DEG)), math.cos(math.radians(FLANK_DEG))
    s = 0.0
    while math.hypot(ct + s * ft, cr + s * fr_) < COLLAR_OD / 2:
        s += 0.001
    lift_to = COLLAR_OD / 2 + R_ROLLER + 0.5
    o(f"contact point at R {rc:.2f} mm; contact normal through the roller centre (R {R_ROLLER_C:.0f}), moment arm "
      f"{arm:.2f} mm about the shaft. Collar OD {COLLAR_OD:.0f}: the flank runs {s:.2f} mm past the contact to the "
      f"OD; with a {EDGE_R} mm edge radius, {s - EDGE_R:.2f} mm of flat flank beyond the contact centre")
    o(f"release: the roller centre must reach R {lift_to:.1f} (lift {lift_to - R_ROLLER_C:.1f} mm) -> pawl opens 30 deg")
    rows = {}
    for name, T in (("static", t_static), ("dynamic", t_dyn), ("strength", t_ult), ("least", least)):
        N, F1, Fr, F2 = stage1(T)
        rows[name] = (T, N, F1, Fr, F2)
        o(f"{name:8s} T {T:6.1f} N m: roller normal {N:6.0f} N, tangential {F1:6.0f} N (into the pawl pivot), "
          f"outward {Fr:5.0f} N, sear force F2 {F2:5.1f} N")
    Nd, F2d = rows["dynamic"][1], rows["dynamic"][4]
    Nu, F2u = rows["strength"][1], rows["strength"][4]
    t_mean = spring_torque(5.0, sp_tol)
    Nm = stage1(t_mean)[0]
    for lab, w in (("mean (spring at 5 deg, +5 %)", Nm), ("dynamic", Nd), ("strength", Nu)):
        p, a, b = hertz_point(w, R_ROLLER, CROWN_R)
        pl, bl = hertz_line(w, R_ROLLER, FLANK_LEN)
        o(f"  flank contact, {lab} {w:.0f} N: crowned NATV (R {CROWN_R:.0f}) p_max {p:.0f} MPa, ellipse "
          f"{2 * a:.1f} x {2 * b:.2f} mm, max shear at ~{0.78 * b:.2f} mm deep; cylindrical roller (line, "
          f"{FLANK_LEN:.0f} mm) {pl:.0f} MPa")
    o("  -> collar 18CrNiMo7-6 case-hardened 58-62 HRC, CHD >= 0.6 mm (>> 2 x the shear depth); contact fatigue "
      "limit ~1,500 MPa; static limit ~4,000 MPa")
    tb, tt = TAIL_SECTION
    wz = tt * tb**2 / 6
    for lab in ("dynamic", "strength"):
        mt = rows[lab][4] * (B_PAWL - TAIL_ROOT)
        o(f"pawl tail bending at the root, {lab}: F2 {rows[lab][4]:.0f} N x {B_PAWL - TAIL_ROOT:.1f} mm = "
          f"{mt / 1000:.1f} N m on {tb} x {tt} mm -> {mt / wz:.0f} MPa (42CrMo4 QT Rp0.2 >= 650)")
    o(f"pawl open {30} deg: tail R 38..47.5 clears the shaft by {OPEN_TAIL_GAP} mm (the old R 32..43 tail would cut it)")
    o("release of the pawl after the sear lets go, dynamic load:")
    Frd = rows["dynamic"][3]
    for mu, cond in ((0.05, "DU bush, lubricated"), (0.25, "DU bush, dry/worn"), (0.7, "corroded steel pin (failure)")):
        m_open = Frd * A_PAWL
        m_fric = mu * Nd * R_PAWL_PIN
        o(f"  mu {mu:4.2f} ({cond}): opening {m_open / 1000:.2f} N m vs friction {m_fric / 1000:.2f} N m -> "
          f"ratio {m_open / m_fric:.1f}")
    Nl, F1l = rows["least"][1], rows["least"][2]
    for mu in (0.12, 0.3, 0.45, 0.6):
        frs = F1l * (math.tan(math.radians(FLANK_DEG)) - mu) / (1 + mu * math.tan(math.radians(FLANK_DEG)))
        ok = frs * A_PAWL > 0.25 * Nl * R_PAWL_PIN
        o(f"  seized pawl roller, flank mu {mu:4.2f}, least load: outward {frs:6.1f} N -> "
          f"{'releases' if ok else 'DOES NOT release'}")

    o("\n== Hold path past the carrier (review M7, I5)")
    rp = 30.0
    for lab, T in (("spring only, -3 deg +5 %", t_hold_s), ("static", t_static), ("dynamic", t_dyn),
                   ("strength", t_ult)):
        ft_ = T * 1000 / rp
        lew = ft_ / (10.0 * math.pi * 1.0 * 0.125)
        o(f"  {lab:24s} {T:6.1f} N m: wheel tooth force {ft_:5.0f} N, Lewis (m1, b 10, y 0.125) {lew:4.0f} MPa "
          f"-> {'OK' if lew < 100 else 'FAILS'} (CuSn12 Rp0.2 ~140, fatigue ~60-90 MPa)")
    lead = math.degrees(math.atan(1.0 / 14.0))
    o(f"  worm lead {lead:.2f} deg: self-locking needs mu > {math.tan(math.radians(lead)):.3f}; worm axial thrust "
      f"= wheel tooth force (above) into P11's F695 seat (printed) -> needs a metal thrust seat")
    for mu in (0.06, 0.10):
        eta = math.tan(math.radians(lead)) / math.tan(math.radians(lead) + math.atan(mu))
        o(f"  gearmotor torque to drive {spring_torque(0, sp_tol):.1f} N m through 60:1 at mu {mu}: "
          f"{spring_torque(0, sp_tol) / 60 / eta:.2f} N m (efficiency {eta:.2f})")
    o("  -> the m1 / z60 bronze set cannot carry even the spring torque: BLOCKING (latch.md section 10)")
    # carrier joint and keys
    f_bolt = t_ult * 1000 / 25.0
    o(f"  carrier joint, 6 x M4 8.8 at R 25 into the wheel (16 mm thread) + 2 dowels: shear at strength "
      f"{f_bolt / 6:.0f} N per bolt (M4 8.8 shear ~3.4 kN); friction grip 6 x 4 kN x 0.15 x R25 = "
      f"{6 * 4000 * 0.15 * 25 / 1000:.0f} N m")
    for lab, T in (("dynamic", t_dyn), ("strength", t_ult)):
        p_key = T * 1000 / 17.5 / 2 / (5.0 * 11.0)
        o(f"  collar keys, 2 x A 10 x 8 x 11 in the 6082 shaft (5 mm in the shaft): {lab} bearing {p_key:.0f} MPa "
          f"(6082-T6 yield 260)")

    o("\n== Stage 2: roller sear as a toggle, sear stop, trip moment (review M1, M4, M5)")
    s0r = C0_SEAR_ROLLER / F2u
    s0p = C0_SEAR_PIVOT / F2u
    o(f"sear roller RSTO 5 (C0 {C0_SEAR_ROLLER / 1000:.1f} kN): s0 {C0_SEAR_ROLLER / F2d:.1f} dynamic, {s0r:.1f} "
      f"strength; pivot HK0609 (C0 {C0_SEAR_PIVOT / 1000:.1f} kN): s0 {C0_SEAR_PIVOT / F2d:.1f} / {s0p:.1f} "
      f"(old 625 + 2 x MR85: s0 ~0.5 at strength)")
    stop_r = (F2u * E2[2] + K_SEAR_SPRING) / STOP_ARM
    o(f"sear stop: engagement {E2[1]:.2f} +/- {E2[2] - E2[1]:.2f} mm; reaction at strength "
      f"({F2u:.0f} N x {E2[2]} + {K_SEAR_SPRING:.0f}) / {STOP_ARM:.0f} = {stop_r:.1f} N")
    F2l = rows["least"][4]
    close_min = F2l * E2[0] + K_SEAR_SPRING
    o(f"holding against shock: closing moment at the least load {close_min:.1f} N mm vs the sear's imbalance at "
      f"{a_imp / G0:.0f} g ({0.006 * a_imp * 0.5:.1f} N mm) -> margin {close_min / (0.006 * a_imp * 0.5):.0f}; "
      f"the closing direction is taken by the stop")
    cases = {"new": (0.0025, 0.5), "aged (design case)": (0.005, 1.5)}
    trips = {}
    for name, (mu_b, drag) in cases.items():
        m, (me, mr, mp) = trip_moment(F2d, E2[2], mu_b, drag)
        trips[name] = m
        o(f"  {name}: toggle {me:.0f} + roller {mr:.1f} (x (L2+R)/R) + pivot {mp:.1f} + spring "
          f"{K_SEAR_SPRING:.0f} = {m:.0f} N mm -> radial push on the tab roller {m / L_TAB:.2f} N")
    for mu_slide in (0.12, 0.6):
        m = F2d * E2[2] + F2d * mu_slide * (L2 + R_SEAR_ROLLER) + 5 + K_SEAR_SPRING
        o(f"  seized sear roller, sliding mu {mu_slide}: {m:.0f} N mm -> {m / L_TAB:.0f} N at the tab (failure)")
    travel_roll = E2[2] + TRIP_OVERTRAVEL
    radial = L_TAB * travel_roll / L2
    o(f"trip travel: roller {travel_roll:.2f} mm past dead centre -> tab roller {radial:.2f} mm radially")

    o("\n== Trip force at the solenoid over the latched range (review M4, I7, M3)")
    r_hot = SOL_R20 * (1 + SOL_TOL) * (1 + ALPHA_CU * (T_HOT - 20))
    r_cold_min = SOL_R20 * (1 - SOL_TOL)
    i_min = I_REG * (1 - I_REG_TOL)
    design = trips["aged (design case)"]
    worst = None
    o(f"regulated pulse {I_REG:.2f} A +/-{100 * I_REG_TOL:.0f} % (min {i_min:.2f} A); rest gap {S_REST} mm; hook gap "
      f"{HOOK_GAP[1]} +/- 0.2 mm; guide DU mu 0.2 aged, plunger PTFE mu 0.25 aged")
    o("| beta | contact | stroke used | gap at load pickup | needed (aged) | available at I_min | margin | mu 0.4/0.5 guide |")
    for beta in (-3.0, 0.0, 15.0, 30.0, 40.0, 48.0):
        phi = beta
        cosp = math.cos(math.radians(phi))
        need, _ = solenoid_force_needed(design, phi, 0.2, 0.25)
        need_bad, _ = solenoid_force_needed(design, phi, 0.4, 0.5)
        pick = S_REST - HOOK_GAP[0] / cosp            # smallest hook gap -> largest gap at pickup (weakest)
        used = (HOOK_GAP[2] + radial) / cosp
        avail = sol_force(pick, i_min)
        m = avail / need
        if worst is None or m < worst[0]:
            worst = (m, beta, need, avail, pick)
        o(f"| {beta:+.0f} | phi {phi:+.0f} | {used:.2f} mm (reserve {S_REST - used:.2f}) | {pick:.2f} mm | "
          f"{need:.2f} N | {avail:.1f} N | {m:.2f} | {avail / need_bad:.2f} |")
    o(f"worst margin {worst[0]:.2f} at beta {worst[1]:+.0f} (needed {worst[2]:.2f} N, gap {worst[4]:.2f} mm)")
    i_2x = None
    i = 1.0
    while i < 2.5:
        if all(sol_force(S_REST - HOOK_GAP[0] / math.cos(math.radians(b)), i)
               >= 2.0 * solenoid_force_needed(design, b, 0.2, 0.25)[0] for b in range(-3, 49)):
            i_2x = i
            break
        i = round(i + 0.01, 2)
    o(f"current for a 2.0x margin at every beta: {i_2x:.2f} A -> regulate to {I_REG:.2f} A +/-{100 * I_REG_TOL:.0f} %")
    o(f"at rest gap {S_REST} the coil pulls {sol_force(S_REST, i_min):.1f} N at I_min (return spring {RETURN_SPRING} N)")

    o("\n== Coil, pulse and reservoir (review M8)")
    v_hot = I_REG * (1 + I_REG_TOL) * (r_hot + R_LOOP)
    o(f"coil {SOL_R20} ohm +/-5 % at 20 C: {r_cold_min:.2f}..{SOL_R20 * (1 + SOL_TOL):.2f}; at {T_HOT:.0f} C worst "
      f"{r_hot:.2f} ohm; loop {R_LOOP} ohm")
    o(f"to hold {I_REG * (1 + I_REG_TOL):.2f} A into the hot coil + loop the driver must deliver {v_hot:.1f} V "
      f"at the end of the pulse")
    e_hot = (I_REG * (1 + I_REG_TOL)) ** 2 * (r_hot + R_LOOP) * PULSE_S
    e_cold = (I_REG * (1 + I_REG_TOL)) ** 2 * (r_cold_min + R_LOOP) * PULSE_S
    e_store = e_hot / BUCK_EFF
    o(f"energy per {1000 * PULSE_S:.0f} ms pulse into coil + loop: {e_hot:.2f} J hot, {e_cold:.2f} J cold; from the "
      f"store at {100 * BUCK_EFF:.0f} % efficiency {e_store:.2f} J; {PULSES} pulses {PULSES * e_store:.1f} J")
    v0, vmin = 27.0, v_hot + 1.5
    c = 2 * PULSES * e_store / (v0**2 - vmin**2)
    o(f"store: from {v0:.0f} V down to {vmin:.1f} V (driver headroom 1.5 V): C >= {1000 * c:.0f} mF; with -20 % "
      f"capacitance at end of life: >= {1000 * c / 0.8:.0f} mF")
    vdirect = 13.5
    o(f"unregulated straight onto the coil from {vdirect} V: hot-coil current {vdirect / (r_hot + R_LOOP):.2f} A "
      f"< {i_2x:.2f} A needed -> not acceptable")
    o(f"peak current: {I_REG * (1 + I_REG_TOL):.2f} A regulated (a short-circuit limit at ~3 A)")

    o("\n== Reduced-current margin test (review M11)")
    for lab, T in (("spring only at beta 0 (+5 %), calm", spring_torque(0, sp_tol)), ("6 m/s", spring_torque(0, sp_tol) + aero_moment(6))):
        F2t = stage1(T)[3]
        mt, _ = trip_moment(F2t, E2[2], 0.005, 1.5)
        need = solenoid_force_needed(mt, 0.0, 0.2, 0.25)[0]
        pick = S_REST - HOOK_GAP[0]
        f_rated = sol_force(pick, 1.94)
        i_t = 1.94 * math.sqrt(1.5 * need / f_rated)
        o(f"  {lab}: T {T:.1f} N m, F2 {F2t:.0f} N, needs {need:.2f} N -> test pulse {i_t:.2f} A gives 1.5x; a pass "
          f"proves {I_REG * (1 - I_REG_TOL) / i_t * 1.0:.2f}x current headroom ({(I_REG * (1 - I_REG_TOL) / i_t) ** 2:.1f}x force)")


if __name__ == "__main__":
    main()
