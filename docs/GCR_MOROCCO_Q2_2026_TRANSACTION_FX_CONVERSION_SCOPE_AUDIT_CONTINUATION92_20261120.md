# Morocco Q2-2026 — Transaction FX Conversion Scope Audit
Date: 2026-11-20
Status: OFFICIAL BPM6 SOURCE-SCOPE REVIEW PASS; PORTFOLIO-FLOW MAD/USD CONVERSION RULE NOT_ESTABLISHED; MAR PARTIAL / NOT PASS

## 1. Preflight
- Re-fetched Master Continuity Ledger, GCR Master Priority Queue, Continuation 91 FX/BPM6 report, Continuation 87/88 MAR dual-leg report, and Continuation 90 V11.4 independent specification review.
- PASS work was not repeated. V11.4 implementation remains NOT_AUTHORIZED; no V2 implementation was attempted.
- Selected the next unresolved exact item from Continuation 91: determine whether Office des Changes' official transaction settlement-rate methodology applies to the Q2 portfolio-investment BOP flow legs.

## 2. New official evidence
### A. Office des Changes — Balance des règlements methodology
- Official methodology note PDF: https://www.oc.gov.ma/sites/default/files/documents/methodologie/oc-methodologie-br.pdf
- It says bank reports for each actual payment record payment type, settlement currency, foreign-currency amount, and MAD countervalue based on the rate applied on the execution date (methodology PDF lines 8–14).
- This methodology is for the *balance of settlements* (balance des règlements), not by itself the full *balance of payments* (balance des paiements). The note expressly distinguishes them: BOP records all resident/nonresident transactions whether or not settled or when settlement is deferred; settlement balance records only actual payments in the period (lines 67–74). It lists further differences and excluded non-cash/non-settled transactions (lines 91–104).
- Therefore this daily execution-rate rule cannot be transferred wholesale to Q2 portfolio BOP flows. It is relevant evidence about source bank reports for settled operations, but not an authoritative universal BOP portfolio-flow FX conversion rule.

### B. Current Office des Changes BOP methodology (2022 annual report, based on MBP6)
- Official annual report: https://www.finances.gov.ma/Publication/oc/2023/RapportAnnuelBPPEG2022_0.pdf
- The report's methodology says financial-account transactions are recorded as net flows of assets and liabilities, not debit/credit, and bank settlement data are the principal source for financial-account statistics (PDF pp.60–61 / extracted lines 2420–2428).
- It does not specify in the inspected methodology section whether foreign-currency portfolio transactions are converted using transaction-date applied rates, BAM daily reference rates, monthly/quarterly averages, or another method.
- The report also documents other financial-account components using surveys/statistical declarations and adjustments, so the fact that bank settlement data are principal does not prove every portfolio transaction is settled or converted using a single daily rate.

### C. Office des Changes metadata: settlement vs transaction
- Official metadata page: https://services.oc.gov.ma/DataBase/MetaDonnees/Front/details/107
- It explicitly distinguishes transaction date from settlement date under BPM6. Nationally, goods are recorded irrespective of settlement timing; for other items, recording is based mainly on settlement data.
- This supports the need for a portfolio-specific conversion method and warns against equating the settlement-rate methodology with all financial-account transactions.

## 3. Scope decision
- Do not apply the old Balance des règlements execution-date exchange-rate rule to the whole Q2 portfolio investment balance-of-payments series.
- Do not substitute BAM daily revaluation reference rate, simple average of daily rates, quarter-end rate, or third-party rate without explicit Office des Changes portfolio-flow conversion authority.
- No numeric conversion is computed; no raw BAM Q2 daily observations are needed until the exact applicable rule is established.
- The existing positive national legs (+4,848 and +36,933 million MAD) and corrected IMF MAR legs (+523,948,820.8007525 and +3,991,543,275.295832 USD) remain directionally consistent under BPM6 labels only. Magnitude comparability remains NOT_DONE.
- Same-vintage remains NOT_ESTABLISHED. IMF ACTION=R alone does not give observation-specific revision timestamp.

## 4. Gate table
| Gate | Status |
|---|---|
| BOP vs settlement-balance methodology distinguished | PASS |
| Official execution-date rate for actual settlement reports identified | PASS |
| Execution-date rule proven applicable to all portfolio BOP flows | NOT_ESTABLISHED |
| Current BPM6 portfolio-flow MAD/USD conversion convention | NOT_ESTABLISHED |
| BAM Q2 daily series required/authorized for this conversion | NOT_ESTABLISHED |
| Numeric separate-leg conversion | NOT_DONE |
| Same-vintage bridge | NOT_ESTABLISHED |
| MAR full validation | PARTIAL / NOT PASS |
| Aggregate and production | NOT_AUTHORIZED |

## 5. Next exact action
- Do not continue searching BAM daily rates until Office des Changes confirms the conversion method for portfolio-investment BOP transactions specifically.
- Next evidence route: inspect the detailed metadata/technical fiche for “Investissements de portefeuille” and the quarterly balance-of-payments source notes; seek an explicit valuation currency and conversion-rate convention. If the public fiche lacks the method, record NOT_ESTABLISHED and advance to the next fixed-cohort member.
- No new IMF query, no fixed cohort rebuild, no unsupported FX conversion, no netting, no production changes.

## 6. Official source register and citations
- Office des Changes, Balance des règlements methodology PDF: https://www.oc.gov.ma/sites/default/files/documents/methodologie/oc-methodologie-br.pdf
- Office des Changes, 2022 Annual BOP/IIP report (BPM6 methodology, financial account pp.60–61): https://www.finances.gov.ma/Publication/oc/2023/RapportAnnuelBPPEG2022_0.pdf
- Office des Changes metadata — Règlements avec l’étranger: https://services.oc.gov.ma/DataBase/MetaDonnees/Front/details/107
- Prior official BAM daily reference methodology remains documented in Continuation 91; it is not approved as the BOP portfolio flow conversion method.

## 7. Protected invariants
Fixed 63-country IMF Q2-2026 cohort unchanged. No new IMF request, no production change, no synthetic data, fabricated timestamps, unsupported FX, forward-fill, guessed mapping or paid API. ₹0. UNKNOWN is never PASS.


## Continuation 92 — Final verification marker
- BOP-versus-settlement methodology distinction reviewed from the official Office des Changes source. Execution-date settlement conversion is not established as the universal Q2 portfolio BOP conversion rule. Numeric conversion remains NOT_DONE; MAR PARTIAL / NOT PASS; aggregate/production NOT_AUTHORIZED.
