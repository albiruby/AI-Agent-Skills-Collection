# Subskill 21 — Physics Error Taxonomy

## Purpose
A shared vocabulary for physics and interaction defects so QA reports are precise and recovery is targeted. Always name defects by ID.

## Severity scale
- **S1 Cosmetic:** barely noticeable, no effect on meaning. Approve with note.
- **S2 Noticeable:** visible to attentive viewers; breaks immersion on replays. Repair or regenerate if cheap; accept only with justification.
- **S3 Critical:** breaks the action, story, or product truth. Reject.
Any defect on a hero beat (the contact, the pour, the product mechanism) is raised one level.

## A. Contact and grasp errors
| ID | Name | Visual signature | Typical triggers | First fix |
|---|---|---|---|---|
| A1 | Pre-contact motion (unintended object motion / "levitation") | Object moves, tilts, or flies before the hand touches it | Ambiguous verbs, missing contact beat, object "comes to" the subject | Rewrite with a contact beat; state that the object stays still until grip; shorten/split |
| A2 | Pass-through grasp | Hand passes through the object or handle | No alignment beat, occluded contact, thin handle | Add alignment + wrap; change framing; simplify handle |
| A3 | Clipping / interpenetration | Solids overlap (arm through torso, hand through table) | Tight spaces, occlusion, two-hand tasks | Add clearance; reframe; reduce simultaneous contacts |
| A4 | Ghost grip | Object follows the hand with no finger closure | Skipped grip beat, fast lift | Add explicit finger-wrap beat and a short grip pause |
| A5 | Hovering grip | Fingers stop short of the object but it still moves | Small hands in frame, long clip | Closer framing on contact (test), shorter clip |
| A6 | Non-follow | Object stays/lags while the hand lifts | Fast lift, heavy object | Slow the lift; state weight; reduce lift height |
| A7 | Glued/stuck | Object stays attached after release | Hurried release | Add release + hand withdraw beat |
| A8 | Wrong contact point | Hand grabs the spout/body instead of the handle | Vague noun | Name the part; add a reference |
| A9 | Release hover | Object floats after release | No support surface | State surface; show contact shadow |
| A10 | Wrong object | Subject acts on a different object | Cluttered scene | Declutter; reference the object |

## B. Hand and anatomy errors
| ID | Name | Signature | First fix |
|---|---|---|---|
| B1 | Finger count change | 4/6 fingers mid-action | Simplify pose; state count; mitten/glove if allowed; reframe |
| B2 | Finger fusion/melt | Fingers merge or blur into the handle | Larger handle; slower motion; wider framing |
| B3 | Impossible joint | Bends backward, double joints | Simplify pose; avoid extreme angles |
| B4 | Hand swap | Right becomes left | State anatomical side; keep one hand |
| B5 | Extra hand/limb | A third hand appears | Remove occluding clutter; shorten |
| B6 | Hand scale drift | Hand becomes oversized/tiny | Wider framing; reference |

## C. Dynamics errors
| ID | Name | Signature | First fix |
|---|---|---|---|
| C1 | Floating/weightless | Object or body lacks weight cues | Add weight and effort cues; support |
| C2 | Teleporting/snapping | Instant position jump or sudden alignment | Shorter shot; first/last-frame anchoring; split |
| C3 | Sliding/skating | Feet slide; object slides forever | State footfalls and friction; slow pace |
| C4 | Wrong trajectory | Falls upward or sideways | Specify gravity direction and endpoint |
| C5 | No response | Collision with no reaction | State the response; pick a material |
| C6 | Overreaction | Violent response to light contact | State force proportionality |
| C7 | Momentum violation | Instant stops/turns | Smoother action; slower pace |
| C8 | Balance defiance | Carries heavy load upright with no lean | Add counterbalance cue |
| C9 | Liquid error | Flows upward; level unchanged; stream with no source; dry target | Simplify to spray/droplets; wide framing; hybrid |
| C10 | Energy error | Bounces rise; infinite bounce | Specify a single bounce/rest |

## D. Continuity errors
| ID | Name | Signature | First fix |
|---|---|---|---|
| D1 | Vanish/spawn | Object appears or disappears | Shorter clip; fewer objects; reference |
| D2 | Duplication | Two cans; extra copies | State count; declutter |
| D3 | Morph | Shape/size/color changes | Reference; shorter clip |
| D4 | Orientation flip | Spout points the other way | State orientation per beat |
| D5 | State error | Lid open→closed; full→empty without cause | State ledger; split |
| D6 | Identity drift | Character/object design changes | Reference/model sheet (subskill 04) |
| D7 | Occlusion permanence fail | Object changes after being hidden | Avoid long occlusions |
| D8 | Scale drift | Object grows/shrinks relative to hand | Fixed framing; reference |
| D9 | Background shift | Props move | Locked camera; simpler set |
| D10 | Light/shadow inconsistency | Shadows change direction; missing contact shadow | Name the light source; stable direction |

## E. Causal and logic errors
| ID | Name | Signature | First fix |
|---|---|---|---|
| E1 | Effect without cause | Door opens untouched | Add a trigger beat |
| E2 | Cause without effect | Pressing does nothing | State the response |
| E3 | Reversed causality | Result precedes action | Reorder beats; shorten |
| E4 | Skipped step | Reach → already holding | Add intermediate beats; split |
| E5 | Looping/stutter | Action repeats | Shorter clip; stop-frame description |
| E6 | Action substitution | Different action than requested | Clearer verb; simplify |
| E7 | Intent mismatch | Reaches the wrong direction | State the target and gaze |
| E8 | Speed anomaly | Sudden slow-motion/time-lapse | State a constant pace |

## F. Camera and rendering-physical errors
| ID | Name | Signature | First fix |
|---|---|---|---|
| F1 | Parallax error | Background and foreground don't move consistently | Static camera or simpler move |
| F2 | Warp/rubber geometry | Shapes bend during camera move | Reduce camera motion |
| F3 | Motion ghosting | Smear or ghost trails | Slower motion; shorter clip |
| F4 | Flicker | Texture/lighting flicker | Re-run; stabilization in post only if allowed |

## Mapping common terms to IDs
- "Teleporting" → C2, D-group jumps
- "Floating" → C1, A9
- "Clipping" → A3, A2
- "Sliding" → C3
- "Snapping" → C2
- "Unintended object motion" → A1, E1
- "The can flies instead of being grabbed" → A1 (plus E4 if the grip is skipped)
- "Hands look wrong" → B-group

## Decision matrix
| Situation | Decision |
|---|---|
| Any S3 | Reject; recover (subskill 23) |
| S2 on a hero beat | Reject or repair |
| S2 off hero beat | Repair if cheap; otherwise approve with note |
| S1 only | Approve with note |
| Several S2 clustered in one window | Treat the window as failed; regenerate or split |
