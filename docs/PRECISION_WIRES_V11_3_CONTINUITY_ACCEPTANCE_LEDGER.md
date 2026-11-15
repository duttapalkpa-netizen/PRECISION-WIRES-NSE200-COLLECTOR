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
- Cross-period matrix `data/research/imf_bop_emde_43_cross_period_matrix_20261114.csv`, commit `6e61a25cf19c546ee1df22b8771b3d9c7b9b5921`, SHA-256 `b7f68ddce1c33d2ecc5536baa9082f0dff5b238ad95429ec8d5e4a681dda913b`, 2,547 bytes, 43 rows.
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
- Cross-period CSV wording corrected: statuses now say `NO_OBSERVATIONS_IN_EITHER_TESTED_WINDOW`; final CSV SHA-256 `d331ba2f80c253c7d1e95dc2ba0c662fa27d4444aa21f12e9c881e200741704a`; correction commit `c94f7a81bc7c71051b16160385c9e7250f8e233e`.
- Updated report: `docs/IMF_BOP_EMDE_HISTORICAL_REACHBACK_RECONCILIATION_20261114.md`, commit `56da512180eb80c9ea35cb52558cfd293fc50104`.
- Historical acquisition and cross-period reconciliation remain PASS as research tasks; reporter coverage acceptance remains NOT PASS; EM aggregation remains BLOCKED. IMF BOP accepted gates remain 5/7 (71.4%) on existing rubric; this audit does not promote the incomplete 154-country coverage gate.
- Next: verify IFS_FLAG definition/codelist and reporter eligibility for the 39 codes with no observations across the tested 2000–2025 windows; no assumption that missing observations equal zero or permanent non-reporting.
- Project-wide PRECISION-WIRES V11.3 progress remains NOT_CALCULABLE until all workstream gates and weights are reconciled. All production invariants remain unchanged; spend ₹0.


## 2026-11-14 — Evidence hash correction for 43-row summary CSV

- The persisted GitHub CSV is the compact 43-row reporter summary (not the separate 86-row local diagnostic matrix). Read-back confirmed 2,547 bytes; correct SHA-256 is `d331ba2f80c253c7d1e95dc2ba0c662fa27d4444aa21f12e9c881e200741704a`. The prior 2,313-byte/hash note referred to a different local intermediate and is superseded. No source observation or status changed.
- The CSV status label is `NO_OBSERVATIONS_IN_EITHER_TESTED_WINDOW`; historical ZWE liabilities has an empty series key but zero observations.



## 2026-11-14 — IMF IFS_FLAG semantics resolved; exact eligibility remains UNKNOWN

- Official IMF Data Portal “Accessing International Financial Statistics (IFS)” page (published 2025-03-24): https://data.imf.org/en/news/accessing . IMF says former IFS data is reorganized into topic datasets; “IFS, Balance of Payments Indicators” maps to BOP. It documents the “IFS Flag” as downloadable series metadata and identifies API component `IMF_FLAG`, with `c[IFS_Flag]=True` selecting series formerly in IFS.
- Semantic determination: IFS_FLAG is a former-IFS collection/provenance marker. It is not a quality grade, BPM methodology, completeness, or revision flag.
- Applied to previously inspected responses only; no reacquisition: asset series ETH/HTI/DZA have IFS_FLAG=true, while liability series ETH/HTI/ZWE have null. Null semantics are not defined by the cited IMF page and remain UNKNOWN; preserve null, do not infer “never IFS”.
- Exact 39-country eligibility remains UNKNOWN. The 154/154 BOP COUNTRY codelist crosswalk proves dimension-code validity only, not reporter eligibility for the exact P_F + USD + quarterly + A_NFA_T/L_NIL_T combinations. Dataset-level annual/quarterly frequency does not establish each reporter's indicator/unit/frequency availability. No reporter-specific constraint evidence was established in this audit.
- Report: `docs/IMF_BOP_IFS_FLAG_AND_EMDE_ELIGIBILITY_METADATA_AUDIT_20261114.md`; created on branch `research/imf-bop-access-audit-v1`.
- Progress: IFS_FLAG semantic identification 100% (PASS); null semantics 0% (UNKNOWN); 39-country exact series eligibility 0% resolved (UNKNOWN); coverage gate NOT PASS; EM aggregation BLOCKED. IMF BOP accepted-gate score remains 5/7 (71.4%)—no gate promotion. Project-wide progress remains NOT_CALCULABLE.
- Next: inspect the exact archived DSD_BOP(24.0.0) structure response and referenced codelists/constraints for accounting entry, indicator, unit, frequency, and reporter-specific constraints. If absent, report only “no eligibility constraint found in inspected artefacts”; do not infer eligibility.
- No API data rerun, no new observations, no aggregation, no production changes, no PR merge. All protected V11.3 invariants remain unchanged; spend ₹0.


### Addendum — archived metadata artefact scope correction (2026-11-14)
- Re-opened prior metadata artifacts #14111193621 and #14112042284. They contain the global SDMx Registry DSD `IMF:BOP(2.6.0)` and global IMF dataflows, not the exact IMF Data Portal `IMF.STA:DSD_BOP(24.0.0)` structure/constraints.
- The global DSD component inventory does not include Portal-specific `IFS_FLAG` / `IMF_FLAG` or Portal dimension IDs `BOP_ACCOUNTING_ENTRY` / `INDICATOR`; its dimensions use a different vocabulary. It must not be used as a substitute for the Portal DSD.
- Consequently, 39-country exact series eligibility remains UNKNOWN; no reporter-specific eligibility conclusion is drawn. The next step must obtain the exact Portal DSD 24.0.0 structure and any associated dataflow constraints, or explicitly document that the exact artefact is unavailable.
- Corrected report: `docs/IMF_BOP_IFS_FLAG_AND_EMDE_ELIGIBILITY_METADATA_AUDIT_20261114.md`. No observation query rerun; no new coverage data; no aggregation or production change.


## 2026-11-14 — Exact Portal DSD_BOP(24.0.0) and IFS_FLAG first-pass retrieval

- New workflow `.github/workflows/imf_bop_portal_dsd24_ifs_flag_constraints.yml`; workflow commit `5c5ce0b637dce55efc2b6fc125d58f8e084a042e`.
- Run #43627524825 SUCCESS; artifact ID `14126861311`; artifact ZIP SHA-256 `054249b68772fcf4fde8eeccae6892e18180c3cdbb88f78038b16f268b804c21`.
- Exact Portal dataflow response HTTP 200, 3,965,650 bytes, SHA-256 `48777f898e943bbb15464bcbe9e99d719f2c94e5284543212d4eb6ec4e583877`; it explicitly references `IMF.STA:DSD_BOP(24.0.0)`.
- Exact Portal DSD response HTTP 200, 3,964,221 bytes, SHA-256 `82886da6dd396373ec85ffc94430bfe36ba838331ec7c93eb304df265ba2637e`; exact dataflow-to-DSD identity PASS.
- DSD contains direct `IFS_FLAG` attribute, concept `IMF.STA:IFS_FLAG`, assignmentStatus `Conditional`. Its direct allowed-value representation, null semantics and attachment level remain UNKNOWN pending focused parser extraction.
- First-pass ContentConstraint request `/contentconstraint/IMF.STA/all/latest?references=all` returned HTTP 204, zero bytes, empty-body SHA-256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`. This is not proof that no constraints exist in other agencies, provision agreements or data providers.
- Exact DSD response included codelist structures, but first-pass component-to-codelist extraction was incomplete; do not claim full COUNTRY / BOP_ACCOUNTING_ENTRY / INDICATOR / UNIT / FREQUENCY codelist reconciliation.
- Report: `docs/IMF_BOP_PORTAL_DSD24_IFS_FLAG_CONSTRAINTS_FIRST_PASS_20261114.md`, report commit `12ad3628d75c96052b23cf384b683eac642e2a99`.
- Gate state unchanged: IFS_FLAG semantic meaning PASS; IFS_FLAG component existence PASS; 39-country exact-series eligibility UNKNOWN (0% resolved); reporter coverage acceptance NOT PASS; EMDE aggregation BLOCKED; IMF BOP accepted gates remain 5/7 (71.4%); project-wide progress NOT_CALCULABLE.
- Next: focused parser against the archived exact DSD response; resolve direct codelist references and IFS_FLAG ConceptScheme; inspect ContentConstraint / ProvisionAgreement / DataProvider metadata for BOP dataflow. No observation query rerun, no aggregation, no production changes, no PR merge. All protected invariants unchanged; spend ₹0.


## 2026-11-14 — Focused DSD24 component/codelist parser and eligibility endpoint audit

- Workflow: `.github/workflows/imf_bop_dsd24_component_eligibility.yml`; workflow commit `339664040ff7e9338d3c013d9b89d0301de5a973`.
- Run #43628988259 SUCCESS; job #132551143961 SUCCESS.
- Artifact #14126994489; artifact ZIP SHA-256 `80b69fb559c22ee3a99641c58c2b1b3f8041c75e923a61aa25aa16e4ec772e28`.
- Exact DSD dataflow reference PASS; five dimension-to-codelist mappings resolved:
  - COUNTRY -> IMF.STA:CL_BOP_COUNTRY(1.0.0), 345 codes.
  - BOP_ACCOUNTING_ENTRY -> IMF.STA:CL_BOP_ACCOUNTING_ENTRY(3.3.0), 97 codes.
  - INDICATOR -> IMF.STA:CL_BOP_INDICATOR(10.0.0), 979 codes.
  - UNIT -> IMF:CL_UNIT(2.11.2), 270 codes.
  - FREQUENCY -> IMF:CL_FREQ(1.2.0), 34 codes.
- IFS_FLAG exact component PASS: concept `IMF.STA:CS_MASTER(1.0.0).IFS_FLAG`; official English definition says it identifies/marks indicators that were part of the IFS data product; core representation Boolean; assignment status Conditional; attached to COUNTRY, BOP_ACCOUNTING_ENTRY, INDICATOR, FREQUENCY and UNIT. It is not a reporter eligibility or completeness flag.
- Null/omitted-value semantics remain UNKNOWN: Boolean + Conditional does not define a default. Never coerce missing to false or true.
- Exact BOP content constraint, agency-wide content constraint, agency-wide provision agreement and agency-wide data provider scheme probes all returned HTTP 204 / zero bytes / empty SHA-256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`. This is no-content for those probes only, not proof of universal eligibility or absence of all possible restrictions.
- Reporter-specific eligibility for 39 countries remains UNKNOWN; historical coverage acceptance NOT PASS; EMDE aggregation BLOCKED. No observations rerun; no aggregation.
- Report: `docs/IMF_BOP_DSD24_COMPONENT_CODELIST_ELIGIBILITY_AUDIT_20261114.md`, report commit `e53c7eaf97fea87accdeb2e91289a3b499b5d5b3`.
- Previous first-pass audit report remains intact. This focused parser corrects the earlier nested DataStructureComponents/CoreRepresentation extraction gap; no old PASS artifact was deleted or rewritten.
- Next: resolve the 39-country exact series eligibility only from official reporter-specific applicability evidence or exact country × accounting-entry × indicator × unit × frequency inventory; otherwise retain UNKNOWN. All protected V11.3 invariants unchanged; spend ₹0.


## 2026-11-15 — Four-reporter series/observation attribute audit from archived raw responses

- Re-downloaded and re-hashed the exact prior GitHub Actions artifacts; both ZIP SHA-256 values match the previous ledger:
  - Historical Run #43626075930 / Artifact #14125219608: `539e34fca42394d5ae53da27d44243f7aea6c79a1631178465f351b5d8bf1157`.
  - Recent Run #43624740474 / Artifact #14125517628: `daaedd6c4d186ac87ba6694ff3ae4816b544ba487fd12589b1b128b87f6cc861`.
- All four raw response body SHA-256 values reverified against prior coverage reports: historical assets `93025fe023aac9d301f6799d13ada7b0f04d27703012d8b3e1373db6c5527226`; historical liabilities `78ffa2a1492667cc2979f357acafecb490875a80f609726838f1be5ea44b5d25`; recent assets `68f865c2578f5d3dd21a145de71c0cb1f731041bf7b626fb5d1d3cd64e704664`; recent liabilities `b6875e20f20b279b2ce17131a42ba4af320adbc61f9c3bd28e9fb1067e597db1`.
- Parsed existing `attributes=all` series and observation attribute arrays from those exact raw responses; no new IMF observation API calls. Eight series keys inspected across DZA, ETH, HTI and ZWE; seven keys have 180 non-empty observations total; historical ZWE liabilities key has zero observations.
- Series attributes: SCALE=6 and METHODOLOGY=BPM6 on all eight keys; DECIMALS_DISPLAYED and OVERLAP null; IFS_FLAG=true on the four observed asset keys, null on three observed liability keys and the empty ZWE liability key. This is a descriptive pattern only; null is not false and does not establish ineligibility.
- Observation attributes across 180 observations: PRECISION=6 (180/180), DERIVATION_TYPE raw code O (180/180), ACCESS_SHARING_LEVEL=PUBLIC_OPEN (180/180), SECURITY_CLASSIFICATION=PUB (180/180); STATUS, ACCESS_SHARING_NOTES and SOURCE null (180/180). No semantic expansion of O, no interpretation of null, no unit scaling.
- Derived CSV: `data/research/IMF_BOP_4_REPORTER_ATTRIBUTE_AUDIT_20261115.csv`, 8 rows, SHA-256 `cf88ebfd39bd934a16ceac11cb08015426061c00290c4083e74b661d948c5cc1`. A transcription error in the first draft (ETH recent PUBLIC_OPEN count) was caught by comparing against the parsed artifact and corrected before final validation; the final file now records 4/4, not 28/4.
- Manifest: `data/research/IMF_BOP_4_REPORTER_ATTRIBUTE_AUDIT_20261115.manifest.json`; report: `docs/IMF_BOP_4_REPORTER_ATTRIBUTE_AUDIT_20261115.md`.
- Gate state unchanged: 39/43 priority reporters still have no observations in either tested window; eligibility for those 39 remains UNKNOWN; coverage acceptance NOT PASS; EMDE aggregation BLOCKED. No country is classified ineligible from missing values.
- No new observation API calls, no aggregation, no production change, no PR merge, ₹0 spend. Production Selector, `RANKING_SCORE`, `+1 PRESSURE_FADE`, CORE-672, engines A–E and Hard Gate unchanged.
- Next: locate explicit official reporter-specific applicability/coverage metadata for the exact BOP series dimensions. If the public source does not expose a country-specific obligation/applicability contract, retain UNKNOWN and document the limitation rather than inferring eligibility.


## 2026-11-14 — 39-country annual-frequency exact-series reachability audit

- Target set was loaded programmatically from the prior verified 43-row quarterly cross-period matrix using `CROSS_PERIOD_STATUS == NO_OBSERVATIONS_IN_EITHER_TESTED_WINDOW`; exact target count 39, cross-checked against the validated 154-country WEO-to-BOP crosswalk.
- Workflow: `.github/workflows/imf_bop_39_country_annual_frequency_audit.yml`.
- Final corrected workflow commit: `f5c535c0c7635b81034f18ad185de37b24479050`.
- Run #43630656519 SUCCESS; job #132556279712 SUCCESS.
- Artifact #14128182046; ZIP size 134,541 bytes; SHA-256 `058ae62904bec701959175076d3d2aa9de20f402eb3425083bbfad2d36accc12`.
- Exact dataset/DSD: `IMF.STA:BOP(21.0.0)` / `IMF.STA:DSD_BOP(24.0.0)`. Series: `P_F`, `USD`, frequency `A`, assets `A_NFA_T`, liabilities `L_NIL_T`. Full annual response requested, then actual observations locally filtered to 2000–2025 inclusive.
- Assets raw response HTTP 200, 360,608 bytes, SHA-256 `711431c957199292cfb37e884a3e9344e7e519e23e9bb4baea2ff9f5523addfc`; 211 response series. Liabilities raw response HTTP 200, 352,754 bytes, SHA-256 `a256a5f5baaef80f48e7d3747c39db80d644078b896abe49a5190f21003b60aa`; 208 response series.
- 39-country annual assets matrix: 33 with >=1 non-null finite observation; 5 empty series keys; 1 no series key. Liabilities matrix: 31 with >=1 observation; 4 empty keys; 4 no series key.
- Cross-side annual result: 31/39 both sides; assets-only `FSM, SSD`; liabilities-only none; neither side has a non-empty annual series `CAF, ERI, GNQ, SOM, TCD, TKM`. 31 codes with both sides: `ARE, ATG, BEN, BFA, BRB, CIV, COG, COM, DMA, GAB, GNB, GRD, IRN, KEN, KNA, LBY, LCA, MDV, MHL, MLI, MWI, NER, NRU, OMN, PLW, SEN, SLE, SYR, TGO, TUV, VCT`.
- Annual result is frequency-specific reachability only; it does not prove quarterly eligibility/completeness, formal reporting obligation, or full annual continuity. Some reporters have short series or year gaps. No annual-to-quarterly conversion or backtest substitution. Empty series keys are not observations.
- Matrices inside artifact: assets CSV 7,836 bytes SHA-256 `8c207d852c9a219e1347cd2b035b782dac78cbbdec1ba12ce3c2a74723cfe24e`; liabilities CSV 7,586 bytes SHA-256 `ce1578e8f6574e78a730be7554d5cd616b358b8b9ca7d220219a0d477725460e`.
- Report: `docs/IMF_BOP_39_COUNTRY_ANNUAL_FREQUENCY_REACHABILITY_AUDIT_20261114.md`, commit `6469ee3f537ed59ae3a5504f77403d816786cb85`.
- Manifest: `data/research/imf_bop_39_country_annual_frequency_audit_20261114.manifest.json`, commit `9c88048d9dc2a98d6de9fcbfed2abf47f5fb3b28`.
- Diagnostic history preserved, not counted as final evidence: Run #43630501862 failed closed because server-side annual period filter returned an empty TIME_PERIOD dimension; Run #43630564954 initial parser failed to enforce the intended local year filter and is superseded; Run #43630618730 failed Python syntax validation. Final corrected Run #43630656519 alone supports the 2000–2025 annual counts.
- Gate decision: annual exact-series acquisition PASS; quarterly reporter eligibility remains UNKNOWN; quarterly coverage acceptance NOT PASS; EMDE aggregation BLOCKED. No quarterly evidence overwritten, no aggregation, no production integration or PR merge.
- Next: inspect annual year gaps and series attributes for 31 both-side + 2 assets-only reporters; separately investigate six no-nonempty-annual reporters. Keep annual and quarterly classes separate. ₹0 spend; all protected V11.3 invariants unchanged.


## 2026-11-15 — Annual continuity and six-country missing-series audit

- Source: downloaded and re-hashed Run #43630656519 artifact #14128182046; ZIP SHA-256 `058ae62904bec701959175076d3d2aa9de20f402eb3425083bbfad2d36accc12`. Used the two archived raw SDMX-JSON response bodies; no fresh API query or external service was needed for this continuity analysis.
- Important parser correctness: SDMX attribute integers are value-list indexes, not literal attribute values. Decoded each series/observation attribute using the corresponding response-structure `attributes.*[].values[]` code lists. Thus SCALE is `6`, METHODOLOGY is `BPM6`, observation DERIVATION_TYPE is `O`, ACCESS_SHARING_LEVEL is `PUBLIC_OPEN`, and SECURITY_CLASSIFICATION is `PUB`; null values remain null.
- Audited 39 countries × 2 sides = 78 rows, explicit 2000–2025 year grid, only non-null observations. No fill, interpolation, extrapolation, synthetic rows, annual-to-quarterly conversion, or aggregation.
- Assets: 33 reporters with ≥1 observation; 9 have all 26 years; 13 have 2025; 3 have interior gaps totalling 9 missing interior years; 649 non-null observations. Largest internal gaps: MWI 5, COG 3, GAB 1.
- Liabilities: 31 reporters with ≥1 observation; 9 have all 26 years; 11 have 2025; 6 have interior gaps totalling 29 missing interior years; 599 non-null observations. Largest internal gaps: MHL 9, LBY 8, COG 5, SLE 4, GNB 2, GAB 1.
- Nine countries have all 26 years on both sides: `ATG, DMA, GRD, KEN, KNA, LCA, MDV, OMN, VCT`. The other 22 with both-side observations have truncated spans and/or missing years and are not labelled continuous.
- Six no-nonempty-annual reporters refined: `CAF`, `GNQ`, `SOM`, `TCD` have EMPTY_SERIES_KEY both sides; `ERI` has NO_SERIES_KEY_RETURNED both sides; `TKM` has EMPTY_SERIES_KEY assets and NO_SERIES_KEY_RETURNED liabilities. For the four empty-both countries, assets series metadata includes SCALE=6, BPM6, IFS_FLAG=true; liabilities includes SCALE=6, BPM6, IFS_FLAG=null. TKM assets has same attributes; ERI has no series metadata. IFS_FLAG semantics are not inferred.
- Observation attributes across the 39 target countries: assets 649 rows: DERIVATION_TYPE=O 649, ACCESS_SHARING_LEVEL=PUBLIC_OPEN 649, SECURITY_CLASSIFICATION=PUB 649, STATUS/SOURCE null 649, PRECISION=6 558 and null 91. Liabilities 599 rows: DERIVATION_TYPE=O 599, ACCESS_SHARING_LEVEL=PUBLIC_OPEN 599, SECURITY_CLASSIFICATION=PUB 599, STATUS/SOURCE null 599, PRECISION=6 516 and null 83.
- Side matrix `IMF_BOP_39_COUNTRY_ANNUAL_CONTINUITY_SIDE_MATRIX_20261115.csv` (78 rows), SHA-256 `69840fa287cf14eb5d50e0ca51465720c315e1fda7b5bf1a594ad3777a7f805e`.
- Country summary `IMF_BOP_39_COUNTRY_ANNUAL_CONTINUITY_SUMMARY_20261115.csv` (39 rows), SHA-256 `3003f065ed3d1b459c5c932b19ab6882b4be4ccbe8968600d2d0391097842259`.
- Detailed JSON `IMF_BOP_39_COUNTRY_ANNUAL_CONTINUITY_AUDIT_20261115.json`, SHA-256 `090174bf4f89750c5425f779a8dda826345ab51d05f31b94caf281aaf6baa258`.
- Report: `docs/IMF_BOP_39_COUNTRY_ANNUAL_CONTINUITY_AND_SIX_COUNTRY_GAP_AUDIT_20261115.md`, commit `67a317db18b4d1ba56576be6572b97d1d2953cc3`.
- Manifest: `data/research/imf_bop_39_country_annual_continuity_audit_20261115.manifest.json`, commit `01f3bbae00fe237e6ff19a2f772072cacb1bdacc`.
- Decision: descriptive annual continuity audit PASS; 26-year annual completeness demonstrated only for nine countries; quarterly reporter eligibility remains UNKNOWN; quarterly coverage acceptance NOT PASS; EMDE aggregation BLOCKED.
- Next: official country-specific IMF reporting metadata / dataflow constraint investigation for CAF, ERI, GNQ, SOM, TCD, TKM. Keep all annual gaps explicit. ₹0 spend; all V11.3 protected invariants unchanged.


## 2026-11-15 — Six-country official BPM6 reporting-basis and SDMX constraint cross-check

- Investigated six no-nonempty-annual reporters: CAF, ERI, GNQ, SOM, TCD, TKM.
- Reviewed IMF public PDF "Availability of Official BPM6 Basis Balance of Payments and International Investment Position Data", April 2025, complete two-page table. The six target countries are not listed in that edition's country table for official own-reported BPM6 BOP start dates. The document footnote states that official BPM6-basis availability reflects own-reported BPM6 data included in the publication; earlier periods and economies not yet providing official BPM6 estimates are IMF-converted BPM5 estimates.
- Interpretation is bounded to April 2025 publication inventory only. It does not prove formal ineligibility, non-reporting, absence of BPM5 data, or lack of later BPM6 submissions. All six eligibility statuses remain UNKNOWN.
- A later document "Economies Reporting on BPM6 Basis October 2025" published 2026-05-14 is indexed on IMF BOP Documents, but its PDF body was not retrieved/inspected. It is an explicit next action, not evidence used in current country conclusions.
- IMF SDMX Central visible Reporting Constraints registry lists `IMF:BOP6_CONSTRAINT` for `BOP6[1.0]` and `IMF:BOP_BP6_CONSTRAINT` for `BOP_BPM6[1.0]`. Neither is demonstrated to target exact `IMF.STA:BOP(21.0.0)` / `DSD_BOP(24.0.0)`; do not transfer these constraints across flows. SDMX Central overview documents that constraints can apply at DSD, Dataflow, Provision Agreement and Data Provider levels, and can define allowed/restricted series/partial series.
- Official sources reviewed: IMF April 2025 BPM6 availability PDF; IMF BOP dataset page; IMF SDMX Central Reporting Constraints and overview pages. URLs recorded in report.
- Report: `docs/IMF_BOP_SIX_COUNTRY_OFFICIAL_BPM6_AND_CONSTRAINT_CROSSCHECK_20261115.md`, commit `3112e6ba17daa598fc14ea5825f30c88aa645d94`.
- Gate: historical publication table review PASS; October 2025 later table NOT_RETRIEVED; exact IMF.STA BOP applicable constraints UNKNOWN; six-country formal eligibility UNKNOWN; quarterly coverage NOT PASS; EMDE aggregation BLOCKED.
- Next: retrieve/inspect October 2025 BPM6 reporting table (published 2026-05-14), then resolve exact BOP dataflow + provision agreement + provider constraint references. Preserve UNKNOWN until exact evidence. ₹0 spend; all V11.3 invariants unchanged.


## 2026-11-15 — October 2025 BPM6 document retrieval-status audit

- Official IMF Documents catalogue and official BOP dataset page both verify the existence of "Economies Reporting on BPM6 Basis October 2025", publication date 14 May 2026, BOP/IIP dataset association, Public or Unrestricted classification, PDF format. Catalogue item ID exposed by search metadata: `1792656603400855000`.
- The catalogue landing page extraction exposed metadata but not a direct PDF URL/body. PDF binary and complete country table were NOT_RETRIEVED. No six-country row presence/absence conclusion is made from this October 2025 edition. April 2025 evidence remains historical only.
- Official SDMX Central Structure Web Service page confirms REST entry point `https://sdmxcentral.imf.org/sdmx/v2/` and structural query capability for Dataflows, DSDs and Provision Agreements. Exact `IMF.STA:BOP(21.0.0)` Dataflow structure and its references were not retrieved. A guessed REST path was inaccessible and is explicitly not treated as evidence of artefact absence.
- Registry constraints page lists BOP6 and BOP_BP6 constraints for different structures; no proof they apply to `IMF.STA:BOP(21.0.0)` / `DSD_BOP(24.0.0)`. Provision Agreement, Data Provider and provider-level constraint remain UNKNOWN.
- Report: `docs/IMF_OCTOBER_2025_BPM6_DOCUMENT_RETRIEVAL_STATUS_AUDIT_20261115.md`, commit `639e56f98623c2ea50c347ea7b522fd26e8ae342`.
- Gate: official catalogue metadata PASS; October 2025 PDF content NOT_RETRIEVED; exact dataflow/provision/provider constraints UNKNOWN; six-country eligibility UNKNOWN; quarterly coverage NOT PASS; EMDE aggregation BLOCKED.
- Next retrieval must use the actual IMF catalogue item download/content URL for item `1792656603400855000`, then preserve PDF/hash and inspect all pages; separately use SDMX Central Structure UI to retrieve actual Dataflow references and follow returned Provision Agreement/Provider references. Do not guess IDs or reuse similarly named BOP6 constraints.
- ₹0 spend; no synthetic data, aggregation, annual-to-quarterly conversion, PR merge or production changes. All protected V11.3 invariants unchanged.


## 2026-11-15 — SDMX retrieval follow-up

- Fresh official IMF Documents catalogue and BOP dataset page inspection reconfirmed "Economies Reporting on BPM6 Basis October 2025", publication date 14 May 2026, but no PDF download target/body was exposed.
- IMF SDMX Central REST Web Service page and Web Services Guide confirm the UI can generate structure queries and supports Dataflow and Provision Agreement queries. Registry overview is paginated; visible sample does not establish absence of IMF.STA BOP dataflow.
- Direct guessed path `/sdmx/v2/structure/dataflow/IMF.STA/BOP/21.0.0` could not be retrieved via web page extraction. This is an access limitation, not evidence of nonexistence.
- Sources recorded in report `docs/IMF_OCTOBER_2025_BPM6_DOCUMENT_RETRIEVAL_STATUS_AUDIT_20261115.md`; updated report commit `2ce23ed9aabf69eac321864c0f79056af1c9fedd`.
- Gate remains unchanged: October 2025 PDF table NOT_RETRIEVED; exact Dataflow / Provision Agreement / Provider constraints UNKNOWN; six-country eligibility UNKNOWN; quarterly coverage NOT PASS; EMDE aggregation BLOCKED.


## 2026-11-15 — IMF SDMX API contract validation

- Inspected official IMF SDMX Central Web Services Guide (May 2025). Confirmed REST base `https://sdmxcentral.imf.org/sdmx/v2/`, supported structure resources including dataflow, provisionagreement, dataproviderscheme and content/actual/allowed/attachment constraints, and references query parameter semantics.
- Exact documented-contract target query prepared: `https://sdmxcentral.imf.org/sdmx/v2/structure/dataflow/IMF.STA/BOP/21.0.0?references=all&format=sdmx-2.1`. This is a query specification, not a retrieved response.
- Direct web retrieval attempts for target Dataflow, broad IMF Dataflow listing, ContentConstraint and ProvisionAgreement listing were inaccessible via the retrieval interface. This does not prove absence and is not origin HTTP evidence.
- IMF:BOP6_CONSTRAINT → BOP6[1.0] and IMF:BOP_BP6_CONSTRAINT → BOP_BPM6[1.0] remain unrelated until an actual reference ties them to IMF.STA:BOP(21.0.0).
- Updated report: `docs/IMF_OCTOBER_2025_BPM6_DOCUMENT_RETRIEVAL_STATUS_AUDIT_20261115.md`, commit `85c1cee4a9578bddcc6a9d63d9d3c3e82fa6b991`.
- Gate: API contract/query specification PASS; target Dataflow response NOT_RETRIEVED; target Provision Agreement/Provider/Constraint UNKNOWN; six-country eligibility UNKNOWN; quarterly coverage NOT PASS; EMDE aggregation BLOCKED.


## 2026-11-15 — IMF SDMX live registry page cross-check

- Live Dataflow overview is paginated (216 entries); first visible page contains CBSL/ESTAT entries, including ESTAT BPM6_BOP_M and BPM6_BOP_Q. This is not a complete IMF listing and cannot prove absence of IMF.STA:BOP.
- Live constraints list explicitly shows `IMF:BOP6_CONSTRAINT` → `BOP6[1.0]` and `IMF:BOP_BP6_CONSTRAINT` → `BOP_BPM6[1.0]`. Neither visible row identifies `IMF.STA:BOP(21.0.0)` or `IMF.STA:DSD_BOP(24.0.0)`; no applicability inferred.
- Provision Agreements view is paginated (1,001 entries); visible entries include `IMF:AT_BOP`, `IMF:BE_BOP` but no exact target reference established. Registrations view separately exposes Dataflow/Data Provider/URL; registrations for BOP6/BOP_BPM6/BOP_GBPM6 are not transferred to the target IMF.STA flow.
- REST Web Service UI provides Structure Type, Agency, ID, Version, References and Download. Exact manual procedure recorded in the audit report: select Dataflow, Agency IMF.STA only if actually offered, ID BOP, version 21.0.0, references All; inspect generated URL and download; preserve raw response/hash; do not substitute similarly named flows.
- Official registry overview confirms constraint cascade across DSD, Dataflow, Provision Agreement and Provider.
- Report updated: `11545f9f4dd3eeeab7f1a835dd33b8df2a01b4a3`.
- Gate: registry-page cross-check PASS; exact target Dataflow/references NOT_RETRIEVED; six-country eligibility UNKNOWN; quarterly coverage NOT PASS; EMDE aggregation BLOCKED.


## 2026-11-15 — Critical IMF SDMX namespace correction

- Live IMF SDMX Central REST UI Agency selector visibly offers `IMF`, not `IMF.STA`; live DSD catalogue lists `IMF:BOP` latest version `2.6.0`, "Balance of Payments and International Investment Position".
- The earlier `IMF.STA/BOP/21.0.0` target is therefore invalid as a confirmed selection in the SDMX Central UI. It is marked SUPERSEDED / INVALID FOR THAT UI only; this does not establish the dataset identifier itself is invalid.
- A separate public IMF Data Portal service catalogue lists `https://api.imf.org/external/sdmx/2.1` and `.../3.0`, distinct from SDMX Central `https://sdmxcentral.imf.org/sdmx/v2/`. Dataset identifiers must not be transplanted between services.
- Next: query SDMX Central `IMF:BOP(2.6.0)` DSD with References=All and separately resolve IMF Data Portal dataset through its own catalogue. Follow provider/provision references only when actually returned.
- Report updated: `f8e2d260664f62ecc1175b2266ffaa6d298364b0`.
- Gate: namespace/catalogue cross-check PASS; IMF:BOP(2.6.0) DSD response NOT_RETRIEVED; separate IMF Data Portal structure response NOT_RETRIEVED; constraints/provision/provider UNKNOWN; October 2025 PDF table NOT_RETRIEVED; six-country eligibility UNKNOWN; quarterly coverage NOT PASS; EMDE aggregation BLOCKED.


## 2026-11-15 — Canonical SDMx Global Registry BOP DSD endpoint

- Official SDMx BOP DSD page identifies SDMx Global Registry as the public unauthenticated host for BOP DSD and related dataflows/constraints; BOP DSD v2.6.0, maintenance agency IMF, with SDMX-ML 2.1 and SDMX 3.0 links. Page says DSD versions are maintained annually and older versions may remain valid where backward compatibility is preserved.
- Exact SDMX-ML 2.1 URL from official link: `https://registry.sdmx.org/sdmx/v2/structure/datastructure/IMF/BOP/2.6.0/?format=sdmx-2.1`.
- References query prepared: `https://registry.sdmx.org/sdmx/v2/structure/datastructure/IMF/BOP/2.6.0/?format=sdmx-2.1&references=all`.
- Web retrieval interface could not render XML (unsupported content-type application/xml) and reported references query inaccessible. This is a client limitation, not origin failure, absence, or successful XML inspection. No DSD dimensions, codelists, dataflows or constraints extracted.
- Do not assume SDMx Global Registry BOP DSD v2.6.0 is equivalent to the original IMF.STA BOP dataset reference. No cross-service equivalence asserted.
- Updated report: `97e96d40d91c43b789c95bf374cd23d46e3fe074`.
- Gate: canonical DSD endpoint discovery PASS; XML body/references NOT_RETRIEVED; IMF Data Portal dataset structure NOT_RETRIEVED; exact constraints/provision/provider UNKNOWN; October 2025 PDF table NOT_RETRIEVED; six-country eligibility UNKNOWN; quarterly coverage NOT PASS; EMDE aggregation BLOCKED.


## 2026-11-15 — Official service-catalogue and retrieval-channel audit

- SDMX Global Registry Web Service UI confirms unauthenticated REST base `https://registry.sdmx.org/sdmx/v2/`, Data Structure/Dataflow/Provision Agreement types, SDMX-ML v2.1/v3.0, References=All and Download control.
- Official SDMx BOP page confirms IMF-maintained BOP DSD v2.6.0 and SDMX-ML 2.1/3.0 links. Older DSDs may remain valid when backward compatible; no compatibility conclusion is made for IMF.STA dataset.
- Public SDMX service catalogue distinguishes IMF Data Portal 2.1/3.0 (`api.imf.org/external/sdmx/2.1`, `.../3.0`) from IMF SDMX Central services. Do not mix IDs across services.
- IMF API help page says Swagger explorer requires beta portal account sign-in. No credentials requested or used.
- Direct XML endpoint retrieval attempted; web interface could not render XML media type and container download failed. XML bytes/hash/DSD components/references NOT_RETRIEVED. Official package CIRCABC link returned 404 through retrieval layer; no origin-server conclusion.
- October 2025 PDF metadata is verified, but PDF body remains NOT_RETRIEVED; no six-country inference.
- Updated report: `d0f67acf2e09d9b85c148a10a9aabad8a269c533`.
- Gate: service catalogue + unauthenticated registry route PASS; XML NOT_RETRIEVED; API Swagger requires beta login and was not accessed; exact constraints/provision/provider UNKNOWN; October PDF table NOT_RETRIEVED; six-country eligibility UNKNOWN; quarterly coverage NOT PASS; EMDE aggregation BLOCKED.


## 2026-11-15 — IMF BOP concept scheme and candidate codelist inventory

- SDMx Global Registry Concept Scheme catalogue lists `IMF:CS_BOP(1.20.0)`, "Balance of Payments Concept Scheme".
- Codelist catalogue visibly lists IMF: `CL_ACCOUNT_ENTRY(1.5.0)`, `CL_ACCOUNTS_ITEM(1.8.0)`, `CL_ADJUSTMENT(1.4)`, `CL_AREA(2.0.0)`, `CL_COMP_METHOD(1.2)`, `CL_CURRENCY(1.6.1)`, `CL_FSENTRY(1.1)`, `CL_FUNCTIONAL_CAT(1.10.1)`, `CL_GFSM_STO(1.0)`, `CL_ORGANISATION(2.1.0)`, `CL_TIME_COLLECT(1.0)`, `CL_UNIT(1.19.0)`.
- These are candidate dependencies by subject matter only. Without BOP DSD XML, none is asserted to be referenced by BOP DSD 2.6.0 or the earlier IMF.STA BOP dataset.
- Concept Scheme page is dynamic; full concept items not exposed by retrieved page; direct URN query inaccessible. No concept IDs/representations inferred.
- Next: retrieve CS_BOP actual export through Global Registry UI, preserve/hash response, then follow only exact references from DSD/concept scheme. Do not assume codelist attachment or cross-service version compatibility.
- Updated report: `6a0d38844569e320360df2ce8e7a8b91824654ff`.
- Gate: CS_BOP identity/version and candidate codelist inventory PASS; actual concept content NOT_RETRIEVED; DSD-to-codelist linkage UNKNOWN; target constraints/provision/provider UNKNOWN; October PDF table NOT_RETRIEVED; six-country eligibility UNKNOWN; quarterly coverage NOT PASS; EMDE aggregation BLOCKED.


## 2026-11-15 — Registry-native cross-reference route

- Official Structure References UI supports selecting structure type, agency and structure and generating cross-reference reports; the all-structures workbook contains maintainable and identifiable cross-reference worksheets.
- Official Export Reports UI offers XLSX exports for Concept Usage (Concept Schemes referenced by Data Structures), Codelist Usage (Codelists referenced by Data Structures), Data Structures Report and Codelist Report.
- Concept Scheme detail UI offers References, Export SDMX-ML 3.0, Export Excel and View Concept Scheme; the detail grid exposes Id, Name, Representation and Description.
- REST Structure UI exposes type, agency, ID, version, format, detail and references selectors, generated query URL and Download. Browser-native download is the correct next route after web text extraction could not render XML.
- Next execution: Structure References for IMF:CS_BOP(1.20.0) and IMF:BOP(2.6.0); download cross-reference reports; run Concept Usage and Codelist Usage XLSX; filter exact IMF structures; export CS_BOP concept detail; follow only actual returned refs.
- Actual reports/XLSX and hashes NOT_YET_DOWNLOADED. Exact CS_BOP-to-BOP DSD link UNKNOWN; DSD-to-codelist links UNKNOWN; target constraints/provision/provider UNKNOWN; October PDF body NOT_RETRIEVED; six-country eligibility UNKNOWN; quarterly coverage NOT PASS; EMDE aggregation BLOCKED.
- Updated report: `8e47f1eb563260fb5c483187cfaa867ab76805e3`.
- No credentials, paid services, external contact, synthetic data or production changes.


## 2026-11-15 — Registry Dataflow inventory cross-check

- Verified catalogue entries: IMF:BOP DSD v2.6.0; IMF:CS_BOP Concept Scheme v1.20.0.
- Dataflow catalogue visibly lists ESTAT:BPM6_BOP_M v2.6.0 and ESTAT:BPM6_BOP_Q v2.6.0 as ESTAT agency dataflows. They are not IMF agency dataflows and cannot be substituted for the IMF Data Portal BOP target.
- Data Providers catalogue shows ESTAT:IMF = IMF as a provider under ESTAT agency; this alone does not establish a BOP Provision Agreement, registration or constraint chain.
- Registry documentation says constraints may be attached to DSD, Dataflow, Data Provider or Provision Agreement and cascade.
- Structure References and XLSX export pages expose UI controls, but browser text retrieval does not expose populated selectors, generated report bytes, download URLs or payload hashes. Registry REST SDMX-ML retrieval via text interface remains inaccessible; this is not evidence of origin failure.
- Actual reports/SDMX-ML and hashes NOT_ACQUIRED. Exact IMF target Dataflow/Provision Agreement/provider registration/constraints UNKNOWN; CS_BOP-to-BOP and BOP-to-codelist references UNKNOWN; October 2025 PDF NOT_RETRIEVED; six-country eligibility UNKNOWN; quarterly coverage NOT PASS; EMDE aggregation BLOCKED.
- Updated audit report commit: `e880b697f8abb4a0461110b2383e9852f4b5b583`.
- No credentials, paid services, external contact, synthetic data or production changes.


## 2026-11-15 — IMF BOP dataset and October 2025 document metadata

- Official BOP dataset page identifies IMF Statistics Department (STA), Annual and Quarterly frequency, and API/View Data/Download/Document navigation.
- Official October 2025 BPM6 reporting document catalogue item `1792656603400855000`: published 14 May 2026; associated with BOP and IIP; Public or Unrestricted; PDF.
- These are catalogue metadata findings only. PDF body/table bytes were not retrieved; six-country October inclusion/exclusion remains UNKNOWN. No quarterly eligibility or coverage PASS inferred.
- BOP dataset metadata VERIFIED; document metadata VERIFIED; PDF bytes/body NOT_RETRIEVED; six-country eligibility UNKNOWN; quarterly coverage NOT PASS; EMDE aggregation BLOCKED.
- Audit report commit: `a0f4fb1d8c0132090b1652f25b71507868bbcae1`.
- No credentials, paid services, external contact, synthetic data or production changes used.


## 2026-11-15 — IMF BOP/IIP aggregate methodology safeguard

- Official IMF BOP/IIP World and Country Group Aggregates page states country-group/world aggregates (except Euro Area) combine reported country data with estimates for nonreporting economies, using sources including WEO and External Wealth of Nations. Country-level information is based on direct IMF reports or National Summary Data Pages, with stated Fund Accounts exception for accounts between economies and IMF.
- Therefore published EMDE/world aggregates do not prove every member country has directly reported quarterly data. Aggregate values cannot substitute for reporter-level observations or establish eligibility. Where decomposition is not exposed, reporter/nonreporter contribution is UNKNOWN.
- Preserve hard gate: no EMDE aggregate promotion until reporter-level coverage and provenance are independently established; no estimate backfill or synthetic rows.
- Methodology statement VERIFIED; October 2025 PDF bytes/body NOT_RETRIEVED; six-country October inclusion UNKNOWN; quarterly eligibility UNKNOWN; quarterly coverage NOT PASS; EMDE aggregation BLOCKED.
- Updated audit report commit: `b04b09e1ae82847375d0dc333af62004423b6e10`.
- No data rows created, estimates substituted, credentials/paid services/external contact or production changes.

## 2026-11-15 — Progress accounting and no-repeat control

- October 2025 BPM6 PDF retrieval/country-table package is 25% (1/4 defined milestones): official catalogue metadata PASS; direct PDF download target NOT_DONE; PDF bytes+SHA-256 NOT_DONE; country-table extraction and six-country comparison NOT_DONE. No country eligibility conclusion.
- IMF BOP workstream acceptance remains 5/7 = 71.4% on the pre-existing rubric. Catalogue metadata re-verification and aggregate methodology safeguard do not add gates or promote acceptance.
- Full PRECISION-WIRES V11.3 overall progress remains NOT_CALCULABLE: current full-workstream denominators and approved weights are not reconciled, and earlier P0/Factor/Regime/Event Study statuses need revalidation. Never substitute IMF 71.4% for project-wide progress.
- No-repeat: do not repeat IMF item 1792656603400855000 metadata search, April 2025 six-country inventory review, 39-country annual audits, or successful 110-row India acquisition/reconciliation without new evidence/code. Next action is direct PDF file target resolution through official document-item download action; if inaccessible, log limitation and pivot to another unresolved gate.
- No new country-level evidence from this reconciliation. No credentials, paid services, synthetic data, external contact or production changes.
- Updated audit report commit: cfa2cd8f6a7f71ba16b6525354d4b252fa61bd92.

## 2026-11-15 — India 110-row vintage/revision readiness audit

- Read committed CSV and JSON manifest directly; no API reacquisition or data mutation.
- CSV has 110 rows; four exact series counts 11/11/44/44; zero duplicate series-period keys. Manifest declares 110 rows, matching four response hashes and series row counts.
- Header has 20 columns and no vintage/revision/release/retrieval/publication timestamp field. SOURCE, STATUS, ACCESS_SHARING_NOTES and OVERLAP are null in all 110 rows. IFS_FLAG true on 55 asset rows and null on 55 liability rows (null remains UNKNOWN). SCALE=6, PRECISION=6, DERIVATION_TYPE=O, ACCESS_SHARING_LEVEL=PUBLIC_OPEN, SECURITY_CLASSIFICATION=PUB across 110 rows.
- Response SHA is one archived response per series, not a revision timeline. Do not infer values were never revised or treat this as first-release data.
- Bounded audit completion: 100% of defined structural checks; outcome for revision/vintage gate is NOT_READY / NOT_ESTABLISHED. Next action: find official public IMF vintage/revision endpoint or reproducible release archive; absent that, keep revision acceptance UNKNOWN and restrict scope to current archived values.
- IMF BOP accepted gates remain 5/7 (71.4%). October 2025 PDF retrieval package remains 25% (1/4). Full project progress remains NOT_CALCULABLE.
- No new observation values, no credentials, paid services, synthetic data, external contact, PR merge or production changes.
- Updated audit report commit: e743e93ac6ae1f7f15aad13fe92a7b1925d56ee3.

## 2026-11-15 — India panel extraction-contract compliance matrix

- Compared Section 3/5 required fields in `IMF_BOP_PORTFOLIO_FLOW_EXTRACTION_SPEC_V1.md` against committed 110-row CSV and manifest. All 16 defined elements reviewed (bounded audit 100% complete); no data re-acquisition or mutation.
- Present: IND country, frequency/period, BPM6, Portal dataflow/version in manifest, exact dimensions, A_NFA_T/L_NIL_T direction, P_F total-portfolio indicator, USD/SCALE metadata, OBS_VALUE, source-response hashes and combined CSV hash.
- Partial: instrument scope (P_F total only, no equity/debt split); observation status/confidentiality (DERIVATION_TYPE=O and public flags present but STATUS null and no OBS_STATUS/CONF_STATUS); source URL/dataset id is in companion provenance, not row-level; key uniqueness checked only within one captured snapshot because vintage dimension absent.
- Missing: per-response retrieval timestamp UTC and publication/release vintage. Do not fabricate them or use audit date as substitute.
- Outcome: revision-aware extraction contract PARTIAL / NOT_READY. Keep current 110-row data as one archived snapshot; do not claim first-release or revision-complete observations.
- Next distinct action: design a separate research-only provenance sidecar schema for future pulls, recording actual timestamp, final URL, HTTP status, Content-Type, bytes, SHA-256 and source-supplied release vintage; unknown vintage stays null/UNKNOWN. Do not mutate existing CSV or production.
- Bounded audit progress 100%; IMF BOP workstream 5/7=71.4%; October PDF package 25%; overall V11.3 project progress NOT_CALCULABLE.
- Updated audit report commit: 2989920fbfeddbfff129cc89d993a36eb033f240.
- No credentials, paid services, synthetic data/timestamps, external contact, PR merge or production changes.

## 2026-11-15 — IMF BOP response provenance sidecar schema V1

- Created `schemas/imf_bop_response_provenance.schema.json` (JSON Schema 2020-12) and `docs/IMF_BOP_RESPONSE_PROVENANCE_SIDECAR_V1.md` on `research/imf-bop-access-audit-v1`.
- Mandatory fields: exact requested/final URL, GET, exact series key, HTTP 200, Content-Type, actual UTC retrieval timestamp, positive response byte count, SHA-256 of exact raw response-body bytes, explicit vintage status and research controls.
- Vintage statuses distinguish SOURCE_PROVIDED / NOT_EXPOSED_BY_SOURCE / NOT_VERIFIED. Null release date/ID required when source does not expose vintage or verification is incomplete. Retrieval timestamp must never substitute for release vintage.
- One sidecar per independently retrieved raw response. Reject non-200/empty responses, missing provenance, malformed hash, schema violations and inconsistent vintage status.
- Existing India 110-row CSV/manifest remain unchanged and are not retroactively compliant. No fabricated timestamps/vintage or new observations created.
- Schema and documentation creation completed; remote file re-fetch verified. Live sidecar instance validation against a new real IMF response NOT_DONE; revision-aware panel gate remains NOT_READY.
- No credentials, paid source, synthetic data, production change or PR merge.
- Report update commit: 0f48d414d9c5ca99f26248c75a0ec754b1b49099.

## 2026-11-15 — Official IMF BOP Portal vintage affordance audit

- Inspected exact official BOP dataset page. It exposes API, VIEW DATA, DOWNLOAD, Metadata and Documents; retrieved page does not expose a visible "See Vintages" action or vintage-history section.
- BOP API link redirects to developer-portal sign-in. IMF API documentation confirms SDMX 2.1/3.0 and beta-account sign-in for Swagger exploration.
- Other IMF datasets (e.g. WEO and selected MFS) show "See Vintages"; this does not prove BOP has the same capability.
- BPM7 defines vintage by public release period for a data value/dataset; retrieval timestamp is not vintage.
- Decision: BOP page vintage affordance NOT_EXPOSED; public BOP vintage endpoint/history selector NOT_ESTABLISHED; India panel revision history UNKNOWN / NOT_READY. This is a bounded UI finding, not proof no authenticated/internal/archive capability exists.
- Next avenue: official dated BOP publication/download archives; require two dated snapshots overlapping the same India series-period keys before revision comparisons.
- No login, credential, bypass, data mutation, new gate promotion, production change or PR merge.
- Audit report update commit: d01e2cb26c6ef6d63e15bbed6bac1030ac4c7141.

## 2026-11-15 — Official IMF BOPSY annual-release archive avenue

- Identified official BOP_AGG dataset page: World and Country Group Aggregates, historically BOPSY, annual publication released each November.
- Inspected official BOPSY 2025 Explanatory Notes (November 2025), BOP Introductory Notes (November 2024), and IMF BOPCOM annual reports 2024/2025.
- Evidence establishes BOPSY 2024 country BOP/IIP data through 2023 and BOPSY 2025 through 2024; 2025 notes list India last reported BOP period 2024.
- Critical source boundary: these notes are not raw observation snapshots for the exact IMF.STA:BOP(21.0.0) India keys. BOP_AGG group/world aggregates may include estimates; do not treat them as reporter observations or exact-series vintages.
- The SDMX pilot BOP page is last updated 2013 and is not a recent vintage archive.
- Outcome: annual publication-document lineage PASS; exact India raw snapshot pair NOT_DONE; revision comparison NOT_DONE; revision/vintage readiness UNKNOWN / NOT_READY.
- Next action: inspect BOP_AGG View Data/Download only to determine whether individual country tables can be exported as raw country observations with an identifiable release vintage. Require exact series/dimension match; otherwise reject as non-equivalent.
- No data/CSV/manifest mutation, no inferred vintage, no new gate promotion, no production change or PR merge.
- Report update commit: f83f7b5dadfc7294abc6779a10dff88308f389b6.

## 2026-11-15 — BOPSY country-table export affordance audit

- Retrieved and inspected the complete official 31-page November 2025 BOPSY Explanatory Notes PDF.
- It states individual country tables are in the "Summary of International Transactions and Positions" table and data can be customized for viewing/download (PDF pp. 3-4). India BOP last reported period is 2024 (PDF p. 8).
- The notes distinguish reported country-level information from world/group aggregates that can include WEO/EWN estimates for nonreporting economies. Aggregates are not reporter observations.
- Public BOP_AGG page exposes VIEW DATA and DOWNLOAD controls; underlying table schema/export payload was not available in the retrieved public page text.
- Exact India P_F series mapping, downloadable dated raw snapshot, and a second overlapping vintage remain UNKNOWN / NOT_DONE. Revision/vintage readiness remains NOT_READY.
- Next action: resolve the official "Summary of International Transactions and Positions" dashboard/export target, then test one India country table export and inspect exact dimensions before any bulk retrieval.
- No CSV/manifest mutation, no vintage inference, no gate promotion, no production changes, no PR merge.
- Audit report update commit: 5a2d4187ffef4391234c2f54a9e0f686773953c3.

## 2026-11-15 — BOPSY dashboard target resolution

- Resolved the BOP_AGG dataset's official Dashboard Release link to the IMF Data report page "BOPSY Dashboard", publication date 19 November 2025, associated with the BOP_AGG dataset.
- Public page representation exposes report identity/date/dataset association but not embedded report payload, direct Power BI embed URL, table visual metadata, export URL, raw downloadable payload, or schema. IMF Tables catalogue page representation likewise exposed only its shell.
- Dashboard identity/dataset association PASS; direct table/export target NOT_ESTABLISHED; country table raw payload/schema NOT_DONE; India P_F exact mapping UNKNOWN; dated raw snapshot pair NOT_DONE.
- Revision/vintage readiness remains UNKNOWN / NOT_READY. This bounded inspection does not prove no export exists in the interactive dashboard or authenticated environment.
- No login/bypass, undocumented API inference, aggregate substitution, data mutation, or gate promotion.
- Next action: inspect only public interactive dashboard controls and officially exposed resource links; if no unauthenticated export target is available, stop at the access boundary.
- Audit report update commit: 50b8b9e8cae282419ff8b1aaf3e858bab47828b6.

## 2026-11-15 — Separate IMF BOP country dataset route

- Identified official IMF dataset page https://data.imf.org/Datasets/BOP, titled "Balance of Payments (BOP)", with API, VIEW DATA, DOWNLOAD, Metadata; annual and quarterly frequency.
- This is distinct from BOP_AGG/BOPSY World and Country Group Aggregates. It is the more direct official country-level BOP candidate; do not substitute BOP_AGG group/world aggregates.
- Official IMF API documentation says SDMX 2.1/3.0; Swagger explorer requires beta portal sign-in. No sign-in or bypass used.
- Dataset page identity/frequency DISCOVERED; exact page-to-dataflow/DSD mapping, India series-key revalidation, raw dated country download, and two-vintage overlap remain NOT_DONE/UNKNOWN.
- Next action: inspect official BOP metadata and VIEW DATA/DOWNLOAD targets; confirm exact version/dimensions and India series keys against known IMF.STA:BOP(21.0.0)/DSD_BOP(24.0.0), then one small provenance-sidecar-backed test only.
- No bulk pull, CSV/manifest mutation, vintage inference, gate promotion, production changes or PR merge.
- Audit report update commit: eb457df653fe82d10e9caaef6dd8e2ef15c3464c.

## 2026-11-15 — IMF BOP identifier/API boundary revalidation

- Official page URL `https://data.imf.org/en/datasets/IMF.STA:BOP` confirms portal dataset identifier `IMF.STA:BOP`, BOP title, API link, VIEW DATA and DOWNLOAD controls.
- API link redirects to `portal.api.imf.org/signin?returnUrl=/apis`; IMF API docs specify SDMX 2.1/3.0 and beta portal account sign-in for Swagger exploration.
- Current public page text does not expose version strings. Keep page-level identifier `IMF.STA:BOP` distinct from the earlier exact versioned extraction contract `IMF.STA:BOP(21.0.0)` / `DSD_BOP(24.0.0)`. Existing successful raw response/manifest evidence remains authoritative for that earlier contract.
- Page identifier PASS; anonymous direct API schema discovery NOT_AVAILABLE through documented Swagger; current versioned DSD revalidation NOT_ESTABLISHED; no new vintage evidence; revision readiness UNKNOWN / NOT_READY.
- No login, bypass, undocumented endpoint probing, data mutation, or gate promotion.
- Next safe step: use existing archived exact-version responses/manifest as the extraction contract; only pursue a public metadata/export endpoint if officially exposed.
- Audit report update commit: ba131d01dcfc0e0764b578db46553c12b35ad802.

## 2026-11-15 — Historical India provenance sidecar compatibility audit

- Re-fetched V1 JSON Schema, sidecar specification, India CSV and manifest; parsed schema/manifest JSON and checked structure and exact series identity.
- Schema/manifest JSON valid; seven required schema groups present; four exact India series keys match; all four response hashes have valid SHA-256 syntax and positive response byte counts.
- CSV has 110 rows, 20 columns, 11/11/44/44 series rows and 110 unique series-period keys. Per-row source-response hash column exists.
- Historical CSV/manifest do not contain retrieval UTC timestamps, requested/final URLs, HTTP status, Content-Type, or query-parameter objects. Exact raw response body bytes are not present in the audited archive paths; hash+byte count cannot reconstruct them.
- Existing V1 sidecar instances therefore REJECTED / NOT_READY for all four historical responses. Do not fabricate fields or retro-create incomplete sidecars. Vintage status remains NOT_VERIFIED / UNKNOWN; revision-aware eligibility NOT_READY.
- Existing CSV, manifest and historical hashes untouched. New compliant sidecar only during a future real HTTP GET capturing exact raw body bytes and transport metadata at acquisition time.
- No new IMF pull, spend, production change, PR merge, or acceptance-gate promotion.
- Audit report update commit: 57c6478aa4cfc5bc396ab1b9def717616a4f1dd9.

## 2026-11-15 — Original India raw response artifacts recovered; four sidecars created

- Recovered original workflow artifacts 14125515371 (run 43623518481) and 14122421554 (run 43616059985); no new IMF API pull.
- Exact body bytes recovered and SHA-256/byte count independently rechecked: annual assets 7,845 / 85cca14c…e23a; annual liabilities 7,846 / 6eba68f8…a4e4; quarterly assets 10,201 / aff39180…d24f; quarterly liabilities 10,185 / 6ebe3c2e…8ccc. All match prior manifest/capture metadata.
- All four original capture records preserve HTTP 200, SDMX Content-Type, requested/final URLs, GET acquisition, exact series key, query parameters and actual UTC retrieval timestamp.
- Created four V1 sidecars under `data/research/provenance/` (annual assets, annual liabilities, quarterly assets, quarterly liabilities). Vintage remains NOT_VERIFIED / UNKNOWN with null release date/ID; no vintage inferred from retrieval time.
- Historical body recovery 4/4 PASS; transport metadata completeness 4/4 PASS; sidecar creation 4/4 PASS; revision-aware eligibility remains NOT_READY pending source-vintage evidence and two dated overlapping releases.
- Existing CSV and manifest unchanged; no synthetic data, new IMF pull, production change, spend, PR merge or gate promotion.
- Audit report update commit: 70c411f5a140fa7fb82f20f781a54ba8156ba6ce.

## 2026-11-15 — Archived raw SDMX vintage-attribute inspection

- Inspected exact archived raw SDMX-JSON response bodies for all four India series from artifacts 14125515371 and 14122421554; no new HTTP request.
- All four bodies have `meta: {}`; no release/vintage field in response metadata.
- Dataset structure has metadata attributes including PUBLICATION_DATE and UPDATE_DATE, but no dedicated vintage/release identifier attribute.
- Dataset-level UPDATE_DATE values observed: `2026-11-07T14:56:50.476461500Z` and `2026-11-07T14:56:50.532906Z`. These are dataset-level update metadata, not per-response release IDs or proven vintages; do not promote them.
- Observation attributes: PRECISION, DERIVATION_TYPE, STATUS, ACCESS_SHARING_LEVEL, ACCESS_SHARING_NOTES, SECURITY_CLASSIFICATION, SOURCE; no observation-level vintage identifier. STATUS, ACCESS_SHARING_NOTES and SOURCE null in captured observations.
- Dataset source-methodology text lists possible source types (country authorities, NSDPs, ECB, IMF Staff Estimates) but does not identify the provenance of each India observation or direct-reported/estimated status.
- Raw vintage-field inspection complete; explicit source-supplied vintage not exposed in inspected structures. Sidecar vintage remains NOT_VERIFIED (retrospective inspection does not create an acquisition-time vintage declaration); revision readiness UNKNOWN / NOT_READY.
- Next: seek a second independently dated IMF snapshot with exact same series keys and overlapping periods. No CSV, manifest, sidecar, raw response, or accepted gate changed.
- Audit report update commit: 4c83d57546873f45b403979c7dbcf648ce4ab028.

## 2026-11-15 — Dated BOPSY 2024 publication snapshot suitability audit

- Located official IMF *Balance of Payments Statistics: Introductory Notes, as of November 2024* PDF. It states BOPSY electronic release contains individual country data for all available periods and world/regional aggregates for 2005–2023; country tables and metadata are online; BPM6 basis. India reporting currency listed as XDC (domestic currency).
- IMF Committee on BOP Statistics 2024 Annual Report independently confirms annual BOP/IIP statistics through 2023 were published in BOPSY 2024; 195 economies reported BOP data.
- Notes distinguish individual country tables from world/regional aggregates, where missing data may be estimated by IMF staff. Do not use aggregate values as reporter observations.
- Country-table documentation confirms portfolio investment assets/liabilities and equity/debt breakdown conceptually, but no archived raw India SDMX response, exact P_F/A_NFA_T/L_NIL_T mapping, or machine-readable four-series snapshot was retrieved.
- Dated publication lineage PASS; raw India BOPSY 2024 country export NOT_RETRIEVED; exact equivalence to IMF.STA:BOP(21.0.0)/DSD_BOP(24.0.0) NOT_ESTABLISHED; second comparable raw snapshot NOT_ESTABLISHED.
- BOPSY 2024 is not accepted as a second vintage for the existing 110-row panel. Revision/vintage readiness UNKNOWN / NOT_READY; no gate promotion.
- Next: pursue only an officially exposed dated country-table export if public and unauthenticated; require raw bytes, release evidence, exact keys and mapping. No hidden endpoint guesses/login bypass.
- Existing CSV, manifest, sidecars and raw responses unchanged.
- Audit report update commit: 58cd00d2e94fb9e813a7836014c5d97b08abaa97.

## 2026-11-15 — IMF November 2024 BOP release-calendar evidence

- Official IMF Data news page confirms BOPSY 2024 published 20 Nov 2024; country BPM6 tables cover 2011–2023 and 2005–2010 are in archive.
- Same page identifies a separate quarterly BOP/IIP release for 2024 Q2, released 20 Nov 2024, with quarterly BOP/IIP coverage across 190 countries since 1945.
- The official Q2 release link redirects to t.imfconnect.imf.org; following it timed out before revealing a public file/document. No raw country export or exact India series values retrieved.
- Release-calendar evidence PASS; raw file retrieval NOT_RETRIEVED; India exact series mapping NOT_ESTABLISHED; second comparable snapshot and revision comparison NOT_ESTABLISHED. Release date alone is not a vintage proof.
- Do not retry the same redirect or repeat BOPSY notes discovery. Search only for an independently indexed official document/file for this release; otherwise close this avenue NOT_RETRIEVED and pivot to a distinct official archive source.
- No data files or accepted gates changed.
- Audit report update commit: 55ad5c20043b81b54da67b5c223a9358a6091d2f.

## 2026-11-15 — IMF CPIS/PIP adjacent-dataset non-equivalence audit

- Identified official IMF dataset `IMF.STA:PIP`, "Portfolio Investment Positions by Counterpart Economy (formerly CPIS)", and Foreign Portfolio Investments Breakdown dashboard.
- Official description: holdings/positions in portfolio securities by counterpart economy and instrument (equity, long-term debt, short-term debt); annual and half-yearly/semester.
- Existing India BOP panel measures financial-account transaction flows: A_NFA_T / L_NIL_T, P_F, USD, annual/quarterly. PIP/CPIS measures positions/stocks, not transactions/flows.
- IMF BOP Introductory Notes distinguish financial-account net acquisition/incurrence transactions from IIP positions at a point in time; IIP changes also reflect revaluations and other volume changes.
- Decision: PIP/CPIS is NOT_EQUIVALENT and REJECTED as a second vintage, flow backfill or revision comparator. It may only support a separately approved stock/position analysis.
- No changes to existing data, mapping, acceptance gates or vintage status; BOP revision readiness remains UNKNOWN / NOT_READY.
- Next: only seek an archived official BOP flow country table/raw response matching the exact four keys; keep PIP out of current flow pipeline.
- Audit report update commit: 3f0559e7ee90ee8b09ba4944493355316e9d6299.

## 2026-11-15 — RBI official BPM6 quarterly BOP parallel-source contract

- Inspected RBI April 2026 *Comprehensive Guide for Current Statistics of the RBI Monthly Bulletin* (page published 8 Oct 2026).
- RBI Table 42 is Standard Presentation of India BoP as per BPM6, quarterly, US$ million, primary source RBI, revision policy "Data are subject to revision". It includes financial-account functional classification including Portfolio Investment and separate credit/debit/net presentation.
- RBI Table 43 is same BPM6 presentation in ₹ crore. Table 40 is a different overall BoP presentation; do not conflate. Table 44 is IIP stock positions, not flow.
- RBI says extended historical time series are available through DBIE in reusable formats; latest data may be provisional and revised.
- This is an independent official India BOP flow source for parallel-source validation, not an automatic replacement for IMF and not a second IMF vintage.
- Exact equivalence to IMF P_F / A_NFA_T / L_NIL_T four keys, direction/sign convention and quarter mapping UNKNOWN / NOT_ESTABLISHED. No DBIE export downloaded.
- Next: inspect DBIE Table 42 actual export/schema and two dated RBI Bulletin snapshots with overlapping quarters. Require exact separate portfolio assets/liabilities and documented sign/frequency mapping before comparison.
- Existing IMF CSV, manifest, sidecars, raw responses and gates unchanged.
- Audit report update commit: d0398f3947ace3aea09691d733b98d312347128a.


## 2026-11-15 — RBI Table 42 live publication snapshots and DBIE export-boundary audit
- Inspected actual official RBI Table 42 bulletin pages, moving beyond the earlier handbook-only source-contract check. The table visibly contains quarterly USD-million Credit/Debit/Net columns and financial-account Portfolio Investment total, Portfolio Investment in India/by India, equity/fund shares and debt securities.
- Two dated RBI Bulletin pages (25 Sep 2026 and 23 Oct 2026) overlap on Apr–Jun 2025 and show identical displayed values: total portfolio 146339/144731/1608; in India 145201/142720/2481; by India 1138/2011/−872; equity 123636/118245/5391; debt 21565/24475/−2910 (Credit/Debit/Net; US$ million). This is cross-publication consistency only, not evidence of a revision event or raw vintage snapshot pair.
- 22 Jul 2026 Table 42 page provides Jan–Mar 2025 and Jan–Mar 2026 (P), but is not used as an overlapping-period revision comparison with Apr–Jun 2025.
- DBIE surfaced page is annual (91 rows; 31-03-2012–31-03-2026) despite being labelled standard BPM6 USD BOP; it is not accepted as the quarterly Table 42 export. CSV/JSON links visible, raw export/schema NOT_RETRIEVED.
- Actual Table 42 schema view PASS; two dated bulletin pages with overlapping quarter PASS; DBIE quarterly raw export NOT_RETRIEVED; exact mapping of RBI credit/debit and "in India/by India" to IMF P_F/A_NFA_T/L_NIL_T UNKNOWN / NOT_ESTABLISHED. No direct sign conversion or series merge permitted.
- RBI remains independent parallel-source lineage, not an IMF vintage. No IMF gate promotion, no source data/CSV/manifest/sidecar mutation, no production change or PR merge.
- Bounded inspection task 100%; RBI export/mapping readiness NOT_READY; IMF BOP workstream 5/7=71.4%; October 2025 IMF PDF package 25%; overall V11.3 progress NOT_CALCULABLE.
- Sources: RBI Table 42 25 Sep 2026 https://www.rbi.org.in/Scripts/BS_ViewBulletin.aspx?Id=24495 ; 23 Oct 2026 https://rbi.org.in/Scripts/BS_ViewBulletin.aspx?Id=24566 ; 22 Jul 2026 https://rbi.org.in/Scripts/BS_ViewBulletin.aspx?Id=24352 ; DBIE annual dataset https://dbie.rbihub.in/tables?table=external_sector.r814_standard_presentation_of_india_s_balance_of_payments_as_pe .

## 2026-11-15 — RBI Table 42 to IMF BPM6 financial-account direction/sign crosswalk audit
- Re-inspected RBI current-statistics guide, actual Table 42 bulletin, RBI Balance of Payments Manual for India, IMF BPM6 Compilation Guide and IMF BOPCOM sign-convention note.
- RBI Table 42 publishes Portfolio Investment total, "in India" and "by India" with Credit/Debit/Net columns. RBI manual explains "in India" includes nonresident investments into India and separately describes India's portfolio investment abroad. This supports a conceptual directional clue (in India = liability-side direction; by India = asset-side direction), not an exact numerical series mapping.
- IMF BPM6 defines financial-account series as net acquisition of financial assets and net incurrence of liabilities; positive denotes increase and negative denotes decrease, with balance assets minus liabilities. RBI's displayed Credit-minus-Debit Net must not be assumed to equal either IMF series.
- RBI Table 42 guide/manual does not expose an explicit equation mapping Credit/Debit/Net to IMF A_NFA_T/L_NIL_T. Symmetrical instrument scope for both directions and exact P_F equivalence also NOT_ESTABLISHED.
- Decision: exact signed-flow crosswalk UNKNOWN / NOT_ESTABLISHED; do not sign-flip, map or merge. RBI remains separate parallel source. DBIE quarterly raw export NOT_RETRIEVED; prior annual DBIE table remains rejected as wrong frequency.
- Bounded crosswalk audit 100%; mapping gate NOT_ESTABLISHED; RBI raw export NOT_RETRIEVED; IMF BOP 5/7=71.4%; October 2025 IMF PDF 25%; overall V11.3 progress NOT_CALCULABLE.
- Next: seek official technical note/raw quarterly DBIE schema with explicit Credit/Debit-to-assets/liabilities mapping; if absent, retain NOT_ESTABLISHED.
- Sources: RBI guide https://www.rbi.org.in/scripts/PublicationsView.aspx?Id=24094 ; RBI Table 42 https://www.rbi.org.in/Scripts/BS_ViewBulletin.aspx?Id=24495 ; RBI BOP Manual https://www.rbi.org.in/scripts/PublicationsView.aspx?id=13013 ; IMF BPM6 Guide https://data.imf.org/-/media/iData/External-Storage/Documents/FB1F86C7158646DDB554D0882F1F2A3B/en/3-BPM6-com-guide.pdf ; IMF BOPCOM note https://www.imf.org/external/pubs/ft/bop/2013/13-13.pdf .
- No paid source, synthetic data, fabricated mapping, data-file mutation, PR merge or production change.

## 2026-11-15 — CORRECTION: RBI official BPM6 sign-convention crosswalk recovered
- Corrects the immediately preceding audit's claim that no official RBI sign rule was located. RBI Manual paragraphs 1.16 and 1.19 explicitly state: asset credit = decrease assets, asset debit = increase assets; liability credit = increase liabilities, liability debit = decrease liabilities. Financial-account changes are netted separately within each asset/liability type.
- RBI Working Group report confirms assets must not be netted against liabilities (except possible derivatives treatment).
- Conditional mapping for separately identified net observations in same functional category/period/unit: IMF net acquisition of assets candidate = Debit − Credit = −RBI asset-side Net; IMF net incurrence of liabilities candidate = Credit − Debit = +RBI liability-side Net. Do not apply to a combined portfolio net or infer side solely from informal labels.
- RBI April 2026 guide confirms Table 42 quarterly USD million BPM6 functional classification and Credit/Debit/Net presentation.
- Official sign convention and methodology-level formula PASS. Exact Table 42 raw row mapping, P_F scope equivalence, quarterly DBIE raw export, two dated raw snapshots and vintage metadata remain NOT_ESTABLISHED / NOT_RETRIEVED. No numeric mapping, data merge or IMF vintage promotion.
- RBI parallel-source readiness NOT_READY. Sign-convention recovery bounded task 100%; IMF BOP 5/7=71.4%; October 2025 IMF PDF 25%; overall V11.3 NOT_CALCULABLE.
- Sources: RBI BOP Manual https://www.rbi.org.in/scripts/PublicationsView.aspx?id=13013 ; RBI Working Group report https://www.rbi.org.in/scripts/PublicationReportDetails.aspx?ID=596 ; RBI 2026 Guide https://www.rbi.org.in/scripts/PublicationsView.aspx?Id=24094 .
- No data mutation, synthetic values, paid source, credentials, PR merge or production change.

## 2026-11-15 — RBI Table 42 vs archived IMF India P_F single-quarter numerical reconciliation (2025-Q2)
- Compared official RBI Table 42 Apr–Jun 2025 with existing archived IMF CSV; no new IMF API pull or data-file modification.
- RBI 2025-Q2 portfolio investment in India: Credit 145201, Debit 142720, Net +2481 USD million. Per RBI sign convention this is liability-side net incurrence candidate +2481.
- RBI 2025-Q2 portfolio investment by India: Credit 1138, Debit 2011, Net −872 USD million. Per RBI sign convention this is asset-side net acquisition candidate +872. Combined Portfolio Investment Net +1608 was not mapped to either side.
- Archived IMF A_NFA_T/P_F/USD/Q/2025-Q2 = 872453921.9430683 raw; SCALE=6 => 872.4539219431 USD million. Difference from RBI +872 = 0.4539219431 USD million (within ±0.5 display rounding).
- Archived IMF L_NIL_T/P_F/USD/Q/2025-Q2 = 2480700911.919279 raw; SCALE=6 => 2480.7009119193 USD million. Difference from RBI +2481 = 0.2990880807 USD million (within ±0.5 display rounding).
- Single-quarter two-sided numerical comparison PASS_WITH_ROUNDING (2/2). This does not establish full-series equivalence or vintage/revision readiness. RBI raw quarterly DBIE export/schema NOT_RETRIEVED; multi-quarter replication NOT_DONE; IMF vintage gate remains NOT_READY. No data merge, mutation or gate promotion.
- Next: repeat on three additional non-adjacent quarters with exact matching RBI Table 42 bulletins; tolerance ±0.5 USD million only for whole-million displayed figures.
- Bounded 2025-Q2 check 100%; IMF BOP workstream 5/7=71.4%; October 2025 IMF PDF 25%; whole V11.3 NOT_CALCULABLE.
- Sources: RBI 25 Sep 2026 bulletin https://www.rbi.org.in/Scripts/BS_ViewBulletin.aspx?Id=24495 ; 23 Oct 2026 https://rbi.org.in/Scripts/BS_ViewBulletin.aspx?Id=24566 ; RBI BOP Manual https://www.rbi.org.in/scripts/PublicationsView.aspx?id=13013 ; archived CSV path data/research/imf_bop_india_portfolio_assets_liabilities_annual_quarterly_2015_2025.csv .
- No new data pull, synthetic values, paid source, credentials, data mutation, PR merge or production change.

## 2026-11-15 — Three additional RBI Table 42 vs archived IMF P_F quarterly reconciliations
- Extended prior 2025-Q2 two-sided comparison to 2024-Q3, 2024-Q4 and 2025-Q1 using RBI Table 42 dated pages (20 Feb, 23 Apr and 22 Jul 2026) and already archived IMF quarterly CSV. No new IMF API pull or data modification.
- Applied RBI Manual sign bridge: asset candidate = −(Portfolio Investment by India Net); liability candidate = Portfolio Investment in India Net. Fixed tolerance ±0.5 USD million (RBI whole-million displayed values).
- 2024-Q3: RBI assets −35 vs IMF A_NFA_T −34.990038547 (diff 0.009961453); liabilities +19815 vs IMF L_NIL_T +19815.071031982 (diff 0.071031982).
- 2024-Q4: RBI assets −63 vs IMF −62.610017414 (diff 0.389982586); liabilities −11435 vs IMF −11434.646504149 (diff 0.353495851).
- 2025-Q1: RBI assets −136 vs IMF −135.999310934 (diff 0.000689065); liabilities −5995 vs IMF −5994.630947245 (diff 0.369052755).
- All 6 comparisons PASS_WITH_ROUNDING. Including 2025-Q2 prior result, cumulative four quarters × two sides = 8/8 PASS_WITH_ROUNDING.
- Strong repeated numeric evidence of tested aggregate mapping, but not full 2015–2025 equivalence. RBI raw quarterly DBIE export/schema not retrieved; no RBI raw-file hashes; IMF vintage remains unverified. Do not merge sources or promote revision/vintage gate.
- Next: 2015–2025 quarterly spot-check matrix (one quarter/year) with exact RBI pages; stop on any mismatch and do not widen tolerance.
- Bounded extension 100%; cumulative 8/8; full-period mapping NOT_DONE; RBI export NOT_RETRIEVED; IMF revision/vintage NOT_READY; IMF BOP 5/7=71.4%; October 2025 PDF 25%; full V11.3 NOT_CALCULABLE.
- Sources: RBI 20 Feb 2026 https://www.rbi.org.in/Scripts/BS_ViewBulletin.aspx?Id=24025 ; 23 Apr 2026 https://www.rbi.org.in/scripts/BS_ViewBulletin.aspx?Id=24156 ; 22 Jul 2026 https://www.rbi.org.in/Scripts/BS_ViewBulletin.aspx?Id=24352 ; prior 25 Sep 2026 https://www.rbi.org.in/Scripts/BS_ViewBulletin.aspx?Id=24495 ; RBI Manual https://www.rbi.org.in/scripts/PublicationsView.aspx?id=13013 ; archived CSV data/research/imf_bop_india_portfolio_assets_liabilities_annual_quarterly_2015_2025.csv .
- No new IMF pull, raw RBI file, data/manifest/sidecar mutation, synthetic data, paid service, credentials, PR merge or production change.


## 2026-11-15 — RBI BPM6 historical cross-check extension (2016–2017)
- Official RBI bulletin: 10 Oct 2017, Table 40, BPM6 Standard Presentation, USD million; https://www.rbi.org.in/Scripts/BS_ViewBulletin.aspx?Id=17190
- Matched calendar Q2 periods: 2016-Q2 and 2017-Q2.
- Mapping: Portfolio Investment by India net -> negative IMF asset net acquisition; Portfolio Investment in India net -> positive IMF liability net incurrence.
- 2016-Q2: assets RBI -863 vs IMF -862.901610612507 (abs diff 0.098389387493); liabilities RBI +1241 vs IMF +1240.54 (abs diff 0.46). 2/2 PASS_WITH_ROUNDING.
- 2017-Q2: assets RBI -530 vs IMF -530.439269462386 (abs diff 0.439269462386); liabilities RBI +11921 vs IMF +11921.16 (abs diff 0.16). 2/2 PASS_WITH_ROUNDING.
- Historical extension: 4/4 PASS_WITH_ROUNDING. Combined with four previously verified quarters: six quarters, 12/12 side comparisons. No full-period equivalence claim.
- 2015–2025 annual spot-check matrix: 2/11 years covered (18.2%); 9/11 NOT_DONE.
- RBI raw quarterly DBIE export NOT_RETRIEVED; IMF vintage NOT_READY / NOT_VERIFIED.
- IMF BOP workstream unchanged at 5/7 (71.4%); overall project progress NOT_CALCULABLE.
- No source CSV/manifest mutation, no synthetic data, no source promotion, no production changes; all project invariants preserved.
- Report commit: ce05f8cce05395488b3ac3726edbe94a1550bac8; report blob: a2fdc68e5606587ab302938216631f5a02f80af5.


## 2026-11-15 — RBI BPM6 annual spot-check extension (2018–2023)
- Official RBI sources: 18 Sep 2020 Table 198 (2018-Q2), https://www.rbi.org.in/scripts/PublicationsView.aspx?id=19931 ; 12 Oct 2020 Table 40 (2019-Q2, 2020-Q2), https://www.rbi.org.in/Scripts/BS_ViewBulletin.aspx?Id=19879 ; 19 Oct 2023 Table 40 (2022-Q2, 2023-Q2), https://www.rbi.org.in/Scripts/BS_ViewBulletin.aspx?Id=22169 .
- 2018-Q2: RBI assets comparator -961, IMF -960.621114404864, diff 0.378885595136; liabilities -9106 vs -9105.960000000043, diff 0.039999999957.
- 2019-Q2: assets +314 vs +313.590331450881, diff 0.409668549119; liabilities +5156 vs +5156.281990468391, diff 0.281990468391.
- 2020-Q2: assets +456 vs +455.928583274424, diff 0.071416725576; liabilities +1098 vs +1097.593483845092, diff 0.406516154908.
- 2022-Q2: assets -29 vs -28.778465336278, diff 0.221534663722; liabilities -14659 vs -14658.870488236891, diff 0.129511763109.
- 2023-Q2: assets +358 vs +358.405859195828, diff 0.405859195828; liabilities +16089 vs +16089.227782268420, diff 0.227782268420.
- 10/10 PASS_WITH_ROUNDING; 2021-Q2 exact USD-million official row NOT_RETRIEVED.
- Cumulative checks: 11 quarters, 22/22 side comparisons PASS_WITH_ROUNDING. Q2 annual matrix 7/11 years (63.6%); 2015, 2021, 2024, 2025 not counted in this Q2 design. 2024–25 have separate quarterly checks.
- RBI raw quarterly DBIE export NOT_RETRIEVED; IMF vintage NOT_READY / NOT_VERIFIED; IMF BOP workstream remains 5/7 (71.4%); whole V11.3 project NOT_CALCULABLE.
- No CSV/manifest/sidecar changes, source promotion, synthetic data, or production changes.
- Report commit: 142acef931f9d40257b2055ef607f7e51c08707f; report blob: 69adbb76e456cd19871d290da35c033c9f88eb28.
