# BCB Instrument-Level Net Portfolio Investment Series — Metadata & Raw Capture
Date: 2026-11-17
Branch: `research/bcb-priority-metadata-audit-20261117`
Status: METADATA 8/8 VERIFIED; RAW CAPTURE WORKFLOW IMPLEMENTED; RUNTIME PENDING

## Why these eight series
The official BCB BPM6 theme hierarchy lists the following instrument-level net series beneath portfolio-investment assets/liabilities:
- 22909: equities, assets.
- 22912: investment funds, assets.
- 22915: debt securities, assets.
- 22927: equities, liabilities.
- 22936: investment funds, liabilities.
- 22939: debt securities, liabilities.
- 22942: debt securities, liabilities, domestic market.
- 22945: debt securities, liabilities, external market.

Official hierarchy: https://dadosabertos.bcb.gov.br/pages/temas
Each selected dataset page identifies BCB/Dstat as source, monthly frequency, USD millions, source SGS, start date 1995-01-01, and BPM6 / financial-account / portfolio-investment taxonomy. The pages also state publication timeliness up to four weeks after the reference period.

## Raw capture implementation
- Script: `scripts/research/capture_bcb_instrument_net_sgs_csv.py`
- Workflow: `.github/workflows/bcb_instrument_net_sgs_raw_capture.yml`
- Allow-list restricts the downloader to the eight codes above.
- Captures raw CSV bytes, response headers/status, final URL, UTC retrieval start/end, byte length and SHA-256; rejects empty/HTML responses and validates UTF-8.
- 8-minute timeout; artifact upload with `if: always()`; 90-day retention.
- No net/component calculations or sign transforms occur in the capture stage.

## Reconciliation gates (not assumed)
- Asset instrument net sum vs 22906: NOT_DONE.
- Liability instrument net sum vs 22924: NOT_DONE.
- Liability debt domestic + external vs 22939: NOT_DONE.
- Exact child coverage and vintage comparability: NOT_DONE.
- Instrument-level country-period cross-check: NOT_DONE.
- Production integration: NOT_AUTHORIZED.

## Next action
Inspect the push-triggered run and artifact. Only after all eight raw files and SHA-256 values pass should a separate parser test the three instrument identities. Do not assume a sum identity or apply sign corrections without official methodology and full-period tests.
