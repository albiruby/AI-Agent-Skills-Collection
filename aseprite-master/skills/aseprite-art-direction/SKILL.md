---
name: aseprite-art-direction
description: Defines and maintains pixel-art visual direction, silhouette, palette, lighting, material language, and consistency across assets. Use when the user wants a style guide, palette ramp, outline policy, or lighting rules defined, or when new assets risk drifting from an established pixel-art look.
---

# Art Direction and Consistency

## Build a mini style guide
Record:
- Era / reference style (e.g. 8-bit, 16-bit, retro handheld, PS1-inspired pixel look)
- Native resolution and pixel density
- Outline policy: dark outline, colored outline, selective outline, or none
- Palette size and ramps
- Light direction and contrast range
- Cluster density and texture rules
- Perspective and camera angle
- Character proportions and facial language
- Background contrast and transparency policy

## Palette workflow
- Group colors by material or ramp.
- Ensure each ramp has useful value separation.
- Reserve accent colors for focal points.
- Check grayscale/value readability.
- Avoid adding near-duplicate colors without a reason.
- Maintain shared colors across related assets when appropriate.

## Pixel cluster rules
- Prefer purposeful 2–5 pixel groupings where resolution allows.
- Avoid accidental stair-step rhythm, tangents, noisy dithering, and isolated pixels.
- Use dithering only when it contributes to texture or value transition.
- Keep diagonals intentional and consistent with the sprite's pixel scale.

## Lighting and materials
- Choose one dominant light direction unless the brief says otherwise.
- Differentiate metal, cloth, skin, wood, stone, magic, and glass through shape and value patterns.
- Highlights should support form, not decorate every edge.
- Maintain shadow direction across all animation frames.

## Style continuity
Maintain a short asset bible for recurring characters:
- body proportions
- head-to-body ratio
- face placement
- palette swatches
- clothing and accessory positions
- outline and shading policy
- signature shapes
- allowed animation deformations

Compare every new asset to the style guide. If a reference conflicts with the established style, identify the conflict rather than blending styles accidentally.
