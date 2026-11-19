# Brazil BCB Portfolio Asset-Side Gross-Flow Identity Audit — Continuation 45

Date: 2026-11-19 (UTC retrieval; Asia/Kolkata reporting)
Scope: research-only, official BCB SGS monthly asset-side series. No production integration.

## Decision
**PASS — 381/381 monthly observations** support:

`SGS 22906 = SGS 22908 - SGS 22907`

where 22906 is net acquisition of financial assets, 22907 is inflows and 22908 is outflows. The opposite sign convention is rejected (0/381).

## Official metadata basis
- 22906: https://opendata.bcb.gov.br/dataset/22906-portfolio-investment---net-acquisition-of-financial-assets---monthly---net
- 22907: https://opendata.bcb.gov.br/dataset/22907-portfolio-investment---net-acquisition-of-financial-assets---monthly---inflows
- 22908: https://opendata.bcb.gov.br/dataset/22908-portfolio-investment---net-acquisition-of-financial-assets---monthly---outflows
BCB describes the asset series as portfolio financial-asset transactions in equity/investment-fund shares and debt securities. All three datasets are monthly, USD millions, BCB/Depec.

## Run and immutable evidence
- Workflow: BCB Portfolio Asset Flow Identity (Research Only)
- Run #2 / ID: 44542505681
- Run URL: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/44542505681
- Job ID: 135624309676 — SUCCESS
- Artifact ID: 14538393352
- Artifact ZIP SHA-256: `51ab88b418ebbaa88595a45eb2a94cf8507c454c3c637075b935c8de07dcf762`
- Artifact files: `manifest.json`, `monthly_identity.csv`, raw JSON responses for 22906/22907/22908.
- Commit: `90b1a68aa5c5a36f88293e4c857530268101a86c`
- Script: `scripts/research/validate_bcb_asset_flow_identity.py`
- Script blob SHA: `951943e2edbfb2459def9ff2ee7e646421e927c7`

## Raw series evidence
All three APIs returned HTTP 200 and 381 valid, unique monthly rows, 1995-01 through 2026-09:
- 22906: 14,594 bytes; SHA-256 `110477090f5ff3e9f4e4d2ce235082d837020603b13795dbc2bde20769a3db30`
- 22907: 14,567 bytes; SHA-256 `920aea58c2a7f90106cfeef25b29b077e66d0f65efa73237ba82be34b8885c7a`
- 22908: 14,593 bytes; SHA-256 `7ef8ee458ceae80914183c49334409f175891e0d30d280ad1d513e684c6dc73e`
- Common months: 381; first 1995-01; last 2026-09.
- Candidate A (outflows minus inflows): 381/381 within tolerance; maximum absolute residual 0.1 USD million.
- Candidate B (inflows minus outflows): 0/381; maximum absolute residual 17,048.8 USD million.
- Tolerance 0.15 USD million is applied only because all three published source values are rounded to one decimal place.
- Retrieval UTC window: 2026-11-19T14:19:42.489212Z to 2026-11-19T14:19:45.566810Z (timestamps recorded in manifest with +00:00).

## Rejected prior attempt / lesson learned
- Separate workflow run #2 / ID 44542407481 failed its 381-month identity gate; artifact ID 14537174964; ZIP SHA-256 `102a1d135fceb52493e4fe93f7194dfa99e2a977371487c5a2abf51d9cd7dbf4`.
- That attempt did not establish the correct accounting sign; its 381 failures must not be represented as source-data failures. The bounded follow-up tested both possible conventions against the three raw series and uniquely established the convention above.
- Do not reuse the failed formula or interpret it as evidence against BCB source quality.

## Brazil reconstruction impact
- Asset-side gross-flow identity: PASS (this report).
- Liability-side gross-flow identity: prior evidence remains 381/381 PASS (run 44538706864).
- BCB–IMF quarterly benchmark: prior evidence remains 94/94 PASS (run 44476176136).
- These accounting checks do not resolve the independent IMF Brazil Provision Agreement/Dataflow identity mismatch: PA references `IMF:BOP6(1.0)`, while BCB payload declares `IMF:BOP_BPM6(1.0)`. Shared DSD is not equivalence. Brazil remains INCOMPLETE / BLOCKED pending official PA history/changelog and transaction evidence.

## GCR impact
This strengthens the Brazil country-source benchmark for portfolio asset transactions. It does not close the synchronized multi-country panel, membership/vintage coverage, source-sign harmonization across countries, or relative-attraction formula/backtest. GCR remains INCOMPLETE / BLOCKED; no score or macro weight is promoted.

## No-change statement
₹0; free official BCB sources only. No synthetic values, no inferred timestamps, no invented hashes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56x12), Engines A-E and production admission remain unchanged.

## Next exact actions
1. Reconcile Brazil PA/Dataflow discrepancy using official Brazil-filtered registry event export and exact PA changelog (owner-side export may be required); do not retry known failing equivalent IMF endpoints.
2. GCR: advance the next country-level current-vintage source benchmark and update the vintage-aware coverage matrix; preserve missing observations as UNKNOWN.
3. Integrate this Brazil asset-side PASS only into research evidence, not production scoring.
