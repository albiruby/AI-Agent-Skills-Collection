---
name: aseprite-sprite-generation
description: Creates pixel-art sprites and sprite sheets in Aseprite, including characters, creatures, props, icons, equipment, and modular asset variants. Use when the user asks to draw a new sprite or sheet from scratch — a character, creature, item, icon, or a set of equipment variants.
---

# Sprite Generation

## Workflow
1. Determine asset class, intended display size, silhouette, view angle, animation needs, and style.
2. Confirm canvas dimensions and whether the deliverable is one sprite, a sheet, or a layered source file.
3. Define a small role-based palette: outline/shadow, deep shadow, base, light, highlight, accent. Adjust to the chosen style.
4. Block silhouette first. Check recognition at native resolution and at 1x zoom.
5. Establish large color masses and light direction.
6. Add anatomy, material cues, face, equipment, and selective texture only after the shape reads.
7. Clean clusters and remove stray pixels.
8. If variants are required, preserve shared proportions and palette rules.
9. Inspect transparency, edges, and canvas bounds.
10. Save source and export only after QA.

## Sprite design rules
- Prioritize readability over detail.
- Use deliberate clusters instead of noisy single-pixel speckling.
- Keep outlines consistent in thickness and hue.
- Avoid unintentional pillow shading; use a clear light source.
- Make material differences visible through value grouping and cluster shape, not just hue.
- Keep character anatomy and costume features stable across directions and frames.
- Do not upscale a small sprite by adding detail that cannot survive at native size.
- Follow requested palette limits; do not silently add colors.

## Character sheet checklist
- Front/side/back or requested views
- Neutral pose and proportion reference
- Palette swatches
- Distinct silhouette and readable face
- Consistent costume, accessories, and handedness
- Clear separation between frames/cells
- Transparent background if requested

## Props and icons
- Make the silhouette recognizable at intended size.
- Ensure interactive/gameplay-relevant parts are distinguishable.
- For icons, use a consistent optical weight and padding.
- For equipment variants, preserve anchor points and relative scale.

## Failure modes
- Too much detail for the resolution
- Inconsistent light source
- Outline colors that flatten the sprite
- One-pixel gaps, noisy clusters, inconsistent proportions
- Background accidentally opaque
- Different variants drifting in size or style

Use art-direction and QA sub-skills alongside this one for production assets.
