# Global Capital Rotation — IMF BOP Aggregate Source Checkpoint
Date: 2026-11-17 (Asia/Kolkata)
Branch: research/global-capital-rotation-overlay-v1
Scope: official source-discovery and methodology assessment; no observation extraction.

## New official source candidate
IMF dataset: Balance of Payments and International Investment Position Statistics (BOP/IIP), World and Country Group Aggregates, historically BOPSY.
Official dataset URL: https://data.imf.org/en/datasets/IMF.STA%3ABOP_AGG
Official explanatory notes: https://data.imf.org/-/media/Explanatory-Notes-November-2025-BOPSY.pdf
The IMF describes this as an annual publication released each November, based on BPM6. The IMF page exposes API, View Data and Download controls.

## Key methodological boundary
The IMF notes that country-level data are actual reports (or national summary data page data), but World and country-group aggregates other than Euro Area combine reported country data with estimates for nonreporting economies, using WEO and other sources. Therefore:
- This is a legitimate official aggregate candidate for a low-frequency global/region portfolio-transaction context.
- It is NOT a pure sum of observed country reports.
- Any use must retain IMF's estimated/nonreporter component as part of the published aggregate methodology and must not relabel it as fully observed flows.
- The BOP_AGG dataset includes both BOP transactions and IIP positions; select only the financial-account portfolio-investment transaction component. Never use IIP positions as flow.
- Annual frequency is unsuitable as a daily trading trigger and must be labelled low-frequency strategic context only.
- The dataset's EMDE grouping is IMF's own grouping and differs from MSCI EM membership; never call it MSCI EM or silently merge memberships.

## Reporting and coverage facts from the November 2025 explanatory notes
- IMF describes World and Country Group Aggregates as annual, November release, BPM6-based.
- The publication includes World and Regional Tables, USD and Percent-of-GDP presentations, and country-group charts.
- IMF states that aggregate estimates fill nonreporting-economy gaps, including for financial-account transactions.
- The country overview shows reporting-year variation; India has BOP and IIP last reported period 2024 in the November 2025 notes. Country coverage is not uniform.
- The Emerging and Developing Economies group is subdivided into Emerging and Developing Asia, Emerging and Developing Europe, Middle East and Central Asia, and Sub-Saharan Africa.

## Current decision
- Official BOP_AGG dataset route: SOURCE DISCOVERY PASS.
- Published aggregate methodology understood at a high level: PASS.
- Exact portfolio-investment transaction table/series mapping: UNKNOWN / NOT_DONE.
- Actual downloaded XLSX/CSV/API payload, raw byte count, retrieval timestamp and SHA-256: NOT_DONE.
- Series key, units, currency, sign, component, country group and release vintage QA: NOT_DONE.
- This source is a candidate to provide official annual EMDE/World aggregate context; it does not yet populate em_portfolio_flow_usd_bn.
- IMF BOP country-level quarterly/annual portfolio transaction panel remains NOT_DONE.
- No full overlay gate or percentage is advanced by this discovery checkpoint.

## Next bounded extraction steps
1. Use the official BOP_AGG View Data/Download controls to obtain the November 2025 workbook or API export without guessing endpoints.
2. Archive raw payload with final URL, retrieved_at UTC, byte count, HTTP metadata if available and SHA-256.
3. Identify the exact Financial Account > Portfolio Investment > Assets/Liabilities transaction series and any equity/debt splits from the workbook's own labels/metadata.
4. Reconcile one selected value to the IMF displayed table; preserve USD units, signs, frequency, release vintage and missingness.
5. Compare official EMDE group aggregate with the separately reported-country panel only if both can be reconstructed; never subtract/replace estimated portions without explicit method.
6. If 2026 annual release is not yet published/accessible as of this audit timestamp, retain latest available vintage and state the period explicitly; do not assume 2026 annual observation exists.

## Protected invariants
No production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56x12), Engines A-E or Hard Gate change. Research-only; no stock score, ranking, buy/sell instruction, automatic trigger, PR merge or production integration. ₹0 spend, official/free sources only. No synthetic observations or fabricated timestamps/hashes; missing/stale remains UNKNOWN.

## Official references
- IMF BOP: https://data.imf.org/en/datasets/IMF.STA%3ABOP
- IMF BOP/IIP World and Country Group Aggregates: https://data.imf.org/en/datasets/IMF.STA%3ABOP_AGG
- IMF BOPSY Explanatory Notes, November 2025: https://data.imf.org/-/media/Explanatory-Notes-November-2025-BOPSY.pdf
