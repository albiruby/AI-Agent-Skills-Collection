# Copy-ready Gemini prompt templates

Replace `{{...}}`. Paste the project's LOCK block where `{{LOCK}}` appears. Attach anchor images where noted.

## 1. Text-to-image (single asset)
```text
LOCK STYLE & THEME:
{{LOCK}}

ASSET GENERATION PROMPT:
Create ONE {{asset type}}. {{subject lock}}. {{composition and camera sentence}}.
Use a perfectly flat uniform {{key color}} background edge to edge. Output one image only. No text.
```

## 2. Generate with references (identity + style)
Attach: character sheet (image 1), style anchor (image 2).
```text
Image 1 is the character identity reference. Image 2 is the style and palette reference.
Keep the face, outfit, colors, proportions and line weight from image 1 and the rendering, outline and palette from image 2.

LOCK STYLE & THEME:
{{LOCK}}

New scene: {{scenario}}. {{camera sentence}}. Output one image only. No text.
```

## 3. Character sheet (turnaround)
```text
LOCK STYLE & THEME:
{{LOCK}}

Create ONE character reference sheet of the character below on a flat uniform {{key color}} background:
front view, side view (facing right) and back view in ONE horizontal row, same scale, same baseline, equal spacing, nothing overlapping.
{{DESIGN LOCK sentence}}
Output one image only. No text, labels or grid lines.
```

## 4. Minimal edit
Attach: the image to change.
```text
Using the provided image, change only {{X}}. Keep the character's face, outfit, colors, proportions, line weight and the background exactly the same. Do not add new objects. Output one image only.
```

## 5. Style transfer
Attach: style anchor.
```text
Match the rendering, outline, palette and shading of the provided style reference exactly. Do not copy its subject.
{{LOCK}}
Draw: {{subject}}. Output one image only. No text.
```

## 6. Sprite sheet
Attach: character sheet.
```text
LOCK STYLE & THEME:
{{LOCK}}

ASSET GENERATION PROMPT:
Create ONE sprite sheet: exactly {{N}} frames in ONE horizontal row, left to right in time order, on a 16:9 landscape canvas. Each frame sits in its own SQUARE cell whose side equals the canvas width divided by {{N}}; the row is centered vertically with flat {{key color}} above and below. The character uses at most 65% of its cell width and about 80% of its cell height with at least 15% empty space on each side. Same scale and camera in every frame; head-top and feet baseline fixed. No labels, numbers, grid lines or overlap.
{{DESIGN LOCK sentence}}
ANIMATION: {{animation}}. FACING: {{direction}}. FRAME ACTIONS: {{frame-by-frame}}.
Output one image only.
```

## 7. Tile / prop atlas
```text
LOCK STYLE & THEME:
{{LOCK}}

ASSET GENERATION PROMPT:
Create ONE atlas of {{count}} {{tiles/props}} on a strict orthogonal grid, {{columns}} columns by {{rows}} rows, equal cells, clear gaps, nothing overlapping, on a flat uniform {{key color}} background. Tiles are seamless on all edges and have no outline; props have a 1 px outline and a clear ground-contact base. Items: {{list}}. Output one image only. No text.
```

## 8. Icon / item
```text
LOCK STYLE & THEME:
{{LOCK}}

ASSET GENERATION PROMPT:
Create ONE item icon: {{item}}, one centered object with a bold simple silhouette that stays readable at 24 px, no slot frame, on a flat uniform {{key color}} background. Output one image only. No text.
```

## 9. Key art / background (no key color)
```text
LOCK STYLE & THEME:
{{LOCK}}

ASSET GENERATION PROMPT:
Create ONE full-frame {{aspect}} illustration, edge to edge, with clear foreground, midground and background layers: {{scene}}. No UI, no text, no logo. Output one image only.
```

## 10. QA review (use in a text chat; attach anchor + outputs)
```text
You are a strict consistency reviewer. Compare the attached output image(s) with the anchor image and this lock:
{{LOCK}}
Score each 0-2: style, palette, identity, proportion/scale, camera, theme, technical cleanliness, text/extra objects, format. Total /18.
Verdict: PASS (>=16 and no zero), FIX (12-15), REGENERATE (<12).
List concrete differences and the smallest fix for each. Do not praise.
```

## 11. Drift fix
Attach: anchor + the drifted output.
```text
The attached output drifted from the anchor in: {{what changed}}. Using the anchor as the only source of truth, redraw the output with only {{what to fix}} corrected. Keep composition, pose and everything else identical. Output one image only.
```
