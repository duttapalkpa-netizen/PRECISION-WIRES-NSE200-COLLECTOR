# GCR Ukraine (UKR) Q2-2026 — NBU official Q2 revision / vintage recheck
Date: 2026-11-26 (Asia/Kolkata)
Continuation: 258
Decision: NO NEW Q2-2026 PORTFOLIO OBSERVATION-SPECIFIC REVISION ID OR LATER NBU Q2 PORTFOLIO DUAL-LEG VINTAGE EVIDENCE WAS ESTABLISHED IN THIS BOUNDED RECHECK. UKR ASSET, LIABILITY AND SEMANTIC MAPPING GATES REMAIN PASS; VINTAGE PENDING; FULL_PASS NO; AGGREGATE NOT_AUTHORIZED.

## 1. Mandatory continuity preflight
- Re-fetched the current Master Continuity Ledger, GCR Master Priority Queue, Historical Task Registry and fixed 63-country national validation matrix.
- Re-read Library Mother File `PRECISION_WIRES_V11_3_MOTHER_FILE_CONTINUATION_1_53_20261122.md` and the controlling UKR C120/C134/C135/C257 record chain.
- Reused the accepted C134 numeric dual-leg extraction and C257 official methodology bridge. Did not repeat NBU IIP row extraction, IMF query, cohort rebuild, or production workflow.
- Current matrix UKR row already records: DATA_CAPTURED; source FOUND; data capture YES; asset PASS; liability PASS; vintage PENDING; full_pass NO; aggregate NOT_AUTHORIZED.

## 2. Official NBU Q2-2026 IIP publication — current document state
- Re-opened the official NBU Q2-2026 IIP PDF: https://roundtable.bank.gov.ua/files/ES/IIP_q.pdf
- The currently retrievable document explicitly identifies section 1.2 as IIP at end-Q2 2026 and states: "Date of last update: 23.09.2026".
- Its information note identifies revisions to direct investment and trade credits for 2022–2024 and currency/deposit assets for 2014–2025. It does not identify a Q2-2026 portfolio-investment transaction revision, observation-specific revision ID, or later Q2 vintage timestamp.
- This is a current retrieval of the same published file/document state, not evidence that the source data were never revised after 23-Sep-2026.

## 3. Official revision notice and release-channel check
- The previously recorded NBU "Changes in external sector statistics" notice remains the controlling revision-notice reference: https://roundtable.bank.gov.ua/admin_uploads/article/Changes_ES.pdf; the prior C257 read records its last update as 23-Sep-2026 and listed revisions through Q1-2026 only.
- A direct open of the notice in the present retrieval channel returned HTTP 403. The official NBU external-sector statistics page also returned HTTP 403. This is a retrieval-channel restriction, not proof that the NBU site or data are unavailable.
- Bounded official-domain web-index searches for a later Q2-2026 NBU portfolio revision, same-vintage identifier, or subsequent Q2-specific revision notice did not return a new eligible observation-level source.
- Therefore no new revision metadata or Q2-specific same-vintage bridge was captured. Do not infer "no revision" from the absence of a surfaced notice.

## 4. Revision-policy implication
- NBU methodology states that prior BOP periods may be revised quarterly and that IIP data can be revised within two years after first publication with comments about changes. These policies mean a 23-Sep publication date cannot itself establish that the Q2 values remained unchanged through the archived IMF 19-Nov snapshot.
- The methodology bridge from C257 remains valid: IIP transaction columns represent financial-account transactions and IIP financial-component rows correspond to BOP financial-account structure.
- Existing C134 Q2 legs remain +USD159m assets and +USD34m liabilities, with exact archived IMF numeric comparisons at NBU whole-million display precision. No new numeric calculation was needed or performed.

## 5. Acceptance decision
| Gate | Result |
|---|---|
| Q2 period / portfolio A-L source rows | PASS (C134 reused) |
| Asset numeric comparison | PASS (C134 reused) |
| Liability numeric comparison | PASS (C134 reused) |
| IIP transaction ↔ BOP financial-account semantic bridge | PASS (C257 reused) |
| Current published Q2 IIP document last-update metadata | 23-Sep-2026 |
| Q2-specific later revision/version identifier | NOT_CAPTURED |
| NBU ↔ archived IMF same-vintage identity | PENDING / NOT_ESTABLISHED |
| UKR full national validation | PARTIAL / NOT PASS |
| Aggregate admission | NOT_AUTHORIZED |

## 6. Exact next action
- Keep UKR's numeric and semantic PASS gates; keep vintage PENDING and full_pass NO.
- Reopen only when a distinct official NBU Q2-specific revision notice, versioned Q2 observation extract, or later official IIP/BOP release explicitly identifies Q2 portfolio A/L revisions and provides an observation-specific date/version that can be compared to the archived IMF receipt.
- The next scheduled Q3 IIP publication window may provide a revision trigger; per NBU methodology, IIP is normally published 85–90 days after quarter-end. Do not assume Q3 publication or a calendar date before it is actually available.
- Do not retry the stale BOP PDF, repeat the Q2 IIP extraction, re-query IMF, rebuild the cohort, or promote the matrix gate without new evidence.

## 7. Protected invariants
₹0; free official sources only; no synthetic data, inferred revision, guessed timestamp, stock-as-flow, net-to-leg inference, unsupported conversion, IMF re-query, cohort rebuild or production change. UNKNOWN is neither PASS nor FAIL. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2.0 unchanged. No workflow dispatch, merge or production integration.
