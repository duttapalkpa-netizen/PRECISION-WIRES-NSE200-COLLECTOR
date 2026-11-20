# GCR Indonesia IDN — official BI sign-convention crosswalk and Q2-2026 recheck
Date: 2026-11-20
Decision: **Asset sign crosswalk PASS; both numerical legs PASS at BI published precision; full same-vintage country validation remains PARTIAL / NOT PASS pending explicit IMF-vs-BI vintage alignment. Aggregate NOT_AUTHORIZED.**

## Progress log / preflight
- Re-fetched the Master Continuity Ledger, GCR priority queue, IDN reconciliation, CHN SAFE blocker, cross-country benchmark and fixed 63-country cohort.
- Excluded completed PASS work: IMF DSD capture, 154-country roster, 9,299-row QA, fixed cohort, IDN 12-country exact-key receipt and prior BI table extraction. No new IMF GET, no panel/cohort rebuild.
- Continued the exact open IDN task: official BI portfolio asset sign convention and revision/vintage rules.

## 1. Official Bank Indonesia sign-convention evidence
A. BI publication “Penerapan BPM6: Apa yang Berubah pada Neraca Pembayaran Indonesia (NPI)” (official PDF):
https://www.bi.go.id/id/publikasi/ruang-media/news-release/Documents/Lampiran-Apa%20yang%20Berubah%20pada%20NPI.pdf
- Lines 30–46: BI says BPM6 classification/method improvements were implemented while the +/- sign convention previously used in BPM5-based NPI publications was retained.
- Lines 149–165: financial-account presentation changed to asset/liability principle.
- Table footnote 4, lines 238–239: in financial transactions, inflow (asset reduction/liability increase) is positive; outflow (asset increase/liability reduction) is negative.
This explicitly documents the BI sign convention; it is not an inferred or residual-fitted transform.

B. BI official English BOP metadata, status update July 2024:
https://www.bi.go.id/en/statistik/Metadata/SEKI/Documents/Indonesia_Summary_Balance_of_Payments_.pdf
- §2.2, lines 67–73: portfolio assets include residents' acquisition of securities issued by non-residents; portfolio liabilities include non-residents' acquisition of securities issued by residents.
- §2.3, lines 80–85: measurement unit USD millions; quarterly and annual reference periods.
- §4.1, lines 100–107: BOP transactions compiled under BPM6 and financial-account asset and liability transactions recorded separately.
- §4.3, lines 119–125: although compiled referring to BPM6, BI presents capital and financial account asset/liability entries as net inflow/outflow; positive for inflow/credit and negative for outflow/debit.
Together these definitions establish:
- BI portfolio asset purchase/increase = outflow = negative; IMF A_NFA_T is net acquisition of financial assets, so the numeric sign is opposite for this crosswalk.
- BI portfolio liability incurrence/increase = inflow = positive; IMF L_NIL_T is net incurrence of liabilities, so the numeric sign is consistent.
Do not apply this country-specific convention universally to other countries.

## 2. Q2-2026 vintage and publication status
- BI Q2 2026 BOP report page: https://www.bi.go.id/en/publikasi/laporan/Pages/NPI_Tw-II_2026.aspx
- Published 2026-08-21 10:00 WIB; page last updated 2026-09-17 20:47 WIB.
- The already inspected SEKI Table V.7 marks Q2 2026 with **, defined in the table as “Very Temporary Data”.
- BI metadata's revision section states first release is very preliminary, then preliminary the next month, and final five months after first release; revised values are marked (r). As at this audit date (2026-11-20), Q2 is still within the five-month finalization window. The BI source vintage is therefore explicitly provisional/very temporary.
- Existing IMF exact-key receipt was retrieved 2026-11-19. The archived receipt records transport retrieval time but the current audit has not established that the IMF Q2 observation is from exactly the same BI source vintage. Do not call the two vintages aligned.

## 3. Reconciliation using only the documented BI sign transform
Existing national table (BI SEKI V.7, Q2** 2026, USDm): portfolio assets -1,488; portfolio liabilities +11,440.
Existing exact IMF receipt: run 44474458684 / artifact 14505009889 / ZIP SHA-256 `588101c0deff3b4310984dae5eabcac64fc8288f4416854b7676b4b6ff6b4cd7`.
IMF raw Q2 2026 values, SCALE=6 (Millions):
- A_NFA_T = +1,487,605,237.21664 USD = +1,487.605237 USDm.
- L_NIL_T = +11,440,221,641.9221 USD = +11,440.221642 USDm.

| Leg | BI original USDm | Official BI→IMF sign map | BI mapped USDm | IMF USDm | IMF−mapped BI residual | Bound | Numeric result |
|---|---:|---|---:|---:|---:|---:|---|
| Assets | -1,488 | negate BI outflow-positive acquisition convention to IMF net-acquisition sign | +1,488 | +1,487.605237 | -0.394763 | ±0.5 | PASS |
| Liabilities | +11,440 | retain sign (inflow / incurrence positive) | +11,440 | +11,440.221642 | +0.221642 | ±0.5 | PASS |

The ±0.5 USDm bound is the half-unit rounding interval from BI's whole-USD-million publication. Both numerical residuals are inside the bound. The asset sign transformation is supported by BI's explicit methodology and portfolio-asset definition, not a fit to observed values.

## 4. Acceptance matrix
| Gate | Status |
|---|---|
| BI BPM6 implementation and retained BPM5 +/- convention | PASS |
| BI portfolio asset/liability definitions | PASS |
| BI asset sign mapping to IMF A_NFA_T | PASS |
| BI liability sign mapping to IMF L_NIL_T | PASS |
| Q2-2026 asset numerical comparison | PASS at published rounding |
| Q2-2026 liability numerical comparison | PASS at published rounding |
| BI Q2 vintage identified | PASS — Very Temporary Data |
| Exact BI↔IMF same-vintage alignment | REVIEW / NOT_ESTABLISHED |
| IDN same-vintage national dual-leg validation | PARTIAL / NOT PASS |
| 63-country aggregate | NOT_AUTHORIZED |

## 5. Next exact action
Keep IDN's sign mapping and rounded numerical reconciliation closed as PASS, but retain country-level full validation as PARTIAL until a dated BI historical revision/vintage snapshot can be matched to the IMF observation vintage or an exact revision history confirms the same Q2 values. If no public version history is available, preserve the vintage limitation and continue the next cohort country. Do not re-run IMF exact GETs or reinterpret the sign rule.

## Protected invariants
No aggregate, netting, imputation, forward-fill, synthetic observations, silent sign flip, or production integration. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS.
