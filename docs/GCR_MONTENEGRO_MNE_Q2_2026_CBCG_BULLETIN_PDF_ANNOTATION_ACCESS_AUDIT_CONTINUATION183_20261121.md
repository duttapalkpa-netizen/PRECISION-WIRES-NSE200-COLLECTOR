# Montenegro (MNE) Q2-2026 — CBCG Bulletin 9/2026 PDF annotation and table-export access audit (Continuation 183)
Date: 2026-11-21 (Asia/Kolkata)

Decision: OFFICIAL BULLETIN PDF RE-OPENED AND CONTENT VERIFIED; TABLES 5.1–5.4 EXPORT ANNOTATION DESTINATION NOT EXPOSED BY AVAILABLE PDF TEXT/LINK EXTRACTION; NO TABLE PAYLOAD BYTES OR Q2 PORTFOLIO LEGS CAPTURED; MNE REMAINS PARTIAL / NOT PASS; AGGREGATE NOT_AUTHORIZED.

## 1. Continuity preflight
- Repository: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR (main).
- Reused Continuation 182 report: `docs/GCR_MONTENEGRO_MNE_Q2_2026_CBCG_BULLETIN_9_2026_TABLE_EXPORT_LOCATOR_CONTINUATION182_20261121.md`.
- Reused fixed 63-country cohort row and SHA-256 from C182: `MNE,Montenegro,2026-Q2,A_NFA_T_PRESENT,L_NIL_T_PRESENT,BOTH_LEGS_PRESENT_IN_IMF_PANEL,NATIONAL_SOURCE_VINTAGE_VALIDATION_PENDING,NOT_AUTHORIZED`; cohort SHA-256 `31f5bfe5adb59f4c1a139b6d8c54b5ad9fb672c8`.
- No cohort rebuild, IMF re-query, panel edit, or repeated C180 ZIP/XML/Browse retrieval.

## 2. New bounded verification performed
- Re-opened the official CBCG Bulletin archive and followed its 9/2026 publication link to the official 65-page PDF:
  https://cbcg.me/slike_i_fajlovi/fajlovi/fajlovi_publikacije/biltencbcg/2026/bilten_9-2026.pdf
- PDF text confirms the BOP section starts on printed page 55 / PDF page 54 and displays “Tables 5.1 - 5.4 - download tables”.
- PDF also confirms the bulletin's published data are preliminary and may be revised; BOP is quarterly and reported in EUR; CBCG uses transaction-day middle rates and monthly/annual average rates and period-end daily rates for relevant valuation differences.
- Methodology text says direct and portfolio investments are monitored using ITRS data and surveys.
- The available PDF extraction exposes the text of the download affordance but does not expose a numbered hyperlink destination or downloadable table URL. An attempted direct PDF byte download in this environment failed. Search for a separately indexed 2026 Tables 5.1–5.4 workbook/CSV did not surface a verifiable official payload.
- This is an access/tool boundary, not evidence that the CBCG tables do not exist. No guessed URL, fabricated timestamp, MIME type, bytes, or hash is recorded.

## 3. Acceptance matrix
| Gate | Status |
|---|---|
| C182 report / fixed cohort / duplicate-prevention context reused | PASS |
| Official CBCG Bulletin archive page and 9/2026 PDF reopened | PASS |
| BOP section and Tables 5.1–5.4 download affordance confirmed | PASS |
| Quarterly EUR reporting and FX methodology re-confirmed | PASS |
| Preliminary/revision caveat re-confirmed | PASS |
| Exact PDF annotation target / table-export URL | BLOCKED / NOT_EXPOSED |
| Official workbook/CSV bytes, MIME, retrieval timestamp, SHA-256 | NOT_CAPTURED |
| Q2-2026 portfolio asset transaction row | NOT_CAPTURED |
| Q2-2026 portfolio liability transaction row | NOT_CAPTURED |
| Row labels/sign convention and IMF-national comparison | NOT_DONE |
| MNE national validation | PARTIAL / NOT PASS |
| Aggregate admission | NOT_AUTHORIZED |

## 4. Rejected / do-not-repeat
- Do not retry the C180 CBCG ZIP, NSDP SDMX XML, or legacy Browse endpoints through the same retrieval method.
- Do not infer numeric values from the PDF's “download tables” text.
- Do not substitute old 2015/2016 CBCG PDF tables, IIP positions, external debt, net-only financial-account totals, or IMF-only rows for Q2-2026 national dual-leg evidence.
- Do not infer zero from omission or back-solve separate legs from a net figure.

## 5. Next action / handoff
- The C182 PDF-affordance route is now fingerprinted as NOT_EXPOSED by the currently available PDF extraction path. Reopen only if a genuinely different supported PDF-annotation or official export-download capability becomes available, or CBCG publishes a distinct official workbook/CSV/API locator.
- Do not spend further time repeating the same search or PDF text extraction. Continue the master rank-1 63-country validation work by selecting the next eligible country only after checking its complete history and the current queue/registry; reuse the fixed cohort and archived IMF exact-key receipt.
- Preserve MNE as PARTIAL / NOT PASS and the aggregate as NOT_AUTHORIZED until national dual-leg, sign/unit, and vintage gates pass.

## 6. Protected invariants
₹0; free official sources only. No synthetic data, fabricated timestamps, unauthorized access, IMF re-query, cohort rebuild, net-to-leg back-solving, stock-as-flow substitution, or unsupported sign/FX conversion. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 remain unchanged. UNKNOWN is never PASS.
