# IIP October 2026 release-date conflict audit
Audit date: 2026-11-14 (Asia/Kolkata)
Scope: official publication schedule only; no data acquisition or production change.

## Finding
Two official MoSPI/PIB publications currently state different release dates for October 2026 IIP:

1. MoSPI Advance Release Calendar 2026-27, updated through October 2026, page 7: October 2026 IIP is listed for **28 November 2026**.
   Source: https://www.mospi.gov.in/uploads/documents/releaseCalender/1793948871564-ARC%202026-27%20updated%20till%20October%202026.pdf
2. PIB/MoSPI September 2026 IIP press release, posted 28 October 2026, paragraph 6: October 2026 IIP release is stated as **Monday, 30 November 2026**.
   Source: https://www.pib.gov.in/PressReleasePage.aspx?PRID=2329475&lang=2&reg=48

Both are primary official sources. The calendar is the later schedule publication (updated through October), but the press release is the month-specific announcement. Without a further official correction/clarification, do not silently choose one date or overwrite the other.

## Fail-closed operational decision
- Release date status: **CONFLICT / UNKNOWN**.
- Collector scheduling: prepare a lightweight availability check for both 28-Nov and 30-Nov; do not trigger a release-missing failure on 28-Nov alone.
- Acceptance: require the actual October-2026 release page/file, its official reference period, publication timestamp, source URL, response metadata, raw-byte SHA-256, and schema/row-count QA before marking October vintage acquired.
- Do not infer that the release has appeared merely because the calendar date arrives; verify the official source.
- Do not use September 2026 data as a substitute for October 2026.
- No changes to Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A-E, Hard Gate, workflows, or production data.

## Status
- Schedule conflict discovery: **PASS** (two conflicting official statements captured).
- Definitive October release date: **UNKNOWN** pending official reconciliation or actual release.
- October 2026 raw data acquisition: **NOT YET DUE / NOT ACQUIRED** as of 14-Nov-2026.
- This audit does not satisfy IIP monthly data coverage or any project Hard Gate.
