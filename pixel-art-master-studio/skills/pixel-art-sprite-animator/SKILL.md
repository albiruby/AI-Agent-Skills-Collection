---
name: pixel-art-sprite-animator
description: "Specialist in frame-by-frame pixel art sprite animation. Use when animating idle, walk, run, jump, fall, climb, attack, hit, death, interaction, facial expressions, 4-direction/8-direction cycles, or sprite-sheet animations."
---
# Pixel Art Sprite Animator

Execute clean, fluid, volume-consistent frame-by-frame pixel art animations across character cycles, combat moves, facial animations, and multi-directional sprite sheets.

## Non-negotiable studio standards

Apply the pack's `../../shared/PIXEL_ART_STANDARDS.md` when installed, plus these defaults:

- 1 logical art pixel = an integer number of screen pixels; nearest-neighbor scaling only, no mixels.
- Lock native resolution, projection, palette, light direction, and outline policy before bulk production.
- Build readable pixel clusters; remove orphan pixels, unintended banding, jaggies, and pillow shading.
- Sprites use binary alpha unless the asset is an intentional VFX/shader effect.
- Export production assets as lossless PNG (plus native editable source); never JPEG.
- Review at 1x gameplay size and 4x zoom; test engine filtering, compression, scaling, and seams before claiming integration.

## When to Use

- Animating character and creature states: `idle`, `walk`, `run`, `jump`, `fall`, `land`, `climb`, `attack`, `cast`, `hurt`, `death`, `interact`.
- Building 4-direction (Down, Up, Left, Right) or 8-direction movement cycles.
- Creating facial animation strips (blink, talk, hurt, happy, angry) for portraits or sprites.
- Polishing rough silhouette animations into shaded, flicker-free pixel art frames.

## Technical & Craft Standards

1. **Layered Cel / Cluster Workflow**: Animate in passes rather than pixel-polishing frame 1 before frame 2 exists:
   - Pass 1: Color-coded silhouette / limb blocking (verify arcs, weight, and timing).
   - Pass 2: Main body, head, and outfit cluster tracking (preserve pixel volume/mass).
   - Pass 3: Secondary motion (hair, cape, cloth, tail) offset by 1-2 frames.
   - Pass 4: Shading, selective outlines, and flicker cleanup.
2. **Zero Pixel Flicker (Boiling)**: Keep shading clusters and texture pixels anchored to the moving surface rather than randomly shifting every frame. Flickering 1-pixel highlights look like static noise in motion.
3. **Standard Cycle Blueprints**:
   - **Idle (2-6 frames)**: Subtle 1 px torso/head breath drop or subpixel highlight shift + optional blink/cape sway.
   - **Walk (4-8 frames)**: Contact -> Down -> Passing -> Up (for each stride); head drops on Down and rises on Up.
   - **Run (6-8 frames)**: Forward torso lean, airborne stride frame, wide arm/leg silhouette separation.
   - **Attack (4-7 frames)**: Anticipation -> Active Swing (with 1-frame smear cluster) -> Follow-through -> Recovery.
   - **Hurt / Death**: Crisp white/bright hit-flash frame (1 frame) -> recoil knockback -> collapse/dissolve with clear final resting silhouette.
4. **4-Direction & 8-Direction Discipline**: Keep head height, stride rhythm, and silhouette width consistent across all directions. Explicitly redraw asymmetrical weapons/shields for Left vs. Right if the Style Bible forbids mirroring.
5. **Pivot & Cell Alignment**: Keep every frame locked to the exact same cell size and foot baseline; expand the uniform cell size across the whole sheet (or use explicit trim offsets in metadata) if an attack extends beyond idle bounds.

## Workflow Steps

1. **Ingest Direction Spec**: Confirm canvas cell size, anchor pivot, palette, and timing table from `pixel-art-animation-director` (or define them if running standalone).
2. **Block Keyframes with Onion Skinning**: Place extreme poses first, verifying silhouette contrast and grounded foot contact.
3. **Add Breakdowns & In-Betweens**: Insert passing poses, anticipation, smear frames, and secondary follow-through.
4. **Playback Timing Test**: Export an integer-scaled (3x or 4x) looping GIF/APNG preview at exact millisecond frame delays and inspect motion rhythm.
5. **Shading & Anti-Flicker Pass**: Shade clusters consistently with the global light direction; step frame-by-frame to eliminate stray pixels or dancing shadows.
6. **Export Strips & Timing Metadata**: Output lossless PNG animation strip(s), GIF preview, and frame duration table for `pixel-art-spritesheet-atlas-architect`.

## Gotchas

- Never animate limbs by rotating pixel sprites with standard bilinear/nearest rotation tools without manual pixel cleanup - raw rotation creates jagged "crumbled" pixels and volume loss.
- Always check the transition from the last frame back to frame 0 on loops to verify zero jump or pause.

## Extended scope

- Idle, walk, run, jump, fall, land, climb, swim, attack, cast, hit, hurt, death, interact, emote, and transition clips.
- Frame-by-frame construction, key poses, breakdowns, in-betweens, onion-skin use, and timing control.
- Looping animation cycles, foot-contact timing, body bob, anticipation, recoil, and follow-through.
- 4-direction and 8-direction sprite sets; ensure facing and equipment consistency.
- Pivot/origin management, frame bounds, consistent canvas, cel/layer organization, and tag naming.
- Animation variants, speed variants, mirrored clips (only when visually valid), and equipment overlays.
- Frame contact sheets, GIF previews, spritesheet strips, and engine-ready export.

## Deliverables

- Editable animation source with named tags/layers
- Frame sequence or sprite sheet
- Preview GIF/contact sheet
- Pivot, timing, and playback metadata

## Quality gates

- All frames share consistent canvas and origin unless intentionally designed otherwise.
- No accidental one-frame artifacts or unintended limb/prop jumps.
- Loop start/end alignment is clean.
- Playback timing and direction order are documented.

## Collaboration and handoff

Coordinate with: `pixel-art-animation-director`, `pixel-art-character-artist`, `pixel-art-creature-artist`, `pixel-art-vfx-artist`, `pixel-art-spritesheet-atlas-architect`, `pixel-art-game-engine-integration`.

When handing work off, state the exact source files, dimensions, palette/projection assumptions, pivot/origin, frame/tile metadata, tools and versions used, and anything that remains unverified. Do not assume another specialist has access to your local tool session; package the required files or write a precise handoff.

### Execution contract

- Read the project brief and the approved art/style specification before making asset-level decisions. If the specification is missing, establish the minimum relevant constraints and label assumptions.
- Work only with tools, files, applications, APIs, and permissions actually available in the active harness. A skill describes a workflow; it does not grant software access.
- Verify the installed application/engine version and consult version-matched official documentation before using version-sensitive commands, properties, or scripting APIs.
- Preserve source editability. Use a working copy or backup before destructive changes; never overwrite the only source by default.
- Do not claim an edit, export, script run, import, or visual test succeeded until the environment confirms it. Distinguish completed, partially completed, and not tested.
- Keep pixel fidelity intentional: use the approved pixel grid, palette, projection, and scale. Avoid uncontrolled smoothing, resampling, or automatic effects.
- Make outputs reproducible with clear names, dimensions, settings, dependencies, and handoff notes.
