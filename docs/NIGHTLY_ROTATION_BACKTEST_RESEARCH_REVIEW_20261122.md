# Nightly Rotation Backtest & Research Performance Review — 2026-11-22

**Phase:** Observation only  
**Decision:** No new NSE session or matured watchlist outcome today. V11.4 remains BLOCKED / NOT_ADMISSIBLE; V11.3 replay UNKNOWN / NOT_AUTHORIZED / NOT_RUN; GCR UNKNOWN / BLOCKED.  
**Production impact:** None. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged.

## 1. Ultimate 2% / 5% / 10% / 15% / 20% Stock-Capture Alert

**আজকের বাজার-অবস্থা:** 2026-11-22 রবিবার; regular NSE equity session ছিল না। Morning alert-এর cutoff 2026-11-20; পরবর্তী session 2026-11-23। তাই আজ নতুন matured outcome = 0।

| Target | Horizon | Verified historical hit / miss / eligible unique symbols | Verified capture rate | 22-Nov alert cohort |
|---|---|---|---|---|
| +2% | H+1 | UNKNOWN / UNKNOWN / UNKNOWN | UNKNOWN | 0 matured; 8 immature unique / 10 signal rows; IMMATURE |
| +5% | H+1 | UNKNOWN / UNKNOWN / UNKNOWN | UNKNOWN | 0 matured; 8 immature unique / 10 signal rows; IMMATURE |
| +10% | H+3 | UNKNOWN / UNKNOWN / UNKNOWN | UNKNOWN | 0 matured; 8 immature unique / 10 signal rows; IMMATURE |
| +15% | H+5 | UNKNOWN / UNKNOWN / UNKNOWN | UNKNOWN | 0 matured; 8 immature unique / 10 signal rows; IMMATURE |
| +20% | H+5 | UNKNOWN / UNKNOWN / UNKNOWN | UNKNOWN | 0 matured; 8 immature unique / 10 signal rows; IMMATURE |

- Current shadow cohort: **8 unique symbols / 10 selector rows** — NRL, V2RETAIL, SIGACHI, RSDFIN, KDDL, YATRA, KMCSHIL, HINDOILEXP. Qualified release candidates: **0**. Outcome denominator for matured scoring: **0**; 8 remain excluded as immature. Capture rate is therefore UNKNOWN, not 0%.
- Intraday high-touch, close-to-close hit and executable trade win: all IMMATURE / UNKNOWN for this cohort. No adverse excursion can be scored yet.
- The earlier 19-Nov cohort's +2% 4/7 high-touch observation remains dated and NOT VALIDATED; it is not included in today's cohort or historical scorecard.
- Previous historical diagnostics (+5% H+1 653/2,991; +10% H+3 458/2,975; +20% H+5 164/2,966) remain **NOT VALIDATED** because of the forward-label defect and unresolved reconciliation. They are not verified capture rates.

## 2. Three independent performance scorecards

### Track 1 — V11.4 Historical Behavioural Selector
**BLOCKED / NOT_ADMISSIBLE.** No accepted Precision, Recall, F1, target-hit rate, false-positive/missed-winner count or confidence interval is available. The v1 label code still uses shift(-1) plus trailing rolling with partial windows rather than exact fully matured exchange-session T+1…T+h labels. H+5 JSON/CSV count parity (613 vs 616) remains unresolved. H+3 DATA_CONTAMINATED State has 24 observations, below the fixed 50-observation threshold; State calibration remains UNKNOWN. New leakage-safe validations tonight: **0/10**.

### Track 2 — V11.3 Cost-aware Trade Replay
**UNKNOWN / NOT_AUTHORIZED / NOT_RUN.** No user-approved entry/exit/stop/circuit/position-sizing/overlap assumptions and no independently reconciled execution ledger. Net return, win rate, expectancy, costs, profit factor and drawdown are not calculated.

### Track 3 — Global Capital Rotation (GCR)
**UNKNOWN / BLOCKED.** No admitted synchronized timestamp/vintage-aligned macro → sector → stock → matured-outcome panel or defensible complete crosswalk. The current Macro-Geo recovery attempt failed before P0 source collection; no GCR metric is produced or inferred from V11.3/V11.4.

## 3. Morning Top-5 alert — matured outcome review

- Reused the 2026-11-22 morning report; no new NSE download or 120-minute prospective workflow was launched.
- Cutoff 2026-11-20; all 8 shadow symbols / 10 rows remain pending. H+1/H+3/H+5 hit/miss, adverse excursion and source-time outcome rows are **IMMATURE**, not false positives or misses.
- Current eligibility gates admitted 0 names. No historical winner is promoted as a prospective candidate.
- Symbol-level maturity ledger (cutoff 2026-11-20): each of the following 8 unique names has all target scenarios IMMATURE; per-symbol future-bar adverse excursion is UNKNOWN and no verified per-symbol cutoff price timestamp is admitted in the morning report.

| Symbol | +2% H+1 | +5% H+1 | +10% H+3 | +15% H+5 | +20% H+5 | Adverse excursion | Cutoff source timestamp |
|---|---|---|---|---|---|---|---|
| NRL | IMMATURE | IMMATURE | IMMATURE | IMMATURE | IMMATURE | UNKNOWN | 2026-11-20 cutoff; exact timestamp NOT_VERIFIED |
| V2RETAIL | IMMATURE | IMMATURE | IMMATURE | IMMATURE | IMMATURE | UNKNOWN | 2026-11-20 cutoff; exact timestamp NOT_VERIFIED |
| SIGACHI | IMMATURE | IMMATURE | IMMATURE | IMMATURE | IMMATURE | UNKNOWN | 2026-11-20 cutoff; exact timestamp NOT_VERIFIED |
| RSDFIN | IMMATURE | IMMATURE | IMMATURE | IMMATURE | IMMATURE | UNKNOWN | 2026-11-20 cutoff; exact timestamp NOT_VERIFIED |
| KDDL | IMMATURE | IMMATURE | IMMATURE | IMMATURE | IMMATURE | UNKNOWN | 2026-11-20 cutoff; exact timestamp NOT_VERIFIED |
| YATRA | IMMATURE | IMMATURE | IMMATURE | IMMATURE | IMMATURE | UNKNOWN | 2026-11-20 cutoff; exact timestamp NOT_VERIFIED |
| KMCSHIL | IMMATURE | IMMATURE | IMMATURE | IMMATURE | IMMATURE | UNKNOWN | 2026-11-20 cutoff; exact timestamp NOT_VERIFIED |
| HINDOILEXP | IMMATURE | IMMATURE | IMMATURE | IMMATURE | IMMATURE | UNKNOWN | 2026-11-20 cutoff; exact timestamp NOT_VERIFIED |


## 4. Best 3 Stocks per Target

### Historical winners
For +2%, +5%, +10%, +15% and +20%: **0 qualified names — NOT VALIDATED / BLOCKED**. The contaminated v1 label/ranking lineage cannot support evidence-backed ordering.

### Prospective candidates
For all five targets: **পর্যাপ্ত যাচাইকৃত প্রার্থী নেই — UNKNOWN/BLOCKED**. Eight shadow names remain unqualified; none is represented as a prediction, guaranteed return or buy recommendation.

## 5. Comparable-day change and rolling/baseline status

- Compared with the 2026-11-21 nightly report: qualified candidates remain 0; shadow cohort remains 8 unique symbols / 10 rows; newly matured observations = 0.
- Fixed baseline and latest rolling-window metrics: **NOT_AVAILABLE / NOT_VALIDATED**. No same-sample, same-universe, same-target, same-cost methodology comparison is admissible; percentage-point change and confidence intervals are UNKNOWN.
- No improvement or deterioration claim is made from watchlist turnover or a non-trading day.

## 6. Workflow, archive and artifact verification

### Reused NSE archive
- Run #416 / run ID **44744602064**; dataset SHA-256 **d6810409dbd800e5146e08a1eb1e8b48207354461876acb62cbb2f656fba51db**; 200 sessions (2026-02-16–2026-11-20), 2,999 symbols, 503,892 normalized rows. Reused; no duplicate collection.

### Run #398 — raw-source retention proof
- Run ID **45027842316**, job **137232482609**, overall workflow **CANCELLED** at Step 16; Steps 1–15 completed successfully. Artifact **14757294944**; GitHub digest and independently recomputed ZIP SHA-256 both **212a84103f2a9f47681865c7e165fe0247001b02d9563a5cef578636fb0b1898**; source head **7360870b768a6ed746451afa96ea918a3bffae07**.
- Independent ZIP inspection: 200 raw NSE bhavcopy CSVs and 200 acquisition-manifest entries; **200/200** raw-file byte counts and SHA-256 values independently matched both retained and source manifest values. QA: 200 sessions, 2,999 symbols, 100% delivery quantity/percentage coverage, no issues.
- Strict field-level provenance limitation: all 200 entries contain source URL, retrieval timestamp, source bytes, source SHA-256 and content type, but per-file HTTP status is absent (0/200) and publication timestamp is absent (0/200). Thus raw-byte retention = **PASS for Run #398**; full per-file provenance = **PARTIAL**. This does not recover the original missing Run #339 artifact bytes.

### Run #45038111510 — Macro-Geo recovery failure
- Workflow event head **dc8022b321a7adb41b0d172e792d696db410f4e9**; latest attempt job **137256604023** checked out branch commit **135801ecea21460f565dd22d19439878bb0b49b3**: Steps 1–8 SUCCESS; Step 9 Collect P0 macro market panel and timestamped news FAILED; Steps 10–13 SKIPPED. Log timestamp 2026-11-22T15:27:37Z: **KeyError: 'weekday_requests'** at pipeline/macro_geo_collect_p0.py:530.
- Source inspection confirms nse_index_history() returns observed_session_requests, rows, failures, while main() still indexes archive_report["weekday_requests"]. The caller/return-schema mismatch is VERIFIED; collection stopped before P0 repair, coverage, event study or hard gate.
- Artifact **14759889454**, GitHub digest and independently recomputed ZIP SHA-256 **618fde324b34fef465a1a9190b07825594c39e2d9ab2dc9f84917c9668cac6cb**. Embedded NSE QA and 200-session manifest validation PASS; canonical panel SHA-256 **d6810409dbd800e5146e08a1eb1e8b48207354461876acb62cbb2f656fba51db**. All seven P0 external input files and the repair, collection-manifest, source-coverage, event-study and hard-gate reports are MISSING. Macro-Geo remains BLOCKED.
- Code SHA-256: **255da8657e7cb838a52b2ba328458befb3d51f7000221acc912bef2c4335041a**; workflow YAML SHA-256: **064b85f9a8d2befb71bf02d495586a6136b236c24ff84437072cc7084e789904**. The series registry is inline in the script; no separate config file was executed.

## 7. Selection Failure & Missed-Winner Root-Cause Audit

- Current 2026-11-20 cutoff cohort: 8 unique shadow symbols / 10 rows; all horizons immature. False positives = UNKNOWN; missed winners = UNKNOWN; adverse excursion = UNKNOWN.
- Same-day eligible-universe contrast cannot be computed because Run #339 retained artifact lacks row-level all-universe predictions and reconciled per-cutoff eligible denominators. No symbol is invented as a missed winner.
- Prior 19-Nov shadow post-mortem is reused from the 2026-11-21 report and not duplicated. Its named misses remain descriptive / NOT VALIDATED due missing original raw bytes and immutable manifest.
- No cutoff-time causal attribution is upgraded without timestamped evidence. Selection and missed-winner audit stays observational.

## 8. Proven gaps and next bounded research actions

| Priority | Research action | Acceptance test | Expected artifact | Blocker |
|---|---|---|---|---|
| P0 | Read-only contract test for the Macro-Geo archive report schema | Assert the return keys from nse_index_history() and every caller key agree; fixture of 3 observed sessions; no network calls; <60 sec | archive_report_contract_validation.json + test log | Any code correction requires a separate approved research change; no patch made tonight |
| P1 | Tighten per-file acquisition provenance schema on a future authorized run | 200/200 entries retain actual source URL, retrieval timestamp semantics, HTTP status, content type, byte count and SHA-256; independent byte/hash reconciliation | versioned acquisition manifest + independent validation JSON | Run #398 lacks per-file HTTP status/publication timestamp; old Run #339 bytes remain unavailable |
| P2 | Reconcile Run #339 eligible universe against row-level predictions before missed-winner claims | Per cutoff: eligible + mutually exclusive exclusions reconcile to raw universe; one identity-matched prediction per eligible symbol; matured/excluded counts reconcile | denominator ledger + missed-winner row ledger + reconciliation JSON | Run #339 artifact omitted required row-level exports; historical raw bytes cannot be reconstructed by redownload |

Additional methodology is limited to proven gaps: archive-report schema contract validation; per-file provenance completeness; exact eligible-universe denominator reconciliation; exact forward-session/full-maturity labels; canonical row-ledger JSON/CSV parity. No unrelated scope expansion. The separate forward-label-v2 implementation remains unauthorized pending explicit user approval.

## 9. Daily Lessons-Learned & Research Integration Loop

- Existing PW-LSN-20261121-001 (forward-label defect) and PW-LSN-20261121-002 (H+5 serialization mismatch) are carried forward without duplicate IDs; both remain OPEN/BLOCKED.
- Existing PW-LSN-20261121-003 is updated: Run #398 proves 200/200 raw-file retention and byte/hash parity, but full per-file provenance is PARTIAL because HTTP status and publication timestamp fields are absent. Original Run #339 raw recovery remains BLOCKED.
- New immutable lesson: **PW-LSN-20261122-001** — archive report schema mismatch (weekday_requests vs observed_session_requests), root cause VERIFIED. Expected archive fallback metadata vs actual KeyError; affected Macro-Geo P0 collector; prevention test is the bounded return-schema contract test above.
- Research note added to the Observation-only diagnostic backlog: archive report producer/consumer schema contract test. No selector, threshold, ranking, production code or admission change.
- Duplicate lessons excluded: no duplicate forward-label, H+5 serialization or raw-artifact omission lesson created.
- Acceptance status: new lesson OPEN / NOT_ACCEPTED until the bounded contract test passes and a separately authorized recovery attempt produces the required P0 artifacts.

## 10. Protected invariants

₹0; free official sources only; no synthetic data, forward-fill, guessed mappings, fabricated timestamps or look-ahead. H+3 minimum remains 50 fully matured observations. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS.
