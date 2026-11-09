import json,glob,collections,os,sys
base=sys.argv[1]
c=collections.defaultdict(collections.Counter)
for f in sorted(glob.glob(os.path.join(base,'results','*.json'))):
    d=json.load(open(f))
    for t,v in d['tools'].items():
        if t not in('mauve','achecks'): continue
        for i in v.get('issues',[]):
            if t=='achecks' and i['tipo']=='warning': continue
            k=(t,i['tipo'],i.get('tecnica') or i.get('check_id'))
            for e in i['elemento']: c[k][e[:160]]+=1
for k,v in c.items():
    print('##',k)
    for e,n in v.most_common(6): print('  ',n,e)
