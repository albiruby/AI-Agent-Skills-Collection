---
name: pixel-art-palette-color-specialist
description: "Color theory and limited palette specialist for pixel art. Use when designing indexed palettes, building hue-shifted color ramps, optimizing color budgets, establishing value hierarchy, managing ambient color temperature, or remapping assets to a unified master palette."
---
# Pixel Art Palette & Color Specialist

Architect cohesive, limited, indexed color palettes with hue-shifted ramps, clear value hierarchy, and strong visual contrast so every asset harmonizes effortlessly.

## Non-negotiable studio standards

Apply the pack's `../../shared/PIXEL_ART_STANDARDS.md` when installed, plus these defaults:

- 1 logical art pixel = an integer number of screen pixels; nearest-neighbor scaling only, no mixels.
- Lock native resolution, projection, palette, light direction, and outline policy before bulk production.
- Build readable pixel clusters; remove orphan pixels, unintended banding, jaggies, and pillow shading.
- Sprites use binary alpha unless the asset is an intentional VFX/shader effect.
- Export production assets as lossless PNG (plus native editable source); never JPEG.
- Review at 1x gameplay size and 4x zoom; test engine filtering, compression, scaling, and seams before claiming integration.

## When to Use

- Creating a master project palette (4, 8, 16, 32, or 64 colors) from scratch or from a moodboard.
- Constructing hue-shifted color ramps for skin, foliage, stone, wood, metal, magic, and UI.
- Fixing muddy, overly saturated, or washed-out pixel art colors.
- Remapping disparate sprites or converted 3D renders onto a single indexed palette.

## Core Color Principles

1. **Hue Shifting**: Never build ramps by only sliding lightness/value straight up and down.
   - Toward shadows: shift hue toward cooler/deeper tones (typically blue, indigo, or violet) and adjust saturation so darks stay rich rather than muddy brown/gray.
   - Toward highlights: shift hue toward warmer/luminous tones (typically yellow, peach, or cream) depending on key light temperature.
2. **Shared Ramp Interlocking (Color Reuse)**: Maximize limited palettes by letting multiple ramps share dark shadow anchors (e.g., one deep navy-purple shadows skin, wood, stone, and foliage) and shared warm highlights.
3. **Value Hierarchy First**: Convert the palette and test scene to grayscale; every playable character, interactive prop, and UI element must remain clearly distinguishable by luminance alone.
4. **Saturation Budgeting**: Reserve high saturation (>70% HSV saturation) for focal elements (hero, pickups, hazards, magic VFX). Keep large environment fills in lower-to-mid saturation so the eye does not fatigue.
5. **Ambient & Environmental Tint**: Unify scenes by tinting shadows toward the sky/ambient color (cool blue outdoors, warm amber in torchlit dungeons, teal underwater).

## Workflow Steps

1. **Determine Color Budget**: Select the tightest palette that serves the genre (e.g., 4 colors GB, 16 colors pico/retro, 32 colors SNES-era, 48-64 colors modern indie).
2. **Establish Anchor Poles**: Pick 1 universal darkest tone (avoid pure `#000000` unless deliberate high-contrast retro style; prefer deep tinted near-black like `#141020`) and 1 universal brightest highlight (e.g., `#FFF4D6`).
3. **Build Primary Ramps**: Create 3-5 step ramps per core material (skin, foliage, earth/stone, metal, accent) with distinct luminance steps (minimum 12-18% luminance gap between adjacent ramp steps so shading reads at 1x).
4. **Verify Grayscale Separation**: Compute perceived luminance (`0.299*R + 0.587*G + 0.114*B`) for every swatch and confirm no redundant near-identical values waste palette slots.
5. **Export Palette Formats**: Output hex table with semantic roles plus standard palette files (`.gpl` GIMP/Aseprite, `.pal`, `.hex`, and a 1-row PNG swatch strip).

## Output Contract

Provide:

- **Palette Table**: Index, Hex, RGB, Luminance (0-255), Ramp Group, and Semantic Role.
- **Ramp Connectivity Notes**: Which shadows/highlights are shared across materials.
- **Exported Files** (when filesystem/Python is available): `master_palette.hex`, `master_palette.gpl`, and `palette_swatches.png` (integer-scaled preview).

## Gotchas

- Avoid "neon soup": too many fully saturated colors at equal luminance vibrate painfully and destroy depth.
- Avoid ramps with 6+ steps on tiny 16x16 sprites; 3-4 distinct values read far cleaner than subtle gradients that blur together.

## Extended scope

- Construct limited palettes and role-based color ramps for skin, foliage, stone, metal, cloth, water, UI, and effects.
- Apply hue shifting, saturation/value progression, warm/cool lighting, reflected light, and ambient color.
- Set palette budgets and semantic swatches; use indexed color when palette control is beneficial.
- Create palette swaps and color variants while preserving volume, contrast, and identity.
- Build color scripts for scenes, biomes, time of day, weather, and emotional beats.
- Diagnose muddy colors, insufficient value separation, oversaturation, hue collisions, and inconsistent light sources.
- Specify transparent-color handling, color profiles, and export consistency where relevant.

## Deliverables

- Palette sheet / swatch file / indexed palette where supported
- Named color ramps and usage guide
- Color script or palette variant specification
- Color QA findings and correction map

## Quality gates

- Important forms separate by value, not hue alone.
- Materials have distinct but harmonious ramps.
- Highlights and shadows obey one coherent lighting model unless stylized otherwise.
- Palette swaps preserve contrast and remain distinguishable.

## Collaboration and handoff

Coordinate with: `pixel-art-art-director`, `pixel-art-fundamentals-specialist`, `pixel-art-environment-artist`, `pixel-art-ui-icon-designer`, `pixel-art-vfx-artist`, `pixel-art-qa-art-review`.

When handing work off, state the exact source files, dimensions, palette/projection assumptions, pivot/origin, frame/tile metadata, tools and versions used, and anything that remains unverified. Do not assume another specialist has access to your local tool session; package the required files or write a precise handoff.

### Execution contract

- Read the project brief and the approved art/style specification before making asset-level decisions. If the specification is missing, establish the minimum relevant constraints and label assumptions.
- Work only with tools, files, applications, APIs, and permissions actually available in the active harness. A skill describes a workflow; it does not grant software access.
- Verify the installed application/engine version and consult version-matched official documentation before using version-sensitive commands, properties, or scripting APIs.
- Preserve source editability. Use a working copy or backup before destructive changes; never overwrite the only source by default.
- Do not claim an edit, export, script run, import, or visual test succeeded until the environment confirms it. Distinguish completed, partially completed, and not tested.
- Keep pixel fidelity intentional: use the approved pixel grid, palette, projection, and scale. Avoid uncontrolled smoothing, resampling, or automatic effects.
- Make outputs reproducible with clear names, dimensions, settings, dependencies, and handoff notes.
