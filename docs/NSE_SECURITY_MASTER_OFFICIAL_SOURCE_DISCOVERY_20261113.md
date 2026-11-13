# NSE CM Security Master — Official Source Discovery Audit
Audit date: 2026-11-13 (Asia/Kolkata)
Status: SOURCE_DISCOVERY_PASS / RAW_ACQUISITION_PENDING
Scope: verify the official NSE report catalogue exposes the two distinct CM-MII security-master report variants; do not claim file acquisition or ISIN reconciliation.

## Official source
- NSE All Reports: https://www.nseindia.com/all-reports
- Directly opened official page during this audit: https://www.nseindia.com/all-reports
- The page's report catalogue explicitly lists:
  1. "CM - MII - Security File (.gz) (NSE Listed securities)"
  2. "CM - MII - Security File (.gz) (NSE Listed and BSE Exclusive securities)"
- The dated catalogue section for 11-Nov-2026 displays both entries:
  - NSE Listed securities: NSE_CM_security_11112026.csv.gz, displayed size 1.22 MB.
  - NSE Listed and BSE Exclusive securities: NSE_CM_security_11112026.csv.gz, displayed size 1.49 MB.
- The report catalogue also shows the 12-Nov-2026 section, but the two security-master entries are not shown there in the captured catalogue result. Do not infer a 12-Nov master exists.
- The catalogue labels and displayed sizes establish two distinct report variants despite the same displayed filename stem. Preserve the variant label, report date and download context as separate metadata; never overwrite one with the other based only on filename.

## Acceptance decision
- PASS: official NSE catalogue route and report labels verified.
- PASS: two distinct 11-Nov-2026 catalogue variants and displayed sizes recorded.
- UNKNOWN: exact downloadable URLs, response MIME types, byte counts, raw file bytes and SHA-256 values; this browser extraction exposed catalogue text, not the downloadable file payloads.
- NOT_STARTED: decompression, header/schema QA, row counts, duplicate checks, ISIN coverage, symbol/name/series reconciliation, and effective-dated security classification.
- NOT_ESTABLISHED: whether NSE Listed and NSE Listed + BSE Exclusive variants are identical subsets or have other schema/content differences. Must compare raw bytes and parsed rows before deciding.
- No claim is made that the 11-Nov file is a 12-Nov or 13-Nov security master.

## Method safeguards carried forward
- Do not infer direct download URLs from filenames.
- Capture the exact official link target and raw response before recording bytes/MIME/SHA-256.
- Keep the two variants separate until byte-level and row-level comparison.
- Preserve source date, report variant, retrieval timestamp, HTTP status, MIME, byte count, SHA-256, decompression result and schema version.
- Treat missing fields/records as UNKNOWN until independently evidenced; no synthetic rows or guessed ISIN mappings.
- Do not alter production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56 × 12), or the Hard Gate.
- ₹0 spend; free official sources only; no paid APIs; no PR merge or production integration.

## Next gated operation
Acquire the two exact 11-Nov-2026 official download payloads independently, then compute SHA-256 and compare compressed and decompressed contents. Only after raw integrity passes should schema/ISIN reconciliation begin.
