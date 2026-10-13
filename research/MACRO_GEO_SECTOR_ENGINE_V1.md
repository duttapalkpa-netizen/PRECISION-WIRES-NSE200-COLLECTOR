# Macro–Geopolitical Sensitivity & Sector Rotation Engine — V1 research specification

Status: RESEARCH DESIGN / AUDIT BRANCH ONLY. Not a production selector. Not a claim that a live data feed is connected.

## Purpose
Add a regime-aware external-context layer to PRECISION-WIRES without changing Run #58, production selector, RANKING_SCORE, collector, QA, 200-session backbone, 672 diagnostic architecture, or +1 PRESSURE_FADE. It must be a risk modifier and sector-relative explanation layer first, not a hard gate.

## Historical evidence window and event map (2006–2026)
Use event studies around these regimes, with actual daily data and point-in-time news timestamps before assigning empirical sensitivity:
- 2007–09 global financial crisis / Lehman: global risk aversion, funding stress, FPI outflows, earnings downgrades.
- 2010–11 euro-area sovereign stress and oil/inflation pressure.
- 2013 taper tantrum: US yields/USD, INR depreciation, foreign-flow stress.
- 2015 China/commodity slowdown: global growth, commodity exporters/importers, risk aversion.
- 2016 demonetisation and domestic liquidity shock; distinguish domestic-policy shock from global shocks.
- 2018 IL&FS/NBFC liquidity crisis: domestic credit/liquidity transmission, NBFC/bank dispersion.
- 2020 COVID crash and recovery: lockdown, oil-demand collapse, policy liquidity, sector divergence.
- 2021–22 reopening, inflation, synchronised global tightening and Russia–Ukraine energy/food shock.
- 2023 global banking stress and AI-led technology repricing.
- 2024 election-result surprise and yen-carry unwind / global volatility.
- 2025–26 geopolitical and energy-risk regimes: use only timestamped, verified observations; do not infer causality from headlines alone.

## Provisional research priority (not yet empirical ranking)
1. Global risk appetite + foreign portfolio flows (FPI/FII), USD strength, US real yields and global volatility.
2. Crude oil / energy and shipping-route disruption, because India is a net oil importer; include the offsetting benefit to upstream producers and the possible lag/price-control effects for downstream OMCs.
3. Domestic earnings breadth, earnings revisions, valuation and earnings delivery.
4. INR, current-account/fiscal/inflation transmission and bond yields.
5. Fed policy surprise and forward guidance; distinguish expected vs unexpected moves and real-yield/USD channels.
6. RBI policy surprise, liquidity stance, banking-system liquidity and domestic bond yields.
7. Domestic growth/demand, monsoon, food inflation, government capex and fiscal policy.
8. Sector-specific catalysts: orders, regulation, commodity input prices, product cycle, capacity, credit costs, pricing power and earnings guidance.
9. China/global industrial cycle and metals/chemicals/commodities.
10. Political/regulatory events, elections, taxation and market microstructure/surveillance.

The order is a starting prior for data collection, not a permanent weight. Empirical event-study and rolling predictive tests must be allowed to reorder it. Avoid double-counting correlated channels (e.g. crude, INR, CPI and yields).

## Sector transmission map
- Banks/NBFCs: RBI/Fed rates, yield curve, deposit costs, credit growth, credit costs, liquidity, FPI flows; rate hikes are not mechanically bearish if margins/credit quality improve.
- IT services: US growth/spending, USD/INR, US yields, AI demand/disruption, deal wins and guidance.
- Oil marketing companies/aviation/paints/tyres/chemicals: crude and freight/input costs, pass-through ability, inventory gains/losses; do not apply a uniform oil shock sign.
- Upstream oil & gas: realised crude/gas prices, taxes, windfall levies, production and policy.
- Metals/mining: China stimulus/property/industrial demand, USD, global commodity prices, tariffs.
- Pharma/healthcare: USFDA/regulatory events, US pricing, product approvals, launches, currency and input costs; may be relatively defensive, not guaranteed to outperform.
- Defence/capital goods/railways/power/grid: order inflow, execution, government capex, policy, valuations, working capital and cash conversion.
- Autos/auto ancillaries: rates/financing, rural demand, fuel, steel/aluminium/rubber, EV transition, inventory and export demand.
- FMCG/consumer discretionary: rural/urban demand, food inflation, monsoon, real wages, input costs and pricing power.
- Telecom/digital platforms: ARPU, tariff/regulation, subscriber growth, competition and capex.
- Real estate/cement: rates, affordability, cement/energy costs, project launches, inventory and local demand.
- Gold-linked businesses: global gold, USD/INR, real yields and risk aversion.

## Live Regime Rank — required logic
Compute a daily factor state from verified data:
- direction and magnitude vs rolling 1y/3y distribution;
- surprise vs consensus where available;
- persistence (1/5/20 sessions), acceleration and reversal;
- transmission confirmation (e.g. crude move + INR/yields/FPI response);
- sector/index relative strength and breadth;
- news confidence/source timestamp and whether the information was known before the market close.
Output factor-level states: POSITIVE / NEGATIVE / MIXED / UNKNOWN, severity 0–5, confidence 0–1, and affected sectors with channel explanations. UNKNOWN must never become NEGATIVE.

## Historical research protocol (20 years)
1. Build point-in-time daily panel: NIFTY 50, NIFTY sector indices, stock returns, INR, Brent crude, US 2y/10y and real yields where available, DXY, VIX/India VIX, FPI flows, RBI repo/liquidity, inflation, bond yields, sector/stock earnings revisions and event timestamps.
2. Separate anticipated policy moves from surprises; use announcement windows (event day, +1, +5, +20 sessions) and matched non-event controls.
3. Estimate index/sector/stock abnormal returns, volatility, drawdown, dispersion and recovery; account for overlapping events and changing index constituents.
4. Test regime dependence and lag effects; report confidence intervals and sample sizes, not just averages.
5. Rolling / walk-forward out-of-sample validation; no look-ahead, survivorship bias, or news published after the cutoff.
6. Measure incremental value over technical-only V11.3: precision/capture for +5% H+1, +10% H+3, +20% H+5; drawdown and false-rejection rates; sector-relative winner capture.
7. Keep historical event studies separate from the prospective ledger. Require at least 30 fully matured prospective cutoffs per target before any promotion. Do not promote without paired confidence interval, cost/liquidity/slippage and circuit audit.

## Daily output contract
- Macro/Geo Regime: label + severity + confidence + evidence timestamps.
- Factor ranking: historical prior beside live regime rank; show what changed and why.
- Sector rotation: leading/lagging sectors, relative strength, catalyst, confirmation and invalidation condition.
- Stock context: sector-relative strength and relevant factor exposure; explain both positive and negative transmission.
- Risk modifier: cautious / neutral / supportive, with uncertainty retained.
- Never issue a stock solely because a headline sounds positive. Require the existing technical/volume/path checks and first-hour confirmation (9:50–10:00 IST) before actionable classification.

## Integration boundaries / next implementation steps
Phase 1: add this specification and machine-readable factor registry to the audit branch.
Phase 2: inventory available columns and data-source coverage; build QA for missingness, timestamp, unit and revision history.
Phase 3: implement historical event-study dataset and sector transmission features as separate audit outputs.
Phase 4: run walk-forward incremental-value tests and compare with the frozen baseline.
Phase 5: only after evidence, propose a reviewable PR for optional Risk Modifier inputs. Production selector and RANKING_SCORE remain unchanged until explicit evidence-based approval.

## Source notes
- RBI Annual Report 2008–09 documents the GFC drawdown, global linkage and FII outflows.
- RBI Bulletin discusses volatility episodes including the 2008–09 GFC, 2013 taper tantrum, 2018 IL&FS, COVID, Russia–Ukraine, global tightening and 2024 yen-carry unwind.
- IMF India Article IV (2025) estimates that a 10% oil-price rise historically lowered real GDP growth by about 20 bps and raised CPI inflation by 30–40 bps, while noting that retail-price pass-through has recently been moderated by OMC pricing.
- A 2021 Journal of International Money and Finance study finds stronger Indian equity sensitivity to US monetary shocks since the early 2000s, transmitted through exchange rates, foreign institutional flows and global risk aversion.
- An open-access 2026 study examines global and India-specific geopolitical risk across 28 broad and sectoral NSE indices through Feb 2025.
- These references motivate tests; they do not by themselves determine the final ranking or prove a tradable edge.
