# Evaluation Harness

Test whether the merged pack produces grounded documentation and real, clean visual assets rather than plausible-looking output.

## Cases

| Case | Focus |
|---|---|
| [`cases/01-garmin-visual-pack.md`](cases/01-garmin-visual-pack.md) | Simulator capture, clean cutout, store compositions, claims |
| [`cases/02-web-docs-pack.md`](cases/02-web-docs-pack.md) | README/architecture accuracy, links, OG visuals |
| [`cases/03-mobile-release.md`](cases/03-mobile-release.md) | Mobile captures, store panels, permissions, release notes |

## Protocol

1. Give the agent only the scenario prompt and the authorized project/inputs. Do not expose the seeded issues.
2. Use a fresh session with the pack installed.
3. Capture the files, tool calls, and QA evidence.
4. Score with [`scorecard.md`](scorecard.md).
5. Repeat at least twice; record variance.

## Pass criteria

- No fabricated features, devices, metrics, or screenshots.
- Clean assets use the requested crop type and contain no chrome.
- Store assets match dimensions and are derived from clean assets.
- Documentation commands/claims are evidence-linked.
- No secrets or personal data in docs/images.
- QA report distinguishes checked vs unverified.
- No claim of store compliance without official verification.

## Limitations

Results depend on the harness, tools, project, and model. This is a sample, not a certification.
