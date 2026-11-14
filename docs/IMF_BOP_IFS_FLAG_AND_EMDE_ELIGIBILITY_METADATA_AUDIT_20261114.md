# IMF BOP IFS_FLAG semantics and EMDE reporter eligibility metadata audit

Audit date: 2026-11-14
Branch: `research/imf-bop-access-audit-v1`
Dataset: `IMF.STA:BOP(21.0.0)`
DSD reference: `IMF.STA:DSD_BOP(24.0.0)`
Scope: resolve the meaning of the observed `IFS_FLAG` attribute and determine what official metadata can and cannot establish about the 39 WEO-EMDE reporters with no observations in either tested 2000-Q1–2014-Q4 or 2015-Q1–2025-Q4 windows.

## 1. Official source evidence

1. IMF Data Portal, “Accessing International Financial Statistics (IFS)” (published 2025-03-24): https://data.imf.org/en/news/accessing
   - The IMF states that IFS data is no longer a single dataset and that former IFS indicators are now distributed among topic datasets.
   - It explicitly maps “IFS, Balance of Payments Indicators” to “Balance of Payments (BOP)”.
   - It states that the Data Explorer can display an “IFS Flag” column and that the flag can be included as metadata in downloads.
   - For API filtering, it says to constrain on component `IMF_FLAG`, using `c[IFS_Flag]=True`.
2. IMF Data Portal, BOP dataset page: https://data.imf.org/Datasets/BOP
   - Identifies BOP as an IMF Statistics Department dataset; annual and quarterly frequencies are supported.
   - The dataset page exposes metadata and API resources.
3. IMF Data API information page: https://data.imf.org/en/Resource-Pages/IMF-API
   - States that IMF data are available through SDMX 2.1 and SDMX 3.0 APIs.
4. IMF SDMX Central overview: https://sdmxcentral.imf.org/overview.html
   - Explains that DSD components define dimensions/attributes and their allowed values, and that dataflows can impose additional constraints on allowable content.

## 2. IFS_FLAG semantic determination

**Resolved meaning:** the IMF “IFS Flag” identifies whether a time series belongs to the former International Financial Statistics (IFS) collection, now reorganized into subject-specific datasets. The IMF's API guide identifies the corresponding API component as `IMF_FLAG` and documents filtering for the former-IFS subset with `c[IFS_Flag]=True`.

This is a provenance/catalogue-membership flag, not an observation-quality grade, BPM methodology indicator, revision flag, or completeness signal. A true value must not be interpreted as “higher quality” or “officially validated” beyond the documented former-IFS membership meaning.

### Application to the previously inspected BOP raw responses

- Observed asset series for ETH, HTI and DZA had `IFS_FLAG=true`.
- Observed liability series for ETH, HTI and ZWE had `IFS_FLAG=null`.
- Therefore, the asset observations inspected are explicitly tagged as former-IFS series. The liability nulls do **not** prove that those series were never in IFS: the IMF documentation explains the true filter but does not define the meaning of a null attribute in this particular DSD version. Preserve null as UNKNOWN.
- No raw response was reacquired and no historical coverage result was changed.

## 3. 39-country eligibility: what is established

The exact 39-country set remains the one in the accepted 2000–2025 cross-period matrix. The existing evidence establishes that the 39 codes have no observations returned for either `A_NFA_T` or `L_NIL_T` under the exact tested slice: portfolio financial flows (`P_F`), USD, quarterly, over the two tested windows.

The existing 154/154 WEO-to-Portal `CL_BOP_COUNTRY(1.0.0)` crosswalk proves that these are valid country-dimension codes in the BOP dataset-specific codelist. It does **not** prove that every country reports every indicator, accounting entry, unit and frequency combination.

The public BOP dataset page confirms that annual and quarterly data exist at dataset level, but does not provide a reporter-by-indicator-by-unit-by-frequency eligibility matrix. The public IMF SDMX Central explanation also distinguishes DSD allowed values from dataflow constraints. A country code's presence in a codelist alone is therefore insufficient to establish that the exact `P_F` + USD + quarterly + asset/liability combination is applicable to that reporter.

**Eligibility result for all 39 countries: UNKNOWN / NOT ESTABLISHED.** No country is promoted to eligible or ineligible on the basis of absence, codelist membership, or the general dataset frequency statement.

## 4. Why the missing-data cause remains UNKNOWN

The public documentation reviewed here does not expose a reporter-specific constraint proving that any of the 39 countries is excluded from the exact requested series. Nor does it establish that each country is required to report the series. A no-observation result could reflect a reporting gap, a non-applicable instrument/account, a currency/frequency availability boundary, a dataflow constraint, or another source-side cause; none is assigned without direct evidence.

No zeros, synthetic rows, permanent non-reporting labels, or inferred eligibility have been created.

## 5. Gate and next action

- IFS_FLAG semantic identification: **PASS (100% of this defined subtask)**.
- Null-value semantics for IFS_FLAG in DSD_BOP(24.0.0): **UNKNOWN**.
- 39-country exact series eligibility: **UNKNOWN (0% resolved)**.
- 2000–2025 historical acquisition and reconciliation: prior PASS as research tasks; not repeated.
- 154-economy reporter coverage acceptance: **NOT PASS**.
- EMDE aggregation: **BLOCKED**.

Next highest-value action: inspect the exact archived DSD_BOP(24.0.0) structure response and its referenced codelists/constraints for `BOP_ACCOUNTING_ENTRY`, `INDICATOR`, `UNIT`, `FREQUENCY`, and any dataflow constraint artefacts; then compare the 39 codes against the actual permitted combinations. If the archived structure contains no reporter-specific constraint, record that as “no eligibility constraint found in the inspected artefacts”, not proof that a country is eligible. Only after this inspection decide whether an official BPM6 reporting-availability document or a separately documented series is needed.

## 6. Invariants

₹0 spend; official public sources only; no paid APIs, credentials, authentication bypass, external contact, synthetic data/timestamps, PR merge or production integration. Production Selector, `RANKING_SCORE`, `+1 PRESSURE_FADE`, CORE-672, engines A–E and Hard Gate unchanged.


## 7. Archived metadata artifact scope check (important limitation)

The previously archived metadata artifacts were opened and inspected before treating them as evidence for the Portal DSD:

- Artifact `14111193621` contains the IMF global SDMx BOP DSD `IMF:BOP(2.6.0)` (raw XML SHA-256 `19d3dc2d341eaef68b95b6c011c4c5db6a3f25336f5967806a728c7f5dd394a5`) and its referenced global codelists. Its component inventory uses the global DSD vocabulary (for example `FLOW_STOCK_ENTRY`, `ACCOUNTING_ENTRY`, `INT_ACC_ITEM`, `UNIT_MEASURE`, `CURRENCY_DENOM`, `TIME_PERIOD`) and does not contain `IFS_FLAG`, `IMF_FLAG`, `BOP_ACCOUNTING_ENTRY`, or `INDICATOR`. It is not the Portal's exact `IMF.STA:DSD_BOP(24.0.0)`.
- Artifact `14112042284` contains a metadata audit of the public dataset page and IMF SDMX Central global dataflows/DSD. Its dataflow request is `https://sdmxcentral.imf.org/sdmx/v2/structure/dataflow/IMF/all/latest/`; it is not a capture of the exact Portal DSD 24.0.0 structure/constraints. The metadata summary explicitly labels the structure inventory as counts-only/manual reconciliation required.
- Therefore neither artifact can be substituted for the exact Portal DSD 24.0.0 when deciding reporter eligibility. No reporter eligibility decision is made from these mismatched global artefacts. This reinforces the 39-country eligibility result as UNKNOWN and the need to retrieve the exact Portal DSD structure/constraint artefacts or another official exact-scope metadata source.
- This artifact-scope check reuses prior downloaded files; no data API query was repeated.
