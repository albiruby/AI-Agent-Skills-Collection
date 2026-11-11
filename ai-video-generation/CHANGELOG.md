# Changelog

## v2.0 — 2026-11-11
Added: Physics & Interaction Validation layer (subskills 15–23): overview and gates with risk tiers R0–R4, Object Interaction Protocol, Contact & Collision Logic, Gravity & Dynamics, Hand-Object Interaction, Spatial & Temporal Physics Continuity, Physics Error Taxonomy (IDs A–F with severities), Frame-by-Frame QA, Failure Recovery ladder (L0–L9).
Added: Subskill 24 — Web Research and Capability Verification (source hierarchy, query templates, capability sheet, prompt-injection safety, offline mode).
Added: templates — physics risk assessment, interaction spec, continuity ledger, frame QA log, iteration log, capability sheet, shot list. Updated QA scorecard and project profile with physics sections.
Added: references — physics cheatsheet, interaction prompt patterns, dated model-landscape snapshot (unverified), research sources.
Added: examples — grabbing a watering can, watering plants, opening a door.
Added: scripts — video_probe.sh, extract_frames.sh, contact_sheet.py (with ROI overlay), roi_motion.py (heuristic pre-contact motion check). Tested on synthetic videos (see README).
Added: PLUG-AND-PLAY.md for chat interfaces without skill support.
Changed: master SKILL.md (workflow gates, language rule, load matrix, research requirement); appended pointers to subskills 02, 03, 06, 08, 10, 11. Fixed README installation instructions.

## v1.0
Initial package: master skill, 14 subskills, 3 templates.
