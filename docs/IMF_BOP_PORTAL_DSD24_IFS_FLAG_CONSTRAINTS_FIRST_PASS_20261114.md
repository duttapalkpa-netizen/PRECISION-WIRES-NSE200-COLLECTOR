# IMF Portal DSD_BOP(24.0.0) exact-structure retrieval — first-pass audit

Audit date: 2026-11-14 (UTC)
Branch: `research/imf-bop-access-audit-v1`
Dataset: `IMF.STA:BOP(21.0.0)`
Expected DSD: `IMF.STA:DSD_BOP(24.0.0)`
Purpose: continue the IFS_FLAG / 39-reporter eligibility investigation without repeating observation queries.

## 1. Run and provenance

- Workflow: `.github/workflows/imf_bop_portal_dsd24_ifs_flag_constraints.yml`
- Workflow creation commit: `5c5ce0b637dce55efc2b6fc125d58f8e084a042e`
- Run ID: `43627524825` — SUCCESS.
- Artifact ID: `14126861311`
- Artifact ZIP SHA-256: `054249b68772fcf4fde8eeccae6892e18180c3cdbb88f78038b16f268b804c21`
- Dataflow response: HTTP 200; 3,965,650 bytes; SHA-256 `48777f898e943bbb15464bcbe9e99d719f2c94e5284543212d4eb6ec4e583877`.
- Exact DSD response: HTTP 200; 3,964,221 bytes; SHA-256 `82886da6dd396373ec85ffc94430bfe36ba838331ec7c93eb304df265ba2637e`.
- Dataflow response explicitly references `IMF.STA:DSD_BOP(24.0.0)`; the independently requested DSD response identifies the same agency, ID and version. Exact Portal dataflow-to-DSD identity check PASS.
- No BOP observations were queried and no coverage data were regenerated.

## 2. IFS_FLAG component evidence

The exact Portal DSD response contains a direct attribute component `IFS_FLAG`:
- Concept identity: `IMF.STA:IFS_FLAG`.
- DSD assignment status: `Conditional`.
- The first-pass component parser did not resolve a direct local codelist reference for this attribute. Therefore the allowed lexical values and the DSD-level encoding/representation of null remain UNKNOWN from this audit.
- The XML component's attachment relationship was flattened by the first-pass parser; attachment level is not promoted to PASS pending a focused parser/read-back.

This is additional structural evidence that IFS_FLAG is a real DSD attribute, not merely an invented field name. It does not change the official IMF semantic determination already recorded: the flag identifies former-IFS series. It does not establish reporter eligibility or quality/completeness.

## 3. Codelists and constraints — first-pass boundary

- The exact DSD request used `references=all` and returned a parseable 3.96 MB SDMX-ML structure response containing codelist structures.
- The first-pass inventory identified codelist objects, but its component-level codelist-reference extraction was incomplete (the dimension and IFS_FLAG component rows did not resolve direct codelist refs). Do not claim the exact `BOP_ACCOUNTING_ENTRY`, `INDICATOR`, `UNIT`, `FREQUENCY`, or `COUNTRY` codelist links are fully reconciled from this parser output.
- The first-pass ContentConstraint request `/contentconstraint/IMF.STA/all/latest?references=all` returned HTTP 204, zero bytes, SHA-256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.
- This establishes only that this particular agency-wide ContentConstraint request returned no body. It does not prove that no constraints exist under another agency, provision agreement, data provider, or narrower resource query. No reporter-specific eligibility constraint was found in the inspected response because it contained no constraint object.
- IMF SDMX documentation distinguishes DSD representations from dataflow/provider/provision-agreement constraints; a code's presence in a codelist is not proof that every reporter can supply every indicator/unit/frequency combination.

## 4. Eligibility decision

- IFS_FLAG semantic identification: PASS (100% of the defined semantic subtask).
- IFS_FLAG DSD component existence: PASS.
- IFS_FLAG allowed-value representation and null semantics: UNKNOWN.
- Complete component-to-codelist crosswalk: INCOMPLETE / UNKNOWN.
- Dataflow/provider/provision-agreement reporter-specific constraints: NOT ESTABLISHED.
- 39-country exact-series eligibility: UNKNOWN (0% resolved).
- EMDE reporter coverage acceptance: NOT PASS.
- EMDE aggregation: BLOCKED.

No absent reporter is classified as ineligible. The 39-country status remains “NO OBSERVATIONS IN EITHER TESTED WINDOW” (2000-Q1–2014-Q4 and 2015-Q1–2025-Q4), not permanent non-reporting, not economic zero, and not proof of non-applicability.

## 5. Next precise action

Perform a focused SDMX-ML component parser against the already archived exact DSD response (do not repeat the data queries): enumerate only direct children of DimensionList and AttributeList; resolve each component's ConceptIdentity and LocalRepresentation/Enumeration references; resolve the referenced ConceptScheme definitions for IFS_FLAG; and inventory the exact ContentConstraint, ProvisionAgreement and DataProvider structures that can be queried for the BOP dataflow. Preserve every HTTP 204/404 and parser limitation. If no reporter-specific constraint is present in the inspected official structures, report only “no eligibility constraint found in inspected artefacts”, leaving reporter eligibility UNKNOWN.

## 6. Invariants

₹0 spend; free official sources only; no paid API, sign-in, credential use, authentication bypass, external contact, synthetic values/timestamps, PR merge, or production integration. Production Selector, `RANKING_SCORE`, `+1 PRESSURE_FADE`, CORE-672 (56 × 12), engines A–E and Hard Gate unchanged.
