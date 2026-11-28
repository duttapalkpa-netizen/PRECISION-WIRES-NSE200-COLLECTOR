# Federal Reserve H.10 raw-ingestion slice — Milestone 6

Date: 2026-11-11
Scope: research-only raw archive; no production integration.

## Source identity

The Board of Governors of the Federal Reserve System publishes the H.10 Data Download Program. Its public "Download all H.10 data as a single XML file" link resolves to:

- `https://www.federalreserve.gov/datadownload/Output.aspx?filetype=zip&rel=h10`
- Official series identifiers:
  - `H10/H10/JRXWTFB_N.B` — Nominal Broad Dollar Index
  - `H10/H10/JRXWTFN_N.B` — Nominal Advanced Foreign Economies Dollar Index
  - `H10/H10/JRXWTFO_N.B` — Nominal Emerging Market Economies Dollar Index

The DDP package review on 2026-11-11 showed all three series available from 2006-01-02 through 2026-11-06 (5,440 observations each). This is source-page evidence, not evidence that this repository has ingested those observations.

Official source pages:
- Choose: https://www.federalreserve.gov/datadownload/Choose.aspx?rel=H10
- Package review: https://www.federalreserve.gov/datadownload/Review.aspx?filetype=csv&label=include&lastobs=10&layout=seriescolumn&rel=H10&series=122e3bcb627e8e53f1bf72a1a09cfb81&type=package

## Collector contract

`pipeline/collect_fed_h10_raw.py` downloads only from the Federal Reserve HTTPS host, enforces a 40 MiB ceiling, validates ZIP structure and member CRCs, preserves the exact raw ZIP bytes, and writes an append-only JSON manifest with retrieval UTC timestamp, source URL, content type, byte count, SHA-256, series identifiers, frequency, and interpretation limits. It rejects redirects outside the approved host, non-ZIP responses, unsafe ZIP paths, and archive collisions.

The collector intentionally does **not** extract, transform, normalize, or create observation rows. Raw archive success is not observation-ingestion success. The next gate must parse the official XML/SDMX structure, reconcile series/dimension identifiers and units, preserve release/vintage metadata, and validate every observation before adding it to a panel.

## Interpretation boundary

These are DAILY FX INDEX series, not portfolio transactions or holdings. The Federal Reserve Broad Dollar Index is not ICE DXY. They can inform the currency-pressure channel only; they cannot independently establish capital moving into or out of India.

## Status

- Source identity and public bulk route: VERIFIED
- Raw ZIP download from a live workflow: NOT YET RUN
- SHA-256 of an actual downloaded source archive: NOT YET AVAILABLE
- XML/SDMX extraction and schema validation: NOT DONE
- Observation panel and synchronized global macro panel: NOT DONE
- Predictive value: NOT TESTED
- Production integration: NOT AUTHORIZED
