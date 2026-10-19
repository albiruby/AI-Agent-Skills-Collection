---
name: game-art-style-theme
description: Define visual style, theme, setting, mood, color palette, typography and art direction for a game (pixel art, low-poly, stylized 3D, anime, cyberpunk, cozy, horror, etc.), plus an art bible and consistency rules. Use for look & feel.
---

# Art Style & Theme Director

## Decide in this order
1. **Theme/setting**: fantasy, sci-fi, cyberpunk, steampunk, post-apocalyptic, western, noir, horror, cozy/slice-of-life, historical, mythology/folklore (e.g. Indonesian/Nusantara folklore), cosmic, military, underwater, kids/fairy-tale, abstract/minimal, retro-arcade, comedy/parody.
2. **Mood keywords** (3): e.g. "warm, nostalgic, mischievous".
3. **Visual style** (pick one and commit):
   - 2D: pixel art (8/16/32-bit, resolution + palette limit), hand-drawn/painterly, vector/flat, cut-out/skeletal (Spine/DragonBones), anime/cel, comic/ink, paper-craft, silhouette, isometric, HD-2D.
   - 3D: low-poly, voxel, PSX/retro-3D, stylized PBR, toon/cel-shaded, realistic PBR, claymation, hand-painted textures, wireframe/vector.
   - UI-driven/minimalist: geometric, neon/synthwave, glitch, text-only.
4. **Palette**: 5-8 colors with roles (primary, secondary, accent, danger, safe, background, UI); check contrast (WCAG) and colorblind safety; define value hierarchy (readability first).
5. **Shape language**: round = friendly, angular = hostile, square = stable; silhouette test for characters/enemies.
6. **Camera & perspective, resolution, pixel-perfect rules, scaling** (integer scale, filtering off for pixel art).
7. **Lighting & VFX language**: 2D lights/normal maps, bloom, post-processing limits; particle style; shader plan (outline, dissolve, water, CRT) per engine.
8. **Typography**: display font + readable body font; licensing check; multi-language glyph coverage.

## Art bible template
Style pillars, mood board refs, palette swatches (hex), character/enemy design rules, environment kit rules, UI style, animation principles (frame counts, timing), do/don't examples, naming conventions, file specs (see 07).

## Cohesion rules
One pixel density, one outline rule, one light direction, one color temperature per biome, consistent UI skin. Mixed AI-generated assets need a style-lock pass (palette remap, same prompt prefix/seed/LoRA/reference).

## Output
Art bible (Markdown), palette JSON, theme-to-feature mapping (how theme influences mechanics, audio, UI), and risk notes (asset volume vs team).
