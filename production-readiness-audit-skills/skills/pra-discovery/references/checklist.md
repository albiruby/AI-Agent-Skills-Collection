# Checklist — Domains 1–4

## 1. Project Discovery & Environment Assessment
- [ ] **Identity**: application type & website purpose · framework, library, runtime · Next.js/React/TypeScript/Node versions · package manager
- [ ] **Structure**: repository structure · all main folders/files · application entry points · App Router vs Pages Router · all routes · dynamic routes · route handlers & API endpoints · Server vs Client Components · server-side vs client-side execution
- [ ] **Data & services**: CMS & external data sources · all third-party integrations · environment variables · database/storage · authentication & authorization · analytics & monitoring tools
- [ ] **Delivery**: deployment platform · hosting & infrastructure · build/test/lint/deploy scripts · CI/CD workflows · dev/preview/staging/production environments
- [ ] **State of work**: project documentation · features done/unfinished/experimental · unused features · technical debt · external-service dependencies · plan/package limits of services used

## 2. Project Scope & Requirements Validation
- [ ] Implementation matches project brief · functional requirements met · non-functional requirements met
- [ ] All planned pages exist · every feature has a clear purpose · all user flows completable
- [ ] Features not connected to backend/CMS · placeholders remaining · mock data remaining · features working only in development
- [ ] Features not matching business need · undocumented scope changes · conflicting requirements · requirements without acceptance criteria
- [ ] Unmet operational needs · unnecessary dependencies/features

## 3. Project Documentation & Knowledge Audit
Files to look for: README · ARCHITECTURE · PROJECT-BRIEF · REQUIREMENTS · SITEMAP · USER-FLOWS · PAGE-SPECS · DESIGN-SYSTEM · CMS-SCHEMA · DATA-MODEL · API-DOCUMENTATION · ENVIRONMENT · DEPLOYMENT · SECURITY · MONITORING · BACKUP-RECOVERY · MAINTENANCE · INCIDENT-RESPONSE · QA-CHECKLIST · CHANGELOG
- [ ] Docs still match implementation · no obsolete instructions · env vars documented
- [ ] Dev setup reproducible · deployment doable by another developer · architecture understandable
- [ ] Third-party services documented · troubleshooting procedures · rollback & recovery procedures · ownership & responsibilities clear

## 4. Repository & Git Audit
- [ ] **Config**: Git configuration · default branch · production branch · development branch (if used) · branch naming · versioning strategy · release tags
- [ ] **History**: commit history · commit message quality · rollback commit availability · repository backup strategy
- [ ] **Working tree**: uncommitted changes · untracked files · unnecessary files · large files · binary files · generated build artifacts · merge-conflict markers
- [ ] **Ignore/attributes**: `.gitignore` · `.gitattributes` · Git LFS if needed · lockfile consistency
- [ ] **Secrets & exposure**: accidentally committed credentials · committed `.env` files · exposed internal documentation
- [ ] **Governance**: repository access permissions · branch protection · required PR reviews · required status checks · force-push restrictions
