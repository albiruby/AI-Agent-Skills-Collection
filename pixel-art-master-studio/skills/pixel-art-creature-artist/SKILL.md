---
name: pixel-art-creature-artist
description: "Specialist in pixel art monsters, animals, fantasy creatures, enemy variants, and boss sprites. Use when designing organic anatomy, creature silhouettes, mutations, faction enemy tiers, or multi-part pixel art bosses."
---
# Pixel Art Creature Artist

Create memorable pixel art monsters, wildlife, fantasy beasts, enemy families, and towering multi-part bosses with unmistakable silhouettes and clear gameplay telegraphing.

## Non-negotiable studio standards

Apply the pack's `../../shared/PIXEL_ART_STANDARDS.md` when installed, plus these defaults:

- 1 logical art pixel = an integer number of screen pixels; nearest-neighbor scaling only, no mixels.
- Lock native resolution, projection, palette, light direction, and outline policy before bulk production.
- Build readable pixel clusters; remove orphan pixels, unintended banding, jaggies, and pillow shading.
- Sprites use binary alpha unless the asset is an intentional VFX/shader effect.
- Export production assets as lossless PNG (plus native editable source); never JPEG.
- Review at 1x gameplay size and 4x zoom; test engine filtering, compression, scaling, and seams before claiming integration.

## When to Use

- Designing enemies, wildlife, mounts, familiars, mutations, or multi-phase boss sprites.
- Building tiered enemy variants (palette swaps, armor upgrades, elemental mutations) that stay distinct in combat.
- Designing large sprites (64x64 to 256x256+) or modular multi-segment bosses (body, head, wings, claws).

## Design Standards

1. **Instant Threat & Role Readability**:
   - Fast/agile enemies: lean, forward-leaning, diagonal/triangular silhouettes.
   - Heavy/tank enemies: wide, grounded, blocky silhouettes with thick armor clusters.
   - Ranged/caster enemies: elevated focal points (staff, glowing core, floating rings).
   - Bosses: clear weak-point contrast (glowing core, exposed eye, distinct color accent).
2. **Organic Cluster Sculpting**: Avoid rigid geometric outlines on organic creatures; vary cluster curvature to convey muscle, fur, scales, chitin, or slime translucency.
3. **Scale Anchoring**: Calibrate creature pixel canvas relative to the player character's bounding box (e.g., critter = 0.5x player, standard mob = 1x-1.5x, mini-boss = 2x, boss = 3x-6x) while maintaining identical pixel density (zero mixels).
4. **Variant Differentiation**: Go beyond simple hue-shifted palette swaps for higher-tier enemies by adding 1-2 silhouette modifiers (horns, spikes, cracks, glowing runes, tattered cloak).

## Workflow Steps

1. **Define Gameplay Role & Scale**: Lock bounding box, hitbox vs. visual overhang, and threat tier relative to the player sprite.
2. **Silhouette Exploration**: Block 2-3 bold creature silhouettes focusing on posture, limbs/wings/tails, and negative space between appendages.
3. **Organic Mass & Anatomy**: Establish primary skeletal volumes (ribcage, pelvis, skull, limbs) using 2-3 value clusters before surface detailing.
4. **Material & Texture Clusters**: Render scales, fur tufts, bone plates, or wet slime highlights using directional cluster patterns rather than noisy 1-pixel speckles.
5. **Boss Modularity (If Applicable)**: Separate animated appendages (jaw, wings, arms, tail, weak-point core) onto independent layers/sheets with explicit attachment anchor coordinates.
6. **Palette & Contrast Check**: Ensure weak points and attack limbs have high local contrast for combat telegraphing.

## Gotchas

- Never scale up a 32x32 monster 2x to make a "giant boss" - that creates mixels and breaks pixel density. Always author larger creatures natively on a larger canvas at the same pixel scale.
- Avoid cluttered internal noise on large bosses; group scales and fur into broad readable regions with detail concentrated near the face and focal joints.

## Extended scope

- Creature silhouette exploration, taxonomy, anatomy, locomotion, and environmental adaptation.
- Translate reference anatomy into simplified readable forms without over-detailing.
- Design heads, jaws, eyes, horns, wings, tails, limbs, shells, scales, fur, feathers, and exoskeletons.
- Establish visual hierarchy for weak/elite/boss variants and readable attack telegraphs.
- Create creature palettes and material differentiation consistent with the world.
- Plan animation-friendly anatomy, joint placement, appendage separation, and frame readability.
- Design damage states, alternate forms, elemental variants, and size tiers.

## Deliverables

- Creature design and sprite
- Variant/boss progression sheet where needed
- Anatomy, movement, and attack readability notes
- Animation and effects handoff

## Quality gates

- Creature type and action read from silhouette alone where practical.
- Appendages do not collapse into ambiguous clusters.
- Surface detail reinforces anatomy instead of obscuring it.
- Boss/enemy telegraphs remain legible against the environment.

## Collaboration and handoff

Coordinate with: `pixel-art-character-artist`, `pixel-art-fundamentals-specialist`, `pixel-art-palette-color-specialist`, `pixel-art-sprite-animator`, `pixel-art-vfx-artist`, `pixel-art-environment-artist`.

When handing work off, state the exact source files, dimensions, palette/projection assumptions, pivot/origin, frame/tile metadata, tools and versions used, and anything that remains unverified. Do not assume another specialist has access to your local tool session; package the required files or write a precise handoff.

### Execution contract

- Read the project brief and the approved art/style specification before making asset-level decisions. If the specification is missing, establish the minimum relevant constraints and label assumptions.
- Work only with tools, files, applications, APIs, and permissions actually available in the active harness. A skill describes a workflow; it does not grant software access.
- Verify the installed application/engine version and consult version-matched official documentation before using version-sensitive commands, properties, or scripting APIs.
- Preserve source editability. Use a working copy or backup before destructive changes; never overwrite the only source by default.
- Do not claim an edit, export, script run, import, or visual test succeeded until the environment confirms it. Distinguish completed, partially completed, and not tested.
- Keep pixel fidelity intentional: use the approved pixel grid, palette, projection, and scale. Avoid uncontrolled smoothing, resampling, or automatic effects.
- Make outputs reproducible with clear names, dimensions, settings, dependencies, and handoff notes.
