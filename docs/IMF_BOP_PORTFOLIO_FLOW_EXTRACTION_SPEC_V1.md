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

No conversion to USD, no annualisation, no aggregation, and no sign inversion may occur in the raw layer. Any derived field must be a separate, documented transformation with its own test.

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

The IMF SDMX Central Web Services Guide (last updated May 2025) specifies public access for the Structure Web Service, HTTP GET, entry point `https://sdmxcentral.imf.org/sdmx/v2/`, resource type `datastructure`, path parameters `agencyID`, `structureID`, and `version`, `references=children` to return referenced structures such as codelists, and `format=sdmx-2.1` plus `prettyPrint=true` for formatted XML.

**Exact request to execute and archive:**

```text
https://sdmxcentral.imf.org/sdmx/v2/structure/datastructure/IMF/BOP/2.6.0/?format=sdmx-2.1&references=children&detail=full&prettyPrint=true
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

**Fallback:** use the IMF SDMX Central web UI at https://sdmxcentral.imf.org/webservice/structure.html, select Data Structure / IMF / BOP / version 2.6.0 / SDMX-ML v2.1 / Detail Full / References Children, and use Download. Record the exact generated query URL and downloaded file checksum. The UI is an alternate transport for the same metadata request, not a substitute for recording provenance.

### Important source boundary

The IMF SDMX Central guide describes the Structure Web Service for metadata (Dataflows, Codelists, Concepts and Data Structures). Do not mistake successful DSD retrieval for access to actual BOP observations. Observation extraction requires a separately verified IMF Data Portal data endpoint and dataset vintage. The IMF Data API page documents SDMX 2.1/3.0 access, while its Swagger explorer requires beta-portal sign-in. No observation API request is asserted as tested here.
