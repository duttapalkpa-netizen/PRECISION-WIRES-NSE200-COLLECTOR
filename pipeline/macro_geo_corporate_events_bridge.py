#!/usr/bin/env python3
"""Bridge validated NSE disclosure ledger rows into the corporate-events factor schema."""
from pathlib import Path
import json
import pandas as pd
ROOT=Path('.')
RAW=ROOT/'data/raw'
OUT=ROOT/'data/external/corporate_events.csv'
REPORT=ROOT/'outputs/macro_geo/corporate_events_bridge_report.json'
OFFICIAL=('https://www.nseindia.com/','https://nsearchives.nseindia.com/','https://archives.nseindia.com/')
COLS=['DATE','SYMBOL','EVENT_TYPE','PUBLISHED_AT','SOURCE_URL','SOURCE','OBSERVED_AT_UTC','EVENT_DATE_BASIS']
def read_rows(path, kind):
 if not path.exists(): return [], {'path':str(path),'status':'MISSING_INPUT','rows':0}
 df=pd.read_csv(path,dtype=str).fillna(''); df.columns=[str(c).strip().upper() for c in df.columns]
 out=[]; rejected={'missing_symbol':0,'missing_publication_timestamp':0,'non_official_source_url':0}
 for row in df.to_dict('records'):
  symbol=str(row.get('SYMBOL','')).strip().upper(); raw=str(row.get('PUBLICATION_TIMESTAMP','') or row.get('BROADCAST_AT','')).strip(); stamp=pd.to_datetime(raw,errors='coerce',utc=True); url=str(row.get('SOURCE_URL','') or row.get('ATTACHMENT_URL','')).strip()
  if not symbol: rejected['missing_symbol']+=1; continue
  if pd.isna(stamp): rejected['missing_publication_timestamp']+=1; continue
  if not url.startswith(OFFICIAL): rejected['non_official_source_url']+=1; continue
  subject=str(row.get('SUBJECT','')).strip(); event=str(row.get('EVENT_KIND',kind)).strip() or kind
  out.append({'DATE':stamp.date().isoformat(),'SYMBOL':symbol,'EVENT_TYPE':event+(': '+subject if subject else ''),'PUBLISHED_AT':stamp.isoformat(),'SOURCE_URL':url,'SOURCE':'NSE official filing ledger','OBSERVED_AT_UTC':pd.Timestamp.now(tz='UTC').isoformat(),'EVENT_DATE_BASIS':'PUBLICATION_DATE_NOT_CONFIRMED_OCCURRENCE_DATE'})
 return out,{'path':str(path),'status':'READ','rows':len(df),'accepted':len(out),'rejected':rejected}
def main():
 rows=[]; inputs=[]
 for name,kind in [('quarterly_results_disclosures.csv','RESULT_DISCLOSURE'),('quarterly_results_calendar.csv','BOARD_MEETING_CALENDAR')]:
  found,rep=read_rows(RAW/name,kind); rows.extend(found); inputs.append(rep)
 df=pd.DataFrame(rows,columns=COLS)
 if not df.empty: df=df.drop_duplicates(['SYMBOL','EVENT_TYPE','PUBLISHED_AT','SOURCE_URL']).sort_values(['PUBLISHED_AT','SYMBOL'])
 OUT.parent.mkdir(parents=True,exist_ok=True); df.to_csv(OUT,index=False)
 report={'status':'AVAILABLE_WITH_VALIDATED_ROWS' if len(df) else 'BLOCKED_NO_VALID_OFFICIAL_ROWS','rows':int(len(df)),'date_min':str(df.DATE.min()) if len(df) else None,'date_max':str(df.DATE.max()) if len(df) else None,'output':str(OUT),'inputs':inputs,'required_contract':COLS,'event_date_policy':'DATE is publication date, not confirmed occurrence date.','missing_data_semantics':'UNKNOWN/BLOCKED, never zero or negative.'}
 REPORT.parent.mkdir(parents=True,exist_ok=True); REPORT.write_text(json.dumps(report,indent=2)); print(json.dumps(report,indent=2)); return 0
if __name__=='__main__': raise SystemExit(main())