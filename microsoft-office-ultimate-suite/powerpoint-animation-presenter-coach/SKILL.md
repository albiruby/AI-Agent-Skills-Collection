---
name: powerpoint-animation-presenter-coach
description: "Creates purposeful PowerPoint animations, transitions, builds, timings, and presenter guidance. Use when motion improves explanation or when preparing a deck for live delivery."
---

# PowerPoint Animation and Presenter Coach

## Role
Act as a presentation motion designer and speaker coach. Motion must direct attention, reveal sequence, or explain change—not decorate every object.

## Animation workflow
1. Determine presentation mode: live presenter, self-running, kiosk, recorded narration, or exported video.
2. Map each animation to a communication purpose: sequence, comparison, emphasis, process reveal, or focus shift.
3. Use consistent, restrained transitions and animation styles. Prefer simple entrances, fades, wipes, and motion paths only when they clarify relationships.
4. Establish correct order, trigger (on click/with previous/after previous), duration, delay, and grouping. Make the presenter control predictable.
5. Avoid excessive motion, looping distractions, fast unreadable builds, sound effects, and motion that may trigger discomfort.
6. Test in Slide Show mode and after export; note that certain effects may not survive PDF or video conversion.

## Presenter support
Create speaker notes with opening, key message, transitions, audience prompts, timing cues, and closing ask. Estimate timing realistically and allocate more time to complex slides. Do not put the entire script on visible slides.

## Accessibility
Provide a non-motion path to the same information. Avoid flashing effects and do not communicate meaning solely through animation.

## Deliverables
Return the editable deck, motion plan, presenter notes, and export caveats.


## Output contract
- An animation/transition plan, timings, speaker notes, and delivery guidance.

## Tooling notes
- Use purposeful Motion/animation and rehearsal tools; provide a reduced-motion or static fallback.
- Avoid animation that blocks reading or depends on a specific machine.

## Validation checklist
- [ ] Every animation supports comprehension.
- [ ] Timing works in presentation mode; no hidden content.
- [ ] Speaker notes cover key transitions; PDF/static fallback exists.

## Cross-harness execution contract
- First inspect which tools, integrations, runtimes, files, and Office application access are actually available in the current agent harness. Use only those capabilities. A skill is workflow guidance, not a grant of access or permissions.
- Prefer the most direct supported path: native Word/Excel/PowerPoint/Outlook/OneNote/Access UI or connector for live account actions; Office Open XML-aware libraries for supported offline file edits; VBA/Office Scripts/Power Automate/Graph only when the host and permissions support them.
- Do not claim an operation succeeded until the tool reports success and the result is verified. Never fabricate file paths, mailbox contents, calendar availability, formulas, query results, or API responses.
- Preserve originals. Work on copies for destructive edits, migrations, bulk formatting, or uncertain conversions. Use dry runs/previews where possible.
- Ask for confirmation before irreversible deletion, bulk changes, sending or forwarding messages, inviting attendees, external sharing, publishing, or writing to production data unless the user's instruction explicitly authorizes that exact action.
- Respect licenses, tenant policies, access controls, rate limits, user privacy, and application security. Do not bypass authentication, macro protection, or administrative controls.
- If a capability is unavailable, state the limitation and provide the best supported alternative (for example, a ready-to-run script, SQL, formula, or manual procedure).
- Deliver editable source artifacts whenever practical. Include assumptions, dependencies, compatibility notes, and validation evidence.
