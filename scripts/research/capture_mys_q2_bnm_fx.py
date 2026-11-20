#!/usr/bin/env python3
"""Research-only capture and reconciliation of official Malaysia BNM USD/MYR FX series."""
from __future__ import annotations

import csv
import hashlib
import io
import json
import sys
import urllib.request
from collections import Counter
from datetime import datetime, timezone
from decimal import Decimal
from pathlib import Path

OUT = Path("artifacts/gcr_mys_q2_bnm_fx")
START = "2026-04-01"
END = "2026-06-30"
DAILY_URL = "https://storage.data.gov.my/finsector/exr/daily_1200.csv"
MONTHLY_URL = "https://storage.data.gov.my/finsector/exr/monthly.csv"
MONTHS = ("2026-04", "2026-05", "2026-06")
TOLERANCE = Decimal("0.00011")  # monthly USD values are published to 4 decimal places


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def fetch(url: str, filename: str) -> dict:
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "PRECISION-WIRES-research-audit/1.0", "Accept": "text/csv,*/*"},
    )
    with urllib.request.urlopen(req, timeout=25) as response:
        raw = response.read()
        headers = {k.lower(): v for k, v in response.headers.items()}
        status = response.status
    (OUT / filename).write_bytes(raw)
    return {
        "url": url,
        "http_status": status,
        "content_type": headers.get("content-type"),
        "content_length_header": headers.get("content-length"),
        "last_modified": headers.get("last-modified"),
        "etag": headers.get("etag"),
        "byte_count": len(raw),
        "sha256": sha256(raw),
        "archive_file": filename,
        "raw_bytes_captured": True,
        "_raw": raw,
    }


def read_csv(raw: bytes) -> list[dict[str, str]]:
    text = raw.decode("utf-8-sig")
    reader = csv.DictReader(io.StringIO(text))
    if not reader.fieldnames:
        raise ValueError("CSV header missing")
    return list(reader)


def write_rows(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    manifest = {
        "task": "MYS Q2-2026 official BNM 1200-middle FX capture and cross-check",
        "retrieved_at_utc": datetime.now(timezone.utc).isoformat(),
        "period": {"start_inclusive": START, "end_inclusive": END},
        "source_owner": "Bank Negara Malaysia (via Malaysia official data.gov.my catalogue)",
        "dataset_ids": {
            "daily": "exchangerates_daily_1200",
            "monthly": "exchangerates",
        },
        "licence": "CC BY 4.0",
        "method": {
            "daily_filter": "rate_type == middle; date in Q2 2026; currency column USD",
            "monthly_filter": "indicator == avg; date in Q2 2026; currency column USD",
            "interpretation": "MYR per USD; monthly avg is the average across trading days; compare monthly avg to arithmetic mean of observed daily 1200-middle rates",
            "no_fill_or_synthetic_values": True,
            "monthly_daily_crosscheck_tolerance": str(TOLERANCE),
        },
        "sources": {},
        "qa": {},
        "decision": "NOT_DONE",
    }
    errors: list[str] = []
    raw_daily = raw_monthly = None

    for key, url, filename in (
        ("daily_1200", DAILY_URL, "bnm_daily_1200_full_raw.csv"),
        ("monthly", MONTHLY_URL, "bnm_monthly_full_raw.csv"),
    ):
        try:
            rec = fetch(url, filename)
            raw = rec.pop("_raw")
            manifest["sources"][key] = rec
            if key == "daily_1200":
                raw_daily = raw
            else:
                raw_monthly = raw
        except Exception as exc:  # preserve exact bounded source-access failure
            errors.append(f"{key}: {type(exc).__name__}: {exc}")
            manifest["sources"][key] = {"url": url, "raw_bytes_captured": False, "error": errors[-1]}

    if raw_daily is not None and raw_monthly is not None:
        try:
            daily_all = read_csv(raw_daily)
            monthly_all = read_csv(raw_monthly)
            daily_required = {"date", "rate_type", "USD"}
            monthly_required = {"date", "indicator", "USD"}
            if not daily_required.issubset(daily_all[0].keys()):
                raise ValueError(f"daily CSV schema missing columns: {sorted(daily_required - set(daily_all[0].keys()))}")
            if not monthly_required.issubset(monthly_all[0].keys()):
                raise ValueError(f"monthly CSV schema missing columns: {sorted(monthly_required - set(monthly_all[0].keys()))}")

            daily = [
                r for r in daily_all
                if START <= (r.get("date") or "") <= END and r.get("rate_type") == "middle"
            ]
            monthly = [
                r for r in monthly_all
                if (r.get("date") or "")[:7] in MONTHS and r.get("indicator") == "avg"
            ]
            daily_dates = [r["date"] for r in daily]
            monthly_dates = [r["date"] for r in monthly]
            if len(daily_dates) != len(set(daily_dates)):
                raise ValueError("duplicate date in daily middle-rate Q2 subset")
            if len(monthly_dates) != len(set(monthly_dates)):
                raise ValueError("duplicate date in monthly avg Q2 subset")
            if {d[:7] for d in daily_dates} != set(MONTHS):
                raise ValueError(f"daily month coverage mismatch: {sorted({d[:7] for d in daily_dates})}")
            if {d[:7] for d in monthly_dates} != set(MONTHS):
                raise ValueError(f"monthly month coverage mismatch: {sorted({d[:7] for d in monthly_dates})}")
            if len(monthly) != 3:
                raise ValueError(f"expected exactly 3 monthly avg rows, found {len(monthly)}")

            daily_by_month: dict[str, list[Decimal]] = {m: [] for m in MONTHS}
            for row in daily:
                value = Decimal(row["USD"])
                if value <= 0:
                    raise ValueError(f"non-positive daily USD rate on {row['date']}")
                daily_by_month[row["date"][:7]].append(value)

            monthly_by_month: dict[str, Decimal] = {}
            for row in monthly:
                value = Decimal(row["USD"])
                if value <= 0:
                    raise ValueError(f"non-positive monthly USD rate on {row['date']}")
                monthly_by_month[row["date"][:7]] = value

            month_checks = []
            for month in MONTHS:
                vals = daily_by_month[month]
                if not vals:
                    raise ValueError(f"no daily observations for {month}")
                daily_mean = sum(vals, Decimal(0)) / Decimal(len(vals))
                monthly_value = monthly_by_month[month]
                difference = abs(daily_mean - monthly_value)
                passed = difference <= TOLERANCE
                month_checks.append({
                    "month": month,
                    "daily_observation_count": len(vals),
                    "daily_middle_mean_myr_per_usd": str(daily_mean),
                    "official_monthly_avg_myr_per_usd": str(monthly_value),
                    "absolute_difference": str(difference),
                    "tolerance": str(TOLERANCE),
                    "status": "PASS" if passed else "FAIL",
                })

            total_count = sum(len(daily_by_month[m]) for m in MONTHS)
            q2_daily_mean = sum(
                (sum(daily_by_month[m], Decimal(0)) for m in MONTHS), Decimal(0)
            ) / Decimal(total_count)
            weighted_monthly_mean = sum(
                (monthly_by_month[m] * Decimal(len(daily_by_month[m])) for m in MONTHS),
                Decimal(0),
            ) / Decimal(total_count)

            daily_out = [{"date": r["date"], "rate_type": r["rate_type"], "USD": r["USD"]} for r in sorted(daily, key=lambda x: x["date"])]
            monthly_out = [{"date": r["date"], "indicator": r["indicator"], "USD": r["USD"]} for r in sorted(monthly, key=lambda x: x["date"])]
            write_rows(OUT / "mys_q2_2026_daily_1200_middle_usd.csv", ["date", "rate_type", "USD"], daily_out)
            write_rows(OUT / "mys_q2_2026_monthly_avg_usd.csv", ["date", "indicator", "USD"], monthly_out)

            month_pass = all(x["status"] == "PASS" for x in month_checks)
            manifest["qa"] = {
                "daily_q2_middle_rows": len(daily),
                "daily_month_counts": {m: len(daily_by_month[m]) for m in MONTHS},
                "monthly_q2_avg_rows": len(monthly),
                "daily_unique_dates": True,
                "monthly_unique_dates": True,
                "all_months_covered": True,
                "month_checks": month_checks,
                "q2_arithmetic_mean_from_daily_rows_myr_per_usd": str(q2_daily_mean),
                "q2_weighted_mean_from_official_monthly_avg_myr_per_usd": str(weighted_monthly_mean),
                "q2_mean_absolute_difference": str(abs(q2_daily_mean - weighted_monthly_mean)),
                "daily_subset_sha256": sha256((OUT / "mys_q2_2026_daily_1200_middle_usd.csv").read_bytes()),
                "monthly_subset_sha256": sha256((OUT / "mys_q2_2026_monthly_avg_usd.csv").read_bytes()),
                "monthly_vs_daily_crosscheck": "PASS" if month_pass else "FAIL",
            }
            if not month_pass:
                errors.append("one or more official monthly averages did not reconcile to daily 1200-middle observations within rounding tolerance")
            manifest["decision"] = "PASS" if month_pass and not errors else "FAIL"
        except Exception as exc:
            errors.append(f"QA: {type(exc).__name__}: {exc}")
            manifest["qa"] = {"status": "FAIL", "error": errors[-1]}
            manifest["decision"] = "FAIL"
    else:
        manifest["decision"] = "BLOCKED_RAW_CAPTURE"

    manifest["errors"] = errors
    (OUT / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in manifest.items() if k != "sources"}, indent=2, ensure_ascii=False))
    return 0 if manifest["decision"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
