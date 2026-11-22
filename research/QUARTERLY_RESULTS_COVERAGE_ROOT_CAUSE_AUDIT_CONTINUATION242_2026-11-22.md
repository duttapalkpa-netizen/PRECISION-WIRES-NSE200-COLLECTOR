# Quarterly Results Coverage Root-Cause Audit — Continuation 242

Date: 2026-11-22
Branch: audit/prospective-selector-tracking
Evidence: Run #128 (44991785839), artifact 14742096510, SHA-256 digest reported by GitHub:
589e65081695b0cc6e12e5494834ff9ad2c8211294effba7674e2ce4eef1f096

## Continuity check
- Reused the completed targeted quarterly workflow Run #128 and inspected its artifact.
- Did not repeat the already successful targeted test, endpoint/schema collection, metric extraction, feature rebuild, or unresolved timestamp/ISIN diagnostic steps.
- The newer Run #129 was still executing XBRL extraction at the last status check. Run #372 had completed XBRL extraction and feature validation but remained in walk-forward step 15. Run #377 had no job result available at the last check.

## Evidence-backed findings from Run #128
### Endpoint and source-validation boundary
- NSE integrated-filing endpoint response: HTTP 200, 500 result disclosure rows, 500 rows with XBRL URLs.
- Board/calendar response: 2,966 rows. These are not financial result metric rows.
- Source validation: 500/500 result disclosure rows valid for required source URL, publication timestamp, reporting period, symbol, and ISIN.
- Step 1 endpoint/schema status PASS only means response/envelope and normalized schema readiness; it is not financial metric coverage PASS.

### Metric extraction
- 500 disclosure rows entered the ledger.
- 68 source-linked verified financial metric rows across 45 symbols.
- 425 rows remained blocked; 7 rows were superseded revisions.
- The report includes 100 diagnostic error samples. In those samples, 99 were HTTP 403 responses from NSE archive XBRL/iXBRL attachment URLs and one was a facts/basis-incomplete iXBRL response. The 100 diagnostics are a sample/list in the report, not a proven complete census of all 425 blocked rows.
- No PDF OCR/headline-number extraction was used.
- The report's event study is blocked because the artifact did not contain data/processed/nse_eq_200_sessions.csv.

### Timestamp nuance
- Raw disclosure response has broadcast_Date for 463/500 rows; 37 have it missing.
- creation_Date is present for 500/500; revised_Date is present for 37/500.
- The raw feed therefore contains a candidate creation timestamp for rows missing broadcast_Date. Do not silently replace broadcast_Date with creation_Date unless the source contract and event-time semantics are explicitly validated. Existing source validation nevertheless reports all 500 normalized records valid.

## Decision / next action
The strongest evidenced bottleneck is attachment retrieval/access (HTTP 403), not the NSE endpoint envelope or normalized disclosure validation. No unsupported alternate endpoint, guessed mirror, or timestamp substitution is introduced. Preserve blocked rows as BLOCKED/UNKNOWN.

Next bounded investigation:
1. Compare NSE archive attachment request headers/session/cookies and official page-origin behavior using the existing collector, without bypassing access controls.
2. Determine whether the 403 is uniform or limited to specific attachments/host paths; retain URL/status/content-type/hash diagnostics.
3. If an officially documented alternative distribution path exists, validate it against the same symbol, ISIN, period, basis, timestamp, and source-hash contract before enabling it.
4. Validate the new CI cap separately: the 30-disclosure / 2-attachment profile intentionally truncates the run and must expose available/processed/truncated counts. It must not be used to claim full-population coverage.

## Status
| Area | Status |
|---|---|
| NSE endpoint/schema Step 1 | PASS |
| Normalized result disclosure validation | PASS (500/500) |
| Source-linked metrics | PARTIAL (68 verified) |
| Metric coverage | BLOCKED (425 blocked; 7 superseded) |
| Event study in this artifact | BLOCKED (missing historical price panel) |
| 403 attachment root cause | IDENTIFIED AS LEADING BLOCKER; remediation not yet verified |
| New bounded CI profile | Pending separate end-to-end verification |

## Protected invariants
Audit branch only. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A-E, and production workflow unchanged. ₹0 research spend. No paid APIs, fabricated timestamps, synthetic financial metrics, OCR guessing, or invented NSE source contracts. UNKNOWN/BLOCKED never becomes PASS.
