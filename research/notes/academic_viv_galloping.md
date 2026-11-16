# Academic & engineering literature on small VIV and galloping wind energy harvesters (for a domestic bladeless build)

Method note: Every WebFetch attempt failed with ENOTFOUND (www.mdpi.com, arxiv.org and www.ncbi.nlm.nih.gov all failed), so all findings below come from WebSearch result snippets, abstracts and summaries, not from reading full papers. Numbers marked "secondary" came from a citing paper or a news write-up. Check them against the DOI before quoting them as definitive. Dates are as of November 2026.

---

## 1. Physics: VIV vs galloping, and which suits low, variable domestic winds. Theoretical maximum capture vs Betz

### Takeaway
VIV is a resonance (lock-in) phenomenon. It gives useful amplitude (about one diameter) only in a narrow band of wind speeds around the speed where the vortex-shedding frequency matches the mast's natural frequency. Galloping (on square, D-shaped or triangular sections, which meet the Den Hartog instability criterion) has no upper lock-in limit and gives large amplitudes that grow with wind speed, but it needs a higher cut-in speed and must be protected from runaway amplitude. Theory and water-tunnel experiments put the best-case conversion efficiency of an oscillating cylinder at about 17–23% (up to about 28–37% for VIVACE with turbulence-control strips at high Reynolds number in water). That compares with the Betz limit of 59.3% for rotors. Peer-reviewed modelling of Vortex-style masts in air gives a peak efficiency of only about 6%.

### Cited Findings
**VIV fundamentals**
- Williamson & Govardhan (2004, *Annual Review of Fluid Mechanics*) is the standard review of VIV. It focuses on very low mass and damping, with lock-in, wake modes and synchronisation as its key themes — [IISc ePrints listing](https://eprints.iisc.ac.in/17385/); [SciSpace PDF](https://scispace.com/pdf/vortex-induced-vibrations-5ae1ijrmof.pdf)
- The "Griffin plot" (peak amplitude vs mass-damping) shows large scatter over 30 years of data. Govardhan & Williamson (2006, *JFM*) showed that the data collapse once Reynolds number is included (the "modified Griffin plot"). At very low mass and damping, the response frequency rises above the structural natural frequency rather than matching it — [Cambridge JFM, modified Griffin plot](https://www.cambridge.org/core/journals/journal-of-fluid-mechanics/article/defining-the-modified-griffin-plot-in-vortexinduced-vibration-revealing-the-effect-of-reynolds-number-using-controlled-damping/C433970B58BB5B1C0358253E74825D65); [Williamson IUTAM abstract](https://eng-web77-v02.ocio.monash.edu/intranet/proceedings/iutam2007/pages/pdf/S1_Inv_Williamson_abs.pdf)
- Lock-in is defined (Williamson 1999, via Navrose & Mittal 2016, *JFM*) as the wake vortex frequency matching the body's oscillation frequency. Even when the aeroelastic system is unstable at all reduced velocities, lock-in occurs only within a limited range of U* — [Navrose & Mittal 2016, "Lock-in in vortex-induced vibration", JFM](https://www-cambridge-org.ezproxyberklee.flo.org/core/services/aop-cambridge-core/content/view/295E778EA8FBDDCBEDB1EE03E159E726/S0022112016001579a.pdf/lock-in-in-vortex-induced-vibration.pdf)
- Vortex Bladeless's own description says the shedding frequency depends on wind speed, and the mast oscillates and harvests energy when its natural frequency is similar. Its magnets "also act as 'Tuning System', modifying the apparent elasticity constant of the mast, thus widening the wind speed range in which oscillations happen" — [vortexbladeless.com/technology (via search snippet)](https://vortexbladeless.com/technology/)
- A summary says Vortex lab masts vary in diameter along the height (up to 95 mm at the base in lab models), so that shedding frequency stays synchronised along the mast. This is a secondary, AI-generated source — [Grokipedia (treat cautiously)](https://grokipedia.com/page/Vortex_Bladeless)

**Galloping fundamentals**
- Barrero-Gil, Alonso & Sanz-Andrés (2010), "Energy harvesting from transverse galloping", *J. Sound & Vibration* 329(14):2873–2883. It models transverse galloping as a 1-DOF system with quasi-steady aerodynamic forces and studies how cross-section geometry and mechanical properties affect the energy conversion factor. It credits Den Hartog with first deriving the galloping onset condition under the quasi-steady assumption. An open-access copy is at UPM — [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0022460X10000891); [UPM open-access PDF](https://oa.upm.es/7294/2/INVE_MEM_2010_78822.pdf)
- Meseguer, Sanz-Andrés & Alonso, "Determination of maximum mechanical energy efficiency in energy galloping systems", *J. Engineering Mechanics* 141(1) — [ASCE Library](https://ascelibrary.org/doi/abs/10.1061/(ASCE)EM.1943-7889.0000817)
- Zhao & Yang (2017) review: galloping has advantages over VIV, including large oscillation amplitude and operation over a wide range of wind speeds — [Wiley, Shock & Vibration, DOI 10.1155/2017/3585972](https://onlinelibrary.wiley.com/doi/10.1155/2017/3585972); [UTS open-access PDF](https://opus.lib.uts.edu.au/bitstream/10453/124929/1/Toward%20small%20scale%20wind%20energy%20harvesting.pdf)
- A 2026 Applied Energy review says VIV harvesters rely on lock-in, while galloping harvesters need a high cut-in speed — [ScienceDirect, "A review of energy harvesting techniques based on flow-induced vibrations" (Applied Energy, 2026)](https://www.sciencedirect.com/science/article/abs/pii/S0306261926005891)
- Other sources say VIV-based piezo harvesters can stabilise output voltage at low wind speeds, while galloping-based ones operate at higher wind speeds with wide bandwidth. They also note that galloping occurs over a much wider wind-speed range than VIV — [search summary of related small-scale literature, NTU "energy from wind" PDF](https://www3.ntu.edu.sg/CorpComms2/Research%20Papers/energy_from_wind.pdf); [UTS: galloping with piezo & EM transduction](https://opus.lib.uts.edu.au/bitstream/10453/138328/1/Effects%20of%20Electrical%20and%20Electromechanical%20Parameters%20on%20Performance%20of%20Galloping-based%20Wind%20Energy%20Harvester%20with%20Piezoelectric%20and%20Electromagnetic%20Transductions.pdf)
- For a bio-inspired cactus-section bladeless mast (Biomimetics 2025), a plain cylindrical mast showed better VIV performance below 5 m/s — [Biomimetics 2025, DOI 10.3390/biomimetics10100692](https://doi.org/10.3390/biomimetics10100692)
- A Mexican study compared circular and triangular sections and found the triangular section formed vortices more easily — [CIO congress abstract](https://congresos.cio.mx/19_enc_mujer/cd_congreso/archivos/resumenes/S1/S1-ING10.pdf)
- Studies disagree on the best galloping shape. One reports a square section giving the highest output among square, rectangular, triangular and D-shapes. Another found the D-shape best at relatively high wind speeds. A third found a square prism beat a circular cylinder at high wind speeds — [search summary across galloping-shape studies, e.g. ResearchGate "Small wind energy harvesting from galloping using piezoelectric materials"](https://www.researchgate.net/publication/260791681_Small_Wind_Energy_Harvesting_From_Galloping_Using_Piezoelectric_Materials)

**Maximum energy capture (efficiency) for an oscillating cylinder**
- Barrero-Gil, Pindado & Avila (2012), "Extracting energy from vortex-induced vibrations: a parametric study", is the source of the efficiency framework most later papers use. A summary says the largest oscillations occur at very low damping, but the best harvesting efficiency comes at a moderate damping ratio of about 0.025–0.05 — [ResearchGate](https://www.researchgate.net/publication/251574443_Extracting_energy_from_Vortex-Induced_Vibrations_A_parametric_study)
- For an elastically mounted rigid cylinder (wake-oscillator model), the optimum is η = 0.23 at damping parameter ξ = 0.16 and frequency ratio δ = 0.90, obtained under lock-in. This is close to the 0.22 reported by Bernitsas et al. For periodic harvesters along a tensioned cable, η = 0.19 — [arXiv 1407.5432, "On the efficiency of energy harvesting using VIV of cables" (J. Fluids & Structures 2014)](https://arxiv.org/html/1407.5432); [ScienceDirect JFS](https://www.sciencedirect.com/science/article/abs/pii/S0889974614001005)
- A 2023 *Ocean Engineering* study, "Optimal energy harvesting efficiency from VIV of a circular cylinder", reports a maximum of about 18% when oscillation and shedding frequencies synchronise. A reduced-order study finds about 0.17 — [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0029801823012532); [arXiv 2302.09975](https://arxiv.org/pdf/2302.09975)
- Lee & Bernitsas high-damping, high-Re tests harnessed a maximum of about 33% of flow energy at Re ≈ 75,000 in water (as cited in the confined-cylinder paper) — [arXiv 2101.11803](https://arxiv.org/pdf/2101.11803)
- Betz limit for rotors = 16/27 ≈ 0.593. Utility turbines reach about 75–80% of Betz at peak — [Wikipedia, Betz's law (via search)](https://en.wikipedia.org/wiki/Betz%27s_law)
- Breen, Mallik & Adhikari (2025, *Renewable Energy* 254:123549) modelled a Vortex-style mast with a wake oscillator. Peak efficiency was **6%**, and maximum power was 600 W, but with a trade-off against structural safety. The most efficient geometries were not the most powerful — [Glasgow Enlighten eprint](https://eprints.gla.ac.uk/357207); [Glasgow news, June 2025](https://www.gla.ac.uk/news/archiveofnews/2025/june/headline_1187739_en.html); [Ecoticias](https://www.ecoticias.com/en/a-bladeless-wind-turbine-that-sways-in-the-wind-could-safely-produce-460-watts-in-computer-simulations-and-the-most-efficient-design-turned-out-not-to-be-the-most-powerful/53690/)
- An AI encyclopedia entry claims independent analyses put VIV-system power coefficients at about 0.15–0.2 vs 0.4–0.5 for bladed designs. This is unverified and Grokipedia is AI-generated — [Grokipedia](https://grokipedia.com/page/Vortex_Bladeless)
- A 2026 Applied Energy review says piezoelectric FIV harvester efficiency is below 1%, while electromagnetic systems have a higher ceiling — [ScienceDirect Applied Energy 2026 review](https://www.sciencedirect.com/science/article/abs/pii/S0306261926005891)

### Inferences
- **Standard textbook background (not verified from a fetched source in this session):** Strouhal number St ≈ 0.2 for a circular cylinder in the subcritical Reynolds range, so f_shed ≈ 0.2·U/D. Lock-in for low mass-damping bodies in air is typically centred near reduced velocity U* = U/(f_n·D) ≈ 5, with a band of roughly U* ≈ 4–8. The Scruton (mass-damping) number Sc ∝ m·ζ/(ρD²) controls peak VIV amplitude, which saturates at about 1 D for low Sc. Den Hartog criterion: a section gallops if dC_L/dα + C_D < 0. An axisymmetric circular cylinder cannot gallop. Galloping onset speed scales roughly linearly with Sc, and amplitude keeps growing with U above onset (no upper limit). Classic texts are Blevins, *Flow-Induced Vibration*, and Païdoussis, Price & de Langre (2011), *Fluid-Structure Interactions: Cross-Flow-Induced Instabilities* (Cambridge University Press).
- **Sizing example (calculation from St ≈ 0.2):** a 20 cm diameter mast at 4 m/s sheds at about 4 Hz. A 5 cm tube at 4 m/s sheds at about 16 Hz. A mast tuned to lock in at 4 m/s will drop out of lock-in by roughly 2.5 m/s and 6–7 m/s unless its stiffness is tuned. This is why Vortex adds a magnetic "tuning" spring.
- **Realistic power for a domestic mast (calculation):** take a 1 m tall × 0.2 m diameter mast, so 0.2 m² projected area. Wind power through that area is 0.5·1.225·0.2·U³: about 7.8 W at 4 m/s and about 15.3 W at 5 m/s. At 6% efficiency (the Glasgow peak) that gives about 0.5–0.9 W. At an optimistic 20% (the theoretical VIV optimum) it gives about 1.6–3 W. A small 1 m diameter rotor (0.785 m²) at 5 m/s with Cp 0.3 gives about 18 W. Per unit of frontal area, a VIV mast is roughly an order of magnitude worse than a small rotor in practice.
- **Physics conclusion for variable domestic winds:** pure VIV has a narrow useful band, so it needs stiffness tuning (magnets, MRE). Galloping is better suited to wide wind ranges, but its cut-in speed is higher and it needs amplitude limiting. The literature often proposes hybrid VIV–galloping designs (a cylinder plus splitter plate or attachments) as the compromise.

### Gaps
- Full text of Barrero-Gil et al. 2012 was not retrieved. The venue is believed to be *Applied Mathematical Modelling*, but this was not verified.
- No numeric maximum galloping efficiency was retrieved from the Meseguer et al. or Barrero-Gil 2010 abstracts.
- No source was found that defines a "swept-area" Cp for oscillating masts in a way directly comparable to Betz. Efficiency definitions vary: frontal area × U³, versus area including oscillation amplitude.

---

## 2. Key review articles and highly cited papers (citations, DOIs, key findings)

### Takeaway
The core reading list is Abdelkefi (2016, IJES), Zhao & Yang (2017, Shock & Vibration), the Applied Energy FIV reviews (2020 and 2026), Williamson & Govardhan (2004) on VIV physics, Barrero-Gil's UPM papers on VIV and galloping efficiency, and Bernitsas's VIVACE papers (water, but the efficiency and turbulence-control lessons transfer). For bladeless masts specifically: Breen et al. 2025 (*Renewable Energy*), the *Scientific Reports* 2025 composite-mast paper, and the Korean resonance-shifting-module papers (*Applied Sciences* 2024/2026).

### Cited Findings
| Ref | Venue / year / DOI | Key content |
|---|---|---|
| Abdelkefi, "Aeroelastic energy harvesting: A review" | *Int. J. Engineering Science* 100:112–135 (2016), DOI 10.1016/j.ijengsci.2015.10.006 | Reviews VIV, galloping, flutter and wake galloping harvesters, with representative models and qualitative and quantitative comparisons. Piezo transduction got the most interest because of its frequency range and ease of application — [UTB catalogue](https://vufind.katalog.k.utb.cz/SummonRecord/FETCH-LOGICAL-c378t-6c669f491f0de937df18d45558c8bb9354ad288e2b95a0c2917841e1b9fbc50b3); [Peeref](https://peeref.com/works/2407268) |
| Zhao & Yang, "Toward small-scale wind energy harvesting: design, enhancement, performance comparison, and applicability" | *Shock & Vibration* 2017, DOI 10.1155/2017/3585972 (open access) | Compares cm-scale turbines, windmills and aeroelastic harvesters (VIV, galloping, flutter, wake-induced, turbulence-induced) by dimensions, cut-in and cut-out speeds — [Wiley](https://onlinelibrary.wiley.com/doi/10.1155/2017/3585972); [UTS PDF](https://opus.lib.uts.edu.au/bitstream/10453/124929/1/Toward%20small%20scale%20wind%20energy%20harvesting.pdf) |
| "The state-of-the-art review on energy harvesting from flow-induced vibrations" | *Applied Energy* (2020), ScienceDirect S0306261920304141 | Principles of VIV, galloping, flutter and buffeting, wind and hydro devices, and challenges. A secondary source says it includes Vortex Bladeless among the FIV concepts — [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0306261920304141) |
| "A review of energy harvesting techniques based on flow-induced vibrations" | *Applied Energy* 2026, S0306261926005891 | Compares VIV, flutter, galloping and WIV across piezo, EM, triboelectric, electrostatic and hybrid conversion. VIV relies on lock-in, galloping needs high cut-in. Piezo efficiency <1%, EM has a higher ceiling — [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0306261926005891) |
| "Fluid flow-based vibration energy harvesters: a critical review of state-of-the-art technologies" | *Applied Sciences* 14(23):11452 (2024) | Open-access critical review — [MDPI](https://www.mdpi.com/2076-3417/14/23/11452) |
| Li et al., "Recent progress on flutter-based wind energy harvesting" | *Int. J. Mech. Syst. Dyn.* 2022, DOI 10.1002/msd2.12035 | Flutter-focused review (Windbelt-type devices, brief relevance only) — [Wiley](https://onlinelibrary.wiley.com/doi/full/10.1002/msd2.12035) |
| Williamson & Govardhan, "Vortex-induced vibrations" | *Annu. Rev. Fluid Mech.* 2004 | Canonical VIV physics: low mass-damping, lock-in, wake modes — [IISc](https://eprints.iisc.ac.in/17385/) |
| Barrero-Gil, Alonso & Sanz-Andrés, "Energy harvesting from transverse galloping" | *JSV* 329(14):2873–2883 (2010) | 1-DOF quasi-steady galloping harvester; effect of geometry on the conversion factor — [UPM OA PDF](https://oa.upm.es/7294/2/INVE_MEM_2010_78822.pdf) |
| Barrero-Gil, Pindado & Avila, "Extracting energy from VIV: a parametric study" | 2012 | Efficiency framework; optimum at moderate damping — [ResearchGate](https://www.researchgate.net/publication/251574443_Extracting_energy_from_Vortex-Induced_Vibrations_A_parametric_study) |
| Vicente-Ludlam, Barrero-Gil & Velázquez (2014) | *J. Fluids & Structures* | Optimal electromagnetic energy extraction from transverse galloping (cited in Hémon et al. 2017) — [Hémon 2017 JFS PDF](https://yakari.polytechnique.fr/Django-pub/documents/hemon2017rp-1pp.pdf) |
| Barrero-Gil group, "Enhance of energy harvesting from transverse galloping by actively rotating the galloping body" | *Energies* 13(1):91 (2020) | Active rotation to boost galloping harvesting — [DOI 10.3390/en13010091](https://doi.org/10.3390/en13010091) |
| VIV of cables efficiency | *JFS* 2014 / arXiv 1407.5432 | η_opt = 0.23 for a rigid cylinder; 0.19 for periodic harvesting on a cable — [arXiv](https://arxiv.org/html/1407.5432) |
| Bernitsas et al., VIVACE | DOE final report DE-FG36-05GO15162; *Renewable Energy* (PTC single cylinder) | Peak efficiency 30.73%, RMS 21.73% (DOE report). With PTC: 37% simulated, 28% experimental. Optimal damping ratio 0.12 — [OSTI](https://www.osti.gov/servlets/purl/896401); [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0960148115301841); [Tethys](https://tethys-engineering.pnnl.gov/publications/numerical-simulation-experimental-validation-energy-harvesting-single-cylinder-vivace) |
| "Bistable vibration energy harvesters: A review" | 2013 | Background on bistable nonlinearity — [ResearchGate](https://www.researchgate.net/publication/258152161_Bistable_vibration_energy_harvesters_A_review) |
| "A state-of-the-art review on VIV phenomenon bladeless wind turbine technology" | 2024 (ResearchGate) | Bladeless-specific review. Cites roughly 30% lower efficiency than conventional turbines — [ResearchGate](https://www.researchgate.net/publication/386170209_A_State-of-the-Art_Review_on_Vortex_Induced_Vibrations_Phenomenon_Bladeless_Wind_Turbine_Technology) |
| Breen, Mallik & Adhikari, "Performance analysis and geometric optimization of bladeless wind turbines using wake oscillator model" | *Renewable Energy* 254:123549 (2025), DOI 10.1016/j.renene.2025.123549 (CC-BY) | 6% peak efficiency; 600 W max; 460 W structurally safe at 0.8 m × 0.65 m — [Glasgow Enlighten](https://eprints.gla.ac.uk/357207); [author PDF](https://userweb.eng.gla.ac.uk/sondipon.adhikari/fulltext/journal/ft474.pdf) |

- Citation conflict: one secondary source lists the Breen et al. paper as *Renewable Energy* vol. 215 — [securities.io](https://www.securities.io/bladeless-wind-turbines-clean-energy-future/). The Glasgow repository and news give vol. 254 (2025), article 123549 — [Glasgow Enlighten](https://eprints.gla.ac.uk/357207). Prefer vol. 254.

### Inferences
- For a builder, the most useful open-access entry points are the UPM PDF of Barrero-Gil 2010 (galloping), the UTS PDF of Zhao & Yang 2017 (comparison tables of cut-in speeds and power), the Glasgow author PDF of Breen et al. 2025 (mast geometry vs power vs safety), and arXiv 1407.5432 (VIV efficiency optimum).

### Gaps
- Author lists for the 2020 and 2026 Applied Energy reviews and the VIVACE PTC paper were not confirmed in snippets. They are believed to include J. Wang et al. (2020) and L. Ding/M. Bernitsas (PTC), but this was not verified.
- Païdoussis's textbook and Blevins's *Flow-Induced Vibration* were not checked in this session.

---

## 3. Measured outputs of small prototypes (mW piezo galloping vs W-scale EM VIV masts)

### Takeaway
Nearly all peer-reviewed lab prototypes with cm-scale bluff bodies deliver **microwatts to tens of milliwatts**. The best galloping-piezo results are about 50 mW at about 5–6 m/s. Typical EM galloping and VIV lab rigs give 0.1–1 mW. I found **no peer-reviewed, independently measured watt-level VIV/galloping wind harvester**. Watt-scale and higher figures come from simulations (Glasgow 460–600 W; *Sci. Rep.* about 119 W at 8 m/s) or from company ratings (Vortex Tacoma about 100 W).

### Cited Findings
| Device / study | Size / body | Transduction | Wind speed | Power | Source |
|---|---|---|---|---|---|
| Sirohi & Mahadik D-section galloping beam | D-shaped bluff body on cantilever | Piezo | 4.92 m/s (another citation: 11.6 mph ≈ 5.2 m/s) | 53 mW | [ResearchGate: "Harvesting wind energy using a galloping piezoelectric beam"](https://www.researchgate.net/publication/267649430_Harvesting_Wind_Energy_Using_a_Galloping_Piezoelectric_Beam) (secondary summary) |
| Cut-corner square prism | Modified square prism | Piezo galloping | 6.24 m/s | 47.5 mW (+261% vs plain square) | [ResearchGate: "Enhanced performance of wind energy harvester by aerodynamic treatment of a square prism"](https://www.researchgate.net/publication/299343082_Enhanced_performance_of_wind_energy_harvester_by_aerodynamic_treatment_of_a_square_prism) |
| Square bluff body GPEH (with/without impact bump stop) | Square prism | Piezo galloping | 8 m/s | 13 mW max | [ResearchGate](https://www.researchgate.net/publication/265604493_Experimental_investigation_of_galloping_piezoelectric_energy_harvesters_with_square_bluff_bodies); [ADS 2014SMaS...23j4012E](https://ui.adsabs.harvard.edu/abs/2014SMaS...23j4012E/abstract) |
| Square-section tip | Square prism | Piezo galloping | 8 m/s | 8.4 mW | search summary of galloping literature (e.g. [ResearchGate galloping piezo](https://www.researchgate.net/publication/260791681_Small_Wind_Energy_Harvesting_From_Galloping_Using_Piezoelectric_Materials)) |
| D-shape (review table) | D-section | Piezo galloping | cut-in 2.5 m/s, peak at 4.7 m/s | 1.14 mW | search summary (review table) |
| Square prism with elliptical rear protrusion | Square + arcuate features | Piezo galloping | 5.1 m/s | 0.757 mW (+157% vs plain square) | [Sensors 25(6):1657 (2025), DOI 10.3390/s25061657](https://doi.org/10.3390/s25061657) |
| Spring-coupling EM galloping harvester (SEGEH) | Bluff body + coupling spring | Electromagnetic | 14 m/s | 0.79 mW, 103.2 mV (+93% vs no spring) | [Micromachines 14(5):968 (2023), DOI 10.3390/mi14050968](https://doi.org/10.3390/mi14050968) |
| Multi-coil EM galloping (same group) | Off-centre coil sets | Electromagnetic | 9 m/s | 0.40 / 0.62 / 0.72 mW (1, 2, multi coils) | [OUCI: coil arrangement study](https://ouci.dntb.gov.ua/works/40y8R23l) |
| EM VIV "Kármán vortex street" harvester | Cylinder | Electromagnetic | 1.192 m/s flow | ~0.1 mW non-rectified | [ScienceDirect, Mechatronics 2012](https://www.sciencedirect.com/science/article/abs/pii/S0957415812000463) |
| Multi-directional, multi-modal VIV harvester | Beam + bluff body | (not confirmed in snippet) | 2.8 m/s | 0.386 mW average | [Applied Physics Letters 125(20):203901 (2024)](https://pubs.aip.org/aip/apl/article/125/20/203901/3319556/Multi-directional-and-multi-modal-vortex-induced) |
| VIV-TENG (low-speed) | Cylinder (single and tandem) | Triboelectric | 2.78 m/s | 392.72 µW avg; 96.79 mW/m² | [AMiner: Nano Energy 2022](https://www.aminer.org/pub/625223b461bd09704f0c0ffc/vortex-induced-vibration-triboelectric-nanogenerator-for-low-speed-wind-energy-harvesting) |
| Vibration-coupled TENG | — | Triboelectric | starts at 1 m/s | (not given) | [Peeref, Nano Energy 2024](https://www.peeref.com/works/28806179) |
| Piezo MEMS VIV in formation | Silicon chip | Piezo | — | nanowatts | [Sci. Rep. 2019 (PMC6938501)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6938501/) |
| VIV harvester (ANSYS model) | — | — | 2 m/s | 2.2 mW (model) | [ResearchGate](https://www.researchgate.net/publication/278392990_Development_and_Analysis_of_Vortex-Induced_Vibrations_Energy_Harvester) |
| 3D-printed bladeless mast | Small mast | — | 3 m/s | 0.43 mW; amplitude ratio 0.155 | [Abyssinia J. Eng. & Computing 2024](https://ajol.info/index.php/ajec/article/view/286124) |
| Bladeless generator (wind tunnel) | — | not confirmed | — | 5.25 mW max | [IJRED (Undip)](https://ejournal.undip.ac.id/index.php/ijred/article/download/43888/pdf) |
| Magnetostrictive wind-induced vibration harvester | — | Magnetostrictive | outdoor 0–3.2 m/s | micro-scale (for WSN) | [e-Prime 2024 (DOAJ)](https://doaj.org/article/c6a04c73b46b4c87bf69ee63bf65d66b) |
| EM magnet-in-coil VIV cylinder (numerical) | Cylinder (tandem) | EM | — | microwatts; up to 15% efficiency in best case | [arXiv 1712.01588 (Soti et al., JFS 2017)](https://ar5iv.labs.arxiv.org/html/1712.01588); [Monash PDF](https://flair.monash.edu/publications/pdfs/SoThShBh_jfs_2017.pdf) |
| "VIV wind harvester", hollow PVC cylinder 50 cm × 12 cm | Cylinder | unclear | 5.5 m/s | claimed 4.02 W, 12.5 V | [Academia.edu (unverified)](https://www.academia.edu/117882425/Performance_Analysis_of_Vortex_Induced_Vibration_Based_Wind_Energy_Harvesting_System) |
| VIVACE (water) | Cylinders with PTC | EM (rotary via belt) | 1.03 m/s water | 98.2 W/m³; up to 885.53 W/m³ for a staggered array | [Academia.edu: high-damping high-Re VIVACE](https://www.academia.edu/24268680/High_damping_high_Reynolds_VIV_tests_for_energy_harnessing_using_the_VIVACE_converter); [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0960148115301841) |
| Vortex Bladeless Tacoma | ~2.75 m class mast (company) | EM linear alternator | — | rated ~100 W (company/secondary) | [Ecoportal](https://www.ecoportal.net/en/wind-turbine-vortex-bladeless/1066/); Glasgow news: "best-performing real-world prototypes… maximum of 100W" — [TechXplore](https://techxplore.com/news/2025-06-optimal-potential-bladeless-turbines.html) |
| Glasgow modelled optimum | 0.8 m tall × 0.65 m dia | (model) | not stated in snippets | 460 W safe; 600 W max (simulation) | [Glasgow news](https://www.gla.ac.uk/news/headline_1187739_en.html) |
| Sci. Rep. composite bladeless mast | composite hollow mast | (model) | 8 m/s | Pm(RMS) = 119.26 W (text garbled, verify) | [Nature Sci. Rep. 15:1355 (2025)](https://www.nature.com/articles/s41598-024-82385-9.pdf) |
| Taguchi optimisation of Vortex 3D model | Vortex-sized | (model) | — | 1.25 kW → 3.44 kW (conference, low reliability) | [IEOM 2024 Dubai](https://ieomsociety.org/proceedings/2024dubai/507.pdf) |
| Tandem water piezo VIV | 2 cylinders | Piezo | water | 533 µW downstream at L/D = 1.7 (29× single) | search summary of tandem literature ([Frontiers Energy Res. 2023](https://www.frontiersin.org/journals/energy-research/articles/10.3389/fenrg.2023.1231966/pdf)) |

- No peer-reviewed electromagnetic VIV wind harvester with watt-level output confirmed in a field test was found. Lab results are typically sub-mW to low mW — [search across WPI, ResearchGate, ScienceDirect results, e.g. WPI MQP](https://digital.wpi.edu/downloads/00000130x?locale=en)
- Company and older claims: ASME reported the company saying the device harvests about 30% of the energy in a gust — [ASME "Harnessing the Vortex"](https://www.asme.org/topics-resources/content/harnessing-the-vortex). A Honduras resource study cites about 30% "field efficiency" for the Tacoma — [ResearchGate, Puerto Cortés](https://www.researchgate.net/publication/353011747_Wind_Resource_Assessment_Analysis_of_the_Vortex_Bladeless_Characteristics_in_Puerto_Cortes_Honduras). These conflict with the peer-reviewed 6% model peak (Breen et al. 2025) and the 17–23% theoretical VIV optimum.

### Inferences
- **The 4.02 W PVC claim is physically implausible.** Wind power through 0.5 m × 0.12 m = 0.06 m² at 5.5 m/s is 0.5·1.225·0.06·5.5³ ≈ 6.1 W. Getting 4.02 W would mean about 66% efficiency, which is above Betz and about three times the theoretical VIV optimum. Treat it as a measurement or reporting error.
- **Similar check on the Glasgow 460 W design (0.8 × 0.65 = 0.52 m²).** At 6% efficiency it would need P_wind ≈ 7.7 kW, i.e. U ≈ 29 m/s. So either the 460 W is at very high wind speed, or the efficiency definition differs. A builder should not read "460 W" as a domestic-wind figure.
- Power density of piezo galloping devices: about 50 mW from a few-cm bluff body at 5 m/s is consistent with a few % efficiency on a very small frontal area. Scaling to watts needs about 0.1–1 m² of frontal area and EM transduction, not piezo patches.
- Practical domestic expectation for a 1–2 m DIY mast: sub-watt to a few watts average in typical 3–5 m/s urban winds (see the Section 1 calculation). That is useful for sensors and battery trickle charging, not household load.

### Gaps
- No independently measured power curve (power vs wind speed) for the Vortex Tacoma/Nano/Atlantis was found in peer-reviewed literature.
- The wind speed for the Glasgow 460 W and 600 W figures was not in the snippets.
- Transduction for several entries (the APL 2024 multi-modal harvester, the IJRED 5.25 mW device) could not be confirmed.
- A study reporting about 4% Cp (about 8.5 mW peak) for an unnamed "test model" appeared in search results but could not be attributed.

---

## 4. Techniques to widen bandwidth and lock-in

### Takeaway
The well-evidenced levers are: (a) **stiffness tuning**, either passive magnetic springs (as Vortex uses) or active and semi-active stiffness via magnetorheological elastomers or "smart rubber". These shift resonance by 64–89% and roughly double the lock-in wind range (e.g. 1.7 to 3.2 m/s). (b) **Shape and attachments** (splitter plates, cut corners, protrusions, V-shaped "swallowtail" fins) that convert VIV into galloping, or lower the galloping cut-in by about 30%. (c) **Magnetic or mechanical nonlinearity** (bistable, tristable, stoppers, coupling springs). (d) **Tandem or wake interference**, which can multiply output when spacing is right. (e) **Passive turbulence control** (roughness strips) from VIVACE.

### Cited Findings
**Stiffness tuning (most relevant to a Vortex-style mast)**
- Vortex Bladeless: magnets act as a tuning system that modifies the mast's apparent spring constant and widens the operating wind range — [vortexbladeless.com/technology (search snippet)](https://vortexbladeless.com/technology/)
- Kang, Kook, Lee & Kim (2024), "A novel small-scale bladeless wind turbine using VIV and a discrete resonance-shifting module", *Applied Sciences* 14(18):8217. It uses an on-off variable-stiffness smart-material module — [DOI 10.3390/app14188217](https://doi.org/10.3390/app14188217)
- An ETASR paper on a magnetorheological-elastomer (MRE) bladeless turbine reports that a magnetic field shifted resonant frequency by **64.3%**, widening the operating range from about 2.0 to 3.3 m/s. It also found that mast diameter was key, and that redesigning the mast for uniform shedding frequency along its height improved performance — [ETASR PDF](https://etasr.com/index.php/ETASR/article/download/12314/5476/62799)
- *Applied Sciences* 2026, 16(1):553, "Design optimization of a small-scaled VIV bladeless wind turbine with binary resonance controller", reports an **88.9% resonance shift**, widening lock-in from **1.7 to 3.2 m/s** — [DOI 10.3390/app16010553](https://doi.org/10.3390/app16010553)
- IEEE: "Development of smart-rubber based resonance tuning module for bladeless wind turbine system" — [IEEE Xplore 10316880](https://ieeexplore.ieee.org/document/10316880/)
- *Sci. Rep.* 2025 (15:1355) tunes natural frequency by changing the stand's effective length or adding mass inside the hollow mast, reporting a **55.7% efficiency increase**. The design requirement is to meet lock-in over a specified wind range — [Nature Sci. Rep. DOI 10.1038/s41598-024-82385-9](https://www.nature.com/articles/s41598-024-82385-9)

**Shape and attachments**
- Two asymmetric splitter plates on a VIV piezo harvester (*Ocean Engineering* 2023; water): power up to **+471.2%** vs a plain VIV harvester (α = 60°, β = 90°). The plates shift the response from VIV to galloping and broaden bandwidth — [Southampton eprint, Wang 2023](https://eprints.soton.ac.uk/474694/1/Plate_splitter_Jwang2023.pdf); [AMiner](https://aminer.org/pub/63bbe69f90e50fcafd1acdcb/enhanced-performance-of-piezoelectric-energy-harvester-by-two-asymmetrical-splitter-plates)
- A rigid splitter plate on galloping prisms gave up to **+67%** power and a significant cut-in reduction — [AIP "Improving the performance of galloping micro-power generators by passively manipulating the trailing edge"](https://bvbvf1.bib-bvb.de/vufind/PrimoRecord/cdi_scitation_primary_10_1063_1_5016102)
- A wavy cylinder with a tuned mass damper gave +121% in one study — search summary ([UCL discovery PDF](https://discovery.ucl.ac.uk/10191570/1/043612_1_5.0200566.pdf))
- V-shaped (swallowtail) attachments gave a **32% cut-in reduction**. Downstream half-cylinder obstacles cut galloping cut-in from **2.23 to 1.55 m/s** — [NWPU: biomimetic swallowtail V-shaped attachments](https://pure.nwpu.edu.cn/en/publications/biomimetic-swallowtail-v-shaped-attachments-for-enhanced-low-spee)
- A cut-corner square prism gave +261% power (47.5 mW at 6.24 m/s) — [ResearchGate](https://www.researchgate.net/publication/299343082_Enhanced_performance_of_wind_energy_harvester_by_aerodynamic_treatment_of_a_square_prism)
- Bionic attachments on a VIV piezo harvester aim to increase amplitude and lower threshold wind speed — [ResearchGate](https://www.researchgate.net/publication/331839487_Design_Modeling_and_Experiments_of_the_Vortex-Induced_Vibration_Piezoelectric_Energy_Harvester_with_Bionic_Attachments)
- Caution: in a PolyU thesis, fins on a cylinder mitigated oscillation at higher angles of attack (30–45°), so fins can suppress as well as enhance — [PolyU thesis PDF](https://theses.lib.polyu.edu.hk/bitstream/200/13132/3/7584.pdf)
- A cactus-section (bio-inspired) mast showed a lower-turbulence wake and a higher power coefficient than a cylinder overall, but the cylinder was better below 5 m/s — [Biomimetics 2025](https://doi.org/10.3390/biomimetics10100692)
- A US patent covers a bladeless wind turbine with vortex generators. One study combining CFD and wind tunnel tests found the modified full-scale mast produced more power — [USPTO 12698752](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12698752)

**Passive turbulence control (VIVACE, Michigan)**
- Roughness strips (PTC) on a single cylinder: 37% simulated and 28% experimental conversion efficiency. A staggered 5D × 5D layout reached 885.53 W/m³ at 22.6% average efficiency. PTC also makes circular cylinders gallop at higher speeds — [Tethys](https://tethys-engineering.pnnl.gov/publications/numerical-simulation-experimental-validation-energy-harvesting-single-cylinder-vivace); [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0960148115301841); [arXiv 2411.16130, time-varying stiffness + PTC](https://arxiv.org/pdf/2411.16130)

**Nonlinearity (magnetic, bistable, stoppers, springs)**
- Monostable vs bistable VIV harvester modelling — [MSSP, ScienceDirect S088832702101089X](https://www.sciencedirect.com/science/article/abs/pii/S088832702101089X); tristable VIV harvester — [MSSP S088832702200992X](https://www.sciencedirect.com/science/article/abs/pii/S088832702200992X)
- Magnetic coupling (IM-GEH, *Int. J. Mech. Sci.*) lowers the critical galloping speed and raises power vs a simple layout — [NWPU Pure](https://pure.nwpu.edu.cn/en/publications/improving-the-galloping-energy-harvesting-performance-with-magnet); magnetic-coupling piezo–EM composite galloping harvester — [PMC9654876](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9654876/)
- A VIV–galloping coupled piezo harvester for industrial use (*Int. J. Mech. Sci.* 2025) — [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0020740325006708); bistable composite-beam wind harvester (*Actuators* 2026, 15(7):409) — [DOI 10.3390/act15070409](https://doi.org/10.3390/act15070409); non-linear bi-directional VIV piezo harvester with magnetic interaction — [PMC8036898](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8036898/)
- A coupling spring on an EM galloping harvester raised power by 93% by recovering energy at stroke ends — [Micromachines 2023](https://doi.org/10.3390/mi14050968)
- A mechanical stopper plus galloping harvester widened bandwidth for both wind and base vibration — [UTS: impact-based broadband](https://opus.lib.uts.edu.au/bitstream/10453/129996/6/An%20impact-based%20broadband.pdf)
- A theoretical paper argues there are fundamental limits to nonlinear energy harvesting (nonlinearity broadens the band but does not raise the power ceiling) — [arXiv 1410.1429](https://arxiv.org/pdf/1410.1429)

**Tandem, wake and interference arrays**
- Hybrid piezo–EM harvester with tandem cylinders (2025): wake interference from dissimilar upstream shapes raised the circular oscillator's power by about 200%. Double tandem square cylinders improved maximum efficiency by 97% over two isolated oscillators — [PMC12824318](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12824318/)
- Abdelkefi et al. tandem piezo harvesters in air: the downstream harvester produced nothing when the upstream cylinder was larger. With a smaller upstream cylinder, wake galloping occurred beyond a critical spacing — search summary ([Southampton eprint](https://eprints.soton.ac.uk/494430))
- Zdravkovich (1988) regimes: proximity-wake interference for G < 3.8, wake interference for G > 3.8 — [Cambridge core](https://www.cambridge.org/core/product/69579BE3FF1ACF8EAD9F152AF883B979)
- A tandem VIV-TENG pair widened the lock-in wind range — [AMiner, Nano Energy 2022](https://www.aminer.org/pub/625223b461bd09704f0c0ffc/vortex-induced-vibration-triboelectric-nanogenerator-for-low-speed-wind-energy-harvesting)

### Inferences
- For a DIY Vortex-style mast, the cheapest high-value widening method is **passive magnetic repulsion springs at the base** with adjustable gap. Opposing magnets give a softening or hardening nonlinearity that shifts the effective natural frequency with amplitude. Second choice is a **sliding tip or internal mass** to retune seasonally (*Sci. Rep.* 2025 approach). The MRE and binary-controller papers show a roughly 2× lock-in range is achievable, but only within about 1.7–3.3 m/s in their small rigs.
- Adding a splitter plate or flattening the mast toward a D-section converts the device toward galloping. That trades a lower top-end cap for a higher cut-in and the need for amplitude stops.

### Gaps
- No quantitative study of passive magnetic-spring tuning on a Vortex-scale (≥1 m) mast was found. Vortex's own magnetic tuning data is covered by other researchers (patents and white papers).

---

## 5. Generator and power electronics for small low-frequency oscillators

### Takeaway
To get watts rather than milliwatts you need (1) frontal area of order 0.1–1 m², (2) **electromagnetic transduction** (moving NdFeB magnets and copper coils, or a mechanical rectifier driving a rotary generator, such as the 2026 cylindrical-cam design or VIVACE's belt-and-pulley drive), and (3) an electrical load set so that electrical damping sits at the optimum damping ratio. Piezo efficiency is below 1%, which limits it to sensor-scale outputs. Interface-circuit literature is dominated by piezo; EM sources are low-impedance and high-current at about 1–100 Hz.

### Cited Findings
- Piezoelectric FIV harvesters have efficiency below 1%; electromagnetic systems have a higher ceiling — [Applied Energy 2026 review](https://www.sciencedirect.com/science/article/abs/pii/S0306261926005891)
- Abdelkefi 2016: electromagnetic, electrostatic and piezoelectric mechanisms are all used; piezo is most popular for its frequency range and ease of application, not for power — [UTB catalogue of IJES review](https://vufind.katalog.k.utb.cz/SummonRecord/FETCH-LOGICAL-c378t-6c669f491f0de937df18d45558c8bb9354ad288e2b95a0c2917841e1b9fbc50b3)
- Optimal damping for harvesting is moderate, not minimal: ζ ≈ 0.025–0.05 (Barrero-Gil et al. 2012) — [ResearchGate](https://www.researchgate.net/publication/251574443_Extracting_energy_from_Vortex-Induced_Vibrations_A_parametric_study); damping parameter ξ = 0.16 at frequency ratio 0.90 gives η = 0.23 — [arXiv 1407.5432](https://arxiv.org/html/1407.5432); VIVACE high-Re optimal damping ratio 0.12 — [Academia.edu VIVACE](https://www.academia.edu/24268680/High_damping_high_Reynolds_VIV_tests_for_energy_harnessing_using_the_VIVACE_converter)
- Vicente-Ludlam, Barrero-Gil & Velázquez (2014) studied **optimal electromagnetic energy extraction** from transverse galloping — [cited in Hémon et al. 2017 JFS](https://yakari.polytechnique.fr/Django-pub/documents/hemon2017rp-1pp.pdf). An axial transducer concept for galloping harvesting is from LadHyX — [ISFA 2020 PDF](http://www.off-ladhyx.polytechnique.fr/people/pascal/pdf/ISFA2020-MAYA.pdf)
- Magnet-in-coil VIV cylinder: the cylinder carries a magnet moving along a coil connected to a resistive load. Output is microwatts at lab scale — [arXiv 1712.01588](https://ar5iv.labs.arxiv.org/html/1712.01588). A square-cylinder EM prototype found harvested power much lower than vibration amplitude suggested, due to resistor dissipation. Its best condition was reduced velocity 7.7 — [ResearchGate: "Investigations on a VIV based energy harvester"](https://www.researchgate.net/publication/321807100_Investigations_on_a_vortex_induced_vibration_based_energy_harvester)
- EM galloping coil layout matters: going from 1 to 2 to multiple off-centre coil sets gave 0.40, 0.62 and 0.72 mW at 9 m/s, with diminishing returns — [OUCI](https://ouci.dntb.gov.ua/works/40y8R23l). A coupling spring increased the duty cycle of induced EMF — [Micromachines 2023](https://doi.org/10.3390/mi14050968)
- Vortex Bladeless uses a linear alternator. The 2026 *Energies* paper instead converts mast oscillation into **unidirectional rotation** with a cylindrical cam (sinusoidal internal groove, billet/follower rolling contact) — [Energies 19(4):1090, DOI 10.3390/en19041090](https://doi.org/10.3390/en19041090)
- Interface circuits: the standard piezo chain is AC-DC rectifier → MPPT → DC-DC → storage. MPPT methods include perturb-and-observe and fractional open-circuit voltage. Resistive impedance matching works only near resonance — [Sensors 2025 review, DOI 10.3390/s25134029](https://mdpi.com/1424-8220/25/13/4029); [PMC9324395 "Circuit techniques for high-efficiency piezoelectric energy harvesting"](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9324395/)
- EM induction sources sit roughly in the 10–100 Hz range and suit converters needing higher current than voltage, because of their low output impedance — [Tanzawa, Shizuoka Univ. repository](https://shizuoka.repo.nii.ac.jp/record/10837/files/181010002.pdf)

### Inferences
- **Standard EM harvester theory (textbook background, not fetched here):** electrical damping c_e = (B·l)²/(R_coil + R_load), and maximum power transfer to the load occurs near R_load ≈ R_coil + (B·l)²/c_m. In plain terms, the generator is the damper. For a VIV mast this means the load must be set so the generator adds roughly the optimal damping ratio (literature: about 0.03–0.16 depending on definition). **Too heavy a load (e.g. a flat battery connected directly) kills lock-in.** Too light a load wastes energy in structural damping.
- A mast oscillating at 1–5 Hz with about 1–5 cm tip stroke at the base generator gives low coil velocity, hence low EMF. Use many turns, strong N42–N52 magnets, a short magnetic gap, motion amplification (a lever from mast to coil), or a mechanical rectifier (cam, ratchet, rack-and-pinion with one-way clutches) to drive a small rotary PM generator at higher RPM. The cam paper and VIVACE's belt drive both go the rotary route, which makes rectification and charging easier.
- For battery charging: full-wave bridge (Schottky diodes or an active/synchronous rectifier to avoid about 0.3–0.7 V drops at low EMF), a buck-boost or boost converter with fractional-Voc or P&O MPPT, then a LiFePO4 or supercap buffer. Off-the-shelf energy-harvesting PMICs suit the mW regime. Small-wind MPPT charge controllers suit the W regime only if the rectified voltage is high enough.

### Gaps
- No review specific to MPPT for **low-frequency electromagnetic** VIV or galloping wind harvesters was found. The literature is piezo-dominated.
- No published coil/magnet sizing design guide for a ≥1 m VIV mast linear generator was found in the searched literature.

---

## 6. Structural and practical issues: fatigue, damping, noise, base mounting, safety, storms

### Takeaway
Galloping amplitude grows without bound as wind rises, so galloping harvesters need bump stops or amplitude-limiting bases. Fatigue (beam bending stress, yield stress) is the binding constraint on harvested energy. Modelled VIV masts face a direct trade-off between power and structural safety (Glasgow: 600 W max vs 460 W "safe"). Piezo galloping devices are generally framed as being for winds ≤6 m/s; above about 7 m/s a propeller turbine is the better choice. Real-site turbulence and annual-energy data are still missing.

### Cited Findings
- An impact bump stop on a square-body galloping piezo harvester reduced bending stress and improved fatigue life vs the baseline. Damping, electrical response and LCO amplitude were measured — [ADS 2014SMaS...23j4012E](https://ui.adsabs.harvard.edu/abs/2014SMaS...23j4012E/abstract)
- Wang et al. used a U-shaped base to limit galloping amplitude and prevent damage at high wind speeds (as cited) — search summary ([Micromachines 14(2):271](https://mdpi.com/2072-666X/14/2/271))
- A theoretical paper treats beam yield stress as a hard limit on harvested energy, notes small allowable tip displacement, and calls for galloping amplitude control systems in engineering applications — [x-mol](https://www.x-mol.com/paperRedirect/1303165832069877760)
- A recent piezo galloping paper warns that excessive (wake) galloping can cause instability, overload and damage. It says these harvesters are designed for about ≤6 m/s, and at ≥7 m/s a conventional propeller generator is the better choice — search summary ([Micromachines 14(2):271](https://mdpi.com/2072-666X/14/2/271))
- Glasgow: peak efficiency (6%) and max power (600 W) trade off against structural safety. The recommended safe design is 460 W at 0.8 m × 0.65 m. The model assumes steady wind; turbulence and changing wind are future work. Some short, wide configurations exceeded the Reynolds range where the wake-oscillator model is validated — [Glasgow Enlighten](https://eprints.gla.ac.uk/357207); [Glasgow news](https://www.gla.ac.uk/news/archiveofnews/2025/june/headline_1187739_en.html); [Ecoticias](https://www.ecoticias.com/en/a-bladeless-wind-turbine-that-sways-in-the-wind-could-safely-produce-460-watts-in-computer-simulations-and-the-most-efficient-design-turned-out-not-to-be-the-most-powerful/53690/)
- Commentary notes that annual energy output is the right yardstick, and no such number yet exists for the Glasgow design — [Ecoticias](https://www.ecoticias.com/en/a-bladeless-wind-turbine-that-sways-in-the-wind-could-safely-produce-460-watts-in-computer-simulations-and-the-most-efficient-design-turned-out-not-to-be-the-most-powerful/53690/)
- The *Sci. Rep.* 2025 paper ties optimal design to composite material mechanical properties (fatigue and stiffness relevant) — [Nature Sci. Rep.](https://www.nature.com/articles/s41598-024-82385-9)
- An ETASR study of four mast prototypes with different materials and dimensions found mast diameter played a key role in response — [ETASR](https://etasr.com/index.php/ETASR/article/download/12314/5476/62799)
- Indonesian design study: one model starts oscillating at 3 m/s, two modified models at 1 m/s — [arXiv 2205.02786](https://arxiv.org/pdf/2205.02786)

### Inferences
- For a domestic build: (1) fit hard end stops or elastomer bump stops, and make the base spring the weak link sized for fatigue, not yield, at maximum stroke (mast oscillations run at about 10⁷–10⁸ cycles/year at 1–5 Hz). (2) For VIV masts, the risk in storms is not lock-in (self-limiting at about 1 D) but drag bending moment at the base and possible galloping if the section is non-circular or iced. (3) Provide a brake or lock-out (shorting the coil adds heavy electrical damping, which pushes the mast out of lock-in). This last point follows from the damping theory above; it has not been checked against a source.
- Noise: VIV masts have no blade-tip noise, but magnets and end stops can knock or clatter. Plan elastomer damping.

### Gaps
- No peer-reviewed measurements of **acoustic noise**, **fatigue life of a full-scale mast**, or **storm survival** of VIV bladeless turbines were found.
- No standard (IEC 61400-2 style) assessment of bladeless masts was found.

---

## 7. Theses and open-access reports documenting build-and-test

### Takeaway
No full master's or PhD thesis documenting a complete small VIV wind generator build with drawings was found through search. The best open-access build-and-test documents are undergraduate project reports (WPI MQPs), a Spanish TFG (UPV), a PolyU thesis on fins, an arXiv thesis-format piezo galloping design, and open-access UPM and LadHyX papers. Vortex Bladeless's own development included wind-tunnel testing at UPM's IDR (Instituto Ignacio Da Riva).

### Cited Findings
- WPI Major Qualifying Project BJS-WD14, "Wind Harvesting via Vortex Induced Vibration": a small wind-tunnel prototype working at 5.4–6.6 m/s — [WPI digital repository](https://digital.wpi.edu/downloads/00000130x?locale=en); a second related WPI report — [WPI dj52w607z](https://digital.wpi.edu/downloads/dj52w607z?locale=en)
- Thesis-format "Design of a Piezoelectric Wind Energy Harvester" (2025): covers VIV and other instabilities, a mathematical model and a literature review. Its focus is galloping — [arXiv 2502.05103](https://arxiv.org/pdf/2502.05103)
- UPV (Valencia) TFG on a wind generator driven by resonant vibrations self-excited by the vortex street — [RiuNet 10251/143371](https://riunet.upv.es/handle/10251/143371); related UPV parametric interaction study — [RiuNet 10251/147959](https://riunet.upv.es/handle/10251/147959)
- OEPM (Spanish patent office) case study: Vortex was tested in the wind tunnel of the Instituto Universitario de Microgravedad "Ignacio Da Riva", UPM. Description: a vertical cylinder on an elastic rod embedded in the ground, resonating with vortex shedding, with an alternator — [OEPM CasoExito VORTEX PDF](https://www.oepm.es/export/sites/oepm/comun/documentos_relacionados/PDF/2020/CasoExito_VORTEX.pdf)
- UNLP (Argentina) numerical study of aerodynamic coupling between cylinders for VIV wind harvesters — [CAIA-UNLP PDF](https://caia.ing.unlp.edu.ar/wp-content/uploads/2023/11/7249-ANALISIS-NUMERICO-DEL-ACOPLAMIENTO-AERODINAMICO-ENTRE-CUERPOS-CILINDRICOS-PARA-APLICACION-EN-COSECHADORES-DE-ENERGIA-EOLICA-MEDIANTE-VIBRACIONES-INDUCIDAS-POR-VORTICES.pdf); also AMCA proceedings — [amcaonline.org.ar](https://amcaonline.org.ar/ojs/index.php/mc/article/download/6069/6073)
- UNAM thesis "Vibraciones de un cilindro infinito inducidas por vórtices" — [UNAM catalogue](https://bibmacro-descubridor.dgb.unam.mx/Record/20.500.14330-TES01000734413/Description?lng=en)
- Universidade NOVA de Lisboa (RUN) thesis download on a related topic — [run.unl.pt](https://run.unl.pt/bitstreams/e9edcb3a-a7fd-47af-8917-5e61c5d1ce73/download)
- PolyU thesis on a finned cylinder at various angles of attack — [PolyU PDF](https://theses.lib.polyu.edu.hk/bitstream/200/13132/3/7584.pdf); PolyU energy harvesting thesis or paper (Zhao) — [PolyU IRA](https://ira.lib.polyu.edu.hk/bitstream/10397/107794/1/Zhao_%20Energy_Harvesting_Based.pdf)
- LadHyX (École Polytechnique) galloping-prism harvester papers (ISFA 2016, 2020) — [ISFA2016](http://www.off-ladhyx.polytechnique.fr/people/pascal/pdf/ISFA2016_FullPaper.pdf); [ISFA2020 axial transducer](http://www.off-ladhyx.polytechnique.fr/people/pascal/pdf/ISFA2020-MAYA.pdf)
- UPM open-access Barrero-Gil galloping paper — [oa.upm.es](https://oa.upm.es/7294/2/INVE_MEM_2010_78822.pdf)
- VIVACE DOE final report (Vortex Hydro Energy, Michigan), with detailed design and test data (water) — [OSTI 896401](https://www.osti.gov/servlets/purl/896401)
- Student-level bladeless build papers: "Design and fabrication of Vortex bladeless turbine" — [ResearchGate](https://www.researchgate.net/publication/350682159_DESIGN_AND_FABRICATION_OF_VORTEX_BLADELESS_TURBINE); "Experimental analysis of VIV in the bladeless small wind turbine" — [ResearchGate](https://www.researchgate.net/publication/338814549_Experimental_Analysis_of_Vortex_Induced_Vibration_in_the_Bladeless_Small_Wind_Turbine); piezo bladeless (*Applied Sciences* 12(15):7769, 2022) — [DOI 10.3390/app12157769](https://doi.org/10.3390/app12157769)

### Inferences
- The WPI MQP and UPV TFG are the most likely to contain build drawings and BOM-level detail, but this is unverified because the full texts could not be fetched.

### Gaps
- No DTU, MIT or Michigan (other than VIVACE) thesis on a small **wind** VIV or galloping generator surfaced in searches. UPM's repository (oa.upm.es) likely holds TFMs on Vortex-related work, but none was found by title.

---

## 8. 2024–2026 papers modelling or testing Vortex-style masts

### Takeaway
Recent work is mostly numerical (wake-oscillator models, CFD, FSI) plus small wind-tunnel rigs in the 1.7–5 m/s range. Peer-reviewed figures are sobering: about 6% peak efficiency in the best model (Glasgow 2025), sub-mW to a few mW from small physical prototypes, and roughly 2× lock-in widening from stiffness tuning. The 2026 *Energies* cam paper proposes a mechanical rectifier (oscillation → rotation) but its performance numbers were not retrievable.

### Cited Findings
- **Energies 2026, 19(4):1090**, "Design and numerical analysis of a novel VIV bladeless wind turbine with cylindrical cam mechanical conversion": a cylindrical cam with a sinusoidal internal groove and billet/follower rolling contact converts mast oscillation into unidirectional rotation. Includes CFD of vortex shedding. Purely numerical — [DOI 10.3390/en19041090](https://doi.org/10.3390/en19041090); [MDPI page](https://www.mdpi.com/1996-1073/19/4/1090); commentary — [foro3d Jan 2026](https://foro3d.com/en/2026/january/bladeless-wind-turbines-energy-from-vortex-vibration.html)
- **Breen, Mallik & Adhikari 2025, *Renewable Energy* 254:123549** (Glasgow): wake-oscillator plus coupled elastic and rigid-body model over a broad parameter sweep. Peak efficiency **6%**, max power **600 W**, safe optimum **460 W** at **0.8 m height × 0.65 m diameter**. Real prototypes so far peak at about 100 W. Longest masts were most efficient but less powerful; the abstract stresses diameter as raising both power and efficiency (the sources emphasise different parameters) — [Glasgow Enlighten](https://eprints.gla.ac.uk/357207); [Glasgow news](https://www.gla.ac.uk/news/headline_1187739_en.html); [TechXplore](https://techxplore.com/news/2025-06-optimal-potential-bladeless-turbines.html); [The Engineer](https://www.theengineer.co.uk/content/news/simulations-unveil-optimal-design-for-bladeless-wind-turbines)
- ***Sci. Rep.* 15:1355 (2025)**, "A novel optimal design approach for bladeless wind turbines considering mechanical properties of composite materials used": natural-frequency tuning via stand effective length or internal mass; **+55.7% efficiency**; Pm(RMS) = 119.26 W at 8 m/s (extracted text garbled, verify) — [Nature](https://www.nature.com/articles/s41598-024-82385-9)
- **Biomimetics 2025, 10(10):692**, columnar-cactus mast: a scaled wind-tunnel prototype. The cross-section increases lift and amplitude, with a higher power coefficient and lower wake turbulence than a cylinder. The cylinder is superior below 5 m/s — [DOI 10.3390/biomimetics10100692](https://doi.org/10.3390/biomimetics10100692)
- ***Applied Sciences* 2024, 14(18):8217** (Kang et al.): discrete resonance-shifting module — [DOI](https://doi.org/10.3390/app14188217). ***Applied Sciences* 2026, 16(1):553**: binary resonance controller, 88.9% shift, lock-in 1.7–3.2 m/s — [DOI](https://doi.org/10.3390/app16010553). ETASR MRE mast: 64.3% shift, 2.0–3.3 m/s — [ETASR](https://etasr.com/index.php/ETASR/article/download/12314/5476/62799)
- **Hamdan et al., *Energies* 17(1):214** (Dec 2023/2024, Abu Dhabi University): experimental plus two-way FSI study of VBWTs with economic and environmental analysis. Numeric results not in the abstract — [DOAJ](https://doaj.org/article/82d69811da0e4acf842533598c4a8286); [ADU repository](https://repository.adu.ac.ae/items/00a55835-ec04-4e2b-a121-3f703e7b026b)
- ***Energies* 2026, 19(1):25**: optimal design methodology for a piezo-based bladeless wind turbine (cantilever-mounted cylinder) — [MDPI](https://www.mdpi.com/1996-1073/19/1/25)
- **EPJ Web of Conferences 2026, 355:04001**: CFD comparison of mast shapes at 1, 3 and 5 m/s with 20 cm and 22.5 cm diameter cylinders — [EPJ Conf](https://www.epj-conferences.org/10.1051/epjconf/202635504001)
- **Springer chapter 2026**, "Investigation of frequency response of bladeless cylindrical wind turbine": wind-tunnel study; oscillation near natural frequency maximises energy — [Springer](https://link.springer.com/chapter/10.1007/978-981-96-9600-0_19)
- **Abyssinia J. Eng. Comput. 2024**: 3D-printed mast, 0.43 mW at 3 m/s, amplitude ratio 0.155 — [AJOL](https://ajol.info/index.php/ajec/article/view/286124)
- "Design optimization of VIV bladeless wind turbines for urban energy harvesting" (2025, ResearchGate) reports highest efficiency 16.99% at 2.75 m (metric unclear) — [ResearchGate](https://www.researchgate.net/publication/396334795_Design_Optimization_of_Vortex-Induced_Vibration_Bladeless_Wind_Turbines_for_Urban_Energy_Harvesting)
- arXiv 2410.13506, "Development of a new type of Vortex bladeless wind…" (content not retrieved) — [arXiv](https://arxiv.org/pdf/2410.13506)
- IEOM 2024 Taguchi optimisation of the Vortex 3D model: 1.25 → 3.44 kW (conference; treat as low reliability). Also suggests a conical mast to synchronise shedding along height — [IEOM PDF](https://ieomsociety.org/proceedings/2024dubai/507.pdf)
- Integrated FE aeroelastic plus piezo model of a bladeless turbine as a cantilever beam — [IJIRSS](https://www.ijirss.com/index.php/ijirss/article/download/5033/790/8131)
- Flutter and other non-VIV bladeless approaches (brief): flutter-TENGs report 29.09 mW/m² at 10 m/s and up to 2850 mW/m² in another design (different normalisations). See the flutter review — [Li et al. 2022](https://onlinelibrary.wiley.com/doi/full/10.1002/msd2.12035)

### Inferences
- The "about 6% peak energy capture" figure the coordinator mentioned comes from Breen et al. (2025). It is model-based, not measured.
- Mechanical rectification (cam, VIVACE-style rotary drive) is the trend for getting usable power from slow oscillation, as an alternative to Vortex's linear alternator. For DIY, a rotary generator via a mechanical rectifier is easier to source than a custom linear alternator.

### Gaps
- Full numeric results (mast size, wind speed, predicted W) of the *Energies* 2026 cam paper were not retrievable because mdpi.com fetch failed. Look up DOI 10.3390/en19041090 directly.
- No 2024–2026 peer-reviewed **field** (outdoor, real-turbulence) test of a Vortex-style mast with a measured power curve was found.
