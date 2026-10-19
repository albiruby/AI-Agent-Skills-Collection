# Google Flow — Timun Mas Sprite-Sheet & Game Asset Prompt Pack

**Project:** Timun Mas: 2D Pixel Art Adventure  
**Platform:** Desktop browser (Phaser 3 + TypeScript + Vite)  
**Visual target:** top-down retro pixel art, internal resolution 320×180, 16×16 world tiles  
**Prompt principle:** one prompt generates one image; for animated characters, that image contains a complete, ordered sprite sheet for one action and one facing direction.

## How to use this document

0. Fill the 3 Flow instruction slots first (see "Google Flow instruction slots"). Keep them enabled for every generation.
1. Copy **one prompt only** into Google Flow per generation. Every prompt is in two parts: `LOCK STYLE & THEME` first, then `ASSET GENERATION PROMPT`.
2. For every character, generate the reference/idle sheet first. Reuse the approved reference image for every later sheet if image references are supported.
3. **One animation + one facing direction = one image.** Example: `Timun Mas / Walk / Facing Down` is one sprite sheet containing 6 separate frames. `Walk / Facing Up` is a different image. `Run / Facing Down` is another image.
4. Each frame must be a separate, evenly spaced square cell in a single horizontal row, in chronological order from left to right. Set Flow to 16:9 landscape: the sheet appears as a horizontal band in the middle of the image with magenta above and below, so crop it afterwards. No overlapping frames, no perspective changes, no labels, no contact sheet layouts.
5. Image generators may not return exact dimensions or perfectly uniform cells. Inspect the output, crop frames, and standardize them in Aseprite/LibreSprite before importing into Phaser.
6. Magenta background is requested for manual removal if transparency is not supported. Remove it carefully, then export PNG with alpha. Full-screen illustrations (BG-xx, PRES-xx) have no magenta.
7. Optional shortcut: if the design is symmetric, generate the right-facing sheets and mirror them horizontally for left. Only keep separate left prompts if the mirrored result looks wrong.
8. Environment/prop atlases are intentional multi-asset images; crop each grid cell or prop into separate files.
9. Never ask Flow to render UI text. Add dialogue, labels, buttons, numbers, and counters in code.

## Google Flow instruction slots (3 slots)

Google Flow offers 3 instruction slots. Fill all three once and keep them enabled for every generation. Slot 1 is the global rules; slots 2 and 3 split the rest by asset type, so Flow never has to guess. Each prompt below also repeats its own LOCK STYLE & THEME, so it stays consistent even if a slot is switched off.

| Slot | Name | Covers |
|---|---|---|
| 1 | Global rules | Theme, style, outline, shading, palette, scale, pixel rules, background, output |
| 2 | Character & sprite sheet canon | Fixed designs of Timun Mas, Buto Ijo, Mbok Srini, NPC; sheet geometry; frame consistency |
| 3 | World, item, VFX & UI canon | Tiles, props, items, projectiles, VFX, UI, backgrounds; reject rules |

### Slot 1 - Global rules

```text
GLOBAL RULES - TIMUN MAS: 2D PIXEL ART ADVENTURE
These rules apply to every generation. If a prompt is unclear, choose the simpler, flatter, more consistent option.

THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.
BACKGROUND: perfectly flat solid magenta (#FF00FF), uniform edge to edge (no vignette, gradient, floor or shadow), for sprites, props, tiles, items, VFX and UI. Full-screen illustrations fill the 16:9 frame edge to edge with no magenta.
OUTPUT: one image per generation. Environment/prop atlases are the only multi-asset images, arranged on a strict orthogonal grid with no overlaps. Never render UI text; dialogue, labels, buttons and counters are added in code.
```

### Slot 2 - Character & sprite sheet canon

```text
CHARACTER & SPRITE SHEET CANON - TIMUN MAS
Applies to every character sprite sheet. Always match the approved reference image; never redesign.

PEOPLE: chibi proportions (head about 38% of body height, small hands), 1 px dark-brown outline (#2A1B14), same shading rules as the global rules, bare feet.
TIMUN MAS (32 px cell, about 26 px tall): young Javanese village girl, warm medium-brown skin, small dark eyes, black hair in a high round bun with a thin muted-gold hairband, cream kebaya-style blouse with ruffled hem and short sleeves, muted-gold sash, brown batik sarong with a small diamond lattice pattern to mid-shin.
BUTO IJO (64 px cell, about 56 px tall): huge ogre, about twice Timun Mas's height, broad hunched shoulders, barrel chest, forest-green skin, heavy brow, small cream tusks, wild dark-brown hair, dark-brown waist cloth with rope belt. Scary but family-friendly.
MBOK SRINI (32 px cell, about 27 px tall): kind middle-aged village woman, dark hair in a low bun under a brown head cloth, cream kebaya-style blouse, brown batik sarong, muted forest-green shawl over one shoulder.
VILLAGE NPC (32 px cell, about 26 px tall): adult villager in cream and earthy-brown rural clothing, silhouette clearly different from the main cast.

FACING: down = front view; up = back view; left / right = true side profile. Never mix views inside one sheet.
SHEET GEOMETRY: ONE horizontal row of SQUARE cells on a 16:9 canvas; cell side = canvas width / frame count; row centered vertically; flat magenta above and below. One frame centered per cell; the character uses at most 65% of the cell width and about 80% of its height; at least 15% empty gap on each side; frames never touch, overlap or get cropped. Use exactly the frame count the prompt states.
ACROSS FRAMES AND SHEETS: identical scale, outfit, hair, colors and line weight. Head-top height and the feet baseline stay fixed (body bob 1 px at most). Only limbs, torso and small details move. Walk and run = clear leg and arm swing with the same stride length in every cycle.
NEVER: extra limbs, a changed hairstyle, new accessories, different outfit colors, a different character size from one sheet to the next.
```

### Slot 3 - World, item, VFX & UI canon

```text
WORLD, ITEM, VFX & UI CANON - TIMUN MAS
Applies to every non-character asset. Same style lock as the global rules.

GROUND TILES: 16x16, orthogonal, seamless edges, no outline, no baked shadows. Atlas on a strict grid, equal spacing, one tile per cell, nothing overlapping.
PROPS, BUILDINGS, TREES, OBSTACLES: top-down / slight three-quarter view, 1 px dark-brown outline, base on a clear ground-contact line, no cast shadow. In an atlas each object is separate with a clear magenta gap.
ITEMS: icon readable at 16x16 or 24x24; one centered object, bold simple silhouette, no frame or slot. World pickup = the same item, slightly smaller, with at most one tiny pale-gold sparkle.
PROJECTILES AND VFX: compact bold shapes, hard pixel clusters, project palette plus the water-blue and muted-red accents only; no glow or soft gradients; transparent-ready on flat magenta.
UI: nine-slice friendly frames, dark warm-brown interior, cream inner edge, muted-gold and wood-brown border; centers stay empty; no text, numbers or icons unless the prompt says so.
BACKGROUNDS AND KEY ART: full 16:9 edge to edge, no magenta, clear foreground / midground / background layers, same palette and line language as the game assets, no UI, no text, no logo.
STANDALONE BACKGROUND: perfectly flat #FF00FF, uniform, with no vignette, floor or shadow.
REJECT AND REGENERATE IF: any text or letters appear, edges are blurry or antialiased, gradients show up, extra objects or characters appear, the subject is cropped, the perspective changes, or the palette drifts toward saturated neon colors.
```

## Recommended generation order

1. Timun Mas idle facing down; Buto Ijo idle facing down; Mbok Srini idle facing down.
2. Remaining idle directions, then walk/run sheets per direction.
3. Action/reaction sheets, then environment, items, VFX, and UI assets.
4. Test frame cropping and playback in Phaser before generating optional assets.

## Character sprite-sheet prompt template

Every character prompt below specifies frame count and action. Keep the character design consistent with the approved reference image. If Flow cannot reliably produce pixel-perfect sprite sheets, generate the sheet as a visual guide and manually clean/crop it in Aseprite/LibreSprite.

### TM-IDLE-DOWN — Timun Mas — idle facing down

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE production-oriented SPRITE SHEET image for an original 2D top-down adventure game inspired by Indonesian folklore. Use a perfectly flat solid magenta (#FF00FF) background for manual removal, uniform edge to edge with no vignette, gradient or floor. Keep the entire sprite visible in every frame, with no cropping and no cast shadow.

SPRITE SHEET LAYOUT: exactly 4 frames in ONE horizontal row, ordered chronologically from left to right, on a 16:9 landscape canvas. Each frame sits in its own SQUARE cell (final cleaned size 32×32 px) whose side equals the canvas width divided by 4; the row is centered vertically and the empty space above and below is flat magenta. Center one frame in each cell. The character occupies at most 65% of its cell's width and about 80% of its cell's height, leaving at least 15% empty magenta on each side, so frames never touch, overlap, or get cropped by a neighbor or the image edge. Same character scale, camera angle and proportions in every frame; head-top and feet stay at the same vertical positions in every frame, with the feet/base on one shared baseline. Do not add labels, numbers, grid lines, frame borders, duplicate rows, extra poses, or decorative elements. The sheet must be easy to slice into 4 equal cells.

CHARACTER: Timun Mas. DESIGN LOCK: Timun Mas, a brave young Javanese village girl, chibi proportions (head about 38% of body height, about 26 px tall in a 32 px cell), warm medium-brown skin, small dark eyes, black hair in a high round bun on top of the head with a thin muted-gold hairband, cream kebaya-style blouse with a ruffled hem and short sleeves, muted-gold sash at the waist, brown batik sarong with a small diamond lattice pattern reaching mid-shin, bare feet; 1 px dark-brown outline.
ANIMATION: idle breathing loop. FACING DIRECTION: down. FRAME-BY-FRAME ACTION: Frame 1 neutral standing; frame 2 subtle breathing/shoulder lift; frame 3 slight return/soft blink if face is visible; frame 4 return to the same neutral pose for a seamless loop. Preserve silhouette, outfit, colors, hair and accessories across all frames. The change between frames should be small and readable at native pixel scale. Output one sprite-sheet image only.
```

### TM-IDLE-UP — Timun Mas — idle facing up

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE production-oriented SPRITE SHEET image for an original 2D top-down adventure game inspired by Indonesian folklore. Use a perfectly flat solid magenta (#FF00FF) background for manual removal, uniform edge to edge with no vignette, gradient or floor. Keep the entire sprite visible in every frame, with no cropping and no cast shadow.

SPRITE SHEET LAYOUT: exactly 4 frames in ONE horizontal row, ordered chronologically from left to right, on a 16:9 landscape canvas. Each frame sits in its own SQUARE cell (final cleaned size 32×32 px) whose side equals the canvas width divided by 4; the row is centered vertically and the empty space above and below is flat magenta. Center one frame in each cell. The character occupies at most 65% of its cell's width and about 80% of its cell's height, leaving at least 15% empty magenta on each side, so frames never touch, overlap, or get cropped by a neighbor or the image edge. Same character scale, camera angle and proportions in every frame; head-top and feet stay at the same vertical positions in every frame, with the feet/base on one shared baseline. Do not add labels, numbers, grid lines, frame borders, duplicate rows, extra poses, or decorative elements. The sheet must be easy to slice into 4 equal cells.

CHARACTER: Timun Mas. DESIGN LOCK: Timun Mas, a brave young Javanese village girl, chibi proportions (head about 38% of body height, about 26 px tall in a 32 px cell), warm medium-brown skin, small dark eyes, black hair in a high round bun on top of the head with a thin muted-gold hairband, cream kebaya-style blouse with a ruffled hem and short sleeves, muted-gold sash at the waist, brown batik sarong with a small diamond lattice pattern reaching mid-shin, bare feet; 1 px dark-brown outline.
ANIMATION: idle breathing loop. FACING DIRECTION: up. FRAME-BY-FRAME ACTION: Frame 1 neutral standing; frame 2 subtle breathing/shoulder lift; frame 3 slight return/soft blink if face is visible; frame 4 return to the same neutral pose for a seamless loop. Preserve silhouette, outfit, colors, hair and accessories across all frames. The change between frames should be small and readable at native pixel scale. Output one sprite-sheet image only.
```

### TM-IDLE-LEFT — Timun Mas — idle facing left

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE production-oriented SPRITE SHEET image for an original 2D top-down adventure game inspired by Indonesian folklore. Use a perfectly flat solid magenta (#FF00FF) background for manual removal, uniform edge to edge with no vignette, gradient or floor. Keep the entire sprite visible in every frame, with no cropping and no cast shadow.

SPRITE SHEET LAYOUT: exactly 4 frames in ONE horizontal row, ordered chronologically from left to right, on a 16:9 landscape canvas. Each frame sits in its own SQUARE cell (final cleaned size 32×32 px) whose side equals the canvas width divided by 4; the row is centered vertically and the empty space above and below is flat magenta. Center one frame in each cell. The character occupies at most 65% of its cell's width and about 80% of its cell's height, leaving at least 15% empty magenta on each side, so frames never touch, overlap, or get cropped by a neighbor or the image edge. Same character scale, camera angle and proportions in every frame; head-top and feet stay at the same vertical positions in every frame, with the feet/base on one shared baseline. Do not add labels, numbers, grid lines, frame borders, duplicate rows, extra poses, or decorative elements. The sheet must be easy to slice into 4 equal cells.

CHARACTER: Timun Mas. DESIGN LOCK: Timun Mas, a brave young Javanese village girl, chibi proportions (head about 38% of body height, about 26 px tall in a 32 px cell), warm medium-brown skin, small dark eyes, black hair in a high round bun on top of the head with a thin muted-gold hairband, cream kebaya-style blouse with a ruffled hem and short sleeves, muted-gold sash at the waist, brown batik sarong with a small diamond lattice pattern reaching mid-shin, bare feet; 1 px dark-brown outline.
ANIMATION: idle breathing loop. FACING DIRECTION: left. FRAME-BY-FRAME ACTION: Frame 1 neutral standing; frame 2 subtle breathing/shoulder lift; frame 3 slight return/soft blink if face is visible; frame 4 return to the same neutral pose for a seamless loop. Preserve silhouette, outfit, colors, hair and accessories across all frames. The change between frames should be small and readable at native pixel scale. Output one sprite-sheet image only.
```

### TM-IDLE-RIGHT — Timun Mas — idle facing right

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE production-oriented SPRITE SHEET image for an original 2D top-down adventure game inspired by Indonesian folklore. Use a perfectly flat solid magenta (#FF00FF) background for manual removal, uniform edge to edge with no vignette, gradient or floor. Keep the entire sprite visible in every frame, with no cropping and no cast shadow.

SPRITE SHEET LAYOUT: exactly 4 frames in ONE horizontal row, ordered chronologically from left to right, on a 16:9 landscape canvas. Each frame sits in its own SQUARE cell (final cleaned size 32×32 px) whose side equals the canvas width divided by 4; the row is centered vertically and the empty space above and below is flat magenta. Center one frame in each cell. The character occupies at most 65% of its cell's width and about 80% of its cell's height, leaving at least 15% empty magenta on each side, so frames never touch, overlap, or get cropped by a neighbor or the image edge. Same character scale, camera angle and proportions in every frame; head-top and feet stay at the same vertical positions in every frame, with the feet/base on one shared baseline. Do not add labels, numbers, grid lines, frame borders, duplicate rows, extra poses, or decorative elements. The sheet must be easy to slice into 4 equal cells.

CHARACTER: Timun Mas. DESIGN LOCK: Timun Mas, a brave young Javanese village girl, chibi proportions (head about 38% of body height, about 26 px tall in a 32 px cell), warm medium-brown skin, small dark eyes, black hair in a high round bun on top of the head with a thin muted-gold hairband, cream kebaya-style blouse with a ruffled hem and short sleeves, muted-gold sash at the waist, brown batik sarong with a small diamond lattice pattern reaching mid-shin, bare feet; 1 px dark-brown outline.
ANIMATION: idle breathing loop. FACING DIRECTION: right. FRAME-BY-FRAME ACTION: Frame 1 neutral standing; frame 2 subtle breathing/shoulder lift; frame 3 slight return/soft blink if face is visible; frame 4 return to the same neutral pose for a seamless loop. Preserve silhouette, outfit, colors, hair and accessories across all frames. The change between frames should be small and readable at native pixel scale. Output one sprite-sheet image only.
```

### TM-WALK-DOWN — Timun Mas — walk facing down

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE production-oriented SPRITE SHEET image for an original 2D top-down adventure game inspired by Indonesian folklore. Use a perfectly flat solid magenta (#FF00FF) background for manual removal, uniform edge to edge with no vignette, gradient or floor. Keep the entire sprite visible in every frame, with no cropping and no cast shadow.

SPRITE SHEET LAYOUT: exactly 6 frames in ONE horizontal row, ordered chronologically from left to right, on a 16:9 landscape canvas. Each frame sits in its own SQUARE cell (final cleaned size 32×32 px) whose side equals the canvas width divided by 6; the row is centered vertically and the empty space above and below is flat magenta. Center one frame in each cell. The character occupies at most 65% of its cell's width and about 80% of its cell's height, leaving at least 15% empty magenta on each side, so frames never touch, overlap, or get cropped by a neighbor or the image edge. Same character scale, camera angle and proportions in every frame; head-top and feet stay at the same vertical positions in every frame, with the feet/base on one shared baseline. Do not add labels, numbers, grid lines, frame borders, duplicate rows, extra poses, or decorative elements. The sheet must be easy to slice into 6 equal cells.

CHARACTER: Timun Mas. DESIGN LOCK: Timun Mas, a brave young Javanese village girl, chibi proportions (head about 38% of body height, about 26 px tall in a 32 px cell), warm medium-brown skin, small dark eyes, black hair in a high round bun on top of the head with a thin muted-gold hairband, cream kebaya-style blouse with a ruffled hem and short sleeves, muted-gold sash at the waist, brown batik sarong with a small diamond lattice pattern reaching mid-shin, bare feet; 1 px dark-brown outline.
ANIMATION: walk cycle. FACING DIRECTION: down. FRAME-BY-FRAME ACTION: A clean six-frame walk cycle: contact, passing, opposite contact, passing, then two transition frames returning smoothly to the first pose. Alternate legs and opposite arm swing; keep body bob subtle. Preserve silhouette, outfit, colors, hair and accessories across all frames. The change between frames should be small and readable at native pixel scale. Output one sprite-sheet image only.
```

### TM-WALK-UP — Timun Mas — walk facing up

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE production-oriented SPRITE SHEET image for an original 2D top-down adventure game inspired by Indonesian folklore. Use a perfectly flat solid magenta (#FF00FF) background for manual removal, uniform edge to edge with no vignette, gradient or floor. Keep the entire sprite visible in every frame, with no cropping and no cast shadow.

SPRITE SHEET LAYOUT: exactly 6 frames in ONE horizontal row, ordered chronologically from left to right, on a 16:9 landscape canvas. Each frame sits in its own SQUARE cell (final cleaned size 32×32 px) whose side equals the canvas width divided by 6; the row is centered vertically and the empty space above and below is flat magenta. Center one frame in each cell. The character occupies at most 65% of its cell's width and about 80% of its cell's height, leaving at least 15% empty magenta on each side, so frames never touch, overlap, or get cropped by a neighbor or the image edge. Same character scale, camera angle and proportions in every frame; head-top and feet stay at the same vertical positions in every frame, with the feet/base on one shared baseline. Do not add labels, numbers, grid lines, frame borders, duplicate rows, extra poses, or decorative elements. The sheet must be easy to slice into 6 equal cells.

CHARACTER: Timun Mas. DESIGN LOCK: Timun Mas, a brave young Javanese village girl, chibi proportions (head about 38% of body height, about 26 px tall in a 32 px cell), warm medium-brown skin, small dark eyes, black hair in a high round bun on top of the head with a thin muted-gold hairband, cream kebaya-style blouse with a ruffled hem and short sleeves, muted-gold sash at the waist, brown batik sarong with a small diamond lattice pattern reaching mid-shin, bare feet; 1 px dark-brown outline.
ANIMATION: walk cycle. FACING DIRECTION: up. FRAME-BY-FRAME ACTION: A clean six-frame walk cycle: contact, passing, opposite contact, passing, then two transition frames returning smoothly to the first pose. Alternate legs and opposite arm swing; keep body bob subtle. Preserve silhouette, outfit, colors, hair and accessories across all frames. The change between frames should be small and readable at native pixel scale. Output one sprite-sheet image only.
```

### TM-WALK-LEFT — Timun Mas — walk facing left

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE production-oriented SPRITE SHEET image for an original 2D top-down adventure game inspired by Indonesian folklore. Use a perfectly flat solid magenta (#FF00FF) background for manual removal, uniform edge to edge with no vignette, gradient or floor. Keep the entire sprite visible in every frame, with no cropping and no cast shadow.

SPRITE SHEET LAYOUT: exactly 6 frames in ONE horizontal row, ordered chronologically from left to right, on a 16:9 landscape canvas. Each frame sits in its own SQUARE cell (final cleaned size 32×32 px) whose side equals the canvas width divided by 6; the row is centered vertically and the empty space above and below is flat magenta. Center one frame in each cell. The character occupies at most 65% of its cell's width and about 80% of its cell's height, leaving at least 15% empty magenta on each side, so frames never touch, overlap, or get cropped by a neighbor or the image edge. Same character scale, camera angle and proportions in every frame; head-top and feet stay at the same vertical positions in every frame, with the feet/base on one shared baseline. Do not add labels, numbers, grid lines, frame borders, duplicate rows, extra poses, or decorative elements. The sheet must be easy to slice into 6 equal cells.

CHARACTER: Timun Mas. DESIGN LOCK: Timun Mas, a brave young Javanese village girl, chibi proportions (head about 38% of body height, about 26 px tall in a 32 px cell), warm medium-brown skin, small dark eyes, black hair in a high round bun on top of the head with a thin muted-gold hairband, cream kebaya-style blouse with a ruffled hem and short sleeves, muted-gold sash at the waist, brown batik sarong with a small diamond lattice pattern reaching mid-shin, bare feet; 1 px dark-brown outline.
ANIMATION: walk cycle. FACING DIRECTION: left. FRAME-BY-FRAME ACTION: A clean six-frame walk cycle: contact, passing, opposite contact, passing, then two transition frames returning smoothly to the first pose. Alternate legs and opposite arm swing; keep body bob subtle. Preserve silhouette, outfit, colors, hair and accessories across all frames. The change between frames should be small and readable at native pixel scale. Output one sprite-sheet image only.
```

### TM-WALK-RIGHT — Timun Mas — walk facing right

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE production-oriented SPRITE SHEET image for an original 2D top-down adventure game inspired by Indonesian folklore. Use a perfectly flat solid magenta (#FF00FF) background for manual removal, uniform edge to edge with no vignette, gradient or floor. Keep the entire sprite visible in every frame, with no cropping and no cast shadow.

SPRITE SHEET LAYOUT: exactly 6 frames in ONE horizontal row, ordered chronologically from left to right, on a 16:9 landscape canvas. Each frame sits in its own SQUARE cell (final cleaned size 32×32 px) whose side equals the canvas width divided by 6; the row is centered vertically and the empty space above and below is flat magenta. Center one frame in each cell. The character occupies at most 65% of its cell's width and about 80% of its cell's height, leaving at least 15% empty magenta on each side, so frames never touch, overlap, or get cropped by a neighbor or the image edge. Same character scale, camera angle and proportions in every frame; head-top and feet stay at the same vertical positions in every frame, with the feet/base on one shared baseline. Do not add labels, numbers, grid lines, frame borders, duplicate rows, extra poses, or decorative elements. The sheet must be easy to slice into 6 equal cells.

CHARACTER: Timun Mas. DESIGN LOCK: Timun Mas, a brave young Javanese village girl, chibi proportions (head about 38% of body height, about 26 px tall in a 32 px cell), warm medium-brown skin, small dark eyes, black hair in a high round bun on top of the head with a thin muted-gold hairband, cream kebaya-style blouse with a ruffled hem and short sleeves, muted-gold sash at the waist, brown batik sarong with a small diamond lattice pattern reaching mid-shin, bare feet; 1 px dark-brown outline.
ANIMATION: walk cycle. FACING DIRECTION: right. FRAME-BY-FRAME ACTION: A clean six-frame walk cycle: contact, passing, opposite contact, passing, then two transition frames returning smoothly to the first pose. Alternate legs and opposite arm swing; keep body bob subtle. Preserve silhouette, outfit, colors, hair and accessories across all frames. The change between frames should be small and readable at native pixel scale. Output one sprite-sheet image only.
```

### TM-RUN-DOWN — Timun Mas — run facing down

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE production-oriented SPRITE SHEET image for an original 2D top-down adventure game inspired by Indonesian folklore. Use a perfectly flat solid magenta (#FF00FF) background for manual removal, uniform edge to edge with no vignette, gradient or floor. Keep the entire sprite visible in every frame, with no cropping and no cast shadow.

SPRITE SHEET LAYOUT: exactly 6 frames in ONE horizontal row, ordered chronologically from left to right, on a 16:9 landscape canvas. Each frame sits in its own SQUARE cell (final cleaned size 32×32 px) whose side equals the canvas width divided by 6; the row is centered vertically and the empty space above and below is flat magenta. Center one frame in each cell. The character occupies at most 65% of its cell's width and about 80% of its cell's height, leaving at least 15% empty magenta on each side, so frames never touch, overlap, or get cropped by a neighbor or the image edge. Same character scale, camera angle and proportions in every frame; head-top and feet stay at the same vertical positions in every frame, with the feet/base on one shared baseline. Do not add labels, numbers, grid lines, frame borders, duplicate rows, extra poses, or decorative elements. The sheet must be easy to slice into 6 equal cells.

CHARACTER: Timun Mas. DESIGN LOCK: Timun Mas, a brave young Javanese village girl, chibi proportions (head about 38% of body height, about 26 px tall in a 32 px cell), warm medium-brown skin, small dark eyes, black hair in a high round bun on top of the head with a thin muted-gold hairband, cream kebaya-style blouse with a ruffled hem and short sleeves, muted-gold sash at the waist, brown batik sarong with a small diamond lattice pattern reaching mid-shin, bare feet; 1 px dark-brown outline.
ANIMATION: run cycle. FACING DIRECTION: down. FRAME-BY-FRAME ACTION: A clean six-frame run cycle: alternating foot contact, push-off and airborne phases. Stronger arm swing and forward lean than walking; keep the head and outfit stable and the feet anchor consistent. Preserve silhouette, outfit, colors, hair and accessories across all frames. The change between frames should be small and readable at native pixel scale. Output one sprite-sheet image only.
```

### TM-RUN-UP — Timun Mas — run facing up

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE production-oriented SPRITE SHEET image for an original 2D top-down adventure game inspired by Indonesian folklore. Use a perfectly flat solid magenta (#FF00FF) background for manual removal, uniform edge to edge with no vignette, gradient or floor. Keep the entire sprite visible in every frame, with no cropping and no cast shadow.

SPRITE SHEET LAYOUT: exactly 6 frames in ONE horizontal row, ordered chronologically from left to right, on a 16:9 landscape canvas. Each frame sits in its own SQUARE cell (final cleaned size 32×32 px) whose side equals the canvas width divided by 6; the row is centered vertically and the empty space above and below is flat magenta. Center one frame in each cell. The character occupies at most 65% of its cell's width and about 80% of its cell's height, leaving at least 15% empty magenta on each side, so frames never touch, overlap, or get cropped by a neighbor or the image edge. Same character scale, camera angle and proportions in every frame; head-top and feet stay at the same vertical positions in every frame, with the feet/base on one shared baseline. Do not add labels, numbers, grid lines, frame borders, duplicate rows, extra poses, or decorative elements. The sheet must be easy to slice into 6 equal cells.

CHARACTER: Timun Mas. DESIGN LOCK: Timun Mas, a brave young Javanese village girl, chibi proportions (head about 38% of body height, about 26 px tall in a 32 px cell), warm medium-brown skin, small dark eyes, black hair in a high round bun on top of the head with a thin muted-gold hairband, cream kebaya-style blouse with a ruffled hem and short sleeves, muted-gold sash at the waist, brown batik sarong with a small diamond lattice pattern reaching mid-shin, bare feet; 1 px dark-brown outline.
ANIMATION: run cycle. FACING DIRECTION: up. FRAME-BY-FRAME ACTION: A clean six-frame run cycle: alternating foot contact, push-off and airborne phases. Stronger arm swing and forward lean than walking; keep the head and outfit stable and the feet anchor consistent. Preserve silhouette, outfit, colors, hair and accessories across all frames. The change between frames should be small and readable at native pixel scale. Output one sprite-sheet image only.
```

### TM-RUN-LEFT — Timun Mas — run facing left

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE production-oriented SPRITE SHEET image for an original 2D top-down adventure game inspired by Indonesian folklore. Use a perfectly flat solid magenta (#FF00FF) background for manual removal, uniform edge to edge with no vignette, gradient or floor. Keep the entire sprite visible in every frame, with no cropping and no cast shadow.

SPRITE SHEET LAYOUT: exactly 6 frames in ONE horizontal row, ordered chronologically from left to right, on a 16:9 landscape canvas. Each frame sits in its own SQUARE cell (final cleaned size 32×32 px) whose side equals the canvas width divided by 6; the row is centered vertically and the empty space above and below is flat magenta. Center one frame in each cell. The character occupies at most 65% of its cell's width and about 80% of its cell's height, leaving at least 15% empty magenta on each side, so frames never touch, overlap, or get cropped by a neighbor or the image edge. Same character scale, camera angle and proportions in every frame; head-top and feet stay at the same vertical positions in every frame, with the feet/base on one shared baseline. Do not add labels, numbers, grid lines, frame borders, duplicate rows, extra poses, or decorative elements. The sheet must be easy to slice into 6 equal cells.

CHARACTER: Timun Mas. DESIGN LOCK: Timun Mas, a brave young Javanese village girl, chibi proportions (head about 38% of body height, about 26 px tall in a 32 px cell), warm medium-brown skin, small dark eyes, black hair in a high round bun on top of the head with a thin muted-gold hairband, cream kebaya-style blouse with a ruffled hem and short sleeves, muted-gold sash at the waist, brown batik sarong with a small diamond lattice pattern reaching mid-shin, bare feet; 1 px dark-brown outline.
ANIMATION: run cycle. FACING DIRECTION: left. FRAME-BY-FRAME ACTION: A clean six-frame run cycle: alternating foot contact, push-off and airborne phases. Stronger arm swing and forward lean than walking; keep the head and outfit stable and the feet anchor consistent. Preserve silhouette, outfit, colors, hair and accessories across all frames. The change between frames should be small and readable at native pixel scale. Output one sprite-sheet image only.
```

### TM-RUN-RIGHT — Timun Mas — run facing right

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE production-oriented SPRITE SHEET image for an original 2D top-down adventure game inspired by Indonesian folklore. Use a perfectly flat solid magenta (#FF00FF) background for manual removal, uniform edge to edge with no vignette, gradient or floor. Keep the entire sprite visible in every frame, with no cropping and no cast shadow.

SPRITE SHEET LAYOUT: exactly 6 frames in ONE horizontal row, ordered chronologically from left to right, on a 16:9 landscape canvas. Each frame sits in its own SQUARE cell (final cleaned size 32×32 px) whose side equals the canvas width divided by 6; the row is centered vertically and the empty space above and below is flat magenta. Center one frame in each cell. The character occupies at most 65% of its cell's width and about 80% of its cell's height, leaving at least 15% empty magenta on each side, so frames never touch, overlap, or get cropped by a neighbor or the image edge. Same character scale, camera angle and proportions in every frame; head-top and feet stay at the same vertical positions in every frame, with the feet/base on one shared baseline. Do not add labels, numbers, grid lines, frame borders, duplicate rows, extra poses, or decorative elements. The sheet must be easy to slice into 6 equal cells.

CHARACTER: Timun Mas. DESIGN LOCK: Timun Mas, a brave young Javanese village girl, chibi proportions (head about 38% of body height, about 26 px tall in a 32 px cell), warm medium-brown skin, small dark eyes, black hair in a high round bun on top of the head with a thin muted-gold hairband, cream kebaya-style blouse with a ruffled hem and short sleeves, muted-gold sash at the waist, brown batik sarong with a small diamond lattice pattern reaching mid-shin, bare feet; 1 px dark-brown outline.
ANIMATION: run cycle. FACING DIRECTION: right. FRAME-BY-FRAME ACTION: A clean six-frame run cycle: alternating foot contact, push-off and airborne phases. Stronger arm swing and forward lean than walking; keep the head and outfit stable and the feet anchor consistent. Preserve silhouette, outfit, colors, hair and accessories across all frames. The change between frames should be small and readable at native pixel scale. Output one sprite-sheet image only.
```

### TM-THROW-DOWN — Timun Mas — throw/use magical item facing down

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE production-oriented SPRITE SHEET image for an original 2D top-down adventure game inspired by Indonesian folklore. Use a perfectly flat solid magenta (#FF00FF) background for manual removal, uniform edge to edge with no vignette, gradient or floor. Keep the entire sprite visible in every frame, with no cropping and no cast shadow.

SPRITE SHEET LAYOUT: exactly 6 frames in ONE horizontal row, ordered chronologically from left to right, on a 16:9 landscape canvas. Each frame sits in its own SQUARE cell (final cleaned size 32×32 px) whose side equals the canvas width divided by 6; the row is centered vertically and the empty space above and below is flat magenta. Center one frame in each cell. The character occupies at most 65% of its cell's width and about 80% of its cell's height, leaving at least 15% empty magenta on each side, so frames never touch, overlap, or get cropped by a neighbor or the image edge. Same character scale, camera angle and proportions in every frame; head-top and feet stay at the same vertical positions in every frame, with the feet/base on one shared baseline. Do not add labels, numbers, grid lines, frame borders, duplicate rows, extra poses, or decorative elements. The sheet must be easy to slice into 6 equal cells.

CHARACTER: Timun Mas. DESIGN LOCK: Timun Mas, a brave young Javanese village girl, chibi proportions (head about 38% of body height, about 26 px tall in a 32 px cell), warm medium-brown skin, small dark eyes, black hair in a high round bun on top of the head with a thin muted-gold hairband, cream kebaya-style blouse with a ruffled hem and short sleeves, muted-gold sash at the waist, brown batik sarong with a small diamond lattice pattern reaching mid-shin, bare feet; 1 px dark-brown outline.
ANIMATION: throw/use item action. FACING DIRECTION: down. FRAME-BY-FRAME ACTION: Anticipation, arm draws back, wind-up, release/throw, follow-through, recovery to ready stance. Show no visible text. Hand/item silhouette must remain readable; item itself may be omitted so it can be drawn separately. Preserve silhouette, outfit, colors, hair and accessories across all frames. The change between frames should be small and readable at native pixel scale. Output one sprite-sheet image only.
```

### TM-THROW-UP — Timun Mas — throw/use magical item facing up

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE production-oriented SPRITE SHEET image for an original 2D top-down adventure game inspired by Indonesian folklore. Use a perfectly flat solid magenta (#FF00FF) background for manual removal, uniform edge to edge with no vignette, gradient or floor. Keep the entire sprite visible in every frame, with no cropping and no cast shadow.

SPRITE SHEET LAYOUT: exactly 6 frames in ONE horizontal row, ordered chronologically from left to right, on a 16:9 landscape canvas. Each frame sits in its own SQUARE cell (final cleaned size 32×32 px) whose side equals the canvas width divided by 6; the row is centered vertically and the empty space above and below is flat magenta. Center one frame in each cell. The character occupies at most 65% of its cell's width and about 80% of its cell's height, leaving at least 15% empty magenta on each side, so frames never touch, overlap, or get cropped by a neighbor or the image edge. Same character scale, camera angle and proportions in every frame; head-top and feet stay at the same vertical positions in every frame, with the feet/base on one shared baseline. Do not add labels, numbers, grid lines, frame borders, duplicate rows, extra poses, or decorative elements. The sheet must be easy to slice into 6 equal cells.

CHARACTER: Timun Mas. DESIGN LOCK: Timun Mas, a brave young Javanese village girl, chibi proportions (head about 38% of body height, about 26 px tall in a 32 px cell), warm medium-brown skin, small dark eyes, black hair in a high round bun on top of the head with a thin muted-gold hairband, cream kebaya-style blouse with a ruffled hem and short sleeves, muted-gold sash at the waist, brown batik sarong with a small diamond lattice pattern reaching mid-shin, bare feet; 1 px dark-brown outline.
ANIMATION: throw/use item action. FACING DIRECTION: up. FRAME-BY-FRAME ACTION: Anticipation, arm draws back, wind-up, release/throw, follow-through, recovery to ready stance. Show no visible text. Hand/item silhouette must remain readable; item itself may be omitted so it can be drawn separately. Preserve silhouette, outfit, colors, hair and accessories across all frames. The change between frames should be small and readable at native pixel scale. Output one sprite-sheet image only.
```

### TM-THROW-LEFT — Timun Mas — throw/use magical item facing left

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE production-oriented SPRITE SHEET image for an original 2D top-down adventure game inspired by Indonesian folklore. Use a perfectly flat solid magenta (#FF00FF) background for manual removal, uniform edge to edge with no vignette, gradient or floor. Keep the entire sprite visible in every frame, with no cropping and no cast shadow.

SPRITE SHEET LAYOUT: exactly 6 frames in ONE horizontal row, ordered chronologically from left to right, on a 16:9 landscape canvas. Each frame sits in its own SQUARE cell (final cleaned size 32×32 px) whose side equals the canvas width divided by 6; the row is centered vertically and the empty space above and below is flat magenta. Center one frame in each cell. The character occupies at most 65% of its cell's width and about 80% of its cell's height, leaving at least 15% empty magenta on each side, so frames never touch, overlap, or get cropped by a neighbor or the image edge. Same character scale, camera angle and proportions in every frame; head-top and feet stay at the same vertical positions in every frame, with the feet/base on one shared baseline. Do not add labels, numbers, grid lines, frame borders, duplicate rows, extra poses, or decorative elements. The sheet must be easy to slice into 6 equal cells.

CHARACTER: Timun Mas. DESIGN LOCK: Timun Mas, a brave young Javanese village girl, chibi proportions (head about 38% of body height, about 26 px tall in a 32 px cell), warm medium-brown skin, small dark eyes, black hair in a high round bun on top of the head with a thin muted-gold hairband, cream kebaya-style blouse with a ruffled hem and short sleeves, muted-gold sash at the waist, brown batik sarong with a small diamond lattice pattern reaching mid-shin, bare feet; 1 px dark-brown outline.
ANIMATION: throw/use item action. FACING DIRECTION: left. FRAME-BY-FRAME ACTION: Anticipation, arm draws back, wind-up, release/throw, follow-through, recovery to ready stance. Show no visible text. Hand/item silhouette must remain readable; item itself may be omitted so it can be drawn separately. Preserve silhouette, outfit, colors, hair and accessories across all frames. The change between frames should be small and readable at native pixel scale. Output one sprite-sheet image only.
```

### TM-THROW-RIGHT — Timun Mas — throw/use magical item facing right

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE production-oriented SPRITE SHEET image for an original 2D top-down adventure game inspired by Indonesian folklore. Use a perfectly flat solid magenta (#FF00FF) background for manual removal, uniform edge to edge with no vignette, gradient or floor. Keep the entire sprite visible in every frame, with no cropping and no cast shadow.

SPRITE SHEET LAYOUT: exactly 6 frames in ONE horizontal row, ordered chronologically from left to right, on a 16:9 landscape canvas. Each frame sits in its own SQUARE cell (final cleaned size 32×32 px) whose side equals the canvas width divided by 6; the row is centered vertically and the empty space above and below is flat magenta. Center one frame in each cell. The character occupies at most 65% of its cell's width and about 80% of its cell's height, leaving at least 15% empty magenta on each side, so frames never touch, overlap, or get cropped by a neighbor or the image edge. Same character scale, camera angle and proportions in every frame; head-top and feet stay at the same vertical positions in every frame, with the feet/base on one shared baseline. Do not add labels, numbers, grid lines, frame borders, duplicate rows, extra poses, or decorative elements. The sheet must be easy to slice into 6 equal cells.

CHARACTER: Timun Mas. DESIGN LOCK: Timun Mas, a brave young Javanese village girl, chibi proportions (head about 38% of body height, about 26 px tall in a 32 px cell), warm medium-brown skin, small dark eyes, black hair in a high round bun on top of the head with a thin muted-gold hairband, cream kebaya-style blouse with a ruffled hem and short sleeves, muted-gold sash at the waist, brown batik sarong with a small diamond lattice pattern reaching mid-shin, bare feet; 1 px dark-brown outline.
ANIMATION: throw/use item action. FACING DIRECTION: right. FRAME-BY-FRAME ACTION: Anticipation, arm draws back, wind-up, release/throw, follow-through, recovery to ready stance. Show no visible text. Hand/item silhouette must remain readable; item itself may be omitted so it can be drawn separately. Preserve silhouette, outfit, colors, hair and accessories across all frames. The change between frames should be small and readable at native pixel scale. Output one sprite-sheet image only.
```

### TM-HURT — Timun Mas — hurt reaction

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE production-oriented SPRITE SHEET image for an original 2D top-down adventure game inspired by Indonesian folklore. Use a perfectly flat solid magenta (#FF00FF) background for manual removal, uniform edge to edge with no vignette, gradient or floor. Keep the entire sprite visible in every frame, with no cropping and no cast shadow.

SPRITE SHEET LAYOUT: exactly 4 frames in ONE horizontal row, ordered chronologically from left to right, on a 16:9 landscape canvas. Each frame sits in its own SQUARE cell (final cleaned size 32×32 px) whose side equals the canvas width divided by 4; the row is centered vertically and the empty space above and below is flat magenta. Center one frame in each cell. The character occupies at most 65% of its cell's width and about 80% of its cell's height, leaving at least 15% empty magenta on each side, so frames never touch, overlap, or get cropped by a neighbor or the image edge. Same character scale, camera angle and proportions in every frame; head-top and feet stay at the same vertical positions in every frame, with the feet/base on one shared baseline. Do not add labels, numbers, grid lines, frame borders, duplicate rows, extra poses, or decorative elements. The sheet must be easy to slice into 4 equal cells.

CHARACTER: Timun Mas. DESIGN LOCK: Timun Mas, a brave young Javanese village girl, chibi proportions (head about 38% of body height, about 26 px tall in a 32 px cell), warm medium-brown skin, small dark eyes, black hair in a high round bun on top of the head with a thin muted-gold hairband, cream kebaya-style blouse with a ruffled hem and short sleeves, muted-gold sash at the waist, brown batik sarong with a small diamond lattice pattern reaching mid-shin, bare feet; 1 px dark-brown outline.
ANIMATION: brief hurt/flinch reaction. FACING DIRECTION: front three-quarter, readable facing down. FRAME-BY-FRAME ACTION: Neutral, flinch backward with arms raised, recoil peak, recover to neutral. No blood, no injury detail. Preserve silhouette, outfit, colors, hair and accessories across all frames. The change between frames should be small and readable at native pixel scale. Output one sprite-sheet image only.
```

### TM-INTERACT — Timun Mas — interact/talk

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE production-oriented SPRITE SHEET image for an original 2D top-down adventure game inspired by Indonesian folklore. Use a perfectly flat solid magenta (#FF00FF) background for manual removal, uniform edge to edge with no vignette, gradient or floor. Keep the entire sprite visible in every frame, with no cropping and no cast shadow.

SPRITE SHEET LAYOUT: exactly 4 frames in ONE horizontal row, ordered chronologically from left to right, on a 16:9 landscape canvas. Each frame sits in its own SQUARE cell (final cleaned size 32×32 px) whose side equals the canvas width divided by 4; the row is centered vertically and the empty space above and below is flat magenta. Center one frame in each cell. The character occupies at most 65% of its cell's width and about 80% of its cell's height, leaving at least 15% empty magenta on each side, so frames never touch, overlap, or get cropped by a neighbor or the image edge. Same character scale, camera angle and proportions in every frame; head-top and feet stay at the same vertical positions in every frame, with the feet/base on one shared baseline. Do not add labels, numbers, grid lines, frame borders, duplicate rows, extra poses, or decorative elements. The sheet must be easy to slice into 4 equal cells.

CHARACTER: Timun Mas. DESIGN LOCK: Timun Mas, a brave young Javanese village girl, chibi proportions (head about 38% of body height, about 26 px tall in a 32 px cell), warm medium-brown skin, small dark eyes, black hair in a high round bun on top of the head with a thin muted-gold hairband, cream kebaya-style blouse with a ruffled hem and short sleeves, muted-gold sash at the waist, brown batik sarong with a small diamond lattice pattern reaching mid-shin, bare feet; 1 px dark-brown outline.
ANIMATION: gentle interaction/talking gesture. FACING DIRECTION: facing down. FRAME-BY-FRAME ACTION: Neutral, small hand gesture, second gentle gesture with slight head movement, return to neutral. Preserve silhouette, outfit, colors, hair and accessories across all frames. The change between frames should be small and readable at native pixel scale. Output one sprite-sheet image only.
```

### TM-RECEIVE — Timun Mas — receiving item

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE production-oriented SPRITE SHEET image for an original 2D top-down adventure game inspired by Indonesian folklore. Use a perfectly flat solid magenta (#FF00FF) background for manual removal, uniform edge to edge with no vignette, gradient or floor. Keep the entire sprite visible in every frame, with no cropping and no cast shadow.

SPRITE SHEET LAYOUT: exactly 4 frames in ONE horizontal row, ordered chronologically from left to right, on a 16:9 landscape canvas. Each frame sits in its own SQUARE cell (final cleaned size 32×32 px) whose side equals the canvas width divided by 4; the row is centered vertically and the empty space above and below is flat magenta. Center one frame in each cell. The character occupies at most 65% of its cell's width and about 80% of its cell's height, leaving at least 15% empty magenta on each side, so frames never touch, overlap, or get cropped by a neighbor or the image edge. Same character scale, camera angle and proportions in every frame; head-top and feet stay at the same vertical positions in every frame, with the feet/base on one shared baseline. Do not add labels, numbers, grid lines, frame borders, duplicate rows, extra poses, or decorative elements. The sheet must be easy to slice into 4 equal cells.

CHARACTER: Timun Mas. DESIGN LOCK: Timun Mas, a brave young Javanese village girl, chibi proportions (head about 38% of body height, about 26 px tall in a 32 px cell), warm medium-brown skin, small dark eyes, black hair in a high round bun on top of the head with a thin muted-gold hairband, cream kebaya-style blouse with a ruffled hem and short sleeves, muted-gold sash at the waist, brown batik sarong with a small diamond lattice pattern reaching mid-shin, bare feet; 1 px dark-brown outline.
ANIMATION: receive an item with both hands. FACING DIRECTION: facing down. FRAME-BY-FRAME ACTION: Hands start relaxed, bring hands forward, receive/cup a small item, settle into a grateful pose. Keep item simple and separable. Preserve silhouette, outfit, colors, hair and accessories across all frames. The change between frames should be small and readable at native pixel scale. Output one sprite-sheet image only.
```

### TM-VICTORY — Timun Mas — victory/relief

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE production-oriented SPRITE SHEET image for an original 2D top-down adventure game inspired by Indonesian folklore. Use a perfectly flat solid magenta (#FF00FF) background for manual removal, uniform edge to edge with no vignette, gradient or floor. Keep the entire sprite visible in every frame, with no cropping and no cast shadow.

SPRITE SHEET LAYOUT: exactly 4 frames in ONE horizontal row, ordered chronologically from left to right, on a 16:9 landscape canvas. Each frame sits in its own SQUARE cell (final cleaned size 32×32 px) whose side equals the canvas width divided by 4; the row is centered vertically and the empty space above and below is flat magenta. Center one frame in each cell. The character occupies at most 65% of its cell's width and about 80% of its cell's height, leaving at least 15% empty magenta on each side, so frames never touch, overlap, or get cropped by a neighbor or the image edge. Same character scale, camera angle and proportions in every frame; head-top and feet stay at the same vertical positions in every frame, with the feet/base on one shared baseline. Do not add labels, numbers, grid lines, frame borders, duplicate rows, extra poses, or decorative elements. The sheet must be easy to slice into 4 equal cells.

CHARACTER: Timun Mas. DESIGN LOCK: Timun Mas, a brave young Javanese village girl, chibi proportions (head about 38% of body height, about 26 px tall in a 32 px cell), warm medium-brown skin, small dark eyes, black hair in a high round bun on top of the head with a thin muted-gold hairband, cream kebaya-style blouse with a ruffled hem and short sleeves, muted-gold sash at the waist, brown batik sarong with a small diamond lattice pattern reaching mid-shin, bare feet; 1 px dark-brown outline.
ANIMATION: relieved victory loop. FACING DIRECTION: facing down. FRAME-BY-FRAME ACTION: Tense posture relaxes, small relieved smile, arms lift slightly in quiet celebration, settle back into a calm happy pose. Preserve silhouette, outfit, colors, hair and accessories across all frames. The change between frames should be small and readable at native pixel scale. Output one sprite-sheet image only.
```

### BI-IDLE-DOWN — Buto Ijo — idle facing down

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE production-oriented SPRITE SHEET image for an original 2D top-down adventure game inspired by Indonesian folklore. Use a perfectly flat solid magenta (#FF00FF) background for manual removal, uniform edge to edge with no vignette, gradient or floor. Keep the entire sprite visible in every frame, with no cropping and no cast shadow.

SPRITE SHEET LAYOUT: exactly 4 frames in ONE horizontal row, ordered chronologically from left to right, on a 16:9 landscape canvas. Each frame sits in its own SQUARE cell (final cleaned size 64×64 px) whose side equals the canvas width divided by 4; the row is centered vertically and the empty space above and below is flat magenta. Center one frame in each cell. The character occupies at most 65% of its cell's width and about 80% of its cell's height, leaving at least 15% empty magenta on each side, so frames never touch, overlap, or get cropped by a neighbor or the image edge. Same character scale, camera angle and proportions in every frame; head-top and feet stay at the same vertical positions in every frame, with the feet/base on one shared baseline. Do not add labels, numbers, grid lines, frame borders, duplicate rows, extra poses, or decorative elements. The sheet must be easy to slice into 4 equal cells.

CHARACTER: Buto Ijo. DESIGN LOCK: Buto Ijo, a huge intimidating ogre from Indonesian folklore, about twice Timun Mas's height (about 56 px tall in a 64 px cell), broad hunched shoulders, heavy barrel chest, forest-green skin (#2F5E3A / #4F8A4B / #8DBB5F), heavy brow, small cream tusks, wild messy dark-brown hair, bare chest, dark-brown waist cloth with a rope belt, bare feet; scary but suitable for a family-friendly pixel adventure; 1 px dark-brown outline.
ANIMATION: heavy idle breathing loop. FACING DIRECTION: down. FRAME-BY-FRAME ACTION: Subtle chest breathing, small shoulder movement, slight head sway, return to starting stance; intimidating but readable. Preserve silhouette, outfit, colors, hair and accessories across all frames. The change between frames should be small and readable at native pixel scale. Output one sprite-sheet image only.
```

### BI-IDLE-UP — Buto Ijo — idle facing up

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE production-oriented SPRITE SHEET image for an original 2D top-down adventure game inspired by Indonesian folklore. Use a perfectly flat solid magenta (#FF00FF) background for manual removal, uniform edge to edge with no vignette, gradient or floor. Keep the entire sprite visible in every frame, with no cropping and no cast shadow.

SPRITE SHEET LAYOUT: exactly 4 frames in ONE horizontal row, ordered chronologically from left to right, on a 16:9 landscape canvas. Each frame sits in its own SQUARE cell (final cleaned size 64×64 px) whose side equals the canvas width divided by 4; the row is centered vertically and the empty space above and below is flat magenta. Center one frame in each cell. The character occupies at most 65% of its cell's width and about 80% of its cell's height, leaving at least 15% empty magenta on each side, so frames never touch, overlap, or get cropped by a neighbor or the image edge. Same character scale, camera angle and proportions in every frame; head-top and feet stay at the same vertical positions in every frame, with the feet/base on one shared baseline. Do not add labels, numbers, grid lines, frame borders, duplicate rows, extra poses, or decorative elements. The sheet must be easy to slice into 4 equal cells.

CHARACTER: Buto Ijo. DESIGN LOCK: Buto Ijo, a huge intimidating ogre from Indonesian folklore, about twice Timun Mas's height (about 56 px tall in a 64 px cell), broad hunched shoulders, heavy barrel chest, forest-green skin (#2F5E3A / #4F8A4B / #8DBB5F), heavy brow, small cream tusks, wild messy dark-brown hair, bare chest, dark-brown waist cloth with a rope belt, bare feet; scary but suitable for a family-friendly pixel adventure; 1 px dark-brown outline.
ANIMATION: heavy idle breathing loop. FACING DIRECTION: up. FRAME-BY-FRAME ACTION: Subtle chest breathing, small shoulder movement, slight head sway, return to starting stance; intimidating but readable. Preserve silhouette, outfit, colors, hair and accessories across all frames. The change between frames should be small and readable at native pixel scale. Output one sprite-sheet image only.
```

### BI-IDLE-LEFT — Buto Ijo — idle facing left

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE production-oriented SPRITE SHEET image for an original 2D top-down adventure game inspired by Indonesian folklore. Use a perfectly flat solid magenta (#FF00FF) background for manual removal, uniform edge to edge with no vignette, gradient or floor. Keep the entire sprite visible in every frame, with no cropping and no cast shadow.

SPRITE SHEET LAYOUT: exactly 4 frames in ONE horizontal row, ordered chronologically from left to right, on a 16:9 landscape canvas. Each frame sits in its own SQUARE cell (final cleaned size 64×64 px) whose side equals the canvas width divided by 4; the row is centered vertically and the empty space above and below is flat magenta. Center one frame in each cell. The character occupies at most 65% of its cell's width and about 80% of its cell's height, leaving at least 15% empty magenta on each side, so frames never touch, overlap, or get cropped by a neighbor or the image edge. Same character scale, camera angle and proportions in every frame; head-top and feet stay at the same vertical positions in every frame, with the feet/base on one shared baseline. Do not add labels, numbers, grid lines, frame borders, duplicate rows, extra poses, or decorative elements. The sheet must be easy to slice into 4 equal cells.

CHARACTER: Buto Ijo. DESIGN LOCK: Buto Ijo, a huge intimidating ogre from Indonesian folklore, about twice Timun Mas's height (about 56 px tall in a 64 px cell), broad hunched shoulders, heavy barrel chest, forest-green skin (#2F5E3A / #4F8A4B / #8DBB5F), heavy brow, small cream tusks, wild messy dark-brown hair, bare chest, dark-brown waist cloth with a rope belt, bare feet; scary but suitable for a family-friendly pixel adventure; 1 px dark-brown outline.
ANIMATION: heavy idle breathing loop. FACING DIRECTION: left. FRAME-BY-FRAME ACTION: Subtle chest breathing, small shoulder movement, slight head sway, return to starting stance; intimidating but readable. Preserve silhouette, outfit, colors, hair and accessories across all frames. The change between frames should be small and readable at native pixel scale. Output one sprite-sheet image only.
```

### BI-IDLE-RIGHT — Buto Ijo — idle facing right

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE production-oriented SPRITE SHEET image for an original 2D top-down adventure game inspired by Indonesian folklore. Use a perfectly flat solid magenta (#FF00FF) background for manual removal, uniform edge to edge with no vignette, gradient or floor. Keep the entire sprite visible in every frame, with no cropping and no cast shadow.

SPRITE SHEET LAYOUT: exactly 4 frames in ONE horizontal row, ordered chronologically from left to right, on a 16:9 landscape canvas. Each frame sits in its own SQUARE cell (final cleaned size 64×64 px) whose side equals the canvas width divided by 4; the row is centered vertically and the empty space above and below is flat magenta. Center one frame in each cell. The character occupies at most 65% of its cell's width and about 80% of its cell's height, leaving at least 15% empty magenta on each side, so frames never touch, overlap, or get cropped by a neighbor or the image edge. Same character scale, camera angle and proportions in every frame; head-top and feet stay at the same vertical positions in every frame, with the feet/base on one shared baseline. Do not add labels, numbers, grid lines, frame borders, duplicate rows, extra poses, or decorative elements. The sheet must be easy to slice into 4 equal cells.

CHARACTER: Buto Ijo. DESIGN LOCK: Buto Ijo, a huge intimidating ogre from Indonesian folklore, about twice Timun Mas's height (about 56 px tall in a 64 px cell), broad hunched shoulders, heavy barrel chest, forest-green skin (#2F5E3A / #4F8A4B / #8DBB5F), heavy brow, small cream tusks, wild messy dark-brown hair, bare chest, dark-brown waist cloth with a rope belt, bare feet; scary but suitable for a family-friendly pixel adventure; 1 px dark-brown outline.
ANIMATION: heavy idle breathing loop. FACING DIRECTION: right. FRAME-BY-FRAME ACTION: Subtle chest breathing, small shoulder movement, slight head sway, return to starting stance; intimidating but readable. Preserve silhouette, outfit, colors, hair and accessories across all frames. The change between frames should be small and readable at native pixel scale. Output one sprite-sheet image only.
```

### BI-WALK-DOWN — Buto Ijo — walk facing down

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE production-oriented SPRITE SHEET image for an original 2D top-down adventure game inspired by Indonesian folklore. Use a perfectly flat solid magenta (#FF00FF) background for manual removal, uniform edge to edge with no vignette, gradient or floor. Keep the entire sprite visible in every frame, with no cropping and no cast shadow.

SPRITE SHEET LAYOUT: exactly 6 frames in ONE horizontal row, ordered chronologically from left to right, on a 16:9 landscape canvas. Each frame sits in its own SQUARE cell (final cleaned size 64×64 px) whose side equals the canvas width divided by 6; the row is centered vertically and the empty space above and below is flat magenta. Center one frame in each cell. The character occupies at most 65% of its cell's width and about 80% of its cell's height, leaving at least 15% empty magenta on each side, so frames never touch, overlap, or get cropped by a neighbor or the image edge. Same character scale, camera angle and proportions in every frame; head-top and feet stay at the same vertical positions in every frame, with the feet/base on one shared baseline. Do not add labels, numbers, grid lines, frame borders, duplicate rows, extra poses, or decorative elements. The sheet must be easy to slice into 6 equal cells.

CHARACTER: Buto Ijo. DESIGN LOCK: Buto Ijo, a huge intimidating ogre from Indonesian folklore, about twice Timun Mas's height (about 56 px tall in a 64 px cell), broad hunched shoulders, heavy barrel chest, forest-green skin (#2F5E3A / #4F8A4B / #8DBB5F), heavy brow, small cream tusks, wild messy dark-brown hair, bare chest, dark-brown waist cloth with a rope belt, bare feet; scary but suitable for a family-friendly pixel adventure; 1 px dark-brown outline.
ANIMATION: walk. FACING DIRECTION: down. FRAME-BY-FRAME ACTION: Six-frame heavy walk cycle with weighty alternating steps, broad arm swing and subtle torso bob. Preserve silhouette, outfit, colors, hair and accessories across all frames. The change between frames should be small and readable at native pixel scale. Output one sprite-sheet image only.
```

### BI-WALK-UP — Buto Ijo — walk facing up

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE production-oriented SPRITE SHEET image for an original 2D top-down adventure game inspired by Indonesian folklore. Use a perfectly flat solid magenta (#FF00FF) background for manual removal, uniform edge to edge with no vignette, gradient or floor. Keep the entire sprite visible in every frame, with no cropping and no cast shadow.

SPRITE SHEET LAYOUT: exactly 6 frames in ONE horizontal row, ordered chronologically from left to right, on a 16:9 landscape canvas. Each frame sits in its own SQUARE cell (final cleaned size 64×64 px) whose side equals the canvas width divided by 6; the row is centered vertically and the empty space above and below is flat magenta. Center one frame in each cell. The character occupies at most 65% of its cell's width and about 80% of its cell's height, leaving at least 15% empty magenta on each side, so frames never touch, overlap, or get cropped by a neighbor or the image edge. Same character scale, camera angle and proportions in every frame; head-top and feet stay at the same vertical positions in every frame, with the feet/base on one shared baseline. Do not add labels, numbers, grid lines, frame borders, duplicate rows, extra poses, or decorative elements. The sheet must be easy to slice into 6 equal cells.

CHARACTER: Buto Ijo. DESIGN LOCK: Buto Ijo, a huge intimidating ogre from Indonesian folklore, about twice Timun Mas's height (about 56 px tall in a 64 px cell), broad hunched shoulders, heavy barrel chest, forest-green skin (#2F5E3A / #4F8A4B / #8DBB5F), heavy brow, small cream tusks, wild messy dark-brown hair, bare chest, dark-brown waist cloth with a rope belt, bare feet; scary but suitable for a family-friendly pixel adventure; 1 px dark-brown outline.
ANIMATION: walk. FACING DIRECTION: up. FRAME-BY-FRAME ACTION: Six-frame heavy walk cycle with weighty alternating steps, broad arm swing and subtle torso bob. Preserve silhouette, outfit, colors, hair and accessories across all frames. The change between frames should be small and readable at native pixel scale. Output one sprite-sheet image only.
```

### BI-WALK-LEFT — Buto Ijo — walk facing left

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE production-oriented SPRITE SHEET image for an original 2D top-down adventure game inspired by Indonesian folklore. Use a perfectly flat solid magenta (#FF00FF) background for manual removal, uniform edge to edge with no vignette, gradient or floor. Keep the entire sprite visible in every frame, with no cropping and no cast shadow.

SPRITE SHEET LAYOUT: exactly 6 frames in ONE horizontal row, ordered chronologically from left to right, on a 16:9 landscape canvas. Each frame sits in its own SQUARE cell (final cleaned size 64×64 px) whose side equals the canvas width divided by 6; the row is centered vertically and the empty space above and below is flat magenta. Center one frame in each cell. The character occupies at most 65% of its cell's width and about 80% of its cell's height, leaving at least 15% empty magenta on each side, so frames never touch, overlap, or get cropped by a neighbor or the image edge. Same character scale, camera angle and proportions in every frame; head-top and feet stay at the same vertical positions in every frame, with the feet/base on one shared baseline. Do not add labels, numbers, grid lines, frame borders, duplicate rows, extra poses, or decorative elements. The sheet must be easy to slice into 6 equal cells.

CHARACTER: Buto Ijo. DESIGN LOCK: Buto Ijo, a huge intimidating ogre from Indonesian folklore, about twice Timun Mas's height (about 56 px tall in a 64 px cell), broad hunched shoulders, heavy barrel chest, forest-green skin (#2F5E3A / #4F8A4B / #8DBB5F), heavy brow, small cream tusks, wild messy dark-brown hair, bare chest, dark-brown waist cloth with a rope belt, bare feet; scary but suitable for a family-friendly pixel adventure; 1 px dark-brown outline.
ANIMATION: walk. FACING DIRECTION: left. FRAME-BY-FRAME ACTION: Six-frame heavy walk cycle with weighty alternating steps, broad arm swing and subtle torso bob. Preserve silhouette, outfit, colors, hair and accessories across all frames. The change between frames should be small and readable at native pixel scale. Output one sprite-sheet image only.
```

### BI-WALK-RIGHT — Buto Ijo — walk facing right

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE production-oriented SPRITE SHEET image for an original 2D top-down adventure game inspired by Indonesian folklore. Use a perfectly flat solid magenta (#FF00FF) background for manual removal, uniform edge to edge with no vignette, gradient or floor. Keep the entire sprite visible in every frame, with no cropping and no cast shadow.

SPRITE SHEET LAYOUT: exactly 6 frames in ONE horizontal row, ordered chronologically from left to right, on a 16:9 landscape canvas. Each frame sits in its own SQUARE cell (final cleaned size 64×64 px) whose side equals the canvas width divided by 6; the row is centered vertically and the empty space above and below is flat magenta. Center one frame in each cell. The character occupies at most 65% of its cell's width and about 80% of its cell's height, leaving at least 15% empty magenta on each side, so frames never touch, overlap, or get cropped by a neighbor or the image edge. Same character scale, camera angle and proportions in every frame; head-top and feet stay at the same vertical positions in every frame, with the feet/base on one shared baseline. Do not add labels, numbers, grid lines, frame borders, duplicate rows, extra poses, or decorative elements. The sheet must be easy to slice into 6 equal cells.

CHARACTER: Buto Ijo. DESIGN LOCK: Buto Ijo, a huge intimidating ogre from Indonesian folklore, about twice Timun Mas's height (about 56 px tall in a 64 px cell), broad hunched shoulders, heavy barrel chest, forest-green skin (#2F5E3A / #4F8A4B / #8DBB5F), heavy brow, small cream tusks, wild messy dark-brown hair, bare chest, dark-brown waist cloth with a rope belt, bare feet; scary but suitable for a family-friendly pixel adventure; 1 px dark-brown outline.
ANIMATION: walk. FACING DIRECTION: right. FRAME-BY-FRAME ACTION: Six-frame heavy walk cycle with weighty alternating steps, broad arm swing and subtle torso bob. Preserve silhouette, outfit, colors, hair and accessories across all frames. The change between frames should be small and readable at native pixel scale. Output one sprite-sheet image only.
```

### BI-RUN-DOWN — Buto Ijo — chase run facing down

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE production-oriented SPRITE SHEET image for an original 2D top-down adventure game inspired by Indonesian folklore. Use a perfectly flat solid magenta (#FF00FF) background for manual removal, uniform edge to edge with no vignette, gradient or floor. Keep the entire sprite visible in every frame, with no cropping and no cast shadow.

SPRITE SHEET LAYOUT: exactly 6 frames in ONE horizontal row, ordered chronologically from left to right, on a 16:9 landscape canvas. Each frame sits in its own SQUARE cell (final cleaned size 64×64 px) whose side equals the canvas width divided by 6; the row is centered vertically and the empty space above and below is flat magenta. Center one frame in each cell. The character occupies at most 65% of its cell's width and about 80% of its cell's height, leaving at least 15% empty magenta on each side, so frames never touch, overlap, or get cropped by a neighbor or the image edge. Same character scale, camera angle and proportions in every frame; head-top and feet stay at the same vertical positions in every frame, with the feet/base on one shared baseline. Do not add labels, numbers, grid lines, frame borders, duplicate rows, extra poses, or decorative elements. The sheet must be easy to slice into 6 equal cells.

CHARACTER: Buto Ijo. DESIGN LOCK: Buto Ijo, a huge intimidating ogre from Indonesian folklore, about twice Timun Mas's height (about 56 px tall in a 64 px cell), broad hunched shoulders, heavy barrel chest, forest-green skin (#2F5E3A / #4F8A4B / #8DBB5F), heavy brow, small cream tusks, wild messy dark-brown hair, bare chest, dark-brown waist cloth with a rope belt, bare feet; scary but suitable for a family-friendly pixel adventure; 1 px dark-brown outline.
ANIMATION: chase run. FACING DIRECTION: down. FRAME-BY-FRAME ACTION: Six-frame heavy chase-run cycle, aggressive forward lean, powerful alternating strides and arm pumping; keep all body parts inside each cell. Preserve silhouette, outfit, colors, hair and accessories across all frames. The change between frames should be small and readable at native pixel scale. Output one sprite-sheet image only.
```

### BI-RUN-UP — Buto Ijo — chase run facing up

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE production-oriented SPRITE SHEET image for an original 2D top-down adventure game inspired by Indonesian folklore. Use a perfectly flat solid magenta (#FF00FF) background for manual removal, uniform edge to edge with no vignette, gradient or floor. Keep the entire sprite visible in every frame, with no cropping and no cast shadow.

SPRITE SHEET LAYOUT: exactly 6 frames in ONE horizontal row, ordered chronologically from left to right, on a 16:9 landscape canvas. Each frame sits in its own SQUARE cell (final cleaned size 64×64 px) whose side equals the canvas width divided by 6; the row is centered vertically and the empty space above and below is flat magenta. Center one frame in each cell. The character occupies at most 65% of its cell's width and about 80% of its cell's height, leaving at least 15% empty magenta on each side, so frames never touch, overlap, or get cropped by a neighbor or the image edge. Same character scale, camera angle and proportions in every frame; head-top and feet stay at the same vertical positions in every frame, with the feet/base on one shared baseline. Do not add labels, numbers, grid lines, frame borders, duplicate rows, extra poses, or decorative elements. The sheet must be easy to slice into 6 equal cells.

CHARACTER: Buto Ijo. DESIGN LOCK: Buto Ijo, a huge intimidating ogre from Indonesian folklore, about twice Timun Mas's height (about 56 px tall in a 64 px cell), broad hunched shoulders, heavy barrel chest, forest-green skin (#2F5E3A / #4F8A4B / #8DBB5F), heavy brow, small cream tusks, wild messy dark-brown hair, bare chest, dark-brown waist cloth with a rope belt, bare feet; scary but suitable for a family-friendly pixel adventure; 1 px dark-brown outline.
ANIMATION: chase run. FACING DIRECTION: up. FRAME-BY-FRAME ACTION: Six-frame heavy chase-run cycle, aggressive forward lean, powerful alternating strides and arm pumping; keep all body parts inside each cell. Preserve silhouette, outfit, colors, hair and accessories across all frames. The change between frames should be small and readable at native pixel scale. Output one sprite-sheet image only.
```

### BI-RUN-LEFT — Buto Ijo — chase run facing left

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE production-oriented SPRITE SHEET image for an original 2D top-down adventure game inspired by Indonesian folklore. Use a perfectly flat solid magenta (#FF00FF) background for manual removal, uniform edge to edge with no vignette, gradient or floor. Keep the entire sprite visible in every frame, with no cropping and no cast shadow.

SPRITE SHEET LAYOUT: exactly 6 frames in ONE horizontal row, ordered chronologically from left to right, on a 16:9 landscape canvas. Each frame sits in its own SQUARE cell (final cleaned size 64×64 px) whose side equals the canvas width divided by 6; the row is centered vertically and the empty space above and below is flat magenta. Center one frame in each cell. The character occupies at most 65% of its cell's width and about 80% of its cell's height, leaving at least 15% empty magenta on each side, so frames never touch, overlap, or get cropped by a neighbor or the image edge. Same character scale, camera angle and proportions in every frame; head-top and feet stay at the same vertical positions in every frame, with the feet/base on one shared baseline. Do not add labels, numbers, grid lines, frame borders, duplicate rows, extra poses, or decorative elements. The sheet must be easy to slice into 6 equal cells.

CHARACTER: Buto Ijo. DESIGN LOCK: Buto Ijo, a huge intimidating ogre from Indonesian folklore, about twice Timun Mas's height (about 56 px tall in a 64 px cell), broad hunched shoulders, heavy barrel chest, forest-green skin (#2F5E3A / #4F8A4B / #8DBB5F), heavy brow, small cream tusks, wild messy dark-brown hair, bare chest, dark-brown waist cloth with a rope belt, bare feet; scary but suitable for a family-friendly pixel adventure; 1 px dark-brown outline.
ANIMATION: chase run. FACING DIRECTION: left. FRAME-BY-FRAME ACTION: Six-frame heavy chase-run cycle, aggressive forward lean, powerful alternating strides and arm pumping; keep all body parts inside each cell. Preserve silhouette, outfit, colors, hair and accessories across all frames. The change between frames should be small and readable at native pixel scale. Output one sprite-sheet image only.
```

### BI-RUN-RIGHT — Buto Ijo — chase run facing right

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE production-oriented SPRITE SHEET image for an original 2D top-down adventure game inspired by Indonesian folklore. Use a perfectly flat solid magenta (#FF00FF) background for manual removal, uniform edge to edge with no vignette, gradient or floor. Keep the entire sprite visible in every frame, with no cropping and no cast shadow.

SPRITE SHEET LAYOUT: exactly 6 frames in ONE horizontal row, ordered chronologically from left to right, on a 16:9 landscape canvas. Each frame sits in its own SQUARE cell (final cleaned size 64×64 px) whose side equals the canvas width divided by 6; the row is centered vertically and the empty space above and below is flat magenta. Center one frame in each cell. The character occupies at most 65% of its cell's width and about 80% of its cell's height, leaving at least 15% empty magenta on each side, so frames never touch, overlap, or get cropped by a neighbor or the image edge. Same character scale, camera angle and proportions in every frame; head-top and feet stay at the same vertical positions in every frame, with the feet/base on one shared baseline. Do not add labels, numbers, grid lines, frame borders, duplicate rows, extra poses, or decorative elements. The sheet must be easy to slice into 6 equal cells.

CHARACTER: Buto Ijo. DESIGN LOCK: Buto Ijo, a huge intimidating ogre from Indonesian folklore, about twice Timun Mas's height (about 56 px tall in a 64 px cell), broad hunched shoulders, heavy barrel chest, forest-green skin (#2F5E3A / #4F8A4B / #8DBB5F), heavy brow, small cream tusks, wild messy dark-brown hair, bare chest, dark-brown waist cloth with a rope belt, bare feet; scary but suitable for a family-friendly pixel adventure; 1 px dark-brown outline.
ANIMATION: chase run. FACING DIRECTION: right. FRAME-BY-FRAME ACTION: Six-frame heavy chase-run cycle, aggressive forward lean, powerful alternating strides and arm pumping; keep all body parts inside each cell. Preserve silhouette, outfit, colors, hair and accessories across all frames. The change between frames should be small and readable at native pixel scale. Output one sprite-sheet image only.
```

### BI-ATTACK-DOWN — Buto Ijo — attack facing down

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE production-oriented SPRITE SHEET image for an original 2D top-down adventure game inspired by Indonesian folklore. Use a perfectly flat solid magenta (#FF00FF) background for manual removal, uniform edge to edge with no vignette, gradient or floor. Keep the entire sprite visible in every frame, with no cropping and no cast shadow.

SPRITE SHEET LAYOUT: exactly 6 frames in ONE horizontal row, ordered chronologically from left to right, on a 16:9 landscape canvas. Each frame sits in its own SQUARE cell (final cleaned size 64×64 px) whose side equals the canvas width divided by 6; the row is centered vertically and the empty space above and below is flat magenta. Center one frame in each cell. The character occupies at most 65% of its cell's width and about 80% of its cell's height, leaving at least 15% empty magenta on each side, so frames never touch, overlap, or get cropped by a neighbor or the image edge. Same character scale, camera angle and proportions in every frame; head-top and feet stay at the same vertical positions in every frame, with the feet/base on one shared baseline. Do not add labels, numbers, grid lines, frame borders, duplicate rows, extra poses, or decorative elements. The sheet must be easy to slice into 6 equal cells.

CHARACTER: Buto Ijo. DESIGN LOCK: Buto Ijo, a huge intimidating ogre from Indonesian folklore, about twice Timun Mas's height (about 56 px tall in a 64 px cell), broad hunched shoulders, heavy barrel chest, forest-green skin (#2F5E3A / #4F8A4B / #8DBB5F), heavy brow, small cream tusks, wild messy dark-brown hair, bare chest, dark-brown waist cloth with a rope belt, bare feet; scary but suitable for a family-friendly pixel adventure; 1 px dark-brown outline.
ANIMATION: heavy melee swing attack. FACING DIRECTION: down. FRAME-BY-FRAME ACTION: Wind-up, arm pulls back, powerful swing, impact pose, follow-through, return to ready stance. No weapon unless specified; no blood. Preserve silhouette, outfit, colors, hair and accessories across all frames. The change between frames should be small and readable at native pixel scale. Output one sprite-sheet image only.
```

### BI-ATTACK-LEFT — Buto Ijo — attack facing left

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE production-oriented SPRITE SHEET image for an original 2D top-down adventure game inspired by Indonesian folklore. Use a perfectly flat solid magenta (#FF00FF) background for manual removal, uniform edge to edge with no vignette, gradient or floor. Keep the entire sprite visible in every frame, with no cropping and no cast shadow.

SPRITE SHEET LAYOUT: exactly 6 frames in ONE horizontal row, ordered chronologically from left to right, on a 16:9 landscape canvas. Each frame sits in its own SQUARE cell (final cleaned size 64×64 px) whose side equals the canvas width divided by 6; the row is centered vertically and the empty space above and below is flat magenta. Center one frame in each cell. The character occupies at most 65% of its cell's width and about 80% of its cell's height, leaving at least 15% empty magenta on each side, so frames never touch, overlap, or get cropped by a neighbor or the image edge. Same character scale, camera angle and proportions in every frame; head-top and feet stay at the same vertical positions in every frame, with the feet/base on one shared baseline. Do not add labels, numbers, grid lines, frame borders, duplicate rows, extra poses, or decorative elements. The sheet must be easy to slice into 6 equal cells.

CHARACTER: Buto Ijo. DESIGN LOCK: Buto Ijo, a huge intimidating ogre from Indonesian folklore, about twice Timun Mas's height (about 56 px tall in a 64 px cell), broad hunched shoulders, heavy barrel chest, forest-green skin (#2F5E3A / #4F8A4B / #8DBB5F), heavy brow, small cream tusks, wild messy dark-brown hair, bare chest, dark-brown waist cloth with a rope belt, bare feet; scary but suitable for a family-friendly pixel adventure; 1 px dark-brown outline.
ANIMATION: heavy melee swing attack. FACING DIRECTION: left. FRAME-BY-FRAME ACTION: Wind-up, arm pulls back, powerful swing, impact pose, follow-through, return to ready stance. No weapon unless specified; no blood. Preserve silhouette, outfit, colors, hair and accessories across all frames. The change between frames should be small and readable at native pixel scale. Output one sprite-sheet image only.
```

### BI-ATTACK-RIGHT — Buto Ijo — attack facing right

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE production-oriented SPRITE SHEET image for an original 2D top-down adventure game inspired by Indonesian folklore. Use a perfectly flat solid magenta (#FF00FF) background for manual removal, uniform edge to edge with no vignette, gradient or floor. Keep the entire sprite visible in every frame, with no cropping and no cast shadow.

SPRITE SHEET LAYOUT: exactly 6 frames in ONE horizontal row, ordered chronologically from left to right, on a 16:9 landscape canvas. Each frame sits in its own SQUARE cell (final cleaned size 64×64 px) whose side equals the canvas width divided by 6; the row is centered vertically and the empty space above and below is flat magenta. Center one frame in each cell. The character occupies at most 65% of its cell's width and about 80% of its cell's height, leaving at least 15% empty magenta on each side, so frames never touch, overlap, or get cropped by a neighbor or the image edge. Same character scale, camera angle and proportions in every frame; head-top and feet stay at the same vertical positions in every frame, with the feet/base on one shared baseline. Do not add labels, numbers, grid lines, frame borders, duplicate rows, extra poses, or decorative elements. The sheet must be easy to slice into 6 equal cells.

CHARACTER: Buto Ijo. DESIGN LOCK: Buto Ijo, a huge intimidating ogre from Indonesian folklore, about twice Timun Mas's height (about 56 px tall in a 64 px cell), broad hunched shoulders, heavy barrel chest, forest-green skin (#2F5E3A / #4F8A4B / #8DBB5F), heavy brow, small cream tusks, wild messy dark-brown hair, bare chest, dark-brown waist cloth with a rope belt, bare feet; scary but suitable for a family-friendly pixel adventure; 1 px dark-brown outline.
ANIMATION: heavy melee swing attack. FACING DIRECTION: right. FRAME-BY-FRAME ACTION: Wind-up, arm pulls back, powerful swing, impact pose, follow-through, return to ready stance. No weapon unless specified; no blood. Preserve silhouette, outfit, colors, hair and accessories across all frames. The change between frames should be small and readable at native pixel scale. Output one sprite-sheet image only.
```

### BI-STUNNED — Buto Ijo — stunned

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE production-oriented SPRITE SHEET image for an original 2D top-down adventure game inspired by Indonesian folklore. Use a perfectly flat solid magenta (#FF00FF) background for manual removal, uniform edge to edge with no vignette, gradient or floor. Keep the entire sprite visible in every frame, with no cropping and no cast shadow.

SPRITE SHEET LAYOUT: exactly 4 frames in ONE horizontal row, ordered chronologically from left to right, on a 16:9 landscape canvas. Each frame sits in its own SQUARE cell (final cleaned size 64×64 px) whose side equals the canvas width divided by 4; the row is centered vertically and the empty space above and below is flat magenta. Center one frame in each cell. The character occupies at most 65% of its cell's width and about 80% of its cell's height, leaving at least 15% empty magenta on each side, so frames never touch, overlap, or get cropped by a neighbor or the image edge. Same character scale, camera angle and proportions in every frame; head-top and feet stay at the same vertical positions in every frame, with the feet/base on one shared baseline. Do not add labels, numbers, grid lines, frame borders, duplicate rows, extra poses, or decorative elements. The sheet must be easy to slice into 4 equal cells.

CHARACTER: Buto Ijo. DESIGN LOCK: Buto Ijo, a huge intimidating ogre from Indonesian folklore, about twice Timun Mas's height (about 56 px tall in a 64 px cell), broad hunched shoulders, heavy barrel chest, forest-green skin (#2F5E3A / #4F8A4B / #8DBB5F), heavy brow, small cream tusks, wild messy dark-brown hair, bare chest, dark-brown waist cloth with a rope belt, bare feet; scary but suitable for a family-friendly pixel adventure; 1 px dark-brown outline.
ANIMATION: short stunned reaction. FACING DIRECTION: facing down. FRAME-BY-FRAME ACTION: Recoil, wobble with dazed posture, knees soften and head droops briefly, recover toward standing. Optional tiny star shapes are not needed because VFX are separate. Preserve silhouette, outfit, colors, hair and accessories across all frames. The change between frames should be small and readable at native pixel scale. Output one sprite-sheet image only.
```

### BI-TRAPPED — Buto Ijo — trapped in mud

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE production-oriented SPRITE SHEET image for an original 2D top-down adventure game inspired by Indonesian folklore. Use a perfectly flat solid magenta (#FF00FF) background for manual removal, uniform edge to edge with no vignette, gradient or floor. Keep the entire sprite visible in every frame, with no cropping and no cast shadow.

SPRITE SHEET LAYOUT: exactly 4 frames in ONE horizontal row, ordered chronologically from left to right, on a 16:9 landscape canvas. Each frame sits in its own SQUARE cell (final cleaned size 64×64 px) whose side equals the canvas width divided by 4; the row is centered vertically and the empty space above and below is flat magenta. Center one frame in each cell. The character occupies at most 65% of its cell's width and about 80% of its cell's height, leaving at least 15% empty magenta on each side, so frames never touch, overlap, or get cropped by a neighbor or the image edge. Same character scale, camera angle and proportions in every frame; head-top and feet stay at the same vertical positions in every frame, with the feet/base on one shared baseline. Do not add labels, numbers, grid lines, frame borders, duplicate rows, extra poses, or decorative elements. The sheet must be easy to slice into 4 equal cells.

CHARACTER: Buto Ijo. DESIGN LOCK: Buto Ijo, a huge intimidating ogre from Indonesian folklore, about twice Timun Mas's height (about 56 px tall in a 64 px cell), broad hunched shoulders, heavy barrel chest, forest-green skin (#2F5E3A / #4F8A4B / #8DBB5F), heavy brow, small cream tusks, wild messy dark-brown hair, bare chest, dark-brown waist cloth with a rope belt, bare feet; scary but suitable for a family-friendly pixel adventure; 1 px dark-brown outline.
ANIMATION: struggling while trapped waist-down. FACING DIRECTION: facing down. FRAME-BY-FRAME ACTION: Arms lift in surprise, struggle left, struggle right, exhausted frustrated pose. Keep lower body partly obscured by a separate mud effect; do not draw a background. Preserve silhouette, outfit, colors, hair and accessories across all frames. The change between frames should be small and readable at native pixel scale. Output one sprite-sheet image only.
```

### BI-RETREAT — Buto Ijo — retreating

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE production-oriented SPRITE SHEET image for an original 2D top-down adventure game inspired by Indonesian folklore. Use a perfectly flat solid magenta (#FF00FF) background for manual removal, uniform edge to edge with no vignette, gradient or floor. Keep the entire sprite visible in every frame, with no cropping and no cast shadow.

SPRITE SHEET LAYOUT: exactly 6 frames in ONE horizontal row, ordered chronologically from left to right, on a 16:9 landscape canvas. Each frame sits in its own SQUARE cell (final cleaned size 64×64 px) whose side equals the canvas width divided by 6; the row is centered vertically and the empty space above and below is flat magenta. Center one frame in each cell. The character occupies at most 65% of its cell's width and about 80% of its cell's height, leaving at least 15% empty magenta on each side, so frames never touch, overlap, or get cropped by a neighbor or the image edge. Same character scale, camera angle and proportions in every frame; head-top and feet stay at the same vertical positions in every frame, with the feet/base on one shared baseline. Do not add labels, numbers, grid lines, frame borders, duplicate rows, extra poses, or decorative elements. The sheet must be easy to slice into 6 equal cells.

CHARACTER: Buto Ijo. DESIGN LOCK: Buto Ijo, a huge intimidating ogre from Indonesian folklore, about twice Timun Mas's height (about 56 px tall in a 64 px cell), broad hunched shoulders, heavy barrel chest, forest-green skin (#2F5E3A / #4F8A4B / #8DBB5F), heavy brow, small cream tusks, wild messy dark-brown hair, bare chest, dark-brown waist cloth with a rope belt, bare feet; scary but suitable for a family-friendly pixel adventure; 1 px dark-brown outline.
ANIMATION: retreat/run away. FACING DIRECTION: facing up (moving away from camera). FRAME-BY-FRAME ACTION: Six-frame retreat run cycle with hurried heavy steps and arms moving for balance; keep the back design consistent. Preserve silhouette, outfit, colors, hair and accessories across all frames. The change between frames should be small and readable at native pixel scale. Output one sprite-sheet image only.
```

### MS-IDLE-DOWN — Mbok Srini — idle facing down

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE production-oriented SPRITE SHEET image for an original 2D top-down adventure game inspired by Indonesian folklore. Use a perfectly flat solid magenta (#FF00FF) background for manual removal, uniform edge to edge with no vignette, gradient or floor. Keep the entire sprite visible in every frame, with no cropping and no cast shadow.

SPRITE SHEET LAYOUT: exactly 4 frames in ONE horizontal row, ordered chronologically from left to right, on a 16:9 landscape canvas. Each frame sits in its own SQUARE cell (final cleaned size 32×32 px) whose side equals the canvas width divided by 4; the row is centered vertically and the empty space above and below is flat magenta. Center one frame in each cell. The character occupies at most 65% of its cell's width and about 80% of its cell's height, leaving at least 15% empty magenta on each side, so frames never touch, overlap, or get cropped by a neighbor or the image edge. Same character scale, camera angle and proportions in every frame; head-top and feet stay at the same vertical positions in every frame, with the feet/base on one shared baseline. Do not add labels, numbers, grid lines, frame borders, duplicate rows, extra poses, or decorative elements. The sheet must be easy to slice into 4 equal cells.

CHARACTER: Mbok Srini. DESIGN LOCK: Mbok Srini, a kind middle-aged Javanese village woman, chibi proportions like Timun Mas (about 27 px tall in a 32 px cell), warm medium-brown skin, gentle face, dark hair in a low bun under a simple brown head cloth, cream kebaya-style blouse, earthy brown batik sarong, muted forest-green shawl over one shoulder, bare feet; caring village-mother silhouette; 1 px dark-brown outline.
ANIMATION: gentle idle breathing loop. FACING DIRECTION: down. FRAME-BY-FRAME ACTION: Subtle breathing, a small head movement, a slight hand/sleeve movement, return to neutral. Calm and warm. Preserve silhouette, outfit, colors, hair and accessories across all frames. The change between frames should be small and readable at native pixel scale. Output one sprite-sheet image only.
```

### MS-IDLE-UP — Mbok Srini — idle facing up

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE production-oriented SPRITE SHEET image for an original 2D top-down adventure game inspired by Indonesian folklore. Use a perfectly flat solid magenta (#FF00FF) background for manual removal, uniform edge to edge with no vignette, gradient or floor. Keep the entire sprite visible in every frame, with no cropping and no cast shadow.

SPRITE SHEET LAYOUT: exactly 4 frames in ONE horizontal row, ordered chronologically from left to right, on a 16:9 landscape canvas. Each frame sits in its own SQUARE cell (final cleaned size 32×32 px) whose side equals the canvas width divided by 4; the row is centered vertically and the empty space above and below is flat magenta. Center one frame in each cell. The character occupies at most 65% of its cell's width and about 80% of its cell's height, leaving at least 15% empty magenta on each side, so frames never touch, overlap, or get cropped by a neighbor or the image edge. Same character scale, camera angle and proportions in every frame; head-top and feet stay at the same vertical positions in every frame, with the feet/base on one shared baseline. Do not add labels, numbers, grid lines, frame borders, duplicate rows, extra poses, or decorative elements. The sheet must be easy to slice into 4 equal cells.

CHARACTER: Mbok Srini. DESIGN LOCK: Mbok Srini, a kind middle-aged Javanese village woman, chibi proportions like Timun Mas (about 27 px tall in a 32 px cell), warm medium-brown skin, gentle face, dark hair in a low bun under a simple brown head cloth, cream kebaya-style blouse, earthy brown batik sarong, muted forest-green shawl over one shoulder, bare feet; caring village-mother silhouette; 1 px dark-brown outline.
ANIMATION: gentle idle breathing loop. FACING DIRECTION: up. FRAME-BY-FRAME ACTION: Subtle breathing, a small head movement, a slight hand/sleeve movement, return to neutral. Calm and warm. Preserve silhouette, outfit, colors, hair and accessories across all frames. The change between frames should be small and readable at native pixel scale. Output one sprite-sheet image only.
```

### MS-IDLE-LEFT — Mbok Srini — idle facing left

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE production-oriented SPRITE SHEET image for an original 2D top-down adventure game inspired by Indonesian folklore. Use a perfectly flat solid magenta (#FF00FF) background for manual removal, uniform edge to edge with no vignette, gradient or floor. Keep the entire sprite visible in every frame, with no cropping and no cast shadow.

SPRITE SHEET LAYOUT: exactly 4 frames in ONE horizontal row, ordered chronologically from left to right, on a 16:9 landscape canvas. Each frame sits in its own SQUARE cell (final cleaned size 32×32 px) whose side equals the canvas width divided by 4; the row is centered vertically and the empty space above and below is flat magenta. Center one frame in each cell. The character occupies at most 65% of its cell's width and about 80% of its cell's height, leaving at least 15% empty magenta on each side, so frames never touch, overlap, or get cropped by a neighbor or the image edge. Same character scale, camera angle and proportions in every frame; head-top and feet stay at the same vertical positions in every frame, with the feet/base on one shared baseline. Do not add labels, numbers, grid lines, frame borders, duplicate rows, extra poses, or decorative elements. The sheet must be easy to slice into 4 equal cells.

CHARACTER: Mbok Srini. DESIGN LOCK: Mbok Srini, a kind middle-aged Javanese village woman, chibi proportions like Timun Mas (about 27 px tall in a 32 px cell), warm medium-brown skin, gentle face, dark hair in a low bun under a simple brown head cloth, cream kebaya-style blouse, earthy brown batik sarong, muted forest-green shawl over one shoulder, bare feet; caring village-mother silhouette; 1 px dark-brown outline.
ANIMATION: gentle idle breathing loop. FACING DIRECTION: left. FRAME-BY-FRAME ACTION: Subtle breathing, a small head movement, a slight hand/sleeve movement, return to neutral. Calm and warm. Preserve silhouette, outfit, colors, hair and accessories across all frames. The change between frames should be small and readable at native pixel scale. Output one sprite-sheet image only.
```

### MS-IDLE-RIGHT — Mbok Srini — idle facing right

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE production-oriented SPRITE SHEET image for an original 2D top-down adventure game inspired by Indonesian folklore. Use a perfectly flat solid magenta (#FF00FF) background for manual removal, uniform edge to edge with no vignette, gradient or floor. Keep the entire sprite visible in every frame, with no cropping and no cast shadow.

SPRITE SHEET LAYOUT: exactly 4 frames in ONE horizontal row, ordered chronologically from left to right, on a 16:9 landscape canvas. Each frame sits in its own SQUARE cell (final cleaned size 32×32 px) whose side equals the canvas width divided by 4; the row is centered vertically and the empty space above and below is flat magenta. Center one frame in each cell. The character occupies at most 65% of its cell's width and about 80% of its cell's height, leaving at least 15% empty magenta on each side, so frames never touch, overlap, or get cropped by a neighbor or the image edge. Same character scale, camera angle and proportions in every frame; head-top and feet stay at the same vertical positions in every frame, with the feet/base on one shared baseline. Do not add labels, numbers, grid lines, frame borders, duplicate rows, extra poses, or decorative elements. The sheet must be easy to slice into 4 equal cells.

CHARACTER: Mbok Srini. DESIGN LOCK: Mbok Srini, a kind middle-aged Javanese village woman, chibi proportions like Timun Mas (about 27 px tall in a 32 px cell), warm medium-brown skin, gentle face, dark hair in a low bun under a simple brown head cloth, cream kebaya-style blouse, earthy brown batik sarong, muted forest-green shawl over one shoulder, bare feet; caring village-mother silhouette; 1 px dark-brown outline.
ANIMATION: gentle idle breathing loop. FACING DIRECTION: right. FRAME-BY-FRAME ACTION: Subtle breathing, a small head movement, a slight hand/sleeve movement, return to neutral. Calm and warm. Preserve silhouette, outfit, colors, hair and accessories across all frames. The change between frames should be small and readable at native pixel scale. Output one sprite-sheet image only.
```

### MS-TALK — Mbok Srini — talking gesture

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE production-oriented SPRITE SHEET image for an original 2D top-down adventure game inspired by Indonesian folklore. Use a perfectly flat solid magenta (#FF00FF) background for manual removal, uniform edge to edge with no vignette, gradient or floor. Keep the entire sprite visible in every frame, with no cropping and no cast shadow.

SPRITE SHEET LAYOUT: exactly 4 frames in ONE horizontal row, ordered chronologically from left to right, on a 16:9 landscape canvas. Each frame sits in its own SQUARE cell (final cleaned size 32×32 px) whose side equals the canvas width divided by 4; the row is centered vertically and the empty space above and below is flat magenta. Center one frame in each cell. The character occupies at most 65% of its cell's width and about 80% of its cell's height, leaving at least 15% empty magenta on each side, so frames never touch, overlap, or get cropped by a neighbor or the image edge. Same character scale, camera angle and proportions in every frame; head-top and feet stay at the same vertical positions in every frame, with the feet/base on one shared baseline. Do not add labels, numbers, grid lines, frame borders, duplicate rows, extra poses, or decorative elements. The sheet must be easy to slice into 4 equal cells.

CHARACTER: Mbok Srini. DESIGN LOCK: Mbok Srini, a kind middle-aged Javanese village woman, chibi proportions like Timun Mas (about 27 px tall in a 32 px cell), warm medium-brown skin, gentle face, dark hair in a low bun under a simple brown head cloth, cream kebaya-style blouse, earthy brown batik sarong, muted forest-green shawl over one shoulder, bare feet; caring village-mother silhouette; 1 px dark-brown outline.
ANIMATION: gentle talking gesture. FACING DIRECTION: facing down. FRAME-BY-FRAME ACTION: Neutral, one hand rises to explain, small expressive gesture, return to neutral. Friendly worried-mother expression. Preserve silhouette, outfit, colors, hair and accessories across all frames. The change between frames should be small and readable at native pixel scale. Output one sprite-sheet image only.
```

### MS-GIVE — Mbok Srini — giving an item

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE production-oriented SPRITE SHEET image for an original 2D top-down adventure game inspired by Indonesian folklore. Use a perfectly flat solid magenta (#FF00FF) background for manual removal, uniform edge to edge with no vignette, gradient or floor. Keep the entire sprite visible in every frame, with no cropping and no cast shadow.

SPRITE SHEET LAYOUT: exactly 4 frames in ONE horizontal row, ordered chronologically from left to right, on a 16:9 landscape canvas. Each frame sits in its own SQUARE cell (final cleaned size 32×32 px) whose side equals the canvas width divided by 4; the row is centered vertically and the empty space above and below is flat magenta. Center one frame in each cell. The character occupies at most 65% of its cell's width and about 80% of its cell's height, leaving at least 15% empty magenta on each side, so frames never touch, overlap, or get cropped by a neighbor or the image edge. Same character scale, camera angle and proportions in every frame; head-top and feet stay at the same vertical positions in every frame, with the feet/base on one shared baseline. Do not add labels, numbers, grid lines, frame borders, duplicate rows, extra poses, or decorative elements. The sheet must be easy to slice into 4 equal cells.

CHARACTER: Mbok Srini. DESIGN LOCK: Mbok Srini, a kind middle-aged Javanese village woman, chibi proportions like Timun Mas (about 27 px tall in a 32 px cell), warm medium-brown skin, gentle face, dark hair in a low bun under a simple brown head cloth, cream kebaya-style blouse, earthy brown batik sarong, muted forest-green shawl over one shoulder, bare feet; caring village-mother silhouette; 1 px dark-brown outline.
ANIMATION: handing a small magical item to someone. FACING DIRECTION: facing down. FRAME-BY-FRAME ACTION: Hands prepare item, extend both hands forward, release item to recipient, return hands toward body. Item may be omitted for separate compositing. Preserve silhouette, outfit, colors, hair and accessories across all frames. The change between frames should be small and readable at native pixel scale. Output one sprite-sheet image only.
```

### MS-WORRIED — Mbok Srini — worried reaction

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE production-oriented SPRITE SHEET image for an original 2D top-down adventure game inspired by Indonesian folklore. Use a perfectly flat solid magenta (#FF00FF) background for manual removal, uniform edge to edge with no vignette, gradient or floor. Keep the entire sprite visible in every frame, with no cropping and no cast shadow.

SPRITE SHEET LAYOUT: exactly 4 frames in ONE horizontal row, ordered chronologically from left to right, on a 16:9 landscape canvas. Each frame sits in its own SQUARE cell (final cleaned size 32×32 px) whose side equals the canvas width divided by 4; the row is centered vertically and the empty space above and below is flat magenta. Center one frame in each cell. The character occupies at most 65% of its cell's width and about 80% of its cell's height, leaving at least 15% empty magenta on each side, so frames never touch, overlap, or get cropped by a neighbor or the image edge. Same character scale, camera angle and proportions in every frame; head-top and feet stay at the same vertical positions in every frame, with the feet/base on one shared baseline. Do not add labels, numbers, grid lines, frame borders, duplicate rows, extra poses, or decorative elements. The sheet must be easy to slice into 4 equal cells.

CHARACTER: Mbok Srini. DESIGN LOCK: Mbok Srini, a kind middle-aged Javanese village woman, chibi proportions like Timun Mas (about 27 px tall in a 32 px cell), warm medium-brown skin, gentle face, dark hair in a low bun under a simple brown head cloth, cream kebaya-style blouse, earthy brown batik sarong, muted forest-green shawl over one shoulder, bare feet; caring village-mother silhouette; 1 px dark-brown outline.
ANIMATION: worried reaction loop. FACING DIRECTION: facing down. FRAME-BY-FRAME ACTION: Concerned neutral, hands rise slightly, anxious glance/head movement, return to worried idle. No dramatic distortion. Preserve silhouette, outfit, colors, hair and accessories across all frames. The change between frames should be small and readable at native pixel scale. Output one sprite-sheet image only.
```

### NPC-A-IDLE-DOWN — Village NPC variant A — idle facing down

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE production-oriented SPRITE SHEET image for an original 2D top-down adventure game inspired by Indonesian folklore. Use a perfectly flat solid magenta (#FF00FF) background for manual removal, uniform edge to edge with no vignette, gradient or floor. Keep the entire sprite visible in every frame, with no cropping and no cast shadow.

SPRITE SHEET LAYOUT: exactly 4 frames in ONE horizontal row, ordered chronologically from left to right, on a 16:9 landscape canvas. Each frame sits in its own SQUARE cell (final cleaned size 32×32 px) whose side equals the canvas width divided by 4; the row is centered vertically and the empty space above and below is flat magenta. Center one frame in each cell. The character occupies at most 65% of its cell's width and about 80% of its cell's height, leaving at least 15% empty magenta on each side, so frames never touch, overlap, or get cropped by a neighbor or the image edge. Same character scale, camera angle and proportions in every frame; head-top and feet stay at the same vertical positions in every frame, with the feet/base on one shared baseline. Do not add labels, numbers, grid lines, frame borders, duplicate rows, extra poses, or decorative elements. The sheet must be easy to slice into 4 equal cells.

CHARACTER: Village NPC variant A. DESIGN LOCK: A a generic adult Javanese village resident, chibi proportions like Timun Mas (about 26 px tall in a 32 px cell), simple modest cream and earthy-brown traditional rural clothing, warm medium-brown skin, bare feet, distinct silhouette from the main cast, no modern accessories; 1 px dark-brown outline.
ANIMATION: idle loop. FACING DIRECTION: down. FRAME-BY-FRAME ACTION: Subtle breathing, slight shift of weight, return to starting pose. Preserve silhouette, outfit, colors, hair and accessories across all frames. The change between frames should be small and readable at native pixel scale. Output one sprite-sheet image only.
```

### NPC-A-IDLE-UP — Village NPC variant A — idle facing up

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE production-oriented SPRITE SHEET image for an original 2D top-down adventure game inspired by Indonesian folklore. Use a perfectly flat solid magenta (#FF00FF) background for manual removal, uniform edge to edge with no vignette, gradient or floor. Keep the entire sprite visible in every frame, with no cropping and no cast shadow.

SPRITE SHEET LAYOUT: exactly 4 frames in ONE horizontal row, ordered chronologically from left to right, on a 16:9 landscape canvas. Each frame sits in its own SQUARE cell (final cleaned size 32×32 px) whose side equals the canvas width divided by 4; the row is centered vertically and the empty space above and below is flat magenta. Center one frame in each cell. The character occupies at most 65% of its cell's width and about 80% of its cell's height, leaving at least 15% empty magenta on each side, so frames never touch, overlap, or get cropped by a neighbor or the image edge. Same character scale, camera angle and proportions in every frame; head-top and feet stay at the same vertical positions in every frame, with the feet/base on one shared baseline. Do not add labels, numbers, grid lines, frame borders, duplicate rows, extra poses, or decorative elements. The sheet must be easy to slice into 4 equal cells.

CHARACTER: Village NPC variant A. DESIGN LOCK: A a generic adult Javanese village resident, chibi proportions like Timun Mas (about 26 px tall in a 32 px cell), simple modest cream and earthy-brown traditional rural clothing, warm medium-brown skin, bare feet, distinct silhouette from the main cast, no modern accessories; 1 px dark-brown outline.
ANIMATION: idle loop. FACING DIRECTION: up. FRAME-BY-FRAME ACTION: Subtle breathing, slight shift of weight, return to starting pose. Preserve silhouette, outfit, colors, hair and accessories across all frames. The change between frames should be small and readable at native pixel scale. Output one sprite-sheet image only.
```

### NPC-A-IDLE-LEFT — Village NPC variant A — idle facing left

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE production-oriented SPRITE SHEET image for an original 2D top-down adventure game inspired by Indonesian folklore. Use a perfectly flat solid magenta (#FF00FF) background for manual removal, uniform edge to edge with no vignette, gradient or floor. Keep the entire sprite visible in every frame, with no cropping and no cast shadow.

SPRITE SHEET LAYOUT: exactly 4 frames in ONE horizontal row, ordered chronologically from left to right, on a 16:9 landscape canvas. Each frame sits in its own SQUARE cell (final cleaned size 32×32 px) whose side equals the canvas width divided by 4; the row is centered vertically and the empty space above and below is flat magenta. Center one frame in each cell. The character occupies at most 65% of its cell's width and about 80% of its cell's height, leaving at least 15% empty magenta on each side, so frames never touch, overlap, or get cropped by a neighbor or the image edge. Same character scale, camera angle and proportions in every frame; head-top and feet stay at the same vertical positions in every frame, with the feet/base on one shared baseline. Do not add labels, numbers, grid lines, frame borders, duplicate rows, extra poses, or decorative elements. The sheet must be easy to slice into 4 equal cells.

CHARACTER: Village NPC variant A. DESIGN LOCK: A a generic adult Javanese village resident, chibi proportions like Timun Mas (about 26 px tall in a 32 px cell), simple modest cream and earthy-brown traditional rural clothing, warm medium-brown skin, bare feet, distinct silhouette from the main cast, no modern accessories; 1 px dark-brown outline.
ANIMATION: idle loop. FACING DIRECTION: left. FRAME-BY-FRAME ACTION: Subtle breathing, slight shift of weight, return to starting pose. Preserve silhouette, outfit, colors, hair and accessories across all frames. The change between frames should be small and readable at native pixel scale. Output one sprite-sheet image only.
```

### NPC-A-IDLE-RIGHT — Village NPC variant A — idle facing right

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE production-oriented SPRITE SHEET image for an original 2D top-down adventure game inspired by Indonesian folklore. Use a perfectly flat solid magenta (#FF00FF) background for manual removal, uniform edge to edge with no vignette, gradient or floor. Keep the entire sprite visible in every frame, with no cropping and no cast shadow.

SPRITE SHEET LAYOUT: exactly 4 frames in ONE horizontal row, ordered chronologically from left to right, on a 16:9 landscape canvas. Each frame sits in its own SQUARE cell (final cleaned size 32×32 px) whose side equals the canvas width divided by 4; the row is centered vertically and the empty space above and below is flat magenta. Center one frame in each cell. The character occupies at most 65% of its cell's width and about 80% of its cell's height, leaving at least 15% empty magenta on each side, so frames never touch, overlap, or get cropped by a neighbor or the image edge. Same character scale, camera angle and proportions in every frame; head-top and feet stay at the same vertical positions in every frame, with the feet/base on one shared baseline. Do not add labels, numbers, grid lines, frame borders, duplicate rows, extra poses, or decorative elements. The sheet must be easy to slice into 4 equal cells.

CHARACTER: Village NPC variant A. DESIGN LOCK: A a generic adult Javanese village resident, chibi proportions like Timun Mas (about 26 px tall in a 32 px cell), simple modest cream and earthy-brown traditional rural clothing, warm medium-brown skin, bare feet, distinct silhouette from the main cast, no modern accessories; 1 px dark-brown outline.
ANIMATION: idle loop. FACING DIRECTION: right. FRAME-BY-FRAME ACTION: Subtle breathing, slight shift of weight, return to starting pose. Preserve silhouette, outfit, colors, hair and accessories across all frames. The change between frames should be small and readable at native pixel scale. Output one sprite-sheet image only.
```

## 4. ENVIRONMENT ASSETS

### ENV-01 — Village ground tileset atlas

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE standalone visual asset for an original 2D top-down adventure game inspired by Indonesian folklore. This must be ONE focused asset image, not a collage, not a presentation board, not a sprite sheet, and not multiple variations. Keep the complete subject centered with generous padding and do not crop any part. Use a perfectly flat solid magenta (#FF00FF) background, clearly separated from the subject, so the background can be removed manually; it must be uniform edge to edge with no vignette, gradient or floor. No cast shadow unless requested. Output one image only.

ASSET ID: ENV-01 — Village ground tileset atlas.
PURPOSE: Reusable ground tiles for assembling the village map.
SUBJECT DESIGN: One orthogonal atlas of individual 16x16 tiles: plain green grass, grass with tiny flowers, sparse grass tufts, packed brown dirt, dirt path, grass-to-dirt transitions, inner/outer corners, pebbles and dry-earth variants. Every tile aligns exactly to the grid and is individually separable.
COMPOSITION: one orderly modular atlas on a flat solid #FF00FF magenta background. Multiple pieces are allowed only because this is a tileset/prop atlas. Arrange each piece separately on a strict orthogonal grid, no overlaps, no labels, no text, no cast shadows.
```

### ENV-02 — Forest ground tileset atlas

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE standalone visual asset for an original 2D top-down adventure game inspired by Indonesian folklore. This must be ONE focused asset image, not a collage, not a presentation board, not a sprite sheet, and not multiple variations. Keep the complete subject centered with generous padding and do not crop any part. Use a perfectly flat solid magenta (#FF00FF) background, clearly separated from the subject, so the background can be removed manually; it must be uniform edge to edge with no vignette, gradient or floor. No cast shadow unless requested. Output one image only.

ASSET ID: ENV-02 — Forest ground tileset atlas.
PURPOSE: Reusable ground tiles for exploration and chase levels.
SUBJECT DESIGN: One orthogonal atlas of individual 16x16 tiles: deep-green grass, mossy ground, brown forest dirt, path straight segments, turns, inner/outer corners, junctions, leaf litter and exposed-root ground. Seamless edges, consistent top-down perspective.
COMPOSITION: one orderly modular atlas on a flat solid #FF00FF magenta background. Multiple pieces are allowed only because this is a tileset/prop atlas. Arrange each piece separately on a strict orthogonal grid, no overlaps, no labels, no text, no cast shadows.
```

### ENV-03 — Village house exterior

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE standalone visual asset for an original 2D top-down adventure game inspired by Indonesian folklore. This must be ONE focused asset image, not a collage, not a presentation board, not a sprite sheet, and not multiple variations. Keep the complete subject centered with generous padding and do not crop any part. Use a perfectly flat solid magenta (#FF00FF) background, clearly separated from the subject, so the background can be removed manually; it must be uniform edge to edge with no vignette, gradient or floor. No cast shadow unless requested. Output one image only.

ASSET ID: ENV-03 — Village house exterior.
PURPOSE: Main house where Timun Mas and Mbok Srini live.
SUBJECT DESIGN: One small traditional Indonesian/Javanese rural wooden house viewed from top-down three-quarter perspective, warm-brown timber walls, muted thatched or tiled roof, visible front door, two small windows, simple eaves, compact footprint, no people or signage.
COMPOSITION: isolated single subject on a flat solid #FF00FF magenta background; no ground plane, no extra objects, no frame, no border.
```

### ENV-04 — Tree props atlas

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE standalone visual asset for an original 2D top-down adventure game inspired by Indonesian folklore. This must be ONE focused asset image, not a collage, not a presentation board, not a sprite sheet, and not multiple variations. Keep the complete subject centered with generous padding and do not crop any part. Use a perfectly flat solid magenta (#FF00FF) background, clearly separated from the subject, so the background can be removed manually; it must be uniform edge to edge with no vignette, gradient or floor. No cast shadow unless requested. Output one image only.

ASSET ID: ENV-04 — Tree props atlas.
PURPOSE: Reusable tree sprites for the forest.
SUBJECT DESIGN: One tidy atlas with four separate top-down trees: small leafy tree, medium rounded tree, tall dense tropical tree, broad old tree with visible trunk base. Deep and mid forest greens, brown trunks, clear silhouettes.
COMPOSITION: one orderly modular atlas on a flat solid #FF00FF magenta background. Multiple pieces are allowed only because this is a tileset/prop atlas. Arrange each piece separately on a strict orthogonal grid, no overlaps, no labels, no text, no cast shadows.
```

### ENV-05 — Canopy overlay atlas

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE standalone visual asset for an original 2D top-down adventure game inspired by Indonesian folklore. This must be ONE focused asset image, not a collage, not a presentation board, not a sprite sheet, and not multiple variations. Keep the complete subject centered with generous padding and do not crop any part. Use a perfectly flat solid magenta (#FF00FF) background, clearly separated from the subject, so the background can be removed manually; it must be uniform edge to edge with no vignette, gradient or floor. No cast shadow unless requested. Output one image only.

ASSET ID: ENV-05 — Canopy overlay atlas.
PURPOSE: Foreground foliage that can render over the player when behind a tree.
SUBJECT DESIGN: One atlas of three separate dark leafy canopy clusters and two hanging branch clusters, designed to overlay tree trunks. Deep greens, clear pixel silhouettes, no complete trees.
COMPOSITION: one orderly modular atlas on a flat solid #FF00FF magenta background. Multiple pieces are allowed only because this is a tileset/prop atlas. Arrange each piece separately on a strict orthogonal grid, no overlaps, no labels, no text, no cast shadows.
```

### ENV-06 — Bamboo fence and gate atlas

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE standalone visual asset for an original 2D top-down adventure game inspired by Indonesian folklore. This must be ONE focused asset image, not a collage, not a presentation board, not a sprite sheet, and not multiple variations. Keep the complete subject centered with generous padding and do not crop any part. Use a perfectly flat solid magenta (#FF00FF) background, clearly separated from the subject, so the background can be removed manually; it must be uniform edge to edge with no vignette, gradient or floor. No cast shadow unless requested. Output one image only.

ASSET ID: ENV-06 — Bamboo fence and gate atlas.
PURPOSE: Modular pieces for village boundaries.
SUBJECT DESIGN: One grid-aligned atlas of separate bamboo fence straight segments, ends, corner pieces, one open gate and one closed gate. Warm bamboo brown, top-down view, tile-friendly proportions.
COMPOSITION: one orderly modular atlas on a flat solid #FF00FF magenta background. Multiple pieces are allowed only because this is a tileset/prop atlas. Arrange each piece separately on a strict orthogonal grid, no overlaps, no labels, no text, no cast shadows.
```

### ENV-07 — Village furniture and utility props atlas

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE standalone visual asset for an original 2D top-down adventure game inspired by Indonesian folklore. This must be ONE focused asset image, not a collage, not a presentation board, not a sprite sheet, and not multiple variations. Keep the complete subject centered with generous padding and do not crop any part. Use a perfectly flat solid magenta (#FF00FF) background, clearly separated from the subject, so the background can be removed manually; it must be uniform edge to edge with no vignette, gradient or floor. No cast shadow unless requested. Output one image only.

ASSET ID: ENV-07 — Village furniture and utility props atlas.
PURPOSE: Small props for the house yard.
SUBJECT DESIGN: One atlas of separate props: wooden bench, low table, terracotta water jar, woven basket, plant pot, small well, stacked firewood and folded mat. Consistent scale and top-down perspective.
COMPOSITION: one orderly modular atlas on a flat solid #FF00FF magenta background. Multiple pieces are allowed only because this is a tileset/prop atlas. Arrange each piece separately on a strict orthogonal grid, no overlaps, no labels, no text, no cast shadows.
```

### ENV-08 — Forest obstacle props atlas

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE standalone visual asset for an original 2D top-down adventure game inspired by Indonesian folklore. This must be ONE focused asset image, not a collage, not a presentation board, not a sprite sheet, and not multiple variations. Keep the complete subject centered with generous padding and do not crop any part. Use a perfectly flat solid magenta (#FF00FF) background, clearly separated from the subject, so the background can be removed manually; it must be uniform edge to edge with no vignette, gradient or floor. No cast shadow unless requested. Output one image only.

ASSET ID: ENV-08 — Forest obstacle props atlas.
PURPOSE: Objects that block movement or guide the player.
SUBJECT DESIGN: One atlas of separate props: large gray-brown rock, small rock cluster, fallen log, exposed root bundle, thorny bush, low fern patch and tree stump. Each has a clear silhouette and consistent top-down view.
COMPOSITION: one orderly modular atlas on a flat solid #FF00FF magenta background. Multiple pieces are allowed only because this is a tileset/prop atlas. Arrange each piece separately on a strict orthogonal grid, no overlaps, no labels, no text, no cast shadows.
```

### ENV-09 — Small vegetation and ground detail atlas

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE standalone visual asset for an original 2D top-down adventure game inspired by Indonesian folklore. This must be ONE focused asset image, not a collage, not a presentation board, not a sprite sheet, and not multiple variations. Keep the complete subject centered with generous padding and do not crop any part. Use a perfectly flat solid magenta (#FF00FF) background, clearly separated from the subject, so the background can be removed manually; it must be uniform edge to edge with no vignette, gradient or floor. No cast shadow unless requested. Output one image only.

ASSET ID: ENV-09 — Small vegetation and ground detail atlas.
PURPOSE: Small non-blocking decoration to avoid repetitive ground patterns.
SUBJECT DESIGN: One atlas of separate tiny props: flower clumps, mushrooms, small fern, scattered leaves, tiny grass tufts, pebbles and yellow fallen leaves. Each prop should fit a 16x16 or 16x32 tile footprint.
COMPOSITION: one orderly modular atlas on a flat solid #FF00FF magenta background. Multiple pieces are allowed only because this is a tileset/prop atlas. Arrange each piece separately on a strict orthogonal grid, no overlaps, no labels, no text, no cast shadows.
```

### ENV-10 — River tileset atlas — optional

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE standalone visual asset for an original 2D top-down adventure game inspired by Indonesian folklore. This must be ONE focused asset image, not a collage, not a presentation board, not a sprite sheet, and not multiple variations. Keep the complete subject centered with generous padding and do not crop any part. Use a perfectly flat solid magenta (#FF00FF) background, clearly separated from the subject, so the background can be removed manually; it must be uniform edge to edge with no vignette, gradient or floor. No cast shadow unless requested. Output one image only.

ASSET ID: ENV-10 — River tileset atlas — optional.
PURPOSE: Optional short river-crossing area.
SUBJECT DESIGN: One modular top-down river atlas with flowing blue-green water, straight river edges, inner corners, shallow banks, stepping stones and one safe crossing. Tile edges must join seamlessly; no characters or text.
COMPOSITION: one orderly modular atlas on a flat solid #FF00FF magenta background. Multiple pieces are allowed only because this is a tileset/prop atlas. Arrange each piece separately on a strict orthogonal grid, no overlaps, no labels, no text, no cast shadows.
```

### ENV-11 — Hill path tileset atlas — optional

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE standalone visual asset for an original 2D top-down adventure game inspired by Indonesian folklore. This must be ONE focused asset image, not a collage, not a presentation board, not a sprite sheet, and not multiple variations. Keep the complete subject centered with generous padding and do not crop any part. Use a perfectly flat solid magenta (#FF00FF) background, clearly separated from the subject, so the background can be removed manually; it must be uniform edge to edge with no vignette, gradient or floor. No cast shadow unless requested. Output one image only.

ASSET ID: ENV-11 — Hill path tileset atlas — optional.
PURPOSE: Optional hill path near the final encounter.
SUBJECT DESIGN: One modular top-down atlas with earthy path, exposed rock, short grass, slope-edge transitions and small ledges represented clearly from above. No isometric perspective or 3D height shading.
COMPOSITION: one orderly modular atlas on a flat solid #FF00FF magenta background. Multiple pieces are allowed only because this is a tileset/prop atlas. Arrange each piece separately on a strict orthogonal grid, no overlaps, no labels, no text, no cast shadows.
```

### ENV-12 — Large boulder obstacle

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE standalone visual asset for an original 2D top-down adventure game inspired by Indonesian folklore. This must be ONE focused asset image, not a collage, not a presentation board, not a sprite sheet, and not multiple variations. Keep the complete subject centered with generous padding and do not crop any part. Use a perfectly flat solid magenta (#FF00FF) background, clearly separated from the subject, so the background can be removed manually; it must be uniform edge to edge with no vignette, gradient or floor. No cast shadow unless requested. Output one image only.

ASSET ID: ENV-12 — Large boulder obstacle.
PURPOSE: One prominent obstacle for the chase path.
SUBJECT DESIGN: One large rounded gray-brown boulder with subtle moss, top-down three-quarter perspective, broad readable silhouette, no surrounding environment.
COMPOSITION: isolated single subject on a flat solid #FF00FF magenta background; no ground plane, no extra objects, no frame, no border.
```

### ENV-13 — Fallen log obstacle

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE standalone visual asset for an original 2D top-down adventure game inspired by Indonesian folklore. This must be ONE focused asset image, not a collage, not a presentation board, not a sprite sheet, and not multiple variations. Keep the complete subject centered with generous padding and do not crop any part. Use a perfectly flat solid magenta (#FF00FF) background, clearly separated from the subject, so the background can be removed manually; it must be uniform edge to edge with no vignette, gradient or floor. No cast shadow unless requested. Output one image only.

ASSET ID: ENV-13 — Fallen log obstacle.
PURPOSE: One fallen tree trunk placed across a path.
SUBJECT DESIGN: One horizontal fallen tropical tree trunk viewed from above, medium-brown bark, a few dark pixel grooves and moss patches, cut end visible, no leaves or scenery.
COMPOSITION: isolated single subject on a flat solid #FF00FF magenta background; no ground plane, no extra objects, no frame, no border.
```

### ENV-14 — Thorn bush obstacle

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE standalone visual asset for an original 2D top-down adventure game inspired by Indonesian folklore. This must be ONE focused asset image, not a collage, not a presentation board, not a sprite sheet, and not multiple variations. Keep the complete subject centered with generous padding and do not crop any part. Use a perfectly flat solid magenta (#FF00FF) background, clearly separated from the subject, so the background can be removed manually; it must be uniform edge to edge with no vignette, gradient or floor. No cast shadow unless requested. Output one image only.

ASSET ID: ENV-14 — Thorn bush obstacle.
PURPOSE: One standalone thorny bush obstacle.
SUBJECT DESIGN: One dense dark-green thorn bush with clearly visible short thorn pixels and a compact readable silhouette, top-down view, no flowers or background objects.
COMPOSITION: isolated single subject on a flat solid #FF00FF magenta background; no ground plane, no extra objects, no frame, no border.
```

### ENV-15 — Clay water jar

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE standalone visual asset for an original 2D top-down adventure game inspired by Indonesian folklore. This must be ONE focused asset image, not a collage, not a presentation board, not a sprite sheet, and not multiple variations. Keep the complete subject centered with generous padding and do not crop any part. Use a perfectly flat solid magenta (#FF00FF) background, clearly separated from the subject, so the background can be removed manually; it must be uniform edge to edge with no vignette, gradient or floor. No cast shadow unless requested. Output one image only.

ASSET ID: ENV-15 — Clay water jar.
PURPOSE: A village prop placed beside the house.
SUBJECT DESIGN: One small terracotta water jar with narrow mouth and rounded body, top-down three-quarter pixel art, warm reddish-brown clay and tiny highlight pixels, no pouring liquid.
COMPOSITION: isolated single subject on a flat solid #FF00FF magenta background; no ground plane, no extra objects, no frame, no border.
```

## 5. MAGICAL ITEM ASSETS

### ITEM-01 — Cucumber seeds — inventory icon

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE standalone visual asset for an original 2D top-down adventure game inspired by Indonesian folklore. This must be ONE focused asset image, not a collage, not a presentation board, not a sprite sheet, and not multiple variations. Keep the complete subject centered with generous padding and do not crop any part. Use a perfectly flat solid magenta (#FF00FF) background, clearly separated from the subject, so the background can be removed manually; it must be uniform edge to edge with no vignette, gradient or floor. No cast shadow unless requested. Output one image only.

ASSET ID: ITEM-01 — Cucumber seeds — inventory icon.
PURPOSE: Inventory icon for Cucumber seeds.
SUBJECT DESIGN: A few small oval cucumber seeds, tan and muted golden brown, 3–5 seeds grouped compactly, unmistakable silhouette. Simplified silhouette recognizable at 16x16 or 24x24 pixels. No frame, no letters, no UI slot.
COMPOSITION: isolated single subject on a flat solid #FF00FF magenta background; no ground plane, no extra objects, no frame, no border.
```

### ITEM-01-W — Cucumber seeds — world pickup

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE standalone visual asset for an original 2D top-down adventure game inspired by Indonesian folklore. This must be ONE focused asset image, not a collage, not a presentation board, not a sprite sheet, and not multiple variations. Keep the complete subject centered with generous padding and do not crop any part. Use a perfectly flat solid magenta (#FF00FF) background, clearly separated from the subject, so the background can be removed manually; it must be uniform edge to edge with no vignette, gradient or floor. No cast shadow unless requested. Output one image only.

ASSET ID: ITEM-01-W — Cucumber seeds — world pickup.
PURPOSE: In-world pickup sprite for Cucumber seeds.
SUBJECT DESIGN: The exact same design as its inventory icon, slightly more detailed but still small-sprite readable, resting on an invisible ground plane, top-down three-quarter view. No glow, no sparkle, no cast shadow.
COMPOSITION: isolated single subject on a flat solid #FF00FF magenta background; no ground plane, no extra objects, no frame, no border.
```

### ITEM-02 — Sewing needles — inventory icon

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE standalone visual asset for an original 2D top-down adventure game inspired by Indonesian folklore. This must be ONE focused asset image, not a collage, not a presentation board, not a sprite sheet, and not multiple variations. Keep the complete subject centered with generous padding and do not crop any part. Use a perfectly flat solid magenta (#FF00FF) background, clearly separated from the subject, so the background can be removed manually; it must be uniform edge to edge with no vignette, gradient or floor. No cast shadow unless requested. Output one image only.

ASSET ID: ITEM-02 — Sewing needles — inventory icon.
PURPOSE: Inventory icon for Sewing needles.
SUBJECT DESIGN: Three slender silver-gray sewing needles grouped at a slight angle, small eye holes only if readable at icon size, no fabric or blood. Simplified silhouette recognizable at 16x16 or 24x24 pixels. No frame, no letters, no UI slot.
COMPOSITION: isolated single subject on a flat solid #FF00FF magenta background; no ground plane, no extra objects, no frame, no border.
```

### ITEM-02-W — Sewing needles — world pickup

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE standalone visual asset for an original 2D top-down adventure game inspired by Indonesian folklore. This must be ONE focused asset image, not a collage, not a presentation board, not a sprite sheet, and not multiple variations. Keep the complete subject centered with generous padding and do not crop any part. Use a perfectly flat solid magenta (#FF00FF) background, clearly separated from the subject, so the background can be removed manually; it must be uniform edge to edge with no vignette, gradient or floor. No cast shadow unless requested. Output one image only.

ASSET ID: ITEM-02-W — Sewing needles — world pickup.
PURPOSE: In-world pickup sprite for Sewing needles.
SUBJECT DESIGN: The exact same design as its inventory icon, slightly more detailed but still small-sprite readable, resting on an invisible ground plane, top-down three-quarter view. No glow, no sparkle, no cast shadow.
COMPOSITION: isolated single subject on a flat solid #FF00FF magenta background; no ground plane, no extra objects, no frame, no border.
```

### ITEM-03 — Coarse salt — inventory icon

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE standalone visual asset for an original 2D top-down adventure game inspired by Indonesian folklore. This must be ONE focused asset image, not a collage, not a presentation board, not a sprite sheet, and not multiple variations. Keep the complete subject centered with generous padding and do not crop any part. Use a perfectly flat solid magenta (#FF00FF) background, clearly separated from the subject, so the background can be removed manually; it must be uniform edge to edge with no vignette, gradient or floor. No cast shadow unless requested. Output one image only.

ASSET ID: ITEM-03 — Coarse salt — inventory icon.
PURPOSE: Inventory icon for Coarse salt.
SUBJECT DESIGN: A small pile of white and pale-cream coarse salt crystals, irregular crisp pixel clusters, no bowl or packaging. Simplified silhouette recognizable at 16x16 or 24x24 pixels. No frame, no letters, no UI slot.
COMPOSITION: isolated single subject on a flat solid #FF00FF magenta background; no ground plane, no extra objects, no frame, no border.
```

### ITEM-03-W — Coarse salt — world pickup

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE standalone visual asset for an original 2D top-down adventure game inspired by Indonesian folklore. This must be ONE focused asset image, not a collage, not a presentation board, not a sprite sheet, and not multiple variations. Keep the complete subject centered with generous padding and do not crop any part. Use a perfectly flat solid magenta (#FF00FF) background, clearly separated from the subject, so the background can be removed manually; it must be uniform edge to edge with no vignette, gradient or floor. No cast shadow unless requested. Output one image only.

ASSET ID: ITEM-03-W — Coarse salt — world pickup.
PURPOSE: In-world pickup sprite for Coarse salt.
SUBJECT DESIGN: The exact same design as its inventory icon, slightly more detailed but still small-sprite readable, resting on an invisible ground plane, top-down three-quarter view. No glow, no sparkle, no cast shadow.
COMPOSITION: isolated single subject on a flat solid #FF00FF magenta background; no ground plane, no extra objects, no frame, no border.
```

### ITEM-04 — Terasi wrapped in banana leaf — inventory icon

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE standalone visual asset for an original 2D top-down adventure game inspired by Indonesian folklore. This must be ONE focused asset image, not a collage, not a presentation board, not a sprite sheet, and not multiple variations. Keep the complete subject centered with generous padding and do not crop any part. Use a perfectly flat solid magenta (#FF00FF) background, clearly separated from the subject, so the background can be removed manually; it must be uniform edge to edge with no vignette, gradient or floor. No cast shadow unless requested. Output one image only.

ASSET ID: ITEM-04 — Terasi wrapped in banana leaf — inventory icon.
PURPOSE: Inventory icon for Terasi wrapped in banana leaf.
SUBJECT DESIGN: A compact brown fermented shrimp-paste block wrapped in a muted-green banana leaf and tied simply, recognizable as a small traditional Indonesian food parcel. Simplified silhouette recognizable at 16x16 or 24x24 pixels. No frame, no letters, no UI slot.
COMPOSITION: isolated single subject on a flat solid #FF00FF magenta background; no ground plane, no extra objects, no frame, no border.
```

### ITEM-04-W — Terasi wrapped in banana leaf — world pickup

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE standalone visual asset for an original 2D top-down adventure game inspired by Indonesian folklore. This must be ONE focused asset image, not a collage, not a presentation board, not a sprite sheet, and not multiple variations. Keep the complete subject centered with generous padding and do not crop any part. Use a perfectly flat solid magenta (#FF00FF) background, clearly separated from the subject, so the background can be removed manually; it must be uniform edge to edge with no vignette, gradient or floor. No cast shadow unless requested. Output one image only.

ASSET ID: ITEM-04-W — Terasi wrapped in banana leaf — world pickup.
PURPOSE: In-world pickup sprite for Terasi wrapped in banana leaf.
SUBJECT DESIGN: The exact same design as its inventory icon, slightly more detailed but still small-sprite readable, resting on an invisible ground plane, top-down three-quarter view. No glow, no sparkle, no cast shadow.
COMPOSITION: isolated single subject on a flat solid #FF00FF magenta background; no ground plane, no extra objects, no frame, no border.
```

### ITEM-05 — Cucumber seed projectile

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE standalone visual asset for an original 2D top-down adventure game inspired by Indonesian folklore. This must be ONE focused asset image, not a collage, not a presentation board, not a sprite sheet, and not multiple variations. Keep the complete subject centered with generous padding and do not crop any part. Use a perfectly flat solid magenta (#FF00FF) background, clearly separated from the subject, so the background can be removed manually; it must be uniform edge to edge with no vignette, gradient or floor. No cast shadow unless requested. Output one image only.

ASSET ID: ITEM-05 — Cucumber seed projectile.
PURPOSE: Projectile sprite when the seed is thrown.
SUBJECT DESIGN: One tiny tan cucumber seed in mid-flight, compact oval silhouette, no motion trail, hand or other items.
COMPOSITION: isolated single subject on a flat solid #FF00FF magenta background; no ground plane, no extra objects, no frame, no border.
```

### ITEM-06 — Needle projectile

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE standalone visual asset for an original 2D top-down adventure game inspired by Indonesian folklore. This must be ONE focused asset image, not a collage, not a presentation board, not a sprite sheet, and not multiple variations. Keep the complete subject centered with generous padding and do not crop any part. Use a perfectly flat solid magenta (#FF00FF) background, clearly separated from the subject, so the background can be removed manually; it must be uniform edge to edge with no vignette, gradient or floor. No cast shadow unless requested. Output one image only.

ASSET ID: ITEM-06 — Needle projectile.
PURPOSE: Projectile sprite when a needle is thrown.
SUBJECT DESIGN: One silver-gray sewing needle in mid-flight at a slight diagonal, clear pointed tip and small eye, no motion trail or hand.
COMPOSITION: isolated single subject on a flat solid #FF00FF magenta background; no ground plane, no extra objects, no frame, no border.
```

### ITEM-07 — Salt scatter projectile

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE standalone visual asset for an original 2D top-down adventure game inspired by Indonesian folklore. This must be ONE focused asset image, not a collage, not a presentation board, not a sprite sheet, and not multiple variations. Keep the complete subject centered with generous padding and do not crop any part. Use a perfectly flat solid magenta (#FF00FF) background, clearly separated from the subject, so the background can be removed manually; it must be uniform edge to edge with no vignette, gradient or floor. No cast shadow unless requested. Output one image only.

ASSET ID: ITEM-07 — Salt scatter projectile.
PURPOSE: Projectile sprite for the salt action.
SUBJECT DESIGN: A small compact scatter of white and cream salt crystals traveling as one readable cluster, no bowl, bag or trail.
COMPOSITION: isolated single subject on a flat solid #FF00FF magenta background; no ground plane, no extra objects, no frame, no border.
```

### ITEM-08 — Terasi toss projectile

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE standalone visual asset for an original 2D top-down adventure game inspired by Indonesian folklore. This must be ONE focused asset image, not a collage, not a presentation board, not a sprite sheet, and not multiple variations. Keep the complete subject centered with generous padding and do not crop any part. Use a perfectly flat solid magenta (#FF00FF) background, clearly separated from the subject, so the background can be removed manually; it must be uniform edge to edge with no vignette, gradient or floor. No cast shadow unless requested. Output one image only.

ASSET ID: ITEM-08 — Terasi toss projectile.
PURPOSE: Projectile sprite for the terasi action.
SUBJECT DESIGN: One small brown terasi parcel wrapped in a green banana leaf, in mid-flight at a slight angle, compact silhouette, no hand or motion trail.
COMPOSITION: isolated single subject on a flat solid #FF00FF magenta background; no ground plane, no extra objects, no frame, no border.
```

## 6. VISUAL EFFECT ASSETS (VFX)

### VFX-01 — Cucumber plant growth effect

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE standalone visual asset for an original 2D top-down adventure game inspired by Indonesian folklore. This must be ONE focused asset image, not a collage, not a presentation board, not a sprite sheet, and not multiple variations. Keep the complete subject centered with generous padding and do not crop any part. Use a perfectly flat solid magenta (#FF00FF) background, clearly separated from the subject, so the background can be removed manually; it must be uniform edge to edge with no vignette, gradient or floor. No cast shadow unless requested. Output one image only.

ASSET ID: VFX-01 — Cucumber plant growth effect.
PURPOSE: A single magical growth effect after cucumber seeds are used.
SUBJECT DESIGN: A compact cluster of bright-green curling vines and broad cucumber leaves emerging from a tiny patch of soil, a few pale-gold sparkle pixels, vertical silhouette, no seed or character.
COMPOSITION: isolated single subject on a flat solid #FF00FF magenta background; no ground plane, no extra objects, no frame, no border.
```

### VFX-02 — Cucumber vine barrier

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE standalone visual asset for an original 2D top-down adventure game inspired by Indonesian folklore. This must be ONE focused asset image, not a collage, not a presentation board, not a sprite sheet, and not multiple variations. Keep the complete subject centered with generous padding and do not crop any part. Use a perfectly flat solid magenta (#FF00FF) background, clearly separated from the subject, so the background can be removed manually; it must be uniform edge to edge with no vignette, gradient or floor. No cast shadow unless requested. Output one image only.

ASSET ID: VFX-02 — Cucumber vine barrier.
PURPOSE: Static obstacle created by the seed item.
SUBJECT DESIGN: A dense low tangle of green cucumber vines, broad leaves and a few small yellow blossoms, viewed from above, wide enough to block a narrow path, no ground tile.
COMPOSITION: isolated single subject on a flat solid #FF00FF magenta background; no ground plane, no extra objects, no frame, no border.
```

### VFX-03 — Thorn bush emergence effect

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE standalone visual asset for an original 2D top-down adventure game inspired by Indonesian folklore. This must be ONE focused asset image, not a collage, not a presentation board, not a sprite sheet, and not multiple variations. Keep the complete subject centered with generous padding and do not crop any part. Use a perfectly flat solid magenta (#FF00FF) background, clearly separated from the subject, so the background can be removed manually; it must be uniform edge to edge with no vignette, gradient or floor. No cast shadow unless requested. Output one image only.

ASSET ID: VFX-03 — Thorn bush emergence effect.
PURPOSE: A short effect for the needle item.
SUBJECT DESIGN: A compact cluster of dark-green thorn branches rising from the ground, visible sharp thorn tips and a few tiny cream sparkle pixels, no ground tile.
COMPOSITION: isolated single subject on a flat solid #FF00FF magenta background; no ground plane, no extra objects, no frame, no border.
```

### VFX-04 — Thorn bush barrier

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE standalone visual asset for an original 2D top-down adventure game inspired by Indonesian folklore. This must be ONE focused asset image, not a collage, not a presentation board, not a sprite sheet, and not multiple variations. Keep the complete subject centered with generous padding and do not crop any part. Use a perfectly flat solid magenta (#FF00FF) background, clearly separated from the subject, so the background can be removed manually; it must be uniform edge to edge with no vignette, gradient or floor. No cast shadow unless requested. Output one image only.

ASSET ID: VFX-04 — Thorn bush barrier.
PURPOSE: Static obstacle created by the needle item.
SUBJECT DESIGN: One dense dark-green thorn hedge with jagged but readable outline and pointed thorns, low top-down obstacle suitable for a 2D RPG path, no character.
COMPOSITION: isolated single subject on a flat solid #FF00FF magenta background; no ground plane, no extra objects, no frame, no border.
```

### VFX-05 — Water splash

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE standalone visual asset for an original 2D top-down adventure game inspired by Indonesian folklore. This must be ONE focused asset image, not a collage, not a presentation board, not a sprite sheet, and not multiple variations. Keep the complete subject centered with generous padding and do not crop any part. Use a perfectly flat solid magenta (#FF00FF) background, clearly separated from the subject, so the background can be removed manually; it must be uniform edge to edge with no vignette, gradient or floor. No cast shadow unless requested. Output one image only.

ASSET ID: VFX-05 — Water splash.
PURPOSE: One isolated water-splash visual.
SUBJECT DESIGN: A compact burst of blue-green water droplets and pale-cyan pixels, crisp radial silhouette, no container or background.
COMPOSITION: isolated single subject on a flat solid #FF00FF magenta background; no ground plane, no extra objects, no frame, no border.
```

### VFX-06 — Water pool barrier

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE standalone visual asset for an original 2D top-down adventure game inspired by Indonesian folklore. This must be ONE focused asset image, not a collage, not a presentation board, not a sprite sheet, and not multiple variations. Keep the complete subject centered with generous padding and do not crop any part. Use a perfectly flat solid magenta (#FF00FF) background, clearly separated from the subject, so the background can be removed manually; it must be uniform edge to edge with no vignette, gradient or floor. No cast shadow unless requested. Output one image only.

ASSET ID: VFX-06 — Water pool barrier.
PURPOSE: Static puddle created by the salt item.
SUBJECT DESIGN: One irregular oval shallow pool of blue-green water with pale-cyan edge pixels and a few ripples, top-down view, no riverbank or rocks.
COMPOSITION: isolated single subject on a flat solid #FF00FF magenta background; no ground plane, no extra objects, no frame, no border.
```

### VFX-07 — Mud eruption

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE standalone visual asset for an original 2D top-down adventure game inspired by Indonesian folklore. This must be ONE focused asset image, not a collage, not a presentation board, not a sprite sheet, and not multiple variations. Keep the complete subject centered with generous padding and do not crop any part. Use a perfectly flat solid magenta (#FF00FF) background, clearly separated from the subject, so the background can be removed manually; it must be uniform edge to edge with no vignette, gradient or floor. No cast shadow unless requested. Output one image only.

ASSET ID: VFX-07 — Mud eruption.
PURPOSE: One isolated mud eruption visual.
SUBJECT DESIGN: A compact upward splash of dark earthy-brown mud with separated droplets, readable pixel silhouette, no character, no ground tile.
COMPOSITION: isolated single subject on a flat solid #FF00FF magenta background; no ground plane, no extra objects, no frame, no border.
```

### VFX-08 — Mud trap obstacle

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE standalone visual asset for an original 2D top-down adventure game inspired by Indonesian folklore. This must be ONE focused asset image, not a collage, not a presentation board, not a sprite sheet, and not multiple variations. Keep the complete subject centered with generous padding and do not crop any part. Use a perfectly flat solid magenta (#FF00FF) background, clearly separated from the subject, so the background can be removed manually; it must be uniform edge to edge with no vignette, gradient or floor. No cast shadow unless requested. Output one image only.

ASSET ID: VFX-08 — Mud trap obstacle.
PURPOSE: Static patch of sticky mud created by terasi.
SUBJECT DESIGN: One irregular dark-brown muddy patch with lighter-brown rim pixels and subtle small ripples, top-down view, no character or surrounding ground.
COMPOSITION: isolated single subject on a flat solid #FF00FF magenta background; no ground plane, no extra objects, no frame, no border.
```

### VFX-09 — Dust puff

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE standalone visual asset for an original 2D top-down adventure game inspired by Indonesian folklore. This must be ONE focused asset image, not a collage, not a presentation board, not a sprite sheet, and not multiple variations. Keep the complete subject centered with generous padding and do not crop any part. Use a perfectly flat solid magenta (#FF00FF) background, clearly separated from the subject, so the background can be removed manually; it must be uniform edge to edge with no vignette, gradient or floor. No cast shadow unless requested. Output one image only.

ASSET ID: VFX-09 — Dust puff.
PURPOSE: Small effect for running feet or a heavy ogre step.
SUBJECT DESIGN: One compact cluster of tan and cream pixel dust clouds, rounded silhouette made of crisp square pixel clusters, no feet or ground.
COMPOSITION: isolated single subject on a flat solid #FF00FF magenta background; no ground plane, no extra objects, no frame, no border.
```

### VFX-10 — Magic sparkle

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE standalone visual asset for an original 2D top-down adventure game inspired by Indonesian folklore. This must be ONE focused asset image, not a collage, not a presentation board, not a sprite sheet, and not multiple variations. Keep the complete subject centered with generous padding and do not crop any part. Use a perfectly flat solid magenta (#FF00FF) background, clearly separated from the subject, so the background can be removed manually; it must be uniform edge to edge with no vignette, gradient or floor. No cast shadow unless requested. Output one image only.

ASSET ID: VFX-10 — Magic sparkle.
PURPOSE: Tiny reusable sparkle for item use.
SUBJECT DESIGN: A small cluster of four-point pale-gold and warm-cream pixel sparkles, only a few crisp pixels, no gradient glow, no blur.
COMPOSITION: isolated single subject on a flat solid #FF00FF magenta background; no ground plane, no extra objects, no frame, no border.
```

### VFX-11 — Stun stars

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE standalone visual asset for an original 2D top-down adventure game inspired by Indonesian folklore. This must be ONE focused asset image, not a collage, not a presentation board, not a sprite sheet, and not multiple variations. Keep the complete subject centered with generous padding and do not crop any part. Use a perfectly flat solid magenta (#FF00FF) background, clearly separated from the subject, so the background can be removed manually; it must be uniform edge to edge with no vignette, gradient or floor. No cast shadow unless requested. Output one image only.

ASSET ID: VFX-11 — Stun stars.
PURPOSE: Small effect above a stunned enemy.
SUBJECT DESIGN: Three tiny pale-yellow stars with dark outline pixels arranged in a loose arc, classic retro RPG visual, no character or text.
COMPOSITION: isolated single subject on a flat solid #FF00FF magenta background; no ground plane, no extra objects, no frame, no border.
```

### VFX-12 — Interaction marker

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE standalone visual asset for an original 2D top-down adventure game inspired by Indonesian folklore. This must be ONE focused asset image, not a collage, not a presentation board, not a sprite sheet, and not multiple variations. Keep the complete subject centered with generous padding and do not crop any part. Use a perfectly flat solid magenta (#FF00FF) background, clearly separated from the subject, so the background can be removed manually; it must be uniform edge to edge with no vignette, gradient or floor. No cast shadow unless requested. Output one image only.

ASSET ID: VFX-12 — Interaction marker.
PURPOSE: Marker displayed above an interactable NPC or object.
SUBJECT DESIGN: One simple cream-colored pixel-art speech/interaction indicator with dark outline, no letter, no punctuation, readable at 8x8 to 16x16 pixels.
COMPOSITION: isolated single subject on a flat solid #FF00FF magenta background; no ground plane, no extra objects, no frame, no border.
```

### VFX-13 — Leaf-and-mote transition strip

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE standalone visual asset for an original 2D top-down adventure game inspired by Indonesian folklore. This must be ONE focused asset image, not a collage, not a presentation board, not a sprite sheet, and not multiple variations. Keep the complete subject centered with generous padding and do not crop any part. Use a perfectly flat solid magenta (#FF00FF) background, clearly separated from the subject, so the background can be removed manually; it must be uniform edge to edge with no vignette, gradient or floor. No cast shadow unless requested. Output one image only.

ASSET ID: VFX-13 — Leaf-and-mote transition strip.
PURPOSE: Reusable motif for scene transitions.
SUBJECT DESIGN: One short horizontal strip of square pixel clusters resembling tropical leaves and muted-gold motes, balanced composition, no words and no full background.
COMPOSITION: isolated single subject on a flat solid #FF00FF magenta background; no ground plane, no extra objects, no frame, no border.
```

## 7. UI ASSETS

### UI-01 — Dialogue panel frame

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE standalone visual asset for an original 2D top-down adventure game inspired by Indonesian folklore. This must be ONE focused asset image, not a collage, not a presentation board, not a sprite sheet, and not multiple variations. Keep the complete subject centered with generous padding and do not crop any part. Use a perfectly flat solid magenta (#FF00FF) background, clearly separated from the subject, so the background can be removed manually; it must be uniform edge to edge with no vignette, gradient or floor. No cast shadow unless requested. Output one image only.

ASSET ID: UI-01 — Dialogue panel frame.
PURPOSE: Reusable dialogue box frame for the bottom of the screen.
SUBJECT DESIGN: A horizontal retro RPG dialogue panel with dark warm-brown interior, cream inner edge, muted-gold and wood-brown pixel border. Corners and edges should work with nine-slice scaling. Completely empty center.
COMPOSITION: one isolated UI panel asset on a flat solid #FF00FF magenta background. Keep the panel fully visible and centered; leave its interior empty for text to be added in code.
```

### UI-02 — Inventory slot — normal

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE standalone visual asset for an original 2D top-down adventure game inspired by Indonesian folklore. This must be ONE focused asset image, not a collage, not a presentation board, not a sprite sheet, and not multiple variations. Keep the complete subject centered with generous padding and do not crop any part. Use a perfectly flat solid magenta (#FF00FF) background, clearly separated from the subject, so the background can be removed manually; it must be uniform edge to edge with no vignette, gradient or floor. No cast shadow unless requested. Output one image only.

ASSET ID: UI-02 — Inventory slot — normal.
PURPOSE: One empty slot to be reused four times in code.
SUBJECT DESIGN: One square retro pixel-art inventory slot, dark-brown inset, muted-gold and cream pixel border, empty center, no item, number or letter.
COMPOSITION: isolated single subject on a flat solid #FF00FF magenta background; no ground plane, no extra objects, no frame, no border.
```

### UI-03 — Inventory slot — selected

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE standalone visual asset for an original 2D top-down adventure game inspired by Indonesian folklore. This must be ONE focused asset image, not a collage, not a presentation board, not a sprite sheet, and not multiple variations. Keep the complete subject centered with generous padding and do not crop any part. Use a perfectly flat solid magenta (#FF00FF) background, clearly separated from the subject, so the background can be removed manually; it must be uniform edge to edge with no vignette, gradient or floor. No cast shadow unless requested. Output one image only.

ASSET ID: UI-03 — Inventory slot — selected.
PURPOSE: Highlighted state for the inventory slot.
SUBJECT DESIGN: Same shape and dimensions as the normal slot, with brighter muted-gold edge and cream corner pixels, empty center, no item or text.
COMPOSITION: isolated single subject on a flat solid #FF00FF magenta background; no ground plane, no extra objects, no frame, no border.
```

### UI-04 — Main menu decorative frame

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE standalone visual asset for an original 2D top-down adventure game inspired by Indonesian folklore. This must be ONE focused asset image, not a collage, not a presentation board, not a sprite sheet, and not multiple variations. Keep the complete subject centered with generous padding and do not crop any part. Use a perfectly flat solid magenta (#FF00FF) background, clearly separated from the subject, so the background can be removed manually; it must be uniform edge to edge with no vignette, gradient or floor. No cast shadow unless requested. Output one image only.

ASSET ID: UI-04 — Main menu decorative frame.
PURPOSE: Frame supporting a code-rendered main menu.
SUBJECT DESIGN: One wide retro pixel-art wooden frame with subtle tropical leaf and muted-gold corner ornaments, empty dark-brown center for title/buttons, no text or characters.
COMPOSITION: one isolated UI panel asset on a flat solid #FF00FF magenta background. Keep the panel fully visible and centered; leave its interior empty for text to be added in code.
```

### UI-05 — Menu button — normal

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE standalone visual asset for an original 2D top-down adventure game inspired by Indonesian folklore. This must be ONE focused asset image, not a collage, not a presentation board, not a sprite sheet, and not multiple variations. Keep the complete subject centered with generous padding and do not crop any part. Use a perfectly flat solid magenta (#FF00FF) background, clearly separated from the subject, so the background can be removed manually; it must be uniform edge to edge with no vignette, gradient or floor. No cast shadow unless requested. Output one image only.

ASSET ID: UI-05 — Menu button — normal.
PURPOSE: Reusable normal-state menu button background.
SUBJECT DESIGN: One horizontal small retro RPG button panel made from dark-brown wood, cream inner pixels and muted-gold thin border, empty center, no text or icon.
COMPOSITION: isolated single subject on a flat solid #FF00FF magenta background; no ground plane, no extra objects, no frame, no border.
```

### UI-06 — Menu button — selected

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE standalone visual asset for an original 2D top-down adventure game inspired by Indonesian folklore. This must be ONE focused asset image, not a collage, not a presentation board, not a sprite sheet, and not multiple variations. Keep the complete subject centered with generous padding and do not crop any part. Use a perfectly flat solid magenta (#FF00FF) background, clearly separated from the subject, so the background can be removed manually; it must be uniform edge to edge with no vignette, gradient or floor. No cast shadow unless requested. Output one image only.

ASSET ID: UI-06 — Menu button — selected.
PURPOSE: Reusable selected-state menu button background.
SUBJECT DESIGN: Same dimensions and design as normal wooden RPG button, but brighter muted-gold edges and cream corner pixels, empty center, no text or icon.
COMPOSITION: isolated single subject on a flat solid #FF00FF magenta background; no ground plane, no extra objects, no frame, no border.
```

### UI-07 — Pause menu panel

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE standalone visual asset for an original 2D top-down adventure game inspired by Indonesian folklore. This must be ONE focused asset image, not a collage, not a presentation board, not a sprite sheet, and not multiple variations. Keep the complete subject centered with generous padding and do not crop any part. Use a perfectly flat solid magenta (#FF00FF) background, clearly separated from the subject, so the background can be removed manually; it must be uniform edge to edge with no vignette, gradient or floor. No cast shadow unless requested. Output one image only.

ASSET ID: UI-07 — Pause menu panel.
PURPOSE: Background panel for pause options.
SUBJECT DESIGN: One compact vertical retro RPG panel with dark-brown center, cream and muted-gold pixel border, subtle leaf ornaments in corners, large empty central area, no words.
COMPOSITION: one isolated UI panel asset on a flat solid #FF00FF magenta background. Keep the panel fully visible and centered; leave its interior empty for text to be added in code.
```

### UI-08 — Notification panel

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE standalone visual asset for an original 2D top-down adventure game inspired by Indonesian folklore. This must be ONE focused asset image, not a collage, not a presentation board, not a sprite sheet, and not multiple variations. Keep the complete subject centered with generous padding and do not crop any part. Use a perfectly flat solid magenta (#FF00FF) background, clearly separated from the subject, so the background can be removed manually; it must be uniform edge to edge with no vignette, gradient or floor. No cast shadow unless requested. Output one image only.

ASSET ID: UI-08 — Notification panel.
PURPOSE: Panel for item pickup and objective notifications.
SUBJECT DESIGN: One narrow horizontal dark-brown pixel-art panel with thin cream and muted-gold border, empty center, no icon or letters.
COMPOSITION: one isolated UI panel asset on a flat solid #FF00FF magenta background. Keep the panel fully visible and centered; leave its interior empty for text to be added in code.
```

### UI-09 — Pixel heart icon — optional

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE standalone visual asset for an original 2D top-down adventure game inspired by Indonesian folklore. This must be ONE focused asset image, not a collage, not a presentation board, not a sprite sheet, and not multiple variations. Keep the complete subject centered with generous padding and do not crop any part. Use a perfectly flat solid magenta (#FF00FF) background, clearly separated from the subject, so the background can be removed manually; it must be uniform edge to edge with no vignette, gradient or floor. No cast shadow unless requested. Output one image only.

ASSET ID: UI-09 — Pixel heart icon — optional.
PURPOSE: Player status icon if a health/hit system is included.
SUBJECT DESIGN: One small classic pixel-art heart in muted red with warm-cream highlights and dark outline, readable at 8x8 or 16x16 pixels, no text.
COMPOSITION: isolated single subject on a flat solid #FF00FF magenta background; no ground plane, no extra objects, no frame, no border.
```

### UI-10 — Item obtained badge

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE standalone visual asset for an original 2D top-down adventure game inspired by Indonesian folklore. This must be ONE focused asset image, not a collage, not a presentation board, not a sprite sheet, and not multiple variations. Keep the complete subject centered with generous padding and do not crop any part. Use a perfectly flat solid magenta (#FF00FF) background, clearly separated from the subject, so the background can be removed manually; it must be uniform edge to edge with no vignette, gradient or floor. No cast shadow unless requested. Output one image only.

ASSET ID: UI-10 — Item obtained badge.
PURPOSE: Small decorative badge beside a newly obtained item.
SUBJECT DESIGN: One simple rounded-square cream and muted-gold pixel-art badge with dark outline and empty center, no item, lettering or number.
COMPOSITION: isolated single subject on a flat solid #FF00FF magenta background; no ground plane, no extra objects, no frame, no border.
```

### UI-11 — Game title emblem

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE standalone visual asset for an original 2D top-down adventure game inspired by Indonesian folklore. This must be ONE focused asset image, not a collage, not a presentation board, not a sprite sheet, and not multiple variations. Keep the complete subject centered with generous padding and do not crop any part. Use a perfectly flat solid magenta (#FF00FF) background, clearly separated from the subject, so the background can be removed manually; it must be uniform edge to edge with no vignette, gradient or floor. No cast shadow unless requested. Output one image only.

ASSET ID: UI-11 — Game title emblem.
PURPOSE: Title illustration; title lettering will be added separately.
SUBJECT DESIGN: A compact ornamental pixel-art emblem combining a cucumber leaf, winding forest path and small muted-gold sun, balanced horizontal composition, no words or letters.
COMPOSITION: isolated single subject on a flat solid #FF00FF magenta background; no ground plane, no extra objects, no frame, no border.
```

### UI-12 — Ending decorative frame

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE standalone visual asset for an original 2D top-down adventure game inspired by Indonesian folklore. This must be ONE focused asset image, not a collage, not a presentation board, not a sprite sheet, and not multiple variations. Keep the complete subject centered with generous padding and do not crop any part. Use a perfectly flat solid magenta (#FF00FF) background, clearly separated from the subject, so the background can be removed manually; it must be uniform edge to edge with no vignette, gradient or floor. No cast shadow unless requested. Output one image only.

ASSET ID: UI-12 — Ending decorative frame.
PURPOSE: Frame for the final story message.
SUBJECT DESIGN: One wide retro pixel-art frame with warm-cream empty center, dark-brown pixel outline, restrained muted-gold corners and tiny leaf motifs, no lettering.
COMPOSITION: one isolated UI panel asset on a flat solid #FF00FF magenta background. Keep the panel fully visible and centered; leave its interior empty for text to be added in code.
```

## 8. STORY BACKGROUND ILLUSTRATIONS

### BG-01 — Village establishing background

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE full-screen illustration for an original 2D top-down adventure game inspired by Indonesian folklore. This must be ONE focused image, not a collage, not a presentation board, not a sprite sheet, and not multiple variations. Fill the entire 16:9 frame edge to edge; do NOT use a magenta or transparent background, since no background removal is needed. Output one image only.

ASSET ID: BG-01 — Village establishing background.
PURPOSE: Full-screen story background introducing the village.
SUBJECT DESIGN: A peaceful rural Indonesian village in the morning, small traditional wooden houses, tropical plants, dirt path and distant trees, warm cream sunlight. Keep details readable at 320x180, with clear foreground/midground/background layers. No characters, UI or text.
COMPOSITION: full-screen edge-to-edge pixel-art scene, 16:9 landscape composition, no UI, no text, no watermark. This is an illustration/background, not a playable map and not a sprite sheet.
```

### BG-02 — Forest establishing background

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE full-screen illustration for an original 2D top-down adventure game inspired by Indonesian folklore. This must be ONE focused image, not a collage, not a presentation board, not a sprite sheet, and not multiple variations. Fill the entire 16:9 frame edge to edge; do NOT use a magenta or transparent background, since no background removal is needed. Output one image only.

ASSET ID: BG-02 — Forest establishing background.
PURPOSE: Full-screen story background for entering the forest.
SUBJECT DESIGN: A mysterious but family-friendly tropical Indonesian forest, dense layered trees, winding brown path leading toward the center, mossy stones, deep forest greens and warm-brown earth. Atmospheric depth only through pixel clusters, not gradients. No characters, UI or text.
COMPOSITION: full-screen edge-to-edge pixel-art scene, 16:9 landscape composition, no UI, no text, no watermark. This is an illustration/background, not a playable map and not a sprite sheet.
```

### BG-03 — Chase climax illustration

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE full-screen illustration for an original 2D top-down adventure game inspired by Indonesian folklore. This must be ONE focused image, not a collage, not a presentation board, not a sprite sheet, and not multiple variations. Fill the entire 16:9 frame edge to edge; do NOT use a magenta or transparent background, since no background removal is needed. Output one image only.

ASSET ID: BG-03 — Chase climax illustration.
PURPOSE: Narrative illustration for the most intense chase moment.
SUBJECT DESIGN: Timun Mas running along a narrow forest path while the much larger green Buto Ijo pursues her from behind. Match approved character references, dramatic but readable 16-bit pixel art, foliage framing the path, no violence, no UI or text. This is an illustration, not a sprite.
COMPOSITION: full-screen edge-to-edge pixel-art scene, 16:9 landscape composition, no UI, no text, no watermark. This is an illustration/background, not a playable map and not a sprite sheet.
```

### BG-04 — Ending illustration

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE full-screen illustration for an original 2D top-down adventure game inspired by Indonesian folklore. This must be ONE focused image, not a collage, not a presentation board, not a sprite sheet, and not multiple variations. Fill the entire 16:9 frame edge to edge; do NOT use a magenta or transparent background, since no background removal is needed. Output one image only.

ASSET ID: BG-04 — Ending illustration.
PURPOSE: Full-screen story illustration after Timun Mas escapes.
SUBJECT DESIGN: Timun Mas safe on a peaceful hill path near the village in warm late-afternoon light, distant tropical trees and calm rural landscape, relieved hopeful mood, consistent 16-bit pixel art. No Buto Ijo in the foreground, no UI or text.
COMPOSITION: full-screen edge-to-edge pixel-art scene, 16:9 landscape composition, no UI, no text, no watermark. This is an illustration/background, not a playable map and not a sprite sheet.
```

## 9. OPTIONAL PRESENTATION ASSETS

### PRES-01 — Game key art

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE full-screen illustration for an original 2D top-down adventure game inspired by Indonesian folklore. This must be ONE focused image, not a collage, not a presentation board, not a sprite sheet, and not multiple variations. Fill the entire 16:9 frame edge to edge; do NOT use a magenta or transparent background, since no background removal is needed. Output one image only.

ASSET ID: PRES-01 — Game key art.
PURPOSE: Promotional illustration for a project page or academic presentation.
SUBJECT DESIGN: Timun Mas in the foreground holding a small pouch, enormous green Buto Ijo in the distant tropical forest, winding path connecting a rural Indonesian village to the forest, cucumber leaves and muted-gold magical accents, balanced cinematic composition, classic 16-bit pixel-art illustration. No title, lettering or logos.
COMPOSITION: full-screen edge-to-edge pixel-art scene, 16:9 landscape composition, no UI, no text, no watermark. This is an illustration/background, not a playable map and not a sprite sheet.
```

### PRES-02 — Gameplay art-direction mockup

**Copy-paste prompt (English):**

```text
LOCK STYLE & THEME:
THEME: Original 2D top-down adventure game "Timun Mas", inspired by Indonesian (Javanese) folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
STYLE: handcrafted retro 16-bit-inspired pixel art, crisp square pixels, deliberate pixel clusters, classic RPG readability, consistent top-down / slight three-quarter top-down perspective, chibi proportions for all people.
OUTLINE: 1 px deep warm-brown outline (#2A1B14) around every sprite, prop and item; never pure black; ground tiles have no outline.
SHADING: light from the top-left; 3 tones per material (base, shadow, highlight); flat color clusters; no gradients, no dithering noise.
PALETTE (use only these, plus restrained accents): forest greens #1F3D2B #2F5E3A #4F8A4B #8DBB5F; earthy browns #3B2616 #5A3A22 #8A5A33 #B88049; warm cream #F2E6C4 #E3D0A0; muted gold #C9A24B #8F7230; skin tones #8F5A34 #B97A4A #D79A66; accents sparingly: muted red #A8432E, water blue #4C8CA8. Magenta #FF00FF never appears in the artwork itself.
SCALE: designed to read at 320x180 internal resolution with 16x16 world tiles and nearest-neighbor scaling; no sub-pixel detail.
HARD PIXEL EDGES: no antialiasing, blur, glow, gradients, 3D, photorealism, painterly rendering, vector art, glossy modern-game rendering.
NO TEXT: no text, letters, numbers, watermarks or logos.
CONSISTENCY: match the approved character/world reference images; do not invent extra characters, props, limbs, accessories or decorative details; keep the silhouette readable at small size.

ASSET GENERATION PROMPT:
Create ONE full-screen illustration for an original 2D top-down adventure game inspired by Indonesian folklore. This must be ONE focused image, not a collage, not a presentation board, not a sprite sheet, and not multiple variations. Fill the entire 16:9 frame edge to edge; do NOT use a magenta or transparent background, since no background removal is needed. Output one image only.

ASSET ID: PRES-02 — Gameplay art-direction mockup.
PURPOSE: Reference image communicating the intended in-game look.
SUBJECT DESIGN: A top-down mock gameplay screen: small Timun Mas on a 16x16-tile-style dirt path in a green forest clearing, trees and rocks around the edges, four simple empty pixel-art inventory slots along the bottom and an empty dialogue panel. No readable text. Visual reference only, not a final screenshot.
COMPOSITION: full-screen edge-to-edge pixel-art scene, 16:9 landscape composition, no UI, no text, no watermark. This is an illustration/background, not a playable map and not a sprite sheet.
```

## Audio assets (not image-generation prompts)

Create or source these separately: village ambience, forest ambience, main-menu theme, chase music, footsteps, dialogue confirm, item pickup, item use, plant growth, thorn emergence, water splash, mud eruption, enemy stun/impact, UI click, ending cue. Use original or properly licensed audio and record sources in the project license file.

## Post-generation checklist

- [ ] One intended subject/action per character image; no collage or accidental second pose.
- [ ] Frame count matches the prompt (idle 4, walk/run 6); frames sit in equal cells with visible gaps, never touching or overlapping.
- [ ] Character height, head-top and feet baseline are identical in every frame and on every sheet of that character.
- [ ] Hair bun with gold hairband, outfit and colors match the approved Timun Mas reference (no headband or sandals).
- [ ] Background is flat uniform magenta, with no vignette or gradient.
- [ ] Same character identity, outfit, hair, palette, and proportions across all references.
- [ ] No text, watermark, unwanted object, duplicate limb, or cropped silhouette.
- [ ] Magenta background removed cleanly; no magenta fringe left on outlines.
- [ ] PNG exported with transparency where needed.
- [ ] Pixel art resized using nearest-neighbor, never bilinear smoothing.
- [ ] Image cropped to a known canvas/frame size and saved using its asset ID.
- [ ] Collision footprint, depth sorting, and animation timing configured separately in Phaser.
- [ ] Asset source and license/usage restrictions recorded.

## Suggested filenames

```text
CHR-01_timun-mas_idle-down.png
CHR-05_timun-mas_walk-down.png
CHR-19_buto-ijo_idle-down.png
ENV-01_village-ground-atlas.png
ITEM-01_cucumber-seeds-icon.png
VFX-06_water-pool.png
UI-01_dialogue-panel.png
BG-01_village-establishing.png
```

## Scope and production caveats

- This pack covers core characters and their key poses, environment tiles and props, four magical items, item projectiles, gameplay VFX, UI frames, background illustrations, and optional presentation images.
- The current character list includes idle directions and representative walk/run directions, plus key interaction/action poses. For smooth frame-by-frame animation, each action generally needs several distinct frames per direction; a single still cannot animate itself.
- Character image consistency is best achieved by generating one approved reference per character and reusing it as a reference in every subsequent Flow generation.
- The four magical item effects are a gameplay adaptation. Confirm that interpretation against the version of the Timun Mas folklore chosen for the project.
- Some assets are optional. If time is limited, prioritize playable character, Buto Ijo, Mbok Srini, village/forest ground, trees/obstacles, four item icons/effects, dialogue panel, inventory, and ending screen.
