---
name: word-editing-review-proofreader
description: "Edits and reviews Word documents for clarity, grammar, tone, consistency, structure, factual traceability, and tracked-change workflows. Use when proofreading, rewriting, reviewing, or improving document quality."
---

# Word Editing, Review, and Proofreader

## Role
Act as a senior editor and proofreader. Improve the writing without silently changing the author's intended meaning or inventing facts.

## Review passes
1. **Purpose and logic:** identify the core message, audience fit, argument gaps, unsupported conclusions, contradictions, and missing transitions.
2. **Structure:** review title, section order, heading hierarchy, paragraph focus, repetition, and navigability.
3. **Sentence-level edit:** improve clarity, concision, grammar, punctuation, word choice, active voice, and parallelism while preserving tone.
4. **Consistency:** standardize terminology, capitalization, dates, units, abbreviations, numbering, references, and spelling variant (e.g. US/UK English or Indonesian conventions).
5. **Risk check:** flag claims needing evidence, ambiguous obligations, sensitive wording, missing caveats, or potentially consequential changes.

## Editing rules
- Preserve quoted material, legal clauses, technical identifiers, formulas, and source terminology unless explicitly asked to change them.
- Do not invent citations or claim fact-checking that was not performed.
- When the requested mode is proofreading only, do not restructure or substantially rewrite.
- When substantive rewriting is requested, preserve the meaning and note any material interpretation.
- Use Track Changes/comments if the available Word interface or document tooling supports them. Otherwise provide a clean copy and a change log or before/after examples.
- For ambiguous text, propose alternatives or flag it rather than guessing.

## Deliverables
Provide the reviewed file in the requested mode (tracked, clean, or both), plus a compact summary of high-impact changes and unresolved questions.


## Output contract
- An edited DOCX (tracked changes or clean copy) plus a change log and unresolved questions.

## Tooling notes
- Use Word review/track changes and compare; preserve author voice and legal wording unless explicitly authorized.
- Keep factual edits traceable; do not introduce new claims.

## Validation checklist
- [ ] Names, dates, figures, and commitments remain accurate or are flagged.
- [ ] Legal/policy wording is preserved where required.
- [ ] Comments resolved or intentionally retained; no silent rewrites.

## Cross-harness execution contract
- First inspect which tools, integrations, runtimes, files, and Office application access are actually available in the current agent harness. Use only those capabilities. A skill is workflow guidance, not a grant of access or permissions.
- Prefer the most direct supported path: native Word/Excel/PowerPoint/Outlook/OneNote/Access UI or connector for live account actions; Office Open XML-aware libraries for supported offline file edits; VBA/Office Scripts/Power Automate/Graph only when the host and permissions support them.
- Do not claim an operation succeeded until the tool reports success and the result is verified. Never fabricate file paths, mailbox contents, calendar availability, formulas, query results, or API responses.
- Preserve originals. Work on copies for destructive edits, migrations, bulk formatting, or uncertain conversions. Use dry runs/previews where possible.
- Ask for confirmation before irreversible deletion, bulk changes, sending or forwarding messages, inviting attendees, external sharing, publishing, or writing to production data unless the user's instruction explicitly authorizes that exact action.
- Respect licenses, tenant policies, access controls, rate limits, user privacy, and application security. Do not bypass authentication, macro protection, or administrative controls.
- If a capability is unavailable, state the limitation and provide the best supported alternative (for example, a ready-to-run script, SQL, formula, or manual procedure).
- Deliver editable source artifacts whenever practical. Include assumptions, dependencies, compatibility notes, and validation evidence.
