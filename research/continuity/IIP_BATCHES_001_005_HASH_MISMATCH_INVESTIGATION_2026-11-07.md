# IIP certified batches 001-005 consolidated audit — 2026-11-07

## Result
The consolidated audit enumerates 54 rows across five existing ledgers and finds 54 unique transition keys. Row counts agree with each batch summary. The audit does **not** pass provenance integrity: four stored CSV digest declarations do not match the current checked-out file bytes.

## Exact discrepancies
- Batch 001: summary field `ledger_csv_sha256` is `334bda7be9fdb441fcbdb217fb4ed861724b33e1bc3edda6b7fe2bfbc122d165`; current audited file is `research/continuity/IIP_CELL_LEVEL_REVISION_BATCH_001_2023-04.csv`, SHA-256 `b30e8135bf0f0edc421c3fa6bd7e78bdbc5d023f33be8bf8f609dac35172e97c`. The summary may refer to the separate `data/macro` copy; do not silently substitute or rewrite either digest.
- Batch 003: declared `175ebc61bb55835a8cd50e7053094ddea56041339dced060a738b7a2ad37d2bc`; current `5a92bfa5797d495537de440f881bb06bb4a081b8c610f4860f0c48b7efbdb4e1`.
- Batch 004: declared `a34b3e634c36e11bb213372235d9d7f76d63672b7d901d2348e3bbabd8e301f9`; current `67834af5b169471d9ab604978c64b7913250f59e2ac6925bb2a67604578b914b`.
- Batch 005: declared `338a2bc02919b5b4907a817a4061df72e3c0866fabd9906a1cf54eb1142712ea`; current `9dc9cd46df57f4969a4081085a7f561ad28e0721be28087d0bcaa170f4948a65`.

## Workflow correctness repair
The first consolidated run (42389739751) had GitHub job conclusion SUCCESS even though the script output was `BLOCKED_BATCH_LEDGER_INTEGRITY`. Root cause: the shell pipeline used `python ... | tee ...` without `set -o pipefail`, so the pipeline exit status came from tee. The workflow was repaired to enable pipefail and upload the audit JSON with `if: always()`, ensuring a blocked audit fails the job while retaining diagnostic evidence.

## Interpretation and no-repeat controls
- 54 unique rows were checked; no duplicate transition keys detected.
- No new source-cell certification is granted by this integrity audit.
- Batch 001 summary still records 684 remaining policy-aligned candidates; batches 002-005 carry 45 additional exact-match rows, but do not change the Batch 001 denominator until the candidate-universe accounting is independently reconciled.
- Do not overwrite declared hashes. Resolve the provenance mapping for Batch 001 and reconstruct/verify the intended historical bytes for Batches 003-005 before any hash field is updated.
- IIP source-cell audit and overall Hard Gate remain BLOCKED.
- Production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 unchanged; research spend ₹0.
