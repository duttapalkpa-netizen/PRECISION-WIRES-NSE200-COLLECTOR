# India Pre-Market — Unified Top-5 Swing Watchlist
## 2026-11-21 | Audit-only research report

**Release decision: qualified candidates = 0. No reliable alert today.**  
21-Nov-2026 is Saturday; the next regular equity session is Monday 23-Nov. NSE's 2026 capital-market holiday circular lists Tuesday 24-Nov as a full trading holiday. This is a research watchlist, not a buy instruction.

## 1. Progress Log

### Completed
- Re-read the master continuity ledger, 20-Nov daily report, prior Run #407 evidence report, archived artifacts, and relevant workflow history before screening.
- Reused completed Run #339 rather than dispatching another workflow or repeating its 200-session acquisition.
- Independently downloaded and SHA-256 checked Run #339 artifact; verified the artifact digest against GitHub's uploaded digest.
- Recomputed the strict 30-matured-cutoff shadow-selector confusion matrices and cutoff-cluster bootstrap intervals from the archived daily audit CSV.
- Reviewed the 20-Nov label-free shadow picks and reused prior official ISIN / risk evidence where still relevant.
- Kept A, B and C scorecards separate. No production code, selector, ranking, or engine changes.

### Blocked / UNKNOWN
- Run #339 artifact omits the 200 raw bhavcopy-delivery files, immutable raw-file manifest and raw per-file hashes. Its logs confirm the 20-Nov session was downloaded, but the raw rows cannot be independently inspected from the retained artifact.
- The 20-Nov candidate-level closing prices, exact quote timestamps, price-volume fields, current circuits and surveillance status are therefore not independently verified here.
- The 100-cutoff main-model recall denominator remains unreconciled with the eligible-universe export; main-model false-positive counts and confidence intervals remain UNKNOWN.
- No user-approved V11.3 entry/exit/stop/circuit/cost assumptions or independently reconciled cost-aware replay.
- No timestamp/vintage-aligned macro → sector → stock → matured-outcome GCR join.
- The previously documented live 1-minute feed remains BLOCKED_SOURCE_ACCESS_403; the EOD audit does not clear that gate.

### Exact next actions
1. Recover the already-downloaded 20-Nov raw bhavcopy-delivery bytes and security master from an existing authorized archive, with manifest, byte counts and SHA-256; do not infer prices from selector ranks.
2. Reconcile the 100-cutoff all_by_date denominator with the exported eligible universe before publishing full-market recall or FP counts.
3. Keep V11.3 replay and GCR UNKNOWN until their separate evidence gates pass. Do not tune production.

## 2. Data cutoff, universe and provenance

- Audit timestamp: **2026-11-21 08:46 IST**.
- Latest prospective selector cutoff: **2026-11-20**.
- Latest completed prospective workflow: **Run #339**, run ID **44799560798**, completed successfully at 2026-11-20 19:18:04 UTC (2026-11-21 00:48:04 IST); source commit **624be8f126f39bd6a146d732ec3f87edde964aec**.
- Workflow log: 200 FULL_BHAVCOPY_DELIVERY downloads returned HTTP 200; newest logged date **20112026**; VALID_SESSIONS=200; normalized dataset log reported **503,892 rows, 2,999 symbols, 200 dates**.
- Artifact QA JSON reports status PASS, 200 raw files, 200 sessions, 200 processed dates, 2,999 symbols, 100% delivery-quantity and delivery-percentage coverage, issues empty. This is the workflow's QA output, not an independent raw-byte audit.
- The Run #339 ZIP does not contain the raw or processed 200-session price file or a raw manifest. The latest independently inspectable processed CSV in the previously recovered Run #407 artifact ends on **2026-11-19**, not 20-Nov. Run #339 logs prove a 20-Nov acquisition occurred, but not the candidate-level values or their timestamps.
- Latest selector output: 10 rows across two selectors, **8 unique symbols**; all 8 have frozen production RANKING_SCORE base ranks greater than 30. Selection score values are ranks, not calibrated probabilities.
- The 20-Nov picks were generated label-free: log says LABELS=NOT_READ FROM_FUTURE. The 20-Nov rows are not matured outcomes.
- Broader universe for the 200-session QA: 2,999 symbols. The current candidate review is limited to the 8 experimental shadow picks; no broader fresh candidate screen is claimed.
- No new workflow was dispatched by this audit; no paid API or external vendor was used.

## 3. Engine A — V11.4 Historical Behavioural Selector

**Status: PARTIAL — retrospective evidence only; not a live probability forecast.**

### Main frozen Top-30 walk-forward summary

Run #339's walk_forward_metrics.json reports 100 tested cutoffs and 3,000 Top-30 rows:

| Target | Source-reported precision / hit rate | Source-reported recall* | Base rate* | Lift* | Target-specific valid n / FP / CI |
|---|---:|---:|---:|---:|---|
| +5% H+1 | 32.43% | 4.08% | 9.17% | 3.54× | UNKNOWN / UNKNOWN / unavailable |
| +10% H+3 | 22.03% | 3.62% | 6.83% | 3.23× | UNKNOWN / UNKNOWN / unavailable |
| +15% H+5 | 14.10% | 3.19% | 4.87% | 2.89× | UNKNOWN / UNKNOWN / unavailable |
| +20% H+5 | 6.96% | 3.49% | 2.20% | 3.17× | UNKNOWN / UNKNOWN / unavailable |

*The source code computes recall and base rate against its internal all_by_date frame. The retained Run #339 artifact does not include row-level universe predictions needed to reconcile that denominator with the eligible-universe export. Thus the starred recall/base-rate/lift values remain provisional, and no main Top-30 FP count or main-model confidence interval is asserted.*

### Strict matured shadow shortlist audit

The archived strict_30_matured_cutoff_daily.csv was independently recalculated for the **CURRENT_WINNER_PROB** selector: Top 5 outside the frozen production Top 30 on 30 matured cutoff dates. Each target has 150 valid picks. Recall below is strictly the capture rate within the matured, eligible **outside-Top-30** pool, not full-market recall.

| Target | TP / valid picks | FP | FN | TN | Eligible outside-Top-30 rows | Outside-Top-30 winners | Precision / hit rate (95% cutoff-cluster CI) | Outside-Top-30 recall (95% CI) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| +5% H+1 | 41 / 150 | 109 | 8,467 | 70,424 | 79,041 | 8,508 | 27.33% (19.33–36.00%) | 0.482% (0.346–0.637%) |
| +10% H+3 | 31 / 150 | 119 | 5,389 | 73,269 | 78,808 | 5,420 | 20.67% (14.00–27.33%) | 0.572% (0.381–0.795%) |
| +20% H+5 | 20 / 150 | 130 | 1,525 | 76,507 | 78,182 | 1,545 | 13.33% (8.67–18.00%) | 1.294% (0.812–1.884%) |

- The paired cutoff-cluster bootstrap used 20,000 resamples, seed 20261121, percentile 95% intervals. Resampling unit was the cutoff date, not individual stock rows.
- Base rates in this outside-Top-30 pool were 10.76% (+5 H+1), 6.88% (+10 H+3), and 1.98% (+20 H+5). Corresponding point-estimate lifts were 2.54×, 3.00× and 6.75×; 95% cluster-bootstrap intervals were 1.82–3.35×, 2.00–4.18× and 4.23–9.82×.
- The P10_P20_MEAN shadow challenger returned 30/150, 31/150 and 16/150 hits for the same targets. Challenger-minus-current paired precision differences were −7.33 pp [−14.67, 0.00], 0.00 pp [−6.02, +6.00], and −2.67 pp [−6.67, +1.33], respectively.
- These are retrospective selected-pick excursion labels, not executable returns, not net of costs, and not evidence of prospective superiority. The challenger is not promoted. The 30-cutoff pooled sample does not establish the required minimum of 50 fully matured observations for each Behavioral DNA State; state calibration remains UNKNOWN.

## 4. Engine B — V11.3 Cost-aware Trade Replay

**Status: UNKNOWN — NOT AUTHORIZED / NOT RUN.**

No user-approved entry, exit, stop, circuit/slippage, brokerage, taxes or position-sizing assumptions were supplied for this replay. No independently reconciled execution replay is attached. Cost-adjusted return, win rate and drawdown are UNKNOWN. Engine B contributes no ranking score or boost.

## 5. Engine C — Global Capital Rotation & Relative-Attraction

**Status: UNKNOWN — BLOCKED.**

No complete timestamp/vintage-aligned macro → sector → stock → matured-outcome join is evidenced for this candidate set. Current sector-relative strength and macro transmission are not independently verified. No GCR boost is applied.

## 6. Current shadow picks — all excluded from the qualified alert

The following are experimental shadow picks only. The rank pair is CURRENT_WINNER_PROB / P10_P20_MEAN; a dash means not selected by that selector. No candidate-specific historical target probability is available.

| Symbol | Shadow rank pair / base rank | NSE security identity | Last official price/time available in inspected evidence | Catalyst and risk evidence | Decision / engine evidence |
|---|---:|---|---|---|---|
| NRL | 1 / 1; base 60 | NSE; ISIN INE0JM501013 verified | ₹172.50 close, 2026-11-13 16:00 IST — stale, not 20-Nov | 12-Nov Q2 filing is already public. The prior 13-Nov snapshot showed BE series, 5% band, 100% margin and impact cost 2.31; current series, band, margin, liquidity and surveillance UNKNOWN. | EXCLUDED: no independently verified 20-Nov close/volume. A = shadow rank only; B/C = UNKNOWN. |
| V2RETAIL | 2 / —; base 43 | NSE main board; ISIN INE945H01021 verified | UNKNOWN | Q2 integrated filing dated 03-Nov. NSE filing also records a promoter block-deal sale of 6.26 million shares on 06-Nov; current supply, price, volume, circuit and surveillance UNKNOWN. | EXCLUDED: current price/time and liquidity not verified. A = shadow rank only; B/C = UNKNOWN. |
| SIGACHI | 3 / —; base 32 | NSE main board; ISIN INE0D0K01022 verified | UNKNOWN | NSE prior intimation dated 28-Oct proposed a 31-Oct board meeting for financial results; a current catalyst/outcome was not independently verified in this audit. | EXCLUDED: current price/time, technicals, liquidity and surveillance UNKNOWN. A = shadow rank only; B/C = UNKNOWN. |
| RSDFIN | 4 / —; base 94 | NSE symbol in selector; official ISIN/series UNKNOWN | UNKNOWN | Fresh official catalyst, price-volume, sector context, liquidity, circuit and surveillance UNKNOWN. | EXCLUDED: security identity and market data incomplete. A = shadow rank only; B/C = UNKNOWN. |
| KDDL | 5 / 3; base 68 | NSE main board; ISIN INE291D01011 verified | ₹4,368 snapshot, 2026-11-17 12:05:27 IST — intraday and stale | The prior snapshot showed +11.61% intraday, 20% band, 52-week high ₹4,440 and impact cost 0.16. Results/investor-presentation disclosures were around 13-Nov; no fresh 20-Nov catalyst or closing quote verified. | EXCLUDED: no 20-Nov close, current band or volume verified. A = shadow rank only; B/C = UNKNOWN. |
| YATRA | — / 2; base 58 | NSE main board; ISIN INE0JR601024 verified | UNKNOWN | Q2 release dated 12-Nov was mixed: revenue and EBITDA fell YoY while gross bookings rose. It is not a new 20-Nov catalyst. | EXCLUDED: current price, volume, relative strength, liquidity and surveillance UNKNOWN. A = shadow rank only; B/C = UNKNOWN. |
| KMCSHIL | — / 4; base 39 | NSE symbol in selector; official listing/ISIN not verified | UNKNOWN | Current official filing, quote, catalyst, price-volume, liquidity, circuit and surveillance UNKNOWN. Quote page was not accessible in this audit. | EXCLUDED: identity and current market evidence incomplete. A = shadow rank only; B/C = UNKNOWN. |
| HINDOILEXP | — / 5; base 56 | NSE main board; ISIN INE345A01011 verified | ₹220.86, 2026-11-19 11:31:43 IST — intraday, not close | 19-Nov snapshot showed ST ASM-1, P/E above 50 for the previous four trailing quarters and 50% applicable margin. Q2 filing dated 06-Nov. Current surveillance and 20-Nov closing data UNKNOWN. | EXCLUDED: stale intraday quote and explicit surveillance/valuation risk. A = shadow rank only; B/C = UNKNOWN. |

For all eight shadow picks:
- 20-Nov official closing price and exact price timestamp: UNKNOWN in the retained artifact.
- 2%, 5%, 10% and 20% target price levels: **not generated** because a verified price base is unavailable.
- Live horizon, entry, stop, invalidation and exit: UNKNOWN. No user trade rules were assumed.
- Current price-volume, relative strength, sector alignment, liquidity, circuit and surveillance checks: UNKNOWN unless a dated historical warning is explicitly described above.
- No guarantee or probability of a 2–20% move is implied.

## 7. Prior comparable day change

Compared with the 19-Nov cutoff union in the 20-Nov report:
- Previous union: 7 symbols.
- Current 20-Nov cutoff union: 8 symbols.
- Retained: NRL, KDDL, YATRA, HINDOILEXP (4).
- New: V2RETAIL, SIGACHI, RSDFIN, KMCSHIL (4).
- Removed: ELITECON, LEENEE, ARYAMAN (3).

This is shadow-list turnover only, not a performance improvement. All 20-Nov picks remain future-labelled/unmatured.

## 8. Exclusions and release decision

- Qualified candidates: **0**.
- All 8 latest shadow picks are excluded until price/time, current volume/relative strength, liquidity and current circuit/surveillance evidence are independently verified.
- No target bands or stops are published from stale or missing prices.
- No other symbols are added: the retained run artifact does not provide a fresh, row-level full-universe price/technical screen for independent candidate review.
- **NO RELIABLE ALERT for the next session. Do not fill the five slots.**

## 9. Reproducibility and immutable references

- Prior daily report: docs/DAILY_UNIFIED_TOP5_SWING_WATCHLIST_20261120.md; Git blob SHA eaf527f31aa39bc202ce966410c5602709718108.
- Latest workflow: [Run #339](https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/44799560798), run ID 44799560798, conclusion success, source commit 624be8f126f39bd6a146d732ec3f87edde964aec.
- Artifact: [prospective-watchlist-audit, ID 14660032260](https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/44799560798/artifacts/14660032260), size 50,543 bytes.
- Independently computed ZIP SHA-256: 23e74e7f9ef2e32bf5b6bbc5a931814c06fe065835b8bdda74f3c00dbdafd213; matches GitHub artifact digest.
- Independently computed internal SHA-256:
  - data/qa/qa_report.json: 48547e28ff82e978c8b63712c9fc5e4692268c3c99fba015bd1bfa3d7bd1af19
  - outputs/prospective/latest_picks.csv: f03b8426bf67b3eaf683d3e520792e1ee5a9e16495818f964aa76f7cba068cc9
  - outputs/prospective/watchlist_ledger.csv: b297883ef6a53d8e5d3498eaf8e62797872b7cdcc101ccdea8ced338a49ecea5
  - outputs/backtest/walk_forward_metrics.json: c170239580dd5f0253a15650c545c69d7140a46be99c569ce7b313a595b23326
  - outputs/prospective/strict_30_matured_cutoff_audit.json: e3e448e210a2b0575ffbef43a37e79d1681716c348e97430dfb15e67e0c04871
  - outputs/prospective/strict_30_matured_cutoff_daily.csv: 940e13cdc6d69a8cb2363b1f40aacdfd30a67d63fc24bbc4b1bd75151c9125cd
  - outputs/prospective/reproducibility_check.json: 1c4ee61c0a44d257aec8ba7e0ce870622b686006f69342381fde6597d2bb3b62
- Reproducibility JSON says the historical audit was repeated twice and selected outputs matched byte-for-byte; input hash was unchanged. This is audit-output reproducibility, not independent raw-source replay.
- Raw 20-Nov bhavcopy-delivery bytes and manifest were not in the artifact; no raw-source SHA-256 is claimed.
- No new workflow dispatch, production code change or selector promotion occurred.

## 10. Official sources

- [NSE All Reports — CM-UDiFF Bhavcopy, Full Bhavcopy and Security Deliverable data](https://www.nseindia.in/all-reports)
- [NSE Capital Market Trading Holidays 2026, Circular NSE/CMTR/71775](https://nsearchives.nseindia.com/content/circulars/CMTR71775.pdf)
- [NSE market timings and holidays](https://www.nseindia.in/resources/exchange-communication-holidays)
- [NSE quote — NRL](https://www.nseindia.com/get-quotes/equity?symbol=NRL)
- [NSE quote — V2RETAIL](https://www.nseindia.com/get-quotes/equity?symbol=V2RETAIL)
- [NSE quote — SIGACHI](https://www.nseindia.com/get-quotes/equity?symbol=SIGACHI)
- [NSE quote — RSDFIN](https://www.nseindia.com/get-quotes/equity?symbol=RSDFIN)
- [NSE quote — KDDL](https://www.nseindia.com/get-quotes/equity?symbol=KDDL)
- [NSE quote — YATRA](https://www.nseindia.com/get-quotes/equity?symbol=YATRA)
- [NSE quote — HINDOILEXP](https://www.nseindia.com/get-quotes/equity?symbol=HINDOILEXP)
- [V2RETAIL Q2 integrated filing, 03-Nov-2026](https://nsearchives.nseindia.com/corporate/ixbrl/INTEGRATED_FILING_INDAS_208957_03112026190824_iXBRL_WEB.html)
- [V2RETAIL promoter PIT disclosure, 06-Nov-2026](https://nsearchives.nseindia.com/corporate/ixbrl/IT_2621_20261106_115841252_WEB.html)
- [SIGACHI prior board-meeting intimation, 28-Oct-2026](https://nsearchives.nseindia.com/corporate/ixbrl/PRIOR_INTIMATION_18747_20261028_112803925_WEB.html)
- [NRL NSE integrated filing / ISIN evidence](https://nsearchives.nseindia.com/corporate/ixbrl/INTEGRATED_FILING_INDAS_142658_12022026195615_iXBRL_WEB.html)
- [KDDL NSE integrated filing / ISIN evidence](https://nsearchives.nseindia.com/corporate/ixbrl/INTEGRATED_FILING_INDAS_159118_19052026225424_iXBRL_WEB.html)
- [YATRA Q2 integrated filing, 12-Nov-2026](https://nsearchives.nseindia.com/corporate/ixbrl/INTEGRATED_FILING_INDAS_213267_12112026234440_iXBRL_WEB.html)
- [HINDOILEXP Q2 integrated filing, 06-Nov-2026](https://nsearchives.nseindia.com/corporate/ixbrl/INTEGRATED_FILING_INDAS_211640_06112026233437_iXBRL_WEB.html)

## 11. Protected invariants

Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 remain unchanged. UNKNOWN is never PASS. ₹0 research spend; official/free sources only; no synthetic data or fabricated timestamps.
