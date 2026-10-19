# Google Flow: 3 instruction slots

Slot 1 = global rules. Slots 2 and 3 split the rest by asset type. Keep every prompt's own `LOCK STYLE & THEME` block as well, in case a slot is off or truncated. Verify the character limit of each slot in Flow.

## Fill-in version (replace the <angle brackets>)
### Slot 1 - Global rules
```text
GLOBAL RULES - <PROJECT>
If a prompt is unclear, choose the simpler, flatter, more consistent option.
THEME: <premise, setting, culture, mood, audience>
STYLE: <medium, rendering, proportions, perspective>
OUTLINE: <weight and hex>
SHADING: <light direction, tones per material>
PALETTE (use only these, plus restrained accents): <groups with hex>. <Key color> never appears in the artwork.
SCALE: <internal resolution, tile size, rendering rule>
HARD EDGES / EXCLUSIONS: <list>
NO TEXT: no text, letters, numbers, watermarks or logos.
BACKGROUND: flat uniform <key color> edge to edge for assets; full-frame art has no key color.
OUTPUT: one image per generation.
```
### Slot 2 - Subject canon
```text
CHARACTER & SHEET CANON - <PROJECT>
<One DESIGN LOCK per character, with size in px>
FACING: down = front, up = back, left/right = side profile.
SHEET GEOMETRY: <geometry text from game-asset-sheet-spec>
ACROSS FRAMES AND SHEETS: identical scale, outfit, hair, colors, line weight; fixed head-top and feet baseline.
NEVER: extra limbs, changed hairstyle, new accessories, different outfit colors.
```
### Slot 3 - World, item, VFX and UI canon
```text
WORLD, ITEM, VFX & UI CANON - <PROJECT>
GROUND TILES: <size, seamless, no outline>
PROPS / BUILDINGS: <view, outline, ground contact, no cast shadow>
ITEMS: <size readability, one centered object>
VFX: <shape language, palette limits>
UI: <nine-slice rules, border and fill colors, no text>
BACKGROUNDS / KEY ART: <aspect, layers, no key color>
REJECT AND REGENERATE IF: <your defect list>
```

## Filled example
See `../examples/timun-mas/instruction-slots.md` (three slots, about 2,200 / 2,200 / 1,600 characters).
