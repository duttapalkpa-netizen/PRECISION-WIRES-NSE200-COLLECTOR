# GCR CHN China Q2-2026 — SAFE post-publication Q3 revision and sign/vintage recheck
Continuation: 264
Date: 2026-11-26 (Asia/Kolkata)
Scope: bounded official-source recheck of the already captured Q2-2026 portfolio-investment asset/liability rows. No IMF query, cohort rebuild, code change, workflow dispatch or production integration.

## Preflight and duplicate prevention
- Re-read the current Master Continuity Ledger, GCR priority queue, historical task registry, 63-country fixed-cohort matrix and Library Mother File 1–53.
- GitHub already uses Continuation 263 for Serbia (SRB); this China recheck is therefore Continuation 264. A misnumbered draft was removed before the durable C264 record was created.
- Reused C247's archived IMF exact-key rows and SAFE 29-Sep-2026 Q2 release; did not repeat numeric extraction or IMF retrieval.
- Skipped completed national legs and PASS checks. CHN's asset sign remains REVIEW; liability PASS retained as previously recorded; vintage PENDING; FULL_PASS=NO; aggregate admission NOT_AUTHORIZED.

## New official evidence checked
1. SAFE's official 13-Nov-2026 Q3 preliminary BOP release was inspected (https://www.safe.gov.cn/en/2026/1113/2466.html). It publishes Q3 and first-three-quarters aggregates. Its detailed financial-account section is labelled as including net errors and omissions for the quarter / first three quarters; it does not expose a distinct revised Q2 portfolio-investment asset/liability pair in the inspected release. Therefore no Q2 revision bridge can be inferred by subtracting aggregates or back-solving.
2. SAFE's official 29-Sep-2026 Q2 release (index 000014453-2026-0068; https://www.safe.gov.cn/en/2026/0929/2458.html) remains the directly inspected Q2 table. It identifies BPM6; states credit is positive and debit negative and that balance values are the sum of credit and debit; and notes rounded-off numbers and regular revision.
3. Q2 portfolio row (USD 100 million units): assets -488; liabilities +433; net -55. In USD million scale this is approximately assets -48,800; liabilities +43,300; net -5,500. These are rounded release values.
4. Archived IMF exact-sample Q2 values retained from C247: assets +48,794.459 USD million; liabilities +43,286.601 USD million. The liability rounded comparison is close; the asset magnitudes are close but signs are opposite. No sign inversion is promoted solely from numerical similarity.
5. SAFE's official Q3 release does not independently establish that the 29-Sep Q2 values were revised or unchanged; no Q2 observation-specific revision ID, vintage timestamp, detailed XLSX bytes/schema/hash or unrounded Q2 portfolio legs were recovered in this bounded recheck.

## Acceptance
- Official Q3 release discovery and bounded review: PASS (scope only).
- Q2 portfolio A/L capture: retained from C247; no new raw capture.
- Liability numeric comparison: prior PASS retained, subject to existing vintage limitation.
- Asset sign crosswalk: REVIEW / NOT ESTABLISHED.
- Same-vintage/revision bridge: PENDING / UNKNOWN.
- Detailed official XLSX, unrounded values and raw-byte hash: NOT_CAPTURED.
- CHN overall: DATA_CAPTURED / PARTIAL / NOT PASS; FULL_PASS=NO; aggregate NOT_AUTHORIZED.

## Exact reopen condition
Reopen only if a distinct supported official SAFE XLSX/API route yields unrounded Q2 portfolio A/L observations with explicit asset sign definitions and observation-specific revision/vintage metadata, plus raw bytes and SHA-256. Do not repeat the 29-Sep Q2 page, the 13-Nov Q3 page, failed XLSX route, or IMF query.

## Invariants
₹0 spend; official/free sources only; fixed 63-country cohort unchanged; no IMF re-query; no annual/H1/net/IIP stock substitution; UNKNOWN is neither PASS nor FAIL; no synthetic data, guessed conversions, fabricated hashes/timestamps, or proxy promotion. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2.0 remain unchanged. No workflow dispatch, merge or production integration.
