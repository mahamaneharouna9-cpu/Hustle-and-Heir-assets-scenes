# 05 — Career paths

Ten career paths. Each has three columns from the brief — **Wardrobe & Wearables (`W`)**,
**Career Tools & Interactable Props (`T`)**, **Specific VFX & UI Overlays (`V`)** — plus one
integration item per career (`A`) covering the shared accessory atlas and the assembled
polygon budget.

**Standing rule for every career (from the brief):** to hold the 3,000–8,000 polygon budget per
character, all career-specific accessories — pouches, pendants, holsters, badges, sashes — are
modelled as **modular, interchangeable attachments** sharing a **single 512×512 texture atlas per
career**. Socket standard is `WRD-19`; atlas spec is `TEX-10`.

---

## 5.1 Cultivator (`CUL`)

### Wardrobe & wearables
- [ ] `CR-CUL-W01` — Outer Sect robe (long, flowing, cloth physics) [S] [P0]
- [ ] `CR-CUL-W02` — Inner Sect robe (lighter layer, worn beneath) [S] [P0]
- [ ] `CR-CUL-W03` — Martial wraps (hands, forearms, shins) [S] [P0]
- [ ] `CR-CUL-W04` — Bamboo conical hat [S] [P1]
- [ ] `CR-CUL-W05` — Jade pendant (neck socket) [S] [P1]
- [ ] `CR-CUL-W06` — Prayer beads (wrist, physics-driven) [S] [P1]

### Tools & interactable props
- [ ] `CR-CUL-T01` — Meditation mat (pairs with `ANM-CRF-23`, `INT-FUR-F11`) [S] [P0]
- [ ] `CR-CUL-T02` — Wooden Wing Chun dummy (pairs with `ANM-MA-MA1-06`) [S] [P1]
- [ ] `CR-CUL-T03` — Alchemy furnace (portable, pairs with `CFT-ALC-*`) [S] [P0]
- [ ] `CR-CUL-T04` — Flying sword (vehicle form, pairs with `VEH-08`) [S] [P0]
- [ ] `CR-CUL-T05` — Inscribed jade slips (readable info items) [S] [P1]

### VFX & UI overlays
- [ ] `CR-CUL-V01` — Ambient Qi mist at the feet (pairs with `AUR-CUL`) [S] [P0]
- [ ] `CR-CUL-V02` — Glowing meridian network overlay (pairs with `MAG-MER-*`) [S] [P0]
- [ ] `CR-CUL-V03` — Spiritual pressure aura: expanding ring on power release [S] [P1]
- [ ] `CR-CUL-V04` — Localised wind distortion around the character during channeling [S] [P1]

### Integration
- [ ] `CR-CUL-A01` — Cultivator accessory atlas (512×512) + assembled budget verified under 8,000 tris [S] [P0]

---

## 5.2 Arcane Scholar (`SCH`)

### Wardrobe & wearables
- [ ] `CR-SCH-W01` — Modernised wizard cloak (tailored, cloth physics) [S] [P0]
- [ ] `CR-SCH-W02` — Tactical trench coat (armoured variant) [S] [P1]
- [ ] `CR-SCH-W03` — Enchanted amulet (chest socket, emissive) [S] [P1]
- [ ] `CR-SCH-W04` — Runic scarf (emissive glyph band) [S] [P1]
- [ ] `CR-SCH-W05` — Spell-foci rings (hand socket, 3 variants) [S] [P1]

### Tools & interactable props
- [ ] `CR-SCH-T01` — 3D tactile grimoire with turnable pages (pairs with `MAG-GRM-*`) [S] [P0]
- [ ] `CR-SCH-T02` — Crystal ball terminal (workstation, scrying interface) [S] [P1]
- [ ] `CR-SCH-T03` — Potion bandolier (wearable, readable vial slots) [S] [P1]
- [ ] `CR-SCH-T04` — Telescope rig (deployable, lens flare) [S] [P2]

### VFX & UI overlays
- [ ] `CR-SCH-V01` — Emissive floating runes orbiting the caster [S] [P0]
- [ ] `CR-SCH-V02` — Elemental particle trails — fire [S] [P0]
- [ ] `CR-SCH-V03` — Elemental particle trails — frost [S] [P1]
- [ ] `CR-SCH-V04` — Elemental particle trails — lightning [S] [P1]
- [ ] `CR-SCH-V05` — Gesture-drawing spell canvas (pairs with `MAG-SHP-07`) [S] [P0]

### Integration
- [ ] `CR-SCH-A01` — Scholar accessory atlas (512×512) + assembled budget verified under 8,000 tris [S] [P0]

---

## 5.3 Cyber Hacker (`HAC`)

### Wardrobe & wearables
- [ ] `CR-HAC-W01` — Streetwear base with LED accent strips (emissive mask driven) [S] [P0]
- [ ] `CR-HAC-W02` — Asymmetrical tech jacket [S] [P0]
- [ ] `CR-HAC-W03` — Glowing visor (head slot, HUD-reflection shader) [S] [P1]
- [ ] `CR-HAC-W04` — Data-glove wearables (hand slot, pairs with `WRD-17`) [S] [P1]

### Tools & interactable props
- [ ] `CR-HAC-T01` — Handheld cyberdeck (portable hacking device) [S] [P0]
- [ ] `CR-HAC-T02` — Multi-monitor rig station (workstation, pairs with `INT-FUR-F08`) [S] [P0]
- [ ] `CR-HAC-T03` — Soldering iron (pairs with `ANM-CRF-17`) [S] [P1]
- [ ] `CR-HAC-T04` — EMP grenades (pairs with `WPN-THR-02`) [S] [P0]
- [ ] `CR-HAC-T05` — Portable server (deployable prop, blinking status lights) [S] [P1]

### VFX & UI overlays
- [ ] `CR-HAC-V01` — Glitch / static screen overlays on hack attempts [S] [P0]
- [ ] `CR-HAC-V02` — Holographic projection cones from deck and monitors [S] [P0]
- [ ] `CR-HAC-V03` — Binary code cascades in world and screen space [S] [P1]
- [ ] `CR-HAC-V04` — Neon green / blue rim lighting (pairs with `TEX-15`) [S] [P0]

### Integration
- [ ] `CR-HAC-A01` — Hacker accessory atlas (512×512) + assembled budget verified under 8,000 tris [S] [P0]

---

## 5.4 Underworld (`UDW`)

### Wardrobe & wearables
- [ ] `CR-UDW-W01` — Tactical stealth suit (matte, low-reflectance material) [S] [P0]
- [ ] `CR-UDW-W02` — Heavy enforcer vest (armoured variant) [S] [P0]
- [ ] `CR-UDW-W03` — Balaclava / face coverings, 3 variants [S] [P0]
- [ ] `CR-UDW-W04` — Concealed holsters (under-jacket socket) [S] [P0]
- [ ] `CR-UDW-W05` — Brass knuckles (hand slot, pairs with `WPN-MEL-FST-02`) [S] [P1]

### Tools & interactable props
- [ ] `CR-UDW-T01` — Tension wrench (pairs with `ANM-CRF-22`) [S] [P0]
- [ ] `CR-UDW-T02` — Lockpick set (case prop + individual picks) [S] [P0]
- [ ] `CR-UDW-T03` — Crowbar (tool and melee hybrid) [S] [P0]
- [ ] `CR-UDW-T04` — Duffel bags of contraband (carry prop, pairs with `RAW-CONT-*`) [S] [P0]
- [ ] `CR-UDW-T05` — Switchblades (pairs with `WPN-MEL-DAG-01`) [S] [P0]
- [ ] `CR-UDW-T06` — Suppressed pistols (pairs with `WPN-RNG-PST-03`) [S] [P0]

### VFX & UI overlays
- [ ] `CR-UDW-V01` — Shadow-step smoke trails on dash and stealth move [S] [P0]
- [ ] `CR-UDW-V02` — Red aggro / stealth detection UI rings (pairs with `ANM-TAC-26`) [S] [P0]
- [ ] `CR-UDW-V03` — Muzzle flash set tuned for suppressed and unsuppressed fire [S] [P0]
- [ ] `CR-UDW-V04` — Blood splatter decals: surface set with decay timer [S] [P1]

### Integration
- [ ] `CR-UDW-A01` — Underworld accessory atlas (512×512) + assembled budget verified under 8,000 tris [S] [P0]

---

## 5.5 Influencer (`INF`)

### Wardrobe & wearables
- [ ] `CR-INF-W01` — Haute couture streetwear set [S] [P0]
- [ ] `CR-INF-W02` — Designer sunglasses, 3 variants [S] [P1]
- [ ] `CR-INF-W03` — Branded sneakers [S] [P1]
- [ ] `CR-INF-W04` — Luxury watches (wrist socket) [S] [P2]
- [ ] `CR-INF-W05` — Dynamic capes (cloth physics, wind-reactive) [S] [P1]

### Tools & interactable props
- [ ] `CR-INF-T01` — Drone cameras (autonomous follower prop, rotor VFX) [S] [P0]
- [ ] `CR-INF-T02` — Portable ring light (deployable, emissive) [S] [P1]
- [ ] `CR-INF-T03` — Smartphone with gimbal stabiliser [S] [P0]
- [ ] `CR-INF-T04` — Branded energy drinks (consumable prop, readable can) [S] [P2]

### VFX & UI overlays
- [ ] `CR-INF-V01` — Camera flash bursts (screen-safe exposure) [S] [P0]
- [ ] `CR-INF-V02` — Heart / like floating particle emojis [S] [P0]
- [ ] `CR-INF-V03` — Vibrant neon aura rings (pairs with `AUR-INF`) [S] [P1]
- [ ] `CR-INF-V04` — Streaming UI frames: live-chat and follower-count overlays [S] [P1]

### Integration
- [ ] `CR-INF-A01` — Influencer accessory atlas (512×512) + assembled budget verified under 8,000 tris [S] [P0]

---

## 5.6 Corporate Heir (`HEI`)

### Wardrobe & wearables
- [ ] `CR-HEI-W01` — Bespoke tailored suit (2 cuts, formal and business) [S] [P0]
- [ ] `CR-HEI-W02` — Silk ties, 4 patterns [S] [P1]
- [ ] `CR-HEI-W03` — Luxury briefcase (carry prop) [S] [P1]
- [ ] `CR-HEI-W04` — Earpieces (ear socket, discreet) [S] [P1]
- [ ] `CR-HEI-W05` — High-end smartglasses (head slot, subtle HUD glint) [S] [P1]

### Tools & interactable props
- [ ] `CR-HEI-T01` — Executive mahogany desk (pairs with `INT-FUR-F14`) [S] [P1]
- [ ] `CR-HEI-T02` — Whiskey decanter set (glass shader, pour interaction) [S] [P2]
- [ ] `CR-HEI-T03` — Physical stock ticker (animated readout) [S] [P2]
- [ ] `CR-HEI-T04` — Signed contract documents (readable prop, signature interaction) [S] [P1]

### VFX & UI overlays
- [ ] `CR-HEI-V01` — Gold-tinted interface panels (UI skin variant) [S] [P0]
- [ ] `CR-HEI-V02` — Rising profit-chart holographic arcs [S] [P1]
- [ ] `CR-HEI-V03` — Crisp, minimal geometric auras (pairs with `AUR-HEI`) [S] [P1]

### Integration
- [ ] `CR-HEI-A01` — Heir accessory atlas (512×512) + assembled budget verified under 8,000 tris [S] [P0]

---

## 5.7 Mechanic / Artisan (`MEC`)

### Wardrobe & wearables
- [ ] `CR-MEC-W01` — Heavy-duty apron (leather, tool loops) [S] [P0]
- [ ] `CR-MEC-W02` — Welding mask (head slot, flip-down visor) [S] [P0]
- [ ] `CR-MEC-W03` — Utility belts (waist socket, tool attachments) [S] [P0]
- [ ] `CR-MEC-W04` — Grease-stained overalls (dirt mask variant) [S] [P0]
- [ ] `CR-MEC-W05` — Thermal gloves (hand slot) [S] [P1]

### Tools & interactable props
- [ ] `CR-MEC-T01` — Blacksmith anvils (pairs with `CFT-FRG-01`) [S] [P0]
- [ ] `CR-MEC-T02` — Hydraulic press (animated rig, pairs with `ANM-CRF-20`) [S] [P1]
- [ ] `CR-MEC-T03` — Blowtorches (flame VFX, pairs with `ANM-CRF-21`) [S] [P0]
- [ ] `CR-MEC-T04` — Vehicle lifts (property station, pairs with `INT-FUR-F12`) [S] [P1]
- [ ] `CR-MEC-T05` — Scattered blueprints (readable decals and paper props) [S] [P1]
- [ ] `CR-MEC-T06` — Wrenches and hand-tool set (socket attachments) [S] [P0]

### VFX & UI overlays
- [ ] `CR-MEC-V01` — Sparks and ember particle systems [S] [P0]
- [ ] `CR-MEC-V02` — Heat distortion waves over the work area [S] [P0]
- [ ] `CR-MEC-V03` — Glowing hot-metal textures (cooling gradient over time) [S] [P0]
- [ ] `CR-MEC-V04` — Crafting success bursts [S] [P0]

### Integration
- [ ] `CR-MEC-A01` — Mechanic accessory atlas (512×512) + assembled budget verified under 8,000 tris [S] [P0]

---

## 5.8 Military / PMC (`MIL`)

### Wardrobe & wearables
- [ ] `CR-MIL-W01` — Modular plate carriers (swappable pouch configuration) [S] [P0]
- [ ] `CR-MIL-W02` — Ballistic helmets with flip-down NVGs [S] [P0]
- [ ] `CR-MIL-W03` — Exoskeleton leg braces (pairs with `WRD-16`) [S] [P1]
- [ ] `CR-MIL-W04` — Combat boots [S] [P0]
- [ ] `CR-MIL-W05` — Tactical radio headsets [S] [P1]

### Tools & interactable props
- [ ] `CR-MIL-T01` — Assault rifles (pairs with `WPN-RNG-RIF-*`) [S] [P0]
- [ ] `CR-MIL-T02` — Breaching charges (pairs with `WPN-THR-07`) [S] [P0]
- [ ] `CR-MIL-T03` — Flashbangs (pairs with `WPN-THR-03`) [S] [P0]
- [ ] `CR-MIL-T04` — Interactive tactical map table (holo-terrain, planning UI) [S] [P1]
- [ ] `CR-MIL-T05` — Weapon workbench cleaning kits (pairs with `ANM-TAC-24`) [S] [P1]

### VFX & UI overlays
- [ ] `CR-MIL-V01` — Red laser sight beams (volumetric, dust-visible) [S] [P0]
- [ ] `CR-MIL-V02` — Thermal vision screen overlays [S] [P0]
- [ ] `CR-MIL-V03` — Heavy muzzle smoke [S] [P0]
- [ ] `CR-MIL-V04` — Squad-status health HUD (teammate vitals panel) [S] [P1]

### Integration
- [ ] `CR-MIL-A01` — Military accessory atlas (512×512) + assembled budget verified under 8,000 tris [S] [P0]

---

## 5.9 Politician (`POL`)

### Wardrobe & wearables
- [ ] `CR-POL-W01` — Pinstripe tailored suits (2 cuts) [S] [P0]
- [ ] `CR-POL-W02` — Lapel pins (faction and campaign variants) [S] [P1]
- [ ] `CR-POL-W03` — Armoured bulletproof vests worn under shirts (hidden layer) [S] [P0]
- [ ] `CR-POL-W04` — Campaign sashes [S] [P1]
- [ ] `CR-POL-W05` — Discreet comms earpieces [S] [P1]

### Tools & interactable props
- [ ] `CR-POL-T01` — Press podiums with dynamic microphones [S] [P0]
- [ ] `CR-POL-T02` — Voting terminals [S] [P1]
- [ ] `CR-POL-T03` — Campaign flyer stacks (scatterable props) [S] [P2]
- [ ] `CR-POL-T04` — Blackmail dossiers (readable, quest-linked) [S] [P1]
- [ ] `CR-POL-T05` — Megaphones (audio cone VFX) [S] [P2]

### VFX & UI overlays
- [ ] `CR-POL-V01` — Approval-rating UI meters [S] [P0]
- [ ] `CR-POL-V02` — Localised area-of-effect "rhetoric" rings on speech [S] [P0]
- [ ] `CR-POL-V03` — Tinted camera flashes from press crowds [S] [P1]

### Integration
- [ ] `CR-POL-A01` — Politician accessory atlas (512×512) + assembled budget verified under 8,000 tris [S] [P0]

---

## 5.10 Cultist / Secret Society (`CLT`)

### Wardrobe & wearables
- [ ] `CR-CLT-W01` — Blank geometric ceremonial masks [S] [P0]
- [ ] `CR-CLT-W02` — Animalistic ceremonial masks (3 variants) [S] [P0]
- [ ] `CR-CLT-W03` — Heavy hooded ritual cloaks (cloth physics) [S] [P0]
- [ ] `CR-CLT-W04` — Emissive branding tattoos (pairs with `CHR-DECAL-18`) [S] [P0]
- [ ] `CR-CLT-W05` — Concealed wrist blades (pairs with `WRD-10`) [S] [P0]

### Tools & interactable props
- [ ] `CR-CLT-T01` — Obsidian sacrificial altars (station, emissive veins) [S] [P0]
- [ ] `CR-CLT-T02` — Forbidden flesh-bound tomes (variant of `MAG-GRM-01`) [S] [P0]
- [ ] `CR-CLT-T03` — Ritual chalk sticks (drawable decals in world) [S] [P1]
- [ ] `CR-CLT-T04` — Heavy incense burners (smoke column VFX) [S] [P1]
- [ ] `CR-CLT-T05` — Blood vials (liquid shader, fill levels) [S] [P1]

### VFX & UI overlays
- [ ] `CR-CLT-V01` — Whispering shadow particle emitters [S] [P0]
- [ ] `CR-CLT-V02` — Screen-edge sanity / void distortions [S] [P0]
- [ ] `CR-CLT-V03` — Crimson ritual circles (ground decal, animated) [S] [P0]
- [ ] `CR-CLT-V04` — Corruption meters (UI, escalating tint) [S] [P1]

### Integration
- [ ] `CR-CLT-A01` — Cultist accessory atlas (512×512) + assembled budget verified under 8,000 tris [S] [P0]
