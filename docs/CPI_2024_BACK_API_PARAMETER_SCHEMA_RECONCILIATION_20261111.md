# CPI 2024 Back-Series API Parameter Schema Reconciliation — 2026-11-11

## Outcome

**PARTIAL PASS — legacy official CPI API parameter schema recovered; current Macro Indicators API contract remains unverified.**

This audit deliberately separates two interfaces that must not be conflated:

1. The current e-Sankhyiki Macro Indicators CPI API page advertises API 2.0.0 / OpenAPI 3.0 and `GET /api/cpi/getCPIData`.
2. The publicly published MoSPI/NSO India `esankhyiki-mcp` repository contains a CPI OpenAPI YAML (version 1.0.11) defining `GET /api/cpi/getCPIIndex` and `GET /api/cpi/getItemIndex`.

The repository is useful official-source evidence for the legacy API contract, but it does **not** prove that its parameter contract applies to the newer `getCPIData` endpoint.

## Evidence inspected

- Current portal API documentation: https://esankhyiki.mospi.gov.in/macroindicators?product=cpi&tab=api
  - Advertises `GET /api/cpi/getCPIData`, API version 2.0.0, OpenAPI 3.0.
  - Describes guest access (optional bearer token) and per-IP rate limiting.
- NSO India / MoSPI public source repository: https://github.com/nso-india/esankhyiki-mcp
- Retrieved source file: https://github.com/nso-india/esankhyiki-mcp/blob/main/swagger/swagger_user_cpi.yaml
  - Git blob SHA: `f3a8d1619468ec8b1dbe14bd7996aece98e2277f`
  - OpenAPI: 3.0.1
  - API server: `https://api.mospi.gov.in/`
  - Spec version: 1.0.11

## Recovered legacy CPI query parameters

Both legacy endpoints require:
- `base_year`: enum `2012`, `2010`, `2024`
- `series`: enum `Current`, `Back`
- `Format`: enum `JSON`, `CSV` (capital F)

Optional query parameters documented in the YAML:
- `year`: comma-separated YYYY values
- `month_code`: comma-separated numeric month codes
- `state_code`: comma-separated numeric codes; for group endpoint, description lists 1–36 and 99 for All India
- `sector_code`: comma-separated numeric codes; group endpoint description lists 1–3
- Group endpoint: `group_code`, `subgroup_code`
- Item endpoint: `item_code`
- For base year 2024: `division_code`, `class_code`, `sub_class_code`, `imputation_code` (Y/N)
- `limit`: integer page size (default 10)
- `page`: page number

Legacy endpoints:
- `/api/cpi/getCPIIndex` — group/subgroup indices and inflation
- `/api/cpi/getItemIndex` — item-level indices and inflation

## Important limitations / unresolved items

- The current portal's `/api/cpi/getCPIData` parameter schema was **not** recovered in this audit.
- Do not send legacy parameters to `getCPIData` without its own OpenAPI contract.
- A web retrieval attempt against the legacy API URL did not return a usable response in this environment. This is **not** an HTTP status result and is not evidence that the endpoint is down.
- No live API smoke test was completed; no observation payload, HTTP status, response content type, retrieval timestamp, or payload SHA-256 exists.
- Numeric code mappings for the exact Back-series workbook filter (All India, Rural/Urban/Combined, CPI General) must be taken from the matching 2024 API metadata, not inferred from labels.
- No rows were ingested or modified; existing workbook and normalized research panel remain unchanged.
- Factor Registry admission remains BLOCKED pending current-endpoint contract, live retrieval, payload provenance, and reconciliation.

## Next acceptance step

Retrieve the current portal OpenAPI YAML from the exact linked Swagger definition and resolve `GET /api/cpi/getCPIData` query parameters and response schema. Only then perform a single, rate-limited, minimal public GET smoke test; capture request URL, UTC retrieval timestamp, HTTP status, content type, raw response bytes and SHA-256. If the portal definition remains unavailable, retain UNKNOWN/BLOCKED and do not substitute the legacy endpoint.

## Project safety

₹0 spend. Public official sources only. No authentication bypass, paid API, fabricated timestamps, synthetic observations, or production integration. Production selector, `RANKING_SCORE`, `+1 PRESSURE_FADE`, CORE-672 and Engines A–E unchanged.
