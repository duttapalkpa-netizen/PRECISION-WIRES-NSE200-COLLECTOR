# GCR — RBI India Capital-Flow Reversal Event Register (Continuation 43, Part-1)
Date: 2026-11-19
Stage: OBSERVATION ONLY
Decision: PRIMARY-SOURCE EVENT REGISTER CREATED; QUANTITATIVE MARKET EVENT STUDY NOT YET RUN.

## 1. Purpose and scope
Convert the RBI Occasional Paper "Cross-border Capital Flows and Sudden Stops: Lessons from Emerging Market Economies" into a bounded India-centred event register. This is source extraction, not independent replication, not a claim of causal equity returns, and not a trading signal.

Primary source: https://www.rbi.org.in/scripts/bs_viewcontent.aspx?Id=4517
Authors: Sujata Kundu, Anshu Kumari and Deepika Rawat. Analysis period Q1-1992 to Q1-2022.

## 2. India-relevant events and exact source-supported classification
| Event window | RBI source finding | Flow classification | Interpretation / guardrail |
|---|---|---|---|
| 2008-09 GFC | India experienced a sudden stop in capital inflows during the GFC (Section III, page text); paper also finds GFC as the only aggregate EME sudden-stop episode in gross and net flows over Q1-1992–Q1-2022 | India-specific sudden-stop statement; aggregate EME sudden stop in gross and net | Use as a primary benchmark event; do not infer daily NIFTY response from quarterly flow classification |
| H2-2015 to H1-2016 | India is explicitly among countries recording sudden stops in this interval, associated by the authors with August-2015 Chinese equity-market turmoil and the first US Fed rate hike in Dec-2015 | Country-level sudden-stop finding; exact India series/flow type must be read from Annex Table A2 before sub-classifying | Keep event window broad as stated in body text; do not assign unverified quarter sub-windows |
| Q1-2022 | India recorded a sudden stop with respect to gross FPI inflows | Gross FPI inflow sudden stop | Distinguish from net capital flows and from market-price reaction |
| 2013 taper tantrum | RBI event-study finds EME weekly net FPI flows heavily impacted; however taper episodes were not identified as sudden stops in the paper's sudden-stop classification | Reversal/market-flow stress, not sudden stop under this paper's criteria | Include as a non-sudden-stop comparison/control event, not as a sudden-stop label |
| 2020 COVID-19 | RBI reports sharp EME weekly net FPI effects and persistent impact; Q3 and Q4-2020 sudden-stop phases are identified for EMEs excluding China on net capital flows, but this text does not establish an India-specific sudden-stop classification | EME panel net-flow sudden-stop classification; India-specific event response not established here | Do not label India a sudden stop from the aggregate result |
| 2021 taper talks | RBI says taper talks did not create major EME net-FPI impact; no taper-talk episode identified as sudden stop in this paper | Limited/contained EME net-flow response; not sudden stop | Useful negative/comparison event |
| Russia-Ukraine war / synchronised AE tightening in 2022 | RBI weekly EME net-FPI event study finds significant impact | EME panel flow reversal response | Separate from India's Q1-2022 gross-FPI sudden-stop result; exact India market impact not established |

## 3. India-specific empirical driver evidence to carry into later design
RBI's India cloglog regression reports:
- Weak global GDP growth, higher global risk and higher global long-term rates are associated with higher likelihood of gross-capital-inflow reversal.
- Higher US Federal Funds rate changes and INR depreciation are also significant in the reported specifications.
- Domestic headline inflation and domestic GDP growth are not statistically significant in the displayed India specification.
- In extended analysis, higher global liquidity lowers reversal likelihood, while higher domestic CAD raises it.
These are quarterly historical model associations over the paper's sample, not daily causal coefficients, not factor weights, and not production thresholds.

## 4. Event-study implementation guardrails
1. Build event windows from the source-stated date spans; where source only gives a broad interval, retain that uncertainty rather than invent exact dates.
2. Keep three labels separate: (a) RBI event-study flow reversal; (b) RBI sudden-stop classification; (c) independently measured India market/FX/sector response.
3. Acquire raw, timestamped daily/weekly NIFTY 50 price index, India VIX, USD/INR, FPI by instrument and relevant global factors before estimating market response.
4. Use global event announcement times and Indian market-session timestamps to avoid look-ahead; no same-day alignment unless publication/trading times support it.
5. Control for concurrent India-specific policy, earnings, election, budget and corporate events; avoid attributing all market movement to global shock.
6. Do not convert quarterly BoP sudden-stop labels into 1–3 day trading signals.
7. Preserve original RBI study definitions and sample period; independently replicate before using any coefficient or label for calibration.

## 5. What is not established
- No exact India sub-quarter 2015/16 event boundaries have been independently extracted from Annex Table A2 in this increment.
- No raw weekly FPI series or event-window market prices were downloaded.
- No NIFTY/Sensex/sector abnormal returns, FX responses, VIX response, causal effects, predictive accuracy or trading edge were calculated.
- No country weights, factor weights, thresholds or production changes are authorized.

## 6. Status
| Item | Status |
|---|---|
| RBI primary-source event statements extracted | VERIFIED |
| India event register | CREATED |
| Exact Annex Table A2 India sub-windows | PENDING |
| Raw daily/weekly event-study panel | NOT_ACQUIRED |
| Independent event-study replication | NOT_DONE |
| Observation phase overall | OPEN |
| Planning / Organizing | NOT_STARTED |
| GCR complete / production admission | NOT_AUTHORIZED |

## 7. Source locations
RBI source page: https://www.rbi.org.in/scripts/bs_viewcontent.aspx?Id=4517
Relevant source sections: India trends (GFC), Section IV event-study framework and results, India cloglog regression Table 1, sudden-stop classification and Annex Table A2.

## 8. Invariants
₹0; official/free sources; no synthetic data, fabricated timestamps, guessed event dates, or unsupported causal claims. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E unchanged. UNKNOWN is never PASS.
