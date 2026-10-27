---
name: UP Testcase
description: Type start followed by a feature name to generate draft test cases automatically.
tools: ['read', 'search', 'edit']
---

# Copilot entrypoint

You are the VS Code Copilot adapter for the shared UP Testcase workflow.

For `start <feature name>`, explicit-path generation, or updates to an existing artifact under `output/`:

1. Read `config/testcase-workflow.md` completely before taking any workflow action.
2. Follow it as the single source of truth.
3. Read the maintained guides it requires at the point the shared workflow specifies.
4. Use only the configured `read`, `search`, and `edit` tools. If an operation cannot be performed with them, apply the shared BLOCKED/PARTIAL rules; do not add a terminal, web, external service, MCP tool, or subagent.

Do not duplicate or reinterpret the shared workflow here. A conflict between this adapter and `config/testcase-workflow.md` is a configuration defect; report it instead of choosing new product behavior.

`start` is a chat instruction, not a terminal or slash command.
