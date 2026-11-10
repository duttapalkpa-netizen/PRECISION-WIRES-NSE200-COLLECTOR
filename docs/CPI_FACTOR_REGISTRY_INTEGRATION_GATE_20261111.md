# CPI 2024=100 Back-Series — Factor Registry Integration Gate
Audit date: 2026-11-11 (Asia/Kolkata)
Branch: research/global-capital-rotation-overlay-v1
Scope: research-only normalized panel preparation and registry admission decision.

## Source artifact and immutable identity
- User Library file: `cpi_2479.xlsx`
- Library file ID: `file_00000000407c8211a2f3ed120a465115`
- Raw bytes: 166,608
- Raw SHA-256: `1779d670323982833f3f0668fee9b5f959dbe93f481571c17ab7a1b44a2ddbc0`
- Workbook sheet: `CPI Data`
- Raw workbook preserved; no cell edits.
- User's earlier official e-Sankhyiki screenshot establishes the selected filters: Base Year 2024, Series Back, Year All, State All India, Sector Rural/Urban/Combined, Division CPI (General). Exact table ID, actual download URL, and retrieval timestamp were not visible in the evidence retained for this audit and remain UNKNOWN.

## Normalized research panel prepared (not active overlay input)
- Derived file: `cpi_2024_back_series_general_research_panel.csv`
- Derived SHA-256: `fa119ac24c2c2ad17bdd95b723286cce50940db4c9ef8451e03e0bad15209bcb`
- Rows: 828 observations + header.
- Index measure: 432 rows; 2013-01 through 2024-12, 3 sectors.
- Annual inflation measure: 396 rows; 2014-01 through 2024-12, 3 sectors.
- Keys unique by (date, indicator, sector); no duplicate keys.
- Every row retains base_year, series, state, sector, division, raw filename and raw SHA.
- Blank 2013 inflation values are not materialized as observations.
- `published_at`, exact `source_table_id`, and `retrieved_at` are deliberately blank because they were not captured. Every normalized row is therefore tagged `quality_status=UNKNOWN`. The official product page URL is recorded as a discovery/source route, not represented as the exact download URL.
- This file is a research derivative only. It must not be copied into the active overlay seed file or treated as a verified observation input until missing provenance is captured.

## Proposed Factor Registry record
- Factor group: `macro_indicators`
- Source family: MoSPI e-Sankhyiki CPI, 2024=100 Back-Series
- Factor candidates: General CPI index (Rural/Urban/Combined); General CPI annual inflation (Rural/Urban/Combined)
- Frequency: Monthly
- Reference windows: Index 2013-01..2024-12; inflation 2014-01..2024-12
- Geography: All India
- Classification scope: CPI (General) only
- Base year / series: 2024 / Back
- Source class: OFFICIAL_STATISTICAL_SOURCE
- Raw artifact SHA-256: `1779d670323982833f3f0668fee9b5f959dbe93f481571c17ab7a1b44a2ddbc0`
- Parser/coverage QA: PASS
- Registry availability: `UNKNOWN_PENDING_PROVENANCE` (not AVAILABLE)
- Production eligibility: `NOT_AUTHORIZED`

## Admission decision
**Registry admission remains BLOCKED/UNKNOWN**, despite successful raw-file and panel QA. The missing source table ID, exact download URL and retrieval timestamp are material provenance fields. Do not upgrade the macro_indicators factor group to AVAILABLE based on a workbook alone. Do not change the current Factor Registry snapshot or claim that this panel has been consumed by the overlay engine.

## Linking and measurement constraints
- Official CPI 2024 press release defines General-level linking factors: Rural 0.5222, Urban 0.5320, Combined 0.5267.
- The factor formula uses the ratio of 2025 annual-average geometric means of the new and old series.
- Direct linking is permitted only at General Index level due to the classification change (CPI 2024 COICOP-2018 vs CPI 2012 classification).
- This back-series file ends in 2024. It cannot independently recalculate the 2025 linking factors; retain published factors as official reference values, not independently recalculated values.
- No group/division/class/subclass/item-level factors may be inferred or applied.

## Next exact acceptance action
Capture from the official e-Sankhyiki browser download history/network details or official UI record: (1) exact table/dataset ID, (2) exact download URL, and (3) retrieval timestamp with timezone. Then bind these to the immutable raw SHA and run deterministic parser re-hash. Only after same-snapshot provenance and Factor Registry-specific QA may the registry status be reconsidered. No authentication bypass, guessed identifiers, or external contact.

## Safety and production invariants
No synthetic data, no fabricated timestamps, no forward-fill, no imputation, no guessed source IDs, and no paid APIs/services. UNKNOWN remains neither PASS nor FAIL. No changes to production selector, `RANKING_SCORE`, `+1 PRESSURE_FADE`, CORE-672, Engines A–E or Hard Gate. No PR merge or production integration.

## Progress accounting
- CPI raw workbook and structural/coverage QA: PASS.
- Normalized research panel preparation: PASS (828 valid measure records, all tagged UNKNOWN pending provenance).
- Factor Registry admission: BLOCKED/UNKNOWN_PENDING_PROVENANCE.
- Active overlay input ingestion: NOT DONE.
- Milestone 6 and overlay percentages: unchanged pending registry admission and formal denominator reconciliation.
- Overall V11.3 progress: NOT_CALCULABLE.
