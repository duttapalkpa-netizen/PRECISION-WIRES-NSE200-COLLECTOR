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
