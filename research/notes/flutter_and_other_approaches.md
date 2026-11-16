# Non-VIV Bladeless Wind Approaches at Domestic Scale: Flutter (Windbelt), Oscillating Aerofoils, Piezo, Triboelectric, Electrostatic, Ducted/Static-Aerofoil

Research date: 16 Nov 2026. Method note: WebFetch failed (ENOTFOUND) for hackaday.com, pmc.ncbi.nlm.nih.gov, energymanagermagazine.co.uk and vernier.com, so most findings come from WebSearch result snippets and summaries, not full-page reads. Where a figure comes only from a snippet, it is marked as such. Vortex Bladeless / VIV mast material is deliberately excluded (covered by other researchers).

Physics anchor for all sections below (my own calculation from the standard formula P = 0.5 x rho x A x v^3, rho = 1.225 kg/m3): wind carries about 16.5 W/m2 at 3 m/s, 76.6 W/m2 at 5 m/s, 132 W/m2 at 6 m/s and 612 W/m2 at 10 m/s. A Betz-limit (59.3%) machine with 1 m2 of frontal area at 5 m/s could make at most ~45 W. Every device below should be judged against that ceiling.

---

## 1. Windbelt (Shawn Frayne / Humdinger Wind Energy): how it works, measured outputs, company fate, DIY builds, independent tests

### Takeaway
The Windbelt is a tensioned polymer ribbon that flutters (aeroelastic flutter, inspired by the 1940 Tacoma Narrows collapse) and shakes magnets past coils. Measured outputs were milliwatts (microBelt ~0.2 mW at 3.5 m/s to ~5 mW at 7.5 m/s; ~2 mW at 5.5 m/s; ~40 mW claimed for a ~1 m prototype at 10 mph), which works out to roughly 0.2-0.5% of the wind power crossing the device. The headline "10-30x more efficient than microturbines" claim is described as refuted. Humdinger never reached mass market and faded; DIY builds are easy and cheap but give LED-level power (e.g. ~1.5 V AC, 20 mA short-circuit).

### Cited Findings
**Origin and mechanism**
- Invented by Shawn Frayne in 2004; a flexible polymer ribbon is stretched between supports transverse to the wind with magnets glued to it; the vibrating ribbon moves magnets relative to coils — [Wikipedia: Windbelt](https://en.wikipedia.org/wiki/Windbelt) (via search snippet; also flagged "needs update" since Dec 2016)
- Frayne was working in Haiti in 2004 in communities lit by kerosene lamps and took inspiration from the 1940 Tacoma Narrows Bridge collapse — [ecoportal.net](https://www.ecoportal.net/en/energy-hack-makes-wind-bladeless-more-power/16847/)
- The belt "vibrates (like a guitar string)"; a magnet on the belt moves relative to a coil; one description attributes the motion to vortex shedding that alternately produces low and high pressures on the belt — [Symscape blog "Wind Belt: Wind Power Minus the Spin"](https://www.symscape.com/blog/wind-belt-wind-power-minus-the-spin.html). (Most other sources call it aeroelastic flutter; the forcing mechanism is described differently by different sources.)
- US patent family: "Generator utilizing fluid-induced oscillations" — [US 8,026,619 (Justia)](https://patents.justia.com/patent/8026619); applications [US20080129254A1](https://www.google.ca/patents/US20080129254) and [US20100207395A1](https://www.google.ca/patents/US20100207395)
- Winner of Popular Mechanics' 2007 Breakthrough Award; described as "a taut membrane with magnets that oscillate between metal coils" — [Newser, 2007 Breakthrough Awards](https://www.newser.com/story/9211/2007-breakthrough-awards.html); [Daily Kos, Oct 2007](https://www.dailykos.com/stories/2007/10/13/397747/-)
- Make: (20 Oct 2007) covered it as a simple build: prototype powered LEDs and a clock using a few dollars' worth of electronics; "you can probably build one yourself before the weekend is through" — [Make: "Windbelt: elegant non-turbine wind generator"](https://makezine.com/2007/10/20/windbelt-elegant-nonturbine-wi/)

**Measured / claimed outputs by model**
- Original ~1 m prototypes: "40 milliwatts in 10-mph" winds (10 mph = 4.5 m/s), framed by Popular Mechanics as "10 to 30 times more efficient than the best microturbines" — [cleanergy blog (Mar 2008) quoting PM](https://cleanergy.blogspot.com/2008/03/innovative-low-cost-windbelt-could.html); [Tom's Guide "Good Vibrations Promise Cheap Wind Power"](https://www.tomsguide.com/us/wind-power-energy-green-energy-windmills,news-6192.html); [signalvnoise](https://signalvnoise.com/posts/1238-turning-aeroelastic-flutter-into-third-world-power)
- microWindbelt: 0.2 mW at 3.5 m/s and 5 mW at 7.5 m/s, given as efficiencies (eta x Cp) of "0.21 and 0.53" — [Wikipedia: Windbelt](https://en.wikipedia.org/wiki/Windbelt) (search snippet)
- microWindbelt cross-sectional area 37 cm2 — [Imperial College "Design and performance" paper](https://t4awstest.cc.ic.ac.uk/media/imperial-college/faculty-of-engineering/electrical-and-electronic-engineering/public/optical-and-semiconductor-devices/pubs/Design-and-performance.pdf) (snippet cut off before its output figures)
- microBelt (product, ~2010): 2 mW at 5.5 m/s; output begins at about 3 m/s — [IDTechEx / Off-Grid Energy Independence](https://www.offgridenergyindependence.com/articles/2146/wind-energy-harvester-from-humdinger); [Geeky Gadgets, 4 Feb 2010](https://www.geeky-gadgets.com/tiny-wind-powered-supercharger-02-04-2010/); [Ubergizmo, Apr 2010](https://www.ubergizmo.com/2010/04/humdinger-wind-energys-microbelt-turbine); [Windfair "product pick of the week"](https://w3.windfair.net/wind-energy/pr/7237-product-pick-of-the-week-the-humdinger-wind-energy-039-s-microbelt-turbine)
- Cell-phone-sized model in development (Dec 2008): 3-10 mW — [Honolulu Advertiser, 7 Dec 2008](https://the.honoluluadvertiser.com/article/2008/Dec/07/bz/hawaii812070327.html)
- Windcell (~1 m long): 1-10 W per Honolulu Advertiser (2008) — [Honolulu Advertiser](https://the.honoluluadvertiser.com/article/2008/Dec/07/bz/hawaii812070327.html); 3-5 W per [Tom's Guide](https://www.tomsguide.com/us/wind-power-energy-green-energy-windmills,news-6192.html). Sources conflict.
- Windcell Panel (1 m2 array, intended for grid-tie): "power rating of 100 W", projected manufacturing cost US$1/W — [EnergyMatters (Australia)](https://www.energymatters.com.au/renewable-news/em799/); contrasted with Wikipedia's projection of ~10 W average for a 1 m2 panel at 6 m/s average wind — [Wikipedia: Windbelt](https://en.wikipedia.org/wiki/Windbelt). Both are projections, not measurements.
- A physics professor estimated (2008) that the Windbelt converts about 10% of wind power into electricity — [Honolulu Advertiser](https://the.honoluluadvertiser.com/article/2008/Dec/07/bz/hawaii812070327.html). This conflicts sharply with the 0.21-0.53% figures above.
- Windbelt still needs "sufficient wind for maximum generation (6 m/s or 13 mph)" — [Make: Backyard Wind Power project page (search summary)](https://makezine.com/projects/backyard-wind-power/)

**Independent tests / debunking**
- Wikipedia states the inventor's claim of being "10-30 times more efficient than small wind turbines" has "been refuted by tests"; the snippet does not name the tests — [Wikipedia: Windbelt](https://en.wikipedia.org/wiki/Windbelt)
- A Wikipedia talk-page editor argued the claim was physically implausible and that sub-1 m turbine efficiencies are typically "well under 1%" (unsourced, contested opinion) — [Talk:Windbelt](https://en.wikipedia.com/wiki/Talk:Windbelt)
- Slashdot commenters (2008) noted the comparison was made at low speeds (10 mph) and that all devices suffer from the cubic dependence of wind power on speed — [Slashdot, 11 Sep 2008](https://hardware.slashdot.org/story/08/09/11/2257228/the-windbelt-a-cheap-wind-power-generator)
- A retrospective says the 10-30x figure "raced around the internet for years" and the honest version is narrower but "still doing something real" — [ecoportal.net](https://www.ecoportal.net/en/?p=16847)

**Academic replications of the windbelt concept (independent of Humdinger)**
- Foong & Wood (2014), J. Physics: Conf. Series 557, theoretical + experimental study of a windbelt-based harvester for low-speed changing winds; model of scaling effect on critical flutter frequency validated experimentally (power figures not in snippet) — [DOI 10.1088/1742-6596/557/1/012089](https://doi.org/10.1088/1742-6596/557/1/012089)
- An academic study reports "~7 mW at ~3 m/s with a 1 m long belt" (snippet from a search result; exact paper attribution uncertain — appeared alongside [TIB PDF](https://edocs.tib.eu/files/e01fn13/770739350.pdf) and [Peeref record](https://peeref.com/works/15636531))
- Malaysian optimized aeroelastic wind belt (J. Chinese Society of Mechanical Engineers, 2020): 81.02 mW at 6 m/s with belt tension 0.816 N, coils in parallel — [CAS catalogue record "Design of Aeroelastic Wind Belt for Low-Energy Wind Harvesting"](https://katalog.lib.cas.cz/KNAV/EdsRecord/edsair,edsair.doi...........7e8024f083f2d4fb3c9cf088cc770155); related [Heriot-Watt "Quantification of Aeroelastic Wind Belt for Malaysia"](https://researchportal.hw.ac.uk/en/publications/quantification-of-aeroelastic-wind-belt-for-malaysia/)
- Lu et al. flutter-based electromagnetic harvester in a small wind tunnel: maximum average power 705 µW (cited in a Malaysian case study; conditions not in snippet) — [Semarak Ilmu journal PDF](https://semarakilmu.com.my/journals/index.php/fluid_mechanics_thermal_sciences/article/download/2554/2249/19421)
- Benchmark flutter device (not a windbelt), curved-panel aeroelastic harvester, Applied Energy 2019: 0.032 mW/cm3 sustained at 25 m/s — [INIS/IAEA record](https://inis.iaea.org/records/c03cc-5ss84)
- Aquino et al. (2017), Strathclyde, "Wind-Induced Flutter Energy Harvester": wind-tunnel tests + CFD for building integration — [Strathprints PDF](https://strathprints.strath.ac.uk/67894/1/Aquino_etal_EP_2017_A_study_on_the_Wind_Induced_Flutter_Energy_Harvester.pdf)
- U. Penn MEMS lab: "An Electromagnetic Energy Scavenger from Direct Airflow" (flutter-type) — [PDF](https://mems.seas.upenn.edu/wp-content/uploads/2020/03/An-Electromagnetic-Energy-Scavenger-from-Direct-Airflow.pdf)

**Company fate**
- Humdinger Wind Energy LLC was a Hawaii LLC with a Hong Kong subsidiary, "primarily a research and development house focused on pushing forward the development of the Windbelt technology" (manual v3.0) — [Scribd copy of Windbelt manual](https://www.scribd.com/document/387148047/WINDBELT-MANUAL-pdf); [EnergyMatters](https://www.energymatters.com.au/renewable-news/em799/)
- 2008 interview: Humdinger was a for-profit startup developing a flexible, modular "wind cell" for small scale — [Disruptor League, 8 Nov 2008](https://www.disruptorleague.com/blog/2008/11/08/interview-with-humdinger-wind-energys-shawn-fayne/page/4124/)
- Windcell commercialization was said (2008) to be 18-24 months away; EnergyMatters later noted Windbelt products had not hit the market and Humdinger was seeking licensing partners — [Honolulu Advertiser](https://the.honoluluadvertiser.com/article/2008/Dec/07/bz/hawaii812070327.html); [EnergyMatters](https://www.energymatters.com.au/renewable-news/em799/)
- "Humdinger, the company built around it, faded"; "wide commercial deployment of the Windbelt never truly arrived"; Frayne moved to other inventions including a small machine for printing low-cost solar panels — [ecoportal.net](https://www.ecoportal.net/en/energy-hack-makes-wind-bladeless-more-power/16847/)
- Humdinger co-developed an educational Windbelt kit with the KidWind Project (now Vernier); manual notes higher belt frequency gives higher voltage, magnet amplitude matters, wind speed "is very important," and "the Classic Windbelt will only work well with a powerful fan" — [Vernier/KidWind Humdinger Windbelt manual PDF](https://www.vernier.com/files/kidwind/humdinger_windbelt_manual.pdf) (content via search summary; direct fetch failed)

**DIY builds**
- Instructables "Windbelt Redux — 21st Century Micro Power Generation": ~1.5 V AC, ~20 mA short-circuit current; drives two anti-parallel LEDs; designed for house cross-ventilation; no wind speed/load stated — [Instructables](https://www.instructables.com/Windbelt-Redux--21st-Century-Micro-Power-Generatio) (also [SlideShare copy](https://www.slideshare.net/slideshow/measuring-device/5463899))
- Instructables "How to build cheap VHS tape WINDBELT generator" (VHS tape as belt; no measured output in snippet) — [Instructables](https://www.instructables.com/HOW-TO-build-cheap-VHS-tape-WINDBELT-generator)
- Blog build (5 Nov 2009), wood and duct tape; "need an even tension across the belt to get it to vibrate" — [Building Stuff in the Basement](https://buildingstuffinthebasement.blogspot.com/2009/11/diy-windbelt-with-wood-and-duct-tape.html)
- Scribd Windbelt manual: belt, stators, magnets, rectifier, test LED; higher vibration frequency gives higher voltage — [Scribd](https://www.scribd.com/document/387148047/WINDBELT-MANUAL-pdf)
- Hackaday (30 Jun 2020) "Experimenting with vibratory wind generators": a Venetian-blind slat with a coil glued to neoprene and an opposing magnet; "output is tiny"; commenters suggested a wind-belt layout and noted that drawing current damps the resonance — [Hackaday](https://hackaday.com/2020/06/30/experimenting-with-vibratory-wind-generators) (search summary; fetch failed). The same post argued a mechanical micro-generator would need "100K+ hours of unattended unmaintained operation" to beat a battery — [Hackaday](https://hackaday.com/2020/06/30/experimenting-with-vibratory-wind-generators)
- Hackaday (9 Mar 2023) "How simple can a wind generator get": flapping designs could pack more units into a given wind-facing area because of smaller cross-section — [Hackaday](https://hackaday.com/2023/03/09/how-simple-can-a-wind-generator-get)
- Supermagnete user project (magnetic wind generator, type not confirmed as a windbelt): ~18 V at 30 km/h and 12 V at 8 km/h (open-circuit voltages, no current/power given) — [Supermagnete "Harnessing wind energy"](https://www.supermagnete.de/eng/Magnet-applications/Harnessing-wind-energy)
- Comparison point, a tiny DIY bladed turbine (Make: "Chispito"): ~1 W (147 mA at 6.7 V) at ~20 mph — [Make: Backyard Wind Power](https://makezine.com/projects/backyard-wind-power/)

### Inferences
- The Wikipedia efficiency figures are almost certainly percentages: power through 37 cm2 at 3.5 m/s is ~97 mW and at 7.5 m/s ~956 mW (my calculation), so 0.2 mW and 5 mW = 0.21% and 0.52%. The microBelt's 2 mW at 5.5 m/s (wind power ~377 mW through 37 cm2) is likewise ~0.5%. This is an order of magnitude below even small turbines and two orders below the "10%" physicist estimate, supporting the "refuted" verdict.
- The best academic windbelt result found (81 mW at 6 m/s) is still ~1/12 of the Make: Chispito mini turbine's ~1 W at ~9 m/s; per unit effort a crude bladed micro-turbine wins by 1-2 orders of magnitude.
- DIY windbelt numbers like "1.5 V, 20 mA short-circuit" do not equal 30 mW deliverable; matched-load power for such a coil would be roughly a quarter of V_oc x I_sc (~7 mW) at best (standard matched-load approximation, not measured).
- A realistic home Windbelt is an educational/demo device or an LED/sensor-node trickle source (mW), not a battery-charging power source.

### Gaps
- No independent, published wind-tunnel test of Humdinger's ~1 m Windbelt or Windcell was found; the tests behind "refuted by tests" are not identified in the snippets.
- Exact date/manner of Humdinger's wind-down (dissolution, licensing) not found.
- No Hackaday.io or YouTube DIY windbelt with a full power curve (W vs m/s into a matched load) was found; no Reddit/FieldLines threads surfaced in searches.
- Could not confirm the paper behind "~7 mW at 3 m/s, 1 m belt".

---

## 2. Other flutter / oscillating-aerofoil generators: Saphonian, Katrick Wind Panel, oscillating wing harvesters, wind harps — any DIY versions?

### Takeaway
Saphonian (Tunisia) and Katrick (Scotland) are oscillating-surface machines aimed at commercial scale; neither has published independent performance data, neither is buyable, and no DIY replications were found. Katrick's own test number (41 W average at 10.2 m/s) is far below its 1 kW rating. Saphonian's claims (up to 80% efficiency, beating Betz) are physically implausible and unverified.

### Cited Findings
**Saphonian (Saphon Energy, Tunisia)**
- Developed by Tunisian start-up Saphon Energy, named after a Carthaginian wind deity; a stationary, sail-shaped body moves back and forth with the wind; motion is converted via a hydraulic system that can store pressure for use when wind drops — [New Atlas](https://newatlas.com/saphonian-bladeless-wind-turbine/24890/?amp=true); [Talking Points Memo](https://talkingpointsmemo.com/idealab/from-tunisia-the-future-of-wind-power)
- "Zero-Blade Technology" eliminates blades, hub and gearbox; inventors Anis Aouini and Hassine Labaied filed in Tunisia in 2010 and received an international patent in 2012; claimed capture "up to 80%" — [SciDev.Net](https://www.scidev.net/global/?p=36757)
- Developers claimed it surpasses the Betz limit (59.3%) — [TPM](https://talkingpointsmemo.com/idealab/from-tunisia-the-future-of-wind-power); coverage was skeptical and no independent hard figures were published — [New Atlas](https://newatlas.com/saphonian-bladeless-wind-turbine/24890/?amp=true)
- The company sought a manufacturing partner and hoped a single sail could eventually make a megawatt — [Yahoo / The National](https://www.yahoo.com/news/wind-energy-converter-inspired-ancient-boats-101727650.html); still being promoted in 2016 — [Africanews, 27 Apr 2016](https://africanews.com/amp/2016/04/27/tunisia-revolutionary-bladeless-wind-turbine-could-change-game-in-wind-farms); also [Windtech International](https://www.windtech-international.com/contacts/the-saphonian), [Climate Home News](https://climatechangenews.com/?p=10913), [BuzzOnEarth 2018](https://buzzonearth.com/blog/2018/04/18/bladeless-wind-turbine-next-revolution-in-wind-energy/amp/)

**Katrick Technologies Wind Panel (Glasgow)**
- Hexagonal, honeycomb-shaped panel of channelling ducts, each with aerofoils that convert wind into mechanical oscillation, then electricity; each module has two aerofoils that can oscillate independently or coupled; aerofoils respond to gusts in <1 s — [Wind Systems Mag](https://www.windsystemsmag.com/news/katrick-wind-panel-tech-shows-promising-energy-capture-results/); [Balkan Green Energy News](https://balkangreenenergynews.com/future-of-wind-energy-turbines-without-blades); [REPQJ paper "Development of a near-ground novel wind energy converter"](https://repqj.com/index.php/repqj/article/view/4537)
- Simulation (Katrick co-authored paper): up to 370 W at 12 m/s and 210 W at 10 m/s — [REPQJ](https://repqj.com/index.php/repqj/article/view/4537/3842)
- Company-reported test: average 41.1 W at 10.2 m/s — [Wind Systems Mag](https://www.windsystemsmag.com/?p=30920)
- Wind-tunnel test showed ~1.5x wind acceleration from ducting even at lower speeds (speed multiplier, not power) — [Magazine Industry USA](https://magazine-industry-usa.com/news/80034-katrick-technologies-begins-next-stage-of-wind-technology-prototype-testing)
- Rated 1 kW per hexagonal unit; LCOE claim 12p/kWh; 18-month pilot at Edinburgh Airport; feasibility study recommended a 10 MW Phase 1 system — [Current News](https://current-news.co.uk/wind-panel-technology-to-pilot-at-edinburgh-airport); [Katrick FAQ / case study (Squarespace)](https://guava-dove-fngh.squarespace.com/faq); [airport case study](https://guava-dove-fngh.squarespace.com/news/airportcasestudy)
- Alpha Stage 1 testing with MTC and University of Strathclyde "exceeds the targets originally set" (dated Feb 2026, no figures); Stage 2 to determine power curve between 5 and 12 m/s — [Energy Manager Magazine, Feb 2026](https://www.energymanagermagazine.co.uk/katrick-technologies-completes-first-testing-milestone); [NA Clean Energy](https://nacleanenergy.com/wind/katrick-technologies-tests-novel-wind-power-system-at-university-of-strathclyde)
- S1 control-system test in Rodez, France, at simulated 4-10 m/s showed "successful energy harvesting" (LinkedIn company claim) — [LinkedIn](https://ro.linkedin.com/in/sorina-baban)
- A 2024 Ansys profile expected a commercial model by mid-to-late 2024 — [Ansys blog](https://ansys.com/blog/katrick-technologies-advances-wind-energy-with-simulation); a claim of 22,000 kWh/yr per panel circulates but is inconsistent with a 1 kW rating — [Balkan Green Energy News (RS)](https://balkangreenenergynews.com/rs/buducnost-energije-vetra-vetroturbine-bez-elisa/)

**DIY oscillating slats/aerofoils**
- The only hobby oscillating-aerofoil build surfaced was the Hackaday 2020 Venetian-blind slat + coil + magnet ("output is tiny") — [Hackaday](https://hackaday.com/2020/06/30/experimenting-with-vibratory-wind-generators)

### Inferences
- Katrick's 41.1 W at 10.2 m/s is ~4% of its 1 kW rating at a wind speed most homes rarely see; at 10.2 m/s the wind carries ~650 W/m2 (my calculation), so unless the panel is well under 1 m2 its conversion efficiency is low. A 22,000 kWh/yr claim implies ~2.5 kW continuous, which a 1 kW-rated panel cannot do.
- An >80% / beyond-Betz claim (Saphonian) is a red flag for any open-flow device; treat as unverified marketing.
- Neither is a home-builder option in Nov 2026; neither has published plans, and hydraulic (Saphonian) or multi-duct (Katrick) mechanics are not hobby-friendly.

### Gaps
- No current (2024-2026) status for Saphon Energy found; no evidence of deployed units.
- No measured Katrick power curve published as of the latest found item (Feb 2026); Edinburgh Airport trial results not found.
- "Wind harps" (Aeolian harps used as generators) and academic "oscillating wing/heaving-pitching aerofoil" harvesters at hobby scale were not covered by the search results; no DIY data found.

---

## 3. Piezoelectric "leaves", Solar Ivy and wind trees: outputs and usefulness

### Takeaway
Piezo-leaf wind harvesters produce picowatts to under a milliwatt per leaf (best: Cornell's ~600 µW peak from one leaf, 2011, lab). Their own developers (Iowa State, 2017) say efficiency is not market-competitive. Commercial "Solar Ivy"/"Energy Tree" concepts never published independent wind-output data. Not useful for home energy; only for sensor-node demos.

### Cited Findings
- Cornell / Northwestern Polytechnical University (Xi'an) "Piezo-Leaf Generator" (J. Applied Physics, 2011): flexible piezo stalks with polymer-film leaves; peak output ~600 µW and max power density ~2 mW/cm3 from a single leaf — [PMC5234829 review citing it](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5234829/); [Peeref record](https://peeref.com/works/11136223)
- Early PVDF-only version made ~100 pW (could not light an LED); adding plastic film to the leaf tip raised power ~100x — [Metropolis "Plastic 'Trees' Generate Energy From Wind"](https://www.metropolismag.com/technology/lab-report-xx/)
- Cornell patent on wind-induced vibration (vs rotation) harvesting: US 8,884,496 "Fluid current energy capture apparatus and method" — [USPTO PDF](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/8884496); [Patsnap](https://eureka.patsnap.com/patent-US8884496B2)
- Other PVDF wind work (cited in a 2025 Cornell rain-harvesting preprint): 0.855 µW from a PVDF leaf model; up to 0.1 mW from a 40 cm2 PVDF surface — [arXiv 2508.11474](https://arxiv.org/html/2508.11474v1)
- Iowa State (2017, PLOS ONE, cottonwood-mimicking tree with piezo leaves): generated electricity in the lab, but the piezo method "didn't achieve the efficiency the technology will need to compete"; won't replace turbines, possible niche for small unobtrusive machines; results "discourage focus on piezoelectric schemes," with triboelectric suggested as more promising; excitation frequency limits output because energy per cycle is small — [PLOS ONE via PMC5234829](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5234829/); [R&D World](https://www.rdworldonline.com/generator-mimics-trees-to-produce-electricity/); [WEF, Feb 2017](https://www.weforum.org/stories/2017/02/generating-electricity-by-taking-a-leaf-out-of-natures-book/); [Power Systems Design](https://www.powersystemsdesign.com/articles/iowa-state-scientists-design-generator-that-mimics-trees/97/11126)
- SMIT "GROW"/Solar Ivy: concept of ivy-like solar+wind fluttering shingles (2008); only critique found was a Make reader comment on durability/UV degradation of polyethylene — [Make: Solar and Wind Leaf shingles (3 Mar 2008)](https://makezine.com/2008/03/03/solar-and-wind-leaf-photo/)
- Solar Botanic "Energy Trees"/"Nanoleaf" are cited as a planned combined wind+solar product; no independent measurements found — [PMC5234829](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5234829/)
- 2009 "piezo tree" concept coverage — [Green Optimistic](https://www.greenoptimistic.com/energy-harvesting-piezo-tree-to-produce-renewable-energy-20091229/); [green-energy-harvesting blog, 2011](https://green-energy-harvesting.blogspot.com/2011/03/energy-harvesting-piezo-tree-concept.html)

### Inferences
- Even at the best lab peak (600 µW/leaf), ~1,700 leaves would be needed for 1 W peak; sustained output in variable wind would be lower. Commercial PVDF film is also far more expensive per watt than coils and magnets.
- For a hobbyist, piezo discs/PVDF strips on a fluttering flag are a fine physics demo (flash an LED after charging a capacitor) but are the worst of the non-VIV options for usable power.

### Gaps
- No DIY piezo-leaf build guide with measured output surfaced in searches.
- No field (outdoor, long-term) output data for any piezo wind tree.

---

## 4. Triboelectric nanogenerator (TENG) wind harvesters: flutter-film TENGs, outputs, DIY feasibility

### Takeaway
Flutter-film TENGs (a plastic film such as FEP/PTFE fluttering between metal electrodes) give hundreds of volts but microamps: typical peak powers 0.1-2.5 mW per palm-sized device, with cut-in as low as ~1.6-3.4 m/s. Materials are cheap and the build is simple (film + foil + frame), so they are DIY-feasible as demos, but output is pulsed high-voltage AC that needs rectification and storage; usable energy is in the µW-mW range. No hobbyist build guides with measured output were found.

### Cited Findings
- Optimized flutter-driven TENG (2021): peak open-circuit voltage 297 V and output power 0.46 mW at 10 m/s; cut-in wind speed 3.4 m/s — [Micromachines via PMC8066174](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8066174/)
- First flutter-driven TENG design: two parallel Al layers and a one-end-fixed FEP film — [PMC8066174](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8066174/)
- Flag-type TENG for self-powered IoT: average power reported as 0.86 mW (search summary) — [PMC9143998](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9143998/)
- Bernoulli-effect TENG (Cell Reports Physical Science, Sep 2020): 175 V, 43 µA, 2.5 mW from a 3 x 8 x 2 cm device; runs from a 1.6 m/s (3.6 mph) breeze; powered 100 LEDs and temperature sensors — [DOAJ record](https://doaj.org/article/1a5c3b53c20148a8ae0610eafe0793ec); [Inverse](https://inverse.com/innovation/micro-energy-invention); [TechXplore, Sep 2020](https://techxplore.com/news/2020-09-tiny-device-scavenge-energy-breeze.amp)
- Omnidirectional weak-wind TENG (Micromachines 2020) with PTFE strips, Al electrodes and NdFeB magnet spacers: 0.64 mW/m2 max power density at 5 MΩ matched load — [PMC7231358](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7231358/); [MDPI PDF](https://mdpi-res.com/d_attachment/micromachines/micromachines-11-00414/article_deploy/micromachines-11-00414-v2.pdf)
- Olsen et al. (2019, Scientific Reports): a 10 cm x 2 cm plastic film fluttering between two copper electrodes lit a string of LEDs; studied frequency/voltage response — [PMC6447574](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6447574/)
- 2014 Nature Communications flag-generator study: flapping in an 8-11 mph breeze generated only a tiny charge — [MWPS world blog](https://www.mwps.world/2014/09/24/flagging-up-the-future-of-wind-power/)
- 2025 J. Mater. Chem. A: fluttering TENG operating at airflow up to 81 m/s — [RSC](https://pubs.rsc.org/en/content/articlelanding/2025/ta/d5ta00649j)
- PolyU work on "boosting power output" of wind TENGs — [PolyU IRA PDF](https://ira.lib.polyu.edu.hk/bitstream/10397/98809/1/Zhang_boosting_power_output.pdf)

### Inferences
- A TENG's few-hundred-volt open-circuit output at µA currents is low-hazard but misleading: a multimeter will under-read, and the energy delivered per day is tiny (e.g. 1 mW for 24 h = 24 mWh, about 0.2% of a phone battery's ~12-15 Wh; my calculation).
- DIY materials (PTFE/FEP film, aluminium tape, acrylic frame, bridge rectifier, capacitor) are cheap and safe, making TENG the easiest "novel" bladeless build to get a measurable result, but output per m2 is no better than a windbelt.
- Many papers report power density in mW/m2 instead of absolute mW, so cross-paper comparisons need care.

### Gaps
- No Instructables/YouTube/Reddit hobby TENG wind build with measured output was found.
- No long-term durability data (film fatigue, humidity sensitivity of triboelectric charge) for outdoor home use found.

---

## 5. Electrostatic / electrohydrodynamic (EWICON, TU Delft): status, feasibility, safety

### Takeaway
EWICON converts wind energy by letting wind blow charged water droplets against an electric field. It got to a 2012-2013 architectural scale model (Mecanoo + TU Delft) displayed on campus since March 2013, with research showing only "positive efficiency." No output figures, commercial product or DIY versions were found; water-pumping losses and the high-voltage system make it impractical and hazardous for home builders.

### Cited Findings
- Principle: wind moves charged particles/droplets against the direction of an electric field, converting kinetic to electrical energy — [Djairam PhD dissertation (TU Delft, 10 Dec 2008), PDF mirror](https://www.eng.uc.edu/~beaucag/Classes/SolarPowerForAfrica/EWICON%20Dissertation%20djairam_20081210.pdf); [TU Delft repository "The Electrostatic Wind Energy Converter"](https://repository.tudelft.nl/record/uuid:e1cfdada-85ea-45c4-b6e4-b798abf5917e)
- The dissertation reports wind energy converted and delivered to an electrical load "with positive efficiency" (no high figure) — [TU Delft repository](https://repository.tudelft.nl/record/uuid:e1cfdada-85ea-45c4-b6e4-b798abf5917e)
- 2011 MSc thesis (A. Winters, supervised by Djairam): self-adjusting multinozzle electrospraying gave "significant improvement" in charging — [TU Delft repository](https://repository.tudelft.nl/record/uuid:81221f03-9d46-4c7c-a5b0-b859a26f7d04)
- Uses electrohydrodynamic atomisation where "a high electric field is used to generate and charge particles simultaneously"; the displayed unit is a scale model — [Designboom](https://www.designboom.com/technology/mecanoo-architects-tu-delft-unveil-a-windmill-without-moving-blades/)
- Mecanoo project page: status "Completed," realisation 2012-2013; prototype on display in front of TU Delft EWI faculty (Mekelpark) since March 2013; designed by Mecanoo with technology from Johan Smit and Dhiradj Djairam — [Mecanoo](https://www.mecanoo.nl/Projects/project/61/Ewicon); [New Atlas](https://newatlas.com/ewicon-bladeless-wind-turbine/26907)
- Water pumping energy is a major issue; might make most sense where rainwater can be collected above turbine height — [Machine Design](https://www.machinedesign.com/archive/wind-power-without-wind-turbines)
- Paul Gipe (2013) "Another Bladeless Windmill Stalks the Mindscape" on EWICON: bladeless windmills are not new (one promoted in 1967; 1970s DOE-funded piezo concept), "it's not here now," and the inventors are seeking money — [wind-works.org](https://wind-works.org/another-bladeless-windmill-stalks-the-mindscape/); CityLab (Apr 2013) reported it would take "a few years, at least" — [CityLab](https://www.citylab.com/life/2013/04/how-long-must-we-wait-bladeless-windmill/5183/)
- 2013 video coverage — [Offshorewind.biz, 3 Apr 2013](https://www.offshorewind.biz/2013/04/03/video-ewicon-e28092-bladeless-windmill)

### Inferences
- More than 13 years after the 2013 demonstrator, no published output figures, follow-on product or spin-off were found, so the concept appears dormant (as of Nov 2026).
- For a home builder, EWICON requires a high-voltage supply, water atomisation, a water supply/pump and charge-collection hardware; the net-energy-positive window is narrow even in the lab, and HV + water + outdoor use is a shock hazard. Not a viable DIY project.

### Gaps
- No kW/W output, operating voltage or measured efficiency figure for the Delft demonstrator found.
- No DIY or hobby EHD wind builds found.

---

## 6. Static ducted / aerofoil designs (Aeromine-style; SheerWind INVELOX): small-scale and DIY replications

### Takeaway
Both contain a rotor, so they are "bladeless" only from the outside. Aeromine (from Sandia/Texas Tech "AeroMINE") uses stationary twin aerofoils to create suction that pulls air past a small internal propeller; Sandia measured ~1/3 of Betz at 1/3 scale and 25% (42% of Betz) at pilot scale, and noted small units perform worse because of internal friction. Commercial units are 5 kW, 1,000+ lb rooftop machines, not home-scale. INVELOX (a funnel feeding a ground turbine) went bankrupt in Dec 2017. No DIY replications of either were found.

### Cited Findings
**Aeromine / AeroMINE**
- Origin: Sandia publication "Aero-MINE (Motionless Integrated Energy) for distributed scalable wind power" (1 Jun 2017) — [Sandia](https://sandia.gov/research/publications/details/aero-mine-motionless-integrated-energy-for-distributed-scalable-wind-power-2017-06-01); "A novel energy-conversion device for wind and hydrokinetic applications" (2019) — [Sandia](https://www.sandia.gov/research/publications/details/a-novel-energy-conversion-device-for-wind-and-hydrokinetic-applications-2019-07-01/); [Texas Tech](https://www.depts.ttu.edu/renewableenergy/Publications/publish64.php)
- Mechanism: two external vertical aerofoils create low pressure, which drives an internal flow through an internal propeller ("the only moving part") driving a sealed PM generator; research design places the turbine-generator at ground level — [Engineers Ireland](https://www.engineersireland.ie/Engineers-Journal/Civil/revealed-the-motionless-wind-turbine-that-doesnt-need-a-blade); [New Atlas (BMW)](https://newatlas.com/energy/aeromine-turbine-bmw/); [EE Power](https://eepower.com/market-insights/aeromine-an-elegantly-simple-rooftop-wind-energy-solution/)
- Readers disputed the "motionless" label, noting a visible spinning turbine underneath; GlobalSpec's own description mentions a propeller — [pv magazine USA, 14 Oct 2022](https://pv-magazine-usa.com/2022/10/14/rooftop-wind-energy-innovation-claims-50-more-energy-than-solar-at-same-cost); [GlobalSpec](https://insights.globalspec.com/article/22509/insights.globalspec.com/help/privacy)
- Sandia efficiencies: 1/3-scale wind tunnel ~1/3 of Betz after optimizing foil spacing, angle of attack and jets (~18% stable); pilot scale 25% (42% of Betz) at >9 m/s with max jet area; "frictional effects of the internal flow are not fully self-similar with scale," so efficiency rises with size; >half-Betz is a projection — [OSTI 1643486](https://www.osti.gov/servlets/purl/1643486); [OSTI 2001645](https://www.osti.gov/servlets/purl/2001645); [Sandia "Performance of AeroMINEs for distributed wind energy" (2020)](https://sandia.gov/research/publications/details/performance-of-aeromines-for-distributed-wind-energy-2020-01-01)
- Commercial unit: 5 kW AC, just over 1,000 lb, withstands 120 mph; typical install 10+ units (50 kW) or 20-40 units on a roof edge; 10 units estimated ~20,000 kWh/yr at 16 ft roof and 4.5 m/s average wind, >150,000 kWh/yr at 50 ft and 8 m/s — [pv magazine, 24 May 2024](https://www.pv-magazine.com/2024/05/24/bladeless-wind-energy-innovation-aims-to-compete-with-rooftop-solar); [BD+C](https://www.bdcnetwork.com/sustainability/news/55165330/a-wind-energy-systemwithout-the-bladescan-be-placed-on-commercial-building-rooftops); [Freethink](https://www.freethink.com/energy/rooftop-wind-energy)
- Conflicting spec: Motor1 says 50 kW per turbine, 450 kg, 47 mph — likely a mix-up — [Motor1](https://www.motor1.com/news/721800/aeromine-wind-turbine-without-blades/about:blank)
- Company claim: ~50% more energy than rooftop solar at the same cost (unverified) — [pv magazine USA](https://pv-magazine-usa.com/2022/10/14/rooftop-wind-energy-innovation-claims-50-more-energy-than-solar-at-same-cost); works best where wind comes from a fairly steady direction — [Interesting Engineering](https://interestingengineering.com/innovation/groundbreaking-motionless-wind-turbine)
- UK's first unit installed at BMW's MINI plant, Oxford, alongside an 11,000-panel solar array — [Euronews, 5 Sep 2024](https://www.euronews.com/green/2024/09/05/could-these-motionless-turbines-solve-wind-energys-noise-and-wildlife-problems)
- Company expected European/North American commercial launch in 2025; a 2026 Houston listing repeats "as much power as 16 rooftop solar panels" per unit — [pv magazine India](https://www.pv-magazine-india.com/2024/05/28/bladeless-wind-energy-innovation-aims-to-compete-with-rooftop-solar/); [InnovationMap Houston](https://houston.innovationmap.com/tag/david-asarnow)

**SheerWind INVELOX**
- Funnel/ducted concentrator feeding a turbine; company claimed 80-560% more energy than conventional turbines; critique "All Hype, No Substance" (Mike Barnard, 8 Jul 2014) noted a couple of million dollars in grants/investment with two small prototypes — [CleanTechnica](https://cleantechnica.com/2014/07/08/invelox-ducted-turbine-latest-long-line-failures/)
- Gipe: SheerWind's "field data" page "shows nothing that makes any sense"; none of the 14 turbines that applied for US certification were SheerWind; Chapter 7 bankruptcy filed 29 Dec 2017 with zero assets and US$3.7 million liabilities — [wind-works.org "Another Ducted Device Dead"](https://wind-works.org/another-ducted-device-dead-sheerwind-invelox-bankrupt/); [wind-works.org "Is the End Nigh"](https://wind-works.org/sheerwind-invelox-is-the-end-nigh-for-another-ducted-turbine/); [demo turbine "in need of demolition"](https://wind-works.org/sheerwind-invelox-demo-turbine-in-need-of-demolition/)

### Inferences
- Sandia's own scale finding (efficiency falls as size shrinks because internal friction does not scale) means a desk- or 1-2 m DIY "Aeromine" would probably do worse than the ~18% they got at 1/3 scale, and a simple small HAWT of the same size would likely beat it.
- Gipe's book Wind Energy for the Rest of Us (2016) targets ducted turbines as a "sacred cow" — [Windtech International review](https://www.windtech-international.com/bookreview/book-review-wind-energy-for-the-rest-of-us); ducts add structure and cost without adding energy beyond what a rotor of the same overall frontal area could capture (standard ducted-turbine critique; Gipe's specific argument text not fetched).

### Gaps
- No DIY/maker replications of AeroMINE or INVELOX (Instructables, YouTube, Hackaday.io) found.
- No independent field data on commercial Aeromine units; 2025-2026 sales/price status unconfirmed.
- No Gipe article specifically on Aeromine found.

---

## 7. "Wind Tree" / Arbre à Vent / Aeroleaf (NewWind, France): bladed, not bladeless

### Takeaway
The Arbre à Vent is a steel "tree" whose "leaves" (Aeroleafs) are small spinning rotors with generators, so it is a cluster of micro wind turbines, not a bladeless device. NewWind went into receivership on 14 Dec 2016 and was liquidated on 8 Mar 2017; a successor (New World Wind) took the assets. Output was modest: ~2,400 kWh/yr from a 4.1 kW, 63-leaf, 10 m tree (a ~7% capacity factor).

### Cited Findings
- NewWind was put into court-supervised restructuring on 14 Dec 2016 and liquidated on 8 Mar 2017 by the Saint-Brieuc commercial court — [Le Journal des Entreprises "Clap de fin pour l'arbre à vent"](https://www.lejournaldesentreprises.com/article/clap-de-fin-pour-larbre-vent-de-newwind-94670); earlier critique "le fiasco prévisible de l'arbre à vent" — [Le Journal des Entreprises](https://www.lejournaldesentreprises.com/article/le-fiasco-previsible-de-larbre-vent-9547)
- INPI profile: Arbre à Vent yields 1,000-3,000 kWh/yr depending on wind — [INPI](https://www.inpi.fr/newwind-un-vent-nouveau-sur-l-eolien)
- 10 m tree with 63 Aeroleafs: 4.1 kW installed, ~2,400 kWh/yr; listed under "rotor magnet assembly technology" — [Energy-XPRT](https://www.energy-xprt.com/products/rotor-magnet-assembly-technology-524579)
- Successor New World Wind acquired the assets; its WindTree catalogue lists 300 W per Aeroleaf and 36 leaves per tree; a newer ~1,000 W generator with two Aeroleafs head-up/head-down — [DirectIndustry catalogue](https://pdf.directindustry.com/pdf/new-world-wind/wind-tree/244907-1009296.html); [ArchiExpo project](https://trends.archiexpo.com/new-world-wind/project-190955-288888.html); [BusinessCoot (New World Wind, turnover €385k, 2018)](https://businesscoot.com/en/company/new-world-wind)

### Inferences
- 2,400 kWh / (4.1 kW x 8,760 h) = ~6.7% capacity factor (my calculation), typical of low-mounted, turbulent-site micro-turbines; it is a sculpture-grade product, not a bladeless innovation.
- Any "wind tree" a hobbyist builds from small VAWT rotors is ordinary small wind, subject to the same rooftop/low-height penalties.

### Gaps
- Whether New World Wind is still trading as of Nov 2026 not confirmed.
- Exact Aeroleaf rotor geometry (Savonius vs other VAWT type) not confirmed from a primary source.

---

## 8. Overall: which non-VIV approach gives the most usable power per unit of hobbyist effort, and what do independent experts say?

### Takeaway
For a home builder, none of these produce meaningful household power. Ranked by usable output per unit effort: (1) electromagnetic flutter belt (Windbelt-style), mW to tens of mW from a ~1 m belt, cheap and well documented; (2) flutter-film TENG, sub-mW to few mW, cheapest materials but awkward HV/µA output; (3) piezo leaves, µW to sub-mW, expensive film; then (4) EWICON, Saphonian-style hydraulics, Katrick-style ducted oscillators, which are not feasible DIY. Ducted "motionless" designs (Aeromine, INVELOX) hide a rotor and lose efficiency at small scale. Independent voices (Paul Gipe, CleanTechnica's Mike Barnard, Hackaday writers) consistently say bladeless concepts are recurring hype with low energy capture, and none appear in small-wind certification lists. A ~$30 DIY bladed micro-turbine (~1 W at 20 mph) outperforms every bladeless option here by 1-3 orders of magnitude.

### Cited Findings
- Gipe: bladeless windmills are an old idea that keeps resurfacing (1967 design; 1970s DOE-funded piezo concept); 2013 critique of EWICON; in 2015 he said everything in that piece applied to Vortex Bladeless too — [wind-works.org "Another Bladeless Windmill Stalks the Mindscape"](https://wind-works.org/another-bladeless-windmill-stalks-the-mindscape/); [wind-works.org "Oh no, not them again: bladeless wind turbines are back"](https://wind-works.org/oh-no-not-them-again-bladeless-wind-turbines-are-back/)
- Gipe maintains a page of "Inventions & Questionable Turbines" on wind-works.org — [wind-works.org](https://wind-works.org/wind/small-wind/questionable-concepts/); he also debunked Honeywell WindTronics rooftop turbines — [wind-works.org](https://wind-works.org/?p=3763)
- Gipe noted none of the 14 turbines applying for US small-wind certification at that time were SheerWind (ducted) — [wind-works.org](https://wind-works.org/another-ducted-device-dead-sheerwind-invelox-bankrupt/)
- CleanTechnica (21 May 2015) "Bladeless Wind Turbine — Reality Check": oscillators don't sweep an area, so material scales roughly linearly with intercepted wind; cost claims based on small prototypes; resonance needs steady wind but small-wind sites are turbulent — [CleanTechnica](https://cleantechnica.com/2015/05/21/bladeless-wind-turbine-reality-check/)
- Hackaday (2020): a mechanical micro-generator would need 100K+ hours unattended operation to beat a battery for sensor power — [Hackaday](https://hackaday.com/2020/06/30/experimenting-with-vibratory-wind-generators)
- Iowa State researchers: piezo leaves won't replace turbines; triboelectric may be more promising — [PMC5234829](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5234829/)
- Flutter devices "almost all have efficiencies below turbine machines" — [Wikipedia: Windbelt (search summary)](https://en.wikipedia.org/wiki/Windbelt)
- DIY bladed comparison: Make: Chispito ~1 W (147 mA at 6.7 V) at ~20 mph — [Make:](https://makezine.com/projects/backyard-wind-power/)
- Summary of measured outputs found (for a comparison table):
  - Windbelt microWindbelt 0.2 mW @ 3.5 m/s; 5 mW @ 7.5 m/s — [Wikipedia](https://en.wikipedia.org/wiki/Windbelt)
  - microBelt 2 mW @ 5.5 m/s — [IDTechEx](https://www.offgridenergyindependence.com/articles/2146/wind-energy-harvester-from-humdinger)
  - ~1 m Windbelt 40 mW @ 4.5 m/s (claim) — [cleanergy/PM](https://cleanergy.blogspot.com/2008/03/innovative-low-cost-windbelt-could.html)
  - Optimized academic wind belt 81 mW @ 6 m/s — [CAS record](https://katalog.lib.cas.cz/KNAV/EdsRecord/edsair,edsair.doi...........7e8024f083f2d4fb3c9cf088cc770155)
  - DIY Windbelt Redux ~1.5 V AC / 20 mA short circuit — [Instructables](https://www.instructables.com/Windbelt-Redux--21st-Century-Micro-Power-Generatio)
  - Cornell piezo leaf ~600 µW peak/leaf — [PMC5234829](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5234829/)
  - Flutter TENG 0.46 mW @ 10 m/s; Bernoulli TENG 2.5 mW — [PMC8066174](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8066174/); [Inverse](https://inverse.com/innovation/micro-energy-invention)
  - Katrick Wind Panel 41.1 W avg @ 10.2 m/s (company) — [Wind Systems Mag](https://www.windsystemsmag.com/?p=30920)
  - Aeromine 5 kW per (~1,000 lb) unit (company rating) — [pv magazine](https://www.pv-magazine.com/2024/05/24/bladeless-wind-energy-innovation-aims-to-compete-with-rooftop-solar)
  - EWICON: no figure ("positive efficiency") — [TU Delft](https://repository.tudelft.nl/record/uuid:e1cfdada-85ea-45c4-b6e4-b798abf5917e)

### Inferences
- Best "power per effort" non-VIV bladeless build for a hobbyist: an electromagnetic flutter belt (1 m polymer ribbon or VHS/cassette tape, NdFeB magnets, two hand-wound or salvaged coils, rectifier + supercapacitor). Expect a few mW to a few tens of mW in 4-6 m/s steady wind, enough to blink LEDs or trickle a low-power sensor node. Tension tuning dominates performance (per DIY and KidWind manuals).
- Scaling up does not rescue it: even the projected 1 m2 Windcell Panel (~10 W average at 6 m/s per Wikipedia's projection) would be under 8% of the ~132 W/m2 in that wind (my calculation), and that panel never shipped.
- Expert consensus (Gipe, Barnard, Hackaday writers, the piezo researchers themselves) points the same way: bladeless non-VIV approaches are educational or IoT-niche technologies, not domestic energy sources. A hobbyist wanting watts should build a conventional small HAWT, or simply buy a small solar panel.
- None of these devices appears to hold small-wind certification (e.g. under IEC 61400-2 / SWCC / MCS); see gap below.

### Gaps
- No small-wind certification body (SWCC, MCS, IEC 61400-2 listing) statement specifically on Windbelt, TENG, piezo, EWICON, Saphonian, Katrick or Aeromine was found; absence from lists is inferred, not documented by a cited source.
- No Gipe article specifically on the Windbelt was found (searches of wind-works.org returned nothing on it).
- Reddit / FieldLines threads on DIY windbelts or TENGs did not surface in searches; YouTube DIY videos with measured power curves were not identifiable from snippets.
- Several primary pages could not be fetched (hackaday.com, pmc.ncbi.nlm.nih.gov, energymanagermagazine.co.uk, vernier.com: ENOTFOUND in this session); figures from those are from search snippets.
