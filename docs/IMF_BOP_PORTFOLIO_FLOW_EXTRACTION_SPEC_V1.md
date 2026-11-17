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

## 2C. IMF SDMX Central dataflow and registration discovery (2026-11-15)

A separate inspection of the live IMF SDMX Central public catalogue identified the following metadata leads. These are catalogue records, not downloaded BOP observations.

| Registry item | Observed catalogue evidence | Interpretation / gate |
|---|---|---|
| Dataflow | Agency IMF, ID `BOP_BPM6`, version 1.0 appears in the public constraints catalogue as `BOP_BPM6[1.0]` | Candidate IMF BOP dataflow identity; retrieve the dataflow structure and compare its DSD reference before constructing any observation key |
| Constraint | `BOP_BP6_CONSTRAINT`, attached to dataflow `BOP_BPM6[1.0]`, is listed as a Cube Region Constraint | Must retrieve and parse the constraint; do not assume every REF_AREA / frequency / counterpart / indicator combination is available |
| Registrations | Public registration catalogue lists `IMF:BOP_BPM6(1.0)` with multiple providers (including AT2, BE1, CH1, GB1, HU1, JP4, MT1, SK1 and US8) | These are provider registration records and point to national statistical authority files; they are not proof of an IMF-hosted global observation series |
| Registration freshness | Catalogue rows show provider-specific update timestamps, ranging from 2023 to 2026 | Preserve each provider and timestamp; do not treat the catalogue as a single synchronized global vintage |

Official catalogue pages:
- Dataflow/constraint registry: https://sdmxcentral.imf.org/data/constraints.html
- Provider registrations: https://sdmxcentral.imf.org/data/registrations.html
- Structure Web Service: https://sdmxcentral.imf.org/webservice/schema.html

### Extraction guardrails from this discovery

1. Retrieve the IMF agency dataflow `BOP_BPM6` version `1.0` and confirm its exact DSD reference; do not assume it references `IMF:BOP(2.6.0)` until the dataflow XML says so.
2. Retrieve `BOP_BP6_CONSTRAINT` and parse the cube-region restrictions before selecting any series.
3. Treat each provider registration as a distinct national reporting source with its own URL, provider ID, last-updated timestamp, publication vintage and checksum. Do not concatenate providers without deduplication and vintage policy.
4. Do not mistake the provider registration table for a central IMF BOP data API or for complete global country coverage.
5. The registrations page is discovery evidence only; no provider XML, national observations or IMF observations were downloaded in this step.

Audit status: DATAFLOW DISCOVERY = PASS; exact dataflow-to-DSD linkage = UNKNOWN; constraint payload parsed = UNKNOWN; observations = NOT DONE.

## 2D. Metadata acquisition workflow expansion (2026-11-15)

The short, manual-dispatch acquisition workflow was expanded to request three version-pinned metadata artefacts in one run:
1. BOP DSD `IMF:BOP:2.6.0` (existing request retained);
2. Dataflow `IMF:BOP_BPM6:1.0`;
3. Content constraint `IMF:BOP_BP6_CONSTRAINT:1.0`.

The SDMX REST resource for the constraint is `contentconstraint` (not the generic word `constraint`); the workflow URL was corrected accordingly after checking the IMF SDMX Central structure-service resource list. Each new metadata request stores its request URL, response headers, transfer metadata, raw XML, SHA-256 and a parseability/element-inventory report. The job timeout remains five minutes and no API key or paid service is used.

Workflow file: `.github/workflows/imf_bop_dsd_acquisition.yml`.
- Research overlay branch commit: `9feb0c4897ea22ca2d4154e8c440c94e03c7b389`.
- PR #34 registration branch commit: `6c0353eb809af8d4c288666961abce9c2b395179`.
- Both branches were updated from the same workflow content. The PR remains draft/unmerged; therefore no run has yet been triggered from the default branch.
- Workflow execution, HTTP response validation, raw XML checksums and component inventory remain NOT DONE until the workflow is registered on the default branch and manually dispatched.

This expansion does not change any production signal or use registration rows as observation data.

## 2E. Semantic metadata QA hardening (2026-11-15)

The acquisition workflow now checks more than XML well-formedness:
- Dataflow must contain exactly one `Dataflow` artefact with ID `BOP_BPM6`.
- That artefact must expose at least one `DataStructureRef`; the exact agency/ID/version values are written to the QA report and are not assumed.
- Constraint must contain exactly one `ContentConstraint` artefact with ID `BOP_BP6_CONSTRAINT` and at least one `CubeRegion`.
- Missing raw payloads remain UNKNOWN in per-item reports and cause the workflow to fail closed; malformed XML or missing required structure is FAIL.
- JSON QA report serialization was corrected to write valid newline-terminated JSON.

Latest workflow commits:
- Research overlay branch: `6d447a53199d24d333f02ec8c582eb00e8654c15`.
- PR #34 registration branch: `72a6968d4065214155045dd830cecbaa6f6b3ac6`.
- Workflow file SHA (before this documentation-only update): `40096faa971db93e9d154697ad24ffd1eb6f5d58`.

Static content comparison confirms both branches contain identical workflow text. Runtime XML results are still NOT DONE: no workflow was dispatched because PR #34 remains draft/unmerged and no default-branch registration has been authorized. A structural PASS from this parser is not yet a claim about IMF's live metadata payload.

## 2F. Exact DSD linkage and constraint-key inventory (2026-11-15)

Further tightened the metadata gate to prevent a false PASS:
- Dataflow `BOP_BPM6` must contain exactly one `DataStructureRef`, and it must exactly equal agency `IMF`, ID `BOP`, version `2.6.0`. Any missing, extra or different reference fails closed.
- Constraint QA now inventories each `CubeRegion` include/exclude flag and its `KeyValue` dimension IDs and values. This is an evidence inventory, not a hard-coded assumption about countries or frequencies.
- Both branch copies were re-fetched and compared byte-for-byte after the update.

Latest workflow commits:
- Research overlay: `543eca8a7ec402d241c03c05febf63cf0a1876f3`.
- PR #34 branch: `f29b16d250627d4171cddaf44f5c0b1398487a06`.
- Workflow blob SHA: `9f7563beab3e9e0f5d0b66cf91a7b49ff551d769`.

Runtime acquisition remains NOT DONE. Exact reference acceptance is encoded as a test expectation derived from the version-pinned DSD source path; it is not claimed as a verified live dataflow result until the official XML is acquired and parsed.

## 2G. SDMX-ML 2.1 Dataflow reference parser correction (2026-11-15)

A standards review found that the prior parser searched for a `DataStructureRef` element. SDMX-ML 2.1 Dataflow structures instead encode the DSD link as `Dataflow/Structure/Ref` (the Ref carries agencyID, id and version). The parser was corrected to read the nested `Structure/Ref` and compare the exact expected reference `IMF:BOP:2.6.0`.

A regression step now parses a minimal namespace-qualified SDMX-ML 2.1 StructureMessage fixture and asserts that the nested Ref is extracted exactly as `{"agencyID":"IMF","id":"BOP","version":"2.6.0"}`. This is a parser regression test, not a live IMF payload test.

Evidence:
- Official SDMX-ML schema catalogue lists the 2.1 structure schemas: https://xml.sdmx.org/ (reviewed 2026-11-15).
- SDMX 2.1 User Guide documents Dataflow/Structure/Ref with a DSD reference: https://sdmx.org/wp-content/uploads/SDMX_2-1_User_Guide_draft_0-1.pdf.
- Research branch workflow commit: `8afffeae3b8bfb4b826055a93f0842d8c46658dd`.
- PR #34 registration branch commit: `3c5fc6b494caac0a17ae74adefc3db19c6503170`.
- Both branch workflow contents re-fetched and confirmed identical; PR #34 remains draft/unmerged.
- Workflow blob SHA: `c35b71a2b464cab87a41dac92dbecec1264e5c4f`.

The parser correction and fixture are committed. The GitHub Actions run, live IMF XML, exact live DSD linkage and cube-region values remain NOT DONE until the workflow is registered on the default branch and dispatched.


## 2H. SDMX 2.1 ContentConstraint / CubeRegion QA hardening (2026-11-15)

- Official SDMX-ML 2.1 schema source: `sdmx-twg/sdmx-ml`, ref `v2.1`, files `schemas/SDMXStructureConstraint.xsd` and `schemas/SDMXCommon.xsd`.
- Schema findings: `ContentConstraintType` permits repeated choice members including `CubeRegion`; SDMX 2.1 `CubeRegion` is typed in the common namespace and contains `KeyValue` and `Attribute`; each `KeyValue` has required `id` and can contain either repeated `Value` elements or a `TimeRange`. Include/exclude semantics are carried by the relevant include attributes.
- Workflow hardening commit: `ffd9a1acb98639ff29e46ec85f4baee0a3eb84b0`; workflow blob `e7a6877721cf2282c781bb0e9f12a74d476f3971`.
- Added a namespace-qualified SDMX 2.1 regression fixture covering included and excluded dimensions, a TIME_PERIOD TimeRange with inclusive/exclusive boundaries, and an Attribute value.
- Expanded runtime QA inventory to retain per-region include status, each KeyValue id/include/Value list/TimeRange boundaries, and Attribute id/include/Value list. This avoids treating a mere CubeRegion count as complete dimensional coverage evidence.
- Verification: branch file re-fetched and confirmed to contain the fixture and expanded inventory; job timeout remains 5 minutes. GitHub Actions runtime has NOT been dispatched; fixture execution and live IMF response validation remain NOT DONE. Do not mark the IMF metadata runtime gate PASS from this static commit alone.


## 2I. Local execution of CubeRegion regression fixture (2026-11-15)

- Re-fetched the exact committed workflow source and extracted the committed SDMX-ML 2.1 ContentConstraint fixture step without modifying it.
- Executed the fixture's Python assertions locally against the namespace-qualified XML sample.
- Result: PASS for exact ContentConstraint ID lookup, one CubeRegion, FREQ included value, REF_AREA excluded value, TIME_PERIOD StartPeriod/EndPeriod with inclusive/exclusive flags, and UNIT_MEASURE Attribute value.
- This validates the fixture's parser assertions locally only. It is not a GitHub Actions run, XSD validation of the live IMF response, or evidence that IMF's live constraint has these exact values.
- No live acquisition or production change was performed. PR #34 remains unmerged; workflow dispatch is still blocked pending authorized registration on the default branch.


## 2J. Independent local execution confirmation of both SDMX 2.1 parser fixtures (2026-11-15)

- Re-fetched workflow blob `e7a6877721cf2282c781bb0e9f12a74d476f3971` and extracted the exact Python source blocks from the committed Dataflow Structure/Ref and ContentConstraint CubeRegion regression steps.
- Executed both extracted blocks in the local Python runtime without editing the fixture code.
- Results: Dataflow Structure/Ref fixture PASS; ContentConstraint CubeRegion fixture PASS.
- This closes the local fixture-execution check for both committed parser examples. It still does not execute the complete GitHub Actions workflow, perform XSD validation, retrieve IMF live XML, or establish live IMF country/frequency coverage.
- Runtime acquisition remains NOT DONE; no PR merge or production integration was performed.


## 2K. Constraint-to-dataflow attachment and dimension-key acceptance hardening (2026-11-15)

- Standards source reviewed: SDMX-ML 2.1 `SDMXStructureConstraint.xsd` and `SDMXCommonReferences.xsd` at `sdmx-twg/sdmx-ml` ref `v2.1`. The ContentConstraint attachment can reference a Dataflow; its Dataflow reference contains a `Ref` with agency, ID and version fields. CubeRegion KeyValue elements carry required dimension IDs and either Value members or TimeRange.
- Tightened the live constraint QA: it now requires exactly one attachment reference matching `IMF:BOP_BPM6:1.0`, at least one dimension KeyValue, unique dimension IDs across the inspected regions, and no dimension key lacking an ID or both Value/TimeRange content. The complete region/dimension/attribute inventory remains preserved.
- Expanded the namespace-qualified regression fixture to include the ConstraintAttachment/Dataflow reference. The exact updated fixture was executed locally and passed all assertions, including exact attachment reference and existing include/exclude, TimeRange and Attribute checks.
- Research branch workflow commit: `1e8e3cb96e70f7934da68c8f91cd775c882595e3`; workflow blob: `4349a273c43ccfdab4dae0d8dc9fa734d0d0b2a9`.
- PR #34 branch synchronization commit: `ead54698aa2d553ed2a62ff3a06ab924ea6a8f25`. Both branch copies re-fetched and confirmed byte-identical.
- This is static QA hardening plus local fixture execution only. Live IMF XML acquisition, GitHub Actions execution, live attachment/coverage verification and milestone acceptance remain NOT DONE. PR #34 remains unmerged; no production changes.


## 2L. Correct dimension-key uniqueness scope across multiple CubeRegions (2026-11-15)

- Review found a false-failure risk in the previous QA: it compared dimension IDs globally across all CubeRegions. SDMX permits the same dimension IDs (for example FREQ and REF_AREA) to recur in separate regions; uniqueness is required within each region, not across the whole constraint.
- Corrected the validator to audit each CubeRegion independently, reporting per-region key counts and uniqueness, and rejecting missing IDs or keys with neither Value nor TimeRange.
- Expanded the namespace-qualified regression fixture to contain two CubeRegions reusing FREQ and REF_AREA IDs with different values and region include flags.
- Executed the updated fixture and the per-region uniqueness assertions locally: PASS. The fixture also retains checks for the exact IMF:BOP_BPM6:1.0 attachment, first-region include/exclude, TIME_PERIOD boundaries and Attribute values.
- Research workflow commit: `0a6af27fe0f230d3d24826605af8020bbb44eb9a`; PR #34 workflow branch sync commit: `86c132676f467cda788f9e7acbbfb9cd6db6f790`; workflow blob: `9d7ba026b42a50108e4f9fec06e39f687ad26a5e`.
- Both workflow branch copies re-fetched and confirmed byte-identical. Live IMF XML, GitHub Actions run, and live constraint coverage remain NOT DONE. PR #34 remains unmerged.


## 2M. Negative-case verification for per-region dimension key gate (2026-11-15)

- Re-fetched the committed workflow blob `9d7ba026b42a50108e4f9fec06e39f687ad26a5e` and independently executed the two-CubeRegion fixture structure in local Python. Both regions correctly retain repeated dimension IDs across regions while each region's own keys remain unique.
- Executed focused negative-case assertions for the same acceptance rule: a valid region with unique IDs is accepted; duplicate IDs within one region are rejected; a KeyValue missing its ID is rejected. All assertions passed.
- This is local logic/fixture validation, not a GitHub Actions run, XSD validation, or live IMF payload check. Runtime acquisition remains NOT DONE; no PR merge or production integration.


## 8. 2026-11-17 official BOP aggregate candidate discovered — not yet extracted
- IMF official dataset: **BOP/IIP World and Country Group Aggregates (BOP_AGG; historically BOPSY)**: https://data.imf.org/en/datasets/IMF.STA%3ABOP_AGG
- Official November 2025 explanatory notes: https://data.imf.org/-/media/Explanatory-Notes-November-2025-BOPSY.pdf
- The IMF describes BOP_AGG as an annual November publication using BPM6. Its published World and country-group aggregates combine reported country data with estimates for nonreporting economies (including WEO-derived estimates). This applies to financial-account transactions as well as other components.
- The official EMDE grouping is IMF's own classification and must not be labelled MSCI EM. The published annual aggregate is low-frequency strategic context, not a daily trading trigger.
- BOP_AGG includes both transactions and IIP positions. Only financial-account portfolio-investment transactions may be considered for the flow indicator; IIP positions remain excluded.
- Source discovery and high-level methodology assessment: PASS.
- Exact portfolio-investment table/series mapping, raw workbook/API payload, retrieval timestamp, byte count, SHA-256, units/sign/series-key QA and release-vintage reconciliation: UNKNOWN / NOT_DONE.
- No BOP_AGG value is admitted into `em_portfolio_flow_usd_bn` until those extraction and validation gates pass.
- Detailed checkpoint: `docs/GLOBAL_CAPITAL_ROTATION_IMF_BOP_AGGREGATE_SOURCE_CHECKPOINT_20261117.md`.


## 2N. IMF SDMX Central service-scope correction — 2026-11-17

A direct review of the IMF SDMX Central Web Services Guide (last updated May 2025) requires a strict service-scope distinction:
- Official structure REST entry point: `https://sdmxcentral.imf.org/sdmx/v2/` (public GET for metadata structures such as dataflows, codelists, concepts and data structures).
- The guide separately identifies `https://sdmxcentral.imf.org/ws/public/data` as the entry point for FMR data-processing services (validation, conversion and registration). It explicitly says there is no official REST API for those data-processing services under the structure service.
- Therefore neither the structure endpoint nor the FMR processing endpoint may be represented as an established public BOP observation-data endpoint. The earlier legacy route discussion concerns structure/catalogue metadata only; it does not prove access to country observations or BOP_AGG values.
- The modern IMF Data Portal API link on the BOP dataset page redirects to the API developer portal sign-in. Anonymous observation retrieval remains NOT_DEMONSTRATED.
- The SDMX Central catalogue lists dataflows from multiple agencies (including national and international providers); appearance of an IMF:BOP DSD is not proof of an IMF BOP observation dataflow hosted there.
- The exact BOP DSD 2.6.0 metadata URL was also attempted through the available browser reader but returned an inaccessible response; no raw XML bytes, HTTP headers, byte count or SHA-256 were obtained.

Corrected status: BOP DSD metadata route documented; raw DSD retrieval NOT_DONE; public IMF BOP/BOP_AGG observation API NOT_VERIFIED; no IMF observations extracted. This correction supersedes any interpretation that the legacy SDMX Central service route is a public BOP observation endpoint.


## 2O. IMF public BOP pilot archive and current BOP dataset route assessment — 2026-11-17

- The current IMF Data Portal country-level Balance of Payments (BOP) dataset is a distinct dataset from annual BOP_AGG. Its official page exposes API / VIEW DATA / DOWNLOAD controls and defines BOP as resident/nonresident transactions. Search metadata describes Annual and Quarterly frequency. The API control redirects to the developer portal sign-in; the page's DOWNLOAD control does not expose a direct file URL in the available page extraction. No current raw observations were retrieved.
- IMF SDMX Central's public dataflow catalogue visibly includes provider-specific BPM6 BOP dataflows (e.g., ESTAT) and its registrations page lists country statistical-provider URLs for BOP6/BOP_GBPM6 dataflows. These are provider-hosted national datasets, not a single IMF global BOP observation panel. They must not be aggregated without a separately verified country universe, provider URL, DSD/version, period coverage, units/sign, revisions and missing-country method.
- A historic IMF SDMX BOP pilot site offers regional compact SDMX files for 75 series per reporting country, but the page explicitly states last update 9-Jan-2013. This route is rejected for current overlay ingestion due to staleness; it may only be used as a historical format/reference example, not current flow evidence.
- BOP_AGG remains a separate annual World/Country Group aggregate dataset. Neither the current BOP page nor the old pilot files establish a current BOP_AGG download payload.
- Result: current BOP dataset discovery PASS; direct current observations NOT_ACQUIRED; country-provider registrations are discovery leads only; 2013 pilot files REJECTED_FOR_CURRENT_SIGNAL; BOP_AGG raw payload NOT_DONE. No observations or values admitted.


## 2P. Country-level official fallback: Brazil BCB SGS portfolio flows — 2026-11-17

A working official BCB open-data JSON endpoint was identified and its live response inspected for two distinct monthly BPM6 portfolio-investment components:
- SGS 22906: net acquisition of financial assets; USD million; monthly; starts 1995-01; latest visible observation 2026-09-01 = +3,269.3 USD million.
- SGS 22924: net incurrence of liabilities; USD million; monthly; starts 1995-01; latest visible observation 2026-09-01 = -1,698.5 USD million.
- Official endpoint URLs and definitions are recorded in the source register.
- These are Brazil country-level BCB observations, not IMF BOP_AGG and not an EM regional aggregate. Do not derive combined net inflow until the exact BCB sign convention is verified. Do not treat as daily trading trigger.
- API live-response retrieval PASS; immutable raw-file archive, byte count, SHA-256, full row QA, revision/vintage and sign reconciliation NOT_DONE. Therefore no observation is yet admitted to the overlay input panel.


## BCB 22905 cross-series comparability guard — 2026-11-17

Official BCB catalogue review adds a critical classification boundary:
- SGS 22905 is a separate monthly “Portfolio investment - net” dataset under BCB/Dstat, associated with the BOP6/BPM6 hierarchy. Its official catalogue describes assets and liabilities, USD millions, monthly observations, and publication timeliness up to four weeks after the reference period.
- SGS 22906 and 22924 are separately catalogued BCB/Depec series (Department of Economics), respectively net acquisition of financial assets and net incurrence of liabilities. Their individual dataset pages provide monthly coverage from 1995-01 and USD-million units.
- Similar labels do not prove identical calculation, sign convention, compilation vintage, or reconciliation. 22905 is a cross-series control candidate only; it must not be used as a plug, replacement, or arithmetic identity for 22906/22924 without BCB methodology reconciliation and overlapping-period numeric testing.
- The BCB portal's stated four-week timeliness for 22905 confirms this is a delayed monthly macro series, not a daily capital-flow signal. Use the actual publication timestamp/vintage if acquired; do not assign the observation date as its publication timestamp.
- Evidence: official BCB dataset pages for 22905, 22906, 22924 and the official topic taxonomy. The direct 22905 JSON endpoint did not render in this browser inspection, so its live observations remain NOT_ACQUIRED in this verification step.


## Correction: BCB SGS 22905 catalogue ownership and resource verification — 2026-11-17

Correction to the immediately preceding 22905 comparability note: the official Open Data Portal page identifies SGS 22905 as organization BCB/Depec (Department of Economics), not BCB/Dstat. The official SGS 22906 page also identifies BCB/Depec; the 22924 catalogue entry likewise identifies BCB/Depec. Therefore the earlier statement that 22905 was a Dstat series distinct by organization from 22906/22924 is withdrawn. The prior claim that 22905 was in a separate BOP6/Dstat hierarchy is not supported by the official catalogue page and must not be used.

Verified catalogue facts for 22905: title “Portfolio investment - monthly - net”; source/author/maintainer Central Bank of Brazil / Department of Economics; monthly; unit million US dollars; temporal coverage from 1995-01-01. The portal's JSON resource link resolves to `https://api.bcb.gov.br/dados/serie/bcdata.sgs.22905/dados?formato=json` and the browser identifies `application/json`, but it did not expose the response rows in readable text. Therefore live observation values, latest period, raw archive, byte count and SHA-256 remain NOT_ACQUIRED / NOT_DONE in this verification.

22905 remains a third BCB/Depec series that may be compared against 22906 and 22924, but no algebraic identity, sign convention, or aggregation relation is inferred from titles. Reconcile BCB methodology and overlapping raw observations before calculating or replacing any series. Prior reported Sep-2026 22906/22924 figures remain historical claims from earlier response inspection and are not revalidated by this catalogue correction.

Official evidence: BCB 22905 dataset page (organization, definition, resources, coverage, frequency, unit); BCB 22906 dataset page (same organization, coverage, frequency, unit); BCB 22924 dataset catalogue (same organization and unit/frequency/coverage).


## Critical dual-catalogue conflict for SGS 22905 — 2026-11-17

A second official BCB portal instance was inspected and reveals an unresolved catalogue conflict for the same SGS code 22905:
- `opendata.bcb.gov.br` page title “Portfolio investment - monthly - net” classifies it as BCB/Depec, with metadata updated 2026-03-26; it links the JSON resource for SGS 22905.
- `dadosabertos.bcb.gov.br` page title “Investimentos em carteira - líquido” classifies it as BCB/Dstat, explicitly places it under Balanço de Pagamentos - BPM6 / Conta financeira / Investimentos em carteira, reports timeliness up to four weeks, and metadata updated 2026-09-08; it also links a JSON resource for SGS 22905.
- Both pages identify monthly frequency, USD million, and start date 1995-01. Both resource links refer to the same SGS code family. This is not safely resolvable from catalogue text alone. Do not assert that 22905 is definitively Depec or Dstat, do not assume the pages describe distinct numerical series, and do not merge or select either taxonomy as authoritative until the exact resource URLs, live payloads, series metadata and publication vintages are compared.
- The latest metadata date on the Dstat page is later, but recency alone does not prove ownership or supersession. Treat classification as CONFLICT / UNKNOWN.
- Next validation: resolve each portal's JSON resource link and capture final URL, HTTP status, content type, response bytes, retrieval timestamp and SHA-256; compare payload values/date keys and SGS series metadata. If payloads are byte/value-identical, treat as duplicate catalogue records and preserve both provenance records. If payloads differ, quarantine both until BCB methodology clarifies the canonical series.
- Evidence: official BCB portal pages `opendata.bcb.gov.br` SGS 22905 and `dadosabertos.bcb.gov.br` SGS 22905. Both catalogues are official but disagree on organization and classification.
- Current decision: SGS 22905 excluded from any calculation; SGS 22906 and 22924 remain separate Depec series pending their own raw archive and reconciliation. No net-flow identity inferred.


## BCB SGS 22905 dual-catalogue endpoint verification — 2026-11-17

Both official BCB portal JSON resource links were resolved and point to the identical endpoint: `https://api.bcb.gov.br/dados/serie/bcdata.sgs.22905/dados?formato=json`. The response from the dadosabertos resource was readable as JSON and showed monthly records from 1995-01 through 2026-09 in the browser excerpt. The opendata resource resolved to the same exact URL. Thus the earlier concern about separate numerical payloads from two distinct resource URLs is not supported; both catalogue records reference one SGS JSON API route.

The catalogue metadata conflict remains: one page identifies BCB/Depec and English title “Portfolio investment - monthly - net”; the other identifies BCB/Dstat and places the dataset under BPM6 / financial account / portfolio investment. A shared endpoint does not decide which metadata hierarchy/owner record is authoritative, nor does it prove a methodology/version history. Preserve both metadata provenance records and keep classification CONFLICT / UNKNOWN until official methodology/version evidence resolves it.

The CSV links also resolve to the same API route with `formato=csv`, but the browser reader rejected the `text/csv` content type; no CSV bytes were acquired. Browser-inspected JSON is not a raw archive: byte count, retrieval timestamp, complete payload capture, SHA-256, full-history row QA and vintage/revision QA remain NOT_DONE. No observations admitted to the global EM flow panel. No relationship with SGS 22906/22924 inferred.



## BCB SGS live-value cross-check — 2026-11-17

Official API JSON browser inspection returned 2026-09-01 values: SGS 22905 = +4,967.8 million USD and SGS 22906 = +3,269.3 million USD. Their arithmetic difference is +1,698.5 million USD. A prior inspection had reported SGS 22924 = -1,698.5 million USD for the same month, but the 22924 endpoint could not be freshly re-fetched in this turn. This exact magnitude match is a one-period reconciliation lead only; it does not establish the formula, signs, accounting treatment or full-history identity.

Acceptance remains blocked until SGS 22924 is freshly captured, all three series are compared over their full common monthly period, official methodology confirms the financial-account sign conventions and any revisions, and raw bytes + retrieval metadata + SHA-256 are archived. No values are admitted to the global EM flow panel or relative-attraction calculation. Keep 22905 catalogue owner/classification as CONFLICT / UNKNOWN.



## BCB liabilities component cross-check discovery — 2026-11-17

Official BCB Open Data Portal catalogues distinguish SGS 22924 (net incurrence of portfolio-investment liabilities, monthly net), SGS 22925 (same liabilities, monthly inflows), and SGS 22926 (same liabilities, monthly outflows). The catalogue describes these as monthly USD-million SGS series beginning 1995-01 and identifies BCB/Depec. This discovery enables a targeted reconciliation test but does not prove a formula or sign orientation.

A direct browser open of the 22924 JSON API URL was inaccessible in this verification; no fresh observation or raw bytes acquired. The previously observed Sep-2026 value is not revalidated here. BCB's September-2026 External Sector Statistics publication reports domestic-market portfolio investment liabilities net outflows USD 2.1bn, including USD 1.7bn equity/fund and USD 0.4bn debt securities, plus USD 5.1bn 12-month net inflows. This publication is contextual cross-check evidence only; do not equate it to SGS 22924 without scope, instrument and period reconciliation.

Required acceptance: retrieve raw 22924/22925/22926 payloads; archive retrieval timestamp, status, content-type, bytes and SHA-256; compare common monthly date keys and missing markers; test candidate net/inflow/outflow identities across every overlapping month; reconcile units, sign convention, gross/net scope, instrument coverage and revisions against BCB methodology; only then consider country-level Brazil pilot admission. No global EM aggregate is inferred.
