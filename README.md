# Hustle-and-Heir-assets-scenes

Asset and scene production repository for **Hustle & Heir**.

## Asset checklist

The full asset production checklist lives in **[docs/asset-checklist/](docs/asset-checklist/README.md)** —
957 tracked deliverables across characters, world, props, UI/magic and the 10 career paths, each
with a stable ID, a provenance tag and a priority.

```bash
python3 tools/check_checklist.py            # validate + print the roll-up
python3 tools/check_checklist.py --write    # refresh the progress table in the index
python3 tools/check_checklist.py --csv build/checklist.csv   # export for a tracker
```

Start with [00-standards-and-conventions.md](docs/asset-checklist/00-standards-and-conventions.md)
for budgets, naming and the definition of done, then
[06-open-questions.md](docs/asset-checklist/06-open-questions.md) for the decisions still open.

## Layout

```
docs/asset-checklist/   the checklist (markdown, source of truth)
tools/                  check_checklist.py — validator, roll-up generator, CSV export
assets/                 art assets (see the source-control layout in docs/00)
```
