# Mode Runbooks

Use these runbooks to turn the audit modes into concrete sequences. They are guidance, not rigid schedules. Scale to project size, risk, and authorization.

## 0. Selecting a mode

| Request shape | Mode | Default output |
|---|---|---|
| "Audit this project/site" with no narrower target | Deep Audit | Full report |
| "Check this checkout flow", "review this auth implementation", "is this cache safe?" | Focused Audit | Focused report plus adjacent risks |
| "What are we missing?", "pre-mortem", "find blind spots", "stress-test our assumptions" | Blind-Spot Hunt | Ranked hypotheses and discoveries |
| "We fixed the findings — verify", "re-audit after remediation" | Re-audit | Status per prior finding plus regressions |

When the request mixes modes, name the primary mode and the secondary one explicitly in the report. Do not silently expand a focused request into a full audit.

## 1. Shared rules for every mode

1. Establish scope and authorization before any state-changing or external action.
2. Build a context model before selecting tests.
3. Record evidence per claim; separate observed, inferred, and unknown.
4. Keep a running hypothesis list; mark each as confirmed, rejected, or unverified.
5. Stop when the marginal value of another probe is low, when access is exhausted, or when a safety condition triggers.
6. Report coverage honestly. A short audit can be complete for its scope; a long audit can still have gaps.

## 2. Deep Audit

**Purpose:** Broad, risk-weighted review of the project and the boundaries that matter.

**Typical inputs:** repository, documentation, running app or preview, test accounts, logs, deployment configuration.

**Sequence:**

1. **Scope and intake (5–10% of effort).** Target, environments, authorization, criticality, known concerns, success criteria.
2. **Context reconstruction (15–20%).** Project profile, stack, architecture, capabilities, actors, data, trust boundaries, critical journeys.
3. **Flow mapping (15–20%).** Map the 3–7 most important journeys end-to-end. Identify invariants and partial-failure points.
4. **Domain selection (5%).** Mark all domains Applicable / Not Applicable / Unknown with reasons. Load only evidenced adapters.
5. **Baseline (10%).** Run existing tests and safe checks; record pre-existing failures separately.
6. **Deep investigation (30–40%).** Work highest-risk domains and flows first. Use blind-spot methods and edge scenarios. Follow propagation between layers.
7. **Verification and reporting (10–15%).** Re-check claims, deduplicate, classify, score coverage, write report.

**Minimum coverage for a Deep Audit:**

- All 13 domains assessed for applicability; no domain left unclassified.
- Every critical journey traced through its authorization, persistence, and asynchronous boundaries (where they exist).
- At least one validation path for each high-severity claim.
- Security, privacy, and money/identity/irreversibility paths explicitly considered when present.
- Coverage matrix completed with limitations.

**Stop conditions:**

- Agreed time or budget exhausted.
- All applicable high-risk areas have been investigated to the available evidence standard.
- Remaining unknowns require access or authorization that is not available.
- A probe risks production state, user impact, or legal exposure.

**Deliverable depth:** full report, executive summary, coverage matrix, remediation plan, evidence log.

## 3. Focused Audit

**Purpose:** Deep review of one feature, route, component, service, integration, or concern, including its dependencies and adjacent failure paths.

**Typical inputs:** named target, surrounding code, relevant environment, test data, prior findings if any.

**Sequence:**

1. **Define the target precisely (5%).** What is in scope, what is adjacent, what is explicitly excluded.
2. **Map the target context (15%).** Owners, inputs, outputs, data, permissions, dependencies, state.
3. **Trace the target end-to-end (35–45%).** Happy path, failure path, retry, concurrency, authorization, persistence, side effects.
4. **Probe adjacent boundaries (20–25%).** Only where the target depends on them or can affect them.
5. **Verify and report (15%).** Findings, residual risk, coverage, and what a full audit would still need to check.

**Minimum coverage for a Focused Audit:**

- Target behavior mapped in the actual system, not only from documentation.
- Authorization and data-boundary checks traced for every actor who can reach the target.
- Failure, retry, duplicate, and partial-success paths considered.
- Adjacent components identified; those inspected are marked, those skipped are disclosed.
- Findings state whether they are confined to the target or indicate broader risk.

**Stop conditions:**

- Target and adjacent boundaries are understood to the available evidence standard.
- Further probes would require production mutation or unauthorized access.
- Scope would need to expand materially; ask before turning it into a Deep Audit.

**Deliverable depth:** focused report; full template optional but coverage and limitations are mandatory.

## 4. Blind-Spot Hunt

**Purpose:** Hypothesis-driven discovery of neglected assumptions, untested surfaces, cross-layer interactions, and second-order effects.

**Typical inputs:** project or feature, prior audit/report, known blind spots, incident history, product claims.

**Sequence:**

1. **Build a hypothesis backlog (15%).** Use assumption register, contradiction detection, unexplored-surface detection, abuse cases, human workflows, promise-vs-implementation. Aim for breadth before depth.
2. **Rank hypotheses (10%).** Impact × plausibility × verifiability. Prefer hypotheses that cross layers or contradict stated behavior.
3. **Run probes (45–55%).** One hypothesis at a time. Record expected result, actual result, and what it proves. Reject hypotheses explicitly.
4. **Follow surprises (10–15%).** When a probe reveals something unexpected, explore the nearest boundary or shared root cause.
5. **Report discoveries and non-findings (15%).** Distinguish verified blind spots, credible hypotheses, and areas that were checked and held up.

**Minimum coverage for a Blind-Spot Hunt:**

- At least three distinct method families used (for example: contradiction detection, state-transition analysis, cross-layer tracing).
- At least two end-to-end or cross-boundary traces.
- Every hypothesis has a status: confirmed, rejected, blocked, or unverified.
- No claim of "no blind spots" — only "no additional blind spots found within this scope".

**Stop conditions:**

- Hypothesis backlog exhausted or marginal value diminishing.
- Time box reached.
- Access or safety boundary blocks further probes.

**Deliverable depth:** discovery memo with ranked findings, rejected hypotheses worth documenting, and recommended next probes.

## 5. Re-audit / Verification

**Purpose:** Verify remediation claims and detect regressions or newly introduced risk.

**Typical inputs:** prior report or findings list, current code/environment, fix description, deployment state, test evidence.

**Sequence:**

1. **Rebuild the baseline (10%).** Import prior findings, scope, evidence, and acceptance criteria.
2. **Verify each item (45–55%).** Re-run the original verification where safe; otherwise inspect the fix and its tests. Classify: fixed, partially fixed, regressed, unchanged, not reproducible, unverifiable.
3. **Check the fix's blast radius (20–25%).** Look for new failure modes, bypasses, data migration issues, cache/version skew, and behavior changes.
4. **Regression sweep (10%).** Re-check the flows most likely to be affected.
5. **Report closure (10%).** Residual risk, open items, and whether the original severity can be reduced.

**Minimum coverage for a Re-audit:**

- Every prior finding has a status and evidence.
- Fixes are verified against the original acceptance criteria, not just "code changed".
- At least the immediate adjacent flows are checked for regressions.
- New findings are clearly separated from prior findings.
- Unverifiable items state what evidence is missing.

**Stop conditions:**

- All prior items have a status.
- Remaining verification requires production access or data mutation that is not authorized.
- New critical risk is discovered; pause and report before continuing.

**Deliverable depth:** `templates/re-audit.md` plus updated coverage for the re-audited scope.

## 6. Mode anti-patterns

- Calling a checklist review a "Deep Audit" without tracing flows or verifying claims.
- Expanding a Focused Audit without telling the user.
- Running a Blind-Spot Hunt as a random list of tests instead of ranked hypotheses.
- Re-auditing only code diffs and ignoring runtime, data, cache, and deployment state.
- Reporting "all clear" because no additional issues were found within a narrow scope.
- Treating a missing test, missing log, or inaccessible environment as proof of a defect.

## 7. When to escalate

Escalate or pause and ask the user when:

- The evidence suggests an active security incident, data exposure, or ongoing financial loss.
- A test could affect real users, real money, production data, or third parties.
- The requested scope conflicts with safety or legal boundaries.
- The project is materially different from what the request assumed (for example, the "marketing site" includes authenticated billing).
- A finding requires specialized legal, privacy, or compliance judgment.
