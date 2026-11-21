# GCR Indonesia (IDN) Q2-2026 — Bank Indonesia BPM5 presentation to IMF BPM6 sign crosswalk (Continuation 185)
Date: 2026-11-21 (Asia/Kolkata)
Decision: **BI ASSET-SIGN MISMATCH RESOLVED BY OFFICIAL BI PRESENTATION METADATA + IMF BPM5↔BPM6 SIGN RULE; BOTH LEGS NUMERICALLY RECONCILE WITHIN BI ±0.5 USDm DISPLAY ROUNDING AFTER THE DOCUMENTED CROSSWALK. FULL NATIONAL VALIDATION REMAINS PARTIAL / NOT PASS BECAUSE Q2 BI OBSERVATION IS VERY TEMPORARY AND EXACT SAME-VINTAGE / SUBSEQUENT-REVISION IDENTITY IS NOT ESTABLISHED. AGGREGATE NOT_AUTHORIZED.**

## 1. Continuity preflight and duplicate prevention
- Re-fetched current Master Continuity & Acceptance Ledger, GCR Master Priority Queue, Historical Task Registry, the existing IDN Q2-2026 comparison, the fixed cohort and exact-key archived IMF CSVs before selecting this open dependency.
- Existing IDN report had one unresolved actionable item: explicit BI asset-sign presentation crosswalk to IMF A_NFA_T. No later dedicated IDN follow-up report was found in the current repository tree.
- Reused fixed 63-country cohort and existing 12-country exact-key IMF receipt. Exact cohort row: `IDN,Indonesia,2026-Q2,A_NFA_T_PRESENT,L_NIL_T_PRESENT,BOTH_LEGS_PRESENT_IN_IMF_PANEL,NATIONAL_SOURCE_VINTAGE_VALIDATION_PENDING,NOT_AUTHORIZED`.
- No IMF re-query, cohort rebuild, panel rebuild, BI table re-extraction beyond official metadata inspection, or production change.

## 2. Primary-source presentation evidence — Bank Indonesia
Official Bank Indonesia BOP metadata:
https://www.bi.go.id/en/statistik/Metadata/SEKI/Documents/Indonesia_Summary_Balance_of_Payments_.pdf
Relevant metadata facts:
- Section 2.2 / 4.1: Indonesia BOP compiled with BPM6 concepts; financial account records asset and liability transactions separately.
- Section 2.2: portfolio assets are resident acquisitions of securities issued by non-residents; portfolio liabilities are non-resident acquisitions of securities issued by residents.
- Section 4.3, especially paragraph at PDF text lines 124–125: although compiled with BPM6 concepts, the published data are still presented based on BPM5; capital and financial account asset/liability sides are presented as net inflow/outflow, positive for inflow/credit and negative for outflow/debit.
- Section 5.5: initial data are provisional, become preliminary in the subsequent quarter, and quarterly data become final 12 months after the release of the last quarterly data of the same year; provisional/preliminary/revised status is annotated.
- This is the previously missing explicit BI-side presentation metadata. It supports a presentation conversion; it does not establish that the Q2** very-temporary vintage equals the IMF snapshot vintage.

## 3. Authoritative BPM5↔BPM6 sign bridge
IMF, *BPM6 Compilation Guide*, Table 8.10, lines 4395–4421:
https://www.imf.org/external/pubs/ft/bop/2014/pdf/guidefinal.pdf
The IMF states:
- BPM6 financial account: increases in assets and liabilities are positive; decreases are negative.
- BPM5 financial account: increases in assets and decreases in liabilities are debits (negative); decreases in assets and increases in liabilities are credits (positive).
Therefore, for the BI published BPM5 presentation versus IMF BPM6:
- Portfolio asset leg: reverse BI's BPM5 sign to compare with BPM6 A_NFA_T.
- Portfolio liability leg: retain BI's BPM5 sign to compare with BPM6 L_NIL_T.
This is a documented convention crosswalk, not a fitted sign or a residual-driven adjustment.

## 4. Reused Q2-2026 source values and comparison
Bank Indonesia SEKI Table V.7, “Financial Account: Portfolio Investment”:
https://www.bi.go.id/SEKI/tabel/TABEL5_7.pdf
Printed page 137 / PDF page 2, unit USD millions. Q2** 2026:
- BI portfolio assets: -1,488 USDm.
- BI portfolio liabilities: +11,440 USDm.
- BI marks Q2 2026 as **Very Temporary Data**.
Archived IMF exact-key receipt reused (Run 44474458684; artifact 14505009889; ZIP SHA-256 `588101c0deff3b4310984dae5eabcac64fc8288f4416854b7676b4b6ff6b4cd7`):
- A_NFA_T raw OBS_VALUE +1,487,605,237.21664 USD; UNIT=USD, SCALE=6; comparison value +1,487.605237 USDm.
- L_NIL_T raw OBS_VALUE +11,440,221,641.9221 USD; UNIT=USD, SCALE=6; comparison value +11,440.221642 USDm.
- Existing exact raw CSV SHA-256s: A_NFA_T `db7198b4c2ccc7bcbe6c45312506913c71507339c6e7bd609c5e1ff6500aae8b`; L_NIL_T `4ec6d04eae8187bd4235c6120f3be5f67972ff32ebfea1accf6cd0a1ab2b4108`. These remain unchanged.

### Crosswalk arithmetic (USDm)
| Leg | BI published BPM5 sign | BI mapped to BPM6 | IMF BPM6 value | Absolute residual | Rounding decision |
|---|---:|---:|---:|---:|---|
| Portfolio assets / A_NFA_T | -1,488 | +1,488 | +1,487.605237 | 0.394763 | PASS within ±0.5 |
| Portfolio liabilities / L_NIL_T | +11,440 | +11,440 | +11,440.221642 | 0.221642 | PASS within ±0.5 |

- BI whole-USD-million display precision implies ±0.5 USDm half-unit rounding bound.
- The two legs are compared independently. No net-to-leg back-solving, offsetting, or residual-tuned transformation.
- The mapped legs imply a national net of +1,488 - 11,440 = -9,952 USDm; the published table reports portfolio investment total +9,953 USDm under BI's BPM5 inflow/outflow presentation. Do not use this net line to override the independently compared legs or silently reinterpret the aggregate's convention. The separate leg crosswalk is the comparison basis.

## 5. Acceptance matrix
| Gate | Status |
|---|---|
| Fixed 63-country cohort row / both IMF legs present | PASS |
| Existing IMF exact-key receipt reused; no new request | PASS |
| BI official detailed Q2 portfolio assets/liabilities table | PASS |
| BI official metadata explicitly states BPM5 presentation despite BPM6 concepts | PASS |
| IMF official BPM5↔BPM6 sign bridge | PASS |
| Asset sign crosswalk (BI BPM5 to IMF BPM6) | PASS |
| Liability sign crosswalk | PASS (same sign) |
| Asset numeric residual within BI rounding bound | PASS |
| Liability numeric residual within BI rounding bound | PASS |
| BI Q2** vintage identified | PASS — Very Temporary |
| Exact same-vintage BI/IMF observation identity | NOT_ESTABLISHED |
| Subsequent BI Q2 revision comparison against same IMF vintage | NOT_DONE |
| Full IDN national dual-leg validation | PARTIAL / NOT PASS |
| Aggregate admission | NOT_AUTHORIZED |

## 6. Next exact action
- Check the next official BI SEKI V.7 vintage / subsequent Q2-2026 publication for revised Q2 values and revision markers, and establish whether an IMF observation snapshot with the matching BI vintage exists in the archived evidence.
- Preserve the BPM5→BPM6 mapping above; do not reopen the sign question unless BI publishes an explicit methodology change or a revised definition.
- If exact same-vintage identity cannot be established, retain IDN PARTIAL / NOT PASS despite the two rounded numeric comparisons passing.

## 7. Rejected shortcuts and invariants
- Do not treat BI's BPM6 compilation basis as proof that its published signs are BPM6; BI explicitly says its publication remains BPM5 presentation.
- Do not reverse both legs: only the asset sign changes under the BPM5↔BPM6 financial-account rule; liability sign is unchanged.
- Do not infer sign from net portfolio total, IIP stocks, or financial-account balance.
- Do not claim same-vintage identity from close values; Q2 BI is marked very temporary.
- ₹0; official/free sources only. No synthetic data/timestamps, no IMF re-query, no cohort rebuild, no production changes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS.
