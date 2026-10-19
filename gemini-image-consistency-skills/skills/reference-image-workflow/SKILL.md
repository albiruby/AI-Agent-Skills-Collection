---
name: reference-image-workflow
description: Workflow for using anchor and reference images to keep characters, styles and environments consistent, including how to label references in prompts, when to edit instead of regenerate, how to avoid copy-of-a-copy drift, and when to reset a chat. Use when attaching images to Gemini or other image models, when a character must match an existing picture, or when edits keep breaking the design. Written for Gemini image generation (Nano Banana family, Imagen) in the Gemini app, AI Studio, API, Google Flow and Gemini CLI.
---

# Reference Image Workflow

## Purpose
Words describe; images fix. A small set of approved anchor images, reused correctly, removes most drift.

## Anchor set
| Anchor | Purpose | Approve by |
|---|---|---|
| Style anchor | Rendering, palette, outline | Looks exactly like the intended style |
| Character anchor (per character) | Identity | Matches the card; clean turnaround or neutral pose |
| Environment anchor (per location) | Architecture and light | Matches location card |
| Format anchor | Sheet or layout geometry | Correct grid and spacing |

Name files `ANCHOR_<type>_<name>_v<N>.png` and record them in the bible.

## Rules for using references
1. **Always reference the anchor, never the last output.** Chaining outputs causes copy-of-a-copy drift.
2. **Label every attached image by role** in the prompt: "Image 1 is the character identity reference. Image 2 is the style and palette reference. Keep the identity from image 1 and the rendering from image 2."
3. **Start with 2-4 references** per request. Nano Banana 2 accepts many more (up to 14 per current guides; verify for your model), but each extra reference dilutes the others, so add more only for a clear reason.
4. **State what to keep and what to change.** "Keep face, outfit, colors and proportions identical. Change only the pose to X."
5. **Edit instead of regenerate** when 90% is right: "Using the provided image, change only <X>. Keep everything else exactly the same."
6. **Pair the Design Lock sentence with the image.** Text and picture reinforce each other.

## Conversation hygiene
- Long chats accumulate noise. After about 8-10 iterations, start a fresh chat with: lock block + anchor images + the one change wanted.
- Do one change per edit. Combined edits cause side effects.
- Save every accepted result with an ID before continuing.

## Process
1. Generate probes, approve anchors (`consistency-qa-reviewer`).
2. For each new asset: attach relevant anchors + paste the full prompt from `master-prompt-builder`.
3. If the result drifts, run `drift-correction-iteration` before trying again.
4. When the design intentionally changes, create `v2` anchors and mark older assets for regeneration.

## Prompt snippets
- Identity transfer: `Use the provided character image as the exact identity reference. Draw the same character in <pose>, same proportions, outfit, colors and line weight.`
- Style transfer: `Match the rendering, outline, palette and shading of the provided style reference exactly; do not copy its subject.`
- Minimal edit: `Using the provided image, change only <X>. Keep everything else exactly the same.`

## Pitfalls
- Attaching a style reference whose subject is strongly different; the model copies the subject. Use a neutral object as style anchor.
- Mirrored references flip asymmetric details. Use true-side views for asymmetric designs.
- Letting an unapproved "pretty good" image become the reference.

## Gemini notes
- Gemini image models are built for reference-driven work: attach the character sheet and style anchor, then use `[reference images] + [relationship instruction] + [new scenario]`.
- In the app, anchors must be re-attached in every new chat; in the API, send them in `contents` before the prompt.
- Gemini can extract a character from an existing image into a clean reference; do this once, approve it, and treat that file as the anchor.
