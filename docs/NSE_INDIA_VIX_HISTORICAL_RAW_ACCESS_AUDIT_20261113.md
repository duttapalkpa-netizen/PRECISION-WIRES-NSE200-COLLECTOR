# NSE India VIX Historical Raw-Access Audit — 2026-11-13

## Scope
Bounded source-access audit for the Global Capital Rotation Overlay. This is not a raw-data acquisition, factor validation, or production change.

## Official source evidence
- NSE historical India VIX page: https://www.nseindia.com/reports-indices-historical-vix
- NSE all-reports page: https://www.nseindia.com/all-reports
- NSE India VIX product/methodology page: https://www.nseindia.com/static/products-services/indices-indiavix-index
- Audit date: 2026-11-13 (IST context).

The NSE historical India VIX page exposes date-range controls (1D, 1W, 1M, 3M, 6M, 1Y, Custom, Clear) and a Download (.csv) control. The currently rendered page did not return historical rows in the inspected default state. This is a UI state observation only; it does not prove the endpoint is unavailable.

The visible historical table schema is:
Date, Open, High, Low, Close, Prev. Close, Change, % Change.

NSE describes India VIX as an annualized near-term expected volatility measure derived from NIFTY options order-book prices, representing expected volatility over the next 30 calendar days. This is a market-implied volatility indicator, not realized volatility.

## Evidence classification
| Check | Status | Reason |
|---|---|---|
| Official NSE source identity | PASS | Official NSE historical India VIX page and product page identified |
| Historical date-range UI | PASS | Range controls and Custom option visible |
| CSV export control | PASS | Download (.csv) control visible |
| Raw response bytes acquired | NOT STARTED | No CSV bytes obtained in this audit |
| Raw SHA-256 | UNKNOWN | No raw file to hash |
| Date coverage / row count | UNKNOWN | No data rows returned in inspected default page state |
| Schema validation | NOT STARTED | UI column labels only; no CSV header/rows inspected |
| Duplicate-date / OHLC validation | NOT STARTED | Requires raw rows |
| PIT / publication timestamp validation | UNKNOWN | Not established by page UI |
| Factor efficacy / backtest acceptance | NOT STARTED | Out of scope |

## Safe acquisition protocol
1. Use the official NSE historical India VIX page and explicitly select a bounded date range (start/end); do not assume the default blank state represents an empty historical series.
2. Trigger NSE's own CSV download control. Do not substitute third-party mirrors or undocumented endpoints.
3. Preserve original bytes unchanged. Record retrieval timestamp (IST and UTC), requested date range, source URL, response headers if available, byte count, and SHA-256 before parsing.
4. Validate CSV file signature/encoding, exact header, date parseability, unique dates, numeric OHLC/previous-close/change/%change fields, and OHLC consistency. Keep missing values as missing; do not impute.
5. Reconcile date coverage against NSE trading sessions and document any gaps; distinguish trade date from retrieval/publication timestamp.
6. Store raw and normalized artifacts separately with immutable manifest entries.

## Gate decision
**BLOCKED for raw-data acceptance.** Source identity and user-facing export mechanism are confirmed, but raw CSV bytes, hash, schema, row count, and date coverage have not been acquired or validated. Do not promote this source to a fully available factor input until those checks pass.

## Project invariants
No paid source, spend, synthetic data, fabricated timestamps, production selector/ranking changes, CORE-672 changes, or PR merge. UNKNOWN remains neither PASS nor FAIL. This document is research-only.
