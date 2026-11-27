# Example: Garmin Connect IQ Watch Face

End-to-end flow for a store-bound Monkey C watch face. The app names and sizes are illustrative; verify device support and current store requirements.

## 1. Request

> Document this Garmin watch-face project. Capture the simulator states, produce clean transparent watch images, and build a Garmin IQ Store cover, hero, and three feature screens. Keep the README accurate and ready to publish.

## 2. Context

Inspect:

- `manifest.xml`, `monkey.jungle`, `.mc` sources.
- Declared device families and display types.
- Implemented features: time, steps, battery, AOD, settings, complications.
- Existing icons, screenshots, fonts, palette.
- Target store placements and their current requirements.

Do not infer device support from a screenshot. Do not claim AOD/battery behavior without evidence.

## 3. Plan

| Deliverable | Details |
|---|---|
| README | Device support, build/run, features, clean preview, limitations |
| Architecture/device notes | Rendering loop, settings, battery/AOD behavior |
| Raw captures | 4 states at native simulator resolution |
| Clean device PNGs | Transparent, equal height, chrome-free |
| Store assets | Cover 500x500, Hero 1440x720, 3 feature screens 1440x900, masters |
| Copy | Store description + banner matrix + release notes |
| QA | Automated validator + visual review |

## 4. Capture raw states

For each state:

1. Launch the simulator for the intended high-resolution device.
2. Load realistic demo data (not empty `0` or debug values).
3. Remove tooltips, cursor, notifications, and overlapping windows.
4. Capture the simulator screen at native resolution.
5. Save under `docs/assets/raw/`.

Recommended states: main time, activity/steps, battery/status, AOD or a second theme.

## 5. Clean and slice

From the pack root:

```bash
python skills/clean-screenshot-slicer/scripts/slice_clean_device.py \
  --input docs/assets/raw \
  --output docs/assets/clean \
  --preset garmin-sim \
  --target-height 720 \
  --padding 8
```

Check the JSON report:

- `corners_transparent: true`
- Sensible output size
- No white halo or clipped bezel/strap

If the simulator toolbar height differs, tune `--crop-top`/`--crop-bottom`. If the background is not removed well, tune `--tolerance`.

For a display-only crop (no bezel), crop inside the round display and preserve the circle. Do not stretch it to a square.

## 6. Compose store assets

Create `docs/store-assets/manifest.json` from `../templates/garmin-ciq-manifest.json`:

- Cover: one hero watch, title + short tagline.
- Hero: 3 watches in a V-overlap, value proposition, highlight pills.
- Feature screens: 3 equal-height watches, one takeaway per slide.

Use headline 3-6 words; captions 2-3 words.

```bash
python skills/store-preview-asset-builder/scripts/compose_store_assets.py \
  --manifest docs/store-assets/manifest.json \
  --output-dir docs/store-assets
```

Verify:

- `master/` contains lossless PNGs.
- Final JPG/PNG dimensions match filenames.
- Text does not collide with watches.
- Devices share baseline/scale.
- Dark bezels stay legible on the dark background.

## 7. Documentation

Create:

- `README.md`: one-line value, clean hero, verified features, supported devices, build/run, limitations.
- `docs/ARCHITECTURE.md`: views, state, update loop, settings, AOD/battery notes.
- `docs/USER_GUIDE.md`: controls, modes, settings.
- `CHANGELOG.md` + release notes.

Embed only clean assets. Link deep detail instead of duplicating it.

## 8. Copy

Banner matrix:

| Asset | Eyebrow | Headline | Subtitle | Captions |
|---|---|---|---|---|
| Hero | `GARMIN WATCH FACE` | `Your day at a glance` | `Time, steps, and battery in one clean view.` | — |
| Screen 1 | `CORE` | `Read it in a second` | `Large time with a calm, high-contrast layout.` | `Time` / `Steps` / `Status` |
| Screen 2 | `THEMES` | `Match your watch` | `Switch themes without losing your settings.` | `Dark` / `Light` / `Minimal` |

Store description: hook, verified features, device compatibility, permissions, support link. Release notes: New/Improved/Fixed.

## 9. QA

```bash
python skills/docs-visual-qa-auditor/scripts/validate_doc_pack.py \
  --project-root . \
  --clean-dir docs/assets/clean \
  --store-dir docs/store-assets
```

Then visually inspect:

- No raw simulator chrome.
- Transparent corners; no white box.
- Round display not stretched.
- No clipped content.
- Store dimensions/format correct or marked unverified.
- Claims match the manifest/source.

## 10. Handoff

```text
README.md
docs/
  ARCHITECTURE.md
  DEVICES.md
  USER_GUIDE.md
  assets/raw/
  assets/clean/
  store-assets/
    COVER_500x500.jpg
    HERO_1440x720.jpg
    SCREEN_1_*.jpg
    SCREEN_2_*.jpg
    SCREEN_3_*.jpg
    master/
    manifest.json
CHANGELOG.md
docs/qa-report.md
```

State clearly what was captured, cleaned, composed, validated, and what store requirements remain unverified.
