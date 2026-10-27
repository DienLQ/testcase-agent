# V1.5: Codex compatibility

## What changed

- Added `config/testcase-workflow.md` as the single behavioral and design source for both clients.
- Converted `.github/agents/testcase.agent.md` into a thin Copilot adapter that loads the shared workflow.
- Added root `AGENTS.md` and the repo-local `$up-testcase` skill as the Codex adapter.
- Added Codex-specific tool adaptation without enabling web access, external services, delegation, or real product execution.
- Corrected the configured structured PRD path and the validator filename.
- Made static tests explicit about UTF-8 and line-ending portability on Windows.

## Upgrade an existing workspace

1. Preserve the existing PRD, SRS, images, registry entries, and team template.
2. Move the detailed workflow into `config/testcase-workflow.md` and replace the Copilot agent body with the thin adapter supplied in this version.
3. Add `AGENTS.md` and `.agents/skills/up-testcase/`; both adapters must reference the same shared workflow path.
4. Merge the V1.5 README and acceptance-test additions.
5. Verify every `prd_json` and `supporting_inputs[].path` value points to the actual local file.
6. Keep `scripts/validate_output.py` as the documented validator name.
7. Run the static suite with UTF-8 mode, then run Copilot and Codex live acceptance separately.

## Invocation

Codex automatically reads the applicable `AGENTS.md`. For generation, use either:

```text
start <feature name>
```

or explicitly:

```text
Use $up-testcase to run start <feature name>.
```

The command is a chat instruction, not a shell command. In Copilot, select the `UP Testcase` custom agent and use the same `start <feature name>` input. Both clients then load `config/testcase-workflow.md`.

## Limitations

Static tests cannot prove that a model follows the workflow. Codex and Copilot have different tool harnesses, so both live acceptance sets remain required. Missing SRS context, unreadable images, conflicts, and setup gaps must still be reported as PARTIAL/TBD rather than inferred.
