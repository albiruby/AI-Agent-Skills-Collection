---
name: uiux-content-microcopy-auditor
description: "Audit interface language, labels, instructions, error messages, empty states, confirmations, and content clarity. Use when copy is vague, inconsistent, overly technical, or when microcopy must guide users through errors and empty states."
---

# Content Design & Microcopy Audit

## Use when

- Labels or instructions are vague, inconsistent, or jargon-heavy.
- Error, empty, loading, or confirmation copy does not help the user act.
- Terminology drifts across screens or languages.

## Do not use when

- The issue is visual hierarchy with no content component.
- You need a full content strategy or SEO review.

## Mission

Make the interface understandable without changing product meaning.

## Procedure

1. Review titles, labels, CTA text, navigation, helper text, placeholders, tooltips, onboarding, empty states, errors, alerts, consent, and success messages.
2. Check clarity, specificity, consistency, tone, terminology, sentence length, reading level, localization, capitalization, punctuation, and grammar.
3. Ensure action labels describe outcomes. Prefer concrete verbs over vague labels; distinguish actions such as Save, Publish, Send, Delete, Archive, and Cancel accurately.
4. Check empty and error states for explanation, cause where known, recovery action, and useful next step. Do not blame users or promise that an action succeeded before confirmation.
5. Review content hierarchy and scanability: chunking, headings, lists, emphasis, table labels, helper text proximity, and disclosure of important information.
6. Check localization expansion, pluralization, dates, numbers, currency, time zones, and right-to-left layout where in scope.
7. Preserve legal, medical, financial, and product wording that requires approval. Flag proposed copy changes for review rather than silently rewriting regulated claims.
8. Run a consistency sweep across related screens after updates so the same concept uses the same term.

## Precision defaults

- Sentence case, active voice, concrete verbs; avoid jargon and blame.
- One term per concept; keep a terminology table.
- Errors: what happened + why + how to fix, near the field.
- Empty states: explain the value and provide a primary action.
- Destructive confirmations: name the object and the consequence.

## Quality gates

- [ ] Copy is accurate, actionable, and consistent.
- [ ] Error/empty states include recovery steps.
- [ ] Success language reflects confirmed system outcome.
- [ ] Sensitive or regulated wording is not changed without appropriate review.

## Evidence to capture

- Copy inventory by screen/state.
- Terminology inconsistencies and reading level.
- Before/after copy with the user impact.

## Output

Return concise findings and decisions in the standard finding record format. For implementation work, include the exact files/components changed, the underlying cause, tests performed, and any residual limitations. If no defect is found, state the surfaces and states actually checked; do not imply broader coverage.

## Shared contract

Read `../../shared/UIUX_AUDIT_STANDARDS.md` before producing findings. Use its modes, evidence hierarchy, standard finding record, severity/priority model, and verification states. Do not duplicate findings that the shared contract already defines; cite the finding IDs and keep evidence local to this skill.

## Resources

- `../../references/state-and-ux-heuristics.md`
- `../../templates/ui-qa-checklist.md`
