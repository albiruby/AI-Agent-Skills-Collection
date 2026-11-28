# Severity, Priority & Decision Log

Use this reference when findings compete for attention. Severity describes impact; priority describes what to do next.

## 1. Severity (impact)

| Level | Label | Definition | Typical examples | Action |
|---|---|---|---|---|
| **P0** | Critical / Broken | Core task blocked, content unreadable, or trust/safety severely damaged | Checkout dead-end; primary text clipped at 320px; page-wide horizontal scroll; overlapping interactive controls; broken hero image; primary text contrast <3.0:1; severe accessibility barrier | Stop polish; fix now |
| **P1** | High / Structural | Major task or brand surface visibly broken, or a systemic defect | Logo >2px off-center; divider stops short; broken grid; uneven sibling cards; body contrast <4.5:1; touch target <44px; keyboard trap; missing page title | Primary remediation pass |
| **P2** | Medium / System | Meaningful friction or localized inconsistency | 13px spacing on a 4px grid; radius pinch; 4 rogue font sizes; missing focus-visible ring; missing loading/empty/error state; inconsistent button heights | Production-quality pass |
| **P3** | Low / Craft | Small polish with limited task impact | 1–2px optical nudge; missing `tabular-nums`; orphan headline word; subtle shadow-direction drift | Polish pass |
| **Info** | Observation | Enhancement or opportunity, not a defect | “Consider a sticky table header”; “Could add a skip link” | Backlog / discuss |

### Severity calibration rules

- Severity is about **user impact**, not code difficulty. A one-line CSS bug that blocks checkout is P0.
- A defect on a hidden admin page can still be P1 if it blocks an operational task.
- Do not inflate severity to get attention. Do not downgrade a P0 because the fix is hard.
- If the same root cause produces several symptoms, assign the highest severity to the cluster and list the symptoms.
- If you cannot verify impact, label confidence **Low** and state the assumption.

## 2. Priority (scheduling)

Priority combines impact with reach, confidence, effort, and timing:

```text
priority ≈ (impact × reach × confidence) / effort
```

| Factor | Low (1) | Medium (2) | High (3) |
|---|---|---|---|
| **Impact** | Cosmetic | Friction | Blocks a core task |
| **Reach** | Rare edge case | One segment/page | Most users / primary flow |
| **Confidence** | Hypothesis | Partial evidence | Reproduced with measurement |
| **Effort** | Days / cross-team | Hours / one component | Minutes / one token |

Use the result as a conversation aid, not false precision. Adjust for:

- **Release timing:** a pre-launch P1 may outrank a post-launch P0 on a low-traffic page.
- **Dependencies:** a token change blocked by a brand decision moves to `clarify`.
- **Blast radius:** a shared-component fix that touches 40 screens needs more verification.
- **Brand risk:** intentional asymmetry or a campaign color may need a product decision.
- **Regression risk:** a risky fix can be deferred behind a safer mitigation.

### Priority bands

| Band | Meaning | Action |
|---|---|---|
| **Now** | P0 or high-impact P1 with high confidence and low effort | Fix in the current pass |
| **Next** | P1/P2 with clear evidence but moderate effort | Schedule in the repair backlog |
| **Later** | P2/P3 or lower reach | Batch with related work |
| **Clarify** | Ambiguous intent, brand trade-off, or missing access | Ask; do not guess |
| **Reject** | Not a defect, out of scope, or contradicts product intent | Record why |

## 3. Decision log

Record every non-obvious decision:

```markdown
| ID | Finding | Decision | Reason | Owner | Follow-up |
|---|---|---|---|---|---|
| GEO-001 | Logo off-center | fix | Confirmed 35.5px drift; grid fix is low risk | Frontend | Verify 375/768/1440 |
| COL-004 | Brand accent fails 4.5:1 | clarify | Darkening changes brand color | Design | Decide by Friday |
| MOT-002 | Parallax hero | defer | P3; reduced-motion fallback exists | Frontend | Next sprint |
```

## 4. Audit scope and authorization

Before triage, write down:

- **Mode:** Audit Only / Audit + Repair / Full Repair / Reference Match / Regression Check.
- **In scope:** routes, screens, states, viewports, platforms, themes.
- **Out of scope:** explicitly excluded areas.
- **Access:** credentials, devices, design files, repositories actually available.
- **Stop conditions:** what requires approval (deploy, data change, brand color, shared API).

If the user says “fix everything”, treat it as **Full Repair** for verified visual findings, but still require explicit authorization for deployment, destructive actions, production data, and security/access policy changes.

## 5. Common triage mistakes

- Fixing P3 polish while P0 overflow remains.
- Treating every finding as P1.
- Scheduling a shared-token change from one component without checking all consumers.
- Calling a brand decision a bug.
- Marking a finding “fixed” because the code changed, not because it was re-verified.
- Hiding a P0 behind “known issue” without a mitigation or owner.
