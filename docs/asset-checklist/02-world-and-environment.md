# 02 — World & environment assets

Twelve districts, the world VFX layer, ten vehicle classes and the interactable set.

**Every district gets the same 8 deliverables** (architecture kit, prop set, hero landmark,
terrain/roads, lighting preset, weather response, audio bed, streaming/collision). That
uniformity is deliberate — it is what lets the world team pipeline twelve districts in parallel
without each one inventing its own deliverable list.

---

## 1. Districts (12 × 8)

### 1.1 Downtown Core (`DTC`)
- [ ] `ENV-DTC-01` — Architecture kit: high-rise towers, glass curtain walls, sky-bridges, retail podiums (24+ pieces) [S] [P0]
- [ ] `ENV-DTC-02` — Prop set: holographic billboards, traffic bollards, café seating, vending machines, dumpsters (20+) [D] [P0]
- [ ] `ENV-DTC-03` — Hero landmark: central exchange tower and plaza [D] [P1]
- [ ] `ENV-DTC-04` — Terrain & road network: grid streets, elevated highway, pedestrian underpasses [D] [P0]
- [ ] `ENV-DTC-05` — Lighting preset: cool blue-grey grade, dense night signage, tuned 24h curve [D] [P1]
- [ ] `ENV-DTC-06` — Weather response: rain sheeting on glass, reflective wet asphalt, steam vents [D] [P1]
- [ ] `ENV-DTC-07` — Audio bed: traffic hum, sirens, crowd murmur + urban-canyon reverb zone [D] [P2]
- [ ] `ENV-DTC-08` — Streaming & collision: nav mesh, HLOD proxies, streaming volume, occluders [D] [P0]

### 1.2 University (`UNI`)
- [ ] `ENV-UNI-01` — Architecture kit: lecture halls, cloisters, libraries, dorm blocks, labs (24+ pieces) [S] [P1]
- [ ] `ENV-UNI-02` — Prop set: desks, noticeboards, lab benches, bike racks, vending machines, campus signage (20+) [D] [P1]
- [ ] `ENV-UNI-03` — Hero landmark: clock tower and central quad [D] [P1]
- [ ] `ENV-UNI-04` — Terrain & road network: campus paths, lawns, service roads, cycle lanes [D] [P1]
- [ ] `ENV-UNI-05` — Lighting preset: warm academic grade, green-space bounce, dusk lecture glow [D] [P1]
- [ ] `ENV-UNI-06` — Weather response: puddles on lawns, umbrella crowd density swap, snow on quad [D] [P2]
- [ ] `ENV-UNI-07` — Audio bed: bells, chatter, page turns + library hush reverb zone [D] [P2]
- [ ] `ENV-UNI-08` — Streaming & collision: nav mesh, HLOD proxies, streaming volume [D] [P1]

### 1.3 Old Town (`OLD`)
- [ ] `ENV-OLD-01` — Architecture kit: timber-framed houses, cobbled lanes, tiled roofs, arched gates (24+ pieces) [S] [P0]
- [ ] `ENV-OLD-02` — Prop set: market stalls, lanterns, crates, barrels, hand-painted signage (20+) [D] [P0]
- [ ] `ENV-OLD-03` — Hero landmark: ancestral shrine gate and market square [D] [P1]
- [ ] `ENV-OLD-04` — Terrain & road network: cobbled lanes, stone steps, canalside walk, dead-ends [D] [P0]
- [ ] `ENV-OLD-05` — Lighting preset: warm lantern-lit grade, tight night falloff, golden hour hero [D] [P1]
- [ ] `ENV-OLD-06` — Weather response: wet cobbles with anisotropic sheen, snow catch on tiles, fog in lanes [D] [P1]
- [ ] `ENV-OLD-07` — Audio bed: market hawking, wooden carts, wind chimes + stone-alley reverb [D] [P2]
- [ ] `ENV-OLD-08` — Streaming & collision: nav mesh, HLOD proxies, streaming volume [D] [P0]

### 1.4 Industrial (`IND`)
- [ ] `ENV-IND-01` — Architecture kit: factories, warehouses, chimneys, gantries, loading bays (24+ pieces) [S] [P1]
- [ ] `ENV-IND-02` — Prop set: pallets, drums, forklifts, pipe runs, chain-link, hazard signage (20+) [D] [P1]
- [ ] `ENV-IND-03` — Hero landmark: blast furnace stack and rail yard [D] [P1]
- [ ] `ENV-IND-04` — Terrain & road network: haul roads, rail spurs, catwalks, fenced yards [D] [P1]
- [ ] `ENV-IND-05` — Lighting preset: sodium-orange grade, heavy haze, harsh work-lamp pools [D] [P1]
- [ ] `ENV-IND-06` — Weather response: acid-rain puddle tint, smog layering with fog, steam plumes [D] [P1]
- [ ] `ENV-IND-07` — Audio bed: machine drone, hydraulic hisses, distant klaxons + hangar reverb [D] [P2]
- [ ] `ENV-IND-08` — Streaming & collision: nav mesh, HLOD proxies, streaming volume [D] [P1]

### 1.5 Entertainment (`ENT`)
- [ ] `ENV-ENT-01` — Architecture kit: clubs, arcades, theatres, neon storefronts, rooftop bars (24+ pieces) [S] [P1]
- [ ] `ENV-ENT-02` — Prop set: neon signage, speaker stacks, arcade cabinets, queue barriers, photo walls (20+) [D] [P1]
- [ ] `ENV-ENT-03` — Hero landmark: main strip arch and concert stage [D] [P1]
- [ ] `ENV-ENT-04` — Terrain & road network: pedestrian strip, VIP alleys, rooftop traverse routes [D] [P1]
- [ ] `ENV-ENT-05` — Lighting preset: saturated neon grade, coloured bounce, strobe-capable fixtures [D] [P1]
- [ ] `ENV-ENT-06` — Weather response: neon reflections doubling on wet ground, rain dimming crowds [D] [P1]
- [ ] `ENV-ENT-07` — Audio bed: layered music beds per venue, crowd roar + club reverb zones [D] [P2]
- [ ] `ENV-ENT-08` — Streaming & collision: nav mesh, HLOD proxies, streaming volume [D] [P1]

### 1.6 Waterfront (`WTR`)
- [ ] `ENV-WTR-01` — Architecture kit: piers, docks, warehouses, boardwalks, lighthouse (24+ pieces) [S] [P1]
- [ ] `ENV-WTR-02` — Prop set: mooring bollards, nets, crates, dock cranes, buoys, fish stalls (20+) [D] [P1]
- [ ] `ENV-WTR-03` — Hero landmark: lighthouse and container crane silhouette [D] [P1]
- [ ] `ENV-WTR-04` — Terrain & road network: boardwalks, ramps, water volumes, boat landings [D] [P1]
- [ ] `ENV-WTR-05` — Lighting preset: cool marine grade, specular sun path over water, night dock lamps [D] [P1]
- [ ] `ENV-WTR-06` — Weather response: wave-height response to storms, spray on piers, sea-fog banks [D] [P1]
- [ ] `ENV-WTR-07` — Audio bed: gulls, rigging creaks, hull slap + open-water reverb [D] [P2]
- [ ] `ENV-WTR-08` — Streaming & collision: nav mesh (incl. water nav for boats), HLOD proxies, streaming volume [D] [P1]

### 1.7 Suburbs (`SUB`)
- [ ] `ENV-SUB-01` — Architecture kit: family homes, garages, fences, porches, cul-de-sacs (24+ pieces) [S] [P1]
- [ ] `ENV-SUB-02` — Prop set: mailboxes, hedges, garden furniture, bins, parked cars, kid toys (20+) [D] [P1]
- [ ] `ENV-SUB-03` — Hero landmark: community park and school frontage [D] [P2]
- [ ] `ENV-SUB-04` — Terrain & road network: cul-de-sacs, driveways, back-alley shortcuts, park paths [D] [P1]
- [ ] `ENV-SUB-05` — Lighting preset: bright domestic grade, long lawn shadows, warm window glow at night [D] [P1]
- [ ] `ENV-SUB-06` — Weather response: sprinkler/rain overlap rules, snow on lawns, heat shimmer on asphalt [D] [P2]
- [ ] `ENV-SUB-07` — Audio bed: birdsong, distant traffic, lawnmowers + open-suburb reverb [D] [P2]
- [ ] `ENV-SUB-08` — Streaming & collision: nav mesh, HLOD proxies, streaming volume [D] [P1]

### 1.8 Mystic Heights (`MYH`)
- [ ] `ENV-MYH-01` — Architecture kit: mountain sect gates, pavilions, cliff temples, stone stairs (24+ pieces) [S] [P1]
- [ ] `ENV-MYH-02` — Prop set: incense burners, prayer flags, stone lions, meditation platforms, herb racks (20+) [D] [P1]
- [ ] `ENV-MYH-03` — Hero landmark: summit pavilion above the cloud line [D] [P1]
- [ ] `ENV-MYH-04` — Terrain & road network: cliff switchbacks, rope bridges, floating stone steps [D] [P1]
- [ ] `ENV-MYH-05` — Lighting preset: high-altitude grade, thin-air haze, dawn-first lighting [D] [P1]
- [ ] `ENV-MYH-06` — Weather response: cloud sea below the ridge, summit lightning, snow line [D] [P1]
- [ ] `ENV-MYH-07` — Audio bed: wind, temple bells, distant chanting + cliff-edge reverb [D] [P2]
- [ ] `ENV-MYH-08` — Streaming & collision: nav mesh, HLOD proxies, streaming volume, vertical-travel volumes [D] [P1]

### 1.9 Arcane District (`ARC`)
- [ ] `ENV-ARC-01` — Architecture kit: floating spires, rune-etched facades, ley-line bridges, crystal growths (24+ pieces) [S] [P1]
- [ ] `ENV-ARC-02` — Prop set: floating tomes, rune pedestals, crystal lamps, summoning floors, arcane scaffolding (20+) [D] [P1]
- [ ] `ENV-ARC-03` — Hero landmark: the great grimoire tower [D] [P1]
- [ ] `ENV-ARC-04` — Terrain & road network: suspended walkways, teleport pads, gravity-inverted steps [D] [P1]
- [ ] `ENV-ARC-05` — Lighting preset: violet-cyan grade, emissive-dominant, low ambient for rune contrast [D] [P1]
- [ ] `ENV-ARC-06` — Weather response: ambient rune drift in all weather, storm-triggered arcane flares [D] [P1]
- [ ] `ENV-ARC-07` — Audio bed: shimmering drone, page flutter, chime clusters + cavernous reverb [D] [P2]
- [ ] `ENV-ARC-08` — Streaming & collision: nav mesh, HLOD proxies, streaming volume, floating-geometry movers [D] [P1]

### 1.10 Underground (`UND`)
- [ ] `ENV-UND-01` — Architecture kit: tunnels, sewers, subway platforms, smuggler dens, vault doors (24+ pieces) [S] [P1]
- [ ] `ENV-UND-02` — Prop set: pipes, grates, graffiti, makeshift stalls, caged lights, contraband crates (20+) [D] [P1]
- [ ] `ENV-UND-03` — Hero landmark: flooded black-market exchange [D] [P1]
- [ ] `ENV-UND-04` — Terrain & road network: tunnel branches, maintenance ladders, water channels [D] [P1]
- [ ] `ENV-UND-05` — Lighting preset: near-black grade, single-source practicals, torch and headlamp falloff [D] [P1]
- [ ] `ENV-UND-06` — Weather response: drip rate tied to surface rain, flooding volumes, no sky visibility [D] [P1]
- [ ] `ENV-UND-07` — Audio bed: dripping, distant trains, muffled surface bleed + tight-tunnel reverb [D] [P2]
- [ ] `ENV-UND-08` — Streaming & collision: nav mesh, HLOD proxies, streaming volume, light-only visibility culling [D] [P1]

### 1.11 Rural (`RUR`)
- [ ] `ENV-RUR-01` — Architecture kit: farmhouses, barns, silos, greenhouses, mill houses (24+ pieces) [S] [P1]
- [ ] `ENV-RUR-02` — Prop set: hay bales, troughs, fencing, scarecrows, carts, crop rows (20+) [D] [P1]
- [ ] `ENV-RUR-03` — Hero landmark: watermill and market barn [D] [P2]
- [ ] `ENV-RUR-04` — Terrain & road network: dirt tracks, field boundaries, river crossings, forest edges [D] [P1]
- [ ] `ENV-RUR-05` — Lighting preset: wide open-sky grade, unoccluded sun, heavy dusk saturation [D] [P1]
- [ ] `ENV-RUR-06` — Weather response: crop sway with wind, mud tracks after rain, frost on fields, heatwave haze [D] [P1]
- [ ] `ENV-RUR-07` — Audio bed: insects, livestock, wind in crops + open-field reverb [D] [P2]
- [ ] `ENV-RUR-08` — Streaming & collision: nav mesh, HLOD impostors for long view distances, streaming volume [D] [P1]

### 1.12 Government Center (`GOV`)
- [ ] `ENV-GOV-01` — Architecture kit: ministry blocks, courthouse steps, plazas, security gates (24+ pieces) [S] [P1]
- [ ] `ENV-GOV-02` — Prop set: flagpoles, barricades, security cameras, metal detectors, podiums (20+) [D] [P1]
- [ ] `ENV-GOV-03` — Hero landmark: capitol dome and ceremonial plaza [D] [P1]
- [ ] `ENV-GOV-04` — Terrain & road network: ceremonial avenue, checkpoint lanes, motorcade routes [D] [P1]
- [ ] `ENV-GOV-05` — Lighting preset: neutral institutional grade, floodlit facades at night [D] [P1]
- [ ] `ENV-GOV-06` — Weather response: searchlight scatter in rain and fog, plaza drainage [D] [P2]
- [ ] `ENV-GOV-07` — Audio bed: flags, PA announcements, boot steps + marble-hall reverb [D] [P2]
- [ ] `ENV-GOV-08` — Streaming & collision: nav mesh, HLOD proxies, streaming volume, restricted-zone triggers [D] [P1]

---

## 2. World VFX — dynamic weather (`ENV-WX`)

Each state needs a material set, a particle system, an audio layer and a gameplay hook
(slippery surfaces, visibility, sound propagation).

### Rain
- [ ] `ENV-WX-01` — Light rain: drizzle streaks, darkened surfaces, soft audio layer [S] [P0]
- [ ] `ENV-WX-02` — Heavy rain: dense streaks, splash decals, reduced visibility cone [S] [P0]
- [ ] `ENV-WX-03` — Torrential / storm rain: wind-sheared streaks, sheet runoff on roofs [S] [P1]
- [ ] `ENV-WX-04` — Puddle system: formation over time, ripple decals, footstep splash [S] [P1]
- [ ] `ENV-WX-05` — Wet surface shader: roughness drop, anisotropic sheen on cobbles and glass [S] [P0]
- [ ] `ENV-WX-06` — Character wetness pass: material blend, dripping, hair clumping [D] [P1]

### Snow & cold
- [ ] `ENV-WX-07` — Snowfall: light / heavy, wind-driven drift behaviour [S] [P1]
- [ ] `ENV-WX-08` — Accumulation shader: upward-facing surface blend, depth-based [S] [P1]
- [ ] `ENV-WX-09` — Footprint and tyre-track decals with melt timer [S] [P1]
- [ ] `ENV-WX-10` — Breath vapour on characters in cold districts [D] [P2]

### Thunderstorms
- [ ] `ENV-WX-11` — Lightning flash: sky bolt, localised strike, screen-safe exposure handling [S] [P1]
- [ ] `ENV-WX-12` — Thunder audio layer with distance-based delay [S] [P1]
- [ ] `ENV-WX-13` — Power flicker and outage hook for district lighting [S] [P1]
- [ ] `ENV-WX-14` — Strike hazard VFX on exposed metal and high ground [D] [P2]

### Fog
- [ ] `ENV-WX-15` — Volumetric fog layer with height falloff [S] [P1]
- [ ] `ENV-WX-16` — Ground fog volumes for lanes, alleys and waterfront [S] [P1]
- [ ] `ENV-WX-17` — Fog-of-war / detection range gameplay hook (stealth balance) [D] [P1]

### Heatwaves
- [ ] `ENV-WX-18` — Heat distortion post-process over asphalt and rooftops [S] [P1]
- [ ] `ENV-WX-19` — Shimmer particles and dust motes, sun-bleached grade [S] [P2]
- [ ] `ENV-WX-20` — Transition system: smooth blending between all weather states, no hard cuts [D] [P0]

---

## 3. World VFX — Spiritual Storms (`ENV-SPS`)

- [ ] `ENV-SPS-01` — Aurora sky dome: banded curtains, colour-shifting, visible from any outdoor district [S] [P0]
- [ ] `ENV-SPS-02` — Floating debris: rocks, tiles and furniture lifted with tumbling physics [S] [P1]
- [ ] `ENV-SPS-03` — Qi rain: luminous falling motes that light surfaces on contact [S] [P1]
- [ ] `ENV-SPS-04` — Localised gravity anomaly volumes (float zones for traversal) [D] [P1]
- [ ] `ENV-SPS-05` — Spiritual pressure screen effect: vignette pulse, chromatic edge, audio swell [S] [P1]
- [ ] `ENV-SPS-06` — Storm-tier scaling: 3 intensities with distinct budgets and gameplay modifiers [D] [P1]

---

## 4. World VFX — Arcane Surges (`ENV-ASG`)

- [ ] `ENV-ASG-01` — Floating runes: drifting glyph billboards with parallax and fade [S] [P0]
- [ ] `ENV-ASG-02` — Ley-line ground glow: animated spline emission along district routes [S] [P1]
- [ ] `ENV-ASG-03` — Rift portals: tear VFX with spawn/despawn states [S] [P1]
- [ ] `ENV-ASG-04` — Surge pulse: expanding ring from a surge origin, occlusion-aware [D] [P1]
- [ ] `ENV-ASG-05` — Emissive material boost pass so runes read against lit surfaces [D] [P1]
- [ ] `ENV-ASG-06` — Surge-tier scaling: 3 intensities, particle budget capped per tier [D] [P1]

---

## 5. Day / night cycle (`ENV-CYC`)

- [ ] `ENV-CYC-01` — Sun and moon path with correct arc per season preset [S] [P0]
- [ ] `ENV-CYC-02` — 24-hour lighting curve: exposure, sky colour, ambient bounce keyframes [S] [P0]
- [ ] `ENV-CYC-03` — Streetlight and window emissive triggers at dusk [S] [P0]
- [ ] `ENV-CYC-04` — Star field and moon phases [S] [P1]
- [ ] `ENV-CYC-05` — Per-district grade blend so all 12 keep their identity through the cycle [D] [P0]
- [ ] `ENV-CYC-06` — NPC schedule hook: crowd density and shop state driven by time of day [D] [P1]
- [ ] `ENV-CYC-07` — Long-shadow and shadow-cascade tuning for the golden-hour frames [D] [P2]

---

## 6. Vehicles (10 classes)

Every vehicle ships with: mesh + rig, **3 damage states (light / heavy / wrecked)**, VFX trail,
interior where applicable, audio set, handling config, and the mount animation from `ANM-VEH`.

- [ ] `VEH-01` — Bicycle: mesh, damage states, chain/pedal rig, bell audio [S] [P0]
- [ ] `VEH-02` — Motorcycle: lean rig, exhaust VFX, engine audio set, crash slide [S] [P0]
- [ ] `VEH-03` — Sedan: 4-door family car, interior, door/boot articulation [S] [P0]
- [ ] `VEH-04` — Sports car: low body, interior, high-rev audio set [S] [P1]
- [ ] `VEH-05` — SUV: taller cabin, roof rack, off-road suspension variant [S] [P1]
- [ ] `VEH-06` — Van: cargo interior, sliding door, haul-capacity config [S] [P1]
- [ ] `VEH-07` — Boat: hull, wake VFX, water interaction, helm interior [S] [P1]
- [ ] `VEH-08` — Flying sword: hover rig, Qi trail, ride platform socket, no interior [S] [P0]
- [ ] `VEH-09` — Magic broom: hover rig, bristle physics, enchantment trail [S] [P1]
- [ ] `VEH-10` — Qi cloud: volumetric cloud mesh, luminous trail, float motion [S] [P1]
- [ ] `VEH-11` — Damage-state standard applied across all 10: dented / wrecked / burning meshes [S] [P0]
- [ ] `VEH-12` — Magic-vehicle VFX set: sword, broom and cloud trails share one material family [D] [P1]
- [ ] `VEH-13` — Interior camera and seat sockets for all driveable vehicles [D] [P1]
- [ ] `VEH-14` — Handling config data per class (accel, top speed, turn radius, air control) [D] [P0]
- [ ] `VEH-15` — Audio sets: engine, tyre, hull, magic hum — one bank per class [D] [P1]
- [ ] `VEH-16` — Wreck persistence: wrecks stay in the world as cover/obstacles [D] [P2]

---

## 7. Interactables — harvestable nodes (`INT-HRV`)

Each node type ships with: model + LOD, **depleted state**, regrowth timer, harvest animation
(from `ANM-CRF`), loot table hook, and scatter/spawn rules.

- [ ] `INT-HRV-01` — Herbs: 5+ species variants, Rural / Mystic Heights scatter [S] [P0]
- [ ] `INT-HRV-02` — Trees: 5+ species, choppable with falling and stump state [S] [P0]
- [ ] `INT-HRV-03` — Ore: 4+ vein types (iron, jade, spirit, tech-scrap), wall and boulder forms [S] [P0]
- [ ] `INT-HRV-04` — Fish: 5+ species, water-volume spawn, bite indicator VFX [S] [P0]
- [ ] `INT-HRV-05` — Tech salvage: 4+ wreck types (drone husk, server rack, car shell, panel) [S] [P0]
- [ ] `INT-HRV-06` — Depleted-state meshes for all node types (picked clean, stump, empty vein) [D] [P0]
- [ ] `INT-HRV-07` — Regrowth and respawn rules per node type, district-tuned [D] [P0]
- [ ] `INT-HRV-08` — Node quality tiers: 5 rarity tiers with visual tells (size, glow, veins) [D] [P1]
- [ ] `INT-HRV-09` — Scatter tooling: procedural placement rules per district biome [D] [P1]

---

## 8. Interactables — modular property furniture (`INT-FUR`)

Property = player-owned interiors. Functional stations drive crafting; decorative props only dress.

### Functional stations
- [ ] `INT-FUR-F01` — Bed (rest / save point), 3 styles [S] [P0]
- [ ] `INT-FUR-F02` — Storage chest / wardrobe, 3 sizes [S] [P0]
- [ ] `INT-FUR-F03` — Portable forge station (anvil + trough pair) [S] [P0]
- [ ] `INT-FUR-F04` — Portable alchemy station (cauldron + burner) [S] [P0]
- [ ] `INT-FUR-F05` — Kitchen station (board + stove unit) [S] [P0]
- [ ] `INT-FUR-F06` — Enchanting circle floor decal + pedestal set [S] [P1]
- [ ] `INT-FUR-F07` — Workbench (general repair and crafting) [S] [P0]
- [ ] `INT-FUR-F08` — Terminal / multi-monitor rig (hacking and management) [S] [P1]
- [ ] `INT-FUR-F09` — Training dummy (martial practice, pairs with `CR-CUL-T02`) [S] [P1]
- [ ] `INT-FUR-F10` — Trophy / display shelf with item sockets [S] [P1]
- [ ] `INT-FUR-F11` — Meditation mat (Qi cultivation, pairs with `CR-CUL-T01`) [S] [P1]
- [ ] `INT-FUR-F12` — Vehicle lift / garage bay (Mechanic property) [S] [P2]
- [ ] `INT-FUR-F13` — Streaming / camera corner (Influencer property) [D] [P2]
- [ ] `INT-FUR-F14` — Executive desk (Corporate Heir property) [D] [P2]

### Decorative props
- [ ] `INT-FUR-D01` — Seating set: chairs, stools, sofa, floor cushions [S] [P1]
- [ ] `INT-FUR-D02` — Tables: dining, coffee, side, desk [S] [P1]
- [ ] `INT-FUR-D03` — Lighting: floor lamp, pendant, candles, lantern, neon strip [S] [P1]
- [ ] `INT-FUR-D04` — Rugs, curtains and wall hangings [S] [P1]
- [ ] `INT-FUR-D05` — Plants and planters, indoor-safe [S] [P1]
- [ ] `INT-FUR-D06` — Shelves, cabinets and display cases [S] [P1]
- [ ] `INT-FUR-D07` — Wall art, mirrors and trophies [S] [P2]
- [ ] `INT-FUR-D08` — Culturally themed sets (Old Town, Arcane, Cyber) so properties match districts [D] [P2]
- [ ] `INT-FUR-D09` — Placement system: grid + free rotate, collision preview, wall/floor snap [D] [P0]
- [ ] `INT-FUR-D10` — Furniture icon set for the placement UI [D] [P1]
