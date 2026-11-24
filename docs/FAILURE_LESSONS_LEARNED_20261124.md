# FAILURE & LESSONS LEARNED — ২৪ নভেম্বর ২০২৬
## PRECISION-WIRES V11.3 — Daily Research Register

**আজকের market status:** NSE equity market holiday (24-Nov-2026); next session 25-Nov-2026. No fresh equity price is claimed.

## 1. New immutable lessons

### PW-LSN-20261124-001 — Audit runtime exceeded 10-minute target
- **Evidence:** Run #420 / 45202379089 completed successfully but elapsed 12m11s; artifact #14833925413, ZIP SHA-256 `693cb2d8f68cc38a56fd9c17140f6126e11bb1617d6b0fee9ad4d2de5264686d`.
- **Confirmed root cause:** the scheduled workflow combined broad acquisition, 200-session build, multiple engine/backtest steps, Macro-Geo collection, live feed and diagnostics in one run.
- **Why not caught:** success/conclusion was emphasized while elapsed time was not a blocking acceptance field.
- **Research question:** can the already identified offline audit steps be split into independent jobs that each complete under 10 minutes without rerunning PASS work?
- **Reproducible test:** time the existing offline DATE1/manifest parity, target-label reconciliation, and 1,032-row decision-ledger validation separately using retained artifacts only.
- **Out-of-sample/leakage plan:** these are data/QA tests, not predictive model training; validate on a second independently retained artifact and verify identical outputs/hashes.
- **Result/confidence:** duration breach CONFIRMED; decomposition test OPEN / NOT_ACCEPTED.
- **Carry-forward:** do not dispatch another broad workflow; split the next offline audits and record wall-clock duration per step.

### PW-LSN-20261124-002 — Final selection must fail closed when GEO/live source is unavailable
- **Evidence:** Run #420 `final_selection_status.json` = `PROVISIONAL_ONLY_FINAL_SELECTION_BLOCKED`; blockers `RISK_GEO_NOT_AVAILABLE` and `LIVE_INTRADAY_1M_FEED_MISSING`. `live_1m_status.json` records HTTP 403, rows 0, symbols 0, captured_at 2026-11-23T15:20:28.603510+00:00.
- **Confirmed root cause:** required source/readiness gates were not satisfied. This is a confirmed data-access/readiness gap, not proof that a stock ranking was wrong.
- **Why not caught:** provisional Top-N files exist even when final readiness is blocked; they can be mistaken for actionable candidates unless the terminal state is read first.
- **Research question:** can every daily report derive qualified-candidate count only from final_selection_status after checking each source's status, timestamp, row count and error?
- **Reproducible test:** offline fixture test using the retained JSON: GEO missing or live 1m rows=0/HTTP403 must force qualified_count=0 and prevent any provisional Top-N row from being labelled qualified.
- **Out-of-sample/leakage plan:** test on at least three distinct archived runs with different blocker combinations; no future price/outcome fields in the gate.
- **Result/confidence:** blocker state CONFIRMED; regression test OPEN / NOT_ACCEPTED.
- **Carry-forward:** add a source-health/readiness matrix to every pre-market report; HTTP 403 remains BLOCKED, never fallback PASS.

### PW-LSN-20261124-003 — Intraday high-touch is not close-to-close or executable profit
- **Evidence:** prior WELSPUNLIV observation, 20-Nov cutoff to 23-Nov H+1: +2% intraday high-touch HIT; close-to-close +0.74% MISS; +5% H+1 MISS; adverse excursion −2.52%.
- **Confirmed root cause:** the observed target label and the close-to-close result are different outcome definitions. No causal trading loss or executable fill is inferred.
- **Why not caught:** a single “target hit” label can hide whether the move was only intraday and then reversed.
- **Research question:** do target-hit rankings change materially when high-touch, close-to-close, adverse excursion and cost-aware executable outcomes are reported separately?
- **Reproducible test:** on matured historical rows, generate separate labels for high-touch, close-to-close, adverse excursion and (only after user-approved assumptions) executable replay; reconcile counts per symbol/cutoff.
- **Out-of-sample/leakage plan:** freeze cutoff-time features; calculate each outcome only after its valid exchange-session horizon; compare on later untouched cutoffs.
- **Result/confidence:** label divergence CONFIRMED; strategy implications UNKNOWN.
- **Carry-forward:** show all outcome definitions separately; never call a high-touch hit “profitable trade” or “win rate”.

## 2. Existing lessons carried forward — no duplicate IDs

- **PW-LSN-20261123-001:** 200 requested labels contain only 188 unique valid sessions; 12 holiday duplicate dates. Root cause remains verified; 200-session acceptance NOT_MET.
- **PW-LSN-20261123-002:** source timestamp timezone contract remains UNKNOWN; do not join unzoned times as UTC.
- **PW-LSN-20261123-003:** maturity calendar is anchored to the cutoff and valid exchange sessions. For 23-Nov cutoff: H+1=25-Nov, H+3=27-Nov, H+5=01-Dec (24-Nov holiday excluded).
- **PW-LSN-20261123-004 HINDOILEXP:** +2/+5 H+1 missed-winner incident; cutoff RVOL 0.39× and prior ASM/high-valuation warnings were known. SUPPORTED risk trade-off, not causal proof.
- **PW-LSN-20261123-005 SHALPAINTS:** +2/+5 H+1 missed-winner; low-RVOL gate plausible (0.08×); exact decision row absent. HYPOTHESIS.
- **PW-LSN-20261123-006 HITECH:** +2/+5 H+1 missed-winner; weak EMA/volume confirmation plausible. HYPOTHESIS.
- **PW-LSN-20261123-007 ITI:** +2/+5 H+1 missed-winner; weak trend/participation plausible. HYPOTHESIS.
- **PW-LSN-20261123-008 THOMASCOOK:** missed-winner cause UNKNOWN; decision row absent.
- **PW-LSN-20261123-009 AJMERA:** missed-winner cause UNKNOWN; decision row absent despite high RVOL.
- **PW-LSN-20261123-010:** full-universe 1,032-row candidate-decision export missing; 255 remaining +2% and 35 remaining +5% missed winners stay UNKNOWN.

## 3. Current cohort maturity
- 23-Nov cutoff shadow picks: BI, ONIXSOLAR, SHALPAINTS, SALASAR, UFBL, SHARDUL, KDDL.
- H+1 outcome: PENDING until 25-Nov close.
- H+3 outcome: PENDING until 27-Nov close.
- H+5 outcome: PENDING until 01-Dec close.
- Do not label immature observations success/failure.

## 4. Today’s learning → research integration → next verification
1. Add per-step runtime budget and elapsed-time record; keep audit jobs below 10 minutes.
2. Add terminal readiness gate test: GEO unavailable or live quote 403/zero rows => qualified count 0.
3. Split high-touch, close-to-close, adverse excursion and executable return labels.
4. Recover the complete point-in-time 1,032-row candidate-decision export.
5. Correct the 200-session semantic spine using only a permitted archival route; no new NSE acquisition without applicable permission.
6. Validate all changes on untouched later cutoffs; no production selector/ranking/threshold changes without user approval.

**Production unchanged:** Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A–E and IPO-PLX V2.0. No user trade assumptions inferred. UNKNOWN is never PASS.


---

## Nightly addendum — ২৪-Nov-2026 (Run #421)

**Preflight:** Master Continuity Ledger C69, 24-Nov morning alert, 23-Nov nightly report, Run #421 artifact ও পূর্বের Lessons Register re-read; accepted ZIP-integrity কাজ পুনরাবৃত্তি হয়নি।

### Existing lesson updates — immutable IDs retained

- **PW-LSN-20261121-001 — exact forward-session label defect (VERIFIED, OPEN):** Run #421 head 7cf2292e467ffebf8c95ae67981570ab4d13a2ca; pipeline/walk_forward_backtest.py Git blob SHA-1 d085f7a2d35a88b4c4eaba65144a429a06961b09, known content SHA-256 dca7363ef1c5f56a097ed66b4305935f2c90975e2387b9c5b44780c4101f83e2. future_outcomes() still uses shift(-1).rolling(h,min_periods=1).max(). H+3/H+5 are trailing/partial windows; close outcomes use max close, not terminal T+h close. No new implementation without separate approval.
- **PW-LSN-20261121-002 — H+5 JSON/CSV parity (VERIFIED discrepancy, OPEN):** Run #421 metrics JSON implies 629 +20% H+5 Top-30 hits (0.2096667 × 3,000); prediction CSV has 632 rows >=20%; unexplained difference = 3. Canonical row-ledger reconciliation not accepted.
- **PW-LSN-20261123-001 — holiday/session duplicates (VERIFIED, OPEN):** Run #421 has 200 DATE labels but 13 exact duplicate official-holiday content pairs; only 187 unique daily content dates. Pairs: 02/03-Mar, 25/26-Mar, 30/31-Mar, 02/03-Apr, 13/14-Apr, 30-Apr/01-May, 27/28-May, 25/26-Jun, 11/14-Sep, 01/02-Oct, 19/20-Oct, 09/10-Nov, 23/24-Nov. Each pair is identical across all non-DATE columns for every symbol in that pair. QA JSON still says PASS because its gate counts raw files/session labels and does not check unique semantic dates or source DATE1 parity.
- **PW-LSN-20261124-001 — runtime budget (VERIFIED, OPEN):** Run #421 completed in 12m06s (15:10:17Z–15:22:23Z), still above the 10-minute maximum; five seconds faster than Run #420 but not accepted.
- **PW-LSN-20261124-002 — fail-closed source health (VERIFIED blocker, OPEN):** Run #421 final selection remains PROVISIONAL_ONLY_FINAL_SELECTION_BLOCKED; live 1m feed HTTP 403, rows=0, symbols=0; market_open_observed=false. GDELT returned 30 article titles but one read-timeout; this does not establish a synchronized GCR panel.
- **PW-LSN-20261124-003 — high-touch vs close-to-close distinction:** carried forward unchanged; no new matured symbol outcome on 24-Nov.

### New immutable lesson

**PW-LSN-20261124-004 — walk-forward evidence contract omits confidence intervals and unique-symbol denominator reconciliation**
- Date/run: 24-Nov-2026, Run #421 / 45422367928; artifact 14936656169.
- Expected: target/horizon-specific point estimates plus cutoff-cluster CI, fully matured/excluded counts, unique symbols, signal rows and reconciled eligible denominator.
- Actual: walk_forward_metrics.json contains point estimates but no CI fields; prediction and full-universe CSVs require separate row/symbol reconciliation; H+5 JSON/CSV differ by 3 rows.
- Root-cause confidence: VERIFIED for missing CI fields and observed count discrepancy; underlying H+5 serialization cause remains UNKNOWN.
- Evidence: metrics SHA-256 ee6624f046bd910491eac0e94d90006200abb23576990b8d5570bb3ebc36d440; predictions SHA-256 e80410b11cfaf8834af774c7e0e3ed39901efd5ce63b0ed2623dd5fef46a6951; universe probabilities SHA-256 356dc3329f28fb38e6cf6920f1564f3febf7b04f98dbe36dc4da887ca9bd96a9.
- Affected research step: V11.4 walk-forward metric serialization, target denominator and uncertainty reporting.
- Prevention test: one canonical row ledger must independently regenerate JSON/CSV/summary; exact integer parity; report unique symbol and signal-row counts separately; emit cutoff-cluster 95% CI only after label/session acceptance.
- Expected artifact: walk_forward_evidence_contract.json plus canonical row ledger.
- Sample/maturity: at least five fully matured cutoffs for a correctness pilot; performance inference only after all required cutoffs mature.
- Limitation/blocker: current forward labels and session spine are invalid; no metric is admitted. Acceptance OPEN / NOT_ACCEPTED.

### Run/artifact and report linkage
- Run #421 ID 45422367928; job 138545045702; artifact 14936656169; head commit 7cf2292e467ffebf8c95ae67981570ab4d13a2ca.
- ZIP SHA-256 d57374c50a8b8e2fe5710fd57660225ea59a2beffd639cb9e83b77e734499954; downloaded ZIP hash independently matched GitHub artifact digest.
- Dataset SHA-256 9f4f4305221a0b901a92088d22ffc5795614daeb2d6f78c013c78c6ec4f929f1; QA JSON SHA-256 48547e28ff82e978c8b63712c9fc5e4692268c3c99fba015bd1bfa3d7bd1af19.
- Dated nightly report: docs/NIGHTLY_ROTATION_BACKTEST_RESEARCH_REVIEW_20261124.md; commit 9f11c8184863eb56c6bf1e701e3cfd2189bbddeb; read-back SHA-256 8b8fc16ea166155484d0696b85001ec3c0543cc292e80038559426c6a9d40538; exact read-back matched.
- New lesson 004 is the only new lesson today; duplicate holiday/forward-label/runtime/source-health lessons were updated in place. Observation-only research note added; all acceptance tests OPEN / NOT_ACCEPTED.
- No new workflow dispatch, no new NSE acquisition, no paid source, no production/selector/ranking/threshold change. ₹0; UNKNOWN never PASS.
