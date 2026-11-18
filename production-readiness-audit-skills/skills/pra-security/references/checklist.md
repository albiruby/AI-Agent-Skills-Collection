# Checklist — Domains 15–22

## 15. Security Architecture
- [ ] Overall security architecture · trust boundaries (application, client/server) · authentication & authorization architecture (if used)
- [ ] Access control · least privilege · privilege-escalation risks · attack surface · exposed endpoints · public/private resource separation
- [ ] Sensitive-data flow · external service trust · security configuration · secure defaults · fail-safe behavior · defense in depth
- [ ] Security-related technical debt · OWASP Top 10 coverage · OWASP ASVS requirements · threat modeling · abuse-case analysis · assumptions · residual risks

## 16. Secrets & Credential Management
- [ ] Hardcoded secrets · API keys · API/access/refresh tokens · database · CMS · webhook · SMTP · analytics · cloud credentials · private keys · certificates
- [ ] `.env` · `.env.local` · Git-history secrets · GitHub Actions secrets · Vercel env vars · Sanity tokens · third-party credentials
- [ ] Client-side exposure · `NEXT_PUBLIC_` usage · secret scope · access permissions
- [ ] Rotation · revoked credentials · expired credentials · credential reuse · credential documentation · secret scanning
- [ ] Leakage in logs · error messages · source maps · build artifacts

## 17. Authentication & Authorization (only if login/dashboard/admin/protected resources exist)
- [ ] Login · logout · session management · cookie security · password storage · reset · email verification · MFA · account recovery
- [ ] Session expiration · revocation · concurrent sessions · brute-force protection · credential stuffing · account enumeration · auth rate limiting
- [ ] Authorization checks · RBAC · ABAC · resource ownership validation · server-side authorization · API authorization · admin separation
- [ ] Privilege escalation · IDOR · session fixation · CSRF · authentication logs · suspicious-login detection

## 18. Application & API Security
- [ ] Endpoint inventory · authentication · authorization · request/response validation · input sanitization · output encoding
- [ ] HTTP method restrictions · Content-Type validation · request/response size limits · rate limiting · throttling · timeouts · abuse prevention
- [ ] API enumeration · sensitive-information exposure · improper error responses · insecure redirects · SSRF · CORS · CSRF · XSS
- [ ] SQL/NoSQL injection (if DB) · command injection · path traversal · file inclusion · prototype pollution · open redirects · HTTP parameter pollution
- [ ] Broken access control · mass assignment · webhook security · replay attacks · idempotency · API versioning · deprecation · logging · monitoring

## 19. Input Validation & Output Security
- [ ] Form validation (server & client) · schema/type validation · string length · numeric range · date · email · URL
- [ ] File type · size · MIME verification · filename sanitization
- [ ] HTML sanitization · rich-text sanitization · Portable Text rendering · Markdown rendering · HTML escaping · output encoding
- [ ] Query-parameter · route-parameter · search-input validation · external URL restrictions · dangerous URL scheme rejection (`javascript:`, `data:`)
- [ ] SVG security · embedded HTML · `dangerouslySetInnerHTML` · DOM-based/stored/reflected XSS · content injection

## 20. Browser & HTTP Security
- [ ] HTTPS enforcement · TLS configuration · certificate validity · HTTP→HTTPS redirect · HSTS
- [ ] CSP · `frame-ancestors` · `X-Content-Type-Options` · `Referrer-Policy` · `Permissions-Policy` · clickjacking · MIME sniffing
- [ ] Secure cookie flags · SameSite · CORS · cross-origin isolation (if needed) · mixed content
- [ ] Cache-control · sensitive response caching · server-information disclosure · unnecessary HTTP methods · header consistency across routes · CSP violation monitoring

## 21. Infrastructure & Deployment Security
- [ ] Vercel project access · GitHub integration permissions · deployment permissions · production-branch restrictions
- [ ] Preview exposure & protection · production environment isolation · env-var access · build-log & runtime-log exposure
- [ ] Serverless function exposure · API route protection · WAF · DDoS protection · firewall rules · IP restrictions
- [ ] Deployment hooks · webhooks · CI/CD credentials · third-party deployment integrations
- [ ] Domain / DNS / subdomain takeover risks · orphaned DNS records · unused deployment domains
- [ ] Public source maps · debug/development/administrative endpoints · infrastructure configuration drift

## 22. Dependency & Supply-Chain Security
- [ ] Known CVEs (critical/high/moderate/low) · transitive vulnerabilities · malicious packages · typosquatting · dependency confusion
- [ ] Package & lockfile integrity · source verification · provenance
- [ ] GitHub Actions security · third-party workflow permissions · build-time scripts · post-install scripts · untrusted dependencies
- [ ] License risks · unsupported dependencies · update strategy · remediation plan · SBOM if needed
