# GCR CDSL Daily Archive — Static Snapshot & Freshness Boundary Audit (Continuation 78)
Date: 2026-11-20 (Asia/Kolkata)
Scope: inspect the already captured official CDSL daily-archive page and its manifest metadata. No new request, no form submission, no challenge bypass, no production ingestion.

## Continuity preflight and excluded repeats
- Re-fetched current Continuity & Acceptance Ledger (blob SHA `924b5a37402654354077911ca9bcea746660b849`), GCR Master Priority Queue (blob SHA `04fe3e5aeda44ac55a1fdd9a4fc73d660b637165`) and Continuation 77 report (blob SHA `181e041bc872d96586ead475092432b7bf8f187a`).
- Reused artifact 14527092174 / run 44519322726. ZIP SHA-256 independently recomputed as `83048ea0bc712b6a453270f8fb5c3c6755b579857ff2ad9eb7d53c8ba1778fbd`, matching the prior digest.
- Did not repeat CDSL daily arithmetic 17/17, category 7/7 or CDSL fortnightly sector 192/192.
- BSE/NSE TRI rights gates already completed; not repeated. NSDL archive postback remains separate and was not guessed.

## Artifact and exact source provenance
- ZIP member: `cdsl_daily_archive.html`
- Official URL from capture manifest: `https://www.cdslindia.com/Publications/ArchiveDataAfter2009.aspx`
- Captured method: GET; HTTP 200; final URL unchanged.
- Retrieved UTC: `2026-11-19T11:57:09.076562+00:00`; response Date: `Thu, 19 Nov 2026 11:57:09 GMT`.
- Content-Type: `text/html; charset=utf-8`; byte count 73,784.
- Member SHA-256: `aa2a03c6621772e52b0b9ac52f11b525d82f1ce80539554302eda861145304df`.
- Response metadata also records Cloudflare server / CF-RAY `a5cf09281baf0789-BLR`; the HTML includes a challenge-platform bootstrap script marker. The captured page nevertheless contains a complete static HTML report body; no challenge resolution or bypass was attempted.

## Observed page contract and content boundary
- Document title: `Archive Data`; heading: `Daily Trends in FII / FPI Investment & Derivatives`.
- No HTML forms, input elements, select elements, or buttons were present in the captured response. No calendar, date picker, date-range selector, or visible archive-control contract was found.
- The page is a static report snapshot, not an interactive date-selection response in the captured HTML.
- Both daily cash and derivatives headings state “upto 02-Mar-2026”.
- Cash table: 86 HTML rows; it contains one explicit daily reporting date, `02-03-2026`, followed by “Total for March”, “Total for 2026”, and “Cumulative total since November 1992 till MAR 02, 2026” aggregate sections. It does not contain a multi-date daily history in this response.
- Derivatives table: 30 HTML rows; its daily report date is `02-MAR-2026`, followed by monthly and 2026 aggregate rows. Derivatives are a separate data dimension and are not combined with cash.
- The archive page's latest daily date is 261 calendar days earlier than the CDSL Latest page's `18-NOV-2026` reporting date captured in the same ZIP (comparison is date-to-date only; no claim that every intervening calendar day is a trading day).
- Cash-table source note says custodian reports submitted on 02-Mar-2026 and trades conducted on/up to previous trading day(s). The Notes section separately distinguishes provisional exchange-member T-day data from custodian-confirmed custodian/depository data for previous trading day(s).

## Decision
**CDSL Daily Archive historical coverage: STALE STATIC SNAPSHOT / INCOMPLETE FOR DAILY HISTORY; date-control execution NOT_AVAILABLE_FROM_CAPTURED_HTML.**
The captured official archive URL returned a static report with a single daily observation date plus monthly/YTD/cumulative aggregates. The capture does not expose an archive date selector or form controls. Its reporting cutoff is 02-Mar-2026 despite retrieval on 19-Nov-2026, while the separately captured Latest page reports 18-Nov-2026. Therefore this artifact cannot establish a continuous historical daily series or current archive completeness.
This is a statement about the exact captured response, not a claim that CDSL has no other archive UI or that its server blocks all historical retrieval. No further request, undocumented parameter, hidden endpoint or challenge bypass was attempted.

## Acceptance matrix
| Gate | Status |
|---|---|
| Existing ZIP digest reverified | PASS |
| Exact CDSL archive HTML member hash/length verified | PASS |
| GET URL, HTTP 200, retrieval UTC and response headers recovered from manifest | PASS |
| Static page title/report headings inspected | PASS |
| No form/input/select/button/calendar in captured response | PASS |
| Daily archive page exposes interactive date-control contract | NOT_FOUND_IN_CAPTURE |
| One daily observation date identified (02-Mar-2026) | PASS |
| Monthly/YTD/cumulative aggregates distinguished from daily observations | PASS |
| Archive cutoff freshness vs Latest page measured (261 calendar days) | PASS |
| Continuous daily historical coverage | UNKNOWN / NOT_ESTABLISHED |
| CDSL archive date-specific selection/output | NOT_DONE |
| NSDL/CDSL matched-date reconciliation | NOT_DONE |
| Sector flow/return predictive join | BLOCKED / NOT_RUN |
| Production admission | BLOCKED / NOT_AUTHORIZED |

## Next exact action
- Do not retry the same captured GET or invent date parameters: the captured page has no date controls.
- If a supported interactive browser becomes available, navigate the official CDSL archive UI from the official site and inspect only visible user controls; select one date only if an actual control is present, then capture fresh response bytes and metadata. No undocumented API or challenge bypass.
- Otherwise, advance to a different unfinished official-source task. Keep the CDSL archive historical daily series UNKNOWN and excluded; do not infer dates from monthly/YTD totals.

## Protected invariants
₹0; official/free sources only; no synthetic or interpolated rows; no challenge/access-control bypass; no fabricated timestamps; no silent forward-fill; no daily/fortnightly conflation; no AUC stock/flow conflation. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E, IPO-PLX V2 and fixed 63-country Q2-2026 IMF cohort unchanged. UNKNOWN is never PASS.
