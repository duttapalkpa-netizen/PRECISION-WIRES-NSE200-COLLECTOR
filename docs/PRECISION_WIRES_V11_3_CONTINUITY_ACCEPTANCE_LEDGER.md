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


## 34. RSS zero-item fail-closed guard + fresh 190-item official snapshot QA — 2026-11-14

- QA hardening: collector now rejects syntactically valid RSS with zero items as `RSS_ITEM_COUNT_ZERO`; added unit test `test_rejects_empty_channel_as_non_evidence`. Collector blob `90b0dba02ddaeaa336a4c410a1349337282843ac`; test blob `2234e0eb85669824e3e0ea415a32861d2db1ca4e`.
- Workflow run 43558025207 (head `244348a2a2e0a78370ed97b1e6e1ecd6e22e9dfd`) completed SUCCESS: parser tests, bounded official acquisition, artifact upload all PASS; run 04:43:06–04:43:21Z (<1 min).
- Official feed HTTP 200, application/xml, retrieval 2026-11-14T04:43:20Z–04:43:21Z; 74,162-byte raw XML SHA-256 `b76717de6777404a56ded5cae962c922f199b32534364800a96ef059918a9990`; 157,661-byte JSONL SHA-256 `fa17c0c89ebc10321821aa54fe5f5eaf7c488ddbd2e3a4d32ac0aa2e49c9b60d`; 6,251-byte manifest SHA-256 `dc4435c3043f323aa79abfeba4b571184dd44ce0b6935be69f01dc8f0ab7a052`.
- Artifact ID `14098814399`, 18,730 bytes, ZIP SHA-256 `ca0649032c67fd4519bce66d2dd6cd61805efbd2f9f7f0612fa88b05cedec517`, expires 2026-12-14T04:43:21Z.
- Structural audit: 190 items; 190/190 GUID absent; only 35/190 non-empty links, 155/190 empty link elements; 35 unique non-empty links, no repeats; 174 unique titles; 16 repeated-title rows; 189 unique descriptions; 190 unique raw item XMLs. All pubDate strings date 14-Nov-2026, source-native 00:00:02–09:54:42, timezone-naive. All 13 links from earlier snapshots occur in this 190-item snapshot. This overlap does not prove historical completeness.
- Empty-link records preserved; no guessed URLs or symbols. RSS is raw discovery only; item identity and attachment mapping remain incomplete.
- Report: `docs/CORPORATE_EVENTS_P0_RSS_EMPTY_FEED_GUARD_AND_SNAPSHOT_QA_20261114.md`.
- Corporate Events P0 remains BLOCKED; official general-announcement CSV and full filing-row reconciliation pending. No paid services, synthetic values, PR/merge or production integration. Protected production selector/ranking/CORE-672 invariants unchanged.


## 35. NSE RSS empty-link cohort deterministic NAV classification — 2026-11-14

- Re-analysed immutable official RSS run 43558025207 / artifact 14098814399 (ZIP SHA-256 `ca0649032c67fd4519bce66d2dd6cd61805efbd2f9f7f0612fa88b05cedec517`; raw XML SHA-256 `b76717de6777404a56ded5cae962c922f199b32534364800a96ef059918a9990`; JSONL SHA-256 `fa17c0c89ebc10321821aa54fe5f5eaf7c488ddbd2e3a4d32ac0aa2e49c9b60d`).
- Deterministic cohort check: all 155/155 empty-link items have source subject `Declaration of NAV`, publication timestamp `14-Nov-2026 07:00:00`, fund/ETF scheme titles and AMC/NAV descriptions. Thus the empty-link cohort is a NAV disclosure cohort, not 155 missing equity-company announcement attachments. All rows retained.
- Any token-like text in descriptions remains unpromoted to listed-equity symbol/issuer ID. No fund-scheme master or exact dated official CSV join was captured; symbol/scheme mapping remains UNKNOWN.
- Official NSE general-announcements indexed latest-five sample (web evidence turn273059search3) is not a date-window CSV and cannot establish completeness or reconcile the NAV cohort. No CSV bytes/hash, pagination contract or row-level filing join claimed.
- Report: `docs/CORPORATE_EVENTS_P0_RSS_EMPTY_LINK_NAV_CLASSIFICATION_20261114.md`.
- Scoped classification PASS 155/155. Equity symbol mapping UNKNOWN; exact General Announcements reconciliation NOT RUN; source completeness UNKNOWN. Corporate Events P0 remains BLOCKED. No code/workflow/production changes, paid service, PR/merge or synthetic values; production selector, RANKING_SCORE, +1 PRESSURE_FADE and CORE-672 unchanged.


## 36. Global-to-India Macro-Geo evidence crosswalk — 2026-11-14

- Added `docs/MACRO_GEO_GLOBAL_TO_INDIA_EVIDENCE_CROSSWALK_20261114.md` as a qualitative, source-grounded crosswalk covering Brent/energy, USD and US yields, Fed liquidity, China demand, industrial metals, precious metals, West Asia/shipping, global equity/AI rotation, yen carry and food/fertiliser channels into Indian sectors.
- Official DIPAM Market Monitor dated 10-Nov-2026 supplies a single-date cross-check of Indian/global indices, FII/DII, repo, India 10Y yield, USD/INR, FX reserves and Brent futures. These values are explicitly not represented as 14-Nov live values or as a historical series. RBI Bulletin describes elevated AE yields, stronger USD, negative EME portfolio flows and West Asia growth/inflation risks. Reuters 13-Nov report is retained as secondary context, not a substitute for official raw series.
- No factor coefficients, intuitive weights, fabricated time series, or production signals created. Event-to-NSE session panel, rolling sensitivities and out-of-sample validation remain NOT BUILT / NOT ESTIMATED. Macro-Geo P0 coverage and Hard Gate remain BLOCKED.
- Report: `docs/MACRO_GEO_GLOBAL_TO_INDIA_EVIDENCE_CROSSWALK_20261114.md`.
- Official NSE Announcements page re-opened; Company/Subject/Search By/date filters/CSV affordance verified, but exact export request, CSV bytes/hash and pagination contract remain NOT CAPTURED because static retrieval does not execute the page UI. No endpoint guessed.
- No code, workflow, production selector, RANKING_SCORE, +1 PRESSURE_FADE or CORE-672 change; no paid service, PR/merge or production integration.


## 37. Official dated Macro-Geo snapshot reconciliation — 2026-11-14

- Updated `docs/MACRO_GEO_GLOBAL_TO_INDIA_EVIDENCE_CROSSWALK_20261114.md` with three separately timestamped official snapshots:
  - CDSL FPI daily trend, reporting date 12-Nov-2026: equity net subtotal +₹14,693.72 crore; Debt-General +₹445.65 crore; Debt-VRR −₹173.22 crore; Debt-FAR exchange net +₹1,022.81 crore. CDSL source notes reporting/previous-trading-day semantics.
  - NSE 13-Nov-2026 intraday snapshot: USD/INR reference ₹94.1997 at 13:00 IST; at 12:51 IST advances 1,264, declines 2,199, unchanged 114, 3,577 traded. Intraday only, not close.
  - RBI NSDP published 13-Nov, series latest dates differ: USD/INR ₹93.77 on 12-Nov; Nifty 50 25,299 vs comparison 25,876 (-2.23%); Sensex 81,911 vs 84,467 (-3.03%); M3 latest 31-Oct; 1Y MCLR latest 06-Nov; T-bill latest 11-Nov.
- Explicitly kept source timestamps, measurement universes and reporting definitions separate. No same-session causal inference from mixed-date observations; no beta/causal coefficient estimated; no synthetic time series.
- Official source URLs recorded in crosswalk: CDSL daily FPI trends, NSE official homepage market snapshot, RBI NSDP. Evidence refs: `turn862951search0`, `turn862951search1`, `turn862951search2`, `turn862951search4`.
- Crosswalk blob after update: `ca586d5014005b3a85c72f166eed5cf016298152`; update commit `06b7c56dd1cba2b090e70fcf121f54b4e97e1aac`.
- Macro-Geo evidence snapshot enrichment: PASS. Historical event-to-session panel, factor sensitivity estimation, 8/8 P0 source coverage, 35-factor coverage and Hard Gate remain NOT PROVEN / BLOCKED. Production selector, RANKING_SCORE, +1 PRESSURE_FADE and CORE-672 unchanged. No paid API, PR/merge or production integration.


## 38. FPI/DII provisional-versus-custodian source semantics audit — 2026-11-14

- Added `docs/FPI_DII_SOURCE_SEMANTICS_RECONCILIATION_20261114.md`. Official NSE 13-Nov-2026 NSE-only FII/FPI net +₹5,253.98 crore and DII -₹1,970.73 crore; combined NSE+BSE+MSEI FII/FPI +₹5,736.55 crore and DII -₹2,253.58 crore. Four buy-minus-sell arithmetic checks PASS.
- CDSL official 12-Nov reporting date equity exchange +₹14,678.72 crore plus primary/other +₹15.00 = equity subtotal +₹14,693.72 crore; arithmetic PASS. CDSL is custodian-submitted and includes previous-day(s) trades; NSE trade activity is provisional. Reporting date, exchange universe, routes, finality and publication availability must be separate join keys. No date-only join, duplicate subtotals or look-ahead allowed.
- Official references: https://www.nseindia.in/reports/fii-dii?os=0 ; https://www.cdslindia.com/eservices/publications/fiidaily ; https://www.cdslindia.com/Publications/ArchiveDataAfter2009.aspx ; https://www.nseindia.com/static/all-reports/historical-equities-fii-fpi-dii-trading-activity .
- Scoped source-semantics and snapshot arithmetic audit PASS. Same-date custodian reconciliation, historical raw archive SHA-256, as-of availability panel and rolling impact study NOT RUN. FPI/DII factor coverage and Hard Gate remain BLOCKED / NOT PROVEN. No synthetic data, paid APIs, PR merge or production changes; protected invariants unchanged.


## 39. CDSL FPI historical archive access and coverage audit — 2026-11-14

- Added `docs/CDSL_FPI_HISTORICAL_ARCHIVE_ACCESS_AND_COVERAGE_AUDIT_20261114.md`.
- Official CDSL archive indexed snapshot says daily FPI investment data up to 13-Nov-2026, visible extracted daily rows beginning 02-Nov-2026, and cumulative totals since Nov-1992; source states custodian submissions and previous trading day(s) semantics. Official CDSL daily page has 12-Nov-2026 arithmetic already checked in Appendix 38.
- Direct open attempt to official archive URL returned an internal error (ticket 604935). No raw downloadable file bytes, content type, byte count, exact download URL or hash could be captured. This is a retrieval limitation, not evidence of zero data. No guessed URL or reconstructed archive created.
- Full daily historical coverage, archive pagination/download contract, raw SHA-256 manifest, same-date NSE/ CDSL reconciliation and rolling sector impact study remain UNKNOWN / NOT RUN. Hard Gate remains BLOCKED. Production selector, RANKING_SCORE, +1 PRESSURE_FADE and CORE-672 unchanged; no paid service, PR/merge or production integration.
- Evidence: official CDSL archive indexed result `turn496926search0`; official CDSL daily `turn496926search1`; archive open error `turn468255view0`.


## 40. SEBI-listed NSDL alternate FPI/DII historical archive route identified — 2026-11-14

- Recovered an alternate official route after CDSL archive internal-error response. SEBI's FPI curation catalog lists NSDL and CDSL in parallel for latest, current-month and archive FPI trends, plus sector-wise, AUC, trade-wise and ODI data (web evidence `turn323022search5`).
- NSDL official FPI portal exposes separate FPI Archive and DII Archive. FPI archive has To Date, View Report and Export to Excel controls (web evidence `turn627844view0` lines 21–29; `turn329375view0` lines 20–25). DII archive resolves to date-entry form; default static extraction shows Please Select Date / No Data Found, not a valid zero-history conclusion (web evidence `turn945792view0` lines 22–27).
- No date was selected and no workbook bytes/export response/hash were captured; raw acquisition and coverage remain NOT ACQUIRED / NOT VERIFIED. This is an actionable official UI route, not a claimed data acquisition. Report updated: `docs/CDSL_FPI_HISTORICAL_ARCHIVE_ACCESS_AND_COVERAGE_AUDIT_20261114.md`; updated report blob `82e16be2c67cc60b4550f99e8f79fdacb0643540`.
- Next bounded task: exact-date NSDL FPI archive export and raw workbook SHA-256, then separately DII archive date export; reconcile to CDSL only where source dates, route and scope align. No guessed query parameters, no synthetic values/timestamps, no paid API, PR/merge or production change. Hard Gate remains BLOCKED.


## 41. Macro-Geo transmission evidence refresh — 2026-11-14

- Updated `docs/MACRO_GEO_GLOBAL_TO_INDIA_EVIDENCE_CROSSWALK_20261114.md` with the RBI dashboard snapshot updated 14-Nov-2026, preserving actual observation dates: policy repo 5.50%, USD/INR ₹94.1997 at 13:00 IST 13-Nov, sovereign yield curve observations 12-Nov, and index observations 12-Nov. Official RBI source: https://m.rbi.org.in/scripts/BS_ViewBulletin.aspx?Id=24446 (web evidence `turn459992news3`).
- Added a guarded transmission map for INR/oil/imported inflation, sovereign yields/discount rates, FPI-vs-breadth divergence, AI/IT rotation and West Asia freight/oil risks. Added recent reporting context from Reuters (13-Nov) and RBI October MPC resolution; these are not promoted to raw official market-series observations or model coefficients (`turn459992news7`, `turn459992news8`, `turn459992news10`, `turn459992search0`).
- Explicit controls retained: no mixed-date joins, no synthetic panel, no forward-fill, no inferred beta/causality, no production selector/ranking/CORE-672 changes. Scoped dated evidence refresh = DOCUMENTED; 8/8 Macro-Geo P0, 35-factor coverage, historical event panel, rolling sensitivity and production-parity backtest remain NOT PROVEN / NOT RUN. Hard Gate remains BLOCKED.
- Crosswalk update commit: `eab424dfb7184cb0bc0e914e892e8bb99011112b`; new crosswalk blob: `749ccf8c79632d8576d63541040e4a9ece6fe59d`.


## 42. Official October 2026 external-sector trade release ingested — 2026-11-14

- Added the Ministry of Commerce & Industry / PIB 13-Nov-2026 October trade release to `docs/MACRO_GEO_GLOBAL_TO_INDIA_EVIDENCE_CROSSWALK_20261114.md`. Official values: merchandise exports US$49.47bn, imports US$89.35bn, merchandise deficit US$39.88bn; total exports US$89.99bn, imports US$110.07bn, total deficit US$20.09bn; April–October merchandise deficit US$218.15bn and total deficit US$93.35bn. October services values are explicitly estimates, as the latest RBI services actual in the release is September. Official source https://www.pib.gov.in/PressReleseDetailm.aspx?PRID=2335914&lang=2&reg=48 (web evidence `turn935975search0`).
- Added export sector context (petroleum products, electronics, gems/jewellery, chemicals, engineering) with explicit guardrail that national export growth is not issuer earnings or stock-return evidence.
- Scoped official monthly data ingestion/documentation: PASS. Full historical monthly panel, issuer-level mapping, factor coverage and rolling validation remain NOT PROVEN / NOT RUN. No synthetic daily data, no causal coefficient, no production change, no PR/merge. Hard Gate remains BLOCKED.
- Crosswalk commit `83c7c71cab7950f4cc68838b7726c56b19374acf`, blob `5fb6d5fe9d150f3fdcf817cfff10018736e49217`.


## 43. CDSL official archive dated-row re-check and arithmetic PASS — 2026-11-14

- Revisited official CDSL archive indexed snapshot (headed daily trends up to 13-Nov-2026). Extracted 02-Nov-2026 equity stock-exchange gross ₹21,334.02cr minus sales ₹17,015.12cr = net ₹4,318.90cr; Primary & Others +₹138.90cr; equity subtotal +₹4,457.80cr. Arithmetic PASS. Debt stock-exchange net −₹522.18cr plus Primary & Others −₹26.15cr = debt subtotal −₹548.33cr. Arithmetic PASS. Official source https://www.cdslindia.com/Publications/ArchiveDataAfter2009.aspx (turn593944search2).
- Separately recorded the 13-Nov-2026 derivatives table snapshot (index futures buy ₹5,266.61cr, sell ₹1,700.53cr, end-date OI ₹32,628.02cr); it is not the same reporting-date record as the 02-Nov cash-equity row.
- SEBI official FPI catalog confirms NSDL/CDSL parallel daily/monthly/archive routes (turn593944search0); CDSL portal exposes archive, fortnightly sector and trade-wise routes (turn593944search1, turn593944search6).
- Scoped visible-row arithmetic validation PASS. Raw original workbook/download bytes, full row coverage, SHA-256 manifest, exact pagination/export contract, historical DII panel and rolling impact study remain NOT ACQUIRED / UNKNOWN / NOT RUN. Hard Gate BLOCKED. No synthetic data, no date-only join, no production selector/ranking/CORE-672 change, no PR/merge.
- Audit report commit 8aa860f036f4cc950b7f04923563394264a32ffc, blob 0cd2d1abac898090880b849859ca98cbc384c6e8.


## 44. CDSL 2026 YTD FPI aggregation and source inventory audited — 2026-11-14

- Official CDSL archive “Total for 2026” at compilation 13-Nov-2026: Equity exchange net −₹210,855.26cr plus Primary & Others +₹69,275.84cr = Equity subtotal −₹141,579.42cr; arithmetic PASS. Other subtotals: Debt +₹57,469.39cr; Debt-VRR −₹18,196.58cr; Debt-FAR +₹29,960.14cr; Hybrid −₹6,715.12cr; MF +₹10,641.48cr; AIF −₹3.46cr; all-category total −₹137,699.41cr. Official source https://www.cdslindia.com/Publications/ArchiveDataAfter2009.aspx (turn479037search0).
- CDSL official FPI landing page inventory records calendar-year, financial-year, quarterly, fortnightly sector-wise, AUC, derivatives, trade-wise equity/debt and ODI/PN datasets; daily derivative reporting since 01-Dec-2010. Source https://www.cdslindia.com/Publications/ForeignPortInvestor.html (turn479037search2).
- CDSL daily page 12-Nov-2026 equity subtotal +₹14,693.72cr and debt category figures retained as separate dated snapshot (turn479037search1). Explicitly noted that one-day positive equity flow does not negate negative 2026 YTD equity subtotal.
- Scoped 2026 YTD aggregation arithmetic and archive inventory: PASS. Original daily archive/workbook bytes, full session history, raw SHA-256 manifest, DII historical export, exact coverage calendar, same-date NSE reconciliation and rolling impact study remain NOT ACQUIRED / NOT RUN. Hard Gate remains BLOCKED. No synthetic data, no date-only joins, no production selector/ranking/CORE-672 changes, no PR/merge.
- Audit report commit ad9ccd04254f3e1221a2b4855cb3dcf33a41fc3f, blob 6c946f25b3b0cc8b4e4d6ab68e485e580df47310.


## 45. CDSL fortnightly sector-wise FPI report inspected — 2026-11-14

- Official CDSL inventory's latest listed fortnightly sector-wise FPI snapshot is 15-Oct-2026; subsequent listed entries are 30-Sep and 15-Sep 2026. No November sector snapshot is visible in the inventory reviewed (turn849696search0).
- Opened exact official 15-Oct report (turn849696search1). Schema includes sector-wise AUC at 30-Sep, net investment for 16–30 Sep and 01–15 Oct, AUC at 15-Oct, with INR crore/USD million and separate Equity, Debt General, Debt VRR, Debt-FAR, Hybrid, MF and AIF fields.
- Visible Automobile & Auto Components equity row: AUC ₹4,98,295cr at 30-Sep; net equity investment −₹3,542cr for 16–30 Sep and −₹6,533cr for 01–15 Oct; AUC ₹4,77,593cr at 15-Oct. This is a visible sector example, not full-table reconciliation; AUC change is not equated to flow because valuation/FX and other effects may contribute.
- Scoped report/schema and one-row extraction: DOCUMENTED. Full machine-readable sector panel, immutable raw download and SHA-256, all-row QA, issuer exposure mapping, multi-period sector-return joins and rolling predictive test remain NOT ACQUIRED / NOT RUN. No production feature/ranking changes; Hard Gate remains BLOCKED.
- Audit report commit 5685d028baac2b6b4ccb02a1f75e7d3b31c0a7cc, blob fac88582ad8fc004c244e658b700ef96359e9184.


## 46. CDSL fortnightly sector-wide FPI flow panel transcribed and audited — 2026-11-14

- Inspected full official 15-Oct-2026 report through Grand Total and methodology notes (turn633522view0 lines 3–63; turn915067view0 lines 25–63). Report has 22 BSE common-industry sectors plus Others.
- Grand Total equity net investment: −₹21,745cr (16–30 Sep) and −₹47,955cr (01–15 Oct); two-period combined −₹69,700cr. Derived arithmetic PASS.
- Recorded all 22 sector Equity net flows for both periods in audit report. Major outflows include Financial Services −₹6,943cr / −₹8,634cr, FMCG −₹972cr / −₹8,172cr, Auto −₹3,542cr / −₹6,533cr, Oil/Gas −₹4,469cr / −₹3,680cr, Telecom −₹2,423cr / −₹3,928cr, Metals −₹2,322cr / −₹3,693cr. IT −₹38cr / +₹2,599cr; Consumer Services +₹1,911cr / −₹1,931cr. These are flow observations only, not price-performance claims.
- Preserved critical caveats: BSE classification of ~4,800 issuers into 22 sectors; Others contains investments outside that issuer set; Debt VRR coverage begins 30-Apr-2020; Debt-FAR/MF/AIF AUC from 31-Aug-2024 and net investment from 15-Sep-2024; fortnightly USD conversion uses period-end RBI reference rates (95.9832 and 95.0691), unlike daily CDSL conversion method.
- Scoped full sector Equity panel transcription and Grand Total arithmetic: DOCUMENTED / PASS. Original raw file bytes and SHA-256, all-category all-sector reconciliation, NSE sector-index mapping, historical multi-period panel and rolling predictive test remain NOT ACQUIRED / NOT RUN. Hard Gate remains BLOCKED. No synthetic data or production changes.
- Audit report commit 395a2815ae6c041f12b07766ae95ec40c5080c19, blob 8d10bd449780f247071c0b7781a83e2fd5dca106.


## 46. CDSL full fortnightly sector-wise equity flow panel audited — 2026-11-14

- Inspected official CDSL 15-Oct-2026 report full table and methodology (turn177159search0). It covers 22 BSE Common Industry Classification sectors plus Others, with separate period-end AUC and two fortnightly net-investment windows.
- Grand Total equity net investment −₹21,745cr (16–30 Sep) and −₹47,955cr (01–15 Oct), combined −₹69,700cr; arithmetic PASS.
- Transcribed all 22 sector Equity flows for both windows into the audit report. Major outflows included Financial Services −₹6,943cr / −₹8,634cr; FMCG −₹972cr / −₹8,172cr; Auto −₹3,542cr / −₹6,533cr; Healthcare +₹3cr / −₹5,497cr; IT −₹38cr / +₹2,599cr. Other sector values are fully enumerated in the report.
- Preserved Others bucket and methodology: BSE classification of ~4,800 issuers; VRR from 30-Apr-2020; Debt-FAR/MF/AIF AUC from 31-Aug-2024 and net investment from 15-Sep-2024; fortnightly USD conversion uses period-end RBI rate, unlike daily conversion.
- Scoped full equity table transcription and grand-total arithmetic: DOCUMENTED / PASS. Original file bytes/SHA-256, all-category reconciliation, multi-period panel, issuer/index mapping and rolling predictive test remain NOT ACQUIRED / NOT RUN. Hard Gate BLOCKED. No production changes.
- Audit report commit 1fb028b71478d30a755e35a1f4588a9588e5a875, blob 33a0d1cd6deac17ce6157c472054c62eac08155e.


## 47. NSDL official 31-Oct-2026 fortnightly FPI sector update captured — 2026-11-14

- Added `docs/NSDL_FPI_SECTOR_CROSS_SOURCE_UPDATE_20261114.md` from official NSDL report (turn177159search2).
- Grand Total equity net flow: −₹47,955cr for 01–15 Oct and +₹13,112cr for 16–31 Oct; derived October fortnight sum −₹34,843cr. Equity AUC at 31-Oct ₹65,25,808cr; 15-Oct ₹65,94,378cr.
- Auto & Auto Components row: equity flow −₹6,533cr for 01–15 Oct and −₹1,098cr for 16–31 Oct; outflow moderated but did not turn positive. One-row check only.
- The newer NSDL report extends sector history beyond CDSL's 15-Oct report; not a same-date cross-source discrepancy. Full sector extraction and method reconciliation remain outstanding.
- Scoped official report/key total/one-row extraction and arithmetic: DOCUMENTED / PASS. Raw file/hash, full sector panel, all-category reconciliation, aligned historical panel, NSE return join and rolling predictive validation remain NOT ACQUIRED / NOT RUN. Hard Gate BLOCKED; no production changes or PR/merge.
- New report commit: a2e205a40537c3239ceb5f2d2fbf6c56b2e248ef.


## 48. NSDL Grand Total and CDSL/NSDL same-period equity flow cross-check — 2026-11-14

- Official NSDL Grand Total row (turn683882view0 line 32): 01–15 Oct equity net flow −₹47,955cr; 16–31 Oct equity net flow +₹13,112cr; 15-Oct equity AUC ₹65,94,378cr; 31-Oct equity AUC ₹65,25,808cr.
- NSDL all-category totals differ from equity-only: −₹45,828cr for 01–15 Oct and +₹21,354cr for 16–31 Oct. These include other instrument categories and must not be called equity flow.
- Aggregate same-period 01–15 Oct equity flow −₹47,955cr matches the CDSL 15-Oct Grand Total equity net flow −₹47,955cr at displayed ₹ crore precision. This is an aggregate consistency check only; not proof of full row-level identity or full-history coverage.
- Corrected taxonomy: NSDL page contains 22 BSE industry sectors plus Sovereign and Others, not 24 industry sectors. Sovereign is government securities; Others is exposures outside BSE-classified ~4,800 issuer universe.
- Two-period October equity sum −₹34,843cr. Period-end USD conversion rates differ from daily conversion; INR retained as primary unit.
- Scoped aggregate same-period cross-source check: MATCH. Raw immutable file acquisition, full history, row-level all-category reconciliation, index mapping and rolling prediction test remain NOT ACQUIRED / NOT RUN. Hard Gate BLOCKED; no production changes.
- Update report commit 86748460104dc92ab379770946bc964b889790b5, blob 26c72cd52814b9c2c1ed138a4d3ebc4e734d67e3.


## 49. NSDL sector-to-NSE index candidate crosswalk and return-panel contract — 2026-11-14

- Added a 22-sector candidate mapping table to `docs/NSDL_FPI_SECTOR_CROSS_SOURCE_UPDATE_20261114.md`, grounded in NSE Indices' official historical-data index inventory (turn250731view0 lines 59–88, 112–129) and NSE historical report directory (turn783238view2 lines 187–196).
- 17 sector labels have label-aligned candidate indices; Construction Materials → NIFTY CEMENT is proxy-only; Diversified, Forest Materials, Textiles and Utilities have no direct index identified. Services → NIFTY SERVICES SECTOR is broad proxy candidate. NIFTY POWER is not substituted for Utilities. Healthcare is not substituted with Pharma.
- Mapping is not constituent equivalence. Dated index constituent/methodology files are required before return attribution. Historical Nifty Indices CSV supports date-range OHLC; distinguish price index vs total-return index. NSE All Reports identifies CM-UDiFF as the current bhavcopy format and old common bhavcopy as discontinued (turn783238view1 lines 169–225).
- Defined no-lookahead join contract: NSDL report publication availability timestamp -> next eligible NSE session -> H+1/H+3/H+5 forward index returns, 0.22% transaction cost; lag global controls and keep all missing values UNKNOWN. No historical index series downloaded or joined, no predictive performance claimed.
- Scoped crosswalk and validation design completion: 100% (documentation deliverable only). Empirical sector-return panel/backtest: 0% executed in this step / NOT RUN. Overall project: NOT CALCULABLE. Hard Gate BLOCKED. Production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 unchanged; no PR/merge.
- Updated sector report commit e1030ebdc82bbf4574f307d7b88ce8b51f82bd2d, blob 059d30cfef2cc2c3ba4c1aaf16c0284ffb6be22e.


## 50. NSDL 16–31 Oct full 22-sector equity panel transcribed; ₹1cr row-sum residual recorded — 2026-11-14

- Transcribed all 22 BSE common-industry sector Equity net flows for 16–31 Oct from official NSDL report lines 8–29 (turn381834view0; turn198123view0).
- Largest displayed sector inflows: Telecommunication +₹11,065cr and Information Technology +₹10,915cr. Remaining sector values are enumerated in the NSDL cross-source report.
- Row-sum QA: 22 sector rows sum +₹12,519cr; Others equity +₹594cr; Sovereign equity ₹0; combined displayed rows +₹13,113cr vs Grand Total +₹13,112cr. Difference +₹1cr. Recorded as ROUNDING_RESIDUAL_1CR, not exact PASS and not silently allocated to any sector.
- Scoped full 22-sector panel transcription: 100%. Row-sum QA: 100% completed with 1cr residual identified. Empirical NSE sector-index return panel/backtest remains 0% executed / NOT RUN. Overall project remains NOT CALCULABLE; Hard Gate BLOCKED.
- No synthetic data, no forced row adjustment, no date-only join, no production selector/ranking/CORE-672 change, no PR/merge.
- Updated report commit 69e9b702961b98f7fd91b2ad88333b85ba06a0c7, blob 65e45ebe9dd1bb8b19cdcd45b9f3408c18ed5ab6.


## 51. NSE sector benchmark methodology revalidation; uncertain candidate mappings downgraded — 2026-11-14

- Rechecked official NSE Indices historical-data selector and March 2026 equity methodology PDF (turn256653view0; turn256653view1).
- Selector contains NIFTY CAPITAL GOODS, CONSTRUCTION, POWER and TELECOMMUNICATIONS, but the methodology PDF's sectoral index contents does not list these four as sectoral indices; it separately lists thematic families. Downgraded these previous label-aligned candidates to SELECTOR_VISIBLE_METHODOLOGY_SCOPE_UNVERIFIED pending index-specific factsheets/methodologies and dated constituents. This is a correction to prevent name-only false mapping.
- Construction Materials → NIFTY CEMENT remains proxy only. Healthcare mapping also requires point-in-time constituent overlap. Index methodology has differing review schedules and free-float/capping rules; historical constituents must be effective-date aligned (turn302571view1; turn879354search9).
- Historical Index Data and Total Returns Index Values are separate official data outputs. TRI should be primary where available; price-index series must remain separate. No date-range submitted and no CSV bytes acquired in this step.
- Scoped methodology audit/crosswalk correction: 100% complete. Empirical index CSV acquisition and FPI-return panel: 0% executed in this step / NOT RUN. Overall project: NOT CALCULABLE; Hard Gate BLOCKED. No production changes, no PR/merge.
- Updated report commit fee1d32f870d03226775f6e7a4775438f29120e9, blob f36ca7a26f92b6975a9d32a6992d00975c5ba5e2.


## 52. NSE TRI/NTRI distinction and 0.22% transaction-cost convention clarified — 2026-11-14

- Official NSE Indices historical-data page exposes Price Index OHLC separately from Total Returns Index Values, with distinct Total Returns Index and Net Total Return Index columns (turn476755search2).
- NSE explainer states price index excludes dividends while TRI includes/reinvests dividends and is the appropriate benchmark for actual investment returns (turn476755search3).
- Corrected prior generic “TRI primary” wording: preserve Price Index, TRI and NTRI as separate fields; do not relabel NTRI as TRI. Confirm NTRI definition from official methodology before selecting it as primary. Do not assume OHLC for TRI/NTRI.
- Pre-registered 0.22% total round-trip cost formula: net=(1+gross)*(1−0.0022)−1. If the original project convention means per-side rather than round-trip, resolve that from canonical project specification before backtest; do not double-subtract by assumption.
- Scoped methodology clarification: 100% complete. No CSV or historical returns acquired in this step; empirical return panel/backtest remains 0% executed / NOT RUN. Overall project NOT CALCULABLE; Hard Gate BLOCKED. Production invariants unchanged; no PR/merge.
- Updated report commit 8ad4ead22ff186d9248bfd17e237e393d79dcd3f, blob cb49c4aaba8f3220880f0f46d2dac2803663b241.


## 53. Official NSE historical index/TRI output schema and interface state verified — 2026-11-14

- Re-opened official NSE Indices Historical Data page (turn100955view0 lines 383–432, 561–567). Confirmed separate Historical Index Data and Total Returns Index Values groups.
- Price index output schema is Date + OHLC; TRI output is Date + Total Returns Index + Net Total Return Index. TRI does not expose OHLC in the page's displayed schema; do not fabricate it.
- Confirmed directory taxonomy Broad Based / Sectoral / Thematic / Strategy and revalidated candidate names (turn100955view0 lines 9–16, 59–89, 112–129). Navigation directory alone does not prove category/methodology or constituent equivalence.
- Blank unselected state “Select an Index and Time Period” / “No Data Found” is not evidence of no historical data (lines 417–422, 465–471, 554–567). CSV controls exist, but static inspection returned no selected data payload.
- No CSV bytes, row counts, byte size, response metadata or SHA-256 acquired. No undocumented POST endpoints or third-party reverse-engineered API adopted as official contract.
- Scoped official interface/schema audit: 100% complete. Actual historical CSV acquisition/validation: 0% in this step / NOT RUN. Overall project NOT CALCULABLE; Hard Gate BLOCKED. Production invariants unchanged; no PR/merge.
- Updated report commit 5306dff767ef9c739311217967b9b547ecc8a1f3, blob 2bd703c4988f75211208947bc371aecf9db345b2.


## 54. Walk-forward transaction-cost implementation audit — 2026-11-14


## 54. Walk-forward backtest transaction-cost implementation audit — 2026-11-14

### Scope and exact source
- Audited branch `research/corporate-events-rss-collector-v1-20261114`, source file `pipeline/walk_forward_backtest.py`.
- Source blob SHA at audit: `d085f7a2d35a88b4c4eaba65144a429a06961b09`.
- This is a read-only code audit; no code, selector, ranking, thresholds, dataset or workflow changed.

### Findings
- Script header identifies the engine as “PRECISION-WIRES V11.4 Walk-Forward Behavioural Validation”; do not silently label this artifact as V11.3 production-parity.
- Forward outcomes are calculated as `FUT{h}_HIGH_PCT` and `FUT{h}_CLOSE_PCT` from future high/close observations relative to current close. Metrics then evaluate thresholds against `FUT{h}_HIGH_PCT`.
- Full-file literal scan found no transaction-cost, fee, commission, slippage, 0.22 or 0.0022 implementation in this script.
- Therefore the currently implemented target/precision/recall/lift calculations are gross-price excursion measures, not verified net-of-cost returns. The 0.22% convention is not implemented in this script.
- Applying a flat cost to the future-high excursion alone would not establish executable round-trip net return: the high is a maximum excursion, not a defined exit fill. Keep gross excursion targets distinct from executable entry/exit net-return metrics.
- Do not patch production or this research script in this audit. Before any net-performance claim, resolve whether 0.22% is round-trip or per-side from an authoritative project specification, define entry and exit execution prices (including same-session/next-session convention), then implement a separately labelled net-return metric with tests. Preserve gross target labels for comparability.
- This finding does not prove that no other project component applies costs; it establishes only that this inspected walk-forward script does not.

### Report reference
- Report commit: `fa74078fabea97d4018cc39d351d75262bbc2027`; report blob SHA: `80166936c2363bf3a1efe285435949f3368349f6`.

### Status
- Scoped script inspection and cost-presence audit: 100% complete.
- Authoritative 0.22% convention resolution: NOT RESOLVED.
- Executable net-of-cost backtest and tests: 0% / NOT RUN.
- Overall project: NOT CALCULABLE; Hard Gate BLOCKED. No PR/merge; no production invariants changed.


## 55. Walk-forward forward-outcome horizon alignment defect — 2026-11-14


## 55. Walk-forward forward-outcome horizon alignment defect identified — 2026-11-14

### Scope
- Read-only audit of `pipeline/walk_forward_backtest.py`, source blob `d085f7a2d35a88b4c4eaba65144a429a06961b09`, function `future_outcomes`, lines 98–105.
- No code, data, ranking, selector, diagnostic, workflow or production behavior changed.

### Confirmed defect
- Current implementation uses `x.shift(-1).rolling(h, min_periods=1).max()` for both future HIGH and future CLOSE, for h in {1,3,5}.
- Pandas rolling is trailing/backward-looking. After shifting by -1, the rolling window at row t for h=3 covers shifted rows t-2..t, which correspond to original observations t-1, t, t+1; it does NOT cover the required future observations t+1, t+2, t+3. h=5 has the same backward-window alignment defect. h=1 is aligned to t+1.
- Deterministic counterexample: source sequence [10,20,30,40,50], at t=0 and h=3 the current expression returns 20, while the required max of next three observations [20,30,40] is 40. At t=1 it returns 30 instead of max([30,40,50])=50.
- `min_periods=1` also permits incomplete horizons near each symbol's end-of-history to produce partial-window outcomes instead of an explicit unavailable/matured-window state. The global cutoff guard does not guarantee each symbol has h subsequent observations when symbol histories are sparse, newly listed, or have missing sessions.
- Both FUT{h}_HIGH_PCT and FUT{h}_CLOSE_PCT are affected for h=3 and h=5. The downstream target labels WIN10_H3 and WIN20_H5, precision/recall/lift, state performance and missed-winner attribution therefore cannot be treated as valid H+3/H+5 empirical results until corrected and rerun. H+1 alignment is not implicated by this specific rolling-window issue.

### Safe remediation design (not applied)
- Define the forward window explicitly as observations at t+1 through t+h, per SYMBOL in sorted session order; use a forward-aligned/reversed rolling implementation or explicit shift-based max with a full-horizon validity mask.
- Require all h future observations for a matured target; otherwise leave outcome UNKNOWN/NaN and exclude it from both numerator and denominator. Do not classify immature horizons as non-winners.
- Add deterministic unit tests for h=1,3,5 using monotonic and non-monotonic sequences, first/middle/last rows, symbol boundaries, missing sessions and insufficient future depth. Verify no cross-symbol leakage and exact next-h observations.
- Recompute all affected artifacts from the corrected implementation; do not reuse prior H+3/H+5 results. Preserve historical outputs as superseded audit evidence, not silently overwrite or promote them.
- This audit does not authorize any code patch or production integration. Fix requires explicit user approval and a separate research-only change.

### Report reference
- Report commit: `fc73ded0cafaa853e054e57992b0b358bf2b407a`; report blob SHA: `589aeceba6dae82d92ce1e2403f8ebf9defc06a1`.

### Status
- Scoped source inspection and mathematical alignment audit: 100% complete.
- Corrective code change and unit tests: 0% / NOT RUN (no approval requested or applied).
- Re-run of H+3/H+5 event study/backtest: 0% / BLOCKED pending correction.
- Overall project: NOT CALCULABLE; Hard Gate BLOCKED. No PR/merge; all production invariants unchanged.


## 56. Walk-forward immature-horizon label propagation defect — 2026-11-14

### Scope
- Distinct read-only downstream-label audit of `pipeline/walk_forward_backtest.py`; source blob SHA `d085f7a2d35a88b4c4eaba65144a429a06961b09`.
- This does not repeat or replace Appendix 55's forward-window alignment defect.

### Confirmed finding
- In `main()`, each label is formed by comparing `FUT{h}_HIGH_PCT` with its threshold and immediately calling `.astype(int)`.
- A missing/NaN outcome compared with a numeric threshold evaluates False; `.astype(int)` converts it to 0. The subsequent `dropna` on integer labels cannot restore missingness.
- Therefore, even after full-horizon handling is added as designed in Appendix 55, immature per-symbol outcomes can be silently relabelled as non-winners unless label construction preserves missingness.
- A global last-five-date cutoff does not guarantee h future observations for every symbol with sparse/newly listed/missing-session histories.
- No dataset was loaded; affected row counts and empirical impact are NOT MEASURED.

### Impact and safe remediation (not applied)
- False negative training labels can contaminate model fitting/calibration and bias target probabilities.
- Build labels as nullable/missing until a finite, full-horizon outcome exists; assign 1/0 only to mature outcomes.
- Filter each target's training rows by its own mature label; do not force unavailable horizons into class 0.
- Add regression tests for NaN preservation, H+1/H+3/H+5, symbol-specific terminal rows, sparse histories and no missing-to-negative conversion.
- Audit metric/calibration denominators to exclude immature outcomes from both winner and non-winner populations.
- Recompute only after Appendix 55 forward alignment and this label propagation correction both pass tests.

### Status
- Scoped source/logic audit: 100% complete.
- Dataset-level impact count: NOT RUN.
- Corrective code/tests: 0% / NOT RUN.
- Refit/backtest rerun: 0% / BLOCKED pending approved research-only corrections.
- Overall project: NOT CALCULABLE; Hard Gate BLOCKED. No code/data/selector/ranking/diagnostic/workflow/production changes; no PR/merge.

### Report reference
- `docs/WALK_FORWARD_IMMATURE_HORIZON_LABEL_AUDIT_20261114.md`
- Report commit: `0a4d5e77c594e7fc5f4759a43e41bc11443bba56`
