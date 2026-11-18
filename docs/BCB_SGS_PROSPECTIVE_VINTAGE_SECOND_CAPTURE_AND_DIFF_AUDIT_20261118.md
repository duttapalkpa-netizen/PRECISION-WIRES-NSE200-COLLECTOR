# BCB SGS Prospective Vintage — Second Capture and Two-Vintage Diff Audit
Date: 2026-11-18 (UTC)
Status: PASS_TWO_VINTAGES_COMPARED

## Objective
Verify the missing second real capture and prove the prospective capture → immutable archive → manifest verification → two-vintage comparator chain works, without changing production logic.

## Trigger gap found and corrected
- The capture workflow watched `docs/BCB_SGS_VINTAGE_CAPTURE_TRIGGER.txt`, but the trigger file did not exist on the research branch.
- Created the trigger file in commit `f36a5b4e0e423170b1ae1f7dd9bb1989c4f2e83d`.
- Capture workflow run #2 / ID `44239680043`: SUCCESS; all capture, immutable snapshot commit and artifact upload steps succeeded.
- Snapshot directory: `data/raw/bcb/sgs_vintage_snapshots/20261118T044659Z/`.
- Snapshot captured at `2026-11-18T04:46:59.635249+00:00`.
- Manifest SHA-256: `0e72d5c572ca1a86cd4a4be3fbf3d2b415d0376ef4df3994a7f06beda54ef1c3`.
- Capture artifact ID `14399231070`; artifact digest SHA-256 `93e8e2663bc80df97e43a986b7fa142fb89cc59f39ff624bcef9715f38d7f228`; expires 2027-02-16.
- Four official SGS CSV requests returned HTTP 200; each series has 381 rows (1995-01 to 2026-09); strict CSV validation PASS.
- Raw CSV SHA-256 values match the first baseline exactly:
  - 22924: `f3769425aed38b4ab6ddfce555f10d886d875d21e7c3e46338b7d9bc131524b2`
  - 22930: `c4730c84ee81765a1c5ae41d91c1ea6f153bcb51ac70ee14b45b453b4dcab776`
  - 22936: `0d1b040d5b11af0b1b98704a70f4972f2790bdfe3c6e78bb16948c7a31640e24`
  - 22942: `4c09c850decf3317d27d1c0f4dc4aa68dc4f0b3aa2aafacfece113ff7f9c7169`

## Comparator execution and result
- Capture workflow's GITHUB_TOKEN commit did not itself start the downstream comparator. To avoid silently claiming automatic chaining, the comparator workflow file was explicitly touched on the research branch in commit `3eb60ad0706f0beecc196151ca786e27fc398195`, which triggered the comparator.
- Comparator run #2 / ID `44239773135`: SUCCESS; all six primary workflow steps succeeded.
- QA output: `data/qa/BCB_SGS_VINTAGE_REVISION_DIFF_20261118T044659Z.json`; Git blob SHA `316eca24f81f93d7e1fbdeaec21a29ff8a091e1a`.
- Artifact ID `14399146898`; size 1,955 bytes; SHA-256 `16b924beb56dd026a417514a65c216ce7e33c137496924a6365d99572fe4d1a3`; expires 2027-02-16.
- Two genuine snapshots were compared: 2026-11-17T13:29:39.897799Z and 2026-11-18T04:46:59.635249Z.
- 4 series × 381 months = 1,524 observation comparisons: unchanged 1,524; changed 0; added 0; removed 0.
- Per-series changed/added/removed counts all zero. Raw CSV SHA-256 values match across snapshots.
- For SGS 22942, the February-2026 current-response value remains USD 2,783.2m; this does not recover the original March-2026 publication vintage or explain the earlier +USD 203.70779636m gap.

## Important interpretation and operational findings
1. This is a real two-vintage comparison, so the comparator gate is now PASS for these two retrieval times. It only proves no observed changes between the two captured current responses; it does not prove no revision occurred before the first capture.
2. A 15-hour interval with zero differences is not a meaningful monthly revision-monitoring period. The next valuable capture should follow the next BCB external-sector release.
3. Official BCB release calendar lists the October-2026 reference release for 26-Nov-2026 at 11:30 (BCB calendar local time). Trigger a new snapshot after that release is available; then compare it with this 18-Nov baseline.
4. The capture workflow is push-triggered on the research branch; it is not an unattended schedule. The comparator currently needs an explicit workflow-file push after a snapshot commit produced by GITHUB_TOKEN. Do not claim an automatic capture→diff chain.
5. Do not repeat the 15-series live/archive audit, original vintage search, accounting identities, or general BOP methodology audit.

## Acceptance
- Trigger file exists: PASS.
- Second real prospective snapshot: PASS.
- Raw bytes, SHA-256, HTTP metadata, UTC timestamps, strict CSV validation: PASS.
- Two-vintage comparator: PASS_TWO_VINTAGES_COMPARED.
- 1,524/1,524 unchanged; 0 changes/additions/removals in this short interval.
- Original February-2026 publication vintage and cause: UNKNOWN / NOT_PROVEN.
- Brazil pilot: NOT_ACCEPTED.
- Production integration: NOT_AUTHORIZED.

## Protected invariants
Research-only; ₹0; official/free BCB sources only; no synthetic observations, fabricated timestamps, raw overwrite, inferred revision cause, or production changes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and Hard Gate remain unchanged.
