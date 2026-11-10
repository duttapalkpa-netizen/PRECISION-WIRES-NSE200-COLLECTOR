# Global Capital Rotation Overlay — official-source access contract
Date: 2026-11-11
Scope: research-only source-access contract; no observations ingested and no production integration.

## Decision
This audit resolves source identity/frequency semantics for the next Global Capital Rotation ingestion slice. It does not claim that capital rotation itself has been measured. Positions, transactions/flows, FX rates, and benchmark returns remain distinct data types.

## Verified public official sources

| Signal family | Official source / identifier | Frequency / coverage | Permitted interpretation | Prohibited inference |
|---|---|---|---|---|
| Cross-border portfolio positions | IMF Portfolio Investment Positions by Counterpart Economy (PIP; formerly CPIS), dataset IMF.STA:PIP | Annual and semi-annual; equity/fund shares, long-term debt, short-term debt | Bilateral portfolio holdings/positions by counterpart economy; structural cross-border exposure | Not daily/weekly flow; valuation changes and exchange-rate effects can change positions |
| India PIP reporting | RBI PIP FAQ | India reporting half-yearly, end-March/end-September reference positions; RBI submits consolidated aggregates to IMF | India reporting cadence and confidentiality boundary | No entity-level holdings; no high-frequency flow proxy |
| US broad dollar index | Federal Reserve H.10 series H10/H10/JRXWTFB_N.B | Daily; available from 2006-01-02 to latest published observation in inspected package | Nominal Broad Dollar Index proxy, with explicit Fed definition | Do not label as ICE DXY; methodology/basket differs |
| US advanced-economy dollar index | Federal Reserve H.10 series H10/H10/JRXWTFN_N.B | Daily; available from 2006-01-02 | Nominal Advanced Foreign Economies Dollar Index | Not a broad all-country dollar index |
| US EM dollar index | Federal Reserve H.10 series H10/H10/JRXWTFO_N.B | Daily; available from 2006-01-02 | Nominal Emerging Market Economies Dollar Index | Not direct capital flow or an India-specific signal |
| Bilateral FX | BIS Bilateral Exchange Rates (XRU topic) | Daily for ~80 economies; monthly/quarterly/annual for broader coverage | USD bilateral exchange-rate history; source/methodology documented by BIS | Do not mix observation time conventions without recording them |
| US international holdings | Federal Reserve Enhanced Financial Accounts, International Portfolio Investment Holdings of Long-term Securities by Country (FRBCNA71) | Monthly country-level holdings | US-reported holdings of long-term securities by country | Holdings are not monthly net transactions; not complete global fund flows |
| India external position context | RBI International Investment Position | Quarterly reference dates | India external asset/liability and portfolio-position context | Not daily flow or same-day trading signal |

## Evidence and source URLs
- IMF PIP dataset: https://data.imf.org/datasets/IMF.STA%3APIP
- IMF PIP dataset page and frequency: https://data.imf.org/en/Datasets/PIP
- RBI PIP FAQ (updated 2026-06-01): https://rbi.org.in/scripts/FAQDisplay.aspx?Id=159
- Federal Reserve H.10 download program: https://www.federalreserve.gov/datadownload/Choose.aspx?rel=H10
- Federal Reserve H.10 package review inspected the following identifiers and availability:
  - H10/H10/JRXWTFB_N.B — Nominal Broad Dollar Index
  - H10/H10/JRXWTFN_N.B — Nominal Advanced Foreign Economies Dollar Index
  - H10/H10/JRXWTFO_N.B — Nominal Emerging Market Economies Dollar Index
  - Inspected availability: 2006-01-02 through 2026-11-06
- BIS bilateral exchange rates: https://data.bis.org/topics/XRU
- Federal Reserve country holdings dataset: https://catalog.data.gov/dataset/international-portfolio-investment-holdings-of-long-term-securities-by-country
- RBI IIP archive: https://www.rbi.org.in/scripts/IIP.aspx

## Ingestion contract (must be applied before any source is admitted)
1. Preserve raw source file/API response unchanged; calculate SHA-256 before transformation.
2. Record exact URL/endpoint, query parameters (redacting credentials), UTC retrieval timestamp, source publication/vintage timestamp, reference period, file size, media type, and source series identifier.
3. Store source type explicitly as POSITION, TRANSACTION/FLOW, FX_RATE, PRICE_INDEX, or TOTAL_RETURN_INDEX.
4. Never relabel positions as flows. For position changes, decompose/label valuation and FX effects only if the source provides a defensible decomposition; otherwise keep the cause UNKNOWN.
5. Keep source frequency and observation calendars explicit. Do not forward-fill or fabricate daily values from semi-annual/monthly observations.
6. Keep Federal Reserve Broad Dollar Index separate from ICE DXY. Do not substitute one under the other's name.
7. Keep provisional/revised vintages immutable and append-only; do not overwrite prior releases.
8. Missing, stale, inaccessible, or schema-unverified observations remain UNKNOWN/BLOCKED, never PASS by assumption.

## Acceptance gates
- Source identity/frequency semantics: PASS for the sources and series explicitly listed above.
- Exact raw download and ingestion with SHA-256: NOT DONE.
- Data schema/coverage/vintage QA: NOT DONE.
- Global flow/position bridge and valuation-effect treatment: NOT DONE.
- Daily FX and benchmark return panel: NOT DONE.
- India sector attraction bridge: NOT DONE.
- Historical event study/backtest: NOT DONE.
- Overlay completion: NOT COMPLETE.
- Production integration: PROHIBITED without separate explicit approval.

## Project invariants
No changes to Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56 x 12), Engines A-E, or Hard Gate. No composite stock score, stock ranking, buy/sell instruction, or automatic trading. ₹0 spend; free public official sources only; no synthetic observations; no paid API; no external contact.

## Research interpretation note
IMF PIP is semi-annual/annual positions data. The Federal Reserve H.10 dollar indices are FX indices, not flows. BIS bilateral exchange rates are rates, not flows. FRB country-level long-term holdings are positions. These can support a macro/structural context layer, but none independently establishes contemporaneous capital rotation into India. Any flow claim requires transaction/flow evidence at a matching frequency and coverage.
