---
name: up-testcase
description: Generate or update evidence-based Markdown test-case drafts from this repository's configured PRD, selective SRS evidence, images, and fixed templates. Use when the user enters a `start` command with a feature name, asks to generate cases for a configured feature, or requests an update to an existing artifact under `output/`; do not use for developing or reviewing the agent framework itself.
---

# Codex entrypoint

Use the repository root as the working directory.

## Load the workflow

For `start <feature name>`, explicit-path generation, or updates to an existing artifact under `output/`, read `config/testcase-workflow.md` completely before taking any workflow action. Follow it as the single source of truth, including its required guides, feature resolution, input safety, selective-SRS budgets, artifact contract, review pass, and BLOCKED/PARTIAL behavior.

Do not load `.github/agents/testcase.agent.md` as an additional workflow source. It is the Copilot adapter for the same shared file.

## Codex tool adaptation

Adapt only the shared workflow's tool mechanics:

- Use local filesystem listing and search to resolve registry entries, check safe paths, choose versions, and perform bounded SRS discovery.
- Local shell use is allowed only for read-only discovery, bounded text extraction, path checks, and deterministic validation. Do not use it to execute product tests or interact with a real app/device.
- Use patch-based edits for generated Markdown artifacts. Recheck the complete artifact set immediately before writing, and read every saved artifact back.
- Do not browse the web, follow remote document links, call external services, or delegate generation to subagents.
- Image inspection is allowed only for local images referenced or inventoried by the configured PRD workflow. Record unreadable or missing images as limitations.

The SRS search and range-read budgets in the shared workflow apply across all local search/read mechanisms used during the run. Shell commands do not reset or bypass those budgets. If Codex cannot satisfy a required operation safely, follow the shared BLOCKED/PARTIAL behavior instead of inventing a fallback.

If another compatible harness discovers this skill, the shared workflow still applies, but that harness must use its own allowed tools rather than the Codex-specific mechanics above.
