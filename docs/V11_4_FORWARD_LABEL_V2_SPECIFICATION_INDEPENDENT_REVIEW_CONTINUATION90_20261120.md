# V11.4 Forward-Label V2 Specification — Independent Review
Date: 2026-11-20
Status: DOCUMENT REVIEW PASS (12/12); IMPLEMENTATION NOT AUTHORIZED; PERFORMANCE ACCEPTANCE NOT RUN

## 1. Preflight
- Re-fetched the Master Continuity Ledger, GCR Master Priority Queue and Continuation 89 specification before selecting work.
- Ledger still records V11.4 BLOCKED / NOT_ADMISSIBLE, V11.3 UNKNOWN / NOT_AUTHORIZED / NOT_RUN, GCR UNKNOWN / BLOCKED.
- Continuation 89 explicitly requires user approval before implementation. No implementation, workflow dispatch, market-data collection or production change was performed.
- Reviewed the exact current repository copies of:
  * docs/V11_4_FORWARD_LABEL_V2_RESEARCH_ONLY_ACCEPTANCE_SPEC_CONTINUATION89_20261120.md (blob SHA c445b4f115a93d75dc9745790c76d7bbd9a0e145)
  * docs/DAILY_HISTORICAL_ROLLING_BACKTEST_PERFORMANCE_ACCEPTANCE_CONTRACT_20261119.md (blob SHA 92c5f46bda07277f5d0529ab24b17aa307b61dba)

## 2. Independent document-level checklist
| Gate | Review result | Evidence in specification |
|---|---|---|
| Source manifest, SHA-256 and publication/vintage provenance | PASS | Sections 2, 6, 9, 10 |
| Exchange-session spine and stable security identity | PASS | Sections 3, 6, 8 |
| Full T+1..T+h maturity; partial rows excluded | PASS | Sections 3, 4, 5, 9 |
| Future-feature, publication-time and revision-vintage leakage | PASS | Sections 4, 6, 8 |
| Independent hand-check against actual archived rows | PASS | Sections 8, 9, 10 |
| Denominator conservation and explicit exclusions | PASS | Sections 5, 6, 7, 8 |
| Exact integer-count parity across JSON/CSV/summary/manifest | PASS | Sections 7, 8, 9 |
| Independent metric recomputation | PASS | Sections 7, 9 |
| H+3 minimum 50 fully matured observations per State | PASS | Sections 8, 9, 11 |
| Runtime under 10 minutes; short isolated jobs | PASS | Sections 8, 9 |
| v1/v2 isolation and shadow-only outputs | PASS | Section 2 |
| Explicit approval boundary and production protection | PASS | Section 11 |

Result: 12/12 document-level checklist items are present. This verifies specification coverage only; it does not prove code, source data, tests, labels, metrics, or workflow execution.

## 3. Cross-check against the existing rolling-backtest acceptance contract
- The v2 specification preserves chronological cutoff discipline, no future/revised-vintage leakage, complete maturity, immutable provenance, per-cutoff denominators, exact reproducibility and bounded jobs.
- It keeps the V11.3 cost-aware replay and GCR scorecards separate; no selector hit rate is represented as executable return or GCR evidence.
- It preserves the user-approved H+3 >=50 fully matured observations per State. Any State below the floor remains UNKNOWN; DATA_CONTAMINATED remains quarantined.
- The existing H+5 JSON/CSV 613-vs-616 mismatch remains an unresolved implementation/data gate. This review does not choose a count or claim it resolved.

## 4. Review decision and remaining blockers
- Document/specification review: PASS (12/12).
- V2 implementation: NOT_AUTHORIZED pending explicit user approval.
- V2 code/tests/row labels/metrics: NOT_RUN.
- H+5 source mismatch: UNRESOLVED.
- V11.4 performance admission: BLOCKED / NOT_ADMISSIBLE.
- V11.3 cost-aware replay: UNKNOWN / NOT_AUTHORIZED / NOT_RUN.
- GCR: UNKNOWN / BLOCKED.
- Production integration: NOT_AUTHORIZED.

## 5. Next exact action
- Await explicit user approval before implementation. If approval is not provided, continue only already-authorized observation work, including H+3/H+5 outcomes once their full market-session windows mature.
- On approval, first reproduce the existing H+5 mismatch and faulty forward-label behavior from immutable artifacts; then implement isolated research-only v2, execute deterministic tests, and archive row-level evidence. Do not touch production selector or score paths.

## 6. Protected invariants
No changes to Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56x12), Engines A–E, IPO-PLX V2, weights, trade gates or production workflows. ₹0, official/free sources only. No synthetic market data, fabricated timestamps, forward-fill, guessed mapping, or unauthorized data collection. UNKNOWN is never PASS.
