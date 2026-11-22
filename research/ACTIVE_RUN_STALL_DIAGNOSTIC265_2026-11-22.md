# Active Run Stall Diagnostic — C265

Date: 2026-11-22
Branch: `audit/prospective-selector-tracking`

## Continuity review
Re-fetched `research/GITHUB_MASTER_CONTINUITY_LEDGER.md`, C264 report, and current `collector/nse_download.py`. Prior PASS work was not repeated; no source code was changed. The collector holiday scope remains the C260 correction. Production invariants remain untouched.

## Direct Actions API poll
At 2026-11-22T08:15:14Z:
- Run #393 / ID `45001043441`, SHA `9fac7d42bd09f6b0a4d9a4c0742a36451816e0a4`: still `in_progress`; job `137143246564` still `in_progress`. Last completed step remains “Validate normalized quarterly metrics and build features (audit only)” SUCCESS; “Run corrected-label walk-forward audit only” remains IN_PROGRESS. No artifacts published. Run updated_at remains 08:07:23Z.
- Run #317 / ID `45001040455`, SHA `885528a076e98996455358ee236f1a2960a276ea`: still `in_progress`; job `137143161030` still `in_progress`. Last completed step remains canonical NSE 200-session panel SUCCESS; “Collect P0 market series and timestamped media evidence” remains IN_PROGRESS. NSDL historical FPI/DII step not reached. No artifacts published. Run updated_at remains 08:07:02Z.
- Both job-log download attempts returned Azure BlobNotFound at 08:15:14Z. This is a log retrieval limitation, not evidence of workflow failure or success.
- No workflow conclusion, no artifact, and no new source-level outcome available. Thus no defensible new PASS/FAIL can be assigned.

## Decision / highest-value action
The only evidence-backed action is to preserve the current execution state and avoid duplicate workflow launches or speculative code changes. Existing runs have not advanced since C264 poll; wait for GitHub Actions to advance and then inspect new step/artifact outputs. Do not rerun or modify active run inputs solely because logs are unavailable.

## Rejected
- Rejected repeating C254 clipping, C260 holiday correction, and all successful acquisition/QA steps.
- Rejected inferring run failure from a BlobNotFound log endpoint.
- Rejected treating the still-running walk-forward or P0 market/media step as PASS.
- Rejected claims about NSDL 2026-07-17 / 2026-08-26 query outcomes; the NSDL step is not reached.
- No synthetic values, fabricated timestamps, paid APIs, or production changes.

## Exact next actions
1. Re-poll #393 and #317 after their status/updated_at changes.
2. If #317 reaches “Collect official NSDL historical FPI/DII daily flows”, inspect artifact and actual date-specific outcomes for 2026-07-17 and 2026-08-26.
3. If #393 completes, inspect complete conclusion and artifacts, including matured sample counts and strict hard gate.
4. If jobs remain unchanged, inspect workflow-run annotations/checks only; do not create duplicate runs.
5. Keep unresolved NSDL data, USDINR, and mature event windows UNKNOWN/BLOCKED until official evidence appears.
