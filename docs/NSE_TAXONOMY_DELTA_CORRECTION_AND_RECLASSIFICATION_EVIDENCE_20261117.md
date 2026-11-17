# NSE 2022→2023 Taxonomy Delta — Correction and Reclassification Evidence

Date: 2026-11-17

## Purpose
Correct over-broad interpretations in the prior sample audit by checking full relevant July-2023 table rows rather than treating absence from a short excerpt as deletion.

## Official sources
- NSE Indices Industry Classification Structure, March 2022: https://nsearchives.nseindia.com/web/sites/default/files/inline-files/NSE%20Indices_Industry%20Classification%20Structure-2022-03.pdf
- NSE Indices Industry Classification Structure, July 2023: https://nsearchives.nseindia.com/web/sites/default/files/inline-files/nse-indices_industry-classification-structure-2023-07.pdf

## Corrected findings

### 1. Air Conditioner — NOT deleted in July 2023
- March 2022 lists IN020201001 “Air Conditioner” with definition “Manufacturers and distributors of air conditioners” (March PDF extracted lines 151–153, page 5).
- July 2023 lists IN020201007 “Household Appliances”; its definition explicitly includes air conditioners, juicers, food processors and microwave ovens (July PDF extracted lines 490–494).
- Decision: classify as a strong candidate for consolidation/reclassification from a standalone Basic Industry to a broader Household Appliances Basic Industry. Do not claim exact one-to-one equivalence for all issuers; issuer-level treatment requires source-specific records.

### 2. Toys — NOT deleted in July 2023
- March 2022 lists IN020201014 “Toys” (March PDF extracted lines 179–182, page 7).
- July 2023 lists IN020201010 “Leisure Products”; definition explicitly includes sports equipment, gift articles, toys and games (July PDF extracted lines 508–512).
- Decision: strong definition-level evidence of consolidation/reclassification into Leisure Products, not deletion.

### 3. Cycles — scope clarification
- March 2022 IN020101002 “2/3 Wheelers” includes bicycles and three-wheelers (March PDF lines 120–124); Cycles is also separately listed as IN020201002 under Consumer Durables (March lines 151–153), showing an apparent scope overlap in the 2022 published definitions.
- July 2023 IN020101002 explicitly excludes bicycles and tricycles; IN020201002 Cycles is explicitly defined as bicycles and tricycles (July PDF lines 371–428).
- Decision: scope boundary was clarified; do not count this as a new Cycles code without issuer-level and full code inventory evidence.

### 4. Automobile trading
- March 2022 IN020101003 “Trading - Automobiles” (March lines 126–128).
- July 2023 IN020101004 “Auto Dealer” with substantially aligned trading/distribution definition (July lines 382–384).
- Decision: candidate rename/recode; exact historical code lineage requires full diff/change notice.

### 5. Auto-component trading
- March 2022 IN020102005 “Trading - Auto Ancillaries” (March lines 146–150).
- July 2023 IN020102007 “Trading - Auto Components” (July lines 404–417).
- Decision: candidate rename/recode with definition-level continuity; not an exact-code match.

## Methodological correction
A missing label or code in a partial page excerpt is NOT evidence of deletion. Each proposed deletion must be checked against every row of the full target-vintage PDF, including broader categories whose definitions may absorb the old activity. Classification must distinguish: exact continuation, code change, label change, definition broadening, scope boundary change, consolidation/reclassification, confirmed deletion, and unresolved.

## Current acceptance state
- Five targeted historical examples reviewed against full relevant PDF table context.
- Air Conditioner: reclassification/consolidation candidate; not deletion.
- Toys: reclassification/consolidation candidate; not deletion.
- Cycles: boundary clarification candidate; not newly introduced in 2023.
- Trading - Automobiles → Auto Dealer: rename/recode candidate.
- Trading - Auto Ancillaries → Trading - Auto Components: rename/recode candidate.
- Exhaustive 2022/2023 Basic Industry inventory and bidirectional diff: NOT_DONE.
- Per-code effective dates / official change log: UNKNOWN.
- Raw PDF byte manifests / SHA-256: NOT_ACQUIRED.
- BSE crosswalk / issuer mapping / PIT / parser / registry: NOT_AUTHORIZED.

## Next action
Complete full-vintage machine-readable inventories preserving exact raw codes, all four parent levels and definitions; then classify every changed row using the categories above. Do not promote any candidate lineage until the full bidirectional inventory closes with zero unexplained rows.

## Invariants
No production logic, issuer assignments, parser, registry, tests or workflows changed. No synthetic data, timestamps or hashes. ₹0. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E, Hard Gate and collector workflows unchanged.
