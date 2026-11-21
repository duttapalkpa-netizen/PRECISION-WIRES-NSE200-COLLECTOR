# GCR Indonesia (IDN) Q2-2026 — BI November 2026 revision-vintage recheck against archived IMF snapshot (Continuation 186)
Date: 2026-11-21 (Asia/Kolkata)
Decision: **NEWER OFFICIAL BI Q3-2026 RELEASE CONFIRMS Q2-2026 PORTFOLIO DUAL-LEG REVISION. BPM5→BPM6 SIGN CROSSWALK REMAINS VALID, BUT BOTH Q2 LEGS NOW DIFFER FROM THE 19-NOV-2026 ARCHIVED IMF SNAPSHOT BY MORE THAN BI'S ±0.5 USDm ROUNDING. EXACT IMF SAME-VINTAGE BRIDGE NOT_ESTABLISHED; IDN PARTIAL / NOT PASS; AGGREGATE NOT_AUTHORIZED.**

## 1. Continuity preflight and duplicate prevention
- Re-fetched the current Master Continuity & Acceptance Ledger, GCR Master Priority Queue, Historical Task Registry, C185 detailed crosswalk, earlier IDN crosswalk/revision report, original BI↔IMF reconciliation and archived exact-key IMF A_NFA_T/L_NIL_T CSVs.
- Confirmed the exact unresolved C185 action: inspect the next official BI SEKI / Q2 revision vintage and test whether the archived IMF observation aligns.
- Excluded completed PASS work: BI BPM5 presentation convention and BPM5→BPM6 sign mapping; old-vintage arithmetic; fixed 63-country cohort; IMF exact-key retrieval and panel QA. No new IMF request, no cohort/panel rebuild, no repeated BI Table V.7 extraction.
- IDN remains the same fixed-cohort member; no change to cohort or its SHA-256.

## 2. New official national release and revision evidence
Bank Indonesia, *Neraca Pembayaran Indonesia — Realisasi Triwulan III 2026*:
- Official report page: https://www.bi.go.id/id/publikasi/laporan/Pages/NPI_Tw-III_2026.aspx
- Official report PDF: https://www.bi.go.id/id/publikasi/laporan/Documents/NPI_Tw-III_2026.pdf
- Publication time shown on the official page: 20-Nov-2026 10:00 WIB; page last updated 20-Nov-2026 14:15 WIB.
- PDF page 28, Box 1, lines 2010–2029 explicitly states that portfolio-investment transaction data for 2026-Q1 and 2026-Q2 were updated because of updated foreign-exchange traffic (LLD) and external-debt (ULN) data.
- PDF page 37, Table 7, reports the revised portfolio-investment financial-account legs (USD million). Its column headers identify 2026 Q1*, Q2*, Q3*; footnote says * = provisional (angka sementara).
- Q2-2026 latest BI Table 7 values are:
  - Portfolio assets (A. Aset): -1,466 USDm (BI BPM5 presentation).
  - Portfolio liabilities (B. Kewajiban): +11,399 USDm (BI BPM5 presentation).
  - Portfolio investment total: +9,934 USDm (BI presentation).
- The older 21-Aug-2026 SEKI V.7 release showed Q2** (Very Temporary): assets -1,488; liabilities +11,440; total +9,953 USDm. The Nov-2026 report explicitly identifies the subsequent Q2 update. Do not treat the earlier Q2** values as current after this newer publication.

## 3. Reused IMF archived vintage — no new request
Exact-key archived IMF rows (receipt already in repository; retrieved 19-Nov-2026, before the BI Q3 report published 20-Nov-2026):
- A_NFA_T: raw OBS_VALUE +1,487,605,237.21664 USD; UNIT=USD; SCALE=6; equivalent +1,487.605237 USDm.
- L_NIL_T: raw OBS_VALUE +11,440,221,641.9221 USD; UNIT=USD; SCALE=6; equivalent +11,440.221642 USDm.
- Raw CSV SHA-256s already recorded: asset `db7198b4c2ccc7bcbe6c45312506913c71507339c6e7bd609c5e1ff6500aae8b`; liability `4ec6d04eae8187bd4235c6120f3be5f67972ff32ebfea1accf6cd0a1ab2b4108`.
- Retrieval timestamps: asset 2026-11-19T06:45:17.435091Z; liability 2026-11-19T06:45:17.874893Z. The official revised BI Q2 values were published on 20-Nov-2026, so the archived IMF transport snapshot predates this newly published national vintage. This is evidence that the compared source snapshots are not the same publication cut; it does not establish the IMF observation's underlying national source vintage.

## 4. Apply the already accepted BI BPM5→IMF BPM6 sign convention
BI official BOP metadata and BPM6 crosswalk previously established in C185/C prior IDN report:
- BI publishes financial-account entries using BPM5 inflow/outflow signs despite BPM6 concepts.
- Convert BI portfolio assets by reversing the BI sign for comparison with IMF A_NFA_T.
- Retain BI portfolio liability sign for comparison with IMF L_NIL_T.
- Do not reopen or refit this convention.

### Updated Q2 dual-leg comparison (USDm)
| Leg | Latest BI Q2 (BPM5) | BI mapped to BPM6 | Archived IMF (19-Nov snapshot) | IMF minus mapped BI | BI rounding bound | Result |
|---|---:|---:|---:|---:|---:|---|
| Portfolio assets / A_NFA_T | -1,466 | +1,466 | +1,487.605237 | +21.605237 | ±0.5 | REVIEW / FAIL rounding |
| Portfolio liabilities / L_NIL_T | +11,399 | +11,399 | +11,440.221642 | +41.221642 | ±0.5 | REVIEW / FAIL rounding |

- Both absolute residuals materially exceed the half-unit whole-USD-million BI publication rounding interval.
- Compared with the prior BI Q2** release, latest revised Q2 asset acquisition magnitude falls by 22 USDm (1,488→1,466); liability incurrence falls by 41 USDm (11,440→11,399); published net total falls by 19 USDm (9,953→9,934).
- The updated BI report attributes portfolio series revisions for Q1–Q2 2026 to updated LLD and ULN source data. This is a substantive source revision, not a rounding difference.
- The archived IMF raw snapshot is dated 19-Nov transport retrieval; it must not be silently overwritten or treated as a same-vintage observation. No IMF re-query is permitted in this task.

## 5. Acceptance matrix
| Gate | Status |
|---|---|
| Fixed cohort / both IMF legs present | PASS (reused) |
| BI BPM5→BPM6 sign convention | PASS (C185) |
| New official BI Q3-2026 report / publication date | PASS |
| Official Q2 revision disclosure (LLD and ULN updates) | PASS |
| Latest BI Q2 portfolio asset/liability legs | PASS — PDF Table 7, USDm |
| Latest BI Q2 revision status | PASS — provisional (*) |
| Archived IMF raw values and transport timestamps | PASS (reused) |
| Asset numeric agreement with latest BI within ±0.5 USDm | FAIL / REVIEW — residual 21.605237 |
| Liability numeric agreement with latest BI within ±0.5 USDm | FAIL / REVIEW — residual 41.221642 |
| Exact IMF observation vintage aligned to latest BI revision | NOT_ESTABLISHED |
| Full IDN national dual-leg validation | PARTIAL / NOT PASS |
| Aggregate admission | NOT_AUTHORIZED |

## 6. Interpretation and next exact action
- C185's sign convention remains correct, but its prior ±0.5 numeric PASS applied only to the older BI Q2** vintage published 21-Aug-2026. It is superseded for current national comparison by the later 20-Nov-2026 BI report.
- The current national Q2 legs are independently evidenced; the archived IMF snapshot predates the BI revision publication. The resulting residuals cannot be explained by BI's rounding.
- Next, only if a later IMF data snapshot is already available in the repository/archive with explicit retrieval and revision metadata, inspect that archived snapshot and compare it to the BI 20-Nov-2026 Q2 revision. Do not issue a new IMF GET in this bounded task. If no later archived IMF snapshot or exact IMF observation revision date is available, retain the mismatch as vintage unresolved and advance to the next eligible fixed-cohort country after full preflight.
- Do not adjust signs, use net totals to back-solve legs, interpolate, or infer that the IMF observation is revised merely because the residuals changed.

## 7. Rejected shortcuts and protected invariants
- Rejected: continue using the superseded 21-Aug BI Q2** values as current national benchmark.
- Rejected: claim that the new ±21.6 / ±41.2 USDm residuals are rounding noise.
- Rejected: treat 19-Nov IMF transport retrieval as a same-vintage match to a BI report published 20-Nov.
- Rejected: re-query IMF, rebuild cohort, or promote net portfolio total as dual legs.
- ₹0; official/free sources only; no synthetic values/timestamps; no production changes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS.
