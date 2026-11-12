# Company Disclosure Screening — Hindustan Copper / NIC-2 Mapping Gate

Recorded: 2026-11-05
Status: OFFICIAL DISCLOSURE IDENTIFIED; NIC-2 EXPOSURE NOT VERIFIED; NO MAPPING ROW PROMOTED

## Purpose
Advance the company-to-NIC-2 evidence intake using an actual NSE Integrated Filing, without guessing a manufacturing-only exposure or treating a document-generation timestamp as the exchange publication timestamp.

## Primary-source observations
1. NSE iXBRL Integrated Filing for Hindustan Copper Limited:
   https://nsearchives.nseindia.com/corporate/ixbrl/INTEGRATED_FILING_INDAS_184391_10082026135400_iXBRL_WEB.html
   - NSE symbol: HINDCOPPER
   - ISIN: INE531E01026
   - Company name: Hindustan Copper Limited
   - Filing reports "Single segment".
   - The disclosed single-segment activity describes mining and processing copper ore into copper concentrate, and manufacturing continuous copper wire rods.
   - The filing's own segment disclosure does not split segment revenue between mining and manufacturing activities.
   - Search/index evidence reference: NSE official iXBRL filing, indexed as 2026-08-10. The URL-embedded time is not accepted as the official exchange broadcast timestamp.

2. NSE Corporate Integrated Filing — Financials landing page:
   https://www.nseindia.com/companies-listing/corporate-integrated-filing
   - The exchange table exposes symbol, company, quarter end, submission type, audited status, consolidation basis, details/XBRL links, broadcast date/time, revised date/time and revision remarks.
   - The exact matching filing row's broadcast timestamp and any revision history must be captured from the exchange record before point-in-time use.

## Mapping decision
- mapping_status: UNKNOWN (not inserted into the VERIFIED mapping ledger).
- Do not assign the whole company to NIC-2025 manufacturing code 24 from its name or product alone.
- The disclosed single segment combines mining (outside the manufacturing-only NIC-2 cohort used by the September 2026 IIP Statement II-A) and downstream manufacturing. There is no disclosed revenue split in this filing to quantify the manufacturing exposure.
- The mapping must remain excluded from the manufacturing IIP join until a primary source provides a defensible activity/revenue split or a separately verified exposure method.
- Do not infer an equal split, use market-sector labels, or promote a code solely from a concordance table.

## Evidence integrity state
- Source URL and company identity are identified.
- Raw HTML/XBRL binary has not been downloaded and hashed in this task; no source SHA-256 is claimed.
- Exact NSE broadcast timestamp, revision-vintage status, segment revenue share and an approved NIC-2025 code remain unverified.
- Therefore no VERIFIED mapping row is added and no Macro-Geo feature is made available to production or the swing backtest.

## Next acceptance gate
1. Capture the exact NSE Integrated Filing row for HINDCOPPER, including broadcast and revised timestamps, submission type and consolidation basis.
2. Acquire the linked original XBRL/Details payload over verified HTTPS; retain raw bytes, HTTP metadata, retrieval time and SHA-256.
3. Inspect annual report/business activity disclosures for any auditable mining-versus-manufacturing split and effective period.
4. Only if the activity scope and revenue share are directly supported, prepare a human-reviewed NIC-2025 mapping proposal. Otherwise preserve UNKNOWN.
5. Apply the time-safe IIP join only after the above evidence gate; compare against the baseline research arm out of sample.

## Non-changes
No changes to production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, engines A/B/C/D/E, or Hard Gate rules. No synthetic observations, fabricated timestamps, guessed mapping, or paid data services.
