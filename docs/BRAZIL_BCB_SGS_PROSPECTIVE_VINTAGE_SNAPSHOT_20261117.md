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
- Recurrence limitation: this workflow lives only on the research branch. GitHub scheduled and manual-dispatch events require the workflow file on the repository default branch; we will not alter the protected/default production branch. Therefore recurring capture is initiated by a push that changes `docs/BCB_SGS_VINTAGE_CAPTURE_TRIGGER.txt` on this research branch after a BCB release. The workflow is deliberately push-only.

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

## First runtime result — PASS (2026-11-17)
- Workflow Run #1 / ID `44093241898`, conclusion SUCCESS; run URL https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/44093241898.
- Snapshot ID: `20261117T132939Z`; directory `data/raw/bcb/sgs_vintage_snapshots/20261117T132939Z/`.
- All four official BCData SGS requests returned HTTP 200; all CSV headers, rows, numeric values, ascending date order and uniqueness checks passed.
- Every series contains 381 monthly observations from 1995-01 through 2026-09.
- Raw files and SHA-256:
  - 22924: 8,809 bytes; `f3769425aed38b4ab6ddfce555f10d886d875d21e7c3e46338b7d9bc131524b2`.
  - 22930: 8,669 bytes; `c4730c84ee81765a1c5ae41d91c1ea6f153bcb51ac70ee14b45b453b4dcab776`.
  - 22936: 8,006 bytes; `0d1b040d5b11af0b1b98704a70f4972f2790bdfe3c6e78bb16948c7a31640e24`.
  - 22942: 8,579 bytes; `4c09c850decf3317d27d1c0f4dc4aa68dc4f0b3aa2aafacfece113ff7f9c7169`.
- Snapshot manifest SHA-256: `4821d71e2308c7ac35ebf765c70c465baa9d9c1ec50be3ca1f44fd2af8a7ed0b`.
- Immutable snapshot Git commit: `6237baa` (full commit is on branch history); files: manifest plus four raw CSVs.
- Artifact ID `14333041266`, 26,480 bytes; archive SHA-256 `7955c0f65379130939258cbd9fcd25c5d1108d49346b4eae0bf1297132897dca`; expires 2027-02-15.
- Latest SGS 22942 February-2026 value in this baseline remains USD 2,783.2m. This is a current response snapshot, not the original March-2026 as-published vintage.
- Structured runtime result: `data/qa/BRAZIL_BCB_SGS_PROSPECTIVE_VINTAGE_BASELINE_20261117.json`.
- Acceptance: first prospective baseline PASS; change detection NOT_DONE until a second timestamped snapshot; February-2026 original-vintage cause UNKNOWN / NOT_PROVEN; Brazil pilot NOT_ACCEPTED; EM panel NOT_DONE; production integration NOT_AUTHORIZED.


## Trigger safety correction
GitHub documents that both `schedule` and `workflow_dispatch` require the workflow file to exist on the default branch; scheduled runs execute on the default branch. This research workflow is intentionally isolated to the research branch, and no default/production branch change is authorized. The workflow was therefore corrected to be push-only, watching `docs/BCB_SGS_VINTAGE_CAPTURE_TRIGGER.txt`. A future monthly snapshot is initiated by updating that trigger file on the research branch after the relevant BCB release. The first baseline run above remains valid; no claim of unattended monthly scheduling is made.
