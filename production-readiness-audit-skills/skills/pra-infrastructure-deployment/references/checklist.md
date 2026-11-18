# Checklist — Domains 50–56

## 50. Hosting & Infrastructure
- [ ] Provider · plan · runtime environment · Node.js version · build & production environment · serverless config
- [ ] Function limits: execution duration · memory · region · CDN · edge behavior · server runtime
- [ ] Resource, bandwidth, image-optimization, request, storage limits · service quotas · scaling limits
- [ ] Reliability · provider status · provider dependency · infrastructure cost · documentation

## 51. Domain & DNS
- [ ] Ownership · registrar · expiration · auto-renew · registrar MFA · transfer lock
- [ ] DNS provider · nameservers · A · AAAA · CNAME · MX · TXT · SPF · DKIM · DMARC · DNSSEC · propagation · TTL
- [ ] Root domain · `www` · canonical domain · redirect rules · subdomains
- [ ] Unused/orphaned records · takeover risk · email-delivery compatibility · DNS backup/documentation

## 52. SSL & Transport Security
- [ ] Certificate validity · expiration · chain · TLS version · HTTPS redirect · mixed content
- [ ] Renewal · domain & subdomain coverage · HSTS · secure cookies
- [ ] Third-party HTTPS resources · API HTTPS · webhook HTTPS · external endpoint security · certificate monitoring

## 53. Vercel Production Configuration
- [ ] Project & team ownership · GitHub connection · production branch · build/install commands · framework preset · root directory · Node.js version
- [ ] Env vars: build · production · preview · development
- [ ] Custom domains · domain verification · SSL · deployment protection · preview protection
- [ ] Deployment history · rollback · runtime logs · build logs · functions · function regions · function duration
- [ ] CDN · image optimization · cache behavior · firewall/WAF · usage limits · spend management
- [ ] Analytics · Speed Insights · log drains · team access · deployment notifications · production promotion procedure

## 54. Environment Configuration
- [ ] Development · preview · staging (if used) · production configuration
- [ ] Variable inventory · naming · required/optional · public/server-only/secret
- [ ] Missing · invalid · incorrect values · environment-specific values · rotation
- [ ] Fallback values · defaults · configuration validation · documentation · drift · environment isolation

## 55. Deployment Strategy
- [ ] Workflow · preview · production · branch-based deployment · PR workflow · review approvals
- [ ] Build validation · test validation · deployment authorization · concurrency · cancellation · atomic behavior
- [ ] Rollback · release tags · release notes · environment promotion · notifications
- [ ] Post-deployment verification · failed-deployment recovery · hotfix process · emergency rollback process

## 56. Production Configuration & Launch
- [ ] Production: domain · Sanity dataset · API endpoints · env vars · analytics · monitoring · redirects · robots · sitemap · metadata
- [ ] Production: error handling · cache settings · security headers · external integrations · email config · form submission · image delivery
- [ ] Preview isolation · deployment status · ownership
