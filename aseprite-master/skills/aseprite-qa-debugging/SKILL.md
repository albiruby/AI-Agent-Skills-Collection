---
name: aseprite-qa-debugging
description: Performs visual and technical QA on Aseprite sprites, animation loops, layers, frame timing, transparency, sprite sheets, and exported assets. Use when an existing sprite, animation loop, or exported sheet must be checked for defects, or when something looks wrong and needs a minimal targeted fix.
---

# QA and Debugging

## Two independent checks
1. Visual QA: does it look right?
2. Technical QA: does the file behave and export correctly?

Passing one does not imply passing the other.

## Visual checklist
- Readable silhouette at native resolution
- Clear focal point and value hierarchy
- Consistent palette and light direction
- No stray pixels or accidental clusters
- No tangents, unintended holes, or awkward single-pixel noise
- Stable proportions across animation frames
- Clear motion arc and key poses
- No unexpected jitter, clipping, or sudden scale changes
- Loop seam reads correctly
- Background and transparency match the brief

## Technical checklist
- Correct canvas dimensions
- Correct frame dimensions and frame count
- Correct layer visibility and order
- Correct frame durations and loop behavior
- Correct color mode / alpha where relevant
- Correct export naming and paths
- Correct spritesheet spacing and padding
- Metadata matches the actual image
- Source remains editable and saved

## Debug loop
1. Describe the defect precisely.
2. Identify the smallest responsible region/frame/layer.
3. Make a minimal correction.
4. Reinspect the affected area and adjacent frames.
5. Re-run the relevant checks.
6. Record any remaining limitation.

## Do not
- Claim visual QA from metadata alone.
- Claim timing QA without previewing or verifying frame durations.
- Claim alpha transparency from a checkerboard-looking flattened image alone.
- Mark an asset as perfect; report concrete checks and known limitations.
