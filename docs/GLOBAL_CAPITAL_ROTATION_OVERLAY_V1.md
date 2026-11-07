# Global Capital Rotation & Relative-Attraction Overlay V1

## Scope and safety
Research-only overlay for PRECISION-WIRES V11.3. It does **not** change the production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, or Hard Gate. It emits transparent categorical diagnostics, not a score, ranking, buy/sell instruction, or automatic trade trigger.

## Transmission chain
1. **Global supply of capital:** IIF nonresident portfolio flows to EM (equity and debt separately when available); Fed target-rate changes; US 2Y/10Y yields and real yields; DXY; VIX; global liquidity/credit stress.
2. **India capture:** NSDL/CDSL FPI equity/debt/hybrid flows, primary-market flows, RBI FX and balance-of-payments data, USD/INR, India bond yields, FII futures positioning where published.
3. **Relative attraction:** India vs MSCI EM/World returns, earnings revisions/growth, valuation differential, macro stability, current-account/oil sensitivity. Relative attraction is UNKNOWN until comparable sourced inputs exist.
4. **Sector transmission:** policy/event registry tags tariff, H-1B/immigration, AI regulation/capex, semiconductors, IT services, pharma, auto/EV, textiles, metals, energy, defence, shipping and financials. Each event requires issuer, jurisdiction, publication time, effective time, source URL, affected sector, transmission channel, direction and confidence. No automatic sector benefit from a political headline.
5. **Stock-level bridge:** sector revenue/geography/export exposure, client concentration where disclosed, FX sensitivity, input cost, order book, earnings sensitivity, liquidity and price confirmation. Sector-level story alone never becomes a stock signal.

## Required observations
Long-format CSV fields: date, indicator, value, unit, source, source_url, published_at, as_of_date, quality_status. Allowed quality: VERIFIED_OFFICIAL, VERIFIED_SECONDARY, PROVISIONAL, UNKNOWN. Keep publication date, observation date and retrieval time distinct. Preserve source vintage and revisions. Never forward-fill a missing daily flow; stale data remains stale/UNKNOWN.

Indicator keys:
- em_portfolio_flow_usd_bn
- india_fpi_equity_inr_cr, india_fpi_debt_inr_cr, india_dii_equity_inr_cr
- dxy_change_pct_20d, us10y_change_bp_20d, fed_target_change_bp_90d
- usd_inr_change_pct_20d, brent_change_pct_20d, india_vs_world_relative_return_pct_20d, vix_change_pct_20d
- us_ai_policy_event_direction, us_h1b_policy_event_direction, us_tariff_policy_event_direction

## Interpretation rules
- EM net outflows can coexist with India-specific FPI inflows; this is a country allocation divergence, not proof of broad capital rotation.
- USD weakening alone is insufficient: check USD/INR, local FX intervention/flows and hedging costs.
- Lower US yields are not always risk-on: distinguish real yields, term premium, credit spreads, growth shock and policy expectations.
- Oil decline benefits India only if it is not offset by INR depreciation, taxes, refining margins or demand shocks.
- H-1B, tariffs and AI regulation are event-specific. Use primary official policy text and effective dates; do not infer from election narratives.
- 13F filings are delayed, incomplete for global positioning and not a real-time flow feed; use only as lagged ownership context, never a trigger.

## Current evidence snapshot (2026-11-07)
- IIF November tracker (released 2026-11-05): nonresident portfolio flows to EM were -$33.8bn in October 2026, after -$19.3bn in September. This is aggregate EM, not India alone.
- CDSL daily FPI report (06-Nov-2026): equity subtotal +₹16,277.99 crore; debt total across General/VRR/FAR subtotals +₹3,191.88 crore; hybrid -₹29.71 crore. Data are based on custodian reports and trades on/up to previous trading days; avoid treating as final same-day execution.
- The coexistence of October EM outflows and a positive 06-Nov India daily FPI print demonstrates why global and India flows must be tracked separately; it does not establish a durable trend.
- FOMC 2026-10-28: target range maintained at 3.75%-4.00%; inflation remained elevated.
- White House 2026-09-18: extended certain H-1B entry restrictions for 12 months; $100,000 payment condition with exceptions. This is not a visa-easing signal.
- US midterm election market reaction (AP, 2026-11-04): US equities rose after Republicans lost control of Congress; selected AI-related shares weakened amid regulation/data-centre concerns. Do not label this a broad US market crash or an AI-sector crash.
- EIA weekly Brent data showed elevated and volatile prices into early November; oil must be treated as an India macro sensitivity, not assumed to be falling.

## Source hierarchy
Official first: IIF tracker for global flow aggregates; NSDL/CDSL for FPI; RBI for FX/BOP; Federal Reserve/FRED for rates and dollar; EIA for crude; NSE/SEBI for market/sector data; White House/Federal Register/USCIS/Congress for policy. Secondary news is context only. No paid feeds, no API subscriptions.

## Limitations
No fund-level real-time holdings are available from public 13F/quarterly filings; these are delayed and US-only. IIF is monthly aggregate. India daily FPI is lagged/provisional depending on feed. Never infer named hedge-fund intentions from aggregate flows.
