# GCR India FPI Matched-Date Reconciliation Audit — Continuation 74
Date: 2026-11-19
Scope: independent inspection of immutable raw artifacts 14524707532 and 14527092174. Research-only; no production admission.

## Inputs and integrity
- Artifact 14524707532 (run 44515445620), ZIP 184,876 bytes, SHA-256/GitHub digest: 29530f3d0913f3eed93afbeb0759ecb8131b4192c71e5928d79961df77c24c69.
- Artifact 14527092174 (run 44519322726), ZIP 196,057 bytes, SHA-256/GitHub digest: 83048ea0bc712b6a453270f8fb5c3c6755b579857ff2ad9eb7d53c8ba1778fbd.
- Both manifests contain seven/eight HTTP 200 source responses respectively. HTTP status alone is not accepted as content-validity or coverage proof.

## Matched-date provider reconciliation
- NSDL Latest table: reporting date 19-Nov-2026; total gross purchases INR 22,356.99 crore; gross sales INR 14,591.05 crore; net INR 7,765.94 crore; net USD 831.87m.
- CDSL eServices current daily cash table: reporting date 18-Nov-2026; total gross purchases INR 29,344.36 crore; gross sales INR 16,797.46 crore; net INR 12,546.90 crore; net USD 1,340.906m; conversion 93.5703 INR/USD.
- NSDL Latest page explicitly explains provisional exchange-member T-day data versus confirmed custodian/depository reports for previous trading day(s). The table displayed on that page is not explicitly split into two machine-readable status tables in the captured HTML; do not silently classify all displayed rows as a confirmed same-date pair.
- CDSL eServices page states the 18-Nov data is compiled from reports submitted to depositories by custodians on 18-Nov and relates to trades conducted up to previous trading day(s).
- Reporting dates differ (19-Nov vs 18-Nov). No matched-date NSDL/CDSL daily comparison is possible from these two rows. Provider variance, relative flow and cross-provider agreement are NOT_COMPUTABLE, not zero and not PASS.

## Arithmetic checks (within-source only)
- NSDL 19-Nov total: 22,356.99 - 14,591.05 = 7,765.94 crore; exact to displayed 2 decimals.
- CDSL 18-Nov total: 29,344.36 - 16,797.46 = 12,546.90 crore; exact to displayed 2 decimals.
- These are arithmetic consistency checks, not independent source corroboration or date alignment.

## CDSL archive instability / response-quality finding
- Artifact 14524707532: `cdsl_daily_archive.html` is 297,824 bytes, SHA-256 `fc95dc0dade735c9f413ef20a3239e138a6064f2694633aa9635864fd8c7ba2b`; main cash table contains 13 dated records from 02-Nov-2026 through 18-Nov-2026 (02,03,04,05,06,09,10,11,12,13,16,17,18 Nov).
- Artifact 14527092174: same requested/final URL returns HTTP 200 but only 73,784 bytes, SHA-256 `aa2a03c6621772e52b0b9ac52f11b525d82f1ce80539554302eda861145304df`; main cash table contains only one 02-Mar-2026 row.
- Same URL, same HTTP 200, materially different content and coverage. This is a raw response instability/partial-render warning; neither response establishes full historical archive completeness. Do not merge the two snapshots or infer missing dates.
- NSDL Monthly and Archive initial GET pages contain forms/selectors; no form submission/postback was attempted. Their HTTP 200 landing responses are not daily data archives.

## CDSL fortnightly sector report (context only)
- Exact 15-Nov-2026 report raw HTML: 327,522 bytes, SHA-256 `3f77f3896a95b8cff3a7728049127493814e1b503eb39dcb75b0e8fe145cf84e`.
- Main table has 24 numbered sector/category rows plus grand total. It separates AUC 31-Oct, net investment 16–31 Oct, net investment 01–15 Nov, and AUC 15-Nov. AUC is stock; fortnightly net investment is flow. Neither is daily cash flow.
- Period-specific INR/USD conversion rates are separately displayed (95.2492 for 31-Oct AUC and 94.1997 for 15-Nov AUC/Nov1–15 net investment). No common FX rate should be imposed.
- Sector classification is based on BSE common industry classification per page note; retain source-defined mapping and Others residual. Sector report cannot validate NSDL/CDSL daily cash flow.

## Acceptance matrix
| Item | Status | Reason |
|---|---|---|
| ZIP digest verification for both captures | PASS | GitHub digest equals downloaded ZIP SHA-256 |
| 8-page official capture runtime | PASS | Run 44519322726 SUCCESS; 8/8 HTTP 200 |
| CDSL dated sector raw capture | PASS | Raw bytes/hash verified |
| NSDL 19-Nov within-table arithmetic | PASS | Gross less sales equals displayed net |
| CDSL 18-Nov within-table arithmetic | PASS | Gross less sales equals displayed net |
| Matched-date NSDL/CDSL daily comparison | NOT_DONE | Reporting dates differ |
| Confirmed/provisional status mapping | PARTIAL | NSDL explanatory caveat; table status not independently separated in capture |
| CDSL archive historical completeness | BLOCKED | Same URL response body/coverage materially inconsistent |
| NSDL archive/monthly daily extraction | NOT_DONE | GET landing pages require form selection/postback; not attempted |
| Sector-to-daily bridge | NOT_APPLICABLE | Different frequency and measure |
| Production ingestion | BLOCKED | No aligned, status-qualified, independently reconciled provider panel |

## Next bounded actions
1. Capture NSDL Latest and CDSL eServices again in a second independent time window; compare reporting date, exact table cells, publication note, raw SHA-256 and content.
2. Obtain a true same-reporting-date NSDL table using only a documented public page/export route; do not infer date alignment from adjacent dates.
3. Investigate CDSL archive date selector/link contract from raw HTML and official page scripts without POST until the request semantics are documented; capture only explicit public GET resources.
4. Build parser tests for gross purchase - gross sale = net, subtotal-to-total, reporting date, unit, route, asset class and provisional/confirmed status; reject unknown status.
5. Brazil: no new endpoint probes. Obtain exact PA changelog/revision export and documented BOP6/BOP_BPM6 crosswalk evidence from official IMF UI/export; until then remain BLOCKED.

## Brazil status unchanged
- Registration lifecycle: 40/40 PASS.
- PA transaction-2 Changelog: BLOCKED (known HTTP 500; no repeat).
- BOP6 vs BOP_BPM6 identity: BLOCKED; no alias.
- Owner-side exact PA Changelog export remains a required external evidence dependency.
- No new Brazil evidence is claimed by this report.

## Hard invariants
₹0; official/free sources only; no synthetic data, daily interpolation, net-to-gross inference, unapproved FX/scale/sign conversion, or fabricated timestamps. UNKNOWN is never PASS. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56x12), Engines A-E unchanged. GCR/Brazil overall remain incomplete and production not authorized.
