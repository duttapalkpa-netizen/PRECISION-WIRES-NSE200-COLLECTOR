# GCR Continuation 284 — Part-4 RBI daily reference-rate publication scope and historical-coverage adjudication (27-Nov-2026)

Date: 2026-11-27 (Asia/Kolkata)  
Conversation: গবেষণা যাচাই অব্যাহত 62, Part-4  
Repository: `duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR`

## 1. Mandatory continuity preflight / PASS skip
- Re-read current Master Continuity Ledger, GCR Master Priority Queue, 63-country Historical Task Registry, C283 full RBI/FBIL calendar-gap report and C282 correction.
- Re-read the Library Mother File `PRECISION_WIRES_V11_3_MOTHER_FILE_CONTINUATION_1_53_20261122.md` (the curated continuity summary through C57) and the Library FX source eligibility audit `PRECISION_WIRES_page31_FX_series_eligibility_audit.csv`, plus the Page-42 FX source boundary register. Existing FX audit already classified RBI Table 223 as official source identity PASS for displayed period only, not a full long-history archive.
- Skipped completed C278 regression PASS, C283 BankWise raw hash/table QA, C283 calendar-gap computation, prior source-discovery and the RBI form extraction attempt. No repeated Library upload, raw payload parse, workflow, or production change.

## 2. Selected task and acceptance question
Determine whether RBI's official Handbook of Statistics daily exchange-rate tables (Table 218/222/223) can be accepted as a complete historical bridge for the missing 2018–2022 segment in the partial BankWise USD/INR reference-rate extract.

## 3. New official RBI evidence
RBI annual-publication pages explicitly label the series as `Daily Exchange Rate of the Indian Rupee`, state that values are based on the RBI Reference Rate, and note that FBIL commenced dissemination from 10-Jul-2018. RBI's 04-Jul-2018 press release separately states that FBIL publishes on Mumbai business weekdays excluding Saturdays, Sundays and Mumbai bank holidays.

The inspected official publication pages show these visible date spans:
| RBI publication | Page publication date | Visible USD/INR observation span in the page representation | Scope finding |
|---|---|---|---|
| Table 218, id=19951 | 18-Sep-2020 | 24-Dec-2019 to 31-Jul-2020 | Partial segment only; does not cover 2019-20 from its start or all of 2020 |
| Table 218, id=22024 | 15-Sep-2023 | 02-Jan-2023 to 28-Jul-2023 | Partial 2022-23 / 2023-24 segment only |
| Table 218, id=22692 | 13-Sep-2024 | 01-Jan-2024 to 31-Jul-2024 | Partial FY segment only |
| Table 222, id=23396 | 29-Aug-2025 | 01-Jan-2025 to 31-Jul-2025 | Partial FY segment only |
| Table 223, id=24048 | 31-Jul-2026 | 01-Jan-2026 to 30-Jun-2026 | Partial FY segment only; no July–Nov 2026 observations in this page |

The visible daily rows are official RBI-published reference-rate observations for their displayed dates. They are not a complete machine-readable full-history archive. The table pages do not expose a single continuous 10-Jul-2018-to-present downloadable dataset in the inspected representation.

## 4. Reconciliation against C283 gap — decision
C283 established that the two identical Library BankWise files contain 1,119 unique observations, with a 1,358-calendar-day hole between 24-Jul-2018 and 12-Apr-2022, including zero observations for 2019, 2020 and 2021. The RBI publication pages inspected here add only isolated/limited windows:
- The 2019/2020 page starts 24-Dec-2019 and ends 31-Jul-2020, leaving 10-Jul-2018 through 23-Dec-2019 and 01-Aug-2020 through 31-Dec-2021 unbridged by this inspected page.
- The 2023 page begins 02-Jan-2023; it does not bridge 2021 or most of 2022.
- The 2024–2026 pages cover only their displayed windows and cannot establish the missing 2018–2022 daily series.

No full raw RBI annual-publication file was downloaded or hashed in this audit; no rows were ingested or merged. Therefore this is a source-scope adjudication, not a raw-data capture or date-by-date reconciliation.

## 5. Corrected acceptance matrix
| Gate | Result | Boundary |
|---|---|---|
| RBI Table 218/222/223 source identity | PASS | Official RBI pages |
| Reference-rate series semantics | PASS | RBI pages say based on RBI Reference Rate; FBIL takeover date stated |
| Displayed-page date observations | SOURCE_FOUND / CONFIRMED | Only the exact dates shown on each page |
| Full 2018–2026 historical coverage | FAIL / NOT_ESTABLISHED | Published pages inspected are discontinuous/partial |
| Full downloadable raw payload and SHA-256 | NOT_CAPTURED | No raw download performed |
| Calendar-aware session completeness | UNKNOWN | Requires authoritative Mumbai holiday calendar joined to complete raw daily rows |
| Interbank OHLC equivalence | NOT_APPLICABLE / NOT_ACCEPTED | Reference fixing is not interbank OHLC |
| USD/INR full-history ingestion | BLOCKED / UNKNOWN | C283 continuity hole remains open |

## 6. Exact next executable action
1. Keep the official RBI Table 218/222/223 pages as displayed-period cross-check references only; do not use them as a continuous replacement for BankWise or the full FBIL archive.
2. Continue only with a genuinely documented, official, machine-readable FBIL historical export or an exact official RBI DBIE table/export route. For DBIE, the brochure proves the daily interbank USD-vis-a-vis-INR series exists, but the exact current official table key, schema and raw export remain unverified. Do not copy the prototype `dbie.rbihub.in` mirror's table or API.
3. If a full official payload is obtained, preserve original bytes and hash before parsing; validate schema, dates, units, duplicates, numeric/null values and calendar-aware expected publication sessions. Keep reference fixing and interbank OHLC as separate series.
4. No paid license, UAT form submission, personal-detail submission, external contact, or terms circumvention. If FBIL use requires a fee-liable licence for the intended research, leave the series BLOCKED under the ₹0 rule.

## 7. Project state / protected invariants
- USD/INR: source identity CONFIRMED; partial BankWise raw integrity PASS; full continuity FAIL; calendar completeness UNKNOWN; full-history ingestion BLOCKED / UNKNOWN.
- FPI/DII remains a separate P0 blocker; do not merge the two flow types or substitute provisional NSE activity / CDSL FPI for final DII.
- Macro-Geo P0 remains last artifact-backed 6/8; strict GCR hard gate BLOCKED; `candidate_release_allowed=false`; overall GCR NOT_COMPUTABLE / NOT_CERTIFIED.
- ₹0; official/free sources only; UNKNOWN is neither PASS nor FAIL; no proxy/mirror, synthetic rows, interpolation, forward-fill or fabricated timestamps.
- CORE-672 (56×12), Engines A–E, Production Selector, `RANKING_SCORE`, `+1 PRESSURE_FADE`, IPO-PLX V2.0 unchanged. No broad workflow, merge or production integration.

## 8. Official source references
- RBI Table 218 (2019–20 / 2020–21): https://www.rbi.org.in/scripts/PublicationsView.aspx?id=19951
- RBI Table 218 (2022–23 / 2023–24): https://www.rbi.org.in/Scripts/PublicationsView.aspx?id=22024
- RBI Table 218 (2023–24 / 2024–25): https://www.rbi.org.in/scripts/PublicationsView.aspx?id=22692
- RBI Table 222 (2024–25 / 2025–26): https://www.rbi.org.in/scripts/PublicationsView.aspx?id=23396
- RBI Table 223 (2025–26 / 2026–27): https://www.rbi.org.in/Scripts/PublicationsView.aspx?id=24048
- RBI FBIL takeover / weekday publication statement: https://www.rbi.org.in/Scripts/BS_PressReleaseDisplay.aspx?prid=44393
- RBI DBIE brochure (daily interbank forex series existence): https://dbieold.rbi.org.in/DBIE/doc/Brochure%20on%20DBIE%20-2022%20English.pdf
