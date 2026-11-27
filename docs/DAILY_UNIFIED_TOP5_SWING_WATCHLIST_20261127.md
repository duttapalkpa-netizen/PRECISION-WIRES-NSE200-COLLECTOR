# PRECISION-WIRES V11.3 — India Pre-Market Unified Top-5 Alert
## ২৭ নভেম্বর ২০২৬

**রিপোর্ট as-of:** 27-Nov-2026 08:49:08 IST  
**Selection cutoff:** 26-Nov-2026 NSE close (15:30 IST; source-level EOD receipt not captured)  
**পরবর্তী NSE equity session:** 27-Nov-2026 — official 2026 holiday circular-এ 27-Nov holiday নেই; 24-Nov holiday ছিল।  
**Research release:** QUALIFIED 0/5 · PROVISIONAL 0 · UNFILLED 5/5

## 1. সিদ্ধান্ত

আজ পাঁচটি ranked slot রাখা হয়েছে, কিন্তু কোনো stock-কে QUALIFIED বা PROVISIONAL বলা হয়নি। 26-Nov cutoff-এর জন্য run 412-তে model raw leads পাওয়া গেলেও official fresh close/time, full price-volume/relative-strength/sector, liquidity, catalyst timestamp ও current risk fields একই cutoff-এ independently reconcile হয়নি। stale/secondary prices দিয়ে target band বা probability তৈরি করা হয়নি।

এটি “বাজারে কোনো সম্ভাবনা নেই” এমন সিদ্ধান্ত নয়; এটি যাচাইকৃত evidence admission না-পাওয়ার সিদ্ধান্ত। Watchlist research-only; buy instruction বা return guarantee নয়।

## 2. Continuity preflight ও reused evidence

- Master Continuity Ledger read-back: current main-branch ledger শেষ হয়েছে GCR Continuation 273-এ; Macro-Geo P0 6/8, strict hard gate BLOCKED, candidate_release_allowed=false; overall GCR NOT_COMPUTABLE/NOT_CERTIFIED। C273-এর MEX evidence reconciliation ও 30-Nov GEO release trigger handover পুনরায় চালানো হয়নি।
- 26-Nov Daily Unified Top-5 report, 26-Nov Failure & Lessons Log, 25-Nov Nightly Rotation Review এবং retained archive/run evidence পড়া হয়েছে। পূর্বে PASS হওয়া ZIP checks পুনরায় করা হয়নি।
- **Run #412**: [Audit-only Prospective Watchlist Tracking](https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/45890145641), job 140150511665, SUCCESS; 7m38s (10-minute target-এর মধ্যে); head `f587c0fdf58bf971e47ca27cafaac71733cc6d0d`.
- Artifact **15151761186**, [download/reference](https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/45890145641/artifacts/15151761186), 17 files. GitHub digest এবং independent downloaded ZIP SHA-256 দুটিই:
  `a5cd5ed868a3f66d9ea0cd43ca03b7fea2e5cd4ebc3b5f83e3c28fc6fdd3ca5a`.
- `qa_report.json`: status PASS, 200 raw-file labels, 200 processed dates, 3,009 symbols, 100% delivery coverage. কিন্তু artifact-এ raw NSE ZIP/per-file acquisition manifest, requested-date বনাম internal DATE1 reconciliation এবং complete point-in-time decision ledger নেই। পূর্বের semantic audit-এ 187 বনাম 188 unique content-session discrepancy-ও অমীমাংসিত। তাই 200 distinct valid sessions, current EOD provenance এবং final-selection readiness **NOT_ACCEPTED**।
- `reproducibility_check.json`: একই input hash `91b611f0e42f5bdf01b7a82fb7834281bda0374eb9851a62fb45869e77a77b6f`-এ retrospective outputs byte-for-byte reproducible। এটি reproducibility PASS মাত্র; label/session/data correctness PASS নয়।

## 3. Next-Session Top-5 Prospective Stock Picks

**27-Nov-2026-এর জন্য Qualified = 0/5; Provisional = 0/5.**

| Rank | NSE symbol / company | Exchange / ISIN | Official reference price/time | 2/5/10/15/20% scenarios | Horizon | Decision / blocker |
|---:|---|---|---|---|---|---|
| 1 | UNFILLED | — | NOT_VERIFIED | NOT_CALCULATED | UNKNOWN | fresh official close/time, trend/RS, sector, liquidity, catalyst ও risk একসঙ্গে verified নয় |
| 2 | UNFILLED | — | NOT_VERIFIED | NOT_CALCULATED | UNKNOWN | একই hard-gate evidence gap |
| 3 | UNFILLED | — | NOT_VERIFIED | NOT_CALCULATED | UNKNOWN | একই hard-gate evidence gap |
| 4 | UNFILLED | — | NOT_VERIFIED | NOT_CALCULATED | UNKNOWN | একই hard-gate evidence gap |
| 5 | UNFILLED | — | NOT_VERIFIED | NOT_CALCULATED | UNKNOWN | একই hard-gate evidence gap |

কোনো verified reference price নেই; তাই target-price arithmetic, probability, invalidation price বা stop প্রকাশ করা হয়নি। User-approved entry/exit/stop rule অনুমান করা হয়নি।

### 3.1 Run #412 raw model leads — candidate list নয়

`latest_picks.csv`-এ 26-Nov cutoff-এর 10 signal rows / 7 unique symbols। `SELECTION_SCORE_VALUE` percentile rank, calibrated probability নয়।

| Model output | Rank | Symbol | Score (percentile) | Identity / official evidence / blocker |
|---|---:|---|---:|---|
| CURRENT_WINNER_PROB | 1 | SHALPAINTS | 99.6732 | Shalimar Paints Ltd, INE849C01026; NSE quote search result সর্বশেষ 20-Nov close ₹97.42—26-Nov-এর জন্য stale; একই NSE page-এ 8 quarters loss-making, encumbered share >50%, impact cost 0.71। |
| CURRENT_WINNER_PROB | 2 | SAKUMA | 99.3101 | Sakuma Exports Ltd, INE190H01024; NSE filing 25-Nov 16:40 IST-এ 65 কোটি শেয়ারের proposed preferential issue প্রত্যাহার এবং 28-Nov EGM বাতিল জানায়; subscription commitment না-পাওয়ার কথা বলা হয়েছে। Current close/volume/RS নেই। |
| CURRENT_WINNER_PROB | 3 | EBIX | 99.2738 | Symbol-to-company/ISIN mapping এই audit-এ official NSE source দিয়ে independently verified নয়; price/time/liquidity/catalyst অনুপস্থিত। |
| CURRENT_WINNER_PROB | 4 | NGIL | 99.0196 | Nakoda Group of Industries Ltd, INE236Y01012; NSE iXBRL identity verified, কিন্তু 26-Nov official close/time ও current price-volume/risk snapshot নেই। |
| CURRENT_WINNER_PROB | 5 | ARIS | 98.9833 | Arisinfra Solutions Ltd, INE0H9P01028; NSE identity verified; 26-Nov official price/volume/RS/liquidity package নেই। 26-Nov filing-এ 25-Nov court-convened meeting-এর তথ্য আছে, কিন্তু সেটি একা positive price catalyst প্রমাণ করে না। |
| P10_P20_MEAN | 1 | SAKUMA | 99.4553 | উপরের একই official filing/event risk; qualified নয়। |
| P10_P20_MEAN | 2 | SHALPAINTS | 99.3646 | উপরের একই stale quote ও risk caveat; qualified নয়। |
| P10_P20_MEAN | 3 | ONIXSOLAR | 99.3101 | Onix Solar Energy Ltd, INE173M01012; NSE ASM page-এ LTASM-I; surveillance hard gate-এ qualified নয়। |
| P10_P20_MEAN | 4 | ARIS | 99.2919 | উপরের একই identity/price evidence gap; qualified নয়। |
| P10_P20_MEAN | 5 | AIROLAM | 98.9833 | Airo Lam Ltd, INE801L01010; NSE ASM page-এ STASM-I; surveillance hard gate-এ qualified নয়। |

**Attribution:** এগুলি audit-branch model output; production selector admission নয়। Seven unique symbols-এর মধ্যে identity ও risk checks আংশিক করা গেছে, কিন্তু কোনো নামের জন্য সব hard gates পূর্ণ হয়নি। 26-Nov official quote pages retrieval surface-এ JavaScript shell/placeholder দেখিয়েছে; secondary price pages থেকে official price হিসেবে কোনো সংখ্যা নেওয়া হয়নি।

## 4. Engine scorecard

| Engine | Status | Evidence / limitation |
|---|---|---|
| A — V11.4 Historical Behavioural Selector | EXPLORATORY ONLY / NOT_ACCEPTED | Run #412 Top-30 target diagnostics আছে; কিন্তু 200-session semantic spine, source manifest, calendar-aware maturity ও full-universe denominator unresolved |
| B — V11.3 Cost-aware Trade Replay | UNKNOWN / NOT_AUTHORIZED | User-approved entry/exit/stop/circuit/cost/position assumptions এবং independently reconciled executable replay নেই |
| C — Global Capital Rotation | UNKNOWN / BLOCKED | Timestamp/vintage-aligned macro-sector-stock panel ও matured outcomes নেই; C273 hard gate BLOCKED; কোনো GCR boost নয় |

## 5. Alert Section 1 — Target-wise capture performance

Run #412 `walk_forward_metrics.json` থেকে Top-30 candidate **signal-row** diagnostics fresh গণনা। এগুলি unique stocks নয়, full-universe recall denominator নয়, এবং accepted performance নয়।

| Target | Horizon | TP / matured evaluated rows | Hit / precision | FP | Recall | Status |
|---|---|---:|---:|---:|---:|---|
| +2% | H+1 | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | target series absent |
| +5% | H+1 | 942 / 2,977 | 31.64% | 2,035 | 4.02% | EXPLORATORY / NOT_ACCEPTED |
| +10% | H+3 | 617 / 2,897 | 21.30% | 2,280 | 3.57% | EXPLORATORY / NOT_ACCEPTED |
| +15% | H+5 | 374 / 2,830 | 13.22% | 2,456 | 3.05% | EXPLORATORY / NOT_ACCEPTED |
| +20% | H+5 | 189 / 2,830 | 6.68% | 2,641 | 3.42% | EXPLORATORY / NOT_ACCEPTED |

এই rates high-touch label/Top-30 selector diagnostics; executable trade win বা profitable return নয়। একই signal একাধিক target-এ hit করতে পারে; target rows overlap করে। +2% গণনা করা যায়নি।

### Comparable-day caveat

Run #411 → #412 raw diagnostic পরিবর্তন: +5% 31.98% → 31.64%; +10% 21.58% → 21.30%; +15% 13.41% → 13.22%; +20% 6.86% → 6.68%। Input SHA বদলেছে (`25cfbd7f97c2a27c474b3bd97335ae149ef59ac185f52dd65d565d9b69fb2378` বনাম `91b611f0e42f5bdf01b7a82fb7834281bda0374eb9851a62fb45869e77a77b6f`); session/label defects-ও অমীমাংসিত। তাই এগুলি NOT_COMPARABLE raw drift, performance improvement/degradation নয়।

## 6. Alert Section 2 — Target-wise historical Best Three

+2%, +5%, +10%, +15%, +20% — প্রতিটি target-এ **<3 / UNKNOWN**। Target-wise independently verified matured symbol outcomes, unique-symbol evaluated n, latest matured cutoff ও exchange/ISIN reconciliation নেই। Aggregate Top-30 metrics থেকে stock-wise winner rank বানানো হয়নি। Historical leaders prospective list থেকে পৃথক থাকবে; survivorship/future-leakage control গ্রহণযোগ্য না হওয়া পর্যন্ত ranking বন্ধ।

## 7. Alert Section 3 — Failure Analysis & Missed-Winner Audit

### 7.1 Previous selected cohorts — symbol ও signal-row পৃথক

| Cutoff | Signal rows | Unique symbols | Run #412 tracker state | Official-session adjudication |
|---|---:|---:|---|---|
| 23-Nov | 10 | 7 | T1=10 rows ও T3=9 rows `MATURED=True`; OUTCOME_LAST_DATE সব blank | H+1=25-Nov; H+3=27-Nov; H+5=01-Dec। 26-Nov run-এ H+3 mature দেখানো premature; T1/T3 values NOT_ACCEPTED |
| 24-Nov | 10 | 9 | T1=10 rows `MATURED=True`; OUTCOME_LAST_DATE blank | NSE holiday; invalid cutoff, বাদ |
| 25-Nov | 10 | 7 | T1=10 rows `MATURED=True`; OUTCOME_LAST_DATE blank | H+1=26-Nov, কিন্তু exact outcome-end date ও official raw row link নেই; PENDING / NOT_VERIFIED |
| 26-Nov | 10 | 7 | T1/T3/T5 সব immature | H+1=27-Nov close; pre-market-এ PENDING |

Run #412 ledger-এ 23-Nov cohort-এর H+3 maturity flag 26-Nov artifact তৈরির আগেই TRUE, যদিও official NSE calendar অনুযায়ী H+3=27-Nov। তাই tracker-এ holiday/session semantics এখনও ভুল; high-touch values-কে matured verified outcome হিসেবে ব্যবহার করা যাবে না।

### 7.2 Full-universe missed winners

**UNKNOWN / BLOCKED — “missed winner নেই” বলা হচ্ছে না।** 26-Nov cutoff-এর সম্পূর্ণ eligible NSE equity universe-এর symbol-by-symbol point-in-time inclusion/exclusion + filter trace এবং reconciled official 26-Nov EOD high/close/corporate-action rows এই artifact-এ নেই। ফলে 27-Nov H+1, 01-Dec H+3, 03-Dec H+5 outcomes এখনো mature হয়নি; আগের cutoffs-এরও accepted full-universe outcome source অনুপস্থিত। Unique symbol এবং signal-row missed-winner count প্রকাশ করা যাচ্ছে না।

### 7.3 Root-cause classification

| Issue | Class | Evidence / impact |
|---|---|---|
| Holiday-aware tracker / OUTCOME_LAST_DATE defect | VERIFIED | Run #412-এ 23-Nov H+3 premature matured flag; 23-Nov ও 25-Nov rows-এ outcome-end date blank। Individual stock return impact UNKNOWN। |
| Raw selector percentile থেকে final risk-qualified admission gap | VERIFIED (schema/code-level) | latest_picks-এ percentile fields; current official price/time, surveillance, liquidity, catalyst timestamp/sector gate নেই। Predictive impact UNKNOWN। |
| SAKUMA event risk | VERIFIED filing fact | 25-Nov official filing-এ proposed preferential issue withdrawal; এটি positive catalyst নয়। Future price impact অনুমান করা হয়নি। |
| AIROLAM / ONIXSOLAR surveillance | VERIFIED official NSE ASM listing | AIROLAM STASM-I; ONIXSOLAR LTASM-I; candidate admission blocked by risk gate। |
| Full-universe missed-winner attribution / CORE-672 filter failure | UNKNOWN | canonical point-in-time decision trace ও reconciled universe outcomes অনুপস্থিত; কোনো filter failure অনুমান নয়। |

## 8. Data universe, exclusions ও limitations

- QA summary-তে 3,009 symbols; 100 cutoff × Top-30 = 3,000 candidate signal rows। এটি accepted eligible-universe denominator নয়।
- 26-Nov latest model output: 10 rows / 7 unique symbols। Duplicate selector rows unique stock count-এ একবার, signal-row analysis-এ পৃথক।
- Exclusions/blockers: missing raw source manifest and exact official EOD retrieval receipt; unresolved 187/188 valid-session discrepancy; no accepted 200-session spine; no official price/time package for raw leads; ASM flags; SAKUMA event risk; EBIX identity mapping unverified; no canonical full-universe decision ledger.
- Intraday/live feed: এই run-এ usable verified live feed capture হয়নি; stale quote-কে live বলা হয়নি।
- 20% target: independently sufficient target-specific sample/consistency নেই; UNVERIFIED / LOW EVIDENCE. No probability supplied.

## 9. Alert Section 4 — EVERY-MISTAKE Learning & Research Register

নতুন lesson তৈরি করা হয়নি। Existing immutable IDs-তে evidence append করা হয়েছে:

- **PW-LSN-20261125-001 — holiday/session-aware maturity:** Run #412-এ 23-Nov T3 premature maturity এবং OUTCOME_LAST_DATE blank; 25-Nov T1 maturity date-ও blank। OPEN.
- **PW-LSN-20261126-001 — raw model percentile is not risk-qualified admission:** 26-Nov latest_picks-এর 7 unique leads, official identity/risk evidence gaps, AIROLAM/ONIXSOLAR ASM flags এবং SAKUMA 25-Nov withdrawal filing append। Code/schema gap VERIFIED; predictive impact UNKNOWN। OPEN.
- Existing forward-label, H+5 JSON/CSV parity, raw-source provenance, full-universe ledger ও high-touch/close/executable separation lessons OPEN; duplicate IDs তৈরি হয়নি।

### পরবর্তী bounded verification tests (প্রতিটি ≤10 মিনিট)

1. `calendar_aware_tracker_regression.json` — 23-Nov→25-Nov/27-Nov/01-Dec; holiday row reject; প্রতিটি horizon-এ exact OUTCOME_LAST_DATE বাধ্যতামূলক।
2. `point_in_time_decision_ledger_audit.json` — একই cutoff-এর প্রতিটি eligible symbol-এর inclusion/exclusion, rank, filter state, source timestamp ও code/config hash।
3. `universe_missed_winner_reconciliation.json` — official session calendar, raw high/close/corporate action ও unique-symbol বনাম signal-row reconciliation।
4. `missed_winner_root_cause_audit.json` — cutoff-only evidence; decision trace না থাকলে CORE-672 attribution UNKNOWN।
5. `prospective_risk_gate_admission_audit.json` — 26-Nov raw leads বনাম official symbol/ISIN, fresh quote, price-volume, delivery, sector, liquidity, catalyst timestamp ও ASM/GSM/price-band/margin fields।

## 10. Sources & evidence

- NSE official 2026 Capital Market holiday circular (12-Dec-2025): https://nsearchives.nseindia.com/content/circulars/CMTR71775.pdf
- NSE official ASM reports: https://www.nseindia.in/reports/asm
- NSE official corporate filings dashboard: https://betanseapi.nseindia.com/companies-listing/corporate-filings-application
- NSE official SHALPAINTS quote (latest accessible indexed data was 20-Nov-2026): https://www.nseindia.in/get-quote/equity/SHALPAINTS/Shalimar-Paints-Limited
- NSE official SAKUMA board outcome PDF: https://nsearchives.nseindia.in/corporate/SAKUMA_25112026164017_Outcome_BM_25112026.pdf
- NSE official identity/filing references: SHALPAINTS https://nsearchives.nseindia.com/corporate/ixbrl/INTEGRATED_FILING_INDAS_205696_28102026182219_iXBRL_WEB.html ; SAKUMA https://nsearchives.nseindia.com/corporate/ixbrl/INTEGRATED_FILING_INDAS_164600_30052026143258_iXBRL_WEB.html ; NGIL https://nsearchives.nseindia.com/corporate/ixbrl/INTEGRATED_FILING_INDAS_207250_30102026165131_iXBRL_WEB.html ; ARIS https://nsearchives.nseindia.com/corporate/ixbrl/INTEGRATED_FILING_INDAS_156469_08052026234814_iXBRL_WEB.html ; AIROLAM https://nsearchives.nseindia.com/corporate/ixbrl/INTEGRATED_FILING_INDAS_162155_27052026184851_iXBRL_WEB.html
- Run #412: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/45890145641
- Run #412 artifact 15151761186: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/45890145641/artifacts/15151761186

## 11. আজকের শিক্ষা → গবেষণায় সংযোজন → পরবর্তী যাচাই

**আজকের শিক্ষা:** QA PASS বা percentile-ranked raw lead নিজে থেকে valid session, matured outcome বা risk-qualified stock প্রমাণ করে না। 23-Nov H+3 premature maturity এবং missing OUTCOME_LAST_DATE আবারও tracker defect নিশ্চিত করেছে।

**গবেষণায় সংযোজন:** PW-LSN-20261125-001 ও PW-LSN-20261126-001-এ Run #412 evidence append; নতুন predictive lesson নয়।

**পরবর্তী যাচাই:** calendar-aware tracker regression → point-in-time decision ledger → full-universe missed-winner reconciliation → prospective risk-gate audit। Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E ও IPO-PLX V2.0 অপরিবর্তিত থাকবে। ₹0; free official sources only; UNKNOWN never PASS.
