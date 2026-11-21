# GCR Q2-2026 — Belize (BLZ) Central Bank official BOP source-boundary audit
Date: 2026-11-21 (Asia/Kolkata)
Continuation: 157
Status: FIXED-COHORT / IMF ROW PRESENCE PASS; OFFICIAL CBB Q2/H1 PUBLICATION AND SEPARATE LEG LABELS CONFIRMED; NATIONAL Q2-ONLY DUAL-LEG VALUES NOT_CAPTURED; BLZ PARTIAL / NOT PASS.

## 1. Continuity preflight and duplicate rejection
- Re-fetched Master Continuity Ledger, GCR Priority Queue and immutable 63-country Q2-2026 cohort. BLZ is a cohort member with both archived IMF legs present.
- Repository search found no dedicated prior BLZ Q2-2026 national portfolio dual-leg report.
- BIH continuation 156: official CBBH Q2 release calendar and historical table confirmed, but dynamic portal export was NOT_EXECUTED; retain BIH PARTIAL. No repeated BIH route here.
- BLR/BLZ/BOL repository search found no dedicated country Q2-2026 national portfolio dual-leg reports; BLZ selected because a new official Central Bank of Belize Q2 review and a downloadable full BOP Excel locator were discoverable.
- No IMF re-query, cohort rebuild, or panel rebuild.

## 2. Official Central Bank of Belize Q2-2026 publication
- Official source: Central Bank of Belize, “June 2026 Quarterly Review”.
- PDF: https://www.centralbank.org.bz/docs/default-source/3.3.2-quarterly-reviews/june-2026-quarterly-review.pdf
- The review identifies its period as the second quarter / January–June 2026 and labels 2026 figures provisional.
- Table A.21 (page 50) “Capital and Financial Accounts”, unit $mn, publishes Jan–June cumulative 2026 portfolio investment net 0.0; subrows by institutional sector are also 0.0. This table does not split the total into portfolio assets and liabilities.
- Table A.22 (page 51) “Balance of Payments”, unit $mn, separately labels:
  - Portfolio Investment Assets: Jan–June 2026 = 0.0
  - Portfolio Investment Liabilities: Jan–June 2026 = 0.0
  - The reference period is Jan–June cumulative, not Q2-only.
- Table A.31 (page 57) is an IIP reconciliation table with positions and Jan–June financial-account transactions; portfolio asset and liability transaction columns are both 0.0 over Jan–June. These are H1 cumulative amounts, not Q2-only; do not infer quarter-specific values by differencing unless the exact same-vintage Q1 series and revision basis are independently captured.
- The review states 2026 figures are provisional and 2025 figures revised. No Q2-specific revision/vintage snapshot was captured.
- Official BOP statistics page defines BOP as transactions during a period and links a “Download full data set in Excel” workbook:
  https://www.centralbank.org.bz/home/statistics/external-sector/balance-of-payments
- Exact XLSX locator from the page:
  https://www.centralbank.org.bz/docs/default-source/3.8-external-sector/3.7.3-balance-of-payments/t48---balance-of-payments-new-format.xlsx?sfvrsn=7c8e8ac_74
  Browser fetch failed with HTTP 400 unsupported XLSX content type. No workbook bytes, sheet layout, quarter-specific rows, raw receipt, timestamp or SHA-256 captured.
- IMF e-GDDS metadata for Belize confirms quarterly and annual BOP, portfolio investment assets/liabilities definitions and data compilation sources. It also describes data sources by asset/liability subcategory:
  https://dsbb.imf.org/egdds/dqaf-base/country/BLZ/category/BOP00

## 3. Existing archived IMF Q2-2026 rows reused — no query
From existing raw IMF panel CSVs:
- Asset file `docs/evidence/imf_bop_emde_20261119/raw/EMDE_A_NFA_T_P_F_ALL_UNITS_Q.csv`, Git blob SHA `15449e87c9057291a1f52f2f8cd9805df55f9fb8`.
  - Exact row: COUNTRY=BLZ; ENTRY=A_NFA_T; INDICATOR=P_F; UNIT=USD; FREQUENCY=Q; PERIOD=2026-Q2; OBS_VALUE=142.2106890070215; SCALE=6; PRECISION=6; DERIVATION_TYPE=O; IFS_FLAG=true.
- Liability file `docs/evidence/imf_bop_emde_20261119/raw/EMDE_L_NIL_T_P_F_ALL_UNITS_Q.csv`, Git blob SHA `15f379dc42e2760eb5f2384618e48f5ddc3177f1`.
  - Exact row: COUNTRY=BLZ; ENTRY=L_NIL_T; INDICATOR=P_F; UNIT=USD; FREQUENCY=Q; PERIOD=2026-Q2; OBS_VALUE=0; SCALE=6; PRECISION=6; DERIVATION_TYPE=O; IFS_FLAG blank.
- Raw OBS_VALUE and SCALE preserved exactly. Git blob SHAs are not SHA-256. No conversion, sign adjustment or numeric comparison.

## 4. Acceptance matrix
| Gate | Status |
|---|---|
| BLZ membership in immutable 63-country Q2-2026 cohort | PASS |
| Archived IMF A_NFA_T / L_NIL_T rows present | PASS |
| Official CBB Q2-2026 review located | PASS |
| Separate national portfolio asset/liability labels | PASS (H1 cumulative only) |
| National H1 2026 values and $mn unit | PASS (period not Q2-only) |
| Q2-only national asset/liability transaction values | NOT_CAPTURED |
| Official full BOP XLSX locator | PASS |
| XLSX raw bytes/sheets/hash | NOT_CAPTURED (HTTP 400 MIME restriction) |
| Q2 observation-specific revision vintage | NOT_ESTABLISHED |
| National sign/item/scale bridge to IMF Q2 rows | NOT_ESTABLISHED |
| Numeric comparison | NOT_DONE |
| BLZ full national dual-leg validation | PARTIAL / NOT PASS |
| 63-country aggregate authorization | NOT_AUTHORIZED |

## 5. Rejected substitutes
- H1 cumulative Jan–June 2026 legs are not Q2-only. Do not use as Q2 values.
- IIP end-period positions are stocks, not BOP transactions.
- Do not derive Q2 by subtracting another quarter without exact same-vintage source rows and documented revision alignment.
- Do not treat a net portfolio row or H1 zero as proof that each Q2 leg is zero.

## 6. Next bounded action
- Recover the official CBB BOP workbook through a supported byte-download or official export route; inspect exact quarter labels and both portfolio legs for 2026-Q2, preserving original bytes, timestamp and SHA-256.
- If workbook access remains blocked, retain BLZ PARTIAL and advance to the next eligible fixed-cohort member. No repeated identical browser XLSX fetch.
- No aggregate admission until country dual-leg gates pass.

## 7. Protected invariants
₹0; free official sources only. No synthetic values, fabricated timestamps, IMF re-query, cohort rebuild, inferred sign/scale, stock-as-flow, net-to-leg back-solving, annual/H1-to-quarter allocation, aggregate admission or production changes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS.
