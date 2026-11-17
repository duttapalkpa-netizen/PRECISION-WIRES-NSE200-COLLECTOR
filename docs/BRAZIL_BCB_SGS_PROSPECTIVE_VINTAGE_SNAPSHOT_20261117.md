# BCB SGS Prospective Vintage Snapshot — Design and Acceptance Contract
Date: 2026-11-17
Status: IMPLEMENTED; FIRST RUNTIME CAPTURE PENDING

## Why this work was selected
The February-2026 SGS 22942 discrepancy is isolated and quantified, but BCB's public SGS/BCData resources expose the current time series and no immutable as-of-date revision endpoint or public revision log was identified in the inspected official material. The official BCB Open Data dataset for SGS 22942 provides JSON/CSV/WSDL resources, metadata, monthly frequency, unit (USD million) and coverage from 1995-01. It does not advertise a vintage-history resource. Therefore historical original-vintage reconstruction cannot be claimed from the live series response.

This work establishes a prospective point-in-time record so future revisions can be measured without inventing a historical cause.

## Series captured together
- SGS 22924: portfolio investment liabilities net — aggregate comparator.
- SGS 22930: domestic-market equity liabilities net.
- SGS 22936: investment-fund liabilities net — Table 10 footnote documents nonresident quota holders with less than 10% of fund NAV in Brazil.
- SGS 22942: domestic-market debt securities liabilities net — target discrepancy series.

## Capture contract
- Official BCB BCData SGS CSV endpoints only; no paid API, no credentials.
- Each workflow execution creates a unique UTC timestamp directory. It never overwrites prior snapshots.
- Store exact raw CSV bytes separately for each SGS code.
- Manifest stores requested/final URL, HTTP status, response headers, UTC retrieval start/end, byte length, SHA-256, content type, first/last period, row count, latest observation, and February-2026 observation where present.
- CSV validation fails closed on wrong header, malformed row, duplicate month, non-ascending dates, invalid numeric values, empty response, non-200 HTTP, or unexpected content type.
- Workflow commits the timestamped raw snapshot to the research branch and uploads an artifact; 6-minute timeout.
- Schedule: monthly on day 28 at 12:17 UTC; manual dispatch available for a new observation after a BCB release.

## Interpretation limits
- This is a snapshot of the current SGS response at the recorded retrieval timestamp, not an original publication-vintage reconstruction.
- A revision is detected only by comparing the same reference-month value across two or more snapshots.
- A change between snapshots proves that the value changed between capture times; it does not prove the cause unless BCB publishes supporting evidence.
- A future snapshot cannot reconstruct the missing March-2026 as-published value. The February 2026 discrepancy therefore remains UNKNOWN / BLOCKED until an immutable historical source is found.

## Acceptance
- Code and workflow committed: PASS.
- First 4-series runtime capture: PENDING.
- Raw per-series hashes and immutable GitHub commit: PENDING.
- Cross-snapshot revision detector: NOT_DONE (requires at least two snapshots).
- February-2026 original-vintage reconciliation: BLOCKED.
- Brazil pilot: NOT_ACCEPTED.
- EM-wide panel: NOT_DONE.
- Production integration: NOT_AUTHORIZED.

## Next bounded actions
1. Verify first scheduled/push-triggered capture and inspect the committed manifest/hashes.
2. After a second monthly snapshot, compare common reference months across manifests and report only changed values with exact before/after timestamps and hashes.
3. Keep the February-2026 original-vintage cause UNKNOWN unless BCB publishes an authoritative historical version or revision notice.

## Protected invariants
Research-only; ₹0; official free BCB sources only. No synthetic data, no forward-fill, no inferred timestamps or hashes. Do not alter Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A–E, Hard Gate, parser admission, seed observations, or production workflows.
