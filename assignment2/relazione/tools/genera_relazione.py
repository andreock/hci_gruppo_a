#!/usr/bin/env python3
"""Genera relazione.html e relazione.pdf da relazione.md, e i file di controllo.

Uso, dalla cartella assignment2/relazione:  python3 tools/genera_relazione.py

Solo libreria standard. Il PDF richiede Node.js e il Playwright di website/tools;
i numeri di pagina dell'indice richiedono pdftotext (poppler): se manca, l'indice
esce senza numeri e 02_controllo_consegna.md senza pagine.

Oltre al Markdown comune, relazione.md usa:
  :::tipo | titolo | fonte ... :::      riquadri (prompt, diff, confronto, prima, dopo, cambio,
                                        responsabile, avviso, figure2, copertina)
  Tabella: testo                        didascalia della tabella che segue
  ![alt](file){didascalia}              figura numerata
  {{Personas}} {{Journey}} {{Sito}}     etichette di fase
  [[INDICE]]                            indice generato
  [DA COMPLETARE: ...] [DA VERIFICARE: ...]   segnaposto, raccolti in 03_da_completare.md
"""
import base64
import html
import pathlib
import re
import shutil
import subprocess
import sys

BASE = pathlib.Path(__file__).resolve().parent.parent
REPO = BASE.parent.parent

# Immagini: (file in assets/img, commit o None per la copia nel repository, nome dello screenshot).
IMMAGINI = [
    ("home-1280-v1.jpg", "e1ebd20", "home-1280.jpg"),
    ("home-1280-v2.jpg", "f0988ba", "home-1280.jpg"),
    ("home-1280-v3.jpg", "797fc7e", "home-1280.jpg"),
    ("donazione-1280-v1.jpg", "e1ebd20", "donazione-1280.jpg"),
    ("donazione-1280-v3.jpg", "797fc7e", "donazione-1280.jpg"),
    ("donazione-riepilogo-errori.png", "797fc7e", "donazione-riepilogo-errori.png"),
    ("ricerca-api-focus.png", "797fc7e", "tastiera-03-card-focus.png"),
    ("home-375.jpg", "797fc7e", "home-375.jpg"),
    ("progetto-375.jpg", "797fc7e", "progetto-375.jpg"),
    ("menu-mobile-375.png", "797fc7e", "menu-mobile-375.png"),
]
SCREENSHOT = "assignment2/website/docs/verifiche/screenshot/"

# Consegna -> sezioni in cui è trattata (per 02_controllo_consegna.md).
CONSEGNA = [
    ("Introduzione al progetto e link al prototipo", ["1"]),
    ("Personas", ["2"]),
    ("Uno user journey per ogni persona", ["3"]),
    ("Personas e journey · strumenti utilizzati e attività", ["4", "5.1"]),
    ("Personas e journey · principali prompt e informazioni fornite", ["5.2"]),
    ("Personas e journey · esempi della prima versione e della versione finale", ["5.3"]),
    ("Personas e journey · problemi individuati negli output", ["5.4"]),
    ("Personas e journey · richieste di modifica e interventi effettuati", ["5.5"]),
    ("Personas e journey · motivazioni delle scelte finali", ["5.8"]),
    ("Personas · come abbiamo reso i profili più specifici, differenziati e coerenti", ["5.6"]),
    ("Journey · come abbiamo migliorato la corrispondenza con obiettivi e caratteristiche delle personas", ["5.7"]),
    ("Sito · strumenti utilizzati e attività", ["4", "6.1"]),
    ("Sito · principali prompt e informazioni fornite", ["6.2"]),
    ("Sito · esempi della prima versione e della versione finale", ["6.3"]),
    ("Sito · problemi individuati negli output", ["6.4"]),
    ("Sito · richieste di modifica e interventi effettuati", ["6.5"]),
    ("Sito · revisione di contenuti, struttura, navigazione e interazioni", ["6.6"]),
    ("Sito · eventuali modifiche apportate direttamente al codice", ["6.7"]),
    ("Sito · motivazioni delle scelte finali", ["6.8"]),
    ("Selezione dei passaggi invece dell'intera cronologia; contributo del gruppo", ["1", "8"]),
    ("Richiesta del gruppo · uso responsabile dell'IA", ["7"]),
]

SEGNAPOSTO = re.compile(r"\[DA (?:COMPLETARE|VERIFICARE):(?! …)[^\]]*\]")  # «…» = citazione del prompt


def inline(testo):
    """Formattazione in linea: il codice viene isolato per primo."""
    parti = re.split(r"(`[^`]+`)", testo)
    out = []
    for p in parti:
        if p.startswith("`") and p.endswith("`") and len(p) > 1:
            cl = ' class="nb"' if len(p) <= 12 else ""  # hash e nomi brevi non vanno a capo
            out.append(f"<code{cl}>" + html.escape(p[1:-1], quote=False) + "</code>")
            continue
        s = html.escape(p, quote=False)
        s = re.sub(r"\[([^\]]+)\]\((https?://[^)\s]+)\)", r'<a href="\2">\1</a>', s)
        s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
        s = re.sub(r"(?<![\*\w])\*(?!\s)([^*]+?)\*(?![\*\w])", r"<em>\1</em>", s)
        s = re.sub(r"\{\{(\w+)\}\}", lambda m: f'<span class="tag tag--{m.group(1).lower()}">{m.group(1)}</span>', s)
        s = re.sub(r"\[DA (?:COMPLETARE|VERIFICARE):(?! …)[^\]]*\]", lambda m: f'<mark class="todo">{m.group(0)}</mark>', s)
        out.append(s)
    return "".join(out)


def slug(testo):
    t = re.sub(r"[^a-z0-9]+", "-", testo.lower().replace("à", "a").replace("è", "e").replace("ì", "i").replace("ò", "o").replace("ù", "u"))
    return t.strip("-")


class Stato:
    def __init__(self, pagine=None):
        self.h2 = 0
        self.h3 = 0
        self.titoli = []          # (livello, numero, testo, id)
        self.fig = 0
        self.tab = 0
        self.segnaposto = []      # (sezione, testo)
        self.sezione = "Copertina"
        self.pagine = pagine or {}


def tabella(righe, didascalia, st):
    celle = lambda r: [c.strip() for c in re.split(r"(?<!\\)\|", r.strip().strip("|"))]
    riga_th = righe[0].startswith("| Dimensione")
    testa = celle(righe[0])
    corpo = [celle(r) for r in righe[2:]]
    caption = ""
    if didascalia:
        st.tab += 1
        caption = f"<caption><b>Tabella {st.tab}.</b> {inline(didascalia)}</caption>"
    cl = "tabella corta" if len(corpo) <= 7 else "tabella"
    h = "".join(f'<th scope="col">{inline(c)}</th>' for c in testa)
    cella = lambda c: "<br>".join(inline(x.strip()) for x in c.split("¶"))
    b = "".join("<tr>" + "".join((f'<th scope="row">{cella(c)}</th>' if riga_th and k == 0 else (f'<td colspan="{len(testa) - k}">{cella(c)}</td>' if k == len(r) - 1 and len(r) < len(testa) else f"<td>{cella(c)}</td>")) for k, c in enumerate(r)) + "</tr>" for r in corpo)
    nome = f"Tabella {st.tab}" if didascalia else "Tabella"
    return f'<div class="{cl}" role="region" aria-label="{nome}" tabindex="0"><table>{caption}<thead><tr>{h}</tr></thead><tbody>{b}</tbody></table></div>'


def figura(alt, src, didascalia, st, classe=""):
    st.fig += 1
    c = f' class="{classe}"' if classe else ""
    return (f'<figure{c}><img src="assets/img/{html.escape(src)}" alt="{html.escape(alt)}" loading="eager">'
            f"<figcaption><b>Figura {st.fig}.</b> {inline(didascalia)}</figcaption></figure>")


def diff_html(testo):
    righe = []
    for r in testo.split("\n"):
        e = html.escape(r, quote=False)
        if r.startswith("+"):
            righe.append(f'<span class="piu">{e}</span>')
        elif r.startswith("-"):
            righe.append(f'<span class="meno">{e}</span>')
        else:
            righe.append(e + "\n")
    return '<pre class="diff">' + "".join(righe) + "</pre>"


def trova_chiusura(righe, i):
    """Restituisce l'indice della riga ':::' che chiude il blocco aperto alla riga i."""
    prof = 1
    j = i + 1
    while j < len(righe):
        s = righe[j].strip()
        if s == ":::":
            prof -= 1
            if prof == 0:
                return j
        elif s.startswith(":::"):
            prof += 1
        j += 1
    raise SystemExit(f"Blocco non chiuso: {righe[i]}")


def blocco(tipo, arg, contenuto, st):
    t = arg[0] if arg else ""
    m = arg[1] if len(arg) > 1 else ""
    if tipo in ("prompt", "diff"):
        testo = "\n".join(contenuto).strip("\n")
        for s in SEGNAPOSTO.findall(testo):
            st.segnaposto.append((st.sezione, s))
        tit = f'<span class="prompt__tit">{inline(t)}' + (f" <span>· {inline(m)}</span>" if m else "") + "</span>"
        corpo = diff_html(testo) if tipo == "diff" else "<pre>" + re.sub(
            r"\[DA (?:COMPLETARE|VERIFICARE):(?! …)[^\]]*\]", lambda x: f'<mark class="todo">{x.group(0)}</mark>',
            html.escape(testo, quote=False)) + "</pre>"
        return f'<div class="prompt">{tit}{corpo}</div>'
    interno = render(contenuto, st)
    if tipo == "confronto":
        return f'<div class="confronto">{interno}</div>'
    if tipo in ("prima", "dopo"):
        nome = t or ("Prima versione" if tipo == "prima" else "Versione finale")
        return (f'<div class="colonna colonna--{tipo}"><span class="colonna__tit">{inline(nome)}</span>'
                f'<span class="colonna__fonte">{inline(m)}</span>{interno}</div>')
    if tipo == "cambio":
        return f'<div class="box box--cambio"><span class="box__tit">Cosa è cambiato e perché</span>{interno}</div>'
    if tipo == "responsabile":
        return f'<div class="box box--responsabile"><span class="box__tit">{inline(t or "Uso responsabile")}</span>{interno}</div>'
    if tipo == "avviso":
        return f'<div class="box box--avviso"><span class="box__tit">{inline(t or "Attenzione")}</span>{interno}</div>'
    if tipo == "figure2":
        extra = " figure2--stretta" if t == "stretta" else ""
        return f'<div class="figure2{extra}">{interno}</div>'
    if tipo == "persona":
        testa, sep, campi = interno.partition('<div class="campo">')
        return f'<section class="scheda-persona">{testa}<div class="campi">{sep}{campi}</div></section>'
    if tipo == "journey":
        return f'<section class="scheda-journey">{interno}</section>'
    if tipo == "meta":
        return f'<div class="scheda-meta">{interno}</div>'
    if tipo == "campo":
        return f'<div class="campo"><h4>{inline(t)}</h4>{interno}</div>'
    if tipo == "html":
        return "\n".join(contenuto)
    raise SystemExit(f"Blocco sconosciuto: {tipo}")


def render(righe, st):
    out = []
    i = 0
    didascalia = None
    while i < len(righe):
        r = righe[i]
        s = r.strip()
        if not s:
            i += 1
            continue
        if s.startswith(":::") and s != ":::":
            j = trova_chiusura(righe, i)
            parti = [p.strip() for p in s[3:].split("|")]
            if parti[0] == "html":
                out.append("\n".join(righe[i + 1:j]).replace("{FIG}", str(st.fig + 1)))
                st.fig += 1
            else:
                out.append(blocco(parti[0], parti[1:], righe[i + 1:j], st))
            i = j + 1
            continue
        if s == "[[INDICE]]":
            out.append("@@INDICE@@")
            i += 1
            continue
        for x in SEGNAPOSTO.findall(s):
            st.segnaposto.append((st.sezione, x))
        m = re.match(r"(#{2,4})\s+(.*)", s)
        if m:
            liv = len(m.group(1))
            testo = m.group(2)
            num = ""
            if liv == 2 and not testo.startswith("Appendice") and testo != "Indice":
                st.h2 += 1
                st.h3 = 0
                num = str(st.h2)
            elif liv == 3 and st.h2 and not st.sezione.startswith("Appendice"):
                st.h3 += 1
                num = f"{st.h2}.{st.h3}"
            ident = slug((num + "-" if num else "") + testo)
            if liv <= 3 and testo != "Indice":
                st.titoli.append((liv, num, testo, ident))
            if liv <= 3:
                st.sezione = (num + " " if num else "") + testo
            n = f'<span class="num">{num}</span>' if num else ""
            out.append(f'<h{liv} id="{ident}">{n}{inline(testo)}</h{liv}>')
            i += 1
            continue
        m = re.match(r"!\[(.*?)\]\((.*?)\)\{(.*)\}$", s)
        if m:
            out.append(figura(m.group(1), m.group(2), m.group(3), st))
            i += 1
            continue
        if s.startswith("Tabella: "):
            didascalia = s[len("Tabella: "):]
            i += 1
            continue
        if s.startswith("|"):
            j = i
            while j < len(righe) and righe[j].strip().startswith("|"):
                for x in SEGNAPOSTO.findall(righe[j]):
                    if j != i:
                        st.segnaposto.append((st.sezione, x))
                j += 1
            out.append(tabella([x.strip() for x in righe[i:j]], didascalia, st))
            didascalia = None
            i = j
            continue
        if s.startswith("- "):
            j = i
            voci = []
            while j < len(righe) and righe[j].strip().startswith("- "):
                voci.append(righe[j].strip()[2:])
                if j != i:
                    st.segnaposto.extend((st.sezione, x) for x in SEGNAPOSTO.findall(righe[j]))
                j += 1
            out.append("<ul>" + "".join(f"<li>{inline(v)}</li>" for v in voci) + "</ul>")
            i = j
            continue
        if re.match(r"\d+\.\s", s):
            j = i
            voci = []
            while j < len(righe) and re.match(r"\d+\.\s", righe[j].strip()):
                voci.append(re.sub(r"^\d+\.\s", "", righe[j].strip()))
                if j != i:
                    st.segnaposto.extend((st.sezione, x) for x in SEGNAPOSTO.findall(righe[j]))
                j += 1
            out.append("<ol>" + "".join(f"<li>{inline(v)}</li>" for v in voci) + "</ol>")
            i = j
            continue
        # paragrafo: fino alla riga vuota o a un blocco
        j = i
        par = []
        while j < len(righe):
            q = righe[j].strip()
            if not q or q.startswith((":::", "#", "|", "- ", "![", "Tabella: ")) or q == "[[INDICE]]":
                break
            par.append(q)
            if j != i:
                st.segnaposto.extend((st.sezione, x) for x in SEGNAPOSTO.findall(q))
            j += 1
        if j == i:
            raise SystemExit(f"Riga non interpretabile: {righe[i]}")
        out.append(f"<p>{inline(' '.join(par))}</p>")
        i = j
    return "\n".join(out)


def indice(st):
    voci = []
    for liv, num, testo, ident in st.titoli:
        pag = st.pagine.get(ident, "")
        etichetta = (num + "  " if num else "") + testo
        voci.append(f'<li class="l{liv}"><a href="#{ident}">{inline(etichetta)}</a>'
                    f'<span class="pun" aria-hidden="true"></span><span class="pag">{pag}</span></li>')
    return '<nav class="indice" aria-label="Indice"><h2 id="indice">Indice</h2><ol>' + "".join(voci) + "</ol></nav>"


def costruisci(sorgente, pagine=None):
    righe = sorgente.split("\n")
    st = Stato(pagine)
    # front matter della copertina
    assert righe[0] == "---"
    fine = righe.index("---", 1)
    meta = dict(r.split(": ", 1) for r in righe[1:fine])
    corpo = render(righe[fine + 1:], st).replace("@@INDICE@@", indice(st))
    dati = "".join(f"<dt>{inline(k)}</dt><dd>{inline(meta[k])}</dd>" for k in ("Gruppo", "Componenti", "Corso", "Data", "Sito pubblicato"))
    for k in ("Gruppo", "Componenti", "Corso", "Data", "Sito pubblicato"):
        st_x = SEGNAPOSTO.findall(meta[k])
        st.segnaposto[:0] = [("Copertina", x) for x in st_x]
    copertina = (
        '<header class="copertina"><div class="copertina__fascia">'
        f'<p>Human-Computer Interaction · Assignment 2</p><h1>{inline(meta["Titolo"])}</h1>'
        f'<p class="copertina__sottotitolo">{inline(meta["Sottotitolo"])}</p></div>'
        f'<div class="copertina__striscia"></div><dl class="copertina__dati">{dati}</dl></header>'
    )
    pagina = (
        '<!doctype html>\n<html lang="it"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width, initial-scale=1">'
        f'<title>{html.escape(meta["Titolo"])} · Gruppo A</title>'
        f'<meta name="description" content="{html.escape(meta["Sottotitolo"])}">'
        '<link rel="stylesheet" href="assets/stile.css"></head>'
        f"<body>{copertina}<main>{corpo}</main></body></html>\n"
    )
    return pagina, st


def estrai_immagini():
    dest = BASE / "assets" / "img"
    dest.mkdir(parents=True, exist_ok=True)
    for nome, commit, orig in IMMAGINI:
        f = dest / nome
        if f.exists():
            continue
        dati = subprocess.run(["git", "show", f"{commit}:{SCREENSHOT}{orig}"], cwd=REPO, capture_output=True)
        if dati.returncode:
            raise SystemExit(f"Impossibile estrarre {orig} da {commit}: {dati.stderr.decode()}")
        f.write_bytes(dati.stdout)


def stampa_pdf():
    node = shutil.which("node")
    if not node:
        print("Node.js non trovato: PDF non generato.")
        return False
    r = subprocess.run([node, str(BASE / "tools" / "genera_pdf.js"), str(BASE / "relazione.html"), str(BASE / "relazione.pdf")])
    return r.returncode == 0


def pagine_titoli(st):
    if not shutil.which("pdftotext"):
        print("pdftotext non trovato: indice senza numeri di pagina.")
        return {}, 0
    testo = subprocess.run(["pdftotext", "-layout", str(BASE / "relazione.pdf"), "-"], capture_output=True, text=True).stdout
    fogli = testo.split("\f")
    norm = lambda s: re.sub(r"\s+", " ", s).strip().lower()
    fogli_n = [norm(f) for f in fogli]
    primo = next((k for k, f in enumerate(fogli_n) if "introduzione" in f and "indice" not in f[:40]), 2)
    # salta copertina e indice: cerca dalla prima pagina dopo l'indice
    pagine = {}
    k = primo
    for liv, num, testo_t, ident in st.titoli:
        chiave = norm((num + " " if num else "") + re.sub(r"[`*]", "", testo_t))[:34]
        for q in range(k, len(fogli_n)):
            if chiave in fogli_n[q]:
                pagine[ident] = q + 1
                k = q
                break
    return pagine, len([f for f in fogli if f.strip()])


def scrivi_controllo(st, pagine, totale):
    per_num = {num: (testo, pagine.get(ident, "")) for _, num, testo, ident in st.titoli if num}
    r = ["# 02 · Controllo della consegna", "",
         "Per ogni punto della consegna: sezione e pagina di `relazione.pdf`.", "", "Numero del gruppo e componenti sono in copertina (pagina 1).", "",
         f"Pagine del PDF: {totale}.", "",
         "| Punto della consegna | Sezione | Pagina del PDF |", "|---|---|---|"]
    for punto, sez in CONSEGNA:
        s = "; ".join(f"§{n} {per_num[n][0]}" for n in sez)
        p = ", ".join(str(per_num[n][1]) for n in sez)
        r.append(f"| {punto} | {s} | {p} |")
    r.append("")
    (BASE / "02_controllo_consegna.md").write_text("\n".join(r), encoding="utf-8")


def scrivi_da_completare(st):
    r = ["# 03 · Segnaposto da completare", "",
         "Dopo averli sostituiti in `relazione.md`, rieseguite `python3 tools/genera_relazione.py`.", ""]
    if not st.segnaposto:
        r.append("Nessun segnaposto rimasto.")
    else:
        r += [f"Totale: {len(st.segnaposto)}.", "", "| # | Sezione | Segnaposto |", "|---|---|---|"]
        for k, (sez, testo) in enumerate(st.segnaposto, 1):
            r.append(f"| {k} | {sez} | {testo} |")
    r.append("")
    (BASE / "03_da_completare.md").write_text("\n".join(r), encoding="utf-8")


def main():
    estrai_immagini()
    # I font sono incorporati: da file:// Chrome blocca i file di font esterni (website/docs/decisioni.md, D-39).
    css = (BASE / "tools" / "stile.css").read_text(encoding="utf-8")
    css = re.sub(r'url\("FONT:([^"]+)"\)', lambda m: 'url("data:font/woff2;base64,' + base64.b64encode((BASE / "assets" / "fonts" / m.group(1)).read_bytes()).decode() + '")', css)
    (BASE / "assets" / "stile.css").write_text(css, encoding="utf-8")
    sorgente = (BASE / "relazione.md").read_text(encoding="utf-8")
    sorgente = re.sub(r"^\[\[INCLUDI (.+?)\]\]$", lambda m: (BASE / m.group(1)).read_text(encoding="utf-8"), sorgente, flags=re.M)
    pagina, st = costruisci(sorgente)
    (BASE / "relazione.html").write_text(pagina, encoding="utf-8")
    pagine, totale = {}, 0
    if stampa_pdf():
        pagine, totale = pagine_titoli(st)
        if pagine:
            pagina, st = costruisci(sorgente, pagine)
            (BASE / "relazione.html").write_text(pagina, encoding="utf-8")
            stampa_pdf()
            pagine, totale = pagine_titoli(st)
            mancanti = [t[3] for t in st.titoli if t[3] not in pagine]
            if mancanti:
                print("Titoli non trovati nel PDF:", mancanti)
    scrivi_controllo(st, pagine, totale)
    scrivi_da_completare(st)
    print(f"Fatto: {totale} pagine, {st.fig} figure, {st.tab} tabelle, {len(st.segnaposto)} segnaposto.")


if __name__ == "__main__":
    sys.exit(main())
