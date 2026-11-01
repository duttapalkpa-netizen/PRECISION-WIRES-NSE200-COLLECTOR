# MoSPI IIP Public Aggregate Live Smoke — 2026-10-31

## Official source verified
- PIB release: https://www.pib.gov.in/PressReleseDetailm.aspx?PRID=2329475&lang=1&reg=3
- Published: 28 October 2026, 16:00 IST
- Reference period: September 2026
- IIP base: 2022-23=100
- Series: Output PPI deflator
- Headline IIP growth: 6.7% year-on-year
- Sectoral growth: Mining -6.2%; Manufacturing 7.6%; Electricity & Gas 11.2%; Water/Sewerage/Waste 5.8%.
- Manufacturing NIC-2-digit and use-based tables are included in the public release; detailed data is also linked to e-Sankhyiki.

## Implemented test
A bounded, unauthenticated public HTML capture saves the exact raw release, extracted HTML tables, SHA-256, final URL, HTTP metadata and retrieval timestamp. It does not request or store credentials. Offline parser tests and a 5-minute GitHub Actions live-smoke workflow are added.

## Interpretation boundary
A successful run proves the PIB public release page can be fetched and preserved and that required release markers exist. It does NOT prove e-Sankhyiki CSV/API ingestion, complete historical back-series, normalized factor coverage, or promotion of macro_indicators. The artifact explicitly records these limitations. Quick estimates must retain release vintage because subsequent releases revise earlier months.

## Promotion gate
Keep macro_indicators unpromoted until the collector has normalized the detailed e-Sankhyiki dataset (or a validated official release table), verified keys/units/frequency/base/period/revision metadata, and passed domain QA on a non-empty time series.
