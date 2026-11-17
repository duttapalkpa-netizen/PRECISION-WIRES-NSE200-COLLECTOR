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


## 2026-11-18 — February-2026 component isolation and public-release revision-window audit
- Reused existing verified extraction output data/qa/BCB_DOMESTIC_PORTFOLIO_RELEASE_VINTAGE_EXTRACT_20261117.json; no raw file download, no re-run of completed identity workflow, no duplicate extractor.
- Exact February-2026 Table 10 vs latest archived SGS component comparison (USD mn):
  | Component | March workbook Table 10 | Latest SGS | Latest minus Table 10 |
  | SGS 22930 domestic equity | 3,132.23744462 | 3,132.2 | -0.03744462 |
  | SGS 22936 fund liabilities | -346.03947175 | -346.0 | +0.03947175 |
  | Equity + funds composite | 2,786.19797287 | 2,786.2 | +0.00202713 |
  | SGS 22942 domestic debt securities | 2,579.49220364 | 2,783.2 | +203.70779636 |
  | Domestic portfolio total | 5,365.69017651 | 5,569.4 | +203.70982349 |
- This isolates the observed discrepancy to SGS 22942 (domestic debt securities). Equity series 22930, fund series 22936 and their composite reconcile within USD 0.04m; the total delta is almost entirely the debt-series delta. This is an evidence-based anomaly localization, not proof of cause.
- January-2026 cross-check using Jan-Feb cumulative Table 10 less February: 22930 difference -USD0.03714621m; 22936 -USD0.00352552m; 22942 -USD0.04077105m; domestic total -USD0.08144278m. All within USD0.1m tolerance. Thus the currently observed large discrepancy is specific to February 2026, not a general month alignment or whole-series scale problem.
- Official contemporaneous BCB press release dated 27-Mar-2026 confirms February portfolio investment domestic market net inflows USD5.4bn, comprising USD2.8bn equity/funds and USD2.6bn debt securities (source: https://bcb.gov.br/content/statistics/externalsectorstatistics_prev/202603_External_sector_statistics_text.pdf; web evidence turn283728view0, lines 62-78). This corroborates the captured Table 10 rounded amount; it does not reveal exact original XLSX bytes or exact unrounded value.
- Sequential public-release review: 24-Apr-2026 BCB release reports March 2026 monthly portfolio investment net outflows USD2.9bn and twelve-month domestic portfolio inflows through Feb USD29.5bn; it discloses a travel-receipts reclassification for Oct-2023 to Feb-2026 but does not name domestic debt series 22942 (official PDF turn183647view0 lines 92-113, 122-159). 26-May-2026 release shows a visual monthly portfolio chart with Feb-2026 approx USD5.4bn and Apr USD0.7bn; the chart is rounded/approximate and does not split debt from equity/funds (turn536083view0 lines 142-180). Therefore later public narrative does not supply exact debt-component revision history.
- Official BCB March 27 extraordinary review disclosure concerns external-debt public/private sector breakdown for Dec-2020 to Sep-2025 caused by SDR double counting and intercompany debt classification; the release says total external indebtedness unchanged (turn283728view0 lines 84-97). This does not establish a cause for February-2026 domestic debt securities flow SGS 22942. April 24 extraordinary review concerns travel receipts, not SGS 22942 (turn183647view0 lines 122-159). Excluded as causal explanations absent a direct link.
- Revision-window decision: exact component change date remains UNKNOWN. Public monthly text releases reviewed through 26-May-2026 do not publish a later exact debt-series value for Feb-2026. The 26-May chart is approximate only and cannot establish an exact post-publication value. Current snapshot captured 17-Nov-2026. Do not assert a precise revision window narrower than after 27-Mar-2026 and by 17-Nov-2026; exact original value/cause remain NOT_PROVEN / UNKNOWN.
- Next action: seek an official BCB revision log or original/archived Table 10 XLSX with a pre-18-Oct-2026 file version. If not accessible, retain the isolated-series anomaly as unresolved and exclude Brazil pilot admission. No additional generic macro conclusions derived from this single series.
- Invariants unchanged: ₹0, official/free sources only, no synthetic data, no invented timestamps, no overwrite, no duplicate audits; Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A-E and production integration unchanged.


## 2026-11-18 — Official live SGS API vs archived 15-series snapshot comparison
- New highest-value check completed using official BCData/SGS JSON endpoints for all 15 archived series. Read-only script scripts/research/audit_bcb_sgs_live_vs_archived_15_series.py; workflow .github/workflows/bcb_sgs_live_vs_archived_audit.yml.
- GitHub Actions Run #1 ID 44155240821, commit e5287c4056789cfc2387498d7d67174c40187fd9, job 134294094688, completed SUCCESS; all six job steps PASS. Run URL https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/44155240821.
- All 15 official SGS API calls HTTP 200; archived CSV SHA-256 and byte lengths verified against the two original capture manifests. Each series has 381 monthly rows from 1995-01 to 2026-09. Overlap 5,715 series-month observations; changed 0; unchanged 5,715. All 15 February-2026 API values equal archived CSV values exactly.
- SGS 22942 February 2026: archived 2,783.2 USD mn; current live API 2,783.2 USD mn; delta 0.0. Live API latest period 2026-09. Thus current SGS and 17-Nov-2026 archive agree; the previously identified +203.70779636m is exclusively between captured March-labelled Table 10 workbook snapshot (2,579.49220364m, Last-Modified 18-Oct-2026) and current SGS. It is not archive corruption or a difference introduced after 17-Nov archive.
- Artifact ID 14361126097; name bcb-sgs-live-vs-archived-15-series-44155240821; 2,951 bytes; GitHub digest and independently downloaded ZIP SHA-256 both 767fd57b7307552beea3135da86220e6a45943c9ea5b2e91160b80c504355216; extracted JSON SHA-256 5a81ad698557bb4de61b24704a88cce226229004980efaf3cbf8eaec3a72f860; expiry 2027-02-15.
- Machine-readable summary committed at data/qa/BCB_SGS_LIVE_VS_ARCHIVED_15_SERIES_20261118_SUMMARY.json (commit 3fa5fe2fd9d3ac71e3480b3967018153a2499ca1). Full report docs/BCB_SGS_LIVE_VS_ARCHIVED_15_SERIES_AUDIT_20261118.md (commit e0497e9f024020a23e283ff9a1c4c4d33ef9ccdc).
- Official source note: BCB Open Data catalog defines 22942 as monthly net portfolio-investment debt securities liabilities issued in domestic market, USD million. Catalog “Metadata last updated 26-Mar-2026” is metadata-record date, not observation-through date: live JSON API contains data through 2026-09. Do not infer data freshness from catalog metadata timestamp.
- Updated decision: collector integrity PASS; 15-series current API/archive snapshot equality PASS; 5,715/5,715 equality PASS; exact original March XLSX vintage NOT_PROVEN; revision date UNKNOWN; cause UNKNOWN / NOT_ATTRIBUTED; Brazil pilot NOT_ACCEPTED; production integration NOT_AUTHORIZED.
- Next action: no rerun of API comparison or accounting identities. Seek exact original March-2026 Table 10 XLSX or official pre-18-Oct-2026 immutable version history. If not available, keep provenance blocker and do not infer cause.
- Invariants unchanged: ₹0, official/free sources only, no synthetic data, invented timestamps, forward-fill, raw overwrites or duplicate audits; Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A–E, Hard Gate and production workflows unchanged.
