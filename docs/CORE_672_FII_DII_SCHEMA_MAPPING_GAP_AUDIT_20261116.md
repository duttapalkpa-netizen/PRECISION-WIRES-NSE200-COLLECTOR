# CORE-672 FII/DII Schema-Mapping Gap Audit

Date: 2026-11-16
Scope: research-only static audit of the committed NSE FII/DII collector, CORE-672 diagnostics, and Risk Modifier. No production behavior was changed.

## Executive finding

FII/DII input is not wired to CORE-672's expected field names. The collector emits one row per category with `group`, `date`, `buy_value`, `sell_value`, and `net_value`. `pipeline/diagnostics_672.py` instead reads `fii_net` and `dii_net` from every row. On the retained Run #161 payload shape and the Library CSV shape, those keys are absent. Consequently the diagnostic's FII/DII inputs resolve to NaN and the `FII_DII_SMART_MONEY` branch evaluates to its neutral base score of 50, which `state()` classifies as UNKNOWN (thresholds: POSITIVE >=60, NEGATIVE <=40).

## Exact source evidence

### 1. Collector schema

File: `collector/context_data.py`, blob `f38e17979774d1439eea79e4dc7728ba92a790d1`.

- Lines 34-51 normalize API categories to `FII_FPI` or `DII`.
- Each output row contains `category`, `group`, `date`, `buy_value`, `sell_value`, `net_value`.
- Source label is `NSE /api/fiidiiTradeReact (category-normalized)`.
- Coverage metadata counts FII and DII rows and distinct dates separately.

### 2. CORE-672 consumer mismatch

File: `pipeline/diagnostics_672.py`, blob `af0a8ddc17d72024509167533585713600a4b845`.

- Lines 20-21 compute means from `x['fii_net']` and `x['dii_net']`.
- Lines 32-33 use those values in `FII_DII_SMART_MONEY`.
- Since collector rows do not contain either field, both comprehensions exclude all rows. With a non-empty `fii_dii` list, NumPy receives empty value lists and produces NaN (and may emit an empty-slice warning).
- The expression at line 33 substitutes zero contribution for NaN, resulting in score 50; `state(50)` is neither POSITIVE nor NEGATIVE and therefore returns UNKNOWN.
- The diagnostic does not distinguish NSE-only from combined NSE+BSE+MSEI scope, and it does not validate observation date, freshness, duplicate categories, or provisional status before using a value.

### 3. Risk Modifier is not an approved mapping substitute

File: `pipeline/risk_modifier.py`, blob `4115a1247992ef8a075b2fd247efb9ce8f8663f6`.

- Lines 23-24 separately select `net_value` by `group` and sum the first 20 entries (or fewer if less than 20 exist).
- Lines 37-40 derive FII and DII states from those sums; UNKNOWN is retained if a sum is NaN.
- The code shown does not sort rows by date, enforce 20 distinct matured sessions, require a fixed exchange scope, or establish that fewer than 20 rows are sufficient for a 20-day metric.
- Therefore this is a separate Risk Modifier calculation and must not be borrowed as CORE-672's missing field mapping or as an approved historical aggregation policy.

## Evidence from retained data

- Library NSE-only and combined CSVs each contain two category rows for 13-Nov-2026.
- All four arithmetic checks `BUY - SELL = NET` passed in the separate CSV QA ledger entry.
- Combined CSV values match retained collector Run #161 API artifact values for the same date; NSE-only values differ, confirming scope distinction.
- Raw Library CSV SHA-256 values are recorded in the preceding continuity ledger entry. Original download URL and download timestamp remain NOT_VERIFIED.
- One date is not sufficient to establish a 20-session history or any rolling behavioral signal.

## Mapping contract — proposed gates, not production authorization

Before any mapping is implemented, a research contract must explicitly specify:

1. **Scope key:** `NSE_ONLY` versus `NSE_BSE_MSEI_COMBINED`; never blend or substitute the two.
2. **Category key:** normalized `FII_FPI` and `DII`; do not depend on row order.
3. **Observation identity:** parse and validate the actual observation date separately from file generation/capture time.
4. **Uniqueness:** at most one valid row per `(scope, date, category)`; duplicates or conflicts remain UNKNOWN until reconciled.
5. **Value semantics:** use `net_value` only after validating `buy_value - sell_value = net_value` within the documented two-decimal ₹ crore precision.
6. **Freshness and maturity:** define acceptable publication delay, provisional-data treatment, correction/revision handling, and the minimum number of distinct matured sessions for any rolling feature.
7. **Missingness:** missing category, stale data, mixed scopes, unparseable dates, or insufficient matured sessions must remain UNKNOWN; never silently coerce to zero.
8. **Consumer separation:** define CORE-672's signal formula independently from Risk Modifier's first-20-row sum. Do not reuse that sum without a separately approved specification.

## Recommended next step

Create a research-only mapping specification and deterministic contract tests using the retained, hash-identified Run #161 / Library data. Tests should prove the present schema mismatch and enforce scope/date/category/uniqueness/arithmetic/missingness rules. Do not alter `collector/context_data.py`, `pipeline/diagnostics_672.py`, `pipeline/risk_modifier.py`, Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672's 56×12 structure, or Engines A-E until the specification is explicitly approved.

## Status

- Collector schema inspection: PASS.
- CORE-672 consumer field inspection: PASS.
- Risk Modifier boundary inspection: PASS.
- Current field compatibility: FAIL (schema mismatch confirmed).
- Production mapping change: NOT_AUTHORIZED / NOT_DONE.
- Rolling 20-session FII/DII evidence: NOT_AVAILABLE.
- Official CSV URL provenance: NOT_VERIFIED.
- Live NSE capture: NOT_RUN.
- Profitability implication: NONE; this audit makes no performance claim.