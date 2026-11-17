# BCB Portfolio Investment — Multi-Period Reconciliation Progress
Date: 2026-11-17
Branch: research/bcb-priority-metadata-audit-20261117
Scope: research-only accounting identities across the 15 already captured official BCB SGS series.

## Reused evidence — no duplicate acquisition
- Aggregate capture: 7/7 raw series PASS; Run #3 / ID 44075768714; archived in commit 73bf04f6333fd90d8c0d24c7ba9e71eb1ba3f568.
- Instrument capture: 8/8 raw series PASS; archived in commit 527a8d41c434609c980eb3181d491eac4fa6e822.
- Each series contains 381 monthly observations, 1995-01 through 2026-09.
- The raw files and per-series SHA-256 are already in the two archived manifests; this task does not redownload or overwrite them.

## Independent arithmetic recomputation from archived CSV rows
All 15 CSV files were read from the research branch and parsed as monthly USD-million series. The common coverage is 381 months. Six identities were checked over every common month using a strict USD 0.11m residual tolerance (displayed series precision is one decimal USD million).

| Identity | Passing months | Maximum absolute residual | Result |
|---|---:|---:|---|
| 22906 = 22908 − 22907 | 381/381 | 0.1 USD mn | PASS |
| 22924 = 22925 − 22926 | 381/381 | 0.1 USD mn | PASS |
| 22905 = 22906 − 22924 | 381/381 | 0.1 USD mn | PASS |
| 22906 = 22909 + 22912 + 22915 | 381/381 | 0.1 USD mn | PASS |
| 22924 = 22927 + 22936 + 22939 | 381/381 | 0.1 USD mn | PASS |
| 22939 = 22942 + 22945 | 381/381 | 0.1 USD mn | PASS |

Total arithmetic coverage: 2,286 identity-month checks; all 2,286 within tolerance in this independent recomputation.

## Sign conventions established empirically from all 381 monthly rows
- Asset side: SGS 22906 = 22908 (outflows) − 22907 (inflows).
- Liability side: SGS 22924 = 22925 (inflows) − 22926 (outflows).
- Net portfolio investment: SGS 22905 = net acquisition of financial assets (22906) − net incurrence of liabilities (22924).
- Asset instrument components: 22906 = 22909 (equity assets) + 22912 (fund assets) + 22915 (debt assets).
- Liability instrument components: 22924 = 22927 (equity liabilities) + 22936 (fund liabilities) + 22939 (debt liabilities).
- Debt liability market split: 22939 = 22942 (domestic-market debt) + 22945 (external-market debt).

The first two sign conventions were not assumed from English series titles; both candidate orientations were tested. The reverse orientations failed all 381 months and are rejected.

## Runtime reproducibility gate
Added:
- Validator: scripts/research/validate_bcb_portfolio_monthly_identities.py
- Five-minute GitHub Actions workflow: .github/workflows/bcb_portfolio_monthly_identity_qa.yml
- The validator re-hashes all 15 raw CSV files against their exact capture manifests, verifies HTTP/content type/byte length, schema, unique ascending monthly periods and 381-month common coverage, then reruns the six identities.
- The workflow compiles and runs the validator, archives deterministic JSON/Markdown QA outputs to the research branch, and uploads a 90-day artifact.
- Validator commit: 7ea509cc52f9dc8f6a73064fbef0bb7bbf3921d1.
- Workflow commit: 9e2e51551875e35875e83f3d9f71b6198806321d.
- GitHub Actions runtime result: PENDING at the time of this progress update. Do not claim runtime PASS until the workflow run and generated artifacts are inspected.

## Official metadata references
- BCB SGS 22905 portfolio investment aggregate: https://opendata.bcb.gov.br/dataset/22905-portfolio-investment---monthly---net
- BCB SGS 22906 net acquisition of financial assets: https://opendata.bcb.gov.br/dataset/22906-portfolio-investment---net-acquisition-of-financial-assets---monthly---net
- BCB SGS 22907 asset inflows: https://opendata.bcb.gov.br/dataset/22907-portfolio-investment---net-acquisition-of-financial-assets---monthly---inflows
- BCB SGS 22908 asset outflows: https://opendata.bcb.gov.br/dataset/22908-portfolio-investment---net-acquisition-of-financial-assets---monthly---outflows
- BCB SGS 22924 net incurrence of liabilities: https://opendata.bcb.gov.br/dataset/22924-portfolio-investment---net-incurrence-of-liabilities---monthly---net
- BCB SGS 22942 domestic-market debt liabilities: https://opendata.bcb.gov.br/dataset/22942-portfolio-investment---debt-securities----issued-in-the-domestic-market---monthly---net

## Acceptance boundary
- Raw archive reuse and 381-month common-coverage arithmetic recomputation: PASS.
- Six accounting identities in direct recomputation: PASS, 2,286/2,286 checks.
- Raw byte SHA-256 revalidation by new committed validator: PENDING GitHub Actions runtime.
- Instrument semantic labels beyond official dataset metadata and manifest titles: retain exact source wording; no broader mapping inferred.
- Brazil pilot: NOT_ACCEPTED until runtime provenance validation, multi-period independent release-table reconciliation, and vintage/revision gate are closed.
- EM-wide aggregation: NOT_DONE.
- Production/classifier admission: NOT_AUTHORIZED.

## Next actions
1. Verify the workflow runtime and generated QA artifact; fix any mismatch without changing source CSVs.
2. Reconcile the already archived BCB release-table vintages against the corresponding SGS components for multiple reference periods; do not repeat completed January/September checks.
3. Keep February-2026 SGS 22942 revision attribution UNKNOWN unless an immutable original vintage or official revision notice is obtained.
4. No synthetic second vintage. Prospective snapshot comparison waits for the next genuine BCB capture.

## Invariants
₹0; official/free BCB sources only; no synthetic data, fabricated timestamps, forward-fill, raw overwrite or access-control bypass. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A–E, Hard Gate, parser admission and production workflows remain unchanged.