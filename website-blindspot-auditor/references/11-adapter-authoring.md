# Technology Adapter Authoring Guide

## 1. Purpose

Adapters add focused knowledge for a technology or integration without making the universal skill dependent on that technology. The core must still work when no adapter exists.

## 2. When to create an adapter

Create one when repeated audits show that technology-specific behavior, configuration, or failure modes cannot be adequately covered by generic methods. Do not create an adapter merely to list framework best practices.

## 3. Adapter template

Use this structure:

```markdown
# Adapter: [Technology / Integration]

## Purpose
What role this technology typically plays and what this adapter helps inspect.

## Detection signals
Reliable repository/configuration/runtime signals. Include false-positive caveats.

## Applicability
When to load this adapter and when not to.

## Boundaries and data flows
Important inputs, outputs, trust boundaries, state, and dependencies.

## Audit procedures
Concrete questions and inspection steps, grouped by risk.

## Verification methods
Safe methods and tools that may be available. Never assume a particular tool exists.

## Common failure modes
Technology-specific edge cases and operational concerns.

## Evidence requirements
What is sufficient to claim a finding and what remains a hypothesis.

## Safety constraints
Actions that require authorization or must not be performed.

## Related modules
Other capabilities, profiles, or adapters that may interact.
```

## 4. Design rules

- Keep the adapter narrowly scoped and evidence-oriented.
- Avoid duplicating universal domain guidance; link back to it conceptually.
- Distinguish behavior guaranteed by the technology from behavior dependent on configuration/version.
- Record version caveats when known. Do not invent version-specific behavior.
- Prefer observable tests over assumptions based on common defaults.
- Cover integration boundaries, not just isolated configuration.
- Include false positives and conditions where a check is irrelevant.
- Avoid destructive examples.

## 5. Unknown and unsupported technology

Do not stop the audit. Use generic methods: identify the component role, inspect its inputs/outputs, contracts, permissions, state, data flow, error handling, dependency boundaries, and observable behavior. Mark specialized details unknown and report the limitation.

## 6. Profile versus adapter

A **profile** describes product/business workflows (for example, booking or SaaS). An **adapter** describes implementation-specific behavior (for example, a database, identity provider, CMS, or hosting platform). A single audit can load multiple profiles and adapters.

## 7. Where adapters live

Shipped adapters are in `adapters/`; start with `adapters/README.md` for detection signals and selection. When adding a new adapter, place it in that folder and update the index. Keep the structure in section 3 and link related domain briefs instead of duplicating them.

Adapters must be evidence-oriented. A framework pattern is a lead; a finding requires reachability, impact, and sufficient evidence.
