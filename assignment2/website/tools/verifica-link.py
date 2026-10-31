#!/usr/bin/env python3
"""Controlla link interni, ancore e link esterni di tutte le pagine (R-009, R-010, R-015).

- ogni href interno punta a un file esistente e, se c'è un'ancora, a un id esistente nella pagina di destinazione
- nessun link interno apre una nuova scheda (target="_blank")
- ogni link esterno (http/https) è dichiarato: classe "ext" con testo nascosto «(sito esterno)»
- nessun link con testo vuoto; nessuno stesso testo che porta a destinazioni diverse nella stessa pagina
- la 404 non è il bersaglio di nessun link interno
Scrive docs/verifiche/link.md. Uso (dalla cartella website/): python3 tools/verifica-link.py
"""
import html.parser
import pathlib
import sys
import urllib.parse

ROOT = pathlib.Path(__file__).resolve().parent.parent
PAGINE = sorted([p for p in ROOT.glob("*.html")] + [p for p in (ROOT / "en").glob("*.html")])
PAGINE = [p for p in PAGINE if "docs" not in p.parts]


class Parser(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids, self.links, self._a, self.risorse = set(), [], None, []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a:
            self.ids.add(a["id"])
        if tag == "a" and "href" in a:
            self._a = {"href": a["href"], "target": a.get("target"), "cls": a.get("class", ""), "testo": "", "label": a.get("aria-label", "")}
        if tag in ("link", "script", "img") and (a.get("href") or a.get("src")):
            self.risorse.append(a.get("href") or a.get("src"))

    def handle_endtag(self, tag):
        if tag == "a" and self._a is not None:
            self.links.append(self._a)
            self._a = None

    def handle_data(self, data):
        if self._a is not None:
            self._a["testo"] += data


def analizza(p):
    pr = Parser()
    pr.feed(p.read_text(encoding="utf-8"))
    return pr


cache = {p: analizza(p) for p in PAGINE}
problemi, n_link, n_ancore, n_ext = [], 0, 0, 0
for p, pr in cache.items():
    rel = p.relative_to(ROOT)
    per_testo = {}
    for ln in pr.links:
        href = ln["href"]
        testo = " ".join((ln["testo"] or ln["label"]).split())
        if not testo:
            problemi.append(f"{rel}: link senza testo verso {href}")
        if href.startswith(("mailto:", "tel:")):
            continue
        if href.startswith(("http://", "https://")):
            n_ext += 1
            if "ext" not in ln["cls"].split():
                problemi.append(f"{rel}: link esterno non dichiarato {href}")
            continue
        n_link += 1
        if ln["target"] == "_blank":
            problemi.append(f"{rel}: link interno in nuova scheda {href}")
        u = urllib.parse.urlsplit(href)
        dest = p if not u.path else (p.parent / u.path).resolve()
        if u.path and not dest.exists():
            problemi.append(f"{rel}: link rotto {href}")
            continue
        if dest.name == "404.html" and p.name != "404.html":
            problemi.append(f"{rel}: link interno verso la 404 ({href})")
        if u.fragment:
            n_ancore += 1
            ids = cache[dest].ids if dest in cache else analizza(dest).ids
            if u.fragment not in ids:
                problemi.append(f"{rel}: ancora inesistente {href}")
        chiave = testo.lower()
        dest_norm = f"{dest.name}?{u.query}#{u.fragment}"
        if chiave and chiave in per_testo and per_testo[chiave] != dest_norm and not ln["label"]:
            problemi.append(f"{rel}: stesso testo «{testo}» per destinazioni diverse ({per_testo[chiave]} / {dest_norm})")
        per_testo.setdefault(chiave, dest_norm)
    for r in pr.risorse:
        if r.startswith(("http", "data:")):
            problemi.append(f"{rel}: risorsa esterna {r}")
            continue
        if not (p.parent / urllib.parse.urlsplit(r).path).resolve().exists():
            problemi.append(f"{rel}: risorsa mancante {r}")

out = ROOT / "docs/verifiche/link.md"
righe = ["# Verifica dei link", "", "Generato da `tools/verifica-link.py`.", "",
         "| Controllo | Valore |", "|---|---|",
         f"| Pagine analizzate (IT + EN) | {len(PAGINE)} |", f"| Link interni controllati | {n_link} |",
         f"| Link con ancora controllati | {n_ancore} |", f"| Link esterni (tutti dichiarati) | {n_ext} |",
         f"| Problemi trovati | {len(problemi)} |", ""]
righe += ["## Problemi", ""] + [f"- {x}" for x in problemi] if problemi else ["Nessun problema: tutti i link interni e le ancore esistono, nessun link interno apre una nuova scheda, nessuna risorsa esterna."]
out.write_text("\n".join(righe) + "\n", encoding="utf-8")
print(f"{len(PAGINE)} pagine, {n_link} link interni, {n_ancore} ancore, {n_ext} esterni, {len(problemi)} problemi")
for x in problemi[:40]:
    print("  ", x)
sys.exit(1 if problemi else 0)
