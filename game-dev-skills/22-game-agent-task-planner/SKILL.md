---
name: game-agent-task-planner
description: Convert a game design and tech decisions into an ordered, agent-executable implementation plan (epics, tasks, acceptance criteria, file structure, prompts) for AI coding agents; includes vertical-slice-first sequencing and verification steps.
---

# Game Agent Task Planner

## Inputs
PROJECT_BRIEF, GDD (01), engine/stack (02, 03), platform matrix (16), art/audio specs (06, 07, 09).

## Sequencing (always vertical-slice first)
1. **M0 Skeleton**: project init, folder structure, CI build, boot -> menu -> empty level -> quit, logging, config.
2. **M1 Core loop prototype**: player controller (13), camera, one enemy/obstacle, win/lose, placeholder art/audio, restart in <3 s.
3. **M2 Vertical slice**: one polished level with final-quality art/audio/UI (06-09), save/load, settings, pause.
4. **M3 Systems**: progression/economy (04), AI (12), inventory/quests (11), level content (10), PCG (21).
5. **M4 Online/Services** if required (14): auth, leaderboards, cloud save, IAP, ads (18).
6. **M5 Content complete + polish**: balance, juice, perf (15), accessibility/localization (20).
7. **M6 QA & Release**: compat tests (16/17), store assets (19), build pipeline, launch.

## Task format (one per task)
```
ID: M1-03
Title: Implement player jump with coyote time and input buffer
Context: link to GDD section + 13 parameters
Files to create/modify: <paths>
Steps: 1..n (small, verifiable)
Acceptance criteria: measurable (e.g. "jump apex 3.0 tiles +/-0.1; coyote 100 ms; unit test passes")
Test/verify: how the agent proves it (run command, screenshot, test)
Depends on: M1-01, M1-02
Out of scope: ...
```

## Agent rules
- Small tasks (<=1 focused change), commit per task, keep the game runnable at every commit.
- Data-driven: values in config files, not code. Placeholder assets named per 07 so swaps need no code edits.
- Run build + tests after each task; report failures with logs; don't mark done without verification.
- Don't add dependencies/plugins without recording the decision (ADR) and license check.
- Ask the human for: art direction approvals, balance feel, store accounts/keys, legal decisions.

## Output
Milestone roadmap, backlog table (ID, title, depends, estimate, acceptance), first 10 tasks fully written, risk list, and a copy-paste master prompt for the coding agent containing the brief, stack, conventions and rules above.
