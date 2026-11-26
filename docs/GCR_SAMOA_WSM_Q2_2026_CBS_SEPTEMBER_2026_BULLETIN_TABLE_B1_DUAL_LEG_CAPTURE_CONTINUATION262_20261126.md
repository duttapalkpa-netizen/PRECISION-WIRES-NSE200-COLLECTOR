# Samoa (WSM) Q2-2026 — CBS September 2026 Bulletin Table B-1 dual-leg capture
Date: 2026-11-26 (Asia/Kolkata)
Continuation: 262
Status: OFFICIAL Q2-2026 NATIONAL PORTFOLIO DUAL LEGS CAPTURED; BPM6/TALA-MILLION SOURCE METADATA VISIBLE; NUMERIC CROSS-SOURCE COMPARISON AND SAME-VINTAGE GATE PENDING; WSM DATA_CAPTURED / PARTIAL / NOT PASS; AGGREGATE NOT_AUTHORIZED.

## 1. Continuity preflight and duplicate prevention
- Re-fetched current Master Continuity Ledger, GCR Master Priority Queue, Historical Task Registry and immutable 63-country national validation matrix before selecting the task.
- Re-read Library Mother File `PRECISION_WIRES_V11_3_MOTHER_FILE_CONTINUATION_1_53_20261122.md` and controlling WSM reports C125, C126 and C243.
- C125/C126 established that the June-2026 bulletin was the March-2026/Q1 issue, with Table B-1 ending at 2026-I. C243's 25-Nov direct-index check found June 2026 still latest and correctly rejected an unconfirmed September search snippet at that time.
- Fresh 26-Nov official index inspection now directly lists September 2026 as latest and was followed to a distinct official PDF. This is a new release route, not a repeat of the June PDF or prior cached search snippet.
- Reused the immutable cohort and already archived IMF raw panels. No IMF re-query, cohort rebuild, or duplicate prior-quarter extraction.

## 2. New official CBS issue and period identity
- Official CBS Quarterly Bulletin index: https://cbs.gov.ws/quarterly-bulletin
- The page's current Latest list directly names “Quarterly Bulletin September 2026” and shows “Last updated 19 Nov 2026”. It says bulletins provide data through the end of the quarter under review and are published with a three-month delay.
- Exact official PDF URL: https://cbs.gov.ws/media/Quarterly-Bulletin---September-2026.pdf
- PDF internal identity: “QUARTERLY BULLETIN SEPTEMBER 2026”, Vol. XLV No.3; contents and overview identify developments during the second quarter of 2026. There is a first extracted cover leaf at PDF page 0 carrying an older “June 2026” label, while the following internal title page (PDF page 2) and contents identify September 2026 / Vol. XLV No.3. This internal cover-leaf inconsistency is retained as a document-quality caveat; it does not override the internal title, contents, issue listing and Q2 narrative.
- Table B-1 is “Balance of Payments”, printed page 35 (PDF page index 38), under “B – External Trade and Payments”. It explicitly states “Amounts in Tala Million”.
- Table B-1 columns show annual totals 2022/23–2025/26, then calendar-year quarter columns 2022 I–IV, 2023 I–IV, 2024 I–IV, 2025 I–IV and 2026 I–II. C125 established that 2026-I in the prior issue was the March 2026 quarter. The new issue's 2026-II is therefore the June 2026 / Q2-2026 column; this mapping is consistent with the issue's explicit second-quarter-of-2026 narrative and its two 2026 quarter columns.
- The table footnote states it is based on the 6th Edition of the IMF Balance of Payments Manual (BPM6).

## 3. National Q2-2026 portfolio transaction legs captured
Read the final 2026-II column in Table B-1:
- Portfolio Investment (net): +9.3 Tala million.
- Portfolio Investment — Assets: +9.5 Tala million.
- Portfolio Investment — Liabilities: +0.2 Tala million.
- Internal table arithmetic: 9.5 − 0.2 = 9.3 Tala million. This is a consistency check on the published table rows, not an independent sign-convention bridge.
- The values are transaction-flow rows in the Balance of Payments table, not the separate International Investment Position stock table.
- Preserve source unit exactly as Tala million. No Tala/USD conversion, no inferred exchange rate and no unapproved sign transformation was performed.

## 4. Existing IMF Q2 rows reused — no query
From the already archived raw IMF panel files:
- Asset file: `docs/evidence/imf_bop_emde_20261119/raw/EMDE_A_NFA_T_P_F_ALL_UNITS_Q.csv`, Git blob SHA `15449e87c9057291a1f52f2f8cd9805df55f9fb8`.
  - Exact WSM row: COUNTRY=WSM; ENTRY=A_NFA_T; INDICATOR=P_F; UNIT=USD; FREQUENCY=Q; PERIOD=2026-Q2; OBS_VALUE=3499391.164998622; SCALE=6; PRECISION=6; DERIVATION_TYPE=O; IFS_FLAG=true.
- Liability file: `docs/evidence/imf_bop_emde_20261119/raw/EMDE_L_NIL_T_P_F_ALL_UNITS_Q.csv`, Git blob SHA `15f379dc42e2760eb5f2384618e48f5ddc3177f1`.
  - Exact WSM row: COUNTRY=WSM; ENTRY=L_NIL_T; INDICATOR=P_F; UNIT=USD; FREQUENCY=Q; PERIOD=2026-Q2; OBS_VALUE=72224.22595641938; SCALE=6; PRECISION=6; DERIVATION_TYPE=O; IFS_FLAG blank.
- Raw OBS_VALUE and SCALE retained exactly. No scale conversion, USD conversion or numeric comparison was performed.

## 5. Remaining validation gates / source limitations
- National dual-leg presence and period/unit/methodology metadata: CAPTURED from official CBS Table B-1.
- Official raw PDF byte download through the current container retrieval path failed; therefore byte count, receipt timestamp, locally computed SHA-256 and a byte-level archived copy were NOT_CAPTURED in this continuation. The public official PDF URL and directly inspected PDF text/page image are retained as source evidence. Do not fabricate a file hash or byte count.
- No same-vintage link between the CBS September 2026 table and the archived IMF 19-Nov panel rows was identified.
- National values are Tala million while IMF rows are USD with SCALE=6. A transaction-specific/period-appropriate official FX bridge and exact sign/scale reconciliation are not established in this task. No comparison residual or PASS is claimed.
- The IIP Table B-9 contains stocks and is excluded from transaction comparison.
- The first PDF cover leaf's stale June label is recorded; the internal September issue title, Vol. XLV No.3, Q2 overview, direct official index listing and 2026-II Table B-1 columns support the new issue/period identity.

## 6. Acceptance
| Gate | Result |
|---|---|
| WSM membership in immutable 63-country Q2 cohort | PASS (reused) |
| New official CBS September 2026 issue listed on direct index | PASS |
| Official PDF opened and internal September issue/Q2 coverage identified | PASS, with stale first-cover-leaf caveat |
| Table B-1 Q2-2026 separate portfolio asset row | CAPTURED: +9.5 Tala million |
| Table B-1 Q2-2026 separate portfolio liability row | CAPTURED: +0.2 Tala million |
| Published portfolio net row | CAPTURED: +9.3 Tala million |
| Internal table arithmetic | PASS: 9.5 − 0.2 = 9.3 |
| BPM6 note / Tala-million unit | PASS |
| National PDF bytes / byte count / SHA-256 | NOT_CAPTURED |
| Existing IMF Q2 asset/liability rows | PASS (reused, no query) |
| Tala-to-USD transaction conversion and cross-source numeric comparison | NOT_DONE |
| Same-vintage/revision bridge | UNKNOWN / NOT_ESTABLISHED |
| Full WSM national dual-leg validation | PARTIAL / NOT PASS |
| 63-country aggregate authorization | NOT_AUTHORIZED |

## 7. Next bounded action
- Seek a supported official byte-transfer route for this exact CBS PDF, or a genuinely distinct official CBS raw-table download, to archive bytes and compute SHA-256; do not fabricate provenance.
- Establish the official transaction/period FX conversion rule and observation-vintage relation before any USD comparison. Use no generic or guessed FX rate.
- If the FX/vintage bridge cannot be established from official evidence, retain WSM DATA_CAPTURED / PARTIAL / NOT PASS and proceed to the next eligible fixed-cohort member. Do not re-extract C125/C126, do not repeat the old June PDF, and do not re-run the C243 stale-index check as if the September issue were still unlisted.

## 8. Protected invariants
₹0; official/free sources only; no IMF re-query/cohort rebuild; no net-to-leg back-solving; no IIP stock-as-flow; no fabricated bytes/hash/timestamps; no inferred FX/sign/scale; UNKNOWN never PASS; Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2.0 unchanged; no workflow dispatch, merge or production integration.
