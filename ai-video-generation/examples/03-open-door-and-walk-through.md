# Example 03 — Opening a Door and Walking Through

> Illustrative walk-through; no generation is claimed.

## Brief
A man opens a wooden door and walks into the next room. 6 seconds.

## Gate A — Risk
Hinged mechanism + body passes through an opening → **R3**.

## Interaction spec (summary)
- Door: opens **inward**, hinge on the **left** (anatomical left of the man as he faces the door), round brass handle at waist height.
- Beats: man stops at the door → right hand grips the handle → handle turns → door swings open along its arc → he steps through after the door is fully open → he exits frame.
- Rule: the door does not move until the handle is turned and pushed.

## Prompt
```
Medium shot, static camera, from the hallway side. A man in a grey jacket stands in front of a closed wooden door with a brass round handle. His right hand grips the handle and turns it; he pushes, and the door swings open inward on its left hinge. After the door is fully open, he steps through the doorway into the room.
Soft indoor light, realistic style.
```

## Gate C — Checkpoints
T2 door closed and still → T3 hand on the handle (correct hand) → T4 handle turn visible → T5 first door movement after the turn → T6 mid-swing arc consistent with the hinge side → T7 he passes through the open doorway without clipping → T9 door left open, state consistent.

## Common failures
E1 (door opens untouched), A2 (hand through handle), A3 (body clips the door), D4 (hinge side flips), D5 (door changes open/closed state).

## Recovery
L2 add hinge + trigger beats, L3 start with his hand on the handle, L5 split into "open" and "walk through" shots with a cut on action, L9 show only the room beyond and his silhouette entering.
