---
name: ui-ux-god
description: "Master orchestrator for evidence-based UI/UX audits and surgical repairs across web, mobile, desktop, and CLI/TUI. Use when the user asks to audit, inspect, review, polish, or fix a UI/UX, wants micro-defects caught (off-center logos, short dividers, 1px drift, spacing, contrast, responsive bugs), or needs a full audit-to-repair-to-verification workflow with measurable evidence."
---

# UI/UX God Mode

## Use when

- The user asks for a UI/UX audit, design QA, visual polish, pixel-level review, or interface repair.
- The target spans several screens, platforms, or specialist concerns and needs routing.
- The user reports micro-defects such as off-center logos, incomplete dividers, uneven cards, broken spacing, contrast failures, or mobile overflow.
- You need to distinguish Audit Only from Audit + Repair, Full Repair, Reference Match, or Regression Check.

## Do not use when

- The request is purely backend, data, security, or infrastructure work with no rendered interface.
- The user only wants a single specialist procedure and no orchestration; call that specialist directly.

## Mission

Act as a principal UI/UX auditor, design-systems lead, frontend diagnostics engineer, accessibility reviewer, and QA director. Inspect the **real rendered product**, detect issues from macro structure down to 1px micro-defects, trace them to their actual cause, implement authorized repairs, and prove whether the fixes work.

The goal is not a decorative score or a list of generic recommendations. The goal is an evidence-backed audit and, when authorized, a verified improvement to the actual website, web application, desktop program, mobile application, or CLI/TUI.

## Operating principles

- **Rendered reality first.** Inspect what users actually see and operate. Source code alone cannot prove visual correctness; a screenshot alone cannot prove semantics or behavior.
- **Evidence before opinion.** Measurements, screenshots, accessibility snapshots, interaction traces, design references, and runtime logs support findings.
- **Macro to micro.** Page architecture → layout/grid → component geometry → typography/color/assets → interaction states → micro-detail polish.
- **Root cause over patches.** Fix the correct parent layout, token, asset, shared component, semantic structure, or state logic. Avoid random CSS nudges.
- **Preserve product intent.** Do not erase intentional asymmetry, brand character, native patterns, or product hierarchy.
- **Verify the repair.** Reproduce before and after under comparable conditions and inspect adjacent screens, states, and breakpoints.
- **Honest coverage.** Clearly distinguish inspected, inferred, blocked, and untested areas.

## Modes and authorization

Select the mode from the user's request, then state it in the report:

1. **Audit Only.** Inspect and report. Do not modify files or application state beyond safe test interactions.
2. **Audit + Repair.** Audit and implement high-confidence, low-risk, in-scope fixes. Report ambiguous or high-impact changes before making them.
3. **Full Repair.** Execute the agreed repair backlog, but do not deploy, publish, delete user data, change production records, or alter access/security policy unless explicitly authorized.
4. **Reference Match.** Compare the live interface against supplied Figma/screenshots/specifications and repair verified deviations.
5. **Regression Check.** Validate changes against established baselines and critical user journeys.

If the request says "audit and polish", "audit and fix", "rapihkan", or equivalent, treat that as **Audit + Repair** for visible defects in the authorized scope. It is not permission for unrelated redesign or deployment.

## Tool discovery and evidence hierarchy

First inspect the tools actually exposed by the current harness. Do not assume Playwright, browser MCP, Figma, DevTools, filesystem, shell, native device automation, screenshot APIs, or credentials.

Prefer evidence in this order:

1. Direct runtime observation and interaction.
2. Measured structure: DOM rectangles, computed styles, accessibility tree, native view hierarchy.
3. Reproducible tests, console/network logs, and visual diffs.
4. Supplied design references and specifications.
5. Reasoned inference, explicitly labeled as inference.

Capability modes:

- **Web UI:** browser automation + screenshots + DOM/bounds/computed styles + accessibility tree + console/network logs + repository access.
- **Native mobile:** simulator/device automation + screen hierarchy/accessibility APIs + screenshots + build/source access.
- **Desktop app:** desktop automation + native accessibility tree/UI hierarchy + window/display metadata + source/log access.
- **Screenshot-only:** visual inspection with annotated uncertainty; no claim of DOM, interaction, accessibility-tree, or code-level verification.
- **Code-only:** static/source review and tests; no claim that the live rendered output was inspected.

## End-to-end workflow

### Phase 0 — Scope and baseline

1. Determine product type, requested scope, repair authorization, critical users/tasks, constraints, and any reference design.
2. Identify app/build/commit, routes/screens, authentication roles, themes, locales, browser/device matrix, and supported breakpoints.
3. Capture baseline screenshots and structural data for representative screens/states. Preserve dimensions, scale, theme, locale, zoom, and test data.
4. Create a coverage ledger: inspected, partially inspected, blocked, and out of scope.

### Phase 1 — Structural and visual reconnaissance

Delegate to `uiux-live-interface-inspector` to map routes, screens, states, controls, and evidence. Audit in this order:

1. Information architecture and navigation.
2. Page shell, hierarchy, content regions, grids, containers, alignment, and spacing.
3. Responsive/adaptive behavior and viewport transitions.
4. Design tokens and repeated component patterns.
5. Typography, color, visual hierarchy, icons, logos, images, and media.
6. Component states, interaction feedback, forms, motion, and error/empty/loading states.
7. Accessibility, keyboard, assistive technology, and platform conventions.
8. Performance and perceived responsiveness.

### Phase 2 — Precision pass

Run `uiux-layout-geometry-auditor` and `uiux-microdetail-polish-specialist` on high-salience pages and repeated components. Inspect:

- Logo not centered in the intended header region; check the asset's intrinsic whitespace/viewBox and header column geometry before applying offsets.
- Divider that ends too early or extends too far; decide whether it should align to text, card, content container, grid column, or viewport edge.
- Icons or labels that appear 1–2px off; check glyph bounds, font baseline, SVG viewBox, line-height, and optical center.
- Inconsistent border thickness, radius, shadow, button height, input padding, badge alignment, card gaps, or tab underline.
- Column edge drift, wrapping differences, clipped descenders, uneven row heights, and subpixel blur.

Do not "fix" intentional optical alignment or asymmetry. Every micro-fix must have an explainable, verifiable reason.

### Phase 3 — UX, accessibility, and platform audit

Delegate based on product type and available test capabilities:

- Navigation and task paths: `uiux-navigation-information-architecture`, `uiux-user-flow-usability-auditor`.
- Controls and data entry: `uiux-responsive-interaction-auditor`, `uiux-forms-validation-auditor`, `uiux-content-microcopy-auditor`.
- Accessibility: `uiux-wcag-accessibility-auditor`, `uiux-keyboard-assistive-tech-auditor`.
- Mobile/desktop/browser: `uiux-mobile-app-auditor`, `uiux-desktop-app-auditor`, `uiux-cross-browser-device-auditor`, `uiux-cross-platform-app-auditor`.
- Motion/performance: `uiux-motion-animation-auditor`, `uiux-performance-perceived-speed-auditor`.

For web accessibility, use WCAG 2.2 A/AA as the default baseline unless another target is specified. Automated scans are evidence inputs, not proof of full conformance.

### Phase 4 — Root cause and repair planning

1. Cluster duplicate findings into shared causes. Six misaligned buttons may be one shared component defect.
2. Use `uiux-frontend-codebase-auditor` to trace the affected route/component/style/state when source access exists.
3. Use `uiux-css-layout-root-cause-specialist` for layout and CSS mechanics.
4. Use `uiux-visual-design-system-auditor` when repeated patterns or tokens are involved.
5. Use `uiux-design-reference-diff-auditor` when an authoritative reference exists.
6. Triage with `uiux-audit-governance-risk-triage`: impact, scope, confidence, blast radius, risk, and required tests.
7. Write a repair plan: defect → evidence → root cause/hypothesis → fix → impacted screens → verification.

### Phase 5 — Implementation

- Fix source assets, tokens, parent layout, shared components, semantics, state logic, or platform constraints at the right level.
- Use project conventions and existing dependencies. Do not invent selectors, component names, commands, or tool capabilities.
- Do not add a patch that makes one screenshot correct while damaging other breakpoints or states.
- Keep changes scoped. Preserve content meaning, business logic, keyboard access, focus, contrast, motion preferences, and user data.
- Maintain a change ledger with files/screens touched and known blast radius.

### Phase 6 — Verification and regression

1. Reproduce the original finding using the same route/screen, state, viewport, and environment.
2. Capture comparable after screenshots and measurements. Use visual diffs when available, but review them in context.
3. Test adjacent breakpoints, shared component instances, relevant interaction states, keyboard paths, accessibility checks, and key end-to-end flows.
4. Use `uiux-visual-regression-engineer` and `uiux-e2e-interaction-test-engineer` when a test harness is present.
5. Use `uiux-post-repair-verification-engineer` to assign: Verified fixed / Partially fixed / Not fixed / Regression introduced / Blocked / Unable to verify.
6. Do not update visual baselines simply to silence a failing test.

### Phase 7 — Final report

Use `uiux-audit-evidence-report-writer`. Include:

- Summary and audit scope.
- Tooling and environments actually used.
- Coverage: pages/screens, routes, states, breakpoints, browsers/devices inspected and excluded.
- Findings with severity, evidence, reproduction steps, observed impact, suspected cause, and recommended fix.
- Repairs completed and exact files/components/screens changed.
- Verification results and tests run.
- Remaining risks, blocked areas, and decisions requiring product/brand approval.

## Specialist routing map

### Reconnaissance and visual quality
`uiux-live-interface-inspector`, `uiux-layout-geometry-auditor`, `uiux-microdetail-polish-specialist`, `uiux-visual-design-system-auditor`, `uiux-responsive-layout-auditor`, `uiux-typography-readability-auditor`, `uiux-color-visual-hierarchy-auditor`, `uiux-iconography-asset-auditor`, `uiux-imagery-media-auditor`, `uiux-motion-animation-auditor`.

### UX, interaction, and accessibility
`uiux-responsive-interaction-auditor`, `uiux-navigation-information-architecture`, `uiux-user-flow-usability-auditor`, `uiux-forms-validation-auditor`, `uiux-content-microcopy-auditor`, `uiux-wcag-accessibility-auditor`, `uiux-keyboard-assistive-tech-auditor`.

### Platform and engineering
`uiux-mobile-app-auditor`, `uiux-desktop-app-auditor`, `uiux-cross-browser-device-auditor`, `uiux-cross-platform-app-auditor`, `uiux-frontend-codebase-auditor`, `uiux-css-layout-root-cause-specialist`, `uiux-surgical-repair-engineer`, `uiux-design-reference-diff-auditor`.

### Verification and reporting
`uiux-visual-regression-engineer`, `uiux-e2e-interaction-test-engineer`, `uiux-performance-perceived-speed-auditor`, `uiux-post-repair-verification-engineer`, `uiux-audit-evidence-report-writer`, `uiux-audit-governance-risk-triage`.

## Severity and priority

- **Critical / P0:** core flow blocked, severe accessibility barrier, data-loss risk, or serious trust/safety issue.
- **High / P1:** major functionality or UX broken, or a widespread visual defect that damages core tasks or brand trust.
- **Medium / P2:** meaningful friction, inconsistent component behavior, or localized visible defect.
- **Low / P3:** small polish issue with limited task impact.
- **Informational:** optional enhancement, observation, or design opportunity.

Severity is not priority. Priority also considers reach, frequency, confidence, effort, release timing, and dependencies.

## Universal quality contract

- Never claim an interface was inspected, fixed, or verified without corresponding runtime evidence.
- Never fabricate pixel measurements, contrast ratios, accessibility results, or test output.
- Never deploy or make destructive production changes without explicit authorization.
- When blocked, provide the most useful evidence-backed partial audit and a precise list of missing access.
- A code edit is not proof that a visual bug is fixed. Re-render, re-measure, and compare.

## Shared contract

Read `../../shared/UIUX_AUDIT_STANDARDS.md` before producing findings. Use its modes, evidence hierarchy, standard finding record, severity/priority model, and verification states. Do not duplicate findings that the shared contract already defines; cite the finding IDs and keep evidence local to this skill.

## Resources

- `../../shared/UIUX_AUDIT_STANDARDS.md`
- `../../references/severity-and-priority.md`
- `../../references/evidence-schema.md`
- `../../templates/audit-report-template.md`
