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


## 2026-11-15 — Alternate official NIC-2025 concordance source access
- Earlier MoSPI PDF URL under new.mospi.gov.in remained unavailable through public retrieval; an alternate official MoSPI URL is now text-accessible: https://www.mospi.gov.in/sites/default/files/main_menu/national_industrial_classification/NIC_2025Final_18112025.pdf
- Official PDF contents place the NIC-2025 / NIC-2008 4-digit concordance on printed pages 232–238 and define (p)=part, +=aggregation. Source text lines 15228–15741 include table rows and reveal a split continuation: NIC-2025 4772 expression ends with '+', followed by blank-code continuation 4799(p); parser must preserve both fragments and join deterministically.
- New checkpoint document: docs/NIC_2025_CONCORDANCE_SOURCE_ACCESS_CHECKPOINT_20261115.md. No raw PDF bytes were archived, no raw SHA-256 claimed, and no complete 463-row structured CSV or parser QA generated in this checkpoint.
- Bounded alternate official-source discovery/text-access task 100% complete. Raw-byte archival 0%; complete extraction 0%; QA 0%; IIP item-group/weight bridge UNKNOWN/BLOCKED. Do not infer 2-digit roll-up.
- Existing examples and no-auto-roll-up safety decision remain unchanged. No source CSV/manifest, prior PASS artifact, PR, production code, selector, ranking score, pressure fade, diagnostic or gate changed.


## 2026-11-15 — IIP classification applicability contradiction: NIC-2008 vs NIC-2025
- New official MoSPI FAQ page, freshly indexed and inspected: https://mospi.gov.in/faq . Under “FAQs on Index of Industrial Production (IIP)”, it states: current IIP base year is 2022-23=100 and “The current IIP series uses National Industrial Classification 2008 (NIC-2008), which is based on ISIC-Rev 4 by the United Nations.” It also describes NIC 2-digit IIP dissemination and the NIC 2/3/4-digit weighting chain.
- This directly conflicts with the earlier interpretation in the 2026-11-08 IIP transition crosswalk v2 and 2026-11-09 NIC safety audit follow-up, which inferred current 2022-23 IIP classification as NIC-2025 from the September 2026 release table labels.
- Additional official metadata cross-check: MoSPI NMDS IIP metadata still describes the 2011-12 IIP series as NIC-2008 and was last updated 30-05-2025; it is stale for the 2022-23 base and cannot resolve the current-series classification by itself. Official source: https://nmds.mospi.gov.in/ . MoSPI ASI 2022-23 results also use NIC-2008, but ASI classification alone does not prove IIP classification.
- The NIC-2025 PDF concordance is a general 4-digit classification crosswalk; it must not be presumed necessary or applicable to current IIP until the IIP-specific source is resolved.
- Decision: IIP classification for 2022-23 base is now CONFLICTED / UNKNOWN pending reconciliation of the MoSPI FAQ with the September 2026 IIP release/table metadata and current IIP technical documentation. Do not promote NIC-2025 mapping as current IIP mapping; do not delete prior evidence. Keep the full NIC concordance extraction on HOLD because its IIP applicability is unproven. General NIC classification research may continue separately if independently justified.
- Next highest-value task: obtain and compare the exact September 2026 PIB IIP release/table header/footnotes and latest MoSPI IIP methodology/technical note against the current FAQ statement; record release IDs, dates, exact classification labels and scope. Resolve the discrepancy before any NIC-2025-to-IIP crosswalk work.
- Progress: official FAQ contradiction discovery 100% complete; reconciliation 0% / NOT_DONE; NIC concordance extraction for IIP 0% / ON_HOLD; IIP mapping gate UNKNOWN / BLOCKED.
- No CSV/manifest, historical PASS artifact, production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, workflow or PR changed.


## 2026-11-15 — IIP NIC-2008 vs NIC-2025 conflict reconciliation
- New audit document: `docs/IIP_NIC_CLASSIFICATION_CONFLICT_RECONCILIATION_20261115.md`.
- Document commit: `daff08b15f2464d1005881c1a93238b743cea743`.
- Directly scoped official MoSPI FAQ PDF for “New Series with Base year 2022-23”, Q28, explicitly states NIC-2025 will be used for NIC 2-digit dissemination in the new IIP series: https://mospi.gov.in/uploads/latestReleases/latest_release_1779857844835_f8e09093-f2ef-4fb3-9890-6149d4162032_FAQ_for_new_IIP_series_with_base_year_2022-23.pdf
- MoSPI TAC-IIP press note dated 25 May 2026 says the updated 2022-23 IIP series is aligned with NIC-2025 and specifically plans manufacturing 2-digit NIC-2025 indices: https://www.mospi.gov.in/uploads/latestReleases/latest_release_1779706122249_3b3add9b-577c-4a1e-a9be-0e2b1c3d6e2c_Press_Note_on_release_of_TAC-IIP_Report_on_base_revision_of_IIP_with_base_2022-23__25052026.pdf
- PIB September-2026 release PRID 2329475 (28 Oct 2026) operationally labels Statement II-A “Manufacturing at NIC 2 digit”, its classification column “NIC 2025”, and paragraph 5 says 2-digit NIC-2025 detail is provided: https://www.pib.gov.in/PressReleasePage.aspx?PRID=2329475&lang=2&reg=48
- Conflicting generic MoSPI HTML FAQ page https://mospi.gov.in/faq says current base 2022-23=100 but NIC-2008. It has no visible version/date context proving it supersedes the directly scoped new-series FAQ PDF. Preserve as official-page documentation inconsistency; do not suppress it or treat it as stronger than the explicit new-series FAQ, TAC-IIP statement and operational release.
- Narrow decision: legacy 2011-12 series remains NIC-2008; current 2022-23 series NIC 2-digit manufacturing dissemination is NIC-2025 — evidence-backed PASS. HTML FAQ inconsistency remains SOURCE_CONFLICT / DOCUMENTATION_DEFECT pending official correction/clarification.
- This does NOT establish an IIP-specific 463-item-group/weight bridge. The general NIC-2025/NIC-2008 4-digit concordance must not be rolled up by prefix or assumed to represent IIP item groups. Full concordance extraction/QA and item-group/weight mapping remain incomplete/UNKNOWN as applicable.
- Progress: source comparison 100% COMPLETE; current-series NIC decision 100% PASS; HTML FAQ discrepancy recording 100% COMPLETE (official correction NOT_DONE); raw concordance binary archival/SHA-256 0%; full concordance extraction/QA 0%; IIP-specific 463-item-group/weight bridge UNKNOWN/BLOCKED.
- No raw PDF bytes were downloaded or hashed in this reconciliation; no SHA-256 claimed. No synthetic data, paid API, spend, external contact, workflow rerun, PR, production change, selector/ranking/pressure-fade/CORE-672 change, or prior artifact alteration.


## 2026-11-15 — NIC-2025 concordance source re-open and extraction readiness checkpoint
- Re-opened the exact official MoSPI NIC-2025 PDF through the alternate official URL already preserved in prior audit: https://www.mospi.gov.in/uploads/publications_reports/publications_reports1763457214315_c3e5d4f3-8e25-4775-85e3-ad42d571652f_NIC_2025_Final.pdf
- Browser document retrieval verified a 322-page official PDF. Its contents page places “Concordance between 4-digit industry classes of NIC-2025 and NIC-2008” on printed pages 232–238; source text explicitly defines (p)=part and +=aggregation.
- Full concordance table text is now accessible in the web document extraction, source lines 10330–10872 (printed pages 232–238). Examples reconfirmed directly include 0113 <- 0113+0128(p), 0330 <- 0311(p)+0312(p)+0321(p)+0322(p), 1512 <- 1512+2220(p), 2611/2619 <- 2610(p), 3511/3512/3513 <- 3510(p), and 4772 continuation: first fragment 4772(p)+4789(p)+4791(p)+ followed by blank-code continuation 4799(p). This corroborates the previously documented split-row hazard.
- Download attempts for the raw PDF binary via the available container downloader failed for both official URLs. Therefore no local raw PDF file, byte length, or SHA-256 was produced. Do not claim archival complete.
- Status update: official PDF browser access 100% COMPLETE; source-table line-range discovery 100% COMPLETE; raw PDF byte archival/SHA-256 0% NOT_DONE; complete structured 463-row transcription 0% NOT_DONE; parser QA/multiplicity audit 0% NOT_STARTED; IIP item-group/weight bridge UNKNOWN/BLOCKED.
- No partial row set promoted as complete; no CSV/manifest created; no fabricated rows, prefix roll-up, workflow rerun, PR/merge, production change, or protected invariant change. Prior source artifacts and PASS evidence remain unchanged.


## 2026-11-15 — NIC concordance exact source-line map verified
- New research document: `docs/NIC_2025_CONCORDANCE_SOURCE_LINE_MAP_20261115.md`.
- Document commit: `ac77df2cb05c1e96a1de6e15bcda694b5fe11e79`.
- Canonical official MoSPI PDF opened successfully via: https://www.mospi.gov.in/uploads/publications_reports/publications_reports1763457214315_c3e5d4f3-8e25-4775-85e3-ad42d571652f_NIC_2025_Final.pdf . It is a 322-page PDF; contents place the concordance on printed pages 232–238.
- Exact browser-extracted table range: lines 10330–10872. Page map: p232 10330–10407; p233 10408–10493; p234 10494–10579; p235 10580–10671; p236 10672–10757; p237 10758–10843; p238 10844–10872.
- Continuation hazards explicitly verified: 0330 across lines 10378–10379; 4340 across 10571–10573; 4772 across 10626–10630 with blank-code continuation 4799(p). Last concordance row 9900 is line 10872; following text is explanatory notes.
- Canonical URL raw binary download attempted in this checkpoint and failed. No local PDF bytes, byte length or SHA-256 claimed.
- Progress: official browser PDF access 100%; exact source line/page map 100%; continuation boundary identification 100%; raw binary archival/SHA-256 0%; full structured extraction 0%; parser QA/multiplicity audit 0%; IIP item-group/weight bridge UNKNOWN/BLOCKED.
- This is source-line boundary work only; no CSV/JSON extraction has been generated or accepted. No duplicate source discovery claimed, no synthetic rows, paid API, spending, external contact, workflow rerun, PR/merge, production code change or protected invariant change.


## 2026-11-15 — NIC concordance parser acceptance suite frozen from official source
- New document: `docs/NIC_2025_CONCORDANCE_PARSER_ACCEPTANCE_TESTS_20261115.md`.
- Initial creation commit: `ad57c4d84602889eb31149becf9ddd71adbbb116`; page-boundary test correction commit: `ae1118ff639fd020094b2e9a49a3d4b9ca43a324`.
- Re-opened the exact official MoSPI PDF directly; browser extraction reports 322 pages and 12,845 source lines. Contents identify the concordance at printed pages 232–238; table begins at source line 10330 and final 9900 row is at 10872. The line map's 10330–10872 range is corroborated.
- Direct source-derived hard cases frozen: 0330 wrap (10378–10379); 4340 wrap (10571–10573); 4772 multi-line + repeated-header + blank-key 4799(p) continuation (10626–10630); 4790 long 23-component expression (10637–10644); 9540 nine-component wrap (10855–10857); and page-boundary keys 4642/4649 retained as separate rows (10579 and 10583).
- Important correction during test review: 4642 and 4649 are two separate NIC-2025 keys with the same expression, not one continuation. Test T06 was corrected before ledger acceptance; correction commit recorded above.
- Parser test specification: 100% COMPLETE. Parser implementation: 0% NOT_DONE. Automated test execution: 0% NOT_DONE. Full 463-row extraction: 0% NOT_DONE. Independent row-count and forward/reverse QA: 0% NOT_DONE. Raw PDF binary/SHA-256: 0% NOT_DONE; direct download still fails, no hash claimed. IIP-specific item-group/weight bridge UNKNOWN/BLOCKED.
- No partial extraction, CSV or manifest accepted. No synthetic rows, workflow rerun, PR/merge, production integration, paid API, spending, external contact, or protected V11.3 invariant changes.


## 2026-11-15 — NIC concordance parser implementation and unit-test checkpoint
- Official source reopened directly: MoSPI NIC-2025 PDF, 322 pages, concordance table printed pages 232–238; exact lines 10330–10872. Source shows wrapped expressions 0330 (10378–10379), 4340 (10571–10573), and 4772 (10626–10630), plus 4790 long expression (10637–10644), and final 9900 row (10872).
- Implemented `scripts/research/nic_concordance_parser.py` in commit `f607d9096cf122d35a04b228847f46d2986ec221`.
- Added `tests/research/test_nic_concordance_parser.py` in commit `e54e5aae2c4ded679bdef0310aab4af7abc9493b`.
- Test-driven defect found: parser originally rejected a continuation fragment that itself ended with '+', as occurs in the official 4340 expression. Fixed continuation regex in commit `0a16ebb97bbae0f384c42a291a5c5e590bfe881c`. This is a real test-discovered correction, not a source-data repair.
- Local unit-test execution after fix: 8 tests PASS, 0 FAIL. Covered simple mapping, partial+aggregation, 0330 wrap, 4340 multi-line wrap, 4772 blank-key continuation across repeated headers, distinct NIC-2025 keys sharing same expression (4642/4649), 23-component 4790 expression, unresolved trailing-plus fail-closed, and duplicate-key audit.
- Parser accepts only source-text input with retained `L<line>@P<pdf-page>:` provenance markers; it emits structured JSON/CSV plus audit metadata. It does not fetch/OCR PDF and does not claim full-table completeness based on sample tests.
- Status: parser implementation 100% for bounded parser module; local unit tests 100% PASS; full source text ingestion 0%; full 463-row extraction 0%; full-table row coverage and multiplicity QA 0%; raw PDF binary/SHA-256 0% (download failed); IIP-specific item-group/weight bridge UNKNOWN/BLOCKED.
- GitHub Actions CI was not dispatched or run; no CI PASS is claimed. No CSV/JSON production dataset or raw-PDF manifest created. No synthetic rows, workflow rerun, PR/merge, production integration, paid API, spending, external contact, or protected V11.3 invariant changes.


## 2026-11-15 — Parser source-layout hardening before full ingestion
- Reopened canonical MoSPI PDF: 322 pages; concordance at printed pages 232–238; source lines 10330–10872. Actual extraction includes page-range provenance tokens such as L10407@P256-257, L10493@P257-258, L10579@P258-259, L10671@P259-260, and L10757@P260-261; 4772 continuation is split by repeated two-column headers; explanatory notes begin after the final concordance row.
- Defect found: original marker regex accepted only a single PDF page number and would discard line/page provenance for page-range markers. Parser updated to accept page ranges and retain both page endpoints; printed-page metadata derives from PDF page number minus 24.
- Added explicit stop at EXPLANATORY NOTES so following explanatory material cannot be misread as concordance rows.
- Added regression test for page-range provenance and table termination. Added repository-relative sys.path setup to test module so parser import resolves under standard test discovery.
- Relevant commits: parser hardening f5a1b7d2e9c6666380c797b1b7c1f28d355f8f2e; regression test eebfe72a7f0841f324b46a977c677b89274cae63; parser marker syntax correction 205f2ee2d5661801f5be953d7ecd0c2b9ba87418; test import correction feadccbada336612840be8469a45c42d89e2a177.
- First marker-regex text replacement did not match and was caught on re-fetch; exact line replacement fixed it. Preserve both commits as audit history; final current file was re-fetched and its marker regex shows optional end-page capture.
- Validation status: source layout reviewed 100%; page-range parser correction committed 100%; regression test authored 100%; actual test execution in this turn NOT_RUN; parser full-source ingestion 0%; 463-row extraction 0%; independent coverage/multiplicity QA 0%; raw PDF binary/SHA-256 0%; IIP-specific item-group/weight bridge UNKNOWN/BLOCKED.
- No full dataset, CSV/JSON, or manifest claimed. No CI PASS claim. No workflow rerun, PR/merge, production integration, synthetic rows, paid API, spending, external contact, or protected V11.3 invariant change.


## 2026-11-15 — NIC parser fail-closed acceptance strengthened
- Re-opened current parser and test files from the default branch before modifying; no full-source extraction had been performed, and prior 8-test result applies only to the earlier bounded test suite, not the current page-range changes.
- Identified a material acceptance weakness: the parser audit previously could return PASS from row count + unique keys alone, even when source line/page provenance was missing or table boundaries were not demonstrated.
- Strengthened audit acceptance to require complete row provenance, strictly increasing non-overlapping source-line order, all source lines within the frozen table range 10330–10872, and final concordance key 9900, in addition to 463 row count, uniqueness and valid keys. Commit 9c43d4493793b52ddaebf7bd8dae87a6cb5dc80b.
- Added a regression test proving that a count-matching row without source provenance remains UNKNOWN_BLOCKED, not PASS. Commit 6983a5c2a7528f79c09d71a1ebe5260254588400.
- Current parser and test files were fetched after updates; automated execution was not performed in this turn. No test PASS claim for the new changes. Full PDF source ingestion and 463-row extraction remain 0%; raw binary/SHA-256 0%; full independent QA 0%; IIP item-group/weight bridge UNKNOWN/BLOCKED.
- No full dataset, synthetic data, workflow rerun, PR/merge, production integration, paid API, spending, external contact, or protected V11.3 invariant changes.

## 2026-11-15 — NIC concordance parser dedicated CI and regression validation
- Added .github/workflows/nic_concordance_parser_tests.yml in commit e9aabddc6885f87cd88628a8cbff06122e2f6c79. It runs only the parser test module on relevant parser/test/workflow path changes, Python 3.12, with a 5-minute job timeout and read-only contents permission.
- First dedicated run #1 / ID 43686193160 failed due to a test-fixture defect, not a parser failure: the “missing provenance” regression used the helper that always adds an L...@P... source marker. Actual suite result was 9 passed, 1 failed. Failure log confirmed provenance_complete was True because the fixture accidentally supplied provenance.
- Corrected only the regression fixture to pass an intentionally unmarked row while retaining the marked table heading. Test-only correction commit: 484fb8027e6c12a5d6e3ac3c529f9a35aac30384.
- Dedicated parser run ID 43686220031, run number 2, on corrected commit 484fb8027e6c12a5d6e3ac3c529f9a35aac30384: SUCCESS. Job parser-unit-tests completed SUCCESS; all 10 tests passed. Runtime approximately 10 seconds (06:36:35Z–06:36:45Z). Run URL: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/43686220031
- Workflow isolation caveat: existing .github/workflows/nse_collector.yml has unrestricted push: branches: [main]. Parser-only commits therefore also trigger the unrelated full NSE collector workflow (including run ID 43686219985 for the test-fixture correction commit, plus earlier adjacent runs). This is an existing repository trigger interaction, not part of dedicated parser validation. Do not claim those NSE runs passed or were required for parser validation. No production selector, rank, pressure fade or CORE-672 changes were made.
- Status: dedicated CI workflow 100% COMPLETE; current 10-test regression suite 100% PASS; test-fixture correction 100% COMPLETE; full official source-text ingestion 0%; full 463-row extraction 0%; independent source coverage/multiplicity QA 0%; raw PDF binary archive/SHA-256 0%; IIP item-group/weight bridge UNKNOWN/BLOCKED.
- This PASS is bounded parser regression validation only. It does not validate full-table extraction, source completeness, row count, IIP mapping, or any production trading signal. No synthetic data, paid API, spend, external contact, PR merge, production integration or protected invariant change.

## 2026-11-15 — Isolated NIC research-only pushes from full NSE collector workflow
- Prior ledger checkpoint commit 173a166cd7ad224d2887e1feed650d3e2b32d830 itself triggered full collector run 43686440086 because nse_collector.yml had unrestricted push-to-main trigger. At inspection it was IN_PROGRESS; no completion/pass claim made.
- Updated .github/workflows/nse_collector.yml push trigger with paths-ignore for docs/**, NIC parser source, NIC parser tests, NIC parser CI workflow, and the collector workflow file itself. This preserves explicit workflow_dispatch and weekday schedule triggers while preventing research-only/documentation and workflow-maintenance commits from launching full 60-minute collection/backtest jobs.
- Trigger-isolation commits: f159600fd63613af3e98f06c4b4beee0a95337dc (initial scoped ignore) and 24cf0b00114d582db1ca8e148abeb821fae747b3 (ignore self-workflow update path). These are CI scheduling controls only; no collector code, production selector, ranking, pressure fade or CORE-672 logic changed.
- Validation scope: config edits committed; GitHub push-event non-trigger behaviour is not yet directly proven by a subsequent matching event. Existing run 43686440086 is a known pre-fix run and must not be treated as evidence against the new filter. Status: parser regression suite 10/10 PASS (run 43686220031); trigger isolation configuration 100% committed, runtime behaviour awaiting next relevant event; full 463-row extraction 0%; independent source QA 0%; raw PDF binary/SHA-256 0%; IIP bridge UNKNOWN/BLOCKED.
- Note: a push changing nse_collector.yml may still have started a full collector run before the self-path ignore commit took effect. Do not cancel or rerun without supported action and explicit need; do not claim run completion unless separately verified.

## 2026-11-15 — Fail-closed numeric-token parser hardening
- Re-inspected the canonical MoSPI NIC-2025 PDF concordance directly: printed pages 232–238, PDF pages 256–262, extracted source lines 10330–10872; final key 9900. Official source identifies 463 NIC-2025 classes, but that count alone is not concordance extraction evidence. Raw PDF binary download retry failed; no local PDF bytes/hash claimed.
- Parser defect found: standalone 1–3 digit numeric tokens were silently ignored even when they did not match the known printed-page metadata. Hardened parser to ignore such a token only when it exactly equals PDF page minus 24; all other unparsed numeric tokens now fail closed.
- Added two regression tests: reject unrecognized 3-digit numeric token; accept a standalone printed page number only when consistent with the documented P256→232 offset.
- Parser commit: a41efc94f94306b5a37091b1b49ec3736332129a. Test commit: 0b05a9466ce77a66d1419bd5b2369d6a465c202f.
- Dedicated CI run #4 ID 43686662809 completed SUCCESS; job parser-unit-tests SUCCESS. This validates the regression suite, not full 463-row source extraction. A preceding superseded run 43686660464 was cancelled after the subsequent test commit; not a failure of the parser suite.
- Current status: parser hardening + regression CI 100% PASS; official source page/line boundary revalidated 100%; full structured 463-row extraction 0%; independent source-row reconciliation 0%; raw PDF archival/SHA-256 0% (download unavailable); IIP item-group/weight bridge UNKNOWN/BLOCKED. No synthetic data, paid service, production selector/ranking/pressure-fade/CORE-672 change, PR or merge.

## 2026-11-15 — Corrected NIC concordance row-level PDF page provenance
- Directly re-opened the official MoSPI NIC-2025 PDF and inspected the full concordance line range 10330–10872. Boundary evidence: L10407@P256-257 contains row 1079 plus printed page marker 233; L10872@P262-266 contains row 9900 plus printed page marker 239, while explanatory notes begin at P266. Therefore the marker's end page is extraction-span metadata and must not automatically be assigned to the row.
- Defect fixed: parser previously copied both ends of every page-range marker into a row's pdf_pages, which could incorrectly attribute row 9900 to PDF page 266 / printed page 242. Parser now assigns a row only to the marker's start page; actual continuation lines contribute their own page provenance.
- Parser commit: bdfe00904bacd5262c1adeb283941660f48e3f5e. Regression test commit: 191dc4f306b087325cb8644bc2c871f61db0a5b1.
- First CI attempt run 43686746506 failed because the concurrent test-file update was not included in that commit's checkout; log identified the stale assertion expecting [256,257]. The subsequent test commit run 43686749415 was initially cancelled by overlapping push updates, then its cancelled job was re-run; final run completed SUCCESS, job SUCCESS. Run URL: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/43686749415.
- Current validated state: parser regression suite 13 tests PASS (12 previous + page-span provenance test); parser provenance fix PASS. Source table boundary reviewed. Full 463-row structured extraction remains 0%; independent source-row reconciliation 0%; raw PDF binary archival/SHA-256 0% (binary download remains unavailable); IIP item-group/weight bridge UNKNOWN/BLOCKED. No production selector, ranking score, pressure fade or 672 diagnostic changes.

## 2026-11-15 — Official NIC source acquisition path established
- New official MoSPI source endpoint discovered: https://www.mospi.gov.in/sites/default/files/main_menu/national_industrial_classification/NIC_2025Final_18112025.pdf. Browser-extracted source exposes concordance as two-cell HTML table rows at source lines 15228–15742, with final row 9900 at line 15740 and explanatory notes beginning line 15745. This is a distinct extraction representation from the earlier line-marker mapping 10330–10872; do not mix their line IDs.
- Source citations reviewed: browser-opened official PDF lines 15228–15303, 15304–15475, 15476–15629, and 15630–15745. The table includes structural repeated headers and the blank-key 4799(p) continuation after 4772; parser must retain that row-join rule.
- Added `scripts/research/acquire_nic_concordance_source.py` (commit 182993485fd5c8471433f6ddbbf88237802a00e3) to download the official PDF, validate redirect host/content type/PDF signature/minimum bytes, calculate SHA-256, extract PDF pages 256–262 with pdftotext, and emit page-marked text plus JSON manifest. No source rows are synthesized.
- Added manual workflow `.github/workflows/nic_concordance_source_acquisition.yml` (commit 573524a3c3c799b1b16870784540741c13933b3c) with 5-minute job timeout, poppler-utils install, source acquisition, parser/audit, and 90-day artifact retention. Workflow has NOT been dispatched/executed in this checkpoint; source PDF download and 463-row extraction remain unverified.
- Parser source-line audit bounds made explicit and configurable for authentic local extraction line numbering (commit 494abd62ece9bcdd5f0b86df1fb7a91718c48515); acquisition output now numbers its own extracted lines from 1, not a fabricated reuse of earlier browser line IDs (commit 747b8ca86912763554433df61ee26114d680904a). Workflow runs strict parser on extracted text (commit 05aee88697a20f28cc05635d9ab592819dd9f9b9).
- Dedicated parser CI run 43686935018 completed SUCCESS; 13 tests passed (verified from job log). URL: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/43686935018.
- Added the acquisition script/workflow to `nse_collector.yml` paths-ignore to prevent research-only changes launching the full NSE collector; commit 9983e65341f41955c04cd861c6ae6a20d906f8ea. This is trigger configuration only.
- Current status: alternate official source discovery 100%; acquisition code/workflow committed 100%; parser regression CI 13/13 PASS; actual PDF download in GitHub Actions NOT_RUN; raw PDF archive and SHA-256 NOT_DONE; full 463-row extraction NOT_DONE; independent source reconciliation NOT_DONE; IIP item-group/weight bridge UNKNOWN/BLOCKED. No production selector/ranking/pressure-fade/CORE-672 changes, no paid API, no spend, no PR or merge.

## 2026-11-15 — Corrected official source URL before acquisition execution
- A fresh HTTP/web verification found that the initially configured alternative URL `https://www.mospi.gov.in/sites/default/files/main_menu/national_industrial_classification/NIC_2025Final_18112025.pdf` returns 404. This would have made the newly committed acquisition workflow fail before download. It was not treated as a valid source.
- Replaced it with the previously verified canonical official MoSPI URL: `https://www.mospi.gov.in/uploads/publications_reports/publications_reports1763457214315_c3e5d4f3-8e25-4775-85e3-ad42d571652f_NIC_2025_Final.pdf`. Browser fetch succeeds and identifies a 322-page PDF. Commit: 8c0895cf0d7aa166955b3e549ff1a45da5f68126.
- Official PDF confirms concordance section printed pages 232–238 (PDF pages 256–262) and states NIC-2025 has 463 classes. This is source metadata only, not proof that 463 concordance rows have been extracted.
- Acquisition workflow has still NOT been dispatched; actual binary download, SHA-256, pdftotext output, parser result, and artifact remain NOT_DONE. No claims of source acquisition or 463-row acceptance.
- Parser unit tests last verified 13/13 PASS in run 43686935018. Production selector, ranking score, pressure fade and CORE-672 unchanged. No paid service or spend.

## 2026-11-15 — NIC source-acquisition preflight regression suite
- Added `tests/research/test_nic_concordance_source_acquisition.py` to validate PDF signature, content type, redirect-host allowlist, minimum payload size, SHA-256 correctness, seven-page extraction count, page markers, and rejection of incomplete extraction. Test commit `29dd3789bd8fdcf66ca8c02fb56e743ac6f2efee`.
- Integrated both parser and acquisition tests into the dedicated bounded CI workflow; expanded `nse_collector.yml` paths-ignore for the new test module. CI commits: `5902c20c1e87d757f4065c795e04b30b1b1848a3`, `ff81b9e96e408df49f82248dd5c3ea8b19f4e410`, `eac75fc16e27ef260bb69740150f2725d6113841`, `f248591d2372ec54ff6956a2067e9320df454012`.
- Initial combined suite surfaced a real test-fixture defect: test used literal backslash-f rather than PDF form-feed page separators. Failed run `43687145727` ran 20 tests; 19 passed, one errored. Corrected fixture in commit `4b2db8bf1c0720c1e272575c606c2eb3b30a9f54`.
- Final dedicated CI run `43687201440` completed SUCCESS; log confirms 20 tests ran, all 20 PASS. Runtime under 10 seconds. URL: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/43687201440.
- Note: run `43687157156` was cancelled by the workflow's concurrency policy while a newer commit superseded it; not counted as a code failure. The 19/20 run is retained as a documented fixture defect and correction, not hidden.
- Status: acquisition script unit-test coverage 100% for the listed fail-closed cases; parser + acquisition regression suite 20/20 PASS. These are mocked/unit tests only. Actual live PDF retrieval, raw PDF SHA-256, pdftotext against the official binary, 463-row extraction and independent source reconciliation remain NOT_DONE. Manual acquisition workflow still requires dispatch.
- The full NSE collector was unintentionally triggered by the first acquisition-test commit before its new path had been added to paths-ignore (run `43687120198`, at last check IN_PROGRESS); subsequent trigger config now includes that test path. Do not claim that collector run passed or that new path-ignore behavior has been runtime-proven.
- No changes to Production Selector, RANKING_SCORE, +1 PRESSURE_FADE or 672 diagnostics; no paid API or spend.

## 2026-11-15 — Post-CI verification and duplicate collector-run incident
- Verified latest NIC combined regression run `43687201440`: completed SUCCESS, logs explicitly show 20 tests ran, all OK; this includes 13 parser tests and 7 acquisition preflight tests. No need to rerun these tests unless code changes.
- Confirmed the dedicated acquisition workflow `.github/workflows/nic_concordance_source_acquisition.yml` has not yet been dispatched; no live acquisition run or artifact exists in the latest run listing.
- Audited unintended full NSE collector runs triggered before all research-only paths were excluded: `43687120198`, `43686940208`, `43686937403`, `43686920391`, `43686917332`. At latest inspection, these were still IN_PROGRESS. Four older runs had completed download, Security Master, normalized dataset build and strict QA successfully, but were all in the 100-session walk-forward backtest step; the newest run was still at the 200-session acquisition step. No overall run conclusion may be inferred.
- Checked available GitHub action tools: no workflow cancellation or dispatch operation is exposed. Do not claim these runs were cancelled. `nse_collector.yml` paths-ignore now includes the acquisition script, acquisition workflow, parser tests and acquisition tests; the post-fix test commits did not create further collector runs in the latest run listing, but path filtering is not yet treated as formally proven.
- Current decision: no additional parser changes or repeated tests. Await manual dispatch of the one-off NIC acquisition workflow, then validate actual PDF bytes, SHA-256, 7-page text, parser output, row count/uniqueness/provenance and artifact. All actual acquisition and 463-row acceptance gates remain NOT_DONE / UNKNOWN.


## 2026-11-15 — Follow-up status audit (no duplicate test execution)
- Re-queried the latest 15 GitHub Actions runs. Dedicated NIC combined regression run 43687201440 remains completed SUCCESS; no rerun was initiated.
- Re-checked the five previously identified unintended NSE collector runs: 43687120198, 43686940208, 43686937403, 43686920391, and 43686917332. All five are still IN_PROGRESS. For each, the active step is the 100-session leakage-safe V11.3 walk-forward behavioural backtest; preceding 200-session acquisition, Security Master, normalized dataset build and strict QA steps are marked completed SUCCESS. All later steps remain pending. No run is represented as a final PASS, and no cancellation was attempted.
- The NIC source-acquisition workflow remains workflow_dispatch-only and has not been run. The next blocking action is a manual dispatch at https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/workflows/nic_concordance_source_acquisition.yml. After dispatch, validate the actual official PDF payload, SHA-256 manifest, seven-page extraction, strict parser output, 463 unique keys and provenance, and uploaded artifact.
- No source acquisition or concordance extraction completion is claimed. Regression coverage remains 20/20 PASS (mocked/preflight tests only). Actual PDF binary/SHA-256, authentic text extraction, 463-row extraction and independent reconciliation remain NOT_DONE.
- No production selector, RANKING_SCORE, +1 PRESSURE_FADE or 672 diagnostic changes; no paid API/service, spend, PR merge or external contact.


## 2026-11-15 — First live NIC official-source acquisition succeeded; parser exposed actual PDF layout mismatch
- Manually dispatched NIC Concordance Source Acquisition on main (commit e92b009863990c1673138ddb932d4e5a874b1146). Three runs were created: 43687797343, 43688167016, 43688472880; all ended FAILURE at the strict parser step. Do not treat them as successful end-to-end runs.
- In all three runs, the official source acquisition step completed SUCCESS. Latest run 43688472880 logged: canonical MoSPI PDF URL, application/pdf, 5,143,225 bytes, SHA-256 66bc2babc1e915b670b21a66d556c2933b97f72d9590a50cc535c5e9239fe709, retrieval time 2026-11-15T07:07:29.017397+00:00, PDF pages 256–262, 7 pages extracted, 296 text lines. This is first verified live source binary retrieval + SHA-256 + seven-page extraction; prior status 0% is superseded for these subtasks.
- Parser failure is reproducible across the three runs at source line 8: 0111                  0111                       0311               0311(p). Current parser expects one two-column row per extracted line; actual pdftotext -layout output places two row pairs side-by-side on one physical line. This is an authentic source-layout mismatch, not a download/network failure. Do not silently drop the second pair or weaken fail-closed checks.
- Parser step failed; upload step was skipped. Therefore no GitHub artifact was retained from these runs, despite source acquisition succeeding in the job workspace. Raw PDF/text/manifest are not yet retrievable as persisted artifacts.
- Current subtask status: official PDF live acquisition 100%; SHA-256 calculation/manifest generation 100% (job log confirms hash; artifact persistence pending); seven-page extraction 100%; correct two-column layout parser adaptation 0%; strict 463-row parse/unique/provenance acceptance NOT_DONE; independent reconciliation NOT_DONE; artifact upload NOT_DONE.
- Next safe action: inspect the actual extracted text from the same source run by ensuring evidence upload executes even when parser fails (workflow upload step if: always()), then implement and test a parser that correctly handles both side-by-side row pairs and wrapped continuation lines while preserving exact source line/page provenance. Do not rerun acquisition repeatedly until the parser/layout issue is corrected.
- No Production Selector, RANKING_SCORE, +1 PRESSURE_FADE or 672 diagnostic changes; no paid APIs/services, spend, PR merge or external contact.


## 2026-11-15 — NIC two-column parser repair iteration and CI findings
- Implemented an initial fail-closed parser branch for `pdftotext -layout` side-by-side row pairs (commit dfbc99765fbbe72c72e2bc62f618a29837af5629), added regression tests for paired/unpaired columns (commit fdca49482a68911c58b09626db3e1741d0c3b387), and configured source evidence upload with `if: always()` (workflow commit 646015c587509779510acf18ba612aa402d15d52) so a parser failure does not suppress PDF/text/manifest artifacts.
- First new parser CI run 43688733051 exposed an implementation defect: the regex delimiter was over-escaped and did not split whitespace; both new tests failed, while the other 20 tests passed (22 total). This was a genuine code defect, not hidden. Follow-up fix commits: 256715041a49ab8d7e180ec75d759b1f72b6aa1b (odd three-column fail-closed handling) and 87666f35dd322dd60094126677e9f8cb4fcbdc17 (correct regex escaping). A new bounded CI run 43688778740 was queued at last check; result not yet known.
- Do not dispatch the live source acquisition workflow again until parser CI is green. The source acquisition already succeeded in prior run 43688472880; avoid repeating network acquisition while parser validation is pending.
- Current state: official PDF acquisition 100%; SHA-256 calculation 100% (hash logged); seven-page text extraction 100%; artifact persistence still NOT_DONE pending rerun with upload-if-always; two-column parser repair implemented but CI validation PENDING; 463-row parse and independent reconciliation NOT_DONE.
- No production selector, ranking score, pressure fade or 672 diagnostic changes; no paid service/spend, PR merge or external contact.

- Follow-up bounded CI run 43688778740 completed SUCCESS after the regex correction; job `parser-unit-tests` is SUCCESS. The workflow executes the parser + acquisition preflight suite; detailed test-count confirmation should be taken from its job log. This validates the current unit-test state only, not the live full-table parser against the official PDF. Live source acquisition must be run once more only after this fix, to persist the source evidence artifact and test all 463 rows.


## 2026-11-15 — Post-repair verification checkpoint
- Rechecked latest Actions history: no new NIC Concordance Source Acquisition run has been dispatched after parser repair. Latest source acquisition runs remain 43688472880 / 43688167016 / 43687797343, all FAILURE at parser step, before the evidence-upload-if-always workflow change was committed.
- Confirmed latest parser CI run 43688778740 SUCCESS; job log explicitly reports 22 tests in 0.014s, OK. Both new tests passed: side-by-side row pair parsing and fail-closed unpaired-column rejection.
- Queried artifacts for failed source run 43688472880: zero artifacts. This is expected because that run predates the upload `if: always()` fix. Do not infer evidence persisted from its successful acquisition logs.
- Current workflow has the always-upload change in commit 646015c587509779510acf18ba612aa402d15d52. Parser implementation current head includes regex correction commit 87666f35dd322dd60094126677e9f8cb4fcbdc17. Parser CI is green; the actual 463-row source parse is still unverified.
- Next action is one single manual dispatch of NIC Concordance Source Acquisition on main. After that, inspect the resulting artifact first (PDF, source_manifest.json, 7-page text extract); then validate parser output and audit. Do not run additional parser CI or repeat source acquisition unless code changes or evidence indicates a new issue.
- Status: live PDF acquisition 100% from prior run; SHA-256 computation 100% but retained artifact pending; 7-page extraction 100%; parser regression 22/22 PASS; durable source evidence artifact NOT_DONE; real 463-row extraction/audit NOT_DONE; independent reconciliation NOT_DONE.


## 2026-11-15 — Latest continuation check: manual dispatch still outstanding
- Queried the latest 20 repository Actions runs. No new NIC Concordance Source Acquisition run exists after the parser repair and artifact-upload `if: always()` commit. Latest parser test run remains 43688778740 SUCCESS (22/22); no duplicate tests were run.
- Re-opened `.github/workflows/nic_concordance_source_acquisition.yml` at current main: workflow_dispatch trigger confirmed; strict parser step precedes artifact upload, and upload has `if: always()`, artifact path `nic_concordance_source/`, retention 90 days, job timeout 5 minutes.
- There is no available GitHub dispatch action in the connected tool set; dispatch cannot be initiated from this session. Do not claim a run was started. Next required step remains the user's single manual `Run workflow` action on main. After the run, inspect artifact existence and contents before judging 463-row acceptance.
- No code changed in this checkpoint; no tests rerun, no duplicate source fetch, no production selector/ranking/pressure-fade/672 changes, and no spend.


## 2026-11-15 — Reconciliation of five previously pending NSE collector runs
- Rechecked the five collector runs previously listed as IN_PROGRESS: 43687120198, 43686940208, 43686937403, 43686920391, 43686917332. All five are now workflow-level completed SUCCESS and their single collect-and-test jobs are completed SUCCESS. This closes the earlier pending-status item; it does not establish full research/Hard-Gate acceptance.
- Each run produced a non-expired artifact (about 61.6 MB): run 43687120198 artifact 14151241008, ZIP SHA-256 5e4596f93454cca24d4a276e26bad99e6bc01adb574510506eae26a67c74a238; run 43686940208 artifact 14150863870, ZIP SHA-256 5a3ce936c8b288d2b898062e8ea7e38e706223b73c735c2944d735d241f01c0e; run 43686937403 artifact 14151275928, ZIP SHA-256 8bc78c7e5cb7e70898482e2168acff250db57079d6487bb2c4b15e75379b2b46; run 43686920391 artifact 14151330140, ZIP SHA-256 bac06283db0f69ab35d357019c3a9b44ed7ee789c376941a50807e8b0b251774; run 43686917332 artifact 14151450202, ZIP SHA-256 0da861d3d50d9415868bfaf8b832fdf0b906e0277f5301a025cbcf1bc2498600.
- Inspected job logs: all five runs show the optional live 1-minute feed step reported BLOCKED_SOURCE_ACCESS_403, rows=0, symbols=0, one QUOTE:HTTPError 403 for PALREDTEC; the workflow explicitly has continue-on-error: true for this step. Therefore workflow SUCCESS is accurate, but live-1m coverage remains BLOCKED/UNKNOWN and must not be described as a PASS. No synthetic rows were created; later risk modifier and artifact upload steps completed. Context snapshot differs across runs (macro/geo values), so do not collapse their outputs as identical.
- Run-level conclusion and artifact existence were verified from GitHub; this is a status/artifact audit, not an independent content-level validation of all five 61-MB ZIPs. Do not redownload/reprocess all five unless a targeted artifact question requires it. Recommended next step: inspect one representative latest artifact's backtest/QA summary and determine whether the optional 403 affects any required acceptance gate; keep the other four immutable artifacts as provenance.
- No code changes, workflow reruns, production selector/ranking/pressure-fade/CORE-672 changes, paid API/service, spend, or PR merge.


## 2026-11-15 — Representative collector artifact content audit (Run 43687120198)
- Downloaded and inspected one representative artifact only (Run 43687120198; artifact 14151241008; ZIP SHA-256 from upload log: 5e4596f93454cca24d4a276e26bad99e6bc01adb574510506eae26a67c74a238; uploaded size 61,618,318 bytes). Other four artifacts were not redundantly downloaded.
- Artifact contains 25 files, including raw 200-session dataset, session coverage, QA report, context/live status, provisional selections, 672 diagnostics, walk-forward predictions/metrics, feature ablation and winner-separation outputs.
- Data QA report: PASS; 200 raw files, 200 sessions, 200 processed dates, 2,994 symbols, delivery quantity and delivery percentage coverage both 100%, no QA issues. Session coverage spans 2026-02-09 through 2026-11-13; symbols have differing available-session counts (e.g. 21STCENMGM 193), so 200-session universe coverage is not 200 sessions for every symbol.
- Walk-forward report records 100/100 tested cutoff sessions and 3,000 candidate rows. Reported precision/lift: T5_H1 precision 0.212, lift 2.344; T10_H3 precision 0.3977, lift 9.843; T20_H5 precision 0.1987, lift 24.759. These are descriptive gross high-price hit statistics, NOT net trading returns, not proof of the target strategy after costs, and not a substitute for the specified 0.22% transaction-cost backtest.
- Critical methodology boundary: artifact metrics identify their engine as V11.4 Historical Winner Separation Engine; source pipeline/walk_forward_backtest.py also labels itself V11.4. Its source code has no 0.22% transaction-cost/slippage/fee implementation. It computes future high-price excursions over H+1/H+3/H+5. Therefore this artifact cannot be accepted as the final V11.3 0.22%-cost rolling backtest; keep it as supplementary historical winner-separation evidence only.
- Critical 672 boundary: artifact report has 672 columns (56×12), 2,994 rows and states NEGATIVE/NOT_APPLICABLE/POSITIVE/UNKNOWN. But source diagnostic_state() rotates only 25 measurable features across the 672 slots. This demonstrates structural 672-column output, not independent validation of 672 distinct core diagnostic signals. Do not count it as full CORE-672 acceptance without approved semantic mapping/evidence per signal. No change to production diagnostic architecture is made here.
- Final selection report is explicitly PROVISIONAL_ONLY_FINAL_SELECTION_BLOCKED with blockers RISK_GEO_NOT_AVAILABLE and LIVE_INTRADAY_1M_FEED_MISSING; top 30/10/3 are provisional shortlists, not actionable finalists. Live 1m status is BLOCKED_SOURCE_ACCESS_403 (PALREDTEC, rows=0). Market context has GDELT HTTPError, GDELT read timeout, and Google News RSS NameError; geo context unavailable. FII/DII snapshot has one date only (13-Nov-2026).
- Conclusion: collector job/workflow and artifact upload PASS; raw-data QA PASS for this run; 100-session V11.4 historical separation report generated; final selection remains BLOCKED; V11.3 acceptance, 0.22%-cost backtest and distinct 672-signal validation remain NOT_DONE/UNKNOWN. Preserve the artifact and do not rerun merely to reproduce it.
- No code changes, workflow reruns, selector/ranking/pressure-fade/CORE-672 production changes, paid APIs, spend, PR merge, or external contact.


## 2026-11-15 — Corrective audit: V11.3 transaction-cost and 672-diagnostic implementation
- Follow-up source review supersedes the earlier tentative statement that 672 diagnostic columns merely rotate 25 features. The artifact's production 672 matrix is generated by pipeline/diagnostics_672.py, not by walk_forward_backtest.py's separate backtest-side diagnostic helper. The correct production-matrix finding is more severe and directly measured from representative artifact 14151241008.
- Inspected pipeline/diagnostics_672.py (SHA af0a8ddc17d72024509167533585713600a4b845). Its nested 56×12 loop computes the same `base` from ENERGY, LEAD_TIME and RVOL20 for almost every diagnostic step/filter; only a few special step branches exist (FII/DII, VIX, Geo, catalyst/event/live UNKNOWN). The filter name is not used to define an independent evidence predicate; each filter receives the same `state(base)` for a given generic step.
- Programmatic audit of outputs/diagnostics/diagnostics_672.csv in artifact 14151241008: 672 diagnostic columns × 2,994 rows, but only 3 unique full-column state vectors across all 672 columns; 540 columns share one vector, 120 share a second vector, and 12 share a third vector. 132 columns are constant UNKNOWN (nunique=1); the remaining 540 columns have 3 states. Aggregate cell counts: UNKNOWN 910,080; NEGATIVE 715,500; POSITIVE 386,388. Therefore 56×12 output shape is present, but 672 independent diagnostics are NOT implemented/evidenced in this artifact. This is a verified blocker, not a PASS.
- Walk-forward file pipeline/walk_forward_backtest.py (SHA d085f7a2d35a88b4c4eaba65144a429a06961b09) is explicitly titled V11.4 Historical Winner Separation Engine. Its reported targets are FUT1/3/5 HIGH price excursion, and source has no 0.22% transaction-cost, slippage, or fee calculation. GitHub code search for `0.22` in this repository returned no results; search for `transaction cost` returned no relevant implementation. Thus the required 0.22%-cost V11.3 rolling backtest remains NOT_DONE. Do not mistake gross high-price hit precision/lift for net strategy performance.
- The walk-forward metric precision is calculated on the concatenated Top-30 predictions (3,000 rows = 100 cutoffs × 30), not on all 2,994×100 universe rows. Reported T5_H1 0.212, T10_H3 0.3976667, T20_H5 0.1986667 are gross Top-30 hit precision. Artifact also has 250,568 full-universe probability calibration observations; these are probability calibration metrics, not net P&L.
- No production code changed. The next implementation work must be a separately scoped, approval-safe research module/spec with explicit entry/exit assumptions and 0.22% round-trip cost applied once, strict cutoff isolation, executable-price/limit/circuit handling, missing-data fail-closed behavior, and tests. Separately, 672 signal definitions need an approved unique step×filter evidence registry; do not patch the production matrix or selectors without explicit permission.
- This corrective finding supersedes the previous ledger note that inferred 25-feature reuse in the production 672 matrix. The previous statement about walk-forward's own helper remains distinct and is not evidence of production matrix behavior. No reruns, spend, paid APIs, PR merge, or changes to selector/ranking/pressure-fade/CORE-672.


## 2026-11-15 — V11.3 cost-aware backtest research contract drafted
- Created `docs/V11_3_COST_AWARE_ROLLING_BACKTEST_RESEARCH_CONTRACT_20261115.md` (research-only draft; not implementation, not backtested, not accepted). It defines the 0.22% total round-trip cost convention as a configurable 0.22 percentage-point deduction once per completed trade, with explicit unit guard and 0.00/0.22/0.44% sensitivity reporting. It does not treat the value as a broker-specific fee schedule; slippage remains separately unmodelled.
- The contract captures leakage/maturity rules, required trade-level ledger, net/gross metrics, provenance manifest, 15 minimum tests, and acceptance gates. It expressly forbids production selector/ranking/+1 pressure-fade/672 changes and any synthetic fills.
- Crucial unresolved dependency: source evidence does not establish entry timing/price, target fill semantics, stop-loss/no-stop, same-bar target/stop ordering, gap fill, circuit/illiquid handling, or portfolio concurrency. G0 remains BLOCKED pending user's explicit decision; no executable trade simulator was coded because silently inventing these rules would invalidate the research.
- Contract commit: 1aecb49b68a460449e72aff7715ebc65a7191144.
- Progress for this scoped task: source audit 100%; research contract draft 100%; user policy decisions 0% (pending); implementation/tests 0%; historical replay 0%; independent reconciliation 0%. No workflow rerun or production code modification.


## 2026-11-15 — User-approved V11.3 research-only execution policy and isolated replay implementation
- User explicitly approved: entry = next trading session OPEN; target = intraday HIGH touch; stop-loss = -3%; if neither target nor stop triggers, exit = horizon final-session CLOSE. Approval is limited to research backtest; Production Selector, RANKING_SCORE, +1 PRESSURE_FADE and 672 diagnostics must remain unchanged.
- Added isolated module `pipeline/v11_3_cost_aware_backtest.py` (commit `94b5731de6f57ce0fa5fe5abc7a48b560a7424a9`). It reads the historical OHLC dataset and existing cutoff/symbol signal ledger; creates three independent trade simulations per signal (+5/H1, +10/H3, +20/H5); deducts 0.22 percentage points once from gross round-trip return; uses stop-first for same-bar target/stop ambiguity; stop gaps fill at observed OPEN; target fills at target price unless OPEN is already above target; no-target exits at horizon close. Missing symbol sessions, non-traded/invalid OHLC, duplicate keys, and immature horizons fail closed. It emits trade ledger, metrics/manifest, and output SHA-256 file.
- Added 8 unit tests in `tests/research/test_v11_3_cost_aware_backtest.py` (commit `bd334a0c6ec6a4a52ac4845e28e34bb39f1248b2`) covering cost-once arithmetic, target, same-bar stop-first, stop gap, horizon-close exit, missing session, immature horizon, zero-volume and invalid cost.
- Added bounded 5-minute GitHub Actions test workflow `.github/workflows/v11_3_cost_aware_backtest_tests.yml` (commit `8f70a9395ae632ed4a4aca48d1d8c4098aea79dc`). This workflow is separate from the production collector workflow. Runtime PASS is not yet observed; do not report tests as passed until a completed run is fetched.
- Important limitations: OHLC daily bars cannot establish intraday event sequence; stop-first is conservative. Circuit/price-band data is not present in the inspected processed OHLC schema, so such constraints are not independently validated by this first implementation. Slippage/market impact are not modelled. Existing walk-forward predictions are reused only as cutoff/symbol signals; their gross outcome fields are ignored by the new simulator. No actual historical replay has been run yet.
- No production code, selector, ranking, pressure-fade, diagnostic matrix, or production workflow was modified. No collector workflow rerun, no spend, no paid APIs, no PR merge.
- Scoped progress: policy approval 100%; research module draft 100%; unit-test source 100%; test runtime validation pending; full historical replay 0%; independent trade-ledger reconciliation 0%; final acceptance BLOCKED.


## 2026-11-15 — CI runtime validation initiated; metrics naming correction
- Corrected output metric semantics in `pipeline/v11_3_cost_aware_backtest.py`: replaced ambiguous `NET_TARGET_HIT_RATE` (which actually measured positive-net target exits) with explicit `TARGET_EXIT_RATE` and `NET_PROFITABLE_TARGET_EXIT_RATE`. Commit `65b3515e973623325c5928fd4b69c50683249a6f`.
- Hardened test invocation to `unittest discover -s tests/research -p test_v11_3_cost_aware_backtest.py -v` to avoid namespace-package/module-shadowing ambiguity. Workflow fix commit `dee9a191cbbff6733ca720a297d299a7da548e2d`.
- GitHub Actions Run #3 / Run ID `43692239851` was observed on commit `dee9a191cbbff6733ca720a297d299a7da548e2d`. At latest check (2026-11-15T07:57:30Z), job `research-unit-tests` was `in_progress`; checkout and Python setup succeeded, dependency installation was in progress, and unit tests had not yet started. Runtime PASS therefore NOT_YET_VERIFIED. No log available yet while job was running.
- No full 200-session replay started. No production files or collector workflows touched.


## 2026-11-15 — Run #3 failure diagnosed; fixtures corrected
- Run #3 / `43692239851` completed FAILURE. The 8 tests ran: 6 passed, 2 failed. Dependency install and runner setup passed.
- Root cause is test-fixture semantics, not yet evidence of a simulator defect: (1) the stop is correctly 3% below the actual next-session entry price, so a low opening price on the entry session cannot be a stop-gap when that same open defines entry; the gap fixture now places the gap on the following session and uses a 3-session horizon. (2) the missing-symbol-session test removed the date from the entire single-symbol dataset, which also removed it from the inferred global trading calendar; fixture now retains that global date via an OTHER symbol row while omitting ABC for that session.
- Corrected test commit `4e144b34ce1b8d8aa0dfc5ca43ccb80b8bea3536`. New Run #4 ID `43692345179` observed QUEUED on that commit. Awaiting its actual result; no test PASS claimed.
- Historical replay remains NOT_STARTED pending CI PASS and additional code review. Production selector, ranking, pressure-fade, CORE-672 and collector unchanged.


## 2026-11-15 — Run #4 result and second fixture refinement
- Run #4 / `43692345179` completed FAILURE. Seven of eight tests passed; only `test_gap_below_stop_fills_open` failed. The failure log shows an earlier entry-session bar hit the +5% target before the later stop-gap bar, so the simulator correctly exited at TARGET. This is a test fixture ordering issue, not a simulator failure.
- Corrected the fixture to keep the first session below target and introduce the gap on the following session. Commit `c3d5028eafa7e936bdfdd1fd271ce532cf226607`.
- A fresh CI run is triggered by the push; its result must be checked before any replay. Do not rerun collector or completed unrelated workflows.
- CI status: Run #3 6/8 tests; Run #4 7/8 tests; latest test correction committed, runtime pending. Historical replay remains NOT_STARTED.


## 2026-11-15 — Research backtest CI PASS and fail-closed code review
- Cost-aware research test Run #5 / ID `43692427702`, commit `c3d5028eafa7e936bdfdd1fd271ce532cf226607`: SUCCESS. Job `research-unit-tests` and all eight tests completed SUCCESS.
- Post-PASS code review found direct-call validation gaps not covered by the initial suite: malformed DATE values and duplicate SYMBOL/DATE keys could bypass the run() guard when calling simulate_one() directly; target_pct and horizon were not explicitly validated. Added fail-closed validation and tests for NaN/Inf/negative cost, non-positive target, fractional horizon and direct duplicate keys.
- Research module commit `b7099903939542edd82cc8b7d37f6a34b50718c3`; test commit `cc4d397f25e735e9f7b63d2da74b40baff1aaab9`. New CI Run #6 ID `43696697367` (code commit) and Run #7 ID `43696699661` (test commit) were observed QUEUED; #7 is the run containing both changes and must be used for next verification.
- Historical replay remains NOT_STARTED pending Run #7 PASS and source/input gate. The previously inspected 200-session artifact does not contain circuit/price-band fields; the replay cannot claim circuit-feasible execution without a separately validated restriction source or an explicit limitation. Existing V11.4 signal file semantics must also be confirmed before treating it as an accepted V11.3 signal set.
- No production selector, ranking, pressure-fade, CORE-672, collector, or historical source artifact modified.


## 2026-11-18 — Continuation page 36, Part 1: IMF SDMX Central RSS / registration audit
- New evidence note: `docs/IMF_SDMXCENTRAL_RSS_REGISTRATION_AUDIT_PART1_20261118.md`.
- Commit: `80c93853f0abf90e985d6b54cb6be893cd9963e8`; file was fetched back from GitHub after commit and verified present (blob SHA `0e6a2ecda679f84362c66cb8e6956333dbb24b68`).
- Official IMF SDMX Central User Guide documents RSS endpoint `https://sdmxcentral.imf.org/rss.xml` and transaction semantics: structure/data registration events link to SDMX-ML 2.1 RegistryInterface documents containing SubmitStructureRequest or SubmitRegistrationRequest. Endpoint route/documentation discovery PASS; RSS HTTP retrieval remains NOT_RETRIEVED. No status, response headers, raw bytes, item count, retrieved timestamp or SHA-256 claimed.
- Official live registration listing `https://sdmxcentral.imf.org/data/registrations.html` displays Brazil row IMF:BOP6(1.0), provider IMF:BR1, BCB XML URL ending `BOP_BPM6.xml`, last updated `2026-10-26T11:47:29.000Z`. This is listing evidence only, not RSS event retrieval or XML validation.
- Prior screenshot records BCB header/Dataflow mismatch CONFIRMED. Preserve exact identifiers; do not normalize BOP_BPM6 to BOP6. Raw BCB XML DataflowRef and ProviderRef validation remains UNKNOWN / NOT_DONE.
- Part-1 defined source-discovery and registration cross-check scope complete; RSS raw retrieval, XML parse, event reconstruction, BCB XML hash/validation remain NOT_DONE / UNKNOWN. Brazil flow, Global EM and Trading admission remain NOT_AUTHORIZED.
- Next bounded action: short CI retrieval of RSS with status/final URL/content-type/retrieved_at_utc/byte count/SHA-256; parse only valid RSS; follow actual Brazil event link if present; separately fetch BCB XML and compare exact Header refs with IMF registry. Keep job <10 minutes.
- No production changes, no PR merge, no synthetic data, no paid API, no changes to Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 or Engines A-E. UNKNOWN is not PASS.


## 2026-11-18 — Continuation page 36, Part 2: isolated IMF retrieval workflow
- Reused Part-1 report `docs/IMF_SDMXCENTRAL_RSS_REGISTRATION_AUDIT_PART1_20261118.md` (commit `80c93853f0abf90e985d6b54cb6be893cd9963e8`) and prior continuity-ledger update (commit `7ebf107aa973d5a8e5158a951925297f90c16798`).
- Created isolated workflow `.github/workflows/imf_sdmx_rss_registration_audit.yml`; commit `2e5361d2ef46d4ae7b052f0846c8c5e78fe7d430`; blob SHA `82c35eec26a2fd93797c7325553cb727fef04c29`. Fetched back from GitHub and verified. One job, ubuntu-latest, timeout 8 minutes, contents:read, standard-library urllib; captures status/final URL/content-type/retrieved_at_utc/bytes/SHA-256, raw XML, RSS item fields, BCB Header reference elements, summary.json and 90-day artifact. Trigger: workflow_dispatch plus narrowly scoped push on this workflow file.
- Part-2 evidence note: `docs/IMF_SDMXCENTRAL_RSS_REGISTRATION_AUDIT_PART2_20261118.md`; commit `b90327619705cf10477ac7b5f85cc0ae155f7a85`.
- Execution is NOT_VERIFIED: workflow run listing could not be read through the available GitHub read interface; no run ID, artifact ID, HTTP response, raw XML hash or XML validation result is claimed. A committed workflow is not a successful workflow run. If push trigger did not fire, repository owner must use workflow_dispatch in GitHub UI; current connector exposes no workflow-dispatch write action.
- Direct browser retrieval of RSS returned internal/access error; BCB XML browser open rejected text/xml. These are browser-interface limitations, not proof that official endpoints are down.
- Next action: inspect Actions run/artifact; if no run, user manually dispatches this isolated workflow; verify raw payload and recompute hashes; parse actual event only if present; compare exact BCB DataflowRef/ProviderRef with IMF registry. Do not rerun 60-minute NSE collector.
- No production changes, PR merge, paid API, synthetic data or admission authorization. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 and Engines A–E unchanged; UNKNOWN is not PASS.


## 2026-11-18 — Continuation page 36, Part 2: IMF raw retrieval verified; Brazil mismatch remains blocking
- Updated evidence note: `docs/IMF_SDMXCENTRAL_RSS_REGISTRATION_AUDIT_PART2_20261118.md`, commit `048c7fea9cca3601e8ad7bfeb8808c21953d7430`.
- Reused earlier full Brazil contract reconciliation run `44290101769`, artifact `14420378420`, digest `6435b5df856889ae1a48742681f0b127b04e1a4057c361b054c329a5049fc8aa`. It had already established exact payload Dataflow `IMF:BOP_BPM6(1.0)` vs registry `IMF:BOP6(1.0)`, same DSD `ECOFIN_DSD` but distinct Dataflow identities, and constraint compatibility 234/237 (98.7342%) under BOP6 vs 27/237 (11.3924%) under BOP_BPM6. Mismatch CONFIRMED; no alias inference; Brazil admission remains BLOCKED pending authoritative resolution.
- New dedicated workflow run #1 `44301482210` SUCCESS; artifact `14426565546`, SHA-256 digest `0a35ddb0f83ae2c14f5ce2a60dc365f5324e56de55a3442227b8a74e786a132f`. Raw IMF RSS HTTP 200/application-xml, retrieved `2026-11-18T12:11:06.691171+00:00`, 30,110 bytes, SHA-256 `8dcad0ed2f284ad6a3326a031ab81d6a311aa94cb1ab44eb4ad65fa36e3e69a2`; XML parse PASS, 33 items (transaction IDs #38646 to #38614 in captured feed). Raw BCB XML HTTP 200/text-xml, retrieved `2026-11-18T12:11:07.589328+00:00`, 4,840,062 bytes, SHA-256 `3e736c45d67fe64ac8c0cb3396718addab21a1ef43d09666ae8dd8ccaba3f52c`; well-formed XML parse PASS. Raw-file hashes independently recomputed from downloaded artifact.
- Two additional duplicate retrieval runs completed SUCCESS: `44301625778` artifact `14426296464`, digest `64bdb245a0d6242969615b7f86ba1fea3ea9f1605f721bdd65a396a0134bd66c`; `44301659461` artifact `14425444941`, digest `036e81dd4e7c36ea2d653a05cc8dad4826b27b8fc98e9182d146f8a022422b02`. These are duplicate transport evidence, not independent observations; no more raw re-download needed absent new requirement.
- RSS transaction links exist, but transaction-detail RegistryInterface payloads were not retrieved; Brazil historical event reconstruction remains UNKNOWN / NOT_DONE. New workflow's first parser did not detect literal DataflowRef because BCB identifies Dataflow in root schemaLocation and Structure namespace; parser corrected to extract this in commit `0e4fd08428f0fcaf2ae34b2e48a0ceac58e36b00`, not yet rerun. Existing prior contract audit is the accepted Dataflow evidence.
- Trigger incident: first IMF workflow commit also triggered full NSE collector run #169 / ID `44301482238` because main collector paths-ignore lacked the new workflow path. Run was observed in progress at “Acquire 200 NSE market sessions”; connector lacks cancel write. User/owner should cancel if still running: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/44301482238 . Fixes: main collector now ignores IMF workflow path (commit `00bbdf1f00d3d8ec633df4ca85f004a03c1e20fa`) and IMF marker path (commit `e75a1326647c8e256bde8fec2b8fba5035f5edc0`); dedicated workflow now manual-only with hardened parser (commit `0e4fd08428f0fcaf2ae34b2e48a0ceac58e36b00`).
- Next action: bounded read-only resolver for captured RSS transaction IDs; parse actual SubmitRegistrationRequest and identify any IMF:BR1 / BCB URL event. If none in captured 33-item window, state only that no Brazil event was found in that window. Do not repeat raw fetch or run the full collector.
- No production change/PR merge/trading admission. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 and Engines A-E unchanged; UNKNOWN is not PASS.


## 2026-11-18 — Continuation page 37: IMF recent transaction window resolved; no Brazil event in 33-item sample
- New report: `docs/IMF_REGISTRY_TRANSACTION_RESOLUTION_PART3_20261118.md`; commit `549a1379e26b54ee0f5a11ccc201dc8d7ae19f5f`.
- Reused exact 33 RSS links from archived RSS run `44301482210`, artifact `14426565546`, RSS SHA-256 `8dcad0ed2f284ad6a3326a031ab81d6a311aa94cb1ab44eb4ad65fa36e3e69a2`; did not re-fetch RSS or BCB XML.
- Resolver run #1 `44302351313` SUCCESS; artifact `14426702319`; digest `sha256:270aad8014a246c6a3aca6b2f03d22ee027f6fde575e3f5760cb06b5bc552dfd`; downloaded ZIP SHA-256 independently recomputed and matched. All 33 transaction URLs returned HTTP 200; all 33 XML payloads were well-formed; all 33 `QueryRegistrationResponse` records had `StatusMessage status=Success`.
- Correct actual payload shape: root RegistryInterface -> QueryRegistrationResponse -> QueryResult/DataResult/Registration -> ProvisionAgreement + Datasource/SimpleDataSource. They were not SubmitRegistrationRequest documents. First parser under-classified the QueryRegistrationResponse and did not collect ProvisionAgreement; raw artifact was independently re-parsed. Parser source correction commit `59710ea3a8a9b7133859a2d571b2cd165cc18a7a` now recognizes QueryRegistrationResponse, StatusMessage, ProvisionAgreement and Datasource; that parser fix has NOT been rerun.
- Exact bounded-window result: no literal `IMF:BR1`, no registered Brazil BCB URL/host, and no BOP_BPM6 Brazil reference in any of the 33 returned registration records. Prefix distribution: IMF:IL_* 21; IMF:CL_* 6; IMF:AT_* 2; IMF:HU_* 2; IMF:NL_* 1; IMF:PT_* 1. Transaction #38642 is `IMF:CL_BOP(1.0)` with Chilean host `si3.bcentral.cl` and SDMXCategory=SDMX_BOP6; this is a false positive if mistaken for Brazil. #38643–38646 also CL_* records. Thus only conclusion: NO_BRAZIL_REGISTRATION_MATCH_IN_THIS_33_TRANSACTION_WINDOW; outside-window historical event remains UNKNOWN.
- Brazil mismatch remains CONFIRMED from run `44290101769` / artifact `14420378420`: registry `IMF:BOP6(1.0)` vs BCB payload `IMF:BOP_BPM6(1.0)`; Brazil admission BLOCKED pending authoritative resolution. No trading admission.
- Trigger lesson: resolver script commit `6751823c58594409a1e241bf605aba6d40424050` and workflow commit `a3fcdb135ee02c4aa4ec04944045f628b40c28a1` happened before paths-ignore guard and accidentally triggered collector runs #170 `44302281284` and #171 `44302288225`. Earlier accidental run #169 `44301482238` was also still active at last check (had passed 200-session acquisition, Security Master, dataset build and Strict QA; walk-forward backtest in progress). Runs #170/#171 were at 200-session acquisition. Actions cancel is unavailable in current connector; user/owner must cancel from Actions UI if still active. The guard is now committed: `nse_collector.yml` commit `ea7381135a388fe291e85d62cddbd9c37aec49d4` ignores resolver workflow, script and trigger marker. Do not create another push trigger for this workflow.
- Next: targeted historical lookup for exact `IMF:BR1`, registered BCB URL, and relevant ProvisionAgreement/Dataflow URNs using documented IMF Activity / Provision Agreement public read endpoints. No unbounded registry scrape, no guessed transaction ID.
- Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 and Engines A–E unchanged. No PR merge or production integration; UNKNOWN is not PASS.


## 2026-11-18 — Continuation page 38: IMF Brazil historical registration GUI/API boundary and macro priority queue
- New report `docs/IMF_BRAZIL_HISTORICAL_REGISTRATION_RECONSTRUCTION_PART4_20261118.md`, commit verified by fetch (blob SHA `ad2235848d7e6a3956e624b9bda3ae08ef2142a3`), records the official IMF Data Registrations historical activity view, visible field schema, official API boundary, exact next action, and deferred high-priority India macro queue.
- IMF Data Registrations view `https://sdmxcentral.imf.org/activity/data-log.html` was inspected. It exposes Agency/Id/Version, Date, Data URL, Action, Data Store, Series, and Registration Details fields (Data URL, Provision URN, Dataflow URN, Data Provider URN, User). Static page extraction exposed no actual rows; no Brazil history timestamp or event is claimed.
- IMF SDMX Central Web Services Guide states there is no official REST API for registration/validation/conversion processing services. No undocumented internal endpoint or guessed transaction ID will be used.
- Reused Part-3 bounded 33-transaction result; no repeat RSS/BCB/transaction downloads. Brazil current mismatch remains CONFIRMED; historical chronology remains UNKNOWN; admission BLOCKED.
- User's high-priority macro topics are captured as a deferred gap queue, not integrated ahead of Brazil closure: P0 US 10Y/Fed/USD/INR/Brent, India FPI/DII sector flow and NSE event study; P1 China rotation/tariffs, Korea/Taiwan AI-semiconductor relative performance, Japan/JPY carry-stress and relative TRI panels. Existing source register already identifies Fed H.10 broad dollar, US DGS10, RBI FX, EIA Brent, CDSL/NSDL FPI and NSE index routes, but synchronized ingestion and India-market predictive validation remain incomplete. H.10 broad dollar is not ICE DXY; NSDL fortnightly data must not be daily-interpolated.
- Exact next action remains Brazil-only: retrieve actual Brazil-specific historical registration rows via official GUI/downloadable documents; compare create/replace/delete chronology to the exact BOP6/BOP_BPM6 and IMF:BR1 identifiers. If unavailable, preserve UNKNOWN/BLOCKED.
- No production changes, no macro overlay integration, no PR merge, no paid APIs, no fabricated data. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 and Engines A-E unchanged; UNKNOWN is not PASS.


## 2026-11-18 — Continuation page 39: IMF Brazil Registration History UI filter audit
- New report `docs/IMF_BRAZIL_REGISTRATION_HISTORY_PART5_20261118.md`; commit `e5acca64ca6b5700ec2d1541e676e4af22c46e76`.
- Official IMF Data Registrations page was inspected beyond the static table: it explicitly offers "Breakdown By Provision Agreement", "Breakdown By Dataflow", "Breakdown By Data Provider", and "Show All Data Registrations". Detail fields include Data URL, Provision URN, Dataflow URN, Data Provider URN and User; event rows include Date, Data URL, Action, Data Store and Series. The static extraction still contains no event rows; interactive provider filter is NOT_DONE.
- Official IMF provider directory identifies `IMF:BR1` as Central Bank of Brazil; current registration listing continues to show `IMF:BOP6(1.0)` / `IMF:BR1` / BCB URL. This is current-state evidence, not historical chronology.
- Official Provision Agreements page exposes URN, URL, Revisions, Description, Annotations, Valid From/To and Changelog/Export controls; no selected Brazil agreement's dated history has yet been captured.
- API boundary clarified from IMF Web Services Guide (May 2025): standard SDMX structure REST entry point is documented, while registration processing uses separate FMR entry point. FMR is not accepted as a historical-registration read API. Candidate standard structure-query URL browser retrieval returned internal access error; no HTTP status/raw payload/hash or endpoint failure claimed.
- No repeat RSS/BCB downloads, no guessed event ID, no undocumented AJAX endpoint. Historical Brazil chronology remains UNKNOWN; BOP6 vs BOP_BPM6 mismatch CONFIRMED; Brazil admission BLOCKED.
- Next single action: use official Data Registrations GUI -> Breakdown By Data Provider -> exact provider IMF:BR1; capture actual dated rows and details, then capture the corresponding Provision Agreement Changelog/exports. If no rows or authorized login is required, preserve the limitation and remain UNKNOWN.
- High-impact macro queue remains deferred behind Brazil closure: P0 US 10Y/Fed/USD/INR/Brent/OPEC+, India FPI/DII sector flow and 200-session event study; P1 China/EM, Korea/Taiwan AI/semiconductor, Japan/JPY carry and relative TRI. No integration or factor weights without synchronized evidence and incremental out-of-sample validation.
- ₹0, official/free sources only; no synthetic data, fabricated timestamps, guessed IDs/endpoints. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 and Engines A–E unchanged; UNKNOWN is not PASS.


## 2026-11-18 — গবেষণা যাচাই অব্যাহত 36, Part-4: official registration/export boundary re-check
- New report: `docs/IMF_BRAZIL_REGISTRATION_HISTORY_PART4_20261118.md`; initial report commit `4bd387a29560950b9ffba5c6177451e30e955b65`; corrected canonical file commit `32debb1c7ed7a25718d5faed20c92fd271a3b477.
- Re-checked the official current Registrations page: it still displays `IMF:BOP6(1.0)` / `IMF:BR1` / the BCB URL with Last Updated `2026-10-26T11:47:29.000Z`. This is current-state metadata, not a historical create/replace/delete event.
- Official Data Registrations activity page still exposes provider/dataflow/provision-agreement filter modes, but accessible static extraction contains no event rows. Exact interactive `IMF:BR1` filter remains NOT_DONE.
- IMF generic structure search/export page warns that Data Registrations and Metadata Sets cannot be downloaded through that generic structure-export facility. Do not expect structure export to substitute for registration history.
- Re-tried the documented Provision Agreement structure query through browser retrieval; it returned an internal access error. This is only a retrieval-interface limitation; no HTTP status, payload, endpoint outage, or invalidity is inferred.
- Acceptance: current Brazil row PASS (current-state only); provider identity PASS; history filter schema PASS; actual Brazil event rows NOT_DONE; Brazil Provision Agreement URN/changelog NOT_DONE; chronology UNKNOWN; BOP6 vs BOP_BPM6 mismatch CONFIRMED; Brazil admission BLOCKED / EM market use NOT_AUTHORIZED.
- Next single action: interactive official GUI -> Data Registrations -> Breakdown By Data Provider -> exact `IMF:BR1`; capture actual dated rows/details, then linked Provision Agreement URN and Changelog/exports. If authorization or UI access is required, preserve limitation and remain UNKNOWN. No guessed IDs/endpoints.
- No repeat RSS/BCB downloads; no production changes, PR merge, trading admission, or macro integration. ₹0 official/free sources only; no synthetic data. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 and Engines A–E unchanged; UNKNOWN is not PASS.


## 2026-11-18 — গবেষণা যাচাই অব্যাহত 36, Part-5: IMF SDMX Transactions Activity
- New report: `docs/IMF_BRAZIL_REGISTRATION_HISTORY_PART5_TRANSACTION_ACTIVITY_20261118.md`; commit `27d6398aa9fcf96113e9e2dad53a308b5d8c85cc`.
- Official IMF SDMX Transactions view exposes Transaction Time / Transaction Type / Action and Download Transaction. Search-indexed rendering showed a bounded 18-row sample of generic Structure Submission Replace/Delete entries, timestamps 2026-05-15 through 2026-10-08. Same rendering inconsistently says “Showing 1 to 2 of 100 entries”; sample is not treated as complete.
- Static extraction provides no row payload/IDs and visible rows identify no agency, dataflow, provider, Provision Agreement or Brazil URL. No row can be attributed to Brazil.
- Login and confirmation/re-authentication UI is visible; no credentials used. No selected-row SDMX-XML or CSV View Details artifact available. FMR View Activity docs describe those controls, but that is capability documentation only.
- Did not repeat archived 33 RSS transaction downloads or BCB XML retrieval; no guessed transaction ID or undocumented endpoint.
- Acceptance: official page/schema PASS; bounded timestamp sample PASS (sample only); Brazil-specific transaction NOT_DONE; transaction XML/CSV NOT_DONE; chronology UNKNOWN; mismatch CONFIRMED; Brazil admission BLOCKED / market use NOT_AUTHORIZED.
- Next: authorized interactive GUI selection -> Download Transaction / View Details; inspect actual XML/CSV for exact IMF:BR1, BCB URL, BOP6/BOP_BPM6 and Provision Agreement identifiers. If login required, owner supplies downloaded file. No timestamp-only attribution.
- ₹0 official/free only; no synthetic data, guessed IDs/endpoints. Macro Overlay deferred. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 and Engines A–E unchanged; UNKNOWN is not PASS.


## 2026-11-18 — গবেষণা যাচাই অব্যাহত 36, Part-6: IMF SDMX public transaction access boundary
- New report: `docs/IMF_BRAZIL_REGISTRATION_HISTORY_PART6_PUBLIC_ACCESS_BOUNDARY_20261118.md`; commit `6cdf9f26c6ae8f46593006c641df2189514ddf67`; verified blob SHA `58d6d2733aa7259574c6b9cbad0a5aceb520647e`.
- Rechecked official SDMX Transactions page. Public rendering exposes Transaction Time / Transaction Type / Action and Download Transaction, but no row IDs, row payloads or Brazil-specific identifiers. Its displayed date range and contradictory “1 to 2 of 100 entries” vs 18 visible records prevent an exhaustive-history claim.
- Official IMF login page confirms an authenticated UI exists; this does NOT prove every activity-log row/download requires login. Anonymous row-level Download Transaction / View Details behavior remains UNKNOWN because no authenticated interactive selection was performed and no credentials were used.
- Official Web Services Guide says there is no official REST API for registration-processing services; standard structure REST is not a historical registration-event API. Official User Guide documents RSS transaction notifications and says each transaction links to a RegistryInterface document containing SubmitStructureRequest or SubmitRegistrationRequest. The exact linked event document, not a timestamp, is the required evidence.
- Official generic Search/Export page explicitly warns that Data Registrations and Metadata Sets cannot be downloaded through generic structure export; that route is REJECTED as a substitute.
- Reused the existing bounded 33-item RSS evidence; no repeat RSS or BCB download. Prior no-Brazil-match result remains limited to that sample; outside-window chronology remains UNKNOWN.
- Acceptance: official page/schema PASS; RSS event-document mechanism PASS; Brazil-specific transaction XML/CSV NOT_DONE; anonymous row-level access UNKNOWN; historical chronology UNKNOWN; BOP6 vs BOP_BPM6 mismatch CONFIRMED; Brazil admission BLOCKED / EM market use NOT_AUTHORIZED.
- Exact next action: owner-side authorized GUI selection of a dated transaction -> Download Transaction / View Details -> save SDMX-XML/CSV and inspect exact IMF:BR1, BCB URL, BOP6/BOP_BPM6 and Provision Agreement URNs. If login is required, owner supplies only exported file; never credentials. Do not infer from timestamps.
- No production changes, no PR merge, no macro overlay integration/weights, no synthetic data or guessed endpoints. ₹0 official/free only. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E unchanged; UNKNOWN is not PASS.


## 2026-11-18 — গবেষণা যাচাই অব্যাহত 36, Part-7: IMF RSS subscription and timestamp semantics
- New report: `docs/IMF_BRAZIL_REGISTRATION_HISTORY_PART7_RSS_SUBSCRIPTION_AND_TIMESTAMP_SEMANTICS_20261118.md`; commit `f2306d2ff9b5c33deab03eaaf1e10027d4707121`; verified blob SHA `d805898903ff3fb7dee99804db2210ab439aa15e`.
- Inspected the official IMF SDMX Central User Guide (May 2025), §6 and §7. It states that re-registering an existing URL updates the Registrations table's Last Updated timestamp. Therefore the Brazil row's `2026-10-26T11:47:29.000Z` cannot be assumed to be its original creation date; initial-registration vs re-registration semantics remain UNKNOWN absent the actual event document.
- The guide documents RSS, email and HTTP POST notifications. RSS updates for structure and data-registration transactions and each item links to an SDMX 2.1 RegistryInterface document containing SubmitStructureRequest or SubmitRegistrationRequest.
- The official “Subscribe to Changes” workflow allows notifications without an IMF SDMX Central account; it requires a valid email address and event selection. Email alerts include a ZIP containing the SDMX change document; HTTP POST sends the RegistryInterface document to a user-defined URL. UI event types include All Data Events / All Structure Events and a Refine Events control.
- This is a prospective monitoring route only, not historical recovery. Exact IMF:BR1/provider filtering in Refine Events is NOT_DONE and must not be assumed. Owner subscription activation is NOT_DONE; no email address or credentials were requested or entered.
- Operational option: owner may subscribe to All Data Events, inspect Refine Events for exact provider/dataflow filters, and locally retain/filter raw ZIP/XML for IMF:BR1, BCB URL and BOP6/BOP_BPM6. Preserve received timestamp, headers and SHA-256. This requires explicit owner action.
- Acceptance: guide semantics PASS; Re-Register updates Last Updated PASS; treating Last Updated as original creation date REJECTED; official RSS/email/POST notification mechanism PASS; no account needed for subscription PASS; exact provider filter NOT_DONE; owner subscription NOT_DONE; historical Brazil event XML/CSV NOT_DONE; chronology UNKNOWN; mismatch CONFIRMED; Brazil admission BLOCKED.
- No repeat RSS/BCB downloads, no guessed endpoints or event IDs, no fabricated chronology. ₹0 official sources only; no production changes, PR merge, Brazil/EM admission or macro weights. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 and Engines A–E unchanged; UNKNOWN is not PASS.


## 2026-11-18 — গবেষণা যাচাই অব্যাহত 36, Part-8: IMF Brazil registration event ingestion contract
- New report: `docs/IMF_BRAZIL_REGISTRATION_EVENT_INGESTION_CONTRACT_PART8_20261118.md`; commit `5d6649c5f9b8ebcf51de8b1a3f38e342005ad1ba`; verified blob SHA `bbd9103ca72fcb3568ab1aa338b71a83ff391ae4`.
- Re-opened the exact May-2025 IMF SDMX Central User Guide. §6 confirms the Registrations table's Data Provider dropdown filter and warns the provider must be configured by IMF; Register and Re-Register both update Last Updated. §7 confirms RSS item links to SDMX 2.1 RegistryInterface with SubmitStructureRequest or SubmitRegistrationRequest; email notifications include ZIP with SDMX document; HTTP POST sends RegistryInterface body. No IMF account is needed for email subscriptions, but confirmation email may be required when not authenticated with matching account email.
- Refine Events and Event Filter controls are documented, but exact filter dimensions are not enumerated. Exact IMF:BR1 filter support remains NOT_DONE; no subscription activated.
- Created a deterministic proposed ingestion contract: immutable raw evidence + SHA-256; namespace-aware XML parsing; strict SubmitRegistrationRequest vs SubmitStructureRequest classification; exact provider/BCB URL attribution; preserve BOP6 and BOP_BPM6 as distinct; event chronology must come from actual event payload, never Last Updated alone; explicit negative controls for Chile, structure-only, malformed/unknown requests, duplicates and missing timestamps.
- This is documentation/specification only, not implemented code or a tested parser. No new Brazil transaction payload was received.
- Acceptance: official guide facts PASS; proposed ingestion contract documented PASS; parser implementation NOT_DONE; exact provider subscription filter NOT_DONE; owner subscription NOT_DONE; Brazil-specific historical event XML/CSV NOT_DONE; chronology UNKNOWN; BOP6 vs BOP_BPM6 mismatch CONFIRMED; Brazil admission BLOCKED / market use NOT_AUTHORIZED.
- Next action: owner may optionally inspect official Subscribe to Changes -> All Data Events -> Refine Events for exact provider filter and/or export a historical transaction SDMX-XML/CSV. Once raw payload is supplied, implement and test the parser in a short isolated workflow with no collector trigger.
- ₹0 official sources only; no synthetic data, guessed IDs/endpoints or fabricated chronology. No production integration, PR merge, Brazil/EM admission or macro overlay weights. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E unchanged; UNKNOWN is not PASS.


## 2026-11-18 — গবেষণা যাচাই অব্যাহত 36, Part-9: IMF Brazil event parser and isolated QA workflow
- Part-8 ingestion contract reviewed before implementation. Existing 33-item RSS resolver was not rerun; no RSS/BCB acquisition or full NSE collector was triggered by the new QA workflow.
- Added offline-only parser `scripts/research/imf_brazil_event_parser.py`, commit `27f26223f46f549107e55f17c7957660a00c94c2`. It validates the RegistryInterface 2.1 root namespace, separates SubmitRegistrationRequest from SubmitStructureRequest, uses exact IMF:BR1 or exact full BCB URL matching, and emits SHA-256/evidence values. A Brazil match remains a candidate requiring manual review, never automatic PASS.
- Added seven unit tests `tests/test_imf_brazil_event_parser.py`; initial commit `fa755e5be28fd473fea0b66e4af37a91daa131ff`, then corrected malformed-XML assertion in commit `5dd500c3c061954eb2af1e4e77d1943dcd72620b`.
- Added isolated workflow `.github/workflows/imf_brazil_event_parser_qa.yml`, commit `cd15fd0aca53beb4e93b0af465c954b6ffc50006`; manual + path-scoped push, Python 3.12, read-only contents, 3-minute timeout. No network acquisition, no NSE collector.
- New report `docs/IMF_BRAZIL_REGISTRATION_EVENT_PARSER_PART9_20261118.md`; commit `068de71316f840fa281371dc414fc6d15596fa6a`; verified blob SHA `04c5030e8dd5e04d390c21434fc2bb6cacbfbcd2`.
- Acceptance: parser source committed PASS; tests committed PASS; isolated workflow committed PASS; malformed XML assertion corrected PASS; GitHub Actions execution NOT_YET_VERIFIED; real IMF Brazil fixture NOT_DONE; parser against real Brazil event NOT_DONE; chronology UNKNOWN; BOP6 vs BOP_BPM6 mismatch CONFIRMED; Brazil admission BLOCKED / market use NOT_AUTHORIZED.
- Unit fixtures are synthetic test inputs only, not market observations or evidence of Brazil registration. Parser is not a complete SDMX semantic validator; it preserves candidate values and never auto-accepts Brazil. Exact event action/time, Dataflow URN and Provision Agreement URN require real payload review.
- Next: verify the scoped GitHub Actions run; fix only failures in this isolated QA path. When owner-exported real IMF XML/CSV is available, hash and inspect it separately; do not promote Brazil before full provenance/URN checks.
- ₹0, no guessed endpoints, no fabricated timestamps, no production integration, no PR merge, no Brazil/EM admission or macro overlay weights. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E unchanged; UNKNOWN is not PASS.


### Part-9 correction — SDMX 2.1 registration request envelope and exact URL gate
- Official IMF Web Services Guide example shows `SubmitRegistrationsRequest` (plural) containing `RegistrationRequest action="Replace"`. Parser initially accepted singular only; corrected to accept documented plural plus singular compatibility form. Source: https://dsbb.imf.org/content/pdfs/IMFSDMXCentralWebServicesGuide.pdf.
- Parser commit `9004edf15e86befb841ee2c5a48761f6131b913c5` adds plural request envelope; commit `59efd1a51dac3d4390fc4530613d68c033c22cb3` tightens BCB URL match to exact whole-value only (no embedded narrative substring).
- Test commit `1669ee9cd0be3a589fb1a0539169a016cd42f537` updates fixtures to plural envelope; `d3a3b9c9936fa78d7939821096f4dc2b167cbecc` adds exact-URL negative control and action-attribute test. Test count now 9.
- Report corrected: `docs/IMF_BRAZIL_REGISTRATION_EVENT_PARSER_PART9_20261118.md`, commit `ff755717bf542ab6c4f83b45e85b8865a07fafa7`, blob SHA `a7d73193f0cfe00d8d1a98fb4f1af037e05789d3`.
- Official source confirms the request envelope syntax only; it does not prove a Brazil transaction. GitHub Actions result remains NOT_YET_VERIFIED. Real Brazil event fixture NOT_DONE; chronology UNKNOWN; mismatch CONFIRMED; Brazil admission BLOCKED. No production integration.


## 2026-11-18 — গবেষণা যাচাই অব্যাহত 36, Part-10: IMF parser QA verification
- New report: `docs/IMF_BRAZIL_REGISTRATION_EVENT_QA_VERIFICATION_PART10_20261118.md`; commit `d322b3bf33f210458daf7e72f8752d63e99e35ad`.
- Re-fetched current parser blob `a51dc69b28d244642736eca47e945bdd5b3d3459`, test blob `a75a68e170fb18eab8c7480b05cc22debc249d5f`, workflow blob `43d9f5c77c7abe4d05ffb446d2ed1c9b0a343b9b`, and Part-9 report blob `a7d73193f0cfe00d8d1a98fb4f1af037e05789d3` from default branch before validation.
- Executed the exact fetched parser + test source in an isolated local temporary directory with `python -m unittest discover -s tests -p 'test_imf_brazil_event_parser.py' -v`: **9 tests PASS, 0 FAIL**, approximately 0.002 seconds. This is local unit-test execution only; not a GitHub Actions run and not real Brazil event validation.
- Attempted connected GitHub commit-workflow-run lookup for test commit `d3a3b9c9936fa78d7939821096f4dc2b167cbecc`; returned an empty list. The connected action is explicitly PR-triggered-only and first-page-only. No general Actions run-list or dispatch action is exposed. Therefore Actions run ID/conclusion/log/artifact remain **NOT_YET_VERIFIED**; empty result is neither FAIL nor PASS.
- Workflow configuration remains scoped to parser/test/workflow paths, Python 3.12, read-only contents, 3-minute timeout. Configuration PASS; runtime NOT_YET_VERIFIED.
- Real Brazil XML/CSV NOT_DONE; chronology UNKNOWN; BOP6 vs BOP_BPM6 mismatch CONFIRMED; Brazil/EM/market admission BLOCKED. No RSS/BCB acquisition, full NSE collector, code changes, production integration, PR merge or spend.
- Next: if runtime CI evidence is needed, inspect GitHub Actions → IMF Brazil Event Parser QA (Offline) and record exact run ID/conclusion/log. Then test a genuine owner-exported transaction document only when available. UNKNOWN is not PASS; all protected production invariants remain unchanged.


## 2026-11-18 — গবেষণা যাচাই অব্যাহত 36, Part-11: Brazil Reconstruction acceptance gap matrix
- Added `docs/IMF_BRAZIL_RECONSTRUCTION_ACCEPTANCE_GAP_MATRIX_PART11_20261118.md`; commit `d7cdd1c62fd754b99ece616a21a869a2e4eacc96`.
- Reconciled the current-state registry row, BCB payload Dataflow mismatch, 33-item RSS transaction window, IMF historical GUI/API boundary, Part-9 parser and Part-10 local 9/9 QA result.
- Formal decision: **Brazil Reconstruction INCOMPLETE / BLOCKED**. Historical Brazil-specific event rows NOT_DONE; Provision Agreement URN/changelog NOT_DONE; create/replace/delete/re-register chronology UNKNOWN; event-to-current-row reconciliation BLOCKED. Parser local tests PASS 9/9; GitHub Actions runtime NOT_YET_VERIFIED; real Brazil transaction fixture NOT_DONE.
- Next closure dependency is actual official GUI-exported IMF:BR1 history rows, linked Provision Agreement details and transaction XML/CSV. If GUI requires authentication or export is unavailable, repository owner must provide the official exports. No guessed endpoints, IDs, chronology, or repeated RSS/BCB downloads.
- No production code/invariants changed; no collector run, PR merge, Brazil/EM admission or spend. UNKNOWN is not PASS.


## 2026-11-18 — গবেষণা যাচাই অব্যাহত 36, Part-12: SDMX 2.1 schema boundary and Brazil evidence handoff
- Added `docs/IMF_BRAZIL_RECONSTRUCTION_SCHEMA_BOUNDARY_PART12_20261118.md`; commit `3fecf9eb82f28e97bff4d7e1b967b9695b627434`.
- Official SDMX XML Schemas index confirms the SDMX 2.1 schema set includes registry XSDs (`SDMXRegistry.xsd`, `SDMXRegistryBase.xsd`, `SDMXRegistryRegistration.xsd`). Linked XSD retrieval returned an unsupported XML content-type error in the browser; XSD body was not inspected or locally validated. This is schema-index discovery only.
- Re-fetched parser/test default-branch blobs `a51dc69b28d244642736eca47e945bdd5b3d3459` / `a75a68e170fb18eab8c7480b05cc22debc249d5f`. Parser is a conservative envelope/evidence candidate parser, not a full SDMX XSD or semantic validator. Part-10 local fixture tests remain 9/9 PASS only; no actual Brazil transaction tested and GitHub Actions runtime NOT_YET_VERIFIED.
- No code change made: actual Brazil transaction payload and inspected XSD semantics are prerequisites to avoid speculative parser changes.
- Exact closure dependency remains owner-exported IMF:BR1 historical registration rows, linked Provision Agreement URN/changelog, and original transaction SDMX-XML/CSV with source URL/retrieval time/raw bytes/SHA-256. No credentials requested.
- Acceptance: official schema index PASS; XSD body/local validation NOT_DONE; historical Brazil rows NOT_DONE; PA URN/changelog NOT_DONE; chronology UNKNOWN; event reconciliation BLOCKED; Brazil/EM admission BLOCKED / NOT_AUTHORIZED.
- No repeated RSS/BCB fetch, no guessed endpoint/ID, no fabricated chronology, no synthetic data, no production integration/PR merge/macro weighting/trading admission. ₹0 official/free only. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E unchanged; UNKNOWN is not PASS.


## 2026-11-18 — গবেষণা যাচাই অব্যাহত 36, Part-13: IMF Brazil Provision Agreement evidence reconciliation
- User Library archive `imf_pa_research(1).zip` inspected. ZIP size 5,628,154 bytes; SHA-256 `8cb2ed4bd96c0b1c4d3f24d0530771a5868f55bba256213404d5acf22a3f2b45`; manifest SHA-256 `0954644ea442a76e380cfc3e8ee2d95503fd9b05da088c853f17fd4c320aa903`.
- Three manifest HTTP 200 responses and raw XML hashes: legacy all `75b7a55f5daafb0ce566593542f76874f202eeae6b4f09cb572f5372ef44be85` (53,443,157 bytes); v2 IMF all `9c8e9c9157da0e3ce33ca23db5afbc25e2517e02f481c8688d3ad0ed7f13ff0e` (52,420,642 bytes); v2 all agencies `85b951126342dc1e5be7b104e676b519b1e9d1a857fa78a4d91b2a3e35637453` (592,196 bytes). All Content-Type values were `application/xml;charset=UTF-8`, including URLs requested with `format=fusion-json`; parsed as XML according to actual content type.
- Target PA found identically in all 3 XML responses: URN `urn:sdmx:org.sdmx.infomodel.registry.ProvisionAgreement=IMF:BR_BOP_BP6(1.0)`; Name “Brazil Balance of Payments”; Agency IMF; ID BR_BOP_BP6; Version 1.0; explicit StructureUsage/Dataflow Ref IMF:BOP6(1.0); explicit DataProvider Ref IMF:DATA_PROVIDERS(1.0).BR1. Thus Brazil PA identity and PA->provider/dataflow references are now CONFIRMED.
- Legacy response has 1,003 PAs, v2 IMF 992, v2 all agencies 1,004. Legacy and v2 IMF each expose 27 PAs linked to provider IMF:BR1. The 27-item inventory is in Part-13. Do not interpret PA ID suffix BP6 in place of explicit Dataflow Ref.
- This resolves the previously missing current PA URN/reference evidence. It does NOT supply PA changelog/revision chronology, BCB URL link, registration event rows, or create/replace/delete/re-register timestamps. The PA confirms registry/PA BOP6 identity, but BCB payload still declares BOP_BPM6; mismatch remains confirmed and unresolved.
- New report `docs/IMF_BRAZIL_PROVISION_AGREEMENT_RECONCILIATION_PART13_20261118.md`; commit `3c0f7b95616ff8a9d511b3e3cfac667446c891e5`.
- Acceptance: PA URN PASS; PA->BR1 PASS; PA->BOP6 PASS; cross-response presence 3/3 PASS; 27 BR1 PA inventory PASS; PA changelog NOT_DONE; PA-to-BCB URL NOT_ESTABLISHED; actual registration event rows NOT_DONE; chronology UNKNOWN; event-to-current-row PARTIAL/BLOCKED; BOP6 vs BOP_BPM6 mismatch BLOCKED; Brazil/EM admission BLOCKED / NOT_AUTHORIZED.
- Per-response HTTP retrieval timestamps are not included in manifest; do not invent them or substitute Library upload timestamp. No synthetic data, guessed IDs, undocumented endpoints, fabricated chronology. ₹0 official/free only. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E unchanged; no production integration/PR merge/macro weights/trading admission; UNKNOWN is not PASS.


## 2026-11-18 — গবেষণা যাচাই অব্যাহত 36, Part-14: IMF Brazil public GUI cross-check
- New report: `docs/IMF_BRAZIL_PUBLIC_GUI_CROSSCHECK_PART14_20261118.md`; report commit `ad5212d6044344739b398c4ecc8fd1be32941666`.
- Re-inspected official IMF Provision Agreements page. The page exposes References, Changelog, Export SDMX-ML 3.0, Export Excel, Compare, View Provision Agreement and detail fields URN/URL/Revisions/Valid From/Valid To. Static extraction did not select the Brazil PA or expose its populated revision/changelog values; actual Brazil PA history remains NOT_OBSERVED, not empty and not proven inaccessible.
- Re-inspected official IMF Registrations page. Its current public rendering independently lists IMF:BOP6(1.0), provider IMF:BR1, the exact BCB URL, and Last Updated 2026-10-26T11:47:29.000Z. This corroborates the current-state tuple only; it does not prove original registration time, transaction ID/action, or PA chronology.
- Current registration tuple cross-check: PASS. PA page UI affordances: PASS. Selected Brazil PA changelog/revisions content: NOT_OBSERVED. Brazil historical event XML/CSV: NOT_DONE. Create/Replace/Delete/Re-Register chronology: UNKNOWN. PA-to-BCB URL relation: NOT_ESTABLISHED. BOP6 vs BOP_BPM6 mismatch: CONFIRMED / UNRESOLVED. Brazil/EM admission: BLOCKED / NOT_AUTHORIZED.
- Exact next dependency: owner-side interactive selection of URN IMF:BR_BOP_BP6(1.0), export/capture Revisions/Changelog/Compare/View details, and export the IMF:BR1 dated registration transaction SDMX-XML/CSV with raw bytes, source URL, retrieval timestamp and SHA-256. No credentials requested.
- No undocumented endpoints, repeated RSS/BCB downloads, parser changes, workflow runs, full NSE collector, production integration, PR merge, macro weights, trading admission or spend. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56 x 12), Engines A-E unchanged; UNKNOWN is not PASS.


## 2026-11-18 — গবেষণা যাচাই অব্যাহত 36, Part-15: IMF Brazil SDMX 2.1 schema and timestamp semantics audit
- New report: `docs/IMF_BRAZIL_SDMX21_SCHEMA_AND_TIMESTAMP_SEMANTICS_AUDIT_PART15_20261118.md`; report commit `fb55f75cd2cdebc5af594f779ebf1399a55ffb63`.
- Official SDMX schema catalogue lists the SDMX 2.1 registry XSD set (SDMXMessage, SDMXRegistry, SDMXRegistryBase, SDMXRegistryRegistration, etc.). Direct raw official XSD retrieval failed in this session; no official raw-byte SHA or local XSD validation is claimed.
- Inspected a pinned third-party SDMX 2.1 XSD mirror at commit `d66144444d27c5b66361fb508d795a87072821ac`; its blob SHAs and provenance limitation are recorded in Part-15. This is mirror-only evidence, not yet hash-equated to official xml.sdmx.org bytes.
- Mirror-derived schema shape: RegistryInterface -> SubmitRegistrationsRequest -> RegistrationRequest (required action) -> Registration -> ProvisionAgreement + Datasource; datasource contains SimpleDataSource and/or QueryableDataSource. The mirror's ActionType enum is Append, Replace, Delete, Information. Current parser action candidates are misaligned (currently accepts register/reregister/re-register; omits Append/Information). Do not infer these enum values map directly to initial-create or re-register.
- Important timestamp clarification: the inspected XSD describes Registration/@lastUpdated as the last time the data source was updated; IMF Web Services Guide separately says re-registering an existing registration updates the Last Updated timestamp. Therefore Last Updated cannot be used as the registry transaction timestamp or original registration date.
- Parser gap: it scans arbitrary descendants rather than requiring the schema-shaped RegistrationRequest/Registration/ProvisionAgreement/Datasource path; it can also mistake arbitrary BOP6-like strings for Dataflow evidence. No parser patch was made because official raw XSD bytes and a real Brazil event fixture are still absent.
- Acceptance: official schema catalogue discovery PASS; IMF guide semantics PASS; pinned third-party schema mirror inspection PASS (mirror-only); official raw XSD hash archive NOT_DONE; XSD fixture validation NOT_DONE; parser correction NOT_DONE; real Brazil event fixture NOT_DONE; chronology UNKNOWN; BOP6 vs BOP_BPM6 mismatch CONFIRMED/UNRESOLVED; Brazil/EM admission BLOCKED.
- Next highest-value task: obtain official raw 2.1 XSD bytes and hash them; then build offline schema-validation tests for parser fixtures and patch parser structure/action handling only against verified official schema plus a genuine owner-exported Brazil transaction. No credentials needed.
- No code/tests/workflow/collector/production changes, no PR merge, no repeated RSS/BCB download, no macro weights, no trading admission, no spend. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56 x 12), Engines A-E unchanged; UNKNOWN is not PASS.


## 2026-11-19 — Brazil Registration URN lifecycle capture (supersedes Part-11/Part-14/Part-15 historical-row status)
- New report: `docs/IMF_BRAZIL_REGISTRATION_HISTORY_PART7_20261119.md`; commit `cb2576201e5e5eab3c2faa0743607c64d150fa6a`.
- Exact Registration URN found: `urn:sdmx:org.sdmx.infomodel.registry.Registration=IMF:D429E36CD161E2F2A34ECAF137994E89(1.0)`; Registration ID `D429E36CD161E2F2A34ECAF137994E89`; PA `IMF:BR_BOP_BP6(1.0)`; provider `IMF:BR1`; exact BCB URL recorded in Part-7.
- Original transaction ID 667: Registry history Date 2023-09-22T09:42:16.389Z; Registry Action Replace; Type Registration; embedded SDMX `SubmitRegistrationsRequest` has `RegistrationRequest action="Information"`; Registration.lastUpdated 2023-09-22T09:42:05. Preserve these three fields separately; no semantics inferred.
- Exact Registration URN history returns 40 events from tx667 / 2023-09-22T09:42:16.389Z through tx37877 / 2026-10-26T11:47:33.098Z. All 40 transaction-item ZIPs HTTP 200; all 40 embedded SDMX-ML 2.1 XML parse PASS; Registration ID/PA/BCB URL match 40/40.
- Global transaction index returned 38,668 records (IDs 1–38,668). Cross-check: all 40 event IDs found, all 40 millisecond timestamps and Registry Action values exactly match. Type field is populated as Registration for tx667 only; absent in the other 39 rows and remains missing/UNKNOWN.
- Artifact run 44465947951 / artifact 14502380926 / ZIP SHA-256 `2a3266a0c2d3e1948955e9de789c2a3f9acb5ecd12ffca42cd54bbad0bb37f41`; global index reconciliation run 44466324080 / artifact 14501663276 / ZIP SHA-256 `3b968f502447b870b1220bafda7ffdf1071f6cfdda9410631c5ec4d3b71f8b33`.
- Durable GitHub data: `docs/evidence/IMF_BRAZIL_REGISTRATION_HISTORY_40_EVENTS.csv` commit `0b490a8373de2f8be2a443bfdd5d150d5f6ef424`; original tx667 XML `docs/evidence/IMF_BRAZIL_REGISTRATION_TX_00667.xml` commit `b47e74956b899c1ef2402779d61d6dd6c0b1ede3`.
- This closes historical events for this exact Registration URN. It does NOT close PA structure transaction ID 2/changelog; tested tx2 item routes returned HTTP 400 and full transaction route HTTP 500. PA history itself reports tx2.
- Current BOP6 and BOP_BPM6 Dataflow structures were independently retrieved and both reference ECOFIN_DSD(1.0), while their Dataflow URNs/names remain distinct. Prior 237-series constraint audit remains authoritative: BOP6 accepts 234/237, BOP_BPM6 accepts 27/237. Mismatch remains confirmed; no header rewrite, alias assumption or admission.
- Real Brazil registration XML fixture is now available; Part-15's prior `real Brazil event fixture NOT_DONE` status is superseded for this one exact registration fixture. Existing generic parser remains unmodified and still requires official raw XSD validation plus tests against this real fixture; its parser implementation is not automatically PASS.
- GCR: Treasury nominal+real history capture run 44376975144 / artifact 14462186283 independently validated (9,226 nominal + 5,973 real observations, raw-page hashes, exact raw-to-CSV values, zero duplicate dates). Reusable validator committed at `scripts/research/validate_treasury_yield_artifact.py`, commit `f98449bc9f893521a2e9c971950a9933d9f1449f`.
- GCR IMF BOP observation API access boundary documented: BOP dataset API link redirects to IMF API Management sign-in; IMF API docs say SDMX 2.1/3.0 and Swagger beta sign-in. No anonymous observation query route verified. Report `docs/GCR_IMF_BOP_OBSERVATION_ACCESS_BOUNDARY_20261119.md`, commit `b40658bc9cf6fad908fbaa297beed69d03d7ef27`.
- Updated master evidence checkpoint: `docs/INDEPENDENT_EVIDENCE_CLOSURE_CHECKPOINT_20261119.md`, latest commit `f98ab611f01934b5b566b677d46a5ac3c81f230c`.
- Current decision: Brazil exact Registration URN lifecycle PASS; Brazil PA structure history BLOCKED; BOP6/BOP_BPM6 mismatch BLOCKED; GCR Treasury capture PASS; GCR IMF BOP observations BLOCKED; full GCR factors/formula/sector transmission/backtest NOT_DONE. Overall workstreams remain INCOMPLETE / BLOCKED. No production selector/ranking/pressure fade/CORE-672/Engines A–E changes; no paid API; no synthetic observations; UNKNOWN is not PASS.


## 2026-11-19 — IMF BOP public observation route closed for a validated BRA/IND pilot (GCR)
- Previous assumption “IMF BOP observations blocked because API sign-in” is superseded: IMF API page says SDMX 2.1/3.0 data APIs are supported and Swagger requires beta portal sign-in; direct public SDMX 3.0 metadata and data endpoints were independently tested without API key or cookies and returned HTTP 200 with actual observations. Official dataset BOP page states annual/quarterly frequency.
- Exact metadata: Dataflow IMF.STA:BOP(21.0.0); DSD IMF.STA:DSD_BOP(24.0.0), SHA-256 `1541c0e65af5801acb86767a183a124537aa4b6a04d2a4e528c23d73d4b2019b`; dimension order COUNTRY.BOP_ACCOUNTING_ENTRY.INDICATOR.UNIT.FREQUENCY.
- Codelists independently captured: CL_BOP_COUNTRY(1.0.0), CL_BOP_ACCOUNTING_ENTRY(3.3.0), CL_BOP_INDICATOR(10.0.0), CL_UNIT(2.13.0), CL_FREQ(1.2.0).
- Selected populated indicator `P_F` (“Portfolio investment, Total financial assets/liabilities”); entries `A_NFA_T` (“Assets, Net acquisition of financial assets”) and `L_NIL_T` (“Liabilities, Net incurrence of liabilities”); USD; Quarterly. `P_MV` test returned 200 but empty rows; rejected from extraction.
- Final run 44472944620, artifact 14504732476, artifact SHA-256 `2e00a175837e1ad5e98346b114c4ec5a9d55ddf38833938711e9a3106a331d6c`. 4/4 exact HTTP 200 and CSV parse; 186 rows; 186 unique keys; 0 duplicates; 186/186 exact-vs-broad raw values match; 186/186 raw-to-normalized attributes match; zero missing/mismatched values; contiguous quarter sequence per series.
- BRA assets and liabilities: 47 each, 2015-Q1–2026-Q3. IND assets and liabilities: 46 each, 2015-Q1–2026-Q2. India 2026-Q3 is missing and remains missing. No forward fill or synthetic observations.
- All 32 source columns retained. SCALE=6, PRECISION=6 kept as source metadata; no conversion. No BOP assets/liabilities netting or sign reinterpretation.
- Durable compressed evidence committed in docs/evidence: normalized pilot panel plus four exact raw CSVs as .csv.gz. Their Git blob SHAs are listed in docs/INDEPENDENT_EVIDENCE_CLOSURE_CHECKPOINT_20261119.md. Full report: `docs/GCR_IMF_BOP_PUBLIC_OBSERVATION_ACCESS_PART1_20261119.md`; machine summary: `docs/evidence/IMF_BOP_PORTFOLIO_PILOT_BRA_IND_2015Q1_2026Q3.json`.
- Status update: GCR IMF BOP metadata route PASS; public observations route PASS; BRA/IND pilot capture PASS; independent raw/broad/normalized reconciliation PASS. Full GCR factor closure remains NOT_DONE because this is not a defined EM universe or full country panel.
- Outstanding blockers: resolve SCALE semantics; define/version EM country membership; assess BOP_AGG annual aggregate separately (official IMF says non-reporting economy estimates may be used); extend exact series coverage; reconcile vintages/revisions; preserve distinction from daily SEBI FPI/FII and IIP/CPIS positions.
- No production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A–E changes; no trading admission. ₹0 spend; no synthetic rows; UNKNOWN is not PASS.


## 2026-11-19 — Next-priority GCR IMF BOP public-route investigation
- Official BOP dataset page inspection confirms static controls API / VIEW DATA / DOWNLOAD and annual + quarterly frequency. Static extraction does not expose a direct View Data or Download URL, so actual data export remains NOT_RESOLVED. Do not mark observations PASS merely because the controls appear.
- Identified official separate BOPSY World and Country Group Aggregates dataset `IMF.STA:BOP_AGG`, annual frequency, with November 2026 dashboard and Explanatory Notes releases.
- BOPSY source composition caveat verified on IMF page: country-level records are actual IMF-reported or sourced from NSDP (IMF-counterparty exceptions can use Fund Accounts); World/area aggregates other than Euro Area combine reported data and estimates for nonreporting economies sourced in part from WEO/EWN; Euro Area is ECB reported. Therefore BOPSY group aggregates cannot be treated as a pure sum of reported EM country observations, and annual BOPSY cannot replace quarterly country-level financial-account flows.
- BOPSY 2026 notes DOCX link was identified but not downloaded or validated; no numeric BOPSY data captured. BOPSY is only ELIGIBLE_FOR_SEPARATE_VALIDATION as an annual macro benchmark, not a completed data panel.
- New report `docs/GCR_IMF_BOP_PUBLIC_RELEASE_DISCOVERY_20261119.md`, commit `f6d6aae08a6f0bdafcf4b0c92c30519e4f1fb874`.
- Updated evidence checkpoint commit `614499b114f229c69cb9e6ce69f19a057ada7631`.
- IMF BOP observations remain BLOCKED pending actual public export route or verified user-provided official export. Do not use guessed API URLs/keys, no credentials/cookies, no CPIS/PIP position substitution, no synthetic observations. Existing hard invariants unchanged.


## 2026-11-19 — GCR Part-1: IMF BOP public observation endpoint opened; exact BRA/IND panel PASS
- Critical correction to prior access assumption: IMF API Swagger explorer requires beta portal sign-in, but the public SDMX 3.0 data endpoint `https://api.imf.org/external/sdmx/3.0/data/dataflow/IMF.STA/BOP/21.0.0/{key}` returned public CSV observations without credentials/cookies. Do not conflate Swagger sign-in with endpoint access.
- Workflow run 44472944620 completed SUCCESS; artifact 14504732476, 7,784,894 bytes, ZIP SHA-256 `2e00a175837e1ad5e98346b114c4ec5a9d55ddf38833938711e9a3106a331d6c`.
- Official Dataflow `IMF.STA:BOP(21.0.0)` and DSD `IMF.STA:DSD_BOP(24.0.0)` structures returned HTTP 200; DSD has dimensions COUNTRY, BOP_ACCOUNTING_ENTRY, INDICATOR, UNIT, FREQUENCY and TIME_PERIOD. Seven exact codelist/concept scheme retrievals all HTTP 200 / XML parse PASS.
- Exact flow panel uses `P_F` (Portfolio investment, Total financial assets/liabilities), accounting entries `A_NFA_T` (Assets, Net acquisition of financial assets) and `L_NIL_T` (Liabilities, Net incurrence of liabilities), unit USD, frequency Q.
- Four exact CSV requests (BRA/IND × asset/liability) returned HTTP 200 and CSV parse PASS. Brazil 47 obs per entry, 2015-Q1..2026-Q3; India 46 obs per entry, 2015-Q1..2026-Q2. Total 186 rows, 186 unique keys, 0 duplicates, no forward fill/synthetic rows/rescaling/currency conversion.
- Independent validator: 186/186 exact-vs-broad raw values match; 186/186 raw-to-normalized attributes match; zero missing/mismatches; each series' quarter sequence contiguous; status PASS. Normalized panel SHA-256 `8ef39ecdefc4dd042d6e7a74e84aaf95aa9c66162de36164667d2bc6ad74e778`.
- Exact CSV SHA-256s: BRA/A_NFA_T `3feca530a6495a3877370ad21bbacece69de87f3ebb725af4cbc455e1f84183c`; BRA/L_NIL_T `2d6b4a22740fe4df16ab4b84e71f69fd6d2833e12c32d94fa0db7bee2925a254`; IND/A_NFA_T `c86388af35f1b83b0b9d2a451d35c3c78541ea03af1d9a9c826a12bb34f04a82`; IND/L_NIL_T `25d41406425a78d575273a7b3fc63cfb3ecc05cda3789c25787b5a610b5c138d`.
- Initial `P_MV` (Portfolio investment, Market value) exact query returned 4× HTTP 200 CSV but 0 nonempty observations. It is recorded as EMPTY/REJECTED for these BOP flow keys; not a positive access result. The diagnostic script was updated to label zero-observation series explicitly (commit `153898be869c2c36faf37d316ca6ece8f8e65f25`).
- Official SDMx Global Registry BOP DSD V2.6.0 captured separately in both SDMX 2.1 and 3.0. Run 44473409770, artifact 14505177819, 237,674 bytes, ZIP SHA-256 `ba2ce640bb3a4c1cf614341103facec5b9b9aea820100fe7e28a3447993576fe`. SDMX 2.1 raw XML SHA-256 `642fa30fa3ee76be08bf2cdcebdef452e38a421355dd3516fe4666d9cce7b122`; SDMX 3.0 raw XML SHA-256 `5296c0fa950d19dea53a5a477a98915bcb14b1cecb673fbac9a0dcc87ebb11a2`; both parse PASS. Archive includes 23 codelists, 1 concept scheme, 3 dataflows.
- Important: Global Registry `IMF:BOP(2.6.0)` DSD (17 dimensions + time) is not assumed identical to IMF Data Portal `IMF.STA:DSD_BOP(24.0.0)` (5 dimensions + time) for `IMF.STA:BOP(21.0.0)`. No silent crosswalk. The older 2013 IMF BOP pilot regional XML files (75 series/country) are stale and rejected.
- Semantics: source `P_F` is portfolio investment financial assets/liabilities; asset and liability entries kept separate. Do not calculate net inflow yet. `SCALE=6` preserved without interpretation or rescaling; separate BOP 2.6.0 uses `UNIT_MULT`. No concept crosswalk has been proven.
- New report: `docs/GCR_IMF_BOP_PUBLIC_OBSERVATION_ACCESS_AND_PILOT_PART1_20261119.md`, commit `b719b0a7cb937be75a2eb198631a29471bc76abd`.
- Current status: IMF BOP public observation route PASS; BRA/IND exact quarterly flow pilot PASS; WEO EMDE membership mapping NOT_DONE; full EMDE panel/aggregate NOT_DONE; scale/unit/sign semantics validation PARTIAL; GCR formula, sector bridge and rolling backtest NOT_DONE. No production changes, no macro weights or trading admission.
- Next: capture official October 2026 WEO Entire Dataset workbook and extract the exact 154 EMDE membership edition; map each member to IMF BOP COUNTRY codes with unmapped/ambiguous records. Then extend the same exact `P_F` asset/liability panel and produce coverage matrix; do not aggregate until unit multiplier, signs, vintages and country membership are validated.


## 2026-11-19 — WEO October 2026 EMDE membership + IMF BOP code crosswalk PASS
- Official WEO October 2026 Entire Dataset workbook acquired directly from IMF: HTTP 200; 5,480,592 bytes; SHA-256 `2aa4f70a05931197b41ed7e0202dc56eee8d816858ac14521e4f8f5dbc38696c`.
- Exact authority is workbook sheet `Country Group Composition`, group code `G200`, group name `Emerging Market and Developing Economies`; 154 rows, 154 unique three-letter country codes, no duplicate members.
- Official October 2026 WEO Appendix also acquired HTTP 200; 985,701 bytes; SHA-256 `cd4e2829d7e621d43134728bfc128547f776e909e08ef1d38b837e2d39e5ae2a`.
- IMF BOP codelist `IMF.STA:CL_BOP_COUNTRY(1.0.0)` acquired HTTP 200; 345 codes; raw XML 204,795 bytes; SHA-256 `54647ef3ac6439ecd059fd80a7954c35e447415d53bf41fbee02728e7cfb6bcb`.
- Exact code-ID crosswalk: 154/154 exact matches; 0 unmapped; 0 duplicate WEO codes. No fuzzy name matching or guessed aliases.
- Nauru (NRU) is the only normalized display-name mismatch: WEO label `Nauru, Republic of`, BOP codelist includes `Naoero, Republic of` and `Nauru` among localized names; code NRU matches exactly. Preserve label discrepancy as metadata, not a failed code mapping.
- Run 44474502699 SUCCESS; artifact 14505617102; 6,204,691 bytes; ZIP SHA-256 `3246d18f7ef6a1d74c2a08ddc37a94542fc0d42c14acf14470e0a8d7bb2783bb`; retained until 2027-02-17.
- Durable GitHub files:
  - `docs/evidence/WEO_OCT2026_EMDE_G200_BOP_CODES_154.csv`, commit `a343a0a92840a2dab01e8bdbcaf236b9fe38fd21`.
  - `docs/evidence/WEO_OCT2026_EMDE_G200_CROSSWALK_SUMMARY.json`, commit `d8fdea10445a7b98e987248cf8d5fa37946d3112`.
  - Report `docs/GCR_WEO_OCT2026_EMDE_MEMBERSHIP_CROSSWALK_PART1_20261119.md`, commit `488693924be34c8d8a6bf8a81f5149a6ed2a99ad`.
- Interpretation: this is a WEO October 2026 vintage membership edition; exact code mapping does NOT mean quarterly BOP observations exist for all 154 members. No aggregate is authorized.
- Next: query exact IMF BOP keys for 154 × 2 accounting entries (`A_NFA_T`, `L_NIL_T`) using `P_F`, USD, Q; produce a country/entry/quarter coverage matrix with raw provenance, preserve empty series and missing quarters; resolve SCALE/sign semantics before summing.
- No production selector/ranking/pressure-fade/CORE-672/Engines A–E changes; no synthetic data; UNKNOWN is not PASS.


## 2026-11-19 — GCR Part-2: 154-member WEO EMDE portfolio flow panel captured and sample-validated
- Official IMF WEO October 2026 entire workbook downloaded anonymously (HTTP 200), SHA-256 `2aa4f70a05931197b41ed7e0202dc56eee8d816858ac14521e4f8f5dbc38696c`, 5,480,592 bytes.
- Extracted exact group `G200` / Emerging Market and Developing Economies from `Country Group Composition`: 154 unique country ISO3 codes.
- Official IMF BOP `CL_BOP_COUNTRY(1.0.0)` XML captured HTTP 200, 5,737,234 bytes, SHA-256 `190c0ab3196a85bba890e2fd0cf40eebda654de2eb8e7d1f16c9644572d59f39`; 154/154 WEO EMDE codes matched, missing codes 0.
- Dataflow `IMF.STA:BOP(21.0.0)`, DSD `IMF.STA:DSD_BOP(24.0.0)`, indicator `P_F`, asset entry `A_NFA_T`, liability entry `L_NIL_T`, quarterly, 2015-Q1..2026-Q3, all unit keys. Both multi-country public SDMX 3.0 GET requests returned HTTP 200 CSV.
- Run 44474218174, artifact 14505862034; ZIP 5,997,777 bytes; SHA-256 `1a1a184f3689e04ff75d4433b44904083a33e18bdc70f096c3e9919900ebeb4f`.
- Raw assets CSV: 484,139 bytes, SHA-256 `677054017f5d3ae5fdd0403d7341588ebf43ad8b54124ae1b616bf323229326e`, 4,681 nonempty obs, 45 empty rows, 113 countries.
- Raw liabilities CSV: 451,290 bytes, SHA-256 `713b7a3000712e2ffb07cd574d08d7e6f3c02a6b2573ce4b40d06e0458cd7bba`, 4,618 nonempty obs, 43 empty rows, 112 countries.
- Combined normalized panel: 9,299 observations, 9,299 unique keys, 0 duplicates, 114 countries with any data. 225/308 country-entry pairs have observations (73.05%). Both legs exist for 111 countries; 40 have neither; DZA and ETH are assets-only; ZWE is liabilities-only. 43 members lack at least one leg. Per-country coverage periods vary; most series end 2026-Q2, only two end 2026-Q3. No fill, no zero substitution, no synthetic observations, no conversion/rescaling.
- Exact sample validation run 44474458684, artifact 14505009889, ZIP SHA-256 `588101c0deff3b4310984dae5eabcac64fc8288f4416854b7676b4b6ff6b4cd7`: 12 countries (ARG/BGD/BRA/CHN/IDN/IND/MEX/NGA/POL/SAU/TUR/ZAF) × 2 entries = 24 exact-key GETs; HTTP 200 24/24; exact series PASS 24/24; 1,106/1,106 exact observation values and all source attributes match broad multi-country raw panel; no missing or mismatches.
- Durable archive persisted to `docs/evidence/imf_bop_emde_20261119/`; persistence run 44474596292 SUCCESS; archive commit `a6eb5865c0a77d6bdaf1c6a3c6925e6e1e69bdf0`.
- Detailed report: `docs/GCR_IMF_BOP_EMDE_PANEL_PART2_20261119.md`, commit `487f7ca6758a105dfe1280e5af8ed5b7b3a0369d`.
- Critical decision: do NOT aggregate 154 EMDE countries yet. Only 111/154 have both assets and liabilities; 40 have neither; 3 are one-sided. Country period coverage is asynchronous. USD is the only returned unit for this query; SCALE=6 retained, not interpreted. Net inflow/aggregation remains BLOCKED until exact SCALE/sign semantics and coverage threshold are accepted.
- Current GCR status: public IMF BOP observations PASS; 154-member membership mapping PASS; 9,299-row panel acquisition PASS; 12-country exact sample validation PASS; full group aggregate BLOCKED/NOT_AUTHORIZED; relative-attraction formula, sector transmission and rolling backtest NOT_DONE.
- No Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A–E changed; no paid APIs; no credentials; no synthetic data; UNKNOWN is not PASS.


### 2026-11-19 — Scale concept and raw-source archive addendum
- Dedicated SCALE concept probe run 44474593356 / artifact 14505692823 / ZIP SHA-256 `218bb0f75f725e44beb2250b06075ddd8796b0a0dff5bd442a5fd57ddeae519b`.
- Exact `IMF:CS_MASTER_SYSTEM(1.0.2)` `SCALE` concept resolves to `IMF:CL_UNIT_MULT(1.0+.0)`; latest public codelist `CL_UNIT_MULT(1.0.2)`; code 6 label = Millions (10^6). This resolves the label, not the application to the raw numeric values. Preserve raw `OBS_VALUE` and `SCALE=6`; do not multiply/divide or rescale until IMF portal display and national-source reconciliation is complete.
- Raw source files persisted to GitHub: WEO October-2026 workbook and IMF BOP country codelist XML; commit `79bfbeb3abd2a0e223ae77d2ed740727404dd112`.
- Detailed report updated with scale semantics and archive receipt: `docs/GCR_IMF_BOP_EMDE_PANEL_PART2_20261119.md`, commit `742e9f4e3c93ca596a93ce92dc965dc8cc0167f0`.
- Master evidence checkpoint update: `docs/INDEPENDENT_EVIDENCE_CLOSURE_CHECKPOINT_20261119.md`, commit `2293e48d54591b0c85eb06a9009dd264b4e79015`.
- Public BOP observation access is no longer blocked; raw 154-member panel PASS; coverage remains PARTIAL; scale conversion BLOCKED; BPM/revision-vintage controls NOT_DONE; EMDE aggregate NOT_AUTHORIZED.


## 2026-11-19 — GCR India scale/sign empirical validation (4 quarterly periods)
- RBI official Table 197 (BPM6 quarterly, US$ million, 31 July 2026) independently benchmarked against IMF Data Portal BOP quarterly `P_F` entries `A_NFA_T` and `L_NIL_T`.
- 2024-Q2, 2024-Q3, 2024-Q4, 2025-Q1: eight comparisons all match within RBI integer-million rounding (max absolute difference 0.490 USD million).
- For these tested India API payloads, `OBS_VALUE / 1,000,000` matches RBI US$ million values; do not multiply raw API values by 1e6 again. `A_NFA_T) is sign-reversed against RBI Portfolio Investment by India net; `L_NIL_T) matches Portfolio Investment in India net. This is empirically PASS for India only, not a global rule.
- Detailed evidence: `docs/GCR_IMF_BOP_SCALE_RECONCILIATION_INDIA_PART1_20261119.md`; machine CSV `docs/evidence/IMF_BOP_IND_SCALE_RECONCILIATION_2024Q2_2025Q1.csv`.
- Global scale transform remains PARTIAL; Brazil and at least two additional national benchmarks still required. Existing BCB SGS reconciliation's 201/381 mismatches since 2010-01 means Brazil remains BLOCKED, not PASS. Do not aggregate the 154-country panel yet.
- Latest evidence checkpoint: `docs/INDEPENDENT_EVIDENCE_CLOSURE_CHECKPOINT_20261119.md`, commit `6cfd076b2aa26532dac19398d02cfd045acc14d3`.

## 2026-11-19 — Independent WEO Appendix validation, full EMDE missingness QA and SCALE metadata (current)
- WEO Oct-2026 Appendix top-level EMDE list parsed as 154 unique labels; same-vintage workbook G200 has 154 unique ISO3; Appendix-to-workbook identity mapping 154/154 PASS; 0 unmapped/ambiguous; all 154 ISO3 present in BOP CL_BOP_COUNTRY.
- WEO membership run 44474629873 / artifact 14506160317 / ZIP SHA-256 acdf014f5f19ba5e0d23dca7a8d57a4b1813b002a3274495d557f0cd05c0fbb1. Durable raw Appendix PDF, workbook, BOP codelist, membership CSV, crosswalk and summary persisted under docs/evidence/imf_bop_emde_20261119/weo_membership_validation/.
- Full EMDE panel run 44474620936 / artifact 14505452613 / ZIP SHA-256 b23854fa433b46b29bb2d8094ec9bc14d2cd6c58fdc1771fa9428ca6ae3aed17; 154 membership rows; 2 raw quarterly CSVs; 9,299 normalized observations; 9,299 unique keys; 0 duplicates.
- Independent raw-to-normalized coverage QA run 44475089564 / artifact 14505623598 / ZIP SHA-256 5f24a529aa0d3c918d598faedeb057c39e328ff043f1f1a86fec587fc1fa8cd8: 9,299/9,299 exact row matches; 30 source attribute columns; 278,970 cell comparisons; 0 mismatches.
- Coverage: 225/308 country-entry pairs with observations (73.05%); 83 empty; 111 countries both legs; DZA and ETH assets-only; ZWE liabilities-only; 40/154 no data; 43/154 lack at least one leg. 4 complete 47-quarter series, 221 partial, 13 series with internal gaps (71 missing quarters). Only Brazil and Pakistan have both legs through 2026-Q3. No fill/zero substitution/synthetic rows/rescaling/FX conversion/aggregation.
- Detailed coverage QA report: docs/GCR_IMF_BOP_EMDE_COVERAGE_QA_PART3_20261119.md; full tables at docs/evidence/imf_bop_emde_20261119/coverage_qa/.
- SCALE semantics capture run 44475051442 / artifact 14505852262 / ZIP SHA-256 391981ce19d89d8ccc6377580e33345a9d75adffdc3f4197c4e4c743a66e3cf3: DSD_BOP SCALE points to CS_MASTER_SYSTEM SCALE, enumerated by CL_UNIT_MULT; code 6 = Millions (10^6). Metadata code meaning PASS; numeric transformation BLOCKED because CSV response may already be normalized and a blind ×10^6 would be implausible. Preserve raw values and SCALE unchanged pending portal/national-source reconciliation.
- Durable report docs/GCR_IMF_BOP_SCALE_SEMANTICS_20261119.md; detailed Part-2 report updated; coverage QA and WEO source files persisted to main.
- Latest main persistence commit from successful archive workflow: 13bdd96d; coverage and scale reports committed as c57913487aa3915da0a88c2622a1ab42b649e059 and 3cd7c4b0eb7de639750ee030cccb1eb50ee8108f; Part-2 report update committed separately.
- Acceptance: membership PASS; acquisition PASS; raw integrity PASS; coverage PARTIAL; scale code semantics PASS but numeric application BLOCKED; EMDE net-flow aggregation BLOCKED/NOT_AUTHORIZED; vintage/revision controls NOT_DONE; relative-attraction formula/sector transmission/backtest NOT_DONE. All production invariants unchanged.


## 2026-11-19 — GCR IMF BOP SCALE/sign benchmark extended to Brazil + India
- Brazil official BCB SGS 22906 (net acquisition financial assets) and 22924 (net incurrence liabilities), both monthly USD million, independently reconcile to IMF quarterly Data Portal `A_NFA_T` and `L_NIL_T` after summing three months and dividing IMF raw `OBS_VALUE) by 1,000,000. Selected quarters 2015-Q1, Q2, Q3, Q4 and 2026-Q3: 10/10 PASS; max residual 0.121925 USD million under 0.15 tolerance.
- India official RBI Table 197 (BPM6 quarterly, USD million), 2024-Q2 through 2025-Q1: 8/8 PASS within ±0.5 million displayed rounding.
- Combined two-country benchmark 18/18 PASS. For the tested Data Portal API payloads, raw observations are base USD; divide by 1e6 for USD million comparisons. Do not apply ×1e6 again. Preserve raw values and SCALE=6 metadata.
- Brazil CSV `docs/evidence/IMF_BOP_BRA_SCALE_RECONCILIATION_2015Q1_2026Q3.csv`; report `docs/GCR_IMF_BOP_SCALE_RECONCILIATION_BRAZIL_INDIA_PART2_20261119.md`.
- Global all-154 rule is not automatically authorized; this proves two country benchmarks for this exact dataflow/series. Full panel remains BLOCKED for aggregation: 40 members have no data, 3 one-sided, 13 series have interior gaps, only 2 countries have both legs at 2026-Q3; vintage/BPM6-BPM7 alignment remains open.
- Older BCB-registered XML vs SGS 2010 structural break remains a separate unresolved source conflict (201/381 monthly mismatches); do not conflate with the passing current IMF Data Portal quarterly vs BCB SGS check.


### 2026-11-19 — Brazil BOP scale/sign normalization PASS
- BCB official SGS 22906 = portfolio investment net acquisition of financial assets, monthly, million USD; SGS 22924 = portfolio investment net incurrence of liabilities, monthly, million USD.
- Captured both complete raw JSON series anonymously (HTTP 200). SHA-256: SGS22906 `110477090f5ff3e9f4e4d2ce235082d837020603b13795dbc2bde20769a3db30`; SGS22924 `2064005a5dd42b83ba66aeb21de983ca4286af9662f57c23971b4b7dfe295dbb`.
- Compared 2015-Q1, Q2, Q3, Q4 and 2026-Q3 for both Brazil entries. `IMF OBS_VALUE / 1e6` vs sum of three monthly BCB values: 10/10 PASS; max absolute residual 0.12192411 USD million; valid tolerance 0.15 USD million due to 3 monthly values rounded to 0.1.
- Run 44475693836 / artifact 14506740234 / ZIP SHA-256 `08e7702d9c5e393779d6ff635f6d532ddcfcb79be1eb2be18fd840a13f37b79b`; durable evidence commit `45d2ce937be6c2f89d1ba4ae7fe0d1ad14842266`.
- Report `docs/GCR_IMF_BOP_SCALE_RECONCILIATION_BRAZIL_20261119.md`, commit `c7cfefadbcad4703df81ec43b461ab941d85b698`.
- Brazil scale/sign normalization PASS for tested series and quarters only. India and remaining EMDE members remain UNKNOWN; do not generalize or release EMDE aggregate. India Table 196's fiscal-quarter period is not directly aligned to IMF calendar-quarter labels, so it is not accepted as a direct validation.
- Overall GCR status: public BOP access PASS; 154-member raw panel PASS; membership mapping PASS; 1,106 exact sample query-shape checks PASS; coverage PARTIAL; Brazil scale PASS; India/remaining EMDE scale UNKNOWN; BPM/revision controls NOT_DONE; EMDE aggregate NOT_AUTHORIZED; daily trading use NOT_SUITABLE.



## WEO G200 EMDE BOP coverage QA and SCALE concept audit — 2026-11-19
- Independent raw-to-normalized audit: 9,299/9,299 exact observation keys; 30 source fields × 9,299 = 278,970 exact field comparisons; zero duplicates, missing keys or attribute mismatches.
- Coverage: 225/308 country-entry pairs with data; 111/154 members both legs; 3 one-sided (DZA/ETH assets only; ZWE liabilities only); 40 no data; 43/154 lack at least one leg. Only 4 series complete 47/47 quarters; 13 series have internal gaps (71 quarters); 2026-Q3 only BRA and PAK.
- All 9,299 observations have DERIVATION_TYPE=O and UNIT=USD; SCALE=6; PRECISION=6 for 9,119 and blank for 180. No forward-fill, zero substitution, rescaling, FX conversion or aggregation.
- Official concept scheme `IMF:CS_MASTER_SYSTEM(1.0.2)` HTTP 200, 6,192,546 bytes; SHA-256 `9ef243509d7b3edc93b5ef2326ba49c89ced79044ae38674c806d1310367420d`. SCALE English Name=Scale; Arabic label `عدد الخانات العشرية` translates to “number of decimal places”; no English definition or referenced codelist. BOP DSD makes SCALE series-level and distinct from UNIT; do not treat as UNIT_MULT or apply 10^6 multiplier. Preserve raw values.
- Coverage QA run 44475665715 SUCCESS; coverage artifact 14506017682; SCALE artifact 14506356045.
- Detailed report: `docs/GCR_IMF_BOP_EMDE_COVERAGE_QA_PART3_20261119.md`; matrices under `docs/evidence/imf_bop_emde_20261119/coverage_qa/`; scale metadata manifest under `docs/evidence/imf_bop_emde_20261119/scale_semantics/`.
- Decision: data integrity PASS; country coverage PARTIAL; EMDE aggregate BLOCKED / NOT_AUTHORIZED. Sign convention, FX and point-in-time vintage remain unresolved.


## 2026-11-19 — IMF BOP scale/sign semantics validated against official BCB source (Brazil)
- IMF BOP DSD `SCALE` attribute references IMF master system concept scheme `CS_MASTER_SYSTEM(1.0.2)` and codelist `CL_UNIT_MULT(1.0+.0)`; code `6` label = `Millions`.
- This metadata alone does not mean multiply the API response again. Official BCB SGS 22906 (monthly portfolio net acquisition of assets, USD million) and 22924 (monthly portfolio net incurrence of liabilities, USD million) provide the source comparator.
- Full cross-source check for 47 quarters 2015-Q1–2026-Q3, both series: sum BCB monthly values in USD million and compare to IMF BOP API `OBS_VALUE / 1,000,000`. 94/94 PASS, 0 REVIEW, 0 BLOCKED; tolerance 0.15 USD million; maximum absolute residual 0.12192411 USD million.
- Operational decision for the tested Brazil series: IMF API `OBS_VALUE` is already USD; preserve `SCALE=6` as source metadata and DO NOT multiply API values by 10^6 again. No panel values were transformed.
- Evidence: `docs/evidence/imf_bop_20261119/bcb_scale_reconciliation/summary.json`, `quarter_reconciliation.csv`, `quarter_reconciliation.json`, raw SGS 22906/22924 JSONs. Full run 44476176136 / artifact 14505944936 / SHA-256 `1c9c1975717764aea11230f9fb659270a43c98b198e0154605589a1a8a19f317`.
- Scope limitation: this is Brazil only. India and other EMDE countries still need independent source-to-source scale/sign validation before GCR aggregation.
- Updated research note: `docs/GCR_IMF_BOP_PUBLIC_OBSERVATION_ACCESS_PART1_20261119.md`; prior access boundary updated with the 94-check result.


### 2026-11-19 — India BOP scale/sign validation PASS; two-country normalization gate
- RBI Table197 official BPM6 quarterly USD-million page (31-Jul-2026) raw HTML archived: 146,017 bytes, SHA-256 `391c549c5b64c0b7f9204eb9634975f77d4ba2d7796542ed23932fb8d740813d`.
- RBI 3.2.A Portfolio Investment in India credit-minus-debit net maps directly to IMF L_NIL_T; RBI 3.2.B Portfolio Investment by India maps to IMF A_NFA_T with sign reversal.
- Six calendar quarters 2024-Q2–2025-Q3 × 2 entries = 12/12 PASS using IMF raw OBS_VALUE / 1e6; max residual 0.4899709189 USD million, within 0.5 million integer rounding bound.
- Run 44476434148 / artifact 14506542277 / ZIP SHA-256 `eb719a38a285603ec2eff92ea7a88aadd5cbb7481393fe5b8f44188bffcacf62`; durable evidence commit `451b9e203fd6edb1541c42432b47a393e030372c`.
- Report `docs/GCR_IMF_BOP_SCALE_RECONCILIATION_INDIA_20261119.md`, commit `4a3bcc34a19d92e747f50609a7cabebe489af69a`.
- Combined pilot-country scale/sign evidence: Brazil BCB 10/10 + India RBI 12/12 = 22/22 PASS. Scale normalization `USD_million=OBS_VALUE/1e6` validated for BRA and IND tested series/quarters; no sign flip applied to IMF raw values.
- Remaining 152 EMDE countries remain UNKNOWN pending national source validation; no full 154-member conversion or aggregate. Coverage remains PARTIAL; BPM/revision/vintage controls NOT_DONE; daily swing use NOT_SUITABLE.


## 2026-11-19 — Cross-country IMF BOP P_F scale/sign validation extended to four EMDE countries
- WEO October-2026 G200 membership remains 154/154 exact-code mapped to IMF BOP COUNTRY codelist; 154 unique, no duplicates, no unmapped.
- Full EMDE panel remains 9,299 observations, 9,299 unique keys, no duplicates; coverage is PARTIAL (114/154 countries any observations, 111 both entries, 40 neither, 83 empty country-entry cells, 13 series with interior gaps, 4 full 47-quarter series).
- Four independent national-source comparisons now provide **118/118 PASS on vintage-aligned samples**:
  - Brazil BCB SGS 22906/22924: 47 quarters × 2 entries = 94/94 PASS; 2015-Q1–2026-Q3; tolerance 0.15 USD million; max residual 0.12192411. Run 44476176136 / artifact 14505944936 / ZIP SHA-256 `1c9c1975717764aea11230f9fb659270a43c98b198e0154605589a1a8a19f317`.
  - India RBI Table 197: 6 quarters × 2 entries = 12/12 PASS; 2024-Q2–2025-Q3; tolerance 0.5 USD million; max residual 0.4899709189. Run 44476434148 / artifact 14506542277 / ZIP SHA-256 `eb719a38a285603ec2eff92ea7a88aadd5cbb7481393fe5b8f44188bffcacf62`.
  - Mexico Banxico CE174: 3 quarters × 2 entries = 6/6 PASS; 2025-Q4–2026-Q2; tolerance 0.5 USD million. Run 44476089607 / artifact 14506696311 / ZIP SHA-256 `26ba04369dfba423609c313f68995dd7eeb7c5c44727d1df29a8062a3998c58c`.
  - Chile Banco Central BDE older official page vintage updated 2026-09-07: 3 quarters × 2 entries = 6/6 PASS; 2025-Q4–2026-Q2; monthly values in whole USD million, ±1.5 quarterly-sum tolerance. This older snapshot is web-rendered official evidence; raw bytes were not archived.
- Empirical conversion for the tested vintages: compare `OBS_VALUE / 1,000,000` to national US$ million values; preserve raw API observations and SCALE=6 metadata; never multiply raw OBS_VALUE by 10^6 a second time.
- **Critical vintage exception:** current Chile BDE pages updated 2026-11-18 were independently captured (run 44476957975 / artifact 14507305215 / ZIP SHA-256 `155fffc6fbc46df12f0905cd00b011651ced7df1368ceb0a65b736a090052691`). Current vintage: Q4 2025 2/2 PASS; Q1–Q2 2026 4/4 REVIEW (differences exceed rounding); Q3 2026 has national data but IMF CHL panel rows are missing (2 IMF_PANEL_MISSING). This indicates source-vintage/revision mismatch; cause remains unresolved. Do not blend 2026-09 and 2026-11 Chile vintages.
- Cross-country report: `docs/GCR_IMF_BOP_SCALE_RECONCILIATION_CROSS_COUNTRY_PART3_20261119.md`, latest update commit `ca294d2d8ce416f306dba580d90286bca903f168`.
- Consolidated 126-row machine-readable matrix: `docs/evidence/IMF_BOP_SCALE_CROSS_COUNTRY_VALIDATION_20261119.csv`, update commit `ee67a4c621ac47be02ecc419257771fcab13ada9` (94 BRA + 12 IND + 6 MEX + 6 CHL old vintage + 8 CHL current vintage).
- Scale metadata and empirical evidence summary: `docs/evidence/imf_bop_emde_20261119/scale_semantics_probe_summary.json`, update commit `747d92a3ad5c794a1d73f1dbb1757f485158ac76`.
- Decision: four-country vintage-aligned sample PASS; latest Chile source-vintage mismatch remains REVIEW. Do not call the transform universal for all 154 countries and do not create an EMDE aggregate yet.
- Next priority: build a vintage-aware country-entry observation matrix; resolve Chile Q1/Q2 2026 revisions; validate one further current-vintage EMDE national source; only then consider an observed-country subtotal with explicit coverage. No imputation.
- Invariants unchanged: Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A–E. ₹0 spend; no paid APIs; no synthetic data; UNKNOWN is not PASS.


 
## 2026-11-19 — India current-vintage scale/sign supplement
- Preserve the India historical RBI Table197 BPM6 baseline: 2024-Q2–2025-Q3, 12/12 PASS.
- New RBI Table42 BPM6 supplement: 2025-Q1/Q2 overlap checks plus 2026-Q1/Q2. 10/12 checks PASS; 2026-Q1 liability and combined net REVIEW; 2026-Q2 all pass.
- 2026-Q1 IMF liability /1e6 = -13,633.508347m vs RBI 3.2.A net -12,121m; residual -1,512.508347m. Do not silently reconcile.
- Detailed supplement report `docs/GCR_IMF_BOP_SCALE_RECONCILIATION_INDIA_CURRENT_VINTAGE_SUPPLEMENT_20261119.md`; raw RBI pages and comparison CSV committed under `docs/evidence/imf_bop_20261119/india_scale_reconciliation_current_vintage/`.
- Current India status: historical baseline PASS, current 2026-Q1 REVIEW. Overall 4-country vintage-aligned benchmark 118/118 remains valid; current Chile and India revisions remain separate REVIEWs. No aggregate or production admission.


## 2026-11-19 — GCR fifth-country Nigeria national-source check
- New report: `docs/GCR_IMF_BOP_SCALE_RECONCILIATION_NIGERIA_20261119.md`; consolidated cross-country Part 4: `docs/GCR_IMF_BOP_SCALE_RECONCILIATION_CROSS_COUNTRY_PART4_20261119.md`.
- Official CBN Q2 2026 BOP Highlights PDF, Table 2 (Financial Accounts), printed page 6, was retrieved HTTP 200; 2,206,494 bytes; SHA-256 `b77c0066385cac4bb3bcbe150321c8da28da7d76c91b78423808a31deaea4cf9`.
- IMF public SDMX 3.0 exact-key queries for Nigeria `NGA.A_NFA_T.P_F.*.Q` and `NGA.L_NIL_T.P_F.*.Q` returned HTTP 200; raw CSVs archived. Periods selected: 2025-Q2, 2026-Q1, 2026-Q2.
- CBN Table 2 USD bn: assets -0.66, +0.26, +0.70; liabilities +5.28, +6.03, +7.09. Derived IMF USD million = raw OBS_VALUE/1e6; CBN USD million = USD bn×1000. Tolerance ±US$5m based on 0.01bn display precision. Six comparisons: 6/6 PASS, 0 REVIEW, 0 missing.
- Workflow run 44485137974 SUCCESS; artifact 14510920161; ZIP SHA-256 `bf80b403e072c8eae39f4ec32de77b55d776ef77b7ff4a88e157e3023da7febf`.
- Durable evidence under `docs/evidence/gcr_nigeria_bop_20261119/`: raw IMF assets/liabilities CSVs, exact comparison CSV, summary/provenance JSON and CBN Table 2 extracted page text. Raw CBN PDF can be re-downloaded from its official URL; raw byte hash is preserved in summary and report.
- Cross-country vintage-aligned sample increases from 118/118 to 124/124 across five countries: Brazil 94, India 12, Mexico 6, Chile older 2026-09 vintage 6, Nigeria 6. This is not universal validation across all 154 EMDE members.
- CBN vintage flags retained: Q2 2025 provisional, Q1 2026 revised, Q2 2026 described as provisional in the release narrative. No vintage mixing.
- India Q1-2026 liability REVIEW and Chile current-vintage revision mismatch remain open. Full 154-member aggregate remains BLOCKED/NOT_AUTHORIZED; no production/backtest admission.
- A malformed path-ignore edit briefly caused the production NSE workflow to trigger on research commits. The literal `\\n` entries were corrected in `.github/workflows/nse_collector.yml` at commit `9ef1922f63c3091519fe5208ee63e259fcc571c5`. The three unintended collector runs (44484649213, 44484666061 and 44485482464) were subsequently cancelled by bounded helper workflow run 44485600055 (SUCCESS). The malformed path-ignore entries were repaired; subsequent research-only commits are included in paths-ignore. No production code was intentionally changed.


## 2026-11-19 — Continuation 38, Part 1: PA transaction-2 alternate serialization probe dispatched
- The exact Brazil registration lifecycle remains captured (Part-7; run 44465947951; artifact 14502380926; 40/40 event XMLs parsed), but PA transaction ID 2 / Changelog remains unresolved.
- Added read-only alternate serialization probes for `/ws/registry/tx/transactions?txId=2&format=fusion-json` and `format=sdmx-json` to `scripts/research/probe_imf_brazil_pa_structure_revision.py`; JSON parser records top-level keys and maintainable object counts/IDs. Script commit `5230a74409a96555fe0f598cd5258f55f42ed11a`.
- Trigger marker commit `032a1871a9713f7330ebaad6455597393639eec3`; production collector ignore rule for the trigger path was checked before triggering.
- Report: `docs/IMF_BRAZIL_PA_TX2_ALTERNATE_SERIALIZATION_PROBE_PART1_20261119.md`.
- Status: IMPLEMENTED / TRIGGER COMMITTED; workflow run and artifact inspection NOT_YET_VERIFIED. Brazil Reconstruction remains BLOCKED; do not infer PA changelog or resolve BOP6/BOP_BPM6 mismatch. No production code, selector, score, diagnostics or engines changed; ₹0; UNKNOWN is not PASS.
- Next: inspect the workflow run/artifact from trigger commit; accept only actual 200 + parsed PA/structure evidence, otherwise preserve exact errors and keep the blocker.


## 2026-11-19 — Continuation 38 Part 1: Brazil PA transaction 2 format probe closed with negative result
- Focused run #34 / 44493473476 SUCCESS; artifact 14513337963; ZIP SHA-256 `824a09425db76982ba73a1b9f51cd768669d560a5b017b732f0cf224ce7720e6`.
- `txId=2&format=fusion-json` and `txId=2&format=sdmx-json` both returned HTTP 500 with identical 39-byte body `Unable to return transaction for id '2'`; raw SHA-256 `76c4819f18129eb81b5fab80dcf0641665f332b823864c2c09280efe21415825`. Both retrievals and raw bytes archived; Content-Type application/zip did not match body.
- Alternate format probe PASS; PA tx2/Changelog BLOCKED; Brazil Reconstruction BLOCKED. No inference that PA absent; BOP6/BOP_BPM6 mismatch remains unresolved; no alias/admission.
- FMR documented UI route for next attempt: Activity / Structure Submissions and Provision Agreement detail Changelog/Compare. If no authorized public access, preserve UNKNOWN and pivot to remaining GCR coverage blockers. No production changes; ₹0.
- Report: `docs/IMF_BRAZIL_PA_TX2_ALTERNATE_SERIALIZATION_PROBE_PART2_20261119.md`.


## Continuation 38 Part 1 — exact IMF UI follow-up route added
- Based on live official IMF SDMX Central pages, next read-only UI route is documented precisely: `/activity/activity-log.html` (transaction period around 2023-09-22 and Download Transaction), `/activity/structure-log.html` (Structure Submissions, Download Revision, Compare), and `/data/provisionAgreements.html` (filter IMF / BR_BOP_BP6; Changelog, Revisions, Compare/Export).
- Official UI pages expose these controls, but the dynamic Brazil PA row/revision files have not yet been captured. No claim of historical PA recovery; chronology remains UNKNOWN/BLOCKED pending actual files.
- Supporting official UI sources: IMF SDMX Central activity log, structure log and Provision Agreements pages. No write action or authentication attempt performed.


## Continuation 39 — Brazil PA RSS historical archive test
- Official IMF SDMX Central RSS GET 200; XML parse PASS; 38 latest items from 2026-11-18 09:11:47Z through 2026-11-19 08:43:07Z. Zero Brazil/PA/BOP6/tx2 matches. Raw SHA-256 `ff0c03df5d6b9557d6f6c21a341a7d589baef38893291fcfc2ff715257619e73`; run #35 / 44493898103 SUCCESS; artifact 14513872121; ZIP SHA `e88d37e4054c304618ed1af4be14337a6e0b583d791b4cf2e93115410854639a`.
- Conclusion: RSS is current/recent activity only, not a 2023 historical transaction archive. tx2 alternate format endpoints remain 500. No duplicate retries. PA chronology and Brazil reconstruction BLOCKED.
- Workflow accidental NSE run #381 / 44493879791 was triggered by missing ignore entry, then successfully CANCELLED by helper run 44493979049. Added paths-ignore entries for both Brazil probe scripts and trigger; guard commit `110c8e6d6abbe536165c760d919c4c3926030501`. No production source changes.
- Next action: actual interactive official IMF UI or authorized historic export. If unavailable, pivot to GCR coverage closure; keep UNKNOWN. Report: `docs/IMF_BRAZIL_RSS_TRANSACTION_ARCHIVE_PROBE_PART3_20261119.md`.


## Continuation 39 Part 2 — GCR zero-data national source discovery
- Parsed the exact 154-country readiness CSV: 40 NO_DATA (both IMF P_F entries absent), 3 ONE_SIDED (DZA assets, ETH assets, ZWE liabilities), and 2 both-leg latest-period mismatches (BRN/KIR); 13 country-entry series have internal gaps per prior QA summary.
- Found official source route for 11/40 zero-data members: seven 2024 BCEAO country reports (BEN/BFA/CIV/GNB/MLI/SEN/TGO), Niger 2023 report, UAE annual source, Kenya annual/quarterly BOP sources, Oman BOP XLSX/CSV listing. UAE currently disseminates annual only; Kenya data vintages/units vary; Oman file not yet captured.
- This is source discovery only, not data repair. Annual reports do not provide quarterly series; no interpolations, forward fills, proxy totals, currency conversions, or IMF P_F admissions.
- Durable report: `docs/GCR_ALTERNATE_NATIONAL_BOP_SOURCE_COVERAGE_MAP_20261119.md`.


## Continuation 40 — BCEAO 2024 UEMOA Annual BOP benchmark extraction
- Official BCEAO Annual Report 2024 PDF Annexes A23–A27 source text yields 2024(*) national BOP tables for all eight UEMOA members. Extracted reported financial-account net balance plus net direct investment, net portfolio investment, net derivatives and net other investment for BEN/BFA/CIV/GNB/MLI/NER/SEN/TGO (FCFA billion; 2024 estimate).
- Component sum QA: 5/8 exact, 3/8 have ±0.1 FCFA bn residual (BFA -0.1, CIV -0.1, TGO +0.1); preserve published totals. Correction to report/checkpoint summary: exact 5/8, not 6/8.
- No source separates assets vs liabilities. IMF A_NFA_T/L_NIL_T mapping remains BLOCKED / NOT_SEPARATELY_DISCLOSED. Annual estimate not admitted to quarterly panel.
- Original PDF bytes/hash not yet archived; values are transcribed from official PDF extracted text pending byte archival and page-image verification.
- CSV `docs/evidence/gcr_bceao_2024/bceao_2024_uemoa_financial_account_net.csv`; report `docs/GCR_BCEAO_2024_ANNUAL_NET_BOP_BENCHMARK_20261119.md`.


## Continuation 40 — BCEAO raw PDF archive verified
- Official BCEAO Annual Report 2024 PDF downloaded by focused run `44494766325` SUCCESS; HTTP 200; 7,076,916 bytes; retrieved UTC 2026-11-19T09:15:44.644765Z; SHA-256 `d1d69c4772e244174c754552b52f4206e8eaf98a6b839bdcd5af1990cf1a3d84`; PDF magic %PDF-1.5.
- Artifact ID `14514282771`, ZIP SHA-256 `7b5865d7c38f45b3d311c7e3cea0e9381ba35f4ed46d0025411ffdcb27e060df`, 90-day retention. Artifact downloaded and raw PDF hash rechecked.
- Accidental NSE runs `44494746703` and `44494753220` cancelled before NSE data acquisition; helper run `44494822191` SUCCESS. Collector paths-ignore now includes archive script, trigger and workflow. No production code change.
- Net benchmark remains PARTIAL; separate IMF asset/liability legs not disclosed by this report, so mapping remains BLOCKED.


## Continuation 41 — BCEAO CIV 2024 gross FDI split
- Found an official 2021 CIV report with aggregate gross asset/liability columns, proving that detailed national reports can contain the required structure; historical vintage is not interchangeable with 2024.
- Archived CIV 2024 national BOP PDF: 3,596,808 bytes, SHA-256 `99aee45e2f75464e85b9b319c9acd93bfd706779119e8c6bfac8db0f5a1a2f28`; run `44495255971` SUCCESS; artifact `14515150693`, ZIP digest `6ad9941564fbed0c144e6d65e7065acbef5c6511df19fb7cd5c59ce5f9659baa`.
- Printed pp.24–25: direct-investment asset acquisition 138.1, liability incurrence 1,892.8; net 138.1−1,892.8=−1,754.7 exactly matches Table 13. Asset/liability subcomponent sums also exact. Portfolio, derivatives and other investment are net-only in the report; total financial account −4,043.1.
- Therefore FDI gross-leg extraction PARTIAL PASS only; aggregate IMF A_NFA_T/L_NIL_T remains BLOCKED / NOT_MAPPED. Do not promote the FDI-only amounts to total legs.
- CSV `docs/evidence/gcr_bceao_2024/civ_2024_fdi_gross_legs.csv`; report `docs/GCR_BCEAO_CIV_2024_FDI_GROSS_LEGS_PARTIAL_20261119.md`.
- Two accidental collector runs `44495237321`, `44495240272` cancelled before market-data step; helper `44495300530` SUCCESS. No production code change.


## Continuation 41 — BCEAO CIV 2024 / BEN-BFA-SEN source work
- CIV 2024 official PDF raw archive verified (3,596,808 bytes, SHA-256 `99aee45e2f75464e85b9b319c9acd93bfd706779119e8c6bfac8db0f5a1a2f28`; run `44495255971`; artifact `14515150693`). Printed pp.24–25 explicitly report FDI asset acquisition 138.1 and liability incurrence 1,892.8 FCFA bn; 138.1−1,892.8=−1,754.7 exactly matches net FDI. Other investment categories are net-only, so aggregate IMF legs remain blocked.
- BEN/BFA/SEN 2024 official reports acquired and hashed in focused run `44495561543` SUCCESS; artifact `14514373729`, SHA-256 `6a670ead73df28b6766aef0c0e5004f795867903dc9bdb3ad59b248c0921518d`. BEN raw hash `15af93618aafee0446eef191ab9e208dcc1c807e3507eadf306c1ce6dbc92193`; BFA `6a4b7149d5abb13d4aac7600cc13a7c0b157cb1d6aa06f8fed41e2b12e33a8ba`; SEN `ee8e7794d2ad85f337d6c1536edcda973f3f7f322cb3b131e332fdb38a133395`.
- Initial screen: BEN transaction table net only; portfolio stocks separately disclosed but not flows. BFA reports total net +777.8bn and inward FDI liability-side decrease -122.6bn; no full gross pair established. SEN gross leg values UNKNOWN pending page-image review. No inferred legs.
- Source-screen report: `docs/GCR_BCEAO_BEN_BFA_SEN_2024_SOURCE_SCREEN_20261119.md`, commit `b0eca5eff4129b84ee7603a49ed7a36837144aeb`.
- Next priority: page-image/OCR review BFA/SEN, then GNB/MLI/TGO 2024 reports. Do not admit to aggregate until both full legs reconcile.


## Continuation 42 — BFA scoped gross legs / BEN-SEN net-only checks
- BFA official Table 15: 2024 non-monetary sector assets 342.6; liabilities 1,120.4; balance -777.8 FCFA bn. Category pairs recorded in `docs/evidence/gcr_bceao_2024/bfa_2024_gross_legs_scoped.csv`. Exact total check. Other investment has 0.1 rounding residual.
- BCEAO optic excludes monetary-sector portfolio, derivatives and other investment; not full IMF national financial account. Thus partial scoped gross-leg PASS only, aggregate remains BLOCKED.
- BEN Table 14 net-only. SEN Table 16 page-image confirmed net-only. Corrected source screen report `docs/GCR_BCEAO_BEN_BFA_SEN_2024_SOURCE_SCREEN_20261119.md`.


## Continuation 60 — GNB IMF BOP series-key / periodicity audit (2026-11-19)
- Existing GCR capture uses legacy dataflow IMF.STA:BOP(21.0.0), DSD IMF.STA:DSD_BOP(24.0.0); dimension order COUNTRY, BOP_ACCOUNTING_ENTRY, INDICATOR, UNIT, FREQUENCY. Existing pilot verifies A_NFA_T = Assets, Net acquisition of financial assets; L_NIL_T = Liabilities, Net incurrence of liabilities; P_F = Portfolio investment, Total financial assets/liabilities; USD; Q.
- Existing 154-member panel QA classifies GNB as no observations for either P_F leg. This is a finding for the captured panel/dataflow/vintage only, not proof that all current IMF dataflow versions lack a GNB series.
- IMF BOP dataset page identifies annual and quarterly frequency and announces BOP/IIP Metadata Dashboard release 2026-11-18. IMF e-GDDS GNB metadata says BOP aggregates appear annually in a national brochure. IMF Country Report 25/167 says final annual BOP data are produced 10–12 months after year-end and notes GNB's NSDP launch in June 2024. Older IMF Country Report 22/196 documented weak BOP data and expected ITRS to improve periodicity from annual to quarterly.
- IMF SDMX Central currently lists BOP DSD v2.6.0; current legacy panel mapping uses DSD 24.0.0. No automatic crosswalk assumed.
- Exact current GNB API requests for GNB.A_NFA_T.P_F.USD.Q and GNB.L_NIL_T.P_F.USD.Q were not successfully executed in this audit; current dashboard GNB country detail was not retrievable. Therefore exact current series availability remains NOT_VERIFIED, not ABSENT.
- Report: docs/GCR_GNB_IMF_BOP_SERIES_KEY_AUDIT_20261119.md, commit 2cd187c3dd1e92738eb6625bcafdde16838504ed.
- Next: bounded read-only API capture of both exact GNB keys in legacy and current structures, preserve HTTP/raw response/attributes/hashes; then assess period, status, unit, scale and vintage. No quarterly interpolation, no gross inference, no production/backtest admission. Production invariants unchanged; ₹0; UNKNOWN is not PASS.


## Continuation 61 — GNB IMF exact-key probe dispatched (2026-11-19)
- The screenshot supplied by the user showed the prior Continuation 59 GNB metadata audit; continued its explicit next action rather than repeating the source summary.
- Public web extraction could not directly open the IMF API data URLs; this is a browser-tool access limitation, not evidence of an IMF HTTP error or absent series. IMF confirms public SDMX 2.1/3.0 APIs are available; official API overview: https://data.imf.org/en/Resource-Pages/IMF-API.
- Added bounded read-only Python probe for exact GNB 2024 quarterly and annual keys: GNB.A_NFA_T.P_F.USD.Q; GNB.L_NIL_T.P_F.USD.Q; GNB.A_NFA_T.P_F.USD.A; GNB.L_NIL_T.P_F.USD.A. It records exact URLs, retrieval UTC, HTTP status, safe headers, raw bytes, byte count, SHA-256, CSV parse/observation counts, periods and samples. No conversion/interpolation/admission.
- First committed production-collector path-ignore guard before adding research files: commit 665ee6336a96e994224b9c1504b05be0eabaea39. Script commit c97f55b13e29a2d8d756844c2667b8fc17072d87; focused workflow commit a02ec6d47b870371c45f2ac3ad961ee5bfc68286; trigger commit 207dc2b12baed47806929afd9ac3186602691255.
- Workflow `.github/workflows/imf_bop_gnb_series_probe.yml` has a 3-minute timeout and uploads raw responses/summary as a 90-day artifact. Trigger was pushed; workflow run/artifact has NOT_YET_BEEN_VERIFIED in this turn. Do not claim the API returned 200/404 until run evidence is inspected.
- Next: inspect Actions run and artifact, verify raw response bytes/hash and exact status; if the IMF API request fails, preserve the response and probe current DSD v2.6.0 separately. GNB gross legs remain UNKNOWN/BLOCKED. No production code/selector/score/pressure-fade/CORE-672/engines changed; ₹0.


## Continuation 62 — GNB IMF exact-key probe results verified (2026-11-19)
- First focused workflow run `44506401980` SUCCESS; artifact `14519308912`, 2,788 bytes, SHA-256 `5a9093879b7d94371a7aba10473c10284a96eb106ec85caa9febfe285dce4519`. Four exact annual/quarterly A_NFA_T/L_NIL_T P_F USD requests each HTTP 200, CSV envelope parse PASS, zero OBS_VALUE; each raw response 400 bytes, SHA-256 `f369fecfb4531216b77a2a0806564140ef8c97fce955e79de92938748d3bb311`.
- Expanded wildcard-indicator workflow run `44507263244` SUCCESS; artifact `14520147539`, 3,681 bytes, SHA-256 `9a94977b98e010536a7f50553e8a8f843e0d7bd30da9bdfedb7b6aabaaeaa187`. Two additional GNB A_NFA_T/L_NIL_T wildcard-indicator quarterly requests also HTTP 200, CSV parse PASS, zero observations. Total six tested requests; all raw response files are header plus dataflow row, no OBS_VALUE.
- Interpretation is strictly scoped: no observations returned for these exact 2024 requests against legacy IMF.STA:BOP(21.0.0); this is not proof of universal absence across all IMF dataflows/versions or all possible units/indicators. HTTP 200 means transport success, not data availability.
- No gross legs inferred from BCEAO net annual figures; no conversion, interpolation, stock-to-flow, forward-fill or production admission.
- Full report: `docs/GCR_GNB_IMF_BOP_EXACT_KEY_PROBE_RESULTS_20261119.md`, commit `ec71d94c13e7fdf65ad28365b60cd5259db02b00`.
- Next bounded action: retrieve official current BOP DSD v2.6.0 and related dataflow/constraints/codelists from SDMx Global Registry; establish exact code crosswalk before any current-version GNB query. Gross-leg status remains BLOCKED.


## Continuation 63 — BOP DSD v2.6.0 official registry capture initiated (2026-11-19)
- Official SDMx Global Registry lists IMF:BOP DSD latest version 2.6.0. Official SDMx-BOP maintenance policy states new DSD versions do not automatically invalidate previous versions; older versions may continue if changes do not affect the exchange template. Therefore legacy 24.0.0 mapping is not presumed invalid.
- Registry model confirms DSD, codelists, dataflows, provision agreements and reporting constraints are distinct artefacts; country coverage must not be inferred from DSD alone.
- Reused existing repository capture script `scripts/research/capture_imf_bop_dsd_v260.py` and workflow `.github/workflows/imf_bop_dsd_v260_capture.yml`; it requests official registry DSD v2.6.0 in SDMX-ML 2.1 and 3.0 with references=all, records raw XML/status/headers/UTC/byte count/SHA-256 and parses artefact references. No observation data is queried.
- Trigger commit `79817af059973e09038969fd401cde3afdd7f00e`; workflow run `44507773721` observed in progress at last check; structure capture step not yet completed and no artifact/hash yet. Do not call this a PASS until the run and artifact are inspected.
- Official sources: https://sdmx.org/sdmx-data-structure-definitions-for-balance-of-payments-sdmx-bop/ ; https://registry.sdmx.org/data/datastructure.html ; https://sdmxcentral.imf.org/overview.html .
- Next: inspect run 44507773721 and verify artifact; extract exact dimensions, codelist IDs, dataflow IDs, constraints, then crosswalk legacy codes to v2.6.0. Only after explicit crosswalk, test GNB provision/coverage. No production admission. Invariants unchanged; ₹0; UNKNOWN is not PASS.


## Continuation 64 — IMF BOP DSD v2.6.0 archive independently verified (2026-11-19)
- Focused workflow run `44507773721` / run #2 SUCCESS; job `capture` SUCCESS; trigger commit `79817af059973e09038969fd401cde3afdd7f00e`.
- Artifact `14520401775`, 237,677 bytes, expires 2027-02-17T10:40:03Z; ZIP SHA-256 `d3948cfae4ed6df052736035e95572914200dbde0a945f3d43f86df950395a94`; manifest SHA-256 `d545ae12d27caa62c48f4303f277f0df4e23d46a8b68af78cce0620f689c76ac`.
- Raw SDMX-ML 2.1: HTTP 200, 1,081,882 bytes, SHA-256 `543c103c18b5597143969ef4fb42ba91be263b03262c257d47824fb45eb8e989`, XML parse PASS. SDMX-ML 3.0: HTTP 200, 1,076,119 bytes, SHA-256 `4508050ea5fce0b0d5ac8184e1d3575bc000e22377e9fd6cb5c126eddd6eedaf`, XML parse PASS.
- Extracted DSD `IMF:BOP(2.6.0)`: 17 ordinary dimensions + TIME_PERIOD; 23 codelists; one concept scheme; 3 returned dataflows. These three dataflows are ESTAT-maintained (`BPM6_BOP_M`, `BPM6_BOP_Q`, `BPM6_ITS_A`) and reference the IMF DSD. Returned package manifest reports zero constraints.
- SDMX-ML 3.0 parsed successfully, but manifest reference counter is not implemented for its namespace/layout (unique_references=0); manual XML inspection confirms DSD and dataflows. Do not interpret counter as missing references.
- Crucial boundary: this Global Registry DSD `IMF:BOP(2.6.0)` is not automatically equivalent to the existing IMF Data Portal `IMF.STA:DSD_BOP(24.0.0)` / dataflow `IMF.STA:BOP(21.0.0)`. Existing legacy mapping is five dimensions + time; new registry DSD is 17 + time. No crosswalk or series remapping performed. Official maintenance policy says newer DSD does not automatically invalidate earlier versions.
- Decision: metadata capture PASS; legacy/current dataflow crosswalk NOT_DONE/BLOCKED; GNB current-version availability NOT_TESTED; no observation capture or GCR coverage repair. Report: `docs/GCR_IMF_BOP_DSD_V260_CAPTURE_VERIFICATION_CONTINUATION64_20261119.md`, commit `e93c8e68571b93fdc9f6855203cdc6e8a3d32b4c`.
- Next: capture exact legacy IMF.STA DSD v24.0.0 and BOP dataflow v21.0.0 metadata/constraints, build an explicit field/code crosswalk only where semantics match, then bounded GNB exact-key tests. No synthetic data, interpolation, forward-fill, scale/sign conversion or production admission. All invariants unchanged; ₹0; UNKNOWN is not PASS.


## Continuation 65 — Legacy IMF BOP metadata request diagnosis and collector isolation (2026-11-19)
- Legacy metadata capture run `44509408818` FAILED; job `135509392076`. Both exact IMF Data Portal structure requests returned HTTP 400; DSD response body 392 bytes SHA-256 `74e7a371a2f0927cc5b7fddaebf4db087200a6338e966027a070054d0fd955f3`; dataflow response body 383 bytes SHA-256 `0b0c774c09266b1e5792094dddd3dbf9ac23ae77ac1d60411d9958c92681ae2a`. XML parse NOT_RUN; artifact upload skipped. These are error-body hashes, not metadata hashes.
- Interpretation: request/endpoint-format failure only; not evidence of absent legacy artefacts or observations. No crosswalk built, no current-version GNB test. Exact response body content was not emitted in the job log, so root cause is not yet established.
- Report: `docs/GCR_IMF_BOP_LEGACY_METADATA_CAPTURE_FAILURE_DIAGNOSIS_20261119.md`, commit `9f6d5d6ca159f388768b6c94e02d0aca261ad8fb`.
- CI guard defect found: NSE collector `paths-ignore` omitted the legacy capture script/workflow, causing accidental collector triggering on the research push. Added both exact paths to `.github/workflows/nse_collector.yml`; guard commit `1a88a2a457a330185fd5ff766b2dff15b41fe390`. Verify subsequent research pushes do not trigger the collector.
- Official IMF SDMX Central registry guide documents its own service entry point `https://sdmxcentral.imf.org/sdmx/v2/`; this must not be conflated with `api.imf.org` Data Portal API or assumed to contain identical artefacts. References: https://sdmxcentral.imf.org/webservice/schema.html ; https://dsbb.imf.org/content/pdfs/IMFSDMXCentralWebServicesGuide.pdf ; https://data.imf.org/en/Resource-Pages/IMF-API .
- Next: inspect official IMF Data API structure-query contract and obtain complete raw error body; run one minimal documented read-only request before any versioned capture. Only after HTTP 200 + parse + exact identity validation may crosswalk work proceed. No production/selector/score/pressure-fade/CORE-672/engine changes; ₹0; UNKNOWN is not PASS.


## Continuation 66 — IMF legacy BOP registry ID probe (2026-11-19)
- Official API documentation reviewed: IMF SDMX Central public structure service entry point is `https://sdmxcentral.imf.org/sdmx/v2/`; IMF Data API is a distinct portal/API route with Swagger requiring beta portal sign-in. Do not conflate them.
- Probe 1, agency `IMF`: run `44510554257` SUCCESS, job `135513379536`, artifact `14522671636`, ZIP SHA-256 `847f0930bc9ee625c01dd1d3c7bb71d10a0063e927d6bad948515a6031def01e`. Exact DSD_BOP v24.0.0 and BOP v21.0.0 requests returned HTTP 404, SDMX Error code 100 / No Results Found. Each body 421 bytes, SHA-256 `aa0b5827e5185b172e34b7891c2ec205db7502459842237eca92bdd11bc1d87e`.
- Probe 2, agency `IMF.STA`: run `44510641519` SUCCESS, job `135513689116`, artifact `14523605400`, ZIP SHA-256 `ec3eeb726daf1a845fcbe710d4888ffff95ad1ad9bbdc1120aff2f97afb79431`; manifest SHA-256 `04a54cf216bbd595afe6bc7e2d0566cc87881de749242a89e8df0747c7799196`. Both exact requests again returned HTTP 404, SDMX Error code 100 / No Results Found; each raw body 421 bytes, same SHA-256 above. Artifact downloaded and ZIP/raw/manifest hashes independently verified. XML is well-formed error XML; XML parse PASS is not metadata success.
- Report: `docs/GCR_IMF_LEGACY_BOP_REGISTRY_ID_PROBE_RESULTS_20261119.md`, commit `8a020cc15742ed77653f75733e72656ea0bbc486`.
- Decision: public SDMX Central does not return either legacy artefact under tested IMF or IMF.STA agency paths. This does NOT establish absence from separate IMF Data Portal API. Legacy metadata capture/crosswalk/GNB current-version tests remain BLOCKED/NOT_DONE. Stop repeating these public registry probes.
- CI isolation: the new research workflow/script/trigger initially caused accidental collector runs because all three paths were not yet ignored. Guard commit `66ba13b9f4c3311dae5b977dc3785a32c7c82e39` now ignores all three. Corrected follow-up script run `44510641519` did not trigger NSE collector. Apply the three-path guard before every future research trigger.
- Next: only pursue IMF Data API route if existing free public access is available; Swagger currently indicates beta portal sign-in. Do not invent credentials or claim public access. Otherwise pivot to alternative official source coverage. No observations, conversion, interpolation, production/backtest admission; selector/score/pressure-fade/CORE-672/engines unchanged; ₹0; UNKNOWN is not PASS.


## Continuation 67 — 2026 GCR market signal mapping (2026-11-19)
- Reviewed all five user-supplied outlook links. Allianz Global Equity Compass Nov-2026 (published 18-Nov) accessible: October Momentum reversal, Quality weakness, Value strength, elevated bond-yield hurdle, AI capex-to-earnings scrutiny and European defence/energy/semiconductor/industrial investment channels. Hedgeweek India rotation article (16-Nov) accessible; its reported India rebound, FPI flow, valuation and oil figures are secondary-source claims, not independently validated raw inputs. Schwab mid-year outlook (8-Jun) accessible: AI-linked earnings/index concentration, capex/earnings support, inflation/geopolitical risks and regional divergence. Franklin Templeton collection page accessible but is an index/discovery page; individual articles require separate review. Goldman Sachs PDF returned HTTP 403; content remains unverified.
- Official RBI homepage snapshot inspected: repo 5.50%, SDF 5.25%, FBIL USD/INR reference 94.1997 as at 13:00 2026-11-13; G-sec yields as at 2026-11-12: 2031 7.0289%, 2036 7.2430%, 2041 7.4011%, 2056 7.7235%; Nifty 50 25,299.35 and Sensex 81,911.01 as at 2026-11-12. Snapshot only, not a historical panel.
- Secondary Moneycontrol discovery surfaced MTD FII net +₹94,229.31 crore and DII net −₹55,570.66 crore through 18-Nov; not reconciled to official NSE/NSDL/CDSL raw files and therefore not accepted as official evidence.
- Added research-only factor-to-gate mapping across valuation, earnings, style, sector, rates, FX/carry, energy, regional TRI, institutional flows, breadth/concentration, volatility and geopolitics. Explicitly prohibits unsupported 100% causal claims, factor weights, silent currency conversion, proxy promotion, look-ahead, forward-fill and production changes.
- Report: `docs/GCR_RELATIVE_ATTRACTION_2026_MARKET_SIGNAL_MAPPING_CONTINUATION67_20261119.md`, commit `50a5c336529a1ee5d4071be7cd4046f5fc840021`.
- Decision: source review PARTIAL; factor-to-gate map DOCUMENTED (research-only); synchronized raw market panel BLOCKED; predictive edge/weights/OOS event study NOT_DONE; production integration NOT_AUTHORIZED. No protected invariant changed. NSE collector `paths-ignore` already includes `docs/**`; no workflow/script/trigger added.
- Next highest-value task: close official India FPI/DII daily cash+derivatives raw lineage (NSE/NSDL/CDSL/SEBI), with source URL, publication timestamp, provisional/final state, raw bytes and SHA-256; then reconcile sector-level flows. Do not use secondary flow summaries as PASS.

- Continuation 67 follow-on: SEBI official FPI curation directory verified NSDL/CDSL links for daily, monthly, archive, yearly and fortnightly sector-wise series. CDSL archive exposes daily gross purchases/sales/net by Equity, Debt, Debt-VRR, Debt-FAR, Hybrid and route, plus derivative trades; CDSL sector page lists fortnightly sector dates through 15-Nov-2026. NSE page provides NSE-only and combined NSE+BSE+MSEI cash-market CSV, explicitly provisional and subject to custodian confirmation. Official route discovery PASS; raw archive/schema/hash/full coverage/reconciliation NOT_DONE. Sources: https://www.sebi.gov.in/curation/fpi.html ; https://www.cdslindia.com/Publications/ArchiveDataAfter2009.aspx ; https://www.cdslindia.com/Publications/ForeignPortInvestor.html ; https://www.nseindia.com/reports/fii-dii. Report updated at docs/GCR_RELATIVE_ATTRACTION_2026_MARKET_SIGNAL_MAPPING_CONTINUATION67_20261119.md, latest report commit 5d56cfb894e587f6517d58208cc34d1e1d22b9de.


## Continuation 68 — CDSL flow freshness audit + Brazil status correction (2026-11-19)
- Important correction: Brazil registration chronology is NOT missing. Part 7 report `docs/IMF_BRAZIL_REGISTRATION_HISTORY_PART7_20261119.md` confirms exact Registration URN lifecycle 40/40 events, 40/40 transaction ZIPs HTTP 200, 40/40 embedded SDMX-ML 2.1 parses, identity match 40/40, and global index cross-check 40/40 IDs/timestamps/Registry Action. First tx667 2023-09-22T09:42:16.389Z; latest tx37877 2026-10-26T11:47:33.098Z. Registry history Action Replace and embedded RegistrationRequest action Information are distinct fields; retain both.
- Brazil remaining blocker is PA structure transaction ID 2 / Changelog only: both documented fusion-json and sdmx-json requests returned HTTP 500, body 39 bytes `Unable to return transaction for id '2'`, SHA-256 `76c4819f18129eb81b5fab80dcf0641665f332b823864c2c09280efe21415825`, report `docs/IMF_BRAZIL_PA_TX2_ALTERNATE_SERIALIZATION_PROBE_PART2_20261119.md`, run 44493473476. BOP6 vs BOP_BPM6 Dataflow mismatch remains unresolved. Do not repeat tx2 public JSON probes.
- GCR official source freshness audit: SEBI directory confirms NSDL/CDSL daily/archive and fortnightly sector routes. CDSL archive page `ArchiveDataAfter2009.aspx` displayed investment data only through 31-Oct-2026; CDSL dedicated daily page `FIIDailyData.aspx` showed investment data dated 30-Aug-2024 while derivatives were current through 18-Nov-2026; CDSL landing page last updated 18-Nov-2026 and lists fortnightly sector report through 15-Nov-2026. This proves field/page freshness asymmetry; derivative freshness must not be used as daily investment freshness.
- CDSL Nov 15 sector report explicitly separates AUC as at Oct31, period net investment Oct16–31, period net investment Nov1–15, and AUC as at Nov15. AUC is stock, net investment is flow; keep separate. No raw HTML bytes/hash or full parser validation archived yet.
- Detailed report `docs/GCR_BRAZIL_SOURCE_FRESHNESS_AND_BLOCKER_AUDIT_CONTINUATION68_20261119.md`, commit `b420dbc5b140a4873959f3c1372e9f0fd3a09d90`.
- Decision: SEBI route directory PASS; CDSL sector report availability PASS; daily investment freshness PARTIAL/BLOCKED; raw archive/parser/reconciliation NOT_DONE. Brazil 40-event Registration lifecycle PASS; PA tx2/Changelog BLOCKED; BOP6/BOP_BPM6 identity BLOCKED. No production changes or admissions.
- Next: capture NSDL archive and CDSL Nov15 sector report as immutable raw files in bounded byte-capable runner; reconcile NSE provisional vs NSDL/CDSL confirmed flows. Brazil only pursue official UI/export for PA tx2 changelog/revisions; if owner-authenticated, record external dependency rather than repeating failing endpoints.


## Continuation 69 — NSDL/CDSL FPI freshness reconciliation (2026-11-19)
- Highest-value action: re-check official daily FPI access/freshness rather than repeat already completed Brazil lifecycle work.
- SEBI official directory explicitly lists NSDL Latest, Current Month, Archive and Fortnightly sector selector URLs. Route discovery PASS.
- Direct fetches of NSDL Latest.aspx, Archive.aspx and FPI_Fortnightly_Selection.aspx returned HTTP 502 in this retrieval environment. This is an access/retrieval limitation, not evidence of missing observations or service outage.
- CDSL archive discrepancy: search-indexed official page snapshot says daily FPI investment through 18-Nov-2026; direct page open renders heading through 31-Oct-2026 and October rows. Conflicting snapshots; freshness now CONFLICT/UNKNOWN pending byte-level raw capture. Do not use derivative date 18-Nov to assert investment cash table freshness.
- Third-party public scraper README suggests NSDL pages use ASP.NET postback; FPI archive month-scoped requests and DII per-trading-day requests. This is implementation discovery only, not source evidence; do not vendor or trust its data without direct official capture.
- Detailed report `docs/GCR_NSDL_CDSL_DAILY_FPI_FRESHNESS_RECONCILIATION_CONTINUATION69_20261119.md`, commit `feb159eee99fe312b8bf23586a014867c9ce96da`.
- Brazil status unchanged/correct: 40-event Registration lifecycle PASS; PA tx2/Changelog BLOCKED after prior two documented JSON 500 responses; BOP6 vs BOP_BPM6 mismatch BLOCKED. No repeated endpoint probes.
- Next: short direct-HTTP GitHub Actions capture of official NSDL Latest/Monthly/Archive/Fortnightly and CDSL archive/sector pages, preserving raw bytes, headers, retrieval UTC, hashes and observed ASP.NET form fields before parsing. Then reconcile matched-date depository-confirmed vs NSE provisional flows. No production admission or invariant change.


## Continuation 70 — GCR official India FPI raw capture harness (2026-11-19)
- Guarded NSE collector first: commit `e51b40cff82dc4ae24a7068b74afabee35e3a370` adds the three exact research paths (workflow, script, trigger) to `paths-ignore` before any trigger commit.
- Added read-only standard-library Python GET-only capture script `scripts/research/capture_india_fpi_official_pages.py`, commit `41ecee60c32aec20a384ec11ba23023b0af7f666`.
- Added bounded 6-minute workflow `.github/workflows/gcr_india_fpi_raw_capture.yml`, commit `092ed5dd2cf78a5265bb07aa11172317ce4bee90`.
- Trigger marker commit `f2c359ce095638f1c081e4d09b3545400c071670`.
- Six official pages targeted: NSDL Latest, Monthly, Archive, Fortnightly selector; CDSL daily archive and fortnightly sector page. Capture records status, final URL, headers, UTC retrieval time, byte count, raw body and SHA-256; manifest/summary uploaded as artifact. No POST, credentials, parsing or production ingestion.
- Runtime run ID/conclusion/artifact not independently verified at ledger update time: PENDING / NOT_VERIFIED. Do not claim source capture PASS until artifact inspection.
- Brazil PA tx2/Changelog and BOP6/BOP_BPM6 identity remain BLOCKED; no repeated endpoints. Registration lifecycle 40/40 remains PASS.
- Report: `docs/GCR_OFFICIAL_INDIA_FPI_RAW_CAPTURE_HARNESS_CONTINUATION70_20261119.md`.
- No production invariants changed; ₹0; UNKNOWN is not PASS.


## Continuation 71 — CDSL current-daily FPI endpoint refinement (2026-11-19)
- Official-source discovery found CDSL eServices current daily endpoint `https://www.cdslindia.com/eservices/publications/fiidaily`; indexed official page snapshot displayed investment data on 17-Nov-2026, with gross buys/sells, net INR/USD, conversion rate and category/route splits. It distinguishes provisional exchange data from confirmed custodian/depository reports.
- CDSL archive indexed snapshot separately displays investment data through 18-Nov-2026; this does not resolve prior direct-render conflict. CDSL fortnightly sector page lists periods through 15-Nov-2026; preserve fortnightly frequency.
- Added eServices endpoint to the read-only raw capture script; commit `4bf466a6542127bbd10bfce4e1ab052c8c3b98a7`. Updated trigger marker `4bbb1bdc6be289079869a72c4ea79a460ac6b219`. Seven official pages now targeted.
- Workflow run/artifact not independently verifiable with available GitHub Actions read tools; raw capture remains PENDING / NOT_VERIFIED. No bytes or hashes claimed.
- Brazil exact PA Changelog remains an owner-side UI/export dependency; do not repeat HTTP 500 transaction endpoint. BOP6/BOP_BPM6 mismatch remains BLOCKED. Registration lifecycle 40/40 PASS.
- Report: `docs/GCR_DAILY_FPI_ENDPOINT_REFINEMENT_CONTINUATION71_20261119.md`. No production invariants changed; ₹0; UNKNOWN is not PASS.


## Continuation 72 — India FPI raw capture execution and schema audit (2026-11-19)
- Verified workflow run #2 / ID `44515445620`, workflow `GCR Official India FPI Raw Page Capture`, push event on `4bbb1bdc6be289079869a72c4ea79a460ac6b219`: completed SUCCESS. Job `capture` and all steps SUCCESS.
- Artifact ID `14524707532`, `gcr-india-fpi-raw-pages-2`, 184,876 bytes. GitHub digest and independently recomputed ZIP SHA-256 both `29530f3d0913f3eed93afbeb0759ecb8131b4192c71e5928d79961df77c24c69`.
- Manifest: seven official pages, 7/7 HTTP 200, 0 non-200/error; GET-only; UTC retrieval timestamps, response headers, byte counts and per-file SHA-256 retained. Full source hashes and findings in `docs/GCR_INDIA_FPI_RAW_CAPTURE_SCHEMA_AUDIT_CONTINUATION72_20261119.md`.
- Schema findings: NSDL Latest contains 19-Nov-2026 daily cash and separate derivative tables, but explicitly distinguishes provisional exchange-member T-day data from confirmed custodian/depository previous-day(s) data; status mapping must be explicit. NSDL Monthly heading 19-Nov but first visible row 02-Nov. NSDL Archive initial GET has no rows and requires ASP.NET date selection/postback (not attempted). NSDL fortnightly selector exposes 15-Nov-2026 onward dates but is not the sector data itself.
- CDSL eServices cash table first row 18-Nov-2026: equity/stock-exchange gross purchases ₹21,092.53cr, gross sales ₹15,177.67cr, net ₹5,914.86cr, USD 632.1301m, conversion 93.5703. Raw schema includes category, route, gross/net INR, USD and conversion. CDSL archive cash table starts 02-Nov although page title says upto 18-Nov; its derivative table is 18-Nov. Do not attribute derivative freshness to cash data. CDSL fortnightly landing page embeds DDP pendency tables and links separate 15-Nov sector report; landing is not sector observation dataset.
- Raw capture execution, artifact integrity and 7/7 HTTP 200 are PASS. Schema discovery PARTIAL PASS. Cross-provider matched-date reconciliation NOT_DONE; confirmed/provisional mapping PARTIAL; sector observation capture NOT_DONE; India production ingestion BLOCKED.
- Brazil unchanged: Registration lifecycle 40/40 PASS; PA tx2 Changelog and BOP6/BOP_BPM6 identity BLOCKED. No repeat probes.
- Next: GET-only capture of exact CDSL 15-Nov-2026 sector report; then matched-date NSDL/CDSL cash-flow reconciliation with status, asset class, route, units, conversion and reporting-date controls. No production admission.
- Protected invariants unchanged; ₹0; UNKNOWN is never PASS.
- Detailed report commit: `b7f5896459c7710af3b12c369a072062129c86a2`.


## Continuation 73 — exact CDSL 15-Nov-2026 sector report capture (2026-11-19)
- Official CDSL landing page revealed the exact dated report URL: `https://www.cdslindia.com/publications/FII/FortnightlySecWisePages/Nov%2015%202026.html`. The report separates AUC as of 31-Oct, net investment 16–31 Oct, net investment 1–15 Nov, and AUC as of 15-Nov; asset classes and INR crore/USD million are separately labelled. It is a fortnightly sector dataset, not daily cash-flow observations.
- Added exact dated URL to GET-only capture script; script commit `0c4a2115b38c4b70eda0fb404858f57dea35d159`; trigger marker commit `abb848a203bd21d0be03fd8eaa2362edc8028953`.
- Actions run `44519322726` was observed IN_PROGRESS at checkpoint time; artifact pending. Do not claim capture PASS until job/artifact/hash verified.
- Detailed report `docs/GCR_CDSL_15NOV2026_SECTOR_REPORT_CAPTURE_CONTINUATION73_20261119.md`, commit `94626aca617e5977ea0f61401118f63858f31eee`.
- India matched-date NSDL/CDSL flow reconciliation NOT_DONE; sector raw capture PENDING. Production ingestion BLOCKED.
- Brazil unchanged: Registration lifecycle 40/40 PASS; PA tx2 Changelog and BOP6/BOP_BPM6 identity BLOCKED; owner-side exact PA GUI/export remains required. No repeat tx2 endpoint probes.
- Protected invariants unchanged; ₹0; UNKNOWN is never PASS.

- Continuation 73 runtime addendum: run `44519322726` SUCCESS; artifact `14527092174`, 196,057 bytes; GitHub digest = recomputed ZIP SHA-256 `83048ea0bc712b6a453270f8fb5c3c6755b579857ff2ad9eb7d53c8ba1778fbd`; manifest 8/8 HTTP 200. Exact 15-Nov sector HTML 327,522 bytes, SHA-256 `3f77f3896a95b8cff3a7728049127493814e1b503eb39dcb75b0e8fe145cf84e`; main sector table 24 numbered rows plus grand total. Detailed report updated at commit `ce9633ccba058f8898ad9c4308d571929524fee6`.
- Exact sector page raw capture/schema inventory PASS; independent arithmetic, sector mapping and matched-date daily flow reconciliation NOT_DONE. Production remains BLOCKED.


## Continuation 74 — India FPI matched-date reconciliation audit (2026-11-19)
- Independently inspected raw HTML inside artifacts 14524707532 and 14527092174; both ZIP hashes match GitHub artifact digests.
- NSDL Latest displays reporting date 19-Nov-2026: gross purchases ₹22,356.99cr, gross sales ₹14,591.05cr, net ₹7,765.94cr, USD 831.87m.
- CDSL eServices cash table displays 18-Nov-2026: gross purchases ₹29,344.36cr, gross sales ₹16,797.46cr, net ₹12,546.90cr, USD 1,340.906m, conversion 93.5703.
- Dates differ; matched-date provider reconciliation NOT_COMPUTABLE. Within-source arithmetic matches on each page; this is not cross-provider validation. NSDL explanatory note distinguishes provisional exchange T-day from confirmed custodian/depository previous-day data, but captured table itself is not status-split; status mapping PARTIAL.
- Critical archive instability: artifact 14524707532 CDSL archive body 297,824 bytes / SHA-256 fc95dc0dade735c9f413ef20a3239e138a6064f2694633aa9635864fd8c7ba2b contains 13 cash dates 02–18 Nov; artifact 14527092174 same URL HTTP 200 body 73,784 bytes / SHA-256 aa2a03c6621772e52b0b9ac52f11b525d82f1ce80539554302eda861145304df contains only 02-Mar-2026. Do not treat HTTP 200 as archive completeness; no merge/imputation.
- CDSL dated sector report remains fortnightly and AUC (stock) separate from net investment (flow); not a daily bridge.
- Detailed report `docs/GCR_INDIA_FPI_MATCHED_DATE_RECONCILIATION_CONTINUATION74_20261119.md`, commit `388c588166d8f9a9fa462b803c8342ed6188f342`.
- India status: raw capture/hash PASS; within-source arithmetic PASS; matched-date provider comparison NOT_DONE; archive completeness BLOCKED; production ingestion BLOCKED.
- Brazil unchanged: Registration lifecycle 40/40 PASS; PA tx2 Changelog and BOP6/BOP_BPM6 identity BLOCKED; no endpoint repeats. No production invariant changes; ₹0; UNKNOWN is never PASS.


## Continuation 75 — Brazil Dataflow identity/access boundary + GCR archive replay (2026-11-19)
- Official IMF Registrations page lists Brazil provider IMF:BR1 under IMF:BOP6(1.0) and the BCB SDMX URL; other providers are registered under IMF:BOP_BPM6(1.0). IMF Reporting Constraints lists BOP_BP6_CONSTRAINT targeting BOP_BPM6[1.0]. These are distinct registration/dataflow references, not proof of equivalence.
- IMF SDMX Central Web Services Guide (May 2025) documents public GET structure queries and states registration/re-registration is private, requiring admin/agency/data-provider access and authenticated POST. Its example separates Dataflow IMF:BOP_BPM6(1.0) from DATA_DOMAIN BOP6; do not confuse domain code with Dataflow ID. This is a useful hypothesis, not a Brazil-specific crosswalk.
- Brazil identity remains BLOCKED: PA IMF:BR_BOP_BP6(1.0) -> IMF:BOP6(1.0), provider IMF:BR1, while BCB payload declares IMF:BOP_BPM6(1.0). No official alias/map or Brazil PA changelog closure evidence obtained. Exact PA revision export and provider-side authoritative mapping/correction evidence remain required.
- Detailed report `docs/BRAZIL_IMF_DATAFLOW_IDENTITY_ACCESS_BOUNDARY_CONTINUATION75_20261119.md`, commit `030bc37c0495244af3888accc069e1b7b26f1a33`.
- GCR controlled CDSL archive replay trigger commit `85e89033c37c6f5f00071446c195b00694c16af9`; Actions run `44521501249` was IN_PROGRESS at checkpoint time; no artifact/hash/conclusion claimed yet.
- No production changes; ₹0; UNKNOWN is never PASS; all invariants preserved.


- Continuation 75 GCR archive replay: run `44521501249` SUCCESS; artifact `14527843295`, 195,431 bytes; ZIP SHA-256 / GitHub digest `2c8952476f58637c0f346e695793d2b8c8fd170dac551386ace1e37e0e7aea99`; 8/8 HTTP 200.
- CDSL archive replay body 70,430 bytes, SHA-256 `3cd92be518721d84e697d42e3f2f8dc8cd6a03df6efea75a3576bf384132c2ec`, visible date 01-Jul-2021 only. Same archive URL across three captures returned (a) 13 dates 02–18 Nov-2026, (b) one date 02-Mar-2026, (c) one date 01-Jul-2021; all HTTP 200. Initial GET is not stable complete archive export; exact date selection semantics must be established before extraction. Do not infer coverage or merge snapshots.
- Detailed GCR replay report `docs/GCR_CDSL_ARCHIVE_CONTROLLED_REPLAY_CONTINUATION75_20261119.md`, commit `2bbad10a038820572adb05e40d68dc3a39dafc6e`.
- Brazil official IMF access boundary: public structure GET queries are distinct from private authenticated registration/re-registration POST; BOP6 DATA_DOMAIN in IMF guide example is not the same field as Dataflow BOP_BPM6. No Brazil-specific crosswalk; PA Changelog and BOP6/BOP_BPM6 identity remain BLOCKED. Detailed report latest commit `e91ec3d3f5a5cd519be289509359aa354bd50f39`.


## Continuation 39 — Part-5: Brazil public structure artifact independent audit (2026-11-19)
- Run 44533595369 / run #36 SUCCESS; job probe SUCCESS. Structure GET, RSS capture and artifact upload succeeded; prior lifecycle steps skipped by design. Artifact 14534769007; 7,648,050 bytes; ZIP SHA-256 = GitHub digest `4a235de4fdd1624bac3526c01f0940d05b4ef23fb435db619b4542dcd467666e`.
- Four official IMF public structure responses: 4/4 HTTP 200 and SDMX 2.1 XML parse PASS. Individual raw hashes/bytes and manifest are recorded in `docs/IMF_BRAZIL_PUBLIC_STRUCTURE_ARTIFACT_AUDIT_CONTINUATION39_PART5_20261119.md`.
- Brazil PA `IMF:BR_BOP_BP6(1.0)` -> Dataflow `IMF:BOP6(1.0)` and Provider `IMF:BR1`. BOP6 label is “Balance of Payments (BPM6) for Collection”; BOP_BPM6 label is “Balance of Payments -- BPM6”. Both use `IMF:ECOFIN_DSD(1.0)`, but remain distinct Dataflows with separate constraints. Shared DSD is not equivalence or alias.
- BOP6 response includes Chile `IMF:CL_BOP(1.0)` -> CL2 and IMF `IMF:IMF_BOP6(1.0)`; BOP6 is not Brazil-only. This does not resolve the BCB payload header `IMF:BOP_BPM6(1.0)` vs Brazil PA Dataflow `IMF:BOP6(1.0)`.
- RSS raw feed 31 entries / 0 Brazil matches for this capture window; not a full chronology. PA transaction ID 2 still HTTP 500 in both documented serializations; no equivalent retries.
- Decision: public structure evidence PASS; Brazil identity BLOCKED / UNRESOLVED; PA Changelog and full event chronology remain external owner/provider evidence dependencies. Exact next requirement is official owner-side PA revision export, dated BR1 event rows and a Brazil-specific mapping/correction if one exists.
- Report commit `93258ce505dca1dd45af758664cc4ab0e7688ac5`; master checkpoint commit `073d60722ed1d9cb3949cbc8ed186463d6057ebd`. Preserve ₹0, no credentials, no aliases, no production changes, UNKNOWN is not PASS.


## Continuation 39 — Part-5: Brazil public structure artifact audit (2026-11-19)
- Run 44533595369 / run #36 SUCCESS; job probe SUCCESS. Structure GET, RSS capture and artifact upload succeeded; prior lifecycle steps skipped. Artifact 14534769007; 7,648,050 bytes; ZIP SHA-256 = GitHub digest `4a235de4fdd1624bac3526c01f0940d05b4ef23fb435db619b4542dcd467666e`.
- Four official IMF public structure responses: 4/4 HTTP 200 and SDMX 2.1 XML parse PASS. Individual raw hashes/bytes and manifest recorded in `docs/IMF_BRAZIL_PUBLIC_STRUCTURE_ARTIFACT_AUDIT_CONTINUATION39_PART5_20261119.md`.
- Brazil PA `IMF:BR_BOP_BP6(1.0)` -> Dataflow `IMF:BOP6(1.0)`, Provider `IMF:BR1`. BOP6 label “Balance of Payments (BPM6) for Collection”; BOP_BPM6 label “Balance of Payments -- BPM6”. Both use `IMF:ECOFIN_DSD(1.0)`, but are distinct Dataflows with separate allowed constraints. Shared DSD is not equivalence or alias.
- BOP6 response includes Chile PA `IMF:CL_BOP(1.0)` -> CL2 and IMF `IMF:IMF_BOP6(1.0)`; BOP6 is not Brazil-only. BCB payload header remains BOP_BPM6 vs Brazil PA Dataflow BOP6; mismatch remains BLOCKED.
- RSS 31 entries / 0 Brazil matches in this captured window only. PA transaction ID 2 still HTTP 500 in both documented serializations; no equivalent retries.
- Report commit `93258ce505dca1dd45af758664cc4ab0e7688ac5`; independent checkpoint update commit `8c67305d079b4f4b918ebb10aa05230395395d14`.
- Next Brazil evidence dependency: authorized owner/provider export of PA revision/changelog and dated BR1 registration events, plus official Brazil-specific mapping/correction if one exists. No credentials, cookies or authenticated write. ₹0; no aliases; no production changes; UNKNOWN is not PASS.


## Continuation 39 — Part-6: Chile BDE portfolio vintage access audit (2026-11-19)
- Official BDE public SDMX_BOP6 table exposes quarterly observations through 2026-Q3 and detailed portfolio-liability categories (debt securities, equity securities and sector splits). Current-vintage category discovery PASS; not an old-vintage archive.
- Official BDE API docs state REST SearchSeries/GetSeries require a valid personal API Key Token. Endpoint and metadata/observation fields documented; no token was available and no authenticated call attempted.
- Exact assets/liabilities series IDs, 07-Sep-2026 vintage bytes, 18-Nov raw capture and row-level IMF P_F bridge remain NOT_DONE/BLOCKED. Preserve Q1/Q2 as REVIEW_VINTAGE_MISMATCH; no numeric revision bridge inferred from publication calendar.
- Report commit `3b61a10b1d788800661673afb8ef3d0a167b7918`; Master Evidence Checkpoint commit `c05730c0237077a88b22aaf3e7636aff6a1f2821`.
- Brazil remains identity BLOCKED (PA BOP6/BR1 vs BCB BOP_BPM6) pending official provider-side PA Changelog and mapping evidence. No txId=2 retries. ₹0; no production changes; UNKNOWN is not PASS.


## Continuation 39 — Part-7: Brazil IMF registry and independent BCB portfolio feeds (2026-11-19)
- Public IMF SDMX Central Registrations row confirms current `IMF:BOP6(1.0)` / `IMF:BR1` and registered BCB URL, last updated 2026-10-26T11:47:29Z. Corroborating registry evidence only; it does not prove BOP6/BOP_BPM6 equivalence, payload's internal declaration or historical actions.
- New BCB/Depec ODbL dataset path: SGS 22905 broad portfolio net; 22906 portfolio financial-asset net acquisition; 22925 portfolio liability net incurrence inflows; 22940 portfolio debt-security inflows. Public 22905 JSON visible through Sep-2026, but no immutable raw archive/hash in this task.
- Report commit `22260e4b98e0346198281b1987b4739128aa277b`; checkpoint commit `7c1dece681cae79df262aebd43526162303a9a49`.
- Next: short, separate raw-ingestion/QA jobs for each SGS family, then exact instrument/sign mapping. Brazil PA chronology still BLOCKED; GCR panel/score NOT_READY. ₹0; no production integration; UNKNOWN is not PASS.

## Continuation 39 — Part-8: bounded Brazil SGS capture workflow (2026-11-19)
- Research-only collector script added for BCB SGS 22905/22906/22925/22940 with raw response archival, provenance headers/UTC/bytes/SHA-256 and fail-closed schema/date/duplicate/ordering QA.
- Separate five-minute GitHub Actions workflow added; NSE collector paths-ignore updated before workflow creation to prevent the full NSE job running. No production logic changed.
- Commits: isolation `6e975b7f375fed914c626eda92b4fcd9e87f7b80`; script `d0a545fb54bea345bf2e4b94c6644310ce09a7bf`; workflow `4e0ef24ac94990e7b34d2c73099414310537071f`; report `68fca473ce92eb4df141fc427875344fb575ade3`.
- Run `44538278638` queued at latest poll; artifact/raw capture/QA NOT_DONE until completed and independently checked. No false PASS.
- Next: poll this run only; then hash-verify artifact, reconcile exact flow semantics and IMF mapping. Brazil PA identity/chronology BLOCKED; GCR panel/score NOT_READY. ₹0; protected invariants unchanged.


## Continuation 39 — Part-8 verified outcome: BCB SGS raw archive PASS (2026-11-19)
- Run `44538278638` SUCCESS; artifact ID `14535963861`; ZIP 11,211 bytes; SHA-256 `ee226a0525edd6974b8e0f3205005d3d5913f3014137065b074890b353ecdf60`.
- Four raw series independently verified: 22905 hash `bc2077cd9439b9a846984641934f678eaf25e3c79ce3d996362159ef74a587f3`; 22906 `110477090f5ff3e9f4e4d2ce235082d837020603b13795dbc2bde20769a3db30`; 22925 `807652fcfc3e17a710ba6dffcb78208bc41c10ec6c2f18986b61e832c6ebd2e0`; 22940 `451cc29b67f2634ac5d62439b30f11297fdab236ec42948f1db16f681eafb033`. Manifest hash `c000fe9dec4d77fed1ac85ca5d416df8cf43c3ab3ff084381aa10017cf61c062`.
- Each series 381/381 valid rows (1995-01 to 2026-09), no duplicate dates, chronological ordering PASS. Raw hashes recomputed independently from ZIP and match manifest. This is raw capture/structural QA PASS, not IMF mapping or overall GCR PASS.
- Report commit `3d59e6653f69d201ea5bb5bb2e025b49abe47ad0`. Brazil PA identity/chronology remains BLOCKED; GCR country panel/score NOT_READY. ₹0; no production changes.


## Continuation 40 — Part-1: Brazil BCB liability gross-to-net integrity (2026-11-19)
- Official SGS 22924 (net liabilities), 22925 (liability inflows), 22926 (liability outflows) monthly identity `22924 = 22925 - 22926` independently checked for 381/381 months, 1995-01–2026-09.
- Run `44538706864` SUCCESS; artifact `14537491095`; ZIP SHA-256 `69c0b92a5f5bc7221fde47a75a879e3f7c1bf8e0c4727c5299356204dd70aaa1`. Max residual 0.1 USD million, tolerance 0.15; no missing months.
- Raw hashes: 22924 `2064005a5dd42b83ba66aeb21de983ca4286af9662f57c23971b4b7dfe295dbb`; 22925 `807652fcfc3e17a710ba6dffcb78208bc41c10ec6c2f18986b61e832c6ebd2e0`; 22926 `519fcd8c068716f80f300202a1ae970fbcf312cfcd902f147143ccc5b4031e8e`.
- Report `docs/BRAZIL_BCB_PORTFOLIO_LIABILITY_IDENTITY_AUDIT_CONTINUATION40_PART1_20261119.md`, commit `ec7f41f9c9383ef5669e653ae4e4ba04f779124f`.
- Result is a BCB source-integrity PASS, not IMF PA identity resolution or GCR aggregate approval. ₹0; no production changes; UNKNOWN is not PASS.


## Continuation 41 — Part-1: Brazil BCB asset gross-to-net integrity (2026-11-19)
- BCB SGS 22906 (net asset acquisition), 22907 (asset inflows), 22908 (asset outflows). Empirical result: `22906 = 22908 - 22907`, 381/381 monthly PASS (1995-01–2026-09); reverse sign 0/381. Max residual USD 0.1m; tolerance USD 0.15m.
- Run `44539091458` SUCCESS; artifact `14535754997`; ZIP SHA-256 `8849f91e5a28d3c7e90a3df1cdcdb46c1fc66bb22ce54af8ea20ebbeca05761b`.
- Raw hashes: 22906 `110477090f5ff3e9f4e4d2ce235082d837020603b13795dbc2bde20769a3db30`; 22907 `920aea58c2a7f90106cfeef25b29b077e66d0f65efa73237ba82be34b8885c7a`; 22908 `7ef8ee458ceae80914183c49334409f175891e0d30d280ad1d513e684c6dc73e`.
- Combined BCB internal identities: assets 381/381 and liabilities 381/381 = 762/762; not independent IMF comparisons and gross legs must not be double-counted in GCR.
- Report `docs/BRAZIL_BCB_PORTFOLIO_ASSET_IDENTITY_AUDIT_CONTINUATION41_PART1_20261119.md`, commit `d5ac88260eb6e334cc99b00007f4fb77a6562ef0`.
- IMF Brazil PA/Dataflow identity and revision chronology remain BLOCKED/NOT_DONE; GCR full EMDE aggregate not authorized. ₹0, no production changes.


## Continuation 42 — Part-1: Brazil IMF public transaction-history boundary (2026-11-19)
- Public `/ws/registry/tx/history?urn=...` returned one shared structure event for PA `IMF:BR_BOP_BP6(1.0)`, Dataflow `IMF:BOP6(1.0)`, and Dataflow `IMF:BOP_BPM6(1.0)`: tx ID 2, Replace, Structure Submission, 2023-09-22T08:26:09.491Z. HTTP 200 for all; identical raw 80-byte body SHA-256 `335149e69147d8b99c9c6b5d0303cdb3b72401510b5bfed64cb3f519ced0b411`.
- Run `44539721149` SUCCESS; artifact `14537831415`; ZIP SHA-256 `042b32108ccbf42dc906af2b616ce7d5a91abdf5065448c8b96abcec9a5ccf0e`; manifest SHA `3003c20193b5c5518e09555e125c9f91a467cc430f713008d617bfeb91c4af2b`.
- Transaction-detail lookup HTTP 500 (parameter error); prior txId=2 detail attempts already failed, so no repeat. This history does not prove BR1 data-registration chronology or PA/payload Dataflow equivalence. Brazil Reconstruction remains BLOCKED.
- Report `docs/IMF_BRAZIL_PUBLIC_REGISTRY_HISTORY_PROBE_CONTINUATION42_PART1_20261119.md`, commit `676f5d771a6f9abc5d7ddbd8fd6b53fde367456a`. ₹0; no production changes; UNKNOWN is not PASS.


## Continuation 43 — Part-1: Brazil 40-event registration lifecycle integrity audit (2026-11-19)
- Reused immutable prior run `44465947951`, artifact `14502380926`; original ZIP SHA-256 independently rechecked: `2a3266a0c2d3e1948955e9de789c2a3f9acb5ecd12ffca42cd54bbad0bb37f41`. No IMF/BCB source re-fetch.
- Added fail-closed offline verifier `scripts/research/audit_imf_brazil_registration_history_artifact.py`; independent execution on original ZIP PASS.
- 40/40 history rows and transaction XMLs verified; 40 unique IDs, chronological 2023-09-22 09:42:16.389 UTC through 2026-10-26 11:47:33.098 UTC. All 40 XMLs independently carry same Registration ID `D429E36CD161E2F2A34ECAF137994E89`, PA `IMF:BR_BOP_BP6(1.0)`, and exact BCB registered URL. Timestamp minus Registration@lastUpdated is +0.460 to +15.037 seconds.
- Distinguish layers: registry Action Replace 40/40; embedded RegistrationRequest action Information 40/40. Event-index Type missing in 39 rows, but all 40 XMLs contain Registration element; classify index Type as omitted, not different event type.
- Report: `docs/IMF_BRAZIL_REGISTRATION_LIFECYCLE_INTEGRITY_AUDIT_CONTINUATION43_PART1_20261119.md`; commit `45e2965f0585842c01e1046d2744f439e9298467`.
- Returned 40-event snapshot integrity now PASS. It does not prove events outside returned set or resolve PA `BOP6` vs payload `BOP_BPM6`; Brazil Reconstruction remains BLOCKED pending official PA Changelog/owner-side crosswalk. GCR full panel/score remains NOT_READY. No production changes; ₹0; UNKNOWN is not PASS.


### Audit execution boundary / failed CI attempts (Continuation 43)
- Offline verifier passed locally against the original downloaded ZIP with the exact expected SHA-256. The optional GitHub Actions wrapper was not accepted as a PASS: run `44540443480` failed because `gh run download` extracted the artifact directory instead of creating the ZIP path expected by the script; run `44540559439` completed with zero jobs. The unverified wrapper workflow was deleted in commit `960d509e2b17532dddb7fea91ba2cc6d141e72b9`. Keep the Python verifier and report; do not cite an Actions PASS for this audit.


## Continuation 44 — Part-1: Official SDMx-BOP 2.6.0 capture and legacy compatibility boundary (2026-11-19)
- Captured official IMF-maintained `IMF:BOP(2.6.0)` from SDMx Global Registry in SDMX-ML 2.1 and 3.0. Both HTTP 200 and XML parse PASS.
- Run `44541286036` SUCCESS; artifact `14537633127`; ZIP SHA-256 (independently recomputed, matches GitHub digest) `b3475f7271324bf4577b5e99337c710e5defffe4f0244f1c8401e7b42b35e682`.
- Raw 2.1: 30,286 bytes, SHA-256 `2b467382bc5a8dfaab3df9bccb18ac8326f52fb4111c197a54f94783a742c644`; raw 3.0: 25,602 bytes, SHA-256 `f54c4ca1beea49674481e75c009c9ebec24373091cdb1906faeb03973f626940`.
- Offline comparison to reused archived `IMF:ECOFIN_DSD(1.0)`: legacy 6 dimensions / 5 attributes; BOP 2.6.0 18 dimensions / 15 attributes; both use OBS_VALUE. New model has 17 non-time dimensions incl. sector, accounting entry, functional category, instrument, maturity, currency and valuation. This is material model change; no name-only crosswalk.
- Official maintenance policy says new versions do not automatically invalidate prior versions. BOP 2.6.0 is not evidence of BOP6/BOP_BPM6 alias or Brazil migration. PA/BR1 adoption not proven; Brazil mismatch remains BLOCKED.
- Report: `docs/SDMX_BOP_260_LEGACY_ECOFIN_COMPATIBILITY_AUDIT_CONTINUATION44_PART1_20261119.md`, commit `8c15f7423643ac1ffdcbe6202d0da3a1f4d5d60b`.
- GCR country coverage/vintage/BPM gates remain blocked; no aggregate/production. ₹0; no production changes; UNKNOWN is not PASS.


## Continuation 45 — Brazil BCB asset gross-flow identity (2026-11-19)
- Official BCB series 22906 (asset net), 22907 (asset inflows), 22908 (asset outflows) identified from official dataset metadata; each API response HTTP 200, parse PASS, 381 unique monthly observations, 1995-01 through 2026-09.
- Research run `44542385747`, commit `e12cc14ff8d7d05ac8a3d30728cf87704f5ce5bd`, job `135623875310`, artifact `14537524166`, artifact SHA-256 `7ae136fc9088568f576edf67906fed7c6a3de98ffa8f17ae83e09ef01933d2f3`.
- Raw SHA-256: 22906 `110477090f5ff3e9f4e4d2ce235082d837020603b13795dbc2bde20769a3db30`; 22907 `920aea58c2a7f90106cfeef25b29b077e66d0f65efa73237ba82be34b8885c7a`; 22908 `7ef8ee458ceae80914183c49334409f175891e0d30d280ad1d513e684c6dc73e`.
- Tested orientation 22906 = 22907 − 22908: 0/381 PASS, 381 FAIL, max absolute residual 170,488.0 USD million at tolerance 0.15. This is a genuine FAIL for the tested orientation, not evidence for the opposite orientation. Must evaluate both signs on archived raw data and confirm official BCB sign semantics before acceptance.
- Report: `docs/BRAZIL_BCB_ASSET_GROSS_FLOW_IDENTITY_CONTINUATION45_20261119.md`; commit `fbcab345578b24db84358c90c5cbf3efca1de619`.
- Asset-side gross-flow decomposition remains BLOCKED. Liability-side 381/381 PASS and prior 94/94 quarterly cross-source benchmark remain separate evidence and do not substitute for this identity. Brazil PA/dataflow mismatch remains BLOCKED; GCR panel/score remains NOT_READY. No production changes; ₹0; UNKNOWN is not PASS.


### Continuation 45 — Brazil asset-side gross-flow identity (2026-11-19)
- PASS: official BCB SGS 22906/22907/22908 identity `22906 = 22908 - 22907`, 381/381 months from 1995-01 to 2026-09; max residual 0.1 USD million; tolerance 0.15; opposite sign convention rejected 0/381.
- Run #2 / ID 44542505681 SUCCESS; job 135624309676; artifact 14538393352; ZIP SHA-256 `51ab88b418ebbaa88595a45eb2a94cf8507c454c3c637075b935c8de07dcf762`.
- Raw series SHA-256: 22906 `110477090f5ff3e9f4e4d2ce235082d837020603b13795dbc2bde20769a3db30`; 22907 `920aea58c2a7f90106cfeef25b29b077e66d0f65efa73237ba82be34b8885c7a`; 22908 `7ef8ee458ceae80914183c49334409f175891e0d30d280ad1d513e684c6dc73e`.
- Failed prior sign-convention attempt run 44542407481/artifact 14537174964 is retained as rejected formula evidence; do not repeat.
- Report: `docs/BRAZIL_BCB_ASSET_SIDE_GROSS_FLOW_IDENTITY_AUDIT_CONTINUATION45_20261119.md`; commit `dd8dd1f4342f089eecd7bf0982354cc1590e3386`.
- Brazil PA/Dataflow discrepancy remains BLOCKED; GCR panel/vintage/relative-attraction gates remain BLOCKED. No production changes.

## Brazil asset-side gross-flow audit — Continuation 45 (2026-11-19)
- Official BCB series index hierarchy confirms portfolio-investment assets: SGS 22906 net (líquido), 22907 revenue/receipts (receita), 22908 expenditure/payments (despesa). Correct identity tested: 22906 = 22908 - 22907. Official index: https://dadosabertos.bcb.gov.br/pages/temas
- Run 44542572111 completed with capture+artifact upload; strict reconciliation correctly returned failure / REVIEW rather than PASS. Artifact ID 14538838057; ZIP SHA-256 57ab33277c5e1a2ea2a9a2778bc2d1d8f6fc6bfd69c70c061c2df42a318ecb20.
- Three official series each HTTP 200, parse PASS, 381 monthly observations, 1995-01..2026-09, no duplicate or missing months. Raw hashes: 22906 110477090f5ff3e9f4e4d2ce235082d837020603b13795dbc2bde20769a3db30; 22907 920aea58c2a7f90106cfeef25b29b077e66d0f65efa73237ba82be34b8885c7a; 22908 7ef8ee458ceae80914183c49334409f175891e0d30d280ad1d513e684c6dc73e.
- 275/381 exact identity matches; 106/381 have residual magnitude USD 1 million; maximum residual USD 1 million. Do not widen 0.15 tolerance or label these as rounding without official BCB precision/method evidence. Status PARTIAL / REVIEW.
- Initial run 44542407481 revealed decimal parser and sign errors; corrected in commit 3724511ffb35592b0c5dc24d856a09d5f9703ca7. Initial malformed calculations are rejected and not accepted as evidence.
- Full report: docs/BRAZIL_BCB_PORTFOLIO_ASSET_GROSS_FLOW_IDENTITY_AUDIT_CONTINUATION45_20261119.md.
- Next action: acquire official BCB methodology/precision statement and resolve only the 106 residual months. No production integration or invariant changes.


## Continuation 45 — Part-1: Brazil BCB asset gross-flow identity PASS (2026-11-19)
- BCB official SGS 22906 (asset net acquisition), 22907 (asset inflows), 22908 (asset outflows): HTTP 200; 381 valid unique monthly observations each; 381 common months; 1995-01–2026-09; no missing months.
- Verified identity `22906 = 22908 - 22907` (net acquisition = outflows minus inflows): 381/381 PASS, 0 fail, maximum absolute residual USD 0.1m, tolerance USD 0.15m.
- Parser defect found in first attempt: decimal point was removed from values (e.g. 190.5 -> 1905), causing false failures. Rejected that run. Fixed with Decimal parsing preserving decimal point; subsequent run is accepted. One escaped-newline import syntax defect was also fixed before accepted run.
- Run `44542948903` SUCCESS; artifact `14537454647`; ZIP SHA-256 independently recomputed and matches GitHub digest `5b7296d257d60ab0be49b1658e9f942b3f5827c92bb4f0ab92a052e174514969`.
- Raw hashes: 22906 `110477090f5ff3e9f4e4d2ce235082d837020603b13795dbc2bde20769a3db30`; 22907 `920aea58c2a7f90106cfeef25b29b077e66d0f65efa73237ba82be34b8885c7a`; 22908 `7ef8ee458ceae80914183c49334409f175891e0d30d280ad1d513e684c6dc73e`.
- Together with liability-side 22924=22925-22926 PASS 381/381 (Continuation 40 Part-1), both Brazil BCB portfolio gross-flow accounting identities are independently closed. IMF PA BOP6 vs BCB payload BOP_BPM6 remains unresolved; Brazil Reconstruction not 100%.
- Report `docs/BRAZIL_BCB_PORTFOLIO_ASSET_GROSS_FLOW_IDENTITY_CONTINUATION45_PART1_20261119.md`, commit `e1c2fd590cb1ec343af93bb2a7e812e80b17919d`.
- GCR country coverage/vintage/BPM gates remain blocked; no EMDE aggregate/relative-attraction score. ₹0; no production changes; UNKNOWN is not PASS.


## 9. Brazil asset-side gross-flow identity — Continuation 45 (2026-11-19)
- PASS: BCB SGS 22906/22907/22908 have 381/381 common monthly observations (1995-01–2026-09); unique identity `22906 = 22908 - 22907`; 381/381 within 0.15 USD million, max residual 0.1. Reverse sign convention 0/381.
- Raw SHA-256: 22906 `110477090f5ff3e9f4e4d2ce235082d837020603b13795dbc2bde20769a3db30`; 22907 `920aea58c2a7f90106cfeef25b29b077e66d0f65efa73237ba82be34b8885c7a`; 22908 `7ef8ee458ceae80914183c49334409f175891e0d30d280ad1d513e684c6dc73e`.
- Validator commit `90b1a68aa5c5a36f88293e4c857530268101a86c`; run `44542505681` SUCCESS; artifact `14538393352`; ZIP SHA-256 `51ab88b418ebbaa88595a45eb2a94cf8507c454c3c637075b935c8de07dcf762`.
- Failure lesson: exploratory run `44542407481` used wrong assumed sign. Preserve it as a rejected test; do not repeat. Corrected validator evaluates both candidate signs.
- Brazil registry mismatch/PA history remains BLOCKED; GCR synchronized coverage and model acceptance remain BLOCKED. No production selector/ranking/pressure/CORE-672/Engines A-E changes; ₹0; UNKNOWN is not PASS.


## Continuation 40 — Part-1: Brazil BOP 2.6.0 migration boundary check (2026-11-19)
- Reused, not repeated: Brazil registration lifecycle 40/40 PASS; current Brazil national-source benchmark 94/94; Brazil/India/Mexico/Chile vintage-aligned benchmark 118/118; official IMF SDMx-BOP v2.6.0 SDMX-ML 2.1 and 3.0 captures/parses PASS (run 44541286036, artifact 14537633127, ZIP SHA-256 b3475f7271324bf4577b5e99337c710e5defffe4f0244f1c8401e7b42b35e682).
- Reconfirmed material structural change: legacy IMF:ECOFIN_DSD(1.0) 6 dimensions/5 attributes vs IMF:BOP(2.6.0) 18 dimensions/15 attributes. No name-only crosswalk or automatic replacement.
- Live official IMF SDMX Central registrations page rendered Brazil under IMF:BOP6(1.0), provider IMF:BR1 and BCB URL; it did not show Brazil under IMF:BOP(2.6.0). Treat as rendered-page observation only, not proof no private/unpublished migration record exists. Official current DSD listing shows IMF:BOP 2.6.0; current BOP 2.6.0 dataflow overview shows the visible BPM6_BOP_M/Q and BPM6_ITS_A flows maintained by ESTAT, not evidence of Brazil/BR1 provision.
- Existing Brazil mismatch remains BLOCKED: PA IMF:BR_BOP_BP6(1.0) -> Dataflow IMF:BOP6(1.0), Provider IMF:BR1; BCB payload declares IMF:BOP_BPM6(1.0). Shared ECOFIN_DSD does not establish Dataflow identity or authorization to rewrite payload. Do not repeat PA transaction-2 JSON requests (prior HTTP 500).
- Existing IMF Data Portal legacy DSD 24.0.0 / BOP 21.0.0 tested URLs returned SDMX 404 No Results Found; error XML is not a structure capture. Do not retry same endpoints absent documented route change.
- New report: docs/GCR_BRAZIL_BOP260_MIGRATION_BOUNDARY_CHECK_CONTINUATION40_PART1_20261119.md; commit 4458be756750658a23282fd064452156e5511862.
- Status: DSD capture PASS; Brazil BOP 2.6.0 adoption UNKNOWN/NOT_FOUND_IN_RENDERED_LISTING; Brazil identity BLOCKED; legacy Data Portal ↔ Global Registry field/code crosswalk NOT_DONE/BLOCKED; GCR 154-country admission and aggregate BLOCKED.
- Next: obtain exact PA Changelog/Compare/View Provision Agreement revision export through documented GUI (authorized owner export if authentication required); separately capture legacy Data Portal DSD/dataflow/codelists only through a documented accessible route; map only exact official concept/code semantics, else NOT_MAPPED/UNKNOWN.
- ₹0, official/free sources only; no synthetic mapping, inferred alias, interpolation, zero fill, guessed timestamps/keys. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 and Engines A–E unchanged. UNKNOWN is not PASS.


## Continuation 40 — Part-2: India Q1-2026 vintage persistence + Brazil PA GUI boundary (2026-11-19)
- Reused India 12/12 historical Table197 baseline and current-vintage supplement (10/12 new comparisons PASS; 2 REVIEW; Q1-2026 liability/combined net discrepancy retained).
- New read-only RBI source check: official Table 42 pages dated 2026-06-22 (Id=24288) and 2026-07-22 (Id=24352) both visibly report Jan-Mar 2026 portfolio investment in India net = -12,121 USD million. Prior supplement also records the same value in the 2026-08-25 Table 42. RBI official table metadata states the data are subject to revision; that is a general policy, not proof this specific value changed.
- India IMF L_NIL_T remains -13,633.508347 USD million in the current panel; residual -1,512.508347 USD million against RBI -12,121. No evidence in this bounded check attributes the discrepancy to revision, scale, period, or BPM basis. Status remains REVIEW / UNRESOLVED; no forced adjustment.
- Official IMF SDMX Central GUI read-only inspection confirms Provision Agreements page controls References, Changelog, Export SDMX-ML 3.0, Export Excel, Compare, View PA; Structure Submissions exposes modification date/action/user and Download Revision/Compare. Static rendering does not populate the selected Brazil PA revision rows/changelog. A generic confirmation/re-authentication dialog is visible, but exact triggering operation is not established.
- No authentication, credentials, interactive selection, export, or mutation attempted. Brazil PA actual revision history remains NOT_OBSERVED / UNKNOWN; do not infer changelog empty or login requirement for every action.
- Brazil current PA/Dataflow/provider identity remains IMF:BR_BOP_BP6(1.0) -> IMF:BOP6(1.0), provider IMF:BR1; BCB payload still declares IMF:BOP_BPM6(1.0). Mismatch remains BLOCKED. Do not repeat transaction-ID-2 fusion-json/sdmx-json HTTP 500 endpoints.
- New report: docs/GCR_INDIA_Q1_2026_VINTAGE_PERSISTENCE_AND_BRAZIL_PA_ACCESS_BOUNDARY_CONTINUATION40_PART2_20261119.md; commit aa26d214cf0d0c316523c8041b328abe99ab7de7.
- Next: India same-vintage IMF country metadata/revision evidence; Brazil authorized owner-side exact PA Changelog/Revision/Compare export; GCR remaining country/vintage validation. No 154-member aggregate until coverage, missingness, BPM and scale gates pass.
- ₹0, official/free only; no fabricated revision attribution, synthetic data, inferred alias or forced reconciliation. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A–E unchanged; UNKNOWN is never PASS.


## Continuation 40 — Part-3: Brazil public structure artifact verification + EMDE workflow trigger hygiene (2026-11-19)
- Closed the pending Continuation 76 verification: workflow run 44533595369 SUCCESS; job 135593069697 SUCCESS; artifact 14534769007, 7,648,050 bytes, expires 2027-02-17. Downloaded artifact ZIP independently recomputed SHA-256 4a235de4fdd1624bac3526c01f0940d05b4ef23fb435db619b4542dcd467666e, exact GitHub digest match.
- Four public SDMX structure GET resources: Brazil PA, BOP6 Dataflow, BOP_BPM6 Dataflow, ECOFIN_DSD. All 4/4 HTTP 200, manifest byte counts and SHA-256 values exactly match raw files, and all 4/4 parse as SDMX-ML 2.1 Structure XML.
- Exact PA: IMF:BR_BOP_BP6(1.0); StructureUsage -> IMF:BOP6(1.0); DataProvider -> IMF:DATA_PROVIDERS(1.0).BR1. BOP6 name “Balance of Payments (BPM6) for Collection”; BOP_BPM6 name “Balance of Payments -- BPM6”. Both reference ECOFIN_DSD(1.0) but remain distinct Dataflow maintainables.
- Current returned BOP6 structure includes 5 PAs referencing BOP6 (BR_BOP_BP6, CL_BOP, IMF_BOP6, RO_BOP_BP6, SE_BOP). Current BOP_BPM6 structure includes 12 PAs referencing BOP_BPM6 (AT_BOP, BE_BOP, CH_BOP, GB_BOP, HU_BOP6, IMF_REPORT_BPM6, JP_BOP, LU_BOP, MT_BOP6, SK_BOP, US_BOP, US_BOP_BPM6); Brazil PA is not among them. These are current public response counts only, not historical completeness.
- IMF Web Services Guide (May 2025) distinguishes DATA_DOMAIN as a separate ECOFIN DSD dimension and documents registration as private/authenticated POST. It does not authorize a Brazil-specific crosswalk or prove the BCB payload DataflowRef can differ from the PA's StructureUsage.
- Transaction-ID-2 fusion-json/sdmx-json remain 2/2 HTTP 500; do not retry. RSS 31 entries/zero Brazil matches remains limited to captured feed window. Artifact does not contain BCB payload XML; selected Brazil PA Changelog/revision export not captured. PA chronology and BOP6/BOP_BPM6 identity remain BLOCKED/UNKNOWN.
- Report: docs/BRAZIL_PUBLIC_STRUCTURE_ARTIFACT_VERIFICATION_CONTINUATION40_PART3_20261119.md; report commit ae81a0d7f901e7d1a3f8e1e7cb53f84e3583efc3.
- CI issue: documentation-only pushes repeatedly triggered .github/workflows/persist_imf_emde_panel.yml with failure but zero jobs and zero artifacts (verified runs 44548677773 and 44548701772). This was not a research execution failure; the archive job never ran. The WEO/IMF panel archive is already committed.
- Retired push path trigger; workflow now manual workflow_dispatch only. Edit commit 0e9260223baf0bad766e5c68ee15568a28cfd878; workflow re-fetched and confirmed.
- Next: Brazil owner-side exact PA Changelog/Revisions/Compare export and original BCB payload raw GET capture; GCR Chile current-vintage Q1/Q2 revision matrix and India 2026-Q1 REVIEW. No 154-country aggregate while 40 members have no selected-entry observations and 83/308 country-entry cells are empty.
- ₹0, official/free only. No synthetic data, inferred aliases, credential use, registration writes, or production changes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E unchanged; UNKNOWN is never PASS.

## Continuation 40 — Part-4: Independent BCB raw payload header reparse (2026-11-19)
- Reused existing official BCB raw XML from run 44301482210 / artifact 14426565546; no duplicate network capture. Original metadata: HTTP 200, text/xml, retrieved 2026-11-18T12:11:07.589328+00:00, 4,840,062 bytes. Independent raw-byte SHA-256 3e736c45d67fe64ac8c0cb3396718addab21a1ef43d09666ae8dd8ccaba3f52c matches original manifest.
- Corrected the earlier parser blind spot: literal DataflowRef scanning returned an empty list, but exact Dataflow is encoded in root xsi:schemaLocation and Header/Structure namespace. Independent reparse confirms Dataflow IMF:BOP_BPM6(1.0), ObsLevelDim TIME_PERIOD, StructureID IMF_BOP_BPM6_1_0, and DataSet structureRef IMF_BOP_BPM6_1_0. The old empty list was parser coverage failure, not absence of a Dataflow.
- Dataset independently parsed: 237 series, 89,097 observations, DATA_DOMAIN=BOP6, REF_AREA=BR, COUNTERPART_AREA=W1, FREQ=M, UNIT_MULT=6, TIME_FORMAT=P1M; 381 monthly periods 1995-01 through 2026-09.
- This strengthens payload-side evidence but does not change admission: current PA IMF:BR_BOP_BP6(1.0) references IMF:BOP6(1.0) / provider IMF:BR1; payload declares IMF:BOP_BPM6(1.0). DATA_DOMAIN=BOP6 is a distinct dataset dimension and does not rename the Dataflow. Mismatch remains CONFIRMED / UNRESOLVED; Brazil-specific crosswalk NOT_PROVEN; Brazil Reconstruction BLOCKED.
- No new GET, no duplicate retrieval, no auth, no credential, no registry write, no alias inference. Transaction-ID-2 HTTP 500 endpoints remain excluded. PA historical Changelog/Revision remains UNKNOWN.
- Report: docs/BRAZIL_BCB_RAW_PAYLOAD_HEADER_REPARSE_CONTINUATION40_PART4_20261119.md.
- Next: authorized owner-side exact PA Changelog/Revisions/Compare + IMF:BR1 registration export; in parallel resolve GCR Chile Q1/Q2 vintage matrix and India Q1-2026 liability REVIEW. Do not publish the 154-member aggregate before coverage/missingness/BPM/scale gates pass.
- ₹0/free official sources only. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E unchanged; UNKNOWN is never PASS.
## Continuation 40 — Part-5: GCR 2026-Q2 synchronous dual-leg candidate cohort (2026-11-19)
- Reused the archived full coverage QA input `docs/evidence/imf_bop_emde_20261119/coverage_qa/coverage_by_country_entry_detailed.csv`, Git blob `1a7fd6f3e5955f08c2fcaf5a8fa81ac6b5b2f091`; parsed all 308 country-entry rows and all 154 unique WEO G200 members.
- Deterministically selected countries where both `A_NFA_T` and `L_NIL_T` have an observation for 2026-Q2, using the explicit `missing_periods` fields. Result: 63/154 countries (40.91%). For 2026-Q3 only 2/154 have both legs. Q2 is therefore the latest broad synchronous dual-leg cohort in this archived panel.
- Important count reconciliation: 61 countries have 2026-Q2 as the latest period for both legs; two additional countries (Brazil and Pakistan) also have Q3 observations but still contain Q2. The 63-country Q2 presence cohort correctly includes them; latest-period-only country_readiness would omit them.
- Added deterministic roster `docs/evidence/imf_bop_emde_20261119/coverage_qa/2026Q2_both_legs_candidate_cohort.csv` (63 rows), with every row explicitly marked `NATIONAL_SOURCE_VINTAGE_VALIDATION_PENDING` and `NOT_AUTHORIZED` for aggregate admission. Roster commit `51468ed45d8b3f831c11f4525cee955b5f3e11f8`.
- Added report `docs/GCR_2026Q2_SYNCHRONOUS_DUAL_LEG_COVERAGE_COHORT_CONTINUATION40_PART5_20261119.md`; report commit `87b5ba9755a719239ca01708a7293cf25c476ba2`.
- Panel availability cohort is a data-readiness PASS only. It does not validate national sign/scale, vintage alignment, BPM basis, or authorize a 63-country subtotal. No data values were aggregated, filled, imputed, rescaled or altered.
- Next: validate official national-source sign/scale/vintage for the 63 members, prioritize large unvalidated EMDEs; keep Chile exact portfolio vintage bridge REVIEW, India Q1-2026 liability REVIEW, and Brazil PA/Dataflow mismatch BLOCKED. No aggregate until all gates pass.
- ₹0/free official sources only. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E unchanged; UNKNOWN is never PASS.

## Continuation 41 — Part-1: India RBI/IMF Q1-2026 bounded metadata reconciliation (2026-11-19)
- Reused existing 63-country 2026-Q2 candidate cohort; India is present with both A_NFA_T and L_NIL_T panel entries. This is panel presence only, not aggregate authorization.
- Reviewed RBI Comprehensive Guide publication page (2026-10-08; April 2026 edition): Table 42 is quarterly BPM6 BoP in US$ million, sourced from RBI/DEPR, with data subject to revision; Table 44 is quarterly end-period IIP stock data and is not interchangeable with BoP flows. IMF SDDS India BOP metadata independently states BPM6 classification and financial-account assets/liabilities.
- Metadata validates the source family and revision possibility, but does not establish a specific Q1-2026 revision or explain the previously recorded residual: RBI -12,121 USD million vs IMF -13,633.508347 USD million (difference 1,512.508347 USD million). No adjustment/sign flip/stock-flow substitution authorized.
- India Q1-2026 liability remains REVIEW / UNRESOLVED; India national-source vintage/sign/scale validation NOT_YET_PASS; 63-country aggregate remains NOT_AUTHORIZED. Brazil PA/Dataflow mismatch remains BLOCKED.
- Report: docs/INDIA_Q1_2026_RBI_IMF_LIABILITY_RECONCILIATION_CONTINUATION41_PART1_20261119.md; report commit cde4d62df4786f17833d775131ca42ce86bd6116.
- Official sources: https://rbi.org.in/Scripts/PublicationsView.aspx?id=24094 ; https://dsbb.imf.org/sdds/dqaf-base/country/IND/category/BOP00 ; https://dsbb.imf.org/sdds/dqaf-base/country/IND/category/IIP00 .
- Next: retrieve exact RBI Q1-2026 Table 42 old/new vintage rows and matching IMF observation dimensions; if no public official vintage bridge exists, retain REVIEW. ₹0/free official sources only; no synthetic data or production changes; UNKNOWN is never PASS.


## Continuation 41 — Part-2: Brazil public IMF registration vs BCB payload identity cross-check (2026-11-19)
- New read-only official public listing check: IMF SDMX Central Registrations indexes Dataflow IMF:BOP6(1.0), Provider IMF:BR1, exact BCB URL, last updated 2026-10-26T11:47:29Z. Source: https://sdmxcentral.imf.org/data/registrations.html (public search-indexed registration listing).
- Reused Part-4 raw XML verification: same BCB URL's payload declares IMF:BOP_BPM6(1.0), structureRef IMF_BOP_BPM6_1_0; raw SHA-256 3e736c45d67fe64ac8c0cb3396718addab21a1ef43d09666ae8dd8ccaba3f52c. Reused PA evidence: IMF:BR_BOP_BP6(1.0) -> IMF:BOP6(1.0), Provider IMF:BR1.
- This triangulates a confirmed current identity mismatch: PA and public registration agree on BOP6; payload served at registered URL declares BOP_BPM6. This does not prove aliases or a valid Brazil-specific crosswalk. Shared DSD/DATA_DOMAIN do not establish equivalence.
- Brazil PA/payload consistency: FAIL / MISMATCH CONFIRMED; Brazil-specific crosswalk: NOT_PROVEN; historical PA change chronology: UNKNOWN/BLOCKED; Brazil Reconstruction remains BLOCKED pending authorized IMF/BCB correction or documented exception plus PA history evidence.
- Report: docs/BRAZIL_IMF_PUBLIC_REGISTRATION_VS_BCB_PAYLOAD_CONTINUATION41_PART2_20261119.md; report commit deab79c66a73a2ad060c4c9775e8c02676821a05; report blob SHA a0ebe2c859ced0639a7960f8f81dd23c84a9c89a.
- Next: owner-side PA history/Changelog and official correction/exception identifying intended Dataflow; after correction, repeat raw-byte/XML validation and require PA, registration and payload identities to agree. No credentials or authenticated writes.
- ₹0, official/free only; no inferred alias, synthetic data, or production changes; UNKNOWN is never PASS.


## Continuation 41 — Part-3: South Africa SARB Q2-2026 official source gate (2026-11-19)
- Reused existing 63-country 2026-Q2 cohort; ZAF has both A_NFA_T and L_NIL_T panel entries. No roster rebuild.
- Located SARB Quarterly Bulletin September 2026 (published 2026-09-29) and official XLSX archive index. Bulletin says Q2-2026 net financial-account capital flow +R1.9bn vs Q1 -R23.1bn; net portfolio investment and financial derivatives were outflows, while direct investment, other investment and reserve assets were inflows. This is directional net-flow context only, not validation of the two gross panel legs.
- Official archive identified: 04Kbp5-Balance-of-Payments-September-2026-updated.zip; quarterly frequency code K1. SARB June 2026 IIP publication is a separate position/stock source and must not be substituted for BOP flows.
- Exact A_NFA_T/L_NIL_T national mapping, units, signs, Q2 observations and vintage remain NOT_YET_VALIDATED. ZAF status PARTIAL / NOT PASS; aggregate remains NOT_AUTHORIZED.
- Report: docs/GCR_SOUTH_AFRICA_SARB_Q2_2026_SOURCE_GATE_CONTINUATION41_PART3_20261119.md; commit 82e8c63b46f7c7468b97a744c312dab690f10969; re-fetched blob cc04872301871d5b11954df83997c7fcab05f685.
- Next: inspect the official SARB BOP XLSX archive for exact portfolio asset/liability quarterly series, units, signs and vintage; only then compare like-for-like with IMF. ₹0, no inferred conversions/sign flips, no aggregate; invariants unchanged; UNKNOWN is never PASS.


## Continuation 41 — Part-4: SARB portfolio series-code candidates and official archive retrieval boundary (2026-11-19)
- Reused Part-3 ZAF source gate and cohort. Official SARB XLSX index confirms Bulletin No.321 September 2026, K1 quarterly, and exact archive 04Kbp5-Balance-of-Payments-September-2026-updated.zip.
- Official attachment URL resolved but ZIP retrieval timed out/failed; no bytes, hash or workbook contents claimed.
- Secondary BER Data Guide surfaced candidate codes KBP5756/5757 (portfolio liabilities: equity/debt securities) and KBP5758/5759 (portfolio assets: equity/debt securities); KBP5644 and KBP5660 are total liability/asset portfolio controls. These are discovery leads only, NOT officially verified; not admitted to national mapping.
- Official SARB Online Statistical Query page documents public KBP-code search, version selection, frequency/date range and export: https://www.resbank.co.za/en/home/what-we-do/statistics/releases/online-statistical-query .
- ZAF status remains PARTIAL / NOT PASS; official series description/version/unit/sign, Q2 observation and vintage not yet inspected; GCR aggregate NOT_AUTHORIZED.
- Report: docs/GCR_SOUTH_AFRICA_SARB_PORTFOLIO_SERIES_CODE_CANDIDATES_CONTINUATION41_PART4_20261119.md; commit a9dbcaa86bb3098f2b12851b04af6cf49769e413; re-fetched blob 615e341e1657ec052b45de0e3093d3b916816485.
- Next: verify candidate codes in official SARB query and export the exact Q2-2026 series/version metadata and values; no credentials, no guessed transforms. Secondary-source discovery never counts as PASS. Invariants unchanged; UNKNOWN is never PASS.


## Continuation 41 — Part-5: SARB official query workflow and alternate BOP archive path (2026-11-19)
- Fresh official SARB Online Statistical Query check confirms numeric KBP code input (prefix auto-added), wildcard, available-version selection, date/frequency selection, and CSV/XLSX/PDF/DOC exports. The page's controls cannot be executed by the web retrieval interface; live open timed out. No code result or export is claimed.
- Identified a second official SARB zipped-data archive index (published 2026-09-29) listing KBP5-BOPD-Sep-20.zip. Listing is confirmed; internal contents/vintage/Q2-2026 coverage not inspected. Do not infer that abbreviated filename means Sep-2026.
- Official Quarterly Bulletin index confirms September 2026 issue published 2026-09-29.
- KBP5756–5759 remain secondary-source candidates only; official series descriptions/versions/units/signs/values not yet obtained. ZAF remains PARTIAL / NOT PASS; GCR aggregate NOT_AUTHORIZED.
- Report: docs/GCR_SARB_OFFICIAL_QUERY_AND_ZIPPED_ARCHIVE_ALTERNATE_PATH_CONTINUATION41_PART5_20261119.md; commit c1b4a5e1f536b64588ed661c5da37fe14b63afcd; re-fetched blob c7e67c36d14363d45d21720f984cbd0520c57552.
- Next: use ordinary public browser UI to inspect/export codes 5756–5759 and version metadata; inspect the exact official zipped BOP attachment only to establish contents/vintage; SHA-256 exports and compare like-for-like. No credentials or guessed transformations. Invariants unchanged; UNKNOWN is never PASS.


## Continuation 42 — Part-1: GCR historical observation phase, global capital transmission into India (2026-11-19)
- User explicitly directed sequence: observation first, then planning, then organizing. This report is OBSERVATION ONLY; planning/organizing not started or approved.
- Created historical synthesis spanning 1991 reforms/1992 FPI opening; 2003–09 global liquidity/GFC; 2010–16 QE/taper/China; 2020–21 pandemic reversal/rebound; 2022 synchronous tightening/geopolitics; FY2023-24 to FY2025-26 FPI/FDI composition.
- Key evidence: RBI research studies Q1-1992 to Q1-2022 sudden stops and identifies global growth/risk/liquidity/long rates/policy changes plus domestic growth/INR as drivers; RBI forex/equity paper finds FPI transactions link equity and FX markets with regime-dependent spillovers. SEBI FY2025-26 reports total FPI net outflow ₹1,52,692 crore, equity outflow ₹1,80,832 crore, debt inflow ₹25,807 crore; RBI Annual Report reports FY2025-26 net FPI -US$16.5bn and net FDI +US$7.7bn. Do not conflate total FPI with equity, nor FDI with FPI.
- Report: docs/GCR_OBSERVATION_PHASE_GLOBAL_CAPITAL_ROTATION_INDIA_HISTORICAL_TRANSMISSION_CONTINUATION42_PART1_20261119.md; commit 0cdf3b490f20824fd9aa5f52b9d706d96c668baa; re-fetched blob 16a73d08f5be00ce60b9a13f90d5c04a82280c51.
- Important design observation: do not add every country equally. Build an exposure-weighted transmission graph (global funding/risk centres, investor domiciles, trade/commodity suppliers, demand partners, systemic peers) → India channels → sectors/markets. Country inclusion and causal weights require later measured evidence.
- Not established: country-specific causal impacts, optimal weights, predictive thresholds, 154-country necessity/sufficiency, or full validation of Brazil/India/Chile/South Africa. No production selector/score/weights/engine changed; GCR not complete; aggregate not authorized.
- Next after observation evidence inventory: produce a separate Planning-stage protocol with hypotheses, variables, sample/frequency, event windows, identification strategy, controls, vintages, acceptance criteria; only then Organizing-stage source registry/pipeline and test harness. ₹0/free official sources; UNKNOWN is never PASS.


## Continuation 42 — Part-2: India-specific historical sudden-stop episode register (2026-11-19)
- Added RBI-published India episode register for Q1:1992–Q1:2022, preserving separate flow definitions:
  - Gross capital inflows: Q4 2008–Q2 2009 (3 quarters); Q1 2016–Q2 2016 (2).
  - Gross FPI inflows: Q3 2008–Q1 2009 (3); Q1 2016 (1); Q1 2022 (1).
  - Net capital flows: Q4 2008–Q2 2009 (3); Q1 2016–Q2 2016 (2).
- RBI paper attributes the 2015–16 country-level stress grouping to August 2015 China stock-market turmoil and the first US Federal Funds rate hike in December 2015. 2013 taper tantrum and 2021 taper talks were not sudden stops under that paper's classification; this does not mean they had no market/flow impact.
- India model findings: weak global growth, higher global rates, higher global risk and INR depreciation associated with lower gross inflows; extended specification also identifies global liquidity and CAD. Separate RBI 2022 tail-risk study reports 3.2% GDP adverse-scenario and 7.7% GDP combined-shock portfolio outflow estimates; these are conditional scenario estimates, not forecasts.
- Report: docs/GCR_OBSERVATION_PHASE_INDIA_SUDDEN_STOP_EPISODE_REGISTER_CONTINUATION42_PART2_20261119.md; commit ae94f928bd1cdc7ec29ff6d98b160767a33e2d70.
- Primary sources: RBI https://www.rbi.org.in/scripts/bs_viewcontent.aspx?Id=4517 and RBI Bulletin https://www.rbi.org.in/Scripts/BS_ViewBulletin.aspx?Id=21067 .
- Limits: author calculations not independently replicated; no event-level NIFTY/Sensex/sector causal impact; no new weights or production logic. Wider Observation remains open; Planning/Organizing NOT STARTED. GCR NOT COMPLETE; aggregate NOT_AUTHORIZED.
- Invariants preserved: ₹0; no synthetic data/fabricated timestamps/guessed transforms; Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A–E unchanged; UNKNOWN is never PASS.


## Continuation 42 — Part-3: India equity-market FPI/DII transmission evidence (2026-11-19)
- Added RBI-published evidence linking unexpected FPI flows with Nifty 50/Midcap/Smallcap returns. RBI Jan-2023 Bulletin Annex 1 uses weekly normalized FPI flows, a five-variable VAR over Jan-2008–Dec-2022 and bivariate VARs before/after Mar-2015. Reported response: 2.2%–3.0% over next 2–3 months before Mar-2015, declining to 1.25%–1.50% thereafter. These are source-study normalized-shock estimates, not daily returns or one-percentage-point flow effects; not independently replicated.
- Same RBI source reports FPI ownership 23.3% (Mar-2015) to 19.0% (Sep-2022), while DII ownership rose 10.4% to 14.8%.
- RBI Financial Stability Report (2025-12-31) reports 2025 calendar-year-to-Dec-10 DII inflows ₹7.4 lakh crore vs FPI outflows ₹1.6 lakh crore; lower recent US-India co-movement/declining beta and market resilience despite outflows; tariff event response heterogeneous across sectors and trade-exposed bank issuers.
- Report: docs/GCR_OBSERVATION_PHASE_INDIA_EQUITY_MARKET_FPI_DII_TRANSMISSION_CONTINUATION42_PART3_20261119.md; commit dc61da1409ca91f3dbf343a275d047ff321db251.
- Sources: RBI Jan-2023 Bulletin https://www.rbi.org.in/Scripts/BS_ViewBulletin.aspx?Id=21533 ; RBI Financial Stability Report https://www.rbi.org.in/Scripts/PublicationReportDetails.aspx?ID=1313 .
- Limits: no independent replication/raw event-window computation, no country-specific causal path, no predictive or 1–3 day edge, no weights/thresholds; prior Brazil/India/Chile/South Africa source gates unchanged.
- Stage: this evidence increment complete; Observation overall still OPEN; Planning/Organizing NOT STARTED; GCR NOT COMPLETE; aggregate NOT_AUTHORIZED.
- Invariants unchanged: ₹0, official/free sources, no synthetic data/fabricated timestamps/guessed transforms; Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 and Engines A–E unchanged; UNKNOWN is never PASS.


## Continuation 42 — Part-4: Official high-frequency source readiness matrix for India event studies (2026-11-19)
- Completed source-discovery audit for zero-cost global-shock → India market/FX/flow event study.
- Verified official/public access paths: NSE historical index and India VIX; NSE daily reports/full bhavcopy/security delivery; SEBI page linking NSDL and CDSL FPI daily/monthly/archive; RBI DBIE daily USD/INR from 2000-08-08 to 2026-06-30 (CSV/JSON); FRED DGS10 daily US 10Y yield (US Fed Board source); FRED VIXCLS daily CBOE close; PPAC Indian Basket crude historical report (FY/monthly view).
- Key constraints: this was source discovery, not raw-data acquisition. No row counts, raw files, hashes, missingness or source vintage claimed. NSE interactive exports not run; NSDL/CDSL definitions/overlap not reconciled; NSE FII/DII report definitions pending; PPAC surfaced monthly/FY layout cannot be interpolated to daily. Different global/India close times require no-look-ahead alignment.
- Report: docs/GCR_OBSERVATION_PHASE_OFFICIAL_HIGH_FREQUENCY_SOURCE_READINESS_CONTINUATION42_PART4_20261119.md; commit 77ed90fe11aa7d66f3214bde72476c97094ed43f.
- Primary source URLs are itemized in the report. Web verification references: NSE historical reports; SEBI FPI curation; RBI DBIE USD/INR; FRED DGS10/VIXCLS; PPAC Indian Basket.
- Next bounded actions: acquire and QA separate raw datasets in short jobs (NSE index/VIX; RBI DBIE USD/INR; NSDL/CDSL FPI; NSE DII/FII; FRED global factors; PPAC monthly context). Preserve original date, publication timestamp, timezone, unit, vintage, manifest and SHA-256. No forward-fill/interpolation across missing calendars.
- Stage: source-readiness increment complete; Observation overall OPEN; Planning/Organizing NOT STARTED; GCR NOT COMPLETE; aggregate/production admission NOT_AUTHORIZED.
- Invariants unchanged: ₹0; official/free sources; no synthetic data/fabricated timestamps/guessed daily interpolation/unsupported country weights; Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A–E unchanged; UNKNOWN is never PASS.


## Continuation 42 — Part-5: NSE NIFTY 50 and India VIX raw acquisition gate (2026-11-19)
- Verified official NSE Indices Historical Data page offers index selection/date range/CSV; NSE Indices FAQ documents NIFTY 50 historical data from 1990-07-03 and distinguishes NIFTY price index vs NIFTY-TR. Official NSE India India VIX page exposes date presets/custom range and CSV download control; current server-rendered view showed no selected data / “No Records”.
- Official NSE historical reports separately list index history, India VIX history and daily/monthly indices archives. Security-level UDiFF bhavcopy is not index history.
- Inspected repository collector/nse_download.py: it handles security-level CM UDiFF/legacy bhavdata, not NIFTY index or India VIX. Existing broad .github/workflows/nse_collector.yml is 60-minute full pipeline and was not triggered for this small task.
- No raw NIFTY/VIX CSV acquired; no row counts, byte counts, timestamps, hashes, missingness or dataset PASS claimed. No unverified undocumented endpoint or third-party API pattern copied into production.
- Report: docs/GCR_NSE_NIFTY50_INDIA_VIX_RAW_ACQUISITION_GATE_CONTINUATION42_PART5_20261119.md; commit e9073fee299f96301e0c88a3a09665a0dac929ad.
- Sources: https://www.niftyindices.com/reports/historical-data ; https://www.niftyindices.com/static/products-services/indices-faqs ; https://www.nseindia.in/reports-indices-historical-vix ; https://www.nseindia.in/static/resources/historical-reports-capital-market-daily-monthly-archives .
- Next: acquire exact NIFTY 50 price-index and India VIX CSV exports through official UI or independently verified official request contract; preserve raw bytes, timestamps, byte counts, SHA-256, schema and trading-date QA. Do not use sample rows or equity bhavcopy as substitutes.
- Stage: source-route/code-boundary review complete; Observation overall OPEN; Planning/Organizing NOT STARTED; GCR NOT COMPLETE; aggregate/production NOT_AUTHORIZED.
- Invariants unchanged: ₹0; official/free sources; no fabricated timestamps, guessed endpoints, synthetic values, forward-fill/interpolation; Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A–E unchanged; UNKNOWN is never PASS.


## Continuation 42 — Part-6: NSE historical index / India VIX sample integrity review (2026-11-19)
- Rechecked official NSE All Reports page. It renders a NIFTY 50 sample block for 01–05 Jan 2019 with a row dated 01-Jan-2019 repeated twice. India VIX sample block heading also says 01–05 Jan 2019, but displayed row date is 03-Sep-2018 and is repeated twice.
- This is a static/pre-rendered page sample, not evidence of a selected-range raw CSV export. Treat duplicate rows and VIX heading/date mismatch as UI/sample rendering anomalies pending live-query/export verification; do not use sample for returns/event studies or silently deduplicate.
- This qualifies Part-5: dedicated pages show no selected-range data in server-rendered output, while All Reports separately renders example blocks. Official routes exist; raw selected-range acquisition remains NOT_DONE.
- Report: docs/GCR_NSE_HISTORICAL_INDEX_VIX_SAMPLE_INTEGRITY_REVIEW_CONTINUATION42_PART6_20261119.md; commit 47cd0c3583b0ab97921d25e1b0242073114e11b2.
- Primary source: https://www.nseindia.in/all-reports ; supporting official pages https://www.niftyindices.com/reports/historical-data and https://www.nseindia.in/reports-indices-historical-vix .
- Acceptance strengthened: archive downloaded raw bytes; verify requested date range, unique dates, duplicate count, chronology, OHLC bounds, selected index type, retrieval timestamp, final URL, content type, byte count, SHA-256 and row count; cross-check with second official route where possible.
- Status: NIFTY/VIX routes VERIFIED; sample block NOT PASS; live raw CSV NOT_DONE; hashes/row counts UNKNOWN; GCR event-study panel NOT_ACCEPTED. Observation overall OPEN; Planning/Organizing NOT STARTED; GCR NOT COMPLETE; aggregate NOT_AUTHORIZED.
- Invariants unchanged: ₹0; official/free sources; no synthetic data/fabricated timestamps/guessed endpoints/silent deduplication/forward-fill/interpolation; Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A–E unchanged; UNKNOWN is never PASS.


## Continuation 43 — Part-1: RBI India capital-flow reversal event register (2026-11-19)
- Extracted a source-grounded India-centred event register from RBI Occasional Paper "Cross-border Capital Flows and Sudden Stops: Lessons from Emerging Market Economies" (Q1-1992 to Q1-2022).
- Source-supported event labels: India GFC capital-inflow sudden stop; India country-level sudden stops during H2-2015/H1-2016 linked in the paper to Aug-2015 China market turmoil and Dec-2015 first US Fed hike; India gross-FPI sudden stop in Q1-2022. 2013 taper is an EME weekly net-FPI reversal/stress event but not a sudden stop under the paper's classification. 2020 COVID net-flow sudden-stop label applies to EMEs excluding China at aggregate level, not specifically India. 2021 taper talks had contained/limited EME net-flow impact and were not classified as sudden stops.
- RBI India cloglog evidence: weak global GDP growth, higher global risk, higher global long-term rates, US Fed Funds rate changes and INR depreciation associated with gross-capital-inflow reversal likelihood; extended model finds global liquidity lowers and domestic CAD raises reversal likelihood. Quarterly historical associations only; no daily causal coefficients, weights or thresholds.
- Report: docs/GCR_RBI_INDIA_CAPITAL_FLOW_REVERSAL_EVENT_REGISTER_CONTINUATION43_PART1_20261119.md; commit c91fa925c3b5ba7ea5e0900ea5c950221368a992.
- Primary source: https://www.rbi.org.in/scripts/bs_viewcontent.aspx?Id=4517 (RBI page sections III, IV, India Table 1, Annex Table A2).
- Limits: exact India quarter-level sub-windows from Annex Table A2 still pending; no raw daily/weekly FPI, NIFTY, VIX or FX event panel acquired; no independent event-study replication or trading edge established.
- Stage: event register increment complete; Observation overall OPEN; Planning/Organizing NOT STARTED; GCR NOT COMPLETE; aggregate/production admission NOT_AUTHORIZED.
- Invariants unchanged: ₹0; official/free sources; no synthetic data/fabricated timestamps/guessed event dates/unsupported causality; Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A–E unchanged; UNKNOWN is never PASS.


## Continuation 43 — Part-2: RBI Annex A2 India sudden-stop evidence-limit audit (2026-11-19)
- Reopened the official RBI paper directly and verified the body-text findings: India GFC capital-inflow sudden stop; India country-level sudden stops in broad H2:2015–H1:2016 window; India gross-FPI sudden stop in Q1:2022; neither 2013 taper tantrum nor 2021 taper-talk episode qualified as a sudden stop under the paper's criteria.
- The Annex Table A2 link did not resolve into independently readable table rows in this inspection. Exact India quarter(s) and 2015–16 flow measure (gross capital inflow vs net flow) remain UNKNOWN/PENDING; do not infer them from the broad body-text window.
- Report: docs/GCR_RBI_ANNEX_A2_INDIA_SUDDEN_STOP_WINDOW_EVIDENCE_LIMIT_CONTINUATION43_PART2_20261119.md; commit 0d9cefe8344e6b2b57e740803b26558ccb6b4dc4.
- Primary source: https://www.rbi.org.in/scripts/bs_viewcontent.aspx?Id=4517 (Section III/IV body text and Annex Table A2 link).
- Limits: no Annex A2 row extraction, no exact quarter boundaries, no daily market/FX/sector response, no raw event-study panel, no independent replication.
- Stage: source evidence-limit audit complete; Observation overall OPEN; Planning/Organizing NOT STARTED; GCR NOT COMPLETE; production admission NOT_AUTHORIZED.
- Invariants unchanged: ₹0; official/free sources; no synthetic data/fabricated timestamps/guessed quarters/guessed flow classifications; Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A–E unchanged; UNKNOWN is never PASS.


## Continuation 43 — Part-3: RBI Annex A2 India quarter-level sudden-stop extraction (2026-11-19)
- Breakthrough: reopened RBI official HTML and inspected Annex Table A2 directly (table heading/source lines 211–213; India row 227–230). Exact India episode windows by flow measure are now transcribed.
- Gross capital inflows: Q4 2008–Q2 2009 (3 quarters); Q1 2016–Q2 2016 (2 quarters).
- Gross FPI inflows: Q3 2006 (1); Q3 2008–Q1 2009 (3); Q1 2016 (1); Q1 2022 (1).
- Net capital flows: Q3 2004 (1); Q3 2006 (1); Q4 2008–Q2 2009 (3); Q1 2016–Q2 2016 (2).
- Correction/supersession: Part-2's UNKNOWN/PENDING for exact India 2015–16 quarter boundaries and flow-type detail is superseded by direct Annex A2 extraction. Do not confuse the broad body-text H2:2015/H1:2016 context with the India row's exact Q1–Q2 2016 entries. Preserve separate gross capital, gross FPI and net-flow labels.
- Report: docs/GCR_RBI_ANNEX_A2_INDIA_QUARTER_LEVEL_SUDDEN_STOP_EXTRACTION_CONTINUATION43_PART3_20261119.md; commit 8eb00a7a0f912085d2dcdb835ed376cef6169310.
- Primary source: https://www.rbi.org.in/scripts/bs_viewcontent.aspx?Id=4517 ; Annex Table A2 India row lines 227–230 in current official HTML rendering.
- Limits: published table extraction verified, but independent replication from raw quarterly BOPS not done; no daily market/FX/sector response; high-frequency raw event-study panel not acquired.
- Stage: Annex A2 extraction increment complete; Observation overall OPEN; Planning/Organizing NOT STARTED; GCR NOT COMPLETE; production admission NOT_AUTHORIZED.
- Invariants unchanged: ₹0; official/free sources; no synthetic data/fabricated timestamps/guessed classifications; Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A–E unchanged; UNKNOWN is never PASS.


## Continuation 43 — Part-4: RBI sudden-stop replication method and India source mapping (2026-11-19)
- Transcribed the official RBI algorithm from the article text and its two methodology images: four-quarter moving sum of gross inflows C_t; year-on-year change ΔC_t = C_t − C_(t−4); previous-five-year rolling mean and standard deviation; symmetric sudden-stop phase starts below mean−1 SD, contains at least one observation at/below mean−2 SD, and ends when it rises above mean−1 SD. Similar method is applied to net capital flows and gross FPI inflows.
- Mapped RBI Table 42 as a free official national cross-check: quarterly, US$ million, BPM6, credit/debit/net separately, includes financial-account functional categories, preliminary labels and revision policy. It is not proven identical to the IMF BOPS data vintage/definitions used in the paper and cannot substitute for the original IMF replication.
- IMF BOP dataset landing page confirms quarterly frequency and API/download entry points; API click redirected to sign-in in this inspection. No raw IMF India series, item codes, dataflow or codelists acquired/verified.
- Report: docs/GCR_RBI_SUDDEN_STOP_REPLICATION_METHOD_AND_INDIA_SOURCE_MAPPING_CONTINUATION43_PART4_20261119.md; commit 82f2fbe795630593c69c33e1bc41f6fa49c4b886.
- Sources: RBI research https://www.rbi.org.in/scripts/bs_viewcontent.aspx?Id=4517 (method text and linked images); RBI Table 42 metadata https://www.rbi.org.in/scriptS/PublicationsView.aspx?id=24094; IMF BOP dataset https://data.imf.org/en/datasets/IMF.STA%3ABOP.
- Next: resolve public IMF BOP dataflow/item codes and acquire India quarterly raw series, preserving vintage/sign/units; if API access remains gated, use RBI Table 42 only as separately labelled national cross-check after exact component mapping.
- Limits: method transcription is source-verified, but independent reproduction NOT_DONE; raw IMF/RBI quarterly exports NOT_ACQUIRED; no daily market response.
- Stage: methodology/source mapping increment complete; Observation overall OPEN; Planning/Organizing NOT_STARTED; GCR NOT COMPLETE; production admission NOT_AUTHORIZED.
- Invariants unchanged: ₹0; no synthetic data/fabricated timestamps/guessed codes/sign conversions/missing-quarter interpolation; Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A–E unchanged; UNKNOWN is never PASS.


## Continuation 44 — Part-1: IMF BOPS public SDMX structure-route audit (2026-11-19)
- New official-source finding: IMF SDMX Central Web Services Guide (last updated May 2025) documents the public structure-service entry point `https://sdmxcentral.imf.org/sdmx/v2/`, supporting Dataflow, Data Structure, Codelist and Concept queries. It documents agency/structure/version/item path parameters and reference expansion. This is a public metadata-discovery route, distinct from the IMF dataset landing-page API sign-in redirect.
- Public IMF SDMX Central registrations page is reachable and its registry listing surfaces IMF Data Structure `BOP`, “Balance of Payments and International Investment Position”, version 2.6.0. The public registration list also shows multiple national BOP-family registrations. This does not prove a current IMF BOP dataflow ID, India registration, or public observation download.
- IMF guide examples show legacy `IMF:BOP_BPM6(1.0)`, `IMF:ECOFIN_DSD(1.0)`, data domain `BOP6`, quarterly `Q`, and example indicator `BCA_BP6_EUR`. These are guide examples only, not verified current India series keys; do not reuse as production codes.
- Direct structure API URL retrieval via the research browser was inaccessible/internal-error; therefore no successful live structure payload, exact dataflow, India REF_AREA codelist, current dimension order, BOP item codes, units, signs or observation attributes have been validated. No observation query, raw IMF India quarterly data, byte count, retrieval timestamp or SHA-256 captured.
- Report: `docs/GCR_IMF_BOPS_SDMX_PUBLIC_STRUCTURE_ROUTE_AUDIT_CONTINUATION44_PART1_20261119.md`; commit `934c33f109ba63b353dc4018eab5f24f1bbcc94e`.
- Official sources: IMF SDMX Central Web Services Guide https://dsbb.imf.org/content/pdfs/IMFSDMXCentralWebServicesGuide.pdf ; IMF SDMX Central registrations https://sdmxcentral.imf.org/data/registrations.html . Research references: IMF guide lines 77–90 (structure service), 424–487 (resources/path parameters), 224–249 (legacy BOP examples); registry page and indexed DSD listing.
- Acceptance: official structure route documented PASS; public registry page reachable PASS; current BOP DSD surfaced PARTIAL; exact current BOP dataflow UNKNOWN; India codes/codelists NOT_DONE; IMF India quarterly raw observations NOT_ACQUIRED; independent RBI sudden-stop replication NOT_DONE.
- Next: bounded read-only live retrieval of current BOP Dataflow + DSD + referenced codelists, archive metadata bytes/hashes, then test whether India quarterly observations are downloadable unauthenticated. Stop on unresolved API failure; never guess keys.
- Stage: Observation OPEN; Planning/Organizing NOT_STARTED; GCR NOT COMPLETE; aggregate/production admission NOT_AUTHORIZED.
- Invariants unchanged: ₹0; official/free sources; no synthetic data, fabricated timestamps, guessed dataflow/item codes, sign conversion or interpolation; Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A–E unchanged; UNKNOWN is never PASS.


## Continuation 44 — Part-2: IMF BOPS dataflow and constraint registry audit (2026-11-19)
- Current public IMF SDMX Central Dataflows overview is reachable and reports 216 entries. Its visible first page includes ESTAT:BPM6_BOP_Q (2.6.0) and ESTAT:BPM6_BOP_M (2.6.0); these are ESTAT flows, not IMF global BOP, and must not be substituted.
- Official IMF Reporting Constraints registry lists `IMF:BOP6_CONSTRAINT` targeting `BOP6[1.0]` and `IMF:BOP_BP6_CONSTRAINT` targeting `BOP_BPM6[1.0]`. These identify two exact registry-listed IMF BPM6-era dataflow candidates, but do not prove either is the current IMF STA BOP product behind data.imf.org.
- The same registry lists `BOP5_CONSTRAINT` → `BOP5_COLLECTION[1.0]`; BPM5 candidate is not used for the BPM6 replication absent explicit source justification.
- Public registrations list includes Brazil/Chile and several other national BOP-family providers. No India registration appeared in reviewed output, but listing output is not proven exhaustive; do not claim India is absent.
- No successful live SDMX structure payload, DSD reference, India REF_AREA, dimension order, item codes, units, sign convention, observation attributes or data response acquired. No raw metadata/data bytes, retrieval timestamp or SHA-256.
- Report: `docs/GCR_IMF_BOPS_DATAFLOW_AND_CONSTRAINT_REGISTRY_AUDIT_CONTINUATION44_PART2_20261119.md`; commit `a95f8de2f4f84ab4fa0d9382800f38060654a108`.
- Official sources: IMF SDMX Central Dataflows https://sdmxcentral.imf.org/data/overview.html ; Reporting Constraints https://sdmxcentral.imf.org/data/constraints.html ; Registrations https://sdmxcentral.imf.org/data/registrations.html ; DSD listing https://sdmxcentral.imf.org/data/datastructure.html .
- Acceptance: public Dataflows page PASS; IMF:BOP6 and IMF:BOP_BPM6 registry identities PASS (identity only); global STA BOP dataflow mapping UNKNOWN; exact DSD relationship NOT_DONE; exhaustive India registration check NOT_DONE; India series/codelists NOT_DONE; raw quarterly observations NOT_ACQUIRED; independent RBI replication NOT_DONE.
- Next: retrieve exact structure payloads for IMF:BOP6(1.0), IMF:BOP_BPM6(1.0), and IMF:BOP(2.6.0), resolve DSD/constraint/codelist references and verify product relationship before any observation query.
- Stage: Observation OPEN; Planning/Organizing NOT_STARTED; GCR NOT COMPLETE; aggregate/production admission NOT_AUTHORIZED.
- Invariants unchanged: ₹0; official/free sources; no guessed mappings, series keys, units, signs or transformations; Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A–E unchanged; UNKNOWN is never PASS.


## Continuation 44 — Part-3: IMF BOPS registry DSD-version and provider evidence audit (2026-11-19)
- Current IMF SDMX Central DSD catalogue lists IMF:BOP, “Balance of Payments and International Investment Position”, latest version 2.6.0, alongside older versions and ECOFIN_DSD. The static detail view exposes fields for Dataflows, Data Providers, Period, Dimensions, Measures and dataset/series/observation/group attributes, but does not render their values. DSD catalogue identity PASS; component payload NOT_DONE.
- Current registration listing confirms national SDDS+ BOP registrations, e.g. IMF:BOP6(1.0) provider BR1 (BCB URL; updated 2026-10-26T11:47:29Z), CL2; IMF:BOP_BPM6(1.0) providers AT2 and JP4; and multiple BOP_GBPM6 registrations. These are national provider XML routes, not proof of the IMF global STA BOP observation product.
- No India-specific BOP registration was visible in the reviewed indexed output, but the dynamic/paginated catalogue was not exhaustively queried/exported. India registration presence/absence remains UNKNOWN.
- Constraint listing reconfirms IMF:BOP6_CONSTRAINT → BOP6[1.0], IMF:BOP_BP6_CONSTRAINT → BOP_BPM6[1.0], and IMF:BOP5_CONSTRAINT → BOP5_COLLECTION[1.0]. Constraint cube-region members were not rendered; no country/frequency/item availability inferred.
- Direct browser retrieval attempts for structure API paths for BOP6(1.0), BOP_BPM6(1.0), and BOP(2.6.0) returned internal/accessibility errors. This is a browser-tool access failure, not an IMF HTTP status and not proof of server outage/authentication.
- Report: `docs/GCR_IMF_BOPS_REGISTRY_DSD_VERSION_AND_PROVIDER_EVIDENCE_CONTINUATION44_PART3_20261119.md`; commit `532c8faf38b2a426305d5bab94afcff46902e76c`.
- Official sources: https://sdmxcentral.imf.org/data/datastructure.html ; https://sdmxcentral.imf.org/data/registrations.html ; https://sdmxcentral.imf.org/data/constraints.html . Research refs: turn921542search1, turn921542search2, turn921542search0, turn824478view0, turn824478view1, turn464589view3.
- Acceptance: IMF:BOP latest DSD version 2.6.0 catalogue listing PASS; DSD component payload NOT_DONE; BOP6/BOP_BPM6 constraint identities PASS only; national registration examples PASS; exhaustive India registration UNKNOWN; global STA dataflow mapping UNKNOWN; India codes/units/signs NOT_DONE; IMF quarterly observations NOT_ACQUIRED; independent replication NOT_DONE.
- Next: attempt official UI export of IMF:BOP 2.6.0 DSD and BOP6/BOP_BPM6 structures with references/codelists; stop if login or UI limitations prevent export. RBI Table 42 remains a separate national cross-check only.
- Stage: Observation OPEN; Planning/Organizing NOT_STARTED; GCR NOT COMPLETE; aggregate/production admission NOT_AUTHORIZED.
- Invariants unchanged: ₹0; official/free sources; no guessed keys/codes/units/sign conversions; Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A–E unchanged; UNKNOWN is never PASS.


## Continuation 44 — Part-4: RBI DBIE Table 42 BPM6 quarterly data route and sign-convention audit (2026-11-19)
- RBI April-2026 Comprehensive Guide identifies Table 42 as standard BPM6 BoP in US$ million, quarterly, DEPR/RBI, revisable; DBIE routes are Publication > Time-Series Publications > Monthly RBI Bulletin > External Sector and Statistics > External Sector > International Trade. Table 43 is the separate ₹ crore counterpart.
- Official DBIE first-party table page surfaced: https://dbie.rbihub.in/tables?table=external_sector.r143_standard_presentation_of_india_s_balance_of_payments_as_pe . Search-indexed metadata reports quarterly, US$ million, period 30-06-2011 to 30-06-2026, 91 rows, CSV and JSON download controls. Rendered search output said “No Rows To Show”; this is export-route discovery only, not raw acquisition.
- Research-browser open returned a JavaScript shell; container-side direct request failed DNS resolution. No raw CSV/JSON bytes, direct download URL, HTTP status, retrieval timestamp, row contents or SHA-256 captured.
- RBI Handbook general BoP sign convention (lines 397–398): increase in assets or decrease in liabilities is debit; increase in liabilities or decrease in assets is credit. Thus portfolio liability increase is on credit side, portfolio asset increase on debit side. Do not infer inflow from an unlabelled net number; inspect row, assets/liabilities and credit/debit. Table 42 covers BPM6 current/capital/financial accounts and functional categories; P marks preliminary where applicable.
- RBI Table 42 is a national BPM6 cross-check only, not proven identical to the IMF BOPS data vintage/definitions used in RBI sudden-stop paper. It starts 2011-06-30 per DBIE metadata, so cannot alone reproduce RBI paper's Q1:1992–Q1:2022 event register. No pre-2011 synthetic extension.
- Report: `docs/GCR_RBI_DBIE_TABLE42_BPM6_QUARTERLY_DATA_ROUTE_AND_SIGN_CONVENTION_CONTINUATION44_PART4_20261119.md`; commit `6bef3c26ca492339c18d5cb18a87e39d9a941cd1`.
- Official sources: RBI Handbook https://www.rbi.org.in/Scripts/PublicationsView.aspx?id=24094 (Table 42 lines 1497–1526; sign convention lines 397–398); DBIE table page above. Web references: turn991238view1, turn412603view0, turn575012search1, turn575012search0.
- Acceptance: Table 42 definition/sign convention PASS; DBIE route and CSV/JSON controls surfaced PASS (route only); period/91-row metadata PASS (page metadata only); raw CSV/JSON NOT_ACQUIRED; 91 raw rows NOT_VERIFIED; item-level row mapping NOT_DONE; IMF equivalence UNKNOWN; full 1992–2022 sudden-stop replication NOT_DONE.
- Next: obtain CSV and JSON using official DBIE download controls in browser-capable environment; preserve raw bytes and metadata/hashes, validate all rows/quarters/signs/revisions, and compare overlapping vintages to RBI Bulletin. Do not invent download URL or claim acquisition.
- Stage: Observation OPEN; Planning/Organizing NOT_STARTED; GCR NOT COMPLETE; aggregate/production admission NOT_AUTHORIZED.
- Invariants unchanged: ₹0; official/free sources; no synthetic pre-2011 extension, guessed signs, interpolation or revision erasure; Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A–E unchanged; UNKNOWN is never PASS.


## Continuation 44 — Part-5: prior RBI Table 197 / Table 42 work recovered; duplicate-task correction (2026-11-19)
- User correctly suspected this work had already been completed. Searched repository code/docs and reopened the exact prior reports/scripts/raw source archive.
- RBI Table 197 India scale/sign benchmark already PASS: 12/12 across 2024-Q2–2025-Q3; assets mapping is negative RBI “Portfolio Investment by India” net to IMF A_NFA_T; liabilities map same-sign RBI “Portfolio Investment in India” net to IMF L_NIL_T. Raw RBI HTML 146,017 bytes, SHA-256 `391c549c5b64c0b7f9204eb9634975f77d4ba2d7796542ed23932fb8d740813d`; workflow run 44476434148; artifact 14506542277; ZIP SHA-256 `eb719a38a285603ec2eff92ea7a88aadd5cbb7481393fe5b8f44188bffcacf62`. Report: `docs/GCR_IMF_BOP_SCALE_RECONCILIATION_INDIA_20261119.md`.
- RBI Bulletin Table 42 current-vintage crosswalk already executed by `scripts/research/crosscheck_india_bop_scale_sign.py`; script captures official raw HTML, timestamps, headers, byte counts, SHA-256 and outputs CSV/JSON/manifest/report. Two official source pages: Id=24424 (published 2026-08-25; raw SHA-256 `a92ac0f8196efbd8f503984620d7c0291c6d704405e52d64eec4f96948ddf744`) and Id=24566 (published 2026-10-23; raw SHA-256 `075c28122d588e5bce0ff45c8c8d5d8b453c53dc5b9a20f79d5cd3a6e54f5396`).
- Table 42 four-quarter crosswalk (2025-Q1, 2025-Q2, 2026-Q1, 2026-Q2) has 12 comparisons: 10 PASS, 2 REVIEW. All 2025 quarters and 2026-Q2 pass; 2026-Q1 asset passes but liability and combined net remain REVIEW. IMF liability -13,633.508347m USD vs RBI 3.2.A net -12,121m; residual -1,512.508347m. Combined-net residual -1,512.457994m. No cause established, no silent adjustment. Supplement report: `docs/GCR_IMF_BOP_SCALE_RECONCILIATION_INDIA_CURRENT_VINTAGE_SUPPLEMENT_20261119.md`; artifact 14505649659; ZIP SHA-256 `8db4f9536a57df1e8635855af5bb90225de0f800e6e9164bd20d99d1f355b4e2`.
- Reopened and verified report blob SHAs at audit: India baseline `83bc6de6a724f4f1ddc6a7e74556e5f596393788`; current-vintage supplement `d638cf4a9bc262b55c7660585d01aca493ebf518`; Table197 script `c746442c2ab483d5212da908715c20f0049d69ad`; Table42 crosscheck script `e058a7988068733b987109cc8c87759a5e8fa213`.
- Correction: Continuation 44 Part-4's “raw acquisition pending” wording was too broad. Already acquired and cross-checked: RBI Bulletin Table42 raw HTML for four quarters (10/12 PASS, 2 REVIEW). Not acquired in that work: separate DBIE time-series CSV/JSON export page. This is a distinct optional route, not a reason to repeat the prior Table42 work.
- New correction report: `docs/GCR_RBI_TABLE42_PRIOR_WORK_REUSE_AND_DUPLICATE_TASK_CORRECTION_CONTINUATION44_PART5_20261119.md`; commit `b0fffe98597de60c1ccdeb5cb1ad2d0ef55261df`.
- Next action: do not rerun Table197/Table42 scripts unchanged. Investigate exact 2026-Q1 vintage/definition discrepancy using archived source pages and IMF observations; seek same-quarter earlier/later official RBI vintage only if available and archiveable. If unresolved, retain REVIEW and move to next independent country/coverage blocker.
- GCR remains INCOMPLETE/BLOCKED; no EMDE aggregate/production admission. ₹0; no synthetic rows/interpolation/guessed transforms; all protected production invariants unchanged; UNKNOWN is never PASS.


## 2026-11-19 — GCR 10-check backtest readiness audit
- Report: `docs/GCR_ROTATION_BACKTEST_READINESS_AUDIT_10_CHECKS_20261119.md`.
- Actual GCR rolling performance backtests executed: 0/10; readiness/contract checks reviewed: 10/10 (0 full execution PASS, 9 PARTIAL, 1 BLOCKED). Do not represent this as a backtest result or evidence of predictive value.
- Reused prior RBI Table 197 12/12 PASS, RBI Table 42 10 PASS / 2 REVIEW, FRED/H.10 audits and existing cost-aware replay contract; no duplicate reruns.
- GCR relative-attraction formula, synchronized sector transmission and rolling backtest remain NOT_DONE; IMF panel aggregate remains blocked by coverage/scale/vintage constraints.
- V11.3 cost-aware replay code and contract inspected; execution assumptions G0 remain BLOCKED, no verified output ledger/hash produced in this audit.
- No workflow dispatched, no run/artifact IDs claimed, no production or protected invariant changes.
- Next action: small, leakage-safe timestamp/vintage-aligned pilot joining archived GCR factors to official India sector TRI/outcomes, then proceed only if source coverage and maturity gates pass.
- Nightly Rotation Backtest automation created for 22:00 Asia/Kolkata, daily; first scheduled run 2026-11-20 22:00.


## 2026-11-19 — Continuation 74: CDSL 15-Nov-2026 sector FPI independent arithmetic QA
- Reused existing raw capture from workflow run 44519322726 / artifact 14527092174; no repeat capture. ZIP SHA-256 independently recomputed and matched GitHub digest: `83048ea0bc712b6a453270f8fb5c3c6755b579857ff2ad9eb7d53c8ba1778fbd`.
- Exact dated sector HTML: 327,522 bytes; SHA-256 `3f77f3896a95b8cff3a7728049127493814e1b503eb39dcb75b0e8fe145cf84e`.
- Main table has 24 numbered sector/category rows, 8 period/currency blocks, 11 components + published total per block. Independent component-sum checks: 192/192 PASS.
- Grand total vs sum of 24 sector totals residuals (published minus sum): 31-Oct AUC INR 0; 31-Oct AUC USD +1; 16–31 Oct net INR -1; same USD +2; 01–15 Nov net INR -2; same USD -2; 15-Nov AUC INR -1; same USD -3. Preserve published values; reconciliation REVIEW, no adjustment.
- Important separation: AUC is position stock; net investment is fortnightly flow; neither is daily flow or sector return. Period-specific USD conversion conventions retained; no recalculation or daily interpolation.
- Report: `docs/GCR_CDSL_15NOV2026_SECTOR_FPI_ARITHMETIC_QA_CONTINUATION74_20261119.md`; commit `eb7647f15d1b3449a35a088c79f684ccbfec2b98`.
- Sector TRI crosswalk, matched NSDL confirmation, and GCR-to-sector/stock predictive backtest remain NOT_DONE/BLOCKED. Next: official BSE sector TRI raw history + exact index IDs and defensible BSE classification mapping; otherwise sector transmission UNKNOWN.
- No production/selector/ranking/pressure-fade/CORE-672/Engines A–E/IPO-PLX V2 changes. ₹0; Observation OPEN; UNKNOWN is not PASS.


## 2026-11-19 — Daily Historical Rolling Backtest Performance Requirement Locked
- User requirement: every day, provide a reliable, comparable historical rolling-backtest performance rate so progress can be measured. Locked as an acceptance contract, not claimed as implemented.
- Contract: `docs/DAILY_HISTORICAL_ROLLING_BACKTEST_PERFORMANCE_ACCEPTANCE_CONTRACT_20261119.md`.
- Separate scorecards mandated: (1) V11.4 exploratory behavioural selector target metrics; (2) V11.3 cost-aware executable replay only after G0 execution assumptions are approved; (3) GCR predictive performance only after timestamp/vintage-aligned factor-to-TRI panel and crosswalk gates pass.
- Daily comparisons must use fixed protocol, matured outcomes only, exact denominators, chronological rolling cutoffs, confidence intervals, dataset/code/config hashes, independent metric reconciliation and same-protocol baseline. Methodology changes start a new versioned series.
- H+3 State calibration minimum remains 50 fully matured observations; below threshold UNKNOWN. No synthetic data; UNKNOWN is never PASS.
- Runtime policy: isolated jobs, preferably 20–60 seconds and never over 10 minutes for new audit jobs. Reuse archived datasets/artifacts; do not trigger the 120-minute prospective workflow solely for daily metrics.
- Existing Nightly Rotation Backtest automation at 22:00 IST is the sole scheduled cadence; no duplicate automation created. Schedule does not imply implementation.
- Current reliable daily performance rate remains NOT_AVAILABLE/UNKNOWN: previous audit verified 0 GCR rolling backtests; V11.4 metrics artifacts not retrieved/verified in this audit; V11.3 G0 assumptions remain unapproved. No performance percentage invented.
- No changes to Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A–E or IPO-PLX V2. ₹0; official/free sources only.


## Unified Daily Top-5 Stock Watchlist and Alert (2026-11-19)
- User requirement: combine the three independent research sections at candidate level into one daily India equity watchlist of up to five names seeking researched 2%–20% upside scenarios; never attribute one engine's result to another.
- V11.4 contributes only matured historical behavioural evidence (target-specific precision/hit rate/recall/false positives); V11.3 contributes cost-aware replay metrics only after G0 assumptions are user-approved and independently reconciled; GCR contributes only when synchronized macro/sector/stock timestamps/vintages and matured outcomes pass. Unknown engine = UNKNOWN and no artificial score boost.
- Each candidate must include verified symbol/exchange/ISIN, price and timestamp, target scenario bands, horizon, catalyst, technical/volume/sector context, liquidity, invalidation/risk, circuit/surveillance/news risks, source links and engine-wise evidence. The 2%–20% bands are scenarios, not promises or buy instructions.
- Select up to five qualified candidates. Never pad the list: if fewer than five pass evidence gates, report the smaller count or no reliable alert. No fabricated prices, timestamps, catalysts or performance metrics.
- New daily automation: “Daily Unified Top-5 Alert”, 08:45 Asia/Kolkata, starting 2026-11-20; created successfully. It inspects prior GitHub ledger/reports/artifacts first, reuses archived data, writes dated reports and updates the ledger with commit/run/artifact/hash verification. It does not imply that five valid candidates will exist each day.
- Existing “Nightly Rotation Backtest” at 22:00 Asia/Kolkata remains the nightly research/backtest task; no duplicate nightly task created.
- Protected invariants unchanged: Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56x12), Engines A-E, IPO-PLX V2. ₹0; official/free sources only; UNKNOWN is never PASS.


## 2026-11-19 — Existing NSE Walk-Forward Ledger Recovery and GCR Join Feasibility
- Reused branch `audit/prospective-selector-tracking`; no new NSE data collected, no workflow dispatched, no backtest rerun.
- Walk-forward source blob `df6e55a72f0e62e59d8de58eff7c58d17e2ec34b`; audit workflow blob `d26af3fd3415050fd16902656079c6747ebeae1c` (timeout 10 minutes). Generated metrics/probability JSON and processed NSE dataset are absent from the committed branch tree; they may exist as Actions artifacts, not recovered/verified here.
- Recovered `outputs/prospective/watchlist_ledger.csv` blob `fe35e72058fe45ff3a91dbe5b66c2e8199a2fdfe`: 290 rows, 29 historical cutoffs (2026-10-02 to 2026-11-18), 131 distinct symbols; 145 picks per selector. Latest cutoff 2026-11-18 has zero matured outcomes at H+1/H+3/H+5.
- Exploratory pooled matured hit rates: CURRENT_WINNER_PROB +5% H+1 36/135=26.67%; +10% H+3 23/124=18.55%; +20% H+5 14/111=12.61%. P10_P20_MEAN +5% H+1 28/136=20.59%; +10% H+3 28/124=22.58%; +20% H+5 13/111=11.71%. Unresolved counts respectively 10/21/34 and 9/21/34. These are selected-pick high-excursion hit rates only, not recall, full-universe confusion matrix, net return, or statistically confirmed performance.
- Daily feedback ledger has 28 rows and documents provisional per-stock outcomes, unresolved official NSE OHLC/volume/delivery cross-checks and unavailable intraday bars. Not a verified official outcome ledger.
- Full walk-forward metrics, probability universe denominator, paired bootstrap CI and per-State matured sample remain NOT_VERIFIED. H+3 minimum 50 fully matured observations per State not proven by pooled selector counts. CORE-672 code slots rotate 25 measurable feature families; not 672 independently validated signals.
- GCR join verdict: technically possible only with timestamp/vintage aligned macro panel, official sector TRI, exact index identifiers and validated symbol-sector crosswalk. Current empirical join BLOCKED; registry/transmission-map sector hypotheses remain HYPOTHESIS_NOT_VALIDATED. GCR remains UNKNOWN and cannot be credited for V11.4 hit rates.
- Report: `docs/EXISTING_NSE_WALK_FORWARD_LEDGER_MATURITY_AND_GCR_JOIN_AUDIT_20261119.md`.
- Next: recover existing Actions artifact (walk_forward_metrics.json, walk_forward_universe_probabilities.csv, historical audit JSONs, reproducibility report) and verify dataset manifest/hash. If unavailable/expired, stop; do not download new NSE data under user's instruction. Recompute full denominators and paired CIs from recovered artifact; then test one small GCR overlap window only after source-vintage/TRI/crosswalk gates.
- V11.3 cost-aware replay remains NOT_AUTHORIZED / NOT_RUN pending G0; no production invariants changed; ₹0; UNKNOWN is never PASS.


## 2026-11-19 — Existing Walk-Forward Actions Artifact Recovered and Metrics Audited
- Recovered existing GitHub Actions artifact only; no NSE download, workflow dispatch, or backtest rerun.
- Workflow run #319 / ID 40112393704, branch `audit/prospective-selector-tracking`, head SHA `7d7faaa3e50e216f4fc6cacfe75b88d3c58b4381`; run conclusion CANCELLED. Artifact ID 12566997895, name `prospective-watchlist-audit`, expires 2027-01-22T16:37:12Z.
- Artifact SHA-256 independently recomputed and matches GitHub digest: `00a990117ac19971396eb5c039cb73c103e40f7ac3d1c93f31ca4839c6e56b7e`. Metrics JSON SHA-256: `c9e0c929914bc1f2f2550ccd38cb7b2410d0247f500f774b471887d638859c79`; QA JSON SHA-256: `e914f2fce4693acef7f4e89feceaafe6da7732f25df7dd0fa51fb4d2b55d25ee`.
- Artifact reports 100/100 sessions, 3,000 candidate rows, Top-30 ranking. Precision: T5_H1 33.31%, T10_H3 22.72%, T15_H5 15.21%, T20_H5 7.82%. Recall: 4.55%, 3.96%, 3.50%, 3.91% respectively. Base rates: 8.63%, 6.54%, 4.84%, 2.23%; lift: 3.86x, 3.48x, 3.14x, 3.51x respectively.
- Full-universe calibration summaries: T5_H1 n=246,661 / Brier 0.075997 / ECE 0.017666; T10_H3 n=246,269 / Brier 0.059030 / ECE 0.002677; T20_H5 n=245,850 / Brier 0.020919 / ECE 0.000874.
- QA report records PASS for 200 sessions, 2,963 symbols, 100% delivery quantity/percentage coverage and no issues. This does not independently verify the missing source manifest/hashes.
- Important model diagnostic: aggregate winner/nonwinner mean probability is 0.086364 vs 0.086580 (winner slightly lower); winner-specific interaction and latent-winner evidence are nearly flat. Thus Top-30 lift exists in the artifact, but probability separation is weak and must be diagnosed before any tuning/promotion.
- ZIP does not contain `walk_forward_universe_probabilities.csv`, dataset manifest or complete cutoff-level reproducibility bundle. Run conclusion CANCELLED. Therefore independent TP/FP/FN/TN, paired cutoff CIs, full leakage/reproducibility audit and selector promotion remain NOT_VERIFIED / NOT_AUTHORIZED.
- 100% hit rate is not an acceptable optimization target because it can be achieved by collapsing coverage or overfitting. Next research objective: improve precision under explicit recall/coverage, sample-size, drawdown and transaction-cost guardrails using chronological held-out shadow/challenger tests only; no production changes.
- Report: `docs/RECOVERED_WALK_FORWARD_ARTIFACT_METRICS_AUDIT_20261119.md`.
- GCR remains UNKNOWN/BLOCKED pending timestamp/vintage-aligned macro panel, official sector TRI, exact index IDs and verified symbol-sector crosswalk. V11.3 cost-aware replay remains NOT_AUTHORIZED / NOT_RUN pending G0 approval.
- Protected invariants unchanged; ₹0; no new NSE collection; UNKNOWN is never PASS.


## 2026-11-20 — Winner Recovery / False-Positive Diagnostic from Existing Walk-Forward Artifact
- Reused run #319 artifact only; no NSE download, no workflow rerun, no production code change. ZIP SHA-256 matched GitHub artifact digest.
- Inspected exact metrics JSON and walk-forward source. Clarified two separate probability diagnostics: generic `WINNER_PROBABILITY` separation is Top-30 only (H+3 winner mean 0.086364 vs nonwinner 0.086580; gap -0.000216), whereas target-specific full-universe Platt-calibrated probability mean gaps are positive: T5_H1 +0.008946, T10_H3 +0.003695, T20_H5 +0.000611. Do not conflate the two.
- Top-30 state diagnostic (3,000 rows): CONTINUATION_READY 2,541 rows; hit rates +5 H+1 34.23%, +10 H+3 23.32%, +15 H+5 15.75%, +20 H+5 7.96%. HIDDEN_WINNER_RECOVERY 459 rows; 28.05%, 19.18%, 12.14%, 7.04%. Continuation leads by 6.18/4.13/3.61/0.92 percentage points. Descriptive only; no per-cutoff CIs.
- Transition signature: DEMAND_CONFIRMATION (1,222 rows) leads +10 H+3 24.96%, +15 H+5 16.28%; EXHAUSTION_BUILD (283 rows) trails with 19.71%, 13.53%, +20 H+5 5.26%. PRESSURE_FADE +20 H+5 is 8.31%, effectively tied with DEMAND_CONFIRMATION 8.31%; no change to protected +1 PRESSURE_FADE.
- Research diagnosis: investigate HIDDEN_WINNER_RECOVERY thresholds and EXHAUSTION_BUILD admission as shadow-only hypotheses; audit score/percentile ordering and target-specific probability fields. No evidence yet supports production tuning.
- Full false-positive/missed-winner symbol lists, per-cutoff paired CIs and shadow challenger validation remain BLOCKED because run #319 ZIP lacks row-level `walk_forward_predictions.csv` and `walk_forward_universe_probabilities.csv`. Recover from an existing successful non-cancelled artifact only; if absent, stop. Do not recollect NSE data.
- Report: `docs/WINNER_RECOVERY_FALSE_POSITIVE_DIAGNOSTIC_20261120.md`.
- No changes to Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A–E or IPO-PLX V2. GCR remains UNKNOWN/BLOCKED; V11.3 cost-aware replay NOT_AUTHORIZED/NOT_RUN. ₹0; UNKNOWN is never PASS.


## 2026-11-20 — Existing Artifact Recovery Exhaustion for Row-Level Winner Analysis
- Searched existing prospective-watchlist workflow artifacts; inspected runs #319, #302, #301, #300, #299, #298 and earlier artifact-bearing failed/cancelled runs. The 43 run records returned for workflow ID 381790326 on the audit branch were CANCELLED or FAILURE; no successful completed validation run was identified in this inspected set.
- Downloaded run #302 artifact ID 12550639923 (8,858,141 bytes). GitHub digest and independently recomputed ZIP SHA-256 both equal `6e20634289f2b2838ee79d156bfce52f6ee2bff68a0a40adeefa732fe9c52da5`.
- Run #302 ZIP contains 110-row `outputs/prospective/watchlist_ledger.csv` (SHA-256 `1bc2712ef3b3bb36faa82346a496a16aecec8971748cb3133705364ceb3c8166`) and `data/qa/qa_report.json` (SHA-256 `e914f2fce4693acef7f4e89feceaafe6da7732f25df7dd0fa51fb4d2b55d25ee`). QA JSON says 200 raw files/sessions/processed dates, 2,963 symbols, 100% delivery coverage, no issues. This QA content does not override run status.
- ZIP listing does not contain `walk_forward_predictions.csv`, `walk_forward_universe_probabilities.csv`, prediction outputs or dataset manifest. Other inspected large artifact from run #319 likewise lacks these files. Tiny ~3.9 KB failed-run artifacts are not usable validation bundles.
- False-positive and missed-winner identities, per-cutoff TP/FP/FN/TN, paired bootstrap CIs and shadow challenger results remain NOT_AVAILABLE / NOT_RECOMPUTABLE / NOT_RUN. Do not infer identities or tune production weights from aggregate state/signature rates.
- Report: `docs/EXISTING_ARTIFACT_RECOVERY_EXHAUSTION_ROW_LEVEL_EVIDENCE_20261120.md`.
- Next: wait for/reuse any existing complete successful artifact; if absent, ask explicit approval before a bounded audit-only export job reusing existing processed dataset. No new NSE data collection under current instruction.
- No changes to Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A–E or IPO-PLX V2. GCR UNKNOWN/BLOCKED; V11.3 cost-aware replay NOT_AUTHORIZED/NOT_RUN. ₹0; UNKNOWN is never PASS.


## 2026-11-20 — Existing Processed Dataset and Workflow Scope Audit
- Inspected main HEAD `82c24bdef151b93f1c5f8d53ffc473a1c7bcde51` and audit branch HEAD `46411147f490abbf05f920073b7139b258e42b1e`. Main `data/processed` contains only `.gitkeep`; audit branch tree has no processed NSE dataset, row-level prediction export or dataset manifest.
- Inspected `.github/workflows/prospective_watchlist_tracking.yml` on the audit branch. Despite its 10-minute timeout, it is not export-only: it downloads 200 NSE sessions, rebuilds the dataset, runs strict QA, quarterly/XBRL collection, walk-forward backtest, Macro-Geo collection/repair and multiple retrospective studies.
- Therefore dispatching it would violate the current no-new-NSE-collection constraint and cannot be represented as a safe audit-only export. No workflow was dispatched; no data was downloaded.
- Existing #319/#302 artifacts still lack row-level prediction CSVs and dataset manifest. Exact TP/FP/FN/TN, false-positive/missed-winner identities and paired cutoff CIs remain NOT_RECOMPUTABLE.
- Report: `docs/EXISTING_PROCESSED_DATASET_AND_AUDIT_WORKFLOW_SCOPE_20261120.md`.
- Next: search only for an already-existing complete processed dataset/artifact from retained sources; otherwise stop and request explicit approval before any new collection. Production invariants unchanged; UNKNOWN is never PASS.


## 2026-11-20 — Successful Run #407 Row-Level Walk-Forward Artifact Recovered
- Found an existing successful run outside the previously inspected prospective audit workflow: NSE Historical Backbone + Adaptive V11.3 + IPO-PLX, Run #407 / ID `44542948987`, main branch, head SHA `d013577157bc1f24322cd100aaf60c40a20c4d17`, job `collect-and-test` SUCCESS.
- Artifact ID `14539426731`, name `precision-wires-adaptive-407`, 61,902,773 bytes, expiry 2027-02-17T14:22:02Z. GitHub digest matches independently recomputed ZIP SHA-256: `b958d9184eb2df4715364b5825d243593c1c9d9d1290a171ae3ab2833950dfd7`.
- Recovered processed 200-session NSE dataset, 3,000-row Top-30 predictions, 251,724-row full-universe probability table, and 9,182-row missed-winner lab. No source dataset manifest in ZIP.
- Key hashes: processed dataset `b59b6c5410d4182c718c9e1010acb727ab0c607b4e9030568264d204a9308470`; predictions `06dc89983aa748bae5e03eee8e3ad4be5bd2add008e5b00dc350e5e65399d843`; universe probabilities `b46de0967bd22ef548f6ee27550386160d8d3967c9aeb4680be5b807f7f612e1`; metrics JSON `9a79719ec8482953044cae38b6ab9329c20849fef64b69dfd85e81c3d3b99061`; missed-winner lab `6c97f7c452a49f14309a4a8958ed98ca8812311b19f14cbe4eae5b08d79c5867`.
- Independent Top-30 vs eligible full-universe confusion matrices:
  - +5 H+1: TP 648, FP 2,351, FN 21,871, TN 226,676; precision 21.61%, eligible-universe recall 2.88%.
  - +10 H+3: TP 1,198, FP 1,802, FN 8,537, TN 240,187; precision 39.93%, eligible-universe recall 12.31%.
  - +20 H+5: TP 612, FP 2,388, FN 1,454, TN 247,270; precision 20.40%, eligible-universe recall 29.62%.
- Metrics JSON has a denominator-scope difference for recall/base-rate: source computes these over all raw rows at the selected cutoffs, while the universe probability CSV contains only rows with history depth >=20 and non-null feature availability. Additionally H+5 precision differs: JSON 20.30% (609 hits implied) vs 20.40% (612 hits in prediction CSV). This internal discrepancy remains BLOCKED pending exact serialization/source reconciliation.
- Full-universe State sample counts: NON_STRONG 88,319; FALSE_STRENGTH 57,511; HIDDEN_WINNER_RECOVERY 49,166; ALREADY_EXPANDED 27,655; NOT_YET_MOVED 12,774; REPRICING_PRESSURE 6,728; STRONG 6,470; EXPANSION_READY 2,085; CONTINUATION_READY 992; DATA_CONTAMINATED 24. DATA_CONTAMINATED remains UNKNOWN under the minimum 50 matured-observation rule.
- Missed-winner lab reasons: RANKED_OUT 6,611; LOW_WINNER_PROBABILITY 2,552; CONTAMINATED 19. This lab covers +10 H+3 and/or +20 H+5, not H+1.
- Report: `docs/RUN407_ROW_LEVEL_WALK_FORWARD_RECOVERY_AUDIT_20261120.md`.
- Artifact recovery PASS; row-level structural QA PARTIAL; metric consistency BLOCKED; executable/net-of-cost performance NOT_ESTABLISHED. No new workflow dispatched or data collected during this audit. Production invariants unchanged; GCR remains UNKNOWN/BLOCKED; UNKNOWN is never PASS.
- Next: reconcile metric denominator and H+5 precision discrepancy from exact source snapshot, then calculate cutoff-clustered paired confidence intervals and false-positive/missed-winner driver summaries.


## 2026-11-20 — Run #407 Cutoff-Clustered Bootstrap and Winner Driver Attribution
- Recovered successful Run #407 artifact ID 14539426731; run ID 44542948987; source commit d013577157bc1f24322cd100aaf60c40a20c4d17. Independent ZIP SHA-256 matches GitHub digest: b958d9184eb2df4715364b5825d243593c1c9d9d1290a171ae3ab2833950dfd7.
- Audited 3,000 Top-30 rows / 100 cutoffs, 251,724 exported universe rows, and 9,182 missed-winner rows. Performed 20,000 paired cutoff-cluster bootstrap resamples (seed 20261120).
- Top-30 precision and 95% cutoff-clustered CIs: +5 H+1 21.61% [19.34,24.07]; +10 H+3 39.93% [36.80,43.20]; +20 H+5 20.40% [18.30,22.70].
- Exported-universe TP/FP/FN/TN: +5 H+1 648/2351/21871/226676; +10 H+3 1198/1802/8537/240187; +20 H+5 612/2388/1454/247270. Recall CIs and lift CIs calculated against exported 251,724-row universe only and remain provisional.
- Found a material denominator mismatch: source metrics JSON uses internal all_by_date frame, while walk_forward_universe_probabilities.csv exports universe_pred. JSON recall differs from exported-universe recomputation (2.7439 vs 2.8776%; 11.4993 vs 12.3061%; 29.0553 vs 29.6225%). Source code explicitly uses all_by_date for universe/base rate. Full-market recall and confusion matrix are therefore not yet reconciled.
- Top-30 subgroup paired bootstrap: HIDDEN_WINNER_RECOVERY materially exceeds CONTINUATION_READY in this artifact for H+3 and H+5. PRESSURE_FADE has strongest observed H+3/H+5 transition-signature hit rates among selected Top-30 rows. EXHAUSTION_BUILD has higher H+3 than most signatures but lower H+5 than PRESSURE_FADE. Descriptive only; no causal inference or production change.
- Missed-winner rows: RANKED_OUT 6,611; LOW_WINNER_PROBABILITY 2,552; CONTAMINATED 19. TOP_DRIVER_GAPS populated 5,685/9,182; RELATIVE_STRENGTH;PROGRESSION 4,344, PROGRESSION 718, RELATIVE_STRENGTH 623. 3,497 gap values missing.
- Report: docs/RUN407_CUTOFF_CLUSTERED_BOOTSTRAP_AND_WINNER_DRIVER_ATTRIBUTION_20261120.md.
- Next: reconcile all_by_date versus universe_pred row membership and forward labels, create cutoff-level denominator ledger, then rerun paired bootstrap and a shadow-only challenger. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A–E and IPO-PLX V2 unchanged. GCR excluded. UNKNOWN is never PASS.


## 2026-11-20 — Run #407 Source Denominator and H+5 Serialization Reconciliation
- Re-read exact source `pipeline/walk_forward_backtest.py` at commit `d013577157bc1f24322cd100aaf60c40a20c4d17` and reconstructed cutoff row membership from the archived processed NSE dataset in artifact #407. No new collection, workflow dispatch, backtest rerun or production change.
- Exact 100-cutoff row counts: `all_by_date` 257,696; HISTORY_DEPTH_AT_T >=20 eligibility rows 251,724; excluded short-history rows 5,972. Export membership check on (CUT_OFF,SYMBOL): zero missing, zero extra, zero duplicates. This fully explains the denominator membership difference.
- Raw all_by_date outcome denominators: T5_H1 23,616 winners (193 null labels); T10_H3 10,418; T20_H5 2,096. Eligible export winners: 22,519; 9,735; 1,964.
- Prediction CSV Top-30 hits: T5_H1 648 (JSON agrees); T10_H3 1,198 (JSON agrees); T20_H5 612 (CSV precision 20.40%) while JSON precision 20.30% implies 609 hits. JSON T20_H5 recall 29.05534% also does not reconcile with 2,096 all_by_date winners and either hit count. T20_H5 remains BLOCKED.
- Reconstructed 20,000 paired cutoff-cluster bootstrap (seed 20261120), 100 cutoff clusters: T5_H1 precision 21.60% CI [19.3333,24.0667], recall 2.74390% CI [2.4950,3.0246], lift 2.35698x CI [2.14014,2.60041]; T10_H3 precision 39.9333% CI [36.8000,43.1667], recall 11.49933% CI [10.8224,12.2239], lift 9.87777x CI [9.33142,10.46156]; T20_H5 precision 20.40% CI [18.3000,22.6333], recall 29.19847% CI [26.5144,32.1632], lift 25.08110x CI [22.80528,27.56944] — T20 values provisional due to 3-hit inconsistency.
- Report: `docs/RUN407_SOURCE_DENOMINATOR_AND_H5_SERIALIZATION_RECONCILIATION_20261120.md`; commit `4c028c3e26608fa447756d614400bd7c778166f3`.
- Next: trace T20_H5 609-vs-612 mismatch from retained job logs/artifact provenance. If not resolvable, keep BLOCKED and request approval for a bounded audit-only export using existing processed data. No new NSE collection.
- Protected invariants unchanged; GCR remains UNKNOWN/BLOCKED; V11.3 cost-aware replay NOT_AUTHORIZED/NOT_RUN; ₹0; UNKNOWN is never PASS.


## 2026-11-20 — Daily Unified Top-5 Pre-Market Audit
- Existing completed workflow inspected; no new workflow dispatch or NSE data collection was initiated by this daily audit. Workflow Run #338: run ID `44599244783`, conclusion `success`, source commit `6899422730c6fdf30d4e1b93c8cac2ce0efe64e2`; artifact ID `14567098741`, size 50,287 bytes. Independently calculated artifact ZIP SHA-256 `d500b8c42e10bde7640d177243aae2c305e4bf21eea3d7bc85cc7ffea71085c3` matches the GitHub artifact digest.
- Audit branch head `34e4718f928753bb8acf93e285ad8c04f6501e70`. Exact source files inspected: `pipeline/walk_forward_backtest.py` blob `df6e55a72f0e62e59d8de58eff7c58d17e2ec34b`; `pipeline/live_prospective_selector.py` blob `6d6cb56b80f4fca3abc984b7ed7c6c75ebbf89d0`.
- Artifact QA JSON reports PASS: 200 raw/processed sessions, 2,997 symbols, delivery quantity and percentage coverage 100%, issues empty. This is artifact-reported QA; raw session bytes and immutable raw-file manifest were not included in the ZIP, so raw-data integrity was not independently re-performed here.
- Latest shadow selector cutoff 2026-11-19: 10 picks, 7 unique names; labels explicitly not read from future. CURRENT_WINNER_PROB: ELITECON, NRL, KDDL, LEENEE, YATRA. P10_P20_MEAN: NRL, KDDL, YATRA, HINDOILEXP, ARYAMAN. All were outside the frozen Top-30. Selector score values are ranking scores, not probabilities.
- V11.4 main 100-cutoff/3,000 Top-30 aggregate metrics: +5 H+1 precision 32.73%, recall 4.12%, base 9.17%, lift 3.57x; +10 H+3 22.34%, 3.67%, 6.85%, 3.26x; +15 H+5 14.33%, 3.21%, 4.91%, 2.92x; +20 H+5 7.07%, 3.52%, 2.21%, 3.20x. Target-specific valid prediction counts and row-level TP/FP are not exported; FP counts and main Top-30 CIs remain UNKNOWN.
- Source code confirms recall/base-rate denominator uses `all_by_date=df[df["DATE"].isin(cutoffs)]`, whereas exported eligible probability universe is history-depth/feature filtered. The artifact lacks row-level universe predictions and raw data needed for independent membership reconciliation. Recall/base-rate/lift therefore remain provisional, not PASS. This repeats the denominator-scope risk already identified in Run #407 but is a distinct Run #338 data window; do not combine metrics across runs.
- Separate strict historical shadow audit: 30 matured cutoffs × 5 picks = 150 per selector per target. CURRENT vs P10_P20_MEAN: H+1 41/150 vs 30/150, paired delta -7.33 pp [95% CI -14.00,-0.67]; H+3 31/150 vs 31/150, delta 0.00 pp [-6.02,+6.00]; H+5 19/150 vs 16/150, delta -2.00 pp [-6.00,+1.33]. Retrospective only; prospective_validation=false and promotion_authorized=false. No production selector promotion.
- Candidate screen: zero qualified candidates. NRL dated NSE snapshot (13-Nov-2026) showed BE, 5% band, 100% margin and 2.31 impact cost; KDDL's last explicit NSE quote snapshot found was 17-Nov-2026 12:05; HINDOILEXP's 19-Nov 11:31:43 snapshot showed ST ASM-1 and P/E >50 for four trailing quarters. YATRA's 12-Nov NSE-filed release had mixed operating metrics; ELITECON ISIN verified but current quote/surveillance not; LEENEE and ARYAMAN official ISIN/current quote checks remain UNKNOWN. No 2/5/10/20 target bands or stops were generated.
- Previous comparable model cutoff 2026-11-18 union had 7 symbols; 2026-11-19 union retained NRL and LEENEE, added ELITECON/KDDL/YATRA/HINDOILEXP/ARYAMAN, and removed BNALTD/CHEMFAB/SANGAMIND/VENUSREM/DHANBANK. This is list turnover only, not performance evidence.
- Engine B V11.3 cost-aware replay: UNKNOWN / NOT AUTHORIZED / NOT RUN; no assumed trade rules or cost score. Engine C GCR: UNKNOWN / BLOCKED; no timestamp/vintage-aligned macro-sector-stock-outcome join and no boost. NSE broad-index snapshot is context only.
- Daily report: `docs/DAILY_UNIFIED_TOP5_SWING_WATCHLIST_20261120.md`; final report commit `65639672a9bc4e59a76e5306e5c15e1bc6ab83de`; Git blob `eaf527f31aa39bc202ce966410c5602709718108`; independently computed UTF-8 content SHA-256 `5630cb4f58b0c82902ab755fbe49d972ab7ab05e3d4486ec4bf9ba94787ec6a3`.
- Artifact internal SHA-256: latest_picks.csv `f5292dada014864764135ad9a591b3ef378e8b437b9219bc42e508afb296f7a5`; walk_forward_metrics.json `a1fccf5d402f8a4ae0c540790c31aee7c9794894099d7c58ec1af38358e00925`; qa_report.json `81d21799277b651d63e736ff5a1e6267e15ba04dbd7849cf1f737228a3d57c36`; strict_30_matured_cutoff_audit.json `02ee46d92ef70ddf3807400e712848b62cb97aa700ff95d1b5fa8a7d4901c304`; watchlist_selector_experiment_summary.json `95f2548174d35917626796f28dc2611a7f99f4325aea11cd33a431cd452ad5cc`; multiwindow_retrospective_audit.json `c846463404661beab4bba963f81f91b5bde1a8ce4239b297bf233a5ced27a1f7`; target5_h1_selector_experiment.json `7c8d8d82e81c341424d85b808fc870c560e65f1665dc50672e3dfcc10f11bb9a`.
- Release decision: NO RELIABLE ALERT TODAY; qualified candidates = 0. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS.


## 2026-11-20 — Run #407 T20_H5 parser-boundary reconciliation (Part 2)
- Root cause established; Part 1's provisional serialization discrepancy is superseded. The archived CSV was parsed with pandas' default float parser, which rounded three exact values 19.999999999999996 up to 20.0, creating three false threshold hits. The CSV contains sufficient precision; JSON metric is correct.
- Parser comparison: default read_csv -> 612 T20_H5 hits; read_csv(..., float_precision="round_trip") -> 609 hits. Boundary rows: REPRO (2026-09-25), AVANCE (2026-10-29), ANNAPURNA (2026-10-29). Exact float for each is 19.999999999999996 (<20).
- Reconciled 100 cutoff rows x 30 unique symbols; zero duplicate cutoff-symbol keys. Round-trip per-cutoff H+5 hits sum to 609; precision 609/3,000 = 20.30%, exactly matches JSON. H+1 648/3,000 and H+3 1,198/3,000 also reconcile.
- Ordered cutoff-symbol-outcome fingerprint SHA-256: 0739c79de53573228e369af8e0d77182665d1656bb86d2ee33abc7335a580c65. Cutoff ledger SHA-256: 54ff61432c9165863c52aa12ae9af5d9991a0460a3ae436a4e81b84bc47a4441.
- Report: docs/RUN407_T20_H5_PARSER_BOUNDARY_RECONCILIATION_PART2_20261120.md; commit 5fa3d4e56000f42713a4833cb9140d5b8c13a970. Cutoff ledger: docs/RUN407_T20_H5_CUTOFF_RECONCILIATION_20261120.csv; commit 39b49e488aec2e5c8922212cb16030ea4e30652d.
- Mandatory audit consumer control: use pandas read_csv with float_precision="round_trip"; never round future outcome labels before threshold comparison. Production scoring/selector unchanged.
- Separate live-selection blocker remains. Run #407 live_1m_status is BLOCKED_SOURCE_ACCESS_403, zero rows; final selection PROVISIONAL_ONLY_FINAL_SELECTION_BLOCKED. The 20-Nov Daily Unified Top-5 audit also reported zero qualified candidates. The provisional Top-3 are not actionable. Do not present a reliable/A+ stock until a fresh timestamped, valid live feed and all required readiness gates pass.
- Next action: inspect free official/authorized live-data source availability and schema; do not bypass access controls, use paid APIs, fabricate prices, or change the production selector. If no valid live source is available, preserve BLOCKED and report no qualified trade.
- Protected invariants unchanged: Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56x12), Engines A-E, IPO-PLX V2. UNKNOWN is never PASS.


## 2026-11-20 — Live-feed source-access assessment
- Reviewed official NSE MCP, NSE real-time data products, and NSE Data Sharing & Usage Policy. Official NSE MCP advertises free/no API key, bulk quote up to 50 symbols, and 1–3 minute delayed intraday data, but explicitly limits use to information/learning and says it is not meant for real-time trading or investment advice. This is not accepted as a substitute for the V11.3 live 1-minute ignition gate.
- NSE official real-time/1-minute snapshot products are provided through NSE Data & Analytics product channels; real-time feeds are delivered via dedicated leased line or authorized vendors, and snapshot data via SFTP/binary. No unrestricted free official 1-minute trading feed was established. Paid products excluded under user constraint.
- Current collector's fail-closed response to HTTP 403 is correct; do not bypass access controls, rotate identities, or hammer endpoints. Keep LIVE_INTRADAY_1M_FEED_MISSING BLOCKED. NSE MCP may be considered only as a separately labeled research/shadow context source if an authorized connector is available and timestamp/delay/schema/coverage checks pass.
- Report: docs/LIVE_FEED_SOURCE_ACCESS_ASSESSMENT_20261120.md; commit be45fede219fc172c024c9674457700468d09866.
- Decision: no stock promoted to reliable/A+/actionable from stale 19-Nov archive. The 20-Nov Daily Unified Top-5 audit had zero qualified candidates. If no authorized free 1-minute source becomes available, issue no actionable alert; do not weaken the readiness gate.
- Official sources: https://www.nseindia.in/nse-mcp ; https://www.nse.in/static/market-data/real-time-data-subscription ; https://www.nseindia.in/static/market-data/nse-data-policy.


## 2026-11-20 — Research continuation 41, Part 1: NSE MCP / SEBI data-use gate
- Official NSE MCP page confirms Bhavcopy is prior-session EOD (up to 5 years) and CM Market is approximately 1–3 minutes delayed, with no tick-by-tick/order-book data. NSE states information/learning only, not real-time trading, investment advice or commercial products; MCP access does not grant commercial exploitation or AI training/fine-tuning rights.
- New primary-source check: SEBI Circular HO/47/17/12(11)2025-MRD-POD3/I/11107/2026 dated 08-May-2026 specifies a 30-day lag for both sharing and usage of market-price data for investor education/awareness activities, with a one-day exception for NISM simulation lab. The circular replaces the earlier one-day/three-month provisions for those educational/awareness activities.
- Legal scope of the SEBI circular against the specific NSE MCP terms and private research workflow is not determined by this technical audit. Therefore do not assume the 1–3 minute MCP snapshot is authorized for PRECISION-WIRES selection, backtests, model training or alerts. Require written NSE terms/permission or qualified legal clarification before ingestion.
- Acceptance decision: MCP cannot replace the missing 1-minute candle feed; do not integrate it into collector/live_1m.py, production selector, engines or backtest. Keep LIVE_INTRADAY_1M_FEED_MISSING BLOCKED; no reliable/actionable stock promoted. No change to production logic.
- Report: docs/NSE_MCP_SEBI_DATA_USE_GATE_20261120.md; commit 0e64e48f43bd6aafc1a61ea015add16ee619c3dd.
- Next permissible work: build a source-permission register (owner, endpoint, permitted purpose, delay, retention, redistribution, model-training rights, authentication, written permission evidence) for all proposed free official sources. Documentation/acceptance gate only.
- Sources: NSE MCP https://www.nseindia.com/nse-mcp ; SEBI circular https://www.sebi.gov.in/legal/circulars/may-2026/norms-for-sharing-and-usage-of-price-data-for-educational-purposes_101293.html ; NSE data policy https://www.nseindia.in/static/market-data/nse-data-policy ; NSE real-time data https://www.nse.in/static/market-data/real-time-data-subscription.
- Invariants: Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. No paid API, no synthetic data, no access-control bypass. UNKNOWN is never PASS.


## 2026-11-20 — Research continuation 41, Part 2: Official Data Source Permission & Coverage Register
- Reviewed current official policy/source pages for NSE, SEBI, MoSPI/e-Sankhyiki, data.gov.in/GODL-India, RBI/DBIE, PIB and IMF; added World Bank terms as a potential comparator. No source data were downloaded/ingested and no production code or selector was changed.
- MoSPI/e-Sankhyiki: portal states open access/no registration and exposes 4,800+ catalogue datasets and APIs; OGD catalog for e-Sankhyiki is marked GODL-India. Acceptance remains resource-level conditional: inspect each actual dataset's licence metadata and retain attribution/version/vintage.
- data.gov.in: portal terms explicitly state each dataset's licence metadata controls; GODL-India grants lawful commercial/non-commercial reuse, adaptation and derivatives only for data validly licensed under it, with attribution and exclusions for third-party, personal, sensitive/non-shareable material. Status GO only where individual resource licence is GODL-India or compatible explicit licence.
- RBI DBIE: official FAQ says research use is permitted with courtesy to DBIE/RBI. This does not expressly grant commercial redistribution, sublicensing or model-training rights; those remain UNKNOWN. Internal research use with attribution only.
- PIB: PIB-owned website material may be reproduced free if accurate, not misleading/derogatory, and source prominently acknowledged; third-party material is excluded and needs separate rights. This is not a market-price feed or blanket model-training permission.
- IMF: SDMX 2.1/3.0 APIs provide programmatic access, but API access is not a blanket reuse licence. eLibrary allows individual research/teaching/fair-use; no commercial/systematic distribution, and broader rights require permission. Model-training rights remain UNKNOWN.
- NSE: Data Sharing Policy requires subscriber request and relevant agreement; research requests route through NSE Economic Policy Research Department; confidentiality declaration and specific use restrictions apply; redistribution only if agreement permits. Commercial market data is priced. No free general entitlement inferred. Live 1-minute feed remains BLOCKED.
- SEBI Circular 08-May-2026: 30-day lag for sharing and usage of market price data for investor education/awareness, with one-day NISM simulation-lab exception. This is a regulatory constraint, not a data licence; its application to a private trading research pipeline is not determined here.
- Other sources (BSE, CDSL, FBIL, FPI/FII and other depositories) remain BLOCKED/NOT REVIEWED until source-specific current policy and licence evidence is obtained. No cross-source licence assumptions.
- Deliverables: docs/OFFICIAL_DATA_SOURCE_PERMISSION_COVERAGE_REGISTER_20261120.md (commit 31b58ba777752d2aab8d65bd9349f5e757437088); machine-readable CSV docs/OFFICIAL_DATA_SOURCE_PERMISSION_COVERAGE_REGISTER_20261120.csv (commit db91a7cb23fb81af8778268d267510f09d17bf4c).
- Mandatory ingestion contract: record source owner, exact endpoint and dataset ID, publisher/original source, exact licence and metadata URL, permitted-purpose flags (research/trading/model training/publication/redistribution/commercial), publication time/reference period/retrieval time/timezone/vintage/frequency/lag, schema/units/classification, coverage/gaps, attribution, retention/deletion, redistribution restrictions, authentication/permission evidence, SHA-256, immutable path, parser version and QA status.
- Acceptance: no public URL/free download/API access alone establishes permission. Dataset-level licence metadata controls. Unknown rights stay UNKNOWN and cannot flow into the relevant use. NSE live feed remains BLOCKED; no stock is promoted to reliable/A+/actionable; no GCR boost or production integration authorized.
- Prior lessons preserved: Run #407 float threshold audit must use pandas read_csv(..., float_precision="round_trip"); NSE 403 remains fail-closed; NSE MCP 1–3 minute snapshot is not 1-minute candle/trading permission; SEBI educational lag is not assumed to be a private research exemption.
- Protected invariants: Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E, IPO-PLX V2 unchanged. No paid APIs, no synthetic observations, no access-control bypass. UNKNOWN is never PASS.


## 2026-11-20 — Research continuation 41, Part 3: MoSPI/e-Sankhyiki Macro Series Audit
- Audited MoSPI GSDD 2026, e-Sankhyiki catalogue/API docs and latest IIP, CPI, NAS/GDP and PLFS official releases. No API calls, data downloads, ingestion, production integration or selector changes were performed.
- Critical policy correction: GSDD 2026 supersedes 2019. Category A includes aggregate National Accounts, CPI, IIP NIC-2, ASI Volume I, NSS reports/factsheets and central statistics reports (free without registration); Category B includes anonymized unit/item data (registered, free non-commercial, commercial priced); Category C restricted; non-shareable data excluded. GSDD is an access/dissemination classification, not a blanket copyright/reuse/model-training/redistribution licence. GODL applies only where the exact resource metadata explicitly names it. Prior Part 2 MoSPI blanket conditional-GODL wording is superseded.
- IIP: current base 2022-23=100, NIC-2025; latest verified Sep-2026 release 28-Oct-2026, growth 6.7% YoY. Next Oct-2026 release scheduled 28-Nov-2026. API v1.0.0 endpoint GET /api/iip/getIIPData; parameter/schema/auth/rate-limit details not verified. Catalogue index still surfaced Aug-2026 records, so catalogue indexing lags press-release truth. Quick estimates subject to revisions.
- CPI: base 2024=100, COICOP 2018, HCES 2023-24 weights; latest Oct-2026 release 12-Nov-2026, CPI 6.09% provisional, CFPI 8.94% provisional; Sep final. API v2.0.0 GET /api/cpi/getCPIData; supports base years 2010/2012/2024, paginated JSON, optional bearer token, IP rate-limited; exact request parameter/page schema not extracted. Catalogue index still surfaced Sep records after Oct release.
- NAS/GDP: new base 2022-23 replacing 2011-12; catalogue has 1,724 records. Q1 FY2026-27 constant/current quarterly expenditure table IDs AEQEAFY2607QTR and AEQEAFY2608QTR, released 31-Aug-2026; macro dashboard GDP growth 7.8%. Q2 FY2026-27 scheduled 30-Nov-2026. New series release has annual FY2022-23–FY2024-25 and quarterly series Q1 FY2022-23 to Q3 FY2025-26; back series expected Dec-2026 per FAQ, not yet verified. No dedicated NAS API endpoint/schema found in reviewed docs; table downloads/press note annexures only confirmed.
- PLFS: survey design revamped Jan-2025; October-2026 monthly bulletin MB-19 dated 16-Nov-2026, 19th monthly bulletin. CWS LFPR age 15+ 55.7% all India, rural 58.4%, urban 50.5%. Monthly bulletins Apr-2025 to Oct-2026. Catalogue index still surfaced Sep records. No API schema found; catalogue Excel/CSV and bulletin tables confirmed. Keep monthly/quarterly CWS separate from annual usual status.
- Corrected existing source register: docs/OFFICIAL_DATA_SOURCE_PERMISSION_COVERAGE_REGISTER_20261120.md commit 90d15914649d5ac8ff4824de95b32365576acd8a; CSV commit b09ff6b34f3209e325a24070dde321c85ba80cd7.
- Part 3 deliverables: docs/MOSPI_ESANKHYIKI_MACRO_SERIES_AUDIT_PART3_20261120.md commit e03458909027365d900c82f905b074c9eb1347b7; machine-readable CSV docs/MOSPI_ESANKHYIKI_MACRO_SERIES_AUDIT_PART3_20261120.csv commit 07b39ab902c943516c33a536034e5dcaee9c4bc2.
- Catalogue freshness control added: always reconcile indexed table period against dated press release and advance release calendar; use actual official release timestamp as operational freshness truth. Catalogue indexing lag identified for IIP, CPI and PLFS.
- Required next technical step: inspect the published IIP/CPI OpenAPI YAML schema and exact parameters in an authorized, bounded read-only environment; then perform one controlled guest/API metadata-only test only after permitted use is confirmed. For NAS/PLFS, inspect exact Excel/CSV table exports and compute coverage/vintage fingerprints. Do not guess parameters or write production collectors yet.
- Acceptance: policy/source research COMPLETED; IIP/CPI endpoint names PARTIAL verified; full OpenAPI schema NOT VERIFIED; NAS/PLFS API NOT ESTABLISHED; historical full-span coverage NOT VERIFIED; resource-level reuse/training rights NOT VERIFIED; production GCR integration NOT AUTHORIZED. No GCR score boost and no stock-selection status change.
- Invariants unchanged: Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E, IPO-PLX V2. No paid API, no synthetic observations, no access-control bypass, no fabricated timestamps. UNKNOWN is never PASS.


## 2026-11-20 — Research continuation 41, Part 4: BSE sector TRI rights/admission gate
- Pre-task continuity check completed before selecting work: fetched current master continuity ledger and searched repository for (a) IIP/CPI API schema work, (b) Brazil BCB 22905 capture, (c) India FPI NSDL/CDSL raw captures, and (d) BSE sector TRI. Confirmed IIP/CPI release/source audit had just been repeated and must not be repeated; BCB SGS 22905/22906/22925/22940 raw capture already PASS (run 44538278638, artifact 14535963861, ZIP SHA ee226a0525edd6974b8e0f3205005d3d5913f3014137065b074890b353ecdf60); CDSL/NSDL seven-page raw capture and multiple follow-on schema/matched-date audits already exist; Continuation 74 explicitly named BSE sector TRI as next action and no prior BSE sector TRI history acquisition/admission was found.
- Reviewed official BSE Indices Terms of Use and Legal Disclaimer. Terms state BISPL data may be used solely for internal business purposes unless otherwise permitted; prohibit using data to create/develop indices, classification systems or historical databases; prohibit creating derived data absent BISPL express written consent; restrict duplication/display/redistribution/resale. Legal disclaimer prohibits modifying/reproducing/distributing/storing index content in a database/retrieval system without prior written permission.
- Official BSE methodology distinguishes PR from Gross TR (regular cash dividends reinvested at ex-date close) and says daily constituent/index-level data are available via subscription. Example TR tickers confirmed: BSEMFGT, BSEINFRT, BSEFXBT, BSEHOUT. Public factsheets show selected TRI summary performance, not full daily history or a research database licence.
- Decision: BSE sector TRI historical data NOT ADMITTED to GCR database or derived sector-transmission panel under current public terms. Historical database creation and derived data require permission; no free research exception identified. No data download or scrape attempted. This is a rights blocker, not a source/data-quality PASS.
- Report: docs/GCR_BSE_SECTOR_TRI_SOURCE_RIGHTS_ADMISSION_GATE_20261120.md; commit 752a90fb44733e49c6ead75a2f4291eab07f034b.
- Acceptance: provider identified PASS; PR/TR methodology distinction PASS; daily historical data public/free NOT_ESTABLISHED; database creation BLOCKED; derived panel BLOCKED; full daily TRI history NOT_DONE; exact CDSL sector taxonomy-to-TRI mapping NOT_DONE; GCR sector transmission BLOCKED.
- Next non-duplicative step: rights-screen official NSE Indices historical TRI source or another official source before acquisition; do not presume NSE terms permit database creation. If no source has suitable free rights, keep sector-return factor UNKNOWN and exclude from GCR scoring. No price-return proxy or sector mapping assumption.
- Carry-forward corrections: IIP/CPI release audit in Part 3 was a duplicate; do not repeat. BCB raw archive already PASS. CDSL/NSDL capture already PASS but specific NSDL Archive ASP.NET postback and CDSL row-level archive/sector file parsing remain distinct pending tasks. Brazil PA Changelog owner-side dependency remains blocked.
- Protected invariants unchanged: Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E, IPO-PLX V2. No paid APIs, no scraping/access bypass, no synthetic data, no production integration. UNKNOWN is never PASS.


## 2026-11-20 — Research continuation 42: NSE Indices historical TRI rights gate
- Preflight: read the Master Continuity Ledger and searched prior reports for NSE TRI route, historical index data and licensing. Existing NSE historical TRI route discovery was already recorded in `docs/GCR_NSE_NIFTY50_INDIA_VIX_RAW_ACQUISITION_GATE_CONTINUATION42_PART5_20261119.md`, `docs/GCR_NSE_HISTORICAL_INDEX_VIX_SAMPLE_INTEGRITY_REVIEW_CONTINUATION42_PART6_20261119.md`, and the GCR source register. Route discovery was rejected as duplicate; this task was limited to the unresolved rights/admission question.
- BSE TRI rights review was already completed in `docs/GCR_BSE_SECTOR_TRI_SOURCE_RIGHTS_ADMISSION_GATE_20261120.md`; not repeated.
- Official NSE Indices Historical Data page exposes a separate Total Returns Index Values interface and Total Returns Index / Net Total Return Index result fields with CSV format: https://www.niftyindices.com/reports/historical-data . This proves public interface availability only, not reuse rights.
- Official NSE Indices Products & Services states use of NSE Indices data/name/indices requires a licence or subscription, licensing is mandatory for tracking index performance, and index data subscription is a paid service: https://www.nse.in/static/nse-indices/products-services .
- Official Index Data Subscription page describes historical data and quantitative research use cases but directs users to licensing opportunities and asserts proprietary rights: https://www.nse.in/static/nse-indices/index-data-subscription .
- NSE Data Sharing & Usage Policy separately governs NSE/NSE Data market-data products; historical data are included in its definition, use is controlled by Relevant Agreement, and research requests follow a documented route. This policy is not misrepresented as the complete NSE Indices TRI licence: https://www.nseindia.in/static/market-data/nse-data-policy .
- Decision: NSE TRI/NTR is NOT ADMITTED to the GCR historical database or derived sector-transmission panel. Public CSV/UI is not a free reuse licence. No explicit permission for persistent historical database creation or derived analytical data was established. This is NOT a claim that technical data availability is absent and is not a legal opinion.
- Acceptance: official provider PASS; TRI/NTR interface PASS; exact series distinction PASS; free reuse permission NOT_ESTABLISHED; database/derived analytics permission UNKNOWN; historical TRI acquisition NOT_DONE; GCR admission BLOCKED.
- No download, scraping, hidden endpoint probing, database build, ingestion or production integration was performed. No paid subscription.
- Reopen only with explicit official open licence or written provider permission covering internal research storage, persistent database creation, derived analytics, retention and disclosure scope. Keep PR/TRI/NTR separate.
- Report: `docs/GCR_NSE_INDICES_HISTORICAL_TRI_SOURCE_RIGHTS_ADMISSION_GATE_20261120.md`; report commit `2d70eb36af0a5c270f17fba70131498d2cea3845`.
- Next work must be selected by a fresh ledger preflight among distinct unfinished GCR tasks; do not repeat TRI route discovery, BSE/NSE rights gates, Brazil BCB SGS raw capture or Brazil Registration URN lifecycle validation. Candidate remaining gaps include raw IMF BOP DSD/codelist/dataflow and specific CDSL/NSDL archive parsing, but verify latest evidence before choosing.
- Protected invariants unchanged: Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2. No synthetic data, fabricated timestamps or access-control bypass. UNKNOWN is never PASS.


## 2026-11-20 — Dependency-ordered GCR priority queue + South Africa Q2-2026 source mapping
- User raised a valid process issue: tasks had been selected without a stable dependency-ordered priority plan. New durable execution order is documented in `docs/GCR_MASTER_PRIORITY_QUEUE_AND_ZAF_Q2_2026_SOURCE_MAPPING_20261120.md`; rank order: (1) 63-country EMDE national-source sign/scale/vintage validation, (2) Brazil PA owner-side identity/Changelog dependency, (3) India FPI/DII daily lineage and NSDL/CDSL reconciliation, (4) synchronized global macro panel, (5) TRI/sector taxonomy rights+mapping, (6) relative-attraction/sector transmission/OOS backtest, (7) production integration only after independent evidence and explicit approval.
- Preflight re-opened the current ledger and relevant IMF BOP, 154-member panel, 63-country Q2 cohort, country-scale reconciliation, SARB, CDSL/NSDL, Brazil PA, and TRI reports. Completed work rejected from repetition: IMF BOP DSD V2.6.0 capture (run 44473409770); IMF BOP public flow/154-member panel/12-country exact-key and 9,299-row structural QA; Brazil BCB raw captures/accounting identities and Registration URN 40/40 lifecycle; India Table197/Table42 completed checks; CDSL 15-Nov sector capture and 192/192 arithmetic; BSE/NSE TRI rights gates. Brazil tx2 public API probes already exhausted; no retries.
- Selected rank-1 country-validation increment: South Africa (ZAF) Q2-2026. Reused existing 63-country 2026-Q2 dual-leg roster; no cohort rebuild. Retrieved official SARB September-2026 Statistical Tables, External Economic Accounts, quarterly BOP table (page S-87/PDF page 3): https://www.resbank.co.za/content/dam/sarb/publications/quarterly-bulletins/quarterly-bulletin-publications/2026/september/8-tables-external-economic-accounts.pdf
- Official SARB Q2-2026 values (R million): portfolio net incurrence of liabilities code 5644K = -9,023; components 5756K equity/fund shares = -34,161 and 5757K debt securities = +25,138; exact subtotal -9,023. Portfolio net acquisition of financial assets code 5660K = -68,769; components 5758K equity/fund shares = -42,915 and 5759K debt securities = -25,854; exact subtotal -68,769.
- Official SARB note 4 defines signs: positive liability incurrence is capital inflow; negative is disposal/outflow. Negative net acquisition of assets is outflow; positive disposal of assets is inflow. Both Q2 portfolio legs are negative/outflow under SARB convention. SARB notes previous four years are preliminary and subject to revision.
- This is official national-source code/label/unit/value/subcomponent arithmetic/sign validation: PASS. Exact IMF-vs-SARB numeric reconciliation, currency conversion and vintage equivalence remain NOT_DONE; no ZAR/USD conversion attempted. ZAF overall validation remains PARTIAL / NOT PASS; 63-country aggregate remains NOT_AUTHORIZED.
- Report and ordered queue: `docs/GCR_MASTER_PRIORITY_QUEUE_AND_ZAF_Q2_2026_SOURCE_MAPPING_20261120.md`; commit `7604d20beb4a5243e6329ceb017a93bc09f6f1fa`.
- Next exact task: retrieve the existing IMF ZAF 2026-Q2 raw row and receipt; align it against SARB values using an official dated quarterly FX convention or an official SARB USD-equivalent series. Preserve original currencies; no conversion without source/vintage proof. After this, continue the same ranked country-validation queue.
- No paid data, synthetic data, fabricated timestamps, silent FX conversion, access-control bypass, repeated completed audit, or production change. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS.


## 2026-11-20 — GCR South Africa ZAF Q2-2026 exact IMF↔SARB/OECD FX reconciliation
- Reused the existing WEO 154-member panel, 63-country Q2 dual-leg cohort, 12-country exact-key receipts, and SARB September-2026 quarterly BOP table. No panel/cohort rebuild and no repeat SARB table extraction.
- IMF exact-key receipt (run 44474458684; artifact 14505009889; ZIP SHA-256 `588101c0deff3b4310984dae5eabcac64fc8288f4416854b7676b4b6ff6b4cd7`) contains ZAF asset and liability series. Exact receipt: `docs/evidence/imf_bop_emde_20261119/exact_sample_checks/summary.json`; ZAF_A_NFA_T.csv SHA-256 `6a4211d9c6475113a652474fa5463acab1a7e2c4e4341cb37352d1d80d0248bb`; ZAF_L_NIL_T.csv SHA-256 `af1655d66cfd815b4aece4dc923ab8f6510c8f26e19cfb05ccb928803c45070f`. Both exact GETs HTTP 200, receipt timestamps 2026-11-19T06:45:24.259338Z and 06:45:24.711771Z, both series end 2026-Q2.
- IMF 2026-Q2 raw values: A_NFA_T = +4,174,854,099.360882 USD; L_NIL_T = -547,771,649.1229077 USD. IMF SCALE=6 metadata means Millions, consistent with the previously validated country-specific conversion practice; preserve raw values and SCALE as separate fields, and use raw/1e6 only for comparison.
- SARB September-2026 Quarterly Bulletin, published 2026-09-29, Table KB502 / page S-87 / PDF page 3, unit R millions: 5660K net acquisition of portfolio financial assets = -68,769; 5644K net incurrence of portfolio liabilities = -9,023. Components reconcile exactly: -42,915 + -25,854 = -68,769; -34,161 + 25,138 = -9,023. SARB note 4 defines the sign meanings. Previous four years are preliminary and revisable.
- FX conversion source: OECD Main Economic Indicators quarterly average daily-rate series for South Africa, surfaced in FRED series CCUSMA02ZAQ618N. Q2-2026 = 16.4719712481963 ZAR/USD; FRED/ALFRED shows the OECD release vintage 2026-08-17. Source metadata identifies OECD as the source, quarterly frequency, not seasonally adjusted, Rand per USD. This is an OECD quarterly average, not an SARB-published rate; retain source attribution and vintage. Source URLs: https://fred.stlouisfed.org/series/CCUSMA02ZAQ618N and https://alfred.stlouisfed.org/release?et=&ob=pv&od=desc&pageID=3&rd=2026-08-17&rid=205&t=exchange+rate .
- Like-for-like comparison in USD millions: SARB liabilities -9,023 / 16.4719712481963 = -547.779003742; IMF liabilities -547.771649123; residual IMF−SARB = +0.007354619 USDm. This is within the ±0.0304 USDm bound implied by SARB integer-R-million rounding.
- Asset comparison requires explicit sign reversal because SARB's note 4 and IMF A_NFA_T use opposite numeric signs for the same outflow meaning in this mapping: (-68,769 / 16.4719712481963) × -1 = +4,174.910152756 USDm; IMF A_NFA_T / 1e6 = +4,174.854099361 USDm; residual = -0.056053395 USDm. This exceeds the ±0.0304 USDm SARB integer-R-million rounding bound; do not widen tolerance to force a pass. Mark asset numerical match REVIEW / OUTSIDE_ROUNDING_BOUND.
- Acceptance: ZAF cohort membership PASS; IMF exact receipt PASS; SARB official national values/components/signs PASS; OECD quarterly FX source/vintage PASS; liability numeric comparison PASS; asset numeric comparison REVIEW; complete ZAF dual-leg numeric reconciliation PARTIAL / NOT PASS; 63-country aggregate remains NOT_AUTHORIZED. No netting, aggregation, imputation, or production changes.
- Durable detail report: `docs/GCR_ZAF_Q2_2026_IMF_SARB_OECD_FX_RECONCILIATION_20261120.md`. No selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A–E, IPO-PLX V2, weights or trade gates changed. UNKNOWN is never PASS.


## 2026-11-20 — GCR China CHN Q2-2026 SAFE vs IMF comparison
- Reused the existing 63-country Q2 both-leg cohort and exact-key receipt; no rebuild or new IMF query. CHN is in the 12-country sample.
- IMF receipt run 44474458684 / artifact 14505009889 / ZIP SHA-256 `588101c0deff3b4310984dae5eabcac64fc8288f4416854b7676b4b6ff6b4cd7`. Q2-2026 raw values: A_NFA_T +48,794,459,103.55 USD; L_NIL_T +43,286,600,714.23 USD. Raw CSV hashes and exact receipt times are recorded in the CHN report.
- Official SAFE release 000014453-2026-0068, 2026-09-29, direct USD-denominated Q2 2026 BPM6 BOP table: portfolio assets -USD 48.8bn; liabilities +USD 43.3bn; total portfolio investment -USD 5.5bn. Published identity -488 + 433 = -55 (USD 100m units).
- IMF/SAFE absolute magnitude residuals: assets 5.540896 USDm; liabilities 13.399286 USDm. Both are within the SAFE table's ±50 USDm half-unit display rounding. Liability sign also matches. Asset sign does not: SAFE assets negative, IMF A_NFA_T positive. No sign flip applied; source concept/sign crosswalk remains unresolved.
- CHN: IMF exact retrieval PASS; SAFE official source and arithmetic PASS; liability comparison PASS at rounded precision; asset magnitude corroboration only, sign REVIEW; full dual-leg national validation PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Detail report: `docs/GCR_CHINA_CHN_Q2_2026_SAFE_IMF_BOP_COMPARISON_20261120.md`. Next action is SAFE detailed time-series BOP export/concept metadata and asset sign mapping; do not use IIP stock data as a flow substitute.


## 2026-11-20 — CHN SAFE detailed BOP workbook access audit
- Continued the open CHN asset sign-mapping task after preflighting the Master Ledger, priority queue, CHN/ZAF reports, cross-country evidence and fixed 63-country cohort. No completed panel, IMF receipt, or prior national-source audit was repeated.
- Official SAFE Data and Statistics navigation reaches the Balance of Payments category and the dated detailed series page (dispatch 2026-09-29, index 000014453-2019-0016). The page links the XLSX at https://www.safe.gov.cn/en/file/file/20260929/20c1e5e45d704a77b302ba234211a75b.xlsx.
- Browser extraction rejects the XLSX MIME type and direct byte download failed in the current environment. Workbook content, sheets, exact detailed rows, revision metadata and hash therefore remain NOT_INSPECTED / NOT_DONE. Do not claim a sign crosswalk.
- SAFE Q2 abridged release (index 000014453-2026-0068) still supports assets -USD48.8bn, liabilities +USD43.3bn, total portfolio -USD5.5bn; its note 2 says credit positive/debit negative; note 8 says BOP data is revised regularly. This does not independently explain IMF A_NFA_T sign for assets.
- CHN liability comparison remains PASS at rounded display precision; asset sign mapping REVIEW; full CHN dual-leg validation PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Detailed audit: `docs/GCR_CHINA_CHN_SAFE_DETAILED_BOP_TIME_SERIES_ACCESS_AUDIT_20261120.md`. Next action: retrieve exact XLSX bytes via supported owner-side browser/workflow route, hash and inspect row metadata; do not use IIP stock or cumulative Q3 values as substitute.


## 2026-11-20 — Indonesia IDN Q2-2026 Bank Indonesia vs IMF portfolio BOP validation
- Preflighted latest Master Ledger, GCR priority queue, CHN/ZAF reports, cross-country evidence and fixed 63-country cohort; omitted all completed PASS work. IDN selected from the existing cohort; reused existing 12-country exact-key receipt, with no panel rebuild or new IMF query.
- Existing IMF receipt run 44474458684 / artifact 14505009889 / ZIP SHA-256 `588101c0deff3b4310984dae5eabcac64fc8288f4416854b7676b4b6ff6b4cd7`. IDN A_NFA_T raw CSV SHA-256 `db7198b4c2ccc7bcbe6c45312506913c71507339c6e7bd609c5e1ff6500aae8b`; L_NIL_T SHA-256 `4ec6d04eae8187bd4235c6120f3be5f67972ff32ebfea1accf6cd0a1ab2b4108`. Both HTTP 200, each exact series matches all 46 broad observations/attributes, 2015-Q1–2026-Q2.
- IMF Q2-2026 raw values: assets +1,487,605,237.21664 USD; liabilities +11,440,221,641.9221 USD (SCALE=6, Millions).
- Bank Indonesia SEKI Table V.7, official “Financial Account: Portfolio Investment”, Q2** 2026, USDm: assets -1,488; liabilities +11,440; total +9,953. Q2 marked ** = Very Temporary Data. Source https://www.bi.go.id/SEKI/tabel/TABEL5_7.pdf.
- Both absolute magnitude residuals are within ±0.5 USDm BI whole-million display rounding. Liability signed comparison PASS (residual +0.221642 USDm). Asset magnitude residual 0.394763 USDm but signed comparison conflicts (BI negative vs IMF positive): REVIEW; no sign flip authorized. IDN full dual-leg validation PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Detail report: `docs/GCR_INDONESIA_IDN_Q2_2026_IMF_BANK_INDONESIA_BOP_RECONCILIATION_20261120.md`. Next action: obtain official BI methodology/concept-sign mapping and same-vintage revision metadata for A_NFA_T; do not substitute IIP stocks or infer from total financial account.


## 2026-11-20 — IDN official BI BPM5 sign convention crosswalk
- Preflighted current Master Ledger, priority queue, IDN report, CHN/ZAF reports, cross-country benchmark and fixed cohort; skipped completed PASS tasks and reused the existing IMF receipt.
- Official BI BPM6 implementation note explicitly states the BPM5 +/- convention was retained; its footnote defines financial inflow (asset reduction/liability increase) as positive and outflow (asset increase/liability reduction) as negative. Official BI BOP metadata independently defines portfolio assets as residents' acquisition of nonresident securities and liabilities as nonresidents' acquisition of resident securities, and states BI presents asset/liability capital-financial entries as net inflow/outflow (+ inflow/credit, − outflow/debit).
- Therefore BI portfolio asset acquisition is negative under BI's retained convention while IMF A_NFA_T net acquisition is positive: an explicit BI→IMF sign inversion is methodologically supported for this asset comparison. Liability sign remains positive and consistent with L_NIL_T. No transform is generalized to other countries.
- Existing Q2-2026 BI values (V.7, USDm): assets -1,488; liabilities +11,440. Applying the documented mapping: assets +1,488 vs IMF +1,487.605237 USDm, residual -0.394763; liabilities +11,440 vs IMF +11,440.221642, residual +0.221642. Both PASS within BI's ±0.5 USDm whole-million display-rounding bound.
- BI Q2 2026 report published 2026-08-21 and page updated 2026-09-17; Table V.7 Q2 is ** Very Temporary Data. BI revision metadata says final status occurs five months after first release; current Q2 remains provisional. IMF exact-key receipt retrieval was 2026-11-19, but exact BI↔IMF same-vintage alignment is not established.
- Thus IDN sign crosswalk and both rounded numerical legs PASS; same-vintage national dual-leg validation remains PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Detail: `docs/GCR_INDONESIA_IDN_BPM5_SIGN_CONVENTION_CROSSWALK_AND_Q2_2026_RECHECK_20261120.md`. Next action is a dated BI Q2 revision snapshot/vintage bridge; if unavailable, retain the limitation and advance to the next cohort country.


## 2026-11-20 — Saudi Arabia SAU Q2-2026 SAMA vs IMF portfolio BOP validation
- Preflighted Master Ledger, GCR priority queue, IDN sign crosswalk, CHN blocker, cross-country benchmark and fixed 63-country cohort; skipped all completed PASS work. After IDN sign mapping was closed but same-vintage remained unresolved, selected SAU from the existing cohort. Reused existing 12-country exact-key IMF receipt; no panel rebuild or new IMF GET.
- IMF receipt run 44474458684 / artifact 14505009889 / ZIP SHA-256 `588101c0deff3b4310984dae5eabcac64fc8288f4416854b7676b4b6ff6b4cd7`. SAU A_NFA_T raw CSV SHA-256 `7574486199f032a8eabfdc2dc38e21f0f70247165537a5732777032de0cbc76d`; L_NIL_T SHA-256 `b2c557662bcfaf22771a3ef50f4d43c48f664abea32d31118adcab5c58cdd926`. Both HTTP 200, 46/46 broad-key matches, 2015-Q1–2026-Q2.
- IMF Q2-2026 values: A_NFA_T +9,663.782086 USDm; L_NIL_T +6,381.234539 USDm (raw values and SCALE=6 retained).
- SAMA September 2026 Monthly Statistical Bulletin, Table 1 Balance of Payments, Contd.6, printed/PDF page 131, USDm, Q2 2026 explicitly estimated (e): net acquisition of portfolio assets +9,664; net incurrence of portfolio liabilities +6,381; portfolio balance +3,283.
- Asset residual IMF−SAMA -0.217914 USDm; liability residual +0.234539 USDm; both within ±0.5 USDm whole-million display-rounding. Signs/concepts match without transform. Both numerical legs PASS.
- Exact SAMA↔IMF same-vintage alignment not established: SAMA values are estimated; IMF receipt timestamp alone is not a source-vintage identity. SAU full national dual-leg validation remains PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Detail report: `docs/GCR_SAUDI_ARABIA_SAU_Q2_2026_SAMA_IMF_PORTFOLIO_BOP_RECONCILIATION_20261120.md`. Next action: seek dated SAMA Q2 estimate revision archive / subsequent revised observation; if unavailable retain PARTIAL and advance within fixed cohort.


## 2026-11-20 — SAU Q2-2026 source-vintage follow-up
- Preflighted current Master Ledger, GCR priority queue, SAU reconciliation report and CHN audit. Did not repeat SAU numeric extraction or IMF exact-key retrieval.
- SAMA official calendar lists the October 2026 monthly bulletin for 29-Oct-2026 and November 2026 bulletin for 29-Nov-2026. Latest available September 2026 bulletin still marks Q2-2026 portfolio rows as e = Estimate.
- IMF DSBB metadata describes general BOP revisions as usually three months after reference quarter, but this does not establish that these exact Q2 portfolio rows were revised. No dated public revised Q2 asset/liability observation or same-vintage bridge was found in the official material inspected.
- SAU asset and liability numeric comparisons remain PASS at published rounding; same-vintage identity NOT_ESTABLISHED; full national dual-leg validation PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Detail audit: docs/GCR_SAUDI_ARABIA_SAU_Q2_2026_SOURCE_VINTAGE_FOLLOWUP_AUDIT_20261120.md. Advance to next eligible country in fixed cohort using existing IMF receipt; no duplicate IMF GET or cohort rebuild.
- Protected invariants unchanged; UNKNOWN is never PASS.


## 2026-11-20 — Poland POL Q2-2026 official NBP source gate
- Preflighted latest Master Ledger, GCR priority queue, SAU and CHN evidence. Selected POL from the existing 12-country IMF exact-key receipt; no new IMF request or cohort rebuild.
- Reused artifact 14505009889 (run 44474458684; ZIP SHA-256 588101c0deff3b4310984dae5eabcac64fc8288f4416854b7676b4b6ff6b4cd7). POL Q2-2026 IMF values: A_NFA_T +6,602,000,000 USD; L_NIL_T +19,391,000,000 USD. Raw CSV hashes: A 19ba3d8918245d7abe73125d76c08e27f9970817cc1a46b8753763352e5a2e21; L 365bac8801d0951f3d69f863628e844c6da07b0e69651880614c815b859c769b.
- Official NBP quarterly workbook locator bop_q.xlsx is linked from NBP's BOP PDF, but workbook bytes/metadata/hash could not be retrieved. PDF front matter says March 2026 / dated 15-May-2026 / April release 12-Jun-2026, while later tables show Q2/Q3 2026 columns. This internal vintage/date conflict means later table values are quarantined and not used as a benchmark.
- NBP workbook inspection BLOCKED / NOT_DONE; POL national asset/liability comparisons NOT_DONE; POL full validation BLOCKED; aggregate NOT_AUTHORIZED.
- Detail: docs/GCR_POLAND_POL_Q2_2026_NBP_IMF_SOURCE_GATE_AUDIT_20261120.md. Next action: retrieve/hash/inspect exact NBP XLSX through supported file transfer; if still blocked, move to next eligible cohort country.


## 2026-11-20 — Türkiye TUR Q2-2026 TCMB vs IMF portfolio BOP validation
- Preflighted current Master Ledger, GCR Priority Queue, POL NBP blocker, SAU vintage audit and CHN access audit. POL's previously failed NBP XLSX path was not retried. Selected TUR from existing 12-country IMF exact-key sample; no new IMF GET or panel/cohort rebuild.
- Reused artifact 14505009889 / run 44474458684 / ZIP SHA-256 588101c0deff3b431098e0f3205005d3d5913f3014137065b074890b353ecdf60. TUR A_NFA_T raw CSV SHA-256 380018babf368f4e66c49f2c1753e5adc496088f3d0d71e4e4676c8c252f529f; L_NIL_T SHA-256 b8852a6b3e5ddbc7e84ecd47786cc71413b3daf74021791a438d6b0638a5df1d. Both HTTP 200, 46/46 broad-key matches; retrieved 2026-11-19T06:45:23.329543Z and 06:45:23.717012Z.
- IMF Q2-2026 values: A_NFA_T +USD5,749m; L_NIL_T +USD9,270m.
- Official TCMB September 2026 monthly detailed BOP table, USDm: April/May/June portfolio assets 2,368/1,266/2,115 (Q2 sum 5,749); liabilities 6,334/-1,802/4,651 (Q2 sum 9,183). Asset leg matches at displayed precision; liability residual IMF−TCMB +USD87m, beyond whole-million rounding.
- TCMB revision policy states current-year and previous-year monthly data may be revised with monthly dissemination. Official data ZIP locator found, but ZIP bytes/hash/revision metadata not inspected due retrieval timeout. IMF retrieval timestamp does not establish same TCMB vintage. Do not attribute the 87m gap to revisions without evidence.
- TUR asset numeric comparison PASS; liability REVIEW / NOT PASS; same-vintage NOT_ESTABLISHED; full dual-leg validation PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Detail report: docs/GCR_TURKIYE_TUR_Q2_2026_TCMB_IMF_PORTFOLIO_BOP_RECONCILIATION_20261120.md. Next: retrieve/hash/inspect TCMB September 2026 data ZIP and revision metadata via supported transfer route; no new IMF query.


## 2026-11-20 — TUR TCMB August-to-September PDF vintage cross-check
- Compared the official TCMB August 2026 and September 2026 BOP PDF snapshots; no repeat of IMF retrieval. Both show Q2 portfolio asset monthly values 2,368 / 1,266 / 2,115 USDm and liability values 6,334 / -1,802 / 4,651 USDm.
- Q2 sums in both snapshots: assets 5,749 USDm; liabilities 9,183 USDm. Existing IMF Q2 values: assets 5,749; liabilities 9,270 USDm. Asset residual 0; liability residual +87 USDm. The discrepancy persists unchanged across the two PDF snapshots; no August-to-September revision observed in those PDFs.
- This is limited two-snapshot evidence only, not a full revision-history proof or exact same-vintage identity. TCMB September ZIP bytes/hash/raw revision metadata remain NOT_INSPECTED due endpoint timeout. TUR remains PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Detail report updated: docs/GCR_TURKIYE_TUR_Q2_2026_TCMB_IMF_PORTFOLIO_BOP_RECONCILIATION_20261120.md. Next: obtain official September ZIP through supported transfer route; if unavailable, preserve blocker and advance to next cohort member.


## 2026-11-20 — Mexico MEX Q2-2026 Banxico vs IMF portfolio BOP validation
- Preflighted latest Master Ledger, GCR Priority Queue and TUR/POL/SAU/CHN detail reports. Did not repeat blocked TCMB ZIP retrieval or any completed country extraction. Selected MEX from the existing 12-country IMF exact-key sample; no new IMF GET or cohort/panel rebuild.
- Reused artifact 14505009889 / run 44474458684 / ZIP SHA-256 588101c0deff3b431098e0f3205005d3d5913f3014137065b074890b353ecdf60. MEX A_NFA_T raw CSV SHA-256 a404aca5a719b9558e75b9483b925d18011fa2d9199937d275956782a84c5014; L_NIL_T SHA-256 1a7de8eb3d258875fbffbde987ce22db437eadbdd9c93e05acec12a4ab7785c7.
- IMF Q2-2026 values: A_NFA_T +USD8,937.255098m; L_NIL_T +USD10,561.285114m. Official Banxico Q2 2026 release (25-Aug-2026), Cuadro 3, USDm: net acquisition of portfolio assets +8,937; net incurrence of liabilities +10,561; portfolio investment balance -1,624 (=8,937−10,561).
- Residuals IMF−Banxico: assets +0.255098 USDm; liabilities +0.285114 USDm; both within ±0.5 USDm whole-million rounding. Concepts/signs align; no FX or sign transform.
- Banxico says components may be revised in future releases. Exact Banxico↔IMF same-vintage bridge is NOT_ESTABLISHED; numeric legs PASS but MEX full national dual-leg validation remains PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Detail report: docs/GCR_MEXICO_MEX_Q2_2026_BANXICO_IMF_PORTFOLIO_BOP_RECONCILIATION_20261120.md. Next: locate versioned Q2 vintage/revision record; if unavailable preserve PARTIAL and advance cohort.


## 2026-11-20 — MEX Banxico live SIE CE174 current-series cross-check
- Re-opened official Banxico SIE CE174 (quarterly BPM6 BOP, USDm, current flows) and CA410 summary after preflighting latest ledger, priority queue and MEX/TUR/POL reports. No duplicate IMF retrieval or original Q2 extraction.
- CE174 latest period Apr–Jun 2026: portfolio balance -1,624; net acquisition of portfolio assets +8,937; net incurrence of portfolio liabilities +10,561 USDm. The table footnote states observations are preliminary and subject to revisions. Current live values match the 25-Aug-2026 release exactly at published whole-million precision.
- This is a second official Banxico publication surface and supports the current Q2 values; it is not a dated revision log or historical vintage archive and does not establish which vintage the IMF 2026-11-19 values used.
- MEX numeric legs remain PASS; exact same-vintage identity NOT_ESTABLISHED; full national validation PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Detail report updated: docs/GCR_MEXICO_MEX_Q2_2026_BANXICO_IMF_PORTFOLIO_BOP_RECONCILIATION_20261120.md. Do not infer same-vintage from current SIE match.


## 2026-11-20 — Argentina (ARG) Q2-2026 INDEC national portfolio validation
- Preflighted current ledger, GCR queue, MEX/TUR/POL reports and IMF panel report; excluded completed PASS work and selected ARG from the existing 12-country exact-key IMF sample. No new IMF GET or panel rebuild.
- Reused run 44474458684 / artifact 14505009889 / ZIP SHA-256 588101c0deff3b431098e0f3205005d3d5913f3014137065b074890b353ecdf60. ARG raw A_NFA_T CSV SHA-256 31ed92d953089ee94eb3c46aa486e8ff32f738e2c4c5e994f40d60e5952160ab; L_NIL_T SHA-256 51e19d9729de105b99f65601155b7c721ec0b0a593e262957c09e87b6b46cfc2.
- IMF Q2 values: assets +USD2,230.206322m; liabilities +USD7,041.052824m. INDEC Q2 report (29-Sep-2026), Table I.13, USDm: ANAF +2,230; ENP +7,041; portfolio balance -4,811. Residuals +0.206322 and +0.052824 USDm; both within ±0.5 whole-million rounding. Concept/sign mapping direct; no FX or sign transform.
- INDEC marks Q2 2026 provisional and subject to revision. Revision annex compares releases only through Q1 2026; no Q2 prior-vintage portfolio bridge. Same-vintage identity NOT_ESTABLISHED; ARG full dual-leg validation PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Detail report: docs/GCR_ARGENTINA_ARG_Q2_2026_INDEC_IMF_PORTFOLIO_BOP_RECONCILIATION_20261120.md. Next: seek versioned INDEC Q2 SDMX-ML vintage/revision evidence; otherwise advance cohort without same-vintage assumption.


## 2026-11-20 — BGD Bangladesh Bank Q2-2026 portfolio source gate
- Preflighted current ledger, GCR queue, ARG/MEX reports and IMF panel evidence; did not repeat completed PASS work. ARG official live BOP SDMX-ML link was identified but browser extraction rejected XML MIME; Datos Argentina quarterly resource timed out. No historical version/change-log proof obtained; same routes not to be retried repeatedly.
- Selected BGD from existing exact-key IMF sample; reused run 44474458684 / artifact 14505009889 / ZIP SHA-256 588101c0deff3b4310984dae5eabcac64fc8288f4416854b7676b4b6ff6b4cd7. Raw BGD A_NFA_T CSV SHA-256 67b7d5a7460fa096a85471b597fe7be5893576e5bbf01a0481acf40bee043106; L_NIL_T SHA-256 de54a736d8cb3975c62a3fe762354921057555dbda830df7f5b8aacf609aafe0.
- IMF Q2 2026 A_NFA_T=0 USD; L_NIL_T=-USD113.334678m. Bangladesh Bank Quarterly Vol XXIII No.4 Table V.1 publishes FY26 Q4 (Apr-Jun 2026) portfolio investment net -109 USDm, but not separate portfolio asset/liability legs. Do not back-solve split or infer sign mapping. National dual-leg validation BLOCKED / NOT PASS; same vintage NOT_ESTABLISHED; aggregate NOT_AUTHORIZED.
- Detail: docs/GCR_BANGLADESH_BGD_Q2_2026_BANGLADESH_BANK_IMF_PORTFOLIO_SOURCE_GATE_20261120.md. Next: find official separate asset/liability portfolio rows with dated vintage/sign metadata; if unavailable preserve BLOCKED.


## 2026-11-20 — BGD Bangladesh Bank NSDP SDMX source-route audit
- Follow-up to BGD BLOCKED gate: official Bangladesh Bank NSDP page lists BOP Browse Data, Download in SDMX and DSBB Metadata. Exact routes: `https://www.bb.org.bd/econdata/nsdp/browsefile/bpm6_bgd.xls`, `https://www.bb.org.bd/econdata/nsdp/xml/bgd/bop6_bgd.xml`, and alternate presentation `https://www.bb.org.bd/econdata/nsdp/xml/bgd/bopanltcl_bgd.xml`.
- Web retrieval rejected XLS and XML MIME types; direct XML download also failed. No bytes/hash/headers/SDMX keys/observations/revision attributes captured. Official SDMX route discovery PASS; actual file capture and dual-leg validation NOT_DONE. Do not infer that the SDMX file contains the required two legs or historical vintage metadata.
- BGD remains BLOCKED / NOT PASS; aggregate NOT_AUTHORIZED. Detail report updated: docs/GCR_BANGLADESH_BGD_Q2_2026_BANGLADESH_BANK_IMF_PORTFOLIO_SOURCE_GATE_20261120.md.


## 2026-11-20 — BGD historical national portfolio component/sign crosswalk
- Inspected official Bangladesh Bank `Balance of Payments & International Investment Position of Bangladesh — Annual 2024–25` PDF. Table 11 (million BDT) exposes quarterly portfolio investment net, assets and liabilities separately for FY25 Q1–Q4. FY25 Q4: net +3,996; assets 0; liabilities -3,996; identity net = assets − liabilities. FY25 full-year net +16,765; assets 0; liabilities -16,765.
- Bangladesh Bank methodology explains credit/debit treatment: credit records decrease in foreign financial asset holdings or increase in foreign financial liabilities; debit records increase in foreign financial assets or decrease in foreign financial liabilities. Historical directional rows support the Bangladesh asset/liability sign crosswalk and accounting identity, but are not Q2 2026 observations.
- Historical FY25 component/sign crosswalk PASS. FY26 Q4 separate national asset/liability values and same-vintage bridge remain NOT_AVAILABLE / NOT_ESTABLISHED; BGD full validation BLOCKED / NOT PASS; aggregate NOT_AUTHORIZED. Do not carry FY25 zero asset value into FY26.
- Detail: docs/GCR_BANGLADESH_BGD_Q2_2026_BANGLADESH_BANK_IMF_PORTFOLIO_SOURCE_GATE_20261120.md.


## 2026-11-20 — BGD FY26 Q4 national net-only recheck; sign-identity exception
- Official Bangladesh Bank Quarterly Apr–Jun 2026 Vol XXIII No.4 Table V.1 reports portfolio net FY26 Q4 -109 USDm, with FY26 Q1/Q2/Q3 values -45/-59/-10 and FY26 annual -223; FY26 entries provisional. Calendar 2026-Q2 maps to FY26 Q4.
- Reused IMF exact-key receipt: A_NFA_T=0 USD; L_NIL_T=-113.334678 USDm. Historical FY25 Bangladesh identity was net=assets−liabilities; applying it mechanically to these IMF legs yields +113.334678 USDm, opposite to national -109 USDm (absolute difference 222.334678 USDm). This is a diagnostic exception only, not proof of an IMF error or validated sign flip. Do not back-solve national legs or silently transform signs.
- FY26 national net-only source row PASS; separate legs NOT_AVAILABLE; cross-source net identity REVIEW / FAIL_DIAGNOSTIC; same-vintage NOT_ESTABLISHED; BGD dual-leg BLOCKED / NOT PASS; aggregate NOT_AUTHORIZED.
- Detail: docs/GCR_BANGLADESH_BGD_Q2_2026_BANGLADESH_BANK_IMF_PORTFOLIO_SOURCE_GATE_20261120.md.


## 2026-11-20 — BGD primary quarterly PDF reinspection and publication date
- Re-inspected official Bangladesh Bank Quarterly Apr–Jun 2026 Vol XXIII No.4, Table V.1 (PDF p.74): unit USDm; portfolio row FY25 -138, FY26P -223, FY26 Q1 -45, Q2 -59, Q3 -10, Q4 -109. Calendar 2026-Q2 maps to FY26 Q4 = -109 USDm; FY26 annual provisional = -223 USDm. P=Provisional; R=Revised. Official recent-publications index dates this edition 2026-11-15.
- Table V.1 reports portfolio investment only as a net row; no separate portfolio asset/liability legs. Its separate DMB/NBDC and reserve asset/liability rows are different categories and cannot substitute for portfolio legs.
- Prior IMF-derived +113.334678 USDm is only a conditional diagnostic under a historical FY25 identity, not a proven FY26 sign mapping. Preserve REVIEW / FAIL_DIAGNOSTIC; no inferred sign flip.
- BGD national net-only PASS; national portfolio legs NOT_AVAILABLE; same-vintage NOT_ESTABLISHED; dual-leg BLOCKED / NOT PASS; aggregate NOT_AUTHORIZED. Detail: docs/GCR_BANGLADESH_BGD_Q2_2026_BANGLADESH_BANK_IMF_PORTFOLIO_SOURCE_GATE_20261120.md.


## 2026-11-20 — BGD portfolio survey source-scope audit
- Official Bangladesh Bank Survey Forms page defines PI asset side as resident-owned non-resident securities and liability side as resident-issued securities owned by non-residents; survey reports on calendar-year basis. Official July–December 2025 PI chapter says annual series 2010–2025; PI-1 returns from AD banks within 15 days following reference month, and coverage includes inflows/outflows/purchase/sale/stock. Published outputs are annual stock/transaction summaries, not a FY26 Q4 quarterly BPM6 dual-leg flow table.
- Therefore survey definitions PASS for conceptual mapping only; published survey series excluded as a source for FY26 Q2 national flow legs. Do not use Dec-2025 stocks, NITA flows or calendar-2025 totals as quarterly asset/liability flows.
- Official annual BOP page confirms FY26P net PI -223 USDm but not separate PI legs; DMB/NBDC assets/liabilities are a distinct category. BGD Q2 national legs NOT_AVAILABLE; same-vintage NOT_ESTABLISHED; dual-leg BLOCKED / NOT PASS; aggregate NOT_AUTHORIZED.
- Detail: docs/GCR_BANGLADESH_BGD_Q2_2026_BANGLADESH_BANK_IMF_PORTFOLIO_SOURCE_GATE_20261120.md.


## 2026-11-20 — BGD Open Data / monthly BOP alternate-route boundary
- Bangladesh Bank Open Data page describes a free monthly-updated Excel workbook with detailed BOP indicators and a 1972 historical workbook; both official XLSX URLs are inaccessible through current supported byte-preserving retrieval (reader rejects XLSX MIME; direct container download of statisticaltable.xlsx failed). No raw bytes/hash claimed.
- Official monthly BOP table displays portfolio investment as net only for current FY periods; DMB/NBDC and reserve assets/liabilities are separate functional categories, not portfolio legs. Official IIP time series is stock/position data, not transaction flows. Excluded all as substitutes for FY26 Q4 portfolio legs.
- Open Data route discovery PASS; workbook byte capture NOT_DONE; monthly BOP scope confirms PI net-only; BGD national dual legs NOT_AVAILABLE; same-vintage NOT_ESTABLISHED; dual-leg BLOCKED / NOT PASS; aggregate NOT_AUTHORIZED. Detail: docs/GCR_BANGLADESH_BGD_Q2_2026_BANGLADESH_BANK_IMF_PORTFOLIO_SOURCE_GATE_20261120.md.


## 2026-11-20 — Malaysia MYS Q2-2026 national portfolio source crosswalk
- Selected MYS from the fixed 63-country Q2-2026 dual-leg cohort after preflight; both IMF entries are present through 2026-Q2 (46/47 quarters each). No cohort rebuild or new IMF query.
- Official BNM Quarterly Bulletin 3Q 2026 Annex Table 3 (BPM6, RMbn; Q2 marked preliminary) separately reports portfolio net -35.2, assets -33.3 and liabilities -1.8. Source notes: negative assets denote outflows from resident acquisition of assets abroad; positive liabilities denote inflows from incurrence of foreign liabilities. Q2 2026 DOSM release on 14-Aug independently confirms net outflow -35.2; Q3 bulletin dated 18-Nov is later vintage exposing component rows.
- Rounded component arithmetic: -33.3 + -1.8 = -35.1 vs net -35.2; 0.1 RMbn difference is consistent with one-decimal rounding, and source explicitly notes figures may not add due rounding. No forced identity.
- National source component extraction and sign-note capture PASS. Exact MYS IMF numeric rows were not extracted from the large archived CSV (GitHub text fetch returned empty); no new IMF query or synthetic value. RM/USD conversion and IMF row-level sign/scale/vintage reconciliation NOT_DONE. MYS full validation PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Detail: docs/GCR_MALAYSIA_MYS_Q2_2026_BNM_IMF_PORTFOLIO_SOURCE_CROSSWALK_20261120.md.


## 2026-11-20 — Research continuation 42, Part 7: Malaysia MYS Q2-2026 official BNM FX and dual-leg validation
- Preflight: reopened this current ledger (pre-task blob SHA `86f6b5bda9ff6ab2bc91e30cf16677543dd2eecc`), GCR priority queue, MYS national crosswalk, exact IMF row extraction, IMF SCALE semantics and cross-country empirical validation. Completed IMF requests, cohort construction, BNM national row extraction, BSE/NSE TRI rights gates and prior CDSL/NSDL captures were not repeated.
- Added a research-only Python capture/QA script `scripts/research/capture_mys_q2_bnm_fx.py` and 5-minute GitHub Actions workflow `.github/workflows/gcr_mys_q2_bnm_fx_capture.yml`. Guarded `.github/workflows/nse_collector.yml` paths-ignore first; no accidental full NSE collector run.
- GitHub commits: NSE collector guard `2f62ec6ed1d66d65ba4d16cf6b739c54766a6d11`; capture script `9e43c42130a4adc8518841280644de77f35970e8`; workflow `fe6244ba676c23ee516e81fccae3e12f9bc90201`.
- GitHub Actions run 44688788754 SUCCESS; job 136129345981. Artifact 14607900969, 1,261,845 bytes, ZIP SHA-256 `aeeb723a0b8a6e8b8bf1472b1ba7c720074c2e4d5cf604e30ba1d2e162e8c07b`, 90-day retention (expiry 2027-02-18).
- Official BNM daily 1200 raw CSV: 3,870,195 bytes, SHA-256 `4b0c6cf00752753bbb070791468c7a50d39d8b8556129b5399cce94a264101be`; monthly raw CSV: 347,365 bytes, SHA-256 `705f81be36b180d8ac4d29ef13df741a97e996ce373567a03188924b980ec71c`; both HTTP 200. Retrieved UTC 2026-11-20T06:34:49.542146Z.
- 60 unique daily `rate_type=middle` observations (Apr 22, May 19, Jun 19) and 3 monthly `indicator=avg` rows. Monthly vs daily means: 3/3 PASS. Q2 daily mean 4.001691666666666666666666667 MYR/USD; daily-count-weighted monthly mean 4.001706666666666666666666667; difference 0.000015.
- Q2 filtered daily subset committed to `docs/evidence/gcr_mys_q2_2026_bnm_fx/mys_q2_2026_daily_1200_middle_usd.csv` (SHA-256 `836fa4241d257dacd9477cd4cac5dd904872190657279bc96132dd59385c48bb`); monthly subset `mys_q2_2026_monthly_avg_usd.csv` (SHA-256 `de9025e701389adcae917065cce1f273f2f6d3d7f9daeb33b73bf3327ba6974b`).
- Using the empirically supported derived comparison `OBS_VALUE/10^6` (raw IMF OBS_VALUE/UNIT/SCALE untouched), asset comparison after the source-specific sign reversal: BNM +8,321.480707 USDm vs IMF +8,328.720913; residual 7.240206 USDm. Liability comparison with sign retained: BNM -449.809768 USDm vs IMF -453.604930; residual 3.795162 USDm. BNM display half-unit rounding bound ±12.494716 USDm; both separate legs PASS at published precision. No netting.
- BNM rounded component arithmetic remains REVIEW (-33.3 -1.8 = -35.1 vs published -35.2 RMbn); source permits rounding. Exact same-vintage BNM preliminary vs IMF panel revision cut-off remains NOT_ESTABLISHED; therefore MYS full national validation PARTIAL / NOT PASS and EMDE aggregate NOT_AUTHORIZED.
- The earlier page-derived 60-row candidate (mean 3.9992166667) is NOT_ADMITTED / SUPERSEDED; exact session/rate type was unproven and it failed cross-check against the official 1200-middle series. Never use it as final FX input.
- Detailed report: `docs/GCR_MALAYSIA_MYS_Q2_2026_BNM_OFFICIAL_FX_AND_DUAL_LEG_RECONCILIATION_20261120.md`, commit `34beb34aeca06c074a90b758655789b7e610e4ae`. Priority queue update commit `d3aa2efdcf36c3394de153004cfb30560d96f376`.
- Next exact action: obtain an explicit official vintage/revision cut-off bridge between BNM's preliminary Q2 national table and the IMF panel. If unavailable, preserve NOT_ESTABLISHED and move to the next eligible cohort member; do not repeat the FX download/cross-check.
- Protected invariants unchanged: Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E, IPO-PLX V2, weights and trade gates. No paid data, synthetic values, fabricated timestamps, forward-fill, imputation, netting, production integration or aggregate authorization. UNKNOWN is never PASS.


## 2026-11-20 — Research continuation 43: MYS vintage gate and THA Q2-2026 numeric dual-leg validation
### Completed / evidence
- Reopened current continuity ledger (pre-task blob SHA `396152cfd62e2c7888e4f40947b019cca7e875b8`), current GCR priority queue (pre-task blob SHA `9c49ce9064f207ce18de6a0e8c80ba8b11e126d9`), fixed 63-country cohort (blob SHA `1f767e22095865c8e5f87c2cfca55d9104b91e3e`), MYS crosswalk/exact IMF rows and BNM FX/dual-leg report. Completed MYS FX capture, 60-row monthly/daily reconciliation and exact IMF extraction were not repeated.
- MYS vintage audit: DOSM Q2 release 14-Aug-2026 gives net portfolio outflow only; BNM Q3 Bulletin issued 18-Nov-2026 shows Q2 components -33.3/-1.8 RMbn marked preliminary; OpenDOSM dashboard updated 18-Nov 13:00 shows Q2 net -RM35,155m only. IMF public BOP landing page does not expose MYS Q2 observation-level source submission/revision timestamp. The separate IMF country metadata dashboard's 18-Nov publication date is not the BOP observation vintage; IMF panel retrieval 19-Nov is acquisition time only.
- MYS official chronology PASS; observation-level IMF vintage NOT_AVAILABLE; same-vintage bridge NOT_ESTABLISHED. MYS dual numeric legs remain 2/2 PASS at BNM published rounding; full MYS validation PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED. Detail: `docs/GCR_MALAYSIA_MYS_Q2_2026_PUBLICATION_VINTAGE_GATE_20261120.md`, commit `6c2d6d65c426b3ac3d3d9c9e4bf9e88375324460`.
- Selected THA next from existing 63-country Q2-2026 cohort because BOT exposes a direct USD-million quarterly dual-leg table with a last-updated field. No cohort rebuild and no new IMF GET.
- Official BOT EC_XT_049_S2 report 1022, Q2/2026 preliminary, last updated 30-Sep-2026 14:33, USD million. Official note: positive means increase in net financial assets/liabilities; negative means decrease; financial-account net is assets minus liabilities. Q2 portfolio assets +4,679.07, liabilities -238.36, portfolio total +4,917.43 USDm; exact displayed identity 4,679.07 - (-238.36)=4,917.43.
- Reused archived IMF panel (SHA-256 `e8a44abbc8455fef44cc1e4677018ae4b9634d1c04f65bf6fc6dad133cfce62a`) and extracted THA Q2 raw values without new IMF request: A_NFA_T +4,679,073,421.50334 USD; L_NIL_T -238,358,188.710181 USD; UNIT=USD, SCALE=6, PRECISION=6, DERIVATION_TYPE=O. Raw values unchanged.
- Derived USDm comparison residuals: asset +0.00342150334; liability +0.001811289819; both within ±0.005 USDm BOT two-decimal display tolerance. Numeric leg comparison 2/2 PASS; no sign flip, raw overwrite, FX conversion or netting.
- BOT raw page receipt: HTTP 200, 551,847 bytes, SHA-256 `b4a42305fe18668c91e1feadd70ada0537f6e2f8c5b13ef59dd1fdcbd4d00f80`, retrieved 2026-11-20T06:41:16.952209Z.
- Script `scripts/research/reconcile_tha_q2_2026_bot_imf.py` commit `6a618eb337a6782cb3b87c28a87efcafd958938f`; workflow `.github/workflows/gcr_tha_q2_2026_bot_imf.yml` commit `768221a7a53842ebc712df57030c19d7bca4b5c9`; NSE paths-ignore guard commit `b983bf461ab852d295b1eea0d17553c322d53953`.
- GitHub Actions run `44689541630` SUCCESS; job `136131786969`; artifact `14607329438`, 39,093 bytes, ZIP SHA-256 `70328900a9e0058385c6ac7efa5384f86d10508a5056f8f16e40c3afd5b24aec`, expiry 2027-02-18.
- Same-vintage remains NOT_ESTABLISHED: BOT current table has Q2 preliminary and 30-Sep update; IMF archived panel was retrieved 19-Nov but its public dataset page has no per-observation submission/revision timestamp. Therefore THA full national validation PARTIAL / NOT PASS; EMDE aggregate NOT_AUTHORIZED.
- Detailed THA report: `docs/GCR_THAILAND_THA_Q2_2026_BOT_IMF_PORTFOLIO_DUAL_LEG_RECONCILIATION_20261120.md`, commit `523016a438a79080ed1c08c033f11f7972ba4994`. Updated master priority queue commit `7f15fa179b5543c0b83899ebf0d65ef2b7530bb6`.
### Rejected / not authorized
- MYS same-vintage status is not inferred from release dates or retrieval timestamps.
- THA same-vintage status is not inferred from BOT update date vs IMF panel retrieval date.
- No cohort rebuild, no repeated IMF GET, no repeated MYS FX acquisition, no universal scale/sign claim, no country aggregation, no production changes.
### Exact next action
- Seek a public BOT revision-history/archived Q2 snapshot and IMF observation-level source vintage for THA. If unavailable, preserve NOT_ESTABLISHED and advance to the next eligible member of the fixed 63-country cohort after preflight. Do not repeat the same BOT table capture.
### Protected invariants
Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E, IPO-PLX V2, weights and trade gates unchanged. No paid data, synthetic values, fabricated timestamps, imputation, forward-fill, FX conversion, netting or aggregate authorization. UNKNOWN is never PASS.


### Operational guard correction — accidental NSE run containment (2026-11-20)
- The THA research script commit was pushed just before its new path was added to `.github/workflows/nse_collector.yml` paths-ignore, so an unintended full collector run `44689517549` started. This was not a research or production change.
- Immediately added the THA script/workflow paths to NSE paths-ignore (guard commit `b983bf461ab852d295b1eea0d17553c322d53953`), then used the existing cancellation workflow.
- Cancellation workflow updated to include run `44689517549` (commit `02fb5dbf3906f295fb41dcb27e123d2fc7016939`); trigger file updated (commit `ebd7951224eecb6d927b13a8c4c8225fd38a9b03`).
- Cancellation workflow run `44689721808` completed successfully; its log confirms “Request to cancel workflow 44689517549 submitted”; target NSE run final status **completed / cancelled** at 2026-11-20T06:43:06Z.
- No claim is made that the full collector completed; its in-progress market-session acquisition was stopped. No production output from that accidental run is admitted as evidence.
- Guard is now in place for the THA script and workflow paths. Future research-only commits must be added to paths-ignore before their first push; research workflows remain bounded to 5 minutes.


## 2026-11-20 — Research continuation 44: Philippines PHL Q2-2026 BSP/IMF dual-leg numeric cross-check
### Completed / evidence
- Preflight reopened the current continuity ledger, GCR priority queue and THA report; preserved the fixed 63-country Q2-2026 cohort and reused the existing IMF normalized panel. No cohort rebuild, no new IMF query, no MYS/THA work repeated.
- Selected PHL from the fixed cohort. Existing IMF Q2 raw rows: A_NFA_T +1,330,642,951.05526 USD and L_NIL_T +1,798,282,616.26536 USD; both UNIT=USD, SCALE=6, PRECISION=6, DERIVATION_TYPE=O. Panel SHA-256 e8a44abbc8455fef44cc1e4677018ae4b9634d1c04f65bf6fc6dad133cfce62a.
- Official BSP dedicated Table 1.7 and 11-Sep-2026 Q2 BOP release show portfolio net -468 USDm, assets +1,331 USDm and liabilities +1,798 USDm. Separate numeric comparison residuals (IMF-derived USDm minus BSP) are -0.35704894474 and +0.28261626536 USDm, both within ±0.5 USDm whole-million display rounding. Numeric dual legs 2/2 PASS at published precision.
- Rounded identity 1,331 - 1,798 = -467 vs -468; 1 USDm difference is within combined display rounding. No forced identity, no netting, no FX or sign transformation.
- Same-vintage NOT_ESTABLISHED: BSP release 11-Sep-2026/current Q2 preliminary; IMF panel retrieval 19-Nov-2026 is acquisition time only, no observation-specific IMF submission/revision timestamp. PHL full validation PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Detailed report created: docs/GCR_PHILIPPINES_PHL_Q2_2026_BSP_IMF_PORTFOLIO_DUAL_LEG_RECONCILIATION_20261120.md, commit 10b25708ac9df0ad7010a952c84941b6ef1b21a9. Priority queue update commit 66cbe880ecba2772ad914b9267de4843671b59c2.
### Rejected / blockers
- First generic Table 1 script parse selected similarly named Other Investment rows; erroneous values explicitly NOT_ADMITTED. Run 44690030449 failed closed.
- Run 44690124941 captured Table 1 raw page and release but parsed wrong category; artifact 14607583953 SHA-256 b8b92e22f272cc19aeab4cc0549ec7046d5f6189fb3f91d0dc40084a92f96938 is diagnostic only.
- Dedicated Table 1.7 script run 44690374864 failed closed because Python HTMLParser did not parse BSP Excel-HTML sparse-cell rows (including ss:Index). No successful structured raw+parsed artifact claimed. Official web-published Table 1.7/release text supports the values; automated capture acceptance remains NOT_PASS.
- Same-vintage bridge not inferred from publication/retrieval dates. No aggregate admission.
### Operational containment / lesson
- Accidental NSE collector runs 44690020188, 44690030398, 44690124814 and 44690374904 were cancelled; their outputs are excluded from evidence. This is an operational defect to prevent recurrence.
- Before research-only pushes, ensure the collector paths-ignore contains every touched path, including cancellation trigger files. Cancellation workflow itself can otherwise cause another collector run if its trigger file is not ignored.
### Exact next action
Repair the BSP Table 1.7 Excel-HTML parser with sparse-cell index handling; verify extracted Q2 column against the dated BSP release; produce a successful raw+parsed evidence artifact. Then seek PHL observation-level IMF vintage evidence. Do not re-fetch IMF, rebuild cohort, or alter production.
### Protected invariants
Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E, IPO-PLX V2, weights and trade gates unchanged. UNKNOWN is never PASS. No paid data, synthetic values, fabricated timestamps, forward-fill, imputation, netting, production integration or aggregate authorization.


## 2026-11-20 — Research continuation 45: PHL parser repair and evidence artifact PASS
### Completed tasks
- Reopened prior raw artifact 14608426572 and inspected BSP Table 1.7 Excel-HTML. Root cause one-cell merged section headings before 20-cell data rows. Corrected parser to skip merged headings and validate Q2 header plus 2026p subheader before extraction.
- Corrected release parser: identical component labels occur in other functional-account sections. Extraction now anchors on Portfolio Investment and reads only its immediate asset/liability rows. Release parity is enforced; no later Other Investment row can overwrite Portfolio Investment values.
- Corrected preliminary flag from verified header cell rather than fragile regex.
- Run 44705225122 SUCCESS; job 136183035008; artifact 14614766459 (15,415 bytes), ZIP SHA-256 7e0d57f7d50f6f0a6622183d81f2bb8bbe04ee297f489f20dd982465d3b46b5c, expiry 2027-02-18. Artifact independently downloaded and inspected.
- Raw Table 1.7: 156,110 bytes, SHA-256 b267ceab83794b86cd6c6a3ce703d878c2185091670e0c528b10df1644774569. BSP release HTML: 148,165 bytes, SHA-256 272890a3a383bbef2eebfb274746e3835f2c3e7d3ab084f303f317f6813b5707. CSV: 384 bytes, SHA-256 8bc1a27fc66c40f99ad7d66789884a90c0f1d1cb91b4c64065fdec4e769d2939. summary.json: 3,919 bytes, SHA-256 376894e48319d0a0a2c0d4e8322f4de0fc578fd8b1b70a4f361e425b0f0dd166.
- Official BSP Table 1.7 and dated release agree exactly: Q2 2026 preliminary TRUE; portfolio net -468 USDm; assets +1,331; liabilities +1,798.
- Archived IMF raw values unchanged; derived comparisons: asset +1,330.64295105526 USDm vs BSP +1,331 (residual -0.35704894474); liability +1,798.28261626536 vs BSP +1,798 (residual +0.28261626536). Both within ±0.5 USDm. Numeric 2/2 PASS. Display identity -467 vs -468 differs by 1 USDm; accepted only as combined display rounding, not forced.
### Rejected / blockers
- Prior parser attempts 44690030449, 44690124941, 44690374864 and 44704973071 remain diagnostic/failed. Their incorrect category values are NOT_ADMITTED.
- BSP Q2 preliminary is not evidence of same-vintage with IMF. Current HTTP Last-Modified response is not a revision history. IMF public BOP dataset page offers API/download but no observation-specific source submission/revision timestamp.
- BSP FDI page notes an FDI in-kind transaction revision; this applies to FDI, not portfolio flows, so it is explicitly excluded from PHL portfolio vintage evidence.
- PHL source capture PASS; release parity PASS; numeric dual legs 2/2 PASS; same-vintage NOT_ESTABLISHED; national acceptance PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
### Operational lessons
- Missing paths-ignore for PHL script/workflow caused accidental full collector runs 44704973029 and 44704985742. Added explicit paths-ignore entries for PHL research paths and cancellation paths in commit fbaa2617f8e996b996f299652194974141cd0921. Both accidental runs were confirmed cancelled; outputs excluded.
- Never push a research-only script/workflow until the exact script, workflow and any trigger-file paths have been verified in the current nse_collector.yml paths-ignore list.
### Exact next action
Run a bounded official-source vintage search for BSP portfolio revision archive and IMF observation-level vintage metadata. If no public series-specific revision history or observation-level IMF vintage field exists, close the gate as NOT_ESTABLISHED and advance to the next eligible country after preflight. Do not repeat parser work, re-fetch IMF, or rebuild cohort.
### Protected invariants
Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E, IPO-PLX V2, weights and trade gates unchanged. UNKNOWN is never PASS. No synthetic data, fabricated timestamps, paid data, forward-fill, imputation, forced netting, production integration or aggregate authorization.


## 2026-11-20 — Continuation 45 addendum: PHL vintage-policy search
- BSP official Revision Policies page confirms all BOP/IIP components released during the reference quarter are preliminary and may be revised in any quarter of the reference year; prior-year revisions may accompany Q2 September and Q4 March releases.
- BSP September-2025 technical note for 2024 BPM6 BOP series documents portfolio-specific revisions to both asset and liability components (including CPIS and BSP reporting-data updates). This is historical precedent only, not proof PHL Q2-2026 was revised.
- BSP FDI in-kind revision notice explicitly excluded from portfolio gate.
- IMF public BOP dataset/API page and BOP/IIP metadata dashboard (18-Nov-2026) expose no PHL Q2 observation-level source submission/revision timestamp; metadata dashboard date is not source observation vintage.
- Bounded official-source search found no public PHL Q2-2026 portfolio revision chain or IMF observation-level vintage field. Gate closed NOT_ESTABLISHED, not PASS. PHL numeric dual legs 2/2 PASS; raw/parsed capture PASS; national acceptance PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Sources archived in PHL report; official pages: BSP revision policy https://www.bsp.gov.ph/SitePages/Statistics/External.aspx?TabId=2 ; BSP historical revision note https://www.bsp.gov.ph/Media_And_Research/Balance%20of%20Payments%20Report/2025/BOP_2qtr2025.pdf ; IMF BOP dataset https://data.imf.org/en/datasets/IMF.STA%3ABOP?sc_site=idata ; IMF BOP/IIP metadata dashboard https://data.imf.org/en/dashboards/bop%20metadata%20dashboard .
- Exact next: preflight existing 63-country cohort and priority queue; choose next eligible country. Do not rebuild cohort, repeat generic vintage searches, re-run PHL parser, or re-query IMF absent an actual revision/source release.


## AK. GCR Colombia COL Q2-2026 — national-source boundary gate (2026-11-20)
- Reused fixed 63-country Q2 dual-leg cohort; no cohort rebuild or IMF re-query. Existing coverage matrix shows COL A_NFA_T and L_NIL_T each have 46 observations through 2026-Q2. Repository preflight found no prior COL national-source report.
- Official BanRep Q2 report (published 1-Sep-2026) gives financial-account aggregate USD3,719m, including external-asset liquidation USD6,149m, derivative gains USD804m, external-liability decreases USD2,683m and reserve transactions USD550m. It mentions net liquidation of portfolio instruments as a partial offset but does not provide separate Q2 portfolio transaction legs in inspected report/PDF.
- BanRep SDDS page last updated 13-Nov-2026 gives Q2 portfolio IIP stocks: assets USD125,046.1m and liabilities USD118,800.9m. These are stocks, not BOP flows, and are NOT_ADMITTED. General BPM6 sign note is insufficient to map portfolio-flow signs.
- BanRep stats portal series route timed out; no raw export or portfolio transaction rows captured. COL national flow legs NOT_EXTRACTED; numeric comparison NOT_DONE; sign mapping and same-vintage NOT_ESTABLISHED; national validation BLOCKED/PARTIAL, not PASS; aggregate NOT_AUTHORIZED.
- Detail report: docs/GCR_COLOMBIA_COL_Q2_2026_BANREP_OFFICIAL_SOURCE_BOUNDARY_AUDIT_20261120.md. Next action: identify the official BanRep public export/series metadata for separate portfolio transaction asset/liability legs, including units, signs and revision metadata; otherwise preserve blocker and advance.
- No paid sources, invented values/timestamps, stock-flow substitution, inferred sign flip, netting, synthetic data or production changes. All V11.3 protected invariants unchanged; UNKNOWN is never PASS.


## AL. GCR Colombia COL — official portfolio series catalogue discovery (2026-11-20)
- BanRep BOP datawarehouse page confirms quarterly BPM6 BOP series from 2000 onward and a dedicated Portfolio Investment annex. SUAMECA multiple-download catalogue lists distinct quarterly series for portfolio total, portfolio net acquisition of financial assets, and portfolio net incurrence of liabilities; component series are in current USD millions, cover 2000-Q1 through 2026-Q2, and show last update 2026-09-01.
- This identifies the exact national component series needed for comparison conceptually, but SUAMECA page access timed out. No series IDs, raw export, Q2 values, series-level sign metadata, receipt or SHA-256 obtained. General BanRep financial-account sign statement is not enough for component-level mapping.
- COL raw national flow values NOT_EXTRACTED; numeric comparison NOT_DONE; sign mapping and same-vintage NOT_ESTABLISHED; national acceptance BLOCKED/PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED. IIP stocks and account-level aggregates remain excluded.
- Detail report: docs/GCR_COLOMBIA_COL_Q2_2026_BANREP_OFFICIAL_SOURCE_BOUNDARY_AUDIT_20261120.md, update commit 40722e580d98c49ac57328f7d8974115529b4e51.
- Next exact action: obtain the two component series IDs and raw Q2 export via supported SUAMECA browser route; preserve bytes, receipt, SHA-256 and series sign/vintage metadata. No IMF re-query, no cohort rebuild, no production changes. UNKNOWN is never PASS.


## 2026-11-20 — Continuation 48: Colombia SDMX route boundary
- Reopened current continuity ledger (pre-update blob 99b4a343614637422e5780827083847c0c0688d1), GCR priority queue, fixed 63-country cohort and COL detail report before continuing. The current country task was COL SUAMECA raw export access.
- Inspected BanRep official SDMX guide v4.0 (Oct-2026). It documents public REST queries and XML/JSON/CSV formats, but its supported flow inventory lists IBR, DTF, TRM, TPM, TIB, COLCAP, monetary aggregates, UVR and TES—not BOP/portfolio investment. The documented SDMX API is therefore NOT_APPLICABLE as a proven BOP export route; no guessed flow ID or unsupported request was made.
- Official SUAMECA catalogue confirms two separate portfolio transaction component series in current USD millions, quarterly through 2026-Q2, published 2026-09-01; exact series IDs/raw bytes/Q2 values/sign-vintage metadata still unavailable. COL raw capture NOT_DONE, numeric validation NOT_DONE, sign mapping and same-vintage NOT_ESTABLISHED; COL PARTIAL/BLOCKED / NOT PASS; aggregate NOT_AUTHORIZED.
- Official sources: https://suameca.banrep.gov.co/archivos/webservices/sdmx_v_3_1/GUIA_CONSUMO_SDMX_V_3_1.pdf ; https://suameca.banrep.gov.co/descarga-multiple-de-datos/ .
- Next: advance Rank-1 validation to the next not-yet-audited member of the existing 63-country cohort after preflight. Do not rebuild cohort, re-query IMF, use IIP stocks, or infer values/signs. Protected production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, engines A–E and IPO-PLX V2 unchanged.


## 2026-11-20 — Continuation 49: Peru BCRP portfolio series source-boundary audit
- Reopened master ledger (pre-update blob 971d93c897c684991b242d2037a80bf49ab084e6), GCR priority queue (pre-update blob 17bbd3f11a9258292f2f90a36e30ff1d385090ba) and fixed 63-country Q2 cohort. COL remains blocked; PER selected as next un-audited cohort member after repository search returned no prior PER national portfolio-flow report.
- Official BCRPData catalogue identifies private-sector portfolio asset series PN39278BQ, private-sector portfolio liability series PN39285BQ, and public-sector portfolio liability series PN39404FQ; all quarterly through Q2-2026 and last updated 2026-08-20. The listed asset series is explicitly private-sector scoped; full-economy asset coverage/public-sector treatment is not established.
- Official BCRP API guide documents GET/POST and CSV/JSON/XML/XLS outputs. A bounded Q2-2026 API retrieval attempt using the documented URL pattern did not return content in the web reader; no raw bytes, Q2 values, receipt or hash claimed.
- PER numeric validation NOT_DONE; sign mapping and same-vintage NOT_ESTABLISHED; full national scope NOT_ESTABLISHED; PARTIAL/BLOCKED / NOT PASS; aggregate NOT_AUTHORIZED. Detail report: docs/GCR_PERU_PER_Q2_2026_BCRP_PORTFOLIO_SERIES_SOURCE_BOUNDARY_AUDIT_20261120.md (commit 55d03cc785edf7ce853366a41565708b0dec6a91).
- Official sources: https://estadisticas.bcrp.gob.pe/estadisticas/series/trimestrales ; https://estadisticas.bcrp.gob.pe/estadisticas/series/documentos/bcrpdataapi.pdf ; https://www.bcrp.gob.pe/docs/Publicaciones/Nota-Estudios/2026/nota-de-estudios-59-2026.pdf .
- Next: use supported raw-byte route for BCRP API and establish complete national portfolio scope/sign/vintage before comparison. No IMF re-query, cohort rebuild, IIP stock substitution, netting or production changes. Protected invariants unchanged; UNKNOWN is never PASS.


## 2026-11-20 — Continuation 50: PAK Q2-2026 official source-boundary audit
- Detail report: docs/GCR_PAKISTAN_PAK_Q2_2026_SBP_PORTFOLIO_SOURCE_BOUNDARY_AUDIT_20261120.md.
- PAK was selected only after fixed-cohort and repository preflight; no prior dedicated PAK Q2-2026 national portfolio-flow report was found. No IMF re-query or cohort rebuild.
- SBP catalogue confirms quarterly BPM6 BOP dataset through Jun-2026 and separately half-yearly Core Set of Portfolio Investment Assets data. EasyData listing reports BPM6 quarterly coverage Sep-2002 to Jun-2026, last release 18-Aug-2026.
- Inspected SBP September-2026 BPM6 PDF: FY26 Jul-Jun cumulative and Sep monthly columns plus Jul-Sep periods; portfolio assets abroad and liabilities in Pakistan are shown as categories, but no Apr-Jun 2026 Q2-specific rows/column. Do not derive Q2 by mixing cumulative/fiscal periods.
- Core Set of Portfolio Investment Assets is an End-June-2025 PKR position snapshot, not transaction flows and not a matching liability leg; explicitly NOT_APPLICABLE to A_NFA_T/L_NIL_T flow validation.
- Separate SBP archive quarterly calendar-year BOP Excel is listed, but raw workbook/metadata/observations were not acquired. Calendar-vs-fiscal period alignment remains NOT_ESTABLISHED.
- PAK gates: official quarterly dataset discovery PASS only; Q2 asset/liability values NOT_EXTRACTED; sign mapping and same-vintage NOT_ESTABLISHED; numeric validation NOT_DONE; national validation PARTIAL/BLOCKED / NOT PASS; aggregate NOT_AUTHORIZED.
- Official sources: https://www.sbp.org.pk/economic-data ; https://easydata.sbp.org.pk/apex/f?p=10:210:8439371819372: ; https://www.sbp.org.pk/assets/document/Balancepayment_BPM6.pdf ; https://www.sbp.org.pk/ecodata/CPIS-Sdds-Assets-Data.pdf ; https://archive.sbp.org.pk/ecodata/index2.asp .
- No changes to protected invariants, production selector, ranking, pressure fade, CORE-672, engines A-E or IPO-PLX V2. No synthetic data, stock-flow substitution, inferred sign/vintage, netting or aggregate admission.


## 2026-11-20 — Continuation 51: PAK official Q2-2026 portfolio component values extracted
- Reopened master ledger, queue, fixed cohort and PAK report before continuing. Found a distinct official SBP quarterly calendar-year BPM6 PDF: https://www.sbp.org.pk/assets/document/BPM6_c.pdf . Its two-row header identifies the Q2 CY26 column as revised (R), units USD million.
- Extracted Q2 CY26(R): Portfolio investment abroad -2 USDm; Portfolio investment in Pakistan -243 USDm. Both are separate portfolio components. This is source-value extraction PASS and corrects Continuation 50's values NOT_EXTRACTED status. The previous September BPM6 table was not the right source for this calendar-quarter view.
- Do not assume sign equivalence to IMF A_NFA_T/L_NIL_T from the row labels alone. Official sign/definition crosswalk NOT_ESTABLISHED; exact IMF PAK Q2 rows not independently retrieved from the existing archive in this step; same-vintage/revision timestamp NOT_ESTABLISHED; numeric dual-leg comparison NOT_DONE; national validation PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- No raw PDF bytes/hash captured. No IMF re-query, no cohort rebuild, no netting, no production change. Protected invariants unchanged.
- Updated report: docs/GCR_PAKISTAN_PAK_Q2_2026_SBP_PORTFOLIO_SOURCE_BOUNDARY_AUDIT_20261120.md. Next: retrieve archived IMF PAK Q2 exact A_NFA_T/L_NIL_T rows, inspect official sign definitions, compare legs separately at SBP USDm display precision, then investigate revision timestamp.


## Continuation 52 — PAK Q2-2026 exact IMF dual-leg reconciliation (2026-11-20)
- Reopened current ledger, GCR queue, fixed 63-country cohort, PAK report, and exact archived IMF raw CSVs. PAK was already in the fixed cohort; no cohort rebuild and no IMF re-query.
- Raw IMF Git blob SHAs: asset file 15449e87c9057291a1f52f2f8cd9805df55f9fb8; liability file 15f379dc42e2760eb5f2384618e48f5ddc3177f1.
- Exact PAK 2026-Q2 rows: A_NFA_T = -2,000,000 USD (scale 6); L_NIL_T = -243,000,000 USD (scale 6). Both ACTION=R, quarterly, USD, Q2-2026.
- Official SBP BPM6 sources establish financial-account sign convention: increases in assets/liabilities positive, decreases negative; financial account uses NAFA and NIL separately. SBP CY26 Q2(R) values are Portfolio investment abroad -2 USDm and Portfolio investment in Pakistan -243 USDm. Separate leg comparisons each match exactly at published USDm precision (2/2 PASS; differences 0). No netting.
- PAK: official sign/framework crosswalk SUPPORTED; dual-leg numeric comparison PASS; exact same-vintage NOT_ESTABLISHED despite both records carrying revised metadata; national validation PARTIAL, not PASS; aggregate NOT_AUTHORIZED.
- No SBP raw PDF SHA-256 claimed; IMF raw archive Git blob SHAs recorded above. No synthetic values, no production change, no cohort rebuild, no new IMF query.
- Detailed evidence: docs/GCR_PAKISTAN_PAK_Q2_2026_SBP_PORTFOLIO_SOURCE_BOUNDARY_AUDIT_20261120.md. GCR priority queue updated in docs/GCR_MASTER_PRIORITY_QUEUE_AND_ZAF_Q2_2026_SOURCE_MAPPING_20261120.md.
- Next exact action: inspect official SBP Data Revision Policy for Q2-2026 portfolio observation-specific revision date/history and compare with IMF vintage metadata. If no public dated history exists, retain UNKNOWN and proceed to the next unvalidated cohort member.


### Continuation 52 — SBP Data Revision Policy check
- Official SBP Data Revision Policy (last updated 11-Sep-2019): https://www.sbp.org.pk/departments/stats/Data-Revision-Policy.pdf . It defines revisions and states that provisional observations are marked P and revised observations R; revisions may reflect better source data, routine recalculation, methodology changes or correction of errors. It says reasons/sources are explained when revised series are released (policy PDF lines 21-29, 53-74, 91-111).
- This supports interpreting SBP's Q2 CY26 (R) label as revised status, but the policy is generic and does not identify the Q2-2026 portfolio rows' specific revision date, prior value, reason, or revision event. Thus it does not close the same-vintage gate. IMF ACTION=R is likewise status-only without matching timestamp evidence.
- Same-vintage remains NOT_ESTABLISHED / UNKNOWN; PAK remains PARTIAL, not PASS; aggregate NOT_AUTHORIZED. Next best action: proceed to next unvalidated fixed-cohort country while retaining this PAK vintage blocker unless a dated observation-specific SBP revision record becomes publicly available.


## Continuation 53 — PER Q2-2026 BCRP source-boundary audit (2026-11-20)
- Re-fetched latest ledger, GCR queue, fixed 63-country cohort and existing IMF raw archive. PER confirmed in cohort; no prior PER dedicated Q2-2026 national portfolio report found. No IMF re-query or cohort rebuild.
- Exact existing IMF rows: PER A_NFA_T 1,999,155,686.69433 USD and L_NIL_T 1,699,664,071.47559 USD, both 2026-Q2, USD quarterly, ACTION=R, SCALE=6, PRECISION=6. Raw archive Git blob SHAs: asset 15449e87c9057291a1f52f2f8cd9805df55f9fb8; liability 15f379dc42e2760eb5f2384618e48f5ddc3177f1.
- BCRP official quarterly indicators PDF inspected, but its latest displayed quarter is 2025-Q4. Candidate official Q2-2026 Note of Studies No. 59 PDF URL yielded only an iframe shell; raw PDF content and national portfolio component values not acquired. Third-party snippets were explicitly excluded.
- PER state: IMF raw row extraction PASS; official BCRP source discovery PASS; Q2 national portfolio asset/liability NOT_EXTRACTED; source bytes/hash NOT_CAPTURED; sign/definition/vintage NOT_ESTABLISHED; numeric comparison NOT_DONE; national validation PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Detailed report: docs/GCR_PERU_PER_Q2_2026_BCRP_IMF_PORTFOLIO_SOURCE_BOUNDARY_AUDIT_20261120.md. GCR queue updated. Next exact action: obtain official BCRP Q2-2026 report via supported official route and inspect the separate portfolio asset/liability transaction table; if inaccessible, retain BLOCKED and move on.
- No synthetic values, no IIP stock substitution, no netting, no FX inference, no production changes. Protected V11.3 invariants unchanged.


## Continuation 54 — PER official BCRPData series recovery (2026-11-20)
- Reused fixed 63-country cohort and existing IMF raw archive; no IMF re-query or cohort rebuild. BCRP official Financial Account quarterly portal identifies private-sector series and separate public-sector series through T2-2026, last updated 20-Aug-2026.
- BCRP Q2-2026 USDm: private portfolio assets PN39278BQ 1,749; private portfolio liabilities PN39285BQ 279; public portfolio liabilities PN39404FQ 1,421. Public source URLs are recorded in the PER report.
- Separate liability comparison: BCRP 279 + 1,421 = 1,700 USDm vs IMF L_NIL_T 1,699.66407147559 USDm; residual +0.33592852441 USDm, within whole-million display precision. Liability numeric PASS, subject to definition/vintage.
- Asset comparison remains incomplete: only private-sector assets 1,749 USDm; public-sector catalogue exposes aggregate assets PN39402FQ but no public-sector portfolio asset subseries in inspected list. Do not use total public assets as proxy. The difference to IMF all-sector A_NFA_T is not like-for-like.
- PER state: official series capture PASS for 3 component series; liability numeric PASS; asset full scope PARTIAL/NOT_DONE; sign/definition and same-vintage NOT_ESTABLISHED; national dual-leg validation PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- BCRP catalogue last update 20-Aug-2026; IMF archived rows ACTION=R but no observation-matched timestamp. No raw API payload or raw file SHA-256 captured. No netting or production changes.
- Detail report: docs/GCR_PERU_PER_Q2_2026_BCRP_IMF_PORTFOLIO_SOURCE_BOUNDARY_AUDIT_20261120.md. GCR queue updated. Next exact action: inspect BCRPData API/developer docs and public-sector asset metadata for a distinct portfolio asset flow series; if absent, retain UNKNOWN and advance.


### Continuation 54 — BCRP API contract check
- Official BCRPData API developer guide: https://estadisticas.bcrp.gob.pe/estadisticas/series/documentos/bcrpdataapi.pdf . It documents GET series queries, up to 10 same-frequency series, output formats including JSON/CSV, and exact series-code/date-range URL structure (guide pp.2-5; updated 24-May-2022).
- Constructed one documented, single-period JSON GET for PN39278BQ-PN39285BQ-PN39404FQ, 2026-2/2026-2/ing. The web retrieval returned an internal access error; no raw API payload/receipt was acquired. Do not claim API download or raw-file hash. Previously inspected official HTML series pages remain the evidence for the three displayed values.
- API path remains an available documented retrieval contract but the exact endpoint access in this session is BLOCKED; do not repeatedly retry the same URL. Continue with HTML display evidence only, and keep the raw-byte archival gate open.


## Continuation 55 — GCR country-source continuation (2026-11-20)
- PER: official BCRPData full quarterly Financial Account catalogue (58 series; public sector 25) checked. Public-sector portfolio-liability components exist; public-sector asset series in catalogue is aggregate only, no portfolio-specific asset subseries. Do not substitute aggregate assets. PER liability comparison 1,700 vs IMF 1,699.664 USDm; +0.336 USDm residual within ±0.5 display rounding. PER remains PARTIAL / NOT PASS due incomplete all-sector asset leg, unestablished sign/definition and same-vintage; aggregate NOT_AUTHORIZED.
- NPL selected as next fixed-cohort country. NRB official external-sector page lists monthly BPM6/BPM5 and yearly BPM6/BPM5 datasets. Official BPM6 XLSX link found but XLSX bytes could not be inspected through current web retrieval (unsupported MIME). Treat source discovery PASS only; data extraction NOT_DONE.
- NPL next action: retrieve exact NRB BPM6 workbook through XLSX-capable path, inspect Apr-Jun 2026 rows, determine separate portfolio asset/liability availability, monthly vs cumulative, units/signs and vintage. Reuse existing IMF raw files only.
- No synthetic data, stock/flow substitution, netting, FX inference, cohort rebuild, IMF re-query, production selector/score/filter/engine changes. UNKNOWN is never PASS.


## Continuation 56 — NPL official source boundary (2026-11-20)
- Reused fixed 63-country cohort and existing IMF archive; no cohort rebuild or IMF re-query. NRB official External Sector page lists monthly BPM6/BPM5 BOP datasets; NSDP lists BOP Browse Data and SDMX, but linked XML is 2024 Q1 and stale.
- NRB Monthly Statistics archive lists relevant 2082-12, 2083-01, 2083-02 monthly XLSX. Official XLSX fetches failed due unsupported MIME/timeout; no bytes/sheets/values/SHA-256 captured. NRB macro report monthly overall BOP is aggregate only; central-bank foreign-securities balance-sheet items are stocks, excluded.
- NPL status: official source discovery PASS; workbook inspection NOT_DONE; separate national portfolio assets/liabilities NOT_EXTRACTED; period basis/sign/units/vintage UNKNOWN; dual-leg comparison NOT_DONE; national validation PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Detail report: docs/GCR_NEPAL_NPL_Q2_2026_NRB_BPM6_PORTFOLIO_SOURCE_BOUNDARY_AUDIT_20261120.md. Next exact action: obtain XLSX via supported XLSX-capable path, inspect portfolio asset/liability flows and monthly-vs-cumulative basis; only then compare with archived IMF rows. No fabricated values, stocks-as-flows, netting, or production changes.


## Continuation 57 — NPL source-family correction (2026-11-20)
- Reopened current NPL audit, GCR queue and continuity ledger. Corrected prior source classification after opening the exact three monthly archive PDFs: Chaitra 2082, Baisakh 2083, Jestha 2083 are Banking & Financial Statistics (Monthly) (Provisional), not BOP. The PDFs contain BFI banking balance sheets/P&L/credit/deposit statistics; full-text searches found no portfolio or BOP section. Withdraw the earlier inference that their XLSX might contain BOP portfolio legs. Exclude these files from BOP evidence.
- Official NRB External Sector BPM6 dataset remains the valid source family; linked BPM6 XLSX fetch is unsupported MIME, so no raw bytes, rows, values or SHA-256 captured. NSDP BOP browse timed out; linked SDMX XML is 2024-Q1 stale and unsupported MIME.
- NPL state: official source discovery PASS; actual BPM6 workbook inspection NOT_DONE; separate Q2-2026 portfolio assets/liabilities NOT_EXTRACTED; period/sign/units/vintage UNKNOWN; dual-leg comparison NOT_DONE; national validation PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Next: locate supported XLSX-capable retrieval for official External Sector BPM6 workbook or NRB official API/export; otherwise retain blocked and advance. No BFR data substitution, stock-as-flow, IMF re-query, cohort rebuild or production changes. UNKNOWN is never PASS.


## India Benchmark Panel — NSE actual raw-capture feasibility gate Part 3 (2026-11-20)
- Reopened current ledger and GCR queue; reused India Benchmark Panel Parts 1–2 and excluded already-PASS official locator/preview-boundary work.
- Official NSE All Reports, Historical Reports directory and NSE Indices Historical Data UI surfaces reconfirmed. The available read-only page retrieval interface does not operate the From/To controls or return the resulting download bytes. No direct official API contract was established; no undocumented endpoint probing.
- Actual NIFTY 50, broad-market companion and India VIX raw payloads remain NOT_CAPTURED. No response headers/MIME/length, raw SHA-256, parsed rows, duplicate/session QA or panel build is claimed. This is an execution-bridge limitation, not evidence of NSE-side denial.
- Detail report: docs/INDIA_NSE_ACTUAL_RAW_CAPTURE_FEASIBILITY_GATE_PART3_20261120.md.
- Next: use supported interactive browser/download capability or obtain exact official NSE downloads as user attachments; hash unchanged bytes before parsing, then validate interval, duplicates, sessions, schema, OHLC and price-index/TRI identity.
- All production invariants and fixed 63-country cohort unchanged; no paid API, synthetic data, inferred timestamps, silent deduplication, forward-fill or production integration. UNKNOWN is never PASS.

## India FPI — NSDL Archive public form contract audit (Continuation 76, 2026-11-20)
- Reopened the current Continuity Ledger and GCR priority queue and reused the existing FPI raw-capture/schema, CDSL sector capture, matched-date reconciliation and sector arithmetic reports.
- Downloaded existing artifact 14524707532 (run 44515445620), 184,876 bytes; independent SHA-256 29530f3d0913f3eed93afbeb0759ecb8131b4192c71e5928d79961df77c24c69 matched the stored GitHub digest.
- Inspected archived NSDL Archive HTML: ASP.NET POST form frmMonthly, action ./Archive.aspx, hidden ViewState/EventValidation fields, disabled initial txtDate, hidden hdnDate, calendar date format %d-%b-%Y, hidden validation/export fields, and public postback targets btnSubmit1 (View Report) / btnExcel (Export to Excel).
- No POST was sent; server-side query semantics, archive response rows, output bytes/hash and date coverage remain UNKNOWN/NOT_DONE. No stale ViewState replay, guessed body, or source-status promotion.
- Detail report: docs/GCR_NSDL_ARCHIVE_PUBLIC_FORM_CONTRACT_AUDIT_CONTINUATION76_20261120.md.
- Next: use supported interactive browser to obtain fresh form state, select one date using the calendar and invoke View Report once; capture raw response provenance and inspect returned rows. If unavailable, preserve NOT_DONE and move to another independent task.
- No production changes; ₹0; no synthetic/interpolated data; no alteration of Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A–E, IPO-PLX V2 or fixed 63-country cohort. UNKNOWN is never PASS.

## India FPI — CDSL Daily 18-Nov-2026 Full-Table Arithmetic QA (Continuation 77, 2026-11-20)
- Re-fetched current ledger and GCR queue; reopened Continuation 76 and prior CDSL sector arithmetic report. Reused existing run 44519322726 / artifact 14527092174; no recapture or repeated sector 192/192 test.
- Independently recomputed ZIP SHA-256 `83048ea0bc712b6a453270f8fb5c3c6755b579857ff2ad9eb7d53c8ba1778fbd` matching artifact digest.
- Parsed exact archived `cdsl_daily_latest_eservices.html` (18-NOV-2026): detailed route/scheme INR arithmetic 17/17 PASS; seven category subtotal identities 7/7 PASS; sum of seven subtotals reproduces published gross purchases INR 29,344.36 cr, sales INR 16,797.46 cr and net INR 12,546.90 cr exactly. USD category subtotals sum to 1,340.9063 vs published 1,340.906 USDm (+0.0003 rounding residual); published total retained.
- CDSL states custodian/depository reports on 18-Nov and trades through previous trading day(s). NSDL Latest is headed 19-Nov and distinguishes provisional T-day exchange-member data from custodian-confirmed prior-day trades; no matched-date provider comparison, variance NOT_COMPUTABLE.
- Detail report: docs/GCR_CDSL_DAILY_18NOV2026_FULL_TABLE_ARITHMETIC_QA_CONTINUATION77_20261120.md; report blob SHA `181e041bc872d96586ead475092432b7bf8f187a`.
- CDSL daily table arithmetic PASS; matched-date NSDL/CDSL NOT_DONE; archive completeness UNKNOWN; sector predictive join BLOCKED; production NOT_AUTHORIZED. No production or cohort changes.


## India FPI — CDSL Daily Archive Static Snapshot & Freshness Boundary (Continuation 78, 2026-11-20)
- Re-fetched current ledger, GCR queue and Continuation 77; reused artifact 14527092174 / run 44519322726; ZIP SHA-256 `83048ea0bc712b6a453270f8fb5c3c6755b579857ff2ad9eb7d53c8ba1778fbd` matched.
- Exact official GET `https://www.cdslindia.com/Publications/ArchiveDataAfter2009.aspx` was captured in manifest on 2026-11-19 11:57:09.076562 UTC; HTTP 200; HTML 73,784 bytes; member SHA-256 `aa2a03c6621772e52b0b9ac52f11b525d82f1ce80539554302eda861145304df`.
- Captured page has no form/input/select/button/calendar/date selector. Static cash and derivatives report headings both say upto 02-Mar-2026. Cash table has one explicit daily date (02-Mar-2026) plus March, 2026 YTD and cumulative-since-Nov-1992 aggregate sections; derivatives are separate. CDSL Latest in same artifact is 18-Nov-2026: archive snapshot is 261 calendar days older.
- Page contains Cloudflare server/CF-RAY metadata and challenge-platform bootstrap marker, but the captured response includes static report body. No challenge bypass or undocumented request attempted. This is not evidence CDSL has no other UI or that all historical access is blocked.
- Detail report: docs/GCR_CDSL_DAILY_ARCHIVE_STATIC_SNAPSHOT_FRESHNESS_AUDIT_CONTINUATION78_20261120.md; blob SHA `69597e2fbe40d859bfbccb4af165b6c10959c4a8`.
- Decision: captured archive route is a stale static snapshot; continuous daily history UNKNOWN/NOT_ESTABLISHED; date-control execution NOT_FOUND_IN_CAPTURE; CDSL archive daily series excluded. NSDL/CDSL matched-date and production remain NOT_DONE/BLOCKED. No production changes.


## Continuation 79 — Japan (JPN) Q2-2026 BOJ/MOF portfolio-flow source contract (2026-11-20)
- Re-fetched current ledger, GCR queue and Continuation 78; did not repeat CDSL/NSDL or completed country audits.
- BOJ official BPM6 documentation confirms monthly portfolio investment assets/liabilities as separate flow legs, with gross and net transactions; asset = net acquisition of financial assets, liability = net incurrence of liabilities. Portfolio investment partner-country flows are described for 45 economies. Regional BOP is a separate quarterly partner-economy product.
- MOF official CY2026 schedule lists Q2-2026 Regional BOP release on 10-Nov-2026. BOJ public Time-Series Data Search/API supports CSV/JSON; exact portfolio series identifiers and Q2 partner-country rows were not obtained.
- Exact India bilateral row availability, Q2 values, units, raw bytes/hash and same-vintage status remain NOT_DONE / NOT_ESTABLISHED. No API request, guessed series code, net-only substitution or causal inference.
- Detail report: docs/GCR_JAPAN_JPN_Q2_2026_BOJ_MOF_PORTFOLIO_FLOW_SOURCE_CONTRACT_AUDIT_20261120.md (commit 869e0fe8b91bb48b1f14fed170706e4b834bd76c; blob 96be39472f3315ba8d5d1f22a32aebfe5c390a0d).
- Acceptance: official source-family/period/API contract PASS; exact Q2 India partner legs NOT_DONE; national/India-transmission validation PARTIAL / NOT PASS; production NOT_AUTHORIZED.
- Next exact action: inspect the official 10-Nov-2026 Q2 Regional BOP attachment and/or official BOJ 45-economy portfolio-by-counterparty data; capture/hash raw bytes before parsing, verify India row, separate assets/liabilities, unit/sign/vintage. Do not infer bilateral values from Japan aggregate BOP.
- Protected production and 63-country cohort invariants unchanged. UNKNOWN is never PASS.


## Continuation 80 — Japan Q2-2026 Regional BOP India-row inspection (2026-11-20)
- Re-fetched current ledger, GCR queue and Japan Continuation 79 report; selected only the unfinished exact attachment inspection.
- Followed MOF official release-date page to its Q2-2026 Regional BOP PDF (published 10-Nov-2026): https://www.mof.go.jp/policy/international_policy/reference/balance_of_payments/regional/rbp20260406.pdf .
- Page 8 Financial Account (Assets) and page 9 Financial Account (Liabilities) each contain a separate Portfolio Investment column and an India row; unit is 100 million yen.
- India Q2-2026 asset cell is a dash (—), not numeric zero; liability cell is 7,526 (100 million yen). No FX conversion.
- PDF was visually inspected through official document retrieval, but byte download failed; no raw file hash/headers/length claimed.
- Result: Q2 India partner-table presence PASS; liability display extraction PASS; asset leg NOT_REPORTED_IN_THIS_TABLE; dual-leg validation PARTIAL / NOT PASS; raw-byte archive NOT_DONE; production NOT_AUTHORIZED.
- Detail report: docs/GCR_JAPAN_JPN_Q2_2026_BOJ_MOF_PORTFOLIO_FLOW_SOURCE_CONTRACT_AUDIT_20261120.md (updated in this continuation).
- Next exact action: exact BOJ 45-economy portfolio asset/liability country-breakdown series for India Q2-2026; verify metadata and observations, capture/hash bytes before parsing. No guessed series IDs, no treating dash as zero, no aggregate substitution.
- All production and fixed 63-country cohort invariants unchanged. UNKNOWN is never PASS.


## Continuation 81 — Japan BOJ 45-economy monthly portfolio country-breakdown (2026-11-20)
- Re-fetched current ledger, queue and Japan report; reused Continuation 80's Q2 Regional BOP row inspection without repeating it.
- BOJ official BPM6 page and official partner list confirm Portfolio Investment Assets by issuer economy and Liabilities by transactor economy, monthly, 45 economies.
- Official MOF June-2026 Portfolio Investment PDF (preliminary), page 4 assets and page 5 liabilities, contains India rows in both sections. Unit 100 million yen.
- June India Assets: total acquisition 1,379; disposition 2,056; net -677; equity net -691; long-term debt net +14; short-term fields are dashes.
- June India Liabilities: total acquisition 1,187; disposition 2,773; net -1,586; equity 0/0/0; long-term debt acquisition dash, disposition 920, net -920; short-term 1,187/1,852/-665. Published liability net retained; displayed component net sum -1,585 leaves 1 unit residual; dash semantics/rounding not resolved.
- Assets populated component arithmetic reconciles exactly to total. Both monthly India legs have source rows. These are June preliminary month values only, not Q2 aggregate.
- PDF web extraction available; raw byte download unsupported in current session, so no raw SHA/HTTP metadata asserted.
- Status: monthly India row coverage PASS; Q2 matched-vintage Apr-Jun aggregation NOT_DONE; raw archive/hash NOT_DONE; dual-leg Q2 validation PARTIAL; production NOT_AUTHORIZED.
- Detail report updated in this continuation. Next: inspect official April and May 2026 monthly portfolio PDFs, preserve each vintage and dash; then compare with 10-Nov Q2 Regional BOP without unsupported aggregation.
- Protected invariants unchanged; UNKNOWN is never PASS.


## Continuation 82 — Japan Q2-2026 April/May monthly India portfolio-flow rows (2026-11-20)
- Re-fetched current ledger, GCR queue and Japan report; no repeat of completed June row extraction or Q2 Regional BOP page inspection.
- Official MOF April and May preliminary PDFs inspected. Both months show India in separate Portfolio Investment Assets Country Breakdown and Portfolio Investment Liabilities Country Breakdown tables (unit 100 million yen).
- April: Assets acquisition/disposition/net 739/1,487/-747; Liabilities 2,070/2,601/-531.
- May: Assets 789/1,434/-645; Liabilities 64/1,371/-1,307.
- Together with June values recorded in Continuation 81, India monthly rows are visible in both legs for Apr-Jun. Simple monthly net sums are Assets -2,069 and Liabilities -3,424 (100 million yen); these are not validated Q2 totals.
- Q2 Regional BOP Continuation 80: India asset dash, not zero; liability 7,526. Vintage/sign/definition/period reconciliation NOT_ESTABLISHED. Do not promote arithmetic sum to quarterly result.
- Official PDF extraction/screenshots available; raw byte downloads, headers and SHA-256 not captured. No raw archive claim.
- Detail report: docs/GCR_JAPAN_JPN_Q2_2026_BOJ_MOF_PORTFOLIO_FLOW_SOURCE_CONTRACT_AUDIT_20261120.md, Continuation 82.
- Status: monthly India row coverage Apr-Jun both legs PASS at table-inspection level; Q2 matched-vintage reconciliation NOT_ESTABLISHED; raw archive/hash NOT_DONE; causal transmission NOT_DONE; production NOT_AUTHORIZED.
- Next: official historical/revised-vintage bridge and Q2 Regional BOP footnote/definition audit; if no supported bridge, retain monthly and quarterly series separately.
- ₹0, official/free sources only; protected production invariants and fixed 63-country cohort unchanged. UNKNOWN is never PASS.


## Continuation 83 — Japan BOJ/MOF revision-vintage and partner-classification boundary (2026-11-20)
- Re-fetched current ledger, GCR queue and Japan report; no repeat of Continuations 80–82 data extraction.
- MOF states Preliminary/Second Preliminary figures are temporary and latest values are published under Historical Data; annual BOP revision is each April.
- BOJ official BPM6 methodology: monthly portfolio assets are by issuer economy; monthly portfolio liabilities by transactor economy; both 45 economies. Monthly preliminary data released two months after reference month; Regional BOP quarterly release five months after quarter-end. Monthly portfolio investment annual revisions in April of following two years; Regional BOP annual revisions in May of following two years.
- MOF schedule confirms Q2 Regional BOP released 10-Nov-2026. The Oct-08-2026 Q2 Second Preliminary listing is for Direct Investment and Direct Investment Income; do not assume a same-vintage second preliminary portfolio partner dataset.
- BOJ FAQ clarifies portfolio liability partner may be the foreign transactor/custodian rather than ultimate investor residence. Therefore equal country label alone does not prove exact monthly/quarterly partner equivalence.
- Q2 monthly simple net sums (-2,069 assets; -3,424 liabilities) remain arithmetic-only, not validated quarterly figures. Q2 Regional India asset dash is not zero; liability 7,526 stays separate. No reconciliation inferred.
- BOJ monthly and quarterly flat-file ZIP links were exposed, but web tool returned unsupported ZIP MIME and direct container download failed. No bytes/headers/length/retrieval UTC/hash captured; exact series IDs/raw archive NOT_DONE.
- Detail: docs/GCR_JAPAN_JPN_Q2_2026_BOJ_MOF_PORTFOLIO_FLOW_SOURCE_CONTRACT_AUDIT_20261120.md, Continuation 83.
- Status: revision calendar/partner semantics PASS; matched-vintage Q2 reconciliation NOT_ESTABLISHED; raw ZIP capture and exact series codes NOT_DONE; causal transmission NOT_DONE; production NOT_AUTHORIZED.
- Next: supported ZIP-capable capture of official BOJ monthly and quarterly flat files + specification/code lists; verify India series codes and preserve raw bytes/hash. If unavailable, no guessed series IDs.
- ₹0; no synthetic data or inferred zero; protected production invariants and fixed 63-country cohort unchanged. UNKNOWN is never PASS.


## Continuation 84 — BOJ BP01 API and flat-file exact-code retrieval bridge (2026-11-20)
- Re-fetched current ledger, GCR queue and Japan report; no repeat of Continuation 83 policy audit or prior PDF extraction.
- Official BOJ API manual confirms BP01 documented metadata endpoint `/api/v1/getMetadata?format=csv&lang=en&db=BP01`, exact-code data endpoint `/api/v1/getDataCode?format=csv&lang=en&db=BP01&startDate=202604&endDate=202606&code=<series-code>`, and layer endpoint. Series code must omit the BP01 prefix. API supports CSV/JSON; metadata updated daily; limits 250 series and 60,000 series-period points/request.
- BOJ BPM6 page exposes series-code workbook URL exbpsm6a.xlsx; BOJ Flat Files Download exposes monthly ZIP bp_m_en.zip and quarterly ZIP regbp_q_en.zip. Web retrieval rejects XLSX/ZIP MIME and direct byte download failed; no raw bytes/hash.
- BOJ statistics list confirms BP01 contains separate portfolio asset/liability country-breakdown total and instrument subseries; quarterly Regional BOP lists India. This is taxonomy confirmation only, not exact series-code extraction.
- Read-only search UI cannot execute controls; API endpoint inaccessible through current retrieval bridge. No guessed series IDs or data values.
- Detail: docs/GCR_JAPAN_JPN_Q2_2026_BOJ_MOF_PORTFOLIO_FLOW_SOURCE_CONTRACT_AUDIT_20261120.md, Continuation 84.
- Status: official API/retrieval contract and taxonomy PASS; exact codes/data/raw bytes NOT_DONE; matched-vintage reconciliation NOT_ESTABLISHED; production NOT_AUTHORIZED.
- Next: supported API/HTTP client or user-supplied official data file; capture BP01 metadata, extract exact India codes, fetch only required series, hash raw bytes before parsing.
- ₹0; protected production invariants and fixed 63-country cohort unchanged. UNKNOWN is never PASS.


## Continuation 85 — BOJ 45-vs-33 partner universe crosswalk and metadata API access gate (2026-11-20)
- Re-fetched current ledger, GCR queue and Japan report; no repeat of Continuations 80–84 data transcription.
- Official BOJ BPM6 documentation: monthly portfolio assets/liabilities country breakdown covers 45 economies; quarterly Regional BOP partner universe covers 33 economies. India appears in both, but universes are not interchangeable.
- BOJ statistics list confirms separate monthly portfolio assets and liabilities country-breakdown totals and instrument subseries, and a separate quarterly Regional BOP India entry.
- Official API manual documents BP01 metadata then exact-code API workflow; attempted metadata URL via current web bridge was inaccessible and returned no metadata body. This is transport limitation only, not proof API is down. No guessed code.
- Public Main Time-series Statistics page displays only broad current-account and financial-account net balance series; not a substitute for 45-economy portfolio country breakdown.
- Structural decision: keep monthly portfolio assets (issuer basis), monthly liabilities (transactor basis), and quarterly Regional BOP partner series separate until exact codes and partner definitions are mapped. India common label does not prove same attribution/coverage.
- Status: 45/33 universe distinction PASS; India present in both PASS; exact series codes/API metadata NOT_DONE; raw bytes/hash NOT_DONE; cross-product equivalence NOT_ESTABLISHED; production NOT_AUTHORIZED.
- Detail: docs/GCR_JAPAN_JPN_Q2_2026_BOJ_MOF_PORTFOLIO_FLOW_SOURCE_CONTRACT_AUDIT_20261120.md, Continuation 85.
- Next: supported HTTP/API client or user-supplied official metadata CSV; capture/hash BP01 metadata, extract exact India codes, query exact monthly observations and separate quarterly series.
- ₹0; protected production invariants and fixed 63-country cohort unchanged. UNKNOWN is never PASS.


## Continuation 86 — Moldova MDA Q2-2026 BNM detailed BOP source gate (2026-11-20)
- Re-fetched Master Continuity Ledger, GCR queue and relevant country history before selection. Reused fixed 63-country Q2 both-leg cohort CSV (blob 31f5bfe5adb59f4c1a139b6d8c54b5ad9fb672c8); MDA is a member with both IMF legs present. No IMF re-query or cohort rebuild.
- Repository search found no dedicated MDA national dual-leg Q2 report. Selected MDA as an executable official-source gate.
- Official BNM Q2 release dated 30-Sep-2026 exposes portfolio investment only as a net aggregate EUR -24.9m in its graphic; no separate asset/liability legs. Do not back-solve or use this net as either leg.
- Official BNM detailed BPM6 interactive report generator identified. Visible controls include indicator/parameter selection, start/end year 2009–2026, quarterly periodicity, quarter selectors I–IV, EUR/USD options, Generate/Export, Statistical Series and Metadata tabs. Read-only extraction cannot operate controls or return generated export bytes.
- Q2 workbook locator identified, but raw workbook bytes/content/hash not captured. Exact indicators, values, signs, units, revision vintage and IMF comparison remain NOT_DONE/NOT_ESTABLISHED.
- Status: cohort membership PASS; Q2 release/source route PASS; separate legs NOT_EXTRACTED; national validation PARTIAL / NOT PASS; aggregate and production NOT_AUTHORIZED.
- Detail: docs/GCR_MOLDOVA_MDA_Q2_2026_BNM_DETAILED_BOP_SOURCE_GATE_CONTINUATION86_20261120.md.
- Next: use supported interactive browser to generate/export official detailed BOP for 2026-Q2, inspect metadata and separate portfolio asset/liability series, hash raw bytes before parsing; otherwise user may attach official BNM Q2 workbook/export. No inference from net EUR -24.9m.
- ₹0; fixed cohort and all production invariants unchanged. UNKNOWN is never PASS.


## Continuation 87 — Morocco MAR Q2-2026 Office des Changes ↔ IMF dual-leg source reconciliation (2026-11-20)
- Re-fetched Master Continuity Ledger, GCR queue and MDA Continuation 86 before selection. MDA remains PARTIAL because interactive BNM export cannot be operated in current read-only browser; no repeated unsupported XLSX retrieval.
- Reused fixed 63-country Q2-2026 both-leg cohort (CSV blob 31f5bfe5adb59f4c1a139b6d8c54b5ad9fb672c8); MAR is a member. Repository search found no prior dedicated MAR Q2 dual-leg report. No cohort rebuild or IMF re-query.
- Official Office des Changes Q2-2026 preliminary BOP PDF (30-Sep-2026 release schedule), unit million MAD: portfolio assets +4,848; liabilities +36,933; balance -32,085. Component identities: assets 1,101+3,747=4,848; liabilities -855+37,788=36,933; 4,848−36,933=−32,085. All three identities exact at published precision.
- Official Ministry DSBB summary independently displays assets +4,848 and liabilities -36,933; liability sign differs from the Office des Changes PDF's explicitly labelled “net incurrence of liabilities” column. Treat as alternate signed presentation, not another observation.
- Reused existing IMF artifact run 44474218174 / artifact 14505862034; ZIP SHA-256 1a1a184f3689e04ff75d4433b44904083a33e18bdc70f096c3e9919900ebeb4f. Panel SHA e8a44abbc8455fef44cc1e4677018ae4b9634d1c04f65bf6fc6dad133cfce62a. Raw asset CSV SHA 677054017f5d3ae5fdd0403d7341588ebf43ad8b54124ae1b616bf323229326e; liability CSV SHA 713b7a3000712e2ffb07cd574d08d7e6f3c02a6b2573ce4b40d06e0458cd7bba.
- Exact IMF Q2 rows (USD, SCALE=6, ACTION=R, DERIVATION_TYPE=O): A_NFA_T OBS_VALUE -28,987,027.88 (IFS_FLAG true); L_NIL_T +9,083.44 (IFS_FLAG blank). Raw fields unchanged.
- Asset sign conflict between national labelled positive net asset acquisition and IMF negative A_NFA_T; no sign flip authorized. Liability signs agree under the explicitly labelled Office des Changes column, but currency comparison not computed because no official Q2 MAD/USD averaging convention was established. National Q2 preliminary vs IMF ACTION=R; same-vintage NOT_ESTABLISHED. National raw PDF bytes/hash not captured.
- Status: national dual-leg extraction and arithmetic PASS; IMF exact-row recovery PASS; sign reconciliation REVIEW/NOT_RESOLVED; FX numeric comparison NOT_DONE; same-vintage NOT_ESTABLISHED; MAR PARTIAL / NOT PASS; aggregate/production NOT_AUTHORIZED.
- Detail: docs/GCR_MOROCCO_MAR_Q2_2026_OFFICE_DES_CHANGES_IMF_DUAL_LEG_SOURCE_RECONCILIATION_CONTINUATION87_20261120.md.
- Next: obtain official Q2 MAD/USD conversion convention and BPM6 sign/mapping methodology; then separate-leg comparison and observation-specific revision-vintage check. No new IMF query/cohort rebuild, unsupported conversion or netting.
- ₹0; fixed cohort and production invariants unchanged. UNKNOWN is never PASS.


## Continuation 88 — Critical MAR country-key transcription correction (2026-11-20)
- Post-write independent QA reopened existing artifact 14505862034 (run 44474218174); ZIP SHA-256 recomputed 1a1a184f3689e04ff75d4433b44904083a33e18bdc70f096c3e9919900ebeb4f; normalized panel SHA-256 recomputed e8a44abbc8455fef44cc1e4677018ae4b9634d1c04f65bf6fc6dad133cfce62a.
- Found critical Continuation 87 country-key transcription error: values -28,987,027.88 / +9,083.44 USD were MDA rows mistakenly copied under MAR. Withdrawn from Morocco analysis.
- Exact filter COUNTRY=MAR, TIME_PERIOD=2026-Q2, BOP_ACCOUNTING_ENTRY=A_NFA_T/L_NIL_T yields correct values: A_NFA_T +523,948,820.8007525 USD; L_NIL_T +3,991,543,275.295832 USD. Both ACTION=R, SCALE=6, PRECISION=6, DERIVATION_TYPE=O. Raw hashes unchanged: assets 677054017f5d3ae5fdd0403d7341588ebf43ad8b54124ae1b616bf323229326e; liabilities 713b7a3000712e2ffb07cd574d08d7e6f3c02a6b2573ce4b40d06e0458cd7bba.
- Correct MAR asset/liability signs agree directionally with Office des Changes +4,848/+36,933 million MAD. Direction only; no FX magnitude comparison absent official Q2 conversion convention and vintage bridge.
- Detail report corrected with explicit Continuation 88 note. National arithmetic PASS; IMF country-key correction PASS; directional agreement PASS; FX comparison NOT_DONE; same-vintage NOT_ESTABLISHED; MAR PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Lesson: assert exact COUNTRY + TIME_PERIOD + BOP_ACCOUNTING_ENTRY before any country report write. No new IMF query or cohort rebuild.


## Continuation 88 — Nightly Rotation Review and Run #416 forward-label integrity audit (2026-11-20)
- Re-read the Master Continuity Ledger through Continuation 87, the 2026-11-20 morning Unified Top-5 report, the prior Run #407 bootstrap report, the current GCR readiness/sector-rights gates, archived data and latest relevant workflow runs. No prior dated nightly review file was found; no completed audit was repeated.
- Reused existing successful NSE Run #416 (run ID 44744602064; source commit 6572a69776272cbda3fde4fec457bddbf7c58ad5; artifact ID 14632139339). Downloaded artifact ZIP SHA-256 b12ea634f24af8241ee9a901635dd743195f4b8a3a1511cc2ffe3c3246282082, matching GitHub digest. Backtest step 13:31:06Z–13:36:04Z (~4m59s); no new workflow dispatch or collection.
- Processed archive: 200 market sessions (2026-02-16 to 2026-11-20), 2,999 symbols, 503,892 rows; QA report PASS, SHA-256 48547e28ff82e978c8b63712c9fc5e4692268c3c99fba015bd1bfa3d7bd1af19. Processed CSV SHA-256 d6810409dbd800e5146e08a1eb1e8b48207354461876acb62cbb2f656fba51db. Original raw NSE source bytes and immutable raw-file manifest are absent from the artifact/repository; processed-file hash does not replace source provenance.
- P0 source defect confirmed in pipeline/walk_forward_backtest.py (Git blob SHA-1 d085f7a2d35a88b4c4eaba65144a429a06961b09): future_outcomes uses x.shift(-1).rolling(h,min_periods=1).max(), a trailing window over shifted values, not forward T+1..T+h. For h=3 it covers source rows about T-1..T+1; h=5 covers T-3..T+1. Per-symbol shifting skips missing market sessions and min_periods=1 accepts partial horizons as mature. FUT3/FUT5 also feed prior-window P10_H3/P20_H5 training and composite WINNER_PROBABILITY/RANKING_SCORE; therefore frozen Top-30 ranking is contaminated for all three targets, including H+1. Run #407 uses the same source blob; its previous bootstrap/subgroup claims are superseded for performance interpretation.
- Denominator membership reconciled on Run #416: 258,034 raw cutoff rows; 252,020 exported eligible rows; 6,014 excluded, all HISTORY_DEPTH_AT_T<20; zero unexplained missing rows with history depth >=20. Membership scope PASS; target-label validity FAIL/BLOCKED.
- Independent post-hoc correct-forward-window diagnostic (next 1/3/5 global market sessions, require every symbol row, no forward-fill; 20,000 cutoff-cluster bootstrap) — **NOT_ADMISSIBLE as selector performance because frozen ranks were trained on faulty labels**:
  * +5% H+1: Top-30 matured 2,991/3,000; TP 653, FP 2,338; eligible matured 251,426; winners 22,468; FN 21,815; precision 21.83% (95% CI 19.53–24.20), recall 2.91% (2.63–3.20), F1 5.13% (4.66–5.63).
  * +10% H+3: Top-30 matured 2,975/3,000; TP 458, FP 2,517; eligible matured 250,356; winners 16,519; FN 16,061; precision 15.39% (13.57–17.34), recall 2.77% (2.49–3.07), F1 4.70% (4.23–5.19). 1,106 Top-30 target-class flips vs source labels.
  * +20% H+5: Top-30 matured 2,966/3,000; TP 164, FP 2,802; eligible matured 249,447; winners 5,184; FN 5,020; precision 5.53% (4.64–6.45), recall 3.16% (2.69–3.66), F1 4.02% (3.42–4.65). 651 Top-30 target-class flips vs source labels.
- Source metrics JSON H+5 precision 0.204333... implies 613 hits, while row-level predictions CSV has 616 hits; three-row serialization mismatch unresolved. Source JSON/CSV hashes: metrics 7f6fa6895c736798368411ab9963ea4ef2680ad663ef57f770925958d00a8482; Top-30 CSV 8ed2d51044373c300ecc5f64e3103b246217794af849f494d80629c967195256; eligible-universe CSV ec1361ce5275370ce1eb6fce97ba2cf86d4f7e39fc52b5b29fb435f537b43aec.
- H+3 state maturity floor: nine of ten current states have >=50 corrected-window matured rows; DATA_CONTAMINATED has 24 and remains UNKNOWN. No state calibration admitted because state/probability assignment path is affected by faulty labels.
- Morning report docs/DAILY_UNIFIED_TOP5_SWING_WATCHLIST_20261120.md records zero qualified candidates. The 10 prospective shadow-selector rows contain 7 unique symbol/cutoffs; all are outside production Top-30. Using Run #416's 2026-11-20 session vs 2026-11-19 cutoff: 7/7 H+1 mature; +2% hit 4/7, miss 3/7; +5/+10/+20 each 0/7 hit. H+1 adverse excursion median -2.17%, range -4.88% to -0.28%. H+3/H+5 7/7 immature; daily data supplies session dates only, not intraday timestamps. This is a shadow-cohort observation, not an official alert or executable return.
- Track decisions: V11.4 Historical Behavioural Selector BLOCKED / NOT_ADMISSIBLE; V11.3 Cost-aware Trade Replay UNKNOWN / NOT_AUTHORIZED / NOT_RUN (no approved G0 entry/exit/stop/circuit/size/overlap assumptions or reconciled replay); GCR UNKNOWN / BLOCKED (no synchronized macro-sector-stock vintage panel, sector rights admission or exact crosswalk). No V11.4/V11.3 metrics attributed to GCR.
- Report: docs/NIGHTLY_ROTATION_BACKTEST_RESEARCH_REVIEW_20261120.md; commit 87ae919f0f35bcdd1fb1be3d3e5d0f539f07a1a0; blob 617088f30f0430f91929688299d179b59d136fca; file SHA-256 87fad4166ce5c71252188ac91ba1ef0dc1689ae6890a4ceb6d4fece2bd1aba1e.
- Supporting audit hashes: audit script 3a69c353a03d77f871f7bd52b120dd43633bf11228fcc0cdcd4bfc83e03f4a2b; config 1d17284e1c4a16e59e51a0d117a8b1e9888cfba39bd5378ce1c61dfca1c6d8a8; corrected-label JSON f0dd74fb7936038b4503ed4e8579a6af17b9f45de9fbb59226360f660e4726a2; cutoff ledger 5cbaf23a92bb8a96b1c0d63424fbeeddeb2b02d1ff40a99351d71c820ef99617; daily outcomes CSV 65d468c7ea8a662c3cb2d131cc5ee4d636e4abf8f3afb0e8aede78c20b9f2858; audit manifest 9f57c4402ddfac6e1b16334e71c49c5c8f25f92e653b22b4e2e601d08b1e0acc.
- Next: prepare research-only forward-label v2 acceptance specification; implementation waits for user approval to move beyond Observation. Continue H+3/H+5 alert outcomes only at full maturity. Keep V11.3/GCR closed until their own gates are satisfied.
- No production change. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. No synthetic data, forward-fill, guessed mapping, fabricated timestamp, paid API or new data collection. UNKNOWN is never PASS.


## Continuation 89 — V11.4 Forward-Label V2 research-only acceptance specification (2026-11-20)
- Preflight re-fetched Master Continuity Ledger, GCR priority queue, Morocco Continuation 87/88 correction report, and the existing Daily Historical Rolling Backtest Performance Acceptance Contract. PASS work was not repeated.
- Selected the highest-priority bounded action from the latest Nightly Rotation Backtest review: formalize a research-only acceptance specification for the forward-label defect. No implementation or workflow was authorized or performed.
- Spec path: docs/V11_4_FORWARD_LABEL_V2_RESEARCH_ONLY_ACCEPTANCE_SPEC_CONTINUATION89_20261120.md; create commit 099bc6ec6edc51af0897a985b4226b703781628f.
- Specification addresses exact exchange-session T+1..T+h mapping (not symbol-row shifts), full-horizon maturity, mutually exclusive incomplete/quarantine states, point-in-time security identity, future-feature/vintage leakage, corporate-action ambiguity, duplicate/conflict handling, canonical row-ledger metric generation, exact JSON/CSV integer-count parity, denominator conservation, offline tests, <10-minute bounded jobs and independent hand-checks.
- Explicitly preserves the user's H+3 minimum 50 matured observations per State; below 50 remains UNKNOWN. DATA_CONTAMINATED remains quarantined until labels and assignment path are independently repaired.
- Prior H+5 JSON-vs-CSV 613/616 mismatch is a mandatory unresolved gate, not silently resolved by selecting one count.
- Status: specification artifact CREATED; specification review/repo re-fetch verification pending; implementation NOT_AUTHORIZED; V11.4 remains BLOCKED / NOT_ADMISSIBLE; V11.3 UNKNOWN / NOT_AUTHORIZED / NOT_RUN; GCR UNKNOWN / BLOCKED.
- No production selector, score, pressure fade, CORE-672, Engines A–E, IPO-PLX V2, weights, gates, or workflows changed. No new market data collection, no synthetic market data, ₹0.
- Next: after explicit user approval, implement in isolated research-only branch/jobs, first reproducing the failure and then passing each gate. Until then continue only matured outcome tracking and other already-authorized observation tasks.
- Lesson: specification and implementation are separate approval stages; do not cross the Observation boundary by implication.


## Continuation 90 — Independent review of Forward-Label V2 specification (2026-11-20)
- Preflight re-fetched Master Continuity Ledger, GCR Priority Queue and Continuation 89 specification; no completed PASS research was repeated.
- Independently reviewed the exact V2 specification against the existing Daily Historical Rolling Backtest Performance Acceptance Contract. Document-level checklist PASS 12/12: provenance/vintage, session spine and identity, full maturity, leakage, hand-check, denominator conservation, JSON/CSV count parity, independent metric recomputation, H+3 >=50 per-State floor, <10-minute runtime, v1/v2 isolation and approval boundary.
- Review report: docs/V11_4_FORWARD_LABEL_V2_SPECIFICATION_INDEPENDENT_REVIEW_CONTINUATION90_20261120.md; commit 6e8681739faf02ae06716a7b52c9521ff41c6c61.
- This is a document review only. It does not verify implementation, source data, labels, tests, metrics or workflow execution. Existing H+5 JSON/CSV 613-vs-616 mismatch remains unresolved.
- Status: specification review PASS 12/12; implementation NOT_AUTHORIZED pending explicit user approval; code/tests/labels/metrics NOT_RUN; V11.4 BLOCKED / NOT_ADMISSIBLE; V11.3 UNKNOWN / NOT_AUTHORIZED / NOT_RUN; GCR UNKNOWN / BLOCKED; production NOT_AUTHORIZED.
- Next: await explicit approval before V2 implementation; otherwise continue only already-authorized observation and H+3/H+5 outcome tracking after full maturity.
- No production changes, no workflow dispatch, no new data collection, ₹0. Protected invariants unchanged. UNKNOWN is never PASS.


## Continuation 91 — Morocco official FX and BPM6 sign-methodology audit (2026-11-20)
- Preflight re-fetched Master Ledger, GCR Priority Queue, Morocco Continuations 87/88, V11.4 Continuations 89/90 and nightly review. PASS work was not repeated. V11.4 implementation remains NOT_AUTHORIZED; no implementation was started.
- Selected the open Morocco Q2 MAD/USD conversion and sign-methodology task.
- Official IMF SDDS DQAF Morocco metadata confirms Office des Changes is BOP compiler, BPM6 framework, financial-account columns are net acquisitions of financial assets / net incurrence of liabilities, transactions recorded net and primarily at settlement. Official Office des Changes 2019 methodology report independently confirms net flow headings. IMF BPM6 guide states increases in assets and liabilities positive, decreases negative; financial-account balance = assets minus liabilities.
- Official BAM 2024 daily USD/MAD reference methodology located: daily rate uses volume-weighted interbank transaction quotes (08:30–15:30) when thresholds met; otherwise five-minute median bid/ask midpoint samples averaged; published daily 16:15; same-day republication possible. BAM explicitly says reference rates mainly serve revaluation of foreign-currency assets/liabilities and are not intended as FX transaction reference.
- BAM developer portal lists Cours de change Version1 REST API, but historical Q2-2026 raw daily observations, revision metadata, API query contract and Office des Changes flow-conversion rule were not established. Therefore no daily arithmetic mean, quarter-end conversion or third-party rate was used.
- Correct MAR Q2 IMF rows from Continuation 88 remain +523,948,820.8007525 USD (A_NFA_T) and +3,991,543,275.295832 USD (L_NIL_T); both ACTION=R, SCALE=6, PRECISION=6, DERIVATION_TYPE=O. National detailed Office des Changes signs (+4,848/+36,933 MDH) are directionally consistent with BPM6 increase-positive semantics; no sign flip.
- Report: docs/GCR_MOROCCO_MAD_USD_FX_AND_BPM6_SIGN_METHODOLOGY_AUDIT_CONTINUATION91_20261120.md; commit a8ecc9189d2f589cfce5d6fa57eebf248c80dac1.
- Status: BPM6 sign/recording methodology bounded review PASS; BAM reference-rate method identified PASS; Q2 flow FX convention NOT_ESTABLISHED; raw BAM Q2 daily series NOT_CAPTURED; numeric conversion/comparison NOT_DONE; same-vintage NOT_ESTABLISHED; MAR PARTIAL / NOT PASS; aggregate/production NOT_AUTHORIZED.
- Next: inspect Office des Changes current methodology appendices for explicit foreign-currency transaction conversion rule; if tied to BAM daily series, retrieve official raw Q2 series and revision metadata with hashes. If no documented convention/vintage bridge, retain PARTIAL and advance cohort.
- ₹0; fixed cohort and all production invariants unchanged. UNKNOWN is never PASS.


## Continuation 92 — Morocco BOP vs settlement FX conversion scope audit (2026-11-20)
- Preflight re-fetched Master Ledger, GCR queue, Morocco Continuation 91 FX/BPM6 report, Continuation 87/88 dual-leg report and Continuation 90 review. PASS work not repeated.
- Official Office des Changes “Balance des règlements” methodology says bank payment reports carry foreign currency, MAD countervalue and rate applied on payment execution date. However the same note explicitly distinguishes settlement balance (actual payments) from BOP (all transactions, settled or unsettled/deferred); therefore execution-date rate cannot be applied wholesale to portfolio BOP flow series.
- Official Office des Changes 2022 annual BPM6 BOP methodology says bank settlement data are the principal source for financial-account statistics and transactions are recorded as net acquisition of assets / net incurrence of liabilities, but the inspected methodology does not state a portfolio-specific foreign-currency conversion convention.
- Official metadata distinguishes transaction and settlement timing; non-goods BOP recording is mainly based on settlement data, but this still does not establish universal portfolio flow conversion.
- BAM daily reference rate remains a revaluation rate and is not an approved proxy for portfolio-flow translation. No Q2 arithmetic average, quarter-end conversion or third-party rate used.
- Report: docs/GCR_MOROCCO_Q2_2026_TRANSACTION_FX_CONVERSION_SCOPE_AUDIT_CONTINUATION92_20261120.md; commit bf6af30f4a4623f9a590405b3d31e51a0d8d6748.
- Status: BOP vs settlement methodology distinction PASS; execution-date rule applicability to all portfolio flows NOT_ESTABLISHED; official portfolio-flow MAD/USD convention NOT_ESTABLISHED; numeric comparison NOT_DONE; same-vintage NOT_ESTABLISHED; MAR PARTIAL / NOT PASS; aggregate/production NOT_AUTHORIZED.
- Next: inspect portfolio-investment statistical metadata/technical fiche for explicit conversion method; if absent, retain blocker and advance fixed cohort. No further BAM daily series retrieval until conversion rule established.
- No IMF re-query, no cohort rebuild, no production change, ₹0. UNKNOWN is never PASS.


## Continuation 93 — Morocco portfolio metadata and current BOP presentation audit (2026-11-20)
- Preflight re-fetched Master Ledger, GCR queue and Morocco Continuation 92 report; completed PASS tasks not repeated.
- Official Office des Changes “Compte d’opérations financières” metadata fiche (created/last updated 14-Oct-2013) says BPM6 recommends net asset acquisition/net liability incurrence, but its national application field says gross credit/debit presentation. Preserve this as historical metadata, not as proof of Q2-2026 current practice.
- Related “Investissement de portefeuille” metadata link resolved toward details/87 but timed out. Portfolio-specific fiche currency, valuation and FX convention NOT_RETRIEVED.
- Current Office des Changes 2024 annual BOP/IIP report p.59 says financial account is recorded as net asset/liability flows, not debit/credit; p.60 defines portfolio investment as negotiable equity/debt securities; p.36 reports 2024 portfolio assets +4,864 MDH, liabilities +3,886 MDH, balance +978 MDH. Current report supports net presentation.
- Official flow-chronology metadata says BPM6 recommends recording at transaction/ownership-transfer time; national practice records at settlement, and accrual basis when information available. This is timing, not FX conversion.
- No portfolio-specific Q2-2026 transaction/valuation currency or FX conversion convention established. No numeric MAD/USD conversion; no BAM revaluation rate proxy, arithmetic mean, quarter-end rate or third-party rate used.
- Status: current classification/net presentation PASS; historical metadata age/conflict documented PASS; portfolio fiche NOT_RETRIEVED; FX convention NOT_ESTABLISHED; numeric conversion NOT_DONE; same-vintage NOT_ESTABLISHED; MAR PARTIAL / NOT PASS; aggregate/production NOT_AUTHORIZED.
- Report path intended: docs/GCR_MOROCCO_Q2_2026_PORTFOLIO_METADATA_AND_BOP_PRESENTATION_AUDIT_CONTINUATION93_20261120.md. GitHub create returned commit c86b71dd38d21ce9312be470cf1c41f251ceb7b2, but subsequent file fetch returned 404 and create retry indicated existing path requires SHA; therefore report-file path/commit association is NOT_VERIFIED. Do not treat the report artifact as verified until resolved. The findings below are recorded in this ledger/queue.
- Decision: close this public metadata route as NOT_ESTABLISHED and advance to next unfinished country in the fixed cohort; revisit MAR only if current versioned fiche/technical note provides explicit FX convention. No IMF re-query or cohort rebuild.
- ₹0; fixed 63-country cohort and production invariants unchanged. UNKNOWN is never PASS.


## Continuation 94 — Nepal NPL NRB BPM6 byte-route closure (2026-11-20)
- Preflight re-fetched Master Ledger, GCR queue, NPL Continuation 58 retrieval-route report and NPL source-boundary report. PASS work not repeated.
- Reconfirmed official NRB External Sector page lists monthly BOP BPM6 dataset and exact workbook URL. Web retrieval returns unsupported XLSX MIME; separate container byte-download invocation also failed. No bytes, workbook structure, values, or SHA-256 captured.
- NRB NSDP currently linked BOP XML remains stale (NEPAL_BOP_2024_Q1.xml); not admitted for Q2-2026. Monthly Banking & Financial Statistics publications remain rejected as wrong document family under Continuation 57.
- Exact report: docs/GCR_NEPAL_NPL_Q2_2026_NRB_BPM6_BYTE_ROUTE_CLOSURE_CONTINUATION94_20261120.md; commit 3d578a8d292a8373f40403094752e297c031b2b5.
- Status: official dataset discovery PASS; exact XLSX locator PASS; browser and separate byte route BLOCKED; workbook bytes/hash/sheets NOT_CAPTURED; Q2 period basis, separate legs, sign/unit/vintage NOT_ESTABLISHED; numeric comparison NOT_DONE; NPL PARTIAL / NOT PASS; aggregate/production NOT_AUTHORIZED.
- Decision: close this exact URL route; do not retry without a genuinely new supported mechanism. Advance to next eligible member of same fixed 63-country cohort after preflight. No IMF re-query or cohort rebuild.
- No new data collection beyond source-route check, ₹0; all production invariants unchanged. UNKNOWN is never PASS.


## Continuation 95 — Romania ROU BNR/ECB portfolio source gate (2026-11-20)
- Preflight re-fetched current Master Ledger (pre-task blob SHA d913928ec432d55d4cccfc6c0e9783ff9000a94f), GCR priority queue (pre-task blob SHA 37d17a2b4ffe3350c446af41acbf2d6f4a146d61), and fixed 63-country Q2-2026 both-leg cohort (blob SHA 31f5bfe5adb59f4c1a139b6d8c54b5ad9fb672c8). ROU is a member with both IMF legs present; no dedicated ROU Q2-2026 national dual-leg report found.
- After NPL's exact NRB XLSX route was closed, selected ROU as the next bounded country-source gate. No NPL route retry, no cohort rebuild, no IMF re-query.
- Official IMF SDDS/DQAF Romania metadata identifies BNR/NBR as compiler, BPM6 framework, quarterly dissemination ~85 days after quarter-end, and financial-account transactions gross-compiled but disseminated net separately for asset and liability components. It also records monthly revisions and subsequent quarter revisions.
- ECB BPS catalogue identifies Romania monthly total-economy portfolio-liability transaction series in RON and states source = National Bank of Romania. Monthly series metadata includes “summed through period”; do not aggregate until its semantics are confirmed. Indexed quarterly Romania transaction series inspected was last updated 17-Apr-2026, before Q2-2026.
- Exact ECB SDW API CSV requests for monthly total-economy portfolio assets and liabilities, 2026-04 to 2026-06, both inaccessible through the current retrieval bridge. No response bytes, values, headers or hashes captured. No Q2 values admitted.
- Report: docs/GCR_ROMANIA_ROU_Q2_2026_BNR_ECB_PORTFOLIO_SOURCE_GATE_CONTINUATION95_20261120.md; create commit 4157f08081d19e8876ad1561e4f8f293157230e7; verified report blob SHA 37f744511aeab33539d1fca15be0bce08536cd90.
- Status: ROU cohort membership PASS; official methodology/source-family discovery PASS; exact Q2 national asset/liability observations NOT_CAPTURED; monthly-vs-quarterly/cumulative basis NOT_ESTABLISHED; unit/sign/vintage bridge NOT_ESTABLISHED; numeric comparison NOT_DONE; ROU PARTIAL / NOT PASS; aggregate/production NOT_AUTHORIZED.
- Next: obtain both separate Q2 portfolio transaction legs through a supported official BNR or ECB SDW API/export; archive raw bytes and vintage metadata before parsing. Monthly aggregation only if the source confirms flow semantics. Reuse archived IMF exact ROU rows; no new IMF GET. If blocked, preserve PARTIAL and advance within fixed cohort.
- ₹0; no synthetic data, no stock-as-flow, no unverified aggregation, no netting, no production changes. Protected selector/score/pressure fade/CORE-672/Engines A–E/IPO-PLX V2 unchanged. UNKNOWN is never PASS.


## Continuation 96 — Romania ROU ECB/BNR methodology and retrieval boundary (2026-11-20)
- Preflight re-fetched current ledger (blob SHA c63e739e3711bd7624ba738f4cb66185e1b2a468), GCR queue (blob SHA 278bdc6288c99663aaccf81223d682966f0f7bdb), and ROU Continuation 95 report (blob SHA 37f744511aeab33539d1fca15be0bce08536cd90). Fixed 63-country cohort reused; no rebuild or IMF query.
- New official IMF Romania DSBB finding: BNR portfolio investment coverage is partial because external custodian information is not fully available.
- New official ECB BOP/IIP e-book §7.3 Romania method: portfolio investment is compiled from monthly security-by-security stocks with derived monthly flows; flows are derived from changes in stocks with price, FX and other changes separately compiled. Asset reference data use CSDB; non-ISIN flows are negligible; Romanian debt securities held by non-residents at external custodians are not covered; liability compilation uses residual approach and SHSDB since 2020.
- ECB asset series page confirms monthly, EUR million, collection indicator “Summed through period”; page update field 17-Apr-2026 and source field ECB. Corresponding liability page returned 503. Exact ECB API asset/liability calls for Apr-Jun 2026 remain inaccessible. No response bytes, headers, values, retrieval receipt or SHA-256. Container download retry produced no file. Search index update date alone not treated as evidence of data contents/vintage.
- Decision: close the current ECB API route; ROU remains PARTIAL / NOT PASS. The source coverage caveat is material and cannot be cleared by rounding match alone. Revisit only with supported BNR interactive/data-set export or verified ECB byte-preserving route with both legs and vintage.
- Report: docs/GCR_ROMANIA_ROU_Q2_2026_ECB_BNR_METHODOLOGY_RETRIEVAL_BOUNDARY_CONTINUATION96_20261120.md; create commit ba48066871b9fc5c0cb279b933abc25232d1f175; verified blob SHA 6f3c046255ada664589286bdae276606588cc9a4.
- Aggregate/production NOT_AUTHORIZED; no cohort rebuild, no IMF re-query, no stock-as-flow, no unverified monthly aggregation, no netting, no production changes. ₹0; UNKNOWN is never PASS.


## Continuation 97 — Rwanda RWA BNR Q2-2026 portfolio source gate (2026-11-20)
- Preflight re-fetched current Master Ledger (blob SHA 1c99bc983be5ecc2f78f2ecf4f7ee6ac52b276d5), GCR queue (blob SHA b5f66fc867c1cce3645256f4067cafc035a3c18e), immutable 63-country Q2-2026 cohort (blob SHA 31f5bfe5adb59f4c1a139b6d8c54b5ad9fb672c8), and ROU reports 95/96. RWA is the next cohort country after ROU; no dedicated RWA Q2 report existed. PASS work skipped; no cohort rebuild or IMF re-query.
- BNR External Sector Statistics portal states BOP/IIP statistics follow BPM6 and lists a “Balance of Payment” item dated 30-Jun-2026. Portal is JS-rendered; exact file locator/bytes unresolved.
- BNR Annual Report 2024-2025 Appendix 14 contains historical fiscal-year BOP separate portfolio assets and liabilities in USDm. FY2024/25: assets 12.1, liabilities 6.3, net 5.8; FY2022/23: assets 50.2, liabilities -58.4, net 108.6. Historical rows support a country-specific arithmetic diagnostic (net = assets − liabilities), not Q2-2026 validation and not an exact IMF concept/sign bridge. Fiscal-year values must not be prorated/interpolated into calendar quarters.
- BNR MPFSS October 2026 Table 12 provides 2026H1 portfolio investment net +14 USDm only; separate H1 asset/liability legs and standalone Q2 are absent. August 2026 MPR summary BOP does not supply portfolio legs. No net-to-leg inference.
- Direct byte download of the BNR annual PDF failed. No raw PDF bytes, headers, byte count, retrieval receipt or SHA-256 captured. BNR portal's 30-Jun-2026 BOP item URL/bytes also NOT_RESOLVED.
- Report: docs/GCR_RWANDA_RWA_Q2_2026_BNR_PORTFOLIO_SOURCE_GATE_CONTINUATION97_20261120.md; create commit ef71745ec25c570886974883bbe9cd194cba2547; verified report blob SHA af725eba157789e16e65a783e886d96f66fdc727.
- Status: RWA cohort PASS; official BPM6 source discovery PASS; historic fiscal-year dual legs PASS (context only); 2026H1 net-only +14 USDm PASS (context only); Q2-2026 national A_NFA_T/L_NIL_T NOT_CAPTURED; same-vintage comparison NOT_DONE; RWA PARTIAL / NOT PASS; aggregate/production NOT_AUTHORIZED.
- Next: resolve the BNR 30-Jun-2026 BOP dataset through a supported downloadable route, capture raw bytes and SHA-256, inspect frequency/period and separate legs. If it is IIP stock or net-only, reject. Reuse archived IMF RWA rows; no new IMF query. If blocked, close exact route and advance after preflight.
- ₹0; no synthetic data, no FY proration, no quarterly interpolation, no net-to-leg inference, no production changes. Protected invariants unchanged; UNKNOWN is never PASS.


## Continuation 98 — Rwanda RWA official source-family rejection / quarter-boundary audit (2026-11-20)
- Preflight re-fetched current Master Ledger (blob SHA 531da8638ca5cddde0af73687311a77272b3d5f7), GCR queue (blob SHA 4d382f5517699c78b6b5c5fee29e3836b53679cc), RWA Continuation 97 (blob SHA af725eba157789e16e65a783e886d96f66fdc727) and fixed cohort (blob SHA 31f5bfe5adb59f4c1a139b6d8c54b5ad9fb672c8). RWA remains a member with both IMF legs present; prior work reused; no IMF re-query or cohort rebuild.
- New official NISR Formal External Trade Q2-2026 page found: goods exports USD 548.98m, imports USD 1,606.39m, re-exports USD 179.59m, trade balance -USD 877.81m. This is goods trade, not financial-account portfolio investment; explicitly rejected for A_NFA_T/L_NIL_T validation.
- BNR August 2026 MPFSS Table 2 is Q1-2026 summary without portfolio legs; rejected wrong period/no dual legs. BNR October 2026 MPFSS Table 12 remains H1 net-only +14 USDm, not Q2 and not separate legs. BNR 30-Jun-2026 portal item remains JS-only to retrieval client; exact file URL/bytes/frequency unresolved.
- Report: docs/GCR_RWANDA_RWA_Q2_2026_OFFICIAL_SOURCE_FAMILY_REJECTION_CONTINUATION98_20261120.md; create commit 1f8997f5c491f62c494fb77494ce1a43537fedcf; verified report blob SHA 001cc1fc2d6f698566206a7e746871d9eba1ee90.
- Status: Q2 goods-trade discovery PASS; wrong-family/period rejection PASS; BNR Q2 BOP file NOT_RESOLVED; Q2 national asset/liability NOT_CAPTURED; comparison NOT_DONE; RWA PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Next: close identical JS-only portal request route. Reopen only with a genuinely new supported official direct dataset/API locator; otherwise advance to next eligible fixed-cohort member after preflight. No IMF re-query/cohort rebuild.
- ₹0; no trade-to-BOP substitution, no net-to-leg inference, no FY proration, no interpolation, no production changes. UNKNOWN is never PASS.


## Continuation 99 — Solomon Islands SLB CBSI Q2-2026 portfolio source/sign-conflict audit (2026-11-20)
- Preflight re-fetched Master Ledger (blob SHA 1194f809a00a214913a5535969d3f80111e5fd1e), GCR queue (blob SHA 15501663d5fbb531e220c5cc2546400477e550b2), RWA Continuation 98 (blob SHA 001cc1fc2d6f698566206a7e746871d9eba1ee90), and fixed 63-country cohort (blob SHA 31f5bfe5adb59f4c1a139b6d8c54b5ad9fb672c8). Reused SAU source-vintage follow-up and excluded its already-completed displayed-rounding numeric PASS; SLB is next cohort member after RWA, both IMF legs present; no prior SLB Q2 report found. No cohort rebuild/IMF re-query.
- Official CBSI BOP page says quarterly and annual BOP includes financial account and is BPM6; latest 2026-Q2. CBSI June 2026 Quarterly Review Table 1.17 (SBD million; quarterly through 2026-Q2) reports financial-asset portfolio investment +38 SBDm and financial-liability portfolio investment “-” (general note defines dash as nil).
- Material internal conflict: Chapter IV narrative says portfolio investment recorded a wider deficit of $38m in Q2, while Table 1.17 shows portfolio asset +38 and liability nil. The publication context does not resolve whether this is reverse sign convention, net balance presentation or editorial inconsistency. No sign flip or zero-to-IMF-leg mapping admitted.
- Table 1.14 IIP portfolio asset position SBD 373m is a stock and rejected as flow. No IIP stock substitution.
- Exact IMF SLB rows not captured: large archived panel blob SHA 2a8db2878cac6323bbad74ffa4035dc70e5e6b98; GitHub fetch returned empty content. No new IMF query. CBSI PDF direct byte download failed; no raw PDF bytes/hash/headers/receipt. SBD/USD transaction conversion and same-vintage not established.
- Report: docs/GCR_SOLOMON_ISLANDS_SLB_Q2_2026_CBSI_PORTFOLIO_SOURCE_SIGN_CONFLICT_CONTINUATION99_20261120.md; create commit 0552b4e1f7aa429c1e0c213235b7d5f25fa007e7; verified report blob SHA 7a696af5f0562941f59363d10bb6b58199319049.
- Status: SLB cohort PASS; official BPM6 source PASS; Q2 portfolio asset +38 SBDm and liability nil published; narrative/table sign conflict BLOCKED; IMF exact rows NOT_CAPTURED; SBD/USD basis NOT_ESTABLISHED; comparison NOT_DONE; SLB PARTIAL / NOT PASS; aggregate/production NOT_AUTHORIZED.
- Next: retrieve CBSI sign/methodology note; expose exact archived IMF rows without new IMF query; establish transaction FX and vintage; archive original PDF bytes; only then compare separate legs. Otherwise preserve PARTIAL.
- ₹0; no sign flip, no net-to-leg inference, no IIP stock-as-flow, no inferred FX, no production changes. Protected invariants unchanged; UNKNOWN is never PASS.


## Continuation 100 — El Salvador SLV Q2-2026 BCR portfolio source-family gate (2026-11-20)
- Preflight re-fetched Master Ledger (blob SHA 185e55b1423c6b55ac24717a4bc6c893135acb4c), GCR queue (blob SHA 03e99b7cc65ef685d3857ac45ebec25cb06493b3), SLB Continuation 99 (blob SHA 7a696af5f0562941f59363d10bb6b58199319049), exact-sample receipt (blob SHA 053fa26e9feaab26d5bb4c35911a09fc3f71d1bd), and fixed 63-country cohort (blob SHA 31f5bfe5adb59f4c1a139b6d8c54b5ad9fb672c8). SLV is next after SLB, both IMF legs present; no dedicated SLV report found. No cohort rebuild or IMF re-query.
- BCR official June-2026 financial statement in USD thousands shows “Inversiones en el Exterior (Neto)” balance-sheet stock: 3,834,678.3 at Mar-2026 and 4,233,089.5 at Jun-2026. Explicitly rejected as economy-wide BOP portfolio transaction legs; stock difference is not a transaction flow.
- IMF staff's El Salvador 2025 EFF/Article IV Table 3a provides annual BPM6 portfolio investment net and separate assets/liabilities, sourced from BCR and IMF staff estimates. It is annual historical/projection context, not Q2-2026 national data; not prorated.
- Existing exact sample receipt includes 12 countries and not SLV. Large panel GitHub fetch remains empty; exact SLV IMF rows NOT_CAPTURED. No new IMF query.
- Report: docs/GCR_EL_SALVADOR_SLV_Q2_2026_BCR_PORTFOLIO_SOURCE_FAMILY_GATE_CONTINUATION100_20261120.md; create commit 94cec1b68b19e8fef099bc4ccbf2083cfaa7a286; verified report blob SHA 658b83d795529e9eecd99879039e6e8bcdb6a8c3.
- Status: SLV cohort PASS; BCR national source identification PASS; Q2 national A_NFA_T/L_NIL_T NOT_CAPTURED; same-vintage comparison NOT_DONE; SLV PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Next: locate BCR official Q2-2026 quarterly BOP financial-account portfolio table with separate assets/liabilities; capture raw bytes, vintage and SHA-256. Retrieve archived exact IMF rows without re-query; compare only after concept/sign/scale bridge.
- ₹0; no stock-as-flow, no annual-to-quarter proration, no net inference, no FX inference, no production changes. Invariants preserved; UNKNOWN is never PASS.


## Continuation 101 — Serbia SRB NBS BPM6 Q2-2026 portfolio dual-leg source gate (2026-11-20)
- Preflight re-fetched current Master Continuity Ledger (blob SHA dc5b53b50cea760387096f0028b52c3892373b71), GCR Priority Queue (blob SHA f048598e774639cb80441e22dacc341efa3d00b2), SLV Continuation 100 (blob SHA 658b83d795529e9eecd99879039e6e8bcdb6a8c3) and immutable 63-country cohort (blob SHA 31f5bfe5adb59f4c1a139b6d8c54b5ad9fb672c8). SRB is next after SLV; both IMF legs present; no dedicated SRB report existed. No cohort rebuild or IMF re-query.
- Official NBS Statistical Bulletin September 2026, Table 2.3 (BPM6, monthly EURm, preliminary), provides separate portfolio asset/liability flow rows. Apr/May/Jun 2026 sums: assets +248; liabilities +4,112; net -3,864. Arithmetic identity and sum of monthly net rows agree.
- Material QA flag: May 2026 portfolio liabilities +3,932 EURm is unusually large; retained as published and must be checked against the official downloadable series / subsequent vintage. No correction or sign transform.
- Detail report: docs/GCR_SERBIA_SRB_Q2_2026_NBS_BPM6_PORTFOLIO_DUAL_LEG_SOURCE_GATE_CONTINUATION101_20261120.md; create commit a2ae592c6416ee54786be29c684f8bf753056312.
- National values extracted from official NBS PDF web text only; raw PDF bytes/byte count/SHA-256 NOT_CAPTURED. Exact archived IMF SRB rows NOT_CAPTURED; concept/sign bridge and same-vintage NOT_ESTABLISHED; comparison NOT_DONE. SRB PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Next: byte-preserving NBS PDF capture/hash; verify May liability observation and vintage; retrieve archived IMF SRB exact rows without new query; establish official mapping and compare both legs separately.
- ₹0; all protected V11.3 invariants unchanged; UNKNOWN is never PASS.


## Continuation 102 — Serbia SRB archived IMF exact Q2-2026 dual-leg extraction (2026-11-20)
- Preflight re-fetched current Master Ledger (blob SHA c57d93a381c4a6cee039c0d2bd58f64410c33aae), GCR queue (blob SHA 4281684d9c879c1ce62ca8a8ececebf3ac365c6b), SRB Continuation 101 (blob SHA ca0eb8844ab9d14a378f4278506f363fdf776c65), and immutable cohort (blob SHA 31f5bfe5adb59f4c1a139b6d8c54b5ad9fb672c8). No completed work repeated.
- Existing archived IMF panel blob SHA `2a8db2878cac6323bbad74ffa4035dc70e5e6b98` successfully fetched through blob SHA route after ordinary large-file fetch returned empty. Extracted exact Q2-2026 SRB rows: A_NFA_T 288,993,091.8400176 USD / 10^6 = USD 288.9930918400176m; L_NIL_T 4,782,903,852.31975 USD / 10^6 = USD 4,782.90385231975m. Embedded asset source-file SHA256 677054017f5d3ae5fdd0403d7341588ebf43ad8b54124ae1b616bf323229326e; liability source-file SHA256 713b7a3000712e2ffb07cd574d08d7e6f3c02a6b2573ce4b40d06e0458cd7bba.
- No new IMF query or cohort rebuild. Exact IMF rows CAPTURED. NBS Sep-2026 bulletin itself confirms May liability +3,932 EURm; independent later-vintage confirmation still NOT_DONE.
- NBS Q2 EURm values remain assets +248 / liabilities +4,112 / net -3,864. USD/EUR transaction FX basis and official sign/concept mapping not established; same-vintage not established; comparison NOT_DONE. NBS PDF raw bytes/hash NOT_CAPTURED. SRB PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Detail report: docs/GCR_SERBIA_SRB_Q2_2026_ARCHIVED_IMF_EXACT_DUAL_LEG_ROW_EXTRACTION_CONTINUATION102_20261120.md; create commit daed219c211da0290f74c1c5c27af11723adbeb3.
- Next: independent NBS May observation/vintage check, PDF raw capture/hash, official transaction FX and sign/concept bridge, then compare each leg separately.
- ₹0; protected V11.3 invariants unchanged; UNKNOWN is never PASS.


## Continuation 103 — Serbia SRB NBS BPM6 sign / FX methodology and later-vintage route (2026-11-20)
- Preflight re-fetched Master Ledger (blob SHA bd4259ad6176cbbcd0d481c12c012efff63f7493), GCR queue (blob SHA 250e3cce04832837cf942b6cd285c62db825b7a2), SRB Continuation 102 (blob SHA 874f1908814137b67c0d4032752b73dd3a29e207), and Continuation 101 (blob SHA ca0eb8844ab9d14a378f4278506f363fdf776c65). No PASS work repeated.
- Official NBS BPM6 Explanatory Notes confirm transaction-date official middle NBS FX rate for original-currency conversion; increases in assets/liabilities positive, decreases negative; net=assets−liabilities. NBS-side sign and transaction-FX methodology PASS.
- Aggregate EUR-to-USD conversion still NOT_ESTABLISHED; transaction-level data/time are unavailable in aggregate table, so no generic period FX rate used. IMF indicator sign/concept mapping and same-vintage alignment NOT_ESTABLISHED.
- Official NBS BOP page lists September 2026 monthly and detailed BPM6 XLS files; latest developments release dated 18-Nov-2026. Attempted official XLS route rejected by current retrieval bridge (unsupported content type); raw workbook bytes/sheets/hash not captured; May revision check NOT_DONE.
- Report: docs/GCR_SERBIA_SRB_Q2_2026_NBS_BPM6_SIGN_FX_METHODOLOGY_AND_REVISION_ROUTE_CONTINUATION103_20261120.md; create commit 97226fa883b88f0546b4b72e92ae10fa602c731f.
- Next: supported XLS byte retrieval, May 2026 revision verification, official IMF A_NFA_T/L_NIL_T definition bridge; compare only after same-vintage/concept basis.
- ₹0; protected invariants unchanged; UNKNOWN is never PASS.


## Continuation 104 — Serbia SRB IMF BPM6 code bridge and NBS later-vintage limit (2026-11-20)
- Preflight re-fetched Master Ledger (blob SHA e0a7e5641a17363311ce4372f75fba5369be6f73), GCR queue (blob SHA 0888f0895bfd817cbda671d4e9831ed09d5af032), SRB Continuation 103 (blob SHA a6a19a1521d8c405c25cd1e8129912fdc2c80d61), Continuation 102 (blob SHA 874f1908814137b67c0d4032752b73dd3a29e207), and Continuation 101 (blob SHA ca0eb8844ab9d14a378f4278506f363fdf776c65). No PASS work repeated.
- Official IMF BPM6 Compilation Guide Appendix 7: A7.7 accounting entry N=net, A=assets, L=liabilities; Table A7.2 3B=portfolio investment. IMF BPM6 Manual 6.54 defines portfolio as cross-border debt/equity securities excluding direct investment and reserve assets. Standards-level semantic mapping of A_NFA_T/L_NIL_T, P_F to NBS portfolio assets/liabilities PASS; national scope/timing/valuation equivalence remains NOT_ESTABLISHED.
- Official NBS September 2026 developments PDF (18-Nov-2026) inspected; Jan-Sep portfolio net inflow EUR 4.4bn, contextual only; no May separate leg revision evidence. XLS and detailed XLS endpoints return unsupported content type; workbook bytes/values/hash NOT_CAPTURED.
- Report: docs/GCR_SERBIA_SRB_Q2_2026_IMF_BPM6_CODE_BRIDGE_AND_LATER_VINTAGE_LIMIT_CONTINUATION104_20261120.md; create commit 43cbf03ef895535ad10d05cd56673012d3b86a9d.
- Exact IMF rows remain captured. May later-vintage separate legs NOT_CAPTURED; transaction-weighted FX bridge NOT_ESTABLISHED; national mapping/coverage equivalence NOT_ESTABLISHED; comparison NOT_DONE. SRB PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Next: supported XLS/CSV raw retrieval, May revision check, official USD or transaction-weighted FX bridge, separate leg comparison.
- ₹0; protected invariants unchanged; UNKNOWN is never PASS.


## Continuation 105 — Serbia SRB NBS alternate public data-route audit (2026-11-20)
- Preflight re-fetched Master Ledger (blob SHA 554fa175e22b21db928da579a05ffc63d267fda0), GCR queue (blob SHA ca9822d94a496ec27b5665d2c223c548b800a7fa), Continuation 104 (blob SHA fd1253e3c6f9b2681a825a756c4a88252f83ee80); completed PASS work excluded.
- NBS BOP page lists September 2026 monthly and detailed BPM6 XLS files; both links fail retrieval with unsupported XLS content type. No raw bytes/sheets/values/hash.
- Statistical Bulletin “Data series in XLS format” resolves to generic Statistics landing page; no separate public CSV/HTML monthly BOP flow route or official USD separate-leg series located in inspected NBS pages. Scoped NOT_FOUND only.
- NBS release calendar schedules 3-Dec-2026 for October 2026 bulletin; future candidate, not current data.
- Report: docs/GCR_SERBIA_SRB_Q2_2026_NBS_ALTERNATE_DATA_ROUTE_AND_NEXT_VINTAGE_GATE_CONTINUATION105_20261120.md; create commit d82302447ca36e0700af3de96d5c0f8561d0340d.
- May revision NOT_CAPTURED; USD/EUR transaction bridge NOT_ESTABLISHED; national equivalence NOT_ESTABLISHED; SRB PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Next: inspect NBS archive form underlying endpoint with supported byte-preserving route; re-check October 2026 bulletin after 3-Dec release; verify actual units before use.
- ₹0; protected invariants unchanged; UNKNOWN is never PASS.


## Continuation 106 — Serbia SRB NBS archive form schema and web-service access gate (2026-11-20)
- Preflight re-fetched Master Ledger (blob SHA b3d818fa8ad5d5ea3a2c5c2efad82cdd7c222edc), GCR queue (blob SHA aa260f77f4a282db6246ebdd6ecc147a1b2489eb), Continuation 105 (blob SHA 916a9d07c1e15f36a24bfe3d28b11c7958e6c90a). PASS work excluded.
- Official NBS BOP page shows monthly BPM6 and detailed archive forms, each Select + five Inputs + Show. Extracted page text exposes no DOM names/options/form action/query/download URL; endpoint not guessed.
- Official NBS web-service page requires a certified application and NBS-issued username/password/licence code. No application or external contact made. Whether archive UI requires this service account UNKNOWN.
- Report: docs/GCR_SERBIA_SRB_Q2_2026_NBS_ARCHIVE_FORM_AND_WEBSERVICE_ACCESS_GATE_CONTINUATION106_20261120.md; create commit b7309fd69b0783ca4bdc6a4bea9c2de34b6bec40.
- XLS raw bytes/sheets/values/hash and May later-vintage separate legs NOT_CAPTURED; USD series NOT_LOCATED; FX bridge NOT_ESTABLISHED; SRB PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Next: inspect archive form DOM/submission via actual browser; capture binary; parse May asset/liability rows; no authenticated service application without explicit authorization.
- ₹0; protected invariants unchanged; UNKNOWN is never PASS.


## Continuation 107 — Serbia SRB NBS July-2026 prior-vintage candidate (2026-11-20)
- Preflight re-fetched Master Ledger (blob SHA 761c100c418e2c7c003df0e46952deeebac34bba), GCR queue (blob SHA dbec3cfe50a6c13022252c0cf687d15620884368), Continuation 106 (blob SHA e5994fc9b1318aaa5b4cc4c4db8aaa1f91106b30); PASS work excluded.
- Located official NBS July-2026 Statistical Bulletin PDF (156 pages), Table 2.3 printed p.105. Text extraction includes portfolio asset/liability rows and a liability value 3,932, but the month header could not be re-opened due PDF timeout.
- July-vintage month attribution of +3,932 NOT_VERIFIED; cross-vintage consistency NOT_DONE. September-2026 May value +3,932 EURm remains existing C101/C102 evidence.
- Report: docs/GCR_SERBIA_SRB_Q2_2026_NBS_JULY_BULLETIN_PRIOR_VINTAGE_CROSSCHECK_CONTINUATION107_20261120.md; create commit e952b837e44f686b76218504214da85de2b4022e.
- Next: recover Table 2.3 header/page image, verify month attribution, compare July vs September values. XLS bytes and USD/EUR bridge remain unresolved.
- ₹0; protected invariants unchanged; UNKNOWN is never PASS.


## Continuation 108 — Serbia SRB July Bulletin Table 2.3 header recovery (2026-11-21)
- Preflight re-fetched Master Ledger (blob SHA 698a63e3efe4d1a77aa60f097e38d7f594e62a6f), GCR queue (blob SHA 7c6bc3b48199d8523c040edb9513a58c48afba83), Continuation 107 (blob SHA d7c063d63b2b8a19ff94c6b4fd31a82de98e7729). No PASS work repeated.
- Official July 2026 Statistical Bulletin PDF open timed out; binary download failed; exact indexed header search returned no result. NBS index/news archive confirm July Bulletin published 03-Sep-2026, publication date only.
- July Table 2.3 rows include a 3,932 liability value in prior text extraction, but month header remains NOT_VERIFIED; May cross-vintage comparison NOT_DONE. September 2026 May values remain captured in prior evidence.
- Report: docs/GCR_SERBIA_SRB_Q2_2026_JULY_BULLETIN_HEADER_RECOVERY_AND_VINTAGE_GATE_CONTINUATION108_20261121.md; create commit f88dce5962c98f799d494dce9700edd891cfe19b.
- Next: acquire PDF bytes through browser/alternate official route; inspect header; compare separate May legs across vintages only after exact alignment.
- ₹0; protected invariants unchanged; UNKNOWN is never PASS.


## Continuation 109 — Serbia SRB September-vintage exact month header verification (2026-11-21)
- Preflight re-fetched Master Ledger (blob SHA ccdda277aa8ee8cfa91a8d98c459e1dd24980509), GCR queue (blob SHA 545794c9590ebf5649b2d01a8dda0ad391e4a34a), Continuation 108 (blob SHA bac151f983b989d7bf5dae0d981b8bcbc6ab4d7d). Completed PASS work skipped.
- Official NBS September-2026 Statistical Bulletin Table 2.3 opened in full at printed p.105. Header at lines 8110–8111 explicitly maps 2026 May to the 10th data column after ITEM.
- May 2026 September-vintage values: portfolio assets -25 EURm; liabilities +3,932 EURm; net -3,957 EURm. Lines 8145–8147. Arithmetic identity -25 - 3,932 = -3,957 PASS. Notes lines 8178–8180 say data available until 17-Sep-2026 and subject to correction.
- This closes exact month mapping for September vintage only. July Bulletin PDF remains timeout; prior extracted 3,932 row lacks header. July month mapping NOT_VERIFIED; July-vs-September revision NOT_DONE.
- Report: docs/GCR_SERBIA_SRB_Q2_2026_SEPTEMBER_VINTAGE_EXACT_MONTH_HEADER_VERIFICATION_AND_JULY_LIMIT_CONTINUATION109_20261121.md; create commit 4c8e006e31eeb8878f14846d762e8dd08cb122d1.
- USD/EUR transaction-weighted bridge and national scope/timing/valuation equivalence NOT_ESTABLISHED. SRB PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Next: recover July PDF through browser/alternate official route, verify month header, then compare separate legs/vintages.
- ₹0; protected invariants unchanged; UNKNOWN is never PASS.


## Continuation 110 — Serbia SRB NBS July Bulletin Serbian archive route (2026-11-21)
- Preflight re-fetched Master Ledger (blob SHA 856d68b455fd5f80cf5d19aae5fb82717f447ef2), GCR queue (blob SHA 6460923fd2db5f709708b3c6d1e1b74f202d6a36), Continuation 109 (blob SHA e3217fd96e3fbc3dd1593e787029e3cafd929100). Completed PASS work excluded.
- Official Serbian archive confirms July Bulletin issue date 31-Aug-2026; Serbian news archive title “Statistički bilten - jul 2026. godine” dated 31.08.2026. English archive lists 03-Sep-2026. These dates establish issue existence, not table column mapping.
- Serbian archive text shows interactive form only, no July PDF href; direct English July PDF open still times out. No raw PDF bytes/header recovered.
- September-vintage May values remain PASS from C109: assets -25 EURm, liabilities +3,932 EURm, net -3,957 EURm; identity holds. July month mapping NOT_VERIFIED; July-vs-September comparison NOT_DONE.
- Report: docs/GCR_SERBIA_SRB_Q2_2026_JULY_BULLETIN_SERBIAN_ARCHIVE_ROUTE_AND_REVISION_STATUS_CONTINUATION110_20261121.md; create commit 1e38f608fdb6c8d188b7ceaa57f6182696ada7db.
- Next: real-browser DOM inspection of Serbian archive form, use Show action, capture official July PDF bytes and inspect header; no authenticated application without approval.
- ₹0; protected invariants unchanged; UNKNOWN is never PASS.


## Continuation 111 — Serbia SRB July Bulletin retrieval route exhaustion (2026-11-21)
- Preflight re-fetched Master Ledger (blob SHA eeef11fd8bfd0ed321e5e5ba35ccf3a6c52f79c9), GCR queue (blob SHA 831c53b4843e9afcac1402a54d75184f98ea24fb), Continuation 110 (blob SHA 13eab75efb08b133c36fe8cd4dcfc989df7832f4). PASS work skipped.
- Fresh official NBS Serbian/English Bulletin archives confirm July 2026 issue; extracted HTML exposes only archive Select/Input/Show controls. Direct July PDF fetch again times out; exact indexed search returns no Table 2.3 header. BOP page lists September current XLS, no direct July dataset.
- July 3,932 text fragment from C107 remains month-unattributed; July header/May legs NOT_VERIFIED; cross-vintage revision NOT_DONE. September May values -25 / +3,932 / -3,957 EURm remain exact PASS from C109.
- Report: docs/GCR_SERBIA_SRB_JULY_BULLETIN_RETRIEVAL_ROUTE_EXHAUSTION_AND_NEXT_GATE_CONTINUATION111_20261121.md; create commit fe431027dfeefe41092fae5d4418c4c1fa158b27.
- Next: requires real browser DOM inspection, form Show action and byte-preserving binary capture. No guessed parameters or gated service application. If unavailable, retain gate BLOCKED and pivot to another unfinished task.
- ₹0; protected invariants unchanged; UNKNOWN is never PASS.


## Continuation 112 — Tajikistan TJK official NBT Q2-2026 publication source gate (2026-11-21)
- Preflight re-fetched Master Ledger (blob SHA 8ff41c04dc598dafbdde6dadcd35f2449f606b4a), GCR Queue (blob SHA 92ffaf39d65737d71feb54ece02ccd42cf254f91); Serbia July-vintage PDF route remains blocked, no duplicate retry. THA numeric legs 2/2 PASS but vintage unresolved.
- TJK is in immutable 63-country cohort; no dedicated national Q2-2026 dual-leg report found in repo search. No cohort rebuild/IMF query.
- NBT official BOP page states BOP compilation under BPM5/BPM6. Official external-sector publication archive exposes a 2026 “FOR THE 2 QUARTER” issue; exact PDF URL resolved but fetch timed out. No PDF bytes, contents or hash.
- IIP 9-month 2025 operations/revaluation table rejected as quarterly BOP flow source; IMF CR 26/001 annual staff estimates rejected as quarterly national source.
- Report: docs/GCR_TAJIKISTAN_TJK_Q2_2026_NBT_OFFICIAL_PUBLICATION_SOURCE_GATE_CONTINUATION112_20261121.md; create commit c5b47be1e1cb76e95c6bcbee98503e8054c5b8bf.
- TJK Q2 PDF content/bytes NOT_CAPTURED; separate Q2 asset/liability legs NOT_CAPTURED; sign/unit/vintage NOT_ESTABLISHED; comparison NOT_DONE; TJK NOT_VALIDATED / NOT PASS.
- Next: byte-preserving PDF retrieval, inspect Q2 vs H1 reporting basis and separate legs; then reconcile to archived IMF rows only after period/sign/unit/vintage alignment.
- ₹0; protected invariants unchanged; UNKNOWN is never PASS.


## Continuation 113 — Tajikistan NBT publication period-basis ambiguity (2026-11-21)
- Preflight re-fetched Master Ledger (blob SHA e7222e8e08233bb2f94decb543f7213a553465e8), GCR Queue (blob SHA 5ca1d0c7fbbc24e8686b9577ffe12c96d7f28195), Continuation 112 (blob SHA dbc7ff164bf05d54e7898365ff6f2359f6bed03d). Completed PASS work skipped.
- NBT official archive link label says “FOR THE 2 QUARTER”; resolved PDF filename “ПБ-нимсолаи 1 с.2026.pdf” denotes first half-year. PDF retrieval times out; internal period basis cannot be verified. Standalone Q2 vs H1 cumulative remains AMBIGUOUS.
- Standard representation page yields no extracted data table. No portfolio asset/liability legs, unit/sign/vintage captured. No H1-Q1 subtraction; IIP and annual estimates rejected as substitutes.
- Report: docs/GCR_TAJIKISTAN_TJK_Q2_2026_NBT_PUBLICATION_PERIOD_BASIS_AND_H1_Q2_AMBIGUITY_CONTINUATION113_20261121.md; create commit 85070d16f9998a480df516733eb1d66df417431a.
- TJK NOT_VALIDATED / NOT PASS. Next: retrieve PDF bytes, inspect internal period and legs; if H1, require same-vintage Q1 dual legs before derivation; otherwise mark unavailable and advance.
- ₹0; protected invariants unchanged; UNKNOWN is never PASS.


## Continuation 114 — Timor-Leste TLS official H1 portfolio source gate (2026-11-21)
- Preflight re-fetched Master Ledger (blob SHA 163b5cfc1653ba7362db3d7394a134876bb7989b), GCR Queue (blob SHA 24b73fabe206fa3e28bd15181c47d2ced9031cf4), and TJK C113 report (blob SHA f27988d966cc9dfb32a3b597ff5d5358f02584cd). GitHub search found no existing TLS Q2 dual-leg report; PASS work skipped.
- BCTL Mid-Year Economic Review reports H1 2026 portfolio investment -USD 524.9m and interprets it mainly as drawdown of external portfolio assets/Petroleum Fund assets. This is H1 aggregate/net component, not separate Q2 asset/liability legs.
- BCTL quarterly BOP schedule lists releases Q1 2025 through Q4 2025 only; Q2 2026 dual-leg release NOT_LOCATED via this route. IIP stock series rejected as BOP transaction substitute.
- Internal source discrepancy preserved: Executive Summary financial account -USD 705.9m vs detailed table/section -USD 702.9m. No silent reconciliation.
- Report: docs/GCR_TIMOR_LESTE_TLS_Q2_2026_BCTL_H1_PORTFOLIO_SOURCE_GATE_CONTINUATION114_20261121.md; create commit c9b29c63569df74cad17cd1ac1105a70dc3e0dca.
- TLS NOT_VALIDATED / NOT PASS; H1 portfolio component captured; Q2 separate legs NOT_CAPTURED; unit USDm for H1 component; Q2 period/sign/vintage and IMF comparison NOT_ESTABLISHED/NOT_DONE.
- Next: search official BCTL archive for Q2 standalone BOP or H1 separate legs; no H1-Q1 subtraction absent same-vintage Q1 dual legs; otherwise advance.
- ₹0; protected invariants unchanged; UNKNOWN is never PASS.


## Continuation 115 — Timor-Leste BCTL BOP archive staleness audit (2026-11-21)
- Preflight re-fetched Master Ledger (blob SHA d856df8391de33cfc973a6511d5cf7eab42d9b05), GCR Queue (blob SHA f02863bd301215904b945f2ec3fe49f768554c80), and TLS C114 report (blob SHA e698bf465389f925ea0440052775af124100148b).
- Official BCTL page labels “Balance Of Payments” PDF Aug 2026, but opened one-page PDF data headers end at I–IV 2016/p and 2016/P; unit thousand USD. Aug 2026 is not data vintage; no 2025/2026 observations.
- C114 H1 2026 portfolio net component -USD 524.9m remains aggregate, not separate Q2 asset/liability legs. No net-to-leg inference, IIP substitution, H1-Q1 subtraction or IMF query.
- Report: docs/GCR_TIMOR_LESTE_TLS_BCTL_BALANCE_OF_PAYMENTS_ARCHIVE_STALENESS_AUDIT_CONTINUATION115_20261121.md; create commit c226bf514c84b281dc36688938fdf6b65229ad78.
- TLS NOT_VALIDATED / NOT PASS. Next: inspect official Economic Statistics/BOP data and H1 review appendices for current dual legs; if unavailable, mark NOT_AVAILABLE and advance.
- ₹0; protected invariants unchanged; UNKNOWN is never PASS.


## Continuation 116 — Timor-Leste BCTL live BOP dashboard / Excel export route (2026-11-21)
- Preflight re-fetched Master Ledger (blob SHA 5b90932ad15477ba22f74d44b705095f9f29cce6), GCR Queue (blob SHA 86f1ca7b64a70d77ed94f342349faac7fef1d8d9), and TLS C115 report (blob SHA 9f243d8b564204e21002b9fe77dec301029f9c0f).
- Newly discovered official BCTL BOP page https://www.bancocentral.tl/stats/balance_pay/ embeds Power BI “BoP_V1” and exposes “+ Export Excel”. Exact export endpoint https://www.bancocentral.tl/stats/bopdoc/download/c81e728d9d4c2f636f067f89cc14862c/.
- XLSX MIME recognized; web tool cannot parse XLSX MIME and direct container download failed. No workbook bytes, sheet names, periods or SHA-256. Power BI extraction yields no data rows.
- H1 2026 portfolio component -USD 524.9m remains aggregate only; Q2 separate legs NOT_CAPTURED. Stale Aug-2026 archive PDF is through 2016 and rejected.
- Report: docs/GCR_TIMOR_LESTE_TLS_BCTL_LIVE_BOP_DASHBOARD_AND_EXCEL_EXPORT_ROUTE_AUDIT_CONTINUATION116_20261121.md; create commit 283427dd67f29be0d6622b492ae698b6ffe6be9d.
- TLS NOT_VALIDATED / NOT PASS. Next: actual browser export of XLSX/Power BI data; capture bytes/hash, inspect period and dual legs; compare archived IMF rows only after alignment. If blocked/no legs, advance.
- ₹0; protected invariants unchanged; UNKNOWN is never PASS.


## Continuation 117 — Timor-Leste BCTL live BOP series latest period and export vintage (2026-11-21)
- Preflight re-fetched Master Ledger (blob SHA d5c6ff4eaae89d0a57cb480ed0f149a28767fa6e), GCR Queue (blob SHA ffc0cefec854638081117e1904253891690f21d0), TLS C116 report (blob SHA 282807d8df8ffe3c91e96c14aa2f66f5f7234d69).
- Official BCTL live BOP chart (Thousand USD) exposes quarter rows Jan-Mar-2020 through Jan-Mar-2025 only; latest is Q1 2025. Numeric keys y/y2/y3 lack extracted legend; no mapping to portfolio legs.
- Export Excel resolves to filename BoP_2025Q3.xlsx; exact URL https://bancocentral.tl/uploads/portfolio/ficheiros/1764122263_8744_BoP_2025Q3.xlsx. Browser click redirected home; direct download failed. Workbook bytes/sheets/hash NOT_CAPTURED; Q3-2025 filename is not Q2-2026 evidence.
- BCTL methodology: BPM6 broadly, quarterly BOP, USD unit, portfolio asset transactions sourced from Petroleum Fund and commercial bank balance sheets, market valuation incl. accrued coupon, excludes non-transaction revaluation. No Q2-2026 dual legs in source.
- H1 2026 -USD 524.9m remains aggregate. TLS Q2 asset/liability legs NOT_CAPTURED; TLS NOT_VALIDATED / NOT PASS; IMF comparison NOT_DONE.
- Report: docs/GCR_TIMOR_LESTE_TLS_BCTL_BOP_LIVE_SERIES_LATEST_PERIOD_AND_EXPORT_VINTAGE_AUDIT_CONTINUATION117_20261121.md; create commit e2e55fcca37495e560397e06e004fed59a74d33c.
- Next: actual browser export/inspect Q3-2025 workbook; if no newer vintage, mark route stale and advance. No IMF query/cohort rebuild.
- ₹0; protected invariants unchanged; UNKNOWN is never PASS.


## Continuation 118 — Türkiye TUR TCMB September-2026 ZIP exact-endpoint access gate (2026-11-21)
- Preflight re-fetched Master Ledger (pre-task blob SHA 8f6c07a3367f03868dbd64b06d3b127e85584ba8), GCR priority queue (pre-task blob SHA f96b0285089875bf80a20119c87d9e57e4147af6), and existing TUR queue sections O/P. Existing Q2 monthly aggregation, August/September PDF cross-check and IMF exact rows were reused; no repeated work, IMF re-query or cohort rebuild.
- Official TCMB BOP statistics page resolves the September-2026 ZIP link to https://tcmb.gov.tr/wps/wcm/connect/08454646-62d8-4188-bfbe-1c8c01d83fc4/bop.zip?CACHEID=ROOTWORKSPACE-08454646-62d8-4188-bfbe-1c8c01d83fc4-q7jJcOm&MOD=AJPERES. Retrieval timed out; ZIP bytes, member list, workbook sheets, byte count, SHA-256 and revision metadata NOT_CAPTURED.
- New report: docs/GCR_TURKIYE_TUR_Q2_2026_TCMB_SEPTEMBER_ZIP_EXACT_ENDPOINT_ACCESS_GATE_CONTINUATION118_20261121.md; commit 45ca5bcebb0a28cce43458fc3f936e5db9ef3a2a.
- Existing comparison retained: Q2 assets USD 5,749m (matches IMF at published precision); liabilities USD 9,183m vs IMF USD 9,270m, residual +USD 87m. No revision explanation established. TUR remains PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Next: obtain ZIP through supported actual browser/Computer Use or byte-preserving official route; otherwise preserve TUR blocker and advance to next eligible fixed-cohort member after roster/prior-report preflight. Do not repeat the same timed-out web fetch. ₹0; no production changes; UNKNOWN is never PASS.


## Continuation 119 — Tanzania TZA Bank of Tanzania Q2-2026 portfolio source-boundary audit (2026-11-21)
- Preflight re-fetched Master Ledger (pre-task blob SHA 1fdd52f5f294e1cc7452b0c2cf6a2553a73f3bf8), GCR queue (pre-task blob SHA d12ab5030ba2b2105d37e089777976b84fe810be), and immutable 63-country cohort report (blob SHA 1f767e22095865c8e5f87c2cfca55d9104b91e3e). No prior TZA entry in current ledger and no dedicated TZA Q2-2026 national dual-leg report found in scoped repository search. TZA follows TUR in immutable cohort order. No IMF re-query or cohort rebuild.
- Official Bank of Tanzania Statistical Bulletin for quarter ending Sep-2026, Vol IV No.3, Table 6.1, “Quarterly Balance of Payments”, unit USDm, reports Q2-2026 (Jun-26 column) portfolio investment net = -14.0. Portfolio investment is a single net row; no separate portfolio asset or liability legs are exposed in this inspected table. Other-investment asset/liability rows are not transferable to portfolio investment.
- Report: docs/GCR_TANZANIA_TZA_Q2_2026_BOT_QUARTERLY_BOP_NET_ONLY_SOURCE_BOUNDARY_AUDIT_CONTINUATION119_20261121.md; commit 08e75278237bbd02628205825f00069b6cc0c440.
- TZA cohort membership PASS; official Q2 BOP source locator/table PASS; net line CAPTURED -USD14.0m; portfolio asset/liability legs NOT_SEPARATELY_PUBLISHED_IN_INSPECTED_TABLE; national dual-leg comparison NOT_DONE; TZA PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED. PDF raw bytes/hash NOT_CAPTURED.
- Next: inspect only a newly identified official BoT/NSDP detailed BOP route for explicit portfolio asset/liability legs; if none, preserve TZA net-only and advance to UKR after roster/prior-report preflight. No net-to-leg inference, IIP stock substitution, IMF re-query, cohort rebuild, or production changes. ₹0; UNKNOWN is never PASS.


## Continuation 120 — Ukraine UKR NBU Q2-2026 BOP latest-period / publication-boundary audit (2026-11-21)
- Preflight re-fetched Master Ledger (pre-task blob SHA 214cef9b9b7e1f892d0fa2bc427242a919105d59), GCR queue (pre-task blob SHA 245eab58e11ac11958f39e894d960f4ba0a1affa), and immutable cohort report (blob SHA 1f767e22095865c8e5f87c2cfca55d9104b91e3e). UKR is in the fixed 63-country roster. Scoped repo search found no dedicated prior UKR Q2-2026 national dual-leg report. No cohort rebuild or IMF re-query.
- Official NBU BPM6 quarterly analytical BOP PDF https://finliteracy.bank.gov.ua/files/ES/BOP_q_en.pdf says last updated 19-Dec-2025; quarterly headers end at Q3 2025, with cumulative I–III 2025. It structurally distinguishes portfolio assets and liabilities, but no Q2-2026 observations.
- Official NBU external-sector revision notice https://roundtable.bank.gov.ua/admin_uploads/article/Changes_ES.pdf last updated 23-Sep-2026 and describes BOP revisions through Q1 2026; it does not expose Q2-2026 portfolio legs. NBU methodology states quarterly BOP publication 75–80 days after quarter-end, but timetable is not proof of observed Q2 values.
- Report: docs/GCR_UKRAINE_UKR_Q2_2026_NBU_BOP_LATEST_PERIOD_AND_PUBLICATION_BOUNDARY_AUDIT_CONTINUATION120_20261121.md; commit 2c353947a40469e2d48631cf5ebe37892b0811ec.
- UKR cohort membership PASS; NBU BPM6 compiler/methodology PASS; current inspected quarterly publication latest Q3-2025; revision notice through Q1-2026; Q2-2026 national portfolio assets/liabilities/net NOT_CAPTURED; national dual-leg comparison NOT_DONE; UKR NOT_VALIDATED / NOT PASS; aggregate NOT_AUTHORIZED.
- Next: revisit only on a newly published official NBU Q2-2026 detailed BOP release or downloadable Excel/SDMX/API response explicitly exposing portfolio asset/liability legs; archive bytes/response + timestamp + size + SHA-256 before parsing. Otherwise advance to URY after preflight. ₹0; no IMF re-query/cohort rebuild, no stock-as-flow or inference; production invariants unchanged; UNKNOWN is never PASS.


## Continuation 121 — Uruguay URY BCU Q2-2026 portfolio dual-leg extraction and archived IMF comparison (2026-11-21)
- Preflight re-fetched Master Ledger (pre-task blob SHA 3a46c4dd898033f42269eea7d35d6ed88d9c6607), GCR queue (pre-task blob SHA 2122a932e6c14d32870988ce29530b1384f1fe35), and immutable 63-country cohort (blob SHA 1f767e22095865c8e5f87c2cfca55d9104b91e3e). URY follows UKR in fixed roster; no prior dedicated URY report found. No IMF re-query/cohort rebuild.
- Official BCU Q2-2026 BOP report, Table 9, explicitly splits portfolio investment by institutional sector. Sum public/private: asset leg -47+566=+519 USDm; liability leg -204+12=-192 USDm. BCU net +710 USDm; legs imply +711 USDm, +USD1m published-rounding difference. Narrative confirms increase in external assets USD519m and reduction in liabilities USD192m. All figures preliminary.
- Reused existing archived IMF normalized panel Git blob SHA 2a8db2878cac6323bbad74ffa4035dc70e5e6b98; no new IMF query. Exact URY 2026-Q2 rows: A_NFA_T raw OBS_VALUE 518514442.91881, SCALE=6, PRECISION=6, source hash 677054017f5d3ae5fdd0403d7341588ebf43ad8b54124ae1b616bf323229326e; L_NIL_T raw OBS_VALUE -191945243.218418, SCALE=6, PRECISION=6, source hash 713b7a3000712e2ffb07cd574d08d7e6f3c02a6b2573ce4b40d06e0458cd7bba. REF_AREA=URY, P_F, USD, Q, 2026-Q2, origin O.
- Derived comparison display OBS_VALUE/1,000,000 gives +518.5144429 USDm assets and -191.9452432 USDm liabilities. Residuals BCU−IMF: +0.4855571 USDm and -0.0547568 USDm; both within ±0.5 USDm. Derived net 710.4596861 USDm vs BCU 710; residual -0.4596861 USDm within ±0.5. Numeric dual-leg and net comparison PASS at published whole-million precision. Raw values/scale remain unchanged; this bounded derived display is not a universal multiplier for all 154 EMDEs.
- Same-vintage alignment and full scope/definition equivalence remain NOT_ESTABLISHED; raw BCU PDF byte archive/hash NOT_CAPTURED. URY numeric dual-leg comparison PASS; full national validation PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Report: docs/GCR_URUGUAY_URY_Q2_2026_BCU_IMF_PORTFOLIO_DUAL_LEG_RECONCILIATION_CONTINUATION121_20261121.md; final correction commit b2be36e37766f3799ed0cd46d736ddbcc62200a6.
- Next: inspect BCU/IMF metadata and revision history specifically for URY Q2 definition/scope/vintage alignment; archive raw BCU PDF bytes/hash before any revision comparison. No repeated extraction, no IMF re-query/cohort rebuild, no production changes. ₹0; UNKNOWN is never PASS.


---

## Daily Unified Top-5 Swing Watchlist — 2026-11-21

- Dated report: docs/DAILY_UNIFIED_TOP5_SWING_WATCHLIST_20261121.md
- Report commit: 602180faa94dcacfd5520e4c792f8af1bd7070c6
- Independently fetched report SHA-256: e92c3d73c8d7f9b9cd303be848fbf3f3fbe4a8d1d25cf18966cf2f03ae8d0eb3
- Latest prospective run inspected: #339 / run ID 44799560798; conclusion success; source commit 624be8f126f39bd6a146d732ec3f87edde964aec.
- Artifact ID 14660032260; size 50,543 bytes; independently computed ZIP SHA-256 23e74e7f9ef2e32bf5b6bbc5a931814c06fe065835b8bdda74f3c00dbdafd213, matching GitHub artifact digest.
- Run log confirms 200 FULL_BHAVCOPY_DELIVERY downloads with HTTP 200, newest date 20112026; 200 valid sessions; normalized dataset log 503,892 rows / 2,999 symbols / 200 dates. QA JSON reports PASS. Raw delivery bytes, raw manifest and per-file raw hashes are absent from retained artifact; candidate price extraction therefore remains BLOCKED.
- Latest selector cutoff 2026-11-20; 10 label-free picks, 8 unique symbols, all outside frozen production Top-30. No 20-Nov labels read from future; latest outcomes remain immature.
- Strict 30-matured-cutoff shadow audit independently recalculated from artifact CSV: CURRENT_WINNER_PROB +5 H+1 = 41/150 TP, 109 FP, 0.482% outside-Top-30 recall; +10 H+3 = 31/150, 119 FP, 0.572%; +20 H+5 = 20/150, 130 FP, 1.294%. 20,000 cutoff-cluster bootstrap resamples, seed 20261121; intervals and denominators are in the dated report. These are outside-Top-30 capture metrics, not full-market recall.
- Main 100-cutoff / 3,000-row V11.4 Top-30 metrics remain provisional because all_by_date recall denominator is not reconciled to the eligible-universe export; FP counts / confidence intervals UNKNOWN.
- Engine statuses: A PARTIAL (retrospective only); B UNKNOWN (no approved execution assumptions / replay); C UNKNOWN (no vintage-aligned macro-sector-stock-outcome join). No candidate qualified; 0 alerts released.
- Shadow union: NRL, V2RETAIL, SIGACHI, RSDFIN, KDDL, YATRA, KMCSHIL, HINDOILEXP. Four retained vs prior cutoff (NRL, KDDL, YATRA, HINDOILEXP); four new (V2RETAIL, SIGACHI, RSDFIN, KMCSHIL); three removed (ELITECON, LEENEE, ARYAMAN). This is selector turnover, not performance improvement.
- No new workflow dispatched; no production logic, Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A–E or IPO-PLX V2 changed. UNKNOWN remains not PASS.
- Run artifact internal SHA-256 values, limitations, official sources, candidate exclusions and next actions are recorded in the dated report.


### 2026-11-21 report correction — NRL security identity and KDDL catalyst wording

- Corrected dated report commit: 2bf04bbec060c144bd7f92b1de953d59cb582a0a
- Corrected report Git blob: b055c883801b936ce33d3ed2aceeda874956336b
- Corrected report SHA-256, independently recomputed after fetching the committed file: 652bc7717d6cd5206005ae49ff4e77329c4f39b86eeded4971fa0dfef5dab0dc
- NRL's 12-Nov-2026 Q2 outcome PDF prints ISIN INEQJMS01013, while an earlier NSE integrated filing prints INE0JM501013. This cross-source conflict is unresolved; NRL ISIN is now UNKNOWN, not verified. The 12-Nov PDF is retained as Q2 catalyst evidence only, not as a security crosswalk.
- KDDL's 13-Nov results/investor-presentation assertion was removed because this audit did not independently re-verify the corresponding filing. The report now states no fresh 20-Nov catalyst was independently verified.
- No candidate status changed: NRL and all other shadow picks remain excluded; qualified candidates remain 0. Production invariants remain unchanged.


## Continuation 122 — Uruguay URY BCU/IMF methodology, scope and vintage bridge (2026-11-21)
- Preflight re-fetched Master Ledger (pre-task blob SHA dc83f74028794dec67293ac21f31d713e121d3b6), GCR queue (pre-task blob SHA 6491dbf4af0059d783cf981e4106f7dd5e5bbb49), C121 report (blob SHA fe70fba8680b07994212b8f8c4a3bf0428683b95), IMF panel methodology report and independent evidence checkpoint. No repeated BCU Table 9 extraction, IMF query or cohort rebuild.
- Official BCU BOP/IIP methodology PDF (updated MBP6 6th edition, Dec-2020) was inspected. Section II.3.2: private nonfinancial portfolio flows/positions from EGESE; public-sector securities from BCU debt registers, market-valued/accrual basis; regulated financial institutions from SSF statements with transactions calculated from balance differences in original currency; pension-fund and external custody assets from SSF and market records, with quarterly financial-institution surveys and annual Stock Exchange survey. Scope/methodology framework now documented, but Q2-2026 respondent-level coverage not available.
- Current BCU SDDS page shows Q2/26 as latest BOP period and portfolio investment net USD710m; template lists portfolio investment unit USD millions and distinct P_123/L_123 fields. Static extraction did not resolve those placeholders to numeric values. BCU Q2 report itself explicitly marks figures preliminary and warns partial sums may differ due to rounding.
- Existing IMF broad source receipt reused, no re-query: A_NFA_T retrieved 2026-11-19T06:46:34.357106Z HTTP200 484,139 bytes SHA256 677054017f5d3ae5fdd0403d7341588ebf43ad8b54124ae1b616bf323229326e; L_NIL_T retrieved 2026-11-19T06:46:34.878465Z HTTP200 451,290 bytes SHA256 713b7a3000712e2ffb07cd574d08d7e6f3c02a6b2573ce4b40d06e0458cd7bba. Receipt file blob SHA 0dd4104c6e0765171a9e6fb5fd09608f93748e54. These are IMF retrieval times, not last-revision timestamps.
- IMF BOP/IIP metadata dashboard published 2026-11-18; static page exposes no URY country-specific metadata rows and interactive data not retrieved. BCU PDF byte-preserving download attempt failed; BCU raw bytes/size/SHA256 remain NOT_CAPTURED. Exact matched vintage/revision history remains NOT_ESTABLISHED.
- Report: docs/GCR_URUGUAY_URY_Q2_2026_BCU_IMF_METHODOLOGY_SCOPE_VINTAGE_BRIDGE_CONTINUATION122_20261121.md; commit c5b9daf0208e75d9610f34b0a1740f53edc62e7c.
- C121 numeric comparison remains PASS at published precision; BCU methodology/source mapping and SDDS period/unit corroboration documented; full URY remains PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED. Next: pursue byte-preserving BCU PDF and country-specific IMF vintage export only if supported; otherwise preserve vintage blocker and advance cohort. ₹0; no production changes; UNKNOWN is never PASS.


## Continuation 123 — Uzbekistan UZB CBU Q2-2026 portfolio dual-leg / archived IMF comparison (2026-11-21)
- Preflight re-fetched Master Ledger (pre-task blob SHA 26dd48d4660851a15f97c9aa2986fd21e50846f3), GCR queue (pre-task blob SHA 75aefdf595a1ef60b0535963a5cddc876b10d7e5), and immutable 63-country cohort. UZB follows URY in fixed order. Scoped repository searches found no prior dedicated UZB Q2-2026 national dual-leg report. No IMF re-query or cohort rebuild.
- Official CBU quarterly BOP dataset https://cbu.uz/en/statistics/e-gdds/data/127982/ update date 29-Sep-2026 11:21; header covers 2005-Q1 through 2026-Q2; separate rows “Portfolio investment: assets” and “Portfolio investment: liabilities”; preview unit note “million USD, end of period”. Q2 values captured from final period column: assets USD0.01m; liabilities USD1,960.49m. Underlying XLSX bytes/hash NOT_CAPTURED.
- CBU official GDDS-DQAF BOP metadata says compiler uses IMF BPM6; all known international transactions/no known coverage exceptions; accrual basis with adjustments; quarterly compilation/publication; BOP can be revised each quarter when new information is available and revisions are identified in publications. Current data-page revision note specifically identifies revisions to services/current-account items through Q1-2026, not portfolio series.
- Reused archived IMF normalized panel Git blob SHA 2a8db2878cac6323bbad74ffa4035dc70e5e6b98; exact UZB Q2 rows: A_NFA_T raw 9793.61706018728 SCALE=6; L_NIL_T raw 1960492267.78624 SCALE=6. Source CSV SHA256s 677054017f5d3ae5fdd0403d7341588ebf43ad8b54124ae1b616bf323229326e and 713b7a3000712e2ffb07cd574d08d7e6f3c02a6b2573ce4b40d06e0458cd7bba. No new IMF query.
- Bounded derived display OBS_VALUE/1e6: assets USD0.009793617m; liabilities USD1,960.492267786m. Residuals CBU−IMF +0.000206383m and -0.002267786m, both within ±0.005m (half of BCU 0.01m displayed precision). Numeric dual-leg comparison PASS at displayed precision; raw values and SCALE unchanged.
- Caveat: BCU page literal unit note “million USD, end of period” needs workbook-level interpretation for BOP financial-account flow rows. BCU update date 29-Sep-2026 vs IMF raw panel retrieval 19-Nov-2026 are not matched vintages. Full UZB validation PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Report: docs/GCR_UZBEKISTAN_UZB_Q2_2026_CBU_IMF_PORTFOLIO_DUAL_LEG_RECONCILIATION_CONTINUATION123_20261121.md; commit bbce4b2aeefb6786eb706d8a32dd9f38c4fd12eb.
- Next: obtain actual BCU XLSX bytes via byte-preserving supported route, record URL/time/size/SHA-256 and inspect unit/time-basis headers; verify current vintage/revision. If still unavailable, keep UZB PARTIAL and advance to VNM after roster/prior-report preflight. ₹0; no production changes; UNKNOWN is never PASS.


## Continuation 124 — Vietnam VNM Q2-2026 official quarterly portfolio source closure (2026-11-21)
- Preflight re-fetched Master Ledger (blob SHA 7300a17c3ff68fdd3b78b9cf63b5832a03c0a339), GCR queue (blob SHA 934ddf803e3561754dc7b256f7f993e926e66f20), fixed 63-country cohort (blob SHA 1f767e22095865c8e5f87c2cfca55d9104b91e3e), and prior VNM boundary audit C59 (blob SHA 37c035bd784df75069ad77360a776e7040f0e26d). Executed C59's explicit next action: search for distinct official SBV quarterly Q2-2026 BOP portfolio dual-leg publication/API/export.
- No qualifying Q2-2026 national portfolio asset/liability observations located. SBV Annual Report 2023 Appendix 4 has separate annual asset/liability/net lines through 2023; 2021 report covers 2020-21. NSO Q2/H1 and Q3/9M 2026 reports were inspected; they contain FDI, investment, securities-market and trade aggregates but no separate BOP portfolio legs.
- IMF e-GDDS DQAF BOP metadata search-indexed text says no data currently available on portfolio assets/liabilities; static page does not expose metadata update date, so corroborative/possibly legacy only, not definitive current 2026 status.
- No Q2 raw national file/hash because qualifying source not located. No annual-to-quarter allocation, no FDI/securities proxy, no sign transform, no IMF re-query or cohort rebuild.
- VNM remains PARTIAL / NOT PASS; numeric dual-leg NOT_DONE; aggregate NOT_AUTHORIZED.
- Report: docs/GCR_VIETNAM_VNM_Q2_2026_SBV_OFFICIAL_QUARTERLY_SOURCE_CLOSURE_CONTINUATION124_20261121.md; commit 4e56a8919fb4478997dd624c8c0605df4bd70db8.
- Next fixed-cohort member after VNM is WSM (Samoa); preflight its prior report/source coverage before any extraction. Reopen VNM only on new official Q2 dual-leg source/revision. ₹0; production unchanged; UNKNOWN is never PASS.


## Continuation 125 — Samoa WSM CBS Q2-2026 BOP portfolio source-boundary audit (2026-11-21)
- Preflight re-fetched Master Ledger (blob SHA 102208e5e1d8cf5f127484479eef0089e008d59e), GCR queue (blob SHA 967b4e7d968811c6e9d6d9d117ba285897750b6b), immutable 63-country cohort (blob SHA 1f767e22095865c8e5f87c2cfca55d9104b91e3e); WSM follows VNM. Scoped repo search found no dedicated prior WSM Q2-2026 national report.
- Official CBS Quarterly Bulletin index states quarterly releases cover quarter-end data and are published with a three-month delay; latest listed June 2026 bulletin. June 2026 Bulletin Table B-1 (Balance of Payments), Tala million, contains distinct Portfolio Investment net/assets/liabilities and BPM6 note. But contents/narrative identify it as covering first quarter/March 2026; table period columns extend only to 2026-I. Bulletin issue month is not the reporting quarter.
- Therefore official quarterly source family PASS, separate labels PASS, BPM6 PASS; Q2-2026 national asset/liability NOT_CAPTURED; numeric comparison NOT_DONE; WSM PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED. Annual forecasts, IMF Article IV projections, and IIP stocks explicitly rejected as substitutes.
- Report: docs/GCR_SAMOA_WSM_Q2_2026_CBS_QUARTERLY_BOP_SOURCE_BOUNDARY_AUDIT_CONTINUATION125_20261121.md; commit 92260e1155d537f6fe2f2cdc2d35fb50a35d79c9.
- Next: do not repeat June bulletin. Locate next CBS bulletin that actually covers June 2026 (Q2), then archive raw bytes/URL/time/size/SHA256 and extract separate Q2-II portfolio legs; compare to existing IMF archive without new query. If not published, retain WSM PARTIAL and advance cohort after preflight. ₹0; no production changes; UNKNOWN is never PASS.


## Continuation 126 — Samoa WSM Q2-2026 CBS release-status recheck (2026-11-21)
- Re-fetched current Master Ledger (blob SHA f4274f9aae19a7dfdc74f64726377c10abd5f6df), GCR queue (blob SHA df6deb6441940b6165469ed1f58a271caf222092), immutable cohort report (blob SHA 1f767e22095865c8e5f87c2cfca55d9104b91e3e), and prior WSM Continuation 125 report (blob SHA 997ac798c8d5b86b7960ddcc37e825ac5b96a3d1).
- Direct CBS official Quarterly Bulletin index lists June 2026 as latest and footer says last updated 18 Aug 2026; September 2026 not listed. A search-engine snippet suggested September 2026, but direct official index contradicts it; snippet treated as stale/unverified, not release evidence.
- June-2026 PDF cover/title says June 2026, but contents and overview identify March 2026 / Q1. Table B-1 (PDF page 37; printed page 34) has Portfolio Investment net/assets/liabilities, Tala million, BPM6 note; latest quarter column 2026-I only. No Q2-II values.
- WSM Q2 assets/liabilities NOT_CAPTURED; numeric comparison NOT_DONE; WSM PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED. No raw Q2 file/hash because no qualifying Q2 bulletin is listed.
- Report: docs/GCR_SAMOA_WSM_Q2_2026_CBS_RELEASE_STATUS_RECHECK_CONTINUATION126_20261121.md; commit 0b7d5d9bd57def55020f8b4139f7445605a57d6f.
- Next fixed cohort member after WSM is ZAF (South Africa), subject to preflight of current ledger/queue and any prior ZAF report/source mapping. Recheck CBS only when a later issue is officially listed. ₹0; production unchanged; UNKNOWN is never PASS.


## Continuation 127 — ZAF Q2-2026 FX conversion methodology boundary (2026-11-21)
- Re-fetched current Master Ledger (blob SHA c2b4bf75acad32a2999a9baae3102716b7cef9f2), Priority Queue (blob SHA bf720dc4590c1b781e2abe2ac706494eed295f93), fixed 63-country cohort (blob SHA 1f767e22095865c8e5f87c2cfca55d9104b91e3e), and ZAF Parts 3/4 plus 20-Nov numeric report.
- Reused ZAF IMF exact rows and SARB Table KB502; no IMF query, no SARB re-extraction, no cohort rebuild. Prior liabilities comparison remains PASS at prior stated precision; assets residual remains REVIEW (0.056053395 USDm > 0.0304 USDm bound).
- New methodological finding: IMF BPM6 §§3.104–3.106 and draft BPM7 §§4.258–4.259 prefer transaction-date rates or shortest-period averages; quarter-average FX is not established as SARB's own conversion method for this flow aggregate. IMF ZAF BOP DQAF page returned only a generic shell, not usable country-specific conversion metadata. SARB narrative confirms net outflow direction only.
- Exact quarter-average conversion equivalence NOT_ESTABLISHED; ZAF full dual-leg remains PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED. No tolerance widening or forced PASS.
- Report: docs/GCR_ZAF_Q2_2026_FX_CONVERSION_METHODOLOGY_BOUNDARY_CONTINUATION127_20261121.md (commit b008571b86b3ebe8855b1c7170ee64a722e20f50).
- Next rank-1 task: continue CHN (China) detailed SAFE Q2-2026 BOP XLSX byte retrieval and workbook inspection; previous audit says official file locator found but bytes unavailable. Do not repeat ZAF or IMF capture. ₹0; production unchanged; UNKNOWN is never PASS.


## Continuation 128 — Fixed 10-country batch selected and sequential work started (2026-11-21)
- User requested batch selection of 10/15/20 countries and sequential execution without repeated user direction. Adopted a fixed 10-country batch for this cycle; each country is worked in order, and blocked routes are recorded once before advancing.
- Preflight re-fetched current Master Ledger, Priority Queue, fixed 63-country cohort and all ten prior country reports. PASS work excluded; no cohort rebuild or IMF re-query.
- Batch order: CHN, COL, POL, TUR, PER, ROU, NPL, RWA, SLV, SLB. Exact next action for each is recorded in the batch report.
- CHN: reopened official SAFE detailed time-series page and followed its XLSX link via a distinct browser link route; fetch returned 400 unsupported XLSX content type. No bytes/hash obtained; CHN remains PARTIAL / BLOCKED.
- COL: official BanRep SUAMECA multiple-download catalogue search exposes separate quarterly portfolio net acquisition of financial assets and net incurrence of liabilities series through 2026-Q2, in current USD millions, update date 2026-09-01. Opening the multiple-download route returned 502; no exact series IDs/export bytes/values/hash. COL remains PARTIAL / BLOCKED; no IIP stock substitution.
- Report: docs/GCR_Q2_2026_NATIONAL_DUAL_LEG_VALIDATION_BATCH10_CONTINUATION128_20261121.md (commit 5a1952a9b3b89db59e4d9dbdc53760aa509aab02).
- Continue batch sequentially with POL next; preserve no-repeat rule, ₹0, production invariants and UNKNOWN never PASS.


## Continuation 129 — Batch 1 sequential progress through ROU (2026-11-21)
- Re-fetched current Master Ledger, Priority Queue, Batch 1 report and relevant POL/TUR/PER/ROU reports before continuing.
- POL: official NBP bop_q.xlsx direct browser route returned 400 unsupported XLSX; separate container download failed. No bytes/hash; POL remains BLOCKED. No more same-route retries.
- TUR: official TCMB bop.zip direct browser route inaccessible; no bytes/hash. Existing PDF numeric status retained: asset displayed PASS; liability residual +87 USDm REVIEW; overall PARTIAL.
- PER: official BCRPData catalogue/result pages re-opened. Q2-2026 USDm: private portfolio assets +1,749; private liabilities +279; public liabilities +1,421. National liabilities total 1,700 vs IMF 1,699.664071 (residual +0.335929, within ±0.5) numeric PASS. Public portfolio-asset subseries absent from full listed public-sector catalogue; full asset coverage PARTIAL; no aggregate substitution. Raw API payload/hash NOT_CAPTURED.
- ROU: official BNR methodology reconfirms portfolio investment compiled title-by-title monthly at market value/accrual; BOP/IIP stocks distinguished. Official Q2 transaction legs/raw file not captured; PARTIAL / NOT PASS.
- Batch 1 report updated: docs/GCR_Q2_2026_NATIONAL_DUAL_LEG_VALIDATION_BATCH10_CONTINUATION128_20261121.md (update commit d255c5bbeb286087a9a9ff185162f6372bcbe7ff).
- Next country: NPL. Use a genuinely different supported NRB API/export route; no repeat of known unsupported XLSX or monthly archive route. Then RWA, SLV, SLB.
- No IMF re-query, no cohort rebuild, no aggregation or production changes. ₹0; UNKNOWN is never PASS.


## Continuation 130 — NPL closed at source-route boundary; RWA rechecked (2026-11-21)
- Preflight re-fetched current Master Ledger, Priority Queue, immutable 63-country cohort, Batch-1 report and NPL/RWA country reports. Batch order preserved.
- NPL: official NRB External Sector BPM6 workbook locator reconfirmed; direct XLSX MIME route fails. Distinct NSDP route tested: BOP Browse Data resolves to a general macro-report archive, while SDMX download is stale 2024-Q1 XML. No alternate current Q2 dataset/API route found; NPL separate national portfolio assets/liabilities NOT_EXTRACTED, PARTIAL/BLOCKED. Same routes must not be retried without a changed source surface.
- RWA: official BNR portal search-indexed record lists 30-Jun-2026 Balance of Payment, BPM6; portal direct open is JS-only and exact document URL unresolved. August-2026 BNR summary table omits portfolio legs and is Q1 scope; H1 net-only +14 USDm and annual FY legs remain non-Q2 evidence. RWA remains PARTIAL/NOT PASS.
- Batch report updated with both country outcomes. Next batch action: resolve BNR June-30 portal item via a genuinely supported document/API route; if unavailable, advance to SLV. No IMF re-query/cohort rebuild; ₹0; production unchanged; UNKNOWN is never PASS.


## Continuation 131 — SLV BCR publication-calendar audit (2026-11-21)
- Re-fetched latest Master Ledger, Priority Queue, immutable cohort, Batch-1 report and SLV country report; prior PASS work skipped.
- New official BCR Revista Trimestral Abril–Junio 2026 located. Publication calendar schedules Q2-2026 Balance of Payments for 30-Sep-2026, but this is a scheduled release date only. Table II.2 in the PDF still contains 2025Q3, 2025Q4 and 2026Q1; Q1 portfolio assets +282.76 USDm and liabilities -56.61 USDm are not Q2 evidence.
- BCR SDDS current Quarterly BOP Data Base link cdr=130 timed out. NSDP is stale (2022-12-23). No Q2 national portfolio legs/raw file/hash/vintage retrieved. SLV remains PARTIAL/BLOCKED; no inference from absent search snippets.
- Next fixed-batch item SLB. No IMF re-query/cohort rebuild; ₹0; no production changes; UNKNOWN is never PASS.


## Continuation 132 — SLB CBSI sign semantics and archived IMF row extraction (2026-11-21)
- Preflight re-fetched current Master Ledger, Priority Queue, immutable 63-country cohort, Batch-1 report and SLB Continuation 99. PASS work skipped; SLB was next unresolved fixed-batch member.
- CBSI June-2026 Table 1.17 gives Q2 portfolio assets +38 SBDm and liabilities nil; Chapter IV calls portfolio investment deficit 38. Reconciled conceptually without sign flip: BPM6 positive asset acquisition is an increase and financial-account net lending is assets minus liabilities; narrative deficit can express the opposite net-inflow perspective. CBSI does not explicitly define this narrative term.
- Extracted exact Q2 SLB rows from archived IMF raw CSVs (no IMF re-query): asset OBS_VALUE 4675384.136569459, SCALE=6; liability OBS_VALUE 0, SCALE=6. Raw file blob SHAs: asset 15449e87c9057291a1f52f2f8cd9805df55f9fb8, liability 15f379dc42e2760eb5f2384618e48f5ddc3177f1.
- Candidate arithmetic only: 38 SBDm / published Q2 average 8.08 SBD/USD = 4.702970297 USDm; IMF asset /1e6 candidate = 4.675384137 USDm; residual -0.027586160 USDm within CBSI rounding bound ±0.061881188 USDm. IMF liability zero matches CBSI nil. However /1e6 conversion not validated specifically for SLB, and CBSI has not explicitly confirmed 8.08 is BOP transaction conversion rate. Keep numeric status REVIEW; do not PASS.
- CBSI source PDF bytes/SHA not captured. SLB PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED. Next: explicit CBSI FX conversion method; otherwise close and advance to next cohort member. ₹0; production unchanged; UNKNOWN never PASS.


## Continuation 133 — TJK/TLS/TZA closure and UKR source breakthrough (2026-11-21)
- Preflight re-fetched latest Master Ledger, Priority Queue, immutable 63-country cohort, TJK C113, TLS C117 and TZA C119. PASS work excluded; no IMF re-query/cohort rebuild.
- TJK: official NBT archive label “FOR THE 2 QUARTER” conflicts with filename “нимсолаи 1” (H1). PDF remains inaccessible; no same-vintage Q1 dual legs. H1−Q1 not permitted. TJK Q2 legs NOT_CAPTURED / period AMBIGUOUS; closed route and advanced.
- TLS: BCTL live BOP chart ends Q1-2025, export filename BoP_2025Q3.xlsx; H1-2026 report is net-only; archive PDF labelled Aug-2026 contains data only through 2016. Q2-2026 separate legs NOT_CAPTURED; public route stale / NOT_AVAILABLE in inspected evidence.
- TZA: fresh official BoT search reconfirmed Q2-2026 portfolio net -USD14.0m only. Separate portfolio asset/liability legs not published in inspected Table 6.1; old BoT “Balance of Payments in USD” download entry dates 2020. No back-solving; TZA remains PARTIAL/NOT PASS.
- UKR selected per TZA C119 next-action sequence. New official NBU Q2-2026 IIP reconciliation provides explicit “changes due to transactions” column, distinct from stocks: portfolio assets +159 USDm, liabilities +34 USDm. Archived IMF raw Q2 UKR rows retrieved from existing panel: asset OBS_VALUE 159000000 SCALE=6; liability 34000000 SCALE=6. Country-specific OBS_VALUE/1e6 candidate = 159/34 USDm; both exact at NBU whole-million display precision, residual 0/0; transaction-component numerical cross-check PASS.
- Critical boundary: NBU source is the IIP transaction-reconciliation component, not the stale standalone BOP PDF (last update 18-Sep-2025). NBU IIP report last updated 23-Sep-2026; revision notice lists BOP revisions only through Q1-2026. Formal IIP transaction-to-BOP P_F source equivalence and same-vintage Q2 revision alignment remain NOT_ESTABLISHED. UKR remains PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Detail: docs/GCR_UKRAINE_UKR_Q2_2026_NBU_IIP_TRANSACTION_BRIDGE_AND_IMF_DUAL_LEG_CHECK_CONTINUATION134_20261121.md. No production changes; ₹0; UNKNOWN never PASS.

## Continuation 135 — UKR current BOP route and CHN SAFE attachment route rechecked (2026-11-21)
- Re-fetched current Master Ledger, Priority Queue, UKR C134, CHN detailed SAFE audit and immutable cohort before work; prior numeric PASS checks were not repeated.
- UKR: official NBU Q2-2026 IIP source remains current through 23-Sep-2026 and reports Q2 portfolio transaction changes assets +159 USDm, liabilities +34 USDm. However the accessible NBU BOP analytical files remain stale: p4 route says last updated 21-Mar-2025; finliteracy mirror says 19-Dec-2025 and table ends Q3-2025 / I-III 2025. NBU external-sector methodology says BOP quarterly publication and quarterly revisions; IIP separately published and can be revised for two years. Current Q2 BOP standalone data/API and matched revision vintage remain NOT_CAPTURED / NOT_ESTABLISHED. UKR PARTIAL / NOT PASS; no IMF query.
- CHN: official SAFE English detail page was reopened and its attachment followed. It resolves to the same XLSX URL already recorded; browser again returns unsupported XLSX MIME. Chinese/English page variants point to the same file; no workbook bytes, sheets or SHA-256. No new source evidence. CHN remains PARTIAL / NOT PASS; stop retrying identical endpoint.
- UKR and CHN detailed audit files updated; current Master Ledger and Priority Queue receive this continuation entry. No cohort rebuild, no IMF re-query, ₹0, no production changes; UNKNOWN never PASS.


## Continuation 138 — Hungary HUN Q2-2026 MNB separate portfolio legs and methodology gate (2026-11-21)
- Preflight reopened Master Continuity Ledger, GCR Master Priority Queue, fixed 63-country cohort, MEX C137 and existing archived IMF raw asset/liability panels. HUN is a fixed-cohort member with no dedicated national Q2 portfolio dual-leg report in the repository tree; no IMF re-query or cohort rebuild.
- Official MNB Statistics Portal Q2-2026 BOP/IIP release, published 25-Sep-2026, reports portfolio net assets -EUR6,277m, assets expanded +EUR2,104m and liabilities expanded +EUR8,380m in the “Net lending (FA) by instruments” section. These are separate financial-account flow legs, not IIP closing stocks. Rounded component arithmetic differs by EUR1m (2,104−8,380=-6,276 vs reported -6,277); retained as a rounding REVIEW, not forced.
- Official MNB BPM6 methodology (Sep-2024) establishes currency-by-currency monthly flows converted to HUF using MNB daily middle-rate monthly averages; quarterly flows sum monthly; EUR presentation derives from HUF via monthly-average HUF/EUR. March/September are longer 4-year revision windows; Q2 2026 publication revised BOP back to 2022. Portfolio transactions derive from security-position changes adjusted for price/FX effects; some household foreign-custody holdings are estimated.
- Reused existing archived IMF HUN Q2 rows without new query: A_NFA_T OBS_VALUE=2,434,272,117.820269 USD, SCALE=6; L_NIL_T=9,813,617,187.260281 USD, SCALE=6. Original values/attributes preserved.
- MNB national separate-leg source and methodology PASS; exact cross-currency reconciliation NOT_DONE because MNB's prescribed monthly conversion method cannot be reproduced by a simple quarterly EUR/USD average; item-level IMF equivalence and same-vintage bridge NOT_ESTABLISHED. HUN PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Detail: docs/GCR_HUNGARY_HUN_Q2_2026_MNB_IMF_PORTFOLIO_SOURCE_AND_METHOD_CROSSWALK_CONTINUATION138_20261121.md.
- Next: obtain MNB monthly BOP and exact monthly conversion series; reproduce the MNB method; verify item-level mapping and same-vintage. No IMF re-query/cohort rebuild. ₹0; no production changes; UNKNOWN never PASS.


## Continuation 139 — HUN monthly portfolio route closed; ALB Bank of Albania Q2 source gate opened (2026-11-21)
- HUN official MNB monthly-data route bounded: index lists HUF/EUR monthly BOP categories updated 13-Nov-2026, but the dedicated monthly publication page explicitly states only selected estimates are published for the open quarter and monthly time series are not published. No continuous monthly portfolio asset/liability rows for Apr–Jun 2026 are available on that route. HUN remains PARTIAL / NOT PASS; no monthly synthetic split or quarterly FX shortcut. HUN C138 report addendum records closure.
- Selected ALB from the existing immutable 63-country Q2 cohort after preflight; no dedicated ALB Q2 national portfolio report found. Official Bank of Albania Statistics Calendar schedules Q2-2026 BOP for 10-Sep-2026. Official quarterly BOP table, updated 10-Sep-2026, is in EUR millions and explicitly exposes portfolio asset parent C.2.A and liability parent C.2.L, each with equity and debt subcomponents.
- ALB national numeric Q2 rows and raw export were not captured; taxonomy/source route PASS only. No unsupported value inference. Reused archived IMF Q2 rows without new request: A_NFA_T OBS_VALUE=181700604.8387097 USD, SCALE=6; L_NIL_T=145011618.7096774 USD, SCALE=6. Numeric comparison NOT_DONE; sign/item mapping and same-vintage NOT_ESTABLISHED; ALB PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Detail: docs/GCR_ALBANIA_ALB_Q2_2026_BOA_BOP_PORTFOLIO_SOURCE_GATE_CONTINUATION139_20261121.md. HUN addendum is in docs/GCR_HUNGARY_HUN_Q2_2026_MNB_IMF_PORTFOLIO_SOURCE_AND_METHOD_CROSSWALK_CONTINUATION138_20261121.md.
- Next: capture Bank of Albania's official Q2 machine-readable BOP table export/raw bytes and exact C.2.A/C.2.L values; verify sign, aggregation, scale and vintage. No IMF re-query/cohort rebuild. ₹0; protected production invariants unchanged; UNKNOWN never PASS.


## Continuation 140 — ALB official BPM6 sign/methodology verified; exact interactive Q2 export remains unextracted (2026-11-21)
- Official Bank of Albania confirms BPM6 BOP compilation and distinguishes BOP transaction flows from IIP stocks. Official 2014 BPM6 transition commentary: financial-account increases in assets/liabilities positive, decreases negative; balance = assets minus liabilities. IMF GDDS/DQAF ALB BOP metadata: EURm publication, non-EUR transactions converted to ALL using monthly transaction-time rates, financial transactions accrual basis, revision policy fixed in methodological notes; detailed time-series downloadable in Excel and dynamic HTML copyable to Excel.
- Reopened official Bank of Albania Main data page cregtab_id=645: Q2 BOP dataset, quarterly, EURm, update 10-Sep-2026; C.2.A and C.2.L with equity/debt children confirmed. Current web retrieval surface returns index/interactive controls only, not selected observation cells or workbook bytes. This is a retrieval-channel boundary, not source absence. No numeric national values or SHA-256 claimed.
- ALB sign/methodology PASS; exact Q2 asset/liability values NOT_CAPTURED; raw export/hash NOT_CAPTURED; numeric comparison NOT_DONE; vintage NOT_ESTABLISHED; ALB PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED. Archived IMF exact rows retained; no new IMF request.
- Detail: docs/GCR_ALBANIA_ALB_Q2_2026_BOA_BOP_PORTFOLIO_SOURCE_GATE_CONTINUATION139_20261121.md (Continuation 140 addendum).
- Next: obtain official interactive Excel/HTML export through supported browser route; preserve raw bytes and SHA-256, extract parent/child portfolio legs, compare separately to archived IMF rows. If unavailable, retain PARTIAL and advance fixed cohort. No guessed API, IMF re-query or cohort rebuild. ₹0; no production changes; UNKNOWN never PASS.


## Continuation 141 — ALB Main-data period ceiling confirmed (2026-11-21)
- Reopened official Bank of Albania Main data page: quarterly, EURm, C.2.A/C.2.L taxonomy visible, but browser-readable period picker ends Q3-2025 and methodology note references 2017 vintage. It cannot serve as Q2-2026 numeric evidence. The statistics index separately advertises the quarterly BOP dataset updated 10-Sep-2026; that index does not expose selected Q2-2026 observations. Direct interactive detail URL retrieval also returned inaccessible. No guessed API/export request and no invented numeric data.
- Official 2014 BPM6 commentary confirms financial-account asset/liability increases positive, decreases negative; financial-account balance is asset change minus liability change; BOP flows published in EUR with average exchange rate for flows (end-period rate for stocks). Exact 2026 transaction FX and vintage bridge remain unestablished.
- ALB remains PARTIAL / NOT PASS; Q2 national legs NOT_CAPTURED, raw export/hash NOT_CAPTURED, dual-leg numeric comparison NOT_DONE, vintage NOT_ESTABLISHED; aggregate NOT_AUTHORIZED. Stop retrying this legacy Main-data view. Next: Q2-specific supported export or advance to another fixed-cohort member. No IMF re-query/cohort rebuild; ₹0; no production changes; UNKNOWN never PASS.


## Continuation 142 — Angola AGO Q2-2026 BNA source-family gate opened (2026-11-21)
- Reopened Master Ledger, Priority Queue and fixed 63-country cohort; AGO is an eligible fixed-cohort member and no dedicated AGO Q2-2026 national portfolio dual-leg validation report existed in repository inventory. Selected as a high-priority oil-exporting EMDE. No IMF re-query/cohort rebuild.
- BNA official portal identifies External Statistics and BOP/IIP report publication family, but current browser-readable SPA route exposes no extractable content or report bytes. BNA Q2-2026 External Statistics Information Note was publicly announced 4-Sep-2026; contemporaneous reporting quotes current-account surplus ~USD2.07–2.08bn and capital-and-financial-account deficit USD2,516.6m. These are broad account-level totals only, not portfolio asset/liability legs. IMF GDDS metadata describes historic annual BOP/IIP dissemination and quarterly bulletin mailing-list distribution; plausible access boundary, not proof of missing detailed data.
- Reused exact archived IMF rows: AGO A_NFA_T OBS_VALUE=23014088.470948 USD SCALE=6; L_NIL_T=1500000000 USD SCALE=6. Asset/liability raw panel blob SHAs remain 15449e87c9057291a1f52f2f8cd9805df55f9fb8 and 15f379dc42e2760eb5f2384618e48f5ddc3177f1. No conversion, netting, or IMF re-query.
- National Q2 portfolio legs/raw bytes/hash NOT_CAPTURED; taxonomy/sign/FX bridge NOT_ESTABLISHED; same-vintage NOT_ESTABLISHED; dual-leg reconciliation NOT_DONE; AGO PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED. Do not infer legs from the reported capital-and-financial-account net deficit.
- Detail: docs/GCR_ANGOLA_AGO_Q2_2026_BNA_EXTERNAL_STATISTICS_PORTFOLIO_SOURCE_GATE_CONTINUATION142_20261121.md.
- Next: obtain Q2 BNA note/report attachment or official quarterly-bulletin source via supported official route; preserve bytes/metadata/SHA-256; extract separate portfolio legs and verify sign/FX/scale/vintage. If unavailable, retain PARTIAL and advance. No repeated SPA retry, IMF re-query or cohort rebuild. ₹0; no production changes; UNKNOWN never PASS.

## Continuation 143 — Armenia ARM Q2-2026 CBA BOP XLS route identified; stock/flow boundary enforced (2026-11-21)
- Reopened Master Ledger, Priority Queue and immutable 63-country cohort; ARM is a cohort member with no dedicated ARM Q2-2026 national portfolio flow dual-leg report in repository inventory. No IMF re-query/cohort rebuild.
- Official CBA legacy External Sector Statistics page exposes direct BPM6 BOP workbook: https://old.cba.am/stat/stat_data_eng/BOP_eng_for_site_BPM6_rev.xls. Browser fetch failed with 400 Unsupported content-type application/vnd.ms-excel; direct container download also failed. Exact workbook bytes/sheets/hash not captured.
- CBA BOP metadata: USD millions, quarterly/annual, BPM6, residency/accrual/double-entry, annual revisions generally end-June. CBA methodology note records 2026 revisions to 2022–2025 goods/imports, insurance/freight, telecom/computer/information services and 2024–2025 compensation/personal transfers; no portfolio unchanged assumption.
- Armstat NSDP Q2/26 BOP flows (USDm) visible: current account -749.7; capital +13.2; financial account -421.4; direct investment -287.5; derivatives +2.6; other investment -235.0; reserves +357.0. Portfolio flow not shown in visible summary; this is not zero. Same page shows IIP END-OF-PERIOD portfolio asset stock 2,131.2 USDm and liability stock 2,526.7 USDm; strictly excluded from BOP flow test. IMF DSBB metadata confirms national BOP FA classification includes portfolio investments.
- Reused archived IMF exact rows: ARM A_NFA_T OBS_VALUE=-206248729.725102 USD SCALE=6; L_NIL_T=52279059.5905749 USD SCALE=6. Raw panel blob SHAs unchanged: 15449e87c9057291a1f52f2f8cd9805df55f9fb8 and 15f379dc42e2760eb5f2384618e48f5ddc3177f1.
- National portfolio flow legs NOT_CAPTURED; workbook bytes/hash NOT_CAPTURED; sign/scale/vintage bridge NOT_ESTABLISHED; numeric comparison NOT_DONE; ARM PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED. IIP stocks are not substitutes.
- Detail: docs/GCR_ARMENIA_ARM_Q2_2026_CBA_BOP_XLS_SOURCE_AND_STOCK_FLOW_BOUNDARY_CONTINUATION143_20261121.md.
- Next: recover exact official XLS via supported spreadsheet/browser or owner-side save, preserve raw bytes/hash, extract Q2 portfolio legs and verify vintage/sign/scale. If inaccessible, retain PARTIAL and advance. No repeated identical XLS fetch, IMF re-query, cohort rebuild; ₹0; no production changes; UNKNOWN never PASS.
## Continuation 144 — Kazakhstan KAZ Q2-2026 NBK portfolio dual-leg numeric reconciliation (2026-11-21)
- Reopened Master Ledger, Priority Queue and immutable 63-country cohort; KAZ is a cohort member and repo search found no dedicated KAZ Q2-2026 national dual-leg report. No IMF re-query/cohort rebuild.
- Official NBK Statistical Bulletin N09 (382), September 2026, table 1.3, pp.9–10, https://nationalbank.kz/file/download/138795, provides Q2-2026 portfolio legs in USDm: net acquisition of financial assets +1,545.1; net incurrence of liabilities +4,448.9.
- Reused archived IMF exact rows: A_NFA_T OBS_VALUE=1545080690.27593 USD SCALE=6; L_NIL_T=4448877446.24013 USD SCALE=6. Raw panel blob SHAs unchanged: 15449e87c9057291a1f52f2f8cd9805df55f9fb8 and 15f379dc42e2760eb5f2384618e48f5ddc3177f1.
- Expressing archived USD raw values in USDm using declared SCALE=6: assets 1,545.08069027593 vs NBK 1,545.1 (difference +0.01930972407); liabilities 4,448.87744624013 vs NBK 4,448.9 (difference +0.02255375987). Both PASS at national displayed precision 0.1 USDm. No sign inversion/netting.
- NBK published financial-account sign commentary: minus indicates inflow and plus outflow. National unit USDm and quarterly frequency supported by NBK/BNS metadata. Same-vintage remains NOT_ESTABLISHED: archived IMF 19-Nov panel vs NBK bulletin/revision history not bridged. PDF binary/hash NOT_CAPTURED.
- KAZ dual-leg numeric gate PASS at publication rounding; full vintage acceptance PARTIAL; aggregate NOT_AUTHORIZED. Do not claim same vintage or aggregate eligibility.
- Detail: docs/GCR_KAZAKHSTAN_KAZ_Q2_2026_NBK_PORTFOLIO_DUAL_LEG_NUMERIC_RECONCILIATION_CONTINUATION144_20261121.md.
- Next: archive NBK PDF bytes/hash and secure exact vintage bridge; retain dual-leg numeric PASS; then advance cohort. ₹0; no production changes; UNKNOWN never PASS.
## Continuation 145 — KAZ N09 publication-date and revision-window correction (2026-11-21)
- Correction to Continuation 144 wording: the cited NBK Statistical Bulletin N09 (382) is the issue labelled N09, but NBK's official bulletin index explicitly lists its publication date as 30-Oct-2026. The 30-Sep-2026 issue is N08. Do not call N09 the September 2026 bulletin. Official index: https://nationalbank.kz/en/news/statisticheskiy-byulleten/rubrics/2596.
- The official NBK Q2-2026 table values remain +1,545.1 USDm portfolio asset net acquisition and +4,448.9 USDm liability net incurrence; the linked official N09 table source remains https://nationalbank.kz/file/download/138795. Numeric comparison against archived 19-Nov IMF raw panel remains PASS at 0.1 USDm publication precision.
- Crucial vintage evidence: NBK BOP metadata states final quarterly data are published 90 days after quarter-end; earlier quarters are updated when final data are released; revisions occur twice yearly, in October and April, covering two years before the reporting year. Source: https://nationalbank.kz/en/news/metadannye/7253. Thus Q2-2026 falls inside the October revision window; N09 published 30-Oct is an October-vintage publication, not a September vintage.
- The IMF archive snapshot date is 19-Nov-2026, later than N09. However, no NBK revision ledger / exact release payload timestamp tied to the two portfolio rows and no IMF extraction-vintage metadata proving same synchronized vintage has been captured. Therefore same-vintage remains NOT_ESTABLISHED; do not infer same vintage merely from dates or rounded numeric equality.
- Official index distinguishes N09 (30-Oct-2026) from N08 (30-Sep-2026). Earlier text in Continuation 144 saying 'September 2026 Statistical Bulletin' is corrected by this addendum; the table values and separate-leg numeric calculations are unchanged.
- Current acceptance: national dual-leg numeric comparison PASS at 0.1 USDm; source issue date corrected to 30-Oct-2026; vintage alignment NOT_ESTABLISHED; PDF bytes/SHA256 NOT_CAPTURED; aggregate NOT_AUTHORIZED.
- Next: only promote vintage gate if an exact archived October NBK payload/revision history and IMF series-vintage provenance are obtained. Otherwise retain PARTIAL and advance to next eligible cohort member. No repeat numeric extraction, IMF re-query or cohort rebuild.
## Continuation 146 — Azerbaijan AZE Q2-2026 CBAR portfolio-only source scope gate (2026-11-21)
- Reopened Master Ledger, Priority Queue and immutable 63-country cohort. AZE is an eligible member; no dedicated Q2-2026 national portfolio-only dual-leg validation report found. No IMF re-query/cohort rebuild.
- Official CBAR Statistical Bulletin 09/2026, Table 1.4, USDm, QII 2026: https://uploads.cbar.az/assets/34f2e92e50d556d098dd5b36f.pdf. It publishes top-level net acquisition of financial assets and net incurrence of liabilities, but both subcategory rows combine 'portfolio and other investments'; no separate Q2 portfolio-only values are exposed. Combined category is not a valid portfolio-only proxy.
- CBAR 15-Sep-2026 H1 briefing as reported by APA gives six-month portfolio component figures (assets -USD0.3bn, liabilities -USD2.0bn). These are H1 cumulative, not Q2-only, and cannot substitute for Q2 or be differenced absent Q1 same-vintage portfolio-only rows.
- Reused archived IMF exact rows: AZE A_NFA_T OBS_VALUE=-333337000 USD SCALE=6; L_NIL_T=-8044000.0000001 USD SCALE=6. Raw panel blob SHAs unchanged: 15449e87c9057291a1f52f2f8cd9805df55f9fb8 and 15f379dc42e2760eb5f2384618e48f5ddc3177f1. No conversion, netting, residual inference or IMF re-query.
- National Q2 portfolio-only asset/liability legs NOT_CAPTURED; Q2 combined portfolio+other rows explicitly excluded; national sign/scale/vintage bridge NOT_ESTABLISHED; numeric comparison NOT_DONE; AZE PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Detail: docs/GCR_AZERBAIJAN_AZE_Q2_2026_CBAR_PORTFOLIO_SOURCE_SCOPE_GATE_CONTINUATION146_20261121.md.
- Next: obtain official detailed Q2 BOP annex/workbook with portfolio separated from other investment, preserve bytes/hash, compare two legs and vintage. If unavailable, retain PARTIAL and advance; do not derive Q2 from H1 or combined rows. ₹0; no production changes; UNKNOWN never PASS.
## Continuation 147 — Ecuador ECU Q2-2026 BCE portfolio dual-leg numeric reconciliation (2026-11-21)
- Reopened Master Priority Queue, Master Continuity Ledger and immutable 63-country Q2 cohort; ECU is eligible and no dedicated ECU Q2-2026 dual-leg report was found. No IMF re-query/cohort rebuild.
- Official BCE SDDS/NEDD English external-sector page, last updated 10-Nov-2026, publishes Q2/26 BOP USDm with separate portfolio rows: asset net acquisition -595.2; liability net incurrence +1,000.3. Page says unless otherwise indicated data are final and BOP/IIP follow IMF BPM6. BCE Q2 press release dated 1-Oct-2026 independently confirms portfolio assets decreased USD595.2m and total liabilities incurred USD1,519.3m.
- Reused archived IMF rows: ECU A_NFA_T OBS_VALUE=-595164167.96001 USD SCALE=6; L_NIL_T=1000348809 USD SCALE=6. Raw panel blob SHAs unchanged: 15449e87c9057291a1f52f2f8cd9805df55f9fb8 and 15f379dc42e2760eb5f2384618e48f5ddc3177f1.
- Declared SCALE=6 display conversion only: assets -595.16416796001 USDm vs BCE -595.2 (difference -0.03583203999); liabilities +1,000.348809 USDm vs BCE +1,000.3 (difference -0.048809). Both PASS at national 0.1 USDm precision; no sign inversion or netting.
- National separate-leg/period/unit/BPM6 scope PASS; archived IMF raw row provenance PASS. Same-vintage NOT_ESTABLISHED (BCE NEDD update 10-Nov; IMF archive 19-Nov but no exact synchronized release/extraction vintage). National raw HTML/PDF SHA256 NOT_CAPTURED. ECU numeric dual-leg gate PASS at publication precision; full acceptance PARTIAL; aggregate NOT_AUTHORIZED.
- Detail: docs/GCR_ECUADOR_ECU_Q2_2026_BCE_PORTFOLIO_DUAL_LEG_NUMERIC_RECONCILIATION_CONTINUATION147_20261121.md.
- Next: archive exact national page/report bytes and SHA256, obtain same-vintage metadata, then advance cohort. No repeated numeric extraction, IMF re-query or cohort rebuild. ₹0; no production changes; UNKNOWN never PASS.
## Continuation 148 — Costa Rica CRI Q2-2026 SECMCA/BCCR portfolio dual-leg numeric comparison (2026-11-21)
- Reopened Master Priority Queue, Master Continuity Ledger and fixed 63-country cohort; CRI is a cohort member and no dedicated CRI Q2-2026 portfolio dual-leg report found. No IMF re-query/cohort rebuild.
- SECMCA ESEA analytical BOP page for Costa Rica displays separate Q2-2026 portfolio investment asset and liability flows in USDm: assets +1,275.5; liabilities +1,167.5. Q2 is the second-quarter column (not H1). It further splits assets into equity/fund shares 998.7 and debt 276.7; liabilities into equity/fund shares 16.0 and debt 1,151.5. SECMCA describes BOP as transactions over a period and units USDm.
- BCCR NEDD page independently shows Q2/26 and DSBB standards/final-data statement, but its visible summary only gives total financial account -2,474.6 USDm; separate IIP portfolio rows are stocks and excluded from flow test. Thus detailed flow legs are from SECMCA regional statistical portal, not yet captured from BCCR primary export.
- Reused IMF raw rows: CRI A_NFA_T OBS_VALUE=1275459662.03478 USD SCALE=6; L_NIL_T=1167506330.15469 USD SCALE=6. Panel blob SHAs unchanged: 15449e87c9057291a1f52f2f8cd9805df55f9fb8 and 15f379dc42e2760eb5f2384618e48f5ddc3177f1.
- Display conversion only via SCALE=6: assets +1,275.45966203478 vs SECMCA +1,275.5 (difference +0.04033796522); liabilities +1,167.50633015469 vs SECMCA +1,167.5 (difference -0.00633015469). Both PASS at 0.1 USDm precision; no sign inversion/netting.
- National primary BCCR raw export/series IDs and SHA256 NOT_CAPTURED; exact same-vintage NOT_ESTABLISHED (SECMCA row-specific revision vintage and IMF extraction-vintage not linked). Numeric dual-leg gate PASS at portal precision; full acceptance PARTIAL; aggregate NOT_AUTHORIZED.
- Detail: docs/GCR_COSTA_RICA_CRI_Q2_2026_SECMCA_BCCR_PORTFOLIO_DUAL_LEG_NUMERIC_RECONCILIATION_CONTINUATION148_20261121.md.
- Next: capture SECMCA export and metadata, map to BCCR primary series, verify revision/vintage; then advance cohort. No repeated numeric extraction, IMF re-query or cohort rebuild. ₹0; no production changes; UNKNOWN never PASS.
## Continuation 149 — Dominican Republic DOM Q2-2026 BCRD quarterly BOP source gate (2026-11-21)
- Reopened Master Priority Queue, Master Continuity Ledger and fixed 63-country cohort; DOM is a member, no dedicated Q2-2026 national portfolio dual-leg report found. No IMF re-query/cohort rebuild.
- BCRD official Sector Externo page lists quarterly BPM6 BOP dataset 2010–2026 and direct XLSX: https://cdn.bancentral.gov.do/documents/estadisticas/sector-externo/documents/bpagos_trim_6.xlsx. Browser fetch failed with unsupported content-type application/octet-stream; direct download failed; workbook bytes/sheets/hash not captured.
- BCRD Informe Enero-Junio 2026 (Sept 2026), pp.41–42 / Anexo 3 pp.80–81 provides H1 cumulative portfolio legs: assets +305.2 USDm; liabilities +2,366.5 USDm. Explicitly not Q2-only. BCRD preliminary Jan-Sep 2026 report gives 9M cumulative legs: assets +136.3 USDm; liabilities +2,473.9 USDm. Explicitly not Q2-only. No H1/9M-to-Q2 inference or netting.
- H1 table's sign note: negative = Dominican net borrowing from rest of world; positive = net lending. Do not infer exact Q2 signs from cumulative rows.
- Reused IMF raw rows: DOM A_NFA_T OBS_VALUE=340200000 USD SCALE=6; L_NIL_T=-184000000 USD SCALE=6. Raw panel blob SHAs unchanged: 15449e87c9057291a1f52f2f8cd9805df55f9fb8 and 15f379dc42e2760eb5f2384618e48f5ddc3177f1. No transformation or IMF re-query.
- Q2 national portfolio asset/liability legs NOT_CAPTURED; H1/9M separate legs captured but wrong period; sign/scale/vintage bridge NOT_ESTABLISHED; numeric comparison NOT_DONE; DOM PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Detail: docs/GCR_DOMINICAN_REPUBLIC_DOM_Q2_2026_BCRD_QUARTERLY_BOP_XLS_SOURCE_GATE_CONTINUATION149_20261121.md.
- Next: recover exact BCRD quarterly XLSX, preserve bytes/hash and inspect Q2-only portfolio legs, then compare and establish vintage. If inaccessible, retain PARTIAL and advance. Do not repeat same unsupported fetch, use H1/9M as Q2, or infer residuals. ₹0; no production changes; UNKNOWN never PASS.
## Continuation 150 — Panama PAN Q2-2026 INEC MBP6 Excel access and period gate (2026-11-21)
- Reopened Master Priority Queue, Master Continuity Ledger and fixed 63-country cohort. PAN is a cohort member; no dedicated Q2-2026 national portfolio dual-leg report found. No IMF re-query/cohort rebuild.
- INEC official BOP publication dated 25-Sep-2026 is explicitly January–June 2026 (H1), uses BPM6 tables and public/private aggregate sector. Official page exposes MBP6 Table 1 Excel: https://www.inec.gob.pa/archivos/P0774740120260925095521Cuadro%201.%20Componentes%20Normalizados%20-%20MBP6.xlsx. Browser retrieval failed with 400 Unsupported content-type application/vnd.openxmlformats-officedocument.spreadsheetml.sheet; workbook bytes/sheets/hash not captured.
- Current INEC publication index lists the H1-2026 release and prior Q1-2026 release dated 26-Jun-2026, but no Q2-only 2026 BOP release. H1 must not be treated as Q2 or differenced with Q1 without exact same-vintage portfolio-only rows.
- Reused exact IMF rows: PAN A_NFA_T OBS_VALUE=3328699298.09 USD SCALE=6; L_NIL_T=450738775.03 USD SCALE=6. Raw panel blob SHAs unchanged: 15449e87c9057291a1f52f2f8cd9805df55f9fb8 and 15f379dc42e2760eb5f2384618e48f5ddc3177f1. No conversion, netting or IMF re-query.
- National Q2 portfolio legs NOT_CAPTURED; Q2-only publication NOT_ESTABLISHED; H1 substitute prohibited; national sign/scale/vintage bridge NOT_ESTABLISHED; numeric comparison NOT_DONE; PAN PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Detail: docs/GCR_PANAMA_PAN_Q2_2026_INEC_BOP_MB6_EXCEL_ACCESS_AND_PERIOD_GATE_CONTINUATION150_20261121.md.
- Next: recover official workbook and await/locate Q2-only release; preserve bytes/hash, extract separate Q2 legs, compare only after period and vintage proof. If absent, retain PARTIAL and advance. ₹0; no production changes; UNKNOWN never PASS.

## Continuation 151 — Colombia COL Q2-2026 BanRep quarterly source confirmation (2026-11-21)
- Reopened Master Ledger, Priority Queue, immutable 63-country cohort, prior COL source-boundary report and batch-10 queue. Reused archived IMF rows; no IMF re-query or cohort rebuild.
- New official BanRep Q2-2026 BOP/IIP report (published 1-Sep-2026) explicitly says Q2 net portfolio-instrument liquidations partially offset net capital inflows, but the accessible narrative does not publish separate numerical asset/liability transaction legs. End-June IIP portfolio positions are stocks and excluded.
- Official SUAMECA multiple-download catalogue independently lists separate quarterly portfolio asset net-acquisition and liability net-incurrence series, each in current USDm, from 31-Mar-2000 through 30-Jun-2026, last updated 1-Sep-2026. This confirms the correct official series families and Q2 coverage; exact series IDs and Q2 values were not exposed in the captured catalogue response.
- BanRep's official user guide confirms the multiple-download service is designed to select historical variables and generate tables; the documented export control is desktop-only. The previously tested direct portal page returned 502. No raw export, response bytes, retrieval timestamp, SHA-256, or exact vintage metadata captured.
- Detail: docs/GCR_COLOMBIA_COL_Q2_2026_BANREP_SUAMECA_OFFICIAL_QUARTERLY_SOURCE_CONFIRMATION_CONTINUATION151_20261121.md (commit c3ddbbbfedc47208aeee8460d59dabbc7e4e099d).
- Acceptance: cohort PASS; official separate series identity/quarterly frequency/USDm/Q2 coverage PASS; exact values/IDs/raw export/hash NOT_CAPTURED; sign/vintage NOT_ESTABLISHED; numeric comparison NOT_DONE; COL PARTIAL / BLOCKED, NOT PASS; aggregate NOT_AUTHORIZED.
- Next: use documented desktop SUAMECA export or a genuinely different supported official export route for both legs together; if inaccessible, stop repeating the same 502 route and advance. Do not use IIP stocks, narrative, or net flow as substitutes. ₹0; no production changes; UNKNOWN never PASS.


## Continuation 152 — Colombia COL SUAMECA desktop export execution boundary (2026-11-21)
- Reopened and preserved Continuation 151, current GCR Priority Queue, fixed 63-country cohort and COL source-boundary evidence. No IMF re-query, cohort rebuild or repeated 502 endpoint attempt.
- Reopened BanRep's official user guide. It documents the multiple-download workflow: add both separate quarterly portfolio series via cart controls; confirm with “Ver datos de series”; set the required period; review the data; use “Exportar a Excel”. The guide states the prebuilt-table right-click export is desktop-only; multiple-download is documented as a multi-series export function.
- The current official catalogue still indexes both portfolio asset net-acquisition and liability net-incurrence series, current USDm, quarterly, through 2026-Q2, disclosed 2026-09-01. Exact IDs/values remain unavailable from indexed content.
- This session has no interactive desktop portal control, so the documented desktop export was not executed. No exact series IDs, Q2 values, raw export bytes, retrieval timestamp, SHA-256 or observation-specific revision metadata captured. This is NOT_EXECUTED, not proof of data absence.
- Detail: docs/GCR_COLOMBIA_COL_Q2_2026_SUAMECA_DESKTOP_EXPORT_EXECUTION_BOUNDARY_CONTINUATION152_20261121.md (commit 6fec2421fbce817557dfa1090125e65e71c3351e).
- Acceptance: official procedure PASS; desktop execution NOT_EXECUTED; exact values/IDs/raw bytes/hash NOT_CAPTURED; sign/vintage NOT_ESTABLISHED; numeric comparison NOT_DONE; COL PARTIAL / BLOCKED, NOT PASS; 63-country aggregate NOT_AUTHORIZED.
- Next: obtain the two-series Q2-2026 export from the documented desktop portal and preserve the original file for hash/metadata/value extraction. No IIP stock, net-flow, qualitative narrative or other financial-account substitute. ₹0; no production changes; UNKNOWN never PASS.


## Continuation 153 — Cabo Verde CPV Q2-2026 BCV official BOP source gate (2026-11-21)
- Re-fetched current ledger (pre-task blob SHA 4e838cfff1695f84a1b4bb55cc340610f745090a), GCR priority queue (4b080ae1148bb8ce7d04700047d191583da86fa1) and immutable 63-country cohort (31f5bfe5adb59f4c1a139b6d8c54b5ad9fb672c8). CPV fixed-cohort membership and both IMF legs PRESENT; no dedicated CPV country report found. No IMF re-query/cohort rebuild.
- Official BCV BOP page (rendering date 17-Nov-2026) lists an XLS dataset covering 2012-Q1 through 2026-Q2. Exact XLS URL was followed through the web route (timeout) and separately attempted through direct byte download (failed). No workbook bytes/sheets/values/file hash/receipt captured; Q2 separate portfolio asset/liability exposure remains NOT_VERIFIED.
- Official BCV statistical bulletin Q1 PDF exposes a single net portfolio-investment line only; it is not Q2 and is not a substitute for separate legs. BCV external-sector overview describes quarterly BOP transactions and quarter-end IIP positions separately.
- IMF e-GDDS metadata says BPM5, CVE presentation, average monthly FX and quarterly revisions; BCV's March-2026 bulletin footnote says BOP compiled under BPM6. Treat this as a methodology-version conflict; e-GDDS update date not visible, so no current BPM version assumption admitted.
- Reused existing IMF raw CSV rows (no query): CPV A_NFA_T 2026-Q2 OBS_VALUE=364678.4706264281 USD, SCALE=6; L_NIL_T OBS_VALUE=0 USD, SCALE=6. Raw file Git blob SHAs unchanged: asset 15449e87c9057291a1f52f2f8cd9805df55f9fb8; liability 15f379dc42e2760eb5f2384618e48f5ddc3177f1. Raw values/SCALE preserved; no conversion/comparison. Git blob SHAs are not claimed as SHA-256.
- Acceptance: cohort + IMF row presence PASS; official BCV workbook locator/period coverage PASS; workbook bytes/dual-leg layout NOT_CAPTURED/NOT_VERIFIED; BPM5/BPM6 CONFLICT; sign/unit/vintage bridge NOT_ESTABLISHED; numeric comparison NOT_DONE; CPV PARTIAL/BLOCKED, NOT PASS; aggregate NOT_AUTHORIZED.
- Detail report: docs/GCR_CABO_VERDE_CPV_Q2_2026_BCV_OFFICIAL_BOP_SOURCE_GATE_CONTINUATION153_20261121.md (commit c5199494261675cc599bd5f82e3862ba9cf41c9d).
- Next: only use a genuinely different supported official BCV export route; inspect separate legs and dated current methodology, then compare each leg. No identical XLS retries, net-only/Q1 substitute, IIP stock, annual interpolation, IMF query or cohort rebuild. ₹0; no production changes; UNKNOWN never PASS.


## Continuation 154 — Georgia GEO Q2-2026 NBG official BOP source-boundary audit (2026-11-21)
- Re-fetched current ledger (pre-task blob SHA c6a953ff88dcae619023bfd11235a1e7936ad12a), GCR queue (0e5fb9304e5af696042aa1919f2f1fa49f651850), immutable 63-country cohort (31f5bfe5adb59f4c1a139b6d8c54b5ad9fb672c8) and CPV Continuation 153. GEO is in fixed cohort with both IMF panel legs present; no prior dedicated GEO Q2 national dual-leg report found. No IMF query or cohort rebuild.
- Official NBG “Balance of Payments of Georgia (II Quarter 2026)” release, 30-Sep-2026, confirms Q2 and explicitly states BPM5. Accessible release text does not publish separate Q2 portfolio-asset/liability transaction amounts. Official NBG NSDP labels separate “Portfolio investment: Assets” and “Portfolio investment: Liabilities” in USDm, but the visible data period is Q3/21, stale for Q2-2026. NBG BOP publication page says data are regularly revised and revisions may apply to any period.
- Official NBG Q2 IIP release reports quarter-end stock positions; excluded from BOP transaction-flow validation. No current Q2 separate-leg dataset/API response, national raw bytes, receipt, timestamp or SHA-256 captured.
- Reused archived IMF raw rows: GEO A_NFA_T OBS_VALUE=325871168.2 USD SCALE=6; L_NIL_T OBS_VALUE=416264206.49 USD SCALE=6. Existing raw panel blob SHAs 15449e87c9057291a1f52f2f8cd9805df55f9fb8 and 15f379dc42e2760eb5f2384618e48f5ddc3177f1. No conversion or numeric comparison.
- Acceptance: cohort/IMF row presence PASS; official Q2 BOP release and BPM5 statement PASS; separate Q2 national transaction legs NOT_CAPTURED; visible NSDP labels PASS for taxonomy only but period stale; item/sign/scale/vintage equivalence NOT_ESTABLISHED; national raw bytes/hash NOT_CAPTURED; numeric comparison NOT_DONE; GEO PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Detail: docs/GCR_GEORGIA_GEO_Q2_2026_NBG_OFFICIAL_BOP_SOURCE_BOUNDARY_AUDIT_CONTINUATION154_20261121.md (commit 3af8633ad131bf2aa95da82a48b4e4c8aff9c8f9).
- Next: investigate a genuinely different NBG current statistics export/API for Q2 separate portfolio transaction legs and dated revision metadata; do not retry same release page, use stale NSDP values or substitute IIP stocks. If unavailable, retain GEO PARTIAL and advance. ₹0; no production changes; UNKNOWN never PASS.


## Continuation 155 — Burundi BDI Q2-2026 BRB official BOP source-boundary audit (2026-11-21)
- Re-fetched current ledger, GCR Priority Queue and immutable 63-country cohort; BDI is a member with both archived IMF legs present. No prior dedicated BDI Q2-2026 national dual-leg report found; no IMF re-query or cohort rebuild.
- Official BRB Q4-2025 Monetary Policy Report (26-Feb-2026), Table 9, publishes separate portfolio legs in MBIF: Q4-2025 net portfolio investment -14,143.6; net acquisition of financial assets 0.0; net incurrence of liabilities 14,143.6. This is historical format evidence only, not Q2-2026. BRB “Autres Documents” index currently exposes Q4-2025 and Q3-2025 reports, no Q2-2026 BOP report in captured index.
- Reused exact IMF Q2 rows: BDI A_NFA_T OBS_VALUE=130723.2699945969 USD SCALE=6; L_NIL_T OBS_VALUE=0 USD SCALE=6. Existing raw panel blob SHAs remain 15449e87c9057291a1f52f2f8cd9805df55f9fb8 and 15f379dc42e2760eb5f2384618e48f5ddc3177f1. No conversion/comparison.
- BDI Q2 national separate legs/raw bytes/hash NOT_CAPTURED; national sign/unit/BPM/vintage bridge NOT_ESTABLISHED; numeric comparison NOT_DONE; BDI PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED. Detail: docs/GCR_BURUNDI_BDI_Q2_2026_BRB_OFFICIAL_BOP_SOURCE_BOUNDARY_AUDIT_CONTINUATION155_20261121.md (commit 1b969bca7d1956275eb046f766f7e596a9630e33).
- GEO addendum: NBG NSDP officially exposes BOP Browse Data / Download in SDMX links, but no exact SDMX URL or Q2 values/raw capture was obtained; rendered NSDP remains stale Q3/2021. A methodology conflict was found: NBG Q2-2026 release states BPM5, while NBG's official 2014 notice says BPM6 from Q1-2014 and BPM6 only since 2015. Resolve with Q2-specific metadata/correction before comparison. GEO remains PARTIAL.
- Next: continue rank-1 63-country validation with next eligible fixed-cohort member after duplicate-report/source-feasibility preflight. Revisit BDI only on a new official Q2-2026 dual-leg source. No IIP stock, annual projection, adjacent-quarter substitution, inferred sign/scale or net-to-leg back-solving. ₹0; production unchanged; UNKNOWN never PASS.


## Continuation 156 — Bosnia and Herzegovina BIH Q2-2026 CBBH official BOP source-boundary audit (2026-11-21)
- Re-fetched current Master Ledger, GCR Priority Queue and immutable 63-country cohort. BIH is a member with both archived IMF Q2 legs present; repository search found no prior dedicated BIH Q2 national dual-leg report. BGD was skipped because its net-only/annual-survey/NSDP access routes were already exhausted and documented.
- CBBH official Q2/2026 BOP release calendar deadline is 30-Sep-2026. Accessible CBBH Bulletin 2 2026 (data cutoff 18-Aug-2026) contains T15 through Q1 2026 only; T15 is KM million, BPM6 and has separate portfolio asset/liability rows. Q1 2026 portfolio net=-101 KMm, asset leg=-101 KMm, liability leg=0 KMm; Q1 values explicitly not used for Q2.
- CBBH portal guide documents anonymous/unregistered access and Excel/PDF export; the dynamic Panorama Necto portal endpoint was inaccessible via current browser. Q2 workboard/export NOT_EXECUTED; no Q2 values/raw bytes/receipt/hash captured. IMF e-GDDS metadata confirms quarterly CBBH BOP, KM million, revision practices and portal dissemination.
- Reused archived IMF rows: BIH A_NFA_T OBS_VALUE=61489941.04204912 USD SCALE=6; L_NIL_T OBS_VALUE=1324417089.731674 USD SCALE=6. Raw panel blobs unchanged (asset 15449e87c9057291a1f52f2f8cd9805df55f9fb8; liability 15f379dc42e2760eb5f2384618e48f5ddc3177f1). No conversion/comparison.
- BIH Q2 national legs NOT_CAPTURED; portal execution NOT_EXECUTED; observation-vintage and exact sign/scale bridge NOT_ESTABLISHED; numeric comparison NOT_DONE; BIH PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED. Detail: docs/GCR_BOSNIA_HERZEGOVINA_BIH_Q2_2026_CBBH_OFFICIAL_BOP_SOURCE_BOUNDARY_AUDIT_CONTINUATION156_20261121.md (commit 8eb7f082930f30d366ce3b8e0f8f5cf7448d7520).
- Next: execute documented anonymous portal Q2-2026 workboard/export only if a supported interactive route is available; otherwise mark NOT_EXECUTED and advance to next eligible fixed-cohort member. No Q1 substitution, IIP stock, IMF projection, BIS position, net-to-leg back-solving, IMF query/cohort rebuild or production changes. ₹0; UNKNOWN never PASS.


## Continuation 157 — Belize BLZ Q2-2026 CBB official BOP source-boundary audit (2026-11-21)
- Re-fetched Master Ledger, GCR Priority Queue and immutable 63-country cohort. BLZ is a fixed-cohort member with both archived IMF Q2 rows present; no dedicated prior BLZ national dual-leg report found. BIH portal export remained NOT_EXECUTED; BIH retained PARTIAL. No IMF query/cohort rebuild.
- Official Central Bank of Belize June-2026 Quarterly Review covers Q2/H1 2026 and states 2026 figures provisional. Table A.22 (page 51, $mn) separately lists Portfolio Investment Assets=0.0 and Liabilities=0.0 for Jan–June 2026; these are H1 cumulative, not Q2-only. Table A.21 also gives H1 net portfolio=0.0 but is not a dual-leg substitute. IIP Table A.31 is stock/reconciliation context, not Q2 flow.
- Official CBB BOP page links full Excel dataset. Exact XLSX URL fetch returned HTTP 400 unsupported MIME; no workbook bytes/sheets/Q2 rows/hash captured. IMF e-GDDS describes quarterly BOP and separate portfolio assets/liabilities source concepts.
- Reused IMF raw rows: BLZ A_NFA_T OBS_VALUE=142.2106890070215 USD SCALE=6; L_NIL_T OBS_VALUE=0 USD SCALE=6. Raw panel blob SHAs unchanged (15449e87c9057291a1f52f2f8cd9805df55f9fb8; 15f379dc42e2760eb5f2384618e48f5ddc3177f1). No conversion/comparison.
- BLZ Q2-only national legs NOT_CAPTURED; H1 dual legs available only as cumulative; XLSX bytes/hash NOT_CAPTURED; Q2 vintage/sign/scale bridge NOT_ESTABLISHED; BLZ PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED. Detail: docs/GCR_BELIZE_BLZ_Q2_2026_CBB_OFFICIAL_BOP_SOURCE_BOUNDARY_AUDIT_CONTINUATION157_20261121.md (commit 02c521f3599b795de7d1d948f9a9279d2ef857b1).
- Next: recover CBB official XLSX via supported raw-byte/export route; inspect exact 2026-Q2 rows only. If inaccessible, retain BLZ PARTIAL and advance. No H1-to-Q2 subtraction without same-vintage Q1 evidence, no IIP substitution, no inference from zero net. ₹0; production unchanged; UNKNOWN never PASS.


## Continuation 158 — Bolivia BOL Q2-2026 BCB official BOP source-boundary audit (2026-11-21)
- Re-fetched current Master Ledger, GCR Priority Queue and immutable 63-country Q2 both-legs cohort. BOL is a member with both archived IMF rows present; no prior dedicated BOL Q2-2026 national dual-leg report found. No IMF re-query or cohort rebuild.
- Official BCB VI Manual Q2-2026 page explicitly lists a Q2 “Balanza de Pagos” XLSX and a separate “Series de tiempo: Balanza de Pagos” XLSX. This is a stronger quarter-specific locator than the generic H1 report.
- Both exact official XLSX URLs were attempted. Web fetch returned HTTP 400 unsupported XLSX MIME; a separate direct byte-download attempt failed. No national workbook bytes/sheets/series IDs/Q2 values/receipt/SHA-256 captured. BCB's separate full report page currently lists H1-2026 dated 30-Sep-2026; H1 is not substituted for Q2.
- Reused exact IMF raw rows: BOL A_NFA_T OBS_VALUE=-154107393.924487 USD SCALE=6; L_NIL_T OBS_VALUE=974071938.904098 USD SCALE=6. Existing raw panel Git blob SHAs unchanged: 15449e87c9057291a1f52f2f8cd9805df55f9fb8 and 15f379dc42e2760eb5f2384618e48f5ddc3177f1. No conversion/comparison.
- Cohort and IMF row presence PASS; official Q2 workbook locators PASS; national values/bytes/dual-leg layout NOT_CAPTURED; Q2-specific BPM/sign/unit/scale/vintage bridge NOT_ESTABLISHED; numeric comparison NOT_DONE; BOL PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Detail: docs/GCR_BOLIVIA_BOL_Q2_2026_BCB_OFFICIAL_BOP_SOURCE_BOUNDARY_AUDIT_CONTINUATION158_20261121.md (commit 88a2d13a353f73a2af386fc1f31deaa4ab7879be).
- Next: use a genuinely supported official BCB raw-byte/export route for the two Q2 XLSX files; if inaccessible, retain PARTIAL and advance. No H1/annual/IIP/net substitute, no IMF re-query, no cohort rebuild. ₹0; production unchanged; UNKNOWN never PASS.


## Continuation 159 — Belarus BLR Q2-2026 NBRB official BOP source-boundary audit (2026-11-21; Chapter 47 Part 7)
- Re-fetched Master Ledger, GCR Priority Queue and immutable 63-country cohort; BLR is a member with both archived IMF Q2 rows present. No prior dedicated BLR Q2 national dual-leg report. Previous BLZ/BOL audits were not repeated; no IMF re-query/cohort rebuild.
- NBRB official metadata and methodology confirm BPM6, quarterly BOP, standard/analytic presentations, portfolio investment functional category, net asset acquisition and net liability incurrence separately, plus=net increase/minus=net decrease, USD/BYN, and preliminary/revision policy. Q2 live data page timed out/inaccessible; no Q2 national dual-leg values or source bytes retrieved.
- Reused exact IMF raw rows: BLR A_NFA_T OBS_VALUE=6414501.08999999 USD SCALE=6; L_NIL_T OBS_VALUE=-325487157.39 USD SCALE=6. Raw panel Git blob SHAs unchanged: 15449e87c9057291a1f52f2f8cd9805df55f9fb8 / 15f379dc42e2760eb5f2384618e48f5ddc3177f1. No conversion/comparison.
- National Q2 values/raw bytes/hash NOT_CAPTURED; Q2 vintage/item/sign/scale bridge NOT_ESTABLISHED; numeric comparison NOT_DONE; BLR PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED. Detail: docs/GCR_BELARUS_BLR_Q2_2026_NBRB_OFFICIAL_BOP_SOURCE_BOUNDARY_AUDIT_CONTINUATION159_20261121.md (create commit 47c7d96056c770943d12cd7040b5cf95d726f2d2).
- Next: supported NBRB Q2-2026 bulletin/data export raw-byte retrieval; otherwise retain PARTIAL and advance. No IIP/annual/adjacent-quarter/net-total substitution. ₹0; production unchanged; UNKNOWN never PASS.


## Continuation 160 — Chapter 47 Part 8: Belarus follow-up + Chile CHL Q2-2026 BCCh BDE monthly dual-leg source capture (2026-11-21)
- Re-fetched current ledger, GCR priority queue and immutable 63-country both-leg cohort. CHL is a fixed-cohort member with both archived IMF rows present. Search found no prior dedicated CHL Q2 national dual-leg report; prior Chile work was source/vintage context and not repeated. Brazil was skipped because BCB monthly portfolio capture and PA/Dataflow identity blocker are already documented; queue says not to repeat exhausted public endpoint probes.
- BLR follow-up: NBRB official publication index currently lists January–June 2026 as latest 2026 bulletin; exact PDF retrieval timed out and direct download failed. H1 cannot substitute for Q2. BLR remains PARTIAL; no values/raw bytes or H1-to-Q2 inference.
- New CHL source result: official BCCh Q2-2026 BOP PDF gives portfolio investment net +USD 299m and notes portfolio-liability increase USD 5,398m, but these were not used to infer the missing asset leg. The official BDE monthly source page independently displays both Q2 flow legs (USD million): assets Apr 1,643.45, May 932.56, Jun 2,522.90; liabilities Apr 3,224.69, May 2,501.14, Jun -328.32. Q2 sums: assets 5,098.91; liabilities 5,397.51; liability-minus-asset = 298.60, rounding to published net +299. This is independent monthly-leg aggregation, not net-to-leg back-solving.
- Official BDE total monthly series codes: assets F068.G2.FLU.Z.0.S.A.Z.T.Z.Z.6.0.M; liabilities F068.G2.FLU.Z.0.S.P.Z.T.Z.Z.6.0.M. BDE metadata identifies USD million, monthly frequency and BPM6. Raw downloadable response bytes, retrieval receipt, SHA-256 and exact same-vintage/revision alignment were not captured.
- Reused exact archived IMF Q2 rows: CHL A_NFA_T OBS_VALUE=5098898918.11 USD SCALE=6; L_NIL_T OBS_VALUE=5397501758.8 USD SCALE=6. Existing raw panel blob SHAs unchanged: 15449e87c9057291a1f52f2f8cd9805df55f9fb8 / 15f379dc42e2760eb5f2384618e48f5ddc3177f1. Diagnostic /1e6 differences versus BDE sums are 0.01108189m asset and 0.0082412m liability; near-match only, NOT PASS pending vintage/raw bytes/sign bridge.
- CHL: cohort/IMF rows PASS; official Q2 release PASS; official BDE separate monthly flow legs and units PASS; Q2 monthly aggregation and net arithmetic PASS (diagnostic); raw-byte SHA-256 NOT_CAPTURED; same-vintage/sign bridge PARTIAL; CHL PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED. Detail: docs/GCR_CHILE_CHL_Q2_2026_BCCH_BDE_MONTHLY_DUAL_LEG_VINTAGE_AUDIT_CONTINUATION160_20261121.md (create commit df6d0252ef70c345308a1da44574671050f8141e).
- Next highest-value bounded action: retrieve BCCh BDE official asset/liability series via documented raw export/API route; capture bytes, response URL, retrieval timestamp, source update/vintage metadata and SHA-256; reconcile Q2 vintage and exact sign/item bridge to IMF. If no supported raw-byte route, retain CHL PARTIAL and advance. No net-to-leg inference, IIP stock substitution, annual/H1 allocation, IMF re-query, cohort rebuild, or production changes. ₹0; UNKNOWN never PASS.


## Continuation 161 — Chapter 47 Part 9: Chile BCCh BDE API/export access-gate audit (2026-11-21)
- Re-fetched current ledger, GCR priority queue and CHL Part-8 report. Limited work to unresolved raw-byte/vintage capture; did not repeat monthly values or Q2 arithmetic.
- Official BCCh API is free but requires a BDE account, API activation and personal API Key Token; REST GetSeries returns JSON observations/metadata and requires token. No authorized BDE credentials/token are present in research context, so API request NOT_EXECUTED; no token guessed, requested from external party or stored.
- Official BDE Canasta UI visibly documents “Exportar a Excel” with horizontal/vertical and year-selection options. Current browser/index route identifies the control but does not execute its “Aceptar” action or yield workbook bytes; export NOT_EXECUTED.
- Therefore Part 8 BDE observations remain source-page evidence only. Raw API/Excel bytes, receipt, retrieval timestamp, SHA-256, updatedAt/vintage snapshot and same-vintage cut-off NOT_CAPTURED/NOT_ESTABLISHED. CHL remains PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Detail: docs/GCR_CHILE_CHL_Q2_2026_BCCH_BDE_API_EXPORT_ACCESS_GATE_AUDIT_CONTINUATION161_20261121.md (create commit 9a192c2c893f2c2ea368f57eb46a1a030599e7f0).
- Next: if an authorized BDE session is available, activate free API or execute official basket Excel export; archive exact response/workbook bytes, URL, timestamp, series IDs, update/vintage metadata and SHA-256. Otherwise retain CHL PARTIAL and advance. No IMF re-query/cohort rebuild or production changes; ₹0; UNKNOWN never PASS.


## Continuation 162 — Chapter 47 Part 10: Colombia COL SUAMECA public quarterly series route recheck (2026-11-21)
- Re-fetched current ledger, priority queue, immutable 63-country Q2 both-leg cohort and prior COL source report. COL remains fixed-cohort member with both IMF panel legs present; no IMF re-query/cohort rebuild and no repeated SDMX route (official SDMX guide excludes BOP).
- Official BanRep/SUAMECA multiple-download catalogue again exposes distinct quarterly portfolio net acquisition of assets and net incurrence of liabilities series, current USD million, 2000-Q1 through Q2-2026, last updated 2026-09-01. Official prebuilt BOP dashboard confirms quarterly detail and annex views through Q2-2026.
- Current retrieval recheck: multiple-download page HTTP 502; prebuilt dashboard timed out. These are retrieval bridge failures, not proof of source absence. No exact series IDs, Q2 observations, export action, raw bytes, receipt, timestamp or SHA-256 captured. IIP stocks/financial-account aggregates not substituted.
- COL remains PARTIAL / BLOCKED / NOT PASS; sign and same-vintage bridge NOT_ESTABLISHED; numeric comparison NOT_DONE; aggregate NOT_AUTHORIZED.
- Detail: docs/GCR_COLOMBIA_COL_Q2_2026_SUAMECA_PUBLIC_SERIES_ROUTE_RECHECK_CONTINUATION162_20261121.md (create commit 2ac1deb306091269a8471531f1f22c8f58c979fd).
- Next: only resume COL via a genuinely supported interactive session that executes official SUAMECA export and captures both Q2 series with raw bytes, vintage, timestamp and SHA-256; otherwise close route and advance to POL. No repeated 502/timeout/SDMX probes. ₹0; no production changes; UNKNOWN never PASS.


## Continuation 163 — Chapter 47 Part 11: Poland POL Q2-2026 NBP quarterly release dual-leg capture (2026-11-21)
- Re-fetched current ledger, priority queue and prior POL source-gate report. The prior quarantine applied to bopa_en.pdf with March 2026 front matter; did not reuse it.
- Identified distinct official NBP Q2 release https://static.nbp.pl/dane/bilans-platniczy/bop_kw_en.pdf, titled “Balance of Payments in Q2 of 2026”, Warsaw 30-Sep-2026. Appendix 1 page 11 (PDF p.10), unit mn PLN, Q2 column: portfolio assets 24,144 (equity 9,616 + debt 14,528); portfolio liabilities 70,910 (equity 969 + debt 69,941). Both dual legs captured independently from national table; arithmetic checks pass.
- Reused existing IMF exact rows without re-query: A_NFA_T +USD6,602m, raw SHA-256 19ba3d8918245d7abe73125d76c08e27f9970817cc1a46b8753763352e5a2e21; L_NIL_T +USD19,391m, raw SHA-256 365bac8801d0951f3d69f863628e844c6da07b0e69651880614c815b859c769b.
- NBP release date known, but raw PDF bytes/SHA-256 not captured (container download failed). No ad-hoc PLN/USD conversion. Exact transaction FX convention and same-vintage bridge to IMF 19-Nov archive NOT_ESTABLISHED; cross-currency comparison NOT_DONE. POL PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Detail: docs/GCR_POLAND_POL_Q2_2026_NBP_QUARTERLY_RELEASE_DUAL_LEG_CAPTURE_CONTINUATION163_20261121.md (commit 438a3deedcd99fc245cdd2c500da6d5b940f7998).
- Next: capture NBP PDF raw bytes/SHA through supported route; establish exact transaction FX conversion or matched USD presentation for same two legs and revision-vintage bridge. If unresolved, retain PARTIAL and advance. No IMF query/cohort rebuild/production changes; ₹0; UNKNOWN never PASS.


## Continuation 164 — Chapter 47 Part 12: Poland NBP methodology/revision-vintage gate (2026-11-21)
- Re-fetched ledger, queue and POL Part-11 report; reused national Q2 dual-leg values and IMF exact receipt, no IMF re-query/cohort rebuild.
- Inspected official NBP Department of Statistics “Balance of payments Statistics — Methodological notes” (Sep-2023): quarterly BOP disseminated about three months after quarter and in PLN/EUR/USD; Q2 compiled/revised in September with up to nine quarters revision depth; portfolio flows sourced from security-by-security reports (holders for assets, issuers/intermediaries for liabilities), transaction market values calculated security-by-security, repo adjusted/excluded. Exact Q2 portfolio transaction FX conversion convention is not stated in this methodology edition.
- IMF DSBB Poland IIP metadata confirms separate portfolio assets/liabilities and security-by-security source, but is not a Q2 BOP conversion rule. NBP Q2 Sep-30 vintage vs IMF archive Nov-19 same-vintage bridge remains NOT_ESTABLISHED.
- New container-backed direct raw PDF download attempt failed; raw bytes/headers/byte count/SHA-256 still NOT_CAPTURED. POL remains PARTIAL / NOT PASS; cross-currency comparison NOT_DONE; aggregate NOT_AUTHORIZED.
- Detail: docs/GCR_POLAND_POL_Q2_2026_NBP_METHODOLOGY_REVISION_VINTAGE_GATE_CONTINUATION164_20261121.md (commit 5ca794a0d0ff42a15e06034adabc7a10281a0d46).
- Next: only pursue an official reporting-form technical spec explicitly stating transaction conversion or a matched-vintage USD Q2 dual-leg table; otherwise preserve PLN observations and advance. No repeat PDF download, FX inference, IMF query or production changes. ₹0; UNKNOWN never PASS.


## Continuation 165 — Chapter 47 Part 13: Poland official transaction-date FX rule found (2026-11-21)
- Re-fetched ledger, queue and Part-12 report. Reused NBP Q2 dual-leg values and IMF raw receipt; no duplicate value extraction, IMF re-query or cohort rebuild.
- New official NBP Department of Statistics “Explanatory notes to reporting questionnaires”, Version 1.8, July 2023: general §6 says end-period foreign-currency balances use NBP average rate on last business day, while other data use actual rate used on operation date or NBP average rate on preceding day. PW-AIN asset form example explicitly translates foreign-security purchase using trade-date USD/PLN 3.15 (USD15 × 3.15 = PLN472,500); end-period position separately uses 3.20. PW-RIN liability-side form example similarly distinguishes trade-date and end-period rates.
- This resolves the FX principle: portfolio security transaction flow uses trade-date actual FX (with §6 fallback), not quarter-end balance rate. Part-12 statement that no exact rule was identified is superseded for the reporting-form FX principle.
- However national Q2 totals PLN24,144m assets and PLN70,910m liabilities cannot be converted to USD with one quarter-average/quarter-end/aggregate-implied rate; transaction-level date/currency weights or an official matched USD Q2 dual-leg aggregate are absent. Raw NBP Q2 PDF SHA-256 remains NOT_CAPTURED; NBP 30-Sep-2026 vs IMF 19-Nov-2026 same-vintage bridge NOT_ESTABLISHED. No numeric cross-currency comparison. POL PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Detail: docs/GCR_POLAND_POL_Q2_2026_NBP_TRANSACTION_FX_RULE_AND_RECONCILIATION_BOUNDARY_CONTINUATION165_20261121.md (commit ae22fe0ca9ea409e9b645198ff70bf6b41118564).
- Next: search only for official NBP Q2 USD-denominated dual-leg aggregate or matching USD series with vintage metadata; otherwise retain PLN observations and advance. Do not infer USD totals from unweighted FX or repeat PDF download. ₹0; no production changes; UNKNOWN never PASS.


## Continuation 166 — Chapter 47 Part 14: Türkiye TCMB route closure and NPL handoff (2026-11-21)
- Re-fetched ledger, queue, POL Part-13, TUR reconciliation and TUR ZIP access-gate report. Reused existing TCMB monthly Q2 PDF snapshot rows and IMF receipt; no duplicate aggregation/PDF comparison, no IMF re-query or cohort rebuild.
- Official TCMB BOP page confirms monthly BPM6 publication and EVDS time-series availability. September-2026 official developments PDF Table 2 presents separate portfolio asset/liability rows in USDm, but columns are September monthly, Jan-Sep cumulative and 12-month, not Q2-only. This publication surface does not resolve the Q2 liability residual.
- Existing Q2 values retained: TCMB assets +5,749 USDm vs IMF +5,749 (displayed match); TCMB liabilities +9,183 vs IMF +9,270 (residual +87, unexplained, beyond display rounding). August/September PDF snapshots already shown identical Q2 rows; no complete revision history or same-vintage identity.
- Exact official September ZIP URL from Continuation 118 remains timed out; no bytes/member list/headers/size/SHA-256/revision metadata. No new byte-preserving route found; no repeated identical ZIP retry. TUR PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- POL official USD Q2 dual-leg search yielded no matched table; retain PLN values and advance. Next fixed-cohort priority: NPL, but avoid already-failed NRB XLSX and stale NSDP/SDMX routes; seek only a genuinely supported official NRB API/export. If none, close once and advance to RWA.
- Detail: docs/GCR_TURKIYE_TUR_Q2_2026_TCMB_OFFICIAL_SERIES_AND_ZIP_ROUTE_CLOSURE_CONTINUATION166_20261121.md (commit 8cc0d9513ef491f5c9b91715f47483e4d92453af).
- ₹0; no synthetic data, unsupported conversion, IMF re-query, cohort rebuild or production changes; UNKNOWN never PASS.


## 2026-11-21 — Mandatory GCR historical-task / duplicate-prevention gate
- New registry: `docs/GCR_Q2_2026_HISTORICAL_TASK_REGISTRY_AND_DUPLICATE_PREVENTION_GATE_20261121.md`.
- This control supersedes stale next-country handoffs where prior country reports already exist. Mandatory preflight: fetch current Ledger + Queue, search full country report history, inspect exact prior route failures, and build route fingerprint before any action.
- PASS tasks are skipped. PARTIAL requires a named unmet gate. BLOCKED/NOT_CAPTURED route is closed and cannot be retried without concrete new official endpoint/API/export, supported transfer capability, permission, or source revision. NOT_DONE is not permission to repeat.
- Duplicate correction: NPL has Continuations 55/56/58/94/128/130 and its NRB BPM6 XLSX, stale NSDP XML and wrong-family monthly archive routes are closed. RWA has Continuations 97/130 and its JS-only BNR portal route is already rechecked. SLV has Continuation 100 history. Do not select any as a new country without new evidence.
- TUR exact ZIP timeout remains closed; POL transaction-date FX principle is known but does not authorize aggregate FX conversion. Other country fingerprints/statuses are indexed in the registry.
- Final verification rule: re-fetch every modified file and record commit SHA + final blob SHA; unverified writes must be reported NOT_VERIFIED. Registry is rolling and does not claim all 63 countries fully indexed.
- No production code/configuration changed; protected invariants unchanged; ₹0; UNKNOWN never PASS.


## Continuation 167 — Chapter 47 Part 15: Honduras HND official BCH source/export gate (2026-11-21)
- Re-fetched current Ledger, Queue, duplicate registry and immutable 63-country cohort. HND is in the cohort; repository search found no prior dedicated HND Q2-2026 national portfolio dual-leg report. No IMF re-query/cohort rebuild.
- BCH official dynamic BOP page confirms quarterly/annual frequency and “Obtener serie de Datos”; official calendar lists quarterly BOP and BOP/IIP/debt report with 90-day release timing and Excel/PDF formats. BCH SDDS page lists BOP Browse Data and SDMX download.
- Exact XLSX locator resolved to SharePoint WOPI; browser page exposed app shell only and separate container download failed. Official SDMX XML retrieval returned HTTP 400 unsupported text/xml. No bytes/sheets/observations/hash captured. Q3-2025 portfolio chart is historical context only, not Q2-2026.
- HND national Q2 asset/liability legs NOT_CAPTURED; sign/unit/vintage NOT_ESTABLISHED; comparison NOT_DONE; HND PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED. Detail: `docs/GCR_HONDURAS_HND_Q2_2026_BCH_OFFICIAL_BOP_SOURCE_AND_XLSX_ACCESS_GATE_CONTINUATION167_20261121.md` (commit `bb1df78f301d016ab90b13c0d6fcbd2f342a0335`).
- Duplicate gate: close identical XLSX/WOPI/XML routes; reopen only on a genuinely distinct supported official API/export/byte-transfer capability. Next: advance to next unvalidated cohort member after full preflight. ₹0; no production changes; UNKNOWN never PASS.


## Continuation 168 — Chapter 47 Part 16: Kosovo KOS BQK Q2-2026 ROW transaction-matrix source gate (2026-11-21)
- Re-fetched current ledger, GCR queue, duplicate registry and immutable 63-country cohort before selection. KOS is in the fixed Q2-2026 both-leg cohort (A_NFA_T and L_NIL_T PRESENT); no dedicated prior KOS national dual-leg report found in scoped repository search. No IMF re-query/cohort rebuild.
- New official BQK route identified: External Sector Statistics → Financial Accounts Statistics → REST OF THE WORLD (S.2) → ROW Matrix — Transactions, period Q2 2026. Exact XLS locator: https://bqk-kos.org/wp-content/uploads/2024/09/ROW%20Matrix%20%E2%80%93%20Transactions.xls . BQK methodology states financial-account statistics record transaction flows by financial instrument and assets/liabilities for relations with non-residents; methodology aligned with ESA 2010/SNA 2008 and BPM6.
- Browser XLS fetch returned HTTP 403 Forbidden; no workbook bytes/sheets/rows/portfolio leg values/hash. Separate BQK monthly Financial account XLS route returned HTTP 400 unsupported Excel MIME; container download failed. These identical routes are closed absent a new supported transfer capability.
- Q2 IIP International Investment Portfolio is a stock product and is NOT_ADMITTED as a transaction-flow substitute. Do not use financial-account net totals or net-to-leg back-solving.
- Status: cohort membership PASS; official ROW transaction-matrix locator/methodology PASS; actual workbook bytes NOT_CAPTURED; portfolio leg exposure NOT_VERIFIED; Q2 national asset/liability legs NOT_CAPTURED; sign/unit/vintage NOT_ESTABLISHED; KOS PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Detail report: docs/GCR_KOSOVO_KOS_Q2_2026_BQK_ROW_TRANSACTION_MATRIX_SOURCE_GATE_CONTINUATION168_20261121.md (commit 8bdb4ee396a68591f46fdcd56f75a365ea48c501).
- Next exact action: only retrieve the exact ROW transaction XLS through a genuinely new supported official byte-transfer/export route; inspect S.2 transactions, instrument labels, Q2 header and separate portfolio asset/liability legs. Then reuse archived IMF rows for separate-leg sign/unit/vintage comparison. No repeated failed XLS requests, no production changes; ₹0; UNKNOWN never PASS.


## Continuation 169 — Chapter 47 Part 17: The Gambia GMB CBG Q2-2026 BOP source-feasibility gate (2026-11-21)
- Re-fetched current Master Ledger, GCR Priority Queue, Historical Task Registry and immutable 63-country Q2 both-leg cohort. GMB is present with A_NFA_T_PRESENT and L_NIL_T_PRESENT; scoped repository search found no prior dedicated GMB national portfolio dual-leg report. No IMF re-query/cohort rebuild.
- Official CBG Monetary Policy Report August 2026 inspected. It confirms preliminary Q2-2026 BOP; current account deficit USD34.6m, capital account surplus USD26.2m, financial-account net inflow USD95.4m. Narrative names FDI inflows USD83.3m, other investment net inflows USD24.1m and reserve-asset net acquisition USD12.0m. Appendix Table 2 reports Q2 financial-account net -95.4; Table 5 only current account/capital account/net lending-borrowing. No portfolio investment row found in report; national Q2 portfolio asset/liability legs NOT_CAPTURED. Absence does not imply zero.
- CBG Statistics page points to its Macroeconomic Data Warehouse; linked URL redirects to an interactive app shell with generic editor/CSV-upload instructions and no visible BOP catalogue, series IDs, export payload or API. CBG quarterly-bulletin page rendering lists files through 2018 only. Historical 2017/18 portfolio-net rows are not Q2-2026 evidence.
- IMF DSBB metadata search result states CBG compiles BOP quarterly using BPM5. This confirms frequency/methodology metadata only, not BPM6 comparability or national Q2 dual legs.
- Status: fixed cohort membership PASS; official Q2 report inspected PASS; quarterly compilation metadata PASS; Q2 national portfolio asset/liability legs NOT_CAPTURED; data warehouse payload NOT_EXTRACTED; sign/unit/classification/vintage NOT_ESTABLISHED; GMB PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Detail report: docs/GCR_GAMBIA_GMB_Q2_2026_CBG_BOP_QUARTERLY_REPORT_AND_DATAWAREHOUSE_SOURCE_GATE_CONTINUATION169_20261121.md (commit ac53489c52ff5bcc4389cdb1a4969c6ecfe13023).
- Next: seek only a distinct public CBG Q2 BOP table or documented data-warehouse API/export payload with separate portfolio asset/liability transaction legs and metadata. If unavailable, close this route and advance after full preflight. No net-to-leg back-solving, no zero inference, no old-quarter substitute, no production changes; ₹0; UNKNOWN never PASS.


## Continuation 170 — Chapter 47 Part 18: Guinea GIN BCRG Q2-2026 BOP source-boundary audit (2026-11-21)
- Re-fetched current Master Ledger, GCR Priority Queue, Historical Task Registry, immutable 63-country cohort, and previous GMB Continuation 169 report. GIN is in the fixed cohort with both IMF rows present; scoped repository searches found no prior dedicated GIN Q2 national dual-leg report. GMB remains PARTIAL and its same route was not repeated. No cohort rebuild or IMF re-query.
- Official BCRG 2026 index and 22nd MPC page (22-Sep-2026 listing; meeting document download label) located. The rendered MPC page did not expose a retrievable document URL. Official BCRG BOP statistics index and Balance des paiements page located; rendered BOP page exposes title but no visible dataset, series IDs, download or API payload.
- Inspected official BCRG June-2025 Q1 monetary policy report. Its Table 11 and Appendix Table 17 show portfolio investment as a single net functional-category row only, not separate asset/liability transaction legs. Historical 2024–Q1 2025 net values are explicitly not used for Q2-2026 and do not prove 2026 detailed data lack a split.
- Current Q2-2026 national portfolio assets/liabilities NOT_CAPTURED; September 2026 MPC raw bytes/hash NOT_CAPTURED; BOP statistics API/export NOT_EXTRACTED; sign/unit/classification/vintage NOT_ESTABLISHED; comparison NOT_DONE; GIN PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Detail report: docs/GCR_GUINEA_GIN_Q2_2026_BCRG_OFFICIAL_BOP_SOURCE_BOUNDARY_AND_REPORTING_ROUTE_CONTINUATION170_20261121.md (commit f524e985d943eb180db883adcc047567005393d4).
- Next: find the actual document URL behind the official September 2026 MPC download control or a distinct public BCRG BOP export/API. Preserve raw bytes/hash and metadata before inspecting Q2 separate portfolio legs. If no new locator exists, retain PARTIAL and advance after full preflight. No historical net-to-leg back-solving, no production changes; ₹0; UNKNOWN never PASS.


## Continuation 171 — Chapter 47 Part 19: Lao PDR LAO BOL Q2-2026 BOP dual-leg source-boundary audit (2026-11-21)
- Re-fetched Master Ledger, GCR Priority Queue, Historical Task Registry, immutable 63-country Q2 cohort and GIN Continuation 170 report. LAO exact cohort row has A_NFA_T_PRESENT and L_NIL_T_PRESENT; scoped repository search found no dedicated LAO national Q2 dual-leg report. GIN remains PARTIAL and no BCRG page retries. No IMF re-query/cohort rebuild.
- Official BOL External Sector Statistics page located: https://www.bol.gov.la/en/External_Sectors. It lists Balance of Payments, Official Reserve Assets, Exchange Rate and FDI netflow, with Download Excel/Metadata columns; indexed rendering shows no populated download link for BOP. Direct open returned HTTP 502. Annual Reports index lists 2025 report last updated 19-Aug-2026; no Q2-2026 file locator or bytes captured.
- Official BOL Annual Economic Report 2023 Table 13 demonstrates historical reporting can split Portfolio investment into net total, assets and liabilities (assets further by equity/fund shares and debt securities), in million USD. Historical values are schema-only and not Q2-2026. Official BOL historical Q4/2016 report used a net-only portfolio row, showing layout varied by vintage; current layout cannot be presumed.
- AMRO 2024 Lao PDR consultation assessment says BOL BOP is quarterly, BPM6, with 1–2 quarter publication lag. Official BOL legal PDF dated 18-Dec-2025 says BOL compiles BOP quarterly and annually, including portfolio investment among transaction types. This is methodology/compilation context, not proof Q2-2026 legs are public.
- Q2-2026 national portfolio asset/liability values NOT_CAPTURED; current Excel/metadata URL NOT_EXPOSED; raw bytes/hash NOT_CAPTURED; sign/unit/classification/vintage NOT_ESTABLISHED; comparison NOT_DONE; LAO PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Detail report: docs/GCR_LAO_PDR_LAO_Q2_2026_BOL_OFFICIAL_BOP_DUAL_LEG_SOURCE_BOUNDARY_CONTINUATION171_20261121.md (commit ed3ca079ce3e347e64e1ee46bf57b7ba2fda98cb).
- Next: resolve actual Download Excel/Metadata URLs behind BOL External Sector Statistics via a distinct supported route; capture Q2-2026 workbook bytes/hash and inspect separate portfolio asset/liability rows, sign/unit/BPM6/vintage. If unavailable/not released, retain PARTIAL and advance after full preflight. No historical/annual/H1 substitute, net-to-leg back-solving or production changes; ₹0; UNKNOWN never PASS.


## Continuation 172 — Chapter 47 Part 20: LAO official NSDP BOP XLSX/SDMX locator discovery (2026-11-21)
- Re-fetched Master Ledger, GCR Priority Queue, Historical Task Registry, Continuation 171 LAO report and immutable Q2 cohort. LAO is in fixed cohort with both IMF legs; no cohort rebuild or IMF re-query.
- New official source discovered: Lao Statistics Bureau National Summary Data Page https://www.lsb.gov.la/lsb-en.htm . Its Balance of Payments row explicitly links Browse Data, Download in SDMX and DSBB Metadata.
- Exact BOL XLSX locator resolved from Browse Data: https://www.bol.gov.la/statistics/BOP6_Lao%20PDR.xlsx . Exact BOL SDMX XML locator resolved from Download in SDMX: https://www.bol.gov.la/statistics2/BOP6_Lao%20PDR.xml . Official IMF DSBB metadata locator: https://dsbb.imf.org/egdds/dqaf-base/country/LAO/category/BOP00 . These exact links are new discoveries and close Continuation 171's locator-identification gap.
- Both BOL downloads were followed from official NSDP page but retrieval returned HTTP 400 Timeout fetching; no bytes, headers, length, XML keys, workbook sheets, observations or SHA-256. A separate container request failed DNS resolution (no HTTP response). DSBB page opened to a general shell; country-specific extracted fields not visible. Do not infer absence/zero or claim data absent.
- Q2-2026 presence, separate portfolio asset/liability legs, sign, units, BPM6 and revision vintage remain NOT_VERIFIED / NOT_ESTABLISHED. LAO PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Detail report: docs/GCR_LAO_PDR_LAO_Q2_2026_BOL_NSDP_SDMX_EXPORT_LOCATOR_DISCOVERY_CONTINUATION172_20261121.md (commit 0628b1ba96b4e3ab31e4530373c7bdb8f5070826).
- Next: retrieve exact XLSX or XML through a genuinely different supported byte-transfer route; record URL/time/status/content type/byte count/SHA-256; inspect Q2-2026 portfolio assets and liabilities separately, signs/units/vintage; only then reconcile archived IMF rows. Do not repeat same timed-out fetch path. No production changes, ₹0, UNKNOWN never PASS.


## Continuation 173 — Chapter 47 Part 21: LAO BOL SDMX Central / DSBB metadata cross-check (2026-11-21)
- Re-fetched Master Ledger, Priority Queue, Historical Registry, Continuation 172 and 171 before work. LAO fixed cohort and both IMF rows remain as previously established; no IMF re-query/cohort rebuild.
- Live official NSDP page https://www.lsb.gov.la/lsb-en.htm reconfirmed BOP Browse Data, Download in SDMX and DSBB Metadata links. Clicking BOL XLSX https://www.bol.gov.la/statistics/BOP6_Lao%20PDR.xlsx and XML https://www.bol.gov.la/statistics2/BOP6_Lao%20PDR.xml now returns HTTP 502 Bad Gateway (C172 recorded HTTP 400 timeout; retain both outcomes as separate attempts). No bytes/headers/length/sheets/series/observations/hash.
- DSBB URL https://dsbb.imf.org/egdds/dqaf-base/country/LAO/category/BOP00 resolves but extracted view is a generic dynamic shell with {{country.CountryName}} and no LAO-specific BOP periodicity/timeliness/methodology/revision fields. Only locator PASS.
- Public IMF SDMX Central registrations page https://sdmxcentral.imf.org/data/registrations.html inspected; find exact “LAO” returned no match. This is scoped absence in that registry page only, not proof no feed exists. No alternate registered mirror identified.
- Q2-2026 period, portfolio asset/liability legs, signs, units, BPM6 and vintage NOT_VERIFIED/NOT_ESTABLISHED; raw data/hash NOT_CAPTURED; LAO PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Detail report: docs/GCR_LAO_PDR_LAO_Q2_2026_BOL_SDMX_CENTRAL_REGISTRY_AND_DSBB_METADATA_CROSSCHECK_CONTINUATION173_20261121.md (commit 39fd1886b182f813a3101905a2bee93bd26f61b8).
- Next: only a distinct official BOL mirror/export, public NSDP data-service endpoint, or genuinely new supported byte-transfer capability; preserve bytes/hash and inspect two Q2 portfolio legs. If unavailable, keep PARTIAL and advance after full preflight. No historical/IMF-only substitutes, production changes; ₹0; UNKNOWN never PASS.


## Continuation 174 — Chapter 47 Part 22: Sri Lanka LKA Q2-2026 CBSL/Treasury portfolio dual-leg reconciliation (2026-11-21)
- Re-fetched current Master Ledger, Priority Queue, Historical Registry, LAO C173 and fixed 63-country cohort. LKA row: A_NFA_T_PRESENT and L_NIL_T_PRESENT; scoped repo search found no prior dedicated LKA national dual-leg reconciliation. No IMF re-query/cohort rebuild; LAO failed route not repeated.
- Official Ministry of Finance, Planning and Economic Development Sri Lanka, Budget Economic and Fiscal Position Report–2027, issued 12-Nov-2026, official PDF https://treasury.gov.lk/api/file/04b45c52-3ded-4621-86c7-b8c67455c9d8 , Table 7 page 102, BOP 2026, USD million, source explicitly CBSL. Separate provisional Q2-2026 Portfolio Investment Assets +26 and Liabilities -351.
- Reused archived IMF raw rows, asset file blob SHA 15449e87c9057291a1f52f2f8cd9805df55f9fb8 exact Q2 value USD +25,676,196.5415909; liability file blob SHA 15f379dc42e2760eb5f2384618e48f5ddc3177f1 exact Q2 value USD -350,932,889.850796. In USD mn: +25.6761965 rounds to +26; -350.9328899 rounds to -351. Both legs independently agree with national published rounded values. No net-to-leg back-solving.
- National values are provisional. CBSL primary statistical tables page direct access returned HTTP 403; no original CBSL workbook or Ministry PDF raw bytes/hash captured. IMF row's revision date unavailable, so exact same-vintage bridge NOT_ESTABLISHED. Classification: strong dual-leg reconciliation / provisional; final same-vintage pass pending. Aggregate remains NOT_AUTHORIZED.
- Detail report: docs/GCR_SRI_LANKA_LKA_Q2_2026_CBSL_TREASURY_BOP_PORTFOLIO_DUAL_LEG_RECONCILIATION_CONTINUATION174_20261121.md (commit 8b9f7f96657d6974a456672b65dfa2dc9180393b).
- Next: obtain underlying CBSL Table 2.10 BPM6 quarterly export + metadata and SHA-256; establish IMF observation revision date vs 12-Nov-2026 national vintage. Upgrade only if bridge is confirmed. No production changes, ₹0; UNKNOWN never PASS.
