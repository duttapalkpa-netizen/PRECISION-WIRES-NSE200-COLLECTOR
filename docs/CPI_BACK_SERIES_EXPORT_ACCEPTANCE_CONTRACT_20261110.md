# CPI Back-Series Export Acceptance Contract — 2026-11-10

## Purpose
Prepare a deterministic acceptance contract for the official MoSPI CPI 2024=100 back-series export. This is a pre-ingestion QA specification; it does not claim that the raw export has been retrieved.

## Official retrieval workflow
The MoSPI e-Sankhyiki FAQ states:
- Macro Indicators product pages allow filtered dataset downloads in CSV according to selections visible on screen.
- Data Catalogue statements are downloadable as Excel.
- Registration is not required for public browsing/download.
Sources:
- https://esankhyiki.mospi.gov.in/macroindicators?product=cpi
- https://esankhyiki.mospi.gov.in/catalogue-main/catalogue?product=CPI
- https://esankhyiki.mospi.gov.in/macroindicators?product=cpi&tab=api

The CPI API page documents GET /api/cpi/getCPIData, paginated JSON, optional guest bearer token, and per-IP rate limits. The rendered API page exposes no readable parameter schema in this retrieval session; do not guess query parameters.

## Exact coverage contract from MoSPI
Source: CPI 2024 first press release dated 12 February 2026:
https://mospi.gov.in/uploads/latestReleases/latest_release_1770891893893_6b458c0a-c327-4fef-a554-41131ea67273_Press_Relase_of_CPI_for_Jan26.pdf
- General index back-series: January 2013 through December 2024, inclusive, for Rural, Urban and Combined.
- Annual inflation back-series: January 2014 through December 2024, inclusive, for Rural, Urban and Combined.
- Linking factors: Rural 0.5222; Urban 0.5320; Combined 0.5267.
- Direct linking allowed only at General Index level.

Expected unique month-sector keys if exported in long format:
- Index: 144 months × 3 sectors = 432 unique keys.
- Annual inflation: 132 months × 3 sectors = 396 unique keys.
These are expected key counts, not a claim about the source workbook's physical row count. Wide-format exports may encode sectors as separate columns; acceptance must normalize without changing source values.

## Mandatory raw-file capture
Before parsing, preserve:
1. Exact official product page URL and selected filter values.
2. Official table/dataset ID (if Catalogue export) or the exact on-screen filter selection (if Macro Indicators CSV).
3. Download URL as actually observed in browser; never construct one.
4. Retrieval timestamp with timezone.
5. Original filename, byte size and SHA-256.
6. Raw file immutable copy; parsed output must be a separate derivative.

## QA checks after raw artifact exists
1. File signature and parseability match the actual extension; no silent format substitution.
2. Detect header rows, sheets, units, sector labels, date representation and provisional/final vintage.
3. Normalize dates to YYYY-MM only in derived QA output; retain raw source unchanged.
4. Validate complete expected coverage per sector and reference month; report missing and extra keys.
5. Check duplicate (reference_month, sector, measure) keys.
6. Check no dates outside official windows.
7. Preserve missing/blank values as missing; no forward fill or imputation.
8. Verify index and inflation measures are not mixed.
9. Validate Rural/Urban/Combined labels and units; do not infer Combined by recomputing rural/urban weights.
10. Compare only published linking-factor values at General level unless unrounded 2025 source inputs are independently available. Do not apply factors to detailed groups/items.
11. Re-run parse from immutable raw file and compare deterministic output hash.

## Current status
- Official retrieval workflow and public-access policy: PASS.
- Expected coverage contract: PASS.
- Exact back-series catalogue ID / download URL: UNKNOWN.
- Raw workbook/CSV bytes and SHA-256: UNKNOWN / NOT RETRIEVED.
- Data completeness/duplicate QA: NOT RUN (no raw file).
- Linking-factor independent recalculation: BLOCKED (unrounded overlapping-year inputs not obtained).

## Non-negotiable controls
No guessed URLs, guessed query parameters, synthetic rows, fabricated timestamps/hashes, silent missing-value fill, or use of third-party mirrors. No paid APIs/services or external contact. UNKNOWN is neither PASS nor FAIL. No production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A–E or Hard Gate changes. This contract does not increase CPI ingestion, Milestone 6, overlay or overall V11.3 progress.
