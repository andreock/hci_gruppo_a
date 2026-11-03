#!/usr/bin/env python3
"""Genera docs/05_tracciabilita.md da 02, 03, 04 e tools/soluzioni.py. Uso (da website/): python3 tools/genera-tracciabilita.py"""
import re, sys, collections, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from soluzioni import S, MATRICE, AREE
D = str(pathlib.Path(__file__).resolve().parent.parent / "docs")
def rows(path):
    for l in open(f'{D}/{path}', encoding='utf-8'):
        if l.startswith('| ') and not l.startswith('|---'):
            yield [c.strip() for c in l.strip().strip('|').split(' | ')]
# 02
probs = []
for r in rows('02_problemi_consolidati.md'):
    if re.fullmatch(r'P-\d{3}', r[0]):
        pid, desc, page, heur, wcag, g, gsrc, fonti = r[:8]
        extra = r[8] if len(r) > 8 else ''
        s = re.split(r'(?<=[a-zà-ù\)»]):\s|;\s', desc)[0]
        if len(s) > 110: s = s[:107].rsplit(' ', 1)[0] + '…'
        probs.append(dict(id=pid, s=s, fonti=fonti, h=heur, w=wcag, g=g, gsrc=gsrc, extra=extra))
# 03: P-xxx -> journey codes ; persona from section
pj = collections.defaultdict(set)
for r in rows('03_bisogni_personas.md'):
    if re.fullmatch(r'J\d\d-F\d', r[0]):
        for p in re.findall(r'P-\d{3}', r[-1]): pj[p].add(r[0])
bneeds = collections.defaultdict(set)
for l in open(f'{D}/03_bisogni_personas.md', encoding='utf-8'):
    m = re.match(r'- (B\d\d-\d) ', l)
    if m:
        for p in re.findall(r'P-\d{3}', l): bneeds[p].add(m.group(1)[:3].replace('B', 'P'))
# 04
reqs = []; sec = None; pr = collections.defaultdict(list)
for l in open(f'{D}/04_requisiti.md', encoding='utf-8'):
    m = re.match(r'## (\d+)\. (.*)', l)
    if m: sec = m.group(2).strip()
    if l.startswith('| R-'):
        c = [x.strip() for x in l.strip().strip('|').split(' | ')]
        reqs.append(dict(id=c[0], desc=c[1], orig=c[2], p=c[3], area=sec))
        for p in re.findall(r'P-\d{3}', c[2]): pr[p].append(c[0])
out = []
w = out.append
w('# 05 · Tracciabilità problema → requisito → soluzione\n')
w('Documento centrale della consegna, aggiornato alla fine della Fase 5 (31/10/2026). Generato da `tools/genera-tracciabilita.py` a partire da `02_problemi_consolidati.md`, `03_bisogni_personas.md`, `04_requisiti.md` e `tools/soluzioni.py`. Le verifiche rimandano ai report in `docs/verifiche/` («percorsi #n» = controllo n di `percorsi.md`) e a `08_verifica_personas.md`.\n')
w('Le sigle delle fonti sono spiegate in `02_problemi_consolidati.md`. La colonna «Personas e journey» riporta i punti di dolore `Jxx-Fn` di `03_bisogni_personas.md` e, tra parentesi, le personas i cui bisogni (`Bxx-n`) citano il problema.\n')
w('## 1. Problema → soluzione\n')
w('| ID problema | Problema (sintesi) | Fonte in assignment1 | Euristica di Nielsen | Criterio WCAG | Gravità | Personas e journey coinvolti | Requisito (R-xxx) | Soluzione adottata | Dove | Verifica | Stato |')
w('|---|---|---|---|---|---|---|---|---|---|---|---|')
noreq = []
for p in probs:
    js = sorted(pj.get(p['id'], []))
    ps = sorted(bneeds.get(p['id'], set()) - {j[:3].replace('J', 'P') for j in js})
    pjtxt = ', '.join(js) + ((' (' + ', '.join(ps) + ')') if ps else '')
    rq = ', '.join(pr.get(p['id'], [])) or '—'
    if rq == '—': noreq.append(p['id'])
    if p['id'] in ('P-088', 'P-089', 'P-090'):
        stato = 'non applicabile'; sol = p['extra']; dove = '—'; ver = '—'
    else:
        sol, dove, ver, stato = S[p['id']]
    w(f"| {p['id']} | {p['s']} | {p['fonti']} | {p['h']} | {p['w']} | {p['g']} | {pjtxt or '—'} | {rq} | {sol} | {dove} | {ver} | {stato} |")
w('')
w('## 2. Requisito → origine\n')
w('Ogni requisito deriva da almeno un problema o da un bisogno di una persona (o da un vincolo della consegna).\n')
w('| Requisito | Area | Priorità | Origine (problemi, bisogni, journey, vincoli) | Problemi collegati |')
w('|---|---|---|---|---|')
for r in reqs:
    ps = ', '.join(sorted(set(re.findall(r'P-\d{3}', r['orig'])))) or '— (bisogno di persona o vincolo)'
    w(f"| {r['id']} | {r['area']} | {r['p']} | {r['orig']} | {ps} |")
w('')
w('## 3. Matrice personas × aree del sito\n')
w('Soluzioni del sito che rispondono ai bisogni di ciascuna persona (dettaglio e prove in `08_verifica_personas.md`).\n')
w('| Persona | ' + ' | '.join(AREE) + ' |')
w('|---' * (len(AREE) + 1) + '|')
for k, v in MATRICE.items():
    w(f'| {k} | ' + ' | '.join(v) + ' |')
w('')
w('## 4. Sintesi della copertura\n')
cnt = collections.defaultdict(lambda: collections.Counter())
def cat(st):
    return 'non applicabile' if st.startswith('non applicabile') else 'parziale' if st.startswith('parziale') else 'non risolto' if st.startswith('non risolto') else 'risolto'
for p in probs:
    st = 'non applicabile' if p['id'] in ('P-088', 'P-089', 'P-090') else S[p['id']][3]
    cnt[p['g']][cat(st)] += 1
w('| Gravità | Problemi | Risolti | Parziali | Non risolti | Non applicabili |')
w('|---|---|---|---|---|---|')
tot = collections.Counter()
for g in ['4', '3', '2', '1', 'n.d.']:
    c = cnt[g]; tot.update(c)
    w(f"| {g} | {sum(c.values())} | {c['risolto']} | {c['parziale']} | {c['non risolto']} | {c['non applicabile']} |")
w(f"| **Totale** | **{sum(tot.values())}** | **{tot['risolto']}** | **{tot['parziale']}** | **{tot['non risolto']}** | **{tot['non applicabile']}** |")
w('')
w('- **Parziali**: nessuno.')
w('- **Non applicabili** (P-088, P-089, P-090): catalogo dei partner (il sito ha un solo ente), risorse `http` e metadato social del fornitore; motivazioni nella tabella 1.')
w('- **Non risolti**: nessuno.')
w(f'- Problemi coperti da almeno un requisito: {len(probs) - len(noreq)} su {len(probs)}; senza requisito: {", ".join(noreq) or "nessuno"} (non applicabili).')
w(f'- Requisiti: {len(reqs)}, tutti con un\'origine documentata (tabella 2).')
w('- Residui emersi dalla valutazione euristica del nuovo sito (`09_valutazione_euristica.md`): nessun problema di gravità 3 o 4; un problema di gravità 2 aperto (V-03, ripresa della donazione su un altro dispositivo).')
open(f'{D}/05_tracciabilita.md', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('probs', len(probs), 'reqs', len(reqs), 'noreq', noreq, dict(tot))
