# Evidence, Confidence, Severity, and Prioritization

## 1. Finding classes

- **Verified Finding:** The issue is demonstrated through a safe reproduction, test, runtime observation, or conclusive implementation evidence.
- **Potential Risk:** A credible weakness is indicated, but impact or exploitability needs more verification.
- **Coverage Gap:** A relevant behavior, control, or environment could not be adequately inspected or tested.
- **Improvement Opportunity:** A beneficial change, optimization, or product enhancement; not necessarily a defect.
- **Not Applicable:** The domain does not apply to the actual project scope.

## 2. Evidence hierarchy

Evidence strength depends on the claim. A practical ordering is:

1. Reproducible observed behavior with clear steps and environment.
2. Automated test result or controlled test evidence.
3. Direct runtime/API/database/log observation.
4. Conclusive source/config/schema evidence for a deterministic behavior.
5. Corroborated indirect evidence.
6. Single static indicator or unverified assumption.

This is not an absolute ranking: a source-level authorization bypass may be conclusive without live testing. Explain why evidence supports the claim.

## 3. Confidence

- **High:** Evidence directly establishes the finding or the implementation path makes the behavior unambiguous.
- **Medium:** Strong indicators exist, but a key runtime, environment, or requirement detail remains unverified.
- **Low:** Plausible hypothesis with limited supporting evidence; usually report as a potential risk or coverage gap, not a confirmed defect.

Confidence describes certainty, not importance.

## 4. Severity guidance

- **Critical:** Severe compromise or widespread impact is readily possible, such as broad unauthorized access, major data exposure, or high-impact transaction compromise.
- **High:** Material security, privacy, financial, data-integrity, or availability impact affecting an important workflow or meaningful user group.
- **Medium:** Meaningful but bounded impact, degraded workflow, recoverable data inconsistency, or notable user/business harm.
- **Low:** Limited impact, minor usability/content/accessibility issue, or low-risk maintenance concern.
- **Informational:** Observation or advisory with no demonstrated material harm.

Adjust to context and exposure. Do not assign Critical merely because a vulnerability category sounds serious.

## 5. Likelihood and impact

Consider:

- Preconditions and attacker/user effort.
- Exposure: public, authenticated, internal, privileged, or environment-limited.
- Reach: one record, one tenant, many tenants, or whole service.
- Sensitivity and value of affected data/assets.
- Frequency and ease of occurrence.
- Detectability and reversibility.
- Operational recovery and downstream effects.

## 6. Opportunity prioritization

For opportunities, assess:

- Expected user or business benefit.
- Confidence in the underlying hypothesis.
- Implementation effort and complexity.
- Dependencies and regression risk.
- Ongoing maintenance or operating cost.

Do not imply measured conversion or revenue impact without analytics or research evidence.

## 7. Required finding fields

Every actionable finding should include:

- ID and concise title.
- Classification and domain.
- Severity and confidence.
- Affected location/component/route.
- Evidence and environment.
- Expected vs observed/implemented behavior.
- Impact and plausible scenario.
- Reproduction or verification steps.
- Recommended remediation.
- Regression/side-effect considerations.
- Remaining uncertainty.

## 8. Deduplication

Group repeated symptoms with the same root cause. Preserve separate findings when the affected controls, exploit paths, impact, or remediation meaningfully differ.

## 9. Avoid overclaiming

- Missing test ≠ confirmed bug.
- No alert observed ≠ no monitoring exists.
- No issue found ≠ safe.
- Dependency listed ≠ vulnerable version.
- UI control hidden ≠ access denied.
- API returns 200 ≠ business operation complete.
- Static code pattern ≠ measured performance regression.
- Legal checklist completion ≠ legal compliance certification.

## 10. Machine-readable export

When findings must feed a tracker, dashboard, or remediation workflow, use `templates/findings.schema.json`. Keep the prose report as the primary explanation; the schema is an exchange format.

Minimum fields per finding:

- Stable ID (for example, `WBS-001`).
- Title, class, domain, severity, confidence, status.
- Affected locations/route/component.
- Evidence references and environment.
- Expected vs observed behavior.
- Impact and realistic scenario.
- Verification/reproduction steps.
- Recommendation and acceptance criteria.
- Remaining uncertainty and related findings.

Do not put secrets or personal data in the schema. Use references/redacted descriptions instead.

## 11. Remediation-ready findings

A recommendation is stronger when the owner can verify completion:

- State the desired behavior, not only the missing control.
- Provide acceptance criteria that can be tested.
- Identify dependencies and migration/rollout concerns.
- Note regression risk and adjacent flows to re-check.
- Separate the minimum fix from optional hardening.

Use `templates/remediation-plan.md` when findings become work items.

## 12. Re-audit status model

For follow-up audits, use one status per prior finding:

- **Fixed:** original failure mode no longer reproduces or the change conclusively removes it; verified in the relevant environment.
- **Partially fixed:** some paths are closed, others remain or are unverified.
- **Regressed:** previously fixed behavior is broken again.
- **Unchanged:** same failure mode remains.
- **Not reproducible:** cannot reproduce with available evidence; state conditions.
- **Unverifiable:** access or environment prevents a conclusion.

Never mark an item fixed because code changed or a ticket closed. Record evidence. Use `templates/re-audit.md`.
