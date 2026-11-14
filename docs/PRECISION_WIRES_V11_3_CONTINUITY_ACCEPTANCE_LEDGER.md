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


## 11. IMF BOP metadata and WEO EMDE membership crosswalk update (2026-11-14; research branch only)
- Research branch: `research/imf-bop-access-audit-v1`; no merge to main and no PR merge.
- IMF BOP metadata run #43590032021 SUCCESS; commit `47c2037de3fe4ff06094803a24e96a5aa5ff24fe`; artifact `14112042284`; ZIP SHA-256 `95aa8c3a730704cd1778ae12b7e5321b6e1c373b0d4eea81b0acfd6448fe1822`.
- IMF BOP DSD/codelist run #43590132930 SUCCESS; commit `8df4589a1171bc74914b577313bd9c65ebc69f02`; artifact `14111193621`; ZIP SHA-256 `60c5485f6dd9538255a1ca364e719a2bc843b68be12d13a7521c5febae84d840`. Direct component inventory: 18 dimensions, 15 attributes, 1 primary measure; 22/22 referenced codelists HTTP 200 + XML parse PASS. First run's recursive XML counts are superseded by the corrected direct-component parser; preserve first run as historical audit.
- WEO EMDE crosswalk run #43598281690 SUCCESS; commit `daa529172a9b55b66202fea7282a07c9bb54912a`; artifact `14114154484`; ZIP SHA-256 `16b59c4356ba31526c4cbc9f3d8796d1cc6d4e9d8fe7f0c6bec486d917cbbe2c`.
- WEO April 2026 appendix page 5 parsed from official PDF: 154 unique EMDE names. Raw PDF SHA-256 `b8a538c3158bf0553a3ae45d4797cd5648cbea684eb4be848a52c1d64d994395`.
- IMF CL_AREA 2.0.0 raw XML SHA-256 `09b5b44664b7d5ae4d41be132c48de01a9d9dcfbd918b6afb49f143adfdec6d4`; 931 English code labels parsed.
- Mapping result: 153/154 unique mappings; zero duplicate code assignments; zero ambiguous matches. “West Bank and Gaza” remains UNKNOWN; no equivalence to “Palestine, State of” (PS) or “Gaza and Jericho” (XG) assumed. India exact mapping IN PASS. Seven explicit reviewed label aliases documented in evidence report.
- WEO-to-CL_AREA crosswalk acceptance: PARTIAL_REVIEW_REQUIRED; full membership mapping gate remains BLOCKED/UNKNOWN pending West Bank and Gaza geography crosswalk decision. Mapping membership is not BOP reporter coverage.
- Failure history preserved: run #43598079002 HTML-table assumption failed because source is PDF; #43598148417 lacked pypdf; #43598156963 stale HTML parser references/uninitialized PDF bytes. Corrected PDF parsing and pinned pypdf 5.9.0; successful run follows.
- Evidence report: `docs/IMF_BOP_METADATA_FIRST_ACQUISITION_EVIDENCE_20261114.md`, commit `6d12d6b5bbd7cc90ab9683e3257c7d30bc76eed6`.
- IMF BOP acceptance-gate progress remains 3/7 PASS (43%); the WEO membership subtask is 153/154 mapped (99.4% mapping coverage) but is NOT an accepted gate because one geography remains UNKNOWN. Do not count a partial subtask as a fully completed gate. Keep work-package progress separate from gate acceptance and production readiness.
- Project-wide verified overall progress: NOT_CALCULABLE until complete acceptance ledger and weights are reconciled. Prior project Hard Gate remains BLOCKED; prior Macro-Geo P0 7/8, Factor Registry 0/35 complete available groups, Historical Regime 9/11, Event Study exploratory/not mature must be revalidated before being stated as current.
- No observation rows acquired; no EM portfolio-flow aggregate calculated; no production integration. Research spend ₹0; no paid API; no synthetic rows or timestamps. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE and CORE-672 unchanged.


## 2026-11-14 — Superseding update: WEO EMDE to IMF CL_AREA crosswalk

This entry supersedes the immediately preceding 153/154 partial-mapping status above. Prior entries and failed-run evidence remain preserved.

- Final workflow Run ID: 43600131132 — SUCCESS; all six workflow steps completed.
- Workflow commit: `9db5d4e7bb14ef9b23321db6918e4f91ae9840f8`.
- Run URL: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/43600131132
- Artifact ID: 14115992695.
- Artifact ZIP SHA-256: `2fcdc5dc4e896791875092bae7bb33c3d7e4d3e3df6eb642c16f9f00bd5d5ac9`.
- Verified final membership: 154 WEO April 2026 EMDE names; 154 unique IMF CL_AREA 2.0.0 codes; 0 unmapped; 0 ambiguous; 0 duplicate code assignments.
- India maps to IN by exact normalized match.
- West Bank and Gaza maps to PS using the official IMF CPIS Data Template, which lists PS as “West Bank and Gaza Strip”; current CL_AREA 2.0.0 labels PS “Palestine, State of”. The separate CL_AREA code XG (“Gaza and Jericho”) is not used. The evidence URL is https://data.imf.org/-/media/iData/External-Storage/Documents/00DA1FBD843040C89781AF28C926168F/en/CDIS-Data-Template.pdf. This is a statistical area-code continuity mapping, not a legal-status assertion.
- Final raw WEO PDF SHA-256: `b8a538c3158bf0553a3ae45d4797cd5648cbea684eb4be848a52c1d64d994395`.
- Final raw CL_AREA XML SHA-256: `98e3d5368a6d2a8fcb93dc274501bdecab478136d7882b49d5c9a592e18f6391`.
- Final crosswalk JSON SHA-256: `91fd83c52efaf0f10c1ad2c275c23b343b607ef628bd0408a9b2edc4d4bbdbc8`.
- Final membership CSV SHA-256: `27f1f996dd84618ce5e7c2137de56b661ce0f4cedb49b2a37677159be6651b85`.
- Artifact was downloaded again; all four files were inspected and their hashes verified. Evidence report: `docs/IMF_WEO_EMDE_CL_AREA_CROSSWALK_AUDIT_20261114.md`, report commit `6ef3e4561b9de4e09d10693e7858415954f56287`.
- The WEO membership and IMF area-code mapping gate is now PASS. On the previously defined seven-gate IMF BOP workstream rubric, this advances accepted gates from 3/7 (43%) to 4/7 (57%). The remaining dataflow-to-registry crosswalk, India BOP observation acquisition/reconciliation, and EM aggregation gates are still UNKNOWN/BLOCKED/NOT_DONE as applicable.
- This membership PASS does NOT establish BOP observation coverage for all 154 economies and does NOT authorize any EM flow aggregate. No BOP observations or aggregate were created.
- Project-wide verified overall progress remains NOT_CALCULABLE pending reconciliation of the full multi-workstream acceptance ledger and current gate weights.
- Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 diagnostics, engines and Hard Gate were not modified. ₹0 spend; free official sources only; no synthetic observations or timestamps.


## 2026-11-14 — IMF BOP Portal-to-SDMX registry crosswalk audit

- New public-source audit Run ID: 43600890212 — SUCCESS; all workflow and artifact-upload steps completed.
- Workflow commit: `1f6be23493e78cbf2c4a4fced7a810b0313597f7`.
- Run URL: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/43600890212
- Artifact ID: 14115559741.
- Artifact ZIP SHA-256: `2ef0f095cc0e0d2b7b1a29a86591ced09bda2d1100b44043c493c18cd005c716`; downloaded again and local digest independently matched.
- Official IMF SDMX Central IMF/all/latest dataflow catalogue: HTTP 200, 101 dataflow objects, raw SHA-256 `547fa36a26e2859301013ea52d05fcbfd99f2cd068afa619696e412bc4760693`.
- Thirteen BOP-related IMF dataflows were inventoried. BOP_GBPM6(2.0) references IMF:BOP(2.0); BPM6_BOP_Q(1.5) references IMF:BOP(1.5); BOP6(1.1) and BOP_BPM6(1.0) reference IMF:ECOFIN_DSD(1.0); other related flows reference DSD versions 1.0, 1.1, 1.2, or 2.0. No BOP-related IMF dataflow in this catalogue references IMF:BOP(2.6.0).
- Official Portal dataset page confirms URN IMF.STA:BOP(21.0.0), HTTP 200, raw SHA-256 `434df7a013e62fa1d0db95d216809f17976480d8c3fc91ca2e0413d96106d9b3`.
- Official IMF API help page confirms SDMX 2.1 and 3.0 APIs, but states Swagger explorer requires beta-portal sign-in. API help raw SHA-256 `7004a1655ea132ea2fe9e39cc11406656dae080d4bbc5d67ecb20e715114855b`.
- Request to https://portal.api.imf.org/apis returned HTTP 200 only after redirect to https://portal.api.imf.org/signin?returnUrl=%2Fapis; captured page SHA-256 `eb094d79d1f431a2020e77b80a3e1aff00e9dfb7a47fe29b7ce8ba0a35324e99`. This is not a public schema or data endpoint. No sign-in or bypass was attempted.
- Crosswalk conclusion remains UNKNOWN: Portal dataset URN IMF.STA:BOP(21.0.0) is not proven to be any listed SDMX Central dataflow. The BOP DSD 2.6.0 registry object is not referenced by any BOP-related IMF dataflow in the captured 101-flow catalogue. Do not infer equivalence from similar names.
- Observation API access remains BLOCKED pending an authorized beta-portal session or an IMF-published public mapping/endpoint. No observations acquired; no EM aggregate calculated.
- Evidence report: `docs/IMF_BOP_PORTAL_TO_SDMX_REGISTRY_CROSSWALK_AUDIT_20261114.md`, report commit `101e631955d9bcb6ab6ab34e0834f47f86cdfdc7`.
- IMF BOP workstream remains 4/7 accepted gates (57%) on the existing rubric: dataset identity, DSD/codelists, direct component inventory and WEO membership mapping are PASS. Portal-to-registry crosswalk UNKNOWN; India observation acquisition BLOCKED/NOT_DONE; EM aggregation BLOCKED.
- The full PRECISION-WIRES V11.3 project percentage remains NOT_CALCULABLE until all workstream gates and weights are reconciled. No current project-wide percentage is asserted.
- No changes to Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, engines or Hard Gate. ₹0 spend; no paid services; no synthetic values/timestamps; no PR merge.


## 2026-11-14 — IMF BOP public client API contract discovery and live endpoint probe

- First-party BOP dataset page and 11 Next.js client chunks inspected using read-only retrieval. Client discovery Run #43601835131 SUCCESS; commit `46dfd2f72312ca48e824515ec7b0d3cf2031ce84`; artifact ID `14117155347`; ZIP SHA-256 `31a0d0add766bc66e928624c18979692045fdb09a10c9fea88f83cf704259963`.
- Official dataset page capture: HTTP 200; 286,324 bytes; SHA-256 `b4c37f5b9bc3013cef59a631acd9d16fd0f828653e1ce75a0361b9c08e63d456`.
- Main first-party client page bundle SHA-256: `b60dc6bfb92b8989965c33b9e17b54704f5df7092f80ba0e26327455424e8dd9`.
- Client bundle contains SDMX 3.0 data-query URL template: `https://api.imf.org/external/sdmx/3.0/data/dataflow/{agencyID}/{resourceID}/{version}/{dimensionKey}?c[TIME_PERIOD]=ge:{startDate}+le:{endDate}&dimensionAtObservation=AllDimensions&attributes=all&detail=full&includeHistory=true&limit=100`.
- Client bundle also constructs structure URL template: `https://api.imf.org/external/sdmx/3.0/structure/dataflow/{agencyID}/{resourceID}/{version}?detail=full&references=all`. This is client source evidence, not a proof of route availability.
- Candidate URN from the BOP page is IMF.STA:BOP(21.0.0). Treating it as agency/resource/version produces a candidate URL path, not a confirmed active SDMX dataflow.
- Two live, unauthenticated structure endpoint probes failed with HTTP 400. Run #43601889079: server message “This endpoint does not support json version 3.0”; response SHA-256 `be55c218632cab1444443c40d1ce720cbc7150a5f403d65aa53ecf62f651ccb2`. Run #43601964709: server message “This endpoint does not support xml version 3.0”; response SHA-256 `59bd7d800cf108ce237613c9419e23d6bc269d23a58432984e14dbed866d7195`; artifact ID `14115719310`; ZIP SHA-256 `613883f8b5102a35451b4830fa275001cc5cf8218a7e70fc7b79d521d302d794`.
- Corrective lesson: a first-party frontend URL template is not proof that the corresponding server route supports the same resource/representation. Test media negotiation before interpreting the response; don't assume a valid data-query route implies a supported structure-query route.
- No dimension metadata was returned; no data query was attempted; no observation rows acquired. No key/dimension ID/order invented.
- Evidence report: `docs/IMF_BOP_PUBLIC_CLIENT_API_CONTRACT_DISCOVERY_20261114.md`, commit `c92ee8d5470bc53ecebdc792069fe5bbe006b3a9`.
- Crosswalk and India observation gates remain UNKNOWN/BLOCKED/NOT_DONE. The IMF BOP workstream remains 4/7 accepted gates (57%) on the existing rubric. The client route discovery does not satisfy the Portal-to-registry mapping gate.
- Project-wide verified progress remains NOT_CALCULABLE pending full acceptance-ledger and weighting reconciliation.
- ₹0 spend; official sources only; no sign-in, credential handling, or auth bypass; no synthetic observations/timestamps; no PR merge; no production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, engine or Hard Gate changes.


## 2026-11-14 — IMF BOP SDMX 2.1 candidate flow, DSD and codelist verification

- Run #43608726175 SUCCESS; workflow commit `eabcde2975fb19da9219700c8a08704c34559d2c`; artifact ID `14119193255`; ZIP SHA-256 `ca28bfd7d48b0e304ce2a41176c3ccf1a5ea241cf24eba880c9c5de246551399`.
- Run #43608839976 SUCCESS; workflow commit `9e8cafda5a878bd7c212b9b3b385ea648e4c3b12`; artifact ID `14119642179`; ZIP SHA-256 `d99c92c23fe8d5f789e4ffd99fdd807f5331c4b261083eb63b0c9fb315ce856d`.
- Public SDMX 2.1 metadata retrieval: HTTP 200 for IMF:BOP_GBPM6(2.0), IMF:BPM6_BOP_Q(1.5), and IMF:BOP(2.6.0), all parseable XML.
- BOP_GBPM6(2.0) explicitly references IMF:BOP(2.0), with 18 dimensions, 15 attributes, OBS_VALUE, and 22 unique direct codelist references.
- BPM6_BOP_Q(1.5) explicitly references IMF:BOP(1.5); direct raw XML parsing shows 17 dimensions (no TYPE_ENTITY), 14 attributes and OBS_VALUE. Do not treat it as schema-identical to BOP 2.0/2.6.0.
- IMF:BOP(2.6.0) direct and descendant responses both parsed. DSD has 18 ordered dimensions, 15 attributes and OBS_VALUE. It has 22 unique direct component codelist references; descendant payload contains 23 codelist objects including one related extra CL_AREA version 1.17.0.
- DSD 2.6.0 directly references IMF:CL_AREA(2.0.0) for REF_AREA/COUNTERPART_AREA (931 codes); India is `IN` / `India`. BOP_GBPM6 DSD 2.0 references IMF:CL_AREA(1.14) (885 codes), also with `IN` / `India`.
- Raw XML hashes: BOP_GBPM6(2.0) descendants `d1698e30516d554740d269db5126487902fc2632131bf0ae3add26aefa7f63c7`; BOP(2.6.0) descendants `0282f8ed931fc1c058c5f612f9b5c5c3ca60fa0590344d059d3ed2f547fd19ea`.
- Corrective lesson: the initial broad XML parser matched nested Dimension references under attribute relationships and emitted blank component IDs. Raw responses were preserved; a follow-up parser scoped dimensions to DataStructureComponents/DimensionList, attributes to AttributeList and measures to MeasureList. Reported component counts were independently checked against raw XML.
- Service boundary correction: IMF SDMX Central's public REST endpoint documented in the May 2025 guide is the Structure metadata query service. Its separate public POST endpoints perform validation/transformation/registration; they are not a raw observation GET API. IMF Data Portal's own SDMX 2.1/3.0 APIs are distinct; Swagger requires beta portal sign-in. No unauthorized access was attempted.
- Crucial unresolved point: IMF Portal dataset URN `IMF.STA:BOP(21.0.0)` remains unproven as a mapping to IMF:BOP_GBPM6(2.0), IMF:BPM6_BOP_Q(1.5), or IMF:BOP(2.6.0). Do not equate similar BOP names or versions.
- India codelist code validation is metadata-only; no India observation rows acquired. Portal crosswalk UNKNOWN; observation access BLOCKED; EMDE reporter coverage NOT DONE; EM aggregation BLOCKED.
- Evidence report: `docs/IMF_BOP_SDMX21_CANDIDATE_METADATA_AUDIT_20261114.md`, commit `4080ebbd6fc0cf855415e1871aa54f8da243a6ef`.
- Extraction specification addendum appended to `docs/IMF_BOP_PORTFOLIO_FLOW_EXTRACTION_SPEC_V1.md`, commit `b51d32073fdeaab1307909851adef5d155b7fb2d`.
- IMF BOP workstream acceptance remains 4/7 (57%) on the existing rubric. Metadata verification adds evidence quality but does not satisfy Portal crosswalk or observation acquisition gates. Project-wide verified progress remains NOT_CALCULABLE pending full ledger reconciliation.
- ₹0 spend, free official sources only, no paid APIs, no credentials/auth bypass, no synthetic observations/timestamps, no external contact, no PR merge, no production changes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, engines and Hard Gate unchanged.


## 2026-11-14 — IMF Portal-owned BOP dataflow crosswalk and India observation access verified

This entry supersedes the earlier ledger status that the Portal URN-to-dataflow crosswalk was UNKNOWN and observation access was wholly BLOCKED. Earlier failures and separate SDMX Central registry-vintage results remain preserved.

### New verified identity

- Portal dataset URN: `IMF.STA:BOP(21.0.0)`.
- Correct SDMX 2.1 REST 1.x Dataflow request: `https://api.imf.org/external/sdmx/2.1/dataflow/IMF.STA/BOP/21.0.0?references=all`.
- HTTP 200, Content-Type `application/vnd.sdmx.structure+xml;version=2.1`, 3,965,650 bytes, raw SHA-256 `e9414015aaf3480d8254f2935eb4f723f8b50196f104881d7cf29454bfb12ce5`.
- Dataflow object: IMF.STA:BOP(21.0.0); exact DSD reference: IMF.STA:DSD_BOP(24.0.0).
- Important correction: adding `/structure/` to this SDMX-REST 1.x path returns HTTP 404 “No such artefact type: *”. The correct resource path has no such prefix. The failed path remains diagnostic history.
- DSD_BOP 24.0.0 direct components: 6 dimensions (COUNTRY, BOP_ACCOUNTING_ENTRY, INDICATOR, UNIT, FREQUENCY, TIME_PERIOD), 45 attributes, OBS_VALUE. TIME_PERIOD is observation-level.
- Verified codes: IND=India; A_NFA_T=Assets, Net acquisition of financial assets; P_F=Portfolio investment, Total financial assets/liabilities; USD=US dollar; A=Annual; Q=Quarterly.
- Do not substitute the SDMX Central registry candidates IMF:BOP_GBPM6(2.0), IMF:BPM6_BOP_Q(1.5), or IMF:BOP(2.6.0) for this Portal-owned DSD_BOP(24.0.0).

### Public observation acquisition

- Exact Data Portal SDMX 3.0 data route and key: `IMF.STA/BOP/21.0.0/IND.A_NFA_T.P_F.USD.A`.
- Annual 2015–2025 time filter; both SDMX-JSON 2.0.0 and SDMX-ML 3.0.0 returned HTTP 200.
- The exact series returned 11 observations, one for each year 2015–2025.
- The full JSON body was 49,654,152 bytes (SHA-256 `844f253263c00e77b7d0ee572a47dd01dc258c7b3eb0bc4b5f1eba9daac59a25`); full XML was 122,045,648 bytes (SHA-256 `ca4676dbccb82383b7e549922169729c40084ec0d1c3eec4208f4ae4b1c25471`). The full XML included 405,562 group metadata nodes, so it is not the preferred narrow extraction profile.
- Compact query profile `dimensionAtObservation=TIME_PERIOD&attributes=all&detail=dataonly&limit=100` returned HTTP 200, 7,845 bytes, SHA-256 `85cca14cabf7a674ba37c00f88e3140f562480130bdde57d4902562fa6e0e23a`, and parsed 11/11 observations. It is 99.9842% smaller than the full JSON response while preserving the observations and all requested attributes.
- Parser correction: compact SDMX-JSON places observations under `dataSets[0].series[*].observations`, not `dataSets[0].observations`. The first parser missed the nested series shape; raw JSON inspection showed the 11 observations, and the parser was corrected. Do not count the initial parser's zero as an API data failure.
- Indicator correction: `P` exists as a broad portfolio category but is not the India asset-side aggregate group used in the response. The observed aggregate series code is `P_F`; the exact codelist label and dataflow group inventory were checked. Do not use P for this aggregate series.

### Observation metadata / flags

- Series: SCALE=6; METHODOLOGY=BPM6.
- Observation: PRECISION=6; DERIVATION_TYPE=O (“Reported official data”); ACCESS_SHARING_LEVEL=PUBLIC_OPEN (“Public (Unrestricted)”); SECURITY_CLASSIFICATION=PUB (“Public or Unrestricted)”).
- STATUS, ACCESS_SHARING_NOTES, SOURCE are null at observation level. Preserve nulls; no inference.
- SCALE and PRECISION are preserved as metadata; no multiplier, scaling or unit conversion was applied.

### Persisted data and hashes

- CSV `data/research/imf_bop_india_portfolio_assets_usd_annual_2015_2025.csv`: 11 rows; SHA-256 `60e557c922763f145284c6243e4612d6c05c0ce756c6f2d8846e0ea2fc7c8697`; commit `47bc2c83bc60aec0bfebb4cb765f5884af84dbd7`.
- Manifest `data/research/imf_bop_india_portfolio_assets_usd_annual_2015_2025.manifest.json`; final commit `4c6d19533ce8c57564376f6fadf5e3055a67d42a`.
- Full report `docs/IMF_BOP_PORTAL_DATAFLOW_AND_INDIA_OBSERVATION_AUDIT_20261114.md`; commit `e01607a6d03c3a3ed511082de79ec9af17fa7c2b`.
- Extraction spec appended; commit `9e35d42b21cdcb78b97794a1d7f2fa704b7233a3`.

### GitHub Actions evidence

- Run #43615378167 — SUCCESS; commit `0405347ac4fb2944b0bdc89fd4159b26e90ea8fb`; artifact ID `14122440301`; ZIP SHA-256 `2411f5837d7145ed6450a1423b17282f240cda6b7b6d61d842e4c18a6e88c125`.
- Run #43615740505 — SUCCESS; commit `4d3630d7fb8d196bb2af74870e2963ef831a9293`; artifact ID `14121942694`; ZIP SHA-256 `e9d2b920a658870f0f4eb9abf60bc82815ed945b4ef0d9f1a96e3bc66c00d666`.
- Run #43616059985 — SUCCESS; commit `e6d54ed5507bcc8a6cd4054dd44ecc7c3ceef863`; artifact ID `14122421554`; ZIP SHA-256 `cc951e2655dc4592ab82d848e0beebc43970132de1f4f3edc5c3ef8b56aaed23`.

### Updated IMF BOP workstream gates

- Accepted gates now 5/7 (71.4%) on the existing rubric: Portal identity, DSD/codelists/direct component inventory, WEO membership mapping, and Portal-owned dataflow crosswalk are accepted.
- Narrow India annual portfolio asset series (11/11) is PASS, but the full India-panel acquisition gate remains IN_PROGRESS / PARTIAL until liabilities, quarterly data and revisions/coverage checks are complete.
- India liability series: NOT DONE.
- India quarterly assets/liabilities: NOT DONE.
- Full 154-economy EMDE reporter coverage: NOT DONE.
- EM portfolio-flow aggregation: BLOCKED.
- Project-wide PRECISION-WIRES V11.3 progress remains NOT_CALCULABLE until all workstream acceptance gates and weights are reconciled. Do not report 71.4% as project-wide progress.

### Next highest-value action

Use the compact `attributes=all&detail=dataonly` profile to retrieve, separately and with exact dimension order:
1. India annual portfolio liability-side series: `IND.L_NIL_T.P_F.USD.A`.
2. India quarterly portfolio asset and liability series with `FREQUENCY=Q` and quarter-specific time filters.
Then reconcile coverage, flags, periods, revisions and asset/liability definitions before widening to the 154-economy EMDE panel.

### Invariants re-confirmed

₹0 spend; free official sources only; no paid APIs; no login or authentication bypass; no synthetic values/timestamps; no external contact; no PR merge; no production changes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, all five engines and Hard Gate unchanged.


## 2026-11-14 — India BOP annual/liability and quarterly assets/liabilities completed; reconciliation PASS

This entry supersedes the immediately prior “India liability series NOT DONE / India quarterly assets/liabilities NOT DONE” status. Historical failed runs and prior artifacts remain preserved.

### Accepted acquisition result
- Portal dataset/dataflow: `IMF.STA:BOP(21.0.0)`; exact DSD reference: `IMF.STA:DSD_BOP(24.0.0)`.
- Exact series dimension order: COUNTRY, BOP_ACCOUNTING_ENTRY, INDICATOR, UNIT, FREQUENCY; observation dimension TIME_PERIOD.
- Four India series are now available for 2015–2025:
  - Annual assets `IND.A_NFA_T.P_F.USD.A`: 11 rows (previously acquired).
  - Annual liabilities `IND.L_NIL_T.P_F.USD.A`: 11 rows.
  - Quarterly assets `IND.A_NFA_T.P_F.USD.Q`: 44 rows.
  - Quarterly liabilities `IND.L_NIL_T.P_F.USD.Q`: 44 rows.
- Total raw observations: 110. All requests HTTP 200; exact requested series keys matched returned dimensions; periods unique and complete for the requested ranges; OBS_VALUE values non-null and finite.
- Codes verified from Portal-owned codelists: IND=India; A_NFA_T=Assets, Net acquisition of financial assets; L_NIL_T=Liabilities, Net incurrence of liabilities; P_F=Portfolio investment, Total financial assets/liabilities; USD=US dollar; A=Annual; Q=Quarterly.

### Annual-to-quarterly arithmetic reconciliation
- Using Decimal arithmetic on raw OBS_VALUE strings, each year's four quarters were summed and compared with the annual value.
- Assets: 11/11 years; maximum absolute difference 0.0000009; tolerance 0.00001; PASS_WITH_TOLERANCE.
- Liabilities: 11/11 years; maximum absolute difference 0.000007; tolerance 0.00001; PASS_WITH_TOLERANCE.
- This is a data arithmetic coherence check only. No scale multiplier, USD conversion, netting, or aggregation was applied.

### Persisted research outputs
- Combined CSV: `data/research/imf_bop_india_portfolio_assets_liabilities_annual_quarterly_2015_2025.csv`; 110 rows; SHA-256 `260ccc247ec564737bb3afe0a820c2435e37a58f588603241274537eca99f1b9`.
- Manifest: `data/research/imf_bop_india_portfolio_assets_liabilities_annual_quarterly_2015_2025.manifest.json`.
- Report: `docs/IMF_BOP_INDIA_PORTFOLIO_SERIES_RECONCILIATION_20261114.md`.
- Extraction specification updated: `docs/IMF_BOP_PORTFOLIO_FLOW_EXTRACTION_SPEC_V1.md`.

### Workflow / artifact evidence
- Run #43623518481 SUCCESS; commit `111167ff11fbba42b226d8ee33634f111be0a893`; artifact ID 14125515371; ZIP SHA-256 `4127f4b691e46967dc8e0f91d6ff5536e9bc01224de0d488f90e5a4acd13327c`. Contains all three newly acquired raw responses and parsed observations.
- First parser attempt Run #43623450125 FAILED after the three requests returned HTTP 200. Root cause: validator incorrectly called mapping methods on the ordered dataset-level attribute array. The raw responses were retained (artifact 14125291402; ZIP SHA-256 `20d24b5109a9c44dd485a357687d789d5417ed5215f41b4bdf90ccbfe1c86a87`). Correction: preserve dataset attributes as an ordered array; no query/key changes.
- Independent committed CSV integrity Run #43623953963 SUCCESS; commit `577f278c0b57ee2e3c48e6a41c731d1ed33f8efd`; artifact ID 14125201831. It recomputed the committed CSV SHA-256, verified 110 rows, all four key/period sets, source hash counts and both annual/quarterly reconciliations.
- Integrity result SHA-256 verified: `260ccc247ec564737bb3afe0a820c2435e37a58f588603241274537eca99f1b9`.

### Metadata and boundaries
- SCALE=6 and PRECISION=6 are preserved as metadata only; no multiplier applied. METHODOLOGY=BPM6; DERIVATION_TYPE=O; ACCESS_SHARING_LEVEL=PUBLIC_OPEN; SECURITY_CLASSIFICATION=PUB.
- STATUS, ACCESS_SHARING_NOTES and SOURCE remain null. Quarterly asset series has IFS_FLAG=true; liability series IFS_FLAG is null.
- India annual/quarterly assets/liabilities base acquisition: PASS (110 observations). Full India panel remains IN_PROGRESS pending vintage/revision and further completeness checks.
- Full 154-economy EMDE reporter coverage: NOT DONE. WEO membership is not observation coverage.
- EM portfolio-flow aggregation: BLOCKED. Keep assets/liabilities separate; no aggregate, netting, currency conversion, or forward-fill.
- IMF BOP workstream accepted-gate score remains 5/7 (71.4%) on the existing rubric; the full India-panel acceptance gate is still partial, so do not increment it yet. Project-wide PRECISION-WIRES V11.3 percentage remains NOT_CALCULABLE pending full workstream and weight reconciliation.

### Next highest-value action
Run an EMDE reporter-coverage audit against the exact Portal DSD_BOP(24.0.0) using the already verified 154-member WEO April 2026 crosswalk. Determine actual reporter coverage separately from membership, and preserve every absent/unresolved reporter as UNKNOWN. Then investigate revision/vintage availability before any panel aggregation.

### Invariants re-confirmed
₹0 spend; free official sources only; no paid APIs; no credentials/auth bypass; no synthetic data/timestamps; no external contact; no PR merge; no production changes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, engines A–E and Hard Gate unchanged.


## 2026-11-14 — WEO EMDE to Portal BOP COUNTRY codelist crosswalk PASS

- WEO April 2026 EMDE membership (154 names) was mapped directly to the exact Portal-owned `IMF.STA:CL_BOP_COUNTRY(1.0.0)` codelist (345 codes) embedded in the already archived Portal dataflow structure response. This is a dataset-specific BOP COUNTRY crosswalk; it does not depend on or substitute the separate CL_AREA mapping.
- Result: 154/154 mapped; 154 unique BOP codes; 0 duplicates; 0 UNKNOWN; 0 ambiguous. 109 normalized exact matches + 45 explicit reviewed aliases. No fuzzy matching.
- Critical correction: WEO “Micronesia” has area code FM / “Micronesia, Federated States of” in the WEO-to-CL_AREA source. The BOP codelist contains both FSM (“Micronesia, Federated States of”) and U057 (“Micronesia”, a regional aggregate). The crosswalk explicitly selects FSM and excludes U057. Do not let a same-name aggregate become a country reporter.
- WEO “West Bank and Gaza” maps to BOP-specific code WBG by exact codelist label; this is a dataset code mapping, not a geopolitical/legal-status assertion. Namibia maps directly to NAM from the BOP codelist.
- CSV: `data/research/imf_weo_emde_to_bop_country_crosswalk_2026_04.csv`; 154 rows; SHA-256 `62ad409cc71c1056994a418e55b5e2a9367bd04c844a6bb5957bda5f0b0dd815`.
- Manifest: `data/research/imf_weo_emde_to_bop_country_crosswalk_2026_04.manifest.json`; report: `docs/IMF_WEO_EMDE_TO_BOP_COUNTRY_CROSSWALK_20261114.md`.
- Integrity Run #43624431543 SUCCESS; commit `60b7a7819048e16c122a0ec760753353d805607c`; artifact ID 14125337955; ZIP SHA-256 `3ae91eae37286936b797719e2e7ae765e53fdba00916974ccbd2f553a4f4b9ee`.

Acceptance boundary: this proves membership-to-BOP-dimension-code mapping only. It does not prove observations exist for any country. The actual 154-economy reporter coverage gate remains NOT DONE until exact BOP response series are queried and reporter codes compared separately for assets/liabilities and frequency. EM aggregation remains BLOCKED. No aggregation or production changes.


## 2026-11-14 — India BOP liabilities and quarterly portfolio series; annual/quarterly reconciliation

- Acquisition workflow Run #43623518481 — SUCCESS. Workflow file `.github/workflows/imf_bop_india_liability_quarterly.yml`; initial diagnostic Run #43623450125 FAILED only because the parser incorrectly treated SDMX dataset attributes as a dictionary. Raw responses were retained. The parser was corrected to respect the SDMX ordered attribute-array shape; no endpoint/key changes were made.
- Fix commit: `111167ff11fbba42b226d8ee33634f111be0a893`.
- Successful run artifact ID `14125515371`; artifact ZIP SHA-256 `4127f4b691e46967dc8e0f91d6ff5536e9bc01224de0d488f90e5a4acd13327c`.
- Dataset identity remained IMF.STA:BOP(21.0.0), DSD IMF.STA:DSD_BOP(24.0.0).
- India annual portfolio liabilities `IND.L_NIL_T.P_F.USD.A`: HTTP 200, 11 observations, 2015–2025, 7,846 bytes, raw SHA-256 `6eba68f8779efa5636afea8d4a9de4ce26478c67150144c1e4f128e4f6d3a4e4`.
- India quarterly portfolio assets `IND.A_NFA_T.P_F.USD.Q`: HTTP 200, 44 observations, 2015-Q1–2025-Q4, 10,201 bytes, raw SHA-256 `aff39180e21eec8f71308ac269f9191eb0138b5471808bfa710c6a582be1d24f`.
- India quarterly portfolio liabilities `IND.L_NIL_T.P_F.USD.Q`: HTTP 200, 44 observations, 2015-Q1–2025-Q4, 10,185 bytes, raw SHA-256 `6ebe3c2eabd7f9019ffd80d51e01de359bc1f64aee66c8609877654ad4558ccc`.
- All three exact series keys were checked; parser verified exact dimension IDs/order and requested key values, unique periods, non-null finite observations. Raw response bodies and parsed observations retained in artifact.
- Compared quarterly sums to annual observations for 2015–2025. All 11 years reconcile for both asset and liability sides within USD 0.00001. Maximum absolute decimal-string difference: assets USD 0.0000009; liabilities USD 0.0000070. These are representation-level differences; no material mismatch.
- Reconciliation report committed: `docs/IMF_BOP_INDIA_ANNUAL_QUARTERLY_RECONCILIATION_20261114.md`, commit `8705031c06a9d6dfafd19770541863715b280e17`.
- India narrow portfolio slice acquisition + annual/quarterly arithmetic reconciliation: PASS. This does not establish full India BOP panel, revisions/vintages, 154-economy EMDE coverage, or EM aggregation. EM aggregate flow remains BLOCKED.
- Initial failed diagnostic Run #43623450125 is retained as history, not counted as a data-access failure: it returned HTTP 200 for all three requests and the subsequent successful parser-only fix passed.
- Invariants unchanged: ₹0 spend; official public sources only; no synthetic values/timestamps; no login or bypass; no PR merge or production integration; Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, engines A–E and Hard Gate unchanged.


## 2026-11-14 — 154-economy EMDE BOP quarterly portfolio reporter coverage audit

- Exact basis: IMF.STA:BOP(21.0.0), DSD IMF.STA:DSD_BOP(24.0.0), WEO April 2026 EMDE membership (154) mapped to dataset-specific CL_BOP_COUNTRY(1.0.0). Existing 154/154 crosswalk PASS is reused; it was not repeated.
- Query scope: portfolio financial flows P_F, USD, quarterly, 2015-Q1 through 2025-Q4 (44 quarters), exact asset entry A_NFA_T and liability entry L_NIL_T, public unauthenticated SDMX 3.0 wildcard COUNTRY key '*'.
- Valid coverage Run #43624740474 SUCCESS; commit e2bcf99383c0ddaa54c089ac2a30c2f06e38a45b; job 132537959631; artifact ID 14125517628; ZIP SHA-256 daaedd6c4d186ac87ba6694ff3ae4816b544ba487fd12589b1b128b87f6cc861.
- Assets raw response 320,788 bytes SHA-256 68f865c2578f5d3dd21a145de71c0cb1f731041bf7b626fb5d1d3cd64e704664. 156 total reporter series, 113/154 EMDE reporters present (73.38%), 41 no series returned in the exact selected query range; 43 returned non-EMDE codes.
- Liabilities raw response 310,236 bytes SHA-256 b6875e20f20b279b2ce17131a42ba4af320adbc61f9c3bd28e9fb1067e597db1. 155 total reporter series, 112/154 EMDE reporters present (72.73%), 42 no series returned in the exact selected query range; 43 returned non-EMDE codes.
- 154-row assets coverage CSV SHA-256 5939c155abcbdb5687f41d8f79831f02a75da02a9dda2d85aae9b748d0bc7cdc; liabilities coverage CSV SHA-256 726f4fcfdaa7f41b165bf9d4ff837bf0c3708e472249d2d78f94fea1ea8654cc.
- Cross-series: 111 EMDE have both sides; DZA and ETH assets-only; ZWE liabilities-only; 40 have no series returned on either side. Union at least one side = 114/154 (74.03%); both sides = 111/154 (72.08%).
- Completeness: 88 EMDE assets reporters have all 44 quarters; 25 are partial. 84 liabilities reporters have all 44 quarters; 28 are partial. Only 83/154 have both sides complete for all 44 quarters; 28 have both sides but at least one partial. Do not infer continuity from first/last periods alone.
- The 40 common no-series codes: ARE, ATG, BEN, BFA, BRB, CAF, CIV, COG, COM, DMA, ERI, FSM, GAB, GNB, GNQ, GRD, HTI, IRN, KEN, KNA, LBY, LCA, MDV, MHL, MLI, MWI, NER, NRU, OMN, PLW, SEN, SLE, SOM, SSD, SYR, TCD, TGO, TKM, TUV, VCT.
- Crucial status wording: NO SERIES RETURNED FOR THIS EXACT FILTER/PERIOD. It does not prove permanent non-reporting. Causes remain UNKNOWN. No aggregation permitted.
- False-positive lesson: Run #43624650170 queried literal country key `all`; HTTP 200 and valid parse returned zero reporter series, but the old workflow marked it SUCCESS because it did not enforce nonempty result. This is a false-positive diagnostic, not 0/154 coverage. Valid wildcard is `*`, used by Run #43624740474. Run #43624650170 remains preserved and must not be counted.
- Workflow hardening commit `735f9191317aa578e8cccc8148c1e8ca9482574c`: zero reporter series now raises an error; automatic push trigger disabled to prevent redundant data calls; manual dispatch only.
- Report: `docs/IMF_BOP_EMDE_QUARTERLY_REPORTER_COVERAGE_20261114.md`, commit `c53a3be32828293306d62a1d1fa6f19dbe006f71`.
- Coverage query and matrix generation PASS; 154/154 asset and liability coverage gates NOT PASS; reasons for absent series UNKNOWN; EM aggregation BLOCKED.
- Next: targeted historical reach-back 2000-Q1 to 2014-Q4 for the 40 common absent and 3 asymmetric codes; then period-gap analysis and revision/vintage investigation. No fuzzy country matching or synthetic fill.
- Invariants unchanged: ₹0 spend, free official sources, no paid APIs, credentials/auth bypass, synthetic values/timestamps, external contact, PR merge, or production changes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, engines A–E and Hard Gate unchanged.


## 2026-11-14 — 2000–2014 historical reach-back and 2000–2025 cross-period reconciliation

- Reused exact 43-code priority target list from the prior accepted coverage report (40 common 2015–2025 no-series codes plus DZA, ETH, ZWE); did not repeat the 154-country crosswalk or 2015–2025 query.
- Historical workflow: `.github/workflows/imf_bop_emde_historical_reachback.yml`; creation commit `126d82d2b04772d09e3d4bf894a45e4cd015c536`; verified workflow blob `5033849aea492da94faed3d4bc25ac124e717c3e`.
- Run #43626075930 SUCCESS; job 132542048096; artifact ID 14125219608; artifact ZIP SHA-256 `539e34fca42394d5ae53da27d44243f7aea6c79a1631178465f351b5d8bf1157`.
- Window 2000-Q1 to 2014-Q4 (60 quarters), exact IMF.STA:BOP(21.0.0) portfolio flows P_F, USD, quarterly; assets A_NFA_T and liabilities L_NIL_T; wildcard COUNTRY `*`; HTTP 200 and parser/schema checks PASS for both queries.
- Assets response 332,012 bytes SHA-256 `93025fe023aac9d301f6799d13ada7b0f04d27703012d8b3e1373db6c5527226`; 143 total series; 100/154 EMDE reporter codes present; 54 absent in this window; 43 non-EMDE codes.
- Liabilities response 320,793 bytes SHA-256 `78ffa2a1492667cc2979f357acafecb490875a80f609726838f1be5ea44b5d25`; 142 total series; 99/154 EMDE reporter codes present; 55 absent in this window; 43 non-EMDE codes.
- Among the 43 priority codes, only ETH and HTI appeared historically, for both assets and liabilities. ETH: 28 observations per side, 2003-Q1–2009-Q4, contiguous. HTI: 32 observations per side, 2004-Q4–2012-Q3, contiguous. Remaining 41/43 priority codes had no series returned in 2000–2014 for either side.
- Reused 2015–2025 run #43624740474 and artifact ID 14125517628; no rerun. DZA assets: 20 contiguous observations 2021-Q1–2025-Q4; ETH assets: 4 contiguous observations 2024-Q1–2024-Q4; ZWE liabilities: 36 contiguous observations 2017-Q1–2025-Q4. No 2015–2025 liabilities series for DZA/ETH; no assets series for ZWE.
- Combined tested 2000–2025: 4/43 priority codes have any observations (DZA, ETH, HTI, ZWE); 39/43 have no series returned for either side in either tested window. Assets 3/43 (DZA, ETH, HTI); liabilities 3/43 (ETH, HTI, ZWE); 2/43 (ETH, HTI) have both sides represented somewhere, but not necessarily same-quarter overlap or continuous coverage.
- Key discontinuities: ETH assets has 56 missing quarters between 2009-Q4 and 2024-Q1; ETH liabilities has no returned series after 2009-Q4 through 2025-Q4; HTI both sides only 2004-Q4–2012-Q3; DZA assets only 2021-Q1–2025-Q4; ZWE liabilities only 2017-Q1–2025-Q4. All observed spans are contiguous internally; gaps outside spans remain missing, never filled.
- Cross-period matrix `data/research/imf_bop_emde_43_cross_period_matrix_20261114.csv`, commit `6e61a25cf19c546ee1df22b8771b3d9c7b9b5921`, SHA-256 `b7f68ddce1c33d2ecc5536baa9082f0dff5b238ad95429ec8d5e4a681dda913b`, 2,313 bytes, 43 rows.
- Research report `docs/IMF_BOP_EMDE_HISTORICAL_REACHBACK_RECONCILIATION_20261114.md`, commit `19ae265bae206095551f483953cf5db7d75818be`.
- Work-package status: historical acquisition PASS; cross-period reconciliation PASS; coverage gate NOT PASS; EM aggregation BLOCKED. Absence remains "NO SERIES RETURNED IN THE TESTED WINDOWS", not economic zero or proven permanent non-reporting.
- Next: inspect exact SDMX series/observation attributes, flags and revision/vintage metadata for ETH, HTI, DZA, ZWE; inspect codelist/dataflow eligibility for the 39 with no observations in either tested window. Keep causes UNKNOWN until evidenced.
- Invariants unchanged: ₹0 spend, official public sources only, no synthetic values/timestamps, paid API, auth bypass, external contact, PR merge or production integration; Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, engines A–E and Hard Gate unchanged.


## 2026-11-14 — Addendum: raw SDMX attributes inspected; empty-series wording corrected

- The four already-downloaded raw response bodies from Runs #43626075930 and #43624740474 were inspected directly. No duplicate data acquisition was performed.
- For every observed series among ETH, HTI, DZA, ZWE: SCALE=6 and METHODOLOGY=BPM6; DECIMALS_DISPLAYED and OVERLAP are null.
- IFS_FLAG=true on observed asset series ETH, HTI, DZA; IFS_FLAG is null on observed liability series ETH, HTI, ZWE. Meaning of IFS_FLAG remains UNKNOWN pending exact official codelist/definition verification; do not infer from boolean value.
- Across every observed quarter for these reporters: PRECISION=6, DERIVATION_TYPE=O, ACCESS_SHARING_LEVEL=PUBLIC_OPEN, SECURITY_CLASSIFICATION=PUB. Observation STATUS, ACCESS_SHARING_NOTES and SOURCE are null. Preserve nulls and do not infer missing metadata.
- Historical liabilities raw response includes a ZWE series key whose observations object is empty. It is not an observed reporter and must not be counted in coverage. Other targeted empty series keys: none. This raw detail corrects the earlier broad phrase “no series returned” to “no observations returned” for 39/43 with no data across both tested windows.
- Cross-period CSV wording corrected: statuses now say `NO_OBSERVATIONS_IN_EITHER_TESTED_WINDOW`; final CSV SHA-256 `4d9686c8e0735a1d076c3f6850648bd481b59771beebcb260f0625bd14d405dc`; correction commit `c94f7a81bc7c71051b16160385c9e7250f8e233e`.
- Updated report: `docs/IMF_BOP_EMDE_HISTORICAL_REACHBACK_RECONCILIATION_20261114.md`, commit `56da512180eb80c9ea35cb52558cfd293fc50104`.
- Historical acquisition and cross-period reconciliation remain PASS as research tasks; reporter coverage acceptance remains NOT PASS; EM aggregation remains BLOCKED. IMF BOP accepted gates remain 5/7 (71.4%) on existing rubric; this audit does not promote the incomplete 154-country coverage gate.
- Next: verify IFS_FLAG definition/codelist and reporter eligibility for the 39 codes with no observations across the tested 2000–2025 windows; no assumption that missing observations equal zero or permanent non-reporting.
- Project-wide PRECISION-WIRES V11.3 progress remains NOT_CALCULABLE until all workstream gates and weights are reconciled. All production invariants remain unchanged; spend ₹0.
