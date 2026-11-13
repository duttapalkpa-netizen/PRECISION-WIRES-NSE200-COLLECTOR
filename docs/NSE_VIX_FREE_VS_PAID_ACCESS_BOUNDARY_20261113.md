# NSE India VIX Free Web Route vs Paid Historical Feed Boundary — 2026-11-13

## Purpose
Resolve a source-governance risk discovered during repeated India VIX retrieval audits: distinguish NSE's free public web pages and controls from NSE Data & Analytics paid EOD/historical data products. No purchase, contact, or paid access attempted.

## Official free public web route
- NSE All Reports: https://www.nseindia.com/all-reports
- Dedicated Historical India VIX page: https://www.nseindia.com/reports-indices-historical-vix
- NSE India VIX methodology/product description: https://www.nseindia.com/static/products-services/indices-indiavix-index

The public NSE pages expose a historical India VIX date-range UI and CSV download control. Their rendered snapshots have already been audited and found insufficient as raw data: All Reports shows an inconsistent example block, while the dedicated page's inspected state shows No Records. Actual user-submitted date-range response and CSV bytes remain unacquired.

## Paid product boundary
NSE Data & Analytics' official EOD/Historical Data product page describes downloadable EOD and historical data products, including index value information in the Capital Market segment. The page explicitly lists a tariff/download and asks users to contact marketdata@nse.co.in for subscription. This is a paid product route and is excluded under the project's ₹0 / free-official-source constraint.

The paid product page is:
https://betanseapi.nseindia.com/static/market-data/eod-historical-data-subscription

The NSE realtime index feed specification describes EOD index information fields including date, index name, opening, closing, high, low, and previous close. This is a product specification, not evidence that a free downloadable historical archive is available.

## Governance decision
1. The public NSE historical web UI remains the only eligible India VIX acquisition route identified in this audit.
2. The paid NSE Data & Analytics EOD/historical feed is explicitly OUT OF SCOPE and must not be used, subscribed to, or contacted.
3. Do not use third-party mirrors as official raw source.
4. Do not promote rendered sample rows to raw observations.
5. If the public web UI cannot produce a bounded date-range CSV, record the source as blocked for ingestion; do not bypass the paywall or infer an undocumented endpoint.

## Evidence ledger
| Item | Status |
|---|---|
| Free official public page identity | PASS |
| Public UI exposes date controls and CSV control | PASS |
| Public raw CSV successfully acquired | NOT ACQUIRED |
| Paid EOD/historical product identified | PASS |
| Paid product excluded under ₹0 rule | PASS |
| Third-party mirrors excluded | PASS |
| Historical raw SHA-256 / coverage | UNKNOWN |
| Factor input acceptance | BLOCKED |

## Next action
Only test the public NSE web UI using a real bounded date query in a browser that supports the site's interaction and file download. Preserve raw bytes and metadata, hash before parsing, then validate date range, uniqueness, OHLC and overlap with the dedicated VIX route. If the UI does not return a downloadable file, stop and retain BLOCKED; do not substitute the paid feed.

## Invariants
₹0 spend; free official sources only; no paid API/feed or external contact; no synthetic rows or timestamps; UNKNOWN is neither PASS nor FAIL; Production Selector, RANKING_SCORE, +1 PRESSURE_FADE and 56×12 CORE-672 unchanged; no PR merge. Research-only.
