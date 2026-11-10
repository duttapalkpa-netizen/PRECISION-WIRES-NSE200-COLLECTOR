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
