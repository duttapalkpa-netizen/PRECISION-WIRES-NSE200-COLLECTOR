# GCR South Africa — SARB portfolio series-code candidates and archive retrieval boundary
Date: 2026-11-19
Continuation: 41, Part-4
Scope: identify candidate national portfolio asset/liability series codes for ZAF Q2-2026 and document the official archive retrieval boundary. This is a lead-generation/source gate, not national-source validation.

## Progress log
- Reused Part-3 official source gate and 63-country cohort; no repeat cohort derivation.
- Opened SARB's official XLSX archive index. It confirms Quarterly Bulletin No. 321 (September 2026), K1 = quarterly, and names the exact archive: 04Kbp5-Balance-of-Payments-September-2026-updated.zip.
- Followed the archive attachment link. The official site resolved the exact ZIP URL, but retrieval timed out at the web fetch layer; a direct download attempt also failed. No ZIP bytes were obtained, so no archive hash or workbook inspection is claimed.
- Found a non-SARB secondary BER Data Guide that lists plausible SARB KBP codes:
  * KBP5756 — portfolio investment, net incurrence of liabilities, equity and investment fund shares
  * KBP5757 — portfolio investment, net incurrence of liabilities, debt securities
  * KBP5758 — portfolio investment, net acquisition of financial assets, equity and investment fund shares
  * KBP5759 — portfolio investment, net acquisition of financial assets, debt securities
  It also lists KBP5644 (total portfolio investment liabilities, K1/J1) and KBP5660 (total portfolio investment assets, K1/J1).
- These code descriptions are secondary-source discovery leads only. They have NOT been independently verified against SARB's official time-series description or the September 2026 workbook. Do not ingest them as validated national mappings.

## Evidence
1. SARB official XLSX archive index, published 2026-09-29:
   https://www.resbank.co.za/en/home/publications/publication-detail-pages/quarterly-bulletins/download-information-from-xlsx-data-files/2026/-download-information-from-xlsx-data-files
   - Official page identifies Bulletin No. 321, K1 quarterly frequency, and archive 04Kbp5-Balance-of-Payments-September-2026-updated.zip.
   - Exact attachment URL resolved by the page:
     https://www.resbank.co.za/content/dam/sarb/publications/quarterly-bulletins/download-information-from-xlsx-data-files/2026/september/04Kbp5%20Balance%20of%20Payments%20September%202026%20updated.zip
   - Retrieval attempts timed out/failed; archive bytes unavailable in this run.
2. SARB official online statistical query page:
   https://www.resbank.co.za/en/home/what-we-do/statistics/releases/online-statistical-query
   - Describes a public query workflow accepting KBP series codes, offering version selection, frequency, date range and export. This is the official path to verify candidate codes/versions.
3. Secondary discovery lead (not an authority for final validation):
   https://dataguide.beranalytics.co.za/datasets/sarb/chapters/quarterly/balance_of_payments.html
   - Lists KBP5756–KBP5759 with the above portfolio liability/asset descriptions and K1/J1 frequencies; lists KBP5644 and KBP5660 totals.

## Gate assessment
- Official SARB archive identification: PASS.
- Official archive byte retrieval / workbook inspection: BLOCKED (retrieval failure; no bytes).
- Candidate codes discovered: PARTIAL (secondary-source lead only).
- Official code description/version/unit/sign verification: NOT_DONE.
- Exact Q2-2026 gross portfolio asset/liability comparison against IMF A_NFA_T/L_NIL_T: NOT_DONE.
- ZAF national-source validation: PARTIAL / NOT PASS.
- GCR 63-country aggregate admission: NOT_AUTHORIZED.

## Exact next action
Use the SARB official online statistical query with KBP5756, KBP5757, KBP5758, KBP5759; inspect each returned official description, available version, unit, quarterly frequency and Q2-2026 observation. Also inspect KBP5644/KBP5660 totals as reconciliation controls, not replacements for instrument-level components. Capture the official export bytes and SHA-256, then compare the two liability components and two asset components to IMF panel definitions, only after establishing sign convention and compatible scope. If the official query cannot export anonymously, retain BLOCKED/PARTIAL and request no credentials.

## Invariants
₹0; free official sources only for acceptance. Secondary sources may guide discovery but cannot pass a gate. No inferred sign/scale conversion, no net-to-gross substitution, no stock/flow substitution, no aggregation. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E unchanged. UNKNOWN is never PASS.
