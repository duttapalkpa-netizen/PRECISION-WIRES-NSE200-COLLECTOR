# PRECISION-WIRES V11.3 — Failure & Lessons Learned Register
## ২৫ নভেম্বর ২০২৬

## New immutable lesson

### PW-LSN-20261125-001 — Prospective tracker holiday row-কে next trading session হিসেবে গণনা করে

**Status:** ROOT CAUSE CONFIRMED; FIX / REGRESSION TEST OPEN  
**Severity:** High — prospective maturity labels ও H+1 failure audit দূষিত হতে পারে  
**Scope:** Audit-only prospective watchlist tracker; Production Selector বা RANKING_SCORE নয়

**Evidence**
- Run #410: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/45490518576
- Run ID 45490518576; artifact ID 14966627305; artifact ZIP SHA-256: 6b1673af895214ae982fb445a62d5536dd2960eb062dc310b85f955b01c8af16. Downloaded ZIP hash GitHub artifact digest-এর সঙ্গে মিলে গেছে।
- Artifact latest_picks.csv SHA-256: aa0a685260f56cbf8355019ae5b6d5b6abf3ea7bb6e98f1417b2f999d63c28e6
- Artifact watchlist_ledger.csv SHA-256: 4c7d629634d945f65beebf73a5cd7f89d96cd5650f3a8d07a54f29a113ebdc13
- ২৩-Nov cutoff-এর ১০টি selector row / ৭টি unique symbol-এ MATURED_T1=True ও T1_HIGH_PCT populated; OUTCOME_LAST_DATE ফাঁকা। অথচ ২৪-Nov ছিল NSE holiday; পরবর্তী বৈধ session ২৫-Nov।
- একই artifact-এ LIVE_CUTOFF=2026-11-24, PICKS=10, LABELS=NOT_READ FROM_FUTURE; ২৪-Nov holiday cutoff-এর ১০টি row / ৯টি unique symbol invalid, current candidate হিসেবে গ্রহণ করা হয়নি।
- Code-level evidence: branch audit/prospective-selector-tracking-এর prospective_watchlist_tracker.py, Git blob SHA-1 f28f7c752c4eaadeb5583f4434190a124a4910d9। outcome() cutoff-এর পর symbol-এর sorted DATE rows থেকে পরের hটি row নেয়; official exchange-session/holiday calendar যাচাই করে না। H+1-এর OUTCOME_LAST_DATE persist করে না।

**Root cause**
- Holiday/session-calendar validation অনুপস্থিত — CONFIRMED.
- নির্দিষ্ট T1_HIGH_PCT কতটা duplicate-content row থেকে এসেছে, per-row price audit ছাড়া সেই অংশ আলাদা করে UNKNOWN.
- MATURED_T1=True কিন্তু OUTCOME_LAST_DATE blank — observed evidence inconsistency CONFIRMED.

**কেন আগের গবেষণা ধরতে পারেনি**
- Tracker row-count/order-কে trading-session maturity ধরে নিয়েছে; official exchange calendar ও source DATE semantic acceptance যুক্ত ছিল না।
- QA status 200 date labels গণনা করেছে; unique valid exchange sessions নয়।

**Prevention research question**
- কোনো horizon কি তখনই mature হবে, যখন cutoff-এর পর যথাক্রমে 1/3/5টি distinct official trading session সম্পূর্ণভাবে পাওয়া যায় এবং প্রতিটি outcome date official session spine-এর সঙ্গে মেলে?

**Free official-source reproducible test**
1. NSE holiday calendar-এর ২৪-Nov-2026 বন্ধের তারিখ session spine-এ non-trading হিসেবে চিহ্নিত।
2. ২৩-Nov cutoff-এর জন্য H+1=২৫-Nov, H+3=২৭-Nov, H+5=০১-Dec।
3. ২৪-Nov row কোনো horizon-এর মধ্যে গণনা করা যাবে না।
4. MATURED_T1/T3/T5=True হলে expected horizon-end date ও OUTCOME_LAST_DATE বাধ্যতামূলক এবং exact match হতে হবে।
5. Missing date, holiday, duplicate-content session বা incomplete horizon হলে PENDING/False থাকবে।
6. ২০-Nov ও ২৩-Nov-এর মতো holiday adjacency-সহ অন্তত দুই retained artifact-এ test পুনরায় চালাতে হবে।

**Out-of-sample / leakage controls**
- এটি data-correctness regression; predictive performance claim নয়।
- Cutoff-time features freeze; official exchange session calendar ছাড়া future row গ্রহণ নয়।
- একাধিক independent retained artifact-এ byte-reproducible ফল; production selector/ranking/threshold অপরিবর্তিত।

**Result / confidence**
- Tracker code omission ও holiday mismatch: CONFIRMED.
- Corrected tracker implementation: NOT_DONE.
- ২৩-Nov cohort H+1 outcome at ২৫-Nov 08:45 IST: PENDING; market close-এর আগে success/failure নয়।

**Carry-forward**
- ২৫-Nov close-এর পরে ২৩-Nov cohort-এর H+1 audit; তার আগে PENDING.
- Audit-only branch-এ calendar-aware tracker test proposal; production integration নয়।
- পুরোনো PW-LSN-20261123-001 (holiday/session spine) ও PW-LSN-20261124-002 (fail-closed source health)-এর সঙ্গে linked; duplicate lesson তৈরি নয়।

## Daily Failure & Missed-Winner scorecard — ২৫-Nov 08:45 IST

- ২৩-Nov cohort: ৭ unique selected symbols; valid matured outcomes: ০; confirmed FP: UNKNOWN/PENDING.
- ২৪-Nov holiday cutoff cohort: ৯ unique symbols excluded; no valid session outcome.
- Target-wise missed winners: UNKNOWN; canonical point-in-time full-universe decision ledger ও valid outcome date reconciliation অসম্পূর্ণ।
- Avoidable / unavoidable misses: UNKNOWN; hindsight-only causal claims গ্রহণ করা হয়নি।
- No new false-positive or missed-winner performance claim is made today.

## Carried-forward research lessons — immutable IDs retained

- PW-LSN-20261121-001: exact forward-session label defect; H+3/H+5 rolling-window semantics remain OPEN.
- PW-LSN-20261121-002: H+5 JSON/CSV count discrepancy; canonical row-ledger parity OPEN.
- PW-LSN-20261123-001: holiday/session spine and unique-date semantic validation OPEN.
- PW-LSN-20261124-002: GEO/live source readiness fail-closed gate OPEN.
- PW-LSN-20261124-003: high-touch vs close-to-close vs executable return distinction.
- PW-LSN-20261124-004: confidence intervals and denominator reconciliation evidence contract OPEN.
- PW-LSN-20261124-005: export-manifest filename/provenance distinction; original ZIP mapping remains BLOCKED.

## Today’s learning → research integration → next verification

1. Add official-session calendar validation to prospective tracker acceptance design.
2. Require OUTCOME_LAST_DATE for every matured horizon.
3. Reconcile the ২৩-Nov cohort only after ২৫-Nov close.
4. Keep +2/+5/+10/+15/+20 target labels separate; high-touch is not executable profit.
5. Keep all selector, ranking, CORE-672, Engines A–E and IPO-PLX V2.0 unchanged pending user approval and leakage-safe out-of-sample validation.

**Controls:** ₹0; free official sources only; no synthetic rows or guessed timestamps; no new workflow dispatch or NSE acquisition; UNKNOWN never PASS.


---

## Nightly addendum — ২৫-Nov-2026

- **Existing immutable lesson updated, not duplicated:** PW-LSN-20261125-001 (holiday row incorrectly counted as next trading session). Today's nightly review rechecked the morning watchlist, Run #410 / artifact #14966627305 and the tracker maturity contract. No new post-close, calendar-correct H+1 artifact was surfaced; therefore the 23-Nov cohort (7 unique symbols / 10 signal rows) remains PENDING for H+1 outcome acceptance, despite the valid exchange close having occurred.
- **Expected vs observed:** expected H+1 outcomes with official session date and per-symbol source timestamp; observed no new reconciled post-close row ledger in the available Actions/artifact inventory. Root cause of tracker holiday-row defect remains CONFIRMED; individual stock hit/miss remains UNKNOWN.
- **Prevention / acceptance test:** exact official session spine; 23-Nov→25-Nov/27-Nov/01-Dec; 24-Nov excluded; every MATURED flag requires matching horizon-end date; reject missing/duplicate/non-session rows. Run on two retained artifacts, row-level deterministic output. Expected artifact calendar_aware_tracker_regression.json; acceptance OPEN / NOT_RUN.
- **Research integration:** carry the calendar-aware regression and 23-Nov H+1 post-close reconciliation in Observation-only backlog. No new lesson ID, no duplicate; no threshold/selector/production changes.
- **Linkage:** nightly report docs/NIGHTLY_ROTATION_BACKTEST_RESEARCH_REVIEW_20261125.md; report commit 24371d62112d6070977fda5bb242c1f5a0839575; report blob SHA-1 cdc3b9d1332733cbb0131f361251891bf829dc99; reused Run #410 / artifact #14966627305 / ZIP SHA-256 6b1673af895214ae982fb445a62d5536dd2960eb062dc310b85f955b01c8af16. No new workflow run or artifact; SHA-256 for the Markdown report itself was not independently computed.
- **Acceptance:** lesson evidence update PARTIAL; calendar-aware fix NOT_DONE; H+1 outcome reconciliation PENDING; no performance metrics promoted.


---

## Evening addendum — next-session watchlist (25-Nov-2026, 19:53 IST)

- Next official NSE equity session is 26-Nov-2026 (Thursday), checked against the official 2026 equity holiday calendar.
- Current official NSE live-equity page rendered its quote table as Loading and market snapshot values blank in this retrieval surface. Official JNPR, SKYWAYS and FINOPB quote pages also rendered no usable price/volume values. This is a retrieval/rendering limitation, not proof that NSE itself had no EOD data.
- Official NSE corporate-filings page listed 25-Nov entries for JNPR (order/contract), SKYWAYS (acquisition) and FINOPB (board-meeting outcome). These are filing leads only; no detailed latest filing payload + fresh EOD price/volume/RS/liquidity/circuit verification was available, so none was promoted to provisional or qualified candidate.
- After-close next-session report: docs/DAILY_UNIFIED_TOP5_NEXT_SESSION_20261126_20261125_AFTER_CLOSE.md; commit 983ae0dd22bafa04419bd383a5378b0a227523d3; report SHA-256 8b19a10b2d5ae050675bf74e764091de07c8b790f4e2637c51a3c97ae218ce6c.
- Run #410 / 45490518576; artifact 14966627305; previously verified ZIP SHA-256 6b1673af895214ae982fb445a62d5536dd2960eb062dc310b85f955b01c8af16. Reused; no duplicate download or new workflow dispatch.
- No qualified or provisional picks: 0/5; all five slots UNFILLED. No scenario prices calculated. 23-Nov cohort H+1 was due after 25-Nov close but remains PENDING/NOT_VERIFIED because the official 25-Nov EOD raw file and independently reconciled outcome ledger were not captured.
- Existing PW-LSN-20261124-002 updated with this official-page rendering/source-readiness occurrence; no new lesson ID. PW-LSN-20261125-001 carried forward: exact official-session maturity and OUTCOME_LAST_DATE test remain OPEN. No new predictive lesson inferred.
- Next verification: capture official 25-Nov CM-UDiFF EOD file via approved route, verify source date/bytes/hash, then reconcile 23-Nov cohort H+1 separately for high-touch, close-to-close and adverse excursion. ₹0; no production/selector/ranking changes; UNKNOWN never PASS.
