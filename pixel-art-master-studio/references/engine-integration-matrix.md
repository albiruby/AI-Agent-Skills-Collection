# Engine Integration Matrix

Working defaults for pixel-perfect integration. Verify the installed engine version and current official documentation before applying version-specific settings.

## 1. Universal rules

- Texture filter: **Nearest/Point**.
- Mipmaps: **Off**.
- Compression: **None/lossless** for crisp pixel assets.
- Wrap: Clamp for sprites/atlases; Repeat only for seamless parallax.
- Integer scaling and pixel snapping for camera/transforms.
- Atlas padding/extrusion to prevent texture bleeding.
- Test at 720p, 1080p, 1440p, and the target aspect ratio.

## 2. Godot 4

- Project Settings -> Rendering -> Textures -> Default Texture Filter: `Nearest`.
- Display -> Window -> Stretch:
  - Mode: `canvas_items` for scalable UI/world, or `viewport` for strict pixel lock.
  - Scale mode: `integer`.
- Enable `Snap 2D Transforms to Pixel` and `Snap 2D Vertices to Pixel`.
- TileSet: configure terrain sets; add atlas margins/extrusion (commonly 1 px).
- Camera2D: test zoom and position snapping; avoid fractional camera positions with unsnapped sprites.
- UI: use a separate CanvasLayer with a compatible scale if world is low-res.

## 3. Unity 2D (URP)

- Texture importer: Filter Mode `Point (no filter)`, Compression `None`.
- Pixels Per Unit (PPU) should match the tile size (for example 16 or 32).
- Use the 2D Pixel Perfect Camera component: Assets PPU, Reference Resolution, Upscale Render Texture/Crop Frame.
- Sprite Atlas: padding, no compression, tight packing off if it changes pivots.
- Animator: frame durations in seconds; match the exposure sheet.
- Canvas: separate screen-space UI or scale with integer factors.

## 4. GameMaker

- Disable `Interpolate colors between pixels`.
- Set the application surface to the native art resolution and upscale to the window.
- Texture groups: avoid compression; set texture page size appropriate to the project.
- Camera/view: integer positions and sizes; test room transitions.
- Nine-slice UI: verify border slices at integer scale.

## 5. RPG Maker MZ

- Disable smoothing where supported; keep asset sizes on the engine's grid.
- Match tile size and character sheet layout exactly; verify frame order.
- Test passability, character offsets, and animation speed.
- Avoid mixing plugin-generated scaling with native pixel art.

## 6. Defold

- Set texture filter to nearest; disable mipmaps/compression.
- Use integer scaling and a fixed render script; test camera/viewport.
- Atlas: padding/extrusion; verify animation playback.
- GUI: separate node scaling for crisp UI.

## 7. Web / HTML5 Canvas / Phaser

```js
ctx.imageSmoothingEnabled = false;
```

```css
canvas { image-rendering: pixelated; }
```

- Size the internal canvas to the native resolution; scale the CSS/window by integer factors.
- Avoid CSS transforms that produce fractional scaling.
- Phaser: `pixelArt: true`, `roundPixels: true`, `antialias: false`.
- Test devicePixelRatio and fullscreen behavior.

## 8. Validation scene

Create a minimal scene with:

1. One sprite with transparent edges.
2. One animation with mixed frame durations.
3. One tileset with terrain transitions.
4. A moving camera and a UI overlay.

Test:

- Camera movement in diagonals and at different speeds.
- Window resize, fullscreen, and aspect-ratio changes.
- Animation state transitions and loop seams.
- Tile adjacency, corners, and one-way platforms.
- UI text/icons at the target scale.

## 9. Common failures

- Linear filtering or compression left on for one texture.
- Mipmaps enabled for a sprite atlas.
- Camera at fractional positions while sprites snap.
- Atlas padding too small; neighbor tiles bleed.
- UI rendered at world pixel scale, becoming unreadable.
- Mixing 1x and 2x pixel assets.
- Testing only in the editor at a non-native zoom.
- Claiming "pixel-perfect" without a runtime test.
