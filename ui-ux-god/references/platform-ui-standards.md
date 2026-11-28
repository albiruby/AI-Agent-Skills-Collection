# Cross-Platform UI/UX Measurable Standards

Concrete platform benchmarks for auditing non-web apps and programs.

## 1. Mobile Standards (iOS HIG vs Android Material 3)

| Dimension | iOS (HIG / SwiftUI) | Android (Material 3 / Compose) |
| :--- | :--- | :--- |
| **Minimum Touch Target** | `44 x 44 pt` | `48 x 48 dp` |
| **Screen Horizontal Margin** | `16 pt` (compact) / `20 pt` (large) | `16 dp` (compact) / `24 dp` (expanded) |
| **Body Text Floor** | `17 pt` default (`>= 13 pt` secondary) | `16 sp` default (`>= 12 sp` caption) |
| **Safe-Area Handling** | `.safeAreaInset` / `GeometryReader` safeAreaInsets | `Modifier.systemBarsPadding()` / `WindowInsets.safeDrawing` |
| **Dynamic Type / Font Scaling** | Must remain usable up to `AX3` without clipping | Must remain usable up to `200%` font scale |

## 2. Desktop Standards (macOS, Windows Fluent, Electron/Tauri, Qt)

- **Window Minimum Bounds**: Define explicit `minWidth` and `minHeight` (typically `>= 800x600` for productivity apps, `>= 360x500` for utility widgets) so toolbars never wrap into collisions.
- **Custom Titlebar Clearance**:
  - macOS traffic lights reserve `~78px` on top-left (`y: 12-28px`).
  - Windows caption controls reserve `~138px` on top-right.
  - Any centered window title MUST account for asymmetric caption buttons using a 3-column grid (`1fr auto 1fr`) rather than centering in remaining space.
- **HiDPI Asset Crispness**: Require SVG or `@2x/@3x` icons; flag blurry upscaled `1x` bitmaps.
- **Divider Alignment**: Full-bleed dividers separate distinct panes (sidebar vs canvas); inset dividers (`16px` left inset or aligned to text start after leading icon) separate rows within a single list.

## 3. CLI / TUI Standards

- **Width Discipline**: Calculate display width using East-Asian / Unicode cell width (`wcwidth` / `string-width`), NEVER raw `.length` or byte count, so emojis and CJK/box glyphs never break right borders.
- **Color Portability**: Use semantic ANSI 16-color or terminal-adaptive palettes; avoid hardcoded `#000000` or `#FFFFFF` foregrounds that disappear on inverted terminal backgrounds.
- **Narrow Terminal Floor**: Layout must degrade cleanly at `80` columns without wrapping table borders or divider lines.

## 4. Web Platform Standards

- **Reflow**: usable at 320px / 400% zoom; no horizontal page scroll except data tables.
- **Mobile input**: font-size >=16px to avoid iOS auto-zoom on focus.
- **Safe areas (PWA/WebView)**: `env(safe-area-inset-*)` with `viewport-fit=cover`.
- **Viewport height**: prefer `100dvh`/`100svh` over `100vh` on mobile browsers.
- **Scrollbars**: avoid layout shift from scrollbar appearance; use `scrollbar-gutter: stable` where appropriate.
- **Fonts**: `font-display: swap`; preload critical faces; avoid invisible text.
- **Focus**: `:focus-visible` with a 2px ring and 3:1 contrast; never remove without replacement.
- **Reduced motion**: honor `prefers-reduced-motion`.
- **Dark mode**: semantic tokens; test both themes, not just the default.

## 5. Cross-Platform Frameworks (Flutter / React Native)

| Concern | Flutter | React Native / Expo |
|---|---|---|
| Safe areas | `SafeArea`, `MediaQuery.padding` | `SafeAreaView`, `useSafeAreaInsets` |
| Text scaling | `MediaQuery.textScaler` | `allowFontScaling`, `maxFontSizeMultiplier` |
| Touch targets | `MaterialTapTargetSize`, min 48dp | `hitSlop`, min 44/48 |
| Platform feel | Material vs Cupertino widgets | `Platform.select`, native navigation |
| Structure capture | Widget Inspector, `debugDumpRenderTree()` | RN Element Inspector, Detox/Appium hierarchy |
| Screenshot | `flutter screenshot` | `simctl` / `adb` |

Do not force one platform's visual language onto another unless the product has a documented cross-platform brand system.

## 6. Wearable, TV & Embedded Standards

- **Wearable**: one primary action per screen; glanceable hierarchy; large touch targets; respect round screens; crown/gesture navigation; minimal text.
- **TV**: focus ring must be obvious at 10-foot distance; remote D-pad order must be logical; overscan-safe margins (~5%); large type; avoid tiny secondary text.
- **Embedded/kiosk**: fixed resolution and orientation; touch/no-touch mode; idle/reset behavior; high-contrast, glare-tolerant palette; no reliance on hover.
- **Accessibility**: map to platform APIs (VoiceOver/TalkBack/Orca), not web ARIA.

## 7. Desktop Web Wrappers (Electron / Tauri)

- Use the native window frame or reserve space for traffic lights/caption buttons.
- Define minimum window size; test 800x600 and the product’s real minimum.
- Support Cmd/Ctrl parity and native menu shortcuts.
- Handle OS scaling (125/150/200%) and multi-monitor DPI changes.
- Do not disable native context menus, zoom, or accessibility APIs without a strong reason.
- Separate web-content zoom from app-window zoom; test both.

## 8. Dialog & Button Order Conventions

| Platform | Primary button | Secondary | Close |
|---|---|---|---|
| Web (general) | Right | Left of primary | Top-right X |
| macOS | Right | Left | Top-left traffic light / Esc |
| Windows | Left | Right of primary | Top-right X |
| iOS | Right (or full-width bottom) | Left | Cancel/back |
| Android | Right (text button) | Left | Back/X |

Follow the platform unless the product has a documented, consistent alternative. Test keyboard order, not just visual order.
