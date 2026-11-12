# RBI DBIE USD-INR discrepancy — independent secondary cross-check
Date: 2026-11-11

## Purpose
Test whether the DBIE grid count of 6,308 has any independent corroboration, without promoting a secondary mirror to an official source or closing the discrepancy.

## Evidence
1. Official DBIE table page for `financial_markets.r691_daily_interbank_forex_rates_usd_vis_a_vis_inr` reports:
   - Period: 08-08-2000 to 30-06-2026
   - Metadata row count: 6,319
   - Grid pagination: 1 to 50 of 6,308 (127 pages)
   - Columns: Date, Interbank Open/High/Low/Close Rate, RBI Reference Rate
   Official URL: https://dbie.rbihub.in/tables?table=financial_markets.r691_daily_interbank_forex_rates_usd_vis_a_vis_inr
2. Independent secondary mirror Dataful reports 6,308 rows, seven columns, same dataset title and period 2000–2026, and last updated 30 October 2026. It also reports field-level missing counts for some rates. This corroborates the grid count but is not an RBI primary artifact and does not prove that 6,308 is the correct complete raw export count.
   URL: https://dataful.in/datasets/17545/
3. DBIE's own documentation says the public read-only CSV endpoint returns the full table with no row limit, and API responses are cached for five minutes. It also says the data reflect the last scrape, not a live feed.
   URL: https://dev.dbie.rbihub.in/docs/using-the-site
4. Direct retrieval of DBIE metadata/CSV API through the current web retrieval channel returned an internal retrieval error. This is not evidence that the endpoint is down.
5. RBI Reference Rate Archive is an official separate source with an Excel download interface. It can potentially validate the RBI Reference Rate column for overlapping dates, but it is not an interchangeable source for interbank Open/High/Low/Close.
   URL: https://www.rbi.org.in/Scripts/ReferenceRateArchive.aspx

## Assessment
- 6,308 is independently corroborated by a secondary mirror and by the official DBIE grid pagination.
- 6,319 remains displayed in official DBIE metadata.
- Cause of the 11-row mismatch remains UNKNOWN.
- The Dataful mirror is not accepted as an official raw source, replacement, or evidence of the missing 11 rows.
- The RBI archive offers a semantically narrower cross-check for the reference-rate field only; it cannot validate the four interbank OHLC fields.

## Next acceptance actions
1. Acquire the official DBIE full CSV bytes from the documented CSV route and preserve the response unchanged.
2. Capture retrieval UTC timestamp, HTTP status, content type, byte count, and SHA-256.
3. Count parsed data records and unique dates independently; compare with both 6,308 and 6,319.
4. If raw count is 6,308, reconcile the 11 metadata-only records using source provenance or row-level evidence; do not fabricate or silently drop.
5. If raw count is 6,319, inspect duplicates, blank rows, invalid dates, and pagination behavior before accepting.
6. Separately compare the RBI Reference Rate column to RBI's archive for matched dates; do not compare OHLC fields to reference-rate-only observations.

## Gate
- Official source identity and documented CSV semantics: PASS.
- Secondary corroboration of 6,308: PASS (context only; not primary evidence).
- 11-row discrepancy cause: UNKNOWN.
- Raw official CSV acquisition and SHA-256: NOT DONE.
- Row-level QA and RBI archive reconciliation: NOT DONE.
- USD/INR ingestion: BLOCKED.
- Overlay actual global-macro ingestion remains 0%; overlay overall remains 62.5%.

## Safety invariants
No synthetic observations, no fabricated timestamps, no silent row deletion, no forward fill. ₹0 spend; free sources only. No production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A–E, or Hard Gate changes. Research-only.