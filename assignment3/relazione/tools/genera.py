#!/usr/bin/env python3
"""Genera la relazione: Appendice A dai dati, indice con numeri di pagina, PDF.
Uso (da assignment3/relazione):  python3 tools/genera.py
Ripete stampa → pdftotext → numeri di pagina finché l'indice non cambia più."""
import glob, html, json, os, re, subprocess, sys
QUI = os.path.dirname(os.path.abspath(__file__)); REL = os.path.dirname(QUI); A3 = os.path.dirname(REL)
HTML = os.path.join(REL, "relazione.html"); PDF = os.path.join(REL, "relazione.pdf")

def sostituisci(testo, marca, contenuto):
    return re.sub(rf"(<!--{marca}:INIZIO-->).*?(<!--{marca}:FINE-->)", lambda m: m.group(1) + "\n" + contenuto + "\n" + m.group(2), testo, flags=re.S)

def appendice_a():
    base = {}
    for riga in open(os.path.join(A3, "risultati_mauve.md"), encoding="utf-8"):
        m = re.match(r"\| `([^`]+)` \| (\d+)% \| (\d+)% \| (\d+) \| (\d+) \|", riga)
        if m: base[m.group(1)] = tuple(int(x) for x in m.groups()[1:])
    loop = {}
    for f in glob.glob(os.path.join(A3, "results", "*.json")):
        d = json.load(open(f, encoding="utf-8")); t = d["tools"]; slug = os.path.basename(f)[:-5]
        pag = ("en/" + slug[3:] if slug.startswith("en-") else slug) + ".html"
        mv = t["mauve"]; c = re.search(r"completezza[^0-9]*(\d+)%", mv["note"])
        ac = t["accessibilitychecker"]
        acs = str(ac["score"]) if ac["status"] == "ok" else ("err." if ac["status"] == "error" else "—")
        loop[pag] = (mv["score"], int(c.group(1)), mv["errors"], f'{t["achecks"]["errors"]}/{t["achecks"]["warnings"]}', t["achecks_lighthouse"]["score"], acs)
    assert set(base) == set(loop) and len(base) == 50, (len(base), len(loop))
    righe = []
    for p in sorted(base, key=lambda x: (x.startswith("en/"), x)):
        b, l = base[p], loop[p]
        assert b[2] == l[2], (p, b[2], l[2])  # criteri segnalati uguali nei due cicli: una colonna sola
        righe.append(f'<tr><th scope="row"><code>{html.escape(p[:-5])}</code></th><td class="n">{max(b[0], l[0])}%</td>'
                     f'<td class="n">{max(b[1], l[1])}%</td><td class="n">{l[2]}</td>'
                     f'<td class="n">{l[3]}</td><td class="n">{l[4]}</td></tr>')
    return "\n".join(righe)

def voci_indice(testo):
    voci = []
    for liv, idv, corpo in re.findall(r'<h([23]) id="([^"]+)"[^>]*>(.*?)</h\1>', testo, flags=re.S):
        if idv == "indice": continue
        num = re.search(r'<span class="num">(.*?)</span>', corpo)
        tit = re.sub(r"<[^>]+>", "", re.sub(r'<span class="num">.*?</span>', "", corpo)).strip()
        voci.append((int(liv), idv, num.group(1) if num else "", html.unescape(tit)))
    return voci

def norm(s): return re.sub(r"\s+", "", s).replace("’", "'")

def indice(voci, pagine):
    out = []
    for liv, idv, num, tit in voci:
        etichetta = (num + "  " if num else "") + tit
        out.append(f'<li class="l{liv}"><a href="#{idv}">{html.escape(etichetta)}</a><span class="pun" aria-hidden="true"></span><span class="pag">{pagine.get(idv, "–")}</span></li>')
    return "\n".join(out)

def pagine_pdf(voci):
    n = int(re.search(r"Pages:\s+(\d+)", subprocess.run(["pdfinfo", PDF], capture_output=True, text=True).stdout).group(1))
    testi = [norm(subprocess.run(["pdftotext", "-f", str(i), "-l", str(i), "-layout", PDF, "-"], capture_output=True, text=True).stdout) for i in range(1, n + 1)]
    # fine dell'indice: ultima pagina che contiene l'ultima voce prima che compaia il primo titolo vero
    ultima = norm(voci[-1][2] + voci[-1][3])
    inizio = next(i for i, t in enumerate(testi) if ultima in t) + 1
    trovate, da = {}, inizio
    for liv, idv, num, tit in voci:
        chiave = norm(num + tit)
        for i in range(da, n):
            if chiave in testi[i]:
                trovate[idv] = i + 1; da = i; break
        else:
            print("titolo non trovato:", num, tit, file=sys.stderr)
    return trovate, n

def main():
    testo = open(HTML, encoding="utf-8").read()
    testo = sostituisci(testo, "APPENDICE_A", appendice_a())
    voci = voci_indice(testo); pagine = {}
    for giro in range(6):
        testo = sostituisci(testo, "INDICE", indice(voci, pagine))
        open(HTML, "w", encoding="utf-8").write(testo)
        subprocess.run(["node", os.path.join(QUI, "genera_pdf.js"), HTML, PDF], check=True, capture_output=True)
        nuove, n = pagine_pdf(voci)
        print(f"giro {giro + 1}: {n} pagine")
        if nuove == pagine: break
        pagine = nuove
    print(json.dumps(pagine))

if __name__ == "__main__":
    main()
