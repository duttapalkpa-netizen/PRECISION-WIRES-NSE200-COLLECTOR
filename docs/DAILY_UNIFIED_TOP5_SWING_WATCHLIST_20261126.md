# PRECISION-WIRES V11.3 — ২৬ নভেম্বর ২০২৬
## India Pre-Market Unified Top-5 Swing Watchlist

**রিপোর্ট as-of:** 26-Nov-2026 08:40:05 IST  
**Market data cutoff:** 25-Nov-2026 close; official quote-page timestamps stock-wise নিচে দেওয়া আছে  
**পরবর্তী NSE equity session:** 26-Nov-2026  
**Qualified:** 0/5 | **Provisional:** 0 | **Unfilled:** 5/5

## 1. Executive decision

আজকের pre-market review-তে **একটিও stock সব hard admission gate পাস করেনি**। তাই পাঁচটি slot-ই UNFILLED রাখা হয়েছে। এটি “আজ কোনো stock উঠবে না” এমন পূর্বাভাস নয়; এটি verified evidence না থাকায় সতর্ক release decision।

Run #411-এর audit-only model পাঁচটি raw lead দিয়েছে, কিন্তু ওই পাঁচটির মধ্যে কয়েকটির official NSE page-এই ASM/LT-ASM, circuit/price-band, অতিরিক্ত margin, দুর্বল liquidity বা stale quote-এর প্রমাণ আছে। Model percentile-কে probability ধরে নেওয়া যাবে না এবং raw lead-কে qualified pick বলা যাবে না।

কোনো target price, probability, stop বা trade instruction তৈরি করা হয়নি। User-approved trade rules নেই; তাই stop/entry/exit অনুমান করা হয়নি।

## 2. Preflight — continuity, reports, archive, runs ও hashes

কাজ শুরুর আগে Master Continuity Ledger (C254 পর্যন্ত), 25-Nov Daily Report, 25-Nov Nightly Review, Failure & Lessons Log, Missed-Winner Integration note, Run #410 ও Run #411-এর artifact/ledger পরীক্ষা করা হয়েছে। আগে সম্পন্ন byte-integrity checks পুনরাবৃত্তি করা হয়নি; নতুন evidence ও unresolved blocker-ই পরীক্ষা করা হয়েছে।

### Run #411 — audit-only prospective selector

- Workflow run ID: **45695700887**; job ID: **139492398062**; run number: **411**; conclusion: SUCCESS.
- Workflow head commit: **fa3220dbddf3dc204eb2f20d08a0a44af719950a**.
- Audit branch commit from job log: **f96f9e8448d121b9f781cf526ed8e838ad3552e9** (prospective ledger update).
- Artifact ID: **15061666636**.
- Artifact ZIP SHA-256 independently recalculated: **6685f9d5d092ff4a8fe505040b0a08f4183e78339a56a53bcfaa6d666d256897** — GitHub upload log digest-এর সঙ্গে মিলে।
- Job runtime প্রায় **8m35s**; কোনো নতুন broad workflow dispatch করা হয়নি।
- Artifact-এ 17টি file আছে; raw NSE source ZIP/per-file acquisition manifest এবং full-universe point-in-time decision ledger নেই।

### Dataset QA বনাম semantic acceptance

Run #411 QA JSON-এ 200 raw files, 200 requested/processed dates, 3,001 symbols, 504,971 rows এবং 100% delivery coverage দেখানো হয়েছে। QA status PASS হলেও এটি **200টি distinct valid NSE trading session-এর acceptance নয়**। আগের semantic audit-এ 187 বনাম 188 unique session—দুটি আলাদা সংখ্যা পাওয়া গেছে; এই বিরোধ এখনো reconcile হয়নি। Run #411 artifact-এ per-file raw manifest, internal DATE1-to-requested-date reconciliation বা holiday duplicate report নেই। তাই 200-session claim এবং historical metrics এখনও NOT_ACCEPTED।

Collector source code NSE-এর CM-UDiFF Common Bhavcopy Final route ব্যবহার করে; NSE All Reports page-এ এই report type-ও তালিকাভুক্ত। কিন্তু এই run artifact-এ 25-Nov-এর exact raw URL, retrieval timestamp, source bytes এবং per-file SHA-256 সংরক্ষিত নেই। ফলে raw provenance gate পূর্ণ হয়নি।

### Run #411 evidence hashes

| File | SHA-256 |
|---|---|
| latest_picks.csv | bc489366de4cfad3811042d8ca9a362489039ed3fcd6eb2fb71e7f56c9f5bedc |
| watchlist_ledger.csv | 3d4e04063b200044ae89529dc6f3b7349bd83d81b17ab19e3748e7ab4c58f3e2 |
| walk_forward_metrics.json | 1353f7df37fbbbf3f1bdebd9b9af16c812988e1ca866c2f8b0eb762ee461ef83 |
| qa_report.json | 77ee88c0ec576ce644597492174e3ab5a498662e5adf9443b83e85627f80599c |

latest_picks.csv-এর hash watchlist ledger-এর PICK_SOURCE_SHA256-এর সঙ্গে মেলে। এটি file integrity প্রমাণ করে; data correctness বা candidate qualification নয়।

## 3. Next-Session Top-5 Prospective Stock Picks

**26-Nov-2026-এর জন্য Qualified = 0/5।** প্রতিটি slot ইচ্ছাকৃতভাবে unfilled। কোনো weak বা stale stock-কে qualified করা হয়নি।

| Rank | NSE symbol / company | Status | Reference price/time | +2/+5/+10/+15/+20 target bands | Horizon | Blocker / invalidation |
|---:|---|---|---|---|---|---|
| 1 | — | UNFILLED — INSUFFICIENT VERIFIED EVIDENCE | নেই | গণনা করা হয়নি | UNKNOWN | Fresh official price, current trend/RS, sector, liquidity, catalyst ও current risk gate একসঙ্গে verified নয় |
| 2 | — | UNFILLED — INSUFFICIENT VERIFIED EVIDENCE | নেই | গণনা করা হয়নি | UNKNOWN | একই hard-gate evidence gap |
| 3 | — | UNFILLED — INSUFFICIENT VERIFIED EVIDENCE | নেই | গণনা করা হয়নি | UNKNOWN | একই hard-gate evidence gap |
| 4 | — | UNFILLED — INSUFFICIENT VERIFIED EVIDENCE | নেই | গণনা করা হয়নি | UNKNOWN | একই hard-gate evidence gap |
| 5 | — | UNFILLED — INSUFFICIENT VERIFIED EVIDENCE | নেই | গণনা করা হয়নি | UNKNOWN | একই hard-gate evidence gap |

কোনো qualified reference price নেই বলে target-price arithmetic, invalidation price বা probability প্রকাশ করা হয়নি। এই report watchlist research; buy instruction বা return guarantee নয়।

### 3A. Audit-only model leads — candidate নয়, admission-এ প্রত্যাখ্যাত

Run #411-এর CURRENT_WINNER_PROB selector 25-Nov cutoff-এ নিচের পাঁচটি raw lead দিয়েছে। SELECTION_SCORE_VALUE হলো percentile-rank field; **99.56 মানে 99.56% probability নয়**। এগুলি production selector পরিবর্তন নয় এবং পাঁচটি Prospective Picks slot-এ স্থান পায়নি।

| Model lead rank | Symbol / company / ISIN | Latest official NSE price evidence | Cutoff-time risk / missing evidence | Admission decision |
|---:|---|---|---|---|
| 1 | SHALPAINTS — Shalimar Paints Ltd — INE849C01026 | NSE quote page সর্বশেষ 20-Nov-2026 16:00; close ₹97.42। 25-Nov fresh official close এই review-তে পাওয়া যায়নি। | NSE page-এ last 8 quarters loss-making, overall encumbered share >50%, impact cost 0.71, 20-Nov traded value ₹1.19 Cr। 25-Nov price/volume, current catalyst ও current sector confirmation নেই। | STALE PRICE + GOVERNANCE/LIQUIDITY RISK — NOT QUALIFIED |
| 2 | APLAPOLLO — APL Apollo Tubes Ltd — INE702C01027 | NSE close ₹1,476.00, 25-Nov-2026 16:00 IST; day −11.62%। | Series ST ASM-1; 52-week low ₹1,342.20; 1W −31.70%, 1M −27.42%; volume 451.05 lakh, traded value ₹6,638.38 Cr, delivery 26.39%। Sharp downside/ASM flag; fresh positive catalyst verified নয়। | SURVEILLANCE + NEGATIVE TREND — NOT QUALIFIED |
| 3 | PASHUPATI — Pashupati Cotspin Ltd — INE124Y01028 | NSE close ₹29.93, 25-Nov-2026 16:00 IST; day +4.98%। | Series LT ASM-1; upper band-এ close ₹29.93; 5% price band; 100% applicable margin; P/E >50 for prior four trailing quarters; 1M −28.26%; traded value ₹12.75 Cr, delivery 72.68%। | LT-ASM / CIRCUIT / MARGIN RISK — NOT QUALIFIED |
| 4 | OAL — Oriental Aromatics Ltd — INE959C01023 | NSE quote page সর্বশেষ 20-Nov-2026 16:00; close ₹516.70, ওই দিনে +20.00%। 25-Nov fresh official close পাওয়া যায়নি। | 20% price band, deliverable/traded quantity 2.73%, impact cost 0.32, 1M −17.25%; quote stale এবং prior 20% limit move। Fresh catalyst/price/volume/sector নেই। | STALE PRICE + CIRCUIT/LOW-DELIVERY RISK — NOT QUALIFIED |
| 5 | NECCLTD — North Eastern Carrying Corporation Ltd — INE553C01016 | NSE quote page সর্বশেষ 20-Nov-2026 16:00; close ₹23.17। 25-Nov fresh official close পাওয়া যায়নি। | Series ST ASM-1; 50% applicable margin; impact cost 1.27; 20-Nov traded value ₹71.81 lakh; current liquidity, price/volume ও catalyst evidence নেই। | STALE PRICE + SURVEILLANCE/LIQUIDITY RISK — NOT QUALIFIED |

**কোনো lead-এর target band বা H+1/H+3/H+5 horizon প্রকাশ করা হয়নি।** Model code-এ live candidate ranking percentile-based; current exchange risk, catalyst এবং final admission fields ওই output-এ join করা নেই। Final hard-gate review তাই আলাদা রাখতে হয়েছে। No user stop/entry rule অনুমান করা হয়নি।

## 4. Three independent engine scorecards

| Engine | Status | আজকের সিদ্ধান্ত |
|---|---|---|
| A — V11.4 Historical Behavioural Selector | HISTORICAL EXPLORATORY ONLY / NOT_ACCEPTED | Run #411-এর Top-30 aggregate metrics নিচে দেখানো হয়েছে; 200-session semantic spine, forward-label ও denominator reconciliation unresolved। Top-5 probability বা production performance হিসেবে ব্যবহার নয়। |
| B — V11.3 Cost-aware Trade Replay | UNKNOWN / NOT_AUTHORIZED | User-approved entry/exit/stop/circuit/position-sizing/overlap/cost assumptions এবং independently reconciled trade replay নেই। Net return, win rate, drawdown UNKNOWN। |
| C — Global Capital Rotation | UNKNOWN / BLOCKED | Macro-sector-stock timestamp/vintage alignment এবং matured outcomes-এর একই-snapshot evidence নেই। GCR ranking boost শূন্য/UNKNOWN। |

### Alert Section 1 — Target-wise capture performance (exploratory Top-30, accepted নয়)

Run #411 walk_forward_metrics.json-এ 100 tested cutoffs এবং 3,000 Top-30 candidate rows আছে। নিচের denominator হলো ওই Top-30 rows-এর target-specific matured rows; এটি full-universe recall denominator নয় এবং আজকের Top-5 alert-এর hit rate-ও নয়।

| Target / horizon | TP / evaluated n | Hit rate | FP | Recall (exploratory) | Status |
|---|---:|---:|---:|---:|---|
| +2% | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | Target series/artifact নেই |
| +5% / H+1 | 952 / 2,977 | 31.98% | 2,025 | 4.05% | Exploratory only |
| +10% / H+3 | 625 / 2,896 | 21.58% | 2,271 | 3.61% | Exploratory only |
| +15% / H+5 | 379 / 2,827 | 13.41% | 2,448 | 3.08% | Exploratory only |
| +20% / H+5 | 194 / 2,827 | 6.86% | 2,633 | 3.50% | Exploratory only |

এগুলি historical high-touch label/selector diagnostics; profitable trade return নয়, executable fill নয়, এবং confidence-accepted performance নয়। +15% সংখ্যা আগের report থেকে copy করা হয়নি; Run #411-এর বর্তমান artifact থেকে fresh count নেওয়া হয়েছে। একই signal একাধিক target-এ hit করতে পারে; target counts overlap করে, তাই যোগ করা যাবে না।

### Prior comparable-day drift

Run #410 → Run #411 input SHA-256 বদলেছে: e788b0b39979094fa3b2f9ad9d1b1ebc57ed2b52088f73a759e75fadebf296d4 → 25cfbd7f97c2a27c474b3bd97335ae149ef59ac185f52dd65d565d9b69fb2378। ফলে output পরিবর্তনকে performance improvement/degradation বলা যাবে না; একই input-এ within-run reproducibility PASS হলেও cross-run input reconciliation হয়নি।

| Target | Run #410 | Run #411 | পার্থক্য |
|---|---:|---:|---:|
| +5% H+1 | 958/2,977 = 32.18% | 952/2,977 = 31.98% | −0.20 pp |
| +10% H+3 | 628/2,892 = 21.72% | 625/2,896 = 21.58% | −0.14 pp |
| +15% H+5 | 381/2,824 = 13.49% | 379/2,827 = 13.41% | −0.08 pp |
| +20% H+5 | 196/2,824 = 6.94% | 194/2,827 = 6.86% | −0.08 pp |

এই drift data/input-vintage change-এর সঙ্গে এসেছে; এটি accepted performance change নয়। +2% দুই artifact-এই UNKNOWN।

## 5. Alert Section 2 — Target-wise historical best three

+2%, +5%, +10%, +15%, +20% — **প্রতিটি target-এ independently verified historical best-three list <3 / UNKNOWN**। Run #411 artifact-এ aggregate Top-30 metrics আছে, কিন্তু target-wise unique-symbol matured outcome table, latest matured cutoff, stock-wise evaluated n ও exchange/ISIN reconciliation নেই। কোনো একক extreme move থেকে historical leader বানানো হয়নি। Survivorship/future leakage controls এবং full-universe row-level reconciliation না হওয়া পর্যন্ত কোনো stock rank করা হবে না।

## 6. Alert Section 3 — Daily Failure Analysis & Missed-Winner Audit

### আগের নির্বাচিত cohort

- 23-Nov cutoff: **7 unique symbols / 10 selector rows** — BI, KDDL, ONIXSOLAR, SALASAR, SHALPAINTS, SHARDUL, UFBL।
- Run #411 watchlist ledger-এ ওই cohort-এর T1_HIGH_PCT এবং MATURED_T1=True দেখা যায়, কিন্তু OUTCOME_LAST_DATE ফাঁকা। 24-Nov-2026 NSE capital-market holiday; তাই 24-Nov row-কে H+1 session হিসেবে গণনা করা যাবে না।
- Official calendar অনুযায়ী 23-Nov cutoff-এর সঠিক horizon: H+1 = 25-Nov, H+3 = 27-Nov, H+5 = 01-Dec। 25-Nov-এর raw official row, exact date linkage ও horizon-end field independentভাবে মেলানো না হওয়া পর্যন্ত H+1 **PENDING**; আগের T1 labels বাতিল/অগ্রহণযোগ্য।
- 24-Nov holiday cutoff cohort বাদ। Holiday date-এ generated 10 selector rows/9 unique symbols candidate বা outcome হিসেবে গণ্য নয়।

### বর্তমান 25-Nov cutoff cohort

- Run #411 tracker: **10 selector rows / 7 unique symbols** — APLAPOLLO, ASHIKAG, NECCLTD, OAL, ORIENTLTD, PASHUPATI, SHALPAINTS।
- 26-Nov pre-market-এ H+1/H+3/H+5 outcomes mature হয়নি; সব PENDING। Official calendar অনুযায়ী expected H+1 = 26-Nov, H+3 = 30-Nov, H+5 = 02-Dec।
- 25-Nov cutoff থেকে current model lead-গুলির কোনোটি qualified হয়নি; তাই false-positive বা forecast success/failure label দেওয়া হয়নি।

### Full eligible-universe missed winners

**UNKNOWN / BLOCKED।** Run #411 artifact-এ 3,001-symbol normalized dataset QA summary আছে, কিন্তু cutoff-by-symbol inclusion/exclusion + per-filter decision trace-সহ canonical point-in-time ledger নেই; full-universe row-level H+1/H+3/H+5 outcome reconciliation-ও নেই। তাই +2/+5/+10/+15/+20 target-এ কত missed winner ছিল বা কোন CORE-672 diagnostic বাদ দিয়েছে তা গণনা করা যায়নি। “কোনো missed winner নেই” বলা হচ্ছে না।

### Root-cause classification

| Issue | Classification | Evidence-based conclusion |
|---|---|---|
| 23-Nov cohort-এর holiday row-কে next session ধরা | VERIFIED (code/contract level) | Tracker outcome() পরের sorted symbol row নেয়; official holiday spine বাধ্যতামূলক নয় এবং OUTCOME_LAST_DATE অনুপস্থিত। Individual return impact UNKNOWN। |
| Full-universe missed-winner count | UNKNOWN / DATA GAP | Point-in-time decision ledger ও full-universe matured outcome rows অনুপস্থিত। |
| Raw model lead-এ ASM/price-band/liquidity risk | SUPPORTED | Official NSE quote pages-এ একাধিক risk flag আছে; model score নিজে risk admission প্রমাণ করে না। |
| নির্দিষ্ট CORE-672 filter বা ranking failure | UNKNOWN | Per-symbol point-in-time decision trace নেই; কোনো filter-কে দায়ী করা হয়নি। |

## 7. Alert Section 4 — EVERY-MISTAKE LEARNING & RESEARCH REGISTER

### Existing immutable lessons — evidence/status carried forward

- **PW-LSN-20261121-001:** exact forward-session label defect — OPEN; Run #411 aggregate metrics এই lesson বন্ধ করে না।
- **PW-LSN-20261121-002:** H+5 JSON/CSV parity — OPEN; canonical row-level parity নেই।
- **PW-LSN-20261121-003:** raw source manifest/provenance — OPEN; Run #411 artifact-এ per-file raw ZIP/hash manifest নেই।
- **PW-LSN-20261123-001:** holiday/session spine — OPEN; আগের 187 বনাম 188 unique-date conflict এখনও reconcile হয়নি।
- **PW-LSN-20261124-002:** fail-closed source readiness — OPEN; pre-market intraday feed এখানে ব্যবহৃত হয়নি; EOD quote freshness-ও symbol-wise যাচাই করতে হয়েছে।
- **PW-LSN-20261124-003:** high-touch vs close-to-close vs executable outcome — OPEN; tracker high-touch label একা executable trade result নয়।
- **PW-LSN-20261124-004:** confidence interval ও denominator reconciliation — OPEN।
- **PW-LSN-20261124-005:** export manifest / raw-package provenance — OPEN।
- **PW-LSN-20261125-001:** holiday row counted as next trading session — OPEN; Run #411-এ OUTCOME_LAST_DATE blank থাকা সত্ত্বেও T1 maturity fields populated, তাই পুনরায় evidence append করা হয়েছে।

### নতুন immutable lesson

**PW-LSN-20261126-001 — Audit-only prospective model lead-এর percentile rank-এ current exchange risk/admission fields নেই।**

- **Evidence:** Run #411 latest_picks.csv-এর five CURRENT_WINNER_PROB leads; selector source code percentile-based score/rank তৈরি করে, কিন্তু ওই output-এ current ASM/GSM, price-band, applicable margin, impact cost, fresh official quote, catalyst timestamp বা sector validation join করে না।
- **Observed examples:** APLAPOLLO — 25-Nov NSE close −11.62%, ST ASM-1; PASHUPATI — 25-Nov close upper 5% band-এ, LT ASM-1 ও 100% margin; OAL — latest accessible official quote 20-Nov-এ +20% upper band এবং 2.73% deliverable; NECCLTD — stale 20-Nov quote, ST ASM-1, impact cost 1.27; SHALPAINTS — latest accessible official quote 20-Nov, loss-making/encumbrance warning।
- **Root cause:** selector-output schema-তে final admission/risk fields না থাকা VERIFIED (code-level)। এটি কোনো stock-এর future return miss করেছে—এমন causal claim নয়।
- **কেন ধরা পড়েনি:** model percentile-কে final rank/qualified alert মনে করলে raw research lead ও executable/risk-qualified candidate এক হয়ে যেতে পারে।
- **Research question:** official NSE quote, security master, price-band/surveillance/margin/liquidity ও dated catalyst evidence যুক্ত না করে কোনো raw lead-কে qualified বলা হচ্ছে কি না?
- **Bounded reproducible test:** latest_picks.csv-এর প্রতিটি unique symbol-এর জন্য একই cutoff-এ NSE official symbol/ISIN/series, close/time, volume/value/delivery, impact cost, price band, ASM/GSM/surveillance, applicable margin, sector এবং filing publication time reconcile করা। Unknown বা stale field থাকলে slot unfilled থাকবে।
- **Leakage-safe validation:** কেবল cutoff-এর আগে প্রকাশিত তথ্য; পরবর্তী দিনের filing/price ব্যবহার নয়। অন্তত 50 matured observations per state-এর পূর্বশর্ত বজায় থাকবে; একক দিনের observation দিয়ে production rule বদলানো যাবে না।
- **Acceptance criterion:** 100% candidate row-এর source URL/time/ISIN ও risk fields independently reconciled; raw percentile probability হিসেবে দেখানো যাবে না; কোনো production code/ranking/threshold change নয়।
- **Expected artifact:** prospective_risk_gate_admission_audit.json। **Confidence:** code-level gap HIGH; predictive impact UNKNOWN। **Carry-forward:** পরবর্তী morning ও nightly audit checklist-এ যুক্ত।

## 8. পরবর্তী bounded verification tests

1. **calendar_aware_tracker_regression.json** — 23-Nov→25-Nov/27-Nov/01-Dec session mapping; holiday row reject; exact horizon end date বাধ্যতামূলক।
2. **point_in_time_decision_ledger_audit.json** — একই cutoff-এ eligible universe-এর প্রতিটি symbol-এর inclusion/exclusion, rank, per-filter PASS/FAIL/UNKNOWN, source time ও code/config hash।
3. **universe_missed_winner_reconciliation.json** — accepted decision ledger-কে official NSE EOD high/close/corporate-action data-র সঙ্গে target/horizon-wise reconcile; unique symbol ও signal-row আলাদা।
4. **missed_winner_root_cause_audit.json** — cutoff-only feature/catalyst reconstruction; filter-level cause কেবল trace থাকলে।
5. **prospective_risk_gate_admission_audit.json** — raw model lead বনাম official risk/liquidity/price freshness gate; observation-only, no production admission।

প্রতিটি job bounded এবং 10 মিনিটের মধ্যে রাখতে হবে; existing evidence reuse করতে হবে। বড় কাজ একসঙ্গে চালানো নয়।

## 9. Controls, sources ও final status

- NSE official 2026 holiday calendar-এ 24-Nov-2026 Prakash Gurpurb Sri Guru Nanak Dev holiday; তাই পরবর্তী trading session 26-Nov।  
- NSE All Reports page CM-UDiFF Common Bhavcopy Final report type তালিকাভুক্ত করে; 25-Nov raw ZIP payload/manifest এই artifact-এ নেই।
- Candidate evidence: NSE official quote pages — SHALPAINTS, APLAPOLLO, PASHUPATI, OAL, NECCLTD (links নিচে)।
- কোনো paid API/service, synthetic data, forward-fill, guessed mapping বা external contact ব্যবহার করা হয়নি। Spend ₹0।
- Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E ও IPO-PLX V2.0 অপরিবর্তিত।
- কোনো threshold, selector, ranking বা production admission পরিবর্তন করা হয়নি।
- **Final: 0 qualified / 5 unfilled; A NOT_ACCEPTED; B UNKNOWN; C UNKNOWN/BLOCKED; historical best-three UNKNOWN; full-universe missed winners UNKNOWN/BLOCKED.**

### Official source links

- NSE 2026 holidays: https://www.nseindia.in/resources/exchange-communication-holidays
- NSE 2026 trading-holiday circular: https://nsearchives.nseindia.com/content/circulars/CMTR71775.pdf
- NSE All Reports / CM-UDiFF report catalogue: https://www.nseindia.com/all-reports
- NSE SHALPAINTS quote: https://www.nseindia.in/get-quote/equity/SHALPAINTS/Shalimar-Paints-Limited
- NSE APLAPOLLO quote: https://www.nseindia.in/get-quote/equity/APLAPOLLO/APL-Apollo-Tubes-Limited
- NSE PASHUPATI quote: https://www.nseindia.in/get-quote/equity/PASHUPATI/Pashupati-Cotspin-Limited
- NSE OAL quote: https://www.nseindia.in/get-quote/equity/OAL/Oriental-Aromatics-Limited
- NSE NECCLTD quote: https://www.nseindia.in/get-quote/equity/NECCLTD/North-Eastern-Carrying-Corporation-Limited
- Run #411: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/45695700887
- Run #411 artifact: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/45695700887/artifacts/15061666636

## 10. আজকের শিক্ষা → গবেষণায় সংযোজন → পরবর্তী যাচাই

**আজকের শিক্ষা:** model percentile probability নয়; raw selector lead-এ exchange risk/price freshness gate না থাকলে তা qualified pick নয়। Holiday-aware maturity এবং raw source provenance-ও এখনো unresolved।

**গবেষণায় সংযোজন:** PW-LSN-20261125-001-এ Run #411 tracker evidence append; নতুন PW-LSN-20261126-001 risk/admission schema gap হিসেবে register; আগের forward-label, H+5 parity, session-spine, provenance ও denominator lessons carry-forward।

**পরবর্তী যাচাই:** প্রথমে calendar-aware tracker regression; তারপর 25-Nov official raw EOD manifest/unique-session parity; এরপর full-universe decision-ledger/outcome reconciliation এবং prospective risk-gate audit। Evidence PASS না হওয়া পর্যন্ত 5টি slot unfilled থাকবে এবং production logic অপরিবর্তিত থাকবে।
