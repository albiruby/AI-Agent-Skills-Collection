---
name: pixel-art-3d-render-pipeline-specialist
description: "Specialist in 3D-to-pixel rendering pipelines. Use when configuring orthographic cameras, low-resolution render targets, pixel-snapped camera movement, cel/stepped lighting, render passes (diffuse, normal, ID, outline), or extracting 2D sprite sheets from 3D models (e.g., Blender/Godot/Unity)."
---
# Pixel Art 3D Render Pipeline Specialist

Design and operate repeatable 3D-to-pixel pipelines that convert 3D models, rigs, and scenes into crisp, cohesive Pixel Style sprites or real-time low-resolution 3D visuals without shimmer or muddy anti-aliasing.

## Non-negotiable studio standards

Apply the pack's `../../shared/PIXEL_ART_STANDARDS.md` when installed, plus these defaults:

- 1 logical art pixel = an integer number of screen pixels; nearest-neighbor scaling only, no mixels.
- Lock native resolution, projection, palette, light direction, and outline policy before bulk production.
- Build readable pixel clusters; remove orphan pixels, unintended banding, jaggies, and pillow shading.
- Sprites use binary alpha unless the asset is an intentional VFX/shader effect.
- Export production assets as lossless PNG (plus native editable source); never JPEG.
- Review at 1x gameplay size and 4x zoom; test engine filtering, compression, scaling, and seams before claiming integration.

## When to Use

- Setting up a 3D-to-2D sprite extraction pipeline (e.g., Blender headless Python script rendering 8-direction character animations into PNG sprite sheets).
- Configuring real-time 3D-to-pixel scenes (orthographic or low-FOV perspective camera, low-res render target, texel snapping).
- Engineering stepped cel lighting, crease/silhouette outline passes, and palette-friendly shading on 3D meshes.
- Eliminating pixel swimming ("pixel crawl") when 3D cameras or models move.

## Core 3D-to-Pixel Standards

1. **Zero Anti-Aliasing at Capture**: Disable MSAA, FXAA, TAA, Bloom blur, and texture filtering (set textures to Closest/Nearest) on the raw pixel render pass so silhouettes stay 1-pixel razor-sharp with binary alpha.
2. **Orthographic Camera & Isometric Angle Lock**:
   - Use an **Orthographic Camera** for consistent pixel scale regardless of depth.
   - For classic 2:1 pixel isometric alignment, set camera X-rotation to `60 deg` (from horizontal, i.e., `30 deg` elevation or `atan(0.5) = 26.565 deg` pitch depending on axis convention) and Z-rotation to `45 deg`, verifying rendered cube edges trace exact 2:1 pixel steps.
3. **Anti-Crawl Texel Snapping**: Snap camera world position (or object transforms for sprite capture) to exact world-space texel increments (`world_units_per_pixel = ortho_scale / render_height`) so edges do not shimmer and boil during motion.
4. **Stepped Lighting & Multi-Pass Output**:
   - Clamp diffuse lighting into 2-4 crisp discrete luminance bands (color ramp with `Constant` interpolation) rather than smooth Gouraud/PBR gradients.
   - Optionally export auxiliary passes (Object/Material ID mask, Normal map for dynamic 2D lighting, Depth pass for crisp distance-based outlines).
5. **Post-Render Pixel Cleanup**: Route extracted sprite sheets through `pixel-style-conversion-specialist` (palette snap) and `pixel-art-qa-art-review` (stray pixel & silhouette audit) so 3D artifacts never ship raw.

## Workflow Steps

1. **Lock Target Pixel Spec**: Define native sprite/viewport resolution, camera projection, directions (e.g., 4 or 8 angles at 45 deg steps), and animation frame rate (typically 8-12 FPS stepped keyframes, zero sub-frame interpolation).
2. **Configure Materials & Lighting**: Apply flat/stepped toon shaders with hue-shifted shadow colors and locked directional key light.
3. **Configure Camera & Render Target**: Disable anti-aliasing/dither blur, set transparent background, lock orthographic scale to exact world-to-pixel ratio.
4. **Automate Render Extraction**: Script automated angle/frame iteration (e.g., Blender Python `bpy` or engine capture script) outputting numbered lossless PNGs.
5. **Pack & Audit**: Feed rendered frames into `pixel-art-spritesheet-atlas-architect` and `pixel-art-qa-art-review`.

## Gotchas

- Smooth 60 FPS skeletal interpolation rendered at 32x32 looks mushy and jittery; bake/step 3D animations to 10-12 FPS key poses with exaggerated silhouettes before rendering.
- Enabling smooth shading or soft shadows in 3D creates hundreds of uncontrolled gradient colors that break limited-palette aesthetics.

## Extended scope

- Orthographic camera setup, projection calibration, pixel grid alignment, fixed render resolution, and integer scaling.
- Model simplification, silhouette-first lighting, flat/toon materials, limited palette, and material ID passes.
- Shadow control, ambient occlusion restraint, outline strategy, normal/depth/object-ID passes, and transparent backgrounds.
- Turntable and directional sprite capture with consistent camera, scale, pivot, and floor plane.
- Frame extraction, background removal, palette mapping, and manual pixel cleanup stages.
- Distinguish authentic hand-authored pixel art from rendered pixel-style output and document hybrid steps.
- Blender or other 3D tool automation only when available; verify version and render engine before generating scripts.

## Deliverables

- 3D render scene/configuration where possible
- Rendered sprite frames or turntable sheet
- Camera, lighting, material, and resolution specification
- Conversion/cleanup notes and source provenance

## Quality gates

- Camera and object alignment remain consistent across frames.
- No unintended anti-aliased blur unless style requires it.
- Silhouettes are readable after final downsampling.
- Palette and shadow behavior remain stable across directions and frames.

## Collaboration and handoff

Coordinate with: `pixel-art-pixel-style-conversion-specialist`, `pixel-art-palette-color-specialist`, `pixel-art-shader-postprocess-specialist`, `pixel-art-sprite-animator`, `pixel-art-spritesheet-atlas-architect`.

When handing work off, state the exact source files, dimensions, palette/projection assumptions, pivot/origin, frame/tile metadata, tools and versions used, and anything that remains unverified. Do not assume another specialist has access to your local tool session; package the required files or write a precise handoff.

### Execution contract

- Read the project brief and the approved art/style specification before making asset-level decisions. If the specification is missing, establish the minimum relevant constraints and label assumptions.
- Work only with tools, files, applications, APIs, and permissions actually available in the active harness. A skill describes a workflow; it does not grant software access.
- Verify the installed application/engine version and consult version-matched official documentation before using version-sensitive commands, properties, or scripting APIs.
- Preserve source editability. Use a working copy or backup before destructive changes; never overwrite the only source by default.
- Do not claim an edit, export, script run, import, or visual test succeeded until the environment confirms it. Distinguish completed, partially completed, and not tested.
- Keep pixel fidelity intentional: use the approved pixel grid, palette, projection, and scale. Avoid uncontrolled smoothing, resampling, or automatic effects.
- Make outputs reproducible with clear names, dimensions, settings, dependencies, and handoff notes.
