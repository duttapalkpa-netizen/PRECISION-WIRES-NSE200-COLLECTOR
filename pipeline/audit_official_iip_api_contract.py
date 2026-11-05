#!/usr/bin/env python3
"""Fetch and fingerprint the official e-Sankhyiki IIP Swagger contract; no data API calls."""
from __future__ import annotations
import hashlib, json, time
from pathlib import Path
from urllib.request import Request, urlopen
import yaml

URL='https://esankhyiki.mospi.gov.in/layout/swagger_user_iip.yaml'
ROOT=Path('artifacts/iip_api_contract')
SRC=ROOT/'source'
SRC.mkdir(parents=True,exist_ok=True)
raw_path=SRC/'swagger_user_iip.yaml'
last_error=None
for attempt in range(1,4):
    try:
        req=Request(URL,headers={'User-Agent':'PRECISION-WIRES-IIP-contract-audit/1.0','Accept':'application/yaml,text/yaml,text/plain,*/*'})
        with urlopen(req,timeout=30) as resp:
            raw=resp.read()
            status=getattr(resp,'status',None)
            content_type=resp.headers.get('Content-Type','')
        if len(raw)<100: raise ValueError(f'spec payload too small: {len(raw)} bytes')
        raw_path.write_bytes(raw)
        break
    except Exception as exc:
        last_error=f'{type(exc).__name__}: {exc}'
        if attempt==3:
            report={'status':'BLOCKED_OFFICIAL_SPEC_NOT_ACQUIRED','source_url':URL,'attempts':attempt,'error':last_error}
            (ROOT/'iip_api_contract_audit.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
            print(json.dumps(report,indent=2)); raise SystemExit(2)
        time.sleep(attempt*2)
sha=hashlib.sha256(raw).hexdigest()
try:
    spec=yaml.safe_load(raw.decode('utf-8-sig'))
except Exception as exc:
    report={'status':'BLOCKED_OFFICIAL_SPEC_PARSE_FAILED','source_url':URL,'sha256':sha,'bytes':len(raw),'error':f'{type(exc).__name__}: {exc}'}
    (ROOT/'iip_api_contract_audit.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    print(json.dumps(report,indent=2)); raise SystemExit(2)
if not isinstance(spec,dict) or not isinstance(spec.get('paths'),dict):
    raise SystemExit('BLOCKED: fetched YAML is not an OpenAPI document with paths')
paths=[]
for path,item in spec['paths'].items():
    if not isinstance(item,dict): continue
    for method,op in item.items():
        if method.lower() not in ('get','post','put','delete','patch') or not isinstance(op,dict): continue
        params=[]
        for p in op.get('parameters',[]) or []:
            sch=p.get('schema',{}) if isinstance(p,dict) else {}
            params.append({'name':p.get('name'),'in':p.get('in'),'required':p.get('required',False),'type':sch.get('type'),'enum':sch.get('enum'),'default':sch.get('default'),'description':p.get('description')})
        paths.append({'path':path,'method':method.upper(),'operationId':op.get('operationId'),'security':op.get('security'),'parameters':params})
iip_ops=[p for p in paths if 'iip' in p['path'].lower()]
has_2022_23=any('2022-23' in (param.get('enum') or []) for op in iip_ops for param in op['parameters'] if param.get('name')=='base_year')
report={'status':'OFFICIAL_SPEC_FETCHED_REQUIRES_SCHEMA_REVIEW','source_url':URL,'http_status':status,'content_type':content_type,'bytes':len(raw),'sha256':sha,'openapi':spec.get('openapi'),'info':spec.get('info'),'servers':spec.get('servers'),'iip_operations':iip_ops,'security_schemes':spec.get('components',{}).get('securitySchemes',{}),'base_year_2022_23_declared':has_2022_23,'data_api_called':False,'note':'This audit fetches only the official contract. It does not call the data endpoint, infer parameters, or assume a token is unnecessary.'}
(ROOT/'iip_api_contract_audit.json').write_text(json.dumps(report,indent=2,ensure_ascii=False),encoding='utf-8')
print(json.dumps(report,indent=2,ensure_ascii=False))
