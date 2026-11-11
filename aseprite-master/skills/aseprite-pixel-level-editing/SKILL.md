---
name: aseprite-pixel-level-editing
description: Performs precise pixel-level editing, cleanup, recoloring, cluster repair, line cleanup, and bounded modifications in Aseprite using verified MCP capabilities. Use when a specific defect must be fixed — stray pixels, broken outlines, staircase diagonals, color spills — or a small bounded change is needed on an existing sprite.
---

# Pixel-Level Editing

## Mission
Make the smallest reliable edit that improves the asset while preserving all unaffected pixels, layers, frames, and document properties.

## Before editing
1. Inspect the active document, canvas bounds, active layer, selected frame, and color mode if the MCP server exposes them.
2. Confirm coordinate origin, index conventions, and color representation.
3. Identify the exact region and frames to change.
4. Save a checkpoint or duplicate the document when supported.
5. If the requested change is ambiguous, clarify before modifying a large region.

## Editing workflow
1. State the intended visual change in observable terms.
2. Test a small operation on a low-risk region when tool behavior is uncertain.
3. Apply edits in bounded batches.
4. Inspect the edited region at native resolution and zoomed-in.
5. Inspect neighboring pixels to catch halos, holes, broken outlines, and accidental color spills.
6. Compare against the original or checkpoint if available.
7. Revalidate dimensions, transparency, palette, and layer/frame selection.

## Pixel-art cleanup
- Remove isolated pixels unless they serve a clear purpose.
- Repair inconsistent staircase diagonals.
- Preserve deliberate texture and dithering.
- Maintain outline thickness and avoid accidental double outlines.
- Repair gaps in silhouettes and color fills.
- Recolor by semantic palette ramps rather than arbitrary pixel substitutions.
- Preserve highlights and shadows consistent with the light source.
- Do not use blur, smooth scaling, or anti-aliasing unless explicitly requested.

## Transformations
Before flip, rotate, scale, shift, or crop:
- confirm the selected region and pivot,
- check whether the operation affects one layer, one frame, or the whole document,
- preserve the original where possible,
- inspect clipping and transparency afterward.

## Failure recovery
If the result is worse:
1. Stop repeated edits.
2. Undo or restore the last verified checkpoint if supported.
3. Re-inspect current state.
4. Apply one targeted correction.
5. Recheck the full asset for collateral changes.

Never claim exact pixel preservation unless it was actually verified.
