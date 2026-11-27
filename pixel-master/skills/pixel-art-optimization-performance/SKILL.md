---
name: pixel-art-optimization-performance
description: "Specialist in pixel art technical optimization and runtime performance. Use when optimizing texture atlases, reducing VRAM footprint, batching draw calls, trimming unused palette colors, compressing PNG files losslessly, or profiling sprite-heavy scenes."
---
# Pixel Art Optimization & Performance

Maximize runtime rendering performance and minimize disk/VRAM footprint for pixel art games without sacrificing a single pixel of visual fidelity.

## Non-negotiable studio standards

Apply the pack's `../../shared/PIXEL_ART_STANDARDS.md` when installed, plus these defaults:

- 1 logical art pixel = an integer number of screen pixels; nearest-neighbor scaling only, no mixels.
- Lock native resolution, projection, palette, light direction, and outline policy before bulk production.
- Build readable pixel clusters; remove orphan pixels, unintended banding, jaggies, and pillow shading.
- Sprites use binary alpha unless the asset is an intentional VFX/shader effect.
- Export production assets as lossless PNG (plus native editable source); never JPEG.
- Review at 1x gameplay size and 4x zoom; test engine filtering, compression, scaling, and seams before claiming integration.

## When to Use

- Consolidating scattered sprite files into shared texture atlases to reduce GPU draw calls.
- Cutting VRAM usage on mobile, web, Switch, or retro-constrained platforms.
- Performing lossless PNG optimization, indexed palette reduction, and duplicate-frame deduplication.
- Diagnosing frame drops caused by overdraw, huge transparent sprite margins, or unbatched particle/tile layers.

## Core Optimization Standards

1. **Draw-Call & Atlas Batching**:
   - Group assets that render together on the same scene/layer (e.g., all Level 1 props + enemies, or all UI icons) into shared power-of-two atlases (`<= 2048x2048` safe limit for WebGL/mobile) to enable single-batch GPU drawing.
   - Separate assets that use different shaders or blend modes (e.g., additive VFX vs. opaque world tiles) so batching is never broken mid-pass.
2. **Trim Empty Space & Deduplicate Frames**:
   - Trim transparent outer padding in packed atlases (preserving exact pivot via metadata) to eliminate massive GPU fill-rate overdraw on large bosses or swing animations.
   - Reference identical repeated animation frames by index/duration rather than duplicating identical pixel cells in the sheet.
3. **Lossless Disk & Memory Efficiency**:
   - Convert flat-alpha assets to **indexed PNG (PNG-8)** on disk when supported by the pipeline, shrinking file size by 40-75% with zero pixel loss.
   - Never use lossy texture compression (BC1/DXT1/ETC1/JPEG) on pixel art; keep textures lossless RGBA8 or indexed LUT + shader when VRAM is tight.
4. **Palette-Swap Memory Savings**: Instead of storing 6 full-color sprite sheets for 6 enemy tiers or team colors, store 1 indexed grayscale sprite sheet + 6 tiny `32x1` palette LUT PNGs.

## Workflow Steps

1. **Profile Current Footprint**: Measure total atlas count, max texture dimensions, transparent pixel waste ratio, disk size, and scene draw calls.
2. **Consolidate & Trim Atlases**: Repack scattered files into scene-grouped atlases with trimmed rects, deduplicated frames, and 1-2 px safe padding.
3. **Optimize Palettes & Storage**: Strip unused palette indices, convert eligible PNGs to indexed lossless PNG, and convert recolor variants to palette LUTs.
4. **Verify Visual & Runtime Parity**: Confirm pixel-for-pixel visual identity before vs. after optimization and record before/after metrics (draw calls, VRAM MB, disk KB).

## Gotchas

- Over-packing unrelated levels into one giant 4096x4096 atlas forces the engine to load Level 5 textures into VRAM during Level 1 and can break older mobile/WebGL GPUs.
- Removing cell padding/extrusion to "save a few pixels" will immediately cause texture bleed and tile seam artifacts in-engine.

## Extended scope

- Measure texture memory, atlas dimensions, sprite counts, animation frame counts, file sizes, and draw-call implications.
- Choose atlas grouping, compression settings, texture formats, palette/indexed formats where supported, and streaming/loading strategies.
- Reduce redundant frames, duplicate assets, unnecessary colors, and excessive texture variants.
- Design LOD or resolution variants where appropriate without compromising pixel grid.
- Optimize tilemaps, batching, sprite sorting, and runtime update patterns in the target engine.
- Set target budgets for memory, loading time, atlas count, and platform-specific limits.
- Compare before/after metrics and record quality trade-offs.

## Deliverables

- Optimization report and measured baseline
- Optimized assets/configuration
- Atlas and memory budget recommendations
- Before/after visual and performance comparison

## Quality gates

- Optimization does not introduce blur, palette changes, frame loss, or atlas bleeding.
- Claims are based on measurements or explicitly labeled estimates.
- Original sources remain available.
- Target platform constraints are verified.

## Collaboration and handoff

Coordinate with: `pixel-art-spritesheet-atlas-architect`, `pixel-art-procedural-automation-engineer`, `pixel-art-game-engine-integration`, `pixel-art-production-delivery-manager`.

When handing work off, state the exact source files, dimensions, palette/projection assumptions, pivot/origin, frame/tile metadata, tools and versions used, and anything that remains unverified. Do not assume another specialist has access to your local tool session; package the required files or write a precise handoff.

### Execution contract

- Read the project brief and the approved art/style specification before making asset-level decisions. If the specification is missing, establish the minimum relevant constraints and label assumptions.
- Work only with tools, files, applications, APIs, and permissions actually available in the active harness. A skill describes a workflow; it does not grant software access.
- Verify the installed application/engine version and consult version-matched official documentation before using version-sensitive commands, properties, or scripting APIs.
- Preserve source editability. Use a working copy or backup before destructive changes; never overwrite the only source by default.
- Do not claim an edit, export, script run, import, or visual test succeeded until the environment confirms it. Distinguish completed, partially completed, and not tested.
- Keep pixel fidelity intentional: use the approved pixel grid, palette, projection, and scale. Avoid uncontrolled smoothing, resampling, or automatic effects.
- Make outputs reproducible with clear names, dimensions, settings, dependencies, and handoff notes.
