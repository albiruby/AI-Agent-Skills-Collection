---
name: uiux-mobile-app-auditor
description: "Audit native and hybrid mobile apps for platform conventions, touch behavior, safe areas, responsive screens, accessibility, navigation, and device conditions. Use when reviewing iOS/Android/Flutter/React Native UI, simulator or device evidence, or mobile-specific failures."
---

# Mobile Application UX Audit

## Use when

- The product is an iOS/Android/Flutter/React Native app or a mobile PWA.
- Safe areas, keyboard avoidance, touch targets, gestures, or navigation feel wrong.
- You need to verify phone/tablet layouts and device conditions.

## Do not use when

- The issue is desktop-only; use the desktop specialist.
- You only have a desktop browser screenshot and no mobile evidence; label the claim as limited.

## Mission

Inspect real mobile behavior, not a desktop page in a narrow window only.

## Procedure

1. Identify platform and app type: iOS, Android, cross-platform, responsive web/PWA, or hybrid. Record OS/device/simulator, app build, density, orientation, and system settings.
2. Inspect navigation conventions, status/navigation bars, safe areas, gestures, back behavior, tab bars, sheets, dialogs, keyboards, system permission prompts, and app lifecycle transitions.
3. Test touch target size/spacing, thumb reach, scroll behavior, swipe conflicts, long press, drag alternatives, orientation, one-handed use, and interrupted sessions.
4. Check dynamic text sizing, display scaling, high contrast, dark mode, reduced motion, screen readers, switch access, and platform accessibility semantics where supported.
5. Review offline/poor network, background/resume, push/deep links, permission denied/revoked, low storage, app update, and session timeout states when tools allow.
6. Evaluate native control conventions and platform-specific expectations. Avoid applying web-only assumptions to native controls or custom-drawing standard interactions without reason.
7. Capture screenshots and screen/view hierarchy for the affected device and state. Record whether an issue reproduces on physical hardware or only simulator.
8. Verify fixes on relevant OS versions and screen sizes; do not claim device coverage beyond the actual test matrix.

## Precision defaults

- iOS touch target >= 44pt; Android >= 48dp.
- Respect safe areas/notches/home indicator and keyboard avoidance.
- Bottom navigation <= 5 tabs; thumb-zone primary actions.
- Test dynamic type, dark mode, reduced motion, screen reader, and orientation.

## Quality gates

- [ ] Platform, build, device and orientation are recorded.
- [ ] Safe areas and system UI are respected.
- [ ] Touch, keyboard, and assistive access are tested where relevant.
- [ ] Permission, lifecycle, offline, and interruption behavior are considered.

## Evidence to capture

- Device/simulator, OS version, build, orientation, and DPR.
- Screenshots plus native view/accessibility hierarchy.
- Offline/permission/interruption states tested.

## Output

Return concise findings and decisions in the standard finding record format. For implementation work, include the exact files/components changed, the underlying cause, tests performed, and any residual limitations. If no defect is found, state the surfaces and states actually checked; do not imply broader coverage.

## Shared contract

Read `../../shared/UIUX_AUDIT_STANDARDS.md` before producing findings. Use its modes, evidence hierarchy, standard finding record, severity/priority model, and verification states. Do not duplicate findings that the shared contract already defines; cite the finding IDs and keep evidence local to this skill.

## Resources

- `../../references/platform-capture-matrix.md`
- `../../references/platform-ui-standards.md`
