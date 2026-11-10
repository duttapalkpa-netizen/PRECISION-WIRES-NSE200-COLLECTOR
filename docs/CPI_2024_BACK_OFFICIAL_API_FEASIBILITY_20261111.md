# CPI 2024 Back-Series — Official API Route Feasibility Audit
Audit date: 2026-11-11 (Asia/Kolkata)
Repository: duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR
Branch: research/global-capital-rotation-overlay-v1
Scope: identify a lawful, reproducible alternative acquisition route for the CPI 2024=100 Back series. This is a route/schema feasibility audit only, not an observation ingestion run.

## Decision
A current official MoSPI e-Sankhyiki CPI API route is verified:
- Product page: https://esankhyiki.mospi.gov.in/macroindicators?product=cpi&tab=api
- Endpoint: GET /api/cpi/getCPIData
- API version: 2.0.0, OpenAPI 3.0
- Response contract described by the official page: paginated records endpoint, JSON envelope with boolean statusCode and human-readable msg.
- Access: bearer token optional; requests without token are served as guest.
- Rate limits: requests are rate-limited per IP.
- Published schema names: MetaData, CpiGroupRecord, CpiItemRecord, Cpi2024Record, CpiRecordsResponse, Cpi2024RecordsResponse, NoDataResponse, ErrorResponse, ServerErrorResponse, ServerError2024Response, LimitErrorResponse, RateLimitResponse, UnauthorizedResponse.

Official API page search-index evidence was captured during this audit. The OpenAPI YAML path advertised by the official UI is ../../layout/swagger_user_cpi.yaml, resolving to https://esankhyiki.mospi.gov.in/layout/swagger_user_cpi.yaml. The browser retrieval attempt in this environment returned an internal access error; this is not evidence that the publisher endpoint is down.

## Back-series scope evidence
Official MoSPI CPI 2024 FAQ states that the Back series is published for:
- All-India Rural, Urban and Combined indices: 2013-01 through 2024-12.
- All-India Rural, Urban and Combined annual inflation: 2014-01 through 2024-12.
The official CPI FAQ also confirms 2024=100 is the current CPI base year.

## Important distinctions and unresolved items
1. The API endpoint is not the same thing as the original workbook's download URL. Do not retroactively assign the API URL to cpi_2479.xlsx.
2. The exact query parameter names/allowed values for the new API's 2024 Back series were not independently retrieved from the OpenAPI YAML in this audit. Do not construct a production request from guessed parameter names.
3. The portal's API page confirms guest access, but no live API request/response was obtained in this audit. No new raw observation payload, HTTP status, response content type, page count, or response SHA-256 is claimed.
4. The official CPI FAQ confirms the Back-series reference window; it does not by itself prove the workbook's acquisition provenance.
5. The old CPI 2012 API manual is not an acceptable substitute for the current 2024 API contract. Its endpoint and series codes differ; do not reuse them.

## Bounded next execution
- Retrieve the exact official OpenAPI YAML from the portal through a supported browser/download route.
- Extract the 2024 Back series request parameters and enum values from that YAML only.
- Execute one small public GET smoke test (one reference month or one page), recording request URL, final URL, UTC retrieval timestamp, HTTP status, content type, raw response bytes and SHA-256.
- Validate response envelope, schema, period, base year, series, geography, sector and natural-key uniqueness.
- Only then consider a separate full-history API acquisition and same-snapshot Factor Registry domain QA. Keep it separate from the user's original XLSX.
- Do not repeatedly retry rate-limited calls; respect documented per-IP rate limits.

## Current gate
- Official current CPI API route: VERIFIED.
- Guest-access availability: VERIFIED from official API description.
- 2024 Back-series official coverage window: VERIFIED from official MoSPI FAQ.
- Exact API parameter contract for 2024 Back: UNKNOWN_PENDING_OPENAPI.
- Live API smoke test / observations / raw payload hash: NOT_DONE.
- Original XLSX exact download URL and retrieval timestamp: UNKNOWN.
- Original workbook structural QA and screenshot filter reconciliation: PASS, unchanged.
- Factor Registry admission: BLOCKED / UNKNOWN_PENDING_PROVENANCE.
- Active overlay ingestion: NOT_DONE.

## Invariants
Research-only. ₹0 spend. No paid API, no authentication bypass, no fabricated timestamps, no guessed query parameters, no synthetic observations, no forward-fill, no unsupported source promotion. UNKNOWN is neither PASS nor FAIL. No changes to production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A-E or Hard Gate. No PR merge or production integration.
