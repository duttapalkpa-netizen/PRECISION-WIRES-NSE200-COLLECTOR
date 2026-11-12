# Global Capital Rotation & Relative-Attraction Overlay V1
## Scope and safety
Research-only overlay for PRECISION-WIRES V11.3. It does **not** change the production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56 × 12), Engine A–E logic, or Hard Gate. It emits provenance-backed categorical diagnostics and horizon divergence, not a composite score, stock ranking, buy/sell instruction, or automatic trade trigger. No PR merge or production integration is authorized by this change.

## Transmission chain
1. **Global capital supply:** official cross-border portfolio-flow aggregates where publicly available; US Fed policy expectations, US 2Y/10Y and real yields, DXY, VIX/credit spreads, and global liquidity. IIF or commercial data are not labelled official and are excluded from the official-source evidence set. If a suitable free official global EM flow series is not verified, this layer is UNKNOWN.
2. **India capture:** NSDL/CDSL FPI equity, debt (General/VRR/FAR separately where possible), hybrid, primary-market and mutual-fund/AIF flows; RBI FX/reserves/BOP; USD/INR; India bond yields; SEBI/NSE positioning where officially disclosed. Separate daily, MTD, monthly and YTD horizons.
3. **Relative attraction:** India versus MSCI EM/World or official comparable broad indices, earnings revisions/growth, valuation differential, macro stability, current-account/oil sensitivity. A single weaker DXY or one positive FPI day is insufficient.
4. **Sector transmission:** event registry covers tariff/trade policy, H-1B/immigration, AI regulation and data-centre capex/power, semiconductors, IT services, pharma, auto/EV, textiles, metals, energy, defence, shipping and financials. Each event must include jurisdiction, official source URL, publication/effective dates, affected sector, channel, direction, confidence and whether it is enacted, proposed, stayed, or merely political commentary. No automatic sector benefit from an election headline.
5. **Stock bridge:** disclosed company revenue/geography, export mix, client concentration, FX sensitivity, import/input costs, order book, earnings sensitivity, liquidity and price/volume confirmation. A sector narrative alone never becomes a stock signal.

## Required observations and provenance
Long-format CSV fields: date, indicator, value, unit, source, source_url, published_at, as_of_date, quality_status. Allowed quality: VERIFIED_OFFICIAL, VERIFIED_SECONDARY, PROVISIONAL, UNKNOWN. Preserve publication date, observation date, retrieval date/time, source vintage, route, gross buys/sells and revisions. Daily depository flows are based on custodian reports and may refer to trades on/up to previous trading days. Do not equate reporting date with real-time execution. Never forward-fill missing flow observations.

Maximum age windows in code are conservative engineering expiry limits, not economic thresholds: EM monthly aggregate 45 days; India FPI/DII daily 7 days; market/FX/oil/relative indicators 7–30 days; policy events 180 days. Use --as-of-date for reproducible runs. Expired data is excluded and reported as stale/UNKNOWN.

Indicator keys include:
- em_portfolio_flow_usd_bn (only if a free official source is verified; otherwise UNKNOWN)
- india_fpi_equity_inr_cr, india_fpi_debt_inr_cr, india_dii_equity_inr_cr
- india_fpi_equity_mtd_inr_cr, india_fpi_equity_ytd_inr_cr
- dxy_change_pct_20d, us10y_change_bp_20d, fed_target_change_bp_90d
- usd_inr_change_pct_20d, brent_change_pct_20d, india_vs_world_relative_return_pct_20d, vix_change_pct_20d
- us_ai_policy_event_direction, us_h1b_policy_event_direction, us_tariff_policy_event_direction

## Interpretation rules
- Global EM outflow and India FPI inflow can coexist; this is country-specific divergence, not proof of broad capital rotation.
- A positive MTD number cannot override a negative YTD number; report both horizons. A short-window reversal is not a durable trend.
- USD weakening alone is insufficient: confirm DXY and USD/INR together and consider local FX intervention and hedging costs.
- Lower US yields are not automatically risk-on: separate real yields, term premium, credit spreads, growth shock and Fed policy expectations.
- Oil decline benefits India only if it is not offset by INR depreciation, taxes, refining margins or a demand shock.
- H-1B, tariffs and AI rules are event-specific. Use primary policy text and effective dates; distinguish proposed legislation from enacted law and court-stayed measures.
- 13F filings are delayed, incomplete for global positioning and not a real-time flow feed; use only as lagged ownership context, never a trigger.
- Do not infer hedge-fund intentions or named institutions' allocation from aggregate depository flow data.

## Evidence snapshot — as of 2026-11-10 (Asia/Kolkata)
### India FPI — official CDSL archive
CDSL archive reports six November trading dates through 09-Nov-2026. Daily equity net investment (INR crore):
- 02-Nov: +4,457.80
- 03-Nov: +3,352.12
- 04-Nov: +7,052.74
- 05-Nov: +7,830.40
- 06-Nov: +16,277.99
- 09-Nov: +14,767.73
- November MTD equity subtotal through 09-Nov: +53,738.78 crore.
- 2026 YTD equity subtotal through 09-Nov: -241,407.13 crore.
- 09-Nov debt combined General + VRR + FAR subtotal: +2,578.19 crore (General -512.72; VRR +49.65; FAR +3,041.26).
These values are transcribed from CDSL's archive, which states that the data are compiled from custodian reports received by depositories on 10-Nov-2026 and represent trades on and up to previous trading day(s). The positive November MTD reversal must be shown alongside the still-negative 2026 YTD total. It does not prove that funds exited US equities and entered India; the two datasets do not identify matched source/destination capital.
Official source: https://www.cdslindia.com/Publications/ArchiveDataAfter2009.aspx
Daily source: https://www.cdslindia.com/eservices/publications/fiidaily

### US political and AI-policy transmission
- 03-Nov-2026 was a US midterm election, not a presidential election. Democrats won control of both chambers of Congress; Donald Trump remained President. Do not describe this as Trump losing the US election or being removed from office.
- Reuters reported that on 05-Nov the Nasdaq fell 5.56% amid investor concern that Democratic lawmakers/governors could pursue data-centre power-cost protections and independent AI testing. This is secondary reporting about political proposals/market expectations, not proof that a federal AI restriction had become law. Store as a WATCH event only until primary bill text, sponsor, status and effective date are verified.
- Reuters reported the dollar index at 101.60, down 0.25%, on 04-Nov and noted US equities rose about 2% that day. AP reported on 09-Nov that the S&P 500 rose 2.3%, Nasdaq 2.7%, and Brent crude fell 5.8% as US equities rebounded. Therefore this was a volatile repricing and rebound, not a one-way US market collapse.
- White House Proclamation 11069 (18-Sep-2026) extended certain H-1B entry restrictions through 21-Sep-2027, subject to stated exceptions. This is not an H-1B easing signal. Any fee/enforcement status potentially affected by litigation must be separately checked against primary court orders before operational interpretation.
- Current DXY 20-day change, US 10Y yield 20-day change, Fed policy repricing, USD/INR 20-day change, Brent 20-day change, India-vs-world relative return, and official global EM flow series were not all independently captured in the official-only seed file. They remain UNKNOWN; no value is imputed.

## Source hierarchy
See docs/GLOBAL_CAPITAL_ROTATION_OFFICIAL_SOURCE_REGISTER_V1.md for the dated source inventory, frequency/coverage checks and measurement caveats. Important: Fed DTWEXBGS is a broad trade-weighted USD index, not ICE DXY; IMF BOP transactions are flows, while IMF PIP/CPIS observations are positions. These must never be conflated.


Official/free first: CDSL/NSDL/SEBI for FPI; RBI for FX/BOP/reserves; Federal Reserve/FRED and US Treasury for rates/yields; EIA for crude; NSE/SEBI for Indian market/sector data; White House/Federal Register/Congress/USCIS and official court records for policy. Secondary news (Reuters/AP) is contextual event discovery only, not an official policy source. IIF is not a government source and is excluded from the official-only evidence dataset. No paid feeds, subscriptions or API spend.

## Status and limitations
This overlay's schema, parser, categorical diagnostics and tests exist on PR #20. This does **not** mean live collection, full global-flow coverage, predictive validation or production integration is complete. Current evidence confirms a short-window India FPI equity inflow alongside a negative YTD position; broad global rotation is unconfirmed because official global EM flow, DXY/yields, FX, relative-return and sector-specific exposure inputs are incomplete.

No named hedge-fund real-time holdings are inferred. Public 13F filings are delayed and US-centric. India daily FPI data are depository/custodian-derived and lagged. Missing/stale/unverified values remain UNKNOWN.


## H.10 historical FX / dollar panel recovery update — 2026-11-12
A research-only full-history daily panel was successfully acquired from the public FRED CSV distribution route for the three modern Board H.10 dollar indices and all 23 bilateral daily FX series identified in the H.10 Library snapshot.

Evidence:
- Collector workflow run: 43276577238 (SUCCESS)
- Run: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/43276577238
- Artifact ID: 13970661965
- Artifact ZIP SHA-256: a6f6af42226ed689ceba8e9c2d843867d82e9aa8f9a7761022c86bd719ef3691
- 26/26 raw series files SHA-256 verified; artifact ZIP digest independently recomputed and matched.
- 304,510 total dated observation rows; 291,831 numeric observations; 12,679 missing-value markers retained without forward-fill.
- Date union: 1971-01-04 to 2026-11-06 (14,570 unique dates).
- H.10 panel acceptance ledger: 6.5/8 = 81.25% using eight equal-weight gates; exact NSE 200-session join is PASS, while point-in-time vintage availability remains UNKNOWN/PENDING. Repository binary archive / overlay integration and matched diagnostic validation remain pending.
- Exact pinned NSE calendar: 200 sessions (2026-01-21 to 2026-11-12); 200/200 NSE raw files and 26/26 H.10 raw series hashes verified.
- Every H.10 series has 190/200 numeric observations (95.00%); six explicit source-missing markers and four no-source-row dates are preserved as blank. No forward-fill.

Measurement boundaries:
- The three Federal Reserve dollar indexes are broad/AFE/EME trade-weighted indices, not ICE DXY and not portfolio flows.
- The 23 bilateral FX series preserve source quote direction. Four are USD per foreign currency; the remaining 19 are foreign currency per USD.
- DEXINUS is the Federal Reserve H.10 noon buying rate in New York, not RBI reference fixing or DBIE interbank close.
- Missing observations remain missing. No forward-fill, synthetic observations, or unverified vintage claims.
- This is FX/rate evidence, not proof that capital flowed from one country to another.

Global Capital Rotation Overlay progress remains 62.5% (5/8) pending completion of the broader synchronized macro/flow panel, exact NSE-calendar joins, relative-attraction and sector bridge, and matured validation. H.10 subpanel progress must not be substituted for overall overlay completion. Production integration remains prohibited; selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 and Engines A–E are unchanged.
