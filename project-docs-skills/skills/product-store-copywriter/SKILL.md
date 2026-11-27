---
name: product-store-copywriter
description: "Writes grounded, conversion-focused store listings, banner headlines and captions, release notes, and user-facing feature descriptions for Garmin Connect IQ Store, Apple App Store, Google Play, GitHub, Product Hunt, and web launches. Use when a project needs app-store copy, screenshot captions, What's New notes, or launch messaging that matches the actual verified product."
---

# Product Store Copywriter

## Mission

Translate verified product capabilities into clear, scannable, honest copy. Every claim must be supported by the current build, manifest, documentation, or user-supplied facts.

## When to use

- Store listing title, subtitle, description, keywords, or permissions copy.
- Banner eyebrows, headlines, subtitles, and device captions for `store-preview-asset-builder`.
- Release notes / "What's New" from a changelog or merged changes.
- GitHub About, README intro, Product Hunt tagline, launch announcement.

## Workflow

### 1. Extract verified value

- Read features, settings, supported devices/platforms, permissions, limitations, and current version.
- Convert technical capabilities into user outcomes:
  - "on-device FIT contributor" → "Adds your custom metric to the activity summary."
  - "1Hz partial updates" → "Keeps the time readable while using less battery."
- Count exact values (themes, devices, languages, modes) and never round up.
- Separate implemented features from planned work.

### 2. Fit the platform

Use `../../references/store-copy-guidelines.md` for reference limits and structure. Verify current official limits when submission compliance matters.

Typical deliverables:

1. **Title** — short, specific, no keyword stuffing.
2. **Subtitle/tagline** — one clear benefit.
3. **Banner copy matrix** — eyebrow, headline, subtitle, 2-3 word captions.
4. **Full description** — hook, feature bullets, compatibility, permissions/privacy.
5. **Release notes** — New / Improved / Fixed, user-facing.
6. **Short social/GitHub copy** — one or two lines.

### 3. Banner copy constraints

- Eyebrow: 2-4 words.
- Headline: 3-6 words.
- Subtitle: one short line (6-12 words).
- Device caption: 2-3 words naming the exact mode/screen.
- Front-load the benefit; avoid puns that obscure meaning.
- Keep text short enough for the smallest asset in the pack.

### 4. Full description structure

```text
Hook: what it is and why it matters (2 sentences)
Key features: 4-6 concrete bullets
Compatibility: verified devices/platforms/requirements
Permissions & privacy: plain-language purpose
Support/links: verified destinations only
```

### 5. Release notes

- Group under New, Improved, Fixed.
- Describe user-visible outcomes, not internal refactors.
- Include compatibility or migration actions.
- Never list unmerged/planned work as released.

### 6. Ground-check and trim

- Remove buzzwords: revolutionary, ultimate, next-gen, seamless, game-changing.
- Verify every number, device, integration, and permission.
- Check character limits.
- Check that each screenshot caption describes what is actually visible.
- Ask one focused question if a material fact is unknown; do not invent it.

## Output contract

- Copy files at the requested paths (for example `docs/store-assets/STORE_LISTING.md`).
- Banner copy matrix keyed to asset filenames.
- Release notes with version/date.
- List of claims that still need verification.
- Platform limits and check date, or "not verified".

## Validation checklist

- [ ] Every feature exists in the current build.
- [ ] Device/platform claims match manifest/config/docs.
- [ ] Numbers, counts, and limits are exact.
- [ ] Character limits fit the destination.
- [ ] Captions match the actual screens.
- [ ] No fake ratings, reviews, awards, or metrics.
- [ ] Permissions explained plainly and accurately.
- [ ] No secrets, personal data, or private endpoints.
- [ ] No marketing superlatives without evidence.
- [ ] Release notes contain released changes only.

## Related templates

- `../../templates/store-listing-template.md`
- `../../templates/release-notes-template.md`
- `../../references/store-copy-guidelines.md`

## Handoff

- Pass the banner copy matrix to `store-preview-asset-builder`.
- Pass the listing/release copy to `docs-release-packager`.
- Pass claims and evidence to `docs-visual-qa-auditor`.
