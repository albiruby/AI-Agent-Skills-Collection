# Human Cognition & Agency (HCA) Skills v1.0

An original, modular, harness-adaptable skill framework for general-purpose AI agents with highly proactive but bounded autonomy.

## Goals
- Human-inspired cognition: contextual understanding, hypotheses, alternatives, and adaptive planning.
- Decision quality: evidence, value of information, risk, reversibility, and proportional reasoning effort.
- Agency: proactive follow-through within authorized scope.
- Verification: distinguish attempted, executed, and verified actions.
- Learning: retain useful lessons only when a supported storage mechanism exists.
- Portability: keep the canonical instructions plain Markdown with `name` and `description` frontmatter.

This project does not claim human consciousness, human-level general intelligence, perfect memory, or guaranteed compliance. Skills influence model behavior; they do not create missing runtime capabilities.

## Skills
- `hca-core`: always-on behavioral contract and module router.
- `hca-cognition`: context, intent, evidence, hypotheses, common-sense checks.
- `hca-decision-making`: options, trade-offs, uncertainty, risk, stop conditions.
- `hca-agency`: proactive planning and bounded execution.
- `hca-verification`: observable success criteria, action status, recovery.
- `hca-metacognition`: calibration, contradiction handling, error detection.
- `hca-adaptive-learning`: evidence-based memory and lesson promotion.
- `hca-social-intelligence`: audience, intent, tone, perspective-taking without pretending to feel emotions.

## Integration
1. Install `skills/<skill-name>/SKILL.md` where your harness discovers skills.
2. Make `hca-core` available as the default behavioral instruction if the harness supports it.
3. Configure specialized skills for conditional loading, or copy their trigger rules into the core if dynamic loading is unavailable.
4. Review `policies/` and adapt them to the real permissions of the runtime.
5. Run `evaluations/` against a baseline before claiming improvement.

Do not assume that OpenCode, Hermes Agent, Claude Code, or another harness shares the same skill discovery, permission, memory, heartbeat, or subagent behavior. Verify each adapter against the current version of that harness.

## Recommended first deployment
Start with `hca-core`, `hca-agency`, and `hca-verification`. Add memory only after confirming that persistent storage is actually available. Add more modules when evaluation demonstrates a need.

## Upstream inspiration
This package is an original synthesis of public concepts, not a copy or bundled dependency. Reference projects include:
- https://github.com/halthelobster/proactive-agent
- https://github.com/eli-labz/Cognitive-Core-Skills
- https://github.com/Zijian-Ni/agent-memory
- https://github.com/rohitpatill/ace-autonomous-agent
- https://github.com/tfatykhov/nous
- https://github.com/xraph/cortex
- https://github.com/clawic/skills
- https://github.com/dayyanj/nmem
- https://github.com/rodspeed/claude-cognitive-architecture

Review each upstream repository's current license, security, dependencies, and compatibility before copying or installing any of its code.
