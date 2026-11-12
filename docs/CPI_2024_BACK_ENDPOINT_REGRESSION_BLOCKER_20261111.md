# CPI 2024 Back-Series Retrieval Blocker — Maintainer Regression Evidence — 2026-11-11

## Decision

**BLOCKED — do not repeatedly retry the 2024 CPI live endpoint until an upstream fix or a new verified success signal exists.**

## New evidence

The NSO India-maintained `esankhyiki-mcp` repository CHANGELOG explicitly records:

> "CPI test switched to base_year=2012 to bypass an upstream 400 regression on the 2024 endpoint"

Source:
https://github.com/nso-india/esankhyiki-mcp/blob/main/CHANGELOG.md

The changelog places this note in release 2.2.0 (2026-04-30). This is direct maintainer-reported evidence of an upstream HTTP 400 regression affecting the 2024 CPI endpoint at the time of that release. It is not proof that the regression remains present on 2026-11-11, but it materially raises the risk of a repeated 2024 request failing.

## Reconciliation with previously verified facts

- Current portal advertises `GET /api/cpi/getCPIData` for the CPI API.
- NSO India-maintained `mospi-esankhyiki` client routes CPI 2024 Group/Item data requests to `https://api.mospi.gov.in/api/cpi/getCPIData`.
- The client discovers valid CPI filters through `GET /api/cpi/getCpiFilterByLevelAndBaseYear` with `base_year`, `level`, and `series_code`.
- The older OpenAPI YAML defines legacy `getCPIIndex` and `getItemIndex` parameter sets; it is not a direct OpenAPI definition of the unified `getCPIData` endpoint.
- Therefore, the legacy YAML must not be described as the independently downloaded current endpoint OpenAPI schema.

## Safe execution decision

1. Do not hammer or automatically retry the 2024 endpoint.
2. Do not substitute 2012 CPI observations for the user's 2024 Back-series panel.
3. Do not assume the 2024 API is currently down: the maintainer note is historical regression evidence, not a current HTTP response.
4. Do not infer state/sector/division numeric codes.
5. Retain the uploaded 432-row official 2024 Back-series workbook and its QA as a separate evidence-backed local dataset; provenance metadata gaps remain as previously recorded.
6. If a future normal public GET is attempted, perform only one low-volume metadata request first, capture the actual HTTP status and response bytes, and stop on HTTP 400/429/5xx. Retry only after a documented upstream fix or controlled retry-after interval.
7. In the meantime, advance other independent M6 official macro-source ingestion work rather than spending time repeatedly probing a known-risk endpoint.

## Status

- Endpoint path / maintained-client routing: VERIFIED.
- Legacy endpoint OpenAPI parameter definitions: VERIFIED for legacy endpoints only.
- Unified 2024 endpoint exact OpenAPI schema: NOT_INDEPENDENTLY_RETRIEVED.
- Maintainer-reported upstream 400 regression: VERIFIED AS HISTORICAL CHANGELOG EVIDENCE.
- Current live endpoint status: UNKNOWN.
- Live metadata smoke test: NOT_DONE.
- New CPI observations ingested: NO.
- Factor Registry admission: BLOCKED.
- CPI workbook/panel content: unchanged.

## Safety and invariants

₹0 spend; public evidence only; no synthetic observations, fabricated timestamps, guessed codes, auth bypass, paid APIs, or production integration. Production selector, `RANKING_SCORE`, `+1 PRESSURE_FADE`, CORE-672, and Engines A–E remain unchanged.
