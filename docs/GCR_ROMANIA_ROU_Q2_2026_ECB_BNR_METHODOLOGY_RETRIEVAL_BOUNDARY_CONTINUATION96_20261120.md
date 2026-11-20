# Romania ROU Q2-2026 — ECB/BNR Portfolio Flow Methodology & Retrieval Boundary
Date: 2026-11-20 (Asia/Kolkata)
Continuation: Research verification 44, Part-2
Decision: **New official methodology findings PASS; national portfolio coverage limitation identified; Q2 raw data still NOT_CAPTURED; ROU PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.**

## 1. Continuity / excluded repeats
- Re-fetched Master Continuity Ledger (blob SHA `c63e739e3711bd7624ba738f4cb66185e1b2a468`), GCR Master Priority Queue (blob SHA `278bdc6288c99663aaccf81223d682966f0f7bdb`) and Continuation 95 report (blob SHA `37f744511aeab33539d1fca15be0bce08536cd90`).
- Reused the fixed 63-country Q2-2026 cohort and existing IMF raw archive. No cohort rebuild, no new IMF query, no repeat NPL XLSX attempt.
- Continued only ROU's unresolved national-source route and methodology boundary.

## 2. New official methodology findings
### IMF Romania DSBB / DQAF
- BNR/NBR is the responsible compiler.
- Romania BOP is largely BPM6; monthly and quarterly dissemination is described, with quarterly release approximately 85 days after quarter end.
- The DSBB metadata states portfolio investment coverage is partial because information from external custodians is not totally available. This is a material national-source coverage caveat; a matching rounded number alone cannot remove it.
- Official metadata also says the NBR statistics site offers an Interactive Database (Balance of payments) and Statistics – Data Sets (Balance of payments and international investment position). Those interactive controls were not operated and no download receipt was obtained in this continuation.

### ECB 2025 BOP/IIP e-book — Romania-specific portfolio method
- The Romania row in section 7.3 (compilation methods) states: monthly stocks are collected security-by-security and monthly flows are derived security-by-security; the central bank application derives flows from the difference between current and previous stocks and separately compiles price changes, exchange-rate changes and other changes.
- For assets, reference data are extracted from the ECB CSDB.
- Non-ISIN securities are collected under Regulation (EU) No 1011/2012; the metadata says non-ISIN transactions with non-residents are negligible.
- Romanian debt instruments purchased by non-residents and held by external custodians are not covered.
- The residual approach is used for liabilities; the difference between domestic issuances and resident holdings of resident-issued securities is allocated to Rest of World. SHSDB information from euro-area resident custodians has also been used since 2020.
- Therefore the ECB monthly “summed through period” transaction series must not be treated as simple directly reported cash transactions. Its underlying Romanian portfolio-flow methodology is stock/valuation/other-change derived. A quarterly observation is acceptable only if the official series itself supplies the quarter or the official method allows a valid quarterly aggregation from the underlying monthly flow observations with vintage/valuation treatment understood.

## 3. Exact retrieval attempts and current boundary
- Official ECB Data Portal asset series page opened:
  `BPS.M.N.RO.W1.S1.S1.T.A.FA.P.F._Z.EUR._T.M.N.ALL`.
  It reports unit = EUR million, monthly, collection indicator = “Summed through period”, but page last-updated field = 17-Apr-2026 and source field = ECB. This is not an admitted Q2 national observation.
- Official ECB Data Portal liability series page for the corresponding key returned HTTP/tool-level 503 when opened in this continuation. Earlier official RON liability series metadata identified BNR as source and “Summed through period”; its last-updated field was 21-May-2026.
- The ECB API endpoints were re-opened exactly for the EUR asset and liability series over 2026-04 to 2026-06. Both remain inaccessible via the current web retrieval bridge. No CSV response bytes, response headers, data rows, retrieval receipt, or SHA-256 were captured.
- A search index showed the EUR liability series in a BPS catalogue updated 20-Oct-2026, but the individual series page/API bytes were not retrieved. Do not use the index update date as proof of the series observation vintage or data content.
- A container byte-download retry did not produce a file; do not claim a raw capture.
- No national Q2 numeric values are admitted. No inferred FX conversion, no netting, no stock-as-flow, and no IMF comparison was performed.

## 4. Gate matrix
| Gate | Status |
|---|---|
| Fixed 63-country Q2 cohort membership | PASS (reused) |
| BNR compiler / BPM6 / release metadata | PASS |
| BNR partial portfolio coverage caveat | PASS (documented) |
| ECB Romania portfolio compilation method | PASS (documented) |
| ECB asset-series key and metadata | PASS (metadata only) |
| Asset series current Q2 raw observations | NOT_CAPTURED |
| Liability series current Q2 raw observations | NOT_CAPTURED |
| ECB API byte capture / headers / SHA-256 | BLOCKED |
| National external-custodian portfolio coverage completeness | PARTIAL / NOT_ESTABLISHED |
| Q2 period/vintage and monthly aggregation basis | NOT_ESTABLISHED |
| Separate national asset/liability numeric comparison | NOT_DONE |
| ROU full national validation | PARTIAL / NOT PASS |
| 63-country aggregate / production | NOT_AUTHORIZED |

## 5. Decision and next action
- Close the current ECB web/API retrieval route for ROU; do not repeat identical endpoint attempts without a genuinely new supported retrieval mechanism.
- Keep ROU PARTIAL / NOT PASS. The national source's documented coverage limitation must remain visible even if future numeric comparisons fall within display rounding.
- ROU may be revisited only after a supported BNR Interactive Database / Data Sets export or a verified ECB byte-preserving API route supplies both legs, raw bytes, exact vintage, and methodology needed to understand derived monthly flows and coverage.
- Advance the fixed cohort to the next eligible unvalidated country in a separate continuation only after preflighting its national-source report and confirming the exact country is in the existing cohort. No IMF re-query or cohort rebuild.

## 6. Official evidence
- IMF Romania DSBB/DQAF: https://dsbb.imf.org/sdds/dqaf-base/country/ROU/category/BOP00
- ECB 2025 BOP/IIP e-book, section 7.3, Romania portfolio compilation row: https://www.ecb.europa.eu/press/pubbydate/2025/html/ecb.bopiipbook202507.pt.html
- ECB BPS Romania monthly asset series: https://data.ecb.europa.eu/data/datasets/BPS/BPS.M.N.RO.W1.S1.S1.T.A.FA.P.F._Z.EUR._T.M.N.ALL
- ECB BPS Romania monthly liability series: https://data.ecb.europa.eu/data/datasets/BPS/BPS.M.N.RO.W1.S1.S1.T.L.FA.P.F._Z.EUR._T.M.N.ALL
- ECB BPS revision policy: https://data.ecb.europa.eu/data/datasets/BPS/data-information
- ECB API asset endpoint: https://data-api.ecb.europa.eu/service/data/BPS/BPS.M.N.RO.W1.S1.S1.T.A.FA.P.F._Z.EUR._T.M.N.ALL?startPeriod=2026-04&endPeriod=2026-06&format=csvdata
- ECB API liability endpoint: https://data-api.ecb.europa.eu/service/data/BPS/BPS.M.N.RO.W1.S1.S1.T.L.FA.P.F._Z.EUR._T.M.N.ALL?startPeriod=2026-04&endPeriod=2026-06&format=csvdata

## 7. Protected invariants
No cohort rebuild, no IMF re-query, no synthetic data, no unverified monthly aggregation, no inferred sign/scale/FX, no stocks-as-flows, no netting, no production changes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS. Research spend ₹0.
