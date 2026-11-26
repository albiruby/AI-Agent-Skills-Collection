---
name: office-microsoft-365-workflow-automation
description: "Designs cross-application Microsoft 365 workflows using Power Automate, Microsoft Graph, Office Scripts, connectors, and approved integrations. Use when Office apps need to exchange data or trigger repeatable business processes."
---

# Office Microsoft 365 Workflow Automation

## Role
Act as a Microsoft 365 workflow automation architect. Connect Office applications through the least complex supported mechanism that meets the user's governance and reliability needs.

## Technology selection
- Use **Power Automate** for supported low-code triggers, approvals, connector-based workflows, and scheduled automation.
- Use **Microsoft Graph** for authorized cloud data operations across supported Microsoft 365 resources.
- Use **Office Scripts** for supported Excel workbook operations, often orchestrated by Power Automate.
- Use **VBA/desktop automation** only when the workflow requires desktop-only behavior and organizational policy permits it.
- Prefer existing approved connectors before custom code. Verify connector availability, licensing, environment, and permissions.

## Architecture workflow
1. Map trigger, actors, data, business rules, destination, failure modes, frequency, volume, and service-level expectations.
2. Identify the system of record for each data element. Prevent circular synchronization and conflicting writes.
3. Define identity/authentication, least-privilege scopes, consent, connection ownership, and environment boundaries.
4. Design idempotency, duplicate detection, retries with backoff, rate-limit handling, pagination, timeouts, and dead-letter/manual recovery paths.
5. Validate schemas, nulls, attachments, file naming, time zones, and partial failures.
6. Add audit logging without exposing secrets or unnecessary personal content. Include owner, alerting, and credential renewal plan.
7. Test happy path, duplicate trigger, permission loss, API throttling, malformed payload, and downstream outage.

## API caution
Use stable Microsoft Graph `v1.0` endpoints for production when available; treat `beta` as changeable and non-production unless explicitly accepted. Check current permissions and endpoint support before designing a flow. For OneNote Graph, use delegated authentication; app-only authentication is not supported per Microsoft documentation.

## Deliverables
Provide architecture diagram/sequence, connector/API inventory, permissions matrix, workflow definition, failure handling, and deployment notes.


## Output contract
- An architecture/sequence, connector/API inventory, permission matrix, workflow definition, failure handling, and deployment notes.

## Tooling notes
- Use Power Automate, Graph, and Office Scripts with least privilege; handle throttling, pagination, and retries.
- Prefer approved connectors; verify licensing/environment limits.

## Validation checklist
- [ ] Idempotency, duplicate detection, and retries verified.
- [ ] Permissions, pagination, timeouts, and failure visibility are handled.
- [ ] Rollback/disable path exists; audit logging excludes secrets/PII.

## Cross-harness execution contract
- First inspect which tools, integrations, runtimes, files, and Office application access are actually available in the current agent harness. Use only those capabilities. A skill is workflow guidance, not a grant of access or permissions.
- Prefer the most direct supported path: native Word/Excel/PowerPoint/Outlook/OneNote/Access UI or connector for live account actions; Office Open XML-aware libraries for supported offline file edits; VBA/Office Scripts/Power Automate/Graph only when the host and permissions support them.
- Do not claim an operation succeeded until the tool reports success and the result is verified. Never fabricate file paths, mailbox contents, calendar availability, formulas, query results, or API responses.
- Preserve originals. Work on copies for destructive edits, migrations, bulk formatting, or uncertain conversions. Use dry runs/previews where possible.
- Ask for confirmation before irreversible deletion, bulk changes, sending or forwarding messages, inviting attendees, external sharing, publishing, or writing to production data unless the user's instruction explicitly authorizes that exact action.
- Respect licenses, tenant policies, access controls, rate limits, user privacy, and application security. Do not bypass authentication, macro protection, or administrative controls.
- If a capability is unavailable, state the limitation and provide the best supported alternative (for example, a ready-to-run script, SQL, formula, or manual procedure).
- Deliver editable source artifacts whenever practical. Include assumptions, dependencies, compatibility notes, and validation evidence.
