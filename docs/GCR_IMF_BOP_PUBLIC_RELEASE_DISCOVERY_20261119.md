# GCR — IMF BOP public release discovery (2026-11-19)

## Purpose
Continue the blocked IMF BOP observation access work by inspecting the official dataset page's non-API routes and the related official BOP/IIP World and Country Group Aggregates release. This is a source-access audit, not an observation panel.

## Verified official sources
1. IMF Balance of Payments (BOP) dataset:
   - https://data.imf.org/en/datasets/IMF.STA%3ABOP
   - Static page exposes `API`, `VIEW DATA`, and `DOWNLOAD` controls.
   - Frequency: annual and quarterly.
   - Publisher: IMF Statistics Department.
   - Static page extraction exposes no direct file URL for the View Data/Download controls. The API link remains routed to the API portal sign-in described in the prior access-boundary note.
2. IMF Balance of Payments and International Investment Position Statistics (BOP/IIP), World and Country Group Aggregates (BOPSY):
   - https://data.imf.org/en/datasets/IMF.STA%3ABOP_AGG
   - Official page states annual frequency and November release cadence.
   - Latest updates visible on 2026-11-19: BOPSY Dashboard release (18 Nov 2026) and BOPSY Explanatory Notes November 2026.
   - Dashboard: https://data.imf.org/en/dashboards/bopsy%20dashboard
   - Explanatory Notes document target exposed by IMF page: https://data.imf.org/-/media/BOPSY-Explanatory-Notes-November-2026.docx
3. IMF API documentation:
   - https://data.imf.org/en/Resource-Pages/IMF-API
   - Confirms SDMX 2.1 and 3.0 API access; Swagger explorer requires beta portal sign-in.

## Critical methodology caveat
IMF describes BOPSY country-level information as actual data reported directly to IMF or obtained from country NSDP, except IMF counterparty accounts may be replaced by Fund Accounts. World and country-group aggregates, other than Euro Area, combine reported country data with estimates for nonreporting economies, using additional sources including WEO and External Wealth of Nations. Euro Area external transactions/positions are ECB-reported.
Therefore:
- BOPSY is a legitimate official annual macro cross-check/benchmark.
- BOPSY World/Regional group aggregates are NOT pure sums of fully reported country observations and must not be used as if they were.
- BOPSY annual data are not a replacement for quarterly country-level BOP financial-account flow observations in a high-frequency capital-rotation panel.
- Country-level BOP observations and BOPSY group estimates must remain distinct datasets and source classes.
- IIP/position measures must remain separate from BOP transaction flows.

## Result / acceptance state
- Official BOP dataset page and BOPSY page discovery: PASS.
- Public static-page extraction of direct BOP dataset View Data/Download URL: NOT_RESOLVED. Buttons are present, but static extraction does not expose their destination; do not infer a download URL.
- Direct BOP observations via anonymous API: BLOCKED pending a verified public endpoint/export.
- BOPSY official aggregate as supplementary annual benchmark: ELIGIBLE_FOR_SEPARATE_VALIDATION; no numeric observations captured in this task, so data ingestion is NOT_DONE.
- No data values, API query keys, SDMX observation keys, country membership or data coverage have been fabricated.

## Next actions
1. Obtain the BOP dataset's public View Data/Download export route through browser interaction or an authenticated user export; no credentials or cookies are requested.
2. If public export is accessible, archive raw file and provenance then validate its dimensions, indicators, units, frequency, time periods, status/revision flags and source coverage against the BOP DSD.
3. Independently acquire the 2026 BOPSY dashboard/download tables if a public file route exists. Preserve country data, group estimates, world totals and Euro Area ECB series as separate source classes.
4. Keep IMF BOP quarterly portfolio investment transaction flow panel BLOCKED until data are actually captured and validated.

## Invariants
₹0, official free sources only; no guessed endpoints/keys; no synthetic observations; no CPIS/PIP substitution for BOP flows; no changes to Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 or Engines A–E; UNKNOWN is not PASS.
