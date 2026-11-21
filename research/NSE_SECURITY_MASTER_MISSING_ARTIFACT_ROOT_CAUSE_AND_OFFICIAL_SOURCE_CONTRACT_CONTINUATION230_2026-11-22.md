# Run #352 Security-Master Retention Root-Cause and Official Source Contract — Continuation 230

Date: 2026-11-22 (Asia/Kolkata)
Branch: audit/prospective-selector-tracking
Status: ROOT CAUSE CONFIRMED; SAFE ACQUISITION IMPLEMENTATION BLOCKED PENDING LIVE FILE-LINK/SCHEMA VALIDATION.

## 1. Continuity preflight
Re-read the Master Continuity Acceptance Ledger, GCR Master Priority Queue and Historical Task Registry through C228, plus C229's Run #352 artifact verification. Skipped the already-PASS 200/200 raw CSV and manifest hash reconciliation. Selected the remaining C229 gap: missing retained NSE security master.

## 2. Exact artifact evidence
Run #352: 44935745368; artifact 14719888911; ZIP SHA-256 623153a4516ba3ada34d406ce8bf217efb4abf6cbf3c01b905dd233944f82fec.
Independent ZIP readback confirms 702 entries and no path containing security_master, securitymaster, or a master CSV. This agrees with C229. The workflow upload allowlist already includes data/reference/security_master.csv; therefore the absence is not caused by the upload allowlist alone.

## 3. Code-level root cause
- collector/build_200_sessions.py defines MASTER=Path(data/reference/security_master.csv).
- Its load_master() returns an empty SYMBOL/ISIN/LISTING_DATE frame if that file is absent.
- The build then silently substitutes FIRST_OBSERVED_SESSION_PROXY for missing listing dates.
- The prospective workflow has no explicit security-master acquisition step before collector/build_200_sessions.py.
- collector/nse_download.py acquires historical Full Bhavcopy / UDiFF data and writes sessions, diagnostics and acquisition manifest, but has no security-master acquisition routine.
Thus the security master is neither downloaded nor built in this workflow run. The artifact allowlist is already correctly configured for its expected normalized path.

## 4. Official source contract (web verification)
- NSE Circular NSE/MSD/60315, dated 2024-01-19, states that CM MII security master files are disseminated daily on NSE's website with filename pattern NSE_CM_security_ddmmyyyy.csv.gz, display name CM - MII - Security File (.gz), via https://www.nseindia.com/all-reports, effective 2024-02-05.
- NSE's official All Reports page lists CM - MII - Security File (.gz) (NSE Listed securities) as a report.
- The public page representation retrieved for this audit exposes the report label but not the concrete attachment href or a stable raw download URL. The exact live file URL, CSV header schema and listing-date field therefore remain unverified in this audit context.

## 5. Safe engineering decision
No URL was guessed, no file was fabricated, and no synthetic security master was created. Do not derive a listing date from first observed trading session and label it official. The existing proxy behavior must remain explicitly a proxy until a valid official security-master row is available; missing official master must not be reported as present or PASS.

A safe implementation requires one bounded acquisition test to resolve the actual href from NSE's official All Reports page, download the .csv.gz, validate gzip/CSV integrity and observed schema, map official symbol/ISIN/listing-date fields without guessing, write the untouched raw gzip plus normalized data/reference/security_master.csv, and record URL/time/content-type/bytes/SHA-256. Then run a small parser/retention test before another full 200-session workflow.

## 6. Acceptance
- C229 raw 200-file retention proof: remains PASS for artifact 14719888911.
- Security-master source availability on official NSE page: FOUND (report listing).
- Exact attachment URL and actual file schema: UNKNOWN / NOT VERIFIED.
- Security-master acquisition in Run #352: NOT DONE.
- Security-master artifact retention: BLOCKED.
- Complete C228/C229 bundle: PARTIAL / NOT ACCEPTED.
- No workflow retry triggered; no production changes.

## 7. Protected invariants
Audit-only. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 and Engines A–E unchanged. No paid API, no synthetic data, no fabricated timestamps. ₹0. UNKNOWN never PASS.