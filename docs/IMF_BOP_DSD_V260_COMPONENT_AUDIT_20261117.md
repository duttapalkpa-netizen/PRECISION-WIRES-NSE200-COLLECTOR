# IMF BOP DSD V2.6.0 Component Audit — 2026-11-17

## Scope and decision
This is a bounded metadata-component audit after the IMF observation-access gate. It does **not** claim that IMF country observations were downloaded, that the IMF BOP dataflow uses a particular code subset, or that a country portfolio-flow panel is available.

## Independently verified official structure identity
- SDMx Global Registry lists agency `IMF`, structure `BOP`, title “Balance of Payments and International Investment Position”, latest version `2.6.0`.
- SDMx BOP package page identifies BOP V2.6.0 as published December 2025, maintained by IMF, and states that registry structure downloads do not require authentication.
- IMF SDMX Central structure catalogue independently lists `IMF / BOP / 2.6.0`.
- Official registry and IMF Central pages are structure metadata sources; neither by itself proves that an IMF observation dataflow/query is public or identifies the actual observation provider/dataflow.

## Component cross-check
The ECB BPM6 2026 booklet's BOP DSD table independently lists the 17 dimensions and their code-list mnemonics. The Eurostat BOP Vademecum (November 2025–July 2026) provides an additional standards cross-check and example values. These are standards-level cross-checks, **not a substitute for parsing the IMF V2.6.0 raw structure artefact**.

| Dimension | Code-list mnemonic shown in standards cross-check | Portfolio-flow use / control |
|---|---|---|
| FREQ | CL_FREQ | Preserve exact frequency; do not assume daily |
| ADJUSTMENT | CL_ADJUSTMENT | Keep adjusted/unadjusted series separate |
| REF_AREA | CL_AREA | Reporting economy |
| COUNTERPART_AREA | CL_AREA | Preserve counterpart; do not conflate bilateral and total |
| REF_SECTOR | CL_SECTOR | Preserve reporting-sector scope |
| COUNTERPART_SECTOR | CL_SECTOR | Preserve counterpart-sector scope |
| FLOW_STOCK_ENTRY | CL_FSENTRY | Select transactions only after IMF codelist verification |
| ACCOUNTING_ENTRY | CL_ACCOUNT_ENTRY | Keep asset acquisition and liability incurrence distinct |
| INT_ACC_ITEM | CL_ACCOUNTS_ITEM | Confirm financial-account portfolio item |
| FUNCTIONAL_CAT | CL_FUNCTIONAL_CAT | Confirm portfolio investment code |
| INSTR_ASSET | CL_INSTR_ASSET | Separate equity/fund shares and debt where supported |
| MATURITY | CL_MATURITY | Preserve debt maturity split |
| UNIT_MEASURE | CL_UNIT | Preserve unit |
| CURRENCY_DENOM | CL_CURRENCY | Preserve currency denomination separately from unit |
| VALUATION | CL_VALUATION | Preserve valuation qualifier |
| COMP_METHOD | CL_COMP_METHOD | Preserve compilation method |
| TYPE_ENTITY | CL_TYPE_ENTITY | Preserve entity coverage |

## What this audit did and did not establish
- DSD identity/version: VERIFIED_OFFICIAL by registry catalogue and IMF Central catalogue.
- 17-dimension component names and codelist mnemonics: independently cross-checked against official statistical standards publications.
- Exact IMF V2.6.0 XML bytes, content length and SHA-256 archived in this repository: NOT_DONE.
- Exact IMF codelist item codes/labels and portfolio investment transaction key: NOT_DONE.
- IMF BOP observation dataflow/provider and public data query: UNKNOWN / NOT_VERIFIED.
- Country-period observation payload, response metadata and raw hash: NOT_DONE.
- Country-level portfolio-flow panel and actual-vs-estimate decomposition: UNKNOWN / NOT_DONE.

## Evidence sources inspected 2026-11-17
1. SDMx Global Registry, Data Structure Definitions catalogue: https://registry.sdmx.org/data/datastructure.html — lists IMF:BOP latest version 2.6.0.
2. SDMx BOP package page: https://sdmx.org/sdmx-data-structure-definitions-for-balance-of-payments-sdmx-bop/ — identifies BOP V2.6.0 (December 2025), IMF maintenance, and unauthenticated registry downloads.
3. IMF SDMX Central, data structure catalogue: https://sdmxcentral.imf.org/data/datastructure.html — lists IMF:BOP 2.6.0.
4. ECB BPM6 booklet (April 2026): https://www.ecb.europa.eu/press/bpm6/pdf/ecb.bpm6202604.en.pdf — BOP DSD dimensions and codelist mnemonics.
5. Eurostat BOP Vademecum (November 2025–July 2026): https://ec.europa.eu/eurostat/documents/39118/18471074/vademecum-balance-of-payments.pdf/fe2f00ea-6036-1f15-c1c1-1d899503636c?t=1759397645542 — component definitions and illustrative code values. Do not copy Eurostat-specific dataflow or coverage into IMF.

## Next exact acceptance step
Download the official IMF BOP V2.6.0 SDMX-ML structure artefact through a verifiable public registry route; archive the untouched bytes and manifest (exact URL, final URL, UTC retrieval time, HTTP status, content type, byte length, SHA-256). Parse the DSD and referenced codelists; then identify the exact IMF dataflow and its constraints before constructing any observation query. If the raw structure or provider-specific dataflow cannot be verified, keep the exact mapping UNKNOWN. Do not guess codes or query URLs.

## Hard controls
No synthetic values, timestamps, mappings, or query URLs; no paid APIs or external contact; no BOP_AGG estimate substitution; no IIP stock-to-flow conversion; no production selector, ranking, CORE-672, or engine changes. UNKNOWN is never PASS.
