# Official Source Acquisition Map — Brazil Reconstruction + Global Capital Rotation Part-36
Date: 2026-11-18 (Asia/Kolkata)
Branch: qa/imf-brazil-parser-schema-path-hardening
PR #39 remains open/draft/unmerged.

## Purpose
Turn known blockers into executable official-source acquisition paths. This is a source discovery and retrieval-boundary checkpoint; discovery does not equal raw-data acquisition or acceptance.

## A. Brazil Reconstruction
### IMF registry / PA
- Public IMF Registrations UI: https://sdmxcentral.imf.org/data/registrations.html
- Public Provision Agreements UI: https://sdmxcentral.imf.org/data/provisionAgreements.html
- Registrations UI exposes Registration ID, Registered URL, Dataflow, Data Provider; page includes SDMX-ML 3.0 export control. Static web extraction does not expose live table rows.
- Provision Agreements UI exposes URN, URL, Revisions, Description, Annotations, Valid From/To and Changelog/Export/Compare/View controls. UI confirms an available official changelog workflow, but current static extraction does not expose Brazil's selected PA record/revision history.
- The uploaded archive directly establishes PA IMF:BR_BOP_BP6(1.0) -> Dataflow IMF:BOP6(1.0), provider IMF:BR1. Prior captured BCB XML declares IMF:BOP_BPM6(1.0). Do not infer alias.
- Exact next browser action: select the Brazil PA URN in the official Provision Agreements page; export its full SDMX-ML and changelog/revisions. On Registrations/Activity page filter Data Provider IMF:BR1 and export full selected period transactions. Preserve downloaded bytes, response metadata, timestamp and SHA-256.
- Registration UI includes login; any authentication boundary must be recorded, not bypassed. No credentials requested or write action attempted.

### BCB XML and SGS
- BCB SDMX XML URL: https://www.bcb.gov.br/content/statistics/sddsdocuments/4%20External%20Sector/Ext%201%20IMF%20SDMX%20BOP%20BPM6.xml
- Fresh web retrieval returned an internal fetch error; no BCB HTTP status/headers/body bytes were captured. Container download also failed. This is an access/retrieval boundary, not a BCB source error.
- BCB External Sector statistics landing page is JavaScript-dependent in static retrieval.
- BCB SGS 22707 official open-data dataset documents JSON/CSV/WSDL/HTML resources, monthly frequency, USD million, coverage from 1995-01, and SGS code 22707: https://opendata.bcb.gov.br/dataset/22707-balance-on-goods---balance-of-payments---monthly---net
- SGS chart source: https://www3.bcb.gov.br/sgspub/consultarvalores/consultarValoresSeries.do?method=consultarGraficoPorId&hdOidSeriesSelecionadas=22707
- Exact Sep-2026 date-filtered JSON/CSV raw response and SHA-256 remain NOT_DONE due prior api.bcb.gov.br DNS block; 6,869m remains secondary-only. Bulletin rounded ~6.9bn is not exact series validation.
- Next: retry via normal DNS-capable browser/network; download JSON and CSV separately, record exact request URL, status, headers, retrieval timestamp, bytes and SHA-256; compare exact observation with official chart and bulletin.

### SDMX-ML schema
- Official XSD authority/index and pinned v2.1 tag documented in Parts 31–32. Need recursive dependency closure, all schema bytes and SHA-256, then offline validation against BCB XML. No code changes until source payload and exact schema error are captured.

## B. Global Capital Rotation — official source paths found
### GCR-01 / GCR-02 / GCR-08 flows, DII, MF/AUM
- SEBI FPI directory: https://www.sebi.gov.in/curation/fpi.html lists NSDL and CDSL latest/current-month/archive/yearwise reports.
- NSDL archive: https://www.fpi.nsdl.co.in/web/Reports/Archive.aspx
- CDSL daily FPI activity: https://www.cdslindia.com/eservices/publications/fiidaily
- NSE FII/FPI & DII report: https://www.nseindia.in/reports/fii-dii. NSE explicitly labels exchange FPI numbers provisional and points to NSDL/CDSL for final data.
- AMFI monthly: https://www.amfiindia.com/research-information/amfi-monthly; monthly PDF and Excel downloads are listed (including Sep and Oct 2026 in current page snapshot).
- SEBI mutual fund directory: https://www.sebi.gov.in/curation/mutual_funds_and_rtas.html links AMFI monthly/quarterly and AUM datasets.
- Required handling: preserve NSE provisional and depository-confirmed records as separate vintages; reconcile dates, segment and classification; do not treat FPI AUC changes as net flows; distinguish AMFI flow from AUM.

### GCR-03 FX
- RBI Reference Rate Archive: https://rbi.org.in/scripts/ReferenceRateArchive.aspx provides date-range search and Excel download.
- RBI official notice: since 2018-07-10 FBIL computes/publishes USD/INR, EUR/INR, GBP/INR, JPY/INR reference rates; RBI stopped publishing them from that date. FBIL portal: https://www.fbil.org.in/#/home
- DXY remains separate: qualify index administrator/licensing/source and raw-history availability before admission. Cross-currency basis/carry remains UNKNOWN unless a free official source is established.

### GCR-04 rates
- US Treasury nominal curve: https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve
- US Treasury real curve: https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_real_yield_curve
- Treasury historical CSV archive: https://home.treasury.gov/interest-rates-data-csv-archive/
- Treasury XML pagination guide: https://home.treasury.gov/treasury-daily-interest-rate-xml-feed (all-time paginated feeds; nominal since 1990, real since 2003).
- India G-Sec/FBIL yield source still requires a byte-captured official historical export and timestamp/revision audit; FBIL portal discovery alone is not ingestion.

### GCR-05 commodities
- EIA weekly Brent official historical series: https://www.eia.gov/dnav/pet/hist/rbrtew.htm
- World Bank Commodity Markets / Pink Sheet monthly and annual XLS: https://www.worldbank.org/en/research/commodity-markets
- Daily Brent and monthly Pink Sheet must remain distinct frequencies; no synthetic daily interpolation.

### GCR-06 / GCR-07 volatility, indices, TRI
- NSE historical reports: https://www.nseindia.in/static/resources/historical-reports-capital-market-daily-monthly-archives
- NSE all reports / historical index and India VIX data: https://www.nseindia.in/all-reports
- Acquire official history, index variant (price vs TRI), as-of-date constituents/weights, and source-level archive hashes.

### GCR-09 geopolitical / supply chain
- Official source candidates remain MEA, PIB, DGFT, UN sanctions and official port/customs notices. No complete timestamped event taxonomy or extracted factor history is established yet. Remains UNKNOWN.

### GCR-10 macro
- e-Sankhyiki CPI API: https://esankhyiki.mospi.gov.in/macroindicators?product=cpi&tab=api; open API documentation describes paginated records and optional bearer token for guest access.
- e-Sankhyiki IIP API: https://esankhyiki.mospi.gov.in/macroindicators?product=iip&tab=api
- e-Sankhyiki CPI catalogue exposes reference period, release date, table ID and provisional status; retain release vintage and base year.
- Additional WPI/BoP/reserves/trade official source acquisition and vintage joins remain outstanding.

## C. GCR factors, backtest and operational gate
- GCR-11: all 35 factor definitions need exact input fields, units, frequency, lookback, transform, winsorization/normalization, direction, missingness and no-lookahead rules. Do not create scores from partial inputs.
- GCR-12: point-in-time rolling regime-aware H+1/H+3/H+5 validation, ablation, confidence intervals and 0.22% transaction cost assumption per saved acceptance matrix. Must compare baseline vs overlay and test incremental value.
- GCR-13: immutable raw archives, manifest, raw-byte SHA-256, schema/version, publication/retrieval timestamps, stale/missing rejection, deterministic reruns and fail-closed UNKNOWN.

## Acceptance state after this checkpoint
- Official endpoint discovery expanded for flows, FX, US nominal/real yields, AMFI, NSE VIX/index history, EIA/World Bank commodities, MoSPI CPI/IIP APIs, IMF PA/changelog UI.
- No claim of complete raw ingestion, complete historical coverage, factor completion, event-study completion or production acceptance.
- Brazil Reconstruction remains INCOMPLETE/BLOCKED pending live BCB payload, official mapping/history, XSD validation and SGS primary data.
- Global Capital Rotation remains INCOMPLETE/BLOCKED pending raw-source archives, full 35-factor schemas, historical backtest and operational controls.
- Protected invariants unchanged. No paid APIs, synthetic values, inferred timestamps, production changes, merge or trading admission. UNKNOWN is not PASS.
