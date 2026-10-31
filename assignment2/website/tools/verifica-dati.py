#!/usr/bin/env python3
"""Coerenza tra data/progetti.json e le pagine generate (R-022, R-026, R-031, R-032, R-055, R-073, R-084, R-132).

Uso (dalla cartella website/):  python3 tools/verifica-dati.py
Scrive docs/verifiche/dati.md e docs/verifiche/segnaposto.md. Esce con 1 se trova errori.
"""
import html
import json
import os
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import build as B  # noqa: E402  (solo funzioni di calcolo; non rigenera le pagine)

errori, controlli = [], []


def check(nome, cond, dettaglio=""):
    controlli.append((nome, bool(cond)))
    if not cond:
        errori.append(f"{nome}: {dettaglio}")


def testo(path):
    s = (ROOT / path).read_text(encoding="utf-8")
    s = re.sub(r"<script.*?</script>", " ", s, flags=re.S)
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s))).replace("\u00a0", " ")


pagine = sorted([p.relative_to(ROOT).as_posix() for p in ROOT.glob("*.html")] + [p.relative_to(ROOT).as_posix() for p in (ROOT / "en").glob("*.html")])

# 1. dati dei progetti
for p in B.PROGETTI:
    c = p["_"]
    s = p["slug"]
    check(f"{s}: le voci di budget sommano all'obiettivo", sum(f["importo"] for f in p["fondi"]) == p["obiettivo"])
    check(f"{s}: sostenitori = somma delle scelte + donazioni libere", c["sostenitori"] == sum(r["scelte"] for r in p["ricompense"]) + p["libere"])
    check(f"{s}: raccolto ≥ somma degli importi minimi", p["raccolto"] >= sum(r["importo"] * r["scelte"] for r in p["ricompense"]) + B.SITO["regole"]["minimo_libero"] * p["libere"])
    check(f"{s}: posti mai superati", all(r["posti"] is None or r["scelte"] <= r["posti"] for r in p["ricompense"]))
    check(f"{s}: «obiettivo raggiunto» solo con raccolto ≥ obiettivo", (c["stato"] in ("reached", "done")) == (p["raccolto"] >= p["obiettivo"]))
    check(f"{s}: esito presente se e solo se la campagna è conclusa", ("esito" in p) == (not c["aperto"]))
    check(f"{s}: ricompense distinte e ordinabili", len({r["importo"] for r in p["ricompense"]}) == len(p["ricompense"]))
    if p.get("secondo_obiettivo"):
        check(f"{s}: secondo obiettivo maggiore dell'obiettivo", p["secondo_obiettivo"]["importo"] > p["obiettivo"])
    for lang in B.LINGUE:
        f = "" if lang == "it" else "en/"
        tx = testo(f"{f}progetto-{s}.html")
        e = lambda x: B.euro(x, lang).replace(" ", " ")
        check(f"{s} [{lang}]: pagina con raccolto, obiettivo e percentuale dei dati", e(p["raccolto"]) in tx and e(p["obiettivo"]) in tx and B.perc(c["perc"]) in tx)
        check(f"{s} [{lang}]: pagina con il numero di sostenitori", f"{c['sostenitori']}" in tx)
        html_ = (ROOT / f"{f}progetto-{s}.html").read_text(encoding="utf-8")
        ordine = re.findall(r'<section id="(presentazione|fondi|team|ricompense|aggiornamenti|commenti|sostenitori)"', html_)
        check(f"{s} [{lang}]: sezioni nell'ordine fisso", ordine == ["presentazione", "fondi", "team", "ricompense", "aggiornamenti", "commenti", "sostenitori"], str(ordine))
        if not c["aperto"]:
            check(f"{s} [{lang}]: campagna conclusa senza link alla donazione", "donazione.html" not in html_)

# 2. contatori complessivi
for lang in B.LINGUE:
    f = "" if lang == "it" else "en/"
    tx = testo(f"{f}index.html")
    aperti = sum(1 for p in B.PROGETTI if p["_"]["aperto"])
    check(f"home [{lang}]: numero di campagne in corso e concluse", f"{aperti} " in tx and f"{len(B.PROGETTI) - aperti} " in tx)
    cof = sum(p["_"]["cofin"] for p in B.PROGETTI if not p["_"]["aperto"])
    check(f"home [{lang}]: cofinanziamento dell'Ateneo calcolato dai dati", B.euro(cof, lang).replace(" ", " ") in tx)
    tp = testo(f"{f}programma.html")
    for anno in sorted({p["anno"] for p in B.PROGETTI if p["programma"]}):
        ps = [p for p in B.PROGETTI if p["programma"] and p["anno"] == anno]
        r = B.euro(sum(p["raccolto"] for p in ps), lang).replace(" ", " ")
        check(f"programma [{lang}] {anno}: totale raccolto della tabella", r in tp)
    tl = testo(f"{f}progetti.html")
    check(f"progetti [{lang}]: tutte le card presenti", len(re.findall(r'data-slug="', (ROOT / f"{f}progetti.html").read_text(encoding="utf-8"))) == len(B.PROGETTI))

# 3. testi in tutte le pagine
ESCLUSI = {"it": [r"\boverfunding\b", r"\bkeep it all\b", r"\bFAI TU\b", r"\bcampaign manager\b", r"\bprogettist", r"\bfee\b", r"\bbacker", r"\bcheckout\b"],
           "en": [r"\boverfunding\b", r"\bkeep it all\b", r"\bcampaign manager\b", r"\bbacker", r"\bFAI TU\b"]}
for pg in pagine:
    lang = "en" if pg.startswith("en/") else "it"
    tx = testo(pg)
    check(f"{pg}: nessun numero di giorni negativo", not re.search(r"-\s?\d+\s(giorn|day)", tx))
    check(f"{pg}: nota «prototipo» nel piè di pagina", ("Prototipo didattico" if lang == "it" else "Teaching prototype") in tx)
    trovati = [r for r in ESCLUSI[lang] if re.search(r, tx, flags=re.I)]
    check(f"{pg}: nessun termine escluso dal lessico", not trovati, ", ".join(trovati))

# 4. metodi di pagamento uguali tra FAQ e donazione
for lang in B.LINGUE:
    f = "" if lang == "it" else "en/"
    faq, don = testo(f"{f}faq.html"), testo(f"{f}donazione.html")
    for m in B.SITO["metodi_pagamento"]:
        check(f"[{lang}] metodo «{m['nome'][lang]}» uguale in FAQ e donazione", m["nome"][lang] in faq and m["nome"][lang] in don)

# 5. stati in date diverse: mai giorni negativi, solo le quattro formule
for d in ("2026-10-31", "2026-12-24", "2027-03-15", "2030-01-01"):
    out = subprocess.run([sys.executable, "-c", "import sys; sys.path.insert(0,'tools'); import build as B; "
                          "print('\\n'.join(B.stato_html(p, l) for p in B.PROGETTI for l in B.LINGUE))"],
                         cwd=ROOT, env={**os.environ, "IB_OGGI": d}, capture_output=True, text=True)
    check(f"stati calcolati al {d}: nessun giorno negativo", out.returncode == 0 and not re.search(r"-\d+ (giorn|day)", out.stdout), out.stderr[-200:])

# 6. segnaposto da verificare
seg = {}
for pg in pagine:
    if pg.startswith("en/"):
        continue
    tx = testo(pg)
    for m in re.finditer(r"\[DA VERIFICARE con l'Ateneo\]", tx):
        frase = " ".join(tx[max(0, m.start() - 140):m.start()].split()).replace("|", "/")
        frase = frase.split("]")[-1].strip()[-120:]
        seg.setdefault(frase, set()).add(pg)

righe = ["# Coerenza dei dati e dei testi", "", "Generato da `tools/verifica-dati.py`.", "",
         f"**{sum(1 for _, ok in controlli if ok)} controlli superati su {len(controlli)}.**", ""]
righe += ["## Errori", ""] + [f"- {e}" for e in errori] if errori else ["Nessun errore."]
righe += ["", "## Controlli eseguiti", "", "| Controllo | Esito |", "|---|---|"] + [f"| {n} | {'superato' if ok else '**NON superato**'} |" for n, ok in controlli]
(ROOT / "docs/verifiche/dati.md").write_text("\n".join(righe) + "\n", encoding="utf-8")
s = ["# Segnaposto «[DA VERIFICARE con l'Ateneo]»", "", "Informazioni istituzionali non documentate nelle fonti: vanno confermate prima di un uso reale. Generato da `tools/verifica-dati.py` sulle pagine italiane (le inglesi hanno gli stessi segnaposto).", "",
     "| Contesto (testo che precede il segnaposto) | Pagine |", "|---|---|"]
s += [f"| …{k} | {', '.join(sorted(v)[:6])}{' e altre' if len(v) > 6 else ''} |" for k, v in sorted(seg.items(), key=lambda x: -len(x[1]))]
(ROOT / "docs/verifiche/segnaposto.md").write_text("\n".join(s) + "\n", encoding="utf-8")
print(f"{sum(1 for _, ok in controlli if ok)}/{len(controlli)} controlli superati; {len(seg)} segnaposto distinti")
for e in errori[:30]:
    print("  ", e)
sys.exit(1 if errori else 0)
