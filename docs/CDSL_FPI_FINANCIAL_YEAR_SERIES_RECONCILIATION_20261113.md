# CDSL Financial-Year FPI Series — Historical Alternate Route & Arithmetic Reconciliation — 2026-11-13

## Result
A second official CDSL historical FPI route is available as a rendered financial-year table:
https://www.cdslindia.com/eservices/Publications/FIIFinancial

The page was opened and its table content inspected on 2026-11-13. It contains financial-year observations from 1998-1999 through the current 2026-2027 row, with an as-of footer of 12-Nov-2026. This provides an official historical annual/financial-year series independently of the still-unresolved CDSL daily archive control.

## Column interpretation
The page groups values in INR crore under:
- Equity: Equity
- Debt: Debt-General Limit, Debt-VRR, Debt-FAR
- Hybrid
- Mutual Fund: Equity, Debt, Hybrid, Solution Oriented, Other
- AIF
- Total

This is an annual financial-year aggregation. It is NOT daily FPI flow and must not be joined to daily NSE provisional or CDSL confirmed daily rows as if it were a daily observation.

## Independent arithmetic checks
Recomputed the visible Total for the two latest financial-year rows by summing the 11 displayed component columns, retaining the displayed signs and precision.

### FY 2025-2026
Components (INR crore):
- Equity: -180831.27
- Debt-General Limit: 12428.44
- Debt-VRR: -2071.04
- Debt-FAR: 15448.97
- Hybrid: -370.76
- Mutual Fund Equity: 2750.29
- Mutual Fund Debt: -594.98
- Mutual Fund Hybrid: -55.37
- Mutual Fund Solution Oriented: -2.74
- Mutual Fund Other: 602.76
- AIF: 4.67
- Recomputed sum: -152691.03
- Displayed Total: -152691.03
- Difference: 0.00 — PASS

### FY 2026-2027 (current partial year)
Components (INR crore):
- Equity: -88632.53
- Debt-General Limit: 52396.65
- Debt-VRR: -19726.76
- Debt-FAR: 19397.85
- Hybrid: -4918.26
- Mutual Fund Equity: 10434.71
- Mutual Fund Debt: -14.27
- Mutual Fund Hybrid: -72.34
- Mutual Fund Solution Oriented: 0.00
- Mutual Fund Other: 879.63
- AIF: 0.79
- Recomputed sum: -30254.53
- Displayed Total: -30254.53
- Difference: 0.00 — PASS

## Provenance and limitations
- Official SEBI FPI curation table lists CDSL financial-year FPI/FII investment details as an official source route:
  https://www.sebi.gov.in/curation/fpi.html
- CDSL page itself displays its current data as-of date 12-Nov-2026; its separate footer says the page was last updated on 20-May-2020. These are distinct metadata fields and must not be conflated.
- The visible HTML table is source evidence but is not a downloaded original CSV/XLSX archive. No raw file bytes, HTTP response headers, file size, or SHA-256 were acquired.
- FY 2026-2027 is a partial year as of the displayed 12-Nov-2026 date; it must not be treated as a completed financial year.
- CDSL's daily historical archive (1999-Till Date selector) remains a separate unresolved acquisition route. This annual table does not close the daily archive gate.
- No daily backfill, daily coverage, or daily NSE provisional-versus-CDSL confirmed reconciliation is claimed.

## Acceptance ledger
| Gate | State |
|---|---|
| Official CDSL financial-year page identity | PASS |
| SEBI curation independently lists CDSL financial-year route | PASS |
| Visible historical financial-year coverage | PASS (rendered table) |
| Latest as-of metadata captured | PASS (12-Nov-2026) |
| FY 2025-26 displayed total arithmetic | PASS |
| FY 2026-27 partial-year displayed total arithmetic | PASS |
| Original raw CSV/XLSX acquired | NOT ACQUIRED |
| SHA-256 of original file | UNKNOWN |
| Daily historical archive acquired | NOT ACQUIRED |
| Daily FPI reconciliation | NOT STARTED |
| Daily-factor acceptance | BLOCKED |

## Project invariants
₹0 spend; free official sources only; no paid APIs/feeds or external contact; no synthetic observations or timestamps; UNKNOWN is neither PASS nor FAIL; Production Selector, RANKING_SCORE, +1 PRESSURE_FADE and 56×12 CORE-672 unchanged; no PR merge. Research-only.
