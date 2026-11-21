# Nightly Rotation Backtest & Research Performance Review — 2026-11-21

**Phase:** Observation only  
**Decision:** V11.4 historical performance claims BLOCKED / NOT_ADMISSIBLE; V11.3 cost-aware replay UNKNOWN / NOT_AUTHORIZED / NOT_RUN; GCR UNKNOWN / BLOCKED.  
**Production impact:** none. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged.

## 1. Preflight, continuity and evidence reused

- Main branch head at preflight: 6adb896eeb83cf0ef8564d71084d2e0bc97ed8f6.
- Master Continuity Ledger re-read: docs/PRECISION_WIRES_V11_3_CONTINUITY_ACCEPTANCE_LEDGER.md, Git blob SHA-1 916e9a9b79beca13b4526c25e1d9a4ea4f11f5f3. Its tail ends at GCR Continuation 220; no dated Lessons Learned Register/section or prior immutable lesson IDs were present. Header still says last reconciled 2026-11-08.
- Previous nightly report re-read: docs/NIGHTLY_ROTATION_BACKTEST_RESEARCH_REVIEW_20261120.md, blob SHA-1 617088f30f0430f91929688299d179b59d136fca, content SHA-256 87fad4166ce5c71252188ac91ba1ef0dc1689ae6890a4ceb6d4fece2bd1aba1e.
- Today's morning alert re-read: docs/DAILY_UNIFIED_TOP5_SWING_WATCHLIST_20261121.md, blob SHA-1 b055c883801b936ce33d3ed2aceeda874956336b, content SHA-256 652bc7717d6cd5206005ae49ff4e77329c4f39b86eeded4971fa0dfef5dab0dc.
- Forward-label v2 acceptance specification re-read: docs/V11_4_FORWARD_LABEL_V2_RESEARCH_ONLY_ACCEPTANCE_SPEC_CONTINUATION89_20261120.md, blob SHA-1 c445b4f115a93d75dc9745790c76d7bbd9a0e145, content SHA-256 9fbd4e8f1e441395e06d667b3585a408a7e78d1398bb7a0ed3d3d6567409a218. It explicitly says implementation and production admission are NOT AUTHORIZED; no implementation was attempted.
- Reused archive Run #416, ID 44744602064, commit 6572a69776272cbda3fde4fec457bddbf7c58ad5, success. Artifact 14632139339, GitHub digest SHA-256 b12ea634f24af8241ee9a901635dd743195f4b8a3a1511cc2ffe3c3246282082; current metadata read-back matches the prior independent verification. Dataset SHA-256 d6810409dbd800e5146e08a1eb1e8b48207354461876acb62cbb2f656fba51db; archive coverage 200 sessions (2026-02-16–2026-11-20), 2,999 symbols, 503,892 rows.
- Reused morning prospective Run #339, ID 44799560798, commit 624be8f126f39bd6a146d732ec3f87edde964aec, success. Artifact 14660032260; GitHub digest SHA-256 23e74e7f9ef2e32bf5b6bbc5a931814c06fe065835b8bdda74f3c00dbdafd213. The alert report documents 8 unique shadow symbols / 10 selector rows and zero qualified candidates.
- Current source file pipeline/walk_forward_backtest.py remains Git blob SHA-1 d085f7a2d35a88b4c4eaba65144a429a06961b09; content SHA-256 dca7363ef1c5f56a097ed66b4305935f2c90975e2387b9c5b44780c4101f83e2. This is the same source blob identified by the prior audit.
- Prior audit script SHA-256 3a69c353a03d77f871f7bd52b120dd43633bf11228fcc0cdcd4bfc83e03f4a2b; prior audit config SHA-256 1d17284e1c4a16e59e51a0d117a8b1e9888cfba39bd5378ce1c61dfca1c6d8a8.
- No new workflow was dispatched; no 120-minute workflow was run. 21-Nov-2026 is Saturday, so there is no new NSE session after the 20-Nov cutoff. No new rolling validation job was started: the known P0 label defect and the explicit v2 approval boundary make another v1 score run invalid.

## 2. Ultimate 2% / 5% / 10% / 15% / 20% Stock-Capture Alert

**Verified historical capture:** all five targets UNKNOWN / NOT VALIDATED. The 2026-11-20 corrected-label diagnostic is still contaminated by the selector/training path and is not promoted to verified performance. The 21-Nov morning alert has zero qualified candidates; its eight shadow picks are not outcome-mature.

| Target | Intended horizon | Verified matured historical hit / miss / eligible unique symbols | Capture rate | Dated 19-Nov shadow cohort — H+1 only | 21-Nov alert cohort |
|---|---|---|---|---|---|
| +2% | H+1 | UNKNOWN / UNKNOWN / UNKNOWN | UNKNOWN | 4 hit / 3 miss / 7 unique; 57.14% intraday high-touch; NOT VALIDATED | 0 qualified; 8 shadow symbols, 10 rows; IMMATURE |
| +5% | H+1 | UNKNOWN / UNKNOWN / UNKNOWN | UNKNOWN | 0 / 7 / 7; 0.00% H+1 high-touch; NOT VALIDATED | 0 qualified; 8 shadow symbols, 10 rows; IMMATURE |
| +10% | H+3 | UNKNOWN / UNKNOWN / UNKNOWN | UNKNOWN | H+1 observation only: 0 / 7; H+3 IMMATURE | 0 qualified; H+3 IMMATURE |
| +15% | H+5 | UNKNOWN / UNKNOWN / UNKNOWN | UNKNOWN | H+1 observation only: 0 / 7; H+5 IMMATURE | 0 qualified; H+5 IMMATURE |
| +20% | H+5 | UNKNOWN / UNKNOWN / UNKNOWN | UNKNOWN | H+1 observation only: 0 / 7; H+5 IMMATURE | 0 qualified; H+5 IMMATURE |

**Cohort definitions and safeguards**
- The dated 19-Nov cutoff cohort contains 7 unique symbols represented by 10 selector rows. Its next-session OHLC review in the prior report is descriptive only: raw source bytes and immutable raw-file manifest are absent from the retained archive evidence. Therefore its 4/7 result is not an independently source-reconciled capture metric and remains NOT VALIDATED.
- For that same H+1 cohort, +2% close-to-close hit was 1/7 (ELITECON only); +2% intraday high-touch was 4/7. For +5%, +10%, +15% and +20%, H+1 high-touch was 0/7. These are not H+3/H+5 results.
- Unique symbols are counted once per cutoff and target. The 7-symbol/10-row cohort must not be presented as 10 independent stocks. The 21-Nov alert's eight shadow symbols are also distinct from its 10 selector rows.
- Intraday high-touch, close-to-close hit and executable trade win are separate. Executable trade wins are UNKNOWN because no approved entry/exit/stop/circuit/cost assumptions or reconciled trade ledger exist.
- Capture rate is not profitable return. No target result is inferred for the 21-Nov cohort before its future sessions mature.

## 3. Best 3 Stocks per Target

### Historical winners
For +2%, +5%, +10%, +15% and +20%: **NOT VALIDATED / BLOCKED — no stock can be evidence-ranked from the contaminated v1 label/ranking path.** No historical-winner names are promoted.

### Prospective candidates
For all five targets: **পর্যাপ্ত যাচাইকৃত প্রার্থী নেই — UNKNOWN/BLOCKED.** The 21-Nov alert has zero qualified candidates. Its eight experimental shadow names (NRL, V2RETAIL, SIGACHI, RSDFIN, KDDL, YATRA, KMCSHIL, HINDOILEXP) fail one or more current identity/price/time/volume/liquidity/surveillance evidence gates. Shadow rank is not a calibrated probability. No prediction, buy recommendation or guaranteed-return claim is made.

## 4. Three independent performance scorecards

### Track 1 — V11.4 Historical Behavioural Selector

**Status: BLOCKED / NOT_ADMISSIBLE.** The source still uses symbol-grouped shift(-1) followed by trailing rolling(h, min_periods=1), not the required exact forward market-session window T+1…T+h. It skips missing symbol-session rows and admits partial windows. Those labels also feed the training/probability/ranking path, contaminating the frozen selections.

The following figures are carried forward solely as **NOT VALIDATED post-hoc diagnostics** from Run #416; they are not verified alert rates:

| Target | Top-30 mature / immature | TP / FP | Eligible mature / immature | Eligible winners / FN | Precision (95% CI) | Recall (95% CI) | F1 (95% CI) |
|---|---:|---:|---:|---:|---:|---:|---:|
| +5% H+1 | 2,991 / 9 | 653 / 2,338 | 251,426 / 594 | 22,468 / 21,815 | 21.83% (19.53–24.20) | 2.91% (2.63–3.20) | 5.13% (4.66–5.63) |
| +10% H+3 | 2,975 / 25 | 458 / 2,517 | 250,356 / 1,664 | 16,519 / 16,061 | 15.39% (13.57–17.34) | 2.77% (2.49–3.07) | 4.70% (4.23–5.19) |
| +20% H+5 | 2,966 / 34 | 164 / 2,802 | 249,447 / 2,573 | 5,184 / 5,020 | 5.53% (4.64–6.45) | 3.16% (2.69–3.66) | 4.02% (3.42–4.65) |

- +2% and +15% have no independently accepted historical metric in this run. No extra target metric is manufactured.
- The prior H+5 serialization mismatch remains unresolved: metrics JSON implies 613 hits while the row-level CSV has 616. Integer denominator/count parity is a hard failure.
- H+3 State DATA_CONTAMINATED has 24 matured observations, below the mandatory 50-per-State floor; it remains UNKNOWN. No State calibration is accepted.
- Confidence intervals above are cutoff-cluster bootstrap diagnostics only; they do not repair the labels or contaminated ranking path.

**Fixed reference vs latest rolling window — diagnostic only, not a valid improvement claim**

| Target | Metric | Fixed first 80 cutoffs | Latest 20 cutoffs | Difference |
|---|---|---:|---:|---:|
| +5% H+1 | Precision | 19.90% | 29.55% | +9.65 pp |
|  | Recall | 2.98% | 2.73% | −0.25 pp |
|  | F1 | 5.18% | 4.99% | −0.19 pp |
| +10% H+3 | Precision | 14.05% | 20.74% | +6.68 pp |
|  | Recall | 2.81% | 2.67% | −0.15 pp |
|  | F1 | 4.69% | 4.73% | +0.04 pp |
| +20% H+5 | Precision | 5.10% | 7.24% | +2.14 pp |
|  | Recall | 3.04% | 3.57% | +0.53 pp |
|  | F1 | 3.81% | 4.79% | +0.98 pp |

Sample counts fixed → latest: H+1 Top-30 mature 2,392→599, eligible mature 197,963→53,463, eligible winners 15,975→6,493; H+3 2,377→598, 197,167→53,189, 11,870→4,649; H+5 2,372→594, 196,485→52,962, 3,981→1,203. Same defective label/ranking lineage; no statistical improvement claim is admissible.

### Track 2 — V11.3 Cost-aware Trade Replay

**Status: UNKNOWN / NOT_AUTHORIZED / NOT_RUN.** User-approved entry, exit, stop, circuit, position sizing and overlap assumptions plus an independently reconciled execution ledger are absent. Net return, win rate, expectancy, costs, profit factor and drawdown are not calculated.

### Track 3 — Global Capital Rotation (GCR)

**Status: UNKNOWN / BLOCKED.** No synchronized publication-time/vintage-aligned macro → sector → stock panel with defensible sector/stock crosswalk and matured outcomes is admitted. Source-rights and exact sector mapping gaps remain. V11.4/V11.3 statistics are not attributed to GCR.

## 5. Today's morning alert — maturity review

- 21-Nov report cutoff is 20-Nov; it records zero qualified candidates and 8 experimental shadow symbols across 10 selector rows. The next regular session is 23-Nov; 21-Nov is Saturday and 24-Nov is a full NSE capital-market holiday per the morning report's official circular reference.
- All eight current shadow symbols are future-labelled/unmatured at this review. H+1/H+3/H+5 outcome rows, adverse excursion and target-hit status are therefore IMMATURE, not misses.
- No fresh price/volume/circuit/surveillance evidence is promoted from shadow rank. No H+1 score enters the historical scorecard tonight.

## 6. Change vs previous comparable report

- Compared with the 20-Nov nightly report, there is no new NSE session or newly matured historical cutoff. New matured sample count = 0; valid percentage-point change = NOT_COMPARABLE / NOT_AVAILABLE. No improvement or deterioration claim.
- Morning shadow list turnover only: prior 7 unique symbols → current 8; retained NRL, KDDL, YATRA, HINDOILEXP (4); new V2RETAIL, SIGACHI, RSDFIN, KMCSHIL (4); removed ELITECON, LEENEE, ARYAMAN (3). This is selector-list turnover, not performance.
- Run #339 and Run #416 are different artifacts and scopes. Their aggregate metrics are not directly compared.

## 7. Validation jobs and reproducibility

- New leakage-safe rolling/walk-forward jobs tonight: **0 of maximum 10**. No job was appropriate while the existing v1 labels remain invalid and v2 implementation is explicitly unauthorized.
- Run #416 total workflow wall-clock from created_at to updated_at was about 10m18s, slightly above the requested 10-minute ceiling; its walk-forward step itself was recorded at about 4m59s. Do not rerun the full workflow just for scorecard output. Split any future approved repair into bounded jobs, target 20–60 seconds and hard-stop below 10 minutes.
- Run #339 completed in about 8m11s and is reused only for its morning shadow-list/provenance findings.
- No new artifact or workflow run ID was created tonight. Reused run/artifact references are listed in Section 1. The dataset, script, prior report, morning report and acceptance-spec hashes above provide reproducibility anchors; no new config was executed.

## 8. Proven gaps and next-day priority actions

| Priority | Exact action | Acceptance test | Expected artifact | Blocker |
|---|---|---|---|---|
| P0 | After separate explicit user approval only, implement forward_label_v2 in an isolated research branch; do not overwrite v1 or feed production | Exact exchange-session spine T+1…T+h; missing middle session does not compress; full h-session maturity; point-in-time identity/vintage and corporate-action gates; future-feature/T-day leakage tests; exact denominator conservation; JSON/CSV/summary/manifest integer parity; independent hand-check; reproducible hashes; each job <10 min | Versioned v2 code/config, tests, canonical row ledger, per-cutoff denominator ledger, manifest, independent validation report | Explicit user approval absent; production admission separately prohibited |
| P1 | Recover the already-acquired 20-Nov raw NSE bhavcopy/delivery/security-master bytes and raw manifest from an existing authorized archive | Every expected file has URL, publication/retrieval timestamp semantics, byte count and SHA-256; 200-session file/session coverage reconciles; no inferred or substituted rows | Immutable raw-source manifest and recovery receipt | Run #339 artifact omits raw files/manifest; no verified existing archive location in this review |
| P2 | Reconcile Run #339 main-model all_by_date recall denominator with the eligible-universe export before any full-universe recall/missed-winner claim | Per-cutoff raw rows = eligible + mutually exclusive exclusions; every eligible symbol/cutoff has one identity-matched prediction row; matured/excluded totals reconcile; independent recomputation | Per-cutoff denominator ledger, missed-winner row ledger and reconciliation JSON | Run #339 retained artifact lacks row-level predictions; Run #416 reconciliation cannot be silently substituted for Run #339 |

Additional methodology is limited to these proven gaps: (1) forward-session/maturity state machine; (2) canonical row-ledger serialization parity; (3) immutable raw-source manifest; (4) exact eligible-universe denominator reconciliation. No unrelated scope expansion.

## 9. Selection Failure & Missed-Winner Root-Cause Audit

### Today's 21-Nov alert cohort
No qualified stock was released. The eight shadow picks have no matured outcome because their cutoff is 20-Nov and the next market session is 23-Nov. Therefore today's false-positive count and missed-winner count are both UNKNOWN/IMMATURE, not zero.

### Prior 19-Nov cutoff shadow cohort — H+1 matured on 20-Nov
This is a seven-unique-symbol / ten-signal-row shadow cohort, not a qualified production alert. Its outcomes are descriptive and NOT VALIDATED due the missing raw source bytes/manifest.

| Symbol | H+1 high / close return | +2% high-touch | Cutoff-time evidence and root-cause status |
|---|---:|---|---|
| ARYAMAN | +0.80% / +0.18% | Miss | ISIN/series, official quote, catalyst, liquidity and surveillance were UNKNOWN at cutoff. Actual reason for non-hit: UNKNOWN. Evidence gap: SUPPORTED. |
| KDDL | +1.50% / −1.26% | Miss | Last quote was 17-Nov intraday, already +11.61%, with 20% band and near 52-week high; no verified 19-Nov close or fresh catalyst. Stale evidence as an exclusion reason: SUPPORTED; causal reason for price non-hit: UNKNOWN. |
| NRL | +0.57% / +1.08% | Miss | Last quote was 13-Nov close; dated snapshot showed BE series, 5% band, 100% applicable margin and impact cost 2.31. Stale quote/execution-friction concern: SUPPORTED; causal reason for price non-hit: UNKNOWN. |
| ELITECON | +4.88% / +4.65% | Hit | ISIN verified, but current quote, volume and surveillance were not verified; this was a shadow rank, not a qualified alert. |
| HINDOILEXP | +3.14% / +1.08% | Hit | 19-Nov intraday quote only; ST ASM-1, P/E above 50 and 50% margin were recorded. Risk-gate concern: SUPPORTED; no executable win inferred. |
| LEENEE | +2.91% / +1.11% | Hit | Official ISIN/series and current quote/liquidity/surveillance were UNKNOWN. Identity/evidence gap: SUPPORTED. |
| YATRA | +3.94% / −1.03% | Hit | Mixed Q2 filing already public; current price/volume/RS/liquidity were UNKNOWN. Catalyst freshness and market-data gap: SUPPORTED. |

- H+1 +2% high-touch misses: 3 unique symbols (ARYAMAN, KDDL, NRL), 5 selector rows. The 4 high-touch hits represent 4 unique symbols and 5 selector rows. H+1 +2% close-to-close hit was ELITECON only (1/7).
- The 5%, 10%, 15% and 20% H+1 high-touch outcomes were 0/7 in this descriptive cohort. H+3/H+5 remain immature; no longer-horizon miss is asserted.
- No true full-universe missed-winner list can be verified: Run #339 lacks row-level all-universe predictions/denominator reconciliation. Do not infer missed winners from a partial shadow shortlist.
- No cutoff-time evidence establishes a single causal market explanation for ARYAMAN/KDDL/NRL misses. Root causes remain UNKNOWN; only the stale/missing evidence and risk flags above are SUPPORTED. No causal claim or selector/filter change is made.

## 10. আজকের শিক্ষা ও গবেষণায় সংযোজন

No earlier immutable lesson IDs/register were present in the master ledger. The following first formal entries consolidate already documented incidents; they are not claims that the defects were newly discovered tonight.

| Immutable lesson ID | Incident / confidence | Evidence and hashes | Affected area | Recurrence-prevention test / acceptance |
|---|---|---|---|---|
| PW-LSN-20261121-001 | Forward-label window is trailing/partial, not exact forward sessions — VERIFIED | Run #416 / artifact 14632139339 / ZIP SHA-256 b12ea634f24af8241ee9a901635dd743195f4b8a3a1511cc2ffe3c3246282082; source commit 6572a69776272cbda3fde4fec457bddbf7c58ad5; code blob SHA-1 d085f7a2d35a88b4c4eaba65144a429a06961b09; code SHA-256 dca7363ef1c5f56a097ed66b4305935f2c90975e2387b9c5b44780c4101f83e2; dataset SHA-256 d6810409dbd800e5146e08a1eb1e8b48207354461876acb62cbb2f656fba51db; config SHA-256 1d17284e1c4a16e59e51a0d117a8b1e9888cfba39bd5378ce1c61dfca1c6d8a8 | V11.4 label generation, target labels and contaminated ranking/training path | Exact T+1…T+h session spine; missing middle session remains incomplete; T not counted as T+1; full horizon required; hand-check actual archived rows |
| PW-LSN-20261121-002 | H+5 JSON vs row-ledger CSV integer mismatch (613 vs 616) — SUPPORTED | Run #416 report blob SHA-1 617088f30f0430f91929688299d179b59d136fca; prior report content SHA-256 87fad4166ce5c71252188ac91ba1ef0dc1689ae6890a4ceb6d4fece2bd1aba1e; artifact 14632139339 / ZIP SHA-256 b12ea634f24af8241ee9a901635dd743195f4b8a3a1511cc2ffe3c3246282082 | Metric serialization and denominator QA | One canonical row ledger generates JSON/CSV/summary/manifest; exact integer equality, independent recomputation, zero unexplained mismatch |
| PW-LSN-20261121-003 | Raw NSE source files/immutable manifest absent from retained Run #339 artifact — SUPPORTED | Run #339 ID 44799560798 / artifact 14660032260 / ZIP SHA-256 23e74e7f9ef2e32bf5b6bbc5a931814c06fe065835b8bdda74f3c00dbdafd213; source commit 624be8f126f39bd6a146d732ec3f87edde964aec; alert report blob SHA-1 b055c883801b936ce33d3ed2aceeda874956336b; alert report content SHA-256 652bc7717d6cd5206005ae49ff4e77329c4f39b86eeded4971fa0dfef5dab0dc | Raw-source provenance and current candidate eligibility | Require per-file URL, timestamps, byte count and SHA-256 plus independently inspectable raw bytes before current-price/candidate evidence can pass |

- Research integration: these three documented gaps are appended to the Observation-phase Lessons Learned Register in the Master Continuity Ledger. No separate research note, selector, threshold, rank, score, workflow or production code is changed.
- Duplicate lessons excluded: none with an existing immutable ID was found; prior narrative evidence is linked rather than repeated as a separate incident.
- Acceptance status: all three lessons recorded; all three recurrence-prevention tests remain OPEN / NOT_ACCEPTED until a future authorized validation produces evidence.
- Next verification: read this register first; check v2 approval status; verify raw manifest recovery; require exact integer parity before any metric release.
- Protected invariants unchanged; ₹0; free official sources only; UNKNOWN is never PASS.
