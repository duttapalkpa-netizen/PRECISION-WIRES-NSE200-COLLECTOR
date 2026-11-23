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
