#!/usr/bin/env python3
"""BV-R002 v0.3.1: offline comparison of two pinned public CSV files (stdlib only)."""
import argparse
import csv
import hashlib
import json
import math
from datetime import date, timedelta
from decimal import Decimal
from pathlib import Path

START = date(2009, 1, 3)
END = date(2020, 2, 15)
HEADER = 'date,cdd,closed_btc,created_btc,dormancy,hodl_0_1d,hodl_1d_1w,hodl_1m_3m,hodl_1w_1m,hodl_1y_2y,hodl_2y_plus,hodl_3m_6m,hodl_6m_1y,live_utxo_count,raw_inputs,spent_btc,supply_btc'.split(',')
SOURCES = [
    dict(tag='v1.0.0', sha256='e8dae3aa663bec46f8848a8bc09c7ded1d2e35bb8a8cf649d653a0ff91882ee9', bytes=1133743, rows=4062, last='2020-02-16'),
    dict(tag='v2.0.0', sha256='3ad5f40c86988e525f06b3e7db67a5494c9e911f0bcba9abc31c6dda9be54d0b', bytes=1848820, rows=6473, last='2026-09-23'),
]
DAILY_HEADER = ['date', 'delta_spent_sats', 'delta_raw_inputs', 'changed_fields']
EP_HEADER = ['start','end','days','positive_spent_sats','negative_spent_sats','net_spent_sats','positive_inputs','negative_inputs','net_inputs']

def require(condition, message):
    if not condition:
        raise ValueError(message)

def exact_int(s, factor=1):
    x = Decimal(s) * factor
    require(x.is_finite() and x == x.to_integral_value() and x >= 0, 'Non-integral or negative value: '+s)
    return int(x)

def read_source(path, spec):
    raw = path.read_bytes()
    require(len(raw) == spec['bytes'] and hashlib.sha256(raw).hexdigest() == spec['sha256'], f"Source mismatch: {spec['tag']}")
    lines = raw.decode('ascii').splitlines()
    reader = csv.reader(lines, strict=True)
    require(next(reader) == HEADER, 'Unexpected schema')
    data = {}
    for i, row in enumerate(reader):
        require(len(row) == len(HEADER), 'Row width mismatch')
        day = START + timedelta(days=i)
        require(row[0] == day.isoformat(), 'Noncontiguous or duplicate dates')
        data[day] = dict(zip(HEADER, row))
    require(len(data) == spec['rows'] and max(data).isoformat() == spec['last'], 'Unexpected coverage')
    return data

def group_episodes(daily):
    groups = []
    for row in daily:
        if not groups or date.fromisoformat(row['date']) - date.fromisoformat(groups[-1][-1]['date']) != timedelta(days=1):
            groups.append([])
        groups[-1].append(row)
    result=[]
    for g in groups:
        s=[r['delta_spent_sats'] for r in g]; n=[r['delta_raw_inputs'] for r in g]
        result.append(dict(start=g[0]['date'], end=g[-1]['date'], days=len(g),
            positive_spent_sats=sum(max(v,0) for v in s), negative_spent_sats=sum(min(v,0) for v in s), net_spent_sats=sum(s),
            positive_inputs=sum(max(v,0) for v in n), negative_inputs=sum(min(v,0) for v in n), net_inputs=sum(n)))
    return result

def compare(a,b):
    counts=dict.fromkeys(HEADER[1:],0); daily=[]
    dorm=[dict(checked=0,changed_dates_checked=0,zero_spent=0,zero_spent_missing_dormancy=0,max_abs_error=0.0) for _ in range(2)]
    for i in range((END-START).days+1):
        day=START+timedelta(days=i); r,s=a[day],b[day]
        changed=[k for k in HEADER[1:] if r[k]!=s[k]]
        for k in changed: counts[k]+=1
        spent=[exact_int(x['spent_btc'],100000000) for x in (r,s)]
        inputs=[exact_int(x['raw_inputs']) for x in (r,s)]
        for j,x in enumerate((r,s)):
            st=dorm[j]; c,sp=map(float,(x['cdd'],x['spent_btc']))
            label=f"{SOURCES[j]['tag']} {day}"
            require(all(map(math.isfinite,(c,sp))), f'Nonfinite Dormancy input: {label}')
            if spent[j]==0:
                require(c==0 and x['dormancy']=='', f'Expected zero CDD and missing Dormancy for zero Spent BTC: {label}')
                st['zero_spent']+=1; st['zero_spent_missing_dormancy']+=1
            else:
                require(x['dormancy']!='', f'Missing Dormancy with nonzero Spent BTC: {label}')
                d=float(x['dormancy'])
                require(math.isfinite(d), f'Nonfinite Dormancy: {label}')
                st['checked']+=1; st['changed_dates_checked']+=int(bool(changed))
                st['max_abs_error']=max(st['max_abs_error'],abs(d-c/sp))
        if changed:
            daily.append(dict(date=day.isoformat(),delta_spent_sats=spent[1]-spent[0],delta_raw_inputs=inputs[1]-inputs[0],changed_fields='|'.join(changed)))
    return counts,daily,dorm

def summary(counts,daily,dorm,episodes):
    return dict(sources=SOURCES, start=START.isoformat(),end=END.isoformat(),excluded='2020-02-16',dates=(END-START).days+1, compared_values=((END-START).days+1)*16, differing_values=sum(counts.values()), differences_by_metric=counts, differing_dates=len(daily), episodes=len(episodes), balanced_episodes=sum(x['net_spent_sats']==0 and x['net_inputs']==0 for x in episodes), positive_spent_sats=sum(x['positive_spent_sats'] for x in episodes),negative_spent_sats=sum(x['negative_spent_sats'] for x in episodes),net_spent_sats=sum(x['net_spent_sats'] for x in episodes),positive_inputs=sum(x['positive_inputs'] for x in episodes),negative_inputs=sum(x['negative_inputs'] for x in episodes),net_inputs=sum(x['net_inputs'] for x in episodes),dormancy_binary64=dorm)

def write_csv(path, fields, records):
    with path.open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fields,lineterminator='\n'); w.writeheader(); w.writerows(records)

def write_results(out, counts,daily,dorm):
    out.mkdir(parents=True,exist_ok=True)
    episodes=group_episodes(daily)
    write_csv(out/'daily_diff.csv',DAILY_HEADER,daily)
    write_csv(out/'episodes.csv',EP_HEADER,episodes)
    report=summary(counts,daily,dorm,episodes)
    (out/'summary.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    return report

def check_report(report):
    require(report['dates']==4061 and report['compared_values']==64976, 'Unexpected overlap')
    require(report['differences_by_metric']=={k:43 if k in ('dormancy','raw_inputs','spent_btc') else 0 for k in HEADER[1:]},'Unexpected differing metrics')
    require(report['differing_dates']==43 and report['episodes']==report['balanced_episodes']==21, 'Unexpected episode counts/balance')
    require(report['positive_spent_sats']==2407702250364 and report['negative_spent_sats']==-2407702250364 and report['net_spent_sats']==0,'Unexpected monetary balance')
    require(report['positive_inputs']==1164 and report['negative_inputs']==-1164 and report['net_inputs']==0,'Unexpected input balance')
    for d in report['dormancy_binary64']:
        require(d['checked']==3801 and d['changed_dates_checked']==43 and d['zero_spent']==d['zero_spent_missing_dormancy']==260 and d['max_abs_error']<=1e-12,'Unexpected Dormancy identity result')

def main():
    p=argparse.ArgumentParser(description=__doc__); p.add_argument('v1',type=Path); p.add_argument('v2',type=Path); p.add_argument('--out',type=Path,default=Path('reproduced'))
    a=p.parse_args(); counts,daily,dorm=compare(read_source(a.v1,SOURCES[0]),read_source(a.v2,SOURCES[1])); report=write_results(a.out,counts,daily,dorm); check_report(report); print('PASS: pinned files, 43 dates, 21 balanced episodes, Dormancy identity')

if __name__=='__main__': main()
