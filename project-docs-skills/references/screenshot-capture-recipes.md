# Platform Screenshot Capture Recipes

Use these recipes to capture crisp raw inputs before slicing.

## 1. Garmin Connect IQ Simulator (Monkey C)

- **Recommended Device**: Pick a flagship high-res round AMOLED device (e.g., Forerunner 965 / 570 47mm, Fenix 8, Epix Gen 2) for store hero banners so bezels and typography stay razor-sharp.
- **Keep Window Unobstructed**: Ensure no tooltips, mouse cursors, or OS notifications overlap the watch bezel.
- **Simulate Realistic State**: Load meaningful demo data (realistic coins/metrics/activity state, never empty `0` states or debug overlays).
- **Slice Command**:

```bash
python3 skills/clean-screenshot-slicer/scripts/slice_clean_device.py \
  --input docs/assets/raw \
  --output docs/assets/clean \
  --preset garmin-sim \
  --target-height 720
```

## 2. Android (Emulator or Physical Device)

Enable clean demo status bar (full battery, clean clock, no clutter notifications), then capture lossless PNG directly:

```bash
adb shell settings put global sysui_demo_allowed 1
adb shell am broadcast -a com.android.systemui.demo -e command clock -e hhmm 0941
adb shell am broadcast -a com.android.systemui.demo -e command battery -e level 100 -e plugged false
adb shell am broadcast -a com.android.systemui.demo -e command notifications -e visible false
adb exec-out screencap -p > docs/assets/raw/android_home.png
```

## 3. iOS Simulator (macOS)

```bash
xcrun simctl status_bar booted override --time "9:41" --batteryState charged --batteryLevel 100 --wifiBars 3
xcrun simctl io booted screenshot docs/assets/raw/ios_home.png
```

## 4. Web Apps & Dashboards (Playwright / Headless Chromium)

Capture exact desktop (`1440x900`) and mobile (`390x844`) viewports at `deviceScaleFactor: 2` (Retina), hiding scrollbars and cookie banners before snapping:

```js
await page.setViewportSize({ width: 1440, height: 900 });
await page.addStyleTag({ content: '::-webkit-scrollbar { display: none !important; }' });
await page.screenshot({ path: 'docs/assets/raw/web_dashboard.png', fullPage: false });
```

Then wrap with subtle rounded corners and shadow:

```bash
python3 skills/clean-screenshot-slicer/scripts/slice_clean_device.py \
  --input docs/assets/raw/web_dashboard.png \
  --output docs/assets/clean/web_dashboard.png \
  --preset viewport-card \
  --radius 24
```

## 5. Desktop Applications

- Capture only the application window, not the full desktop, unless context is evidence.
- Use OS window capture or the app's own screenshot feature.
- Remove desktop wallpaper, other windows, and OS notifications.
- If the app has a light/dark theme, match the documentation theme and record it.
- For multi-window workflows, capture the meaningful state rather than every panel.

## 6. Games

- Capture representative gameplay, not only menus or splash screens.
- Hide debug overlays (FPS, colliders, console) unless they are the subject.
- Use a deterministic save/state; avoid personal account names.
- Record resolution, aspect ratio, build, and scene.
- For store art, capture clean HUD states at the highest practical resolution.
- Do not fabricate gameplay; use the real build.

## 7. CLI, API, and Developer Tools

- Use a clean terminal theme with readable contrast; hide personal paths, hostnames, tokens, and shell history.
- Show real commands and real output; truncate long output intentionally.
- For APIs, prefer request/response cards or an API explorer capture over a fake terminal.
- For libraries, use code snippets plus architecture/sequence diagrams.
- Do not include API keys, authorization headers, or customer data.
- If output is synthetic, label it as an example, not observed production behavior.

## 8. Manual fallback and privacy

If the harness cannot drive a simulator, browser, or device:

1. Give exact manual steps for the target platform.
2. Ask for captures at native resolution.
3. Process the supplied files without claiming a live capture.
4. Record the limitation in the handoff.

Before capture, check for:

- Personal names, emails, phone numbers, avatars, notifications.
- Health, financial, location, or customer data.
- Tokens, private URLs, internal hostnames.
- Confidential project names or unreleased features.

Redact only when necessary; disclose redaction and keep the original evidence separate.
