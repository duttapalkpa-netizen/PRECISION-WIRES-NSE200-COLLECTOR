# ZAF Q2-2026 FX conversion methodology boundary — Continuation 127
Date: 2026-11-21
Status: ZAF PARTIAL / NOT PASS; asset comparison REVIEW remains unresolved.

## 1. Preflight and prior-work reuse
- Re-fetched current Master Continuity Ledger, blob SHA `c2b4bf75acad32a2999a9baae3102716b7cef9f2`.
- Re-fetched GCR Priority Queue, blob SHA `bf720dc4590c1b781e2abe2ac706494eed295f93`.
- Re-fetched immutable 63-country Q2 cohort, blob SHA `1f767e22095865c8e5f87c2cfca55d9104b91e3e`.
- Reopened ZAF prior reports:
  - Part-3 source gate, blob SHA `cc04872301871d5b11954df83997c7fcab05f685`.
  - Part-4 code-candidate/archive boundary, blob SHA `615e341e1657ec052b45de0e3093d3b916816485`.
  - 2026-11-20 numeric reconciliation, blob SHA `ececb23c04ed9e9500366cf0fdc300bf92dab535`.
- Reused archived IMF exact ZAF rows and SARB September-2026 Table KB502; no IMF query, no SARB table re-extraction, no cohort rebuild.
- Confirmed next high-priority unresolved country task is CHN detailed SAFE workbook inspection; existing CHN audit report blob SHA `0fbf24a0ef403e3076be22e911b924d4eefecf32`.

## 2. Existing numeric status (not recalculated)
From the existing ZAF reconciliation:
- Liabilities: SARB -9,023 Rm; conversion using OECD quarterly-average 16.4719712481963 ZAR/USD gives -547.779003742 USDm versus IMF -547.771649123 USDm; residual +0.007354619 USDm, previously marked PASS against the half-unit bound.
- Assets: SARB -68,769 Rm; after documented SARB sign interpretation, converted display +4,174.910152756 USDm versus IMF +4,174.854099361 USDm; residual -0.056053395 USDm, previously marked REVIEW because it exceeds the 0.0304 USDm half-R-million bound.
- SARB table note 4 sign semantics and instrument-component arithmetic were already checked. The above values are reused, not a new recalculation or acceptance.

## 3. New methodology boundary evidence
- IMF BPM6 currency-conversion principle: flows denominated in foreign currency are converted at the rate prevailing when flows take place; actual transaction rates are preferred; daily averages can approximate daily transactions; if unavailable, use the average for the shortest applicable period. For continuous flows, period average may be appropriate. Source: IMF BPM6 Chapter 3, paragraphs 3.104–3.105: https://www.elibrary.imf.org/display/book/9781589068124/ch03.xml
- IMF BPM6 para 3.106 further says derived measures should in principle be built after converting underlying flows, rather than directly converting a derived aggregate from one currency into another. Source: same official IMF chapter.
- IMF BPM7 draft para 4.258 similarly prefers actual transaction rates, then daily averages, then the shortest period available; para 4.259 warns derived measures may differ across currencies because underlying flow timing and exchange-rate variation matter: https://www.imf.org/-/media/files/data/statistics/bmp7/draft-bpm7-chaptersonly-globcon-july-30.pdf
- The existing OECD Q2 quarterly-average exchange rate is a published reference series, but no SARB-specific Q2 portfolio-flow conversion instruction was found in the re-opened ZAF reports or current official source set. It is therefore not proven that multiplying a quarterly R-million aggregate by one quarterly-average ZAR/USD rate reproduces SARB's own USD compilation or IMF's country-reported USD observations.
- IMF South Africa BOP DQAF URL was opened, but the page returned only a generic shell/navigation and no country-specific BOP metadata text. It does not establish SARB's conversion practice. URL: https://dsbb.imf.org/sdds/dqaf-base/country/ZAF/category/BOP00
- SARB September 2026 bulletin page confirms Q2 portfolio investment was a net outflow, but that narrative is directional only and cannot explain the precise asset residual: https://www.resbank.co.za/en/home/publications/publication-detail-pages/quarterly-bulletins/quarterly-bulletin-publications/2026/september
- SARB's September 2026 downloadable BOP ZIP was previously identified, but Part-4 records that the ZIP retrieval timed out and no workbook bytes/hash were captured. The PDF table is official, but it does not disclose a detailed foreign-currency conversion methodology for this specific aggregate.

## 4. Decision
- SARB labels, codes, units, Q2 values, component arithmetic and sign note: PASS (existing evidence).
- IMF exact Q2 raw observations and source hashes: PASS (existing evidence).
- Liability numerical comparison using the prior quarterly-average conversion: PASS at the prior stated rounding bound, but conversion-method equivalence itself is not independently proven.
- Asset numerical comparison: REVIEW / OUTSIDE_ROUNDING_BOUND under the prior quarterly-average conversion.
- Quarter-average FX as the exact SARB/IMF conversion method: NOT_ESTABLISHED.
- ZAF full dual-leg national-source validation: PARTIAL / NOT PASS.
- 63-country aggregate: NOT_AUTHORIZED.

Important: this report does not replace the unresolved residual with a larger tolerance or label the quarterly-average method as validated. It explains why the current residual is not enough to infer an error or to force a PASS.

## 5. Next highest-value action
- Do not repeat ZAF IMF retrieval, SARB PDF extraction, or component arithmetic.
- Continue the existing Rank-1 63-country validation with CHN (China), whose open task is byte-preserving retrieval and inspection of the official SAFE Q2-2026 detailed BOP XLSX. Existing report: `docs/GCR_CHINA_CHN_SAFE_DETAILED_BOP_TIME_SERIES_ACCESS_AUDIT_20261120.md`.
- Recheck official SAFE URL through a supported byte-transfer route; if bytes become available, capture HTTP status, retrieval timestamp, byte count and SHA-256, then inspect workbook labels, definitions, unit, sign, vintage and Q2 observations. If still unavailable, preserve BLOCKED and move to the next executable high-weight cohort member without repeated retries.
- For ZAF, reopen only if SARB-specific conversion documentation, a USD-equivalent official quarterly series, or a transaction/monthly FX methodology becomes available. Do not use a generic quarter average as a universal conversion rule.

## 6. Protected constraints
₹0; official/free sources only. No synthetic observations, invented FX rates, widened tolerance, net-to-leg back-solving, silent sign/scale transformation, new IMF query, cohort rebuild, aggregation, or production changes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS.
