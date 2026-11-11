---
name: aseprite-reference-to-sprite
description: Converts image references and visual briefs into a practical pixel-art construction plan and editable Aseprite asset workflow. Use when the user supplies a photo, concept art, screenshot, or visual brief and wants it reduced into a readable pixel-art sprite at a target resolution.
---

# Reference-to-Sprite Pipeline

## Goal
Translate a reference into a coherent pixel-art asset while respecting the target resolution and style. A reference image is not automatically an editable sprite, animation, or layered Aseprite document.

## Analyze the reference
Extract:
- main silhouette and pose
- proportions and landmarks
- camera angle / perspective
- dominant colors and value groups
- light direction
- materials and distinguishing details
- negative space
- features that must remain recognizable at low resolution

Separate essential identity cues from details that should be simplified.

## Reduce to target resolution
1. Confirm target dimensions.
2. Simplify large forms before small details.
3. Prioritize silhouette and value hierarchy.
4. Limit colors to the requested palette or an agreed compact palette.
5. Convert smooth gradients into deliberate pixel clusters.
6. Replace tiny details that disappear at native size with a readable shape cue.
7. Avoid blindly tracing anti-aliased edges from a high-resolution reference.

## Construct in passes
- pass 1: silhouette
- pass 2: large value/color masses
- pass 3: anatomy and identifying features
- pass 4: shadows and highlights
- pass 5: cluster cleanup
- pass 6: comparison and QA

## For animation references
- Identify stable landmarks and pivot.
- Distinguish pose changes from camera changes.
- Build key poses first.
- Preserve costume, palette, proportions, and handedness.
- Do not infer unseen frames as facts; label invented in-betweens as design choices.

## If an image-generation model is used
Treat the result as a reference unless the tool genuinely produces the required editable pixel grid and animation structure. Inspect for off-grid artifacts, inconsistent pixel scale, anti-aliasing, and impossible details. Rebuild or clean it in Aseprite using confirmed tools.

## Comparison report
Describe what was preserved, what was simplified, what was changed to fit the pixel grid, and any uncertain interpretation.
