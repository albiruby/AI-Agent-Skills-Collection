# Microsoft Office Ultimate Suite — Universal Agent Skills

A modular, cross-harness Agent Skills package for professional work across Microsoft Word, Excel, PowerPoint, Outlook, OneNote, and Access. It contains **1 master orchestrator + 35 specialist skills**.

## What this package is
These are workflow instructions in the portable `SKILL.md` format. They help an AI agent plan and execute Office work when the active harness exposes suitable application tools, connectors, APIs, file access, or runtimes. **The skills do not install Microsoft Office, grant account access, provide API credentials, or create tools that the agent does not already have.**

## Included application coverage

| Area | Skills | Core coverage |
|---|---:|---|
| Word | 5 | Document architecture, layout, editing, templates/mail merge, accessibility/publishing |
| Excel | 8 | Workbook design, formulas, cleaning, analysis, dashboards, Power Query/Data Model, automation, financial models |
| PowerPoint | 6 | Storyline, slide design, data visualization, animation/presenter support, templates/brand, accessibility |
| Outlook | 4 | Email, inbox workflows, calendar/meetings, contacts/follow-ups |
| OneNote | 2 | Knowledge architecture, meeting and research capture |
| Access | 5 | Database architecture, SQL queries, forms/reports, VBA, migration/integrity |
| Cross-application | 5 | Microsoft 365 automation, file conversion, accessibility, security/governance, QA/delivery |
| Master | 1 | Task routing and end-to-end orchestration |

## Directory structure

```text
microsoft-office-ultimate-suite/
  README.md
  SKILL-INDEX.md
  PORTABILITY-GUIDE.md
  REFERENCES.md
  package.json
  install.sh
  install.ps1
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

The installers copy each skill folder. Existing skills are skipped by default. Use `--overwrite` with Bash or `-Overwrite` with PowerShell only when intentionally replacing existing versions.

## How to use
1. Make sure the harness supports Agent Skills or can load `SKILL.md` instructions from a configured directory.
2. Install the package into the correct skill directory.
3. Give the agent an outcome-oriented request, such as: “Create a quarterly performance workbook from these files and build an executive PowerPoint.”
4. The master skill should route work to the appropriate specialists. You can also invoke a specialist directly by its skill ID if the harness supports direct skill selection.
5. Connect or enable the appropriate Office app, Graph, Power Automate, file, desktop, or scripting tools separately where needed.

## Important implementation notes
- **DOCX/XLSX/PPTX:** offline package libraries are useful for file creation/editing but may not reproduce native Office rendering or features. Reopen and validate important deliverables in Office or a compatible renderer.
- **Excel formulas:** writing a formula into XLSX is not the same as calculating it. Use Excel or a compatible calculation engine to recalculate and verify results.
- **Excel automation:** Office Scripts use TypeScript and are supported in eligible Microsoft 365 Excel environments; availability depends on platform, tenant settings, licensing, and permissions. VBA is mainly a desktop automation path and may be restricted by policy.
- **Outlook:** Graph actions require correct identity, permissions, and mailbox access. Drafting does not equal sending; meeting proposals do not equal invitations.
- **OneNote:** Microsoft Graph OneNote access uses delegated authentication; app-only authentication is not supported. Check current API support before building integrations.
- **Access:** evaluate concurrency, file-size, security, and availability needs. A split Access front end/back end or a server database may be more appropriate than a single shared file.

## Validation
Every skill has YAML frontmatter with only the standard `name` and `description` fields and begins its body with `# Instructions`. The package is vendor-neutral and does not include hidden tool calls or harness-specific runtime dependencies.
