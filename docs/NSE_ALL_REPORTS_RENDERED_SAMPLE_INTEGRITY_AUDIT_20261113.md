# NSE All Reports Rendered Historical-Sample Integrity Audit — 2026-11-13

## Scope
Cross-sectional audit of the server-rendered historical sample blocks on NSE All Reports. This follows the India VIX alternate-route audit and tests whether the displayed sample blocks can be treated as actual query results. No user-interactive date query or file download was executed.

## Official source
https://www.nseindia.com/all-reports

## Observations from the rendered page
The page contains multiple historical sections with headings describing selected periods and accompanying sample rows. Several show repeated rows:
- Historical Data - India VIX heading: 01-01-2019 to 05-01-2019; visible row dates: 03-Sep-2018, repeated twice with identical OHLC and change values.
- Historical Data for NIFTY 50 heading: 01-01-2019 to 05-01-2019; visible row date: 01-Jan-2019, repeated twice with identical values.
- Historical Data for NIFTY 50 Total Returns Index heading: 01-01-2019 to 05-01-2019; visible row date: 01-Jan-2019, repeated twice.
- Historical NIFTY 50 P/E, P/B & Div. Yield block for 01-01-2019 to 05-01-2019 shows 01-Jan through 04-Jan rows, illustrating that not every section has the same mismatch pattern.
- Other unrelated sample blocks also contain repeated identical rows, e.g. SBIN security-wise price-volume data and SBIN high/low data.

## Interpretation
The rendered page is not a trustworthy raw-data response for the India VIX query. It appears to contain stale, repeated, or example content in multiple sections. However, without submitting a new date-range query through the live UI and inspecting the resulting download, it is not possible to conclude whether the backend query itself is defective.

Therefore:
- Do not parse the rendered HTML table as historical VIX observations.
- Do not use the duplicate sample rows as data.
- Do not infer that the underlying NSE endpoint is broken or that the actual query returns the same sample.
- Require an interactive, bounded date-range query and original downloaded file bytes before acceptance.

## Data integrity acceptance rules
For every selected query:
1. Every returned date must fall inside the requested interval.
2. Dates must be unique unless the official schema defines a valid key with multiple records per date.
3. Header and numeric fields must match the documented series.
4. OHLC invariants: Low <= min(Open, Close) and High >= max(Open, Close); all values finite and non-negative.
5. Change must reconcile to Close minus Prev. Close within the published rounding precision; percentage change must reconcile to Change / Prev. Close × 100 within rounding tolerance.
6. Record exact query range, source URL, retrieval time, response status/content-type, file size and SHA-256 before parsing.
7. Preserve original bytes and never silently deduplicate, impute, or rewrite source rows.

## Evidence status
| Item | Status |
|---|---|
| Official All Reports page identity | PASS |
| Multiple historical sample sections inspected | PASS |
| Rendered India VIX sample date-range mismatch | FAIL (rendered sample only) |
| Repeated identical sample rows observed | FAIL (rendered sample only) |
| Actual interactive VIX query executed | NOT EXECUTED |
| Raw VIX download acquired | NOT ACQUIRED |
| Raw SHA-256 / schema / coverage | UNKNOWN |
| Production factor acceptance | BLOCKED |

## Gate
**Rendered sample blocks rejected as raw evidence.** India VIX historical source remains unqualified for ingestion pending a real user-selected query and downloaded raw file validation.

## Invariants
₹0 spend; free official NSE source only; no synthetic rows/timestamps; UNKNOWN is neither PASS nor FAIL; production selector, RANKING_SCORE, +1 PRESSURE_FADE and 56×12 CORE-672 unchanged; no PR merge. Research-only.
