# Garmin Connect IQ Development

A single, comprehensive `SKILL.md` for building production-ready Garmin wearables with Monkey C and the Connect IQ SDK: watch faces, widgets (glances), data fields, and audio content provider apps — from first design to Connect IQ Store submission.

## What it covers

The skill walks through the full engineering lifecycle in 26 sections:

- **Model & workflow** — the Connect IQ device/app model, inspecting an existing project before touching it, evidence and version rules.
- **Engineering** — Monkey C standards, manifest/permissions/resources, build tooling and debugging, repository structure.
- **Design** — UI/layout system, adaptive design across device sizes, watch-face engineering, widgets and data fields.
- **Data & background work** — sensors and activity data, ANT+/Bluetooth Low Energy, networking, background services.
- **Quality** — performance, memory and battery optimization, a test matrix, accessibility and wearable UX, localization.
- **Release** — store and distribution readiness, security and privacy, common failure modes, required output formats, and a final quality gate.

## Install

Copy this folder into the skills directory your agent scans (the folder name matches the frontmatter `name: garmin-connect-iq-development`). The skill is harness-neutral: it works as a skill file, pasted instructions, or a custom GPT/Gem prompt.

## When to use

Use when planning or building Garmin wearable software, designing adaptive watch UI, checking device or API compatibility, handling sensors and activity data, optimizing battery and memory use, testing across device profiles, or preparing a Connect IQ Store release.

## Notes

- Device models, API levels, and store policies change — always verify against the current [Connect IQ documentation](https://developer.garmin.com/connect-iq/) before locking a target or submitting a build.
- The skill instructs the agent to discover the installed SDK/tooling versions rather than assume them.
