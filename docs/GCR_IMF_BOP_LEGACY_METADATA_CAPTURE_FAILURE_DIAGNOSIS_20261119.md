# IMF BOP legacy metadata capture — failed request diagnosis (2026-11-19)

## Scope
Read-only metadata retrieval only. No observations, no mapping, no production or backtest admission.

## Run evidence
- Workflow run: 44509408818
- URL: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/44509408818
- Trigger commit: b316c8de607cf5d85c2556f30d40a755bdb67ee1
- Job: 135509392076 (capture), conclusion FAILURE.
- Step 4 failed; artifact upload skipped.
- Job logs show two HTTP 400 responses:
  - DSD URL: https://api.imf.org/external/sdmx/3.0/structure/datastructure/IMF.STA/DSD_BOP/24.0.0?references=all&format=xml
  - Dataflow URL: https://api.imf.org/external/sdmx/3.0/structure/dataflow/IMF.STA/BOP/21.0.0?references=all&format=xml
- DSD error response: 392 bytes; SHA-256 74e7a371a2f0927cc5b7fddaebf4db087200a6338e966027a070054d0fd955f3
- Dataflow error response: 383 bytes; SHA-256 0b0c774c09266b1e5792094dddd3dbf9ac23ae77ac1d60411d9958c92681ae2a
- Both XML parse statuses NOT_RUN. These hashes are of HTTP error bodies, not valid metadata.

## Interpretation
- This is a request/endpoint-format failure, not evidence that the legacy DSD/dataflow or observations are absent.
- No artifact was uploaded; no successful raw metadata capture or XML validation can be claimed.
- Do not infer a legacy/current DSD crosswalk.
- IMF SDMX Central documentation describes its own registry entry point as https://sdmxcentral.imf.org/sdmx/v2/ and supports structure queries; this is a separate service from api.imf.org Data Portal API. Do not silently substitute one service for the other or assume it hosts the same IMF.STA legacy artefacts.
- Official references: https://sdmxcentral.imf.org/webservice/schema.html ; https://dsbb.imf.org/content/pdfs/IMFSDMXCentralWebServicesGuide.pdf ; https://data.imf.org/en/Resource-Pages/IMF-API

## CI isolation correction
- The NSE collector workflow paths-ignore list omitted the new legacy metadata capture script and workflow, causing the research trigger commit to start the market-data collector.
- Added both exact paths to .github/workflows/nse_collector.yml paths-ignore.
- Guard commit: 1a88a2a457a330185fd5ff766b2dff15b41fe390.
- Future path isolation must be checked before adding any research-only trigger. Do not treat any accidental NSE collector run as research evidence.

## Status and next action
- Legacy metadata capture: BLOCKED (HTTP 400; exact cause in server response body not included in job log output).
- Artifact / hashes for successful metadata: NOT_CREATED.
- Crosswalk: NOT_DONE.
- GNB current-version tests: NOT_TESTED.
- Next: inspect exact IMF Data API structure-query contract and response-body details using official API documentation; issue one minimal read-only request against a documented route, preserve the full raw error/success body, and only then capture exact versioned structures if the endpoint supports them.
- No observations, synthetic values, interpolation, scale/sign conversion, or production admission.
