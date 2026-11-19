# IMF legacy BOP registry ID probe — verified negative result (2026-11-19)

## Objective
Determine whether the exact legacy Data Portal identifiers are publicly retrievable from IMF SDMX Central. This is a registry-location test only; it does not establish that the Data Portal identifiers or dataflow are absent from IMF Data.

## Official API contract
The IMF SDMX Central Web Services Guide (updated May 2025) identifies the public structure-service entry point as `https://sdmxcentral.imf.org/sdmx/v2/`, describes structure queries and their URL construction, and gives `/structure/...` as the structure-query family. The web UI independently shows the same entry point. This differs from the IMF Data API portal, which advertises SDMX 2.1/3.0 APIs and an authenticated Swagger exploration route.
Sources:
- https://dsbb.imf.org/content/pdfs/IMFSDMXCentralWebServicesGuide.pdf
- https://sdmxcentral.imf.org/webservice/schema.html
- https://data.imf.org/en/Resource-Pages/IMF-API

## Probe 1 — agency path IMF
- Run `44510554257`, run #1, SUCCESS; job `135513379536`.
- Trigger/workflow commit `8f5f650ba0aa15c395073a49de48cc1b3c41328d`.
- Artifact `14522671636`, 1,717 bytes; artifact ZIP SHA-256 `847f0930bc9ee625c01dd1d3c7bb71d10a0063e927d6bad948515a6031def01e`.
- DSD `IMF/DSD_BOP/24.0.0` and Dataflow `IMF/BOP/21.0.0`: HTTP 404, SDMX error code 100, text `No Results Found`.
- Each response 421 bytes, SHA-256 `aa0b5827e5185b172e34b7891c2ec205db7502459842237eca92bdd11bc1d87e`.

## Probe 2 — exact agency path IMF.STA
- Run `44510641519`, run #3, SUCCESS; job `135513689116`.
- Script correction commit `282b046000509ce8767f2d4376f220a804905cd4`.
- Artifact `14523605400`, 1,722 bytes; ZIP SHA-256 `ec3eeb726daf1a845fcbe710d4888ffff95ad1ad9bbdc1120aff2f97afb79431`; expiry 2027-02-17.
- DSD `IMF.STA/DSD_BOP/24.0.0` and Dataflow `IMF.STA/BOP/21.0.0`: HTTP 404, SDMX error code 100, text `No Results Found`.
- Each response 421 bytes, SHA-256 `aa0b5827e5185b172e34b7891c2ec205db7502459842237eca92bdd11bc1d87e`.
- Artifact ZIP was downloaded and independently SHA-256 checked against GitHub's digest; both raw XML response hashes and manifest hash were independently computed after extraction. Manifest SHA-256 `04a54cf216bbd595afe6bc7e2d0566cc87881de749242a89e8df0747c7799196`.
- XML parser returned PASS only because the error payload is well-formed XML; root is SDMX `message:Error`, not a DataStructure/Dataflow. This is NOT metadata parse success.

## Conclusion
- Both candidate agency namespaces (IMF and IMF.STA) returned the same explicit SDMX 404 / No Results Found for both exact legacy artefact IDs on the public SDMX Central registry.
- This establishes only that these IDs were not found in this public registry under the tested paths at retrieval time. It does NOT prove the artefacts or dataflow are absent from the separate IMF Data Portal API.
- No DSD/Dataflow metadata capture, codelist/constraint capture, crosswalk, or GNB current-version test has passed. Legacy/current mapping remains BLOCKED/NOT_DONE.
- The earlier `api.imf.org/external/sdmx/3.0/structure` HTTP 400 failure remains separately documented; do not conflate these two services.

## CI isolation learning
- The first research commits accidentally triggered the NSE collector because the collector's `paths-ignore` list initially omitted the new probe script, trigger marker and workflow file.
- Guard commit `66ba13b9f4c3311dae5b977dc3785a32c7c82e39` now ignores all three exact paths.
- Corrected follow-up script commit `282b046000509ce8767f2d4376f220a804905cd4` triggered the research workflow and did NOT trigger the NSE collector in the observed run list. Earlier accidental collector runs remain unrelated to this research; no market data from them was used.
- Before any future research trigger, add its script, marker and workflow paths to collector ignore list before pushing those files.

## Next action
Stop probing the same SDMX Central registry IDs. Use the authenticated IMF Data API Swagger route only if the user's existing public/free access is available; no credentials or API key may be invented or requested here. Otherwise pivot to another official public source or preserve the legacy schema mapping as BLOCKED. No production/backtest admission.
