# Subskill 23 — Failure Recovery

## Purpose
When a model keeps failing on a physical interaction, escalate **systematically** instead of piling on adjectives and negative prompts. Each step changes one variable, is logged, and has a stop-loss.

## Principles
1. Diagnose first (taxonomy ID, window, severity).
2. Change one variable per attempt.
3. Use a stop-loss: after about 3 failed attempts at one rung, move down the ladder (heuristic; adjust to credits).
4. Prefer reducing the difficulty of the shot to increasing the length of the prompt.
5. Never claim success without re-running the inspection (subskill 22).
6. Do not hide a failure that the audience is meant to rely on (product truth, safety, scientific demonstrations).

## The recovery ladder
| Rung | Action | When to use |
|---|---|---|
| L0 | Verify inputs: reference actually attached, correct mode, correct aspect/duration, correct prompt version | Any unexpected result |
| L1 | Resample: new seed/variation of the same prompt | Defect looks random, tier R2 or lower |
| L2 | Clarify the prompt: name the part and hand, add the contact beat, state "stays still until contact", remove conflicting instructions, put the action in chronological order, shorten | Ambiguity-type errors (A1, A8, E4, E6) |
| L3 | Simplify the action: one hand, stationary object, shorter distance, slower pace, no turn while carrying, remove secondary actions | Complex or chained errors (A4, A6, C8, E5) |
| L4 | Reframe: medium shot that shows the whole chain; static camera; remove occluders; avoid extreme macro on fingers | Hand/anatomy and clipping errors (A2, A3, B-group) |
| L5 | Decompose into shots: (A) reach until contact, (B) insert of grip/lift, (C) carry; cut on action | R3 shots; repeated failures at the contact beat |
| L6 | Keyframe anchoring: start frame with the object in place; end frame with the hand on the handle or the object lifted; or generate the contact frame as an image and animate from it (when the tool supports first/last-frame or image-to-video) | Drift, snapping, wrong state |
| L7 | Change mode or model: another model, video-to-video, motion reference | Repeated structural failures on the same model |
| L8 | Hybrid: real footage insert, compositing, 3D/simulation render, animation, or an editorial trick (below) | R4 or hero beats that must be exact |
| L9 | Redesign the idea: imply the action off-screen or by outcome (she walks out of frame, returns with the can) | When the interaction is not essential |

## Editorial tricks (disclose when the audience relies on the action)
- Cut on action: end Shot A as the fingers close, start Shot B with the can lifted.
- Cutaway/insert: show the face, the plants, or the can's spout while the contact happens off-screen.
- Occlude with the body or frame edge, then verify re-emergence (subskill 20).
- Trim to the good segment; join approved segments from different takes.
- Speed changes only when they are stylistically appropriate.
- Overlays, masking, or compositing of a clean plate for the defect region.
Do not use these to present a false depiction of a real product, mechanism, safety behavior, or scientific result.

## Error → first recovery step
| Error IDs | Start at |
|---|---|
| A1, A8, A10, E1, E4, E6, E7 | L2 (clarify prompt), then L3 |
| A2, A3, A5, B1–B6 | L4 (reframe), L3 (simplify hand pose), then L5 |
| A4, A6, A7, A9 | L2 then L3 (add grip/release beats), then L5 |
| C1–C10 | L2 (weight/trajectory cues), L3, then L8 for liquids/impacts |
| D1–D10 | L6 (anchoring), L5 (shorter shots), reference (subskill 04) |
| E5, E8 | L3 (shorter and simpler), L1 |
| F1–F4 | L4 (static camera) then L1 |

## Targeted correction prompt patterns
Keep unchanged parts verbatim; edit only the failing sentence.
- A1: "The watering can stays completely still on the bench. Only after her right hand grips the handle does the can lift with her hand."
- A4/A6: "Her fingers close around the handle, she pauses, then lifts the can with her arm; the can rises at the same speed as her hand."
- B1: "Her right hand has five fingers wrapped around the handle." (use sparingly; prefer reframing)
- A9: "She places the can on the bench; the can rests on the wood with a soft shadow beneath it."
- C9: "She tilts the can; water sprays from the rose head in small droplets and darkens the soil."
Do not append a block of generic negatives. Fix the actual beat.

## Split-shot template
```
Shot A (0–3 s): Medium shot. [Subject] walks to the bench and reaches toward the can's handle. End on the right hand wrapping around the handle. Object has not moved.
Shot B (3–6 s): Medium close insert of the hand lifting the can by its handle; the can follows the hand.
Shot C (6–9 s): Medium wide. [Subject] carries the can toward the plants; same hand, same handle.
Anchors: end state of A = start state of B; use last frame as first frame when supported.
```

## Logging
Record each attempt in `templates/iteration-log.md`: prompt version, variable changed, taxonomy IDs found, decision. Stop-loss: record why you moved down a rung.

## When to stop
- The brief is satisfied by an approved take or edit.
- The remaining defects are S1 and accepted.
- The cost of further attempts exceeds the value; propose L8 or L9.
Tell the user plainly which rung solved it and what limits remain.
