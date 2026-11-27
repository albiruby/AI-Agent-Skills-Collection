# Pixel Art Master Studio - Universal Technical and Visual Standards

All 26 skills enforce these baselines unless the project's approved Style Bible explicitly overrides a parameter. Record overrides; do not assume a universal resolution.

## 0. Paradigm definitions

- **Authentic pixel art:** pixels are placed deliberately on a fixed grid; palette, clusters, outlines, and anti-aliasing are authored.
- **Pixel style:** a low-resolution render or image conversion that is quantized/dithered to a pixel grid. It is not automatically authentic pixel art.
- **Hybrid:** explicit rules for which layers use which paradigm; never mix silently.

## 1. Canvas resolution and pixel density

- Common grids: 8x8 (micro icons/particles), 16x16 (classic tiles/items), 24x24 (RPG icons), 32x32 (16-bit characters/tiles), 48x48/64x64 (detailed characters/bosses), 128x128+ (key art/large bosses).
- Every asset on the same screen plane must use one logical pixel scale. Never mix 1x and 2x pixel sizes (mixels).
- Upscale previews/exports by integer multiples (2x, 3x, 4x, 8x) with nearest-neighbor. No bilinear, bicubic, or Lanczos filtering on pixel assets.
- Author at a base viewport that divides cleanly into target displays (for example 320x180, 480x270, 640x360); document the scale matrix.

## 2. Color and palette discipline

- Lock a master palette before production (4, 8, 16, 32, or 64 colors). Authentic assets map to approved palette indices plus optional 1-bit transparency.
- Use hue-shifted ramps: shadows toward cooler/deeper hues, highlights toward warmer/brighter hues; adjust saturation and value together, not just black/white.
- Separate value hierarchy: foreground entities highest contrast, interactive midground medium, background/parallax compressed.
- Provide hex values and palette index order in the style bible. Avoid unapproved colors hidden in anti-aliasing or effects.
- Check readability in grayscale, not only color.

## 3. Shape, cluster, and shading craft

- **Silhouette first:** every character, creature, item, and icon must read as a flat one-color silhouette before detail.
- **Cluster discipline:** build forms from intentional connected pixel clusters. Remove orphan 1-pixel noise unless it is a deliberate glint or texture.
- **No pillow shading:** use one global light direction from the Style Bible. Do not ring every edge dark and center-highlight.
- **Banding/jaggies:** avoid parallel 1-pixel contour bands and irregular step progressions on curves/diagonals; use smooth 1-1-2-3-style steps.
- **Outlines:** lock one system per project: full black, tinted, selective (sel-out), or lineless.
- **Manual AA/dithering:** apply selectively at high-contrast curves; never blur whole sprites. Use ordered/controlled dithering only where ramp steps are too wide.
- **Materials:** distinguish metal, cloth, skin, wood, stone by ramp shape and highlight behavior, not just hue.

## 4. Animation and motion standards

- Adapt the 12 principles to pixels: silhouette clarity, anticipation, snappy smears, follow-through, subpixel motion for subtle shifts.
- Lock one foot baseline/center pivot across every frame and direction. No jitter during transitions.
- Express frame durations in milliseconds or target FPS. Typical authentic pixel motion is 8-15 FPS; high-frame-rate styles may use 24-60 FPS.
- Loops must wrap seamlessly: last frame to first frame with no double-beat or hitch.
- Sync animation events (hitbox on/off, footsteps, VFX spawn, sound) to explicit frames in the production sheet.
- VFX may use partial alpha when intentional; sprites use binary alpha by default.

## 5. Export, engine, and QA gates

- Export production assets as lossless 32-bit RGBA or indexed PNG; GIF/APNG for previews; JSON/XML/Aseprite metadata for timing/slices; native editable sources (`.aseprite`, `.pxo`, `.ora`, `.blend`).
- Never export production pixel art as JPEG.
- Avoid semi-transparent edge halos; sprites use binary alpha unless VFX/shader alpha is specified.
- Engine pixel-perfect configuration: nearest/point filtering, mipmaps off, lossless/uncompressed textures, pixel snap/integer scaling, padded atlas cells to prevent bleeding.
- QA at 100% and 400% zoom, at actual gameplay/display size, on representative backgrounds, and in the engine when integration is in scope.
- Distinguish passed, failed, and not-tested checks.

## 6. AI-generated pixel art and conversion

Image models can produce useful concepts, but their output is usually a raster image with a simulated pixel grid.

- Never call a generated image "authentic pixel art" without inspecting the actual grid, palette, clusters, and alpha.
- Check for mixels (inconsistent pixel sizes), soft/blurred edges, JPEG artifacts, gradients, and semi-transparent fringe.
- Prompt for flat colors, a fixed grid, limited palette, no anti-aliasing, no gradients, no text artifacts, and a clear silhouette.
- Treat generated output as a draft/reference. Rebuild or clean it on the real grid; quantize to the approved palette; remove noise; redraw critical edges and faces.
- For conversion pipelines, document the source, method, palette, and cleanup steps. Label output as "converted pixel style" when appropriate.
- Do not copy a distinctive copyrighted character, logo, or artist's exact composition. Track licenses/provenance.
- If a tool cannot generate/edit images, provide a precise prompt, palette, grid, and manual cleanup procedure; do not claim the image exists.

## 7. Style Bible and production gates

Before bulk production, lock:

- Paradigm, native resolution, pixel scale, projection, tile/grid size.
- Palette (hex order), light direction, outline/AA/dither policy.
- Character proportions, pivots, world scale, transparency rules.
- Animation state matrix, frame budget, durations, engine events.
- Engine/editor version, import settings, naming, formats, performance budgets.
- Acceptance criteria and QA views.

Create one representative benchmark (character/prop/tile/UI) and review it at native and gameplay size before scaling production.

## 8. Delivery, naming, and provenance

- Use deterministic lowercase kebab-case names with asset ID, state, direction, and frame where applicable.
- Keep `source/`, `working/`, `export/`, `atlas/`, `metadata/`, and `qa/` separate.
- Deliver an asset manifest: file, type, dimensions, pivot, frames/durations, palette, engine settings, source, license, validation status.
- Preserve native editable sources when the tool allows.
- Do not ship third-party reference art, fonts, or brushes without rights.
- State known limitations and untested integration items.

## 9. Bundled QA utilities

```bash
# Pixel craft and alpha checks
python scripts/pixel_art_qa.py path/to/sprite.png --max-colors 32 --check-seams --cell 32x32

# Palette compliance
python scripts/pixel_art_qa.py sprite.png --palette "#0f0f1b,#f4f4f4,#c84b31"

# Package structure/frontmatter validation
python scripts/validate_package.py

# Hue-shifted palette ramp helper
python scripts/palette_ramp.py "#3a6ea5" --steps 5
```

These scripts support QA; they do not replace visual review or engine testing.
