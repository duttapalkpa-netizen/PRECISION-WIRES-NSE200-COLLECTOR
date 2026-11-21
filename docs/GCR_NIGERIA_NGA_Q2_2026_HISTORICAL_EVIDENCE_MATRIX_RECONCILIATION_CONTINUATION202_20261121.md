# GCR Continuation 202 — Nigeria (NGA) historical evidence / 63-country matrix reconciliation
Date: 2026-11-21

## Preflight and selection
- Re-opened the Master Continuity Ledger, GCR Master Priority Queue, Historical Task Registry and current 63-country matrix before selecting work.
- The matrix marked NGA as SOURCE_FOUND, while the existing report `docs/GCR_IMF_BOP_SCALE_RECONCILIATION_NIGERIA_20261119.md` already documented the official CBN Q2-2026 BOP Highlights PDF, both national portfolio transaction legs, and six comparisons (Q2-2025, Q1-2026, Q2-2026; assets and liabilities) passing against archived IMF observations.
- Selected a historical evidence reconciliation, not a new source fetch. No IMF re-query, cohort rebuild, or repeat CBN retrieval.

## Evidence reviewed
- Existing CBN PDF: 2,206,494 bytes; SHA-256 `b77c0066385cac4bb3bcbe150321c8da28da7d76c91b78423808a31deaea4cf9`.
- Existing IMF asset CSV SHA-256: `4e7ea3a3f3e171e7b72895ff1b0ad32ee4e8cbba69cf48d2bc2f63f7d2419f24`.
- Existing IMF liability CSV SHA-256: `c6e5bec075e950aa6731380b78c0293a15f38fc7c69a725574971ce115584c45`.
- Existing report records 6/6 comparisons PASS within the CBN publication's USD 5m rounding tolerance. Q2-2026 CBN value is explicitly provisional.

## Matrix correction
- NGA current_stage corrected from SOURCE_FOUND to DATA_CAPTURED.
- source_gate=FOUND; data_capture_gate=YES; asset_gate=PASS; liability_gate=PASS; vintage_gate=PENDING; full_pass=NO; aggregate_admission=NOT_AUTHORIZED.
- Status flags: DATA_CAPTURED=YES, ASSET_PASS=YES, LIABILITY_PASS=YES; VINTAGE_PASS=NO; FULL_PASS=NO; BLOCKED=NO.
- evidence_ref now points to `GCR_IMF_BOP_SCALE_RECONCILIATION_NIGERIA_20261119`.
- The correction does not promote NGA to FULL_PASS. The CBN release labels Q2-2026 provisional; a same-vintage/revision bridge to the archived IMF vintage remains unestablished.

## Guardrails
- Fixed 63-country cohort remains immutable; no cohort rebuild or IMF re-query.
- No net-flow backsolve, unsupported conversion, synthetic values, or aggregate admission.
- All 63-country aggregate_admission remains NOT_AUTHORIZED unless separately authorized by complete acceptance gates.
- CORE-672, engines A-E, Production Selector, RANKING_SCORE and +1 PRESSURE_FADE remain unchanged; UNKNOWN never PASS.
- ₹0 spend; official/free evidence only.

## Result
- This is a matrix/evidence-reference reconciliation only. It closes one stale stage classification, not Nigeria's vintage gate or the wider 63-country audit.
- Updated matrix: `docs/evidence/gcr/2026Q2_63_country_national_validation_master_matrix.csv`.
