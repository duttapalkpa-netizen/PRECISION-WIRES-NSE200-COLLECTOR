#!/usr/bin/env python3
"""Measure warm-cache validation without making network requests."""
from __future__ import annotations
import argparse, json, time
from datetime import date, timedelta
from pathlib import Path
from collector.nse_download import validate_cached_file


def audit_cache(raw_dir: Path, sessions: int) -> dict:
    if sessions < 1:
        raise ValueError("sessions must be >= 1")
    started = time.perf_counter()
    today = date.today()
    hits, misses, scanned = [], [], 0
    for offset in range(1000):
        if len(hits) + len(misses) >= sessions:
            break
        day = today - timedelta(days=offset)
        if day.weekday() >= 5:
            continue
        scanned += 1
        path = raw_dir / f"sec_bhavdata_full_{day.strftime('%d%m%Y')}.csv"
        if path.is_file() and validate_cached_file(path, day):
            hits.append(day.isoformat())
        else:
            misses.append(day.isoformat())
    elapsed = time.perf_counter() - started
    return {
        "requested_sessions": sessions,
        "scanned_trading_dates": scanned,
        "valid_cache_hits": len(hits),
        "cache_misses": len(misses),
        "hit_dates": hits,
        "miss_dates": misses,
        "elapsed_seconds": round(elapsed, 6),
        "dates_per_second": round(scanned / elapsed, 3) if elapsed else None,
        "network_requests": 0,
        "benchmark_type": "local_warm_cache_validation_only",
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--raw-dir", default="data/raw")
    parser.add_argument("--sessions", type=int, default=200)
    parser.add_argument("--output", default="data/qa/nse_warm_cache_benchmark.json")
    args = parser.parse_args()
    result = audit_cache(Path(args.raw_dir), args.sessions)
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if result["valid_cache_hits"] != args.sessions:
        raise SystemExit(f"warm cache incomplete: {result['valid_cache_hits']}/{args.sessions} valid sessions")


if __name__ == "__main__":
    main()
