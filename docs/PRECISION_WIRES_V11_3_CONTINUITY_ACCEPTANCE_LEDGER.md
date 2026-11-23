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
