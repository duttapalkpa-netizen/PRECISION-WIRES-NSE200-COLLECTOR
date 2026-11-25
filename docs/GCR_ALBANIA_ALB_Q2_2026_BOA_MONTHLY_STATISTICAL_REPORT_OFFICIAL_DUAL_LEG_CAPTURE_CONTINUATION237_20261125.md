# GCR — Albania (ALB) Q2-2026 official BNA Monthly Statistical Report dual-leg capture
Date: 2026-11-25 (Asia/Kolkata)
Continuation: 237
Decision: **A distinct official Bank of Albania PDF route was found and its Q2-2026 portfolio investment transaction legs were extracted. This closes the prior “Q2 cells not exposed” data-capture gap without repeating the legacy Main-data route. It does not yet establish the accepted EUR→USD bridge or exact observation vintage/revision chain. ALB advances to DATA_CAPTURED / PARTIAL / NOT PASS; both numeric comparison gates remain REVIEW; aggregate NOT_AUTHORIZED.**

## 1. Mandatory continuity and duplicate-prevention preflight
- Re-read current default-branch Master Continuity Ledger, GCR Priority Queue, 63-country Historical Task Registry, current 63-country matrix, Library Mother File (pages 1–53/addenda through C57) and related GCR reports.
- Reopened ALB C139 (including C140/C141) and C192. Existing ALB sign/taxonomy/methodology findings were reused. The exact legacy Main-data URL and the C140/C141 interactive detail route are closed and were not repeated.
- C192 explicitly left open only a distinct Q2-specific attachment/API/export route. The official Monthly Statistical Report PDF below is a different publication artifact and URL.
- Archived IMF Q2 panel observations from C139 were reused; no IMF re-query, cohort rebuild, or duplicate panel extraction.

## 2. New official source — Bank of Albania Monthly Statistical Report 08/2026
- Official PDF: https://www.bankofalbania.org/rc/doc/RSM_gusht_2026_anglisht_35170.pdf
- The opened PDF identifies itself as MONTHLY STATISTICAL REPORT 08/2026.
- Contents identify External Sector table 2-1 Balance of payments (quarterly). The section is explicitly presented in millions EUR.
- Table 2-1 Financial Account header defines Portfolio investment as column 19 = (20−21), with separate columns:
  - 20: Portfolio investment — Assets
  - 21: Portfolio investment — Liabilities
- The row labelled 2026 / II (Q2 2026) reports:
  - Financial account: −610.16 EURm
  - Portfolio investment net: +31.55 EURm
  - Portfolio investment assets: +156.25 EURm
  - Portfolio investment liabilities: +124.70 EURm
- Arithmetic check: 156.25 − 124.70 = 31.55 EURm exactly. This confirms the published net identity; it is not used to derive either leg.
- Official PDF text was opened and parsed through the web document reader. A direct raw-byte download attempt from the same PDF URL failed in the current container, so no raw PDF bytes, response headers, retrieval receipt, or SHA-256 are claimed. The official URL and page/table content remain cited evidence, but raw-byte provenance is still outstanding.

## 3. Reused national methodology and IMF observations
- Reuse C140/C141 official BoA BPM6 methodology: financial-account asset and liability increases are recorded positive; financial-account balance uses asset change minus liability change. Do not substitute IIP stock observations.
- Reuse C139 archived IMF raw observations without re-query:
  - Asset A_NFA_T, P_F, USD, Q, 2026-Q2: OBS_VALUE=181700604.8387097; SCALE=6; PRECISION=6; DERIVATION_TYPE=O.
  - Liability L_NIL_T, P_F, USD, Q, 2026-Q2: OBS_VALUE=145011618.7096774; SCALE=6; PRECISION=6; DERIVATION_TYPE=O.
- National Q2 legs are now captured in EURm. The IMF rows are in USDm after their existing scale representation. No FX conversion is admitted in this continuation.
- Diagnostic only (not an accepted conversion): the raw ratios IMF-USD / BoA-EUR are approximately 1.16288387097 for each leg. This ratio is algebraically implied by the two datasets; it is not an independently sourced FX rate and must not be used to claim reconciliation.
- BoA Monthly Statistical Report table 2-2 provides monthly average ALL/USD and ALL/EUR exchange rates, but the current capture does not establish the exact transaction-date/quarter aggregation method needed to bridge the two quarterly portfolio legs. No inferred cross-rate or average-rate conversion has been applied.

## 4. Acceptance matrix
| Gate | Status |
|---|---|
| Fixed 63-country cohort membership | PASS (reused) |
| Distinct official Q2-specific source artifact | PASS |
| Official source PDF identity / 08-2026 issue | PASS (document reader) |
| Q2-2026 period row identified | PASS |
| Portfolio asset and liability observations captured separately | PASS (official PDF text) |
| National asset-minus-liability net identity | PASS (31.55 EURm) |
| Raw PDF bytes / response headers / SHA-256 | NOT_CAPTURED |
| National sign convention | PASS (reused C140) |
| National units / EURm | PASS |
| Existing IMF Q2 rows | PASS (reused C139) |
| EURm→USDm conversion method for these quarterly flow legs | NOT_ESTABLISHED |
| Asset numeric reconciliation | REVIEW / NOT_PASS |
| Liability numeric reconciliation | REVIEW / NOT_PASS |
| Exact same-vintage/revision bridge | UNKNOWN / NOT_ESTABLISHED |
| Full ALB national validation | DATA_CAPTURED / PARTIAL / NOT PASS |
| Aggregate admission | NOT_AUTHORIZED |

## 5. Duplicate prevention and next action
- Do not repeat the official PDF URL through the same retrieval surface merely to recreate text already captured; do not repeat C140/C141/C192 legacy Main-data routes.
- Reopen only for a distinct supported raw-byte/download path for this exact official PDF or a newer dated BoA Q2 revision/methodology record that establishes the observation vintage and transaction FX conversion convention.
- Next bounded task: independently establish the official Q2 transaction FX bridge (prefer BoA’s published flow-conversion rule plus dated monthly observations at transaction period) and revision cutoff; compare legs only after the conversion is authorized. If that cannot be established, retain REVIEW/PENDING and advance to the next fixed-cohort item.
- No IMF re-query, cohort rebuild, or national net-to-leg back-solving.

## 6. Protected invariants
₹0; free official sources only; no synthetic data, fabricated timestamps, IIP stock substitution, net-to-leg back-solving, unsupported sign/scale/FX conversion, paid source, or external contact. UNKNOWN is neither PASS nor FAIL. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2.0 unchanged. No production integration or merge.
