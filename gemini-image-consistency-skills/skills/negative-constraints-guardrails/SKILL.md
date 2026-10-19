---
name: negative-constraints-guardrails
description: Builds standard exclusion blocks and guardrails for image prompts - unwanted styles, artifacts, text and logos, extra objects, copyrighted characters, real people, unsafe or off-tone content, cultural sensitivity - and phrases them for models with or without a negative prompt field. Use when outputs contain unwanted elements, before finalizing any prompt pack, or when the project has brand, cultural or safety constraints. Written for Gemini image generation (Nano Banana family, Imagen) in the Gemini app, AI Studio, API, Google Flow and Gemini CLI.
---

# Negative Constraints & Guardrails

## Purpose
Prevent recurring defects and keep the project safe and original. Exclusions are part of the lock, not an afterthought.

## Standard exclusion groups
| Group | Typical exclusions |
|---|---|
| Rendering | gradients, glow, blur, anti-aliasing, 3D render look, photorealism, glossy shine |
| Artifacts | extra limbs, merged frames, duplicated subjects, cropped subject, watermark, border, frame |
| Text | letters, numbers, labels, logos, signatures |
| Additions | extra characters, extra props, decorative clutter, background scenery on asset sheets |
| Color | neon, oversaturated primaries, pure black/white fills, key color inside art |
| Composition | changed perspective, tilted camera, vignette, floor shadow |
| Tone | content outside the project's audience rating |

## Phrasing
- **Models with a negative field:** list items plainly; also keep a positive version in the main prompt.
- **Models without one:** put a single `EXCLUSIONS:` line near the end and restate the key defect positively ("flat color clusters", "uniform background").
- Keep the list to the 6-10 defects you actually see. Long lists increase side effects.

## Originality and IP
- Do not reference copyrighted characters, franchises, trademarks or living artists by name; describe the attributes instead.
- Do not generate real people's likeness without explicit rights; use fictional characters.
- Original designs only; if a design resembles a famous character, change silhouette and key features.

## Cultural and content care
- Use specific, respectful details drawn from the user's sources; avoid mixing cultures or caricature.
- Respect the audience rating; keep imagery age-appropriate.
- Follow the provider's usage policy; if a request conflicts, offer a safe alternative instead of working around it.

## Process
1. Start from the standard groups; delete those not relevant.
2. Add defects found during QA (feed from `consistency-qa-reviewer`).
3. Write the final line: `EXCLUSIONS: ...` and store it in the bible.
4. Re-check each time the style changes.

## Pitfalls
- Using only negatives ("not blurry"). Pair with a positive description.
- Excluding the thing the model needs ("no background") when a flat key color is wanted.

## Gemini notes
- Gemini image generation typically has no separate negative-prompt field. Write the positive version in the body ("uniform flat background") and keep one `EXCLUSIONS:` line near the end. Verify in current docs for your surface.
