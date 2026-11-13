# NSE CM-MII Security Master — Source Lineage & Acceptance Contract
Audit date: 2026-11-13 (Asia/Kolkata)
Status: OFFICIAL_SOURCE_LINEAGE_PASS / RAW_PAYLOAD_UNKNOWN
Scope: reconcile the official dissemination rule with the two separately labelled report variants currently displayed by NSE; define fail-closed acquisition checks. This is not raw-file acquisition.

## Official source evidence
1. NSE Circular NSE/MSD/60315, dated 19-Jan-2024, effective 05-Feb-2024:
   - states CM MII security master filename pattern `NSE_CM_security_ddmmyyyy.csv.gz`
   - display name: "CM - MII - Security File (.gz)"
   - website path: https://www.nseindia.com/all-reports
   - official circular: https://nsearchives.nseindia.com/content/circulars/MSD60315.pdf
2. NSE Capital Market Consolidated Circular NSE/CMTR/73927, Circular 56/2026, dated 28-Apr-2026:
   - current consolidated circular replacing the 30-Apr-2025 consolidated circular; use it as current rulebook context.
   - source PDF: https://avantiscdnprodstorage.blob.core.windows.net/legalupdatedocs/55296/NSE-issued-a-circular-regarding-the-Capital-Market-Consolidated-Circular-April282026.pdf
3. NSE All Reports page (live catalogue, opened 13-Nov-2026):
   - for 11-Nov-2026 it lists two separate entries:
     a. "CM - MII - Security File (.gz) (NSE Listed securities)" — displayed filename `NSE_CM_security_11112026.csv.gz`, displayed size 1.22 MB.
     b. "CM - MII - Security File (.gz) (NSE Listed and BSE Exclusive securities)" — same displayed filename, displayed size 1.49 MB.
   - for 12-Nov-2026 the captured dated list does not show these two CM-MII entries. No 12-Nov CM-MII file is inferred.
   - official catalogue: https://www.nseindia.com/all-reports

## Reconciliation / interpretation
- The 2024 circular establishes the generic daily CM-MII filename pattern and official website location.
- The current live catalogue differentiates two report scopes (NSE Listed only vs NSE Listed + BSE Exclusive) while displaying the same filename stem and different sizes.
- These sources do not establish that the two variants are byte-identical, subset/superset, interchangeable, or that their contents share the same row universe.
- Treat each as a separate source series with independent retrieval metadata. Do not key storage solely by the filename. Use a compound identity: exchange + segment + report date + catalogue scope label + source URL + retrieval timestamp.
- The 2024 generic circular is not sufficient to infer the precise download URL or the complete scope semantics of each 2026 variant. The 2026 consolidated circular is a current rulebook reference, not evidence that the raw payload was fetched.

## Fail-closed acquisition contract
Before accepting either file:
1. Resolve and record the exact clickable download target from the live NSE catalogue; never construct a URL from the filename.
2. Fetch each scope independently. Record UTC and IST retrieval timestamps, HTTP status, final URL, response Content-Type, Content-Length, actual byte count, and SHA-256.
3. Reject non-2xx responses, HTML/JSON error bodies, empty bodies, mismatched content type, or gzip magic-byte failure. Never cache an access-denied page under a .gz filename.
4. Decompress with integrity check; record decompressed byte count and SHA-256.
5. Parse headers and row counts separately per scope. Preserve raw rows; test blank/duplicate identifiers, ISIN format/uniqueness, symbol/name/series fields, and schema drift.
6. Only then compare scopes: exact row equality, set inclusion, scope-specific additions, duplicate keys and conflicting field values. Do not assume superset from larger displayed size.
7. Cross-check selected fields against same-date official NSE Bhavcopy/security deliverable and official security master metadata; mismatches remain UNKNOWN pending evidence.
8. Preserve source vintage and all raw hashes in immutable manifest.

## Acceptance state
- PASS: official generic CM-MII filename pattern and All Reports route evidenced by NSE circular.
- PASS: live catalogue confirms two distinct 11-Nov-2026 scope labels and different displayed sizes.
- UNKNOWN: exact download hrefs, raw bytes, MIME, HTTP status, byte counts, SHA-256, gzip integrity, decompressed hashes, schema and row counts.
- NOT_STARTED: ISIN/symbol/series reconciliation and variant comparison.
- NOT_ESTABLISHED: 12-Nov-2026 security-master availability.
- This work package does not change any V11.3 production logic or Hard Gate.

## Prior failure controls
- A successful HTTP response is not proof of a valid data file.
- Filename extension is not proof of payload format.
- Same filename is not proof of same content.
- Displayed MB size is catalogue metadata, not actual byte count.
- Missing date/section must remain UNKNOWN; do not carry forward prior-day master silently.
- No synthetic rows, inferred timestamps, guessed URLs, paid APIs, or spending.

## Project invariants
Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56 × 12), Engines A–E, and Hard Gate remain unchanged. ₹0 spend, free official sources only. No PR merge or production integration without explicit approval.
