# V1.6: Two-question Preconditions

## Contract
The Preconditions column contains exactly two lines:

1. `UP Content installation on ThinQ App: Required | Not required | TBD`
2. `Device firmware supporting the UP Content: Required | Not required | TBD`

Use one value per line. The values must be derived from PRD, selective SRS, accepted structured/image evidence, or explicit user requirements. Silence never proves `Not required`.

## Migration
1. MERGE the V1.6 block in `config/testcase-workflow.md`.
2. Replace the prior Preconditions guide with `config/preconditions-standard.md`.
3. Merge companion-template and quality/PRD-reading guide changes.
4. Keep the fixed test-case columns unchanged.
5. For existing artifacts, move setting/course/device-state preparation from Preconditions to the start of Steps and update analysis/review companions.

## Live acceptance
- Behavior case whose source identifies an installed UP Content: installation Required.
- Installation case: installation Not required before the case; install action remains in Steps.
- Device-side UP Content behavior: supported firmware Required even if the exact build is unknown.
- Pure app-only case with explicit independence from device firmware: firmware Not required.
- Missing or conflicting evidence: TBD and SETUP CLARIFICATION REQUIRED.
- Preconditions contains no third line or explanation.

Static checks do not prove live Codex/Copilot compliance or product correctness. Developer/QE review remains required.
