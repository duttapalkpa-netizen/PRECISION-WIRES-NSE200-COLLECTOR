"""Research-only FII/DII structural contract; deliberately emits no trading signal."""
from datetime import datetime
import math

ALLOWED_SCOPES = {"NSE_ONLY", "NSE_BSE_MSEI_COMBINED"}
EXPECTED_GROUPS = {"FII_FPI", "DII"}


def validate_rows(rows, scope):
    """Validate one declared scope only. Returns structural metadata, never POSITIVE/NEGATIVE."""
    if scope not in ALLOWED_SCOPES:
        raise ValueError("unknown exchange scope")
    if not isinstance(rows, list) or not rows:
        raise ValueError("rows missing or empty")
    seen = set()
    dates = set()
    for row in rows:
        if not isinstance(row, dict):
            raise ValueError("row must be an object")
        group = row.get("group")
        if group not in EXPECTED_GROUPS:
            raise ValueError("unknown/missing category")
        date = row.get("date")
        if not isinstance(date, str):
            raise ValueError("invalid observation date")
        try:
            parsed = datetime.strptime(date, "%d-%b-%Y")
        except ValueError as exc:
            raise ValueError("invalid observation date") from exc
        if parsed.strftime("%d-%b-%Y") != date:
            raise ValueError("invalid observation date")
        key = (scope, date, group)
        if key in seen:
            raise ValueError("duplicate scope/date/category")
        seen.add(key)
        values = {}
        for field in ("buy_value", "sell_value", "net_value"):
            value = row.get(field)
            if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
                raise ValueError("non-finite numeric " + field)
            values[field] = round(float(value), 2)
        if round(values["buy_value"] - values["sell_value"], 2) != values["net_value"]:
            raise ValueError("buy/sell/net arithmetic mismatch")
        dates.add(date)
    return {
        "status": "STRUCTURE_VALIDATED_ONLY",
        "scope": scope,
        "row_count": len(rows),
        "groups": sorted({r["group"] for r in rows}),
        "distinct_dates": len(dates),
    }


def maturity_status(rows, min_distinct_sessions):
    """Return UNKNOWN until caller-approved minimum distinct dates is reached."""
    if isinstance(min_distinct_sessions, bool) or not isinstance(min_distinct_sessions, int) or min_distinct_sessions < 1:
        raise ValueError("min_distinct_sessions must be a positive integer")
    dates = {r.get("date") for r in rows if isinstance(r, dict) and isinstance(r.get("date"), str)}
    return "MATURED_FOR_REVIEW" if len(dates) >= min_distinct_sessions else "UNKNOWN"
