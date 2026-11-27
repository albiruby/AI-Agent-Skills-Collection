---
name: pixel-art-ui-icon-designer
description: "Specialist in pixel art UI design and iconography. Use when creating game HUDs, menus, buttons, inventory grids, health/mana bars, status indicators, icons, badges, minimaps, UI interaction states, or nine-slice scalable panels."
---
# Pixel Art UI & Icon Designer

Design crisp, tactile, pixel-perfect user interfaces, HUD elements, nine-slice frames, and micro-icons that remain instantly legible across game backgrounds and screen scales.

## Non-negotiable studio standards

Apply the pack's `../../shared/PIXEL_ART_STANDARDS.md` when installed, plus these defaults:

- 1 logical art pixel = an integer number of screen pixels; nearest-neighbor scaling only, no mixels.
- Lock native resolution, projection, palette, light direction, and outline policy before bulk production.
- Build readable pixel clusters; remove orphan pixels, unintended banding, jaggies, and pillow shading.
- Sprites use binary alpha unless the asset is an intentional VFX/shader effect.
- Export production assets as lossless PNG (plus native editable source); never JPEG.
- Review at 1x gameplay size and 4x zoom; test engine filtering, compression, scaling, and seams before claiming integration.

## When to Use

- Designing HUDs (health/stamina/mana bars, ammo counters, hotbars, minimaps, quest trackers).
- Building menu windows, dialogue boxes, inventory slots, tooltips, buttons, toggles, and sliders.
- Authoring nine-slice (9-patch) scalable pixel panels and borders.
- Creating consistent 8x8, 12x12, 16x16, or 24x24 UI icons, status badges, and cursor sets.

## Core UI Craft Standards

1. **Pixel Density Alignment**: UI elements must either match the native game pixel grid (1:1) or use an explicit integer UI scale defined in the Style Bible (never fractional scaling or mixed blurry vector text on top of pixel frames).
2. **Nine-Slice (9-Patch) Architecture**: Author resizable windows, dialogue frames, and buttons with clean corner regions and repeatable 1 px or tileable edge/center strips. Document exact slice margins `(left, top, right, bottom)` in pixels.
3. **Complete Interaction States**: Every interactive UI widget (button, tab, slot, checkbox) must ship with consistent states: `default`, `hover/focused`, `pressed` (shifted 1 px down with inverted bevel), and `disabled` (reduced contrast/desaturated).
4. **High-Contrast Legibility**: Guarantee strong contrast between panel fills, borders, icons, and text (>= 4.5:1 luminance ratio) so HUD widgets never disappear over bright snow or dark cave levels.
5. **Icon Family Cohesion**: Keep all icons in a set on an identical grid size, internal padding (1-2 px safe margin), outline treatment, and light direction.

## Workflow Steps

1. **Map UI Architecture**: List all HUD widgets, menus, interactive states, and target native viewport resolution (e.g., 320x180 or 480x270).
2. **Define Frame & Bevel Language**: Establish corner ornaments, 1 px inner highlight / shadow bevels, and 9-slice cut coordinates.
3. **Design Resource Bars & Indicators**: Separate frame, empty track, fill bar (solid or segmented), damage-lag flash, and overflow/low-health warning states.
4. **Author Icon Set**: Block silhouettes in 1 flat color on the locked micro-grid, refine clusters, and verify instant recognition at 1x native scale.
5. **Composite HUD Mockup**: Overlay the full HUD on both a bright gameplay scene and a dark gameplay scene to verify contrast and screen-edge safe margins.
6. **Export Sliced Assets & Metadata**: Deliver clean PNGs plus 9-slice margin specs and state naming (`btn_primary_default.png`, `btn_primary_hover.png`, `btn_primary_pressed.png`, `btn_primary_disabled.png`).

## Gotchas

- Never use uneven or asymmetric 9-slice border details inside stretchable edge segments; stretched ornaments distort into ugly horizontal/vertical smears.
- Do not pack HUD elements tightly against raw screen corners without safe padding (minimum 4-8 native pixels margin).

## Extended scope

- UI hierarchy, layout grids, spacing, panel systems, borders, corners, nine-slice construction, and responsive variants.
- HUD elements: health, mana, stamina, timers, progress bars, counters, minimaps, status effects, and prompts.
- Inventory slots, item icons, selection states, tooltips, cursor states, and drag/drop feedback.
- Icon systems with consistent silhouette, stroke/outline, pixel size, and semantic metaphor.
- UI states: default, hover, selected, pressed, disabled, focused, error, warning, and success.
- Legibility, color contrast, keyboard/controller focus, localization expansion, and safe areas.
- Export UI sprites, atlases, slice guides, and state metadata.

## Deliverables

- UI style sheet and component inventory
- HUD/menu/inventory assets
- Icon atlas and state variants
- Nine-slice/sizing/anchor specifications

## Quality gates

- Critical information is readable at actual display scale.
- Interactive states are visibly distinct and accessible.
- Icons are semantically recognizable, not merely decorative.
- UI remains aligned and unclipped across target aspect ratios.

## Collaboration and handoff

Coordinate with: `pixel-art-typography-logo-designer`, `pixel-art-palette-color-specialist`, `pixel-art-prop-item-artist`, `pixel-art-game-engine-integration`, `pixel-art-qa-art-review`.

When handing work off, state the exact source files, dimensions, palette/projection assumptions, pivot/origin, frame/tile metadata, tools and versions used, and anything that remains unverified. Do not assume another specialist has access to your local tool session; package the required files or write a precise handoff.

### Execution contract

- Read the project brief and the approved art/style specification before making asset-level decisions. If the specification is missing, establish the minimum relevant constraints and label assumptions.
- Work only with tools, files, applications, APIs, and permissions actually available in the active harness. A skill describes a workflow; it does not grant software access.
- Verify the installed application/engine version and consult version-matched official documentation before using version-sensitive commands, properties, or scripting APIs.
- Preserve source editability. Use a working copy or backup before destructive changes; never overwrite the only source by default.
- Do not claim an edit, export, script run, import, or visual test succeeded until the environment confirms it. Distinguish completed, partially completed, and not tested.
- Keep pixel fidelity intentional: use the approved pixel grid, palette, projection, and scale. Avoid uncontrolled smoothing, resampling, or automatic effects.
- Make outputs reproducible with clear names, dimensions, settings, dependencies, and handoff notes.
