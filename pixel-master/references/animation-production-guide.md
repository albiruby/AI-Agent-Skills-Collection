# Animation Production Guide

## 1. State matrix

Define every clip before drawing:

| State | Trigger | Directions | Frames | Loop | Pivot |
|---|---|---|---:|---|---|
| idle | default | 4/8 | 4-8 | yes | bottom-center |
| walk | movement | 4/8 | 6-8 | yes | bottom-center |
| run | sprint | 4/8 | 6-8 | yes | bottom-center |
| attack | input | 4/8 | 5-8 | no | bottom-center |
| hit | damage | 4/8 | 2-3 | no | bottom-center |
| death | zero HP | 4/8 | 6-10 | no | bottom-center |

Adapt counts to the project; do not treat them as universal.

## 2. Frame budget and timing

- Define total frames and per-frame durations in ms.
- Use non-uniform timing for weight: anticipation, impact hold, recovery.
- Typical authentic pixel motion: 8-15 FPS; smooth/high-frame-rate styles may use more.
- Keep gameplay events explicit: hitbox on/off, projectile spawn, footstep, VFX, sound.
- Avoid flat timing on combat actions; it feels robotic.

## 3. Key poses

- Silhouette first: every key pose must read as a flat shape.
- Anticipation: compress/coil before the action.
- Impact: strongest silhouette and contrast at the active frame.
- Follow-through: secondary motion (hair, cape, weapon) 1-2 frames later.
- Recovery: return to a stable pose that blends into idle/walk.
- For loops, ensure the last frame leads naturally into the first.

## 4. Pivot and baseline

- Lock one pivot (bottom-center or foot baseline) across all frames and directions.
- Keep the character's feet on a consistent ground line unless airborne.
- Reserve canvas space for weapon/VFX overhang without clipping.
- Do not scale the character between frames unless intended.

## 5. Directions and consistency

- Mirror only symmetric designs; redraw asymmetric gear/handedness.
- Keep head size, torso length, and limb thickness consistent across directions.
- Check walk/run foot contacts and hip height.
- Use a turnaround/reference sheet for every direction.

## 6. Export

- Native editable source (Aseprite/Piskel/Pixelorama/ORA) plus PNG sheet.
- JSON/XML metadata: frame tags, durations, pivots, events.
- Consistent cell size and padding; document rows/columns.
- Provide GIF/APNG previews for review, not as the production source.
- Keep the exposure sheet with the deliverable.

## 7. QA

- [ ] Pivot/baseline stable across frames.
- [ ] Loop has no duplicate/hitch.
- [ ] No frame pop, volume drift, or scale drift.
- [ ] Silhouette reads at 1x gameplay size.
- [ ] Timing matches the exposure sheet.
- [ ] Events align with hitboxes/VFX/sound.
- [ ] Engine playback tested.
