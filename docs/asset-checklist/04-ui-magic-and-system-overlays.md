# 04 — UI, magic & system overlays

Interface skin, the spell-casting input layer and the per-persona aura system.

All UI is **9-slice, localisation-safe** (no baked text), legible at 720p and 4K. Obsidian
glassmorphism is a single master material with instance parameters — panels never bake their own
border or blur.

---

## 1. Interface (`UI`)

### Obsidian glassmorphism panel system
- [ ] `UI-01` — Master obsidian glass material: dark tint, depth blur, specular edge, grain [S] [P0]
- [ ] `UI-02` — 9-slice panel base with corner filigree variants (3) [S] [P0]
- [ ] `UI-03` — Panel header bar with title slot and close control [S] [P0]
- [ ] `UI-04` — Divider, rule and section-break elements [S] [P0]
- [ ] `UI-05` — Tooltip variant (compact, anchored) [S] [P0]
- [ ] `UI-06` — Modal / confirm variant with dimmed backdrop [S] [P0]
- [ ] `UI-07` — Notification toast variant, stacking rules [S] [P0]
- [ ] `UI-08` — Button states: idle / hover / pressed / disabled / focus [D] [P0]
- [ ] `UI-09` — Scroll bar, slider, checkbox, dropdown and tab components [D] [P0]
- [ ] `UI-10` — Empty / loading / error states for every panel [D] [P1]

### Adaptive joysticks
- [ ] `UI-11` — Left adaptive joystick, appears at first touch point [S] [P0]
- [ ] `UI-12` — Right adaptive joystick / look zone [S] [P0]
- [ ] `UI-13` — Joystick skins: obsidian default + high-contrast accessibility skin [S] [P0]
- [ ] `UI-14` — Dead-zone, opacity and size settings exposed in options [D] [P0]
- [ ] `UI-15` — Contextual face-button ring that swaps with the joystick on thumb focus [D] [P1]

### Gesture-zone prompts
- [ ] `UI-16` — Gesture-zone overlay: drawn arcs showing swipe, hold and draw areas [S] [P0]
- [ ] `UI-17` — Prompt icons: interact, cast, draw, stealth, vehicle, harvest [S] [P0]
- [ ] `UI-18` — Zone highlight and success/failure feedback flash [S] [P0]
- [ ] `UI-19` — First-time tutorial overlay that fades once a gesture is learned [D] [P1]

### Floating dialogue cards
- [ ] `UI-20` — Floating dialogue card: obsidian frame, portrait slot, nameplate [S] [P0]
- [ ] `UI-21` — Choice list variant with up to 4 options and scroll [S] [P0]
- [ ] `UI-22` — World-anchored card that tracks the speaker's head [S] [P1]
- [ ] `UI-23` — Affinity / faction reaction indicator on the card [D] [P1]
- [ ] `UI-24` — Text reveal typing effect with skip control [D] [P1]

### Circular GPS minimaps
- [ ] `UI-25` — Circular minimap: compass ring, rotation modes (north-up / heading-up) [S] [P0]
- [ ] `UI-26` — POI icon set: quest, vendor, property, threat, harvest, vehicle (12+) [S] [P0]
- [ ] `UI-27` — Fog-of-war reveal layer tied to visited areas [S] [P1]
- [ ] `UI-28` — Zoom levels: street / district / city, with label density rules [S] [P1]
- [ ] `UI-29` — Off-screen objective arrow ring around the minimap [D] [P0]
- [ ] `UI-30` — Full-screen map screen built from the same map data [D] [P1]

### HUD & system screens
- [ ] `UI-31` — Health, stamina and Qi bars with low-state pulses [S] [P0]
- [ ] `UI-32` — Persona / reputation meter [S] [P0]
- [ ] `UI-33` — Money, inventory weight and quick-slot strip [S] [P0]
- [ ] `UI-34` — Inventory grid with rarity frames, sorting and comparison [S] [P0]
- [ ] `UI-35` — Quest tracker and journal screen [S] [P0]
- [ ] `UI-36` — Character screen: creator preview, stats, equipped layers [S] [P1]
- [ ] `UI-37` — Crafting screen: recipe list, material sockets, yield preview [S] [P0]
- [ ] `UI-38` — Skill / cultivation tree screen [S] [P1]
- [ ] `UI-39` — Property management screen (furniture placement, upgrades) [S] [P1]
- [ ] `UI-40` — Main menu, settings, credits and loading screens [D] [P0]
- [ ] `UI-41` — Damage indicators, hit markers, kill confirmations [D] [P0]
- [ ] `UI-42` — Accessibility pass: colourblind modes, text scale, hold-vs-toggle, subtitles [D] [P1]
- [ ] `UI-43` — Diegetic variant pass for VR / immersion mode (optional) [D] [P2]

---

## 2. Magic & Qi (`MAG`)

### Spell drawing shapes — 6 (`MAG-SHP`)
Six drawable gestures. The **shape names below are proposals** — the brief specifies the count,
not the identities, so design must lock them (see open questions).

- [ ] `MAG-SHP-01` — Shape 1: circle — ward / shield family [S] [P0]
- [ ] `MAG-SHP-02` — Shape 2: triangle — elemental strike family [S] [P0]
- [ ] `MAG-SHP-03` — Shape 3: spiral — Qi gather / channel family [S] [P0]
- [ ] `MAG-SHP-04` — Shape 4: cross / sigil — bind and seal family [S] [P0]
- [ ] `MAG-SHP-05` — Shape 5: star polygon — summon family [S] [P1]
- [ ] `MAG-SHP-06` — Shape 6: rune lattice — dispel / counter family [S] [P1]
- [ ] `MAG-DRW-01` — Draw canvas: gesture trail renderer with fade and taper [D] [P0]
- [ ] `MAG-DRW-02` — Recognition feedback: partial-match highlight, success snap, failure shatter [D] [P0]
- [ ] `MAG-DRW-03` — Per-shape cast animation (cross-ref `ANM-CRF-24`) [D] [P0]
- [ ] `MAG-DRW-04` — Accuracy grading: sloppy vs. precise draw changes cast speed and cost [D] [P2]

### 3D grimoire & lockable runes (`MAG-GRM`)
- [ ] `MAG-GRM-01` — Physical 3D grimoire: cover, spine, page block, worn leather material [S] [P0]
- [ ] `MAG-GRM-02` — Turnable pages with curl deformation and page-flip audio [S] [P0]
- [ ] `MAG-GRM-03` — Page layout template: illustration, rune block, note space [S] [P0]
- [ ] `MAG-GRM-04` — **Lockable runes**: sealed glyph state with lock iconography [S] [P0]
- [ ] `MAG-GRM-05` — Rune unlock sequence: key insert, glow build, seal break VFX [S] [P0]
- [ ] `MAG-GRM-06` — Unlocked rune idle state: slow pulse matched to its element [S] [P1]
- [ ] `MAG-GRM-07` — Page content set: one spread per spell family (6 minimum) [D] [P1]
- [ ] `MAG-GRM-08` — Grimoire variants per career (Scholar tome vs. Cultivator jade slips vs. Cultist flesh tome) [D] [P1]

### Meridian body map overlays (`MAG-MER`)
- [ ] `MAG-MER-01` — Body-map overlay mesh conforming to all 5 base body frames [S] [P0]
- [ ] `MAG-MER-02` — Principal meridian line set (12 lines, anatomically routed) [S] [P0]
- [ ] `MAG-MER-03` — Acupoint node markers with selectable states [S] [P0]
- [ ] `MAG-MER-04` — Qi flow animation along the lines, direction-aware [S] [P0]
- [ ] `MAG-MER-05` — **Elemental colour shifts**: metal (white), wood (green), water (blue), fire (red), earth (amber) [S] [P0]
- [ ] `MAG-MER-06` — Blocked / damaged meridian state (dull, broken flow) [S] [P1]
- [ ] `MAG-MER-07` — Cultivation-stage overlay intensity: 5 stages of brightness and line count [S] [P1]
- [ ] `MAG-MER-08` — Screen-space and in-world versions of the overlay [D] [P1]
- [ ] `MAG-MER-09` — Readability pass: overlay must survive strong rim lighting and dark districts [D] [P1]

---

## 3. Persona auras (`AUR`) — one per career, 50–100 particles

Hard cap from the brief: **50–100 particles per aura**. Each aura ships with an idle loop, a
combat/intensity boost variant, an off state for low graphics settings, and a rim-light colour
that feeds `TEX-15`.

- [ ] `AUR-CUL` — Cultivator: drifting Qi mist, low-to-ground, jade tint [S] [P0]
- [ ] `AUR-SCH` — Arcane Scholar: orbiting rune motes with faint page glyphs [S] [P0]
- [ ] `AUR-HAC` — Cyber Hacker: pixel glitch motes, scan-line flicker, neon green/blue [S] [P0]
- [ ] `AUR-UDW` — Underworld: low smoke crawl, ash flecks, desaturated [S] [P0]
- [ ] `AUR-INF` — Influencer: floating heart/like sparks, sparkle motes, camera-flash pops [S] [P0]
- [ ] `AUR-HEI` — Corporate Heir: crisp geometric shards, gold flecks, minimal and slow [S] [P0]
- [ ] `AUR-MEC` — Mechanic / Artisan: ember sparks, heat shimmer wisp, soot flecks [S] [P0]
- [ ] `AUR-MIL` — Military / PMC: dust motes, radio-static crackle sparks, muted red [S] [P1]
- [ ] `AUR-POL` — Politician: soft light bloom, confetti motes on success, camera flashes [S] [P1]
- [ ] `AUR-CLT` — Cultist / Secret Society: whispering shadow tendrils, crimson embers [S] [P1]
- [ ] `AUR-SYS-01` — Shared aura master material so all 10 share one shader and one budget governor [D] [P0]
- [ ] `AUR-SYS-02` — Intensity governor: aura particle count scales with cultivation / reputation level within the 50–100 cap [D] [P1]
