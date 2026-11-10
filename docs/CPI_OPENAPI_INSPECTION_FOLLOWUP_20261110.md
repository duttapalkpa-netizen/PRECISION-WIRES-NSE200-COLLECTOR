# CPI API OpenAPI Inspection — Follow-up
Audit date: 2026-11-10 (Asia/Kolkata)
Repository: duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR
Branch: research/global-capital-rotation-overlay-v1
Scope: documentation-only inspection; no API observation request was sent.

## New official documentation facts
The current MoSPI eSankhyiki CPI API page identifies:
- OpenAPI version 3.0.0; API version 2.0.0.
- GET /api/cpi/getCPIData, described as a paginated CPI index and inflation records endpoint.
- CPI base years 2010, 2012 and 2024.
- JSON response envelope with boolean statusCode and human-readable msg.
- Guest access is advertised; bearer token is optional; requests are rate-limited per IP.
- Swagger UI explicitly warns that its preview returns only the first 10 records.
- Published schema names: MetaData, CpiGroupRecord, CpiItemRecord, Cpi2024Record, CpiRecordsResponse, Cpi2024RecordsResponse, NoDataResponse, ErrorResponse, ServerErrorResponse, ServerError2024Response, LimitErrorResponse, RateLimitResponse, UnauthorizedResponse.

## Retrieval attempt and limitation
- The official page links to ../../layout/swagger_user_cpi.yaml; the resolved URL tested was https://esankhyiki.mospi.gov.in/layout/swagger_user_cpi.yaml.
- The available web inspection route returned an Internal Error / URL not accessible. This is a tool retrieval limitation only; it does not establish that the MoSPI file or API is unavailable.
- Therefore exact query parameter names/types, required fields, response property definitions, pagination parameters, and rate-limit thresholds remain UNKNOWN.
- No guessed parameter names, undocumented endpoint calls, authentication bypass, or API observation requests were attempted.

## Catalogue scope guard
Official catalogue search results show CPI monthly 2024-base datasets, including August 2026 provisional releases (e.g. CPIMCY26002AUG, released 2026-09-14) and July 2026 provisional releases (e.g. CPIMCY26001JULY, released 2026-08-12). These IDs identify catalogue tables, not proven API query parameters. Do not infer API parameters from table IDs.
Keep Rural, Urban, Combined; General/group/division/item level; and 2010/2012/2024 base-year series separate. Preserve provisional/final status and release vintage. The 2024 base uses COICOP 2018 with 12 divisions; no splicing to earlier base years without an official linking method.

## Gate outcome
- Official API documentation / endpoint / guest-access policy: VERIFIED.
- Schema component names: VERIFIED from the published API page.
- Exact OpenAPI YAML and parameter/property schemas: UNKNOWN (tool could not retrieve the linked YAML).
- CPI raw observations ingested in this task: NO.
- CPI observation acceptance: NOT PASSED; remains blocked pending authoritative schema and raw-response QA.
- This task: documentation inspection and limitation recording completed.

## Next safe action
Use the portal's own documented CSV download for one exact aggregate catalogue table, if the exact table-download URL and response can be obtained from the official UI. Preserve raw bytes and SHA-256, then compare with same-period/base/vintage catalogue metadata. This is a separate catalogue-download route, not a guessed API request. If the exact official download path cannot be resolved, stop and retain UNKNOWN.

## Invariants
Research-only; no changes to production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A-E or Hard Gate. No paid data, synthetic observations, or unsupported source promotion.
Milestone 6 remains 20%; overlay remains 62.5%; overall V11.3 remains NOT_CALCULABLE.
