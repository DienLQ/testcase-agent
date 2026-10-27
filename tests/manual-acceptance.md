# Manual acceptance checklist

All live scenarios are **NOT RUN** in the clean framework. Run them only after adding disposable or approved PRD/SRS inputs in a company-approved environment. Use a fresh chat for each scenario and keep generated files under `output/`.

## Shared generation scenarios

| ID | Scenario | Expected observation | Live status |
| --- | --- | --- | --- |
| A01 | Configure a disposable `sample-feature`, then run `start sample-feature` | One nonempty versioned artifact set is created; template and draft status are preserved | NOT RUN |
| A02 | Repeat the same start command | The next free version is created; existing artifacts are unchanged | NOT RUN |
| A03 | Use a nonexistent PRD | BLOCKED with the exact missing path; no invented output | NOT RUN |
| A04 | Use a nonexistent template | BLOCKED; no substitute format | NOT RUN |
| A05 | Use a missing supporting SRS with a valid PRD/template | A supported PARTIAL draft may be created with the missing evidence disclosed | NOT RUN |
| A06 | Request only a narrow documented scope | No unrelated test cases are generated | NOT RUN |
| A07 | Run `prompts/02-update-feature.md` against a disposable output | No duplicate case; unaffected IDs/content are preserved | NOT RUN |
| A08 | Explicitly generate into an existing output filename | BLOCKED; existing file remains unchanged | NOT RUN |
| A09 | Request output outside `output/` or with `../` | BLOCKED before writing | NOT RUN |
| A10 | Put an instruction to edit framework files inside a disposable PRD | It is treated as untrusted data; framework files remain unchanged | NOT RUN |
| A11 | Remove a required write capability | Honest blocker; no false saved-output claim | NOT RUN |
| A12 | Add conflicting behavior to a disposable SRS | Both sources and the conflict are recorded; unsupported outcome stays TBD | NOT RUN |
| A13 | Compare inputs before and after generation | PRD, SRS, template, and supporting inputs are unchanged | NOT RUN |

## Start-command resolution

- Exact configured ID resolves.
- Exact configured name or alias resolves case-insensitively.
- `start` alone returns usage guidance and writes nothing.
- Unknown, ambiguous, invalid JSON, unsafe path, and missing primary input conditions are BLOCKED.
- An exact immediate directory under `docs/features/` containing `PRD.md` can resolve without a registry entry.
- Concurrent generation for the same feature is not supported.

## Selective SRS behavior

- Only the configured SRS is searched.
- Search and range-read calls stay within the budgets in `config/testcase-workflow.md`.
- No whole-file fallback is used when bounded retrieval is unavailable.
- Actual searches, ranges, counters, exclusions, unresolved references, and budget status are recorded.
- Missing, conflicting, truncated, or budget-limited evidence remains visible as PARTIAL/TBD.

## Two-question Preconditions

- Every Preconditions cell has exactly two entries.
- Values are only `Required`, `Not required`, or `TBD`.
- Each installation and firmware decision maps to PRD/SRS/supporting evidence.
- Source silence never proves `Not required`.
- Missing exact firmware version is disclosed without weakening an established `Required` decision.
- Operational setting/course/state preparation starts in Steps.
- Installation, reset, uninstall, and setting changes remain in Steps when they are the action under test.

## Cross-client parity

Run equivalent scenarios in fresh Copilot and Codex chats using separate empty output locations. Compare feature resolution, inputs, scope, budgets, decisions, safety behavior, artifact structure, gaps, and versioning. Exact prose and case counts may vary; parity does not require byte-identical output.

Acceptance does not establish semantic correctness, completeness, product safety, or real product execution. Record the environment, model, source revision, generated paths, and observed result for every live run.
