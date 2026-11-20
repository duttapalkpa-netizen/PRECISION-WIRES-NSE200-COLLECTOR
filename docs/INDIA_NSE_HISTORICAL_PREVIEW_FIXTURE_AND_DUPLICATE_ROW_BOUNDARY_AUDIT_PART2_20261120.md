# India NSE Historical Preview — Fixture and Duplicate-Row Boundary Audit (Part 2)
Date: 2026-11-20 (Asia/Kolkata)
Project: PRECISION-WIRES V11.3 / India Market Transmission Benchmark Panel
Status: **OFFICIAL NSE HISTORICAL DOWNLOAD ROUTES CONFIRMED; PAGE-EMBEDDED SAMPLE ROWS REJECTED AS INGESTION EVIDENCE; RAW CSV CAPTURE NOT_DONE.**

## 1. Continuity
- Reopened the India Benchmark Panel Official Source Contract Part 1 and the GCR Master Priority Queue.
- Executed the next bounded task against NSE's official Historical Reports / All Reports pages.
- This is a preview-fixture and data-boundary audit only. No CSV or ZIP file bytes were acquired, no raw SHA-256 was generated, and no production ingestion was performed.

## 2. Official source surfaces confirmed
- NSE All Reports page exposes Historical Index Data and Historical Data - India VIX sections, date inputs, View Data controls and Multiple file Download links.
- NSE Indices Historical Data page exposes index selector, sub-index selector, date range, CSV output, OHLC rows and separate Total Returns Index / Net Total Return Index output.
- NSE Indices FAQ states NIFTY 50 historical data are available from 03-Jul-1990 and describes NIFTY and NIFTY-TR as useful research series.
- Official source URLs:
  - https://www.nseindia.in/all-reports
  - https://www.niftyindices.com/reports/historical-data
  - https://betanseapi.nseindia.com/static/products-services/indices-faqs

## 3. Critical preview-data boundary findings
- NSE All Reports page's embedded illustrative section is titled “Historical Data for NIFTY 50 for the period 01-01-2019 to 05-01-2019” but displays only 01-Jan-2019 twice with identical OHLC/activity values. This is a duplicated preview row in the page extraction; it is not proof that the downloadable source CSV contains duplicate records.
- The same page's embedded India VIX sample carries the same 2019 date-range heading but displays 03-Sep-2018 twice with identical values. That date is outside the displayed 2019 interval. This is a clear sample/preview mismatch; do not treat the embedded sample as actual query output or as 2019 observations.
- NIFTY Total Returns Index sample similarly displays 01-Jan-2019 twice. Again, page-extracted preview duplication only; downloadable CSV integrity remains untested.
- The page parser/search text also repeats some historical examples in other sections. This reinforces that extracted page text is not a raw-data receipt.
- Therefore, no sample values, duplicate rows, or date range from the embedded page preview are admitted into the benchmark panel. Only the actual date-filtered downloadable CSV/XLSX/ZIP payload can establish data content.

## 4. Research implications and ingestion QA contract
1. A successful HTTP/page render is not a successful historical-data capture.
2. The downloader must record the exact requested index identifier, from/to dates, selected report type, and returned file name.
3. Validate payload signature and MIME against actual bytes; reject HTML pages returned in place of CSV/XLSX/ZIP.
4. Parse the actual payload, then test:
   - date parsing and timezone/session key;
   - requested interval coverage;
   - sorted dates;
   - duplicate dates (exact duplicate vs conflicting duplicate);
   - missing NSE sessions against official trading calendar;
   - numeric parse, OHLC constraints (low <= open/close <= high), nonnegative shares/turnover;
   - index identity and price-index vs TRI distinction;
   - row count, file byte count, SHA-256 and parser version.
5. Do not automatically drop duplicates. Exact duplicates must be reported and quarantined until raw payload provenance determines whether the source itself duplicates or the page/rendering layer duplicates.
6. For India VIX, require the returned observation dates to fall within the requested range; reject stale cached fixture rows.
7. Keep NIFTY price index, NIFTY TRI and NIFTY NTRI as distinct series. Do not concatenate or substitute them.
8. No forward-fill for absent sessions; reconcile against NSE holiday/trading calendar.

## 5. Acceptance matrix
| Gate | Status |
|---|---|
| Part-1 source contract reopened | PASS |
| Official NSE All Reports route | PASS |
| Official NSE Indices CSV route | PASS |
| Official NIFTY historical availability from 03-Jul-1990 | PASS |
| Embedded NIFTY preview rows as raw evidence | REJECTED |
| Embedded India VIX preview rows as raw evidence | REJECTED |
| Embedded TRI preview rows as raw evidence | REJECTED |
| Actual date-filtered NIFTY CSV bytes | NOT_CAPTURED |
| Actual date-filtered India VIX CSV bytes | NOT_CAPTURED |
| Raw SHA-256 manifest | NOT_DONE |
| Duplicate-date result on actual payload | NOT_TESTED |
| Missing-session/holiday QA | NOT_DONE |
| Synchronized benchmark panel | NOT_DONE |
| Event study / causal validation | NOT_DONE |
| Production use | NOT_AUTHORIZED |

## 6. Next exact action
- Capture actual NSE Indices CSV payloads (not embedded preview) in a small isolated run for NIFTY 50, one broad-market companion index, and India VIX over a fixed short date window with official trading sessions.
- Save raw bytes, response metadata, requested parameters and SHA-256 before parsing.
- Run date-range, exact/conflicting duplicate, missing-session, schema and OHLC checks. Keep TRI/NTRI separate.
- If NSE endpoint rejects automated access or returns HTML, stop retries and use the official manual Multiple file Download route; do not scrape or infer an undocumented API.
- Only after actual payload QA passes should the same method be expanded to selected sector indices.

## 7. Protected invariants
No sample fixture values, synthetic data, fabricated timestamps, forward-fill, silent deduplication, silent TRI substitution, paid data, or production changes. Do not modify the fixed 63-country IMF cohort, Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E, IPO-PLX V2, weights, trade gates or alert behavior. UNKNOWN is never PASS.

## Sources
- NSE All Reports: https://www.nseindia.in/all-reports
- NSE Indices Historical Data: https://www.niftyindices.com/reports/historical-data
- NSE Indices FAQs: https://betanseapi.nseindia.com/static/products-services/indices-faqs
