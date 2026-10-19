# AI Agent Skills Collection

A collection of platform-agnostic `SKILL.md` packs for AI assistants and coding agents. Each pack is self-contained: drop a skill folder into your agent's skills directory and it works with Claude, ChatGPT, Gemini, OpenCode, or any harness that reads Markdown instructions.

## Packs

| Pack | Contents | Use it for |
|---|---|---|
| [`web-app-dev-skills`](web-app-dev-skills/README.md) | 22 skills | PRDs, architecture, database schemas, API contracts, implementation planning, testing, security, DevOps |
| [`game-dev-skills`](game-dev-skills/README.md) | 23 skills | Full game lifecycle: concept, GDD, engine choice, mechanics, art, audio, networking, QA, launch |
| [`gemini-image-consistency-skills`](gemini-image-consistency-skills/README.md) | 18 skills + plug-and-play kits | Keeping Gemini image output consistent: locked style, theme, palette, characters, assets |
| [`hca-skills-v1`](hca-skills-v1/README.md) | 8 skills + policies + evals | Human-inspired cognition and bounded proactive agency for general-purpose agents |
| [`garmin-dev-skill`](garmin-dev-skill/SKILL.md) | 1 skill | Garmin Connect IQ apps, watch faces, widgets, and data fields in Monkey C |

## Layout

```
.
├── web-app-dev-skills/
│   ├── skills/<skill-name>/SKILL.md
│   └── templates/
├── game-dev-skills/
│   └── <NN>-<skill-name>/SKILL.md
├── gemini-image-consistency-skills/
│   ├── skills/<skill-name>/SKILL.md
│   ├── plug-and-play/
│   └── templates/
├── hca-skills-v1/
│   ├── skills/<skill-name>/SKILL.md
│   ├── policies/
│   ├── adapters/
│   └── evaluations/
└── garmin-dev-skill/
    └── SKILL.md
```

## Installing

Copy the individual skill folders into the directory your harness scans for skills, for example:

- OpenCode: `~/.config/opencode/skills/`
- Claude Code: `~/.claude/skills/`
- Generic: any folder your agent loads `SKILL.md` files from

Copy only the skills you need. Loading an entire pack wastes context.

## Conventions

Every skill starts with YAML frontmatter:

```yaml
---
name: skill-name
description: When to use this skill and what it does.
---
```

The body defines a role, principles, a step-by-step workflow, and a required output structure. Skills keep facts, assumptions, recommendations, and open questions separate, and never claim something was run or verified unless it was.

## License

MIT — see [LICENSE](LICENSE).
