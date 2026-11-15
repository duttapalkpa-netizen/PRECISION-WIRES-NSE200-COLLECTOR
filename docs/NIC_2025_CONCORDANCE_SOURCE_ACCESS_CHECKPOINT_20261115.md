# NIC-2025 to NIC-2008 Concordance — Official Source Access Checkpoint

Date: 2026-11-15
Status: OFFICIAL PDF TEXT ACCESS VERIFIED; RAW FILE BYTES NOT ARCHIVED; FULL ROW EXTRACTION NOT YET COMPLETED

## Official source access result

The earlier attempted MoSPI PDF URL under new.mospi.gov.in/uploads/publications_reports/ returned a retrieval error. A second official MoSPI URL is accessible through the public document text index:

- Official PDF: https://www.mospi.gov.in/sites/default/files/main_menu/national_industrial_classification/NIC_2025Final_18112025.pdf
- The PDF identifies itself as National Industrial Classification 2025, Government of India / MoSPI / NSO.
- Contents explicitly place “Concordance between 4-digit industry classes of NIC-2025 and NIC-2008” on printed pages 232–238.
- Source text defines (p) as part and + as aggregation of classes.
- The concordance table is rendered in the accessible PDF text as two-column table rows. Printed pages 232–237 and the start of page 238 are visible in source lines 15228–15741.

## Exact extraction boundary and edge case

- The concordance is at 4-digit class level; it is not an IIP-specific 2-digit item-group or weight bridge.
- A split continuation is explicitly visible: NIC-2025 code 4772 has source expression 4772(p)+4789(p)+4791(p)+ at the end of one table block, followed by a blank NIC-2025 code row with 4799(p) in the next block. This continuation must be attached to 4772 only after preserving both raw fragments and page/table context.
- No prefix-based or 2-digit roll-up is approved.

## Integrity / scope limits

- PDF content is readable through official public web document extraction; a local PDF binary was not downloaded in this run. Therefore no raw PDF byte length or SHA-256 is claimed.
- No complete machine-readable 463-row CSV was generated in this checkpoint; no row count or parser QA is claimed.
- Previously documented examples and no-auto-roll-up decision remain unchanged.
- IIP-specific item-group/weight bridge remains UNKNOWN / BLOCKED. Production use NOT_APPROVED.
- No synthetic rows, inferred mappings, workflow reruns, PR merges, production changes, or changes to protected V11.3 invariants.

## Next bounded action

Use the now-accessible official PDF text/visual pages 232–238 to transcribe every table row, retaining verbatim source expression, printed page, table-block identity and continuation fragments. Then independently validate exactly 463 unique NIC-2025 4-digit keys, parsed 4-digit NIC-2008 components, partial flags, aggregation markers, duplicate keys, forward/reverse multiplicities, and the 4772 continuation. If any source row is not legible or extraction count differs, fail closed and retain UNKNOWN.

## Progress

- Alternate official source discovery and text access: 100% for this bounded task.
- Raw PDF byte archival and SHA-256: 0% / NOT_DONE.
- Complete 463-row structured extraction: 0% / NOT_DONE.
- Extraction QA and multiplicity audit: 0% / NOT_STARTED.
- IIP 2-digit / item-group-weight bridge: UNKNOWN / BLOCKED.
