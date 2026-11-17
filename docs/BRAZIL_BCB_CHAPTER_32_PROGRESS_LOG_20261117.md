# PRECISION-WIRES V11.3 — Chapter 32 Brazil BCB Continuity Log
Date: 2026-11-17 (Asia/Kolkata)
Workstream: Global Capital Rotation & Relative-Attraction Overlay
Task: Brazil BCB Portfolio Investment — Seven Priority SGS Raw Observation Capture + SHA-256
Branch: `research/bcb-priority-metadata-audit-20261117`
Prior metadata audit commit: `d3470dc4f886e3d86923214377e2b482287cbec3`
Current branch head after this work: `9813ec5b884712461aa59ec9664e66915e7bf94b`

## 1. Prior work reused; not repeated
- Official BCB portfolio-investment hierarchy map already completed: `docs/BRAZIL_BCB_PORTFOLIO_INVESTMENT_HIERARCHY_MAP_20261117.md`.
- Seven-series metadata audit already completed: `docs/BRAZIL_BCB_PRIORITY_SERIES_METADATA_AUDIT_20261117.md`.
- Exact identities, organization BCB/Depec, monthly periodicity, USD-million unit, and 1995-01-01 coverage already qualified for SGS 22905, 22906, 22907, 22908, 22924, 22925 and 22926.
- Existing SGS 22907/22926 pilot discovery and prior 22906/22907/22908 crosswalk are reused; no repeated endpoint discovery.
- Official BCB portal CSV resource links inspected. Direct Download links for 22905 and 22924 resolved to the BCData/SGS CSV URL pattern. The other five official dataset pages expose their corresponding code-specific CSV resources.
- Web retrieval rejected CSV bodies with unsupported text/csv content type. This is a reader limitation; it is not proof that BCB endpoints are invalid and not a raw-byte capture.

## 2. New work completed in this session
- Added `scripts/research/capture_bcb_priority_sgs_csv.py`: allow-listed seven-series byte capture; per-series retry; HTTP response headers/status; request/final URL; UTC retrieval start/end; content type; byte length; SHA-256; UTF-8 sanity check; delimiter sniff; per-series PASS/BLOCKED manifest; partial-failure preservation; no sign transformation or arithmetic.
- Added `.github/workflows/bcb_priority_sgs_raw_capture.yml`: manual dispatch and path-filtered push trigger; 8-minute job timeout; Python syntax check; bounded capture; artifact upload with `if: always()`; 90-day retention.
- Added `docs/BRAZIL_BCB_SEVEN_PRIORITY_SGS_RAW_CAPTURE_20261117.md`: capture contract, seven series and acceptance gates.
- Added a syntax-check step before download to fail early on malformed script while still retaining failure artifact evidence.
- Script bug found during fetch-back inspection: JS-generated source initially wrote a literal escaped newline into the manifest and used an incorrectly escaped tab delimiter. Corrected to `chr(10)` and `chr(9)`; re-fetched and verified the corrected blob.
- No production files, registry, parser admission rules, seed observations, Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A–E, Hard Gate or collector workflow changed.

## 3. New commits
- Initial capture script: `c208a73efa0110873918981535a834d80219e858`.
- Initial workflow: `4f4999332dd1131403e757b255abf0565a75d44f`.
- Capture contract doc: `50a0ecbe8bd953bcb4892d2fe20b51b505ea5f96`.
- Script newline/delimiter correction: `eaaa1291170c6c7a6c87cfc15d86a679983755b0`.
- Workflow syntax-check hardening: `9813ec5b884712461aa59ec9664e66915e7bf94b`.
- Script final blob SHA: `fb2c9d4de1d85a94e6bd46423cd2acfb9a69ef1a`.
- Workflow final blob SHA: `306de5e7544bdbf14967142f36e5d6581b418a83`.
- Capture documentation final blob SHA: `e59e5877994e3429a6dddcf3424f7527fcdea4f0`.

## 4. Current status — do not overstate
| Work item | Progress | Evidence status |
|---|---:|---|
| Official hierarchy mapping | 100% | PASS |
| Seven-series identity/unit/frequency/coverage metadata | 100% | PASS |
| Raw-capture script and workflow implementation | 100% | IMPLEMENTED |
| Script/workflow fetch-back review | 100% | PASS |
| GitHub Actions runtime | 0% verified | UNKNOWN / NOT_CHECKED |
| Seven raw CSV bytes | 0% | NOT_DONE |
| HTTP metadata + byte lengths + SHA-256 manifest | 0% | NOT_DONE |
| Date-level parsing / duplicate / missing-period QA | 0% | NOT_RUN |
| Accounting sign and net/component reconciliation | 0% | UNKNOWN / NOT_DONE |
| Country-period QA | 0% | NOT_DONE |
| Brazil pilot acceptance | — | BLOCKED / NOT_ACCEPTED |
| EM-wide panel | 0% | NOT_DONE |
| Production integration | — | NOT_AUTHORIZED |

## 5. Next exact action
1. Check GitHub Actions for the push-triggered workflow run on this branch.
2. If no run exists, manually dispatch `Brazil BCB Seven Priority SGS Raw Capture` once.
3. Inspect the artifact even if the job fails. Verify all seven CSV raw files, manifest completeness, response headers, status, byte length and recomputed SHA-256.
4. Only after raw capture succeeds, create a separate parser/QA stage based on the actual observed CSV delimiter, headers, decimal notation, date format and value encoding.
5. Separately retrieve the official BCB Balance of Payments methodological note and reconcile signs/perimeter before any net/component identity or combined flow calculation.

## 6. Accounting and safety boundaries
- Keep 22905 total net, 22906 asset net, 22907/22908 asset components, and 22924/22925/22926 liability net/components distinct.
- Do not assume inflows minus outflows equals a net series until the official sign convention and perimeter are established.
- Do not infer Brazilian equity-only foreign portfolio flow from the broad portfolio aggregate.
- Do not confuse BOP transaction flows with IIP/CPIS positions.
- No synthetic observations, forward-fill, guessed values, timestamps, signs, or hashes.
- ₹0 spend; free official BCB sources only.
- No production integration or PR merge without explicit authorization.


## 7. 2026-11-17 — Raw capture runtime PASS and independent artifact inspection
- GitHub Actions Run #3 / ID `44075768714`, head `9813ec5b884712461aa59ec9664e66915e7bf94b`: completed SUCCESS.
- Artifact ID `14324188933`; archive SHA-256 `40a1ff44317b16ffb789b4669496628a048a94010113d55cd40161d6570ee6c8`; artifact contains manifest plus all seven CSV files.
- Independently downloaded artifact and recomputed archive SHA-256; exact match. Independently recomputed each of seven raw CSV SHA-256 values and byte lengths; all seven matched manifest.
- All seven HTTP responses 200; content type `text/csv; charset=utf-8`.
- CSV schema observed: UTF-8, header `data;valor`, semicolon delimiter, date `DD/MM/YYYY`, decimal comma.
- Each series has exactly 381 rows, 1995-01-01 through 2026-09-01; all date sequences unique, strictly increasing, contiguous monthly and aligned; no missing numeric values.
- Deterministic audit script added: `scripts/research/audit_bcb_priority_sgs_csv.py`; commit `3351e3818a573ad9ce96e4d92aca7a4b460c8244`.
- QA results note commit `51c157fe6307eb5946cea2763fc18db3b1af8cc0`; machine-readable QA summary commit `f93228ce7f007f046ce5436e9f14ac29160b52ea`.
- Three candidate net/component identities tested over all 381 months: 22906 = 22908 − 22907 (275 exact; all 381 within ±0.1); 22924 = 22925 − 22926 (283 exact; all 381 within ±0.1); 22905 = 22906 − 22924 (285 exact; all 381 within ±0.1). Maximum absolute difference for each is 0.1 USD million.
- BCB official methodology note supports asset net = acquisitions less disposals, liability net = issuance less repayment, and financial-account balance = net financial assets less net financial liabilities. The data are empirically consistent with the candidate sign orientation. However, one-decimal CSV display precision and no formally approved tolerance mean these identities are ROUNDING-CONSISTENT, not final PASS.
- Official series-specific receipt/expense sign/perimeter mapping and tolerance approval remain pending. Do not modify source values to force exact identities.
- Raw capture + manifest hashes: PASS. Structural monthly QA: PASS. Accounting sign reconciliation: PARTIAL_EMPIRICAL_ALIGNMENT. Country-period QA: NOT_DONE. Brazil pilot: NOT_ACCEPTED. EM-wide panel: NOT_DONE. Trusted observation admission / production integration: NOT_AUTHORIZED.
- Raw artifact retention is 90 days. Permanent raw-byte repository archive is still NOT_DONE; do not claim permanent archival until a committed archive can be fetched back and re-hashed.

## 8. Next action
1. Resolve the 0.1 USD-million residuals using source precision/revision semantics, without applying an invented tolerance. Consider a separately captured official JSON resource only as a precision/schema cross-check; do not overwrite CSV raw bytes.
2. Obtain the exact BPM6/BCB series-specific methodological statement for the Portuguese `receita/despesa` definitions and verify the perimeter for 22905–22926.
3. Complete a separate country-period cross-check against a BCB official release/table where the perimeter is explicit; document that aggregate press-release series may not equal the SGS series.
4. Commit the raw ZIP archive permanently only after verifying the repository binary-archive upload and re-fetch SHA-256; meanwhile artifact ID 14324188933 is the 90-day raw evidence source.
5. Keep Brazil pilot acceptance blocked until the above gates pass; then proceed to the instrument-level equity/fund/debt split and only later EM-wide panel.


## 9. 2026-11-17 — Permanent raw-byte archive PASS
- Added `.github/workflows/archive_bcb_priority_sgs_artifact.yml`; workflow downloads the exact already successful Run #3 artifact ID 14324188933, does not re-fetch BCB source data, validates manifest byte lengths and SHA-256, commits original CSVs with `*.csv -text`, then re-fetches committed Git blobs and recomputes SHA-256.
- Archive workflow Run #1 / ID `44076318974`: SUCCESS.
- Permanent archive commit: `73bf04f6333fd90d8c0d24c7ba9e71eb1ba3f568`.
- Durable path: `data/raw/bcb/priority_series_capture_20261117/`.
- Confirmed tree entries: `.gitattributes`, `manifest.json`, and `sgs_22905.csv`, `sgs_22906.csv`, `sgs_22907.csv`, `sgs_22908.csv`, `sgs_22924.csv`, `sgs_22925.csv`, `sgs_22926.csv`.
- Re-fetch SHA-256 validation: PASS 7/7 after commit. Original CRLF bytes preserved via `.gitattributes`.
- This closes the permanent raw CSV archive gate. The Actions artifact is still useful provenance but no longer the only copy.


## 10. 2026-11-17 — Independent official BCB BPM6 historical vintage audit
- Captured official monthly BOP history ZIP from BCB: `https://www.bcb.gov.br/ftp/notaecon/balpagm.zip`.
- Capture Run #1 / ID `44076495816`: SUCCESS; artifact ID `14324932604`; outer artifact SHA-256 `1da1dda4398abc2d3f93255bc47e1595f75a778731d5ae80241e3852ac1a0c4c`.
- Inner ZIP: 2,813,472 bytes; SHA-256 `e58d64374d13ae62fb2af95e4bd26acaf924f0da113a825842307c95219dec4b`; HTTP 200; ZIP CRC PASS. One member: `BalPagM.xlsx`, 2,875,732 bytes, internal date 2019-03-22.
- Workbook `Balanço` explicitly labels itself “Balanço de pagamentos – BPM6”; its available monthly span is Jan-1995 to Feb-2019 (290 months). It is a 2019 vintage, not a current 2026 dataset.
- Exact SGS mapping verified from workbook code column: row 220=22905; 221=22906; 222=22907; 223=22908; 241=22924; 242=22925; 243=22926.
- All three accounting identities hold across 290 months in the 2019 workbook to floating-point residuals no larger than approximately 1e-11: 22906=22908−22907; 22924=22925−22926; 22905=22906−22924.
- Current 2026 SGS CSV vs 2019 workbook (same 290 dates) is not fully identical: 22907 290/290 within ±0.05; 22908 288/290; 22906 287/290 (one half-step/floating edge and Jan/Feb 2019 revisions); 22905 245/290; 22924 245/290; 22925 246/290; 22926 247/290. The 22905/22924/22925/22926 differences begin in 2015 and indicate vintage differences; reason not yet established. Do not treat old-vintage mismatches as source errors or replace current values.
- Historical archive workflow Run #1 / ID `44077157516`: SUCCESS; permanent archive commit `88eebada24c1619d82292bb757df64e4372851ad`; path `data/raw/bcb/monthly_bop_history_20190322/`; post-commit `git show` SHA-256 verification PASS.
- Result: conceptual sign orientation CONFIRMED; 2019-vintage identity PASS; current 2026 displayed-value identities remain rounding-consistent but formal tolerance is not approved; current-vintage vs 2019-vintage reconciliation PARTIAL.
