---
name: uiux-imagery-media-auditor
description: "Audit images, video, avatars, thumbnails, and media treatments for crop, focal point, resolution, loading, and visual consistency. Use when photos are stretched, crops cut faces, media feels inconsistent, or image performance and fallbacks need review."
---

# Imagery, Media & Art Direction

## Use when

- Images are stretched, cropped badly, or inconsistent in treatment.
- Media causes layout shift, slow loading, or missing fallbacks.
- You need to verify art direction across breakpoints and themes.

## Do not use when

- The issue is an icon or logo; use the iconography specialist.
- You need a full performance audit; use the performance specialist and treat this as media-specific.

## Mission

Ensure media supports content and composition at all breakpoints.

## Procedure

1. Inspect source and rendered media dimensions, aspect ratio, object-fit/object-position, focal point, crop, resolution density, format, compression, transparency, and fallback behavior.
2. Check crop at each viewport and card ratio. Ensure faces, products, labels, and meaningful details are not cut off. Verify focal points remain visible when containers resize.
3. Review visual consistency: color treatment, corner radius, borders, overlays, image style, avatar treatment, thumbnail ratios, and mixed media quality.
4. Check loading states, lazy loading, placeholders, broken sources, layout shift, video poster, captions/transcripts where relevant, and reduced-motion or autoplay behavior.
5. Verify alternative text is appropriate to purpose: informative image gets useful description; decorative image is ignored; complex charts/diagrams have an equivalent text explanation.
6. For generated or manipulated images, preserve factual meaning and brand/IP requirements. Do not invent that a source image has been licensed or approved.
7. Repair object-position, container ratio, responsive source selection, image sizing, and fallback in a reusable way; compare against the original focal point and page balance.

## Precision defaults

- Preserve intrinsic aspect ratio; flag distortion > 2%.
- Serve responsive widths; avoid upscaling beyond 2x intrinsic size.
- Reserve width/height or aspect-ratio to prevent CLS.
- Provide alt text for informative media; empty alt for decorative.

## Quality gates

- [ ] Media crop is inspected at all important sizes.
- [ ] No unexpected distortion, stretching, or layout shift.
- [ ] Alt-text decision reflects image purpose, not filename.
- [ ] Video and animated media have appropriate controls and reduced-motion behavior.

## Evidence to capture

- Natural vs rendered dimensions and aspect ratio.
- Crop/focal-point screenshots across breakpoints.
- Loading strategy, formats, and fallback behavior.

## Output

Return concise findings and decisions in the standard finding record format. For implementation work, include the exact files/components changed, the underlying cause, tests performed, and any residual limitations. If no defect is found, state the surfaces and states actually checked; do not imply broader coverage.

## Shared contract

Read `../../shared/UIUX_AUDIT_STANDARDS.md` before producing findings. Use its modes, evidence hierarchy, standard finding record, severity/priority model, and verification states. Do not duplicate findings that the shared contract already defines; cite the finding IDs and keep evidence local to this skill.

## Resources

- `../../references/performance-budgets.md`
- `../../templates/ui-qa-checklist.md`
