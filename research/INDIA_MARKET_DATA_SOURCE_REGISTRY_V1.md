# India Market Data Source Registry — V1

## Purpose
Source-discovery and provenance inventory for PRECISION-WIRES V11.3. This is not evidence that any collector is live or that a source group is covered. All rows begin as DISCOVERED_NOT_LIVE_VALIDATED.

## Remediation order
1. macro_indicators — MoSPI/e-Sankhyiki, MoSPI releases, OGD India, RBI/DBIE.
2. sector_fundamentals — NSE/BSE filings, issuer IR, CEA, PPAC, DPIIT and ministry releases.
3. market_microstructure — NSE, BSE, SEBI, NSDL and CDSL aggregate publications.
4. global_freight_shipping — PPAC, Commerce, OGD and FRED; add ports/shipping sources only after review.
5. fx_carry_and_cross_currency — RBI/DBIE, NSDL FPI, SEBI and FRED.
6. india_bond_yields — RBI/DBIE and RBI releases; benchmark-specific sources only after validation.

## Required observation contract
Preserve DATE/reference period; INDICATOR and source-native ID; VALUE and UNIT; FREQUENCY and relevant geography/sector; RELEASED_AT (source publication timestamp, null if unverified); SOURCE; exact SOURCE_URL; retrieval method; OBSERVED_AT_UTC; revision/vintage and raw checksum where available.

Never substitute OBSERVED_AT_UTC for RELEASED_AT. Never infer missing release times, units, reference periods or values.

## Access and fallback rules
- Prefer official primary sources. OGD India is a discovery/aggregation layer, not a replacement for source-owner verification.
- Prefer public HTML/PDF/CSV/XLS downloads where sufficient and permitted.
- Authentication is endpoint-specific. Do not assume all MoSPI routes require a token or that every route is public.
- Do not bypass login, access controls, rate limits or usage terms.
- Fallback observations are interchangeable only when definition, unit, frequency, geography, reference period and revision vintage match. Otherwise retain separate series and mark the gap.
- Issuer IR material is supplementary; exchange-filed disclosures are the verification anchor.
- Record licence/terms, rate limits, access mode and retention restrictions before scheduling a collector.

## Promotion gate
A source group remains UNKNOWN/PARTIAL/BLOCKED until non-zero live observations, stable typed schema, reference-period and release-time provenance, exact URL, reproducible retrieval, null/duplicate/range/unit/frequency/domain QA, reconciliation where available, and a run artifact/checksum are all evidenced.

This registry does not promote coverage or change the production selector, RANKING_SCORE, +1 PRESSURE_FADE, 672 diagnostics, collector backbone or 200-session dataset. V11.3 hard gate remains fail-closed.

All source entries are candidates pending live endpoint, terms, schema and QA validation. See config/india_market_data_source_registry.csv.
