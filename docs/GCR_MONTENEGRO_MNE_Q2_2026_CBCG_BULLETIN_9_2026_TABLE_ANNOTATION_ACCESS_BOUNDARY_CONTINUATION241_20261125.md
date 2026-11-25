# GCR — Montenegro (MNE) Q2-2026 CBCG Bulletin 9/2026 table-annotation access boundary

Date: 2026-11-25 (Asia/Kolkata)
Continuation: 241

Decision: **The official Bulletin 9/2026 and its BoP methodology were independently re-opened. The PDF text reader exposes the “Tables 5.1–5.4 — download tables” label but does not expose a clickable annotation target or payload URL. A byte-preserving PDF download attempt failed. No table workbook/CSV bytes, Q2 portfolio asset/liability values, response metadata or hash were obtained. MNE remains PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.**

## 1. Mandatory continuity preflight and selection
- Re-fetched current Master Continuity Ledger, GCR Priority Queue, Historical Task Registry and 63-country national validation matrix. Re-read the Library Mother File Continuation 1–53 and available GCR context.
- C240 (TJK) was already committed after C239. C237–C240 accepted/bounded work was skipped; no repeat of ALB, BGD or TJK.
- MNE is a fixed 63-country cohort member. Its controlling prior report is C182. The registry explicitly permits reopening only to resolve the Bulletin PDF's linked Tables 5.1–5.4 annotation or a distinct official CBCG export interface.
- Re-fetched C182 and reviewed its exact next action. The earlier CBCG ZIP and MONSTAT NSDP SDMX/XML/Browse routes remain closed and were not retried. No IMF re-query/cohort rebuild.

## 2. New bounded official-source recheck
- Official CBCG Bulletin archive: https://www.cbcg.me/en/publications/regular-publications/cbcg-bulletin
- Official Bulletin 9/2026 PDF: https://www.cbcg.me/slike_i_fajlovi/fajlovi/fajlovi_publikacije/biltencbcg/2026/bilten_9-2026.pdf
- The archive currently lists issues 10/2026 through 1/2026; the official publications feed dates Bulletin 9/2026 to 24-Oct-2026 (archive page current listing confirms 9/2026).
- PDF document reader opened the 65-page official Bulletin. It identifies the BoP section on printed page 55 / PDF page 54 and exposes “Tables 5.1–5.4 - download tables” as text, but no link target/annotation ID or direct workbook URL is exposed in the available extraction surface.
- The PDF states BoP follows IMF BPM6, is published quarterly in EUR, and source-currency conversion uses CBCG middle rates at transaction day, monthly and annual middle average rates, and period-end daily rate for monitored valuation differences. Direct and portfolio investment are monitored using foreign payment operations statistics (ITRS) and surveys.
- The PDF warns that bulletin data are preliminary and may be revised as final data become available.
- The 2026 CBCG dissemination calendar lists Q2-2026 IIP for 21-Sep-2026. This is an IIP position release date, not proof of Q2 BOP transaction-table availability and not a substitute for portfolio flow legs.
- A separate byte-preserving download attempt of the exact Bulletin PDF failed in the current runtime. This does not establish an origin-server HTTP status. No PDF bytes, response headers, content length or SHA-256 were captured.

## 3. Acceptance boundary
| Gate | Status |
|---|---|
| MNE fixed-cohort membership | PASS (reused) |
| Official Bulletin 9/2026 PDF and BoP section re-opened | PASS (document-reader text only) |
| Quarterly frequency / EUR reporting / BPM6 | PASS (methodology text) |
| Transaction-day and average FX conventions | PASS (methodology text; no conversion applied) |
| Provisional/revision warning | PASS |
| PDF Tables 5.1–5.4 label visible | PASS (label only) |
| Annotation target / direct table-export URL | NOT_EXPOSED |
| Table workbook/CSV raw bytes, headers, size, SHA-256 | NOT_CAPTURED |
| Q2-2026 portfolio asset transaction leg | NOT_CAPTURED |
| Q2-2026 portfolio liability transaction leg | NOT_CAPTURED |
| Separate-leg sign mapping and national/IMF comparison | NOT_DONE |
| Observation-specific revision/vintage bridge | UNKNOWN |
| MNE national validation | PARTIAL / NOT PASS |
| Aggregate admission | NOT_AUTHORIZED |

## 4. Duplicate prevention and next action
- Close the exact PDF text-reader route for further identical extraction attempts; it does not expose the annotation target.
- Do not repeat the failed byte-preserving download of the same Bulletin PDF, old C180 ZIP, or NSDP XML/Browse route.
- Reopen MNE only if a supported PDF-annotation/link extraction or browser download capability becomes available, or a distinct official CBCG table-export page/API provides the exact tables.
- Otherwise advance to another fixed-cohort member after a complete report-history/route-fingerprint preflight. Do not use Q2 IIP stocks, account-level totals or net values as transaction-leg substitutes.

## 5. Protected invariants
₹0; free official sources only; no synthetic values, invented timestamps, net-to-leg back-solving, stock-as-flow substitution, unsupported FX/sign/scale conversion, paid services or external contact. No IMF re-query/cohort rebuild. UNKNOWN is neither PASS nor FAIL. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2.0 remain unchanged. No production integration or merge.
