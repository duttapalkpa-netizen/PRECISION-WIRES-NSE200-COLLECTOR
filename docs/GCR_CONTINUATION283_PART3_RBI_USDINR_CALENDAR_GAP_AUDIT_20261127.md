# GCR Continuation 283 — Part-3 RBI/FBIL USD-INR calendar-gap audit and coverage adjudication (27-Nov-2026)

Date: 2026-11-27 (Asia/Kolkata)  
Conversation: গবেষণা যাচাই অব্যাহত 62, Part-3  
Repository: `duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR`

## 1. Mandatory continuity preflight and PASS skip
- Re-read the current GitHub Master Continuity Ledger (pre-update blob `5bd56b3fdda381b044ef856d237db0f80b04a9d7`), GCR Master Priority Queue (blob `d519c2dc2de7b4b9e7557cd780ccf5c7aa714d66`), 63-country Historical Task Registry (blob `8ee0e9f9c148ea4e8d589d946fb54f01fc2bf48d`), C280 official USD/INR source report, C281 attachment identity gate and C282 raw payload report.
- Rechecked Library `/BankWise.xls` and `/BankWise(1).xls` using the already materialized original bytes. Both remain exact duplicates; no new Library upload, overwrite, rename or deletion.
- Skipped C278 isolated archive-contract regression PASS, prior NSE archive/QA PASS work, and C282 raw byte capture/hash/table parsing already completed. No repeat source discovery or broad workflow.

## 2. Raw input identity carried forward
- File: `/BankWise.xls` (same bytes as `/BankWise(1).xls`), 57,289 bytes.
- SHA-256: `379318c3e4b048eeba63824bc09d26b2e6f5d9418e17bd589059d4c0b63e93e2`.
- Payload is HTML table markup with columns `Date` and `USD (INR / 1 USD)`, not a native BIFF/OOXML workbook.
- 1,119 parsed observations; 1,119 unique dates; 0 duplicate dates; 0 malformed rows; 0 blank cells; all rates positive and numeric.
- Earliest observation: 2018-07-24 (one isolated row); next observation: 2022-04-12; latest observation: 2026-11-26.

## 3. Critical continuity result
The 1,119 unique rows do NOT constitute a continuous 2018–2026 daily series.
- Year counts: 2018=1; 2019=0; 2020=0; 2021=0; 2022=176; 2023=242; 2024=240; 2025=243; 2026=217.
- Largest observed-date gap: 1,358 calendar days, from 2018-07-24 to 2022-04-12.
- Within that gap alone, 969 Monday–Friday calendar dates have no observation. These are weekday candidates, not an assertion that all are expected publication sessions.
- Across the full file, 35 intervals exceed three calendar days; they contain 1,008 intervening Monday–Friday calendar dates in total (969 in the 2018–2022 hole and 39 in shorter intervals).
- Short 4–6-day intervals may include weekends and Mumbai bank holidays; without a complete authoritative holiday calendar joined to the FBIL publication calendar, they are UNRESOLVED, not automatically missing trading sessions.
- RBI's 04-Jul-2018 release says FBIL USD/INR reference rates are published each weekday excluding Saturdays, Sundays and Mumbai bank holidays, effective 10-Jul-2018: https://www.rbi.org.in/Scripts/BS_PressReleaseDisplay.aspx?prid=44393. This makes the 2018–2022 gap a decisive continuity exception, not a routine weekend gap.

## 4. Full gap inventory (>3 calendar days)
| Previous observation | Next observation | Calendar gap (days) | Intervening Mon–Fri dates |
|---|---|---:|---:|
| 2018-07-24 | 2022-04-12 | 1358 | 969 |
| 2022-04-13 | 2022-04-18 | 5 | 2 |
| 2022-05-13 | 2022-05-17 | 4 | 1 |
| 2022-08-11 | 2022-08-17 | 6 | 3 |
| 2022-10-21 | 2022-10-25 | 4 | 1 |
| 2023-04-06 | 2023-04-10 | 4 | 1 |
| 2023-04-13 | 2023-04-17 | 4 | 1 |
| 2023-04-28 | 2023-05-02 | 4 | 1 |
| 2023-05-04 | 2023-05-08 | 4 | 1 |
| 2023-09-29 | 2023-10-03 | 4 | 1 |
| 2023-11-24 | 2023-11-28 | 4 | 1 |
| 2023-12-22 | 2023-12-26 | 4 | 1 |
| 2024-01-19 | 2024-01-23 | 4 | 1 |
| 2024-01-25 | 2024-01-29 | 4 | 1 |
| 2024-02-16 | 2024-02-20 | 4 | 1 |
| 2024-03-07 | 2024-03-11 | 4 | 1 |
| 2024-03-22 | 2024-03-26 | 4 | 1 |
| 2024-03-28 | 2024-04-02 | 5 | 2 |
| 2024-05-17 | 2024-05-21 | 4 | 1 |
| 2024-06-14 | 2024-06-18 | 4 | 1 |
| 2024-10-31 | 2024-11-04 | 4 | 1 |
| 2024-11-14 | 2024-11-18 | 4 | 1 |
| 2025-03-13 | 2025-03-17 | 4 | 1 |
| 2025-03-28 | 2025-04-02 | 5 | 2 |
| 2025-04-11 | 2025-04-15 | 4 | 1 |
| 2025-04-17 | 2025-04-21 | 4 | 1 |
| 2025-05-09 | 2025-05-13 | 4 | 1 |
| 2025-08-14 | 2025-08-18 | 4 | 1 |
| 2025-09-05 | 2025-09-09 | 4 | 1 |
| 2026-01-23 | 2026-01-27 | 4 | 1 |
| 2026-04-02 | 2026-04-06 | 4 | 1 |
| 2026-04-30 | 2026-05-04 | 4 | 1 |
| 2026-06-25 | 2026-06-29 | 4 | 1 |
| 2026-09-11 | 2026-09-15 | 4 | 1 |
| 2026-10-01 | 2026-10-05 | 4 | 1 |

## 5. Corrected acceptance matrix
| Gate | Result | Interpretation |
|---|---|---|
| Raw bytes / SHA-256 | PASS | Exact payload identity retained |
| HTML table parse / schema | PASS | Two expected columns, 1,119 parsed rows |
| Numeric / null / duplicate QA | PASS | Positive numeric values; no blanks or duplicate dates |
| Minimum sample count (>=60 distinct dates) | PASS | 1,119 unique observations |
| Minimum span (>=90 calendar days) | PASS | Date endpoints span 3,047 days |
| Full 2018–2026 continuity | FAIL | 1,358-day hole; no rows for 2019–2021 |
| Calendar-aware session completeness | UNKNOWN / NOT_VERIFIED | Official Mumbai holiday calendar and expected publication-session join not completed |
| Source transaction metadata / retrieval headers | NOT_CAPTURED | User screenshots + payload; no independently captured HTTP request/response headers |
| FBIL historical full-archive certification | BLOCKED | The saved file is incomplete for the requested full historical window |
| Interbank OHLC / DXY / carry | NOT_ACCEPTED | Reference fixing is not an OHLC/carry series |

The earlier C282 minimum-count and minimum-span checks remain true as narrow arithmetic checks, but they do NOT establish continuous coverage. C282's broad phrase “captured/validated reference-rate payload for research staging” is narrowed by this C283 audit: retain as a partial raw source extract only; do not label as full-history accepted, complete, production-ready, or a complete 2018–2026 FBIL panel.

## 6. Official source semantics and next executable action
- RBI confirms FBIL assumed computation/dissemination of the USD/INR reference rate from 10-Jul-2018 and that it is published on weekdays excluding Mumbai bank holidays. Official source: https://www.rbi.org.in/Scripts/BS_PressReleaseDisplay.aspx?prid=44393.
- FBIL's official website currently exposes recent INR/1 USD observations, but the exact historical export route and a complete 2018–2026 payload are not yet verified: https://www.fbil.org.in/.
- Next action: obtain the complete original FBIL daily reference-rate history from the official FBIL route (or an official RBI/FBIL export with documented coverage) and attach/capture the exact unmodified payload. Compare it against the present partial extract; preserve both originals and hashes; never overwrite the partial file.
- Then join dates to an authoritative Mumbai bank-holiday/publication calendar, enumerate expected FBIL publication sessions, and classify each absent date as observed / official holiday / unresolved / true missing. No weekend-only proxy calendar, interpolation, forward-fill or synthetic rows.
- Do not retry the same RBI form extraction path unless a genuinely new official, executable download route is identified.

## 7. Project state and constraints
- USD/INR reference-rate source family: official source identity CONFIRMED; this particular payload's raw integrity PASS; full-history continuity FAIL; final ingestion status BLOCKED / UNKNOWN.
- FPI/DII remains a separate P0 blocker under C279/C280 reuse/permission boundary; do not substitute NSE provisional data or CDSL FPI for DII.
- Macro-Geo P0 remains last artifact-backed 6/8; strict GCR hard gate BLOCKED; `candidate_release_allowed=false`; overall GCR NOT_COMPUTABLE / NOT_CERTIFIED.
- ₹0 spend; official/free sources only; no third-party mirror, no paid API, no credential bypass, no external contact, no synthetic rows or imputation. UNKNOWN is neither PASS nor FAIL.
- CORE-672 (56×12), Engines A–E, Production Selector, `RANKING_SCORE`, `+1 PRESSURE_FADE`, IPO-PLX V2.0 and all production logic remain unchanged.
