# GCR — alternate national BOP source coverage map (2026-11-19)

## Purpose and scope
The IMF G200 quarterly panel has 154 members, but its official IMF P_F panel has 40 countries with no observations for either A_NFA_T or L_NIL_T, three one-sided countries (DZA assets only, ETH assets only, ZWE liabilities only), and 13 country-entry series with internal gaps. This source map identifies official national/regional BOP sources for a first repair cohort. It is a source-discovery result only; it does not populate the IMF panel or authorize a proxy aggregate.

## Priority cohort A — eight zero-data WAEMU members
The existing country-readiness file confirms all eight WAEMU members below are NO_DATA in the current IMF panel:
BEN Benin; BFA Burkina Faso; CIV Côte d'Ivoire; GNB Guinea-Bissau; MLI Mali; NER Niger; SEN Senegal; TGO Togo.

BCEAO's official Balance des paiements publication page lists country reports for 2024 for seven members (Benin, Burkina Faso, Côte d'Ivoire, Guinea-Bissau, Mali, Senegal and Togo) and a Niger 2023 report. BCEAO states that each national directorate produces an annual BOP report, reviewed by the national BOP committee and published by BCEAO. The reports are prepared on BPM6 basis; values are expressed in CFA francs and rounded to one decimal in the Côte d'Ivoire report. These are annual national-source benchmarks, not quarterly series and not a replacement for IMF quarterly P_F keys.

Official index: https://www.bceao.int/fr/publications/balance-des-paiements
2024 country pages:
- CIV: https://www.bceao.int/fr/publications/balance-des-paiements-et-position-exterieure-globale-de-la-cote-divoire-2024
- BEN: https://www.bceao.int/fr/publications/balance-des-paiements-et-position-exterieure-globale-du-benin-2024
- GNB: https://www.bceao.int/fr/publications/balance-des-paiements-et-position-exterieure-globale-de-la-guinee-bissau-2024
- SEN: https://www.bceao.int/fr/publications/balance-des-paiements-et-position-exterieure-globale-du-senegal-2024
- BFA: https://www.bceao.int/fr/publications/balance-des-paiements-et-position-exterieure-globale-du-burkina-2024
- MLI: https://www.bceao.int/fr/publications/balance-des-paiements-et-position-exterieure-globale-du-mali-2024
- TGO: https://www.bceao.int/fr/publications/balance-des-paiements-et-position-exterieure-globale-du-togo-2024
- NER: the index currently surfaces a Niger 2023 BOP report; a 2024 Niger report was not identified in the current index inspection.

Direct report evidence opened:
- CIV 2024 PDF: https://www.bceao.int/sites/default/files/2026-09/Balance_des_Paiements_et_Position_Ext%C3%A9rieure_Globale_2024-C%C3%B4te_d-Ivoire.pdf (63 pages). The report states BPM6 basis and includes current, capital and financial accounts, plus a detailed annual BOP table. The report's financial-account table must be mapped carefully to IMF net acquisition of financial assets and net incurrence of liabilities; do not equate the BCEAO "optique" financial-account balance to either leg without a line-item bridge.
- BEN 2024 PDF: https://www.bceao.int/sites/default/files/2026-09/Balance%20des%20Paiements%20et%20Position%20Ext%C3%A9rieure%20Globale%202024%20-%20B%C3%A9nin.pdf (78 pages).
- SEN 2024 PDF: https://www.bceao.int/sites/default/files/2026-09/Balance%20des%20Paiements%20et%20Position%20Ext%C3%A9rieure%20Globale%202024%20-%20S%C3%A9n%C3%A9gal.pdf (66 pages).
- BFA 2024 PDF: https://www.bceao.int/sites/default/files/2026-09/Balance%20des%20Paiements%20et%20Position%20Ext%C3%A9rieure%20Globale%202024%20-%20Burkina.pdf (91 pages).
- GNB PDF URL is listed on the BCEAO page; the web retrieval exceeded the 15 MB content cap, so preserve as NOT_DOWNLOADED until a bounded official download is archived.

BCEAO bulletin supplement:
- March 2026 quarterly statistical bulletin contains Côte d'Ivoire BOP table with annual 2021–2025 values (2025 marked provisional), in CFA billions. Official PDF: https://www.bceao.int/sites/default/files/2026-06/Bulletin-Trimestriel-des-Statistiques-mars-2026.pdf.
- This is annual BOP data in a quarterly bulletin, not a full quarterly country time series.

## Priority cohort B — UAE, Kenya, Oman (zero-data IMF panel members)
- ARE UAE: IMF DSBB country metadata updated 2026-10-28 says BOP is currently compiled and disseminated annually; quarterly compilation/dissemination is planned, though some components are collected/compiled quarterly. The 2025 annual data was first submitted confidentially to IMF in 2026; public dissemination is approximately six months after period end. Do not classify UAE as quarterly-ready. Official DSBB: https://dsbb.imf.org/e-gdds/dqaf-base/country/ARE/category/BOP00.
- KEN Kenya: Central Bank of Kenya has an official BOP statistics page with an annual BOP statement and a BOP Annual table. Its June 2026 Statistical Bulletin provides a BPM6-format annual BOP table for 2022–2025 (KES millions). Its Q4 2025 Quarterly Economic Review includes quarterly BOP information (USD millions), and its August 2026 Monthly Economic Indicators include a cumulative-12-month analytical BOP statement. These vintages/frequencies/units differ and require separate validation. Official pages:
  - https://www.centralbank.go.ke/statistics/balance-of-payment-statistics/
  - https://www.centralbank.go.ke/uploads/statistical_bulletin/75890805_Statistical%20Bulletin%20-%20June%202026.pdf
  - https://www.centralbank.go.ke/uploads/quarterly_economic_review/1446337670_Q4%202025.pdf
  - https://www.centralbank.go.ke/uploads/monthly_economic_indicators/1440098731_Monthly%20Economic%20Indicators%20August%202026%20-%20Final%20Draft.pdf
- OMN Oman: Central Bank of Oman official Open Data page lists a Balance of Payments dataset with XLSX and CSV download formats. Actual data bytes, frequency, series definitions and vintage have not yet been retrieved; mark SOURCE_LISTED / DATA_NOT_YET_CAPTURED. Official page: https://cbo.gov.om/Pages/BalanceDetails.aspx.

## Required mapping and validation before any data admission
For every country source:
1. Archive exact original PDF/XLSX/CSV bytes, official URL, retrieval UTC, HTTP status, byte count and SHA-256.
2. Record publication vintage, revision/provisional flags, frequency, period, currency, scale and source table/page.
3. Map financial-account component lines to IMF A_NFA_T and L_NIL_T independently. Do not substitute total financial-account balance, current account, overall balance, IIP stocks or reserves.
4. Reconcile sign convention, net/gross presentation, BPM5/BPM6 basis and coverage; maintain an explicit crosswalk with formula and unresolved residual.
5. Annual reports may validate annual rollups only. Do not interpolate quarterly values, forward-fill, convert currencies without an approved source FX methodology, or manufacture observations.
6. Retain country-entry-period-level PASS/REVIEW/BLOCKED/UNKNOWN states. No country enters an EMDE aggregate until both legs, aligned periods, scale/sign, and vintage pass.

## Acceptance status
- Source discovery: PARTIAL PASS (official national/regional sources found for 11 of the 40 zero-data members: 7 WAEMU 2024 reports + Niger 2023; UAE annual source; Kenya annual/quarterly sources; Oman BOP XLSX/CSV listing).
- Source byte archival and IMF A_NFA_T/L_NIL_T exact-key reconciliation: NOT_DONE.
- Quarterly coverage recovery: NOT_DONE.
- Full 154-member aggregate: BLOCKED / NOT_AUTHORIZED.
- No synthetic data, no production/backtest admission, no universal scale/sign inference. UNKNOWN is not PASS; research spend ₹0.
