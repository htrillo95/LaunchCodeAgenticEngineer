# Agent Context Boundary Policy

## Purpose
This file defines how context boundaries are managed in this project.
At the start of each new phase of work, the agent must follow the
procedure below before taking any action.

## Context Boundary Procedure
At the start of each new phase, before doing any editing or analysis:

1. Restate the current task goal in one sentence.
2. List the rules currently in effect (verbatim, not paraphrased).
3. State explicitly which prior rules are no longer in effect, if any.
4. Identify the specific artifact being worked on in this phase.
5. Then proceed with the requested work.

## Why This Matters
Rules and requirements change during long sessions. This procedure ensures the agent is always operating from the current version of the rules, not a prior version buried in conversation history.

## Compaction Policy

Compaction is a last resort. Proactive summarization (see .claude/skills/summarize-session/SKILL.md) should be triggered before the context window exceeds 60% capacity to avoid relying on compaction.

Observations from testing:
- Compaction reliably preserves: the original task, style guide rules, edited section state, and remaining work in the tested session.
- Compaction may lose or distort: no information was lost or distorted in the four probes during this test, but compaction should not be assumed to preserve every detail in longer sessions.
- Manual compaction should be triggered at: 60% context usage if proactive summarization has not already occurred.
