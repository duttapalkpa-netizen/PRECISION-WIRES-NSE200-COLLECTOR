# Burundi BDI Q2-2026 Historical Matrix Evidence-Link Reconciliation — Continuation 207
Date: 2026-11-21 (Asia/Kolkata)

## Decision
Corrected one stale evidence reference in the fixed 63-country Q2-2026 matrix. BDI's row described the BRB historical dual-leg table and source-boundary finding but its evidence_ref still said NO_DEDICATED_REPORT_REF_IN_BASELINE, despite the existing dedicated C155 report. The row now links to that exact report. This is a metadata/evidence-link correction only, not national Q2 data validation.

## Mandatory preflight and duplicate prevention
- Re-fetched current Master Continuity Ledger, Priority Queue, Historical Task Registry, 63-country matrix and BDI C155 report before selecting this item.
- Existing controlling report: `docs/GCR_BURUNDI_BDI_Q2_2026_BRB_OFFICIAL_BOP_SOURCE_BOUNDARY_AUDIT_CONTINUATION155_20261121.md`, blob SHA-1 `a266b65609a3dedc2e809c645c94b377283b9dfc`.
- C155 establishes that BRB Q4-2025 and Q3-2025 reports contain separate historical portfolio asset/liability lines, but neither is target Q2-2026. It also records the archived IMF Q2 rows without a national comparison.
- Rejected duplicate work: no BRB re-download, no annual/Article IV substitution, no IMF re-query, no scale conversion, no national numeric comparison. Historical adjacent-quarter values are not substituted for Q2-2026.

## Evidence boundary retained
- BRB Q4-2025 Table 9 (MBIF) reports portfolio net -14,143.6; net acquisition of financial assets 0.0; net incurrence of liabilities 14,143.6. Q3-2025 report also has a historical dual-leg table. Both are outside Q2-2026.
- Existing IMF Q2-2026 raw panel rows: A_NFA_T OBS_VALUE 130723.2699945969, SCALE=6; L_NIL_T OBS_VALUE 0, SCALE=6. Raw values and scales remain unchanged; no national comparison is admitted.
- No Q2-2026 national portfolio asset/liability values, raw national bytes, receipt timestamp, SHA-256, current unit/sign mapping or observation-specific revision vintage were captured.
- Therefore BDI remains PARTIAL / NOT PASS; national Q2 legs NOT_CAPTURED; vintage UNKNOWN; aggregate NOT_AUTHORIZED.

## Exact matrix change
- File: `docs/evidence/gcr/2026Q2_63_country_national_validation_master_matrix.csv`
- Changed only BDI row evidence_ref:
  - Before: `NO_DEDICATED_REPORT_REF_IN_BASELINE`
  - After: `GCR_BURUNDI_BDI_Q2_2026_BRB_OFFICIAL_BOP_SOURCE_BOUNDARY_AUDIT_CONTINUATION155_20261121`
- Matrix write commit: `641e119f6a7dd13a2fd4893bf3549592152acb62`
- New matrix blob SHA-1: `7a27ec249675fb40721340f3ed065ca9a2c5bb5c`
- No other BDI field or any other country row was changed.

## Acceptance and constraints
- Evidence-link correction: read-back verification recorded below.
- BDI Q2 national validation: PARTIAL / NOT PASS.
- No Q2 national legs captured; no same-vintage bridge; aggregate NOT_AUTHORIZED.
- No new data retrieval, IMF re-query/cohort rebuild, synthetic data, paid spend or production changes; ₹0.
- Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS.

## Next exact action
BDI may be reopened only if BRB publishes a Q2-2026 BOP table or a genuinely different official export provides target-quarter separate portfolio transaction legs and dated revision metadata. Do not use Q4-2025/Q3-2025 values as Q2-2026 and do not repeat the existing IMF or BRB retrieval work.
