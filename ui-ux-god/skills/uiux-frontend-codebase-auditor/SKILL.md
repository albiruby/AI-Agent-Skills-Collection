---
name: uiux-frontend-codebase-auditor
description: "Trace visible UI defects to frontend structure, component boundaries, CSS, state logic, assets, and framework implementation. Use when the rendered defect needs a code-level root cause, when the same bug repeats across screens, or before planning a repair."
---

# Frontend Codebase Diagnosis

## Use when

- A rendered defect needs a `file:line` root cause, not just a visual description.
- The same bug repeats across screens and may share a component or token.
- You need to map a route/state to its component, style, and data path.

## Do not use when

- You have no source access; report the visual finding and a precise handoff instead.
- The issue is purely visual with an obvious CSS fix and no code tracing needed.

## Mission

Connect what users see to the code that produces it.

## Procedure

1. Identify framework, router, rendering model, styling system, component library, state management, build tooling, and conventions from project files before proposing implementation changes.
2. Trace the affected UI from route to page component to shared component to style/token and data/state source. Search for duplicated components and global selectors that influence the area.
3. Inspect computed styles and DOM ancestry alongside source CSS to identify cascade, specificity, inherited styles, CSS modules, utility classes, container queries, and runtime style injection.
4. Check console errors, failed assets/fonts, hydration warnings, React/Vue/etc. key/state issues, event handlers, layout shifts, and failed network requests if tools are available.
5. Identify root cause category: layout constraint, asset defect, token drift, content/data variation, state mismatch, browser compatibility, runtime bug, or missing requirement.
6. Before editing, inspect package scripts and tests, relevant docs, component usage sites, and architecture boundaries. Avoid unrelated refactors.
7. Propose the narrowest robust code change. Preserve framework idioms, type safety, semantic markup, design tokens, and existing tests.
8. Report files changed, cause, expected impact, tests run, and unresolved limitations.

## Precision defaults

- Trace route → page → layout → component → style/token → state.
- Record exact `file:line` and the rendered evidence it explains.
- Distinguish confirmed cause from hypothesis.
- Check framework boundaries: server/client, hydration, CSS-in-JS, shadow DOM.

## Quality gates

- [ ] A visible finding is linked to source/component cause when source access exists.
- [ ] Existing project conventions are followed.
- [ ] No invented framework, test command, or package is assumed.
- [ ] Changes stay within authorized scope.

## Evidence to capture

- File/component/line references and the rendered symptom.
- Computed style or state values that confirm the cause.
- Related call sites and shared-component impact.

## Output

Return concise findings and decisions in the standard finding record format. For implementation work, include the exact files/components changed, the underlying cause, tests performed, and any residual limitations. If no defect is found, state the surfaces and states actually checked; do not imply broader coverage.

## Shared contract

Read `../../shared/UIUX_AUDIT_STANDARDS.md` before producing findings. Use its modes, evidence hierarchy, standard finding record, severity/priority model, and verification states. Do not duplicate findings that the shared contract already defines; cite the finding IDs and keep evidence local to this skill.

## Resources

- `../../references/evidence-schema.md`
- `../../references/surgical-fix-patterns.md`
