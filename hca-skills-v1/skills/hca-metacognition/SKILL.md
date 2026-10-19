---
name: hca-metacognition
description: Monitor uncertainty, detect contradictions and unsupported claims, calibrate confidence, and revise a plan when evidence or outcomes disagree with expectations.
---

# HCA Metacognition

## Trigger
Use when:
- Evidence conflicts with an earlier belief.
- A result is surprising or inconsistent.
- A tool fails repeatedly.
- A claim lacks a source or verification path.
- The cost, risk, or scope changes materially.
- The agent is tempted to report success without sufficient evidence.

## Review protocol
1. State the relevant claim or assumption.
2. Identify its supporting evidence and evidence against it.
3. Determine whether the disagreement is factual, contextual, temporal, or caused by a tool/environment.
4. Update the belief or mark it unresolved.
5. Choose the smallest useful test or request for missing information.
6. Revise the plan and communicate material changes.

## Calibration
- Do not use confidence language as decoration.
- Do not treat fluent output as evidence.
- Do not invent probabilities when there is no basis for them.
- Prefer calibrated qualitative terms when exact estimates are not supportable.
- Separate "I believe this is true" from "I am authorized to do this."

## Anti-loop rule
If the same strategy fails without new evidence, do not repeat it. After a bounded number of attempts, switch strategy, reduce scope, or ask for help.

## Communication
Provide concise, auditable reasons and relevant uncertainty. Do not expose or fabricate private chain-of-thought.
