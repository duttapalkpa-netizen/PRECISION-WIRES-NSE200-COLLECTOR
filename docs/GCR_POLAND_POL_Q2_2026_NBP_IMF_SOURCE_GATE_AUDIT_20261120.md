# Poland POL Q2-2026 official BOP source-gate audit — 2026-11-20

Status: **BLOCKED / NOT_DONE**. Existing IMF observations are available, but the official NBP national-source Q2 vintage and comparable quarterly component rows could not be established to the required standard. No country validation PASS is claimed.

## Continuity preflight
- Prior to selection, re-fetched Master Continuity Ledger, GCR Priority Queue, SAU reconciliation/vintage reports and CHN access audit.
- SAU numerical work and prior country PASS items were excluded. POL was selected from the existing 12-country IMF exact-key sample; no new IMF request and no cohort rebuild.
- Reused existing IMF receipt: run 44474458684 / artifact 14505009889 / ZIP SHA-256 588101c0deff3b4310984dae5eabcac64fc8288f4416854b7676b4b6ff6b4cd7.

## Existing IMF exact-key evidence
- POL A_NFA_T raw CSV SHA-256: 19ba3d8918245d7abe73125d76c08e27f9970817cc1a46b8753763352e5a2e21; 4,891 bytes.
- POL L_NIL_T raw CSV SHA-256: 365bac8801d0951f3d69f863628e844c6da07b0e69651880614c815b859c769b; 4,726 bytes.
- Existing exact receipt includes both legs through 2026-Q2. Q2-2026 values (USD, SCALE=6): A_NFA_T +6,602,000,000; L_NIL_T +19,391,000,000. Display in USDm: +6,602 and +19,391.
- These are IMF-side values only; they are not a national-source validation.

## Official NBP source path and limitation
- NBP official quarterly BOP analytical release PDF: https://static.nbp.pl/dane/bilans-platniczy/bopa_en.pdf
- The PDF's narrative front matter says “Balance of payments in Poland in March 2026”, dated 15 May 2026, and says April 2026 data will be published on 12 June 2026. It links official quarterly time-series workbooks:
  - https://static.nbp.pl/dane/bilans-platniczy/bop_q.xlsx
  - https://static.nbp.pl/dane/bilans-platniczy/bop_q_pln.xlsx
- The same PDF's later tables show columns headed 2025 III, 2026 II*, 2026 III* and include Q2/Q3 2026 values. The mismatch between the front-matter vintage/date and later table period headings prevents treating this PDF as a clean, self-consistent Q2-2026 release without the underlying workbook and its metadata.
- The official XLSX URL was attempted through the available browser and direct file retrieval paths; browser rejected the XLSX MIME type and direct retrieval failed. Workbook bytes, sheets, revision timestamp, exact row labels and hash remain NOT_INSPECTED / NOT_DONE.
- Therefore any values read from the later PDF table are quarantined as candidate-only and are not used in the comparison or status decision. Do not infer the PDF's effective release vintage from its table heading alone.

## Decision matrix
- Existing IMF exact receipt / raw hashes: PASS (reuse only).
- NBP official quarterly workbook locator: PASS.
- NBP workbook bytes / metadata / hash: BLOCKED / NOT_DONE.
- NBP Q2-2026 same-vintage source rows: NOT_ESTABLISHED.
- POL national asset comparison: NOT_DONE.
- POL national liability comparison: NOT_DONE.
- POL full dual-leg validation: BLOCKED / NOT_DONE.
- 63-country aggregate: NOT_AUTHORIZED.

## Next exact action
Retrieve the exact official NBP workbook bytes using a supported file-transfer route; record HTTP status, retrieval timestamp, content length, response headers and SHA-256; inspect sheets/labels/units/revision date; identify Q2 2026 portfolio assets and liabilities; then compare with the existing IMF raw receipt. If workbook access remains unavailable, preserve POL as BLOCKED and advance to the next eligible country using the fixed cohort. No new IMF query or cohort rebuild.

## Protected invariants
No aggregation, netting, imputation, forward-fill, synthetic data, silent sign transform or production integration. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 remain unchanged. UNKNOWN is never PASS.
