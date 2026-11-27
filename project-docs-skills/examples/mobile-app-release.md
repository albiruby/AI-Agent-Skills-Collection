# Example: Mobile App Release

## 1. Request

> Prepare App Store and Google Play screenshots, a README, and release notes for this Flutter app. Use real screenshots and clean status bars.

## 2. Context

- Platforms and supported devices.
- Implemented flows and localization.
- Existing icon, brand colors, fonts.
- Current store requirements and target placements.
- Privacy/permissions used.

## 3. Capture source states

iOS Simulator:

```bash
xcrun simctl status_bar booted override --time "9:41" --batteryState charged --batteryLevel 100 --wifiBars 3
xcrun simctl io booted screenshot docs/assets/raw/ios_home.png
```

Android:

```bash
adb shell settings put global sysui_demo_allowed 1
adb shell am broadcast -a com.android.systemui.demo -e command clock -e hhmm 0941
adb shell am broadcast -a com.android.systemui.demo -e command battery -e level 100 -e plugged false
adb shell am broadcast -a com.android.systemui.demo -e command notifications -e visible false
adb exec-out screencap -p > docs/assets/raw/android_home.png
```

Use synthetic accounts and data. Remove test banners, debug overlays, and personal notifications.

## 4. Clean

- Keep native device screenshots for store panels.
- If a device frame is needed, use a genuine frame or a clearly labeled mockup.
- If removing a background, preserve the phone corners and screen content.
- Do not stretch screenshots to another aspect ratio; use padding/canvas.

## 5. Compose store panels

Use `mobile_panel` for portrait store screenshots. Keep:

- One feature per panel.
- Large device, readable caption.
- Safe margins.
- Consistent palette across the set.
- Text that survives small preview sizes.

Verify current Apple/Google dimensions and formats before export; record the check date.

## 6. Documentation

- README: value, supported platforms, setup/build, screenshots, permissions, limitations.
- User guide: core tasks and settings.
- Release notes: New/Improved/Fixed + migration actions.
- Privacy/permissions explanation in plain language.

## 7. QA

- No unclean status bars, personal data, or test banners.
- Correct device/OS version and screen state.
- Store dimensions match current official requirements.
- Text is legible at thumbnail size.
- No unsupported device/platform claims.
- Screenshots match available features.

## 8. Handoff

Include source captures, clean assets, store panels, masters, manifest, QA report, and a list of unverified store requirements.
