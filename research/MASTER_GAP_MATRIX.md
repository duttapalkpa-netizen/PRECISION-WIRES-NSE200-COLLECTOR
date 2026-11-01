# PRECISION-WIRES V11.3 — MASTER GAP MATRIX

**Snapshot date:** 2026-11-01  
**Repository:** `duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR`  
**Branch:** `fix/factor-registry-same-snapshot-reconcile`  
**Snapshot commit:** `54b90e592d7b67588febc34651c63862d154d1f2`  
**Purpose:** Preserve prior work, separate proven PASS from PARTIAL/BLOCKED/UNKNOWN, prevent duplicate work, and define the next evidence-backed action.

## 1. Non-negotiable controls

- Legal use only; no bypassing access controls, licence terms, or publisher restrictions.
- Research spend must remain **₹0**. No paid API/SFTP, subscription, licence, or paid dataset.
- No external contact, registration, account creation, API-key request, data sharing, or production change without the user's explicit prior approval.
- Production selector, `RANKING_SCORE`, frozen `+1 PRESSURE_FADE`, and the 672 diagnostics (56 × 12) remain unchanged.
- `UNKNOWN` is neither PASS nor FAIL. No synthetic rows, invented timestamps, or unsupported source promotion.
- Hard Gate stays `BLOCKED` until all required P0 coverage, data-quality, and matured event-study acceptance criteria are met.
- PR #13 remains Draft; do not merge as part of this audit.

## 2. Status definitions

| Status | Meaning |
|---|---|
| **PASS** | The exact acceptance test and its artifact were inspected and support the claim. |
| **PARTIAL** | Some implementation/data exists, but a material coverage, provenance, permission, or acceptance gap remains. |
| **BLOCKED** | A known dependency or failed acceptance check prevents progression. |
| **UNKNOWN** | Evidence is not available in this snapshot; do not infer success or failure. |
| **ARTIFACT_UNVERIFIED** | A workflow may have run, but the artifact has not been inspected against the acceptance criteria. |

A workflow conclusion of SUCCESS alone is not sufficient to promote a data source or close a research gate.

## 3. Master workstream matrix

| ID | Workstream / prior work | Evidence currently established | Status | Remaining gap / next acceptance condition |
|---|---|---|---|---|
| M01 | V11.3 architecture and 672 diagnostics | Architecture and 56 × 12 design are established in project history and repository. | **PASS — frozen design** | Regression proof must continue to show no changes to selector, `RANKING_SCORE`, `+1 PRESSURE_FADE`, or diagnostic count. |
| M02 | RBI DBIE monthly G-Sec yield adapter | Adapter QA Run `41314656919` PASS; 365 monthly observations, Apr-1996–Aug-2026, 30 tenors, 9,477 observations, no duplicate date/tenor keys; normalized CSV SHA-256 `772aca6e440ca1adba603b8c8d10f6da049111181035262d501813e181bd2e07`. | **PASS — monthly adapter QA** | Not a daily FBIL/FBIL-like series. Do not relabel as daily 10Y par yield. Factor use still subject to factor-registry source/frequency fit. |
| M03 | RBI DBIE same-snapshot Factor Registry audit | Run `41314900549` PASS; artifact ID `13085804606`; 35 factor groups, 31 partial, 4 disconnected; F14 remains partial and India bond-yield factor has data-quality warning. | **PARTIAL** | 4 disconnected groups and partial coverage remain. Re-run only after source repair; preserve same-snapshot rule. |
| M04 | FBIL official endpoint discovery | Official first-party routes identified: `/wasdm/gsec/fetch`, `/wasdm/gsec/fetchfiltered`, `/wasdm/gsec/downloadPublished`; read-only probing; no authentication bypass. | **PASS — endpoint discovery** | The live fetch endpoint returns archive metadata, not per-observation publication clock time. |
| M05 | FBIL historical archive backfill | Run #14 `41325197755` PASS. Inspected artifact ID `13089969056`: 236 XLSX archives downloaded, 236 parsed rows, 236 unique observation dates, 0 download errors, 0 parser errors, 0 quarantined files; date range 2025-11-03–2026-10-23. Normalized CSV SHA-256 `7dcd2b698cf2e92aa7f2ad515da5b4411a640509759ebdf554a34dc21e85908b`. | **PASS — archive collection & date/row parse only** | This is 236 archive observations, not proof that every date is a trading session. Publication timestamp coverage is 0%; do not infer 18:30 or another time. |
| M06 | FBIL release timestamp and permitted use | Parser deliberately leaves `PUBLISHED_AT_IST` and `RELEASED_AT_UTC` blank. FBIL written permission not obtained. | **BLOCKED — production eligibility** | Keep out of Production Factor Registry until publication-time provenance and lawful free internal-use rights are evidenced. Do not contact FBIL without fresh user approval. |
| M07 | FBIL latest workflow integrity gate | Run #13 `41324215737` failed due to an incorrect quarantine-count assertion. Corrected in commit `54b90e592d7b67588febc34651c63862d154d1f2`; Run #14 `41325197755` SUCCESS. Inspected artifact ID `13089969056`: 236 files, 236 rows, 236 unique dates, zero download errors, zero parser errors, zero quarantined files; timestamp coverage 0%; normalized CSV SHA-256 `7dcd2b698cf2e92aa7f2ad515da5b4411a640509759ebdf554a34dc21e85908b`. Legacy homepage HTML parser still has no historical Date+Time rows. | **PASS — archive integrity gate; still BLOCKED for production eligibility** | Verifier corrected in commit `54b90e592d7b67588febc34651c63862d154d1f2` to require zero mismatches and zero errors. A fresh workflow run and artifact review are still required. |
| M08 | NSE 200-session cache / manifest | NSE Benchmark Run #162 `41325197764` SUCCESS; artifact ID `13090719723`; 200/200 sessions, 200 valid cache hits, 0 misses, 0 network requests in warm-cache benchmark; elapsed 12.768868 sec (15.663 sessions/sec); manifest SHA-256 `d23b294d8b9a4b93f3aeab06778a01be4646f7071b549155953ea073383d7422`; snapshot ID `f90c01c1d7e228ab7282a96fef4dfb3ceca7f67675938926dac009f9cb92d72c`; dates 2026-01-07–2026-10-30. | **PARTIAL — 200-session count, manifest generation and warm-cache benchmark PASS; legacy provenance remains unresolved** | Manifest states legacy cached files lack original network URL and authoritative retrieval timestamp; mtime is only a local proxy. Need source-provenance classification and full dataset/manifest reconciliation before calling the 200-session dataset fully accepted. Warm-cache speed is not an acquisition-speed benchmark. |
| M09 | NSE acquisition provenance | Benchmark artifact contains diagnostics showing legacy cached rows without original source URL; a small number of misses were freshly fetched from NSE archives during benchmark. | **PARTIAL** | Verify source URLs, response hashes and retrieval times for every newly acquired file; do not invent provenance for legacy files. |
| M10 | NSE snapshot manifest QA | Manifest test output records 200 sessions and a manifest hash in Run #161 artifact. | **PASS — generated manifest check** | Full row-level reconciliation against canonical data and all required layers remains to be proven. |
| M11 | Step 1 — NSE Quarterly Results endpoint/schema repair | Repository has quarterly-results workflow, collectors, candidate-join and QA tests (e.g. `.github/workflows/quarterly_results_targeted_tests.yml`, `pipeline/quarterly_results_research.py`, `qa/test_quarterly_results_research.py`). | **ARTIFACT_UNVERIFIED / BLOCKING** | Retrieve latest run and inspect source/schema repair artifact; validate issuer/symbol/ISIN, period, source URL and publication time. This remains first priority in the six-step audit. |
| M12 | Step 2 — financial result provenance validation | Validation logic and quarterly metrics modules exist. | **BLOCKED by M11** | After Step 1 passes, prove source URL, publication timestamp, reporting period and symbol/ISIN for each row. |
| M13 | Step 3 — News & Catalyst Join | Dedicated workflow and RSS fallback diagnostics exist. Historical project record reports repeated Step 3 failures. | **BLOCKED / ARTIFACT_UNVERIFIED** | Inspect latest run artifacts; prove join coverage, event timestamp alignment, symbol mapping, source provenance and no look-ahead leakage. |
| M14 | Step 4 — Macro-Geo P0 source groups | Eight split P0 workflows and collectors exist for panel, indices, crude/FX, geopolitical events, reconciliation, canonical integration, normalization and reproducible backbone audit. Historical user reports include several successful parts/runs; latest referenced Run #247 status was UNKNOWN. | **PARTIAL / ARTIFACT_UNVERIFIED** | Reconcile all four required groups: `benchmark_index`, `sector_indices`, `volatility`, `geopolitical_events`. Inspect the latest artifact for each part and source freshness/coverage. |
| M15 | Step 5 — missing/stale hard-gate rejection | Hard-gate implementation and QA modules exist (`pipeline/macro_geo_hard_gate.py`, `qa/test_macro_geo_hard_gate.py`). | **ARTIFACT_UNVERIFIED** | Prove missing/stale required input rejects; prove UNKNOWN is not converted to FAIL or PASS; no hard-gate relaxation. |
| M16 | Step 6 — cross-artifact consistency audit | Existing audit workflows and manifest/factor reports exist. | **BLOCKED** | Complete only after M11–M15 evidence is available; reconcile Manifest, NSDL, repair, event study, factor coverage and counts from the same snapshot. |
| M17 | Historical event study / matured labels | Event-study and historical-regime modules/workflows exist. | **BLOCKED / ARTIFACT_UNVERIFIED** | Need matured H+1/H+3/H+5 outcomes, reproducible event windows and source-timestamp alignment. Do not score immature labels. |
| M18 | Rolling backtest (1 Dec–26 Oct; ~2,700 shares) | User-defined methodology exists in project history: next-day Open entry, 1–5 day exit, 0.22% cost, base universe price >₹50 and average volume >200k. | **ARTIFACT_UNVERIFIED** | Verify input dataset, daily universe, fills, survivorship handling, costs, output ledger and comparison vs base. Do not report performance without artifact. |
| M19 | IPO-PLX V2.0 | Separate IPO discovery/post-listing overlay architecture exists in project design. | **UNKNOWN** | Do not include in V11.3 hard gates. Inspect cohort and W5/W10/W20 artifacts only if required for final paper scope. |
| M20 | Final research paper and evidence appendix | Deliverable structure is defined; cross-report audit and evidence appendix not complete. | **BLOCKED** | Requires accepted P0, provenance, data integrity, matured event study, backtest and regression evidence. |

## 4. Latest verified workflow ledger (2026-11-01)

| Workflow | Run ID | Conclusion | Artifact / evidence | Interpretation |
|---|---:|---|---|---|
| FBIL Provenance #9 | `41320496728` | SUCCESS | Artifact `13089092719` | Earlier backfill/parser attempt; later corrected. |
| FBIL Provenance #10 | `41320718563` | SUCCESS | Artifact `13088957286` | Corrected filename/date parsing run. |
| FBIL Provenance #11 | `41320723105` | SUCCESS | Artifact `13089432150` | Strict workflow at that revision; inspect only for its exact code revision. |
| FBIL Provenance #12 | `41324200203` | SUCCESS | Artifact available in run | Retry-enabled backfill; 236 files and parse success confirmed by latest artifact data. |
| FBIL Provenance #13 | `41324215737` | FAILURE | Artifact `13090164109` | Incorrect quarantine assertion; superseded by #14. |
| FBIL Provenance #14 | `41325197755` | SUCCESS | Artifact `13089969056`; ZIP digest `5ab17515fc6078fdd9f51b83e555a83e6afcbc44c8148b021dfe7320962560d4` | 236 rows, 236 unique dates, zero errors/quarantine; timestamp 0%. |
| NSE Benchmark #162 | `41325197764` | SUCCESS | Artifact `13090719723`; ZIP digest `8e442a108c7cf197b07f0c2be890e9db4492546e207c2d8b5d35f05d2b1142ed` | 200/200 warm-cache hits; 12.768868 sec; manifest/snapshot verified. |
| NSE Benchmark #161 | `41324215748` | SUCCESS | Artifact `13090408760`; ZIP digest `596f5f3d61b524612ec99ef5504dc422a279186a83aa8c26096bfd0a82aacaa1` | 200 sessions / warm-cache validation; provenance caveats remain. |

Earlier workflow outcomes from previous project sessions are retained as historical user-reported evidence only unless their exact artifacts are re-opened and rechecked. A past PASS is not automatically current acceptance.

## 5. Six-step audit gate — current position

| Step | Required work | Current status | Gate |
|---:|---|---|---|
| 1 | NSE Quarterly Results endpoint/schema repair | Implemented modules/tests; latest artifact not yet re-verified | **OPEN — FIRST PRIORITY** |
| 2 | Results source URL, publication time, period, symbol/ISIN validation | Dependent on Step 1 | **BLOCKED** |
| 3 | News/catalyst join coverage and timestamp alignment | Repeated historical failures; latest artifact required | **BLOCKED** |
| 4 | Four Macro-Geo P0 source groups | Partial implementation and prior partial passes; full same-snapshot artifact proof missing | **BLOCKED** |
| 5 | Missing/stale hard-gate rejection test | Code exists; latest acceptance artifact missing | **BLOCKED** |
| 6 | New audit artifacts and cross-report consistency review | Depends on Steps 1–5 | **BLOCKED** |

## 6. Exact next-action queue (no duplicate work)

1. FBIL archive integrity gate is now closed at Run #14; do not repeat this work. Keep FBIL out of Production because timestamp provenance and written use permission remain unresolved.
2. Inspect latest Quarterly Results workflow run and artifact. Do not rebuild its collector unless the artifact identifies a concrete unresolved defect.
3. Inspect latest Step 3 News/Catalyst artifact; repair only the demonstrated failing join/timestamp issue.
4. Inspect the latest artifacts for Macro-Geo P0 Parts 1–8 and build a same-snapshot four-group coverage table. Do not rerun already-passing parts without a reason.
5. Verify hard-gate negative tests and frozen production invariants.
6. Only after all dependencies pass, run the final consistency audit and matured event study/backtest.

## 7. Current phase verdict

**The project is not starting from zero.** Existing work is preserved. The current state is a mixed **PARTIAL + BLOCKED** state:

- Proven passes: RBI DBIE monthly adapter QA; FBIL archive download/row parsing at the latest inspected artifact; NSE 200-session count and warm-cache check; NSE manifest generation check.
- Partial: Factor Registry coverage, NSE legacy-cache provenance, FBIL timestamp provenance and usage permission, Macro-Geo four-group coverage.
- Blocked: quarterly results acceptance, financial-result provenance, News/Catalyst join, full P0 reconciliation, matured event study, final consistency audit, final research paper.
- Unknown/artifact-unverified: historical runs whose artifacts have not been reopened in this snapshot.

**No claim of 100% completion is made. Hard Gate remains BLOCKED.**
