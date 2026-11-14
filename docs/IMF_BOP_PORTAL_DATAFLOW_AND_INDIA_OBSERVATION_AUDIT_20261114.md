# IMF BOP Portal Dataflow Crosswalk and India Portfolio Observation Audit

Audit date: 2026-11-14 (UTC)
Branch: research/imf-bop-access-audit-v1
Scope: official IMF Data Portal SDMX 2.1 structure and SDMX 3.0 data APIs; unauthenticated read-only retrieval; one India annual portfolio-investment asset-side series. No aggregation or production changes.

## Executive result

**PORTAL DATAFLOW CROSSWALK: PASS. PUBLIC OBSERVATION ACCESS: PASS. INDIA NARROW SERIES SAMPLE: PASS (11/11 periods). FULL INDIA PANEL: NOT DONE. EM AGGREGATION: BLOCKED.**

The correct IMF Data Portal SDMX 2.1 REST 1.x route was identified. The Portal's own Dataflow object was retrieved:
- Agency: IMF.STA
- Dataflow: BOP
- Version: 21.0.0
- Exact DSD reference: IMF.STA:DSD_BOP(24.0.0)

This directly maps the Portal dataset URN `IMF.STA:BOP(21.0.0)` to the Portal Dataflow `IMF.STA:BOP(21.0.0)` and DSD `IMF.STA:DSD_BOP(24.0.0)`. This is not a name-based inference from SDMX Central's separate IMF registry namespace.

A public SDMX 3.0 data query then returned 11 actual annual observations for India for 2015–2025. No sign-in, credentials, paid API, or authentication bypass was used.

## 1. Correct SDMX 2.1 route and crosswalk

### Path correction retained

The initial probe incorrectly inserted a `/structure/` path segment. That route returned HTTP 404 with body:
`{"status":404,"code":40411,"message":"No such artefact type: *",...}`.
The failure was retained as a diagnostic; it was not promoted to PASS.

The standard SDMX-REST 1.x resource path without that prefix succeeded:
`https://api.imf.org/external/sdmx/2.1/dataflow/IMF.STA/BOP/21.0.0?references=all`

Response:
- HTTP 200
- Content-Type: `application/vnd.sdmx.structure+xml;version=2.1`
- 3,965,650 bytes
- SHA-256: `e9414015aaf3480d8254f2935eb4f723f8b50196f104881d7cf29454bfb12ce5`
- Parsed Dataflow: IMF.STA:BOP(21.0.0)
- Explicit DSD reference: IMF.STA:DSD_BOP(24.0.0)

The alternate `/datastructure/IMF.STA/BOP/21.0.0` request returned HTTP 204 with an empty body; it was not treated as DSD evidence. The actual DSD reference came from the Dataflow response itself.

### DSD_BOP 24.0.0 direct component inventory

The Dataflow response included the pinned DSD and its descendant structures/codelists. Direct parsing of the DSD's own DataStructureComponents yielded:
- 6 dimensions: COUNTRY, BOP_ACCOUNTING_ENTRY, INDICATOR, UNIT, FREQUENCY, TIME_PERIOD.
- TIME_PERIOD is the observation-level time dimension.
- 45 attributes.
- 1 primary measure: OBS_VALUE.

Dimension order for the series key (time dimension excluded):
1. COUNTRY
2. BOP_ACCOUNTING_ENTRY
3. INDICATOR
4. UNIT
5. FREQUENCY

The DSD's ConceptScheme references establish:
- COUNTRY -> IMF.STA:CL_BOP_COUNTRY(1.0.0)
- BOP_ACCOUNTING_ENTRY -> IMF.STA:CL_BOP_ACCOUNTING_ENTRY(3.3.0)
- INDICATOR -> IMF.STA:CL_BOP_INDICATOR(10.0.0)
- UNIT -> IMF:CL_UNIT(2.11.2)
- FREQUENCY -> IMF:CL_FREQ(1.2.0)

Verified values:
- COUNTRY `IND` = India.
- BOP_ACCOUNTING_ENTRY `A_NFA_T` = Assets, Net acquisition of financial assets.
- INDICATOR `P_F` = Portfolio investment, Total financial assets/liabilities.
- UNIT `USD` = US dollar.
- FREQUENCY `A` = Annual; `Q` = Quarterly.

The exact key used for the sample was therefore:
`IND.A_NFA_T.P_F.USD.A`

### Key-code correction

The first sample key used `INDICATOR=P`. Although P exists in the indicator codelist as “Portfolio investment”, the India series-group inventory showed that the actual total financial asset/liability aggregate is `P_F`; the P key did not return observations. The key was corrected using the exact CL_BOP_INDICATOR label and the Dataflow response's observed group inventory. No data values were fabricated or inferred.

## 2. Public India observation access — verified

Exact request:

```text
https://api.imf.org/external/sdmx/3.0/data/dataflow/IMF.STA/BOP/21.0.0/IND.A_NFA_T.P_F.USD.A?c[TIME_PERIOD]=ge:2015-A1+le:2025-A1&dimensionAtObservation=AllDimensions&attributes=all&detail=full&includeHistory=true&limit=100
```

Both supported representations returned HTTP 200:
- SDMX-JSON 2.0.0: 49,654,152 bytes; SHA-256 `844f253263c00e77b7d0ee572a47dd01dc258c7b3eb0bc4b5f1eba9daac59a25`.
- SDMX-ML 3.0.0: 122,045,648 bytes; SHA-256 `ca4676dbccb82383b7e549922169729c40084ec0d1c3eec4208f4ae4b1c25471`.

Both responses contain 11 observations for the exact India key and period range. The XML response also included 405,562 Group metadata nodes, making the full representation unnecessarily large for a narrow series extraction.

### Compact data-only response — validated

The same series and period range was requested using:
- `dimensionAtObservation=TIME_PERIOD`
- `attributes=all`
- `detail=dataonly`
- `limit=100`
- Accept: `application/vnd.sdmx.data+json;version=2.0.0`

Result:
- HTTP 200
- 7,845 bytes
- SHA-256: `85cca14cabf7a674ba37c00f88e3140f562480130bdde57d4902562fa6e0e23a`
- 11/11 observations parsed
- Time periods exactly 2015–2025
- Explicit series dimensions and observation-level time dimension present in the JSON structure.

Compared with the full JSON response (49,654,152 bytes), the compact data-only response is approximately 99.9842% smaller while preserving all 11 observations and requested attributes. This is the preferred extraction profile for subsequent narrow pulls.

### Parser correction

The first compact probe used `attributes=none`. It returned a valid compact SDMX-JSON body with observations nested under `dataSets[0].series[*].observations`, not `dataSets[0].observations`. The initial parser looked only for the latter and reported zero rows. Inspection of the raw JSON confirmed the 11 rows; the parser was corrected to traverse series keys and observation indexes. The follow-up `attributes=all`, `detail=dataonly` run parsed all 11 rows and retained attributes. The first parser result remains preserved; it is not relabelled as a successful row parse.

## 3. Verified India annual portfolio asset observations

All values below are raw IMF response strings in USD; no conversion, rescaling, imputation, or aggregation has been applied.

| Year | OBS_VALUE (USD) |
|---:|---:|
| 2015 | -279742829.086578 |
| 2016 | 572919484.2881465 |
| 2017 | 281669940.6064565 |
| 2018 | -1719691073.628995 |
| 2019 | 2179509031.003673 |
| 2020 | 681396183.8648327 |
| 2021 | 2689366887.453217 |
| 2022 | 1173569677.79838 |
| 2023 | 433676031.9214586 |
| 2024 | 42229946.89046127 |
| 2025 | 1107624645.420241 |

Common series dimensions:
- COUNTRY=IND
- BOP_ACCOUNTING_ENTRY=A_NFA_T
- INDICATOR=P_F
- UNIT=USD
- FREQUENCY=A

### Observation and series attributes

Series-level:
- SCALE=6 (preserved as source metadata; no scaling transformation applied)
- METHODOLOGY=BPM6

Observation-level:
- PRECISION=6
- DERIVATION_TYPE=O, IMF codelist label “Reported official data”
- STATUS is null/absent
- ACCESS_SHARING_LEVEL=PUBLIC_OPEN, label “Public (Unrestricted)”
- ACCESS_SHARING_NOTES is null/absent
- SECURITY_CLASSIFICATION=PUB, label “Public or Unrestricted”
- SOURCE is null/absent at observation level

The dataset-level source/citation metadata is separate from row-level SOURCE and is not assigned to individual observations. Missing STATUS/SOURCE attributes remain null; they are not converted to PASS or to inferred values.

## 4. Persistent CSV and provenance manifest

Committed research data:
- CSV: `data/research/imf_bop_india_portfolio_assets_usd_annual_2015_2025.csv`
- Rows: 11
- CSV SHA-256: `60e557c922763f145284c6243e4612d6c05c0ce756c6f2d8846e0ea2fc7c8697`
- CSV commit: `47bc2c83bc60aec0bfebb4cb765f5884af84dbd7`

Manifest:
- `data/research/imf_bop_india_portfolio_assets_usd_annual_2015_2025.manifest.json`
- Final manifest commit: `4c6d19533ce8c57564376f6fadf5e3055a67d42a`
- Manifest records exact dataflow, DSD, key, query parameters, raw body hash, artifact hash, attribute interpretation, scope limits, and unchanged production invariants.

### GitHub Actions evidence

**Portal Dataflow/DSD probe**
- Run #43615378167 — SUCCESS.
- Commit: `0405347ac4fb2944b0bdc89fd4159b26e90ea8fb`.
- Artifact ID: `14122440301`.
- Artifact ZIP SHA-256: `2411f5837d7145ed6450a1423b17282f240cda6b7b6d61d842e4c18a6e88c125`.
- Dataflow response SHA-256: `e9414015aaf3480d8254f2935eb4f723f8b50196f104881d7cf29454bfb12ce5`.

**India full observation smoke test**
- Run #43615740505 — SUCCESS.
- Commit: `4d3630d7fb8d196bb2af74870e2963ef831a9293`.
- Artifact ID: `14121942694`.
- Artifact ZIP SHA-256: `e9d2b920a658870f0f4eb9abf60bc82815ed945b4ef0d9f1a96e3bc66c00d666`.

**India compact data-only extraction**
- Run #43616059985 — SUCCESS.
- Commit: `e6d54ed5507bcc8a6cd4054dd44ecc7c3ceef863`.
- Artifact ID: `14122421554`.
- Artifact ZIP SHA-256: `cc951e2655dc4592ab82d848e0beebc43970132de1f4f3edc5c3ef8b56aaed23`.
- Compact response SHA-256: `85cca14cabf7a674ba37c00f88e3140f562480130bdde57d4902562fa6e0e23a`.

## 5. Acceptance matrix

| Gate | Status |
|---|---|
| Official Portal dataset identity captured | PASS |
| Portal SDMX 2.1 Dataflow identity and exact DSD reference | PASS |
| DSD_BOP 24.0.0 direct component inventory | PASS |
| Dimension/codelist key values for the sample verified | PASS |
| Public unauthenticated SDMX 3.0 observation endpoint | PASS |
| India annual portfolio asset series 2015–2025, 11/11 rows | PASS (narrow series only) |
| Compact data-only extraction and parser QA | PASS |
| India liability-side portfolio series | NOT DONE |
| India quarterly portfolio series | NOT DONE |
| Full India BOP portfolio panel and revisions reconciliation | NOT DONE |
| 154-economy EMDE reporter coverage in this dataflow | NOT DONE |
| EM portfolio-flow aggregate | BLOCKED |

IMF BOP workstream remains 5/7 accepted gates (71.4%) on the existing seven-gate rubric: the Portal crosswalk has moved from UNKNOWN to PASS. The narrow India sample is evidence of public observation access, but it does not complete the full India-panel acquisition gate. EM aggregation remains blocked.

Project-wide PRECISION-WIRES V11.3 progress remains NOT_CALCULABLE until all workstream gates and weights are reconciled. Do not substitute the IMF BOP workstream percentage for project-wide progress.

## 6. Next highest-value action

Use the compact data-only profile to acquire, separately:
1. India portfolio-investment liability-side annual series using the DSD-confirmed key `IND.L_NIL_T.P_F.USD.A`.
2. India quarterly assets and liabilities using `FREQUENCY=Q` and quarter-specific time filters.
3. Reconcile values, revisions, period coverage, status and derivation flags; keep assets and liabilities separate.
4. Only then begin country-by-country EMDE reporter coverage checks using the already versioned WEO 154-economy crosswalk.

No EM aggregate until reporter availability, periods, instruments, units, flags, and data vintage are reconciled for the accepted universe.

## Invariants

Research-only; ₹0 spend; free official sources only; no paid API; no login or authentication bypass; no synthetic observations or timestamps; no external contact; no PR merge; no production changes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, all five engines and Hard Gate unchanged.
