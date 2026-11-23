# PRECISION-WIRES V11.3 — Nightly Rotation Backtest & Research Performance Review
**Review date:** 23-Nov-2026 (Asia/Kolkata)  
**Morning alert cutoff:** 20-Nov-2026 EOD  
**Phase:** Observation only — no production admission, selector/ranking/code change

## 1. Ultimate 2% / 5% / 10% / 15% / 20% Stock-Capture Alert

**Important status:** all rolling historical rows below are post-hoc, exact-session diagnostics on the frozen Top-30 ranking and are **NOT VALIDATED**. The source code trained probabilities with defective H+3/H+5 labels; the date spine also contains 12 holiday duplicates. These figures are not verified performance, not profitable returns and not executable trade wins.

### Historical frozen-ranking diagnostic — 96 valid cutoffs
Original export: 100 cutoffs / 3,000 Top-30 rows. Four holiday cutoffs were removed (14-Sep, 02-Oct, 20-Oct and 10-Nov); 12 holiday-labelled duplicate dates were removed from the session spine. Remaining cutoff period: 30-Jun–16-Nov-2026. Unique-symbol counts deduplicate repeated symbols across cutoffs; signal rows do not.

| Target / horizon | Eligible unique symbols | Universe unique high-touch winners | Captured unique winners | Missed unique winners | Capture = captured / eligible | Eligible signal rows / selected matured rows |
|---|---:|---:|---:|---:|---:|---:|
| +2% / H+1 | 2,899 | 2,871 | 851 | 2,020 | 29.35% | 241,146 / 2,871 |
| +5% / H+1 | 2,899 | 2,587 | 386 | 2,201 | 13.31% | 241,146 / 2,871 |
| +10% / H+3 | 2,883 | 2,254 | 273 | 1,981 | 9.47% | 240,092 / 2,856 |
| +15% / H+5 | 2,880 | 1,797 | 204 | 1,593 | 7.08% | 239,218 / 2,848 |
| +20% / H+5 | 2,880 | 1,193 | 102 | 1,091 | 3.54% | 239,218 / 2,848 |

| Target / horizon | TP / FP / FN / TN (signal rows) | Precision (95% CI) | Recall (95% CI) | F1 (95% CI) | Universe signal-row hit rate (95% CI) | Status |
|---|---:|---:|---:|---:|---:|---|
| +2% / H+1 | 1,804 / 1,067 / 93,883 / 144,392 | 62.84% (60.31–65.26) | 1.89% (1.80–1.99) | 3.66% (3.50–3.86) | 39.68% (37.11–42.22) | NOT VALIDATED |
| +5% / H+1 | 584 / 2,287 / 20,883 / 217,392 | 20.34% (18.38–22.22) | 2.72% (2.50–2.94) | 4.80% (4.43–5.18) | 8.90% (8.14–9.68) | NOT VALIDATED |
| +10% / H+3 | 436 / 2,420 / 15,940 / 221,296 | 15.27% (13.45–17.13) | 2.66% (2.39–2.94) | 4.53% (4.08–4.98) | 6.82% (6.24–7.46) | NOT VALIDATED |
| +15% / H+5 | 322 / 2,526 / 11,267 / 225,103 | 11.31% (9.92–12.79) | 2.78% (2.51–3.06) | 4.46% (4.02–4.92) | 4.84% (4.45–5.26) | NOT VALIDATED |
| +20% / H+5 | 162 / 2,686 / 5,054 / 231,316 | 5.69% (4.77–6.65) | 3.11% (2.65–3.59) | 4.02% (3.43–4.63) | 2.18% (2.01–2.36) | NOT VALIDATED |

95% intervals are 3,000-resample cutoff-cluster bootstrap intervals for signal-row metrics; they do not repair the defective labels. H+1/H+3/H+5 full-universe immature exclusions were respectively 596 / 1,650 / 2,524 rows; selected Top-30 immature exclusions were 9 / 24 / 32 rows.

### Close-to-close outcome — separate from intraday high-touch
This uses the actual close at the end of the horizon, not the maximum future high and not the code's stored future-close column.

| Target / horizon | Eligible unique | Universe unique close winners | Selected unique close hits | Missed unique close winners | Close capture |
|---|---:|---:|---:|---:|---:|
| +2% / H+1 | 2,899 | 2,811 | 517 | 2,294 | 17.83% |
| +5% / H+1 | 2,899 | 2,214 | 184 | 2,030 | 6.35% |
| +10% / H+3 | 2,883 | 1,709 | 134 | 1,575 | 4.65% |
| +15% / H+5 | 2,880 | 1,169 | 92 | 1,077 | 3.19% |
| +20% / H+5 | 2,880 | 705 | 48 | 657 | 1.67% |

All close-to-close figures are also **NOT VALIDATED**. Executable trade wins: **UNKNOWN / NOT_AUTHORIZED**; no approved entry, exit, stop, circuit, sizing, overlap or cost assumptions exist.

### 23-Nov morning cohort — matured H+1 only
A separate cutoff-safe base universe was reconstructed from 20-Nov data: EQ series, close >₹50, prior 20 valid sessions' average volume >200,000 shares, and a 23-Nov outcome row. This produced **1,032 eligible unique symbols**. It is a base-screen universe, not a substitute for the missing final selector-decision ledger.

| Scenario | Universe high-touch winners | Qualified alert hit | Missed winners | Eligible unique denominator | Capture |
|---|---:|---:|---:|---:|---:|
| +2% / H+1 | 261 | 1 | 260 | 1,032 | 0.097% |
| +5% / H+1 | 41 | 0 | 41 | 1,032 | 0.00% |

Close-to-close: +2% had 76 universe winners and 0 selected hits; +5% had 17 universe winners and 0 selected hits. +10% / H+3 and +15% / +20% / H+5 remain **IMMATURE**.

The sole qualified observation-only candidate was **WELSPUNLIV** (1 symbol / 1 row): 20-Nov close ₹268.78; 23-Nov high ₹278.99 (**+3.80% intraday high-touch**), close ₹270.76 (**+0.74% close-to-close**), low ₹262.00 (**−2.52% adverse excursion**). Thus +2% high-touch hit, +2% close miss; +5% H+1 miss. This is not a trade win.

Previous shadow cohort: **8 unique symbols / 10 selector rows**, evaluated separately from WELSPUNLIV.

| Symbol | 23-Nov high vs 20-Nov close | 23-Nov close vs 20-Nov close | Adverse excursion |
|---|---:|---:|---:|
| NRL | +1.97% | −1.76% | −2.90% |
| V2RETAIL | −0.45% | −6.45% | −7.75% |
| SIGACHI | +1.86% | −1.57% | −2.49% |
| RSDFIN | +0.11% | −1.95% | −3.52% |
| KDDL | +2.55% | −0.36% | −0.88% |
| YATRA | +0.89% | −3.30% | −4.11% |
| KMCSHIL | +0.84% | −6.79% | −7.90% |
| HINDOILEXP | +7.51% | +3.33% | −2.22% |

Shadow cohort H+1: +2% intraday high-touch 2/8 (KDDL, HINDOILEXP); +5% 1/8 (HINDOILEXP); +2% close-to-close 1/8; +5% close-to-close 0/8. Median adverse excursion −3.21%, range −7.90% to −0.88%. Longer H+3/H+5 outcomes remain immature. This small shadow cohort is not a market-wide capture rate.

**Horizon-calendar correction:** cutoff 20-Nov means 23-Nov is H+1; 24-Nov is a holiday; 25-Nov H+2; 26-Nov H+3; 27-Nov H+4; 30-Nov H+5. The morning note's H+3=25-Nov and H+5=27-Nov dates were one session early and are superseded by this correction.

## 2. Three independent performance tracks

| Track | Status | Evidence-based result |
|---|---|---|
| V11.4 Historical Behavioural Selector | BLOCKED / NOT VALIDATED | Corrected-label frozen-ranking diagnostics above only; no accepted Precision/Recall/F1 or capture claim. DATA_CONTAMINATED State has 26 rows / 22 unique symbols, below the required 50 fully matured observations; State calibration remains UNKNOWN. |
| V11.3 Cost-aware Trade Replay | UNKNOWN / NOT_AUTHORIZED / NOT_RUN | No user-approved execution assumptions or independently reconciled trade ledger. Net return, win rate, expectancy, costs, profit factor and drawdown are UNKNOWN. |
| Global Capital Rotation (GCR) | UNKNOWN / BLOCKED | Only one-day NSE FII/FPI and DII snapshot is present; no synchronized macro/sector/stock vintage panel or defensible crosswalk. No V11.3/V11.4 metric is relabelled as GCR. |

Run #420's 672 diagnostic shape check reports 672 columns = 56×12, but this does not override the session-spine, label and provenance blockers. Final selection remains PROVISIONAL_ONLY_FINAL_SELECTION_BLOCKED with RISK_GEO_NOT_AVAILABLE and LIVE_INTRADAY_1M_FEED_MISSING. NSE live 1m status is HTTP 403 with zero rows. GDELT timeouts and Google News RSS NameError remain recorded. The 23-Nov market snapshot (generated 15:20:05Z) shows NIFTY 50 −1.75%, NIFTY Bank −3.17%, NIFTY Midcap 100 −1.01%, India VIX +3.11%; this is context only, not a GCR performance result. The latest IMF EMDE panel workflow Run #1395 failed and exposed no job record/artifact in the retrieved run response; its cause remains UNKNOWN.

### Best 3 Stocks per Target — target-specific rank status

- **Historical Winners:** +2%, +5%, +10%, +15% এবং +20%—সব target-এ **UNKNOWN / BLOCKED**। Defective labels, 12 duplicate holiday dates, unresolved H+5 parity এবং incomplete raw provenance থাকায় কোনো stock-কে historical winner rank দেওয়া যাবে না।
- **Prospective Candidates:** WELSPUNLIV একমাত্র observation-only qualified candidate; H+1-এ +2% intraday high-touch করেছে, কিন্তু close-to-close +2% করেনি। একক candidate-কে target-specific Best-1/Best-3 rank দেওয়া হচ্ছে না; +5% H+3 ও দীর্ঘ horizon এখনও immature।
- **Final:** পাঁচ target-এর কোনোটির জন্যই evidence-backed Best 3 তালিকা নেই। সংখ্যা পূরণের জন্য stale/provisional Top-30 বা unverified ranking ব্যবহার করা হয়নি। এটি buy recommendation নয়।

## 3. Dataset, workflow, archive and integrity audit

- Morning alert: [Daily Unified Top-5 — 23-Nov](https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/blob/main/docs/DAILY_UNIFIED_TOP5_SWING_WATCHLIST_20261123.md), blob SHA-1 ae329664612040bd0a470800ede951a193581799, SHA-256 d227479be9d83bb0966765aef0ef5ab73d2a055b599fa7aadcfe04ce51b55d01.
- Previous report: [Nightly Review — 22-Nov](https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/blob/main/docs/NIGHTLY_ROTATION_BACKTEST_RESEARCH_REVIEW_20261122.md), SHA-256 d42514bdf1d34cf84573c60c55d83f5f7c63cca232468d2efd56ede3c36ac7ab.
- GitHub scheduled Run #420 / ID 45202379089, job 137788955150, head c9622ba253c8f963736035a77fb94df1682d8d06, conclusion SUCCESS, duration 12m11s (over the requested 10-minute ceiling). Artifact #14833925413, ZIP SHA-256 693cb2d8f68cc38a56fd9c17140f6126e11bb1617d6b0fee9ad4d2de5264686d; independently downloaded ZIP SHA matched the GitHub artifact digest. No new workflow was dispatched by this review.
- Artifact processed dataset: 504,250 rows, 2,999 symbols, 200 requested date labels. **Only 188 are unique valid sessions**: 12 official NSE holidays are duplicate copies of the previous valid session. For all 12 date pairs, every shared symbol's normalized numeric fields matched the previous date (100%); examples include 20-Oct and 19-Oct, both 397,312-byte downloads. The 12 dates are 03-Mar, 26-Mar, 31-Mar, 03-Apr, 14-Apr, 01-May, 28-May, 26-Jun, 14-Sep, 02-Oct, 20-Oct and 10-Nov.
- Root cause is verified in source: collector skips weekends only (lines 246–251); builder assigns DATE from the requested filename (line 49); QA counts sessions.txt rows and distinct filename-derived DATE values, without validating source DATE1/TradDt against the requested date or the official holiday calendar (lines 8–29). The bundled QA JSON says PASS, but semantic session acceptance is **FAIL / NOT_ACCEPTED**.
- Walk-forward code defect is verified: pipeline/walk_forward_backtest.py lines 98–105 computes shift(-1).rolling(h,min_periods=1).max() (a trailing rolling window on the shifted series, not exact T+1…T+h); lines 532–534 use those labels for training. Partial windows are accepted. Holiday duplicates also distort the exchange-session horizon. The model's frozen rankings are therefore contaminated, including the composite score.
- Four holiday cutoffs were removed from the 100-cutoff export, leaving 96 valid cutoffs. Full-universe probability rows: 252,335 original; 10,593 holiday-cutoff rows excluded; 241,742 valid-cutoff rows. The H+5 JSON/CSV discrepancy persists: metrics JSON implies 619 Top-30 hits; prediction CSV contains 622 rows at/above +20% using its stored label.
- Raw NSE source files and a per-file raw-byte manifest are absent from Run #420 artifact. Run log records 23-Nov source retrieval at 2026-11-23T15:11:39.2558057Z (HTTP 200, 405,464 bytes) and 20-Nov at 2026-11-23T15:11:40.1687754Z (HTTP 200, 405,548 bytes); source publication timestamps and per-file raw SHA-256 are not available. The processed dataset hash is reproducible, but does not substitute for raw-source provenance.

### Validation IDs and reproducibility
1. PW-DATE-20261123-R420-SESSIONSPINE-01 — 200 labels / 188 valid sessions / 12 duplicates; 100% duplicate-value comparison; acceptance NOT_MET.
2. PW-V114-20261123-R420-POSTHOC-96C-01 — 96 valid cutoffs, 241,742 eligible probability rows before target maturity exclusions, 3,000-resample cutoff-cluster CI; diagnostic only, NOT_VALIDATED.
3. PW-ALERT-20261123-H1-OUTCOME-01 — 1,032 base-universe symbols, 1 qualified candidate, 8-symbol shadow cohort; H+1 matured, provenance PARTIAL / NOT_VALIDATED.
4. PW-MW-20261123-BASE1032-H1-01 — +2% 261 universe high-touch winners / 260 missed; +5% 41 / 41 missed; candidate-decision export missing, root-cause coverage PARTIAL.

Key SHA-256:
- ZIP artifact: 693cb2d8f68cc38a56fd9c17140f6126e11bb1617d6b0fee9ad4d2de5264686d
- nse_eq_200_sessions.csv: 8d6c634ddbb442bd5003ec96f20fdac8f150b5775f451efd84eeb5262bc12f57
- walk_forward_metrics.json: 7f07438780eca7a7aaae89fd9bc5ee241025fa8f58952a481f2d78ed0ca1f496
- walk_forward_predictions.csv: 37f613d6c4368b98e4d14ac41f5cbb0a445b748b4e5d37dc0d94cd514101d16d
- walk_forward_universe_probabilities.csv: 625d9f5ca9b18af72f78907df2a2a3370fe067c1c83c86e5eaac45bd9bd0c661
- provisional_top30.csv: 064f4562c6837d2a65e1c3d756988ee510b2da2351cee2f055555c8cd99baf23
- qa_report.json: 48547e28ff82e978c8b63712c9fc5e4692268c3c99fba015bd1bfa3d7bd1af19
- market_context.json: 4a5efd8f4fe8e21680e814e407f54f541b341b1359d6b8c304ec2cf478c4ef1c
- live_1m_status.json: 3db350566454f1fb3ad7decbd901ddaa2f59c78ef50e61a906ec1187750a4f07
- diagnostics_672_report.json: c030f411a4d27ce93f8478299938d0bfbee02c88c36292e04c0cfbd1781a4caa

Source code/config SHA-256 (same commit as Run #420):
- pipeline/walk_forward_backtest.py: dca7363ef1c5f56a097ed66b4305935f2c90975e2387b9c5b44780c4101f83e2
- pipeline/v11_3_abcd_e.py: 7800ff3c39b0c58a3162fb196b4f0efaa023dfe3adbeefc5fbe2d5fb0c6a8bbd
- pipeline/risk_modifier.py: 994ac0d6637c7733e73c9756a6e5e4228d9e0bec34b25055d535ab1a9835dd0a
- config/universe.csv: 6a8c89061b367041c4d0e1ab84ba684d0a5e2615674827ebdcc236b361efecb9 (7-byte header-only file; not a populated universe configuration)
- collector/nse_download.py: a55e6390f7e4299fc47b812baaa24047bbfae84686e397f1535e08f56c6f7e0f
- collector/build_200_sessions.py: 7190c653a829b56eaf2041a9886cf0b873de0bd2d1af1821ce0bcb80458181a1
- qa/validate_dataset.py: 2a7590ad14522fa0440ad4609d11e12e0414f5b25f948c10d47c59c025803c19
- .github/workflows/nse_collector.yml: 61121eb2b8bde79844c9594c43e8f30a74ffd45a611d135a5f93eb9651b82f13

## 4. Fixed baseline vs latest rolling window

Same frozen ranking, corrected post-hoc outcome calculation and no transaction costs; both series remain NOT_VALIDATED. Fixed baseline = 96 valid cutoffs; latest rolling = last 20 valid cutoffs (16-Oct–16-Nov). The previous 22-Nov report had no accepted comparable metrics, so no valid day-over-day percentage-point improvement can be claimed.

| Target | Fixed 96-cutoff precision / recall / F1 | Latest 20-cutoff precision / recall / F1 | Rolling minus fixed (pp) |
|---|---|---|---|
| +5% H+1 | 20.34 / 2.72 / 4.80 | 25.21 / 2.39 / 4.37 | +4.87 / −0.33 / −0.43 |
| +10% H+3 | 15.27 / 2.66 / 4.53 | 19.26 / 2.40 / 4.26 | +3.00 / −0.27 / −0.27 |
| +20% H+5 | 5.69 / 3.11 / 4.02 | 7.58 / 3.52 / 4.81 | +1.89 / +0.42 / +0.79 |

Latest-20 95% cluster-bootstrap CIs: +5 precision 20.83–29.55%, recall 2.10–2.79%, F1 3.87–5.01%; +10 precision 14.50–24.67%, recall 1.98–2.91%, F1 3.52–5.10%; +20 precision 5.19–10.23%, recall 2.52–4.59%, F1 3.43–6.22%. Sample rows changed from 241,146→53,465 (+5), 240,092→53,185 (+10), 239,218→52,952 (+20); selected matured rows changed 2,871→599, 2,856→597, 2,848→594. These window deltas are descriptive only, not a strategy improvement claim.

## 5. Selection Failure & Missed-Winner Root-Cause Audit

### False positives / selected candidate
- WELSPUNLIV: +2% H+1 intraday high-touch **hit**; +2% H+1 close-to-close **miss**; +5% H+1 **miss** (the broader +5% H+3 horizon is not yet mature). Low/adverse excursion −2.52%. Low delivery (10.71%) and high-touch/close divergence are cutoff-time risk observations, not a proven causal failure. Root cause for close miss: **UNKNOWN**. No executable trade result.
- No confirmed high-touch false positive in the one-qualified-candidate sample. One close-based miss is recorded separately.

### Missed winners — same 1,032-symbol base universe
- +2% H+1: 261 universe high-touch winners; WELSPUNLIV captured one; **260 unique winners missed**.
- +5% H+1: 41 universe high-touch winners; no qualified candidate captured one; **41 unique winners missed**.
- Close-to-close: +2% 76 winners, +5% 17 winners; no selected close hit.
- Representative missed winners (sorted by realised H+1 high excursion for retrospective diagnosis only; not a prospective ranking):

| Symbol | High / close / adverse | Cutoff-time evidence (20-Nov) | Cause confidence |
|---|---|---|---|
| HINDOILEXP | +7.51 / +3.33 / −2.22% | 5d +12.69%, 20d +31.64%, EMA20>EMA50, RSI 72.31, RVOL 0.39×; morning alert explicitly flagged low volume and prior ASM/high-valuation risk | SUPPORTED |
| SHALPAINTS | +19.89 / +6.72 / +5.67% | 5d +1.55%, 20d +41.09%, EMA20>EMA50, RSI 73.58, RVOL 0.08× | HYPOTHESIS — volume/liquidity gate plausible; no exact decision row |
| HITECH | +16.36 / +13.51 / +6.04% | 5d −0.26%, 20d +14.06%, EMA20<EMA50, RSI 54.94, RVOL 0.56× | HYPOTHESIS — trend/volume confirmation weak |
| ITI | +15.96 / +12.41 / +0.72% | 5d −8.34%, 20d +8.12%, EMA20<EMA50, RSI 49.16, RVOL 0.04× | HYPOTHESIS — weak trend/participation |
| THOMASCOOK | +14.68 / +12.85 / +1.17% | 5d +4.36%, 20d +21.23%, EMA20>EMA50, RSI 68.10, RVOL 0.98× | UNKNOWN — no row-level exclusion reason |
| AJMERA | +13.72 / +8.93 / −2.47% | 5d +12.01%, 20d +16.94%, EMA20>EMA50, RSI 71.36, RVOL 9.81×, delivery 13.90% | UNKNOWN — strong volume/trend but decision row absent |

The morning report's 8-symbol shadow cohort also included SIGACHI (below ₹50 floor), RSDFIN (195 shares traded / illiquid), and KDDL (below the prior-20 average-volume base filter); these are universe exclusions, not eligible-universe misses. NRL, V2RETAIL, YATRA and KMCSHIL did not hit +2% H+1; their cutoff-time extension/weak trend/volume risks are documented, but no causal failure is asserted.

The remaining missed-winner cases (255 additional +2% and 35 additional +5% unique winners outside the six examples) are not individually attributable because the morning artifact does not preserve a complete 1,032-row candidate/eligibility/exclusion decision export. They remain UNKNOWN pending that export. The audit is therefore PARTIAL, not complete.

### Evidence and timing
- NSE archive endpoints used by the collector: https://nsearchives.nseindia.com/products/content/sec_bhavdata_full_20112026.csv and https://nsearchives.nseindia.com/products/content/sec_bhavdata_full_23112026.csv.
- Retrieval timestamps are in the Run #420 log (20:41:40 IST for 20-Nov and 20:41:39 IST for 23-Nov); per-file publication timestamps and raw-byte SHA-256 are unavailable. The processed dataset hash above is the reproducibility anchor, not raw-source provenance.
- WELSPUNLIV official quote page: https://www.nseindia.in/get-quote/equity/WELSPUNLIV/Welspun-Living-Limited. The 21-Nov filing time is preserved as unzoned source text; timezone semantics remain UNKNOWN.
- Selector repository code identity: pipeline/v11_3_abcd_e.py SHA-256 7800ff3c39b0c58a3162fb196b4f0efaa023dfe3adbeefc5fbe2d5fb0c6a8bbd; pipeline/risk_modifier.py SHA-256 994ac0d6637c7733e73c9756a6e5e4228d9e0bec34b25055d535ab1a9835dd0a. The universe CSV is only a 7-byte header; the alert-specific orchestration/config hash and per-symbol decision export were not retained, so causal attribution remains capped at SUPPORTED/HYPOTHESIS/UNKNOWN.
- No later outcome information was used as cutoff-time explanatory evidence. Future OHLC is used only to define the realised outcome.

## 6. Next-day highest-value research actions (Observation only)

1. **Holiday/date-semantic offline regression using retained artifacts only.** Acceptance: every raw/normalized source date matches its manifest/requested date; all 12 holidays are rejected as sessions; no duplicate prior-session rows; a 200-unique-session claim is accepted only after 200 distinct official trading dates exist. Expected artifact: session_spine_qa_20261124.json + duplicate-date comparison. Blocker: no new automated NSE acquisition until a permitted archival route and source-use boundary are established.
2. **Exact forward-label v2 research test, only after separate approval for code work.** Acceptance: H+1/H+3/H+5 equals exactly the next 1/3/5 valid exchange sessions; no partial windows; missing symbol-session rows are excluded, never skipped/forward-filled; row-level labels reconcile independently. Expected artifact: forward_label_v2_acceptance_20261124.json + cutoff-symbol reconciliation. Blocker: current code defect and holiday spine; no selector/production changes.
3. **Full-universe daily decision ledger.** Acceptance: all 1,032 base-universe symbols reconcile to exactly one cutoff-time decision and an explicit eligibility/exclusion reason; selected + missed winners reconcile to the same denominator; timestamps and hashes are attached. Expected artifact: daily_candidate_decision_20261123.csv + denominator reconciliation JSON. Blocker: current morning artifact contains only one qualified candidate and partial shadow rows.

Only proven additional methods: holiday-aware session spine; source-date/manifest parity; exact forward-horizon maturity; cutoff-anchored maturity calendar; per-symbol candidate exclusion ledger; source timestamp timezone contract. No scope expansion beyond these gaps.

## 7. আজকের শিক্ষা ও গবেষণায় সংযোজন

- Existing lessons updated, not duplicated: PW-LSN-20261121-001 (forward labels), PW-LSN-20261121-002 (H+5 JSON/CSV mismatch), PW-LSN-20261123-001 (holiday duplicate sessions), PW-LSN-20261121-003 (raw manifest/provenance), and PW-LSN-20261123-002 (timezone contract remains UNKNOWN).
- New immutable lessons: PW-LSN-20261123-003 (cutoff-to-horizon maturity dates were one session early); PW-LSN-20261123-004 (HINDOILEXP +2/+5 H+1 missed winner); PW-LSN-20261123-005 (SHALPAINTS +2/+5 H+1 missed winner); PW-LSN-20261123-006 (HITECH +2/+5 H+1 missed winner); PW-LSN-20261123-007 (ITI +2/+5 H+1 missed winner); PW-LSN-20261123-008 (THOMASCOOK +2/+5 H+1 missed winner); PW-LSN-20261123-009 (AJMERA +2/+5 H+1 missed winner); PW-LSN-20261123-010 (missing full-universe candidate-decision export).
- Acceptance status: all new diagnostic tests OPEN / NOT_ACCEPTED. The remaining 255 +2% and 35 +5% missed winners are not individually assigned causal lessons because the required decision export is missing; they remain UNKNOWN, not guessed.
- Research notes added only for proven data/timing/decision-export gaps. No thresholds, ranking, selector, production code or admission changed.
- Next verification: corrected cutoff calendar; 200 unique-session date gate; exact forward-label reconciliation; complete candidate-decision denominator.
