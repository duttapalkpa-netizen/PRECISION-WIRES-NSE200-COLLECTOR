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


## 10. Runtime verification update (2026-11-18)
- Workflow Run #2 ID 44150764171: SUCCESS; commit 17e40218c1a2446e5d31bdd4df694e216386298a; job 134278191392; artifact ID 14358771813; ZIP 2,885 bytes; SHA-256 a8ea641748f3c7410aeb6dceda7eeaee8ea0c904a0ceb659ebffa174c4772d86. Downloaded and independently re-hashed. Manifest/workbook SHA and byte-length validation PASS; Table 10 internal identities PASS.
- Workflow Run #1 ID 44150706922 also SUCCESS. Canonical 15-series identity workflow Run #1 ID 44148019785 SUCCESS; all six identities 381/381 PASS, 2,286/2,286 checks, 0 failures; artifact ID 14356334010, ZIP SHA-256 fcf6c72dec436f7847e293c1b179b628a0c0625b420be90aa1460dfdb6baba77, independently re-hashed.
- Official BCB 28-Sep-2026 revision note confirms 2025 portfolio-liability aggregate revised USD 15.1bn to USD17.6bn with reclassification for nonresident individual fund ownership >=10%; it does not attribute February-2026 SGS 22942's +USD203.70779636m delta. Keep cause UNKNOWN.
- Runtime gate: PASS. Original as-published vintage: NOT_PROVEN. Brazil pilot: NOT_ACCEPTED. EM-wide panel: NOT_DONE. Production integration: NOT_AUTHORIZED.


## Follow-on source-scope check (2026-11-18)
- Further targeted official BCB search found no original as-published March-2026 workbook copy and no direct revision notice naming SGS 22942 / February-2026 / USD 203.70779636m.
- BCB 28-Sep-2026 policy note explicitly states the annual review covers definitive 2025 statistics and current-year 2026 estimates. Its documented portfolio-liability change is an annual 2025 aggregate revision from USD 15.1bn to USD 17.6bn, with fund ownership >=10% reclassification between direct and portfolio investment. It does not identify the February-2026 domestic debt monthly-series discrepancy. The same note's 2026 estimate adjustments listed in section 3.3 concern current-account aggregates and direct-investment profits; no 22942-specific amount is disclosed. This is contextual evidence only, not attribution.
- BCB Open Data metadata for SGS 22942 identifies it as monthly, USD million, source Department of Economics/Statistics, temporal coverage from 1995-01; metadata updated 26-Mar-2026 (the localized dataset mirror separately shows metadata update 8-Sep-2026). No revision log/versioned observation history exposed in the metadata record.
- Decision: retain Feb-2026 SGS 22942 cause UNKNOWN / NOT_PROVEN. Original as-published workbook vintage NOT_PROVEN. No further inference from the general revision policy.

## Verified workflow evidence
- Release-vintage QA Run #2 44150764171 SUCCESS; artifact 14358771813; ZIP SHA-256 a8ea641748f3c7410aeb6dceda7eeaee8ea0c904a0ceb659ebffa174c4772d86; independently downloaded and re-hashed.
- Canonical 15-series identity QA Run #1 44148019785 SUCCESS; all six identities 381/381 PASS, 2,286/2,286 monthly checks, 0 failures; artifact 14356334010; ZIP SHA-256 fcf6c72dec436f7847e293c1b179b628a0c0625b420be90aa1460dfdb6baba77; independently downloaded and re-hashed.


## 2026-11-18 — Contemporaneous BCB publication located: February-2026 debt securities rounded value
- Located and opened the official BCB original contemporaneous External Sector Statistics press release dated 27-Mar-2026: https://bcb.gov.br/content/statistics/externalsectorstatistics_prev/202603_External_sector_statistics_text.pdf (official PDF; browser source ref turn942487view0).
- The release reports February-2026 portfolio investment traded in the domestic market: total net inflows USD 5.4bn; equities and investment funds USD 2.8bn; debt securities USD 2.6bn (one decimal billion precision). This is direct official contemporaneous publication evidence that the debt-liability figure was published rounded to USD 2.6bn, consistent with the later-captured March workbook Table 10 value USD 2,579.49220364m.
- The one-decimal press-release value does NOT prove the exact as-published workbook figure or its raw bytes. Do not label the October-Last-Modified workbook as the original March vintage. Exact original value remains NOT_PROVEN; the published rounded figure is corroborated.
- Current captured SGS 22942 is USD 2,783.2m; captured March workbook Table 10 is USD 2,579.49220364m; current-minus-captured delta +USD 203.70779636m. Official March press release rounded value USD 2.6bn (nominal rounding interval approximately USD 2,550m to <2,650m) is consistent with the captured workbook and materially below current snapshot, but it cannot determine exact difference or revision date.
- Important scope exclusions from contemporaneous official releases: 27-Mar-2026 press release section 3 describes an extraordinary external-debt public/private-sector breakdown correction for Dec-2020 to Sep-2025 due to SDR double-counting and intercompany-debt classification, with no change in total external debt; it does not mention portfolio domestic debt series 22942. 24-Apr-2026 press release section 3 covers international travel revenue reclassification Oct-2023 to Feb-2026 from Financial Account—Other Investment—Currency and Deposits; it does not identify SGS 22942 or domestic debt securities. These disclosed revisions are not proven causes of the 22942 delta.
- Updated interpretation: as-published rounded February debt-securities amount = OFFICIAL CONTEMPORANEOUS EVIDENCE (USD 2.6bn); exact as-published workbook/raw vintage = NOT_PROVEN; subsequent difference = SNAPSHOT DIFFERENCE CONFIRMED, revision date/cause = UNKNOWN / NOT_ATTRIBUTED. Do not infer cause from unrelated revision notes.
- Next highest-value action: retrieve the exact February-2026 (27-Mar-2026) BCB historical Tables XLSX from the official “External sector statistics – All publications” archive or an immutable contemporaneous copy; validate its source URL, publication timestamp, bytes and SHA-256, then inspect Table 10 exact row 24. If no exact original file can be retrieved, retain exact-vintage NOT_PROVEN and preserve the PDF's rounded 2.6bn as corroborating evidence only.
- No duplicate extractor, validator, workflow, or raw data created. Existing QA Runs #2 44150764171 and #1 44148019785 remain PASS; no rerun of completed checks. ₹0; official/free sources only; production selector, ranking, pressure fade, CORE-672, Engines A-E and production integrations unchanged.


## 2026-11-18 — Original XLSX retrieval attempt and contemporaneous publication bound
- Exact official BCB Tables URL recovered from the existing raw-capture manifest (not guessed): https://www.bcb.gov.br/content/estatisticas/hist_estatisticassetorexterno/202603_Tabelas_de_estatisticas_do_setor_externo.xlsx. Existing immutable capture at this URL is 151,485 bytes, SHA-256 3590b1bf3baded2a12c5ec747329bdd0fb7be10b26043eba99b64f8de9f75017; response on 2026-11-17 returned HTTP 200 but Last-Modified Sun, 18-Oct-2026 18:30:04 GMT. This confirms current URL serves an October-modified workbook snapshot, not demonstrated original March 2026 file.
- Re-attempted direct retrieval of the official XLSX in this session. Binary retrieval was unavailable in the current execution environment (download failed; direct network DNS unavailable); browser could identify but not download XLSX content type. No replacement file was created, no raw file overwritten, no synthetic vintage generated. Exact original workbook remains NOT_RETRIEVED / NOT_PROVEN.
- Opened the original contemporaneous official BCB press release PDF: https://bcb.gov.br/content/statistics/externalsectorstatistics_prev/202603_External_sector_statistics_text.pdf, dated 27-Mar-2026. Lines 76-82 state February 2026 domestic-market portfolio net inflows USD 5.4bn, comprising USD 2.8bn equities/funds and USD 2.6bn debt securities. Lines 107-121 disclose a separate extraordinary external-debt public/private breakdown correction for Dec-2020 to Sep-2025 due to SDR double-counting and intercompany-debt classification; it states total external debt unchanged. This note does not attribute SGS 22942's domestic debt securities change. (Official PDF evidence inspected in web source turn998532view0.)
- Official BCB Open Data catalog confirms SGS 22942 is “Portfolio investment - Debt securities - issued in the domestic market - monthly - net”, source BCB/Depec, unit USD million, monthly frequency, series coverage from 1995-01. It is not itself a version-history source and does not disclose the specific revision cause. (Official catalog source turn680671search0.)
- Quantitative cross-check using already-archived captured March workbook and latest archived SGS (not a new download): captured Table 10 row 24 = USD 2,579.49220364m; SGS 22942 February-2026 = USD 2,783.2m; difference = +USD 203.70779636m. The captured workbook amount rounds to USD 2.6bn at one decimal billion and is therefore consistent with the March 27 press release. The current SGS amount rounds to USD 2.8bn and is inconsistent with that contemporaneous rounded figure.
- Derived rounding bound (model calculation, assuming conventional nearest USD 0.1bn rounding): a published USD 2.6bn corresponds to an approximate [USD 2,550m, USD 2,650m) interval. Current USD 2,783.2m is at least USD 133.2m above that interval; exact as-published value cannot be inferred from the rounded press release. This is a consistency bound, not a BCB-published exact amount or revision attribution.
- Revised evidence classification: contemporaneous rounded February debt-security publication CONFIRMED; exact March-2026 original XLSX bytes/value NOT_RETRIEVED / NOT_PROVEN; captured later workbook snapshot exact value VERIFIED by prior SHA/Actions run; later SGS snapshot difference QUANTIFIED; exact revision date and cause UNKNOWN / NOT_ATTRIBUTED. Do not call this a proven revision event without exact original vintage or official revision notice.
- No official SharePoint version-history endpoint could be verified from accessible evidence in this pass. Do not treat the workbook's October Last-Modified timestamp as its original release date. No archive mirror accepted as official.
- Next action is narrowed: obtain a pre-18-Oct-2026 immutable copy or BCB file-version record for the exact official XLSX. If no such version is publicly accessible, close this subtask as “exact original workbook unavailable; rounded contemporaneous figure corroborated” and retain the provenance blocker. Do not repeat completed extraction or identity workflows.
- Invariants unchanged: ₹0; official free sources only; no raw overwrite, synthetic data, inferred timestamps or invented exact values; no production integration or scoring changes.
