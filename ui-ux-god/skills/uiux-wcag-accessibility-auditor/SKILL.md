---
name: uiux-wcag-accessibility-auditor
description: "Audit digital interfaces against WCAG 2.2 A/AA and applicable native platform accessibility criteria. Use when checking contrast, semantics, reflow, target size, focus appearance, error identification, or when an accessibility conformance claim must be evidence-backed."
---

# Accessibility Audit - WCAG & Inclusive Design

## Use when

- You need a WCAG 2.2 A/AA audit with criterion-level evidence.
- Contrast, semantics, reflow, target size, focus appearance, or error identification is in question.
- A conformance claim, VPAT, or release gate needs defensible findings.

## Do not use when

- You only need a quick automated scan; that is an input, not a conformance audit.
- The product is native-only and WCAG web criteria do not map; use platform equivalents.

## Mission

Identify accessibility barriers using testable criteria and evidence.

## Procedure

1. Set scope and target conformance explicitly. For web content, use WCAG 2.2 Level A and AA as the default audit baseline unless the user or policy specifies another target. Do not label a product WCAG-conformant based on a quick scan.
2. Evaluate the four principles: perceivable, operable, understandable, robust. Map observations to relevant success criteria and distinguish definite failures, potential issues, and not-applicable criteria.
3. Inspect text alternatives, captions/transcripts, semantic structure, headings, labels, relationships, reading order, color contrast, non-text contrast, reflow, text spacing, focus appearance, target size, error identification, and status messages.
4. Use automated tools for detectable issues but verify results manually. Automated scans cannot establish full conformance or assess all meaning, task flow, keyboard behavior, and visual clarity.
5. For native applications, map comparable requirements to platform accessibility APIs and guidelines; do not force web-specific WCAG techniques onto native components without context.
6. Record criterion ID/name, affected element, route/screen, state, evidence, impact, reproducibility, and recommended remediation. Note exceptions and content/platform boundaries.
7. Retest the actual fix and adjacent components. Do not suppress a rule or add ARIA solely to silence a tool if the underlying semantics remain incorrect.

## Precision defaults

- Default target: WCAG 2.2 Level A + AA for web.
- Text contrast 4.5:1; large text 3:1; UI components/graphics 3:1.
- Target size minimum 24x24px (SC 2.5.8); 44/48px is the ergonomic recommendation.
- Reflow at 320px / 400% zoom; text spacing adjustable; focus appearance visible.
- Automated scans are evidence inputs, never proof of full conformance.

## Quality gates

- [ ] WCAG target and version are explicitly stated.
- [ ] Automated scan results are not equated with full accessibility conformance.
- [ ] Each failure is mapped to a criterion when possible.
- [ ] Native platforms are assessed using relevant native semantics and APIs.

## Evidence to capture

- Criterion ID/name, element, route, state, and observed failure.
- Tool output plus manual verification.
- Screenshots/recordings, accessibility tree, and keyboard/AT notes.

## Output

Return concise findings and decisions in the standard finding record format. For implementation work, include the exact files/components changed, the underlying cause, tests performed, and any residual limitations. If no defect is found, state the surfaces and states actually checked; do not imply broader coverage.

## Shared contract

Read `../../shared/UIUX_AUDIT_STANDARDS.md` before producing findings. Use its modes, evidence hierarchy, standard finding record, severity/priority model, and verification states. Do not duplicate findings that the shared contract already defines; cite the finding IDs and keep evidence local to this skill.

## Resources

- `../../references/wcag22-quick-reference.md`
- `../../references/evidence-schema.md`
