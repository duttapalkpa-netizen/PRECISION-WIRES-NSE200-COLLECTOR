# Historical PASS Evidence Reconciliation — PRECISION-WIRES V11.3

**Date:** 2026-11-02  
**Repository:** `duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR`  
**Working branch:** `fix/factor-registry-same-snapshot-reconcile`  
**Purpose:** Recover historical PASS evidence, preserve accepted work, distinguish historical scope from refreshed-snapshot status, and prevent duplicate execution.

## Executive decision

The project is not restarting. Steps 1 and 2 are PASS/CLOSED on the current Quarterly Results acceptance runs. Step 3 has a historical PASS WITH COVERAGE LIMITATION from the full paired-ablation artifact; the later zero-item RSS transport smoke does not invalidate it. Step 4 has PASS WITH SOURCE QUALIFICATIONS for all eight P0 groups on a separate audit-branch artifact. Step 5 is PASS for the tested missing-file and stale/misalignment rejection scope; absolute wall-clock staleness is not covered. Step 6 remains BLOCKED.

Do not rerun Steps 1–4 absent a changed source snapshot, an evidenced freshness failure, or a specific provenance defect. Preserve PR #13 as Draft and do not merge.

## Reconciliation ledger

| Step | Evidence | Observed result | Decision |
|---:|---|---|---|
| 1 — NSE Quarterly Results endpoint/schema | Run `41330698503`; artifact `13093865217`; 1,767 records; four pages 500+500+500+267; unique rows 1,767; pagination complete. | Endpoint HTTP 200 and page contract validated. | **PASS — CLOSED** |
| 2 — financial-results metadata | Run `41334950000`; artifact `13094767719`; ZIP SHA-256 `90bf3546cd044782fba522940e5fe4180b9e39f072bf1f6c94e7f79dad9232e3`. Five fields each 1,767/1,767; missing 0; ambiguous 0; duplicate hashes 0; six acceptance tests true. | Metadata validation complete for SYMBOL, ISIN, SOURCE_URL, PUBLICATION_TIMESTAMP and REPORTING_PERIOD. | **PASS — CLOSED for metadata only**; XBRL metric extraction remains separate. |
| 3 — News/Catalyst join | Historical Run `39977796193`; artifact `12513903105`; ZIP SHA-256 `5dbf03176d7d655a533c04f97f27c56209948b3b8318515a6b4af98bce6e3b59`. | 10 cutoff-symbol pairs; 10 coverage rows; unknown 0; verified news 1; unverified 0; no-match GDELT query windows 9; timestamp-window failures 0; invalid article/query URLs 0; duplicate pairs 0. Verification report PASS (1 checked row). Status `READY_FOR_PAIRED_ABLATION`. | **PASS WITH COVERAGE LIMITATION** for that historical snapshot. Nine no-match queries do not prove no material news exists. |
| 3 — later transport smoke | Run `41335754845`; artifact `13095585092`; Google News RSS HTTP 200 for test symbol TESTCO, 0 items; full Step 3 acceptance `NOT_EVALUATED`. | This was not a replay of the historical 10-pair candidate universe and did not run the full join. | **Does not invalidate historical Step 3 PASS.** A refreshed snapshot needs its own frozen candidate universe and full acceptance run. |
| 4 — Macro-Geo P0 | Run `41283471559` on `audit/run145-factor-registry-gap-audit` (PR #11 branch); artifact `13074955372`; ZIP SHA-256 `82352f62a22647ff6d6c4c2a448b73285e092808893f34768b8362e3e1f1dde4`. | P0 coverage 8/8 `P0_COMPLETE`; crude_oil 211 rows (`AVAILABLE_SECONDARY`, US EIA official XLS); usd_inr 203 rows (`AVAILABLE_SECONDARY`, community mirror, not direct RBI); corporate_events 1,689 rows (NSE official); fpi_dii_flows 208 rows (NSDL official; FPI 105 dates/151 days, DII 103 dates/150 days). Benchmark 10, sector 90, volatility 228, geopolitical 15; four-group validator PASS. | **PASS WITH SOURCE QUALIFICATIONS** for P0 coverage on this artifact snapshot. Do not recollect without a specific reason. |
| 5 — hard-gate rejection | Initial real-data Run `41283471559` was BLOCKED as expected. Follow-up isolated regression Run `41340059447` SUCCESS; artifact `13097241013`; ZIP SHA-256 `24f553d2983f5369904f6b545986d5b5d7b35955bae634341efd6c8043531099`. Inspected log: 3 tests PASS — aligned complete fixture passes; missing required coverage input blocks and preserves UNKNOWN/BLOCKED; market/equity date gap >3 days blocks. | All three tests assert production selector, `RANKING_SCORE` and `+1 PRESSURE_FADE` unchanged. | **PASS — defined negative-test scope**; absolute wall-clock staleness when both panels are equally old remains untested. |
| 6 — final consistency audit | Same P0 artifact manifest reports `final_manifest_reconciliation.status=RECONCILED`, but `source_snapshot_id` and `snapshot_id` are null; hard gate remains BLOCKED. | Cross-report reconciliation exists, but it is not final release acceptance. | **BLOCKED** |

## Step 4 interpretation: what PASS does and does not mean

The P0 repair report shows all four formerly missing repair targets present. The two secondary sources remain explicitly labelled and were accepted only under a domain-QA contract: source identity, positive values, unique date keys, requested-window bounds, freshness <=3 calendar days, and source URL provenance. They must not be relabelled as direct FRED/RBI feeds. Geopolitical rows are publisher/RSS/GDELT mentions; occurrence is not independently verified.

The same artifact's overall strict hard gate remains BLOCKED because 35 Factor Registry groups had 0 fully available schema groups, 13 disconnected and 22 partial; historical regime anchor coverage was incomplete (11 anchors, 9 regimes with windows, 2 without windows). Event study was exploratory with pending events (43 event rows, 29 eligible, 14 pending; 81 window rows); historical regime study was exploratory, not causal.

## Branch/snapshot boundaries

- Step 1 and Step 2 current acceptance evidence is on `fix/factor-registry-same-snapshot-reconcile`.
- Historical Step 3 evidence is from Run `39977796193`; it is preserved with its explicit coverage limitation.
- Step 4 evidence Run `41283471559` belongs to `audit/run145-factor-registry-gap-audit`, associated with PR #11, not PR #13.
- PR #13 remains Draft and unmerged.
- Step 4 manifest says `RECONCILED`, but both immutable snapshot identifiers are null. Do not treat this artifact as a PR #13 immutable snapshot.

## No-duplicate-work decision

1. Do not rerun Step 1 endpoint/schema acceptance.
2. Do not rerun Step 2 five-field metadata acceptance unless the source snapshot changes.
3. Do not rerun the historical 10-pair Step 3 audit. For a new snapshot, first restore/build the frozen cutoff-symbol universe, then run full join acceptance.
4. Do not recollect Step 4 P0 groups without a new snapshot, freshness failure, or source-provenance correction.
5. Step 5 missing-input and stale/misalignment rejection tests now PASS in Run `41340059447`; artifact `13097241013` inspected. Preserve this evidence. Absolute wall-clock staleness remains a narrower follow-up, not a reason to rerun the completed negative tests.
6. Then perform Step 6 against one immutable snapshot ID.

## Frozen invariants

- Production selector unchanged.
- `RANKING_SCORE` unchanged.
- Frozen `+1 PRESSURE_FADE` unchanged.
- 672 diagnostics unchanged.
- `UNKNOWN` is neither PASS nor FAIL.
- No synthetic rows, fabricated timestamps, unsupported source promotion, or gate relaxation.
- Hard Gate remains BLOCKED until all required Factor Registry, historical-regime, provenance and matured event-study conditions pass.
- Research spend remains ₹0; no paid APIs, licences, subscriptions or external contact without explicit approval.

## Step 5 regression completion — 2026-11-02

- Workflow [Run `41340059447`](https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/41340059447) completed SUCCESS on the active PR #13 branch.
- Artifact `13097241013` inspected; ZIP SHA-256 `24f553d2983f5369904f6b545986d5b5d7b35955bae634341efd6c8043531099`.
- Three deterministic tests passed in 0.017 seconds: missing required input rejects; >3-day market/equity date misalignment rejects; aligned complete fixture passes.
- `UNKNOWN/BLOCKED` semantics and all frozen production invariants were asserted unchanged.
- Limitation: this test covers panel/equity date misalignment, not absolute wall-clock staleness where both datasets are equally old.
