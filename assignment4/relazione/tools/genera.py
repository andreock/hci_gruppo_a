#!/usr/bin/env python3
"""Genera la relazione dell'Assignment 4 a partire da modello.html e dai CSV in ../dati.
Uso (da assignment4):  python3 relazione/tools/genera.py [--dati CARTELLA] [--senza-pdf]
Scrive relazione/relazione.html e relazione/assignment4_gruppoA.pdf e stampa l'elenco di ciò che manca."""
import argparse, csv, html, json, os, re, statistics, struct, subprocess, sys
QUI = os.path.dirname(os.path.abspath(__file__)); REL = os.path.dirname(QUI); A4 = os.path.dirname(REL)
sys.path.insert(0, QUI)
from task import TASK, SUS, DEFINIZIONI, URL_TEST, URL_DOPO  # noqa: E402

e = html.escape
VUOTO = '<td class="vuoto">—</td>'
MANCA, ERRORI = [], []
ESITI = {"S": ("b-s", "completato da solo"), "A": ("b-a", "completato con aiuto"), "F": ("b-f", "non completato")}
COL = {"S": "#2a7d4f", "A": "#c98a10", "F": "#b3301f"}  # verificati con il validatore della palette (CVD e contrasto)
DIM = {"Tempo": "Efficienza", "Esito": "Efficacia", "Errore": "Efficacia", "Richiesta di aiuto": "Efficacia",
       "Blocco": "Efficienza", "Facilità percepita (SEQ)": "Soddisfazione"}

def leggi(cartella, nome):
    with open(os.path.join(cartella, nome), encoding="utf-8-sig", newline="") as f:
        return [{k: (v or "").strip() for k, v in r.items()} for r in csv.DictReader(f)]

def intero(v, dove, minimo=0, massimo=None):
    if v == "": MANCA.append(dove); return None
    try: n = int(v)
    except ValueError: ERRORI.append(f"{dove}: «{v}» non è un numero intero"); return None
    if n < minimo or (massimo is not None and n > massimo): ERRORI.append(f"{dove}: {n} fuori dall'intervallo {minimo}–{massimo if massimo is not None else '∞'}"); return None
    return n

def secondi(v, dove):
    """Accetta «95» (secondi) oppure «1:35» (minuti:secondi)."""
    if v == "": MANCA.append(dove); return None
    m = re.fullmatch(r"(\d+):([0-5]\d)", v)
    if m: return int(m.group(1)) * 60 + int(m.group(2))
    if v.isdigit(): return int(v)
    ERRORI.append(f"{dove}: «{v}» non è un tempo valido (usare secondi oppure min:sec)"); return None

def mmss(s): return "—" if s is None else f"{int(round(s)) // 60}:{int(round(s)) % 60:02d}"
def num(x, dec=1): return "—" if x is None else (f"{x:.{dec}f}".replace(".", ",") if dec else str(int(x)))
def td(v, cls=""): return VUOTO if v in (None, "") else f'<td{" class=" + chr(34) + cls + chr(34) if cls else ""}>{e(str(v))}</td>'
def tdn(v, fmt=str): return '<td class="n vuoto">—</td>' if v is None else f'<td class="n">{fmt(v)}</td>'
def badge(esito): return f'<span class="badge {ESITI[esito][0]}">{esito}</span>' if esito in ESITI else "—"
def utente(u): return "Utente " + u.lstrip("Uu")

# ------------------------------------------------------------------ dati
def carica(cartella):
    D = {"part": leggi(cartella, "partecipanti.csv"), "sus": {r["utente"]: r for r in leggi(cartella, "sus.csv")},
         "int": {r["utente"]: r for r in leggi(cartella, "intervista.csv")}, "prob": leggi(cartella, "problemi.csv"),
         "task": {r["task"]: r for r in leggi(cartella, "task.csv")}}
    D["utenti"] = [r["utente"] for r in D["part"]]
    S = {}
    for r in leggi(cartella, "sessioni.csv"):
        dove = f'sessioni.csv {r["utente"]}/{r["task"]}'
        if r["utente"] not in D["utenti"]: ERRORI.append(f"{dove}: utente non presente in partecipanti.csv"); continue
        esito = r["esito"].upper()
        if esito == "": MANCA.append(dove + " esito")
        elif esito not in ESITI: ERRORI.append(f"{dove}: esito «{esito}» non valido (S, A o F)"); esito = ""
        S[(r["utente"], r["task"])] = {
            "esito": esito, "tempo": secondi(r["tempo_s"], dove + " tempo_s"), "errori": intero(r["errori"], dove + " errori"),
            "aiuti": intero(r["aiuti"], dove + " aiuti"), "blocchi": intero(r["blocchi"], dove + " blocchi"),
            "seq": intero(r["seq_1_7"], dove + " seq_1_7", 1, 7), "oss": r["osservazioni"], "cit": r["citazioni"]}
        if not r["osservazioni"]: MANCA.append(dove + " osservazioni")
    for u in D["utenti"]:
        for t in TASK:
            if (u, t["id"]) not in S: ERRORI.append(f"sessioni.csv: manca la riga {u}/{t['id']}")
    D["ses"] = S
    D["susp"] = {}
    for u in D["utenti"]:
        r = D["sus"].get(u, {})
        q = [intero(r.get(f"q{i}", ""), f"sus.csv {u} q{i}", 1, 5) for i in range(1, 11)]
        D["susp"][u] = (q, None if None in q else 2.5 * sum((v - 1) if i % 2 == 0 else (5 - v) for i, v in enumerate(q)))
    for r in D["part"]:
        for k, v in r.items():
            if v == "": MANCA.append(f'partecipanti.csv {r["utente"]} {k}')
    for u in D["utenti"]:
        r = D["int"].get(u, {})
        for k in ("cosa_e_piaciuto", "cosa_non_e_piaciuto", "cosa_cambierebbe"):
            if not r.get(k): MANCA.append(f"intervista.csv {u} {k}")
    return D

def sintesi_task(D, tid):
    righe = [D["ses"][(u, tid)] for u in D["utenti"] if (u, tid) in D["ses"]]
    conta = {k: sum(1 for r in righe if r["esito"] == k) for k in ESITI}
    tempi = [r["tempo"] for r in righe if r["esito"] in ("S", "A") and r["tempo"] is not None]
    def somma(k):
        v = [r[k] for r in righe if r[k] is not None]; return sum(v) if v else None
    seq = [r["seq"] for r in righe if r["seq"] is not None]
    return {"n": sum(conta.values()), "conta": conta, "tempi": tempi, "mediana": statistics.median(tempi) if tempi else None,
            "errori": somma("errori"), "aiuti": somma("aiuti"), "blocchi": somma("blocchi"), "seq": statistics.mean(seq) if seq else None}

# ------------------------------------------------------------------ blocchi HTML
def tab_soggetti(D):
    return "\n".join(f'<tr><th scope="row">{utente(r["utente"])}</th>' + td(r["fascia_eta"]) + td(r["genere"]) + td(r["occupazione"]) + td(r["titolo_studio"])
                     + td(r["competenza_digitale_1_5"], "n") + td(r["acquisti_online"]) + td(r["familiarita_crowdfunding"]) + td(r["ha_donato_online"]) + "</tr>" for r in D["part"])

def tab_sessioni(D):
    return "\n".join(f'<tr><th scope="row">{utente(r["utente"])}</th>' + td(r["data"]) + td(r["modalita"]) + td(r["dispositivo"]) + td(r["browser"])
                     + td(r["durata_min"], "n") + td(r["facilitatore"]) + td(r["osservatore"]) + "</tr>" for r in D["part"])

def sintesi_soggetti(D):
    comp = [int(r["competenza_digitale_1_5"]) for r in D["part"] if r["competenza_digitale_1_5"].isdigit()]
    if len(comp) < len(D["part"]): return '<p><span class="todo">Sintesi del campione: verrà calcolata quando la tabella 3 è completa.</span></p>'
    def conta(campo):
        c = {}
        for r in D["part"]: c[r[campo]] = c.get(r[campo], 0) + 1
        return ", ".join(f"{v} «{e(k.lower())}»" for k, v in sorted(c.items(), key=lambda x: -x[1]))
    return (f'<p>In sintesi: fasce d\'età {conta("fascia_eta")}; confidenza con il web da {min(comp)} a {max(comp)} su 5 (mediana {num(statistics.median(comp))}); '
            f'familiarità con il crowdfunding: {conta("familiarita_crowdfunding")}; modalità: {conta("modalita")}.</p>')

def blocco_task(D):
    out = []
    for i, t in enumerate(TASK, 1):
        lim = D["task"].get(t["id"], {}).get("tempo_limite_s", "")
        esp = D["task"].get(t["id"], {}).get("tempo_esperto_s", "")
        if esp == "": MANCA.append(f'task.csv {t["id"]} tempo_esperto_s')
        out.append(f"""<div class="testa"><h3 id="s4-{i}">{t['id']} · {e(t['titolo'])}</h3>
<p class="meta"><span class="badge b-tool">{e(t['percorso'])}</span> <span class="badge b-tool">Tempo limite {mmss(int(lim)) if lim.isdigit() else '—'}</span> <span class="badge b-tool">Tempo dell'esperto {mmss(int(esp)) if esp.isdigit() else 'da misurare'}</span></p>
<div class="scenario"><p>{e(t['scenario'])}</p></div></div>
<div class="tre">
<div class="box box--ok"><span class="box__tit">Completato se</span><p>{e(t['successo'])}</p></div>
<div class="box box--info"><span class="box__tit">Percorso più breve</span><p>{e(t['ottimale'])}</p></div>
<div class="box box--problema"><span class="box__tit">Contati come errori</span><p>{e(t['errori'])}</p></div>
</div>""")
    out.append(f"""<div class="coppia">
<figure><img src="img/t0-home.png" alt="Home di ideaBlume: titolo, ricerca, pulsante «Scopri i progetti in corso» e progetto in evidenza"><figcaption><b>Figura 1.</b> La home da cui parte ogni task (versione provata).</figcaption></figure>
<figure><img src="img/t3-donazione.png" alt="Primo passo della donazione: scelta dell'importo o della ricompensa"><figcaption><b>Figura 2.</b> Il primo dei cinque passi della donazione (T3).</figcaption></figure>
</div>""")
    return "\n".join(out)

def tab_sintesi(D):
    righe = []
    for t in TASK:
        s = sintesi_task(D, t["id"]); n = len(D["utenti"]); esp = D["task"].get(t["id"], {}).get("tempo_esperto_s", "")
        c = lambda k: f'<td class="n">{s["conta"][k]}/{n}</td>' if s["n"] else '<td class="n vuoto">—</td>'
        righe.append(f'<tr><th scope="row">{t["id"]} · {e(t["titolo"])}</th>{c("S")}{c("A")}{c("F")}{tdn(s["mediana"], mmss)}'
                     + (f'<td class="n">{mmss(min(s["tempi"]))}–{mmss(max(s["tempi"]))}</td>' if s["tempi"] else '<td class="n vuoto">—</td>')
                     + tdn(int(esp) if esp.isdigit() else None, mmss) + tdn(s["errori"]) + tdn(s["aiuti"]) + tdn(s["blocchi"]) + tdn(s["seq"], num) + "</tr>")
    return "\n".join(righe)

def tab_per_task(D):
    out = []
    for i, t in enumerate(TASK):
        s = sintesi_task(D, t["id"]); righe = []
        for u in D["utenti"]:
            r = D["ses"].get((u, t["id"]))
            if not r: continue
            righe.append(f'<tr><th scope="row">{utente(u)}</th>' + (f"<td>{badge(r['esito'])} {ESITI[r['esito']][1]}</td>" if r["esito"] else VUOTO)
                         + tdn(r["tempo"], mmss) + tdn(r["errori"]) + tdn(r["aiuti"]) + tdn(r["blocchi"]) + tdn(r["seq"]) + "</tr>")
        tot = (f'<tr class="gruppo"><th scope="row">Sintesi</th><th>{s["conta"]["S"]} S · {s["conta"]["A"]} A · {s["conta"]["F"]} F</th>'
               f'<th class="n">mediana {mmss(s["mediana"])}</th><th class="n">{num(s["errori"], 0)}</th><th class="n">{num(s["aiuti"], 0)}</th><th class="n">{num(s["blocchi"], 0)}</th><th class="n">media {num(s["seq"])}</th></tr>') if s["n"] else ""
        out.append(f"""<div class="tabella compatta"><table>
<caption><b>Tabella {6 + i}.</b> {t['id']} · {e(t['titolo'])}: misure per utente</caption>
<thead><tr><th>Utente</th><th>Esito</th><th class="n">Tempo (min:s)</th><th class="n">Errori</th><th class="n">Richieste di aiuto</th><th class="n">Blocchi</th><th class="n">Facilità (1–7)</th></tr></thead>
<tbody>{"".join(righe)}{tot}</tbody></table></div>""")
    return "\n".join(out)

def tab_per_utente(D):
    righe = []
    for u in D["utenti"]:
        rr = [D["ses"].get((u, t["id"])) for t in TASK]; rr = [r for r in rr if r]
        def somma(k):
            v = [r[k] for r in rr if r[k] is not None]; return sum(v) if len(v) == len(TASK) else None
        soli = sum(1 for r in rr if r["esito"] == "S") if all(r["esito"] for r in rr) and rr else None
        righe.append(f'<tr><th scope="row">{utente(u)}</th>' + "".join(f"<td>{badge(r['esito'])}</td>" if r["esito"] else VUOTO for r in rr)
                     + tdn(soli, lambda x: f"{x} su {len(TASK)}") + tdn(somma("tempo"), mmss) + tdn(somma("errori")) + tdn(somma("aiuti")) + tdn(somma("blocchi")) + tdn(D["susp"][u][1], num) + "</tr>")
    return "\n".join(righe)

def qualitativi(D):
    out = []
    for i, u in enumerate(D["utenti"], 1):
        p = next(r for r in D["part"] if r["utente"] == u)
        profilo = " · ".join(x for x in (p["fascia_eta"] and p["fascia_eta"] + " anni", p["occupazione"], p["familiarita_crowdfunding"] and "crowdfunding: " + p["familiarita_crowdfunding"].lower()) if x)
        righe = []
        for t in TASK:
            r = D["ses"].get((u, t["id"]))
            if not r: continue
            cit = "".join(f"<blockquote>«{e(c.strip().strip('«»\"'))}»</blockquote>" for c in re.split(r"\s*\|\s*", r["cit"]) if c.strip())
            righe.append(f'<tr><th scope="row">{t["id"]} {badge(r["esito"]) if r["esito"] else ""}</th>' + (f"<td>{e(r['oss'])}</td>" if r["oss"] else VUOTO) + f"<td>{cit or '—'}</td></tr>")
        out.append(f"""<div class="tabella compatta"><table>
<caption><b>{utente(u)}</b>{" · " + e(profilo) if profilo else ""}</caption>
<thead><tr><th style="width:11%">Task</th><th style="width:50%">Comportamento osservato</th><th>Frasi dette</th></tr></thead>
<tbody>{"".join(righe)}</tbody></table></div>""")
    return "\n".join(out)

def tab_sus(D):
    righe = []
    for u in D["utenti"]:
        q, p = D["susp"][u]
        righe.append(f'<tr><th scope="row">{utente(u)}</th>' + "".join(tdn(v) for v in q) + tdn(p, num) + "</tr>")
    punti = [p for _, p in D["susp"].values() if p is not None]
    if punti:
        righe.append(f'<tr class="gruppo"><th scope="row" colspan="11">Media ({len(punti)} utenti) · mediana {num(statistics.median(punti))} · min {num(min(punti))} · max {num(max(punti))}</th><th class="n">{num(statistics.mean(punti))}</th></tr>')
    return "\n".join(righe)

def giudizio_sus(m):
    for soglia, agg in ((85.5, "eccellente"), (72.6, "buono"), (52.0, "accettabile (OK)"), (39.2, "scarso")):
        if m >= soglia: return agg
    return "pessimo"

def sus_commento(D):
    punti = [p for _, p in D["susp"].values() if p is not None]
    if len(punti) < len(D["utenti"]): return '<p><span class="todo">Il punteggio medio e il commento compaiono quando tutte le risposte al SUS sono inserite.</span></p>'
    m = statistics.mean(punti); sotto = [utente(u) for u in D["utenti"] if D["susp"][u][1] < 68]
    # affermazioni con il contributo medio più basso (0–4): indicano dove il giudizio è peggiore
    contr = []
    for i in range(10):
        v = [D["susp"][u][0][i] for u in D["utenti"]]; contr.append((statistics.mean((x - 1) if i % 2 == 0 else (5 - x) for x in v), i))
    peggio = sorted(contr)[:2]
    return (f'<p>Il punteggio medio è <strong>{num(m)}</strong> su 100 (da {num(min(punti))} a {num(max(punti))}), {"sopra" if m >= 68 else "sotto"} la media di riferimento di 68: '
            f'nella scala di aggettivi di Bangor corrisponde a «{giudizio_sus(m)}». '
            + (f'Sotto 68: {", ".join(sotto)}. ' if sotto else "Nessun utente è sotto 68. ")
            + "Le affermazioni con il giudizio medio peggiore sono la " + " e la ".join(f"{i + 1} («{e(SUS[i])}», contributo medio {num(c)} su 4)" for c, i in peggio)
            + '.</p><p><span class="todo">Commento: il SUS misura la percezione, non la prestazione. Confrontarlo con la tabella 10: chi ha dato un punteggio alto ha anche completato i task da solo?</span></p>')

def tab_intervista(D):
    righe = []
    for u in D["utenti"]:
        r = D["int"].get(u, {})
        righe.append(f'<tr><th scope="row">{utente(u)}</th>' + td(r.get("cosa_e_piaciuto")) + td(r.get("cosa_non_e_piaciuto")) + td(r.get("cosa_cambierebbe")) + f'<td>{e(r.get("altro", "")) or "—"}</td></tr>')
    return "\n".join(righe)

def misure(cartella):
    """Misure prima/dopo scritte da prima_dopo.py: nei testi di problemi.csv si citano con {prima:p5.telefono.y_prima_scheda_px}."""
    p = os.path.join(cartella, "misure.json")
    return json.load(open(p, encoding="utf-8")) if os.path.exists(p) else {}

def con_misure(testo, M, dove):
    def val(m):
        v = M.get(m.group(1), {})
        for k in m.group(2).split("."):
            v = v.get(k) if isinstance(v, dict) else None
        if v is None: ERRORI.append(f"{dove}: misura {m.group(0)} non trovata in misure.json (lanciare prima_dopo.py)"); return "?"
        return {True: "sì", False: "no"}.get(v, str(v)) if isinstance(v, bool) else str(v)
    return re.sub(r"\{(prima|dopo):([\w.]+)\}", val, testo)

def problemi(D, M):
    n = len(D["utenti"]); P = []
    for r in D["prob"]:
        if not r["id"]: continue
        dove = "problemi.csv " + r["id"]
        r = {k: con_misure(v, M, dove) for k, v in r.items()}
        us = [x.strip().upper() for x in re.split(r"[;, ]+", r["utenti"]) if x.strip()]
        for x in us:
            if x not in D["utenti"]: ERRORI.append(f"{dove}: utente «{x}» sconosciuto")
        org = r.get("origine", "").lower() or "test"
        if org not in ("test", "ispezione"): ERRORI.append(f"{dove}: origine «{org}» non valida (test o ispezione)")
        P.append({**r, "us": us, "org": org, "imp": intero(r["impatto_1_3"], dove + " impatto", 1, 3), "per": intero(r["persistenza_1_3"], dove + " persistenza", 1, 3),
                  "g": intero(r["gravita_0_4"], dove + " gravità", 0, 4)})
        for k in ("titolo", "descrizione", "dove", "task"):
            if not r[k]: MANCA.append(f"{dove} {k}")
        if not us: MANCA.append(f"{dove} utenti (chi lo ha incontrato nelle sessioni; se nessuno, rivedere la gravità)")
        if not r["evidenza"]: MANCA.append(f"{dove} evidenza (che cosa hanno fatto o detto gli utenti)")
        if (P[-1]["g"] or 0) >= 2 and not r["soluzione"]: MANCA.append(f"{dove} soluzione")
    P.sort(key=lambda p: (-(p["g"] if p["g"] is not None else -1), -len(p["us"]), p["id"]))
    if not P: MANCA.append("problemi.csv: nessun problema inserito")
    return P, n

NOMI_G = {4: "4 · catastrofe", 3: "3 · grave", 2: "2 · minore", 1: "1 · cosmetico", 0: "0 · non è un problema"}
def bg(g, stima=False): return "—" if g is None else f'<span class="badge b-g{g}">{NOMI_G[g]}{" (stima)" if stima else ""}</span>'
def bgp(p): return bg(p["g"], stima=not p["us"])
def origine(p): return '<span class="badge b-c1">ispezione</span>' if p["org"] == "ispezione" else '<span class="badge b-c2">test</span>'
def freq(p, n): return f'<td class="n">{len(p["us"])} su {n}</td>' if p["us"] else '<td class="n vuoto">da rilevare</td>'

def tab_problemi(P, n):
    if not P: return f'<tr><td class="vuoto" colspan="10">Da compilare in dati/problemi.csv dopo la riunione di sintesi.</td></tr>'
    return "\n".join(f'<tr><th scope="row">{e(p["id"])}</th><td>{e(p["titolo"])}</td><td>{e(p["task"])}</td><td>{origine(p)}</td>'
                     + (f'<td>{e(", ".join(p["us"]))}</td>' if p["us"] else VUOTO) + freq(p, n)
                     + f'{tdn(p["imp"])}{tdn(p["per"])}<td>{bgp(p)}</td></tr>' for p in P)

def problemi_dettaglio(P, n):
    if not P: return ""
    out = ['<h3 id="s8-1">I problemi uno per uno</h3>']
    for p in P:
        visto = (f"<p><strong>Che cosa è successo nelle sessioni.</strong> {e(p['evidenza'])}</p>" if p["evidenza"] else
                 '<p><strong>Che cosa è successo nelle sessioni.</strong> <span class="todo">Da scrivere: quali utenti lo hanno incontrato, che cosa hanno fatto e detto, con quali conseguenze (errori, aiuti, tempo). Se nessuno lo ha incontrato, dirlo e abbassare la gravità.</span></p>')
        out.append(f"""<div class="blocco"><div class="testa"><h4>{e(p['id'])} · {e(p['titolo'])}</h4>
<p class="meta">{bgp(p)} {origine(p)} <span class="badge b-tool">{e(p['task'])}</span> <span class="badge b-tool">{f"{len(p['us'])} utenti su {n}" if p['us'] else "frequenza da rilevare"}</span> <span class="badge b-tool">{e(p['dove'])}</span></p></div>
<p>{e(p['descrizione'])}</p>"""
                   + (f"<p><strong>Misura sulla versione provata.</strong> {e(p['misura_prima'])}</p>" if p["misura_prima"] else "") + visto + "</div>")
    return "\n".join(out)

def dim_png(percorso):
    with open(percorso, "rb") as f: t = f.read(24)
    return struct.unpack(">II", t[16:24]) if t[:8] == b"\x89PNG\r\n\x1a\n" else (0, 0)

def figura(src, alt, did):
    if not src: return "", False
    pieno = os.path.join(REL, src)
    if not os.path.exists(pieno): ERRORI.append(f"immagine non trovata: {src}"); return "", False
    w, h = dim_png(pieno)
    return f'<figure><img src="{e(src)}" alt="{e(alt)}"><figcaption>{did}</figcaption></figure>', (0 < w <= 420 or h > w * 1.2)

def redesign(P):
    fatti = [p for p in P if p["stato"].lower().startswith("fatt")]
    if not fatti:
        return '<div class="box box--todo"><span class="box__tit">Da fare dopo il test</span><p>Il re-design parte dai problemi di <code>dati/problemi.csv</code>: per ognuno vanno compilate le colonne <code>tipo_intervento</code>, <code>soluzione</code>, <code>file_modificati</code>, <code>stato</code> («fatto») e, se utili, le schermate <code>img_prima</code> e <code>img_dopo</code>.</p></div>'
    out, nf = [], 3
    out.append('<div class="tabella compatta"><table><caption><b>Tabella 15.</b> Interventi di re-design, problemi da cui nascono e risultato misurato sulle due versioni</caption><thead><tr><th style="width:20%">Problema</th><th>Gravità</th><th>Tipo di intervento</th><th>Prima</th><th>Dopo</th></tr></thead><tbody>'
               + "".join(f'<tr><th scope="row" style="white-space:normal">{e(p["id"])} · {e(p["titolo"])}</th><td>{bgp(p)}</td><td>{e(p["tipo_intervento"])}</td><td>{e(p["misura_prima"]) or "—"}</td><td>{e(p["misura_dopo"]) or "—"}</td></tr>' for p in fatti) + "</tbody></table></div>")
    for p in fatti:
        fig = ""
        if p["img_prima"] or p["img_dopo"]:
            a, stretta = figura(p["img_prima"], f"Prima: {p['titolo']}", f"<b>Figura {nf}.</b> Prima: la versione provata dagli utenti.")
            b, _ = figura(p["img_dopo"], f"Dopo: {p['titolo']}", f"<b>Figura {nf + 1}.</b> Dopo il re-design.")
            nf += 2; fig = f'<div class="coppia{" coppia--tel" if stretta else ""}">{a}{b}</div>'
        out.append(f"""<div class="blocco"><div class="testa"><h3>{e(p['id'])} · {e(p['titolo'])}</h3>
<p class="meta">{bgp(p)} <span class="badge b-c2">{e(p['tipo_intervento'])}</span> <span class="badge b-tool">{e(p['task'])}</span> <span class="hash">{e(p['file_modificati'])}</span></p></div>
<div class="tre">
<div class="box box--problema"><span class="box__tit">Il problema</span><p>{e(p['misura_prima'] or p['descrizione'])}</p></div>
<div class="box box--info"><span class="box__tit">Che cosa abbiamo cambiato</span><p>{e(p['soluzione'])}</p></div>
<div class="box box--ok"><span class="box__tit">Risultato misurato</span><p>{e(p['misura_dopo']) or '—'}</p></div>
</div>{fig}</div>""")
    return "\n".join(out)

def non_corretti(P):
    resto = [p for p in P if not p["stato"].lower().startswith("fatt")]
    if not P: return '<p><span class="todo">Elenco dei problemi lasciati aperti, con il motivo.</span></p>'
    if not resto: return '<p>Tutti i problemi della tabella 14 sono stati corretti. <span class="todo">Se dalle sessioni emergono altri problemi, aggiungerli a <code>problemi.csv</code> con origine «test»: quelli non corretti compaiono qui con il motivo.</span></p>'
    return "<ul>" + "".join(f"<li><strong>{e(p['id'])} · {e(p['titolo'])}</strong> ({bgp(p)}): {e(p['soluzione'] or 'motivo da indicare nella colonna «soluzione»')}</li>" for p in resto) + "</ul>"

# ------------------------------------------------------------------ grafici (SVG statici per la stampa)
INK, MUTED, GRIGLIA = "#3b1d2a", "#5f4e45", "#e6dcd0"
def svg(w, h, corpo, titolo): return f'<svg viewBox="0 0 {w} {h}" role="img" aria-label="{e(titolo)}" font-family="Inter, Arial, sans-serif">{corpo}</svg>'

def grafico_esiti(D):
    n = len(D["utenti"]); w, x0, larg, hr = 360, 34, 300, 30; c = []
    for i, t in enumerate(TASK):
        s = sintesi_task(D, t["id"]); y = 8 + i * hr; x = x0
        c.append(f'<text x="0" y="{y + 13}" font-size="10" font-weight="600" fill="{INK}">{t["id"]}</text>')
        for k in ("S", "A", "F"):
            v = s["conta"][k]
            if not v: continue
            lw = larg * v / n
            c.append(f'<rect x="{x:.1f}" y="{y}" width="{max(lw - 2, 1):.1f}" height="18" rx="3" fill="{COL[k]}"/><text x="{x + lw / 2 - 1:.1f}" y="{y + 13}" font-size="9.5" font-weight="700" fill="#fff" text-anchor="middle">{v} {k}</text>')
            x += lw
    h = 8 + len(TASK) * hr
    return ('<figure class="grafico"><figcaption>Esito dei task<span>Numero di utenti su ' + str(n) + ' per ogni esito</span></figcaption>' + svg(w, h, "".join(c), "Esito dei task per numero di utenti")
            + f'<p class="legenda"><i style="background:{COL["S"]}"></i>S da solo<i style="background:{COL["A"]}"></i>A con aiuto<i style="background:{COL["F"]}"></i>F non completato</p></figure>')

def grafico_tempi(D):
    tutti = [r["tempo"] for r in D["ses"].values() if r["tempo"] is not None]
    lim = [int(v["tempo_limite_s"]) for v in D["task"].values() if v["tempo_limite_s"].isdigit()]
    mx = max(tutti + lim); mx = (int(mx / 60) + 1) * 60
    w, x0, larg, hr = 360, 34, 310, 30; X = lambda s: x0 + larg * s / mx; c = []
    h = 8 + len(TASK) * hr + 16; passo = 60 if mx <= 480 else 120
    for s in range(0, mx + 1, passo):
        c.append(f'<line x1="{X(s):.1f}" y1="4" x2="{X(s):.1f}" y2="{h - 16}" stroke="{GRIGLIA}" stroke-width="1"/><text x="{X(s):.1f}" y="{h - 4}" font-size="8.5" fill="{MUTED}" text-anchor="middle">{s // 60} min</text>')
    for i, t in enumerate(TASK):
        y = 8 + i * hr + 9; s = sintesi_task(D, t["id"])
        c.append(f'<text x="0" y="{y + 4}" font-size="10" font-weight="600" fill="{INK}">{t["id"]}</text>')
        esp = D["task"].get(t["id"], {}).get("tempo_esperto_s", "")
        if esp.isdigit(): c.append(f'<path d="M{X(int(esp)):.1f} {y - 9} l4 6 l-8 0 z" fill="{INK}"/>')
        for u in D["utenti"]:
            r = D["ses"].get((u, t["id"]))
            if r and r["tempo"] is not None and r["esito"]:
                c.append(f'<circle cx="{X(r["tempo"]):.1f}" cy="{y}" r="4.5" fill="{COL[r["esito"]]}" stroke="#fffdf9" stroke-width="1.5"/>')
        if s["mediana"] is not None: c.append(f'<line x1="{X(s["mediana"]):.1f}" y1="{y - 9}" x2="{X(s["mediana"]):.1f}" y2="{y + 9}" stroke="{INK}" stroke-width="2"/>')
    return ('<figure class="grafico"><figcaption>Tempo per task<span>Un punto per utente, colore = esito</span></figcaption>' + svg(w, h, "".join(c), "Tempo impiegato da ogni utente per ogni task")
            + '<p class="legenda">| mediana dei task completati &nbsp; ▼ tempo dell\'esperto</p></figure>')

def grafico_sus(D):
    w, x0, larg, hr = 360, 56, 270, 19; X = lambda v: x0 + larg * v / 100; c = []; h = 6 + len(D["utenti"]) * hr + 16
    for v in (0, 25, 50, 75, 100): c.append(f'<line x1="{X(v):.1f}" y1="2" x2="{X(v):.1f}" y2="{h - 16}" stroke="{GRIGLIA}"/><text x="{X(v):.1f}" y="{h - 4}" font-size="8.5" fill="{MUTED}" text-anchor="middle">{v}</text>')
    for i, u in enumerate(D["utenti"]):
        p = D["susp"][u][1]; y = 6 + i * hr
        c.append(f'<text x="0" y="{y + 10}" font-size="9.5" fill="{INK}">{utente(u)}</text>')
        if p is not None: c.append(f'<rect x="{x0}" y="{y}" width="{max(larg * p / 100, 1):.1f}" height="13" rx="3" fill="#1d5b73"/><text x="{X(p) - 4 if p >= 20 else X(p) + 4:.1f}" y="{y + 10}" font-size="9.5" font-weight="700" fill="{'#fff' if p >= 20 else INK}" text-anchor="{'end' if p >= 20 else 'start'}">{num(p)}</text>')
    c.append(f'<line x1="{X(68):.1f}" y1="0" x2="{X(68):.1f}" y2="{h - 16}" stroke="{INK}" stroke-width="1.5" stroke-dasharray="4 3"/>')
    return ('<figure class="grafico"><figcaption>Punteggio SUS per utente<span>Da 0 a 100; linea tratteggiata = media di riferimento (68)</span></figcaption>' + svg(w, h, "".join(c), "Punteggio SUS di ogni utente") + "</figure>")

def grafico_errori(D):
    w, x0, larg, hr = 360, 34, 250, 30; c = []; S = [sintesi_task(D, t["id"]) for t in TASK]
    mx = max([1] + [(s["errori"] or 0) for s in S] + [(s["aiuti"] or 0) for s in S] + [(s["blocchi"] or 0) for s in S])
    for i, (t, s) in enumerate(zip(TASK, S)):
        y = 6 + i * hr
        c.append(f'<text x="0" y="{y + 15}" font-size="10" font-weight="600" fill="{INK}">{t["id"]}</text>')
        for j, (k, col) in enumerate((("errori", "#b3301f"), ("aiuti", "#1d5b73"), ("blocchi", "#8a6d1b"))):
            v = s[k] or 0; yy = y + j * 8
            c.append(f'<rect x="{x0}" y="{yy}" width="{max(larg * v / mx, 1):.1f}" height="6" rx="2" fill="{col}"/><text x="{x0 + larg * v / mx + 4:.1f}" y="{yy + 6}" font-size="8" fill="{INK}">{v}</text>')
    return ('<figure class="grafico"><figcaption>Errori, richieste di aiuto e blocchi<span>Totale degli utenti per ogni task</span></figcaption>' + svg(w, 6 + len(TASK) * hr, "".join(c), "Errori, richieste di aiuto e blocchi per task")
            + '<p class="legenda"><i style="background:#b3301f"></i>errori<i style="background:#1d5b73"></i>richieste di aiuto<i style="background:#8a6d1b"></i>blocchi</p></figure>')

def grafici(D):
    if not any(r["esito"] for r in D["ses"].values()):
        return '<div class="box box--todo"><span class="box__tit">Grafici</span><p>I grafici (esito dei task, tempi, errori e SUS) vengono disegnati automaticamente quando <code>dati/sessioni.csv</code> e <code>dati/sus.csv</code> contengono dati.</p></div>'
    return f'<div class="grafici">{grafico_esiti(D)}{grafico_tempi(D)}</div><div class="grafici" style="margin-top:8pt">{grafico_errori(D)}{grafico_sus(D)}</div><p class="piccolo"><b>Figure 3–6.</b> I valori esatti sono nelle tabelle 5–11.</p>'

def cifre(D):
    es = [r["esito"] for r in D["ses"].values() if r["esito"]]; punti = [p for _, p in D["susp"].values() if p is not None]
    P = [p for p in D["prob"] if p["id"]]
    def c(v, t): return f'<div class="cifra"><b>{v}</b><span>{t}</span></div>'
    return (c(len(D["utenti"]), "utenti, " + str(len(TASK)) + " task ciascuno") + c(f'{es.count("S")} su {len(es)}' if es else "—", "task completati senza aiuto")
            + c(num(statistics.mean(punti)) if punti else "—", "punteggio SUS medio (0–100)") + c(len(P) if P else "—", "problemi di usabilità classificati"))

# ------------------------------------------------------------------ indice e PDF (come nell'Assignment 3)
def sostituisci(testo, marca, contenuto):
    return re.sub(rf"(<!--{marca}:INIZIO-->).*?(<!--{marca}:FINE-->)", lambda m: m.group(1) + "\n" + contenuto + "\n" + m.group(2), testo, flags=re.S)
def norm(s): return re.sub(r"\s+", "", s).replace("’", "'")
def voci_indice(testo):
    voci = []
    for liv, idv, corpo in re.findall(r'<h([23]) id="([^"]+)"[^>]*>(.*?)</h\1>', testo, flags=re.S):
        if idv == "indice": continue
        n = re.search(r'<span class="num">(.*?)</span>', corpo)
        tit = re.sub(r"<[^>]+>", "", re.sub(r'<span class="num">.*?</span>', "", corpo)).strip()
        voci.append((int(liv), idv, n.group(1) if n else "", html.unescape(tit)))
    return voci
def indice(voci, pagine):
    return "\n".join(f'<li class="l{l}"><a href="#{i}">{e((n + "  " if n else "") + t)}</a><span class="pun" aria-hidden="true"></span><span class="pag">{pagine.get(i, "–")}</span></li>' for l, i, n, t in voci)
def pagine_pdf(voci, pdf):
    n = int(re.search(r"Pages:\s+(\d+)", subprocess.run(["pdfinfo", pdf], capture_output=True, text=True).stdout).group(1))
    testi = [norm(subprocess.run(["pdftotext", "-f", str(i), "-l", str(i), "-layout", pdf, "-"], capture_output=True, text=True).stdout) for i in range(1, n + 1)]
    da = next(i for i, t in enumerate(testi) if norm(voci[-1][2] + voci[-1][3]) in t) + 1; trovate = {}
    for l, idv, nu, tit in voci:
        for i in range(da, n):
            if norm(nu + tit) in testi[i]: trovate[idv] = i + 1; da = i; break
        else: print("  titolo non trovato nel PDF:", nu, tit, file=sys.stderr)
    return trovate, n

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--dati", default=os.path.join(A4, "dati")); ap.add_argument("--senza-pdf", action="store_true")
    ap.add_argument("--uscita", default=REL, help="cartella in cui scrivere relazione.html e il PDF")
    a = ap.parse_args()
    D = carica(a.dati); P, n = problemi(D, misure(a.dati))
    testo = open(os.path.join(REL, "modello.html"), encoding="utf-8").read()
    testo = re.sub(r"<!-- Questo è il MODELLO.*?-->\n", "<!-- File generato da tools/genera.py: modificare modello.html e i CSV in ../dati, non questo file. -->\n", testo, flags=re.S)
    blocchi = {
        "URL_TEST": URL_TEST, "URL_DOPO": URL_DOPO, "N_UTENTI": str(len(D["utenti"])), "CIFRE": cifre(D),
        "CONTESTO": "", "DEFINIZIONI": "".join(f'<tr><th scope="row">{e(k)}</th><td>{DIM[k]}</td><td>{e(v)}</td></tr>' for k, v in DEFINIZIONI),
        "TAB_SOGGETTI": tab_soggetti(D), "TAB_SESSIONI": tab_sessioni(D), "SINTESI_SOGGETTI": sintesi_soggetti(D), "TASK": blocco_task(D),
        "TAB_SINTESI": tab_sintesi(D), "GRAFICI": grafici(D), "TAB_PER_TASK": tab_per_task(D), "TAB_PER_UTENTE": tab_per_utente(D),
        "QUALITATIVI": qualitativi(D), "TAB_SUS": tab_sus(D), "SUS_COMMENTO": sus_commento(D), "TAB_INTERVISTA": tab_intervista(D),
        "TAB_PROBLEMI": tab_problemi(P, n), "PROBLEMI_DETTAGLIO": problemi_dettaglio(P, n), "REDESIGN": redesign(P), "NON_CORRETTI": non_corretti(P),
        "SUS_ITEM": "".join(f"<li>{e(q)}</li>" for q in SUS),
    }
    for k, v in blocchi.items(): testo = testo.replace("{{" + k + "}}", v)
    da_scrivere = len(re.findall(r'class="todo"', testo))
    blocchi = {}
    blocchi["STATO_BOZZA"] = "" if not (MANCA or ERRORI or da_scrivere) else (
        f'<div class="box box--todo"><span class="box__tit">Bozza: la relazione non è ancora completa</span><p>Mancano <strong>{len(MANCA)}</strong> valori nei file di dati e '
        f'<strong>{da_scrivere}</strong> parti di testo da scrivere (evidenziate in giallo). Le celle gialle con «—» sono dati non ancora raccolti. Questo riquadro sparisce da solo quando tutto è compilato.</p></div>')
    for k, v in blocchi.items(): testo = testo.replace("{{" + k + "}}", v)
    resto = re.findall(r"\{\{[A-Z_]+\}\}", testo)
    if resto: ERRORI.append("segnaposto non sostituiti: " + ", ".join(resto))
    testo = testo.replace("<p></p>\n", "")
    os.makedirs(a.uscita, exist_ok=True)
    out_html = os.path.join(a.uscita, "relazione.html"); out_pdf = os.path.join(a.uscita, "assignment4_gruppoA.pdf")
    if os.path.abspath(a.uscita) != REL:  # uscita di prova: i percorsi relativi di CSS e immagini puntano alla cartella vera
        testo = testo.replace('href="relazione.css"', f'href="file://{REL}/relazione.css"').replace('src="img/', f'src="file://{REL}/img/')
    voci = voci_indice(testo); pagine = {}
    for giro in range(6):
        testo = sostituisci(testo, "INDICE", indice(voci, pagine))
        open(out_html, "w", encoding="utf-8").write(testo)
        if a.senza_pdf: break
        subprocess.run(["node", os.path.join(QUI, "genera_pdf.js"), out_html, out_pdf], check=True, capture_output=True)
        nuove, np_ = pagine_pdf(voci, out_pdf)
        if nuove == pagine: print(f"PDF: {out_pdf} ({np_} pagine)"); break
        pagine = nuove
    if ERRORI:
        print(f"\nERRORI nei dati ({len(ERRORI)}):"); [print("  ✗", x) for x in ERRORI]
    print(f"\nDa completare: {len(MANCA)} valori nei CSV, {da_scrivere} testi nel modello (cercare class=\"todo\").")
    gruppi = {}
    for m in MANCA: gruppi.setdefault(m.split(" ")[0], []).append(m)
    for f, v in gruppi.items(): print(f"  {f}: {len(v)} mancanti, per esempio «{v[0]}»")
    sys.exit(1 if ERRORI else 0)

if __name__ == "__main__":
    main()
