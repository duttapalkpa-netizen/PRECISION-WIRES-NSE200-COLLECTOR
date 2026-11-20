# India FPI — NSDL Archive Public Form Contract Audit (Continuation 76)
Date: 2026-11-20 (Asia/Kolkata)
Project: PRECISION-WIRES V11.3 / GCR India FPI Lineage
Status: **RAW LANDING PAGE AND FORM CONTRACT INSPECTED; POSTBACK/ARCHIVE ROWS NOT EXECUTED; NO DAILY ARCHIVE DATA CLAIMED.**

## 1. Continuity preflight
- Re-fetched current Continuity & Acceptance Ledger (blob SHA `eb05fb1714143e5e153b1e67c38be38330b42961`) and GCR Master Priority Queue (blob SHA `8ec86aa54515138f0dc2384c8ce96c1ae067e14a`).
- Reopened India FPI source/schema audit Continuation 72, exact CDSL sector capture Continuation 73, matched-date reconciliation Continuation 74 and sector arithmetic QA Continuation 74.
- Excluded completed PASS work: seven-page raw capture and ZIP digest verification; eight-page capture and sector raw-page capture; 192/192 sector-row subtotal arithmetic. Did not repeat daily total arithmetic or pretend adjacent NSDL/CDSL dates match.
- Selected the remaining executable source-contract dependency: inspect the already captured official NSDL Archive ASP.NET form to establish whether the date selection and export controls are documented and what the public request surface actually exposes.

## 2. Artifact integrity
- Downloaded existing GitHub Actions artifact 14524707532 (run 44515445620) as ZIP.
- Local file: `gcr-india-fpi-raw-pages-2.zip`, 184,876 bytes.
- Independently recomputed SHA-256: `29530f3d0913f3eed93afbeb0759ecb8131b4192c71e5928d79961df77c24c69`, matching the previously recorded GitHub digest.
- Inspected only the already archived `nsdl_archive.html` member; no source POST or form submission was made.

## 3. Observed official NSDL Archive form contract
Official page: https://www.fpi.nsdl.co.in/web/Reports/Archive.aspx
- Form: `frmMonthly`; method: POST; action: `./Archive.aspx`.
- ASP.NET hidden state fields present: `__VIEWSTATE`, `__VIEWSTATEGENERATOR`, `__EVENTVALIDATION`.
- Date controls:
  - `txtDate`: text input, disabled in the captured initial HTML, maxlength 10.
  - `hdnDate`: hidden input; page calendar callback copies the selected `txtDate` value into this field.
  - Calendar display format: `%d-%b-%Y`.
- Export/validation fields:
  - `HdnValexceldata`: hidden field populated by `ExportDIVtoExcel()` from the current `#dvArchiveData` HTML after HTML escaping.
  - `hdnFlag`: hidden validation flag. `fnVal()` sets it to `F` if date is blank, otherwise clears it.
- Explicit postback controls observed in anchors:
  - View Report: `__doPostBack('btnSubmit1','')`
  - Export to Excel: `__doPostBack('btnExcel','')`
- The page is therefore an interactive ASP.NET postback form, not a static GET archive file. The date field is not directly editable in the captured initial DOM; its calendar callback sets the hidden date value.
- The initial GET response contains no archive investment rows. It does not prove any date-specific query succeeded.

## 4. Safety and evidence boundary
- No POST was sent. The exact server-side handling, required control values, selected-date acceptance, returned report schema, and export response remain unverified.
- The visible JavaScript documents the client-side validation and postback target names, but does not establish server-side semantics or whether the report is one date, one month, or another period.
- Do not replay captured ViewState/EventValidation values in a later session; ASP.NET state may be session/time dependent. Any later read-only query must obtain a fresh page state and follow the actual public calendar/control flow.
- No archive rows, values, date coverage, row count, source hash for queried output, or confirmed/provisional status are claimed.
- No third-party scraper code was used. No credentials, login, CAPTCHA bypass, access-control bypass or external contact.

## 5. Acceptance matrix
| Gate | Status |
|---|---|
| Current ledger and queue reopened | PASS |
| Prior FPI reports reopened | PASS |
| Existing artifact downloaded | PASS |
| Artifact ZIP SHA-256 matches recorded digest | PASS |
| Exact NSDL Archive page raw HTML inspected | PASS |
| ASP.NET form/method/action identified | PASS |
| Date and hidden-field names identified | PASS |
| View Report / Export postback target names identified | PASS |
| Server-side query semantics | UNKNOWN |
| Fresh-state date-specific postback | NOT_DONE |
| Archive output bytes / response headers | NOT_CAPTURED |
| Archive row schema/date coverage | NOT_DONE |
| Matched-date NSDL/CDSL reconciliation | NOT_DONE |
| Production ingestion | BLOCKED / NOT_AUTHORIZED |

## 6. Next exact action
- Use a supported browser interaction to load a fresh NSDL Archive page, operate the visible calendar, choose one explicit historical report date, and invoke the public View Report control once; capture the exact response bytes, headers, final URL, retrieval UTC and SHA-256.
- If that returns a report table, inspect whether the output is one date or a month of daily rows, preserve every source row and reporting date, and only then assess matched-date comparability with CDSL eServices.
- If the host cannot perform this interactive postback, leave archive data NOT_DONE; do not guess the POST body or automate stale ViewState values. Advance only to another independent source task.
- Export to Excel is not required if the View Report response itself contains the full table; avoid duplicate requests.

## 7. Protected invariants
₹0; official public sources only; no paid API; no synthetic or interpolated rows; no daily/fortnightly conflation; no AUC-stock/flow conflation; no guessed date alignment; no silent status promotion. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E, IPO-PLX V2 and the fixed 63-country IMF cohort unchanged. UNKNOWN is never PASS.
