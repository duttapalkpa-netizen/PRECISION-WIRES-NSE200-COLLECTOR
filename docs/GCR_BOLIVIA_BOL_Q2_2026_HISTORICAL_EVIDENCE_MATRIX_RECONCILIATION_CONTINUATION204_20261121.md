# GCR Continuation 204 — Bolivia (BOL) historical evidence matrix reconciliation
Date: 2026-11-21 (Asia/Kolkata)

## 1. Mandatory continuity preflight
Re-fetched the default-branch artifacts before selecting the task:
- Master Continuity & Acceptance Ledger: `docs/PRECISION_WIRES_V11_3_CONTINUITY_ACCEPTANCE_LEDGER.md`, pre-task blob SHA `b78f381c9bd222f2a73efadd75f5dd52ed64f0fe`.
- GCR Master Priority Queue: `docs/GCR_MASTER_PRIORITY_QUEUE_AND_ZAF_Q2_2026_SOURCE_MAPPING_20261120.md`, pre-task blob SHA `e13c5c1a90e1d094a93998133dc2c4f78ee458e8`.
- Historical Task Registry: `docs/GCR_Q2_2026_HISTORICAL_TASK_REGISTRY_AND_DUPLICATE_PREVENTION_GATE_20261121.md`, pre-task blob SHA `70875181b54df170c8df3e4156fe526ec1c7d745`.
- 63-country national validation matrix: `docs/evidence/gcr/2026Q2_63_country_national_validation_master_matrix.csv`, pre-task blob SHA `2e9b5a9246cebc249acc2e615cae5e43d4d8f4ac`.
- Bolivia country report C158: `docs/GCR_BOLIVIA_BOL_Q2_2026_BCB_OFFICIAL_BOP_SOURCE_BOUNDARY_AUDIT_CONTINUATION158_20261121.md`, blob SHA `374c376d4240e7d6c2b876c1f270aec491d34877`.
- Immutable cohort: `docs/evidence/imf_bop_emde_20261119/coverage_qa/2026Q2_both_legs_candidate_cohort.csv`, blob SHA `31f5bfe5adb59f4c1a139b6d8c54b5ad9fb672c8`.

The fixed 63-country cohort and archived IMF panel were reused. No IMF request, cohort rebuild, or national-source download was performed.

## 2. Duplicate / completed work rejected
- C158 already established two official BCB Q2-2026 workbook locators:
  - BOP workbook: `https://www.bcb.gob.bo/webdocs/publicacionesbcb/1.%20BOP_T2%202026.xlsx`
  - Time-series workbook: `https://www.bcb.gob.bo/webdocs/publicacionesbcb/4.%20Serie_BOP_T2%202026.xlsx`
- Both same-route XLSX retrieval attempts returned HTTP 400 unsupported XLSX MIME. No bytes, sheets, Q2 national values, retrieval receipt, or SHA-256 were captured.
- The C158 report explicitly prohibits repeating the same unsupported route. Therefore no source retry, IMF extraction, numeric comparison, or sign/scale inference was performed.
- C158's accepted status is PARTIAL / NOT PASS: official Q2 locator PASS; national data NOT_CAPTURED; comparison NOT_DONE; aggregate NOT_AUTHORIZED.

## 3. Stale matrix defect and correction
The matrix incorrectly listed BOL as NOT_STARTED / NOT_FOUND despite C158's documented official Q2 locator discovery and blocked retrieval outcome.

Corrected only the BOL row:
- current_stage: BLOCKED
- source_gate: FOUND
- data_capture_gate: NO
- asset_gate: NOT_CAPTURED
- liability_gate: NOT_CAPTURED
- vintage_gate: UNKNOWN
- full_pass: NO
- aggregate_admission: NOT_AUTHORIZED
- status_NOT_STARTED=NO
- status_SOURCE_FOUND=NO
- status_DATA_CAPTURED=NO
- status_ASSET_PASS=NO
- status_LIABILITY_PASS=NO
- status_VINTAGE_PASS=NO
- status_FULL_PASS=NO
- status_BLOCKED=YES
- source_status=SOURCE_FOUND
- data_capture_status=BLOCKED
- asset_status=BLOCKED
- liability_status=BLOCKED
- vintage_status=BLOCKED
- overall_status=BLOCKED
- evidence_ref=C158

This is a status reconciliation only. It does not promote any national evidence gate.

## 4. Recomputed matrix snapshot
The updated CSV was parsed and checked before write:
- Data rows: 63
- NOT_STARTED: 0
- SOURCE_FOUND: 18
- DATA_CAPTURED: 25
- BLOCKED: 20
- ASSET_PASS: 17
- LIABILITY_PASS: 17
- VINTAGE_PASS: 0
- FULL_PASS: 0

Gate counts overlap and are not additive. All 63 countries remain outside FULL_PASS; aggregate remains NOT_AUTHORIZED.

## 5. Acceptance result
| Gate | Status |
|---|---|
| Continuity / queue / registry / country report preflight | PASS |
| Fixed 63-country cohort preserved | PASS |
| C158 prior source evidence reused | PASS |
| Duplicate BCB XLSX route avoided | PASS |
| Stale BOL matrix row corrected | PASS, pending GitHub read-back |
| BOL national data capture | BLOCKED / NOT_CAPTURED |
| BOL dual-leg numeric validation | NOT_DONE |
| BOL vintage validation | UNKNOWN |
| BOL full national validation | PARTIAL / NOT PASS |
| 63-country aggregate | NOT_AUTHORIZED |

## 6. Protected invariants
₹0; free official sources only; no IMF re-query; no cohort rebuild; no synthetic values, fabricated timestamps, unsupported scale/sign conversion, stock-flow substitution, netting, or aggregate admission. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 remain unchanged. UNKNOWN is never PASS.
