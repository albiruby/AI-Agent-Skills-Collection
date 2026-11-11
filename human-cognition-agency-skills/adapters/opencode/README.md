# OpenCode adapter — verification required

Do not assume paths or loading semantics remain stable across OpenCode versions. Check the documentation for the exact installed version and test skill discovery, project/global scope, tool permissions, context behavior, and any memory integration.

Minimum smoke tests:
1. Confirm `hca-core` is included in the agent's active instructions.
2. Confirm a specialized skill can be found or its rules are available through the core.
3. Confirm the agent does not claim shell/file access when unavailable.
4. Test approval behavior for a destructive operation in a safe fixture.
5. Run the evaluation suite and record model/version/configuration.
