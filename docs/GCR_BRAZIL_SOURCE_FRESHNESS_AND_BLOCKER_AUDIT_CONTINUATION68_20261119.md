# GCR + Brazil Evidence Gate Audit — Continuation 68
Date: 2026-11-19 (Asia/Kolkata)
Scope: source freshness/schema gate audit using official CDSL pages and existing Brazil lifecycle evidence. Research-only; no production changes.

## Executive result
- GCR: Official CDSL sector-wise FPI report for 2026-11-01 to 2026-11-15 is publicly accessible. Daily investment freshness is inconsistent across CDSL pages: archive page reports investment data only through 2026-10-31; the dedicated daily page's investment table is dated 2024-08-30, while its derivative table is current through 2026-11-18. Therefore sector-flow route is available, but daily FPI investment acquisition is NOT current/accepted from these rendered pages.
- Brazil: Corrected continuity status. Exact Brazil Registration URN's 40-event lifecycle is already captured and independently cross-checked against global transaction index. Do not repeat it. Remaining Brazil blocker is the distinct Provision Agreement transaction ID 2 / Changelog payload, whose two documented JSON serializations both returned HTTP 500; dataflow identity mismatch BOP6 vs BOP_BPM6 remains unresolved.
- No 100% completion claim. GCR raw synchronized panel and Brazil PA changelog/dataflow reconciliation remain blocked.

## CDSL official source freshness audit
Official SEBI curation directory confirms:
- NSDL and CDSL daily latest, current month, archive, calendar-year and financial-year FPI routes.
- NSDL/CDSL fortnightly sector-wise FPI route.
Source: https://www.sebi.gov.in/curation/fpi.html

Exact CDSL pages inspected:
1. Archive: https://www.cdslindia.com/Publications/ArchiveDataAfter2009.aspx
   - Rendered heading: Daily Trends in FII/FPI Investments upto 31-Oct-2026.
   - Derivatives section on same page also shows upto 31-Oct-2026.
   - Contains gross purchases, gross sales, net INR crore, net USD million, conversion rate, asset class and investment route.
2. Dedicated daily page: https://www.cdslindia.com/Publications/FIIDailyData.aspx
   - Investment section is dated 30-AUG-2024.
   - Derivatives section is dated 18-NOV-2026.
   - This is a clear field-level freshness mismatch; do not infer investment freshness from derivative freshness.
3. Landing page: https://www.cdslindia.com/Publications/ForeignPortInvestor.html
   - Page last updated 18-Nov-2026.
   - Daily investment links listed from 04-Apr-2025 backwards; the latest displayed link in the rendered section is not a 2026 daily file.
   - Fortnightly sector-wise reports are listed through 15-Nov-2026.
4. Latest sector report:
   https://www.cdslindia.com/publications/FII/FortnightlySecWisePages/Nov%2015%202026.html
   - Header explicitly distinguishes AUC as at 31-Oct-2026, net investment for 16–31-Oct-2026, net investment for 01–15-Nov-2026, and AUC as at 15-Nov-2026.
   - Sector rows include Auto, Capital Goods, Chemicals, Construction, Construction Materials, Consumer Durables, Consumer Services, Diversified, FMCG, Financial Services, Forest Materials, Healthcare, IT, Media, Metals & Mining, Oil/Gas, Power and other sectors.
   - This is a fortnightly sector-allocation source, not a daily flow series. Do not interpolate to daily.
   - Web rendering confirms table contents, but raw HTML bytes, file hash, complete table parser and independent row/column validator have not yet been archived in the repo.

## Data gate and interpretation
- The CDSL page labels gross purchase/sales/net by asset class and route. Preserve Equity, Debt, Debt-VRR, Debt-FAR, Hybrid, MF and AIF separately.
- Preserve Stock Exchange vs Primary Market & Others. These categories have different economic meanings; do not merge without a defined question.
- CDSL notes that confirmed FPI data is compiled from custodian/depository submissions and represents trades on/up to previous trading day(s); exchange provisional figures are distinct. Retain the reporting date and underlying trade date distinction.
- CDSL conversion note uses RBI reference rate on trading day, with immediately preceding working-day rate on bank holidays. Preserve supplied INR/USD values and conversion rate; do not re-convert or combine with a separate FX series.
- The fortnightly sector report's AUC is a position/stock, while net investment is a period flow. Never mix AUC with period flow or derive one from the other.
- Daily investment series currentness is NOT_ESTABLISHED from the inspected CDSL pages. NSDL official archive route remains to be captured and reconciled; NSE FII/FPI-DII cash-market file remains provisional and should be reconciled to custodian/depository-confirmed data.
- Current evidence status: SEBI route directory PASS; CDSL fortnightly sector report availability PASS; daily FPI investment freshness PARTIAL/BLOCKED; raw immutable archive NOT_DONE; parser/schema/hash validation NOT_DONE; NSE-vs-CDSL/NSDL reconciliation NOT_DONE; predictive edge NOT_DONE.

## Brazil — exact corrected status
- Exact Registration URN: `urn:sdmx:org.sdmx.infomodel.registry.Registration=IMF:D429E36CD161E2F2A34ECAF137994E89(1.0)`.
- Part 7 report: `docs/IMF_BRAZIL_REGISTRATION_HISTORY_PART7_20261119.md`.
- 40/40 history events retrieved; 40/40 transaction item ZIPs HTTP 200; 40/40 embedded SDMX-ML 2.1 documents parsed.
- Registration ID, PA reference and BCB URL match 40/40. Global transaction index has 38,668 records (IDs 1–38,668); 40/40 history IDs found and 40/40 millisecond timestamps + Registry Action values match exactly.
- First event tx667 at 2023-09-22T09:42:16.389Z; latest returned tx37877 at 2026-10-26T11:47:33.098Z.
- Distinct fields preserved: registry history Action=Replace for all 40; embedded SDMX RegistrationRequest@action=Information for all 40. Do not conflate.
- Remaining PA transaction ID 2 / Changelog probe: report `docs/IMF_BRAZIL_PA_TX2_ALTERNATE_SERIALIZATION_PROBE_PART2_20261119.md`; run 44493473476 SUCCESS as a probe, but both fusion-json and sdmx-json returned HTTP 500, 39-byte body `Unable to return transaction for id '2'`, SHA-256 `76c4819f18129eb81b5fab80dcf0641665f332b823864c2c09280efe21415825`.
- PA reference Dataflow `IMF:BOP6(1.0)` vs BCB payload `IMF:BOP_BPM6(1.0)` remains a distinct unresolved identity mismatch; compatibility counts BOP6 234/237 vs BOP_BPM6 27/237. No alias/rewrite/admission.
- Next Brazil action: pursue only the already documented official UI download route for tx2/PA revision changelog; if it requires authenticated owner-side export, preserve as external dependency. Do not repeat public tx2 JSON endpoint probes.

## Next highest-value actions
1. GCR: capture NSDL archive + CDSL fortnightly Nov-15 raw source files in a byte-capable runner, with raw response bytes, UTC retrieval time, HTTP headers, file hashes, row/column counts and parser QA. First test NSDL daily archive because CDSL investment freshness is stale/inconsistent. Do not use third-party scrapers as source evidence.
2. Reconcile NSE provisional daily FII/FPI and DII with depository-confirmed NSDL/CDSL where same scope/date/asset classes are available; explicitly model provisional/final revisions.
3. Brazil: owner-side official UI export for PA tx2 changelog and revisions; only then reconcile Dataflow identity and lifecycle.
4. No weights, EM aggregate, production integration, selector/score/pressure-fade/CORE-672/engine changes, or trade admission until all gates pass.

## Sources
- SEBI FPI directory: https://www.sebi.gov.in/curation/fpi.html
- CDSL archive: https://www.cdslindia.com/Publications/ArchiveDataAfter2009.aspx
- CDSL daily: https://www.cdslindia.com/Publications/FIIDailyData.aspx
- CDSL landing: https://www.cdslindia.com/Publications/ForeignPortInvestor.html
- CDSL sector report: https://www.cdslindia.com/publications/FII/FortnightlySecWisePages/Nov%2015%202026.html
- Brazil Part 7 lifecycle: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/blob/main/docs/IMF_BRAZIL_REGISTRATION_HISTORY_PART7_20261119.md
- Brazil PA tx2 Part 2: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/blob/main/docs/IMF_BRAZIL_PA_TX2_ALTERNATE_SERIALIZATION_PROBE_PART2_20261119.md

No production changes. ₹0. UNKNOWN is not PASS.
