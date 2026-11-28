---
name: uiux-cross-platform-app-auditor
description: "Audit non-web UI beyond standard browsers: cross-platform frameworks, wearables, TV, embedded displays, and CLI/TUI programs. Use when checking Flutter/React Native platform quirks, safe areas, HiDPI, window constraints, terminal box-drawing, or platform-native ergonomics."
---

# Cross-Platform, Wearable, TV & CLI/TUI Audit

## Use when

- The target is Flutter, React Native, a wearable, TV, embedded display, or a CLI/TUI program.
- You need platform capture commands, safe-area/HiDPI checks, or terminal layout verification.
- A cross-platform app looks native on one platform but wrong on another.

## Do not use when

- The target is a standard web page; use the web specialists.
- You need deep iOS/Android or desktop coverage; use the mobile or desktop specialist and use this for cross-cutting platform checks.

## Mission

Extend evidence-based UI/UX auditing beyond standard browsers to cross-platform frameworks, wearables, TV, embedded displays, and terminal interfaces. Respect platform conventions instead of forcing one visual language everywhere.

## Procedure

1. Identify the target family: Flutter, React Native/Expo, native iOS/Android, Electron/Tauri, Qt/WPF/WinUI/GTK/AppKit, wearable, TV, embedded, or CLI/TUI.
2. Capture real frames using the platform capture matrix:
   - Mobile: `xcrun simctl io booted screenshot` or `adb exec-out screencap -p`; dump the view hierarchy (`uiautomator dump`, Flutter `debugDumpRenderTree()`).
   - Desktop: capture default, minimum, and maximized window sizes at 100% and 150%/200% scaling.
   - CLI/TUI: capture at `80x24` and `120x40`; preserve exact column widths and ANSI state.
3. Run the pixel inspector on captured PNGs for centering, margin symmetry, and divider completeness:

```bash
python ../../scripts/pixel_precision_audit.py --image ./capture.png --out ./annotated.png --json ./pixel-report.json
```

4. Mobile safe areas: no content under the status bar, notch/Dynamic Island, rounded corners, or home indicator. Keyboard avoidance must keep the active field visible.
5. Mobile ergonomics: bottom navigation <= 5 tabs, primary actions in the thumb zone, touch targets >= 44pt iOS / >= 48dp Android.
6. Desktop windows: explicit minimum size; titlebar/traffic lights never collide with custom headers; hairlines and vector icons stay sharp at 125/150/200% DPI; Cmd/Ctrl parity and native dialog order.
7. CLI/TUI: box-drawing borders align with no jagged right edge; divider rules span `width - 2`; no wrapping; ANSI colors remain legible in dark and light terminals; wide Unicode/emoji are width-checked.
8. Wearable/TV/embedded: verify glanceable hierarchy, focus/remote navigation, overscan-safe margins, large targets, and limited-color/contrast constraints.
9. Stress long localized strings (+30%) and platform text scaling; verify truncation, wrapping, and layout reflow.
10. Record findings with platform-native units (`pt`, `dp`, `px`, columns) and the exact platform API/constraint fix.

## Precision defaults

- iOS target **44pt**; Android **48dp**; TV focus targets visibly large; wearable actions few and glanceable.
- Safe-area insets: zero collisions with system UI.
- HiDPI: 125/150/200% scaling; 1px hairlines and vector icons remain sharp.
- CLI/TUI: `80x24` floor and `120x40` standard; divider width = panel inner width; no ANSI bleed.
- Long strings: +30% expansion without clipping or overlap.
- Native conventions: back behavior, typography defaults, modal patterns, and button order per platform.

## Quality gates

- [ ] Platform, build, device/window, orientation, and scale are recorded.
- [ ] System UI/safe areas are respected.
- [ ] Platform conventions are followed unless a documented brand system intentionally overrides them.
- [ ] The claim matches the evidence: simulator vs physical device, visual-only vs hierarchy-backed.

## Evidence to capture

- Captured frame and view/accessibility hierarchy.
- Platform coordinates and the offending widget/constraint.
- Before/after screenshots at the affected device/window/terminal size.

## Output

Return platform-native findings with exact units, the fix at the correct platform layer, and a clear statement of which devices/windows/terminal sizes were actually tested.

## Shared contract

Read `../../shared/UIUX_AUDIT_STANDARDS.md` before producing findings. Use its modes, evidence hierarchy, standard finding record, severity/priority model, and verification states. Do not duplicate findings that the shared contract already defines; cite the finding IDs and keep evidence local to this skill.

## Resources

- `../../references/platform-capture-matrix.md`
- `../../references/platform-ui-standards.md`
- `../../scripts/pixel_precision_audit.py`
