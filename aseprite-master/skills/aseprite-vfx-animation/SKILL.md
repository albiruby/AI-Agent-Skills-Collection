---
name: aseprite-vfx-animation
description: Creates pixel-art visual effects such as magic spells, projectiles, explosions, smoke, impact flashes, particles, trails, auras, and elemental effects. Use when the user wants a spell cast, fireball, explosion, hit flash, smoke, particle trail, or elemental effect animated as its own sprite sequence.
---

# VFX Animation

## Plan the effect as phases
For a spell, for example:
1. Charge / anticipation
2. Energy accumulation
3. Release flash
4. Projectile or traveling effect
5. Impact
6. Dissipation / residue

For impact effects:
- contact flash
- expanding shape or debris
- peak contrast
- fragmentation
- fade / smoke / particles

## Shape language
- Fire: irregular upward tongues, bright core, darker outer mass.
- Ice: angular shards, crisp highlights, sparse particles.
- Lightning: sharp directional zigzags, strong contrast, brief exposure.
- Arcane magic: rings, runes, orbiting motes, controlled accent colors.
- Smoke: expanding soft-edged clusters, broken contours, slower dissipation.
- Physical impact: radial burst, debris, dust, recoil cues.

These are visual heuristics, not mandatory genre rules; follow the brief.

## Production rules
- Make the effect readable at native size.
- Keep character and effect layers separate when possible.
- Use distinct silhouettes for charge, travel, impact, and fade.
- Preserve travel direction and projectile origin.
- Avoid uniform circular growth if the effect needs directional energy.
- Avoid overusing single-pixel particles.
- Keep the effect's brightest moment brief unless the style calls for sustained glow.
- Validate transparency and bounding-box margins so the effect is not clipped.
- Ensure the character's hands, weapon, or staff align with the effect origin.

## Mage casting sequence checklist
- Mage anticipation and charge pose
- Energy visibly accumulates over multiple frames
- Release pose is distinct from charge pose
- Projectile has a clear direction and shape
- Impact or disappearance is represented if requested
- Mage follow-through / recoil / exhaustion is readable
- Effects do not obscure the entire character unintentionally
- Timing communicates effort and impact
