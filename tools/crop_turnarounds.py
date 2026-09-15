#!/usr/bin/env python3
"""
crop_turnarounds.py — Extract front/side/back views from concept sheets that
already contain turnarounds.

Handles two known sheet layouts:
  1. 01_base_meshes  — three figures side by side (front | side | back) on a
     dark background. Crop into thirds, then auto-trim to the subject.
  2. 03_vehicles     — spec sheet with FRONT/SIDE/REAR/TOP thumbnails in the
     lower band. Crop the three labeled panels (fixed template coordinates),
     then auto-trim each to the subject.

Output: multiview/<category>/<name>_front.jpg | _side.jpg | _back.jpg
Usage:  python tools/crop_turnarounds.py
"""

import sys
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "concept_art"
OUT = ROOT / "multiview"

# lower-band panel boxes (x0, y0, x1, y1) on the 1536x1024 vehicle sheet
VEHICLE_PANELS = {
    "front": (28, 448, 424, 706),
    "side": (432, 448, 830, 706),
    "back": (838, 448, 1160, 706),
}
TRIM_THRESHOLD = 28      # pixels darker than this are "background"
TRIM_MARGIN = 12         # keep a little breathing room


def trim_content(im: Image.Image) -> Image.Image:
    g = im.convert("L")
    mask = g.point(lambda v: 255 if v > TRIM_THRESHOLD else 0)
    bbox = mask.getbbox()
    if not bbox:
        return im
    x0, y0, x1, y1 = bbox
    m = TRIM_MARGIN
    x0 = max(0, x0 - m)
    y0 = max(0, y0 - m)
    x1 = min(im.width, x1 + m)
    y1 = min(im.height, y1 + m)
    return im.crop((x0, y0, x1, y1))


def save_view(im: Image.Image, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    im.save(dst, quality=92)


def crop_base_mesh(src: Path, outdir: Path) -> None:
    im = Image.open(src).convert("RGB")
    w = im.width
    thirds = [(0, w // 3), (w // 3, 2 * w // 3), (2 * w // 3, w)]
    views = ["front", "side", "back"]
    for (x0, x1), view in zip(thirds, views):
        # skip the title strip at the top of the sheet (first third only)
        top = 80 if view == "front" else 0
        part = im.crop((x0, top, x1, im.height))
        save_view(trim_content(part), outdir / f"{src.stem}_{view}.jpg")


def crop_vehicle(src: Path, outdir: Path) -> None:
    im = Image.open(src).convert("RGB")
    # scale template boxes if the sheet is not 1536x1024
    sx, sy = im.width / 1536.0, im.height / 1024.0
    for view, (x0, y0, x1, y1) in VEHICLE_PANELS.items():
        box = (int(x0 * sx), int(y0 * sy), int(x1 * sx), int(y1 * sy))
        part = im.crop(box)
        save_view(trim_content(part), outdir / f"{src.stem}_{view}.jpg")


def main() -> int:
    base = sorted((SRC / "01_base_meshes").glob("*.jpg"))
    veh = sorted((SRC / "03_vehicles").glob("*.jpg"))
    for src in base:
        crop_base_mesh(src, OUT / "01_base_meshes")
        print(f"cropped {src.name}")
    for src in veh:
        crop_vehicle(src, OUT / "03_vehicles")
        print(f"cropped {src.name}")
    print(f"done: {len(base)} base meshes, {len(veh)} vehicles")
    return 0


if __name__ == "__main__":
    sys.exit(main())
