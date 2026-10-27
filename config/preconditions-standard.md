# Preconditions decision standard V1.6

## Objective
The Preconditions column answers exactly two source-based questions for each test case:
1. Must the UP Content feature already be installed through ThinQ App before this case starts?
2. Must the device use firmware that supports this UP Content before this case starts?

Do not place feature settings, navigation, course, power, phase, lock, error, account, connectivity, model, or other setup details in Preconditions. Put supported setup actions at the beginning of Steps. Put evidence, unresolved versions/procedures, and gap IDs in Notes and the analysis companion. Do not change the fixed test-case columns.

## Exact rendering contract
Every Preconditions cell contains exactly these two lines, in this order:

`UP Content installation on ThinQ App: Required | Not required | TBD`

`Device firmware supporting the UP Content: Required | Not required | TBD`

Use one value on each line, not the three-value notation. Separate the lines with `<br>` in a Markdown table. Do not add explanations or a third line inside Preconditions.

## Decision 1: UP Content installation on ThinQ App
Answer `Required` when the case assumes the UP Content is available before the tested action, including feature behavior, feature setting, persistence, reset, uninstall, notification, exception, and product-control cases.

Answer `Not required` only when evidence establishes that the case starts before installation, installation is the action under test, or the feature is built in and does not require UP Content installation. For an installation test, keep the installation action in Steps.

Answer `TBD` when the PRD/SRS and accepted structured/image evidence do not establish whether installation is required. Silence is not evidence for `Not required`. Do not confuse installing ThinQ App with installing the UP Content through ThinQ App.

## Decision 2: supported device firmware
Answer `Required` when PRD/SRS evidence identifies the behavior as UP Content, limits it to supported product variants, or otherwise requires device-side support. A missing exact firmware version does not change the decision to `TBD` when the need for supported firmware is established; keep the decision `Required` and record the missing version/build as a gap.

Answer `Not required` only when evidence explicitly establishes that the case is independent of device firmware, such as a purely app-side case before any device interaction.

Answer `TBD` when the sources do not establish whether device-side firmware support is needed. Do not infer `Not required` from missing firmware-version text.

## Evidence and precedence
Derive both decisions from the configured PRD, selectively retrieved SRS, structured PRD fields, readable images, and explicit user-provided requirements. Record the supporting source or local requirement ID for each decision in the analysis companion.

When sources conflict, use `TBD`, identify both claims, and mark the affected case `SETUP CLARIFICATION REQUIRED` unless an approved precedence rule resolves the conflict. Never invent an installation mechanism, firmware version, compatibility list, or upgrade path.

## Relocating other setup
Preconditions no longer carries operational setup. Move source-supported initial setting and device-state preparation to the beginning of Steps before the action under test. Preserve these distinctions:
- Installation case: UP Content is not installed initially; installation remains the tested action.
- Setting-change case: establish/verify the initial value before changing it.
- Negative case: preserve Off, not-installed, unsupported, locked, error, or other negative state.
- Timeout/event case: prepare the state without consuming the timeout or triggering the event under test.
- Reset/uninstall case: establish the non-default configuration first; reset/uninstall remains the tested action.

Unknown required setup remains `TBD` in Steps or Notes and makes the case `SETUP CLARIFICATION REQUIRED`. Do not use `same as above`, `configure as needed`, or an unexplained setup ID.

## Analysis and review
For every case, the analysis companion records:
- objective/action under test;
- UP Content installation decision;
- supported-firmware decision;
- evidence for both decisions;
- missing installation procedure or firmware version/build;
- readiness: `READY-FOR-HUMAN-REVIEW` or `SETUP-CLARIFICATION-REQUIRED`.

The single review pass checks:
- Does Preconditions contain exactly the two required lines and no other setup?
- Is each `Required`, `Not required`, or `TBD` decision supported by PRD/SRS or accepted evidence?
- Is `Not required` based on explicit evidence rather than silence?
- Were operational setting/state prerequisites moved into Steps without performing the action under test?
- Are missing installation procedures and firmware versions disclosed in Notes/analysis?
- Are negative initial states preserved?

`READY-FOR-HUMAN-REVIEW` is not approval or product validation. Never execute setup, install UP Content, update firmware, control ThinQ App, or operate a physical appliance.
