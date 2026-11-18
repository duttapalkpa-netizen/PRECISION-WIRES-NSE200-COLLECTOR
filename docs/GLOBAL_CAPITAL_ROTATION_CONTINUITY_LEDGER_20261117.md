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

## 3G. 2026-11-17 CDSL reporting-date correction and H.10 DDP route change
- Correction report: docs/GLOBAL_CAPITAL_ROTATION_CDSL_DATE_CORRECTION_H10_DDP_ROUTE_20261117.md.
- Commit: 9d45eef7f3711b559c772e527966dbaf5cfe40ba; post-commit blob SHA: f5e1a180f7472b7f6dee624d0c9a058ccd3a15fa.
- Official CDSL Daily Trends page currently displays latest investment report 16-NOV-2026, not 17-Nov. The previously asserted 17-Nov figures (+₹5,107.61cr equity etc.) are withdrawn/rejected and must not be ingested. 16-Nov displayed FPI subtotal +₹4,845.93cr; MF separate -₹18.74cr; page total +₹4,827.19cr. Raw CDSL bytes/hashes remain NOT_DONE.
- Federal Reserve DDP Build Your Package was retired 12-Nov-2026. Official DDP offers last-10-observation CSV previews and 26.2MB all-G5/H10 XML; full raw historical XML not acquired in this audit. FRED API v2 full-history route requires account/API key; do not assume anonymous API access. H.10 20-interval return remains UNKNOWN.
- No synchronized panel, relative-attraction calculation, event study or predictive validation completed. No production changes.
## 3H. Direct H.10 XML endpoint and CDSL arithmetic clarification — 2026-11-17
- Official Fed XML download endpoint resolved from the DDP page control: https://www.federalreserve.gov/datadownload/Output.aspx?filetype=zip&rel=H10 (26.2 MB SDMX/ZIP). Browser text extraction rejected the binary content type and a separate container download attempt failed; no ZIP bytes were created. Route PINNED_OFFICIAL; raw acquisition/XML parse/series extraction remain NOT_DONE.
- CDSL live 16-Nov page's Equity sub-total is +₹5,564.90 crore, calculated from gross buys ₹18,571.97cr less gross sales ₹13,007.07cr. The ₹5,564.89cr exchange-only row is not the accepted sub-total. FPI five-category subtotal +₹4,845.93cr; MF separate -₹18.74cr; page total +₹4,827.19cr.
- Updated correction report: docs/GLOBAL_CAPITAL_ROTATION_CDSL_DATE_CORRECTION_H10_DDP_ROUTE_20261117.md; latest report commit 28e689b990b3f08681361aa554aaa772d6c7e0a9; blob f5f06537d3ad8f5ce1590e4227bf8538d80d9d1f.
- No raw H.10/CSDL payload acquired, no calculation gates passed. Production invariants unchanged; PR #20 remains open, draft, unmerged.
## 3I. Overlay source-freshness correction carried into main specification — 2026-11-17
- `docs/GLOBAL_CAPITAL_ROTATION_OVERLAY_V1.md` now carries the CDSL 16-Nov reporting-date correction and Fed H.10 XML route/acquisition status so the core specification no longer relies only on a side correction note.
- Core spec commit: e70ce0f325afb8250d792875d8caa5f96e8e2dcf; blob: fa12430084748377346e7feb34cd93b4d243face.
- H.10 official XML binary fetch remains unavailable in this execution environment. Exact route is official, but no ZIP bytes/hash/parser output have been acquired. CDSL raw payload likewise NOT_DONE.
- The overlay research unit-test workflow has historical PASS runs (latest visible prior run 43204879661, commit 7bc769b002c9c4bb26aa3bb464888e962944e580); no new run is yet visible for the latest documentation-only commits. Do not carry forward an old PASS as current-head CI evidence.
- No new source observations or calculation gates were admitted. Overall overlay completion percentage remains unreported pending a full acceptance-matrix audit.

## 3J. H.10 release-page XML route and IMF API access checkpoint — 2026-11-17
- New checkpoint: `docs/GLOBAL_CAPITAL_ROTATION_H10_IMF_ACCESS_CHECKPOINT_20261117.md`.
- Checkpoint commit: 1235521fa4dca01590a14922c10d559886fe968b.
- Official Fed H.10 release landing page now yields exact XML/ZIP route `https://www.federalreserve.gov/releases/h10/data/FRB_h10_xml.zip`. Browser fetch rejected binary content type; route discovery PASS only, raw ZIP acquisition/parse NOT_DONE. Fed FAQ confirms release-page XML continues after BYP retirement, but is overwritten each update and does not provide archived point-in-time vintages.
- IMF official API page documents SDMX 2.1/3.0 but Swagger requires beta portal sign-in. Legacy IMF SDMX Central guide documents a public REST endpoint, but no live response or BOP_AGG mapping was verified. IMF observation acquisition remains NOT_DONE; no values admitted.
- No synchronized panel or overlay calculation gates advanced. All production invariants unchanged; PR #20 remains open/draft/unmerged.


## 3K. IMF BOP versus BOP_AGG catalogue distinction — 2026-11-17
- Official IMF API documentation advertises SDMX 2.1/3.0 but Swagger exploration requires beta portal sign-in. Official IMF SDMX Central catalogue visibly lists IMF:BOP DSD versions including 2.6.0; this does not establish that IMF.STA:BOP_AGG is available on that legacy service.
- Country-level IMF:BOP transaction observations are a distinct possible medium-frequency fallback, not a substitute label for BOP_AGG. Live dataflow/DSD/observation retrieval, dimension mapping, EM membership/weights and missing-reporter treatment all remain unverified.
- Updated source register: commit 6e65f6a820fd6d4032f7d63c6a33c6fdf5727e50; blob 991c974d338620e5852f609a7122e2f59a86c643.
- No IMF observations admitted, no panel/calculation gate advanced, no production changes.


## 3L. IMF SDMX Central observation-endpoint scope correction — 2026-11-17
- The official IMF SDMX Central Web Services Guide (May 2025) distinguishes `/sdmx/v2/` as the public structure/metadata service from `/ws/public/data` for FMR data-processing operations. Neither route is evidence of a public BOP observation-data endpoint.
- Modern IMF BOP dataset API link redirects to developer-portal sign-in. Public BOP/BOP_AGG observations remain NOT_VERIFIED; DSD raw XML retrieval also NOT_DONE. No values admitted.
- Updated extraction spec commit: 3c93551577c32ec584173f62c76d24c333251d8f; blob: 808021c9239c35a77b445611fff62dfb83371f13.
- Updated official source register commit: 19758b6d62da532f960b05d1ce2836b81d701c81; blob: b1d7c4f9d1e5ccd8080c35dc761a4f1c6703f03c.
- No panel or calculation gate advanced; no production changes.


## 3M. IMF current BOP dataset route and stale pilot rejection — 2026-11-17
- Current IMF BOP dataset page is distinct from BOP_AGG and describes resident/nonresident transactions; page exposes API/VIEW DATA/DOWNLOAD, but API redirects to sign-in and no current raw payload/direct download URL was acquired.
- SDMX Central contains provider-specific national BOP dataflows/registrations, not a unified IMF global observation panel. Treat as leads only pending provider-level QA.
- Historic IMF BOP pilot regional SDMX files explicitly last updated 2013-01-09; rejected for current overlay signal, retained only as historical format/reference.
- Updated IMF extraction spec commit: ecea657c2cf515933eeedbaeb51c8f0928bdf5c8; blob: 2d85316df371b56e88ffb2cef33e1b65e420e023.
- Updated source register commit: 910399d2e9e893233dd402197d0a454dea0a6db4; blob: 85ab457b8b9cbc198aa50d21d38867ccc3f28b64.
- No observations admitted; BOP/BOP_AGG panel, synchronized panel and relative-attraction gates remain NOT_DONE. Production unchanged.


## 3N. Brazil BCB official monthly portfolio-flow pilot — 2026-11-17
- Identified and retrieved live JSON responses from official BCB open-data API endpoints via the BCB Open Data Portal resource links.
- SGS 22906 (net acquisition of financial assets): monthly USD million, from 1995-01; latest visible 2026-09-01 = +3,269.3.
- SGS 22924 (net incurrence of liabilities): monthly USD million, from 1995-01; latest visible 2026-09-01 = -1,698.5.
- Exact URLs, definitions, provenance boundaries and acceptance limits recorded in source register. This is Brazil country-level monthly data, not IMF BOP_AGG/EM aggregate. Do not combine signs before exact series sign reconciliation.
- Updated source register commit: 25f1a32402b68f7a26ebee517c6d492b1473f1d6; blob: a05537f917efd3bddbee9af59ba4940f60f787a3.
- Updated IMF extraction spec commit: 6c6dcf41ec17352d14147e0d49d1bcec5e331fd0; blob: 194e2a4561d2faabbcd964e73ca7a8a4e37a6f21.
- API response inspection PASS; raw archive, byte count, SHA-256, full-history QA, vintage and sign reconciliation NOT_DONE. No value admitted to global EM flow input; synchronized panel and relative-attraction gates remain NOT_DONE. Production unchanged.


## 3O. BCB 22905 comparability guard — 2026-11-17
- Official BCB Dstat dataset 22905 is a distinct monthly portfolio-investment-net series in the BOP6/BPM6 hierarchy; unit USD million; stated publication timeliness up to four weeks after reference period.
- SGS 22906/22924 are separately catalogued Depec asset/liability component series. No arithmetic equivalence or sign mapping assumed.
- 22905 promoted only to cross-series control candidate; direct API observation not acquired in this browser verification. No series substitution or net-flow calculation permitted until methodology and overlapping observations reconcile.
- Source register update commit: 2218f35e427a90733f9ba3768e6ee1a342d9b193; blob: beb4874d05c4560d392af9fbbe919a96bf481c06. Extraction spec update commit: d04cf751dcb3706dad15c32f4c1c58905cd8a2cd; blob: 4a0b6468834cb96817cb2c7dfa6113e4f9513470.


## 3P. Publication timestamp ordering defect — UTC normalization — 2026-11-17
- Code review found `_published_key()` retained offset-bearing ISO timestamp strings and `latest()` selected the newest publication by lexicographic string order. This can misorder timestamps that use different UTC offsets, selecting the wrong vintage.
- Patched `pipeline/global_capital_rotation_overlay.py` to convert offset-aware datetimes to UTC before returning the comparison key. Date-only and naive legacy values retain their prior representation; no fabricated timezone is assigned.
- Added regression test `test_latest_publication_orders_timezone_offsets_by_utc_instant` with 2026-11-07T00:30:00+02:00 (22:30Z) versus 2026-11-06T23:00:00Z; expected newest is the latter. A local arithmetic check confirmed the UTC order (22:30Z < 23:00Z).
- Pipeline commit: 5daeb769f671a0cfadf1ccd362f545018958758e; blob: 7f6942a6ba061262cd5e11acb0efb7867fcf6a4c.
- Test commit: 33bae5d289932803a0cdb30108e6c114849ecbb4; blob: 6d7eb2fe2a96661c2bf6c08da9a3d89997d06cbd.
- Both files re-fetched and patch presence verified. Full repository unit test suite / CI execution: NOT_VERIFIED; no workflow run returned for the test commit. Do not mark test suite PASS.
- Scope: research overlay timestamp selection only. No production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A-E or hard-gate changes.


## 3Q. Correction to BCB SGS 22905 organization/source classification — 2026-11-17
- Rechecked the exact official BCB portal pages and JSON resource link. SGS 22905 is BCB/Depec (Department of Economics), monthly, million USD, coverage from 1995-01. SGS 22906 and SGS 22924 are also catalogued as BCB/Depec. The earlier 3O note's “BCB/Dstat” classification and claim of a distinct organizational hierarchy are withdrawn as unsupported.
- The 22905 JSON resource link resolves to the official API endpoint and identifies application/json, but response rows were not rendered by the browser. Values/latest period/raw archive/byte count/SHA-256 remain NOT_ACQUIRED/NOT_DONE.
- No arithmetic relationship between 22905 and 22906/22924 inferred. Methodology and overlapping raw observation reconciliation still required.
- Corrected source register commit: acdf663e31d6881d286d44d12d3bd5ef9e3dd677; blob: c97cb778ddd8305ea547daf5fa1c13fbb26432d1. Corrected extraction spec commit: a0605a0f3634b1d7f9e6e5bed1b48b9edd53a209; blob: 47b46ba3588580a8af421622731a9f442a878ed6.
- Evidence: official BCB portal catalogue pages for SGS 22905, 22906 and 22924. No production change.


## 3R. Dual official BCB catalogue conflict for SGS 22905 — 2026-11-17
- Identified conflicting official portal records for SGS 22905: `opendata.bcb.gov.br` classifies as BCB/Depec (metadata 2026-03-26), while `dadosabertos.bcb.gov.br` classifies as BCB/Dstat under BPM6/financial account/portfolio investment (metadata 2026-09-08, timeliness up to four weeks).
- Both identify monthly USD million from 1995-01 and both link an SGS 22905 JSON resource. Catalogue text alone cannot establish whether duplicate records point to the same payload or conflicting definitions.
- Withdraw definitive single-owner assertions. Classification now CONFLICT / UNKNOWN; exclude 22905 from all calculations until final resource URLs, payloads, metadata, date keys, and hashes are compared. Do not infer a net-flow identity with 22906/22924.
- Updated source register commit: 9ce57cf065bc604a41de84960fb81134b39020a5; blob: 4383152e51526c48da87afdda21b8afafdf30861. Extraction spec commit: ef0ac5dabf80952ff5d17636d48567d555934ee2; blob: 51ac652bcc8846552ed8350afa6a08537166de50.
- Official evidence: BCB `opendata` and `dadosabertos` portal dataset pages. No production change.


## 3S. BCB SGS 22905 shared JSON endpoint confirmed; metadata conflict retained — 2026-11-17
- Followed the JSON resource links on both official BCB catalogue pages. Both resolve to the exact same endpoint: `https://api.bcb.gov.br/dados/serie/bcdata.sgs.22905/dados?formato=json`.
- The `dadosabertos` resource click returned readable JSON; visible records begin 1995-01-01 and extend through 2026-09-01 in the browser excerpt. The `opendata` resource resolves to the same URL; no distinct second payload URL exists.
- This resolves the resource-URL comparison: the previous hypothesis of two different payload endpoints is NOT_SUPPORTED. The two official portal entries reference one SGS API series route.
- The metadata conflict remains unresolved: `opendata` labels organization BCB/Depec and `dadosabertos` labels BCB/Dstat and BPM6 financial-account hierarchy. Shared endpoint identity does not establish the authoritative metadata owner, classification, methodology version or historical revision policy. Keep metadata status CONFLICT / UNKNOWN and preserve both provenance records.
- Both CSV resource links resolve to the same `formato=csv` endpoint, but browser reader could not parse `text/csv`; no CSV bytes acquired.
- JSON body was inspected in browser only. Raw response file, byte count, retrieval timestamp, full payload capture, SHA-256, full-history QA and vintage/revision QA remain NOT_DONE. No data admitted to global EM flow input; no relationship/sign mapping to SGS 22906/22924 inferred.
- Updated official source register and IMF extraction spec in the same branch; follow-up commit/blob SHAs to be recorded after writes and re-fetch verification. No production change; PR #20 remains draft/unmerged unless independently changed.



## 3T. BCB live JSON values: 22905/22906 comparison; 22924 re-fetch pending — 2026-11-17
- Official API JSON response for SGS 22905 visibly includes 2026-09-01 = +4,967.8 million USD.
- Official API JSON response for SGS 22906 visibly includes 2026-09-01 = +3,269.3 million USD.
- Arithmetic difference 22905 − 22906 = +1,698.5 million USD.
- A previous inspection had recorded SGS 22924 for 2026-09-01 = −1,698.5 million USD, but the 22924 API could not be freshly retrieved in this turn. The magnitude match is a one-period reconciliation lead only, not proof of formula/sign identity. Do not combine or admit any series.
- Official 22905 catalogue page confirms monthly USD-million data, starts 1995-01 and describes portfolio investment split into assets and liabilities, with stated timeliness up to four weeks. The same page labels organization BCB/Dstat and BPM6 financial-account hierarchy; the second official portal still conflicts with BCB/Depec metadata. Retain CONFLICT / UNKNOWN.
- Raw JSON bytes, byte count, retrieval timestamp, SHA-256, full-history row/date/missing QA, revision/vintage history and BCB methodology sign reconciliation remain NOT_DONE. Browser-rendered JSON is inspection evidence only.
- Next action: acquire 22924 raw response; archive all three series with hashes; run exact common-month comparison for 1995 onward; test any candidate formula across every overlapping month; inspect official SGS detailed metadata/methodology and revisions; keep UNKNOWN/excluded until every gate passes.
- No overlay calculation, stock ranking, selector, production or trading logic changed.



## 3U. BCB liability inflow/outflow component discovery; 22924 live refresh blocked — 2026-11-17
- Official BCB catalogue identifies three distinct monthly USD-million series, all beginning 1995-01 and attributed to BCB/Depec: SGS 22924 (liabilities net), SGS 22925 (liabilities inflows), SGS 22926 (liabilities outflows).
- This is a new, useful reconciliation path. The existence of gross inflow/outflow series does not prove SGS 22924 = 22925 − 22926 or any other formula. Sign convention, gross/net treatment, scope, timing and revisions must be tested against full common-period raw observations and BCB methodology.
- Direct open of the official 22924 JSON endpoint was inaccessible to the browser reader in this turn. Treat as tool access limitation, not source outage. No fresh 22924 value/raw bytes acquired; previously noted Sep-2026 -1,698.5 is not freshly revalidated.
- BCB's September-2026 External Sector Statistics publication reports domestic-market portfolio investment liabilities net outflows USD 2.1bn, equity/fund outflows USD 1.7bn and debt-security outflows USD 0.4bn; 12-month net inflows USD 5.1bn. This is contextual official cross-check only, not proven identical to SGS 22924.
- Source register, IMF extraction spec and this ledger updated. Acceptance remains BLOCKED: raw 22924/22925/22926 capture, byte counts, retrieval timestamps, SHA-256, full common-period QA, formula/sign reconciliation, vintage/revision QA all NOT_DONE. No values admitted to overlay.
- No production changes. PR #20 remains open/draft/unmerged pending fresh status verification.



## 3V. Brazil Sep-2026 outflow: India transmission relevance classification — 2026-11-17
- BCB official External Sector Statistics (release 26-Oct-2026): Brazil domestic-market portfolio investment net outflow USD 2.1bn in Sep-2026, split equity/funds -USD 1.7bn and debt securities -USD 0.4bn; trailing 12-month portfolio investment net inflows remained +USD 5.1bn.
- RBI official preliminary India BoP release (13-Nov-2026): Sep-2026 net FPI -USD 6.7bn, including FPI investment in India -USD 6.5bn; Apr-Sep 2026 cumulative net FPI -USD 8.9bn.
- RBI official macro-financial commentary reports India and other EM portfolio flows net sold since September, attributing the environment to West Asia tensions, elevated crude oil and rising global bond yields; RBI also describes Indian equities as bearish in Sep and Oct (through 19-Oct), with DII net buying providing support.
- Interpretation: BCB Sep outflow is **contextual cross-country risk-appetite corroboration only**. It does not quantify an India market impact or establish causality. Do not compare the Brazil USD 2.1bn and India USD 6.7bn figures as apples-to-apples market impact; definitions/perimeters differ. Brazil's positive trailing-12-month net inflow argues against reading one month as structural outflow.
- Overlay disposition: `BRAZIL_PORTFOLIO_FLOW_CONTEXT` = contextual only / low direct India-transmission confidence. No independent NIFTY/sector/stock weight, ranking score, buy/sell trigger or production selector input. Direct India FPI, FX, yields, crude, VIX and domestic breadth/flows remain the testable transmission channels.
- Updated Overlay V1 doc and this ledger. This is a research classification decision; no production change.



## 3W. Daily India-market temporal-alignment guard — 2026-11-17
- Code review identified that the classifier selected the latest value per indicator but did not report whether the daily market inputs shared comparable observation dates.
- Added `temporal_alignment.daily_india_market_panel` to the research-only output. It evaluates latest non-stale observations for India FPI equity/debt, DII equity, USD/INR, Brent, VIX, India-vs-world relative return, ICE DXY (if separately supplied), Fed broad USD, and US 10Y.
- Threshold is explicitly an engineering guard of 3 calendar days, not an economic threshold: `ALIGNED_WITHIN_3D` when at least two inputs exist and spread <=3 days; `UNSYNCHRONIZED` when spread >3; `NOT_ASSESSED` when fewer than two inputs exist. Output records dates, included indicators and missing/stale exclusions.
- No forward-fill or interpolation. Monthly EM flows remain a separate frequency layer. The date check does not establish same-session timing, publication-vintage equality or causality.
- Added three unit tests: over-3-day spread rejects synchronization; within-3-day spread passes the date-proximity guard; fewer than two inputs remains NOT_ASSESSED.
- Pipeline commit `c20810f635fef01f738fcbdfec44ee94f1a98dbc` (blob `d82f37b3699cdac25b154e87b01214f81783cfd4`); test commit `8fd36b33685ac8e09e7d79e3fa8ba9b7e0663512` (blob `584d50ce8f904c3c5447501d66c87c139443b62a`).
- Files were updated on the existing research branch; CI result pending. No live dataset, relative-attraction computation, stock score, production selector or trade trigger created. PR remains draft/unmerged unless separately changed.



## 3X. Existing seed inventory check — synchronized raw panel not present — 2026-11-17
- Inspected the complete `data/global_capital_rotation/` directory on the research branch. It contains only three CSVs: `2026-11-07_seed_observations.csv`, `2026-11-10_seed_observations.csv`, and `fed_h10_derived_observation_2026-11-06.csv`.
- The 2026-11-10 seed contains six daily India FPI equity rows for 02-Nov through 09-Nov, one MTD and one YTD subtotal, one debt subtotal, and one H-1B policy event. It does not contain DII, USD/INR, Brent, VIX, DXY, US10Y, India-vs-world relative return, or global EM flow observations. The Fed H.10 derived file is a single broad-USD diagnostic and is not ICE DXY.
- Therefore the new temporal-alignment guard can only report NOT_ASSESSED/UNKNOWN on current seed data; it cannot manufacture a synchronized panel. This is an inventory finding, not a failure of the new date guard.
- Official CDSL page latest visible reporting date at this audit is 16-Nov-2026, but no immutable 16-Nov raw snapshot is present in the overlay data directory. Preserve the previous 09-Nov seed as historical; do not silently overwrite or pretend it is current.
- Next data work remains: acquire immutable official daily series for the synchronized India-market group, with each series' observation date, published_at, retrieved_at, source URL, raw bytes and SHA-256; acquire DII combined NSE+BSE+MSEI separately from NSE-only; acquire USD/INR, Brent, VIX, comparable total-return benchmark and US yields; then build date-keyed panel with missing dates left blank and vintage metadata preserved.
- No values admitted; no synthetic fill; no production changes. CI for the new code/test commits has not been observed; last verified historical successful run is 43204879661 on older commit 7bc769b002c9c4bb26aa3bb464888e962944e580, not the current code.


## 3Y. Official H.10 raw archive extraction and broad-USD 20-interval calculation — 2026-11-17
- Retrieved the user's Library-held `FRB_H10.zip` into the working environment and inspected its ZIP/XML contents. ZIP bytes = 2,087,297; ZIP SHA-256 = `aa78aedcc4620594b69617e99a1453a52ae837d45469ed0dea859c5461f37401`; embedded `h10_data.xml` SHA-256 = `49b625b653e279f2ccf9cf665f581e507492d4b47d02dd106eddf06cf5502edf`.
- H.10 XML header Prepared = `2026-11-09T18:25:06`. Identified series `JRXWTFB_N.B`, “Nominal Broad Dollar Index”, unit index Jan-1997=100, daily. 5,440 observations; archive coverage 2006-01-02 to 2026-11-06.
- Last valid point 2026-11-06 = 121.8803; 21st preceding valid point 2026-10-09 = 121.6023; change over 20 valid observation intervals = +0.2286140969373074%. ND on 2026-10-12 (-9999.0) was explicitly excluded as missing, not treated as a value.
- Created `data/global_capital_rotation/fed_h10_nominal_broad_usd_20obs_2026-11-06.csv`, commit `fff9580f0948689dce9139fc1b2d933f9a25ff36`; source register commit `9d2c971031eb3c5ab7fb9da464e70ce4efa85501`.
- Critical correction: existing `fed_h10_derived_observation_2026-11-06.csv` contains FRED DTWEXBGS, not the H.10 JRXWTFB_N.B series. H.10 JRXWTFB_N.B uses Jan-1997 base; FRED DTWEXBGS uses Jan-2006 base. Keep separate, do not splice or label as ICE DXY.
- The new H.10 metric is a historical daily observation and may be stale depending on as-of date; it is not a current 17-Nov print. It is not yet mapped to the classifier's existing `fed_broad_usd_change_pct_20d` key, deliberately preventing silent substitution. H.10/FRED daily observation vintage alignment, other market inputs and synchronized panel remain incomplete.
- This is a raw-archive and derivation integrity PASS only. Full H.10 dataset source-level QA, end-to-end pipeline execution, CI on current branch, full synchronized panel, IMF country-flow panel, relative-attraction calculation and predictive validation remain NOT_DONE/BLOCKED. No production changes.

## 3Z. CDSL live-page recheck — 2026-11-17 21:47 Asia/Kolkata

- Fresh official CDSL Daily Trends page inspection at 21:47 IST now displays reporting date 17-NOV-2026. The archive page also states that daily investment archive is available up to 17-Nov-2026. This is a later live-page state than the earlier 16-Nov correction checkpoint; preserve both observations with their retrieval context rather than overwriting history.
- Current displayed 17-Nov category subtotals (INR crore): Equity +5,107.61; Debt-General +137.23; Debt-VRR -2,379.67; Debt-FAR -424.29; Hybrid -4.74. Arithmetic subtotal = +2,436.14. Mutual Funds are separate at +37.68; displayed page total including MF = +2,473.82. Do not treat the page total as FPI-only.
- CDSL states the investment figures are based on custodian reports received by depositories on 17-Nov and represent trades on and up to previous trading day(s); the reporting date is not an intraday execution timestamp. Derivatives table is a separate dataset and must not be mixed into cash investment categories.
- Official page refs inspected: https://www.cdslindia.com/eservices/publications/fiidaily and https://www.cdslindia.com/Publications/ArchiveDataAfter2009.aspx. This checkpoint is HTML/display evidence only.
- Acceptance boundary: current displayed page + arithmetic recheck = PASS (bounded); immutable raw HTML/CSV/response bytes, exact download URL, byte count, retrieved_at header capture and SHA-256 = NOT_DONE. Do not ingest this display-only checkpoint into the raw daily panel or claim raw archive acquisition.
- Next action remains actual CDSL archive/raw-byte capture through a verified official download route, then independent hash + schema/vintage QA. If no downloadable raw payload is exposed, record BLOCKED with the exact route limitation; do not fabricate a CSV from rendered page text.

## 3AA. CDSL archive-route and BCB component-series follow-up — 2026-11-17

### CDSL
- Reopened the official CDSL archive page. Its current page header explicitly says daily FII/FPI investment archive is available through 17-Nov-2026; the archive page exposes historical daily rows and a cumulative table. This confirms archive-page coverage is fresher than the earlier 06-Nov archive snapshot.
- Reopened the official live Daily Trends page. It displays 17-NOV-2026 investment reporting date. FPI category subtotals: Equity +₹5,107.61cr; Debt-General +₹137.23cr; Debt-VRR -₹2,379.67cr; Debt-FAR -₹424.29cr; Hybrid -₹4.74cr; arithmetic FPI subtotal +₹2,436.14cr. Mutual Funds are separate +₹37.68cr; page total including MF +₹2,473.82cr. CDSL says values are custodian reports received 17-Nov and trades on/up to previous trading day(s).
- Official archive page: https://www.cdslindia.com/Publications/ArchiveDataAfter2009.aspx ; live page: https://www.cdslindia.com/eservices/publications/fiidaily .
- Important: archive HTML exposure is not immutable raw-file capture. The page-reader exposes rendered HTML/table rows but no verified CSV/XLS download payload, exact export URL, HTTP response headers, byte count or raw response SHA-256. Therefore raw archive acceptance remains NOT_DONE. Do not synthesize a CSV from page text and do not ingest the 17-Nov display as immutable raw data.
- Web evidence refs: CDSL archive page turn807292view0 (header through 17-Nov-2026; historical daily table and cumulative rows) and live page turn807292view1 (17-Nov detailed category rows and source caveat).

### BCB Brazil component series
- New official catalogue verification: SGS 22907 is “Portfolio investment - Net acquisition of financial assets - monthly - inflows”, BCB/Depec, monthly, USD million, starts 1995-01, with up to four weeks' reporting timeliness. Official dataset exposes JSON and CSV resource links. This is a component series, not a verified substitute for the monthly net-acquisition series 22906.
- SGS 22926 is “Portfolio investment - Net incurrence of liabilities - monthly - outflows”, BCB/Depec, monthly, USD million, starts 1995-01. Official dataset exposes JSON and CSV resources. This is a component series, not a verified substitute for liabilities net series 22924.
- Official catalogue sources: https://opendata.bcb.gov.br/dataset/22907-portfolio-investment---net-acquisition-of-financial-assets---monthly---inflows ; https://opendata.bcb.gov.br/dataset/22926-portfolio-investment---net-incurrence-of-liabilities---monthly---outflows .
- Direct official SGS API JSON opens for 22907 and 22926 were inaccessible to the web inspection layer. A separate execution-environment request failed DNS resolution before HTTP response. This is a tool/network access limitation, not evidence that BCB is down. No raw bytes, HTTP status, response size, retrieved_at, SHA-256 or full-history values were acquired. No values admitted.
- No relationship such as 22906 = 22907 - another component, or 22924 = inflows - 22926, is inferred from labels. Need raw common-period observations, BCB methodology and sign/unit/vintage checks before any formula.

### Next action and acceptance boundary
1. Acquire CDSL official downloadable raw payload only if an actual official export/download resource can be followed; otherwise retain display-only checkpoint and mark raw capture BLOCKED by access-layer limitation.
2. Acquire BCB 22907, 22925, 22926 and net controls 22906/22924 as immutable raw responses; record final URL, response status/content-type, byte count, UTC retrieval timestamp, SHA-256, parsed row count, min/max period, duplicate/missing checks and revision/vintage evidence.
3. Reconcile gross components against net controls over every common month before admitting any Brazil portfolio flow. Until then all BCB components remain contextual/discovery-only, not EM aggregate.
4. Daily synchronized India panel, IMF BOP_AGG observation panel, Relative-Attraction calculation and predictive validation remain NOT_DONE/BLOCKED. No composite score or production integration.

## 3AB. Fresh official BCB SGS 22907 JSON inspection + CDSL archive page revalidation — 2026-11-17

### BCB SGS 22907
- Followed the official Open Data Portal JSON resource link for SGS 22907. The browser returned the visible JSON series from 1995-01 through 2026-09; latest visible observation: 2026-09-01 = USD 2,685.9 million.
- SGS 22907 metadata: Portfolio investment - Net acquisition of financial assets - monthly - inflows; BCB/Depec; monthly; USD million; coverage starts 1995-01; portal metadata updated 2026-03-26. This is an assets-side inflow component only, not a global/EM portfolio aggregate and not a substitute for SGS 22906 net asset acquisition.
- Official JSON resource: https://api.bcb.gov.br/dados/serie/bcdata.sgs.22907/dados?formato=json . Official catalogue/resource refs: turn159489view2, turn333578view0.
- Browser-visible JSON is inspection evidence only. CSV resource click timed out at browser fetch; a separate direct request failed DNS resolution. No immutable raw response bytes, HTTP headers/status, byte count, exact retrieval timestamp, SHA-256, full row-count/duplicate/missing QA or vintage history were captured. Therefore 22907 remains DISCOVERED / BROWSER-INSPECTED, NOT_RAW_VERIFIED, and EXCLUDED from calculated/netted overlay features.
- No formula or sign relation between 22907 and 22906 inferred. Any component reconciliation must be tested across full common monthly coverage against official methodology and corresponding controls.

### CDSL official archive page revalidation
- Reopened the official CDSL archive page. Its current header reads Daily Trends in FII/FPI Investments upto 17-Nov-2026; the live daily page independently displays 17-NOV-2026 investment reporting date.
- Archive rows expose daily category tables in rendered HTML, but page inspection finds no visible CSV or Download link. This is not raw-file acquisition. Do not convert rendered table text into a purported official CSV or hash it as if it were the source response.
- Live 17-Nov category values: Equity +₹5,107.61cr; Debt-General +₹137.23cr; Debt-VRR -₹2,379.67cr; Debt-FAR -₹424.29cr; Hybrid -₹4.74cr; FPI subtotal +₹2,436.14cr. Mutual Funds +₹37.68cr remain separate; total including MF +₹2,473.82cr. CDSL says custodian reports received 17-Nov and trades on/up to previous trading day(s).
- Official evidence refs: archive turn159489view0 (header and table), live daily turn159489view1 (17-Nov rows and custodian/reporting-date caveat). This confirms rendered-page coverage only, not raw archive bytes.

### Disposition / next action
- BCB 22907 latest visible Sep-2026 component observation = browser-inspected only; no calculation admitted.
- CDSL current page/archive display = bounded verification PASS; immutable raw payload + SHA-256 = NOT_DONE.
- Continue only with an actual retrievable official raw payload and preserve byte-level provenance. If the available browser/download route continues to time out and no alternative official export is exposed, record a bounded access BLOCKER rather than synthesizing data.
- IMF BOP_AGG raw observation archive, synchronized India daily panel, Relative-Attraction calculation and predictive validation remain NOT_DONE/BLOCKED. No production changes; PR #20 remains research-only.

## 3AC. IMF BOP_AGG and RBI USD/INR source-fitness recheck — 2026-11-17

### IMF BOP_AGG — official source qualification
- Reopened the exact IMF dataset page `https://data.imf.org/en/datasets/IMF.STA:BOP_AGG`. It describes BOP/IIP World and Country Group Aggregates (historically BOPSY), an annual publication released each November and based on BPM6. Country-group aggregates combine reported data with estimates for nonreporting economies; country-level data have a different compilation basis.
- The page exposes API / View Data / Download affordances, but following the API link redirects to the IMF API developer portal sign-in page. No public raw BOP_AGG observation payload, CSV/XLS bytes, response metadata or SHA-256 was acquired in this check.
- Fitness decision: BOP_AGG is annual and group-aggregate/contextual evidence, not a daily or monthly synchronized global portfolio-flow panel. Do not use it as a substitute for daily FPI/DII or monthly country-level portfolio-flow series. It may remain a separate annual macro-context layer if and when raw public data are acquired and its aggregate-estimate methodology is preserved.
- Evidence: IMF BOP_AGG dataset page `turn250862view0` lines 13-23; API link redirects to sign-in `turn212170view0`.

### RBI USD/INR — official DBIE and RBI archive qualification
- Official RBI DBIE search result for `financial_markets.r691_daily_interbank_forex_rates_usd_vis_a_vis_inr` identifies “Daily interbank forex rates (USD vis-a-vis INR)”, source RBI, daily frequency, 6,319 rows, coverage 08-Aug-2000 to 30-Jun-2026, with Download CSV and JSON controls. The displayed latest period is 30-Jun-2026, so as of this 17-Nov-2026 checkpoint it is over four months behind and fails a current daily freshness gate until refreshed. No raw CSV/JSON bytes, exact API/export URL, retrieval timestamp or SHA-256 acquired.
- RBI's own Reference Rate Archive is an interactive date/currency search page and exposes an Excel download control, not a directly verified CSV resource in this inspection. This is a separate RBI reference-rate series and must not be silently substituted for DBIE interbank rates. Source page shows last website update 17-Nov-2026, which is not itself a latest observation date.
- Evidence: DBIE table result `turn940379search6`; RBI Reference Rate Archive `turn250862view2` lines 23-50 and 91.
- Decision: RBI DBIE daily series = official metadata discovered, latest visible observation stale for current panel, raw acquisition NOT_DONE. RBI reference-rate archive = official archive UI discovered, direct downloadable payload not acquired. Keep these two rate definitions distinct.

### CDSL freshness caveat
- Fresh search-index result for the CDSL live page displayed 16-NOV-2026; a previously opened live-page view in this same research stream displayed 17-NOV-2026. Search-index/cache and page-open snapshots therefore disagree on the latest displayed date. Preserve both retrieval vintages; do not overwrite the 17-Nov checkpoint or claim an independently stable current value based on the cached snippet alone.
- CDSL archive search-index result displayed coverage only through 06-Nov-2026, while the earlier direct page-open checkpoint showed an archive header through 17-Nov-2026. This discrepancy is a retrieval/rendering freshness conflict, not evidence that CDSL deleted later rows. Raw bytes and hash remain NOT_DONE.
- Evidence: live search result `turn940379search4`; archive search result `turn940379search5`; prior direct-open checkpoints recorded in sections 3AA/3AB.

### Acceptance / next action
- New work completed: source suitability and access-gate qualification for IMF BOP_AGG and RBI USD/INR, plus CDSL snapshot conflict explicitly preserved.
- No raw source bytes acquired in this checkpoint; no new values admitted; no synchronized panel assembled. IMF annual aggregate is rejected as daily/monthly substitute; RBI DBIE current freshness is not accepted until latest data are refreshed; CDSL remains display-only.
- Next smallest high-value action: use an actual official downloadable RBI DBIE CSV/JSON resource or RBI archive Excel export to capture raw bytes, response metadata, retrieval time and SHA-256; then test latest observation freshness before admitting it. Do not use third-party mirrors or fill missing dates.
- Relative-Attraction calculation and predictive validation remain BLOCKED. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A-E and Hard Gate unchanged; no production integration.

## 3AD. RBI USD/INR official download-route test — bounded access blocker — 2026-11-17

- Rechecked the official RBI DBIE table listing for `financial_markets.r691_daily_interbank_forex_rates_usd_vis_a_vis_inr`. It identifies the RBI daily interbank USD/INR table, daily frequency, 6,319 rows and visible coverage 08-Aug-2000 to 30-Jun-2026, with CSV and JSON download controls. Latest visible observation remains 30-Jun-2026, stale for a 17-Nov-2026 synchronized daily panel. Evidence: `turn756974search1`.
- Reopened the official RBI Reference Rate Archive. It exposes date/currency search controls and an “Download to: Excel” control. The page reader resolves the Excel icon as `https://www.rbi.org.in/Images/xlsx.gif`; following it returned an unsupported image/gif response, not an Excel dataset. Evidence: `turn625688view0` lines 23-50 and 91; click attempt `turn206397view0`.
- This confirms the archive UI exists but does not expose the generated Excel export through the available inspection route. No actual xlsx/csv/json data bytes, response headers/status for the dataset, byte count, retrieved_at, SHA-256, row count or latest observation were acquired. Do not treat the icon image as a dataset and do not mark RBI raw capture PASS.
- A third-party mirror/derived data service reports newer dates but is excluded under the official-source-only constraint. Do not substitute it for RBI raw data.
- Acceptance: official source identity/frequency = previously PASS; DBIE visible coverage/freshness = STALE; RBI archive export access = BLOCKED by current reader route; raw capture/hash = NOT_DONE; panel admission = REJECTED pending fresh official payload.
- Next exact action: use the DBIE CSV/JSON control or RBI Reference Rate Archive's generated Excel action in an environment that can retrieve the actual data response; record final URL, status/content-type, bytes, UTC retrieval timestamp, SHA-256, schema and latest observation. If it cannot be retrieved, retain BLOCKED and proceed to another independent official input without imputing FX.
- No changes to pipeline, classifier, production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A-E or Hard Gate. No synthetic values or production integration.

## 3AE. RBI official FX freshness cross-check — current homepage reference rate vs stale DBIE interbank table — 2026-11-17

- Fresh official RBI homepage result displays current exchange rates with INR/USD 94.1997, explicitly timestamped “As at 1.00pm of November 13, 2026”. Evidence: `turn797966search6`. This is a current official RBI-published reference-rate snapshot (as-of 13-Nov), not a DBIE daily interbank OHLC observation and not a 17-Nov observation.
- Official DBIE table remains daily interbank USD-vs-INR with visible latest period 30-Jun-2026, 6,319 rows, CSV/JSON controls. It is stale for current daily alignment; do not replace it with the homepage snapshot or silently relabel series. Evidence: `turn797966search0`.
- Official RBI Foreign Exchange Turnover release dated 05-Nov-2026 provides daily interbank/merchant turnover for 26-Oct through 30-Oct-2026, but this is turnover, not USD/INR price. It can serve as a separate activity/context variable only if raw release data and units are captured; it cannot substitute for FX level/return. Evidence: `turn797966search4`.
- Official RBI daily exchange-rate publication table is visible through 28-Apr-2026 in the search result, not a fresh current FX series. Evidence: `turn797966search7`.
- Non-official mirrors/aggregators and third-party archives are excluded from the official-source-only pipeline even where they claim later updates. No third-party raw file used.
- Acceptance: current official RBI reference-rate snapshot freshness = PASS only through 13-Nov-2026 as a distinct snapshot; DBIE interbank daily series current freshness = FAIL/STALE; raw immutable capture and SHA-256 for either source = NOT_DONE; no panel admission yet. Preserve source definitions and timestamp separately.
- Next action: source a dated official RBI/FBIL reference-rate downloadable raw file with full provenance, or retain this official 13-Nov snapshot as a separately tagged one-off observation and leave later dates missing. Do not interpolate, forward-fill, or map it into the DBIE interbank field.

## 3AF. MSEI official combined FPI/DII 17-Nov snapshot — scope and vintage separation — 2026-11-17

- Opened the official MSEI FII/DII activity page. It explicitly labels the combined MSE+NSE+BSE Capital Market Segment data and displays 17-Nov-2026 values: FII/FPI buy ₹19,930.98cr, sell ₹15,735.60cr, net +₹4,195.38cr; DII buy ₹14,903.80cr, sell ₹14,706.87cr, net +₹196.93cr. Evidence: turn591741view0 lines 335-358.
- Arithmetic independently checks: 19,930.98 - 15,735.60 = 4,195.38; 14,903.80 - 14,706.87 = 196.93. Displayed arithmetic PASS only.
- MSEI states its FII/DII data are compiled from trading-member client codes/UCC classifications and are provisional, subject to custodial confirmation and modifications; NSE and BSE use their respective exchange classification fields. Evidence: turn591741view0 lines 359-364.
- This is a provisional combined exchange cash-market series, not CDSL/NSDL custodian-confirmed FPI. It must remain distinct from CDSL 17-Nov custodian reporting snapshot (which states trades on/up to previous trading day(s)) and from NSE-only scope. Do not compare or join by the displayed date alone. CDSL Equity +₹5,107.61cr and MSEI combined provisional FPI +₹4,195.38cr have different reporting/coverage and confirmation semantics; the difference is not an error or reconcilable residual without matched trade-date scope.
- No visible downloadable raw CSV/XLS payload or exact file URL was exposed in this page inspection. Raw bytes, byte count, retrieved_at, SHA-256, full history, and schema QA remain NOT_DONE. Do not synthesize a raw file from HTML.
- Acceptance: official source identity and scope metadata = PASS; displayed arithmetic = PASS; raw acquisition/hash = NOT_DONE; matched daily panel = BLOCKED; no overlay admission pending raw and vintage QA.
- Next action: capture MSEI official daily history/raw export only through a verifiable official download route; otherwise preserve as display-only provisional evidence. Continue separate CDSL confirmed FPI, NSE-only provisional, and combined MSEI/NSE/BSE provisional series. No forward-fill or cross-scope substitution.

## 3AG. NSE two-scope FII/DII snapshot byte-integrity and cross-scope reconciliation — 2026-11-17

### Exact files inspected from Library
- `fii-dii-combined-latest.csv` (Library file `file_0000000077ec8211afe18d751021a9c6`), 218 bytes, created 2026-11-16 09:09:45 UTC; SHA-256 `2697546fa012f4c08449b37a3eb7d0f8298f296c25fd8ce4b7ca134c37999eb2`.
- `fii-dii-nse-latest.csv` (Library file `file_000000006a3c82119beb9a4557318937`), 218 bytes, created 2026-11-16 09:09:45 UTC; SHA-256 `b733444b5a846abb672226bc96448bc0baea2da0ad15fe810207fbe93aad7f18`.
- Correction to prior shorthand: hash `2697546f...99eb2` belongs to COMBINED; hash `b733444b...7f18` belongs to NSE-ONLY. Do not reverse these labels.
- Both files contain exactly two categories (DII and FII/FPI) for 13-Nov-2026, with buy/sell/net in INR crore. No daily history beyond this one date is present in these files.

### Independent arithmetic (4/4 PASS)
- Combined: FII/FPI 18,339.57 - 12,603.02 = +5,736.55; DII 11,745.95 - 13,999.53 = -2,253.58.
- NSE-only: FII/FPI 17,376.50 - 12,122.52 = +5,253.98; DII 10,561.32 - 12,532.05 = -1,970.73.
- All four recomputed nets equal the stored net values to 0.01 crore precision; zero arithmetic mismatches.

### Scope deltas (COMBINED minus NSE-only; not an extra flow)
- FII/FPI: buy +963.07; sell +480.50; net +482.57 crore.
- DII: buy +1,184.63; sell +1,467.48; net -282.85 crore.
- These are cross-scope differences between provisional exchange series, not an additional independent investor flow, not custodian-confirmed final FPI and not a CDSL reconciliation residual. Do not add them to either scope or infer investor domicile.

### Provenance and admission boundary
- Byte integrity was recomputed from the two exact Library files in this run; their file sizes and SHA-256 are verified. This proves the stored snapshot bytes, not the original NSE download route: exact original CSV href, HTTP headers/status, download/retrieval timestamp, and upstream NSE response hash were not captured in this checkpoint.
- Official NSE report page identifies two distinct CSV downloads: NSE-only and combined NSE+BSE+MSEI. It also states FII/FPI values are provisional and subject to custodial confirmation/modifications. Evidence: `turn119296view0` lines 128-134 and 118-127; search result table confirms the separate scopes `turn250660search0`.
- Therefore acceptance = Library byte-integrity PASS; arithmetic PASS 4/4; scope comparison PASS; upstream raw-source provenance PARTIAL; full-history acquisition NOT_DONE; matched panel BLOCKED. This one-day snapshot is research evidence only and is not admitted as a complete daily flow panel.
- No production integration or selector changes. No fill-forward, synthetic rows or scope mixing.

## 3AH. MSEI freshness-vintage conflict + official NSE CSV affordance recheck — 2026-11-17

- Official NSE FII/DII report page was reopened. It explicitly exposes two separate CSV download controls: (1) NSE-only Capital Market Segment and (2) combined NSE+BSE+MSEI Capital Market Segment. It also describes the provisional/custodial-confirmation caveat for FII/FPI. Evidence: `turn119296view0` lines 128-134 and 118-127. The web reader's click on the shared page link ID did not resolve a distinct CSV href; it returned the same report page (`turn335055view0`). Therefore the exact original CSV export URLs and HTTP response metadata remain uncaptured.
- MSEI current source snapshots are inconsistent across language/cache routes: English search-index page surfaced 13-Nov-2026 values (FPI +5,736.55cr; DII -2,253.58cr; `turn250660search3`); Hindi search-index surfaced 16-Nov-2026 values (FPI +4,864.68cr; DII -3,519.05cr; `turn250660search6`); directly opened Hindi page displayed only 06-Nov-2026 (FPI +13,749.82cr; DII -5,968.70cr; `turn722859view0` lines 327-354). Treat this as page-vintage/cache/rendering disagreement. Do not select the most recent-looking snippet as a raw observation or overwrite prior 17-Nov displayed snapshot. MSEI provisional classification semantics remain unchanged.
- MSEI equity daily archive page currently states daily downloads are unavailable in the visible page result; this does not prove the separate FII/DII page has no export, but it means no archive download route was verified here (`turn250660search11`).
- This checkpoint does not supersede the Library CSV byte QA in 3AG: two one-day 13-Nov snapshots remain byte-verified (combined SHA `2697546fa012f4c08449b37a3eb7d0f8298f296c25fd8ce4b7ca134c37999eb2`; NSE-only SHA `b733444b5a846abb672226bc96448bc0baea2da0ad15fe810207fbe93aad7f18`). Their exact original download URL/retrieval transport provenance remains PARTIAL.
- Next action: use a browser-capable official NSE download session to retrieve both CSV payloads for a multi-date period and capture exact href, response metadata, bytes, retrieval timestamp, hashes and full-period QA; separately resolve MSEI's dated-page vintage conflict before admitting any MSEI data. No cross-scope substitution or forward-fill.


## 2026-11-18 — Chapter 35 Part-2: Brazil BOP collection metadata semantics
- Recovered and independently re-read the prior Part-7 Brazil raw artifact: Run 44256602275, Artifact 14405348744, raw XML 4,840,062 bytes, SHA-256 3e736c45d67fe64ac8c0cb3396718addab21a1ef43d09666ae8dd8ccaba3f52c; 237 distinct INDICATOR codes and 89,097 observations remain confirmed.
- IMF SDMX Central Web Services Guide and IMF SDDS Plus Technical Implementation Guide confirm the ECOFIN six-dimension dissemination DSD and the mixed INDICATOR dimension / IMF CL_INDICATOR codelist. Do not confuse it with global-use IMF:BOP:2.6.0.
- Corrected .github/workflows/imf_bop_dsd_acquisition.yml: dataflow reference expected IMF:ECOFIN_DSD:1.0; added version-pinned ECOFIN_DSD raw capture, CL_INDICATOR extraction, component/code inventory, bytes and SHA-256. Commits 70b640f8d010d6145819ed5ec15cea1e49e364b9 and 83fd95e67c6f73f6f7405dd1f0758e92153c38da; final blob 226daa294d329b501b19312eb94cec290f17e160. Re-fetched static verification PASS.
- Runtime acquisition NOT_DONE: container DNS failed before HTTP response; GitHub connector did not expose a workflow-dispatch operation. Do not call this an IMF outage.
- Nine Brazil code IDs have BFP/BFPL lexical prefixes, but no prefix-only semantic assignment is accepted. Full 237-code mapping remains NOT_DONE.
- New audit record: docs/BRAZIL_BOP_BPM6_INDICATOR_SEMANTIC_AUDIT_20261118.md, latest audit update commit ef4019b1a560e4bf0280322484a0226436e25042 (at time of this ledger update).
- Next exact action: run the updated workflow on the research branch using GitHub Actions UI/manual dispatch; download artifact; verify live dataflow ref, ECOFIN_DSD, CL_INDICATOR code list, response headers, bytes and hashes; only then generate the 237-code semantic crosswalk. Keep unmapped codes UNKNOWN.



## 2026-11-18 — Chapter 35 Part-3: IMF ECOFIN INDICATOR compliance gate
- Official IMF SDMX Central User Guide, Section 2.2 (May 2025, PDF pp. 5–6), specifies ECOFIN validation: a non-CL_INDICATOR code fails if it does not begin with the reporting country's three-letter ISO code; a non-listed code with that prefix is a warning. Source: https://dsbb.imf.org/content/pdfs/IMFSDMXCentralUserGuide.pdf.
- Added `qa/audit_brazil_bop_indicator_codes.py` to require ECOFIN_DSD 1.0, INDICATOR -> IMF:CL_INDICATOR:1.0, codelist identity/version and unique codes; parse BCB StructureSpecificData namespace for IMF:BOP_BPM6(1.0); enforce REF_AREA BR; classify official code matches, BRA_-prefixed local warnings and other unmapped codes (FAIL/quarantine). No semantic or flow admission is inferred from code-list status.
- Added four tests in `tests/test_brazil_bop_indicator_codes.py`: standard vs Brazil-specific distinction, unlisted non-BRA code fail-closed, wrong codelist identity, wrong dataflow identity. Wired tests into the acquisition workflow; GitHub runtime has not yet executed them.
- Updated workflow to checkout code, run tests, acquire current official BCB BOP XML alongside version-pinned IMF ECOFIN_DSD + CL_INDICATOR, preserve headers/request/completion timestamps/bytes/SHA-256, run the audit and upload evidence. Timeout set to 8 minutes. Final workflow commit 9a17d6fd0144708ffee152d4af233945dfee98bf; blob c5caacbe917d16d108f74bc28047aa60ff89c5e0.
- QA script commit 1924fc0c1290435ed9db5a76168bf0b2b6f95e66; blob b2dbb6b9a63b02c57293f316fc5218fe743161fa. Test commit 0516defffc320cb26c5acc98745c9d3fb265330c; blob 42f8e83fc9ed13f9683a9bfab698fbd98b9809e9.
- Static GitHub re-fetch checks PASS for workflow checkout, test step, timeout, official BCB URL, QA invocation, ECOFIN request and CL_INDICATOR inventory. No workflow dispatch available in this session, so runtime acquisition and GitHub test run remain NOT_DONE.
- Re-parse of existing Part-7 raw BCB XML remains 237 series / 237 unique INDICATORs / 89,097 observations; nine BFP/BFPL codes remain lexical candidates only. Do not infer meaning from prefixes.
- Gate: code-list QA implementation = PASS (committed/static); live codelist match = NOT_DONE; full semantic crosswalk = NOT_DONE; Brazil portfolio flow panel / global EM aggregate / trading signal = NOT_AUTHORIZED. Protected selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 and Engines A–E unchanged.
- Next exact action: manually dispatch the updated workflow on the research branch in GitHub Actions; verify tests and live payload/codelist artifacts; inspect every indicator row; separately review labels, financial-account transaction semantics, assets/liabilities, unit, multiplier, sign, status and vintage. Keep all unproven fields UNKNOWN.

- Final workflow artifact-upload review found the Brazil payload/report directory was not yet included; corrected upload paths to preserve both `evidence/imf_bop_dsd/` and `evidence/brazil_bop/`. Correction commit 9b793dfc10476dcd83d272e8a36275c8bd978b2b; workflow blob affcbdf7166a4dc1bdbbb104c2877975631109e1. Audit documentation update commit 832bf50da23cc1292e70e825acd9da737f12cb42.


- Part-4 registry corroboration: official IMF catalogue search results list IMF:ECOFIN_DSD latest version 1.0 and IMF:CL_INDICATOR (Economic Indicator) version 1.0. Catalogue listing is not a raw XML capture; no codelist codes or payload hashes are claimed from it. Official pages: https://sdmxcentral.imf.org/data/datastructure.html and https://sdmxcentral.imf.org/items/codelist.html.
- Expanded Brazil indicator QA regression tests from four to seven: wrong REF_AREA; country-ISO3 prefix mismatch (IND_ code under REF_AREA BR / BRA); duplicate CL_INDICATOR code. Commit 1f8b07b7111a218880e247997e4cc8f010d8c7fd. Runtime test execution remains NOT_DONE.
- Current acceptance remains: static QA implementation PASS; live IMF codelist capture NOT_DONE; actual 237-code match NOT_DONE; economic classification NOT_DONE; no Brazil/global EM/trading-signal admission.



## 2026-11-18 — Chapter 35 Part-5: verified historical 237-code BOP crosswalk
- Re-downloaded and independently parsed IMF metadata Artifact 14333192531 from Run 44095286184 (not the Brazil raw artifact): `IMF:BOP_BPM6(1.0)` dataflow references `IMF:ECOFIN_DSD(1.0)`; referenced ECOFIN DSD XML 42,707,649 bytes, SHA-256 81f4bf8bf43d466f94f8a429f8c8c40eccffe480845018421a1c384aae97d045; contains IMF:CL_INDICATOR(1.0), 113,644 codes. Dataflow XML SHA 74a8f3a58ff3e0bc6e6681c4143cd042cc642edee06f8080e86c29dc3b64e919; constraint XML SHA aa6c002fb3a2498420ed8796621664b492c18f58d75918d5c1bf8737fc917656.
- Re-downloaded Brazil raw artifact 14405348744 from Run 44256602275. Raw XML 4,840,062 bytes, SHA-256 3e736c45d67fe64ac8c0cb3396718addab21a1ef43d09666ae8dd8ccaba3f52c. Header identifies IMF:BOP_BPM6(1.0); 237 unique series; 89,097 observations; 1995-01 through 2026-09; no duplicate series keys.
- Exact CL_INDICATOR join: 237/237 matched, zero unmatched. Nine financial-account portfolio investment indicators (BFP/BFPA/BFPAD/BFPAEEO/BFPAEIS/BFPL/BFPLD/BFPLEEO/BFPLEIS); nine distinct current-account portfolio investment income indicators (BIPIPED/BIPIPI/BIPIP/BMIPIPED/BMIPIPI/BMIPIP/BXIPIPED/BXIPIPI/BXIPIP). Do not confuse portfolio income with financial-account portfolio capital flows.
- Each of the nine financial-account portfolio series has 381 monthly observations from 1995-01 to 2026-09. Series count distribution across all 237: 217×381, 16×345, 2×249, 2×201. Label-based domain counts: Current Account 146; Financial Account 79; Capital Account 9; Other BOP 3.
- Captured XML has series attrs DATA_DOMAIN, REF_AREA, INDICATOR, COUNTERPART_AREA, FREQ, UNIT_MULT, TIME_FORMAT; UNIT_MULT=6 and IMF labels specify USD. No explicit UNIT_MEASURE attribute; no observation-level OBS_STATUS/CONF_STATUS present. Quality remains UNKNOWN; no rescaling performed.
- BPM6 official sign convention recorded: increases in assets/liabilities positive, decreases negative; FA balance = net acquisition assets minus net incurrence liabilities. Never treat either side alone as net inflow. Do not sum total BFP, assets total BFPA, liabilities total BFPL and their child components together. Sources: IMF BPM6 paragraph 3.31 and Compilation Guide paragraphs 8.102–8.104, Tables 8.9–8.10.
- Important open provenance conflict: BCB XML header says IMF:BOP_BPM6(1.0), while current IMF Registrations page lists the BCB URL under IMF:BOP6(1.0). Preserve both facts; do not overwrite source header or admit to production until reconciled.
- Added qa/build_brazil_bop_indicator_crosswalk.py (commit 2b355b9ea5db9b4e934454fe877b18a17d6a6036) and tests/test_brazil_bop_indicator_crosswalk.py (commit 94e48d826ca1cce865fc0eab8143b6d30e008fd1). Local independent execution produced PASS_CODELIST_CROSSWALK_ONLY; JSON 238,180 bytes; SHA-256 637c64cffdc37e250704e6ac560d5167cdefec1e7e417b33c999644c7fbfcf1f.
- Updated workflow to include push trigger for research branch paths, run both test files, capture current BCB + IMF metadata, generate/hash the full 237-code crosswalk and upload evidence. Commit 7584d5a1292356741716ce4540d4e0a693ed948d.
- Workflow Run 44270663838 started 2026-11-18T08:51:57Z. At audit update it was still in progress; unit test and initial metadata acquisition/validation steps completed successfully; ECOFIN_DSD + CL_INDICATOR acquisition was still running. Must fetch final run conclusion and artifact before runtime PASS claims.
- Brazil panel, global EM aggregate and trading-signal admission remain NOT_AUTHORIZED pending quality attributes, unit scaling confirmation and BCB registration-vs-header reconciliation. Protected selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 and Engines A–E unchanged.


- Additional value QA on recovered Brazil XML: 89,097 observations = 88,764 finite numeric values + 333 literal `...` missing tokens. All 333 are in `BFDLERV_BP6_USD` (132) and `BFOR_BP6_USD` (201). No duplicate TIME_PERIOD values and no missing OBS_VALUE attributes. Do not convert `...` to zero; reason remains unspecified and quality remains UNKNOWN.
- Crosswalk builder enhanced to count explicit missing tokens, validate numeric finite OBS_VALUE, reject unknown nonnumeric values and duplicate periods. Commit 2275348648ac97efeb0a72358dbae54528e8769b; blob 1a1828c0b2e5fb7c918b8a348265844971ed54ff.
- Added three regression tests for missing token, invalid nonnumeric value, duplicate time period. Commit c7210113190afef7627e71212f043e0afe521b02; blob a3e6f9a9110a52be2a12c1620ae9d3227bed6513.
- Push-triggered runs: 44270990383 (commit 2275348648ac97efeb0a72358dbae54528e8769b) and 44271011602 (commit c7210113190afef7627e71212f043e0afe521b02), both in progress at ledger update. Earlier run 44270663838 also still running at last check; retrieve final conclusions/artifacts before claiming runtime acceptance.


## 2026-11-18 — Chapter 35 Part-5 FINAL: runtime workflow + full 237-code crosswalk PASS
- Successful GitHub Actions Run 44271446838; commit 9298d8638b9ed471ed6d0411899bd11ae5e6e72d; conclusion SUCCESS; completed 2026-11-18T08:57:54Z. Artifact 14412253203; ZIP 4,860,541 bytes; digest ccec2f3d88e7bd572d09a9c09a4bb8675cd88f14a7171353d1f9a6d31c45e4ba. Link: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/44271446838.
- All 15 unit/regression tests passed. Workflow steps all passed: IMF DSD 2.6.0, SDMX parser fixtures, current BOP_BPM6 dataflow + constraint capture, exact ECOFIN_DSD ref validation, immutable CL_INDICATOR archive retrieval + SHA/byte/count checks, BCB current capture, code-list audit, crosswalk generation, artifact upload.
- To avoid repeated 42.7 MB transfer timeouts, corrected workflow to reuse version-pinned IMF metadata artifact from successful Run 44095286184 / Artifact 14333192531, verify raw ECOFIN_DSD+CL_INDICATOR SHA 81f4bf8bf43d466f94f8a429f8c8c40eccffe480845018421a1c384aae97d045, byte count 42,707,649 and unique code count 113,644. Added actions:read and fixed token expression.
- Live BOP_BPM6 dataflow XML SHA 705fd14cef5bbc8cc9c4f23662ceab8daa3e2be768be2d1a4fbdeca0643e6075; refs IMF:ECOFIN_DSD:1.0. Live constraint XML SHA 60d31fbf8fa7f76102f68981e5666579b1982b59b5c500d30d057c29402f6b96; one CubeRegion, three unique dimension keys; constraint attached to BOP_BPM6. Both PASS.
- Current BCB capture HTTP 200; raw XML 4,840,062 bytes, SHA 3e736c45d67fe64ac8c0cb3396718addab21a1ef43d09666ae8dd8ccaba3f52c. Code audit PASS: 237/237 official CL_INDICATOR matches, zero unmatched.
- Generated crosswalk artifact JSON: 257,449 bytes, SHA 6161f9929e02474bc9db11fb07c865f1c0e4febb00cdb1300dbbdebd707f12b4. 237 series / 89,097 observations / 88,764 finite numeric / 333 literal ... missing tokens. Domain counts: current 146, financial 79, capital 9, other 3. Nine Financial Account portfolio codes; nine separate Current Account portfolio-income codes. Each of the nine financial-account portfolio series has 381 months from 1995-01 to 2026-09.
- Quality and unit gates remain UNKNOWN: no observation-level OBS_STATUS/CONF_STATUS, no explicit UNIT_MEASURE, UNIT_MULT=6 and label USD, no rescaling. 333 ... values (132 in BFDLERV_BP6_USD; 201 in BFOR_BP6_USD) are missing tokens, never zero. No net portfolio flow calculated; no summing total/parent and component series.
- Open provenance conflict retained: BCB XML header and live IMF dataflow are IMF:BOP_BPM6(1.0), while IMF registrations page lists the BCB URL under IMF:BOP6(1.0). Requires official reconciliation before admission.
- Failed runs retained for reproducibility: Run 44270663838 failed because three 75-second downloads of 42.7MB ECOFIN DSD timed out after partial transfer; artifact 14412855873 retained. Run 44271396745 failed due malformed escaped GITHUB_TOKEN expression for cross-run artifact download; artifact 14412202990 retained. Corrected version-pinned artifact reuse; final Run 44271446838 SUCCESS.
- Final audit update commit 836b166193bb93b125bc1465a82a4c4286deaf6d. Full audit: docs/BRAZIL_BOP_BPM6_INDICATOR_SEMANTIC_AUDIT_20261118.md. Full runtime artifact: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/44271446838/artifacts/14412253203.
- Acceptance: IMF code-list join and 237-code semantic crosswalk PASS; Brazil portfolio panel remains NOT_AUTHORIZED pending unit/scale verification, missing observation quality status, missing-value semantics, and BCB registration-vs-header reconciliation. Global EM aggregate/trading signal NOT_AUTHORIZED. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 and Engines A–E unchanged. Research spend ₹0; no synthetic data.



## 2026-11-18 — Chapter 35 Part-5: successful crosswalk + reconciliation blocker
- GitHub Actions Run #44271446838 / run #5: SUCCESS, all 15 substantive steps; branch research/global-capital-rotation-overlay-v1; head SHA 9298d8638b9ed471ed6d0411899bd11ae5e6e72d. Artifact #14412253203, ZIP digest sha256:ccec2f3d88e7bd572d09a9c09a4bb8675cd88f14a7171353d1f9a6d31c45e4ba; independently downloaded ZIP digest matched. URL https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/44271446838.
- Captured BCB raw payload: 4,840,062 bytes, SHA-256 3e736c45d67fe64ac8c0cb3396718addab21a1ef43d09666ae8dd8ccaba3f52c; Header dataflow IMF:BOP_BPM6:1.0. DATA_DOMAIN=BOP6 is a separate series dimension value, not the dataflow ID.
- IMF ECOFIN_DSD 1.0 / CL_INDICATOR 1.0 captured metadata reused from immutable run 44095286184; 113,644 unique codelist codes; 42,707,649 bytes; SHA-256 81f4bf8bf43d466f94f8a429f8c8c40eccffe480845018421a1c384aae97d045.
- All 237/237 observed Brazil indicators matched CL_INDICATOR; 89,097 observations; 88,764 numeric; 333 literal ... missing; periods 1995-01 to 2026-09. 146 current, 79 financial, 9 capital, 3 other. Nine financial-account portfolio-investment codes; nine portfolio-investment-income current-account codes (keep separate).
- CL_UNIT_MULT code 6 = Millions; labels USD; values not rescaled. Observation quality attributes and explicit UNIT_MEASURE absent; quality remains UNKNOWN_NOT_PASS.
- New reconciliation finding: BFP_BP6_USD vs BFPA_BP6_USD - BFPL_BP6_USD matches exactly for 180 months (1995-01–2009-12) but mismatches for all 201 months (2010-01–2026-09); no missing periods. Maximum absolute difference 8,402.74195204 million USD; mean absolute difference among mismatches 1,249.2619595526864 million USD. BFP label says “Portfolio investment” but does not explicitly say balance. This is an unresolved BPM6-consistent reconciliation diagnostic, not a proven source error. Require BCB/IMF definition and 2010 break explanation.
- Diagnostic report: docs/BRAZIL_BOP_PORTFOLIO_RECONCILIATION_AUDIT_20261118.json. Script qa/audit_brazil_bop_portfolio_reconciliation.py. Three local regression tests passed. Commits: script 425dd717f54b05d566ef2a80a8295c1e217deb63; tests d3b8dff403cde26effb1d14c630108be1bd1552f; report cb2d16465c90067107d9dd18fc66405739cf5a6b.
- Workflow now runs both Brazil QA test modules and emits the reconciliation diagnostic. Commit 3cc6191068924322cc819977ae365920e4d61fad. Push-triggered run #44277686817 / run number 6 was IN_PROGRESS at ledger update; must inspect final status and artifact before acceptance.
- Gates: Run #5 crosswalk PASS; 237/237 codelist match PASS; local reconciliation tests PASS; full period reconciliation FAIL; quality UNKNOWN_NOT_PASS; BFP semantics / 2010 break UNKNOWN/BLOCKED; Brazil panel, Global EM aggregate and trading signal NOT_AUTHORIZED. Production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 and Engines A–E unchanged.
- Next exact work: inspect run #44277686817; investigate BFP code definition and 2010 break using BCB/IMF official metadata; check parent-child instrument roll-ups and quality/vintage metadata. Do not derive net flow or aggregate until reconciliation is resolved.



## 2026-11-18 — Chapter 35 Part-5: BCB SGS cross-source divergence and evidence
- Run #44278280236 / workflow run 10 SUCCESS; all 18 substantive steps completed; head SHA 40765b42efce31255c35abe1e3ade3a91246eccd. Artifact #14415646956, size 4,884,893 bytes, ZIP SHA-256 e0cc555c3d85348ab430fcd2c1c2c92750be99219aec5d4b23ede0b3c382bae3. URL https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/44278280236.
- Captured BCB official SGS 22905 (portfolio net), 22906 (net acquisition assets), 22924 (net incurrence liabilities). Each HTTP 200, 381 monthly rows 1995-01 to 2026-09, units million USD. SHA-256: 22905 bc2077cd9439b9a846984641934f678eaf25e3c79ce3d996362159ef74a587f3; 22906 110477090f5ff3e9f4e4d2ce235082d837020603b13795dbc2bde20769a3db30; 22924 2064005a5dd42b83ba66aeb21de983ca4286af9662f57c23971b4b7dfe295dbb.
- BCB SGS internal identity 22905 = 22906 - 22924 passed within one-decimal rounding tolerance for all 381 months (0 mismatches).
- Provisional concept crosswalk vs IMF-SDMX BFP/BFPA/BFPL: each 180/180 months match 1995-01–2009-12; each 201/201 months diverge 2010-01–2026-09. Max absolute differences in million USD: 22905 19,427.157519; 22906 11,346.55107301; 22924 22,286.52238714. Jan-2010 examples: 22905 -4,441.7 vs BFP 88.38340538; 22906 332.1 vs BFPA 1,194.68277602; 22924 4,773.7 vs BFPL 0.00736122.
- Finding: BCB SGS series are internally consistent; all three mappings to the BCB-published IMF-SDMX BOP_BPM6 XML diverge after 2010. This is a source-series lineage/content discrepancy; cause not established. Do not infer which source is wrong or substitute/splice one source into the other.
- Audit JSON docs/BRAZIL_BOP_SGS_CROSS_SOURCE_AUDIT_20261118.json, SHA-256 3c161e4f27d170a62ab68803f9a25bc8a1e3fe8a9830c288d74415a67d85abd5. Commit 5d363ab50d75dd844d91ac40f6262340b6a843e0.
- New cross-source QA script qa/audit_brazil_bop_sgs_crosscheck.py; tests/test_brazil_bop_sgs_crosscheck.py (3 new tests). Run #10 passed the full combined test suite and all capture/comparison/artifact steps. Earlier run #7 failed due to commit sequencing (workflow referenced SGS script before script file existed); runs #8/#9 failed because escaped shell variable expansion yielded literal $SGS. Corrected by commit 40765b42efce31255c35abe1e3ade3a91246eccd; Run #10 verified HTTP 200 JSON for all three endpoints.
- Gates: 237-code join PASS; BCB SGS internal identity PASS_WITHIN_ROUNDING; SGS-to-IMF-SDMX pre-2010 match PASS_WITHIN_ROUNDING; post-2010 cross-source mapping FAIL_SOURCE_DIVERGENCE; source lineage/vintage cause UNKNOWN/BLOCKED; Brazil panel, Global EM aggregate, trading signal NOT_AUTHORIZED.
- Next exact action: request/locate official BCB metadata lineage explaining the SGS-to-IMF-SDMX difference from 2010-01. Inspect Dataflow BOP_BPM6, DATA_DOMAIN=BOP6, counterpart W1, revision/vintage and code mapping. Preserve both source series separately. No production selector or protected engine changes.

- Official BCB Methodological Note No.1 says BPM6 external-sector statistics began release in April 2015; BCB provides a separate official BPM6 historical-series page with monthly archive. The 2010-01 cross-source break predates that release; do not attribute it to BPM6 adoption without evidence. Sources: https://www.bcb.gov.br/ingles/economic/nm1bpm6i.pdf and https://www.bcb.gov.br/ingles/economic/seriehist_i_bpm6.asp?frame=1. Next: acquire/hash the official monthly ZIP and perform three-way comparison SGS vs BCB monthly archive vs IMF-SDMX XML; inspect DATA_DOMAIN, counterpart, vintage and lineage.



## 2026-11-18 — Chapter 35 Part-6: BCB official BPM6 monthly archive acquisition gate
- Inspected successful Run #10 artifact #14415646956 (4,884,893 bytes; ZIP SHA-256 e0cc555c3d85348ab430fcd2c1c2c92750be99219aec5d4b23ede0b3c382bae3). Verified 237/237 official CL_INDICATOR matches, 237 unique series, 89,097 observations (88,764 numeric; 333 `...` missing tokens), 9 Financial Account portfolio indicators and 9 separate Current Account portfolio-income indicators. Observation quality attributes are absent; quality gate UNKNOWN_NOT_PASS; Brazil flow panel remains NOT_AUTHORIZED_PENDING_SIGN_AND_QUALITY_REVIEW.
- Reconciled unit metadata: CL_UNIT_MULT code 6 = Millions, labels = US Dollars, so scale is million USD; raw values remain unscaled.
- Confirmed SGS 22905/22906/22924 internally satisfy net = assets - liabilities for 381 months within one-decimal rounding, but provisional mapping to IMF-SDMX BFP/BFPA/BFPL diverges for all 201 months 2010-01 to 2026-09. Cause remains UNKNOWN; no source substitution.
- Official BCB BPM6 historical page offers monthly ZIP; exact link resolves to https://www.bcb.gov.br/ftp/notaecon/balpaym.zip. Added safe archive inventory script `qa/inspect_brazil_bop6_archive.py` (commit 695a35dcc33c06d9cf2070efff82f18e875891a3; 4 test cases in `tests/test_inspect_brazil_bop6_archive.py`, commit e91a56ec3bcf4f77544a8065abaa4f3bf431c547). It validates ZIP CRC and member paths and hashes archive bytes; no workbook interpretation.
- Updated acquisition workflow to capture ZIP, request/response metadata, timestamps, SHA-256 and safe inventory; artifact upload includes evidence. Workflow commit f1e6dcd1cde2645572c3482b8ce17dd5f32fe111; blob 2e154a0a84ac802f0f77c260e7c116b662ad654b. Static re-fetch verification pending.
- Runtime status: no Run #11 or monthly ZIP capture confirmed yet. The connector does not expose workflow_dispatch; if push event did not start a run, user must manually dispatch workflow in GitHub Actions UI.
- Next: acquire artifact; inspect ZIP members and workbook sheet/header schema; only then implement parser for exact portfolio assets/liabilities/net rows; compare three-way BCB archive vs SGS vs IMF-SDMX month-by-month. Keep 2010+ divergence BLOCKED until official series lineage/vintage clarification. No Brazil panel, Global EM aggregate or trading-signal admission. Protected production invariants unchanged.



## 2026-11-18 — Chapter 35 Part-6B: BCB monthly workbook tri-source reconciliation evidence
- Run #11 / ID 44280075026 SUCCESS, artifact #14417185373, 7,738,415 bytes, digest c2bbc0a6cc330e36c0eda193a73580ae89f40789c7897b9e09cdb1a3adf50a27. BCB monthly ZIP HTTP 200; 2,849,867 bytes; SHA a7e66aad377851d2969dbc07d4555e8f79839282c5355a3ad3af77459cdb2473. ZIP has one member BalPayM.xlsx (2,915,799 bytes; embedded member timestamp 2019-06-19 15:14; not asserted formal publication date). Workbook SHA dfe3e2ee268bd29a9b9dda8d6e5ff62bf8e84c1c30c1d01e5aa8b4497903189d; sheets Balance, Balance 2, Financial gap.
- In Balance sheet, exact SGS Code mapping: 22905 Portfolio investment row 220; 22906 Net acquisition of financial assets row 221; 22924 Net incurrence of liabilities row 241. Headers row6 year, row7 month; US$ million; 293 periods Jan-1995 to May-2019. Workbook internal 22905=22906-22924 identity PASS 293/293 within 0.051 million USD.
- Independent manual parse of workbook compared with current SGS and IMF XML: Archive vs SGS matches/mismatches: 22905 245/293 match, 48 mismatch; 22906 291/293 match, 2 mismatch; 22924 245/293 match, 48 mismatch. Archive vs IMF-SDMX: all three 180/293 match and 113 mismatch, all mismatches from 2010-01. Pre-break 180 months match.
- 2010-01 workbook values (million USD): net -4441.66992884; assets 332.07298376; liabilities 4773.74291260. They reproduce prior BCB SGS values to displayed precision. IMF-SDMX values same month: 88.38340538; 1194.68277602; 0.00736122. Do not infer source fault.
- Archive vs current SGS revisions first differ 2015-04 for net/liabilities; assets first differ 2019-04. This is evidence of a vintage/content difference; exact revision history not known.
- Added `qa/audit_brazil_bop6_archive_reconciliation.py` and 4 tests (commits 70a7818c62f51890094c0c7fa19e6c70bf137601 / b3879e01790fd9888e2755af7dc3fc411d21c5f7); workflow integration d3b52f78e71d18d7c9c81ae0c541fa5dd100d691. Uses pinned openpyxl 3.1.5, parses exact row labels/code column, period coverage and three-way differences, does not rescale or replace.
- Run #12 ID 44280444665 was in progress when this entry was drafted; no runtime PASS claim until jobs/artifact are checked.
- Admission: Brazil panel, Global EM aggregate and trading signal NOT_AUTHORIZED. Next: validate Run #12, capture three-way reconciliation JSON/hash, then pursue official BCB/IMF source lineage and revision metadata. Keep 2010 break and later revision differences UNKNOWN until explained.



## 2026-11-18 — Chapter 35 Part-6 runtime closeout and Part-7 component-level audit
- Run #12 / ID 44280444665 SUCCESS, head d3b52f78e71d18d7c9c81ae0c541fa5dd100d691; artifact #14416134135, 7,741,512 bytes, SHA 85820e487a4313d89ced5aad88d1f18fe4e122b35fe609a210349a78b84e37b7. Three-way JSON SHA 093bf56e463fd5392b4f76729ecbe7c4703600a0d2f0251d39e3690701068cc7. ZIP and workbook hashes as above.
- BCB archive hierarchy manually checked for 293 months: 22906 assets = 22909 equity assets + 22912 investment fund shares assets + 22915 debt securities; 22924 liabilities = 22927 equity liabilities + 22936 investment fund shares liabilities + 22939 debt securities; 22905 net = 22906 - 22924. All three parent-child identities 293/293 within 0.051 million USD.
- Nine archive-to-IMF series (BFP, BFPA, BFPAEEO, BFPAEIS, BFPAD, BFPL, BFPLEEO, BFPLEIS, BFPLD): each 180/293 match pre-2010 and 113/293 mismatch 2010-01 to 2019-05.
- IMF-SDMX internal parent-child rollups: assets parent BFPA vs three components 180/381 match, 201/381 mismatch; liabilities parent BFPL vs three components 180/381 match, 201/381 mismatch. Both mismatches begin 2010-01. Cause not established.
- Added nine-series component audit script `qa/audit_brazil_bop6_portfolio_components.py` (commit 881425f4c7706051f7de0c8a55c34c891fa37105) and 3 tests (commit e94e48acc46f73a4cdb7108081ddcd276dfb9c88). Workflow now captures all nine SGS codes and runs component audit (commits b0dbd5f33fcc2e1a2815ed765aaab09adde21123, d5797a4842d0200a726e84d6a75e09e703d5ed34, bf423222d7624f9eec20044dee93996ca5906a2e).
- Runs #13 44280922280 and #14 44280941633 were in progress at ledger entry; runtime status pending. Inspect both; prioritize #14 as latest workflow integration.
- All flow admission remains NOT_AUTHORIZED. No source substitution, series shifts, splicing, synthetic repair or production integration.

- QA correction: Run #15's SGS component roll-up false-positive counts were caused by using 0.051 tolerance on one-decimal SGS values. Corrected SGS roll-up tolerance to 0.151 (max residual 0.10); archive/IMF remain 0.051. Cross-source comparisons stay 0.051. Script commit 21ba07f1ab17128cdb61ed8e2c025f1df3a51afa; regression test commit 8af623974a8c8dc22944a5e5ba30199acb66a783. Run #17 is the corrected runtime acceptance run.



## 2026-11-18 — Chapter 35 Part-7 runtime closeout: nine-series portfolio components
- Corrected Run #17 / ID 44281174648 SUCCESS; head 8af623974a8c8dc22944a5e5ba30199acb66a783; all 21 substantive steps passed. Artifact #14416138359, 7,784,632 bytes, SHA 599c639ccb5d7f35c5800858b289bb0f8668f1afb1ca23be1c164f048c12fbd7.
- Component audit JSON SHA 8cdc08da5e788f7fdf2d6f64d5e7f272aba22bd5d4b068d6b0cfd383a224335d. Permanent summary `docs/BRAZIL_BOP_PORTFOLIO_COMPONENT_AUDIT_20261118.json`, commit da7ed0a0a928d6a461c597019bf01d771ee55f6b.
- Corrected source-specific roll-up results: BCB archive assets/liabilities/net all 293/293 PASS; current SGS assets/liabilities/net all 381/381 PASS at 0.151 tolerance (max residual 0.10 due one-decimal source display); BCB-published IMF-SDMX assets/liabilities/net each 180/381 PASS and 201/381 FAIL from 2010-01 to 2026-09 at 0.051.
- Each of nine archive-to-IMF series has 180/293 matches for 1995-01–2009-12 and 113/293 mismatches for 2010-01–2019-05.
- First Run #15 SGS component rollup flags (128/115/96 mismatches) were false positives from using 0.051 on rounded SGS values; superseded by corrected Run #17. Correct tolerance is 0.151 for SGS rollups only; archive/IMF and cross-source comparisons remain 0.051.
- Next: official BCB/IMF source-lineage and revision matrix for all nine series, dataflow/domain/counterpart/vintage, and 2010-01 transition. Keep source-specific values separate and all admission gates NOT_AUTHORIZED.



## 2026-11-18 — Chapter 35 Part-8: IMF registration vs BCB payload Dataflow ID
- Official IMF registrations page lists the BCB URL under `IMF:BOP6(1.0)`, provider `IMF:BR1`, last updated 2026-10-26T11:47:29Z. The actual BCB XML Structure namespace says `IMF:BOP_BPM6(1.0)`. IMF constraints catalogue lists BOP6_CONSTRAINT -> BOP6 and BOP_BP6_CONSTRAINT -> BOP_BPM6. No alias/mapping is proven; exact relationship UNKNOWN.
- BCB Methodological Note 1 says BPM6 release began April 2015; prior releases since 2001 used BPM5. The observed divergence starts 2010-01, before BPM6 public release. This timing is a key source-lineage clue but does not establish the cause.
- BCB 2015 Administration Report says BCB retained gross flow compilation/publication for analytical value while aligning to BPM6. SGS 22905 metadata: BCB/Depec, monthly, US$ million, temporal coverage from 1995-01.
- Added `qa/audit_imf_bop6_registration_alignment.py` and three tests; commits e0515734c684defcd1d6b9c8b95710de0234d59f / ceac9031df02e851ec117a904e4edf5f3a9ffdf2. Workflow now captures registrations page, BOP6 dataflow/constraint, and compares to BOP_BPM6 metadata plus BCB payload namespace; commits 78b8bb9a5fd3b45093359af05e9fb1bd6a2bac64, 9b36aafd60cafafd6f3cab9a844c82e4e2631f8e, bd6a40540c4e24d6ca954241e125c5fa09973df7.
- Runs #18 (44281693103) and #19 (44281713846) precede final step integration. Await Run #20 to verify the registration alignment report and artifact.
- 2010-01 divergence remains BLOCKED/UNKNOWN; all flow admission remains NOT_AUTHORIZED.



## 2026-11-18 — Chapter 35 Part-8B: Constraint coverage blocker
- IMF raw registration HTML is client-rendered; downloaded page contains empty table body. Run #20 failed only because parser expected static rows. Not an IMF outage. Versioned official rendered-page snapshot saved at `config/imf_bop6_registration_snapshot_20261118.json`, commit 049b0b66d8736cc87d1ae60be7216d7c6387a2b0.
- Both live IMF Dataflows BOP6 and BOP_BPM6 reference ECOFIN_DSD 1.0. Their constraints differ: BOP6_CONSTRAINT allowed 4,313 indicators and covers 234/237 observed BCB codes (missing BMSOBL_USD, BSOBL_USD, BXSOBL_USD); BOP_BP6_CONSTRAINT allowed 98 and covers only 27/237 (210 observed codes outside constraint).
- Actual BCB XML uses BOP_BPM6; IMF registration catalogue lists BOP6 / provider BR1 / same BCB URL / updated 2026-10-26. Same DSD does not prove Dataflow alias. Constraint mismatch is a P0 metadata alignment blocker; no observations are rejected or admitted solely from this yet.
- Corrected alignment audit to read snapshot, parse both constraints and compare code coverage; script commit 29221dee9993a6d9042eb9c0d64aeafc68c3d485, tests commit b172e716d589d8fbb1576aa8b8e291b82910d077, workflow snapshot invocation commit 27e26095b482f24e65bafca69cca9d870922fffd.
- Run #20 ID 44281736564 FAIL at obsolete HTML parser; artifact #14417810859 preserves evidence. Run #21 was before final workflow invocation commit; Run #22 is acceptance run.
- Do not replace BOP_BPM6 constraint with BOP6 constraint without proving registration semantics. All flow admission remains NOT_AUTHORIZED.

- Raw Dataflow descriptions: BOP6 = “Balance of Payments (BPM6) for Collection”; BOP_BPM6 = “Balance of Payments -- BPM6”. Both use ECOFIN_DSD 1.0, but BOP6_CONSTRAINT covers 234/237 observed codes while BOP_BP6_CONSTRAINT covers 27/237. Registration uses collection Dataflow BOP6; BCB XML header declares BOP_BPM6. This is a scope/registration mismatch clue, not a proven alias or confirmed cause. Do not substitute constraints without official contract evidence.



## 2026-11-18 — Chapter 35 Part-8 runtime closeout
- Run #23 / ID 44282235752 SUCCESS; head 27e26095b482f24e65bafca69cca9d870922fffd; all 22 substantive steps passed. Artifact #14416443972, 7,835,957 bytes, SHA 53d377849e2bf6cdb7db384443076dd091658c04d02468d7a37a088ab66d55d0.
- Registration alignment report SHA e994a95813dc302091cfff286505a80b0db1bbf413ef13c596d07d8d5bf2b58f. Registry: IMF:BOP6(1.0)/IMF:BR1. BCB XML header: IMF:BOP_BPM6(1.0). Both Dataflows reference ECOFIN_DSD 1.0.
- BOP6 collection constraint: 4,313 allowed indicators, 234/237 observed covered, 3 excluded: BMSOBL_USD, BSOBL_USD, BXSOBL_USD. BOP_BPM6 constraint: 98 allowed indicators, 27/237 observed covered, 210 excluded. Descriptions differ (collection vs BOP BPM6). This is a P0 contract/constraint alignment blocker, not an alias proof.
- Permanent JSON summary docs/BRAZIL_BOP6_REGISTRATION_ALIGNMENT_AUDIT_20261118.json, commit ae7e7f41e7631640e222705b669670d579dbb2c0. Run #20 parser failure superseded by Run #23.
- Next: authoritative IMF registration/provision-agreement semantics; determine correct constraint for registered BCB source. No constraint substitution or flow admission before proof.


## 2026-11-18 — Chapter 35 Part-9: Strict execution discipline and verified Part-8 evidence
- User raised repeated-work/time/error risk. Adopted `docs/PRECISION_WIRES_RESEARCH_EXECUTION_PROTOCOL.md`: one atomic batch commit, source-hash reuse, no repeat of unchanged audits, pre-run source/schema checks, one consolidated ≤8-minute run, failed-step diagnosis before rerun, explicit PASS/FAIL/PARTIAL/UNKNOWN/NOT_RUN states, and no source substitution/synthetic data.
- Verified latest integrated runtime Run #23 / ID 44282235752, head 27e26095b482f24e65bafca69cca9d870922fffd, SUCCESS, 22 substantive steps; artifact #14416443972, 7,835,957 bytes, SHA-256 53d377849e2bf6cdb7db384443076dd091658c04d02468d7a37a088ab66d55d0. This is the integrated evidence baseline; do not rerun unchanged steps.
- Component report `evidence/brazil_bop/bpm6_monthly_archive/portfolio_component_audit.json`, SHA-256 8cdc08da5e788f7fdf2d6f64d5e7f272aba22bd5d4b068d6b0cfd383a224335d. Source-specific rollups: BCB archive 293/293 PASS for assets, liabilities and net; current BCB SGS 381/381 PASS at 0.151 million USD tolerance; BCB-published IMF-SDMX 180/381 PASS and 201/381 FAIL for each rollup, first mismatch 2010-01, last 2026-09. This is verified from Run #23; do not cite Run #12 as its evidence because Run #12 predates this audit.
- Nine series: archive-vs-IMF each 180/293 matches and 113/293 mismatches from 2010-01 to 2019-05. Archive-vs-SGS mismatches are vintage differences and must remain source-separated. SGS tolerance is 0.151 only for rounded SGS internal rollups; cross-source/archive and IMF comparisons remain 0.051.
- Registration report: Run #23 artifact `brazil_bop/bop6_registration_alignment.json`, SHA e994a95813dc302091cfff286505a80b0db1bbf413ef13c596d07d8d5bf2b58f. Registry BOP6 collection vs BCB payload BOP_BPM6 mismatch; BOP6 constraint covers 234/237; BOP_BPM6 constraint covers 27/237. Registration semantics/contract remains UNKNOWN; no constraint substitution.
- Workflow execution gate: only manual `workflow_dispatch` or consolidated commit message marker `[run-bop-audit]` launches the expensive run; workflow-file-only commits no longer trigger it; concurrency serialized per branch. Protocol and workflow update are committed atomically in this batch. No new data-acquisition run is required to verify this documentation/control-only patch.
- Admission remains NOT_AUTHORIZED for Brazil portfolio panel, Global EM aggregate and trading signal. Production invariants unchanged.


## 2026-11-18 — Chapter 35 Part-10: IMF Brazil registration/provision contract investigation (runtime pending)

### Reused verified baseline — no repeated source-data acquisition
- Previous accepted baseline remains Run #23 / ID 44282235752, commit 27e26095b482f24e65bafca69cca9d870922fffd, artifact #14416443972, SHA-256 53d377849e2bf6cdb7db384443076dd091658c04d02468d7a37a088ab66d55d0.
- Registration snapshot `config/imf_bop6_registration_snapshot_20261118.json`, blob SHA bb5b3f4d41b3d273cda9e76b9cd8990e4a4a7b74; exact observed row: IMF:BOP6(1.0), IMF:BR1, BCB URL, last updated 2026-10-26T11:47:29.000Z.
- Official IMF Data Providers catalogue identifies IMF:BR1 as Central Bank of Brazil. Official registrations catalogue shows BOP6(1.0) / BR1 / same BCB URL. Do not infer an alias with BOP_BPM6.

### Official SDMX semantics established from public IMF documentation
- SDMX Central overview says constraints may attach to Dataflow, Provision Agreement and Data Provider, and can cascade; this confirms the prior Dataflow-only audit was incomplete for contract interpretation.
- IMF Web Services Guide (last updated May 2025) documents public REST structure queries and explicitly lists `dataproviderscheme`, `provisionagreement`, and `contentconstraint` resources; REST query blueprint is `/sdmx/v2/structure/{resource}/{agencyID}/{resourceID}/{version}/{itemID}`, with `references=parents|all` options.
- Same guide says registration is a link between Dataflow, Data Provider and a URL; the registration request message also contains a ProvisionAgreement reference. Registration API is private/authenticated; do not attempt write/registration operations. Read-only public structure queries are the only intended action.
- Official references: https://sdmxcentral.imf.org/overview.html ; https://sdmxcentral.imf.org/data/provisionAgreements.html ; https://sdmxcentral.imf.org/organisations/dataproviders.html ; https://sdmxcentral.imf.org/data/registrations.html ; https://dsbb.imf.org/content/pdfs/IMFSDMXCentralWebServicesGuide.pdf .

### Focused, non-duplicative implementation
- Added `qa/audit_imf_brazil_bop_registration_contract.py`, three regression tests, and dedicated workflow `.github/workflows/imf_bop_registration_contract_audit.yml`. This workflow only queries the public registry structure metadata; it does not redownload IMF BOP observations or BCB source datasets.
- Unit tests completed SUCCESS in GitHub Actions Run #1 (ID 44286951595), head 599c87c1ff4469b31ac2f26b3d0bec20d46f1c76.
- At the last status inspection, Run #1 remained IN_PROGRESS at the official registry structure capture step; provider/provision/constraint parse and artifact upload had not yet completed. Therefore no real registry result is claimed. Runtime state: IN_PROGRESS; metadata contract result: NOT_RUN pending raw XML.
- Current run page: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/44286951595 .

### Guardrails and next action
- Do not interpret absence in a public structure query as proof that no private/unexposed agreement exists.
- Do not substitute BOP6_CONSTRAINT for BOP_BP6_CONSTRAINT; do not rewrite the BCB payload Dataflow; do not admit Brazil flow panel, Global EM aggregate or trading signal.
- Next: obtain Run #1 completion and raw structure artifact; inspect provider BR1 identity, any ProvisionAgreement whose StructureUsage/StructureProvider links BOP6 and BR1, and any ContentConstraint attached at provider or agreement level. If all-structure queries are too slow, switch to a targeted provider-scheme item query with `references=parents`, preserving the same 8-minute job cap and raw response hashes.


## 2026-11-18 — Part-10 Run #1 failure analysis and bounded-query correction
- GitHub Actions Run #1 / ID 44286951595 completed FAILURE; head 599c87c1ff4469b31ac2f26b3d0bec20d46f1c76. Unit-test step PASS; metadata capture step FAIL; parser step SKIPPED. Artifact #14419587288, 2,083,123 bytes, GitHub artifact digest SHA-256 7886e4a5ce6c852f295765dca893818046ba65fb852221093b138321afcc04f6.
- Downloaded artifact was inspected. Provider response: HTTP 200, 673,441 bytes, complete XML, SHA-256 01e86f8ecc0242adfcd16d5ba8d3ff971dcd6700384955c1f4315b3c1dbe8b96; provider BR1 resolves to “Central Bank of Brazil”. Provision Agreement response: HTTP 200, 41,901,260 bytes, SHA-256 d927c504950379fd04e340018dce69ec4fad01406046128b549d126cef5ecc50, but XML is truncated (ElementTree ParseError: no element found at line 260, column 992718). It was requested with references=all, which expanded the response with referenced structures and exceeded the capture window. Content Constraint query was not reached. Do not parse or use the truncated Provision Agreement XML as complete evidence.
- Corrective change: all three read-only registry structure queries now use references=none, preserving each structure's own references while avoiding expansion of referenced structures. Each request is bounded to 60 seconds, with one retry. Parser now fails closed with an explicit incomplete/malformed XML error and validates the SDMX root element. Added a regression test for truncated XML.
- This is a capture/runtime failure, not evidence that a Brazil Provision Agreement or provider constraint is absent. Actual agreement and provider-constraint semantics remain UNKNOWN / NOT_RUN until complete raw structures are captured and parsed.
- Next run is a focused metadata-only retry. No BOP observations, BCB archive, 237-code mapping or nine-series rollup will be reacquired. Admission gates remain NOT_AUTHORIZED.


## 2026-11-18 — Part-10 exact contract result: Brazil BOP6 Provision Agreement identified
- Accepted metadata-only runtime: Run #2 / ID 44288520760, head a335c44d236c71aff1c1f3812acecb8078ac73c5, SUCCESS; artifact #14420935493, 264,592 bytes, digest SHA-256 104bfa8b0cfe79bd4a3d60b41ebbd9a00335b979347aa7a897bb96616693db31. Run #3 / ID 44288554888 also completed SUCCESS on the same bounded-capture code; Run #2 is the inspected evidence artifact.
- Complete public IMF SDMX Central structure queries returned HTTP 200: provider scheme 26,382 bytes SHA-256 0865a1127fcc3c205bc3e21a4b55358183c5a923b953940fa6f0a67e548fb469; provision agreements 583,838 bytes SHA-256 beddaca5badb350e31cc44042ff5ecf4e1b97632d8c3b1c52ea10d5d266d0d07; content constraints 3,072,059 bytes SHA-256 ef4fa1e71ca09591f382f971965ed4b861b6f684105a55e480f6365ba2d8a48e. Captured 992 provision agreements and 84 content constraints.
- Provider scheme has exactly IMF:BR1 = Central Bank of Brazil.
- Exact Provision Agreement IMF:BR_BOP_BP6(1.0) / “Brazil Balance of Payments” exists and references Dataflow IMF:BOP6(1.0) AND Data Provider IMF:BR1. This matches the public registration row IMF:BOP6(1.0) / IMF:BR1 / BCB URL updated 2026-10-26T11:47:29Z. Registration and PA contract are confirmed aligned on BOP6 + BR1.
- Full current public ContentConstraint catalogue: 84 constraints; BOP6_CONSTRAINT is attached to Dataflow BOP6; BOP_BP6_CONSTRAINT is attached to Dataflow BOP_BPM6. No constraint attached to provider BR1 and no constraint attached to Provision Agreement BR_BOP_BP6 were found in the complete returned catalogue. The only provider-level constraint in the catalogue is attached to US3, not BR1.
- Thus the registered contract selects BOP6 and its BOP6 constraint, while the BCB payload header declares BOP_BPM6 and the BOP_BPM6 constraint is a distinct Dataflow constraint. This is a confirmed registration/PA-vs-payload Dataflow mismatch; alias semantics are not established. Do not rewrite header/registration or apply a constraint to the payload until authoritative BCB contract evidence resolves it. No Brazil flow panel, Global EM aggregate or trading signal admission.
- Run #1 failure was a capture-size issue caused by references=all (41.9 MB truncated PA response); superseded for metadata capture by Run #2's complete references=none evidence. Original artifact #14419587288 retained.
- Corrected parser now selects exact PA links and reports provider/PA/dataflow constraint attachment levels separately. Added tests for exact links, absent provider/PA constraints, wrong-provider mismatch, truncated XML and fail-closed registration identity. Next: execute corrected parser against archived Run #2 XML (no new download) and commit permanent JSON.


## 2026-11-18 — Part-10 exact contract audit closed (P0 payload mismatch remains)
- Corrected exact-reference parser ran successfully in GitHub Actions Run #4 / ID 44288831427, head 025c0e4f33a151fa6e097d15f6e89f6f6bab58eb, SUCCESS. All workflow steps PASS, including regression tests, three complete IMF public structure captures, exact parser, and artifact upload. Artifact #14419763992, 260,905 bytes, digest SHA-256 5c114648c17ba6cfd54319f3ddbcd0bd9e0f7583ccb974410128d0cf0dd6dfbe. Audit JSON SHA-256 d4448669f65bf99dc0990ffd468ce646f3be2c1e6b55cdda363f58be1799b504.
- Parser results: IMF:BR1 provider found exactly once; exact Provision Agreement IMF:BR_BOP_BP6(1.0) found exactly once, linking Dataflow IMF:BOP6(1.0) and Provider IMF:BR1. Registration row also BOP6 / BR1. Thus registration and PA contract alignment is CONFIRMED.
- Complete public ContentConstraint catalogue: 84 records. One constraint BOP6_CONSTRAINT attaches to BOP6; one BOP_BP6_CONSTRAINT attaches to BOP_BPM6. No provider-level constraint for BR1 and no PA-level constraint for BR_BOP_BP6 in the complete public catalogue. The only provider-level constraint observed is US_CONSTRAINT for US3.
- BCB payload header remains BOP_BPM6, so the registration/PA-vs-payload Dataflow mismatch is CONFIRMED. Alias semantics are NOT_ESTABLISHED. The current payload cannot be admitted under either constraint until BCB's authoritative contract resolves the mismatch. No source substitution, header rewrite, registration rewrite, or flow admission.
- Run #5 / ID 44288864477 also SUCCESS with duplicate artifact #14420152608 (260,910 bytes; digest SHA-256 dc2cfc4ebe636562041cc7eac2c31de0b58b2599887c40778060574e463ce996); same code/data capture, recorded as duplicate verification only, not independent evidence.
- Permanent machine-readable result: docs/BRAZIL_BOP_REGISTRATION_CONTRACT_AUDIT_20261118.json. Next: inspect the exact BCB-published XML header and official BCB technical metadata for its declared Dataflow ID and registration contract. Do not reacquire BOP observations or change production logic.


## 2026-11-18 — Execution lesson: duplicate workflow trigger avoided going forward
- Part-10 exact parser batch produced Run #4 (ID 44288831427) on commit 025c0e4f33a151fa6e097d15f6e89f6f6bab58eb and a second same-batch Run #5 (ID 44288864477) after a subsequent contents-API trigger write. Both succeeded; Run #4 is the inspected evidence artifact. Run #5 is duplicate verification only, not independent evidence.
- Root cause: a Git Data API ref update already dispatched Run #4; a follow-up contents-API workflow-path update dispatched Run #5. Do not issue a second trigger write without first checking the Actions run list for the target commit/workflow.
- Added section 8 “Trigger deduplication” to the research execution protocol. Future batches must use one deliberate trigger and immediately inspect existing runs before any further write.
