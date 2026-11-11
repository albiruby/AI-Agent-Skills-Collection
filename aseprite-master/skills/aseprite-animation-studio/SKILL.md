---
name: aseprite-animation-studio
description: Plans, creates, cleans, times, and validates frame-by-frame pixel-art animations in Aseprite, from simple loops to complex character actions. Use whenever the task is to produce a complete character animation in Aseprite — idle, walk, run, jump, attack, cast, or death — rather than a single pose or a one-off edit.
---

# Animation Studio

## Animation pipeline
1. Confirm frame dimensions, frame count or duration, target FPS, loop behavior, facing direction, and required states.
2. Create or confirm a stable character reference and pivot/ground point.
3. Define the animation's intent and readable key poses.
4. Block key poses before adding in-betweens.
5. Check silhouette and center of mass at each key pose.
6. Add breakdowns and in-betweens only where they improve motion.
7. Add secondary motion (hair, cloth, weapon, accessories) after the primary action reads.
8. Clean clusters and maintain palette, proportions, and outline policy.
9. Set frame durations using actual supported document operations; verify units and timing.
10. Preview at intended speed, not only frame-by-frame.
11. Check loop seam, foot sliding, pops, clipping, and inconsistent pivots.
12. Export a sprite sheet and/or animation format as requested; verify it.

## Motion principles for pixel art
- Use clear anticipation, action, and follow-through when appropriate.
- Favor readable poses over excessive frame count.
- Keep the main silhouette legible during fast motion.
- Preserve contact points and ground plane.
- Use deliberate spacing changes to convey acceleration.
- Avoid random frame changes that look like flicker.
- Keep effects and character layers separable when the project supports it.
- Do not make every frame a simple translation; change pose and cluster shapes to show action.

## Common animation patterns
- Idle: subtle breathing, blink, weight shift; avoid noisy whole-body jitter.
- Walk/run: contact, down, passing, up poses; check foot placement and loop rhythm.
- Jump: anticipation, takeoff, apex, fall, landing/recovery.
- Attack: anticipation, strike, impact, follow-through, recovery.
- Hit reaction: anticipation if needed, impact pose, recoil, recovery.
- Cast spell: charge, release, projectile/effect, recoil or exhaustion.
- Death: clear loss of control and readable final pose; respect requested tone.
- UI/icon animation: consistent bounding box and optical center.

## Timing
- Use the requested FPS or per-frame durations.
- If unspecified, propose a timing plan before committing to complex work.
- Distinguish animation FPS from frame duration in milliseconds.
- Confirm whether the tool expects milliseconds, ticks, or another unit.
- Preview at real speed; a technically valid frame sequence can still feel wrong.

## Loop validation
- Compare first and last poses for position, scale, and energy.
- Ensure there is no duplicate pause or abrupt pop at the seam.
- Check ground contact and repeated motion rhythm.
- Do not force a seamless loop for one-shot actions unless requested.

## Animation review report
Include frame count, total duration, loop/non-loop, timing assumptions, visual defects found, fixes applied, and remaining limitations.
