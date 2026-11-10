"""Fail-closed validation for V11.3 behavioral calibration evidence."""
import json
import math
from pathlib import Path

REQUIRED_METADATA = (
    "schema_version", "producer_engine", "producer_engine_version",
    "feature_contract_version", "producer_run_id", "producer_commit_sha",
    "dataset_sha256", "cutoff_start", "cutoff_end", "generated_at_utc",
    "target_definition", "label_maturity_cutoff",
)

def validate_calibration_artifact(path):
    path = Path(path)
    if not path.exists():
        return {"status": "UNKNOWN_MISSING", "block_selection": True, "reason": "artifact_missing"}
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError):
        return {"status": "UNKNOWN_MALFORMED", "block_selection": True, "reason": "artifact_unreadable_or_invalid_json"}
    if not isinstance(payload, dict):
        return {"status": "UNKNOWN_SCHEMA", "block_selection": True, "reason": "root_must_be_object"}
    missing = [key for key in REQUIRED_METADATA if key not in payload or payload[key] in (None, "")]
    if missing:
        return {"status": "UNKNOWN_PROVENANCE", "block_selection": True,
                "reason": "required_metadata_missing", "missing_metadata": missing}
    states = payload.get("states")
    if not isinstance(states, dict) or not states:
        return {"status": "UNKNOWN_INCOMPLETE", "block_selection": True, "reason": "states_missing_or_empty"}
    for state, record in states.items():
        if not isinstance(record, dict) or "hit10_h3_rate" not in record:
            return {"status": "UNKNOWN_INCOMPLETE", "block_selection": True,
                    "reason": "state_rate_missing", "state": str(state)}
        rate = record["hit10_h3_rate"]
        if isinstance(rate, bool) or not isinstance(rate, (int, float)) or not math.isfinite(rate) or not 0 <= rate <= 1:
            return {"status": "INVALID_VALUE", "block_selection": True,
                    "reason": "rate_must_be_finite_number_in_0_1", "state": str(state)}
    return {"status": "VALID", "block_selection": False, "reason": "validated_structure_and_metadata"}
