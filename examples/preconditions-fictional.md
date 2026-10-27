# Fictional examples: writing style only
These are synthetic examples, NOT ThinQ navigation or actual product requirements. Do not copy these paths/labels/behavior into real cases.

## Assumed synthetic source for these examples only
A fictional app has a Sample Device > Sample Preferences > Sample Alerts screen. Sample Content is installed using a documented Install action on a Sample Catalog screen; the completion label is Installed. Sample Alerts has a switch, default OFF; changes take effect immediately and there is no Save button. The fictional test feature is an alert at a documented event E. These facts exist only in this example.

## A. Alert behavior
Preconditions:
1. UP Content installation on ThinQ App: Required
2. Device firmware supporting the UP Content: Required
Steps: establish Sample Alerts ON and prepare the device before event E; then trigger documented event E.
Expected: the documented alert appears.

## B. Installation is the test objective
Preconditions: UP Content installation on ThinQ App: Not required<br>Device firmware supporting the UP Content: Required
Steps: verify Sample Content is NOT installed and Sample Catalog is accessible; invoke Install.
Expected: documented Installed confirmation.

## C. Setting change is the test objective
Preconditions: UP Content installation on ThinQ App: Required<br>Device firmware supporting the UP Content: Required
Steps: open Sample Alerts and verify the switch is OFF; change it to ON.
Expected: switch displays ON according to the synthetic source.

## D. Negative case
Preconditions: UP Content installation on ThinQ App: Required<br>Device firmware supporting the UP Content: Required
Steps: set Sample Alerts OFF and prepare the device before event E; trigger E.
Expected: use the source-defined OFF behavior. If that behavior is not specified, TBD; do not assume suppression.

## E. Missing installation procedure
Preconditions: UP Content installation on ThinQ App: Required<br>Device firmware supporting the UP Content: TBD
Notes: SETUP CLARIFICATION REQUIRED — SETUP-GAP-01: installation navigation/completion evidence not supplied; FW-GAP-01: firmware support is not established. Do not invent a menu/version or mark ready.

Read only relevant examples; they illustrate style, not product facts.
