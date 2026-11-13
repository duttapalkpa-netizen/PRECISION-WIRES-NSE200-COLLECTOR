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


## 16. CDSL custodian-confirmed FPI daily flow qualification (2026-11-13)
- Official CDSL daily page inspected; reporting date 12-NOV-2026. CDSL says daily values are based on reports submitted to depositories by custodians on reporting date and represent trades on/up to previous trading day(s). Treat reporting date as publication date, not same-day trade date; exact underlying date window UNKNOWN.
- Daily table separates Equity, Debt-General, Debt-VRR, Debt-FAR, Hybrid, Mutual Funds, AIFs and Stock Exchange vs Primary market & others. For equity cash flow, use the Equity subtotal only after verifying route components; do not use grand Total (includes non-equity buckets, Mutual Funds and AIFs). Primary market & others includes corporate-action and non-secondary-market items; keep separate. Hybrid includes REITs/InvITs.
- CDSL conversion uses RBI reference rate for trading day (previous working day for bank holiday); preserve INR crore raw value and conversion metadata. Derivatives report is separate and must not be mixed with cash equity flow.
- CDSL explicitly distinguishes exchange provisional trading-member data from custodian-confirmed trades submitted to depositories. Preferred official validation/reference route; not zero-lag signal. CDSL public daily view accessible; raw downloadable file URL/bytes/size/retrieval time/SHA-256 not acquired. No display values ingested.
- NSDL listing has stale website-updated marker (05-Oct-2020) and a reproduction/redistribution restriction; do not scrape or redistribute without current terms review. CDSL preferred for this checkpoint.
- Source register commits `76fc10d6fc260b898f441645905f239ef81c2ab4` (initial) and `24a35e171796377256f379771d3fdcb9ea337e67` (numeric display removal/correction); final blob `73d342e2c067d182cda3a47a77791a5cc26be03e`.
- QA guard commit `2b044df94d855230c35d80318a8781295ccc8483`, blob `de6ae8e3b3fea88a89d8af9fd4edec9014ebd7a6`.
- Defined source qualification, reporting-lag and bucket semantics work package = 100% pending CI. Raw file/period mapping/historical panel = 0% or UNKNOWN. No observations or signal imported.


### Final CI verification for section 16
- CI Run `43374624974`: SUCCESS; 33 tests passed in 0.021s; 0 failures/errors. https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/43374624974 .
- Section 16 source qualification + methodology/lag/bucket QA + CI = 100%. Raw export/hash and exact trade-date mapping remain NOT ACQUIRED/UNKNOWN.


## 17. CDSL daily report arithmetic reconciliation — 12-NOV-2026 live snapshot (2026-11-13)
- Official CDSL page opened on 13-Nov-2026; displayed report date 12-NOV-2026. Recalculated bucket totals using exact decimal arithmetic: equity +14,693.72; debt-general +445.65; debt-VRR -173.22; debt-FAR +1,022.81; hybrid +34.86; mutual funds +9.59; AIF -5.20 (INR crore). Sum = +16,028.21, matching published Total.
- Gross purchases bucket sum = INR 36,138.01 crore; gross sales sum = INR 20,109.80 crore; both match published grand totals. USD net sum = 1,708.6278m, rounds to published 1,708.628m. Arithmetic PASS within published precision.
- This is a live page snapshot arithmetic QA only, not immutable raw-file provenance, trade-date verification, custodian completeness proof, or predictive validation. Do not ingest it as historical panel data. Reporting date still covers previous trading day(s), not necessarily same-day trades.
- Source register commit `af62d3a9144c0e0c0222aa939af236faa4f9a4cf`, blob `e021dd9db60dac765be4034304e8218042e1171a`.
- Decimal arithmetic regression commit `9d465a4af307760aba6043b25a5cbe9ceb4ff370`, blob `93e2d70bfcf324dcceeaa3e47ec6b4c6540dec90`.
- Work package (snapshot arithmetic reconciliation + exact-decimal regression) = 100% pending CI. Raw export/archive/hash and exact underlying trade-date mapping remain NOT ACQUIRED/UNKNOWN.


### Final CI verification for section 17
- CI Run `43374862590`: SUCCESS; 34 tests passed in 0.035s; 0 failures/errors. https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/43374862590 .
- Section 17 snapshot arithmetic and exact-decimal regression = 100%. Raw source file/hash and trade-date mapping remain pending.


## 18. CDSL historical Daily Trends archive route and coverage boundary — 2026-11-13
- Official archive landing page inspected: https://www.cdslindia.com/Publications/ForeignPortInvestor.html (page metadata: last updated 05-Nov-2026). The New Format Daily Trends list exposes dated report links from 02-Sep-2024 through 04-Apr-2025; latest listed daily item = 04-Apr-2025.
- Followed official 04-Apr-2025 link; exact resolved XLS target: https://www.cdslindia.com/downloads/Publications/Latest/latest_04042025.xls . Browser retrieval refused the XLS content type; direct transfer attempt also failed before bytes were obtained. URL verified; raw XLS bytes, size, headers, retrieval timestamp, SHA-256 and workbook contents NOT ACQUIRED.
- Current live daily page is a separate view and does not prove historical archive coverage after 04-Apr-2025. No live snapshots, search snippets, monthly/fortnightly/quarterly values, mirrors or guessed filenames used as backfill.
- Archive labels are report dates; exact underlying trade-date mapping remains UNKNOWN because CDSL daily reports cover trades on and up to previous trading day(s), and raw file notes/metadata were not inspected.
- Source register: commit ebd24cdc15fd2b05287256c93b2a74aef24c930c; blob e3ff04d629cfc3c1be9847930c65f4a43953dfe1.
- QA regression: commit 10b8ee7d442369006e9149ab9eec10db72da019c; blob 688312e06d25e6d77f8730d6108351adcde91d48. CI pending at ledger write.
- Defined work package (official archive route + one exact file link + visible coverage boundary + fail-closed QA guard) = 100% after CI. Raw XLS acquisition/hash = 0%; historical daily coverage after 04-Apr-2025 = NOT VERIFIED; trade-date mapping = UNKNOWN; historical panel = 0%.
- No production changes, no PR/merge, no change to selector, RANKING_SCORE, +1 PRESSURE_FADE, 672 diagnostics, engines or Hard Gate.
- Overall V11.3 progress remains NOT CALCULABLE until full weighted acceptance ledger is reconciled.


## 19. CDSL fortnightly sector-wise FPI report — frequency and measurement qualification (2026-11-13)
- Official CDSL archive lists fortnightly sector reports through 31-Oct-2026; separate New Format Daily Trends archive list ends 04-Apr-2025. Fortnightly reports do not establish daily continuity.
- Opened official 31-Oct-2026 report: https://www.cdslindia.com/publications/FII/FortnightlySecWisePages/Oct%2031%202026.html . It explicitly separates AUC at 15-Oct, net investment 01–15 Oct, net investment 16–31 Oct, and AUC at 31-Oct. AUC is stock/position, not flow.
- Table contains 23 sector rows plus Others and Grand Total; sector taxonomy is BSE common industry classification adopted by NSE/BSE from 30-Apr-2022; unclassified issuers outside approximately 4,800 classified issuers are Others. No issuer-level flow inference or automatic mapping to NIFTY indices.
- Coverage breaks: Debt-VRR net investment/AUC included from 30-Apr-2020; Debt-FAR, Mutual Funds and AIF AUC from 31-Aug-2024; their net investment from 15-Sep-2024.
- Fortnightly USD conversion uses end-of-period RBI reference rate; keep INR crore primary and do not compare USD values directly with daily conversion basis.
- Official monthly calendar page displays 2026 monthly net investments and the custodian/DDP previous-trading-day(s) caveat, but footer still says last updated 20-May-2020. Treat footer as page metadata, not current observation vintage. No monthly raw export or bytes obtained.
- Source register commit 7a792d40818d5a28e490a0e125fa6852b3733fc8, blob 2d5ff874de9d6875dd0ec05faf462f6997f01768.
- QA guard commit 65552bb726eb89737f18d59898f24a66236843c9, blob 2d4a14d90941c5a90428f10e88e3a15b325158a5. CI pending.
- Defined source/methodology/frequency qualification = 100% pending CI. Raw report bytes/hash and machine-readable extraction = 0%; sector-to-stock bridge = UNKNOWN; predictive validation = NOT DONE; production use = NOT AUTHORIZED.
- No production changes, no PR/merge, no protected invariant changes. Overall V11.3 progress remains NOT CALCULABLE.


### Final CI verification for section 19
- First run `43375757182` on the source-register change: SUCCESS, before the new regression assertion was added.
- The first regression run `43375779011` failed on an overly exact wording expectation; correction attempt `43375867329` still failed because the assertion did not preserve the source's capitalization. These were test-assertion defects, not source-data failures.
- Corrected the assertion to match the exact persisted register wording. Final CI Run `43375956310`: SUCCESS; 36 tests passed in 0.030s; 0 failures/errors. https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/43375956310 .
- Final QA commit: `d76ef4ef7e52df7a81c4cd0e665aedfc1d5cbad6`, blob `52e38336169ba879505c01c13781f7697e34e088`.
- This CI PASS verifies the fail-closed documentary guard only; it does not acquire CDSL raw XLS bytes, validate the raw report, create a sector panel or validate predictive edge.


## 20. BSE industry-classification hierarchy qualification for CDSL fortnightly sector bridge — 2026-11-13
- Inspected official BSE Industry Classification Structure PDF: https://www.bseindia.com/Downloads1/India_Industry_Classification_Structure.pdf . It defines MEI_CODE, SECT_CODE, IND_CODE, BASIC_IND_CODE and definitions. It is a taxonomy hierarchy/dictionary, not an issuer membership list.
- BSE legacy Industry_Classification.aspx page returned 403 to this retrieval. No dated issuer-to-code membership file, stable identifier mapping, effective dates, or NSE/BSE security master join acquired. Do not interpret 403 as proof no such file exists.
- CDSL 31-Oct-2026 report route renders an HTML sector aggregate; retrieved HTML page exposes no separate binary download link. Raw report binary/hash remain NOT ACQUIRED.
- CDSL 23 named sectors + Others cannot be assigned to issuer securities from taxonomy labels alone. Others must not be redistributed. Similar names are not a verified crosswalk.
- Source register section 20 commit f9945a35f104379e83f4ce3717a90d013a5e44cd, blob d2ff913ae02d74bdeea95bbe5f7c5201fc2f0297.
- QA fail-closed regression commit 8cd3694c83164d09415ff6e296754294385fc1d1, blob 53ade65378b2294944908ebe75cb89717b2d6892.
- Acceptance: official BSE hierarchy dictionary = VERIFIED; issuer membership + effective dates = NOT ACQUIRED; CDSL raw binary export = NOT ACQUIRED; sector-to-issuer bridge = UNKNOWN; taxonomy crosswalk = PARTIAL/NOT VALIDATED; NSE security mapping = UNKNOWN. No synthetic mapping/data ingestion/predictive use/production authorization.
- Defined source hierarchy and bridge-boundary qualification = 100% pending CI. Actual issuer bridge = 0%; CDSL raw file/hash = 0%; sector-panel extraction = 0%; predictive validation = NOT DONE.
- No production changes, no PR/merge, no protected invariant changes. Overall V11.3 progress remains NOT CALCULABLE pending full weighted acceptance-ledger reconciliation.


### Final CI verification for section 20
- CI Run 43377552716: SUCCESS; job 131727465554; 37 tests passed in 0.019s; 0 failures/errors. https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/43377552716 .
- Branch compare after this work: 75 commits ahead, 0 behind main; research-only branch. No PR opened or merged.
- CI validates the fail-closed documentary guard, not actual issuer membership, CDSL raw report bytes, a machine-readable panel or predictive performance.


## 21. NSE Indices issuer-classification source and bulk-membership gap — 2026-11-13
- Opened official NSE Industry Classification page https://www.nseindia.com/static/products-services/industry-classification . It documents four levels and says assignment is primarily based on audited consolidated annual revenue; classification is reviewed annually and may change after significant corporate events. It is methodology, not a dated complete membership file.
- BSE common taxonomy PDF https://www.bseindices.com/Downloads/India_Industry_Classification_Structure.pdf contains hierarchy codes and definitions, not issuer identifier membership rows.
- Official-source search found individual issuer disclosures containing classifications, but no complete machine-readable effective-dated issuer roster or API contract. Individual issuer reports cannot be scraped into an assumed complete universe; missing issuers cannot be inferred.
- Required minimum bridge fields: stable identifier (prefer ISIN plus exchange symbol/security code), classification codes, valid_from/valid_to or dated snapshot, publication/vintage timestamp, and universe coverage. NSE/BSE roster equivalence remains UNKNOWN.
- Source register section 21 commit c9e88e11d4cd4b87d86828f68293f40399822c80, blob 035e0f972c500838963da46b02993e9e6434ed34.
- QA fail-closed regression commit 17e98314f3c39f4372a1ff6d531c053f83500281, blob e9c80c9bc1ff9a0183668dfd1884893a900d3716.
- Acceptance: NSE methodology = VERIFIED; BSE hierarchy = VERIFIED; complete issuer membership = NOT LOCATED/NOT ACQUIRED; historical effective-dated roster = NOT LOCATED/NOT ACQUIRED; CDSL sector-to-issuer bridge = UNKNOWN. No issuer mappings constructed, no synthetic join, no ingestion, no production use.
- Defined source/methodology/coverage-gap qualification = 100% pending CI. Complete issuer roster acquisition = 0%; historical point-in-time mapping = 0%; CDSL panel bridge = 0%; predictive validation = NOT DONE.
- No production changes, no PR/merge, no protected invariants changed. Overall V11.3 progress remains NOT CALCULABLE pending full weighted acceptance-ledger reconciliation.


### Final CI verification for section 21
- CI Run 43378035122: SUCCESS; job 131729029308; 38 tests passed in 0.021s; 0 failures/errors. https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/43378035122 .
- This verifies only the fail-closed source/coverage guard. It does not create the missing official issuer roster or a CDSL-to-stock bridge.


## 22. Official NSE/BSE security-master identifier bridge candidate — 2026-11-13
- NSE official equity availability catalogue exposes exact CSV target https://nsearchives.nseindia.com/content/equities/EQUITY_L.csv; CSV retrieval refused text/csv content type, so no bytes/schema/row count/hash acquired. Catalogue page updated 09-Nov-2026; not assumed to be file vintage.
- NSE All Reports distinguishes MII security gzip for NSE-listed-only versus NSE-listed + BSE-exclusive universes. NSE master spec identifies daily security.txt header/version/date, token, symbol, series; token is symbol-series scoped, not permanent issuer key.
- BSE Standardised Security Master format specifies dated BSE_EQ_SCRIP_DDMMYYYY.csv with Scrip Code, Instrument Code, Scrip Name and ISIN. No industry classification or classification validity interval in inspected schema.
- ISIN is a security-level join candidate; names/symbols alone prohibited. Token/Scrip Code are exchange-local. ISIN alone may not unify issuer across multiple securities/share classes without separate issuer relation.
- Source register section 22 commit 97acf8360e91e5da34b4f016664bcfb6aabca08a, blob b26cfcc1901713a2f87ab7327f8efe42166fcc5e.
- QA fail-closed regression commit d0deba9549fe56bc260882a32fbb4f228d39407e, blob c4cc1b13bb1bc98148d538d54f5339e535805f8a.
- Acceptance: NSE/BSE security-master schemas = VERIFIED at documentation level; raw file bytes/hash/schema = NOT ACQUIRED; cross-exchange ISIN reconciliation = NOT DONE; issuer-to-industry membership = NOT ACQUIRED; CDSL sector-to-stock bridge = UNKNOWN. No data ingestion or inferred mapping.
- Defined identity-schema/source-boundary qualification = 100% pending CI. Raw NSE/BSE master acquisition = 0%; cross-exchange identifier reconciliation = 0%; issuer classification roster = 0%; CDSL sector bridge = 0%; predictive validation = NOT DONE.
- No production changes, no PR/merge, no protected invariants changed. Overall V11.3 progress remains NOT CALCULABLE pending complete weighted acceptance ledger.


### Final CI verification for section 22
- CI Run 43378544793: SUCCESS; job 131730665642; 39 tests passed in 0.021s; 0 failures/errors. https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/43378544793 .
- CI validates source/identifier-boundary regression only. It does not download the NSE/BSE master files, hash them, reconcile ISINs or create industry membership.



## 23. BSE 2026 security-master schema change and NSE dated MII report-scope verification — 2026-11-13
- BSE Notice 20260422-15 (22-Apr-2026) revises Field 24 to CAS Indicator (Char(1), ISO `ElgbltyClsgAuctnSsn`, 0/1) and renames Field 59 ISO tag from `Rsyd01` to `XchgExclsv` while retaining BSE Exclusive flag and Char(1) type. Effective end-of-day 31-Jul-2026. Do not assume raw CSV header/position beyond the notice; raw-file parser validation remains required.
- NSE All Reports catalogue inspected 13-Nov-2026 lists two distinct MII universes: NSE Listed only and NSE Listed + BSE Exclusive. Latest displayed example `NSE_CM_security_11112026.csv.gz` for each has different displayed sizes (1.22 MB vs 1.49 MB). Do not conflate them.
- NSE EQUITY_L.csv direct download attempt failed; separate HTTPS attempt failed at DNS resolution in the execution environment. No bytes/hash acquired. This does not establish source absence.
- No current official BSE dated master download URL/bytes acquired; no guessed URL or third-party provider used.
- Source register section 23 appended; QA fail-closed regression added. CI verification pending.
- Acceptance: BSE schema change/effective date and NSE report-universe distinction = VERIFIED; raw NSE/BSE bytes/hash = NOT ACQUIRED; BSE parser compatibility = NOT TESTED; ISIN reconciliation = NOT DONE; issuer classification roster = NOT ACQUIRED; CDSL sector-to-stock bridge = UNKNOWN.
- Defined schema/report-scope qualification = 100% pending CI; raw acquisition = 0%; parser validation = 0%; cross-exchange reconciliation = 0%; issuer roster = 0%; CDSL bridge UNKNOWN.
- No ingestion, inferred mapping, predictive claim, production integration, PR or merge. Protected invariants unchanged; overall V11.3 progress remains NOT CALCULABLE.

Official references: https://www.bseindia.com/markets/MarketInfo/DownloadAttach.aspx?attachedId=20260422-15 ; https://avantiscdnprodstorage.blob.core.windows.net/legalupdatedocs/55077/BSE-issued-a-notification-regarding-an-update-in-the-enhancement-in-the-Scrip-Master-File-format-April232026.pdf ; https://www.nseindia.com/all-reports ; https://nsearchives.nseindia.com/content/equities/EQUITY_L.csv .


### Section 23 repository persistence and CI status
- Source Register commit: `efe85124d2fa7bcc3c5a1195f5c059a890ad3d6e`; blob `10c7b107c02d1129436a3b2bc4cc10f678845739`.
- QA regression commit: `88b1f75426062236f4eabe1108c171b0e39fc19a`; blob `c255e76ee67b97d025ff7dd578f3fe4f6ff6f259`.
- Ledger section 23 commit: `9ad44c5035bbe5b5dab928b2d35090b9ad7ababa`; blob `c413524e5733d393c4a64ed29f52e3b92c7a34c6`.
- The workflow is configured for push to this research branch when the QA file or source register changes, with a 5-minute timeout. The QA push should trigger it; run ID/result was not accessible through the available GitHub Actions read actions in this session. Therefore CI status = PENDING / NOT VERIFIED; do not mark section 23 CI PASS until a run result is inspected.
- No PR opened or merged; no production selector/ranking/pressure-fade/672-diagnostic changes.


## 24. Exchange security-master raw-file intake validator — 2026-11-13
- Next-step selection: raw NSE/BSE master downloads were already attempted and failed; no duplicate network/download attempt was made. Built a reusable local intake validator so the next uploaded/acquired raw file can be audited reproducibly without assuming exchange schema.
- Added `pipeline/security_master_intake.py`: exact-byte SHA-256 and byte size before decompression; gzip magic detection and integrity check; UTF-8-BOM handling; delimiter detection; header checks; row count, blank rows, row-width errors, explicit ISIN-column duplicate counts. Structural status is not source authentication or schema certification.
- Added QA regression tests for raw-byte hashing, gzip magic, duplicate ISIN counts, false .gz rejection and ragged-row failure.
- Repository commits:
  - Validator: `0d20a9eb04baeb7fac23a42c301ee18ff72f7ceb`.
  - QA tests: `584b3d1f3f97dbf4c0bbd9a76e7f9a19dbc62a47`, blob `6af3ff745e1b0eed76ae275e790aac04c1c31aa9`.
  - Source register: `15a2cf1f525cfd5653fe1b1ef7ddbc2aae54ccfc`, blob `1beafb41dd55026b96bbc22f2c4d557fff227930`.
- Workflow is configured to trigger on QA/source-register push. CI run ID and result have not been retrieved; status PENDING / NOT VERIFIED. Do not claim tests passed until run output is inspected.
- Work-package progress: validator implementation/persistence 100%; regression test authoring/persistence 100%; CI execution verification 0% pending run inspection; raw NSE/BSE file acquisition 0%; exchange-specific schema certification 0%; ISIN reconciliation 0%; issuer/industry bridge 0%.
- Overall project progress: NOT CALCULABLE; the full weighted acceptance ledger has not been reconciled. Hard Gate remains BLOCKED. No production selector, RANKING_SCORE, +1 PRESSURE_FADE, 56×12=672 diagnostics, Engines A–E or Hard Gate logic changed. No PR/merge, no paid API, no spend, no synthetic rows/timestamps.


### Section 24 QA fixture correction — 2026-11-13
- Review of the newly added ragged-row test found its original two-record fixture could make Python's `csv.Sniffer` reject the delimiter before row-width validation. This was a test-fixture weakness, not a production-parser defect.
- Replaced the fixture with a consistent three-column header, two well-formed rows and one ragged row, allowing delimiter detection to succeed and the intended row-width rejection to be exercised.
- Corrective QA commit: `e793033ded8863276aedc163ee729e34971cd110`, blob `1ce4a4f98d5fbb1fd3d20c7dc2de7e8d3129eb72`.
- CI result remains PENDING / NOT VERIFIED; the GitHub connector's commit-workflow-runs action returns PR-triggered runs only and returned no runs for the QA commit. No run ID has been verified. No CI PASS claim.


### Section 24 delimiter-inference defect correction — 2026-11-13
- Additional adversarial review found the original use of `csv.Sniffer` could fail on the very ragged-row input the intake validator must diagnose. The earlier fixture correction alone did not eliminate this parser-level weakness.
- Replaced Sniffer with conservative repeated-field-count voting over up to 40 nonblank lines and comma/pipe/semicolon/tab candidates. It requires at least two consistent multi-column records and rejects ambiguous ties; malformed rows remain visible to the row-width counter.
- Focused local checks: (1) comma CSV widths 3,3,2,3 selects comma and reveals one malformed row; (2) pipe-delimited three-column sample selects pipe; (3) two-row comma CSV selects comma. These are local focused checks, not full suite or GitHub CI.
- Parser hardening commit: `7f61ac0d29fcef6426988c2d73deef7245f8e6eb`, blob `7ba5a000e82d6174cda98f9bfbc13ad477eb20af`.
- Source Register follow-up: `28b3ef2dfb04bbf41e40595cedc6f3694ccf9eab`, blob `3440a77a41a03cccbfeed78582bb5c7b33de3d80`.
- CI result remains PENDING / NOT VERIFIED. The available GitHub run-list connector does not expose push-triggered workflow runs; no run ID or conclusion is asserted. No external paid service, data download, PR or merge.
- Section 24 progress: parser implementation 100%; QA regression fixture persisted 100%; local delimiter-focused checks 100%; full test-suite execution 0% pending; GitHub CI verification 0%; raw NSE/BSE file acquisition 0%; exchange-specific schema certification 0%.
- Overall V11.3 progress remains NOT CALCULABLE; Hard Gate BLOCKED. Production selector, RANKING_SCORE, +1 PRESSURE_FADE, 672 diagnostics, Engines A–E and Hard Gate logic unchanged.

- Added an explicit pipe-delimited regression test to ensure the parser does not silently assume comma-separated input. QA commit: `f0224936f09d1ca26656535191064651ea11d863`, blob `28f35489af9a409d2a4fe676c77646acda56e865`. Workflow trigger should execute on this QA push; run result remains unverified with the available connector.

 
### Section 24 follow-up — validator runtime defect correction (2026-11-13)
- Reinspection of the persisted generic security-master intake validator exposed two implementation defects missed by earlier focused delimiter checks: the return payload referenced undefined `dialect.delimiter` although delimiter inference used a local `delimiter` variable; the tab candidate was written as a literal backslash-plus-t rather than the actual tab character.
- Corrected both defects. Validator commit: `95b106d04a084c9ba2833cfa6ea66eb84cd55816`; blob: `5cae180e1f279215e6926a538e8be799896c98eb`.
- Added tab-delimited and cross-format delimiter-report regression tests; repaired existing intake QA fixtures that encoded literal backslash-n sequences instead of actual line breaks. QA commit: `28d642007055e4f621327ca864d85d95cabd06b9`; blob: `623e561da19816ddf293eeeceb6fee719b422b84`.
- Updated workflow path filters to include `pipeline/security_master_intake.py`, so future validator-only changes trigger this research QA workflow.
- Important correction: earlier focused delimiter checks did not exercise the complete report-return path; they must not be interpreted as validator PASS. Full unittest suite and GitHub Actions result remain PENDING / NOT VERIFIED until an actual run and logs are retrieved.
- No NSE/BSE raw master bytes acquired; no publisher authentication, exchange-specific schema certification, or cross-exchange ISIN reconciliation. No production integration, PR, or merge.
- Section 24 progress: identified/corrected code defects 100%; QA regression definitions persisted 100%; workflow path coverage updated 100%; full test-suite execution 0% pending; GitHub CI verification 0%; official raw-file acquisition 0%; exchange-specific schema certification 0%.
- Overall V11.3 progress remains NOT CALCULABLE; Hard Gate BLOCKED. Production selector, RANKING_SCORE, +1 PRESSURE_FADE, 56×12=672 diagnostics, Engines A–E, and Hard Gate logic unchanged.

- Follow-up QA inspection caught and corrected escaped fixture literals in the newly added tab/delimiter regression cases so test inputs contain actual tab characters and actual line breaks (not backslash sequences). Corrective QA commit: `23698e40feb62b2b8a6f188cfb9626f8db646d38`; blob: `0407fee5edadb44459144b3f52f4cab2f28f9bb7`. This correction is recorded separately; no test execution is implied.

 
### Section 24 follow-up — strict CSV quoting (2026-11-13)
- Additional fail-closed review found Python's default CSV reader is permissive about malformed quoted records. Both delimiter sampling and full-row parsing now use `strict=True`; malformed quoted CSV raises `csv.Error` rather than being structurally accepted.
- Validator commit: `7206989479284205bcee24afbfd9c4923c8d2e30`; blob: `75246bc91d84da293100532bb4061d4b69523dfb`.
- Added malformed-quote regression test and corrected its test fixture to use actual line breaks. Final QA commit: `eedbee83b9afc019aaf9ec84b13fee4403fc4195`; blob: `86d82597c511f286a173cbda4625d59b2d728a25`.
- Final source files were re-fetched from the research branch; strict parsing and regression fixture are present. Test execution is still NOT RUN here; GitHub Actions result remains NOT VERIFIED because the available connector exposes only PR-triggered commit runs and has no workflow-dispatch/list-push-run action.
- No raw NSE/BSE file bytes acquired; no exchange schema certification, cross-exchange reconciliation, PR, merge, or production change.

 
### 2026-11-13 follow-up — QA execution boundary and repository visibility check
- Rechecked current repository metadata: GitHub reports `visibility=public`. This conflicts with the previously recorded user requirement to keep the research repository private. No visibility-change action is exposed by the connected GitHub tools; no change is claimed. User action required in GitHub repository Settings → General → Danger Zone → Change repository visibility → Make private. This should be treated as an urgent governance item. Making the repository private does not revoke existing clones or forks.
- Rechecked combined commit status for latest Source Register commit `5a978c7bb7ce4561eb036a40e2e3977c92335e74`: no status entries returned. This is NOT a test pass.
- Available GitHub connector does not expose a workflow dispatch or repository-wide push-run listing action. `fetch_commit_workflow_runs` is explicitly PR-triggered-only; no run ID or CI conclusion can be verified. Full test suite remains NOT RUN / NOT VERIFIED.
- The latest validator and QA source files are persisted: validator blob `75246bc91d84da293100532bb4061d4b69523dfb`; QA blob `86d82597c511f286a173cbda4625d59b2d728a25`. No test outcome is inferred from source presence.

 
### Section 24 follow-up — tab delimiter and blank-only input correction (2026-11-13)
- Reinspection of the persisted parser found the tab delimiter candidate still encoded as the two-character sequence backslash+t, despite the tab regression test expecting an actual tab. This is now corrected to the actual tab character. A separate guard now rejects whitespace-only payloads with a controlled `ValueError` instead of leaking `max() arg is an empty sequence`.
- Validator commit `64aad36ed09688716dcf7b5c30cdffedf9dfcbd8`; blob `bb15dd80ccba3933f147967b5df6b995c5ec923a`.
- Added blank-only input regression; corrected its fixture after review to use actual whitespace/newline characters. Final QA commit `69fb2a1bb6c5f670f144d9135b3f2c2c5801e0a8`; blob `f929f8b6a0f4225577d2306dd6c2a69b148983fa`. QA file currently contains 49 test methods.
- Re-fetched source confirms actual tab candidate and blank-only guard. Workflow path filter includes `pipeline/security_master_intake.py`. Full suite has NOT been executed; no test or CI pass is claimed.
- Earlier assertions that tab detection was fixed are superseded by this correction; previous persisted test fixture itself also required correction. Do not mark tab parsing PASS until the actual suite executes.
- No raw NSE/BSE master bytes acquired; schema certification, cross-exchange ISIN reconciliation and issuer/industry bridge remain pending/unknown. No production change, PR or merge.

 
### Section 24 correction — final tab-candidate encoding audit (2026-11-13)
- A source-character audit (not visual inspection) showed the prior parser line still contained the two literal characters backslash and `t`, not a tab. Earlier progress statements claiming the tab candidate was fully fixed were therefore premature. Corrected the candidate list to use `chr(9)`, eliminating source-escaping ambiguity.
- Validator commit `86edc76f30a04fc78408cc45af2c46d1456a9c7e`; blob `a625908d5701f5f95a717582dcf10913f1cbbb08`.
- Existing QA tab test uses Python's `\t` escape in source, which produces a real tab at runtime; test definitions remain 49. QA blob `f929f8b6a0f4225577d2306dd6c2a69b148983fa`.
- Re-fetched source confirms candidate line uses `chr(9)`. This is source verification only; full QA execution and CI are still NOT RUN / NOT VERIFIED.
- Official Python CSV documentation confirms `csv.reader` supports a one-character delimiter and that `strict=True` raises `csv.Error` on malformed CSV; see https://docs.python.org/3/library/csv.html. This documents the parser contract, not test execution.
- No raw NSE/BSE bytes, schema certification, cross-exchange reconciliation or issuer bridge acquired. No production changes, PR or merge.

 
### Section 24 follow-up — logical-record CSV delimiter inference (2026-11-13)
- Adversarial review identified a remaining parser limitation: delimiter voting split physical lines, so a valid quoted field containing an embedded newline could be treated as multiple records or cause delimiter sampling to fail. Python's official CSV documentation confirms quoted fields may contain newlines and that readers should consume a file-like stream opened with `newline=''`.
- Replaced physical-line sampling with per-candidate `csv.reader(io.StringIO(text, newline=''), strict=True)` over logical records. It counts up to 40 nonblank records, retains ragged-row visibility, and rejects ambiguity; malformed quoting remains fail-closed.
- Validator commit `fa65175e011c36711b94193513a0b7507c2cae72`; blob `b97516e076c60a0b4e659ccc0fd7606c0c79fb80`.
- Added quoted multiline-field regression test. QA commit `1db674e9ce57e20953432c0a622a00336a2bb074`; blob `7260b5210b5171a6facdb132b0b2470e9fd78520`. Test definition is persisted; full suite has not been executed.
- Source Register/ledger updates pending this entry; no source-data acquisition, schema certification, production integration, PR or merge.


### Section 24 follow-up — CI failure diagnosis and verified correction (2026-11-13)
- Push CI run `43436158714` on `be176e05a753afbbf84c588fdb0ca4903615e457` executed all 50 tests: 48 passed, 1 failed, 1 errored. Logs identified (1) blank-only whitespace input reached delimiter ambiguity instead of the controlled `no nonblank CSV records` error, and (2) multiline regression fixture encoded literal backslash-n text rather than actual newline characters.
- Corrected validator to reject `not text.strip()` before delimiter inference: commit `ad5037a9825313422f3faf7dc8aa89aa8ee0237f`, blob `2e2f48eeeab3d9a05b0e7f5e5499ae8c3c326cbf`.
- Corrected multiline test fixture to use actual newline escapes: commit `b24395ac514d88ffb116d74bb9939ca1f98241a0`, blob `c7a72386f9633b09841e0f1630fa3e2ae24bd01d`.
- Latest CI run `43438875821` on QA commit `b24395ac514d88ffb116d74bb9939ca1f98241a0`: `python -m unittest qa.test_global_capital_rotation_overlay -v` ran 50 tests in 0.083s; both previously failing cases are `ok`; workflow conclusion SUCCESS.
- The earlier run `43438865632` on validator-only commit failed because it started before the corrected QA fixture commit; it is superseded by successful run `43438875821`.
- These are validator unit tests only. No raw NSE/BSE security-master bytes were acquired; publisher authentication, exchange schema certification, cross-exchange ISIN reconciliation and issuer/industry bridge remain NOT ACQUIRED / UNKNOWN. No production selector/ranking/pressure-fade/672-diagnostic changes, no PR and no merge.


### Section 25 — CDSL daily FPI archive retrieval retry and date-boundary reconciliation (2026-11-13)
- Re-opened the official CDSL FPI archive landing page. It reports page metadata `last updated November 05, 2026`; the New Format Daily Trends list's newest dated report remains `04 April 2025`, oldest visible report `02 September 2024` (archive landing page lines 70–356). This confirms the dated archive list does not extend to the 2026 live page.
- Followed official archive item `04 April 2025` (landing-page link 24). Both page navigation and direct file retrieval of `https://www.cdslindia.com/downloads/Publications/Latest/latest_04042025.xls` fail at the retrieval layer with unsupported `application/vnd.ms-excel` content type / download failure. No binary bytes were obtained. No file size, response headers, retrieval timestamp for a successful transfer, SHA-256, workbook sheets, schema, or report contents may be asserted.
- Official current Daily Trends page/search snapshot displays reporting date `11-NOV-2026`; its own explanatory note says custodian-confirmed figures are based on custodian reports and represent trades on and up to previous trading day(s). Therefore reporting date must not be substituted for a specific trade date without report-level evidence.
- Date reconciliation result: dated archive boundary = 02-Sep-2024 to 04-Apr-2025 (visible official list); daily continuity/completeness inside that interval has NOT been machine-counted or proven; post-04-Apr-2025 daily archive coverage = NOT VERIFIED; live snapshot date = 11-Nov-2026; exact underlying trade-date mapping = UNKNOWN. No synthetic gap-fill, inferred filename sequence, mirrors, or monthly/fortnightly substitution.
- Acceptance: official archive boundary and exact 04-Apr-2025 link re-verified; raw XLS acquisition = NOT ACQUIRED; SHA-256 = NOT AVAILABLE; data ingestion = NOT DONE; production use = NOT AUTHORIZED. Stop acquisition attempts at the content-type boundary unless an official browser download or user-supplied original file becomes available.


## 26. Research QA CI run verification and pending-status reconciliation — 2026-11-13
- Reconciled earlier Section 23/24 CI PENDING notes against GitHub Actions push-run listing instead of relying on the PR-only commit workflow lookup.
- Latest verified branch run: 43443062681; head SHA 218119c4d8c549579b06904a655ba9d0ea5d2238; push event; workflow Global capital rotation overlay research tests; job 131945376329 completed SUCCESS.
- Retrieved job log and verified exact command: python -m unittest qa.test_global_capital_rotation_overlay -v. Result: Ran 50 tests in 0.240s; OK; 0 failures and 0 errors. All 50 named tests in the retrieved log report ok.
- Coverage includes NSE/BSE security-master schema/report-universe boundary, BSE hierarchy versus issuer-membership boundary, NSE classification methodology versus effective-dated roster, CDSL daily archive and fortnightly-report boundaries, date-cutoff/vintage/UNKNOWN fail-closed behavior, and security-master intake parser regressions.
- Separate run 43439033905 (head 772fa0109d000be009035fef24b9256c8672cf9e) also completed SUCCESS; job 131931506100. It is not substituted for the latest branch run.
- This closes CI execution-verification gap for the test suite on latest verified head. It does NOT acquire official raw NSE/BSE files, authenticate publishers, certify exchange-specific schemas against raw payloads, reconcile cross-exchange ISINs, create issuer-industry membership, or resolve CDSL sector-to-stock bridge. Those remain NOT ACQUIRED / NOT DONE / UNKNOWN.
- Section 23 CI status may now be marked PASS for verified workflow execution at head 218119c4d8c549579b06904a655ba9d0ea5d2238; do not interpret as data-source acceptance or production validation.
- No production selector, RANKING_SCORE, +1 PRESSURE_FADE, 56x12=672 diagnostics, Engines A-E, or Hard Gate logic changed. No PR opened/merged; no spend, paid API, synthetic data or external contact.
- Work-package progress: CI run discovery 100%; job/step status verification 100%; full test-log inspection 100%; 50-test suite execution 100%; documentation persistence follows this entry. Raw NSE/BSE acquisition 0%; exchange-specific raw schema certification 0%; cross-exchange ISIN reconciliation 0%; issuer classification roster 0%; CDSL bridge UNKNOWN.
- Overall V11.3 progress remains NOT CALCULABLE because full weighted acceptance ledger has not been reconciled. Hard Gate remains BLOCKED.


## 27. NSE active securities CM and debt source discovery — 2026-11-13
- Selected a new official NSE source candidate after checking the Continuity Ledger and Source Register to avoid repeating the prior EQUITY_L.csv/MII security-file audits.
- Official NSE page separately lists “List of Active Securities CM And Debt (.csv)” (displayed 373 KB; page updated 09-Nov-2026). Exact target: https://nsearchives.nseindia.com/content/equities/List_of_Active_Securities_CM_DEBT.csv . A single official link retrieval attempt failed at the gateway with HTTP 400 / unsupported content-type text/csv.
- The active-security list is distinct from the already catalogued Equity-segment available-for-trading CSV and MII security-file universes. Its actual row population and semantics are not yet established. Page display size is not a downloaded byte count.
- Raw bytes, payload schema, row count, ISIN coverage, embedded vintage, successful retrieval timestamp and SHA-256: NOT ACQUIRED / UNKNOWN. No parser, mapping, ingestion or source promotion performed. Identity/universe candidate only; not issuer-industry membership evidence.
- Work-package progress: official page reinspection 100% PASS; distinct catalogue-item identification 100% PASS; exact link resolution 100% PASS; bounded retrieval attempt 100% PASS (access failed); raw payload acquisition 0% BLOCKED; schema/ISIN QA 0% PENDING; historical validity and cross-exchange reconciliation 0% PENDING; issuer-industry bridge UNKNOWN.
- No repeated gateway retries or unofficial mirrors. Reattempt only with official browser download or original user-provided payload; preserve original bytes and SHA-256 before parsing. No spend, paid API, synthetic data, external contact, production change, PR or merge. All invariants remain unchanged.
- Overall V11.3 progress remains NOT CALCULABLE: this single source-discovery checkpoint does not reconcile the full weighted acceptance ledger. Hard Gate remains BLOCKED.


## 28. NSE FII/FPI–DII page freshness and scope checkpoint — 2026-11-13
- Performed a new page-freshness audit using the official NSE report page; did not repeat the previously blocked generic CSV download-link click.
- Retrieved page snapshot exposes NSE-only sample date 09-Oct-2026 and combined NSE+BSE+MSEI sample date 30-Oct-2026. Relative to 13-Nov-2026 these are 35 and 14 calendar days old. Treat as stale rendered examples, not current daily data and not immutable raw observations.
- Official page preserves separate NSE-only and combined scopes and states provisional/custodial caveats. DII is based on trading-member codes and client category, not unique beneficial-owner holdings. Preserve scope and provisional labels; no merge with final CDSL/NSDL data.
- CSV controls exist, but exact distinct final URLs remain unexposed in the link map. No repeated generic click and no raw CSV acquired. URLs, bytes, retrieval timestamps, sizes, hashes, full daily coverage and arithmetic QA remain UNKNOWN / NOT DONE.
- Work-package progress: official page reinspection 100% PASS; scope distinction/semantics verification 100% PASS; visible sample freshness comparison 100% PASS; CSV endpoint resolution 0% PENDING; raw CSV acquisition 0% PENDING; date/schema/arithmetic/calendar QA 0% PENDING; historical matched-panel/event study 0% PENDING.
- No production use, no synthetic data, no paid source, no external contact, no PR/merge. All protected invariants unchanged. Overall V11.3 progress remains NOT CALCULABLE pending full weighted acceptance-ledger reconciliation; Hard Gate BLOCKED.


## 29. NSE 2026 CM trading-holiday addendum reconciliation — 2026-11-13
- New high-value check: reconciled the original NSE CM holiday circular NSE/CMTR/71775 (12-Dec-2025) with official addendum NSE/CMTR/72260 (12-Jan-2026) and current official NSE equities holiday page.
- Original circular omits 15-Jan-2026; later CM addendum explicitly adds Thursday 15-Jan-2026 as a Capital Market trading holiday for Municipal Corporation Election in Maharashtra and says it partially modifies 71775. Current official NSE holiday page also includes this date. Base circular alone is therefore insufficient; addendum is mandatory for the 2026 CM session calendar.
- This correction affects trading-session counts, missing-session checks, H+1/H+3/H+5 horizon indexing, and joins of daily flow/FX inputs. 15-Jan-2026 is not a regular CM trading session. Do not substitute settlement, debt, F&O or SLBS notices.
- Official evidence: https://nsearchives.nseindia.com/content/circulars/CMTR71775.pdf ; https://nsearchives.nseindia.com/content/circulars/CMTR72260.pdf ; https://www.nseindia.com/resources/exchange-communication-holidays?apiversion=v2 .
- Work-package progress: base circular reinspection 100% PASS; addendum discovery/verification 100% PASS; current holiday page cross-check 100% PASS; complete 2026 special-session manifest 0% PENDING; historical multi-year calendar manifest 0% PENDING; reconcile all collected session rows 0% PENDING; recompute rolling H+1/H+3/H+5 windows 0% PENDING.
- Scope is one verified calendar correction, not a complete calendar certification. User-reported 317-session total remains unverified in this task. Muhurat 08-Nov-2026 is a separate Sunday special session and must be handled separately, not as a regular weekday session.
- No synthetic data, forward-fill, ingestion, production changes, PR/merge or spend. Protected invariants unchanged. Overall V11.3 progress remains NOT CALCULABLE pending full weighted acceptance-ledger reconciliation; Hard Gate BLOCKED.


## 30. NSE 2026 Capital Market full-year session calendar and Muhurat special-session manifest — 2026-11-13
- Built a 365-date machine-readable calendar manifest: `data/calendars/NSE_CM_2026_SESSION_CALENDAR_MANIFEST.csv` (365 date rows plus header). Each date is classified as regular CM trading day, exchange holiday, ordinary weekend, or the distinct Muhurat Sunday special session. No market observation rows or synthetic trading dates were created.
- Reconciled the 16 weekday CM holidays against the current official NSE equities holiday page and the base/addendum circular chain: NSE/CMTR/71775 (12-Dec-2025) plus NSE/CMTR/72260 (12-Jan-2026). The addendum's 15-Jan-2026 closure is included; the base circular alone is not sufficient.
- The 16 weekday holidays in the manifest are: 15-Jan, 26-Jan, 03-Mar, 26-Mar, 31-Mar, 03-Apr, 14-Apr, 01-May, 28-May, 26-Jun, 14-Sep, 02-Oct, 20-Oct, 10-Nov, 24-Nov and 25-Dec 2026. NSE page separately lists weekend-dated holidays 15-Feb, 21-Mar and 15-Aug; these remain ordinary weekends with no extra weekday closure. 08-Nov is separately classified as a Muhurat special session, not an ordinary weekday.
- Official CM Muhurat circular NSE/CMTR/76941 dated 19-Oct-2026 was opened directly: https://nsearchives.nseindia.com/content/circulars/CMTR76941.pdf . Sunday 08-Nov-2026 schedule: block deal 13:50–14:05; special preopen for IPO/relisted securities 14:05–14:50; continuous trading opens 14:20; CAS securities regular market close 15:15; non-CAS securities close 15:30; CAS order entry 15:20–15:30, matching 15:30–15:35, transition 15:35–15:50, post-close 15:50–16:00; trade-modification cutoff 16:15. All trades create settlement obligations. Do not treat this session as a normal 09:15–15:30 weekday session.
- Manifest arithmetic: 365 calendar dates; 103 Saturdays/Sundays; 16 weekday exchange holidays; 245 regular weekday CM sessions; 1 distinct Sunday Muhurat special session; 246 total distinct 2026 CM trading dates when special session is included. This is a calendar-derived expected count, not a verified count of downloaded daily observations.
- Official sources: NSE current holiday page https://www.nseindia.com/resources/exchange-communication-holidays?apiversion=v2 ; base holiday circular https://nsearchives.nseindia.com/content/circulars/CMTR71775.pdf ; 15-Jan addendum https://nsearchives.nseindia.com/content/circulars/CMTR72260.pdf ; Muhurat CM circular https://nsearchives.nseindia.com/content/circulars/CMTR76941.pdf .
- Acceptance: official 2026 weekday holiday list reconciliation = PASS; 15-Jan addendum application = PASS; Muhurat special-session identity/timings = PASS; 365-date manifest creation = PASS; arithmetic reconciliation = PASS. This manifest is a calendar specification only; it does not prove actual daily raw-data coverage, trading-day observation continuity, historical multi-year calendar completeness, or backtest indexing.
- Remaining: reconcile the actual locally archived NSE session-date set against this manifest (not yet available/verified in this task); identify any additional official circular amendments after this snapshot; then recompute rolling H+1/H+3/H+5 only after actual date rows and event windows are validated. User-reported 317 sessions remains unverified.
- No synthetic observations, forward-fill, raw market-data ingestion, production changes, PR/merge or spend. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A–E and Hard Gate unchanged; Hard Gate remains BLOCKED. Overall V11.3 progress remains NOT_CALCULABLE pending full weighted acceptance-ledger reconciliation.
