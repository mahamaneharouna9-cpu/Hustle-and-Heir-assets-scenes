# 00 — Pipeline standards, naming & acceptance criteria

Global rules for every asset in this checklist. Individual items in `01`–`05` are not
re-stated with their full requirements here — an item is not "done" until it satisfies the
**Definition of Done** for its discipline below.

This file contains no trackable checkboxes; it is the contract the checklists point at.

---

## 1. Tag legend used in every checklist item

Every item ends with two tags: `[S|D] [P0|P1|P2]`.

| Tag | Meaning |
| --- | --- |
| `[S]` | **Specified** — named explicitly in the original asset brief. |
| `[D]` | **Derived** — not named in the brief, but required to make an `[S]` item shippable (LODs, collision, audio, depleted states, icon sets, streaming, etc.). Flag for review if you disagree. |
| `[P0]` | **Vertical slice** — needed for the first playable district slice. |
| `[P1]` | **Alpha** — needed for content-complete gameplay across all 12 districts. |
| `[P2]` | **Beta / launch** — polish, variant count, cosmetic breadth. |

Checkbox states: `- [ ]` open, `- [x]` done, `- [-]` deferred / won't-ship.

Every asset ID is registered in `tools/check_checklist.py` (`PREFIXES`). Adding a new
category means adding its prefix there first, or the check fails.

---

## 2. Polygon & budget targets

| Asset class | Budget | Notes |
| --- | --- | --- |
| Player / NPC character | **3,000–8,000 tris total** | Hard cap from the brief. This is the *assembled* budget: body + wardrobe layers + accessories + hair. |
| Base body frame (naked) | ≤ 3,500 tris | Leaves 4,500+ for wardrobe, hair and accessories. |
| Hairstyle | 300–1,500 tris | Cards; long styles at the top of the range. |
| Wardrobe layer | 200–900 tris per layer | 8 layers max visible at once. |
| Career accessory (pouch, pendant, holster…) | ≤ 250 tris | **Modular interchangeable attachments only**, never welded to the body. |
| Melee / ranged weapon | 600–1,800 tris | Tier 1 low, Tier 3 high. |
| Crafting workstation | 1,500–6,000 tris | Hero interactable, seen in close-up. |
| Raw material pickup | ≤ 300 tris | Also needs a 2D inventory icon. |
| District kit piece | 200–2,500 tris | Trim and facade panels under 500. |
| District hero landmark | ≤ 30,000 tris | One per district, HLOD-proxied. |
| Vehicle | 2,000–8,000 tris | Magic vehicles (sword, broom, Qi cloud) at the low end. |
| UI panel element | n/a | 9-slice; no baked borders. |

**Accessory rule (from the brief):** to hold the 3,000–8,000 character budget, all
career-specific accessories — pouches, pendants, holsters, badges, sashes — are modelled as
**modular, interchangeable attachments** sharing **one 512×512 texture atlas per career**.
One atlas, not one atlas per item. Attachment sockets are defined once in `WRD-19`.

### VFX budgets

| VFX class | Budget |
| --- | --- |
| Persona aura | **50–100 particles max** (hard cap from the brief) |
| Weapon hit / impact | ≤ 40 particles |
| Ambient district VFX | ≤ 150 particles per active volume |
| Weather (rain/snow) | Shader + GPU particles, never per-actor emitters |
| Full-screen overlay | 1 post-process pass; stack no more than 3 concurrently |

---

## 3. Texture standards

| Map | Size | Channels |
| --- | --- | --- |
| Head / face | 1024×1024 | albedo, normal, ORM, **grayscale tint mask** |
| Body | 1024×1024 | albedo, normal, ORM |
| Wardrobe atlas A / B | 512–1024 | albedo + grayscale tint mask |
| **Career accessory atlas** | **512×512 (one per career)** | albedo + ORM packed, shared by every accessory in that career |
| Hair | 512×512 | strand alpha + root/tip gradient mask |
| Scar / tattoo decals | 512×512 atlas | alpha + grayscale tint mask |
| Inventory icons | 64 / 128 | UI-space, transparent |

**Grayscale tint mask channel convention** (used everywhere, no exceptions):

| Channel | Drives |
| --- | --- |
| R | Primary fabric / skin tint |
| G | Secondary trim |
| B | Hair |
| A | Emissive accent (implants, runes, LEDs) |

Skin uses a **subsurface scattering** shader: SSS profile + thickness map + curvature/AO map.
All characters get **edge rim lighting** via a fresnel mask, tunable per persona aura colour.

Formats: source in `.psd`/`.sbsar`, export PNG (albedo/mask) and BC7/TGA (normal, ORM). Never
commit source PSDs to the export folder.

---

## 4. Naming conventions

| Prefix | Type | Example |
| --- | --- | --- |
| `SM_` | Static mesh | `SM_ENV_OLD_BrickWall_Corner_A` |
| `SK_` | Skeletal mesh | `SK_CHR_Base_Athletic` |
| `SK_W_` | Wardrobe / attachment | `SK_W_CUL_InnerRobe_A` |
| `T_` | Texture | `T_CHR_Face_A`, `T_CUL_Acc_Atlas_M` |
| `M_` / `MI_` | Material / instance | `M_CHR_Skin_SSS`, `MI_ENV_Rain_Wet` |
| `VFX_` | Particle system | `VFX_AUR_CUL_QiMist` |
| `AN_` | Animation | `AN_MEL_SWD_LightCombo_01` |
| `AM_` / `ABP_` | Montage / anim blueprint | `AM_CRF_Forge_HammerHeavy` |
| `BP_` | Blueprint | `BP_INT_HRV_OreNode` |
| `UI_` | Widget | `UI_Panel_Obsidian_Modal` |
| `AU_` | Audio | `AU_ENV_DTC_TrafficBed` |

Domain codes appear in the ID: `ENV_<DISTRICT>`, `CR_<CAREER>`, `WPN_<CLASS>`.
District codes and career codes are the canonical lists in `tools/check_checklist.py`
(`DISTRICTS`, `CAREERS`) — do not invent new ones.

---

## 5. LOD, collision, pivots

* **Characters:** LOD0 game-res, LOD1 60%, LOD2 35%, LOD3 15% + shadow proxy. Screen sizes 1.0 / 0.5 / 0.25 / 0.12.
* **Environment kit pieces:** LOD0 + LOD1 (50%) + HLOD impostor per district block.
* **Weapons:** LOD0 + LOD1 only (first-person visible).
* **Collision:** kit pieces get simplified convex; interactables get a `UCX_` box plus an
  interaction sphere; characters use capsules. No mesh-as-collision on anything over 500 tris.
* **Pivots:** bottom-centre, Z-up, metres, world-scale 1.0. Kit pieces snap to a 100 cm grid.
* **Attachments:** every accessory has exactly one named socket and zero baked transforms.

---

## 6. Animation standards

* 30 fps source, retargeted through one shared skeleton across **all 5 base body frames**.
* Root motion on all locomotion and melee; in-place for idle/emote/crafting loops.
* Additive layers for hit reactions, breathing and weapon sway — never baked into base clips.
* IK: foot placement, hand weapon grip, look-at. Physics proxies for hair and cloth.
* Naming: `AN_<DOMAIN>_<CLASS>_<ACTION>_<VARIANT>`, e.g. `AN_TAC_RIF_Reload_Tactical`.
* Every melee class and martial style ships with matching **montage + anim-notify set**
  (hit windows, footstep, VFX spawn, SFX cue) — the clip alone is not done.

---

## 7. Interactable standards

Every interactable (harvest node, workstation, furniture, vehicle) ships with:

1. mesh + LOD + collision,
2. interaction prompt hook (see `UI-` gesture-zone items),
3. a matching character animation (see `ANM-CRF` / `ANM-VEH`),
4. state variants (idle / in-use / depleted / broken) where applicable,
5. audio (loop + one-shot),
6. VFX slot,
7. a loot/economy data hook — no hard-coded rewards in the mesh or blueprint.

---

## 8. Definition of Done

| Discipline | An item is done when… |
| --- | --- |
| Mesh | Modelled, UV'd, in-engine at budget, LODs built, collision assigned, pivot correct, no lightmap overlap, checked in a test level. |
| Texture | All maps authored to the channel convention above, tint mask verified with 3 recolour variants, no >2 unused channels. |
| Shader/Material | Master material + documented instance parameters, runs at target on the lowest supported platform. |
| Rig/Anim | Retargets to all 5 body frames without foot sliding or mesh tearing; notifies authored; montage reviewed in gameplay. |
| VFX | Within particle budget, readable at 60 fps on target hardware, has an off state for the low graphics preset. |
| UI | 9-slice, localisation-safe (no baked text), readable at 720p and 4K, has empty/overflow states. |
| Career kit | Every wardrobe item fits the assembled 8,000-tri cap and pulls from the single 512 career atlas. |

---

## 9. Source control layout

```
assets/
  characters/   base/  wardrobe/<CAREER>/  hair/  decals/
  animation/    locomotion/  melee/<CLASS>/  martial/  tactical/  crafting/  vehicle/
  environment/  districts/<DISTRICT>/  vfx/  vehicles/  interactables/
  props/        workstations/  materials/  weapons/{melee,ranged,throwable}/
  ui/           panels/  hud/  magic/  auras/
  source/       (PSD, ZBrush, Blend, Houdini — excluded from export)
```

Only `.fbx`/`.gltf`, textures, engine assets and the checklists themselves are tracked.
Generated exports, caches and `source/` intermediates stay out of Git.

---

## 10. How to work this checklist

1. Pick a P0 slice: `ENV-DTC-*`, `CHR-BODY-*`, `ANM-LOC-*`, `WPN-*` tier 1, `UI-` core panels.
2. Check items off with `- [x]`; use `- [-]` for anything consciously cut (leave it visible).
3. Re-run `python3 tools/check_checklist.py --write` — it validates IDs, asserts the brief's
   numbers and refreshes the roll-up in `docs/asset-checklist/README.md`.
4. `--csv build/checklist.csv` exports the whole thing for a spreadsheet or tracker import.
