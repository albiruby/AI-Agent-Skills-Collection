# Subskill 22 — Frame-by-Frame QA

## Purpose
Inspect interaction shots at the frames that matter: before, during, and after contact. A hero frame or a normal-speed watch is not enough.

## Honesty rule
Only report what you actually inspected. If you cannot view video or frames, say so and give the user the review steps and the scripts in `scripts/`. Never write "reviewed, looks good" without having seen the frames.

## Review passes
| Pass | Speed | What to look for |
|---|---|---|
| 0 Technical | — | Duration, aspect ratio, resolution, frame rate, audio presence (`scripts/video_probe.sh`) |
| 1 Intent | Normal | Does the action read? Does the story beat happen? |
| 2 Motion | 0.5× to 0.25× | Smoothness, pre-contact motion, hover, sliding, speed anomalies |
| 3 Checkpoints | Frame by frame | Contact, grip, lift, release (below) |
| 4 Whole-shot | Normal again | Continuity, identity, state, lighting |

## Checkpoints (extract these frames)
| Checkpoint | When | Questions |
|---|---|---|
| T0 Pre-state | First frame | Object at rest? Correct count, orientation, position? |
| T1 Approach | Mid-approach | Hand path plausible? Object still unmoved? |
| T2 Pre-contact | 2–4 frames before first touch | Is the object stationary? Is there a gap between hand and object? |
| T3 Contact | First touch | Correct part? Correct hand? Touch visible? No pass-through? |
| T4 Grip | A few frames after contact, before lift | Fingers wrapped? Count correct? Object still in place? |
| T5 Lift start | First movement of the object | Does it move **with** the hand? Weight cue? |
| T6 Carry mid | Middle of carry | Same hand, same part, same size, same distance? |
| T7 Release | Fingers open | Object supported? Hand withdraws cleanly? |
| T8 Settle | Just after release | Residual motion physical? Contact shadow present? |
| T9 End state | Last frame | Matches the brief and ledger? |

For other verbs substitute the checkpoints (door: handle contact, first opening motion, mid-swing, stop).

## Method
1. Extract frames: `scripts/extract_frames.sh <video> <outdir> [fps] [start] [end]`. Use 8–12 fps over the interaction window, higher (24–30) around the contact.
2. Build a contact sheet: `scripts/contact_sheet.py <outdir> sheet.png --fps 10`. Review in order with timestamps.
3. Optional objective check: `scripts/roi_motion.py <outdir> --fps 10 --roi x,y,w,h --contact T` reports motion energy inside the object's region. Spikes **before** the first touch time suggest A1 (pre-contact motion). This is a heuristic signal; confirm by eye.
4. Compare against the object reference or ledger for shape, size, and count.
5. Record findings in `templates/frame-qa-log.md` using taxonomy IDs and severities.

## What to measure by eye
- Object displacement between consecutive frames before contact (expected ≈ 0).
- Finger count at T3, T4, T5, T7.
- Gap between fingers and handle at T2 and T3.
- Object-to-hand distance during carry (should be stable).
- Object height and contact shadow at T8.
- Object state at T0 vs T9.

## Pass/fail logic
- Fail immediately: A1, A2, A4 at hero beats; B1/B2 at hero beats; D1/D2 on the main object; C9 on a required pour; any S3.
- Repair or regenerate: clustered S2 defects; unresolved continuity problems.
- Approve with note: isolated S1 or S2 off hero beats.

## Reporting format
```
Shot: <name> | Tier: R<n> | Take: <n>
Checkpoints reviewed: T0–T9 (frames extracted: yes/no)
Defects: <ID – description – timestamp – severity>
Objective vs taste: <separate lists>
Decision: Approve / Approve with note / Regenerate / Simplify or split / Repair in post
Next change (one variable): <...>
```

## Common review traps
- Approving from a hero frame.
- Missing a one-frame jump in the contact window.
- Forgetting to count fingers in motion blur frames.
- Letting a good-looking background distract from an incorrect interaction.
- Ignoring audio sync with contact events (a click before the touch).
