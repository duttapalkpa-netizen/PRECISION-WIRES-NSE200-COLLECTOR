# IMF BOP Response Provenance Sidecar V1

Status: SCHEMA DEFINED; NOT YET POPULATED WITH A NEW HTTP RESPONSE.
Scope: research branch only. This schema does not alter the existing 110-row India CSV or its manifest.

## Purpose
Record verifiable transport provenance for each future raw IMF BOP response so snapshots can be distinguished without inventing release vintages.

## Files
- JSON Schema: `schemas/imf_bop_response_provenance.schema.json`
- One sidecar JSON instance is required per independently retrieved raw response. Do not reuse a single sidecar for multiple URLs or response bodies.

## Required capture sequence
1. Record the exact requested URL and the final URL after redirects.
2. Perform the real HTTP GET; accept only HTTP 200.
3. Capture actual Content-Type and byte count from the exact response body.
4. Capture retrieval time from the acquisition process clock in UTC, serialized as RFC 3339 with trailing `Z`. Never derive it from commit date, audit date, or file modification time.
5. Compute SHA-256 over exact response body bytes before parsing, normalizing, decompressing at the application layer, or rewriting.
6. Inspect source metadata for an explicit publication/release vintage. If absent, set status `NOT_EXPOSED_BY_SOURCE`, with release_date and release_id null. If not inspected or evidence is inconclusive, use `NOT_VERIFIED`. Never copy retrieval date into release_date.
7. Preserve request query parameters and exact series key.
8. Validate the sidecar against the JSON Schema before accepting the response into a revision-aware panel.

## Status semantics
- `SOURCE_PROVIDED`: source explicitly exposes a release date/identifier; include evidence_url.
- `NOT_EXPOSED_BY_SOURCE`: source was checked and no release vintage field/identifier was exposed for this response.
- `NOT_VERIFIED`: vintage evidence was not adequately inspected. This is UNKNOWN, not proof of absence.

## Acceptance and failure handling
- Missing retrieval timestamp, final URL, HTTP status, Content-Type, byte count, or valid SHA-256 => provenance sidecar REJECTED.
- HTTP non-200 or empty body => response acquisition REJECTED; retain diagnostic separately, do not present as valid data.
- Invalid schema, unexpected fields, or inconsistent vintage status => REJECTED pending correction.
- Repeated response hashes may be retained as separate retrieval events; do not deduplicate away timestamps.
- This schema records response provenance, not proof that two responses are distinct publication vintages. Revision comparison additionally requires source-supplied vintage evidence or independently archived dated releases.

## Existing India panel boundary
The committed 110-row CSV and manifest predate this schema. They remain valid archived snapshot evidence under their original checksums, but they are NOT retroactively compliant with this new sidecar contract. Do not backfill fabricated timestamps or release vintages. A future actual pull must create a new sidecar and a separately versioned snapshot; do not overwrite the prior CSV/manifest.

## Research controls
₹0 spend, official public sources only, no credentials or login bypass, no synthetic values/timestamps, no production integration, no PR merge without approval.
