# India Pre-Market — Unified Top-5 Swing Watchlist
## 2026-11-20 | Audit-only research report

**সিদ্ধান্ত: যোগ্য candidate <5 — আজ 0টি qualified alert।**  
এই রিপোর্ট watchlist research; buy instruction নয়। বর্তমান official price, liquidity, surveillance এবং engine evidence একসঙ্গে যাচাই না হওয়ায় দুর্বল/অযাচাইকৃত নাম দিয়ে পাঁচটি পূরণ করা হয়নি।

### 1. Data cutoff, universe ও provenance

- Report timestamp: **2026-11-20, 08:45 IST**.
- Shadow selector cutoff: **2026-11-19**; workflow log: `LIVE_CUTOFF=2026-11-19 PICKS=10 LABELS=NOT_READ FROM_FUTURE`.
- NSE archived QA: **PASS** — 200 raw sessions, 200 processed sessions, 2,997 symbols, delivery-quantity ও delivery-% coverage 100%, issues=[].
- Historical engine: 100 cutoff sessions, 3,000 Top-30 rows (30 per cutoff).
- Live shadow list: দুই selector-এ 10 rows, **7 unique symbols**; সবগুলো frozen production Top-30-এর বাইরে। `SELECTION_SCORE_VALUE` ranking score, calibrated probability নয়।
- Important limitation: uploaded workflow artifact-এ raw 200-session data, immutable raw-file manifest, row-level Top-30 predictions এবং `walk_forward_universe_probabilities.csv` নেই। ফলে QA JSON ও aggregate metrics পাওয়া গেলেও raw input থেকে সম্পূর্ণ independent replay করা যায়নি। Source code-এ recall/base-rate denominator `all_by_date` (cutoff dates-এর raw rows), কিন্তু probability export-এ history-depth ≥20 ও feature-eligible rows ব্যবহৃত হয়; এই membership reconciliation artifact-এ নেই। তাই recall/base-rate/lift **provisional**, false-positive counts **UNKNOWN**।
- আগের published daily report পাওয়া যায়নি। Comparable model ledger-এর সর্বশেষ cutoff 2026-11-18।

### 2. Three independent engine scorecards

#### A — V11.4 Historical Behavioural Selector

**Status: PARTIAL — retrospective/exploratory.**

Run artifact `walk_forward_metrics.json`-এর reported Top-30 results:

| Target | Reported precision / hit rate | Reported recall* | Base rate* | Lift* | Target-specific valid n / FP |
|---|---:|---:|---:|---:|---|
| +5% H+1 | 32.73% | 4.12% | 9.17% | 3.57× | UNKNOWN / UNKNOWN |
| +10% H+3 | 22.34% | 3.67% | 6.85% | 3.26× | UNKNOWN / UNKNOWN |
| +15% H+5 | 14.33% | 3.21% | 4.91% | 2.92× | UNKNOWN / UNKNOWN |
| +20% H+5 | 7.07% | 3.52% | 2.21% | 3.20× | UNKNOWN / UNKNOWN |

* Recall/base-rate/lift source summary থেকে এসেছে; raw denominator ও exported eligible-universe row membership independently reconcile হয়নি। Aggregate artifact-এ 3,000 Top-30 rows আছে, কিন্তু target-wise valid prediction count এবং row-level TP/FP list নেই। তাই confidence interval নেই এবং FP count বানিয়ে দেওয়া হয়নি।

**Separate matured-cutoff shadow comparison:** 30 matured cutoffs × 5 picks = 150 picks per selector per target; retrospective only, not prospective validation.

| Target | CURRENT_WINNER_PROB | P10_P20_MEAN | Challenger − current paired 95% CI |
|---|---:|---:|---:|
| +5% H+1 | 41/150 = 27.33% | 30/150 = 20.00% | −7.33 pp [−14.00, −0.67] |
| +10% H+3 | 31/150 = 20.67% | 31/150 = 20.67% | 0.00 pp [−6.02, +6.00] |
| +20% H+5 | 19/150 = 12.67% | 16/150 = 10.67% | −2.00 pp [−6.00, +1.33] |

These are paired cutoff-date bootstrap intervals from the strict 30-matured-cutoff audit. They do not establish prospective superiority; promotion_authorized=false. No selector change is authorised. Top-30 generic winner-probability mean separation was also negligible/reversed (winner 0.08703 vs non-winner 0.08727). Target-specific eligible-universe calibration: H+1 n=251,546 (Brier 0.08017; ECE 0.01473; winner/non-winner mean gap +0.01034), H+3 n=251,183 (Brier 0.06173; ECE 0.00376; gap +0.00343), H+5 n=250,776 (Brier 0.02076; ECE 0.00031; gap +0.00024). এগুলো calibration diagnostics, আজকের নামগুলোর hit probability নয়।

#### B — V11.3 Cost-aware Trade Replay

**Status: UNKNOWN — NOT AUTHORIZED / NOT RUN.**

User-approved entry, exit, stop, circuit/slippage, brokerage, taxes and position-sizing assumptions are not present in this run; no independently reconciled cost-aware replay is attached. No net return, win rate, drawdown or B-score assigned. This engine contributes **no ranking boost**.

#### C — Global Capital Rotation & Relative-Attraction

**Status: UNKNOWN — BLOCKED.**

No complete timestamp/vintage-aligned macro → sector → stock → matured-outcome join was evidenced in this artifact. Official market snapshot is context only, not a GCR signal. No GCR boost applied.

**Market context (NSE, 2026-11-19 close):** NIFTY 50 +1.14%, NIFTY 100 +1.22%; 16:00 market breadth 2,012 advances vs 1,606 declines. NIFTY IT −1.10%, NIFTY Auto +4.40%, NIFTY FMCG +2.09%. This broad index snapshot does not prove sector-specific alignment for today's candidates.

### 3. Latest shadow selector output — candidate-level screening

Selector ranks below are experimental ranks outside the frozen Top-30, not production ranks or probability estimates.

| Symbol | CURRENT rank / base rank | P10_P20 rank / base rank | Exchange / ISIN | Last official quote available | Screen decision |
|---|---:|---:|---|---|---|
| ELITECON | 1 / 128 | — | NSE EQ; INE669R01026 verified | Price/time UNKNOWN | Exclude: current price, volume, current surveillance and catalyst not verified |
| NRL | 2 / 60 | 1 / 60 | NSE; INE0JM501013 verified | ₹172.50 close, 2026-11-13 16:00 IST | Exclude: stale quote; BE series, 5% price band, 100% applicable margin, impact cost 2.31 on that dated NSE snapshot |
| KDDL | 3 / 44 | 2 / 44 | NSE EQ; INE291D01011 verified | ₹4,368 snapshot, 2026-11-17 12:05:27 IST | Exclude: no 19-Nov official close verified; dated snapshot already showed +11.61% intraday, 20% band and 52-week high ₹4,440 |
| LEENEE | 4 / 78 | — | NSE symbol from selector; official ISIN/series UNKNOWN | Price/time UNKNOWN | Exclude: official security/price, liquidity, surveillance and circuit status not verified |
| YATRA | 5 / 43 | 3 / 43 | NSE EQ; INE0JR601024 verified | Price/time UNKNOWN | Exclude: current official price/volume and technical context unavailable; Q2 result is mixed and already public |
| HINDOILEXP | — | 4 / 40 | NSE EQ; INE345A01011 verified | ₹220.86, 2026-11-19 11:31:43 IST (intraday snapshot, not close) | Exclude: NSE flagged ST ASM-1 and P/E >50 for previous 4 trailing quarters; 50% margin; quote not final close |
| ARYAMAN | — | 5 / 69 | NSE symbol from selector; official ISIN/series UNKNOWN | Price/time UNKNOWN | Exclude: official security/price, liquidity, surveillance and catalyst not verified |

#### Candidate evidence notes

- **HINDOILEXP:** NSE quote snapshot reported 1W +16.84% vs NIFTY 50 +0.16%, 1M +32.66% vs NIFTY 50 +10.71%, traded volume 7.73 lakh, traded value ₹17.30 crore, impact cost 0.08 and deliverable/traded quantity 36.08%. 52-week high ₹238.89 was recorded on 2026-11-18. Momentum exists, but the explicit ST ASM-1 and elevated P/E flags, plus the intraday-only price timestamp, fail the alert gate.
- **NRL:** NSE snapshot as of 2026-11-13 16:00 showed BE series, 5% price band, 100% applicable margin, impact cost 2.31, volume 45.75K and value ₹78.35 lakh. NSE also flagged close-to-close price movement >75% in the previous 6 months and >100% in the previous 365 days; order-book fields were blank in that snapshot. This is an execution-friction warning, not a current 20-Nov quote.
- **KDDL:** NSE snapshot as of 2026-11-17 12:05 showed ₹4,368, +11.61%, volume 2.58 lakh, value ₹111.42 crore, impact cost 0.16, 20% price band and 52-week high ₹4,440. NSE filings show results/investor-presentation disclosures around 13-Nov; no new catalyst with a verified 20-Nov timestamp was established. A fresh official 19-Nov closing quote was not verified.
- **YATRA:** NSE-filed 2026-11-12 press release reports Q2 revenue ₹2,136 million (−39.1% YoY), adjusted EBITDA ₹150 million (−41.2%), EBITDA ₹132 million (−47.0%) and net loss ₹7 million. Offsetting positives: Q2 gross bookings +6% YoY, H1 gross bookings +11%, corporate gross bookings +18%, and air gross bookings +15%. Mixed fundamentals; no current official price/volume confirmation.
- **ELITECON:** ISIN INE669R01026 is verified in an NSE circular; current quote, price band and surveillance status were not independently verified for this cutoff.
- **LEENEE / ARYAMAN:** selector membership alone is not sufficient. Official current quote, ISIN, series, price band, liquidity and surveillance checks remain UNKNOWN.

### 4. Target bands, horizon, invalidation and risk

- Qualified candidates: **0**. Therefore no 2%, 5%, 10% or 20% price bands have been generated. A stale or missing price must not be used as a target base.
- Candidate-specific horizon: UNKNOWN. Historical labels H+1/H+3/H+5 do not assign a live horizon to an unverified candidate.
- Entry, stop, invalidation and exit levels: UNKNOWN; no user-approved trade rules were inferred.
- Circuit/surveillance/news: material warnings are recorded above; missing checks remain UNKNOWN, not clear.
- No guarantee of any 2–20% move is implied.

### 5. Prior comparable model-list change

Latest model ledger cutoff before today: 2026-11-18. Unique-symbol union changed from 7 names to 7 names on 2026-11-19. Retained: **NRL, LEENEE** (2); new entrants: **ELITECON, KDDL, YATRA, HINDOILEXP, ARYAMAN** (5); removed: **BNALTD, CHEMFAB, SANGAMIND, VENUSREM, DHANBANK** (5). This is selector-list turnover only; it is not evidence of performance. All 2026-11-19 picks remain future-labelled/unmatured in the prospective tracker.

### 6. Exclusions and release decision

- Excluded from today's qualified list: all 7 shadow-selector names, for the candidate-specific reasons above.
- Other names: not added; the artifact provides only the 10 shadow picks, and no broader fresh official screen with row-level data was independently available.
- Release decision: **NO RELIABLE ALERT TODAY — 0 qualified candidates**. Do not fill the five slots.

### 7. Reproducibility and immutable references

- GitHub workflow: [Run #338](https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/44599244783) — run ID `44599244783`, conclusion `success`, source commit `6899422730c6fdf30d4e1b93c8cac2ce0efe64e2`.
- Artifact: [prospective-watchlist-audit, ID 14567098741](https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/44599244783/artifacts/14567098741), size 50,287 bytes. Independently calculated ZIP SHA-256: `d500b8c42e10bde7640d177243aae2c305e4bf21eea3d7bc85cc7ffea71085c3` (matches upload log digest).
- Audit-branch head after prospective ledger update: `34e4718f928753bb8acf93e285ad8c04f6501e70`.
- Artifact internal file SHA-256:
  - `latest_picks.csv`: `f5292dada014864764135ad9a591b3ef378e8b437b9219bc42e508afb296f7a5`
  - `walk_forward_metrics.json`: `a1fccf5d402f8a4ae0c540790c31aee7c9794894099d7c58ec1af38358e00925`
  - `qa_report.json`: `81d21799277b651d63e736ff5a1e6267e15ba04dbd7849cf1f737228a3d57c36`
  - `strict_30_matured_cutoff_audit.json`: `02ee46d92ef70ddf3807400e712848b62cb97aa700ff95d1b5fa8a7d4901c304`
  - `watchlist_selector_experiment_summary.json`: `95f2548174d35917626796f28dc2611a7f99f4325aea11cd33a431cd452ad5cc`
  - `multiwindow_retrospective_audit.json`: `c846463404661beab4bba963f81f91b5bde1a8ce4239b297bf233a5ced27a1f7`
- Run QA `PASS` does not promote the exploratory selector or resolve missing row-level provenance. This report does not label the recall/FP audit or any candidate as PASS.

### 8. Official source links

- [NSE market snapshot and indices](https://nseindia.in/)
- [NSE — HINDOILEXP quote and surveillance fields](https://www.nseindia.in/get-quote/equity/HINDOILEXP/Hindustan-Oil-Exploration-Company-Ltd)
- [NSE — NRL quote and security fields](https://www.nseindia.in/get-quote/equity/NRL/Nupur-Recyclers-Limited)
- [NSE — KDDL quote and security fields](https://www.nseindia.in/get-quote/equity/KDDL/KDDL-Limited)
- [NSE — YATRA integrated filing, 12-Nov-2026](https://nsearchives.nseindia.com/corporate/ixbrl/INTEGRATED_FILING_INDAS_213267_12112026234440_iXBRL_WEB.html)
- [NSE — YATRA Q2/H1 FY27 press release, 12-Nov-2026](https://nsearchives.nseindia.com/corporate/YATRA2022_12112026235603_Press_Release_Financials_12112026.pdf)
- [NSE circular security/ISIN list including ELITECON](https://nsearchives.nseindia.com/content/circulars/CML73797.pdf)

### 9. Protected invariants

No production code or ranking changes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 remain unchanged. UNKNOWN is not PASS. No synthetic data, paid API, assumed stop, or fabricated timestamp used.
