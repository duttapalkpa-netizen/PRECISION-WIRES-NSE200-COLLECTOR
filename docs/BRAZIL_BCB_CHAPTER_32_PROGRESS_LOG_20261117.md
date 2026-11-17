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
