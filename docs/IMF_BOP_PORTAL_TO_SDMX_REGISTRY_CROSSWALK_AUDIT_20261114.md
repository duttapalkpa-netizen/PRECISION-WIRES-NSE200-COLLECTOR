# IMF BOP Portal-to-SDMX Registry Crosswalk Audit

Audit date: 2026-11-14 (UTC)
Branch: research/imf-bop-access-audit-v1
Scope: public official catalogue metadata only. No authenticated API access, no observation rows, no production changes.

## Result

**UNRESOLVED / BLOCKED — public registry inventory completed; Portal dataset-to-SDMX dataflow crosswalk not proven.**

The official IMF Data Portal dataset page identifies the dataset as:
- Title: Balance of Payments (BOP)
- Portal URN: IMF.STA:BOP(21.0.0)
- Agency ID: IMF.STA:BOP
- Last updated: 2026-11-03T15:12:50Z
- Dataset page: https://data.imf.org/en/datasets/IMF.STA%3ABOP
- Captured page: HTTP 200, 286,418 bytes
- Raw page SHA-256: 434df7a013e62fa1d0db95d216809f17976480d8c3fc91ca2e0413d96106d9b3

The public IMF SDMX Central structure catalogue returned 101 IMF dataflow objects (HTTP 200, XML parse successful). It contained 13 BOP-related records. Their explicit DSD references were:

| Dataflow ID | Version | Referenced DSD | DSD version |
|---|---:|---|---:|
| BOP5_COLLECTION | 1.0 | ECOFIN_DSD | 1.0 |
| BOP6 | 1.1 | ECOFIN_DSD | 1.0 |
| BOP_BPM5 | 1.0 | ECOFIN_DSD | 1.0 |
| BOP_BPM6 | 1.0 | ECOFIN_DSD | 1.0 |
| BOP_GBPM6 | 2.0 | BOP | 2.0 |
| BPM6_BOP_Q | 1.5 | BOP | 1.5 |
| BPM6_RA_M | 1.0 | BOP | 1.2 |
| DSE_GBPM6 | 2.0 | BOP | 2.0 |
| EXD_GBPM6 | 2.0 | BOP | 2.0 |
| IIP_GBPM6 | 2.0 | BOP | 2.0 |
| ILV1_GBPM6 | 2.0 | BOP | 2.0 |
| ILV2_GBPM6 | 2.0 | BOP | 2.0 |
| ZZZNL_TEST | 1.0 | BOP | 1.1 |

Important: the inventory did not find a BOP-related IMF dataflow whose DSD reference is IMF:BOP:2.6.0. The BOP DSD 2.6.0 previously retrieved and parsed successfully is a valid public registry structure, but its presence does not prove it is the DSD used by the Portal dataset IMF.STA:BOP(21.0.0).

## Portal API access evidence

The official IMF API help page states that IMF datasets are available through SDMX 2.1 and SDMX 3.0 APIs. It also says the Swagger/API explorer requires signing in with a beta portal account:
- API help: https://data.imf.org/en/Resource-Pages/IMF-API
- Captured HTTP 200, 203,102 bytes
- Raw SHA-256: 7004a1655ea132ea2fe9e39cc11406656dae080d4bbc5d67ecb20e715114855b

The Portal API explorer request:
- Requested URL: https://portal.api.imf.org/apis
- HTTP response: 200 HTML after redirect
- Final URL: https://portal.api.imf.org/signin?returnUrl=%2Fapis
- Captured bytes: 4,654
- Raw SHA-256: eb094d79d1f431a2020e77b80a3e1aff00e9dfb7a47fe29b7ce8ba0a35324e99

This is a sign-in redirect, not a public API schema response. No account credentials were supplied, no sign-in was attempted, and no restricted endpoint was queried. No attempt was made to bypass authentication.

## Public source hashes

- IMF SDMX Central Dataflow catalogue: HTTP 200; 448,310 bytes; SHA-256 `547fa36a26e2859301013ea52d05fcbfd99f2cd068afa619696e412bc4760693`.
- Portal BOP dataset page: HTTP 200; 286,418 bytes; SHA-256 `434df7a013e62fa1d0db95d216809f17976480d8c3fc91ca2e0413d96106d9b3`.
- IMF API help page: HTTP 200; 203,102 bytes; SHA-256 `7004a1655ea132ea2fe9e39cc11406656dae080d4bbc5d67ecb20e715114855b`.
- Portal API sign-in redirect page: HTTP 200 after redirect; 4,654 bytes; SHA-256 `eb094d79d1f431a2020e77b80a3e1aff00e9dfb7a47fe29b7ce8ba0a35324e99`.

## GitHub Actions evidence

- Run ID: 43600890212 — SUCCESS; all audit and artifact-upload steps completed.
- Run URL: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/43600890212
- Workflow commit: `1f6be23493e78cbf2c4a4fced7a810b0313597f7`
- Artifact ID: 14115559741
- Artifact ZIP SHA-256: `2ef0f095cc0e0d2b7b1a29a86591ced09bda2d1100b44043c493c18cd005c716`
- Artifact re-downloaded and local SHA-256 independently matched the GitHub upload digest.
- Artifact files: raw IMF dataflow XML, raw Portal dataset HTML, raw API help HTML, raw API sign-in HTML, JSON crosswalk inventory.

## Acceptance matrix

| Check | Status |
|---|---|
| Official Portal dataset identity IMF.STA:BOP(21.0.0) captured | PASS |
| Official IMF SDMX Central IMF dataflow catalogue retrieved and parsed | PASS |
| All BOP-related IMF dataflow IDs and DSD references inventoried | PASS |
| Candidate IMF:BOP DSD 2.6.0 reference found in BOP-related dataflows | NOT FOUND |
| Portal dataset URN crosswalked to a specific SDMX Central dataflow | UNKNOWN |
| Portal API schema/dataflow metadata publicly inspectable without sign-in | BLOCKED |
| Authorized observation endpoint and access scope verified | BLOCKED |
| India BOP observations acquired | NOT DONE |
| EMDE reporter coverage reconciled | NOT DONE |
| EM portfolio-flow aggregate | BLOCKED |

## Interpretation and next safe action

The public SDMX Central dataflow catalogue is a separate registry namespace from the IMF Data Portal dataset catalogue. Similar names and shared BOP subject matter do not establish identity. The Portal dataset URN IMF.STA:BOP(21.0.0) must not be equated with IMF:BOP_GBPM6(2.0), IMF:BPM6_BOP_Q(1.5), or the BOP DSD 2.6.0 structure without a source-backed crosswalk.

The next legitimate action is to obtain an authorized beta-portal account/session from the user or find an IMF-published public endpoint/document that explicitly maps the Portal dataset URN to its SDMX dataflow and key. Until then, retain the dataflow crosswalk as UNKNOWN and observation acquisition as BLOCKED. Do not fabricate a data key or infer the API endpoint from the DSD.

## Invariants

Research-only, ₹0 spend, official sources only. No paid API, no external contact, no authentication bypass, no synthetic data/timestamps, no PR merge, no production changes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, all engines and hard-gate logic unchanged.
