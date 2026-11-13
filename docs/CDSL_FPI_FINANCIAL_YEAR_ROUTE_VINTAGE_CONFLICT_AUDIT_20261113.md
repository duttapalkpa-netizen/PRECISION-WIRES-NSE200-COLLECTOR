# CDSL FPI Financial-Year Route Vintage Conflict Audit — 2026-11-13

## Executive result
Two official CDSL financial-year pages expose different vintages and must not be merged or treated as equally current.

### Route A — current eServices route
URL: https://www.cdslindia.com/eservices/Publications/FIIFinancial
Observed page data-as-of: **12-Nov-2026**.
Visible rows extend through FY 2026-2027 (partial year) and include FY 2025-2026.
The page-level footer separately says "Page last updated on May 20, 2020". This footer is stale page metadata and is not the data-as-of date. Preserve both fields independently.

### Route B — legacy Publications route
URL: https://www.cdslindia.com/Publications/FIIFPIInvstmntFinYrData.aspx
Observed data footer: **30-Aug-2024**.
Visible rows end at FY 2024-2025 and a Total row. It does not contain FY 2025-2026 or FY 2026-2027. Treat it as a legacy historical snapshot, not current annual series.

## Cross-route reconciliation
The overlapping FY 1998-1999 through FY 2023-2024 values in the rendered text appear aligned for the early periods. The last common FY 2023-2024 row in the current eServices route is:
- Equity 208211.24
- Debt-General 121058.84
- Debt-VRR -2972.37
- Debt-FAR 0
- Hybrid 12766.91
- Mutual Fund Equity/Debt/Hybrid/Solution/Other 0/0/0/0/0
- AIF 0
- Total 339064.62

The legacy route has a materially different FY 2024-2025 row and a footer date 30-Aug-2024, while the current eServices route has later category granularity and a current data-as-of date. Therefore the legacy FY 2024-2025 values must not be substituted for the current eServices route or used to infer FY 2025-2026/2026-2027.

## Latest current-route arithmetic check
For the current eServices route:
- FY 2025-2026 component sum = -152691.03 INR crore; displayed Total = -152691.03; difference 0.00.
- FY 2026-2027 component sum = -30254.53 INR crore; displayed Total = -30254.53; difference 0.00.
These are arithmetic checks on rendered HTML values, not raw-file QA.

## Data governance decisions
1. Use Route A (eServices) as the current financial-year rendered series, with its data-as-of field 12-Nov-2026.
2. Retain Route B only as a legacy snapshot with its own 30-Aug-2024 vintage.
3. Never interpret either page's "last updated May 20, 2020" footer as the actual data-as-of date; keep the explicit data footer separately.
4. Do not merge values from the two routes into one time series without row-level vintage and category mapping.
5. Annual FY data remains a separate frequency and is not daily FPI flow.
6. No original CSV/XLSX bytes, response headers, file size, or SHA-256 were acquired. No raw archive acquisition is claimed.

## Acceptance ledger
| Check | State |
|---|---|
| Current CDSL eServices route identified | PASS |
| Legacy CDSL Publications route identified | PASS |
| Data-as-of dates separated from page footer | PASS |
| Current route FY 2025-26 arithmetic | PASS |
| Current route FY 2026-27 arithmetic | PASS |
| Legacy route kept separate | PASS |
| Original raw file acquired / hashed | NOT ACQUIRED / UNKNOWN |
| Daily archive acquisition | NOT ACQUIRED |
| Daily FPI reconciliation | NOT STARTED |
| Daily factor acceptance | BLOCKED |

## Invariants
₹0 spend; free official sources only; no paid APIs/feeds or external contact; no synthetic rows/timestamps; UNKNOWN is neither PASS nor FAIL; Production Selector, RANKING_SCORE, +1 PRESSURE_FADE and 56×12 CORE-672 unchanged; no PR merge. Research-only.
