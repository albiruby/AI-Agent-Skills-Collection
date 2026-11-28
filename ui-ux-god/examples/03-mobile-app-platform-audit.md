# Example 3 — Mobile App Platform Audit

A worked example for a cross-platform mobile app (React Native/Expo, iOS + Android). The product is fictional; the platform checks are reusable.

## 1. Scope

- **Mode:** Audit + Repair
- **Screens:** Home, Search, Item detail, Checkout, Settings
- **Platforms:** iOS 17 (iPhone 15 simulator), Android 14 (Pixel 8 emulator)
- **States:** default, loading, empty, error, keyboard open, offline, dark mode, large text
- **Tools:** simulator screenshots, `uiautomator dump`, accessibility inspector, manual gestures

## 2. Capture

```bash
# iOS
xcrun simctl io booted screenshot ios-home.png

# Android
adb exec-out screencap -p > android-home.png
adb shell uiautomator dump /sdcard/window.xml
adb pull /sdcard/window.xml android-home.xml
```

```bash
python ../../scripts/pixel_precision_audit.py \
  --image ios-home.png \
  --out ios-home-annotated.png \
  --json ios-home.json
```

## 3. Findings

### [IOS-001] Checkout button collides with the home indicator

- **Category:** platform / mobile
- **Severity:** P0
- **Confidence:** High
- **Surface:** Checkout, default
- **Environment:** iPhone 15, iOS 17, dark, large text
- **Evidence:** Primary button frame `y=812..860`; safe-area bottom inset 34pt; button bottom is 12pt from the screen edge and overlaps the home-indicator region
- **Observed:** The bottom CTA sits inside the system gesture area.
- **Impact:** Taps can trigger the home gesture; the CTA is hard to hit.
- **Cause:** Fixed bottom padding; no `SafeAreaView`/`useSafeAreaInsets`.
- **Fix:** Apply bottom safe-area inset + 12pt spacing; keep the CTA above the indicator.
- **Verification:** `FIXED_AND_VERIFIED` — button bottom 46pt above the edge; tap test on device.

### [AND-001] Icon-only “filter” button is 32dp

- **Category:** accessibility / mobile
- **Severity:** P1
- **Confidence:** High
- **Surface:** Search, toolbar
- **Environment:** Pixel 8, Android 14
- **Evidence:** `uiautomator` bounds `[1040,96][1072,128]` = **32x32dp**; no `hitSlop`
- **Observed:** The filter target is below the 48dp recommendation and the 24dp WCAG floor is only just met.
- **Impact:** Mis-taps; difficult for motor-impaired users.
- **Cause:** 24dp icon used as the touch target.
- **Fix:** 48dp touch container with the 24dp icon centered; keep visual size.
- **Verification:** `FIXED_AND_VERIFIED` — 48x48dp; spacing to neighbor 12dp.

### [FORM-002] Keyboard covers the coupon field

- **Category:** forms / mobile
- **Severity:** P1
- **Confidence:** High
- **Surface:** Checkout, keyboard open
- **Environment:** iPhone 15, iOS 17
- **Evidence:** Active input at `y=690`; keyboard top at `y=520`; field fully hidden
- **Observed:** The user cannot see what they type.
- **Impact:** Coupon entry fails or requires blind typing.
- **Cause:** Scroll view does not adjust for keyboard; no `KeyboardAvoidingView`.
- **Fix:** `KeyboardAvoidingView`/`behavior="padding"` + scroll active field into view.
- **Verification:** `FIXED_AND_VERIFIED` — field visible 24pt above keyboard.

### [NAV-001] Android back closes the app from Item detail

- **Category:** navigation / platform
- **Severity:** P0
- **Confidence:** High
- **Surface:** Item detail → back
- **Environment:** Pixel 8, Android 14
- **Evidence:** Hardware/gesture back exits to the launcher instead of returning to Search; deep link entry has no back stack
- **Observed:** Back behavior violates Android convention.
- **Impact:** Users lose context and may think the app crashed.
- **Cause:** Custom navigation without a back handler/stack for deep links.
- **Fix:** Use native stack/back handler; synthesize a parent route for deep links.
- **Verification:** `FIXED_AND_VERIFIED` — back returns to Search; deep link back goes Home.

### [A11Y-003] Large text truncates the price

- **Category:** typography / accessibility
- **Severity:** P1
- **Confidence:** High
- **Surface:** Item detail, checkout summary
- **Environment:** iOS AX3 / Android 200% font scale
- **Evidence:** Price label `Rp 1.250.000` clipped at 200%; container fixed height 24
- **Observed:** The price becomes unreadable at large text sizes.
- **Impact:** Users who need larger text cannot confirm the price.
- **Cause:** Fixed-height label and `numberOfLines={1}`.
- **Fix:** Remove fixed height; allow wrapping or use `adjustsFontSizeToFit` with a minimum; test AX3.
- **Verification:** `FIXED_AND_VERIFIED` — full price visible at AX3/200%.

### [OFF-001] Offline state is a blank screen

- **Category:** state / mobile
- **Severity:** P2
- **Confidence:** High
- **Surface:** Home, offline
- **Environment:** iOS 17, airplane mode
- **Evidence:** Blank list with no message; retry only after app restart
- **Observed:** The app looks broken offline.
- **Impact:** Users do not know whether to wait or retry.
- **Cause:** No offline/error state; fetch failure swallowed.
- **Fix:** Show offline banner + cached content + retry; distinguish offline from server error.
- **Verification:** `FIXED_AND_VERIFIED` — banner + retry works; cached list visible.

## 4. Platform matrix

| Check | iOS | Android | Result |
|---|---|---|---|
| Safe areas | 34pt bottom | 24dp gesture inset | iOS failed; Android pass |
| Touch targets | 44pt | 48dp | Android filter failed |
| Keyboard avoidance | Required | Required | iOS failed |
| Back behavior | Swipe/back button | System back | Android failed |
| Large text | AX3 | 200% | Both failed |
| Offline state | Required | Required | Both failed |

## 5. Repair plan

1. `IOS-001` safe-area CTA (P0).
2. `NAV-001` Android back stack (P0).
3. `AND-001` touch target (P1).
4. `FORM-002` keyboard avoidance (P1).
5. `A11Y-003` large-text price (P1).
6. `OFF-001` offline state (P2).

## 6. Verification summary

| Finding | Before | After | Status |
|---|---|---|---|
| IOS-001 | CTA in gesture area | 46pt above edge | FIXED_AND_VERIFIED |
| AND-001 | 32x32dp | 48x48dp | FIXED_AND_VERIFIED |
| FORM-002 | field hidden | visible above keyboard | FIXED_AND_VERIFIED |
| NAV-001 | back exits app | returns to Search | FIXED_AND_VERIFIED |
| A11Y-003 | price clipped | full price at AX3 | FIXED_AND_VERIFIED |
| OFF-001 | blank screen | banner + retry + cache | FIXED_AND_VERIFIED |

## 7. What this example demonstrates

- Platform audits need real device/simulator evidence, not a desktop browser at 375px.
- Safe areas and keyboard avoidance are functional defects, not polish.
- Platform back behavior is part of navigation quality.
- Large-text testing is mandatory; fixed heights are a common failure.
- Offline is a state like any other; a blank screen is not a state.
