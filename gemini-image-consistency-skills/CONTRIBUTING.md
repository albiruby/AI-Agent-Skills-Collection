# Contributing

Thanks for improving Image Consistency Skills.

## Adding or changing a skill
1. Copy `_template/SKILL.md` to `skills/<kebab-case-name>/SKILL.md`.
2. Frontmatter needs `name` (matches the folder) and `description` (what it does + when to use it, with trigger phrases).
3. Keep the body under about 150 lines; move long material to `references/` inside the skill folder and point to it.
4. Use the standard sections: Purpose, When to use, Process, Output format, Rules, Pitfalls.
5. Keep skills Gemini-specific but explicit about what is volatile: put model names, limits and surface details in the "Gemini notes" section or in `gemini-image-prompting`, and mark them "verify in current docs".
6. Add the skill to the README table and CHANGELOG.

## Style rules
- English, plain sentences, imperative mood.
- No copyrighted characters, living artists' names or real people in examples.
- Examples must be original.

## Testing a skill
Run 3 prompts that should trigger it and 2 that should not. Check that outputs follow the Output format and that locks are copied verbatim.

## Pull requests
One topic per PR; describe the problem, the change and the test you ran.
