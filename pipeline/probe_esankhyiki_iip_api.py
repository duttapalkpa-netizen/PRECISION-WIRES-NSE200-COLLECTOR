#!/usr/bin/env python3
"""Unauthenticated, read-only discovery probe for the official MoSPI IIP API.

This probe never sends credentials or changes data. It records the live OpenAPI
contract and a bounded response sample so the historical collector can be
implemented against observed official schema rather than guessed parameters.
"""
from __future__ import annotations
import argparse, hashlib, json, re, urllib.error, urllib.request
from datetime import datetime, timezone
from pathlib import Path

BASE = "https://esankhyiki.mospi.gov.in"
SPEC_URL = BASE + "/layout/swagger_user_iip.yaml"
API_URL = BASE + "/api/iip/getIIPData"
UA = "PRECISION-WIRES-IIP-readonly-schema-probe/1.0"

def request(url: str, timeout: int = 20):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json, text/yaml, */*"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as response:
            body = response.read(2_000_001)
            return {"http_status": getattr(response, "status", 200),
                    "content_type": response.headers.get("Content-Type", ""),
                    "final_url": response.geturl(), "body": body,
                    "truncated": len(body) > 2_000_000}
    except urllib.error.HTTPError as exc:
        return {"http_status": exc.code, "content_type": exc.headers.get("Content-Type", ""),
                "final_url": exc.geturl(), "body": exc.read(200_000), "truncated": False}
    except Exception as exc:
        return {"http_status": None, "content_type": "", "final_url": url,
                "body": b"", "error": f"{type(exc).__name__}: {exc}", "truncated": False}

def summarize_api(body: bytes, content_type: str):
    result = {"parse_status": "NON_JSON", "top_level_type": None, "keys": [], "record_count": None, "sample": None}
    try:
        payload = json.loads(body.decode("utf-8-sig"))
    except Exception as exc:
        result["parse_error"] = f"{type(exc).__name__}: {exc}"
        result["text_preview"] = body[:1000].decode("utf-8", "replace")
        return result
    result["parse_status"] = "JSON"
    result["top_level_type"] = type(payload).__name__
    if isinstance(payload, dict):
        result["keys"] = sorted(map(str, payload.keys()))
        for value in payload.values():
            if isinstance(value, list):
                result["record_count"] = len(value)
                result["sample"] = value[:2]
                break
    elif isinstance(payload, list):
        result["record_count"] = len(payload)
        result["sample"] = payload[:2]
    return result

def probe(out: Path):
    out.mkdir(parents=True, exist_ok=True)
    spec = request(SPEC_URL)
    api = request(API_URL)
    spec_text = spec["body"].decode("utf-8", "replace")
    (out / "iip_openapi_raw.yaml").write_bytes(spec["body"])
    (out / "iip_api_raw_response.bin").write_bytes(api["body"])
    path_match = re.search(r"(?m)^\s*/api/iip/getIIPData\s*:", spec_text)
    path_block = ""
    if path_match:
        tail = spec_text[path_match.start():]
        next_path = re.search(r"(?m)^\s{2}/", tail[1:])
        path_block = tail[:next_path.start()+1] if next_path else tail[:12000]
    report = {
        "retrieved_at_utc": datetime.now(timezone.utc).isoformat(),
        "source": "official MoSPI e-Sankhyiki",
        "spec": {"url": SPEC_URL, "http_status": spec["http_status"],
                 "content_type": spec["content_type"], "final_url": spec["final_url"],
                 "bytes": len(spec["body"]), "sha256": hashlib.sha256(spec["body"]).hexdigest(),
                 "contains_iip_path": bool(path_match), "iip_path_contract_excerpt": path_block,
                 "error": spec.get("error")},
        "api_no_auth_no_params": {"url": API_URL, "http_status": api["http_status"],
                 "content_type": api["content_type"], "final_url": api["final_url"],
                 "bytes": len(api["body"]), "truncated": api["truncated"],
                 "sha256": hashlib.sha256(api["body"]).hexdigest(),
                 "response_summary": summarize_api(api["body"], api["content_type"]),
                 "error": api.get("error")},
        "decision": "SCHEMA_DISCOVERY_ONLY",
        "limitations": ["No credentials or tokens were sent.",
          "No historical series is declared ingested by this probe.",
          "A successful HTTP response is not a data-coverage PASS.",
          "API parameters and pagination must be implemented only after the official contract is inspected."]
    }
    (out / "iip_api_probe.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"spec_status": spec["http_status"], "spec_has_endpoint": bool(path_match),
                      "api_status": api["http_status"], "api_parse": report["api_no_auth_no_params"]["response_summary"]["parse_status"],
                      "decision": report["decision"]}, indent=2))
    return report

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default="artifacts/esankhyiki_iip_probe")
    args = parser.parse_args()
    probe(Path(args.out))
