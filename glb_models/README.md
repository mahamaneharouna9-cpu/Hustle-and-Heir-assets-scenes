# GLB Models (3D conversion of all concept art)

Every one of the 822 concept-art images in `concept_art/` has been converted
into a 3D model in this folder, mirroring the original directory structure
(`glb_models/<category>/<name>.glb` sits next to the data of
`concept_art/<category>/<name>.jpg`).

## What each model is

Each `.glb` is a solid **embossed relief block**:

- a flat bottom plate,
- four side walls that follow the image's edge profile,
- a wavy top surface whose height is derived from the image's luminance
  (bright areas rise, dark areas sit low),
- the original artwork embedded as a JPEG texture on the top surface
  (512 px max, quality 72),
- smooth vertex normals baked in, so the relief shades smoothly in any viewer.

The block is 2.0 world units along its long edge, with a relief amplitude of
0.45 units. One mesh, one PBR material (metallic 0 / roughness 1) per file —
fully self-contained glTF 2.0 binary (geometry, normals, UVs and texture are
all inside the single file).

## Generating / regenerating

```bash
python tools/images_to_glb.py [SRC_ROOT] [OUT_ROOT] [LIMIT] [GRID] [TEX_MAX] [JQ]
# defaults: concept_art  glb_models  0  44  512  72
```

Requires only `numpy` + `pillow`. ~822 images take about 35 s.

- `GRID` — relief resolution (cells along the long edge, default 44)
- `TEX_MAX` — max embedded texture size in px (default 512)
- `JQ` — embedded JPEG quality (default 72)

## Notes

- Conversion is procedural (CPU-only). It is *not* AI single-image 3D
  reconstruction — the relief is a heightmap extrusion of the artwork, which
  is the best that's reproducible at this scale without GPU inference.
- Total size: ~81 MB across 822 files.
- Open any file in Blender, three.js, Unity (glTFast/VRM), Godot,
  Babylon.js, or online viewers (gltf.report, modelviewer.dev) — it is
  standard glTF 2.0.
