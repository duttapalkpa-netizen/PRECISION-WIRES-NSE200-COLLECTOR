# PRECISION-WIRES V11.3 — Continuity & Acceptance Ledger
Last reconciled: 2026-11-23 (Asia/Kolkata)
Repository: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR

## 1. Non-negotiable project invariants
- Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56 Steps × 12 Filters), Engines A–E and IPO-PLX V2.0 remain unchanged.
- Research-only code is not production integration. No automatic trade trigger.
- UNKNOWN is neither PASS nor FAIL.
- No fabricated data, inferred timestamps, synthetic rows, unsupported source promotion, or proxy substitution.
- ₹0 spend; free official sources only; no paid APIs.
- Retain prior PASS artifacts, Run IDs, manifests and SHA-256 values.
- No PR merge or production integration without explicit user approval.
- Keep CI bounded; do not repeat completed PASS work.

## 2. IIP audit — verified state
- Run #251 / ID 42501079840: 41-vintage audit and independent revision validator PASS.
- Run #254 / ID 42507902637: 41-vintage audit, PIB supplementary snapshot ingestion and independent revision validator PASS; artifact 13628033276; ZIP SHA-256 a988e47f6679def45d3fa3316e5d3207040047a847cd19410458a40db1814f3b.
- Run #254 PIB sidecar: 69 rows = 3 periods × 23 NIC codes; 69/69 exact value match to MoSPI-hosted March-2026 press-release Statement IV. Later snapshot only, not original vintage recovery.
- Legacy 2011-12/NIC-2008 series ends March-2026; April-2026 is the separate 2022-23 series. Do not splice.
- IIP series-transition crosswalk and NIC applicability details remain as recorded in earlier ledger history; no production changes.

## 3. Global Capital Rotation / Macro-Geo status
- Verified NSE archive raw-byte retention and artifact QA are preserved; semantic 200-session issue separately identified in Continuation 60.
- Macro-Geo P0 remains 6/8. Missing required groups include USD/INR and final FPI/DII daily history. Strict Hard Gate BLOCKED; candidate_release_allowed=false.
- Run #45050554515 / artifact #14765264055 ZIP SHA-256 972db66a147c7b67b3a81e24bbfb98eae8a3b23c4f046dea9650e195f7b67703 is accepted only for report-integrity/regression scope, not full Macro-Geo acceptance.
- CDSL current daily FPI confirmed snapshot is distinct from historical archive completeness. NSE provisional exchange trading activity cannot substitute for final depository FPI. CDSL FPI is not DII.
- NSDL archival remains blocked absent written permission; no reverse engineering or unauthorized archival.

## 4. Continuation 61 — CDSL official FPI archive recheck (23-Nov-2026)
- CDSL landing page last updated 18-Nov-2026; linked daily list begins 04-Apr-2025; fortnightly sector reports through 15-Nov-2026 are not daily flows.
- CDSL current daily page showed confirmed custodian/depository FPI activity dated 20-Nov-2026.
- ArchiveDataAfter2009.aspx produced one non-reproducible result and then Internal Error, ticket 439701. No raw bytes, full row count/schema, or SHA-256 captured.
- Evidence report: docs/CDSL_OFFICIAL_FPI_ARCHIVE_RECHECK_CONTINUATION61_20261123.md; commit 6de8a89276688b157c776efd09285583006279a3.
- Final FPI historical ingestion remains BLOCKED/UNKNOWN; >=60 distinct daily dates spanning >=90 days not verified.

## 5. Continuation 62 — CDSL archive retry (23-Nov-2026)
- Preflight: re-read Mother File and current ledger; skipped CDSL Continuations 77/78/61, NSE provisional CSV boundary work (Continuations 59/60), and accepted NSE archive/QA. No repeated raw NSE acquisition.
- Re-opened official CDSL archive URL https://www.cdslindia.com/Publications/ArchiveDataAfter2009.aspx. It returned “Error Occurred / Internal Error Occurred Please try after some time”, TicketNumber 439701, reproducing the same failure ticket from Continuation 61.
- CDSL current confirmed daily page https://www.cdslindia.com/eservices/publications/fiidaily currently renders 20-NOV-2026 with category/route, gross purchases/sales, net INR crore, USD million and conversion rate; figures are based on custodian reports submitted to depositories. This is a current snapshot, not a historical archive.
- Landing page https://www.cdslindia.com/Publications/ForeignPortInvestor.html remains last updated 18-Nov-2026; linked new-format daily list begins 04-Apr-2025. Fortnightly sector reports through 15-Nov-2026 are not daily history.
- Legacy CDSL archive link https://www.cdslindia.com/Publications/FIITrends.aspx renders an interactive date form, page last updated 20-May-2020; no export URL/schema exposed. SEBI FPI directory confirms this as the CDSL archive link, but route identity is not retrieval success.
- No raw archive response, full date list, row count, schema, export request, or SHA-256 captured. >=60 distinct daily dates / >=90 calendar days NOT VERIFIED.
- Result: current confirmed snapshot DISCOVERED; historical archive INTERMITTENT / NOT REPRODUCIBLE; final FPI historical ingestion BLOCKED/UNKNOWN. P0 remains 6/8; strict Hard Gate BLOCKED; candidate_release_allowed=false.
- Evidence report: docs/CDSL_OFFICIAL_FPI_ARCHIVE_RETRY_CONTINUATION62_20261123.md; commit 9fec57885b849ea401f4341a9feed41ac486713d.
- Next action: do not repeatedly retry while ticket 439701 persists. Resume only via an approved auditable browser/session when the archive responds consistently; capture full raw bytes, exact request metadata, all distinct reporting dates, schema, terms/usage boundary and SHA-256. Admit nothing until >=60 distinct valid dates spanning >=90 days. NSE provisional activity remains separate; CDSL FPI is not DII.
- No collector mapping, fixture, source-coverage code, workflow run, or production rule changed.

## 6. Current blockers and next actions
1. CDSL final FPI historical archive: BLOCKED/UNKNOWN until stable official raw archive capture and terms boundary; no repeated retries during ticket 439701.
2. NSDL FPI/DII: BLOCKED pending written permission for archival; no scraping/reverse engineering.
3. NSE provisional exchange activity: separate candidate only; endpoint/schema/usage rights and historical coverage not admitted.
4. FBIL USD/INR: methodology/source identity confirmed; documented historical export/API, terms and raw archive not verified.
5. Once permitted raw source files exist, validate >=60 distinct dates spanning >=90 days, exact raw URL, observation/publication semantics, units/schema, row-level QA and SHA-256 before collector mapping. Only then rerun source coverage, event study and strict hard gate.
6. Keep hard-gate release false unless hard_gate_report.json explicitly says status=PASS, blockers=[], candidate_release_allowed=true and all reports reconcile.

## 7. Research constraints
₹0; official/free sources only; no synthetic rows, fabricated timestamps, interpolation, forward-fill, proxy promotion or untrusted mirrors. UNKNOWN never PASS. H+3 State calibration requires >=50 fully matured observations per State. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A–E and IPO-PLX V2.0 unchanged. No merge or production integration without explicit approval.


## 7. Continuation 63 — NSE session-spine correction readiness (23-Nov-2026)
- Preflight read Mother File through Continuation 57, current Master Ledger through C62, and the C58 FBIL, C59–60 NSE CSV, C61–62 CDSL, NSE semantic audit and failure-lessons reports. PASS work was skipped; no broad workflow or Macro-Geo rerun.
- Independently downloaded artifact #14757294944 from run #45027842316. ZIP SHA-256 `212a84103f2a9f47681865c7e165fe0247001b02d9563a5cef578636fb0b1898` verified. 200/200 retained file byte counts and SHA-256 values match the manifest.
- Independently parsed all 200 CSV internal DATE1 values: only 188 unique observed trading dates. Twelve requested NSE holidays repeat the previous valid session's exact file/hash. The 200-session claim remains NOT_ACCEPTED.
- Code-level root cause verified: `collector/nse_download.py` skips weekends but not NSE holidays; legacy/cached/full-delivery validation does not enforce internal DATE1 == requested trade date; `qa/validate_dataset.py` accepts sessions.txt count >=200 without checking distinct observed dates or manifest/date equality.
- Official NSE CMTR/71775 holiday calendar cross-check supports the 12 duplicate dates. Twelve earlier weekday candidate dates before 16-Feb-2026 were identified: 29–30 Jan and 02–13 Feb 2026 (weekdays only; 26-Jan is excluded as Republic Day). These dates are calendar candidates only, not captured raw data.
- NSE Terms of Use current page prohibits systematic/automated collection and restricts copying/storage absent applicable permission. No project-specific written permission was established. No additional NSE download, endpoint probing, workflow dispatch, code modification or production change was made.
- Evidence report: `docs/NSE_SESSION_SPINE_CORRECTION_READINESS_CONTINUATION63_20261123.md`; report commit `bc2c1bc9bbd9a23bf59b9be6f70b252d00304613`.
- Acceptance: artifact/hash integrity PASS; 188 unique DATE1 audit PASS; 12 holiday duplicate mappings PASS; collector holiday exclusion NOT_IMPLEMENTED; DATE1/manifest QA NOT_IMPLEMENTED; 12 earlier raw sessions NOT_CAPTURED; corrected 200-session archive BLOCKED; walk-forward metrics remain UNKNOWN / NOT_ACCEPTED.
- Exact next action: implement a bounded offline, research-only date-semantic QA regression on retained files; fail closed on DATE1/manifest/holiday mismatch. Do not run automated NSE acquisition until a permitted zero-cost archival route is established. Only after permitted raw files exist and the corrected archive passes 200 unique-session acceptance may label-v2/walk-forward metrics be recomputed.
- Invariants unchanged: ₹0; official sources only; no synthetic data/fabricated timestamps; UNKNOWN never PASS; Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A–E and IPO-PLX V2.0 unchanged; no merge or production integration.


## 8. Continuation 64 — Nightly Rotation Backtest & daily outcome audit (23-Nov-2026)
- Preflight: read Master Ledger through C63, 23-Nov morning Daily Unified Top-5 report, 22-Nov nightly report, existing NSE artifacts and latest workflow runs. Reused Run #420 artifact; no new workflow dispatch and no new NSE source acquisition by this review.
- GitHub scheduled Run #420 / ID 45202379089, job 137788955150, head c9622ba253c8f963736035a77fb94df1682d8d06, SUCCESS; duration 12m11s (exceeds 10-minute target). Artifact #14833925413; ZIP SHA-256 693cb2d8f68cc38a56fd9c17140f6126e11bb1617d6b0fee9ad4d2de5264686d, independently matched after download.
- Processed dataset SHA-256 8d6c634ddbb442bd5003ec96f20fdac8f150b5775f451efd84eeb5262bc12f57; 504,250 rows / 2,999 symbols / 200 date labels. Semantic audit confirms 12 holiday duplicate dates and only 188 valid sessions; QA JSON PASS is not accepted for session semantics.
- Walk-forward source SHA-256 dca7363ef1c5f56a097ed66b4305935f2c90975e2387b9c5b44780c4101f83e2; collector a55e6390f7e4299fc47b812baaa24047bbfae84686e397f1535e08f56c6f7e0f; builder 7190c653a829b56eaf2041a9886cf0b873de0bd2d1af1821ce0bcb80458181a1; QA 2a7590ad14522fa0440ad4609d11e12e0414f5b25f948c10d47c59c025803c19; workflow config 61121eb2b8bde79844c9594c43e8f30a74ffd45a611d135a5f93eb9651b82f13.
- Walk-forward output hashes: metrics 7f07438780eca7a7aaae89fd9bc5ee241025fa8f58952a481f2d78ed0ca1f496; predictions 37f613d6c4368b98e4d14ac41f5cbb0a445b748b4e5d37dc0d94cd514101d16d; full-universe probabilities 625d9f5ca9b18af72f78907df2a2a3370fe067c1c83c86e5eaac45bd9bd0c661; provisional top30 064f4562c6837d2a65e1c3d756988ee510b2da2351cee2f055555c8cd99baf23.
- Validation IDs: PW-DATE-20261123-R420-SESSIONSPINE-01; PW-V114-20261123-R420-POSTHOC-96C-01; PW-ALERT-20261123-H1-OUTCOME-01; PW-MW-20261123-BASE1032-H1-01. These are bounded offline diagnostics, not accepted validation runs.
- Historical V11.4: 96 valid cutoffs after excluding four holiday cutoffs; post-hoc corrected-label metrics/cluster CIs recorded in the dated report as NOT_VALIDATED because the frozen ranking was trained on defective labels and the source spine has 12 duplicates. H+3 State DATA_CONTAMINATED = 26 rows / 22 unique symbols (<50); calibration UNKNOWN.
- Daily H+1: base universe 1,032 unique symbols (EQ, close >₹50, prior 20 valid sessions' average volume >200k). +2% high-touch: 261 winners, 1 selected hit, 260 missed; +5%: 41 winners, 0 selected, 41 missed. WELSPUNLIV +3.80% high / +0.74% close / −2.52% adverse. Eight-symbol shadow cohort separately: +2 high-touch 2/8, +5 1/8; H+3/H+5 immature. Raw source manifest/publication timestamps absent, so daily outcome figures are NOT_VALIDATED / provenance PARTIAL.
- Close-to-close is reported separately; executable trade win remains UNKNOWN / NOT_AUTHORIZED. V11.3 replay not run. GCR remains UNKNOWN/BLOCKED; live 1m source 403, GDELT/RSS errors, one-day FII/DII snapshot only. Latest IMF EMDE Run #1395 failed; no job/artifact surfaced.
- H+3/H+5 maturity correction: for 20-Nov cutoff, H+1=23-Nov, H+3=26-Nov and H+5=30-Nov after the 24-Nov holiday. Morning report's 25-Nov/27-Nov maturity dates were one session early. Existing lesson IDs updated and new lessons PW-LSN-20261123-003 through -010 appended; duplicate holiday/label lessons were not recreated.
- Report: NIGHTLY_ROTATION_BACKTEST_RESEARCH_REVIEW_20261123.md; report commit 21ade4ee39b9693f89d4ac8ece316bab79854807; report SHA-256 7c0210b8bb8e55279df65d2974658338f510b1342c716276c65e4f92ae7c928e.
- Lessons Register: FAILURE_LESSONS_LEARNED_20261123.md; commit 40dd31048202338fb970d31dd32f0438e6973cd4; SHA-256 c52ae39fc0b03d3ab7231c1065adf23fecc187c54deab3ea19a75c3d02a8f70d.
- Acceptance: artifact ZIP integrity PASS; 12 holiday duplicates VERIFIED; source manifest PARTIAL; 188 valid-session semantic audit PASS; 200-session claim NOT_ACCEPTED; forward labels BLOCKED; H+5 JSON/CSV parity BLOCKED (619 JSON-implied vs 622 CSV hits); V11.4 NOT_VALIDATED; V11.3 NOT_AUTHORIZED; GCR BLOCKED; daily missed-winner attribution PARTIAL.
- Next actions: offline holiday/date-semantic regression on retained artifacts; exact forward-label v2 test only after separate approval; full 1,032-row candidate-decision export and denominator reconciliation. No production or selector changes.
- All invariants unchanged: ₹0, free official sources only; no synthetic data, forward-fill, guessed mappings, fabricated timestamps or look-ahead; UNKNOWN never PASS; Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2.0 unchanged; Observation-only.


### Continuation 64 — Addendum 1: final report/lesson hashes and Best-3 status (23-Nov-2026)
- Supersedes the initial report/lesson file references in C64 without deleting history.
- Final report commit: 12b3996f794cf0e3c29d715f48a1e0951d36c586; final report SHA-256: 7dd603986f940f1ec0a8c859684e5bcf2f9cbcfb829cc3a9b84128a72699df8d.
- Final Lessons Register commit: e022360a2fb28dc178d3f027b716a8520c06e595; SHA-256: 03b48fa405607a8188910c5dec0630323830561af1661a8e0595cce6ffdb17df.
- Correct source file SHA-256: 23-Nov morning alert d227479be9d83bb0966765aef0ef5ab73d2a055b599fa7aadcfe04ce51b55d01; 22-Nov nightly report d42514bdf1d34cf84573c60c55d83f5f7c63cca232468d2efd56ede3c36ac7ab.
- Selection code identities: pipeline/v11_3_abcd_e.py 7800ff3c39b0c58a3162fb196b4f0efaa023dfe3adbeefc5fbe2d5fb0c6a8bbd; pipeline/risk_modifier.py 994ac0d6637c7733e73c9756a6e5e4228d9e0bec34b25055d535ab1a9835dd0a. config/universe.csv 6a8c89061b367041c4d0e1ab84ba684d0a5e2615674827ebdcc236b361efecb9 is header-only; alert orchestration hash and row-level decisions remain unavailable.
- Best 3 Stocks per Target: all five target-specific historical lists UNKNOWN/BLOCKED; WELSPUNLIV remains an unranked observation-only prospective candidate, not a Best-3 rank.
- All run/artifact evidence and acceptance states remain as C64. No selector, ranking, threshold, code, production admission or trade assumption changed.


### Continuation 64 — Addendum 2: final GitHub read-back hashes (23-Nov-2026)
- Final report commit: 12b3996f794cf0e3c29d715f48a1e0951d36c586; SHA-256 of exact GitHub read-back content: e8b9d3cccfcecff08cacbe2176d2c010cad1057f5814df1d1e975288b61f2c84; blob SHA-1 c37aed7564cb2b68dcfbac1da0a8615c512c6f13.
- Final Lessons Register commit: 6c4ee00e0de6fc83ab249be541fb22a687ba1b65; SHA-256 of exact GitHub read-back content: 2edbde8c37ba6fc909fdf3925b72577b98ccdd8e4d92dfbe659b16128a4fc3a2; blob SHA-1 ee43f72cc5220373dff7312d94e3525139b84d0c.
- These exact read-back hashes supersede the pre-write hashes in C64/Addendum 1. The report and lessons contents were read back from GitHub after commit; no data/selector/production change occurred.


## 9. Continuation 65 — Daily Unified Top-5 Pre-Market / holiday session (24-Nov-2026)
- Preflight: read Master Ledger through C64, 23-Nov morning report, 23-Nov nightly rotation report, 23-Nov Failure & Lessons Register, NSE 200-session semantic audit, latest workflow runs and existing artifacts. PASS byte-integrity work was reused; no new NSE acquisition or workflow dispatch.
- Market status: 24-Nov-2026 is an NSE Capital Market trading holiday (Prakash Gurpurb Sri Guru Nanak Dev); next equity session 25-Nov-2026.
- Reused Run #420 / ID 45202379089 (SUCCESS; job 137788955150; 12m11s, exceeding 10-minute target), artifact #14833925413; ZIP SHA-256 693cb2d8f68cc38a56fd9c17140f6126e11bb1617d6b0fee9ad4d2de5264686d independently matched. Processed dataset SHA-256 8d6c634ddbb442bd5003ec96f20fdac8f150b5775f451efd84eeb5262bc12f57; 504,250 rows / 2,999 symbols / 200 labels but only 188 unique valid sessions and 12 holiday duplicates. Semantic 200-session acceptance NOT_MET.
- Reused Run #409 / ID 45282753297 (SUCCESS; job 138071166956; 8m19s), artifact #14870843264; ZIP SHA-256 462728add6a22efc8f76174b7578d559ac5f7f1d1ed72c1c8919c4ad6f4074d9 independently matched. latest_picks.csv SHA-256 5f451b59076912318d1f36e893dfeee8657ad378cc040111c66f650015ebea56.
- Final selection status remains PROVISIONAL_ONLY_FINAL_SELECTION_BLOCKED; blockers RISK_GEO_NOT_AVAILABLE and LIVE_INTRADAY_1M_FEED_MISSING (HTTP 403; zero rows). Provisional Top-3/Top-10 and seven-symbol shadow cohort were not promoted. Qualified candidates = 0.
- A engine: strict 30-matured-cutoff shadow audit only; +5 CURRENT 40/150 (26.67%, FP 110), P10_P20 31/150 (20.67%, FP 119); +10 CURRENT 31/150 (20.67%, FP 119), P10_P20 33/150 (22.00%, FP 117); +20 CURRENT 18/150 (12.00%, FP 132), P10_P20 14/150 (9.33%, FP 136). +2/+15 UNKNOWN. Exploratory only, not accepted; Best-3 all targets UNKNOWN. B UNKNOWN/NOT_AUTHORIZED; C UNKNOWN/BLOCKED.
- Prior WELSPUNLIV H+1 outcome: +2 high-touch HIT, close-to-close +0.74% MISS, +5 H+1 MISS, adverse excursion -2.52%. The seven-symbol 23-Nov shadow cohort (BI, KDDL, ONIXSOLAR, SALASAR, SHALPAINTS, SHARDUL, UFBL) remains PENDING until H+1 25-Nov close, H+3 27-Nov close, H+5 01-Dec close.
- 20-Nov cutoff 1,032-symbol base-universe retrospective audit: +2 H+1 high-touch 261 winners / 260 missed; +5 41 winners / 41 missed. Full per-symbol decision export absent; remaining cases UNKNOWN. Six representative incident rows are carried forward; no hindsight-only predictive signal added.
- New lessons: PW-LSN-20261124-001 runtime 12m11 >10m target; PW-LSN-20261124-002 fail-closed readiness/source health (GEO missing + live feed 403); PW-LSN-20261124-003 high-touch vs close-to-close label divergence. Existing PW-LSN-20261123-001 through -010 updated/carried forward, not duplicated.
- Dated report: docs/DAILY_UNIFIED_TOP5_SWING_WATCHLIST_20261124.md; commit 731e1ff9af41be3b6ddf23c69af37b6dbd59f0c0; GitHub read-back SHA-256 734a6bb2010d46398a0f3a6e1cba86fa97c6194b1983a87278583b07000cccc7; blob 6356694126d6fa65cb1a5c0dde290f386b86a650; exact read-back content matched.
- Dated lessons: docs/FAILURE_LESSONS_LEARNED_20261124.md; commit b869025280a0c22182fb11ced97c605f0c87621f; GitHub read-back SHA-256 9bdb423ddc5f59c48a92f69c7a1e5a3cf20d536c08e7cb50519fb06139fde708; blob 1a2d382ee643369547638284a8c59cc7af863423; exact read-back content matched.
- Acceptance: artifact ZIP byte/hash integrity PASS; 188 unique session semantic audit PASS; 200-session claim NOT_ACCEPTED; V11.4 NOT_VALIDATED; Best-3 UNKNOWN; V11.3 cost-aware replay UNKNOWN/NOT_AUTHORIZED; GCR UNKNOWN/BLOCKED; current qualified candidates 0.
- No new NSE data acquisition, no workflow dispatch, no production change. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2.0 unchanged. ₹0; official/free sources only; UNKNOWN never PASS.


### Continuation 65 — Addendum 1: final report Markdown normalization (24-Nov-2026)
- Daily report was re-read and its status marker normalized to standard GitHub Markdown; no research data or decision changed.
- Final report commit: 3cde33447fe7e1349f84b8cce0a989e9acc5b3ad; final blob: 17a76517efb3285c5abe7e52953b009d070926d6; exact GitHub read-back verified; SHA-256 5a6a388e1030c09d5cbaf5d8d8aa96c69b5c6331db79985da8a83261b76464ca.


## 10. Continuation 66 — Data Export Attachment Recovery Phase 2 (24-Nov-2026)
- Preflight read Phase-1 Recovery Audit, Mother File Continuation 57, recovered-work index and current ledger through C65. Pre-update ledger blob SHA: 4dc8e4e7812ea9fdf56e9606ac56004231fc62d9. No accepted PASS work repeated.
- Rechecked 147 conversation records: 378 attachment metadata entries (322 image/JPEG, 56 non-image); non-image subset = 55 unique attachment IDs and 53 distinct filenames. One attachment ID occurs twice. Metadata does not establish payload-byte recovery.
- Five priority Library files independently materialized and hashed; CSV row parsing and ZIP/XLSX container checks completed. SHA-256:
  - Operational-layer CSV: 5acea71d5c3961d68727718cb99622d2854ac94a748588b3f5500d0d35fceef7 (2,650 data rows).
  - Merged NSE bhavcopy CSV: e65146b4d466eec988d0d3b92a31d6f3b7acd316c45535ef283eafa2183781ce (666,867 data rows).
  - IMF PA ZIP: 8cb2ed4bd96c0b1c4d3f24d0530771a5868f55bba256213404d5acf22a3f2b45 (ZIP test PASS, 4 entries).
  - Macro-Geo event-study ZIP: 3e0d07946dd54b54aeb53ea0aa02e7d49b818c08cda93ce28ac56b582f7e4b38 (ZIP test PASS, 32 entries).
  - NSE_MASTER_DATA_1.xlsx: d98a484dfe32474cf9a31d7a21c95dadaaafa543185d2c0790ab0d794097e676 (XLSX container test PASS, 25 entries).
- These are Library-byte integrity checks only; they do not prove equality with export .dat payloads. Full 53-name reconciliation and 322-image audit remain open.
- export_manifest.json remains NOT_PROVIDED; .dat payload mapping and original export-byte equivalence remain BLOCKED/UNKNOWN. Next exact action: obtain only export_manifest.json, map attachment ID → original filename → .dat path → expected/actual size/hash, and only then select critical payloads.
- Report: docs/PRECISION_WIRES_V11_3_DATA_EXPORT_RECOVERY_AUDIT_PHASE2_2026-11-24.md; report commit 63b17e951857440538d0ee4c1d058e3f12236b99. Library copy saved at /PRECISION-WIRES Research Archive/PRECISION_WIRES_V11_3_DATA_EXPORT_RECOVERY_AUDIT_PHASE2_2026-11-24.md.
- No NSE acquisition, workflow dispatch, production/selector/ranking/threshold change or merge. ₹0; official/free sources only; UNKNOWN never PASS; CORE-672, Engines A–E and IPO-PLX V2.0 unchanged.


## 11. Continuation 67 — Attachment metadata index Phase 3 (24-Nov-2026)
- Preflight re-read GitHub Master Continuity Ledger through C66 and Phase-2 Recovery Audit. Current pre-update ledger blob SHA: 1fd2ba68c48c97c361b5a442b682731051399397. Existing byte-verification PASS items were not repeated.
- Re-ran a complete 975-item Library filename/path scan and semantic search for export_manifest.json, manifest, export, attachment and .dat. No original ChatGPT export_manifest.json and no .dat payload files were found. Domain-specific research manifests are unrelated and were not substituted.
- Built a row-level metadata index from the two supplied conversation JSON files: 147 conversations; 378 attachment entries; 322 image/jpeg; 56 non-image; 55 unique non-image IDs; 53 unique non-image filenames. One non-image ID (file_00000000b08082118f5b1409a80fd4a5) appears twice and both rows were retained.
- CSV index SHA-256: a7d85e4a1f85b90841f2ae5815d311911e50387125dabfc90a6c4e02584483c2. CSV and summary JSON saved in Library under /PRECISION-WIRES Research Archive/.
- Acceptance: metadata index construction PASS; export-manifest discovery NOT_FOUND; .dat mapping BLOCKED; payload size/hash comparison UNKNOWN/NOT_RUN. Metadata is not payload evidence; no claim of full attachment recovery.
- Report: docs/PRECISION_WIRES_ATTACHMENT_METADATA_INDEX_PHASE3_2026-11-24.md; commit e6d82d6dc33dd2bc7602810b8b02091023300d8c; GitHub read-back blob 7110355d91933392d6558c110f99e260d6bc3f01.
- Exact next action: obtain original export_manifest.json from the same ChatGPT export package, then join attachment ID → .dat path and compare expected/actual bytes and hashes. No manifest reconstruction/fabrication.
- No production, selector, ranking, threshold, workflow or data-acquisition changes. ₹0; UNKNOWN never PASS; CORE-672, Engines A–E and IPO-PLX V2.0 unchanged.


## 12. Continuation 68 — Attachment Library reconciliation Phase 4 (24-Nov-2026)
- Preflight re-read current Master Continuity Ledger through C67, Phase-2 Recovery Audit and Phase-3 Attachment Metadata Index report. Pre-update ledger blob SHA: c2ba1eff3a3b6e8704c2167312e32be050e66d59. Prior PASS byte/hash/container checks and metadata-index construction were reused, not repeated.
- Completed a paginated full Library listing: 959 file items. Reconciled 53 unique non-image filenames from the 56 metadata rows against exact Library filenames and source byte counts.
- Exact filename found: 51/53. Exact filename plus byte-size match: 51/53. Size mismatches among found names: 0.
- NOT_FOUND: CF-AN-equities-02-Aug-2026.csv (8,064 expected bytes); cpi_2479.xlsx (166,608 expected bytes; metadata carries a Library ID but current full listing does not resolve that exact filename, so pointer treated as stale/unresolved).
- 19 filenames have duplicate exact-name Library paths; two FII/DII filenames have three paths each. No duplicate was merged, overwritten or deleted. No similarly named substitution.
- Acceptance boundary: name/size reconciliation 51 PASS, 2 NOT_FOUND; cryptographic equivalence to export .dat remains UNKNOWN/NOT_RUN because original export_manifest.json and .dat paths are still absent. Same name and size do not prove identical bytes. 322-image audit remains open.
- Report: docs/PRECISION_WIRES_ATTACHMENT_LIBRARY_RECONCILIATION_PHASE4_2026-11-24.md; commit 13df33f8806379e57b647435879f9a59ac22bb14; GitHub read-back blob 6f7f56e51b964da93e8abfd9c3bc235b8438bf43.
- Exact next action: obtain the original export_manifest.json from the same export package and perform ID→.dat path→expected/actual size/hash reconciliation. Separately locate/re-upload only the two unresolved named files if required.
- No NSE acquisition, workflow dispatch, production/selector/ranking/threshold change, merge or data mutation. ₹0; no paid services; no external contact; UNKNOWN never PASS; Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2.0 unchanged.


## 13. Continuation 69 — Image attachment Library reconciliation Phase 5 (24-Nov-2026)
- Mandatory preflight: re-read Master Continuity Ledger through C68 (pre-update blob SHA 03cf9358978cfcc8c15995ed9455a16cfd3b1265), Phase 2 recovery audit, Phase 3 metadata-index report, and Phase 4 non-image Library reconciliation report. Reused previous accepted work; no duplicate byte/hash checks.
- Re-opened Phase 3 CSV metadata index from Library and completed a fresh paginated Library listing: 1,121 file items. Isolated the 322 image/jpeg rows.
- Image metadata inventory: 322 rows, 322 unique attachment IDs, 315 distinct filenames; seven filenames occur twice and both source rows were retained. None of the image rows carried a Library ID in the Phase 3 index.
- Exact filename present in current Library: 106/322; exact filename plus byte-size match: 106/322; exact-name byte-size mismatch: 0; exact filename not found: 216/322. Source sizes span 26,621–203,816 bytes.
- Acceptance: image metadata inventory count/uniqueness PASS; Library filename+size reconciliation 106 MATCH / 216 NOT_FOUND / 0 SIZE_MISMATCH. Name and size do not prove byte identity or export provenance. Original export_manifest.json and image .dat paths remain unavailable; SHA-256 payload equivalence UNKNOWN/BLOCKED. Missing rows are not asserted deleted.
- Report saved to Library: /PRECISION-WIRES Research Archive/PRECISION_WIRES_IMAGE_ATTACHMENT_LIBRARY_RECONCILIATION_PHASE5_2026-11-24.md (file_id file_00000000dc248211b1c577770d7ff70c; library_file_id libfile_a4cda6404688819192a658683e25b47d).
- GitHub report: docs/PRECISION_WIRES_IMAGE_ATTACHMENT_LIBRARY_RECONCILIATION_PHASE5_2026-11-24.md; commit efb02ef5cc5ffa73f7d41bd4fdd0572f06367917; read-back blob SHA 9bdd42e7e3560a4d49763a2d9112b661ed614049.
- Next action: obtain original export_manifest.json from the same export package; map all image attachment IDs to exact .dat paths and compare expected/actual sizes and SHA-256. No fabricated paths or hashes.
- ₹0; no paid services, external contact, NSE acquisition, workflow dispatch, production/selector/ranking/threshold change, merge or data mutation. UNKNOWN never PASS; Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2.0 unchanged.


## 14. Continuation 70 — Image attachment recovery checklist Phase 6 (24-Nov-2026)
- Mandatory preflight re-read C69 ledger (pre-task blob SHA 0d1c1446c4005c4fece8f456f78ec02498cff871), Phase 3 metadata-index report/CSV, Phase 4 non-image reconciliation report, and Phase 5 image reconciliation report. Prior PASS checks were reused, not repeated.
- Fresh full paginated Library listing: 1144 items; no warnings. Reconciled all 322 image/jpeg metadata rows against exact filename + source byte size.
- Result: 106 matches and 216 NOT_FOUND rows. Built a row-preserving recovery checklist with attachment ID, filename, expected size, conversation title/ID, message ID and role. Duplicate source filenames were retained as distinct rows.
- NOT_FOUND means no exact filename+size match in the current Library listing; it does not establish deletion or irrecoverable loss. Alternate/renamed files were not inferred.
- Checklist CSV: docs/evidence/attachment_recovery/PRECISION_WIRES_IMAGE_ATTACHMENT_RECOVERY_CHECKLIST_PHASE6_2026-11-24.csv; commit 0be39c7bf74e4c6c857797a873f1cfbeb0ab66ac.
- Report: docs/PRECISION_WIRES_IMAGE_ATTACHMENT_RECOVERY_CHECKLIST_PHASE6_2026-11-24.md; commit 39aea60b6ca171ed5064f3082cbbe09e17455095.
- Original export_manifest.json, .dat paths and expected hashes remain unavailable; cryptographic payload identity UNKNOWN/BLOCKED. The 106 prior matches remain presence-only, not byte-identity proof.
- Next action: obtain the original export_manifest.json and same-export payload package; then join attachment IDs to exact .dat paths and compare actual size/SHA-256. Do not fabricate paths or hashes.
- ₹0; no paid services, external contact, NSE acquisition, workflow dispatch, production/selector/ranking/threshold/merge/delete changes. UNKNOWN never PASS; Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E, IPO-PLX V2.0 unchanged.


## 14. Continuation 70 — Nightly Rotation Backtest & Research Performance Review (24-Nov-2026)

- Preflight re-read Master Continuity Ledger through C69, 24-Nov Daily Unified Top-5 report, 23-Nov nightly report, 24-Nov Lessons Register, retained archives, latest runs and artifact metadata. Existing accepted ZIP byte-integrity work reused; no repeated download of Run #420/#409 and no new NSE acquisition.
- Reused scheduled Run #421 / ID 45422367928; job 138545045702; conclusion SUCCESS; head commit 7cf2292e467ffebf8c95ae67981570ab4d13a2ca; duration 12m06s (10-minute target exceeded). Artifact #14936656169, 62,184,126 bytes; GitHub digest and downloaded ZIP SHA-256 independently matched: d57374c50a8b8e2fe5710fd57660225ea59a2beffd639cb9e83b77e734499954.
- Dataset nse_eq_200_sessions.csv SHA-256 9f4f4305221a0b901a92088d22ffc5795614daeb2d6f78c013c78c6ec4f929f1; 504,610 rows / 2,999 symbols / 200 DATE labels. Independent exact-content audit excluding DATE found 13 official holiday duplicate pairs: 02/03-Mar, 25/26-Mar, 30/31-Mar, 02/03-Apr, 13/14-Apr, 30-Apr/01-May, 27/28-May, 25/26-Jun, 11/14-Sep, 01/02-Oct, 19/20-Oct, 09/10-Nov, 23/24-Nov. Every pair was identical across all non-DATE fields for all symbols in the pair; only 187 unique daily content sessions. Official NSE holiday calendar circular CMTR/71775 confirms those 13 holiday dates. 200-session semantic acceptance NOT_MET.
- QA report SHA-256 48547e28ff82e978c8b63712c9fc5e4692268c3c99fba015bd1bfa3d7bd1af19 still says PASS; code inspection shows QA counts raw file/session labels and duplicate SYMBOL+DATE but not unique semantic dates or source DATE1 parity. Collector validator does not compare source date to requested stamp; builder assigns DATE from filename. QA PASS therefore NOT_ACCEPTED for session semantics.
- Walk-forward code at run head: Git blob SHA-1 d085f7a2d35a88b4c4eaba65144a429a06961b09; known source SHA-256 dca7363ef1c5f56a097ed66b4305935f2c90975e2387b9c5b44780c4101f83e2. shift(-1).rolling(h,min_periods=1).max() remains; H+3/H+5 trailing/partial; close outcome is max close, not terminal T+h close. Exact forward labels remain BLOCKED.
- Walk-forward output: 100 cutoffs, 3,000 Top-30 prediction rows / 1,109 unique selected symbols; full-universe file 252,656 rows / 2,902 unique symbols. Metrics JSON SHA-256 ee6624f046bd910491eac0e94d90006200abb23576990b8d5570bb3ebc36d440 and contains no CI fields. H+5 JSON implies 629 hits while prediction CSV has 632 rows >=20% (3-row discrepancy); predictions SHA-256 e80410b11cfaf8834af774c7e0e3ed39901efd5ce63b0ed2623dd5fef46a6951; universe probabilities SHA-256 356dc3329f28fb38e6cf6920f1564f3febf7b04f98dbe36dc4da887ca9bd96a9. No validated Precision/Recall/F1/capture rate or CI accepted.
- Three tracks remain separate: V11.4 NOT_VALIDATED; V11.3 cost-aware replay UNKNOWN/NOT_AUTHORIZED; GCR UNKNOWN/BLOCKED. H+3 State calibration UNKNOWN; contaminated rows do not count toward the >=50 fully matured requirement.
- 24-Nov morning alert: NSE holiday, qualified candidates 0; final readiness PROVISIONAL_ONLY_FINAL_SELECTION_BLOCKED due live 1m HTTP 403 / zero rows. No 24-Nov symbol matured. 23-Nov seven-symbol shadow cohort remains pending: H+1 25-Nov close, H+3 27-Nov, H+5 01-Dec. All target-wise verified unique capture counts/rates UNKNOWN; denominator 0 for today's alert, not 0% capture. Best-3 all targets UNKNOWN/BLOCKED.
- Previous Run #420: 200 labels / 188 unique sessions / 12 holiday duplicates; Run #421: 200 labels / 187 unique content sessions / 13 duplicate pairs. No comparable performance change; archive semantic status worsened by one duplicate. Runtime improved only 5 seconds (12m11s to 12m06s), still over 10 minutes.
- Existing lesson IDs updated: PW-LSN-20261121-001 (forward labels/terminal-close semantics), PW-LSN-20261121-002 (H+5 JSON/CSV 629 vs 632), PW-LSN-20261123-001 (13 holiday duplicate pairs), PW-LSN-20261124-001 (runtime), PW-LSN-20261124-002 (source readiness); PW-LSN-20261124-003 carried forward without new occurrence. New immutable lesson PW-LSN-20261124-004: metrics evidence contract lacks CI and unique-symbol denominator reconciliation; acceptance OPEN.
- Observation-only research note added for CI + unique-symbol/signal-row denominator evidence contract. Next actions: offline holiday/session-spine QA on retained artifact; exact label-v2 pilot only after separate user approval; canonical H+5 parity and full candidate-decision denominator export. No new validation run or 120-minute workflow dispatched.
- Dated report: docs/NIGHTLY_ROTATION_BACKTEST_RESEARCH_REVIEW_20261124.md; commit 9f11c8184863eb56c6bf1e701e3cfd2189bbddeb; exact GitHub read-back SHA-256 8b8fc16ea166155484d0696b85001ec3c0543cc292e80038559426c6a9d40538; blob SHA-1 7f894effa068971edc8940e03a665d1e9bbf4eff.
- Lessons Register: docs/FAILURE_LESSONS_LEARNED_20261124.md; commit 80d909602875ebaba25a3c5c5251dde883bd5589; exact GitHub read-back SHA-256 ba91c3f1bd2629e1989c8a99f14442cb0648add4440efe95959fd8f909bffdda; blob SHA-1 9081a370d55db7aa36fee7424adaf50590762387.
- Acceptance: artifact ZIP integrity PASS; semantic 200-session claim NOT_ACCEPTED; V11.4 NOT_VALIDATED; V11.3 NOT_AUTHORIZED; GCR BLOCKED; Best-3 UNKNOWN; current qualified candidates 0; all production invariants unchanged. ₹0; UNKNOWN never PASS; Observation-only.

## 15. Continuation 71 — Export Manifest source-validity audit (24-Nov-2026; গবেষণা 56, Part-1)
- Mandatory preflight: fetched the current default-branch Master Continuity & Acceptance Ledger through C70 (pre-update blob SHA-1 `27c5a73d56e646430ccb1aa87d994feb23b90abe`); re-read the C70 Phase-6 attachment recovery checklist, C70 Nightly Rotation Backtest review, 24-Nov Failure & Lessons Register and 24-Nov Daily Unified Top-5 report. Prior PASS work was reused; no 1,144-item Library scan, 322-image reconciliation, 106 filename+size matching, or previous artifact ZIP/hash checks were repeated.
- Library exact-title search found `export_manifest.json`: file ID `file_00000000c34482119ed5bb0b14dea4a0`, 171 bytes, JSON version 1. Materialized exact bytes at `/mnt/data/files/export_manifest.json`; JSON parse PASS. All five arrays (`artifacts`, `incomplete_corpora`, `inventory_warnings`, `omissions`, `redactions`) are empty. `requested_at` = `2026-11-22T16:45:12.659530+00:00`. SHA-256 `7181b2bbce551969efa1dfdb8525e68e7efbabbf782d629b90752236492f0abe`.
- Acceptance: Library discovery, JSON syntax and exact-byte hash capture PASS. Original ChatGPT export manifest identity NOT_VERIFIED; attachment ID→`.dat` path mapping BLOCKED; expected-vs-actual payload size/SHA-256 verification UNKNOWN; recovery of C70's 216 NOT_FOUND image rows NOT_DONE/BLOCKED. A matching filename is not proof of package provenance. C70 remains 322 image rows / 106 exact filename+size matches / 216 NOT_FOUND / 0 size mismatches; these are presence-only, not byte identity.
- Evidence report: `docs/PRECISION_WIRES_EXPORT_MANIFEST_SOURCE_VALIDITY_AUDIT_C71_2026-11-24.md`; commit `cff0e0508b15b57e05d5e3590e65bda973e61ff0`.
- Failure Lessons Register updated with immutable lesson `PW-LSN-20261124-005` (filename is not provenance; schema-valid empty inventory is not an attachment recovery manifest); commit `a938fb7f6dc4fd46606ed49e5cbdf35c4305e57c`.
- Exact next action: obtain the original ChatGPT export ZIP or extracted root containing its genuine manifest and `.dat` payload directory; verify package relationship; map attachment ID→filename→exact payload path→expected/actual size and SHA-256. Do not inspect all `.dat` files before manifest mapping; do not fabricate mappings or hashes.
- No NSE acquisition, workflow dispatch, paid source, external contact, production/selector/ranking/threshold/merge/delete change. ₹0; UNKNOWN never PASS; Production Selector, `RANKING_SCORE`, `+1 PRESSURE_FADE`, CORE-672 (56×12), Engines A–E and IPO-PLX V2.0 unchanged.


## 16. Continuation 72 — Pre-task reconciliation and export-recovery blocker decision (25-Nov-2026)
- Mandatory preflight completed: re-fetched current ledger through C71, C71 source-validity report, C70 Phase-6 recovery checklist, Mother File, data-export recovery Phases 1–2, GCR priority queue and task registry. Previously accepted scans, attachment reconciliations and hash checks were skipped.
- Highest-value next action remains C71 original ChatGPT export ZIP / extracted root recovery. Scoped Library search for original export ZIP, extracted .dat payload root and genuine attachment manifest did not surface the package. C71's 171-byte export_manifest.json remains valid-but-empty and cannot map attachment IDs to payloads.
- No payload mapping or bulk .dat scan was attempted; package provenance is a hard prerequisite. C71 remains BLOCKED pending the user's original export package.
- Bounded read-back of existing Run #421 artifact #14936656169: ZIP 62,184,126 bytes; SHA-256 d57374c50a8b8e2fe5710fd57660225ea59a2beffd639cb9e83b77e734499954, matching C70. Independent fingerprint again found the 13 previously documented identical-content date pairs among 200 labels (187 unique content sessions); this is confirmation only, not a new PASS. QA JSON still reports PASS despite the semantic duplicate issue.
- Final selection remains PROVISIONAL_ONLY_FINAL_SELECTION_BLOCKED; live 1m status is HTTP 403 with zero rows/symbols. No candidate qualification or release.
- C72 report: docs/PRECISION_WIRES_CONTINUATION72_PRETASK_RECONCILIATION_AND_BLOCKER_DECISION_20261125.md; report commit 2aa6625c5e0d7184ed122d4c996955bb759e4274.
- Exact unblock requirement: original ChatGPT export ZIP or extracted root containing the genuine manifest and matching .dat payload directory. After receipt, verify package relationship before ID→path→size/SHA-256 mapping; process project-critical payloads in bounded batches.
- No NSE acquisition, workflow dispatch, paid source, external contact, or production/selector/ranking/threshold/merge/delete change. ₹0; UNKNOWN never PASS; all production invariants preserved.


## 17. Continuation 73 — Export manifest and Library payload inventory audit (25-Nov-2026)
- Re-read C72 and controlling C71/C70/Phase-1/2 reports; prior scans not repeated. Recursive paginated Library listing: 1,288 file items, no warnings.
- New inventory-bearing `export_manifest(2).json` found (210,361 bytes; Library file ID `file_00000000813c8211a09a53aa71cf8bb1`). JSON parse PASS; schema `export_files`, `logical_files`, `manifest_file`, `version`; version 1; manifest_file `export_manifest.json`.
- Manifest declares 821 export files: 807 `.dat`, 12 `.json`, one `.txt`, one `.html`; total declared uncompressed size 720,697,430 bytes. User's 822-item count is consistent with 821 entries plus the manifest, but package provenance is not yet established.
- Current Library snapshot contains 292 `.dat` files (181,836,813 bytes); only 191 have strict file_<32hex>.dat names. This is inventory-only, not an exact manifest join. Expected-vs-actual paths/sizes/SHA-256 remain NOT_DONE.
- Additional 210,361-byte manifest copies exist; matching size/snippets are not cryptographic equality. Three 171-byte empty manifests remain distinct and must not be accepted as the inventory manifest.
- Acceptance: inventory-bearing manifest discovery and JSON parse PASS; original ZIP/package provenance UNKNOWN; 821-entry payload reconciliation NOT_DONE; byte identity NOT_DONE. Next: reconcile manifest expected names/paths/sizes to Library files, then hash only exact mapped payloads in bounded batches. Preserve original package; do not bulk-scan unrelated files.
- Report: docs/PRECISION_WIRES_CONTINUATION73_EXPORT_PACKAGE_LIBRARY_INVENTORY_AUDIT_20261125.md; commit e2baa6e76b2b8ad16e71b2a64025a9118838722d. Read-only, ₹0; no external contact, workflow dispatch, NSE acquisition, or production/selector/ranking/threshold changes. UNKNOWN never PASS.


## 18. Continuation 74 — 25-Nov pre-market review and holiday-maturity tracker defect (25-Nov-2026)
- Preflight re-read current Master Ledger through C73, 24-Nov Daily Unified Top-5 report, 24-Nov Failure & Lessons Register, C72/C73 reports, Run #410 prospective artifact and Run #421 collector evidence. Previously accepted ZIP/hash checks were reused; no broad workflow or new NSE acquisition.
- Run #410 / ID 45490518576 / artifact #14966627305: conclusion SUCCESS; 9m52s run window; ZIP SHA-256 `6b1673af895214ae982fb445a62d5536dd2960eb062dc310b85f955b01c8af16`, independently downloaded and matched GitHub artifact digest. It is audit-only, not a production selector run.
- Run #410 artifact latest_picks.csv SHA-256 `aa0a685260f56cbf8355019ae5b6d5b6abf3ea7bb6e98f1417b2f999d63c28e6`; watchlist_ledger.csv SHA-256 `4c7d629634d945f65beebf73a5cd7f89d96cd5650f3a8d07a54f29a113ebdc13`.
- Run #410 log records LIVE_CUTOFF=2026-11-24, PICKS=10, LABELS=NOT_READ FROM_FUTURE. NSE official 2026 holiday circular confirms 24-Nov is a trading holiday. The 24-Nov cutoff's 10 rows / 9 unique symbols are invalid for current selection and excluded.
- 23-Nov cutoff's 10 tracker rows / 7 unique symbols have MATURED_T1=True and T1_HIGH_PCT populated but OUTCOME_LAST_DATE blank. The next valid session after 23-Nov is 25-Nov; H+1 is not mature at 08:45 IST. Code-level audit of audit/prospective-selector-tracking branch prospective_watchlist_tracker.py (blob SHA-1 f28f7c752c4eaadeb5583f4434190a124a4910d9) confirms outcome() takes the next h sorted date rows without official exchange-calendar/holiday validation; H+1 end date is not persisted. Holiday/session root cause confirmed; exact per-row contribution of duplicate-content data remains UNKNOWN.
- New lesson PW-LSN-20261125-001 created; full evidence, root cause, test plan and carry-forward action in docs/FAILURE_LESSONS_LEARNED_20261125.md. Do not label the 23-Nov cohort success/failure until 25-Nov close; H+3=27-Nov and H+5=01-Dec.
- Run #421 / ID 45422367928 / artifact #14936656169 remains the latest collector run; ZIP SHA-256 d57374c50a8b8e2fe5710fd57660225ea59a2beffd639cb9e83b77e734499954 was already independently verified in C72. Runtime 12m06s exceeded 10-minute target; not rerun.
- 200 labels / 187 unique content sessions / 13 holiday duplicate pairs remain NOT_ACCEPTED. Final selection remains PROVISIONAL_ONLY_FINAL_SELECTION_BLOCKED; live 1m source last recorded HTTP 403 with zero rows/symbols. No 25-Nov final selector run found.
- Engine A diagnostics remain exploratory only; +2% UNKNOWN, +5/+10/+15/+20 values as in dated report are NOT_ACCEPTED due session/forward-label defects. B UNKNOWN; C BLOCKED. No qualified candidate released. No target Best-3 accepted.
- Daily report: docs/DAILY_UNIFIED_TOP5_SWING_WATCHLIST_20261125.md; commit 0d45319f2ce33523b3f193f0d2cf21b7838055aa; blob SHA-1 2376b36ec30265805facd1d3a94f23833e06a16c; SHA-256 979572bc047123ce3a2f6e12258cb6727e03cceaef3250e2889a7358627ed1ba; exact GitHub read-back matched.
- Failure & Lessons Register: docs/FAILURE_LESSONS_LEARNED_20261125.md; commit 55d74c00a984be97727c5e24a559fd7424148547; blob SHA-1 d3ce91b8e6d33ebe415e83fbfb9401295417d126; SHA-256 de80ecb666aa02a4cc1c54f5a6b675d091d943849da77473536b5f45460e759a; exact GitHub read-back matched.
- Final report decision: qualified candidates 0; no price bands or stops fabricated. No workflow dispatch, NSE acquisition, paid source, production/selector/ranking/threshold/CORE-672/Engines A–E/IPO-PLX V2.0 change. ₹0; UNKNOWN never PASS.


## 19. Continuation 75 — Holiday tracker root-cause and Library delta audit (25-Nov-2026)
- Mandatory preflight: re-read current ledger through C74, C72/C73 reports, C74 daily report, 25-Nov Failure & Lessons Register, and Library Mother File (continuations 1–53). Reused accepted artifact hashes; skipped completed PASS checks.
- Static audit-only branch inspection of `prospective_watchlist_tracker.py` (branch `audit/prospective-selector-tracking`, blob SHA-1 `f28f7c752c4eaadeb5583f4434190a124a4910d9`) reconfirmed PW-LSN-20261125-001: next h raw symbol-date rows are treated as sessions without official NSE calendar validation; duplicate dates are silently dropped; maturity depends on row count and HIGH_PRICE; OUTCOME_LAST_DATE is only written in H+5 branch, not H+1/H+3.
- C75 correction contract now specifies required official NSE session spine, exact next 1/3/5 valid sessions, fail-closed missing/duplicate/non-session rows, per-horizon end dates, and holiday/missing/duplicate regression fixtures. This is design/static audit only; implementation and tests remain OPEN.
- Library recursive snapshot: 1,445 items across 15 pages, no warnings; 399 .dat files / 278,932,615 bytes. Genuine inventory manifest still declares 821 entries (807 .dat, 12 .json, 1 .txt, 1 .html). Dedicated ChatGPT_Data_Export_2026-11-25 folder contains 7 core metadata files; two dated incoming folders contain 13 and 7 items; six additional dated .dat files appear under Research Uploads.
- The raw 807-vs-399 .dat count delta is not a verified missing count. Exact manifest→Library filename/path/size join and SHA-256 remain NOT_DONE; package provenance UNKNOWN. No bulk scan or invented mapping.
- 23-Nov cohort H+1 remains PENDING until 25-Nov close; H+3 expected 27-Nov; H+5 expected 01-Dec. No premature outcome acceptance.
- Report: `docs/PRECISION_WIRES_CONTINUATION75_HOLIDAY_TRACKER_ROOT_CAUSE_AND_LIBRARY_DELTA_AUDIT_20261125.md`; report commit 81cc382e7c45edfe890dfd4c65191c62e31c73b5.
- Acceptance: C75 preflight/static audit PASS; calendar-aware implementation/tests OPEN; export payload reconciliation NOT_DONE. No workflow dispatch, NSE acquisition, paid source, external contact, production/selector/ranking/threshold/merge/delete changes. ₹0; UNKNOWN never PASS.

## GCR Continuation 229 — CDSL daily archive raw freshness and arithmetic QA (25-Nov-2026)
- Mandatory GCR preflight: re-read current Master Continuity Ledger, GCR Priority Queue, 63-country Historical Task Registry, C39/C68 CDSL freshness, C74 sector arithmetic, C76 NSDL form contract, and C77 CDSL daily arithmetic. Previously accepted PASS work skipped.
- Reused artifact 14527092174 / run 44519322726. ZIP SHA-256 83048ea0bc712b6a453270f8fb5c3c6755b579857ff2ad9eb7d53c8ba1778fbd reverified. CDSL archive raw HTML 73,784 bytes, SHA-256 aa2a03c6621772e52b0b9ac52f11b525d82f1ce80539554302eda861145304df, captured 2026-11-19T11:57:09.076562Z, HTTP 200, page displays investment/derivatives cutoff 02-Mar-2026.
- Arithmetic: daily/March/YTD 75/75 purchases-sales-net identities; cumulative 8/8; INR category subtotal sums 3/3 exact. USD daily and March subtotal sums show -0.01 USDm displayed residual; retained REVIEW. No total adjustment.
- Material freshness finding: C229's 02-Mar snapshot conflicts with C39's 30-Sep and C68's 31-Oct rendered snapshots for same archive URL; preserve as distinct responses; archive freshness/completeness remains NOT PASS/UNKNOWN.
- CDSL daily 18-Nov and sector 15-Nov prior PASS evidence not repeated; NSDL archive form contract C76 reused. NSDL postback output and matched-date NSDL/CDSL reconciliation remain NOT_DONE.
- Report: docs/GCR_CDSL_DAILY_ARCHIVE_RAW_FRESHNESS_AND_ARITHMETIC_QA_CONTINUATION229_20261125.md; report commit undefined; queue commit 7d361eb3caaa242aea590573c8054cac4918e9e1; registry commit 6759145fb9c660803ca4c00fab596b8f13403770.
- Next exact action: fresh-state NSDL Archive interactive date selection + View Report using supported browser; if unavailable, keep NOT_DONE and do not guess POST or replay stale ViewState. No source/prod changes; ₹0; UNKNOWN never PASS.

## GCR Continuation 230 — NSDL archival permission gate reconciliation (25-Nov-2026)
- Reconciled the C76/C229 suggested NSDL public-form postback with the controlling GCR ledger rule: NSDL FPI/DII archival is BLOCKED pending written permission. No permission evidence found; no postback executed or authorized. No stale ViewState replay, guessed POST, scraping or reverse engineering.
- NSDL archive rows remain NOT_CAPTURED; matched-date NSDL/CDSL reconciliation NOT_DONE. CDSL C229 arithmetic PASS retained; archive freshness/completeness remains NOT_PASS / UNKNOWN.
- CHN/COL/POL routes remain blocked as documented; next cohort work must require a genuinely new official route and full route-history preflight. TUR's existing ZIP timeout is closed absent distinct official route/revision. No IMF re-query/cohort rebuild, paid source, external contact, workflow dispatch or production changes. ₹0; UNKNOWN never PASS.
- Report: docs/GCR_NSDL_ARCHIVAL_PERMISSION_GATE_RECONCILIATION_CONTINUATION230_20261125.md.


## GCR Continuation 231 — RWA BNR WebDash alternate-route boundary (25-Nov-2026)
- Mandatory preflight completed: re-read current ledger, GCR queue, 63-country registry, RWA C97/C130, NPL C58/C94/C130, SLV C100/C131, and Library Mother File 1–53 + GCR Gap Matrix. Completed PASS work skipped.
- NPL current-route closure check: NRB External Sector BPM6 XLSX locator unchanged; NSDP BOP SDMX link still points to stale NEPAL_BOP_2024_Q1.xml. No new official Q2 API/export route; NPL remains PARTIAL/BLOCKED; no repeated XLSX fetch.
- RWA new official route: https://webdash.bnr.rw/ indexed Balance of Payment table shows annual USDm 2019–2023 with combined portfolio investment only; no Q2-2026 separate asset/liability legs or API/export contract. BNR June-30 portal item remains JS shell / exact URL unresolved. October MPFSS 2026H1 portfolio net +USD14m is net-only and not Q2; annual FY rows remain non-quarterly. RWA remains PARTIAL / NOT PASS; Q2 legs NOT_CAPTURED; vintage UNKNOWN; aggregate NOT_AUTHORIZED.
- RWA matrix note/evidence_ref updated without gate promotion. Report: docs/GCR_RWANDA_RWA_Q2_2026_BNR_WEB_DASH_ALTERNATE_ROUTE_BOUNDARY_CONTINUATION231_20261125.md; report commit 719b1482b5b1216d0a3a6cb5ea73c6a002f81025. Queue/registry/matrix updated.
- Next: SLB official transaction-FX conversion-method boundary from C132 after exact route-history preflight. No generic quarterly FX, inferred sign/scale, IMF re-query, cohort rebuild, paid data, external contact or production changes. ₹0; Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2.0 unchanged; UNKNOWN never PASS.


## GCR Continuation 232 — SLB CBSI official Q2 dataset locator / transaction-FX method boundary (25-Nov-2026)
- Mandatory preflight: current Master Ledger, GCR queue, 63-country registry/matrix, SLB C99/C132, C128 handoff, C231 and Library Mother File 1–53 + GCR Gap Matrix reread. Existing PASS work skipped.
- New official CBSI BOP page confirms BPM6, quarterly/annual series, SB$ million presentation and latest 2026-Q2. Exact official workbook URL discovered: https://www.cbsi.com.sb/sites/default/files/2026-09/Balance-of-Payment-Statistics-2006-2026-Q2.xlsx; web retrieval HTTP 400 unsupported XLSX MIME and direct byte download failed. No raw bytes/hash claimed.
- CBSI June-2026 Quarterly Review reports quarterly-average SBD/USD 8.08 and Q2 Table 1.17 portfolio assets +38 SBDm / liabilities nil. Neither report nor CBSI daily-rate publication page states that the quarterly average or daily published rate is the BOP transaction conversion rate. SLB transaction FX method and SCALE bridge remain NOT_ESTABLISHED; numeric comparison REVIEW, vintage PENDING, national validation PARTIAL / NOT PASS, aggregate NOT_AUTHORIZED.
- SLB matrix evidence_ref/note updated only. Report: docs/GCR_SOLOMON_ISLANDS_SLB_Q2_2026_CBSI_OFFICIAL_DATASET_AND_TRANSACTION_FX_METHOD_BOUNDARY_CONTINUATION232_20261125.md; commit a5c7ecc52b89d8fff0d81bec0b00b785f123abf2. Queue/registry/matrix updated.
- Next: SRB same-vintage/revision bridge after exact preflight C101/C103/C104/C109/C112. No repeated monthly arithmetic/sign/FX work. ₹0; no IMF re-query/cohort rebuild, paid source, external contact or production change. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2.0 unchanged; UNKNOWN never PASS.


## GCR Continuation 233 — Serbia SRB same-vintage / revision bridge route boundary (25-Nov-2026)
- Mandatory preflight re-read current ledger, GCR queue, 63-country registry, and SRB C104/C109/C110/C111 history; C101/C103/C104/C109 references reconciled. C112 was not located as a distinct SRB report in current repo docs or Library search; no claim it was independently read.
- September-vintage May legs and arithmetic retained PASS: assets -EUR25m, liabilities +EUR3,932m, net -EUR3,957m. NBS sign/transaction-date FX and IMF A/L portfolio semantics/exact rows retained PASS/CAPTURED. No repeated arithmetic, IMF query or cohort rebuild.
- New official NBS archive check: English Statistical Bulletin page exposes only generic Select/Input/Show archive controls; “Data series in XLS format” leads to general Statistics landing page, not July issue workbook. Official chronology confirms July issue only. No July Table 2.3 header or month attribution recovered.
- Known July PDF direct route not retried (C109–C111 exhausted). No supported browser DOM/download capability; no guessed POST/ViewState, scraping, authenticated request, external contact or paid route. July raw bytes/hash remain NOT_CAPTURED; July May legs NOT_VERIFIED; July-to-September revision NOT_DONE; SRB PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Detail: ${reportPath}; report commit ${created.result.commit_sha}. Next: resume only with supported interactive browser or genuinely new official NBS byte route; preserve all gates. ₹0; no production changes; UNKNOWN never PASS.


## GCR Continuation 234 — Mongolia MNG official Open Data API documentation and table-route boundary (25-Nov-2026)
- Mandatory preflight re-read current ledger, GCR queue, 63-country registry, MNG C179/C190/C221/C222 and C233 SRB handoff. Existing MNG table/source gates and previous endpoint failures were reused; no repeated IMF retrieval/cohort rebuild.
- New official NSO Open Data page (https://www.1212.mn/en/data-base/open-data) documents a GET API route example, metadata response fields title/variables/code/text/values/valueTexts and JSON/XML formats. NSO terms confirm 1 request/second/IP, max 100,000 responses/request and CC BY 4.0. This advances API contract evidence beyond C221.
- Reopened official MNG BOP PxWeb page: 69 Indicator values, 71 Quarter values incl. 2026-2, quarterly, million USD, source Bank of Mongolia, general BOP description includes portfolio investment. Page updated date 11/9/2026 is not an observation vintage.
- MNG table-specific API metadata response was not captured; candidate route inaccessible through current retrieval surface with no HTTP status/body/headers/bytes/hash. No API query submitted; no indicator codes inferred. MNG A/L NOT_CAPTURED, national validation BLOCKED/PARTIAL/NOT PASS, aggregate NOT_AUTHORIZED.
- Detail: docs/GCR_MONGOLIA_MNG_Q2_2026_OFFICIAL_OPEN_DATA_API_DOCUMENTATION_AND_TABLE_ROUTE_BOUNDARY_CONTINUATION234_20261125.md; report commit fc9d3bfb4503c75e30341f90277823977a417d52. Next: supported GET-capable client fetches table metadata; parse real indicator labels/codes, then Q2 cells under <=1 request/sec/IP. ₹0; no production changes; UNKNOWN never PASS.

## GCR Continuation 235 — MNG documented GET metadata endpoint suffix test (25-Nov-2026)
- Re-read current ledger/queue/registry, MNG C179/C190/C221/C222/C234, current matrix, C233 handoff, Library Mother File 1–53 + Continuation 57 and Library Data Export Recovery Phase 1/2. C234 official API docs reused; no accepted PASS work repeated.
- Official NSO Open Data page documents GET, metadata schema and table identifier .px suffix. One new .px-suffix GET variant attempted for exact MNG table: https://data.1212.mn/api/v1/en/NSO/NSO__Economy,%20environment__Balance%20of%20Payments/DT_NSO_0100_001V10_quarter.px. Current retrieval surface returned “URL not accessible”; no HTTP status, headers, body, bytes or hash. This is not evidence of server-side 4xx/5xx.
- Exact .px variant closed for repeat through same reader. No indicator codes guessed, no API query submitted, no Q2 national A/L values. MNG remains BLOCKED / PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Detail: docs/GCR_MONGOLIA_MNG_Q2_2026_DOCUMENTED_GET_METADATA_ENDPOINT_SUFFIX_TEST_CONTINUATION235_20261125.md; report commit 08c32ffc9d205e7141118a98c71c9637bcee1ee0. Next: use genuinely different supported GET-capable client/browser or official Q2 downloadable export; otherwise move to next eligible cohort member after exact route-history preflight. ₹0; no IMF re-query/cohort rebuild; no production changes; UNKNOWN never PASS.



## GCR Continuation 236 — Angola BNA dissemination-calendar / public-access boundary reconciliation (25-Nov-2026)
- Mandatory preflight re-read current ledger, GCR queue, 63-country registry/matrix, C142 and Library Mother File/GCR context. Existing PASS work and the known BNA JavaScript SPA route were not repeated.
- New official INE-hosted PASEN 2026 PDF confirms BNA Q2 BOP/IIP production under MBP6; quarterly reference period; public availability in quarter n+1. BNA dissemination calendar describes BOP/IIP as previous-quarter, bimonthly, website publication after 60 days.
- Current IMF e-GDDS metadata says quarterly external-sector data are posted on BNA website simultaneously to all users; separate hard-copy quarterly bulletin and annual BOP/IIP mailing-list wording is not evidence that quarterly online BOP is mailing-list-only. This refines C142 access-boundary interpretation, but supplies no exact detailed portfolio dataset locator/API/schema.
- Q2 release announcement dated 4-Sep-2026 is consistent with the 60-day schedule after 30-Jun; public text exposes account-level current-account and capital/financial-account totals only. No separate portfolio A/L values, raw bytes/hash, or national methodology bridge captured. No net-to-leg back-solving.
- AGO remains SOURCE_FOUND / PARTIAL / NOT PASS; national A/L NOT_CAPTURED; vintage UNKNOWN; FULL_PASS NO; aggregate NOT_AUTHORIZED. Matrix gates unchanged; evidence_ref/note updated to C236.
- Report: docs/GCR_ANGOLA_AGO_Q2_2026_BNA_DISSEMINATION_CALENDAR_AND_PUBLIC_ACCESS_BOUNDARY_RECONCILIATION_CONTINUATION236_20261125.md; report commit 7aec846aef1f3a1079ad503215fba3579f72eeae.
- Next: use only a supported official BNA public download/browser surface if it exposes detailed Q2 BOP portfolio A/L rows; capture raw response, metadata, terms and SHA-256. Do not repeat the BNA SPA or guess an API. If unavailable, move to next fixed-cohort country after exact route-history preflight. ₹0; no IMF re-query/cohort rebuild; no production changes; UNKNOWN never PASS.


## GCR Continuation 237 — Albania ALB official Q2 dual-leg capture (25-Nov-2026)
- Mandatory preflight re-read current ledger/queue/registry/matrix, Library Mother File/GCR context, and ALB C139–C141/C192. PASS methodology/taxonomy and archived IMF rows reused; legacy Main-data routes closed and not repeated.
- New distinct official Bank of Albania Monthly Statistical Report 08/2026 PDF: https://www.bankofalbania.org/rc/doc/RSM_gusht_2026_anglisht_35170.pdf. Table 2-1 (quarterly BOP, EURm) explicitly separates portfolio assets/liabilities. Q2 2026 row: assets +156.25 EURm; liabilities +124.70 EURm; portfolio net +31.55 EURm; 156.25−124.70=31.55 exact.
- Official PDF opened via document reader; direct raw-byte download failed in current container. No raw PDF bytes/headers/receipt/SHA-256 claimed. This is a new Q2-specific official publication artifact, not the closed legacy table route.
- Reused C139 IMF raw Q2 rows: assets 181700604.8387097 USD (SCALE=6); liabilities 145011618.7096774 USD (SCALE=6). No IMF re-query. No EUR/USD conversion applied. Diagnostic implied ratios are not accepted FX rates and are not used as reconciliation evidence.
- ALB advances to DATA_CAPTURED; source and national EURm/sign/net identity are documented. Asset/liability numeric comparison gates remain REVIEW / NOT_PASS pending independently authorized conversion method; same-vintage/revision UNKNOWN; FULL_PASS NO; aggregate NOT_AUTHORIZED.
- Report: docs/GCR_ALBANIA_ALB_Q2_2026_BOA_MONTHLY_STATISTICAL_REPORT_OFFICIAL_DUAL_LEG_CAPTURE_CONTINUATION237_20261125.md; report commit 214a86283beb2ecc1cca5dfabf7d39201ac748cd.
- Next: establish BoA's applicable Q2 transaction FX bridge and revision cutoff using an independently published official method; no inferred cross-rate, no repeat of legacy routes/PDF text scrape, no IMF re-query/cohort rebuild. ₹0; production unchanged; UNKNOWN never PASS.
## GCR Continuation 238 — Albania official flow FX convention and revision boundary (25-Nov-2026)
- Mandatory preflight re-read current ledger, GCR queue, 63-country registry/matrix, Library Mother File 1–53/addenda through C57 and C237 report. C237 capture and prior accepted BPM6 sign work reused; no legacy Main-data route, repeated PDF text extraction or IMF re-query.
- New official BoA June-2014 BPM6 commentary confirms BOP presentation in EUR and says users may convert flow values using published average exchange rates; stocks use end-period rates. BoA monthly-average table defines monthly averages as simple averages of daily official rates to ALL. IMF BPM6 §§3.105–3.106 support transaction-rate/shortest-period average principles and require converting underlying flows before deriving net.
- This establishes the broad flow-vs-stock convention, but not the exact Q2-2026 portfolio-specific quarterly USD aggregation or observation-level FX inputs. No FX conversion applied; inferred ALL cross-rate/unweighted quarter average rejected.
- BoA methodology metadata DOCX was linked but current reader returned unsupported DOCX MIME; no content assumed. No Q2-2026 observation-specific revision timestamp/cutoff matched to archived IMF rows. ALB asset/liability remain REVIEW, vintage UNKNOWN, FULL_PASS NO, aggregate NOT_AUTHORIZED.
- Report: docs/GCR_ALBANIA_ALB_Q2_2026_BOA_OFFICIAL_FLOW_FX_RULE_AND_REVISION_BOUNDARY_CONTINUATION238_20261125.md; report commit 01d226cb0c6d751643e988ff6f5377600e87adc7.
- Next: reopen only on distinct BoA Q2-2026 dated revision record, detailed compilation/FX note, or official transaction-level flow-rate data. Otherwise move to next eligible fixed-cohort item after exact route-history preflight. ₹0; no production change; UNKNOWN never PASS.


## GCR Continuation 239 — Bangladesh BGD Q2-2026 official net-only source boundary (25-Nov-2026)
- Mandatory preflight re-read current Master Continuity Ledger, GCR Priority Queue, 63-country Historical Task Registry/matrix and Library Mother File/GCR context. Fixed cohort and archived IMF panel reused; no IMF re-query or cohort rebuild.
- New official Bangladesh Bank Quarterly, Volume XXIII No.4, “April-June, 2026”: https://www.bb.org.bd/pub/quaterly/bbquarterly/bangladesh%20bank%20quarterly%2C%20%20vol%20xxiii%2C%20no%204.pdf. Cover confirms calendar Q2 2026. Annexure 1 Table V.1 (USD million) reports Bangladesh FY26 Q4 = Apr-Jun 2026; portfolio investment appears as a net-only line, not separate asset/liability transaction legs.
- Table V.1 shows separate assets/liabilities in some other-investment and reserve-asset rows, but those are different instruments and cannot be substituted for portfolio legs. FY26 is provisional; no observation-specific revision timestamp or IMF-matched vintage ID found.
- No net-to-leg back-solving, IIP substitution, IMF re-query, or cohort rebuild. BGD remains SOURCE_FOUND / PARTIAL / NOT PASS; national A/L NOT_CAPTURED; vintage UNKNOWN; aggregate NOT_AUTHORIZED.
- Report: docs/GCR_BANGLADESH_BGD_Q2_2026_BB_Q4FY26_NET_ONLY_SOURCE_BOUNDARY_CONTINUATION239_20261125.md; report commit 68b6eb13da5ca33ba26f4f8d0ec5734f041642f3.
- Next: reopen only on distinct official Bangladesh Bank Q2 dual-leg table/export with revision metadata; otherwise advance to next eligible fixed-cohort member after route-history preflight. ₹0; no production changes; UNKNOWN never PASS.


## GCR Continuation 240 — Tajikistan TJK official BOP workbook locator / byte-access boundary (25-Nov-2026)
- Mandatory preflight re-read current Master Ledger, Priority Queue, 63-country Historical Task Registry/matrix and Library Mother File/GCR context. TJK is in the fixed cohort; no prior TJK-specific continuation was found in the registry. Existing IMF panel reused; no IMF re-query/cohort rebuild.
- New official NBT Balance of Payments page (https://www.nbt.tj/en/payments_balance/) states BOP compilation is an NBT function and cites IMF BPM5/BPM6 methods. Its 2026 Standard Representation link resolves to https://www.nbt.tj/upload/iblock/d9d/6x5djzg70lrzfq0t9f3pibhv3vmkb71x/st_pr_2026_2.xlsx; Analytical Representation separately resolves to https://www.nbt.tj/upload/iblock/1fd/gt06fcxjn5ilv466tnxmf28usqj9vnc5/an_pr_2026_2.xlsx.
- Both official XLSX links returned HTTP 400 / unsupported XLSX MIME in the document reader; direct byte download of the standard workbook also failed. No workbook bytes, headers, byte count, sheet/schema, Q2 row values, portfolio A/L legs, revision metadata or SHA-256 captured. IIP stocks, annual forecasts and unrelated banking assets/liabilities are not substitutes.
- TJK remains SOURCE_FOUND / PARTIAL / NOT PASS; both national legs NOT_CAPTURED; vintage UNKNOWN; aggregate NOT_AUTHORIZED. Matrix gates unchanged; evidence_ref/note points to C240.
- Report: docs/GCR_TAJIKISTAN_TJK_Q2_2026_NBT_OFFICIAL_STANDARD_BOP_XLSX_LOCATOR_AND_BYTE_ACCESS_BOUNDARY_CONTINUATION240_20261125.md; report commit 35f0059e6d7a884db9f606d288c4d5919d0d1e85.
- Next: use only a genuinely different supported XLSX byte-transfer/browser route or distinct official NBT export; do not repeat the same document-reader or direct-download attempts. ₹0; no production changes; UNKNOWN never PASS.


## GCR Continuation 241 — Montenegro MNE CBCG table-annotation access boundary (25-Nov-2026)
- Mandatory preflight re-read current Ledger/Queue/Registry/matrix, Library Mother File/GCR context, and controlling MNE C182 report. C240 TJK was recognized as already committed; C237–C240 accepted/bounded work skipped. No IMF re-query/cohort rebuild.
- Re-opened official CBCG Bulletin 9/2026 PDF via document reader. It exposes the BoP section and “Tables 5.1–5.4 - download tables” label, but the extraction surface does not expose an annotation target or direct payload URL. Separate byte-preserving download of the same PDF failed; no PDF bytes/headers/hash claimed.
- Official methodology text confirms BPM6, quarterly EUR reporting, transaction-day/monthly and annual average FX conventions, period-end rate for monitored valuation differences, and provisional/revisable data. No FX conversion performed. Q2 IIP calendar date is a stock release, not a substitute for BOP flows.
- No table workbook/CSV, Q2 portfolio asset/liability legs, or revision-vintage bridge captured. MNE remains PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED. Exact PDF text-reader route is closed for identical repeat; reopen only on supported PDF-annotation extraction or distinct official CBCG export URL/API.
- Report: docs/GCR_MONTENEGRO_MNE_Q2_2026_CBCG_BULLETIN_9_2026_TABLE_ANNOTATION_ACCESS_BOUNDARY_CONTINUATION241_20261125.md; report commit c7eb31705caef3183f90a848a08551210026402a. ₹0; no production changes; UNKNOWN never PASS.


## GCR Continuation 242 — Paraguay PRY BCP Statistical Annex alternate export boundary (25-Nov-2026)
- Mandatory preflight re-fetched current Ledger/Queue/Registry/matrix and searched Library Mother File/GCR context. Re-read PRY C60. C237–C241 and PASS work skipped; no IMF re-query/cohort rebuild.
- New distinct official BCP Statistical Annex page says the periodically updated file includes BOP statistics. Current download locator resolved to `https://www.bcp.gov.py/documents/20117/213069/Anexo_Estad%C3%ADstico_del_Informe_Econ%C3%B3mico_23_11_2026.xlsx/1fc7fda2-74cf-e07c-be5b-535f02a89ba3?t=1795456089070`. This differs from the C60 Q2-specific BOP/IIP workbook URL.
- Annex XLSX reader click returned HTTP 400 unsupported XLSX MIME; a separate direct byte-download attempt failed. No bytes/headers/size/sheets/schema/Q2 coverage/A-L values/revision metadata/hash captured. BCP BOP page confirms quarterly and annual dissemination with three-month lag; current calendar lists next quarterly release 30-Dec-2026, not proof of annex Q2 legs.
- PRY remains SOURCE_FOUND / PARTIAL / NOT PASS; both national legs NOT_CAPTURED; vintage UNKNOWN; aggregate NOT_AUTHORIZED. Close this annex URL's identical reader/download attempts. Reopen only with a distinct supported XLSX/API/export route.
- Report: docs/GCR_PARAGUAY_PRY_Q2_2026_BCP_STATISTICAL_ANNEX_ALTERNATE_EXPORT_ACCESS_BOUNDARY_CONTINUATION242_20261125.md; report commit ec6e16fb0507a278cf1cc23e6c98548596cc81a5. ₹0; no production changes; UNKNOWN never PASS.


## Chapter 57 — Ten-conversation closeout summary and page-rollover rule (25-Nov-2026)

### Conversation range and scope
- Chapter: `গবেষণা যাচাই অব্যাহত 57`
- Counted research continuations: C233–C242 (10 conversations).
- Purpose: fixed-cohort Q2-2026 GCR national portfolio asset/liability source validation, with source-access, period, dual-leg, vintage and duplicate-prevention gates. This chapter summary is a navigation/continuity checkpoint, not a claim that all country validations passed.

### Ten-conversation summary
1. **C233 — Serbia (SRB):** attempted July-vintage source retrieval; archive XLS redirected to the general Statistics page. July Table 2.3 header and separate May asset/liability values were not captured; revision bridge and dual-leg comparison remain incomplete. SRB remains PARTIAL / NOT PASS.
2. **C234 — Mongolia (MNG):** official NSO documentation/metadata structure reviewed; 69 indicators, 71 quarters and Q2 code `2026-2` identified. Actual metadata response/indicator values and portfolio legs remained blocked. Documentation-level work only; MNG not passed.
3. **C235 — Mongolia (MNG):** documented `.px` GET metadata endpoint was tested but inaccessible in the current retrieval surface; no response or data captured. Do not repeat the same route. MNG remains BLOCKED/PARTIAL.
4. **C236 — Angola (AGO):** reconciled official INE PASEN 2026 schedule, BNA dissemination calendar and IMF e-GDDS public-access metadata. Quarterly BPM6 BOP/IIP is public in quarter n+1; BNA calendar says website publication after 60 days. This corrects the prior overly broad mailing-list-only interpretation, but public Q2 text exposes only account-level totals, not portfolio A/L. AGO remains SOURCE_FOUND / PARTIAL / NOT PASS.
5. **C237 — Albania (ALB):** official BoA Q2-2026 report/table dual-leg capture; published assets EUR 156.25m, liabilities EUR 124.70m, net EUR 31.55m, arithmetic identity holds. Raw PDF bytes/headers/hash and independently verified FX/vintage bridge were not obtained; numeric arithmetic does not establish IMF-matched validation. ALB remains PARTIAL / NOT PASS.
6. **C238 — Albania (ALB):** clarified BoA flow FX convention (average FX for BOP flows; end-period FX for IIP stocks) and monthly average-rate construction. Exact Q2 portfolio USD aggregation and same-vintage revision cutoff remain unestablished; no conversion applied. ALB remains REVIEW / REVIEW / UNKNOWN / NOT_AUTHORIZED.
7. **C239 — Bangladesh (BGD):** Bangladesh Bank Quarterly Vol XXIII No.4, Table V.1 inspected. Calendar Q2-2026 maps to FY26 Q4; portfolio investment is net-only, with no separate portfolio asset/liability legs. Other investment and reserves were correctly excluded as substitutes. BGD remains SOURCE_FOUND / PARTIAL / NOT PASS.
8. **C240 — Tajikistan (TJK):** official NBT BOP page and 2026 Standard/Analytical XLSX locators confirmed. XLSX reader returned unsupported MIME/400 and direct byte retrieval failed; no workbook bytes/schema/Q2 legs/vintage/hash. TJK remains SOURCE_FOUND / PARTIAL / NOT PASS.
9. **C241 — Montenegro (MNE):** official CBCG Bulletin 9/2026 confirms BPM6, quarterly EUR and FX methodology; tables 5.1–5.4 download label found, but annotation target/direct export URL was not exposed and PDF byte download failed. No Q2 portfolio A/L captured. MNE remains PARTIAL / NOT PASS.
10. **C242 — Paraguay (PRY):** distinct official BCP Statistical Annex page and current XLSX locator identified; the annex is described as including BOP statistics. XLSX reader rejected MIME/400 and byte download failed; Q2 scope, portfolio A/L, raw hash and vintage remain unverified. PRY remains PARTIAL / NOT PASS.

### Chapter-level result
- Ten country/source-boundary continuations were reviewed and documented; no country was promoted to FULL_PASS from these ten tasks.
- New official source/dissemination evidence was added for Angola and Paraguay; Albania dual-leg arithmetic and FX methodology were clarified; Bangladesh net-only limitation was confirmed; Mongolia, Tajikistan and Montenegro retrieval boundaries were recorded; Serbia's July-vintage route remained unresolved.
- All countries remain subject to their individual matrix statuses. The 63-country aggregate remains `NOT_AUTHORIZED`; no national validation should be represented as fully complete on the basis of source discovery or partial numeric checks alone.
- No IMF re-query, fixed-cohort rebuild, net-to-leg back-solving, IIP-stock substitution, synthetic values, unsupported FX/sign/scale conversion or production changes.
- Spend ₹0; free official sources only. CORE-672 (56×12), V11.3 Engines A–E, Production Selector, RANKING_SCORE, +1 PRESSURE_FADE and IPO-PLX V2.0 remain unchanged.

### Fixed chapter/page rollover rule (user instruction, 25-Nov-2026)
- Count **conversations** within each numbered research chapter/page, not tool calls, messages, commits or continuation IDs.
- After every 10 conversations, provide a concise chapter closeout summary: work/checks completed, country/task outcomes, GitHub records updated, unresolved blockers, and next actions.
- Explicitly tell the user that the 10-conversation block is complete and they should open the next numbered research page/chapter before continuing.
- Reset the counter for the new page. If the user opens a new page early, continue from the current GitHub Ledger/Library continuity state; do not fabricate a 10-conversation completion.
- Do not claim the summary has been fixed in product automation; this is the standing conversation/workflow instruction and is recorded here for continuity.


## GCR Continuation 243 — Samoa WSM official CBS index release-status recheck (25-Nov-2026)
- Mandatory preflight re-read current Ledger, GCR Master Priority Queue, 63-country Historical Task Registry/matrix, and Library Mother File / WSM C125–C126 context. Pre-update blob SHAs: Ledger dd272c937f21b09f540e00bda834ee9236bf9f8d; Queue 0abd8c411ec731e8d5a99cd4e28d8949184a1850; Registry 202fbc104019ee59b04406efc5209956731830c; Matrix 49123248b14ecdfc7746f6ec0d288f10d3242f47. Existing accepted work reused; no IMF re-query/cohort rebuild.
- New direct official CBS Quarterly Bulletin index inspection: https://cbs.gov.ws/quarterly-bulletin. Although the search-index snippet named “Quarterly Bulletin September 2026”, the opened official page's Latest list still starts with June 2026 and footer says last updated 18-Aug-2026. The conflicting snippet is UNCONFIRMED and is not accepted as release proof.
- CBS page states bulletins are published with a three-month delay. C125/C126 remain controlling for the June 2026 issue: it covers Q1/March 2026 and Table B-1 ends at 2026-I. No September 2026 PDF, Q2-2026 Table B-1, portfolio A/L values, raw bytes or SHA-256 captured.
- WSM remains SOURCE_FOUND / PARTIAL / NOT PASS; both Q2 national legs NOT_CAPTURED; vintage UNKNOWN; FULL_PASS NO; aggregate NOT_AUTHORIZED. Matrix evidence_ref/note updated to C243 only; no gate promotion.
- Report: docs/GCR_SAMOA_WSM_Q2_2026_CBS_OFFICIAL_INDEX_RELEASE_STATUS_RECHECK_CONTINUATION243_20261125.md; commit 3fe2ccb003850611f6a9e7b4def92e04d13c79e9. Web direct-page evidence: turn896134view0 lines 292–308.
- Next: reopen only when a later issue is listed directly on the official CBS index or a distinct official Q2-2026 BOP table is published; verify the internal reporting period before capture. Do not repeat June PDF extraction or accept stale search snippets. ₹0; no IMF re-query/cohort rebuild; no production changes; UNKNOWN never PASS.


## GCR Continuation 244 — Mexico MEX Banxico Q3 scheduled release / Q2 vintage precheck (25-Nov-2026)
- Mandatory preflight re-read current Ledger, Priority Queue, Historical Registry, 63-country matrix, Library Mother File GCR context, and controlling MEX C137/C208. Reused existing national Q2 separate-leg values, archived IMF exact rows and arithmetic PASS; skipped completed PDF/SIE extraction, duplicate IMF requests and cohort rebuild.
- Official Banxico BOP page states quarterly releases are scheduled for the 25th of May/August/November at 09:00 and lists Q2 (25-Aug-2026) as latest. Official November calendar indexed Q3 BOP for 25-Nov-2026. At check time 19:10 IST / 07:40 Mexico City, the 09:00 local scheduled release was 80 minutes in the future. Dynamic calendar form returned no publication rows; no Q3 release/Q2 revision bytes or observations captured.
- MEX existing numeric checks remain PASS at ±USD0.5m; same-vintage PENDING / NOT_ESTABLISHED; FULL_PASS NO; aggregate NOT_AUTHORIZED. No gate promotion.
- Post-release only: after 20:30 IST inspect official Banxico publication page. If Q3 release is present, capture raw bytes/metadata/UTC/hash and inspect Q2 revised portfolio asset/liability rows plus explicit revision vintage; do not treat Q3 flows as Q2 or release date alone as vintage proof. If absent, stop and preserve PENDING.
- Report: docs/GCR_MEXICO_MEX_Q2_2026_BANXICO_Q3_RELEASE_SCHEDULE_AND_VINTAGE_GATE_PRECHECK_CONTINUATION244_20261125.md; commit 86196e69abcd73f494e19e3ec2519e112f50e0d7. No IMF re-query/cohort rebuild, ₹0, no production changes; UNKNOWN never PASS.


## GCR Continuation 245 — Uzbekistan UZB CBU latest-vintage / release-calendar boundary (25-Nov-2026)
- Mandatory preflight re-read current Ledger, Priority Queue, Registry, fixed 63-country matrix, Library Mother File GCR pages 46–53, and controlling UZB C123 report. Existing numeric dual-leg PASS reused; no IMF re-query, cohort rebuild, repeated arithmetic or repeated identical XLSX-byte attempt.
- New official evidence: CBU standard BOP dataset page indexed update 29-Sep-2026 and Q2-2026 as latest; official e-GDDS calendar lists Q2 publication 30-Sep and Q3 publication 31-Dec. CBU official H1-2026 review announcement dated 29-Sep reports net portfolio investment inflows around USD2bn only; it does not provide Q2 separate asset/liability legs or observation revision timestamp. A distinct H1 statistical bulletin XLSX appears as an indexed locator on the statistics page updated 24-Nov, but the dynamically opened cached page was stale and did not expose/serve the workbook; no workbook bytes or metadata captured.
- Unit/time-basis issue remains: CBU e-GDDS Q2 dataset says “million USD, end of period”; without workbook headers the Q2 portfolio transaction-vs-stock time basis is NOT_ESTABLISHED. Dataset update date and IMF retrieval date do not prove same-vintage.
- UZB remains DATA_CAPTURED; existing asset/liability numeric PASS retained; vintage PENDING; FULL_PASS NO; aggregate NOT_AUTHORIZED. No matrix gate changed.
- Report: docs/GCR_UZBEKISTAN_UZB_Q2_2026_CBU_LATEST_VINTAGE_AND_RELEASE_CALENDAR_BOUNDARY_CONTINUATION245_20261125.md; report commit 5a4efbb7d5608682b482419d48e18070826ca6e9.
- Next: only a supported byte-preserving capture of the distinct CBU H1-2026 statistical bulletin or new Q2 workbook; inspect headers/time basis and observation-specific revision metadata. If unavailable, retain blocker and advance next eligible fixed-cohort task after preflight. ₹0; production unchanged; UNKNOWN never PASS.


## GCR Continuation 245 — Uruguay URY Q2 preliminary-status / Q3 release vintage gate (25-Nov-2026)
- Mandatory preflight re-read current Ledger, Priority Queue, Historical Registry, fixed 63-country matrix, C244 report and Library Mother File / prior URY context. Reused prior URY Table 9 separate-leg numeric PASS; skipped repeated arithmetic, IMF re-query and cohort rebuild.
- New official BCU evidence: Q2 2026 BOP/IIP report still labels figures preliminary; Table 9 provides sector-level portfolio flow detail. Official BCU statistics calendar lists “Cuentas Internacionales 3er Trimestre 2026” for 30-Dec-2026. This is a future release schedule, not evidence of a Q2 revision.
- No Q2 revision identifier, observation-specific timestamp or explicit BCU-to-IMF vintage bridge found. URY numeric dual-leg PASS remains reused; vintage PENDING / NOT_ESTABLISHED; FULL_PASS NO; aggregate NOT_AUTHORIZED. Matrix unchanged because no gate changed.
- Detail: docs/GCR_URUGUAY_URY_Q2_2026_BCU_PRELIMINARY_STATUS_AND_Q3_RELEASE_VINTAGE_GATE_CONTINUATION245_20261125.md; sources turn142592view0 / turn795836view0 / turn874156search0 / turn874156search4. Next: after 30-Dec-2026 inspect Q3 release for Q2 revised legs and explicit vintage bridge; if absent, retain UNKNOWN and advance after fresh preflight. ₹0; no production changes; UNKNOWN never PASS.


## Nightly Rotation Review — 25-Nov-2026 (C76)
- Preflight reused 25-Nov morning alert, 25-Nov Failure & Lessons Register, C72–C75 evidence, 24-Nov nightly report and accepted Run #410/#421 artifacts. No completed PASS task repeated; no new NSE acquisition or broad workflow dispatch.
- 25-Nov morning report: docs/DAILY_UNIFIED_TOP5_SWING_WATCHLIST_20261125.md, blob SHA-1 2376b36ec30265805facd1d3a94f23833e06a16c; market-data cutoff 23-Nov close; qualified candidates 0/5; live 1m feed HTTP 403/zero rows.
- Reused prospective tracker Run #410 / ID 45490518576, artifact #14966627305, head ab7287e42921629a89977e551c2ed7410c6ad07c, SUCCESS, 9m52s; ZIP SHA-256 6b1673af895214ae982fb445a62d5536dd2960eb062dc310b85f955b01c8af16. It is pre-market evidence, not a post-close outcome artifact.
- 23-Nov shadow cohort remains 7 unique symbols / 10 signal rows; H+1 was due 25-Nov close, but no new calendar-correct post-close row-level outcome artifact was found. H+1 PENDING/UNKNOWN; H+3 expected 27-Nov; H+5 expected 01-Dec. 24-Nov holiday cohort (9 unique / 10 rows) remains excluded.
- Ultimate +2/+5/+10/+15/+20 historical capture metrics all UNKNOWN/BLOCKED. Prior morning diagnostics are NOT_VALIDATED due 187 unique content sessions from 200 labels, forward-label defect, missing CI and unresolved denominator reconciliation. High-touch, terminal close and executable outcomes remain separate; executable replay NOT_AUTHORIZED.
- Track A V11.4 BLOCKED/NOT_VALIDATED; Track B V11.3 UNKNOWN/NOT_AUTHORIZED; Track C GCR UNKNOWN/BLOCKED (P0 6/8; final FPI/DII and USD/INR historical archive blockers). Best-3 historical lists all UNKNOWN/BLOCKED; next-session qualified candidates 0, five slots unfilled.
- No accepted new walk-forward validation; 0 new validation jobs. No comparable pp change; fixed baseline/latest rolling NOT_COMPARABLE. No false-positive/missed-winner attribution without a reconciled eligible-universe ledger.
- Existing lesson PW-LSN-20261125-001 updated in place; no duplicate lesson. Calendar-aware tracker regression remains OPEN; expected artifact calendar_aware_tracker_regression.json. H+1 reconciliation remains pending.
- Dated report: docs/NIGHTLY_ROTATION_BACKTEST_RESEARCH_REVIEW_20261125.md; create commit 24371d62112d6070977fda5bb242c1f5a0839575; blob SHA-1 cdc3b9d1332733cbb0131f361251891bf829dc99. Report SHA-256 not independently computed. No new run/artifact.
- Acceptance: overall PARTIAL/BLOCKED; no performance PASS. No selector, ranking, threshold, Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A–E or IPO-PLX V2.0 change. ₹0; free official sources only; UNKNOWN never PASS.


## 20. Continuation 76 — 25-Nov after-close next-session Top-5 evidence gate (25-Nov-2026)
- Mandatory preflight: re-read Master Continuity Ledger through C75, C74 25-Nov morning report, C75 holiday-tracker root-cause report, 25-Nov Failure & Lessons Register and prior Nightly report. Reused accepted Run #410 artifact evidence; no repeat ZIP download, broad workflow, or new NSE acquisition.
- Next official NSE equity session: 26-Nov-2026 (Thursday), checked against the official NSE 2026 holiday list. 25-Nov is not a listed equity holiday.
- Current official NSE live-equity page rendered quote table as Loading and market snapshot values blank in the current retrieval surface. Official quote pages for JNPR, SKYWAYS and FINOPB also returned no usable price/volume values. This is a retrieval/rendering limitation; it does not prove NSE had no EOD data.
- NSE corporate-filings page lists 25-Nov entries for JNPR (order/contract), SKYWAYS (acquisition) and FINOPB (board-meeting outcome). Company/ISIN mapping is available from official NSE filing pages, but detailed latest filing payload and fresh EOD price/volume/RS/liquidity/circuit verification were not captured. These remain filing leads only, not provisional or qualified picks.
- Decision: 0 QUALIFIED / 0 PROVISIONAL / 5 UNFILLED. No reference prices or scenario bands calculated. Target-wise historical capture and historical Best-3 remain UNKNOWN/NOT_VALIDATED; V11.4 NOT_VALIDATED, V11.3 replay UNKNOWN/NOT_AUTHORIZED, GCR UNKNOWN/BLOCKED.
- Prior 23-Nov cohort (7 unique symbols / 10 rows) H+1 was due 25-Nov close; without the raw official EOD file and independent row reconciliation it remains PENDING/NOT_VERIFIED. H+3=27-Nov, H+5=01-Dec.
- Reused Run #410 / 45490518576, job 138787290238, artifact 14966627305; prior independently verified ZIP SHA-256 6b1673af895214ae982fb445a62d5536dd2960eb062dc310b85f955b01c8af16; no new workflow dispatch. Run #421 artifact 14936656169 retained as previously verified.
- Existing lesson PW-LSN-20261124-002 updated for current official quote-page rendering/source-readiness limitation; existing PW-LSN-20261125-001 carried forward for holiday-aware maturity. No duplicate/new predictive lesson.
- Report: docs/DAILY_UNIFIED_TOP5_NEXT_SESSION_20261126_20261125_AFTER_CLOSE.md; commit 983ae0dd22bafa04419bd383a5378b0a227523d3; SHA-256 8b19a10b2d5ae050675bf74e764091de07c8b790f4e2637c51a3c97ae218ce6c.
- Lessons log: docs/FAILURE_LESSONS_LEARNED_20261125.md; commit 98927edc3e6782a53f0136bff88de27181d543d4; SHA-256 ad54915457c68de6c2d110201c3c46fba4fa2c445017055bfcc0b6bba32d7e95.
- Acceptance: continuity preflight PASS; reuse of prior artifact evidence PASS; next-session calendar PASS; fresh official EOD price/volume capture NOT_DONE; candidate qualification 0/5; previous cohort H+1 outcome PENDING/NOT_VERIFIED; all performance tracks remain non-PASS.
- Next: obtain exact official 25-Nov CM-UDiFF EOD bytes and manifest through a permitted route; independently validate source date/bytes/hash; then reconcile 23-Nov cohort H+1 high-touch, terminal close and adverse excursion with exact OUTCOME_LAST_DATE. No production changes; ₹0; UNKNOWN never PASS.


## Continuation 77 — user-directed full-universe missed-winner discovery (25-Nov-2026)
- User identified an unacceptable research gap: market stocks made +2% to +20% moves while the alert returned no qualified candidates. Requirement is to identify these missed winners, explain why they were not captured, and carry evidence-backed learning into every subsequent alert.
- Re-read the current continuity ledger, Failure & Lessons Register and 25-Nov morning/nightly/after-close evidence before adding this continuation.
- Evidence-backed reasons current individual missed winners cannot yet be named: (1) no reconciled point-in-time eligible-universe decision ledger linked to per-symbol selector decisions; (2) 25-Nov morning live 1m retrieval path HTTP 403 / zero rows / zero symbols; (3) 23-Nov shadow cohort 7 unique symbols / 10 signal rows remains H+1 PENDING because 24-Nov was a holiday and tracker lacks official session-spine validation; (4) prior historical labels NOT_VALIDATED due 187 unique content sessions from 200 date labels plus forward-label/denominator defects.
- Confirmed blockers do not establish which stock was missed or which filter failed. Exact stock names, per-filter reason and cutoff-time signal remain UNKNOWN until full-universe outcome reconciliation and point-in-time decision trace are available.
- New report: docs/MISSED_WINNER_DISCOVERY_AND_RESEARCH_INTEGRATION_20261125.md. It defines full-universe +2/+5/+10/+15/+20 H+1/H+3/H+5 audit, unique symbol vs signal-row accounting, high-touch vs close vs executable outcomes, cutoff-only root-cause reconstruction, confidence classes and four bounded acceptance artifacts.
- Failure & Lessons Register updated with the same requirement and acceptance tests; existing lesson IDs preserved, no fabricated predictive lesson.
- Acceptance tests OPEN: point_in_time_decision_ledger_audit.json; calendar_aware_tracker_regression.json; universe_missed_winner_reconciliation.json; missed_winner_root_cause_audit.json.
- Carry-forward requirement: every morning and nightly alert must include prospective Top-5 (qualified only), matured full-universe missed-winner list, root-cause table, recurring lesson updates and next validation test. If full-universe data/decision trace is absent, explicitly report exact UNKNOWN/BLOCKED coverage; never infer there were no missed winners.
- Automation prompt persistence was attempted but the automation update action returned NOT_FOUND; therefore this continuation does NOT claim that the scheduled automation prompts were changed. Alert integration remains OPEN until the saved automation definitions are successfully updated and read back.
- Observation-only; ₹0/free official sources; no synthetic data, look-ahead, threshold or production changes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A–E and IPO-PLX V2.0 unchanged.


## GCR Continuation 246 — Mexico MEX Banxico Q3 publication / Q2 vintage recheck (25-Nov-2026)
- Mandatory preflight: re-fetched current Master Ledger, Priority Queue, Historical Task Registry, fixed 63-country matrix and Library Mother File; reused C244 MEX precheck and earlier C137/C208 Q2 dual-leg work. No IMF re-query, cohort rebuild or repeated arithmetic.
- C244 scheduled the Banxico post-release check after 20:30 IST. Official Banxico index now lists the Q3-2026 BOP release dated 25-Nov-2026; official PDF inspected.
- New Q3 release's Q2 portfolio rows: net acquisition of assets USD 9,480m; net incurrence of liabilities USD 10,561m; portfolio balance USD -1,082m. Prior numeric dual-leg PASS is retained, not recalculated.
- The release footnote says some BOP items were revised and identifies principal revisions in profits/dividends, direct investment and services. It does not explicitly identify portfolio asset/liability rows as revised or unchanged and supplies no observation-specific revision timestamp/version bridge.
- Latest Q2 snapshot found; same-vintage with archived IMF rows remains NOT_ESTABLISHED. Raw PDF bytes/headers/SHA-256 were not captured. MEX remains DATA_CAPTURED; asset/liability PASS reused; vintage PENDING; FULL_PASS NO; aggregate NOT_AUTHORIZED. Matrix gates unchanged.
- Report: docs/GCR_MEXICO_MEX_Q2_2026_BANXICO_Q3_RELEASE_POSTPUBLICATION_VINTAGE_RECHECK_CONTINUATION246_20261125.md; report commit 2a4e47d5d82933ffe11bedcc2a0738d4b8994458. Next: compare Q2 portfolio pair against exact 25-Aug first-release table; record any row-level delta and official revision evidence. If no explicit vintage bridge, retain UNKNOWN and advance after fresh preflight. ₹0; no production changes; UNKNOWN never PASS.


## GCR Continuation 247 — CHN SAFE Q2 dual-leg / sign-crosswalk audit (25-Nov-2026)
- Preflight re-fetched Master Ledger, Priority Queue, Historical Registry, fixed 63-country matrix; Library Mother File and prior CHN instructions reviewed. Reused 19-Nov archived IMF sample files; no IMF re-query.
- SAFE official Q2 release (29-Sep, index 000014453-2026-0068) table unit USD100m: portfolio assets -488, liabilities +433; values rounded; SAFE states BPM6, credit positive/debit negative, and BOP data revised regularly.
- Archived IMF Q2: A_NFA_T +USD48,794,459,103.55; L_NIL_T +USD43,286,600,714.23. SAFE rounded magnitudes differ by USD5.540896m and USD13.399286m; USD100m display precision cannot test ±USD0.5m. SAFE asset sign differs from IMF A_NFA_T; exact field-level sign mapping not established. Asset REVIEW; liability PASS retained as prior matrix state only; vintage PENDING; FULL_PASS NO; aggregate NOT_AUTHORIZED.
- SAFE 13-Nov Q3 release lacks portfolio rows in standalone table; cumulative 9M table not used for Q2 back-solving. Detailed time-series XLSX bytes/schema/hash/revision bridge not captured.
- Report/status: docs/GCR_CHN_C247_STATUS_20261125.md (commit 7fd26ccf0bc1d3be33657e5e3a7901a355136620); matrix commit 104d57c06737f2c5b1a00cd04f6fd9c814f11abe. Next: distinct supported SAFE XLSX transfer route only; no repeat failed route/IMF query. ₹0; cohort fixed; production unchanged; UNKNOWN never PASS.


## C246 authoritative correction note (carried forward in C247)
- The C246 first-pass prose above is superseded by the later direct comparison: 25-Aug Banxico Q2 asset USD8,937m vs 25-Nov Q3-release Q2 asset USD9,480m (+USD543m); liabilities USD10,561m unchanged. Archived IMF asset USD8,937.255098m now differs by USD542.744902m; liability USD10,561.285114m differs by -USD0.285114m.
- Correct MEX gate: asset REVIEW, liability PASS, vintage PENDING, FULL_PASS NO, aggregate NOT_AUTHORIZED. Fixed cohort matrix row is already synchronized and read back. Do not rely on the earlier C246 sentence saying both legs PASS. The correction report is docs/GCR_MEXICO_MEX_Q2_2026_BANXICO_Q3_RELEASE_POSTPUBLICATION_VINTAGE_RECHECK_CONTINUATION246_20261125.md; addendum availability must be checked separately.


## GCR Continuation 248 — Colombia COL Q2-2026 source-scope boundary (26-Nov-2026)
- Mandatory preflight: current Ledger, GCR Queue, Historical Task Registry, fixed 63-country matrix, Library Mother File and COL C151/C152/C162 reports re-read. CHN C247, MEX C246 and all previously accepted PASS work skipped.
- Official BanRep catalogue confirms separate quarterly BOP portfolio net-acquisition-of-assets and net-incurrence-of-liabilities series in current USDm through Q2-2026. A separate monthly local-market foreign portfolio flow series is not equivalent and is not admitted as a substitute. Q2 IIP positions are stocks; the Q2 financial-account aggregate includes other components; both excluded.
- Identical SUAMECA 502/dashboard routes and desktop procedure were not repeated. No raw Q2 legs, series IDs, export bytes/hash, portfolio sign crosswalk or same-vintage bridge obtained. COL remains BLOCKED / NOT PASS; 63-country aggregate NOT_AUTHORIZED.
- Report commit: a1206349a0ae0285e97b5e406fdbfc05651296b2; report: docs/GCR_COLOMBIA_COL_Q2_2026_OFFICIAL_PORTFOLIO_SERIES_SCOPE_AND_ALTERNATE_ROUTE_AUDIT_CONTINUATION248_20261126.md.
- Matrix COL row evidence_ref/note updated; gate statuses unchanged. Next eligible cohort task POL, with exact preflight and no unsupported PLN→USD conversion. ₹0; no IMF re-query/cohort rebuild; production invariants unchanged; UNKNOWN never PASS.


## GCR Continuation 249 — Poland POL Q2-2026 NBP v2.1 publication / latest vintage boundary (26-Nov-2026)
- Mandatory preflight: re-read current Master Ledger, GCR Queue, Historical Registry, fixed 63-country matrix, Library Mother File 1–53, and POL C163/C164/C165/C181. Reused national PLN legs and transaction-date FX rule; skipped C248, all PASS work, prior extraction, NBP byte-download retries, IMF re-query and cohort rebuild.
- Fresh official NBP public reporting-list review found explanatory notes version 2.1 dated 13-Jul-2026. The page extraction exposes metadata only; the v2.1 attachment URL/bytes/text were not exposed. Do not claim its unseen contents.
- Inspected retrievable official NBP v2.0 explanatory notes (June 2025): other data use actual transaction-date rate or prior-day NBP average rate; rates used for reporting conversions have four decimal places. This corroborates C165 transaction-date rule but does not supply Q2 transaction currency/date weights.
- Latest indexed NBP monthly BOP publication 13-Nov-2026 covers September and is explicitly preliminary/revisable; it is not a matched Q2 USD portfolio dual-leg table and does not establish NBP 30-Sep vs IMF 19-Nov observation-specific same vintage.
- POL national legs remain 24,144 mn PLN assets and 70,910 mn PLN liabilities (PASS reused). New matched USD dual legs NOT_FOUND in bounded public-source review; transaction-level currency/date weights NOT_CAPTURED; NBP Q2 raw PDF SHA-256 NOT_CAPTURED; same-vintage NOT_ESTABLISHED; cross-currency comparison NOT_DONE; POL PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Report: docs/GCR_POLAND_POL_Q2_2026_NBP_VERSION21_PUBLICATION_AND_LATEST_VINTAGE_BOUNDARY_RECHECK_CONTINUATION249_20261126.md; report commit 37573606aa47bb1fa65a14ddbf66032088e98e42.
- Matrix POL explanatory note/evidence_ref updated; all gate states unchanged. Next candidate MNE: only a genuinely supported CBCG Tables 5.1–5.4 annotation/link extraction or distinct official export route; do not repeat C241's failed PDF-reader/byte-download paths. ₹0; no IMF re-query/cohort rebuild; production invariants unchanged; UNKNOWN never PASS.

## GCR Continuation 250 — MNE Montenegro Q2-2026 official CBCG BPM6 download route fingerprint (26-Nov-2026)
- Mandatory preflight: re-read current Master Ledger, GCR Queue, Historical Registry, fixed 63-country matrix, Library Mother File 1–53 and MNE C241. Skipped PASS work, C249 Poland, CBCG Bulletin PDF reader/byte retries, old CBCG ZIP route, MONSTAT NSDP SDMX/XML/Browse, IMF re-query and cohort rebuild.
- New official CBCG BOP statistical page located: https://www.cbcg.me/me/statistika/statisticki-podaci/ekonomski-odnosi-sa-inostranstvom/platni-bilans. It states BPM6 compilation, quarterly EUR reporting, financial account shown as net acquisition of assets / net increase in liabilities, and page updated 19-Nov-2026.
- Official page BPM6 (2010–2026) link resolved to exact URL: https://www.cbcg.me/slike_i_fajlovi/fajlovi/fajlovi_publikacije/statistika/bop_sep_2026.zip. This is distinct from the old CBCG bulletin ZIP route and the C241 PDF path.
- Web retrieval rejected application/zip as unsupported content-type (reader limitation); separate direct byte-download attempt failed. No ZIP bytes, headers, size, archive listing, workbook/table, Q2 portfolio A/L legs or SHA-256 captured. Filename `bop_sep_2026` is not proof of internal period coverage.
- MNE source discovery/download locator PASS only; actual data NOT_CAPTURED; separate portfolio asset/liability NOT_CAPTURED; sign/unit mapping NOT_ESTABLISHED; national comparison NOT_DONE; vintage UNKNOWN; MNE BLOCKED / PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Report: docs/GCR_MONTENEGRO_MNE_Q2_2026_CBCG_OFFICIAL_BPM6_DOWNLOAD_ROUTE_FINGERPRINT_CONTINUATION250_20261126.md; commit 0026acf7352ff6711b31b292fe2ab41963aad04c. Matrix note/evidence_ref updated without gate promotion. Reopen only with supported official ZIP byte retrieval or another distinct CBCG endpoint. ₹0; no production changes; UNKNOWN never PASS.

## GCR Continuation 251 — ALB Albania official USD archive Q2 eligibility / vintage boundary (26-Nov-2026)
- Mandatory preflight re-read current Ledger, Queue, Registry, fixed 63-country matrix, Library Mother File 1–53, C250 and ALB C139/C237/C238. Skipped all PASS work, repeated EUR PDF extraction, legacy Main-data route, C238 methodology PDF, IMF query and cohort rebuild.
- New official BoA archive navigation discovered separate `Balance of Payments USD (Quarterly)` and `Financial Account USD (Quarterly)` plus `Financial account USD (New format) (Quarterly)` series. Legacy USD BOP child page explicitly selects Q1-1993 through Q4-2013 and says 11-Sep-2017 publication revised 2013 data. New-format USD financial-account page also carries 11-Sep-2017 revision note and exposes asset/liability portfolio taxonomy, but no Q2-2026 observation cells.
- These legacy USD series are not eligible as a Q2-2026 conversion bridge; no USD value, FX conversion, revision link, raw export or SHA-256 captured. Reused C237 EURm legs +156.25 assets/+124.70 liabilities; C238 general average-flow FX convention remains PASS only at broad-method level. Q2-specific EUR→USD aggregation and same-vintage remain NOT_ESTABLISHED/UNKNOWN. ALB DATA_CAPTURED / PARTIAL / NOT PASS; asset/liability REVIEW; aggregate NOT_AUTHORIZED.
- Report: docs/GCR_ALBANIA_ALB_Q2_2026_BOA_LEGACY_USD_ARCHIVE_Q2_ELIGIBILITY_AND_VINTAGE_BOUNDARY_CONTINUATION251_20261126.md; commit 9835344450ed796d63bbaedbf633fb3bcc531296. Matrix note/evidence_ref updated without gate promotion. Do not reuse the 2013-ending USD archive as 2026 bridge. ₹0; production unchanged; UNKNOWN never PASS.

## GCR Continuation 252 — HUN Hungary MNB post-C138 release-calendar / monthly-BOP trigger check (26-Nov-2026)
- Mandatory preflight re-read current Ledger, Queue, Registry, fixed 63-country matrix, Library Mother File 1–53, C251 and full HUN C138/C139 report. Reused Q2 legs and methodology; skipped repeated PDF extraction, IMF panel extraction and C139 monthly-data route.
- Official MNB release calendar lists 13-Nov-2026 `Monthly balance of payments` for reference period September 2026; official MNB statistics homepage still shows BOP/IIP last updated 25-Sep-2026, reference period Q2 2026. Calendar/homepage retrieval exposes no monthly portfolio A/L transaction observations, Q2 revision ID or MNB↔IMF same-vintage bridge. This is not evidence that monthly BOP label contains portfolio legs.
- C138 values reused: assets EUR +2,104m; liabilities EUR +8,380m; reported net EUR -6,277m (retain EUR1m displayed rounding difference). C138 methodology/revision policy remain general PASS; C139 monthly portfolio route remains closed/unavailable. Cross-currency reconciliation NOT_DONE; exact item equivalence/vintage NOT_ESTABLISHED; HUN DATA_CAPTURED / PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Report: docs/GCR_HUNGARY_HUN_Q2_2026_MNB_POST_C138_RELEASE_CALENDAR_AND_MONTHLY_BOP_VINTAGE_TRIGGER_RECHECK_CONTINUATION252_20261126.md; commit 8af5f5c0e9197078651f219b6aa14c058f60b89b. Matrix corrected to reflect C138 national legs already captured, no numeric gate promotion. Reopen only on new monthly portfolio A/L dataset, Q2 revision artifact or Q3 BOP/IIP report. ₹0; production unchanged; UNKNOWN never PASS.

## GCR Continuation 253 — CHL Chile Q2 portfolio net revision / vintage boundary (26-Nov-2026)
- Mandatory preflight re-read current Ledger, Queue, Registry, fixed 63-country matrix, Library Mother File 1–53, CHL C160 and C161. Reused earlier BDE monthly dual-leg observations and IMF raw rows; did not repeat BDE extraction, credential-gated API, public basket export, IMF query or cohort rebuild.
- New official BCCh Q3-2026 BOP/IIP report (18-Nov-2026) explicitly states Q1 and Q2 BOP data were revised. Table 1 shows Q2 portfolio-investment net USD +154m, compared with USD +299m in the earlier Q2 publication captured in C160: net revision -USD145m.
- Q3 report Table 3 shows Q2 total financial-account assets revised 1,114→2,051 USDm and liabilities 4,536→5,118 USDm. These are overall financial-account totals / institutional-sector cuts, not portfolio-only A/L. No Q2 portfolio revised A/L pair or observation-specific BDE series update receipt was exposed. No net-to-leg back-solving.
- Prior C160 BDE Q2 monthly legs +5,098.91 assets / +5,397.51 liabilities remain earlier source-page vintage only; they cannot be relabelled current-vintage after the published net revision. C161's API token gate/public basket export boundary remains unchanged.
- CHL remains DATA_CAPTURED / PARTIAL / NOT PASS; asset/liability gate values retained as existing historical numeric evidence, vintage PENDING, full NO, aggregate NOT_AUTHORIZED. Current-vintage dual-leg comparison NOT_DONE. Report: docs/GCR_CHILE_CHL_Q2_2026_BCCH_Q3_RELEASE_PORTFOLIO_NET_REVISION_AND_VINTAGE_BOUNDARY_CONTINUATION253_20261126.md; report commit 02c7ff97ea91d09423ec1a30c9e589aa016a3ec2.
- Reopen only with executed authorized public BDE export or another accessible official export giving both revised Q2 portfolio legs, series identifiers, update/vintage metadata and raw bytes/hash. ₹0; no IMF re-query/cohort rebuild; production invariants unchanged; UNKNOWN never PASS.


## GCR Continuation 254 — MEX Mexico later IMF archive inventory / vintage bridge boundary (26-Nov-2026)
- Mandatory preflight re-read current Ledger, Queue, Registry, 63-country matrix, Library Mother File 1–53, MEX C137/C208/C246 and the 19-Nov IMF panel/receipt files. Reused all existing national and IMF evidence; no IMF query or panel/cohort rebuild.
- C246's open next action was to determine whether a later IMF vintage already existed in archived panel files. Inspected panel report `docs/GCR_IMF_BOP_EMDE_PANEL_PART2_20261119.md`, exact receipt `docs/evidence/imf_bop_emde_20261119/exact_sample_checks/summary.json`, and both broad raw CSVs. The only MEX exact-key receipt found is dated 19-Nov-2026 06:45:19 UTC; no later MEX raw snapshot, receipt or later IMF panel artifact was found in bounded GitHub/Library search. This is not proof of absence outside those searchable records.
- Reused exact MEX rows: A_NFA_T OBS_VALUE 8,937,255,098 SCALE=6; L_NIL_T OBS_VALUE 10,561,285,114 SCALE=6. Exact raw hashes: asset a404aca5a719b9558e75b9483b925d18011fa2d9199937d275956782a84c5014; liability 1a7de8eb3d258875fbffbde987ce22db437eadbdd9c93e05acec12a4ab7785c7. No scale conversion/reconciliation rerun.
- C246 Banxico comparison reused: Q2 assets 8,937→9,480 USDm (+543); liabilities 10,561 unchanged. Without a later IMF receipt or Banxico observation-specific revision/version bridge, same-vintage remains NOT_ESTABLISHED. MEX remains DATA_CAPTURED / PARTIAL / NOT PASS; asset REVIEW; liability PASS; vintage PENDING; FULL_PASS NO; aggregate NOT_AUTHORIZED.
- Report: docs/GCR_MEXICO_MEX_Q2_2026_IMF_LATER_ARCHIVE_INVENTORY_AND_VINTAGE_BRIDGE_BOUNDARY_CONTINUATION254_20261126.md; commit ab937972f13098af06f4a25e35e47f0f7d3f35a0. Matrix note and evidence_ref updated only; no gate promotion. Do not re-query IMF or rebuild panel/cohort. Reopen only on a later archived IMF snapshot with verifiable receipt/hashes or explicit Banxico Q2 revision/version bridge. ₹0; production invariants unchanged; UNKNOWN never PASS.


## Daily Unified Top-5 Alert 255 — 26-Nov-2026 pre-market
- Mandatory preflight re-read current Master Continuity Ledger C254, 25-Nov morning/nightly reports, Failure & Lessons Log, Missed-Winner Integration note, Run #410 and Run #411 evidence. Existing PASS byte-integrity checks reused; no repeated broad workflow or paid source.
- Next NSE equity session confirmed as 26-Nov-2026; 24-Nov is official Prakash Gurpurb Sri Guru Nanak Dev holiday. Review cutoff 26-Nov-2026 08:40:05 IST; latest completed market session 25-Nov.
- Run #411: ID 45695700887; job 139492398062; artifact 15061666636; workflow head fa3220dbddf3dc204eb2f20d08a0a44af719950a; audit-branch commit f96f9e8448d121b9f781cf526ed8e838ad3552e9; runtime ~8m35s. ZIP SHA-256 independently verified: 6685f9d5d092ff4a8fe505040b0a08f4183e78339a56a53bcfaa6d666d256897. Artifact contains 17 files but no raw source ZIP/per-file manifest or full-universe decision ledger.
- Run #411 QA nominally reports 200 files/dates, 3,001 symbols, 504,971 rows and 100% delivery coverage; semantic 200-session acceptance NOT_MET. Prior semantic records conflict between 187 and 188 unique sessions; unresolved. Raw 25-Nov source URL/retrieval timestamp/bytes/per-file SHA absent from artifact.
- Raw CURRENT_WINNER_PROB leads: SHALPAINTS, APLAPOLLO, PASHUPATI, OAL, NECCLTD. Their score field is percentile rank, not probability. Official NSE pages expose stale quote, ST/LT ASM, upper-band/5% circuit, 100% margin, impact-cost/liquidity or governance flags. None passed final hard gates. Top-5 status: 0 qualified / 0 provisional / 5 unfilled. No target bands or probability issued.
- A Top-30 exploratory metrics from Run #411: +5 H+1 952/2,977 (31.98%), FP 2,025; +10 H+3 625/2,896 (21.58%), FP 2,271; +15 H+5 379/2,827 (13.41%), FP 2,448; +20 H+5 194/2,827 (6.86%), FP 2,633; +2 UNKNOWN. These are not accepted because session/label/denominator integrity is unresolved. Run #410 to #411 input hash changed (e788b0... → 25cfbd...), so metric drift is NOT_COMPARABLE.
- Historical best three for all targets remain <3/UNKNOWN. B Cost-aware Replay UNKNOWN/NOT_AUTHORIZED; C GCR UNKNOWN/BLOCKED.
- 23-Nov cohort remains 7 unique symbols / 10 rows; tracker has T1_HIGH_PCT/MATURED_T1 but blank OUTCOME_LAST_DATE, despite 24-Nov holiday. Correct H+1/H+3/H+5 = 25-Nov/27-Nov/01-Dec. PW-LSN-20261125-001 remains OPEN. 25-Nov cohort = 7 unique / 10 rows; H+1/H+3/H+5 = 26-Nov/30-Nov/02-Dec, all PENDING at pre-market.
- Full-universe missed winners remain UNKNOWN/BLOCKED: point-in-time eligible-universe decision ledger and full-universe matured outcome rows absent. No CORE-672 filter cause inferred.
- New immutable lesson PW-LSN-20261126-001: raw prospective model percentile output lacks current official risk/admission fields; code-level gap VERIFIED, predictive impact UNKNOWN. Existing PW-LSN-20261121-001/002, 20261121-003, 20261123-001, 20261124-002/003/004/005 and 20261125-001 carried forward; no duplicate IDs.
- Report: docs/DAILY_UNIFIED_TOP5_SWING_WATCHLIST_20261126.md; commit f1f73e4c59ccffb3e489130c184f7867b26b4025; blob 8377cd15d3e8b570db638e58deee604bb188d538; SHA-256 2b62374501b0625833cda0469c9d52622cc4eab001bf48f287590c6c7831e34b; exact read-back verified=true.
- Failure log: docs/FAILURE_LESSONS_LEARNED_20261126.md; commit f1b8f21eaa57862d786e52c5df0a77015637b596; blob 7a6c08f5c2004458e5a2eb2218ed9d2c9199beb0; SHA-256 1923c0935bbe8c28b392f1bf8bb4ceb65b21cbd63e6d0980c2ec6df2b86be6d4; exact read-back verified=true.
- Evidence artifact reused: Run #411 artifact 15061666636; ZIP SHA-256 above. Output SHA-256 latest_picks bc489366de4cfad3811042d8ca9a362489039ed3fcd6eb2fb71e7f56c9f5bedc; watchlist ledger 3d4e04063b200044ae89529dc6f3b7349bd83d81b17ab19e3748e7ab4c58f3e2; walk_forward_metrics 1353f7df37fbbbf3f1bdebd9b9af16c812988e1ca866c2f8b0eb762ee461ef83; QA 77ee88c0ec576ce644597492174e3ab5a498662e5adf9443b83e85627f80599c.
- Next bounded tests: calendar_aware_tracker_regression.json; point_in_time_decision_ledger_audit.json; universe_missed_winner_reconciliation.json; missed_winner_root_cause_audit.json; prospective_risk_gate_admission_audit.json. Reuse existing evidence, each job ≤10 minutes.
- Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2.0 unchanged. ₹0; no paid APIs; no synthetic data, forward-fill, guessed mapping, fabricated timestamp, look-ahead or production change. Overall PARTIAL/BLOCKED; UNKNOWN never PASS.


## GCR Continuation 255 — ZAF South Africa SARB EXCX135D Q2 daily FX coverage / endpoint boundary (26-Nov-2026)
- Mandatory preflight re-read current Ledger, Queue, Registry, fixed 63-country matrix, Library Mother File 1–53, and ZAF C127/C215. Reused prior numeric reconciliation; skipped IMF fetch, SARB PDF/table extraction, OECD quarter-average arithmetic and cohort rebuild.
- Official SARB OpenAPI documents `HistoricalExchangeRatesDaily`, no-date observations endpoint and date-bounded observations endpoint. EXCX135D is Rand per US Dollar. Its description says weighted average of banks' daily rates at approximately 10:30 am.
- New no-date observations route exposes 24 visible rows in this retrieval: only 2026-04-01 (16.8446), 04-02 (16.9611) and 04-07 (16.8258) are Q2 dates; remaining rows are March 2–31. No May/June observations in this response. Do not treat this as complete Q2 history.
- The documented 2026-04-01/2026-06-30 route and two alternate date-format probes were inaccessible via current web retrieval; this is a retrieval-channel limit, not proof SARB API is broken. Separate daily snapshot last visible date 2026-08-07; monthly snapshot omitted EXCX135D. No full Q2 bytes/headers/API retrieval UTC/hash.
- No Q2 average or FX conversion calculated; SARB BOP portfolio transaction conversion convention remains NOT_ESTABLISHED. Existing ZAF liability PASS retained; asset REVIEW; vintage PENDING; PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED. Report docs/GCR_SOUTH_AFRICA_ZAF_Q2_2026_SARB_EXCX135D_DAILY_SERIES_Q2_COVERAGE_AND_HISTORICAL_ENDPOINT_ACCESS_BOUNDARY_CONTINUATION255_20261126.md; commit 81d155fe62f823d317c6d678f2f3bead446efd8e.
- Reopen only with complete official Q2 daily response or distinct official export, raw bytes/headers/retrieval UTC/hash, and SARB-specific BOP conversion method. ₹0; no IMF re-query/cohort rebuild; production invariants unchanged; UNKNOWN never PASS.


## GCR Continuation 256 — CPV updated BCV BOP statistical-table locator / XLS access boundary (2026-11-26)
- Mandatory preflight re-fetched the current Ledger, Priority Queue, Historical Task Registry and fixed 63-country matrix; Library Mother File 1–53 and CPV C213 methodology report were reopened. C214 evidence-reference correction checked. PASS work skipped; no IMF re-query/cohort rebuild or repeated old workbook route.
- Official BCV BOP statistical page indexed 17-Nov-2026 lists an XLS “Balança de Pagamentos” document covering Q1-2012 through Q2-2026. This is a new page-level locator. Actual attachment href/filename/MIME/bytes are not exposed; page retrieval returned cache miss/timeout. No raw XLS/hash or workbook contents captured.
- C213 BPM6 methodology remains PASS; BOP flow vs IIP stock boundary retained. No claim that the XLS contains separate Q2 portfolio A/L legs. CPV remains SOURCE_FOUND / PARTIAL / NOT PASS; A/L NOT_CAPTURED; vintage UNKNOWN; aggregate NOT_AUTHORIZED.
- Report: docs/GCR_CABO_VERDE_CPV_Q2_2026_BCV_UPDATED_BOP_STATISTICAL_TABLE_LOCATOR_AND_XLS_ACCESS_BOUNDARY_CONTINUATION256_20261126.md; commit 47c8575c83f201653b7da3be67288547fa1d3e27. No national gate promotion. Reopen only via supported XLS-capable route resolving the actual attachment and preserving raw bytes/provenance; if same C153 fingerprint, close as duplicate. ₹0; production unchanged; UNKNOWN never PASS.
