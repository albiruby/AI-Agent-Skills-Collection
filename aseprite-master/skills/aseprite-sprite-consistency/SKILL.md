---
name: aseprite-sprite-consistency
description: Maintains visual and structural consistency across characters, views, poses, animation states, and batches of Aseprite assets. Use when new sprites, views, or frames must match an existing character or approved batch, or when the user warns that proportions, palette, or style are drifting.
---

# Sprite Consistency System

## Create a source of truth
For recurring assets, maintain a compact character/asset bible containing:
- asset ID and version
- native dimensions and baseline
- silhouette landmarks
- head/body proportions
- face and feature placement
- palette swatches and color roles
- light direction and shadow rules
- outline policy
- costume, equipment, and accessory placement
- handedness and facing-direction conventions
- allowed deformations during animation
- known exceptions

## Consistency checks
Compare new frames/assets against the source of truth:
- Does the head scale remain stable?
- Are shoulders, hips, hands, feet, and major landmarks coherent?
- Are clothing colors and accessory locations preserved?
- Does the light direction remain consistent?
- Is the outline treatment stable?
- Are weapon and spell origins aligned with the intended hand?
- Does the baseline or pivot drift without an animation reason?
- Are the colors from the agreed palette or deliberate additions?

## Batch production
1. Finalize one representative asset before generating variants.
2. Record accepted dimensions, palette, and style decisions.
3. Produce a small sample batch.
4. Compare sample assets side-by-side.
5. Correct systematic drift before scaling up.
6. Keep an exception log for intentional changes.

## Reference priority
When references conflict, use this order unless the user specifies otherwise:
1. explicit user instructions,
2. current approved project bible,
3. approved source asset,
4. earlier draft,
5. inferred convention.

Do not silently blend incompatible art styles. Report conflicts and ask only when the decision materially affects the outcome.
