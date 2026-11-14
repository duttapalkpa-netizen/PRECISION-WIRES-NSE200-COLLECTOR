# NSE RSS 35 linked-attachment inventory audit — 2026-11-14

## Scope and input provenance
Built a row-preserving inventory from the exact `announcements.jsonl` member of GitHub Actions run `43558025207`, artifact ID `14098814399`. Source member SHA-256: `fa17c0c89ebc10321821aa54fe5f5eaf7c488ddbd2e3a4d32ac0aa2e49c9b60d`. Original 190 RSS records retained as source; this inventory contains only the 35 records with non-empty source links.

## Completed inventory
- 35/35 linked RSS rows inventoried.
- 35/35 links are the exact original strings from RSS; no URL was constructed or normalized.
- 35 distinct link URLs.
- 33 PDF links and 2 XML links.
- 20 distinct issuer-title strings; repeated disclosures remain separate rows.
- Each inventory row preserves source record index, original issuer title, original pubDate, original description, exact URL, exact filename, extension, filename-leading token candidate, and explicit content/symbol validation states.
- CSV output: `NSE_RSS_35_linked_attachment_inventory_20261114.csv`.
- CSV size: 15,648 bytes.
- CSV SHA-256: `ba60e2859990be59f5f1a573ffccb4dfab6f498e5042d3bb5ab5ec8c4ad066ef`.

## Access/validation attempts and boundaries
- All 35 URLs are in the original RSS as `https://nsearchives.nseindia.com/corporate/...`; this proves source-domain string provenance only, not that every link resolves.
- Direct page-open checks were attempted for both XBRL/XML URLs, one Coal India PDF, and one Oriana results PDF. The web retrieval path could not retrieve the two XMLs or Coal India PDF; the Oriana PDF response was rejected because the document was too large (12,488,688 bytes). These outcomes are retrieval-tool limitations, not proof of broken source links.
- No attachment response status, final redirect URL, MIME header, byte count, downloaded bytes, PDF text, XML parse, or attachment SHA-256 is claimed for any of the 35.
- Therefore attachment-content validation remains 0%; no event type, result figures, issuer legal identity, or stock symbol is promoted from filenames alone.
- NSE official All Reports page and NSE market-data documentation establish that daily MII/security-master files and equity reports are published through NSE channels, but the current public security-list page does not provide a dated historical MII payload URL in this audit. No guessed direct URL was used.

## Safe next step
Use the exact 35 original links in an isolated, bounded acquisition job that records per-URL status, redirect, content type, byte count, SHA-256, and parse result; enforce size/time limits and preserve failures as UNKNOWN. For 2 XML files, validate XML well-formedness and issuer identifiers; for 33 PDFs, extract text/metadata and validate issuer/legal name and disclosure date. Only after this, reconcile each issuer against an official dated NSE MII/security master using the composite key `TckrSymb + SctySrs + ISIN`. Do not change selectors, ranking, diagnostics, or Hard Gate.

## Status
- Linked-row inventory: 100%.
- Exact-link and filename preservation: 100%.
- File-extension inventory: 100%.
- Live attachment retrieval/response metadata: 0% / NOT VALIDATED.
- PDF/XML content validation: 0% / NOT VALIDATED.
- Official issuer-symbol mapping: 0% / UNKNOWN.
- Event-to-price join and matured H+1/H+3/H+5 study: 0% / BLOCKED.
- No code, source data, selector, ranking, diagnostic, workflow or production behavior changed; no PR/merge.
- Overall project: NOT CALCULABLE; Hard Gate BLOCKED.

## Official source references
- NSE All Reports: https://www.nseindia.com/all-reports
- NSE Securities Available for Trading: https://www.nseindia.com/static/market-data/securities-available-for-trading
- NSE Equity market-data report documentation: https://www.nseindia.com/static/products-services/equity-market-data-reports-download
