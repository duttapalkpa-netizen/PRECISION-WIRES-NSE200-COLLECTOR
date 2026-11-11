# RBI DBIE USD-INR — source authority correction and ingestion hold
Date: 2026-11-11

## Why this correction is necessary
Prior research notes described `dev.dbie.rbihub.in` / `data-api.dbie.rbihub.in` as if they were the official RBI DBIE API. That authority classification was too strong and is corrected here.

## Primary-source evidence
- RBI's own publications identify the Database on Indian Economy (DBIE) at `https://data.rbi.org.in` as the RBI's long-time-series data dissemination platform.
- RBI's older official material also identifies `https://dbie.rbi.org.in` as the DBIE browser URL.
- RBI's official Reference Rate Archive is hosted on `rbi.org.in`: `https://www.rbi.org.in/Scripts/ReferenceRateArchive.aspx`.
- RBI's 2008 release describes DBIE as RBI's data warehouse and says series were made available in downloadable formats.

## Mirror / prototype evidence — NOT primary RBI endpoint
- `https://dev.dbie.rbihub.in/docs` explicitly describes itself as a mirror/prototype of RBI DBIE; says the content is scraped into its own Postgres database and that it is built for testing/demo purposes.
- The same documentation warns that figures may lag RBI's latest published/revised data and that some tables may be missing.
- Its API host `https://data-api.dbie.rbihub.in` serves that mirror's own read-only database. It is not established by the retrieved evidence as an RBI-operated primary endpoint.
- The mirror's documented 5-minute API cache and last-scrape vintage apply to the mirror, not automatically to RBI's primary DBIE.

## Consequence for the 6,319 vs 6,308 finding
- The 11-row difference is a discrepancy within the mirror's table metadata versus grid pagination.
- A secondary mirror's 6,308 count is corroborative only; it does not establish the correct count in RBI's primary dataset.
- Previous wording that called the mirror CSV endpoint an 'official DBIE CSV endpoint' is withdrawn.
- The mirror may be used only as secondary comparison evidence, clearly labelled as a prototype/mirror.

## Corrected source hierarchy
1. Primary: RBI DBIE at `https://data.rbi.org.in` (or the current RBI-designated DBIE route verified from an RBI-owned page).
2. Primary for RBI reference-rate-only validation: RBI Reference Rate Archive on `rbi.org.in`.
3. Secondary only: `dev.dbie.rbihub.in` / `data-api.dbie.rbihub.in` and Dataful.

## Current acceptance state
- RBI DBIE primary route for the specific daily interbank USD/INR table: NOT YET VERIFIED in this audit.
- Primary RBI raw CSV bytes, retrieval timestamp, byte count, SHA-256: NOT DONE.
- Mirror row-count discrepancy: observed, but not a primary-source discrepancy.
- Dataful corroboration: secondary only.
- USD/INR panel ingestion: BLOCKED until primary RBI source route and raw vintage are captured.
- Do not ingest mirror observations as primary RBI data.

## Corrective actions
1. Re-resolve the target table through RBI-owned DBIE navigation / current official RBI documentation.
2. Capture the exact primary download URL and the source table's own title, frequency, period, unit, row count, and metadata.
3. Download original bytes, record UTC retrieval time, HTTP status, content type, byte count, and SHA-256.
4. Perform date-key and field QA on the primary file.
5. Compare only semantically matching reference-rate values with RBI's Reference Rate Archive; do not use reference rates to validate interbank OHLC.
6. Keep mirror comparison as a separate non-primary diagnostic.

## Project safety
No synthetic rows, fabricated timestamps, silent row deletion, or forward fill. ₹0 spend; free official sources only. Research-only. No production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A–E, or Hard Gate changes.