# Skill Index — ui-ux-god

**32 skills: 1 master + 31 specialists.**

## Master

- `ui-ux-god` — Master orchestrator for evidence-based UI/UX audits and surgical repairs across web, mobile, desktop, and CLI/TUI. Use when the user asks to audit, inspect, review, polish, or fix a UI/UX, wants micro-defects caught (off-center logos, short dividers, 1px drift, spacing, contrast, responsive bugs), or needs a full audit-to-repair-to-verification workflow with measurable evidence.

## Reconnaissance & visual quality

- `uiux-live-interface-inspector` — Map and capture real rendered interfaces before judging them. Use when starting a UI/UX audit, when routes/screens/states/viewports are unknown, or when you need a coverage inventory, baseline screenshots, DOM/accessibility evidence, and an honest list of what could not be inspected.
- `uiux-layout-geometry-auditor` — Measure rendered layout geometry, grid alignment, centering, dividers, spacing, overflow, clipping, and sibling symmetry. Use when auditing page structure, catching off-center logos or headers, incomplete divider lines, uneven cards, broken grids, horizontal scroll, or verifying layout fixes with DOM and pixel measurements.
- `uiux-microdetail-polish-specialist` — Detect and polish high-salience micro-defects: optical centering, 1px misalignment, divider length, border and radius joins, icon offsets, baseline drift, and pixel-level spacing. Use when the macro layout is stable and the interface needs flagship-grade finish, or when the user reports small visual imperfections.
- `uiux-visual-design-system-auditor` — Audit visual craft and design-system mathematics: typography hierarchy, contrast, 4/8px rhythm, concentric radii, elevation, icon consistency, and token drift. Use when evaluating visual polish, color harmony, readability, spacing discipline, or when repeated components drift from the system.
- `uiux-responsive-layout-auditor` — Audit responsive and adaptive layouts across viewports, orientation, zoom, text scaling, and input modes. Use when checking breakpoint failures, mobile overflow, cramped tablets, ultra-wide containment, or when a layout works on desktop but breaks on smaller screens.
- `uiux-typography-readability-auditor` — Audit type choice, scale, hierarchy, line length, wrapping, line height, weights, and readability across languages and screens. Use when text feels cramped, inconsistent, or hard to read, or when verifying typography before launch.
- `uiux-color-visual-hierarchy-auditor` — Audit palette, contrast, semantic color, visual hierarchy, states, and theme behavior without flattening brand expression. Use when colors compete, CTAs lack prominence, dark mode looks harsh, or contrast and semantic states need verification.
- `uiux-iconography-asset-auditor` — Audit icons, logos, illustrations, SVGs, and interface assets for alignment, legibility, consistency, sizing, and semantic clarity. Use when icons look mismatched, logos sit off-center, SVG padding distorts alignment, or asset fidelity is suspect.
- `uiux-imagery-media-auditor` — Audit images, video, avatars, thumbnails, and media treatments for crop, focal point, resolution, loading, and visual consistency. Use when photos are stretched, crops cut faces, media feels inconsistent, or image performance and fallbacks need review.
- `uiux-motion-animation-auditor` — Audit transitions, animations, feedback motion, timing, easing, loading indicators, and reduced-motion behavior. Use when motion feels janky, distracting, too slow, or when verifying accessibility and performance of animations.

## UX, interaction & accessibility

- `uiux-responsive-interaction-auditor` — Audit responsive behavior, interactive states, touch targets, focus visibility, and practical accessibility on rendered interfaces. Use when checking the 9 mandatory UI states, mobile ergonomics, keyboard focus, hover/pressed/disabled feedback, or responsive interaction bugs.
- `uiux-navigation-information-architecture` — Audit navigation structure, labels, hierarchy, wayfinding, breadcrumbs, search, and information scent. Use when users get lost, menus feel flat, labels are ambiguous, or navigation needs restructuring.
- `uiux-user-flow-usability-auditor` — Evaluate end-to-end task flows for usability, friction, cognitive load, error recovery, and completion clarity. Use when a signup, checkout, onboarding, or core workflow feels slow, confusing, or hard to recover from.
- `uiux-forms-validation-auditor` — Audit forms, controls, validation, error messages, input masks, autofill, multi-step flows, and submission feedback. Use when forms reject valid input, errors are vague, labels are missing, or completion and recovery need testing.
- `uiux-content-microcopy-auditor` — Audit interface language, labels, instructions, error messages, empty states, confirmations, and content clarity. Use when copy is vague, inconsistent, overly technical, or when microcopy must guide users through errors and empty states.
- `uiux-wcag-accessibility-auditor` — Audit digital interfaces against WCAG 2.2 A/AA and applicable native platform accessibility criteria. Use when checking contrast, semantics, reflow, target size, focus appearance, error identification, or when an accessibility conformance claim must be evidence-backed.
- `uiux-keyboard-assistive-tech-auditor` — Test keyboard-only operation, focus order, screen-reader semantics, accessible names, announcements, and assistive-technology interaction. Use when verifying tab order, focus traps, custom widgets, ARIA, or screen-reader behavior.

## Platform & engineering

- `uiux-mobile-app-auditor` — Audit native and hybrid mobile apps for platform conventions, touch behavior, safe areas, responsive screens, accessibility, navigation, and device conditions. Use when reviewing iOS/Android/Flutter/React Native UI, simulator or device evidence, or mobile-specific failures.
- `uiux-desktop-app-auditor` — Audit native desktop applications across Windows, macOS, and Linux for layout, window behavior, keyboard conventions, HiDPI scaling, accessibility, and interaction quality. Use when reviewing Electron/Tauri/Qt/WPF/WinUI/AppKit apps or desktop-specific window and DPI issues.
- `uiux-cross-browser-device-auditor` — Audit rendering and interaction consistency across browsers, engines, devices, DPRs, operating systems, and input modes. Use when a UI works in one browser but breaks in another, or when Safari/Firefox/Edge/mobile rendering, fonts, scrolling, or input need verification.
- `uiux-cross-platform-app-auditor` — Audit non-web UI beyond standard browsers: cross-platform frameworks, wearables, TV, embedded displays, and CLI/TUI programs. Use when checking Flutter/React Native platform quirks, safe areas, HiDPI, window constraints, terminal box-drawing, or platform-native ergonomics.
- `uiux-frontend-codebase-auditor` — Trace visible UI defects to frontend structure, component boundaries, CSS, state logic, assets, and framework implementation. Use when the rendered defect needs a code-level root cause, when the same bug repeats across screens, or before planning a repair.
- `uiux-css-layout-root-cause-specialist` — Diagnose and repair CSS/layout root causes: flexbox, grid, sizing, overflow, stacking contexts, positioning, and responsive constraints. Use when a layout bug resists surface patches, when `!important` is spreading, or when the parent layout must be fixed properly.
- `uiux-surgical-repair-engineer` — Implement verified UI repairs at the correct level and prove them with closed-loop re-render and re-measure. Use when an audit has produced verified findings and the user authorizes repair, when a fix must preserve behavior and design-system consistency, or when you need before/after evidence and a regression gate.
- `uiux-design-reference-diff-auditor` — Compare a live implementation against design references, screenshots, mockups, or design-system specs and quantify deviations. Use when a build must match Figma or a visual reference, or when pixel and geometry differences need evidence.

## Verification & reporting

- `uiux-visual-regression-engineer` — Build and operate visual regression checks with stable screenshots, baselines, masks, thresholds, and reviewable diffs. Use when establishing visual test coverage, investigating snapshot failures, or preventing repair regressions.
- `uiux-e2e-interaction-test-engineer` — Design and execute end-to-end tests for critical UI tasks, state transitions, navigation, forms, and failure recovery. Use when a flow needs repeatable browser or device verification, or when a repair must be proven end to end.
- `uiux-performance-perceived-speed-auditor` — Audit loading performance and perceived responsiveness: LCP, INP, CLS, feedback latency, rendering, assets, and interaction delays. Use when a UI feels slow, when Core Web Vitals regress, or when loading and feedback states need measurement.
- `uiux-post-repair-verification-engineer` — Verify that UI/UX fixes resolve the reported defect without regressions across screens, states, breakpoints, and platforms. Use when a repair has been implemented and must be proven, when a regression gate is needed, or when a finding's status must be evidence-backed before release.
- `uiux-audit-evidence-report-writer` — Produce actionable UI/UX audit reports with evidence, measurements, severity, reproduction steps, recommendations, and repair status. Use when findings must be documented for engineers, stakeholders, or a release gate, or when audit coverage and limitations need a clear record.
- `uiux-audit-governance-risk-triage` — Triage UI/UX findings, set audit scope, manage change risk, protect brand intent, and decide when to fix, defer, or request clarification. Use when findings compete for priority, when a repair is risky or ambiguous, or when audit scope and authorization need explicit decisions.
