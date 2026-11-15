# NIC-2025 Concordance Parser — Source-Derived Acceptance Tests

Date: 2026-11-15
Status: TEST SPECIFICATION COMPLETE; PARSER IMPLEMENTATION AND FULL EXTRACTION NOT DONE
Source: Official MoSPI NIC-2025 PDF, printed concordance pages 232–238.
Canonical URL: https://www.mospi.gov.in/uploads/publications_reports/publications_reports1763457214315_c3e5d4f3-8e25-4775-85e3-ad42d571652f_NIC_2025_Final.pdf

## Purpose

Freeze difficult source-layout cases as deterministic parser acceptance tests before extracting the complete 463-class concordance. This is a test specification, not a claim that the CSV, parser or QA run exists.

## Source-derived test cases

| Test ID | NIC-2025 key | Source lines | Expected reconstructed NIC-2008 expression | Required behaviour |
|---|---|---:|---|---|
| T01 | 0113 | 10339 | 0113+0128(p) | preserve aggregation and partial marker |
| T02 | 0330 | 10378–10379 | 0311(p)+0312(p)+0321(p)+0322(p) | join wrapped continuation under same key |
| T03 | 1512 | 10430 | 1512+2220(p) | preserve aggregation and partial |
| T04 | 1811 | 10440 | 1811+1313(p) | preserve cross-division component |
| T05 | 4340 | 10571–10573 | 4311(p)+4312(p)+4321(p)+4322(p)+4329(p)+4330(p)+4390(p) | join multiple wrapped lines |
| T06 | 4642 / 4649 | 10579–10583 | 4649(p)+4659(p) | page transition; continuation under next page table header assigned only by source sequence |
| T07 | 4772 | 10626–10630 | 4772(p)+4789(p)+4791(p)+4799(p) | retain first fragment; ignore repeated header; append blank-key continuation |
| T08 | 4790 | 10637–10644 | 4510(p)+4711(p)+4719(p)+4721(p)+4722(p)+4723(p)+4730(p)+4741(p)+4742(p)+4751(p)+4752(p)+4753(p)+4759(p)+4761(p)+4762(p)+4763(p)+4764(p)+4771(p)+4772(p)+4773(p)+4774(p)+4791(p)+4799(p) | retain every plus-separated component |
| T09 | 9540 | 10855–10857 | 4520(p)+4540(p)+9511(p)+9512(p)+9521(p)+9522(p)+9523(p)+9524(p)+9529(p) | join wrapped final-page expression |
| T10 | 9900 | 10872 | 9900 | accept final concordance row; stop before explanatory notes |

## Parser rules made testable

1. Preserve all codes as strings; never cast to integers or drop leading zeroes.
2. A row starts only when a valid four-digit NIC-2025 key and a NIC-2008 expression occur in the correct two-column table context.
3. A continuation line with an empty NIC-2025 key may append to the immediately preceding row only if page/table sequence and column structure establish continuity.
4. Repeated table headings (“NIC 2025 Code / NIC 2008 Code”) are structural tokens, never data.
5. Page-number tokens and PDF page markers are metadata, never code components.
6. Join wrapped expressions without dropping plus signs, partial markers, or components; preserve raw source fragments separately from normalized expression.
7. Parse each component as exactly four digits plus optional (p); reject malformed tokens rather than repairing them.
8. has_partial is true iff at least one component has (p); has_aggregation is true iff two or more source components are joined by +.
9. A row with an incomplete trailing +, unresolved blank-key continuation, malformed code or ambiguous table boundary remains UNKNOWN and blocks acceptance.
10. Full-table acceptance requires exactly 463 unique non-empty NIC-2025 keys and independent source-row coverage reconciliation; the published taxonomy count alone is not sufficient.
11. Calculate forward and reverse multiplicities independently. Do not infer 2-digit IIP mappings, item-group coverage, weights or index conversion from this class-level table.

## Expected test assertions

- T02, T05, T07, T08 and T09 reconstruct exactly the expressions shown above.
- T07 contains 4 source components after joining; continuation 4799(p) is not lost or emitted as a separate row.
- T08 contains 23 source components; no component is silently truncated.
- T09 contains 9 source components.
- T10 is the final concordance key and no explanatory-note text is ingested.
- No test may pass by silently repairing a malformed source token.

## Progress and limitations

- Source-derived difficult-case identification: 100% COMPLETE.
- Deterministic parser acceptance specification: 100% COMPLETE.
- Parser implementation: 0% NOT_DONE.
- Automated test execution: 0% NOT_DONE.
- Complete 463-row structured extraction: 0% NOT_DONE.
- Independent row-count / forward-reverse QA: 0% NOT_DONE.
- Raw PDF binary archival and SHA-256: 0% NOT_DONE (download attempt failed; no hash claimed).
- IIP-specific item-group / weight bridge: UNKNOWN / BLOCKED.

No CSV or manifest created; no source rows fabricated; no workflow rerun, PR, merge, production integration, paid API, spending, external contact, or protected V11.3 invariant change.
