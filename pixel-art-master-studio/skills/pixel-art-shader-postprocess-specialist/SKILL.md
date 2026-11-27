---
name: pixel-art-shader-postprocess-specialist
description: "Specialist in pixel art shaders and post-processing effects. Use when writing or configuring pixelation shaders, nearest-neighbor sampling, palette quantization LUT shaders, ordered Bayer dithering shaders, pixel-clean outline shaders, CRT/scanline effects, or 2D normal-mapped pixel lighting."
---
# Pixel Art Shader & Post-Process Specialist

Design real-time shaders and post-processing pipelines (GLSL, HLSL, Godot Shader, Unity URP/ShaderGraph) that deliver crisp Pixel Style rendering, indexed palette swapping, dithering, clean outlines, and optional retro CRT presentation.

## Non-negotiable studio standards

Apply the pack's `../../shared/PIXEL_ART_STANDARDS.md` when installed, plus these defaults:

- 1 logical art pixel = an integer number of screen pixels; nearest-neighbor scaling only, no mixels.
- Lock native resolution, projection, palette, light direction, and outline policy before bulk production.
- Build readable pixel clusters; remove orphan pixels, unintended banding, jaggies, and pillow shading.
- Sprites use binary alpha unless the asset is an intentional VFX/shader effect.
- Export production assets as lossless PNG (plus native editable source); never JPEG.
- Review at 1x gameplay size and 4x zoom; test engine filtering, compression, scaling, and seams before claiming integration.

## When to Use

- Implementing real-time pixelation or low-resolution viewport upscaling shaders.
- Writing GPU palette-swap shaders (1D LUT texture lookup) or palette quantization + Bayer dithering post-process shaders.
- Creating 1-pixel sprite outline shaders, hit-flash shaders, dissolve effects, or 2D normal-mapped dynamic lighting that preserves pixel grid integrity.
- Building authentic, toggleable CRT/scanline/phosphor post-processing passes.

## Core Shader Standards

1. **Strict Nearest-Neighbor & Subpixel-Safe Sampling**:
   - Sample pixel textures at exact texel centers (`(floor(uv * texSize) + 0.5) / texSize`) to avoid half-pixel shift and shimmering.
   - For smooth scrolling or non-integer screen resolutions, use sharp-bilinear / pixel-art AA upscaling (upscaling only across the 1-pixel boundary transition) rather than blurry bilinear filtering.
2. **Indexed Palette Swap & Quantization**:
   - **Palette Swap (Hero/Enemy Variants)**: Store grayscale index values in the sprite texture and look up final RGBA from a `Nx1` palette LUT texture with `Nearest` filtering for zero-cost runtime recolors and day/night cycling.
   - **Color Quantization + Ordered Dither**: Apply a 4x4 or 8x8 Bayer threshold matrix in screen-space pixel coordinates (`mod(fragCoord, 4.0)`) before snapping to the nearest palette color so dithering stays locked to the pixel grid without swimming.
3. **Pixel-Clean Outlines**: Sample 4-neighbor (cardinal) or 8-neighbor offsets at exact `1.0 / texSize` steps in alpha; ensure sprites have at least 1 px transparent padding around the canvas so outlines are never clipped by quad bounds.
4. **CRT & Retro Post-Processing (Optional & Toggleable)**: Keep scanlines, subtle phosphor aperture grille, gentle curvature, and bloom restrained so text and small icons remain effortless to read, and always provide an accessibility toggle to disable CRT effects.

## Workflow Steps

1. **Confirm Target Engine & Pipeline**: Identify shader language (Godot `canvas_item`/`spatial`, Unity HLSL/URP, WebGL/GLSL, GameMaker GLSL ES) and render order (per-sprite vs. full-screen post-process).
2. **Specify Uniforms & Inputs**: Define palette LUT textures, pixel grid resolution uniform, Bayer matrix size, outline color, and blend parameters.
3. **Write Clean, Commented Shader Code**: Avoid heavy branching inside fragment loops; precompute constants and clamp UVs cleanly.
4. **Validate Visual Integrity**: Test at 1x, 2x, 3x, and non-integer (e.g., 1080p / 1440p) viewports to verify zero pixel crawl, zero edge clipping, and stable frame times.

## Gotchas

- Applying post-process bloom or chromatic aberration *before* pixel quantization destroys clean pixel clusters; run pixelation/quantization at native art resolution first, then apply optional CRT/display effects at final display resolution.
- Never sample a 4x4 Bayer matrix using UV coordinates that stretch with aspect ratio; always index it by integer native pixel coordinates.

## Extended scope

- Low-resolution render targets, nearest-neighbor sampling, integer scaling, viewport/camera snapping, and stable pixel grids.
- Palette quantization, ordered dithering, Bayer matrices, color ramps, posterization, and controlled color banding.
- Outline/depth/normal-based effects, edge detection, silhouette emphasis, and selective contour rendering.
- CRT scanlines, phosphor masks, curvature, chromatic aberration, and noise as optional effects—not default pixel-art requirements.
- Shader parameter design, performance-aware implementation, and engine/version-specific verification.
- Separate world rendering, UI rendering, and post-process stages to prevent unwanted pixelation of text or UI.
- Debug sampling artifacts, shimmer, moiré, subpixel jitter, and inconsistent edge thickness.

## Deliverables

- Shader/material source and setup notes
- Parameter reference and sample scene where possible
- Visual comparison and performance observations
- Known limitations by renderer/platform

## Quality gates

- Pixel grid remains stable during camera movement.
- Texture filtering and scaling preserve intended pixel edges.
- Effects do not compromise HUD or gameplay readability.
- Performance is measured on target hardware when available.

## Collaboration and handoff

Coordinate with: `pixel-art-3d-render-pipeline-specialist`, `pixel-art-game-engine-integration`, `pixel-art-optimization-performance`, `pixel-art-qa-art-review`.

When handing work off, state the exact source files, dimensions, palette/projection assumptions, pivot/origin, frame/tile metadata, tools and versions used, and anything that remains unverified. Do not assume another specialist has access to your local tool session; package the required files or write a precise handoff.

### Execution contract

- Read the project brief and the approved art/style specification before making asset-level decisions. If the specification is missing, establish the minimum relevant constraints and label assumptions.
- Work only with tools, files, applications, APIs, and permissions actually available in the active harness. A skill describes a workflow; it does not grant software access.
- Verify the installed application/engine version and consult version-matched official documentation before using version-sensitive commands, properties, or scripting APIs.
- Preserve source editability. Use a working copy or backup before destructive changes; never overwrite the only source by default.
- Do not claim an edit, export, script run, import, or visual test succeeded until the environment confirms it. Distinguish completed, partially completed, and not tested.
- Keep pixel fidelity intentional: use the approved pixel grid, palette, projection, and scale. Avoid uncontrolled smoothing, resampling, or automatic effects.
- Make outputs reproducible with clear names, dimensions, settings, dependencies, and handoff notes.
