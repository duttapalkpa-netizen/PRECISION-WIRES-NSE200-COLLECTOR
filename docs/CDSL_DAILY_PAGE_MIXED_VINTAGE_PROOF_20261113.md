# CDSL Daily Page Mixed-Vintage Proof — 2026-11-13

## Finding
The official CDSL legacy daily page is a mixed-vintage page at the time inspected: its cash investment section is dated 30-AUG-2024, while its derivatives section is dated 12-NOV-2026. This directly confirms that the cash and derivatives sections on this page cannot be assumed to share a reporting date.

## Official page
URL: https://www.cdslindia.com/Publications/FIIDailyData.aspx
Inspected page: 13-Nov-2026 (web retrieval)
Evidence:
- Lines 0–1: page title and cash heading “Daily Trends in FII / FPI Investments on 30-AUG-2024”.
- Lines 2–20: cash rows and total for 30-AUG-2024.
- Line 21: cash methodology states custodian reports submitted on 30-AUG-2024 and trades conducted on/up to previous trading day(s).
- Lines 24–27: separate derivatives heading and table header.
- Lines 28–36: nine derivative product rows, all reporting date 12-NOV-2026.
- Line 37: derivatives methodology says reports submitted by NSE and BSE on 12-NOV-2026 and reflects previous trading day position.
- Lines 22–23: CDSL distinguishes exchange provisional T-day FII/FPI data from confirmed custodian-reported data.

## Date-alignment result
| Data section | Displayed reporting date | Coverage result |
|---|---|---|
| Legacy page cash investment | 30-AUG-2024 | Does not provide 12-Nov-2026 cash |
| Legacy page derivatives | 12-NOV-2026 | Provides 12-Nov derivatives |
| Current eServices daily page | 11-NOV-2026 in latest indexed extraction | Separate route; does not establish 12-Nov cash |

## Interpretation
1. The 12-Nov-2026 derivatives values are independently visible on the official legacy page and match the previously captured nine-row derivatives QA artifact.
2. The same page's cash section is explicitly 30-Aug-2024. Therefore, it is incorrect to label that cash section as 12-Nov-2026 or use it to fill the 12-Nov cash gap.
3. The latest indexed extraction of the current eServices daily page shows 11-Nov-2026 cash and derivatives. That does not establish the 12-Nov cash report.
4. This establishes a route-level absence of 12-Nov cash in the inspected page snapshots, not proof that no such report exists elsewhere in CDSL's official archive or another official source.
5. Keep CDSL custodian-confirmed data separate from exchange provisional data. Reporting date is not automatically the underlying trade date.

## Data integrity
This is a direct official HTML page observation, not a downloadable raw dataset. No raw archive binary, byte count, MIME type, or SHA-256 is claimed. No synthetic row was created. No endpoint was guessed.

## Acceptance ledger
| Gate | State |
|---|---|
| 12-Nov derivatives visible on official CDSL page | PASS |
| 12-Nov derivatives match prior nine-row QA | PASS |
| Cash section date independently read from same page | PASS (30-Aug-2024) |
| 12-Nov cash available on inspected legacy page | NOT PRESENT |
| 12-Nov cash available on current daily page snapshot | NOT ESTABLISHED |
| 12-Nov cash available elsewhere in CDSL official archive | UNKNOWN |
| Raw daily archive acquired | NOT ACQUIRED |
| Raw-file SHA-256/schema QA | NOT STARTED |
| Daily factor acceptance | BLOCKED |

## Invariants
₹0 spend; free official sources only; no paid APIs/feeds or external contact; no synthetic rows/timestamps; UNKNOWN is neither PASS nor FAIL; Production Selector, RANKING_SCORE, +1 PRESSURE_FADE and 56×12 CORE-672 unchanged; research-only; no PR merge.
