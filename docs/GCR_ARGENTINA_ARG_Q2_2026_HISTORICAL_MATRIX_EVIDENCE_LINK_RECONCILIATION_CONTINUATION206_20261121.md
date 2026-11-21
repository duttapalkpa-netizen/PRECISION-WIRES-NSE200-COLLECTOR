# Argentina ARG Q2-2026 Historical Matrix Evidence-Link Reconciliation — Continuation 206
Date: 2026-11-21 (Asia/Kolkata)

## Decision
Completed a narrow evidence-link correction in the existing 63-country Q2-2026 national validation matrix. Argentina's row already recorded DATA_CAPTURED and separate asset/liability numeric PASS gates, but its evidence_ref incorrectly remained NO_DEDICATED_REPORT_REF_IN_BASELINE even though the dedicated INDEC–IMF reconciliation report exists. The matrix now points to that exact report. No validation status was upgraded.

## Mandatory preflight and duplicate prevention
- Re-fetched current Master Continuity Ledger, GCR Master Priority Queue, Historical Task Registry and 63-country national validation matrix before selecting this item.
- Inspected the dedicated report: docs/GCR_ARGENTINA_ARG_Q2_2026_INDEC_IMF_PORTFOLIO_BOP_RECONCILIATION_20261120.md (blob SHA-1 862a8f5e60430d775504898fbdd40b9eb2c2cd41).
- Existing ARG report already documents Q2 2026 national observations, exact IMF receipt, numeric comparisons and the open vintage limitation. No new INDEC retrieval, IMF query, cohort rebuild, arithmetic rerun, or vintage claim was necessary.
- Excluded repeat work: both numeric leg comparisons, INDEC report extraction, IMF artifact retrieval and the failed INDEC XML/CSV vintage routes.

## Evidence retained without alteration
- Official INDEC Q2-2026 BOP report dated 29-Sep-2026, Table I.13: ANAF assets +2,230 USDm; ENP liabilities +7,041 USDm; net portfolio balance -4,811 USDm.
- Existing IMF exact observations: assets +2,230.20632195952 USDm; liabilities +7,041.05282363644 USDm.
- Residuals (IMF exact minus INDEC displayed integer): asset +0.206322 USDm; liability +0.052824 USDm. Both remain PASS within ±0.5 USDm published-integer rounding.
- Existing immutable IMF artifact: run 44474458684, artifact 14505009889, ZIP SHA-256 588101c0deff3b4310984dae5eabcac64fc8288f4416854b7676b4b6ff6b4cd7.
- INDEC says 2024 through Q2-2026 figures are provisional/revisable. The inspected revision annex does not establish a prior Q2-2026 vintage; same-vintage remains NOT_ESTABLISHED.

## Exact matrix change
- File: docs/evidence/gcr/2026Q2_63_country_national_validation_master_matrix.csv
- Changed only ARG row evidence_ref:
  - Before: NO_DEDICATED_REPORT_REF_IN_BASELINE
  - After: GCR_ARGENTINA_ARG_Q2_2026_INDEC_IMF_PORTFOLIO_BOP_RECONCILIATION_20261120
- Matrix write commit: c8b346302cea6197b0de577ef26045fd7dc0eb70
- New matrix blob SHA-1: 1fa8a1e7c57b064ad58f51e6ae18ebe8c3336daf
- The row's current_stage remains DATA_CAPTURED; asset PASS; liability PASS; vintage PENDING; full_pass NO; aggregate_admission NOT_AUTHORIZED.

## Acceptance and constraints
- Evidence-link correction: pending read-back at report creation.
- Argentina full national validation: PARTIAL / NOT PASS.
- Same-vintage bridge: NOT_ESTABLISHED.
- No 63-country aggregate authorization.
- No new source observations or production changes; ₹0; no synthetic data, no net-to-leg back-solving, no sign/scale transformation.
- Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 remain unchanged. UNKNOWN is never PASS.

## Next exact action
Only pursue a distinct, accessible, versioned INDEC Q2-2026 SDMX-ML archive or dated source revision record. The previously tested text/xml transfer and Datos Argentina CSV route are closed for identical retries. If no genuinely new byte-capable official route is available, preserve vintage PENDING and advance to another eligible cohort member.


## Read-back closure — 2026-11-21
All five artifacts were re-fetched from the default branch after the writes:
- Matrix: 63 data rows / 30 columns; ARG evidence_ref verified as the dedicated INDEC–IMF report; row remains DATA_CAPTURED / asset PASS / liability PASS / vintage PENDING / FULL_PASS NO / aggregate NOT_AUTHORIZED. Blob SHA-1: `1fa8a1e7c57b064ad58f51e6ae18ebe8c3336daf`.
- Recomputed matrix stages: SOURCE_FOUND 17; DATA_CAPTURED 26; BLOCKED 20; NOT_STARTED 0. Independent gates: ASSET_PASS 18; LIABILITY_PASS 18; VINTAGE_PASS 0; FULL_PASS 0. All 63 aggregate_admission values remain NOT_AUTHORIZED.
- Detail report read-back blob SHA-1: `95e95fd2215fb264f2b298dce121e861e1301df3`.
- Priority Queue read-back blob SHA-1: `af5aece9d9d1d64a28b691db2d5010974f92976f`.
- Historical Registry read-back blob SHA-1: `adc74756c6243cb8f127f71455d5780527ee6e9f`.
- Master Continuity Ledger read-back blob SHA-1: `df92b6865cb5df6811ddf0b3a83b987c445d03b7`.
- C206 marker and ARG report reference were verified in the detail report, queue, registry and ledger. No numeric, vintage or aggregate status was promoted.
