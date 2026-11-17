# CDSL reporting-date correction and H.10 access-route change — 2026-11-17

Scope: correction to prior research notes; fail-closed source verification. Research branch only.

## 1. CDSL 17-Nov claim withdrawn

A fresh inspection of the official CDSL Daily Trends page on 2026-11-17 shows the latest displayed investment report as **16-NOV-2026**, not 17-NOV-2026.
Official page: https://www.cdslindia.com/eservices/publications/fiidaily

Displayed confirmed custodian/depository values for 16-Nov-2026:
- Equity: +₹5,564.90 crore
- Debt-General: +₹389.47 crore
- Debt-VRR: +₹51.60 crore
- Debt-FAR: -₹1,163.67 crore
- Hybrid: +₹3.63 crore
- Five-category FPI subtotal: +₹4,845.93 crore
- Mutual Funds (separate category): -₹18.74 crore
- Page total including Mutual Funds: +₹4,827.19 crore

The page states that these figures are based on custodian reports submitted to depositories on 16-Nov-2026 and constitute trades conducted on and up to previous trading day(s). They are not intraday T-day execution data.

**Correction:** Any previous note or assistant response asserting a CDSL 17-NOV-2026 investment reporting date and values (+₹5,107.61 crore equity etc.) is unsupported by the official page inspected in this audit and is withdrawn from accepted evidence. Do not ingest or cite those figures. This correction supersedes the previous GLOBAL_CAPITAL_ROTATION_CDSL_H10_FRESHNESS_CHECKPOINT_20261117.md CDSL section; retain that file for audit history but treat its claimed 17-Nov snapshot as REJECTED / NOT_VERIFIED.

The official archive page surfaced through 06-Nov-2026 in the current extraction; it is not proof of a complete daily raw archive through 16-Nov.

Status:
- Official live page visible reporting date 16-Nov: VERIFIED_OFFICIAL_PAGE_SNAPSHOT.
- Arithmetic for values shown: PASS.
- 17-Nov investment reporting-date claim: REJECTED / WITHDRAWN.
- Raw response bytes, final data URL, response headers, retrieval timestamp, byte count, SHA-256: NOT_DONE.
- Historical complete daily CDSL panel: NOT_DONE.

## 2. Fed H.10 route change and valid acquisition path

Official Federal Reserve DDP Choose page: https://www.federalreserve.gov/datadownload/Choose.aspx?rel=H10

The page reports the H.10 release last released Monday, 16-Nov-2026 and offers preformatted H.10 daily indexes (CSV, last 10 observations) and daily rates (CSV, last 10 observations). It also lists a single XML download for all G.5/H.10 data (SDMX/ZIP, 26.2 MB).

Official DDP/FRED partnership notice: https://www.federalreserve.gov/data/data-download-fred-information.htm

The Federal Reserve states on 12-Nov-2026 that Build Your Package was retired; preformatted package options are scheduled for retirement on 31-Mar-2027, and the DDP site for 01-Jul-2027. Historical XML remains available on Board statistical release pages. FRED API v2 provides full historical DDP series but requires a FRED user account/API key for programmatic API access; do not assume anonymous API access.

H.10 broad index:
- Series ID: H10/H10/JRXWTFB_N.B
- Description: Nominal Broad Dollar Index
- Unit: Index, January 1997=100
- Not ICE DXY.
- Preview as of 13-Nov-2026 includes ND on 11-Nov. The current 20-row preview does not supply 21 valid observations for a 20-interval return.

Status:
- Official route and retirement announcement: VERIFIED.
- Full H.10 historical raw XML/CSV bytes captured in this audit: NOT_DONE.
- 21-valid-observation window and 20-interval return: NOT_DONE.
- fed_broad_usd_change_pct_20d remains UNKNOWN.

## 3. Next action / no false PASS
1. Use the official Board statistical release XML download or a FRED account/API key if the user chooses to create one; preserve exact raw bytes, final URL, retrieval timestamp, byte count, SHA-256 and release vintage.
2. Capture official CDSL daily source bytes and complete date coverage; do not treat displayed HTML as a raw CSV archive.
3. Continue to keep IMF BOP_AGG transactions separate from positions; no observations are admitted until actual payload and series mapping are verified.
4. No synchronized panel, relative-attraction output, event study or predictive validation is accepted yet.

No production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A-E, or PR merge changed.