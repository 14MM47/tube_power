# DIY and maker-community builds of small bladeless (VIV / oscillating-mast) wind turbines

Research date: 16 Nov 2026. Method note: WebFetch failed with ENOTFOUND for almost every primary page tried (instructables.com, hackaday.com, physicsforums.com, engineering.txst.edu, digital.wpi.edu, irjmets.com, kscst.org.in, abstracts.societyforscience.org, forum.allaboutcircuits.com). The WebSearch tool also refuses reddit.com. Nearly all findings below therefore come from search-result snippets and summaries, not full-page reads. Treat specific numbers as snippet-level evidence. The URLs are recorded so they can be cited or checked later.

Overall picture: the maker ecosystem for home-built VIV ("Vortex Bladeless-style") generators is very thin. I found no step-by-step Instructables, Thingiverse, Printables or GitHub build of a VIV wind generator, and no YouTube build that documents real power measurements. The most useful hands-on material is (a) a few hobbyist proof-of-concept demos, such as Robert Murray-Smith's speaker-coil and blind-slat vibrators covered by Hackaday in 2020, (b) university senior-design and school science-fair projects, and (c) generic energy-harvesting electronics. Where measured, output is in the microwatt to low-milliwatt range.

---

## 1. Build guides on maker sites (Instructables, Hackaday, Thingiverse/Printables, GitHub, Make:, Hackster)

### Takeaway
No maker site turned up a complete, replicable build guide for a VIV / oscillating-mast wind generator. The closest items are a 2020 Hackaday write-up of Robert Murray-Smith's crude vibrating-stick generators ("tiny" output), a Hackaday.io oscillating-film electrostatic generator (flutter, not VIV), and project-idea pages with no results. Windbelt (flutter) guides do exist on Instructables and Make:.

### Cited Findings
**Hackaday blog**
- Hackaday, 30 June 2020, "Experimenting with vibratory wind generators": Robert Murray-Smith generated electrical power from wind "without any moving parts" (no rotating parts) using two devices. Device 1: the cone of a standard loudspeaker was cut out and a flat stick glued to the voice coil. As the stick vibrates in the wind, the coil moves in the magnet's field and produces a voltage. Device 2: a window-blind slat replaces the speaker parts, and the slat's oscillation moves a magnet relative to a coil. The article calls the output "tiny, of course" and the speaker version "a proof of concept" that "isn't terribly elegant." No wind speed or wattage was found in the snippet. — [Hackaday 2020](https://hackaday.com/2020/06/30/experimenting-with-vibratory-wind-generators) (full page not fetchable; details via search summary)

**Hackaday.io**
- "Flexible circuit wind generator" (FLAG, Flexible Linear Aeroelectrostatic Generator): built from polyester film. "When exposed to the wind, the generator oscillates, and the relative motion of the conductive areas extracts work from the wind." Submitted to the 2021 Hackaday Prize. This is an oscillating/flutter electrostatic device, not a VIV mast. — [Hackaday.io project 181882](https://hackaday.io/project/181882-flexible-circuit-wind-generator)
- Other wind projects on Hackaday.io found by the same search are conventional rotors, not bladeless: "Simple VAWT wind power generator" (coils + magnets), "VentolONE challenge" (small VAWT; its "Vortex one" is a reed-switch anemometer, not a vortex-shedding device), "Mini Vertical Wind Generator 3D printed", "3D printed portable wind turbine", "Bi-Generator vertical wind turbine". — [Hackaday.io search results: 164870](https://hackaday.io/project/164870-simple-vawt-wind-power-generator/), [11967](https://hackaday.io/project/11967-the-ventolone-challenge-beyond), [87345](https://hackaday.io/project/87345-mini-vertical-wind-generator-3d-printed), [185070](https://hackaday.io/project/185070-3d-printed-portable-wind-turbine), [191729](https://hackaday.io/project/191729-bi-generator-vertical-wind-turbine)
- Hackaday.io "Inside out wind turbine" (project 206229) is described as "a physics demonstrator, not a power plant — output is single-digit milliwatts". It is not identified as a bladeless/VIV device. — [Hackaday.io 206229](https://hackaday.io/project/206229-inside-out-wind-turbine)

**Instructables**
- Searches for "Instructables bladeless wind turbine" returned no Instructables VIV-generator guide. The site's "bladeless" content is a bladeless *fan* ("How to Make a Bladeless Fan – DIY Homemade Silent Fan", tied to the Fixitsamo YouTube channel), which is a trap for searchers and is not a generator. — [Instructables bladeless fan](https://www.instructables.com/How-to-Make-a-Bladeless-Fan-DIY-Homemade-Silent-Fa)
- Windbelt (flutter) guides (brief; flutter is covered by another researcher): "How to Build Cheap VHS Tape WINDBELT Generator" (a micro Windbelt described as having "limited output capacity", no wattage given) and "Windbelt Redux – 21st Century Micro Power Generation" (a second iteration of Shawn Frayne's design, "designed to utilise cross ventilation in a house"; no output numbers in snippet). — [Instructables VHS Windbelt](https://www.instructables.com/HOW-TO-build-cheap-VHS-tape-WINDBELT-generator); [Instructables Windbelt Redux](https://www.instructables.com/Windbelt-Redux--21st-Century-Micro-Power-Generatio)
- Context from a conventional KidWind Instructable: you need "about 1.8 volts" to light an LED Christmas bulb, and a non-geared model turbine produces "between 0.5 – 2.5 volts". This is a useful benchmark for what a small DIY generator must reach to light an LED. — [Instructables KidWind Model Wind Turbine](https://www.instructables.com/Model-Wind-Turbine-KidWind-Project/)

**Make: magazine**
- Make: covered the Windbelt in a 20 Oct 2007 post ("Windbelt – elegant non-turbine wi[nd generator]"). No Make: article on a VIV/oscillating-mast build was found. — [Make: 2007](https://makezine.com/2007/10/20/windbelt-elegant-nonturbine-wi/)

**Thingiverse / Printables / GitHub / Hackster**
- Searches aimed at Thingiverse, Printables and GitHub returned only patents and academic papers, with no printable mast or base designs and no code repositories for VIV wind harvesting. Hackster.io results were conventional vertical-axis turbines. — [Hackster VAWT example](https://www.hackster.io/Newphysicist/making-a-wind-turbine-project-vertical-axis-diy-39e095)

**Other "maker-adjacent" pages**
- Skyfi Labs (Indian student-project vendor) has "project idea" pages for vortex bladeless turbines. One concept uses a hollow tower with magnets, an alternator and wires, and another uses a rigid base. These are idea listings with no build results, and they repeat marketing claims such as "40% cheaper". — [Skyfi Labs: Vortex type bladeless windmill](https://www.skyfilabs.com/project-ideas/vortex-type-bladeless-windmill); [Skyfi Labs: Vortex Bladeless Turbines](https://www.skyfilabs.com/project-ideas/vortex-bladeless-turbines)
- SimScale public CFD project "VIP Vortex Bladeless Design" by user mdiep: a simulation model with no recorded results. — [SimScale](https://www.simscale.com/projects/mdiep/vip_vortex_bladeless_design/)
- homemadetools.net forum thread "Bladeless wind turbine – GIF" exists, but its build content was not visible in snippets. — [homemadetools.net](https://homemadetools.net/forum/bladeless-wind-turbine-gif-88869)
- A LEGO "Bladeless Turbine Generator Build" by Jamie's Brick Jams is a Tesla-style disc turbine, a different "bladeless" concept that is not VIV. — [TechEBlog](https://www.techeblog.com/?p=237591)

### Inferences
- The word "bladeless" is heavily overloaded in maker spaces. It is used for Dyson-style fans, Tesla disc turbines, and mislabelled VAWTs. A builder searching for VIV designs has to filter these out.
- The only hobbyist pattern with a documented working result (Murray-Smith) is the "flexible reed + moving voice coil/magnet" approach, which is closer to a flutter or galloping harvester than to a tuned VIV mast.

### Gaps
- Could not open Instructables or Hackaday pages directly to check whether any lesser-known Instructables VIV builds exist, or to read Hackaday comment threads.
- No Thingiverse, Printables or GitHub designs were found. It is unclear whether none exist or whether search coverage was poor.
- Could not locate the original Robert Murray-Smith YouTube video title or date, or any voltage/power figure for his devices.

---

## 2. Notable YouTube builds

### Takeaway
YouTube search turned up only explainers (mostly of the commercial Vortex Bladeless prototype), one academic pendulum-generator demo, a clickbait "$60 bladeless device" video, and basic magnet-coil demos. No YouTube home build of a VIV mast with measured watts, or even reliable LED-lighting results, was found.

### Cited Findings
- Vortex Bladeless official channel, plus explainer videos: "Vortex Bladeless How it Works, scheme (2020)"; "This is the Cheapest and Quietest Wind Turbine – Vortex Bladeless"; "No blades! A pole-shaped wind turbine, Vortex Bladeless, generates power by shaking"; "A wind turbine without blades?"; "Bladeless wind turbines"; plus a Shorts clip "How these Vortex Bladeless makes electricity by shaking". These are explainers or company footage, not builds. — [Vortex Bladeless channel](https://www.youtube.com/channel/UCVIBk9xcmPDnsh2hTJpD6pA); [How it Works 2020](https://www.youtube.com/watch?v=lirOhO4nKIc); [Cheapest and Quietest](https://www.youtube.com/watch?v=CV15JSVg_xU); [No blades!](https://www.youtube.com/watch?v=VrEKrx4CdyU); [A wind turbine without blades?](https://www.youtube.com/watch?v=qb6NWB5Hb4A); [Bladeless wind turbines](https://www.youtube.com/watch?v=QS2e-vLa-T8); [Short](https://www.youtube.com/shorts/rfkXIF4_iyM)
- "Design of a Vortex Bladeless Wind Generator with an Arc-shaped Pendulum" (YouTube). Its title matches a 2017 IEEE ICSEng paper by Ladaran, Cabana, Orilla, Bacasnot, Martinez, Teresa and Salvador, "Design and Construction of Arc Shaped and Disc Shaped Pendulum for Vortex Bladeless Wind Generator". In that design, permanent magnets on a pendulum at the mast base act "as a piston", with stator coils of 2,200 turns each on the sides of the pendulum. The arc-shaped pendulum showed "a significant increase of voltage" over the disc shape. The authors note it was small-scale. An MDPI Energies review suggests the arc magnet's higher output may simply be because it was larger. — [YouTube](https://www.youtube.com/watch?v=MbSjUa_6FNc); [paper record](https://katalog.lib.cas.cz/KNAV/EdsRecord/edsair,edsair.doi...........c9c958c3f97bd2ea3ff3aafbb98e1c3c); [MDPI Energies 15(18):6773](https://mdpi.com/1996-1073/15/18/6773)
- "Forget Wind Turbines — This $60 Bladeless Device Generates Free Power 24/7". The title is in clickbait style ("free power 24/7"), and nothing about it could be verified. — [YouTube](https://www.youtube.com/watch?v=3wyupCvhPic)
- "Magnetic Oscillator": a strong neodymium magnet, a 400-turn insulated copper coil and an old plastic syringe. It demonstrates the linear magnet-coil generator principle a DIY mast base would use, but it is not a wind build. — [YouTube](https://www.youtube.com/watch?v=i0h8sZFFSbI)
- Searches for "vortex bladeless DIY … magnet coil" also return "free energy" vortex-math coil videos (e.g., "Vortex Tech Replication. Frame and Coil Build, by netica"; "Holmstrom Heptacontakaidigram Free Energy Coil"). These are unrelated pseudoscience. — [netica](https://www.youtube.com/watch?v=9kqN7ihsOyM); [Holmstrom coil](https://www.youtube.com/watch?v=r5eKJ_G1MTA)
- Searches for "bladeless windmill project … working model" on YouTube return only conventional bladed school-science models. — [example](https://www.youtube.com/watch?v=cFvuwMyzviQ)
- A Spanish-language search ("turbina eólica sin aspas casera") returned only news coverage of Vortex Bladeless (e.g., an elastic rod plus coils and magnets, Spanish patent ES2374233B1, company prototypes up to 6 m tall), with no home-build instructions. — [madrimasd](https://www.madrimasd.org/blogs/patentesymarcas/2021/aerogeneradores-sin-palas-eolica-2-0-con-vortex-bladeless/); [ecoinventos](https://ecoinventos.com/proyecto-vortex/)

### Inferences
- The search results contain no high-profile YouTube maker build of a VIV mast (e.g., from a large engineering channel) with real power measurements. If such a build exists, it is not prominent. The best-documented hobbyist "bladeless" wind demo found is Murray-Smith's (via Hackaday), which reports "tiny" output.
- Clickbait "free power 24/7" bladeless videos should be flagged to the user as unreliable.

### Gaps
- Could not query YouTube directly or read video descriptions or comments. Channel names, upload years and any measured outputs for most hits are unknown.
- No video was found that reports milliwatt or watt measurements under a stated wind speed for a home VIV build.

---

## 3. Forum discussions and practical lessons / skepticism

### Takeaway
Forum discussion is mostly a reaction to Vortex Bladeless press coverage (2015 and 2021), not DIY build logs. Experienced commenters stress that the device only works in a narrow wind-speed/Reynolds range, that it needs steady wind, that the "30% less energy" claim is implausible, and that scaling is poor. Reddit, FieldLines/otherpower and Stack Exchange could not be reached or returned nothing.

### Cited Findings
- **Physics Forums**, "New Bladeless Design for Wind Energy" (thread 814428, c. 2015, inferred from the thread's subject, the 2015 Vortex reveal). Commenters note the device seems to rely on vortex shedding "to keep it wiggling" and question the narrow Reynolds-number range this implies. They point out the company doesn't "even have a one kW prototype demonstrated in a on field test". One reply on page 2: "I am not sure the claim they 'only' capture 30% less energy than a bladed turbine is plausible." A summary attributes to the thread the view that a realistic figure "might be closer to 10% of a regular turbine on a good day". — [Physics Forums p1](https://physicsforums.com/threads/new-bladeless-design-for-wind-energy.814428); [p2](https://www.physicsforums.com/threads/new-bladeless-design-for-wind-energy.814428/page-2); [post](https://www.physicsforums.com/threads/new-bladeless-design-for-wind-energy.814428/post-5122031)
- **All About Circuits**, "Bladeless wind turbines a hoax?" (thread 129771). A skeptic estimate surfaced alongside this thread: even if it performed as claimed, a ~4 kW unit would need ~500 units "to replace a single 2 megawatt (or 2,000 watt) conventional wind turbine". The "(2,000 watt)" is an error in the original, since 2 MW = 2,000 kW. Attribution is from a search summary and was not verified on the page. — [AAC thread](https://forum.allaboutcircuits.com/threads/bladeless-wind-turbines-a-hoax.129771/post-1065442); [AAC post 2](https://forum.allaboutcircuits.com/threads/bladeless-wind-turbines-a-hoax.129771/post-1066437)
- **All About Circuits**, "Small wind generator for couple hundred milliWatts" (thread 147068): a builder targeting about 200 mW output at about 5 mph, a useful real-world sizing reference for micro-wind. It is not a bladeless build. — [AAC thread](https://forum.allaboutcircuits.com/threads/small-wind-generator-for-couple-hundred-milliwatts.147068/post-1252509)
- **Permies**, "bladeless wind turbine" (thread 58130): the poster calls them easy to build, not very expensive and low maintenance, and asks "How much power can it produce?". No answer was visible in the snippet. — [Permies](https://permies.com/t/58130/bladeless-wind-turbine)
- **Endless Sphere**, "Savonius rotor (generator)" thread, page 2 (2015): Vortex Bladeless is mentioned only in passing, via a Wired article. No build. — [Endless Sphere](https://endless-sphere.com/sphere/threads/savonius-rotor-generator.62084/page-2)
- **Reddit**: the search tool refuses reddit.com. Secondhand: the Guardian (Mar 2021) reported that a Reddit post on Vortex drew "more than 94,000 ratings and 3,500 comments" and the nickname "skybrator". There is also an r/nextfuckinglevel "vibrating wind turbine" thread (via a libreddit mirror). No Reddit DIY build was identified. — [Guardian via PressReader](https://www.pressreader.com/usa/the-guardian-usa/20210317/281947430611337); [libreddit mirror](https://libreddit.winscloud.net/r/nextfuckinglevel/comments/ljohrf/vibrating_wind_turbine/gng8y70/?context=3)
- **Expert/blog skepticism** often cited in forums:
  - CleanTechnica (Michael Barnard, 21 May 2015) "Bladeless Wind Turbine — Reality Check": the design is impractical, "won't scale to anything useful economically", and resonance depends on relatively stable winds, a problem at turbulent sites. Earlier concepts (Windstalk, Saphonian) "went nowhere". — [CleanTechnica](https://cleantechnica.com/2015/05/21/bladeless-wind-turbine-reality-check/)
  - Wind-Works (Paul Gipe), "Oh no, not them again: bladeless wind turbines are back": the company has not published its performance measurements. — [Wind-Works](https://wind-works.org/oh-no-not-them-again-bladeless-wind-turbines-are-back/)
- **FieldLines/otherpower, Electronics/Engineering Stack Exchange**: domain-restricted searches returned no relevant threads. — (no source; see Gaps)

### Inferences
- The practical lessons from experienced wind builders amount to the following. VIV only produces useful motion near lock-in, so output is concentrated in a narrow wind band. Real gusty home sites make this worse. Swept-area physics means a small mast captures very little energy compared with an equivalent small rotor.
- A hobbyist forum culture of logged builds with measurements (as exists for axial-flux rotor builds on FieldLines) does not seem to exist for VIV masts.

### Gaps
- Could not read Reddit (r/DIY, r/windpower, r/AskEngineers, r/RenewableEnergy, r/engineering) directly.
- No FieldLines/otherpower threads surfaced. It is unknown whether that community has discussed or tested VIV masts.
- Stack Exchange answers on VIV generator design were not found.

---

## 4. Kits, educational kits and components

### Takeaway
No bladeless/VIV wind kit (hobby or educational) was found for sale. "Bladeless" listings on Alibaba/Accio are mislabelled vertical-axis or "maglev" rotor turbines. Relevant buildable parts are generic. Energy-harvesting electronics such as the SparkFun LTC3588 piezo harvester breakout (US$41.50) are the most concrete. Conventional STEM wind kits contain magnet/coil AC generators. A Windbelt (Humdinger, via KidWind/Vernier) exists as a flutter teaching kit.

### Cited Findings
- **Alibaba / Accio "bladeless" listings are not VIV devices.** Examples: a 300 W "vertical bladeless" unit at US$420–462; a 1000 W "magnetic levitation" model at US$538–550 (MOQ 2); a 500 W unit at US$170–190 (MOQ 50); "Vortex Bladeless Wind Turbine – 1200W Home Generator" showroom; one listing at an implausible US$0.50. These are rotor turbines or placeholders using the "bladeless/vortex" name. — [Alibaba vertical bladeless](https://www.alibaba.com/showroom/vertical-bladeless-wind-turbine.html); [Alibaba bladeless](https://www.alibaba.com/showroom/bladeless-wind-turbine.html); [Alibaba "vortex bladeless 1200W"](https://www.alibaba.com/showroom/vortex-bladeless-turbine.html); [Accio](https://www.accio.com/plp/bladeless-wind-turbine-price)
- **SparkFun Energy Harvester Breakout – LTC3588 (BOB-09946)**: US$41.50 retail (US$35.28 at 100+), stock status unclear. Other sellers: Proto-Pic £33.00; Robot Italy €29.40; Core Electronics AUD 67.90; Little Bird AUD 83.95. The LTC3588 rectifies and regulates low-power piezo/vibration sources, which makes it suitable for a piezo-based mini mast. — [SparkFun](https://www.sparkfun.com/sparkfun-energy-harvester-breakout-ltc3588.html); [Proto-Pic](https://proto-pic.co.uk/product/energy-harvester---ltc3588-breakout--bob-09946-); [Robot Italy](https://robot-italy.com/en/products/energy-harvester-ltc3588-breakout); [Core Electronics](https://core-electronics.com.au/energy-harvester-ltc3588-breakout.html.md); [Little Bird](https://littlebirdelectronics.com.au/products/sparkfun-energy-harvester-breakout-ltc3588)
- **Conventional STEM wind kits (bladed), possible parts donors**: STEMfinity PicoSolutions Vertical Wind Turbine 2.0 from US$24.99 (powers an LED, piezo buzzer or multimeter). Wards Science PicoSolutions Vertical Wind Turbine Plus Kit US$82.89 (includes an AC generator "with magnets and coils"). Wards bundles cost US$253.89–355.89. — [STEMfinity](https://stemfinity.com/collections/all/products/picosolutions-vertical-wind-turbine-2-0); [Wards Science](https://www.wardsci.com/us/en/product/46165355/picosolutions-vertical-wind-turbine-plus-kit)
- **Windbelt teaching kit (flutter, brief)**: the KidWind Humdinger Windbelt manual (hosted by Vernier) notes that a belt vibrating at higher frequency produces higher voltage, and that the classic model "will only work well with a powerful fan". — [Humdinger Windbelt manual (Vernier/KidWind)](https://www.vernier.com/files/kidwind/humdinger_windbelt_manual.pdf)
- **Linear vibration generators**: searches for AliExpress/Amazon linear generator or vibration harvester kits returned only patents. Benchmarks from those patents: one design gave a peak of 9 mW at 6 Hz vibration, and another gave 76 µW at 0.04 g. Harvesters are typically tuned to below 10 Hz. — [US 8957558 Linear vibration generator](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/8957558); [US 9041230](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/9041230)
- A "Magnetic Oscillator" demo shows a DIY linear generator: a neodymium magnet sliding in a plastic syringe inside a 400-turn coil. — [YouTube](https://www.youtube.com/watch?v=i0h8sZFFSbI)

### Inferences
- A home builder would assemble a VIV device from generic parts: a hollow light mast (PVC, fibreglass or carbon tube), an elastic base (spring rod or elastomer), a magnet + coil linear generator or piezo discs/PVDF strips, a bridge rectifier, and an LTC3588-type harvester or supercapacitor. No integrated kit was found.
- Hobbyists should be warned that anything sold as a "bladeless" or "vortex" turbine in the 300–1,200 W range on marketplace sites is not a VIV device.

### Gaps
- No prices or listings were found for purpose-made carbon-fibre masts, elastomer/spring bases, or ready-made tubular linear generators on AliExpress, Amazon or eBay (no shopping listings surfaced).
- No piezo-stack or PVDF price data was gathered.
- No educational VIV/"bladeless" kit was found. Possibly none exists.

---

## 5. School / university student build projects

### Takeaway
Student projects are the richest source of hands-on VIV builds. They include Texas State senior design (2022), a WPI MQP (about 1 mW), several Indian engineering/KSCST piezo prototypes, Roswell High School (ISEF-style) 3D-printed micro masts, Georgia College wind-tunnel work, and a 2017 IEEE pendulum-magnet build. Published power figures are rare, and where given they are milliwatt-scale or voltage-only.

### Cited Findings
**US university**
- **Texas State University, Spring 2022, E1.02 "Bladeless Wind-powered Generator" ("Vortex 1")**: a four-person team, advisor Dr. Rich Compeau. The device is "a long cylinder secured to the ground that harvests crosswinds and outputs a steady DC voltage" via vortex-induced vibration, using "a series of linear alternators". No measured power was found. — [TXST E1.02](https://engineering.txst.edu/senior-design/prior-events/2022-spring/sdd-spring-2022/e1-02.html)
- **Texas State, Spring 2022, E1.03 "A Wind Turbine that produces power without blades" ("Wind Vortex"/"Power Shake")**: a rocking-motion design with four stages: generation (AC, magnet moving over copper coils), rectification, accumulation and a USB 3.0 output. The team compared two coil windings and found the higher-winding coil more effective. No measured power was found. — [TXST E1.03](https://www.engineering.txst.edu/senior-design/prior-events/2022-spring/sdd-spring-2022/e1-03.html); [E1.03 poster PDF](https://docs.gato.txst.edu/252623/E1.03%20Poster.pdf)
- **Texas State, Fall 2022, E2.02 "Vortex One" and E2.03 "Power Shake"** (follow-on teams). The Vortex One page notes that its "single bending rod … experiences wear over time", a fatigue concern. — [TXST E2.02](https://engineering.txst.edu/senior-design/prior-events/2022-fall/sdd-fall-2022/e2-02.html); [TXST E2.03](https://www.engineering.txst.edu/senior-design/prior-events/2022-fall/sdd-fall-2022/e2-03.html)
- **Worcester Polytechnic Institute MQP "Wind Harvesting via Vortex Induced Vibration" (BJS-WD14)**: developed two small-scale vibrational harvesters (a bluff body and an airfoil). The electromagnetic transducer "harvested up to 1 milliwatt of power". The report PDF is downloadable, making it probably the most practical starting point. — [WPI report PDF](https://digital.wpi.edu/downloads/00000130x?locale=en); [WPI record](https://digital.wpi.edu/concern/student_works/mk61rj41w?locale=en)
- **Georgia College & State University (2014–2017)**: built a wind tunnel with a 30.3 × 30.3 cm test section (30.3 × 29.1 cm in a 2014 APS abstract by Ian Agnew and Taylor Ray) to evaluate bladeless designs. 2015 abstract by Chukwuemeka Ibebuike and Hauke Busch. By 2017 the team was "testing the 3D printed prototypes and evaluating the efficiency and power production". No results were seen. — [GCSU 2015](https://kb.gcsu.edu/src/2015/friday/150); [GCSU 2017](https://kb.gcsu.edu/src/2017/friday/65); [APS 2014](https://meetings-archive.aps.org/apr/2014/t1/41); [core.ac.uk PDF](https://core.ac.uk/download/230889757.pdf)

**High school / science fair**
- **Roswell High School (Sarah Palmer), "Optimizing Micro-Geometric Bladeless Wind Turbines, Year Five"** (Society for Science/ISEF-style abstract). The goal was a turbine "small enough to implement in a residential area". Magnets attached to the turbine vibrate past a coil, with wind-tunnel tests of voltage, current, frequency and amplitude (filmed VIV). Five shapes were simulated in ANSYS Fluent, and three were 3D-printed: a triangular prism, a 5°-tapered prism, and a 4-inch 10°-tapered prism. No power figures were seen in the snippet. — [Society for Science abstract 5354](https://abstracts.societyforscience.org/Home/PrintPdf/5354)
- **Florida science-fair project (PVDF piezo)**: tested ways to amplify oscillation of PVDF piezoelectric strips on a bladeless harvester. "The best sail for the piezoelectric element model was the circular sail." — [Society for Science abstract 16889](https://abstracts.societyforscience.org/Home/PrintPdf/16889)
- A Rhode Island K-12 site (East Greenwich) has a "How it Works" page on Vortex Bladeless in a computer-science/renewables unit (explainer level). — [ewg.k12.ri.us](https://sites.google.com/ewg.k12.ri.us/computerscienceinrenewableener/vortex-bladeless)

**Indian / Asian engineering student prototypes** (generally low documentation quality)
- **KSCST (Karnataka State Council for Science & Technology) student project 45S_BE_0352**: a prototype using piezo plates instead of a magnet-coil alternator, reporting "around 60–80" (unit cut off in the source; likely volts open-circuit, unverified). A second KSCST bladeless project is 45S_BE_2185. — [KSCST 0352 PDF](https://www.kscst.org.in/spp/45_series/SPP45S/02_Exhibition_Projects/206_45S_BE_0352.pdf); [KSCST 2185 PDF](https://www.kscst.org.in/spp/45_series/SPP45S/02_Exhibition_Projects/145_45S_BE_2185.pdf)
- **IRJET V8 I2 (2021) paper**: a conical-frustum mast with a spring and piezo chips, output stored in a capacitor and used to light a small bulb. — [IRJET via Issuu](https://issuu.com/irjet/docs/irjet-v8i2285)
- **IRJET "Design, Analysis and Prototype of Vortex Bladeless Wind Turbine"**: a student design-plus-prototype aimed at rural electrification. — [SlideShare](https://www.slideshare.net/slideshow/irjet-design-analysis-and-prototype-of-vortex-bladeless-wind-turbine/173310000)
- **IRJMETS, April 2023, "Design and Development of Vortex Bladeless …"**: a reverse-engineering prototype that "generated some electricity" (no figure seen). — [IRJMETS PDF](https://www.irjmets.com/uploadedfiles/paper/issue_4_april_2023/35364/final/fin_irjmets1680678161.pdf)
- **IRJET V11 I5 (2024) "Design and Testing of Bladeless Wind Turbine"**: details not retrieved. — [Issuu](https://issuu.com/irjet/docs/irjet-v11i5310)
- **2017 Pune college project "Vortex Bladeless Turbine Gyro E-Generator"**: proposed a 3D-printed scaled mast with a gyroscope-based generator. The text is partly garbled. — [academia.edu](https://www.academia.edu/35850988/VORTEX_BLADELESS_TURBINE_GYRO_E_GENERATOR)
- **Zenodo "Design and Analysis of Vortex Bladeless Windmill for Composite Material"**: design/analysis only. — [Zenodo](https://zenodo.org/records/3355094)
- **2017 IEEE ICSEng pendulum build (Ladaran et al.)**: arc- vs disc-shaped magnet pendulum at the mast base, 2,200-turn coils; arc-shaped gave higher voltage (see section 2). — [record](https://katalog.lib.cas.cz/KNAV/EdsRecord/edsair,edsair.doi...........c9c958c3f97bd2ea3ff3aafbb98e1c3c)
- **Linear generator for VIV mast (Pharos Engineering Science Journal, Dec 2024)**: "Design and fabrication of linear generator for vortex bladeless wind turbine". This is academic but directly relevant to a DIY base generator. — [journals.ekb.eg](https://journals.ekb.eg/article_379929.html)
- **Malaysia: "Design of Portable Vortex Bladeless Wind Turbine: The Preliminary Study"**. — [semarakilmu](https://semarakilmu.com.my/journals/index.php/appl_mech/article/view/1474)

### Inferences
- Student builds converge on two generator approaches: (1) magnets at the mast base moving past fixed coils (TXST, Roswell, ICSEng pendulum, WPI) and (2) piezo plates/PVDF strips (KSCST, IRJET, Florida). Magnet-coil builds give usable current at low voltage. Piezo builds give high open-circuit voltage and negligible current. This would explain "60–80 V"-type claims with tiny power.
- Few projects publish power under load at a stated wind speed. WPI's "up to 1 mW" is the most credible number found.

### Gaps
- Could not open the TXST pages or poster, the WPI report, or the Roswell, KSCST or IRJMETS PDFs to extract dimensions, materials, wind speeds or measured power.
- No capstone report found that gives a full bill of materials plus load-tested output curve.

---

## 6. Realistic power outputs and common failure points

### Takeaway
Documented small-scale bladeless/VIV builds produce from nanowatts (MEMS) through microwatts to about 1–5 mW (centimetre-scale and student builds). No hobbyist build with credible watt-level output was found. Recurring problems: output only near lock-in (a narrow wind band), the need for steady wind, VIV amplitude that does not grow with wind speed, fatigue/wear of the single bending element, generators too weak at low frequency, and piezo outputs that read high voltage but deliver negligible power.

### Cited Findings
**Measured/claimed outputs**
- WPI MQP electromagnetic VIV harvester: up to 1 mW. — [WPI](https://digital.wpi.edu/downloads/00000130x?locale=en)
- A review table of centimetre-scale VIV harvesters lists maximum outputs of 0.03–5 mW. The 5 mW entry used a bluff body about 2.5 cm in diameter × 11 cm long with a cut-in speed of about 2 m/s. — [arXiv 2308.04110 review](https://arxiv.org/pdf/2308.04110)
- A MEMS piezo VIV harvester (hollow polystyrene cylinder on a silicon chip) produced nanowatt-range power. Placing it among up to 25 cylinders raised output versus the isolated case. — [PMC6938501](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6938501/)
- Murray-Smith's speaker-coil/blind-slat vibrators: output "tiny". — [Hackaday 2020](https://hackaday.com/2020/06/30/experimenting-with-vibratory-wind-generators)
- KSCST piezo prototype: "around 60–80" (unit cut off, presumably volts; no current/power). — [KSCST](https://www.kscst.org.in/spp/45_series/SPP45S/02_Exhibition_Projects/206_45S_BE_0352.pdf)
- For comparison, even small bladed model turbines produce only 0.5–2.5 V, and about 1.8 V is needed to light an LED. — [Instructables KidWind](https://www.instructables.com/Model-Wind-Turbine-KidWind-Project/). A forum builder's rotary test gave at most 0.5 V with a hairdryer, and another got about 2 V ("won't power an LED"). — [PrepRoom forum](https://community.preproom.org/index.php?threads/diy-wind-turbine.12263/)
- Windbelt needs about 6 m/s (13 mph) for maximum generation. — [Tom's Guide](https://www.tomsguide.com/us/wind-power-energy-green-energy-windmills,news-6192.html)

**Failure points / limitations**
- **Lock-in / narrow wind band**: bladeless turbines "face operational limitations due to the lock-in phenomenon". Proposed fixes are tuning natural frequency by adjusting mast length or adding mass, and material choice matters. — [Scientific Reports 2025 via PMC11711754](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11711754/). Physics Forums commenters likewise flag the narrow Reynolds-number range. — [Physics Forums](https://physicsforums.com/threads/new-bladeless-design-for-wind-energy.814428)
- **Amplitude does not rise with wind speed**: "unlike the galloping phenomenon, the vibration magnitude of VIV does not monotonically increase with the wind speed." — [PMC9693298](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9693298/)
- **Needs stable wind / turbulence problem**: resonance depends on relatively stable winds, which turbulent (e.g., urban, rooftop) sites lack. — [CleanTechnica 2015](https://cleantechnica.com/2015/05/21/bladeless-wind-turbine-reality-check/)
- **Fatigue/wear at the bending element**: TXST Vortex One notes its single bending rod "experiences wear over time". — [TXST E2.02](https://engineering.txst.edu/senior-design/prior-events/2022-fall/sdd-fall-2022/e2-02.html)
- **Weak generator at low frequency / coil design matters**: TXST E1.03 found the higher-winding coil more effective. ICSEng builders used 2,200-turn coils and found the larger arc magnet gave more voltage. Patent benchmarks for linear vibration generators are about 9 mW at 6 Hz. — [TXST poster](https://docs.gato.txst.edu/252623/E1.03%20Poster.pdf); [MDPI review](https://mdpi.com/1996-1073/15/18/6773); [US 8957558](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/8957558)
- **Rectification/storage stage required**: TXST E1.03 had to add rectification and accumulation stages before a USB output. IRJET builds stored charge in a capacitor before lighting a bulb. — [TXST poster](https://docs.gato.txst.edu/252623/E1.03%20Poster.pdf); [IRJET](https://issuu.com/irjet/docs/irjet-v8i2285)
- **Tuning to shedding frequency**: Vortex-style designs use spring features so the shedding frequency matches the structure's natural frequency. The Strouhal number is the standard tool for predicting shedding frequency. — [US patent 12698752 (via Physics Forums search)](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12698752); [AMME journal paper](https://amme.journals.ekb.eg/article_449047_077ebba036dddc0f399a259daeb8e1b1.pdf); [US 10982648 telescoping tuning patent](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/10982648)

### Inferences
- A realistic expectation for a well-built home VIV mast under about 2 m is single-digit milliwatts to perhaps tens of milliwatts near lock-in, and near zero elsewhere. That is enough to trickle-charge a supercapacitor for an LED blink or a sensor node, not to make household power. No source documents a hobby build reaching 1 W.
- Using St ≈ 0.2 (standard Strouhal value for a circular cylinder), a 10 cm-diameter mast in a 5 m/s wind sheds vortices at about f = 0.2 × 5 / 0.1 ≈ 10 Hz. The mast/spring system must therefore be tuned to around 10 Hz, and it will drop out of lock-in as wind speed shifts. This explains the "narrow wind band" complaint. (Own calculation, illustrative only.)
- Piezo builds reporting tens of volts open-circuit should not be read as meaningful power. The current, and therefore the power, is tiny. Load-tested power is the metric to ask for.
- A 2 m mast at domestic scale will see millions of bending cycles per week near 10 Hz. Base fatigue (the rod, spring or elastomer) is therefore the predictable mechanical failure, as hinted by TXST.

### Gaps
- No hobbyist source with load-tested power vs. wind-speed curves for a home-scale (0.5–2 m) VIV mast was found.
- No quantified data on rectification losses (diode drop vs. coil voltage) for DIY VIV builds was found, only the presence of rectifier/storage stages.
- No documented long-term outdoor endurance or fatigue tests of hobby builds were found.
