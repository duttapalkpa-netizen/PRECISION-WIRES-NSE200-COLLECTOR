# IMF BOP DSD_BOP(24.0.0) component, codelist and eligibility audit

Audit date: 2026-11-14 UTC
Branch: `research/imf-bop-access-audit-v1`
Dataflow: `IMF.STA:BOP(21.0.0)`
Data structure: `IMF.STA:DSD_BOP(24.0.0)`

## 1. Run and immutable evidence

- Workflow: `.github/workflows/imf_bop_dsd24_component_eligibility.yml`
- Workflow commit: `339664040ff7e9338d3c013d9b89d0301de5a973`
- Run ID: `43628988259` — SUCCESS.
- Job ID: `132551143961` — SUCCESS.
- Artifact ID: `14126994489`
- Artifact ZIP SHA-256: `80b69fb559c22ee3a99641c58c2b1b3f8041c75e923a61aa25aa16e4ec772e28`
- Dataflow structure response: HTTP 200, 3,965,650 bytes, SHA-256 `d21181c24cc28b104e42fc12e98f4ea6abedbac1b47bae246e4a3498aa74a311`.
- DSD structure response: HTTP 200, 3,964,221 bytes, SHA-256 `bfeb109c4efb636ea9bb19b90060de3526efe3ae4642951a7af6e9a87832101a`.
- Exact BOP dataflow-to-DSD link: PASS.
- Exact structure XML parsed; artifact contains raw XML, component audit JSON and endpoint response records.

## 2. Exact DSD component-to-codelist crosswalk

All five required dimensions and their exact concept-scheme references were resolved to codelists present in the same official IMF structure response:

| DSD dimension | Concept reference | Codelist reference | Codes |
|---|---|---|---:|
| COUNTRY | IMF.STA:CS_BOP(17.0.0).COUNTRY | IMF.STA:CL_BOP_COUNTRY(1.0.0) | 345 |
| BOP_ACCOUNTING_ENTRY | IMF.STA:CS_BOP(17.0.0).BOP_ACCOUNTING_ENTRY | IMF.STA:CL_BOP_ACCOUNTING_ENTRY(3.3.0) | 97 |
| INDICATOR | IMF.STA:CS_BOP(17.0.0).INDICATOR | IMF.STA:CL_BOP_INDICATOR(10.0.0) | 979 |
| UNIT | IMF:CS_MASTER_DATA(1.0.0).UNIT | IMF:CL_UNIT(2.11.2) | 270 |
| FREQUENCY | IMF:CS_MASTER_SYSTEM(1.0.2).FREQ | IMF:CL_FREQ(1.2.0) | 34 |

This corrects the previous first-pass parser limitation: it did not descend through DataStructureComponents and did not resolve CoreRepresentation/Enumeration references from the referenced ConceptScheme. The focused parser now resolves the exact five dimension references and finds every referenced codelist in the official response.

## 3. IFS_FLAG exact component semantics

The exact DSD contains an attribute component:
- Component: `IFS_FLAG`
- Concept: `IMF.STA:CS_MASTER(1.0.0).IFS_FLAG`
- English name: “IFS flag”
- Official concept description: “A key indicator flag is used to identify and mark indicators that were part of the IFS data product.”
- Core representation: `TextFormat textType="Boolean"`
- DSD assignment status: `Conditional`
- Attribute relationship: `COUNTRY, BOP_ACCOUNTING_ENTRY, INDICATOR, FREQUENCY, UNIT`.

Therefore:
- IFS_FLAG component existence: PASS.
- Boolean data type: PASS.
- Attribute attachment dimensions: PASS.
- Its documented meaning is historical IFS product membership at the series-dimension combination; it is not a reporter eligibility flag and does not establish observation completeness, timeliness, quality, or current availability.
- Conditional assignment plus Boolean representation does not define the meaning of an omitted/null value. Null semantics remain UNKNOWN; do not coerce missing to false or true.

## 4. Constraint / provider endpoint checks

The following unauthenticated public IMF SDMX endpoints were probed and each returned HTTP 204 with zero bytes and SHA-256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`:
- exact BOP content constraint: `/contentconstraint/IMF.STA/BOP/21.0.0?references=all`
- agency-wide content constraints: `/contentconstraint/IMF.STA/all/latest?references=all`
- agency-wide provision agreements: `/provisionagreement/IMF.STA/all/latest?references=all`
- agency-wide data provider schemes: `/dataproviderscheme/IMF.STA/all/latest?references=all`

HTTP 204 is a no-content response for each requested endpoint. It is not evidence that all reporters are eligible, nor does it prove that no restrictions exist in another agency/resource or in documentation outside these probes. No reporter-specific eligibility constraint was retrieved.

## 5. Gate disposition

| Check | State |
|---|---|
| Exact dataflow-to-DSD reference | PASS |
| Five required dimension definitions | PASS |
| Five exact concept-to-codelist mappings | PASS |
| All five codelists found and inventoried | PASS |
| IFS_FLAG component and concept | PASS |
| IFS_FLAG Boolean representation | PASS |
| IFS_FLAG attachment dimensions | PASS |
| IFS_FLAG missing/null semantics | UNKNOWN |
| Reporter-specific eligibility for 39 countries | UNKNOWN |
| 39-country historical coverage acceptance | NOT PASS |
| EMDE aggregation | BLOCKED |

No observation query was repeated. No missing country was relabelled as ineligible. Previously reported 39-country “no observations in tested windows” remains a coverage observation only, not a definitive eligibility finding. No aggregation was performed.

## 6. Next decision

The remaining unresolved item is not the DSD's dimension/codelist wiring: that structural task is complete. To prove or disprove eligibility for the 39 reporters, the next evidence must be an official reporter-specific applicability/coverage rule or a country × accounting-entry × indicator × unit × frequency metadata/observation inventory for the exact 39 reporters. If the public API exposes no such eligibility contract, preserve UNKNOWN and document the API limitation; do not invent a rule.

## 7. Protected invariants

₹0 spend; public official IMF endpoints only; no credentials, sign-in, paid APIs, synthetic rows, fabricated timestamps, external contact, PR merge, or production integration. Production Selector, `RANKING_SCORE`, `+1 PRESSURE_FADE`, CORE-672 (56 × 12), engines A–E, and Hard Gate remain unchanged.
