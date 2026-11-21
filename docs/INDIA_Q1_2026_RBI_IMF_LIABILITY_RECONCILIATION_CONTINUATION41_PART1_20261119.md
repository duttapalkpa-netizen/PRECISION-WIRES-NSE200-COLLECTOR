# India national-source metadata and Q1-2026 liability discrepancy — Continuation 41 Part-1
Date: 2026-11-19
Scope: bounded official-source metadata check for India within the 2026-Q2 synchronous dual-leg candidate cohort. This does not claim that the Q1-2026 numeric residual is resolved.

## Progress log
- Reused the existing 63-country candidate cohort; India (IND) is present for 2026-Q2 with both A_NFA_T and L_NIL_T panel entries.
- Inspected the RBI's current official Comprehensive Guide for Current Statistics (publication page dated 2026-10-08; guide edition April 2026).
- RBI Table 42 is explicitly the standard BPM6 Balance of Payments presentation in US$ million, quarterly, sourced from RBI/DEPR, with data subject to revision. It presents financial-account assets/liabilities and credit/debit/net components.
- IMF SDDS India BOP metadata states that India's BOP classification follows BPM6 and describes the financial account as assets and liabilities for direct, portfolio, derivatives and other investment.
- RBI Table 44 is an IIP stock-position table, quarterly end-of-period, US$ million. It must not be substituted for Table 42 transaction-flow series when reconciling A_NFA_T/L_NIL_T flows.

## Evidence / sources
1. RBI Comprehensive Guide, publication page: https://rbi.org.in/Scripts/PublicationsView.aspx?id=24094
   - Published 2026-10-08; Table 42 is BPM6 BoP in US$ million, quarterly; revision policy says data are subject to revision.
   - Guide says provisional values may be revised as revisions are received.
   - Table 44 describes end-quarter IIP stocks, distinct from BoP flows.
2. IMF SDDS India BOP metadata: https://dsbb.imf.org/sdds/dqaf-base/country/IND/category/BOP00
   - States BPM6 classification and describes financial-account assets/liabilities.
3. IMF SDDS India IIP metadata: https://dsbb.imf.org/sdds/dqaf-base/country/IND/category/IIP00
   - Describes IIP as quarter-end stocks and BPM6 classification. Used only to prevent flow/stock conflation.

## Finding
- Official metadata confirms a suitable national BPM6 source family and confirms that RBI observations can be revised.
- This metadata does NOT establish that the particular RBI Q1-2026 portfolio-liability observation was revised, does not provide the exact old/new vintage pair, and does not explain the previously recorded residual of 1,512.508347 USD million between the RBI value (-12,121 USD million) and the IMF panel value (-13,633.508347 USD million).
- Therefore India Q1-2026 liability reconciliation remains REVIEW / UNRESOLVED. Do not apply a sign flip, scale conversion, stock/flow substitution, or revision adjustment based on general metadata.
- India Q2 panel membership remains a panel-presence PASS only; India national-source vintage/sign/scale validation is NOT_YET_PASS. The 63-country cohort remains NOT_AUTHORIZED for aggregation.

## Next exact action
Obtain the exact archived RBI Table 42 release/vintage rows for the Q1-2026 observation and the matching IMF panel series metadata/observation dimensions. Compare identical period, functional category, instrument coverage, unit, sign convention, and release vintage. If the historical RBI vintage cannot be recovered from public official material, retain REVIEW and document the limitation.

## Invariants
₹0; official/free sources only. No synthetic data, inferred alias, fabricated timestamp, guessed revision, or aggregate. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), and Engines A–E unchanged. UNKNOWN is never PASS.


## Continuation 187 addendum — RBI Q1-2026 published-value persistence (2026-11-21)
- Official RBI Table 43/42 release pages dated 22-Jun-2026, 22-Jul-2026 and 25-Aug-2026 were inspected. The Q1-2026 portfolio investment in India net is unchanged at -12,121 USDm in July/August; portfolio investment by India remains +74 USDm; total net remains -12,047 USDm. June Table 43 reports the Q1 values in ₹ crore (-110,826; +677; -110,149); no conversion was applied.
- This shows no change in the published RBI Q1 net values across the three inspected release pages. It does not establish a complete revision history or the IMF source vintage.
- Existing IMF Q1 L_NIL_T remains -13,633.508347 USDm vs RBI -12,121, residual -1,512.508347 USDm; liability and combined net remain REVIEW. Asset comparison remains PASS. Full India Q1 remains PARTIAL / NOT PASS.
- C187 report: `docs/GCR_INDIA_IND_Q1_2026_RBI_TABLE42_RELEASE_PERSISTENCE_AUDIT_CONTINUATION187_20261121.md`. No new IMF GET, no cohort rebuild, no inferred cause.
