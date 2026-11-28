# GCR Continuation 290 — RBI historical reference-rate cross-check for DBIE interbank TXT (28-Nov-2026)

## Scope
Read-only, bounded cross-check of the RBI reference-rate field in the newly acquired 6,330-row TXT, focused on the 21-Mar-2016 anomalous Open value. No production ingestion, normalization, automatic repair, or source substitution.

## Preflight / evidence reused
- Reused the existing C289 raw TXT and immutable SHA-256: `ac8cbec57bc8c87b2c4cacd5a02f68620e44672f488bd711fd0f81565ca6bf1c`.
- Reused C289's structural QA; no repeated acquisition or parsing.
- Official RBI publication located: **Table 226: Daily Exchange Rate of the Indian Rupee**, publication dated 16-Sep-2016. The table note states the data are based on RBI Reference Rate. Source: https://www.rbi.org.in/scripts/PublicationsView.aspx?id=17359
- Current RBI publication Table 223 is also titled Daily Exchange Rate of the Indian Rupee, but is a reference-rate series, not interbank OHLC. Source: https://www.rbi.org.in/Scripts/PublicationsView.aspx?id=24048

## Exact row reconciliation
The following three adjacent RBI publication observations match the TXT's final RBI Reference Rate column exactly:

| Date | TXT RBI Reference Rate | Official RBI Table 226 | Result |
|---|---:|---:|---|
| 18-Mar-2016 | 66.6088 | 66.6088 | PASS |
| 21-Mar-2016 | 66.5040 | 66.5040 | PASS |
| 22-Mar-2016 | 66.5411 | 66.5411 | PASS |

Official Table 226 rows are visible in its dated table; the table explicitly says the data are based on RBI Reference Rate. This provides direct official corroboration of the TXT reference-rate field for these three dates.

## What this proves — and does not prove
- **PASS (narrow):** the TXT's RBI Reference Rate field is correctly aligned with the official RBI daily reference-rate series for these three dates.
- **The 21-Mar-2016 Open anomaly remains unresolved:** the TXT still records Open = `3,355.7300`, while the official RBI reference rate for that date is `66.5040`. The official Table 226 is a reference-rate table; it does not publish interbank Open/High/Low/Close. It therefore cannot be used to replace or certify the Open value.
- **High/Low inversion remains BLOCKED:** Table 226 contains no interbank OHLC fields and cannot validate the TXT's High/Low column labels. No automatic swap is authorized.
- No source row was changed, dropped, imputed, or forward-filled. Raw bytes remain immutable.
- This cross-check does not establish current coverage after 31-Jul-2026, completeness of the 6,330-row historical extract, or permission to ingest the OHLC fields.

## Updated acceptance state
| Component | State |
|---|---|
| RBI TXT raw bytes / hash | PASS (C289) |
| Date / schema / duplicate structural checks | PASS (C289) |
| RBI reference-rate field, 18–22 Mar 2016 sample | PASS — 3/3 exact |
| 21-Mar-2016 interbank Open value | BLOCKED / NOT CORRECTED |
| Interbank High/Low semantics | BLOCKED |
| 01-Aug-2026 onward current segment | NOT CAPTURED |
| Clean USD/INR interbank OHLC ingestion | NOT ACCEPTED |
| Strict GCR hard gate | BLOCKED; candidate_release_allowed=false; overall NOT_COMPUTABLE / NOT_CERTIFIED |

## Next action — only unresolved work
1. Obtain an official RBI DBIE report definition or official raw export that actually exposes the interbank OHLC fields; reference-rate tables are not substitutes.
2. Independently adjudicate the High/Low field semantics and the 21-Mar-2016 Open misprint from official OHLC source evidence. Until then, retain the original tokens and do not normalize.
3. Acquire the official current segment from 01-Aug-2026 onward. Do not forward-fill missing dates.
4. Keep CCIL FX-Clear transaction tape, RBI interbank OHLC, and RBI/FBIL reference fixing as three separate datasets.

## Invariants
Research spend ₹0; official/free sources only; no paid API/licence/subscription, external contact, synthetic values, interpolation, or silent repair. CORE-672 (56×12), Engines A–E, Production Selector, RANKING_SCORE, +1 PRESSURE_FADE and IPO-PLX V2.0 remain unchanged. UNKNOWN is neither PASS nor FAIL.
