---
name: color-palette-lock
description: Builds and locks a project color palette with hex codes, roles, ramps, lighting temperature and a reserved chroma-key color, and explains how to phrase it so image models respect it. Use when colors drift between generated images, when the user wants a brand or game palette, "lock the colors", or when assets need a removable background color. Written for Gemini image generation (Nano Banana family, Imagen) in the Gemini app, AI Studio, API, Google Flow and Gemini CLI.
---

# Color Palette Lock

## Purpose
Keep every image inside one controlled color world. Models only approximate hex codes, so the palette is stated three ways: names, hex values and ratios.

## Palette structure
| Part | Count | Notes |
|---|---|---|
| Dominant | 2-3 colors | about 60% of the image area |
| Secondary | 2-3 colors | about 30% |
| Accent | 1-2 colors | about 10%, used sparingly |
| Neutrals | 2 | outline color (never pure black unless chosen), paper/cream |
| Ramps | per material | shadow / base / highlight for skin, cloth, foliage, wood, stone |
| Reserved | 1 | chroma-key color for removable backgrounds, e.g. #FF00FF, never used in artwork |

## Process
1. Start from theme and mood: pick the dominant hue family first.
2. Choose 8-16 colors; give each a **name, hex and role** (e.g. "moss green #2F5E3A - foliage shadow").
3. Build 3-tone ramps for the 3-5 most common materials.
4. Set lighting temperature: key color (warm/cool) and shadow tint.
5. Write the palette line for prompts: names plus hex, plus "use only these colors, plus restrained accents".
6. Verify on probe images with an eyedropper or the QA skill; adjust wording, not the palette, unless the palette is wrong.

## Inclusive skin tones
Define a skin ramp for each recurring character explicitly (3 hex values). Do not rely on words like "tan" alone.

## Output format
```
PALETTE (use only these, plus restrained accents):
<group> <hex> <hex> <hex>; <group> <hex> ...
ACCENTS: <names + hex>, sparingly
RESERVED: <key color> never appears in artwork
LIGHT COLOR: <warm key / cool shadow>
```

## Tips for models
- Say each color in words too ("deep forest green #1F3D2B").
- Repeat the full line in every prompt; do not shorten to "earthy colors".
- If saturation creeps up, add "muted, low-saturation" to the line and name a forbidden hue ("no neon, no pure saturated primaries").
- Pure black and pure white attract artifacts; use a dark warm brown and a cream.

## Pitfalls
- More than 16 colors: the model stops respecting any of them.
- Reusing the chroma-key color inside the art.
- Changing the palette after assets exist without a version bump.

## Gemini notes
- Gemini treats hex codes as approximate guidance. State name + hex + ratio, then confirm with an eyedropper and snap colors in post.
- If saturation rises, add "muted, low-saturation" and name the forbidden hue.
