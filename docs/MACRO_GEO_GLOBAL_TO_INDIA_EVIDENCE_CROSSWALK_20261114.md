# Macro-Geo global-to-India evidence crosswalk — 2026-11-14

## Purpose and boundary
This is an evidence crosswalk for research ingestion and future event studies. It is not a live trading signal, a calibrated coefficient set, or permission to change the production selector/ranking. No numeric sensitivity coefficients are inferred.

## Official / source evidence captured
1. DIPAM Market Monitor dated 10-Nov-2026 (source list printed in document: Bloomberg, BSE, NSE, RBI, FBIL, CDSL, NSDL, PIB):
   - Indian indices and sector indices; global US, Europe and Asia indices.
   - FII/DII daily flows; macro indicators including repo rate, India 10Y yield, USD/INR and FX reserves.
   - Derivatives snapshot including Brent futures and INR/USD forward rates.
   - Reported snapshot values include USD/INR spot 93.94, India 10Y yield 7.15%, repo 5.50%, FX reserves USD 717.06bn, and Brent Dec-26 futures 90.81. These are specifically 10-Nov report values, not 14-Nov live values.
   - Source: https://dipam.gov.in/resources/pdf/publication/Market_Monitor-10.11.2026.pdf
2. RBI Bulletin page (published/crawled within the current research window) describes elevated major-economy treasury yields, stronger US Dollar Index, negative EME portfolio flows, and West Asia geopolitical tensions as global growth/inflation trade-off risks.
   - Source: https://www.rbi.org.in/Scripts/BS_ViewBulletin.aspx?Id=24516
3. Reuters report dated 13-Nov-2026 reports Indian equity weakness alongside crude/inflation pressure, October CPI at 6.09%, rupee around 94.04 at open, and November foreign inflows. This is secondary news evidence and must not replace official raw series.
   - Source: https://www.reuters.com/world/india/indian-shares-likely-open-flat-oil-surge-counters-strong-foreign-inflows-2026-11-13/

## Global-to-India factor mapping (qualitative hypotheses; not fitted)
| Global factor | India transmission channel | Most exposed NSE groups | Required primary series before scoring |
|---|---|---|---|
| Brent crude / energy supply shock | Import bill, CPI, INR, current account, margin pressure | OMCs, aviation, paints, chemicals, logistics; upstream producers may benefit | Daily Brent/WTI; official India crude basket; USD/INR; sector index; company margin disclosures |
| USD broad strength / US real yields | FPI risk allocation, INR translation, valuation discount rate | IT exporters (mixed FX/valuation), rate-sensitive growth, banks, NBFCs | DXY or official reproducible proxy; US Treasury yields; USD/INR; FPI equity/debt flows |
| US Fed policy expectations | Global liquidity, EM risk premium, bond flows | Banks, NBFCs, realty, long-duration growth | FOMC release timestamps; US yields; RBI policy; India G-sec curve |
| China demand / industrial cycle | Metals, chemicals, capital goods order cycle | Metals, mining, industrials, shipping | China official industrial production/PMI/imports; LME copper/aluminium; NSE sector indices |
| Copper / aluminium / steel prices | Realisations, input costs, working capital | Hindustan Copper, metal producers, cable/electricals, auto ancillaries | LME settlement series; INR conversion; company production/sales and cost disclosures |
| Gold / silver and risk aversion | Safe-haven demand, commodity-linked flows, jewellery demand | Gold lenders, jewellery, miners, commodity funds | LBMA/official exchange prices; INR; real yields; company disclosures |
| West Asia / shipping / sanctions / conflict | Oil supply premium, freight/insurance, risk sentiment | OMCs, aviation, paints, chemicals, ports, logistics, defence | Timestamped official MEA/PIB/UN notices; Brent; freight indices; issuer-specific exposure evidence |
| Global equity / AI-capex rotation | Foreign flows and valuation rotation | IT services, semiconductor-linked suppliers, power/capital goods | Major global indices; company order books; official capex disclosures; FPI flows |
| Japan yen / carry unwind | Global leverage reduction and EM portfolio liquidation | High-beta small/midcaps, leveraged financials | USDJPY; JGB yields; VIX; FPI flows; India market breadth |
| Global food/fertiliser shocks | CPI, rural demand, subsidy/fiscal channel | FMCG, fertiliser, agrochemicals, consumer discretionary | FAO/official commodity series; India CPI/WPI; monsoon/agri data; company input disclosures |

## Research implementation rules
- Preserve source event time, publication time, retrieval time and timezone independently.
- Join global event windows to Indian market sessions using exchange holiday calendars; never assume same-day reaction where event occurs after NSE close.
- Estimate factor sensitivity only with observed historical data and out-of-sample/rolling validation; do not assign intuitive weights as if measured.
- Control for NIFTY regime, sector index return, USD/INR, FPI/DII flows, India VIX, rates and commodity beta; avoid double-counting correlated global factors.
- Use lagged values available at decision time to prevent look-ahead leakage.
- Keep missing observations UNKNOWN; do not forward-fill event shocks or synthesize prices.
- Sector exposure is a hypothesis until supported by issuer disclosures, segment revenue/cost mix, and measured return response.
- The 10-Nov DIPAM snapshot is contextual cross-check evidence only. It is not a time series and cannot calibrate coefficients.

## Current result
- Evidence crosswalk: documented.
- Numeric factor sensitivities / coefficients: NOT ESTIMATED.
- Timestamped historical event-to-NSE-session panel: NOT BUILT.
- Production integration: NOT AUTHORIZED / NOT DONE.
- This document does not satisfy Macro-Geo P0 coverage by itself and does not unblock the Hard Gate.


## Fresh official dated market snapshots (retrieved for 2026-11-14 review)

### CDSL FPI daily trend — reporting date 12-Nov-2026
- Equity: gross purchases ₹32,887.51 crore; gross sales ₹18,208.79 crore; net exchange investment ₹14,678.72 crore; primary/other net ₹15.00 crore; subtotal net ₹14,693.72 crore.
- Debt-General subtotal net ₹445.65 crore; Debt-VRR subtotal net −₹173.22 crore; Debt-FAR stock-exchange net ₹1,022.81 crore.
- Conversion rate shown by CDSL: ₹93.8075/USD.
- CDSL notes the report is compiled from exchange/depository reports and represents the previous trading day's FII/FPI trading/position. Preserve its reporting-date semantics; do not conflate debt routes or treat the subtotal as a full independent capital-flow measure.
- Source: https://www.cdslindia.com/eservices/publications/fiidaily

### NSE reference / market snapshot — 13-Nov-2026
- NSE reference rate at 13:00 IST: USD/INR ₹94.1997 (previous day ₹93.7650); 26-Nov USDINR futures LTP 94.3800, +0.2523% at the displayed snapshot.
- NSE market statistics at 12:51 IST: 3,577 stocks traded; advances 1,264; declines 2,199; unchanged 114; 93 stocks at 52-week high and 25 at 52-week low. This is an intraday breadth snapshot, not closing breadth.
- Source: https://www.nseindia.com/

### RBI National Summary Data Page — published 13-Nov-2026; several series latest 12-Nov-2026
- USD/INR ₹93.77 on 12-Nov versus ₹88.64 in the comparison period shown; Nifty 50 25,299 versus 25,876 (-2.23%) and Sensex 81,911 versus 84,467 (-3.03%) in the page's comparison columns.
- 1-year MCLR range 8.45–8.90% latest 06-Nov; T-bill rates 5.8681% latest 11-Nov; broad money M3 ₹337,684.2bn latest 31-Oct.
- Source: https://www.rbi.org.in/SCRIPTs/BS_NSDPDisplay.aspx

### Interpretation guardrails
- The CDSL 12-Nov net equity inflow and the NSE 13-Nov intraday rupee/breadth snapshots are distinct time stamps and source definitions. Do not combine them into a same-session causal claim.
- A positive one-day FPI equity figure can coexist with weak breadth or a weaker rupee; this is not contradictory because the observations differ in timestamp, universe, and measurement. Require a multi-session panel before asserting persistence or predictive value.
- These snapshots enrich the factor register but do not estimate betas, causal effects, or 1–5 day return probabilities. They are not a substitute for the full official historical panel.
