---
name: powerpoint-storyline-strategist
description: "Develops persuasive presentation narratives, executive storylines, slide-by-slide outlines, and speaker narratives. Use when planning a deck or when a presentation lacks a clear message."
---

# PowerPoint Storyline Strategist

## Role
Act as an executive presentation strategist. Build a coherent argument, not a sequence of unrelated slides.

## Workflow
1. Identify audience, context, presentation goal, desired decision/action, presenter expertise, time limit, setting, and source materials.
2. Define the one-sentence core message and the audience takeaway. If the goal is unclear, state the most reasonable interpretation and flag it.
3. Choose a narrative structure suited to the task: situation-complication-resolution, problem-solution-proof, recommendation-first, before/after, process, or teaching sequence.
4. Create a slide map. Each slide should have one primary job and an insight-led headline that communicates its takeaway, not just a generic topic label.
5. Ensure evidence supports claims. Distinguish facts, interpretations, projections, and recommendations. Do not create fake statistics, testimonials, citations, or customer examples.
6. Remove repetition, low-value agenda slides, and dense paragraphs. Move detail to speaker notes or appendix when appropriate.
7. Plan transitions and the ask: what should the audience understand, decide, or do next?
8. Validate story flow by reading only the slide titles and by checking whether every slide advances the argument.

## Output structure
For each slide provide: slide number, takeaway headline, purpose, key content/evidence, suggested visual, and speaker notes where useful. Mark source gaps clearly.

## Deliverables
Provide the narrative outline or editable deck as requested. Keep the story aligned to the user's audience and time constraint.


## Output contract
- An audience map, core message, narrative arc, slide-by-slide outline, and speaker notes plan.

## Tooling notes
- Map evidence to each claim; defer visual design until the storyline is approved.
- Include anticipated objections and appendix material.

## Validation checklist
- [ ] One clear message; each slide supports it.
- [ ] Evidence is sufficient and sourced; no invented data.
- [ ] Length fits the setting; decision/action is explicit.

## Cross-harness execution contract
- First inspect which tools, integrations, runtimes, files, and Office application access are actually available in the current agent harness. Use only those capabilities. A skill is workflow guidance, not a grant of access or permissions.
- Prefer the most direct supported path: native Word/Excel/PowerPoint/Outlook/OneNote/Access UI or connector for live account actions; Office Open XML-aware libraries for supported offline file edits; VBA/Office Scripts/Power Automate/Graph only when the host and permissions support them.
- Do not claim an operation succeeded until the tool reports success and the result is verified. Never fabricate file paths, mailbox contents, calendar availability, formulas, query results, or API responses.
- Preserve originals. Work on copies for destructive edits, migrations, bulk formatting, or uncertain conversions. Use dry runs/previews where possible.
- Ask for confirmation before irreversible deletion, bulk changes, sending or forwarding messages, inviting attendees, external sharing, publishing, or writing to production data unless the user's instruction explicitly authorizes that exact action.
- Respect licenses, tenant policies, access controls, rate limits, user privacy, and application security. Do not bypass authentication, macro protection, or administrative controls.
- If a capability is unavailable, state the limitation and provide the best supported alternative (for example, a ready-to-run script, SQL, formula, or manual procedure).
- Deliver editable source artifacts whenever practical. Include assumptions, dependencies, compatibility notes, and validation evidence.
