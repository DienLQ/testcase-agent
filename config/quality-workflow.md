# Quality workflow V1.3
## Atomic requirements
Create LOCAL R-001 style IDs, never pretend they are source requirement IDs. Record original IDs separately. One observable behavior per row: variant/scope, precondition, trigger, expected behavior, constraints/exceptions, evidence, gaps. Classify EXPLICIT / OBSERVED-UI / ASSUMPTION / CONFLICT. UI observation does not prove hidden behavior. Preserve negative requirements and source units.
## SRS reconciliation
Use V1.2 selective SRS retrieval and shared budgets. Map SRS evidence to extracted requirements. Keep conflicts/unprocessed dependencies visible; no full-file reads. Reading every source does not prove completeness.
## Models before cases
- State transitions: state, event, guard, action, next state, source. Include documented timeout/cancel/pause/resume/reset only in scope. Unknowns stay TBD.
- Decision rules: conditions, supported feasible combinations, actions, source. Exclude combinations only with evidence; avoid unrestricted Cartesian products.
- Partitions/boundaries: domain, units, precision, limits, source. At/below/above only when domain and precision are known; never invent +/-1 units or tolerance.
- Variants: separate app/LCD/LED/model behavior only when sources establish applicability. Do not expand scope from unrelated rows in a review image.
Mark nonapplicable models N/A with a short reason.
## Generate
Each case needs reproducible preconditions, concrete steps, observable expected results and source/requirement links. Avoid 'works correctly'. Unsupported outcomes are TBD. No fixed case count. Preserve team columns; traceability may live in the analysis companion. Do not claim execution or passing product tests.
## One review pass
Check evidence for every expected result, scope/variant, executable steps, duplicate cases/IDs, uncovered extracted requirements, supported model branches and unread sources. Correct supported issues once; record unresolved gaps. Same-agent review is NOT independent validation.
Map each local requirement/model element to case IDs or NOT-COVERED with reason. Do not call extracted-requirement mapping product coverage or claim 100% completeness. Report only observed counts, never fabricated token usage.
## Update and save
Preserve unaffected IDs/content and prior provenance; update affected mappings. Use companion templates. Read back all artifacts. Report saved paths, actual case count, sources read, PARTIAL/gaps and developer/QE review required. Missing primary PRD/template is BLOCKED; missing supporting context permits a supported PARTIAL draft.

## V1.6 Preconditions quality gate
Read config/preconditions-standard.md. Before generation, decide per case whether UP Content installation through ThinQ App and supported device firmware are Required / Not required / TBD. Preconditions contains exactly those two answers and no operational setup. Track both decisions, evidence, gaps and readiness in the analysis companion. Move source-supported setting and device-state preparation to the beginning of Steps while keeping the action under test in Steps. Preserve negative states. Never infer `Not required` from silence or call a case ready when required installation/firmware evidence is unresolved. Use existing test-case columns; companion templates may express the two decisions directly.
