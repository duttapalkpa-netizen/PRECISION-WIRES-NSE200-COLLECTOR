# Global Capital Rotation — CDSL 17-Nov update and H.10 freshness checkpoint

Audit date: 2026-11-17 (Asia/Kolkata)
Branch: research/global-capital-rotation-overlay-v1
Research-only. No production integration or PR merge.

## 1. CDSL official daily page — new reporting date

Official page: https://www.cdslindia.com/eservices/publications/fiidaily
Retrieved page snapshot: 2026-11-17 (web page inspection); reporting date 17-NOV-2026.

| Category | Gross purchases (INR cr) | Gross sales (INR cr) | Net (INR cr) |
|---|---:|---:|---:|
| Equity | 16,657.30 | 11,549.69 | +5,107.61 |
| Debt-General | 341.86 | 204.63 | +137.23 |
| Debt-VRR | 3.97 | 2,383.64 | -2,379.67 |
| Debt-FAR | 1,168.66 | 1,592.95 | -424.29 |
| Hybrid | 18.66 | 23.40 | -4.74 |
| **FPI subtotal (five above)** | | | **+2,436.14** |
| Mutual Funds (separate category) | 41.41 | 3.73 | +37.68 |
| **CDSL page total including Mutual Funds** | 18,231.86 | 15,758.04 | **+2,473.82** |

Arithmetic verified:
- Equity: 16,657.30 - 11,549.69 = 5,107.61
- Debt-General: 341.86 - 204.63 = 137.23
- Debt-VRR: 3.97 - 2,383.64 = -2,379.67
- Debt-FAR: 1,168.66 - 1,592.95 = -424.29
- Hybrid: 18.66 - 23.40 = -4.74
- Five-category FPI subtotal = 2,436.14
- Mutual Funds are not FPI; do not include +37.68 in FPI subtotal. Page total including MF = +2,473.82.

CDSL says this page is compiled from custodian reports submitted to depositories on 17-Nov-2026 and constitutes trades conducted on and up to previous trading day(s). Therefore the reporting date is not an intraday execution timestamp. The page explains that exchange provisional T-day FPI activity differs from confirmed custodian/depository activity; do not merge them.

Status:
- Official live page and displayed 17-Nov snapshot: VERIFIED_OFFICIAL_PAGE_SNAPSHOT.
- Arithmetic: PASS.
- Raw HTML/CSV response bytes, final raw download URL, response headers, byte count and SHA-256: NOT_DONE.
- Do not claim this is a hashed raw CSV or a fully immutable source archive.

## 2. Federal Reserve H.10 official preview

Official preview: https://www.federalreserve.gov/datadownload/Preview.aspx?pi=400&preview=H10%2FH10%2FJRXWTFB_N.B&rel=H10
Official H.10 DDP review: https://www.federalreserve.gov/datadownload/Review.aspx?filetype=csv&from=&label=include&las%5CtObs=10&layout=seriescolumn&rel=H10&series=122e3bcb627e8e53f1bf72a1a09cfb81&to=&type=package
Series: H10/H10/JRXWTFB_N.B, Nominal Broad Dollar Index; unit Index January 1997=100; multiplier 1.
Preview shows latest observation 2026-11-13 = 122.6503, 2026-11-12 = 122.5433, 2026-11-11 = ND, 2026-11-10 = 122.1143, 2026-11-09 = 121.6623.
DDP review lists 5,445 observations from 2006-01-02 to 2026-11-13 for each of broad, advanced economies, and emerging market economies indexes.

Important limitation: the 20-observation preview from 2026-10-19 through 2026-11-13 includes an ND sentinel on 2026-11-11, leaving only 19 numeric observations in that preview window. It is insufficient to claim a complete 20-interval return, which requires 21 valid observations. Do not substitute the short 10-row uploaded file or the FRED DTWEXBGS index base (Jan-2006=100) for the H.10 index base (Jan-1997=100). The H.10 broad index is not ICE DXY.

Status:
- Official H.10 series identity, unit, latest date/value and available history count: VERIFIED.
- 20-interval return from a complete 21-valid-observation sample: NOT_DONE.
- Downloaded full historical CSV bytes, retrieval timestamp, byte count and SHA-256 in this task: NOT_DONE.
- Keep `fed_broad_usd_change_pct_20d` UNKNOWN until a valid 21-observation window is archived and computed.

## 3. Current acceptance effect

This checkpoint advances only the official page snapshot and arithmetic verification for CDSL and confirms H.10 data availability. It does not complete raw-byte provenance, IMF BOP transactions, synchronized daily panel, relative-attraction calculation, event study, or predictive validation. No composite score, stock ranking, trade trigger, production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, or Engine A-E changes.
