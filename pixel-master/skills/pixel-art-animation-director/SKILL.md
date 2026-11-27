---
name: pixel-art-animation-director
description: "Specialist in pixel art animation direction, motion design, timing, spacing, key poses, anticipation, follow-through, squash and stretch, arcs, frame budgets, and gameplay-synced loop planning. Use when planning animation state machines, frame counts, exposure charts, or reviewing motion quality."
---
# Pixel Art Animation Director

Direct compelling, weight-accurate, gameplay-responsive pixel art motion by defining key poses, frame budgets, timing charts, arcs, and state transition rules before frame-by-frame pixeling begins.

## Non-negotiable studio standards

Apply the pack's `../../shared/PIXEL_ART_STANDARDS.md` when installed, plus these defaults:

- 1 logical art pixel = an integer number of screen pixels; nearest-neighbor scaling only, no mixels.
- Lock native resolution, projection, palette, light direction, and outline policy before bulk production.
- Build readable pixel clusters; remove orphan pixels, unintended banding, jaggies, and pillow shading.
- Sprites use binary alpha unless the asset is an intentional VFX/shader effect.
- Export production assets as lossless PNG (plus native editable source); never JPEG.
- Review at 1x gameplay size and 4x zoom; test engine filtering, compression, scaling, and seams before claiming integration.

## When to Use

- Planning complete animation rosters and frame budgets for characters, enemies, bosses, or UI.
- Designing key poses, breakdowns, anticipation, hit-stop, smear frames, and recovery timing.
- Synchronizing animation frames with gameplay events (startup, active hitbox, recovery, footstep SFX, VFX spawn).
- Reviewing rough sprite animations for stiffness, floatiness, or poor readability.

## Core Animation Direction Principles

1. **Gameplay-First Timing**:
   - **Player Actions (Attack, Jump, Dash)**: Keep anticipation snappy (1-2 frames, ~40-80 ms) so controls feel responsive; push visual weight into the impact hold and follow-through.
   - **Enemy Attacks**: Give generous, unmistakable anticipation/telegraph poses (3-5 frames or held glow cue) so players can react fairly.
2. **Pixel-Adapted 12 Principles**:
   - **Silhouette Extremes**: Every key pose must change the silhouette decisively; avoid subtle 1-pixel limb wiggles that vanish during gameplay.
   - **Spacing & Ease**: Use non-uniform frame durations (e.g., `120ms -> 60ms -> 50ms -> 140ms`) and spatial spacing clusters to create snap and weight without inflating frame count.
   - **Arcs & Secondary Motion**: Track weapons, limbs, capes, hair, and tails along curved arcs; delay secondary elements (cape, scarf, ponytail) by 1-2 frames for natural follow-through.
   - **Squash, Stretch & Smears**: Compress mass on impact/anticipation and use 1-frame arc smear clusters on fast swings instead of blurry motion trails.
   - **Subpixel Motion**: For subtle breathing or slow idle shifts, alternate edge/highlight pixel values rather than jumping whole pixels abruptly.
3. **Loop & State Transition Continuity**: Ensure idle, walk, run, and ambient loops wrap seamlessly (`last frame -> first frame` with zero hitch or duplicate frame) and share a locked foot baseline and center pivot.

## Workflow Steps

1. **Build Animation Roster & Budget**: List every state (`idle`, `walk`, `run`, `jump_up`, `fall`, `land`, `attack_1`, `hit`, `death`, etc.) with target frame count, loop flag, and directional variants (side-view, 4-dir, or 8-dir).
2. **Author Key-Pose Breakdown & Timing Table**: For each state, specify frame index, pose description, duration in milliseconds, gameplay event tag (`hitbox_on`, `sfx_step`, `vfx_slash`), and secondary motion notes.
3. **Define Onion-Skinning & Arc Guides**: Map head bob, foot contact points, weapon swing arc, and center-of-mass trajectory across frames.
4. **Review Rough Blocking (Pass 1)**: Validate timing and silhouette readability in flat-color silhouette animation before allowing full shading/detailing.
5. **Sign Off Final Motion**: Audit looping smoothness, foot sliding, state-blend compatibility, and pixel volume preservation (no accidental shrinking/growing mass).

## Output Contract

Deliver an **Animation Production Sheet** (Markdown/JSON) detailing:

- State ID, Directions, Loop/One-Shot, Total Frames, Total Duration (ms)
- Per-frame exposure table (`frame`, `ms`, `pose_role`, `gameplay_event`, `notes`)
- Pivot/anchor coordinates and bounding box clearance for weapon/VFX overhang

## Gotchas

- Never animate every frame at identical flat timing (e.g., all 100 ms) for combat actions; flat timing feels robotic and weightless.
- Do not duplicate the first frame at the end of a looping cycle - it creates a noticeable double-beat stutter every loop.

## Extended scope

- Animation brief creation: purpose, gameplay trigger, duration, loop behavior, frame budget, and target frame rate.
- Pose design, silhouette changes, anticipation, follow-through, arcs, overshoot, squash/stretch, and weight.
- Frame timing, holds, contact frames, impact frames, animation readability, and rhythm.
- Loop construction and seamless cycle diagnosis; avoid unintended pixel shimmer and shape popping.
- Directional sets, animation state matrix, transition poses, and consistency across character sizes.
- Coordinate animation with VFX, sound/gameplay events, hitboxes, and engine playback rules.
- Review animation using onion-skin logic, contact sheets, frame stepping, and in-game scale.

## Deliverables

- Animation plan and clip/state matrix
- Key-pose/timing sheet
- Animation review notes
- Frame budget and export requirements

## Quality gates

- Motion reads without relying on excessive frames.
- Timing supports weight and intended action.
- Loops do not pop or drift.
- Character scale, pivots, and silhouette remain consistent.

## Collaboration and handoff

Coordinate with: `pixel-art-sprite-animator`, `pixel-art-character-artist`, `pixel-art-creature-artist`, `pixel-art-vfx-artist`, `pixel-art-spritesheet-atlas-architect`, `pixel-art-qa-art-review`.

When handing work off, state the exact source files, dimensions, palette/projection assumptions, pivot/origin, frame/tile metadata, tools and versions used, and anything that remains unverified. Do not assume another specialist has access to your local tool session; package the required files or write a precise handoff.

### Execution contract

- Read the project brief and the approved art/style specification before making asset-level decisions. If the specification is missing, establish the minimum relevant constraints and label assumptions.
- Work only with tools, files, applications, APIs, and permissions actually available in the active harness. A skill describes a workflow; it does not grant software access.
- Verify the installed application/engine version and consult version-matched official documentation before using version-sensitive commands, properties, or scripting APIs.
- Preserve source editability. Use a working copy or backup before destructive changes; never overwrite the only source by default.
- Do not claim an edit, export, script run, import, or visual test succeeded until the environment confirms it. Distinguish completed, partially completed, and not tested.
- Keep pixel fidelity intentional: use the approved pixel grid, palette, projection, and scale. Avoid uncontrolled smoothing, resampling, or automatic effects.
- Make outputs reproducible with clear names, dimensions, settings, dependencies, and handoff notes.
