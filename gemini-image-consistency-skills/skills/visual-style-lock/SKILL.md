---
name: visual-style-lock
description: Defines and freezes the visual style of an image project as a reusable Style Lock Block - medium, rendering, outline, shading, light direction, texture, detail density, proportions, perspective, resolution. Use whenever images must share one look, when the user says "lock the style", "same art style", "consistent look", or when Gemini outputs keep drifting in rendering style. Written for Gemini image generation (Nano Banana family, Imagen) in the Gemini app, AI Studio, API, Google Flow and Gemini CLI.
---

# Visual Style Lock

## Purpose
Describe the look in attributes precise enough that every prompt can repeat it verbatim. Produces a Style Lock Block of at most about 120 words.

## Style dimensions (decide each one)
| Dimension | Decide | Example values |
|---|---|---|
| Medium | What it imitates | pixel art, flat vector, cel-shaded 3D, gouache, watercolor, ink + color, isometric low-poly |
| Rendering | How surfaces look | flat color clusters, soft painterly, hard-edged, textured paper |
| Outline | Weight and color | 1 px dark-brown outline, no outline, thick uniform black |
| Shading | Model | 3 tones per material, cel shadow, ambient occlusion only |
| Light | Direction and color | from top-left, warm key, cool fill |
| Texture | Amount | none, subtle grain, visible brush |
| Detail density | Level | minimal, medium, rich; "readable at 64 px" |
| Proportions | Anatomy | chibi (head 38% of height), realistic, long-limbed |
| Perspective | Camera | top-down, 3/4 top-down, side view, isometric |
| Resolution logic | Grid | 16x16 tiles, 320x180 internal, crisp square pixels |
| Exclusions | What is banned | gradients, glow, 3D render look, photorealism, anti-aliasing |

Describe by **attributes**, not by living artists' names or copyrighted franchises. Say "handcrafted 16-bit era pixel art", not a game title.

## Process
1. Take the brief; pick one value per dimension (ask the user only when it changes the result a lot).
2. Write the Style Lock Block, one labeled line per dimension, in this order: STYLE, OUTLINE, SHADING, LIGHT, SCALE, EXCLUSIONS.
3. Run the **probe test**: generate 3 images (a simple object, a character, a scene) with only the block plus a one-line subject.
4. Compare with `consistency-qa-reviewer`. If rendering differs, tighten the weakest line (see below) and rerun.
5. Freeze as `STYLE LOCK v1.0` in the bible.

## Tightening weak lines
| Symptom | Fix |
|---|---|
| Outline appears and disappears | State weight, color and "around every sprite" |
| Gradients sneak in | Put "flat color clusters, no gradients" in both STYLE and EXCLUSIONS |
| Looks 3D/glossy | Add "matte, hand-drawn look, no render shine" |
| Detail level jumps | Add a size anchor: "must read at 64 px" |
| Perspective wanders | Move to `composition-camera-lock` and repeat the camera sentence |

## Output format
```
LOCK STYLE:
STYLE: <medium + rendering + proportions>
OUTLINE: <...>
SHADING: <...>
LIGHT: <...>
SCALE: <...>
EXCLUSIONS: <...>
```

## Rules
- Positive wording first, exclusions second. Keep each line under 30 words.
- Never rewrite the block per image. Only subject and action change.
- If the user supplies a reference image, derive the block from what is visible, then confirm.

## Gemini notes
- Gemini image models respond well to descriptive scene language. If the labeled lines (`STYLE:`, `OUTLINE:`) are partly ignored in probe tests, rewrite the same content as one short descriptive paragraph and re-test.
- Use a neutral object as the style anchor so the model copies the rendering, not the subject.
