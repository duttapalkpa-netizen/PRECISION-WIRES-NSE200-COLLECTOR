# Morocco MAR Q2-2026 — Portfolio Metadata and BOP Presentation Audit
Date: 2026-11-20
Status: PORTFOLIO CLASSIFICATION / CURRENT NET PRESENTATION REVIEW PASS; FX CONVERSION RULE NOT_ESTABLISHED; MAR PARTIAL / NOT PASS

## 1. Preflight
- Re-fetched Master Continuity Ledger, GCR Master Priority Queue, Morocco Continuation 92 transaction-FX scope report, and earlier Morocco dual-leg report.
- PASS work was not repeated. V11.4 implementation remains NOT_AUTHORIZED. No new IMF request or fixed-cohort rebuild.
- Selected the exact next task: inspect Office des Changes portfolio-investment metadata/technical documentation for transaction timing, measurement, source and currency conversion convention.

## 2. Official Office des Changes metadata reviewed
### A. Portfolio / financial account concept fiche
- Official metadata fiche for “Compte d’opérations financières”:
  https://services.oc.gov.ma/DataBase/MetaDonnees/Front/details/69
- It defines financial-account transactions as operations on financial assets/liabilities between residents and non-residents.
- It states BPM6 recommends net recording as net acquisition of assets / net incurrence of liabilities, but its “Application au niveau national” field says the national financial account is recorded on a gross credit/debit basis and four functional categories are separately presented.
- This metadata fiche was created 14-Oct-2013 and last updated 14-Oct-2013. Its age matters: it conflicts with the current 2024 annual report's explicit net flow presentation. Treat this old fiche as historical metadata, not proof that the Q2-2026 table is gross. A current versioned metadata fiche was not located.

### B. Portfolio-investment classification
- The metadata fiche’s related-term link for “Investissement de portefeuille” (link id 3) resolves toward details/87 but timed out during retrieval. Exact portfolio-specific fiche content, currency, unit, rate convention and vintage were therefore not captured.
- Current official Office des Changes 2024 annual BOP/IIP report:
  https://www.oc.gov.ma/sites/default/files/2025-09/Rapport%20Annuel%20de%20la%20Balance%20de%20Paiements%20et%20de%20la%20Position%20Ext%C3%A9rieure%20Globale%20-%20Ann%C3%A9e%202024_0.pdf
  * Financial-account methodology (p.59 / PDF lines 2948–2961) explicitly says financial transactions are recorded as net flows of assets and liabilities (“Acquisition nette d’avoirs” and “Accroissement net des engagements”), not debit/credit.
  * Portfolio investments are negotiable securities, mainly equity and debt securities (p.60 / lines 2960–2962).
  * The portfolio flow table reports assets +4,864 MDH, liabilities +3,886 MDH and balance +978 MDH for 2024 (p.36 / lines 1861–1867). The asset/liability table is presented as net flows.
- Thus the current 2024 annual report supports net presentation of portfolio flow legs. It does not state the currency conversion rule for foreign-currency portfolio transactions.

### C. Recording chronology fiche
- Official metadata “Chronologie d’enregistrement des flux”:
  https://services.oc.gov.ma/DataBase/MetaDonnees/Front/details/62
- BPM6 recommendation: record transactions when they occur / ownership changes, which need not coincide with settlement.
- National application: flows are recorded at settlement; when information is available, accrual basis is used.
- This supports the Continuation 92 distinction: settlement data are a principal source, but timing can be settlement-based or accrual-based when available. It does not establish the FX rate convention applied to every portfolio transaction.

### D. General BOP fiche
- Official metadata “Balance des paiements”:
  https://services.oc.gov.ma/DataBase/MetaDonnees/Front/details/56
- Defines BOP as transactions between residents and non-residents over a period and identifies BPM6 as the reference.
- Does not state the foreign-currency conversion convention.

## 3. Scope decision
- Current official 2024 BOP report confirms net assets/liabilities presentation for portfolio flows; old 2013 concept fiche records a historical gross credit/debit national application. The current report is the stronger current publication evidence, but do not silently overwrite the older fiche: preserve both and mark metadata-version conflict/age.
- The portfolio-specific metadata fiche could not be retrieved (link timeout). No evidence obtained for transaction currency, valuation currency, or a daily/monthly/quarterly conversion-rate rule.
- No MAD/USD numeric conversion performed. Do not use BAM revaluation reference rates, daily arithmetic means, quarter-end rates or third-party rates as substitutes.
- Existing Q2-2026 national/IMF positive asset and liability directions remain directionally consistent only; magnitude comparability NOT_DONE; same-vintage NOT_ESTABLISHED.

## 4. Acceptance table
| Gate | Status |
|---|---|
| Current portfolio classification (equity/debt securities) | PASS |
| Current 2024 report's net portfolio flow presentation | PASS |
| Historical 2013 gross/net metadata conflict identified | PASS — conflict/age documented |
| Portfolio-specific fiche details retrieved | NOT_RETRIEVED |
| Q2-2026 portfolio transaction currency/valuation currency | NOT_ESTABLISHED |
| Q2 portfolio-flow FX conversion convention | NOT_ESTABLISHED |
| Numeric MAD/USD conversion | NOT_DONE |
| Same-vintage bridge | NOT_ESTABLISHED |
| MAR complete national validation | PARTIAL / NOT PASS |
| Aggregate / production | NOT_AUTHORIZED |

## 5. Decision and next step
- Close the currently accessible public metadata route as NOT_ESTABLISHED for FX conversion; do not repeat the same timed-out link.
- Advance the fixed 63-country cohort to the next unfinished country rather than looping on Morocco. Keep MAR PARTIAL / NOT PASS and retain the unresolved metadata/version and FX-conversion blockers in the queue.
- If Office des Changes later publishes a current portfolio fiche or versioned technical note with an explicit transaction FX convention, revisit MAR using that evidence and the existing corrected IMF rows. No new IMF query required.
- No numeric conversion, no cohort rebuild, no production change, ₹0.

## 6. Official source register
- Office des Changes metadata — Compte d’opérations financières: https://services.oc.gov.ma/DataBase/MetaDonnees/Front/details/69
- Office des Changes metadata — Chronologie d’enregistrement des flux: https://services.oc.gov.ma/DataBase/MetaDonnees/Front/details/62
- Office des Changes metadata — Balance des paiements: https://services.oc.gov.ma/DataBase/MetaDonnees/Front/details/56
- Office des Changes Annual BOP/IIP Report 2024: https://www.oc.gov.ma/sites/default/files/2025-09/Rapport%20Annuel%20de%20la%20Balance%20de%20Paiements%20et%20de%20la%20Position%20Ext%C3%A9rieure%20Globale%20-%20Ann%C3%A9e%202024_0.pdf

## 7. Protected invariants
Fixed 63-country Q2-2026 IMF cohort unchanged. No new IMF request, no production change, no synthetic data, fabricated timestamps, unsupported FX, forward-fill, guessed mapping or paid API. ₹0. UNKNOWN is never PASS.
