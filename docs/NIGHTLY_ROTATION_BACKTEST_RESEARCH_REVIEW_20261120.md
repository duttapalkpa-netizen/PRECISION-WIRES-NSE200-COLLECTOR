# Nightly Rotation Backtest & Research Performance Review — 2026-11-20

**Phase:** Observation only  
**Overall decision:** V11.4 performance claims **BLOCKED / NOT_ADMISSIBLE**; V11.3 cost-aware replay **UNKNOWN / NOT_AUTHORIZED / NOT_RUN**; GCR **UNKNOWN / BLOCKED**.  
**Production impact:** none. Production Selector, `RANKING_SCORE`, `+1 PRESSURE_FADE`, CORE-672 (56×12), Engines A–E and IPO-PLX V2 remain unchanged.

## 1. Progress Log

### Completed
- Re-read the current Master Continuity Ledger (before this review: blob `0636ed7438fb57e9b0bf08f43cb90f78c2b49835`, ending at Continuation 86), the 2026-11-20 morning Unified Top-5 report, the Run #407 bootstrap report and the latest GCR readiness/sector-rights reports.
- Located the latest successful NSE archive run, **Run #416** (`44744602064`, commit `6572a69776272cbda3fde4fec457bddbf7c58ad5`), and independently downloaded/hashed artifact **14632139339**. Its ZIP SHA-256 `b12ea634f24af8241ee9a901635dd743195f4b8a3a1511cc2ffe3c3246282082` matches GitHub's artifact digest.
- Verified the processed archive spans 200 market sessions, 2026-02-16 through 2026-11-20, 2,999 symbols and 503,892 rows; QA JSON is `PASS`, with no duplicate `(DATE,SYMBOL)` keys. The walk-forward step ran from 13:31:06Z to 13:36:04Z (about 4m59s); no new workflow was dispatched.
- Reconciled all raw cutoff rows against `walk_forward_universe_probabilities.csv`: 258,034 raw rows, 252,020 eligible rows, 6,014 excluded rows; all 6,014 exclusions have history depth below 20, and zero rows with history depth ≥20 are missing from the exported universe.
- Independently rebuilt the forward outcome windows from the archived OHLC data using the next 1/3/5 **market sessions**, requiring a symbol row for every session in the horizon. This exposed a P0 label-construction defect in the source code.
- Reviewed the 2026-11-19 shadow cohort against the 2026-11-20 session: 10 selector rows, 7 unique symbol/cutoffs, all 7 have a mature H+1 observation; H+3/H+5 remain immature.

### Blocked / rejected
- Do not accept Run #416 or Run #407 V11.4 precision/recall/lift, subgroup or behavioural-DNA metrics as validated performance. The target labels are not the intended forward windows, and the same faulty labels are used in prior-window training.
- Do not calculate V11.3 net return, win rate, expectancy, costs, profit factor or drawdown. User-approved entry/exit/stop/circuit/position-size/overlap assumptions and an independently reconciled replay are absent; G0 remains blocked.
- Do not assign GCR performance. Timestamp/vintage-aligned macro-to-sector-to-stock outcomes and a defensible sector crosswalk are not established; NSE and BSE sector TRI rights gates remain not admitted.
- No previous dated nightly review report was found in `docs/`; the latest comparable stored evidence was the Run #407 research report, not a nightly report.

### Exact next actions
1. Prepare a research-only forward-label v2 correction and acceptance tests; do not admit it to production or move beyond Observation without approval.
2. Continue the seven-symbol alert cohort only when H+3/H+5 windows are fully mature; do not score immature horizons.
3. Keep V11.3 and GCR at NOT_AUTHORIZED/BLOCKED until their respective execution-approval and official-source/crosswalk gates are satisfied.

## 2. Source and reproducibility record

| Item | Evidence |
|---|---|
| Latest NSE workflow | [Run #416](https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/44744602064), run ID `44744602064`, conclusion `success` |
| Artifact | ID `14632139339`, created `2026-11-20T13:38:39Z`, ZIP SHA-256 `b12ea634f24af8241ee9a901635dd743195f4b8a3a1511cc2ffe3c3246282082` |
| Source commit | `6572a69776272cbda3fde4fec457bddbf7c58ad5` |
| Source file | `pipeline/walk_forward_backtest.py`, Git blob SHA-1 `d085f7a2d35a88b4c4eaba65144a429a06961b09` |
| Processed dataset SHA-256 | `d6810409dbd800e5146e08a1eb1e8b48207354461876acb62cbb2f656fba51db` |
| Top-30 predictions SHA-256 | `8ed2d51044373c300ecc5f64e3103b246217794af849f494d80629c967195256` |
| Eligible-universe export SHA-256 | `ec1361ce5275370ce1eb6fce97ba2cf86d4f7e39fc52b5b29fb435f537b43aec` |
| Source metrics JSON SHA-256 | `7f6fa6895c736798368411ab9963ea4ef2680ad663ef57f770925958d00a8482` |
| Independent audit | ID `V11.4-OBS-LABEL-RECON-20261120-RUN416`; audit script SHA-256 `3a69c353a03d77f871f7bd52b120dd43633bf11228fcc0cdcd4bfc83e03f4a2b`; config SHA-256 `1d17284e1c4a16e59e51a0d117a8b1e9888cfba39bd5378ce1c61dfca1c6d8a8` |
| Corrected-label audit JSON | SHA-256 `f0dd74fb7936038b4503ed4e8579a6af17b9f45de9fbb59226360f660e4726a2` |
| Per-cutoff denominator ledger | SHA-256 `5cbaf23a92bb8a96b1c0d63424fbeeddeb2b02d1ff40a99351d71c820ef99617` |
| Daily alert cohort input | SHA-256 `69c5ecba2d06b9dbe3968f0e1a023bf7b0ff58486d2f580bcaf4735d0c0ae20a` |
| Daily alert outcome CSV | SHA-256 `65d468c7ea8a662c3cb2d131cc5ee4d636e4abf8f3afb0e8aede78c20b9f2858` |
| Daily alert outcome summary | SHA-256 `e8da668872fc4f5942c791e94abfde8ac0ae7a9e9e78d2017f8a5c9699f560bb` |

**Provenance limitation:** Run #416 contains the processed 200-session CSV and derived outputs, but not the original raw NSE source bytes or an immutable raw-file manifest. The hashes above verify the downloaded workflow ZIP, processed file and audit outputs; they do not substitute for missing raw-source provenance.

## 3. Track 1 — V11.4 Historical Behavioural Selector

**Status: BLOCKED / NOT_ADMISSIBLE**

### P0 defect: forward label window is wrong

At source commit `6572a697...`, `future_outcomes()` uses:

```python
x.shift(-1).rolling(h, min_periods=1).max()
```

This is a trailing rolling window over a shifted series, not the required forward window `T+1..T+h`. In source-row terms, the h=3 expression spans approximately `T-1..T+1`; h=5 spans `T-3..T+1`. It also shifts within each symbol, which skips missing market-session rows, while `min_periods=1` accepts partial windows as if they were mature.

The same `FUT3_HIGH_PCT` and `FUT5_HIGH_PCT` labels feed the prior-window training targets `P10_H3` and `P20_H5`, and those probabilities feed the composite `WINNER_PROBABILITY` / `RANKING_SCORE`. Therefore the frozen Top-30 ranking itself is contaminated for all three reported targets, including H+1. The following corrected-label statistics are **post-hoc diagnostics on frozen selections only**, not accepted selector-performance metrics.

### Corrected-label diagnostic — all 100 cutoffs

Method: next 1/3/5 consecutive market sessions from the global archive calendar; all h future symbol rows required; no forward-fill; selector recall denominator is the exported eligible universe. 20,000 cutoff-cluster bootstrap resamples, percentile 95% intervals. The 95% intervals describe cutoff variation, not a repaired model.

| Target | Top-30 mature / immature | TP / FP | Eligible mature / immature | Eligible winners | FN | Precision (= target-hit rate), 95% CI | Recall, 95% CI | F1, 95% CI | FPR, 95% CI | Missed-winner rate, 95% CI |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| +5% H+1 | 2,991 / 9 | 653 / 2,338 | 251,426 / 594 | 22,468 | 21,815 | 21.83% (19.53–24.20) | 2.91% (2.63–3.20) | 5.13% (4.66–5.63) | 1.02% (0.99–1.05) | 97.09% (96.80–97.37) |
| +10% H+3 | 2,975 / 25 | 458 / 2,517 | 250,356 / 1,664 | 16,519 | 16,061 | 15.39% (13.57–17.34) | 2.77% (2.49–3.07) | 4.70% (4.23–5.19) | 1.08% (1.05–1.10) | 97.23% (96.93–97.51) |
| +20% H+5 | 2,966 / 34 | 164 / 2,802 | 249,447 / 2,573 | 5,184 | 5,020 | 5.53% (4.64–6.45) | 3.16% (2.69–3.66) | 4.02% (3.42–4.65) | 1.15% (1.13–1.17) | 96.84% (96.34–97.31) |

`FPR = FP / (FP + TN)`; FP is the matured non-hit count inside Top-30, while FN is the matured winner count missed from the eligible universe. These values must not be promoted as V11.4 performance because the ranking and training labels are affected by the source defect.

### Source-label impact and serialization mismatch

| Target | Source Top-30 hits | Correct forward-window Top-30 hits | Class flips on common mature rows | Source eligible winners | Correct eligible winners |
|---|---:|---:|---:|---:|---:|
| +5% H+1 | 655 | 653 | 0 | 22,535 | 22,468 |
| +10% H+3 | 1,204 | 458 | 1,106 | 9,775 | 16,519 |
| +20% H+5 | 616 | 164 | 651 | 2,061 | 5,184 |

- Correct H+1 maturity is also stricter: source labels mark 2,999 Top-30 rows and 251,843 eligible rows mature; the complete next-market-session rule yields 2,991 and 251,426 respectively. The difference is caused by symbol-only shifting across missing market-session rows.
- `walk_forward_metrics.json` reports H+5 precision `0.204333...`, implying 613 Top-30 hits, while the row-level prediction CSV contains 616 hits. **Three-row mismatch remains unresolved.** H+1 and H+3 source JSON precision agree with row-level source labels.
- The raw `all_by_date` denominator is broader than the selector universe. On Run #416, 6,014 raw cutoff rows are excluded; all have history depth below 20. The exported eligible universe has no unexplained missing row with history depth ≥20. This resolves membership scope, not label validity.

### Fixed reference vs latest rolling window — diagnostic only

The first 80 cutoffs (2026-06-29 to 2026-10-16) are the fixed reference; the latest 20 (2026-10-19 to 2026-11-13) are the rolling window. These windows are part of the same post-hoc corrected-label audit and **not a valid improvement claim** because the frozen ranking was trained on invalid targets.

| Target | Metric | Fixed first 80 (95% CI) | Latest 20 (95% CI) | Latest − baseline |
|---|---|---:|---:|---:|
| +5% H+1 | Precision | 19.90% (17.68–22.16) | 29.55% (23.54–36.50) | +9.65 pp |
|  | Recall | 2.98% (2.68–3.30) | 2.73% (2.23–3.41) | −0.25 pp |
|  | F1 | 5.18% (4.67–5.73) | 4.99% (4.12–6.19) | −0.19 pp |
| +10% H+3 | Precision | 14.05% (12.21–15.93) | 20.74% (15.91–25.96) | +6.68 pp |
|  | Recall | 2.81% (2.48–3.13) | 2.67% (2.12–3.36) | −0.15 pp |
|  | F1 | 4.69% (4.13–5.22) | 4.73% (3.80–5.87) | +0.04 pp |
| +20% H+5 | Precision | 5.10% (4.18–6.03) | 7.24% (4.89–9.73) | +2.14 pp |
|  | Recall | 3.04% (2.51–3.59) | 3.57% (2.57–4.68) | +0.53 pp |
|  | F1 | 3.81% (3.14–4.48) | 4.79% (3.42–6.22) | +0.98 pp |

Sample sizes (fixed → latest): H+1 Top-30 mature `2,392 → 599`, eligible mature `197,963 → 53,463`, eligible winners `15,975 → 6,493`; H+3 `2,377 → 598`, `197,167 → 53,189`, `11,870 → 4,649`; H+5 `2,372 → 594`, `196,485 → 52,962`, `3,981 → 1,203`.

### H+3 state maturity floor

Correct-window matured observations in the exported universe exceed 50 for nine of the ten current states. `DATA_CONTAMINATED` has only 24 matured rows and remains **UNKNOWN** under the mandatory 50-observation floor. No state is calibrated or admitted because the state assignment/probability path is affected by the faulty labels.

## 4. Today's alert cohort — matured outcome review

Morning report `docs/DAILY_UNIFIED_TOP5_SWING_WATCHLIST_20261120.md` (blob `eaf527f31aa39bc202ce966410c5602709718108`) records **0 qualified alert candidates**. Its 10 shadow-selector rows represent 7 unique symbols, all outside the frozen production Top-30. The cohort is a research-only shadow list, not an official Top-5 alert or buy instruction. The source prospective tracker is Run #338 (`44599244783`), artifact `14567098741`, ZIP SHA-256 `d500b8c42e10bde7640d177243aae2c305e4bf21eea3d7bc85cc7ffea71085c3`; the frozen watchlist ledger blob is `5c623925e553b69771c30b877789e153b52d3d26`.

Run #416 provides the 2026-11-20 session. All 7 unique symbol/cutoffs have a complete H+1 row. Scenario hits use the 2026-11-20 high against the 2026-11-19 close; adverse excursion uses the 2026-11-20 low against that close.

| Symbol | H+1 high return | H+1 adverse excursion | H+1 close return | +2% | +5% | +10% | +20% |
|---|---:|---:|---:|---|---|---|---|
| ARYAMAN | +0.80% | −0.28% | +0.18% | Miss | Miss | Miss | Miss |
| ELITECON | +4.88% | −4.88% | +4.65% | Hit | Miss | Miss | Miss |
| HINDOILEXP | +3.14% | −0.64% | +1.08% | Hit | Miss | Miss | Miss |
| KDDL | +1.50% | −2.00% | −1.26% | Miss | Miss | Miss | Miss |
| LEENEE | +2.91% | −3.05% | +1.11% | Hit | Miss | Miss | Miss |
| NRL | +0.57% | −4.21% | −1.89% | Miss | Miss | Miss | Miss |
| YATRA | +3.94% | −2.17% | −1.03% | Hit | Miss | Miss | Miss |

- H+1: **7/7 matured**; +2% hit `4/7`, miss `3/7`; +5%, +10% and +20% each `0/7` hit, `7/7` miss.
- H+3 and H+5: **7/7 immature**; no scoring before their full future windows exist.
- H+1 adverse excursion median `−2.17%`, range `−4.88%` to `−0.28%`.
- Base session date `2026-11-19`; outcome session date `2026-11-20`. The processed daily rows expose session dates, not per-row intraday timestamps. Run #416 artifact creation time is `2026-11-20T13:38:39Z`; it is an artifact timestamp, not a trade-time timestamp.
- This is a 7-symbol descriptive cohort, not a random sample or executable replay; no confidence interval or net-return claim is assigned.

## 5. Track 2 — V11.3 Cost-aware Trade Replay

**Status: UNKNOWN / NOT_AUTHORIZED / NOT_RUN**

No user-approved entry/exit, stop, circuit-lock, position sizing or overlap assumptions were evidenced, and no independently reconciled trade ledger was attached. The 0.22% convention in the existing draft contract is not treated as user approval. Net return, win rate, expectancy, transaction costs, profit factor and drawdown are therefore **not calculated**.

## 6. Track 3 — Global Capital Rotation (GCR)

**Status: UNKNOWN / BLOCKED**

No synchronized timestamp/vintage-aligned macro → sector → stock panel with matured outcomes is admitted. The current GCR readiness audit remains 0 full execution PASS across 10 checks (9 PARTIAL, 1 BLOCKED). The 2026-11-20 NSE and BSE sector TRI rights gates do not admit those historical TRI series to the GCR database/derived sector-transmission panel; exact sector crosswalk and matched-vintage joins remain incomplete. V11.4 or V11.3 metrics are not attributed to GCR.

## 7. Change vs prior evidence and open gaps

- No prior nightly report exists in `docs/`, so no prior-night percentage-point improvement is claimed.
- The morning alert's earlier prospective artifact lacked row-level outcomes; Run #416 now supplies the 2026-11-20 OHLC session, enabling the seven-symbol H+1 review above.
- The Run #407 bootstrap report `docs/RUN407_CUTOFF_CLUSTERED_BOOTSTRAP_AND_WINNER_DRIVER_ATTRIBUTION_20261120.md` (blob `23b144304efd8ed3c3aac63105fc4b7aae8f3b5a`) is superseded for performance interpretation: Run #407 artifact `14539426731` (ZIP SHA-256 `b958d9184eb2df4715364b5825d243593c1c9d9d1290a171ae3ab2833950dfd7`) and Run #416 use the same source blob SHA `d085f7a2...`, so the forward-label defect applies to Run #407 too. Its H+3/H+5 metrics and subgroup conclusions must not be used as validated evidence; H+1 ranking evidence is also contaminated by the composite training path.
- Proven gaps: faulty forward-window labels; symbol-only shifting across missing market sessions; partial windows accepted as mature; H+5 metrics JSON vs row-level CSV mismatch (3 hits); missing original raw-file manifest/raw bytes in Run #416 artifact; unapproved V11.3 G0 assumptions; GCR source-rights and exact sector mapping gaps.

## 8. Next highest-value research actions

| Priority | Exact action | Acceptance test | Expected artifact | Blocker |
|---|---|---|---|---|
| P0 | Prepare a research-only forward-label v2 correction; keep it outside production | For every cutoff, label `T+1..T+h` only; require all h market-session rows; verify against independently hand-checked real archive rows; no future feature enters T; source/eligible/Top-30 denominators reconcile; H+5 JSON and CSV counts agree; job <10 minutes | Versioned label-v2 code, tests, row-level prediction CSV, per-cutoff denominator ledger, manifest and report | Moving beyond Observation / implementation requires user approval; production admission is not authorized |
| P1 | Continue the seven-symbol 2026-11-19 cohort's H+3/H+5 outcome tracking | Only mature after 3/5 complete next market sessions; report symbol/cutoff, high/low/close, 2/5/10/20 hits, adverse excursion, source dates, immature/excluded counts | Updated dated daily outcome CSV + SHA-256 manifest | Future sessions have not yet matured |
| P2 | Keep V11.3 and GCR scorecards closed until their own gates are satisfied | V11.3: approved G0 execution assumptions + reconciled replay; GCR: explicit official reuse rights, exact sector mapping and synchronized vintages | Separate V11.3 replay evidence or GCR source/join admission report | User approval and/or official free-use source evidence absent |

### Additional methodology only from proven gaps
1. Forward-looking horizon label function with complete-market-session maturity guard.
2. Row-level serialization consistency gate between metrics JSON and prediction CSV.
3. Immutable raw-source manifest and retrieval provenance for the processed NSE archive.
4. Explicit user-approved V11.3 execution assumptions before any net replay.
5. Official rights + exact sector/stock crosswalk before any GCR transmission study.

## 9. Audit decision

- V11.4: **BLOCKED / NOT_ADMISSIBLE** for performance claims pending label-v2 repair and a fresh leakage-safe shadow walk-forward.
- V11.3: **UNKNOWN / NOT_AUTHORIZED / NOT_RUN**.
- GCR: **UNKNOWN / BLOCKED**.
- Daily shadow cohort: H+1 descriptive review complete; H+3/H+5 immature.
- No new NSE data collection, no workflow dispatch, no paid API, no synthetic data, no forward-fill, no guessed mapping, no fabricated timestamp, and no production change in this review.
