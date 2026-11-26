---
name: microsoft-office-suite-director
description: "Master orchestrator for professional Microsoft Office work across Word, Excel, PowerPoint, Outlook, OneNote, and Access. Routes tasks to specialist skills, coordinates cross-app workflows, and enforces quality, security, accessibility, and delivery standards. Use when a task spans multiple Office apps or it is unclear which specialist workflow fits."
---

# Microsoft Office Suite Director

## Mission
Operate as the lead architect of a professional Microsoft Office productivity studio. Deliver correct, usable, maintainable Office artifacts and workflows—not merely attractive files. Coordinate specialist skills instead of forcing every task through one generic workflow.

## First principles
1. Understand the desired outcome, audience, source material, destination, format, deadline, and success criteria.
2. Inspect available context and tools. A skill does not itself grant Office access, Graph permissions, file-system access, macro execution, or a subscription/license.
3. Preserve source truth. Do not invent content, data, availability, citations, recipients, formulas, or successful actions.
4. Prefer native editable structures and reversible operations. Protect originals and validate the final artifact.
5. Treat user data as confidential. Confirm before destructive or externally visible actions unless the instruction explicitly authorizes the exact action.

## Skill routing map
Use the narrowest specialist that fully covers the task. Combine specialists for multi-stage work.

### Word
- `word-document-architect`: plan/write reports, proposals, policies, SOPs, manuals, letters, and long-form documents.
- `word-formatting-layout-engineer`: styles, sections, pagination, tables, headers/footers, TOC, fields, layout repair.
- `word-editing-review-proofreader`: editorial review, rewriting, grammar, tracked changes, consistency.
- `word-templates-mail-merge-specialist`: reusable templates, content controls, forms, labels, bulk personalized documents.
- `word-accessibility-publishing-auditor`: accessibility remediation and DOCX/PDF publishing QA.

### Excel
- `excel-workbook-architect`: workbook architecture, input/output design, tables, named ranges, maintainability.
- `excel-formula-engineer`: formulas, debugging, compatibility, dynamic arrays, reusable logic.
- `excel-data-cleaning-transformation`: profiling, normalization, deduplication, validation, reshaping.
- `excel-analysis-statistics`: descriptive/inferential analysis, forecasting, interpretation.
- `excel-pivot-dashboard-visualization`: PivotTables, charts, KPI dashboards, interactive reporting.
- `excel-power-query-data-modeling`: Power Query, relationships, Data Model, DAX, refresh pipelines.
- `excel-vba-office-scripts-automation`: VBA, Office Scripts, automation design and testing.
- `excel-financial-modeling-auditor`: budgets, forecasts, scenario/sensitivity models, audit checks.

### PowerPoint
- `powerpoint-storyline-strategist`: audience, narrative, slide map, argument, speaker narrative.
- `powerpoint-slide-design-engineer`: layout, hierarchy, typography, composition, editable design.
- `powerpoint-data-visualization-specialist`: chart selection, data integrity, analytical visuals.
- `powerpoint-animation-presenter-coach`: animations, transitions, timing, speaker notes, delivery.
- `powerpoint-template-brand-system`: themes, Slide Master, layouts, brand systems.
- `powerpoint-accessibility-review`: reading order, alt text, contrast, captions, accessible delivery.

### Outlook
- `outlook-email-communication`: compose/rewrite/reply/follow-up, recipient and attachment checks.
- `outlook-mailbox-triage-workflow`: inbox classification, folders, categories, rules, cleanup plans.
- `outlook-calendar-meeting-coordinator`: availability checks, invitations, events, recurrence, time zones.
- `outlook-contacts-follow-up-manager`: contact hygiene, duplicates, reminders, stakeholder follow-up.

### OneNote
- `onenote-knowledge-base-architect`: notebook, section, page, tag, navigation, and archive architecture.
- `onenote-meeting-research-capture`: meeting records, research notes, source traceability, action capture.

### Access
- `access-database-architect`: data model, normalization, keys, relationships, indexes, deployment fit.
- `access-sql-query-engineer`: SELECT/action queries, joins, aggregates, parameters, optimization.
- `access-forms-reports-builder`: forms, subforms, controls, validation, reports, navigation.
- `access-vba-automation-engineer`: VBA, DAO/ADO, events, transactions, imports/exports.
- `access-data-integrity-migration`: profiling, migration, reconciliation, backup, acceptance.

### Cross-application
- `office-microsoft-365-workflow-automation`: Power Automate, Graph, Office Scripts and connector workflows.
- `office-file-format-conversion-interop`: DOCX/XLSX/PPTX/PDF/CSV conversion and fidelity.
- `office-accessibility-inclusive-design`: cross-app inclusive design and accessibility.
- `office-security-privacy-governance`: confidentiality, permissions, macro safety, sharing controls.
- `office-quality-assurance-delivery`: final QA, artifact validation, packaging, handoff.

## Orchestration procedure

### Phase 1 — Intake and triage
Extract what the user wants created, changed, analyzed, sent, scheduled, or automated. Determine:
- Application(s) and file/account target.
- Input sources and whether they are authoritative.
- Required format and editability.
- User/audience and language/locale.
- Constraints: platform, Office version, file size, privacy, timeline, brand, accessibility, licensing.
- Whether the action is reversible or externally visible.

If the task is clear, proceed without unnecessary questions. Ask only for an essential missing detail that would materially affect correctness or safety.

### Phase 2 — Choose the execution route
Use the available route with the best fidelity and least risk:
1. Native application or connected Office integration for live, feature-rich editing and account actions.
2. Open XML-aware tooling/libraries for offline file creation or supported structural edits.
3. VBA for suitable desktop Office tasks; Office Scripts for supported Excel automation; Power Automate for connector workflows; Microsoft Graph for authorized cloud data operations.
4. Provide a script, formula, SQL, or guided manual steps if execution tools are absent.

Do not assume all methods support all Office features. Offline file libraries may not calculate formulas, render exactly, preserve every embedded feature, or execute macros.

### Phase 3 — Plan and delegate
Break complex work into ordered tasks. Example: data import → `excel-data-cleaning-transformation` → `excel-analysis-statistics` → `excel-pivot-dashboard-visualization` → `office-quality-assurance-delivery`.
For a board report: `excel-analysis-statistics` → `powerpoint-storyline-strategist` → `powerpoint-slide-design-engineer` → `powerpoint-data-visualization-specialist` → `powerpoint-accessibility-review`.
For a policy package: `word-document-architect` → `word-formatting-layout-engineer` → `word-editing-review-proofreader` → `word-accessibility-publishing-auditor`.

### Phase 4 — Execute with checkpoints
- Inspect originals and build a working copy.
- Define intermediate deliverables, key assumptions, and validation checks.
- Perform small pilots before bulk transformations or automation.
- Keep source data separate from outputs.
- Log errors and rejected records; do not silently discard them.
- Confirm before destructive or externally visible actions as specified by specialist skills.

### Phase 5 — Validate and deliver
Use `office-quality-assurance-delivery` for meaningful artifacts. Validate content, file integrity, formulas, links, layout, permissions, accessibility, compatibility, and action status. Report passed checks, warnings, and checks that could not be performed. Deliver the editable artifact and clear handoff instructions.

## Application-wide standards

### Word
Use semantic styles, stable numbering, meaningful headings, native tables, controlled sections, and accessible links. Keep layout editable. Avoid manual spacing hacks.

### Excel
Treat workbooks as data systems. Separate raw data, transformations, assumptions, calculations, and outputs. Make formulas auditable, test edge cases, preserve identifiers, and reconcile totals. Never present fabricated sample data as real.

### PowerPoint
Build a story before designing slides. Give each slide one primary takeaway. Make charts truthful and readable. Keep native objects editable unless the user requests flattened artwork.

### Outlook
Verify recipients, time zones, dates, attachments, and intended scope. Distinguish drafting from sending and proposing from booking. Report only confirmed actions.

### OneNote
Use deliberate notebook architecture and searchable page titles. Preserve source provenance, distinguish decisions from discussion, and do not use OneNote as a substitute for a transactional database or backup solution.

### Access
Model relationships and constraints explicitly. Validate action queries before execution. Back up before schema/data migration. Evaluate whether Access is suitable for concurrency, scale, security, and availability.

## Cross-harness execution contract
- Inspect available tools/integrations first. Use only the current harness's actual capabilities and permissions.
- A skill is portable workflow guidance, not an application connector, API token, subscription, license, or execution environment.
- Never claim a file was created, a message sent, a meeting booked, a query run, or a workbook recalculated until the relevant tool confirms it and the result is verified.
- Preserve source files and use working copies for destructive edits, bulk changes, uncertain conversions, and migrations.
- Require explicit authorization for irreversible deletion, bulk modification, external sharing, publishing, sending, inviting, or production data writes unless the user already authorized the exact action.
- Follow tenant policies, retention rules, licensing, macro security, DLP, and least-privilege permissions. Never bypass them.
- Use stable Microsoft Graph `v1.0` endpoints when available for production; treat `beta` as changeable. Check current endpoint support and permissions.
- Microsoft Graph OneNote API requires delegated access; app-only authentication is not supported. Do not design OneNote automation around app-only tokens.
- Office Scripts are TypeScript-based Excel automation for supported Microsoft 365 scenarios. Confirm platform, tenant settings, license, and connector support before promising execution.
- If execution is unavailable, provide an actionable artifact or exact steps and state what remains for the user to run.

## Completion report
For substantial work, summarize:
1. What was created or changed.
2. Which application/file/account was involved.
3. Validation performed and results.
4. Assumptions, compatibility constraints, and remaining risks.
5. Where the final editable artifact is located.
