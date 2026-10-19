---
name: consistency-qa-reviewer
description: Reviews generated images against the style bible with a scored checklist - style, palette, identity, scale, camera, technical cleanliness, theme, text artifacts, sheet geometry - and returns a PASS, FIX or REGENERATE verdict with specific differences. Use after any generation batch, on probe images before mass production, when the user asks "is this consistent", "check these images", or uploads outputs for comparison. Written for Gemini image generation (Nano Banana family, Imagen) in the Gemini app, AI Studio, API, Google Flow and Gemini CLI.
---

# Consistency QA Reviewer

## Purpose
Catch drift early and objectively. Compare every output with the locked bible and the anchors, never with memory.

## What to compare
Put outputs next to the relevant anchor (a contact sheet works best). Judge each criterion, not the overall "feel".

## Scorecard (0 = fail, 1 = minor issue, 2 = pass)
| # | Criterion | Check |
|---|---|---|
| 1 | Style | Medium, outline, shading, texture match the Style Lock |
| 2 | Palette | Colors stay in the palette; no neon, no key color inside art |
| 3 | Identity | Face, hair, outfit, signature features match the card/anchor |
| 4 | Proportion and scale | Head ratio, size relative to others, consistent across images |
| 5 | Camera | Viewpoint, framing, light direction match the camera lock |
| 6 | Theme | Motifs, materials and mood fit; no taboo items |
| 7 | Technical | Clean edges, uniform background, no cropping, no artifacts |
| 8 | Text and extras | No text, logos, extra characters or objects |
| 9 | Format | Correct aspect, padding, requested count |

**Verdicts:** total >= 16/18 and no zero -> PASS. 12-15 or one zero fixable by edit -> FIX. Below 12 or identity/style failing -> REGENERATE.

## Sheet checklist (sprite sheets and atlases)
- Frame count equals the spec; equal cells; visible gaps; no overlap or crop.
- Same character height and feet baseline in every frame.
- Walk/run limbs alternate correctly; loop frame returns to start.
- Same scale as the previous sheet of that character.
- Background flat and uniform.

## Process
1. Gather outputs and anchors; note asset IDs.
2. Score each criterion; write one short evidence note per score below 2.
3. Give the verdict and the **smallest change** that would fix it (edit, prompt tweak, new reference, reset).
4. Log in `templates/QA_SCORECARD.md`; list recurring defects and send them to `negative-constraints-guardrails` and `drift-correction-iteration`.
5. At batch level: after every 5-10 assets, review a contact sheet for series-wide drift.

## Report format
```
ASSET: <ID> | VERDICT: PASS/FIX/REGENERATE | SCORE: x/18
ISSUES: 1) <criterion>: <evidence>  2) ...
FIX: <smallest change>
```

## Pitfalls
- Judging each image alone; drift is visible only side by side.
- Accepting "close enough" for identity features; the cast will diverge over time.
- Scoring on beauty. Consistency is the goal.

## Gemini notes
- Use Gemini itself as a reviewer: in a text chat, attach the anchor and the new output and paste the **QA prompt** from `plug-and-play/PROMPT-TEMPLATES.md`. Treat its scores as a first pass and confirm by eye.
