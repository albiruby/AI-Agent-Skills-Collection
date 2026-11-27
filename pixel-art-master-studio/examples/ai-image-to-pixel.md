# Example: AI Image to Authentic Pixel Art

## Brief

Use a generated character concept as a reference, then produce a clean 32x32 sprite with an approved 16-color palette. The result must be labeled accurately.

## 1. Generate a reference (optional)

Prompt pattern:

```text
Full-body character concept, hooded forest runner, side view, strong silhouette,
limited dusk palette (#0f0f1b, #3a6ea5, #ef7d57, #f4f4f4),
flat colors, no text, plain neutral background, concept art reference.
```

This is a **reference**, not production pixel art. A model may ignore the grid/palette.

## 2. Inspect at 800%

Check:

- Real pixel grid vs simulated pixels (mixels).
- Soft edges, gradients, anti-aliasing, JPEG noise.
- Palette count and off-palette colors.
- Broken anatomy, extra limbs, merged props, fake text.
- Background/alpha.

Record why the image is not yet usable.

## 3. Build the target sprite

1. Choose the final 32x32 cell and pivot.
2. Downscale to the target grid using nearest-neighbor if the source is pixel-like; otherwise redraw.
3. Block the silhouette in one flat palette color.
4. Redraw the face, hands, weapon, and outline at the final grid.
5. Quantize to the approved palette; map each color to a ramp.
6. Remove orphan pixels, unintended dithering, and stray highlights.
7. Convert sprite alpha to binary; remove halos.

## 4. Palette and QA

```bash
python scripts/palette_ramp.py "#3a6ea5" --steps 5 --format hex
python scripts/pixel_art_qa.py export/hero_idle_side_00_32x32.png \
  --max-colors 16 --palette "<approved hex list>" --cell 32x32
```

Check at 1x gameplay size and 4x zoom. If it only reads at 4x, simplify.

## 5. Animation from AI references

- Generate one key pose at a time; do not trust a full sheet.
- Rebuild key poses and in-betweens on the real grid.
- Lock pivot/foot baseline and frame durations.
- Check frame-to-frame volume, head size, weapon length.
- Use `../templates/sprite-animation-plan.md`.

## 6. Label the result

- **Authentic pixel art:** authored on the final grid with approved palette/clusters.
- **Converted pixel style:** downscaled/quantized raster; state the method.
- **AI draft/reference:** not final production art.
- **Hybrid:** mixed methods with explicit per-layer rules.

## 7. Handoff

Include the source reference, prompt/tool, cleanup steps, palette, QA results, and authenticity label. Do not claim the model produced a production-ready sprite.
