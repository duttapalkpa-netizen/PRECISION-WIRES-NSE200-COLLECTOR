# CGA Capex evidence-ledger decision — 2026-11-02

Decision: accept six PIB publication timestamps as dated corroborating evidence for FY2025-26 April–September CGA Capital Expenditure cumulative points. Preserve the distinction between dated release evidence and complete historical vintage proof.

## Ledger treatment
- Add six rows to the research-only dated release crosswalk. Each row records reference month, PIB Release ID, publication time in IST and UTC, reported cumulative Capital Account Expenditure, derived standalone monthly value, current CGA snapshot value, delta, and vintage status.
- Release timestamp belongs to the dated PIB cumulative release observation. The standalone monthly flow is derived by differencing consecutive cumulative releases; it does not have a separately observed publication timestamp.
- The six PIB cumulative values and six derived monthly values match current CGA snapshots exactly (all deltas zero).
- Status: `DATED_RELEASE_CROSSCHECK_PASS`; `INTERMEDIATE_VINTAGES_UNKNOWN`; `SOURCE_LINEAGE_INDEPENDENCE_UNPROVEN`.
- This is a research evidence ledger, not a canonical production source promotion.

## Required fail-closed treatment
1. Do not assign the PIB release timestamp to each underlying daily/monthly raw source observation unless its semantics match the released aggregate.
2. Do not label all six periods FINAL; retain the official provisional/revision caveat from CGA monthly accounts.
3. Do not infer that no intermediate revisions ever occurred. Only the six observed dated release points were compared.
4. Keep `india_government_capex` partial / provisional vintage limitation. No Factor Registry promotion.
5. Hard Gate remains BLOCKED.

## Regression invariants
Production selector unchanged; `RANKING_SCORE` unchanged; `+1 PRESSURE_FADE` unchanged; 56×12 = 672 diagnostics unchanged; UNKNOWN remains neither PASS nor FAIL. Research spend ₹0. No merge or deployment.
