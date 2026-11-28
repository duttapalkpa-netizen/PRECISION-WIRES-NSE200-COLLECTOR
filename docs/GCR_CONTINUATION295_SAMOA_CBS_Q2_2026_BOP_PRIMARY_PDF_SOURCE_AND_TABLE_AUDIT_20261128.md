# GCR Continuation 295 — Samoa CBS Q2-2026 BOP primary PDF source and Table B-1 audit
Date: 28-Nov-2026 (Asia/Kolkata)
Scope: WSM / Samoa; immutable Q2-2026 63-country cohort; provenance and table-semantic audit only.

## 1. Mandatory continuity preflight
- Re-read current Master Continuity Ledger, GCR Master Priority Queue, Historical Task Registry, immutable 63-country matrix, C294, and Library Mother File `PRECISION_WIRES_V11_3_MOTHER_FILE_CONTINUATION_1_53_20261122.md`.
- Existing C262 dual-leg extraction was reused; no repeat IMF query, cohort rebuild, numeric recomputation, or status promotion.
- Current WSM matrix row retains DATA_CAPTURED; asset REVIEW; liability REVIEW; vintage UNKNOWN; FULL_PASS=NO. Matrix was not edited.

## 2. Official source and direct file
- Central Bank of Samoa official Quarterly Bulletin index: https://cbs.gov.ws/quarterly-bulletin
- Official index lists “Quarterly Bulletin September 2026” and was updated 19-Nov-2026.
- Direct official PDF: https://cbs.gov.ws/media/Quarterly-Bulletin---September-2026.pdf
- The official PDF is 64 pages in the browser-rendered document. Interior cover at PDF page index 2 identifies “September 2026, Vol. XLV No.3”; contents place Table B-1 Balance of Payments on printed page 34.
- **Document-control anomaly:** PDF page index 0 is a separate graphic cover labelled “June 2026”, while PDF page index 2 and the body identify September 2026 / Vol XLV No.3. Do not silently normalize this inconsistency. The bulletin identity is supported by the interior cover, contents, and Table B-1 body, but the stale June graphic should be disclosed in provenance notes.

## 3. Table B-1 independent field confirmation
Official PDF printed page 34 (browser PDF page index 38), Table B-1:
- Table unit: Tala million.
- Header provides quarterly columns through 2026-I and 2026-II.
- Q2-2026 / 2026-II Portfolio Investment (net): +9.3.
- Q2-2026 / 2026-II Portfolio Investment Assets: +9.5.
- Q2-2026 / 2026-II Portfolio Investment Liabilities: +0.2.
- Displayed-value identity: 9.5 − 0.2 = 9.3 (PASS at published one-decimal precision).
- Table footnote says it is based on the IMF Balance of Payments Manual, 6th Edition (BPM6).
- The separate IIP table is a stock table and is not substituted for these BOP transaction flows.
- This independently confirms the C262 values and corrects any ambiguity about the column period: the last two quarter columns are 2026-I and 2026-II.

## 4. Acceptance boundary
| Gate | Result |
|---|---|
| Official publisher and direct PDF URL | PASS |
| Interior publication identity / issue | PASS — September 2026, Vol XLV No.3 |
| Table B-1 Q2-2026 period and unit | PASS — 2026-II, Tala million |
| Separate portfolio A/L and net identity | PASS — 9.5 / 0.2 / 9.3 |
| BPM6 statement | PASS |
| PDF raw bytes / byte count / SHA-256 | NOT_CAPTURED — retrieval surface exposed PDF text/rendering but did not provide raw file bytes |
| Stale June graphic on first PDF page | DOCUMENT-CONTROL WARNING |
| FX conversion and IMF USD comparison | PENDING — do not convert using an unverified period rate or an IIP end-period stock rate |
| Observation-specific revision/vintage bridge | UNKNOWN |
| WSM VINTAGE_PASS / FULL_PASS | NO / NO |
| Aggregate admission | NOT_AUTHORIZED |

## 5. Exact next action and no-repeat boundary
- Preserve the official direct PDF URL and Table B-1 evidence; do not repeat the same PDF text extraction.
- Obtain the actual PDF bytes from the official URL through a supported raw-file capture route; compute byte count and SHA-256 and retain the exact file.
- For USD comparison, locate a documented CBS Q2 transaction-conversion convention or a suitable Q2 average exchange-rate series with exact dates/units. Do not use the key-indicator end-period exchange-rate figure as a substitute without an official conversion rule.
- Seek observation-specific CBS release/revision metadata and matching archived IMF vintage. If unavailable, retain UNKNOWN/PENDING.
- No IMF re-query, no matrix promotion, no net-to-leg inference, no IIP-stock substitution, no guessed FX conversion.

## 6. Invariants
₹0; official/free sources only; immutable 63-country cohort; CORE-672 (56×12), Engines A–E, Production Selector, RANKING_SCORE, +1 PRESSURE_FADE and IPO-PLX V2.0 unchanged. UNKNOWN is neither PASS nor FAIL.

**Task result:** official source locator, Q2 BOP table semantics, values, arithmetic and BPM6 basis independently verified. Raw PDF hash, USD conversion and synchronized vintage remain pending; no country gate promoted.
