# Global Capital Rotation & Relative-Attraction Overlay — Continuity Ledger
Checkpoint: 2026-11-17 (Asia/Kolkata)
Repository: duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR
Research branch: research/global-capital-rotation-overlay-v1
Parent work: PR #20, Research-only Global Capital Rotation & Relative-Attraction Overlay V1 (OPEN / UNMERGED).
Status rule: preserve all earlier evidence; no production acceptance inferred from scoped PASS results.

## 1. Purpose and invariants
Build a provenance-backed research overlay for global capital supply, India capital capture, relative attraction, sector transmission and company-level exposure. It must emit source-grounded categorical diagnostics only; no composite stock score, ranking, buy/sell instruction or automatic trade trigger.
Protected: Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A-E and project Hard Gate remain unchanged. Research spend ₹0; official/free sources only; no paid APIs, synthetic observations, fabricated timestamps, forward-fill, PR merge or production integration without explicit approval.

## 2. Work completed / preserved evidence
- PR #20 exists and remains OPEN / UNMERGED. Overlay schema, provenance-aware parser, categorical diagnostics, staleness handling and bounded QA were implemented in its research branch.
- Official source register: docs/GLOBAL_CAPITAL_ROTATION_OFFICIAL_SOURCE_REGISTER_V1.md. It records IMF BOP (flow) vs PIP/CPIS (position), CDSL/NSDL FPI, NSE/SEBI DII, Fed H.10, Treasury/FRED yields, RBI FX, EIA Brent, Cboe VIX, NSE indices, policy sources and sector/company disclosures.
- Overlay design: docs/GLOBAL_CAPITAL_ROTATION_OVERLAY_V1.md. Five-stage transmission chain: global capital supply; India capture; relative attraction; sector transmission; stock bridge.
- Official source access contract: docs/GLOBAL_CAPITAL_ROTATION_OFFICIAL_SOURCE_ACCESS_CONTRACT_20261111.md. It distinguishes positions, transactions, FX, price indices and total-return indices; contains the Treasury TIC Securities A source addition and its February-2023 structural break constraints.
- Fed H.10 daily historical panel: workflow Run ID 43276577238 SUCCESS; artifact ID 13970661965; ZIP SHA-256 a6f6af42226ed689ceba8e9c2d843867d82e9aa8f9a7761022c86bd719ef3691. 26/26 raw series hashes verified; 304,510 dated rows; 291,831 numeric observations; 12,679 missing markers preserved; date union 1971-01-04 to 2026-11-06. Exact 200-session NSE join PASS; point-in-time vintage availability remains UNKNOWN/PENDING.
- H.10 diagnostic independently rechecked 2026-11-15: DTWEXBGS 20-interval change +0.3568637816% over valid observations 2026-10-08 to 2026-11-06. This is the Fed Nominal Broad U.S. Dollar Index, not ICE DXY. It must populate fed_broad_usd_change_pct_20d, never dxy_change_pct_20d.
- CDSL FPI evidence snapshot in PR #20: six daily equity observations through 2026-11-09; MTD +₹53,738.78 crore and 2026 YTD -₹2,41,407.13 crore. Positive short-window reversal does not negate YTD outflow or prove US-to-India transfer.
- CDSL FPI categories remain separate: Equity, Debt-General, Debt-VRR, Debt-FAR, Hybrid. Mutual Funds are a separately displayed category and must not be silently folded into FPI.
- India FPI/DII and global EM flow are different populations. Daily India FPI cannot establish broad EM rotation.
- IMF BOP extraction specification: docs/IMF_BOP_PORTFOLIO_FLOW_EXTRACTION_SPEC_V1.md. BOP is annual/quarterly; DSD BOP 2.6.0 identified, but exact DSD/codelist parse/archive, observation extraction, country panel, versioned EM membership and EM aggregate remain UNKNOWN/NOT DONE. PIP/CPIS positions must never be substituted for BOP transactions.
- Treasury TIC Securities A was added as a monthly transaction/flow candidate. Its post-February-2023 SLT regime has a structural break and changed country attribution; raw country files, SHA-256, vintage reconstruction and India-row QA remain pending. It is U.S.-centric and cannot prove direct India FPI.
- NSE daily FII/FPI & DII ingestion contract: docs/NSE_FII_DII_DAILY_ACTIVITY_INGESTION_CONTRACT_V1.md. NSE-only and combined NSE+BSE+MSEI series are distinct; raw bytes, exact CSV URLs, SHA-256 and parsed daily DII panel were not acquired in the prior audit.

## 3A. 2026-11-17 fresh India FPI/DII source checkpoint
- File: docs/GLOBAL_CAPITAL_ROTATION_INDIA_FPI_DII_SOURCE_CHECKPOINT_20261117.md
- Commit: e766e11df9b9bf11cd632db55f702005b6c058d8
- Post-commit fetch verified; blob SHA: 91156ae69c8cb180698475eb865bca8cd0d0e335; 54 lines.
- CDSL 17-Nov displayed-page arithmetic: FPI category subtotal +₹2,436.14 crore; separately displayed MF +₹37.68 crore; page total +₹2,473.82 crore. Bounded display/arithmetic PASS only.
- NSE official page exposes two distinct CSV download controls (NSE-only and NSE+BSE+MSEI); exact download URLs/raw bytes were not available in this check. Both CSV raw acquisition and SHA-256 remain NOT_DONE.
- No change to prior gate status or overall overlay percentage; this is not a full overlay gate.

## 3B. 2026-11-17 official-source correction (supersedes earlier draft)
- The first draft of `GLOBAL_CAPITAL_ROTATION_INDIA_FPI_DII_SOURCE_CHECKPOINT_20261117.md` contained unsupported 17-Nov CDSL values. Those figures are withdrawn and must not be used.
- Corrected file commit: 58b3995f3d86cfc4b2836d5614f2fdec1a306e0f.
- Fresh CDSL official page showed 16-Nov-2026 as latest visible investment reporting date: FPI category subtotal +₹4,845.93 crore; separately displayed MF -₹18.74 crore; page total +₹4,827.19 crore. Bounded displayed-page arithmetic only.
- Fresh NSE official page showed 13-Nov-2026: NSE-only FII/FPI +₹5,253.98 crore and DII -₹1,970.73 crore; combined NSE+BSE+MSEI FII/FPI +₹5,736.55 crore and DII -₹2,253.58 crore. Both provisional; scopes remain separate.
- CDSL raw bytes/hash, both NSE raw CSVs/hash, matched daily panel and IMF BOP transaction panel remain NOT_DONE.
- No new full overlay gate is accepted; overall percentage remains NOT_RECALCULATED.

## 3C. 2026-11-17 IMF BOP aggregate candidate checkpoint
- New file: docs/GLOBAL_CAPITAL_ROTATION_IMF_BOP_AGGREGATE_SOURCE_CHECKPOINT_20261117.md
- Checkpoint commit: 5842a401e8264ce393cb338b8d2699a6283af4ed.
- IMF BOP extraction spec appended with BOP_AGG findings; commit: c43722774b2e48636ec57b423c2ae3cbb7308f10.
- Official IMF BOP_AGG is an annual November BPM6 publication. Its World/country-group aggregates combine reported data with estimates for nonreporting economies; EMDE grouping is IMF-defined and not MSCI EM. Use only financial-account portfolio-investment transactions, never IIP positions.
- Source discovery/methodology assessment PASS only. Exact portfolio-investment series mapping and raw workbook/API payload, retrieval timestamp, byte count, SHA-256, unit/sign/vintage QA remain NOT_DONE.
- No value admitted to em_portfolio_flow_usd_bn; no full overlay gate or percentage advanced.

## 3. 2026-11-17 new checkpoint
Created docs/GLOBAL_CAPITAL_ROTATION_INDIA_FPI_DII_SEMANTICS_CHECKPOINT_20261117.md.
Commit: 66271d77c685f348943af804945ec1e9e3f65684.
Post-commit fetch verified the exact file at branch head path; blob SHA: eee13b32ce28e0f16a7aa608a23da712e5d0d715; 84 lines.
Official CDSL daily page displayed reporting date 16-NOV-2026. Displayed values (INR crore): Equity +5,564.90; Debt-General +389.47; Debt-VRR +51.60; Debt-FAR -1,163.67; Hybrid +3.63; separately displayed Mutual Funds -18.74; page Total +4,827.19.
Arithmetic reconciles: FPI categories subtotal = +4,845.93; adding separately displayed Mutual Funds -18.74 = page Total +4,827.19. Thus the page Total is not pure FPI net investment.
CDSL page says the figures are compiled from custodian reports received by depositories on 16-Nov and represent trades on and up to previous trading day(s); reporting date is not an intraday execution timestamp.
NSE page distinguishes NSE-only and combined NSE+BSE+MSEI Capital Market Segment downloads. It says FII/FPI activity is based on PANs provided by NSDL and provisional subject to custodial confirmation/modifications; DII uses Trading Member trading codes/client-category classifications. NSE sample date surfaced by the page was 21-Aug-2026, not a matched 16-Nov observation.
SEBI FPI curation page cross-checks official NSDL/CDSL daily, monthly and archive routes; this is FPI source routing, not a DII dataset.
New checkpoint is SOURCE SEMANTICS + DISPLAYED VALUE ARITHMETIC PASS only. It is not raw-byte ingestion, not SHA-256 archive, not matched daily panel and not overlay acceptance.

## 4. Current gap matrix
| Workstream | State |
|---|---|
| Overlay schema/parser/categorical QA | COMPLETE in PR #20 scope |
| Fed H.10 raw/derived panel archive and hash validation | PASS, with vintage caveat |
| CDSL daily FPI displayed-source arithmetic checkpoint | PASS, bounded |
| CDSL raw archive byte capture + immutable SHA-256 | NOT_DONE |
| NSE-only daily CSV raw acquisition | NOT_DONE |
| Combined NSE+BSE+MSEI daily CSV raw acquisition | NOT_DONE |
| Daily DII panel | NOT_DONE |
| IMF BOP DSD parse and country transactions | UNKNOWN / NOT_DONE |
| Versioned EM membership and valid aggregate | UNKNOWN / NOT_DONE |
| Treasury TIC raw country files and point-in-time releases | NOT_DONE |
| Matched synchronized macro/flow panel | NOT_DONE |
| India vs World/EM matched total-return study | NOT_DONE |
| Sector-to-stock exposure/transmission validation | NOT_DONE |
| Matured historical event study / predictive validation | NOT_DONE |
| Production integration | NOT_AUTHORIZED |

## 5. Prior overall progress and interpretation
PR #20 / overlay progress was last recorded as 62.5% (5/8) on 2026-11-12. This checkpoint does not recalculate the full eight-gate denominator and therefore preserves 62.5% as the last recorded project figure, not a newly measured current completion rate. The new bounded source-semantics checkpoint is not counted as a new full overlay gate.

## 6. Rejected / prohibited interpretations
- Do not call Fed DTWEXBGS ICE DXY.
- Do not treat IMF PIP/CPIS or FRB holdings as transactions/flows.
- Do not infer EM aggregate from partial country coverage or mixed currencies.
- Do not combine CDSL FPI categories with separately reported Mutual Funds.
- Do not treat NSE provisional FII/FPI or Trading Member-classified DII as custodian-final flows.
- Do not splice NSE-only and combined exchange scope.
- Do not infer US-to-India capital transfer from Indian FPI net buys.
- Do not forward-fill missing/stale observations or infer missing values as zero.
- Do not use a single positive MTD figure to override negative YTD.

## 7. Next highest-value action
Acquire and reconcile the official India daily flow source panel: (a) CDSL official daily/archive raw bytes with exact URL, retrieved_at, byte count, SHA-256 and reporting/coverage semantics; (b) NSE-only and combined NSE+BSE+MSEI CSVs via actual browser download or independently documented official export route; (c) strict schema/category/arithmetic/duplicate/calendar QA; (d) matched-date comparison preserving provisional vs custodian-compiled status and lag. Do not repeat the prior generic NSE link click or blocked direct-network attempt; do not invent the undocumented fiidiiTradeReact endpoint.

## 8. References
- PR #20: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/pull/20
- Official CDSL daily: https://www.cdslindia.com/eservices/publications/fiidaily
- Official CDSL archive: https://www.cdslindia.com/Publications/ArchiveDataAfter2009.aspx
- Official NSE FII/DII: https://www.nseindia.com/reports/fii-dii
- SEBI FPI directory: https://www.sebi.gov.in/curation/fpi.html
- Fed H.10 source: https://www.federalreserve.gov/datadownload/Choose.aspx?rel=H10
- IMF BOP dataset: https://data.imf.org/en/datasets/IMF.STA%3ABOP
- IMF SDMX Central: https://sdmxcentral.imf.org/data/datastructure.html
- Treasury TIC Securities A: https://home.treasury.gov/data/treasury-international-capital-tic-system-home-page/tic-forms-instructions/securities-a-us-transactions-with-foreign-residents-in-long-term-securities

## 7. Project-wide TOTAL ACTIVITY AUDIT pointer — 2026-11-17
- Master audit: `docs/PRECISION_WIRES_TOTAL_ACTIVITY_AUDIT_20261005_20261117.md`.
- Commit: `20fb54cdea4dbf15d89ee79330a7d1300832df6d`.
- File blob SHA verified after commit: `8debb302d2cab0696dbe21ed310d5e0742712311`; 297 lines.
- Covers earliest auditable repository PR activity (2026-10-05) through 2026-11-17; PR inventory #1–#38, dated workstream timeline, accepted evidence, blocked/unknown/not-done items, rejected interpretations, next actions and progress-reporting rules.
- Important boundary: 2026-10-05 is the earliest PR activity verified in the reviewed repository history, not proof of absolute project inception. Full chat/file/run/artifact reconstruction remains partial where direct evidence is not indexed.
- Current whole-project acceptance remains NOT_RECONCILED; overall V11.3 percentage NOT_CALCULABLE. Global Capital Rotation 62.5% is only the last recorded 2026-11-12 value, not a newly measured 2026-11-17 value.
- Preserve this master audit as the starting reference for future continuation chapters. Do not repeat PASS work without a new source, code, artifact, or explicit revalidation requirement.


## 3D. 2026-11-17 IMF BOP_AGG raw acquisition blocker
- New bounded attempt record: `docs/GLOBAL_CAPITAL_ROTATION_IMF_BOP_AGG_RAW_ACQUISITION_BLOCKER_20261117.md`.
- Commit: 6f8149629ebbd466b5c8677dfc10c524a389cf91; post-commit fetch verified blob SHA: 4934021f899ade9fd84535c44e9be889e1a8f543.
- Official BOP_AGG landing page exposes VIEW DATA and DOWNLOAD controls, but the available text extraction did not expose a concrete download URL/file. Following the official API link redirected to the IMF API developer portal sign-in page; anonymous API access was not demonstrated.
- No IMF raw bytes were acquired; byte count, retrieval timestamp, SHA-256, transaction-series mapping, units/sign/vintage QA remain NOT_DONE/UNKNOWN. Third-party mirror excluded under official-only constraint.
- This is a documented access blocker, not a source-data PASS. No value admitted to `em_portfolio_flow_usd_bn`; no overlay gate or percentage advanced; no production change.


## 3E. 2026-11-17 uploaded CSV byte and arithmetic audit
- New report: `docs/GLOBAL_CAPITAL_ROTATION_UPLOADED_FILE_BYTE_AUDIT_20261117.md`.
- Commit: 8cf077dbe9f538288f7a604ecba8f95956e80832; post-commit verification pending at time of ledger update.
- User Library copies of combined NSE+BSE+MSEI and NSE-only CSVs were byte-hashed (218 bytes each); buy-sell arithmetic exactly reconciles to reported net for DII and FII/FPI on 13-Nov-2026 in both scopes. Duplicate copies had identical hashes and are not additional observations.
- H.10 user Library slice: 813 bytes, SHA-256 c47d0f4b10e2cc5f541f91113d9c4d34bd9dfc72845b2313a99e68437ea7dad1; 10 daily observations 26-Oct through 06-Nov-2026; metadata identifies JRXWTFB_N.B as Nominal Broad Dollar Index, index Jan-1997=100. Endpoint changes over this 9-interval slice: broad +0.227048%, advanced +0.254686%, emerging market economies +0.200138%. Not a 20-session return and not ICE DXY.
- Supplied-file byte integrity and arithmetic/schema checks PASS only. Original official download URLs/retrieval timestamps/response provenance were not embedded or independently verified; official raw-download provenance remains NOT_VERIFIED. The H.10 slice is not enough for a 20-interval indicator. No panel, relative-attraction calculation, or gate advanced.


## 3F. 2026-11-17 CDSL official page refresh and H.10 freshness check
- New checkpoint: `docs/GLOBAL_CAPITAL_ROTATION_CDSL_H10_FRESHNESS_CHECKPOINT_20261117.md`.
- Commit: 42fd95bd337e23720a2344d9c1ff956b128116b4; post-commit fetch blob SHA: 1b944b4e34700394517d52773edc8214b459ef55.
- CDSL official daily page now displays reporting date 17-Nov-2026. Equity +₹5,107.61cr; Debt-General +₹137.23cr; Debt-VRR -₹2,379.67cr; Debt-FAR -₹424.29cr; Hybrid -₹4.74cr; five-category FPI subtotal +₹2,436.14cr. Mutual Funds separately +₹37.68cr; page total including MF +₹2,473.82cr. Arithmetic reconciles. CDSL says custodian reports received 17-Nov and trades conducted on/up to previous trading day(s); reporting date is not intraday execution time.
- CDSL official page snapshot VERIFIED and arithmetic PASS; raw response bytes/CSV URL/byte count/SHA-256 NOT_DONE.
- Fed H.10 official preview shows broad dollar index 122.6503 on 13-Nov, unit index Jan-1997=100; DDP review lists 5,445 observations from 2006-01-02 to 2026-11-13. Last 20-observation preview has ND on 11-Nov, leaving 19 numeric observations; 20-interval return requires 21 valid observations and remains NOT_DONE. H.10 is not ICE DXY.
- No IMF transaction panel, synchronized panel, relative-attraction calculation, event study or predictive validation completed. No production changes.
