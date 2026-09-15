#!/usr/bin/env python3
"""update_manifest.py — rebuild multiview/MANIFEST.json from what's on disk.

Run after each generation wave so progress is always accurate and committed.
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "concept_art"
OUT = ROOT / "multiview"

# subjects in these categories also need an interior view
INTERIOR_CATS = {"03_vehicles", "17_businesses", "18_housing",
                 "19_cultivation_sects", "20_magic_towers"}
# open vehicles without a cabin — no interior view needed
NO_INTERIOR = {"03_vehicles/VEHICLE_01_Bicycle", "03_vehicles/VEHICLE_02_Scooter",
               "03_vehicles/VEHICLE_10_Hoverboard", "03_vehicles/VEHICLE_11_Qi_Cloud"}

# priority order for generation waves (base meshes first ... careers last)
WAVES = [
    "01_base_meshes", "03_vehicles", "05_workstations", "21_pets",
    "22_mounts", "23_harvestable_herbs", "24_harvestable_trees",
    "25_harvestable_ore_veins", "26_harvestable_fish",
    "27_harvestable_tech_salvage", "17_businesses", "18_housing",
    "19_cultivation_sects", "20_magic_towers", "28_housing_interiors",
    "29_faction_building_interiors", "30_cultivation_sect_interiors",
    "31_arcane_tower_interiors", "32_special_building_interiors",
    "12_cultivation_martial_arts", "10_careers",
]


def main() -> None:
    subjects = []
    for cat in WAVES:
        d = SRC / cat
        if not d.exists():
            continue
        for src in sorted(d.rglob("*.jpg")):
            rel = src.relative_to(SRC)
            outdir = OUT / rel.parent
            need = ("front", "side", "back") + (
                ("interior",) if cat in INTERIOR_CATS
                and f"{cat}/{src.stem}" not in NO_INTERIOR else ())
            views = {v: (outdir / f"{src.stem}_{v}.jpg").exists()
                     for v in need}
            subjects.append({
                "src": str(rel),
                "done": sum(views.values()),
                "missing": [v for v, ok in views.items() if not ok],
            })
    manifest = {
        "subjects": subjects,
        "priority_order": [w for w in WAVES if (SRC / w).exists()],
        "stats": {
            "subjects": len(subjects),
            "complete": sum(1 for s in subjects if s["done"] == len(s["missing"]) or not s["missing"]),
            "views_pending": sum(len(s["missing"]) for s in subjects),
            "views_per_turn_limit": 10,
        },
    }
    (OUT / "MANIFEST.json").write_text(json.dumps(manifest, indent=1))
    st = manifest["stats"]
    print(f"subjects={st['subjects']} complete={st['complete']} "
          f"views_pending={st['views_pending']}")


if __name__ == "__main__":
    main()
