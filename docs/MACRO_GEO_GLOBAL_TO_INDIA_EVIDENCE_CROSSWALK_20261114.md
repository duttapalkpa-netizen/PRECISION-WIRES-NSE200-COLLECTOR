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
