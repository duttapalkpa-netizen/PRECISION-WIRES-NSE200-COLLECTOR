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


## Verified Fed H.10 broad-dollar diagnostic — 2026-11-15

The previously acquired workflow artifact was downloaded and independently revalidated in this audit:
- Run: 43276577238 (SUCCESS); artifact ID: 13970661965.
- Downloaded ZIP size: 3,462,888 bytes.
- ZIP SHA-256 recomputed: `a6f6af42226ed689ceba8e9c2d843867d82e9aa8f9a7761022c86bd719ef3691` (matches the previously recorded digest).
- All 26/26 raw series files independently match the byte sizes and SHA-256 values in the embedded manifest.
- Both derived panel CSV files independently match their manifest byte sizes and SHA-256 values.
- Federal Reserve H.10 series `DTWEXBGS` (Nominal Broad U.S. Dollar Index) has 5,440 dated rows from 2006-01-02 to 2026-11-06; 5,227 numeric observations and 213 source-missing observations.
- On the last 21 valid published observations (2026-10-08 to 2026-11-06), the 20-observation interval change is +0.3568637816%.
- This is a broad trade-weighted USD index, **not ICE DXY**. It is now stored under the distinct key `fed_broad_usd_change_pct_20d`; it must not populate `dxy_change_pct_20d` or satisfy the DXY+USD/INR paired FX diagnostic.
- Derived research-only observation: `data/global_capital_rotation/fed_h10_derived_observation_2026-11-06.csv`.
- No missing value was forward-filled. The calculation uses 21 valid observations to measure 20 intervals; source gaps outside those valid endpoints are not imputed.

This adds a verified broad-dollar input only. It does not establish capital flows, an ICE DXY observation, a synchronized USD/INR panel, sector transmission, predictive value, or production readiness.

## Source freshness correction — 2026-11-17
- CDSL live Daily Trends page currently displays 16-NOV-2026 as its latest investment reporting date. Do not treat the 17-Nov page-access date as a 17-Nov investment observation. Accepted 16-Nov Equity sub-total is +₹5,564.90 crore (gross buys 18,571.97 less gross sales 13,007.07); five-category FPI subtotal +₹4,845.93 crore; Mutual Funds separately -₹18.74 crore; page total +₹4,827.19 crore. The 17-Nov investment figures previously stated in a checkpoint are withdrawn/rejected.
- Official Federal Reserve H.10 DDP page (last release 16-Nov-2026) exposes a 26.2 MB single XML/SDMX ZIP download. Exact link: https://www.federalreserve.gov/datadownload/Output.aspx?filetype=zip&rel=H10. The binary fetch was rejected by the available inspection layer and a local download attempt failed; no raw archive, hash, XML parse, or extracted observations are claimed from this step.
- Fed DDP announcement says Build Your Package was retired 12-Nov-2026; historical XML remains available on Board release pages and full-history FRED API v2 retrieval requires an account/API key. See https://www.federalreserve.gov/data/data-download-fred-information.htm.
- Until a raw payload is acquired and hashed, H.10 full-history ingestion remains NOT_DONE. Do not calculate a fresh H.10 return from the 10-observation preview or splice series with incompatible base-year metadata.


## Brazil September-2026 portfolio outflow: India transmission relevance and overlay treatment — 2026-11-17

### Official observations
- BCB External Sector Statistics, released 26-Oct-2026, reports September-2026 domestic-market portfolio investment net outflows of USD 2.1bn: equity/investment funds USD 1.7bn and debt securities USD 0.4bn. The same release reports a positive USD 5.1bn net inflow over the trailing 12 months through September. This is a one-month country-specific flow observation, not evidence of persistent Brazil-wide or global capital flight.
- RBI preliminary India BoP release, 13-Nov-2026, reports September-2026 net foreign portfolio investment of -USD 6.7bn, including -USD 6.5bn FPI investment in India; April-September 2026 cumulative net FPI was -USD 8.9bn. These India observations are direct domestic-market evidence and have greater relevance to Indian market transmission than Brazil's country-specific monthly flow.
- RBI's October-2026 Financial Stability / macro-financial commentary states FPI flows to India and other emerging-market portfolio flows have been net sold since September, driven by renewed West Asia tensions, elevated crude prices and rising global bond yields. RBI also describes Indian equities as bearish in September and October (through 19-Oct), with FII selling pressure partly offset by DII net buying.

### Interpretation and hard boundary
- Brazil's USD 2.1bn monthly outflow is useful as **cross-country corroborative context** for global risk appetite / emerging-market capital rotation. It is not a direct causal input for India and cannot quantify the impact on NIFTY, sectors or individual Indian stocks.
- Do not compare USD 2.1bn Brazil directly as a market-impact magnitude against India's USD 6.7bn FPI outflow: country coverage, reporting definitions, investor perimeter and balance-of-payments treatment are not yet harmonized. The juxtaposition is directional context only.
- The BCB release's positive trailing-12-month USD 5.1bn net inflow cautions against interpreting the single September monthly outflow as a persistent structural exit.
- Overlay classification: `BRAZIL_PORTFOLIO_FLOW_CONTEXT` = contextual corroboration / low direct India-transmission confidence. It may appear in a global risk-appetite evidence panel with source date, reference month, horizon and definition; it must not receive an independent India stock score, direct NIFTY directional weight, buy/sell trigger, or production selector input.
- India-specific FPI flows, DXY/broad USD (kept distinct), USD/INR, US yields, VIX, crude, NSE breadth/price-volume and DII offset are the direct transmission set to test. Cross-country confirmation should be evaluated only after synchronized dates and historical event-study tests; no predictive coefficient or impact percentage is asserted.

### Research decision
Brazil September-2026 outflow: retain as contextual evidence only; exclude from direct India transmission scoring and trading triggers. This is a classification decision, not a claim that Brazil flows never matter. No production change.



## Daily market temporal-alignment guard — 2026-11-17

The research classifier now emits `temporal_alignment.daily_india_market_panel` for the latest non-stale observations among India FPI equity/debt, DII equity, USD/INR, Brent, VIX, India-vs-world relative return, ICE DXY (if separately supplied), Fed broad USD, and US 10Y. This is a calendar-date proximity audit only:
- `ALIGNED_WITHIN_3D`: at least two available inputs and the maximum observation-date spread is no more than 3 calendar days.
- `UNSYNCHRONIZED`: at least two available inputs and the maximum spread exceeds 3 calendar days. Do not treat the combined cross-market snapshot as synchronized.
- `NOT_ASSESSED`: fewer than two available inputs.
- The report lists included dates and excluded missing/stale indicators. No date is forward-filled, and no values are interpolated.

Important limitation: calendar-date proximity does not prove same-session availability, common publication vintage, common market close, or causal comparability. A full synchronized panel still requires immutable raw archives, source publication/retrieval timestamps, trading-calendar mapping and vintage QA. Monthly EM flow remains a separate low-frequency layer and is not forced into the daily synchronization group. This guard does not create an EM aggregate or a Relative-Attraction score and has no production effect.
