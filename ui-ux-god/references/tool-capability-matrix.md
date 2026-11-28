# Tool Capability & Evidence Matrix

A skill defines procedure and judgment; it does not grant access. Discover what the active harness actually exposes before promising an audit, a repair, or a verification.

## 1. Capability discovery

Check for:

- Browser automation (navigate, click, type, hover, resize, screenshot, DOM, computed styles, accessibility tree, console/network).
- Native mobile automation (simulator/device, tap/swipe/type, screen hierarchy, accessibility APIs).
- Desktop automation (launch/window, UI automation tree, screenshot, DPI/scale metadata).
- CLI/TUI capture (terminal run, ANSI-to-image, fixed columns).
- Repository/file access (read, edit, search, diff).
- Test/CLI runners (unit, E2E, visual, lint, typecheck).
- Design references (Figma/screenshots/specs) and credentials.

If a capability is missing, record it as a limitation. Do not invent it.

## 2. Claim ladder

Use the strongest claim the evidence supports:

| Evidence available | You may claim |
|---|---|
| Live browser + DOM + computed + a11y + interaction | Visual, structural, semantic, and interaction findings for the inspected states |
| Live browser + screenshots only | Visual findings only; no DOM/semantics/interaction claims |
| Screenshots supplied, no runtime | Visual review with annotated uncertainty; no code-level or behavioral claims |
| Source code only | Static/code findings; no claim that the rendered output was inspected |
| Native simulator + hierarchy | Native visual/structural findings for the tested device/OS |
| No access | A plan and a precise list of missing access; do not claim an audit |

## 3. Capability matrix

| Capability | Web | Native mobile | Desktop | CLI/TUI | If absent |
|---|---|---|---|---|---|
| Open/navigate | Browser | Simulator/device | App/window | Terminal | Blocked |
| Capture | Screenshot/full page | `simctl`/`adb` capture | Window capture | Terminal capture | Visual-only |
| Structure | DOM/computed/a11y tree | View/a11y hierarchy | UI automation tree | Cell grid | No structural claim |
| Interact | Hover/focus/type/resize | Tap/swipe/type/rotate | Click/type/resize/DPI | Keys/ANSI | No interaction claim |
| Code access | Repo tools | Source/build | Source/build | Repo | Handoff, not fix |
| Verify | Re-render + diff | Same device/state | Same window/DPI | Same width/theme | `UNABLE_TO_VERIFY` |
| Auth | Storage state/login | App login/biometrics | OS session | Shell env | Blocked surfaces |

## 4. Tool mapping

| Need | Preferred | Acceptable fallback |
|---|---|---|
| Rendered screenshot | Playwright/browser MCP | Manual screenshot with recorded conditions |
| Geometry | DOM `getBoundingClientRect` + computed styles | Pixel measurement with known DPR |
| Accessibility | Accessibility tree + keyboard/AT | Manual checklist; label as limited |
| Native structure | Platform accessibility/UI tree | Screenshot-only visual review |
| Code root cause | Repo search + file:line | Precise handoff with component guess labeled |
| Visual diff | Playwright `toHaveScreenshot` / pixel diff | Side-by-side manual review |
| Performance | Lighthouse/trace/RUM | Lab estimate labeled as estimate |

## 5. Evidence integrity

- Preserve the tool’s actual output; do not paraphrase a measurement into a different number.
- Keep screenshot paths/IDs returned by the tool.
- Record environment: build/commit, route, viewport, DPR, OS/browser, theme, locale, zoom, state.
- Do not expose secrets, tokens, personal data, or internal URLs in evidence.
- Redact sensitive content before sharing screenshots.

## 6. When blocked

Deliver:

1. What was inspected and with which tools.
2. What could not be inspected and why (no access, no device, no credentials, no source).
3. The strongest evidence-backed partial findings.
4. A precise list of access/tools needed to complete the audit.
5. What you will **not** claim until that access exists.

A partial audit with honest limits is more valuable than a fabricated complete one.
