# NSE India VIX All-Reports Cross-Check — 2026-11-13

## Objective
Cross-check the previously audited NSE Historical Data - India VIX page against the separate official NSE All Reports page. This is a bounded source/UI integrity audit, not raw-data acceptance.

## Official routes
1. Dedicated historical page: https://www.nseindia.com/reports-indices-historical-vix
2. All Reports page: https://www.nseindia.com/all-reports
3. NSE India VIX definition/methodology page: https://www.nseindia.com/static/products-services/indices-indiavix-index

## New finding
The official All Reports page contains a separate section titled "Historical Data - India Vix" with From, To, and View Data controls. It is therefore an additional official user-facing retrieval route beyond the dedicated historical page's date-range UI.

The rendered All Reports page currently labels its sample result:
"Historical Data for India VIX for the period 01-01-2019 to 05-01-2019"
but the visible sample rows carry date 03-Sep-2018, and the same row is duplicated twice:
03-Sep-2018 | Open 12.5975 | High 13.7175 | Low 11.1700 | Close 13.3925 | Prev. Close 12.5975 | Change 0.8000 | % Change 6.31

This mismatch is a **rendered-page sample integrity warning**. It does not establish that a user-selected query for 01–05 Jan 2019 would return those rows; the page may be exposing stale/example content in its server-rendered snapshot. No CSV download was performed and no raw bytes were received.

## Evidence classification
| Check | Status | Evidence |
|---|---|---|
| Dedicated NSE historical India VIX route | PASS | Official page identified |
| Separate All Reports India VIX route | PASS | Official page section and From/To/View Data controls visible |
| Displayed sample date range consistency | FAIL (sample only) | Heading 01–05 Jan 2019; rows dated 03-Sep-2018 |
| Displayed sample uniqueness | FAIL (sample only) | Identical row repeated twice |
| Actual selected-range query executed | NOT EXECUTED | Web-rendered controls cannot submit user interaction |
| Raw CSV bytes acquired | NOT ACQUIRED | No file bytes returned |
| Raw SHA-256 | UNKNOWN | No raw file |
| Actual date coverage / row count | UNKNOWN | No query response |
| Production data acceptance | BLOCKED | Must not promote sample rows |

## Correct next retrieval protocol
1. In a browser/network-enabled environment, open the official All Reports page.
2. In the specific "Historical Data - India Vix" section, set a bounded date interval (first test a short known trading-day interval, then a longer interval).
3. Submit View Data and verify every returned row date lies within the requested interval.
4. Use the section's Multiple file Download control (if exposed after query) and preserve the exact CSV bytes.
5. Record query interval, request/retrieval timestamp, response headers, byte count, and SHA-256 before parsing.
6. Validate header, date range, unique dates, numeric OHLC fields, and consistency of Change = Close - Prev. Close (subject to published rounding). Do not accept duplicate rows without source-backed explanation.
7. Compare the selected-range response with the dedicated historical VIX route for overlapping dates. Preserve both originals; do not silently deduplicate or overwrite discrepancies.

## Gate decision
**SOURCE ROUTE DISCOVERY IMPROVED; RAW DATA ACCEPTANCE STILL BLOCKED.** The second official route is confirmed, but the page's rendered sample is internally inconsistent. No raw observations are accepted.

## Project invariants
₹0 spend; free official NSE sources only; no synthetic rows, inferred timestamps, or guessed endpoints; UNKNOWN is neither PASS nor FAIL; no changes to Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, or 56×12 CORE-672; no PR merge. Research-only.
