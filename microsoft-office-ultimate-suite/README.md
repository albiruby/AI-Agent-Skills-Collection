# Microsoft Office Ultimate Suite — Universal Agent Skills

A modular, cross-harness Agent Skills package for professional work across Microsoft Word, Excel, PowerPoint, Outlook, OneNote, Access, Teams/SharePoint, and Microsoft 365 Copilot governance. It contains **1 master orchestrator + 41 specialist skills**.

## What this package is

These are workflow instructions in the portable `SKILL.md` format. They help an AI agent plan and execute Office work when the active harness exposes suitable application tools, connectors, APIs, file access, or runtimes. **The skills do not install Microsoft Office, grant account access, provide API credentials, or create tools that the agent does not already have.**

## Included application coverage

| Area | Skills | Core coverage |
|---|---:|---|
| Word | 6 | Document architecture, layout, editing, templates/mail merge, accessibility/publishing, VBA/field automation |
| Excel | 8 | Workbook design, formulas, cleaning, analysis, dashboards, Power Query/Data Model, automation, financial models |
| PowerPoint | 6 | Storyline, slide design, data visualization, animation/presenter support, templates/brand, accessibility |
| Outlook | 5 | Email, inbox workflows, calendar/meetings, contacts/follow-ups, shared mailboxes/delegation |
| OneNote | 2 | Knowledge architecture, meeting and research capture |
| Access | 6 | Database architecture, SQL queries, forms/reports, VBA, migration/integrity, security/deployment |
| Cross-application | 8 | Microsoft 365 automation, file conversion, accessibility, security/governance, QA/delivery, SharePoint/Teams collaboration, Planner/Forms coordination, Copilot governance |
| Master | 1 | Task routing and end-to-end orchestration |

## Quality system

Beyond the skills themselves, the pack includes optional shared resources:

- `references/tool-recipes.md` — concrete implementation patterns for DOCX/XLSX/PPTX, VBA, Office Scripts, Graph, Access, and validation limits.
- `references/deliverable-checklists.md` — per-app QA and handoff checklists.
- `references/visual-and-accessibility-standards.md` — hierarchy, typography, charts, layout, accessibility, and review gates.
- `templates/` — briefs/specs for Word, Excel, PowerPoint, Outlook, OneNote, Access, automation, and delivery QA.
- `examples/` — three end-to-end worked examples.
- `evals/` — three evaluation cases and a scorecard.

Individual skill folders remain self-contained; shared resources are optional pack-level aids.

## Directory structure

```text
microsoft-office-ultimate-suite/
  README.md
  CHANGELOG.md
  SKILL-INDEX.md
  PORTABILITY-GUIDE.md
  REFERENCES.md
  package.json
  install.sh
  install.ps1
  references/
  templates/
  examples/
  evals/
  <skill-id>/
    SKILL.md
```

## Installation

Install to the skill directory that your AI agent actually reads. Examples:

```bash
# Project-level skills
bash ./install.sh .agents/skills

# Or a global directory configured by your harness
bash ./install.sh ~/.agents/skills
```

PowerShell:

```powershell
.\install.ps1 -Destination ".agents\skills"
```

The installers copy each skill folder. Existing skills are skipped by default. Use `--overwrite` with Bash or `-Overwrite` with PowerShell only when intentionally replacing existing versions. The shared `references/`, `templates/`, `examples/`, and `evals/` folders are pack-level resources and are not copied by the installer; copy them separately if you want them installed alongside the skills.

## How to use

1. Make sure the harness supports Agent Skills or can load `SKILL.md` instructions from a configured directory.
2. Install the package into the correct skill directory.
3. Give the agent an outcome-oriented request, such as:
   - "Create a quarterly performance workbook from these files and build an executive PowerPoint."
   - "Turn these legal comments and HR notes into an accessible Word policy with a manager checklist."
   - "Triage my inbox into action/waiting/FYI, draft replies, and propose next week's meetings. Do not send."
   - "Audit our SharePoint library permissions before enabling Copilot."
   - "Deploy this Access app for eight users without oversharing data."
4. The master skill routes work to appropriate specialists. You can also invoke a specialist directly by its skill ID.
5. Connect or enable the appropriate Office app, Graph, Power Automate, file, desktop, or scripting tools separately where needed.

## Important implementation notes

- **DOCX/XLSX/PPTX:** offline libraries are useful for creation/editing but may not reproduce native rendering or features. Reopen and validate important deliverables in Office or a compatible renderer.
- **Excel formulas:** writing a formula into XLSX is not calculating it. Recalculate in Excel or a verified engine before trusting results.
- **Excel automation:** Office Scripts use TypeScript and are supported in eligible Microsoft 365 environments; availability depends on platform, tenant settings, licensing, and permissions. VBA is mainly a desktop path and may be restricted by policy.
- **Outlook:** Graph actions require correct identity, permissions, and mailbox access. Drafting does not equal sending; meeting proposals do not equal invitations.
- **OneNote:** Microsoft Graph OneNote access uses delegated authentication; app-only authentication is not supported. Check current API support before building integrations.
- **Access:** evaluate concurrency, file size, security, and availability. A split front end/back end or a server database may be more appropriate than a single shared file.
- **SharePoint/Teams:** permissions, sharing links, versioning, and retention are security decisions. Teams tabs inherit SharePoint permissions; verify effective access, not just group names.
- **Copilot:** Copilot can surface content a user already has access to. Oversharing remediation, labels/DLP, and audit readiness are prerequisites, not afterthoughts.
- **Microsoft 365 features:** availability, API support, and admin controls vary by plan and tenant. Verify current documentation before promising a capability.

## Validation

Every skill has YAML frontmatter with only the standard `name` and `description` fields, and begins its body with a title-case H1. The package is vendor-neutral and does not include hidden tool calls or harness-specific runtime dependencies. Each specialist now includes an output contract, tooling notes, and a validation checklist.

## Evaluation

Use `evals/` to test artifact correctness, structure/editability, data integrity, visual quality, accessibility, validation honesty, safety, and handoff. The cases are samples, not a certification.

## Version

Current version: **2.0.0**. See `CHANGELOG.md`.
