# PRECISION-WIRES V11.3 — India Pre-Market Unified Top-5 Watchlist
## 2026-11-22 | Observation-only daily report

**Release decision: যোগ্য candidate ০ — আজ কোনো নির্ভরযোগ্য alert নেই।** এটি research watchlist, buy instruction নয়।

## 1. Session status, data cutoff ও universe
- Report date: 2026-11-22 (Sunday, Asia/Kolkata); no regular NSE equity session today.
- Latest archived market cutoff available to this review: 2026-11-20.
- Next scheduled NSE equity session: 2026-11-23; 2026-11-24 is a capital-market trading holiday under NSE Circular NSE/CMTR/71775.
- Reused only existing authorized archive evidence; no new NSE download or workflow dispatch.
- Run #416 archive: 200 sessions, 2026-02-16 through 2026-11-20; 2,999 symbols; 503,892 normalized rows. Dataset SHA-256: `d6810409dbd800e5146e08a1eb1e8b48207354461876acb62cbb2f656fba51db`.
- The archive is normalized data plus security master, not the original raw NSE payload archive. Original bhavcopy/delivery bytes and an acquisition-time per-file manifest are absent. It cannot be treated as a complete raw-source replay.
- Prospective shadow cohort from the 2026-11-20 cutoff: 8 unique symbols / 10 selector rows: NRL, V2RETAIL, SIGACHI, RSDFIN, KDDL, YATRA, KMCSHIL, HINDOILEXP. These remain shadow observations only; none passes current candidate evidence gates.
- Candidate universe for release: eligible verified names after current identity + price/time + price-volume + liquidity + circuit/surveillance + catalyst checks = 0. No five-name fill.

## 2. Executive target-wise historical capture performance
The prior Nightly Review dated 2026-11-21 marks the v1 historical target labels/ranking lineage NOT_ADMISSIBLE. The corrected-label diagnostic remains contaminated by the selector/training path. Therefore no verified historical capture count or rate is released today.

| Target | Horizon | Verified TP / evaluated denominator | Historical hit rate | False positives | Sample size |
|---|---|---:|---:|---:|---:|
| +2% | H+1 | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN |
| +5% | H+1 | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN |
| +10% | H+3 | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN |
| +15% | H+5 | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN |
| +20% | H+5 | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN |

Historical target-hit rate is not profitable trade return, executable win rate, or cost-adjusted return. No earlier unvalidated +15% value is reused.

## 3. Historical best three stocks per target
Ranking is BLOCKED / NOT_VALIDATED for every target because the v1 forward-label window is defective and contaminates the training/ranking lineage. No stock is promoted as a historical leader.

| Target | Qualified historical leaders | Result |
|---|---|---|
| +2% | 0 | UNKNOWN / NOT_VALIDATED; qualified stock <3 |
| +5% | 0 | UNKNOWN / NOT_VALIDATED; qualified stock <3 |
| +10% | 0 | UNKNOWN / NOT_VALIDATED; qualified stock <3 |
| +15% | 0 | UNKNOWN / NOT_VALIDATED; qualified stock <3 |
| +20% | 0 | UNKNOWN / NOT_VALIDATED; qualified stock <3 |

No symbols, hit counts, denominators, or rates are invented. Historical leaders remain separate from the current-day candidate list.

## 4. Three independent engine scorecards

### A — V11.4 Historical Behavioural Selector
**Status: BLOCKED / NOT_ADMISSIBLE.**
- Existing 100-cutoff retrospective summaries are not accepted as verified performance.
- Run #416 audit established that the forward-label construction uses symbol-grouped shift(-1) followed by trailing rolling(h, min_periods=1), allowing partial windows and symbol-local session compression instead of exact exchange sessions T+1…T+h.
- A prior H+5 serialization mismatch remains unresolved: JSON implies 613 hits while row-level CSV has 616.
- H+3 DATA_CONTAMINATED State has 24 matured observations, below the fixed minimum 50; it remains UNKNOWN.
- +2% and +15% independently accepted metrics remain UNKNOWN.
- No corrected v2 implementation was attempted because the research-only v2 specification requires separate explicit approval. No production promotion.

### B — V11.3 Cost-aware Trade Replay
**Status: UNKNOWN / NOT_AUTHORIZED / NOT_RUN.**
No user-approved entry, exit, stop, circuit, sizing, brokerage/tax/slippage assumptions or independently reconciled trade ledger. Cost-adjusted return, win rate, expectancy and drawdown are UNKNOWN. No ranking boost.

### C — Global Capital Rotation
**Status: UNKNOWN / BLOCKED.**
No admitted timestamp/vintage-aligned macro → sector → stock → matured-outcome panel with verified crosswalks. No GCR boost.

## 5. Current candidate list
**Qualified candidates: 0.**

No symbol is promoted from the eight shadow names. For all eight, current official close/time, raw-source manifest linkage, current volume/relative strength, sector confirmation, liquidity, current circuit/surveillance and validated catalyst are incomplete or UNKNOWN. No target price bands, horizon, entry, stop or invalidation levels are generated from stale/missing prices.

## 6. Daily Failure Analysis & Missed-Winner Audit

### Current 2026-11-20 cutoff cohort
- 8 unique shadow symbols / 10 selector rows.
- Outcome status: **PENDING / IMMATURE**. The next exchange session is 2026-11-23; no H+1 failure or success is assigned before that session.
- Current false positives: UNKNOWN, not zero.
- Target-wise missed winners: UNKNOWN; full-universe denominator and row-level predictions are not reconciled.
- Avoidable/unavoidable miss count: UNKNOWN.

### Previously matured 2026-11-19 cutoff cohort — reuse, do not duplicate
The 2026-11-21 Nightly Review already records a 7-unique-symbol / 10-row H+1 shadow post-mortem. It reported descriptive +2% intraday high-touch of 4/7, with ARYAMAN, KDDL and NRL as high-touch misses; ELITECON, HINDOILEXP, LEENEE and YATRA were high-touch hits. The same review explicitly marks this cohort NOT VALIDATED because raw source bytes and the immutable raw-file manifest are absent. Its H+3/H+5 outcomes remain immature. These figures are not admitted as validated capture rates and are not repeated as current performance.
- No full-universe missed-winner list is admissible: Run #339 lacks row-level all-universe predictions and reconciled denominator.
- For the named H+1 misses, stale/missing quote and risk evidence is supported, but the actual causal reason for price non-hit remains UNKNOWN. Hindsight explanations are not promoted to predictive features.

## 7. Failure & Lessons Learned — today's carry-forward
No new independently proven stock-selection error was established today because no new market session/outcome matured. Existing immutable lessons are reused, not duplicated:

| Existing lesson ID | Current evidence/status | Research integration / next verification |
|---|---|---|
| PW-LSN-20261121-001 — forward-label window defect | Root cause VERIFIED; v2 implementation NOT_AUTHORIZED | Keep v1 metrics BLOCKED. If separately approved, run a five-fully-matured-cutoff correctness pilot with exact T+1…T+h session spine, full maturity, point-in-time identity, leakage checks and hand verification. |
| PW-LSN-20261121-002 — H+5 JSON/CSV mismatch | Mismatch SUPPORTED; exact serialization cause UNKNOWN | Reconcile from one canonical row ledger; require integer parity across row ledger, JSON, CSV, summary and manifest before any metric release. |
| PW-LSN-20261121-003 — raw NSE source artifact retention omission | Exact workflow allowlist omission VERIFIED in Continuation 228; isolated audit-branch fix committed; future retention proof PENDING; acquisition-time manifest NOT_DONE | Inspect the next already-authorized bounded artifact only after it exists; verify original raw files, successful URL, timestamp semantics, byte count and SHA-256. Do not redownload old sessions and call them original bytes. |

**আজকের শিক্ষা → গবেষণায় সংযোজন → পরবর্তী যাচাই**
- শিক্ষা: runner-এ successful acquisition/QA হওয়া retained artifact provenance-এর সমান নয়; normalized CSV থাকাও original raw-source replay-এর সমান নয়।
- সংযোজন: daily candidate eligibility stays fail-closed until raw source bytes + per-file manifest + security identity + price timestamp are independently inspectable. This is appended to the existing PW-LSN-20261121-003 line of work; no duplicate lesson ID.
- পরবর্তী যাচাই: future artifact allowlist retention proof; acquisition-time manifest; security-master source/vintage validation; only then current price/volume/circuit gates.
- No selector, threshold, RANKING_SCORE, +1 PRESSURE_FADE or production logic change.

## 8. Prior comparable day change
- 2026-11-21 report: 0 qualified candidates; 8 unique shadow symbols / 10 rows, all not qualified.
- 2026-11-22: no new exchange session, no newly matured cohort, 0 qualified candidates.
- New matured sample count today: 0. Valid performance delta: NOT_COMPARABLE / NOT_AVAILABLE. No improvement or deterioration claim.

## 9. Reproducibility, workflow and archive references
- Master ledger preflight blob: `e02d8dea8963e83be182250ca621deaf10108c69`.
- Prior morning report: `docs/DAILY_UNIFIED_TOP5_SWING_WATCHLIST_20261121.md`, blob `b055c883801b936ce33d3ed2aceeda874956336b`.
- Prior nightly report: `docs/NIGHTLY_ROTATION_BACKTEST_RESEARCH_REVIEW_20261121.md`, blob `1cd8217aed06d6c8021baa5873c467c81208177e`.
- Run #416: run ID `44744602064`, source commit `6572a69776272cbda3fde4fec457bddbf7c58ad5`, conclusion success; artifact ID `14632139339`; ZIP SHA-256 `b12ea634f24af8241ee9a901635dd743195f4b8a3a1511cc2ffe3c3246282082`.
- Run #339: run ID `44799560798`, source commit `624be8f126f39bd6a146d732ec3f87edde964aec`, conclusion success; artifact ID `14660032260`; ZIP SHA-256 `23e74e7f9ef2e32bf5b6bbc5a931814c06fe065835b8bdda74f3c00dbdafd213`.
- Latest relevant prospective audit branch run #365: run ID `44938858340`, conclusion cancelled; it does not provide future raw-retention proof.
- Run #339 raw artifact was 17 entries and omitted original raw NSE CSVs, sessions, acquisition diagnostics, security master and raw manifest despite the job log recording 200 successful full-delivery responses.
- Continuation 228 identified the exact artifact upload allowlist omission and added raw CSV/session/acquisition-diagnostic/security-master paths on isolated branch commit `46f4a359f21da676cb0c92e874fb08f14ee20d90`. Future artifact proof remains pending; per-file acquisition-time manifest remains not done.
- No new workflow dispatch, NSE download, paid source, synthetic row or production change in this report.

## 10. Official source and project links
- [NSE 2026 Capital Market trading-holiday circular NSE/CMTR/71775](https://nsearchives.nseindia.com/content/circulars/CMTR71775.pdf)
- [NSE All Reports — official daily bhavcopy/delivery reports](https://www.nseindia.in/all-reports)
- [Run #416](https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/44744602064)
- [Run #339](https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/44799560798)
- [Run #365 — cancelled audit-only run](https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/44938858340)
- [Prior daily report — 2026-11-21](https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/blob/main/docs/DAILY_UNIFIED_TOP5_SWING_WATCHLIST_20261121.md)
- [Prior nightly failure and lesson audit — 2026-11-21](https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/blob/main/docs/NIGHTLY_ROTATION_BACKTEST_RESEARCH_REVIEW_20261121.md)
- [Run #339 raw-source retention root-cause report — Continuation 228](https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/blob/main/docs/NSE_RUN339_RAW_SOURCE_ARTIFACT_PACKAGING_ROOT_CAUSE_AND_RETENTION_FIX_CONTINUATION228_20261121.md)

## 11. Protected invariants
Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS. ₹0, free official sources only, no synthetic data or fabricated timestamps.
