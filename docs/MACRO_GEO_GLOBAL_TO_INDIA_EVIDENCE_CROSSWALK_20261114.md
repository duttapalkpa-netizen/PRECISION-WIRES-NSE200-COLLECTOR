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


## 2026-11-14 macro risk transmission refresh — official RBI and dated market evidence

### Verified RBI dashboard snapshot (14-Nov-2026 page update; observations retain their own dates)
- RBI policy rates: repo 5.50%, SDF 5.25%, MSF/Bank Rate 5.75%; CRR 3.00%, SLR 18.00%.
- FBIL USD/INR reference: ₹94.1997 as at 13:00 on 13-Nov-2026; GBP ₹124.6140, EUR ₹104.1814, JPY ₹58.9400 per 100 yen.
- Government security yields as at 12-Nov-2026: 6.20% GS 2029 6.8894%; 6.53% GS 2031 7.0289%; 6.94% GS 2036 7.2430%; 7.06% GS 2041 7.4011%; 7.63% GS 2056 7.7235%.
- Nifty 50 25,299.35 and Sensex 81,911.01, both as at 12-Nov-2026. These are not 14-Nov live prices.
- Source: RBI Bulletin/dashboard, https://m.rbi.org.in/scripts/BS_ViewBulletin.aspx?Id=24446 (web evidence `turn459992news3`).

### Current transmission interpretation — hypotheses, not measured coefficients
- INR weakness + elevated crude can raise imported inflation/current-account and input-cost pressure; the impact is asymmetric across OMCs, upstream energy, aviation, paints, chemicals and exporters. Confirm with company-level exposure and lagged observed data.
- Higher sovereign yields and hawkish global rate expectations can tighten equity discount rates and funding conditions; rate-sensitive banks/NBFCs, real estate and long-duration growth valuations need separate sector tests.
- FPI equity inflows can support index liquidity but do not guarantee broad participation; retain breadth, cash-market flow, derivatives positioning and domestic institutional flow as separate features.
- AI/technology rotation can move global IT valuations independently of Indian domestic demand; do not use Nasdaq/AI headlines as an automatic IT signal without sector-relative returns and issuer guidance.
- West Asia shipping/geopolitical risk is a conditional oil/freight shock, not a deterministic direction forecast. Cross-check official notices, Brent curve, freight/insurance evidence and Indian sector exposure.

### Fresh market context (not promoted to production feature)
- 13-Nov reporting described INR near ₹94.24/USD, renewed crude pressure and higher US yields; Nifty fell on the day despite strong November foreign inflows. Treat this as contextual reporting, not an official raw series or executable factor observation. Source: Reuters, https://www.reuters.com/world/india/rupees-faltering-rally-faces-returning-oil-pressure-surging-us-yields-2026-11-13/ (`turn459992news7`); https://www.reuters.com/world/india/indian-shares-likely-open-flat-oil-surge-counters-strong-foreign-inflows-2026-11-13/ (`turn459992news8`).
- IEA reporting on 13-Nov projected a Q4-2026 oil-market surplus as Gulf exports recover, while also noting continuing shipping/security risks; Brent was reported near $95.71/bbl. This is a scenario input requiring official IEA series and timestamped price validation, not a substitute for raw price acquisition. Source: https://www.reuters.com/business/energy/world-oil-market-is-returning-surplus-gulf-exports-recover-iea-says-2026-11-13/ (`turn459992news10`).
- RBI October MPC resolution raised repo to 5.50% and shifted stance to calibrated tightening; RBI cited West Asia, energy prices, global yields and domestic inflation risks. GDP projection 7.1%, CPI projection 5.2% for FY2026-27. Source: https://rbi.org.in/Scripts/BS_ViewBulletin.aspx?Id=24511 (`turn459992search0`).

### Controls and status
- Keep observation date, publication timestamp, retrieval timestamp, timezone, source class, universe, route and finality as separate fields.
- Do not merge RBI dashboard observations, Reuters reporting, CDSL custodian flows, NSE provisional flows or DIPAM snapshots into one same-date row without explicit alignment keys.
- No numeric factor beta, event coefficient, causal effect or H+1/H+3/H+5 predictive probability is inferred from this snapshot. No synthetic panel or forward-fill created.
- Macro evidence snapshot refresh: DOCUMENTED. Historical event-to-NSE-session panel, P0 8/8 coverage, 35-factor source coverage, rolling out-of-sample sensitivity and production-parity backtest: NOT PROVEN / NOT RUN. Hard Gate remains BLOCKED.


## India external-sector shock / export opportunity refresh — official October 2026 trade release

### Ministry of Commerce & Industry / PIB release (published 13-Nov-2026)
- October 2026 merchandise exports: US$49.47bn; merchandise imports: US$89.35bn; merchandise trade deficit derived by direct subtraction: US$39.88bn. The subtraction is an arithmetic cross-check of the published source values, not an additional observation.
- October total exports (goods + services): US$89.99bn; total imports: US$110.07bn; reported total trade balance: deficit US$20.09bn. Services October figures are estimates because latest RBI services data in the release is September 2026.
- April–October FY2026-27 merchandise exports US$309.06bn, imports US$527.21bn, merchandise deficit US$218.15bn; total exports US$568.84bn, imports US$662.19bn, total deficit US$93.35bn.
- Export growth leaders reported for October include petroleum products +140.21%, electronic goods +62.70%, gems & jewellery +40.06%, organic/inorganic chemicals +36.20%, engineering goods +36.01%. These are year-on-year sector export values, not listed-company revenue growth or stock-return signals.
- Non-petroleum exports US$40.58bn; non-petroleum imports US$66.53bn. Non-petroleum/non-gems-jewellery exports US$37.38bn and imports US$57.37bn. Preserve the source's category definitions and table notes.
- Official source: PIB, Ministry of Commerce & Industry, PRID 2335914, https://www.pib.gov.in/PressReleseDetailm.aspx?PRID=2335914&lang=2&reg=48 (web evidence `turn935975search0`).

### India equity transmission hypotheses (not measured stock signals)
- Wider merchandise deficit + higher petroleum imports can increase external financing/INR sensitivity when global crude and freight rise; test with USD/INR, Brent, reserves, current-account data and sector-level import intensity.
- Export growth in electronics, engineering, chemicals and petroleum products may support relevant listed supply chains only where issuer export mix, margins, capacity and order-book disclosures corroborate. National sector export growth must not be mapped directly to every constituent.
- Strong services surplus can partially offset goods deficit; October services data are estimated and must not be treated as final RBI-reported actuals.
- Distinguish commodity-price/volume effects, base effects, gold/seasonal imports, and export unit-value effects before assigning a persistent macro regime.

### Controls / status
- Keep October trade data as a monthly release with publication timestamp 13-Nov-2026 and reference month October 2026; never align to daily NSE bars by calendar date alone.
- No synthetic daily values, issuer attribution, beta, causal coefficient or H+1/H+3/H+5 probability inferred. No production selector/ranking/CORE-672 modification.
- Scoped official trade-release ingestion and arithmetic reconciliation: DOCUMENTED. Full historical monthly panel, issuer-level exposure mapping, Macro-Geo P0 8/8, 35-factor coverage and rolling out-of-sample validation remain NOT PROVEN / NOT RUN. Hard Gate remains BLOCKED.
