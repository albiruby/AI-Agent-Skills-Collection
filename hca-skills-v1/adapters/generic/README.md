# Generic adapter checklist

This directory defines integration checks rather than executable glue code.

Before claiming a harness is supported, verify:
- Where and how it discovers skill files.
- Whether frontmatter keys and descriptions are accepted.
- Whether specialized skills can be loaded conditionally.
- What tools are actually exposed and how permissions work.
- Whether persistent memory exists, where it is stored, and how writes are confirmed.
- Whether background jobs/heartbeats and subagents exist and are authorized.
- How context compaction or session restarts are handled.
- Whether all critical core rules survive context limits.

Mark each capability as `verified`, `unsupported`, or `not tested`. Never infer compatibility solely from Markdown support.
