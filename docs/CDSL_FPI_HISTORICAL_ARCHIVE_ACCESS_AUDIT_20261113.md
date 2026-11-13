# CDSL Historical FPI Archive — Access and Evidence Audit
Audit date: 2026-11-13 (Asia/Kolkata)
Project: PRECISION-WIRES V11.3
Status: OFFICIAL_ARCHIVE_DISCOVERY_PASS / RAW_ARCHIVE_ACQUISITION_BLOCKED

## Objective
Continue the historical confirmed-FPI input workstream without repeating the 12-Nov-2026 CDSL live-page arithmetic audit. Establish the official archive surface, its stated coverage, and whether retrievable raw archive bytes are available through the current research retrieval path.

## Official source evidence
1. CDSL historical archive page:
   https://www.cdslindia.com/Publications/FIITrends.aspx
   - Page exposes an Archive section.
   - Archive controls visibly include "1999-Till Date" and "1992-1998".
   - Page footer states last updated 20-May-2020.
   - The retrieved page text exposes archive controls but no direct downloadable archive URL, file name, byte count, or machine-readable response.
2. SEBI official FPI curation:
   https://www.sebi.gov.in/curation/fpi.html
   - Lists CDSL source links for Daily Trends, Current Month, and Trends in FPI Investments Archive.
   - CDSL archive link is https://www.cdslindia.com/Publications/FIITrends.aspx.
3. CDSL daily confirmed FPI page:
   https://www.cdslindia.com/eservices/publications/fiidaily
   - Current inspected page displays reporting date 12-NOV-2026.
   - This is live-page evidence only; the prior 12-Nov arithmetic audit is not repeated here.
   - CDSL explains that confirmed FPI trades are compiled from custodian reports and relate to trades on and up to previous trading days; exchange T-day data is provisional and must remain separate.

## Retrieval attempt and outcome
- Opened the official CDSL archive URL; archive selector is visible, but the page extraction exposes no direct file link or archive payload.
- Attempted direct page retrieval from the execution environment; retrieval failed. This does not establish a CDSL server-side outage or a failed HTTP status.
- No archive bytes, rows, date range, schema, or raw SHA-256 were obtained in this audit.
- No inferred URL, guessed API endpoint, synthetic observations, or third-party replacement dataset was used.

## Evidence status
| Check | Status | Basis |
|---|---|---|
| Official archive source identity | PASS | SEBI curation and CDSL archive page |
| Archive coverage selector | PASS | Visible "1999-Till Date" and "1992-1998" controls |
| Archive page freshness | LIMITATION | Footer says last updated 20-May-2020 |
| Direct archive download endpoint | UNKNOWN | No endpoint exposed in retrieved page text |
| Raw archive acquisition | BLOCKED | No bytes retrieved |
| Raw SHA-256 | UNKNOWN | No raw bytes |
| Schema / row count / date coverage | UNKNOWN | No raw bytes |
| Daily report date / publication date reconciliation | NOT_STARTED | Requires archive payload and date dictionary |
| Confirmed-vs-provisional reconciliation | NOT_STARTED | Must preserve separate source classes |

## Non-substitution and point-in-time controls
- CDSL confirmed custodian-reported FPI series must remain separate from NSE provisional exchange T-day FPI/FII series.
- Preserve reporting date, underlying trade date (where explicitly documented), publication/retrieval timestamp, source URL, raw bytes, and source revision as separate fields.
- Never backfill missing archive dates, infer weekends/holidays as zero, or overwrite confirmed values with provisional values.
- Do not infer an API route from page controls or scrape around access restrictions.
- Do not accept secondary mirrors as official CDSL raw archive.

## Next exact action
Obtain the archive through the official CDSL page's supported date/period control or a documented public endpoint. Preserve the original response bytes and response metadata, hash before parsing, then validate file type, schema, unique date/category keys, coverage gaps, and overlap against CDSL daily pages and SEBI's curation record. If the official control does not expose a public download, retain BLOCKED and request a user-provided official export; do not guess endpoints.

## Project invariants
₹0 spend; free official sources only; no paid APIs; no synthetic rows or timestamps; UNKNOWN is neither PASS nor FAIL. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56 × 12), and Hard Gate remain unchanged. No PR merge or production integration is authorized. Overall project progress remains NOT_CALCULABLE until the full acceptance ledger and weights are reconciled.
