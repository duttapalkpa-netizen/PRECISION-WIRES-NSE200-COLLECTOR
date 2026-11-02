# Macro-Geo P0 source separation and collector validation audit — 2026-11-02

## Scope
Research-only. Window: 2025-10-01 through 2025-10-10. No production selector, scoring, pressure-fade, or 672-diagnostic changes.

## Official endpoint findings

| Group | Official endpoint / route | Established | Not established |
|---|---|---|---|
| Benchmark index | https://www.nseindia.com/reports-indices-historical-index-data | Dedicated NSE Historical Index Data page, index selector, date controls and CSV control. | No selected-window raw CSV or direct download URL retrieved. |
| Sector indices | https://www.niftyindices.com/reports/historical-data | NSE Indices historical-data interface and sectoral index catalogue, including AUTO, BANK, IT, METAL. | No selected index/date-range CSV bytes retrieved. Do not reuse broad NSE CSV as independent sector evidence. |
| India VIX | https://www.nseindia.com/reports-indices-historical-vix | Separate NSE India VIX historical page; Date/Open/High/Low/Close/Prev Close/Change/% Change fields and CSV control. | Current scrape returned No Records; direct October 2025 CSV URL and bytes not established. |
| Geopolitical events | https://www.pib.gov.in/AllRel.aspx?lang=1&reg=3 ; https://www.mea.gov.in/advanced-search-list.htm | PIB PRID 2175552 shows 06 Oct 2025 7:50 PM publication time. | Raw HTML/PDF bytes not archived here. MEA advanced search is discovery, not a dated release record. |

## Cross-group contamination
The previous config assigned the same NSE all-indices URL to benchmark_index, sector_indices and volatility. This is not independent evidence. Collector v1.1 rejects cross-group URL reuse with CROSS_GROUP_URL_REUSE_REJECTED.

## Collector v1.1 safeguards
- Requires expected_date for market series.
- Requires CSV parsing, non-empty rows, date column and expected date.
- Supports optional index_name_column, expected_index_names and required_columns.
- Rejects cross-group URL reuse.
- Preserves raw bytes, response metadata and SHA-256; performs repeated-download comparison.
- Requires publication_vintage_verified=true before producing a vintage revision ledger.
- Retrieval/schema PASS is not factor coverage PASS; Hard Gate remains BLOCKED.

## Execution and evidence status
Collector v1.1 committed to research branch. No verified Actions run ID or downloadable artifact was exposed by the available GitHub integration during this operation. Therefore no raw-response SHA-256, drift outcome, or vintage revision conclusion is claimed. PIB/MEA raw HTML/PDF capture remains pending. No archived vintage pair verified; no revision ledger created.

## Official references
- https://www.nseindia.com/reports-indices-historical-index-data
- https://www.nseindia.com/reports-indices-historical-vix
- https://www.nseindia.com/all-reports
- https://www.niftyindices.com/reports/historical-data
- https://www.pib.gov.in/PressReleasePage.aspx?PRID=2175552

## Decision
SOURCE_ROUTE_IDENTIFIED_BUT_RAW_ACQUISITION_INCOMPLETE. All four P0 groups remain PARTIAL/UNKNOWN as applicable. No source promotion. Hard Gate BLOCKED.
