# NSE Security Master Runtime Metadata Route Discovery — Continuation 232

Date: 2026-11-22 (Asia/Kolkata)
Branch: audit/prospective-selector-tracking
Status: OFFICIAL REPORT PRESENCE CONFIRMED; RUNTIME API CANDIDATE IDENTIFIED BUT NOT OFFICIALLY VERIFIED; DOWNLOAD URL / CSV SCHEMA STILL UNKNOWN

## 1. Continuity and duplicate gate
- Reused the latest audit-branch Continuation 231 source-contract report and the default-branch continuity state through C228. Did not repeat C229 raw-file/manifest hash reconciliation or C230/C231 report-label/circular checks.
- Re-read the current audit-branch workflow and collector/builder implementation.
- The workflow artifact allowlist already includes `data/reference/security_master.csv`; therefore another allowlist edit is not justified.
- `collector/nse_download.py` currently acquires bhavcopy data and writes acquisition provenance but has no Security Master acquisition routine.
- `collector/build_200_sessions.py` expects `data/reference/security_master.csv`; if absent, `load_master()` returns an empty SYMBOL/ISIN/LISTING_DATE frame. This confirms the missing acquisition step remains the direct blocker.

## 2. New official NSE page evidence
- NSE All Reports page search result (retrieved 2026-11-22) visibly lists the daily report `CM - MII - Security File (.gz) (NSE Listed securities)` with a dated filename such as `NSE_CM_security_30102026.csv.gz`; it separately lists the broader NSE Listed and BSE Exclusive variant.
- Official NSE circular NSE/MSD/60315 specifies the naming pattern `NSE_CM_security_ddmmyyyy.csv.gz`, website distribution path `https://www.nseindia.com/all-reports`, and effective date 2024-02-05.
- Official NSE circular NSE/MSD/67344 explicitly distinguishes the NSE-listed-only and NSE+BSE-exclusive variants. The project should continue to select NSE-listed-only.
- The live All Reports page provides report presence and visible dated filename evidence, but the page representation available in this audit does not expose the attachment href or underlying report metadata response.

## 3. Runtime endpoint lead — NOT YET ACCEPTED
- A public third-party technical note describes `GET https://www.nseindia.com/api/daily-reports?key=CM` and response fields `fileKey`, `filePath`, `fileActlName`, with the suggested download URL formed from `filePath + fileActlName`.
- This is third-party reverse-engineering evidence, not an official NSE API contract. A direct read attempt of that endpoint through the available research retrieval surface returned inaccessible; no JSON response, report identifier, exact attachment URL, HTTP status, or file bytes were obtained.
- Consequently this endpoint is recorded only as a candidate for a future controlled verification, not as a verified production source. Do not hardcode it or infer a response schema into the collector yet.

## 4. Acceptance matrix
| Item | Status | Evidence |
|---|---|---|
| Daily NSE-listed MII Security File exists | PASS | Official NSE All Reports page and circulars |
| NSE-listed-only variant distinguished from NSE+BSE-exclusive | PASS | Official NSE circular NSE/MSD/67344 |
| Official filename pattern known | PASS | NSE/MSD/60315 |
| Runtime metadata endpoint | UNKNOWN | Third-party lead only; direct retrieval inaccessible |
| Exact attachment URL / official host response | UNKNOWN |
| Actual gzip bytes / magic / decompression | NOT_CAPTURED |
| Actual CSV header and symbol/ISIN schema | UNKNOWN |
| Listing-date field presence and semantics | UNKNOWN |
| Collector acquisition implementation | NOT_DONE |
| Future workflow artifact retention proof | PENDING |

## 5. Decision and next bounded action
Do not change collector code or launch the long prospective workflow from this evidence alone. Next action is a narrowly scoped official-source verification of the runtime metadata response in an environment capable of reaching NSE's public All Reports API. Accept only a response retrieved from an NSE-controlled host, matching the NSE-listed-only report label and explicitly selected trading date. Then validate the resolved attachment host, filename, gzip magic, decompressed CSV header, and actual symbol/ISIN fields before implementing acquisition. Preserve raw gzip and record observed source URL, UTC retrieval time, content-type, byte count and SHA-256. Keep listing date UNKNOWN unless an actual validated field is present.

## 6. Protected invariants
Audit-only. No production workflow, selector, ranking, +1 PRESSURE_FADE, CORE-672 or Engines A-E changes. ₹0; no paid APIs, guessed URLs, synthetic data, fabricated timestamps, or inferred listing dates. UNKNOWN never PASS.
