---
name: uiux-desktop-app-auditor
description: "Audit native desktop applications across Windows, macOS, and Linux for layout, window behavior, keyboard conventions, HiDPI scaling, accessibility, and interaction quality. Use when reviewing Electron/Tauri/Qt/WPF/WinUI/AppKit apps or desktop-specific window and DPI issues."
---

# Desktop Application UX Audit

## Use when

- The product is a desktop app or a web wrapper such as Electron/Tauri.
- Window resizing, titlebar collisions, HiDPI scaling, or native shortcuts are suspect.
- You need to verify desktop accessibility and platform conventions.

## Do not use when

- The issue is a mobile app; use the mobile specialist.
- You only have a browser page and no desktop window evidence.

## Mission

Assess the actual application window and operating-system context.

## Procedure

1. Identify OS, application version, window manager, display scale, monitor configuration, and whether the app is native, Electron, webview, or another runtime.
2. Inspect resizing, minimum window size, maximize/restore, fullscreen, multi-window, dialogs, menus, context menus, title bars, system trays, and window focus behavior.
3. Check keyboard shortcuts, menu discoverability, focus traversal, command consistency, accelerators, undo/redo, clipboard, drag/drop, and platform-specific navigation expectations.
4. Inspect high-DPI behavior, fractional scaling, multi-monitor movement, font rendering, clipping, native controls, scrollbars, and system theme integration.
5. Test accessibility tree and native accessibility APIs where exposed. Verify names, roles, values, states, focus, and logical reading order.
6. Check file dialogs, save/open flows, unsaved-change handling, destructive confirmation, long-running tasks, cancellation, progress, and recovery after crash/restart where relevant.
7. For cross-platform apps, compare the same task on each supported OS and distinguish intended platform variation from inconsistent behavior.
8. Record exact OS/build/display scale and reproduce defects after a fix. Do not overgeneralize from one machine.

## Precision defaults

- Test default, minimum, and maximized window sizes.
- Check 100%, 125%, 150%, and 200% display scaling.
- Titlebar/traffic lights must not collide with custom headers.
- Cmd/Ctrl parity and native dialog button order per platform.

## Quality gates

- [ ] Window and display-scaling behavior is tested.
- [ ] Keyboard and native accessibility conventions are included.
- [ ] File/task interruption and recovery are assessed where relevant.
- [ ] OS-specific claims have a recorded test environment.

## Evidence to capture

- Window sizes, display scale, OS, and build.
- Native UI/accessibility hierarchy and screenshots.
- Keyboard shortcut parity and window-resize behavior.

## Output

Return concise findings and decisions in the standard finding record format. For implementation work, include the exact files/components changed, the underlying cause, tests performed, and any residual limitations. If no defect is found, state the surfaces and states actually checked; do not imply broader coverage.

## Shared contract

Read `../../shared/UIUX_AUDIT_STANDARDS.md` before producing findings. Use its modes, evidence hierarchy, standard finding record, severity/priority model, and verification states. Do not duplicate findings that the shared contract already defines; cite the finding IDs and keep evidence local to this skill.

## Resources

- `../../references/platform-capture-matrix.md`
- `../../references/platform-ui-standards.md`
