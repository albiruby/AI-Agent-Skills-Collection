# AI Pixel Generation and Cleanup

Guidance for using image-generation models as concept/reference tools without misrepresenting the result as authentic pixel art.

## 1. What image models usually get wrong

- **Mixels:** mixed pixel sizes inside one image; edges that are 2px in one place and 1px in another.
- **Soft edges:** anti-aliasing, gradients, and blur that survive downscaling.
- **Palette drift:** hundreds of colors, including colors that look similar but are not on the approved ramp.
- **Fake detail:** noisy textures, stray single pixels, and "pixel-ish" dithering that is not grid-aligned.
- **Inconsistent frames:** animation sheets where the character changes size, shape, palette, or pivot.
- **Text artifacts:** unreadable pseudo-letters, malformed icons, extra limbs, or merged props.
- **Transparency errors:** white/black halos, semi-transparent fringes, or a baked background.

Never call generated output "authentic pixel art" until it has been inspected and rebuilt on a real grid.

## 2. Prompt patterns

Use prompts as guidance, not guarantees. Example structure:

```text
Authentic pixel art sprite, 32x32 native grid, single character, front-facing idle,
limited 16-color palette (list hex values), flat fills, hard 1-pixel edges,
no anti-aliasing, no gradients, no blur, no text, no watermark,
transparent background, strong silhouette, centered on a 32x32 cell,
pivot at bottom-center, consistent pixel size.
```

For animation sheets, add:

```text
4-frame walk cycle, identical canvas and pivot in every frame,
same palette and proportions, frames arranged in a 4x1 grid,
no frame-to-frame scale drift, no motion blur.
```

Do not overload the prompt with dozens of negatives. Specify the grid, palette, silhouette, and view; fix the rest in cleanup.

## 3. Cleanup workflow

1. **Inspect at 400-800%.** Identify the real pixel grid, mixels, soft edges, palette count, and alpha fringe.
2. **Choose a target grid.** Native sprite size (16x16, 32x32, 48x48) and integer display scale.
3. **Downscale with nearest-neighbor** to the target grid when the source is pixel-like; avoid smooth interpolation.
4. **Quantize to the approved palette.** Map each pixel to the nearest approved color; prefer perceptual distance (Lab/OKLab) when available.
5. **Rebuild critical edges.** Redraw silhouette, face, hands, weapon, and outline pixels manually. Generated detail rarely survives a small grid.
6. **Clean alpha.** Convert to binary alpha for sprites; remove halos and semi-transparent fringe; keep partial alpha only for intentional VFX.
7. **Remove noise.** Delete orphan pixels, unintended dithering, stray highlights, and fake texture.
8. **Normalize frames.** Same canvas, pivot, baseline, palette, and proportions across all frames.
9. **QA and label.** Run `../scripts/pixel_art_qa.py`; state whether the result is authentic, converted pixel style, or hybrid.

## 4. Palette quantization notes

- Always use the project palette, not the model's palette.
- Preserve value hierarchy after quantization; a flat nearest-color map can collapse shadows and highlights.
- Check material ramps separately (skin, metal, cloth, wood) so they do not become one muddy ramp.
- Re-check contrast at 1x gameplay size and in grayscale.
- Keep a backup of the pre-quantized image for reference.

## 5. Animation consistency

- Generate one key pose at a time when possible; a full sheet often drifts.
- Use a locked reference image and explicit palette/grid instructions.
- Check frame bounds, pivot, foot baseline, head size, and weapon length across every frame.
- Rebuild motion arcs and timing manually; generated frames often have inconsistent spacing.
- Do not trust a model's frame count or timing; define the exposure sheet yourself.

## 6. Authenticity labels

Use precise language:

- **Authentic pixel art:** authored on the final grid with an approved palette and intentional clusters.
- **Converted pixel style:** a raster/3D image downscaled and quantized; acceptable for some styles, but not the same craft.
- **AI draft/reference:** generated concept, not final production art.
- **Hybrid:** authentic foreground sprites over a converted/3D background, with explicit rules.

## 7. If image tools are unavailable

Provide:

- The exact prompt, target grid, palette hex list, and view.
- A cleanup checklist and acceptance criteria.
- A manual procedure or script outline.
- An explicit statement that no image was generated or edited.

Do not claim an asset exists when only a prompt was produced.
