# Audit Coverage Matrix

Use one row per domain or meaningful subdomain. "Inspected" and "Verified" must reflect real work performed.

## 1. Domain coverage

| Domain / capability | Applicable? | Inspected? | Executed? | Method used | Verified result | Limitation / next step |
|---|---|---|---|---|---|---|
| Requirements / business logic | Unknown | No | No | — | — | — |
| Functional behavior | Unknown | No | No | — | — | — |
| Security / privacy | Unknown | No | No | — | — | — |
| Data integrity / lifecycle | Unknown | No | No | — | — | — |
| UX / usability / trust | Unknown | No | No | — | — | — |
| Performance / resources | Unknown | No | No | — | — | — |
| Accessibility / compatibility | Unknown | No | No | — | — | — |
| Content / SEO | Unknown | No | No | — | — | — |
| Reliability / operations | Unknown | No | No | — | — | — |
| Architecture / maintainability | Unknown | No | No | — | — | — |
| Analytics / measurement | Unknown | No | No | — | — | — |
| Compliance / digital rights | Unknown | No | No | — | — | — |
| Product / business opportunities | Unknown | No | No | — | — | — |

## 2. Critical journey coverage

| Journey | Traced? | Layers covered | Evidence | Not covered / limitation |
|---|---|---|---|---|
| | | | | |

## 3. Cross-boundary coverage

| Boundary | Inspected? | Method | Result | Limitation |
|---|---|---|---|---|
| Auth / session | | | | |
| Authorization / tenancy | | | | |
| Persistence / transactions | | | | |
| Async jobs / webhooks | | | | |
| Cache / CDN / search | | | | |
| Email / notifications | | | | |
| Analytics / consent | | | | |
| Deployment / version skew | | | | |

## 4. Coverage score

Score each dimension 0–2 (0 absent, 1 partial, 2 strong). Mark N/A when it does not apply.

| Dimension | Score (0–2 / N/A) | Evidence / note |
|---|---:|---|
| Context reconstruction | | |
| Domain selection and applicability | | |
| Critical journey tracing | | |
| Cross-layer analysis | | |
| Security/privacy/trust boundaries | | |
| Money/identity/content/irreversibility | | |
| Failure/retry/concurrency/recovery | | |
| Execution and verification depth | | |
| Evidence quality and reproducibility | | |
| Coverage transparency | | |

Do not average into a precision-looking percentage unless the consumer understands its limits. Safety failures are a gate, not a score.

## 5. Status definitions

- **Applicable:** Evidence indicates the domain matters to this project.
- **Not Applicable:** Evidence indicates the domain is outside this project's actual scope.
- **Unknown:** Insufficient evidence to decide.
- **Inspected:** Relevant files, configuration, paths, or behavior were examined.
- **Executed:** A check or test was actually run.
- **Verified:** The relevant claim was confirmed with sufficient evidence.
- **Blocked:** Access, authorization, environment, or safety prevented work.

Do not use "Passed" as a substitute for explaining what was tested and how.

## 6. Unknown register

| Unknown | Risk if wrong | Why unresolved | Next step / owner |
|---|---|---|---|
| | | | |

## 7. Definition of done

See `references/16-coverage-and-completion.md`. At minimum: scope explicit, domains classified, critical journeys traced or disclosed, findings evidenced, coverage scored, limitations stated.
