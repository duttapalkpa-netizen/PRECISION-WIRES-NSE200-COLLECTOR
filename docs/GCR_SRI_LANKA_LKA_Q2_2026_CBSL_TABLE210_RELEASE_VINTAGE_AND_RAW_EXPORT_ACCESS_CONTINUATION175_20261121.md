# Sri Lanka LKA Q2-2026 — CBSL Table 2.10 release-vintage and raw-export access gate (Continuation 175)
Date: 2026-11-21 (Asia/Kolkata)
Decision: OFFICIAL CBSL EXTERNAL-SECTOR LANDING PAGE CONFIRMS BPM6 QUARTERLY BOP TABLE 2012Q1–LATEST; EXACT VERSIONED TABLE 2.10 XLSX URL, filename date and Last-Modified are independently located in a secondary source catalogue; official CBSL landing page and direct XLSX return HTTP 403 in this session; workbook bytes and hash NOT_CAPTURED; third-party-reported SHA-256 NOT_INDEPENDENTLY_VERIFIED; 30-Sep-2026 file release marker is temporally compatible with Q2-2026 values but cannot be treated as the same vintage as 12-Nov-2026 Treasury report; same-vintage bridge NOT_ESTABLISHED; LKA remains STRONG DUAL-LEG RECONCILIATION / PROVISIONAL, NOT FINAL PASS; aggregate NOT_AUTHORIZED.

## 1. Continuity preflight and duplicate prevention
- Re-fetched Master Continuity Ledger (blob SHA `2996c660b650ae12657a26224fe939bfcb1be637`), GCR Master Priority Queue (`d1513271dc66e3a268c7a458bf5f65c5dc751419`), Historical Task Registry (`89e7b0f86828ce10d0a1e99c104a146e0a823a97`), Continuation 174 (`36363f9a1e85cc1922ee96005f5f310b1bb6c67f`) and immutable cohort (`31f5bfe5adb59f4c1a139b6d8c54b5ad9fb672c8`).
- Reused fixed LKA cohort row; no cohort rebuild, no IMF re-query, no repeat Treasury Table 7 extraction.
- Continuation 174 remains valid for separate provisional Q2 national legs: assets +26 USD mn; liabilities -351 USD mn. Both legs independently match archived IMF values at national whole-million precision. The present task targets the unresolved primary CBSL export and release-vintage bridge only.

## 2. Official CBSL landing page evidence
- Official CBSL External Sector page: https://www.cbsl.gov.lk/en/statistics/statistical-tables/external-sector
- Search-indexed official page describes “Balance of Payments (BPM6 Basis) - Quarterly (2012 1Q to Latest)”.
- Direct page open in this session returned HTTP 403 Forbidden; the indexed official page still grounds existence, BPM6 basis, quarterly frequency and coverage description. It does not expose the XLSX download bytes in this session.

## 3. Exact versioned workbook locator — provenance carefully bounded
- A secondary research source catalogue identifies the CBSL Table 2.10 workbook as:
  https://www.cbsl.gov.lk/sites/default/files/cbslweb_documents/statistics/sheets/table2.10_20260930_e.xlsx
- Filename/version marker: `table2.10_20260930_e.xlsx`.
- Reported HTTP Last-Modified: Wed, 30 Sep 2026 15:06:48 GMT.
- Reported SHA-256: `2d6e3ebd5c4305028a3693d9e1c25a0c64c606616f0b24cf334695e1ad3d62f6`.
- The same catalogue describes Table 2.10, sheet “BPM6-Financial AC - Quarterly”, as quarterly BPM6 financial-account data, with one pair of columns per quarter (net incurrence of liabilities and net acquisition of financial assets), through 2026-Q2.
- These are third-party reported metadata/fingerprint values, NOT a locally downloaded or independently verified CBSL artifact. They must not be written into our raw archive manifest as verified file bytes/hash.

## 4. Retrieval attempts and access outcome
- Web open of exact official XLSX URL: HTTP 403 Forbidden.
- Container download attempt of exact same official XLSX URL: failed; no file created.
- Official landing page open: HTTP 403 Forbidden.
- No alternate mirror was used because no authorized mirror with a verifiable exact copy was identified.
- Bytes, content length, MIME header, workbook sheets, Q2 numeric cells, embedded metadata and SHA-256 NOT_CAPTURED / NOT_VERIFIED. No hash computed.

## 5. Official revision policy and vintage interpretation
- CBSL-authored article “A Key Milestone in External Sector Statistics: Current Account Statistics on a Monthly Basis” states complete BOP including financial-account data is generally published quarterly with a three-month lag; CBSL follows BPM6 (article lines 6, 56–62).
- The article says monthly current-account statistics are provisional; current revision policy revises monthly statistics with each regular quarterly BOP publication, and a full revision of two consecutive years occurs with each annual publication (lines 186–190).
- This supports that vintage/revision control matters and that Q2 data may be revised. It does NOT disclose the exact revision date or vintage identifier for the Q2 portfolio legs in the Treasury report.
- Treasury report is issued 12-Nov-2026 (Continuation 174 evidence); workbook filename date and reported Last-Modified are 30-Sep-2026. They are distinct date markers. No proof that the Treasury Table 7 values and this September workbook represent the same revision snapshot. Exact same-vintage bridge remains NOT_ESTABLISHED.
- Do not assume the Treasury report is a later correction or the September XLSX the definitive vintage without inspecting the workbook and release metadata.

## 6. Status matrix
| Gate | Status |
|---|---|
| Fixed cohort membership / prior work reuse | PASS |
| Official CBSL external-sector page identifies BPM6 quarterly BOP | PASS (indexed official page; direct page 403) |
| Exact versioned Table 2.10 XLSX locator | LOCATED (secondary catalogue corroboration) |
| XLSX bytes / content headers / workbook inspection | NOT_CAPTURED |
| Reported XLSX SHA-256 | UNVERIFIED (third-party claim only) |
| Official CBSL revision policy located | PASS (CBSL-authored article) |
| Exact Q2 portfolio revision vintage bridge | NOT_ESTABLISHED |
| National Q2 dual-leg numeric agreement | PASS at published rounding (Continuation 174) |
| LKA final same-vintage validation | NOT_PASS / PENDING |
| Aggregate authorization | NOT_AUTHORIZED |

## 7. Rejected list
- Do not retry identical 403 CBSL landing page or XLSX fetch through the same web/container paths unless a genuinely different access route becomes available.
- Do not treat the third-party SHA-256 as verified archive hash.
- Do not treat 30-Sep-2026 file marker and 12-Nov-2026 Treasury issue date as same-vintage evidence.
- Do not use Macro Lab values as primary evidence; its metadata only helped locate CBSL's file.
- No IIP stock, net-only, annual/H1 substitution, net-to-leg back-solving, synthetic data or revision assumptions.

## 8. Next exact action
1. Obtain the official Table 2.10 XLSX via a genuinely distinct, supported byte-transfer route or an official SDDS/National Summary Data Page download that resolves to the same versioned CBSL file.
2. Verify bytes against reported SHA-256 `2d6e3ebd...` (full value above), record response headers, byte count, sheets, cell coordinates and Q2 values for both legs.
3. Find the exact CBSL BOP release/vintage identifier and determine whether the 30-Sep-2026 workbook was superseded before the 12-Nov-2026 Treasury report.
4. If no new route is available, close this retrieval attempt as PARTIAL and advance to the next fixed-cohort country only after preflight; do not repeat this same failed route.
5. Aggregate remains NOT_AUTHORIZED until cohort acceptance gates pass.

## 9. Protected invariants
No production code/configuration, Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E, IPO-PLX V2, weights, gates or alerts changed. No IMF re-query, cohort rebuild, paid API, synthetic data, fabricated timestamp, unsupported sign/scale/FX conversion, stock-as-flow substitution or acceptance relaxation. Research spend ₹0. UNKNOWN is never PASS.
