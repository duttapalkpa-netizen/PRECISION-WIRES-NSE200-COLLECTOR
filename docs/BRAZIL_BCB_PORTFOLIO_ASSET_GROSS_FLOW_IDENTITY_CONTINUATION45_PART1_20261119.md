# Brazil BCB Portfolio Asset Gross-Flow Identity Audit — Continuation 45 Part 1
Date: 2026-11-19 (Asia/Kolkata)
Decision: **PASS — BCB monthly portfolio asset net acquisition (SGS 22906) reconciles to gross outflows (22908) minus gross inflows (22907) for all 381 common months, within source rounding tolerance.**

## Progress Log
### Completed / reused
- Reused existing BCB asset net series 22906 raw baseline SHA-256 `110477090f5ff3e9f4e4d2ce235082d837020603b13795dbc2bde20769a3db30`; did not re-fetch or alter the historical raw value.
- Reused the established monthly liability-side identity from Continuation 40 Part 1: 22924 = 22925 - 22926, 381/381 PASS.
- Reused official BCB Open Data Portal metadata for 22906 (net acquisition), 22907 (inflows), 22908 (outflows). No identifier guessed.

### Defect found and fixed
- First asset run used a parser that removed decimal points from Brazilian decimal strings (e.g. `190.5` became `1905`), producing false residuals and 106 false failures. No data or conclusion was accepted from that run.
- Corrected parser to `Decimal(str(valor).replace(",", "."))`, preserving decimal point and avoiding binary floating-point. This is a code/parser correction, not a change to the source data or tolerance.
- A subsequent commit fixed an escaped newline in the import statement. The successful run below executes the corrected code. Prior failed runs are retained as rejected attempts and not treated as evidence.

## Official raw capture
- Source: Banco Central do Brasil SGS API; all HTTP 200.
- Requested period: 1995-01 through current retrieval date 2026-11-19; latest observation 2026-09.
- Each series: 381 unique valid monthly rows; 381 common months; no missing months.
| Series | Meaning | Bytes | SHA-256 |
|---|---|---:|---|
| 22906 | Portfolio investment — net acquisition of financial assets, monthly net | 14,594 | `110477090f5ff3e9f4e4d2ce235082d837020603b13795dbc2bde20769a3db30` |
| 22907 | Portfolio investment — net acquisition of financial assets, monthly inflows | 14,567 | `920aea58c2a7f90106cfeef25b29b077e66d0f65efa73237ba82be34b8885c7a` |
| 22908 | Portfolio investment — net acquisition of financial assets, monthly outflows | 14,593 | `7ef8ee458ceae80914183c49334409f175891e0d30d280ad1d513e684c6dc73e` |

## Identity
Tested official metadata-supported candidate:
`22906 = 22908 - 22907`

- PASS: 381/381
- FAIL: 0
- Maximum absolute residual: USD 0.1 million
- Tolerance: USD 0.15 million (three source values at one decimal precision)
- No missing common month.
- Reverse candidate `22906 = 22907 - 22908` is not the identity and was not accepted.

Example Jan 1995: net 10.8 = outflows 55.0 - inflows 44.2. This supports the asset-side sign direction independently of the liability-side identity.

## Run and artifact
- Workflow run `44542948903`, SUCCESS; URL https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/44542948903
- Artifact ID `14537454647`, name `bcb-asset-gross-flow-44542948903`.
- ZIP SHA-256 independently recomputed and matches GitHub artifact digest: `5b7296d257d60ab0be49b1658e9f942b3f5827c92bb4f0ab92a052e174514969`.
- Artifact manifest independently inspected; all three raw JSON hashes match manifest.

## Brazil Reconstruction acceptance impact
- Asset gross-flow identity: PASS 381/381.
- Liability gross-flow identity: PASS 381/381 (Continuation 40 Part 1).
- Both sides now have source-native monthly internal accounting checks over 1995-01–2026-09.
- This does NOT resolve IMF PA/Dataflow identity: PA/registration uses `IMF:BOP6(1.0)`, BCB payload declares `IMF:BOP_BPM6(1.0)`. No alias or crosswalk inferred.
- IMF BOP scale/sign benchmark remains 94/94 Brazil comparisons PASS; separate from gross-flow identities.
- Brazil Reconstruction remains BLOCKED pending authoritative PA/payload identity or correction evidence, and any remaining required Brazil reconstruction gates.

## GCR impact and invariants
- Stronger validated Brazil portfolio-flow source layer is now available for GCR with asset and liability gross/net decomposition; this is not yet a synchronized country panel.
- GCR remains blocked by 154-member coverage completeness (40 no-data countries, 3 one-sided, 83 empty country-entry cells, 13 interior-gap series), Chile current-vintage review differences, and BPM/period-vintage alignment.
- Do not combine assets and liabilities into an invented attraction score or EMDE aggregate until those gates pass.
- ₹0; no synthetic data; raw source values preserved; UNKNOWN is not PASS.
- Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E unchanged. No production integration or macro weights.

## Exact next action
1. For Brazil: keep the two BCB internal identities as PASS and pursue only authoritative IMF BR1 PA revision/migration/registration evidence for the unresolved BOP6 vs BOP_BPM6 identity. Public page JS exposes a registration inventory query path, but direct public route attempts returned 404/No Results; do not keep guessing endpoint paths.
2. For GCR: highest-value next bounded task is source-native vintage/coverage repair for the country panel (starting with missing/one-sided EMDE cases and Chile Q1/Q2 2026 revision reconciliation); preserve every missing cell explicitly.
