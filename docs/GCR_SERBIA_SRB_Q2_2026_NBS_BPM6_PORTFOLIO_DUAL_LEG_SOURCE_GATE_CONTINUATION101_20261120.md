# Serbia SRB Q2-2026 — NBS BPM6 portfolio dual-leg source gate
Date: 2026-11-20 (Asia/Kolkata)
Continuation: Research verification 44 / Continuation 101
Decision: **SRB fixed-cohort membership PASS; official NBS BPM6 monthly BOP source publishes separate portfolio asset and liability transaction rows for Apr–Jun 2026; quarterly sums are computable from the monthly flow table; Q2 national legs extracted from published text but raw PDF bytes/SHA-256 and exact archived IMF SRB rows are not captured; same-vintage comparison NOT_DONE; SRB PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.**

## 1. Continuity preflight / PASS work excluded
- Re-fetched Master Continuity Ledger (blob SHA dc5b53b50cea760387096f0028b52c3892373b71), GCR Priority Queue (blob SHA f048598e774639cb80441e22dacc341efa3d00b2), SLV Continuation 100 (blob SHA 658b83d795529e9eecd99879039e6e8bcdb6a8c3), and immutable 63-country cohort (blob SHA 31f5bfe5adb59f4c1a139b6d8c54b5ad9fb672c8).
- SRB (Serbia, Republic of) is the next fixed-cohort member after SLV and is present with both IMF Q2-2026 legs. Repository search found no dedicated SRB Q2 national portfolio dual-leg report.
- No cohort rebuild, no IMF re-query, and no repeat of SLV/SLB/RWA source gates.

## 2. Official NBS source and direct observations
- National Bank of Serbia (NBS), Statistical Bulletin — September 2026, Table 2.3 “Balance of Payments of the Republic of Serbia (BPM6)”, page 105, reports monthly observations in million euros and labels the data preliminary.
- The table includes separate rows:
  - 3.2.A Portfolio investment — Assets
  - 3.2.B Portfolio investment — Liabilities
  - 3.2 Portfolio investment, net (= asset − liabilities)
- The table note says the BOP presentation follows BPM6 as far as possible, values are subject to correction as official sources change, and data are subject to rounding. The table is available in the official NBS Statistical Bulletin PDF. Its data cutoff is 17 September 2026 as stated in the adjacent Table 2.3 source notes; publication vintage is September 2026 bulletin. Exact first-publication timestamp for this PDF was not independently captured.

## 3. Q2-2026 quarterly aggregation from monthly flow rows
Source unit: EUR million. Monthly entries are monthly BOP flow observations; Q2 is Apr + May + Jun 2026.

| NBS Table 2.3 row | Apr-2026 | May-2026 | Jun-2026 | Q2-2026 sum |
|---|---:|---:|---:|---:|
| 3.2.A Portfolio assets | +149 | -25 | +124 | **+248** |
| 3.2.B Portfolio liabilities | -19 | +3,932 | +199 | **+4,112** |
| 3.2 Portfolio net (= assets − liabilities) | +168 | -3,957 | -75 | **-3,864** |

- Arithmetic check: 248 − 4,112 = -3,864 EURm; matches the sum of the three monthly net rows (168 − 3,957 − 75 = -3,864 EURm).
- The Q2 values above are derived only by summing the published separate monthly transaction rows. No net-to-leg inference, stock difference, FX conversion, sign reversal or annual proration was used.
- The large May 2026 liability value (+3,932 EURm) is reproduced as published; it is not normalized, winsorized or silently “corrected”. It materially drives the quarter total and must be checked against the source workbook / subsequent vintage before any final comparison.
- Table uses the NBS presentation “net (= asset − liabilities)”; separate asset and liability row values are preserved with their published signs. Do not impose an unverified transformation to IMF signs.

## 4. Evidence boundary / gate matrix
- SRB fixed 63-country Q2 both-leg cohort membership: PASS.
- Official NBS BPM6 monthly BOP table and separate portfolio asset/liability rows: PASS (web-text inspection).
- Q2 asset and liability arithmetic from monthly flows: PASS (248 / 4,112 EURm; preliminary).
- Net identity check: PASS (-3,864 EURm).
- Original PDF bytes, response headers, byte count and SHA-256: NOT_CAPTURED.
- Exact IMF archived SRB A_NFA_T and L_NIL_T rows: NOT_CAPTURED; existing 12-country exact-sample receipt does not establish SRB values. Large normalized panel has previously returned empty content through the GitHub fetch route; no alternate byte-preserving retrieval completed here.
- IMF↔NBS concept/sign bridge: NOT_ESTABLISHED.
- Same-vintage alignment: NOT_ESTABLISHED.
- Independent confirmation of unusual May liability observation: NOT_DONE.
- Two-leg IMF comparison: NOT_DONE.
- SRB country validation: PARTIAL / NOT PASS.
- Aggregate / production admission: NOT_AUTHORIZED.

## 5. Next exact actions
1. Obtain the official NBS September 2026 Statistical Bulletin PDF as raw bytes through a supported byte-preserving route; record URL, HTTP status/headers, byte count, SHA-256, retrieval timestamp and immutable archive path before parsing.
2. Verify the May-2026 +3,932 EURm portfolio-liability monthly value against the official NBS downloadable statistical series / subsequent bulletin vintage; preserve both vintages if revised.
3. Retrieve exact archived IMF SRB Q2-2026 A_NFA_T and L_NIL_T rows from the existing panel via a supported raw-file route; no new IMF query.
4. Establish the NBS-to-IMF sign/concept and vintage mapping from official metadata, then compare the two legs independently. Until then, do not admit SRB to any aggregate.

## 6. Official source
- NBS Statistical Bulletin — September 2026, official PDF: https://www.nbs.rs/export/sites/NBS_site/documents-eng/publikacije/sb/sb_09_26.pdf
- NBS Balance of Payments official data page: https://www.nbs.rs/en/drugi-nivo-navigacije/statistika/platni_bilans/

## 7. Protected invariants
No cohort rebuild, no IMF re-query, no synthetic data, no stock-as-flow, no net-to-leg inference, no FX inference, no sign flip, no unverified vintage promotion, no production changes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS. Research spend ₹0.
