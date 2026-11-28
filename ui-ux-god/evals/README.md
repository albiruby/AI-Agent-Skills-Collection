# Evaluation Harness

Three representative cases for checking whether an agent actually follows the audit-and-repair workflow, rather than producing a generic UI review.

## Cases

| Case | Focus | Skills expected |
|---|---|---|
| [01 — Micro-detail landing](cases/01-microdetail-landing.md) | Logo centering, divider, focus ring, contrast, repair proof | `ui-ux-god`, `uiux-layout-geometry-auditor`, `uiux-microdetail-polish-specialist`, `uiux-surgical-repair-engineer`, `uiux-post-repair-verification-engineer` |
| [02 — Responsive dashboard](cases/02-responsive-a11y-dashboard.md) | Mobile overflow, table scroller, modal focus, chart encoding, CLS | `uiux-responsive-layout-auditor`, `uiux-responsive-interaction-auditor`, `uiux-wcag-accessibility-auditor`, `uiux-performance-perceived-speed-auditor` |
| [03 — Native platform](cases/03-native-platform-audit.md) | Safe area, touch target, keyboard, back behavior, large text | `uiux-mobile-app-auditor`, `uiux-cross-platform-app-auditor`, `uiux-keyboard-assistive-tech-auditor` |

## How to run

1. Give the agent the case prompt and the fixture (repo URL or screenshots + source access).
2. Let it work in the allowed mode.
3. Score with [scorecard.md](scorecard.md).
4. A case passes at **>= 3.0 / 4.0 average** with no criterion at 0.
5. Record the transcript and artifacts; compare across model/harness versions.

## What the harness checks

- Does the agent **inspect before judging**?
- Does every finding have a route, state, viewport, and measurable evidence?
- Does it distinguish fact, hypothesis, and recommendation?
- Does it fix the root cause instead of applying a magic offset?
- Does it re-render and re-measure before claiming “fixed”?
- Does it state coverage and limitations honestly?

## Anti-gaming rules

- A finding without evidence is not a finding.
- A “fix” without before/after evidence is not verified.
- A high score without a P0/P1 list and coverage statement is invalid.
- Do not reward verbosity; reward traceable decisions.
