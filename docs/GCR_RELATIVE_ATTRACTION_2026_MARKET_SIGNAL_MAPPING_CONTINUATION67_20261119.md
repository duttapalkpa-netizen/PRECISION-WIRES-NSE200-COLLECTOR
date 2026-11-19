# GCR Relative-Attraction 2026 Market Signal Mapping — Continuation 67
Date: 2026-11-19 (Asia/Kolkata)
Scope: research-only source review and factor-to-gate mapping. No weights, production integration, trade signal, or backtest claim.

## Decision
The supplied 2026 outlook material supports expanding the GCR evidence map across valuation, style/factor leadership, sector breadth, earnings delivery, bond-yield opportunity cost, regional relative performance, FX/energy transmission, institutional flows and market concentration. It does not support a claim that these variables have a literal 100% causal influence on equities, nor does it establish a calibrated predictive model. This is a source-to-factor specification only.

## Source review: user-supplied links
1. Allianz Global Investors, “Global Equity Compass: Nov 2026”, published 2026-11-18:
   https://www.allianzgi.com/en/insights/global-equity-compass-nov-2026
   Page directly accessible. It reports October reversal in Momentum, weakness in Quality and outperformance of Value; elevated government-bond yields raise the return hurdle for equities; investors increasingly scrutinise whether AI capex translates into earnings/productivity; European defence, energy, semiconductors and industrial capacity are cited as possible implementation/earnings channels. Its chart discussion says markets historically underpriced Fed tightening in four of five prior cycles; this is historical context, not a forecast.
2. Goldman Sachs Global Investment Research, “Global Equity Strategy Outlook”, dated URL 2026-11-12:
   https://www.gspublishing.com/content/research/en/reports/2026/11/12/24403184-34ea-4419-9f7a-cba7b7c8ddbd.pdf
   Direct fetch returned HTTP 403. Contents, date and claims are NOT independently verified in this pass. Do not cite as accepted evidence until a lawful accessible copy is available.
3. Hedgeweek, “Indian equities rebound as global investors rotate away from AI stocks”, published 2026-11-16:
   https://hedgeweek.com/news/india-equities-rebound-as-global-investors-rotate-away-from-ai-stocks
   Accessible secondary report attributing its account to Bloomberg. It reports MSCI India +11% from October low, November foreign net purchases of $8.5bn, India forward P/E around 20x, improving earnings expectations, lower oil and investor diversification away from crowded AI trades. These remain secondary-source reported values, not independently reconciled raw observations; do not promote them to production inputs.
4. Charles Schwab, “2026 Mid-Year Outlook: Global Equity”, published 2026-06-08:
   https://www.schwab.com/learn/story/global-stock-market-outlook
   Accessible. It describes strong earnings/capex support but concentrated AI-linked earnings and index leadership, inflation/geopolitical risks and regional growth divergence. This is a mid-year outlook, not a November update.
5. Franklin Templeton, “Global Investment Outlook 2026” collection:
   https://www.franklintempleton.co.uk/insights/collections/global-investment-outlook-2026
   Accessible collection page. It lists 2026 outlook material on healthcare, energy, international value, Japan, small caps, consumer staples and emerging markets. Treat as a discovery/index page; each article must be separately captured before detailed claims are accepted.

## Additional current official snapshot inspected
RBI homepage/current-rates page (official; snapshot displayed as at 2026-11-13):
https://www.rbi.org.in/?t=1740755414021
- Policy repo 5.50%; SDF 5.25%; MSF/bank rate 5.75%.
- FBIL-sourced USD/INR reference rate 94.1997 as at 13:00 on 2026-11-13.
- Government security yields shown for 2026-11-12: 2031 7.0289%, 2036 7.2430%, 2041 7.4011%, 2056 7.7235%.
- Nifty 50 25,299.35 and Sensex 81,911.01 as at 2026-11-12.
These are dated snapshot values; they are not continuous histories and do not establish direction or causal impact by themselves.

Institutional flow discovery:
- Moneycontrol page surfaced November-2026 cash-market FII/DII figures, including month-to-date FII net +₹94,229.31 crore and DII net −₹55,570.66 crore through 18-Nov-2026. It is a secondary aggregator and was not reconciled here to NSE/NSDL/CDSL raw official files. Use only as a lead, NOT accepted official evidence.
- Hedgeweek's $8.5bn November foreign-flow claim is also secondary. Do not combine USD and INR series without a dated, documented FX convention.

## GCR factor map — proposed research-only mapping
| Domain | Required measurable series | Relative-attraction question | Destination gate | Status now |
|---|---|---|---|---|
| Equity valuation | Forward P/E, earnings yield, CAPE where comparable; timestamped regional/sector coverage | Is a market/sector cheaper relative to its own history and peers, after growth/quality adjustment? | Valuation & region comparison | PARTIAL; no synchronized global panel |
| Earnings | EPS growth, revisions, breadth, margins, cash conversion, capex-to-revenue and realised productivity | Are expected returns supported by realised/revised earnings rather than narrative? | Earnings quality / catalyst | PARTIAL; source-specific outlooks only |
| Style/factor rotation | Value, Momentum, Quality, Growth, Low Volatility and Size total-return indices | Is leadership changing persistently or is this a one-month reversal? | Factor leadership / regime | PARTIAL; Allianz qualitative October read |
| Sector rotation | Sector TRI, relative strength, breadth, earnings revisions and fund flows | Which sectors are gaining both price leadership and fundamental support? | Sector strength → stock transmission | BLOCKED pending synchronized sector TRI + point-in-time fundamentals |
| Rates / bond opportunity cost | UST nominal & real curve, India G-sec curve, policy expectations, term premium where available | Are discount rates and equity risk premium changing in a way that alters relative attractiveness? | Macro discount-rate / risk modifier | PARTIAL; Treasury capture exists separately; RBI snapshot only |
| FX / dollar / carry | DXY kept distinct from Fed H.10 broad dollar; USD/INR FBIL reference kept distinct from spot/interbank; JPY/carry | Is currency pressure changing foreign returns, import costs or carry risk? | FX transmission / risk | PARTIAL; histories and basis reconciliation remain open |
| Energy / commodities | Brent spot FOB (EIA RBRTED) distinct from futures; India energy import sensitivity and sector margins | Does oil help/hurt India's external balance, inflation and sector earnings? | Energy transmission | PARTIAL; no matched event study here |
| Regional allocation | Country TRI in common currency plus local-currency returns, FX contribution, earnings growth, valuation and risk | Is India/EM gaining relative to US, Europe, Japan and Asia after currency adjustment? | Regional relative-attraction | BLOCKED; accepted synchronized global TRI panel absent |
| Institutional flows | NSE FPI/FII & DII daily cash/derivatives; NSDL/CDSL country/sector flows; global fund flow only with source/method | Are flows persistent, broad-based and confirmed by prices/breadth? | Flow confirmation | BLOCKED for official reconciled panel |
| Breadth / concentration | Advance-decline, equal-weight vs cap-weight, top-10 contribution, sector participation, new highs/lows | Is index performance broadening or carried by a narrow group? | Breadth / concentration-risk | NOT_DONE in GCR synchronized panel |
| Volatility / risk appetite | VIX with exact index identity, realised vol, credit spreads, liquidity proxies | Is the rotation risk-on, defensive or a volatility shock? | Global risk regime | BLOCKED pending versioned aligned series |
| Geopolitics / policy | Official dated event, affected supply/trade channel, exposure and observed price/earnings response | Does the event have a measurable transmission path rather than headline-only sentiment? | Event/catalyst gate | PARTIAL; no headline-only stock inference |

## Evidence rules / computation contract
- Keep local-currency and common-currency return series side by side. Never silently convert; record FX source, timestamp, convention and conversion formula.
- Use total-return indices for equity performance comparisons; price indices alone are not equivalent.
- Align all observations by market close/time zone and retain publication timestamp and vintage. No look-ahead.
- Compare valuation only with compatible definitions, currencies, sector classifications, earnings horizons and dates.
- Separate observed flow, price performance, valuation and analyst narrative. A flow is not proof of destination/beneficiary.
- Rotation requires persistence and breadth tests; one-month relative outperformance is a candidate signal, not a confirmed regime.
- Any stale/missing leg makes the relevant comparison UNKNOWN; no forward-fill, synthetic values or proxy substitution without a separately approved mapping.
- Do not assign factor weights or modify Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 or Engines A–E until synchronized raw panels, deterministic formulas, leakage-safe rolling OOS tests, transaction costs, drawdown, false-positive/missed-winner analysis and ablation pass.
- Research spend remains ₹0; official/free sources preferred. Secondary reports are discovery/context only.

## Priority closure sequence
1. Acquire and validate synchronized official daily macro series: Treasury nominal/real yields; Fed H.10 and FRED broad dollar with overlap/vintage audit; RBI FBIL reference rate; EIA Brent spot.
2. Close official India FPI/DII daily cash + derivatives and sector-flow lineage (NSE/NSDL/CDSL/SEBI), preserving provisional/final status and publication times.
3. Acquire official global and India sector/country TRI histories with exact index IDs, currencies and dividends.
4. Build comparable regional/sector valuation and earnings panel from free official/licensed-public source material; if no free reproducible source exists, mark that factor UNKNOWN rather than scrape paywalled estimates.
5. Implement deterministic relative-attraction calculations and no-lookahead validation in a research-only branch.
6. Run rolling out-of-sample regime/event study and sector-to-stock transmission test; only then submit for explicit review.

## Acceptance state
- User-supplied source review: PARTIAL (4/5 pages accessible; Goldman PDF 403; Franklin collection page is not an individual source report).
- Factor-to-gate mapping: DOCUMENTED / research-only.
- Raw synchronized market panel: BLOCKED / incomplete.
- Predictive edge, factor weights, rolling OOS event study: NOT_DONE.
- Production integration / trade admission: NOT_AUTHORIZED.
- No change to protected production invariants.


## Official India flow route discovery (same continuation; no data archive yet)
- SEBI FPI curation directory explicitly links NSDL and CDSL daily latest, current-month, archive, calendar/financial-year and fortnightly sector-wise FPI series: https://www.sebi.gov.in/curation/fpi.html.
- CDSL historical archive page exposes daily FPI equity/debt/hybrid gross purchases, gross sales, net INR/USD values and conversion rate, plus daily FPI derivative trades: https://www.cdslindia.com/Publications/ArchiveDataAfter2009.aspx. Web-rendered archive view in this review currently showed investment data through 31-Oct-2026 and derivative table through 18-Nov-2026; the page's search-index excerpt surfaced investment rows through 18-Nov-2026. Exact page snapshot/raw export still needs to be captured by a byte-capable runner before ingestion.
- CDSL sector-wise FPI page lists fortnightly sector dates through 15-Nov-2026: https://www.cdslindia.com/Publications/ForeignPortInvestor.html. This provides a plausible official sector-allocation route, but files/column schema and historical coverage must be captured and validated.
- NSE FII/FPI & DII page exposes CSV downloads for NSE-only and combined NSE+BSE+MSEI cash-market activity: https://www.nseindia.com/reports/fii-dii. NSE notes these are provisional and subject to custodial confirmation; final FPI series should be reconciled with NSDL/CDSL.
- CDSL daily FPI page notes its confirmed trade series is compiled from custodian/depository reports and describes its RBI reference-rate conversion convention; retain Equity/Debt/Debt-VRR/Debt-FAR/Hybrid and Stock Exchange vs Primary Market & Others as separate dimensions. Do not collapse gross legs, provisional vs confirmed, or investment routes.
- Source discovery status: PASS for official route identification; raw byte archive, full date coverage, schema, hashes, NSE-vs-depository reconciliation and sector panel remain NOT_DONE/BLOCKED. No FII/DII flow series promoted to production.
