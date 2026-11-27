# Pixel Art Engine Validation

- Engine + exact version:
- Render pipeline/backend:
- Target platform(s):
- Internal render resolution:
- Display/window resolution(s):
- Texture filter/sampling:
- Mipmap/compression settings:
- Camera snapping/pixel-perfect setup:
- Integer scaling/aspect-ratio policy:
- Sprite pivot/origin policy:
- Tilemap/terrain/autotile configuration:
- Sorting/layering/parallax:
- UI scale and safe areas:

## Test cases
- [ ] Static sprite at native internal resolution
- [ ] Sprite at all target output scales
- [ ] Moving camera and moving sprite
- [ ] Diagonal movement and subpixel motion
- [ ] Animated sprite and loop playback
- [ ] Tile adjacency and map edges
- [ ] Transparent edges/atlas padding
- [ ] UI text and icons
- [ ] Aspect-ratio/window resize
- [ ] Representative target hardware performance

## Findings
| Test | Result (pass/fail/not tested) | Evidence | Fix/owner |
|---|---|---|---|
