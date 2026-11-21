# GCR India (IND) Q2-2026 — historical evidence matrix reconciliation (Continuation 205)
Date: 2026-11-21 (Asia/Kolkata)

## 1. Mandatory continuity preflight
Before selecting this task, re-fetched the current default-branch artifacts:
- Master Continuity Ledger: `docs/PRECISION_WIRES_V11_3_CONTINUITY_ACCEPTANCE_LEDGER.md`, blob SHA `e5635829db06e5979a91df202e7d3c56c2d1b9aa`.
- GCR Master Priority Queue: `docs/GCR_MASTER_PRIORITY_QUEUE_AND_ZAF_Q2_2026_SOURCE_MAPPING_20261120.md`, blob SHA `bfd6a61e8c0ceb20127045c71595189eb1aefa23`.
- Historical Task Registry: `docs/GCR_Q2_2026_HISTORICAL_TASK_REGISTRY_AND_DUPLICATE_PREVENTION_GATE_20261121.md`, blob SHA `d4a9d33da1912358dc0e375d0ee3aa3b04b69c5f`.
- 63-country national validation matrix: `docs/evidence/gcr/2026Q2_63_country_national_validation_master_matrix.csv`, pre-task blob SHA `670a3636e7cca35f41e4b996f43e6084669e6e46`.
- India current-vintage supplement: `docs/GCR_IMF_BOP_SCALE_RECONCILIATION_INDIA_CURRENT_VINTAGE_SUPPLEMENT_20261119.md`, blob SHA `b3a1a41e60209f11229fe07e9439dd95935b67ed`.
- India Q1 release-persistence report C187: `docs/GCR_INDIA_IND_Q1_2026_RBI_TABLE42_RELEASE_PERSISTENCE_AUDIT_CONTINUATION187_20261121.md`, blob SHA `547cdd8b615e80cf4473b2811b96ae7a4c4cedfd`.
- Existing comparison CSV: `docs/evidence/imf_bop_20261119/india_scale_reconciliation_current_vintage/india_bop_scale_sign_crosswalk.csv`, blob SHA `8ff2534dc730c822b20351530b9379fb86369cb2`.
- Fixed Q2-2026 both-leg cohort: `docs/evidence/imf_bop_emde_20261119/coverage_qa/2026Q2_both_legs_candidate_cohort.csv`, blob SHA `31f5bfe5adb59f4c1a139b6d8c54b5ad9fb672c8`.

## 2. Task selection / completed work excluded
- Matrix row IND was still SOURCE_FOUND / data_capture NO / both national legs NOT_CAPTURED, but the already-archived RBI current-vintage supplement records Q2-2026 asset, liability and combined-net comparisons as PASS.
- C187 Q1 release-persistence work is already complete and was not repeated. Its Q1-2026 liability discrepancy remains REVIEW; this C205 task does not change it.
- BOJ C84–C85 metadata/API access gate is already documented; no repeated BOJ API/ZIP request, no guessed series code, and no new BOJ extraction was attempted.
- No RBI source page was re-fetched; existing raw HTML, archived crosswalk and source hashes were reused. No IMF GET, cohort rebuild or source-data rewrite.

## 3. Q2-2026 official national source and exact comparison
- Official RBI Table 42, “Standard Presentation of BoP in India as per BPM6 (US$ Million)”, Apr–Jun 2026 page: https://www.rbi.org.in/Scripts/BS_ViewBulletin.aspx?Id=24566
- Publication date: 2026-10-23. The existing supplement states both official RBI Table 42 pages were retrieved anonymously and raw HTML, retrieval timestamps, safe headers and SHA-256 are archived.
- Source HTML SHA-256 for the Apr–Jun 2025/2026 Table 42 page: `075c28122d588e5bce0ff45c8c8d5d8b453c53dc5b9a20f79d5cd3a6e54f5396`.
- Official RBI unit: USD million; integer display; comparison tolerance ±0.5 USDm.
- Mapping retained from prior India validation: RBI 3.2.A “Portfolio Investment in India” credit-minus-debit net ↔ IMF `L_NIL_T`, same sign; RBI 3.2.B “Portfolio Investment by India” net ↔ negative IMF `A_NFA_T`; RBI combined net ↔ IMF `L_NIL_T - A_NFA_T`.
- Existing comparison CSV exact Q2 rows:
  - Assets: IMF derived USDm 923.5105867793835; RBI comparable +924; residual -0.4894132206165; bound ±0.5; PASS.
  - Liabilities: IMF derived USDm -8,638.759946257262; RBI comparable -8,639; residual +0.240053742738; bound ±0.5; PASS.
  - Combined net: IMF derived USDm -9,562.2705330366455; RBI -9,562; residual -0.2705330366455; bound ±0.5; PASS.
- All three Q2 comparisons are PASS at the published integer-million rounding tolerance. Raw IMF OBS_VALUE / SCALE metadata are preserved in the source crosswalk; no IMF raw value is overwritten.

## 4. Vintage and acceptance boundary
- Q2-2026 is captured from the official 23-Oct-2026 RBI Table 42 release and raw HTML is archived with a SHA-256.
- The current-vintage supplement does not establish exact same-vintage identity between the archived IMF observation snapshot and the RBI 23-Oct release. Therefore the vintage gate remains PENDING, not PASS.
- India Q1-2026 remains separate: RBI published liability net -12,121 USDm persisted across the inspected June/July/August releases, while archived IMF liability is -13,633.508347 USDm; residual -1,512.508347 USDm remains REVIEW, cause/same-vintage NOT_ESTABLISHED (C187).
- Do not roll Q2 numeric PASS into an all-quarter India FULL_PASS. Do not infer Q1 correction, use BOJ monthly figures to overwrite RBI Q2, or admit India to aggregate.

## 5. Corrected Q2-2026 matrix row
Only the IND Q2 row was corrected:
- current_stage=DATA_CAPTURED; source_gate=FOUND; data_capture_gate=YES
- asset_gate=PASS; liability_gate=PASS; vintage_gate=PENDING
- full_pass=NO; aggregate_admission=NOT_AUTHORIZED
- status_NOT_STARTED=NO; status_SOURCE_FOUND=NO; status_DATA_CAPTURED=YES
- status_ASSET_PASS=YES; status_LIABILITY_PASS=YES; status_VINTAGE_PASS=NO; status_FULL_PASS=NO; status_BLOCKED=NO
- source_status=SOURCE_FOUND; data_capture_status=DATA_CAPTURED
- asset_status=ASSET_PASS; liability_status=LIABILITY_PASS; vintage_status=DATA_CAPTURED; overall_status=DATA_CAPTURED
- evidence_ref=`GCR_IMF_BOP_SCALE_RECONCILIATION_INDIA_CURRENT_VINTAGE_SUPPLEMENT_20261119`

## 6. Recomputed 63-country matrix snapshot
Validated proposed CSV before write:
- Rows: 63
- SOURCE_FOUND: 17
- DATA_CAPTURED: 26
- BLOCKED: 20
- NOT_STARTED: 0
- ASSET_PASS: 18
- LIABILITY_PASS: 18
- VINTAGE_PASS: 0
- FULL_PASS: 0
- All rows retain aggregate_admission=NOT_AUTHORIZED. Gate counts overlap; they are not additive.

## 7. Acceptance and invariants
| Gate | Status |
|---|---|
| Ledger / queue / registry / prior-report preflight | PASS |
| RBI Table 42 Q2-2026 official source evidence reused | PASS |
| Existing IMF exact-key rows and comparison CSV reused | PASS |
| Q2 assets numeric comparison | PASS |
| Q2 liabilities numeric comparison | PASS |
| Q2 combined net comparison | PASS |
| IND matrix status corrected from stale SOURCE_FOUND | PASS, pending read-back |
| Q2 same-vintage bridge | PENDING / NOT_ESTABLISHED |
| India Q1 liability discrepancy | REVIEW (unchanged) |
| India FULL_PASS | NO |
| Aggregate admission | NOT_AUTHORIZED |

₹0; official/free evidence only; no synthetic observations, fabricated timestamps, IMF re-query, cohort rebuild, unsupported sign/scale changes, or production changes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS.


## Final GitHub read-back (2026-11-21)
- Matrix correction committed and re-fetched from the default branch. The IND row now reads DATA_CAPTURED / asset PASS / liability PASS / vintage PENDING / FULL_PASS NO / aggregate NOT_AUTHORIZED.
- Recomputed after read-back: 63 rows; SOURCE_FOUND 17; DATA_CAPTURED 26; BLOCKED 20; NOT_STARTED 0; ASSET_PASS 18; LIABILITY_PASS 18; VINTAGE_PASS 0; FULL_PASS 0.
- Master Ledger, Priority Queue, Historical Registry, Matrix and this report were all re-fetched after writes; all five contain the C205 entry/correction. All 63 aggregate_admission fields remain NOT_AUTHORIZED.
