# NSE Corporate Announcements RSS run 43558025207 — artifact integrity and cohort QA

## Scope
Independent inspection of GitHub Actions run `43558025207`, workflow `NSE Corporate Announcements RSS — isolated read-only acquisition`, branch `research/corporate-events-rss-collector-v1-20261114`, head commit `244348a2a2e0a78370ed97b1e6e1ecd6e22e9dfd`.
This is artifact-level evidence validation for a new run, not a repeat of the earlier static RSS parser/source audit.

## Workflow execution evidence
- Run conclusion: SUCCESS; job `acquire` completed successfully.
- Parser safety/lossless-field unit tests: 5 tests ran, all passed.
- Official bounded acquisition: HTTP 200 from `https://nsearchives.nseindia.com/content/RSS/Online_announcements.xml`.
- Acquisition manifest: `ACQUIRED`, parse status `PASS`, synthetic_data `false`.
- Raw XML: 74,162 bytes; SHA-256 `b76717de6777404a56ded5cae962c922f199b32534364800a96ef059918a9990`; 190 items.
- The enforcement step was marked skipped in the successful job; the collector log records acquisition_status ACQUIRED and parse_status PASS. Do not describe that skipped step as a failed test.
- Uploaded workflow artifact: ID `14098814399`, ZIP size 18,730 bytes, SHA-256 `ca0649032c67fd4519bce66d2dd6cd61805efbd2f9f7f0612fa88b05cedec517`, expires 2026-12-14T04:43:21Z.

## Downloaded artifact verification
The artifact ZIP was downloaded and locally inspected:
- `announcements.xml`: 74,162 bytes; SHA-256 matches manifest/raw acquisition.
- `announcements.jsonl`: 157,661 bytes; SHA-256 `fa17c0c89ebc10321821aa54fe5f5eaf7c488ddbd2e3a4d32ac0aa2e49c9b60d`; 190 JSON records.
- `manifest.json`: 6,251 bytes; SHA-256 `dc4435c3043f323aa79abfeba4b571184dd44ce0b6935be69f01dc8f0ab7a052`.
- ZIP contents: exactly these three files; extracted total 238,074 bytes.
- ZIP SHA-256 independently recomputed locally matches GitHub Actions artifact digest.

## Cohort and field QA
- 190 records; title, description_original and pubDate_original are populated for all records.
- 190/190 records have no GUID; manifest independently records guid_count=0 and items_without_guid=190. Preserve original source records; do not synthesize GUIDs.
- 155/190 records have empty links. All 155 belong to the `Declaration of NAV` subject cohort; these are NAV-disclosure records, not missing equity-attachment links. Do not treat them as missing links requiring fabricated URL repair.
- 35/190 records have non-empty links, all on `nsearchives.nseindia.com`.
- 155 records share the displayed 07:00:00 publication time; preserve the original publication-time strings and do not fabricate more precise timestamps.
- Repeated company/title names exist (e.g. multiple disclosures for one issuer); retain record-level rows and do not deduplicate by title alone.
- This QA does not establish symbol mapping, attachment contents, historical completeness, or a dated stock-return join.

## Boundaries and next use
- This run provides a preserved, hashed raw RSS snapshot and parsed JSONL for the retrieval time only.
- No issuer-symbol crosswalk, PDF download/content validation, corporate-event to price/volume join, event-study sample or return attribution was performed.
- No code, data, selector, ranking, diagnostics, workflow or production behavior was changed; no PR/merge.

## Status
- Run/job log verification: 100%.
- Artifact download, ZIP digest verification and member-file hashing: 100%.
- 190-row structural/cohort QA: 100%.
- Symbol mapping and official attachment-content verification: 0% / NOT RUN.
- Event join and matured H+1/H+3/H+5 study: 0% / BLOCKED.
- Overall project: NOT CALCULABLE; Hard Gate BLOCKED.
