---
name: clean-screenshot-slicer
description: "Cleans and slices raw simulator, emulator, browser, desktop, and mobile screenshots into chrome-free assets: transparent device cutouts, display-only crops, or rounded viewport cards. Use when screenshots contain OS title bars, simulator menus, status bars, white canvas, browser chrome, desktop clutter, or messy borders, or when the user asks for clean sliced device screenshots ready for docs and store previews."
---

# Clean Screenshot Slicer

## Mission

Convert messy raw captures into clean PNG assets with no window chrome, no white simulator canvas, no desktop clutter, and crisp edges. Preserve the real app UI and any interior white content.

## Clean vs dirty standard

**Dirty (reject):**

- Simulator/emulator window title bar, menu bar, toolbar, or memory/status bar.
- Solid white or light-gray canvas around a watch/phone.
- Browser chrome, scrollbars, cookie banners, desktop wallpaper.
- Clipped hardware, jagged white halos, or stretched device geometry.
- Multiple devices or unrelated UI in one output.

**Clean (accept):**

- Only the intended device silhouette and active screen, or only the app viewport.
- Fully transparent exterior for device cutouts.
- Crisp anti-aliased edges with no white fringe.
- Consistent scale across sibling screens.
- Interior white text/icons remain opaque.

## Output types

| Type | Use | Default |
|---|---|---|
| Isolated device cutout | Store hero/feature graphics, device mockups | Transparent RGBA PNG |
| Display-only crop | Docs, UI galleries, screen comparisons | Rectangular PNG, no bezel |
| Viewport card | Web/desktop/mobile docs | Rounded corners + subtle shadow |
| Full environment | Debugging evidence only | Never use in final store art unless requested |

Ask when "screenshot" could mean device cutout vs display-only; the results are not interchangeable.

## Workflow

### 1. Inspect inputs

- List files, dimensions, color mode, and whether chrome/canvas is present.
- Group by device/platform and visual type.
- Choose the output type and target height per group.
- Identify a representative sample before batch processing.

### 2. Run the slicer

Use `scripts/slice_clean_device.py` (Pillow required; numpy optional). Use `python` on Windows or `python3` on macOS/Linux.

```bash
# Garmin simulator: strip chrome, isolate device, transparent background
python scripts/slice_clean_device.py \
  --input docs/assets/raw \
  --output docs/assets/clean \
  --preset garmin-sim \
  --target-height 720 \
  --padding 8

# Generic window/desktop capture
python scripts/slice_clean_device.py \
  --input docs/assets/raw/app.png \
  --output docs/assets/clean/app.png \
  --preset window-clean \
  --crop-top 60 --crop-bottom 28

# Web/mobile viewport card with rounded corners
python scripts/slice_clean_device.py \
  --input docs/assets/raw/dashboard.png \
  --output docs/assets/clean/dashboard.png \
  --preset viewport-card \
  --radius 24
```

Available presets: `garmin-sim`, `window-clean`, `chroma-key`, `viewport-card`.

Useful options: `--crop-top`, `--crop-bottom`, `--crop-left`, `--crop-right`, `--tolerance`, `--padding`, `--target-height`, `--bg-color`, `--radius`.

### 3. Check the report

The script prints JSON with output size, transparent ratio, and `corners_transparent`. A valid device cutout should report transparent corners and a sensible bounding box.

### 4. Visual QA

Follow `../../references/slicing-qa-rules.md`:

- Four exterior corners alpha = 0.
- No white halo around dark bezels.
- No clipped straps, lugs, buttons, or phone corners.
- Interior white UI preserved.
- Sibling devices equal height/scale.
- Expected display geometry (round stays round; no stretch).

### 5. Iterate

- Adjust `--crop-top`/`--crop-bottom` for non-standard simulator toolbars.
- Adjust `--tolerance` if background removal leaves fringe or eats the device.
- Use `--bg-color` for a known solid background.
- Re-run on a sample before the batch.
- If automation is uncertain, provide manual crop coordinates and ask for a reference crop rather than shipping a bad cutout.

## Transparency rules

- Use **edge-connected flood fill**, never global white replacement. Global keying destroys white text/icons inside the app.
- Keep exterior transparent only when the output is a device cutout; display-only crops may be opaque rectangles.
- Save clean device assets as lossless PNG. Do not JPEG-compress a transparent cutout.
- Avoid repeated resampling; normalize height once per sibling group.

## Garmin notes

- The simulator window may include title bar, menu bar, white canvas, and memory/status bar.
- The watch bezel and round display are different boundaries. Decide whether the output includes the bezel.
- Prefer a high-resolution simulator device for store art.
- Avoid tooltips, mouse cursors, and OS notifications over the watch.
- Use realistic demo data, not empty `0` or debug states.

See `../../references/garmin-connect-iq-playbook.md`.

## Fallback when scripts are unavailable

- Use any available image editor/API to crop the known bounds and remove the exterior background.
- Provide the user with exact crop regions and a QA checklist.
- Do not claim the image was cleaned if no processing occurred.
- If only a text-only harness is available, provide the command to run and ask for the output image.

## Output contract

- Clean PNG files in `docs/assets/clean/`.
- Processing report (input/output size, transparency, corners) or equivalent evidence.
- Mapping from raw file to clean output.
- Statement of output type, target height, and any manual adjustments.
- Known defects or images requiring manual review.

## Validation checklist

- [ ] Zero simulator/OS/browser chrome.
- [ ] Correct output type (device vs display-only vs viewport card).
- [ ] Exterior transparency only where intended.
- [ ] Interior white UI preserved.
- [ ] No white halo, clipping, or aspect distortion.
- [ ] Sibling assets share scale/height.
- [ ] Lossless PNG for device cutouts.
- [ ] Raw originals untouched.
- [ ] Every output visually reviewed or flagged.

## Handoff

- Clean device cutouts go to `store-preview-asset-builder`.
- Display-only/viewport images go to docs or galleries.
- Final assets go to `docs-visual-qa-auditor`.
