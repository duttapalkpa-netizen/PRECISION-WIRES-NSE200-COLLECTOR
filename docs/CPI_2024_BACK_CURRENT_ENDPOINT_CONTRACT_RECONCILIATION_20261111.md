# CPI 2024 Back-Series Current Endpoint Contract Reconciliation — 2026-11-11

## Outcome

**PASS — current CPI 2024 endpoint parameter contract recovered from the NSO India-maintained client routing and its referenced OpenAPI parameter definitions.**
**BLOCKED — live API smoke test not executed in this environment.**

This resolves the prior ambiguity between the portal's current unified 2024 endpoint and the legacy endpoints.

## Primary official portal evidence

The current e-Sankhyiki CPI API page advertises:
- API version 2.0.0 / OAS 3.0
- `GET /api/cpi/getCPIData`
- 2024, 2012 and 2010 base-year support
- Paginated JSON response envelope with `statusCode` and `msg`
- Optional bearer token / guest access and per-IP rate limits

Source: https://esankhyiki.mospi.gov.in/macroindicators?product=cpi&tab=api

## NSO India-maintained client routing evidence

Repository: https://github.com/nso-india/mospi-esankhyiki
Source file: `esankhyiki/client.py`
Retrieved source confirms:
- CPI Group and CPI Item requests with `base_year == "2024"` are routed to `https://api.mospi.gov.in/api/cpi/getCPIData`.
- CPI Group and Item requests for other base years use their legacy endpoint paths.
- CPI metadata discovery uses `GET /api/cpi/getCpiFilterByLevelAndBaseYear` with `base_year`, `level`, and `series_code`.
- The client passes the request parameter dictionary through to the unified 2024 endpoint.
- The production base URL is identified in source as `https://api.mospi.gov.in`.

Source: https://github.com/nso-india/mospi-esankhyiki/blob/main/esankhyiki/client.py

## OpenAPI parameter definitions

The NSO India-maintained repository's `swagger/swagger_user_cpi.yaml` defines the parameter set for `GET /api/cpi/getCPIIndex` and `GET /api/cpi/getItemIndex`. The same maintained client routes 2024 CPI requests to `getCPIData` while passing the CPI request parameter dictionary unchanged. This establishes the parameter contract used by that maintained client for the unified 2024 endpoint, but the portal's rendered OAS 2.0.0 schema itself was not independently downloaded in this audit.

Common parameters:
- Required: `base_year` (enum 2010, 2012, 2024), `series` (Current, Back), `Format` (JSON, CSV; case-sensitive key as published).
- Optional: `year` (comma-separated YYYY), `month_code`, `state_code`, `sector_code`.
- Group level: `group_code`, `subgroup_code`.
- 2024 classification filters: `division_code`, `class_code`, `sub_class_code`, `imputation_code` (Y/N).
- Pagination: `limit`, `page`.
- Item level: `item_code`.

Metadata lookup:
`GET https://api.mospi.gov.in/api/cpi/getCpiFilterByLevelAndBaseYear?base_year=2024&level=Group&series_code=Back`

Do not infer numeric values for All India, Rural/Urban/Combined, or CPI General. Retrieve exact values from the metadata response before making the data request.

## Smoke-test attempt and result

A read-only metadata GET URL was prepared from the maintained client's documented function and parameter names. The web retrieval environment returned an internal URL-access error before exposing an HTTP response. This is not a server HTTP status, not evidence that the API is unavailable, and not a completed smoke test.

No bearer token was requested or bypassed. No data API request was sent with guessed codes. No observation payload was returned. Therefore:
- HTTP status: NOT_OBTAINED
- Content-Type: NOT_OBTAINED
- Retrieval timestamp: NOT_OBTAINED
- Raw payload SHA-256: NOT_APPLICABLE
- Observation ingestion: NOT_DONE

## Acceptance and gate status

- Current 2024 endpoint path: VERIFIED
- Current client routing for 2024: VERIFIED
- Parameter names and types via maintained client + OpenAPI source: VERIFIED WITH SCOPE NOTE
- Exact filter code values: UNKNOWN until metadata response
- Live API metadata smoke test: BLOCKED by available retrieval interface
- Data smoke test: NOT_DONE
- CPI Factor Registry admission: BLOCKED pending metadata response, live payload provenance and reconciliation

## Next action

Use an authorized browser/client capable of making a normal public HTTPS GET to the metadata endpoint. Capture the exact final URL, UTC time, HTTP status, content type, raw response bytes, and SHA-256. Then use only returned filter values to request a single small page from `getCPIData`; verify schema and reconcile to the uploaded 432-row Back-series workbook before full retrieval.

## Safety

₹0 spend. Public official source only. No guessed filter codes, synthetic observations, fabricated timestamps, authentication bypass, paid API, or production integration. Production selector, `RANKING_SCORE`, `+1 PRESSURE_FADE`, CORE-672 and Engines A–E remain unchanged.
