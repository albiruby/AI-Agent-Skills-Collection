---
name: gemini-image-prompting
description: Core Gemini image skill - how to prompt and edit with Gemini image models (Nano Banana family, Nano Banana 2, Nano Banana Pro, Imagen) in the Gemini app, Google AI Studio, the Gemini API, Google Flow and Gemini CLI. Covers the reference-image formula, edit prompts, aspect and size settings, text rendering, backgrounds, model choice and where to put locks. Use for any Gemini image generation or editing request, "nano banana" prompts, or when moving a prompt pack into Gemini.
---

# Gemini Image Prompting

> Model names, limits and features change often. The facts below were checked against Google's published prompting guidance and current guides in October 2026; verify limits in the official docs for your model before relying on them.

## Models (working picture)
| Name | Underlying model | Use |
|---|---|---|
| Nano Banana | Gemini 2.5 Flash Image | Quick drafts, simple generation |
| Nano Banana 2 | Gemini 3.1 Flash Image | Default in the Gemini app since Feb 2026; fast; strong character consistency; many reference images |
| Nano Banana Pro | Gemini 3 Pro Image | Specialist, complex scenes and precise text |
| Imagen | Imagen family | Text-to-image; check its reference-image support |

Pick the model in the surface you use; record it in the bible's "Model notes".

## Prompting rules that work on Gemini
1. **Describe, do not list.** Clear sentences under stable labels beat keyword piles.
2. **Reference formula:** `[reference images] + [relationship instruction] + [new scenario]`. Example relationship: "Image 1 is the character identity; image 2 is the style and palette. Keep identity from image 1 and rendering from image 2."
3. **References:** current guides state Nano Banana 2 accepts up to 14 reference images per request. More references are not always better; start with 2-4 purposeful ones (character sheet, style anchor, layout anchor).
4. **One change per edit.** "Using the provided image, change only X. Keep everything else exactly the same."
5. **Name framing and view** in words: close-up, wide shot, full body, slight three-quarter top-down.
6. **Aspect ratio and size:** set them in the UI/API when offered and repeat the ratio in the prompt. Newer models offer sizes from about 0.5K up to 4K; use a larger size for sheets, then downscale in post.
7. **Text in images:** newer models render text much better, but keep it short; for game assets prefer no text and add text in code.
8. **Backgrounds:** ask for a flat uniform key color (#FF00FF) and remove it in post; do not rely on true transparency.
9. **Hex codes are approximate:** pair names + hex + ratio.
10. **Each request is independent:** repeat the lock block and attach the anchors every time.
11. **Grounding / web search** (where enabled) pulls real-world information; useful for real places and products, risky for invented worlds.

## Where the lock goes
| Surface | Put it |
|---|---|
| Gemini app chat | Paste the two-part prompt each time; attach anchors |
| Gem | Global rules in the Gem instructions (`plug-and-play/GEM-INSTRUCTIONS.md`); per-asset prompt in chat |
| AI Studio | System instruction = global rules; user turn = per-asset prompt + images |
| Gemini API | `system_instruction` = global rules; `contents` = images then prompt (`plug-and-play/batch_generate.py`) |
| Google Flow | Instruction slots from `instruction-slot-packager` (`plug-and-play/FLOW-3-SLOTS.md`) |
| Gemini CLI | Skills in `.gemini/skills/` plus the `GEMINI.md` context file |

## Prompt skeletons
```
LOCK STYLE & THEME:
<lock block>

ASSET GENERATION PROMPT:
Create one <asset type>. <Subject lock>. <Composition and camera>. <Background rule>.
Keep <invariants> identical to the reference. Output one image only, with no text.
```
```
Image 1 is the character identity reference. Image 2 is the style reference.
Keep the face, outfit, colors, proportions and line weight from image 1 and the rendering from image 2.
New scene: <scenario>. <Camera lock>. <Background rule>. Output one image only.
```

## Process
1. Take the Prompt Pack from `master-prompt-builder`.
2. Set model, aspect ratio and size; attach anchors.
3. Run 3 probes; compare with the anchors using `consistency-qa-reviewer`.
4. Record wording that worked and any failure in "Model notes".

## Pitfalls
- Very long prompts that bury the key rule at the end; put the most important rules early.
- Asking for transparency, exact pixel counts and rendered text in one prompt.
- Assuming every surface offers every feature; check the surface you use.
- Treating a "pretty good" output as the reference; approve anchors deliberately.
