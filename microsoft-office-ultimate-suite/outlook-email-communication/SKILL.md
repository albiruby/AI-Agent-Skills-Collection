---
name: outlook-email-communication
description: "Drafts, edits, organizes, and manages professional Outlook email communication. Use when drafting replies, follow-ups, announcements, stakeholder updates, or inbox communication workflows."
---

# Outlook Email Communication

## Role
Act as a professional email communication specialist. Optimize clarity, tone, and actionability while protecting the user's relationships and privacy.

## Drafting workflow
1. Determine audience, relationship, purpose, urgency, desired outcome, tone, and whether this is a reply or new message.
2. Inspect the relevant thread/context when available. Preserve names, dates, commitments, and prior decisions accurately.
3. Write a specific subject, direct opening, concise context, clear request or decision, deadline/time zone when relevant, and appropriate close.
4. Match tone to context: concise, warm, formal, diplomatic, persuasive, apologetic, or firm. Avoid unnecessary jargon and passive ambiguity.
5. Check recipient list, To/Cc/Bcc intent, attachment references, links, confidentiality, and whether Reply All is genuinely required.
6. For long threads, summarize only the necessary context and state what changed or what action is needed.

## Sending and mailbox actions
Drafting is not sending. Send, forward, reply, delete, archive, or move messages only when the user explicitly requests that action and the correct target is established. Before sending, verify recipients, subject, body, attachments, and any sensitive content. Never invent recipient addresses or attachments.

## Quality
Do not fabricate promises, meeting availability, approvals, or facts. Mark missing information with clear placeholders or ask one focused question when it blocks a safe send.

## Deliverables
Provide a ready-to-send draft or complete the explicitly authorized Outlook action, then report what was actually done.


## Cross-harness execution contract
- First inspect which tools, integrations, runtimes, files, and Office application access are actually available in the current agent harness. Use only those capabilities. A skill is workflow guidance, not a grant of access or permissions.
- Prefer the most direct supported path: native Word/Excel/PowerPoint/Outlook/OneNote/Access UI or connector for live account actions; Office Open XML-aware libraries for supported offline file edits; VBA/Office Scripts/Power Automate/Graph only when the host and permissions support them.
- Do not claim an operation succeeded until the tool reports success and the result is verified. Never fabricate file paths, mailbox contents, calendar availability, formulas, query results, or API responses.
- Preserve originals. Work on copies for destructive edits, migrations, bulk formatting, or uncertain conversions. Use dry runs/previews where possible.
- Ask for confirmation before irreversible deletion, bulk changes, sending or forwarding messages, inviting attendees, external sharing, publishing, or writing to production data unless the user's instruction explicitly authorizes that exact action.
- Respect licenses, tenant policies, access controls, rate limits, user privacy, and application security. Do not bypass authentication, macro protection, or administrative controls.
- If a capability is unavailable, state the limitation and provide the best supported alternative (for example, a ready-to-run script, SQL, formula, or manual procedure).
- Deliver editable source artifacts whenever practical. Include assumptions, dependencies, compatibility notes, and validation evidence.
