# Example: Timun Mas (2D pixel-art game, Javanese folklore)

A filled example of the instruction slots produced with this suite. Replace everything for your own project.

## Slot 1 - Global rules

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

## Slot 2 - Character & sprite sheet canon

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

## Slot 3 - World, item, VFX & UI canon

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

