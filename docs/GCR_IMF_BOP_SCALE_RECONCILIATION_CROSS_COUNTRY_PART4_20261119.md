# GCR — Cross-country IMF BOP portfolio-flow scale/sign validation (Part 4)
Date: 2026-11-19
Decision: **124/124 vintage-matched country/period/entry comparisons PASS across five EMDE countries; full 154-member aggregate remains BLOCKED.**

## Progress Log
### Completed
- Prior Part 3 sample: 118/118 PASS across Brazil, India, Mexico and Chile's 2026-09-07 vintage.
- Added Nigeria (NGA) using the Central Bank of Nigeria's official Q2 2026 BOP Highlights, Table 2, printed page 6.
- CBN PDF anonymous retrieval: HTTP 200; 2,206,494 bytes; SHA-256 `b77c0066385cac4bb3bcbe150321c8da28da7d76c91b78423808a31deaea4cf9`.
- IMF public SDMX 3.0 exact country-entry GETs for NGA assets and liabilities both HTTP 200; raw source CSVs archived.
- Q2 2025, Q1 2026 and Q2 2026 × assets/liabilities = 6/6 PASS within ±US$5m, matching CBN's two-decimal USD-billion display precision.
- Combined sample: 118 previous + 6 Nigeria = **124/124 PASS across five countries**.

### Nigeria comparisons
| Period | Entry | CBN USD bn | IMF raw OBS_VALUE | IMF ÷ 1e6 (USD m) | CBN USD m | Residual USD m | Result |
|---|---|---:|---:|---:|---:|---:|---|
| 2025-Q2 | Assets | -0.66 | -661,884,851.605964 | -661.884852 | -660 | -1.884852 | PASS |
| 2026-Q1 | Assets | 0.26 | 261,042,097.262066 | 261.042097 | 260 | 1.042097 | PASS |
| 2026-Q2 | Assets | 0.70 | 703,015,513.296694 | 703.015513 | 700 | 3.015513 | PASS |
| 2025-Q2 | Liabilities | 5.28 | 5,283,292,152.805870 | 5,283.292153 | 5,280 | 3.292153 | PASS |
| 2026-Q1 | Liabilities | 6.03 | 6,025,245,356.212000 | 6,025.245356 | 6,030 | -4.754644 | PASS |
| 2026-Q2 | Liabilities | 7.09 | 7,088,922,653.053650 | 7,088.922653 | 7,090 | -1.077347 | PASS |

Formula:
- `IMF USD million = raw OBS_VALUE / 1,000,000`
- `CBN USD million = published USD billion × 1,000`
- PASS tolerance = ±US$5m, reflecting CBN two-decimal USD-billion rounding.

CBN footnotes identify Q2 2025 as provisional and Q1 2026 as revised; the Q2 2026 narrative describes the current release statistics as provisional. Vintage labels are retained; do not mix vintages silently.

## Reproducibility
- Workflow run: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/44485137974
- Artifact ID: `14510920161`; ZIP 2,056,239 bytes; SHA-256 `bf80b403e072c8eae39f4ec32de77b55d776ef77b7ff4a88e157e3023da7febf`; 90-day retention.
- Durable report: `docs/GCR_IMF_BOP_SCALE_RECONCILIATION_NIGERIA_20261119.md`.
- Durable raw IMF CSVs and comparison: `docs/evidence/gcr_nigeria_bop_20261119/`.
- Raw CBN PDF remains reproducible from its official URL; raw byte hash is recorded above and in `summary.json`. Full downloaded PDF and extracted page text are retained in the workflow artifact.

## Rejected / not authorized
- No universal 154-country scale/sign transform inferred from five countries.
- No EMDE aggregate/net flow, no currency conversion, no imputation, no forward-fill, no synthetic observations.
- No all-country vintage alignment, BPM basis or sign convention assumed.
- No production selector, ranking, pressure-fade, CORE-672 or Engine A–E changes.

## Next actions
1. Extend national-source cross-checks to more members, prioritizing large EMDE markets and exact assets/liabilities legs.
2. Resolve Chile's latest-vintage revision differences and India 2026-Q1 liability REVIEW.
3. Build country-entry-period vintage matrix and explicit coverage eligibility thresholds.
4. Only then evaluate an observed-country subtotal; never label it a complete EMDE aggregate while coverage remains incomplete.

**Decision:** five-country empirical scale/sign evidence strengthened; universal conversion and aggregate admission remain BLOCKED / NOT_AUTHORIZED. UNKNOWN is not PASS.
