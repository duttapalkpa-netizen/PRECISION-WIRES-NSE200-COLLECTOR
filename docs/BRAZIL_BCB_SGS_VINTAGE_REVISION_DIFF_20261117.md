# BCB SGS Vintage Revision Difference Audit — 2026-11-17
Status: IMPLEMENTED; FIRST BASELINE VERIFICATION PENDING; SECOND VINTAGE NOT YET AVAILABLE

## Purpose
Avoid repeating any BCB capture or the already completed January/September reconciliation. The first prospective snapshot exists at `data/raw/bcb/sgs_vintage_snapshots/20261117T132939Z/`. This task adds a fail-closed comparator for future snapshots.

## What the tool does
- Enumerates only timestamped snapshot directories with a manifest.
- Verifies the exact raw CSV byte length and SHA-256 against each manifest.
- Validates HTTP 200 and prior CSV PASS flags, exact four-series set (22924, 22930, 22936, 22942), CSV header, numeric values, ascending unique dates, row count, month set, and every value/date against the manifest.
- Requires timezone-aware capture and retrieval timestamps.
- Compares the two latest snapshots only after source URL and capture-time compatibility checks.
- Reports unchanged, changed, added and removed monthly observations separately, with exact old/new values and numeric delta.
- Never attributes a cause. A value change is only a difference between captured current-response vintages.

## Current baseline boundary
One genuine snapshot is available. The audit must therefore return `WAITING_FOR_SECOND_VINTAGE`, not a revision PASS. It must not generate a second snapshot or infer the old February-2026 as-published value.

## Runtime and storage
A bounded GitHub Actions workflow runs when the comparator or a snapshot directory changes on the research branch. It has a five-minute timeout, commits a timestamped QA JSON result, and uploads the result as a 90-day artifact. No network calls are made by the comparator.

## Acceptance criteria
- First snapshot raw/manifest integrity: required for PASS.
- One snapshot: `WAITING_FOR_SECOND_VINTAGE`; baseline validation PASS only.
- Two snapshots: compare all four series across the union of months; record exact diffs and hashes.
- Any URL, hash, byte length, date-order, duplicate, series-set, manifest-value, or timestamp failure: fail closed.
- Revision cause: always UNKNOWN unless separately supported by an official BCB revision notice or immutable original-vintage source.

## Current status
- Comparator implemented: PASS (code committed).
- Workflow implemented: PASS (code committed).
- First baseline integrity/runtime: PENDING.
- Two-vintage revision detection: NOT_DONE; second real snapshot required.
- February-2026 original-vintage cause: UNKNOWN / NOT_PROVEN.
- Brazil pilot: NOT_ACCEPTED; EM panel: NOT_DONE; production integration: NOT_AUTHORIZED.

## Invariants
₹0; official BCB data only; no synthetic market observations, no inferred timestamps, no raw overwrites, no production selector/scoring/CORE-672/Engines A-E/Hard Gate/parser-admission changes.
