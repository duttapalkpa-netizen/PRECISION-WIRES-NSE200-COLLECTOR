# Guinea (GIN) Q2-2026 — BCRG MPC download-affordance and link-target access gate (Continuation 189)
Date: 2026-11-21 (Asia/Kolkata)
Decision: THE OFFICIAL BCRG 22ND MONETARY POLICY COMMITTEE PAGE IS DIRECTLY ACCESSIBLE AND SHOWS A “Télécharger” DOWNLOAD AFFORDANCE, BUT THE PAGE'S EXTRACTED LINK INVENTORY DOES NOT EXPOSE A FILE LINK TARGET OR DOCUMENT URL. NO NEW DOWNLOAD LOCATOR, PDF/XLSX BYTES, Q2 PORTFOLIO LEGS OR HASH CAPTURED. THIS IS A CONFIRMED LINK-TARGET DISCOVERY BOUNDARY, NOT EVIDENCE THAT DATA ARE ABSENT. GIN REMAINS PARTIAL / NOT PASS; AGGREGATE NOT_AUTHORIZED.

## 1. Continuity preflight and selection
- Re-fetched current Master Continuity Ledger, GCR Master Priority Queue, Historical Task Registry, C188 LKA report, GIN C170 report and immutable 63-country cohort before selecting next task.
- LKA C175–C177 routes are closed for repetition; C188 found page-freshness metadata only and explicitly directed progression to next eligible cohort member.
- GIN C170 identifies the exact open dependency: resolve the official 22nd MPC page “Télécharger” target or a distinct BCRG official BOP export locator. No IMF re-query, cohort rebuild or repeated static BOP page extraction.
- Reused exact GIN cohort row: both IMF Q2 legs present; national source vintage validation pending; aggregate NOT_AUTHORIZED. Cohort blob SHA remains `31f5bfe5adb59f4c1a139b6d8c54b5ad9fb672c8`.

## 2. Direct official BCRG page inspection
- Official page opened successfully: https://www.bcrg-guinee.org/22eme-reunion-ordinaire-du-comite-de-politique-monetaire-de-la-republique-de-guinee/
- Page title: “22ème REUNION ORDINAIRE DU COMITE DE POLITIQUE MONETAIRE DE LA REPUBLIQUE DE GUINEE”.
- The rendered page visibly contains the label “Télécharger” (download) at line 140 in the extracted page content.
- The page's numbered link inventory does not expose a corresponding file link target or URL. The only nearby numbered links are author/profile and image/navigation links; none is a document locator.
- Therefore no attachment URL was inferred or fabricated. No PDF/XLSX bytes, MIME, response headers, byte count, timestamp for an attachment, document title, or SHA-256 was captured.

## 3. Scope boundary
- This verifies the official page and its download affordance only. It does not establish that the attachment is absent, nor that the underlying Q2-2026 BOP dataset lacks portfolio asset/liability legs.
- C170's prior BCRG historical reporting sample showed portfolio investment as a net category; that historical sample is not used as Q2-2026 data and does not prove the current 2026 dataset has no separate legs.
- The official BCRG Balance des paiements statistics page remains a locator only unless a distinct machine-readable export/API is surfaced. Do not repeat the same static page inspection without a new link target or data payload.

## 4. Acceptance matrix
| Gate | Status |
|---|---|
| Master Ledger / Priority Queue / Registry / C170 / C188 preflight | PASS |
| Fixed GIN cohort membership | PASS (reused) |
| Official 22nd MPC page opened | PASS |
| “Télécharger” affordance confirmed | PASS |
| Actual attachment href / document URL | NOT_EXPOSED |
| Official attachment bytes / metadata / SHA-256 | NOT_CAPTURED |
| Q2-2026 portfolio assets and liabilities | NOT_CAPTURED |
| Sign, unit, classification and revision vintage | NOT_ESTABLISHED |
| GIN full national dual-leg validation | PARTIAL / NOT PASS |
| Aggregate authorization | NOT_AUTHORIZED |

## 5. Rejected list and next exact action
- Rejected: guessing the download URL from the page label, using historical net-only values as current Q2 dual legs, treating no extracted href as proof of data absence, or back-solving from net totals.
- Next: reopen GIN only if a distinct BCRG official file/API locator or an actual attachment target becomes available through a supported retrieval surface. Otherwise retain PARTIAL and advance to the next eligible cohort item after full preflight. Do not repeat the same page extraction or static BOP page route.
- No IMF re-query, no cohort rebuild, no synthetic data, no paid APIs, no fabricated timestamps. ₹0; official/free sources only. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN never PASS.
