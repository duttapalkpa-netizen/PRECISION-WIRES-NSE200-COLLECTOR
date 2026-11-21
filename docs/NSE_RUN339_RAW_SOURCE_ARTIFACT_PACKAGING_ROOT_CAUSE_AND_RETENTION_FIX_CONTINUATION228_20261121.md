# NSE Run #339 Raw-Source Artifact Packaging Root Cause & Retention Fix — Continuation 228
Date: 2026-11-21 (Asia/Kolkata)
Status: historical raw recovery BLOCKED; artifact allowlist correction committed; future-run validation PENDING.

## 1. Preflight and task selection
- Re-fetched Master Continuity Ledger, GCR Priority Queue and Historical Task Registry; reviewed the current Nightly Rotation Backtest review and immutable lesson `PW-LSN-20261121-003`.
- Excluded completed GCR C227 and all prior PASS work. CHN SAFE XLSX route is already marked duplicate/blocked and was not retried.
- Selected the unresolved Run #339 raw-source provenance gap because it affects whether daily candidate prices, delivery and security-master identity can be independently audited.

## 2. Direct evidence inspected
### Run #339 / prospective artifact
- Workflow run: `44799560798`; job: `136507856112`; source commit: `624be8f126f39bd6a146d732ec3f87edde964aec`.
- Artifact: `14660032260`, `prospective-watchlist-audit`, 50,543 bytes, GitHub digest and independently recomputed ZIP SHA-256:
  `23e74e7f9ef2e32bf5b6bbc5a931814c06fe065835b8bdda74f3c00dbdafd213`.
- ZIP integrity verified. It contains 17 entries / 254,360 uncompressed bytes. It contains no `sec_bhavdata_full_*.csv`, no `sessions.txt`, no `acquisition_diagnostics.json`, no `security_master.csv`, and no raw-source manifest.
- Job log records 200 successful `FULL_DELIVERY` responses and ends at `OK_FULL_BHAVCOPY_DELIVERY (200/200)`; QA reports `raw_files: 200`. This proves the files existed in the runner workspace during acquisition/QA, not that they were retained in the artifact.

### Independent comparison artifact
- Run #416: `44744602064`; artifact `14632139339`; ZIP size 61,990,061 bytes; SHA-256 `b12ea634f24af8241ee9a901635dd743195f4b8a3a1511cc2ffe3c3246282082`.
- ZIP integrity verified; 25 entries / 235,380,936 uncompressed bytes. It contains the normalized 200-session dataset `data/processed/nse_eq_200_sessions.csv` and `data/reference/security_master.csv`, but no original `sec_bhavdata_full_*.csv` raw files, no raw acquisition manifest and no delivery source payload archive.
- The repository tree contains only `data/raw/.gitkeep` as a tracked raw-directory file; no historical Run #339 raw archive is committed in the repository.

## 3. Root cause — now directly supported
- Run #339 workflow code checks/uses `data/raw/sec_bhavdata_full_*.csv`; `collector/nse_download.py` writes full bhavcopy + security deliverable files into `data/raw`.
- The workflow's `actions/upload-artifact` allowlist included selected QA, prospective, quarterly, news and macro outputs, but omitted the NSE raw CSV glob, `data/raw/sessions.txt`, `data/raw/acquisition_diagnostics.json` and `data/reference/security_master.csv`.
- Therefore the acquisition and QA step succeeded, but the artifact packaging allowlist excluded the NSE source files. This is stronger than the earlier generic packaging hypothesis: the exact allowlist omission is verified. It does not prove whether any ephemeral runner copy survives elsewhere after job completion.

## 4. Corrective change committed (isolated audit branch)
- Updated `.github/workflows/prospective_watchlist_tracking.yml` on branch `audit/prospective-selector-tracking` only.
- Added the following artifact paths:
  - `data/raw/sec_bhavdata_full_*.csv`
  - `data/raw/sessions.txt`
  - `data/raw/acquisition_diagnostics.json`
  - `data/reference/security_master.csv`
- Commit: `46f4a359f21da676cb0c92e874fb08f14ee20d90`.
- No main/production workflow, production selector, ranking, thresholds, gates or CORE-672 files were changed. No paid sources or new data downloads were initiated by this correction.

## 5. Acceptance and remaining blockers
| Check | Result |
|---|---|
| Run #339 artifact ZIP integrity and inventory | PASS |
| Run #339 acquired 200 raw daily files in runner workspace | PASS (log + QA evidence) |
| Historical raw files present in retained Run #339 artifact | FAIL / NOT_RETAINED |
| Exact artifact allowlist omission identified | PASS |
| Future artifact allowlist corrected on isolated audit branch | PASS (commit read-back required) |
| Future workflow artifact proves raw-file retention | PENDING; requires next bounded run |
| Per-file immutable raw manifest with URL, retrieval timestamp, byte count and SHA-256 | NOT_DONE |
| Recovery of old Run #339 raw bytes | BLOCKED; not present in either inspected artifact or tracked repository tree |

- Do not redownload the old 200 sessions and call them the original Run #339 bytes. Do not infer exact successful URL from the two candidate URLs in the downloader; Run #339 log line records status/bytes but not the selected URL.
- The correction retains original source CSVs on future workflow artifacts; it does not yet create the required per-file provenance manifest. A future manifest must record actual successful URL, UTC retrieval timestamp, HTTP status/content type, byte count and SHA-256 at acquisition time; cached files must retain unknown retrieval metadata rather than fabricate it.
- Historical Run #339 raw recovery remains BLOCKED; the 19-Nov/20-Nov shadow cohort remains NOT VALIDATED for independent raw-source provenance.

## 6. Protected invariants
Research-only audit branch; no production integration, selector/ranking/weight/gate changes, no synthetic data, no fabricated timestamps, no paid APIs. ₹0. UNKNOWN never PASS.
