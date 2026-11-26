# Blind-Spot Discovery Methods

These are reasoning procedures. Use them to generate testable hypotheses, not to manufacture findings.

## 1. Assumption register

For every important flow, identify assumptions such as:

- Input is valid because the UI validates it.
- A request is sent only once.
- External APIs respond quickly and correctly.
- A user remains authenticated throughout an action.
- Data is fresh because it was recently fetched.
- A role or tenant ID supplied by the client is trustworthy.
- A background job eventually succeeds.
- Deleting a record removes every copy.
- A successful HTTP response means the business operation completed.

Classify assumptions as verified, disproven, or unknown. Challenge assumptions with the greatest impact first.

## 2. Negative and boundary testing

Try realistic invalid, missing, repeated, extreme, stale, and interrupted inputs/states. Include null/empty values, unexpected types, boundary lengths, invalid formats, expired tokens, duplicate requests, and partial completion where applicable.

Do not use destructive payloads against production or systems outside authorization.

## 3. State-transition analysis

Model important entities as states and transitions. Ask:

- Which transitions are allowed, forbidden, reversible, or terminal?
- Can two transitions race?
- Can a stale client overwrite newer state?
- Can a user repeat or skip a transition?
- What happens if a transition succeeds in one system but fails in another?
- Does the UI represent the authoritative state?

## 4. Contradiction detection

Compare:

- Product wording vs actual behavior.
- UI permission vs server enforcement.
- API contract vs runtime response.
- CMS schema vs frontend assumptions.
- Database constraints vs business rules.
- Analytics events vs actual user actions.
- Documentation vs current implementation.
- Error messages vs recoverability.

## 5. Second-order analysis

For each important finding or proposed fix, ask:

- What new failure mode might this create?
- What other component relies on this behavior?
- Does it affect caching, authorization, analytics, billing, exports, or background work?
- Does it change old data or only new data?
- What happens during deployment when old and new versions coexist?
- Could it create cost, latency, or operational burden elsewhere?

## 6. Unexplored-surface detection

Look for:

- Routes, handlers, jobs, or admin actions without tests or clear ownership.
- Branches that are difficult to reach through the UI.
- API endpoints not represented in navigation.
- Configurations that alter security or runtime behavior.
- Error paths with no user feedback or logs.
- Features with no recovery or rollback path.
- Third-party callbacks and asynchronous paths.
- Shared utilities used by many features but tested narrowly.

A missing test is a coverage gap, not automatic proof of a bug.

## 7. Abuse-case analysis

Think like an unauthorized or over-privileged actor, within safe and authorized scope:

- Can inputs be manipulated outside the UI?
- Can an action be repeated, automated, or reordered?
- Can another user's object be referenced?
- Can limits be bypassed through concurrency or alternate endpoints?
- Can content or files execute or mislead downstream systems?
- Can errors reveal information?

Do not exploit third-party or live targets without explicit authorization.

## 8. Human workflow analysis

Examine what operators, editors, support staff, or administrators must do:

- Can they identify failure and affected users?
- Can they correct mistakes safely?
- Is there an audit trail for consequential actions?
- Are bulk operations reversible or previewable?
- Are responsibilities and manual handoffs clear?
- Does recovery depend on undocumented knowledge or one individual?

## 9. Opportunity discovery

Look beyond defects:

- Can a confusing task be simplified?
- Is important functionality hard to discover?
- Can avoidable manual work be automated safely?
- Can a user understand status, cost, or next steps earlier?
- Can performance or infrastructure costs be reduced without harming quality?
- Can observability make support and incident response easier?

Label evidence-based opportunities separately from speculative product hypotheses.

## 10. Promise-versus-implementation analysis

Collect explicit promises: pricing, guarantees, limits, delivery times, privacy claims, security claims, support hours, cancellation terms, and onboarding copy. For each material promise, trace the implementation and find where the promise is enforced, computed, or merely displayed.

Ask:

- What must be true in code/data/operations for this promise to hold?
- Which surface enforces it: UI, API, job, contract, or manual process?
- What happens at the boundary (refund window, quota, trial end, guarantee expiry)?
- Which promise is contradicted by another page, email, or policy?

Report the contradiction only when the promise is explicit and the implementation evidence is sufficient.

## 11. Invariant derivation

Derive invariants from business meaning, not from current code:

- Money: one charge per intended purchase; totals reconcile; refunds reverse revenue and access.
- Access: a user sees only authorized objects/tenants; revocation propagates everywhere.
- Inventory/capacity: confirmed commitments never exceed available units.
- Publication: unpublished content is not publicly reachable, indexed, or cached.
- Identity: account/email changes cannot be completed by the wrong party.
- Lifecycle: deletion/export matches the stated policy across stores.

Then ask which layer should enforce each invariant and whether any path bypasses it.

## 12. Change and version-skew analysis

Use recent changes, release notes, migrations, feature flags, and dependency upgrades as a map of likely blind spots:

- What changed without corresponding tests or docs?
- Which clients, workers, caches, or integrations still assume the old shape?
- Can old and new versions coexist during deploy or rollback?
- Did a configuration/default change alter behavior silently?
- Is a feature flag partially rolled out, leaving inconsistent states?

Do not blame a recent change without evidence; use it to prioritize hypotheses.

## 13. Shadow-process and workaround analysis

Look for the manual steps people invented to keep the system working:

- Spreadsheet exports, copy/paste between tools, manual reconciliation.
- Support scripts that repair data directly.
- One person who "always fixes" a recurring issue.
- Retry rituals or "do not click twice" instructions.
- Off-system approvals, emails, or chat confirmations.

A workaround is evidence that the formal workflow is incomplete, unreliable, or unclear. It may also create unlogged access or data copies. Treat it as a finding or coverage lead, not automatically a defect.

## 14. Counterfactual reasoning

For each important claim, ask what would have to be true for the opposite conclusion:

- "This endpoint is protected" — what proves every path reaches the check?
- "The cache is per-user" — what makes the key user-specific?
- "The webhook is idempotent" — what prevents the second event from repeating the effect?
- "Deleted data is gone" — which stores were checked?
- "The report is accurate" — which event definition and reconciliation support it?

Use the counterfactual to choose the next probe. If the answer is unknown, that is a coverage gap, not a finding.
