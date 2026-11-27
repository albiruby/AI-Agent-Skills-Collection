# Reference: Professional Documentation Principles

## Purpose-first documentation

Every document should answer a real reader question. Before writing, define the audience, task, and expected outcome. Avoid documentation that exists only to make a repository look larger.

## Single source of truth

Assign each technical fact to an authoritative location. Link to it from other documents rather than copying large sections. When duplication is unavoidable, identify which source controls updates.

## Evidence and status labels

Use precise status language:

- **Implemented:** confirmed in the current code or observed application.
- **Partially implemented:** some behavior exists but important parts are missing or constrained.
- **Planned:** intended future work, not currently available.
- **Deprecated:** still present but no longer recommended or supported.
- **Unverified:** evidence is insufficient.

Do not use “supported” merely because a dependency or configuration entry exists.

## Reader-centered structure

A useful order often is:

1. What this project is.
2. Who it is for and what it does.
3. Requirements and supported environment.
4. Quick start.
5. Common workflows.
6. Deeper technical details.
7. Testing, troubleshooting, and contribution information.

Adapt this order to the document and audience.

## Maintainability

Prefer concise documents with stable links. Include update triggers for facts that change often, such as supported platforms, install commands, configuration variables, external APIs, and store requirements. Keep release-specific information out of evergreen setup guides unless needed.

## Examples and commands

Examples should be copyable and consistent with the actual project. Use placeholder values for secrets, and identify placeholders clearly. Do not include real tokens, private endpoints, or personal data.

## Diagrams

Use a diagram when it clarifies component relationships, data flow, sequence, state transitions, or deployment topology. Keep diagrams tied to the implementation and label proposed architecture as proposed. Provide editable source when available and useful.

## Documentation maturity

- Small prototype: README, setup/run instructions, important limitations.
- Maintained application: README, user/developer guides, architecture and testing documentation as needed.
- Public API/SDK: reference documentation, examples, versioning and compatibility details.
- Production service: operational, deployment, security, observability, recovery, and release documentation where verified.

This is guidance, not a mandatory file checklist.
