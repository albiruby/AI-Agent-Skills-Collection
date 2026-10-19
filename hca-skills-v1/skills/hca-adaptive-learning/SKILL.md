---
name: hca-adaptive-learning
description: Learn from verified outcomes, explicit user corrections, recurring failures, and relevant prior experience. Use only memory and storage facilities actually available.
---

# HCA Adaptive Learning

## Memory capability check
Before claiming continuity, establish whether this harness exposes readable/writable persistent storage. If not, use current-session context only and state the limitation when relevant.

## Memory categories
- Working: current task state and temporary decisions.
- Preference: explicit, stable user preferences.
- Episodic: what happened in a prior task and its outcome.
- Semantic: facts with a source and context.
- Procedural: reusable steps supported by successful outcomes.
- Governance: rules and permissions, maintained through authorized channels.

## Retrieval
Retrieve only records relevant to the current goal, project, or explicit request to recall prior work. Check scope, freshness, source, and possible conflicts. A memory is evidence, not unquestionable truth.

## Write criteria
Consider recording:
- Explicit user corrections or durable preferences.
- A verified failure cause and successful recovery.
- A repeatable procedure that produced a good result.
- Important project decisions or constraints likely to matter later.

Do not save every exchange, one-time instructions, unsupported guesses, credentials, or unnecessary sensitive data.

## Record schema
Use an available supported format; a portable Markdown/JSON record may include:
- id
- type
- scope
- observation
- action
- outcome
- lesson
- source/evidence
- confidence/status
- created_at
- review_after or expiry

Do not invent timestamps or sources.

## Promotion and revision
Treat a single observation as a candidate, not a universal rule. Promote a lesson when it is explicitly confirmed or repeatedly supported in relevant contexts. Retire, qualify, or revise stale lessons when evidence changes. Preserve provenance and resolve contradictions rather than silently overwriting them.

## Safe persistence
Write only through supported mechanisms and authorized paths. Confirm that writes succeeded before claiming memory was updated. Respect retention and deletion requests where supported. Do not modify core policy or this skill automatically as a result of a self-reflection.
