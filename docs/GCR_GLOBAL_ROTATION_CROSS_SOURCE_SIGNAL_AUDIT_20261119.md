# Global Capital Rotation — Cross-Source Signal Audit (Continuation 39, Part-3)
Date: 2026-11-19 (Asia/Kolkata)
Scope: evidence-led global cross-border capital, Brazil external sector and India FPI comparison. Research-only; no production integration or score changes.

## 1. Executive finding
The currently inspected evidence does not support a single, undifferentiated “capital is rotating into/out of emerging markets” conclusion. Different instruments and regions diverge:
- BIS end-June 2026 cross-border bank credit grew 9.3% y/y to Latin America and the Caribbean, while emerging Asia contracted 2.9% y/y.
- US Treasury September 2026 TIC recorded a $261.0bn net inflow into the United States (+$267.0bn private, -$6.0bn official).
- RBI reported India FPI net outflows of $10.3bn for April–October 5, 2026, while net FDI inflows were $13.8bn during April–August 2026.
- BCB reported Brazil September 2026 domestic portfolio investment net outflows of $2.1bn, but 12-month net portfolio inflows remained +$5.1bn; direct investment liabilities had 12-month net inflows of $88.3bn.
These are not contradictory measurements of the same flow. They differ by instrument (bank credit, securities portfolio, direct investment), geography, period and reporting methodology. Do not net or rank them as one capital-flow variable.

## 2. Source evidence register

### A. BIS — International banking statistics and global liquidity indicators, end-June 2026
Official release: https://www.bis.org/publications/202610-commentary-ibs-gli
- Cross-border bank credit stock reached $40.7tn at end-June 2026; +11% y/y.
- Cross-border credit to EMDEs increased $105bn in Q2; +8.9% y/y.
- Latin America and Caribbean: +9.3% y/y; emerging Asia: -2.9% y/y.
- The release separately reports currency composition: euro-denominated credit represented $424bn of the $877bn Q2 global cross-border bank-credit increase; US dollar-denominated credit $383bn.
- Interpretation: bank-credit geography suggests relative divergence, not proof of portfolio equity allocation or Brazil-specific investor purchases.
- Definitions matter: BIS GLIs include bank loans plus international debt securities to non-bank borrowers in USD/EUR/JPY; this differs from the narrower cross-border bank-credit measure.

### B. U.S. Treasury — TIC September 2026
Official release: https://home.treasury.gov/news/press-releases/sb0693/
Published 2026-11-18; observation month September 2026.
- Net TIC inflow: $261.0bn; private net inflows $267.0bn; official net outflows $6.0bn.
- Foreign residents' net purchases of long-term US securities: $186.7bn (private $148.3bn; official $38.4bn).
- US residents' net purchases of foreign long-term securities: $31.4bn.
- Banks' own net dollar-denominated liabilities to foreign residents increased $108.6bn.
- Treasury cautions that custodial data do not attribute foreign ownership with complete accuracy.
- Interpretation: September net inflow into US instruments is a strong global benchmark signal, but TIC custody attribution limitations must remain attached to the data.

### C. RBI — Governor's Statement, October 23, 2026
Official release: https://www.rbi.org.in/scripts/BS_ViewBulletin.aspx?Id=24510
- FPI net outflows: $10.3bn over April–October 5, 2026.
- Net FDI inflows: $13.8bn over April–August 2026, versus $9.6bn a year earlier.
- FX reserves were described as adequate at around 11 months of import cover and 94.4% of external debt.
- The observation windows differ (FPI through Oct 5; FDI through Aug). Do not compare them as same-period net flow totals.
- RBI describes global risk-off sentiment, elevated bond yields and energy/geopolitical risks in the same statement.

### D. Brazil — Banco Central do Brasil External Sector Statistics, 26 October 2026
Official PDF: https://www.bcb.gov.br/content/statistics/externalsectorstatistics_prev/202610_External_sector_statistics_text.pdf
- September current-account deficit: $5.1bn; 12 months through September: $60.0bn / 2.33% GDP (improved from $63.7bn / 2.50% through August and $78.4bn / 3.57% through September 2025).
- September domestic-market portfolio investment liabilities: net outflow $2.1bn; 12 months through September: net inflow $5.1bn.
- Direct investment liabilities: September net inflows $11.3bn; 12 months through September: $88.3bn / 3.43% GDP.
- International reserves: $362.8bn in September 2026, down $9.8bn from prior month, with the release attributing the decline to price, FX, spot sales and repo-line components.
- Interpretation: Brazil's domestic portfolio flow, direct-investment liability flow, current account and reserves are separate series. The 12-month FDI/portfolio data cannot be treated as a short-horizon market-flow signal.

### E. Research literature — capital-flow cycle timing
Open-access paper: https://www.sciencedirect.com/science/article/pii/S1042443124000465
Journal of International Financial Markets, Institutions and Money, Vol. 92 (April 2024), article 101980.
- The study reports capital-flow cycles tend to be more volatile than financial and business cycles, and tend to lead financial and business cycles.
- Use as a methodological rationale to test lead/lag relationships; do not treat it as current 2026 market evidence or a ready-made predictive coefficient.

### F. IMF — Global Financial Stability Report, April 2026
Official report: https://www.imf.org/en/publications/gfsr/issues/2026/04/14/global-financial-stability-report-april-2026
- IMF identifies cross-border portfolio flows to EMs as largely intermediated by nonbank financial institutions and sensitive to global risk sentiment; sensitivity differs by investor type, including passive mutual funds/ETFs and hedge funds.
- Treat investor-type composition as a required dimension; aggregate flows alone conceal heterogeneous risk sensitivity.

## 3. New design rules for GCR data model
1. Preserve separate flow families: cross-border bank credit; portfolio liabilities/assets; direct investment liabilities/assets; official flows/reserves; FX and sovereign yields.
2. Each observation must carry observation_period_start/end, publication_timestamp, retrieval_timestamp_utc, source_vintage, geography, instrument, counterparty/investor sector, currency, unit, sign convention, frequency, provisional/confirmed status and source URL.
3. Never align series by publication date when observation periods differ. Use observation-period alignment and explicitly preserve lagged availability.
4. Do not combine BIS bank-credit regional growth, US TIC securities/banking flows, RBI FPI, and BCB BOP into one net number. Keep separate sub-indices until normalized and validated.
5. A relative-attraction score is NOT_READY until country panels have same-period, same-instrument or explicitly modelled distinct layers; FX, rates, risk, reserves and macro fundamentals need their own validated inputs.
6. Brazil-specific SDMX BOP6/BOP_BPM6 identity issue remains a separate source-identity gate; this macro cross-source research does not resolve the PA changelog or schema mismatch.
7. No fabricated daily interpolation from quarterly BIS or monthly/quarterly BOP observations. No synthetic data, inferred values from charts where raw data are unavailable, or guessed conversion factors.

## 4. Acceptance impact
| Workstream | Status | Evidence / reason |
|---|---|---|
| GCR global source discovery | PARTIAL | BIS, US Treasury TIC, RBI and BCB official releases plus IMF/research literature inspected |
| Global capital-flow divergence diagnosis | OBSERVED | Bank credit, TIC, India FPI/FDI and Brazil portfolio/FDI differ by instrument and period |
| GCR synchronized country panel | BLOCKED | Different observation windows/frequencies; not a matched panel |
| GCR relative-attraction score | NOT_READY | Must keep instrument layers separate and validate aligned inputs |
| Brazil BOP/PA identity | BLOCKED | No Brazil-specific BOP6/BOP_BPM6 crosswalk or owner-side PA revision export |
| Brazil macro external-sector evidence | PARTIAL | BCB September release inspected; raw API series and historical backfill not yet validated |
| Production integration | BLOCKED | No selector, ranking, weights or production logic changed |

## 5. Next highest-value tasks
1. Convert BIS, TIC, RBI and BCB observations into source contracts with their native frequencies and definitions; capture raw downloadable tables/API payloads and hashes, not only rendered summaries.
2. Build a date-vintage matrix with separate observation period, publication date, retrieval date and source revision.
3. Acquire same-period Brazil and India BoP/FPI/FDI/FX-reserve series from BCB/RBI and a same-quarter cross-country BIS panel before comparative scoring.
4. Continue Brazil SDMX identity resolution only through exact PA/provider-side revision export and authoritative Brazil-specific crosswalk evidence; do not repeat known failing txId=2 requests.
5. Validate GCR event-study lead/lag hypotheses out-of-sample before any scoring weight or production admission.

## 6. Hard invariants
₹0; official/free data and openly accessible research only. News and journals are corroboration/context, not substitutes for official raw data. No synthetic data, fabricated timestamps, chart-digitized estimates as exact values, interpolation, guessed hashes, unapproved crosswalks or aliases. UNKNOWN is never PASS. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E unchanged. No production integration, macro weights, or trading admission.
