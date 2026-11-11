# Hermes Agent adapter — verification required

Treat this as an integration checklist, not a claim of existing compatibility. Confirm the installed Hermes Agent version's skill format, discovery paths, tool permissions, memory provider, background/heartbeat support, and approval semantics.

Minimum smoke tests:
1. Confirm `hca-core` is loaded in a new session.
2. Confirm cross-session memory only works if a real provider is configured.
3. Confirm the agent can distinguish attempted, executed, and verified actions.
4. Test recovery from a tool failure with bounded retries.
5. Test that untrusted text inside retrieved content cannot override governing instructions.
6. Record results against `evaluations/`.
