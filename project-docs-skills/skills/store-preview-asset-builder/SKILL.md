---
name: store-preview-asset-builder
description: "Composes store-ready and preview graphics from clean transparent screenshots using a declarative JSON manifest: covers, hero banners, multi-device feature showcases, mobile store panels, GitHub social cards, and Open Graph images. Use when a project needs Garmin Connect IQ Store, Apple App Store, Google Play, web/GitHub, Product Hunt, or README preview visuals built from real clean screenshots."
---

# Store Preview Asset Builder

## Mission

Turn clean, transparent screenshots into a cohesive asset set that looks professionally designed and remains truthful to the product. Generate lossless masters and destination-ready exports from one locked visual system.

## When to use

- A Garmin Connect IQ app needs Cover/Hero/Feature screens.
- A mobile app needs App Store/Play Store preview panels.
- A web project needs OG/GitHub social cards or a README hero.
- A release needs a consistent feature gallery.
- A docs pack needs polished preview visuals.

Do not use this skill to clean screenshots; that is `clean-screenshot-slicer`. Do not use it to invent UI.

## Inputs

- Clean transparent device cutouts or clean viewport images.
- Verified feature headlines/captions (from `product-store-copywriter` or user-approved copy).
- Brand palette, fonts, and logo assets, if available.
- Exact destination dimensions and format from current official requirements, or a user-supplied spec.

## Workflow

### 1. Verify inputs and requirements

- Confirm every source image is clean, chrome-free, and the correct output type.
- Verify all devices in a set share scale/height.
- Look up dimensions/formats in `../../references/store-asset-specs.md` and, for submission, current official platform documentation.
- Record the source URL and date checked. If unavailable, mark compliance **not verified**.
- Lock one palette, font pairing, background treatment, and device framing for the whole set.

### 2. Choose layouts

| Layout | Best for | Notes |
|---|---|---|
| `cover` | Square icon/cover | One hero device, short title/tagline |
| `hero_overlap` | Hero banner, social card | 1-3 devices in a V-overlap, copy on the right |
| `feature_showcase` | Feature screens | 3 equal-height devices on a shared baseline, captions below |
| `mobile_panel` | Portrait store screenshot | Large device, copy above/below, generous safe margins |

### 3. Write the manifest

Start from `../../templates/garmin-ciq-manifest.json` or `../../templates/web-mobile-manifest.json`.

```json
{
  "theme": {
    "bg_top": "#0D2452",
    "bg_bottom": "#040A18",
    "title_color": "#5CE1FF",
    "subtitle_color": "#F1F5F9",
    "caption_color": "#FACC15",
    "muted_color": "#94A3B8",
    "accent": "#38BDF8",
    "decor": "pixel-squares",
    "font_bold": null,
    "font_regular": null
  },
  "assets": [
    {
      "output": "COVER_500x500.jpg",
      "layout": "cover",
      "width": 500,
      "height": 500,
      "title": "APP TITLE",
      "subtitle": "SHORT TAGLINE",
      "images": [{ "src": "../assets/clean/watch_main.png" }]
    }
  ]
}
```

Paths in `src` resolve relative to the manifest file. Keep `manifest.json` beside the outputs and clean assets nearby.

### 4. Render

```bash
python scripts/compose_store_assets.py \
  --manifest docs/store-assets/manifest.json \
  --output-dir docs/store-assets
```

The script writes:

- Lossless PNG masters in `docs/store-assets/master/`.
- Optimized JPG/PNG deliverables beside the manifest.

### 5. Review and iterate

- View every output at actual size.
- Check text fit, collision with devices, contrast, alignment, and consistent baselines.
- Verify dimensions and file size.
- Adjust copy length, font size, palette, or device scale in the manifest and re-run.
- Keep the manifest as the editable source of truth.

## Composition rules

- Product UI is the primary evidence; decoration is secondary.
- Headlines 3-6 words; subtitles one short line; device captions 2-3 words.
- Keep at least 8% side margins in multi-device layouts.
- Do not stretch devices; preserve aspect ratio and use padding.
- Keep dark bezels legible on dark backgrounds with subtle glow/contrast.
- Use accessible contrast; do not rely on color alone.
- Keep one visual system across the whole pack.
- Do not place text over essential UI.

See `../../references/visual-composition-guide.md`.

## Platform notes

- **Garmin:** Cover 500x500, Hero 1440x720, Feature 1440x900 (verify current store requirements).
- **Apple:** portrait screenshot sizes vary by device; icon must follow alpha constraints.
- **Google Play:** feature graphic and phone screenshots have separate specs.
- **Web/GitHub:** OG 1200x630, GitHub social 1280x640.
- Requirements change; prefer official sources and record the check date.

## Output contract

- `manifest.json` (editable source).
- Lossless masters in `master/`.
- Destination-ready assets with deterministic names.
- Dimension/format/size report.
- List of unverified platform requirements.
- Clear statement of which layouts and devices were used.

## Validation checklist

- [ ] All source screenshots are clean and genuine.
- [ ] Correct output dimensions and formats.
- [ ] Lossless masters exist for every final asset.
- [ ] No stretched/distorted devices.
- [ ] Text is legible, high-contrast, and does not collide.
- [ ] Devices align on a consistent baseline and scale.
- [ ] One palette/font system across the set.
- [ ] Claims match verified features.
- [ ] File sizes acceptable for the destination.
- [ ] Requirements checked or marked unverified.

## Gotchas

- A beautiful banner with wrong numbers or mismatched UI is a failure.
- Do not reuse a manifest from another project without replacing all copy, paths, and palette.
- Do not ship JPG as the only master for transparent assets.
- Do not let text touch device bezels or safe-area edges.
- Do not assume one store's dimensions apply to another placement.

## Handoff

- Send the final pack to `docs-visual-qa-auditor`.
- Send the manifest and masters to `docs-release-packager`.
- If copy is missing, route to `product-store-copywriter` before rendering.
