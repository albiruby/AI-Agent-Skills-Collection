---
name: master-prompt-builder
description: Assembles final image-generation prompts from the locked bible using a fixed two-part format - LOCK STYLE & THEME first, then the asset-specific prompt - and produces global instructions and per-image prompts that are copy-paste ready for Gemini. Use whenever the user asks to write, standardize, or batch image prompts, a master prompt, a prompt template, or "plug and play prompts". Written for Gemini image generation (Nano Banana family, Imagen) in the Gemini app, AI Studio, API, Google Flow and Gemini CLI.
---

# Master Prompt Builder

## Purpose
Produce prompts that are identical in everything except the subject. The format guarantees every asset carries the same lock.

## Two-part format (every prompt)
```
LOCK STYLE & THEME:
<verbatim: THEME, STYLE, OUTLINE, SHADING, PALETTE, SCALE, EXCLUSIONS, CONSISTENCY>

ASSET GENERATION PROMPT:
<asset type sentence>
<format/layout rules>
<subject lock (character DESIGN LOCK or location/prop line)>
<action / composition>
<output rules>
```

## Anatomy of the ASSET part (in this order)
1. **Asset type and count**: "Create ONE standalone ...", "Create ONE sprite sheet with 6 frames ...".
2. **Format rules**: canvas, aspect ratio, background, padding, grid (see `game-asset-sheet-spec`).
3. **Subject lock**: the Design Lock sentence or the Environment Lock line, verbatim.
4. **Action and composition**: pose, expression, camera sentence.
5. **Output rules**: "Output one image only. No text."

## Process
1. Load the bible. Copy the Lock block exactly; never retype it.
2. For each asset, fill only the bracketed slots: `[ASSET TYPE] [SUBJECT LOCK] [ACTION] [FORMAT]`.
3. Keep the whole prompt under about 350 words; if longer, move stable rules into the global instruction (`instruction-slot-packager`) and keep the repeated lock short.
4. Run `negative-constraints-guardrails` to append standard exclusions.
5. Number prompts with asset IDs from the manifest.
6. Output a Prompt Pack (`templates/PROMPT_PACK.md`) with one fenced block per prompt so each can be copied alone.

## Writing rules
- Use plain, concrete nouns and measurable attributes ("1 px outline", "26 px tall").
- Use the same labels and word order in every prompt; models respond to stable patterns.
- Avoid contradictions between lock and asset text; the lock wins.
- No filler ("masterpiece, ultra detailed, 8k") unless the style truly needs it.
- One image per prompt unless an atlas is the stated goal.
- Write in English by default for best Gemini adherence.

## Template
```
LOCK STYLE & THEME:
{{LOCK_BLOCK}}

ASSET GENERATION PROMPT:
Create ONE {{ASSET_TYPE}} for {{PROJECT_ONE_LINER}}. {{FORMAT_RULES}}

{{SUBJECT_LOCK}}
ACTION / COMPOSITION: {{ACTION}} {{CAMERA_LOCK}}
Output one image only. No text.
```

## Pitfalls
- Re-summarizing the lock "to save space". Shorten the lock once in the bible, never per prompt.
- Adding new style adjectives in one prompt only.
- Stacking several subjects in one prompt, which splits the model's attention.

## Gemini notes
- When references are attached, use the Gemini formula: **[reference images] + [relationship instruction] + [new scenario]**. Place the relationship line (what to copy from which image) between the LOCK block and the scene.
- Keep prompts as clear sentences under each label; avoid keyword soup.
