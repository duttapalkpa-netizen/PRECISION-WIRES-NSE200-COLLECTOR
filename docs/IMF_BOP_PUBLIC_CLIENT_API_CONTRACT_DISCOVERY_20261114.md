# IMF BOP Public Client API Contract Discovery and Endpoint Probe

Audit date: 2026-11-14 (UTC)
Branch: research/imf-bop-access-audit-v1
Scope: public IMF BOP dataset page and its first-party client bundles; read-only endpoint probe. No authentication, no API bypass, no observations.

## Executive outcome

**CLIENT CONTRACT DISCOVERY: PASS. LIVE STRUCTURE ENDPOINT: BLOCKED. DATAFLOW CROSSWALK: UNKNOWN.**

The official BOP dataset page exposes an API link, View Data, and Download controls. Its first-party Next.js client bundle contains SDMX 3.0 API URL templates. The bundle's copied-data-link template is:

```text
https://api.imf.org/external/sdmx/3.0/data/dataflow/{agencyID}/{resourceID}/{version}/{dimensionKey}?c[TIME_PERIOD]=ge:{startDate}+le:{endDate}&dimensionAtObservation=AllDimensions&attributes=all&detail=full&includeHistory=true&limit=100
```

The bundle also constructs a structure URL template:

```text
https://api.imf.org/external/sdmx/3.0/structure/dataflow/{agencyID}/{resourceID}/{version}?detail=full&references=all
```

The dataset page's captured URN is `IMF.STA:BOP(21.0.0)`. Parsing this as agency/resource/version gives a candidate request path, but this does not by itself prove that it is an actual SDMX dataflow identifier. The route template is source-code evidence of what the first-party client constructs, not an independent guarantee that every route supports anonymous access.

## Endpoint probe

Candidate structure request tested:

```text
https://api.imf.org/external/sdmx/3.0/structure/dataflow/IMF.STA/BOP/21.0.0?detail=full&references=all
```

Two read-only probes were made:
1. Accept: SDMX 3.0 JSON first — HTTP 400, message: “This endpoint does not support json version 3.0”.
2. Accept: SDMX 3.0 XML only — HTTP 400, message: “This endpoint does not support xml version 3.0”.

The response paths resolve through IMF's API gateway, but the structure resource does not support either tested SDMX 3.0 representation. Therefore:
- Candidate structure endpoint: BLOCKED / unsupported representation.
- Dataflow identity IMF.STA:BOP(21.0.0) as an SDMX dataflow: UNKNOWN.
- No DSD or dimension list was returned.
- No data query was attempted because the required dimension key and dataflow identity are not verified.
- No observation row was acquired.

This test corrects the previous assumption that the frontend's structure URL template could be called successfully as an SDMX 3.0 structure resource. The route string exists in the client code; the server response rejects both XML and JSON 3.0 structure representations.

## First-party client bundle evidence

- Dataset page: https://data.imf.org/en/datasets/IMF.STA%3ABOP
- HTTP 200; 286,324 bytes; SHA-256 `b4c37f5b9bc3013cef59a631acd9d16fd0f828653e1ce75a0361b9c08e63d456`.
- Eleven Next.js chunks were retrieved. The principal route-containing page bundle:
  `https://data.imf.org/_next/static/chunks/pages/%5B%5B...path%5D%5D-d978758aba7bb98c.js`
- Bundle size: 1,081,179 bytes.
- Bundle SHA-256: `b60dc6bfb92b8989965c33b9e17b54704f5df7092f80ba0e26327455424e8dd9`.
- Client-bundle inventory records route templates and exact source asset hashes.
- Client-bundle workflow Run ID: 43601835131 — SUCCESS.
- Workflow commit: `46dfd2f72312ca48e824515ec7b0d3cf2031ce84`.
- Artifact ID: 14117155347.
- Artifact ZIP SHA-256: `31a0d0add766bc66e928624c18979692045fdb09a10c9fea88f83cf704259963`.

## Failed live probes preserved

- Probe Run #43601889079: HTTP 400, JSON 3.0 unsupported; response body SHA-256 `be55c218632cab1444443c40d1ce720cbc7150a5f403d65aa53ecf62f651ccb2`.
- Probe Run #43601964709: HTTP 400, XML 3.0 unsupported; response body SHA-256 `59bd7d800cf108ce237613c9419e23d6bc269d23a58432984e14dbed866d7195`.
- Second probe artifact ID: 14115719310; ZIP SHA-256 `613883f8b5102a35451b4830fa275001cc5cf8218a7e70fc7b79d521d302d794`.
- Both failures are retained as diagnostic evidence, not overwritten or relabelled PASS.

## Acceptance update

| Gate | Status |
|---|---|
| Official BOP dataset page and URN captured | PASS |
| First-party API client route templates extracted | PASS |
| Candidate data URL template documented | PASS (template only) |
| Candidate structure URL tested with SDMX 3.0 JSON | BLOCKED (HTTP 400 unsupported) |
| Candidate structure URL tested with SDMX 3.0 XML | BLOCKED (HTTP 400 unsupported) |
| Portal URN mapped to an active SDMX dataflow/DSD | UNKNOWN |
| Dimension IDs and key order validated | NOT DONE |
| India BOP observations acquired | NOT DONE |
| EMDE reporter coverage reconciled | NOT DONE |
| EM aggregate | BLOCKED |

## Next action

Investigate the SDMX 2.1/3.0 registry stream endpoints and the API's documented metadata-query operation using only first-party public documentation and unauthenticated read-only requests. If metadata remains behind beta-portal sign-in, stop and request an authorized API schema export from the account owner. Do not guess dimension IDs, dimension order, API keys, or observation URLs. Do not use the client bundle's data URL with a fabricated key.

## Invariants

Research-only, ₹0 spend, official sources only. No paid API, no credentials, no authentication bypass, no synthetic data/timestamps, no external contact, no PR merge, no production changes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, engines and Hard Gate unchanged.
