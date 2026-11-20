# Vietnam (VNM) Q2-2026 SBV Portfolio Source-Boundary Audit — Continuation 59
Date: 2026-11-20
Status: **OFFICIAL SOURCE FAMILY IDENTIFIED; Q2-2026 NATIONAL PORTFOLIO LEGS NOT PUBLISHED/NOT LOCATED IN INSPECTED SBV EVIDENCE; VNM PARTIAL / NOT PASS.**

## 1. Continuity and duplicate rejection
- Reopened the fixed 63-country Q2-2026 synchronous dual-leg cohort and current GCR master priority queue.
- Repository search found no dedicated VNM Q2-2026 national portfolio-flow validation report. VNM is a member of the existing 63-country cohort.
- Mexico (MEX) already has a dedicated Banxico dual-leg report; Argentina (ARG) has an INDEC dual-leg comparison; Thailand (THA) has an existing reconciliation script. These were rejected from duplicate work.
- Reused the existing IMF cohort/panel conceptually; no cohort rebuild and no IMF re-query were performed. This bounded task is a national-source boundary audit only.

## 2. Official SBV evidence inspected
- State Bank of Viet Nam (SBV) Annual Report 2023, Appendix 4 “Balance of Payment”, unit USD million, provides separate lines:
  - “Portfolio Investment Abroad: Assets”
  - “Portfolio Investment in Viet Nam: Liabilities”
  - “Portfolio Investment (net)”
- The table's latest displayed annual observations are 2022 and 2023. It is annual, not quarterly, and does not contain 2026-Q2 observations.
- The SBV Annual Report 2021 appendix independently uses the same separate portfolio asset/liability labels, but its observations are 2020 and 2021. It is also stale for Q2-2026.
- The SBV annual-report table demonstrates the official source family and the existence of separate asset/liability concepts; it does not establish Q2-2026 values, a quarterly publication route, or current sign methodology.
- The SBV Annual Report 2023 appendix is available at: https://www.sbv.gov.vn/documents/d/sbv_portal/590044 (Appendix 4, Balance of Payment; source SBV).
- SBV Annual Report 2021 appendix: https://www.sbv.gov.vn/documents/d/sbv_portal/532439 (Appendix 4).
- NSO Q2/H1 and Q3/9M 2026 socioeconomic reports were inspected as possible adjacent official sources. They report FDI, securities-market activity, trade and investment aggregates, but the inspected content does not provide separate BOP portfolio-asset and portfolio-liability transaction legs. These aggregates are not substitutes.
  - H1 2026: https://www.nso.gov.vn/en/data-and-statistics/2026/08/report-socio-economic-performance-in-second-quarter-and-the-first-half-of-2026/
  - Q3/9M 2026: https://www.nso.gov.vn/en/data-and-statistics/2026/11/press-release-socio-economic-performance-in-the-q3-and-the-nine-months-of-2026/

## 3. Sign-convention boundary
- SBV annual table labels assets and liabilities separately, but the inspected annual table alone does not document the exact sign convention needed to map each leg to IMF A_NFA_T and L_NIL_T.
- An AMRO 2026 report notes that Vietnam's BOP follows BPM6 while its financial-account sign follows BPM5. This is secondary analytical context, not a substitute for an SBV primary-methodology sign crosswalk; it is not used to transform any value.
- No sign flip, scale conversion, annual-to-quarter allocation, or inferred Q2 value is admitted.

## 4. Gate matrix
| Gate | Status |
|---|---|
| VNM membership in fixed 63-country Q2-2026 cohort | PASS |
| Prior VNM national validation duplicate search | PASS (no dedicated report found) |
| Official SBV BOP source family / separate labels | PASS |
| Official Q2-2026 national portfolio asset transaction value | NOT_EXTRACTED |
| Official Q2-2026 national portfolio liability transaction value | NOT_EXTRACTED |
| Quarterly publication route for Q2-2026 | NOT_ESTABLISHED |
| Raw Q2 source bytes / SHA-256 | NOT_CAPTURED |
| BPM6/BPM5 sign crosswalk for Q2 rows | NOT_ESTABLISHED |
| Same-vintage / revision timestamp | NOT_ESTABLISHED |
| Dual-leg numeric comparison | NOT_DONE |
| VNM national validation | PARTIAL / NOT PASS |
| 63-country aggregate admission | NOT_AUTHORIZED |

## 5. Next exact action
1. Search only for a distinct official SBV quarterly BOP statistical release, downloadable data table or documented API/export that explicitly exposes Q2-2026 portfolio assets and liabilities separately.
2. If found, preserve raw bytes, publication timestamp/vintage, units and source metadata; calculate SHA-256 before parsing.
3. Establish the SBV BPM5 financial-account sign convention from an SBV primary methodology note before mapping to IMF A_NFA_T and L_NIL_T.
4. Reuse the existing archived IMF exact-key Q2 rows; compare asset and liability separately. Do not query IMF again, allocate annual values into quarters, use FDI/securities-market aggregates, or net the legs.
5. If no distinct official quarterly route is available, preserve VNM PARTIAL / NOT PASS and advance to the next unvalidated member of the fixed cohort.

## 6. Protected invariants
No synthetic values, fabricated timestamps, annual-to-quarter allocation, stock-as-flow substitution, inferred sign transform, IMF re-query, cohort rebuild, paid API, or production changes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 remain unchanged. UNKNOWN is never PASS.

## Evidence
- SBV Annual Report 2023, Appendix 4: https://www.sbv.gov.vn/documents/d/sbv_portal/590044
- SBV Annual Report 2021, Appendix 4: https://www.sbv.gov.vn/documents/d/sbv_portal/532439
- Vietnam NSO H1 2026: https://www.nso.gov.vn/en/data-and-statistics/2026/08/report-socio-economic-performance-in-second-quarter-and-the-first-half-of-2026/
- Vietnam NSO Q3/9M 2026: https://www.nso.gov.vn/en/data-and-statistics/2026/11/press-release-socio-economic-performance-in-the-q3-and-the-nine-months-of-2026/
- Secondary context only (not admitted as national evidence): AMRO Vietnam Annual Consultation Report 2026, notes BPM6 with BPM5 financial-account sign.
