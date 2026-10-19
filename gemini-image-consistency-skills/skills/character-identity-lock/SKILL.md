---
name: character-identity-lock
description: Creates character cards and a reusable Design Lock sentence so the same character stays recognizable across poses, angles, expressions, outfits and scenes. Use when a character keeps changing between generations, when building a cast, mascot, game hero or comic character, or when the user says "keep the same character", "character sheet", "turnaround", "consistent face/outfit". Written for Gemini image generation (Nano Banana family, Imagen) in the Gemini app, AI Studio, API, Google Flow and Gemini CLI.
---

# Character Identity Lock

## Purpose
Make a character reproducible. Identity is carried by a fixed written card plus one approved anchor image.

## Character card (fill every field)
| Field | Content |
|---|---|
| Name and role | Who they are in the story |
| Proportions | Head-to-body ratio, build, relative height vs other cast |
| Signature features | **Three** unmistakable traits (e.g. gold hairband bun, ruffled blouse hem, diamond-pattern sarong) |
| Face | Eye shape/color, brows, nose, mouth style, skin ramp (3 hex) |
| Hair | Style, length, color hex, accessories |
| Outfit | Each garment with color hex and pattern; footwear |
| Props | Items always or sometimes held |
| Invariants | Things that never change |
| Variables | Things allowed to change (pose, expression, props, outfit variant) |
| Size in game or layout | e.g. 26 px tall in a 32 px cell |

## Design Lock sentence
Compress the card into one sentence of 40-70 words that starts with the name and ends with the outline rule. Reuse it **verbatim** in every prompt containing that character.

Example:
`DESIGN LOCK: Timun Mas, a brave young Javanese village girl, chibi proportions, warm medium-brown skin, small dark eyes, black hair in a high round bun with a thin muted-gold hairband, cream kebaya-style blouse with ruffled hem, muted-gold sash, brown batik sarong with a diamond lattice to mid-shin, bare feet; 1 px dark-brown outline.`

## Process
1. Build the card from the brief; do not invent traits the user did not give (mark `[assumed]`).
2. Generate a **reference turnaround**: front, side, back (and 3/4 if needed) on a neutral or key-color background, same scale, one row.
3. Choose and approve one anchor image. Record file name and version.
4. For expressions and poses, always attach the anchor and repeat the Design Lock sentence.
5. Create outfit or age variants as **separate cards** that inherit the base card and list only the differences.
6. For a cast, ensure each member differs in at least two of: silhouette, dominant color, size, headwear.

## Output
- `CHARACTER_CARD` per character (use `templates/CHARACTER_CARD.md`)
- Design Lock sentence
- Turnaround prompt and anchor file note

## Rules
- Do not describe a character with a real person's name or a copyrighted character; describe attributes.
- Hands, feet and small accessories drift most; simplify them in the design if they keep failing.
- Left and right views: if the design is symmetric, generate one side and mirror it in post.

## Pitfalls
- Describing mood instead of features ("brave, kind"). Models need visible traits.
- Three variants of the Design Lock sentence floating around. Keep one canonical copy in the bible.
- Changing hairstyle or outfit color "just a bit" to fix one image; edit the image instead (see `reference-image-workflow`).

## Gemini notes
- Build a **character sheet first** (front, side, back, key expressions) and attach it to every later request. Google's own consistent-imagery lab follows this pattern: extract the character into a reference image, then generate new scenes from prompt + reference.
- Nano Banana 2 accepts many references per request (up to 14 per current guides; verify for your model). Attach the character sheet plus one style anchor, not everything you have.
