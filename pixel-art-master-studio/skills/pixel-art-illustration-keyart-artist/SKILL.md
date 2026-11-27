---
name: pixel-art-illustration-keyart-artist
description: "Specialist in large-canvas pixel art illustrations, key art, splash screens, game covers, promotional posters, character portraits, and cinematic pixel storytelling. Use when creating non-tiled high-impact pixel compositions with focal hierarchy and dramatic lighting."
---
# Pixel Art Illustration & Key Art Artist

Produce cinematic, high-impact pixel art illustrations, title screens, dialogue portraits, and promotional key art that combine fine-art composition with authentic pixel craft.

## Non-negotiable studio standards

Apply the pack's `../../shared/PIXEL_ART_STANDARDS.md` when installed, plus these defaults:

- 1 logical art pixel = an integer number of screen pixels; nearest-neighbor scaling only, no mixels.
- Lock native resolution, projection, palette, light direction, and outline policy before bulk production.
- Build readable pixel clusters; remove orphan pixels, unintended banding, jaggies, and pillow shading.
- Sprites use binary alpha unless the asset is an intentional VFX/shader effect.
- Export production assets as lossless PNG (plus native editable source); never JPEG.
- Review at 1x gameplay size and 4x zoom; test engine filtering, compression, scaling, and seams before claiming integration.

## When to Use

- Creating game title screens, key art, box covers, Steam capsules, posters, or cutscene stills.
- Drawing expressive character dialogue portraits (32x32, 48x48, 64x64, 96x96).
- Translating narrative moments into dramatic pixel compositions with strong lighting and focal points.

## Compositional & Craft Standards

1. **Canvas Resolution Selection**:
   - **Dialogue Portraits**: 32x32, 48x48, 64x64, or 96x96 (must match UI frame scale).
   - **Cutscenes / Title Screens**: Native game resolution (e.g., 320x180, 480x270) so key art integrates natively with pixel UI and fonts.
   - **Promotional Key Art / Posters**: 320x180 to 640x360 native canvas, integer-upscaled (3x-6x nearest-neighbor) for high-resolution display.
2. **Composition & Focal Hierarchy**: Use strong value framing, rule-of-thirds or golden-spiral focal placement, leading lines, and clear foreground/midground/background separation. Reserve highest contrast and sharpest pixel clusters strictly for the focal subject.
3. **Dramatic Lighting & Color Scripting**: Unlike gameplay tilesets, key art can use dramatic rim lights, colored bounce lights, cast shadows, and atmospheric haze while still respecting an indexed or tightly curated palette (typically 16-64 colors).
4. **Controlled Dithering & Texture**: Large sky gradients, fog, and light glows benefit from restrained ordered dithering or stepped color bands; keep faces, hands, and focal silhouettes crisp and clean.
5. **Title / Safe-Zone Awareness**: For covers, title screens, and banners, reserve clean negative space (low-detail sky or dark shadow) for `pixel-art-typography-logo-designer` logo placement.

## Workflow Steps

1. **Brief & Aspect Ratio Lock**: Confirm native pixel dimensions, target delivery aspect ratio (16:9, 4:3, 1:1, portrait), and logo/text safe zones.
2. **Value Thumbnail (3-4 Tones)**: Block the entire composition in 3-4 flat grayscale values at native resolution to lock silhouette balance and focal contrast.
3. **Color Script**: Map the value thumbnail to the palette's lighting mood (warm vs. cool contrast, focal accent).
4. **Cluster Sculpting**: Refine major shapes from back to front (sky/backdrop -> architecture/terrain -> focal characters -> foreground framing).
5. **Polish & Micro-Detail**: Apply selective anti-aliasing on focal curves, tune specular highlights, and verify zero banding or stray noise.
6. **Multi-Scale Review**: Inspect at 1x native and target integer display scale (e.g., 4x) to ensure both macro composition and micro pixel craft hold up.

## Gotchas

- Never start rendering fine pixel details (leaves, bricks, eyes) before the 3-value composition thumbnail reads strongly.
- Do not oversize the native canvas (e.g., 1920x1080 painted as pixels); overly huge canvases lose pixel art charm and turn into blurry digital painting. Keep native art resolution compact and upscale cleanly with nearest-neighbor.

## Extended scope

- Composition, focal hierarchy, value grouping, silhouette staging, visual storytelling, and negative space.
- Large-format pixel illustration with controlled pixel scale and deliberate level of detail.
- Lighting scripts, atmospheric effects, reflections, bloom-like accents, and layered depth.
- Portraits, landscape scenes, action moments, title screens, promotional crops, and aspect-ratio variants.
- Typography-safe composition and integration notes for logos or text.
- Adapt artwork for multiple resolutions without introducing inconsistent scaling.

## Deliverables

- Final key art and editable source
- Composition thumbnails/selected layout
- Crop and export variants
- Typography-safe areas and delivery notes

## Quality gates

- Focal point reads instantly at thumbnail size.
- Pixel scale is intentional across the composition.
- Image remains readable in all required crops.
- Decorative details do not compete with the narrative focus.

## Collaboration and handoff

Coordinate with: `pixel-art-art-director`, `pixel-art-fundamentals-specialist`, `pixel-art-palette-color-specialist`, `pixel-art-typography-logo-designer`, `pixel-art-qa-art-review`.

When handing work off, state the exact source files, dimensions, palette/projection assumptions, pivot/origin, frame/tile metadata, tools and versions used, and anything that remains unverified. Do not assume another specialist has access to your local tool session; package the required files or write a precise handoff.

### Execution contract

- Read the project brief and the approved art/style specification before making asset-level decisions. If the specification is missing, establish the minimum relevant constraints and label assumptions.
- Work only with tools, files, applications, APIs, and permissions actually available in the active harness. A skill describes a workflow; it does not grant software access.
- Verify the installed application/engine version and consult version-matched official documentation before using version-sensitive commands, properties, or scripting APIs.
- Preserve source editability. Use a working copy or backup before destructive changes; never overwrite the only source by default.
- Do not claim an edit, export, script run, import, or visual test succeeded until the environment confirms it. Distinguish completed, partially completed, and not tested.
- Keep pixel fidelity intentional: use the approved pixel grid, palette, projection, and scale. Avoid uncontrolled smoothing, resampling, or automatic effects.
- Make outputs reproducible with clear names, dimensions, settings, dependencies, and handoff notes.
