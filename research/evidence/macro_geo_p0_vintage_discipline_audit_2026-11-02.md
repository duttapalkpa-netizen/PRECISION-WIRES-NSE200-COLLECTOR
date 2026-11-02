# Macro-Geo P0 vintage discipline audit — 2026-11-02

Status: research-only source/vintage audit. This is not a coverage PASS and does not promote any source group.

## A. CGA first-publication / independently preserved historical copy investigation

### Official route findings
- CGA monthly archive index exposes FY/month report navigation: https://cga.nic.in/MonthlyReport/Published/11/2025-2026.aspx
- Official month-specific HTML report pages remain available, e.g. June/August/September/October FY2025-26. The currently served page is a current retrieval, not proof of first-publication time.
- CGA advance release calendar explicitly says dates are expected and subject to change: https://cga.gov.in/Page/Advance-Release-Calendar.aspx. It is not actual publication evidence.
- CGA monthly-account disclaimer explicitly says figures are provisional and subject to change: https://cga.gov.in/Page/Monthly-Accounts-Review.aspx.
- Internet Archive/Wayback exact-URL wildcard routes were attempted for CGA June, August, September and October 2025 report URLs. The research interface could not retrieve the wildcard/CDX capture records; therefore no Wayback capture timestamp or archived file was certified in this run.
- An independent third-party archival index (The Public Rupee) identifies a CGA March 2026 report copy with SHA-256 and first-acquired date 2026-07-26. This proves that one later CGA report has been independently content-hashed and retained since that acquisition date; it does not provide historical copies or first-publication timestamps for the six FY2025-26 Apr-Sep reports. See https://www.thepublicrupee.com/sources/df0460c0-ec87-4418-9573-0192a4b6d61e.
- Result for requested six-month first-publication evidence: NOT FOUND / UNKNOWN. Do not infer release time from reference month, archive page labels, document metadata, calendar, retrieval timestamp, or current URL.

### CGA status
`DATED_PIB_RELEASE_CROSSCHECK_PASS` for six release points; `CGA_FIRST_PUBLICATION_TIMESTAMP_UNKNOWN`; `INDEPENDENT_HISTORICAL_CGA_COPIES_NOT_FOUND_FOR_TARGET_MONTHS`; `INTERMEDIATE_REVISIONS_UNKNOWN`. Keep Capex partial/provisional. No promotion.

## B. Apply the same vintage discipline to Macro-Geo P0 groups

| P0 group | Official source route | What is supported | Vintage/revision boundary | Status |
|---|---|---|---|---|
| benchmark_index | NSE Historical Index Data / All Reports; Nifty Indices Historical Data | Official daily historical index series and historical-report downloads are available. NSE FAQ says NIFTY 50 historical series extends to 3 Jul 1990. | Trading date is observation date, not source publication timestamp. Historical index values can be restated/reconstructed; index methodology and constituent changes must be versioned. No release-time or immutable daily-vintage ledger produced in this run. | PARTIAL / RELEASE_AT_UNKNOWN / VINTAGE_UNVERIFIED |
| sector_indices | NSE Indices Historical Data; NSE Indices methodology documents | Official sector index definitions/methodologies and historical index data routes exist. | Methodology versions, rebalances, corporate-action adjustments and back-calculation must be distinguished from as-published daily level. No complete archived daily vintage set with capture hashes and release times produced in this run. | PARTIAL / METHODOLOGY_VERSION_REQUIRED / VINTAGE_UNVERIFIED |
| volatility | NSE India VIX historical data and All Reports; NSE India VIX methodology | Official India VIX is option-implied expected volatility for the next 30 calendar days; official historical-data download route exists. NSE announced real-time dissemination from 19 Jul 2010. | Observation/trading date is not dissemination timestamp for each historical row. Intraday vs end-of-day, methodology version, missing data and later corrections must be preserved. No immutable row-level vintage or publication-time ledger produced in this run. | PARTIAL / RELEASE_AT_UNKNOWN / VINTAGE_UNVERIFIED |
| geopolitical_events | PIB Archives (1947 onward), PIB All Releases; MEA advanced search/archive | Official government event/statement pages can provide dated publication records and source URLs. PIB archive is searchable by year/month/ministry/keyword; MEA has date/year/month and content-type filters. | Publication timestamp is not necessarily event occurrence time. Event-time, publication-time, update-time, timezone, source ministry, event taxonomy, duplicates and corrections need separate fields. No complete canonical event universe or historical correction ledger established in this run. | PARTIAL / EVENT_COVERAGE_UNVERIFIED / REVISION_HISTORY_UNKNOWN |

## C. Required schema / hard rules for all four groups

Every observation/event must carry, where applicable:
- `observation_date` or `event_occurred_at` (source-defined semantics)
- `published_at` (source-stated timestamp only; null if absent)
- `retrieved_at_utc` (our collector retrieval timestamp; never substitute for publication)
- `source_url`, `source_publisher`, `source_document_id` / release ID
- `source_file_sha256`, `capture_timestamp` (only for independently archived capture)
- `methodology_version`, `base_date`, `index_variant`, `provisional/final status` where applicable
- `vintage_key`, `supersedes_vintage`, `revision_delta` only when two real vintages exist
- `timestamp_precision` and explicit `UNKNOWN_NOT_SUPPLIED` reason codes.

Rules:
1. Never synthesize publication timestamps from dates, retrieval time, HTTP Last-Modified, file metadata, release calendar or report path.
2. Do not treat a Wayback capture date as original publication date; record it separately as archive capture time.
3. Never infer no revisions from one current file. Require at least two independently dated vintages for a revision comparison.
4. Do not treat methodology/back-series recalculation as a data revision without explicit classification.
5. UNKNOWN is neither PASS nor FAIL; missing sources remain UNKNOWN and block coverage promotion.
6. No paid sources, no API spend, no external contact.

## D. Next bounded collection tasks
1. CGA: continue exact URL CDX/API and alternate archive catalog checks; preserve any returned timestamp and raw WARC/HTML hashes. Until then retain UNKNOWN.
2. Benchmark/sector: download bounded official NSE/NiftyIndices daily CSVs for a fixed sample period, hash raw files, record source date and retrieval time separately, then test repeated downloads for byte/value drift.
3. VIX: collect official daily historical CSV for same bounded period; separately identify end-of-day versus intraday source semantics and methodology documents.
4. Geopolitical events: build bounded PIB/MEA dated release sample with publication timestamp, event occurrence time only when explicitly sourced, release ID, URL, hash and correction/supersession links.
5. Run same-snapshot 4-group audit only after source rows, manifests and QA reports are generated. Do not change production.

## E. Final decision
`MACRO_GEO_P0_VINTAGE_AUDIT_COMPLETE_WITH_GAPS`. The audit method has been applied to all four P0 groups; source acquisition and vintage certification are incomplete. Keep all four groups PARTIAL/UNKNOWN as shown. Hard Gate remains BLOCKED. Production selector, `RANKING_SCORE`, `+1 PRESSURE_FADE`, and 672 diagnostics unchanged.
