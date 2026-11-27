# Release-Readiness QA Checklist (Docs & Visual Assets)

## A. Technical Documentation

- [ ] `README.md` opens with a crisp 1-sentence summary and clean hero/preview graphic.
- [ ] Every install, build, and run command is verified against the actual repo.
- [ ] All relative links and image paths resolve cleanly with exact filename casing.
- [ ] Zero leftover placeholders (`TODO`, `[TBD]`, `[Insert ...]`).
- [ ] `CHANGELOG.md` reflects the exact release version and real changes.

## B. Clean Sliced Screenshots (`docs/assets/clean/`)

- [ ] Zero OS window chrome (title bars, menu bars, memory/status bars, scrollbars).
- [ ] All 4 exterior corners are fully transparent (`alpha == 0`) for device cutouts.
- [ ] Interior white UI text and icons remain 100% opaque.
- [ ] Zero bright white pixel halos around dark bezels or straps.
- [ ] Sibling screens share uniform height and aspect ratio.

## C. Store & Preview Assets (`docs/store-assets/`)

- [ ] Exact platform dimensions match spec (`COVER_500x500`, `HERO_1440x720`, `SCREEN_1..5` `1440x900`, etc.).
- [ ] Lossless `.png` masters exist in `docs/store-assets/master/`.
- [ ] Typography is crisp, high-contrast, and never collides with device frames.
- [ ] Consistent brand palette, font pairing, and baseline alignment across all slides.
- [ ] Store copy claims match real shipping features.

## D. Requirements traceability

- [ ] Every user requirement maps to a deliverable and a check result.
- [ ] Pass / Fail / Not verified / N/A is recorded per requirement.
- [ ] Unverified store requirements are explicitly labeled.

## E. Accessibility and presentation

- [ ] Images have meaningful alt text.
- [ ] Text has sufficient contrast at final size.
- [ ] Color is not the only carrier of meaning.
- [ ] Captions are readable at the smallest destination size.
- [ ] Reading order is sensible in documents and composed graphics.
- [ ] Reduced-motion/static alternatives exist where relevant.

## F. Handoff and manifest

- [ ] Asset manifest lists file, use, dimensions, source, and validation state.
- [ ] Source/working/final assets are separated.
- [ ] Editable sources are preserved where useful.
- [ ] The package is understandable without the original chat.
- [ ] Publication/submission status is stated precisely.
