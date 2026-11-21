# Tanzania TZA — Bank of Tanzania Q2-2026 portfolio source-boundary audit (Continuation 119)
Date: 2026-11-21 (Asia/Kolkata)

## Decision
The official Bank of Tanzania Statistical Bulletin for the quarter ending September 2026, Table 6.1 (Quarterly Balance of Payments), reports Q2 2026 portfolio investment as a single net line of **-USD 14.0 million**. The published table does not separately expose portfolio net acquisition of financial assets and net incurrence of liabilities for portfolio investment. Therefore this is a net-only national observation, not a dual-leg validation. TZA remains PARTIAL / NOT PASS; aggregate admission is NOT_AUTHORIZED.

## 1. Continuity preflight and duplicate rejection
- Re-fetched Master Continuity & Acceptance Ledger: `docs/PRECISION_WIRES_V11_3_CONTINUITY_ACCEPTANCE_LEDGER.md`, pre-task blob SHA `1fdd52f5f294e1cc7452b0c2cf6a2553a73f3bf8`. No Tanzania/TZA entry was present in the current ledger.
- Re-fetched GCR Master Priority Queue: `docs/GCR_MASTER_PRIORITY_QUEUE_AND_ZAF_Q2_2026_SOURCE_MAPPING_20261120.md`, pre-task blob SHA `d12ab5030ba2b2105d37e089777976b84fe810be`.
- Re-opened immutable cohort report `docs/GCR_2026Q2_SYNCHRONOUS_DUAL_LEG_COVERAGE_COHORT_CONTINUATION40_PART5_20261119.md`, blob SHA `1f767e22095865c8e5f87c2cfca55d9104b91e3e`. It lists TUR followed by TZA; TZA is therefore the next member after the prior TUR task in the fixed 63-country order.
- Repository searches for TZA Q2-2026 country validation / national dual-leg report returned no prior dedicated report. No IMF re-query, no cohort rebuild, and no prior PASS work repeated.

## 2. Official national source captured
- Issuer: Bank of Tanzania (BoT).
- Publication: Statistical Bulletin for the quarter ending September 2026, Vol. IV No. 3.
- Official PDF: https://www.bot.go.tz/Publications/Regular/Quarterly%20statistical%20Bulletin/sw/2026110312172422.pdf
- Table: 6.1, “Quarterly Balance of Payments”.
- Unit: Millions of USD.
- Table period headers include Dec-24, Mar-25, Jun-25, Sep-25, Dec-25, Mar-26, Jun-26 and Sep-26.
- The “Portfolio investment” row values include Mar-26 -2.1, Jun-26 -14.0, Sep-26 -1.0 (USDm). Q2 2026 is the Jun-26 column, **-14.0 USDm**.
- The same table separately disaggregates “Other investment” into assets and liabilities, but portfolio investment itself remains a single net line. Do not borrow the other-investment split for portfolio investment.
- The table is a later quarterly statistical bulletin and contains Q2 data; this source observation is not itself proof of exact IMF vintage alignment.

## 3. Dual-leg source boundary
- National portfolio net line: CAPTURED, -USD 14.0m for Q2 2026.
- National portfolio assets: NOT_SEPARATELY_PUBLISHED_IN_INSPECTED_TABLE.
- National portfolio liabilities: NOT_SEPARATELY_PUBLISHED_IN_INSPECTED_TABLE.
- Asset/liability signs and separate national transaction legs: NOT_ESTABLISHED.
- Exact archived IMF TZA row values were not extracted in this bounded task; cohort membership establishes the availability of both IMF panel entries, not national-source validation.
- National-to-IMF dual-leg comparison: NOT_DONE.
- Do not back-solve assets or liabilities from the net line, infer either leg from unrelated other-investment data, or use IIP stocks as BOP transactions.
- A historical IMF DQAF Tanzania assessment from 2004 notes older dissemination practices with single-line portfolio investment, but it is not used as proof of the current 2026 source boundary; the current 2026 BoT table itself is the evidence for this audit.

## 4. Gate matrix
| Check | Status |
|---|---|
| TZA membership in immutable 63-country Q2 cohort | PASS |
| No prior dedicated TZA Q2 dual-leg report found in repository search | PASS (scoped search) |
| Official BoT Q2-2026 BOP table located | PASS |
| Q2 2026 portfolio net | CAPTURED: -USD 14.0m |
| National portfolio asset leg | NOT_SEPARATELY_PUBLISHED_IN_INSPECTED_TABLE |
| National portfolio liability leg | NOT_SEPARATELY_PUBLISHED_IN_INSPECTED_TABLE |
| Raw PDF byte count / SHA-256 | NOT_CAPTURED |
| IMF exact-row numeric comparison | NOT_DONE |
| Full TZA dual-leg validation | PARTIAL / NOT PASS |
| Aggregate admission | NOT_AUTHORIZED |

## 5. Next action
- Do not derive or estimate separate portfolio legs from -USD 14.0m.
- If a BoT/NSDP downloadable detailed quarterly BOP dataset or official national supplementary table is discovered that explicitly separates portfolio assets and liabilities, inspect its exact period basis, unit, sign and vintage, and archive raw bytes/hash before parsing.
- Otherwise retain TZA as net-only / PARTIAL and advance to the next eligible fixed-cohort member, UKR, after checking the immutable roster and repository for prior UKR reports. No IMF re-query and no cohort rebuild.

## 6. Protected constraints
₹0 spend; official free sources only. No synthetic data, no inferred legs, no stock-as-flow, no generic FX, no sign flip, no net-to-leg back-solving, no production changes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS.

## Sources
- Bank of Tanzania Statistical Bulletin, quarter ending September 2026, Table 6.1: https://www.bot.go.tz/Publications/Regular/Quarterly%20statistical%20Bulletin/sw/2026110312172422.pdf
- Immutable 63-country cohort report: `docs/GCR_2026Q2_SYNCHRONOUS_DUAL_LEG_COVERAGE_COHORT_CONTINUATION40_PART5_20261119.md`


## Continuation 133 — Tanzania alternative-source boundary reconfirmed (2026-11-21)
- Re-fetched current Ledger/Queue/cohort and TZA Continuation 119. Fresh official BoT Quarterly Statistical Bulletin search result independently reconfirmed Table 6.1: Q2-2026 portfolio investment single net line -USD14.0m. Other-investment assets/liabilities are separately listed but are not portfolio legs.
- BoT official quarterly publication filter exposes a separate “Balance of Payments in USD” dataset only dated 25-Aug-2020; this is not Q2-2026. Other current BoT quarterly bulletin versions retain portfolio as net-only. Tanzania Investment Report is annual and not a quarterly BOP flow source. Do not back-solve or substitute unrelated instruments.
- TZA remains net-only / PARTIAL / NOT PASS; no national dual-leg values. Follow the existing TZA report's next item UKR. No IMF query/cohort rebuild; ₹0; UNKNOWN never PASS.
