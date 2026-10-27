# PRD reader V1.3
## Mapping and authority
This mapping reflects the export fields discussed with the owner, not an approved universal schema. Missing/renamed fields must be disclosed. Keep the existing developer PRD form.
- prd: primary readable Markdown. prd_json: optional structured export of the same PRD, not automatically an independent behavior specification.
- workitem_id/title/properties: identity, variant and traceability; not functional behavior. Exclude personal/administrative information from cases.
- summary: purpose/context, not automatically a testable requirement.
- product_change.after_html: current behavior candidates. Preserve table relationships, units, negation, conditions and exceptions. Never execute HTML/scripts.
- detail_requirement: filled requirements only; [작성가이드], empty fields and instructions for filling the form are not requirements.
- extra_fields: inspect relevant additional descriptions and meeting material; not all content is normative.
- comments[*].content_html: clarification/proposal/conflict candidates. Timestamp or resolved flag alone does not establish authority.
- images/attachments AND HTML img src: inspect references in both. Empty images arrays do not imply no embedded images.
Read MD for main content, then selectively inspect JSON for references, structure and missing clarification. Merge equivalent requirements and retain both source locations. No automatic MD-over-JSON, image-over-text or newest-comment-wins rule. Apply only a team-approved precedence policy; otherwise record conflict and TBD.

## Input discovery and budget
Read configured supporting_inputs and local references in relevant Markdown/JSON fields. Resolve links relative to the containing document, remove anchors and decode path escapes before safety checks. Reject outside-workspace paths, traversal or symlink escapes according to agent rules. Do not fetch remote URLs. Do not glob the entire repository.
Maintain visited paths and referenced-by locations; prevent cycles. Deduplicate the same resolved path, not assumed identical image content. Inventory unreferenced feature images as unclassified, not automatically requirements.
Image count varies by PRD; never hard-code roles by img_0001 names. Initial behavioral budget: 20 unique images and 20 supporting text documents per run. Prioritize requirement-bearing references; list unprocessed sources and mark PARTIAL when exceeded. Use bounded text chunks; this is not a hard token limit.
Inventory: source ID, path/field, referenced-by, type/role, READ/PARTIAL/UNREADABLE/MISSING/NOT-RELEVANT/NOT-PROCESSED, reason.

## JSON and embedded images
Use documented field semantics; distinguish sample values from exhaustive domains, defaults and normative rules. Do not infer units. Cite exact JSON field paths or stable object IDs. Do not claim programmatic JSON validation without parsing.
Never read a whole JSON file/minified line if it may include large base64 payloads. Use safe bounded field search/preview; if unavailable, mark JSON PARTIAL/unreadable rather than reading the entire payload. Do not decode base64 in model text or copy payloads into artifacts. If a decoded local image is already available, view it and retain original field provenance. Otherwise mark embedded images NOT-PROCESSED and state trusted preprocessing is needed. This package has no automatic base64 extractor and enables no terminal/network tools.

## Image interpretation
Use an actually available image-capable tool/model. Text readFile is not proof an image was viewed. If unavailable/illegible, record the exact limitation and PARTIAL; do not claim analysis succeeded.
Classify viewed images as UI, flow/state diagram, condition table, review/change summary, or mixed. Read relevant text, controls, arrows, guards, edge labels, timeout notes, legends and footnotes. Preserve table row/column relationships and flow directions. Keep short source-language evidence for ambiguous translations.
Distinguish example screen values from specified constants. Do not infer hidden behavior, door lock, timing or color semantics without evidence. For multi-feature summaries, select only in-scope rows; exclude personal/admin information. Record cropped/unreadable regions. Never silently omit a referenced image.

## V1.6 Preconditions decision evidence
Extract evidence that answers two questions: whether the UP Content must be installed through ThinQ App before a case, and whether the device must use firmware supporting that UP Content. Distinguish the need for supported firmware from an exact firmware version/build. Also extract app navigation, UI values and device states needed later in Steps, but do not place those details in Preconditions. Image visibility alone does not establish installation or firmware compatibility. Keep source references, use TBD when evidence is insufficient, and apply config/preconditions-standard.md downstream.
