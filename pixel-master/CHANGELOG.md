# Changelog

## 2.0.0

Merged the Gemini and universal GPT editions into one production pack.

### Merged

- 26 skills: 1 master orchestrator + 25 specialists.
- Gemini's concrete craft standards, studio modes, pipeline, gotchas, and shared pixel-art standards.
- GPT's consistent specialist structure: role, scope, deliverables, quality gates, collaboration, execution contract.
- Both source versions' templates, checklists, and validation logic.

### Added

- Expanded `shared/PIXEL_ART_STANDARDS.md` covering paradigms, grid/palette, clusters, animation, engine QA, AI generation/cleanup, style bible, delivery.
- Pillow-only `scripts/pixel_art_qa.py` (no numpy): palette compliance, alpha fringe, orphans, seams, cell divisibility.
- `scripts/palette_ramp.py` for hue-shifted ramps.
- `scripts/validate_package.py` for frontmatter, H1, trigger, standards block, resources, JSON.
- References: AI pixel cleanup, engine matrix, palette/ramp, tileset/autotile, animation, delivery/naming.
- Templates: style bible, palette spec, tileset spec, sprite atlas, QA report, production brief, animation plan, engine validation, asset manifest.
- Worked examples: character, environment, AI-to-pixel, 3D-to-pixel.
- Evaluation harness with three cases and scorecard.
- `skill-pack.json`, `SKILL-INDEX.md`, installers, portability guide, attribution notes.

### Fixed / enhanced

- Removed the inconsistent `# Instructions` H1 pattern; every skill now has a title-case H1.
- Added a non-negotiable standards block to every skill for standalone use.
- Added explicit authenticity labels for generated/converted pixel art.
- Added Pixel-only fallback for environments without numpy.
- Clarified engine-version verification and "untested" reporting.
- Consolidated master routing and five studio modes.

## 1.0.0 (source editions)

- `pixel-art-master-studio-gemini` v1.0.0: 26 skills, shared standards, studio modes, QA utility.
- `pixel-art-master-studio-universal-GPT` v1.0.0: 26 skills, execution contracts, templates, package validation.
