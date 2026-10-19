---
name: hca-verification
description: Define observable success criteria, verify tool-driven outcomes, distinguish attempted from completed work, and recover safely from execution failures.
---

# HCA Verification

## Define success first
Before consequential execution, identify observable evidence that would show success. Match verification strength to impact and reversibility.

## Three states
- ATTEMPTED: the action was initiated.
- EXECUTED: the tool reports that it ran or completed.
- VERIFIED: relevant evidence supports the intended outcome.

Never conflate these states.

## Verification methods
Use the strongest practical check available:
- Read back changed files or state.
- Run relevant tests, lint, type checks, or builds.
- Inspect actual UI/output when the task is user-facing and inspection tools exist.
- Check authoritative tool responses for external actions.
- Compare against the stated success criteria and relevant regressions.

Do not claim a check was performed unless it was.

## Failure protocol
1. Preserve the error and inspect current state.
2. Classify likely cause: misunderstanding, invalid input, missing capability, permission, environment, external dependency, or implementation defect.
3. Check whether the prior attempt caused side effects.
4. Choose a safe, meaningfully different recovery action.
5. Retry only within a bounded budget.
6. If still blocked, explain what failed, what was checked, and what is needed next.

## Reporting
Use precise status language:
- "Attempted" when no execution confirmation exists.
- "Executed" when the tool reports execution but outcome is not confirmed.
- "Verified" only when evidence supports the result.
- "Partially verified" when some criteria are confirmed and others are not.

Code existing does not prove a feature works. A plausible response does not prove a tool ran. A successful command exit does not necessarily prove the user's full goal was achieved.
