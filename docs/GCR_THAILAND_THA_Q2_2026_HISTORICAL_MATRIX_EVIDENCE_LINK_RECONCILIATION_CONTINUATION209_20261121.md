# Thailand THA Q2-2026 historical matrix evidence-link reconciliation — Continuation 209
Date: 2026-11-21 (Asia/Kolkata)

## Decision
Corrected only the stale THA evidence_ref in the fixed 63-country matrix to point to the already-existing BOT–IMF dual-leg reconciliation. This is a metadata-link repair, not a new national validation or vintage pass.

## Preflight and duplicate prevention
- Re-fetched the current Master Continuity Ledger, GCR Priority Queue, Historical Task Registry, 63-country matrix and the dedicated THA report before selection.
- Existing report: `docs/GCR_THAILAND_THA_Q2_2026_BOT_IMF_PORTFOLIO_DUAL_LEG_RECONCILIATION_20261120.md`, blob SHA-1 `9ae717f73f333f88a13a101679896b7be4caa028`.
- BOT EC_XT_049_S2 Q2/2026 p official USD table: assets +4,679.07 USDm; liabilities -238.36 USDm; portfolio parent 4,917.43 USDm; displayed accounting identity passes.
- Archived IMF exact rows reused from immutable panel; residuals: asset +0.00342150334 USDm and liability +0.001811289819 USDm, both within ±0.005 USDm display tolerance.
- Existing run 44689541630 succeeded (~13 seconds); artifact 14607329438; ZIP SHA-256 `70328900a9e0058385c6ac7efa5384f86d10508a5056f8f16e40c3afd5b24aec`. Raw BOT HTML SHA-256 `b4a42305fe18668c91e1feadd70ada0537f6e2f8c5b13ef59dd1fdcbd4d00f80`.
- No BOT re-fetch, IMF re-query, panel/cohort rebuild, or repeat numeric comparison performed.

## Exact matrix change
- File: `docs/evidence/gcr/2026Q2_63_country_national_validation_master_matrix.csv`
- THA evidence_ref: `NO_DEDICATED_REPORT_REF_IN_BASELINE` → `GCR_THAILAND_THA_Q2_2026_BOT_IMF_PORTFOLIO_DUAL_LEG_RECONCILIATION_20261120`.
- No other THA field or country row changed.

## Gate decision retained
THA remains DATA_CAPTURED; asset PASS; liability PASS; vintage PENDING; FULL_PASS=NO; aggregate NOT_AUTHORIZED. BOT page is preliminary and last updated 30-Sep-2026 14:33; IMF archived panel retrieval date is 19-Nov-2026, not an observation vintage. Same-vintage bridge remains NOT_ESTABLISHED. Numeric agreement does not prove vintage identity.

## Read-back acceptance
The matrix and continuity artifacts must be re-fetched after writes. This task passes only if the THA evidence_ref is exact, 63 rows/30 columns remain, all other country rows and THA gate fields are unchanged, and the C209 marker is present in the queue, registry and ledger.

## Protected invariants
₹0 spend; no synthetic values or fabricated timestamps; UNKNOWN never PASS; aggregate remains NOT_AUTHORIZED. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged.
