# Case 03 — Native Mobile Platform Audit

## Fixture

A fictional React Native/Expo checkout app with:

- A bottom CTA overlapping the iOS home-indicator area.
- A 32dp Android filter icon-only button.
- A coupon field hidden by the iOS keyboard.
- Android back from Item detail exiting the app on a deep-link entry.
- A price clipped at iOS AX3 / Android 200% text scale.
- A blank screen when offline.
- iOS simulator and Android emulator available; source access.

## Prompt

> Audit the checkout flow on iOS 17 and Android 14. Check safe areas, touch targets, keyboard behavior, back navigation, large text, and offline. Fix the verified issues and show before/after evidence.

## Expected behavior

1. Capture real simulator/emulator frames and view hierarchy.
2. Record device, OS, build, orientation, theme, and text scale.
3. Treat safe-area/keyboard/back as functional defects, not polish.
4. Measure touch targets in pt/dp; distinguish 44/48 recommendation from 24px floor.
5. Test large text (AX3/200%) and long localized strings.
6. Add an offline state with cached content + retry.
7. Re-test on the same device/OS; state what was not tested (physical device, other OS versions).

## Evidence required

- Safe area: button frame vs inset, before/after.
- Touch: `uiautomator`/accessibility bounds before/after.
- Keyboard: field position vs keyboard top.
- Back: navigation path before/after, deep link case.
- Large text: screenshot at AX3/200%.
- Offline: state screenshot + retry behavior.

## Scoring focus

| Criterion | Must show |
|---|---|
| Platform evidence | Real device/simulator, units, conventions |
| Root cause | SafeArea/insets, native stack/back handler, KeyboardAvoidingView |
| Repair quality | Preserve visual size while expanding hit area |
| Verification | Same device/state, adjacent text scale/orientation |
| Coverage honesty | Physical device/OS versions not tested |

## Failure modes

- Auditing from desktop screenshots at 375px and calling it mobile.
- Fixing the safe area with a hardcoded `paddingBottom: 12`.
- Making the icon visually 48dp instead of expanding the hit area.
- Adding `BackHandler` that exits instead of navigating.
- Using `adjustsFontSizeToFit` to shrink the price below readability.
- Treating offline as a backend-only issue.
