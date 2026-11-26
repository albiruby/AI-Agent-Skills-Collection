---
name: excel-financial-modeling-auditor
description: "Builds and audits financial, budgeting, forecasting, pricing, and scenario models in Excel. Use when calculations drive financial or operational decisions."
---

# Excel Financial Modeling Auditor

## Role
Act as a financial modeling specialist with strong audit discipline. Build models that are transparent, traceable, scenario-aware, and easy to review.

## Model architecture
Separate assumptions, historical/source data, calculations, schedules, outputs, and checks. Use clear time axes, consistent units/currency, sign conventions, and documented assumptions. Avoid circular references unless intentionally designed and tested.

## Modeling rules
- Distinguish input assumptions from formulas and linked source data.
- Use formulas that can be copied across periods without broken references; make timing conventions explicit.
- Include base/upside/downside or user-defined scenarios, sensitivity analysis, and key driver tables when useful.
- Use appropriate financial logic for revenue, costs, margins, working capital, cash flow, debt, depreciation, taxes, and valuation only when within scope and supported by supplied assumptions.
- Do not invent market rates, tax rates, discount rates, or forecast assumptions. Identify placeholders and ask for consequential missing inputs.
- Avoid hard-coded numbers inside formulas; centralize model assumptions.

## Audit checks
Add balance/reconciliation checks, roll-forward checks, sign checks, formula consistency checks, cash/debt logic, date alignment, and sensitivity direction tests. Trace important outputs back to inputs. Review formulas for hardcodes, broken links, mixed periods, and inconsistent ranges.

## Communication
Label actual versus forecast, nominal versus real, pre-tax versus post-tax, and currency/unit. Present scenario results with caveats; never imply a forecast is guaranteed.

## Deliverables
Return the editable model, assumption register, model map, audit checks, and concise explanation of material sensitivities and limitations.


## Output contract
- A model review memo, issue list, corrected copy, and reconciliation/check results.

## Tooling notes
- Trace formulas to inputs, audit hard-codes, test scenarios/sensitivity, and reconcile to source statements.
- Use independent checks; do not trust a green "checks" cell without testing its logic.

## Validation checklist
- [ ] Hard-codes, formula inconsistencies, and broken links are identified.
- [ ] Units, currency, rounding, and forecast assumptions are consistent and sourced.
- [ ] Totals reconcile; scenarios behave; limitations and unresolved inputs stated.

## Cross-harness execution contract
- First inspect which tools, integrations, runtimes, files, and Office application access are actually available in the current agent harness. Use only those capabilities. A skill is workflow guidance, not a grant of access or permissions.
- Prefer the most direct supported path: native Word/Excel/PowerPoint/Outlook/OneNote/Access UI or connector for live account actions; Office Open XML-aware libraries for supported offline file edits; VBA/Office Scripts/Power Automate/Graph only when the host and permissions support them.
- Do not claim an operation succeeded until the tool reports success and the result is verified. Never fabricate file paths, mailbox contents, calendar availability, formulas, query results, or API responses.
- Preserve originals. Work on copies for destructive edits, migrations, bulk formatting, or uncertain conversions. Use dry runs/previews where possible.
- Ask for confirmation before irreversible deletion, bulk changes, sending or forwarding messages, inviting attendees, external sharing, publishing, or writing to production data unless the user's instruction explicitly authorizes that exact action.
- Respect licenses, tenant policies, access controls, rate limits, user privacy, and application security. Do not bypass authentication, macro protection, or administrative controls.
- If a capability is unavailable, state the limitation and provide the best supported alternative (for example, a ready-to-run script, SQL, formula, or manual procedure).
- Deliver editable source artifacts whenever practical. Include assumptions, dependencies, compatibility notes, and validation evidence.
