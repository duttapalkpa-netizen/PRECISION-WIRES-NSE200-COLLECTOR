# Chapter 34 — IMF SDMX Structure vs Observation API Boundary Audit
Date: 2026-11-17 (Asia/Kolkata)
Scope: official endpoint-boundary verification; research-only.

## Result
The official IMF SDMX Central Web Services Guide (last updated May 2025) documents a public, GET-only structure-query service at:
- Base: `https://sdmxcentral.imf.org/sdmx/v2/`
- Resource: `structure`
- Supported structure resource includes `codelist`.
- URL template: `https://sdmxcentral.imf.org/sdmx/v2/structure/{resource}/{agencyID}/{resourceID}/{version}/{itemID}/?{parameters}`
- The guide explicitly classifies this service as Public and documents 200/404/500 response meanings.
- The guide's example structure request is an ECOFIN concept scheme query in SDMX 3.0.
- The structure service can retrieve structure artefacts (DSDs, codelists, dataflows, etc.); it is not itself proof of an observation-data endpoint.

A candidate codelist request can therefore be constructed from the documented pattern:
`https://sdmxcentral.imf.org/sdmx/v2/structure/codelist/IMF/CL_REF_AREA/+/?format=sdmx-2.1`
This is a documented-pattern candidate only. It was not successfully retrieved in this audit through the available browser retrieval path. Therefore India REF_AREA remains NOT_VERIFIED; no codelist value is asserted.

The separate IMF Data Portal API page says IMF data are available through SDMX 2.1 and SDMX 3.0 APIs, but directs API exploration to Swagger and states that a beta portal account is required to sign in. The available public documentation therefore establishes API families, not anonymous access, exact observation endpoint, or the request key syntax for this BOP_BPM6 pilot.

## Confirmed query semantics from official guide
- ECOFIN data examples show `DATA_DOMAIN=BOP6`, `REF_AREA`, `COUNTERPART_AREA=W1`, `FREQ=Q`, `TIME_FORMAT=P3M`, and `UNIT_MULT`.
- The guide's quarterly example explicitly uses `FREQ=Q`.
- This confirms the quarterly frequency code as documented in the guide's ECOFIN context; still preserve and verify the exact code from the captured referenced codelist before executing the observation pilot.
- No observation values were retrieved; no observation API call was made.

## Acceptance status
| Gate | Status |
|---|---|
| Official public SDMX Central structure-service base and GET scope | PASS — documented |
| Structure resource includes codelist | PASS — documented |
| Structure URL template and parameters | PASS — documented |
| Candidate CL_REF_AREA request actually retrieved | NOT_VERIFIED |
| Exact India REF_AREA code | NOT_DONE |
| FREQ=Q semantics in ECOFIN examples | PASS — documented; codelist-level confirmation pending |
| IMF Data Portal SDMX 2.1/3.0 availability statement | PASS — documented |
| Anonymous observation endpoint and key syntax | UNKNOWN / NOT_DONE |
| India quarterly BFPA/BFPL observation pilot | NOT_DONE |

## Decision
Do not guess India code, do not execute an observation query against an invented URL, and do not label any data access PASS. Next bounded action is to obtain the referenced codelist XML through a verifiable route, then establish an authorized/public observation endpoint and test a single bounded request only if public access is documented and works without credentials.

## Hard invariants
₹0; official/free sources only; no credentials or paid API; no synthetic observations or timestamps; no forward-fill; UNKNOWN is not PASS. No production selector, ranking, pressure-fade, CORE-672, Engines A–E, hard-gate, parser, registry or production workflow changes. No PR merge or production integration.

## Official sources
1. IMF SDMX Central Web Services Guide, May 2025: https://dsbb.imf.org/content/pdfs/IMFSDMXCentralWebServicesGuide.pdf (especially sections 2, 4.1–4.6; structure service entry point, Public GET access, codelist resource and URL blueprint).
2. IMF Data APIs: https://data.imf.org/en/Resource-Pages/IMF-API (SDMX 2.1/3.0 and Swagger beta-portal sign-in requirement).
