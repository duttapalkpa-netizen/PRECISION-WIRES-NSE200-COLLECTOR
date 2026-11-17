# BCB Monthly BOP Historical ZIP — Permanent Vintage Archive
Status: PASS — HISTORICAL VINTAGE COMMITTED AND RE-FETCHED WITH SHA-256 VERIFICATION
Source capture: Run #1 / ID 44076495816; artifact 14324932604.
Source URL: `https://www.bcb.gov.br/ftp/notaecon/balpagm.zip`
Inner ZIP SHA-256: `e58d64374d13ae62fb2af95e4bd26acaf924f0da113a825842307c95219dec4b`
Raw ZIP byte length: 2,813,472.
HTTP status: 200; ZIP CRC: PASS.
The inner ZIP contains one member: `BalPagM.xlsx`, 2,875,732 bytes, internal file date 2019-03-22.

The archive is an older BPM6 historical snapshot, not the current 2026 data vintage. It must be preserved as a separate historical vintage and never overwrite the current SGS CSVs.

The archive workflow downloads the existing capture artifact (no source re-fetch), validates raw ZIP byte length/hash and CRC, commits exact ZIP bytes with `*.zip -text`, then re-fetches the committed Git blob and verifies SHA-256. Target path: `data/raw/bcb/monthly_bop_history_20190322/`.

Acceptance: workflow code COMPLETE; runtime commit/re-fetch PENDING until Actions run succeeds.


## Verified archive result
- Archive workflow Run #1 / ID `44077157516`: SUCCESS.
- Permanent archive commit: `88eebada24c1619d82292bb757df64e4372851ad`.
- Durable path: `data/raw/bcb/monthly_bop_history_20190322/`.
- Original ZIP byte length: 2,813,472.
- Original ZIP SHA-256: `e58d64374d13ae62fb2af95e4bd26acaf924f0da113a825842307c95219dec4b`.
- Workflow verified the original capture manifest, ZIP CRC, and post-commit `git show` re-fetch SHA-256. No BCB source re-fetch occurred during archiving.
- The archive contains `BalPagM.xlsx`, one workbook member, 2,875,732 bytes, internal date 2019-03-22.
