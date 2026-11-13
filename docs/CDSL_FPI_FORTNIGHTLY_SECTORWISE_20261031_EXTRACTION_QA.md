# CDSL FPI Fortnightly Sector-wise Report — 31 October 2026

## Acquisition status
- Official source: CDSL, Fortnightly Sector-wise FII/FPI Investment Data.
- Report date: 31-Oct-2026.
- Official page URL: https://www.cdslindia.com/publications/FII/FortnightlySecWisePages/Oct%2031%202026.html
- Reached from the 31-Oct-2026 item in CDSL's official FPI landing-page archive.
- Representation inspected: rendered HTML page. This is **not** a downloaded raw CSV/XLS/PDF archive; no raw-file byte count or SHA-256 is claimed.
- Scope: 24 sector/category rows plus Grand Total; AUC as of 15-Oct and 31-Oct; net investment for 01–15 Oct and 16–31 Oct 2026.
- Currency: INR crore and USD million as displayed by CDSL.

## Grand Total — key extracted values
| Measure | INR Cr | USD Mn |
|---|---:|---:|
| AUC as on 15-Oct-2026 | 7,346,751 | — |
| Net investment 01–15 Oct 2026 | -45,828 | -4,821 |
| Net investment 16–31 Oct 2026 | 21,354 | 2,243 |
| AUC as on 31-Oct-2026 | 7,284,170 | — |

AUC component columns (INR Cr), in CDSL order Equity, Debt-General, Debt-VRR, Debt-FAR, Hybrid, MF-Equity, MF-Debt, MF-Hybrid, MF-Solution-Oriented, MF-Other, AIF:
- 15-Oct opening AUC: 6,594,378; 203,478; 152,842; 323,967; 56,597; 11,388; 891; 259; 0; 2,914; 37. Sum = 7,346,751.
- 31-Oct closing AUC: 6,525,808; 205,978; 153,461; 319,246; 55,420; 19,465; 888; 160; 0; 3,711; 33. Sum = 7,284,170.

Net investment component columns (INR Cr), same category order:
- 01–15 Oct: -47,955; 3,377; -559; -751; -117; 168; -19; 5; 0; 23; 0. Sum = -45,828.
- 16–31 Oct: 13,112; 3,958; 901; -6,235; -180; 9,554; -1; -98; 0; 343; 0. Sum = 21,354.

USD million component checks:
- 01–15 Oct: -5,044; 355; -59; -79; -12; 18; -2; 0; 0; 2; 0. Sum = -4,821.
- 16–31 Oct: 1,377; 416; 95; -655; -19; 1,003; 0; -10; 0; 36; 0. Sum = 2,243.

## Arithmetic QA
- PASS: 15-Oct AUC category components sum exactly to displayed Grand Total 7,346,751 INR Cr.
- PASS: 31-Oct AUC category components sum exactly to displayed Grand Total 7,284,170 INR Cr.
- PASS: 01–15 Oct net-investment components sum exactly to displayed Grand Total -45,828 INR Cr and -4,821 USD Mn.
- PASS: 16–31 Oct net-investment components sum exactly to displayed Grand Total 21,354 INR Cr and 2,243 USD Mn.
- PASS: CDSL labels the period columns explicitly; no daily observations are inferred from this fortnightly report.

## Methodology and comparability cautions
- CDSL says Debt-VRR net investment and AUC are included w.e.f. 30-Apr-2020.
- Debt-FAR, Mutual Funds and AIF AUC are included w.e.f. 31-Aug-2024; their net investment is included w.e.f. 15-Sep-2024.
- USD conversion note: CDSL says the site’s FPI net-investment USD conversion uses daily RBI reference rates, while this report uses the period-end RBI reference rate for conversion. Do not treat the USD values as directly interchangeable with daily-rate-converted series.
- CDSL says sector classification follows BSE's common industry classification; investment outside the roughly 4,800 classified issuers is placed in “Others”.
- This fortnightly sector/AUC report is a separate frequency/product from the daily confirmed FPI series and from NSE provisional daily FII/FPI figures. Do not backfill daily data or merge series without a separately specified reconciliation method.

## Provenance and limitations
- Source is an official CDSL HTML report reached through its official FPI landing page.
- The web-rendered page exposes the table and notes; raw source bytes were not downloaded in this task. Therefore no raw archive checksum, file schema, or binary acquisition status is asserted.
- This is research-only evidence. No production selector, ranking score, pressure-fade rule, diagnostics, or hard gate was modified.
- No spend; no paid source; no external contact; no PR or merge.

## Next data task
Acquire the next adjacent fortnightly CDSL report (15-Nov-2026 when published) using the same official route, then compare the overlapping AUC endpoint and validate period net-investment arithmetic. Separately pursue raw daily CDSL archive acquisition; this report does not close that gap.
