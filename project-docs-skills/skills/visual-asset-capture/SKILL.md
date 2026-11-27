---
name: visual-asset-capture
description: "Captures genuine application screenshots and visual evidence from simulators, emulators, browsers, desktop apps, game runtimes, physical devices, and terminals. Use when a project needs accurate screenshots for documentation, READMEs, galleries, store listings, or QA evidence, especially when a clean target state, viewport, device, or privacy-safe demo data must be prepared first."
---

# Visual Asset Capture

## Mission

Obtain authentic source captures of the real application. Capture is evidence; it must not be fabricated, staged with fake UI, or silently altered to look better.

This skill produces **raw source captures**. Cleaning, slicing, and composition happen in `clean-screenshot-slicer` and `store-preview-asset-builder`.

## When to use

- A README, docs page, store listing, release note, or QA report needs screenshots.
- The user wants Garmin simulator, mobile emulator, browser, desktop, game, or terminal captures.
- Existing screenshots are dirty, inconsistent, outdated, or show the wrong state.
- You need to prepare a repeatable screenshot set for a release.

## Screenshot categories

Do not conflate these outputs:

1. **Full environment capture:** simulator/emulator window, browser chrome, desktop, or terminal, including surrounding UI. Useful as debugging evidence.
2. **Isolated device render:** real device body/bezel/strap plus active screen, background removed. Useful for device mockups and store art.
3. **Display-only capture:** only the active app display/viewport, excluding bezel, strap, browser chrome, and desktop. Useful for clean docs, galleries, and UI reviews.
4. **Designed preview:** genuine app screenshot composed into a designed graphic with background, frame, and captions. Produced by the store builder, not this skill.

Ask which output is required when the difference materially changes the result. Do not assume "screenshot" means a full window.

## Workflow

### 1. Define the target

- Application, build/version, platform, device, viewport, orientation, theme, locale.
- Screen/state/flow to capture and why it matters.
- Intended destination: docs, README, store listing, QA, presentation.
- Required output category and dimensions.
- Privacy constraints: accounts, notifications, names, emails, tokens, customer data.

### 2. Probe capture capability

Determine whether the environment can:

- control a simulator/emulator or launch a build;
- drive a browser with automation;
- capture a desktop window or game runtime;
- access a physical device;
- only process supplied images.

Do not assume simulator control from repository access. If capture is unavailable, use supplied screenshots or give exact manual steps and state that no capture was performed.

### 3. Prepare a truthful state

- Build/run the correct version.
- Use representative, synthetic, non-sensitive demo data.
- Close unrelated overlays, debug HUDs, notifications, and tooltips.
- Set the intended viewport, device, theme, locale, and orientation.
- Do not hide relevant errors/warnings or change app code just to make a screenshot.
- Capture the highest practical native resolution; preserve the original.

### 4. Capture by platform

Detailed commands are in `../../references/screenshot-capture-recipes.md`.

- **Garmin Connect IQ:** launch the simulator for the target device, navigate to the state, use the simulator screen capture (or a clean window capture), avoid overlays. Record device family and display geometry.
- **Android:** `adb exec-out screencap -p`, clean demo status bar, no notifications.
- **iOS:** `xcrun simctl io booted screenshot`, clean status bar override.
- **Web:** Playwright/Chromium at exact viewports (desktop and mobile), hide scrollbars/cookie banners, wait for stable render.
- **Desktop:** capture the app window, not the whole desktop, unless evidence requires context.
- **Games:** capture representative gameplay, not only menus; hide debug FPS/collider overlays.
- **CLI/API:** use clean terminal renders, response cards, or diagrams; avoid personal paths and tokens.

### 5. Name and record

Use deterministic names:

```text
<project>_<platform>_<screen-or-state>_<variant>_<sequence>.png
```

Record source, build/date, device/viewport, crop intent, and privacy review in a capture log or the asset manifest.

### 6. Hand off

- Keep raw files in `docs/assets/raw/`.
- Do not edit the only source.
- Pass the raw captures and desired output type to `clean-screenshot-slicer`.
- For a store pack, pass clean assets to `store-preview-asset-builder`.

## Privacy and authenticity

- Never include real customer names, emails, phone numbers, tokens, private URLs, or production data.
- Replace with realistic synthetic data.
- Do not invent app UI, metrics, ratings, or supported devices.
- Do not use AI-generated lookalike UI as product evidence.
- Redact sensitive regions if they cannot be avoided; disclose redaction.

## Output contract

- Raw capture files at native resolution.
- Capture log: app/build, platform/device/viewport, state, date, intended crop, privacy notes.
- Explicit statement of capture type and whether the capture was actually performed.
- Limitations and any manual steps required.

## Validation checklist

- [ ] Correct app, build, platform, device, and state.
- [ ] Requested screenshot category is clear.
- [ ] No debug overlays, tooltips, notifications, or unrelated windows.
- [ ] No personal data, secrets, or confidential content.
- [ ] Resolution is sufficient for the destination.
- [ ] Original captured file is preserved.
- [ ] Naming is deterministic and documented.
- [ ] If capture was impossible, the fallback is clearly labeled.

## Handoff

- `clean-screenshot-slicer` for chrome removal, transparency, and tight crops.
- `store-preview-asset-builder` for designed store/preview compositions.
- `docs-visual-qa-auditor` for final evidence review.

## Related references

- `../../references/screenshot-capture-recipes.md`
- `../../references/visual-asset-guidelines.md`
- `../../references/tool-capability-contract.md`
- `../../references/garmin-connect-iq-playbook.md`
