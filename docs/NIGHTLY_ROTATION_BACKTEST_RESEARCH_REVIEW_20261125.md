# PRECISION-WIRES V11.3 — Nightly Rotation Backtest & Research Performance Review
**তারিখ:** ২৫-Nov-2026 (Asia/Kolkata)  
**Status:** PARTIAL / BLOCKED — no validated performance PASS  
**Mode:** Observation only; ₹0; free official sources only

## 1. Ultimate 2% / 5% / 10% / 15% / 20% Stock-Capture Alert

| Target | Horizon | Matured unique hit | Miss | Eligible unique denominator | Capture rate | Signal rows | Status |
|---|---:|---:|---:|---:|---:|---:|---|
| +2% | H+1 | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | BLOCKED |
| +5% | H+1 | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | BLOCKED / NOT_VALIDATED |
| +10% | H+3 | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | BLOCKED / NOT_VALIDATED |
| +15% | H+5 | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | BLOCKED / NOT_VALIDATED |
| +20% | H+5 | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | BLOCKED / NOT_VALIDATED |

Historical high-touch, terminal close-to-close and executable trade win are separate; all three are UNKNOWN for a reconciled historical universe. Executable win is NOT_AUTHORIZED. Capture rate is not profitable return. Earlier +5 H+1 958/2,977, +10 H+3 628/2,892, +15 H+5 381/2,824 and +20 H+5 196/2,824 in the 25-Nov morning report are explicitly NOT_VALIDATED: session spine contains only 187 unique content sessions from 200 labels, forward-label semantics are defective, CI absent, and denominator reconciliation is incomplete. Do not carry these forward as verified results.

**Morning cohort (25-Nov 08:45):** 0 qualified / 5; 23-Nov shadow cohort = 7 unique symbols / 10 selector rows (BI, KDDL, ONIXSOLAR, SALASAR, SHALPAINTS, SHARDUL, UFBL). Its H+1 was due only after 25-Nov close; no post-close validated tracker artifact or fresh row-level price evidence was found in this review. Therefore H+1 remains PENDING/UNKNOWN, not hit or miss. H+3 expected 27-Nov close; H+5 expected 01-Dec close. 24-Nov holiday cutoff's 9 unique / 10 rows remains invalid and excluded.

## 2. Preflight, reused evidence and run inventory

- Read 25-Nov morning watchlist, 25-Nov Failure & Lessons Register, C72–C75 reports, latest continuity ledger entries, prior 24-Nov nightly report and existing retained artifact metadata. Reused already verified ZIP hashes; did not repeat downloads or broad workflow runs.
- Morning report: `docs/DAILY_UNIFIED_TOP5_SWING_WATCHLIST_20261125.md`, blob SHA `2376b36ec30265805facd1d3a94f23833e06a16c`; cutoff 23-Nov close; qualified 0/5. Live 1m feed HTTP 403/zero rows and final selection blocked.
- Latest prospective tracker evidence: Run #410 / ID `45490518576`, artifact `14966627305`, head `ab7287e42921629a89977e551c2ed7410c6ad07c`, conclusion SUCCESS, 9m52s; artifact digest / independently matched ZIP SHA-256 `6b1673af895214ae982fb445a62d5536dd2960eb062dc310b85f955b01c8af16`. This is pre-market/previous-evening evidence, not a 25-Nov post-close outcome.
- Run #410 tracker defect: 23-Nov cohort was incorrectly marked MATURED_T1 with T1_HIGH_PCT while OUTCOME_LAST_DATE was blank; 24-Nov NSE holiday had been counted as the next row. 24-Nov cutoff's 10 rows / 9 unique symbols are invalid. Controlling lesson PW-LSN-20261125-001.
- Run #421 / ID `45422367928`, artifact `14936656169`, ZIP SHA-256 `d57374c50a8b8e2fe5710fd57660225ea59a2beffd639cb9e83b77e734499954`, reused only as prior diagnostic evidence; 12m06s exceeds the 10-minute cap.
- Current 25-Nov Actions inventory showed numerous GCR persistence runs failing; no new post-close prospective-tracker run/artifact for the 23-Nov H+1 cohort was identified. No new broad/120-minute workflow dispatched.
- Current ledger blob SHA reported by GitHub: `2b95a954fe1b43c12f2313e9f7c915c199c15a86`; morning and lesson-register blob SHAs recorded above.

## 3. Three independent performance tracks

| Track | Status | Evidence-based conclusion |
|---|---|---|
| A — V11.4 Historical Behavioural Selector | **BLOCKED / NOT_VALIDATED** | No Precision, Recall, F1, target-hit rate, FP, missed-winner rate or CI admitted. Dataset/session spine and forward labels are invalid; H+5 JSON/CSV parity unresolved. H+3 State calibration UNKNOWN; minimum 50 fully matured observations per State not independently demonstrated. |
| B — V11.3 Cost-aware Trade Replay | **UNKNOWN / NOT_AUTHORIZED** | User-approved entry/exit/stop/circuit/position-sizing/overlap/cost assumptions and independently reconciled replay absent. Net return, win rate, expectancy, costs, profit factor and drawdown not reported. |
| C — Global Capital Rotation | **UNKNOWN / BLOCKED** | No synchronized timestamp/vintage-aligned macro-sector-stock panel, validated crosswalk and matured outcomes. Macro-Geo P0 6/8; final FPI/DII history and USD/INR historical archive remain blockers. |

No accepted rolling/walk-forward validation was run today. The existing 100-cutoff and 30-cutoff diagnostics remain exploratory/NOT_ACCEPTED; no new methodology series or comparable performance delta can be claimed. Daily cap of 10 validation jobs respected (0 new validation jobs).

## 4. Best 3 Stocks per Target

**Historical winners:** +2%, +5%, +10%, +15%, +20% — all UNKNOWN/BLOCKED. No independently verified matured stock-level ranking with reconciled unique-symbol denominator and leakage-safe labels.

**Prospective candidates:** no qualified candidates for the next session. All five slots are UNFILLED — INSUFFICIENT VERIFIED EVIDENCE. The morning alert had 0/5 qualified; current official price/time, current price-volume/RS, liquidity/circuit and synchronized catalyst evidence were not verified. No provisional stock is promoted. No probability or target price invented.

## 5. Morning alert outcome review and comparable-day changes

- 25-Nov morning alert had 0 qualified candidates; hence no qualified selected-stock forecast to score.
- 23-Nov shadow cohort has 7 unique symbols / 10 signal rows. H+1 due 25-Nov close, but no fresh post-close official/archived row-level evidence or calendar-correct tracker artifact is available; retain PENDING. H+3 and H+5 remain immature.
- 24-Nov holiday cohort excluded (9 unique / 10 rows).
- False positives, missed winners and adverse excursion for today's matured cohort: UNKNOWN; no valid denominator.
- Fixed baseline vs latest rolling window: NOT_COMPARABLE / UNKNOWN. Archive semantic defects, label defects and absent post-close evidence prevent same-universe/methodology comparison. No pp change or improvement claim.

## 6. Selection Failure & Missed-Winner Root-Cause Audit

- Matured selected failures: UNKNOWN (no valid matured outcomes).
- Matured selected hits: UNKNOWN.
- Same eligible-universe missed winners: UNKNOWN; canonical point-in-time decision/exclusion ledger and reconciled valid outcomes absent.
- False-positive vs missed-winner contrast cannot be computed. No hindsight-only cause assigned.
- Confirmed process/data issue: PW-LSN-20261125-001 — tracker used next sorted price row rather than next official trading session and omitted H+1/H+3 outcome-end date. Root cause CONFIRMED at code/contract level; individual price impact UNKNOWN.
- Research-only prevention test: require versioned official NSE session spine; exact next 1/3/5 official sessions; reject holidays/missing/duplicate/conflicting rows; require horizon-specific outcome end date matching expected session; test 23-Nov→25-Nov/27-Nov/01-Dec plus second holiday-adjacency and missing-calendar cases on two retained artifacts. Expected artifact: `calendar_aware_tracker_regression.json`. Acceptance OPEN; implementation not run.

## 7. Highest-value next research actions (max 3)

1. **Calendar-aware prospective tracker regression (audit-only branch).** Acceptance: 24-Nov excluded; 23-Nov H+1/H+3/H+5 end dates exactly 25-Nov/27-Nov/01-Dec; missing/duplicate/non-session rows remain PENDING; per-horizon end-date fields required. Artifact: `calendar_aware_tracker_regression.json`. Blocker: offline implementation/test not yet completed; no production integration.
2. **Post-close 23-Nov cohort reconciliation.** Acceptance: official valid-session date and raw source timestamp for each symbol; 7 unique symbols vs 10 signal rows; exact high/close/adverse excursion per target; missing data excluded and explained. Artifact: `PW-ALERT-20261123-H1-POSTCLOSE-RECON.json`. Blocker: no fresh post-close artifact in current run inventory; automated NSE acquisition not permitted absent applicable permission.
3. **Session-spine + forward-label evidence contract.** Acceptance: 200 distinct valid official sessions and DATE1/requested-date parity; exact T+1…T+h labels; terminal close distinct from high-touch; JSON/CSV integer parity; cutoff-cluster CI only after acceptance. Artifact: `session_label_reconciliation_v2.json`. Blocker: retained archive has 187 unique content sessions; raw source manifest absent; forward-label implementation remains defective and requires separate approval before code changes.

No unrelated scope added. No NSE data acquisition, paid source, new workflow dispatch or 120-minute workflow run.

## 8. আজকের শিক্ষা ও গবেষণায় সংযোজন

- **New lesson:** none; PW-LSN-20261125-001 already exists and is carried forward, not duplicated.
- **Updated evidence:** today's review confirms no post-close tracker artifact was surfaced and the 23-Nov H+1 result must remain PENDING until row-level valid data is reconciled.
- **Duplicate lessons excluded:** holiday/session-spine, forward-label, denominator/CI, source-health, high-touch-vs-close/executable and export-manifest lessons retain their existing immutable IDs.
- **Observation note:** calendar-aware tracker acceptance test and post-close cohort reconciliation carried forward; no new performance claim or selector change.
- **Next verification:** run the bounded offline calendar regression; then reconcile 23-Nov cohort only with official valid-session observations. Re-check PW-LSN-20261125-001 acceptance before any future maturity label is accepted.

## 9. Controls and final status

No Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E or IPO-PLX V2.0 changes. No threshold/ranking/production admission change. ₹0; free official sources only; no synthetic data, forward-fill, guessed mappings, fabricated timestamps or look-ahead. UNKNOWN never PASS.

**Overall: PARTIAL / BLOCKED.** This report does not certify performance. GitHub report creation succeeded (commit 24371d62112d6070977fda5bb242c1f5a0839575; blob SHA-1 cdc3b9d1332733cbb0131f361251891bf829dc99). Lessons Register append succeeded (commit 4fc73b80adc094a5d054ddd03fd972f9d8de5421; read-back blob SHA-1 c9b997ad5842ad8dd45dfd5496c88a32b85a16ef). Master Continuity Ledger append succeeded (commit 5011647885a21e0917d85ba691d86ef6010ee6ac; read-back blob SHA-1 54f01e2822faf101e6fcc54ff8952ba142d996c3). All three files were read back and their Git blob IDs matched the returned write results. Markdown report SHA-256 was not independently computed; therefore no SHA-256 acceptance is claimed.
