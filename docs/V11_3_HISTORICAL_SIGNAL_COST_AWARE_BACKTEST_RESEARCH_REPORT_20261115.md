# PRECISION-WIRES V11.3 — Historical Signal & Cost-Aware Backtest Research Report
**Report date:** 2026-11-15  
**Scope:** Research-only V11.3 historical signal adapter, 1–5 session OHLC replay, independent execution reconciliation, full scored-universe selection-quality audit.  
**Decision:** Research package complete; **profitability gate BLOCKED**; not approved for live trading or production integration.

## Executive summary

A cutoff-safe, research-only V11.3 signal adapter was built and executed against a processed NSE dataset rebuilt directly from the previously verified 200-session raw archive. The rebuilt dataset exactly matches the raw archive's 200-session calendar. The adapter produced 5,880 top-30 signals across 196 cutoffs from 484,985 scored cutoff-symbol observations. The cost-aware replay produced 17,640 trade rows. An independent row-level audit passed with zero blockers, zero execution reconciliation errors, zero net-return arithmetic errors, and zero exclusion-policy errors. A separate full-universe audit recomputed precision, recall, false-positive rate, false-discovery rate, missed winners, drawdown proxy, and cost sensitivity.

The ranking shows positive selection lift of approximately 1.59–1.68× over the scored-universe base rate, but recall is only about 1.9–2.0%, false-discovery rate is 87–97%, and mean net returns are negative at all three target horizons—even with zero assumed transaction cost. Therefore, this version is **not profitable under the tested execution convention** and must not be promoted to production or used as a live-trading trigger.

This is a scoped research report, not the final system-wide PRECISION-WIRES acceptance paper. Macro-Geo Step 4 / Factor Registry and CORE-672 semantic acceptance remain separate project gates.

## 1. Data provenance and acceptance

### 1.1 Source archive

- Source repository: `duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR`
- Verified raw-archive workflow Run ID: `43734398604`
- Raw archive artifact ID: `14170166475`
- Raw archive artifact SHA-256: `3c15ceb5cd6cb3270515090eb8393d22f8ca609a6032d0d7e128c5b78fb57494`
- Raw manifest: PASS; 200 raw files; 200 listed sessions; no blockers.
- Session range: **2026-01-21 to 2026-11-13**.

### 1.2 Processed dataset rebuilt from raw archive

The historical replay workflow downloads the verified raw archive and rebuilds the processed dataset in the same run. It does not reuse the earlier processed artifact from Run #146.

- Processed rows: **500,733**
- Unique symbols: **2,997**
- Unique sessions: **200**
- Delivery quantity coverage: **100%**
- Delivery percentage coverage: **100%**
- QA report: PASS; no issues; final-selection data readiness true.
- Processed dataset SHA-256: `8c433c8163dd5a52faf02ffe29e77571043c5791716c65d8c04cfca98ee857b1`.

An earlier processed artifact (Run #146) had a different 200-date set from the verified raw archive. It was rejected for this replay. The final workflow now enforces exact equality between raw `sessions.txt` and processed `DATE` values before signal generation. The final Run #16 passed this gate.

## 2. Historical signal methodology

### 2.1 Research-only adapter

File: `pipeline/v11_3_historical_signals_research.py`

The adapter reproduces the V11.3 A/B/C/D/E feature and score structure for each historical cutoff using information available on or before that cutoff. It does not call or modify the production selector, `RANKING_SCORE`, `+1 PRESSURE_FADE`, CORE-672, or production workflow logic.

- Adaptive RET20 lookback matches V11.3's `min(20, history_depth - 1)` behavior.
- State calibration uses the H+3 label: HIGH excursion of at least 10% from cutoff CLOSE over the next three consecutive global sessions.
- A calibration observation becomes eligible only after its full three-session outcome window has matured.
- Minimum calibration sample: 100 prior matured observations per state (research-only conservative threshold).
- Below-threshold calibration remains UNKNOWN; no numeric score is assigned.
- Maximum 30 candidates selected per cutoff.

### 2.2 Signal output

- Scored universe: **484,985 cutoff-symbol rows**.
- Selected signals: **5,880**.
- Cutoffs with signals: **196**.
- Selected signals per cutoff: up to 30.
- Signal ledger SHA-256: `0e57446e98c372fb832bcfa5a4957791142e88a8f10bacc04e3dc61a945a0df3`.
- Full calibration audit SHA-256: `8ac7fd3f1c1f7727778603f64d52c89261085ded03c55775f5b8a3356d7af435`.
- Regression tests: **4/4 PASS**, including matured-window cutoff, minimum-sample UNKNOWN, no matured data UNKNOWN, and adaptive RET20 semantics.

## 3. Cost-aware execution model

The isolated replay module is `pipeline/v11_3_cost_aware_backtest.py`.

| Parameter | Convention |
|---|---|
| Entry | Next global trading session OPEN |
| Targets | +5% / H+1, +10% / H+3, +20% / H+5 |
| Stop | -3% from entry |
| Target detection | Intraday HIGH touch |
| Same-bar target/stop ambiguity | Stop first (conservative) |
| Stop gap | Fill at observed OPEN |
| No target/stop | Horizon final-session CLOSE |
| Base round-trip cost | 0.22 percentage points, deducted once |
| Slippage / market impact | Not modelled |

The replay created **17,640** trade rows: **17,023 executable** and **617 excluded**. Exclusions were fail-closed for missing symbol sessions or unmatured horizons.

## 4. Cost-aware backtest results

All returns are percentage points. Base cost is 0.22 percentage points per completed round trip.

| Target / horizon | Executable | Target exits | Target-exit rate | Mean net return | Median net return | Profitable trade rate |
|---|---:|---:|---:|---:|---:|---:|
| +5% / H+1 | 5,802 | 747 | 12.87% | **-0.813%** | -1.669% | 32.09% |
| +10% / H+3 | 5,676 | 513 | 9.04% | **-0.877%** | -3.220% | 26.25% |
| +20% / H+5 | 5,545 | 157 | 2.83% | **-0.926%** | -3.220% | 22.67% |

### 4.1 Cost sensitivity

Mean net return under alternative round-trip cost assumptions:

| Target / horizon | 0.00% cost | 0.22% cost | 0.44% cost |
|---|---:|---:|---:|
| +5% / H+1 | -0.593% | -0.813% | -1.033% |
| +10% / H+3 | -0.657% | -0.877% | -1.097% |
| +20% / H+5 | -0.706% | -0.926% | -1.146% |

Mean net returns are negative even at zero assumed transaction cost. The negative result is therefore not explained by the 0.22% cost assumption alone.

## 5. Full scored-universe selection quality

The denominator is the full scored research universe (AVAILABLE calibration and non-null research score), restricted to rows with a complete, executable next-global-session OHLC window. A winner is a trade that reaches the target before the stop under the same stop-first replay convention.

| Target / horizon | Universe winners | Selected winners (TP) | Precision | Recall | Base winner rate | Lift | False-positive rate | False-discovery rate | Missed winners |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| +5% / H+1 | 36,975 | 747 | 12.87% | 2.02% | 7.69% | 1.68× | 1.14% | 87.13% | 36,228 |
| +10% / H+3 | 26,830 | 513 | 9.04% | 1.91% | 5.67% | 1.60× | 1.16% | 90.96% | 26,317 |
| +20% / H+5 | 8,289 | 157 | 2.83% | 1.89% | 1.78% | 1.59× | 1.18% | 97.17% | 8,132 |

The selection has measurable ranking lift, but it captures only a small fraction of all executable winners and most selected trades do not reach the target before the stop. A low conventional false-positive rate is a consequence of selecting only a small fraction of the scored universe; the false-discovery rate among selected trades is the more decision-relevant measure here.

### 5.1 Drawdown proxy

A non-overlapping cutoff-cohort proxy was calculated by spacing cohorts at horizon + 1 sessions and compounding each cohort's equal-weight average net return:

| Target / horizon | Cohorts | Mean cohort net return | Proxy max drawdown |
|---|---:|---:|---:|
| +5% / H+1 | 98 | -0.886% | -57.78% |
| +10% / H+3 | 49 | -0.854% | -34.56% |
| +20% / H+5 | 32 | -0.963% | -25.70% |

**Important:** this is not a fully capital-constrained overlapping-position portfolio backtest. It is a non-overlapping cohort-equity proxy and must not be presented as production portfolio drawdown.

## 6. Independent validation and reproducibility

### 6.1 Execution reconciliation

Independent audit script: `scripts/research/audit_v11_3_cost_aware_replay.py`.

- Audit status: **PASS**
- Blockers: **0**
- Trade rows: 17,640
- Executable: 17,023
- Excluded: 617
- Execution reconciliation errors: 0
- Net arithmetic errors: 0
- Exclusion policy errors: 0
- Duplicate trade keys: 0
- Entry, exit, stop/target ordering, costs, net returns, and output hashes were independently reconciled.

### 6.2 Full-universe selection audit

Script: `scripts/research/analyze_v11_3_selection_quality.py`.

- Audit workflow Run ID: `43738744068`
- Artifact ID: `14171208561`
- Artifact SHA-256: `253295eedd33d6e01df880d2f38e3f0e4be38d7153b31207b58d5c7cc2ddb9aa`
- Audit status: PASS; blockers: 0.
- Selection-quality JSON SHA-256: `79ef94ebcc14c5c465354270c9ab7a71cfa6c99f32102243c886cbe33cf00971`.

### 6.3 Primary replay evidence

- Final replay workflow Run ID: `43738312823`
- Artifact ID: `14171590981`
- Artifact SHA-256: `c57469193b0f0fb6019202409b819118388a25897f0b698463f25a4e359a1360`
- Processed input SHA-256: `8c433c8163dd5a52faf02ffe29e77571043c5791716c65d8c04cfca98ee857b1`
- Trade ledger SHA-256: `05773a572055f7018220ceaf8581cde95bac83b64bb8c6d0005d268563c23670`
- Metrics JSON SHA-256: `3b813a5b6b825dc4a20c75a46d3e4c468a45bd865500d2c3f6b4bc409e4a7daf`
- Independent audit JSON SHA-256: `56a00314ab0417fd6b4548dc828319dbc92babbdc60a408d5f793cb072f9cf51`.

## 7. Interpretation and limitations

1. **Not profitable:** mean net returns are negative for all targets, including the zero-cost sensitivity case.
2. **Low recall:** the Top-30 selector misses 97.98–98.11% of scored-universe winners.
3. **High false-discovery rate:** 87.13–97.17% of selected executable trades fail to reach the relevant target before stop.
4. **Calibration/execution label mismatch:** calibration uses H+3 HIGH excursion from cutoff CLOSE; replay targets are measured from next-session OPEN. This follows the existing V11.3 behavioural calibration convention but should be tested against an execution-aligned, matured label in a future research-only experiment.
5. **Daily OHLC limitation:** intraday sequence is unknown; stop-first is a conservative assumption, not observed tick-level execution.
6. **Cost model limitation:** 0.22 percentage points is an assumed round-trip deduction; actual broker charges, taxes, spread, slippage, market impact, and price-band/circuit execution are not fully modelled.
7. **Scope limitation:** this adapter does not execute the full production selector, live 1% gate, risk modifier, research-house consensus, global macro overlay, all 672 diagnostics, or every production A–E operating gate.
8. **Sample limitation:** 200 sessions are not enough to establish robust long-regime performance; a separate untouched holdout and additional rolling periods are required.

## 8. Acceptance decision and next work

| Gate | Status | Progress |
|---|---|---:|
| Verified 200-session raw-to-processed date lineage | PASS | 100% |
| Cutoff-safe V11.3 research signal generation | PASS (research-only) | 100% |
| Cost-aware H+1/H+3/H+5 replay | EXECUTED | 100% |
| Independent row-level execution audit | PASS | 100% |
| Full-universe precision/recall/missed-winner audit | PASS | 100% |
| Profitability acceptance | BLOCKED (negative net expectancy) | 0% |
| Full production-selector equivalence | NOT ESTABLISHED | 0% |
| Project-wide Final Research Paper / release acceptance | BLOCKED by other P0 gates | 0% |

### Required next research actions

1. Do not deploy this selector or treat it as a buy signal.
2. Investigate why a -3% stop produces negative expectancy even before costs; test a predeclared, bounded set of entry/stop/exit variants without changing production logic.
3. Align calibration labels to the actual next-session OPEN execution basis and preserve the matured-outcome cutoff rule.
4. Improve recall and reduce false discovery with an explicitly measured anti-miss path; report precision/recall trade-offs rather than optimizing hit rate alone.
5. Repeat the rolling evaluation on an untouched later period before any production acceptance.
6. Separately close Macro-Geo Step 4 / Factor Registry, CORE-672 semantic evidence, and remaining system-wide acceptance gates before issuing the final project-wide paper.

## 9. Governance

- Research spend: ₹0.
- No paid APIs or synthetic data.
- Production Selector, `RANKING_SCORE`, `+1 PRESSURE_FADE`, CORE-672, and production workflows were not changed.
- No production integration or trade automation is authorized.
- PR #37 remains Draft/Open/Unmerged; no merge was performed.

**Final conclusion:** The historical signal, replay, and independent validation work package is complete and reproducible. The evidence does not support a profitable strategy at this stage. The correct outcome is to retain the research artifact, mark profitability BLOCKED, and continue with a targeted anti-miss/entry-exit improvement study—not to promote the current engine.
