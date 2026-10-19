---
name: drift-correction-iteration
description: Diagnoses and fixes consistency drift in AI image generation - style, identity, palette, scale, perspective, detail creep, hallucinated additions, text artifacts - with a symptom-to-fix map, one-variable-at-a-time iteration, reset rules and a prompt changelog. Use when images no longer match, a character or style keeps changing, edits break the design, or the user says "it keeps changing" or "why is it different now". Written for Gemini image generation (Nano Banana family, Imagen) in the Gemini app, AI Studio, API, Google Flow and Gemini CLI.
---

# Drift Correction & Iteration

## Purpose
Fix drift systematically instead of rewording prompts at random.

## Diagnose first
| Symptom | Likely cause | Fix |
|---|---|---|
| Style slowly changes over a session | Long chat noise, paraphrased lock | Fresh chat, paste the verbatim lock and anchors |
| Character face/outfit changes | No reference, Design Lock paraphrased | Attach the anchor, restate the Design Lock, edit instead of regenerate |
| Colors turn saturated | Palette stated loosely | Palette with names + hex + "muted", forbid neon |
| Sizes differ between sheets | No scale anchor | Add size line and a scale anchor; fix in post by normalization |
| Perspective changes | Camera lock missing or buried | Put camera sentence right after the style lock |
| New objects appear | Prompt too open | Add "do not add anything else", shorten the prompt |
| Details multiply | "ultra detailed" style words | Remove them; state minimal detail density |
| Frames touch or overlap | Geometry unclear | Use `game-asset-sheet-spec` wording, reduce frame count or widen canvas |
| Text shows up | Model decoration habit | Add "no text" and remove words that suggest signs or labels |
| One asset type always fails | Needs a different workflow | Split the request or generate modules and assemble |

## Iteration protocol
1. **Freeze**: note the prompt, references, and result.
2. **Change one variable** (wording, reference, aspect, prompt length). Not several.
3. **Compare** against the failed image and the anchor.
4. After **3 failed attempts**, change strategy: edit an existing image, split the task, simplify the design, or generate a different view and fix in post.
5. **Reset** the chat when drift appears after many turns.
6. Record what worked in the prompt changelog.

## Prompt changelog format
```
v1.3 (date): moved camera sentence after style lock; reason: perspective drift; result: fixed in 4/5 tests
```

## Design simplification (often the real fix)
If something never stays stable (tiny accessories, complex patterns, hands), simplify the design in the bible and update the card, then regenerate anchors with a version bump.

## Pitfalls
- Adding more adjectives in every retry; prompts become contradictory.
- Editing the lock to suit one failed image.
- Skipping the version bump when the bible changes.

## Gemini notes
- Fastest fix order on Gemini: (1) new chat with lock + anchors, (2) edit prompt "change only X", (3) simplify the design element that keeps failing.
- Long chats accumulate noise; reset after about 8-10 turns.
