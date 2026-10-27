# V1.4: Detailed, objective-specific Preconditions

## What changed
Same single agent and `start <feature name>`. No input redesign. Preconditions now describe relevant feature applicability, UP Content installation state, ThinQ App requirements and initial appliance state in concise test-execution language. The four setup groups remain the planning checklist, but generated prose should prefer natural labels such as Appliance, ThinQ App, Feature setting and Appliance state. Tested actions stay in Steps. Negative cases keep OFF/uninstalled conditions. Unknown setup becomes TBD with explicit readiness gaps in Notes/companions instead of repetitive analysis prose in every Preconditions cell.

## Upgrade existing workspace
1. Backup/commit your current working agent and input reader.
2. Because your input reader has local improvements, MERGE the V1.4 block from `.github/agents/testcase.agent.md` instead of replacing the entire file blindly.
3. Add `config/preconditions-standard.md`.
4. Merge V1.4 additions into `config/quality-workflow.md`, `config/prd-reading-guide.md`, `templates/analysis-template.md` and `templates/review-template.md`.
5. Keep your real PRD, SRS, registry, image handling and fixed test case template unchanged. No new columns are required.
6. Start a fresh Copilot chat, choose UP Testcase and run `start <feature name>`. Existing cases are not automatically migrated: request an explicit update to the relevant file if desired.

Optional update prompt:
```text
Update Preconditions in output/<feature>/test-cases-v001.md using the V1.4 standard.
Preserve case IDs, Steps and Expected Result unless a setup/action contradiction requires a source-supported correction. Report any such correction.
Use the existing PRD and relevant sources; keep selective SRS retrieval.
Expand app configuration and content installation prerequisites only from evidence.
Do not invent missing setup; record gaps and update analysis/review companions.
Do not modify input documents or the fixed template.
```

## Acceptance scenarios: live NOT RUN
- Alert behavior: documented install/configuration setup detailed in Preconditions.
- Feature applicability: appliance support appears first; app-dependent cases state that the app is installed and supports the feature.
- Natural wording: no repeated `applicable device; exact model TBD` or `preparation confirmation TBD` boilerplate.
- Install case: initial state not installed; install action only in Steps.
- Setting-change case: initial value in Preconditions, change in Steps.
- OFF/uninstalled case: no accidental enabling/installing.
- Missing menu/confirmation: explicit TBD and SETUP CLARIFICATION REQUIRED.
- Image shows destination only: no invented intermediate path or Save button.
- Different model/app labels: preserve applicable variant and source labels.
- Update: unaffected IDs/content preserved; relevant companions updated.
- Fixed template: same columns; use existing Notes/companion for readiness.

## Limitations
Instruction-based behavior, not a hard enforcement engine. Unit/static checks do not prove Copilot follows the instructions or that cases are correct. No actual app/device execution, no new image/OCR capabilities, no automatic base64 extraction. Additional setup evidence may require more context; existing SRS budgets remain. Developer/QE review is required.
