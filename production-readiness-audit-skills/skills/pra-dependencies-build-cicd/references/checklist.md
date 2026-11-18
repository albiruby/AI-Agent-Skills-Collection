# Checklist — Domains 12–14

## 12. Dependency & Package Audit
- [ ] `package.json` · lockfile · package-manager consistency
- [ ] Direct · transitive · dev · peer · optional dependencies
- [ ] Unused · duplicate · outdated · deprecated · unsupported · abandoned packages
- [ ] Suspicious packages · typosquatting · provenance · maintainer reputation · known malware reports
- [ ] License compatibility · vulnerability advisories · dependency conflicts
- [ ] Version compatibility · breaking changes · Node.js compatibility · React/Next.js compatibility
- [ ] Bundle-size contribution · runtime overhead · update policy · automated update configuration

## 13. Build & Compilation Audit
- [ ] Production build · development build · TypeScript compilation · ESLint · formatting checks
- [ ] Import & module resolution · invalid imports · missing assets
- [ ] Build warnings · build errors · environment-variable availability
- [ ] Static generation errors · dynamic route generation · server-side rendering · client-side hydration
- [ ] Build reproducibility · determinism · production vs development differences
- [ ] Bundle generation · source-map exposure · build-artifact integrity · build time · resource consumption

## 14. CI/CD Pipeline Audit
- [ ] GitHub Actions configuration · workflow triggers · branch filters · PR checks
- [ ] Stages: lint · typecheck · unit · integration · E2E · build · security scanning · dependency scanning · secret scanning
- [ ] Artifact handling · environment separation · deployment approvals · production deployment restrictions · preview deployment
- [ ] Deployment concurrency · failed-deployment behavior · rollback capability
- [ ] CI secret permissions · third-party Action pinning · workflow permissions · supply-chain security
- [ ] Deployment notifications · CI execution time · CI cost
