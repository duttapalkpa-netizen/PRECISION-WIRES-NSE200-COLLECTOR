# Global Capital Rotation — Source Registry and Runtime Gate Audit

Date: 2026-11-17
Branch reviewed: research/taxonomy-crosswalk-contract-20261117
Scope: static inspection only; no runtime execution, no data ingestion, no production change.

## Exact artifacts inspected
- Research-only parser: pipeline/global_capital_rotation_overlay.py
- Parser blob SHA: 38c05239cd805ce1d9e44edb14008eb280c7f2f3
- Source registry: config/global_capital_rotation_source_registry.json
- Registry blob SHA: 0db25e919abab6db5b8e00ab678710d7e314b587
- Registry schema_version=1; policy=fail_closed_exact_match_and_raw_payload_manifest_required; sources=[] (empty intentionally).

## What the current parser does enforce (static code evidence)
- Requires the core observation columns and allowed quality labels.
- Loads a schema-versioned source registry; trusted rows require an exact tuple match on source, source_url, indicator, unit and quality_status.
- Trusted rows require evidence fields: evidence_manifest_id, raw_sha256, retrieved_at, http_status, content_type, byte_length and raw_payload_path.
- Checks 64-character lowercase SHA-256 syntax, manifest-ID syntax, HTTP 200, positive byte length, retrieval/publication chronology, registry-approved content type, input-directory path containment, and recomputes payload byte length and SHA-256.
- UNKNOWN and PROVISIONAL rows are not admitted to trusted classifier observations.
- Reproducible classification requires as_of_date and decision_at; stale observations are excluded rather than forward-filled.

## Current runtime admission state
- Registry has zero entries. Therefore no VERIFIED_OFFICIAL or VERIFIED_SECONDARY row can pass the exact registry tuple match in this branch as currently configured.
- This is a deliberate fail-closed state, not a parser success for any live indicator. The overlay cannot yet admit any trusted source observations until entries are independently qualified and added.
- Do not loosen the empty registry or add guessed domains/units/content types merely to make the pipeline run.

## Remaining static trust-boundary gap
- The parser validates the evidence fields carried in each CSV row and independently hashes the referenced raw payload file. However, in the inspected function it does not open or validate a separate immutable evidence-manifest object keyed by evidence_manifest_id.
- Consequently evidence_manifest_id is currently syntax-checked but not resolved to an independently stored manifest record. retrieved_at, final URL, HTTP status, content type and byte length are accepted from the CSV row itself; only payload bytes/length/hash are independently rechecked. The row's source_url is exact-matched to the registry, but the manifest is not proven to attest that same final URL, response metadata, publication/vintage timestamp, and payload hash as one indivisible record.
- This is a static code-level gap, not evidence of observed tampering or incorrect live observations. No runtime exploit test was run.

## Acceptance and status
- Parser fail-closed source-registry matching: STATIC_REVIEW_PASS.
- Raw payload byte length and SHA-256 re-computation: STATIC_REVIEW_PASS.
- Registry currently populated with qualified indicator/source/unit/content-type tuples: BLOCKED / EMPTY_BY_DESIGN.
- Manifest ID resolution and manifest-to-row field binding: GAP_CONFIRMED_STATIC.
- Runtime tests on this branch: NOT_RUN in this audit.
- Actual trusted observation ingestion: NOT_DONE.
- Point-in-time historical replay validation: NOT_DONE.
- Predictive validation: NOT_DONE.
- Production integration: NOT_AUTHORIZED.

## Next bounded remediation (do not repeat taxonomy or H.10 discovery)
1. Define an immutable manifest schema and storage convention with a manifest ID resolving to a canonical JSON record.
2. Bind the manifest's final URL, retrieval timestamp, HTTP status, content type, byte length, SHA-256, source publication/vintage, source ID and raw payload path to the CSV row; reject every mismatch.
3. Add offline tests for unknown manifest ID, manifest/CSV URL mismatch, timestamp mismatch, status/content-type mismatch, byte-length mismatch, hash mismatch, path traversal, and one fully valid fixture.
4. Only after those tests pass, qualify source-registry entries one at a time from already reviewed official sources. Keep unqualified indicators UNKNOWN.
5. Do not enable any live observation merely to fill the empty registry; require exact unit, cadence, field semantics, publication-vintage and payload evidence for each tuple.

## Invariants
Documentation-only audit. No parser, registry, tests, workflows, observations or production files changed. No synthetic market data, timestamps or hashes. ₹0. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E, Hard Gate and collector workflows unchanged. UNKNOWN is never PASS.
