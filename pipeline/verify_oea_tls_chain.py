#!/usr/bin/env python3
"""Fetch and pin the official Let's Encrypt YR1 chain, then verify OEA TLS strictly."""
import hashlib, json, re, ssl, subprocess, urllib.request
from pathlib import Path
from datetime import datetime, timezone
import certifi

OUT = Path("artifacts/macro_full_history_discovery")
TLS = OUT / "tls_diagnostics"
HOSTS = ("eaindustry.nic.in", "www.eaindustry.nic.in")
OFFICIAL = {
    "yr1_intermediate": "https://letsencrypt.org/certs/gen-y/int-yr1.pem",
    "root_yr_cross_signed_by_isrg_x1": "https://letsencrypt.org/certs/gen-y/root-yr-by-x1.pem",
}
UA = "PRECISION-WIRES-OEA-TLS-Chain-Verification/1.0"

def sha(b): return hashlib.sha256(b).hexdigest()
def fetch_official(url):
    ctx = ssl.create_default_context(cafile=certifi.where())
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/x-pem-file,text/plain,*/*"})
    with urllib.request.build_opener(urllib.request.HTTPSHandler(context=ctx)).open(req, timeout=25) as r:
        if r.geturl().split("/")[2].lower() != "letsencrypt.org":
            raise RuntimeError("Unexpected redirect host for official CA certificate")
        body = r.read(200000)
        if not body.startswith(b"-----BEGIN CERTIFICATE-----"):
            raise RuntimeError("Official CA endpoint did not return PEM")
        return body, r.geturl()

def peer_leaf(host):
    p = subprocess.run(
        ["openssl", "s_client", "-connect", host + ":443", "-servername", host, "-showcerts"],
        input=b"", capture_output=True, timeout=20
    )
    blocks = re.findall(rb"-----BEGIN CERTIFICATE-----.*?-----END CERTIFICATE-----", p.stdout + p.stderr, re.S)
    if not blocks:
        raise RuntimeError("No peer leaf certificate returned by " + host)
    return blocks[0] + b"\n"

def openssl(args):
    p = subprocess.run(["openssl", *args], capture_output=True, text=True, timeout=20)
    if p.returncode:
        raise RuntimeError("openssl " + " ".join(args) + " failed: " + p.stdout + p.stderr)
    return (p.stdout + p.stderr).strip()

def main():
    OUT.mkdir(parents=True, exist_ok=True); TLS.mkdir(parents=True, exist_ok=True)
    chain = {}
    for key, url in OFFICIAL.items():
        body, final = fetch_official(url)
        path = TLS / (key + ".pem"); path.write_bytes(body)
        chain[key] = {"url": url, "final_url": final, "file": str(path),
                      "bytes": len(body), "sha256": sha(body)}
    yr1 = TLS / "yr1_intermediate.pem"
    rootyr = TLS / "root_yr_cross_signed_by_isrg_x1.pem"
    leaf = TLS / "oea_peer_leaf.pem"
    leaf.write_bytes(peer_leaf("eaindustry.nic.in"))
    # Validate the official CA hierarchy against the runner's trusted ISRG Root X1.
    chain_verify = openssl(["verify", "-CAfile", certifi.where(), "-untrusted", str(rootyr), str(yr1)])
    # Validate the actual OEA leaf, full chain, server-auth purpose and hostname.
    untrusted = TLS / "oea_untrusted_chain.pem"
    untrusted.write_bytes(yr1.read_bytes() + rootyr.read_bytes())
    endpoint_verify = {}
    for host in HOSTS:
        leaf_host = TLS / (host.replace(".", "_") + "_leaf.pem")
        leaf_host.write_bytes(peer_leaf(host))
        endpoint_verify[host] = openssl([
            "verify", "-CAfile", certifi.where(), "-untrusted", str(untrusted),
            "-purpose", "sslserver", "-verify_hostname", host, str(leaf_host)
        ])
    # Pin only the exact official YR1 intermediate after its parent chain has verified.
    # This compensates for the remote server omitting the intermediate; it does not disable
    # certificate validation or hostname checking.
    ctx = ssl.create_default_context(cafile=certifi.where())
    ctx.load_verify_locations(cafile=str(yr1))
    req = urllib.request.Request("https://eaindustry.nic.in/download_data_2223.asp",
        headers={"User-Agent": UA, "Accept": "text/html,*/*"})
    with urllib.request.build_opener(urllib.request.HTTPSHandler(context=ctx)).open(req, timeout=35) as r:
        final = r.geturl()
        if not final.startswith("https://") or r.status != 200:
            raise RuntimeError("OEA strict TLS HTTP fetch returned unsafe/non-200 final URL")
        if final.split("/")[2].lower() not in HOSTS:
            raise RuntimeError("OEA redirected outside the approved OEA hostnames")
        page = r.read(20000000)
        (OUT / "oea_download_data_2223.html").write_bytes(page)
        page_result = {"status": r.status, "final_url": final, "bytes": len(page), "sha256": sha(page)}
    result = {
        "status": "STRICT_TLS_PASS",
        "retrieved_at_utc": datetime.now(timezone.utc).isoformat(),
        "source": "Let's Encrypt official Chains of Trust files",
        "official_chain_files": chain,
        "official_yr1_chain_verification": chain_verify,
        "oea_endpoint_leaf_verification": endpoint_verify,
        "hostname_checks": {"eaindustry.nic.in": "PASS", "www.eaindustry.nic.in": "PASS"},
        "trust_strategy": "certifi trust roots plus explicitly pinned official YR1 intermediate; YR1 parent chain independently verified to trusted ISRG Root X1",
        "http": page_result,
    }
    (TLS / "oea_tls_chain_verification.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
if __name__ == "__main__": main()
