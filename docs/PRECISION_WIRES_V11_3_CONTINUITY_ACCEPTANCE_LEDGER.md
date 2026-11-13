# PRECISION-WIRES V11.3 — Continuity & Acceptance Ledger
Last reconciled: 2026-11-08 (Asia/Kolkata)
Repository: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR

## 1. Non-negotiable project invariants
- Production Selector unchanged.
- RANKING_SCORE unchanged.
- +1 PRESSURE_FADE unchanged.
- CORE-672 unchanged: 56 Steps × 12 Filters.
- Engines A–E and IPO-PLX V2 overlay remain as specified in the approved master architecture.
- Research-only code is not production integration. No automatic trade trigger.
- UNKNOWN is neither PASS nor FAIL.
- No fabricated data, inferred timestamps, synthetic vintage rows, unsupported source promotion, base-year/classification splicing, or relaxed Hard Gate.
- ₹0 spend; free official sources only; no paid APIs.
- Retain prior PASS artifacts, Run IDs, manifests and SHA-256 values.
- No PR merge or production integration without explicit user approval.
- Keep CI bounded to <10 minutes, ideally 20–60 seconds where feasible.

## 2. IIP audit — verified state
### April 2026 current-series cross-check
- PR #23, branch `qa/iip-apr2026-crosscheck-validation`, head `73124e1ac011e4975350330dfe50f11fefb9f09b`, open/draft/unmerged at last recorded check.
- Run #46 / ID `42491849056`: SUCCESS; 23/23 named NIC-2 manufacturing rows matched two later PIB Statement IV releases.
- Uploaded portal workbook `iip_62.xlsx`: 90,294 bytes; SHA-256 `31ab1a00ea14b90a21086d3c618cd65456e45b3a02b4ae85251ee1dac9fb189e`.
- April portal catalogue ID/download timestamp not captured; do not invent them.
- First-release WPI PDF raw SHA remains pending.

### 41-vintage audit and revision comparison
- PR #21, branch `fix/iip-41-vintage-audit-mainline-isolated`, open/unmerged; no production merge.
- Run #245 / ID `42452130606`: audit completed operationally; 37 qualifying records, 36 raw workbooks downloaded/cache-verified and parsed, 1 failed download (April 2026 legacy 2011-12/NIC-2008 file HTTP 404), 116,740 parsed observations, 1,058 snapshot differences.
- Run #250 / ID `42500736335`: full audit passed, independent validator failed because it incorrectly treated repeated series-period keys across distinct successive vintage pairs as duplicates.
- Fix: uniqueness key now includes both previous and current vintage IDs.
- Run #251 / ID `42501079840`: SUCCESS; full 41-vintage audit and independent validator both passed. This validates 1,058 snapshot differences against observation rows, hashes, delta arithmetic and release chronology. It does not prove why MoSPI changed a value.
- Independent classification: 1,010 differences in 2011-12/NIC-2008 and 48 in 2022-23/NIC-2025. All are snapshot differences, not necessarily corrections or errors.
- Run #252 / ID `42501277644`: SUCCESS on PIB ingestion sidecar's initial commit (script not yet included in workflow at that commit).
- Run #253 / ID `42501293659`: FAILED. The new PIB sidecar found the Statement IV table but failed due to a case mismatch: HTML headers were lowercased, while month lookup keys were mixed-case. Exact fix committed as `cc1b8c0ceaf7f7d4bcf0660827534f482357d69f`: normalize target keys to lowercase.
- Run #254 / ID `42507902637`: SUCCESS; full 41-vintage audit, PIB supplementary snapshot ingestion and independent revision validator all passed. Artifact ID `13628033276`, ZIP SHA-256 `a988e47f6679def45d3fa3316e5d3207040047a847cd19410458a40db1814f3b`.
- Run #254 PIB sidecar output: exactly 69 rows = 3 periods × 23 NIC codes (10–32), no missing code-period combinations; periods 2025-04, 2025-09, 2026-02; source PRID 2256241, release date 2026-04-28; all rows carry the same non-empty source-page SHA-256 `cf78fee28f487cd152c527d5249de5747316348cbc1fcc646ebcb24b95c9eb2b`; CSV SHA-256 `1199f490ad3003f28628d4fbb6f990d0d0371b277bf4f877b2b1d4c3384c9038`.
- All 69 rows explicitly labelled `PIB_LATER_RELEASE_SNAPSHOT` and `NOT_ESTABLISHED_FROM_THIS_SNAPSHOT` for first-release status. This is supplementary later-snapshot coverage, not original MoSPI vintage recovery.
- Independent value cross-check: all 69 values (23 NIC codes × Apr-25, Sep-25, Feb-26) were compared against MoSPI-hosted March-2026 press-release PDF, Statement IV; 69/69 exact matches, 0 mismatches. MoSPI PDF URL: https://www.mospi.gov.in/uploads/latestReleases/latest_release_1777370981972_ac151bbf-29ab-4f2c-a10e-bd727a4d3564_IIP_Press_release_March_2026.pdf . The PDF release is dated 28 Apr 2026 and explicitly provides monthly NIC-2008 values for the last 13 months. Raw PDF bytes/SHA-256 not captured in this session; do not claim a raw-PDF hash.
- Run #254 artifact ZIP SHA-256: `a988e47f6679def45d3fa3316e5d3207040047a847cd19410458a40db1814f3b`; PIB supplementary CSV SHA-256: `1199f490ad3003f28628d4fbb6f990d0d0371b277bf4f877b2b1d4c3384c9038`; revision differences CSV SHA-256: `51f4036ebd45796a07514295728e018049ec20b4b1c7683d7ee11d246e277f17`; observation CSV SHA-256: `e8cbda9e24d4f1d56aedd9cbd216ce708ee34dac82769da2dbc912ad8193b3b6`; vintage manifest SHA-256: `efeadc05f5a84203e17d3a157e9efadd1055aab6550bbb01cece5e7c83b21d49`.
- Run #254 revision validator again passed: 116,740 observation rows; 1,058 differences; 0 integrity errors.
- Run #253 case mismatch root cause was fixed by lowercasing TARGETS keys; no further parser patch was needed after Run #254.

### Missing periods and source boundary
- Three missing reference periods in the legacy 2011-12/NIC-2008 audit window: 2025-04, 2025-09, 2026-02.
- Official PIB release PRID 2256241, posted 28 Apr 2026, includes Statement IV with monthly NIC-2008 indices for Mar-25 through Mar-26. This is a later published snapshot, NOT the original MoSPI catalogue release/vintage. It can provide supplementary observation coverage only, not vintage restoration.
- Official source URL: https://www.pib.gov.in/PressReleasePage.aspx?PRID=2256241&lang=2&reg=48
- The attempted legacy April 2026 MoSPI workbook request returned HTTP 404 with response SHA-256 `811de0d1fef7c9e0efae9cac56aa62dc5ddeff228cdb572326c97e6079a87030`; response body excerpt `{"error":"File not found"}`.
- Official MoSPI March-2026 old-series press release (28 Apr 2026) provides old-base 2011-12 NIC-2008 data through March 2026, including Statement IV monthly NIC-2 values. Official PDF: https://www.mospi.gov.in/uploads/latestReleases/latest_release_1777370981972_ac151bbf-29ab-4f2c-a10e-bd727a4d3564_IIP_Press_release_March_2026.pdf
- MoSPI's first April-2026 release is explicitly the NEW series with base 2022-23, dated 1 Jun 2026. The Ministry states the base year was revised from 2011-12 to 2022-23 and the April release is Part A of the new series. Official PDF: https://www.mospi.gov.in/uploads/latestReleases/latest_release_1780371708887_52b83604-666c-443a-82c6-4411103e2ede_Press_Release_IIP_2022-23f.pdf
- Therefore April-2026 is not a missing monthly observation in the old 2011-12/NIC-2008 series: the official release boundary is March-2026. The 404 does not establish a lost required vintage; the old-series April catalogue ID/file expectation should be retired as NOT_APPLICABLE unless a separate official catalogue record proves otherwise.
- Do not replace this old series with the separate 2022-23/NIC-2025 April workbook. Do not splice base years/classifications. Maintain two distinct series with an explicit transition boundary.
- Legacy 2011-12/NIC-2008 monthly release lineage and new 2022-23/NIC-2025 lineage must remain separate.

## 3. Global Capital Rotation overlay
- PR #20: research-only overlay; open/unmerged. Engineering implementation and QA reported 100%; live continuous acquisition incomplete; India-vs-US/World historical backtest 0% proven; sector-to-stock transmission validation 0%; production integration 0%.
- Keep global EM aggregate flow distinct from India FPI; daily Indian FPI does not prove broad EM rotation.
- Missing/stale source values remain UNKNOWN; no forward-fill.
- No automatic sector or stock beneficiary inference from political headlines.

## 4. Other known blockers
- Project-wide Hard Gate remains BLOCKED. Earlier audit: P0 source groups 7/8, factor groups 0/35, historical regime coverage 9/11; revalidate before using as current status.
- Multi-source acquisition registry commit `bc2f1a12918b19b9bea0b339deef6291bae43427` had sources DISCOVERED_NOT_LIVE_VALIDATED.
- Full production acceptance ledger and event-study maturity are not complete; no defensible overall project percentage until reconciled.

## 5. Next actions — ordered, do not repeat completed work
1. Run #254, its 69-row supplementary PIB snapshot validation, and the 69/69 MoSPI PDF Statement IV value cross-check are complete; do not repeat these tasks without new source/code changes.
2. Close the legacy April-2026 2011-12/NIC-2008 workbook recovery as NOT_APPLICABLE, not NOT_RECOVERED: the official old series ends with March-2026 and April-2026 is the first 2022-23 base release. Retain the 404 response as an audit trail, but do not keep searching for a nonexistent old-series April release unless an official catalogue entry proves one existed.
3. The next highest-value IIP work is a formal series-transition crosswalk: old base 2011-12/NIC-2008 through Mar-2026, new base 2022-23 from Apr-2026, with overlap/comparability metadata kept separate and no index-level splicing.
4. Preserve PR #21 open/unmerged and PR #23 evidence separately.
5. Complete consolidated project acceptance reconciliation before publishing an overall project percentage.

## 6. Progress reporting rules
Report workstream percentages separately from evidence status. Percentage means completion of the defined work package, not confidence or production readiness. Use PASS / BLOCKED / UNKNOWN explicitly. Overall project percentage must be marked NOT_CALCULABLE until the complete acceptance ledger and weights are reconciled; never invent a percentage.

## 7. User workflow preferences
- User asks for the single highest-value next task, completed quickly and correctly.
- Do not repeat completed work. Check prior Run IDs, artifact hashes and commits first.
- For each task, report progress percentage and evidence status; report overall project percentage only when defensible.
- Preserve project history and explain fixes learned from earlier CI failures.
- Respond in Bengali; no spending money.


## 8. IIP transition crosswalk v2 — current official series controls (2026-11-08)
- New durable document: `docs/IIP_SERIES_TRANSITION_CROSSWALK_V2.md`.
- Commit: `bec01dff8d290948baffe6c0396ae0f872968e1b`.
- URL: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/blob/main/docs/IIP_SERIES_TRANSITION_CROSSWALK_V2.md
- Important correction from official source reconciliation: current 2022-23 IIP classification is NIC-2025, not NIC-2008. MoSPI September-2026 release explicitly reports manufacturing groups at NIC-2025 two-digit level. Keep legacy `2011-12 / NIC-2008` and current `2022-23 / NIC-2025` separate; no join without official concordance.
- Important vintage correction: 1 June 2026 new-base release used WPI deflator but was explicitly superseded by MoSPI/PIB on 29 June 2026 with Output PPI-based 2022-23 series. Current IIP pipeline must use Output-PPI vintage; preserve 1 June as superseded first-release vintage only.
- 29 June 2026 official comparative annual growth-rate bridge was transcribed into the crosswalk (not recomputed from index levels). General: 2022-23 Output-PPI series 6.8%, 5.7%, 4.3% for FY2023-24/2024-25/2025-26 versus legacy 5.9%, 4.0%, 4.1%. Manufacturing: 7.1%, 6.0%, 4.8% versus legacy 5.5%, 4.1%, 5.0%. Official warning: growth rates are not strictly comparable because of coverage, methods, baskets, sector composition and weights.
- Latest verified monthly vintage in this review: September-2026 quick estimate, PIB PRID 2329475, published 28 Oct 2026; overall IIP growth 6.7%, manufacturing 7.6%, mining -6.2%, electricity & gas 11.2%, water/sewerage/waste management 5.8%. August-2026 final revision also reported. Quick estimates are revisable; retain vintage and response-rate metadata (86.5% for September quick estimate; 92.0% for August final revision).
- Official source pages: https://www.pib.gov.in/newsite/archiveContent.aspx?lang=2&reg=48&relid=290616 (29 Jun Output-PPI supersession and comparative bridge); https://www.pib.gov.in/PressReleasePage.aspx?PRID=2329475&lang=2&reg=48 (Sep 2026 latest monthly release); https://www.pib.gov.in/PressReleasePage.aspx?PRID=2256241&lang=2&reg=3 (last legacy series release).
- Earlier IIP transition doc's broad classification description is superseded by this v2 crosswalk where it states the current new-series classification. Do not repeat the earlier assumption that new series is NIC-2008.
- Crosswalk specification/evidence reconciliation: 100% complete for the defined documentation task; raw-byte SHA-256 capture for all cited release PDFs, a machine-readable official NIC concordance, complete monthly vintage acquisition, IIP 41-vintage gate and all other project gates remain incomplete or UNKNOWN.
- No production changes, no PR merge, no workflow rerun, and no alteration to protected V11.3 invariants.


## 9. NIC concordance applicability audit (2026-11-09)
- New document: `docs/NIC_CONCORDANCE_IIP_APPLICABILITY_AUDIT.md`.
- Commit: `810bbb3728d2ad244c3c876bc8b32b6d7007d38c`.
- URL: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/blob/main/docs/NIC_CONCORDANCE_IIP_APPLICABILITY_AUDIT.md
- Official MoSPI NIC-2025 PDF located: https://www.mospi.gov.in/uploads/publications_reports/publications_reports1763457214315_c3e5d4f3-8e25-4775-85e3-ad42d571652f_NIC_2025_Final.pdf . Concordance is explicitly 4-digit class level, printed pages 232–238; source defines `(p)` as part and `+` as aggregation.
- Verified examples include 0113 <- 0113+0128(p), 0330 <- 0311(p)+0312(p)+0321(p)+0322(p), 2611/2619 <- 2610(p), 3511/3512/3513 <- 3510(p), and 3101/3102 <- 3100(p). This proves simple prefix/truncation or one-to-one renaming is unsafe.
- Decision: official concordance source discovery and IIP applicability audit PASS; machine-readable full extraction, forward/reverse multiplicity tests, and IIP-specific item-group/weight mapping remain UNKNOWN/BLOCKED. Do not claim a complete 2-digit bridge or derive IIP weights/index conversion from class concordance.
- This closes only source discovery and applicability assessment, not the IIP classification bridge, 41-vintage gate or project Hard Gate.
- No CI rerun, no PR merge, no production changes, no changes to protected V11.3 invariants.


## 10. IIP manufacturing NIC crosswalk safety audit (2026-11-09)
- New document: `docs/IIP_MANUFACTURING_NIC_CROSSWALK_SAFETY_AUDIT.md`.
- Commit: `5f5a7540dde1a1c814cd959a9ccb3a6c53fcfe46`.
- URL: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/blob/main/docs/IIP_MANUFACTURING_NIC_CROSSWALK_SAFETY_AUDIT.md
- Official MoSPI source PDF was opened and inspected at printed pages 232–234 / source lines 15228–15475: https://www.mospi.gov.in/sites/default/files/main_menu/national_industrial_classification/NIC_2025Final_18112025.pdf .
- Manufacturing examples verified include 1103/1104 <- 1103(p); 1512 <- 1512+2220(p); 1811 <- 1811+1313(p); 2520 <- 2520+3030(p); 2611/2619 <- 2610(p); 3101/3102 <- 3100(p); 3511/3512/3513 <- 3510(p); 3530 <- 3530+1104(p).
- Safety determination PASS: do not collapse 4-digit concordance into IIP 2-digit divisions by prefix, row count or class count. The mapping has partial splits and cross-division aggregations; NIC concordance alone is not an IIP item-group/weight bridge.
- Full 463-row machine-readable extraction remains NOT_COMPLETED; IIP-specific item-group/weight correspondence remains UNKNOWN/BLOCKED. A source table continuation fragment exists (NIC-2025 4772 row continues with 4799(p) in next table block); future parser must preserve and deterministically join such fragments or fail closed.
- No workflow rerun, no PR merge, no production changes, no changes to protected V11.3 invariants.


## 11. IMF BOP_AGG estimation-methodology and vintage gate (2026-11-13)
- Official source inspected: IMF BOPSY Explanatory Notes, November 2025 (31-page PDF), https://data.imf.org/-/media/Explanatory-Notes-November-2025-BOPSY.pdf . Dataset page: https://data.imf.org/en/datasets/IMF.STA%3ABOP_AGG .
- New source-register addendum records the critical quality boundary: IMF uses WEO data to fill gaps in financial-account transactions for world/country-group aggregates; other components may use WEO substitutions and carry-forward adjustments. BOP_AGG group values therefore are not observed-only country-reported flow sums.
- The explanatory notes also document global financial-account discrepancies, vintage-specific Emerging and Developing Economies regional membership, and country reporting-year heterogeneity. India’s November-2025 overview reports BOP and IIP through 2024; this annual data cannot time a 2026 daily signal.
- Source register updated: `docs/GLOBAL_CAPITAL_ROTATION_OFFICIAL_SOURCE_REGISTER_V1.md`, commit `1cba3087696aaad9f51f519979f7a6493051a91e`, blob `2110d623a7ce27cc91e9d352231181963473b52d`.
- QA regression added to `qa/test_global_capital_rotation_overlay.py`; final assertion correction commit `0f2d0069e7b91f1bb7c2176349a3915959e497a6`, blob `ba9f4708c966b7cbba1b492d4c1c92217e394e53`.
- CI Run `43372002545`: SUCCESS; 28 tests passed in 0.011s; 0 failures/errors. https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/43372002545 .
- Defined work-package progress: methodology/source qualification + documentation + regression guard = 100% complete. Separate raw BOP_AGG download/vintage/SHA-256 QA = 0% complete (not acquired). BOP6 country-level observation access remains UNKNOWN/BLOCKED; no observation or EM aggregate created.
- Candidate branch at verification: 37 commits ahead, 0 behind `main`; no PR opened or merge performed. No production selector, ranking, pressure-fade, diagnostics, engines or Hard Gate changes.
- Project-wide progress: NOT_CALCULABLE until the full weighted acceptance ledger across all V11.3 layers, data coverage, matured event studies and backtests is reconciled. Do not substitute branch commit count or this work-package percentage for total project completion.


## 12. IMF BOP_AGG 2026 vintage and raw-download access gate (2026-11-13)
- Official IMF dataset page and linked BOPSY Dashboard inspected. Dataset is annual/November; dashboard page publication date is 19 November 2025. As at 13 November 2026, no 2026 BOP_AGG publication date/vintage is exposed by the inspected official pages. State is 2026 vintage NOT VERIFIED, not proof of non-publication.
- IMF API link redirects to sign-in. Dataset page's visible VIEW DATA / DOWNLOAD controls do not expose a direct static file URL in the retrieved page text. No official workbook/table bytes acquired.
- November 2025 notes show India latest reported BOP and IIP period = 2024; retain reporting lag distinct from publication vintage.
- Source register commit `12f6bca6682b74eac48eae5e51228a4df890030f`, blob `453e50f74e346257f03a32e3dbd22a91418e960f`.
- QA regression commit `72f3c6261239b0152c95214db1e64f1b789b10fa`, blob `a593790e7b86e2f5ce0bc42a011a51ab29bce965`.
- Defined work package (official page/date/access-path reconciliation and QA guard) = 100% pending CI; raw data acquisition/HTTP provenance/SHA-256 = 0%; 2026 vintage = NOT VERIFIED. No third-party mirror or synthetic observation used.
- Production and project-wide completion percentages remain unchanged; total V11.3 percentage NOT CALCULABLE pending weighted master-ledger reconciliation.


### Final CI verification for section 12
- CI Run `43372403935`: SUCCESS; 29 tests passed in 0.013s; 0 failures/errors. https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/43372403935 .
- Work-package completion including documentation and CI = 100%. Data acquisition remains 0% because the IMF anonymous download route is not verified and no raw file was acquired.


## 13. IMF WEO October 2026 country-group flow candidate qualification (2026-11-13)
- Official WEO October 2026 page lists a complete Excel dataset with Countries, Country Groups and Commodity Prices sheets. Official workbook target URL recorded in source register; workbook bytes were not retrieved (web viewer unsupported XLSX content-type; direct transfer attempt failed). Size, retrieval time and SHA-256 NOT ACQUIRED.
- Official October 2026 Database Appendix confirms data cutoff 2026-09-30; workbook shading distinguishes historical results vs IMF staff projections; some 2025 and earlier values may be estimates; country-group composites generally require at least 90% weighted coverage; external-account composites are sums converted to USD at average market exchange rates; WEO EMDE membership is vintage-specific. Exact net portfolio investment series code/unit and actual/projection flags remain unverified until workbook parsed.
- Register commit `6bb4d5cf1977f5bb3b1e14bb56f25afefa85adc0`, blob `4ae97039db62231966e1550dd09631cf05341729`.
- QA regression commit `d00db490cd9c3aa86f6c52bbc17e365a1ec50dc9`, blob `6ac5bedd77ba3241f6a127cb50e971d93e271725`.
- Decision: separate WEO candidate for low-frequency macro context only; not a BOP_AGG replacement, not an observed-only flow source, and not a 1–5 day trigger. No WEO values ingested. Metadata qualification pending CI; workbook acquisition/series mapping 0%.
- Overall V11.3 progress remains NOT CALCULABLE; production unchanged; no PR/merge.


### Final CI verification for section 13
- CI Run `43372686084`: SUCCESS; 30 tests passed in 0.022s; 0 failures/errors. https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/43372686084 .
- WEO metadata/source-qualification work package including register, QA guard and CI = 100%. Actual workbook acquisition and exact series mapping = 0% / PENDING; no observations used.


## 14. WEO country-group actual/projection metadata correction and download attempt (2026-11-13)
- Official IMF WEO FAQ (last updated October 2026) states individual country-series can expose `Latest Actual Annual Data`, but explicitly says this metadata is NOT provided for WEO country-group data; for groups, publication year is assumed to start the forecast period. The prior appendix-only note about shading/forecast years was insufficient for classifying group values. Group actual-vs-estimate state is now UNKNOWN / NOT_POINT_IN_TIME_VERIFIED; do not infer from year, shading or country metadata.
- FAQ confirms WEO database has no monthly/quarterly observations; historical data may include IMF staff estimates when country source data are incomplete; WEO group compositions are restated using publication-vintage membership across historical periods. These restrictions make WEO unsuitable as observed-only EM portfolio flow panel or short-horizon trigger.
- Direct IMF-hosted Excel download attempted; transfer failed before bytes were obtained. No local workbook, response headers, byte count, retrieval timestamp or SHA-256. No third-party checksum adopted.
- Corrective source register commit `8503ec835126b77cce63d57d019c5b546264ec31`, blob `fabf8f49495e429ff99de1ac095c0f9c46d6f59e`.
- Regression guard commit `8c1fb2fa24799d807787f1e79f44375445297a17`, blob `b92022c74ef903f4926871255d486c0147646b2b`.
- Work package (official FAQ reconciliation, correction, regression guard) = 100% pending CI. Raw workbook acquisition/series mapping = 0%. No values used. Overall V11.3 progress remains NOT CALCULABLE.


### Final CI verification for section 14
- CI Run `43373473191`: SUCCESS; 31 tests passed in 0.022s; 0 failures/errors. https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/43373473191 .
- Section 14 source/metadata correction + QA + CI = 100%. Actual workbook download and exact series mapping remain 0%; no raw data acquired.


## 15. NSE FII/FPI–DII official download-control and provisional-semantics audit (2026-11-13)
- Re-inspected official NSE FII/DII report page. It exposes two distinct CSV controls: NSE-only Capital Market and combined NSE+BSE+MSEI Capital Market. Browser extraction and generic link click do not reveal actual CSV href/final URL; exact URLs remain UNKNOWN. No CSV bytes or SHA-256 acquired.
- Official page confirms provisional data; FII/FPI activity is PAN-based from NSDL, may change after custodial confirmation/modifications, and can include expiry-day physical settlement obligations. DII classification is based on Trading Member-entered trading codes and client category uploaded with UCC details. It is not a depository-confirmed holdings/flow measure. NSE points to NSDL/CDSL for final FPI data.
- Page-rendered examples dated 09-Oct-2026 (NSE-only) and 30-Oct-2026 (combined) are display snapshots only; NOT ingested as raw observations.
- Source register commit `f80ad3a19f984b45b85cc1d5367f5604c829f2b4`, blob `18c7e21cb8850568f380abc8d4799309240672e5`.
- QA guard commit `2aff3cba3292f53c7e121a48676cbd35e40eece7`, blob `d89721d5bf9381b802192c6086a19874fd006d88`.
- Work package (official semantics/download-control reconciliation + regression) = 100% pending CI; exact href/raw bytes/history panel/final FPI reconciliation = 0% / UNKNOWN. No production use.


### Final CI verification for section 15
- CI Run `43374184518`: SUCCESS; 32 tests passed in 0.027s; 0 failures/errors. https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/43374184518 .
- Section 15 defined work package (official NSE page semantics + download-control audit, register, QA and CI) = 100%. Actual CSV acquisition and historical panel = 0%; exact CSV URLs remain UNKNOWN.
