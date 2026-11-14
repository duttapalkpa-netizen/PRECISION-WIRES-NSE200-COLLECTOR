# IMF BOP SDMX 2.1 Candidate Dataflow and DSD Descendant Audit

Audit date: 2026-11-14 (UTC)
Branch: research/imf-bop-access-audit-v1
Scope: public IMF SDMX Central structure metadata only. No observations or dataflow crosswalk to the IMF Data Portal dataset are claimed.

## Executive result

**PUBLIC METADATA RETRIEVAL: PASS. COMPONENT/CODELIST INVENTORY: PASS. IMF DATA PORTAL CROSSWALK: UNKNOWN. COUNTRY OBSERVATIONS: NOT DONE.**

The official IMF SDMX Central Structure REST service successfully returned parseable SDMX-ML 2.1 for:
- IMF dataflow BOP_GBPM6 version 2.0 and its descendant structures;
- IMF dataflow BPM6_BOP_Q version 1.5 and its descendant structures;
- IMF Data Structure Definition IMF:BOP version 2.6.0 and its descendant structures.

The decisive version relationship is:
- IMF:BOP_GBPM6(2.0) explicitly references IMF:BOP(2.0), not IMF:BOP(2.6.0).
- IMF:BPM6_BOP_Q(1.5) explicitly references IMF:BOP(1.5), not IMF:BOP(2.6.0).
- IMF:BOP(2.6.0) is separately retrievable as a public DSD, but the tested candidate dataflows do not reference it.

This is why the BOP DSD 2.6.0 must not be silently substituted for the DSD actually referenced by a selected dataflow.

## Official service boundary and correction

The IMF SDMX Central Web Services Guide (last updated May 2025) documents:
- Public GET Structure REST API at `https://sdmxcentral.imf.org/sdmx/v2/` for Dataflows, Data Structures, Codelists and other metadata.
- Separate public POST processing endpoints for validation (`/ws/public/data/validate`) and transformation (`/ws/public/data/transform`), and data registration operations.
- It does not document an anonymous raw-observation GET endpoint at the SDMX Central Structure REST service.

The IMF Data Portal API help separately states that Data Portal datasets are accessible through SDMX 2.1 and SDMX 3.0 APIs, while its Swagger/API explorer requires beta portal sign-in. Thus SDMX Central metadata retrieval is not the same thing as IMF Data Portal observation access.

Correction to the initial exploratory interpretation: the generic SDMX Central page wording about querying structures and data must not be read as proof that the Structure REST API provides the required BOP country observations. The specific service guide's operation definitions control the conclusion.

## Candidate dataflow / DSD results

### IMF:BOP_GBPM6(2.0)

- HTTP 200; SDMX-ML 2.1 parsed.
- Dataflow name: Balance of Payments _Global use_BOP_BPM6.
- Exact DSD reference: IMF:BOP(2.0).
- Raw descendant XML: 853,627 bytes.
- Raw XML SHA-256: `d1698e30516d554740d269db5126487902fc2632131bf0ae3add26aefa7f63c7`.
- DSD components: 18 dimensions including TIME_PERIOD; 15 attributes; primary measure OBS_VALUE.
- 22 unique direct codelist references resolved by descendant response.

### IMF:BPM6_BOP_Q(1.5)

- HTTP 200; SDMX-ML 2.1 parsed.
- Dataflow name: Balance of Payments --BPM6--Global DSD.
- Exact DSD reference: IMF:BOP(1.5).
- Raw response: 42,202 bytes; SHA-256 `455f510be1b86fea238e6aa1327ca7bad152d382883378ffeccd88a6048b592d`.
- Direct XML component inspection: 17 dimensions including TIME_PERIOD; 14 attributes; primary measure OBS_VALUE. Unlike DSD 2.0/2.6.0, this version does not contain TYPE_ENTITY as a dimension.
- This is a distinct vintage and must not be treated as dimension-identical to DSD 2.0/2.6.0.

### IMF:BOP(2.6.0)

- HTTP 200; SDMX-ML 2.1 parsed.
- Raw direct response: 30,282 bytes; SHA-256 `fe03227eda536a17388df5c2bb8d9840f681fa8faf0c20c4278b901d588df5f1`.
- Raw descendant response: 1,078,911 bytes; SHA-256 `0282f8ed931fc1c058c5f612f9b5c5c3ca60fa0590344d059d3ed2f547fd19ea`.
- DSD components: 18 dimensions, 15 attributes, primary measure OBS_VALUE.
- Dimension order (1-based):
  1 FREQ
  2 ADJUSTMENT
  3 REF_AREA
  4 COUNTERPART_AREA
  5 REF_SECTOR
  6 COUNTERPART_SECTOR
  7 FLOW_STOCK_ENTRY
  8 ACCOUNTING_ENTRY
  9 INT_ACC_ITEM
  10 FUNCTIONAL_CAT
  11 INSTR_ASSET
  12 MATURITY
  13 UNIT_MEASURE
  14 CURRENCY_DENOM
  15 VALUATION
  16 COMP_METHOD
  17 TYPE_ENTITY
  18 TIME_PERIOD (time dimension)
- 15 attributes: TIME_FORMAT, OBS_STATUS, CONF_STATUS, PRE_BREAK_VALUE, COMMENT_OBS, COMMENT_TS, TITLE, UNIT_MULT, DECIMALS, TIME_PER_COLLECT, REF_PERIOD_DETAIL, COMPILING_ORG, DATA_COMP, DISS_ORG, TITLE_COMPL.
- 22 unique direct codelist references were found on the DSD components. The descendants response contained 23 codelist objects because it also returned an additional related CL_AREA version 1.17.0 beyond the direct CL_AREA 2.0.0 reference.

## Codelist and country-code verification

For IMF:BOP(2.6.0), the REF_AREA and COUNTERPART_AREA dimensions reference IMF:CL_AREA(2.0.0). That codelist contains 931 codes in the captured response. An additional related IMF:CL_AREA(1.17.0) codelist was returned in the descendants payload with 918 codes; it is not the direct REF_AREA reference recorded in this DSD.

For IMF:BOP(2.0), the REF_AREA/COUNTERPART_AREA codelist reference is IMF:CL_AREA(1.14), with 885 codes.

The code `IN` is labelled `India` in:
- IMF:CL_AREA(2.0.0), the direct DSD 2.6.0 area-code list;
- IMF:CL_AREA(1.14), the area-code list referenced by BOP_GBPM6(2.0).

This confirms the India code within these specific codelists only. It does not establish that the IMF Data Portal dataset URN `IMF.STA:BOP(21.0.0)` maps to either candidate dataflow, nor does it verify reporter coverage in observations.

## Run and artifact evidence

### Candidate flow / DSD retrieval

- Run ID: 43608726175 — SUCCESS.
- Workflow commit: `eabcde2975fb19da9219700c8a08704c34559d2c`.
- Artifact ID: 14119193255.
- Artifact ZIP SHA-256: `ca28bfd7d48b0e304ce2a41176c3ccf1a5ea241cf24eba880c9c5de246551399`.
- Raw response SHA-256 values:
  - BOP_GBPM6(2.0): `f3d6e3edfbcb0951023c93c776279a9e966c2c3fdd49d360af0add50d4bceb62`
  - BPM6_BOP_Q(1.5): `455f510be1b86fea238e6aa1327ca7bad152d382883378ffeccd88a6048b592d`
  - BOP(2.6.0): `fe03227eda536a17388df5c2bb8d9840f681fa8faf0c20c4278b901d588df5f1`

### Descendant / codelist retrieval

- Run ID: 43608839976 — SUCCESS.
- Workflow commit: `9e8cafda5a878bd7c212b9b3b385ea648e4c3b12`.
- Artifact ID: 14119642179.
- Artifact ZIP SHA-256: `d99c92c23fe8d5f789e4ffd99fdd807f5331c4b261083eb63b0c9fb315ce856d`.
- Raw response SHA-256 values:
  - BOP(2.6.0) descendants: `0282f8ed931fc1c058c5f612f9b5c5c3ca60fa0590344d059d3ed2f547fd19ea`
  - BOP_GBPM6(2.0) descendants: `d1698e30516d554740d269db5126487902fc2632131bf0ae3add26aefa7f63c7`

## Parser correction

The first inventory script in Run 43608726175 used a broad descendant search for elements named Dimension, which also captured nested Dimension references inside attribute attachment relationships. This produced a noisy component list with empty IDs. The raw XML was retained. The follow-up parser now scopes dimensions to the direct children of DataStructureComponents/DimensionList, attributes to AttributeList, and measures to MeasureList. The 18/17 dimension counts and ordered IDs in this report come from direct XML component parsing, not the flawed broad descendant list.

## Acceptance matrix

| Gate | Status |
|---|---|
| Public SDMX Central SDMX-ML 2.1 request route verified | PASS |
| BOP_GBPM6(2.0) dataflow and exact DSD reference retrieved | PASS |
| BPM6_BOP_Q(1.5) dataflow and exact DSD reference retrieved | PASS |
| BOP DSD 2.6.0 retrieved and parsed | PASS |
| BOP DSD 2.6.0 ordered dimension/attribute/measure inventory | PASS |
| Descendant codelist inventory retrieved for BOP DSD 2.6.0 | PASS |
| India code IN confirmed in the selected CL_AREA versions | PASS |
| Portal URN IMF.STA:BOP(21.0.0) mapped to a tested SDMX Central dataflow | UNKNOWN |
| IMF Data Portal public observation access verified without beta login | BLOCKED |
| India BOP portfolio investment observations acquired | NOT DONE |
| EMDE reporter coverage reconciled | NOT DONE |
| EM portfolio-flow aggregate | BLOCKED |

## Next action

Do not query observations using a guessed key or treat the SDMX Central Structure service as a data dissemination endpoint. The next valid path is to test the IMF Data Portal's official Download/View Data public controls or use a user-authorized beta-portal API schema/export. If an unauthenticated official download is available, archive it and reconcile its embedded dataflow/DSD/vintage to the structures above before parsing any country observations.

## Invariants

Research-only, ₹0 spend, official sources only. No paid APIs, no credentials, no authentication bypass, no external contact, no synthetic data/timestamps, no PR merge, no production changes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, engines and Hard Gate unchanged.
