# Pixel Art Master Studio

**A production-grade pixel-art studio for AI agents: 1 master orchestrator + 25 specialists, merged from the Gemini and universal GPT editions.**

The pack covers authentic hand-authored pixel art and pixel-style pipelines (raster conversion, 3D-to-pixel, shaders). It is designed for games, asset packs, character/environment/UI production, key art, and technical integration.

## What this pack is

- **26 skills** with explicit roles, concrete craft standards, workflows, deliverables, quality gates, and execution contracts.
- **Two paradigms:** authentic pixel art and pixel style, kept distinct.
- **Five studio modes:** Complete Game, Character, Environment, Pixel UI, 3D-to-Pixel.
- **Shared standards:** canvas/pixel density, palette, clusters, shading, animation, export, engine QA.
- **Bundled tooling:** Pillow-only pixel QA, palette ramp generator, package validator.
- **Templates and references:** style bible, production brief, palette spec, tileset, atlas, animation plan, engine validation, QA, AI cleanup, delivery.
- **Examples and evals:** character, environment, AI-to-pixel, 3D-to-pixel, plus scored test cases.

## Architecture

```text
pixel-art-master-studio/
  README.md
  INSTALL.md
  CHANGELOG.md
  SKILL-INDEX.md
  PORTABILITY-GUIDE.md
  LICENSE-AND-ATTRIBUTION.md
  REFERENCES.md
  skill-pack.json
  package.json
  install.sh
  install.ps1
  shared/
    PIXEL_ART_STANDARDS.md
  skills/
    pixel-art-studio-director/        # master
    pixel-art-art-director/           # 01
    pixel-art-fundamentals-specialist/# 02
    ...                               # 26 skills total
  references/
  templates/
  scripts/
  examples/
  evals/
```

## Skills

- **Master:** `pixel-art-studio-director` — routing, studio modes, production pipeline, QA/delivery.
- **Foundation:** art director, fundamentals, palette/color, pixel-style conversion.
- **Characters/world:** character, creature, prop/item, environment, tileset, isometric, key art.
- **UI/type:** UI/icon, typography/logo.
- **Motion:** animation director, sprite animator, VFX.
- **Technical:** atlas/sprite sheet, editor operator, procedural automation, 3D render pipeline, shader/post-process, engine integration, optimization, QA, delivery.

See `SKILL-INDEX.md`.

## Studio modes

- **Complete Pixel Art Game:** full visual system from art direction to engine-ready delivery.
- **Character Studio:** concept, turnaround, variants, animation, atlas, QA.
- **Environment Studio:** tilesets, autotile, props, parallax, lighting, VFX.
- **Pixel UI Studio:** HUD, menus, icons, bitmap type, nine-slice, states.
- **3D-to-Pixel Studio:** orthographic render, quantization/dither, cleanup, engine.

## Quick start

1. Install the pack (see `INSTALL.md`).
2. Ask:

> Use `pixel-art-studio-director` to plan and produce a 32x32 side-view character with idle/walk/attack animations for Godot 4.

Or invoke a specialist directly:

> Use `pixel-art-character-artist` to design a 32x32 hooded runner with a 16-color dusk palette.

> Use `pixel-art-game-engine-integration` to fix blurry sprites and tile seams in my Godot 4 project.

> Use `pixel-art-qa-art-review` to audit these PNGs at 1x and 4x.

## Scripts

```bash
# Pixel craft, palette, alpha, orphan, seam, grid checks (Pillow only)
python scripts/pixel_art_qa.py sprite.png --max-colors 16 --palette "#0f0f1b,#3a6ea5,#ef7d57,#f4f4f4" --cell 32x32

# Hue-shifted ramp helper
python scripts/palette_ramp.py "#3a6ea5" --steps 5 --format hex

# Validate the package
python scripts/validate_package.py
```

On Windows use `python`; macOS/Linux may use `python3`. Pillow is required; numpy is not.

## Quality rules

- Ground every asset claim in real files, scripts, or observed behavior.
- Do not call a generated image authentic pixel art without grid/palette/alpha cleanup.
- Lock grid, palette, projection, pivots, and engine settings before bulk work.
- Lossless PNG + native source; never JPEG for production assets.
- Verify engine filtering/scaling/seams or mark integration untested.
- Track third-party assets and licenses; do not copy distinctive copyrighted characters.
- Distinguish created, converted, reviewed, validated, and published states.

## Merged from

- `pixel-art-master-studio-gemini` v1.0.0 — concrete craft standards, studio modes, shared standards, QA utility.
- `pixel-art-master-studio-universal-GPT` v1.0.0 — consistent specialist structure, execution contracts, templates, package validation.

Version **2.0.0**. History in `CHANGELOG.md`.
