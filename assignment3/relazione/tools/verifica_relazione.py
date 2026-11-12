#!/usr/bin/env python3
"""Controlli della relazione: numeri ricalcolati dalle fonti, estratti di codice nel diff,
commit nella tabella riassuntiva, formule da evitare fuori dalla §9, contrasti, segnaposto."""
import glob, html, json, os, re, statistics as st, subprocess, sys
REL = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); A3 = os.path.dirname(REL); ROOT = os.path.dirname(A3)
H = open(os.path.join(REL, "relazione.html"), encoding="utf-8").read()
T = html.unescape(re.sub(r"<[^>]+>", " ", H)); T = re.sub(r"\s+", " ", T)
ok = True
def check(nome, cond, extra=""):
    global ok; ok &= bool(cond); print(("OK  " if cond else "NO  ") + nome + (f" · {extra}" if extra else ""))
it = lambda x, d=1: f"{x:.{d}f}".replace(".", ",")

# --- MAUVE++ baseline e loop
base = {}
for r in open(os.path.join(A3, "risultati_mauve.md"), encoding="utf-8"):
    m = re.match(r"\| `([^`]+)` \| (\d+)% \| (\d+)% \| (\d+) \| (\d+) \|", r)
    if m: base[m.group(1)] = [int(x) for x in m.groups()[1:]]
res = [json.load(open(f, encoding="utf-8")) for f in glob.glob(os.path.join(A3, "results", "*.json"))]
mv = [r["tools"]["mauve"] for r in res]
comp = [int(re.search(r"completezza[^0-9]*(\d+)%", m["note"]).group(1)) for m in mv]
num = {
  "media acc. baseline": it(st.mean(v[0] for v in base.values())) + "%",
  "media compl. baseline": it(st.mean(v[1] for v in base.values())) + "%",
  "media compl. loop": it(st.mean(comp)) + "%",
  "media acc. loop": it(st.mean(m["score"] for m in mv)) + "%",
  "criteri baseline": str(sum(v[2] for v in base.values())),
  "criteri per pagina": it(sum(v[2] for v in base.values()) / 50, 2),
  "manuali/pagina base": it(sum(v[3] for v in base.values()) / 50, 2),
  "manuali/pagina loop": it(sum(m["warnings"] for m in mv) / 50, 2),
  "occ. errore MAUVE++": str(sum(i["occorrenze"] for m in mv for i in m["issues"] if i["tipo"] == "error")),
  "AChecker known": str(sum(r["tools"]["achecks"]["errors"] for r in res)),
  "AChecker potential": f'{sum(r["tools"]["achecks"]["warnings"] for r in res):,}'.replace(",", "."),
}
num["occorrenze totali"] = f'{int(num["occ. errore MAUVE++"]) + int(num["AChecker known"]):,}'.replace(",", ".")
for k, v in num.items():
    if v in T: check(f"{k} = {v}", True)
    else: print(f"--  {k} = {v} (non citato nel testo)")
check("medie del resoconto 92,7% e 88,1%", num["media acc. baseline"] == "92,7%" and num["media compl. baseline"] == "88,1%")
check("pagine 50 (baseline e loop)", len(base) == 50 and len(res) == 50)
# per tecnica (Tabella 4)
occ = {}
for m in mv:
    for i in m["issues"]:
        if i["tipo"] == "error": occ[i["tecnica"]] = occ.get(i["tecnica"], 0) + i["occorrenze"]
for tec, n in [("ARIA6", 370), ("G18", 150), ("F73", 148), ("G140", 50), ("H98", 48), ("C38", 40)]:
    check(f"occorrenze {tec} = {n}", occ.get(tec) == n)
check("G195+F78 = 100", occ.get("G195", 0) + occ.get("F78", 0) == 100)
ac = {}
for r in res:
    for i in r["tools"]["achecks"]["issues"]:
        if i["tipo"] == "error": ac[i["check_id"]] = ac.get(i["check_id"], 0) + i["occorrenze"]
check("AChecker #116 = 100, #245 = 22", ac == {"116": 100, "245": 22}, str(ac))
acs = [r["tools"]["accessibilitychecker"]["status"] for r in res]
check("AccessibilityChecker 3 ok / 1 error / 46 skipped", (acs.count("ok"), acs.count("error"), acs.count("skipped")) == (3, 1, 46))
check("issues.csv 2.119 righe", sum(1 for _ in open(os.path.join(A3, "issues.csv"))) - 1 == 2119)

# --- controlli locali (dati/)
D = os.path.join(REL, "dati")
rd = lambda w, f: open(os.path.join(D, w, f), encoding="utf-8").read()
check("html-validate PRIMA 12 errori", "12 problems (12 errors" in rd("prima", "html-validate.txt"))
check("html-validate DOPO 0", "exit=0" in rd("dopo", "html-validate.txt"))
check("percorsi 104/105 e 105/105", "104/105" in rd("prima", "percorsi.txt") and "105/105" in rd("dopo", "percorsi.txt"))
check("contrasti 2 sotto soglia → 0", "91 coppie × 2 temi, 2 sotto soglia" in rd("prima", "contrasto.txt") and "91 coppie × 2 temi, 0 sotto soglia" in rd("dopo", "contrasto.txt"))
check("contrasto nativo PRIMA 180/180", "90 coppie × 2 temi, 0 sotto soglia" in rd("prima", "contrasto.nativo-base.txt"))
for w in ("prima", "dopo"):
    check(f"{w}: 329/329, 1702 link, 422 ancore, file:// 8/8", "329/329" in rd(w, "verifica-dati.txt") and "1702 link interni, 422 ancore" in rd(w, "verifica-link.txt") and rd(w, "verifica-file.txt").count("OK  ") == 8)
check("bersagli 6 → 0", rd("prima", "responsive.txt").count("×21") == 6 and "×21" not in rd("dopo", "responsive.txt"))
check("axe DOPO 0", '"serious":0' in rd("dopo", "verifica-pagine.txt") and '"serious":0' in rd("dopo", "verifica-pagine.run2.txt"))
check("axe PRIMA 1 transitoria, poi 0 e 0", '"serious":1' in rd("prima", "verifica-pagine.txt") and '"serious":0' in rd("prima", "verifica-pagine.run2.txt") and '"serious":0' in rd("prima", "verifica-pagine.run3.txt"))
for f, regola, a, b in [("html-validate.recommended.json", "tel-non-breaking", 128, 128), ("", "no-inline-style", 80, 80), ("", "void-style", 72, 68), ("", "doctype-style", 50, 50), ("", "no-trailing-whitespace", 34, 34), ("", "no-redundant-for", 22, 22)]:
    cnt = []
    for w in ("prima", "dopo"):
        j = json.load(open(os.path.join(D, w, "html-validate.recommended.json")))
        cnt.append(sum(1 for x in j for m in x["messages"] if m["ruleId"] == regola))
    check(f"{regola} {a} → {b}", cnt == [a, b], str(cnt))

# --- estratti di codice presenti nel diff
diff = subprocess.run(["git", "-C", ROOT, "diff", "adc8f85", "HEAD", "--", "assignment2/website/tools/build.py", "assignment2/website/css", "assignment2/website/js"], capture_output=True, text=True).stdout
diff += subprocess.run(["git", "-C", ROOT, "log", "-p", "adc8f85..HEAD", "--", "assignment2/website/tools/build.py", "assignment2/website/css"], capture_output=True, text=True).stdout
# confronto anche con le pagine HTML delle due versioni (cartelle indicate da PAGINE_A2 e PAGINE_A3)
a2, a3 = os.environ.get("PAGINE_A2"), os.environ.get("PAGINE_A3")
if a2 and a3:
    diff += subprocess.run(["diff", "-r", a2, a3], capture_output=True, text=True).stdout.replace("\n< ", "\n-").replace("\n> ", "\n+")
righe = set(l.rstrip() for l in diff.splitlines())
for pre in re.findall(r'<span class="(?:meno|piu)">(.*?)</span>', H):
    riga = html.unescape(re.sub(r"<[^>]+>", "", pre))
    if "…" in riga:
        parti = [p for p in riga.split("…") if p.strip()]
        trovata = any(all(p.lstrip("+-").strip() in l for p in parti) and l[:1] == riga[:1] for l in righe)
    else:
        trovata = riga.rstrip() in righe
    check("estratto nel diff: " + riga[:70], trovata)

# --- nessun riferimento ai commit nel testo (si parla solo di Assignment 2 e Assignment 3)
commit = subprocess.run(["git", "-C", ROOT, "log", "--format=%h", "adc8f85^..HEAD"], capture_output=True, text=True).stdout.split()
check("nessun hash di commit nel testo", not any(h in T for h in commit))
check("nessuna parola «commit» nel testo", "commit" not in T.lower())

# --- formule da evitare fuori dalla §9
fuori = H[:H.index('id="s9"')] + H[H.index('id="s10"'):]
fuori_t = html.unescape(re.sub(r"<[^>]+>", " ", fuori))
fuori_t = fuori_t[:fuori_t.find("Appendice C · Estratti")] if "Appendice C · Estratti" in fuori_t else fuori_t
for f in ["agente", "Claude ha", "Codex ha", "è stato generato", "è stata generata", "generato automaticamente", "l'IA ha"]:
    check(f"nessun «{f}» fuori dalla §9", f.lower() not in fuori_t.lower())

# --- contrasti dei colori di testo usati
def lum(h):
    h = h.lstrip("#"); c = [int(h[i:i+2], 16) / 255 for i in (0, 2, 4)]
    c = [x / 12.92 if x <= .03928 else ((x + .055) / 1.055) ** 2.4 for x in c]
    return .2126 * c[0] + .7152 * c[1] + .0722 * c[2]
def cr(a, b): la, lb = sorted([lum(a), lum(b)], reverse=True); return (la + .05) / (lb + .05)
coppie = [("badge Risolto", "#17472e", "#e3f2e6"), ("badge Parziale", "#5c3e00", "#fdf1d0"), ("badge Non risolto", "#7d1c12", "#fbe9e5"),
          ("badge Ciclo 1", "#154657", "#e2eff4"), ("badge Ciclo 2", "#8a350c", "#fbeadd"), ("hash", "#3b1d2a", "#f8f2ea"),
          ("badge WCAG", "#ffffff", "#3b1d2a"), ("intestazione tabella", "#ffffff", "#3b1d2a"), ("testo", "#2c1f24", "#ffffff"),
          ("testo su riga alterna", "#2c1f24", "#f8f2ea"), ("didascalie", "#5f4e45", "#ffffff"), ("didascalie su riga", "#5f4e45", "#f8f2ea"),
          ("numero di sezione", "#bf4a12", "#ffffff"), ("copertina occhiello", "#f4b93e", "#3b1d2a"), ("copertina titolo", "#fbf6ee", "#3b1d2a"),
          ("copertina etichette", "#a63f0f", "#fbf6ee"), ("copertina valori", "#3b1d2a", "#fbf6ee"), ("gruppo tabella", "#a33f0f", "#fbf6ee"),
          ("DA COMPLETARE", "#5c3e00", "#fdf1d0"), ("diff meno", "#7d1c12", "#fbeadd"), ("diff più", "#17472e", "#e3f2e6"),
          ("migliora", "#17472e", "#ffffff"), ("peggiora", "#7d1c12", "#f8f2ea"), ("link", "#a33f0f", "#ffffff"), ("piè di pagina", "#5f4e45", "#ffffff"),
          ("grafico etichette", "#5f4e45", "#ffffff")]
for n, a, b in coppie: check(f"contrasto {n} {cr(a, b):.2f}:1 ≥ 4,5", cr(a, b) >= 4.5)

# --- segnaposto
todo = re.findall(r"\[DA COMPLETARE[^\]]*\]", T)
print(f"\n[DA COMPLETARE] rimasti: {len(todo)}")
for t in todo: print("  -", t)
print("\nESITO:", "tutti i controlli superati" if ok else "CI SONO CONTROLLI NON SUPERATI")
sys.exit(0 if ok else 1)
