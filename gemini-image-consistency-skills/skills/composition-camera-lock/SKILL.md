---
name: composition-camera-lock
description: Locks camera angle, perspective, lens feel, framing, aspect ratio, horizon, lighting direction and depth layering so a set of images shares the same viewpoint. Use when perspective or framing varies across generations, for top-down game art, product shots, comic panels, storyboards, or when the user says "same angle", "same camera", "consistent framing", "shot list". Written for Gemini image generation (Nano Banana family, Imagen) in the Gemini app, AI Studio, API, Google Flow and Gemini CLI.
---

# Composition & Camera Lock

## Purpose
Remove viewpoint randomness. Camera is part of the style, so it is also repeated verbatim.

## Camera dimensions
| Dimension | Options |
|---|---|
| Viewpoint | top-down, slight 3/4 top-down, eye-level, low angle, isometric, side view |
| Lens feel | wide, 35 mm, 50 mm, telephoto compression (for photo/3D styles) |
| Framing | full body, waist-up, close-up, establishing wide, object-centered |
| Aspect ratio | 1:1, 4:3, 3:2, 16:9, 9:16 (name the use) |
| Subject placement | centered, rule of thirds, with padding of X% |
| Horizon / ground plane | high, middle, none (flat) |
| Depth layers | foreground / midground / background roles |
| Light | direction, softness, key/fill ratio |
| Background | plain, flat key color, scene |

## Camera lock sentence
Write one sentence per deliverable type:
- Character sprite: `Consistent slight three-quarter top-down view, full body centered, feet on a shared baseline, 20% padding.`
- Environment: `Slight three-quarter top-down view, horizon not visible, light from the top-left.`
- Key art: `Wide 16:9 establishing shot, eye-level, layered foreground, midground, background.`

## Process
1. Pick the viewpoint per deliverable type (one per type, not per image).
2. Set aspect ratios from the brief; state them in the prompt **and** in the tool's aspect setting when available.
3. Write the camera lock sentence and place it right after the style lock in prompts.
4. For series (storyboard, comic, product line) create a **shot list**: ID, framing, subject, action, light.
5. Test with two probes from different subjects; viewpoints must match.

## Shot list template
```
ID | Framing | Subject | Action | Light | Aspect
S01 | wide | hero at gate | arriving | morning, from left | 16:9
```

## Pitfalls
- Asking for "dynamic angles" in a project that needs a fixed view.
- Mixing top-down characters with side-view backgrounds.
- Leaving padding unspecified; sprites then touch the canvas edge.

## Gemini notes
- Set the aspect ratio in the UI or API **and** name it in the prompt. Name the framing in plain words (close-up, wide shot, full body) and the viewpoint (slight three-quarter top-down).
