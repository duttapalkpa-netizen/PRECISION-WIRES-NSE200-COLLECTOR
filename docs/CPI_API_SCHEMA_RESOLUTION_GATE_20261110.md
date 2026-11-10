# CPI API Schema Resolution Gate — 2026-11-10

## Objective
Resolve the official MoSPI e-Sankhyiki CPI API query schema before making any CPI observation request.

## Verified official facts
- CPI API documentation page: https://esankhyiki.mospi.gov.in/macroindicators?product=cpi&tab=api
- API version shown: 2.0.0; OpenAPI 3.0.
- Endpoint shown: GET /api/cpi/getCPIData.
- API covers CPI base years 2010, 2012 and 2024.
- Response is paginated and uses a JSON envelope with boolean statusCode and human-readable msg.
- Bearer token is optional for guest requests; requests are rate-limited per IP.
- Published schema names include MetaData, CpiGroupRecord, CpiItemRecord, Cpi2024Record, CpiRecordsResponse and Cpi2024RecordsResponse.
- The API page exposes the relative OpenAPI document path ../../layout/swagger_user_cpi.yaml.
- The corresponding resolved candidate URL https://esankhyiki.mospi.gov.in/layout/swagger_user_cpi.yaml was attempted through the available web retrieval route but was not accessible. This is a retrieval limitation, not evidence that the file or API is invalid.
- CPI catalogue page https://esankhyiki.mospi.gov.in/catalogue-main/catalogue?product=CPI reports 495 datasets and pagination; the rendered first page exposes only records 1–10. No back-series table ID or download URL was established from the accessible catalogue page in this pass.
- Official e-Sankhyiki FAQ states catalogue datasets can be downloaded as Excel and Macro Indicator datasets as CSV, and that registration is not required for browsing/downloading.

## Gate decision
- API route and broad access model: PASS.
- Exact OpenAPI parameter names, types, requiredness, pagination controls, base-year selector and response field schema: UNKNOWN / NOT RESOLVED.
- Back-series table ID and exact catalogue download URL: UNKNOWN.
- CPI raw observation request: NOT SENT.
- CPI raw observations, row counts, completeness, vintage and SHA-256: NOT AVAILABLE.
- Numerical recomputation of published linking factors: BLOCKED pending source observations and exact methodology inputs.

## Why no API request was sent
Without the authoritative parameter schema, a guessed request could return an empty/default/current-series sample or the wrong base-year/vintage. The page itself says Swagger previews only the first 10 records. A preview must not be mistaken for complete extraction. No guessed parameter names, endpoint query, or fabricated response were used.

## Next safe action
Obtain the OpenAPI YAML or official API user manual from an accessible official route, or use the portal's authorized UI to export the exact CPI 2024 back-series table as CSV/XLSX. Then preserve raw bytes, request/response metadata, retrieval timestamp and SHA-256 before parsing. If the route remains unavailable, use a user-provided official export. Do not bypass authentication or rate limits.

## Project controls
No paid service/API, external contact, or production integration. No change to production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A–E or Hard Gate. UNKNOWN remains neither PASS nor FAIL. This schema audit does not increase CPI ingestion, Milestone 6, overlay, or overall V11.3 progress.
