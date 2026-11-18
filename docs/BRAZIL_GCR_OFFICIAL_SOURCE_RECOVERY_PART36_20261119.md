# Official Source Recovery Checkpoint — Brazil Reconstruction + Global Capital Rotation Part-36
Date: 2026-11-19 (Asia/Kolkata)
Branch: qa/imf-brazil-parser-schema-path-hardening
Status: source discovery and contract verification only; no false completion claim.

## 1. Brazil — official endpoint verification
### IMF registry
- Official registrations listing: https://sdmxcentral.imf.org/data/registrations.html
- Current listing search result shows IMF:BOP6(1.0), provider IMF:BR1, BCB URL https://www.bcb.gov.br/content/statistics/sddsdocuments/4%20External%20Sector/Ext%201%20IMF%20SDMX%20BOP%20BPM6.xml, Last Updated 2026-10-26T11:47:29.000Z.
- Official Provision Agreements UI: https://sdmxcentral.imf.org/data/provisionAgreements.html. UI exposes URN, URL, revisions, description, annotations, valid-from/to, References, Changelog, Export SDMX-ML 3.0 and Export Excel. Static extraction did not expose selected Brazil PA detail/changelog payload. Do not infer event chronology from UI controls.
- Official SDMX Transactions UI: https://sdmxcentral.imf.org/activity/activity-log.html. It exposes transaction time/type/action and Download Transaction. Static extraction did not expose Brazil/BR1 event payload; user-authenticated/interactive export may be required. No registry mutation or login attempted.
- BCB live XML direct retrieval via browser failed with fetch error (400 OK); no HTTP body/headers/raw bytes/hash available in this run. This is a retrieval-tool boundary, not a BCB source failure.
- Prior archive proof remains: Brazil PA IMF:BR_BOP_BP6(1.0) StructureUsage IMF:BOP6(1.0), provider IMF:BR1. Prior BCB payload evidence declares IMF:BOP_BPM6(1.0). Distinct IDs remain unresolved. Do not map them without authoritative mapping/structure comparison or registry event history.

### BCB SGS 22707
- Official dataset: https://dadosabertos.bcb.gov.br/dataset/22707-balanca-comercial---balanco-de-pagamentos---mensal---saldo
- Dataset defines monthly USD million, source BCB Statistics, expected timeliness up to four weeks; the goods-balance concept includes BCB adjustments to MDIC/Siscomex trade data.
- Official JSON contract page: https://dadosabertos.bcb.gov.br/dataset/22707-balanca-comercial---balanco-de-pagamentos---mensal---saldo/resource/999ce9e2-ee0c-4910-b4f9-0a1d1fbdfa66
- It documents date filters dataInicial/dataFinal in DD/MM/YYYY and ultimos/{N}. Live endpoint remains DNS-blocked in prior local environment; current browser can open resource contract but exposes no response rows. Exact Sep-2026 primary value and raw SHA-256 remain NOT_VERIFIED. 6,869m remains SECONDARY_ONLY; official bulletin rounded ~6.9bn is not exact value evidence.

## 2. Global Capital Rotation — newly reverified official sources/contracts
- RBI Reference Rate Archive: https://rbi.org.in/scripts/ReferenceRateArchive.aspx — official archive has currency selector (USD, GBP, EUR, JPY, AED, IDR, RUB), date range and Excel download. This is a concrete route to replace community USD/INR mirror. Raw export/row count/hash not captured here.
- NSDL FPI Investments: https://pilot.fpi.nsdl.co.in/Reports/ReportsListing.aspx — official portal lists current and archive FPI/DII, FPI net investment (calendar/financial year/quarter), top-10 country data, fortnightly sector FPI, AUC country/category/client, debt utilisation, trade-wise equity/debt. Page fetch timed out in web retrieval; source discovery verified, raw export not captured.
- U.S. Treasury daily nominal curve: https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve — daily CSV/XML and maturity series.
- U.S. Treasury daily real curve: https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_real_yield_curve — daily CSV/XML; real curve is published as TIPS par real yields.
- EIA Europe Brent daily history: https://www.eia.gov/dnav/pet/hist/RBRTED.htm — official historical series discovered.
- IMF PIP (formerly CPIS): https://data.imf.org/Datasets/PIP — official portfolio positions by counterpart economy, annual/half-yearly/semester frequency; useful for structural positions, NOT a substitute for daily FPI flow.
- BCB external sector monthly goods balance dataset remains official source for Brazil/India macro external-balance overlay input.
- DXY official source qualification, cross-currency basis/carry, India G-Sec/FBIL yield series, CDSL final daily flow archive, AMFI category flow/AUM archive, NSE VIX historical files, CBOE volatility source, official geopolitical event extraction, and ETF creation/redemption raw archive still require dedicated source+download validation.

## 3. Important modelling boundaries
- RBI reference rates are official reference observations, not necessarily executable spot or cross-currency basis.
- NSDL FPI net flows and AUC/holdings are different measures; AUC changes include valuation effects and cannot be treated as net purchases.
- IMF PIP/CPIS is portfolio position data at annual/half-yearly/semester frequency, not daily flow.
- Treasury nominal and TIPS real curves are separate source series; preserve methodology and series-break metadata.
- EIA Brent does not complete all broad commodities/freight.
- No DXY proxy, mirror, or inferred cross-currency carry is promoted to official.
- Do not infer sector/stock beneficiaries from macro headlines without measured transmission and point-in-time tests.

## 4. Acceptance status
Brazil Reconstruction: INCOMPLETE/BLOCKED — registry-vs-payload Dataflow mismatch, BR1 registration/PA event history, live BCB XML byte archive, full pinned XSD closure/offline validation, and exact primary SGS value remain open.
Global Capital Rotation: INCOMPLETE/BLOCKED — official source discovery improved, but raw archives, all factor schemas, operational gates and overlay-specific point-in-time H+1/H+3/H+5 backtest/ablation remain open.
Combined 100% acceptance: NOT MET.

## 5. Next work units (bounded)
1. Browser/interactive export: select BR1 in IMF Data Registrations; download transaction history; select Brazil PA and export Changelog/Excel/SDMX-ML; hash exact exports.
2. Download BCB XML through normal network/browser and preserve exact response bytes/headers/hash; compare Header/ProvisionAgreement/StructureUsage with IMF registry snapshot.
3. Run a separate short acquisition for RBI USD reference archive and NSDL FPI/DII historical files; keep final vs provisional and flow vs AUC separate.
4. Acquire Treasury nominal+real curves and EIA Brent raw CSV/XML; archive metadata/hashes.
5. Continue CDSL/AMFI/NSE/FBIL/official DXY/UN/MEA/DGFT source qualification.
6. Implement the 35 factor contracts only after source coverage, units, timestamps, vintage, missingness and no-lookahead rules are explicit; then run rolling backtest and ablation.

## Invariants
₹0 spend, official free sources only; no synthetic data, fabricated timestamps, forward-fill of stale values, or unknown-to-pass conversion. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56x12), Engines A-E unchanged. PR #39 stays unmerged; no production integration or trading admission.
