# Corporate Events P0 — Official Source Access Audit
Date: 2026-11-14
Status: PARTIAL SOURCE DISCOVERY; P0 remains BLOCKED.

## Objective
Resolve the missing eighth Macro-Geo P0 group, `corporate_events`, which the exact Macro-Geo Run 210 artifact reports as BLOCKED because it contains 0 valid official rows satisfying the required symbol, subject, publication timestamp, and source URL fields.

## Official source evidence
1. NSE Corporate Filings landing page:
   - URL: https://www.nseindia.com/companies-listing/corporate-filings-application?id=allAnnouncements
   - Observed on 2026-11-14: page displayed 5 Corporate Announcements, 0 Corporate Actions, and 413 Board Meetings.
   - Latest announcement rows displayed:
     - RELIGARE — Monitoring Agency Report — 14-Nov-2026
     - FUSIONCX — Outcome of Board Meeting — 14-Nov-2026
     - KOTHARIPET — Amalgamation/Merger — 14-Nov-2026
     - KOTHARIPET — Shareholders meeting — 14-Nov-2026
     - SENCO — Investor Presentation — 14-Nov-2026
   - This overview confirms symbol, subject, and broadcast date at page level, but does not expose exact publication time or event-specific source/attachment URL in the rendered summary.

2. NSE Corporate Filings application page:
   - URL: https://www.nseindia.com/companies-listing/corporate-filings-application
   - Observed latest-activity dashboard displayed 673 Corporate Announcements, 26 Corporate Actions, and 535 Board Meetings, with latest rows dated 13-Nov-2026.
   - Counts differ from the allAnnouncements-filtered page above; do not reconcile or merge these page counts without capturing the exact page filters and query snapshot.

3. NSE Announcement XBRL page:
   - URL: https://www.nseindia.com/companies-listing/corporate-filings-announcements-xbrl
   - Rendered result exposes columns SYMBOL, COMPANY NAME, Event/Subject, DETAILS, ATTACHMENT, TYPE OF SUBMISSION, and BROADCAST DATE/TIME.
   - Sample rendered rows include broadcast timestamps with seconds and attachment metadata. This demonstrates the required timestamp and attachment fields exist in at least this XBRL view, but the currently rendered rows are dated 28–29 Oct 2026 and do not establish complete daily coverage or the normal-announcements schema.

4. NSE RSS feed catalogue:
   - URL: https://www.nseindia.com/static/rss-feed
   - NSE describes RSS feeds for Announcements, Board Meetings, Corporate Actions, Financial Results, Insider Trading, Shareholding Pattern, and other corporate information. NSE states RSS provides the latest information posted on its website.
   - Exact announcement-feed URL and historical backfill/retention limits were not resolved in this audit.

## Candidate interface — NOT promoted to verified source contract
A third-party technical article describes a public NSE JSON route:
`https://www.nseindia.com/api/corporate-announcements?index=equities&from_date=DD-MM-YYYY&to_date=DD-MM-YYYY`
and reports fields including `seq_id`, `symbol`, `desc`, `an_dt`, `exchdisstime`, and `attchmntFile`.
This is an undocumented interface described by a non-official source. Direct retrieval through the available web reader was unsuccessful. Therefore:
- endpoint existence and live response schema are NOT VERIFIED in this audit;
- no rows, row counts, timestamps, or attachment URLs are accepted from the third-party article as project data;
- do not bypass CAPTCHA, access controls, or anti-bot restrictions;
- do not treat an undocumented endpoint as a stable production source until independently validated against NSE's own page/RSS and dated filing documents.

## Field-level acceptance matrix
| Required evidence | Current result | Reason |
|---|---|---|
| Official source identity | PASS | NSE-owned filing pages and RSS catalogue identified |
| Symbol | PARTIAL | Visible in latest-announcement overview |
| Subject | PARTIAL | Visible in latest-announcement overview |
| Publication timestamp | PARTIAL / UNKNOWN | Timestamp field exists in XBRL view, but not verified for the current normal-announcement feed over a controlled date range |
| Event-specific source URL | PARTIAL / UNKNOWN | Attachment column exists; event-level URL was not captured and hashed |
| Historical date-range completeness | UNKNOWN | No controlled full-range extraction or reconciliation |
| Raw response/file bytes and SHA-256 | BLOCKED | No raw official response/archive acquired |
| Symbol/issuer/ISIN bridge | UNKNOWN | No raw row set to reconcile |
| Corporate Events P0 valid rows | BLOCKED | No qualifying row has been admitted to the evidence archive in this audit |

## Safe next procedure
1. Resolve the official NSE RSS Announcements feed URL from the NSE catalogue and test only a normal public read; record HTTP/result metadata and raw bytes where accessible.
2. Independently validate one normal announcement and one XBRL announcement against the NSE filing page, preserving the exact symbol, subject, broadcast timestamp, attachment/source URL, filing identifier, and original timezone.
3. If a documented/official route supports a date range, perform a narrow one-day test first, deduplicate on the exchange filing identifier, then reconcile row counts with the NSE page.
4. Archive original unmodified bytes and SHA-256 before parsing. Record parser/schema version, source URL, retrieval timestamp, and row-level provenance.
5. Only mark rows valid when symbol, subject, publication timestamp, and source URL are all present and verified. Missing fields remain UNKNOWN; do not infer or synthesize.
6. Re-run the existing Macro-Geo P0 validation only after a real archived input exists; do not modify the production selector, ranking score, pressure-fade rule, 672 diagnostics, or Hard Gate.

## Invariants and exclusions
Research-only. No paid API, paid feed, spend, external contact, workflow rerun, PR, merge, production integration, or synthetic data. No prior PASS evidence is replaced. The Macro-Geo Run 210 artifact remains the controlling baseline: P0 7/8 and corporate_events BLOCKED.
