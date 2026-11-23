# PRECISION-WIRES V11.3 — Daily Unified Top-5 Swing Watchlist
**Report date:** 2026-11-23 | **Review:** 08:45 IST | **Data cutoff:** NSE 20-Nov-2026 EOD  
**Decision:** 1 observation-only qualified watch candidate; fewer than five. Not a buy instruction.

## Executive alert — target capture performance

**Important acceptance caveat:** Run #398's walk-forward metrics file reports the following arithmetic, but the same artifact's supposed 200-session spine contains 12 NSE holidays duplicated as prior sessions. Row-level predictions are not retained to remove those duplicate cutoffs and recompute the metrics. Therefore every artifact figure below is **PROVISIONAL / NOT ACCEPTED**; the verified performance rates for this report remain UNKNOWN.

| Target | Artifact-reported TP / evaluated n | Artifact-reported hit rate | Artifact-derived FP | Accepted verified rate |
|---|---:|---:|---:|---|
| +2% | UNKNOWN | UNKNOWN | UNKNOWN | **UNKNOWN** — target absent |
| +5% H+1 | 965 / 2,976 | 32.43% | 2,011 | **UNKNOWN** — date spine invalid |
| +10% H+3 | 637 / 2,892 | 22.03% | 2,255 | **UNKNOWN** — date spine invalid |
| +15% H+5 | 399 / 2,830 | 14.10% | 2,431 | **UNKNOWN** — date spine invalid |
| +20% H+5 | 197 / 2,830 | 6.96% | 2,633 | **UNKNOWN** — date spine invalid |

These are historical excursion labels in a 100-cutoff / 3,000-row Top-30 audit, not profitable trade returns, win rates, or cost-adjusted returns. Artifact recall values (+5 4.08%, +10 3.62%, +15 3.19%, +20 3.49%) are also not accepted until the unique-session rerun. +2% is not present in the metrics file.

## 1. Three engine scorecards

| Engine | Status | Evidence used today |
|---|---|---|
| **A — V11.4 Historical Behavioural Selector** | **PARTIAL / NOT ACCEPTED** | Run #398 has a corrected-label test and walk-forward metrics, but the 200-session input includes 12 holiday duplicates; no row-level predictions are retained for a clean rerun. The artifact also reports winner-probability mean 0.086886 versus non-winner 0.087184 inside Top-30, so ranking separation is not demonstrated. No A boost is applied. |
| **B — V11.3 Cost-aware Trade Replay** | **UNKNOWN** | No user-approved entry/exit/stop/circuit/cost assumptions and no independently reconciled trade ledger. |
| **C — Global Capital Rotation** | **UNKNOWN** | Macro-Geo P0 remains blocked; filing timestamp timezone semantics are not verified; no vintage-aligned macro → sector → stock → matured-outcome join. No GCR boost. |

### Target-wise historical best-three stocks
For each of +2%, +5%, +10%, +15%, +20%: **qualified historical leaders <3 / UNKNOWN**. The retained artifact has aggregate target metrics but no independently verified per-symbol matured outcome table, and the date spine is not accepted. No names are ranked by a single extreme move or immature result.

## 2. Data, universe and method

- **Latest equity session:** Friday 20-Nov-2026. No 23-Nov live/pre-open quote was available at the 08:45 review.
- **Raw source:** official NSE full bhavdata CSV for 20-Nov; source URL below. File retrieved 22-Nov-2026 14:00:42.495300 UTC; publication timestamp not provided by the manifest.
- **Universe:** Run #398 security-master / bhavdata universe, 2,999 symbols before screening. Established research base filters: EQ series, price >₹50, prior-20-session average volume >200,000 shares; then trend, RSI, volume expansion, liquidity, official catalyst and risk checks.
- **Archive correction:** 200 raw files and hashes pass byte integrity, but only 188 unique internal DATE1 trading dates are present. Twelve requested dates are NSE holidays and exact duplicates. Technical indicators below were recomputed after de-duplicating by internal DATE1; no holiday duplicate was counted as a session.
- **Indicators:** EMA20/EMA50 from unique-session CLOSE_PRICE series; RSI14 Wilder-style smoothing; volume ratio = 20-Nov volume / mean volume of prior 20 unique sessions. These are research calculations, not production selector changes.
- **Market context:** NIFTY 50 +1.12%, NIFTY 500 +0.80%, NIFTY Metal −0.23% on 20-Nov. Textile-specific sector index data were not verified. Relative strength is benchmark context only; no GCR boost.
- **24-Nov-2026:** NSE equity-market holiday; therefore 23-Nov H+1 matures after the 23-Nov close, H+3 after 25-Nov close and H+5 after 27-Nov close.

## 3. Qualified candidate

<badge color="success">1 qualified observation-only candidate</badge>

### WELSPUNLIV — Welspun Living Limited
- **Exchange / identity:** NSE EQ; ISIN `INE192B01031` (matches NSE quote page and archived security master).
- **Last official EOD data:** 20-Nov-2026 NSE live-market table shows `LTP ₹263.80` (+4.21% vs ₹253.14 previous close); the raw bhavdata row separately records `LAST_PRICE ₹263.80` and `CLOSE_PRICE ₹268.78` (+6.18% close-field change). These official fields differ; the target scenarios below are explicitly calculated from the bhavdata CLOSE_PRICE field ₹268.78, not from LTP. Do not collapse the two fields; reconcile before any executable use. No 23-Nov live price is claimed.
- **Price-volume / trend (188 unique sessions):** 1-session close-field return +6.18%; 5-session +7.45%; 20-session +25.63%; EMA20 ₹245.71; EMA50 ₹228.23; RSI14 63.56; 20-Nov volume 21,258,542 shares vs prior-20-session average 11,004,795 (1.93×); traded value ₹565.16 crore vs prior-20-session average ₹268.10 crore; deliverable quantity 10.71%.
- **Relative-strength context:** 20-Nov NSE live-market LTP return +4.21% vs NIFTY 500 +0.80% (+3.41 percentage points); raw bhavdata CLOSE_PRICE field implies +6.18% (+5.38 points). This range is shown because CLOSE_PRICE and LAST_PRICE differ in the official bhavdata row.
- **Industry / sector:** NSE basic industry “Other Textile Products”. Textile-specific sector-index return: UNKNOWN.
- **Fresh catalyst:** NSE filing dated 21-Nov-2026 reports board approval for up to ₹3,200 crore capex in wholly owned Welspun Home Solutions Limited, including terry-towel capacity expansion and backward integration. The filing describes up to ₹800 crore investment by the parent and up to ₹2,400 crore subsidiary borrowing; long implementation horizon and financing/execution risks apply. Official filing link below.
- **Liquidity:** 20-session average traded value about ₹268.10 crore; 20-Nov value ₹565.16 crore; NSE quote snapshot reports impact cost 0.05. Liquidity appears adequate in the archived session, but actual 23-Nov spread/order book is UNKNOWN.
- **Risk / circuit / surveillance:** latest accessible NSE quote snapshot dated 19-Nov shows EQ, Active, 20% price band, 2.90% daily / 55.40% annualised volatility; it also flags P/E >50 for the prior four trailing quarters and >75% close-to-close movement over the prior six months. Exact 23-Nov price band and current ASM/GSM/surveillance state are UNKNOWN until refreshed. Low delivery percentage (10.71%) increases the need to verify follow-through.
- **Research invalidation markers, not an approved stop:** 20-Nov low ₹249.50 and computed EMA20 ₹245.71. Stop order / stop distance: UNKNOWN; no user-approved stop assumptions were supplied.
- **Scenario target prices from ₹268.78 close (not forecasts or guaranteed returns):**

| Target | Scenario price | Research horizon |
|---|---:|---|
| +2% | ₹274.16 | H+1 |
| +5% | ₹282.22 | H+1 to H+3 |
| +10% | ₹295.66 | H+3 |
| +15% | ₹309.10 | H+5 |
| +20% | ₹322.54 | H+5 |

- **Engine attribution:** A = no accepted historical probability score; B = UNKNOWN; C = UNKNOWN. The observation qualifies only on independent price-volume/trend + a fresh official filing, not on a fabricated combined engine score and not as a production-selector rank.

## 4. Exclusions / rejected shadow candidates

| Symbol | 20-Nov evidence | Reason not qualified |
|---|---|---|
| NRL | Close ₹184.36; 5-session +140.65%, 20-session +217.42%; RSI14 86.47; turnover ~₹3.42 crore; volume 0.76× average | Extreme extension, low liquidity, unresolved ISIN mismatch and prior BE / 5% band / 100% margin context. |
| V2RETAIL | Close ₹162.06; volume 4.11× average, but 5-session −1.24%, 20-session −4.75%; below EMA50; RSI14 48.73 | Volume spike without trend confirmation; previous promoter-sale disclosure is a supply risk. |
| SIGACHI | Close ₹30.57; volume 8.81× average | Below established ₹50 base-universe floor. |
| RSDFIN | Close ₹82.92; only 195 shares traded; turnover ~₹0.0016 crore | Illiquid; fails average-volume / tradability screen. |
| KDDL | Close ₹4,620.70; 5-session +10.99%, 20-session +26.21%; volume 0.77× average | Trend is positive but no fresh verified catalyst and volume below average. |
| YATRA | Close ₹89.02; 5-session +13.94%; below EMA50; RSI14 ~53.3; volume 0.45× average | Weak trend/volume confirmation; latest earnings context is mixed. |
| KMCSHIL | Close ₹203.78; 5-session +21.38%, 20-session +34.49%; RSI14 74.24; volume 1.05× average | Extended, no fresh official catalyst verified, no meaningful volume expansion. |
| HINDOILEXP | Close ₹216.82; 5-session +12.69%, 20-session +31.64%; volume 0.39× average | Low current volume; prior ST ASM-1 / valuation warnings require fresh verification. |
| APLAPOLLO | Close ₹2,121.60; 5-session −5.77%; below EMA20/EMA50; RSI14 ~43.5 | Weekend acquisition catalyst is material, but price structure has not confirmed; event-only, not qualified. |
| TATASTEEL | Close ₹178.00; 5-session −4.65%; below EMA20/EMA50; RSI14 ~47.2 | Asset-sale catalyst but weak technical structure; NIFTY Metal −0.23% on 20-Nov. |
| HMAAGRO | Close ₹33.91 (<₹50), +15.58% on 20-Nov; volume 1,129.70 lakh | Outside the existing base universe. NSE shows board-outcome broadcast at 16:03:44, after the 16:00 close; do not attribute the earlier same-session rise to that later disclosure. |

## 5. Failure & missed-winner audit

- Previous 20-Nov shadow cohort: 8 unique symbols / 10 rows. At 08:45 on 23-Nov, **matured outcomes = 0**; false positives = UNKNOWN/PENDING; target-wise missed winners = UNKNOWN/PENDING.
- HMAAGRO is a same-session price mover outside the >₹50 base universe, not a post-cutoff eligible-universe missed winner. Its official board outcome was broadcast after the session close; hindsight attribution to the earlier price rise is not allowed.
- APLAPOLLO and TATASTEEL are event-driven names, but their 20-Nov technical structure was weak; excluding them from the qualified list avoids a catalyst-only false positive.
- No new production filter, threshold or selector change is proposed.

## 6. Today’s learning → research addition → next verification
1. **Holiday-aware session spine:** add `PW-LSN-20261123-001`; fix the 200-session claim before using walk-forward metrics.
2. **Timezone semantics:** add `PW-LSN-20261123-002`; preserve raw NSE timestamp text and block UTC joins until the timezone contract is proven.
3. **Hindsight discipline:** HMAAGRO's post-close filing cannot explain its earlier session move; test universe-floor sensitivity only in a separate shadow audit, with no production change.
4. **Next verification:** corrected unique-session backfill (188 valid existing + 12 earlier valid sessions), DATE1/manifest regression, NSE timestamp contract test, then row-level matured target recalculation.

## 7. GitHub evidence
- Run #398 / ID `45027842316`: overall `prospective-audit` job CANCELLED at Macro-Geo P0 collection; earlier acquisition/hash/date-label steps completed.
- Artifact ID `14757294944`; head SHA `7360870b768a6ed746451afa96ea918a3bffae07`; ZIP SHA-256 `212a84103f2a9f47681865c7e165fe0247001b02d9563a5cef578636fb0b1898` (independently verified).
- Detailed audit: [NSE 200-session semantic date audit](NSE_200_SESSION_ARCHIVE_SEMANTIC_DATE_AUDIT_20261123.md)
- Failure log: [2026-11-23 lessons](FAILURE_LESSONS_LEARNED_20261123.md)
- Official NSE sources:
  - [NSE 20-Nov live equity-market row (LTP, volume, traded value)](https://www.nseindia.in/market-data/live-equity-market?symbol=NIFTY+TOTAL+MKT)
  - [WELSPUNLIV quote / announcement page](https://www.nseindia.in/get-quote/equity/WELSPUNLIV/Welspun-Living-Limited)
  - [WELSPUNLIV official board outcome PDF](https://nsearchives.nseindia.in/corporate/WELSPUNIND_21112026191142_Reg30_Outcome_21112026_signed.pdf)
  - [20-Nov NSE bhavdata CSV](https://nsearchives.nseindia.com/products/content/sec_bhavdata_full_20112026.csv)
  - [NIFTY 500 20-Nov snapshot](https://www.nseindia.in/index-tracker/NIFTY%20500)
  - [NSE 2026 trading-holiday circular](https://nsearchives.nseindia.com/content/circulars/CMTR71775.pdf)
  - [HMAAGRO 20-Nov NSE quote](https://www.nseindia.in/get-quote/equity/HMAAGRO/HMA-Agro-Industries-Ltd)
  - [HMAAGRO official board outcome PDF](https://nsearchives.nseindia.in/corporate/HMA_20112026160306_OutcomeofBoardmeeting20112026.pdf)

## 8. Invariants
Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 remain unchanged. No paid API, no synthetic data, no fabricated timestamps, no guessed mappings. UNKNOWN is never PASS.
