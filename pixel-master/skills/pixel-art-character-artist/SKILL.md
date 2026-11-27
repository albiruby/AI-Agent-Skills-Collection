---
name: pixel-art-character-artist
description: "Specialist in pixel art character design and sprite creation. Use when designing player characters, NPCs, base body templates, character proportions, facial features, outfits, hairstyles, poses, turnarounds, or modular character variations."
---
# Pixel Art Character Artist

Design iconic, readable, animation-ready pixel art characters with clear silhouettes, consistent anatomy/proportions, expressive features, and modular variation support.

## Non-negotiable studio standards

Apply the pack's `../../shared/PIXEL_ART_STANDARDS.md` when installed, plus these defaults:

- 1 logical art pixel = an integer number of screen pixels; nearest-neighbor scaling only, no mixels.
- Lock native resolution, projection, palette, light direction, and outline policy before bulk production.
- Build readable pixel clusters; remove orphan pixels, unintended banding, jaggies, and pillow shading.
- Sprites use binary alpha unless the asset is an intentional VFX/shader effect.
- Export production assets as lossless PNG (plus native editable source); never JPEG.
- Review at 1x gameplay size and 4x zoom; test engine filtering, compression, scaling, and seams before claiming integration.

## When to Use

- Designing player characters, companions, NPCs, or modular character paper-doll systems.
- Establishing canonical sprite proportions (16x16, 16x24, 24x32, 32x32, 32x48, 48x64).
- Creating character turnarounds (front, side, back, 3/4), neutral base bodies, outfits, hairstyles, and equipment overlays.
- Ensuring character readability across gameplay backgrounds.

## Design Standards

1. **Proportion Calibration**:
   - **16x16 / 16x24 (Tiny/Retro)**: 1:1 to 1.5-head chibi ratio; emphasize hair silhouette, primary tunic color, and bold weapon/prop read.
   - **24x32 / 32x32 (Classic 16-bit)**: 2 to 2.5-head ratio; clear head, torso, limbs, distinct footwear, and 1x2 or 2x2 eye placement.
   - **48x64+ (Detailed/Action)**: 3 to 5-head heroic ratio; readable anatomy, cloth folds, layered armor, and facial expressions.
2. **Silhouette Hierarchy**: At least 2 unmistakable silhouette hooks per character (e.g., cape, hat, hairstyle, shoulder pauldron, weapon posture) so characters never blur together in motion.
3. **Color Distribution (60-30-10 Rule)**: 60% dominant base outfit/body, 30% secondary trim/hair/armor, 10% high-contrast focal accent (scarf, gem, visor, emblem).
4. **Animation-Ready Construction**: Keep limbs, torso, head, and accessories cleanly separated in structure (and on distinct layers when using an editor) so `pixel-art-sprite-animator` can animate smoothly without redrawing the entire silhouette.
5. **Fixed Foot Baseline & Pivot**: Place the bottom of the character's feet consistently at a locked Y-baseline (typically 1-2 px above the bottom of the canvas cell) and horizontally centered on the pivot column.

## Workflow Steps

1. **Confirm Spec**: Lock canvas cell size, perspective (top-down 3/4, side-view, isometric), head-to-body ratio, and master palette.
2. **Block Base Silhouette**: Draw the neutral idle pose in 1 flat color; verify readable separation between head, torso, arms, and legs.
3. **Establish Anatomy & Landmark Pixels**: Place eye line, shoulder width, waist, and foot stance. Avoid symmetrical stiff "T-poses" unless explicitly building a modular paper-doll template; prefer a grounded 3/4 hero stance.
4. **Layer Outfit, Hair & Focal Props**: Group clothing into clean pixel clusters; avoid 1-pixel noisy belts or buckles that disappear in motion.
5. **Shade & Outline**: Apply Style Bible lighting and selective outlining; keep head/face slightly higher contrast than boots to guide the viewer's eye.
6. **Build Turnaround & Variations**: Produce required directional views (Front/Down, Side/Right, Back/Up; mirror Left only if design is symmetrical or redraw asymmetrical gear explicitly) and modular swaps (hair, armor, palette swaps).

## Gotchas

- Never place eyes too high on the head; in pixel art, lowering the eye line slightly creates a more appealing, expressive read.
- Never mirror asymmetrical characters (sword in right hand, eyepatch on left eye) blindly in-engine without checking if handedness continuity matters.

## Extended scope

- Character ideation, role-based shape language, silhouette thumbnails, proportion systems, and visual hierarchy.
- Pixel-scale anatomy and gesture: head/body ratios, limbs, hands, feet, facial features, and readable poses.
- Clothing, armor, accessories, hairstyles, equipment, material separation, and costume variants.
- Front/side/back views, turnaround sheets, expression sheets, portrait sprites, and directional sprite sets.
- Player/NPC/enemy distinction through silhouette, palette, scale, and animation vocabulary.
- Consistent character construction across multiple sizes and alternate outfits.
- Design for animation: clear joints, readable limb separation, pivot awareness, and pose continuity.

## Deliverables

- Character concept sheet and approved sprite
- Directional/variation sprite set as scoped
- Palette and proportion notes
- Layer/pivot/animation handoff specification

## Quality gates

- Character reads at actual gameplay size.
- Pose and silhouette communicate role and action.
- Pixel density, palette, lighting, and outlines match the project.
- Accessories do not merge confusingly into anatomy.

## Collaboration and handoff

Coordinate with: `pixel-art-art-director`, `pixel-art-fundamentals-specialist`, `pixel-art-palette-color-specialist`, `pixel-art-sprite-animator`, `pixel-art-animation-director`, `pixel-art-spritesheet-atlas-architect`.

When handing work off, state the exact source files, dimensions, palette/projection assumptions, pivot/origin, frame/tile metadata, tools and versions used, and anything that remains unverified. Do not assume another specialist has access to your local tool session; package the required files or write a precise handoff.

### Execution contract

- Read the project brief and the approved art/style specification before making asset-level decisions. If the specification is missing, establish the minimum relevant constraints and label assumptions.
- Work only with tools, files, applications, APIs, and permissions actually available in the active harness. A skill describes a workflow; it does not grant software access.
- Verify the installed application/engine version and consult version-matched official documentation before using version-sensitive commands, properties, or scripting APIs.
- Preserve source editability. Use a working copy or backup before destructive changes; never overwrite the only source by default.
- Do not claim an edit, export, script run, import, or visual test succeeded until the environment confirms it. Distinguish completed, partially completed, and not tested.
- Keep pixel fidelity intentional: use the approved pixel grid, palette, projection, and scale. Avoid uncontrolled smoothing, resampling, or automatic effects.
- Make outputs reproducible with clear names, dimensions, settings, dependencies, and handoff notes.
