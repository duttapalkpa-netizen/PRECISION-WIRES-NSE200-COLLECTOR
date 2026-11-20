# GCR BSE Sector TRI Source Rights & Admission Gate — 20 November 2026
Research continuation 41, Part 4
Scope: source-rights and access audit for BSE/BSE Indices historical sector Total Return Index (TRI) data, requested as the next GCR sector-transmission input. This is a read-only public-policy review; no data download, scraping, database build, or production integration.

## Why this task was selected (continuity check)
Before starting, the GitHub continuity ledger and prior reports were searched:
- Continuation 74 explicitly identifies official BSE sector TRI historical data + exact index identifiers/currency/dates/raw hashes as the next highest-value task before any sector-flow join.
- Continuation 67 requires total-return (not price-only) indices, matched close/timezone, publication timestamp and vintage; it says not to infer sector mapping.
- No prior evidence was found that BSE sector TRI history had been acquired or admitted. Therefore this is a new gate, not a repeat of IIP/CPI or earlier CDSL/NSDL capture.
- Earlier taxonomy checkpoint has BSE classification methodology but issuer-level mapping and historical classification versions remain incomplete.

## Primary official evidence
1. BSE Indices Terms of Use: https://www.bseindices.com/terms-of-use
   - BISPL data may be used solely for internal business purposes unless otherwise permitted.
   - Users must not use BISPL data to create/develop indices, a classification system or historical databases.
   - Users must not create derived data based on BISPL data except with BISPL express written consent.
   - Disclosure, duplication, display, redistribution, resale or conveyance is restricted except as expressly allowed for authorized service end users.
2. BSE Indices Legal Disclaimer: https://www.bseindices.com/legal-disclaimer
   - Index content may not be modified, reverse-engineered, reproduced, distributed or stored in a database/retrieval system without prior written permission.
3. BSE Thematic Indices Methodology: https://www.bseindices.com/Downloads/BSE_Thematic_Indices_Methodology.pdf
   - Methodology distinguishes Price Return (PR) and Gross Total Return (TR); regular cash dividends are reinvested in TR versions at ex-date close.
   - Daily constituent and index-level data are available via subscription.
   - Example TR tickers include BSEMFGT, BSEINFRT, BSEFXBT and BSEHOUT. This confirms that index-specific TR variants exist, not that the full historical data are freely reusable.
4. BSE Index Details interface: https://www.bseindices.com/indices-details/code/1
   - Public page exposes performance date-range controls and factsheet/constituent/benchmark-code links, but a public UI does not override data-use restrictions.
5. BSE Sector Leaders paper (Oct 2025): https://www.bseindices.com/Downloads/BSE_India_Sector_Leader_Paper_Oct_2025.pdf
   - Publishes selected TRI performance summaries as at 30-Sep-2025. Summary statistics are not a complete daily sector TRI history and cannot replace the requested matched daily panel.

## Decision
**BSE sector TRI historical data is NOT ADMITTED for the GCR research database or derived sector-transmission panel under the currently inspected public terms.**
The explicit prohibition on building historical databases and derived data without express written consent is directly material to this project. The public methodology and factsheets do not grant a research exception. The user’s no-paid-source constraint does not create a reuse licence.

## Acceptance matrix
| Gate | Status | Evidence / reason |
|---|---|---|
| Official BSE index provider identified | PASS | BISPL / BSE Indices |
| PR vs Gross TR methodology distinction | PASS | Official methodology |
| Sector TR index examples/tickers identified | PASS (examples only) | BSEMFGT, BSEINFRT, BSEFXBT, BSEHOUT |
| Daily historical index data public/free | NOT ESTABLISHED | Methodology says daily data via subscription |
| Historical database creation permitted | BLOCKED | Terms prohibit absent permission |
| Derived data / sector-return panel permitted | BLOCKED | Express written consent required |
| Redistribution/display permitted | BLOCKED / RESTRICTED | Terms and disclaimer restrictions |
| Full daily historical sector TRI acquired | NOT_DONE | No download attempted |
| BSE sector classification ↔ TRI exact mapping | NOT_DONE | Requires exact index identifiers/official benchmark codes |
| GCR sector transmission admission | BLOCKED | Rights + history + mapping not closed |

## Practical next path (no paid data)
1. Do not fetch/ingest BSE index levels into the GCR historical database unless the provider grants express written permission covering research database creation and derived calculations.
2. Do not rely on public factsheets/marketing PDFs as a licence for daily data extraction or long-term storage.
3. Investigate an alternate official source whose own terms explicitly permit the intended use (e.g. NSE Indices, if its applicable licence/terms support internal research and derived analytics). This is a source-rights discovery task only; do not presume permission.
4. If no free official source with adequate rights exists, mark the BSE sector TRI factor UNKNOWN and exclude it from GCR score/sector transmission. Do not substitute price-return indices for TRI or proxy one sector with another.
5. If the user obtains written provider permission independently, archive the permission scope and validity period; only then define exact index universe, PR/TR type, ticker, currency, launch/first-value/base dates, back-tested/live distinction, daily history, timestamps, revision vintage, raw hashes and methodology versions.

## Effect on GCR and PRECISION-WIRES
- CDSL fortnightly sector FPI data and BSE sector TRI cannot be joined into a predictive sector-flow/return panel until the TRI source rights, exact series history and taxonomy mapping are all accepted.
- No sector transmission, relative-attraction score, macro weight or stock-level beneficiary inference is authorized from this audit.
- No stock pick is generated from this work.
- No NSE/BSE endpoint scraping, access-control bypass, paid API, or synthetic data was used.

## Prior experience preserved
- Do not repeat already completed IIP/CPI release and source-permission audits.
- Do not repeat CDSL/NSDL seven-page raw captures already archived; the unresolved NSDL Archive postback and CDSL raw table/sector file parsing are separate tasks.
- Do not repeat Brazil BCB SGS 22905/22906/22925/22940 raw capture; run 44538278638 and artifact 14535963861 already PASS with four hashes.
- Brazil PA/Dataflow mismatch and owner-side PA changelog remain separate BLOCKED external dependency.
- GCR must use total-return rather than price-return series, aligned by close/timezone and vintage, with no look-ahead.
- Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS.

## Audit conclusion
**BSE sector TRI: RIGHTS BLOCKED / NOT ADMITTED.** This is a valid research result: it prevents an unlicensed historical database and a false claim of completed sector-transmission validation. The next permissible research task is to rights-screen the NSE Indices historical TRI route or another official source before any acquisition.
