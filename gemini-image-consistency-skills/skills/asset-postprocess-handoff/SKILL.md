---
name: asset-postprocess-handoff
description: Post-processes generated images into production-ready assets and hands them off - crop, key-color background removal with fringe cleanup, nearest-neighbor downscale, palette snapping, sheet slicing, baseline alignment, naming, atlas metadata, folder structure and provenance notes. Use after image generation when assets must go into a game, app, website or print workflow, or when the user asks how to clean up, slice, or export AI-generated sprites and images. Written for Gemini image generation (Nano Banana family, Imagen) in the Gemini app, AI Studio, API, Google Flow and Gemini CLI.
---

# Asset Post-Process & Handoff

## Purpose
Models give "close" images. Post-processing makes them exact, small, transparent and consistent.

## Pipeline
1. **Select** approved outputs only (QA verdict PASS).
2. **Crop** to the sheet band or subject with a fixed margin.
3. **Remove key color**: tolerance threshold on the flat background (e.g. #FF00FF); then clean edge fringes (erode 1 px or recolor pink-tinted edge pixels to the nearest palette color).
4. **Slice** sheets into N equal cells (width / N); verify each cell contains one frame.
5. **Normalize**: align feet baseline, center horizontally, scale all frames of a character by the same factor.
6. **Downscale** with nearest-neighbor to the target cell size (e.g. 32x32, 64x64). Never use smooth resampling for pixel art.
7. **Snap to palette**: map colors to the project palette to remove stray shades.
8. **Export** PNG with alpha; keep the master (large) version.
9. **Name** per manifest ID: `TM-WALK-DOWN_6f_32.png` (id, frames, cell size).
10. **Atlas data**: produce a JSON/atlas for the engine (frame size, count, anchor) or per-tool format.

## Minimal Python (Pillow) snippets
```python
from PIL import Image
import numpy as np

def remove_key(path, key=(255,0,255), tol=60):
    im = Image.open(path).convert("RGBA"); a = np.array(im)
    d = np.abs(a[...,:3].astype(int) - key).sum(axis=2)
    a[d < tol, 3] = 0
    return Image.fromarray(a)

def slice_row(im, n):
    w, h = im.size; cw = w // n
    return [im.crop((i*cw, 0, (i+1)*cw, h)) for i in range(n)]

def to_size(im, size):                      # nearest-neighbor for pixel art
    return im.resize((size, size), Image.NEAREST)
```
For real sheets, trim each frame to its bounding box, then paste into a square canvas aligned to a shared baseline before resizing.

## Folder structure
```
assets/
  characters/<name>/<animation>_<dir>.png
  tiles/  props/  items/  ui/  vfx/  backgrounds/
  _masters/   (original large images)
  _atlas/     (json)
  MANIFEST.md  QA_LOG.md  CHANGELOG.md
```

## Handoff checklist
- [ ] IDs match the manifest; no duplicates
- [ ] All frames equal size; transparent PNG; no pink fringe
- [ ] Palette matches the bible; scale consistent per character
- [ ] Mirrored directions documented
- [ ] Atlas/metadata provided
- [ ] Provenance note: generated with <model>, date, prompt pack version; check the provider's terms on commercial use and any watermark/provenance metadata
- [ ] Bible version recorded

## Pitfalls
- Downscaling before removing the key color (pink blends into edges).
- Normalizing each frame independently; it breaks the animation.
- Losing the master images.

## Gemini notes
- Images from Google models may carry provenance marks (such as invisible watermarking) and the app may add visible marks in some cases. Note this in the handoff and check Google's current terms for commercial use.
