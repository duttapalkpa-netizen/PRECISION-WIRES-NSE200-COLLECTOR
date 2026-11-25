# PRECISION-WIRES V11.3 — ২৫ নভেম্বর ২০২৬
## India Pre-Market Unified Top-5 Swing Watchlist

**সময়:** ২৫-Nov-2026, 08:45 IST  
**সর্বশেষ বৈধ market-data cutoff:** ২৩-Nov-2026 close  
**২৪-Nov-2026:** NSE Capital Market holiday — Prakash Gurpurb Sri Guru Nanak Dev  
**আজকের qualified candidate:** ০ / ৫

## Executive decision

আজ কোনো qualified swing candidate প্রকাশ করা হয়নি। ২৩-Nov-এর processed dataset-এ source/raw-manifest provenance অসম্পূর্ণ, ২০০ date-label-এর মধ্যে মাত্র ১৮৭টি unique content session, এবং final readiness এখনও blocked। ২৪-Nov holiday-কে prospective tracker ভুলভাবে next row/session হিসেবে ব্যবহার করেছে—তাই তার apparent H+1 outcome গ্রহণযোগ্য নয়। ২৫-Nov-এর market open-এর আগে আজকের intraday/1-minute confirmation-ও নেই।

এটি “কোনো stock উঠবে না” এমন সিদ্ধান্ত নয়; এটি প্রমাণের ঘাটতিতে alert release না করার সিদ্ধান্ত। Buy instruction নয়, profit guarantee নয়।

## 1. Preflight — ledger, reports, archive, runs ও hashes

- Current Master Continuity Ledger C73 পর্যন্ত পুনরায় পড়া হয়েছে; ২৪-Nov Daily Report ও Failure & Lessons Register, C72/C73 reports, সংশ্লিষ্ট archive ও workflow evidence পরীক্ষা করা হয়েছে।
- আগের accepted byte/hash checks পুনরাবৃত্তি করা হয়নি।
- **Run #410 — Audit-only Prospective Watchlist Tracking:** run ID 45490518576; conclusion SUCCESS; head commit ab7287e42921629a89977e551c2ed7410c6ad07c; artifact ID 14966627305; artifact ZIP SHA-256 6b1673af895214ae982fb445a62d5536dd2960eb062dc310b85f955b01c8af16. Artifact download করে SHA-256 independently মিলেছে। Run window 9m52s; এটি audit-only, final production selector run নয়।
- Run #410 artifact-এর QA JSON-এ 200 raw files / 200 sessions / 200 processed dates PASS লেখা; কিন্তু C72/C70 semantic audit-এ ২০০ label-এর মধ্যে ১৮৭টি unique content session এবং ১৩টি duplicate-content holiday pair পাওয়া গেছে। QA PASS session-semantic acceptance নয়।
- **Run #421:** ID 45422367928; artifact 14936656169; ZIP SHA-256 d57374c50a8b8e2fe5710fd57660225ea59a2beffd639cb9e83b77e734499954. এটি আগেই independent read-back করা হয়েছে; runtime 12m06s, 10-minute target অতিক্রম করেছে। পুনরায় download/run করা হয়নি।
- Run #410 reproducibility check-এর byte-for-byte PASS শুধু retrospective output reproducibility; এটি data correctness বা prospective validation নয়।
- Run #410 log: LIVE_CUTOFF=2026-11-24, PICKS=10, LABELS=NOT_READ FROM_FUTURE. ২৪-Nov official NSE holiday হওয়ায় ওই cutoff-এর ১০টি row / ৯টি unique symbol current candidate হিসেবে ব্যবহার করা হয়নি।
- ২৩-Nov cutoff-এর ১০টি prospective row / ৭টি unique symbol: BI, KDDL, ONIXSOLAR, SALASAR, SHALPAINTS, SHARDUL, UFBL. Tracker-এ MATURED_T1=True ও T1_HIGH_PCT লেখা হলেও OUTCOME_LAST_DATE ফাঁকা; ২৪-Nov holiday-কে পরের row হিসেবে গণনা করা হয়েছে। প্রকৃত H+1 হলো ২৫-Nov close-এর পরে।
- C72 অনুযায়ী latest final selection status PROVISIONAL_ONLY_FINAL_SELECTION_BLOCKED; live 1m source HTTP 403 / zero rows / zero symbols. ২৫-Nov-এর নতুন final selector run পাওয়া যায়নি।
- C73 export audit: inventory-bearing manifest-এ 821 entry (807 .dat, 12 .json, 1 .txt, 1 .html); Library snapshot-এ 292 .dat. Original ZIP/package provenance এবং manifest-to-payload exact mapping/hash reconciliation এখনও UNKNOWN/NOT_DONE. এই export task market candidate-এর বিকল্প evidence নয়।

Evidence:
- Run #410: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/45490518576
- Run #421: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/45422367928
- C72: docs/PRECISION_WIRES_CONTINUATION72_PRETASK_RECONCILIATION_AND_BLOCKER_DECISION_20261125.md
- C73: docs/PRECISION_WIRES_CONTINUATION73_EXPORT_PACKAGE_LIBRARY_INVENTORY_AUDIT_20261125.md

## 2. Market / official filing context

সর্বশেষ বৈধ NSE session ২৩-Nov-2026-এ NIFTY 50 25,349.65-এ −1.75%; NIFTY Bank −3.17%, NIFTY Metal −3.68%, আর NIFTY IT +1.69% ছিল। এটি risk-off backdrop, GCR signal নয়।

NSE-এর current corporate-filings page-এ ২৫-Nov তারিখে SRIT ও KDDL investor-meet updates, MKJEWELS press release, SETCO board-meeting intimation এবং ২৪-Nov-এ ASTERDM director/KMP change দেখা যাচ্ছে। ২৫-Nov ex-date corporate actions-এর মধ্যে BONLON rights, VRAJ interim dividend এবং ZEEL buyback আছে; ENRIN, RAJRATAN ও SATIN-এর board meetings তালিকাভুক্ত। এগুলিকে একা price-volume confirmation বা qualified catalyst ধরা হয়নি; মূল company filing, security mapping ও market reaction আলাদাভাবে যাচাই প্রয়োজন।

Official sources:
- NSE 2026 holiday circular: https://nsearchives.nseindia.com/content/circulars/CMTR71775.pdf
- NSE corporate filings: https://www.nseindia.com/companies-listing/corporate-filings-application?id=eqCorpAnnouncementsNav
- NSE 23-Nov market data context: https://www.nseindia.com/market-data/live-equity-market
- Reuters 23-Nov market recap: https://www.reuters.com/world/india/indian-shares-set-open-higher-foreign-inflows-ai-selloff-persists-2026-11-23/

## 3. Three engine status — strictly separate

| Engine | Status | সিদ্ধান্ত |
|---|---|---|
| A — V11.4 Historical Behavioural Selector | NOT_VALIDATED / exploratory only | ২০০-session semantic defect ও forward-label defect থাকায় কোনো production-grade performance বা ranking boost গ্রহণ নয় |
| B — V11.3 Cost-aware Trade Replay | UNKNOWN / NOT_AUTHORIZED | User-approved entry/exit/stop/circuit/cost assumptions ও independently reconciled replay নেই |
| C — Global Capital Rotation | UNKNOWN / BLOCKED | Macro/sector/stock vintage alignment ও matured outcomes নেই; geo feed/source blockers বহাল |

### A1. 100-cutoff Top-30 diagnostic — NOT_ACCEPTED

Run #410 artifact-এর walk_forward_metrics.json: 100 cutoff, 3,000 Top-30 candidate rows. Target-specific matured denominators আলাদা; নিচের সংখ্যাগুলি exploratory diagnostics, accepted metrics নয়।

| Target / horizon | Hits / matured n | Hit rate | False positives | Recall (exploratory) |
|---|---:|---:|---:|---:|
| +2% | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN |
| +5% H+1 | 958 / 2,977 | 32.18% | 2,019 | 4.08% |
| +10% H+3 | 628 / 2,892 | 21.72% | 2,264 | 3.61% |
| +15% H+5 | 381 / 2,824 | 13.49% | 2,443 | 3.08% |
| +20% H+5 | 196 / 2,824 | 6.94% | 2,628 | 3.52% |

95% CI এই metrics JSON-এ নেই। Recall/base-rate denominator-ও semantic session correction-এর পরে পুনরায় reconcile হয়নি। Code-level forward-label defect-এ shift(-1).rolling(h) ব্যবহৃত; H+3/H+5 exact forward window নয় এবং close outcome terminal T+h close নয়। ১৮৭ unique content sessions-এর কারণে সব হার NOT_ACCEPTED।

### A2. Strict 30-matured-cutoff shadow audit — exploratory only

Top 5 outside frozen Production Top-30; প্রতি selector-এ 150 picks। এটি full-universe recall নয়।

| Target | CURRENT hits / 150 | CURRENT FP | P10_P20 hits / 150 | P10_P20 FP |
|---|---:|---:|---:|---:|
| +2% | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN |
| +5% H+1 | 39 (26.00%) | 111 | 33 (22.00%) | 117 |
| +10% H+3 | 33 (22.00%) | 117 | 34 (22.67%) | 116 |
| +15% | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN |
| +20% H+5 | 18 (12.00%) | 132 | 13 (8.67%) | 137 |

Paired precision-delta 95% CI (P10_P20 minus CURRENT): +5% −4.00 percentage points [−10.00, +1.33]; +10% +0.67 pp [−4.67, +6.00]; +20% −3.33 pp [−8.00, +0.67]. কোনো target-এ promotion অনুমোদিত নয়।

### A3. Target-first +5% research experiment

একই ৩০-cutoff exploratory set-এ P5_H1_ONLY 46/150 = 30.67% (daily precision 95% CI 22.67–38.67%); P5_H1_EXHAUSTION_GUARDED 52/150 = 34.67% (95% CI 26.00–43.33%). এই idea আগেই exploratoryভাবে দেখা হয়েছিল; এটি clean confirmatory holdout নয়। অন্তত ২০টি, আদর্শভাবে ৩০টি নতুন matured prospective cutoff ছাড়া কোনো promotion নয়।

### Historical best-three

+2%, +5%, +10%, +15%, +20%—সব target-এ independently verified stock-level Best-3: UNKNOWN / যোগ্য stock <3. Per-symbol repeated sample অপর্যাপ্ত (এই +5% experiment-এ এক symbol-এর সর্বোচ্চ repeat count 5); অন্য target-এ নির্ভরযোগ্য stock-level sample export নেই। Survivorship/leakage-safe stable ranking প্রতিষ্ঠিত নয়। কোনো নাম জোর করে দেওয়া হয়নি।

## 4. Current candidate list

**Qualified candidate: ০.**

কোনো stock-এর target-price band, horizon বা stop scenario দেওয়া হয়নি, কারণ ২৩-Nov-এর last valid price/volume ও raw-source provenance candidate-level independently verified নয় এবং final release gate blocked। Run #410-এর ২৪-Nov cutoff picks holiday-date; সেগুলি candidate নয়। Provisional/shadow rank-কে qualified alert-এ উন্নীত করা হয়নি।

Universe reference: processed archive-এ 2,999 symbols / 200 date labels; semantic accepted unique sessions মাত্র 187. Exclusions: 13 holiday duplicate-content pairs, invalid 24-Nov cutoff picks, unresolved source/mapping provenance, blocked live 1m feed, unverified liquidity/circuit/news mapping. এটি accepted 200-session universe নয়।

## 5. Failure Analysis & Missed-Winner Audit

- ২৩-Nov cohort: ৭ unique symbols; valid H+1 outcome এখনো mature হয়নি, কারণ ২৪-Nov holiday এবং H+1 = ২৫-Nov close. 08:45 IST-এ matured outcomes = 0; false positives/successes = PENDING, not zero-performance.
- Run #410 tracker ভুলভাবে ওই ২৩-Nov cohort-এর T1 mature দেখিয়েছে; T1 outcome date blank. এই maturity label বাতিল।
- ২৪-Nov holiday cutoff-এর ৯ unique shadow picks বাতিল; কোনো winner/loser outcome label গ্রহণ নয়।
- Full-universe missed-winner counts ও কারণ: UNKNOWN, কারণ canonical point-in-time decision ledger এবং valid outcome date reconciliation অসম্পূর্ণ।
- Avoidable/unavoidable miss: UNKNOWN; hindsight-only catalyst explanation predictive lesson হিসেবে নেওয়া হয়নি।

## 6. আজকের শিক্ষা → গবেষণায় সংযোজন → পরবর্তী যাচাই

**নতুন immutable lesson: PW-LSN-20261125-001 — Prospective tracker holiday row-কে next trading session হিসেবে গণনা করে।**

- Evidence: Run #410 artifact 14966627305; watchlist_ledger.csv-তে ২৩-Nov cohort-এর MATURED_T1=True, T1_HIGH_PCT populated, OUTCOME_LAST_DATE blank; ২৪-Nov NSE holiday.
- Code evidence: audit/prospective-selector-tracking branch-এর prospective_watchlist_tracker.py, Git blob SHA-1 f28f7c752c4eaadeb5583f4434190a124a4910d9. outcome() symbol rows DATE দিয়ে sort করে পরের h row নেয়; official exchange-session calendar/holiday check নেই; H+1-এর জন্য outcome-last-date persist হয় না।
- Root cause: holiday/session validation omission CONFIRMED. নির্দিষ্ট T1_HIGH_PCT কতটা duplicate-content row থেকে এসেছে, সেটি per-row price audit ছাড়া আলাদা করে UNKNOWN.
- Prevention research: official holiday/session spine join; cutoff-এর পরের hটি distinct valid trading session না পাওয়া পর্যন্ত outcome immature; exact expected end-date ও OUTCOME_LAST_DATE বাধ্যতামূলক।
- Reproducible test: 23-Nov cutoff + 24-Nov holiday => H+1=25-Nov, H+3=27-Nov, H+5=01-Dec; 24-Nov row কোনো maturity count-এ ঢুকবে না।
- Validation: retained artifact-এ offline unit test, তারপর দ্বিতীয় independent artifact-এ same test; out-of-sample predictive claim নয়, data-correctness test।
- Carry-forward: ২৫-Nov close-এর পরেই ২৩-Nov cohort-এর H+1 audit; তার আগে PENDING. Audit-only tracker fix/test আলাদা research branch-এ; Production Selector/Ranking/Threshold অপরিবর্তিত।

Carried-forward lessons: PW-LSN-20261123-001 (holiday session spine), PW-LSN-20261124-002 (fail-closed source health), PW-LSN-20261124-003 (high-touch vs close/executable outcome), PW-LSN-20261124-004 (CI and denominator contract), PW-LSN-20261124-005 (manifest provenance), PW-LSN-20261121-001/002 (forward labels and H+5 parity). Duplicate lesson IDs তৈরি হয়নি।

## 7. Controls and final status

- No new workflow dispatch; no new NSE acquisition; no paid source; no external contact.
- No production, selector, ranking, threshold, CORE-672, Engines A–E or IPO-PLX V2.0 change.
- ₹0. UNKNOWN is neither PASS nor FAIL.
- Run #410 artifact ZIP integrity PASS; prospective tracker maturity semantics NOT_ACCEPTED; 200-session archive NOT_ACCEPTED; V11.4 NOT_VALIDATED; B UNKNOWN; C BLOCKED.
- পরবর্তী কাজ: ২৫-Nov close-এর পর valid H+1 cohort audit; offline holiday-aware tracker test; raw source provenance ও unique-session acceptance recovery.