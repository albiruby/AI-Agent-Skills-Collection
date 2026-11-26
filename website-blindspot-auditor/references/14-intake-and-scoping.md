# Intake, Scoping, and Authorization

Use this reference before an audit that is ambiguous, high-risk, production-facing, or likely to expand. For small read-only requests, use the fast path and proceed with stated assumptions.

## 1. Fast path (ask at most 6 questions)

Ask only what changes scope, safety, or the usefulness of the result:

1. **Target and environment:** Which repository/site/feature, and is it local, test, staging, preview, or production?
2. **Goal:** Find hidden issues, verify a suspicion, prepare for launch, check a fix, or decide whether to invest further?
3. **Access:** What may I read or run? What is explicitly off-limits?
4. **Criticality:** What would hurt most if it failed — money, access, data, revenue, reputation, compliance?
5. **Known context:** Any recent changes, incidents, complaints, or areas the team already distrusts?
6. **Deliverable:** Quick memo, full report, ticket-ready findings, or verification status?

Do not block on questions that can be answered from evidence. Record an assumption and proceed.

## 2. Full intake bank

Use the relevant groups; do not interrogate the user with every question.

### Product and business

- What does the product do, and who are its users?
- What are the critical journeys and the moments users cannot recover from?
- How does the business make money, and where can money or entitlement be lost?
- What promises are made in marketing, pricing, terms, or onboarding that the system must keep?
- Which metrics or reports are trusted for decisions?
- Are there seasonal peaks, launches, or migrations upcoming?

### System and architecture

- What are the major components, services, data stores, and external providers?
- Which parts are new, recently changed, or known to be fragile?
- Where are the trust boundaries between anonymous users, customers, staff, admins, and services?
- What is authoritative when systems disagree?
- Which environments mirror production, and where do they differ?

### Data and privacy

- What personal, financial, health, or confidential data is processed?
- Where is it stored, exported, logged, cached, or sent to third parties?
- What are the retention, deletion, and consent rules?
- Are there jurisdictions or contractual obligations that may apply?
- May test data be synthetic, or is anonymized production data authorized?

### Access and tooling

- Which repository, runtime, database, logs, analytics, and deployment tools are available?
- Are test accounts or sandbox credentials available?
- Which commands are permitted: tests, build, dependency audit, browser automation, read-only SQL?
- Is there a maintenance window or a freeze?

### Risk and constraints

- What must not be touched?
- What would count as a successful audit?
- What is the time box or budget?
- Who consumes the report, and what decision will it support?

## 3. Authorization matrix

Record explicitly before active testing:

| Action class | Allowed? | Conditions / limits |
|---|---|---|
| Read repository, docs, configuration | | |
| Run existing tests, lint, type-check, local build | | |
| Run dependency or static analysis tools | | |
| Inspect a running local/staging app in a browser | | |
| Use test accounts and synthetic data | | |
| Read production logs or analytics | | |
| Query a database read-only | | |
| Send test emails, webhooks, or payment requests | | |
| Modify code, data, configuration, or dependencies | | |
| Load, fuzz, or state-changing tests | | |
| Test production accounts or third-party systems | | |

When an action is not clearly allowed, treat it as forbidden and report the limitation.

## 4. Scope contract

For a formal audit, capture:

- **Target:** exact repository, URLs, routes, services, versions, and environments.
- **Objective:** the decision or outcome the audit supports.
- **Mode:** Deep, Focused, Blind-Spot Hunt, or Re-audit.
- **In scope:** features, flows, domains, and boundaries.
- **Out of scope:** explicitly excluded systems, data, vendors, and test types.
- **Authorized actions:** from the matrix above.
- **Prohibited actions:** production mutation, real payments, destructive tests, third-party probing.
- **Data handling:** synthetic data only, redaction rules, retention of notes and artifacts.
- **Time box and checkpoints:** when to report interim findings.
- **Deliverables:** memo, full report, schema export, remediation plan, verification.
- **Stop conditions:** what must pause the audit immediately.
- **Contacts and escalation:** who to notify for a critical discovery.

Use `templates/intake-and-scope.md` as the record.

## 5. Ambiguity handling

- If the user says "audit the site", assume a read-only Deep Audit unless context strongly indicates otherwise, and state that assumption.
- If the user names a feature, default to a Focused Audit, not a full audit.
- If the user asks "is it safe?", clarify whether they mean security, correctness, privacy, reliability, or readiness for a specific event.
- If the user asks for a fix, do not silently audit the whole project; use findings only as needed to guide the fix.
- If the target is a production system and active testing is implied but not authorized, restrict to static analysis and clearly state what could not be verified.
- If the user cannot answer scope questions, propose a conservative default and list the assumptions in the report.

## 6. Refusal and boundary cases

Do not perform, even if asked in general terms:

- Intrusive testing against systems the user does not clearly own or have permission to test.
- Credential attacks, denial-of-service, malware, or exfiltration.
- Accessing production personal data beyond what is necessary and authorized.
- Publishing secret values, tokens, private keys, or personal data in the report.
- Legal or compliance certification.

When declining an action, offer the nearest safe alternative: static review, sandbox testing, synthetic data, or a verification plan for the owner to run.

## 7. Handoff to structured audit workflows

When a structured pack such as `production-readiness-audit-skills` is available:

- Use its discovery/scope skills when the user needs a formal pre-launch inventory.
- Use its domain skills to deepen a specific area found here.
- Use its remediation/verification workflow after findings are accepted.
- Do not duplicate the same checks in both skills without stating why.

The audit plan and intake record are portable: they can seed the structured pack without re-interviewing the user.
