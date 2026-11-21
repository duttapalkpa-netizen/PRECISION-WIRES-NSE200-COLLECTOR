# NSE Security Master Existing Collector Reconciliation — Continuation 234

Date: 2026-11-22 (Asia/Kolkata)
Branch: audit/prospective-selector-tracking
Status: EXISTING LEGACY EQUITY MASTER COLLECTOR FOUND; DAILY MII SOURCE ALIGNMENT NOT VERIFIED; PROSPECTIVE WORKFLOW DOES NOT INVOKE IT

## 1. Continuity preflight and duplicate gate
- Re-fetched default-branch Master Continuity Acceptance Ledger (SHA `e02d8dea8963e83be182250ca621deaf10108c69`), GCR Priority Queue (`3d7f1d0df3b0c94d0f1abd0f4eb0d41bb630f670`) and Historical Task Registry (`bb44c49904893f766dddefbd9548334b39922fd7`); all three tails remain C228.
- Re-opened audit-branch C233 API-access-boundary report (SHA `e1dfdfd02ec703efe97e18d615ebc1682bf11d58`), `collector/security_master.py`, `collector/build_200_sessions.py`, `.github/workflows/nse_collector.yml`, `.github/workflows/prospective_watchlist_tracking.yml`, and README.
- This source-code read-back corrects an overbroad statement in C232/C233: `collector/security_master.py` DOES exist. It tries two static legacy `EQUITY_L.csv` URLs, parses a CSV with SYMBOL, optionally ISIN NUMBER/ISIN and LISTING DATE/LISTING_DATE, and writes `data/reference/security_master.csv`.
- The default `nse_collector.yml` invokes that script with `continue-on-error: true`, then runs the builder. Therefore a failed master acquisition is intentionally non-fatal in that workflow.
- The prospective audit workflow `prospective_watchlist_tracking.yml` does not invoke `collector/security_master.py` before `collector/build_200_sessions.py`; it only includes the normalized master path in its artifact allowlist. Thus the daily MII master integration gap in the prospective workflow remains real, but it is not accurate to say the repository has no security-master acquisition script at all.

## 2. Official-source comparison
- Current official NSE All Reports page displays the daily report `CM - MII - Security File (.gz) (NSE Listed securities)` with a dated `NSE_CM_security_ddmmyyyy.csv.gz` filename; a separate NSE-listed plus BSE-exclusive variant is also displayed. (Official page result retrieved 2026-11-22.)
- NSE circular NSE/MSD/60315 documents the daily MII file nomenclature and All Reports distribution path; circular NSE/MSD/67344 distinguishes the two variants.
- The existing script's two `EQUITY_L.csv` URLs are not the daily MII filename/source documented by those circulars. No evidence in the inspected repository or official source materials establishes that the legacy EQUITY_L file is equivalent in field coverage, listing-date semantics, or update cadence to the daily MII security file.
- The official page's search-indexed rendering provides the report label and dated filename but not the underlying attachment href or raw payload. Exact URL, gzip content, and CSV schema remain unverified.

## 3. Actual implementation risks
1. The prospective audit workflow can build without first acquiring a current security master.
2. In the default collector workflow, Security Master failure is suppressed by `continue-on-error: true`.
3. The builder explicitly substitutes `FIRST_OBSERVED_SESSION_PROXY` when official listing date is missing. This is labelled in output, but must not be interpreted as an official listing date.
4. The legacy `EQUITY_L.csv` collector does not record a provenance manifest (source URL, UTC retrieval timestamp, content-type, bytes, SHA-256) in the inspected code.
5. The static legacy CSV parser only requires SYMBOL; it does not fail closed when ISIN or listing date columns are absent.

## 4. Acceptance matrix
| Item | Status |
|---|---|
| Existing security_master.py collector exists | PASS |
| Existing script writes normalized SYMBOL/ISIN/LISTING_DATE columns | PASS (code path; not a live source payload validation) |
| Default collector invokes legacy script | PASS |
| Default collector suppresses script failure | PASS |
| Prospective audit workflow invokes security_master.py | FAIL / NOT WIRED |
| Existing EQUITY_L.csv proven equivalent to daily MII file | UNKNOWN |
| Official daily MII attachment URL and payload schema | UNKNOWN |
| Raw MII acquisition + provenance manifest | NOT DONE |
| Listing-date field verified against official daily MII schema | UNKNOWN |

## 5. Next bounded task selected
Do not repeat API route probing without a working NSE retrieval path. The next highest-value code task is to add a fail-closed, offline-tested acquisition contract for the prospective workflow: it must not treat an absent or stale master as PASS; it must report master status and distinguish official listing date from first-observed-session proxy. Keep the daily MII downloader itself blocked until the exact official attachment URL and actual CSV schema are captured. Do not change the production workflow or production selector.

## 6. Protected invariants
Audit-only. No production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 or Engines A-E changes. ₹0; no paid API, fabricated timestamps, guessed URLs, synthetic data or false listing dates. UNKNOWN never PASS.
