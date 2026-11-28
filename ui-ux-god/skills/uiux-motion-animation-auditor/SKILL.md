---
name: uiux-motion-animation-auditor
description: "Audit transitions, animations, feedback motion, timing, easing, loading indicators, and reduced-motion behavior. Use when motion feels janky, distracting, too slow, or when verifying accessibility and performance of animations."
---

# Motion & Animation Audit

## Use when

- Motion feels janky, sluggish, distracting, or inconsistent.
- You need to verify reduced-motion behavior, loading feedback, or transition timing.
- Animation may be causing layout shift or main-thread jank.

## Do not use when

- The issue is static layout or color.
- Motion is purely decorative and the user has not asked for a motion review.

## Mission

Use motion to explain state change, not obscure interface behavior.

## Procedure

1. Inventory motion: page transitions, modal/drawer entrance, hover transitions, accordion expansion, loading, skeletons, notifications, charts, progress, parallax, and decorative loops.
2. Evaluate purpose, trigger, duration, easing, direction, distance, continuity, interruption, and whether motion communicates hierarchy or state. Identify motion that delays task completion.
3. Check for layout-jumping animation, abrupt transforms, conflicting transitions, hover flicker, animation that restarts unexpectedly, and overlays that move away from the pointer or focus.
4. Test reduced-motion preferences and app-level motion settings. Essential information and state changes must remain understandable without animation.
5. Inspect flashing, strobing, large movement, parallax, auto-playing loops, and motion sensitivity. Do not introduce high-risk flashing behavior.
6. Check loading and feedback timing: users should understand whether an action was accepted, is processing, failed, or completed. Motion cannot be the only feedback channel.
7. Prefer transform/opacity for efficient UI transitions where suitable, while avoiding blanket animation of every property. Verify performance under realistic conditions.
8. Adjust shared motion tokens/components where possible and retest with pointer, keyboard, touch, and reduced motion.

## Precision defaults

- UI micro-interactions: 150–300ms; larger transitions: 200–500ms.
- Enter with ease-out, exit with ease-in; avoid linear for spatial motion.
- Respect `prefers-reduced-motion`; remove non-essential movement.
- Target 60fps; avoid animating layout properties when transform/opacity works.

## Quality gates

- [ ] Reduced-motion mode is tested.
- [ ] Motion does not hide state, block controls, or create unexpected layout shifts.
- [ ] Critical feedback is also available as text/semantic state.
- [ ] Flashing and continuous motion are reviewed for safety and necessity.

## Evidence to capture

- Duration, easing, and animated properties per transition.
- Reduced-motion screenshots/recordings.
- Performance trace or long-task evidence where jank is claimed.

## Output

Return concise findings and decisions in the standard finding record format. For implementation work, include the exact files/components changed, the underlying cause, tests performed, and any residual limitations. If no defect is found, state the surfaces and states actually checked; do not imply broader coverage.

## Shared contract

Read `../../shared/UIUX_AUDIT_STANDARDS.md` before producing findings. Use its modes, evidence hierarchy, standard finding record, severity/priority model, and verification states. Do not duplicate findings that the shared contract already defines; cite the finding IDs and keep evidence local to this skill.

## Resources

- `../../references/state-and-ux-heuristics.md`
- `../../references/wcag22-quick-reference.md`
- `../../references/performance-budgets.md`
