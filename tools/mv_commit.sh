#!/usr/bin/env bash
# mv_commit.sh — update the multiview manifest, commit any new images/tools,
# and push to the session branch. Run at the end of every generation wave so
# generated images are never lost.
set -euo pipefail
cd "$(dirname "$0")/.."
PY=/home/user/.glbenv/bin/python
# self-heal: venv is cleared between sessions
if [ ! -x "$PY" ]; then
  echo "recreating python venv..."
  python3 -m venv /home/user/.glbenv
  /home/user/.glbenv/bin/pip install --quiet pillow numpy
fi
BRANCH=arena/01a0a60e-hustle-and-heir-assets-scenes

$PY tools/update_manifest.py
git add multiview tools 2>/dev/null || true

if ! git diff --cached --quiet; then
  N=$($PY -c "import json;print(json.load(open('multiview/MANIFEST.json'))['stats'])" 2>/dev/null || echo "?")
  git -c user.name="Arena Agent" -c user.email="agent@arena.local" \
      commit -m "multiview: generation wave progress ($N)"
  git push origin "$BRANCH"
  echo "committed + pushed"
else
  echo "nothing new to commit"
fi
