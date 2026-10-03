# PRECISION-WIRES NSE200 COLLECTOR

Automated NSE equity acquisition, QA and adaptive V11.3 technical-core pipeline.

## Master architecture

NSE Historical Backbone (200+ market sessions)
-> Security Listing-Age Detection
-> Adaptive History Engine
-> A/B/C/D/E
-> Risk Modifier
-> Live 1%
-> Finalist

**200+ sessions is the market historical backbone, NOT a stock-level eligibility gate.**

Security routing:
- 200+ -> FULL V11.3
- 100-199 -> EXTENDED V11.3
- 50-99 -> DEVELOPING V11.3
- 20-49 -> EARLY V11.3
- 5-19 -> EARLY EXPANSION ENGINE
- 1-4 -> IPO-PLX V2.0

Every analysed security is retained and output includes:
**SCORE + HISTORY_DEPTH + ANALYSIS_MODE + DATA_CONFIDENCE**.

Listing-age detection currently uses the first observed session in the acquired backbone as a transparent proxy. An NSE Security Master listing date can later replace this proxy without changing the adaptive routing.

## Commands

python -m pip install -r requirements.txt
python collector/nse_download.py --sessions 200
python collector/build_200_sessions.py
python qa/validate_dataset.py
python pipeline/v11_3_abcd_e.py
python pipeline/risk_modifier.py

Outputs are stored under data/processed, data/qa and outputs/finalists.

## Scope

This pass implements the adaptive history/routing layer and data-backed technical core. It does **not** claim that all 672 V11.3 diagnostics are currently live. Catalyst, research-house, FII/DII, macro/geo-shock and live first-hour inputs remain explicitly unavailable rather than fabricated.
