# Context Drift Iteration Log

## Baseline Run

- Session: Fresh Claude Code session
- Messages completed: 8/8
- Context usage at end: 5%
- Approximate half-full point: Not reached
- Drift observed: No significant context drift observed

### Rubric Scores

- Rule Accuracy: 4/4
- Task Adherence: 4/4
- Coherence: 4/4
- Total: 12/12

### Observations

Claude consistently followed the active style guide throughout all eight messages. It correctly applied the updated rules introduced during Message 4 and later updated earlier sections to match those rules. During the final consistency pass, it identified and corrected two formatting inconsistencies rather than losing track of the current requirements.

Because the context window only reached about 5%, the session did not create enough context pressure to produce noticeable drift. This baseline therefore represents a successful no-drift run.

## Context Boundaries Run

- Session: Fresh Claude Code session with CLAUDE.md context boundary policy
- Messages completed: 8/8
- Context usage at end: 6%
- Drift observed: No significant context drift observed

### Rubric Scores

- Rule Accuracy: 4/4
- Task Adherence: 4/4
- Coherence: 4/4
- Total: 12/12

### Observations

Claude correctly tracked the rule changes introduced during Message 4. It replaced the 25-word sentence limit with the 35-word limit, removed the "In short:" requirement, and applied the new opening-question rule.

When revisiting the Introduction and Authentication sections, Claude removed the old summary sentences and updated both sections to the current rules.

During the final consistency pass, Claude identified missed first-use bolding in Making Requests, Error Handling, and Best Practices and corrected those issues. The superseded rules did not reappear.

### Baseline Comparison

- Unmanaged baseline: 12/12
- Context boundaries run: 12/12
- Baseline context usage: 5%
- Context boundaries context usage: 6%

Both runs achieved the same rubric score and showed no significant context drift. The context-boundary run demonstrated that explicit phase preambles kept the current rule set clear when requirements changed, although the baseline run was already successful.

## Summarization Run

- Session: Fresh Claude Code session continued from verified /summarize-session output
- Messages completed: 8/8
- Context usage at end: 6%
- Summary verification: One incomplete remaining-work description was reviewed; no unsupported future scope was added
- Drift observed: No significant context drift observed

### Rubric Scores

- Rule Accuracy: 4/4
- Task Adherence: 4/4
- Coherence: 4/4
- Total: 12/12

### Observations

Claude correctly distinguished the original rules from the updated rules after the fresh start. It carried the verified summary forward, applied the 35-word limit, removed the old "In short:" requirement, and applied the new opening-question rule.

The summary did not introduce an error that affected downstream output. During verification, Claude correctly flagged unsupported future work rather than adding information that had not yet been introduced.

During the final consistency pass, Claude identified and corrected first-use bolding violations. The summarization run therefore completed successfully with no significant context drift.

### Run Comparison

- Unmanaged baseline: 12/12
- Context boundaries run: 12/12
- Summarization run: 12/12
- Baseline context usage: 5%
- Context boundaries context usage: 6%
- Summarization fresh-session context usage: 6%

All three approaches achieved the same rubric score. The summarization run showed that a verified summary could carry the task state into a fresh session while preserving the current requirements.
