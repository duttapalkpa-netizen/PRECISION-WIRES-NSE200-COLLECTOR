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


## 11. Continuity delta reconciliation — 2026-11-14 (research-only)

This appendix records verified work added after the ledger's 2026-11-08 reconciliation. It does not promote UNKNOWN/BLOCKED evidence to PASS and does not modify production.

### 11.1 CDSL FPI official-source audit — daily, FY, derivatives and fortnightly

- Daily cash/derivatives and date-alignment work is recorded in:
  - 11-Nov cash arithmetic: commit `940fff57a820afd8a5deb44059e5e72e9d8150d4`, file `docs/CDSL_DAILY_CONFIRMED_FPI_20261111_ARITHMETIC_QA.md`.
  - 11-Nov USD cross-check: commit `c47907225a59b377fe34a7c37a765c14902301a9`, file `docs/CDSL_FPI_20261111_FX_AND_SUBTOTAL_CROSSCHECK.md`.
  - 12-Nov derivatives OI delta: commit `ed68ee12dc9c73d9cadbc7dbf7383e424ae90076`, file `docs/CDSL_FPI_DERIVATIVES_20261112_OI_DELTA_QA.md`.
  - 13-Nov cash + derivatives: commit `5ae4d16e7febee293a1f7a8d0b1b0d46b85e2b22`, file `docs/CDSL_FPI_DAILY_20261113_CASH_DERIVATIVES_QA.md`.
  - 13-Nov USD/INR reconciliation: commit `00aad92706288707e98c863f0ccf5aa24f12da23`, file `docs/CDSL_FPI_20261113_USD_CATEGORY_INR_RECONCILIATION.md`.
  - Date alignment: commit `49ebca293172d5e8eb2924fd2830e7aff712fe55`, file `docs/CDSL_DAILY_FPI_DATE_ALIGNMENT_LEDGER_20261113.md`.
  - 12-Nov independent validation and mixed-vintage proof: commits `205ac42f20d8217b6592f6f5aa96fc5587e696ad` and `406b9e67841e25485c9b058eceb9d6886a2af0f9`.
- 11-Nov and 13-Nov daily cash totals passed their recorded arithmetic checks; 12-Nov cash remains UNKNOWN because the legacy daily page's cash section was stale while derivatives were dated 12-Nov. Do not fill that gap from FY/fortnightly data.
- 13-Nov daily USD reconciliation recorded USD components 1037.4148 Mn versus displayed 1037.4150 Mn (rounding residual -0.0002 Mn), and converted INR cash total ₹9,727.3217475 Cr, rounding to ₹9,727.32 Cr.
- FY series and route-vintage checks are documented in commits `6d479dcfb832b5eda33fd565ae0a4ea2a14bcc0b`, `20b59372739ca7ab3543f4e619fc84dc5377e39d`, `1bb2f0e02dd8a52bfe664110914a451caa8df1d3`, `342fc20b39dc642036879f1a1da44749402f419c`, and `552f0af71b7eef51f5fae497787b6d8b0660c314`. FY 2026-27 snapshots and daily totals reconcile for the recorded dates; the undated search-index value is not a current dated observation.
- Fortnightly sector-wise 31-Oct extraction and display/FX/frequency audits are recorded in commits `746d42d492e7b2c60d6a3cae84f42778c2c22edb`, `97a389e83b6e2029c8de252794c9ab0adb3b7d92`, and `ffa110e739e524f3975d66dd4fb7157bd2fedca4`.
- **Critical remaining blocker:** CDSL daily raw archive bytes are NOT_ACQUIRED. MIME, byte count, raw SHA-256, raw schema and archival validation remain UNKNOWN. The daily factor is not eligible for full acceptance until raw evidence is acquired and reconciled. No daily gap may be silently imputed.

### 11.2 NSE CM-MII security-master source semantics and raw acquisition blocker

- Official source discovery: commit `673b6b109238c91235a52edbfa5de9997109adca`, file `docs/NSE_SECURITY_MASTER_OFFICIAL_SOURCE_DISCOVERY_20261113.md`.
- Lineage contract: commit `7ecc6a59a45e7b4c8888bef02ce199c64ad1c9f7`, file `docs/NSE_CM_MII_SECURITY_MASTER_SOURCE_LINEAGE_CONTRACT_20261113.md`.
- Variant-scope semantics: commit `ce509ca302dee9cc032515ed52fb5b67592815da`, file `docs/NSE_CM_MII_VARIANT_SCOPE_SEMANTICS_AUDIT_20261113.md`.
- 11-Nov download-resolution update: commit `c339e8c2894e131650e5b3476ae26e5920d15321`, file `docs/NSE_CM_MII_11NOV2026_DOWNLOAD_RESOLUTION_CHECK_20261114.md`.
- Official NSE circular NSE/MSD/67344 (28-Mar-2025) distinguishes the NSE-listed-only master from the NSE-listed + BSE-exclusive master. In the combined variant, BSE-exclusive status is not equivalent to ordinary NSE tradability; preserve original symbol including any `$` suffix and raw `PrtdToTrad` field. Missing or unrecognized values remain UNKNOWN. Do not infer an alternative-venue invocation without a dated official event.
- Official All Reports evidence lists two 11-Nov-2026 entries with the same displayed filename `NSE_CM_security_11112026.csv.gz` but different displayed sizes (1.22 MB and 1.49 MB). The extracted page did not expose the two row-specific hrefs. The 12-Nov captured list did not show these MII entries. Neither fact authorizes inventing an archive URL or substituting CM-UDiFF/Full Bhavcopy.
- **Critical remaining blocker:** 11-Nov two raw MII variants are NOT_ACQUIRED; exact row hrefs, HTTP metadata, bytes, SHA-256, gzip integrity, schema, row counts and cross-variant comparison remain UNKNOWN/NOT_STARTED. Previously uploaded 08-Nov/09-Nov archives do not substitute for 11-Nov.

### 11.3 IIP October-2026 schedule reconciliation — corrected interpretation

- The initial research note incorrectly called 28-Nov versus 30-Nov a conflict. This has been corrected in research branch `research/iip-oct2026-release-date-conflict-20261114`, latest commit `d7ea2ff00f0107f69a6394b448f52f1a22bf496d`, file `docs/IIP_OCTOBER_2026_RELEASE_DATE_CONFLICT_AUDIT_20261114.md`, blob `bc09c1785e407818c62fd1399cdf480762315161`.
- MoSPI's updated 2026-27 Advance Release Calendar lists 28-Nov-2026; PIB's 28-Oct-2026 September IIP release explicitly says October IIP will be released Monday 30-Nov-2026 and states the standard 28th-or-next-working-day rule. 28-Nov-2026 is Saturday; therefore 30-Nov is the operational expected date, subject to any subsequent official change.
- Official sources: MoSPI calendar PDF https://www.mospi.gov.in/uploads/documents/releaseCalender/1793948871564-ARC%202026-27%20updated%20till%20October%202026.pdf ; PIB release https://www.pib.gov.in/PressReleasePage.aspx?PRID=2329475&lang=2&reg=48 .
- Schedule reconciliation: PASS. October-2026 raw data: NOT_YET_DUE / NOT_ACQUIRED as of 14-Nov-2026. When released, acquire original source bytes, publication timestamp, reference period, MIME/byte count, SHA-256, schema and row-count QA. Do not substitute September data.

### 11.4 Consolidated acceptance state — no promotion

- CDSL daily raw archive: BLOCKED / NOT_ACQUIRED.
- NSE 11-Nov MII raw variants: BLOCKED / NOT_ACQUIRED.
- IIP October-2026: scheduled for 30-Nov-2026; raw vintage not yet due/acquired.
- Project Hard Gate remains BLOCKED until all required source coverage, factor registry, historical regimes and matured H+1/H+3/H+5 event-study evidence are satisfied.
- Overall research percentage remains NOT_CALCULABLE until the complete weighted acceptance ledger is reconciled.
- No workflow run was started, no PR merged, no production integration performed, and no changes made to Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E or Hard Gate.


## 12. CDSL daily FPI archive fallback discovery — 2026-11-14

### Official route map verified
- SEBI's official FPI curation page explicitly lists both NSDL and CDSL source routes for Daily Trends (latest date), Current Month, Trends Archive, Calendar-year and Financial-year summaries. Official curator: https://www.sebi.gov.in/curation/fpi.html
- SEBI exposes a date-range archive UI titled Daily Trends in FII Investments with From/To date fields: https://www.sebi.gov.in/statistics/fpi-investment/archive/1999-till-date.html . The opened page exposes date inputs and a GO control, but this review did not obtain a dated result payload or raw download. This is discovery evidence only, not an acquired dataset.
- NSDL official Latest route linked by SEBI resolves to https://pilot.fpi.nsdl.co.in/Reports/Latest_chart.aspx . Its visible page states Website updated as on: 05 Oct 2020 and does not expose a current dated data table in the captured page. It is not accepted as a current raw-data fallback without a dated response and provenance.
- CDSL current daily route https://www.cdslindia.com/eservices/publications/fiidaily has latest indexed content dated 11-Nov-2026; it is not evidence for 12-Nov or 13-Nov daily cash raw rows.
- CDSL legacy archive route https://www.cdslindia.com/Publications/FIITrends.aspx has indexed metadata saying last updated 20-May-2020; no modern dated raw archive payload was captured.

### Source-boundary decision
- SEBI curation establishes an official source directory; it does not prove every underlying route provides downloadable raw data for every date.
- Do not substitute monthly, FY, calendar-year, fortnightly or third-party aggregates for missing daily cash observations.
- Do not promote NSDL values to CDSL raw-archive acceptance without documenting measure, reporting date, trade-date convention, category coverage and vintage equivalence.
- Do not treat the NSDL Latest chart page as current merely because SEBI still links it.
- The SEBI date-range form is a candidate bounded test for exact dates 12-Nov-2026 and 13-Nov-2026. Record response URL/status/content type/bytes and compare only like-for-like fields. If no dated payload is returned, preserve UNKNOWN and stop; do not reverse-engineer unsupported endpoints.

### Status
- Official fallback route discovery: PASS.
- SEBI date-range archive result payload/raw file: UNKNOWN / NOT_ACQUIRED.
- NSDL current raw daily response: UNKNOWN; visible Latest page has stale update metadata.
- CDSL 12-Nov daily cash: UNKNOWN; existing 13-Nov page arithmetic audit remains separate, while raw archive bytes remain NOT_ACQUIRED.
- CDSL daily raw-archive acceptance: BLOCKED.
- No production changes, workflow runs, PR merges, paid sources or external contact.


## 13. Bounded official archive endpoint probe — 2026-11-14

### Exact routes tested
- SEBI date-range UI: https://www.sebi.gov.in/statistics/fpi-investment/archive/1999-till-date.html . Retrieved page contains only date input labels (DD-MM-YYYY), To field and GO control; no result table, response payload, downloadable file, or dated observations were exposed in this retrieval. Exact 12-Nov-2026 and 13-Nov-2026 query submission was therefore NOT_EXECUTED; do not claim these dates were searched.
- NSDL Archive route published by SEBI: https://www.fpi.nsdl.co.in/web/Reports/Archive.aspx returned retrieval failure 502 in this review. No payload acquired.
- NSDL Current Month route published by SEBI: https://www.fpi.nsdl.co.in/web/Reports/Monthly.aspx returned retrieval failure 502 in this review. No payload acquired.
- CDSL Current Month route published by SEBI: https://www.cdslindia.com/Publications/FIIMonthlyData.aspx displayed an internal-error page (ticket 393899); no dated monthly payload acquired.
- CDSL current daily route remains indexed with reporting date 11-Nov-2026; it does not supply 12-Nov daily cash evidence in this retrieval.

### Outcome and fail-closed handling
- Official route existence: PASS (SEBI curation directory).
- SEBI archive UI structure observed: PASS; actual dated query: NOT_EXECUTED because the retrieval surface cannot submit form values.
- NSDL Archive and Current Month payload access: BLOCKED (502 retrieval failure).
- CDSL Current Month payload access: BLOCKED (site internal error).
- CDSL 12-Nov daily cash: UNKNOWN; no source payload obtained.
- CDSL 13-Nov daily cash arithmetic audit remains as previously recorded; raw daily archive bytes remain NOT_ACQUIRED.
- No NSDL/SEBI/CDSL values promoted, no monthly-to-daily substitution, no third-party source used for acceptance.
- Next admissible step requires an actual interactive form submission or official downloadable raw response; absent that, preserve UNKNOWN. No guessed API endpoints or fabricated HTTP metadata.
- No workflow run, production change, PR merge, or spend.


## 14. V11.3 Behavioral DNA calibration provenance audit — 2026-11-14

- Read-only audit report: `docs/V11_3_BEHAVIORAL_DNA_CALIBRATION_PROVENANCE_AUDIT_20261114.md`.
- Inspected default-branch source blobs: walk-forward producer `d085f7a2d35a88b4c4eaba65144a429a06961b09`; V11.3 consumer `34ad08f130254a0e8c5f09ae5a0e2d93590757df`; workflow `8860fd4f7bb43164ad1b514c884f5e9adf750973`; final selection `8bf216c866030d92f8066e9183c9636880577910`; diagnostics `af0a8ddc17d72024509167533585713600a4b845`.
- Confirmed V11.3 imports feature helpers from V11.4-labelled walk-forward module. Workflow executes walk-forward producer before V11.3 consumer and uploads backtest outputs.
- Confirmed critical fallback: missing/unreadable/empty calibration JSON becomes `{}`; absent state rate and max rate fall back to zero; calibration component becomes 50/100, i.e. 5 composite score points from its 10% weight. A valid all-zero library can produce the same value. Missing artifact is therefore not distinguishable from a valid zero-rate state in the score.
- Calibration JSON does not embed producer commit, workflow run ID, artifact ID, source-data digest/date range, schema version or checksum. Historical run-level binding remains UNKNOWN pending artifact retrieval.
- Static audit acceptance: producer-consumer ordering PASS; shared dependency CONFIRMED; silent fallback ambiguity FAIL; embedded provenance FAIL; intentional cross-version contract UNKNOWN; historical artifact binding UNKNOWN.
- Remediation recommendation only: decide shared-vs-frozen V11.3 helper contract; fail closed for absent/unreadable/stale/invalid calibration; embed and validate producer/run/data provenance. No code change applied pending explicit policy approval.
- Protected invariants unchanged; no workflow run, PR, merge, production integration, synthetic data or spend.
- Project Hard Gate remains BLOCKED; overall research percentage NOT_CALCULABLE.


## 15. Missing delivery evidence propagation / ablation impact audit — 2026-11-14

- Read-only report: `docs/DELIVERY_UNKNOWN_FEATURE_PROPAGATION_ABLATION_AUDIT_20261114.md`.
- Source inspected: `pipeline/walk_forward_backtest.py`, blob `d085f7a2d35a88b4c4eaba65144a429a06961b09`; existing issue #27 records two GSEC10ABSL missing delivery observations in Run 110 (2026-09-11 and 2026-09-14).
- Confirmed: missing DELIV_GAP contributes 0 delivery points in ABSORPTION because NaN >= 0 is False; the same missing value is neutralized to 0 gap / 50-point subcomponent in REPRICING_PRESSURE; `_winner_interaction_score` propagates NaN because it has no missing-value branch.
- Current inspected walk-forward `RANKING_SCORE` excludes WINNER_INTERACTION_SCORE; counterfactual ablation variants still include it, so missing delivery can contaminate non-current ablation comparisons. Historical affected-row count and metric delta remain UNKNOWN pending exact Run 110 replay.
- Policy remains UNRESOLVED; no silent UNKNOWN→PASS/FAIL/neutral conversion approved. No code change, imputation, workflow run, PR or production integration.
- Protected invariants unchanged. Project Hard Gate remains BLOCKED; overall research percentage NOT_CALCULABLE.


## 16. Run 110 exact artifact replay — missing delivery evidence — 2026-11-14

- Retrieved exact Run #110 artifact ID `13678590181` (`precision-wires-adaptive-110`), run ID `42622884559`; job `collect-and-test` concluded success.
- ZIP size 61,442,608 bytes; SHA-256 `02422a83c781e28dde568574e6f65a71d311a871b88c7095ed1169bd7c8dc8c7`, matching issue #27 evidence.
- Archived input `data/processed/nse_eq_200_sessions.csv`: 500,808 × 21; SHA-256 `51bb6875fe1ec4474c73feefd99e49c37c9eaacec7735f18b34f72f639040a4c`. Walk-forward output: 249,473 universe predictions, 100 cutoff dates.
- Recomputed delivery rolling fields over 255,082 cutoff-universe rows: exactly 2 raw DELIV_PER missing rows, both GSEC10ABSL on 2026-09-11 and 2026-09-14; separately 1,269 rows had current DELIV_PER present but DELIV20 baseline unavailable due rolling(20,min_periods=5); total DELIV_GAP NaN = 1,271. Do not conflate raw missingness with insufficient rolling history.
- For the two raw missing rows: ABSORPTION delivery component = 0; REPRICING_PRESSURE delivery subcomponent = neutral 50 (weighted contribution 10 before outer clip); archived WINNER_INTERACTION_SCORE = NaN; archived current RANKING_SCORE finite (7.0868191099 and 8.3152488958), consistent with inspected formula excluding WINNER_INTERACTION_SCORE. Both archived H+3 outcomes were below +10% (+0.212333% and 0.000000%).
- Full exact artifact replay report: `docs/RUN110_DELIVERY_UNKNOWN_EXACT_ARTIFACT_REPLAY_20261114.md`.
- Artifact/data integrity and missingness/downstream reconciliation: PASS. Counterfactual performance impact: NOT_RUN / UNKNOWN. UNKNOWN-delivery policy remains UNRESOLVED pending owner approval. No imputation, code change, workflow rerun, PR, merge or production integration.
- Protected invariants unchanged; Hard Gate BLOCKED; overall research percentage NOT_CALCULABLE.


## 17. Macro-Geo P0 Run 210 exact artifact provenance reconciliation — 2026-11-14

- Retrieved Run #210 ID `40898379422`; job `macro-geo-p0` SUCCESS; artifact ID `12908992135`, 96,946 bytes; ZIP SHA-256 `8c2de588aaf79697578a1343f7c88c9fd9bd383cbd6e2866d51e97eb5fadcb48`.
- Exact archived `data/external/brent_crude.csv`: 213 rows, 2025-12-22..2026-10-26; US EIA RBRTE daily Brent spot, source URL `https://www.eia.gov/dnav/pet/hist_xls/RBRTEd.xls`; SHA-256 `203b886a538a18c4631b4d21f4a91d44f0bdf41986ef026ea7e9d800cf3810b8`. `p0_repair_report.json` agrees on path, source, rows, dates and URL.
- `crude_oil_collection_report.json` separately reports Yahoo BZ=F futures proxy at `data/external/brent_crude_futures_proxy.csv`, 212 rows; explicitly not spot. That proxy CSV is absent from the ZIP, so proxy payload retention remains UNKNOWN; do not claim it was archived. The canonical EIA spot was not overwritten in this artifact.
- Exact artifact hard gate BLOCKED: P0 7/8 (corporate_events blocked); Factor Registry 0/35 fully available, 21 not connected; event study 48 rows, 26 eligible, 22 pending, exploratory; regime anchors 9/11; FPI 101 and DII 100 dates over 147 days; market/equity panels aligned through 2026-10-26. Selector, RANKING_SCORE and +1 PRESSURE_FADE unchanged.
- Report: `docs/MACRO_GEO_RUN210_EXACT_ARTIFACT_PROVENANCE_RECONCILIATION_20261114.md`.
- Canonical EIA spot provenance reconciliation: PASS. Proxy payload packaging: UNKNOWN. Hard Gate remains BLOCKED. No code change, workflow rerun, PR, merge, imputation, paid API or external contact.


## 18. Corporate Events P0 official source contract and failure diagnosis — 2026-11-14

- Revisited exact Run #210 evidence: `corporate_events` BLOCKED, 0 accepted rows; reason requires symbol, subject, publication timestamp and source URL; prior `https://www.nseindia.com/api/corporate-announcements` attempt timed out after 6 seconds. Zero rows indicates acquisition/normalization failure, not absence of events.
- Inspected official NSE Corporate Filings application, Corporate Actions page and investor-relations Announcements page. The filings application separates announcements (Symbol, Subject, Broadcast Date) from corporate actions (Symbol, Purpose, Ex-Date); these time fields must remain distinct.
- Defined raw-first, immutable, fail-closed event schema and acquisition QA contract in `docs/CORPORATE_EVENTS_P0_OFFICIAL_SOURCE_CONTRACT_20261114.md`.
- Official page/field semantics contract: PASS. Live API request shape/pagination: UNKNOWN; raw payload/hash/MIME/bytes: NOT ACQUIRED; symbol/series/ISIN validation and duplicate/timestamp/coverage QA: NOT RUN. Corporate Events P0 remains BLOCKED.
- No guessed API parameters, paid source, third-party scraper, synthetic rows/timestamps, code/workflow change, PR merge or production integration. Hard Gate BLOCKED; protected invariants unchanged.


## 19. Corporate Events P0 — official NSE RSS channel evaluation — 2026-11-14

- Identified first-party NSE RSS page `https://www.nseindia.com/static/rss-feed` (legacy `/rss-feed` redirects). It enumerates separate feeds for Announcements, Corporate Actions, Board Meetings and other disclosure classes; NSE describes RSS as a timely update channel, while warning reader/provider delays may occur.
- NSE filings application separately exposes announcement Symbol/Subject/Broadcast Date, corporate action Symbol/Purpose/Ex-Date, and board meeting Symbol/Purpose/Meeting Date. Keep these source families and date semantics separate.
- RSS is a plausible official discovery/fallback channel, but exact XML feed href could not be resolved from the page's extracted link text. No feed URL guessed. Raw XML, MIME/bytes/SHA, GUID/pubDate/timezone/schema/retention and historical coverage remain UNKNOWN/NOT ACQUIRED.
- Report: `docs/CORPORATE_EVENTS_P0_OFFICIAL_NSE_RSS_CHANNEL_EVALUATION_20261114.md`.
- Source discovery and semantic separation: PASS. RSS ingestion readiness: NOT ESTABLISHED. Corporate Events P0 remains BLOCKED. No code/workflow change, paid source, third-party vendor, guessed URL, PR merge or production integration.


## 20. Corporate Events P0 — NSE announcements RSS URL resolution — 2026-11-14

- Official NSE RSS page explicitly lists the Announcements feed and instructs subscribers to open its RSS icon. An independent feed directory corroborates the NSE-hosted announcements URL `https://nsearchives.nseindia.com/content/RSS/Online_announcements.xml`; related NSE-hosted Corporate Actions, Board Meetings and Financial Results feeds are separately listed.
- Direct XML open produced an unsupported-content-type response (`application/xml`) in the web reader, not an HTML page. This does not establish HTTP status or valid XML. Raw download from the execution environment failed at DNS resolution; no bytes or SHA-256 were obtained.
- URL resolution: PASS (candidate NSE-hosted endpoint, independently corroborated). Raw acquisition/schema/GUID/pubDate/timezone/retention/coverage: NOT ACQUIRED / NOT RUN. Corporate Events P0 remains BLOCKED.
- Report: `docs/CORPORATE_EVENTS_P0_NSE_ANNOUNCEMENTS_RSS_URL_RESOLUTION_20261114.md`.
- No guessed query parameters, synthetic data, paid service, code/workflow change, PR merge or production integration.


## 21. Corporate Events P0 — RSS operational signal and bounded acquisition — 2026-11-14

- Official NSE RSS page confirms the Announcements first-party feed and instructs users to obtain the exact feed URL via its RSS icon; it warns third-party reader/provider delays may occur.
- Two independent Feeder directory listings currently report the NSE-hosted Announcements feed as working with recent items. This is secondary availability evidence only, not authoritative data or proof of raw NSE endpoint health/completeness. A recent third-party technical article reports a 10-Nov sample, but is not adopted as official source evidence.
- Direct GET to `https://nsearchives.nseindia.com/content/RSS/Online_announcements.xml` with browser-like headers and 15s timeout failed at DNS resolution in this runtime. No HTTP response, bytes, MIME, redirect chain or SHA-256 obtained. Web reader's `application/xml` limitation is not an HTTP status.
- Report: `docs/CORPORATE_EVENTS_P0_RSS_OPERATIONAL_SIGNAL_20261114.md`.
- Operational signal: SECONDARY SUPPORT ONLY. Raw feed acquisition/schema/GUID/timezone/retention/completeness: UNKNOWN/NOT RUN. Corporate Events P0 remains BLOCKED. No code/workflow change, PR merge or production integration.


## 22. Corporate Events P0 — official filings vs RSS freshness cross-check — 2026-11-14

- Official NSE Corporate Filings snapshot exposes 7 Corporate Announcements, 26 Corporate Actions and 535 Board Meetings; latest announcement table fields are Symbol, Subject, Broadcast Date. Five displayed rows are YATRA, GICHSGFIN, TARSONS, ONIDA and RUBYMILLS, all dated 13-Nov-2026. Corporate Actions use Ex-Date; Board Meetings use Meeting Date. Keep families/date semantics distinct.
- NSE page disclaimer states issuer-submitted information is displayed without exchange verification of adequacy, accuracy or veracity; raw issuer provenance and independent verification status must remain explicit.
- Two Feeder RSS reader listings report the same feed working but disagree on freshness and post-rate (~1,011/day vs ~1,427/day); these are secondary reader signals, not coverage denominators. Their displayed latest items do not overlap the five displayed official rows, but the page is only a limited latest-row sample and raw XML is unavailable; no missing-event conclusion or item-level reconciliation is valid.
- Report: `docs/CORPORATE_EVENTS_P0_OFFICIAL_RSS_FRESHNESS_CROSSCHECK_20261114.md`.
- Official page field semantics/snapshot and disclaimer: PASS. RSS reader signals: secondary only, inconsistent. Raw XML/GUID/item-level matching/retention/completeness: NOT ACQUIRED / NOT RUN. Corporate Events P0 remains BLOCKED.


## 23. Corporate Events P0 — RSS collector implementation readiness — 2026-11-14

- Complete GitHub main recursive tree returned 49 entries, not truncated; no tracked path matches RSS/corporate/announcement/event. No dedicated RSS collector, parser, QA, manifest or workflow exists.
- `nse_collector.yml` blob `8860fd4f7bb43164ad1b514c884f5e9adf750973`: `contents: read`, 60-minute timeout, full multi-stage collector/backtest/selection workflow; unsuitable for isolated sub-10-minute RSS acquisition. `prospective_watchlist_tracking.yml` blob `850b7c266bfa29e01f70722dbf342988730fc351`: `contents: write`, 120-minute timeout; exclude.
- Readiness recommendation: isolated workflow with `contents: read`, 8-minute timeout, manual trigger, exact official RSS URL allowlist, immutable raw XML + manifest/hash, safe XML parser, item retention and explicit error accounting; no secrets, write permissions, push or PR. Specification is in `docs/CORPORATE_EVENTS_P0_RSS_COLLECTOR_IMPLEMENTATION_READINESS_20261114.md`.
- No code/workflow edit or run was performed. GitHub Actions outbound DNS and official raw XML availability remain UNKNOWN until a bounded runner test. Corporate Events P0 remains BLOCKED.


## 24. Corporate Events P0 — isolated read-only RSS collector v1 implementation — 2026-11-14

- Official NSE RSS catalogue lists Announcements among its RSS feeds; NSE cautions that reader/provider refresh delays may occur. Source page: https://www.nseindia.com/static/rss-feed.
- Added `collector/nse_announcements_rss.py`: one bounded request to the previously identified NSE announcements RSS URL; 15-second socket timeout; 10 MiB response cap; records requested/final URL, HTTP status, content type, byte count, SHA-256 and UTC retrieval interval; raw XML preserved before parsing; original title/link/GUID/isPermaLink/pubDate/description and raw item XML retained in JSONL; rejects DTD/entity declarations and unexpected XML roots; writes failure manifest on network/HTTP/parse errors. Standard-library only.
- Added `qa/test_nse_announcements_rss.py`: four tests for original pubDate/GUID preservation, missing GUID retention, DTD/entity rejection and unexpected root rejection.
- Added `.github/workflows/nse_corporate_events_rss.yml`: manual-only, isolated branch checkout, `contents: read`, `persist-credentials: false`, 8-minute job timeout, 30-day diagnostic artifact upload, no push/PR/secrets.
- GitHub blob SHAs: collector `217d4c11ce5f070341447f7c01bfd03b41c19a93`; tests `81e7f906f77f8c2abe2fd2a4e175743e00838a69`; workflow final `b2fefaa9f9a6f89ea537f385cbfc17f03068f31e`.
- Workflow file was fetched again after correcting its artifact-name expression; verified final expression is `${{ github.run_id }}`.
- Implementation files are committed only on research branch `research/corporate-events-rss-collector-v1-20261114`; no default-branch change, PR or merge.
- Execution status: NOT RUN. The available GitHub connector has no workflow-dispatch operation; no claim of tests passing or raw XML acquisition. Unit tests are committed but require execution in GitHub Actions. DNS/network reachability and source XML validity remain UNKNOWN.
- Corporate Events P0 remains BLOCKED until the manual Actions run produces raw XML + manifest and item-level coverage/replay checks pass. No source data promoted, no synthetic values, no paid service, no production selector/ranking/CORE-672 changes.


## 25. Corporate Events P0 — first verified official NSE RSS raw acquisition — 2026-11-14

- GitHub Actions run #1 / run ID `43489286657`, head `daf88704dd0f7464e0258ce4b5b9a082e7f86dfa`, completed SUCCESS. Checkout, Python setup, 4 parser unit tests, one bounded official fetch and artifact upload all PASS. Runtime under 1 minute; configured timeout 8 minutes.
- Official URL requested and final URL both `https://nsearchives.nseindia.com/content/RSS/Online_announcements.xml`; HTTP 200; content-type `application/xml`; 6,270 response bytes; retrieval `2026-11-13T19:08:23Z`–`19:08:24Z`.
- Raw XML SHA-256 `21de2c9b2d1f39cad81600cdca22556e813d2854eeee28d5082c913ec95aa1a4`.
- 13 RSS items parsed; title/link/pubDate/description present 13/13. GUID present 0/13; no GUID synthesized. 13 unique links and 13 unique original pubDate strings in this snapshot. pubDate has no timezone suffix; original string retained; do not normalize/assume UTC.
- Artifact ID `14069815552`, name `nse-corporate-announcements-rss-43489286657`, ZIP SHA-256 `624617b0e9ef1de4220d5672c5fcb9f4fd97a7bae15b35600602e128b63fb966`, size 4,273 bytes, retention until 2026-12-13. Members XML, JSONL, manifest. JSONL SHA-256 `b918f872cabca6b6d053e4f5eeb12850e1086233d27e2dbb8f79ffdc902a6511`; manifest SHA-256 `7fd9fd4236ab223a8988095a4644cae4c48e88ce6438ad24bbd08d2c28fb287b`.
- Report: `docs/CORPORATE_EVENTS_P0_NSE_RSS_FIRST_RAW_ACQUISITION_AUDIT_20261114.md`.
- Endpoint single-snapshot reachability and parser path PASS. Historical completeness, repeat snapshot overlap, item-level official page reconciliation, pubDate timezone semantics, symbol identity and retention/replay remain UNKNOWN/NOT RUN. Corporate Events P0 remains BLOCKED.
- No PR/merge, no production integration, no synthetic data, no symbol/GUID/timezone inference, no paid source. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE and CORE-672 unchanged.


## 26. Corporate Events P0 — two-snapshot official RSS overlap audit — 2026-11-14

- Second isolated workflow run #2 / ID `43490004265`, head `d4f89dc34e9f0199e1c567c5a851ba97cd575598`, completed SUCCESS. Four parser tests PASS, bounded fetch PASS, artifact upload PASS.
- Snapshot 2: HTTP 200, 6,270 bytes, retrieved `2026-11-13T19:12:42Z`; raw XML SHA-256 `ee92888d16048899cffe4da9f57a6c246a7d4db2e133822e223e0674722bdaf0`; RSS lastBuildDate `Sat, 14 Nov 2026 00:41:41 +0530`.
- Snapshot 2 artifact ID `14068698333`, ZIP size 4,275 bytes, SHA-256 `302a080ad812d577e64694d0230bc7b09b7d2f46d27b088aa1b17225c38dce96`, expiry 2026-12-13T19:12:42Z.
- Compared downloaded artifacts from both runs: parsed JSONL byte-identical (13/13 exact same records; 0 added, 0 removed, 0 changed); JSONL SHA-256 `b918f872cabca6b6d053e4f5eeb12850e1086233d27e2dbb8f79ffdc902a6511`. Raw XML differs only in `lastBuildDate` (00:38:09 +0530 to 00:41:41 +0530); replacing that single element with a neutral token makes full XML byte streams identical. Raw XML SHA-256s differ as expected.
- Both snapshots: GUID 0/13; no GUID synthesized. pubDate strings have no timezone; original values retained. Snapshot interval 4m18s; no item delta in this interval.
- Report: `docs/CORPORATE_EVENTS_P0_NSE_RSS_TWO_SNAPSHOT_OVERLAP_AUDIT_20261114.md`.
- Two-snapshot replay/overlap audit PASS for the observed short interval. Longer-horizon coverage, historical completeness, pubDate timezone semantics, official filings cross-check and GUID identity remain UNKNOWN/NOT RUN. Corporate Events P0 remains BLOCKED.
- No PR/merge, no production integration, no synthetic values, no paid services. Protected production selector/ranking/diagnostic invariants unchanged.


## 27. Corporate Events P0 — RSS vs official NSE visible filings sample cross-check — 2026-11-14

- Official NSE Corporate Filings page snapshot exposes 7 Corporate Announcements and latest table fields Symbol, Subject, Broadcast Date. Five visible rows: YATRA, GICHSGFIN, TARSONS, ONIDA, RUBYMILLS, each broadcast 13-Nov-2026. Corporate Actions use Ex-Date; Board Meetings use Meeting Date; date semantics kept separate.
- Compared the 13-item identical RSS snapshot (runs 43489286657 and 43490004265). RSS company titles cover Religare Enterprises (3), Fusion CX (3), Kothari Petrochemicals (2), Viaz Tyres (1), Transteel Seating Technologies (2), Optivalue Tek Consulting (1), Senco Gold (1). None exactly matches the five visible rows. This is only a non-overlap against a five-row rendered sample; it is not a failed reconciliation or evidence of missing events.
- RSS lacks GUID, explicit symbol and ISIN. Its pubDate strings are timezone-naive (14-Nov 00:00–00:35); official page sample only shows date-level broadcast dates (13-Nov). No symbol inferred from names or filename prefixes; no date normalization assumed.
- Full 13-item row-level reconciliation, symbol/ISIN mapping and attachment URL cross-check remain NOT POSSIBLE from visible page sample / UNKNOWN. Need the complete official page-linked request/response captured from official browser network behavior; do not adopt undocumented third-party query parameters as official contract.
- Report: `docs/CORPORATE_EVENTS_P0_RSS_OFFICIAL_FILINGS_VISIBLE_SAMPLE_CROSSCHECK_20261114.md`.
- Corporate Events P0 remains BLOCKED; no code/workflow/production change, no paid service, no PR/merge, no synthetic values. Protected selector/ranking/CORE-672 invariants unchanged.


## 28. NSE RSS live visible-row reconciliation + endpoint discovery boundary — 2026-11-14

- Re-read official NSE Corporate Filings page on 2026-11-14. The page showed 9 Corporate Announcements and five visible Latest Announcements rows (all Broadcast Date 14-Nov-2026): RELIGARE / Analyst/Investor Meet Para A-XBRL; FUSIONCX / Dividend; RELIGARE / Analysts/Institutional Investor Meet/Con. Call Update; FUSIONCX / Record Date; RELIGARE / Monitoring Agency Report. Official NSE symbol links resolve to Religare Enterprises Limited and Fusion CX Limited.
- Cross-check against the existing 13-item RSS JSONL (two previously verified identical snapshots): RELIGARE has 3/3 subject-level matches in visible rows; FUSIONCX has 2/3 visible subject-level matches (its Outcome of Board Meeting RSS item is not in the five-row slice). This is a bounded visible-row result, not full 9-row reconciliation and not a missing-event conclusion. Exact attachment URL equality not tested.
- RSS pubDate timezone-naive; official Broadcast Date date-only. No timestamp equivalence or normalization asserted.
- A third-party article describes a possible NSE page JSON endpoint, but no NSE-published API contract was found in the official page evidence. Treat only as an unverified lead; do not request it by guessed parameters or promote to collector source. Need capture exact official page network request/response or NSE-published specification, including schema/pagination/date semantics, before implementation.
- Report: `docs/CORPORATE_EVENTS_P0_NSE_RSS_LIVE_VISIBLE_ROW_RECONCILIATION_20261114.md`.
- Corporate Events P0 remains BLOCKED; all-13 reconciliation UNKNOWN/NOT COMPLETE; no code/workflow/production change, no paid service, no PR/merge, no synthetic data. Protected production selector/ranking/CORE-672 invariants unchanged.


## 29. Official NSE Announcement XBRL surface discovery — 2026-11-14

- Verified official NSE page `https://www.nseindia.com/companies-listing/corporate-filings-announcements-xbrl` exposes Announcement Type, Company, Events/Subject, From/To filters, CSV download affordance and pagination (20 of 958 records; 48 pages) in current rendered retrieval.
- Visible columns: SYMBOL, COMPANY NAME, Event/Subject, DETAILS, ATTACHMENT, TYPE OF SUBMISSION, BROADCAST DATE/TIME; expanded row text also separates Exchange Dissemination Time and Time Taken. This provides a richer official structured surface than the basic five-row Latest Announcements widget.
- Scope is Announcement XBRL only. Do not assume it covers every general RSS announcement. Visible sample dates are 28–29 Oct 2026, outside the RSS 13–14 Nov window. No RSS item-level match claimed.
- Official page/schema/UI CSV affordance VERIFIED; exact browser request URL, date-filtered CSV bytes/hash and pagination contract NOT CAPTURED. Next step is capture the official page's own CSV export request/response for an overlapping date range, then test issuer/subject matching while keeping XBRL subset distinct.
- Report: `docs/CORPORATE_EVENTS_P0_NSE_OFFICIAL_XBRL_SURFACE_DISCOVERY_20261114.md`.
- General announcement completeness UNKNOWN; Corporate Events P0 remains BLOCKED. No code/workflow/production change, no paid service, no PR/merge, no synthetic data. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE and CORE-672 unchanged.


## 30. NSE Announcement XBRL fresh revalidation + taxonomy migration — 2026-11-14

- Fresh retrieval of official NSE Announcement XBRL page confirms UI controls (Announcement Type, Company, Events/Subject, From/To, GO, CSV download), current displayed 1–20 of 958 records / 48 pages, and columns SYMBOL, COMPANY NAME, Event/Subject, DETAILS, ATTACHMENT, TYPE OF SUBMISSION, BROADCAST DATE/TIME. Expanded row includes Exchange Dissemination Time and Time Taken. Evidence ref: `turn423980search0`.
- Newly recorded source-published taxonomy notice: an event has been merged into Para B; data available under Para B dropdown effective 20-Jun-2026. Treat this as a time-versioned taxonomy transition; preserve original source labels and effective date, do not silently rewrite historical labels.
- The 958/48 count is a current UI snapshot only, not a historical coverage denominator. CSV control visible but no CSV bytes, exact request URL/headers, date-filter execution or pagination contract captured. Current sample is 27–29 Oct 2026, outside RSS 13–14 Nov window. No row-level RSS match claimed.
- Report: `docs/CORPORATE_EVENTS_P0_NSE_XBRL_FRESH_REVALIDATION_TAXONOMY_20261114.md`.
- Corporate Events P0 remains BLOCKED; date-window export and full RSS reconciliation pending. No code/workflow/production change, no paid service, no PR/merge, no synthetic data. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE and CORE-672 unchanged.


## 31. Official NSE XBRL category-route inventory and coverage boundary — 2026-11-14

- Fresh official NSE retrievals identify distinct route surfaces:
  - General Announcement XBRL: `/companies-listing/corporate-filings-announcements-xbrl`, displayed 958 records / 48 pages.
  - Trading Window Disclosure: `/companies-listing/corporate-filings-announcements-xbrl-trading-window-disclosure`, displayed 390 records / 20 pages.
  - Loss of Share: `/companies-listing/corporate-filings-announcements-xbrl-loss-share`, displayed 8 records / 1 page.
  - Official XBRL Filing Information catalog: `/static/companies-listing/xbrl-information`, a filing-form catalog, not an event feed.
- Evidence refs: `turn937329search0`, `turn937329search1`, `turn937329search3`, `turn937329search8`.
- Route-specific counts are current UI snapshots, not additive totals, and specialized routes must not be double-counted without source-native identity reconciliation. XBRL form catalog files are not event rows. Para A→Para B effective 20-Jun-2026 taxonomy migration remains time-versioned.
- Samples are 27–30 Oct 2026, not RSS 13–14 Nov; no RSS row-level match claimed. Cross-route dedup, complete route inventory, date-window CSV bytes/hash and 13-item reconciliation NOT RUN/UNKNOWN.
- Report: `docs/CORPORATE_EVENTS_P0_NSE_XBRL_CATEGORY_ROUTE_INVENTORY_20261114.md`.
- Corporate Events P0 remains BLOCKED. No code/workflow/production change, paid service, PR/merge or synthetic data. Protected production selector/ranking/CORE-672 invariants unchanged.


## 32. Official NSE XBRL taxonomy crosswalk + filing scope rules — 2026-11-14

- Revalidated official XBRL catalog: NSE describes structured compliance filing through NEAPS with taxonomy and instance-document downloads; catalog includes distinct Regulation 30 event categories, Regulation 29 prior intimation, Regulation 33 results, Regulation 44 voting results, shareholding, investor complaints, credit rating, default history and Para B. Evidence `turn649111search1`.
- General Announcement XBRL page currently displays 958 records / 48 pages and fields SYMBOL, COMPANY NAME, Event/Subject, DETAILS, ATTACHMENT, TYPE OF SUBMISSION, BROADCAST DATE/TIME; Para B migration notice effective 20-Jun-2026 remains. Evidence `turn649111search0`.
- Trading Window XBRL is a specialized route (390 records / 20 pages), not an additive count absent identity-level dedup. Evidence `turn649111search4`.
- General Corporate Filings page indexed snapshots differ (9/14/420 and 7/26/535 across announcement/action/meeting counts); these are time-varying snapshots, not stable totals or RSS coverage denominators. Separate Broadcast Date, Ex-Date, Meeting Date, Period Ended and As-on Date semantics. Evidence `turn649111search2`, `turn649111search3`.
- Report: `docs/CORPORATE_EVENTS_P0_NSE_XBRL_TAXONOMY_CROSSWALK_SCOPE_RULES_20261114.md`.
- No date-window CSV bytes or exact export request captured; cross-route identity audit and 13-item RSS exact reconciliation NOT RUN. Corporate Events P0 remains BLOCKED. No code/workflow/production change, paid service, PR/merge or synthetic data; protected production selector/ranking/CORE-672 invariants unchanged.


## 33. Official NSE general Announcements CSV UI surface identified — 2026-11-14

- Fresh inspection of official `https://www.nseindia.com/companies-listing/corporate-filings-announcements` (web ref `turn687576view0`, lines 139–166) identified a dedicated **Announcements** panel with Company (name/symbol), Subject keyword, Search By selector, date presets (1D/1W/1M/3M/1Y/Custom/Clear), Play Announcements, Download (.csv), Convert XBRL into Excel and Refresh.
- This is a stronger official UI candidate for RSS comparison than the previously examined XBRL-only page or the five-row Latest Announcements widget. The page is a multi-panel filing dashboard; other filing panels have distinct filters and must not be merged into the Announcements dataset.
- UI control labels verified, but Search By option values, exact custom-date format, request URL, response schema, pagination, CSV bytes and SHA-256 are not exposed by static page retrieval. No UI interaction/download was performed and no endpoint guessed.
- Report: `docs/CORPORATE_EVENTS_P0_NSE_GENERAL_ANNOUNCEMENTS_CSV_UI_CONTRACT_20261114.md`.
- Next bounded step: use the official page UI, verify the Search By publication/broadcast date option, set Custom 13–14 Nov 2026, download CSV and capture exact network request/response metadata and raw bytes before parsing/reconciliation.
- Corporate Events P0 remains BLOCKED; 13-item row-level reconciliation NOT RUN. No code/workflow/production change, paid API, PR/merge or synthetic data. Protected production selector/ranking/CORE-672 invariants unchanged.
