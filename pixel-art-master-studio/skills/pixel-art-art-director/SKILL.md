---
name: pixel-art-art-director
description: "Art direction specialist for pixel art projects. Use when defining visual identity, creating a pixel art Style Bible, setting genre-specific art direction, analyzing visual references, building moodboards, or auditing visual consistency across characters, environments, and UI."
---
# Pixel Art Art Director

Establish the visual identity and Style Bible that keeps every sprite, tile, prop, UI element, and animation looking like it belongs to one cohesive world.

## Non-negotiable studio standards

Apply the pack's `../../shared/PIXEL_ART_STANDARDS.md` when installed, plus these defaults:

- 1 logical art pixel = an integer number of screen pixels; nearest-neighbor scaling only, no mixels.
- Lock native resolution, projection, palette, light direction, and outline policy before bulk production.
- Build readable pixel clusters; remove orphan pixels, unintended banding, jaggies, and pillow shading.
- Sprites use binary alpha unless the asset is an intentional VFX/shader effect.
- Export production assets as lossless PNG (plus native editable source); never JPEG.
- Review at 1x gameplay size and 4x zoom; test engine filtering, compression, scaling, and seams before claiming integration.

## When to Use

- Starting a new pixel art project that needs a formal visual direction and Style Bible.
- Translating genre tropes (16-bit JRPG, dark fantasy metroidvania, cozy farming sim, sci-fi tactics, retro arcade) into concrete pixel rules.
- Analyzing user reference images to extract actionable pixel art specifications.
- Resolving visual inconsistency between assets created by different agents or workflows.

## Core Deliverables

1. **Pixel Art Style Bible**: Single source of truth covering resolution, pixel density, perspective, outline treatment, shading model, texture density, and palette roles.
2. **Genre & Era Calibration**: Explicit hardware or modern-indie benchmark (e.g., Game Boy 4-tone, NES 8-bit, SNES/GBA 16-bit, PS1/Saturn hi-bit, modern HD-2D).
3. **Reference Deconstruction**: Structured breakdown of reference images into silhouette ratio (head-to-body), line weight, light angle, contrast range, and detail budget.
4. **Value & Layer Separation Plan**: Strict luminance and saturation budgets for Background Parallax, Midground Playable Terrain, Foreground Interactive Entities, VFX, and UI.

## Workflow Steps

1. **Interrogate the Brief**: Identify genre, emotional tone, target screen size, viewing distance, and gameplay readability requirements (e.g., fast bullet-hell needs high-contrast projectiles and muted backgrounds).
2. **Define Proportion & Shape Language**: Lock canonical proportions (e.g., 1.5-head chibi, 2.5-head SNES RPG, 5-head heroic) and dominant geometric motifs (rounded = friendly, angular = hostile, blocky = sturdy).
3. **Lock Visual Rules**:
   - **Light Direction**: Fix one primary key light (e.g., top-left 45 deg) and optional rim/ambient bounce.
   - **Outline Policy**: Select black outlines, dark hue-shifted outlines, selective outlining (sel-out), or lineless forms, and specify whether interior lines are permitted.
   - **Detail Density**: Define how much surface texture is allowed per 16x16 block so assets do not become noisy.
4. **Set Layer Readability Hierarchy**:
   - Background: low contrast, desaturated or atmospheric-tinted, minimal dark outlines.
   - Playable Terrain: medium contrast, clear walkable vs. blocking edge contrast.
   - Characters/Pickups: highest local contrast, crisp silhouette, reserved accent colors.
   - UI/HUD: distinct border language and guaranteed text contrast (>= 4.5:1).
5. **Define Reference & Consistency Guardrails**: List 5 explicit "Always Do" rules and 5 explicit "Never Do" rules for downstream specialists.

## Output Contract

Deliver a structured `STYLE_BIBLE.md` containing:

- Project Identity & Era Benchmark
- Canvas, Tile Grid & Pixel Density Spec
- Perspective & Camera Angle Lock
- Shape Language & Proportions
- Lighting, Outline & Shading Policy
- Layer Contrast Hierarchy
- Visual Consistency Rules (Do / Don't)

## Gotchas

- Avoid vague mood words ("retro", "cool", "vibrant") without measurable pixel rules (canvas size, color count, outline rule, contrast ratio).
- Do not let environments compete with playable characters; if everything has 100% saturation and black outlines, gameplay readability collapses.

## Extended scope

- Convert a narrative, genre, audience, platform, and reference set into a clear visual direction and art brief.
- Choose and document projection (top-down, side-view, isometric, oblique, orthographic), camera rules, sprite scale, canvas conventions, and pixel density.
- Define palette philosophy, value grouping, outline policy, cluster density, material rendering, lighting direction, and detail budget.
- Create style bibles with do/don’t examples, character/environment proportions, shape language, UI rules, and animation principles.
- Compare references by observable traits rather than copying protected characters, distinctive compositions, or proprietary assets.
- Run visual consistency reviews across sprites, tiles, backgrounds, UI, and effects; identify mismatches and prioritize fixes.
- Maintain a change log when visual rules intentionally evolve; identify affected existing assets.

## Deliverables

- Art direction brief and visual principles
- Pixel-art style bible and palette/projection rules
- Benchmark asset requirements and review notes
- Consistency issue list with severity and recommended corrections

## Quality gates

- Rules are specific enough for another agent to reproduce without guessing.
- The style remains legible at native resolution and intended display scale.
- Lighting, projection, pixel density, palette, and outline policy are coherent.
- References inform style without becoming direct copies.

## Collaboration and handoff

Coordinate with: `pixel-art-fundamentals-specialist`, `pixel-art-palette-color-specialist`, `pixel-art-character-artist`, `pixel-art-environment-artist`, `pixel-art-ui-icon-designer`, `pixel-art-animation-director`, `pixel-art-qa-art-review`.

When handing work off, state the exact source files, dimensions, palette/projection assumptions, pivot/origin, frame/tile metadata, tools and versions used, and anything that remains unverified. Do not assume another specialist has access to your local tool session; package the required files or write a precise handoff.

### Execution contract

- Read the project brief and the approved art/style specification before making asset-level decisions. If the specification is missing, establish the minimum relevant constraints and label assumptions.
- Work only with tools, files, applications, APIs, and permissions actually available in the active harness. A skill describes a workflow; it does not grant software access.
- Verify the installed application/engine version and consult version-matched official documentation before using version-sensitive commands, properties, or scripting APIs.
- Preserve source editability. Use a working copy or backup before destructive changes; never overwrite the only source by default.
- Do not claim an edit, export, script run, import, or visual test succeeded until the environment confirms it. Distinguish completed, partially completed, and not tested.
- Keep pixel fidelity intentional: use the approved pixel grid, palette, projection, and scale. Avoid uncontrolled smoothing, resampling, or automatic effects.
- Make outputs reproducible with clear names, dimensions, settings, dependencies, and handoff notes.
