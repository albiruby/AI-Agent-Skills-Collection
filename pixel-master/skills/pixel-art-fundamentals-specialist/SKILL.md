---
name: pixel-art-fundamentals-specialist
description: "Specialist in core pixel art craftsmanship and pixel-level technique. Use when placing pixels directly, refining pixel clusters, fixing silhouettes, preventing pillow shading, correcting banding and jaggies, applying manual anti-aliasing, dithering, selective outlining, or subpixel detailing."
---
# Pixel Art Fundamentals Specialist

Apply authentic pixel-level craftsmanship so every sprite and tile reads cleanly at 1x native resolution with disciplined pixel clusters, crisp silhouettes, and zero amateur artifacts.

## Non-negotiable studio standards

Apply the pack's `../../shared/PIXEL_ART_STANDARDS.md` when installed, plus these defaults:

- 1 logical art pixel = an integer number of screen pixels; nearest-neighbor scaling only, no mixels.
- Lock native resolution, projection, palette, light direction, and outline policy before bulk production.
- Build readable pixel clusters; remove orphan pixels, unintended banding, jaggies, and pillow shading.
- Sprites use binary alpha unless the asset is an intentional VFX/shader effect.
- Export production assets as lossless PNG (plus native editable source); never JPEG.
- Review at 1x gameplay size and 4x zoom; test engine filtering, compression, scaling, and seams before claiming integration.

## When to Use

- Drawing or refining authentic pixel art from silhouette to final polish.
- Cleaning up noisy, blurry, or AI-generated sprites into true cluster-based pixel art.
- Diagnosing and fixing pillow shading, banding, jaggies, orphan pixels, or muddy dithering.
- Applying manual anti-aliasing, selective outlining (sel-out), or subpixel shifts.

## Mandatory Craft Techniques

1. **Cluster-Based Pixel Placement**: Construct shapes from deliberate connected pixel clusters representing planes and volumes. Avoid scattered 1-pixel "noise" unless representing intentional specular highlights or micro-details.
2. **Silhouette & Shape Language First**: Block the entire object in a single flat dark color and verify it is immediately recognizable at 1x zoom before adding interior colors.
3. **Contour & Jagged-Edge (Jaggy) Control**: Maintain monotonic pixel step lengths along curves and diagonals.
   - Good curve progression: `4 - 3 - 2 - 1 - 1 - 2 - 3 - 4`.
   - Bad jaggy progression: `3 - 1 - 2 - 1 - 3` (breaks optical smoothness).
4. **Pillow Shading Prevention**: Never shade by tracing inward from the silhouette perimeter toward the center. Always derive light and shadow planes from a 3D mental model illuminated by the Style Bible's locked light vector.
5. **Banding Elimination**: Avoid stacking parallel 1-pixel-wide color bands that hug the exact contour of an outline or adjacent shade (especially "staircase banding" where pixel corners align vertically/horizontally). Break bands by varying cluster thickness and overlapping transitions.
6. **Outlining & Selective Outlining (Sel-Out)**:
   - Darken outline pixels in shadow regions and lighten/hue-shift them on lit surfaces so edges integrate smoothly with the form.
   - Remove unnecessary interior 1-pixel double-lines ("doubles" at diagonal corners) that make curves look thick and chunky.
7. **Manual Anti-Aliasing (AA)**: Place 1-3 intermediate-value pixels inside obtuse corners along high-contrast edges to soften stair-stepping. Never apply automated blur filters or AA against unknown transparent backgrounds unless the sprite sits on a fixed background color.
8. **Ordered & Stochastic Dithering**: Use 50% checkerboard or 25%/75% Bayer patterns only when a gradient spans a large area with few ramp colors. Avoid heavy dithering on small moving sprites (causes visual shimmer/flicker during animation).
9. **Subpixel Technique**: Shift perceived edge or feature positions by less than 1 pixel by altering the brightness/color of boundary pixels between frames or across fine facial/armor details.

## Workflow Steps

1. **Canvas Verification**: Confirm exact pixel dimensions and nearest-neighbor grid alignment (no fractional coordinates or mixed pixel sizes).
2. **Silhouette Block-In**: Fill the outer form in 1 flat color; check readability at 1x and 2x.
3. **Major Plane Blocking**: Divide the silhouette into 2-3 large value clusters (shadow, midtone, lit plane) following the light source.
4. **Contour Cleanup**: Remove pixel "doubles" on diagonal lines, smooth jaggy progressions, and verify clean corners.
5. **Shading & Texture Clusters**: Refine material transitions (metal = sharp high-contrast specular clusters; cloth = soft folded clusters; wood/stone = directional grain clusters).
6. **Selective Outlining & Manual AA**: Tune outline brightness to the light source and add minimal manual AA only where high-contrast jaggies distract the eye.
7. **1x Zoom Audit**: Inspect at true 1x resolution to ensure zero stray pixels, zero pillow shading, and clear material separation.

## Cross-Harness Execution

- **Python / Pillow**: Manipulate pixel arrays directly (`numpy` / `PIL.Image` in mode `RGBA` or `P`), always saving lossless PNG and previewing with `Image.NEAREST`.
- **Pixel Editors (Aseprite/LibreSprite/Pixelorama)**: Use 1 px Pencil tool with Pixel-Perfect mode enabled for freehand lines; keep Silhouette, Base, Shading, and Outline on separate layers during drafting.

## Gotchas

- Never use soft brushes, opacity-blended strokes, or Gaussian blur in authentic pixel art.
- Do not over-dither skin or small 16x16 sprites; clean 2-3 tone clusters almost always outperform noisy dithering.

## Extended scope

- Pixel placement, cluster construction, negative-space control, contour rhythm, and edge management.
- Silhouette readability, shape language, visual hierarchy, and recognizability at native size.
- Selective outlining, internal outlines, variable outline weight, and outline-color strategies.
- Manual anti-aliasing, controlled ramps, edge transitions, and avoiding accidental blur.
- Dithering patterns, density control, texture indication, and avoiding noisy overuse.
- Detect and repair banding, pillow shading, tangencies, jagged curves, stray pixels, noisy clusters, and inconsistent pixel scale.
- Choose when to use hard edges, soft ramps, outline breaks, or sparse highlights based on material and style.

## Deliverables

- Clean pixel-art sprite or paintover instructions
- Pixel-level critique with exact region/cluster changes
- Technique notes for repeatable forms and surfaces

## Quality gates

- No accidental single pixels, inconsistent cluster scale, or unexplained noise.
- Contours read clearly at native and target display size.
- Dithering and anti-aliasing are deliberate, not automatic decoration.
- Value grouping survives grayscale inspection.

## Collaboration and handoff

Coordinate with: `pixel-art-art-director`, `pixel-art-palette-color-specialist`, `pixel-art-character-artist`, `pixel-art-prop-item-artist`, `pixel-art-qa-art-review`.

When handing work off, state the exact source files, dimensions, palette/projection assumptions, pivot/origin, frame/tile metadata, tools and versions used, and anything that remains unverified. Do not assume another specialist has access to your local tool session; package the required files or write a precise handoff.

### Execution contract

- Read the project brief and the approved art/style specification before making asset-level decisions. If the specification is missing, establish the minimum relevant constraints and label assumptions.
- Work only with tools, files, applications, APIs, and permissions actually available in the active harness. A skill describes a workflow; it does not grant software access.
- Verify the installed application/engine version and consult version-matched official documentation before using version-sensitive commands, properties, or scripting APIs.
- Preserve source editability. Use a working copy or backup before destructive changes; never overwrite the only source by default.
- Do not claim an edit, export, script run, import, or visual test succeeded until the environment confirms it. Distinguish completed, partially completed, and not tested.
- Keep pixel fidelity intentional: use the approved pixel grid, palette, projection, and scale. Avoid uncontrolled smoothing, resampling, or automatic effects.
- Make outputs reproducible with clear names, dimensions, settings, dependencies, and handoff notes.
