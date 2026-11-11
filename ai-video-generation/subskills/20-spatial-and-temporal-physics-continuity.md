# Subskill 20 — Spatial and Temporal Physics Continuity

## Purpose
Keep objects and characters physically consistent from frame to frame and shot to shot. This extends subskill 08 with strict per-object tracking for interaction shots.

## Object ledger (per interaction shot)
Track every object that matters:

| Field | Example |
|---|---|
| Identity | Green metal watering can, long spout, top handle |
| Count | Exactly one |
| Size/scale | Roughly forearm height; stays that size |
| Position | On the wooden bench, left end |
| Orientation | Spout points right |
| State | Full of water; lid closed |
| Attachment | Resting on bench → in right hand → at her side |
| Light/shadow | Soft shadow on bench, light from upper left |

Update the ledger at every beat. Any change not caused by a beat is a defect.

## Frame-to-frame invariants
Unless the story changes them, these stay constant:
- Shape, scale, color, material, count of objects.
- Character outfit, hair, accessories, and hand/finger count.
- Light direction, shadow direction, time of day.
- Background props and architecture positions.
- Support relationships (what sits on what).

## Object permanence and occlusion
- An object that goes behind another object or out of frame must return with the same shape, color, orientation, and state.
- Anything hidden by a body part (the hand covers the handle) must be the same object when revealed.
- Do not rely on long occlusions when an object's identity matters.

## Teleporting and snapping
- Position changes must be continuous. Any jump larger than the motion between adjacent frames, without a cut, is a defect.
- Snapping (sudden alignment into the hand or onto a surface) is a defect even if the end state is correct.

## Spatial relations
- State relative positions with anchors: "on the left end of the bench, near the tomato plants".
- Maintain screen direction (subject moves left-to-right) across cuts (subskill 05).
- Keep distances plausible: a reach should match arm length; a carry should keep the object at a stable distance from the body.

## Shot-to-shot hand-off (multi-shot)
1. Record the **end state** of shot N (positions, held objects, pose, light).
2. Use it as the **start state** of shot N+1.
3. When the tool supports it, use the last frame of N as the first frame of N+1 or as a reference image; otherwise restate the state in text and attach references.
4. Check cut points: do not cut mid-contact unless the contact continues convincingly in the next shot (cut on action: after grip, before lift).
5. Reverify identity (can design) and hand count in each shot.

## Clip length and drift
Longer continuous takes give the model more opportunities to drift in shape, count, and physics. For continuity-heavy content generate shorter shots and assemble the approved segments. Extensions and "continue" features can accumulate errors; inspect the join.

## Ledger entries for liquids and states
- Fullness levels (full, half, empty) change only through the pour.
- Wetness persists (wet soil stays dark).
- Doors, lids, and switches keep their state between shots.

## Checklist
- [ ] Ledger filled for all key objects
- [ ] No unexplained changes in shape/size/color/count
- [ ] Occlusions resolved consistently
- [ ] No teleporting/snapping
- [ ] Lighting and shadow direction stable
- [ ] End state of shot N equals start state of shot N+1

Use `templates/continuity-ledger.md`.
