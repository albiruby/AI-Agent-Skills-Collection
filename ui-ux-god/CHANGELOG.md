# Changelog

## 1.0.0 — 2026-11-28

Initial release. Merges the Gemini “Godmode Audit” suite and the universal GPT “Visual Audit & Repair Studio” into one evidence-based pack.

### Added

- **32 skills:** 1 master (`ui-ux-god`) + 31 specialists.
- **Shared contract:** `shared/UIUX_AUDIT_STANDARDS.md` — modes, authorization, evidence hierarchy, finding record, severity/priority, thresholds, verification states, anti-patterns, output contract.
- **12 references:** evidence schema, severity/priority, platform capture, platform standards, micro-defect catalog, surgical fix patterns, design laws/formulas, state heuristics, WCAG 2.2 quick reference, performance budgets, visual regression playbook, tool capability matrix.
- **10 templates:** audit report, issue evidence, repair plan, QA checklist, viewport matrix, token inventory, implementation handoff, scorecard, coverage ledger, remediation backlog.
- **5 scripts:**
  - `dom_geometry_audit.mjs` — centering, dividers, overflow, clipping, card symmetry, overlap; routes, auth, channels, fail-on.
  - `pixel_precision_audit.py` — Pillow-only margins, optical centering, divider completeness, before/after diff.
  - `design_token_audit.mjs` — contrast, typography, 4px spacing, radius nesting; routes.
  - `interactive_a11y_audit.mjs` — touch targets, focus rings, media, labels, headings; routes.
  - `validate_package.py` — structure, frontmatter, triggers, paths, manifest.
- **3 worked examples:** landing page micro-detail, dashboard responsive/a11y, native mobile platform.
- **3 eval cases + scorecard.**
- Installers, manifest, package metadata, portability guide, references.

### Changed from the source packs

- Deduplicated four overlapping specialist pairs into merged skills:
  - layout grid + layout geometry → `uiux-layout-geometry-auditor`
  - design-system consistency + visual design system → `uiux-visual-design-system-auditor`
  - interaction state + responsive/interaction/a11y → `uiux-responsive-interaction-auditor`
  - component repair + surgical remediator → `uiux-surgical-repair-engineer`
- Replaced the 523-word duplicated boilerplate in 30 GPT skills with one shared contract.
- Rewrote all 32 descriptions with explicit `Use when…` triggers.
- Fixed the Python pixel script (OpenCV Hough shape crash) by making it Pillow-only.
- Fixed Playwright resolution so scripts work when the pack lives outside the target project.
- Fixed relative resource paths and normalized to a `skills/` layout.
- Added `examples/`, `evals/`, `templates/`, `scripts/`, manifest, and validator to the Gemini side; added executable tooling to the GPT side.

### Fixed

- `pixel_precision_audit.py` `IndexError` on OpenCV 4.12 (`lines[:, 0, :]`).
- Python 3.9 compatibility (`str | None`).
- Missing `../` in three cross-skill references.
- Missing `Use when…` triggers in 32 descriptions.
- Inconsistent `uiux-` naming and nested wrapper folders.
