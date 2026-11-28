---
name: uiux-navigation-information-architecture
description: "Audit navigation structure, labels, hierarchy, wayfinding, breadcrumbs, search, and information scent. Use when users get lost, menus feel flat, labels are ambiguous, or navigation needs restructuring."
---

# Navigation & Information Architecture

## Use when

- Users cannot tell where they are, what is primary, or how to get back.
- Menus, tabs, breadcrumbs, or search do not match the content hierarchy.
- Labels are ambiguous, inconsistent, or overloaded.

## Do not use when

- The issue is a single broken link or routing bug.
- You need a full usability study; this is an interface/IA audit.

## Mission

Help people understand where they are, where they can go, and how to return.

## Procedure

1. Map the route/screen hierarchy and navigation systems: global, local, contextual, utility, footer, breadcrumbs, tabs, side navigation, and in-page anchors.
2. Compare labels with destination content and user language. Flag vague, duplicate, overly technical, or inconsistent names; preserve domain-specific vocabulary when users need it.
3. Test active/selected state, hierarchy, nesting, overflow, responsive menu behavior, current-location indication, back navigation, deep links, and browser history.
4. Audit search, filtering, sorting, pagination, and empty results for discoverability and understandable recovery. Search results should expose useful context and state.
5. Review wayfinding: page titles, breadcrumbs, section headers, progress indicators, tabs, contextual links, and return paths. Avoid multiple competing navigation patterns without clear purpose.
6. Check navigation accessibility and interaction with keyboard and assistive technology; coordinate deeper checks with accessibility specialists.
7. Recommend structural changes based on user tasks and content relationships rather than aesthetic preference alone. Validate labels and hierarchy against real content.

## Precision defaults

- Top-level navigation: aim for <= 7 items; mobile tabs <= 5.
- Labels: 1–3 words, concrete nouns, consistent terminology.
- Active state must be visible in every nav pattern.
- Deep content needs breadcrumbs, back behavior, or search.

## Quality gates

- [ ] Current location and navigation hierarchy are understandable.
- [ ] Labels accurately predict destination/content.
- [ ] Responsive navigation retains key destinations and state.
- [ ] Deep links, browser history, and return paths behave coherently.

## Evidence to capture

- Navigation inventory and hierarchy map.
- Screenshots of default, active, hover, mobile, and overflow states.
- Label/term consistency table.

## Output

Return concise findings and decisions in the standard finding record format. For implementation work, include the exact files/components changed, the underlying cause, tests performed, and any residual limitations. If no defect is found, state the surfaces and states actually checked; do not imply broader coverage.

## Shared contract

Read `../../shared/UIUX_AUDIT_STANDARDS.md` before producing findings. Use its modes, evidence hierarchy, standard finding record, severity/priority model, and verification states. Do not duplicate findings that the shared contract already defines; cite the finding IDs and keep evidence local to this skill.

## Resources

- `../../references/evidence-schema.md`
- `../../templates/ui-qa-checklist.md`
