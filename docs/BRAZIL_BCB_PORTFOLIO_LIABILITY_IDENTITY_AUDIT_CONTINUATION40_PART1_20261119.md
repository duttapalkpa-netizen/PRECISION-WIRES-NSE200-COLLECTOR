# Brazil Portfolio Liabilities — Monthly Inflow/Outflow/Net Identity Audit
Date: 2026-11-19 (Asia/Kolkata)
Continuation: Research verification 40, Part-1
Decision: **381/381 monthly identity checks PASS**. This closes one independent BCB accounting-consistency gate only; it does not resolve IMF Brazil PA/Dataflow identity or authorize GCR aggregation.

## Progress Log
### Reused / completed
- Reused the prior 47-quarter IMF BOP Data Portal vs BCB national-source reconciliation: BCB SGS 22906/22924, 94/94 PASS. No repeat.
- Reused the Part-8 BCB SGS 22925 raw capture; verified its SHA-256 again against the new artifact.
- Official BCB metadata identifies SGS 22924 as net incurrence of portfolio-investment liabilities, SGS 22925 as liability inflows, and SGS 22926 as liability outflows. See official datasets: https://opendata.bcb.gov.br/dataset/22924-portfolio-investment---net-incurrence-of-liabilities---monthly---net ; https://opendata.bcb.gov.br/dataset/22925-portfolio-investment---net-incurrence-of-liabilities---monthly---inflows ; https://opendata.bcb.gov.br/dataset/22926-portfolio-investment---net-incurrence-of-liabilities---monthly---outflows .
- Rejected treating 22925 as a replacement for 22924; they are distinct gross-inflow and net measures.

## Method
Tested monthly identity:
`SGS 22924 = SGS 22925 - SGS 22926`
All values are in USD million. Three series are fetched independently from BCB's public SGS JSON endpoint; exact response bytes, retrieval timestamps, HTTP response headers, byte counts and SHA-256 are retained. Monthly dates are joined by YYYY-MM. A row passes only when all three values exist, each has one decimal place, and the absolute residual is <= USD 0.15 million, the maximum rounding bound for three one-decimal values. No interpolation or missing-value fill.

## GitHub Actions evidence
- Workflow: `.github/workflows/bcb_liability_flow_identity.yml`
- Script: `scripts/research/validate_bcb_liability_flow_identity.py`
- Run ID: `44538706864`; run #1; completed SUCCESS. URL: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/44538706864
- Artifact ID: `14537491095`; name `bcb-liability-identity-44538706864`; 15,478 bytes.
- ZIP SHA-256 (independently recomputed; equals GitHub artifact digest): `69c0b92a5f5bc7221fde47a75a879e3f7c1bf8e0c4727c5299356204dd70aaa1`.
- Artifact contents: three raw JSON files, manifest, monthly identity CSV.

## Raw response integrity
| SGS | Meaning | Bytes | SHA-256 |
|---|---|---:|---|
| 22924 | Liabilities net incurrence | 14,890 | `2064005a5dd42b83ba66aeb21de983ca4286af9662f57c23971b4b7dfe295dbb` |
| 22925 | Liabilities inflows | 15,086 | `807652fcfc3e17a710ba6dffcb78208bc41c10ec6c2f18986b61e832c6ebd2e0` |
| 22926 | Liabilities outflows | 15,068 | `519fcd8c068716f80f300202a1ae970fbcf312cfcd902f147143ccc5b4031e8e` |

All three responses HTTP 200; each 381 valid monthly rows, 1995-01 through 2026-09; no invalid rows. The 22925 hash matches Part-8's independently archived response exactly. ZIP hash and each raw-file hash were independently recomputed from the downloaded artifact.

## Identity results
- Common matched months: 381/381.
- PASS: 381; REVIEW: 0; missing months: 0.
- Maximum absolute residual: USD 0.1 million; permitted bound: USD 0.15 million.
- 98 rows have non-zero residuals, all within the documented rounding bound; 283 exact zero-residual rows.
- Example first month 1995-01: net -890.7 = inflows 1,881.3 - outflows 2,772.0.
- Example last month 2026-09: net -1,698.5 vs inflows 34,689.0 - outflows 36,387.6 = -1,698.6; residual +0.1, PASS.

## Acceptance matrix
| Gate | Status |
|---|---|
| Official metadata for 22924/22925/22926 | PASS |
| Three raw SGS downloads HTTP 200 | PASS |
| 381 valid observations per series | PASS |
| Exact date-key join / no missing common months | PASS |
| Monthly identity within rounding tolerance | PASS (381/381) |
| Artifact ZIP and raw hashes independently verified | PASS |
| Brazil IMF Data Portal 94-quarter scale/sign check | Previously PASS; not rerun |
| BCB registered XML BOP_BPM6 vs Brazil PA BOP6 identity | BLOCKED / unresolved |
| Full Brazil PA revision chronology | NOT_DONE |
| GCR 154-member coverage/vintage/BPM gate | BLOCKED / partial |
| EMDE aggregate / production admission | NOT_AUTHORIZED |

## Interpretation / limitations
This proves that BCB's gross liability inflows less gross liability outflows reproduce its net liability incurrence series for the entire currently captured monthly history, within source rounding. It provides a robust national-source internal accounting check and confirms the three SGS roles are not interchangeable. It does not prove a Brazil-specific crosswalk between IMF Data Portal BOP P_F and the separately registered BCB SDMX BOP_BPM6 payload; it does not settle the PA StructureUsage mismatch (Brazil PA BOP6 vs BCB payload BOP_BPM6); it does not establish the IMF registration chronology. Do not use the identity to infer a production capital-attraction score or combine gross and net measures as if they were separate independent capital flows.

## Exact next actions
1. Preserve this 381-month gross-to-net identity as a Brazil national-source integrity gate.
2. Resolve the IMF Brazil PA/Dataflow mismatch only with official owner-side PA revision/changelog and BR1 registration evidence; do not repeat failed transaction-ID-2 calls or alias Dataflows.
3. For GCR, prioritize Chile raw historical vintage recovery and further national-source vintage reconciliation; maintain 40 no-data EMDE countries, 83 empty country-entry cells and 13 interior-gap series as missing.
4. No EMDE aggregate until country coverage, BPM6/BPM7, vintage, sign and semantics gates are explicitly passed.

## Invariants
₹0; official free sources only; no synthetic values, inferred timestamps, or fabricated hashes; UNKNOWN is not PASS. No production integration, macro weights, selector/ranking/pressure-fade/CORE-672/Engines A-E changes.
