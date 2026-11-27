# Palette and Ramp Guide

## 1. Palette budgets

| Budget | Typical use |
|---|---|
| 2-4 colors | Micro icons, 1-bit UI, game jam prototypes |
| 8 colors | NES/Game Boy-like constraints, tiny sprites |
| 16 colors | Classic 16-bit characters/tiles, tight cohesion |
| 32 colors | Richer scenes while staying readable |
| 64+ colors | Detailed key art, larger scenes, modern pixel style |

A larger palette is not automatically better. Lock the budget and treat exceptions as deliberate.

## 2. Ramp structure

For each material, define a ramp:

```text
shadow-2 | shadow-1 | base | light-1 | highlight
```

- Shift hue: shadows toward blue/violet, highlights toward yellow/cream.
- Adjust saturation: often lower at extremes, higher in midtones.
- Adjust value: keep enough separation for readable clusters.
- Do not simply blend toward black/white; that produces dead, chalky ramps.

## 3. Value hierarchy

- Foreground/playable: highest contrast and clearest silhouette.
- Midground/interactive: medium contrast.
- Background/parallax: compressed value range and lower detail.
- UI: highest legibility; avoid competing with gameplay.
- Test in grayscale; if the hierarchy disappears, fix values before adding color.

## 4. Material separation

- Skin: warm midtone, subtle hue shift, soft highlights.
- Metal: high contrast, sharp specular, cool shadows.
- Cloth: broader midtones, less specular.
- Wood/stone: texture clusters, not random noise.
- Magic/energy: may use saturated accents and intentional semi-alpha VFX.

## 5. Palette file format

Record in the style bible:

```text
name: dusk-16
colors:
  0: #0b0c10  (outline)
  1: #1f2833  (shadow)
  2: #c5c6c7  (light)
  3: #66fcf1  (accent)
usage:
  outline: 0
  skin: [1, 2, 3]
  cloth: [1, 2]
```

Include index order; many engines and shaders depend on it.

## 6. Dithering

- Use ordered dithering or controlled checkerboards only when ramp steps are too wide.
- Avoid dithering on small animated sprites; it shimmers.
- Do not use dithering to hide a bad ramp or noisy silhouette.
- Keep patterns intentional and repeatable.

## 7. Accessibility and readability

- Do not rely on hue alone to distinguish gameplay-critical elements.
- Check common color-vision deficiencies; add shape/value cues.
- Keep contrast sufficient at 1x on the target display.
- Avoid tiny text made of single pixels; use a dedicated bitmap font and test at target size.

## 8. QA

- Count unique colors (`../scripts/pixel_art_qa.py --max-colors N`).
- Check palette compliance (`--palette "#..."`).
- Remove unapproved anti-aliasing colors.
- Check grayscale hierarchy.
- Verify palette consistency across the asset set and engine import.
