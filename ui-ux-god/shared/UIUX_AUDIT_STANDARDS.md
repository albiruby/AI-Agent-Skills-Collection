# UI/UX Audit & Repair Standards

The canonical contract for every skill in this pack. Read this before producing findings, severity, repairs, or verification claims. Skills add domain procedure; this file defines the shared rules.

## 1. Purpose and scope

This pack audits and repairs the **rendered interface** of websites, web apps, dashboards, landing pages, component libraries, native mobile apps, desktop programs, wearables, TV/embedded displays, and CLI/TUI programs.

It covers visual craft, layout geometry, design systems, responsiveness, interaction states, accessibility, content/microcopy, navigation, flows, forms, performance, motion, platform conventions, root-cause engineering, repair, regression, and reporting.

It does **not** replace product research, legal/security review, backend correctness, or full accessibility certification. Those are separate evidence domains.

## 2. The evidence rule

Never perform a UI/UX audit by guessing from source code alone or by offering vague subjective praise. Every finding must be backed by at least one verifiable artifact:

1. **Rendered observation** — screenshot, screen recording, native frame, terminal capture.
2. **Measured structure** — DOM rectangle, computed style, accessibility tree, native view hierarchy, terminal cell grid.
3. **Reproducible test/log evidence** — console/network output, test run, visual diff, performance trace.
4. **Authoritative reference** — Figma/spec/design-system source that is current and in scope.
5. **Reasoned inference** — clearly labeled as inference, never presented as measured fact.

Evidence preference: direct runtime observation > measured structure/computed values > reproducible tests/logs > supplied references > inference.

If only a screenshot is available, label the audit **visual-only**. If source is absent, do not claim a code-level root cause. If a route, state, device, or test cannot be opened, record it as **not inspected** or **blocked**.

## 3. Modes and authorization

| Mode | What you may do | What you must not do |
|---|---|---|
| **Audit Only** | Inspect, measure, capture, report | Edit files, change app state beyond safe test interactions |
| **Audit + Repair** | Audit and implement high-confidence, low-risk, in-scope visible fixes | Redesign unrelated areas, deploy, change data/security policy |
| **Full Repair** | Execute the agreed repair backlog | Deploy/publish, delete data, change production records or access without explicit authorization |
| **Reference Match** | Compare against an authoritative reference and repair verified deviations | Treat an outdated/contradictory reference as truth |
| **Regression Check** | Validate changes against baselines and critical journeys | Update baselines merely to silence failures |

If the request says “audit and polish”, “audit and fix”, “rapihkan”, or equivalent, treat it as **Audit + Repair** for visible defects in the authorized scope. It is not permission for unrelated redesign or deployment.

## 4. Coverage ledger

Every audit keeps a ledger with one row per surface:

| Field | Example |
|---|---|
| Surface / route / screen | `/pricing`, `Settings > Billing`, `Checkout` |
| States checked | default, hover, focus, error, empty, loading |
| Viewports / devices | 375x812, 768x1024, 1440x900; iPhone 15, Windows 11 |
| Theme / locale / zoom | light, dark; en-US, id-ID; 100%, 200% |
| Tools / evidence | Playwright, accessibility tree, simulator |
| Result | inspected / partial / blocked / not in scope |
| Evidence path | `audit-out/pricing-375.png` |

Never claim full-site or full-app coverage without a route/screen inventory. Never infer an unvisited screen from a homepage screenshot.

## 5. Standard finding record

Use this record for every actionable finding. Keep the same fields in chat, Markdown, and JSON.

### Markdown record

```markdown
### [ID] Concise title

- **Category:** layout | typography | color | icon | imagery | motion | interaction | navigation | flow | form | content | accessibility | performance | platform | code | design-system
- **Severity:** Critical (P0) / High (P1) / Medium (P2) / Low (P3) / Informational
- **Confidence:** High / Medium / Low
- **Surface:** route/screen, user role, state
- **Environment:** viewport/device, OS/browser, DPR/scale, theme, locale, zoom
- **Evidence:** screenshot/crop path, selector or element ID, bounds, computed values, accessibility node, log/test output
- **Observed fact:** what is wrong, measured
- **User impact:** what the user cannot do, sees, or misunderstands
- **Frequency / scope:** always / intermittent / one component / global
- **Reproduction:** numbered steps
- **Suspected cause:** confirmed or hypothesis (label it)
- **Recommended fix:** the correct layer and the expected result
- **Verification:** status + before/after evidence
```

### JSON record

```json
{
  "id": "GEO-001",
  "title": "Header logo drifts 35.5px left of center",
  "category": "layout",
  "severity": "P1",
  "confidence": "High",
  "surface": { "route": "/", "screen": "Home", "state": "default" },
  "environment": { "viewport": "1440x900", "dpr": 1, "theme": "light", "locale": "en-US" },
  "target": {
    "selector": "header nav .brand-logo",
    "componentFile": "src/components/Navbar.tsx:42"
  },
  "evidence": {
    "elementCenterX": 684.5,
    "containerCenterX": 720.0,
    "deltaX_px": -35.5,
    "tolerance_px": 1.5,
    "screenshotBefore": "audit-out/home-1440-before.png"
  },
  "rootCause": "Navbar uses flex justify-between with asymmetric left (112px) and right (183px) slots.",
  "recommendedFix": "Use CSS Grid `grid-template-columns: 1fr auto 1fr`.",
  "verification": {
    "status": "FIXED_AND_VERIFIED",
    "deltaAfter_px": 0.0,
    "screenshotAfter": "audit-out/home-1440-after.png"
  }
}
```

Separate **observed fact**, **inferred cause**, and **proposed fix**. Never write a hypothesis as a confirmed cause.

## 6. Severity and priority

### Severity (impact)

| Level | Label | Examples | Action |
|---|---|---|---|
| **P0** | Critical / Broken | Core flow blocked, unreadable primary content, page-wide horizontal overflow on mobile, overlapping controls, broken images, severe contrast (<3.0:1 on primary text), data-loss risk | Fix before any polish |
| **P1** | High / Structural | Logo off-center >2px, incomplete/misaligned divider, broken grid, uneven sibling cards, body contrast <4.5:1, touch target <44px, major platform-convention breach | Primary remediation pass |
| **P2** | Medium / System | Off-grid spacing, concentric radius mismatch, rogue font sizes/colors, missing focus-visible ring, missing loading/empty/error state | Production-quality pass |
| **P3** | Low / Craft | 1–2px optical nudge, missing `tabular-nums`, orphan headline wrap, subtle shadow-direction variance | Polish pass |
| **Info** | Observation | Optional enhancement or design opportunity | Backlog / discuss |

### Priority (scheduling)

Priority is not severity. Consider:

```text
priority ≈ (impact × reach × confidence) / effort
```

Adjust for release timing, dependencies, brand risk, and blast radius. Record the rationale. A P1 on a high-traffic checkout may outrank a P0 on a hidden admin page; a risky token change may wait for a design decision.

### Decision values

`fix` / `defer` / `clarify` / `reject` — always with a reason and owner.

## 7. Precision thresholds

Use these defaults unless the product has a documented, stricter standard. Record the tolerance you used.

| Dimension | Default threshold | Notes |
|---|---|---|
| Horizontal centering | **1.5px** | <1.0px is usually subpixel/DPR noise |
| Divider asymmetry | **2px** | Decide full-bleed vs content-aligned first |
| Radius nesting | `R_inner = max(0, R_outer - padding)`, **2px** tolerance | Pinched corners are a common tell |
| Spacing rhythm | **4px** base; 8px macro rhythm | Flag 13/19/27px drift |
| Body contrast | **4.5:1** | Large text >=3.0:1 |
| UI component/graphic contrast | **3.0:1** | Borders, icons, focus indicators |
| Body text size | **>=16px** reading; >=14px dense UI | Mobile inputs >=16px to avoid iOS zoom |
| Line height | **>=1.35** body | Headings may be tighter |
| Measure | **45–75ch** | Flag >75ch |
| Font families | **<=3** | More needs a documented reason |
| Arbitrary font sizes | **<=8** | Without a modular scale |
| Touch target | **44x44px** iOS / **48x48dp** Android | WCAG 2.2 SC 2.5.8 floor is 24x24px |
| Focus ring | **>=2px**, >=3:1 | Must be visible on all backgrounds |
| Reflow | **320px / 400% zoom** | No 2D scroll except data tables |
| Text spacing | line-height >=1.5x, paragraph >=2x font size | Adjustable without clipping |
| Overflow | `scrollWidth > viewport + 1px` | Test 320px and 375px |
| Interactive overlap | **>3px** in both axes | Exclude intentional overlays |
| UI motion | **150–300ms** micro, 200–500ms larger | Honor reduced motion |
| Core Web Vitals | LCP **<=2.5s**, INP **<=200ms**, CLS **<=0.1** | 75th percentile |
| Feedback latency | **<=100ms** for direct manipulation | Longer needs a pending state |
| Main-thread long task | **<=50ms** during interaction | Trace-backed |
| HiDPI | **125/150/200%** | 1px hairlines and vector icons stay sharp |
| CLI/TUI widths | **80x24** floor, **120x40** standard | Divider width = panel inner width |

## 8. Verification states and gate

Every finding ends in one state:

- `OPEN` — detected with evidence, not yet patched.
- `FIXED_AND_VERIFIED` — patched, re-rendered, re-measured, within tolerance, no regression.
- `PARTIAL_NEEDS_DESIGN_DECISION` — technical fix requires a brand/product decision.
- `BLOCKED_EXTERNAL` — third-party iframe, external embed, or read-only asset.
- `NOT_FIXED` — attempted, still failing.
- `REGRESSION_INTRODUCED` — fix broke another surface.
- `UNABLE_TO_VERIFY` — no access to the required state/device/tool.

A code edit is **not** proof a visual bug is fixed. Re-render, re-measure, compare before/after under the same route, state, viewport, theme, DPR, locale, and data. Test at least one neighboring breakpoint and one adjacent shared component.

Cap a repair loop at **2 verification rounds** per cluster. If still blocked, record the blocker and options instead of looping.

## 9. Cross-harness capability matrix

Discover what the active harness actually exposes. Do not assume tools.

| Capability | Web | Native mobile | Desktop | CLI/TUI | If absent |
|---|---|---|---|---|---|
| Navigate/open | Browser automation | Simulator/device | App launch/window | Terminal run | Record as blocked |
| Capture | Screenshot/full page | `simctl`/`adb` screenshot | Window capture | Terminal capture | Visual-only claim |
| Structure | DOM, computed styles, a11y tree | View/accessibility hierarchy | UI automation tree | Cell grid | No code-level claim |
| Interact | Hover/focus/type/resize | Tap/swipe/type/rotate | Click/type/resize/DPI | Keys/ANSI | No interaction claim |
| Code access | Repository/file tools | Source/build tools | Source/build tools | Repository | Handoff instead of fix |
| Verify | Re-render + diff | Same device/state | Same window/DPI | Same width/theme | `UNABLE_TO_VERIFY` |

A skill defines procedure and judgment. It does not grant browser, device, filesystem, credential, or application access.

## 10. Anti-patterns

- Auditing from source code alone and claiming visual correctness.
- Treating a screenshot as proof of semantics, keyboard behavior, or DOM structure.
- Inventing pixel measurements, contrast ratios, or accessibility results.
- Fixing a symptom with `!important`, magic margins, or `transform` while the parent layout stays broken.
- Applying blind optical nudges without checking SVG viewBox/transparent padding.
- Hiding overflow with `overflow-x: hidden` on `body` (breaks sticky positioning).
- Judging responsive behavior only by resizing a desktop window.
- Calling an automated accessibility scan “WCAG conformance”.
- Treating a visual diff score as the sole definition of design quality.
- Updating visual baselines to silence a failing test.
- Erasing intentional asymmetry, brand character, or platform conventions.
- Claiming “fixed” after editing code without re-rendering.

## 11. Output contract

Every audit output includes, at minimum:

1. **Scope and mode** — what was audited, what authorization applied.
2. **Environment** — build/commit, routes/screens, viewports/devices, themes/locales.
3. **Coverage** — inspected, partial, blocked, not in scope.
4. **Findings** — standard record, sorted by severity/priority.
5. **Repairs** — files/components/screens changed, rationale, blast radius.
6. **Verification** — before/after evidence and status per finding.
7. **Limitations** — what could not be tested or claimed.
8. **Next actions** — decisions needed, deferred items, follow-up tests.

Keep the executive summary short. Put evidence in the finding, not in vague prose.

## 12. Safety and limitations

- Never deploy, publish, delete user data, change production records, or alter access/security policy without explicit authorization.
- Preserve content meaning, business logic, keyboard access, focus, contrast, motion preferences, and user data.
- Do not expose secrets, personal data, or internal URLs in screenshots or reports.
- When blocked, deliver the most useful evidence-backed partial result and a precise list of missing access.
- This pack provides audit findings and engineering guidance, not legal, security, or accessibility certification.

## 13. Quick routing

| Request | Start with |
|---|---|
| Full audit / repair program | `ui-ux-god` |
| “Where do I start?” / map the app | `uiux-live-interface-inspector` |
| Logo off-center, divider short, 1px drift | `uiux-layout-geometry-auditor`, `uiux-microdetail-polish-specialist` |
| Inconsistent colors, spacing, radii, tokens | `uiux-visual-design-system-auditor` |
| Mobile overflow, breakpoints, zoom | `uiux-responsive-layout-auditor` |
| Hover/focus/disabled/loading states | `uiux-responsive-interaction-auditor` |
| WCAG / screen reader / keyboard | `uiux-wcag-accessibility-auditor`, `uiux-keyboard-assistive-tech-auditor` |
| Slow or janky UI | `uiux-performance-perceived-speed-auditor` |
| “Fix it properly” | `uiux-surgical-repair-engineer` |
| “Prove it is fixed” | `uiux-post-repair-verification-engineer` |
| Write the report | `uiux-audit-evidence-report-writer` |
| “What should we fix first?” | `uiux-audit-governance-risk-triage` |
