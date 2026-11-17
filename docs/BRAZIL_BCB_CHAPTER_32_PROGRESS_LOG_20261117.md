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


## 11. 2026-11-17 — Instrument-level child metadata, raw capture and archive
- Official BCB BPM6 theme hierarchy and eight individual dataset pages verified: 22909 assets/equities net; 22912 assets/investment-funds net; 22915 assets/debt net; 22927 liabilities/equities net; 22936 liabilities/investment-funds net; 22939 liabilities/debt net; 22942 liabilities/debt domestic-market net; 22945 liabilities/debt external-market net.
- All eight individual dataset pages report BCB/Dstat, monthly SGS, USD millions, start 1995-01-01, BPM6/financial-account/portfolio-investment hierarchy, and timeliness up to four weeks after the reference period. Metadata: 8/8 PASS.
- Instrument-level capture Run #1 / ID `44077406268`: SUCCESS; artifact ID `14326096168`; artifact ZIP SHA-256 `37dcb1d5f4ad2938741953a1b8aad0cea3030a34c4e83d565379f2dd43fa0090`.
- Eight raw child series each HTTP 200; SHA-256 and byte lengths verified against manifest; 381 unique ordered monthly observations per series, 1995-01 through 2026-09; no missing numeric values.
- Reconciliation against archived parent seven series, all 381 months: 22906 = 22909+22912+22915 (253 exact; all within ±0.1); 22924 = 22927+22936+22939 (266 exact; all within ±0.1); 22939 = 22942+22945 (295 exact; all within ±0.1). Maximum residual 0.1 USD million. These are rounding-consistent, not formal PASS; no rounding tolerance is approved.
- Added reproducible audit script `scripts/research/audit_bcb_instrument_net_sgs.py` (commit `539efaff548f33780b28a7c041d4aa4123481018`), machine-readable QA record `data/qa/BRAZIL_BCB_INSTRUMENT_NET_QA_20261117.json` (commit `a536e3ea6c475d1fe03405fd071050ed434f972a`), and results doc (commit `4418653074ecd39e72da1187bb8c3a4d2a53b5d4`).
- Permanent archive workflow Run #1 / ID `44077573395`: SUCCESS; archive commit `527a8d41c434609c980eb3181d491eac4fa6e822`; durable path `data/raw/bcb/instrument_net_capture_20261117/`; post-commit Git-blob re-fetch and SHA-256 PASS for all eight.
- Instrument hierarchy coverage is now metadata-verified and raw-archived. Country-period QA remains NOT_DONE; Brazil pilot remains NOT_ACCEPTED; EM-wide panel remains NOT_DONE; production integration remains NOT_AUTHORIZED.


## 12. 2026-11-17 — Official September-2026 country-period cross-check PASS
- BCB official 26-Oct-2026 release reports domestic portfolio net outflows of USD 2.1bn in Sep-2026: equity/funds domestic-market outflows USD 1.7bn; domestic debt-security outflows USD 0.4bn.
- Added exact domestic equity SGS 22930 metadata verification (BCB/Dstat, monthly, USD million, start 1995-01, BPM6 / portfolio liabilities / equities / domestic market).
- Workflow Run #1 / ID `44077864021`: SUCCESS. Captured only missing series 22930; reused already archived 22936 and 22942 (no re-fetch of those series).
- 22930 raw CSV: HTTP 200, 8,669 bytes, SHA-256 `c4730c84ee81765a1c5ae41d91c1ea6f153bcb51ac70ee14b45b453b4dcab776`.
- Input Sep-2026 values (USD mn): 22930=-2,110.8; 22936=+416.8; 22942=-382.4.
- Derived equity+funds net outflow = USD 1.694bn → rounds to 1.7bn; domestic debt net outflow = USD 0.3824bn → 0.4bn; total = USD 2.0764bn → 2.1bn. All three match BCB's published release at its stated USD 0.1bn precision.
- Country-period QA: PASS for the September-2026 release comparison only.
- Raw CSV, manifest and crosscheck report committed at `bcb_domestic_market_crosscheck_202609/`; permanent commit `446971a0da670d69e6dcb2c9efe0208ea50db572`; commit push plus post-commit SHA-256 re-fetch PASS.
- This is a one-period validation, not full-history country-period acceptance. Brazil pilot remains NOT_ACCEPTED pending full instrument/perimeter and revision gates; EM-wide panel and production integration remain NOT_DONE / NOT_AUTHORIZED.

## 13. 2026-11-17 — Multi-period domestic portfolio country reconciliation
- Reused committed raw CSVs; no BCB re-download and no repeated September-only audit.
- Sources: SGS 22930 blob f7626bbc6b62630b6518451c472f718de3370175; SGS 22936 blob 3865fe689081cea11dff15227d01da4bb75925e0; SGS 22942 blob 3da8dc2b03da91e0dc9ff0861024c1ff17cce400. Raw SHA-256 values are checked by the reproducible audit script.
- Compared latest-vintage SGS 22930+22936 (equity/funds), 22942 (domestic debt), and their sum against BCB monthly press release values for nine reference months: Dec-2025; Jan, Feb, Mar, Apr, Jun, Jul, Aug and Sep-2026.
- 7/9 months match all three published measures at the releases' one-decimal USD-billion precision; 23/27 individual comparisons match.
- Unresolved vintage exceptions: Dec-2025 current SGS equity/funds -1.1bn vs release -1.4bn and total +4.2bn vs +3.9bn; Feb-2026 current SGS debt +2.8bn vs release +2.6bn and total +5.6bn vs +5.4bn. Other component in each month matches. These are classified VINTAGE_DIFFERENCE_UNRESOLVED, not source errors.
- BCB's September-2026 release says 2025 statistics became definitive and 2026 estimates were revised. This is consistent with, but does not prove, the cause of the two observed differences. Same-vintage bridge and exact revision attribution remain NOT_DONE.
- Report: docs/BRAZIL_BCB_MULTI_PERIOD_COUNTRY_RECONCILIATION_20261117.md. Machine-readable QA: data/qa/BRAZIL_BCB_MULTI_PERIOD_COUNTRY_RECONCILIATION_20261117.json.
- Reproducible audit script: scripts/research/audit_bcb_multi_period_country_reconciliation.py. Bounded workflow: .github/workflows/bcb_multi_period_country_reconciliation.yml; 5-minute timeout; raw SHA checks; no source re-fetch.
- Workflow run #1 / ID 44086204426 was queued on commit ed7c695c33c4739b9dd5acebf663f08469b2cb15; runtime result pending at log update.
- Acceptance: nine-period comparison implemented and independently calculated; overall multi-period country validation PARTIAL; Brazil pilot NOT_ACCEPTED; EM-wide panel NOT_DONE; production integration NOT_AUTHORIZED.
- Next action: verify the bounded CI result; then resolve only Dec-2025 and Feb-2026 using exact same-vintage BCB tables/archives and the September-2026 revision bridge. Do not repeat raw capture or September-only validation.
- Invariants preserved: ₹0; official sources only; no synthetic data or invented hashes/timestamps; no production selector, ranking, +1 pressure fade, CORE-672, Engines A–E, Hard Gate, seed or production workflow changes.

## 14. 2026-11-17 — Bounded reconciliation CI runtime PASS
- Workflow Run #1 / ID 44086204426; head `ed7c695c33c4739b9dd5acebf663f08469b2cb15`; conclusion SUCCESS.
- Job `reconcile` SUCCESS; the raw SHA-256 verification and nine-period reproducibility step completed SUCCESS.
- Runtime re-confirmed all three raw source SHA-256 values; 9 months checked; 7 complete months; 23/27 component/total comparisons matched. The two vintage-sensitive exceptions are preserved, not hidden.
- Artifact ID 14328529268; name `bcb-multi-period-country-reconciliation`; archive digest `c65447a53ba44c44c85a0239776bb9af08c454bdc6e9046c98700492806dc647`; expires 2027-02-15T12:45:57Z.
- Run URL: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/44086204426
- Bounded CI runtime: PASS. Country-period multi-vintage reconciliation remains PARTIAL; Brazil pilot NOT_ACCEPTED; exact Dec-2025 and Feb-2026 revision attribution NOT_DONE.

## 15. 2026-11-17 — Exact-value reproducibility hardening CI PASS
- Updated the research-only audit script to emit exact current SGS values in USD million for every checked month, while retaining the release-rounded comparison.
- Re-run #2 / ID 44086387367 on script commit `b3d5bf9b29e1c730a7f9d60a510277b64d181f48`: SUCCESS; job `reconcile` and raw SHA-256/reproduction step SUCCESS.
- Runtime verified exact exception values: Dec-2025 equity/funds -1082.9, domestic debt +5321.6, total +4238.7 USD million; Feb-2026 equity/funds +2786.2, domestic debt +2783.2, total +5569.4 USD million.
- Summary unchanged: 9 months; 7 complete matches; 23/27 comparisons match; two vintage exceptions remain unresolved.
- Artifact ID 14329222273; SHA-256 `fc6d34e8856db75ca0eb22a254bafdc395e0a77d783f7149ffb89474ce379138`; expiry 2027-02-15T12:47:07Z.
- Run URL: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/44086387367
- No raw-source re-download, production change, or general tolerance introduced.

## 15. 2026-11-17 — Official hierarchy correction and scope qualification
- Re-opened the exact official BCB topic catalogue after the screenshot raised a possible 22942 short-term classification conflict.
- The catalogue explicitly shows 22942–22944 = domestic-market debt-security liabilities (net/inflow/outflow), 22945–22947 = foreign-market debt-security liabilities, 22948–22950 = foreign-market short-term debt, and 22951–22953 = foreign-market long-term debt.
- Therefore the screenshot's short-term concern is not correct for SGS 22942. The prior hierarchy map had a row-offset/mapping error; corrected it in docs/BRAZIL_BCB_PORTFOLIO_INVESTMENT_HIERARCHY_MAP_20261117.md. The existing 22942 raw archive is the correct domestic-market debt net series; no raw observations changed.
- BCB catalogue lists 22930 as domestic-market equity liabilities, but lists 22936 only as investment-fund liabilities without a domestic/foreign-market qualifier. This leaves the release-to-22936 fund-share perimeter UNKNOWN.
- Reproducible script updated to report the scope qualification explicitly and prevent interpreting the 23/27 numeric matches as full country-perimeter PASS. 22942 debt comparison scope confirmed (8/9 numerical matches; Feb-2026 differs); 22936 fund market perimeter unknown; overall equity/funds and total domestic-market validation PARTIAL / NOT_ACCEPTED.
- Report and QA JSON superseded with the correction; source URLs are recorded in the report. No raw data re-download or overwrite.
- Next actions: (1) verify updated CI after script change; (2) obtain an authoritative BCB definition of 22936 market perimeter; (3) obtain same-vintage official release tables/archive for Dec-2025 and Feb-2026 and resolve their debt/equity/fund differences. Do not claim revision causation until supported.
- Status: hierarchy 22942/22945 corrected PASS; 22936 perimeter UNKNOWN; numerical reproduction pending updated CI; Brazil pilot NOT_ACCEPTED; EM panel NOT_DONE; production integration NOT_AUTHORIZED.
- Invariants preserved: ₹0; official free sources; no synthetic data; no raw changes; no production selector, score, pressure fade, CORE-672, engines, hard gate, parser admission or seed changes.

## 16. 2026-11-17 — Scope-aware reconciliation CI PASS; matched-vintage table capture queued
- Updated reconciliation script CI Run #3 / ID 44089780668: SUCCESS; commit 6e10775e5ea3a3902519d8edb75fabfb45ef71c8. Runtime verified the same three raw SHA-256 values and explicit scope flags: 22942 domestic-market debt; 22930 domestic-market equity; 22936 fund liabilities without explicit market qualifier in catalogue.
- Updated result: 9 periods; 7 complete numeric matches; 23/27 numeric comparisons; debt comparison scope confirmed 8/9; fund market perimeter UNKNOWN. This is a reproducibility PASS, not country-perimeter acceptance.
- Artifact ID 14330248320; digest sha256:4b46d50d369370b5eb7806e5f61a95af1802220bb0ccb099804040d09e2a2fa3; expiry 2027-02-15T13:08:37Z.
- Run URL: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/44089780668
- New bounded official BCB historical release table capture workflow committed: .github/workflows/bcb_release_tables_vintage_capture.yml; commit 9329767f79814bf61afad1bb9e311429e228dff1. It targets Jan-2026 publication tables (Dec-2025 reference) and Mar-2026 publication tables (Feb-2026 reference), preserving raw XLSX, HTTP headers, byte lengths, SHA-256 and sheet names. Run ID 44089945873 queued; runtime result pending.
- Next: verify capture; inspect the exact BCB workbook cells for the two vintage exceptions and the 22936 market perimeter; only then decide whether a revision bridge can be proved.

## 17. 2026-11-17 — Exact Table 10 component crosswalk and vintage differences
- Captured official BCB historical Table 10 workbooks for publication periods 202601, 202603 and 202610, including HTTP response headers, ETags, bytes and SHA-256.
- Capture Run #2 ID 44090062072 SUCCESS (202601/202603); Run #3 ID 44090618010 SUCCESS (added 202610).
- Official Table 10 component mapping verified:
  - SGS 22930 = domestic-market equity, Table 10 row 14.
  - SGS 22936 = investment-fund liabilities, Table 10 row 20. Footnote 1 says the nonresident quota holder owns <10% of the net asset value of the investment fund in Brazil; row 41 combines equity and funds and row 40 is domestic-market portfolio total. This supports the domestic-fund scope mapping.
  - SGS 22942 = domestic-market debt securities, Table 10 row 24. Correct official topic catalogue mapping; not short-term-only.
- Table 10 accounting identities passed for all three files/periods: row14+row20=row41; row24=row42; row41+row42=row40.
- 2026-09 current Table 10 vs latest SGS: 22930 -2110.79771091 vs -2110.8; 22936 +416.80852785 vs +416.8; 22942 -382.35384003 vs -382.4; all within USD 0.1 million. This validates the current crosswalk and parser.
- Current archived SGS minus Table 10 historical values (USD mn):
  - Dec-2025: 22930 +116.1748; 22936 +211.6830; 22942 +39.3771; equity/funds +327.8578; domestic total +367.2349.
  - Feb-2026: 22930 -0.0374; 22936 +0.0395; 22942 +203.7078; equity/funds +0.0020; domestic total +203.7098.
- The contemporaneous Jan-2026 PDF release reports Dec-2025 equity/funds -1.4bn, debt +5.3bn, total +3.9bn. The contemporaneous Mar-2026 PDF release reports Feb-2026 equity/funds +2.8bn, debt +2.6bn, total +5.4bn. Latest SGS rounds to Dec-2025 -1.1/+5.3/+4.2 and Feb-2026 +2.8/+2.8/+5.6. Differences are confirmed at published 0.1bn precision.
- Critical caveat: the period-indexed XLSX files 202601 and 202603 were served with HTTP Last-Modified 19-Oct-2026 and 18-Oct-2026. They are official historical tables as served 2026-11-17, but are not proven immutable original publication-vintage snapshots. Contemporaneous PDFs preserve only rounded values. Specific revision cause/date remains UNKNOWN.
- Exact extraction file: data/qa/BCB_DOMESTIC_PORTFOLIO_RELEASE_VINTAGE_EXTRACT_20261117.json. Raw workbook manifest: data/raw/bcb/BCB_HISTORICAL_RELEASE_TABLES_VINTAGE_MANIFEST_20261117.json. Reproducer: scripts/research/extract_bcb_domestic_portfolio_release_vintage.py.
- Extraction Run #4 ID 44090856672 SUCCESS; commit 6b8cfc3daf489a04bd22db882343dc58342318b5; artifact 14330724185; digest 9c6c2c2733c75a2b098c4180d556bf5208cd6cea06dccf85a86f32d86f42e8f1.
- Status: series crosswalk PASS; latest Sep-2026 component validation PASS; Dec-2025 and Feb-2026 vintage differences CONFIRMED; exact original-vintage file proof UNKNOWN; revision attribution NOT_DONE; Brazil pilot NOT_ACCEPTED; EM panel NOT_DONE; production integration NOT_AUTHORIZED.
- Next: seek a documented BCB revision notice or immutable as-of-publication values for Dec-2025 and Feb-2026 only. Do not re-download existing raw SGS or repeat Sep-2026 validation.
- Invariants preserved: ₹0; official free sources; no synthetic values; no raw source overwrite; no Production Selector/RANKING_SCORE/+1 PRESSURE_FADE/CORE-672/Engines A–E/Hard Gate/seed/parser/production changes.

## 18. 2026-11-17 — BCB 2025 annual revision bridge confirmed
- Archived official BCB September-28-2026 External Sector Statistics release PDF: 852,292 bytes; SHA-256 2120db15085716f0c2a76270149cfbd2b40e8b9d57eb69d611b05bae8e72625e; HTTP 200; Last-Modified 05-Oct-2026.
- BCB explicitly states 2025 net portfolio-investment liabilities revised from USD 15.1bn to USD 17.6bn; direct/portfolio reclassifications follow the 10% nonresident ownership criterion. September revision cycle covers definitive 2025 and revised 2026 estimates.
- Current archived SGS 22924 12-month sum for 2025 = USD 17,569.2m, rounds to BCB revised USD 17.6bn. January-2026 Table 10 prior total = USD 15,139.9821m. Latest minus prior = +USD 2,429.2179m. Annual parent-level revision bridge PASS at published precision.
- Annual component comparison (latest SGS minus Jan-2026 Table 10, USD mn): 22930 +116.1254; 22936 +1,931.1145; 22942 +239.5814; domestic-market total +2,286.8213. Fund-liability component has the largest annual movement, consistent with BCB's stated direct/portfolio reclassification mechanism; exact monthly allocation is not established.
- December-2025 month-specific component deltas remain as previously measured; do not claim all are directly attributable to the 10% reclassification.
- February-2026 22942 debt discrepancy remains USD +203.7078m vs the March-2026 Table 10 value. BCB says 2026 estimates were revised but does not identify this specific series/month cause. Attribution UNKNOWN.
- Script: scripts/research/audit_bcb_2025_annual_revision_bridge.py; output: data/qa/BRAZIL_BCB_2025_ANNUAL_REVISION_BRIDGE_20261117.json; PDF archive: data/raw/bcb/revision_release_202609/.
- Run #1 ID 44091390515 SUCCESS; artifact 14330869727; digest 15d99f469b7cb9d461c47125dc9d1dec513e2edaa3deb744b7900c92e0ada971.
- Status: 2025 annual revision bridge PASS; Dec-2025 monthly attribution PARTIAL/NOT_ATTRIBUTED; Feb-2026 debt attribution UNKNOWN; Brazil pilot NOT_ACCEPTED; EM panel NOT_DONE; production integration NOT_AUTHORIZED.
- Next: investigate only Feb-2026 22942 debt and month-specific 2025 revision allocation through official revision history or preserved SGS vintages. No repeat source capture or Sep-2026 check.

## 19. 2026-11-17 — Feb-2026 22942 debt discrepancy isolated to February
- Used March-2026 Table 10 Jan-Feb cumulative row values minus February monthly row values to infer January 2026, then compared with current SGS January raw observations.
- January component deltas (latest SGS minus BCB-implied, USD mn): 22930 -0.0371; 22936 -0.0035; 22942 -0.0408; equity/funds -0.0407; domestic total -0.0814. All match within USD 0.1m.
- February 2026: 22930 -0.0374; 22936 +0.0395; 22942 +203.7078; equity/funds +0.0020; domestic total +203.7098. Thus the Jan-Feb cumulative debt difference is isolated to February 22942, not January carry-over or equity/fund mismatch.
- Exact inferred January values and Jan-Feb cumulative identities are now included in data/qa/BCB_DOMESTIC_PORTFOLIO_RELEASE_VINTAGE_EXTRACT_20261117.json; all inferred January Table 10 identities PASS.
- Updated extraction Run #5 / ID 44091831003 SUCCESS; artifact ID 14332500865; digest ee222deb9a1eabe10b0357ab1b1907f7696b764f5dfcfa2924166cb809f0cbfd.
- Status: January 2026 component comparison CLOSED (within 0.1m); February 2026 22942 debt discrepancy isolated, exact revision cause UNKNOWN; 2025 annual revision bridge PASS; Brazil pilot NOT_ACCEPTED; EM panel NOT_DONE; production integration NOT_AUTHORIZED.
- Next: investigate only February-2026 22942 revision using official BCB revision notice or preserved historical SGS vintage. Do not repeat January or September checks.
