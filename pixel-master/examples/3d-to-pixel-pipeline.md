# Example: 3D-to-Pixel Pipeline

## Brief

Create a pixel-style character sprite from a low-poly 3D model, for a game with a fixed isometric camera and a limited palette.

## 1. Choose the paradigm

This is **pixel style** unless the render is deliberately rebuilt on the final pixel grid. State it. A low-res render is not automatically authentic pixel art.

## 2. Model and camera

- Low-poly model; clean silhouette; no high-frequency detail that will disappear.
- Orthographic camera; fixed angle matching the game projection.
- Consistent scale/pivot; render the same bounds for every direction/frame.
- Neutral lighting; avoid soft shadows that quantize badly.

## 3. Render

- Render at a low internal resolution (for example 64x64 or 96x96) or downscale with nearest-neighbor.
- Transparent background; no motion blur; consistent framing.
- Export a lossless PNG sequence or sprite sheet.
- Render each direction/frame from the same camera rig.

## 4. Convert to pixel grid

1. Downscale to the target sprite size with nearest-neighbor.
2. Quantize to the approved palette; preserve value hierarchy.
3. Clean edges, remove semi-alpha fringe, and rebuild the silhouette.
4. Redraw face, hands, and focal details on the grid.
5. Remove noise and unintended gradients.
6. Check mixels and inconsistent pixel sizes.

## 5. Animate

- Render key poses/frames from the 3D rig if the motion is reliable.
- Rebuild timing and arcs; do not assume 3D interpolation equals good pixel animation.
- Lock pivot/foot baseline and frame durations.
- Clean each frame; ensure no scale/volume drift.

## 6. Optional shader/post-process

- Quantization/dither shader for runtime pixel style.
- CRT/scanline effects only if intentional and readable.
- Keep a clean pixel asset for documentation/store; do not rely on the shader for basic readability.

## 7. Engine integration

- Nearest filtering, no mipmaps/compression, pixel snap/integer scale.
- Test the orthographic camera and sprite pivot in the target scene.
- Verify no shimmer during movement.

## 8. QA

- [ ] Paradigm labeled correctly
- [ ] Grid/palette consistent
- [ ] No alpha fringe/mixels
- [ ] Pivot/frames stable
- [ ] Engine render tested
- [ ] Source model/render/export preserved

## 9. Handoff

Include the 3D source, render settings, conversion steps, palette, frame metadata, shader notes, QA report, and authenticity label.
