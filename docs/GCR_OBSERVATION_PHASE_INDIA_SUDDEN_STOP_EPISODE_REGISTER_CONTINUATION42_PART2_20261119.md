# GCR Observation Phase — India Sudden-Stop Episode Register (Continuation 42, Part-2)
Date: 2026-11-19
Stage: OBSERVATION ONLY

## 1. Purpose and boundary
Extend the historical observation inventory with India-specific, officially published episode classifications. This is not a planning specification, country-weight model, causal claim about NIFTY/Sensex, or production change. The source study covers Q1:1992–Q1:2022 and uses IMF Balance of Payments Statistics quarterly data for 19 EMEs.

## 2. India episodes reported by RBI
RBI Occasional Paper, “Cross-border Capital Flows and Sudden Stops: Lessons from Emerging Market Economies”, Annex Table A2 reports:

| Flow definition | India episode(s) | Quarters |
|---|---|---:|
| Gross capital inflows | Q4 2008–Q2 2009 | 3 |
| Gross capital inflows | Q1 2016–Q2 2016 | 2 |
| Gross FPI inflows | Q3 2008–Q1 2009 | 3 |
| Gross FPI inflows | Q1 2016 | 1 |
| Gross FPI inflows | Q1 2022 | 1 |
| Net capital flows | Q4 2008–Q2 2009 | 3 |
| Net capital flows | Q1 2016–Q2 2016 | 2 |

Interpretation: these are separate definitions and should not be collapsed into a single binary “capital outflow” flag. Gross capital inflows, gross FPI inflows and net capital flows identify different stress windows.

## 3. Important classification distinctions
- RBI reports that the GFC was the only sudden-stop episode for the full EME sample during Q1:1992–Q1:2022 under both gross-capital-inflow and net-flow definitions. Excluding China, Q3–Q4 2020 were sudden-stop phases on net capital flows only.
- India was among the country-level cases with sudden stops in H2 2015 and H1 2016, associated by the RBI paper with August 2015 Chinese equity-market turmoil and the first US Federal Funds rate hike in December 2015.
- None of the 2013 taper-tantrum or 2021 taper-talk episodes qualified as sudden stops in the paper’s stated classification.
- However, India did record a gross-FPI sudden stop in Q1 2022. This should not be generalized into a claim that every 2022 shock quarter or all capital-flow measures had a sudden stop.
- “Shock episode”, “capital-flow reversal”, and methodologically defined “sudden stop” are distinct labels. Keep all three.

## 4. India-specific drivers reported by RBI
For India, the RBI paper’s baseline model associates weak global economic growth, higher global interest rates and higher global risk with falls in gross capital inflows. Year-on-year increases in global long-term rates and the US Federal Funds rate raise reversal likelihood; exchange-rate depreciation also raises the probability. In extended specifications, global liquidity and domestic current-account deficit are significant: higher global liquidity lowers reversal likelihood, while a higher CAD raises it. The paper reports domestic GDP growth and inflation as statistically insignificant in the baseline specification. These are model-specific findings, not timeless laws or trading signals.

A separate RBI “Capital Flows at Risk: India’s Experience” paper (June 16, 2022) finds global risk aversion to be the main push factor and growth differentials/domestic term premia to be predominant pull factors. Its 3.2% of GDP adverse-scenario and 7.7% of GDP combined-shock portfolio-outflow estimates are conditional tail-risk scenario estimates, not forecasts or observed losses.

## 5. GCR observation implications (not implementation)
1. Preserve separate time series/labels for gross capital inflows, gross FPI inflows, net capital flows, FDI, portfolio equity, portfolio debt and other investment.
2. Store the RBI paper's exact quarterly episode windows as historical evidence, not as daily signal dates.
3. Do not label 2013 or 2021 as “no impact”; only state that they did not meet this paper's sudden-stop classification.
4. A quarterly episode register cannot by itself establish short-horizon NIFTY/Sensex or sector return effects. Daily/weekly price, FX, yield, commodity and flow data plus confounder controls are still required.
5. The paper's analysis ends Q1 2022; it cannot classify 2023–2026 episodes. FY2025-26 observations in Part-1 remain separate annual-flow evidence.

## 6. Unresolved evidence
- Exact Annex Table A2 event quarter boundaries have been captured from the RBI publication; source workbook/raw IMF BOPS vintage and replication of the authors' calculations have not been independently reproduced.
- The article's regression findings are not independently re-estimated here.
- No event-level causal effect on NIFTY, Sensex, sector indices or individual securities has been measured.
- No country weights, factor weights, thresholds or production logic are authorized.
- Brazil, India Q1-2026 liability reconciliation, Chile, South Africa and the 63-country Q2-2026 cohort gates remain as documented in prior ledger entries; this report does not change their statuses.

## 7. Primary sources
1. RBI, “Cross-border Capital Flows and Sudden Stops: Lessons from Emerging Market Economies” (Q1:1992–Q1:2022), especially main text around sudden-stop classification and Annex Table A2/A3/A5.3:
https://www.rbi.org.in/scripts/bs_viewcontent.aspx?Id=4517
2. RBI Bulletin, “Capital Flows at Risk: India’s Experience” (June 16, 2022):
https://www.rbi.org.in/Scripts/BS_ViewBulletin.aspx?Id=21067

## 8. Stage and invariants
OBSERVATION: this India-specific episode-register increment is complete; the wider global-to-India evidence inventory remains OPEN.
PLANNING: NOT STARTED.
ORGANIZING: NOT STARTED.
GCR maturity: NOT COMPLETE; aggregate/production admission NOT AUTHORIZED.
₹0 spend; official/free sources prioritized; no synthetic data, fabricated timestamps, guessed transformations, or unsupported country weights. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E unchanged. UNKNOWN is never PASS.
