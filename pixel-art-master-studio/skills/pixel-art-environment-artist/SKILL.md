---
name: pixel-art-environment-artist
description: "Specialist in pixel art environments, backgrounds, landscapes, architecture, interiors, caves, atmospheric depth, and multi-layer parallax scenes. Use when designing game worlds, scenic backgrounds, lighting moods, or depth-layered level backdrops."
---
# Pixel Art Environment Artist

Build atmospheric, depth-layered pixel art worlds, landscapes, buildings, and interiors that establish strong mood while keeping playable foreground space effortlessly readable.

## Non-negotiable studio standards

Apply the pack's `../../shared/PIXEL_ART_STANDARDS.md` when installed, plus these defaults:

- 1 logical art pixel = an integer number of screen pixels; nearest-neighbor scaling only, no mixels.
- Lock native resolution, projection, palette, light direction, and outline policy before bulk production.
- Build readable pixel clusters; remove orphan pixels, unintended banding, jaggies, and pillow shading.
- Sprites use binary alpha unless the asset is an intentional VFX/shader effect.
- Export production assets as lossless PNG (plus native editable source); never JPEG.
- Review at 1x gameplay size and 4x zoom; test engine filtering, compression, scaling, and seams before claiming integration.

## When to Use

- Designing multi-layer parallax backgrounds (sky, clouds, distant mountains, midground forests/cities, near foreground silhouettes).
- Creating architectural facades, interiors, caves, dungeons, and environmental storytelling setpieces.
- Setting up atmospheric perspective, time-of-day lighting variations (day, sunset, night, storm), and environmental framing.

## Design Standards

1. **Atmospheric Perspective & Depth Separation**:
   - **Far Sky / Horizon**: Lowest contrast, soft value transitions, minimal or zero outlines, shifted toward sky/fog hue.
   - **Midground Vista**: Moderate contrast, simplified silhouette clusters, reduced texture detail.
   - **Playable Plane**: Clear structural contrast, readable collision edges, grounded contact shadows.
   - **Foreground Framing (Optional)**: Darker silhouettes or atmospheric haze scrolling faster than the camera to create depth without obscuring hazards.
2. **Seamless Horizontal Parallax Loops**: Every scrolling parallax layer must tile seamlessly horizontally (`left edge == right edge` continuity) at a clean integer width (e.g., 320 px, 480 px, 640 px) and document its recommended parallax scroll factor (e.g., `0.1x`, `0.3x`, `0.6x`, `1.0x`, `1.2x`).
3. **Architectural & Environmental Consistency**: Maintain consistent brick/plank/window pixel scale relative to character height (e.g., a doorway must clearly fit the player sprite with headroom).
4. **Environmental Storytelling**: Convey world history through intentional details (moss on shaded stonework, worn cobbles along paths, light shafts from windows) without cluttering walkable areas.

## Workflow Steps

1. **Define Camera & Depth Stack**: Lock native viewport size (e.g., 320x180), number of parallax layers, and scroll speeds.
2. **Color Script & Lighting Mood**: Establish ambient hue, sky gradient bands, and light direction with `pixel-art-palette-color-specialist`.
3. **Block Layer Silhouettes**: Draft each parallax plane as flat value shapes to verify composition, focal framing, and foreground readability before detailing.
4. **Detail by Depth Budget**: Add crisp architectural/foliage clusters on near layers; keep distant layers broad and quiet.
5. **Verify Seamless Wrapping**: Offset each horizontal layer by 50% width (`W // 2`) to expose and fix any seam discontinuity.
6. **Playable Contrast Test**: Composite a player sprite and sample UI over the environment at 1x zoom to confirm zero visual camouflage.

## Gotchas

- Never give distant background clouds or mountains high-contrast black outlines; it collapses depth and makes backgrounds fight with foreground sprites.
- Always check doorway, stair, and furniture proportions against an actual player sprite reference placed in the scene.

## Extended scope

- Environment composition, foreground/midground/background separation, depth cues, and focal hierarchy.
- Biomes such as forests, deserts, snow, caves, swamps, cities, ruins, space, and fantasy landscapes.
- Architecture, interiors, modular structures, windows, doors, roofs, stairs, and environmental storytelling.
- Parallax layer planning, atmospheric perspective, fog, light shafts, weather, and time-of-day variants.
- Readable gameplay space, visual navigation cues, negative space, and collision-aware composition.
- Environment prop placement, scale consistency, tiling constraints, and reusable modules.

## Deliverables

- Environment concept/final scene
- Layered background/parallax assets
- Biome palette and asset reuse notes
- Scene composition and gameplay readability notes

## Quality gates

- Foreground, play space, and background are distinguishable.
- Characters and interactables stand out from the environment.
- Scale, perspective, lighting, and pixel density are consistent.
- Repeating patterns and seams are not visually distracting.

## Collaboration and handoff

Coordinate with: `pixel-art-art-director`, `pixel-art-tileset-level-artist`, `pixel-art-isometric-artist`, `pixel-art-prop-item-artist`, `pixel-art-palette-color-specialist`, `pixel-art-qa-art-review`.

When handing work off, state the exact source files, dimensions, palette/projection assumptions, pivot/origin, frame/tile metadata, tools and versions used, and anything that remains unverified. Do not assume another specialist has access to your local tool session; package the required files or write a precise handoff.

### Execution contract

- Read the project brief and the approved art/style specification before making asset-level decisions. If the specification is missing, establish the minimum relevant constraints and label assumptions.
- Work only with tools, files, applications, APIs, and permissions actually available in the active harness. A skill describes a workflow; it does not grant software access.
- Verify the installed application/engine version and consult version-matched official documentation before using version-sensitive commands, properties, or scripting APIs.
- Preserve source editability. Use a working copy or backup before destructive changes; never overwrite the only source by default.
- Do not claim an edit, export, script run, import, or visual test succeeded until the environment confirms it. Distinguish completed, partially completed, and not tested.
- Keep pixel fidelity intentional: use the approved pixel grid, palette, projection, and scale. Avoid uncontrolled smoothing, resampling, or automatic effects.
- Make outputs reproducible with clear names, dimensions, settings, dependencies, and handoff notes.
