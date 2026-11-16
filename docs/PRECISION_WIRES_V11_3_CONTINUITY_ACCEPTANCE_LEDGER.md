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


## 2026-11-15 — Run #7 PASS and signal-ledger fail-closed hardening
- Verified cost-aware research CI Run #7 / ID `43696699661`: job `research-unit-tests` completed SUCCESS on the code + validation-test commits. Run #6 / ID `43696697367` was cancelled; do not repeat it.
- Review of the accepted simulator found `run()` silently removed duplicate `CUT_OFF,SYMBOL` rows using `drop_duplicates()`, contrary to the fail-closed duplicate-key contract. It also conflated target touch with net profitability in `TARGET_HIT` and accepted infinite volume as a valid positive quantity.
- Created isolated branch `research/cost-aware-signal-ledger-guard-20261115` from reviewed commit `56a8b63d4f5c286917db9368b96907383388143c`.
- Hardened research-only simulator to reject duplicate normalized signal keys, make `TARGET_HIT` represent target execution independently of net profitability, and reject non-finite volume. Added focused regression tests for all three cases.
- Module commit: `d930fa8a2f6d335c9c1682e147180250173a42cb`; module blob: `ec9b4e95c2b06ed98bb057af251f151fe12c36d2`.
- Test commit: `0c798e0b12f538a46610d733f30c780b0bc479d7`; test blob: `48c6d3f5dfb9dd3f30ee936fa8595aeed9facdaf`.
- New workflow runtime validation is pending; no PASS claim until its run is fetched. Historical replay remains BLOCKED pending signal-source acceptance and independent input/outcome gates. No production logic or production workflow modified.


## 2026-11-16 — Critical H+3/H+5 forward-outcome alignment finding and isolated correction
- Source review of `pipeline/walk_forward_backtest.py` (blob SHA `d085f7a2d35a88b4c4eaba65144a429a06961b09`) found `future_outcomes()` computes `shift(-1).rolling(h, min_periods=1).max()`. This is a trailing rolling window over shifted values, not the exact forward window T+1..T+h for h>1; `min_periods=1` also emits partial labels at the end of each symbol series. H+1 is not affected by the window-direction issue, but H+3/H+5 labels are not accepted as correctly aligned/matured from this implementation. Existing derived H+3/H+5 precision/lift and state labels must be treated as NOT_VERIFIED pending rebuild/reconciliation. Do not silently overwrite old artifacts.
- Kept the V11.4 pipeline and all production logic untouched. Added isolated research helper `pipeline/forward_outcome_integrity.py` (commit `136a11721f8802e318f5881ae20a8df30739e5b0`) that computes exactly T+1..T+h per symbol, preserves input row order, rejects invalid dates/duplicate symbol-date keys, and emits NaN/UNKNOWN unless every future session and price in the horizon is valid.
- Added `tests/research/test_forward_outcome_integrity.py` (commit `cf81c469de62c2806e2c672fb23de1c38c5da91b`) with nine regression tests: exact H1/H3/H5 high and close outcomes; full maturity/no partial tail labels; symbol isolation; unsorted input; duplicate/date rejection; invalid future price; invalid horizons; input immutability.
- Updated isolated 5-minute research CI workflow to include the new helper and discover all `tests/research/test_*.py` tests. Workflow commit: `11d80d5a9394fc95c4e2be312ed60931b526ae8d`.
- Runtime CI validation is pending; no PASS claim until run and job result are fetched. No historical replay or production pipeline modification was performed. CORE-672, Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, collector workflow and archived artifacts remain unchanged.
- Progress: source defect identification 100%; isolated correction implementation 100%; regression-test authoring 100%; CI runtime verification pending; corrected historical replay 0%; independent outcome reconciliation 0%; final V11.3 research acceptance BLOCKED.


## 2026-11-16 — Forward-outcome integrity PR checkpoint
- Created draft PR #38: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/pull/38 . It is OPEN, DRAFT, NOT MERGED. No production code is included.
- Added isolated exact-forward label helper commit `136a11721f8802e318f5881ae20a8df30739e5b0`; nine tests commit `cf81c469de62c2806e2c672fb23de1c38c5da91b`.
- CI workflow commit `11d80d5a9394fc95c4e2be312ed60931b526ae8d` expanded push paths and test discovery; follow-up commit `9f0c5ae865cd475e02eba11bcd88a72f6d2e0b1a` aligned pull_request path filters. Bounded timeout remains five minutes.
- Independent fixture arithmetic sanity check confirmed ABC cutoff 2026-01-01 yields H1 HIGH +2%, H3 HIGH +6%, H3 CLOSE +5%, H5 HIGH +6%, H5 CLOSE +5%; XYZ labels remain isolated. This is a local fixture sanity check only, not GitHub CI PASS.
- GitHub workflow-run listing/status endpoint available through this connector does not expose push-triggered run listing; the commit combined-status endpoint currently returns no statuses, and PR-triggered run lookup returned no runs at the time of check. Therefore CI runtime remains NOT_VERIFIED; do not infer PASS.
- Historical outcome rebuild remains NOT_STARTED; old H+3/H+5 artifacts remain NOT_VERIFIED. Do not reuse their precision/lift or state labels as accepted evidence until corrected rebuild and independent ledger reconciliation.
- Scoped progress: defect audit 100%; isolated helper 100%; regression test source 100%; workflow wiring 100%; fixture arithmetic sanity 100%; CI runtime verification pending; historical replay 0%; independent reconciliation 0%; final acceptance BLOCKED.


## 2026-11-16 — Second-pass test audit: global-session maturity guard
- Reopened PR #38 files and performed a test-by-test source audit. Found a defect in the newly authored maturity assertion: it unintentionally included XYZ rows while asserting ABC's H+3 tail was immature. Corrected the assertion to scope ABC only.
- More importantly, identified that symbol-local row shifting could silently skip a missing symbol/date row and count a later date as the next trading session. Hardened `pipeline/forward_outcome_integrity.py` to use the dataset-wide unique trading-session calendar and require a valid row for the symbol on every one of the next H sessions; missing symbol/session observations now remain UNKNOWN.
- Added a regression test proving a missing ABC row on a global market session cannot be skipped when calculating H+1/H+3. Updated helper commit `2d50256f0319b0d32c476054b1d0236f28826229`; test commit `a5963b6e3f4f84e8725fba7f6abb2ce62d151055`.
- The forward-outcome suite now contains 10 test methods (previous PR description said nine; description must be updated). The workflow still discovers all `test_*.py` research tests and has a 5-minute timeout.
- Branch comparison against main: 11 commits ahead, 0 behind. No production file changed; PR #38 remains draft/unmerged. CI run listing still returns no PR-triggered runs and combined commit status must be checked again; no runtime PASS claim.
- Progress: source/test audit 100%; global calendar guard implementation 100%; 10-test source suite 100%; CI runtime pending; full historical rebuild 0%; independent reconciliation 0%; final acceptance BLOCKED.


## 2026-11-16 — Research contract decision reconciliation and replay gate
- Re-read the full research contract and simulator source rather than repeating the earlier source audit. Confirmed simulator records target touch independently of net profitability (`TARGET_HIT = reason == TARGET`), applies 0.22 percentage-point cost once, enters next global session OPEN, uses intraday HIGH, -3% stop, conservative stop-first, and horizon-final CLOSE. Existing focused tests cover target touch with negative net return, stop-first, gap stop, missing symbol sessions, maturity and duplicate keys.
- The contract still incorrectly said G0 was blocked pending decisions, despite the user's previously explicit approval of the above conventions. Reconciled the contract to freeze those exact research-only rules and mark G0 PASS for convention approval; circuit/price-band feasibility remains explicitly unverified due missing validated restriction data, and portfolio sizing/concurrency remain undefined, so only per-trade metrics are permitted.
- Contract update commit: `62eb7c42ec01c490838f2eb62b4d94d651ade0f8`. No simulator or production code changed in this step.
- Replay is still not safe to start: the actual OHLC source artifact and accepted signal CSV must be present and provenance/hash-verified in the active workspace; the repository's simulator defaults alone do not prove those inputs exist. CI for PR #38 remains NOT_VERIFIED (connector returned no workflow runs/statuses); no PASS inferred.
- Progress: decision/contract reconciliation 100%; simulator convention source review 100%; CI runtime verification pending; source-input provenance gate 0%; corrected historical replay 0%; independent reconciliation 0%; final acceptance BLOCKED.


## 2026-11-16 — Historical replay input provenance audit (read-only)
- Audited the exact input contracts and source-generation path for the research replay. The simulator expects `data/processed/nse_eq_200_sessions.csv` and `outputs/backtest/walk_forward_predictions.csv`; these are runtime-generated paths, not evidence that the files currently exist or are verified in this session.
- Confirmed `collector/build_200_sessions.py` creates the processed OHLC/delivery dataset from `data/raw/sec_bhavdata_full_*.csv`, and writes `data/processed/nse_eq_200_sessions.csv` plus `symbol_session_coverage.csv`. The main collector workflow runs `collector/nse_download.py --sessions 200`, then builder, QA, V11.4 walk-forward, and uploads `data/processed/`, `data/reference/`, `data/qa/`, and `outputs/backtest/` as a GitHub Actions artifact. The separate prospective workflow independently rebuilds 200 sessions and uploads audit outputs.
- Input provenance gate remains BLOCKED: no actual downloaded artifact bytes, artifact ID, SHA-256, row count, unique symbol/session counts, date range, or signal-file content were available from the repository source inspection. Do not substitute the previously reported 317-session archive for the 200-session path expected by this simulator; reconcile exact source artifact and intended coverage first.
- Newly identified QA weakness (audit finding, not changed): `collector/build_200_sessions.py` calls `drop_duplicates(["SYMBOL","DATE"])` before QA, silently suppressing duplicate source rows rather than failing closed. `qa/validate_dataset.py` checks duplicate keys only after that suppression, and its PASS gate requires at least 200 raw session-list entries but does not assert processed DATE count equals session-list count or that each symbol's missing sessions are accounted for. Therefore a PASS from this QA script alone is insufficient proof of raw-to-processed row integrity or per-symbol full-session coverage.
- Do not modify the protected collector workflow or production builder in this task. Record this as a source-integrity blocker requiring an isolated audit/check against the original raw files and the uploaded artifact before any replay.
- Workflow artifact API listing could not be retrieved through the connected GitHub interface in this audit; no artifact ID or run was invented. Existing CI status for PR #38 remains NOT_VERIFIED; no PASS claim.
- Progress: input-path/source-flow audit 100%; artifact bytes/hash verification 0%; raw-to-processed duplicate reconciliation 0%; global session/date reconciliation 0%; signal-file provenance verification 0%; corrected replay 0%; independent ledger reconciliation 0%; final acceptance BLOCKED.


## 2026-11-16 — Read-only raw-to-processed integrity audit implemented
- Added `scripts/research/audit_raw_processed_integrity.py`, a read-only audit that hashes each raw Bhavcopy file and processed dataset; derives session dates from raw filenames; detects duplicate raw and processed SYMBOL/DATE keys; compares raw versus processed session-date sets and distinct symbol/date key sets; and reports symbol-level session gaps without fabricating rows.
- Added five focused tests in `tests/research/test_raw_processed_integrity.py`: exact match PASS; duplicate raw key FAIL; missing processed date/key FAIL; extra processed date FAIL; symbol session gap reported without false failure or synthetic fill.
- Wired both new files into the existing 5-minute research-only unittest workflow. No production collector, builder, QA, selector, ranking, pressure-fade, CORE-672, or main workflow changed.
- Commits: audit script initial `7158cec7e1eb1d7c1f736a6453aa0958b452de53`; test `55a4812f15b302221f65febff48894ea1199d6cc`; newline correction `d6e736fafc67c698966feb9bdae173e1ad684a3f`; workflow wiring `22e4ca4c618c5e36c34968215333af3ca83741b3`.
- Important interpretation: a symbol-level missing session is reported as a coverage gap but does not automatically fail the whole raw-to-processed key audit, because listings/suspensions/source availability require separate evidence. No missing row is synthesized. The audit is not yet run against the real Actions artifact because artifact ID/bytes are not available in the current connected session.
- CI status is pending/not verified; source files and tests are committed but no runtime PASS is claimed.
- Progress: audit utility implementation 100%; five test cases authored 100%; 5-minute workflow wiring 100%; GitHub ledger update 100%; CI runtime 0%/pending; actual artifact download/hash audit 0%; corrected replay 0%; independent reconciliation 0%; final acceptance BLOCKED.


### CI runtime update — 2026-11-16
- The newly wired PR-triggered research workflow has now started: Run #35, ID `43747974395`.
- Job `research-unit-tests`, job ID `132915404242`. At last inspection, checkout and Python setup completed; dependency installation was in progress; unittest step had not started. No conclusion/PASS yet.
- The run is recorded as IN_PROGRESS, not PASS. Recheck this run before any replay or acceptance decision.


## 2026-11-16 — CI cancellation diagnosis and mitigation
- Rechecked Run #35 (`43747974395`), job `132915404242`: workflow ended CANCELLED; dependency installation completed but the unittest step was skipped. This is not a test failure and not a PASS.
- Job log shows GitHub reported `The operation was canceled` immediately after installing latest pandas 3.1.1 and numpy 2.5.4. The workflow used `concurrency.cancel-in-progress: true`; rapid consecutive commits on the same branch could cancel an in-flight run. Dependency versions also drifted beyond repository requirements (`pandas>=2.2,<3`, `numpy>=1.26,<3`).
- Mitigation committed: concurrency now has `cancel-in-progress: false`; CI installs the repository-compatible ranges `pandas>=2.2,<3` and `numpy>=1.26,<3`. Commit `4654f9648b6c018f5d148231e3ce7a8b88a6da4d`.
- This is a targeted CI reliability fix; no production pipeline or strategy logic changed. A new run was not yet returned by the commit-workflow-run lookup at the time of this ledger update. CI runtime remains NOT_VERIFIED.
- Updated progress: cancellation diagnosis 100%; mitigation commit 100%; rerun result pending; actual NSE artifact integrity audit 0%; replay 0%; final acceptance BLOCKED.


## 2026-11-16 — Research CI PASS + actual 200-session raw/processed artifact reconciliation
### CI evidence
- PR workflow Run #40: ID `43748065772`, conclusion SUCCESS; job `research-unit-tests` ID `132915699706` SUCCESS.
- Job log explicitly reports `Ran 50 tests in 0.094s` and `OK`. This includes the five new raw/processed integrity audit tests, forward-outcome integrity tests, cost-aware replay tests, and existing NIC concordance tests.
- Run URL: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/43748065772
### Actual raw archive artifact
- Located successful NSE raw backfill Run #25: ID `43746369460`; merge job ID `132911365036` SUCCESS; all 21 bounded shard acquisition jobs shown SUCCESS.
- Downloaded artifact `nse-200-session-raw-archive-25`, artifact ID `14174496957`, size 26,279,303 bytes. GitHub artifact digest and independently computed ZIP SHA-256 both equal `8bd3b32e9efb1ae39086b1fe5901307e17d5f8eb245e615f82c2beb1b7d2f308`.
- Independently inspected archive and embedded `qa/raw_archive_manifest.json`: status PASS, exactly 200 raw Bhavcopy files / 200 distinct dates, 2026-01-21 through 2026-11-13; 500,733 EQ rows; 2,997 unique symbols; all 200 per-file SHA-256 values and manifest row counts/date fields matched; duplicate raw SYMBOL/DATE key rows = 0.
### Processed + signals/replay artifact
- Downloaded successful cutoff-safe replay Run #21 artifact `v11-3-cutoff-safe-replay-21`, artifact ID `14174526631`; GitHub digest and independently computed ZIP SHA-256 both equal `69494bd25d688f7aa48a30f969f154f5f13229b19cac483deb5d5c8077c6573b`.
- Processed input `data/processed/nse_eq_200_sessions.csv` SHA-256 `8c433c8163dd5a52faf02ffe29e77571043c5791716c65d8c04cfca98ee857b1`. Independently compared all raw EQ SYMBOL/DATE keys against processed dataset: raw rows 500,733; processed rows 500,733; unique symbols 2,997 each; sessions 200 each; duplicate keys raw=0 / processed=0; missing raw-to-processed keys=0; extra processed keys=0; missing/extra session dates=0. Raw-to-processed key reconciliation PASS for this exact artifact pair.
- Historical signal file SHA-256 `0e57446e98c372fb832bcfa5a4957791142e88a8f10bacc04e3dc61a945a0df3`; 5,880 rows; 196 cutoff dates; exactly 30 rows per cutoff; 0 duplicate cutoff/symbol keys; every signal symbol/cutoff existed in processed input. This is key-presence provenance only, not full feature look-ahead proof.
- Cost-aware trade ledger: 17,640 rows; zero duplicate cutoff/symbol/target/horizon keys. Embedded independent replay audit says PASS, blockers empty, execution reconciliation errors=0, net arithmetic errors=0, exclusion policy errors=0.
- Performance evidence is not a profitability PASS: gross target hit rates were 12.87% (5%/H+1), 9.04% (10%/H+3), 2.83% (20%/H+5); mean net returns after 0.22 percentage-point round-trip cost were -0.813%, -0.877%, -0.926% respectively. Median net returns were -1.669%, -3.220%, -3.220%. Slippage not modelled. This historical research-only adapter does not invoke the production selector or production RANKING_SCORE.
- Historical calibration labels/score construction and strict no-lookahead provenance still require code-level review against the exact signal generation commit. The separate previously identified H+3/H+5 walk-forward label defect remains NOT_VERIFIED until corrected labels are regenerated and independently audited; do not substitute this artifact's simulation outputs for that separate acceptance gate.
### Current state
- PASS: 50-test research CI; raw archive per-file hashes/date/row checks; raw-to-processed exact SYMBOL/DATE key reconciliation for the exact two artifacts above; basic signal cutoff-key presence; independent replay arithmetic reconciliation.
- NOT_VERIFIED: complete calibration-label no-lookahead audit; rerun on corrected forward outcome labels; current-main production collector artifact pairing; price-band/circuit execution; slippage and portfolio sizing/drawdown.
- BLOCKED: final paper acceptance / claim of profitable scanner.
- Next step: inspect exact signal-generation source and prove calibration uses only fully matured observations available at each cutoff; then bind the exact processed/signal/replay artifacts to their producing commit and regenerate the H+3/H+5 corrected event labels. Do not repeat the raw-to-processed audit for this exact artifact pair.


## 2026-11-16 — Historical calibration independent recomputation + timestamp semantic audit
### Exact source/artifact reviewed
- Source generation run: #21, ID `43746369505`, commit `2315455ae6e7e98e6a80e95d8d3aa4cf68bf6919`; workflow `.github/workflows/v11_3_historical_signals_research.yml`; successful job `132910523067`.
- Generator source: `pipeline/v11_3_historical_signals_research.py`; blob SHA `(source blob verified in GitHub during audit)`; feature helper source `pipeline/walk_forward_backtest.py`, blob SHA `d085f7a2d35a88b4c4eaba65144a429a06961b09`.
- Artifact `v11-3-cutoff-safe-replay-21`, ID `14174526631`, SHA-256 `69494bd25d688f7aa48a30f969f154f5f13229b19cac483deb5d5c8077c6573b`.
- Processed input SHA-256 `8c433c8163dd5a52faf02ffe29e77571043c5791716c65d8c04cfca98ee857b1`; calibration audit CSV 500,733 rows; signal CSV 5,880 rows.
### Independent calibration reconstruction — PASS for this exact artifact
- Rebuilt next-3-global-session HIGH excursion labels directly from processed OHLC, requiring the symbol to have observations on each of the next three global sessions.
- Reconstructed each cutoff's eligible training population using only label cutoff sessions <= current cutoff index - 3.
- Compared expected state sample counts and H+3 >=10% hit rates against every audit row; 489,756 available/unknown state-row checks; mismatches = 0.
- Independently recomputed calibration score `clip(50 + 50 * state_hit_rate / max_eligible_state_hit_rate, 0, 100)`; 489,756 available rows, mismatches = 0; max absolute floating-point difference 4.27e-14.
- Joined all 5,880 selected signals to their audit rows; missing matches = 0; calibration sample/rate/score mismatches = 0.
- Source review: `add_features()` and `add_tomorrow_features()` use current/prior OHLCV, rolling/EMA, and same-date cross-sectional values; `add_tomorrow_features` does not shift from future rows despite its name. Calibration labels are created separately and only used after three global sessions mature. No direct feature look-ahead found in the inspected generator/helper paths.
### Timestamp semantics — BLOCKER / NOT PASS
- All 5,880 signal rows set `SIGNAL_TIMESTAMP` to `pd.Timestamp(cutoff_date).isoformat()`, yielding `YYYY-MM-DDT00:00:00` for every signal.
- However, the generator's features include that cutoff session's OHLCV, including same-day close/high/low/current volume. The exact data availability time is therefore not midnight. The input only supplies a trading date; no verified exchange publication/close timestamp is recorded.
- Do not fabricate a clock time. The timestamp is semantically false/misleading and can imply look-ahead/chronology errors. Treat all 5,880 `SIGNAL_TIMESTAMP` fields as NOT_VERIFIED; the date-only `CUT_OFF` remains the valid as-of key. The replay ledger currently also copies cutoff midnight into its `SIGNAL_TIMESTAMP`; same correction needed there.
- Required repair: retain `CUT_OFF` as date-only as-of date, add/use an explicit date-only `SIGNAL_AS_OF_DATE` if needed, and leave exact `SIGNAL_TIMESTAMP` null unless an official source proves actual publication/availability time. Add regression tests that reject midnight-as-observed-time and ensure replay preserves null timestamp while using CUT_OFF for execution.
### Status / next step
- PASS: independent H+3 calibration sample/rate/score reconstruction; signal-to-audit mapping; source-level review found no direct future feature shift in inspected functions.
- NOT_VERIFIED: actual exact intraday information-availability timestamp; historical signal timestamp semantics.
- BLOCKED: strict end-to-end no-lookahead acceptance until timestamp schema is corrected and CI/artifact regenerated. H+3/H+5 separate walk-forward label defect remains unresolved.
- Next task: research-only timestamp semantic repair in the historical signal generator and cost-aware replay output, with targeted regression tests and a short CI run. Do not change production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, or engines A-E.


## 2026-11-16 — Research-only timestamp semantic repair committed; CI pending
- Implemented on source branch `research/nse-raw-manifest-retention-20261115` (PR #37 branch; no merge/production change):
  - Generator now writes `SIGNAL_AS_OF_DATE=YYYY-MM-DD` and leaves `SIGNAL_TIMESTAMP` null because input contains date-only OHLC and no verified publication/availability clock time.
  - Cost-aware replay now carries the same date-only as-of key and null timestamp for both executable and excluded trades. Replay input rejects non-null `SIGNAL_TIMESTAMP` values to prevent reuse of fabricated midnight timestamps.
  - Independent replay audit rejects non-null signal/trade timestamps and checks `SIGNAL_AS_OF_DATE` exactly equals `CUT_OFF`.
  - Added three regression tests: generator timestamp semantics; executable replay preserves null timestamp/date key; excluded replay preserves null timestamp/date key.
- Commits on source branch, in order:
  - generator initial repair `fef1369eebae7ecc4783bbb1bc212e8f5a350ffb`
  - replay propagation and fail-closed input check `01ff9f90e4df859d09e7667361ba48976fcd44d7`
  - three timestamp regression tests `8074b203720a67ea3be5688fd0a5a195d193bd19`
  - independent audit timestamp checks `6d98df1f69eab5b0ece745b3ba285c7d2ff36509`
  - corrected Python quoting in helper `14c23b8933b70d448c81d267a182f68e12947fd7`
  - workflow adds audit script trigger, stable pandas/numpy version ranges and disables in-progress cancellation `63c45276c49534a5e469ba219609d85da4f424c9`
- Workflow retains 10-minute maximum because it also downloads/verifies raw archive, rebuilds the processed dataset and runs historical replay; unit test additions are small. No production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, or A-E production code changed.
- CI has been triggered by the final workflow commit; runtime conclusion must be fetched before claiming PASS. If workflow does not trigger, inspect branch/PR event wiring; do not infer success from commits.
- Prior Run #21's 5,880 historical signals and 17,640 trade rows remain immutable historical evidence with misleading midnight timestamps; they are NOT corrected artifacts and must not be reused for final acceptance. New run must regenerate signals/replay and artifact hashes.
- Status: code edits committed 100%; test source added 100%; independent audit guard added 100%; CI runtime NOT_VERIFIED; regenerated artifact 0%; strict no-lookahead acceptance BLOCKED until CI and new artifact checks pass.


### CI trigger checkpoint — 2026-11-16
- Final workflow commit `63c45276c49534a5e469ba219609d85da4f424c9` triggered PR Run #32, ID `43748694785`, event `pull_request`, head SHA matches the workflow commit, current status PENDING at last poll. No jobs had yet been returned by the jobs endpoint. This is pending, not PASS.
- PR #37 remains OPEN; do not merge. Corrected artifacts and new SHA-256 values are pending the successful run.


### Run #32 live checkpoint — 2026-11-16
- Re-polled GitHub Actions run #32, ID `43748694785`, head SHA `63c45276c49534a5e469ba219609d85da4f424c9`: status IN_PROGRESS; job `historical-signals-and-replay`, ID `132917876701`, IN_PROGRESS.
- Completed steps: job setup, checkout, Python setup. Current step: `Install minimal research dependencies` IN_PROGRESS. Archive download, manifest verification, dataset rebuild, historical signal generation, replay, independent audit, regression tests and artifact upload are still PENDING.
- This is a queue/runtime checkpoint only. No CI PASS, no corrected artifact, no new hashes, and no acceptance promotion. Do not start a duplicate run while this one is active.



## 2026-11-16 — Run #32 corrected timestamp artifact regenerated and independently audited
- GitHub Actions Run #32: ID `43748694785`, workflow job `historical-signals-and-replay` ID `132917876701`, completed SUCCESS. Source head commit: `63c45276c49534a5e469ba219609d85da4f424c9`; PR merge-ref checkout `7cc4c6d96c1f1d4b80270dd27e1c7393f9b01f54`. Run URL: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/43748694785
- All workflow steps SUCCESS: dependency install; download immutable raw archive; raw manifest/session verification; processed dataset rebuild; exact processed-to-raw session-date equality; cutoff-safe historical signal generation; cost-aware H+1/H+3/H+5 replay; independent reconciliation; timestamp/calibration regression tests; artifact upload.
- Source archive used by this run: `nse-200-session-raw-archive-5`, artifact ID `14170166475`; downloaded ZIP digest verified by Actions as `3c15ceb5cd6cb3270515090eb8393d22f8ca609a6032d0d7e128c5b78fb57494`. Embedded manifest: 200 raw files / 200 sessions, 2026-01-21 through 2026-11-13.
- Newly regenerated artifact: `v11-3-cutoff-safe-replay-32`, artifact ID `14175118322`, size 25,817,040 bytes, GitHub artifact ZIP SHA-256 `141109906b276a37b241a13fa583a8b8d732245e8735a93dea25ff0de4426599`, retention through 2027-02-13. Artifact URL: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/43748694785/artifacts/14175118322
- Independent replay audit output: status PASS; blockers=[]; 5,880 signal rows across 196 cutoffs; 17,640 trade rows; 17,023 executable and 617 excluded; execution reconciliation errors=0; net arithmetic errors=0; exclusion policy errors=0. Independent audit SHA-256s: processed input `d046f879b6b35ee2740ff6b721dee4cecc1ff5761ef644d5b399bb80333fb928`; signals `cce0f8039c2c6930022b3f00adb0f08f2dfe7ee0cf701a8e9a8f471066456bcd`; trade ledger `b5d66feef1a2b8901a916c01bba3e96052c10a78fa7596c5587737f943abb1cc`; metrics `e014c90bfe6f994d36402ac6f6eb243db94d67f9f783907f420f8ebcbd16b415`.
- Timestamp semantic repair verified in regenerated outputs: date-only `SIGNAL_AS_OF_DATE`; exact `SIGNAL_TIMESTAMP` remains null; replay propagates null and uses `CUT_OFF` for date-based execution. Seven focused regression tests passed (7/7), including below-minimum sample UNKNOWN, no matured window UNKNOWN, fully matured cutoffs only, empty replay null timestamp, executable replay null timestamp/date-only as-of, and midnight timestamp rejection.
- Performance remains negative after 0.22 percentage-point round-trip cost: +5%/H+1 gross hit 12.87%, mean net -0.813%, median -1.669%; +10%/H+3 gross hit 9.04%, mean net -0.877%, median -3.220%; +20%/H+5 gross hit 2.83%, mean net -0.926%, median -3.220%. This is an integrity/replay PASS, NOT a profitability PASS. Slippage, circuit/price-band feasibility and portfolio sizing/concurrency remain unmodelled or unverified.
- The new artifact supersedes Run #21's timestamp-defective artifact for the corrected research replay. Preserve Run #21 as immutable historical provenance; do not reuse it for final acceptance.
- Status: timestamp code repair 100%; focused regression tests 100% / 7 of 7 PASS; Run #32 workflow 100% SUCCESS; corrected artifact generation 100%; independent replay reconciliation 100% PASS; timestamp semantic gate PASS for this artifact; profitable strategy gate BLOCKED; project-wide Hard Gate and final paper remain BLOCKED pending separate unresolved items (including H+3/H+5 forward-label defect, CORE-672 semantic independence, Macro-Geo/Factor Registry, circuit/slippage and portfolio tests).
- No production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 definitions, engines A-E production code, collector production workflow, or default branch changed. PR #37 remains open/unmerged; PR #38 remains open/draft/unmerged. No paid API or spend.
- Next highest-value task: inspect and correct the separate H+3/H+5 forward-label window defect in `pipeline/walk_forward_backtest.py` in an isolated research-only branch, add exact T+1..T+h maturity and no-partial-tail regression tests, then run a short CI and independently recompute labels. Do not repeat Run #32, timestamp repair, raw archive verification or this replay audit absent new changes.



## 2026-11-16 — H+3/H+5 forward-label defect: isolated research-only correction committed; CI pending
- After Run #32 passed, inspected exact source `pipeline/walk_forward_backtest.py` (prior blob SHA `d085f7a2d35a88b4c4eaba65144a429a06961b09`). Confirmed `shift(-1).rolling(h, min_periods=1).max()` is a trailing rolling window over shifted values, not the exact forward T+1..T+h window for h>1; `min_periods=1` also emits partial-tail outcomes. This invalidates existing H+3/H+5 label values near the cutoff and tail.
- Research-only correction on `research/nse-raw-manifest-retention-20261115`: introduced `_forward_window_max(series, horizon)`, which shifts by one session, reverses for forward rolling, requires `min_periods=horizon`, and restores original order. `future_outcomes()` sorts by SYMBOL/DATE and uses exact T+1..T+h maxima for HIGH and CLOSE. Incomplete future windows remain NaN/UNKNOWN; no partial-tail labels.
- Added three regression tests: H+3 uses exact next-three rows and excludes a later out-of-window spike; H+5 requires all five future rows and leaves all immature tail rows NaN; H+1 HIGH/CLOSE labels use only the next session and final row remains NaN.
- Commits: source fix `6c2e90248b556da11ce8d7b1075749270b60700a`; tests `e16b742c8d5ee19e14f2cbf2e70ce3f1bd7358cd`; workflow trigger path includes `pipeline/walk_forward_backtest.py`, commit `ec95660f8e559346cd8d52103af2e5c6e6c3893f`.
- CI lookup for final workflow commit `ec95660f8e559346cd8d52103af2e5c6e6c3893f` returned no workflow run at first poll. Runtime validation is PENDING / NOT_VERIFIED; do not claim PASS. No duplicate run dispatched.
- Scope: code correction 100%; focused tests authored 100%; workflow trigger wiring 100%; CI runtime 0% / pending; corrected H+3/H+5 artifact regeneration 0%; independent full-dataset label recomputation 0%; acceptance BLOCKED until runtime and artifact verification.
- This correction does not modify production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, engines A-E, collector workflow or production output. PR #37 remains open/unmerged; PR #38 remains open/draft/unmerged.
- Next action: poll for the workflow triggered by the above commit. If it passes, run a separate bounded research-only label rebuild/audit against the exact 200-session artifact and compare every H+1/H+3/H+5 outcome against a direct T+1..T+h reference implementation; retain incomplete tails as UNKNOWN. Do not repeat Run #32 or timestamp repair.



### CI checkpoint — forward-label correction (2026-11-16)
- Located the exact PR workflow run missed by the commit-run wrapper: Run #36, ID `43749155334`, workflow `V11.3 Research Cutoff-Safe Historical Signals + Cost-Aware Replay`, head SHA `ec95660f8e559346cd8d52103af2e5c6e6c3893f`, PR #37. Run URL: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/43749155334
- At direct GitHub REST recheck, run status remained `pending`, conclusion null; jobs endpoint returned an empty list. No test job had started; no runtime PASS/FAIL and no corrected artifact can be claimed.
- Related PR workflows for other changed files did complete SUCCESS (NSE Raw Manifest Official-Source Probe Run ID `43749155298`; NSE Raw Archive Manifest Tests Run ID `43749143112`), but these are not the V11.3 historical-signal/replay workflow and do not validate the modified forward-label code. Do not substitute them as evidence.
- No duplicate run dispatched, no rerun, no production changes. Next action is poll Run #36 until jobs start/complete; then inspect its job log and artifact before accepting the forward-label fix.


## 2026-11-16 — Run #36 H+3/H+5 forward-label runtime validation PASS; artifact hash verified
- Polled the exact previously pending Run #36; no duplicate workflow was dispatched. Final GitHub run status: `completed`, conclusion `success`; run ID `43749155334`; job ID `132919512328`; head SHA `ec95660f8e559346cd8d52103af2e5c6e6c3893f`; URL https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/43749155334.
- All substantive workflow steps completed SUCCESS: immutable raw archive download, manifest/session verification, processed dataset build, exact processed-to-raw session-date equality, cutoff-safe signal generation, cost-aware H+1/H+3/H+5 replay, independent signal/execution/cost/metric reconciliation, cutoff-safe calibration regression tests, and artifact upload. Cleanup steps also completed; job conclusion SUCCESS.
- Artifact: `v11-3-cutoff-safe-replay-36`, artifact ID `14175433267`, size 25,817,040 bytes, retention until 2027-02-13. GitHub-reported digest and independently computed downloaded ZIP SHA-256 both equal `da4243672222fc764214bc8dcc9ef2afe3fbf661724c95f3c09d6581a3bca6e1`. Artifact URL https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/43749155334/artifacts/14175433267.
- Artifact manifest reports 200 sessions (2026-01-21 through 2026-11-13), 500,733 processed rows, 2,997 symbols, 5,880 signals across 196 cutoffs, and timestamp policy: `SIGNAL_AS_OF_DATE` is date-only; `SIGNAL_TIMESTAMP` null because exact official availability time is absent. Independently inspected both signal CSV and trade ledger: all 5,880 signal timestamps and all 17,640 trade timestamps are null; date-only as-of fields are populated and align with CUT_OFF.
- Independently verified all three historical-signal output SHA-256 values and byte lengths against the manifest: signals `cce0f8039c2c6930022b3f00adb0f08f2dfe7ee0cf701a8e9a8f471066456bcd`; coverage `f88fe42aab0965c1d27039baacdb044a213c693d20e01319885ce478185025e7`; calibration audit `8ac7fd3f1c1f7727778603f64d52c89261085ded03c55775f5b8a3356d7af435`. All matched.
- Independent replay audit in artifact: status PASS, blockers empty, 5,880 signals, 17,640 trade rows, 17,023 executable, 617 excluded; execution reconciliation errors=0, net arithmetic errors=0, exclusion-policy errors=0. Independent audit JSON SHA-256 `64068b56e199ebe7250c6376ab942c0ad68c7f95e751f2a3d19f76f49dead703`.
- Updated gross target hit rates and cost-adjusted results remain economically negative: +5% H+1 gross hit 12.87%, mean net -0.813%, median -1.669%; +10% H+3 gross hit 9.04%, mean net -0.877%, median -3.220%; +20% H+5 gross hit 2.83%, mean net -0.926%, median -3.220%. Slippage not modelled; circuit/price-band feasibility and portfolio sizing/concurrency remain unverified. Integrity PASS is not profitability PASS.
- Inspected corrected `pipeline/walk_forward_backtest.py` at head SHA: `_forward_window_max` shifts one row forward, reverses, applies `rolling(window=horizon,min_periods=horizon)`, then restores order; `future_outcomes` applies it to HIGH_PRICE and CLOSE_PRICE. Separately checked a deterministic six-value reference sequence for H+1/H+3/H+5: exact T+1..T+h maxima matched and incomplete tails were NaN. This is a focused formula sanity check, not yet a full 200-session independent per-row label recomputation.
- Status update: Run #36 runtime 100% PASS; corrected full 200-session artifact generation 100%; artifact download/hash verification 100%; artifact timestamp semantics 100% PASS; independent replay reconciliation 100% PASS; forward-label full-dataset independent recomputation remains NOT_DONE (0%); project-wide hard gate and final research paper remain BLOCKED on separate Macro-Geo/Factor Registry, CORE-672 semantic independence, slippage/circuit/portfolio and other acceptance requirements.
- No production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 definitions, engines A-E production code, collector workflow, or main branch changed. PR #37 remains open/unmerged; PR #38 remains open/draft/unmerged. No paid APIs/spend.
- Next highest-value task: perform the missing independent full-dataset H+1/H+3/H+5 label recomputation from the immutable processed input, comparing exact forward windows and incomplete-tail/missing-session behavior against the generated calibration labels. Do not repeat timestamp repair, raw archive verification, or Run #36.


## 2026-11-16 — Independent full-dataset forward-label recomputation PASS (Run #36 artifact)
- Completed the next acceptance task without rerunning CI or repeating timestamp/raw-archive checks. Used the downloaded Run #36 artifact `v11-3-cutoff-safe-replay-36` (artifact SHA-256 `da4243672222fc764214bc8dcc9ef2afe3fbf661724c95f3c09d6581a3bca6e1`) as the immutable input.
- Independently recomputed exact per-symbol forward HIGH and CLOSE maxima for H+1, H+3, H+5 using a direct slice/reference implementation over all 500,733 rows and compared against the corrected reverse-rolling implementation from `pipeline/walk_forward_backtest.py` at commit `ec95660f8e559346cd8d52103af2e5c6e6c3893f`.
  - H+1 HIGH/CLOSE: 497,736 valid rows each; 2,997 incomplete symbol tails; NaN pattern identical; 0 mismatches; max absolute difference 0.
  - H+3 HIGH/CLOSE: 491,746 valid rows each; 8,987 incomplete tails; NaN pattern identical; 0 mismatches; max absolute difference 0.
  - H+5 HIGH/CLOSE: 485,762 valid rows each; 14,971 incomplete tails; NaN pattern identical; 0 mismatches; max absolute difference 0.
  - No partial-tail labels emitted by the corrected helper. The check confirms exact next h observed rows per symbol; it does not establish exchange price-band/circuit execution feasibility.
- Separately reconstructed the historical calibration label pipeline independently from the same processed dataset: assigned global session indices, required the symbol to have a row on each of the next 3 consecutive global sessions, formed max HIGH over those sessions, computed the >=10% excursion label, matured only labels with SESSION_IDX <= cutoff_idx-3, grouped by STATE, applied minimum sample threshold 100, and independently reconstructed calibration sample count, hit rate and calibration score for every row.
  - 500,733/500,733 rows joined exactly; 489,219 valid H+3 labels and 11,514 invalid/missing-session labels.
  - Across 489,756 non-null calibration comparisons: sample-count mismatches 0; hit-rate mismatches 0 (max absolute diff 9.72e-17); calibration-score mismatches 0 (max absolute diff 1.43e-14); null-pattern equality PASS.
- This is an independent full-dataset label/calibration integrity PASS, not a profitability PASS. The cost-aware returns remain negative as recorded in the Run #36 entry. H+3 calibration label policy is stricter than the generic per-symbol forward-window helper: it explicitly requires the next three global sessions, preserving UNKNOWN for missing sessions.
- Progress: H+1/H+3/H+5 exact forward-window recomputation 100% PASS; H+3 global-session calibration-label recomputation 100% PASS; calibration maturity/sample/score reconciliation 100% PASS; Run #36 runtime/artifact validation 100% PASS. Overall project hard gate/final paper remain BLOCKED by independent outstanding Macro-Geo/Factor Registry, CORE-672 semantic independence, circuit/slippage/portfolio and final acceptance requirements.
- No production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, engines A-E production code, collector workflow, or main branch changed. PR #37 remains open/unmerged; PR #38 remains open/draft/unmerged. No paid APIs/spend.
- Next highest-value work: audit the research adapter's feature/score mapping and CORE-672 semantic independence against the declared 56x12 contract, without changing production selector or RANKING_SCORE; separately retain Macro-Geo/Factor Registry as an unresolved blocker. Do not repeat this forward-label recomputation, Run #36, timestamp repair, or raw archive verification absent new changes.


## 2026-11-16 — CORE-672 independent semantic audit: implementation gap confirmed (read-only)
- Inspected exact source on branch `research/nse-raw-manifest-retention-20261115`: `pipeline/diagnostics_672.py`, blob SHA `af0a8ddc17d72024509167533585713600a4b845`. No code, production file, selector, ranking, engine, dataset or workflow was changed.
- Confirmed 56 Step names and 12 Filter names are declared and nested loops emit 672 named columns, but the Filter variable is used only to construct the column name; it is never used in the calculation. Therefore each Step's 12 Filter outputs are identical by construction. This is a structural 672-column matrix, not 672 independently evaluated diagnostics.
- Most Steps use the same candidate-level proxy: mean of ENERGY, LEAD_TIME and min(RVOL20*25,100), classified with one fixed state() threshold pair (60/40). The eight explicitly named technical Steps also call the same state(base), functionally identical to the generic else branch. Thus many unrelated macro/sector/price/event/global-theme labels are not backed by Step-specific evidence.
- Special branches also repeat one value across all 12 Filters: one aggregate FII/DII scalar, India VIX percentChange vs 10, and geopolitical news article_count vs 40. Five catalyst/event/earnings Steps are hard-coded UNKNOWN; three live/progression/reversal Steps are hard-coded UNKNOWN.
- `NOT_APPLICABLE` is declared in STATES but no code path emits it; state() emits only POSITIVE/NEGATIVE/UNKNOWN. The report's 672 count is only a named-column count and does not test semantic independence or provenance.
- Audit report committed separately: `docs/CORE_672_INDEPENDENT_SEMANTIC_AUDIT_20261116.md`, commit `4ff0f81a6a32e1c0426b2645d46369b0e524b175`, on research branch `research/nse-raw-manifest-retention-20261115`. This report records F1–F5, evidence, acceptance matrix and repair plan. Status: static source audit 100%; CORE-672 acceptance BLOCKED; runtime candidate-dataset correlation audit 0%; Step×Filter evidence registry 0%; repair/tests 0%.
- Research impact: do not treat CORE-672 scores/coverage as 672 independent confirmations; any downstream aggregation may overcount repeated evidence. Do not infer all engines or entire project invalid; this finding is scoped to this diagnostics generator. UNKNOWN remains UNKNOWN; do not relabel as PASS.
- Next action: build a read-only, source-backed Step×Filter evidence registry and runtime duplication/coverage audit using the actual candidates input and context files, without changing production. Any repair requires explicit approval and must be isolated; no PR merge or production change.


## 2026-11-16 — CORE-672 Step×Filter Evidence Registry and downstream-consumer audit (read-only)
- Reused the already-recorded runtime duplication result from artifact 14151241008; did not rerun that audit. Existing evidence: 672 columns × 2,994 rows, only 3 unique full-column state vectors (540 columns in one vector, 120 in a second, 12 in a third); 132 columns constant UNKNOWN. This is a prior verified artifact result, not a newly regenerated measurement.
- Re-fetched exact `pipeline/diagnostics_672.py` from branch `research/nse-raw-manifest-retention-20261115`, blob SHA `af0a8ddc17d72024509167533585713600a4b845`. Parsed the source declarations directly: 56 Steps and 12 Filters; generated 672 explicit registry cells. Registry file: `docs/CORE_672_STEP_FILTER_EVIDENCE_REGISTRY_20261116.csv`; commit `af21723ee05b897209e8d880d01744c310ba97e7`.
- Each registry cell records the observed source/field, actual transformation, threshold/freshness status, applicability/missing-data behavior and filter-logic status. Where source code does not define unique Step×Filter evidence, the registry explicitly marks it NOT_IMPLEMENTED / BLOCKED; no missing source mapping was invented. All 672 cells are NOT_ACCEPTED because the Filter dimension is unused by the implementation, even where a Step has a special branch.
- Downstream consumer audit: inspected `pipeline/final_selection.py` (blob SHA `8bf216c866030d92f8066e9183c9636880577910`). It checks only whether `outputs/diagnostics/diagnostics_672.csv` exists and adds blocker `672_DIAGNOSTIC_ENGINE_OUTPUT_MISSING` if absent. It does not load, aggregate, score, or inspect any D01–D56 diagnostic column. Repository code search for `D01_FRESHNESS`, `D56_PATH`, and `diagnostics_672.csv read_csv` found no other direct column consumer; this is bounded to accessible indexed code/search results, not a mathematical proof that no indirect/external consumer exists.
- Consequence: current final-selection readiness gate validates file presence, not 672-cell semantic coverage or quality. This does not change ranking or selection; it is a governance/acceptance gap.
- Runtime evidence and static source evidence are separate: prior artifact runtime duplication remains verified; new registry is source-derived. No candidate/context files were rerun because no fresh candidate/context artifact was retrieved in this task. No new runtime dataset correlation/coverage result is claimed.
- Progress: prior runtime duplication evidence reuse 100%; exact source/step/filter extraction 100%; 672-cell registry generation 100%; final-selection consumer inspection 100%; direct downstream column-consumer search 100% (bounded search); new runtime replay 0% / NOT RUN; repair/tests 0% / NOT AUTHORIZED; CORE-672 acceptance BLOCKED.
- No production code, dataset, selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 definitions, engines A–E, collector workflow or default branch changed. No PR merged. No paid APIs or spend.
- Next step: user-approved research-only design of independently testable evidence predicates and data contracts for each cell; do not implement in production until explicit approval.


## 2026-11-16 — CORE-672 FII/DII source-schema mismatch isolated; contract/test spec committed (read-only)
- Reused the existing 672-cell registry and semantic audit; did not rerun the 672-column runtime correlation audit.
- Inspected exact source blobs: `collector/context_data.py` `f38e17979774d1439eea79e4dc7728ba92a790d1`; `pipeline/diagnostics_672.py` `af0a8ddc17d72024509167533585713600a4b845`; `pipeline/risk_modifier.py` `4115a1247992ef8a075b2fd247efb9ce8f8663f6`. Collector emits FII/DII rows with `group`, `date`, `net_value`; CORE-672 diagnostic reads `fii_net` and `dii_net`. This is a deterministic schema mismatch. The risk modifier consumes the collector schema but uses a separate first-20-row sum; that is not proof of the intended CORE-672 aggregation rule.
- Source-level consequence: the diagnostic's FII/DII list comprehensions find no populated fields in the collector-shaped records; aggregate values become NaN and the branch substitutes zero before classification, resulting in UNKNOWN under the current state thresholds. This is source-derived analysis, not a fresh runtime measurement.
- Created `docs/CORE_672_FII_DII_CONTEXT_CONTRACT_TEST_SPEC_20261116.md`, commit `150e8bbaffbf7c8be82ac5d89a5a4d672123ef9c`, branch `research/nse-raw-manifest-retention-20261115`. It records the exact schema mismatch, canonical input fields, fail-closed requirements, 12 regression-test cases, additional CORE-672 tests, acceptance gates and scope protections.
- Deliberately did not choose latest-date vs rolling-window aggregation, missing-side substitution, or freshness limits: current source does not establish these policies. Implementation must wait for explicit policy approval; do not silently copy risk_modifier's 20-row sum.
- Progress: source retrieval 100%; schema comparison 100%; mismatch classification 100%; regression-test specification 100%; aggregation policy BLOCKED; implementation 0%; regression execution 0%; CORE-672 acceptance BLOCKED.
- No production code, collector, diagnostic generator, risk modifier, dataset, selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 definitions, engines A–E, workflow or default branch changed. No CI run dispatched; no PR merged; no paid API/spend.
- Next highest-value task: after policy approval, implement a small research-only adapter for the existing collector schema and run only the focused FII/DII contract tests; then inspect a real archived context artifact before considering any wider runtime audit.


## 2026-11-16 — FII/DII runtime context artifact availability audit (read-only)
- Reused the already-inspected collector and workflow sources; did not repeat the schema-mismatch analysis. Exact blobs: `collector/context_data.py` `f38e17979774d1439eea79e4dc7728ba92a790d1`; `.github/workflows/nse_collector.yml` `96a714e7e74aa9d09b43f74facc758f358fd3124`. Workflow includes `data/context/` in its artifact upload paths and invokes the context collector; this is expected-output configuration, not evidence of a specific successful output.
- Downloaded existing replay artifact ID `14175433267` (known Run #36 / run ID `43749155334`). ZIP size 25,817,040 bytes; independently recomputed SHA-256 `da4243672222fc764214bc8dcc9ef2afe3fbf661724c95f3c09d6581a3bca6e1`, matching the previously recorded artifact hash.
- Inspected all 13 ZIP entries. Found the raw archive manifest and historical signal manifest, but no `data/context/` directory, no `market_context.json`, and no FII/DII payload. This is a finding only about artifact `14175433267`; it does not prove other collector workflow artifacts lack context.
- Audit document: `docs/CORE_672_FII_DII_RUNTIME_CONTEXT_ARTIFACT_AUDIT_20261116.md`, commit `11b53ebeb2f2f91293ca85f7ef08780cf5fe0193`, branch `research/nse-raw-manifest-retention-20261115`.
- Progress: source/workflow reinspection 100%; artifact download/hash verification 100%; ZIP inventory/context-presence check 100%; all-workflow artifact discovery NOT_COMPLETE; real context runtime schema validation 0% / NOT_VERIFIED; aggregation policy BLOCKED; adapter/tests 0% / NOT_STARTED.
- Next: inspect artifact inventories for the actual collector workflow runs and retrieve a context-bearing artifact if one exists. Do not rerun the full collector workflow merely to recreate context; first check existing artifacts. If none retained, design a bounded research-only retention test.
- No production code, workflow, dataset, selector, `RANKING_SCORE`, `+1 PRESSURE_FADE`, CORE-672 definitions, engines A–E, default branch or PR state changed. No CI dispatched, no PR merged, no paid API/spend.


## 2026-11-16 — Real FII/DII runtime context recovered and verified (Run #161)
- Located an actual successful Collector workflow artifact, closing the previous discovery gap for one run. Workflow `.github/workflows/nse_collector.yml`, workflow ID `373721663`; Run #161 / ID `43696699698`; branch `main`; head commit `cc4d397f25e735e9f7b63d2da74b40baff1aaab9`; completed success from `2026-11-15T08:54:51Z` to `2026-11-15T09:01:03Z`.
- Artifact ID `14154408713`, name `precision-wires-adaptive-161`, size 61,626,954 bytes, created `2026-11-15T09:00:59Z`. Downloaded ZIP independently SHA-256 verified: `b4623c28d30d04a73d21eb67662caeeab56123b2eba637d9eb652225df0305e8`. ZIP contains 25 entries and actual `data/context/market_context.json` (5,973 bytes), whose SHA-256 is `83c811be558501bbfed7b2104658f2d3796bfd506b37149800a730384bed5dc8`.
- Fetched `collector/context_data.py` at exact run head commit; blob SHA `f38e17979774d1439eea79e4dc7728ba92a790d1`, same source blob as prior source audit.
- Parsed actual JSON successfully. `generated_at=2026-11-15T08:59:46.921319+00:00`; source provenance `NSE /api/fiidiiTradeReact (category-normalized)`; two rows, one DII and one FII/FPI, both date-only `13-Nov-2026`; coverage metadata rows=2, fii_rows=1, dii_rows=1, fii_dates=1, dii_dates=1. DII buy/sell/net=11745.95/13999.53/-2253.58; FII/FPI=18339.57/12603.02/5736.55. Actual fields: `category`, `group`, `date`, `buy_value`, `sell_value`, `net_value`. Both groups recognized, finite numeric net values, one row per group/date, no duplicate group/date pair, no collector error keys.
- This proves collector-shaped runtime schema and provenance for Run #161 only. It does not prove a rolling history, a correct aggregation window, sign/unit policy, missing-side rule, freshness limit, or any CORE-672 POSITIVE/NEGATIVE output. `generated_at` is generation time, not an intraday market observation timestamp. Do not infer a broader historical retention guarantee from one artifact.
- Verification report: `docs/CORE_672_FII_DII_ARCHIVED_RUNTIME_CONTEXT_VERIFICATION_20261116.md`, commit `dcca451010228d11ab10f7d6c902b5dd0d513fe6`, branch `research/nse-raw-manifest-retention-20261115`.
- Progress: Run discovery 100%; artifact retrieval 100%; ZIP SHA verification 100%; context extraction and SHA verification 100%; JSON/provenance/schema/row structure validation 100% for this artifact; runtime schema evidence now VERIFIED_FOR_RUN_161_ONLY; aggregation/freshness policy BLOCKED; adapter 0%; focused regression execution 0%; CORE-672 semantic acceptance BLOCKED.
- Next: create a minimal research-only adapter contract test pinned to this real archived payload, without synthetic market rows and without emitting a trading state until aggregation/freshness policy is approved.
- No production code/workflow/data/selector/`RANKING_SCORE`/`+1 PRESSURE_FADE`/CORE-672/engines A–E/default branch/PR state changed. No CI dispatched, no PR merged, no paid API/spend.


## 2026-11-16 — Run #161 provenance-pinned FII/DII research contract tests PASS
- Re-downloaded the actual Run #161 collector artifact (ID `14154408713`) and independently recomputed hashes: ZIP SHA-256 `b4623c28d30d04a73d21eb67662caeeab56123b2eba637d9eb652225df0305e8`; member `data/context/market_context.json` SHA-256 `83c811be558501bbfed7b2104658f2d3796bfd506b37149800a730384bed5dc8`. Both match the prior verification report. Actual payload still has exactly two rows, one per `FII_FPI` and `DII`, date-only `13-Nov-2026`.
- Added research-only provenance fixture `tests/research_fii_dii_run161/fixtures/run161_fii_dii_excerpt.json`. It is a literal excerpt of the two real archived rows, explicitly labelled as an excerpt and pinned to Run ID, artifact ID, ZIP hash and member hash; it is not synthetic market data.
- Added isolated test module `tests/research_fii_dii_run161/test_contract.py`. Its validator checks source provenance, generation timestamp, date-only observation, recognized groups, finite numeric `net_value`, and duplicate group/date rejection. It confirms there is no dependency on legacy `fii_net`/`dii_net` fields and does not zero-fill a missing category. The return status is only `SCHEMA_VALIDATED_ONLY`; it cannot emit POSITIVE/NEGATIVE or calculate an aggregate.
- Local execution: `python -m unittest -v`; 10/10 tests PASS in 0.001 sec. Test cases cover real fixture schema, legacy-field absence, one-sided data without zero fill, duplicate rows, unknown group, null/string/NaN/infinite/boolean net values, missing provenance, timestamp-shaped/invalid date, missing generated_at, and absent/empty rows. No GitHub Actions run was dispatched.
- Research branch `research/nse-raw-manifest-retention-20261115` commits: fixture `8cd945b42dec13b830fb8875452d44be59082cb1`; tests `5d47dd5619d5cebfbfbadb4891c6f1726e6a0ae0`; report `52c3824c403afa88b02c30b3bfd44a8be2f69927`. Report path: `docs/CORE_672_FII_DII_RUN161_RESEARCH_REGRESSION_20261116.md`.
- Defined work package progress: artifact provenance recheck 100%; fixture creation 100%; research-only validator/tests 100%; local regression execution 100% PASS. Aggregation period, sign/units, freshness threshold and missing-side policy remain BLOCKED; production adapter/integration 0% / NOT_AUTHORIZED; CORE-672 semantic acceptance BLOCKED. One-date fixture does not establish rolling coverage.
- No production code, collector, workflow, dataset, selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 56×12 contract, engines A–E, default branch, or PR state changed. No CI dispatch, merge, paid API or spend. Preserve UNKNOWN as UNKNOWN.
- Next highest-value task: obtain explicit policy approval for the FII/DII aggregation period, sign/units interpretation, freshness rule and missing-side behavior before writing any state-producing adapter. Do not repeat this fixture/hash/test run unless its source artifact or test code changes.


## 2026-11-16 — FII/DII official-source policy evidence matrix and segment-scope reconciliation
- Reused the verified Run #161 archive and existing regression fixture; did not rerun schema tests or repeat artifact hashing. Re-fetched exact collector source `collector/context_data.py` blob `f38e17979774d1439eea79e4dc7728ba92a790d1`, diagnostics source blob `af0a8ddc17d72024509167533585713600a4b845`, risk modifier blob `4115a1247992ef8a075b2fd247efb9ce8f8663f6`, and the previously committed contract/verification/regression reports.
- Inspected official NSE FII/DII report page: https://www.nseindia.in/reports/fii-dii . It distinguishes (a) NSE-only Capital Market Segment and (b) combined NSE+BSE+MSEI Capital Market Segment. It labels Buy/Sell/Net values in ₹ Crores. NSE notes FII/FPI same-day activity is compiled from PANs provided by NSDL and is provisional, subject to custodial confirmation/modifications; DII categorization is based on Trading Member trading codes/client-category classification. NSE directs users to NSDL/CDSL for final FII/FPI data.
- Material one-date reconciliation: Run #161 archived values for 13-Nov-2026 (FII/FPI 18,339.57 / 12,603.02 / +5,736.55; DII 11,745.95 / 13,999.53 / -2,253.58) exactly match the official NSE page's combined NSE+BSE+MSEI table. The separate NSE-only table for that date reports different values (FII/FPI 17,376.50 / 12,122.52 / +5,253.98; DII 10,561.32 / 12,532.05 / -1,970.73).
- Consequence: the archived values are consistent with the combined dataset for this date; do not label them NSE-only based solely on the endpoint/source label. Collector source string `NSE /api/fiidiiTradeReact (category-normalized)` does not contain an explicit market-scope field. Exact API-to-table mapping needs a raw API response or official endpoint contract. The one-date match is not proof of endpoint scope across all dates.
- Arithmetic checked: buy minus sell equals net for both archived groups. Thus positive net means buy exceeds sell and negative net means sell exceeds buy in this sample. This supports column arithmetic/sign interpretation only, not a CORE-672 threshold or direction score.
- New evidence matrix: `docs/CORE_672_FII_DII_POLICY_EVIDENCE_MATRIX_20261116.md`, research branch `research/nse-raw-manifest-retention-20261115`, commit `6750197acdc5ee04d023a568d7277546bdaaa4a4`. It separates verified source facts from unresolved decisions: intended market scope, aggregation period/session alignment, provisional vs final FII vintage/revisions, freshness/cutoff, missing-side and duplicate handling, and signal normalization.
- Scoped progress: official NSE source inspection 100%; unit/sign/segment-label evidence extraction 100%; Run #161 one-date table reconciliation 100%; endpoint-to-table scope proof BLOCKED; aggregation/freshness/missing-side policy approval BLOCKED; state-producing adapter 0% / NOT_AUTHORIZED; CORE-672 FII/DII acceptance BLOCKED.
- No production files, collector, workflow, selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 56×12 definitions, engines A–E, dataset, default branch or PR state changed. No CI dispatched, no PR merged, no paid API/spend.
- Next highest-value task: obtain and archive the exact raw `/api/fiidiiTradeReact` response for a known date and compare it against both official NSE table variants; if the API response cannot be retrieved historically, add an explicit unresolved scope field/blocker rather than infer it. Do not repeat the 13-Nov-2026 table comparison or existing regression suite absent new evidence/code changes.


## 2026-11-16 — FII/DII raw API capture access gate (bounded attempt)
- Objective: resolve exact market scope of `https://www.nseindia.com/api/fiidiiTradeReact` by capturing its raw response and comparing same-date official NSE-only and NSE+BSE+MSEI CSVs.
- Reused existing evidence without repeating it: Run #161 artifact ID `14154408713`, run ID `43696699698`, normalized context SHA-256 `83c811be558501bbfed7b2104658f2d3796bfd506b37149800a730384bed5dc8`, collector source blob `f38e17979774d1439eea79e4dc7728ba92a790d1`; prior one-date comparison on 13-Nov-2026 showed archived values match the combined table, not NSE-only.
- Reopened official NSE FII/DII page https://www.nseindia.in/reports/fii-dii . The rendered page explicitly labels two datasets: “on NSE in Capital Market Segment” and “on NSE, BSE and MSEI in Capital Market Segment”, each with its own CSV download control. The page extraction did not expose distinct underlying CSV URLs; both controls resolved to a generic link reference.
- Attempted direct retrieval of `https://www.nseindia.com/api/fiidiiTradeReact` through the available web retrieval channel; it returned inaccessible/internal-error. No raw JSON body, response headers, resolved URL, or official endpoint documentation was obtained. This is an access-channel limitation, not proof that the endpoint is unavailable to the collector.
- Result: API market scope remains BLOCKED. Do not infer API scope from the one-date match alone. Do not label the payload NSE-only solely because the collector's source string contains NSE.
- Created bounded access-gate report: `docs/CORE_672_FII_DII_RAW_API_CAPTURE_ACCESS_GATE_20261116.md`, research branch `research/nse-raw-manifest-retention-20261115`, commit `a6f37ac897a80e668f20163d88fa43b167e1cde1`. It defines the exact evidence needed for a future raw capture: request URL/time, redacted response headers, raw bytes/hash, parsed JSON/hash, both official CSV byte hashes and deterministic row-level reconciliation; secrets/cookies must never be committed.
- Progress: official report page/table labels reconfirmed 100%; direct API retrieval attempted 100% but ACCESS_BLOCKED; raw response bytes/hash 0% / NOT_OBTAINED; official CSV payload hashes 0% / NOT_OBTAINED; API-to-table scope reconciliation BLOCKED; CORE-672 aggregation policy BLOCKED; trading-state adapter 0% / NOT_AUTHORIZED.
- No production code, collector, workflow, dataset, selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 56×12 contract, engines A–E, default branch or PR state changed. No CI, no merge, no paid API/spend.
- Next action: a one-off, manually triggered, research-only capture with NSE session bootstrap and raw-response/official-CSV archival in an isolated environment. If access remains blocked, stop and retain UNKNOWN; do not guess undocumented endpoints or silently alter production collector.


## 2026-11-16 — Isolated NSE FII/DII raw capture utility committed (live capture pending)
- To advance the previously documented ACCESS_BLOCKED gate without changing production, added `tools/research/capture_nse_fii_dii.py` on research branch `research/nse-raw-manifest-retention-20261115`.
- Utility design: fetch official report HTML; bootstrap public NSE homepage session; request exact `/api/fiidiiTradeReact`; preserve raw response bytes and separately parsed JSON; download distinct NSE-only and combined NSE+BSE+MSEI official CSVs; compute SHA-256 and write a local manifest. It fails closed with `ACCESS_BLOCKED` when it cannot resolve two distinct CSV links or obtain a required response.
- Added explicit CLI URL overrides for the two CSV controls when page HTML has generic labels. URLs must be on official NSE domains and must differ. Exact URLs must be copied from the two official NSE controls; placeholders must not be used.
- Security: utility does not serialize request cookies/session headers; raw captures remain local and are not automatically committed; no CI, cron, workflow, production pipeline import or scheduled run.
- Utility source commits: initial `079f771384a733dc3a5b2e80170f95dc95b9fa08`; follow-up URL override `73dbd31a378b0f5a9f524527fe54e18212b24f31`, source blob SHA `98882b58a50023a7d170f76b198be204658ded6d`.
- Usage/limitations document: `docs/CORE_672_FII_DII_RESEARCH_CAPTURE_UTILITY_20261116.md`, commit `a7afe6c27252b3e27d77f4b41d303413db8d79c8`.
- Important honesty boundary: the utility has been committed, but Python compile/runtime test and live NSE capture have NOT been executed in this environment. Do not claim capture success, raw response availability, or market-scope reconciliation. Current progress: utility authoring 100%; GitHub source commit 100%; Python compile/runtime 0% / NOT_RUN; live API and CSV capture 0% / NOT_RUN; API-to-table scope reconciliation BLOCKED; production integration 0% / NOT_AUTHORIZED.
- No production files, collector, workflow, dataset, selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 56×12 contract, engines A–E, default branch or PR state changed. No CI dispatched, no PR merged, no paid API/spend.
- Next action: execute this one-off utility in a permitted environment with outbound access; if official page links cannot be extracted, provide the two exact CSV URLs copied from NSE's distinct report controls. Preserve raw bytes/hashes locally and create a redacted evidence report only after inspecting the actual capture. Do not repeat prior one-date reconciliation or regression tests.


## 2026-11-16 — Capture utility executable-quality hardening (tests committed, execution pending)
- Reused the exact committed utility and performed source-level review; did not repeat FII/DII source/schema/one-date audits. Shell attempt to retrieve raw GitHub source for local execution failed with DNS name-resolution error, establishing this environment has no outbound DNS/network. Therefore no claim of Python runtime or live NSE execution.
- Found and fixed two security issues: initial URL validator accepted HTTP and the initial manifest retained query strings in CSV link metadata. Final `safe_nse_url` requires HTTPS, official NSE domain/subdomain, no embedded credentials, and default/443 port; malformed URLs fail closed. `manifest_url` strips query and fragment from manifest URLs. Both CSV overrides must be supplied together.
- Final utility source blob SHA: `b5d59bd284df342927814335ed7e8357f71cf7a0`; hardening commits `9e08de5aef60ae876a1fd91e32d4db7796487485` and `e2876b213826fa951b9cef92c9e1155b1c6da80f`.
- Added offline test file `tools/research/tests/test_capture_nse_fii_dii.py`, commit `66b7330e9b5980c3161f1f75f85eb8c372008a38`. Tests cover official URL allowlist, HTTP/lookalike/credential/port/malformed URL rejection, manifest query redaction, SHA-256 known vector, anchor parsing and file hash/length.
- Updated utility documentation with quality hardening addendum, commit `965af6bc840577813ffed64e61f1bc697e7c301d`.
- Status/progress: source-level quality review 100%; HTTPS/domain/credential/port validation 100% implemented; query redaction 100% implemented; offline tests authored 100%; Python compile and unit-test execution 0% / NOT_RUN due outbound DNS unavailable; live API/CSV capture 0% / NOT_RUN; API market-scope reconciliation BLOCKED. Tests are committed, not PASS until actually executed.
- No production files, collector, workflow, dataset, selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 56×12 contract, engines A–E, default branch or PR state changed. No CI dispatch, no PR merge, no paid API/spend.
- Next action: run `python -m unittest discover -s tools/research/tests -v` and `python -m py_compile tools/research/capture_nse_fii_dii.py` in a permitted Python environment; then run one live capture only after offline tests pass. Do not rerun old FII/DII audits or the one-date table reconciliation.


## 2026-11-16 — Offline test import-path defect corrected; helper harness PASS (bounded)
- Reviewed the committed test module and found its import path pointed one directory above the utility. Fixed `Path(__file__).parents[2]` to `parents[1]`. Commit `b4509318799b72ff23e7ddec5b18111a41dee9c3`; test blob `41be6239d896e1a0c4229fc9e49c0b9d4a9fc80f`.
- Python 3.13.5 and requests 2.32.5 are available in the local container, but DNS resolution to raw.githubusercontent.com fails, so exact committed repository files could not be downloaded for execution.
- Executed a temporary offline harness reconstructed from the committed utility's helper functions and the same seven unit cases. Harness syntax compilation PASS; 7/7 helper tests PASS in 0.002 sec. This is explicitly NOT a run of the exact committed checkout and does not validate the full main() network capture flow.
- Updated utility documentation addendum: `docs/CORE_672_FII_DII_RESEARCH_CAPTURE_UTILITY_20261116.md`, commit `bcaa1c3bc3061c861fd9bcb2d2b83407e51a640e`, blob `36bc7306021a6bd281c7de444d31b38f718a2481`.
- Progress: test import-path defect identified/fixed 100%; bounded helper harness 7/7 PASS; exact repository checkout test execution NOT_VERIFIED; live NSE capture NOT_RUN; market-scope reconciliation BLOCKED. Do not claim full utility test suite PASS.
- No production code, collector, workflow, selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 56×12, engines A–E, default branch or PR state changed. No CI dispatched, no merge, no paid API/spend.
- Next action: run the exact committed branch checkout in a network-enabled GitHub Actions runner or developer environment; only after exact tests pass, attempt a single live NSE capture. Do not repeat prior audits or helper harness unless source changes.

## 2026-11-16 — NSE FII/DII capture utility: exception-message URL redaction
- Further exact-source review found that the capture manifest serialized raw exception messages. Requests exceptions may embed full URLs with query parameters. Changed the error record to retain only exception class plus a fixed safe diagnostic; raw exception text is no longer written.
- Source commit `6eb13368faae01c4b054dcfb6df74d835c25f246`; source blob `534a290ab5ec244150e97cce1b92de9c7076dea5`.
- Utility documentation commit `78e3a117b5fc992eb973b1221bb8775ecc210281`; blob `3e51a54f3ad57b4d3f1b1a8d3ddfec57e79d2b83`.
- Exact committed tests NOT_RUN after this change; helper harness 7/7 from previous iteration is not evidence for this modified source. Live NSE capture NOT_RUN. No production workflow/code, selector, score, pressure fade, CORE-672, engines, or default branch changed.
## 2026-11-16 — Exact test execution blocker: GitHub dispatch capability
- Checked the research branch workflow directory: no dedicated NSE FII/DII capture utility unit-test workflow exists. Available GitHub connector methods support repository/file reads and workflow-run/artifact/log reads, but expose no workflow_dispatch/run-workflow action. Thus I cannot start a new GitHub Actions run from this session. No workflow file was added and no existing workflow/production path was modified.
- Utility documentation updated: commit `59636d586a2455dbd4bab64eeacac5b387225331`; blob `fc76ad7c8d26930749a1736e3a82a95bb5210c95`.
- Exact committed test suite status remains NOT_RUN; live NSE capture NOT_RUN. This is an execution-capability boundary, not a test failure and not a PASS. Next execution requires a user-triggered dedicated test workflow or a network-enabled exact checkout.
## 2026-11-16 — Dedicated manual-only NSE FII/DII unit-test workflow committed
- Added `.github/workflows/nse_fii_dii_capture_unit_tests.yml` to research branch `research/nse-raw-manifest-retention-20261115` in commit `91f116a2dd426427845dd8bf4343cb8c6b0e259f`.
- Workflow is manual-only (`workflow_dispatch`), `contents: read`, concurrency-cancelled, 5-minute timeout, Python 3.12. It installs requests, runs `py_compile` on the utility, then runs only the 7-test offline suite. It does not call NSE, access secrets, upload artifacts, or modify production collector workflows.
- Utility documentation update commit `57b91540102d7b4dbdc8f546760b67bbef8e37f2`; blob `590e21026a94155855b7c7acc18ef419f0beb57e`.
- Workflow is committed but NOT_RUN: connected GitHub capability has no workflow_dispatch action. User-triggered path: Actions tab → NSE FII-DII Capture Utility Unit Tests → Run workflow → choose research branch. Exact test status remains NOT_RUN until run result is available. Live NSE capture remains NOT_RUN.
- No default branch/PR/merge, production workflow, production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, engines A–E, or collector code changed.
## 2026-11-16 — Capture documentation URL-provenance wording corrected
- Clarified that manifest URL provenance is query-free (scheme/host/path); query strings and fragments are intentionally omitted. This aligns the documentation with `manifest_url()` and exception redaction behavior.
- Documentation correction commit `ba30eec75483b243ba35f8bea02e02334c755551`; blob `33cbe371071bb1dc62ea1872b5f6fa8dd65cc48c`.
- Dedicated workflow commit remains `91f116a2dd426427845dd8bf4343cb8c6b0e259f`; committed but NOT_RUN. No claims of exact test PASS.

## 2026-11-16 — Default-branch dispatch enablement for isolated FII/DII tests
- User explicitly authorized adding only the isolated test workflow to the repository default branch; no other production or research files were authorized for modification.
- Repository metadata confirmed default branch is `main`.
- Confirmed the workflow path did not previously exist on `main`; created only `.github/workflows/nse_fii_dii_capture_unit_tests.yml` in commit `1539bba91bb44dadeb46a0f8a7b701a16acf0729`.
- Follow-up hardening commit `5689512b2119a4c3d75a5bd743292616bae97e73` explicitly pins `actions/checkout` to research branch `research/nse-raw-manifest-retention-20261115`. This ensures the manual workflow executes the intended research-branch utility and seven-test suite, not files from `main`.
- Final workflow file was re-fetched from `main`; blob SHA `217daf02687457fda6fb1ceaa2e699c53a70e93e`. Commit diff confirms the follow-up changed only this workflow file (added explicit checkout ref).
- Workflow remains manual-only (`workflow_dispatch`), `contents: read`, concurrency-cancelled, 5-minute timeout, Python 3.12, installs requests, compiles the utility and runs only the named offline unit-test file. No NSE request, secrets, artifact upload, cron, push trigger, or production pipeline integration.
- No other file was changed on `main`; no research source/test/doc file changed in this operation; no PR/merge, production selector, `RANKING_SCORE`, `+1 PRESSURE_FADE`, CORE-672 contract, Engines A–E, collector workflow or dataset changed.
- Status: default-branch workflow installation 100% (verified by fetch); research-branch checkout pin 100% (verified by fetch/diff); exact GitHub Actions execution NOT_RUN; compile NOT_RUN; seven unit tests NOT_RUN; live NSE capture NOT_RUN; API/CSV scope reconciliation BLOCKED.
- Next action: user opens repository Actions → “NSE FII-DII Capture Utility Unit Tests” → Run workflow, selects `main` (workflow file source), then starts it. Workflow itself checks out the pinned research branch. Record run ID, commit SHA, duration, job conclusion and test output only after actual run completion.


## 2026-11-16 — NSE FII/DII capture utility exact GitHub Actions test PASS
- Verified the manually dispatched workflow run from GitHub API and fetched its actual job logs; this is an exact committed research-branch checkout, not the earlier reconstructed helper harness.
- Workflow: `NSE FII-DII Capture Utility Unit Tests`; run number #3; run ID `43834406640`; event `workflow_dispatch`; workflow-source branch `main`; workflow head SHA `5689512b2119a4c3d75a5bd743292616bae97e73`; conclusion `success`; total duration 13 seconds; job `capture-utility-tests` completed success in 9 seconds.
- Job ID `133187345477`. Logs confirm checkout of research branch `research/nse-raw-manifest-retention-20261115`, checked-out source commit `ba30eec75483b243ba35f8bea02e02334c755551`, Python `3.12.16`, requests `2.34.2`.
- Step outcomes: checkout PASS; Python setup PASS; requests install PASS; `python -m py_compile tools/research/capture_nse_fii_dii.py` PASS; `python -m unittest discover -s tools/research/tests -p 'test_capture_nse_fii_dii.py' -v` PASS.
- Exact offline test output: 7 tests ran in 0.001s, all OK:
  1. `test_anchor_parser_preserves_label_and_href`
  2. `test_https_official_hosts_allowed`
  3. `test_invalid_port_does_not_raise`
  4. `test_manifest_url_drops_query_and_fragment`
  5. `test_non_https_and_non_official_hosts_rejected`
  6. `test_sha256_known_vector`
  7. `test_write_bytes_returns_hash_and_length`
- Evidence URLs: run `https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/43834406640`; job logs retrieved from GitHub Actions job `133187345477`.
- Status: exact Python compile PASS; exact committed seven-test suite PASS; manual workflow PASS. This validates only tested helper/security/file-write behavior and Python syntax. It does NOT validate live NSE API access, CSV retrieval, response schema, raw capture integrity in a live session, market-scope reconciliation, rolling FII/DII history, CORE-672 mapping or production integration.
- Next highest-value task: perform one controlled live NSE research-only capture from the exact tested research branch, first checking whether official page HTML exposes two distinct CSV control URLs. If not, require the exact two URLs copied from the official NSE page; do not guess. Keep raw captures local, hash them, redact secrets, and preserve UNKNOWN if access is blocked. Live capture remains NOT_RUN.
- No production collector, workflow, dataset, selector, `RANKING_SCORE`, `+1 PRESSURE_FADE`, CORE-672 contract, Engines A–E, or default branch code beyond the already authorized isolated workflow file was changed by this test run.


## 2026-11-16 — Library FII/DII CSV review (user-supplied files)
- User stated the two NSE FII/DII CSV files had been saved in ChatGPT Library. Located and read:
  - `/PRECISION-WIRES/NSE-FII-DII/fii-dii-nse-latest.csv` (218 bytes; file ID `file_000000006a3c82119beb9a4557318937`)
  - `/PRECISION-WIRES/NSE-FII-DII/fii-dii-combined-latest.csv` (218 bytes; file ID `file_0000000077ec8211afe18d751021a9c6`)
  - Duplicate copies also exist at Library root with alternate names; their contents match the corresponding folder files. No need to process duplicate copies again.
- Both files contain two rows dated `13-Nov-2026` and columns CATEGORY, DATE, BUY VALUE (₹ Crores), SELL VALUE (₹ Crores), NET VALUE (₹ Crores).
- NSE-only file values:
  - DII buy 10,561.32; sell 12,532.05; net -1,970.73.
  - FII/FPI buy 17,376.50; sell 12,122.52; net +5,253.98.
- Combined NSE+BSE+MSEI file values:
  - DII buy 11,745.95; sell 13,999.53; net -2,253.58.
  - FII/FPI buy 18,339.57; sell 12,603.02; net +5,736.55.
- Raw file SHA-256 (computed from materialized original bytes):
  - NSE-only: `b733444b5a846abb672226bc96448bc0baea2da0ad15fe810207fbe93aad7f18`
  - Combined: `2697546fa012f4c08449b37a3eb7d0f8298f296c25fd8ce4b7ca134c37999eb2`
- Scope comparison confirms these are distinct series; combined values must not be substituted for NSE-only values. These are user-provided Library files; no source URL, download timestamp, original HTTP response headers, or capture manifest was included with the files. Therefore content/hash verification is PASS, but official-source provenance/live capture verification remains UNKNOWN/NOT_VERIFIED.
- No repeated analysis of duplicate root copies beyond confirming content equality; no market history inferred from these single-date rows. These files alone do not resolve the CORE-672 `fii_net`/`dii_net` aggregation or freshness policy.
- Status: locate/read files 100%; schema/date/value extraction 100%; raw-byte SHA-256 100%; official source URL/provenance verification NOT_VERIFIED; live API capture NOT_RUN; rolling history NOT_AVAILABLE.


## 2026-11-16 — FII/DII official CSV URL discovery follow-up
- Reopened the exact capture utility source `tools/research/capture_nse_fii_dii.py` on `research/nse-raw-manifest-retention-20261115`. Its current contract correctly fails closed unless it resolves two distinct official CSV URLs, either from unambiguous report-page anchors or as a pair of exact user-copied URLs. It also records query-free URL provenance and never serializes exception text that could leak URL tokens.
- Rechecked the official NSE report page. It explicitly labels two separate report controls: (1) FII/FPI & DII trading activity on NSE in Capital Market Segment; (2) FII/FPI & DII trading activity on NSE, BSE and MSEI in Capital Market Segment. The visible page extraction exposes both as generic Download (.csv) controls, not their distinct href/download URLs. Web source: `turn984136view0`, lines 128-134.
- Official NSE search-indexed report text additionally states that NSE-exclusive and combined series are separately collated, and that FII/FPI data is provisional and subject to custodial confirmation/modifications; DII classification is based on trading-member codes/client category. Source: `turn523810search6` and `turn523810search0`.
- Direct browser retrieval of `https://www.nseindia.com/api/fiidiiTradeReact` was not accessible in the web retrieval environment; no API payload was obtained in this step. This is a tool-access limitation, not evidence that the endpoint is down.
- No URL was guessed, no live capture was attempted, no raw data was committed, and no production file/workflow was changed.
- Current state: official page scope labels VERIFIED; provisional-data caveat VERIFIED; exact CSV URLs NOT_RESOLVED; live capture NOT_RUN. Next safe action is obtain the two exact download request URLs from the user's browser (or an official-page browser network/download trace), then pass both together to the existing isolated utility.


## 2026-11-16 — User correction: use existing Library files; do not request re-upload
- User clarified that FII/DII files are already stored in ChatGPT Library and expects the research workflow to retrieve and use them independently rather than asking the user to resend files or manually download them.
- Confirmed Library folder `/PRECISION-WIRES/NSE-FII-DII` contains both existing files: `fii-dii-nse-latest.csv` and `fii-dii-combined-latest.csv` (218 bytes each). Both were already read from Library and raw-byte SHA-256 computed in prior ledger entry.
- Current official NSE page search result independently shows the same two distinct series and same 13-Nov-2026 values as the Library files: NSE-only DII -1,970.73 and FII/FPI +5,253.98; combined DII -2,253.58 and FII/FPI +5,736.55. Official source also says FII/FPI data is provisional and subject to custodial confirmation/modifications. Source `turn817618search1`.
- Clarification: no need to ask user to re-upload or re-send already available Library CSV files. Continue retrieving known files from Library and use official web sources/programmatic research wherever available. Ask the user only if a truly unavailable input requires their direct browser action; explain the precise access limitation.
- The remaining provenance gap is not missing CSV content. It is the absence of original download URL/request metadata and capture timestamp in the stored CSVs. Do not misrepresent the user-supplied Library files as a new live NSE capture. Keep source provenance NOT_VERIFIED and live API capture NOT_RUN until independently acquired evidence supports changing those statuses.

## 2026-11-16 — FII/DII Library CSV arithmetic and cross-source reconciliation
- New bounded QA pass on the two already-stored Library CSVs (no re-upload and no hash recomputation required):
  - Both files contain exactly the expected two categories (DII, FII/FPI), same observation date 13-Nov-2026, and same ₹ Crores units.
  - Verified each row's arithmetic exactly to 2 decimals: BUY − SELL = NET.
  - NSE-only: DII 10,561.32 − 12,532.05 = −1,970.73; FII/FPI 17,376.50 − 12,122.52 = +5,253.98.
  - Combined: DII 11,745.95 − 13,999.53 = −2,253.58; FII/FPI 18,339.57 − 12,603.02 = +5,736.55.
  - All four row arithmetic checks PASS; category/date/unit alignment PASS; no duplicate category within either file.
- Cross-source reconciliation: combined CSV's two rows exactly match the existing NSE API artifact Run #161 (market_context.json, observation date 13-Nov-2026): DII net −2,253.58 and FII/FPI net +5,736.55, including buy/sell values. This is an independent consistency check of the combined series, but not a substitute for original CSV download URL metadata.
- NSE-only series has no matching independent same-date API row in the evidence presently retained; its independent cross-source check remains NOT_AVAILABLE.
- Calculated scope deltas (Combined minus NSE-only): DII buy +1,184.63, sell +1,467.48, net −282.85; FII/FPI buy +963.07, sell +480.50, net +482.57. These are exchange-scope differences, not data errors.
- Current web-indexed official NSE report page returns stale 21-Aug-2026 table values in this retrieval snapshot, while a separately indexed NSE page variant returns “No Records”; these are cache/index retrieval artefacts and are not used to overwrite the Library's 13-Nov-2026 records. Official page continues to describe the two scopes separately and notes FII/FPI provisional status.
- Status update: Library CSV schema/date/category checks PASS; four row arithmetic checks PASS; combined-series Run #161 reconciliation PASS; NSE-only independent same-date reconciliation NOT_AVAILABLE; CSV source URL/download timestamp NOT_VERIFIED; live raw capture NOT_RUN; historical coverage NOT_AVAILABLE.
- No production code, selector, score, diagnostics, engines, collector, or workflow changed. This is research evidence only.

## 2026-11-16 — CORE-672 FII/DII schema-mapping gap audit completed
- Added research-only report `docs/CORE_672_FII_DII_SCHEMA_MAPPING_GAP_AUDIT_20261116.md` (commit `80f2038fc3ccae42bd5caa14ee4a87b9bb377cd3`; report blob re-fetched and verified).
- Exact source blobs reviewed: `collector/context_data.py` `f38e17979774d1439eea79e4dc7728ba92a790d1`; `pipeline/diagnostics_672.py` `af0a8ddc17d72024509167533585713600a4b845`; `pipeline/risk_modifier.py` `4115a1247992ef8a075b2fd247efb9ce8f8663f6`.
- Confirmed schema mismatch: collector emits category/group/date/buy_value/sell_value/net_value; CORE-672 diagnostics reads `fii_net` and `dii_net`. For retained collector-shaped rows both lists are empty -> NaN -> neutral score 50 -> UNKNOWN. No zero is asserted as actual flow.
- Confirmed Risk Modifier separately sums first 20 group-specific net_value rows but does not sort by date or enforce 20 distinct matured sessions/scope. This is not an approved CORE-672 mapping or rolling-history policy.
- Report specifies required gates: explicit exchange scope, category normalization, observation-date identity, uniqueness, arithmetic validation, freshness/provisional/revision handling, minimum matured-session rule, fail-closed UNKNOWN, and separation of CORE-672 from Risk Modifier.
- Status: static source inspection PASS; mismatch finding PASS; production mapping change NOT_AUTHORIZED/NOT_DONE; rolling 20-session evidence NOT_AVAILABLE; live NSE capture NOT_RUN; official CSV download provenance NOT_VERIFIED.
- No production source, collector, diagnostics, Risk Modifier, Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 56×12 structure, Engines A-E, or workflow was modified. Research report only.

## 2026-11-16 — Research-only FII/DII mapping contract and isolated tests
- Created isolated branch `research/fii-dii-contract-tests-20261116` from `research/nse-raw-manifest-retention-20261115`; no default-branch merge and no production files changed.
- Added `tools/research/fii_dii_contract.py` (commit `6e596937923e157c370a8facd7a865c995cbfd52`, blob `a63a6008f8f0e5d24d1b26d7c96b012205dec23f`). The validator is structural only: explicit scope enum (`NSE_ONLY` / `NSE_BSE_MSEI_COMBINED`), category allowlist, date-only observation date, duplicate scope/date/category rejection, finite numeric validation, BUY-SELL=NET arithmetic, and explicit caller-supplied maturity threshold. It emits no POSITIVE/NEGATIVE signal and does not define a production aggregation policy.
- Added `tools/research/tests/test_fii_dii_mapping_contract.py` (final commit `777e8272b71800c1be448a40990fc86965dafb76`, blob `3433ddd68ee14f6b7e80307062dcde3c1ecb7afd`), 13 tests using provenance-pinned Run #161 fixture `tests/research_fii_dii_run161/fixtures/run161_fii_dii_excerpt.json`. Invalid-input mutations are test cases only, not synthetic market observations. Import path was explicitly fixed using importlib because unittest discovery runs from the tests directory.
- Extended only the existing manual `workflow_dispatch` offline test workflow on this isolated branch to run the new contract suite after the existing capture utility suite. Workflow update commit `fa10ab59c6b08e74f0f6ef9c7e2c8f1fcd017531`, blob `5b4db141ff0de4906887cc7e913a315461b347c3`. Workflow retains contents:read, 5-minute timeout, no NSE calls, no secrets, no artifacts, no production schedule.
- Re-fetched all three final files from the isolated branch; verified 13 test methods and both test commands are present. Exact GitHub Actions execution is NOT_RUN because this session has no workflow-dispatch action. Do not claim test PASS until user triggers the workflow and GitHub confirms success.
- This contract deliberately does not assume a 20-session FII/DII window or set a new threshold. `maturity_status` requires a caller-supplied positive integer; the one-date Run #161 fixture returns UNKNOWN for a 20-session requirement. Any actual production window/freshness/provisional policy remains to be approved separately.
- Status: contract authoring 100%; 13 test cases authored 100%; manual workflow wiring 100%; final GitHub file retrieval verification 100%; exact automated execution NOT_RUN; production mapping NOT_AUTHORIZED/NOT_DONE; live NSE capture NOT_RUN; historical multi-session evidence NOT_AVAILABLE.
- No changes to default branch, Production Selector, `RANKING_SCORE`, `+1 PRESSURE_FADE`, CORE-672 56×12 production diagnostics, engines A-E, collector production code, or production workflows.

## 2026-11-16 — FII/DII contract scope-provenance boundary hardening
- Continued the isolated mapping-contract task on `research/fii-dii-contract-tests-20261116`; no repeated execution of prior tests and no production edits.
- Code review identified an important boundary: the contract receives scope as a caller argument; the retained Run #161 fixture itself does not carry authenticated exchange-scope metadata. Therefore a validator cannot prove the caller's NSE-only/combined label from that fixture alone.
- Hardened `tools/research/fii_dii_contract.py` to return `declared_scope` rather than `scope`, and clarified its docstring: it validates rows under a caller-declared label but does not authenticate scope provenance. Final blob `090f9b5f58922fcb543f69d425c2a32fb387dd93`, commit `591317831a4093c930223682191a39edfa96a327`.
- Expanded `tools/research/tests/test_fii_dii_mapping_contract.py` from 13 to 14 tests, including a regression assertion that the output exposes only `declared_scope` and does not claim `authenticated_scope`. Final blob `efddbdb4e3a36e77cb35b8ae2701e2ee3b3423b9`, commit `e6be1907cb1452aea43926a64be53b7c1beffe5f`.
- Re-fetched final contract, test file, and manual workflow from the branch. Verified final test count=14 and workflow still includes both isolated test suites. Workflow blob `5b4db141ff0de4906887cc7e913a315461b347c3`.
- This prevents a false PASS where a caller could label one scope as another without evidence. Authentic scope proof still requires official source/download metadata or another trusted scope identifier. Existing CSV contents and Run #161 match remain consistency evidence only, not authentication of download scope.
- Status: contract/test authoring 100%; scope-provenance limitation explicitly encoded 100%; workflow wiring 100%; GitHub source re-fetch verification 100%; automated execution NOT_RUN; live NSE capture NOT_RUN; production mapping NOT_AUTHORIZED/NOT_DONE.
- No default-branch changes, no PR/merge, no production collector/diagnostic/risk-modifier/selector/score/CORE-672/engine/workflow modifications.

## 2026-11-16 — Default-branch isolated workflow checkout correction
- User screenshot showed the `main` workflow commit `Pin isolated FII-DII tests to research branch` had hard-pinned checkout to `research/nse-raw-manifest-retention-20261115`, and only ran the capture utility suite. This explained why selecting `research/fii-dii-contract-tests-20261116` in the Run workflow dialog could not execute the newer mapping-contract suite.
- Within the user's explicit authorization limited to the isolated test workflow on the default branch, changed only `.github/workflows/nse_fii_dii_capture_unit_tests.yml` on `main`.
- Replaced hard-coded checkout ref with `ref: ${{ github.ref }}` so the workflow checks out the branch selected in GitHub's Run workflow dialog.
- Added the isolated `test_fii_dii_mapping_contract.py` test step after the existing capture utility tests. Workflow remains manual-only (`workflow_dispatch`), `contents: read`, 5-minute timeout, and no NSE network capture, secrets, artifacts, or production schedule.
- Commit: `84bfa57529b2a812d4690e7ec0e91f794be448cd`; final workflow blob: `d6b897dc164b4e38ec24f2704149c5f076c5d6bd`. Re-fetched from `main`; verified selected-ref expression and both test commands.
- This is the sole default-branch file changed, consistent with the user's prior authorization. No other production or research files changed on `main`.
- Status: default-branch workflow correction PASS (source re-fetch verified); run execution NOT_RUN; test outcome NOT_KNOWN until GitHub Actions reports it.
