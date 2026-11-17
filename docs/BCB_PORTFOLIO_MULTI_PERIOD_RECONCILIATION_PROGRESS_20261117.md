# BCB Portfolio Investment — Multi-Period Reconciliation Progress
Date: 2026-11-17
Branch: research/bcb-priority-metadata-audit-20261117
Scope: research-only accounting identities across the 15 already captured official BCB SGS series.

## Reused evidence — no duplicate acquisition
- Aggregate capture: 7/7 raw series PASS; Run #3 / ID 44075768714; archived in commit 73bf04f6333fd90d8c0d24c7ba9e71eb1ba3f568.
- Instrument capture: 8/8 raw series PASS; archived in commit 527a8d41c434609c980eb3181d491eac4fa6e822.
- Each series contains 381 monthly observations, 1995-01 through 2026-09.
- The raw files and per-series SHA-256 are already in the two archived manifests; this task does not redownload or overwrite them.

## Independent arithmetic recomputation from archived CSV rows
All 15 CSV files were read from the research branch and parsed as monthly USD-million series. The common coverage is 381 months. Six identities were checked over every common month using a strict USD 0.11m residual tolerance (displayed series precision is one decimal USD million).

| Identity | Passing months | Maximum absolute residual | Result |
|---|---:|---:|---|
| 22906 = 22908 − 22907 | 381/381 | 0.1 USD mn | PASS |
| 22924 = 22925 − 22926 | 381/381 | 0.1 USD mn | PASS |
| 22905 = 22906 − 22924 | 381/381 | 0.1 USD mn | PASS |
| 22906 = 22909 + 22912 + 22915 | 381/381 | 0.1 USD mn | PASS |
| 22924 = 22927 + 22936 + 22939 | 381/381 | 0.1 USD mn | PASS |
| 22939 = 22942 + 22945 | 381/381 | 0.1 USD mn | PASS |

Total arithmetic coverage: 2,286 identity-month checks; all 2,286 within tolerance in this independent recomputation.

## Sign conventions established empirically from all 381 monthly rows
- Asset side: SGS 22906 = 22908 (outflows) − 22907 (inflows).
- Liability side: SGS 22924 = 22925 (inflows) − 22926 (outflows).
- Net portfolio investment: SGS 22905 = net acquisition of financial assets (22906) − net incurrence of liabilities (22924).
- Asset instrument components: 22906 = 22909 (equity assets) + 22912 (fund assets) + 22915 (debt assets).
- Liability instrument components: 22924 = 22927 (equity liabilities) + 22936 (fund liabilities) + 22939 (debt liabilities).
- Debt liability market split: 22939 = 22942 (domestic-market debt) + 22945 (external-market debt).

The first two sign conventions were not assumed from English series titles; both candidate orientations were tested. The reverse orientations failed all 381 months and are rejected.

## Runtime reproducibility gate
Added:
- Validator: scripts/research/validate_bcb_portfolio_monthly_identities.py
- Five-minute GitHub Actions workflow: .github/workflows/bcb_portfolio_monthly_identity_qa.yml
- The validator re-hashes all 15 raw CSV files against their exact capture manifests, verifies HTTP/content type/byte length, schema, unique ascending monthly periods and 381-month common coverage, then reruns the six identities.
- The workflow compiles and runs the validator, archives deterministic JSON/Markdown QA outputs to the research branch, and uploads a 90-day artifact.
- Validator commit: 7ea509cc52f9dc8f6a73064fbef0bb7bbf3921d1.
- Workflow commit: 9e2e51551875e35875e83f3d9f71b6198806321d.
- GitHub Actions runtime result: PENDING at the time of this progress update. Do not claim runtime PASS until the workflow run and generated artifacts are inspected.

## Official metadata references
- BCB SGS 22905 portfolio investment aggregate: https://opendata.bcb.gov.br/dataset/22905-portfolio-investment---monthly---net
- BCB SGS 22906 net acquisition of financial assets: https://opendata.bcb.gov.br/dataset/22906-portfolio-investment---net-acquisition-of-financial-assets---monthly---net
- BCB SGS 22907 asset inflows: https://opendata.bcb.gov.br/dataset/22907-portfolio-investment---net-acquisition-of-financial-assets---monthly---inflows
- BCB SGS 22908 asset outflows: https://opendata.bcb.gov.br/dataset/22908-portfolio-investment---net-acquisition-of-financial-assets---monthly---outflows
- BCB SGS 22924 net incurrence of liabilities: https://opendata.bcb.gov.br/dataset/22924-portfolio-investment---net-incurrence-of-liabilities---monthly---net
- BCB SGS 22942 domestic-market debt liabilities: https://opendata.bcb.gov.br/dataset/22942-portfolio-investment---debt-securities----issued-in-the-domestic-market---monthly---net

## Acceptance boundary
- Raw archive reuse and 381-month common-coverage arithmetic recomputation: PASS.
- Six accounting identities in direct recomputation: PASS, 2,286/2,286 checks.
- Raw byte SHA-256 revalidation by new committed validator: PENDING GitHub Actions runtime.
- Instrument semantic labels beyond official dataset metadata and manifest titles: retain exact source wording; no broader mapping inferred.
- Brazil pilot: NOT_ACCEPTED until runtime provenance validation, multi-period independent release-table reconciliation, and vintage/revision gate are closed.
- EM-wide aggregation: NOT_DONE.
- Production/classifier admission: NOT_AUTHORIZED.

## Next actions
1. Verify the workflow runtime and generated QA artifact; fix any mismatch without changing source CSVs.
2. Reconcile the already archived BCB release-table vintages against the corresponding SGS components for multiple reference periods; do not repeat completed January/September checks.
3. Keep February-2026 SGS 22942 revision attribution UNKNOWN unless an immutable original vintage or official revision notice is obtained.
4. No synthetic second vintage. Prospective snapshot comparison waits for the next genuine BCB capture.

## Invariants
₹0; official/free BCB sources only; no synthetic data, fabricated timestamps, forward-fill, raw overwrite or access-control bypass. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A–E, Hard Gate, parser admission and production workflows remain unchanged.

## 2026-11-18 — BCB release-table snapshot integrity and revision boundary
- Reused the existing Table 10 extraction script/output and the three already captured official BCB workbook files; no duplicate download or raw overwrite.
- Found the captured workbook HTTP Last-Modified headers all fall in October 2026: 202601 file 19-Oct-2026 03:00:58 GMT; 202603 file 18-Oct-2026 18:30:04 GMT; 202610 file 26-Oct-2026 11:31:47 GMT. Thus file naming/publication period alone does not prove original as-published vintage. All three must be treated as captured BCB workbook snapshots, not proven original releases.
- Reused manifest data/raw/bcb/BCB_HISTORICAL_RELEASE_TABLES_VINTAGE_MANIFEST_20261117.json (blob 82f6790a0d1590c5519e93abb225300ac9995f1c): all three HTTP 200, XLSX ZIP integrity PASS, sizes and SHA-256 captured. Full details are in docs/BCB_RELEASE_TABLE_SNAPSHOT_VS_SGS_REVISION_BOUNDARY_20261118.md (commit 73bd74ee76bc66885d54c5a28ddd1cd90476df56).
- Existing extraction output data/qa/BCB_DOMESTIC_PORTFOLIO_RELEASE_VINTAGE_EXTRACT_20261117.json (blob 520d78bcb03e34313fe72dd24b17b4c57234138a) shows current SGS minus captured workbook: 2025-12 domestic total +367.23488068 USD mn; 2026-01 inferred from Jan-Feb cumulative -0.08144278; 2026-02 +203.70982349 (driven by SGS 22942 +203.70779636); 2026-09 -0.05697691. January inferred and September differences are within USD 0.1m; December and February differences are materially larger. These are cross-snapshot differences, not attributed revisions.
- February-2026 SGS 22942 remains UNKNOWN/NOT_PROVEN: captured March workbook's row 24 is USD 2,579.49220364m, current archived SGS is USD 2,783.2m, difference +203.70779636m; no original as-published workbook, official revision notice or intermediate dated snapshot has been evidenced.
- Hardened the existing extractor (did not create a second extractor): scripts/research/extract_bcb_domestic_portfolio_release_vintage.py now checks configured manifest periods, exact workbook byte length and SHA-256 before opening, nonempty XLSX and Table 10 presence; emits explicit original-as-published NOT_PROVEN and differences UNATTRIBUTED. Commit 17e40218c1a2446e5d31bdd4df694e216386298a.
- Added bounded research-only workflow .github/workflows/bcb_domestic_release_vintage_qa.yml, 6-minute timeout, read-only contents permission, compile + manifest hash + Table 10 extraction + 90-day artifact. Commit a8ca74e8eea0760561a405c031d52229f746dbc9. Runtime/artifact still NOT_VERIFIED pending run inspection.
- Continuity correction: Master Ledger already contained canonical 15-series validator scripts/research/validate_bcb_portfolio_monthly_identities.py and workflow .github/workflows/bcb_portfolio_monthly_identity_qa.yml. A duplicate validator/workflow/report set briefly created during this continuation was deleted; canonical implementation retained. Cleanup commits: 0d5d4e84e9318db6b0185a880b419691bd09165f, c41b257b63ff598929cbcdd8ea2fb66aaa69a9cb, 9cb8ed1e89e95d2aa3335c3998c0be99c5934799, 50c0c090dfeea88ea8cbc7fff8eef3c2f753e3a5.
- Acceptance: workbook snapshot capture and manifest evidence PASS; existing Table 10 extraction/internal workbook identities PASS; deltas quantified PASS; workbook manifest revalidation code COMMITTED / runtime NOT_VERIFIED; original as-published vintage NOT_PROVEN; February 2026 SGS 22942 cause UNKNOWN; multi-vintage revision attribution NOT_DONE; Brazil pilot NOT_ACCEPTED; EM-wide panel NOT_DONE; production integration NOT_AUTHORIZED.
- Exact next action: inspect the Actions run and artifact for the new BCB domestic release vintage QA workflow. Then seek an official original dated workbook or revision note for 2026-02; absent that evidence, retain UNKNOWN.


## 2026-11-18 — GitHub Actions runtime closure and official revision-policy cross-check
- BCB domestic release vintage workflow verified end-to-end: Run #2 / ID 44150764171, commit 17e40218c1a2446e5d31bdd4df694e216386298a, created 2026-11-17T18:42:37Z, completed SUCCESS; job extract-and-verify ID 134278191392; all 7 steps (checkout, Python, openpyxl, compile, manifest+Table 10 extraction, artifact upload) PASS. Run URL https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/44150764171.
- Artifact ID 14358771813, name bcb-domestic-release-vintage-qa-44150764171, 2,885 bytes, SHA-256 a8ea641748f3c7410aeb6dceda7eeaee8ea0c904a0ceb659ebffa174c4772d86; downloaded and independently re-hashed in this session; ZIP contains BCB_DOMESTIC_PORTFOLIO_RELEASE_VINTAGE_EXTRACT_20261117.json. Expiry 2027-02-15.
- Artifact JSON acceptance PASS_TABLE_EXTRACTION_AND_INTERNAL_IDENTITIES; VINTAGE_DIFFERENCES_QUANTIFIED_NOT_ATTRIBUTED. All three workbook byte lengths/SHA-256 exactly match manifest; all Table 10 internal identities true; original_as_published_vintage_status NOT_PROVEN; February 2026 SGS 22942 cause UNKNOWN_NOT_PROVEN. Run #1 ID 44150706922 also SUCCESS; Run #2 confirms hardened extractor code. Both are separate runs of same workflow, not duplicate audits.
- Existing canonical 15-series monthly identity workflow also verified: Run #1 / ID 44148019785, commit 9e2e51551875e35875e83f3d9f71b6198806321d, created 2026-11-17T18:27:24Z, completed SUCCESS; job validate ID 134268354820; all steps PASS, including raw SHA checks and all six identities across 381 months (1995-01 to 2026-09), 2,286/2,286 identity-month checks; every identity 381/381 PASS, 0 failures, max absolute residual USD 0.1m under tolerance USD 0.11m. The workflow archived QA output in branch commit b3f6a63 (short SHA as shown in job log).
- Canonical identity artifact ID 14356334010, 4,396 bytes, SHA-256 fcf6c72dec436f7847e293c1b179b628a0c0625b420be90aa1460dfdb6baba77; downloaded and independently re-hashed. ZIP contains JSON and Markdown report. Expiry 2027-02-15.
- Official BCB cross-check: 28-Sep-2026 External Sector Statistics press note (official BCB page) says the September 2026 annual revision policy updated definitive 2025 and estimates for 2026; for 2025, portfolio-investment liability inflows were revised USD 15.1bn to USD 17.6bn, with reclassification between direct and portfolio investment where a nonresident investor individually owns >=10% of a fund (ownership data not available in exchange contracts). The note does not state that this mechanism caused the specific February-2026 domestic debt-liability SGS 22942 +USD203.70779636m delta; therefore the Feb-2026 cause remains UNKNOWN. Source: https://bcb.gov.br/estatisticas/estatisticassetorexterno (section “Política e processo de revisão”; publication 28-Sep-2026). Revision-policy PDF: https://www.bcb.gov.br/content/estatisticas/Documents/notas_metodologicas/Politica_de_Revisoes_de_Estatisticas.pdf. BCB open-data SGS 22942 metadata confirms monthly USD million series, source BCB Department of Economics/Statistics, metadata update 26-Mar-2026 (catalog page: https://opendata.bcb.gov.br/dataset/22942-portfolio-investment---debt-securities----issued-in-the-domestic-market---monthly---net).
- No original as-published Feb-2026 workbook or direct 22942 revision notice found in this pass. The broad September revision disclosure is context only, not direct causal proof. Preserve UNKNOWN / NOT_PROVEN.
- Runtime acceptance updated: BCB domestic release vintage validator runtime PASS; canonical 15-series identity validator runtime PASS; both artifact ZIP digests independently reverified. Original vintage proof NOT_PROVEN; Feb-2026 22942 attribution UNKNOWN; multi-vintage revision attribution NOT_DONE; Brazil pilot NOT_ACCEPTED; EM-wide panel NOT_DONE; production integration NOT_AUTHORIZED.
- Exact next action: continue official-source search for a dated original 2026-03 workbook / immutable pre-October 2026 copy or a BCB-specific 22942 revision notice; if absent, retain UNKNOWN and await next genuine future BCB snapshot for prospective comparison. Do not redownload existing archive or repeat the six identity tests.


## Follow-on source-scope check (2026-11-18)
- Further targeted official BCB search found no original as-published March-2026 workbook copy and no direct revision notice naming SGS 22942 / February-2026 / USD 203.70779636m.
- BCB 28-Sep-2026 policy note explicitly states the annual review covers definitive 2025 statistics and current-year 2026 estimates. Its documented portfolio-liability change is an annual 2025 aggregate revision from USD 15.1bn to USD 17.6bn, with fund ownership >=10% reclassification between direct and portfolio investment. It does not identify the February-2026 domestic debt monthly-series discrepancy. The same note's 2026 estimate adjustments listed in section 3.3 concern current-account aggregates and direct-investment profits; no 22942-specific amount is disclosed. This is contextual evidence only, not attribution.
- BCB Open Data metadata for SGS 22942 identifies it as monthly, USD million, source Department of Economics/Statistics, temporal coverage from 1995-01; metadata updated 26-Mar-2026 (the localized dataset mirror separately shows metadata update 8-Sep-2026). No revision log/versioned observation history exposed in the metadata record.
- Decision: retain Feb-2026 SGS 22942 cause UNKNOWN / NOT_PROVEN. Original as-published workbook vintage NOT_PROVEN. No further inference from the general revision policy.

- BCB release vintage QA Run #2 44150764171 SUCCESS; artifact 14358771813; ZIP SHA-256 a8ea641748f3c7410aeb6dceda7eeaee8ea0c904a0ceb659ebffa174c4772d86; independently verified.
- Canonical 15-series monthly identity QA Run #1 44148019785 SUCCESS; all six identities 381/381 PASS across 381 months (2,286/2,286 checks); artifact 14356334010; ZIP SHA-256 fcf6c72dec436f7847e293c1b179b628a0c0625b420be90aa1460dfdb6baba77; independently verified.
