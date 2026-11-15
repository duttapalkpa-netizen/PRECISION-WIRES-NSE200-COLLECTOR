# Macro-Geo P0: Official-source recovery acceptance contract — 2026-11-12

## Immutable baseline
- Latest successful fresh snapshot workflow: Run 43259234768, commit cf7cfbfcc459f0195a727798af00712babfdffe2, artifact 13963926359, artifact digest sha256:bcc2cfafd25488160bfca68300de07ef06da9a94291083ec70e50445b48b1e02.
- Rebuilt equity panel: 200 verified sessions, panel sha256:91b320094baff93be9982564e5dc175203bc45cb7b03d59afc470bc049900122.
- Same-snapshot P0 status: 4/8 source groups available by file/schema checks, not 8/8; factor groups 0 fully available, 7 partial, 28 not connected. Do not overwrite older audits with these counts without identifying their distinct snapshot.
- No production selector, RANKING_SCORE, +1 PRESSURE_FADE, 672 diagnostic, or PR merge changes.

## Source recovery priority and non-equivalence
1. USD/INR: RBI DBIE official daily interbank USD/INR table: https://dbie.rbihub.in/tables?table=financial_markets.r691_daily_interbank_forex_rates_usd_vis_a_vis_inr . Archive: https://rbi.org.in/scripts/ReferenceRateArchive.aspx . RBI reference rates since 2018-07-10 are computed by FBIL; do not silently equate interbank close with FBIL reference fixing. Verify publication timestamp and source availability as of each signal timestamp; an undated current CSV is NOT point-in-time verified.
2. Crude oil: PPAC Indian Basket historical report: https://ppac.gov.in/index.php/prices/international-prices-of-crude-oil . Indian Basket (Brent Dated + Oman/Dubai blend) is NOT Brent front-month. Do not map it into BRENT CRUDE FRONT MONTH without an explicit approved contract change. Monthly averages are NOT daily observations; never forward-fill them as if observed daily.
3. FPI/DII: existing fresh run returned only 2 records on 2026-11-12 (1 FII/FPI, 1 DII); this is insufficient historical coverage. Collect only authentic dated historical rows with source URLs, retrieved-at UTC and original files. Do not treat one date as full 200-session coverage.
4. Corporate events: official NSE corporate announcements API timed out in the fresh run. Preserve as NOT_CONNECTED until official timestamped disclosures can be downloaded, mapped by security and date, and verified against historical session eligibility.

## Hard gate acceptance criteria (all mandatory)
- Verify raw official source bytes, SHA-256, URL, retrieval timestamp, license/access boundary, schema, units and source revision.
- Report date range, expected/observed session intersections, unique date counts, missing date counts, and publication-to-market timestamp eligibility separately for every series.
- Join by actual NSE trading calendar. Keep holidays and missing values UNKNOWN. No synthetic values, synthetic timestamps, future revisions, or silent proxy substitution.
- Use exact equity snapshot ID ee037b46aa2e8e7bce7df51919aada51418fd03787a1ed740a103f4b47804305, with immutable source manifest and output hashes. Store independent status per source and 35-factor group.
- A successful collector workflow only establishes execution success, not 8/8 P0 coverage, full factor availability, matured event-study acceptance, historical-regime completeness, or Hard Gate clearance.
- Research constraints: ₹0 spend; free official sources only for promoted macro factors; no paid APIs, no PR merge without approval. Secondary media events are never promoted to official-source macro observations.

## Reproducible next actions
A. Recover RBI daily FX source file and validate dates/units/close-vs-fixing metadata.
B. Recover PPAC historical file and classify daily-vs-monthly Indian Basket separately; locate an *official, freely usable, actual* Brent front-month daily series before asserting Brent completion.
C. Recover historical FPI/DII and corporate disclosures from official sources with source-specific parsers, bounded retries and failure-as-UNKNOWN.
D. Run same-snapshot reconciliation and update Master Gap Matrix only from emitted hashed evidence.

## Status at this commit
SOURCE_CONTRACT_DOCUMENTED; INGESTION_NOT_YET_VERIFIED; HARD_GATE_BLOCKED. No backtest or production ranking promotion authorized.
