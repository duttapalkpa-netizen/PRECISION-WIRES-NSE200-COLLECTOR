# NSE RSS issuer cohort and symbol-candidate audit — 2026-11-14

## Scope and source
Inspected the exact downloaded GitHub Actions artifact from run `43558025207`, artifact ID `14098814399`, whose ZIP SHA-256 is `ca0649032c67fd4519bce66d2dd6cd61805efbd2f9f7f0612fa88b05cedec517`. The parsed `announcements.jsonl` member SHA-256 is `fa17c0c89ebc10321821aa54fe5f5eaf7c488ddbd2e3a4d32ac0aa2e49c9b60d`. This audit is a new classification of the preserved 190-row snapshot, not a repeat of the ZIP-integrity audit.

## Cohort reconciliation
- Total RSS rows: 190.
- `Declaration of NAV` rows: 155; these are mutual-fund/ETF scheme NAV disclosures, not listed-company corporate-event rows. Their titles identify fund/scheme names, and the RSS items have no links. They must be excluded from listed-equity issuer-symbol and corporate-event-to-equity-return joins; preserve them in a separate NAV-disclosure stream.
- Non-NAV rows: 35; all have non-empty official NSE archive links.
- Distinct corporate-issuer titles among those 35 rows: 20.
- These 35 rows represent 20 distinct issuers, with repeated records retained (e.g. Fusion CX 8; Religare Enterprises 3; SRIT India 3; Tamilnadu Telecommunication 3; Kothari Petrochemicals 2; Transteel Seating Technologies 2).

## Filename-derived identifiers — candidates only
The linked filenames contain 22 distinct leading tokens across the 35 non-NAV records. These are source-file naming strings, NOT certified NSE trading symbols:
`AJAX123`, `COALINDIA`, `FUSIONCX`, `GOLDIAM`, `HAIQUE`, `KOTHARIPET`, `OPTIVALUETEK`, `ORIANA`, `PARKMEDIWORLD2025`, `REG30_PARA_B_27796_WebXMLFile`, `RELIGARE`, `SAIIM_2677_WebXMLFile`, `SREEL`, `SRIT`, `SUNSHINE123`, `Sencogold`, `TIMESCAN`, `TNTELE`, `TRANSTEEL`, `VATECH`, `VIAZTYRES`, `VIBHOR`.
Some filenames have non-symbol prefixes or XML document identifiers (e.g. `REG30_PARA_B_27796_WebXMLFile`, `SAIIM_2677_WebXMLFile`); several prefixes carry suffixes or casing that cannot be accepted as exchange symbols. Do not silently normalize, truncate, or promote them to symbols.

## Official master source and limitation
NSE's official “Securities available for Trading” page exposes a downloadable “Securities available for Equity segment (.csv)” and “Changes in Symbols” file. NSE's official market-data documentation describes the Securities Master as containing symbol, ISIN, security code and series. The repository's `collector/security_master.py` also specifies the official `EQUITY_L.csv` source path.
However, the official CSV bytes were not acquired and hashed for this audit, and no dated 14-Nov-2026 historical master snapshot was found in the downloaded RSS artifact. Therefore zero of the 22 filename tokens is marked as an authoritative symbol match in this report. Current/undated master membership would not by itself establish point-in-time symbol identity at the disclosure timestamp; symbol changes and issuer renames need dated history.

## Safe next join design (not applied)
1. Keep all 155 NAV scheme records in a separate NAV disclosure dataset; do not force a stock symbol.
2. For 35 corporate records, preserve title, original description, original pubDate, exact link, filename token and raw record as separate columns.
3. Acquire and hash an official NSE security master plus official symbol/company-name change history valid at 14-Nov-2026 (or the nearest applicable official trading date); preserve raw bytes and retrieval metadata.
4. Match issuer legal names to master company names/ISINs with explicit exact/alias evidence. Treat ambiguous or absent matches as UNKNOWN; do not map from filename token alone.
5. Validate every matched symbol against the corresponding official announcement attachment/XBRL issuer identifier and point-in-time master. Then build the event-to-price join.
6. Keep repeated disclosures as separate event records; any event clustering must be separately specified and auditable.

## Status
- Artifact source/row cohort classification: 100% complete.
- NAV-vs-equity separation for this 190-row snapshot: 100% complete.
- Filename token extraction: 100% complete.
- Official dated security-master acquisition and hash: 0% / NOT RUN.
- Authoritative issuer-symbol mapping: 0% / NOT RUN; UNKNOWN pending evidence.
- Attachment validation and event-to-price join: 0% / BLOCKED.
- No code, data, selector, ranking, diagnostics, workflow or production behavior changed; no PR/merge.
- Overall project: NOT CALCULABLE; Hard Gate BLOCKED.

## Source references
- NSE official securities-available-for-trading page: https://www.nseindia.com/static/market-data/securities-available-for-trading (lists Equity CSV and Changes in Symbols CSV).
- NSE official equity market data/report documentation: https://www.nseindia.com/static/products-services/equity-market-data-reports-download (describes Securities Master fields including symbol, ISIN, security code and series).
- Repository script: `collector/security_master.py`, blob SHA `044e39ceef4dbb05f9e7942514f59aa724efdf9a`.
