---
name: asset-manifest-batch-planner
description: Plans a complete set of image assets as a manifest with IDs, categories, priorities, dependencies, sizes and generation order, then feeds each row to the prompt builder. Use when the user needs many images (game asset packs, icon sets, comic pages, product shots, social series), wants a coverage list ("what assets do I need"), asset IDs, a generation roadmap, or a batch of prompts. Written for Gemini image generation (Nano Banana family, Imagen) in the Gemini app, AI Studio, API, Google Flow and Gemini CLI.
---

# Asset Manifest & Batch Planner

## Purpose
Turn "I need a lot of images" into an ordered, trackable list so nothing is missed and the riskiest assets are validated first.

## Manifest columns
| Column | Meaning |
|---|---|
| ID | Stable code, e.g. `TM-WALK-DOWN`, `ENV-HOUSE-01`, `UI-BTN-02` |
| Category | character, tile, prop, item, vfx, ui, background, key art |
| Name | Human readable |
| Spec | Size, frames, aspect, background |
| Depends on | Anchor or asset that must exist first |
| Priority | P0 core, P1 needed, P2 nice |
| Status | todo, drafted, approved, post-processed, shipped |
| Prompt | Link to Prompt Pack entry |

## ID convention
`<GROUP>-<THING>[-<VARIANT>][-<DIR>]`, uppercase, hyphens, no spaces. Groups are short (2-4 letters) and listed in the bible.

## Coverage matrices (use for characters)
Rows = characters, columns = animations (idle, walk, run, attack, hurt, death), sub-columns = directions (down, up, left, right). Mark mirrored directions to cut work.

## Generation order
1. **Probes**: 1 object, 1 character, 1 environment. Approve anchors.
2. **Character anchors** and turnarounds.
3. **Highest-risk assets** (complex sheets, hands, multi-object atlases) to find problems early.
4. **Bulk assets** (tiles, props, items) using the same lock.
5. **Special assets** (key art, backgrounds, UI).
6. **Variants** (day/night, damage states) by editing approved images.

## Process
1. Read brief and bible; list deliverables by category.
2. Build the manifest (`templates/ASSET_MANIFEST.md`), assign IDs and priorities.
3. Mark dependencies and the generation order.
4. For each row call `master-prompt-builder` and store the result in the Prompt Pack.
5. After each batch of 5-10 assets, run `consistency-qa-reviewer` on a contact sheet before continuing.
6. Update statuses; report counts per status.

## Estimating effort
Assume 1.5-3 generations per approved asset for simple items and 3-6 for sheets and complex scenes. State this as an estimate and update it after the first batch.

## Pitfalls
- Generating everything first and checking later.
- Inconsistent IDs; renames break engine references.
- Forgetting variants and states until the end.

## Gemini notes
- In the app, generate one asset per message. For dozens of assets use `plug-and-play/batch_generate.py` with a JSON prompt pack made by `plug-and-play/pack_to_json.py`.
