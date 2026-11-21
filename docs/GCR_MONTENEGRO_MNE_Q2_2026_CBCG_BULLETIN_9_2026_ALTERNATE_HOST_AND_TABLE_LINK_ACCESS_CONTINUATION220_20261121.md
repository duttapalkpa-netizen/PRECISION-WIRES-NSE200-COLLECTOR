# Montenegro (MNE) Q2-2026 — CBCG Bulletin 9/2026 alternate-host PDF and table-link access boundary
Date: 2026-11-21 (Asia/Kolkata)
Continuation: 220 / Research Verification 53
Status: DISTINCT OFFICIAL WWW-HOST PDF ROUTE NOW RENDERS THE 65-PAGE BULLETIN; Q2 TABLE DOWNLOAD LINK IS VISUALLY PRESENT BUT ITS TARGET URL/ANNOTATION AND TABLE BYTES REMAIN UNRESOLVED. MNE PARTIAL / NOT PASS.

## 1. Mandatory continuity preflight and queue selection
- Re-fetched current Master Continuity Ledger, GCR Master Priority Queue and Historical Task Registry.
- Reopened CHN SAFE detailed BOP audit, COL BanRep route audit C136/C151/C152/C162, POL NBP C163–C165 and TUR C166 handoff. CHN's known English/Chinese XLSX routes remain blocked; COL's catalogue/desktop export is blocked and its SDMX guide excludes BOP; POL national PLN legs are captured but no valid aggregate USD bridge exists; TUR ZIP route remains closed. These items were not repeated.
- Reopened MNE Continuation 182, which identified CBCG Bulletin 9/2026 and the Tables 5.1–5.4 download affordance but did not capture its target URL or table bytes.
- Selected MNE's distinct official bulletin PDF host route because the existing exact `cbcg.me` PDF locator was inaccessible through the current web reader and the official archive exposed a direct bulletin link.

## 2. New access result — official alternate host
- Official CBCG bulletin archive: https://cbcg.me/en/publications/regular-publications/cbcg-bulletin ; its 9/2026 entry links to the official bulletin PDF.
- The same exact PDF path under the official `www.cbcg.me` host now renders successfully through the PDF reader: https://www.cbcg.me/slike_i_fajlovi/fajlovi/fajlovi_publikacije/biltencbcg/2026/bilten_9-2026.pdf
- The PDF reader identifies a 65-page Bulletin 9/2026. The English BOP section is printed page 55 / PDF page index 54; the preceding page shows the visual hyperlink text “Tables 5.1–5.4 — download tables”.
- The alternate hostname is a distinct successful document-rendering route. It does not itself provide a new BOP dataset or a raw PDF file. A separate direct byte download of this PDF through the current container transfer route failed; no PDF byte count, response headers or SHA-256 were captured.

## 3. Link-resolution boundary
- The visual “download tables” text is confirmed on the rendered PDF page. The PDF text extraction does not expose a numbered link target or destination URL, and the PDF bytes could not be downloaded for local annotation inspection.
- No table-export URL, XLSX/CSV MIME, workbook bytes, table sheets, exact Q2-2026 portfolio asset/liability values, response headers, retrieval timestamp or SHA-256 were obtained.
- Do not invent a URL from the hyperlink label, infer a CBCG file path, or treat the PDF page render as the data export.
- Existing C182 methodology remains valid: CBCG reports quarterly BOP in EUR; the bulletin states transaction-day CBCG middle exchange rates for source-currency conversion and flags preliminary/revisable data. These facts do not provide the missing portfolio rows.

## 4. Acceptance matrix
| Gate | Status |
|---|---|
| Fixed MNE Q2-2026 cohort membership | PASS (reused from C182) |
| Official CBCG Bulletin 9/2026 archive link | PASS |
| Alternate `www.cbcg.me` PDF rendering route | PASS |
| PDF content / 65-page identity | PASS |
| Visual Tables 5.1–5.4 download affordance | PASS — visible locator only |
| Raw PDF bytes / SHA-256 | NOT_CAPTURED |
| Hyperlink annotation destination / export URL | NOT_RESOLVED |
| Tables 5.1–5.4 workbook/CSV bytes | NOT_CAPTURED |
| Q2 portfolio asset and liability observations | NOT_CAPTURED |
| MNE sign / vintage bridge and IMF comparison | NOT_DONE |
| MNE national validation | PARTIAL / NOT PASS |
| 63-country aggregate | NOT_AUTHORIZED |

## 5. Decision and next action
- The alternate official host solved only the PDF-rendering route. It did not solve the table payload. Close this exact PDF-rendering test; do not repeat it as though it were a new data route.
- Reopen MNE only if the exact PDF bytes become available for annotation inspection, a CBCG table export URL is directly exposed, or a distinct official CSV/XLSX endpoint is discovered.
- Next executable candidate: MNG Mongolia NSO PxWeb BOP table. Its official page is currently accessible and documents a public JSON/XML API in NSO terms of use; the prior C179 API attempt failed at the retrieval bridge. Test only a genuinely supported API route if its exact endpoint and request method can be established from official NSO documentation; otherwise preserve BLOCKED and move on. Do not guess indicator codes or request bodies.

## 6. Protected invariants
₹0; free official sources only. No IMF re-query, cohort rebuild, synthetic values, fabricated timestamps, inferred series IDs, guessed export URLs, stock-as-flow, net-to-leg back-solving, unsupported sign/scale/FX conversion, tolerance widening or aggregate promotion. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS.

## 7. Official source references
- CBCG Bulletin archive: https://cbcg.me/en/publications/regular-publications/cbcg-bulletin
- CBCG Bulletin 9/2026 PDF, alternate official host: https://www.cbcg.me/slike_i_fajlovi/fajlovi/fajlovi_publikacije/biltencbcg/2026/bilten_9-2026.pdf
- Controlling prior report: docs/GCR_MONTENEGRO_MNE_Q2_2026_CBCG_BULLETIN_9_2026_TABLE_EXPORT_LOCATOR_CONTINUATION182_20261121.md
- NSO public API terms (next candidate): https://www.nso.mn/en/terms_of_use