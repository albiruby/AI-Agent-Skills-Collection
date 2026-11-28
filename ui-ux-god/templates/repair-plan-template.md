# UI/UX Repair Plan

## 1. Scope and authorization

- **Mode:** Audit + Repair / Full Repair
- **Authorized by:**
- **In scope:**
- **Out of scope:**
- **Stop conditions:** deploy / data change / brand color / shared API / security policy

## 2. Repair backlog

| Order | Finding IDs | Root cause / hypothesis | Change location | Proposed repair | Blast radius | Risk | Verification |
|---:|---|---|---|---|---|---|---|
| 1 | | | | | | Low/Med/High | |

## 3. Grouping

Cluster findings that share one root cause:

| Cluster | Findings | Shared cause | One fix | Screens affected |
|---|---|---|---|---|
| | | | | |

## 4. Guardrails

- Preserve brand and product intent:
- Preserve semantics, keyboard, focus, accessibility:
- Responsive widths/states to retest:
- Shared components affected:
- Tokens affected:
- Tests and rollback considerations:
- Do not use `!important`, magic offsets, or blind transforms:

## 5. Verification plan

| Finding | Re-run audit | Before/after screenshot | Adjacent breakpoint | Regression check | Owner |
|---|---|---|---|---|---|
| | | | | | |

## 6. Change ledger

| File / component | Change | Reason | Risk | Verified |
|---|---|---|---|---|
| | | | | |

## 7. Rollback

- Revert strategy:
- Feature flag / toggle:
- Data migration rollback:
- Communication owner:
