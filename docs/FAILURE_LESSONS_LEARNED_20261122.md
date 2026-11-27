# Failure & Lessons Learned Research Log — 2026-11-22
## PRECISION-WIRES V11.3 | Observation-only

**Status:** No new market session or newly matured outcome on 2026-11-22 (Sunday). No new stock-selection failure can be classified today. Existing lessons are carried forward without duplicate IDs.

## 1. Cohort state
- Latest shadow cutoff: 2026-11-20.
- Shadow cohort: 8 unique symbols / 10 selector rows: NRL, V2RETAIL, SIGACHI, RSDFIN, KDDL, YATRA, KMCSHIL, HINDOILEXP.
- Next regular NSE session: 2026-11-23; 24-Nov-2026 is a capital-market holiday per NSE/CMTR/71775.
- Current cohort H+1/H+3/H+5 outcomes: PENDING / IMMATURE.
- False positives and target-wise missed winners for this cohort: UNKNOWN.
- No full-universe missed-winner attribution is admissible until per-cutoff eligible universe and row-level predictions reconcile.

## 2. Existing immutable lessons — no duplicate IDs

### PW-LSN-20261121-001 — exact forward-session label defect
- Root cause: VERIFIED. Existing source used shift(-1) + trailing rolling with partial windows, not exact T+1…T+h exchange-session windows.
- Why selection failed: target labels and ranking/training path are contaminated; current historical metrics cannot be treated as valid selector performance.
- Research question: does an exact exchange-session spine + full-horizon maturity state machine remove partial-window and missing-session compression?
- Bounded test: only after separate user approval, five fully matured cutoff correctness pilot; hand-check labels against archived exchange-session rows; no production admission.
- Current status: BLOCKED pending explicit approval; no code change today.

### PW-LSN-20261121-002 — H+5 count serialization mismatch
- Root cause: SUPPORTED mismatch; exact cause UNKNOWN. JSON indicates 613 while row-level CSV has 616.
- Why selection/research failed: different metric outputs are not integer-consistent, so no metric can pass denominator/count parity.
- Research question: can one canonical row ledger generate all JSON/CSV/summary/manifest counts exactly?
- Bounded test: derive target counts once from canonical unique symbol/cutoff rows; compare all outputs; independent recomputation.
- Current status: OPEN / NOT_ACCEPTED; no rerun or production change.

### PW-LSN-20261121-003 — raw NSE artifact allowlist omission
- Root cause: VERIFIED in Continuation 228: artifact upload allowlist omitted raw bhavcopy CSVs, sessions, acquisition diagnostics and security master.
- Corrective change: isolated audit branch commit `46f4a359f21da676cb0c92e874fb08f14ee20d90`; future artifact retention proof remains PENDING; per-file acquisition-time manifest NOT_DONE.
- Why candidate selection failed: latest quote/volume/circuit/security evidence cannot be independently replayed from retained raw bytes; stale or missing inputs must fail closed.
- Research question: does a future bounded artifact retain every acquired raw file plus source URL, publication/retrieval timestamp semantics, HTTP status, content type, byte count and SHA-256?
- Bounded test: inspect the next already-authorized artifact after it exists; compare expected session inventory with retained raw files and manifest; do not redownload historical bytes.
- Current status: root cause confirmed; correction committed on isolated branch; acceptance OPEN / NOT_ACCEPTED.

## 3. Daily research integration
1. Keep V11.4 metrics BLOCKED until label correctness, full maturity, identity and count parity pass.
2. Keep V11.3 cost-aware replay UNKNOWN until user-approved assumptions and an independently reconciled trade ledger exist.
3. Keep GCR UNKNOWN until publication-time/vintage-aligned macro → sector → stock → matured outcome join is proven.
4. Keep current eight-symbol cohort PENDING until 23-Nov H+1 session and later exact H+3/H+5 session maturity.
5. No new target-hit rates, best-three stock names, or full-universe missed winners are invented.

## 4. Today’s learning → research addition → next verification
- Learning: successful acquisition in a runner and a QA PASS do not prove retained raw-source bytes or independent source replay.
- Research addition: raw bytes + per-file acquisition-time manifest + point-in-time security identity + official price timestamp remain hard gates for daily candidate eligibility. Link to PW-LSN-20261121-003; do not create a duplicate lesson.
- Next verification: future artifact retention proof; acquisition-time manifest completeness; security-master provenance; then current price/volume/circuit gates.
- No production selector, rank, threshold, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A–E or IPO-PLX V2 changes.


## 2026-11-22 — Run #398 raw-retention evidence update
- Existing lesson updated: PW-LSN-20261121-003 (no duplicate ID).
- Run #398 / run ID 45027842316, job 137232482609, artifact 14757294944, source head 7360870b768a6ed746451afa96ea918a3bffae07.
- Artifact ZIP SHA-256 212a84103f2a9f47681865c7e165fe0247001b02d9563a5cef578636fb0b1898 independently matches GitHub digest. Inventory: 200 raw NSE bhavcopy CSVs, 200 acquisition-manifest entries; independent per-file retained-byte and SHA-256 checks: 200/200 PASS. QA: 200 sessions, 2,999 symbols, 100% delivery quantity/percentage coverage.
- Field-level limitation: source URL, retrieval timestamp, source byte count, source SHA-256 and content type are present for 200/200; per-file HTTP status 0/200 and publication timestamp 0/200. Therefore future raw-byte retention is PASS for Run #398, but complete per-file provenance remains PARTIAL. Original Run #339 raw bytes remain BLOCKED/unrecoverable from inspected artifacts.
- Evidence file hashes: acquisition manifest SHA-256 0c501b483c9bcb7de0e079bf15171bb59ad91edee966d036475423c8c9a4d5be; manifest-validation JSON 38704f930ad171bf71fe68b73f2c7fa2fe29c2250595490626938064cd87641a; QA JSON 48547e28ff82e978c8b63712c9fc5e4692268c3c99fba015bd1bfa3d7bd1af19.

### PW-LSN-20261122-001 — Macro-Geo archive report schema mismatch
- Date/cutoff: 2026-11-22; Run 45038111510, latest attempt job 137256604023; failed log timestamp 2026-11-22T15:27:37Z.
- Expected: nse_index_history() returns archive metrics accepted by its caller. Actual: producer returns observed_session_requests, rows, failures; main() indexes missing weekday_requests at line 530 and raises KeyError. Root-cause confidence: **VERIFIED** by source inspection and job log.
- Run outcome: Steps 1–8 SUCCESS; P0 collection Step 9 FAILED; repair, source coverage, event study and hard gate SKIPPED. Artifact 14759889454 SHA-256 618fde324b34fef465a1a9190b07825594c39e2d9ab2dc9f84917c9668cac6cb independently verified; all P0 external inputs and downstream reports are MISSING.
- Dataset SHA-256: d6810409dbd800e5146e08a1eb1e8b48207354461876acb62cbb2f656fba51db. Collector code blob SHA-1 99b0fdd1a8155fe9471a2cc6e349d927e046caed; collector code SHA-256 255da8657e7cb838a52b2ba328458befb3d51f7000221acc912bef2c4335041a. Workflow YAML blob SHA-1 2859d1884a7c9c58d538ac1a2f00ef9c20c84731; workflow SHA-256 064b85f9a8d2befb71bf02d495586a6136b236c24ff84437072cc7084e789904. The SERIES registry is inline in the collector; no separate config file was used.
- Affected diagnostic: Macro-Geo P0 index archive fallback / producer-consumer schema contract. Expected vs actual: archive metadata should serialize observed-session request count; actual missing key aborts collection. Sample: 200-session input archive; progress log reached 180/200 before exception; no macro source rows accepted.
- Recurrence-prevention test: bounded, network-free fixture over 3 observed sessions; assert producer return keys and caller access keys match; expected artifact archive_report_contract_validation.json plus test log; runtime target <60 sec. No code patch or workflow rerun authorized in this review.
- Limitation/blocker: macro source collection and hard gate never ran; no GCR metric may be inferred. Lesson status OPEN / NOT_ACCEPTED pending test and separately authorized recovery.


### PW-LSN-20261122-002 — Archive report consumer key mismatch repaired (2026-11-22)
- Root cause: nse_index_history() returns observed_session_requests, while main() consumed weekday_requests; Run #45038111510 failed with KeyError after 180/200 observed sessions.
- Bounded fix: consumer now reads observed_session_requests. Collector commit afa063959b39846c6722370afa655cb77335d4df; blob 78fe030e5964b8728963a4a0e0604f3cbe184c3f.
- Regression test added: qa/test_macro_geo_archive_report_contract.py, AST-based producer/consumer contract; commit 491cf1ff7b94ce40129f00c9e8baea499d6087c8; blob 56d62af1f318414b7db0eb51d25a122e8a4ae03a.
- Recovery workflow runs this test before P0 collection; workflow commit 1c9ecb82c29433f91b14e7bc9173652aa6ead67f; blob 546234eb9415a916038120d810946089b13c9012.
- Status: CODE PATCH COMMITTED; REGRESSION EXECUTION PENDING; end-to-end Macro-Geo remains BLOCKED until the new run proves collection and downstream evidence. Do not mark PASS based on commits.
- No selector, threshold, ranking, production code or admission changes. UNKNOWN remains not PASS.


### PW-LSN-20261122-002 — 27-Nov-2026 regression execution follow-up
- Existing collector fix (afa063959b39846c6722370afa655cb77335d4df) and AST test (491cf1ff7b94ce40129f00c9e8baea499d6087c8) were re-read and reused; no duplicate patch.
- Added dedicated network-free workflow .github/workflows/macro_geo_archive_contract_regression.yml, isolated branch commit 12cce4a15fdf9defa099fc17fa1675e2972505ee, job timeout 5 minutes. It runs only the AST contract test and writes archive_report_contract_validation.json with source/test SHA-256.
- GitHub combined status returned an empty list at review time; workflow run and artifact are NOT_VERIFIED. Status remains REGRESSION PENDING / NOT_ACCEPTED; do not infer PASS from workflow creation.
- Next: retrieve the workflow run, inspect test log and JSON artifact; record run/job/artifact IDs and ZIP SHA-256. Only then consider a separate audit-only Macro-Geo recovery. No broad run, NSE raw acquisition, selector, production or hard-gate change.
