# NSE Security Master Source Verification Update — Continuation 231

Date: 2026-11-22 (Asia/Kolkata)
Branch: audit/prospective-selector-tracking

## Continuity and duplicate gate
Rechecked Master Continuity Ledger, GCR Master Priority Queue, Historical Task Registry through C228 and C229/C230 research notes. Skipped C229's already-PASS raw-file/manifest hash work. Continued only the missing Security Master source acquisition blocker.

## New official-source evidence
- NSE All Reports page currently exposes two distinct CM MII security-file report labels: (1) CM - MII - Security File (.gz) (NSE Listed securities); (2) CM - MII - Security File (.gz) (NSE Listed and BSE Exclusive securities).
- NSE circular NSE/MSD/60315 (2024-01-19) specifies the NSE-listed MII file naming pattern NSE_CM_security_ddmmyyyy.csv.gz, display name CM - MII - Security File (.gz), and website path https://www.nseindia.com/all-reports; effective 2024-02-05.
- Later NSE circular NSE/MSD/67344 also repeats the NSE-listed MII file and separately identifies a broader NSE & BSE securities file under the same naming convention but distinct website display link. The project must select the NSE-listed-only report unless the universe contract explicitly expands to BSE-exclusive instruments.
- NSE circular CMTR/71394 (2025) confirms the daily NSE website distribution remains available through All Reports.
- The opened All Reports page exposes report labels as form inputs, not a direct attachment hyperlink in the parsed page. No exact download href or concrete CSV header schema was retrieved. The filename pattern is an official naming contract, not proof of a raw URL template.

## Engineering decision
Do not hardcode a guessed URL or invent a CSV schema. The next implementation should resolve the selected report's actual attachment URL from the official All Reports page's runtime report metadata/API, for an explicitly selected trading date; download only if the resolved host/path is official NSE; validate gzip magic, decompression, CSV header and required symbol/ISIN fields; preserve raw gzip; normalize only fields confirmed by observed headers; record URL, UTC retrieval timestamp, content-type, bytes and SHA-256. Keep listing date UNKNOWN unless the file actually contains a validated listing-date field.

## Acceptance
- Official NSE-listed MII security-master report exists on All Reports: PASS.
- Official filename pattern and distribution path: PASS.
- Distinction from NSE-listed + BSE-exclusive variant: PASS.
- Actual file attachment URL: UNKNOWN / NOT RETRIEVED.
- Actual CSV schema and listing-date field: UNKNOWN / NOT RETRIEVED.
- Acquisition and artifact retention: BLOCKED; no code change or workflow rerun justified yet.
- C229 raw NSE file and manifest PASS remain unchanged.

## Protected invariants
Audit-only. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 and Engines A-E unchanged. ₹0, no paid APIs, no synthetic data, no fabricated timestamps. UNKNOWN never PASS.

## Sources
- https://nsearchives.nseindia.com/content/circulars/MSD60315.pdf
- https://nsearchives.nseindia.com/content/circulars/MSD67344.pdf
- https://nsearchives.nseindia.com/content/circulars/CMTR71394.pdf
- https://www.nseindia.com/all-reports