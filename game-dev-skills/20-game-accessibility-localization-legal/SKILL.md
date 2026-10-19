---
name: game-accessibility-localization-legal
description: Accessibility, localization/internationalization, privacy, age ratings, licensing and legal compliance for games (GDPR, COPPA, loot box rules, IP, open-source licenses, AI-content disclosure).
---

# Accessibility, Localization & Legal
(Not legal advice: recommend professional counsel for contracts and compliance.)

## Accessibility (ref: Game Accessibility Guidelines, Xbox Accessibility Guidelines)
- **Visual**: colorblind-safe palettes + shape/icon redundancy, UI scale, high-contrast mode, subtitles with size/background/speaker names, no information by color alone, reduce flashing (WCAG: <= 3 flashes/s; photosensitivity warning), screen shake/motion blur/camera bob toggles.
- **Motor**: full rebinding, hold-to-toggle, one-handed modes, adjustable timing/QTE alternatives, aim assist, auto-run, large touch targets.
- **Cognitive**: clear objectives/quest reminders, adjustable difficulty/assist, skippable puzzles, tutorial replay, pause anywhere, simple language option.
- **Auditory**: visual cues for sounds, captions, separate volume buses, mono audio.
- Provide an accessibility menu early (first-run), and test with disabled players where possible.

## Localization (i18n/l10n)
- All text in string tables with stable keys; no concatenated sentences (use placeholders/ICU plural rules); no text baked in images.
- Plan languages by market (EN, ES, PT-BR, FR, DE, RU, ZH-CN/TW, JA, KO, ID, TR, AR...); fonts with full glyph coverage (CJK, Thai, Arabic, Devanagari); RTL layout support; expansion margin 30-40% for UI text; date/number/currency formats; cultural review of icons/colors/gestures/content; localized store pages; pseudo-localization test; voice-over strategy (subtitles-only vs dubbing).
- Tools: Crowdin, Lokalise, POEditor, Weblate, engine localization packages, spreadsheet pipeline (CSV/PO/JSON).

## Privacy & compliance
Privacy policy + terms, data inventory (what, why, where stored), consent flows (GDPR/UK GDPR, CCPA/CPRA, Indonesia PDP Law, LGPD), COPPA/children's codes for under-13 audiences (no behavioral ads, parental consent), ATT/Google Play data safety forms, analytics/ads SDK disclosure, account deletion path (required on major mobile stores), data retention, breach plan.
**Age ratings**: ESRB, PEGI, IARC (digital stores), USK, CERO, GRAC, local regulators (e.g. Indonesia IGRS); content descriptors honest.
**Gambling/loot boxes**: regional restrictions; disclose odds; avoid real-money payouts without licenses.

## IP & licensing
Own or license all assets (fonts, music, sprites, code); track licenses (CC-BY attribution, CC0, MIT/GPL implications for engines/libraries), no trademarked names/likeness, trademark search for game title, third-party SDK terms, AI-generated content terms and store disclosure rules, contributor agreements, EULA, credits file.

## Output
Accessibility option list with priority, localization plan + string table spec, compliance checklist per target market/platform, license register template, ratings plan.
