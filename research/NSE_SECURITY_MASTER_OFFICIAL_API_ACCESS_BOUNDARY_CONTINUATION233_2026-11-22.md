# NSE Security Master Official API Access Boundary — Continuation 233

Date: 2026-11-22 (Asia/Kolkata)
Branch: audit/prospective-selector-tracking
Status: OFFICIAL REPORT LISTING RECONFIRMED; CANDIDATE API UNREACHABLE IN AVAILABLE RETRIEVAL CHANNEL; IMPLEMENTATION BLOCKED

## 1. Mandatory continuity and duplicate gate
- Re-fetched the default-branch Master Continuity Acceptance Ledger (blob SHA `e02d8dea8963e83be182250ca621deaf10108c69`), GCR Priority Queue (`3d7f1d0df3b0c94d0f1abd0f4eb0d41bb630f670`) and Historical Task Registry (`bb44c49904893f766dddefbd9548334b39922fd7`). The default-branch ledgers still end at C228.
- Re-fetched audit-branch C232 report (blob SHA `b6f25dc6318f46a71b5c1aea39730f738c2acae3`), plus the workflow, `collector/nse_download.py`, and `collector/build_200_sessions.py`.
- Excluded already-PASS raw-file/manifest retention checks and prior official report-label / circular checks. No workflow allowlist edit was repeated: the allowlist already includes `data/reference/security_master.csv`.
- Code read-back reconfirms the actual gap: no Security Master acquisition routine exists in `collector/nse_download.py`; builder expects the file and returns an empty master frame when absent.

## 2. New route-level verification
- Opened the official NSE All Reports page through the current public web surface. It resolves/redirects from `nseindia.com` to `nseindia.in` and displays the daily report `CM - MII - Security File (.gz) (NSE Listed securities)`, with a dated filename such as `NSE_CM_security_30102026.csv.gz`. It separately displays the NSE Listed and BSE Exclusive variant.
- The rendered page exposes report names and dated filenames but not the attachment href or a visible runtime JSON payload in the retrieved representation.
- Attempted the candidate `https://www.nseindia.com/api/daily-reports?key=CM` directly; the retrieval surface returned “URL is not accessible”. Repeated against `https://www.nseindia.in/api/daily-reports?key=CM`; it was also inaccessible.
- A direct HTTP session attempt from the available execution environment could not resolve `www.nseindia.com` (DNS resolution failure). Therefore no HTTP status, response body, headers, cookies, attachment URL, or file bytes were obtained.
- Search did not surface an NSE-published API contract for this route. The route remains an unverified third-party lead only.

## 3. Acceptance matrix
| Item | Status | Evidence |
|---|---|---|
| NSE-listed-only MII report is listed on official All Reports page | PASS | Current official page |
| NSE-listed-only distinguished from NSE+BSE-exclusive variant | PASS | Current official page + NSE circular evidence in C231/C232 |
| Official filename pattern | PASS | NSE/MSD/60315, recorded in C231/C232 |
| Candidate daily-reports endpoint officially documented | UNKNOWN | No NSE API contract located |
| Candidate endpoint response retrieved | BLOCKED | Retrieval surface inaccessible; execution DNS failure |
| Exact attachment URL and source headers | UNKNOWN |
| Gzip bytes / decompression / CSV schema | NOT_CAPTURED |
| Symbol and ISIN field validation | NOT_DONE |
| Listing-date field semantics | UNKNOWN |
| Collector acquisition implementation | NOT_DONE |

## 4. Engineering decision
No code change is justified. Do not assume the candidate endpoint's query contract, response fields, file path composition, or report selector. Do not synthesize an attachment URL from the filename. The next valid implementation gate requires a successful response from an NSE-controlled host with:
1. an explicit NSE-listed-only report identity;
2. an explicit selected trading date;
3. a returned attachment URL on an approved NSE host;
4. a downloadable gzip payload whose magic bytes and decompression validate;
5. an observed CSV header with verified symbol and ISIN fields.

After that gate, the collector can preserve the raw gzip and record observed source URL, retrieval UTC timestamp, content-type, byte count and SHA-256. Listing date remains UNKNOWN unless a validated field exists.

## 5. Protected invariants
Audit-only. No production workflow, selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 or Engines A-E changes. No paid APIs, credentials, fabricated timestamps, guessed URLs, synthetic data or inferred listing dates. ₹0. UNKNOWN never PASS.
