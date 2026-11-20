# GCR Morocco (MAR) Q2-2026 — Office des Changes ↔ IMF portfolio dual-leg source reconciliation
Date: 2026-11-20 (Asia/Kolkata)
Decision: **Official national dual-leg Q2 values and accounting identity PASS at source precision; exact IMF rows recovered from the pre-existing archive; national-to-IMF asset sign conflict observed; currency/vintage comparability NOT_ESTABLISHED; MAR remains PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.**

## 1. Continuity and selection
- Re-fetched current Master Continuity Ledger, GCR Master Priority Queue and prior MDA Continuation 86 report before selecting work.
- MDA remains PARTIAL: the BNM interactive report route was identified but cannot be operated by the current read-only browser; no generated export or raw bytes exist. Do not repeat that failed XLSX route. Advance within the fixed cohort.
- Reused fixed 63-country Q2-2026 both-leg cohort CSV (blob SHA 31f5bfe5adb59f4c1a139b6d8c54b5ad9fb672c8); MAR (Morocco) is a member with both IMF legs present. No cohort rebuild and no new IMF request.
- Repository search found no dedicated MAR Q2-2026 national portfolio dual-leg reconciliation report. MAR selected because the official Office des Changes Q2 report publishes both portfolio transaction legs directly in native MAD units.

## 2. Official national source — Office des Changes Q2 report
- Primary source: Office des Changes, “Balance des paiements — Deuxième trimestre 2026”, official PDF:
  https://www.oc.gov.ma/sites/default/files/2026-10/BDP_2026_T2.pdf
- PDF explicitly labels data “Données provisoires (en millions de dirhams)” — preliminary, million MAD.
- Financial-account table columns are explicitly:
  1) Acquisition nette d’avoirs (net acquisition of financial assets)
  2) Accroissement net des engagements (net incurrence of liabilities)
  3) Solde (balance)
- Portfolio investment row, Q2-2026 (million MAD):
  * Assets / net acquisition: +4,848
  * Liabilities / net incurrence: +36,933
  * Portfolio balance: -32,085
- Displayed component arithmetic:
  * Assets: equity/fund shares +1,101; debt securities +3,747; sum +4,848.
  * Liabilities: equity/fund shares -855; debt securities +37,788; sum +36,933.
  * Balance identity: 4,848 - 36,933 = -32,085, exact at published integer precision.
- This is a dual-leg transaction-flow table, not IIP stocks and not net-only. Preserve native million-MAD units and preliminary flag.
- The official Office des Changes release calendar lists Q2-2026 BOP publication on 30-Sep-2026. No separate historical revision chain was captured.

## 3. Independent official dissemination surface and sign-presentation boundary
- Morocco Ministry of Economy and Finance “Morocco: Economic and Financial Data” DSBB page:
  https://www.finances.gov.ma/Pages/TAND_Maroc_english.htm
- Page states its data correspond to IMF DSBB prescribed data; last update 13-Nov-2026; BOP is compiled according to IMF BPM6; changes are expressed in million dirhams.
- Its Q2/26 summary displays portfolio assets +4,848 MDH and portfolio liabilities -36,933 MDH. This is the same national pair of magnitudes as the Office des Changes detailed PDF, but the Ministry summary presents the liability entry with the opposite sign to the PDF's explicitly labelled “net incurrence of liabilities” column.
- The Ministry financial-account summary identity uses signed entries (assets + liabilities-as-negative) and reports the total financial-account balance -16,389 MDH. Do not interpret its signed liability -36,933 as the raw BPM6 L_NIL_T value without applying a documented presentation crosswalk.
- For this report, the primary national comparison convention is the Office des Changes PDF's explicit column label “net incurrence of liabilities” (+36,933). The DSBB summary is an independent display check, not an additional observation.

## 4. Existing IMF Q2 rows — recovered from committed artifact; no re-query
- Downloaded existing workflow artifact 14505862034 from run 44474218174. ZIP SHA-256 verified locally: 1a1a184f3689e04ff75d4433b44904083a33e18bdc70f096c3e9919900ebeb4f. This is the already archived EMDE panel; no new IMF request.
- Normalized panel CSV SHA-256: e8a44abbc8455fef44cc1e4677018ae4b9634d1c04f65bf6fc6dad133cfce62a.
- Raw IMF asset CSV SHA-256: 677054017f5d3ae5fdd0403d7341588ebf43ad8b54124ae1b616bf323229326e.
- Raw IMF liability CSV SHA-256: 713b7a3000712e2ffb07cd574d08d7e6f3c02a6b2573ce4b40d06e0458cd7bba.
- Exact normalized MDA rows, dataflow IMF.STA:BOP(21.0.0), indicator P_F, unit USD, quarterly 2026-Q2, SCALE=6, PRECISION=6, DERIVATION_TYPE=O, ACTION=R:
  * A_NFA_T: OBS_VALUE = -28,987,027.88 USD; IFS_FLAG=true.
  * L_NIL_T: OBS_VALUE = +9,083.44 USD; IFS_FLAG blank.
- Raw OBS_VALUE and SCALE remain unchanged. Prior empirical IMF panel comparisons use OBS_VALUE / 1,000,000 only as a derived USD-million comparison field; that convention does not alter stored source values.

## 5. Comparison and blocker decision
- National source publishes MAD million; IMF rows are USD. No Q2-2026 official daily/quarterly-average MAD/USD conversion series, matching convention or raw FX capture was established in this bounded task. Therefore no numeric USD comparison or residual is calculated.
- Asset direction diagnostic: national Office des Changes reports positive net acquisition of assets (+4,848 MDH), while IMF A_NFA_T raw OBS_VALUE is negative (-28,987,027.88 USD). This is a sign conflict at the labelled concept level; do not silently flip either series. Scope, valuation, source revision and/or mapping may differ; cause NOT_ESTABLISHED.
- Liability: Office des Changes explicitly reports positive net incurrence (+36,933 MDH); IMF L_NIL_T is positive (+9,083.44 USD), so signs agree, but magnitude comparison is impossible without an official FX convention and scope/vintage bridge.
- IMF ACTION=R indicates revised status, not the exact observation revision timestamp. Office des Changes Q2 source is preliminary. Same-vintage alignment NOT_ESTABLISHED.
- No national raw PDF bytes, HTTP headers, retrieval UTC, byte count or SHA-256 were captured: web extraction provided the table, while direct byte download failed. Do not claim a raw national-file hash.

## 6. Acceptance
| Gate | Status |
|---|---|
| MAR in fixed 63-country Q2 both-leg cohort | PASS |
| Official Office des Changes Q2-2026 source identified | PASS |
| Separate portfolio asset and liability flow legs extracted | PASS |
| Component arithmetic and net identity | PASS (3/3 identities) |
| Official DSBB summary cross-display located | PASS |
| Liability sign presentation difference identified | PASS — presentation boundary only |
| Existing IMF exact Q2 rows recovered without re-query | PASS |
| IMF raw values and source-file hashes preserved | PASS |
| Asset sign/concept reconciliation | REVIEW / NOT_RESOLVED |
| MAD→USD Q2 comparison FX convention | NOT_ESTABLISHED |
| Numeric dual-leg national↔IMF comparison | NOT_DONE |
| Same-vintage / revision cut-off | NOT_ESTABLISHED |
| National raw PDF bytes + SHA-256 | NOT_CAPTURED |
| MAR full national validation | PARTIAL / NOT PASS |
| 63-country aggregate admission | NOT_AUTHORIZED |
| Production integration | NOT_AUTHORIZED |

## 7. Next exact action
- Seek an official Bank Al-Maghrib / Office des Changes Q2-2026 daily or quarterly-average MAD/USD reference series and its precise averaging convention; archive raw bytes and hash before calculating a conversion.
- Inspect Office des Changes' BPM6 compilation methodology for the asset sign and DSBB summary liability-sign transformation. Do not infer sign transformation from arithmetic alone.
- Then compare separate legs against the already recovered IMF rows using the official conversion convention and source display rounding; seek observation-specific revision vintage.
- If the official Q2 FX convention or observation-level revision bridge is not public, retain MAR PARTIAL / NOT PASS and advance to the next cohort member. No new IMF request, cohort rebuild, unsupported FX conversion, netting, or production change.
- Official sources:
  * Office des Changes Q2-2026 BOP PDF: https://www.oc.gov.ma/sites/default/files/2026-10/BDP_2026_T2.pdf
  * Office des Changes Q2 release calendar: https://www.oc.gov.ma/fr/methodologie/calendrier-de-diffusion
  * Ministry of Economy and Finance DSBB summary: https://www.finances.gov.ma/Pages/TAND_Maroc_english.htm
  * Office des Changes BOP/IIP publications: https://www.oc.gov.ma/fr/balance-paiements
- ₹0; official/free sources only. No synthetic data, fabricated timestamps, net-only substitution, annual-to-quarter allocation, unsupported FX, netting, forward-fill or production changes. Fixed 63-country cohort and all production invariants unchanged. UNKNOWN is never PASS.
