# Brazil Registration History — Part 7 (2026-11-19)

## Scope
Public IMF SDMX Central Registration URN history for the exact Brazil registration object:
- Registration URN: `urn:sdmx:org.sdmx.infomodel.registry.Registration=IMF:D429E36CD161E2F2A34ECAF137994E89(1.0)`
- Registration ID: `D429E36CD161E2F2A34ECAF137994E89`
- Provision Agreement: `IMF:BR_BOP_BP6(1.0)`
- Data Provider: `IMF:BR1`
- Registered BCB URL: `https://www.bcb.gov.br/content/statistics/sddsdocuments/4%20External%20Sector/Ext%201%20IMF%20SDMX%20BOP%20BPM6.xml`

## Independent capture and validation
- Workflow run: [44465947951](https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/44465947951)
- Artifact ID: `14502380926`
- Artifact ZIP SHA-256: `2a3266a0c2d3e1948955e9de789c2a3f9acb5ecd12ffca42cd54bbad0bb37f41`
- History response: 2,131 bytes; SHA-256 `23fe31fafad2f08bfe63473d4f45792365f92c53f3a27b6158472f0c8e232072`.
- 40/40 history events retrieved; 40/40 transaction item ZIPs HTTP 200; 40/40 embedded SDMX-ML 2.1 XML documents parsed.
- Registration ID, PA reference and BCB URL each match 40/40.
- Global transaction index cross-check: 38,668 records (IDs 1–38,668); 40/40 history IDs found; 40/40 millisecond timestamps and 40/40 Registry Action values exactly match. Index raw SHA-256 `74725cb58eb6d612e67e7af41df870edaa58f81e95b5ba1c4c3713ccb72ae709`.

## Action semantics — preserve both layers
- Registry history Action: `Replace` on all 40 events.
- Embedded SDMX `RegistrationRequest@action`: `Information` on all 40 payloads.
- These are separate fields from separate layers; this report does not treat them as equivalent.
- The global transaction index's Type is present as `Registration` for tx667 only; the other 39 Type fields are absent and remain missing/UNKNOWN.

## Date range
- First transaction: ID 667, 2023-09-22T09:42:16.389Z.
- Latest transaction returned: ID 37877, 2026-10-26T11:47:33.098Z.
- Registration.lastUpdated is recorded separately and is not substituted for the transaction timestamp.

## Reproducible data
- Machine-readable 40-event index: `docs/evidence/IMF_BRAZIL_REGISTRATION_HISTORY_40_EVENTS.csv`.
- Original Registration submission (tx667): `docs/evidence/IMF_BRAZIL_REGISTRATION_TX_00667.xml`.
- Full raw transaction ZIPs/XMLs remain in GitHub Actions artifact `14502380926` (90-day retention); re-download before expiry if a byte-identical archive is needed.

## Remaining blockers
- PA structure transaction ID 2 / PA Changelog payload was not retrievable from the tested endpoints (HTTP 500 full transaction; HTTP 400 PA/Dataflow/DSD/Provider item downloads).
- Dataflow IDs `IMF:BOP6(1.0)` and `IMF:BOP_BPM6(1.0)` remain distinct despite sharing DSD `IMF:ECOFIN_DSD(1.0)`.
- Existing contract reconciliation remains authoritative: BOP6 constraint accepted 234/237 payload indicators; BOP_BPM6 constraint accepted 27/237. No identifier rewrite or admission.
