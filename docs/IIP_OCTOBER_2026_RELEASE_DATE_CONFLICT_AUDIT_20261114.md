# IIP October 2026 release schedule — corrected reconciliation
Audit date: 2026-11-14 (Asia/Kolkata)
Supersedes the initial interpretation in this file's first version.

## Corrected finding
The two official dates are **not a substantive conflict**.

1. MoSPI Advance Release Calendar 2026-27, page 7, schedules October 2026 IIP for **28 November 2026**. The calendar's page 9 footnote explicitly states: **“In case of holidays, reports release on next working day.”**
   Official PDF: https://www.mospi.gov.in/uploads/documents/releaseCalender/1793948871564-ARC%202026-27%20updated%20till%20October%202026.pdf
2. PIB/MoSPI September 2026 IIP press release, posted 28 October 2026, paragraph 6, specifies **Monday, 30 November 2026** for October 2026 IIP.
   Official release: https://www.pib.gov.in/PressReleasePage.aspx?PRID=2329475&lang=2&reg=48

28 November 2026 falls on a Saturday; the calendar itself allows movement to the next working day, and the month-specific PIB announcement identifies Monday, 30 November. The two official statements therefore align under the calendar's working-day proviso. Treat **30-Nov-2026 (Monday)** as the operational expected release date, subject to any subsequent official schedule change.

## Correction to prior version
The previous version incorrectly classified the two dates as CONFLICT / UNKNOWN and advised separate 28-Nov and 30-Nov failure checks. That classification is withdrawn. Do not carry the false conflict forward into the acceptance ledger.

## Fail-closed operational decision
- Expected release date: **30-Nov-2026 (officially specified by PIB)**.
- 28-Nov is the calendar's nominal date; its holiday/working-day proviso resolves the apparent difference.
- On 30-Nov, check the official MoSPI/PIB release page and e-Sankhyiki source; do not assume availability merely from the schedule.
- Accept October-2026 vintage only after recording the actual official reference period, publication timestamp, source URL, response metadata, raw-byte SHA-256, schema, row count, and independent consistency checks.
- Do not substitute September 2026 data.
- No production selector, ranking, CORE-672, Engines A-E, Hard Gate, workflow, or production data change.

## Status
- Calendar and PIB schedule reconciliation: **PASS**.
- Expected October 2026 release date: **30-Nov-2026**.
- October 2026 raw data acquisition: **NOT YET DUE / NOT ACQUIRED** as of 14-Nov-2026.
- This scheduling reconciliation does not satisfy monthly IIP acquisition, event-study maturity, or project Hard Gate.
