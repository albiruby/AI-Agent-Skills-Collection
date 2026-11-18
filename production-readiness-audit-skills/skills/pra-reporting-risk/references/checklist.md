# Checklist — Domains 90–95

## 90. Audit Methodology
- [ ] Whole repository audited before conclusions · actual source · configuration · dependencies · accessible environments · implemented features · requirements & docs
- [ ] Relationships examined: components · frontend↔CMS · app↔external services
- [ ] Behavior checked: production build · browser · viewports · errors & warnings · edge cases · security boundaries · performance bottlenecks · operational risks
- [ ] Every finding verified · no assumptions without evidence · false positives avoided · "safe" never claimed from absence of findings
- [ ] Inaccessible areas, unrun checks and limitations recorded

## 91. Risk Classification & Prioritization
- [ ] Severity per finding (Critical · High · Medium · Low · Informational)
- [ ] Factors: likelihood · impact · exploitability · exposure · business impact · user impact · data sensitivity · operational impact · remediation complexity · regression risk · launch dependency
- [ ] Status per finding: Confirmed · Suspected · Not Reproducible · Not Applicable · Accepted Risk · Resolved · Deferred

## 92. Evidence & Finding Documentation
- [ ] Finding ID · category · title · severity · status · affected file/component/route/environment · exact code location
- [ ] Evidence · reproduction steps · expected vs actual behavior · root cause
- [ ] Technical · business · security · user impact
- [ ] Recommended fix · dependencies · estimated complexity · regression risks · verification procedure · references · resolution status

## 93. Audit Coverage & Verification
- [ ] Total categories · completed · partially completed · not tested · not applicable
- [ ] Critical routes · API endpoints · CMS document types · components · environments · browsers · viewports covered
- [ ] Tests executed/passed/failed/skipped · findings verified/unverified · evidence completeness · remaining uncertainties
- [ ] Source reading ≠ runtime testing ≠ security testing ≠ production verification (reported separately)

## 94. Remediation Planning
- [ ] Group by severity · identify launch / security / functional / architectural / CMS blockers · performance bottlenecks · operational gaps · quick wins · long-term improvements
- [ ] Prioritize · map to affected files · dependent changes · complexity · regression risk · acceptance criteria · test cases · rollback strategy · order
- [ ] Track resolved findings · re-audit modified areas · run regression tests

## 95. Final Production Readiness Assessment
- [ ] Verdict: READY · READY WITH CONDITIONS · NOT READY · INCONCLUSIVE — decided by evidence, not checklist count
- [ ] Weighed: code quality · architecture · security · dependency health · CMS integrity · content quality · functional correctness · responsive behavior · accessibility · performance · SEO · infrastructure · deployment · monitoring · backup · recovery · operational ownership · legal/privacy · cost · maintenance readiness
