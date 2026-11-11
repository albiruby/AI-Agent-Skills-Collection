---
name: aseprite-animation-blueprints
description: Designs reusable frame-by-frame animation blueprints with key poses, timing, spacing, and acceptance criteria for common 2D game actions. Use when an agent needs the key-pose and timing blueprint for a standard 2D game action — idle, walk, jump, melee attack, hit reaction, death, or spell cast — before drawing frames.
---

# Animation Blueprints

These are starting structures, not rigid frame counts. Adapt them to the requested sprite size, style, speed, and tool capabilities. Never invent a universal FPS or frame count.

## Blueprint format
For every animation, record:
- state name
- one-shot or loop
- key poses in order
- intended timing emphasis
- root/pivot behavior
- secondary motion
- transitions in and out
- likely defects to inspect

## Locomotion
### Idle
- neutral pose
- compression / inhale
- relaxed high pose
- return toward neutral
Keep movement subtle and avoid whole-body pixel jitter. Blink can be a separate event.

### Walk / run
Identify contact, down, passing, and up poses for each side as appropriate. Keep feet aligned to a ground line. Check that the contact foot does not slide unexpectedly. Running usually uses stronger vertical compression and more decisive spacing than walking, but follow the character design.

### Jump
- anticipation
- takeoff
- ascent
- apex
- descent
- landing impact
- recovery
Keep trajectory and ground contact understandable. Do not force a loop.

## Combat
### Melee attack
- anticipation / wind-up
- committed strike
- impact or contact pose
- follow-through
- recovery
Keep weapon direction, arm attachment, and character silhouette coherent. Use a separate impact effect if useful.

### Projectile attack
- aim / anticipation
- release
- follow-through
Keep projectile origin and direction consistent. Avoid changing hand or weapon side accidentally.

### Hit reaction
- pre-hit or neutral
- impact compression
- recoil
- recovery
Communicate the hit through silhouette and spacing rather than arbitrary flashing alone.

### Death
- loss of balance or decisive hit
- collapse / fall
- settling
- final pose
Keep the ending readable and avoid unnecessary extra frames.

## Magic casting blueprint
- ready / focus
- charge begins
- energy grows
- peak charge
- release pose
- follow-through
- exhaustion or recovery if requested

For a mage who becomes winded, show the cost with posture, shoulder drop, breathing, or staff support. Avoid random full-body shaking.

## VFX blueprint
- anticipation
- bright / high-energy peak
- expansion or travel
- fragmentation
- fade / residue
Keep the effect readable at native resolution and avoid clipping at frame edges.

## Timing guidelines
- Assign timing to the intent: anticipation may be held longer; impact often reads as a brief accent; recovery may be slower.
- Use actual supported frame-duration units.
- Preview at the target speed.
- If no preview tool exists, report timing validation as incomplete.
