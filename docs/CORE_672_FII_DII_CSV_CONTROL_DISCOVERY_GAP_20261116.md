# NSE FII/DII CSV Control Discovery — Parser Contract Finding

Date: 2026-11-16  
Status: **CONFIRMED STATIC DISCOVERY GAP; LIVE HTML PARSE NOT EXECUTED**  
Branch: `research/nse-raw-manifest-retention-20261115`

## Finding

The official NSE report page exposes two separate section headings and two corresponding `Download (.csv)` controls:
1. “FII/FPI & DII trading activity on NSE in Capital Market Segment”
2. “FII/FPI & DII trading activity on NSE, BSE and MSEI in Capital Market Segment”

Official page: https://www.nseindia.com/reports/fii-dii

The committed capture utility's `AnchorParser` records only individual `<a>` hrefs and their own text. The subsequent selector requires the anchor's own label to contain `capital market` and either `fii` or `dii`. The visible NSE page structure places the scope descriptions in section headings and the anchor labels are simply “Download (.csv)”. Therefore, based on the page's rendered structure, the current selector cannot reliably associate the two download controls with their section headings and may return no choices, triggering the intended fail-closed ACCESS_BLOCKED path.

This is a source-level selector mismatch, not proof of a live HTTP failure. The exact raw HTML/DOM and the actual download URLs have not been captured in this session. Do not infer URLs from the rendered page, search snippets, filenames, or guessed API routes.

## Required bounded repair

1. Add a parser that retains heading/section context around each download control, including links and button/input attributes used by the page.
2. Resolve exactly one control for NSE-only and exactly one for NSE+BSE+MSEI using explicit nearby section text; reject missing, duplicate, same-URL, or ambiguous controls.
3. Validate both resolved URLs with the existing HTTPS NSE-domain allowlist.
4. Add offline HTML fixtures based only on captured official page markup, preserving source URL, capture timestamp, and fixture SHA-256. Do not invent fixture attributes or URLs.
5. Once exact raw markup is available from a legitimate capture, add the fixture and tests; only then attempt live capture.
6. Keep both CLI URL overrides as a manual fail-safe, but record that supplied URLs are caller-declared and not independently authenticated merely because the host is NSE.

## Status matrix

- Official page displays two distinct scope headings and CSV download controls: **PASS (rendered page inspection)**.
- Current parser's section-to-control association: **BLOCKED / selector design inadequate**.
- Exact raw page HTML/DOM fixture: **NOT_CAPTURED**.
- Exact two CSV download URLs: **UNKNOWN**.
- Live API + both CSV capture: **NOT_RUN**.
- API-to-CSV reconciliation: **BLOCKED**.
- Production mapping: **NOT_AUTHORIZED / NOT_DONE**.

## Protected invariants

No production pipeline, Production Selector, `RANKING_SCORE`, `+1 PRESSURE_FADE`, CORE-672 56×12, Engines A–E, or collector production workflow changes. No fabricated HTML fixture, guessed URL, synthetic data, or scope inference.


## 2026-11-16 — Second-stage official page link-resolution check

- Re-opened the official NSE page through the available source viewer: https://www.nseindia.com/reports/fii-dii (source reference in research session: `turn984782view0`).
- The extracted page confirms the two section headings at lines 128 and 132 and one `Download (.csv)` control under each at lines 130 and 134. However, the viewer exposes both controls only as the same generic link reference (`17`); it does not expose either underlying href/URL.
- Therefore this second check confirms the scope/control ordering but does not supply the raw HTML, DOM attributes, or exact download URLs. It cannot be used as an HTML fixture and does not resolve the parser gap.
- The web extraction reports a crawl age of approximately three months; treat it as corroborating rendered-page structure only, not a fresh live response or an authenticated download URL.
- Decision: do not click the generic shared link reference as a substitute for the two distinct controls; do not infer a URL. The next executable evidence step requires a raw HTTP capture from an environment that can reach NSE and preserve response bytes/headers. This chat's GitHub connector can read/write repository files but does not provide a workflow-dispatch action; no live runner was triggered in this step.
- Status remains: raw HTML/DOM NOT_CAPTURED; exact CSV URLs UNKNOWN; live capture NOT_RUN; parser repair BLOCKED pending authentic markup.
