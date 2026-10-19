---
name: game-asset-pipeline
description: Plan and specify all game assets (sprites, tilesets, 3D models, animations, VFX, UI, audio, fonts): formats, sizes, naming, import settings, atlas, compression, tools, and AI-asset generation prompts and legal checks.
---

# Asset Pipeline Planner

## Asset inventory first
Produce an **asset list** (CSV-style): ID, category, name, description, size/spec, animations/states, priority (P0 MVP/P1/P2), source (hand-made/AI/store/commissioned), status, license.

## 2D specs
- Sprites: PNG (lossless), power-of-two atlases (or engine auto-pack), consistent pivot, 4-8 directional sets, frame counts per action (idle 4-6, walk 6-8, attack 4-8), padding/extrusion 1-2 px to avoid bleeding.
- Tilesets: tile size (16/32/48/64), autotile rules (47-blob / wang / 16-tile), collision/navigation layers, Tiled (.tmx/.json) or LDtk or engine tilemap.
- Animation: Aseprite/Pyxel Edit/Krita, Spine/DragonBones/Live2D (cut-out/vtuber style), frame-by-frame vs skeletal.
- Backgrounds: parallax layers (3-6), seamless loops.
- UI: 9-slice, SVG/vector for scalable, icon grid sizes, @1x/@2x/@3x for mobile.

## 3D specs
- Models: glTF/GLB (web & modern engines), FBX (Unity/Unreal), USD; poly/tri budgets per platform class; LODs; UV (no overlap for lightmaps), PBR maps (albedo, normal, ORM/metal-rough, emissive); texture sizes (mobile 512-1024, PC 2k-4k) with compression (ASTC mobile, BC/DXT desktop, KTX2/Basis web).
- Rig/animation: humanoid retargeting, root motion, blend trees/state machines; Mixamo/Blender/Maya/Blockbench/MagicaVoxel.
- Environment: modular kits, trim sheets, foliage cards, terrain, skybox/HDRI, baked vs realtime lighting.

## VFX/Shaders
Particle sprite sheets, shader graph/Godot shader/GLSL; budget overdraw.

## Audio files (see 09)
WAV masters; OGG/MP3/AAC for ship; loop points; loudness targets.

## Naming & folders
`category_name_variant_state_nn` lowercase snake_case, e.g. `enemy_slime_blue_walk_01.png`; keep raw sources (`.aseprite`, `.blend`, `.psd`) outside shipped assets.

## AI-generated assets
- Use a **locked style prompt prefix** + reference images + fixed negative prompts; generate sprite sheets with grid guides; post-process (palette quantize, cleanup, alignment, background removal).
- Prompt template: `[subject], [style], [view/angle], [palette], [lighting], [background: plain/transparent], [constraints: consistent proportions, no text]`.
- Check licenses/terms of each generator and training-data risk; keep a provenance log; disclose AI use where stores require it (e.g. Steam AI disclosure).

## Output
Asset list, spec sheet per category, naming/folder convention, tool chain, import settings per engine, build-time optimization (atlas, compression), AI prompt pack if requested.
