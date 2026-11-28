---
name: uiux-forms-validation-auditor
description: "Audit forms, controls, validation, error messages, input masks, autofill, multi-step flows, and submission feedback. Use when forms reject valid input, errors are vague, labels are missing, or completion and recovery need testing."
---

# Forms & Data Entry Audit

## Use when

- Users cannot complete a form, or errors appear late/vague.
- Labels, required states, autofill, input modes, or validation need review.
- A multi-step form loses data or has unclear progress.

## Do not use when

- The issue is backend validation logic only, with no interface.
- You need a full accessibility audit; use WCAG/keyboard and treat this as forms-specific.

## Mission

Reduce entry errors and make recovery obvious.

## Procedure

1. Inventory each field: label, purpose, type, required/optional status, format, constraints, default, helper text, autocomplete, input mode, and data sensitivity.
2. Check labels are persistent and programmatically associated; placeholder text is not the sole label. Verify required indicators and optional fields are clear.
3. Test valid, invalid, boundary, empty, malformed, duplicate, pasted, autofilled, localized, and long values. Include keyboard and mobile keyboard behavior.
4. Check validation timing: avoid premature error floods, preserve entered values, associate messages with fields, summarize errors for long forms, and move focus appropriately where suitable.
5. Review input masks and formatting. Ensure formatting does not prevent paste, password managers, screen readers, international phone/address formats, or correction.
6. Inspect multi-step forms: progress, back navigation, saved state, conditional fields, review screen, timeout, and confirmation after submission.
7. Check duplicate-submit prevention, loading state, server-side errors, retry, privacy notice, consent, and destructive/irreversible consequences.
8. Fix semantics and validation logic alongside styling; test actual submission behavior instead of considering a green success screen sufficient.

## Precision defaults

- Every input has a visible label; placeholder is not a label.
- Errors inline, specific, and announced; provide an error summary for long forms.
- Set `autocomplete`, `inputmode`, and correct `type`; do not block paste.
- Touch targets >= 44px; inputs >= 16px font on mobile to avoid iOS zoom.

## Quality gates

- [ ] Every field has a meaningful label and clear constraints.
- [ ] Errors explain how to fix the problem and are programmatically associated.
- [ ] Input values survive recoverable failures.
- [ ] Keyboard/autofill/paste and mobile entry are verified.

## Evidence to capture

- Field inventory: label, type, required, autocomplete, validation, error copy.
- Valid/invalid submission screenshots and announcements.
- Multi-step persistence and back behavior.

## Output

Return concise findings and decisions in the standard finding record format. For implementation work, include the exact files/components changed, the underlying cause, tests performed, and any residual limitations. If no defect is found, state the surfaces and states actually checked; do not imply broader coverage.

## Shared contract

Read `../../shared/UIUX_AUDIT_STANDARDS.md` before producing findings. Use its modes, evidence hierarchy, standard finding record, severity/priority model, and verification states. Do not duplicate findings that the shared contract already defines; cite the finding IDs and keep evidence local to this skill.

## Resources

- `../../references/wcag22-quick-reference.md`
- `../../references/state-and-ux-heuristics.md`
