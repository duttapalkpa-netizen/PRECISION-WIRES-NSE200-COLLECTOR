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


## Actions run audit (verified 2026-11-02)
Workflow: `.github/workflows/macro_geo_p0_raw_acquisition.yml`

| Run | Commit | Conclusion | Evidence |
|---|---|---|---|
| #1 — 41423497196 | 475303fc54f2d7c398e4f319bfc492e813fb2050 | failure | Initial push-trigger workflow failed. |
| #2 — 41423553534 | e5bd88c50b24bdb5c606f14c56d061a2d2e744fa | failure | Self-contained push trigger revision failed. |
| #3 — 41431166713 | a7d52a70c3d122285d3b83ed2697234143661acd | failure | Strict CSV date/index validation revision failed. |
| #4 — 41431703627 | 5ab0742b906cb2f401729901280c327dd8468ee9 | failure | QA assertion/workflow revision failed. |
| #5 — 41432079313 | cdb112ba3747a71914d108c7bbe7892bd2209dea | failure | HTML rejection assertion fix run failed. |
| #6 — 41432087344 | 66438f2c1b6f7a1883075a797c81475457cbf109 | success | QA-only: 5 tests passed in 0.04s; collect job skipped. |

Run #6 job IDs: QA 125232874120 (success); collect 125232996100 (skipped).
Run #6 artifact inventory: 0 artifacts. Consequently there is no workflow artifact ZIP to download and no raw-file SHA-256 or drift result to independently recompute from this run. The successful result is limited to collector unit tests; it is not a successful acquisition.

## Dated official response records found (not raw-byte archived)
- PIB PRID 2175552: official rendered release page identifies Ministry of Finance, title “Fourth Kautilya Economic Conclave (KEC 2025)...”, Posted On 06 Oct 2025 7:50 PM by PIB Delhi. URL: https://www.pib.gov.in/PressReleasePage.aspx?PRID=2175552 . The page was inspected in rendered form; the original HTTP response bytes/headers were not captured to a file, so no SHA-256 is claimed.
- MEA official PDF located: https://www.mea.gov.in/Portal/CountryNews/25076_Press_release_for_Diwali_reception_on_19th_Oct_2025.pdf . Search-indexed PDF identifies Embassy of India, Ashgabat, press release about the 19 Oct 2025 Diwali reception. The PDF bytes were not downloaded into the workflow artifact; no SHA-256 is claimed.
- PIB archive documentation confirms PIB archive records are searchable by year/month, ministry and keyword: https://www.pib.gov.in/Aboutarchive.aspx?lang=1&reg=1 .

## Hash and validation disposition
- Unit validation: PASS, 5/5 tests (Run #6 logs).
- Production raw CSV date/index validation on downloaded market data: NOT RUN; no market raw CSV acquired.
- Independent SHA-256 recomputation: NOT POSSIBLE; no acquisition artifact/raw response file exists in Run #6.
- Download drift/repeat-fetch comparison: NOT RUN.
- PIB/MEA response archival: SOURCE LOCATED, ORIGINAL RESPONSE BYTES NOT ARCHIVED.
- Archived vintage pair: NOT FOUND/NOT VERIFIED. No revision ledger created, by design.

## Updated decision
COLLECTOR_QA_PASS_RAW_ACQUISITION_BLOCKED. Route discovery and tests are useful progress, but no market raw acquisition or official-response byte archive has been completed. All P0 coverage remains partial/unknown; no source promotion; Hard Gate BLOCKED.
