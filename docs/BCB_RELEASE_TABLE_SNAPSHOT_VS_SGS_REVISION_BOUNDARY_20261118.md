# BCB Release-Table Snapshot vs Current SGS — Revision Boundary Audit
Date: 2026-11-18
Branch: research/bcb-priority-metadata-audit-20261117
Scope: re-use the three already captured official BCB external-sector workbooks and the existing 15-series/22930 SGS archive. No new raw download, no overwrite, no inferred as-published values.

## 1. Core finding
The three files are official BCB external-sector workbooks named for publication periods 202601, 202603 and 202610. Their captured HTTP Last-Modified headers are all in October 2026:
- 202601 workbook: Mon, 19 Oct 2026 03:00:58 GMT.
- 202603 workbook: Sun, 18 Oct 2026 18:30:04 GMT.
- 202610 workbook: Mon, 26 Oct 2026 11:31:47 GMT.

Therefore the captured workbook files cannot be asserted to be the original as-published release vintages for January/March/October solely from their filenames. Treat them as immutable captured BCB workbook snapshots with the observed October Last-Modified metadata. Original as-published values remain NOT_PROVEN unless an original release archive, immutable dated copy, or official revision history is obtained.

## 2. Raw capture integrity already recorded
Manifest: data/raw/bcb/BCB_HISTORICAL_RELEASE_TABLES_VINTAGE_MANIFEST_20261117.json
Git blob: 82f6790a0d1590c5519e93abb225300ac9995f1c
Captured: 2026-11-17T13:13:52.546869Z.
All three workbook captures report HTTP 200, XLSX ZIP integrity PASS, content-length matches, and SHA-256:
| File period | Bytes | SHA-256 | HTTP Last-Modified |
|---|---:|---|---|
| 202601 | 232,666 | 525d3ad355d2a68b37d9f59554b2dc2446fd8536647f3c8889b2e91b47345685 | 2026-10-19 03:00:58 GMT |
| 202603 | 151,485 | 3590b1bf3baded2a12c5ec747329bdd0fb7be10b26043eba99b64f8de9f75017 | 2026-10-18 18:30:04 GMT |
| 202610 | 116,357 | 8888aaef2ee5279a8e2f247c0c417247caa24733a659b90e04b618742de71c3a | 2026-10-26 11:31:47 GMT |

## 3. Existing Table 10 extraction results — current SGS minus captured workbook
Existing extraction output: data/qa/BCB_DOMESTIC_PORTFOLIO_RELEASE_VINTAGE_EXTRACT_20261117.json
Git blob: 520d78bcb03e34313fe72dd24b17b4c57234138a
Table: Tabela 10 — Investimentos em carteira — passivos. Units USD million.
| Reference month | SGS 22930 minus table | SGS 22936 minus table | SGS 22942 minus table | Domestic total difference |
|---|---:|---:|---:|---:|
| 2025-12 | +116.17484159 | +211.68297984 | +39.37705925 | +367.23488068 |
| 2026-01 (inferred from Jan-Feb cumulative less Feb) | -0.03714621 | -0.00352552 | -0.04077105 | -0.08144278 |
| 2026-02 | -0.03744462 | +0.03947175 | +203.70779636 | +203.70982349 |
| 2026-09 | -0.00228909 | -0.00852785 | -0.04615997 | -0.05697691 |

Interpretation: the 2026-01 inferred values and 2026-09 Table 10 values are close to the latest archived SGS values (within USD 0.1m). For 2025-12 and 2026-02, larger differences exist, especially SGS 22942 in 2026-02 (+USD 203.7078m current SGS minus captured workbook). These are observed cross-snapshot differences only. They are NOT attributed to a specific revision, correction, classification change, or publication-vintage event.

## 4. Why February 2026 SGS 22942 remains UNKNOWN
- Captured March-2026 workbook's Feb-2026 Table 10 row 24 = USD 2,579.49220364m.
- Captured latest SGS 22942 Feb-2026 value = USD 2,783.2m.
- Difference = +USD 203.70779636m.
- The workbook file's Last-Modified is 18-Oct-2026, not its March 2026 nominal publication month.
- No original as-published February/March workbook, official revision note, or intermediate dated snapshot is in the captured evidence.
- Thus cause/status: UNKNOWN / NOT_PROVEN. Do not label this a confirmed revision or data error.

## 5. Reproducibility hardening
Updated existing script (do not create a second extractor):
scripts/research/extract_bcb_domestic_portfolio_release_vintage.py
Commit: 17e40218c1a2446e5d31bdd4df694e216386298a
New checks: validate exact configured manifest period set; verify each workbook byte length and SHA-256 against manifest before opening; require nonempty file and Table 10 sheet; emit explicit original-as-published status NOT_PROVEN and differences UNATTRIBUTED; retain the February 22942 cause UNKNOWN.
Added bounded workflow:
.github/workflows/bcb_domestic_release_vintage_qa.yml
Commit: a8ca74e8eea0760561a405c031d52229f746dbc9
Six-minute timeout, research branch only, read-only contents permission, compile, manifest hash verification, Table 10 extraction, 90-day artifact. Runtime remains NOT_VERIFIED until a run and artifact are inspected.

## 6. Prior-work continuity correction
The Master Ledger already contained canonical 15-series validator scripts/research/validate_bcb_portfolio_monthly_identities.py and workflow .github/workflows/bcb_portfolio_monthly_identity_qa.yml. A duplicate validator/workflow/report set created during this continuation was deleted rather than retained. The canonical validator remains the sole 15-series identity implementation. Cleanup commits: 0d5d4e84e9318db6b0185a880b419691bd09165f, c41b257b63ff598929cbcdd8ea2fb66aaa69a9cb, 9cb8ed1e89e95d2aa3335c3998c0be99c5934799, 50c0c090dfeea88ea8cbc7fff8eef3c2f753e3a5.

## 7. Acceptance matrix
| Gate | Status |
|---|---|
| Three official BCB workbook snapshots and manifest metadata | PASS — captured |
| Table 10 row extraction and internal workbook arithmetic | PASS — existing extraction output |
| Current SGS vs captured workbook differences quantified | PASS — descriptive only |
| Workbook raw bytes/length/SHA verified by hardened script | CODE COMMITTED; runtime NOT_VERIFIED |
| Original as-published vintage proof | NOT_PROVEN |
| 2026-02 SGS 22942 cause | UNKNOWN |
| Multi-vintage revision attribution | NOT_DONE |
| Brazil pilot acceptance | NOT_ACCEPTED |
| EM-wide panel / production integration | NOT_DONE / NOT_AUTHORIZED |

## 8. Exact next action
Inspect the GitHub Actions run for the newly added bounded workflow and download its artifact. If the run passes, preserve the artifact ID and ZIP SHA-256. Then seek an official original dated workbook or BCB revision note for 2026-02; if none is available, retain UNKNOWN and do not infer a cause from the delta alone.

## 9. Invariants
₹0; official/free sources only; no synthetic data, invented timestamps, forward-fill, raw overwrites or access-control bypass. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A–E, Hard Gate, parser admission and production workflows unchanged. No source admission or production integration authorized.
