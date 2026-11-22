# Run #386 Hard-Gate Failure Analysis — Continuation 252

Date: 2026-11-22
Branch: `audit/prospective-selector-tracking`
Run: #386, ID `44994024718`
Head: `e81aeb913f426917f27f602da926c1f56201478a`
Job: `macro-geo-p0`, job ID `137121090511`
Artifact: `macro-geo-p0-event-study`, ID `14743653729`
Artifact size: 4,909,299 bytes
Artifact SHA-256: `20e83e668e7d089bf915b74bfc31cd47853ec77171c9d34cda52fb65aa5c690a`

## 1. Exact failure
Run #386 conclusion: FAILURE. Steps 1–15, 17 and 19 succeeded; strict hard gate step 16 failed with exit code 1. This is a deliberate acceptance-gate failure, not a Python exception or regression-test failure.

Hard-gate report:
- status BLOCKED
- P0 groups: 7/8
- missing group: usd_inr
- event-study windows: 0
- blockers: EVENT_STUDY_NOT_COMPUTED_WITH_MATURE_WINDOWS; P0_SOURCE_COVERAGE_INCOMPLETE
- candidate_release_allowed=false
- production_selector_changed=false; ranking_score_changed=false; pressure_fade_changed=false

## 2. Artifact evidence
- `p0_collection_manifest.json`: NIFTY 50, NIFTY IT, NIFTY BANK, NIFTY AUTO, NIFTY METAL, NIFTY PHARMA, NIFTY ENERGY, NIFTY FMCG, NIFTY REALTY, NIFTY INFRA, INDIA VIX and GLOBAL VIX are present with official NSE/Cboe provenance. Brent collection in initial collector was BLOCKED because FRED timed out and Yahoo returned HTTP 429; however bounded repair succeeded using official US EIA RBRTE XLS, 212 rows, 2026-01-19 through 2026-11-17.
- `p0_repair_report.json`: USD/INR BLOCKED because FRED DEXINUS timed out and no direct official FBIL endpoint is configured. Community mirror remains disabled. NSE FPI/DII snapshot had 1 distinct date / 0-day span and correctly failed the >=60 dates / >=90 calendar days rule. Corporate events 164,375 rows from official NSE endpoint.
- NSDL official FPI archive: FPI 119 dates / 172 days; DII 102 dates / 150 days, with 7 DII daily schema misses. These are separate from the NSE snapshot and are present in the artifact.
- Event study: 21 publisher-feed mentions, only 1 eligible, 20 pending, 0 event windows. All 20 pending records are dated 2026-11-21/22, later than the market panel latest close 2026-11-20. The single eligible record had no valid pre/post publication-close window. Events are publisher publication-time proxies, not verified occurrence timestamps. No prices or event dates were fabricated.
- Market panel: 2,496 rows, 12 series; latest date 2026-11-20. NSE equity panel latest date 2026-11-20; no calendar freshness gap.

## 3. Interpretation
The hard gate is behaving correctly. Do not weaken its acceptance criteria, label secondary data as official, manufacture earlier event dates, or count immature event windows. The immediate unresolved source task is direct FBIL USD/INR historical retrieval. Public official evidence confirms FBIL assumed USD/INR reference-rate computation and dissemination from 2018-07-10; the FBIL website publishes INR/1 USD reference-rate observations. This does not yet prove a machine-readable historical archive endpoint has been identified or validated.

## 4. Source-policy and research findings
- RBI official release: https://www.rbi.org.in/Scripts/BS_PressReleaseDisplay.aspx?prid=44393
- FBIL official site: https://www.fbil.org.in/
- RBI official publication Table 223: https://www.rbi.org.in/Scripts/PublicationsView.aspx?id=24048
- FBIL methodology: https://www.fbil.org.in/uploads/FBIL_REFERENCE_RATE_FINAL_fa318d5727.pdf
- RBI confirms FBIL took over reference rates from 2018-07-10. FBIL site displays official INR/1 USD rates; a public page snippet showed dated daily observations. Need verify the actual official download/API contract before coding. The RBI Table 223 page currently surfaced a dated table only through April 2026, so it is not accepted as complete coverage through the required 2026-11-20 window.
- Do not reintroduce community GitHub mirror or use paid/credentialed services.

## 5. Status
- C251 code and five policy regression tests: committed; this run's earlier regression test step succeeded.
- C251 end-to-end source-policy CI: not PASS because hard gate is blocked.
- Brent official EIA repair: PASS (212 rows).
- USD/INR official historical data: BLOCKED.
- Mature event study: BLOCKED_PENDING_MATURE_WINDOWS.
- Hard gate / candidate release: BLOCKED.
- Production selector invariants: unchanged.

## 6. Next exact actions
1. Inspect FBIL official website frontend/download flow to identify the official historical USD/INR archive or public endpoint and its schema; do not assume endpoint names.
2. Build a bounded collector with source URL, retrieval timestamp, response hash, row count, and official source identity; regression-test parsing, dates, currency pair, units, and missing/duplicate rows.
3. If official historical FBIL archive is unavailable for the complete required period, keep USD/INR BLOCKED and record the exact coverage gap.
4. Add historical event backfill only from source-linked publications with actual publication timestamps; keep occurrence date unverified unless independently evidenced. Existing events from Nov 21/22 remain pending until later market closes mature.
5. Re-run targeted QA, then the P0 workflow; update ledger with exact artifact and hard-gate evidence. Never bypass the hard gate.

## Invariants
Audit branch only; ₹0 spend; official/free sources only; no synthetic data, fabricated timestamps, or community mirror. UNKNOWN/BLOCKED never PASS. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E unchanged.
