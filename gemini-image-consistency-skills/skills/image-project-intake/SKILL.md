---
name: image-project-intake
description: Captures the project brief before any image generation - purpose, audience, subject, deliverables, platform, aspect ratios, constraints, existing references. Use at the start of any image-set, brand visual, game art, illustration series or "make me consistent images" request, and whenever the user gives a vague visual goal that needs to be pinned down. Produces PROJECT_BRIEF with explicit assumptions. Written for Gemini image generation (Nano Banana family, Imagen) in the Gemini app, AI Studio, API, Google Flow and Gemini CLI.
---

# Image Project Intake

## Purpose
Turn a vague visual wish into a brief that the locking skills can use. Ask little, assume sensibly, record assumptions.

## When to use
First step of any consistency project, or when the goal is unclear.

## The six core questions (ask in ONE message)
1. **What is it for?** Game, app UI, book, social media, product, brand, presentation, print.
2. **What is shown?** Main subjects (characters, objects, places) and rough count of images.
3. **What should it feel like?** Three mood words or a reference (describe attributes, not artist names).
4. **Where will it be used?** Platform and final size or aspect ratio; transparent background needed?
5. **What already exists?** Logos, palettes, character art, screenshots, a previous style.
6. **What must never appear?** Forbidden content, colors, symbols, cultural or brand constraints.

## Defaults when the user does not know
| Missing | Default | Mark as |
|---|---|---|
| Aspect ratio | 1:1 for icons, 16:9 for scenes, 9:16 for mobile-first | [assumed] |
| Medium | Clean stylized illustration | [assumed] |
| Background | Plain neutral or flat key color for assets | [assumed] |
| Count | 10-20 images | [assumed] |
| Text in images | None; add text in post | [assumed] |

## Process
1. Read everything the user already provided (messages, files, screenshots). Extract answers first.
2. Ask only for what is still missing, in one batch.
3. Fill `templates/PROJECT_BRIEF.md`.
4. List assumptions at the top and ask for a quick yes/no.
5. Hand off to `visual-style-lock`.

## Output: PROJECT_BRIEF
```
PROJECT: <name>
PURPOSE: <one sentence>
AUDIENCE / MOOD: <words>
DELIVERABLES: <asset types x counts>
FORMAT: <aspect ratios, final px sizes, background needs>
EXISTING MATERIAL: <list or none>
FORBIDDEN: <list>
LANGUAGE: <prompt language, UI language>
ASSUMPTIONS: <list marked [assumed]>
```

## Pitfalls
- Asking 15 questions. Six is the ceiling.
- Accepting "make it cool". Convert to attributes (line weight, saturation, lighting).
- Skipping the forbidden list; it prevents most later rework.

## Gemini notes
- Ask which surface and model will be used (Gemini app, AI Studio, API, Google Flow; Nano Banana, Nano Banana 2, Nano Banana Pro or Imagen). Reference-image limits, output sizes and aspect options differ per model; record the answer in the bible.
- Ask whether the user can attach images in the chosen surface.
