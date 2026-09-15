#!/usr/bin/env python3
"""
images_to_glb.py — Convert 2D concept-art images into 3D GLB models.

Each image becomes a solid "embossed relief" block:
  * a flat bottom plate
  * four side walls following the image's edge profile
  * a wavy top surface whose height is derived from the image luminance
  * the original art embedded as a JPEG texture on the top surface

Output is a spec-compliant glTF 2.0 binary (.glb) file, written with a
hand-rolled GLB encoder (no external 3D libraries required — just numpy + pillow).

Usage:
    python tools/images_to_glb.py [SRC_ROOT] [OUT_ROOT] [LIMIT] [GRID] [TEX_MAX] [JQ]

Defaults:
    SRC_ROOT = concept_art
    OUT_ROOT = glb_models
    LIMIT    = 0   (0 = all images)
    GRID     = 44  (relief cells along the long edge)
    TEX_MAX  = 512 (max texture size, long edge, px)
    JQ       = 72  (embedded JPEG quality)
"""

import io
import json
import struct
import sys
import time
from pathlib import Path

import numpy as np
from PIL import Image, ImageFilter, ImageOps

WORLD_W = 2.0      # world units along the long (x) edge
AMP = 0.45         # relief amplitude (world units)
BASE_H = 0.06      # minimum slab thickness (world units)
BLUR_SIGMA = 0.9   # gaussian smoothing of the heightmap (cells)

IMG_EXTS = {".jpg", ".jpeg", ".png", ".webp", ".bmp"}


# --------------------------------------------------------------------------
# Geometry
# --------------------------------------------------------------------------
def build_relief(height: np.ndarray, W: float, H: float):
    """Build a solid relief block.

    height: (ny+1) x (nx+1) array of top-surface heights in [0, 1].
    Returns (positions float32 N x 3, uvs float32 N x 2, indices).
    """
    ny, nx = height.shape[0] - 1, height.shape[1] - 1
    Y = BASE_H + height * AMP

    xs = np.linspace(0.0, W, nx + 1)
    zs = np.linspace(0.0, H, ny + 1)
    X, Z = np.meshgrid(xs, zs)                      # (ny+1, nx+1)
    pos_top = np.stack([X, Y, Z], axis=-1).reshape(-1, 3).astype(np.float32)
    uv_top = np.stack([
        np.tile(np.linspace(0.0, 1.0, nx + 1), ny + 1),
        np.repeat(1.0 - np.linspace(0.0, 1.0, ny + 1), nx + 1),
    ], axis=-1).reshape(-1, 2).astype(np.float32)

    def g(i, j):                                    # top-grid vertex index
        return j * (nx + 1) + i

    positions = [pos_top]
    uvs = [uv_top]
    nverts = len(pos_top)
    idx = []

    for j in range(ny):
        for i in range(nx):
            a, b, c, d = g(i, j), g(i + 1, j), g(i, j + 1), g(i + 1, j + 1)
            idx += [(a, c, b), (c, d, b)]           # CCW from +y (top)

    def add_wall(edge, flip=False):
        """Walls from a top-grid edge (list of vertex indices) down to y=0."""
        nonlocal nverts, idx
        n = len(edge)
        top_pos = pos_top[edge]
        bot_pos = top_pos.copy()
        bot_pos[:, 1] = 0.0
        positions.append(bot_pos)
        uvs.append(np.stack([uv_top[edge][:, 0], np.zeros(n, dtype=np.float32)],
                            axis=-1))
        bbase = nverts
        nverts += n
        for k in range(n - 1):
            t0, t1 = edge[k], edge[k + 1]
            b0, b1 = bbase + k, bbase + k + 1
            if flip:                                # outward normal +edge dir
                idx += [(t0, b0, t1), (t1, b0, b1)]
            else:
                idx += [(t0, t1, b0), (t1, b1, b0)]

    add_wall([g(i, 0) for i in range(nx + 1)], flip=False)  # z=0, n=-z
    add_wall([g(i, ny) for i in range(nx + 1)], flip=True)  # z=H, n=+z
    add_wall([g(0, j) for j in range(ny + 1)], flip=True)   # x=0, n=-x
    add_wall([g(nx, j) for j in range(ny + 1)], flip=False) # x=W, n=+x

    # bottom face (normal -y)
    bbase = nverts
    positions.append(np.array([[0, 0, 0], [W, 0, 0], [W, 0, H], [0, 0, H]],
                              dtype=np.float32))
    uvs.append(np.array([[0, 0], [1, 0], [1, 0], [0, 0]], dtype=np.float32))
    idx += [(bbase, bbase + 1, bbase + 3), (bbase + 1, bbase + 2, bbase + 3)]

    pos = np.concatenate(positions)
    uv = np.concatenate(uvs)
    ind = np.asarray(idx, dtype=np.int64).reshape(-1, 3)
    ind = ind.astype(np.uint16) if ind.max() < 65536 else ind.astype(np.uint32)

    # smooth vertex normals (area-weighted face-normal accumulation)
    v0, v1, v2 = pos[ind[:, 0]], pos[ind[:, 1]], pos[ind[:, 2]]
    fn = np.cross(v1 - v0, v2 - v0)
    nrm = np.zeros_like(pos)
    np.add.at(nrm, ind[:, 0], fn)
    np.add.at(nrm, ind[:, 1], fn)
    np.add.at(nrm, ind[:, 2], fn)
    nrm /= (np.linalg.norm(nrm, axis=1, keepdims=True) + 1e-12)
    return pos, uv, nrm, ind


def heightmap_from_image(img: Image.Image, nx: int, ny: int) -> np.ndarray:
    lum = img.convert("L").resize((nx + 1, ny + 1), Image.LANCZOS)
    t = np.asarray(lum, dtype=np.uint8)
    t = np.asarray(Image.fromarray(t)
                   .filter(ImageFilter.GaussianBlur(BLUR_SIGMA)),
                   dtype=np.float32) / 255.0
    lo, hi = float(t.min()), float(t.max())
    if hi - lo < 1e-4:
        return np.zeros_like(t)
    return (t - lo) / (hi - lo)


# --------------------------------------------------------------------------
# GLB encoding
# --------------------------------------------------------------------------
def _pad4(b: bytes, pad: bytes) -> bytes:
    r = len(b) % 4
    return b + (pad * (4 - r) if r else b"")


def encode_glb(name: str, pos, uv, nrm, idx, jpeg_bytes: bytes) -> bytes:
    pos_b, uv_b, nrm_b, idx_b = (pos.tobytes(), uv.tobytes(),
                                 nrm.tobytes(), idx.tobytes())

    n_off = 0
    u_off = n_off + len(pos_b)
    r_off = u_off + len(uv_b)
    i_off = r_off + len(nrm_b)
    img_off = i_off + len(idx_b) + ((4 - ((i_off + len(idx_b)) % 4)) % 4)
    img_end = img_off + len(jpeg_bytes)
    bin_len = img_end + ((4 - (img_end % 4)) % 4)

    bin_buf = bytearray(bin_len)
    bin_buf[n_off:n_off + len(pos_b)] = pos_b
    bin_buf[u_off:u_off + len(uv_b)] = uv_b
    bin_buf[r_off:r_off + len(nrm_b)] = nrm_b
    bin_buf[i_off:i_off + len(idx_b)] = idx_b
    bin_buf[img_off:img_off + len(jpeg_bytes)] = jpeg_bytes

    n, m = len(pos), len(idx)
    json_doc = {
        "asset": {"version": "2.0",
                  "generator": "Hustle-and-Heir images_to_glb.py (relief extrusion)"},
        "scene": 0,
        "scenes": [{"name": "Scene", "nodes": [0]}],
        "nodes": [{"name": name, "mesh": 0}],
        "meshes": [{
            "name": name,
            "primitives": [{
                "attributes": {"POSITION": 0, "NORMAL": 1, "TEXCOORD_0": 2},
                "indices": 3,
                "material": 0,
                "mode": 4,
            }],
        }],
        "materials": [{
            "name": f"{name}_tex",
            "pbrMetallicRoughness": {
                "baseColorTexture": {"index": 0},
                "metallicFactor": 0.0,
                "roughnessFactor": 1.0,
            },
        }],
        "images": [{"name": f"{name}.jpg", "mimeType": "image/jpeg",
                    "bufferView": 4}],
        "textures": [{"sampler": 0, "source": 0}],
        "samplers": [{"magFilter": 9729, "minFilter": 9987,
                      "wrapS": 10497, "wrapT": 10497}],
        "accessors": [
            {"bufferView": 0, "componentType": 5126, "count": n, "type": "VEC3",
             "min": pos.min(axis=0).tolist(), "max": pos.max(axis=0).tolist()},
            {"bufferView": 2, "componentType": 5126, "count": n, "type": "VEC3"},
            {"bufferView": 1, "componentType": 5126, "count": n, "type": "VEC2"},
            {"bufferView": 3, "componentType": 5123 if idx.dtype == np.uint16
             else 5125, "count": m * 3, "type": "SCALAR"},
        ],
        "bufferViews": [
            {"buffer": 0, "byteOffset": n_off, "byteLength": len(pos_b),
             "target": 34962},
            {"buffer": 0, "byteOffset": u_off, "byteLength": len(uv_b),
             "target": 34962},
            {"buffer": 0, "byteOffset": r_off, "byteLength": len(nrm_b),
             "target": 34962},
            {"buffer": 0, "byteOffset": i_off, "byteLength": len(idx_b),
             "target": 34963},
            {"buffer": 0, "byteOffset": img_off,
             "byteLength": len(jpeg_bytes)},
        ],
        "buffers": [{"byteLength": bin_len}],
    }
    json_p = _pad4(json.dumps(json_doc, separators=(",", ":")).encode("utf-8"),
                   b" ")

    glb = struct.pack("<III", 0x46546C67, 2,
                      12 + 8 + len(json_p) + 8 + bin_len)
    glb += struct.pack("<II", len(json_p), 0x4E4F534A) + json_p
    glb += struct.pack("<II", bin_len, 0x004E4942) + bytes(bin_buf)
    return glb


# --------------------------------------------------------------------------
# Per-image pipeline
# --------------------------------------------------------------------------
def convert_image(src: Path, dst: Path, grid: int, tex_max: int,
                  jq: int) -> int:
    img = Image.open(src)
    ImageOps.exif_transpose(img, in_place=True)
    img = img.convert("RGB")
    w, h = img.size

    if w >= h:
        nx = grid
        ny = max(2, int(round(grid * h / w)))
    else:
        ny = grid
        nx = max(2, int(round(grid * w / h)))
    H = WORLD_W * h / w
    height = heightmap_from_image(img, nx, ny)
    pos, uv, nrm, ind = build_relief(height, WORLD_W, H)

    scale = min(1.0, tex_max / max(w, h))
    tw, th = max(1, int(round(w * scale))), max(1, int(round(h * scale)))
    buf = io.BytesIO()
    img.resize((tw, th), Image.LANCZOS).save(buf, format="JPEG",
                                             quality=jq, optimize=True)
    jpeg_bytes = buf.getvalue()

    glb = encode_glb(src.stem, pos, uv, nrm, ind, jpeg_bytes)
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_bytes(glb)
    return len(glb)


def main() -> int:
    src_root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("concept_art")
    out_root = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("glb_models")
    limit = int(sys.argv[3]) if len(sys.argv) > 3 else 0
    grid = int(sys.argv[4]) if len(sys.argv) > 4 else 44
    tex_max = int(sys.argv[5]) if len(sys.argv) > 5 else 512
    jq = int(sys.argv[6]) if len(sys.argv) > 6 else 72

    images = sorted(p for p in src_root.rglob("*")
                    if p.is_file() and p.suffix.lower() in IMG_EXTS)
    if limit:
        images = images[:limit]
    print(f"converting {len(images)} images | grid={grid} "
          f"tex<={tex_max}px jq={jq} -> {out_root}/", flush=True)

    total = 0
    t0 = time.time()
    for k, src in enumerate(images, 1):
        dst = out_root / (src.relative_to(src_root).with_suffix(".glb"))
        try:
            total += convert_image(src, dst, grid, tex_max, jq)
        except Exception as e:  # keep the batch alive
            print(f"  !! {src}: {type(e).__name__}: {e}", flush=True)
        if k % 50 == 0 or k == len(images):
            el = time.time() - t0
            print(f"  {k}/{len(images)} done | {total/1e6:.1f} MB "
                  f"| {el:.0f}s | avg {el/k*1000:.0f} ms/img", flush=True)
    print(f"DONE {len(images)} images, {total/1e6:.2f} MB, "
          f"{time.time()-t0:.1f}s", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
