---
name: uiux-live-interface-inspector
description: "Map and capture real rendered interfaces before judging them. Use when starting a UI/UX audit, when routes/screens/states/viewports are unknown, or when you need a coverage inventory, baseline screenshots, DOM/accessibility evidence, and an honest list of what could not be inspected."
---

# Live Interface Reconnaissance

## Use when

- You are starting an audit and need to map routes, screens, dialogs, states, and viewports before judging anything.
- You need a baseline evidence set: screenshots, DOM/computed styles, accessibility tree, or native view hierarchy.
- You must record what was inspected, what was blocked, and what was not in scope.

## Do not use when

- You already have a complete, current evidence set and only need a focused specialist check.
- The task is purely source-code analysis with no rendered interface to inspect.

## Mission

Establish what is actually running before making design claims.

## Procedure

1. Identify the application surface: public website, authenticated web app, embedded webview, desktop application, mobile application, kiosk, or other UI. Identify the available inspection path: browser automation, DOM/devtools, accessibility tree, native accessibility APIs, simulator/device automation, desktop UI automation, screenshots, or a combination.
2. Build a coverage inventory: routes/screens, navigation entry points, dialogs, drawers, tabs, menus, forms, tables, empty states, loading states, errors, permissions, and responsive variants. Record inaccessible areas rather than silently excluding them.
3. Capture a baseline at realistic conditions. For web, use full-page and viewport screenshots plus structural snapshots where available. For native apps, capture screen hierarchy/accessibility metadata and representative screenshots. Preserve viewport, device scale factor, theme, locale, zoom, and app version.
4. Inspect both rendered appearance and underlying structure. For web, inspect DOM, bounding boxes, computed styles, font loading, layout ancestors, accessibility tree, console, and network failures when tools permit. For native UI, inspect view hierarchy, constraints/layout bounds, semantic labels, focus order, and system settings where supported.
5. Interact deliberately: hover, focus, keyboard, tap, long press, scroll, resize, open/close overlays, submit valid/invalid forms, navigate back, and test disabled/loading states. Reset state between scenarios when it affects results.
6. Create an evidence index with screen/route, state, viewport/device, screenshot or snapshot reference, element identifier, observed behavior, and any measurement. Never infer an unvisited screen from a homepage screenshot.
7. Before reporting coverage, state what was inspected, what was not accessible, which tools were available, and whether findings are visual-only, code-backed, or interaction-tested.

## Precision defaults

- Capture at minimum 375px mobile, 768px tablet, and 1440px desktop; add 320px and 1920px for flagship audits.
- Record build/commit, route, viewport, DPR, OS/browser, theme, locale, zoom, and state for every baseline.
- Use full-page and viewport screenshots; keep element bounds and accessibility snapshots where available.
- Never infer an unvisited screen from a homepage screenshot.

## Quality gates

- [ ] Every finding is tied to a route/screen, state, viewport, and inspectable evidence.
- [ ] A screenshot is not treated as a substitute for DOM/accessibility inspection when those are available.
- [ ] No claim of full-site or full-app coverage without a route/screen inventory.
- [ ] Dynamic or personalized content is recorded as variable rather than mistaken for a defect.

## Evidence to capture

- Route/screen inventory and coverage ledger.
- Baseline screenshot paths and structural snapshot references.
- Console/network failures, font-loading state, and blocked areas.

## Output

Return concise findings and decisions in the standard finding record format. For implementation work, include the exact files/components changed, the underlying cause, tests performed, and any residual limitations. If no defect is found, state the surfaces and states actually checked; do not imply broader coverage.

## Shared contract

Read `../../shared/UIUX_AUDIT_STANDARDS.md` before producing findings. Use its modes, evidence hierarchy, standard finding record, severity/priority model, and verification states. Do not duplicate findings that the shared contract already defines; cite the finding IDs and keep evidence local to this skill.

## Resources

- `../../references/platform-capture-matrix.md`
- `../../references/evidence-schema.md`
- `../../templates/coverage-ledger.md`
