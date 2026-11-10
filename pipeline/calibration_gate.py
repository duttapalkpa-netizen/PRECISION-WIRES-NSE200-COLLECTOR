"""Fail-closed validation for V11.3 behavioral calibration evidence."""
import json
import math
import re
from datetime import date, datetime
from pathlib import Path

REQUIRED_METADATA = (
    "schema_version", "producer_engine", "producer_engine_version",
    "feature_contract_version", "producer_run_id", "producer_commit_sha",
    "dataset_sha256", "cutoff_start", "cutoff_end", "generated_at_utc",
    "target_definition", "label_maturity_cutoff",
)

def _unknown(status, reason, **extra):
    return {"status": status, "block_selection": True, "reason": reason, **extra}

def validate_calibration_artifact(path):
    path = Path(path)
    if not path.exists():
        return _unknown("UNKNOWN_MISSING", "artifact_missing")
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError):
        return _unknown("UNKNOWN_MALFORMED", "artifact_unreadable_or_invalid_json")
    if not isinstance(payload, dict):
        return _unknown("UNKNOWN_SCHEMA", "root_must_be_object")
    missing = [key for key in REQUIRED_METADATA if key not in payload or payload[key] in (None, "")]
    if missing:
        return _unknown("UNKNOWN_PROVENANCE", "required_metadata_missing", missing_metadata=missing)
    if not re.fullmatch(r"[0-9a-fA-F]{40}", str(payload["producer_commit_sha"])):
        return _unknown("UNKNOWN_PROVENANCE", "producer_commit_sha_invalid")
    if not re.fullmatch(r"[0-9a-fA-F]{64}", str(payload["dataset_sha256"])):
        return _unknown("UNKNOWN_PROVENANCE", "dataset_sha256_invalid")
    try:
        start, end = date.fromisoformat(str(payload["cutoff_start"])), date.fromisoformat(str(payload["cutoff_end"]))
        generated = datetime.fromisoformat(str(payload["generated_at_utc"]).replace("Z", "+00:00"))
        date.fromisoformat(str(payload["label_maturity_cutoff"]))
        if end < start or generated.tzinfo is None:
            raise ValueError("invalid chronology or timezone")
    except ValueError:
        return _unknown("UNKNOWN_PROVENANCE", "date_or_timestamp_metadata_invalid")
    states = payload.get("states")
    if not isinstance(states, dict) or not states:
        return _unknown("UNKNOWN_INCOMPLETE", "states_missing_or_empty")
    for state, record in states.items():
        if not isinstance(record, dict) or not {"sample_count", "hit10_h3_count", "hit10_h3_rate"}.issubset(record):
            return _unknown("UNKNOWN_INCOMPLETE", "state_counts_or_rate_missing", state=str(state))
        n, hits, rate = record["sample_count"], record["hit10_h3_count"], record["hit10_h3_rate"]
        if isinstance(n, bool) or not isinstance(n, int) or n <= 0:
            return _unknown("UNKNOWN_INCOMPLETE", "sample_count_must_be_positive_integer", state=str(state))
        if isinstance(hits, bool) or not isinstance(hits, int) or hits < 0 or hits > n:
            return _unknown("INVALID_VALUE", "hit_count_out_of_range", state=str(state))
        if isinstance(rate, bool) or not isinstance(rate, (int, float)) or not math.isfinite(rate) or not 0 <= rate <= 1:
            return _unknown("INVALID_VALUE", "rate_must_be_finite_number_in_0_1", state=str(state))
        if not math.isclose(float(rate), hits / n, rel_tol=0.0, abs_tol=1e-9):
            return _unknown("INVALID_VALUE", "rate_does_not_reconcile_to_counts", state=str(state))
    return {"status": "VALID", "block_selection": False, "reason": "validated_metadata_counts_and_rates"}
