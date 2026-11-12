# FRED full-table access and RBI DBIE API route verification
Date: 2026-11-11
Scope: exact public access routes and table metadata verified. This is not raw-byte ingestion.

## A. FRED full observation table route — verified
FRED exposes full table-data pages at:
- https://fred.stlouisfed.org/data/DTWEXBGS
- https://fred.stlouisfed.org/data/DTWEXAFEGS
- https://fred.stlouisfed.org/data/DTWEXEMEGS

Verified page metadata on all three:
- Source: Board of Governors of the Federal Reserve System (US)
- Release: H.10 Foreign Exchange Rates
- Frequency: Daily
- Units: Index Jan 2006=100
- Date range: 2006-01-02 to 2026-11-06
- Last updated: 2026-11-09 3:16 PM CST
- Table columns: DATE, VALUE
- Pages expose historical table rows beginning 2006-01-02, not only the chart preview.

## B. FRED retrieval semantics
- FRED series are subject to revision; pin retrieval timestamp and retain immutable snapshots.
- Public table page is not evidence of a locally downloaded raw file. Do not assign a local-file SHA-256.
- The official FRED API observations endpoint requires an API key. Do not insert demonstration keys or bypass access.
- Preserve missing values shown as '.' and non-business-day calendar semantics; no forward fill.

## C. RBI DBIE — public API route
Official table page:
https://dbie.rbihub.in/tables?table=financial_markets.r691_daily_interbank_forex_rates_usd_vis_a_vis_inr

Official DBIE documentation states that the public read-only API is https://data-api.dbie.rbihub.in and provides metadata, paged rows and full CSV routes. Full CSV supports all rows without a row limit.

Exact table CSV route:
https://data-api.dbie.rbihub.in/api/tables/financial_markets/r691_daily_interbank_forex_rates_usd_vis_a_vis_inr/csv

Official table metadata:
- Daily interbank forex rates (USD vis-a-vis INR)
- Period: 2000-08-08 to 2026-06-30
- 6,319 rows; daily; source RBI
- Fields: Date, Interbank Open, High, Low, Close, RBI Reference Rate
- CSV and JSON download controls visible.

Retrieval boundary:
- API documentation and table page are discoverable.
- Opening the CSV endpoint through this web retrieval environment returned an internal retrieval error. This is not evidence the RBI endpoint is down.
- No raw CSV bytes, local file, retrieval timestamp, byte count or SHA-256 were obtained.
- Documentation describes the endpoint as public, read-only GET, no API key. Use a normal TLS-validating client and inspect the response.

## D. Gate
| Check | Status |
|---|---|
| Three FRED full table URLs and metadata | PASS |
| FRED historical observation pages available | PASS |
| RBI official table metadata and 6,319-row coverage | PASS |
| RBI documented full CSV endpoint | PASS |
| Raw bytes saved locally | NOT DONE |
| SHA-256 for raw bytes | NOT DONE |
| Full row-level QA | NOT DONE |
| Cross-source date/value reconciliation | NOT DONE |
| Daily panel ingestion | NOT DONE |

## E. Exact next-run protocol
1. Retrieve the three FRED table pages or official downloadable series data through normal public access. Preserve raw response bytes and hash before parsing.
2. Retrieve RBI full CSV endpoint with a normal TLS-verifying HTTP client. Save bytes unchanged and hash before parsing.
3. Verify HTTP status, content type, bytes, header/schema and source metadata.
4. Confirm date ranges and row counts; preserve '.'/blank/missing values.
5. Check unique dates, sorting, duplicate keys, numeric parse errors and coverage gaps.
6. Cross-check latest observations against official table metadata and release date.
7. Keep each source vintage immutable; do not forward-fill holidays or fabricate calendar rows.
8. Only after QA, create a derived date-keyed panel. Keep US index dates and India FX dates in separate source calendars; join only exact dates with explicit unmatched rows.

## F. Guardrails
No production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A-E or Hard Gate changes. No production integration. No synthetic data, fabricated timestamps, paid feeds or spend. Research-only.