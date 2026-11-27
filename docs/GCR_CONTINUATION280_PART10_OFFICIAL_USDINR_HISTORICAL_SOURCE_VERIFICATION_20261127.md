# GCR Continuation 280 — Part-10 official USD/INR historical-source verification and capture boundary (27-Nov-2026)

Date: 2026-11-27 (Asia/Kolkata)

## 1. Preflight and duplicate prevention
- Re-read current GitHub Master Continuity Ledger, C279 report, GCR Master Priority Queue, Historical Task Registry, Failure Lessons and Library Mother File (available addenda through Continuation 57).
- Reused the established C278 archive-contract regression PASS; no rerun.
- Skipped completed NSE raw archive QA, canonical panel rebuild, CDSL repeated archive retry, export Phases 4–6 and prior source-route adjudication. No duplicate Library upload.
- The current Mother File is a curated continuity record through C57, not a verbatim transcript of every continuation; missing chat detail remains UNKNOWN.

## 2. Selected task
Continue the only executable technical source task from C279: establish whether a documented official FBIL/RBI USD/INR historical daily source can be captured without third-party proxies, credentials, or terms circumvention.

## 3. New official-source evidence
- RBI Reference Rate Archive was reopened: https://www.rbi.org.in/Scripts/ReferenceRateArchive.aspx. It visibly exposes USD selection, From/To date fields and an Excel download control. The accessible page representation does not expose the form submission request or downloadable workbook bytes.
- RBI's official explanation states that FBIL assumed computation and dissemination of USD/INR and other major-currency reference rates from 10-Jul-2018; RBI discontinued its own daily publication after 09-Jul-2018: https://www.rbi.org.in/scripts/FS_RTI_Diclosure_Logs.aspx?fn=6 and https://www.rbi.org.in/commonman/Upload/English/PressRelease/PDFs/PR3504072018.PDF.
- IMF SDDS metadata for India states that FBIL USD/INR reference rates have been disseminated daily since 10-Jul-2018 and that historical data pertaining to this series from 10-Jul-2018 are available on the FBIL website: https://dsbb.imf.org/sdds/dqaf-base/country/IND/category/EXR00.
- IMF metadata specifies the reference-rate calculation uses actual spot USD/INR transactions in a 11:30–12:30 IST electronic-platform window, with a randomly selected 15-minute window; the daily rate is published on Mumbai business days. This is a benchmark observation, not OHLC, DXY, or a carry measure.
- FBIL's official website search rendering exposes recent daily INR/1 USD observations and archive navigation for other benchmark families: https://www.fbil.org.in/. Its JavaScript-rendered landing page has no readable lines in the available page interface; no exact historical USD/INR download endpoint, request schema, or workbook was captured.
- FBIL's official methodology PDF confirms the transaction-based calculation: https://www.fbil.org.in/uploads/FBIL_REFERENCE_RATE_FINAL_fa318d5727.pdf.
- An IMF metadata statement that history is available and a current FBIL daily page are source-availability evidence only; they do not prove this task has acquired or validated the historical raw data.

## 4. Capture attempt and exact limitation
- Reopened the official RBI archive in the available web interface. It rendered the input controls and Excel image link, but did not provide an executable form-submit/postback interaction or the actual workbook response.
- Opened the official FBIL landing page. It is client-rendered and returned no readable page lines; no documented downloadable daily-history endpoint was surfaced by the official page representation.
- Therefore no actual request URL/parameters, HTTP response metadata, workbook bytes, byte count, worksheet names/schema, observation-date count, retrieval timestamp, or SHA-256 can be truthfully recorded.
- No third-party Zenodo/GitHub compiled dataset or paid API was used or promoted. No NSDL terms circumvention or external contact occurred.

## 5. Status and acceptance
- Official source family: CONFIRMED (FBIL daily USD/INR reference-rate series).
- Historical daily availability statement: CONFIRMED by IMF metadata as an official dissemination description.
- Exact auditable historical export endpoint/request: NOT_CAPTURED.
- Raw workbook bytes and SHA-256: NOT_CAPTURED.
- Row-level QA and >=60 distinct valid dates spanning >=90 calendar days: NOT_RUN / NOT_VERIFIED.
- USD/INR ingestion: BLOCKED / UNKNOWN; do not mark PASS or AVAILABLE.
- Macro-Geo P0 remains 6/8 on the last artifact-backed inventory. Strict GCR hard gate remains BLOCKED; candidate_release_allowed=false; overall GCR remains NOT_COMPUTABLE / NOT_CERTIFIED.
- FPI/DII remains a separate blocker: NSDL terms/reuse-permission issue from C279 remains unresolved. No FPI/DII substitution or data ingestion was attempted.

## 6. Next executable handoff
The remaining step requires the official FBIL/RBI historical Excel export itself. User/authorized operator should download the USD historical date-range workbook directly from the official RBI/FBIL UI and attach that exact original file in this conversation. Then validate its workbook structure, source attribution, date span, >=60 distinct valid dates over >=90 calendar days, duplicates/missing dates, numeric values, units, and SHA-256. Preserve the original bytes and record exact retrieval metadata. Do not infer missing values or fill gaps. If the workbook cannot be downloaded, provide the visible error or exact UI outcome; keep BLOCKED.

## 7. Protected invariants
₹0 spend; official/free sources only; no third-party proxy promotion, synthetic rows, fabricated timestamps, interpolation, forward-fill, credential bypass, or external contact. UNKNOWN is neither PASS nor FAIL. H+3 State calibration remains >=50 matured observations per state. CORE-672 (56×12), Engines A–E, Production Selector, RANKING_SCORE, +1 PRESSURE_FADE and IPO-PLX V2.0 unchanged. No production integration, merge, threshold change or broad workflow run.
