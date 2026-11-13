# CDSL 12-Nov-2026 Official-Source Cross-Validation — 2026-11-13

## Objective
Cross-check the previously recorded 12-Nov-2026 CDSL derivative observation against an independently indexed official CDSL page, while explicitly testing whether the same source supplies a matching 12-Nov cash observation.

## Official sources inspected
1. CDSL legacy daily page: https://www.cdslindia.com/publications/FIIDailyData.aspx
2. CDSL current daily page: https://www.cdslindia.com/eservices/publications/fiidaily
3. CDSL FPI landing page: https://www.cdslindia.com/Publications/ForeignPortInvestor.html

## Independent observation
The official CDSL legacy daily page search-index extraction returned a section titled “Daily Trends in FII / FPI Derivative Trades on 12-NOV-2026” and the following nine product rows. The same extracted page's cash section showed a historical 30-AUG-2024 report, not 12-Nov-2026 cash. Therefore, it validates the derivative table only and does not establish a matching cash observation.

| Product | Buy contracts | Buy amount (₹ Cr) | Sell contracts | Sell amount (₹ Cr) | EOD OI contracts | EOD OI amount (₹ Cr) |
|---|---:|---:|---:|---:|---:|---:|
| INDEX_FUTURES | 46,926 | 7,947.67 | 26,621 | 4,614.95 | 184,954 | 31,349.07 |
| INDEX_OPTIONS | 14,517,699 | 2,397,478.52 | 14,566,762 | 2,404,333.50 | 4,317,978 | 720,848.91 |
| STOCK_FUTURES | 340,168 | 23,625.43 | 339,541 | 23,901.06 | 6,115,686 | 410,110.74 |
| STOCK_OPTIONS | 419,990 | 30,494.35 | 432,056 | 31,475.38 | 1,494,678 | 103,262.88 |
| INTEREST_RATE_FUTURES | 0 | 0.00 | 0 | 0.00 | 3,800 | 73.63 |
| CURRENCY_FUTURES | 39,706 | 373.30 | 40,168 | 377.43 | 295,656 | 2.78 |
| CURRENCY_OPTIONS | 0 | 0.00 | 0 | 0.00 | 0 | 0.00 |
| COMMODITY_FUTURES | 31,129 | 967.87 | 31,951 | 1,000.72 | 75,722 | 1,900.55 |
| COMMODITY_OPTIONS | 976,181 | 24,327.39 | 1,024,879 | 25,311.32 | 396,422 | 13,303.08 |

The table matches the previously captured 12-Nov derivative QA artifact (commit `ed68ee12dc9c73d9cadbc7dbf7383e424ae90076`) row-for-row and value-for-value in the available extracted result.

## Cross-validation outcome
- 12-Nov-2026 derivatives: INDEPENDENT OFFICIAL PAGE MATCH — PASS.
- 12-Nov-2026 cash: NOT PRESENT in this extracted official page result — UNKNOWN.
- The current CDSL daily page search result separately displays cash and derivatives for 11-NOV-2026. Do not relabel that cash table as 12-Nov.
- CDSL's methodology says custodian/depository data reflects trades conducted on and up to previous trading day(s). Reporting date and underlying trade date must remain separate fields.
- The extracted legacy page currently combines a stale 30-Aug-2024 cash section with a 12-Nov-2026 derivatives section. This is a mixed-vintage page extraction; never assume the cash and derivatives sections share a reporting date without checking each section heading.

## Data integrity limits
This is independent page-text cross-validation, not raw archive acquisition. No downloadable raw file was obtained; no MIME type, byte count, binary hash, or raw schema QA is claimed. The web extraction itself is not an immutable source artifact. Preserve the existing raw-data acquisition gate as NOT ACQUIRED.

## Acceptance ledger
| Check | State |
|---|---|
| 12-Nov derivatives row-level independent cross-check | PASS |
| 12-Nov cash row-level evidence | UNKNOWN |
| Cash/derivative report-date equality | NOT ESTABLISHED |
| Historical daily archive raw bytes | NOT ACQUIRED |
| Raw SHA-256/schema QA | NOT STARTED |
| Daily factor acceptance | BLOCKED |

## Invariants
₹0 spend; free official sources only; no paid APIs/feeds or external contact; no synthetic rows/timestamps; UNKNOWN is neither PASS nor FAIL; Production Selector, RANKING_SCORE, +1 PRESSURE_FADE and 56×12 CORE-672 unchanged; research-only; no PR merge.
