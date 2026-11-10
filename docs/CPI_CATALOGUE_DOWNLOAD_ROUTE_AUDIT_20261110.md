# CPI Catalogue Download Route — Acceptance Boundary
Audit date: 2026-11-10 (Asia/Kolkata)
Repository: duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR
Branch: research/global-capital-rotation-overlay-v1

## Official route findings
1. The current eSankhyiki CPI catalogue exposes monthly 2024-base catalogue entries. Example: All India General (Rural, Urban and Combined) group-wise indices and inflation for August 2026, provisional, table ID CPIMCY26002AUG, release date 2026-09-14. July 2026 provisional group-wise table ID CPIMCY26002JULY, release date 2026-08-12.
2. The official eSankhyiki FAQ states that Macro Indicators datasets can be downloaded as CSV from the product page after applying selections; the CSV is the filtered dataset visible on screen. It separately states that Data Catalogue publications are downloadable as MS Excel according to released statements.
3. The data.gov.in e-Sankhyiki listing exposes a Catalog API and Zip Download at the portal listing level, but it is not itself evidence of a direct CPI table CSV URL.
4. Current CPI API documentation identifies GET /api/cpi/getCPIData as paginated and says guest access is supported; Swagger preview is limited to first 10 records. This does not establish a specific CSV endpoint.

## What is verified vs not
- Official CPI catalogue table IDs and metadata: VERIFIED.
- Official product-page CSV download capability: VERIFIED at UI/workflow level.
- Exact direct CSV URL / backend request for CPIMCY26002AUG or CPIMCY26002JULY: NOT RESOLVED.
- Raw CSV bytes, HTTP status, response content type, row count, SHA-256: NOT RETRIEVED.
- The data.gov.in Catalog API / Zip Download must not be mistaken for a CPI-specific direct download.
- No URL patterns, query parameters, table-ID-to-filename transformations, or API parameters were guessed.
- No data were fabricated, no credentials used, no API calls made.

## Controlled next step
On the official eSankhyiki portal, open Macro Indicators > CPI > Table; choose one exact aggregate series (All India Combined General, base 2024, one reference month and explicit provisional/final vintage); use the portal's own CSV Download control. Preserve original bytes and response metadata before parsing. If the download action cannot be captured as a stable public URL or file response in the authorized environment, retain UNKNOWN and request the user to export the file through the portal and upload it. Do not substitute a catalogue XLSX or a different vintage.

## CPI series bridge note
MoSPI's official CPI base-2024 FAQ states that back series are linked using the overlapping year 2025, comparing annual average geometric-mean CPI for old and new series. This is an official linking-factor method, but the actual linking factor and series-specific back-series values must be read from the official released back-series tables; do not calculate or infer missing values from this description alone.

## Acceptance gate
CPI observation ingestion remains NOT COMPLETE. Acceptance requires raw CSV SHA-256, exact table ID and release metadata, period/base/geography/level/vintage match, row-count reconciliation, unique key check, null/missing audit, and numeric/unit validation.

## Invariants and progress
Research-only. No production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A-E or Hard Gate changes. No paid data or synthetic observations.
This route audit is complete; it is not a CPI data-ingestion pass. Milestone 6 remains 20%; overlay remains 62.5%; overall V11.3 remains NOT_CALCULABLE.
