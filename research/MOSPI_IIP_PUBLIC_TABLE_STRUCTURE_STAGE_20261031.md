# MoSPI IIP public release — structural extraction stage

## Verified live collection
Run #41189792423 succeeded without credentials. The collector received HTTP 200 from the official PIB IIP release page, content type `text/html; charset=utf-8`, captured 2,188,872 bytes, extracted 10 HTML tables, and recorded raw SHA-256 `b7296571ef1b199100bd71dcee17b4db1eaecff0d222a20cc83048ecd88fbe88`. Retrieval timestamp: 2026-10-31T09:42:51.459991+00:00. Artifact ID: 13037898401.

## Next stage implemented
The collector now emits a structural inventory and one CSV per extracted HTML table, padding ragged rows while preserving cell text. This is a forensic table-discovery layer, not yet a semantic IIP time-series parser.

## Acceptance criteria for this stage
- Raw HTML remains immutable and hash-addressed.
- Table inventory records table ID, row count, maximum column count, non-empty cell count and CSV filename.
- At least one non-trivial table candidate (2+ rows and 2+ columns) must exist.
- No column names, units, frequency or periods are inferred from position alone.
- No promotion to factor availability until semantic mapping, numeric validation, duplicate-key checks, unit/base/frequency/revision checks and non-empty time-series QA pass.

## Source caveat
The public PIB release page is an official release source, while e-Sankhyiki is the preferred source for detailed downloadable IIP tables and longer series. The portal FAQ says CSV downloads are available without registration. This current smoke artifact does not yet capture an e-Sankhyiki CSV/API response.
