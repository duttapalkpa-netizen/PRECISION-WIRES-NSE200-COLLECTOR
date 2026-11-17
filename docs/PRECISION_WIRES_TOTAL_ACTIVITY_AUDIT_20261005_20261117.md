# PRECISION-WIRES V11.3 — TOTAL ACTIVITY AUDIT
Audit cutoff: 2026-11-17 (Asia/Kolkata)
Repository: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR
Primary research branch for this audit: `research/global-capital-rotation-overlay-v1`
Audit class: repository-history reconciliation + existing evidence-ledger consolidation
Status: MASTER AUDIT RECORDED; HISTORICAL COVERAGE IS BOUNDED BY RETRIEVABLE GITHUB EVIDENCE

## 0. Executive truth statement
This is the central activity record for the PRECISION-WIRES V11.3 research program from the earliest auditable repository activity through 2026-11-17. The earliest PR activity directly verified in the repository is 2026-10-05 (PRs #1–#3). This is the earliest date proven by the PR history reviewed here; it is not proof that no research or work existed before that date in chats, local files, deleted branches, or other systems.

The audit combines:
1. repository PR history (#1–#38, excluding issue-number gaps);
2. the 2026-11-08 V11.3 Continuity & Acceptance Ledger;
3. the Global Capital Rotation design/source/continuity ledgers and 2026-11-17 activity audit;
4. available project memory on NSE collection, 317-session archive, CORE-672, Engines A–E, macro/geo, backtests, and operating constraints.

This document does NOT claim every individual chat message, every GitHub Actions run, every artifact, or every research page has been independently reconstructed. Where exact evidence is unavailable, status is UNKNOWN / NOT_RECONSTRUCTED. Do not convert it to PASS.

## 1. Repository and PR-history reconciliation
Repository metadata verified:
- Repository: `duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR`
- Default branch: `main`
- Visibility: public
- Linked GitHub permissions: admin/maintain/pull/push
- PR history reviewed: #1 through #38 (35 PR records; #12, #27, #29 are Issues, not PRs).
- PR #20 is the Global Capital Rotation research branch; OPEN / UNMERGED at audit time.
- Research branch `research/global-capital-rotation-overlay-v1` contains the overlay continuity and activity audit documents.
- The PR metadata for #20 at the audit showed 140 commits, 51 changed files and 3,879 additions; this is cumulative PR metadata, not a count of newly completed research gates.

### PR inventory — authoritative state as returned by GitHub on 2026-11-17
| PR | Scope | State | Merged | Notes |
|---|---|---|---|---|
| #1 | V11.4 stable probability calibration and winner recovery | CLOSED | YES | Early V11.4 experiment |
| #2 | Separation engine + rare-event specialist v2 | CLOSED | YES | Early V11.4 experiment |
| #3 | Winner interactions and transition latent evidence | CLOSED | YES | Early V11.4 experiment |
| #4 | Audit-only feature ablation isolation | CLOSED | YES | Audit experiment |
| #5 | Minimal ranking revision from Run #52 ablation | CLOSED | YES | V11.4 experiment; keep distinct from V11.3 protected baseline |
| #6 | Audit-only winner autopsy components | CLOSED | YES | Audit experiment |
| #7 | V11.4 minimal +1 PRESSURE_FADE ranking bonus | CLOSED | YES | V11.4 line; do not silently import into V11.3 baseline |
| #8 | Audit-only forward target-label generation fix | OPEN | NO | Research/audit-only |
| #9 | Isolated Step 3 RSS fallback diagnostics | CLOSED | YES | Bounded source fallback |
| #10 | Run #93 event-count reporting and bounded GDELT queries | OPEN | NO | Event-count/query correction |
| #11 | Run #145 Factor Registry source audit and bounded repair | OPEN | NO | Large Factor Registry workstream; blockers remain |
| #13 | Factor Registry same-snapshot reconciliation | OPEN | NO | Reconciliation branch; not full 35/35 proof |
| #14 | Macro evidence snapshot v2 repair | CLOSED | NO | Superseded/closed unmerged iteration; do not count as accepted delivery |
| #15 | Macro evidence snapshot v2 fail-closed hash/provenance repair | OPEN | NO | Follow-on repair branch |
| #16 | 41-vintage MoSPI IIP audit | CLOSED | NO | Superseded/closed unmerged iteration |
| #17 | 41-vintage MoSPI IIP ingestion/revision audit | OPEN | NO | Current isolated IIP audit line |
| #18 | Inert NSE-57 workflow_dispatch stub | CLOSED | YES | Workflow registration only |
| #19 | NSE security identity reconciliation for stale candidates | OPEN | NO | Research-only |
| #20 | Global Capital Rotation & Relative-Attraction Overlay V1 | OPEN | NO | 140 commits / 51 files / +3,879 additions at audit; research-only |
| #21 | Isolated IIP 41-vintage audit: truthful timestamps/scoped gate | OPEN | NO | Preserve evidence; no production merge |
| #22 | Provisional April-2026 NIC-2025 IIP PDF cross-check ledger | OPEN | NO | First-release evidence line |
| #23 | Bounded QA for April-2026 IIP PDF first-release evidence | OPEN | NO | 23/23 cross-check recorded in continuity ledger; PR still open |
| #24 | Extract/independently validate 463 NIC-2025 concordance rows | OPEN | NO | Separate taxonomy/classification workstream |
| #25 | IIP 2022-23 public weights/item-level access boundary | OPEN | NO | Access boundary audit |
| #26 | Delivery-field completeness without rounding away missing rows | OPEN | NO | QA/reporting correction |
| #27 | Issue: inconsistent missing-delivery evidence in historical features | OPEN | N/A | Requires explicit UNKNOWN policy; no silent neutral/zero substitution |
| #28 | QA-only delivery missingness policy regression tests | OPEN | NO | Regression test work |
| #29 | Issue: V11.3 scoring provenance/shared V11.4 dependencies | OPEN | N/A | Feature/calibration lineage unresolved |
| #30 | QA contract for V11.3 calibration artifact failure modes | OPEN | NO | QA contract |
| #31 | Provenance-safe Federal Reserve H.10 raw ingestion | OPEN | NO | Raw ingestion line; PR metadata reports open |
| #32 | Exact-origin validation in Fed H.10 collector | OPEN | NO | Collector validation repair |
| #33 | Verified Fed H.10 Library snapshots and QA | OPEN | NO | Artifact snapshot and QA record |
| #34 | IMF BOP DSD acquisition workflow registration | OPEN | NO | Workflow registration does not equal BOP observation extraction |
| #35 | Fail-closed NSE full-delivery date-integrity guard | OPEN | NO | Guard implementation |
| #36 | NSE date integrity across cached and legacy paths | OPEN | NO | Guard implementation |
| #37 | NSE raw archive with date-verified SHA-256 manifest | OPEN | NO | Raw archive/manifest branch |
| #38 | H+3/H+5 forward outcome maturity and ledger guards | OPEN | NO | Research-only outcome maturity correction |

PR state caution:
- GitHub returned several open PRs with non-null test/merge candidate SHAs. The audit uses the explicit `merged` boolean and PR state, not the presence of a merge candidate SHA.
- PRs #14 and #16 were CLOSED but NOT MERGED. They are not accepted production/mainline changes.
- Issues #12, #27 and #29 are tracked separately from PR inventory.
- A PR's commit count, changed-file count or added-line count is not an acceptance score.

## 2. Project architecture and invariants preserved
The research program's stated objective is a data-driven Indian equities 1–3 day swing-trading research/scanner system, with an evidence-backed final pre-market shortlist. The system architecture and non-negotiable boundaries recorded across prior project history are:
- CORE-672 = 56 diagnostic steps × 12 filters.
- Engines A–E: (A) 20% Pre-Explosion/Lead-Time; (B) 10% Event/Repricing; (C) 5% Ignition/Continuation; (D) Stress-Divergence/Resilience; (E) Cross-Engine Opportunity Preservation/Anti-Miss.
- IPO-PLX V2.0 remains a separate IPO research engine.
- Production Selector unchanged; RANKING_SCORE unchanged; +1 PRESSURE_FADE unchanged for the protected V11.3 baseline; CORE-672 unchanged; Engines A–E unchanged.
- V11.4 experimental PRs (#1–#7) are separate historical work. Their merged state does not authorize importing V11.4 changes into V11.3.
- Research-only branches/PRs are not production integration. No PR merge or production change without explicit user approval.
- UNKNOWN is neither PASS nor FAIL. Missing/stale data is not converted to zero, neutral, or success unless an explicit, approved feature policy says so.
- No synthetic data, fabricated timestamps, invented hashes, forward-fill across missing observations, silent series/classification splicing, or unverified source promotion.
- Research spend ₹0; free official/primary sources only; no paid APIs or subscriptions; no external contact.
- Prefer bounded CI jobs under 10 minutes, with small incremental tasks where possible.
- No automatic trade trigger, buy/sell instruction, or unvalidated stock ranking from the Global Capital Rotation overlay.

## 3. Total activity timeline — earliest auditable repository activity to 2026-11-17

### Phase A — 2026-10-05 to 2026-10-11: early V11.4 calibration and audit experiments
Verified PR history:
- PRs #1–#7 were opened and merged between 05-Oct and 07-Oct. They cover stable probability calibration/winner recovery, separation/rare-event specialist, winner interactions/transition evidence, feature ablation, a minimal V11.4 ranking revision, winner autopsy components and a V11.4 +1 PRESSURE_FADE bonus.
- PR #8 opened 11-Oct for an audit-only forward target-label generation fix; remained open at the 17-Nov PR inventory.
Interpretation:
- This phase is evidence of V11.4 experimental work. It must not be conflated with the protected V11.3 production baseline.
- The exact first-ever project activity before 05-Oct is not reconstructed by this repository PR inventory.

### Phase B — 2026-10-22 to 2026-11-02: source diagnostics, Macro-Geo and Factor Registry
Verified PR/issue history:
- PR #9 (22-Oct) merged isolated Step 3 RSS fallback diagnostics.
- PR #10 (24-Oct) opened to correct Run #93 event-count reporting and bound GDELT queries; remained open.
- PR #11 (26-Oct) opened for Run #145 Factor Registry source audit and bounded repair; remained open.
- PR #13 (30-Oct) opened for Factor Registry same-snapshot reconciliation; remained open.
- Issue #12 (29-Oct) consolidated P0/Factor Registry, provenance, event-study and rolling-backtest parity remediation.
Evidence in Issue #12 at its recorded snapshot:
- Macro-Geo P0 source coverage 7/8; Corporate Events blocked.
- Factor Registry 0/35 groups fully available.
- Event study 53 events: 32 eligible, 21 pending.
- Historical regime anchors 9/11 with windows; 2 missing.
- Crude-oil source/provenance mismatch (EIA Brent spot vs Yahoo Brent futures) required reconciliation.
- Rolling backtest used explicit A/B/C/D/E proxy rules, not confirmed production V11.3 selector; D was relatively strongest but its H+5 net result was still negative. This is diagnostic proxy evidence, not production validation.
- One missing 2026-10-20 session was identified; ambiguous next-session executions must remain excluded.
These figures are dated issue evidence, not asserted as current counts on 17-Nov without a fresh run.

### Phase C — 2026-11-03 to 2026-11-10: IIP vintages, NIC concordance, delivery QA, macro evidence
Verified PR history:
- PR #14 (03-Nov) macro evidence snapshot v2 repair iteration closed unmerged; PR #15 follow-on fail-closed hash/provenance repair opened and remained open.
- PR #16 (03-Nov) 41-vintage IIP audit iteration closed unmerged; PR #17 follow-on remained open.
- PR #18 (04-Nov) merged an inert NSE-57 workflow_dispatch stub; workflow registration only.
- PR #19 (05-Nov) opened research-only NSE security identity reconciliation; remained open.
- PR #20 (07-Nov) opened Global Capital Rotation & Relative-Attraction Overlay V1; remained open.
- PRs #21–#26 and #28 were opened for IIP vintage evidence, April-2026 IIP first-release checks, 463 NIC-2025 concordance rows, public weights/access boundaries, delivery completeness and missingness QA.
- PR #23's continuity evidence reports Run #46 / ID 42491849056 SUCCESS; 23/23 named NIC-2 manufacturing rows matched later PIB Statement IV releases. Portal workbook iip_62.xlsx: 90,294 bytes; SHA-256 31ab1a00ea14b90a21086d3c618cd65456e45b3a02b4ae85251ee1dac9fb189e. First-release WPI PDF raw SHA remained pending.
- PR #21/17 IIP audit evidence: Run #251 / ID 42501079840 SUCCESS after correcting a false duplicate-key validator rule; Run #254 / ID 42507902637 SUCCESS with supplementary PIB snapshot ingestion and independent validator. 116,740 observations; 1,058 snapshot differences; 0 integrity errors. Artifact ID 13628033276; ZIP SHA-256 a988e47f6679def45d3fa3316e5d3207040047a847cd19410458a40db1814f3b. 69 supplementary rows (3 periods × 23 NIC codes) matched 69/69 against the later MoSPI PDF statement; these are later snapshots, not restored original first-release vintages.
- IIP source boundary was clarified: old 2011-12/NIC-2008 series ends March-2026; new 2022-23/NIC-2025 series begins April-2026. No splicing. A legacy April-2026 old-series 404 is NOT_APPLICABLE absent evidence the old-series release existed.
- Current-series correction: June-2026 first release used WPI deflator and was superseded on 29-Jun-2026 by Output-PPI-based series. Preserve first-release vintage separately; current pipeline uses the Output-PPI series, as documented in IIP transition crosswalk.
- Issue #27 records a delivery-missingness inconsistency: one feature treated NaN comparison as zero-like while another filled missing DELIV_GAP with zero/neutral. Policy decision is required before code/metrics change.
- Issue #29 records a V11.3/V11.4 dependency-lineage concern: V11.3 imports feature and tomorrow-feature functions from a V11.4-labelled walk-forward module and consumes a behavioral DNA library generated there. Full semantic equivalence and per-run artifact lineage remain unresolved.
- PR #30 calibration artifact failure-mode QA contract opened 10-Nov and remained open.

### Phase D — 2026-11-11 to 2026-11-17: FX panels, NSE archive integrity, global capital overlay and taxonomy
Verified PR history:
- PR #31–#33 cover provenance-safe Fed H.10 raw ingestion, exact-origin validation, and verified H.10 Library snapshots/QA.
- PR #34 registers IMF BOP DSD acquisition workflow; workflow registration is not proof of IMF BOP transaction observations.
- PRs #35–#38 add fail-closed NSE date-integrity guards, raw archive SHA-256 retention and H+3/H+5 outcome-maturity guards.
- PR #20 Global Capital Rotation branch grew to 140 commits / 51 files / +3,879 additions at the latest PR metadata check; it remained OPEN / UNMERGED.

#### FX / Fed H.10 / FRED
- H.10 workflow Run ID 43276577238 SUCCESS; artifact ID 13970661965; ZIP SHA-256 a6f6af42226ed689ceba8e9c2d843867d82e9aa8f9a7761022c86bd719ef3691.
- 26/26 raw series hashes verified; 304,510 dated rows; 291,831 numeric values; 12,679 missing markers retained; date union 1971-01-04 to 2026-11-06.
- Exact 200-session NSE calendar join PASS; point-in-time vintage availability still UNKNOWN/PENDING.
- DTWEXBGS is the Fed Nominal Broad U.S. Dollar Index, not ICE DXY. 15-Nov 20-interval result +0.3568637816% over 2026-10-08 to 2026-11-06 is a research-only FX index calculation, not a flow observation.
- 17-Nov H.10/FRED five-date preview match: 5/5 exact, including the 11-Nov missing observation.
- Federal Reserve methodology explains 2019 re-indexing to Jan-2006=100, Broad factor 1.014163. H.10 Preview unit metadata still conflicts/stale; preserve source metadata discrepancy.
- Official DDP/FRED crosswalk CSV route and schema were found, but exact row mapping was not extracted. H.10 XML ZIP and public FRED CSV full-history routes were identified; raw bytes failed to download in the available runtime. No full-history reconciliation or new SHA was produced.

#### FBIL / RBI FX
- 11-Nov FBIL endpoint: HTTP 200 for 15–16-Oct-2026; 14 records, 7 currency products × 2 dates.
- Raw response SHA-256 aeec99630a30d4b5961755c35e05b1e795dec1c39a373e48d95eca5edd165e27; workflow Run ID 42983033561; artifact ID 13837574133; artifact ZIP SHA-256 48340a456b11aa8b3cc7e6133d00dcd92794b08c8460cbe65742cc25986c56f4.
- Eight USD/GBP/EUR/JPY overlapping cells matched public displays (8/8).
- Recent 05–11-Nov requests repeatedly returned empty arrays; root cause UNKNOWN. No outage claim, no synthetic fill.
- Full history, recent live coverage and daily collector remain NOT_DONE.

#### India FPI / DII
- Existing CDSL snapshot through 09-Nov: six daily equity observations; MTD +₹53,738.78 crore and YTD -₹2,41,407.13 crore.
- 17-Nov bounded CDSL semantics checkpoint (commit 66271d77c685f348943af804945ec1e9e3f65684; file verified, blob SHA eee13b32ce28e0f16a7aa608a23da712e5d0d715): 16-Nov displayed FPI categories subtotal +₹4,845.93 crore; separately displayed Mutual Funds -₹18.74 crore; page total +₹4,827.19 crore. Page total is not pure FPI.
- NSE-only and combined NSE+BSE+MSEI CSV scopes remain separate. NSE FPI is provisional pending custodian confirmation; DII classification is based on Trading Member codes/client categories.
- CDSL raw archive byte/hash capture, NSE raw CSV byte/hash acquisition, and a matched lag-aware daily FPI/DII panel remain NOT_DONE.

#### IMF BOP / Treasury TIC / global EM flow
- IMF BOP DSD V2.6.0 and metadata-first extraction contract identified. IMF PIP/CPIS positions are not BOP transaction flows. No country-level BOP observation panel or defensible global EM aggregate extracted.
- Treasury TIC Securities A added as a candidate monthly transaction source, but it is US-centric and has a post-Feb-2023 SLT structural break. Raw country files, full schema QA, India row validation and point-in-time release archive remain pending.
- India FPI cannot stand in for global EM flow; neither TIC nor a US dollar index proves direct US-to-India capital transfer.

#### Taxonomy / industry / sector-to-stock
- 17-Nov NSE March-2022, NSE July-2023 and BSE classification PDFs were inspected for a bounded checkpoint.
- Observed discrepancy: NSE 2022 2/3 Wheelers definition included bicycles; July-2023 excludes bicycles/tricycles and separately lists Cycles. This is a scope reassignment signal, not a simple rename.
- Full row extraction, bidirectional code diff, definition-level semantic diff, issuer mapping, historical raw PDF hashes and parser integration remain NOT_DONE.
- Sector-to-stock exposure and capital transmission validation remain NOT_DONE.

#### NSE collector / historical archive / backtest integrity
- Project memory records a 200-session NSE backfill target, later archive growth to 317 sessions (reported 12-Nov); do not equate session count with complete schema/source coverage.
- PR #35/#36: fail-closed date-integrity guards across delivery/cache/legacy paths.
- PR #37: raw archive retention with date-verified SHA-256 manifest.
- PR #38: H+3/H+5 forward outcome maturity and ledger guards; research-only.
- H+3/H+5 matured observation policy: minimum 50 fully matured observations per State; below threshold remains UNKNOWN/uncalibrated. Do not lower to 30 or count immature windows.
- Full rolling production-parity backtest, target-specific cost-adjusted precision/recall, drawdown, false-positive/missed-winner analysis and matured event study remain incomplete.

## 4. Consolidated workstream status matrix (as of audit cutoff)
| Workstream | Evidence-backed state | Boundary / remaining work |
|---|---|---|
| V11.3 architecture / CORE-672 / Engines A-E | SPECIFIED / PROTECTED | Full project acceptance remains separate |
| V11.4 experiment history | Several early PRs merged | Must not silently alter V11.3 baseline |
| NSE collector/backfill | Archive and date-integrity work in progress; 317 sessions reported in project history | Full source coverage, schema completeness, raw archive manifest and reproducibility still require per-artifact acceptance |
| Security identity reconciliation | PR #19 OPEN | Full stale-candidate closure not established |
| Macro-Geo P0 / Corporate Events | Historical issue evidence shows 7/8 P0; Corporate Events BLOCKED | Fresh P0 audit needed; do not reuse stale 29-Oct counts as current |
| Factor Registry | Historically 0/35 fully available at Issue #12 snapshot; repair PRs #11/#13 OPEN | Current complete 35/35 audit not verified |
| IIP 41-vintage audit | Run #251 and #254 recorded SUCCESS with validator evidence | Original vintage semantics vs later snapshots remain distinct; PRs open |
| NIC-2025 concordance | PR #24 for 463 rows OPEN | Exact issuer-level mapping / transition acceptance not claimed |
| Delivery missingness policy | Issue #27 OPEN; regression PR #28 OPEN | User-approved UNKNOWN policy and downstream replay required |
| V11.3/V11.4 dependency provenance | Issue #29 OPEN | Version pinning and per-run calibration lineage unresolved |
| Calibration artifact QA | PR #30 OPEN | Complete acceptance not established |
| Fed H.10 raw/derived panel | Artifact and hashes PASS | PIT vintage archive and FRED full-history reconciliation pending |
| FBIL FX sample | 14-row historical sample PASS | Recent data empty; full history and scheduler NOT_DONE |
| IMF BOP | DSD/spec/workflow route identified | Actual portfolio transactions and EM aggregate NOT_DONE |
| Treasury TIC | Candidate source/structural break documented | Raw data and release vintage QA NOT_DONE |
| India FPI | CDSL bounded displayed-source checks PASS | Full raw daily archive and historical panel NOT_DONE |
| India DII | Official NSE scopes/semantics documented | Raw CSV and daily panel NOT_DONE |
| Global EM flow | UNKNOWN / NOT_DONE | Do not infer from India FPI or holdings |
| Relative attraction / India vs World | NOT_DONE | Synchronized total-return panel and matched calendars required |
| Sector-to-stock bridge | NOT_DONE | Issuer exposures, sector constituents and lagged transmission required |
| Matured event study / predictive validation | NOT_DONE / PARTIAL historical evidence | Mature windows, sample size, costs, uncertainty and selector parity required |
| Production integration | NOT_AUTHORIZED | No approval to merge PR #20 or change protected selector |

## 5. Previously recorded quantitative evidence — do not mix unlike denominators
- CORE-672 architecture: 56 × 12 = 672 diagnostics (design invariant, not a completion percentage).
- NSE archive: 317 sessions reported by 12-Nov in project history (session count, not complete acceptance).
- IIP: 116,740 parsed observations; 1,058 snapshot differences; 0 integrity errors in Run #254 validator; 69 supplementary later-snapshot values matched 69/69.
- H.10: 26 series, 304,510 dated rows, 291,831 numeric values, 12,679 missing markers retained.
- FBIL: 14 rows; 8/8 cross-display overlapping cells matched.
- CDSL: 16-Nov displayed arithmetic FPI subtotal +₹4,845.93 crore; MF -₹18.74 crore; total +₹4,827.19 crore.
- Factor Registry: 0/35 fully available in dated Issue #12 evidence snapshot; not revalidated as current on 17-Nov.
- Macro-Geo P0: 7/8 in dated Issue #12 evidence snapshot; not revalidated as current on 17-Nov.
- Historical regime anchors: 9/11 in dated Issue #12 snapshot; not revalidated as current.
- Event study: 53 events, 32 eligible, 21 pending in dated Issue #12 snapshot; not current maturity count.
- Global Capital Rotation: 62.5% (5/8) was the last recorded overlay figure on 12-Nov. On 17-Nov no full eight-gate re-audit was performed. Current overall overlay percentage = NOT_RECALCULATED / NOT_VERIFIED. Do not present 62.5% as a freshly measured current rate.
- Whole V11.3 project overall percentage: NOT_CALCULABLE until all workstreams, acceptance weights and current evidence are reconciled.

## 6. Rejected interpretations and known failed/closed iterations
1. PR #14 and PR #16 were closed unmerged; do not count their branch iterations as accepted mainline delivery.
2. PR #5/#7 are V11.4 experimental changes; do not silently treat them as V11.3 production changes.
3. IMF PIP/CPIS holdings/positions are not BOP transactions/flows.
4. Fed DTWEXBGS / H.10 Broad Dollar Index is not ICE DXY.
5. India daily FPI is not a global EM aggregate and does not prove source/destination capital transfer.
6. CDSL page Total includes a separately displayed Mutual Funds category; do not label it pure FPI.
7. NSE-only and combined NSE+BSE+MSEI flows are distinct source scopes; do not splice or average.
8. Treasury TIC is US-centric; post-Feb-2023 SLT has a structural break; it does not prove direct India FPI.
9. EIA Brent spot, FRED DCOILBRENTEU and Yahoo Brent futures are not interchangeable.
10. An empty FBIL response is EMPTY_ARRAY / UNKNOWN, not a confirmed outage and not zero flow.
11. A successful GitHub Actions workflow is not proof that the research Hard Gate passed.
12. A later PIB snapshot is not an original MoSPI first-release vintage.
13. The old 2011-12/NIC-2008 April-2026 file expectation is NOT_APPLICABLE unless an official catalogue record proves such a release existed.
14. A non-null PR merge-candidate SHA is not proof a PR is merged.
15. Commits, changed files, lines added, branch count and document count are not research acceptance percentages.

## 7. Current exact next actions — ordered to avoid repetition
1. **Reconcile the actual repository evidence index:** enumerate all current PASS artifacts, run IDs, artifact IDs, SHA-256s and source manifests across the 317-session NSE archive, H.10, IIP and macro workflows. Do not re-run successful audits without new inputs/code.
2. **Finish India FPI/DII raw acquisition:** archive official CDSL daily/archive bytes and both NSE CSV scopes, with exact URLs, retrieval/publication timestamps, byte length, SHA-256, schema QA and duplicate/date checks. Do not invent an NSE endpoint.
3. **Execute BCB vintage extraction script** against the pinned 202601/202603 workbooks; verify that the referenced raw files exist, run it, inspect output and independently validate row semantics/hashes. Script presence alone is NOT_DONE.
4. **Build matched lag-aware India panel:** CDSL FPI categories separate; NSE-only DII separate from combined NSE+BSE+MSEI DII; align actual trade/reporting dates and preserve provisional status. No fill-forward.
5. **IMF BOP transaction extraction:** acquire DSD/codelists and actual observation payload through a documented free route; declare country membership, weights, instruments, sign conventions, coverage and missing reporters before any EM aggregate.
6. **Complete H.10/FRED migration audit:** obtain raw XML/CSV and official crosswalk CSV bytes; verify exact mapping; full daily date/value/status comparison; pre/post-2019 methodology bridge; revision-vintage archive. Keep H.10 canonical until all gates pass.
7. **Refresh P0 / Factor Registry / corporate-events status** using current artifacts; reconcile issue #12 and PRs #10/#11/#13 without repeating stale source discovery.
8. **Close IIP transition and taxonomy diffs:** keep 2011-12/NIC-2008 and 2022-23/NIC-2025 separate; finish full code-level NSE/BSE classification inventory and issuer mapping only after source archive/hash QA.
9. **Resolve delivery UNKNOWN and calibration lineage:** explicit missingness policy; version-pin V11.3 feature and behavioral-DNA producer dependencies; record artifact/run/commit/digest for every scoring replay.
10. **Matured, production-parity backtest:** use frozen V11.3 selector, correct session calendar and next-session entry rules, transaction costs, target-specific H+1/H+3/H+5 outcomes, matured-only labels, state minimum 50, precision/recall, false positives, missed winners, drawdown/adverse excursion, benchmark and uncertainty. Keep proxy results separate.
11. **Reconcile final Hard Gate and research paper:** no PASS until every mandatory gate is supported by fresh, reproducible evidence. Keep production integration unauthorized absent explicit approval.

## 8. Reporting contract for all future continuation chapters
Before starting a new chapter, provide a concise Progress Log with:
- Completed Tasks (with exact evidence);
- Rejected / Excluded list and reason;
- BLOCKED / UNKNOWN / NOT_DONE items;
- exact next action(s), preferably one bounded task;
- workstream completion percentages only where a defined denominator exists;
- overall percentage only after the entire acceptance matrix is reconciled.

For every new work unit, append:
- date/time and timezone;
- branch, commit SHA and exact file path;
- workflow Run ID / job ID / Artifact ID if applicable;
- raw source URL, publication date, retrieval timestamp, byte length, SHA-256;
- validation counts and test result;
- explicit PASS / FAIL / BLOCKED / UNKNOWN / NOT_DONE;
- what was not tested;
- protected invariants confirmation.

Do not repeat work already marked PASS unless a new input, code change, source revision or explicit independent verification requirement justifies it.

## 9. Source documents and audit trail
- `docs/PRECISION_WIRES_V11_3_CONTINUITY_ACCEPTANCE_LEDGER.md` (last reconciled 2026-11-08; historical baseline, not current master by itself).
- `docs/GLOBAL_CAPITAL_ROTATION_CONTINUITY_LEDGER_20261117.md` (overlay continuity, 17-Nov).
- `docs/GLOBAL_CAPITAL_ROTATION_15_DAY_ACTIVITY_AUDIT_20261117.md` (15-day overlay audit, 17-Nov).
- `docs/GLOBAL_CAPITAL_ROTATION_OVERLAY_V1.md` (overlay design).
- `docs/GLOBAL_CAPITAL_ROTATION_OFFICIAL_SOURCE_REGISTER_V1.md` (official source register).
- `docs/IMF_BOP_PORTFOLIO_FLOW_EXTRACTION_SPEC_V1.md` (IMF flow extraction contract).
- `docs/NSE_FII_DII_DAILY_ACTIVITY_INGESTION_CONTRACT_V1.md` (NSE scope/ingestion contract).
- `docs/GLOBAL_CAPITAL_ROTATION_INDIA_FPI_DII_SEMANTICS_CHECKPOINT_20261117.md` (CDSL/NSE semantics).
- `docs/GLOBAL_CAPITAL_ROTATION_H10_FRED_FULL_HISTORY_RETRIEVAL_ROUTE_20261117.md` and `docs/GLOBAL_CAPITAL_ROTATION_H10_FRED_BYTE_CAPTURE_ATTEMPT_20261117.md` (H.10/FRED routes and failed byte capture).
- `docs/NSE_BSE_TAXONOMY_INVENTORY_EXTRACTION_CHECKPOINT_20261117.md` (classification checkpoint).
- GitHub Issue #12 (consolidated remediation gate), #27 (delivery missingness), #29 (V11.3/V11.4 dependency provenance).
- PR #1–#38 inventory above; #12/#27/#29 are issue numbers, not PRs.

## 10. Final audit decision
- TOTAL ACTIVITY AUDIT: RECORDED in this master document.
- Repository PR history: reviewed from earliest auditable PR dated 2026-10-05 through 2026-11-17.
- Historical chat/page/file/run/artifact coverage: PARTIAL; exact completeness not provable from repository PR inventory alone.
- Current full-project acceptance: NOT_RECONCILED.
- Current overall V11.3 percentage: NOT_CALCULABLE.
- Global Capital Rotation latest defensible overall percentage: NOT_RECALCULATED; 62.5% remains only the last recorded 2026-11-12 figure.
- PR #20 production/merge status: OPEN / UNMERGED.
- Production integration: NOT_AUTHORIZED.
- All protected invariants remain in force.
