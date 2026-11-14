# FPI/DII Source Semantics Reconciliation — 2026-11-14

## Source observations (official)
- NSE FII/FPI & DII trading activity page, 13-Nov-2026: NSE-only FII/FPI buy 17,376.50, sell 12,122.52, net +5,253.98 INR crore; NSE-only DII buy 10,561.32, sell 12,532.05, net -1,970.73 INR crore.
- Same page, combined NSE+BSE+MSEI 13-Nov-2026: FII/FPI buy 18,339.57, sell 12,603.02, net +5,736.55 INR crore; DII buy 11,745.95, sell 13,999.53, net -2,253.58 INR crore.
- NSE explicitly calls these trade-based values provisional and subject to custodial confirmation, modifications, expiry physical settlement and classification effects. Source: https://www.nseindia.in/reports/fii-dii?os=0
- CDSL daily FPI page displayed reporting date 12-Nov-2026: equity exchange net +14,678.72 INR crore; equity primary/other +15.00; equity subtotal +14,693.72. Debt-General subtotal +445.65; Debt-VRR subtotal -173.22; Debt-FAR subtotal +1,022.81. Source: https://www.cdslindia.com/eservices/publications/fiidaily
- CDSL notes custodian-reported trades on and up to previous trading day(s), and that primary/other covers corporate actions as well as primary-market transactions. CDSL archive presents multiple dated historical rows; current archive page is not yet a hashed historical acquisition. Source: https://www.cdslindia.com/Publications/ArchiveDataAfter2009.aspx
- Official NSE report archive offers historical equities FII/FPI and DII report surface: https://www.nseindia.com/static/all-reports/historical-equities-fii-fpi-dii-trading-activity

## Arithmetic QA
- NSE NSE-only FII/FPI: 17,376.50 - 12,122.52 = 5,253.98.
- NSE combined FII/FPI: 18,339.57 - 12,603.02 = 5,736.55.
- NSE NSE-only DII: 10,561.32 - 12,532.05 = -1,970.73.
- NSE combined DII: 11,745.95 - 13,999.53 = -2,253.58.
- CDSL 12-Nov equity exchange: 32,887.51 - 18,208.79 = 14,678.72; adding primary/other +15.00 = 14,693.72.
- Differences between 13-Nov NSE and 12-Nov CDSL cannot be attributed to revisions or foreign-flow reversals: dates, population, routes and status differ.

## Required canonical schema and no-lookahead rules
- Preserve source, source URL, raw file hash, retrieval UTC, report publication UTC if supplied, source-native reporting date, trade date if explicitly known, exchange universe, investor category, asset class, investment route, buy, sell, net, currency, units, preliminary/final status and revision/version.
- Use distinct keys: (source, reporting_date, trading_date_if_verified, exchange_universe, investor_category, asset_class, route, status, version). No date-only joins or additive merging of NSE and CDSL rows.
- Never sum CDSL equity subtotal with its stock-exchange and primary/other components (double count).
- Never add NSE-only and combined-exchange flows (overlap).
- Never use custodian-confirmed later reports in earlier trading decisions; enforce as-of availability at each decision timestamp.
- Provisional NSE and custodian CDSL are separate observed series. Cross-source reconciliation is a hypothesis until exact same underlying trading date, scope, route and version are confirmed.
- Any absent publication timestamp, trading-date mapping or version is UNKNOWN; no assumed T+1 and no backfilled synthetic timestamps.

## Outcome
- Official source definition / arithmetic audit: PASS for these observed snapshot rows.
- Same-date, same-universe source reconciliation: NOT RUN.
- Historical raw archive bytes, manifests and SHA-256: NOT CAPTURED in this task.
- Rolling FPI/DII-to-NSE sector return study: NOT RUN.
- Production selector and ranking untouched; Hard Gate BLOCKED.
