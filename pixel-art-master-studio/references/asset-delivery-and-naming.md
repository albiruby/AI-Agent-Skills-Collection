# Asset Delivery and Naming

## 1. Folder structure

```text
project/
  source/          native editable files
  working/         WIP crops, experiments
  export/          lossless PNG sprites/tiles/UI
  atlas/           sprite sheets and tile atlases
  metadata/        JSON/XML/TSX/TMX/Aseprite tags
  preview/         GIF/APNG/contact sheets
  qa/              QA reports and screenshots
```

Adapt to project conventions, but keep source, working, export, and QA separate.

## 2. Naming

Use deterministic lowercase kebab-case:

```text
<asset-id>_<state>_<direction>_<frame>_<size>.png
hero_idle_down_00_32x32.png
slime_attack_side_02_32x32.png
ui_icon_health_16x16.png
terrain_grass_autotile_16x16.png
```

- Include asset ID, state, direction, frame, and dimensions where useful.
- Avoid `final`, `new`, `copy`, and ambiguous dates.
- Keep frame numbers zero-padded.
- Use the same naming in the manifest and engine import.

## 3. Manifest

Include:

- File/path, asset ID, type.
- Dimensions, pivot/origin, frame count/durations.
- Palette name/version, projection, scale.
- Engine import settings, atlas page, collision data.
- Source file and license/provenance.
- QA status and known issues.

Use `../templates/asset-manifest.csv` as a starting point.

## 4. Versioning

- Version asset packs with a semantic version and date.
- Keep a changelog for breaking changes (size, pivot, palette, naming).
- Do not silently replace an asset with different dimensions/pivot; mark breaking changes.
- Preserve previous export if the engine or downstream project depends on it.

## 5. Licensing and attribution

- Track third-party fonts, brushes, reference art, and generated images.
- Do not redistribute assets without rights.
- Include attribution required by licenses.
- Distinguish generated concepts from final authored assets.

## 6. Handoff

The receiver should get:

- Final exports + native sources.
- Manifest and metadata.
- Style bible/palette.
- Engine import notes and test evidence.
- Known limitations and outstanding QA.
- A clear statement of what was created, converted, or only specified.
