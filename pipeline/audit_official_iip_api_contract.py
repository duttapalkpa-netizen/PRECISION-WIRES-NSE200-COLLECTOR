#!/usr/bin/env python3
"""Fetch and strictly assess the current official e-Sankhyiki IIP API contract; never call data API."""
from __future__ import annotations
import hashlib,json,re,time
from pathlib import Path
from urllib.request import Request,urlopen
import yaml

URL='https://esankhyiki.mospi.gov.in/layout/swagger_user_iip.yaml'
ROOT=Path('artifacts/iip_api_contract'); SRC=ROOT/'source'; SRC.mkdir(parents=True,exist_ok=True)
raw_path=SRC/'swagger_user_iip.yaml'
def save(report):
    (ROOT/'iip_api_contract_audit.json').write_text(json.dumps(report,indent=2,ensure_ascii=False),encoding='utf-8')
    print(json.dumps(report,indent=2,ensure_ascii=False))
raw=None; last_error=None; status_code=None; content_type=None
for attempt in range(1,4):
    try:
        req=Request(URL,headers={'User-Agent':'PRECISION-WIRES-IIP-contract-audit/2.0','Accept':'application/yaml,text/yaml,text/plain,*/*'})
        with urlopen(req,timeout=30) as resp:
            raw=resp.read(); status_code=getattr(resp,'status',None); content_type=resp.headers.get('Content-Type','')
        if len(raw)<100: raise ValueError(f'payload too small: {len(raw)} bytes')
        break
    except Exception as exc:
        last_error=f'{type(exc).__name__}: {exc}'
        if attempt<3: time.sleep(attempt*2)
if raw is None:
    save({'status':'BLOCKED_OFFICIAL_SPEC_NOT_ACQUIRED','source_url':URL,'attempts':3,'error':last_error,'data_api_called':False}); raise SystemExit(2)
raw_path.write_bytes(raw); sha=hashlib.sha256(raw).hexdigest()
try: spec=yaml.safe_load(raw.decode('utf-8-sig'))
except Exception as exc:
    save({'status':'BLOCKED_OFFICIAL_SPEC_PARSE_FAILED','source_url':URL,'sha256':sha,'bytes':len(raw),'error':f'{type(exc).__name__}: {exc}','data_api_called':False}); raise SystemExit(2)
if not isinstance(spec,dict) or not isinstance(spec.get('paths'),dict):
    save({'status':'BLOCKED_NOT_OPENAPI','source_url':URL,'sha256':sha,'bytes':len(raw),'data_api_called':False}); raise SystemExit(2)
operations=[]
for path,item in spec['paths'].items():
    if not isinstance(item,dict): continue
    for method,op in item.items():
        if method.lower() not in ('get','post','put','delete','patch') or not isinstance(op,dict): continue
        params=[]
        for p in op.get('parameters',[]) or []:
            if not isinstance(p,dict): continue
            sch=p.get('schema',{}) or {}
            params.append({'name':p.get('name'),'in':p.get('in'),'required':p.get('required',False),'type':sch.get('type'),'enum':sch.get('enum'),'default':sch.get('default'),'description':p.get('description')})
        operations.append({'path':path,'method':method.upper(),'operationId':op.get('operationId'),'summary':op.get('summary'),'security':op.get('security',spec.get('security')),'parameters':params})
iip_ops=[o for o in operations if 'iip' in o['path'].lower() or 'iip' in str(o.get('operationId','')).lower()]
expected=[o for o in iip_ops if 'getiipdata' in (o['path']+' '+str(o.get('operationId',''))).lower()]
baseyear_params=[p for o in iip_ops for p in o['parameters'] if p['name'] and p['name'].lower() in ('base_year','baseyear','baseyearcode') ]
supports_2022=any('2022-23' in (p.get('enum') or []) or p.get('default')=='2022-23' for p in baseyear_params)
security=spec.get('components',{}).get('securitySchemes',{})
auth_declared=bool(security) or any(o.get('security') for o in iip_ops)
status='CONTRACT_COMPATIBLE_REVIEW_REQUIRED' if expected and supports_2022 else 'BLOCKED_LEGACY_OR_INCOMPLETE_CONTRACT'
report={'status':status,'source_url':URL,'http_status':status_code,'content_type':content_type,'bytes':len(raw),'sha256':sha,'openapi':spec.get('openapi'),'swagger':spec.get('swagger'),'info':spec.get('info'),'servers':spec.get('servers'),'iip_operations':iip_ops,'expected_getIIPData_operation_found':bool(expected),'base_year_parameters':baseyear_params,'base_year_2022_23_declared':supports_2022,'authentication_declared':auth_declared,'security_schemes':security,'data_api_called':False,'interpretation':'The contract is accepted for further manual review only when the IIP data operation and 2022-23 base-year parameter are both explicitly declared. An older operation or missing base-year enum is a blocker; do not reuse old parameters or assume authentication is optional.'}
save(report)
if status!='CONTRACT_COMPATIBLE_REVIEW_REQUIRED': raise SystemExit(2)
