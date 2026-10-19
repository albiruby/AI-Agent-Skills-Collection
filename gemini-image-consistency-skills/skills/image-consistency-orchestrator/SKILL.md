---
name: image-consistency-orchestrator
description: Entry point and router for the Image Consistency Skills suite. Use whenever the user wants AI-generated images (Gemini / Nano Banana / Imagen) to look consistent across many outputs - a series, a brand, a game, a comic, a product line - or says "lock the style", "keep the same character", "make all assets match", "style bible", "consistent image set". Decides which skills to run, in what order, and keeps one STYLE BIBLE as the single source of truth. Written for Gemini image generation (Nano Banana family, Imagen) in the Gemini app, AI Studio, API, Google Flow and Gemini CLI.
---

# Image Consistency Orchestrator

## Purpose
Image models treat every generation as independent. Consistency only appears when the same locked description is repeated verbatim and anchored by reference images. This skill runs the whole workflow: define, lock, package, produce, verify.

## Core principles
1. **Lock before you generate.** No asset prompts until the style, theme and palette are written down.
2. **One source of truth.** Everything lives in a single STYLE BIBLE (`templates/STYLE_BIBLE.md`). Prompts are assembled from it, never improvised.
3. **Verbatim reuse.** Lock blocks are copied word for word. Paraphrasing a lock is the main cause of drift.
4. **Anchor images beat words.** Approve one canonical image per character, style and environment and reuse it as a reference.
5. **Hierarchy of locks.** Global rules > asset-type canon > asset-specific prompt. A lower level never overrides a higher one.
6. **Verify, then freeze.** Run the QA reviewer on probe images before mass generation, then freeze the bible version.

## Workflow
| Phase | Goal | Skills |
|---|---|---|
| A. Define | Understand the project | `image-project-intake` -> `visual-style-lock` -> `theme-world-lock` -> `color-palette-lock` |
| B. Canon | Fix recurring subjects | `character-identity-lock`, `environment-prop-lock`, `composition-camera-lock` |
| C. Package | Turn canon into prompts | `negative-constraints-guardrails` -> `master-prompt-builder` -> `instruction-slot-packager` -> `asset-manifest-batch-planner` |
| D. Produce | Generate | `reference-image-workflow`, `gemini-image-prompting`, `game-asset-sheet-spec` (game assets only) |
| E. Verify | Check and fix | `consistency-qa-reviewer` -> `drift-correction-iteration` -> `asset-postprocess-handoff` |

## Which skill for which situation
| User says | Run |
|---|---|
| "I want a consistent set of images" (nothing defined yet) | Full workflow from phase A |
| "Here is my style, make prompts" | Skip to phase C |
| "My character keeps changing" | `character-identity-lock`, `reference-image-workflow`, `drift-correction-iteration` |
| "Results look different from each other" | `consistency-qa-reviewer` then `drift-correction-iteration` |
| "I only have 3 instruction slots / a system prompt" | `instruction-slot-packager` |
| "I need 80 game assets" | `asset-manifest-batch-planner` + `game-asset-sheet-spec` |
| "Use these in my app/game" | `asset-postprocess-handoff` |

## Quick start (5-minute minimum lock)
When the user wants speed, do only this and say what was skipped:
1. Ask the 6 intake questions (see `image-project-intake`).
2. Write a 100-word Style Lock Block and a 50-word Theme Lock Block.
3. Pick 6-8 palette colors with hex codes.
4. Generate 3 probe images (object, character, environment) and approve one anchor.
5. Use `master-prompt-builder` for every later prompt.

## Output
- `STYLE_BIBLE.md` (v1.0) filled from the template
- Next recommended skill and why
- A version note: what is locked, what is still open

## Rules
- Ask at most one batch of clarifying questions; use sensible defaults for the rest and list them as assumptions.
- Never invent lore or brand facts the user did not provide; mark them `[assumed]`.
- Keep the user's language for conversation; write lock blocks and prompts in English unless the user asks otherwise (Gemini image models follow English most reliably).
- If the bible changes, bump the version and note which assets must be regenerated.

## Gemini notes
- Best home: a **Gem** (paste `plug-and-play/GEM-INSTRUCTIONS.md`), Google AI Studio (system instruction), or Gemini CLI (`.gemini/skills/`).
- Do not rely on cross-chat memory for visuals: re-attach the anchor images in every new chat.
- Keep one chat per asset family (characters, tiles, UI) so context stays clean.
