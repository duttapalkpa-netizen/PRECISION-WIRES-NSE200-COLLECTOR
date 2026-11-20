# Run #407 — T20_H5 parser-boundary reconciliation (Part 2)
Date: 2026-11-20

## Status
**ROOT CAUSE IDENTIFIED — historical T20_H5 metric reconciled.** This supersedes the provisional "serialization discrepancy" diagnosis in Part 1. The archived JSON metric is correct; the apparent CSV count of 612 was caused by the default pandas CSV float parser rounding three boundary values upward.

## Provenance
- Repository: `duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR`
- Run #407 / run ID: `44542948987`
- Job ID: `135625864171`
- Source commit: `d013577157bc1f24322cd100aaf60c40a20c4d17`
- Artifact ID: `14539426731`
- Artifact ZIP SHA-256: `b958d9184eb2df4715364b5825d243593c1c9d9d1290a171ae3ab2833950dfd7`
- Prediction CSV SHA-256: `06dc89983aa748bae5e03eee8e3ad4be5bd2add008e5b00dc350e5e65399d843`
- Metrics JSON SHA-256: `9a79719ec8482953044cae38b6ab9329c20849fef64b69dfd85e81c3d3b99061`

## Independent reproduction
The archived prediction CSV was parsed twice:
1. Default `pandas.read_csv`: T20_H5 hits = **612**.
2. `pandas.read_csv(..., float_precision="round_trip")`: T20_H5 hits = **609**.

The three parser-sensitive records are:
- 2026-09-25 / REPRO
- 2026-10-29 / AVANCE
- 2026-10-29 / ANNAPURNA

For each record, the exact round-trip parsed value is `19.999999999999996`, which is strictly less than 20. The default parser rounds it to `20.0`, incorrectly counting it as a winner. The CSV contains sufficient numeric precision; this is a parser-boundary issue, not a stale JSON, missing row, duplicate key, or serializer mismatch.

## 100-cutoff reconciliation
Using round-trip float parsing:
- 3,000 prediction rows
- 100 cutoffs
- exactly 30 rows and 30 unique symbols per cutoff
- zero duplicate (CUT_OFF, SYMBOL) keys
- per-cutoff T20_H5 hit counts sum to **609**
- T20_H5 precision = `609 / 3000 = 0.203 = 20.30%`
- JSON T20_H5 precision = `0.203` — exact agreement
- T5_H1: 648 / 3,000 = 21.60%, JSON agrees
- T10_H3: 1,198 / 3,000 = 39.9333%, JSON agrees

The 100-row cutoff ledger is archived as `docs/RUN407_T20_H5_CUTOFF_RECONCILIATION_20261120.csv`.

Ordered exact `(CUT_OFF, SYMBOL, FUT5_HIGH_PCT)` membership fingerprint (SHA-256):
`0739c79de53573228e369af8e0d77182665d1656bb86d2ee33abc7335a580c65`

Cutoff-ledger CSV SHA-256:
`54ff61432c9165863c52aa12ae9af5d9991a0460a3ae436a4e81b84bc47a4441`

## Corrective control
Any audit/reconciliation consumer that classifies threshold outcomes from this CSV must use:
`pd.read_csv(path, float_precision="round_trip")`
and must assert that the exact ordered membership fingerprint and per-cutoff totals reconcile with the JSON metrics. Do not round the observed outcome column before applying the >=20 threshold. Do not change the backtest production selector or scoring logic for this parser issue.

## Separate live-selection blocker — still open
Run #407 `final_selection_status.json` remains `PROVISIONAL_ONLY_FINAL_SELECTION_BLOCKED`, blocker `LIVE_INTRADAY_1M_FEED_MISSING`. The archived `live_1m_status.json` records NSE quote endpoint HTTP 403, zero live rows, and no observed market-open confirmation. Thus the provisional Top-3 are research candidates only, not actionable recommendations. Do not promote a symbol to reliable/A+ status from this archive alone.

The next stock-selection task is a bounded live-feed source-access and schema validation, using only free official/authorized sources and recording actual timestamps; no fabricated live values. If no verified live feed is available, keep the readiness gate blocked and report the ranked candidates as provisional only.

## Protected invariants
Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E, and IPO-PLX V2 remain unchanged. No synthetic data. UNKNOWN is never PASS.
