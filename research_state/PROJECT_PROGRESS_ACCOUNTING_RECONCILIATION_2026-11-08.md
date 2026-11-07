# PRECISION-WIRES V11.3 — Project progress accounting reconciliation
Date: 2026-11-08
Branch: fix/iip-41-vintage-audit-clean
Status: WORKSTREAM EVIDENCE RECONCILED; GLOBAL PERCENTAGE NOT YET DEFENSIBLY CALCULABLE

## Why the displayed 36% appeared unchanged
- The prior Continuation 20 progress policy explicitly said: "Do not invent an overall percentage. Last remembered overall baseline was 36%; no complete denominator/reconciliation has yet re-certified it."
- Subsequent assistant summaries repeated 36% as if it were a current live metric. That was a reporting error: it is only a historical baseline, not a recalculated current project percentage.
- Recent work did advance materially. The official April/May 2026 IIP API extraction and 43/43 latest-PIB comparisons had already been completed in Run 42381121341 (#12), but the newer Continuation 21 checkpoint did not carry that evidence forward and then repeated a smaller 37-row PIB transcription. This omission made progress appear frozen.
- Corrective rule: show 36% only as "last historical baseline, not current"; do not claim the project is still exactly 36% and do not fabricate a replacement percentage until the full master denominator is reconstructed.

## Reconciled workstream scorecard
| Workstream / task | Evidence-backed progress | Current status | Scope limitation |
|---|---:|---|---|
| April 2026 official MoSPI API contract | 100% | PASS | OpenAPI schema recovered; official API contract only |
| April 2026 API extraction | 100% (43/43 rows) | PASS | JSON API, not native XLSX |
| April 2026 API vs latest PIB PRID 2329475 | 100% (43/43) | PASS | Index values rounded to one decimal; growth rates not recomputed |
| May 2026 API vs latest PIB PRID 2329475 | 100% (43/43) | PASS | Same limitation |
| April+May API comparison | 100% (86/86) | PASS | Does not certify full historical vintage panel |
| PPI series identity | 100% at series level | CORROBORATED | API row schema has no explicit deflator field |
| April native catalogue XLSX | 0% | NOT RECOVERED | API is not XLSX |
| 41-month XLSX ingestion | 39/41 = 95.1% | PARTIAL | Ingestion ratio only, not audit completion |
| Full IIP vintage/revision audit | Not measurable as one % | BLOCKED_WITH_GAPS | 693 transitions, 431 unresolved; source-cell maturity gates remain |
| Existing revision batches 001–005 | 54 structural rows validated | PASS_WITH_HASH_DRIFT_QUARANTINED | Structure/arithmetic validation only; source workbook re-certification not implied |
| September 2026 IIP transcription/structure QA | 100% within bounded QA | PASS | Raw PIB PDF binary hash not acquired |
| Next-Day Radar one-off artifact | 100% within bounded run | PASS | One-off output only |
| Next-Day Radar daily automation | 0% | NOT ENABLED | No main-branch merge/automation approval |
| CORE-672 full live implementation | Not measurable from available evidence | NOT COMPLETE | README explicitly says all 672 diagnostics are not claimed live |
| IPO-PLX V2.0 | Foundation only; no global % | PARTIAL | Subscription/GMP/effective float/queue/catalyst inputs remain UNKNOWN |
| Global Macro/Geo + factor registry + event study | Not measurable from reconciled evidence | OPEN | Prior evidence had P0 7/8 and 0/35 factor groups; must be refreshed before scoring |

## What the percentages mean
- 43/43 and 86/86 are exact bounded API-to-PIB comparison ratios, not project completion.
- 39/41 = 95.1% is the monthly workbook ingestion ratio, not vintage audit or research completion.
- 54 rows are structural validation in batches 001–005; they are not 54 source-cell certifications.
- A task-specific 100% means only that the stated bounded task met its own acceptance criteria.

## Global progress denominator — missing before a new overall %
The complete project-level denominator has not been reconstructed in one immutable master acceptance register. It must enumerate and weight at least:
1. 56 steps × 12 filters (672 diagnostics), each with source, implementation, tests and matured validation criteria.
2. All five engines A/B/C/D/E, production selector and ranking invariants.
3. NSE historical data, Security Master, adaptive history and data QA.
4. Macro/Geo source groups and 35 factor groups with freshness/coverage.
5. IIP, corporate results, announcements, FII/DII, bulk deals, shareholding and event/catalyst evidence.
6. Backtest/walk-forward sample maturity, transaction costs, false positives, precision/recall and stress-regime tests.
7. IPO-PLX source/label coverage and winner/loser separation.
8. Risk Modifier, live ignition, monitoring, Radar and approved automation.
9. Step-6 same-snapshot reconciliation, artifact hashes, provenance and final Hard Gate.
10. Final research paper and acceptance criteria.

A defensible overall percentage requires a frozen denominator, per-item weights, binary/evidence-backed status definitions, dependency rules (blocked tasks cannot be counted as passed), and a snapshot date. None is currently present as one reconciled canonical register. Therefore a new global percentage would be fabricated.

## Reporting correction
- Historical overall baseline: 36% (last remembered; not current/re-certified).
- Current overall completion: NOT CALCULABLE from reconciled evidence yet.
- This is not a statement that work has not progressed. It means the previous single number was not being updated from a stable denominator.
- Next high-value task: build and reconcile the canonical master acceptance register from repository artifacts and the user's previously established final acceptance criteria; then calculate the first defensible updated overall percentage.
- Do not alter any production logic to make progress numbers look better.

## Immutable constraints
Production selector, RANKING_SCORE, +1 PRESSURE_FADE and CORE-672 remain unchanged. UNKNOWN is neither PASS nor FAIL. No synthetic rows, fabricated timestamps, unsupported source promotion or Hard Gate relaxation. Research spend ₹0.
