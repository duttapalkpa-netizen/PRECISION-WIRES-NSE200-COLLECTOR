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
