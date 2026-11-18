# Finding template (one per finding)

```
ID:            <CAT-NNN>
Title:         <specific, e.g. "Sanity write token exposed via NEXT_PUBLIC_ variable">
Category:      <audit domain number + name>
Severity:      Critical | High | Medium | Low | Informational
Status:        Confirmed | Suspected | Not Reproducible | Not Applicable | Accepted Risk | Resolved | Deferred
Launch blocker: yes | no
Environment:   local | preview | production
Affected:      file(s) / component / route / service
Location:      path:line-range
Evidence:      <masked snippet, command + output excerpt, or HTTP observation>
Reproduction:  1. … 2. …
Expected:      …
Actual:        …
Root cause:    …
Technical impact:  …
Business impact:   …
Security impact:   … (if relevant)
User impact:       …
Likelihood / Exploitability / Exposure: …
Recommended fix:   …
Dependencies:      <other findings or changes>
Complexity:        S | M | L
Regression risk:   low | medium | high (+ why)
Verification:      <how to prove it is fixed>
References:        <docs, CVE, WCAG SC, OWASP ID>
Resolution:        <status notes, date, who verified>
```

Rules: no vague titles; one root cause per finding; mask secrets/PII; if Suspected, state the step that would confirm it.
