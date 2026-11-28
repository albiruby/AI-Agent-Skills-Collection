# UI/UX God Mode

An evidence-based UI/UX **audit, micro-detail repair, accessibility, responsive, platform, and verification** studio for AI coding agents.

This pack does not stop at “the design looks off”. It requires the agent to inspect the real rendered interface, measure geometry and computed styles, cite evidence, fix the root cause, and prove the fix with before/after re-rendering.

```text
32 skills = 1 master orchestrator + 31 specialists
```

## Why this pack exists

Most AI UI reviews fail in one of two ways:

1. They read source code and guess what the rendered page looks like.
2. They look at a screenshot and give generic advice with no measurements.

This pack combines both worlds:

- **Rendered evidence** — screenshots, DOM bounds, computed styles, accessibility tree, native view hierarchy, terminal grid.
- **Concrete craft standards** — centering tolerance 1.5px, divider asymmetry 2px, contrast 4.5:1 / 3:1, touch 44/48px, 4/8px rhythm, concentric radius math, type scale, motion timing.
- **Root-cause repair** — fix the parent layout, token, component, state logic, or platform constraint; no `!important` or magic offsets.
- **Closed-loop verification** — re-render, re-measure, compare before/after, test adjacent breakpoints and shared components.
- **Honest coverage** — what was inspected, what was partial, what was blocked, what was not in scope.

## Package contents

```text
ui-ux-god/
├── skills/                  # 32 skills
│   ├── ui-ux-god/           # master orchestrator
│   └── uiux-*/              # 31 specialists
├── shared/
│   └── UIUX_AUDIT_STANDARDS.md
├── references/              # 12 deep references
├── templates/               # 10 operational templates
├── scripts/                 # 5 tools (4 audit + 1 validator)
├── examples/                # 3 worked audits
├── evals/                   # 3 evaluation cases + scorecard
├── README.md / INSTALL.md / PORTABILITY-GUIDE.md
├── REFERENCES.md / SKILL-INDEX.md / CHANGELOG.md
├── LICENSE / skill-pack.json / package.json
└── install.ps1 / install.sh
```

## The 32 skills

### Master

- `ui-ux-god` — routing, modes, 7-phase workflow, severity, verification gate.

### Reconnaissance & visual quality (10)

`uiux-live-interface-inspector`, `uiux-layout-geometry-auditor`, `uiux-microdetail-polish-specialist`, `uiux-visual-design-system-auditor`, `uiux-responsive-layout-auditor`, `uiux-typography-readability-auditor`, `uiux-color-visual-hierarchy-auditor`, `uiux-iconography-asset-auditor`, `uiux-imagery-media-auditor`, `uiux-motion-animation-auditor`.

### UX, interaction & accessibility (7)

`uiux-responsive-interaction-auditor`, `uiux-navigation-information-architecture`, `uiux-user-flow-usability-auditor`, `uiux-forms-validation-auditor`, `uiux-content-microcopy-auditor`, `uiux-wcag-accessibility-auditor`, `uiux-keyboard-assistive-tech-auditor`.

### Platform & engineering (8)

`uiux-mobile-app-auditor`, `uiux-desktop-app-auditor`, `uiux-cross-browser-device-auditor`, `uiux-cross-platform-app-auditor`, `uiux-frontend-codebase-auditor`, `uiux-css-layout-root-cause-specialist`, `uiux-surgical-repair-engineer`, `uiux-design-reference-diff-auditor`.

### Verification & reporting (6)

`uiux-visual-regression-engineer`, `uiux-e2e-interaction-test-engineer`, `uiux-performance-perceived-speed-auditor`, `uiux-post-repair-verification-engineer`, `uiux-audit-evidence-report-writer`, `uiux-audit-governance-risk-triage`.

Full descriptions with triggers: [`SKILL-INDEX.md`](SKILL-INDEX.md).

## Quick start

### OpenCode / Claude Code / Codex / Gemini CLI / Cursor

Install the whole pack into a skill source that scans nested `SKILL.md` files:

```powershell
.\install.ps1 -Destination "$HOME\.config\opencode\skills"
```

```bash
bash ./install.sh ~/.claude/skills
```

Or symlink/junction the pack folder into your global skills directory:

```powershell
New-Item -ItemType Junction -Path "$HOME\.config\opencode\skills\ui-ux-god" -Target "D:\Skills by Albireo\ui-ux-god"
```

Start with:

```text
Use `ui-ux-god` to audit this project and propose a repair plan.
```

Then call a specialist directly when the scope is narrow:

```text
Use `uiux-layout-geometry-auditor` to check why the header logo looks off-center.
Use `uiux-wcag-accessibility-auditor` to audit the checkout form against WCAG 2.2 AA.
Use `uiux-surgical-repair-engineer` to fix the verified P1 findings.
```

## Scripts

All scripts resolve Playwright from the current project first, then from the global npm root. Use `--channel msedge` or `--channel chrome` if a bundled Chromium is not installed.

```bash
# DOM geometry, centering, dividers, overflow, clipping, card symmetry
node scripts/dom_geometry_audit.mjs \
  --url http://localhost:3000 \
  --routes /,/pricing,/checkout \
  --viewports mobile,tablet,desktop \
  --out ./audit-out

# Design tokens, contrast, spacing grid, radius nesting
node scripts/design_token_audit.mjs \
  --url http://localhost:3000 --routes /,/pricing --out ./audit-out

# Touch targets, focus rings, broken/stretched images, labels, headings
node scripts/interactive_a11y_audit.mjs \
  --url http://localhost:3000 --routes /,/checkout --out ./audit-out

# Pixel-level centering, margins, divider completeness (Pillow-only)
python scripts/pixel_precision_audit.py \
  --image ./audit-out/root-desktop-1440.png \
  --out ./audit-out/root-desktop-1440-annotated.png \
  --json ./audit-out/pixel-report.json

# Before/after visual diff
python scripts/pixel_precision_audit.py \
  --before ./audit-out/before.png \
  --after ./audit-out/after.png \
  --out ./audit-out/diff.png

# Validate the pack structure
python scripts/validate_package.py
```

Common options: `--channel`, `--routes`, `--viewports`, `--storage-state`, `--headers`, `--color-scheme`, `--fail-on P0|P1|P2|P3`.

`pixel_precision_audit.py` is Pillow-only; no numpy/OpenCV required. Python 3.9+.

## Modes

- **Audit Only** — inspect and report; no file edits.
- **Audit + Repair** — fix high-confidence, low-risk, in-scope defects.
- **Full Repair** — execute the agreed backlog; deployment/destructive changes still need explicit authorization.
- **Reference Match** — compare against Figma/screenshots/specs.
- **Regression Check** — validate against baselines and critical journeys.

## Workflow

```text
Scope & baseline
  → Reconnaissance
  → Structural/visual audit
  → Precision pass
  → UX/a11y/platform
  → Root cause & plan
  → Repair
  → Verify & regression
  → Report
```

Every finding uses the standard record in [`shared/UIUX_AUDIT_STANDARDS.md`](shared/UIUX_AUDIT_STANDARDS.md): ID, category, severity, confidence, surface, environment, evidence, observed fact, impact, reproduction, cause, fix, verification.

## Default thresholds

| Dimension | Default |
|---|---|
| Centering drift | 1.5px |
| Divider asymmetry | 2px |
| Radius nesting | `R_inner = max(0, R_outer - padding)` |
| Spacing | 4px base / 8px rhythm |
| Body contrast | 4.5:1 |
| Large text / UI contrast | 3:1 |
| Touch target | 44/48px (24px WCAG floor) |
| Focus ring | 2px, 3:1 |
| Reflow | 320px / 400% zoom |
| Body line-height | >=1.35 |
| Measure | 45–75ch |
| Core Web Vitals | LCP <=2.5s, INP <=200ms, CLS <=0.1 |

Full list: [`shared/UIUX_AUDIT_STANDARDS.md`](shared/UIUX_AUDIT_STANDARDS.md).

## Quality gates

- No finding without evidence.
- No “fixed” without re-render and re-measure.
- No `!important`, magic offsets, or blind transforms.
- No full-coverage claim without a route/screen inventory.
- No WCAG conformance claim from an automated scan alone.
- No baseline update to silence a failing visual test.
- No destructive/deploy action without explicit authorization.

## License

MIT. See [`LICENSE`](LICENSE).
