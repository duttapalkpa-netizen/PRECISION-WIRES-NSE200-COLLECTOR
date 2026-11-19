# GNB IMF BOP Exact-Key Probe — Verified Results
Date: 2026-11-19
Continuation: 62

## Executive result
**The focused GitHub workflow completed SUCCESS and its artifact was downloaded and SHA-256 verified. All six requests to the legacy IMF.STA:BOP(21.0.0) dataflow returned HTTP 200 with a valid CSV envelope but zero OBS_VALUE observations. This establishes no returned observations for the exact tested request keys/window; it does NOT establish universal absence from every IMF dataflow/version or every possible indicator/unit. GNB gross-leg admission remains BLOCKED.**

## Workflow and artifact evidence
First exact-key run:
- Workflow run: 44506401980 — SUCCESS
- Artifact ID: 14519308912
- Artifact ZIP: 2,788 bytes
- Artifact SHA-256: 5a9093879b7d94371a7aba10473c10284a96eb106ec85caa9febfe285dce4519
- Raw response files: four; each 400 bytes; each SHA-256 f369fecfb4531216b77a2a0806564140ef8c97fce955e79de92938748d3bb311
- Each CSV contained the header plus a dataflow structure row, no nonempty OBS_VALUE.

Expanded wildcard run:
- Workflow run: 44507263244 — SUCCESS
- Artifact ID: 14520147539
- Artifact ZIP: 3,681 bytes
- Artifact SHA-256: 9a94977b98e010536a7f50553e8a8f843e0d7bd30da9bdfedb7b6aabaaeaa187
- Artifact expiry: 2027-02-17
- Six raw CSV responses included and archive hash rechecked after download.

## Exact tested requests
All requests used dataflow IMF.STA:BOP(21.0.0), 2024 period window:
1. GNB.A_NFA_T.P_F.USD.Q — HTTP 200, CSV parse PASS, 0 observations
2. GNB.L_NIL_T.P_F.USD.Q — HTTP 200, CSV parse PASS, 0 observations
3. GNB.A_NFA_T.P_F.USD.A — HTTP 200, CSV parse PASS, 0 observations
4. GNB.L_NIL_T.P_F.USD.A — HTTP 200, CSV parse PASS, 0 observations
5. GNB.A_NFA_T..USD.Q — HTTP 200, CSV parse PASS, 0 observations (wildcard indicator)
6. GNB.L_NIL_T..USD.Q — HTTP 200, CSV parse PASS, 0 observations (wildcard indicator)

The two wildcard requests returned the same 400-byte header/dataflow-only response as the four exact requests. This is limited to the queried dataflow, country, accounting-entry, unit and frequency dimensions.

## Interpretation
- HTTP 200 is transport success, not data availability.
- Zero observations are not a 404 and do not prove the GNB country is absent from all IMF BOP datasets.
- The wildcard indicator query did not return any observations for either leg in the tested 2024 quarterly scope.
- The annual exact-key query also returned no observations for 2024.
- No values were inferred from BCEAO annual net Financial Account balances.
- No annual-to-quarterly interpolation, stock-to-flow conversion, sign flip, scale conversion, FX conversion, forward-fill, synthetic row or panel admission occurred.

## Structure/version caution
The existing project panel uses IMF.STA:DSD_BOP(24.0.0) with the legacy IMF.STA:BOP(21.0.0) dataflow. IMF/SDMx official documentation lists BOP DSD V2.6.0 (published December 2025); DSD version updates do not automatically invalidate prior versions, and explicit code/codelist crosswalk is required before remapping. See:
- https://sdmx.org/sdmx-data-structure-definitions-for-balance-of-payments-sdmx-bop/
- https://sdmxcentral.imf.org/data/datastructure.html

This probe did NOT query a separate current-version dataflow with a verified v2.6.0 code mapping. That remains a bounded follow-up, not an assumed equivalence.

## Acceptance ledger
| Gate | Result |
|---|---|
| First exact-key workflow | PASS |
| First artifact downloaded and SHA-256 verified | PASS |
| Expanded wildcard workflow | PASS |
| Expanded artifact downloaded and SHA-256 verified | PASS |
| Tested legacy keys returned HTTP 200 | PASS |
| CSV envelope parsed | PASS |
| Nonempty GNB observations for tested 2024 keys | 0 / NOT FOUND |
| Current DSD v2.6.0 crosswalk/API coverage | NOT_DONE |
| Gross assets/liabilities recovered | NO |
| GNB production/backtest admission | BLOCKED |

## Next bounded action
Retrieve the current BOP DSD v2.6.0 and associated dataflow/constraint/codelists from the official SDMx Global Registry; map current accounting-entry and indicator codes explicitly; then make a narrowly scoped GNB query only if a valid current dataflow/provision agreement is established. Preserve raw bytes, HTTP metadata, timestamps and hashes. If current structure has no GNB provision or observations, document that precise scope. Do not infer gross legs from net annual national BOP data.

## Invariants
No production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 or A–E engine changes. No paid APIs. UNKNOWN is never PASS.
