# NSE Security Master + Company Segment Evidence — Execution Gate
Recorded: 2026-11-05
Branch: fix/iip-41-vintage-audit-clean

## Official-source verification
1. NSE Securities Available for Trading page lists a dedicated "Securities available for Equity segment (.csv)" download. The official page is:
   https://www.nseindia.com/static/market-data/securities-available-for-trading
   The page's CSV download link resolves to the NSE archives host and is the supported public source for the equity universe.
2. NSE Data and Reports Download documentation describes the Securities Master as a report containing security symbol, ISIN, security code and series:
   https://www.nseindia.com/static/products-services/equity-market-data-reports-download
3. NSE Corporate Integrated Filing page exposes financial filings with symbol, company name, quarter end, original/revision status, audited status, standalone/consolidated basis, details/XBRL, broadcast timestamp and revised timestamp:
   https://www.nseindia.com/companies-listing/corporate-integrated-filing
4. NSE filing examples show the Segment Revenue (Income) reporting format, including revenue per segment, total segment revenue and inter-segment revenue. Example source:
   https://nsearchives.nseindia.com/corporate/ixbrl/INTEGRATED_FILING_INDAS_182376_04082026192806_iXBRL_WEB.html

## Repository changes
- `collector/security_master.py` now retains the raw source response, hashes it, validates EQ series symbol/ISIN/company-name uniqueness, emits an enriched security master and preserves the one-column `config/universe.csv` interface.
- `data/reference/security_master_manifest.json` will contain retrieval timestamp, exact source URL, HTTP status, byte count, SHA-256 and row counts.
- `research/data/company_segment_disclosure_evidence_template.csv` captures reported segment label, segment revenue, inter-segment revenue, revenue share, verbatim activity, filing broadcast timestamp, source URL/ID and source SHA-256.
- `research/data/company_nic2_exposure_mapping_template.csv` remains the adjudicated mapping ledger. Segment disclosure and NIC assignment are separate stages; do not auto-promote a candidate NIC code to VERIFIED.
- `.github/workflows/nse_security_master_audit.yml` now includes a 5-minute bounded audit, push validation for this branch, manual dispatch, and weekday schedule. GitHub scheduled workflows run only from the repository default branch; the weekday schedule becomes active only after this workflow is merged to the default branch.

## What is not yet established
- The live NSE CSV binary has not been acquired in this assistant session; no raw-source SHA-256, row count or security-master artifact is available yet.
- The GitHub Actions workflow has not been executed from this session; no run ID, artifact ID or CI PASS is claimed.
- No actual company-to-NIC-2025 mapping rows have been created. A segment label is not automatically equivalent to a NIC-2025 class. Human/source adjudication is required, including multiple segment handling and effective dates.
- No stock-level Macro-Geo/IIP join or H+1/H+3/H+5 uplift is claimed.

## Required completion evidence
1. Successful workflow run ID and downloaded artifact.
2. Original NSE equity CSV, raw SHA-256 and manifest cross-check.
3. Enriched SYMBOL/ISIN/company master and exact one-to-one identity QA.
4. Segment filing documents with broadcast timestamp and source SHA-256.
5. Independently adjudicated NIC-2025 code and segment revenue share, with UNKNOWN retained wherever evidence is insufficient.
6. Time-safe join QA at the actual decision cutoff.

## Guardrails
No paid APIs, no fabricated data, no guessed mappings, no backdating, no production selector/score/672 diagnostic changes, and no relaxation of Hard Gate.
