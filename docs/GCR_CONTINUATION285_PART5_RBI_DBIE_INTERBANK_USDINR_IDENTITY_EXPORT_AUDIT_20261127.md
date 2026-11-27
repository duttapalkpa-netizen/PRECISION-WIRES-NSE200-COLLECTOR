# GCR Continuation 285 — Part-5 RBI DBIE daily interbank USD/INR identity and export-route audit
Date: 27-Nov-2026

## Mandatory preflight and duplicate prevention
Re-read Master Continuity Ledger, GCR Master Priority Queue, 63-country Historical Task Registry and C284 Part-4 report. Re-searched Library and read the existing Page-32 DBIE access/provenance gate, Page-33 official navigation/DBIE capability audit, Page-34 official interbank series identity reconciliation, and Page-42 FX source boundary register. Existing conclusions were reused; no duplicate Library uploads, no repeat of BankWise raw parsing, no repeat of C283 calendar-gap audit, and no re-run of RBI Tables 218/222/223 scope audit.

## Official evidence established
1. RBI DBIE Brochure (May 2022) explicitly lists under Forex Market: daily exchange rate of INR against four major currencies, daily forward premia (inter-bank), and **daily interbank forex rates (USD vis-a-vis INR)**. It establishes official series existence, not the current table key or raw observations. https://dbieold.rbi.org.in/DBIE/doc/Brochure%20on%20DBIE%20-2022%20English.pdf
2. RBI's current Comprehensive Guide (April 2026; Publication page id=24094) identifies data.rbi.org.in as the DBIE platform, states extended historical time series are available through DBIE in reusable formats, and says the bulletin time series align with DBIE. This is platform/export-capability evidence, not an exact series mapping. https://www.rbi.org.in/SCRIPTs/PublicationsView.aspx?id=24094
3. The official DBIE portal resolves at https://data.rbi.org.in/DBIE/ but the web-readable response exposes no catalogue/table lines or downloadable payload in this audit.
4. The RBI Handbook's table 4 (Sale/Purchase of U.S. Dollar by RBI) is monthly and not the daily interbank USD/INR series; it is excluded as a substitute.
5. Existing Library Page-32/34 registers show the string `financial_markets.r691_daily_interbank_forex_rates_usd_vis_a_vis_inr` and claimed 2000-08-08–2026-06-30 coverage only on dbie.rbihub.in prototype. The prototype explicitly is not the live official portal; its table key, API, row counts and values are **not** accepted as RBI evidence.
6. No exact official RBI DBIE table ID, current official catalogue record, schema/column dictionary, downloadable CSV/XLS bytes, or official request/response was retrieved. No raw data or SHA-256 exists for this interbank series.

## Adjudication
- RBI DBIE daily interbank USD-vis-a-vis-INR series existence: PASS (official brochure).
- Official DBIE portal identity and general reusable time-series export capability: PASS.
- Exact official table key / table ID: UNKNOWN / NOT_VERIFIED.
- Schema and field definitions (including whether OHLC fields are official): UNKNOWN.
- Official raw payload, retrieval metadata, hash, row-level QA: NOT_CAPTURED / NOT_RUN.
- Prototype r691: DISCOVERY_ONLY; REJECTED_AS_PRIMARY_SOURCE.
- RBI/FBIL reference fixing: separate series; cannot substitute for interbank OHLC.
- Monthly RBI sale/purchase of USD: separate flow series; cannot substitute for daily interbank prices.

## Next action and stop condition
The next viable action is a bounded manual inspection by the user/authorized operator of the official DBIE portal's Financial Market > Forex Market catalogue, then attach/export the exact daily interbank USD-vis-a-vis-INR dataset directly from data.rbi.org.in. Capture the official table title/key, displayed frequency, period, column labels/definitions, export format, retrieval timestamp, original bytes and SHA-256. If the official portal does not expose the series/export to an ordinary user session, stop and retain UNKNOWN; do not call the mirror, infer its key, scrape hidden endpoints, bypass access controls, submit personal details, pay a fee, or contact RBI/FBIL without explicit approval. No browser automation/export was performed in this audit.
 
## GCR status and invariants
USD/INR interbank source remains BLOCKED / UNKNOWN; this does not clear the separate reference-rate continuity issue or FPI/DII blocker. Macro-Geo P0 last artifact-backed 6/8. Strict GCR hard gate BLOCKED; candidate_release_allowed=false; overall NOT_COMPUTABLE / NOT_CERTIFIED. No production changes. CORE-672 (56x12), Engines A-E, Production Selector, RANKING_SCORE, +1 PRESSURE_FADE and IPO-PLX V2.0 unchanged. UNKNOWN is neither PASS nor FAIL. Research spend ₹0; no paid services, subscriptions, external contact, synthetic rows, interpolation, forward-fill, or mirror data.

## Sources
- RBI DBIE Brochure 2022: https://dbieold.rbi.org.in/DBIE/doc/Brochure%20on%20DBIE%20-2022%20English.pdf
- RBI Comprehensive Guide for Current Statistics, April 2026: https://www.rbi.org.in/SCRIPTs/PublicationsView.aspx?id=24094
- Official DBIE portal: https://data.rbi.org.in/DBIE/
- Library Page-32, Page-33, Page-34 and Page-42 registers (read-only; existing Library files, not re-uploaded).
