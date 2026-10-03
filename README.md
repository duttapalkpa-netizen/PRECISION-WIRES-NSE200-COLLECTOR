# PRECISION-WIRES NSE200 COLLECTOR

Automated NSE equity acquisition, QA and transparent V11.3 technical-core pipeline.

Flow: NSE Full Bhavcopy -> 200 valid EQ sessions -> normalized dataset -> strict QA -> V11.3 A/B/C/D/E technical diagnostics -> risk modifier -> finalist artifacts.

NSE's official reports archive lists Full Bhavcopy and Security Deliverable data and CM-UDiFF reports. The legacy CM Bhavcopy/Common Bhavcopy reports are marked discontinued in favor of UDiFF. This collector deliberately fails if it cannot acquire 200 valid sessions.

Scope: this first executable pass validates acquisition/normalization/QA and runs the data-backed technical core. Catalyst, research-house, FII/DII, macro/geo-shock and live first-hour inputs are explicitly marked unavailable rather than fabricated.

Local commands:
python -m pip install -r requirements.txt
python collector/nse_download.py --sessions 200
python collector/build_200_sessions.py
python qa/validate_dataset.py
python pipeline/v11_3_abcd_e.py
python pipeline/risk_modifier.py

Outputs are stored under data/processed, data/qa and outputs/finalists.
