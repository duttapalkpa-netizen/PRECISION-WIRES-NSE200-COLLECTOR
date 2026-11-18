# IMF Brazil event parser schema-path hardening — Part 16
Date: 2026-11-18 (Asia/Kolkata)
Workstream: PRECISION-WIRES V11.3 / গবেষণা যাচাই অব্যাহত 36
Branch: `qa/imf-brazil-parser-schema-path-hardening`

## Objective
Reduce false-positive Brazil event candidates by restricting parser evidence to the SDMX 2.1 RegistryInterface request payload and the RegistrationRequest -> Registration -> ProvisionAgreement / Datasource subtrees. Preserve action lexical values and distinguish source Last Updated from transaction chronology.

## Source basis
- Official SDMX XML schema catalogue: https://xml.sdmx.org/ — lists the SDMX-ML 2.1 schema set, including SDMXMessage.xsd, SDMXRegistry.xsd, SDMXRegistryBase.xsd and SDMXRegistryRegistration.xsd. Catalogue discovery is confirmed.
- Pinned SDMX 2.1 schema mirror (not official raw-byte equivalent): https://github.com/airosa/sdmx-ml-v2_1/tree/d66144444d27c5b66361fb508d795a87072821ac/schemas
- IMF Web Services Guide (May 2025): https://dsbb.imf.org/content/pdfs/IMFSDMXCentralWebServicesGuide.pdf
- IMF User Guide (May 2025): https://dsbb.imf.org/content/pdfs/IMFSDMXCentralUserGuide.pdf
- Official raw XSD direct retrieval was attempted but failed in this environment. No official XSD raw SHA-256 or schema-validation PASS is claimed. This patch is grounded in the official catalogue plus the pinned mirror and is explicitly QA-only pending official-byte validation.

## Code changes (isolated QA branch)
Files changed:
- `scripts/research/imf_brazil_event_parser.py`
- `tests/test_imf_brazil_event_parser.py`

Changes:
1. Require RegistryInterface 2.1 namespace and a direct request payload child; nested fake request elements are not treated as the top-level payload.
2. Restrict supported request payloads to SubmitRegistrationsRequest and SubmitStructureRequest; structure submissions remain NOT_APPLICABLE to data registration.
3. Require direct RegistrationRequest children and direct Registration / ProvisionAgreement / Datasource subtrees before extracting candidate evidence.
4. Candidate matching now uses exact Brazil PA URN, exact BCB URL, or exact provider token only inside the schema-relevant PA/Datasource subtrees. An unrelated annotation/description containing the Brazil URL or PA URN no longer creates a candidate.
5. Preserve action exactly as `action_raw`; validate only against the mirror-derived SDMX 2.1 ActionType values Append, Replace, Delete, Information. No mapping to create/re-register is inferred.
6. Preserve Registration/@lastUpdated as `source_last_updated`; do not manufacture a `transaction_timestamp`.
7. Candidate output remains `REQUIRES_MANUAL_EVIDENCE_REVIEW`, never PASS.

## Test evidence
- Local command: `python -m unittest discover -s tests -p 'test_imf_brazil_event_parser.py' -v`
- Result: 12 tests passed, 0 failed, runtime 0.001 seconds.
- Tests cover exact PA URN, exact datasource URL, narrative false positives, action enum preservation, source Last Updated semantics, structure-event separation, Chile negative control, BOP6-only negative control, wrong namespace, malformed XML and nested fake request.
- These are local synthetic fixture tests only. They are not XSD validation, not GitHub Actions results, and not a real IMF Brazil transaction test.

## Git verification
- Parser blob SHA: `e0df76a518fd7d5f9149c1675f53ab4e199b6c94`
- Tests blob SHA: `e875ee62a4aea19238ae55e728bd299f889aa1a3`
- Branch: `qa/imf-brazil-parser-schema-path-hardening`
- A draft PR is to be opened for review only; do not merge or deploy.

## Acceptance
- Parser schema-path hardening implemented on isolated QA branch: PASS (code presence verified).
- Local fixture tests: PASS (12/12).
- Official SDMX 2.1 raw XSD retrieval/hash: NOT_DONE.
- Formal XSD validation: NOT_DONE.
- GitHub Actions run: NOT_VERIFIED.
- Real Brazil transaction fixture: NOT_DONE.
- Brazil event chronology: UNKNOWN.
- BOP6 vs BOP_BPM6 payload mismatch: CONFIRMED / UNRESOLVED.
- Brazil/EM admission and market use: BLOCKED / NOT_AUTHORIZED.

## No-change / safety
No merge, no production integration, no NSE collector, no RSS/BCB repeat acquisition, no paid API, no macro weights, no trading admission. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56 x 12), and Engines A-E remain unchanged. UNKNOWN is not PASS.
