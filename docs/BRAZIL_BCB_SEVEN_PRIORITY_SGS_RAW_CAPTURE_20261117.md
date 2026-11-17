# Brazil BCB Seven Priority SGS Raw Capture — 2026-11-17
Status: IMPLEMENTED ON ISOLATED RESEARCH BRANCH; RUNTIME NOT YET VERIFIED
Branch: `research/bcb-priority-metadata-audit-20261117`

## Why this is the next task
The seven official dataset identities, monthly frequency, USD-million units and 1995-01 coverage are already metadata-qualified. Repeating metadata discovery would add no value. The remaining highest-value dependency is raw observation bytes with transport provenance and SHA-256.

## Official raw resource route
Each official BCB dataset page exposes a CSV resource named `csv_serie-sgs-{code}`. The BCB portal's Download link for SGS 22905 and 22924 resolves to the BCData/SGS route pattern:
`https://api.bcb.gov.br/dados/serie/bcdata.sgs.{code}/dados?formato=csv`.
The other five official dataset pages expose the corresponding code-specific CSV resources. The exact URLs are generated only from the seven allow-listed SGS codes in the capture script.

## Seven series
22905 total portfolio investment net; 22906 asset net; 22907 asset inflows; 22908 asset outflows; 22924 liability net; 22925 liability inflows; 22926 liability outflows.
All remain separate series. No sign conversion, addition/subtraction, or combined flow is performed.

## New files
- `scripts/research/capture_bcb_priority_sgs_csv.py`
- `.github/workflows/bcb_priority_sgs_raw_capture.yml`

## Capture contract
For each code, the script captures the entire unbounded official CSV response as raw bytes and records request/final URL, UTC retrieval start/end, HTTP status, all response headers, content type, byte length, SHA-256, UTF-8 sanity check and sniffed delimiter. It rejects empty bodies and obvious HTML error pages. Partial failures are recorded per series; the job exits non-zero unless all seven pass. Raw files and manifest are uploaded with `if: always()`, 90-day retention, and an 8-minute timeout.

The first pass is deliberately transport/raw-byte acceptance only. It does not assume date/value column names or decimal conventions, does not calculate accounting identities, and does not promote observations to the trusted feature registry.

## Acceptance state before runtime
- Seven official metadata identities: PASS (prior audit; not repeated).
- CSV resource routes: official portal resource links verified; 22905 and 22924 Download URLs independently resolved to the API URL pattern.
- Raw observation bytes: NOT_DONE until workflow artifact inspected.
- HTTP metadata / SHA-256: NOT_DONE until artifact inspected.
- Date ordering, duplicates, missing periods, numeric parsing: NOT_RUN.
- Accounting sign and net/component reconciliation: UNKNOWN / NOT_DONE.
- Brazil pilot: NOT_ACCEPTED.
- EM-wide panel: NOT_DONE.
- Production integration: NOT_AUTHORIZED.

## Next action
Check for the push-triggered run. If absent, manually dispatch this workflow once on the branch. Inspect all seven raw files and manifest even if the run fails. Only then design a separate parser/QA stage based on the actual CSV schema.

## Protected invariants
Research-only; no paid APIs, no production changes, no PR merge. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and Hard Gate remain unchanged. UNKNOWN never PASS. No synthetic observations, forward fill, guessed sign, or fabricated timestamps/hashes. ₹0.
