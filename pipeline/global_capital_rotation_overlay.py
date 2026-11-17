#!/usr/bin/env python3
"""Research-only global capital rotation dashboard; never alters production ranking."""
from __future__ import annotations
import argparse, csv, hashlib, json, math, re
from collections import defaultdict
from datetime import date, datetime, timezone
from pathlib import Path

REQUIRED = {"date","indicator","value","unit","source","source_url","published_at","as_of_date","quality_status"}
EVIDENCE_FIELDS = {"evidence_manifest_id","raw_sha256","retrieved_at","http_status","content_type","byte_length","raw_payload_path"}
TRUSTED_QUALITIES = {"VERIFIED_OFFICIAL","VERIFIED_SECONDARY"}
DEFAULT_SOURCE_REGISTRY = Path(__file__).resolve().parents[1] / "config" / "global_capital_rotation_source_registry.json"

def _load_source_registry(path: Path):
    try:
        payload=json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"source registry unavailable or invalid: {path}") from exc
    if not isinstance(payload,dict) or payload.get("schema_version") != 1 or not isinstance(payload.get("sources"), list):
        raise ValueError("source registry schema_version=1 and sources[] are required")
    entries={}
    for item in payload["sources"]:
        required={"source","source_url","indicator","unit","quality_status","allowed_content_types"}
        if not isinstance(item,dict) or not required.issubset(item):
            raise ValueError("invalid source registry entry")
        if not all(isinstance(item[k],str) and item[k].strip() for k in ("source","source_url","indicator","unit","quality_status")):
            raise ValueError("source registry identity fields must be non-empty strings")
        if not item["source_url"].startswith("https://"):
            raise ValueError("source registry source_url must use HTTPS")
        content_types=item["allowed_content_types"]
        if not isinstance(content_types,list) or not content_types or not all(isinstance(x,str) and x.strip() for x in content_types):
            raise ValueError("allowed_content_types must be a non-empty list of strings")
        if item["quality_status"] not in TRUSTED_QUALITIES:
            raise ValueError("registry quality_status must be a trusted quality")
        key=(item["source"],item["source_url"],item["indicator"],item["unit"],item["quality_status"])
        if key in entries:
            raise ValueError("duplicate source registry entry")
        entries[key]=item
    return entries

def _load_evidence_manifest(input_dir: Path, manifest_id: str, row_number: int):
    if not re.fullmatch(r"[0-9A-Za-z._:-]{1,128}", manifest_id):
        raise ValueError(f"row {row_number}: invalid evidence_manifest_id")
    root=input_dir.resolve()
    manifest_path=(root / "evidence_manifests" / f"{manifest_id}.json").resolve()
    manifest_root=(root / "evidence_manifests").resolve()
    if manifest_root not in manifest_path.parents:
        raise ValueError(f"row {row_number}: evidence manifest path escapes manifest directory")
    try:
        manifest=json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"row {row_number}: evidence manifest unavailable or invalid") from exc
    required={"schema_version","evidence_manifest_id","source","source_url","final_url","indicator","unit","quality_status","published_at","retrieved_at","http_status","content_type","byte_length","sha256","raw_payload_path"}
    if not isinstance(manifest,dict) or not required.issubset(manifest) or manifest.get("schema_version") != 1:
        raise ValueError(f"row {row_number}: evidence manifest schema_version=1 and required fields are required")
    if manifest["evidence_manifest_id"] != manifest_id:
        raise ValueError(f"row {row_number}: evidence manifest ID mismatch")
    return manifest

def _validate_trusted_evidence(row, registry, row_number):
    if row["quality_status"] not in TRUSTED_QUALITIES:
        return
    key=(row["source"],row["source_url"],row["indicator"],row["unit"],row["quality_status"])
    entry=registry.get(key)
    if entry is None:
        raise ValueError(f"row {row_number}: trusted quality has no exact source-registry match")
    if not all(row.get(k,"").strip() for k in EVIDENCE_FIELDS):
        raise ValueError(f"row {row_number}: trusted quality missing evidence manifest fields")
    manifest=_load_evidence_manifest(Path(row["_input_dir"]),row["evidence_manifest_id"],row_number)
    row_manifest_fields={
        "source":row["source"],"source_url":row["source_url"],"indicator":row["indicator"],
        "unit":row["unit"],"quality_status":row["quality_status"],"published_at":row["published_at"],
        "retrieved_at":row["retrieved_at"],"http_status":row["http_status"],
        "content_type":row["content_type"],"byte_length":row["byte_length"],
        "sha256":row["raw_sha256"],"raw_payload_path":row["raw_payload_path"]
    }
    for field,expected in row_manifest_fields.items():
        actual=manifest.get(field)
        if field in {"published_at","retrieved_at"}:
            try:
                matches=_published_key(actual)==_published_key(expected)
            except (TypeError,ValueError):
                matches=False
        elif field=="http_status":
            matches=str(actual)==str(expected)
        elif field=="byte_length":
            matches=str(actual)==str(expected)
        else:
            matches=actual==expected
        if not matches:
            raise ValueError(f"row {row_number}: evidence manifest {field} mismatch")
    if manifest["final_url"] != row["source_url"]:
        allowed_final_urls=entry.get("allowed_final_urls",[row["source_url"]])
        if manifest["final_url"] not in allowed_final_urls:
            raise ValueError(f"row {row_number}: evidence manifest final_url not allowed by source registry")
    if not isinstance(manifest["final_url"],str) or not manifest["final_url"].startswith("https://"):
        raise ValueError(f"row {row_number}: evidence manifest final_url must use HTTPS")
    if not re.fullmatch(r"[0-9a-f]{64}",row["raw_sha256"]):
        raise ValueError(f"row {row_number}: raw_sha256 must be 64 lowercase hex characters")
    try:
        retrieved=_published_key(row["retrieved_at"])
        status=int(row["http_status"])
        length=int(row["byte_length"])
    except (TypeError,ValueError):
        raise ValueError(f"row {row_number}: invalid retrieval metadata")
    if status != 200 or length <= 0 or retrieved < _published_key(row["published_at"]):
        raise ValueError(f"row {row_number}: invalid HTTP status, byte length, or retrieval chronology")
    if row["content_type"].lower() not in entry.get("allowed_content_types",[]):
        raise ValueError(f"row {row_number}: content_type not allowed by source registry")
    payload_root=Path(row["_input_dir"]).resolve()
    payload_path=(payload_root / row["raw_payload_path"]).resolve()
    if payload_root not in payload_path.parents:
        raise ValueError(f"row {row_number}: raw_payload_path escapes input directory")
    try:
        raw_bytes=payload_path.read_bytes()
    except OSError as exc:
        raise ValueError(f"row {row_number}: raw payload unavailable") from exc
    if len(raw_bytes) != length or hashlib.sha256(raw_bytes).hexdigest() != row["raw_sha256"]:
        raise ValueError(f"row {row_number}: raw payload byte length or SHA-256 mismatch")

ALLOWED_QUALITY = {"VERIFIED_OFFICIAL","VERIFIED_SECONDARY","PROVISIONAL","UNKNOWN"}
MAX_AGE_DAYS = {
    "em_portfolio_flow_usd_bn":45,
    "india_fpi_equity_inr_cr":7,"india_fpi_debt_inr_cr":7,"india_dii_equity_inr_cr":7,
    "india_fpi_equity_mtd_inr_cr":7,"india_fpi_equity_ytd_inr_cr":30,
    "dxy_change_pct_20d":30,"us10y_change_bp_20d":30,"fed_target_change_bp_90d":120,
    "usd_inr_change_pct_20d":7,"brent_change_pct_20d":7,
    "india_vs_world_relative_return_pct_20d":7,"vix_change_pct_20d":7,
    "us_ai_policy_event_direction":180,"us_h1b_policy_event_direction":180,"us_tariff_policy_event_direction":180,
}

def _published_key(value):
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except (AttributeError, TypeError, ValueError):
        raise ValueError("published_at must be an ISO date or datetime")
    # Treat timezone-naive source dates/timestamps as UTC; normalize offsets
    # before ordering vintages so lexical ordering is chronological.
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc).isoformat()

def load_observations(path: Path, registry_path: Path = DEFAULT_SOURCE_REGISTRY):
    registry=_load_source_registry(registry_path)
    grouped=defaultdict(list)
    seen_keys=set()
    with path.open(encoding="utf-8-sig", newline="") as f:
        reader=csv.DictReader(f)
        if not reader.fieldnames or not REQUIRED.issubset(set(reader.fieldnames)):
            raise ValueError(f"missing columns: {sorted(REQUIRED-set(reader.fieldnames or []))}")
        for n,row in enumerate(reader, start=2):
            if row["quality_status"] not in ALLOWED_QUALITY:
                raise ValueError(f"row {n}: invalid quality_status")
            if not all(row[k].strip() for k in ("date","as_of_date","indicator","unit","source","source_url","published_at")):
                raise ValueError(f"row {n}: missing provenance/date")
            try:
                observed=date.fromisoformat(row["date"])
                asof=date.fromisoformat(row["as_of_date"])
                published=_published_key(row["published_at"])
                value=float(row["value"])
                if not math.isfinite(value): raise ValueError("non-finite value")
            except (TypeError,ValueError):
                raise ValueError(f"row {n}: invalid date, publication timestamp, or finite numeric value")
            duplicate_key=(row["indicator"],row["date"],row["as_of_date"],published,row["source"],row["source_url"])
            if duplicate_key in seen_keys:
                raise ValueError(f"row {n}: duplicate observation key within the same source publication vintage")
            seen_keys.add(duplicate_key)
            if observed > asof:
                raise ValueError(f"row {n}: observation date is after as_of_date")
            if not row["source_url"].startswith("https://"):
                raise ValueError(f"row {n}: source_url must use HTTPS")
            row["_input_dir"]=str(path.resolve().parent)
            _validate_trusted_evidence(row,registry,n)
            if row["quality_status"] in {"UNKNOWN","PROVISIONAL"}: continue
            grouped[row["indicator"]].append({**row,"value":value,"_published_key":published})
    return grouped

def latest(grouped,key,decision_at=None):
    rows=grouped.get(key,[])
    if decision_at is not None:
        cutoff=_published_key(decision_at)
        decision_date=datetime.fromisoformat(cutoff).date()
        rows=[r for r in rows if r["_published_key"] <= cutoff
              and date.fromisoformat(r["date"]) <= decision_date
              and date.fromisoformat(r["as_of_date"]) <= decision_date]
    if not rows: return None
    # Deterministic vintage selection: freshest observation, then latest publication.
    chosen=max(rows,key=lambda x:(x["as_of_date"],x["date"],x["_published_key"]))
    tie=[r for r in rows if (r["as_of_date"],r["date"],r["_published_key"]) ==
         (chosen["as_of_date"],chosen["date"],chosen["_published_key"])]
    if len({r["value"] for r in tie}) > 1:
        raise ValueError(f"{key}: conflicting values share the same observation and publication vintage")
    return chosen



def filter_fed_h10_valid_xml_observations(observations):
    """Keep only explicitly available H.10 observations; reject ND sentinels."""
    valid = []
    for obs in observations:
        if obs.get("OBS_STATUS") != "A":
            continue
        try:
            date.fromisoformat(obs["TIME_PERIOD"])
            value = float(obs["OBS_VALUE"])
        except (KeyError, TypeError, ValueError):
            continue
        if not math.isfinite(value):
            continue
        valid.append(obs)
    return valid


def derive_fed_h10_broad_dollar_change_20obs(grouped, decision_at):
    """Research-only percentage change across 20 prior valid H.10 observations."""
    indicator = "fed_h10_nominal_broad_dollar_index"
    try:
        cutoff = _published_key(decision_at)
        decision_date = datetime.fromisoformat(cutoff).date()
    except (TypeError, ValueError):
        raise ValueError("decision_at must be an ISO date or datetime")
    by_date = {}
    for row in grouped.get(indicator, []):
        if row.get("quality_status") not in TRUSTED_QUALITIES:
            continue
        try:
            observed = date.fromisoformat(row["date"])
            asof = date.fromisoformat(row["as_of_date"])
            published = _published_key(row["published_at"])
            value = float(row["value"])
        except (KeyError, TypeError, ValueError):
            continue
        if not math.isfinite(value) or published > cutoff or observed > decision_date or asof > decision_date:
            continue
        current = by_date.get(observed)
        candidate = {"date": observed, "value": value, "published": published}
        if current is None or published > current["published"]:
            by_date[observed] = candidate
        elif published == current["published"] and value != current["value"]:
            raise ValueError(f"conflicting H.10 values for {observed.isoformat()} at the same publication vintage")
    ordered = [by_date[k] for k in sorted(by_date)]
    # 20 prior valid observations plus the current observation = 21 values.
    if len(ordered) < 21:
        return None
    window = ordered[-21:]
    base, current = window[0], window[-1]
    if base["value"] == 0:
        raise ValueError("H.10 base observation must be non-zero")
    return {
        "indicator": "fed_h10_nominal_broad_dollar_change_pct_20obs",
        "value": (current["value"] / base["value"] - 1.0) * 100.0,
        "unit": "percent",
        "window_observation_count": 21,
        "prior_valid_observation_count": 20,
        "window_start_date": base["date"].isoformat(),
        "window_end_date": current["date"].isoformat(),
        "base_value": base["value"],
        "latest_value": current["value"],
        "decision_at": cutoff,
        "calendar_semantics": "20 prior valid Federal Reserve H.10 observation dates; not Indian trading sessions; no forward-fill",
        "quality_status": "VERIFIED_OFFICIAL",
        "production_eligible": False,
        "not_equivalent_to": "ICE DXY / dxy_change_pct_20d"
    }


def classify(grouped,as_of_date=None,decision_at=None):
    if as_of_date is None:
        raise ValueError("as_of_date is required for reproducible freshness classification")
    if decision_at is None:
        raise ValueError("decision_at is required for point-in-time classification")
    try:
        asof=date.fromisoformat(as_of_date)
    except (TypeError, ValueError):
        raise ValueError("as_of_date must be an ISO date")
    if decision_at is not None:
        decision_date=datetime.fromisoformat(_published_key(decision_at)).date()
        if decision_date > asof:
            raise ValueError("decision_at UTC date is after as_of_date")
    keys=list(MAX_AGE_DAYS)
    x={k:latest(grouped,k,decision_at) for k in keys}
    stale={}
    for k,row in x.items():
        if row:
            observed=date.fromisoformat(row["as_of_date"])
            age=(asof-observed).days
            if age<0: raise ValueError(f"{k}: as_of_date is in the future")
            if age>MAX_AGE_DAYS[k]:
                stale[k]={"age_days":age,"max_age_days":MAX_AGE_DAYS[k]}
                x[k]=None
    def v(k): return None if x.get(k) is None else x[k]["value"]
    if v("em_portfolio_flow_usd_bn") is None: global_flow="UNKNOWN"
    elif v("em_portfolio_flow_usd_bn")>0: global_flow="EM_NET_INFLOW"
    elif v("em_portfolio_flow_usd_bn")<0: global_flow="EM_NET_OUTFLOW"
    else: global_flow="FLAT"
    if v("india_fpi_equity_inr_cr") is None: india_fpi="UNKNOWN"
    elif v("india_fpi_equity_inr_cr")>0: india_fpi="FPI_EQUITY_NET_BUY"
    elif v("india_fpi_equity_inr_cr")<0: india_fpi="FPI_EQUITY_NET_SELL"
    else: india_fpi="FLAT"
    if v("dxy_change_pct_20d") is None or v("usd_inr_change_pct_20d") is None: fx="UNKNOWN"
    elif v("dxy_change_pct_20d")<0 and v("usd_inr_change_pct_20d")<0: fx="USD_WEAKENING_INR_STRENGTHENING"
    elif v("dxy_change_pct_20d")>0 and v("usd_inr_change_pct_20d")>0: fx="USD_STRENGTHENING_INR_WEAKENING"
    else: fx="DIVERGENT_OR_MIXED"
    if v("us10y_change_bp_20d") is None or v("fed_target_change_bp_90d") is None: rates="UNKNOWN"
    elif v("us10y_change_bp_20d")<0 and v("fed_target_change_bp_90d")<=0: rates="US_RATE_RELIEF"
    elif v("us10y_change_bp_20d")>0 and v("fed_target_change_bp_90d")>0: rates="US_RATE_PRESSURE"
    else: rates="MIXED"
    if v("india_vs_world_relative_return_pct_20d") is None: relative="UNKNOWN"
    elif v("india_vs_world_relative_return_pct_20d")>0: relative="INDIA_OUTPERFORMING"
    elif v("india_vs_world_relative_return_pct_20d")<0: relative="INDIA_UNDERPERFORMING"
    else: relative="INLINE"
    if v("brent_change_pct_20d") is None: oil="UNKNOWN"
    elif v("brent_change_pct_20d")<0: oil="OIL_PRICE_RELIEF"
    elif v("brent_change_pct_20d")>0: oil="OIL_PRICE_PRESSURE"
    else: oil="FLAT"
    if v("vix_change_pct_20d") is None: risk="UNKNOWN"
    elif v("vix_change_pct_20d")<0: risk="VOLATILITY_EASING"
    elif v("vix_change_pct_20d")>0: risk="VOLATILITY_RISING"
    else: risk="FLAT"
    mtd=v("india_fpi_equity_mtd_inr_cr"); ytd=v("india_fpi_equity_ytd_inr_cr")
    if mtd is None or ytd is None: horizon="UNKNOWN"
    elif mtd>0 and ytd<0: horizon="SHORT_TERM_INFLOW_LONG_TERM_OUTFLOW"
    elif mtd<0 and ytd<0: horizon="OUTFLOW_BOTH_HORIZONS"
    elif mtd>0 and ytd>0: horizon="INFLOW_BOTH_HORIZONS"
    elif mtd<0 and ytd>0: horizon="SHORT_TERM_OUTFLOW_LONG_TERM_INFLOW"
    else: horizon="MIXED_OR_FLAT"
    return {
      "status":"RESEARCH_ONLY_NO_PRODUCTION_SCORE","as_of_date":asof.isoformat(),
      "global_em_flow":global_flow,"india_fpi_equity":india_fpi,"india_fpi_horizon_divergence":horizon,"fx_transmission":fx,
      "us_rates_transmission":rates,"relative_attraction":relative,"oil_transmission":oil,
      "global_risk_appetite":risk,
      "india_fpi_debt":"UNKNOWN" if v("india_fpi_debt_inr_cr") is None else ("FPI_DEBT_NET_BUY" if v("india_fpi_debt_inr_cr")>0 else "FPI_DEBT_NET_SELL" if v("india_fpi_debt_inr_cr")<0 else "FLAT"),
      "india_dii_equity":"UNKNOWN" if v("india_dii_equity_inr_cr") is None else ("DII_NET_BUY" if v("india_dii_equity_inr_cr")>0 else "DII_NET_SELL" if v("india_dii_equity_inr_cr")<0 else "FLAT"),
      "policy_events":{k:("UNKNOWN" if v(k) is None else {"direction":v(k),"source":x[k]["source"],"source_url":x[k]["source_url"],"published_at":x[k]["published_at"]}) for k in keys[-3:]},
      "stale_observations_excluded":stale,
      "latest_observations":{k:(None if x[k] is None else {q:x[k][q] for q in ("date","value","unit","source","source_url","published_at","as_of_date","quality_status")}) for k in keys},
      "interpretation":"Global EM flows and India-specific FPI flows are separate populations and periods. A positive India daily print does not prove broad EM rotation. Missing or stale inputs remain UNKNOWN."
    }

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--input",required=True,help="long-format provenance CSV")
    p.add_argument("--output",default="global_capital_rotation_dashboard.json")
    p.add_argument("--as-of-date",required=True,help="Required ISO date for reproducible freshness checks")
    p.add_argument("--decision-at",required=True,help="Required ISO instant for point-in-time publication cutoff")
    a=p.parse_args()
    result=classify(load_observations(Path(a.input)),a.as_of_date,a.decision_at)
    Path(a.output).write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"status":result["status"],"output":a.output,"global_em_flow":result["global_em_flow"],"india_fpi_equity":result["india_fpi_equity"],"excluded_stale":len(result["stale_observations_excluded"])},indent=2))
if __name__=="__main__": main()
