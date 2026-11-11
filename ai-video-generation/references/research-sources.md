# Research Sources (consulted 2026-11-11)

Use as pointers; paraphrase, do not quote at length. Verify current versions.

## Physics and interaction evidence
- CapCut — "Physics and Realism in AI Video: What Improved and What Still Breaks" (Aug 2026). Practical shot-risk guidance and approval checklist; cites Physion-Eval figures (reported: most evaluated clips had at least one human-identifiable physical glitch) and PhyGenBench.
  https://www.capcut.com/create/ai-video-physics-realism-whats-fixed-and-whats-broken
- PhyWorldBench (ICLR 2026; arXiv 2507.13428) — physics adherence benchmark with fundamental, composite, and "anti-physics" categories.
  https://arxiv.org/abs/2507.13428
- VideoScience-Bench (Hao AI Lab) — scientific-reasoning benchmark; reports "great visuals, bad physics" failures.
  https://hao-ai-lab.github.io/blogs/videoscience
- Ego2Act — goal-directed egocentric hand-manipulation benchmark (2,640 videos, 110 tasks); reports failures in fine-grained physical dynamics and dropped steps.
  https://aiweekly.co/alerts/ego2act-benchmark-pins-2640-videos-on-hand-manipulation
- Physion-Eval — arXiv 2603.19607 (cited by CapCut article).
  https://arxiv.org/html/2603.19607v1
- PhyGenBench — OpenGVLab (160 prompts, 27 physical laws).
  https://github.com/OpenGVLab/PhyGenBench
- invideo — "How accurately do AI video generators simulate physics?" (Aug 2026): non-contact physics reliable; complex physics roughly half-successful in its test; recommends multi-take selection.
  https://invideo.io/faq/how-accurately-do-ai-video-generators-simulate-physics/
- Zilliz — why Sora-class models struggle with object physics (learned vs programmed physics; drift over long clips).
  https://zilliz.com/ai-faq/why-does-sora-struggle-with-object-physics

## Prompting and model landscape (secondary)
- VEED, Atlabs, Atlas Cloud — Veo 3.1 prompting guides (five-part prompt formula; first/last frame; reference images).
- Pinggy, Techsy, Dupple, Fliki, PixVerse, Dreamina (CapCut) — 2026 model comparisons; Sora 2 discontinuation reports.

## Limits of this research
Most model-landscape sources are blogs or vendor-adjacent marketing; benchmark results vary by version and date. Re-verify with official documentation before making capability claims.
