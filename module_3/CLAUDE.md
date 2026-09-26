# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is a Docker-based development environment for LaunchCode's **Agentic Programming** course, Module 3. 

## MCP Servers

Two MCP servers are pre-installed and configured in `/root/.claude/settings.json`:

### Slack
- Package: `@modelcontextprotocol/server-slack`
- Requires env vars: `SLACK_BOT_TOKEN`, `SLACK_TEAM_ID`
- Allows Claude Code prompts to read channels, post messages, and interact with Slack workspaces.

### Gmail
- Package: `@gongrzhe/server-gmail-autoauth-mcp`
- OAuth credentials stored in `/root/.gmail-mcp/` (persist this directory across container runs if needed)
- Allows Claude Code prompts to read, search, and send Gmail messages.

## Skills

Pre-configured skills (invoked with `/skill-name` in Claude Code):

| Skill | Description |
|---|---|
| `/send-slack-message` | Send a message to a Slack channel |
| `/check-gmail` | Summarize recent unread Gmail messages |
| `/send-email` | Draft and send an email via Gmail |
| `/summarize-session` | Bullet-point summary of the current session |

Skills are defined in `settings.json` which is copied to `/root/.claude/settings.json` during image build.

## Agents

Pre-configured sub-agents available inside Claude Code sessions. Agents are autonomous specialists that Claude Code can invoke automatically or that you can request explicitly.

| Agent | Description |
|---|---|
| `code-reviewer` | Reviews recent git changes for quality, security, and maintainability |
| `email-summarize` | Checks new Gmail messages and posts sender + 2-line summary to #test Slack channel |

Agents are defined as Markdown files with YAML frontmatter in `/root/.claude/agents/` inside the container. Source files live in the `agents/` directory of this repo and are copied in at build time.

**Running an agent:**

Ask Claude Code to use the agent explicitly:
```
Review my recent changes using the code-reviewer agent.
```

Or Claude Code may invoke it automatically when the task matches the agent's description.

## Running Streamlit Apps

From inside the container:
```bash
streamlit run app.py
```

Access at `http://localhost:8501`.

## Key Dependencies (requirements.txt)

- `anthropic` — Claude API client
- `streamlit` — web UI framework
- `python-dotenv` — environment variable management
- `slack_sdk` — Slack integration (Python)
- `google-api-python-client`, `google-auth-oauthlib` — Gmail/Google API access (Python)
- `fastapi`, `flask`, `uvicorn` — web frameworks
- `pydantic`, `httpx` — HTTP and data validation

## Environment & Tools in the Container

- Python 3.12 (aliased as `python` and `pip`)
- Claude Code CLI (`claude`) installed globally via npm
- OpenCode (`opencode-ai`) installed globally via npm
- MCP server: `@modelcontextprotocol/server-slack`
- MCP server: `@gongrzhe/server-gmail-autoauth-mcp`
- ngrok for tunneling
- Workspace mounted at `/workspace`

## Gmail API Setup

Place `credentials.json` (from Google Cloud Console) in your workspace directory. On first run it triggers OAuth and saves `token.json`. Both files should be in `.gitignore`.

## Orchestrator workflow instructions

The main Claude Code session acts as the Orchestrator. It coordinates the workflow but does not perform the specialized work assigned to subagents.

### Workflow goal and acceptance criteria

Goal: coordinate the Module 3 multi-agent workflow using scoped subagents and structured handoffs.

The workflow is complete only when:
- the requested work satisfies the applicable PRD or task requirements,
- the Reviewer reports no unresolved high-severity issues,
- the Tester reports all required tests passing, and
- any required human approvals have been received.

### Standard sequence

Invoke roles in this order:

1. planner — receives the task request and relevant repository context
2. implementer — receives the approved plan and relevant file list
3. reviewer — receives the modified files and implementation result
4. tester — receives the modified files and test requirements
5. project-manager — receives the assembled run summary and an existing ticket ID; if no ticket exists, the handoff must explicitly instruct the project-manager to create one before updating it

The Orchestrator coordinates these roles and should not perform their specialized work itself.

### Evaluation gate

After each subagent returns, evaluate its output against that phase's acceptance criteria before continuing.

Only pass an output to the next phase when it satisfies the gate. If it does not, follow the branching rules below.

### Branching logic

- Loop: if the Reviewer reports more than three issues, return the review report to the Implementer, then run the Reviewer again.
- Loop: if the Tester reports any failing test, return the failures to the Implementer, then run the Tester again.
- Skip: if the Planner determines that no code change is required, skip the Implementer and continue to the Reviewer.
- Halt and escalate: if the same phase fails its evaluation gate twice in a row, stop and ask the human how to proceed.

### Human-in-the-loop checkpoints

- After the Planner returns, show the plan to the human and obtain approval before implementation begins.
- Before the Project Manager performs any consequential outward-facing update, obtain human confirmation.

### Handoff rules

Use the structured handoff templates in `.memory/knowledge/` when sending work to a subagent and when receiving results.

Each handoff must identify the role, task, relevant inputs, constraints, acceptance criteria, and required output format. Subagents should report unresolved questions or blockers rather than guessing.
