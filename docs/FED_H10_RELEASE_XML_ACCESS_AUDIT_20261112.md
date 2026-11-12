# Federal Reserve H.10 release XML access audit — 2026-11-12

## Verified official route

The Federal Reserve Board H.10 release landing page exposes an explicit **XML** link. Following that link resolves to:

- Landing page: https://www.federalreserve.gov/releases/h10/
- XML/ZIP target: https://www.federalreserve.gov/releases/h10/data/FRB_h10_xml.zip
- Link evidence: the XML link is link 17 on the official H.10 release page as inspected on 2026-11-12.
- Source owner: Board of Governors of the Federal Reserve System.
- Format advertised by the release page: XML download; resolved object filename is `FRB_h10_xml.zip`.

The Federal Reserve's DDP Choose page currently also exposes a 26.1 MB single-XML ZIP package and states that the Build Your Package feature is being removed in preparation for DDP retirement. The H.10 release landing page separately links XML, making it the better official release-page route to investigate for a future collector.

## Access test result

- Official landing page retrieval: VERIFIED.
- XML link target resolution: VERIFIED from the official page link.
- Browser binary retrieval: NOT AVAILABLE in the current research browser; the response was rejected because its content type was `application/x-zip-compressed`.
- Independent raw-byte download: FAILED in the current execution environment.
- Actual downloaded byte count: NOT AVAILABLE.
- Actual archive SHA-256: NOT AVAILABLE.
- ZIP CRC/member inspection: NOT RUN.
- XML/SDMX parsing and observation extraction: NOT RUN.

A rejected binary response is not evidence that the official URL is invalid. Equally, a verified hyperlink is not evidence that this repository has downloaded or ingested the archive.

## Collector recommendation

Use the exact official release-page URL as the next candidate source for a dedicated H.10 release XML collector. Before changing the production source URL, require a successful raw-byte download, exact HTTPS origin validation, ZIP CRC/member checks, SHA-256 manifest, and independent XML parsing. Keep raw bytes immutable and retain release/vintage metadata.

The archive contains daily FX indices and bilateral FX rates; it is not portfolio-flow data. The Fed Broad Dollar Index must not be relabelled as ICE DXY.

## Current status

`OFFICIAL_XML_LINK_VERIFIED_RAW_DOWNLOAD_BLOCKED_NO_INGESTION_CLAIM`

No production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engine A–E, or Hard Gate changes are made. No PR is merged.
