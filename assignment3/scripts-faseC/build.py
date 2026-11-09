import json,glob,collections,os,sys,csv
base=sys.argv[1]; out=sys.argv[2]
TN={'mauve':'MAUVE++','achecks':'AChecker','achecks_lighthouse':'Lighthouse (ACHECKS)','accessibilitychecker':'AccessibilityChecker'}
LV={'1.1.1':'A','1.2.1':'A','1.3.1':'A','1.3.3':'A','1.3.5':'AA','1.4.1':'A','1.4.3':'AA','1.4.4':'AA','1.4.5':'AA','1.4.10':'AA','1.4.12':'AA','2.1.1':'A','2.3.1':'A','2.4.1':'A','2.4.2':'A','2.4.4':'A','2.4.5':'AA','2.4.6':'AA','2.4.7':'AA','2.5.3':'A','3.1.2':'AA','3.2.3':'AA','3.2.4':'AA','3.3.1':'A','3.3.2':'A','3.3.3':'AA','3.3.4':'AA','4.1.2':'A','4.1.3':'AA'}
pages={}
for f in sorted(glob.glob(os.path.join(base,'results','*.json'))):
    pages[os.path.basename(f)[:-5]]=json.load(open(f))
short=lambda u:u.split('/assignment3/')[1] or '/'
# CSV
with open(os.path.join(base,'issues.csv'),'w',newline='') as fh:
    w=csv.writer(fh); w.writerow(['url','strumento','criterio','livello','descrizione','elemento','occorrenze'])
    for s,d in pages.items():
        for t,v in d['tools'].items():
            for i in v.get('issues',[]):
                tec=i.get('tecnica') or i.get('check_id')
                desc=f"[{i['tipo']}] [{tec}] {i['descrizione']}"
                w.writerow([d['url'],TN[t],i.get('criterio') or '',i.get('livello') or '',desc,' | '.join(i['elemento']),i.get('occorrenze')])
# per criterio
C=collections.defaultdict(lambda:{'lv':set(),'err':set(),'warn':set(),'tools':collections.defaultdict(set),'occ_e':0,'occ_w':0,'tec':set()})
for s,d in pages.items():
    for t,v in d['tools'].items():
        for i in v.get('issues',[]):
            if not i.get('criterio'): continue
            for c in [x.strip() for x in i['criterio'].split(',')]:
                r=C[c]; r['lv'].add(LV.get(c,i['livello']))
                tec=i.get('tecnica') or ('#'+i['check_id'])
                r['tec'].add(f"{TN[t].split()[0]} {tec}{'' if i['tipo']=='error' else '*'}")
                r['tools'][TN[t]+(' (errore)' if i['tipo']=='error' else ' (avviso)')].add(s)
                if i['tipo']=='error': r['err'].add(s); r['occ_e']+=i['occorrenze'] or 0
                else: r['warn'].add(s); r['occ_w']+=i['occorrenze'] or 0
L=[]
def lvl(c):
    import re
    return c
rows=sorted(C.items(),key=lambda x:(-len(x[1]['err']),-len(x[1]['err']|x[1]['warn']),[int(p) for p in x[0].split('.')]))
L.append('| Criterio | Liv. | Pagine con errore | Pagine coinvolte (errori o avvisi) | Strumenti (pagine) | Occ. errori | Occ. avvisi |')
L.append('|---|---|---|---|---|---|---|')
for c,r in rows:
    tl='; '.join(f"{k}: {len(v)}" for k,v in sorted(r['tools'].items()))
    L.append(f"| {c} | {'/'.join(sorted(r['lv']))} | {len(r['err'])} | {len(r['err']|r['warn'])} | {tl} | {r['occ_e']} | {r['occ_w']} |")
L.append('')
# top 10 pages
P=[]
for s,d in pages.items():
    m=d['tools']['mauve']; a=d['tools']['achecks']
    occ=sum(i['occorrenze'] for t in ('mauve','achecks') for i in d['tools'][t]['issues'] if i['tipo']=='error')
    ne=sum(1 for t in ('mauve','achecks') for i in d['tools'][t]['issues'] if i['tipo']=='error')
    P.append((occ,ne,s,d,m,a))
P.sort(key=lambda x:(-x[0],-x[1],x[4]['score']))
L.append('| # | Pagina | Template | Occorrenze di errore (MAUVE++ + AChecker) | Tecniche/controlli in errore | MAUVE++ % | Criteri in errore MAUVE++ | Errori AChecker | Avvisi AChecker |')
L.append('|---|---|---|---|---|---|---|---|---|')
for n,(occ,ne,s,d,m,a) in enumerate(P[:10],1):
    L.append(f"| {n} | `{short(d['url'])}` | {d['template']} | {occ} | {ne} | {m['score']} | {m['errors']} | {a['errors']} | {a['warnings']} |")
L.append('')
# full page table
L.append('| Pagina | Template | MAUVE++ % | MAUVE++ err/avv | AChecker err/avv | Lighthouse | AccessibilityChecker |')
L.append('|---|---|---|---|---|---|---|')
for s,d in sorted(pages.items(),key=lambda x:x[1]['url']):
    m=d['tools']['mauve']; a=d['tools']['achecks']; l=d['tools']['achecks_lighthouse']; ac=d['tools']['accessibilitychecker']
    acs={'ok':f"{ac['score']} (0 critici)",'skipped':'skipped','error':'error'}[ac['status']]
    L.append(f"| `{short(d['url'])}` | {d['template']} | {m['score']} | {m['errors']}/{m['warnings']} | {a['errors']}/{a['warnings']} | {l['score']} | {acs} |")
open(os.path.join(out,'tables.md'),'w').write('\n'.join(L))
print('\n'.join(L))
