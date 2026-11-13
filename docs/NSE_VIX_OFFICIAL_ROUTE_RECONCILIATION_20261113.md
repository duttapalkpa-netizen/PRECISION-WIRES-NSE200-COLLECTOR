# NSE India VIX Official Route Reconciliation — 2026-11-13

## Scope
Reconcile the official NSE historical reports index, its India VIX link, and the dedicated India VIX historical page. This is source-navigation and access-state evidence only; no raw observations are accepted.

## Official route chain
1. NSE Historical Reports index:
   https://www.nseindia.com/static/resources/historical-reports-capital-market-daily-monthly-archives
2. The index labels an "Indices" subsection and provides a distinct "Historical Data - India Vix" link.
3. That official link resolves to:
   https://www.nseindia.com/reports-indices-historical-vix
4. The destination page exposes 1D, 1W, 1M, 3M, 6M, 1Y, Custom, Clear controls and a Download (.csv) control. Its currently extracted rendered state shows the expected columns but "No Records".

## Freshness metadata
The historical reports index footer displays "Updated on: 10/08/2026". The page was crawled on 2026-11-13, but the displayed update date is older than the audit date. This is page-level freshness metadata only; it does not establish the last update time of the India VIX data endpoint.

## Cross-route conclusion
- The All Reports page contains a separate India VIX date-range UI and rendered sample block, but prior audits found that sample block internally inconsistent (heading 01-01-2019 to 05-01-2019; repeated row dated 03-Sep-2018).
- The Historical Reports index independently confirms that NSE routes users to the dedicated historical India VIX page.
- The dedicated page has a CSV download control and date-range controls, but the inspected extracted state shows "No Records".
- The index route and dedicated page therefore confirm official source identity and user-facing navigation, but do not establish successful query execution, raw CSV availability, or valid historical coverage.

## Evidence ledger
| Check | Status |
|---|---|
| Official NSE historical reports index | PASS |
| Explicit India VIX link on index | PASS |
| Link resolves to dedicated NSE India VIX page | PASS |
| Dedicated page date-range controls | PASS |
| Dedicated page CSV control | PASS |
| Index page displayed update date | PASS (10-Aug-2026 metadata) |
| Dedicated page rendered records | NONE IN INSPECTED STATE |
| Actual user-selected date-range query | NOT EXECUTED |
| Raw CSV bytes / SHA-256 | NOT ACQUIRED / UNKNOWN |
| Historical schema and coverage QA | NOT STARTED |

## Gate
**SOURCE IDENTITY PASS; RAW DATA INGESTION BLOCKED.** Do not treat the stale All Reports sample or the dedicated page's empty extracted state as data. Next valid step is an actual browser interaction with a bounded date range and download, followed by raw-byte preservation and QA. Do not guess undocumented endpoints.

## Invariants
₹0 spend; official free NSE source only; no synthetic data/timestamps; UNKNOWN is neither PASS nor FAIL; Production Selector, RANKING_SCORE, +1 PRESSURE_FADE and CORE-672 unchanged; no PR merge. Research-only.
