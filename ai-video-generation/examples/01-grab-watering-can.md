# Example 01 — Grabbing a Watering Can (full pipeline)

> Illustrative walk-through. Nothing here claims a video was generated or reviewed. Replace the character and setting with your project's own.

## Brief
A woman in a green apron walks to a wooden bench in a garden, takes a green metal watering can, and carries it toward tomato plants. 8 seconds, 16:9, realistic style, no dialogue.

## Gate A — Risk
- Interactions: pick up (R2), carry (adds R3), set-down not needed.
- Modifiers: continuous take, carry with a turn → raise to **R3**.
- Policy: interaction spec required; prefer split shots; plan 4–8 takes.

## Interaction spec (summary)
- Object: one green metal watering can, long spout, **top handle**, resting on the left end of the bench, spout pointing right. State: empty (or full; choose one and keep it).
- Subject: right hand, power grip on the top handle, approach from the side with the palm facing down.
- Beats: gaze at can → walk to bench → right hand reaches the top handle → fingers wrap → brief pause → lift → carry at her side toward the plants, slight lean to counterbalance.
- Rule: **the can stays completely still until her fingers close around the handle.**
- Camera: medium shot, static camera, contact area unobstructed.

## Gate B — Encoded prompt (single-shot version)
```
Medium shot, static camera. A woman in a green apron stands beside a wooden bench in a sunny garden with tomato plants in the background. A green metal watering can with a long spout and a top handle rests on the left end of the bench and stays completely still.
She reaches out with her right hand to the top handle; her fingers wrap around the handle; she pauses for a moment, then lifts the can. The can rises at the same speed as her hand. She carries the can at her side toward the tomato plants, leaning slightly to counterbalance its weight.
Natural daylight from the upper left, soft shadows, realistic style.
```
Targeted exclusions (only if the tool supports them and only after seeing the failure): "can moving before the hand touches it", "extra fingers".

## Simplified fallback (if unstable)
"Medium shot, static camera. The woman stands beside the bench with her right hand already resting on the can's top handle. She lifts the can a short distance and holds it at her side."

## Split-shot plan (recommended for R3)
| Shot | Content | Ends with | Anchor |
|---|---|---|---|
| A (0–3 s) | Walks to bench, reaches toward the handle | Fingers wrapping the handle; can has not moved | Start frame: can on bench |
| B (3–6 s) | Medium close insert: grip and lift; the can follows the hand | Can lifted at her side | Start from A's last frame if supported |
| C (6–8 s) | Medium wide: carries toward the plants | Reaches the plants | Start from B's last frame |

## Gate C — Checkpoints to inspect
T0 can on bench, count one → T2 can still before touch → T3 right hand on the **top handle** → T4 fingers wrapped, count correct → T5 can moves **with** the hand → T6 same can size and same hand during carry → T9 end position in the garden.

## Gate D — If a failure appears
| Observation | ID | Next step |
|---|---|---|
| The can lifts a few frames before her fingers close | A1 | L2: add "stays completely still until her fingers close"; if repeated, L5 split at the grip |
| Fingers go through the handle | A2 | L4: reframe to medium close on the hand; L3: bigger handle or hook grip |
| Can follows the hand but with no fingers wrapped | A4 | L2: add grip pause beat; L5 |
| Spout flips direction mid-carry | D4 | Add orientation per beat; shorten the carry |
| Can duplicates during the walk | D2 | Declutter; shorten; reference |
