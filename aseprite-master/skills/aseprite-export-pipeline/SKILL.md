---
name: aseprite-export-pipeline
description: Exports Aseprite source files, sprite sheets, frame sequences, GIF previews, and metadata with verified dimensions, transparency, naming, and layout. Use when the user asks to export .aseprite sources, sprite sheets, PNG frame sequences, GIF previews, or JSON/XML metadata and needs the output files verified.
---

# Export Pipeline

## Confirm deliverable
Ask or infer whether the user needs:
- Editable `.ase` / `.aseprite` source
- PNG sprite sheet
- Individual PNG frames
- Animated GIF preview
- Sprite sheet plus JSON/XML metadata, if supported
- Engine-specific package or naming convention

Do not promise formats or metadata the installed tools cannot generate.

## Before export
- Save the editable source.
- Confirm frame count, frame size, sheet layout, padding, spacing, and extrusion requirements.
- Confirm transparency and color mode.
- Confirm naming scheme and destination.
- Confirm animation timing and loop metadata needs.

## After export
- Verify that every expected file exists.
- Inspect image dimensions and alpha channel where tools allow.
- Confirm frame order and sheet layout.
- Check that no frame is clipped or duplicated accidentally.
- Confirm metadata indices correspond to the actual sheet.
- If possible, re-import the export or render a preview.
- Report only verified paths.

## Naming suggestion
`project_asset_variant_direction_state_v001.aseprite`
`project_asset_variant_direction_state.png`
`project_asset_variant_direction_state.json`

Adapt naming to the user's existing project convention; never rename existing files blindly.

## Handoff
Provide source, export, dimensions, frame count, timing, transparency, and known limitations.
