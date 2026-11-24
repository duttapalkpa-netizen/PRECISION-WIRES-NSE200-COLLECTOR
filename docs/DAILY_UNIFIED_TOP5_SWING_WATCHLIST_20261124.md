# PRECISION-WIRES V11.3 — ২৪ নভেম্বর ২০২৬
## India Pre-Market Unified Top-5 Swing Watchlist
**পরবর্তী সম্ভাব্য equity session:** বুধবার, ২৫ নভেম্বর ২০২৬  
**আজকের অবস্থা:** NSE Capital Market segment বন্ধ — Prakash Gurpurb Sri Guru Nanak Dev / Guru Nanak Jayanti। সরকারি NSE 2026 holiday circular: https://nsearchives.nseindia.com/content/circulars/CMTR71775.pdf  
**Data cutoff:** ২৩ নভেম্বর ২০২৬-এর সর্বশেষ retained processed NSE session; ২৪-Nov live equity price নেই।

**যোগ্য candidate: ০**

**সিদ্ধান্ত:** আজ/পরবর্তী session-এর জন্য কোনো qualified Top-5 alert প্রকাশ করা হয়নি। ২৩-Nov artifact-এর final readiness state `PROVISIONAL_ONLY_FINAL_SELECTION_BLOCKED`; blockers: `RISK_GEO_NOT_AVAILABLE` এবং `LIVE_INTRADAY_1M_FEED_MISSING`। Live 1m quote request HTTP 403-এ blocked। Provisional Top-N বা shadow picks-কে qualified candidate হিসেবে দেখানো হয়নি।

## 1. Preflight — ledger, reports, archives, runs, hashes

- Master Continuity Ledger C64 পর্যন্ত পড়া হয়েছে; ২৩-Nov morning report, ২৩-Nov Nightly Rotation Backtest report, Failure & Lessons Register এবং NSE 200-session semantic audit পুনরায় পরীক্ষা করা হয়েছে।
- PASS byte-integrity কাজ পুনরাবৃত্তি করা হয়নি; Run #420 ও Run #409-এর বিদ্যমান artifact পুনর্ব্যবহার করা হয়েছে।
- **Run #420:** ID `45202379089`, conclusion SUCCESS, job `137788955150`; elapsed 12m11s — 10-minute target অতিক্রম করেছে। Artifact ID `14833925413`, ZIP SHA-256 `693cb2d8f68cc38a56fd9c17140f6126e11bb1617d6b0fee9ad4d2de5264686d` (download করে পুনরায় hash মিলেছে)।
- Run #420 processed dataset SHA-256: `8d6c634ddbb442bd5003ec96f20fdac8f150b5775f451efd84eeb5262bc12f57`; 504,250 rows, 2,999 symbols, 200 date labels। কিন্তু semantic date audit-এ মাত্র 188 unique valid trading dates; 12টি holiday date আগের session-এর duplicate। 200-session acceptance NOT_MET।
- Run #409: ID `45282753297`, conclusion SUCCESS, job `138071166956`; elapsed 8m19s। Artifact ID `14870843264`, ZIP SHA-256 `462728add6a22efc8f76174b7578d559ac5f7f1d1ed72c1c8919c4ad6f4074d9` (download করে পুনরায় hash মিলেছে)। `latest_picks.csv` SHA-256 `5f451b59076912318d1f36e893dfeee8657ad378cc040111c66f650015ebea56`।
- Run #420 raw NSE files/per-file raw manifest retained হয়নি; processed hash raw-source provenance-এর বিকল্প নয়। নতুন NSE acquisition করা হয়নি; project ledger-এ NSE Terms of Use/source-use restriction এবং project-specific written permission অনুপস্থিতির বাধা নথিভুক্ত আছে।
- IMF EMDE persistence Run #1403 / ID `45220449039` FAILED; GCR-এর জন্য নতুন verified vintage-aligned panel নেই।

## 2. Market context — ২৩ নভেম্বরের শেষ session

Run #420-এর retained NSE market-context snapshot:
- NIFTY 50: 25,349.65, −1.75%
- NIFTY Bank: −3.17%
- NIFTY Midcap 100: −1.01%
- India VIX: 17.86, +3.11%
- FII/FPI net: +₹5,672.99 crore; DII net: −₹2,760.12 crore — এক দিনের snapshot মাত্র, পূর্ণ vintage-aligned flow history নয়।
- GDELT/RSS geo-news collection errors; geo article coverage শূন্য/UNKNOWN।

এটি দুর্বল risk backdrop-এর প্রমাণ, কিন্তু GCR score নয়। এক দিনের FII/DII snapshot দিয়ে capital-rotation boost দেওয়া হয়নি।

Official source endpoints/links:
- NSE 2026 holiday circular: https://nsearchives.nseindia.com/content/circulars/CMTR71775.pdf
- ২৩-Nov NSE full bhavdata source URL (archive provenance incomplete): https://nsearchives.nseindia.com/products/content/sec_bhavdata_full_23112026.csv
- NSE market data: https://www.nseindia.com/market-data/live-equity-market
- NSE index tracker: https://www.nseindia.com/market-data/indices-watch

## 3. Three engine status — strictly separate

| Engine | Status | Decision |
|---|---|---|
| A — V11.4 Historical Behavioural Selector | PARTIAL / NOT_VALIDATED | 188 unique sessions only; frozen ranking trained on defective holiday/forward-label pipeline. Historical diagnostics exploratory only; no accepted probability/ranking boost. |
| B — V11.3 Cost-aware Trade Replay | UNKNOWN / NOT_AUTHORIZED | User-approved entry/exit/stop/circuit/cost assumptions and independently reconciled replay absent. |
| C — Global Capital Rotation | UNKNOWN / BLOCKED | Geo/news feed errors, one-day FII/DII only, timestamp/vintage-aligned macro-sector-stock matured outcomes absent. No GCR boost. |

### A. Target-wise historical capture — exploratory shadow audit only

Run #409-এর `strict_30_matured_cutoff_audit.json`: 30 matured historical cutoff; প্রতিটি selector-এর 150 picks (প্রতি cutoff Top-5 outside frozen production Top-30)। এগুলি retrospective exploratory labels, prospective performance নয়; মূল frozen model-এর label/session contamination-এর কারণে NOT_ACCEPTED।

| Target | CURRENT_WINNER_PROB | P10_P20_MEAN | সিদ্ধান্ত |
|---|---:|---:|---|
| +2% | UNKNOWN | UNKNOWN | target-specific accepted audit নেই |
| +5% H+1 | 40/150 = 26.67%; FP 110 | 31/150 = 20.67%; FP 119 | exploratory only |
| +10% H+3 | 31/150 = 20.67%; FP 119 | 33/150 = 22.00%; FP 117 | exploratory only |
| +15% | UNKNOWN | UNKNOWN | target-specific accepted audit নেই |
| +20% H+5 | 18/150 = 12.00%; FP 132 | 14/150 = 9.33%; FP 136 | exploratory only |

Denominator = selector-এর 150 evaluated shadow picks; sample = 30 cutoffs × 5 picks per selector. These are historical target-hit labels, not profitable trade returns, executable win rate, or cost-adjusted performance. +2%/+15% সংখ্যা অনুমান বা extrapolate করা হয়নি।

Main V11.4 full Top-30 metrics ও recall এখনও NOT_VALIDATED: 96 valid cutoffs post-hoc diagnostics হলেও training/ranking label contamination এবং 188/200 session defect আছে। Full-universe recall denominator independently reconciled নয়।

### Target-wise historical Best-3 stocks

| Target | Verified Best-3 |
|---|---|
| +2% | UNKNOWN — যোগ্য stock <3 |
| +5% | UNKNOWN — যোগ্য stock <3 |
| +10% | UNKNOWN — যোগ্য stock <3 |
| +15% | UNKNOWN — যোগ্য stock <3 |
| +20% | UNKNOWN — যোগ্য stock <3 |

Stock-level independently verified matured target counts, sample sizes, stable hit rates ও point-in-time survivorship/leakage checks ছাড়া কোনো historical leader ঘোষণা করা হয়নি। Historical Best-3 ও current candidate list আলাদা; আজ কোনো Best-3 rank নেই।

## 4. Current candidate decision — qualified = 0

Run #420 `final_selection_status.json`:
- universe candidates: 2,999
- provisional Top-30: 30
- provisional Top-10: 10
- provisional Top-3: 3
- final state: `PROVISIONAL_ONLY_FINAL_SELECTION_BLOCKED`
- blockers: `RISK_GEO_NOT_AVAILABLE`, `LIVE_INTRADAY_1M_FEED_MISSING`

Provisional Top-3 are not alerts:
1. **SREEL** — last retained row 14-Sep-2026, close ₹333.27; stale for 25-Nov decision.
2. **RELCHEMQ** — 23-Nov close ₹126.71, EMA20 ₹119.64, EMA50 ₹117.50, RVOL20 1.75×, 20-session return +19.18%; turnover only ₹28.48 lakh in the retained row; no verified live confirmation and final readiness blocked.
3. **SAB** — 23-Nov close ₹188.55, only 547 shares / ₹1.08 lakh turnover; history depth 35, EARLY/DEVELOPING; liquidity and sample insufficient.

### 23-Nov shadow selector picks — screened, not qualified

Seven unique symbols across two exploratory selectors: BI, KDDL, ONIXSOLAR, SALASAR, SHALPAINTS, SHARDUL, UFBL. 23-Nov retained processed rows and security-master mappings:

| Symbol | ISIN | 23-Nov close | Volume / turnover | Key exclusion |
|---|---|---:|---:|---|
| BI | INE986A01012 | ₹76.22 | 3,834 / ₹2.92 lakh | RVOL 0.03×; illiquid |
| KDDL | INE291D01011 | ₹4,604.00 | 79,404 / ₹36.95 crore | RVOL 0.62×; below average volume; no fresh verified catalyst |
| ONIXSOLAR | INE173M01012 | ₹252.80 | 376,378 / ₹9.46 crore | below EMA20/EMA50; 5d −3.82%, 20d −15.27% |
| SALASAR | INE170V01027 | ₹5.22 | 4,279,283 / ₹2.25 crore | below established ₹50 base-universe floor; RVOL 0.47× |
| SHALPAINTS | INE849C01026 | ₹103.97 | 8,956,197 / ₹98.11 crore | 20d +65.95%, RVOL 6.89×; intraday high ₹116.80 then close ₹103.97 — extended/large reversal risk |
| SHARDUL | INE037B01020 | ₹46.71 | 1,744 / ₹0.82 lakh | below ₹50 floor and illiquid |
| UFBL | INE382M01027 | ₹531.25 | 38,712 / ₹2.05 crore | RVOL 0.25×; close below EMA20/EMA50; 20d −20.32% |

These rows are from the retained processed artifact, not independently re-fetched raw NSE files. Therefore all are screening diagnostics, not qualified candidates. No target price, horizon, stop, or invalidation order is issued for any of them.

## 5. Prior comparable day / outcome maturity

- ২৩-Nov morning report had one observation-only candidate, WELSPUNLIV. Its 23-Nov H+1 outcome: +2% intraday high-touch HIT; close-to-close +0.74% MISS; +5% H+1 MISS; adverse excursion −2.52%. High-touch success is not a profitable trade result.
- ২৩-Nov cutoff-এর seven-symbol shadow cohort-এর H+1 is **PENDING until 25-Nov close**; H+3 = 27-Nov close; H+5 = 01-Dec close. 24-Nov is excluded as exchange holiday.
- No immature 23-Nov cohort result is called success/failure.

## 6. Daily Failure Analysis & Missed-Winner Audit

২০-Nov cutoff-এর 1,032-symbol base universe (close >₹50 and prior 20 valid sessions' average volume >200,000):
- +2% H+1 high-touch: 261 universe winners; WELSPUNLIV one hit; 260 missed.
- +5% H+1 high-touch: 41 universe winners; zero selected hits; 41 missed.
- Full candidate-decision export is missing; the remaining 255 +2% and 35 +5% cases have no defensible individual exclusion reason and remain UNKNOWN.

Representative missed-winner incidents (retrospective outcome; not prospective picks):
| Symbol | 23-Nov H+1 high / close / adverse | Cutoff-time reason classification |
|---|---|---|
| HINDOILEXP | +7.51% / +3.33% / −2.22% | SUPPORTED risk trade-off: RVOL 0.39× and prior ASM/high-valuation warning had been flagged; causal proof absent |
| SHALPAINTS | +19.89% / +6.72% / +5.67% | HYPOTHESIS: cutoff RVOL 0.08× may have triggered volume/liquidity exclusion; exact decision row absent |
| HITECH | +16.36% / +13.51% / +6.04% | HYPOTHESIS: weak EMA/trend and RVOL 0.56× |
| ITI | +15.96% / +12.41% / +0.72% | HYPOTHESIS: negative 5d trend, below EMA20/EMA50, RVOL 0.04× |
| THOMASCOOK | +14.68% / +12.85% / +1.17% | UNKNOWN — no row-level decision reason |
| AJMERA | +13.72% / +8.93% / −2.47% | UNKNOWN — high RVOL 9.81×, but exact exclusion/catalyst decision missing |

These are six examples only; not the complete 260/41 missed-winner audit. No hindsight-only catalyst is converted into a predictive signal.

## 7. EVERY-MISTAKE Learning Register — today

New immutable lessons:
- **PW-LSN-20261124-001 — audit runtime exceeded target:** Run #420 took 12m11s, exceeding the 10-minute goal. Confirmed operational issue. Research action: split offline session-spine, label, and candidate-denominator audits into independent bounded jobs; do not rerun completed PASS steps.
- **PW-LSN-20261124-002 — readiness/source-health fail-closed:** final selection blocked by GEO missing and live NSE 1m quote HTTP 403. Confirmed source-access/readiness gap, not a proven stock-ranking error. Research action: retain per-source status/timestamp/error and require independent source-health acceptance before any candidate can be qualified.
- **PW-LSN-20261124-003 — high-touch vs close outcome divergence:** WELSPUNLIV reached +2% intraday high but closed only +0.74%; +5% H+1 missed. Confirmed label distinction. Research action: keep high-touch, close-to-close, adverse excursion and executable trade return as separate outcomes.

Existing lessons updated, not duplicated:
- PW-LSN-20261123-001 holiday duplicate session defect remains verified: 188/200 unique sessions.
- PW-LSN-20261123-002 timestamp timezone contract remains UNKNOWN.
- PW-LSN-20261123-003 maturity calendar corrected: for 23-Nov cutoff H+1=25-Nov, H+3=27-Nov, H+5=01-Dec.
- PW-LSN-20261123-004 to -009 missed-winner incident evidence carried forward; causal hypotheses remain bounded.
- PW-LSN-20261123-010 full-universe candidate decision export gap remains OPEN; 255/+2 and 35/+5 residual cases UNKNOWN.

### আজকের শিক্ষা → গবেষণায় সংযোজন → পরবর্তী যাচাই
1. Holiday-aware 200 unique-session spine and DATE1/manifest parity; no new NSE acquisition without permitted zero-cost archival route.
2. Full 1,032-row point-in-time candidate decision ledger with one decision/reason per symbol.
3. Source-health gate for GEO and live quote; HTTP 403 remains BLOCKED, not a fallback PASS.
4. Separate high-touch, close-to-close, adverse and executable-return labels.
5. Run audit jobs in <10-minute bounded parts; no production threshold/selector changes.

## 8. Acceptance and invariants

- Artifact ZIP byte/hash verification: PASS for existing Run #420 and #409 archives.
- 200-session semantic coverage: NOT_ACCEPTED (188 unique sessions only).
- V11.4 historical metrics: NOT_VALIDATED.
- Best-3 lists: UNKNOWN.
- V11.3 cost-aware replay: UNKNOWN / NOT_AUTHORIZED.
- GCR: UNKNOWN / BLOCKED.
- Current qualified candidates: 0.
- Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2.0 unchanged.
- No paid API, no synthetic data, no guessed mapping, no fabricated timestamp, no new NSE download, no workflow dispatch, no production modification.
- UNKNOWN is never PASS.

## 9. Evidence links
- [Run #420](https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/45202379089)
- [Run #409](https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/45282753297)
- [23-Nov Nightly Rotation Backtest report](NIGHTLY_ROTATION_BACKTEST_RESEARCH_REVIEW_20261123.md)
- [23-Nov Failure & Lessons Register](FAILURE_LESSONS_LEARNED_20261123.md)
- [NSE 200-session semantic audit](NSE_200_SESSION_ARCHIVE_SEMANTIC_DATE_AUDIT_20261123.md)
