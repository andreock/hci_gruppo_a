import json,glob,collections,os,sys
base=sys.argv[1]
pages={}
for f in sorted(glob.glob(os.path.join(base,'results','*.json'))):
    d=json.load(open(f)); pages[os.path.basename(f)[:-5]]=d
st=collections.Counter(); keys=collections.Counter()
for s,d in pages.items():
    for t,v in d['tools'].items():
        st[(t,v['status'])]+=1
        for i in v.get('issues',[]): keys.update(i.keys())
print(st); print(keys)
# per tool, unique (tipo, criterio, tecnica/check_id, descr)
agg=collections.defaultdict(lambda:[set(),0])
for s,d in pages.items():
    for t,v in d['tools'].items():
        for i in v.get('issues',[]):
            k=(t,i.get('tipo'),i.get('criterio'),i.get('livello'),i.get('tecnica') or i.get('check_id') or i.get('id'),i.get('descrizione')[:80])
            agg[k][0].add(s); agg[k][1]+=i.get('occorrenze') or 0
for k,v in sorted(agg.items(),key=lambda x:(x[0][0],x[0][1],-len(x[1][0]))):
    print(len(v[0]),v[1],k)
for s,d in pages.items():
    print(s,d['template'],[(t,v['status'],v['score'],v['errors'],v['warnings']) for t,v in d['tools'].items() if t!='accessibilitychecker'])
for s,d in pages.items():
    a=d['tools']['accessibilitychecker']
    if a['status']!='skipped': print('AC',s,a['status'],a['score'],a['errors'],a['warnings'],len(a.get('issues',[])),a['note'][:200])
