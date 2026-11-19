# GCR — NSE Historical Index / India VIX Sample Integrity Review (Continuation 42, Part-6)
Date: 2026-11-19
Stage: OBSERVATION ONLY
Decision: OFFICIAL ROUTES EXIST; SERVER-RENDERED SAMPLE IS NOT ACCEPTABLE AS A RAW HISTORICAL DATASET.

## 1. Purpose
Reconcile the Part-5 source-route gate against the official NSE All Reports page, which renders example rows for historical index and India VIX sections. This is a source-integrity review, not a raw download or event study.

## 2. Exact observations on official NSE All Reports page
Official URL: https://www.nseindia.in/all-reports
- Historical Index Data section appears at the page's Historical Index Data area.
- It displays a heading: Historical Data for NIFTY 50 for period 01-01-2019 to 05-01-2019.
- Displayed NIFTY row: 01-Jan-2019, Open 10881.70, High 10923.60, Low 10807.10, Close 10910.10, Shares Traded 159404542, Turnover 8688.26 Cr.
- The same row is rendered twice in the captured page output.
- Historical Data - India Vix section displays a heading for period 01-01-2019 to 05-01-2019.
- Displayed India VIX row date is 03-Sep-2018 (Open 12.5975, High 13.7175, Low 11.1700, Close 13.3925, Prev Close 12.5975, Change 0.8000, %Change 6.31).
- The same India VIX row is rendered twice. Its date is outside the heading's stated Jan-2019 range.
- The page provides From/To/View Data controls and Multiple file Download controls; the static server-rendered extract does not demonstrate that the selected period was queried in this run.

## 3. Interpretation and correction to Part-5 wording
- Correct: the official NSE pages and UI routes exist for historical NIFTY/index and India VIX data.
- Correct: selected-range CSV acquisition has not been completed or verified.
- Important qualification: the All Reports page's pre-rendered sample block contains duplicate rows; India VIX sample date is inconsistent with the heading range. Treat these as UI/sample rendering anomalies until the live date-range query and download are independently verified.
- Do not call these two rows an acquired historical dataset, do not infer endpoint behaviour from them, and do not calculate returns/volatility from the sample.
- Part-5's statement that a server-rendered page showed no selected data remains true for the dedicated historical pages, but All Reports has separate pre-rendered example blocks. This Part-6 supersedes any broad interpretation that no sample data is rendered anywhere.

## 4. Acceptance gate strengthened
For a future official export, require:
1. Explicit user-selected From/To dates and selected instrument (NIFTY 50 Price Index, NIFTY 50 TRI, or India VIX) recorded.
2. The downloaded file itself—not webpage example text—must be archived as raw bytes.
3. Raw CSV row dates must fall within the requested date range; duplicates must be counted and explained, not silently deduplicated.
4. For NIFTY, validate monotonic dates, unique trading dates, OHLC bounds and index type.
5. For India VIX, validate monotonic dates, unique trading dates, positive values and date-window match; preserve published percent/index units.
6. Record retrieval timestamp, final URL, content type, byte count, SHA-256, row count, first/last dates and parser version.
7. Cross-check a sample of dates against a second official NSE/NSE Indices route if available.
8. Reject stale, mismatched or duplicated sample payloads pending reconciliation.

## 5. Current status
| Gate | Status |
|---|---|
| Official NIFTY historical UI route | VERIFIED |
| Official India VIX historical UI route | VERIFIED |
| Static NIFTY example block internally clean | NOT PASS (duplicate row in rendered sample) |
| Static India VIX example date matches heading | NOT PASS (date outside heading window) |
| Live selected-range NIFTY CSV acquired | NOT_DONE |
| Live selected-range India VIX CSV acquired | NOT_DONE |
| Raw hashes / row counts / missingness | UNKNOWN |
| GCR event-study India outcome panel | NOT_ACCEPTED |

## 6. Primary source
NSE India All Reports, Historical Index Data and Historical Data - India Vix sections: https://www.nseindia.in/all-reports
Supporting official pages:
- https://www.niftyindices.com/reports/historical-data
- https://www.nseindia.in/reports-indices-historical-vix

## 7. Stage and invariants
This review strengthens source acceptance criteria only. Observation overall OPEN; Planning/Organizing NOT STARTED; GCR NOT COMPLETE; aggregate/production admission NOT_AUTHORIZED.
₹0; official/free sources only; no synthetic data, fabricated timestamps, guessed endpoints, silent deduplication, forward-fill or interpolation. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E unchanged. UNKNOWN is never PASS.
