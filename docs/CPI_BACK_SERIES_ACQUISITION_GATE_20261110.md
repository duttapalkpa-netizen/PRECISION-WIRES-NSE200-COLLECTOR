# CPI 2024 Back-Series Acquisition Gate — 2026-11-10

## Scope
Bounded official-source verification for the MoSPI CPI 2024=100 back-series (All-India General indices, Rural/Urban/Combined, January 2013–December 2024) and its published linking-factor scope. Research-only; no production integration.

## Official evidence verified
1. MoSPI/PIB first CPI 2024 press release, 12 February 2026:
   https://www.pib.gov.in/PressReleseDetailm.aspx?PRID=2227012&lang=2&reg=48
   - States that the back-series covers All-India General indices for Rural, Urban and Combined, January 2013–December 2024, and annual inflation January 2014–December 2024.
   - Defines the linking factor as the ratio of 2025 annual-average geometric mean CPI (new series) to the corresponding 2025 annual-average geometric mean CPI (old series).
   - Publishes General-level factors: Rural 0.5222; Urban 0.5320; Combined 0.5267.
   - Explicitly limits direct linking to the General Index level because CPI 2024 adopts COICOP-2018 while CPI 2012 used a different classification.
2. MoSPI CPI catalogue:
   https://esankhyiki.mospi.gov.in/catalogue-main/catalogue?product=CPI
   - Catalogue is publicly indexed and lists current CPI tables. The web-readable catalogue view did not expose the back-series downloadable record or its file URL in this audit.
3. MoSPI CPI API documentation:
   https://esankhyiki.mospi.gov.in/macroindicators?product=cpi&tab=api
   - Describes an open, paginated CPI API endpoint (GET /api/cpi/getCPIData), guest access without bearer token, and IP rate limiting.
   - The OpenAPI YAML/schema parameters and exact back-series query mapping were not resolved in this audit. No API request was made.

## Result / gate
- Official publication existence and date range: **PASS** (primary MoSPI/PIB release).
- Published General-level linking factors and formula: **PASS** (primary MoSPI/PIB release).
- General-only linking scope guard: **PASS** (explicitly stated by MoSPI).
- Actual back-series workbook/CSV bytes, source download URL, row count, monthly values, and SHA-256: **UNKNOWN / NOT RETRIEVED**.
- Independent numerical recalculation of factors from unrounded 2025 observations: **BLOCKED**; underlying unrounded observations and exact source table not acquired.
- CPI detailed group/division/class/subclass/item linking: **BLOCKED / NOT PERMITTED by current official scope**; do not apply General-level factors to detailed series.

## Controls
- Do not fabricate rows, dates, observations, URLs, hashes, or source IDs.
- Do not treat the published rounded factors as independently recalculated.
- Do not merge CPI 2012 and CPI 2024 detailed classifications.
- Do not infer that a discoverable API route proves a specific back-series query or returned data.
- Preserve UNKNOWN as neither PASS nor FAIL.
- No paid source/API, no external contact, no production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, or Hard Gate changes.

## Next acquisition step
Use the official e-Sankhyiki CPI catalogue/API with the exact documented query schema to retrieve the back-series table as an authorized guest request, capture raw response bytes and metadata, then validate 144 monthly records per sector (if the published range is inclusive) and annual inflation coverage. If the endpoint schema or downloadable record remains inaccessible, request a user-provided official export; do not bypass access controls.

## Completion accounting
This is a source-discovery and scope-gate audit only. It does not constitute CPI observation ingestion, numerical factor recomputation, or Milestone 6 completion. No project or overlay progress increase is justified by this note.
