# CPI Base-2024 Back-Series Linking — Official Method and Scope Guard
Audit date: 2026-11-10 (Asia/Kolkata)
Repository: duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR
Branch: research/global-capital-rotation-overlay-v1

## Official primary-source finding
MoSPI's official FAQ, "FAQs on CPI 2024 Series", Q37–Q38 and the January 2026 CPI press release state:
- The overlapping year is 2025, when CPI 2012 and CPI 2024 observations are both available.
- Annual average geometric-mean CPI for the new series is divided by the corresponding old-series annual average to obtain the linking factor.
- Earlier old-series observations are multiplied by the relevant linking factor.
- Published general-level linking factors for CPI 2024=100 are:
  - Rural: 0.5222
  - Urban: 0.5320
  - Combined: 0.5267
- The same official FAQ/press release explains that CPI 2024 follows COICOP-2018 while CPI 2012 used a different classification; because of these classification differences, the two series can be directly linked only at the general index level.

## Material correction / strict guard
The previously recorded general description of the linking method must NOT be interpreted as permission to link group-wise, division-wise, class-wise, subclass-wise or item-level CPI 2012 data to CPI 2024 using these three factors.
The factors above apply only to the corresponding all-India general level Rural, Urban and Combined series, as explicitly published.
No factor is inferred for groups or divisions. No group/item mapping is fabricated. Do not use these factors to splice detailed COICOP groups.
Keep CPI 2012 and CPI 2024 detailed classifications separate unless MoSPI publishes a valid official detailed-level concordance or linking method.

## Evidence references
- MoSPI official FAQ PDF: https://mospi.gov.in/uploads/documents/documents/1770891066052-Annexure_V.pdf (Q37–Q38; linking factors and classification limitation).
- MoSPI official January 2026 CPI press release: https://www.mospi.gov.in/uploads/latestreleasesfiles/1770893247472-Press%20Relase%20of%20CPI%20for%20Jan26.pdf (back-series coverage, linking factors, and general-level-only conclusion).

## Validation implications for the research pipeline
1. Preserve source series ID, base year, geography, sector (Rural/Urban/Combined), index level and publication vintage.
2. For any general-level bridge, use only the official matching factor: Rural 0.5222, Urban 0.5320, Combined 0.5267.
3. Do not recompute the published factors from rounded displayed monthly values; use MoSPI's published official factors.
4. Validate back-series values against the official released MoSPI back-series table, where available. Do not assume multiplying displayed rounded values reproduces the official table exactly.
5. For detailed group/division/item research, maintain separate base-year panels; require an official concordance before any cross-base comparison.
6. Do not combine CPI series in a single inflation calculation across the base break without documenting the permitted general-level bridge and vintage.

## Gate and project controls
- Official method and general-level factors: VERIFIED.
- Detailed-level linking factors/concordance: NOT PROVIDED in this official method; UNKNOWN/BLOCKED.
- Raw CPI observations ingested in this task: NO.
- This is a methodology/source audit, not CPI data ingestion.
- Research-only. No changes to production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A-E or Hard Gate.
- Milestone 6 remains 20%; overlay remains 62.5%; overall V11.3 remains NOT_CALCULABLE.
