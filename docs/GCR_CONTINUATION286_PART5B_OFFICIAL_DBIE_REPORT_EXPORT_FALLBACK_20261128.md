# GCR Continuation 286 — Part-5B Official DBIE export fallback after FBIL Fetch failure
Date: 28-Nov-2026

## Objective and preflight
Respond to repeated FBIL Foreign Exchange date-range Fetch failures without delaying the RBI DBIE daily interbank USD/INR data task. Re-read current Master Continuity Ledger, GCR Master Priority Queue, Historical Task Registry and C285 report before selecting the next unfinished action. Reused the existing Library screenshots from the user's DBIE export flow; no duplicate Library upload or Library mutation. C282 BankWise raw audit, C283 RBI/FBIL reference-rate calendar gap audit, C284 RBI reference publication scope audit and C285 official DBIE series-existence audit were not repeated.

## Evidence from user-operated official interfaces
- User reached the official RBI DBIE report titled "Daily Interbank Forex Rates (USD vis-a-vis INR) - Web Intelligence" on data.rbi.org.in.
- Screenshot visibly shows six fields: Date; Interbank Open Rate; Interbank High Rate; Interbank Low Rate; Interbank Close Rate; RBI Reference Rate. It also states data available from August 2000. A visible observation dated 31 July 2026 is shown. This is screenshot-level evidence of the official report and displayed schema, not evidence of complete downloadable history.
- In the RBI DBIE export dialog, Excel and TXT formats were available. For Excel, the Reports radio option and "Forex Rates (Current Report)" were selectable, while the Data radio option appeared disabled. User then opened TXT export; Reports and current report were selectable. No exported file has yet been supplied, so no row count, full coverage, or hash has been verified.
- User attempted FBIL Foreign Exchange date-range Fetch repeatedly, including a shorter interval, and reported that loading continued without a result page. This is evidence of repeated client-visible failure only; it does not prove an FBIL server outage. FBIL's public site remains reachable and shows recent USD/INR reference-rate rows. No inference of confirmed outage is made.

## New official workaround
RBI DBIE's own export guide says pre-formatted reports can be exported to Excel, PDF, Text and CSV using "Export Document as"; it also describes report filters, navigation and page controls. Official RBI 2025 dataset compendium identifies the daily forex series as accessible via DBIE Home > Statistics > Financial Market > Forex Market, with MS Excel/PDF dissemination. Therefore use the official report-export path, not the disabled Data radio:
1. Return to the official DBIE report "Daily Interbank Forex Rates (USD vis-a-vis INR)".
2. Tap Download/export icon.
3. Choose Excel.
4. Keep Reports selected; select only "Forex Rates (Current Report)" (not All reports).
5. Export the report. If Excel fails, repeat same steps using TXT; retain the original downloaded file unchanged.
6. Upload the resulting original file for local parsing, row/date/duplicate/null/numeric checks, all-page completeness assessment and SHA-256.
The user previously showed the Excel export dialog but has not yet confirmed selecting Reports > current report > Export. This is the next action, not a completed download.

## Third-party fallback discovery — not accepted
- Dataful page indexed a RBI-attributed daily interbank forex dataset with date, reference_rate, open_rate, high_rate, low_rate, close_rate, unit; it described daily frequency and 2000–2026 coverage. Its page's own opened content reported 6,308 rows / last updated 30-Oct-2026, while a later search snippet reported 6,331 rows / 17-Nov-2026. These inconsistent snapshots and non-RBI hosting make it unsuitable as primary or accepted production data. Discovery only; do not download/merge or use as a substitute for official DBIE export.
- An independent third-party catalogue exposes candidate source identifier IB_FOREX_RT_RN and 31,191 indexed rows, but the exact identifier is not confirmed on RBI's own portal and the indexing layer is not RBI. Treat as discovery-only; not official proof.
- No Dataful, RSI-data, GitHub mirror, NSE/FBIL derived dataset, or other non-official copy was merged into project data.

## Adjudication
- Official RBI DBIE series existence: PASS (C285).
- Official report title and six displayed columns: SCREENSHOT_CONFIRMED.
- DBIE official export facility for reports: PASS (RBI guide / compendium).
- Excel Reports export attempt by user: NOT_YET_CONFIRMED.
- Original downloaded file, full history, row counts, null/duplicate QA, hash: NOT_CAPTURED / NOT_RUN.
- FBIL Fetch failure: USER_REPORTED_REPEATED_FAILURE; server outage NOT_PROVEN.
- USD/INR interbank ingestion: BLOCKED pending original official DBIE report export and QA.
- FBIL reference-rate full history: remains separately blocked; not conflated with interbank OHLC.

## Next action
User to export the current official RBI DBIE report using Excel > Reports > Forex Rates (Current Report) > Export (or TXT Reports fallback) and attach the original file. Do not use the disabled Data radio. Do not submit paid registration, use hidden endpoints, bypass controls, or accept third-party mirrors as primary. Once file is attached, inspect it and test whether all pages/rows and all six columns are present; if partial, retain partial status and identify next official path.

## GCR state and invariants
Macro-Geo P0 last artifact-backed 6/8. FPI and DII remain separate blockers. Strict GCR hard gate BLOCKED; candidate_release_allowed=false; overall NOT_COMPUTABLE / NOT_CERTIFIED. No production logic change: CORE-672 (56x12), Engines A-E, Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, IPO-PLX V2.0 unchanged. UNKNOWN is neither PASS nor FAIL. Research spend ₹0; no paid API, licence, subscription, external contact, fabricated data, interpolation, forward-fill or mirror data.

## Sources
- RBI DBIE export guide: https://dbieold.rbi.org.in/DBIE/doc/Exporting_report_data_%26_related_options.pdf
- RBI Compendium of Datasets and Registries in India 2025 (DBIE route and dissemination formats): https://mospi.gov.in/uploads/announcements/announcements_1784105510784_81827f6f-a2a9-4bbf-8b37-a061a55e1f45_Compendium_of_Datasets_and_Registries_in_India_2025.pdf
- RBI DBIE Comprehensive Guide, April 2026: https://www.rbi.org.in/SCRIPTs/PublicationsView.aspx?id=24094
- Dataful listing, discovery-only and rejected as primary: https://dataful.in/datasets/17545/
- Third-party indexed catalogue, discovery-only: https://platform.rsi-data.com/catalogue/rbi-dbie/acf28c830394ee954deaaa7b
- FBIL official public page: https://www.fbil.org.in/
