# AI Video QA Scorecard

Score each category from 1 (poor) to 5 (excellent). Mark N/A only when genuinely irrelevant.

| Category | Score | Observations |
|---|---:|---|
| Brief adherence | | |
| Subject/reference fidelity | | |
| Action clarity | | |
| Temporal coherence | | |
| Anatomy/physical interaction | | |
| Contact and grip correctness | | |
| Gravity, weight, and dynamics | | |
| Spatial/temporal continuity of objects | | |
| Camera/composition | | |
| Visual style | | |
| Lighting/color | | |
| Audio/text correctness | | |
| Technical delivery | | |

## Critical defects
- [ ] Wrong subject or identity
- [ ] Missing required action
- [ ] Anatomy or object-interaction failure
- [ ] Object moves before contact (A1) or hand passes through (A2)
- [ ] Ghost grip / non-follow / hover after release (A4, A6, A9)
- [ ] Object vanishes, duplicates, or morphs (D1–D3)
- [ ] Liquid or state change incorrect (C9, D5)
- [ ] Major temporal inconsistency
- [ ] Style drift
- [ ] Unwanted text/audio
- [ ] Technical/export failure
- [ ] Safety or rights concern

## Diagnosis
What failed, and why is that the likely cause?

## Next iteration
What is the smallest useful change?

## Decision
- [ ] Approve
- [ ] Approve with minor defects
- [ ] Regenerate
- [ ] Simplify or split the scene
- [ ] Repair in post-production

## Physics detail
Reference `templates/frame-qa-log.md` and the taxonomy IDs in subskill 21. Any S3 defect or an S2 on a hero beat means do not approve.
