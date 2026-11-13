# NSE CM-MII 11-Nov-2026 Raw Download Resolution Check
Audit date: 2026-11-14 (Asia/Kolkata)
Status: OFFICIAL_REPORT_LIST_CONFIRMED / DIRECT_VARIANT_URL_UNRESOLVED / RAW_BYTES_NOT_ACQUIRED
Scope: resolve the next raw-acquisition gate for the two 11-Nov-2026 NSE CM-MII security-master variants. Research-only; no production changes.

## Official report-list evidence
Official NSE All Reports page:
https://www.nseindia.com/all-reports

The retrieved page snapshot for Reports for 11-Nov-2026 lists both:
1. `CM - MII - Security File (.gz) (NSE Listed securities)` — displayed basename `NSE_CM_security_11112026.csv.gz`, displayed size 1.22 MB.
2. `CM - MII - Security File (.gz) (NSE Listed and BSE Exclusive securities)` — same displayed basename `NSE_CM_security_11112026.csv.gz`, displayed size 1.49 MB.

The page snapshot for 12-Nov-2026 does not list either CM-MII file in the captured report list. This is a statement about that retrieved page snapshot only; it is not evidence that a file was never published elsewhere.

## Retrieval attempt and fail-closed outcome
- The All Reports page's extracted text exposes the two report labels, displayed basename and displayed sizes, but not the per-row downloadable hrefs.
- Opening the candidate NSE archive path `https://nsearchives.nseindia.com/content/cm/NSE_CM_security_11112026.csv.gz` through the available browser retrieval returned an internal access error. No HTTP status, response headers, MIME, byte count, or payload bytes were obtained.
- A third-party data catalogue describes a generic archive URL pattern, but it is not official NSE evidence for either of the two identically named 11-Nov report rows. It is not promoted as an authoritative download link.
- Because both report rows share the same basename, a guessed URL could resolve only one variant or the wrong variant. No guessed URL, downloaded payload, or SHA-256 is claimed.
- Therefore raw acquisition remains NOT_ACQUIRED; gzip integrity, decompressed bytes, schema, row counts, duplicate checks, ISIN checks, and cross-variant comparison remain NOT_STARTED/UNKNOWN.

## Required acceptance evidence (per variant)
1. Exact row-specific href copied from the official All Reports page or an official NSE-provided download response.
2. HTTP status and final URL, response Content-Type, Content-Length/actual byte count, retrieval timestamp (Asia/Kolkata).
3. Raw payload saved without modification; SHA-256 of exact raw bytes.
4. Gzip integrity and decompressed SHA-256.
5. Header/schema, row count, key nulls, duplicate composite keys, ISIN format/uniqueness checks.
6. Separate classification of NSE-listed and combined NSE-listed+BSE-exclusive variants; no assumption that one is a strict superset.
7. Preserve source vintage and raw `PrtdToTrad` values; BSE-exclusive must not be marked ordinary NSE-tradable absent the applicable invocation event evidence.

## Existing user-supplied baseline (not substituted for 11-Nov)
Previously supplied 08-Nov and 09-Nov payloads remain the only verified raw MII inputs in the referenced prior audit manifests. Their hashes and results remain preserved in those manifests. They do not satisfy 11-Nov acquisition.

## Safety / project invariants
- No synthetic data, guessed download URLs, or fabricated timestamps.
- `UNKNOWN` is neither PASS nor FAIL.
- No production selector, `RANKING_SCORE`, `+1 PRESSURE_FADE`, CORE-672 (56×12), Engines A–E, or Hard Gate changes.
- No paid API/service, spending, PR merge, or production integration.
- No raw acquisition PASS is claimed.

## Result
This check confirms the two official 11-Nov report-list entries and documents why the raw-acquisition gate cannot safely be closed from the currently exposed page text. The next decisive input is the exact official per-row download target (or the two raw files supplied directly); once available, byte-level validation and cross-variant comparison can proceed without repeating scope-semantics work.


## Independent official-page recheck (2026-11-14)
A fresh retrieval of the official NSE All Reports page independently returned the date-scoped section "Reports for 11-Nov-2026" and explicitly listed both CM-MII rows with their separate displayed sizes (1.22 MB and 1.49 MB) and the shared displayed basename. The same date-scoped section also listed the Full Bhavcopy/Security Deliverable and CM-UDiFF Bhavcopy reports; these are distinct report products and are not substitutes for the MII master files.

The official page's extracted representation still exposes no row-specific href or download response for either MII row. A direct browser retrieval attempt against the candidate archive URL
`https://nsearchives.nseindia.com/content/cm/NSE_CM_security_11112026.csv.gz`
returned an inaccessible/internal-error result. This does not establish whether the URL is invalid, blocked, or variant-ambiguous; it establishes only that this retrieval channel did not obtain the payload or HTTP metadata.

Updated decision: official listing confirmation strengthened by an independent fresh page retrieval; exact per-row link and raw payload remain UNKNOWN / NOT_ACQUIRED. Do not promote this to raw-source PASS.
