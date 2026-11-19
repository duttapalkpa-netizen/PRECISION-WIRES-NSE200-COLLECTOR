# Brazil BCB Portfolio-Asset Gross-Flow Identity Audit — Continuation 45
Date: 2026-11-19 (Asia/Kolkata)
Scope: official BCB SGS metadata and raw monthly series; research-only; no production changes.

## Decision
**PARTIAL / REVIEW — NOT PASS.** Official series identification and full monthly capture succeeded. Exact net/gross identity matches in 275/381 months. The remaining 106 months each show a USD 1 million residual under the source-published values. No tolerance expansion or rounding explanation is assumed.

## Official series taxonomy
The BCB Open Data Portal official series index places all three under Financial Account / Portfolio Investment / Assets:
- SGS 22906: assets — net (Portuguese: líquido).
- SGS 22907: assets — revenue/receipts (receita).
- SGS 22908: assets — expenditure/payments (despesa).
The official hierarchy establishes the semantic relation and the signed test used here: **22906 = 22908 − 22907**. This is not the same sign convention as the liability-side series.
Official index: https://dadosabertos.bcb.gov.br/pages/temas
Dataset records: https://opendata.bcb.gov.br/dataset/22906-portfolio-investment---net-acquisition-of-financial-assets---monthly---net ; https://opendata.bcb.gov.br/dataset/22907-portfolio-investment---net-acquisition-of-financial-assets---monthly---inflows ; https://opendata.bcb.gov.br/dataset/22908-portfolio-investment---net-acquisition-of-financial-assets---monthly---outflows

## Capture
- Workflow run: 44542572111 (completed; capture job failed strict reconciliation gate; upload succeeded).
- Run URL: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/44542572111
- Artifact ID: 14538838057
- Artifact ZIP SHA-256: 57ab33277c5e1a2ea2a9a2778bc2d1d8f6fc6bfd69c70c061c2df42a318ecb20
- Artifact size: 13,532 bytes.
- All three series: HTTP 200, JSON parse PASS, 381 observations each, 1995-01 through 2026-09, no duplicate months, no missing months.
- Raw 22906 SHA-256: 110477090f5ff3e9f4e4d2ce235082d837020603b13795dbc2bde20769a3db30 (14,594 bytes).
- Raw 22907 SHA-256: 920aea58c2a7f90106cfeef25b29b077e66d0f65efa73237ba82be34b8885c7a (14,567 bytes).
- Raw 22908 SHA-256: 7ef8ee458ceae80914183c49334409f175891e0d30d280ad1d513e684c6dc73e (14,593 bytes).
- Retrieval UTC timestamps and exact source URLs are recorded in the artifact manifest.

## Reconciliation
- Formula tested: 22906 − (22908 − 22907).
- Common months: 381.
- Exact residual zero: 275/381.
- Residual non-zero: 106/381; each residual magnitude USD 1 million.
- Maximum absolute residual: USD 1 million.
- No accepted tolerance was widened. The strict 0.15 USD million gate remains, so these 106 rows are REVIEW, not PASS.
- Initial run 44542407481 exposed two implementation defects: decimal strings were incorrectly parsed by stripping decimal points, and the first sign assumption was reversed. Both were corrected in commit 3724511ffb35592b0c5dc24d856a09d5f9703ca7. The corrected run's values show 275 exact matches and 106 one-million residuals. The earlier run's malformed calculations are not accepted as evidence.

## What is closed / what remains
Closed:
1. Official series IDs and hierarchy confirmed from BCB's official series index.
2. Raw data acquisition and monthly coverage for 1995-01..2026-09.
3. Correct sign convention confirmed empirically against the official hierarchy and the 275 exact identity matches.
4. Parser decimal handling fixed; raw values retained.

Still REVIEW / BLOCKED:
1. Obtain an authoritative BCB statement of published rounding/precision and calculation method for the three series.
2. Determine whether the 106 one-million residuals arise from independent rounding, source compilation, revisions or a genuine non-identity. Do not infer.
3. Only after the above, independently validate the 106 rows against source-level detail or official monthly tables.
4. Do not combine this asset-side test with the separate liability-side identity as if they shared sign semantics.

## Reproducibility and guardrails
- Code: scripts/research/capture_bcb_asset_gross_flow.py
- Code fix commit: 3724511ffb35592b0c5dc24d856a09d5f9703ca7
- Capture workflow: .github/workflows/bcb_asset_gross_flow.yml
- Workflow creation commit: e12cc14ff8d7d05ac8a3d30728cf87704f5ce5bd
- Trigger commit: 54f7dfe517db6c87a96004099a1915cba36c9ec4
- ₹0; free official BCB sources only.
- No synthetic data, no inferred timestamps, no tolerance relaxation, no production integration.
- Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E unchanged.
- UNKNOWN is never PASS.

## Next highest-value action
Retrieve the official BCB methodological note / metadata explaining how portfolio-asset net, revenue and expenditure series are calculated and rounded. Then re-test only the 106 residual months against that documented precision rule. Keep 275 exact matches as PASS and 106 unresolved as REVIEW until authoritative evidence settles them.
