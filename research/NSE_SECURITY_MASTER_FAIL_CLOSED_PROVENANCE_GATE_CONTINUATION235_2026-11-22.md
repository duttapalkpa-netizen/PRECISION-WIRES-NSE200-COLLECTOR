# NSE Security Master Fail-Closed Provenance Gate — Continuation 235

Date: 2026-11-22 (Asia/Kolkata)
Branch: audit/prospective-selector-tracking
Status: CODE + OFFLINE TESTS COMMITTED; LIVE NSE ACQUISITION / CI EXECUTION NOT YET VERIFIED

## 1. Continuity preflight
- Re-fetched Master Continuity Acceptance Ledger SHA `e02d8dea8963e83be182250ca621deaf10108c69`, GCR Priority Queue SHA `3d7f1d0df3b0c94d0f1abd0f4eb0d41bb630f670`, and Historical Task Registry SHA `bb44c49904893f766dddefbd9548334b39922fd7`; all default-branch tails remain C228.
- Re-read C234 report, prospective workflow, existing collector and builder. Excluded all previously PASS report-label, raw retention and source-contract work.
- Selected C234's next bounded task: fail-closed legacy master provenance validation in the audit workflow. No attempt to invent the daily MII URL or schema.

## 2. Changes committed on isolated audit branch
1. Updated `collector/security_master.py`:
   - requires non-empty CSV response and a SYMBOL header;
   - now requires an ISIN NUMBER/ISIN header and at least one row with both SYMBOL and ISIN;
   - atomically writes normalized `security_master.csv`;
   - writes `security_master_manifest.json` with observed source URL, UTC retrieval timestamp, HTTP status, content type, raw source bytes and SHA-256, normalized SHA-256, row count and explicit `source_family=LEGACY_EQUITY_L_CSV` / `daily_mii_equivalence=NOT_ESTABLISHED` boundary.
   - acquisition failure exits non-zero and does not claim PASS.
2. Added `qa/validate_security_master.py`:
   - fails if master/manifest is absent;
   - permits only the two explicitly configured official NSE hosts;
   - requires timezone-aware retrieval time no older than seven days and rejects materially future-dated timestamps;
   - verifies normalized file SHA-256, required columns, non-empty SYMBOL/ISIN, unique symbols, row-count parity and source provenance fields.
3. Added six offline unit tests in `qa/test_security_master_validation.py`: valid pass with explicit non-equivalence, missing manifest, unapproved host, stale manifest, hash mismatch, and missing ISIN.
4. Updated `.github/workflows/prospective_watchlist_tracking.yml` to run the legacy collector followed by fail-closed validation before dataset build; added the manifest to artifact retention.

## 3. Commit trail
- Collector provenance capture: `50f042c8c4308038a26094c27c8bec3bea6b8093`
- Validator: `990df66fbb2a8541f50f63b6df33c87cba75b338`
- Offline tests: `63bd88901a394d64d67f294f2177ae1d42499e95`
- Workflow gate: `7fb70319874bd232e93b6ce1c41560302e0bc982`
- Test fixture newline correction: `560d0528ca150ca1f0dc1b7c7caf47f6507b9dc6`

## 4. Acceptance status
| Item | Status |
|---|---|
| Collector fails closed for missing SYMBOL/ISIN or empty data | CODED |
| Raw + normalized provenance manifest | CODED |
| Official NSE host allowlist + freshness + hash + row-count validation | CODED |
| Six offline regression tests | ADDED; execution not independently observed in this task |
| Prospective workflow invokes collector and validator before build | CODED |
| Manifest retained in prospective artifact | CODED |
| CI test result | PENDING |
| Live NSE source reachable / current acquisition successful | NOT VERIFIED |
| Daily MII equivalence | UNKNOWN / NOT ESTABLISHED |
| Daily MII downloader and actual schema | BLOCKED pending official attachment evidence |

The existing test step `python -m unittest discover -s qa -p "test_*.py" -v` will discover the new tests. No successful CI result is claimed until a run is observed.

## 5. Explicit boundaries and risks
- This is a guarded legacy `EQUITY_L.csv` collector, not a newly implemented daily MII downloader. The manifest records that distinction so a future reader cannot silently interpret this source as MII.
- Listing date remains blank if the source does not expose one of the already-supported listing-date headers. No first-observed-session proxy is relabeled as an official date.
- A seven-day provenance freshness limit is a technical guardrail, not proof that NSE updates this legacy file daily.
- No full prospective workflow was deliberately dispatched as a test; that workflow performs 200-session acquisition and multiple research stages. CI status therefore remains pending.

## 6. Protected invariants
Audit-only branch. No production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A-E, or production workflow changes. ₹0; no paid APIs, synthetic data, guessed MII URLs, or fabricated timestamps. UNKNOWN never PASS.
