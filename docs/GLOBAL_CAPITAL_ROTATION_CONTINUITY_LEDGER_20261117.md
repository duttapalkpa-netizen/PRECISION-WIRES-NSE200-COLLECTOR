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