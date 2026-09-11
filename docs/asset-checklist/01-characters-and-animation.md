# 01 — Character & animation assets

Covers base meshes, the character creator, textures, wardrobe and the full animation set.
Budget rules and DoD: [00-standards-and-conventions.md](00-standards-and-conventions.md).

**Headline constraint:** assembled character = 3,000–8,000 tris. Base body ≤ 3,500 so wardrobe,
hair and accessories still fit.

---

## 1. Base meshes — 5 body frames

Each frame ships as: skeletal mesh, shared-skeleton rig, 4 LODs + shadow proxy, capsule collision,
morph-target slots for the face, and attachment sockets.

- [ ] `CHR-BODY-01` — Slim frame: `SK_CHR_Base_Slim`, ≤3,200 tris, narrow shoulders, long limb proportion [S] [P0]
- [ ] `CHR-BODY-02` — Athletic frame: `SK_CHR_Base_Athletic`, defined shoulders, standard proportion baseline [S] [P0]
- [ ] `CHR-BODY-03` — Average frame: `SK_CHR_Base_Average`, mid mass, widest wardrobe compatibility [S] [P0]
- [ ] `CHR-BODY-04` — Heavy frame: `SK_CHR_Base_Heavy`, broad torso, wardrobe layers need a widened variant [S] [P0]
- [ ] `CHR-BODY-05` — Tall frame: `SK_CHR_Base_Tall`, +8–12% scale, camera and cover heights re-tuned [S] [P0]
- [ ] `CHR-BASE-01` — Shared master skeleton, identical bone set and naming across all 5 frames [D] [P0]
- [ ] `CHR-BASE-02` — Gender/presentation variants or a single androgynous base with chest/hip morphs — **decision needed, see open questions** [D] [P0]
- [ ] `CHR-BASE-03` — Retarget proof: one animation clip played on all 5 frames with no sliding or clipping [D] [P0]
- [ ] `CHR-BASE-04` — NPC body preset bank (20+ named presets) so crowds are not all identical [D] [P1]
- [ ] `CHR-BASE-05` — Body-type-driven wardrobe refit pass (auto-scale layers for Heavy and Tall) [D] [P1]

---

## 2. Creator morphs — face sliders (41)

Grouped anatomically; each slider needs a morph target on every body frame and a clamped UI range.

### Jaw & chin (5)
- [ ] `CHR-FACE-01` — Jaw width [S] [P0]
- [ ] `CHR-FACE-02` — Jaw angle / squareness [S] [P0]
- [ ] `CHR-FACE-03` — Chin height [S] [P0]
- [ ] `CHR-FACE-04` — Chin protrusion [S] [P0]
- [ ] `CHR-FACE-05` — Chin width / cleft [S] [P0]

### Cheeks (4)
- [ ] `CHR-FACE-06` — Cheekbone height [S] [P0]
- [ ] `CHR-FACE-07` — Cheekbone width [S] [P0]
- [ ] `CHR-FACE-08` — Cheek fullness [S] [P0]
- [ ] `CHR-FACE-09` — Cheek hollow / gauntness [S] [P1]

### Nose (6)
- [ ] `CHR-FACE-10` — Bridge height [S] [P0]
- [ ] `CHR-FACE-11` — Bridge width [S] [P0]
- [ ] `CHR-FACE-12` — Nose length [S] [P0]
- [ ] `CHR-FACE-13` — Tip upturn [S] [P0]
- [ ] `CHR-FACE-14` — Tip width / bulbosity [S] [P1]
- [ ] `CHR-FACE-15` — Nostril size [S] [P1]

### Mouth (5)
- [ ] `CHR-FACE-16` — Upper lip thickness [S] [P0]
- [ ] `CHR-FACE-17` — Lower lip thickness [S] [P0]
- [ ] `CHR-FACE-18` — Mouth width [S] [P0]
- [ ] `CHR-FACE-19` — Mouth vertical position [S] [P1]
- [ ] `CHR-FACE-20` — Philtrum length [S] [P1]

### Eyes & brows (10)
- [ ] `CHR-FACE-21` — Eye size [S] [P0]
- [ ] `CHR-FACE-22` — Eye spacing [S] [P0]
- [ ] `CHR-FACE-23` — Eye depth / socket set [S] [P0]
- [ ] `CHR-FACE-24` — Eye tilt / canthus angle [S] [P0]
- [ ] `CHR-FACE-25` — Upper eyelid fold (monolid ↔ double) [S] [P1]
- [ ] `CHR-FACE-26` — Eyelid openness [S] [P1]
- [ ] `CHR-FACE-27` — Brow height [S] [P0]
- [ ] `CHR-FACE-28` — Brow angle [S] [P0]
- [ ] `CHR-FACE-29` — Brow thickness [S] [P0]
- [ ] `CHR-FACE-30` — Brow inner/outer shape [S] [P1]

### Structure (7)
- [ ] `CHR-FACE-31` — Forehead height [S] [P0]
- [ ] `CHR-FACE-32` — Forehead slope [S] [P1]
- [ ] `CHR-FACE-33` — Face width [S] [P0]
- [ ] `CHR-FACE-34` — Face length [S] [P0]
- [ ] `CHR-FACE-35` — Mid-face ratio (upper/mid/lower thirds) [S] [P1]
- [ ] `CHR-FACE-36` — Ear size [S] [P1]
- [ ] `CHR-FACE-37` — Ear protrusion [S] [P1]

### Age & condition (4)
- [ ] `CHR-FACE-38` — Skin age / wrinkle depth [S] [P1]
- [ ] `CHR-FACE-39` — Brow furrow lines [S] [P2]
- [ ] `CHR-FACE-40` — Nasolabial fold depth [S] [P2]
- [ ] `CHR-FACE-41` — Facial weight / fat distribution [S] [P1]
- [ ] `CHR-FACE-42` — Morph budget check: all 41 targets under the memory and draw-call cap when stacked [D] [P0]

---

## 3. Creator morphs — hairstyles (44) + facial hair (14)

Hair is card-based from `T_CHR_Hair_*`; every style needs LOD1 (half cards), LOD2 (silhouette
proxy) and a physics proxy for long styles.

- [ ] `CHR-HAIR-01` — Buzz cut [S] [P0]
- [ ] `CHR-HAIR-02` — Crew cut [S] [P0]
- [ ] `CHR-HAIR-03` — Fade (low / mid / high variants) [S] [P0]
- [ ] `CHR-HAIR-04` — Undercut [S] [P0]
- [ ] `CHR-HAIR-05` — Textured short crop [S] [P0]
- [ ] `CHR-HAIR-06` — Short curly [S] [P0]
- [ ] `CHR-HAIR-07` — Coily / short afro [S] [P0]
- [ ] `CHR-HAIR-08` — Full afro [S] [P0]
- [ ] `CHR-HAIR-09` — Cornrow braids [S] [P0]
- [ ] `CHR-HAIR-10` — Box braids, shoulder length [S] [P0]
- [ ] `CHR-HAIR-11` — Box braids, long [S] [P1]
- [ ] `CHR-HAIR-12` — Dreadlocks, short [S] [P0]
- [ ] `CHR-HAIR-13` — Dreadlocks, long [S] [P1]
- [ ] `CHR-HAIR-14` — Two-strand twists [S] [P1]
- [ ] `CHR-HAIR-15` — Mohawk [S] [P0]
- [ ] `CHR-HAIR-16` — Faux hawk [S] [P1]
- [ ] `CHR-HAIR-17` — Mullet [S] [P1]
- [ ] `CHR-HAIR-18` — Bowl cut [S] [P1]
- [ ] `CHR-HAIR-19` — Shag [S] [P1]
- [ ] `CHR-HAIR-20` — Wolf cut [S] [P0]
- [ ] `CHR-HAIR-21` — Pixie [S] [P0]
- [ ] `CHR-HAIR-22` — Bob, chin length [S] [P0]
- [ ] `CHR-HAIR-23` — Lob, shoulder length [S] [P0]
- [ ] `CHR-HAIR-24` — Long straight [S] [P0]
- [ ] `CHR-HAIR-25` — Long wavy [S] [P0]
- [ ] `CHR-HAIR-26` — Long curly [S] [P1]
- [ ] `CHR-HAIR-27` — Side part [S] [P0]
- [ ] `CHR-HAIR-28` — Slicked back [S] [P0]
- [ ] `CHR-HAIR-29` — Pompadour [S] [P1]
- [ ] `CHR-HAIR-30` — Quiff [S] [P1]
- [ ] `CHR-HAIR-31` — Blunt fringe / bangs [S] [P0]
- [ ] `CHR-HAIR-32` — Curtain bangs, middle part [S] [P1]
- [ ] `CHR-HAIR-33` — High ponytail [S] [P0]
- [ ] `CHR-HAIR-34` — Low ponytail [S] [P0]
- [ ] `CHR-HAIR-35` — Top knot / bun [S] [P0]
- [ ] `CHR-HAIR-36` — Space buns [S] [P1]
- [ ] `CHR-HAIR-37` — Braided crown / halo braid [S] [P1]
- [ ] `CHR-HAIR-38` — Single side braid [S] [P1]
- [ ] `CHR-HAIR-39` — Twin braids [S] [P1]
- [ ] `CHR-HAIR-40` — Fishtail braid [S] [P2]
- [ ] `CHR-HAIR-41` — Cultivator topknot with hairpin (pairs with `CR-CUL-W*`) [S] [P1]
- [ ] `CHR-HAIR-42` — Long tied-back tail (samurai style) [S] [P1]
- [ ] `CHR-HAIR-43` — Bald / shaved [S] [P0]
- [ ] `CHR-HAIR-44` — Receding / thinning [S] [P1]
- [ ] `CHR-HAIR-45` — Hair physics proxies for all styles longer than shoulder length [D] [P1]
- [ ] `CHR-HAIR-46` — Hair-wet and hair-wind material variants [D] [P2]

### Facial hair (14)
- [ ] `CHR-BRD-01` — Clean shaven [S] [P0]
- [ ] `CHR-BRD-02` — Light stubble [S] [P0]
- [ ] `CHR-BRD-03` — Heavy stubble [S] [P0]
- [ ] `CHR-BRD-04` — Short boxed beard [S] [P0]
- [ ] `CHR-BRD-05` — Full beard [S] [P0]
- [ ] `CHR-BRD-06` — Long beard [S] [P1]
- [ ] `CHR-BRD-07` — Goatee [S] [P0]
- [ ] `CHR-BRD-08` — Circle beard [S] [P1]
- [ ] `CHR-BRD-09` — Moustache [S] [P0]
- [ ] `CHR-BRD-10` — Handlebar moustache [S] [P1]
- [ ] `CHR-BRD-11` — Chinstrap [S] [P1]
- [ ] `CHR-BRD-12` — Sideburns / mutton chops [S] [P1]
- [ ] `CHR-BRD-13` — Soul patch [S] [P2]
- [ ] `CHR-BRD-14` — Braided beard with beads [S] [P2]

---

## 4. Creator morphs — iris patterns (24)

All irises are one mesh with a swappable material; emissive variants feed the persona aura colour.

- [ ] `CHR-EYE-01` — Solid amber [S] [P0]
- [ ] `CHR-EYE-02` — Jade green [S] [P0]
- [ ] `CHR-EYE-03` — Ice blue [S] [P0]
- [ ] `CHR-EYE-04` — Storm grey [S] [P0]
- [ ] `CHR-EYE-05` — Deep violet, arcane [S] [P0]
- [ ] `CHR-EYE-06` — Crimson [S] [P0]
- [ ] `CHR-EYE-07` — Gold fleck [S] [P1]
- [ ] `CHR-EYE-08` — Honey brown with limbal ring [S] [P0]
- [ ] `CHR-EYE-09` — Steel blue, radial striations [S] [P1]
- [ ] `CHR-EYE-10` — Heterochromia, sectoral [S] [P1]
- [ ] `CHR-EYE-11` — Heterochromia, complete [S] [P1]
- [ ] `CHR-EYE-12` — Spiral Qi vortex (animated) [S] [P1]
- [ ] `CHR-EYE-13` — Rune-etched sigil [S] [P1]
- [ ] `CHR-EYE-14` — Cyber scan-ring (animated) [S] [P1]
- [ ] `CHR-EYE-15` — Vertical slit pupil, beast [S] [P1]
- [ ] `CHR-EYE-16` — Cat slit pupil [S] [P1]
- [ ] `CHR-EYE-17` — Starfield [S] [P2]
- [ ] `CHR-EYE-18` — Nebula swirl [S] [P2]
- [ ] `CHR-EYE-19` — Fractured glass [S] [P2]
- [ ] `CHR-EYE-20` — Molten ember (emissive) [S] [P1]
- [ ] `CHR-EYE-21` — Frost crystal [S] [P2]
- [ ] `CHR-EYE-22` — Oil-slick iridescent [S] [P2]
- [ ] `CHR-EYE-23` — Void black [S] [P1]
- [ ] `CHR-EYE-24` — Bioluminescent ring (emissive) [S] [P1]

---

## 5. Full colour spectrums

- [ ] `CHR-CLR-01` — Skin tone ramp: 24 swatches across Fitzpatrick I–VI plus fantasy tints (ashen, jade, bronze-gold) [S] [P0]
- [ ] `CHR-CLR-02` — Natural hair ramp: 20 swatches, black → platinum, incl. greying gradient [S] [P0]
- [ ] `CHR-CLR-03` — Fantasy hair ramp: 24 swatches, neon and elemental [S] [P1]
- [ ] `CHR-CLR-04` — Eye colour ramp bound to the 24 iris patterns [S] [P0]
- [ ] `CHR-CLR-05` — Tattoo / scar ink ramp (8 inks incl. emissive Qi ink) [S] [P1]
- [ ] `CHR-CLR-06` — Wardrobe fabric dye ramp, driven by the tint mask R/G channels [S] [P0]
- [ ] `CHR-CLR-07` — Metal & trim ramp (steel, brass, chrome, blackened, jade-inlaid) [S] [P1]
- [ ] `CHR-CLR-08` — Emissive accent ramp tied to persona aura colour (tint mask A channel) [S] [P0]
- [ ] `CHR-CLR-09` — Colourblind-safe validation pass on all UI-facing ramps [D] [P2]

---

## 6. Scar & tattoo patterns (18)

Decal system: projected onto the body at runtime from `T_CHR_Decal_Atlas`, positioned by the
creator, tinted by `CHR-CLR-05`.

- [ ] `CHR-DECAL-01` — Sect brand, cheek [S] [P0]
- [ ] `CHR-DECAL-02` — Ritual scarification lines [S] [P0]
- [ ] `CHR-DECAL-03` — Duel scar across the eye [S] [P0]
- [ ] `CHR-DECAL-04` — Burn scar [S] [P0]
- [ ] `CHR-DECAL-05` — Claw marks, three-strip [S] [P0]
- [ ] `CHR-DECAL-06` — Blade slash, torso [S] [P1]
- [ ] `CHR-DECAL-07` — Circuit-trace tattoo, arm [S] [P0]
- [ ] `CHR-DECAL-08` — Runic script sleeve [S] [P1]
- [ ] `CHR-DECAL-09` — Tribal band, upper arm [S] [P0]
- [ ] `CHR-DECAL-10` — Lotus / koi ink [S] [P1]
- [ ] `CHR-DECAL-11` — Barcode, neck [S] [P1]
- [ ] `CHR-DECAL-12` — Gang sigil [S] [P0]
- [ ] `CHR-DECAL-13` — Meridian map tattoo, torso (ties to `MAG-MER-*`) [S] [P1]
- [ ] `CHR-DECAL-14` — Qi circuitry, emissive variant [S] [P1]
- [ ] `CHR-DECAL-15` — Tribal face paint [S] [P1]
- [ ] `CHR-DECAL-16` — Alchemical sigil, hand [S] [P2]
- [ ] `CHR-DECAL-17` — Spine-line tattoo [S] [P2]
- [ ] `CHR-DECAL-18` — Cultist branding mark (ties to `CR-CLT-W*`) [S] [P1]
- [ ] `CHR-DECAL-19` — Runtime decal projection system: scale, rotation, mirror, layering limit [D] [P0]

---

## 7. Textures & shading

- [ ] `TEX-01` — 1024 face albedo, `T_CHR_Face_A` [S] [P0]
- [ ] `TEX-02` — 1024 face normal with wrinkle/pore detail [S] [P0]
- [ ] `TEX-03` — 1024 face ORM (occlusion / roughness / metallic packed) [S] [P0]
- [ ] `TEX-04` — 1024 face **grayscale tint mask**, R/G/B/A per the standard channel convention [S] [P0]
- [ ] `TEX-05` — 1024 body albedo, all 5 frames [S] [P0]
- [ ] `TEX-06` — 1024 body normal [S] [P0]
- [ ] `TEX-07` — 1024 body ORM [S] [P0]
- [ ] `TEX-08` — 512–1024 wardrobe atlas A (torso / legs) + tint mask [S] [P0]
- [ ] `TEX-09` — 512–1024 wardrobe atlas B (head / hands / feet) + tint mask [S] [P0]
- [ ] `TEX-10` — **512×512 accessory atlas, one per career** (10 atlases) — shared by every pouch, pendant and holster in that career [S] [P0]
- [ ] `TEX-11` — 512 scar/tattoo decal atlas with alpha + tint mask [S] [P0]
- [ ] `TEX-12` — 512 hair atlas: strand alpha + root/tip gradient mask [S] [P0]
- [ ] `TEX-13` — **Subsurface scattering skin shader**: SSS profile, curvature, tuned translucency [S] [P0]
- [ ] `TEX-14` — SSS thickness map (ears, nose, fingers, thin cloth) [S] [P0]
- [ ] `TEX-15` — **Edge rim lighting**: fresnel mask + per-persona rim colour parameter [S] [P0]
- [ ] `TEX-16` — Emissive mask for implants, irises and Qi tattoos [S] [P0]
- [ ] `TEX-17` — 64/128 inventory icon set for wardrobe and accessories [D] [P1]
- [ ] `TEX-18` — Tiled detail normal (pore, fabric weave, metal brush) [D] [P1]
- [ ] `TEX-19` — Wet / dirty / bloodied overlay set applied over the base maps [D] [P1]
- [ ] `TEX-20` — 128 UI portrait renders per body frame for dialogue cards [D] [P1]
- [ ] `TEX-21` — Atlas utilisation audit: no career atlas under 60% coverage, none over budget [D] [P1]

---

## 8. Wardrobe system

Modular layers on named sockets — never welded. Eight layers visible max, all inside the 8,000-tri cap.

- [ ] `WRD-01` — Layer 1: base underlayer [S] [P0]
- [ ] `WRD-02` — Layer 2: mid layer (shirt / tunic) [S] [P0]
- [ ] `WRD-03` — Layer 3: outer layer (jacket / coat / robe) [S] [P0]
- [ ] `WRD-04` — Layer 4: head (hat / hood / helmet) [S] [P0]
- [ ] `WRD-05` — Layer 5: feet [S] [P0]
- [ ] `WRD-06` — Layer 6: hands / gloves [S] [P0]
- [ ] `WRD-07` — Layer 7: belt & waist accessories [S] [P0]
- [ ] `WRD-08` — Layer 8: back (cape / backpack / scabbard) [S] [P1]
- [ ] `WRD-09` — Neck accessory slot (pendants, ties, scarves) [S] [P1]
- [ ] `WRD-10` — Wrist / ring / bracer slot [S] [P1]
- [ ] `WRD-11` — Cybernetic **mechanical arm, left** with exposed servo detail [S] [P0]
- [ ] `WRD-12` — Cybernetic **mechanical arm, right** [S] [P0]
- [ ] `WRD-13` — **Neural glow** cranial ports, emissive and pulsing [S] [P0]
- [ ] `WRD-14` — Ocular implant (ties to `CHR-EYE-14`) [S] [P1]
- [ ] `WRD-15` — Spinal interface port [S] [P1]
- [ ] `WRD-16` — Exoskeleton leg brace [S] [P1]
- [ ] `WRD-17` — Cyber hand / data glove [S] [P1]
- [ ] `WRD-18` — Subdermal glow lines, emissive body decal [S] [P2]
- [ ] `WRD-19` — **Attachment socket standard**: named sockets, zero baked transforms, one socket per accessory [D] [P0]
- [ ] `WRD-20` — Career outfit presets — 10 careers, cross-referenced from [05-career-paths.md](05-career-paths.md) [S] [P0]
- [ ] `WRD-21` — Condition variants per outfit: clean / worn / torn / bloodied [D] [P1]
- [ ] `WRD-22` — Formal / casual / combat variant set for each career [D] [P1]
- [ ] `WRD-23` — Clothing physics proxies on cloaks, capes and robes [D] [P1]
- [ ] `WRD-24` — Auto-hide rules (long hair vs. hood, gloves vs. hand implants) to stop clipping [D] [P1]

---

## 9. Animation — locomotion (20)

- [ ] `ANM-LOC-01` — Idle, breathing loop + 2 fidget variants [S] [P0]
- [ ] `ANM-LOC-02` — Walk 8-directional (F / B / L / R + diagonals), root motion [S] [P0]
- [ ] `ANM-LOC-03` — Run 8-directional [S] [P0]
- [ ] `ANM-LOC-04` — Sprint + sprint-to-stop [S] [P0]
- [ ] `ANM-LOC-05` — Crouch idle + crouch walk [S] [P0]
- [ ] `ANM-LOC-06` — Prone idle + prone crawl [S] [P1]
- [ ] `ANM-LOC-07` — Jump: start / air loop / land (light + heavy) [S] [P0]
- [ ] `ANM-LOC-08` — Fall loop, long fall variant [S] [P0]
- [ ] `ANM-LOC-09` — Swim: idle tread + stroke [S] [P1]
- [ ] `ANM-LOC-10` — Vault / climb low obstacle [S] [P1]
- [ ] `ANM-LOC-11` — Turn in place, 90° and 180° [D] [P0]
- [ ] `ANM-LOC-12` — Stop and pivot blends [D] [P0]
- [ ] `ANM-LOC-13` — Stumble / knockdown / recover [S] [P0]
- [ ] `ANM-LOC-14` — Strafe and sidestep set for combat facing [S] [P0]
- [ ] `ANM-LOC-15` — Sit / stand (bench, chair, floor, meditation) [S] [P1]
- [ ] `ANM-LOC-16` — Lean against wall, casual idle [S] [P2]
- [ ] `ANM-LOC-17` — Carry states: empty / light / two-handed / dragging [D] [P1]
- [ ] `ANM-LOC-18` — Wounded locomotion layers (limp, clutch side), additive [D] [P1]
- [ ] `ANM-LOC-19` — Crowding / bump reactions for dense NPC districts [D] [P2]
- [ ] `ANM-LOC-20` — Anim blueprint: blend spaces, state machine and foot IK across all 5 body frames [D] [P0]

---

## 10. Animation — melee movesets (6 weapon classes × 11)

One block per weapon class. Each block ships with its montage, hit-window notifies, footstep
notifies, VFX and SFX cues. Classes: **fists, daggers, swords, greatswords, blunt, polearms**.

### Fists / gauntlets (`FST`)
- [ ] `ANM-MEL-FST-01` — Combat stance / idle [S] [P0]
- [ ] `ANM-MEL-FST-02` — Guard up / guard down [S] [P0]
- [ ] `ANM-MEL-FST-03` — Light combo, 3-hit chain [S] [P0]
- [ ] `ANM-MEL-FST-04` — Heavy attack (haymaker / palm strike) [S] [P0]
- [ ] `ANM-MEL-FST-05` — Block / cover-up [S] [P0]
- [ ] `ANM-MEL-FST-06` — Parry + riposte [S] [P1]
- [ ] `ANM-MEL-FST-07` — Dodge / slip [S] [P0]
- [ ] `ANM-MEL-FST-08` — Hit reactions, light and heavy (additive) [S] [P0]
- [ ] `ANM-MEL-FST-09` — Death, 2 variants [S] [P0]
- [ ] `ANM-MEL-FST-10` — Special / finisher [S] [P1]
- [ ] `ANM-MEL-FST-11` — Sprint attack + air attack [D] [P1]

### Daggers (`DAG`)
- [ ] `ANM-MEL-DAG-01` — Combat stance / idle [S] [P0]
- [ ] `ANM-MEL-DAG-02` — Draw and sheathe (quick-draw for stealth) [S] [P0]
- [ ] `ANM-MEL-DAG-03` — Light combo, 3-hit chain [S] [P0]
- [ ] `ANM-MEL-DAG-04` — Heavy attack (lunging stab) [S] [P0]
- [ ] `ANM-MEL-DAG-05` — Block / deflection [S] [P0]
- [ ] `ANM-MEL-DAG-06` — Parry + riposte [S] [P1]
- [ ] `ANM-MEL-DAG-07` — Dodge / roll [S] [P0]
- [ ] `ANM-MEL-DAG-08` — Hit reactions, light and heavy [S] [P0]
- [ ] `ANM-MEL-DAG-09` — Death, 2 variants [S] [P0]
- [ ] `ANM-MEL-DAG-10` — Stealth takedown from behind [S] [P0]
- [ ] `ANM-MEL-DAG-11` — Sprint attack + air attack [D] [P1]

### Swords (`SWD`)
- [ ] `ANM-MEL-SWD-01` — Combat stance / idle [S] [P0]
- [ ] `ANM-MEL-SWD-02` — Draw and sheathe [S] [P0]
- [ ] `ANM-MEL-SWD-03` — Light combo, 3-hit chain [S] [P0]
- [ ] `ANM-MEL-SWD-04` — Heavy attack (overhead cleave) [S] [P0]
- [ ] `ANM-MEL-SWD-05` — Block / guard [S] [P0]
- [ ] `ANM-MEL-SWD-06` — Parry + riposte [S] [P0]
- [ ] `ANM-MEL-SWD-07` — Dodge / sidestep [S] [P0]
- [ ] `ANM-MEL-SWD-08` — Hit reactions, light and heavy [S] [P0]
- [ ] `ANM-MEL-SWD-09` — Death, 2 variants [S] [P0]
- [ ] `ANM-MEL-SWD-10` — Special / finisher [S] [P1]
- [ ] `ANM-MEL-SWD-11` — Sprint attack + air attack [D] [P1]

### Greatswords (`GSW`)
- [ ] `ANM-MEL-GSW-01` — Combat stance / idle (two-handed carry) [S] [P0]
- [ ] `ANM-MEL-GSW-02` — Shouldering and unshouldering [S] [P1]
- [ ] `ANM-MEL-GSW-03` — Light combo, 3-hit chain (slow, committed) [S] [P0]
- [ ] `ANM-MEL-GSW-04` — Heavy attack (ground slam) [S] [P0]
- [ ] `ANM-MEL-GSW-05` — Block / guard, stagger-resistant [S] [P0]
- [ ] `ANM-MEL-GSW-06` — Parry + riposte (armour-breaking) [S] [P1]
- [ ] `ANM-MEL-GSW-07` — Dodge (heavy step, no roll) [S] [P0]
- [ ] `ANM-MEL-GSW-08` — Hit reactions, light and heavy [S] [P0]
- [ ] `ANM-MEL-GSW-09` — Death, 2 variants [S] [P0]
- [ ] `ANM-MEL-GSW-10` — Special / finisher (wide sweep) [S] [P1]
- [ ] `ANM-MEL-GSW-11` — Sprint attack + air attack [D] [P1]

### Blunt (`BLT` — maces, hammers, clubs)
- [ ] `ANM-MEL-BLT-01` — Combat stance / idle [S] [P0]
- [ ] `ANM-MEL-BLT-02` — Draw and sheathe / stow [S] [P0]
- [ ] `ANM-MEL-BLT-03` — Light combo, 3-hit chain [S] [P0]
- [ ] `ANM-MEL-BLT-04` — Heavy attack (crushing overhead) [S] [P0]
- [ ] `ANM-MEL-BLT-05` — Block / guard [S] [P0]
- [ ] `ANM-MEL-BLT-06` — Parry + stagger riposte [S] [P1]
- [ ] `ANM-MEL-BLT-07` — Dodge / roll [S] [P0]
- [ ] `ANM-MEL-BLT-08` — Hit reactions, light and heavy [S] [P0]
- [ ] `ANM-MEL-BLT-09` — Death, 2 variants [S] [P0]
- [ ] `ANM-MEL-BLT-10` — Special / finisher (armour crush) [S] [P1]
- [ ] `ANM-MEL-BLT-11` — Sprint attack + air attack [D] [P1]

### Polearms (`POL` — spears, glaives, staves)
- [ ] `ANM-MEL-POL-01` — Combat stance / idle (reach advantage) [S] [P0]
- [ ] `ANM-MEL-POL-02` — Draw and stow (shaft collapse or sling) [S] [P1]
- [ ] `ANM-MEL-POL-03` — Light combo, 3-hit chain (thrusts) [S] [P0]
- [ ] `ANM-MEL-POL-04` — Heavy attack (sweep) [S] [P0]
- [ ] `ANM-MEL-POL-05` — Block / shaft guard [S] [P0]
- [ ] `ANM-MEL-POL-06` — Parry + riposte [S] [P1]
- [ ] `ANM-MEL-POL-07` — Dodge / backstep [S] [P0]
- [ ] `ANM-MEL-POL-08` — Hit reactions, light and heavy [S] [P0]
- [ ] `ANM-MEL-POL-09` — Death, 2 variants [S] [P0]
- [ ] `ANM-MEL-POL-10` — Special / finisher (spinning sweep) [S] [P1]
- [ ] `ANM-MEL-POL-11` — Sprint attack + air attack [D] [P1]
- [ ] `ANM-MEL-POL-12` — Shared weapon socket set and grip IK for all 6 classes [D] [P0]

---

## 11. Animation — 6 martial arts styles (6 × 6)

Six distinct unarmed styles. Style 1 is named in the brief (Wing Chun, via the Cultivator's
wooden dummy). **Styles 2–6 are unnamed in the brief — placeholder codes until design locks them.**

### Style 1 — Wing Chun (`MA1`)
- [ ] `ANM-MA-MA1-01` — Stance / idle, centre-line guard [S] [P0]
- [ ] `ANM-MA-MA1-02` — Chain-punch 3-hit combo [S] [P0]
- [ ] `ANM-MA-MA1-03` — Low kick / stamp kick [S] [P1]
- [ ] `ANM-MA-MA1-04` — Deflect and trap (pak sao / lop sao) [S] [P0]
- [ ] `ANM-MA-MA1-05` — Throw / grapple [S] [P1]
- [ ] `ANM-MA-MA1-06` — Special: wooden-dummy drill sequence [S] [P1]

### Style 2 — name TBD (`MA2`)
- [ ] `ANM-MA-MA2-01` — Stance / idle [S] [P1]
- [ ] `ANM-MA-MA2-02` — 3-hit combo [S] [P1]
- [ ] `ANM-MA-MA2-03` — Kick set [S] [P1]
- [ ] `ANM-MA-MA2-04` — Block / deflection set [S] [P1]
- [ ] `ANM-MA-MA2-05` — Throw / grapple [S] [P1]
- [ ] `ANM-MA-MA2-06` — Special [S] [P2]

### Style 3 — name TBD (`MA3`)
- [ ] `ANM-MA-MA3-01` — Stance / idle [S] [P1]
- [ ] `ANM-MA-MA3-02` — 3-hit combo [S] [P1]
- [ ] `ANM-MA-MA3-03` — Kick set [S] [P1]
- [ ] `ANM-MA-MA3-04` — Block / deflection set [S] [P1]
- [ ] `ANM-MA-MA3-05` — Throw / grapple [S] [P1]
- [ ] `ANM-MA-MA3-06` — Special [S] [P2]

### Style 4 — name TBD (`MA4`)
- [ ] `ANM-MA-MA4-01` — Stance / idle [S] [P1]
- [ ] `ANM-MA-MA4-02` — 3-hit combo [S] [P1]
- [ ] `ANM-MA-MA4-03` — Kick set [S] [P1]
- [ ] `ANM-MA-MA4-04` — Block / deflection set [S] [P1]
- [ ] `ANM-MA-MA4-05` — Throw / grapple [S] [P1]
- [ ] `ANM-MA-MA4-06` — Special [S] [P2]

### Style 5 — name TBD (`MA5`)
- [ ] `ANM-MA-MA5-01` — Stance / idle [S] [P1]
- [ ] `ANM-MA-MA5-02` — 3-hit combo [S] [P1]
- [ ] `ANM-MA-MA5-03` — Kick set [S] [P1]
- [ ] `ANM-MA-MA5-04` — Block / deflection set [S] [P1]
- [ ] `ANM-MA-MA5-05` — Throw / grapple [S] [P1]
- [ ] `ANM-MA-MA5-06` — Special [S] [P2]

### Style 6 — name TBD (`MA6`)
- [ ] `ANM-MA-MA6-01` — Stance / idle [S] [P1]
- [ ] `ANM-MA-MA6-02` — 3-hit combo [S] [P1]
- [ ] `ANM-MA-MA6-03` — Kick set [S] [P1]
- [ ] `ANM-MA-MA6-04` — Block / deflection set [S] [P1]
- [ ] `ANM-MA-MA6-05` — Throw / grapple [S] [P1]
- [ ] `ANM-MA-MA6-06` — Special [S] [P2]
- [ ] `ANM-MA-MA6-07` — Style-switch blend layer so a character can hold two styles [D] [P2]

---

## 12. Animation — tactical (26)

- [ ] `ANM-TAC-01` — Enter low cover [S] [P0]
- [ ] `ANM-TAC-02` — Enter high cover [S] [P0]
- [ ] `ANM-TAC-03` — Exit cover (back, left, right, vault) [S] [P0]
- [ ] `ANM-TAC-04` — Cover peek left / right [S] [P0]
- [ ] `ANM-TAC-05` — Cover blind fire [S] [P1]
- [ ] `ANM-TAC-06` — Cover reposition (slide along wall) [S] [P1]
- [ ] `ANM-TAC-07` — Aim down sights, per-stance (stand / crouch / prone) [S] [P0]
- [ ] `ANM-TAC-08` — Aim sway and recoil recovery layer, additive [S] [P0]
- [ ] `ANM-TAC-09` — Reload — pistol (`PST`) [S] [P0]
- [ ] `ANM-TAC-10` — Reload — SMG (`SMG`) [S] [P0]
- [ ] `ANM-TAC-11` — Reload — shotgun (`SHG`, shell by shell) [S] [P0]
- [ ] `ANM-TAC-12` — Reload — rifle (`RIF`) [S] [P0]
- [ ] `ANM-TAC-13` — Reload — marksman rifle (`DMR`) [S] [P0]
- [ ] `ANM-TAC-14` — Reload — sniper (`SNP`, bolt cycle) [S] [P0]
- [ ] `ANM-TAC-15` — Tactical (partial mag) reload variant per class [D] [P1]
- [ ] `ANM-TAC-16` — Malfunction / clear jam [S] [P1]
- [ ] `ANM-TAC-17` — Draw and holster sidearm [S] [P0]
- [ ] `ANM-TAC-18` — Weapon swap (primary ↔ sidearm ↔ melee) [S] [P0]
- [ ] `ANM-TAC-19` — Grenade throw, overhand [S] [P0]
- [ ] `ANM-TAC-20` — Grenade throw, underhand / roll [S] [P1]
- [ ] `ANM-TAC-21` — Plant breaching charge [S] [P1]
- [ ] `ANM-TAC-22` — Stealth takedown (standing and crouched) [S] [P0]
- [ ] `ANM-TAC-23` — Suppressed-fire bracing and follow-through [S] [P1]
- [ ] `ANM-TAC-24` — Weapon inspect / cleaning loop (pairs with `CR-MIL-T05`) [D] [P2]
- [ ] `ANM-TAC-25` — Body drag / carry unconscious NPC [D] [P2]
- [ ] `ANM-TAC-26` — Cover and stance anim blueprint with detection-ring hooks (see `CR-UDW-V02`) [D] [P0]

---

## 13. Animation — crafting & interaction (31)

Tactile, close-camera motions. Every one must read at first-person distance and sync to a
workstation socket.

- [ ] `ANM-CRF-01` — Forge: hammer strike, light loop [S] [P0]
- [ ] `ANM-CRF-02` — Forge: hammer strike, heavy (timed hit) [S] [P0]
- [ ] `ANM-CRF-03` — Forge: quench in trough (steam burst) [S] [P0]
- [ ] `ANM-CRF-04` — Forge: bellows / stoke fire [S] [P1]
- [ ] `ANM-CRF-05` — Forge: sharpen on whetstone [S] [P0]
- [ ] `ANM-CRF-06` — Forge: tong lift and place billet [S] [P1]
- [ ] `ANM-CRF-07` — Alchemy: stir cauldron loop [S] [P0]
- [ ] `ANM-CRF-08` — Alchemy: grind with pestle and mortar [S] [P0]
- [ ] `ANM-CRF-09` — Alchemy: add reagent (pinch / pour / drop) [S] [P0]
- [ ] `ANM-CRF-10` — Alchemy: adjust distillation coil valves [S] [P1]
- [ ] `ANM-CRF-11` — Alchemy: bottle and cork finished potion [S] [P1]
- [ ] `ANM-CRF-12` — Kitchen: chop on cutting board (3 speeds) [S] [P0]
- [ ] `ANM-CRF-13` — Kitchen: work the stove (stir, flip, plate) [S] [P0]
- [ ] `ANM-CRF-14` — Kitchen: season / garnish finish [S] [P2]
- [ ] `ANM-CRF-15` — Enchanting: trace rune in the circle, standing loop [S] [P0]
- [ ] `ANM-CRF-16` — Enchanting: channel and release burst [S] [P0]
- [ ] `ANM-CRF-17` — Tech: solder with iron [S] [P0]
- [ ] `ANM-CRF-18` — Tech: type on cyberdeck, loop + success flourish [S] [P0]
- [ ] `ANM-CRF-19` — Tech: strip and salvage components [S] [P1]
- [ ] `ANM-CRF-20` — Mechanic: wrench torque loop + hydraulic press lever [S] [P0]
- [ ] `ANM-CRF-21` — Mechanic: blowtorch weld [S] [P0]
- [ ] `ANM-CRF-22` — Lockpick: tension wrench + pick, with feedback jiggle [S] [P0]
- [ ] `ANM-CRF-23` — Meditation: seated loop, cross-legged (Qi gathering) [S] [P0]
- [ ] `ANM-CRF-24` — Spell gesture draw, one per shape (6 — pairs with `MAG-SHP-*`) [S] [P0]
- [ ] `ANM-CRF-25` — Harvest: herb / plant pick [S] [P0]
- [ ] `ANM-CRF-26` — Harvest: chop tree (axe loop + fell) [S] [P0]
- [ ] `ANM-CRF-27` — Harvest: mine ore (pick swing + chip) [S] [P0]
- [ ] `ANM-CRF-28` — Harvest: fish (cast, wait idle, reel, land) [S] [P0]
- [ ] `ANM-CRF-29` — Harvest: tech salvage (pry open, extract) [S] [P0]
- [ ] `ANM-CRF-30` — Grimoire: open, page turn, close (physical 3D book) [S] [P0]
- [ ] `ANM-CRF-31` — Generic: sit at desk, inspect item (turntable), eat, drink, hand over item [D] [P1]

---

## 14. Animation — vehicles (17)

One mount/dismount pair per vehicle class plus the ride pose.

- [ ] `ANM-VEH-01` — Mount / dismount — bicycle [S] [P0]
- [ ] `ANM-VEH-02` — Mount / dismount — motorcycle [S] [P0]
- [ ] `ANM-VEH-03` — Mount / dismount — sedan / SUV / van (shared car set) [S] [P0]
- [ ] `ANM-VEH-04` — Mount / dismount — sports car (low entry) [S] [P1]
- [ ] `ANM-VEH-05` — Mount / dismount — boat [S] [P1]
- [ ] `ANM-VEH-06` — Mount / dismount — flying sword (step-on hover) [S] [P0]
- [ ] `ANM-VEH-07` — Mount / dismount — magic broom [S] [P1]
- [ ] `ANM-VEH-08` — Mount / dismount — Qi cloud [S] [P1]
- [ ] `ANM-VEH-09` — Ride pose — bicycle pedalling + lean [S] [P0]
- [ ] `ANM-VEH-10` — Ride pose — motorcycle, lean into turns [S] [P0]
- [ ] `ANM-VEH-11` — Drive pose — seated, hands on wheel + steering blend [S] [P0]
- [ ] `ANM-VEH-12` — Drive pose — passenger variant [D] [P1]
- [ ] `ANM-VEH-13` — Pilot pose — boat at the helm [S] [P1]
- [ ] `ANM-VEH-14` — Ride pose — flying sword stance, balance sway [S] [P0]
- [ ] `ANM-VEH-15` — Ride pose — broom, seated forward + cape physics [S] [P1]
- [ ] `ANM-VEH-16` — Ride pose — Qi cloud, floating lotus [S] [P1]
- [ ] `ANM-VEH-17` — Crash / eject reaction + hit-by-vehicle ragdoll [D] [P1]

---

## 15. Animation — face & emotes (12)

- [ ] `ANM-FAC-01` — Viseme lip-sync set (15 shapes) for dialogue [S] [P1]
- [ ] `ANM-FAC-02` — Blink and saccade / eye aim IK [S] [P1]
- [ ] `ANM-FAC-03` — Expression blendshapes: 8 emotions × 3 intensities [S] [P1]
- [ ] `ANM-FAC-04` — Portrait capture rig for dialogue cards (see `UI-*`) [D] [P1]
- [ ] `ANM-FAC-05` — Emote: wave [S] [P1]
- [ ] `ANM-FAC-06` — Emote: point / direct [S] [P1]
- [ ] `ANM-FAC-07` — Emote: laugh [S] [P1]
- [ ] `ANM-FAC-08` — Emote: cheer / celebrate [S] [P1]
- [ ] `ANM-FAC-09` — Emote: bow / salute (career-flavoured) [S] [P1]
- [ ] `ANM-FAC-10` — Emote: dance ×3 (club / stream / victory) [S] [P2]
- [ ] `ANM-FAC-11` — Emote: pose for camera (Influencer) [D] [P2]
- [ ] `ANM-FAC-12` — Emote wheel UI hook + per-career emote set assignment [D] [P2]

---

## 16. Rig & animation tech (10)

- [ ] `ANM-RIG-01` — Master skeleton with LOD bone reduction and consistent naming [D] [P0]
- [ ] `ANM-RIG-02` — Retarget chain proven across all 5 base body frames [D] [P0]
- [ ] `ANM-RIG-03` — IK solvers: foot placement, two-handed weapon grip, look-at [D] [P0]
- [ ] `ANM-RIG-04` — Physics assets: hair, cloth (capes/robes), straps and cords [D] [P1]
- [ ] `ANM-RIG-05` — Facial rig: blendshape set + control board, shared by all frames [D] [P1]
- [ ] `ANM-RIG-06` — Additive layer slots: breathing, hit react, aim sway, wounded [D] [P0]
- [ ] `ANM-RIG-07` — Root motion authored and audited (no in-place locomotion) [D] [P0]
- [ ] `ANM-RIG-08` — Ragdoll setup per body frame + weapon drop physics [D] [P1]
- [ ] `ANM-RIG-09` — Socket map: weapons, accessories, vehicle seats, workstation poses [D] [P0]
- [ ] `ANM-RIG-10` — Animation budget audit: montage memory and per-frame update cost in a crowded district [D] [P1]
