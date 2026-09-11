# 03 — Crafting & combat props

Workstations, raw materials and the weapon arsenal. Every station here is the *full* hero
version; the portable property versions live in `INT-FUR-F*` (02-world-and-environment.md).

---

## 1. Crafting workstations

Each station ships with: hero mesh + LOD, interactive highlight, a synced character pose
(from `ANM-CRF`), VFX (heat / steam / glow), audio loop, success and failure states.

### Blacksmith forge (`CFT-FRG`)
- [ ] `CFT-FRG-01` — **Anvil**: hero mesh, worn top face, hot-metal contact scorch decal [S] [P0]
- [ ] `CFT-FRG-02` — **Quench trough**: water volume, steam burst on quench, ripple [S] [P0]
- [ ] `CFT-FRG-03` — **Whetstone**: sharpening rig, spark and slurry VFX [S] [P0]
- [ ] `CFT-FRG-04` — Forge fire: ember bed, animated flame, bellows-driven intensity [S] [P0]
- [ ] `CFT-FRG-05` — Bellows: articulated mesh with pump interaction [D] [P1]
- [ ] `CFT-FRG-06` — Tong and hammer rest, billet rack, finished-work quench rack [D] [P1]
- [ ] `CFT-FRG-07` — Heat distortion and rising ember particle system [D] [P0]
- [ ] `CFT-FRG-08` — Timed-hit mini-game feedback: hot-zone glow on the workpiece [D] [P0]

### Alchemy lab (`CFT-ALC`)
- [ ] `CFT-ALC-01` — **Cauldron**: liquid surface shader, colour shifts by reagent mix [S] [P0]
- [ ] `CFT-ALC-02` — **Pestle and mortar**: grinding rig, powder VFX [S] [P0]
- [ ] `CFT-ALC-03` — **Distillation coils**: glass coil set, bubbling flow, condensation drip [S] [P0]
- [ ] `CFT-ALC-04` — Burner / spirit lamp with adjustable flame [S] [P0]
- [ ] `CFT-ALC-05` — Reagent shelf with labelled vials and jars (reads from the material list) [D] [P1]
- [ ] `CFT-ALC-06` — Bottling station: empty vials, corks, filled-potion display [D] [P1]
- [ ] `CFT-ALC-07` — Reaction VFX: successful brew glow, failure smoke and splatter [D] [P0]
- [ ] `CFT-ALC-08` — Balance / scale prop for recipe weighing [D] [P2]

### Kitchen (`CFT-KIT`)
- [ ] `CFT-KIT-01` — **Cutting board**: knife contact, chopped-ingredient decals [S] [P0]
- [ ] `CFT-KIT-02` — **Stove**: burner rings, flame or induction variants, pot and pan support [S] [P0]
- [ ] `CFT-KIT-03` — Cookware set: pot, pan, wok, ladle, spatula [S] [P1]
- [ ] `CFT-KIT-04` — Spice rack and ingredient bins [D] [P1]
- [ ] `CFT-KIT-05` — Plating station with finished-dish display sockets [D] [P1]
- [ ] `CFT-KIT-06` — Steam, sizzle and char VFX plus cooking audio loop [D] [P0]
- [ ] `CFT-KIT-07` — Burnt-failure state: scorched pot mesh and smoke [D] [P1]

### Enchanting circle (`CFT-ENC`)
- [ ] `CFT-ENC-01` — Floor rune circle: emissive decal, rotating ring layers [S] [P0]
- [ ] `CFT-ENC-02` — Pedestal set (3–5) with focus-object sockets [S] [P0]
- [ ] `CFT-ENC-03` — Central focus: floating crystal / orb with charge states [S] [P1]
- [ ] `CFT-ENC-04` — Candle or crystal ring for the perimeter [D] [P1]
- [ ] `CFT-ENC-05` — Channeling VFX: beam from caster to focus, rune ignition sequence [D] [P0]
- [ ] `CFT-ENC-06` — Success burst and overload-failure VFX [D] [P0]
- [ ] `CFT-ENC-07` — Portable / property version of the circle (cross-ref `INT-FUR-F06`) [D] [P1]

---

## 2. Raw materials

Six families. Every material ships with: 3D pickup model (≤300 tris), 64/128 inventory icon,
5 quality tiers, and an economy data entry — no hard-coded values in the asset.

### Botanical herbs (`RAW-HERB`)
- [ ] `RAW-HERB-01` — Healing leaf cluster [S] [P0]
- [ ] `RAW-HERB-02` — Spirit-root bulb [S] [P0]
- [ ] `RAW-HERB-03` — Blood-petal flower [S] [P0]
- [ ] `RAW-HERB-04` — Frost moss [S] [P1]
- [ ] `RAW-HERB-05` — Embercap mushroom [S] [P1]
- [ ] `RAW-HERB-06` — Moonvine tendril [S] [P1]
- [ ] `RAW-HERB-07` — Common cooking herb bundle [D] [P1]

### Animal cores & meats (`RAW-ANIM`)
- [ ] `RAW-ANIM-01` — Beast core (glowing organ, 5 rarity tints) [S] [P0]
- [ ] `RAW-ANIM-02` — Spirit beast core (emissive, animated pulse) [S] [P1]
- [ ] `RAW-ANIM-03` — Raw meat cuts, 3 varieties [S] [P0]
- [ ] `RAW-ANIM-04` — Hide / pelt, rolled [S] [P1]
- [ ] `RAW-ANIM-05` — Bone and horn set [S] [P1]
- [ ] `RAW-ANIM-06` — Fish catch models (ties to `INT-HRV-04`) [S] [P0]

### Mineral chunks (`RAW-MIN`)
- [ ] `RAW-MIN-01` — Iron ore chunk [S] [P0]
- [ ] `RAW-MIN-02` — Steel ingot [S] [P0]
- [ ] `RAW-MIN-03` — Jade chunk (polished and raw states) [S] [P0]
- [ ] `RAW-MIN-04` — Spirit crystal shard [S] [P1]
- [ ] `RAW-MIN-05` — Coal / fuel lump [S] [P1]
- [ ] `RAW-MIN-06` — Precious metal nugget (gold, silver) [S] [P1]

### Tech components (`RAW-TECH`)
- [ ] `RAW-TECH-01` — Circuit board, intact [S] [P0]
- [ ] `RAW-TECH-02` — Circuit board, damaged / salvaged [S] [P0]
- [ ] `RAW-TECH-03` — Servo and actuator unit [S] [P1]
- [ ] `RAW-TECH-04` — Power cell / battery pack [S] [P1]
- [ ] `RAW-TECH-05` — Optic lens and sensor array [S] [P1]
- [ ] `RAW-TECH-06` — Data chip / memory shard [S] [P1]

### Contraband (`RAW-CONT`)
- [ ] `RAW-CONT-01` — Sealed package (opaque, generic) [S] [P0]
- [ ] `RAW-CONT-02` — Unmarked vials, rack of 4 [S] [P0]
- [ ] `RAW-CONT-03` — Stolen data drives [S] [P1]
- [ ] `RAW-CONT-04` — Forged documents / ID chips [S] [P1]
- [ ] `RAW-CONT-05` — Unlicensed weapon parts [S] [P1]
- [ ] `RAW-CONT-06` — Heat level visual state: item glows or flags when carried in a restricted district [D] [P1]

### Glowing Qi stones (`RAW-QI`)
- [ ] `RAW-QI-01` — Qi stone, low grade (dim inner glow) [S] [P0]
- [ ] `RAW-QI-02` — Qi stone, mid grade [S] [P0]
- [ ] `RAW-QI-03` — Qi stone, high grade (bright, faceted) [S] [P0]
- [ ] `RAW-QI-04` — Qi stone, supreme grade (animated core, particle emission) [S] [P1]
- [ ] `RAW-QI-05` — Shared emissive material family across all grades, one shader [D] [P0]
- [ ] `RAW-QI-06` — Inventory icon set with rarity legibility at 64px [D] [P0]

---

## 3. Arsenal — melee (6 classes × 3 tiers)

Tier 1 = common/crafted, Tier 2 = refined, Tier 3 = rare/named. Each weapon needs LOD0 + LOD1,
a first-person variant, a sheathed variant, and impact VFX matched to its damage type.

### Fists / gauntlets (`FST`)
- [ ] `WPN-MEL-FST-01` — Tier 1: wrapped fists / cloth gloves [S] [P0]
- [ ] `WPN-MEL-FST-02` — Tier 2: brass knuckles [S] [P0]
- [ ] `WPN-MEL-FST-03` — Tier 3: powered cyber gauntlet (emissive servos) [S] [P1]

### Daggers (`DAG`)
- [ ] `WPN-MEL-DAG-01` — Tier 1: rusty shiv / switchblade [S] [P0]
- [ ] `WPN-MEL-DAG-02` — Tier 2: steel dagger [S] [P0]
- [ ] `WPN-MEL-DAG-03` — Tier 3: ritual blade with rune fuller [S] [P1]

### Swords (`SWD`)
- [ ] `WPN-MEL-SWD-01` — Tier 1: iron jian / straight sword [S] [P0]
- [ ] `WPN-MEL-SWD-02` — Tier 2: folded-steel dao / sabre [S] [P0]
- [ ] `WPN-MEL-SWD-03` — Tier 3: Qi-infused sword with energy edge [S] [P1]

### Greatswords (`GSW`)
- [ ] `WPN-MEL-GSW-01` — Tier 1: crude cleaver slab [S] [P0]
- [ ] `WPN-MEL-GSW-02` — Tier 2: forged greatsword [S] [P0]
- [ ] `WPN-MEL-GSW-03` — Tier 3: enchanted greatsword with emissive runes [S] [P1]

### Blunt (`BLT`)
- [ ] `WPN-MEL-BLT-01` — Tier 1: wooden club / pipe [S] [P0]
- [ ] `WPN-MEL-BLT-02` — Tier 2: flanged mace [S] [P0]
- [ ] `WPN-MEL-BLT-03` — Tier 3: warhammer with impact charge [S] [P1]

### Polearms (`POL`)
- [ ] `WPN-MEL-POL-01` — Tier 1: wooden spear / bo staff [S] [P0]
- [ ] `WPN-MEL-POL-02` — Tier 2: steel-tipped qiang / glaive [S] [P0]
- [ ] `WPN-MEL-POL-03` — Tier 3: spirit-lance with energy head [S] [P1]
- [ ] `WPN-MEL-POL-04` — Shared: damage-type impact VFX set (slash / pierce / crush / energy) [D] [P0]

---

## 4. Arsenal — ranged (6 classes × 3 tiers)

Classes span pistols to snipers. Each needs LOD0 + LOD1, a first-person model with animated
moving parts, muzzle-flash socket, and reload parts that match the `ANM-TAC` reload clips.

### Pistol (`PST`)
- [ ] `WPN-RNG-PST-01` — Tier 1: worn semi-auto pistol [S] [P0]
- [ ] `WPN-RNG-PST-02` — Tier 2: modern service pistol with rail [S] [P0]
- [ ] `WPN-RNG-PST-03` — Tier 3: suppressed / smart-linked pistol [S] [P1]

### SMG (`SMG`)
- [ ] `WPN-RNG-SMG-01` — Tier 1: improvised SMG [S] [P0]
- [ ] `WPN-RNG-SMG-02` — Tier 2: compact PDW [S] [P0]
- [ ] `WPN-RNG-SMG-03` — Tier 3: vector-style PDW with holographic sight [S] [P1]

### Shotgun (`SHG`)
- [ ] `WPN-RNG-SHG-01` — Tier 1: sawn-off double barrel [S] [P0]
- [ ] `WPN-RNG-SHG-02` — Tier 2: pump-action shotgun [S] [P0]
- [ ] `WPN-RNG-SHG-03` — Tier 3: auto-shotgun with drum mag [S] [P1]

### Assault rifle (`RIF`)
- [ ] `WPN-RNG-RIF-01` — Tier 1: weathered carbine [S] [P0]
- [ ] `WPN-RNG-RIF-02` — Tier 2: modular assault rifle with attachments [S] [P0]
- [ ] `WPN-RNG-RIF-03` — Tier 3: energy-assist rifle with rail system [S] [P1]

### Marksman rifle (`DMR`)
- [ ] `WPN-RNG-DMR-01` — Tier 1: bolt-action hunting rifle [S] [P1]
- [ ] `WPN-RNG-DMR-02` — Tier 2: designated marksman rifle [S] [P1]
- [ ] `WPN-RNG-DMR-03` — Tier 3: semi-auto DMR with thermal scope [S] [P1]

### Sniper (`SNP`)
- [ ] `WPN-RNG-SNP-01` — Tier 1: scoped long rifle [S] [P1]
- [ ] `WPN-RNG-SNP-02` — Tier 2: anti-materiel sniper with bipod [S] [P1]
- [ ] `WPN-RNG-SNP-03` — Tier 3: railgun / charged-shot sniper (arcane-tech hybrid) [S] [P1]
- [ ] `WPN-RNG-SNP-04` — Shared: muzzle flash, casing eject, smoke trail, tracer VFX set [D] [P0]
- [ ] `WPN-RNG-SNP-05` — Shared: attachment kit (scope, suppressor, grip, mag) as modular sockets [D] [P1]

---

## 5. Arsenal — throwables (`WPN-THR`)

- [ ] `WPN-THR-01` — Frag grenade: mesh, pin pull, cook timer, blast VFX [S] [P0]
- [ ] `WPN-THR-02` — EMP grenade: arc discharge VFX, disables tech and cybernetics [S] [P0]
- [ ] `WPN-THR-03` — Flashbang: screen-flash and audio-ring effect [S] [P0]
- [ ] `WPN-THR-04` — Smoke grenade: occlusion volume, blocks detection cones [S] [P1]
- [ ] `WPN-THR-05` — Molotov / Qi incendiary: burning ground area [S] [P1]
- [ ] `WPN-THR-06` — Paper talisman bomb (cultivator / cultist flavour) [S] [P1]
- [ ] `WPN-THR-07` — Breaching charge (placeable, pairs with `ANM-TAC-21`) [S] [P1]
- [ ] `WPN-THR-08` — Shared throw arc preview UI and trajectory VFX [D] [P0]
