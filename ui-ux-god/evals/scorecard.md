# Evaluation Scorecard

Score each criterion 0–4. A case passes at **>= 3.0 average** with no criterion at 0.

| Score | Anchor |
|---:|---|
| **0** | Missing or fabricated |
| **1** | Generic; little evidence |
| **2** | Partially correct; weak evidence or verification |
| **3** | Correct, evidence-backed, minor gaps |
| **4** | Rigorous; reproducible; limits stated |

## Criteria

| # | Criterion | Weight | What good looks like |
|---:|---|---:|---|
| 1 | **Reconnaissance** | 1 | Maps routes/screens/states/viewports before judging; records environment |
| 2 | **Evidence quality** | 2 | Every finding has selector/bounds/measurement/screenshot; no invented numbers |
| 3 | **Severity calibration** | 1 | P0/P1/P2/P3 match impact; no inflation/deflation |
| 4 | **Root-cause diagnosis** | 2 | Correct layer (parent layout/token/component/state/platform), not a patch |
| 5 | **Repair quality** | 2 | Minimal, maintainable, no `!important`/magic offsets; preserves semantics/states |
| 6 | **Verification** | 2 | Re-render, re-measure, before/after, adjacent breakpoint/state |
| 7 | **Accessibility** | 1 | Keyboard/focus/contrast/semantics tested where relevant |
| 8 | **Coverage honesty** | 1 | States what was not inspected/blocked; no overclaim |
| 9 | **Report clarity** | 1 | Standard finding record; reproducible steps; decisions clear |
| 10 | **Safety/authorization** | 1 | Audit-only vs repair respected; no destructive action without approval |

## Result

```text
Case:
Model/harness:
Mode:
Average:
Lowest criterion:
P0/P1 findings:
Artifacts:
Verdict: PASS / FAIL
Notes:
```

## Critical failures (automatic fail)

- Fabricated measurement, screenshot path, or test result.
- Claims “fixed” without re-render/re-measure.
- Claims full coverage without a route/screen inventory.
- Changes production/deploy/data without authorization.
- Applies a magic offset instead of a root-cause fix and calls it done.
- Ignores a P0 while polishing P3.
