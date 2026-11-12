# RBI DBIE USD-INR row-count and data-vintage discrepancy audit
Date: 2026-11-11
Scope: independent reconciliation of official DBIE table metadata versus grid pagination and API semantics. No raw observations ingested.

## Finding 1 — row-count discrepancy (must remain unresolved)
The official DBIE table page for `financial_markets.r691_daily_interbank_forex_rates_usd_vis_a_vis_inr` currently exposes both:
- Header metadata: Period 08-08-2000 to 30-06-2026; Rows = 6,319.
- Grid pagination text: 1 to 50 of 6,308; Page 1 of 127.
- Difference: 11 rows.
These are two distinct displayed counts on the same official table view. The source page does not explain the 11-row difference in the retrieved evidence.
Decision: do NOT hardcode 6,319 as the accepted export row count; do NOT assume 6,308 is correct either. Keep expected row count UNKNOWN pending actual full CSV bytes and independent row-key QA. Do not delete or synthesize 11 rows.

Official table page: https://dbie.rbihub.in/tables?table=financial_markets.r691_daily_interbank_forex_rates_usd_vis_a_vis_inr

## Finding 2 — data vintage is not necessarily live
Official DBIE documentation states that API responses are cached for five minutes and that DBIE content reflects the last scrape of the DBIE portal, not a live feed. The source is therefore a periodically loaded/scraped snapshot, not a guaranteed live RBI feed.
Documentation: https://dev.dbie.rbihub.in/docs/using-the-site
Consequences:
- Preserve DBIE load/snapshot vintage if supplied in table provenance.
- Do not infer that a 2026-11-11 retrieval means the latest observation is 2026-11-11.
- The currently displayed last period remains 2026-06-30 in the retrieved table metadata.
- Record retrieved_at separately from source_as_of / latest observation date.

## Finding 3 — documented API semantics
DBIE documentation states:
- Public read-only GET API, no key required.
- Table metadata route `/api/tables/{schema}/{table}`.
- Rows route supports equality filters, `from`, `to`, `order`, `limit`, `offset`, `labels=1`.
- CSV route returns full table or filtered slice with no row limit.
- API results are cached for five minutes.
Exact candidate CSV endpoint:
https://data-api.dbie.rbihub.in/api/tables/financial_markets/r691_daily_interbank_forex_rates_usd_vis_a_vis_inr/csv
An attempted web retrieval of the metadata and CSV endpoint returned an internal retrieval error. This is a limitation of that retrieval environment, not proof of RBI/DBIE endpoint failure.

## Required acceptance test when raw CSV is available
1. Save response bytes unchanged; capture exact URL, UTC retrieval time, status, content type, byte count and SHA-256.
2. Parse with original header retained. Count physical data records independently.
3. Compare raw record count to both published counts (6,319 and 6,308); report discrepancy, never silently normalize.
4. Check date range, unique dates, duplicate dates, nulls, numeric fields, ordering and non-business-day calendar.
5. Compare row keys and selected values to DBIE paginated rows and the official RBI reference-rate archive where comparable; do not equate interbank OHLC with RBI reference rate.
6. Preserve source snapshot and any later correction as separate immutable vintages.

## Gate decision
- DBIE source identity and API semantics: PASS.
- Displayed row-count consistency: FAIL / discrepancy detected (11 rows), cause UNKNOWN.
- Data vintage semantics: PASS (cached last-scrape snapshot; not live).
- Full raw CSV acquisition: NOT DONE.
- Raw SHA-256 and row-level QA: NOT DONE.
- USD-INR ingestion gate: BLOCKED pending raw CSV and row-count reconciliation.
- Overlay Milestone 6 actual ingestion: remains 0%; overlay overall remains 62.5% (5/8).

## Invariants
No synthetic rows, no deleting unmatched rows, no fabricated timestamps, no forward fill. ₹0 spend; free official sources only. No production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A-E, or Hard Gate changes. Research-only.