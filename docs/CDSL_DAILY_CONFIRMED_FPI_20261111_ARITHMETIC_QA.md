# CDSL Daily Confirmed FPI — 11-Nov-2026 Rendered-Table Extraction and Arithmetic QA

## Source and observation identity
- Official CDSL daily route: https://www.cdslindia.com/eservices/publications/fiidaily
- Displayed report date: 11-NOV-2026.
- CDSL methodology note: compiled from reports submitted by custodians on 11-NOV-2026 and represents trades conducted on and up to the previous trading day(s).
- This is custodian/depository-reported confirmed activity, not same-day exchange provisional T-day flow.
- Representation inspected: rendered official HTML table. No raw daily archive bytes were acquired; no SHA-256 is claimed.

## Daily investment totals (INR crore)
| Category | Gross purchases | Gross sales | Net investment |
|---|---:|---:|---:|
| Equity (including primary/others) | 20,711.14 | 13,751.79 | 6,959.35 |
| Debt-General | 350.80 | 55.51 | 295.29 |
| Debt-VRR | 185.30 | 48.75 | 136.55 |
| Debt-FAR | 1,014.98 | 2,189.46 | -1,174.48 |
| Hybrid | 4.11 | 16.83 | -12.72 |
| Mutual Funds | 65.11 | 6.79 | 58.32 |
| AIF | 0.00 | 0.00 | 0.00 |
| **Total** | **22,331.44** | **16,069.13** | **6,262.31** |

USD net investment total displayed: USD 667.212 million.

## Arithmetic QA
- PASS: category gross purchases sum to 22,331.44 INR crore.
- PASS: category gross sales sum to 16,069.13 INR crore.
- PASS: category net investment sums to 6,262.31 INR crore.
- PASS: total gross purchases minus gross sales = 6,262.31 INR crore.
- PASS: Equity net 6,959.35; Debt-General 295.29; Debt-VRR 136.55; Debt-FAR -1,174.48; Hybrid -12.72; MF 58.32; AIF 0.00 sum to 6,262.31.
- USD total is retained as displayed; this task did not independently re-perform each category's FX conversion.

## Archive route investigation
- SEBI's official FPI curation index maps daily latest/current-month/archive routes to both NSDL and CDSL.
- CDSL legacy archive page renders only date controls and the 1999-Till Date / 1992-1998 choices in accessible HTML text; it does not expose a historical downloadable file URL or bytes in this retrieval.
- The corresponding NSDL archive URL listed by SEBI returned HTTP 502 in this web retrieval. This is an access failure for this attempt, not proof of permanent outage.
- Therefore daily historical raw archive acquisition remains OPEN / NOT ACQUIRED. No synthetic reconstruction or interpolation from fortnightly/monthly series is permitted.

## Integration and research status
- Keep this CDSL custodian-reported daily series distinct from NSE provisional T-day exchange data.
- Do not merge it with the fortnightly sector/AUC report as if they were same-frequency observations.
- Research-only. No production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 diagnostics, or Hard Gate changed.
- No spend, no paid source, no external contact, no PR/merge.
- This page-level arithmetic QA is not a full daily historical archive or multi-day date-coverage validation.

## Next step
Resolve historical archive retrieval through the official CDSL date selector using a browser-capable interaction or obtain the official exported archive bytes for reproducible hashing and date/schema QA. Keep historical archive status UNKNOWN until actual bytes are acquired and validated.
