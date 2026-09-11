# 06 — Open questions

Places where the brief specifies a **count** but not the **identities**, or where a shippable
asset requires a decision the brief doesn't make. Each one names the checklist items blocked
behind it. Nothing here is a blocker for starting P0 work — but each needs an owner.

| # | Question | Blocked items | Assumption used in this checklist |
| --- | --- | --- | --- |
| 1 | **Which six martial arts styles?** The brief names the count and only Wing Chun appears elsewhere (the Cultivator's wooden dummy). | `ANM-MA-MA2-*` … `ANM-MA-MA6-*` (30 clips) | Style 1 = Wing Chun. Styles 2–6 carry placeholder codes and generic stance/combo/kick/block/throw/special structure. |
| 2 | **Which six spell drawing shapes?** Count is specified, identities are not. | `MAG-SHP-01`…`MAG-SHP-06`, `MAG-DRW-*`, `ANM-CRF-24` | Circle, triangle, spiral, cross/sigil, star polygon, rune lattice — mapped to ward / strike / channel / bind / summon / dispel. Marked as proposals in the file. |
| 3 | **Five body frames — how do they interact with gender/presentation?** The brief lists slim/athletic/average/heavy/tall and says nothing about sex characteristics. | `CHR-BASE-02`, and the whole wardrobe refit pass | Single androgynous base per frame with chest/hip morphs, rather than 10 separate meshes. Halves the wardrobe refit cost if accepted. |
| 4 | **What are the six ranged classes?** The brief says "pistols to snipers" only. | `WPN-RNG-*` (18 weapons), `ANM-TAC-09`…`-15` (reload clips) | `PST`, `SMG`, `SHG`, `RIF`, `DMR`, `SNP`. The reload animation set is derived directly from this list, so changing it changes both. |
| 5 | **How many weapon tiers?** The brief gives 6 melee + 6 ranged classes but no tier structure. | `WPN-MEL-*`, `WPN-RNG-*` | 3 tiers per class (crafted / refined / rare), 36 weapons total. Drop to 2 tiers and this loses 12 items. |
| 6 | **Which careers ship in the vertical slice?** All 10 are listed flat. | The `[P0]` split across `05-career-paths.md` | The signature outfit, primary tool and primary VFX of every career are `P0`; the rest is `P1`/`P2`. If only 3–4 careers are in the slice, this needs re-tagging. |
| 7 | **Which districts are in the vertical slice?** Twelve are named with no order. | `ENV-*` priority tags | Downtown Core and Old Town are `P0` (modern + traditional, covers the widest art range); the other ten are `P1`. |
| 8 | **Target engine and platforms?** Not stated, and it drives texture formats, shader model and the real budget ceiling. | `TEX-*`, all budgets in `00-standards` | Written engine-agnostic with a PC/console baseline. Mobile changes the 3,000–8,000 character budget conversation entirely. |
| 9 | **Is the 50–100 aura particle cap per character, or per screen?** | `AUR-*`, `AUR-SYS-02` | Per character, with a global concurrent-aura governor on top. Ten auras on screen at 100 particles is 1,000 particles before anything else. |
| 10 | **Meridian system — how literal?** The brief says "meridian body map overlays with elemental colour shifts". | `MAG-MER-*` | 12 principal meridians (traditional Chinese medicine routing) and 5 elemental colours (metal / wood / water / fire / earth). If design wants a fictional system, only `MAG-MER-02` and `-05` change. |
| 11 | **How many damage states per vehicle?** The brief says "visible damage models" without a count. | `VEH-11` | Three: light / heavy / wrecked, plus a burning state on the wreck. |
| 12 | **Raw material quantities.** Six families are named; item counts inside them are not. | `RAW-*` | 5–7 items per family, 35 total. Each is small (≤300 tris + an icon), so this is cheap to expand. |
| 13 | **Property furniture scope.** "Modular property furniture" could be 20 items or 200. | `INT-FUR-*` | 14 functional stations + 10 decorative prop sets to start, with a themed set per major district later. |
| 14 | **Do all 5 body frames get every hairstyle?** Card hair usually needs per-frame fitting. | `CHR-HAIR-*` | Authored on the Athletic frame and auto-fitted to the other four, with manual fixups on Heavy and Tall. If that fails, hairstyle cost multiplies by 5. |
| 15 | **Career exclusivity.** Can a character hold two careers at once? | `CR-*-A01` atlas and socket work, `WRD-20` | One career at a time, one 512 atlas loaded. Multi-career would need atlas streaming or a merged atlas. |

## Deliberate additions not in the brief

These are all tagged `[D]` in the checklist. Listed here so they can be cut as a group if scope
tightens:

* **LODs, collision, pivots, streaming volumes** — none of it is in the brief, none of it is optional.
* **Depleted and damage states** for harvest nodes, vehicles and workstations.
* **Audio beds and reverb zones** per district (12 items).
* **Icon sets** for every inventory-visible material, wardrobe item and prop.
* **Empty / loading / error states** for every UI panel, plus an accessibility pass.
* **Montages and animation notifies** — clips alone do not play in a game.
* **The shared aura master material and budget governor** that keeps ten auras inside one shader.
