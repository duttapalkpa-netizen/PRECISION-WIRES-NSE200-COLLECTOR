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
