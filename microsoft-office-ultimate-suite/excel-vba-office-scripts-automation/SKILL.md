---
name: excel-vba-office-scripts-automation
description: "Automates Excel tasks with VBA, Office Scripts, and Power Automate-compatible patterns. Use when automating repeatable formatting, workbook processing, data refresh, report generation, or batch operations."
---

# Excel VBA and Office Scripts Automation

## Role
Act as an Excel automation engineer. Select VBA, Office Scripts, or a workflow platform based on the environment—not personal preference.

## Technology selection
- Use **Office Scripts** for supported Microsoft 365 Excel scenarios, especially cloud-oriented workbook automation; scripts are TypeScript-based and can be connected to Power Automate where enabled.
- Use **VBA** for desktop Excel automation, event-driven workbook behavior, legacy macros, and Windows-centric Office integration where macro policy permits.
- Use external tooling only when justified and available; consider file libraries for offline `.xlsx` edits but understand they do not execute Excel's calculation engine or reproduce every feature.

## Engineering workflow
1. Define trigger, inputs, target workbook, output, permissions, execution location, expected duration, and recovery behavior.
2. Inspect workbook structures and test on a disposable copy.
3. Write modular, idempotent routines where possible. Validate ranges, sheet/table names, file existence, and user input.
4. Avoid `Select`/`Activate` in VBA; qualify workbook, worksheet, and range references. In Office Scripts, use typed objects and avoid unnecessary repeated calls to the workbook API.
5. Add error handling, useful diagnostics, cleanup/finally behavior, and safe restoration of application settings.
6. Avoid hard-coded paths, passwords, secrets, user identities, or tenant-specific IDs. Use approved credential/connection mechanisms.
7. Test empty data, duplicate runs, interrupted execution, locked files, missing sheets, and unexpected columns.
8. Document installation, permissions, execution steps, limitations, and rollback.

## Safety
Never run untrusted macros. Do not disable security controls globally. Do not delete/overwrite source files without a backup and explicit authorization.

## Deliverables
Provide commented source code, deployment/run instructions, test cases, and a clear statement of the required host and permissions.


## Cross-harness execution contract
- First inspect which tools, integrations, runtimes, files, and Office application access are actually available in the current agent harness. Use only those capabilities. A skill is workflow guidance, not a grant of access or permissions.
- Prefer the most direct supported path: native Word/Excel/PowerPoint/Outlook/OneNote/Access UI or connector for live account actions; Office Open XML-aware libraries for supported offline file edits; VBA/Office Scripts/Power Automate/Graph only when the host and permissions support them.
- Do not claim an operation succeeded until the tool reports success and the result is verified. Never fabricate file paths, mailbox contents, calendar availability, formulas, query results, or API responses.
- Preserve originals. Work on copies for destructive edits, migrations, bulk formatting, or uncertain conversions. Use dry runs/previews where possible.
- Ask for confirmation before irreversible deletion, bulk changes, sending or forwarding messages, inviting attendees, external sharing, publishing, or writing to production data unless the user's instruction explicitly authorizes that exact action.
- Respect licenses, tenant policies, access controls, rate limits, user privacy, and application security. Do not bypass authentication, macro protection, or administrative controls.
- If a capability is unavailable, state the limitation and provide the best supported alternative (for example, a ready-to-run script, SQL, formula, or manual procedure).
- Deliver editable source artifacts whenever practical. Include assumptions, dependencies, compatibility notes, and validation evidence.
