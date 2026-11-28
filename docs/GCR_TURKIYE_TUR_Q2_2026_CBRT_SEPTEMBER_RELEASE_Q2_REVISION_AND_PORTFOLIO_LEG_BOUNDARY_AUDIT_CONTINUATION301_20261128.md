# GCR Continuation 301 — Türkiye (TUR) Q2-2026 CBRT September release / revision and portfolio-leg boundary audit
Date: 2026-11-28 (Asia/Kolkata)
Task ID: GCR-C301-TUR-CBRT-SEP26-Q2-REVISION-01
Scope: Bounded review of the latest official CBRT September-2026 BOP release and official data/revision-policy access routes, reusing prior Q2 work without repeating closed numeric or IMF tasks.

## 1. Continuity and duplicate-prevention preflight
- Re-fetched current Master Continuity Ledger, GCR Master Priority Queue, Historical Task Registry and immutable 63-country Q2-2026 matrix.
- Re-read Library Mother File Continuation 1–53 and the TUR historical task notes.
- TUR matrix baseline: DATA_CAPTURED; asset PASS; liability REVIEW; vintage PENDING; FULL_PASS=NO; aggregate NOT_AUTHORIZED. The existing liability residual of USD87m and previous source limitations were carried forward; no numeric re-run.
- No repeat IMF extraction, previous Q2 PDF arithmetic, or old source retrieval attempts. The next eligible trigger was the distinct official CBRT September-2026 BOP publication and its data/revision-policy links.

## 2. New official CBRT September-2026 publication
- Official publication: *Balance of Payments Developments, September 2026*, CBRT, September 2026.
- PDF: https://www.tcmb.gov.tr/wps/wcm/connect/4329826e-067d-44b6-8748-620900d91741/BalanceofPayments_September2026.pdf?MOD=AJPERES
- The release includes Table 2 financial-account data in USD million, with portfolio assets and liabilities separately reported for September 2026, January–September 2026 cumulative totals and 12-month totals.
- Table 2 values (USD million):
  - Portfolio assets: September 2026 +1,972; Jan–Sep 2026 +19,397; 12-month September +24,082.
  - Portfolio liabilities: September 2026 -5,761; Jan–Sep 2026 +15,353; 12-month September +19,491.
  - Portfolio net: September 2026 +7,733; Jan–Sep 2026 +4,044; 12-month September +4,591.
- These are monthly September, Jan–Sep cumulative and rolling 12-month figures. They are NOT a Q2-only April–June 2026 portfolio asset/liability pair. Do not subtract cumulative periods or infer Q2 from cumulative totals without the exact monthly observation series and matched release vintage.
- The report's narrative says portfolio investments recorded a net outflow of USD7,733m in September under its financing/sign presentation; Table 2's portfolio net row is +7,733m. Preserve the source's table and narrative presentation context; do not silently flip or merge the two sign frames.

## 3. Official data and revision-policy route
- CBRT official BOP statistics page: https://tcmb.gov.tr/wps/wcm/connect/EN/TCMB%2BEN/Main%2BMenu/Statistics/Balance%2Bof%2BPayments%2Band%2BRelated%2BStatistics/Balance%2Bof%2BPayments%2BStatisticss/
- The page states Türkiye's BOP statistics are monthly and compiled under BPM6; it links the September-2026 data ZIP, PDF, metadata, revision policy, methodological changes and future revisions.
- The September-2026 data ZIP link resolved to the official first-party URL ending `/bop.zip`, but the browser retrieval timed out. The Revision Policy PDF link also timed out. These are source locators only; no ZIP/PDF bytes, sheet names, series IDs, headers, Q2 row values, response headers or hashes were obtained.
- The CBRT Methodological Changes index identifies a 13-Aug-2026 item “Revisions to the Financial Account Items of the Balance of Payments Statistics”, a 13-May-2026 item “Reflecting the Investment Fund Shares on Portfolio Liabilities”, and a 12-Mar-2026 item on interest payments on portfolio investments. The index alone does not prove which Q2-2026 portfolio liability observation changed or by how much.
- The CBRT July 24, 2026 press release No. 2026-29 describes changes for currency/deposits and financial derivatives and says these are reflected in June-2026 BOP statistics scheduled for 13-August. That announcement is not a portfolio-liability revision notice and cannot explain the existing USD87m discrepancy.
- Do not infer a Q2 portfolio revision from the existence/title of the annual/monthly release, from a general revision-policy link, or from unrelated financial-account methodology changes.

## 4. Q2-specific decision boundary
| Test | Result | Explanation |
|---|---|---|
| New official CBRT September-2026 release | PASS | First-party PDF opened and Table 2 extracted |
| Latest release contains separate portfolio A/L | PASS, limited | September month and Jan–Sep / 12-month aggregates only |
| Q2-2026 April–June separate A/L pair in inspected PDF | NOT_EXPOSED | No Q2-only row in the report's Table 2 |
| Official September data ZIP locator | FOUND | Exact first-party URL identified |
| ZIP bytes / workbook or CSV schema / Q2 rows / SHA-256 | NOT_CAPTURED | Retrieval timed out |
| Revision policy PDF bytes/content | NOT_CAPTURED | Retrieval timed out |
| Portfolio-specific Q2 revision identifier | NOT_CAPTURED | Index titles alone are insufficient |
| Existing liability USD87m residual | REVIEW — unchanged | No new Q2-only pair to test |
| Same-vintage CBRT ↔ IMF | NOT_ESTABLISHED | No matched observation-specific source-vintage metadata |
| TUR national validation | PARTIAL / NOT PASS | Asset PASS; liability REVIEW; vintage PENDING; FULL_PASS=NO |
| 63-country aggregate | NOT_AUTHORIZED | No admission change |

## 5. Exact next action / stop rule
- Do not repeat the identical browser ZIP click or PDF revision-policy click through the same reader after timeout.
- Reopen TUR only through a genuinely different supported first-party byte-preserving route that yields the September data ZIP or a distinct CBRT EVDS export, with complete monthly Q2 observations, series IDs, units, sign definitions, revision metadata and raw bytes/hash.
- Once a valid Q2-only asset/liability pair is captured, compare each leg separately to the existing archived IMF rows and preserve all earlier release vintages. Do not net, back-solve or widen tolerance.
- If no distinct supported route is available, retain liability REVIEW and vintage PENDING, and move to another eligible fixed-cohort country.

## 6. Protected invariants
₹0; official/free sources only. No paid APIs, credentials, external contact, fabricated observations, inferred Q2 values, cumulative-to-quarter back-solving, sign inversion, synthetic data, or IMF re-query. Fixed 63-country cohort unchanged. UNKNOWN is neither PASS nor FAIL. CORE-672 (56 Steps × 12 Filters), Engines A–E, Production Selector, RANKING_SCORE, +1 PRESSURE_FADE and IPO-PLX V2.0 unchanged. No production integration, workflow dispatch, merge or aggregate release.
