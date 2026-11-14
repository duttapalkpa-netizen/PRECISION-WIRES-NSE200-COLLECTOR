# IMF BOP Portfolio-Flow Extraction Specification V1

Audit date: 2026-11-10 (Asia/Kolkata)
Status: METADATA/EXTRACTION CONTRACT ONLY — NO COUNTRY OBSERVATIONS EXTRACTED
Scope: free IMF-published data only; research branch; no production signal.

## 1. Verified source route

- Dataset: IMF Balance of Payments (BOP), dataset identifier displayed by IMF as `IMF.STA:BOP`.
- Official dataset page: https://data.imf.org/en/datasets/IMF.STA%3ABOP
- Official API documentation: https://data.imf.org/en/Resource-Pages/IMF-API
- IMF states that its data are accessible through SDMX 2.1 and SDMX 3.0 APIs.
- IMF's API page links to a Swagger explorer and states that a beta portal account is required to sign in there. This audit has not authenticated, downloaded, or validated a BOP observation payload. Do not describe the raw data endpoint as anonymously tested.
- The SDMx Global Registry publishes the IMF-maintained BOP DSD V2.6.0 (published December 2025) and states registry access is unauthenticated. SDMX-ML 2.1 structure URL: https://registry.sdmx.org/sdmx/v2/structure/datastructure/IMF/BOP/2.6.0/?format=sdmx-2.1 . The official SDMx page also provides the SDMX 3.0 structure link. The XML payload itself was not parsed in this audit because the web viewer rejected application/xml; therefore dimension/codelist mapping remains UNKNOWN until the raw XML is downloaded and archived.
- IMF SDMX Central's public structure service is documented at https://sdmxcentral.imf.org/sdmx/v2/ and its web-services guide specifies public GET access for structure queries. This is metadata access, not proof of public BOP observations.
- The IMF Data Portal API page documents SDMX 2.1/3.0 data APIs but says the Swagger explorer requires beta-portal sign-in. No authenticated data API session was used. Dataset page provides VIEW DATA and DOWNLOAD controls; actual download has not yet been tested.

## 2. Required extraction target

Extract only BOP financial-account **portfolio investment transactions**. Preserve separately:
- Equity and investment-fund shares
- Debt securities (short-term and long-term, if the official structure supports the split)
- Assets and liabilities, separately
- Credits/debits or the official net acquisition/net incurrence representation, exactly as defined in the selected BOP vintage

Do not assume SDMX dimension codes, codelist values, sign conventions, units, or a single net-flow variable from a display label. Apply a metadata-first extraction: retrieve and archive the exact DSD, codelists, dataflow, annotations, and dataset vintage. Map official dimension values to human-readable fields only after inspecting those metadata.


## 2A. Independently documented BOP DSD V2.6.0 component crosswalk

A current European Commission/Eurostat BOP Vademecum (updated November 2025 / July 2026) identifies the BOP DSD V2.6.0 dimensions and attributes. This is a standards cross-check for the shared BOP DSD, **not evidence that an IMF Data Portal dataflow uses the same selected series or country coverage**.

| DSD component | Meaning | Extraction handling |
|---|---|---|
| FREQ | Frequency | Preserve Q/A as transmitted; do not mix quarterly and annual series |
| REF_AREA | Reporting economy/area | Primary country key |
| ADJUSTMENT | Seasonal/calendar adjustment | Keep separate; don't combine adjusted and unadjusted series |
| COUNTERPART_AREA | Counterpart economy/area | Preserve, including world/region codes; avoid double counting bilateral and total |
| REF_SECTOR / COUNTERPART_SECTOR | Institutional sectors | Retain exact scope; total economy vs sector-specific is not interchangeable |
| FLOW_STOCK_ENTRY | Transactions / positions / other changes | Select transaction code only after reading CL_FSENTRY |
| ACCOUNT_ENTRY | Accounting entry | Keep net acquisition of assets distinct from net incurrence of liabilities |
| INT_ACC_ITEM | International accounts item | Financial account selection must be confirmed against CL_ACCOUNTS_ITEM |
| FUNCTIONAL_CAT | Functional investment category | Portfolio investment classification; verify code list |
| INSTR_ASSET | Financial instrument/asset | Preserve equity/investment-fund shares vs debt instruments; do not infer from text |
| MATURITY | Original/remaining maturity | Retain debt maturity split when supplied; equity maturity is not applicable |
| UNIT_MEASURE / CURRENCY_DENOM | Reporting unit / currency of denomination | Preserve both, not interchangeable |
| VALUATION / COMP_METHOD / TYPE_ENTITY | Valuation, compilation method, entity type | Preserve series qualifiers and breaks |

Vademecum further documents observation-level `OBS_STATUS` and `CONF_STATUS`, and series-level `UNIT_MULT` and `DECIMALS`. These are required ingestion fields, not optional decoration. The exact IMF dataflow's attributes and codelist values still need direct comparison before extraction is accepted.

### Sign and key rules confirmed from the Vademecum
- For BPM6 financial-account entries, the updated terminology is net acquisition of assets and net incurrence of liabilities; positive values indicate an increase and negative values a decrease in the respective asset or liability. Never apply an extra sign flip without a separately documented transformation.
- A complete SDMX series key includes all DSD dimensions. Deduplicate on the complete dimension key plus time period and vintage, not merely country + period.
- The Vademecum's sample series keys and code values are European transmission examples. Do not copy its Eurostat-specific dataset IDs or country coverage into the IMF dataflow without verification.

### Practical example (standards illustration, not an IMF observation)
A quarterly series with `FLOW_STOCK_ENTRY = T` is explicitly labelled transactions in the Vademecum example. If an asset-side financial-account transaction is +10 in the source unit, that denotes an increase in the asset under the documented BPM6 convention; it is not automatically a +10 net inflow into the reporting economy. A liability-side +10 denotes an increase in liabilities. Keep these as separate columns and preserve the source unit/multiplier.

## 3. Raw observation contract

Every downloaded observation must retain:
- reporting economy code and label
- frequency and reference period
- BOP standard/version (e.g. BPM6/BPM7) and dataflow/version
- official dimension key and all dimension values
- portfolio instrument classification
- asset/liability or official accounting-entry classification
- measure/transaction basis and unit/currency
- unit multiplier / scale
- numeric value exactly as published
- observation status / confidentiality / estimation flags
- source URL and dataset identifier
- retrieval timestamp (UTC), publication/release vintage, and file checksum

No synthetic rows, values, timestamps, or mappings are permitted. No conversion to USD, no annualisation, no aggregation, and no sign inversion may occur in the raw layer. Any derived field must be a separate, documented transformation with its own test.

## 4. EM panel membership and aggregation gate

No EM aggregate is accepted until a versioned country-membership file is committed with:
1. Explicit classification authority and edition/vintage (do not silently mix IMF WEO, World Bank, MSCI or other classifications).
2. Included and excluded economy codes, with rationale for exclusions.
3. A declared equal-weight or other defensible weighting rule. Do not sum currencies or units across economies.
4. Harmonised currency and scale conversion method, source, timestamp and FX convention if a USD aggregate is later calculated.
5. Instrument coverage, BPM basis, frequency, reporting-period alignment, net/gross definition and missing-reporter coverage.
6. Duplicate/revision handling and a publication-vintage policy.

Until those requirements pass, `em_portfolio_flow_usd_bn` remains UNKNOWN. Never infer a global EM total from a partial convenience sample or from IMF PIP/CPIS positions.

## 5. Validation gates before a panel can be marked VERIFIED

- Exact series key uniqueness at economy × frequency × period × instrument × direction × measure × vintage.
- No duplicate observations unless they are explicitly distinct vintages or dimensions.
- Valid ISO reporting-period format and supported frequency.
- Numeric values finite; missing/suppressed values remain missing, never zero.
- Unit and multiplier present and consistent within any aggregation group.
- Sign convention verified against IMF metadata and, where possible, one country statistical release.
- BPM5/BPM6/BPM7 breaks identified; do not concatenate incompatible bases without an approved bridge.
- Assets/liabilities and equity/debt never collapsed before the requested output definition is explicit.
- Country coverage denominator and missingness reported for every period.
- Retrieval timestamp, source URL, raw file SHA-256 and dataset vintage retained.
- A sample of observations reconciled to the IMF portal's displayed table/download.

## 6. Practical example (illustrative only; not observed data)

Suppose Economy X reports quarterly portfolio-liability transactions of +12.0 in its local-currency unit and Economy Y reports -4.0 in a different currency. These values must **not** be added as +8.0 or labelled USD flows. First confirm the official meaning/sign of each observation, convert each using a declared period-consistent FX method, align periods and instruments, then aggregate only across the committed EM membership list. If Y's observation is missing, report the coverage gap; do not replace it with zero.

## 7. Current audit outcome

| Check | Result |
|---|---|
| Official BOP dataset identified | PASS |
| Official SDMX 2.1/3.0 API route documented | PASS |
| BOP frequency (annual/quarterly) confirmed | PASS |
| Official BOP DSD V2.6.0 public registry URL and version identified | PASS |
| Exact BOP DSD/codelist dimension mapping downloaded, parsed and archived in this repo | UNKNOWN / NOT DONE |
| IMF BOP observation download tested and reconciled | UNKNOWN / NOT DONE |
| Country-level portfolio transaction panel extracted | UNKNOWN / NOT DONE |
| Versioned EM country membership committed | UNKNOWN / NOT DONE |
| EM aggregate calculated and reconciled | UNKNOWN / NOT DONE |
| Daily trading trigger suitability | FAIL — BOP is annual/quarterly, not a daily trigger |

This specification is an extraction contract and source audit, not a claim that IMF data have already been extracted. It does not change the production selector, ranking score, pressure-fade logic, CORE-672 diagnostics, engines, or Hard Gate.


## 2B. Reproducible IMF SDMX Central DSD retrieval recipe (verified API contract)

The IMF SDMX Central Web Services Guide (last updated May 2025) specifies public access for the Structure Web Service, HTTP GET, entry point `https://sdmxcentral.imf.org/sdmx/v2/`, resource type `datastructure`, path parameters `agencyID`, `structureID`, and `version`, `references=children` to return referenced structures such as codelists, and `format=sdmx-2.1` plus `prettyPrint=true` for formatted XML. It also documents `saveAs` as a request parameter that sets Content-Disposition to an attachment and lets the server choose the extension from the response format; this is used below to request a direct file download.

**Exact request to execute and archive:**

```text
https://sdmxcentral.imf.org/sdmx/v2/structure/datastructure/IMF/BOP/2.6.0/?format=sdmx-2.1&references=children&detail=full&prettyPrint=true&saveAs=IMF_BOP_DSD_2_6_0
```

This URL is constructed from the official guide's documented entry point, resource, path parameters and request parameters. It is a reproducible request specification, **not evidence that this audit successfully retrieved the response**. The prior download attempt in this environment failed before an HTTP response body was obtained. Therefore:
- response HTTP status: UNKNOWN;
- XML byte count and SHA-256: NOT AVAILABLE;
- parsed component and codelist counts: UNKNOWN;
- no IMF-specific code mapping is promoted to PASS.

### Execution and acceptance procedure

1. Request the URL above using an HTTP client with redirects enabled; save response headers and body without modifying the body.
2. Accept only HTTP 200 with an XML media type and a parseable SDMX-ML document. Record HTTP status, Content-Type, retrieval timestamp (UTC), final URL and byte count.
3. Compute SHA-256 over the exact saved response bytes before parsing.
4. Parse with a namespace-aware XML parser; reject HTML error pages, empty responses, malformed XML, or an SDMX error message.
5. Inventory the DSD identity/version, dimensions, measures, attribute attachment levels, enumerated representations and every referenced codelist/concept scheme. Save a machine-readable component inventory.
6. Independently request the relevant referenced codelists or use the complete `references=children` response; confirm each component's representation points to the expected agency, codelist ID and version.
7. Compare parsed components against the independent Vademecum crosswalk. Differences are recorded, not silently overwritten. The IMF DSD is authoritative for IMF extraction.
8. Archive raw XML, response metadata, SHA-256, parser version, inventory and QA report together. Only then may the DSD-parse gate become PASS.

**Download handling:** `saveAs=IMF_BOP_DSD_2_6_0` is included to request an attachment, as documented in the IMF guide. It is a transport hint, not evidence of successful retrieval; the HTTP status, Content-Type, final URL, exact byte count and SHA-256 must still be captured and validated.

**Second documented transport candidate (legacy SDMX-REST 1.x):** IMF SDMX Central also advertises the public SDMX-REST 1.x entry point `https://sdmxcentral.imf.org/ws/public/sdmxapi/rest`. The IMF's older technical guide demonstrates the `/datastructure/{agency}/{id}/{version}/` path and `format=sdmx-2.1`, `detail=full`, and `references=all` parameters. The following version-pinned request combines that documented path pattern with the documented attachment parameter:

```text
https://sdmxcentral.imf.org/ws/public/sdmxapi/rest/datastructure/IMF/BOP/2.6.0/?format=sdmx-2.1&detail=full&references=children&saveAs=IMF_BOP_DSD_2_6_0_legacy
```

This is an independently documented alternate endpoint family, but the exact BOP 2.6.0 request has **not** been successfully retrieved in this audit. Treat it as a candidate to test, not as a verified response URL. The legacy service is for structure metadata; it does not supply BOP country observations.

**Fallback:** use the IMF SDMX Central web UI at https://sdmxcentral.imf.org/webservice/structure.html, select Data Structure / IMF / BOP / version 2.6.0 / SDMX-ML v2.1 / Detail Full / References Children, and use Download. Record the exact generated query URL and downloaded file checksum. The UI is an alternate transport for the same metadata request, not a substitute for recording provenance.

### Important source boundary

The IMF SDMX Central guide describes the Structure Web Service for metadata (Dataflows, Codelists, Concepts and Data Structures). Do not mistake successful DSD retrieval for access to actual BOP observations. Observation extraction requires a separately verified IMF Data Portal data endpoint and dataset vintage. The IMF Data API page documents SDMX 2.1/3.0 access, while its Swagger explorer requires beta-portal sign-in. No observation API request is asserted as tested here.


## 8. 2026-11-14 verified SDMX 2.1 metadata addendum

The exact IMF SDMX Central public Structure REST requests were executed and raw responses archived. This supersedes the earlier status in Section 2B that the BOP DSD 2.6.0 XML had not yet been parsed.

- `IMF:BOP_GBPM6(2.0)` was retrieved and its Dataflow explicitly references `IMF:BOP(2.0)`.
- `IMF:BPM6_BOP_Q(1.5)` was retrieved and its Dataflow explicitly references `IMF:BOP(1.5)`.
- `IMF:BOP(2.6.0)` was independently retrieved and parsed successfully.
- DSD 2.6.0 has 18 ordered dimensions (including TIME_PERIOD), 15 attributes and primary measure OBS_VALUE.
- DSD 2.6.0 has 22 unique direct component codelist references. The descendants response contains 23 codelist objects because it also includes a related CL_AREA(1.17.0) in addition to the directly referenced CL_AREA(2.0.0).
- The direct REF_AREA/COUNTERPART_AREA codelist for DSD 2.6.0 is IMF:CL_AREA(2.0.0), 931 codes. India is represented by `IN` / `India`.
- The BOP_GBPM6 DSD 2.0 uses IMF:CL_AREA(1.14), 885 codes, and likewise contains `IN` / `India`.
- The BPM6_BOP_Q DSD 1.5 has 17 dimensions (no TYPE_ENTITY dimension), 14 attributes and OBS_VALUE. Do not assume its key schema is identical to DSD 2.0/2.6.0.
- The first inventory parser used broad descendant matching for Dimension nodes and generated blank IDs from nested attachment references. Raw XML was retained. A corrected parser now scopes to DataStructureComponents/DimensionList, AttributeList and MeasureList; counts above were independently checked against the raw XML.

Run/artifact evidence:
- Run `43608726175` SUCCESS; commit `eabcde2975fb19da9219700c8a08704c34559d2c`; artifact `14119193255`; ZIP SHA-256 `ca28bfd7d48b0e304ce2a41176c3ccf1a5ea241cf24eba880c9c5de246551399`.
- Run `43608839976` SUCCESS; commit `9e8cafda5a878bd7c212b9b3b385ea648e4c3b12`; artifact `14119642179`; ZIP SHA-256 `d99c92c23fe8d5f789e4ffd99fdd807f5331c4b261083eb63b0c9fb315ce856d`.
- DSD 2.6.0 descendant raw XML SHA-256 `0282f8ed931fc1c058c5f612f9b5c5c3ca60fa0590344d059d3ed2f547fd19ea`.
- BOP_GBPM6(2.0) descendant raw XML SHA-256 `d1698e30516d554740d269db5126487902fc2632131bf0ae3add26aefa7f63c7`.

Service boundary clarification: IMF SDMX Central's documented Structure REST API is a public metadata query service. Its separate public POST endpoints cover dataset validation/transformation/registration; they are not a raw country-observation GET API. IMF Data Portal's own SDMX 2.1/3.0 data APIs are separately documented, and its Swagger explorer requires beta-portal sign-in. Do not conflate these services.

The Portal dataset URN `IMF.STA:BOP(21.0.0)` is still not mapped to either IMF:BOP_GBPM6(2.0), IMF:BPM6_BOP_Q(1.5), or DSD 2.6.0. No observation endpoint, dimension key for the Portal dataset, or country observation is yet verified. India code verification in the public codelists is not proof of reporter observations.

Current status: DSD and codelist metadata retrieval PASS; Portal dataset-to-dataflow crosswalk UNKNOWN; public observation access BLOCKED pending a verifiable official Download/View Data route or an authorized beta-portal API schema. No aggregation permitted.


## 9. 2026-11-14 — Portal-owned Dataflow crosswalk and India public observation acquisition

This section supersedes the earlier UNKNOWN/blocked status for the Portal-to-registry crosswalk and the absence of an observation route. It does not supersede the distinct SDMX Central registry-vintage findings in Sections 8 and prior addenda.

### Exact Portal-owned mapping

The correct SDMX-REST 1.x route is:
`https://api.imf.org/external/sdmx/2.1/dataflow/IMF.STA/BOP/21.0.0?references=all`

The path does not include a `/structure/` prefix. The latter returned 404 (“No such artefact type: *”). The standard resource path returned HTTP 200, SDMX-ML 2.1, and an explicit Dataflow object:
- IMF.STA:BOP(21.0.0)
- DSD reference IMF.STA:DSD_BOP(24.0.0)

This is the Portal-owned dataflow and DSD mapping. It is not the same object as SDMX Central's separate IMF:BOP_GBPM6(2.0) or IMF:BOP(2.6.0).

### DSD 24.0.0 key schema

Direct DSD component parsing yields 6 dimensions, 45 attributes and OBS_VALUE:
- COUNTRY
- BOP_ACCOUNTING_ENTRY
- INDICATOR
- UNIT
- FREQUENCY
- TIME_PERIOD (observation time dimension)

The 5-part series key order is COUNTRY.BOP_ACCOUNTING_ENTRY.INDICATOR.UNIT.FREQUENCY. ConceptScheme/codelist references and exact labels were checked:
- IND = India
- A_NFA_T = Assets, Net acquisition of financial assets
- P_F = Portfolio investment, Total financial assets/liabilities
- USD = US dollar
- A = Annual; Q = Quarterly

The first attempted indicator P exists in CL_BOP_INDICATOR as “Portfolio investment”, but the India dataflow group inventory did not contain a matching India asset-side aggregate group for that key. The correct aggregate code for the series requested here is P_F. The query was corrected using the official codelist label and the dataflow response's actual group inventory. Preserve the first attempt as a diagnostic; do not rewrite it as a success.

### Actual observation route and narrow India sample

Official Data Portal SDMX 3.0 data route:
`https://api.imf.org/external/sdmx/3.0/data/dataflow/IMF.STA/BOP/21.0.0/{key}`

Exact series key:
`IND.A_NFA_T.P_F.USD.A`

Period filter: 2015-A1 through 2025-A1. The route returned HTTP 200 in SDMX-JSON 2.0.0 and SDMX-ML 3.0.0. It returned 11 observations for 2015–2025. This verifies public unauthenticated access for this exact series only; it does not complete the full India BOP panel.

Raw response hashes:
- Full JSON (49,654,152 bytes): `844f253263c00e77b7d0ee572a47dd01dc258c7b3eb0bc4b5f1eba9daac59a25`
- Full XML (122,045,648 bytes): `ca4676dbccb82383b7e549922169729c40084ec0d1c3eec4208f4ae4b1c25471`
- Compact data-only JSON (7,845 bytes): `85cca14cabf7a674ba37c00f88e3140f562480130bdde57d4902562fa6e0e23a`

The compact profile `dimensionAtObservation=TIME_PERIOD&attributes=all&detail=dataonly&limit=100` preserved all 11 observations and the series/observation attributes while reducing the response from 49,654,152 bytes to 7,845 bytes (99.9842% smaller). Use this profile for narrow future pulls unless an attribute or structural requirement proves otherwise.

Parser correction: in compact data-only SDMX-JSON, observations are nested under `dataSets[0].series[*].observations`, with time values in the observation dimension. The first compact parser looked only at `dataSets[0].observations` and reported zero. The raw body showed the 11 rows; the parser was corrected and the subsequent compact `attributes=all` run parsed 11/11 rows. Retain the initial parser diagnostic.

### Observation metadata

Series attributes: SCALE=6; METHODOLOGY=BPM6.
Observation attributes: PRECISION=6; DERIVATION_TYPE=O (Reported official data); ACCESS_SHARING_LEVEL=PUBLIC_OPEN (Public/Unrestricted); SECURITY_CLASSIFICATION=PUB (Public/Unrestricted). STATUS, ACCESS_SHARING_NOTES and SOURCE are null at observation level. Preserve nulls; do not infer values. SCALE is retained as a source attribute; no scaling transformation is applied.

### Stored outputs and evidence

- CSV: `data/research/imf_bop_india_portfolio_assets_usd_annual_2015_2025.csv`, 11 rows, SHA-256 `60e557c922763f145284c6243e4612d6c05c0ce756c6f2d8846e0ea2fc7c8697`, commit `47bc2c83bc60aec0bfebb4cb765f5884af84dbd7`.
- Provenance manifest: `data/research/imf_bop_india_portfolio_assets_usd_annual_2015_2025.manifest.json`, final commit `4c6d19533ce8c57564376f6fadf5e3055a67d42a`.
- Audit report: `docs/IMF_BOP_PORTAL_DATAFLOW_AND_INDIA_OBSERVATION_AUDIT_20261114.md`, commit `e01607a6d03c3a3ed511082de79ec9af17fa7c2b`.
- Dataflow probe Run `43615378167` SUCCESS; artifact `14122440301`; ZIP SHA-256 `2411f5837d7145ed6450a1423b17282f240cda6b7b6d61d842e4c18a6e88c125`.
- Full India sample Run `43615740505` SUCCESS; artifact `14121942694`; ZIP SHA-256 `e9d2b920a658870f0f4eb9abf60bc82815ed945b4ef0d9f1a96e3bc66c00d666`.
- Compact data-only Run `43616059985` SUCCESS; artifact `14122421554`; ZIP SHA-256 `cc951e2655dc4592ab82d848e0beebc43970132de1f4f3edc5c3ef8b56aaed23`.

Current gates: Portal crosswalk PASS; narrow India annual portfolio asset series PASS (11/11); full India panel, liabilities, quarterly series and revision reconciliation NOT DONE; EMDE reporter coverage NOT DONE; EM aggregate BLOCKED. The IMF BOP workstream is 5/7 accepted gates (71.4%); the narrow sample does not complete the full India panel gate. Project-wide progress remains NOT_CALCULABLE pending full workstream ledger reconciliation.


## 2026-11-14 — India annual/liability and quarterly assets/liabilities acquisition

The Portal-owned BOP dataflow crosswalk is proven from the Portal's own SDMX 2.1 structure response: `IMF.STA:BOP(21.0.0)` references `IMF.STA:DSD_BOP(24.0.0)`. Do not substitute SDMX Central registry candidate DSDs.

Exact series dimension order: COUNTRY, BOP_ACCOUNTING_ENTRY, INDICATOR, UNIT, FREQUENCY; TIME_PERIOD is the observation dimension. Verified codes: IND=India; A_NFA_T=Assets, Net acquisition of financial assets; L_NIL_T=Liabilities, Net incurrence of liabilities; P_F=Portfolio investment, Total financial assets/liabilities; USD=US dollar; A=Annual; Q=Quarterly.

Acquired using `dimensionAtObservation=TIME_PERIOD&attributes=all&detail=dataonly`:
- `IND.A_NFA_T.P_F.USD.A`: 11 annual rows, 2015–2025 (previously captured; do not reacquire absent a new source vintage).
- `IND.L_NIL_T.P_F.USD.A`: 11 annual rows, 2015–2025.
- `IND.A_NFA_T.P_F.USD.Q`: 44 quarterly rows, 2015-Q1–2025-Q4.
- `IND.L_NIL_T.P_F.USD.Q`: 44 quarterly rows, 2015-Q1–2025-Q4.

Combined 110-row CSV: `data/research/imf_bop_india_portfolio_assets_liabilities_annual_quarterly_2015_2025.csv`, SHA-256 `260ccc247ec564737bb3afe0a820c2435e37a58f588603241274537eca99f1b9`. Manifest: `data/research/imf_bop_india_portfolio_assets_liabilities_annual_quarterly_2015_2025.manifest.json`. Audit report: `docs/IMF_BOP_INDIA_PORTFOLIO_SERIES_RECONCILIATION_20261114.md`.

Annual/quarterly Decimal reconciliation over all 11 years: assets max absolute difference `0.0000009`; liabilities `0.000007`; both below declared raw-value tolerance `0.00001`. Independent committed-file integrity Run #43623953963 SUCCESS verified 110 rows, four period sets, source-response hash distribution, CSV SHA-256 and both reconciliations. Artifact ID `14125201831`.

Parser correction: Run #43623450125 failed because the validator treated the SDMX dataSet-level ordered attribute array as a mapping. Raw responses were retained. The corrected parser preserves the ordered array and Run #43623518481 passed all three new series. Do not discard the failed run; its failure was in the validator, not the HTTP responses.

Series metadata SCALE=6 and PRECISION=6 are retained without applying a multiplier. METHODOLOGY=BPM6; DERIVATION_TYPE=O; ACCESS_SHARING_LEVEL=PUBLIC_OPEN; SECURITY_CLASSIFICATION=PUB. Null STATUS, ACCESS_SHARING_NOTES and SOURCE remain null. Quarterly asset series carries IFS_FLAG=true; liabilities series IFS_FLAG is null. Do not combine/net assets and liabilities, convert USD, or aggregate EMDE until unit/scale semantics, reporter coverage and vintage/revision checks pass.

Current India acquisition subtask: annual and quarterly asset/liability base series PASS (110 observations). Full India panel remains IN_PROGRESS until revisions/vintage and completeness checks are complete. Full 154-economy EMDE reporter coverage NOT DONE; EM aggregate BLOCKED.
