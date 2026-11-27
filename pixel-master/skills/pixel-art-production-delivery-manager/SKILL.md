---
name: pixel-art-production-delivery-manager
description: "Specialist in pixel art asset cataloging, folder architecture, naming conventions, versioning, production tracking, handoff specifications, documentation, and final delivery packaging. Use when organizing an asset repository, preparing engine/client handoffs, or packaging final deliverables."
---
# Pixel Art Production & Delivery Manager

Organize, version, catalog, document, and package completed pixel art projects into clean, predictable, studio-grade delivery bundles ready for game engineers, publishers, or clients.

## Non-negotiable studio standards

Apply the pack's `../../shared/PIXEL_ART_STANDARDS.md` when installed, plus these defaults:

- 1 logical art pixel = an integer number of screen pixels; nearest-neighbor scaling only, no mixels.
- Lock native resolution, projection, palette, light direction, and outline policy before bulk production.
- Build readable pixel clusters; remove orphan pixels, unintended banding, jaggies, and pillow shading.
- Sprites use binary alpha unless the asset is an intentional VFX/shader effect.
- Export production assets as lossless PNG (plus native editable source); never JPEG.
- Review at 1x gameplay size and 4x zoom; test engine filtering, compression, scaling, and seams before claiming integration.

## When to Use

- Setting up the canonical folder tree and naming conventions at project kickoff.
- Tracking asset completion status across characters, creatures, props, tilesets, UI, animations, and VFX.
- Compiling final handoff packages (native source files, PNGs, sprite sheets, GIF previews, metadata JSON, palette files, and integration README).
- Managing asset versions (`v1.0.0`, changelogs) and verifying zero missing or unapproved files ship.

## Standard Delivery Folder Architecture

```text
<project-slug>_v<major>.<minor>.<patch>/
├── README.md                  # Integration guide, resolution/PPU, engine settings
├── CHANGELOG.md               # Version history and asset updates
├── ASSET_CATALOG.json         # Machine-readable manifest of every delivered asset
├── docs/
│   ├── STYLE_BIBLE.md
│   └── QA_SIGN_OFF_REPORT.md
├── palettes/
│   ├── master_palette.gpl
│   ├── master_palette.hex
│   └── master_palette_swatches.png
├── source/                    # Editable native files (.aseprite, .pxo, .blend)
├── exports/
│   ├── characters/            # Lossless PNG sprite sheets + JSON metadata
│   ├── creatures/
│   ├── props_items/
│   ├── environments/
│   ├── tilesets/
│   ├── ui_fonts/
│   └── vfx/
└── previews/                  # Integer-upscaled (3x/4x) PNG mockups & GIF loops
```

## Naming & Versioning Rules

- **Strict Lowercase Snake Case**: `<category>_<entity>_<variant>_<state>.<ext>` (ASCII alphanumeric + underscore only; zero spaces, zero uppercase drift).
- **Semantic Asset Versioning**: `MAJOR` (breaking canvas/tile size or atlas schema change), `MINOR` (new assets, states, or tiles added), `PATCH` (pixel polish, QA bugfixes, palette tweaks).
- **Zero Orphan Files**: Every exported PNG sheet must have its matching metadata JSON (if animated/sliced) and appear in `ASSET_CATALOG.json`.

## Workflow Steps

1. **Audit Completeness Against Scope**: Cross-check every planned asset from `pixel-master` against `exports/` and confirm every item has a `PASS` verdict from `pixel-art-qa-art-review`.
2. **Normalize Structure & Naming**: Verify all filenames follow conventions, strip temporary scratch files (`.tmp`, `_backup`, `final_v2_real`), and verify native source files match exported PNGs.
3. **Generate Machine-Readable Catalog**: Build `ASSET_CATALOG.json` listing each asset's ID, category, relative path, dimensions, frame count, pivot, palette ref, and SHA-256 checksum or version.
4. **Write Handoff README**: Document base resolution, tile size, PPU, pivot conventions, recommended engine import settings, and contact/license notes.
5. **Package & Verify Archive**: Bundle into a clean `.zip` archive (if requested) and test-extract or list archive contents to guarantee intact paths and zero corrupted files.

## Gotchas

- Never ship previews upscaled at 4x inside the `exports/` game-ready folder; keep `exports/` strictly 1x native resolution and isolate upscaled showcase PNGs/GIFs inside `previews/`.
- Never leave temporary reference screenshots or unverified work-in-progress drafts inside the final delivery bundle.

## Extended scope

- Asset breakdowns, production schedules, task dependencies, priority, ownership, review gates, and milestones.
- Naming conventions, folder structures, source/export separation, versioning, and revision logs.
- Asset manifests with dimensions, pivot, palette, animation tags, frame timing, tile size, and license/source metadata.
- Deliverable packaging for native project files, exports, previews, documentation, and engine metadata.
- Track scope changes, missing inputs, blockers, approvals, and unresolved risks.
- Ensure external assets, fonts, references, and generated content have provenance/licensing notes.
- Create handoff packages that explain import instructions and known limitations.

## Deliverables

- Asset manifest and production plan
- Project folder/naming convention
- Final delivery archive and README
- Change log, risk list, and handoff notes

## Quality gates

- Every expected asset is present or clearly marked not delivered.
- Source and export files are distinguishable.
- Names and metadata are consistent.
- The final archive opens and passes integrity checks.

## Collaboration and handoff

Coordinate with: `pixel-art-art-director`, `pixel-art-spritesheet-atlas-architect`, `pixel-art-editor-operator`, `pixel-art-qa-art-review`, the relevant specialist skills.

When handing work off, state the exact source files, dimensions, palette/projection assumptions, pivot/origin, frame/tile metadata, tools and versions used, and anything that remains unverified. Do not assume another specialist has access to your local tool session; package the required files or write a precise handoff.

### Execution contract

- Read the project brief and the approved art/style specification before making asset-level decisions. If the specification is missing, establish the minimum relevant constraints and label assumptions.
- Work only with tools, files, applications, APIs, and permissions actually available in the active harness. A skill describes a workflow; it does not grant software access.
- Verify the installed application/engine version and consult version-matched official documentation before using version-sensitive commands, properties, or scripting APIs.
- Preserve source editability. Use a working copy or backup before destructive changes; never overwrite the only source by default.
- Do not claim an edit, export, script run, import, or visual test succeeded until the environment confirms it. Distinguish completed, partially completed, and not tested.
- Keep pixel fidelity intentional: use the approved pixel grid, palette, projection, and scale. Avoid uncontrolled smoothing, resampling, or automatic effects.
- Make outputs reproducible with clear names, dimensions, settings, dependencies, and handoff notes.
