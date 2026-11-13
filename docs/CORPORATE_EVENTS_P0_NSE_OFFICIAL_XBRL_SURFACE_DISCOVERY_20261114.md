# NSE Official Filing Surface Discovery — XBRL Route vs RSS Reconciliation Boundary
Date: 2026-11-14

## Fresh official-source finding
The official NSE Corporate Filings — Announcement XBRL page is publicly rendered at:
https://www.nseindia.com/companies-listing/corporate-filings-announcements-xbrl

A fresh web retrieval on 2026-11-14 exposes the following UI controls and table schema:
- Filters: Announcement Type, Company (company name or symbol), Events / Subject, From, To.
- Download: CSV.
- Pagination: 1–20 of 958 records, 48 pages.
- Visible columns: SYMBOL, COMPANY NAME, Event / Subject, DETAILS, ATTACHMENT, TYPE OF SUBMISSION, BROADCAST DATE/TIME.
- The rendered sample includes exact timestamp fields and separates Exchange Dissemination Time and Time Taken in expanded text.
This is a useful official, structured filing surface and provides richer timestamp/attachment fields than the basic Latest Announcements five-row widget.

## Critical scope distinction
This route is explicitly Announcement XBRL. It must not be treated as the complete general Corporate Announcements feed or as guaranteed to contain every RSS item. Its current rendered sample is dated 28–29 Oct 2026, not the 13–14 Nov RSS snapshot window. Therefore no direct record-level join to the 13 RSS items is claimed here.
The ordinary Corporate Filings page continues to show only a limited Latest Announcements table in the web-rendered snapshot. The 13 RSS items still require date-filtered official row-level evidence.

## Endpoint contract status
- Official page URL and UI schema: VERIFIED.
- Official CSV export affordance: VERIFIED (button visible; no export bytes retrieved in this audit).
- Exact browser request URL, query parameter names, pagination contract and CSV response bytes: NOT CAPTURED.
- No undocumented JSON endpoint inferred from third-party sources has been called or promoted.
- Next safest step: capture the official XBRL page's own CSV export request/response for a narrowly scoped date range that overlaps the RSS pubDate window, record the exact request URL and returned bytes/hash, and verify whether the XBRL subset covers any of the RSS issuer/subjects. Keep the XBRL subset distinct from general announcements.

## Acceptance
| Check | Result |
|---|---|
| Official NSE XBRL page | VERIFIED |
| Table schema incl. symbol/company/subject/attachment/timestamp | VERIFIED |
| Pagination visible | VERIFIED |
| Exact date-window export bytes | NOT CAPTURED |
| RSS 13-item cross-check using this surface | NOT RUN |
| General announcement coverage completeness | UNKNOWN |
| Corporate Events P0 | BLOCKED |

No code or workflow change. No production integration, no PR/merge, no paid service, no synthetic data. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE and CORE-672 unchanged.

Source: official NSE Announcement XBRL page, retrieved 2026-11-14 (web evidence ref `turn672382search5`).
