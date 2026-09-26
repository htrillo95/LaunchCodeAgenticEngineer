# Iteration Log

## Run — storage grant/denial verification

- Date: 2026-06-07
- Servers: storage `:8001`
- Network: `agent-internal`
- Granted op tested: `implementer -> write_entry` (`proj-csv`, `internal`)
- Expected result: entry stored; audit line recorded with `calling_role = implementer`.
- Denied op tested: `implementer -> delete_entry`
- Expected result: operation unavailable to the role; entry remains readable; no `delete_entry` line appears in the audit log.
- Status: ready to verify in the course harness.

## Run — end-to-end integration (storage + retrieval live)

- Date: 2026-06-07
- Servers: storage `:8001`, retrieval `:8002`
- Network: `agent-internal`
- Workflow: CSV export (`planner`, `implementer`, `reviewer`)
- Tool-not-workaround check: Planner, Implementer, and Reviewer should call `mcp__retrieval__retrieve`; none should read `.memory/reference/` directly.
- Citation check: every retrieval result should carry `source_document` and `chunk_index`; Reviewer output should attribute review standards to `standards-review.md`.
- Ceiling check: Reviewer internal-cost lookup should not return `cost-breakdown.md`.
- Audit check: `write_entry` records should exist for Planner, Implementer, and Reviewer with `calling_role` populated.
- Status: ready to verify in the course harness.

## Run 0 — Tool-scope verification (pre-run check)

- Date: 2026-09-22
- Role tested: implementer
- Tool attempted: `mcp__coursetools__task_tracker`
- Expected: denied (`task_tracker` is owned by project-manager)
- Result: denied at the harness allow-list layer. The tool was not exposed in the implementer subagent's tool set, so the implementer could not invoke it.
- Conclusion: the denial is enforced, not merely declared. The implementer's explicit tool allow-list prevents access to `task_tracker`.

## Run 1 — 2026-09-26

### Misfire 1: Project Manager invoked without a ticket ID
- What happened: the Project Manager was invoked to close the CSV-export ticket, but no ticket ID had been created or included in its handoff. The workflow stalled and required human intervention to create a new ticket before the Project Manager could complete its task.
- Roles involved: Orchestrator and Project Manager.
- Cause: the orchestration workflow assumed an existing ticket ID but did not require one in the Project Manager handoff or define what to do when no ticket exists.
- Proposed fix: update the Orchestrator workflow instructions so that before invoking the Project Manager it must either provide an existing ticket ID or explicitly instruct the Project Manager to create a ticket first.

### Observation: Tester could not execute the real test file
- What happened: the Tester correctly used its scoped test_runner tool, but the supplied course test_runner returned a stubbed PASS result instead of actually executing example-task-app/test.js.
- Roles involved: Tester.
- Cause: the supplied course test_runner is a simulated tool rather than a real Node test executor.
- Outcome: the Tester correctly refused to claim live execution and escalated. Static verification was accepted at the human checkpoint.
- Proposed fix: in an environment with a real test runner, wire test_runner to execute the requested test command. No additional Tester permissions should be granted as a workaround.

### Rerun — Project Manager handoff verification — 2026-09-26
- Fix applied: updated the Orchestrator workflow in CLAUDE.md to require an existing ticket ID or explicit instructions to create a ticket before invoking the Project Manager.
- Result: the Orchestrator correctly generated a handoff instructing the Project Manager to create a new ticket first when no ticket ID exists.
- No Project Manager or task-tracker invocation was required for this verification.
- Conclusion: fix holds.
