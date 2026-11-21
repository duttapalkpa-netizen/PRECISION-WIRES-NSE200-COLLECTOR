# Vietnam VNM — Q2-2026 official quarterly portfolio source closure (Continuation 124)
Date: 2026-11-21

## Decision
The prior VNM boundary audit (Continuation 59) was re-opened and its exact next action executed: search for a distinct official SBV quarterly BOP release, downloadable data table or documented API/export exposing Q2-2026 portfolio investment assets and liabilities separately. No such Q2-2026 official quarterly portfolio dual-leg publication was located in the inspected official SBV/NSO sources. SBV annual reports demonstrate separate portfolio asset/liability labels only through 2023 annual observations. The official NSO Q2/H1 and Q3/9M 2026 reports contain investment, FDI, securities-market and trade statistics but not BOP portfolio legs. IMF e-GDDS metadata search result states that no data are currently available on portfolio assets and liabilities; because the metadata page does not expose a visible update date in its static rendering, treat this as corroborative metadata, not proof of current 2026 publication status. VNM remains PARTIAL / NOT PASS; no numeric dual-leg comparison; aggregate NOT_AUTHORIZED.

## 1. Continuity preflight and duplicate rejection
- Re-fetched Master Ledger, pre-task blob SHA `7300a17c3ff68fdd3b78b9cf63b5832a03c0a339`.
- Re-fetched GCR Priority Queue, pre-task blob SHA `934ddf803e3561754dc7b256f7f993e926e66f20`.
- Re-fetched fixed 63-country cohort report, blob SHA `1f767e22095865c8e5f87c2cfca55d9104b91e3e`.
- Re-fetched VNM prior boundary audit, blob SHA `37c035bd784df75069ad77360a776e7040f0e26d`. Its explicit next action was the exact official quarterly route search completed here.
- No IMF query, no cohort rebuild, no duplicate national extraction, no annual-to-quarter allocation.

## 2. Official SBV and NSO evidence
- SBV Annual Report 2023 Appendix 4 (Balance of Payment): https://www.sbv.gov.vn/documents/d/sbv_portal/590044. Separate annual lines “Portfolio Investment Abroad: Assets”, “Portfolio Investment in Viet Nam: Liabilities”, and “Portfolio Investment (net)”; latest annual observations shown are 2022 and 2023, not Q2-2026.
- SBV Annual Report 2021 Appendix 4: https://www.sbv.gov.vn/documents/d/sbv_portal/532439. Separate annual asset/liability labels, observations 2020–2021 only.
- Official NSO Q2/H1 2026 press release: https://www.nso.gov.vn/en/data-and-statistics/2026/08/press-release-socio-economic-performance-in-the-q2-and-the-first-half-of-2026/ . It reports FDI, investment, securities-market and trade statistics; inspected sections do not publish BOP portfolio assets/liabilities.
- Official NSO Q3/9M 2026 press release: https://www.nso.gov.vn/en/data-and-statistics/2026/11/press-release-socio-economic-performance-in-the-q3-and-the-nine-months-of-2026/ . It likewise reports FDI, securities-market and trade aggregates, not separate BOP portfolio legs.
- NSO Statistical Yearbook 2024 defines the financial account as including portfolio investment, but the inspected source is a definitions/methodology description, not a Q2-2026 numeric series: https://www.nso.gov.vn/wp-content/uploads/2026/01/NG-TONG-CUC-2024_OKIN_Final.pdf
- IMF e-GDDS DQAF BOP metadata page: https://dsbb.imf.org/e-gdds/dqaf-base/country/VNM/category/BOP00 . Search-indexed metadata text says “No data are currently available on the capital account and on portfolio assets and liabilities.” The page's static rendering did not expose the metadata update date; this is corroborative, potentially legacy metadata, not definitive proof of 2026 publication status.
- Search for distinct official SBV Q2-2026 portfolio dual-leg release/data route returned no qualifying Q2 rows or API/export in the inspected results. Search absence is bounded to this audit; it does not prove no unpublished/internal dataset exists.

## 3. Sign and data boundary
- Annual SBV tables use separate asset and liability labels, but the inspected SBV primary evidence does not establish a current Q2-2026 sign crosswalk to IMF A_NFA_T and L_NIL_T.
- Prior audit's AMRO BPM5-sign note remains secondary context only; it cannot authorize a sign transformation.
- Do not substitute FDI, securities-market trading/capitalization, total foreign investment, goods/services trade, net portfolio investment, or annual data for quarterly portfolio asset/liability transactions.
- No raw Q2 national file exists to hash because no qualifying Q2 national dual-leg publication was located. IMF archived panel is not re-queried.

## 4. Updated gate matrix
| Gate | Status |
|---|---|
| VNM in fixed 63-country cohort | PASS |
| Prior VNM boundary audit and next action reviewed | PASS |
| SBV official annual portfolio asset/liability source family | PASS |
| Official Q2-2026 national portfolio assets | NOT_LOCATED |
| Official Q2-2026 national portfolio liabilities | NOT_LOCATED |
| Qualifying SBV quarterly Q2-2026 source/API/export | NOT_LOCATED |
| NSO Q2/H1 and Q3/9M official adjacent reports inspected | PASS; no qualifying portfolio legs |
| IMF metadata corroboration | LEGACY/UPDATE_DATE_UNKNOWN |
| Current Q2 sign convention | NOT_ESTABLISHED |
| National Q2 raw bytes/hash | NOT_APPLICABLE — qualifying source not located |
| Numeric dual-leg comparison | NOT_DONE |
| VNM validation | PARTIAL / NOT PASS |
| Aggregate authorization | NOT_AUTHORIZED |

## 5. Next cohort action
- Fixed roster places WSM (Samoa) after VNM. Proceed to WSM only after checking its prior report and source coverage; do not revisit VNM unless a new official Q2 dual-leg source or revision is published.
- No IMF re-query, no cohort rebuild, no annual interpolation, no sign/scale inference, no paid APIs, no production changes.

## 6. Protected invariants
₹0; official/free sources only. No synthetic data, fabricated timestamps, annual-to-quarter allocation, stock-as-flow, inferred sign transform, net-to-leg back-solving, IMF re-query, cohort rebuild or production changes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS.
