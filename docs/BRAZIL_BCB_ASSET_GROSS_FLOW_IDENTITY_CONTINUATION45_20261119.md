# Brazil BCB Portfolio-Asset Gross-Flow Identity — Continuation 45 (2026-11-19)

## Scope and decision

Research-only test of the asset-side decomposition of Brazil's portfolio investment using the Banco Central do Brasil (BCB) official Open Data Portal / BCData SGS series. No production selector, scoring, CORE-672 diagnostics, or Engines A–E were changed.

**Decision: BLOCKED / identity not closed.** The three official series were successfully fetched and parsed with complete aligned coverage, but the executed candidate identity did not reconcile. No PASS is claimed.

## Official source identification

The BCB Open Data Portal identifies:
- SGS 22906: portfolio investment assets, monthly, net.
- SGS 22907: portfolio investment net acquisition of financial assets, monthly, inflows.
- SGS 22908: portfolio investment net acquisition of financial assets, monthly, outflows.

Official dataset pages:
- https://dadosabertos.bcb.gov.br/dataset/22906-investimentos-em-carteira---ativos---mensal---liquido
- https://opendata.bcb.gov.br/dataset/22907-portfolio-investment---net-acquisition-of-financial-assets---monthly---inflows
- https://opendata.bcb.gov.br/dataset/22908-portfolio-investment---net-acquisition-of-financial-assets---monthly---outflows

All are monthly series in USD millions, beginning January 1995. The official 22906 dataset describes portfolio assets as transactions and positions in foreign capital/debt securities, distinct from direct investment and reserve assets. Series labels are preserved as published; the accounting sign is not inferred from the words “inflows” and “outflows”.

## Acquisition evidence

GitHub Actions:
- Workflow: Brazil BCB Portfolio Asset Gross Flow Identity (Research Only)
- Run ID: 44542385747
- Run URL: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/44542385747
- Commit: e12cc14ff8d7d05ac8a3d30728cf87704f5ce5bd
- Run result: FAILURE at the identity gate; capture and artifact upload succeeded.
- Job ID: 135623875310
- Artifact ID: 14537524166
- Artifact name: bcb-asset-gross-flow-44542385747
- Artifact size: 14,404 bytes
- GitHub artifact digest: sha256:7ae136fc9088568f576edf67906fed7c6a3de98ffa8f17ae83e09ef01933d2f3

Captured source series:
| Series | HTTP | Parse | Rows | Coverage | Raw SHA-256 |
|---|---:|---|---:|---|---|
| 22906 net | 200 | PASS | 381 | 1995-01 to 2026-09 | 110477090f5ff3e9f4e4d2ce235082d837020603b13795dbc2bde20769a3db30 |
| 22907 inflows | 200 | PASS | 381 | 1995-01 to 2026-09 | 920aea58c2a7f90106cfeef25b29b077e66d0f65efa73237ba82be34b8885c7a |
| 22908 outflows | 200 | PASS | 381 | 1995-01 to 2026-09 | 7ef8ee458ceae80914183c49334409f175891e0d30d280ad1d513e684c6dc73e |

All three series have 381 unique monthly observations, same first/last month, and no duplicate months. The source capture took approximately five seconds on the GitHub runner.

## Identity test outcome

The workflow tested only the candidate:
`22906 = 22907 - 22908`

Result:
- Common months: 381
- PASS: 0
- FAIL: 381
- Maximum absolute residual: 170,488.0 USD million
- Configured tolerance: 0.15 USD million

This proves that the *tested orientation* does not reconcile. It does not establish the opposite orientation. The raw data must be checked against both candidate identities:
- `22906 = 22907 - 22908`
- `22906 = 22908 - 22907`

Do not change signs or relabel the series merely to force a match. Confirm the official sign semantics in BCB methodological notes and test the alternate orientation against all 381 exact months before acceptance. Any scale, rounding, revision, or definition mismatch must be separately explained.

## Prior evidence retained

The liability-side identity remains independently verified: BCB SGS 22924 = 22925 − 22926, 381/381 PASS, max residual 0.1 USD million, tolerance 0.15; run 44538706864, artifact 14537491095, ZIP SHA-256 69c0b92a5f5bc7221fde47a75a879e3f7c1bf8e0c4727c5299356204dd70aaa1.

The separate quarterly cross-source benchmark remains 94/94 PASS for BCB 22906/22924 versus IMF BOP P_F, 47 quarters; run 44476176136, artifact 14505944936, ZIP SHA-256 1c9c1975717764aea11230f9fb659270a43c98b198e0154605589a1a8a19f317. This benchmark does not validate the gross-flow decomposition.

## Next actions

1. Re-run the existing fail-closed validator that tests both sign orientations on the already archived three-series data; avoid unnecessary re-download.
2. If one orientation passes all 381 months under the established precision tolerance, independently verify that orientation against BCB methodology and document the accounting interpretation.
3. If neither orientation passes, segment residuals by period and inspect official definitions/revisions; keep the decomposition BLOCKED.
4. Preserve raw sources, retrieval timestamps, HTTP headers, byte counts, hashes, and monthly reconciliation output.
5. Only after asset-side identity is resolved, update Brazil's source-validation matrix. This does not resolve the IMF PA `BOP6` vs BCB payload `BOP_BPM6` registration mismatch.
6. GCR remains BLOCKED until synchronized country coverage, vintage, sign, and BPM-basis gates pass.

## Guardrails

- Research-only; no production integration or macro weights.
- ₹0 spend; official public sources only.
- No synthetic observations, interpolation, guessed codes, or fabricated metadata.
- UNKNOWN is never PASS.
- Preserve Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), and Engines A–E unchanged.
