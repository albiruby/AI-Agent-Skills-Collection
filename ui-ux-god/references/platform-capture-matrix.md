# Platform Capture & Inspection Matrix

Use this matrix to capture real rendered frames and structural UI trees across every platform type before auditing.

| Platform / Stack | Live Frame Capture Method | Structural / Geometry Tree Source | Primary Audit Tools |
| :--- | :--- | :--- | :--- |
| **Web (Next.js, React, Vue, Svelte, Plain HTML)** | Playwright headless Chromium (`page.screenshot({ fullPage: true })`) | Live DOM `getBoundingClientRect()` + `getComputedStyle()` | `dom_geometry_audit.mjs`, `design_token_audit.mjs`, `interactive_a11y_audit.mjs`, `pixel_precision_audit.py` |
| **Desktop Web-Wrapper (Electron, Tauri)** | Playwright connected via CDP (`--remote-debugging-port=9222`) or WebDriver | Live WebView DOM + Window bounds | Same Web scripts + `uiux-cross-platform-app-auditor` window/HiDPI checks |
| **Mobile (Flutter)** | `flutter screenshot` or Integration Test `takeScreenshot()` + DevTools | Flutter Widget Inspector / Semantics Tree dump (`debugDumpRenderTree()`) | `pixel_precision_audit.py` + `uiux-cross-platform-app-auditor` |
| **Mobile (React Native / Expo)** | `xcrun simctl io booted screenshot` (iOS) / `adb exec-out screencap -p` (Android) | Detox / Appium UI hierarchy XML or RN Element Inspector | `pixel_precision_audit.py` + `uiux-cross-platform-app-auditor` |
| **Native iOS (SwiftUI / UIKit)** | `xcrun simctl io booted screenshot` + Xcode View Hierarchy | Accessibility Inspector / XCUITest frame dump | `pixel_precision_audit.py` + `uiux-cross-platform-app-auditor` |
| **Native Android (Compose / Views)** | `adb exec-out screencap -p` | `adb shell uiautomator dump` (exact XML bounds `[x1,y1][x2,y2]`) | `pixel_precision_audit.py` + `uiux-cross-platform-app-auditor` |
| **Desktop Native (Qt, WPF, WinUI, GTK)** | OS window capture (`screencapture`, `grim`, PowerShell/PIL) | UI Automation Tree (Windows) / Accessibility API (macOS) / GammaRay (Qt) | `pixel_precision_audit.py` + `uiux-cross-platform-app-auditor` |
| **CLI / TUI (Ink, BubbleTea, Textual, Rich)** | Terminal screenshot or ANSI-to-SVG/PNG capture at fixed columns (80x24, 120x40) | Rendered character grid buffer (exact row/col width checks) | Box-drawing continuity check + `uiux-cross-platform-app-auditor` |

## Standard Viewport Capture Set (Web)

Always capture at least 3 breakpoints; use the full 5-point set for flagship audits:

1. `mobile-375`: `375 x 812` (iPhone standard, DPR 2)
2. `mobile-320`: `320 x 568` (Minimum small-screen stress test)
3. `tablet-768`: `768 x 1024` (iPad portrait)
4. `desktop-1440`: `1440 x 900` (Standard laptop/desktop)
5. `wide-1920`: `1920 x 1080` (Full HD monitor, checks max-width containment and ultra-wide alignment)

## Capture Setup Checklist

Before capturing, record and preserve:

- **Build/commit** and environment (local, preview, production).
- **Route(s)** and navigation entry point.
- **Auth state**: storage state/cookies for web; app login/biometrics for native.
- **Theme**: light/dark/system, and the resolved theme.
- **Locale/timezone**: language, date/number format, timezone.
- **Zoom/scale**: browser zoom, OS display scale, DPR.
- **Data state**: seeded fixtures, empty state, long content, error state.
- **Motion**: `prefers-reduced-motion` on/off.

### Web auth/storage state

```bash
# Save a logged-in state once, reuse it for every capture
npx playwright codegen --save-storage=auth.json http://localhost:3000
```

```js
const context = await browser.newContext({ storageState: 'auth.json' });
```

Do not commit `auth.json`; it contains session credentials.

### Route capture

```bash
node ../../scripts/dom_geometry_audit.mjs \
  --url http://localhost:3000 \
  --routes /,/pricing,/checkout \
  --viewports mobile,tablet,desktop \
  --out ./audit-out
```

## Wearable, TV & Embedded Capture

| Target | Capture | Structure | Key checks |
|---|---|---|---|
| **watchOS** | Xcode simulator screenshot | Accessibility hierarchy | Glanceable hierarchy, crown/gesture navigation, tiny safe areas |
| **Wear OS** | Emulator screenshot | `uiautomator dump` | Round-screen insets, swipe dismissal, ambient mode |
| **tvOS / Android TV** | Simulator/emulator capture | Accessibility/UI tree | Focus ring, remote navigation, overscan-safe margins, large type |
| **Embedded/kiosk** | Device capture or vendor tool | Vendor UI tree | Fixed resolution, touch/no-touch, glare/contrast, idle reset |
| **WebView in native** | Device capture | WebView DOM via remote debugging | Safe areas, bridge behavior, scroll containment |

## Terminal / CLI Capture

- Capture at **80x24** and **120x40**; record terminal, font, theme, and locale.
- Preserve exact columns; do not let the terminal reflow before capture.
- Check wide Unicode/emoji with `wcwidth`; strip ANSI before measuring plain text.
- Test dark and light terminal themes, and `NO_COLOR=1`.
- Save the raw ANSI output plus a PNG/SVG rendering when available.

## Evidence Index Template

| # | Surface | State | Viewport/device | Theme/locale | Evidence path | Tool | Result |
|---|---|---|---|---|---|---|---|
| 1 | `/` | default | 1440x900, DPR 1 | light, en-US | `audit-out/home-1440.png` | Playwright | inspected |
| 2 | `/checkout` | error | 375x812, DPR 2 | light, en-US | `audit-out/checkout-375-error.png` | Playwright | inspected |
| 3 | Settings | default | iPhone 15, iOS 17 | dark, en-US | `audit-out/ios-settings.png` | Simulator | partial — no AT |
