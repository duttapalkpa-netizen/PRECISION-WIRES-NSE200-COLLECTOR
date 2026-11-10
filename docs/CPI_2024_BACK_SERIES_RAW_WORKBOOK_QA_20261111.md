# CPI 2024=100 Back-Series Raw Workbook QA — 2026-11-11

## Artifact identity
- Library file: cpi_2479.xlsx
- Library file ID: file_00000000407c8211a2f3ed120a465115
- Library path: /cpi_2479.xlsx
- MIME: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
- Size: 166,608 bytes
- SHA-256: 1779d670323982833f3f0668fee9b5f959dbe93f481571c17ab7a1b44a2ddbc0
- Workbook sheet: CPI Data
- Header columns: base_year, series, year, month, state, sector, division, group, class, sub_class, item, code, index, inflation, imputation
- Retrieval context: User-provided screenshot of official e-Sankhyiki CPI table showed Base Year=2024, Series=Back, Year=All, State=All India, Sector=Rural/Urban/Combined, Division=CPI (General), and 20 of 432 records. User subsequently confirmed the downloaded workbook was saved in Library. The workbook filename itself does not encode the catalogue ID; do not infer one.

## QA results
- Workbook opens successfully with openpyxl; one sheet named CPI Data.
- Header row: 15 columns; data rows: 432; blank data rows: 0.
- Scope values: base_year=2024 (432/432), series=Back (432/432), state=All India (432/432), division=CPI (General) (432/432).
- Reference years: 2013–2024 inclusive, 12 years.
- Each year contains 36 observations (12 months × 3 sectors).
- Sector coverage: Rural 144, Urban 144, Combined 144.
- Month coverage: each calendar month occurs 36 times.
- Unique (year, month, sector) keys: 432; duplicate keys: 0.
- Expected key set: 144 months × 3 sectors = 432; missing keys: 0; extra keys: 0.
- Index: all 432 values present and parseable as numeric strings.
- Inflation: 396 values present and parseable as numeric strings; 36 missing values are exactly all three sectors for each 2013 month. This matches the official back-series inflation window beginning January 2014; 2013 index values are present and retained.
- Imputation column is blank for all 432 rows.
- No data rows were modified; raw workbook preserved.

## Gate decision
- Raw workbook acquisition: PASS (file is in Library and raw bytes materialized for inspection).
- Workbook structure and expected coverage: PASS.
- Scope and dimension integrity: PASS.
- Duplicate/missing month-sector key QA: PASS.
- Index measure completeness: PASS.
- Inflation measure completeness against its 2014-01 to 2024-12 scope: PASS (396/396 expected; 36 pre-window blanks retained).
- Raw source URL/table ID and retrieval timestamp from source browser: UNKNOWN; user screenshot confirms selected official filters and 432-row table, but not the download request URL or catalogue ID.
- Independent recomputation of published linking factors: NOT PERFORMED; raw file contains back-series 2013–2024, not the unrounded 2025 overlapping new/old inputs required by the official geometric-average formula.

## Controls
- No synthetic observations, no forward fill, no imputation, no guessed table ID or download URL.
- 2013 inflation blanks are expected pre-window missing values, not data errors.
- Do not treat the 432 records as 432 inflation observations; index has 432, inflation has 396.
- General Index only; do not apply published linking factors to detailed groups/items.
- No paid API/service or external contact.
- No production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A–E or Hard Gate changes.

## Progress accounting
This artifact validates CPI back-series observation coverage for the General Index only. It may be credited as a completed raw CPI panel ingestion/QA subtask once registered in the Factor Registry with same-snapshot provenance and domain checks. Do not independently increase the Global Capital Rotation Overlay/Milestone 6 percentage until its formal denominator and registry integration are reconciled. Overall V11.3 remains NOT_CALCULABLE pending global acceptance denominator reconciliation.
