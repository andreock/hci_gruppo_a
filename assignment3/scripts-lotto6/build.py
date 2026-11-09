"""Lotto 6: costruisce a11y/results/<slug>.json dai dati grezzi in a11y/tmp-lotto6/.
Stessa logica di tmp-lotto2/build.py; snippet presi dalla mappa XPath -> HTML del DOM pubblicato (dom-<p>.json)."""
import json, collections, os, re

A = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(A, "tmp-lotto6")
BASE = "https://andreock.github.io/hci_gruppo_a/anteprime/assignment3/"
checks = json.load(open(f"{A}/achecks-checks.json"))

PAGES = {
    "progetto-dialetti-archivio": dict(template="scheda", checked_at="2026-11-09T13:26:00+01:00",
        mauve=dict(score=94, errors=6, warnings=4, compl=89),
        lh=dict(passed=29, na=31)),
    "progetto-plastica-batteri": dict(template="scheda", checked_at="2026-11-09T13:28:00+01:00",
        mauve=dict(score=94, errors=6, warnings=4, compl=89),
        lh=dict(passed=29, na=31)),
    "progetto-matematica-accessibile": dict(template="scheda", checked_at="2026-11-09T13:30:00+01:00",
        mauve=dict(score=94, errors=6, warnings=4, compl=89),
        lh=dict(passed=29, na=31)),
}

SAME = {p: ("Riepilogo (94%, 6 errori, 4 avvisi, completezza 89%) identico per le tre schede del lotto 6: stesso "
    "template scheda senza form di donazione (a differenza delle schede del lotto 4, che hanno un form e in più "
    "H98, C38, ARIA19, G199). HTML statico, non generato via JavaScript. Le occorrenze e gli XPath cambiano tra "
    "le pagine (es. C28 6/7/7; le pagine hanno 53/54/54 elementi segnalati), quindi i report sono distinti.")
    for p in ("progetto-dialetti-archivio", "progetto-plastica-batteri", "progetto-matematica-accessibile")}


def mauve(p, info):
    d = json.load(open(f"{D}/mauve-{p}.json"))
    assert d["url"] == BASE + p + ".html", d["url"]
    snip = json.load(open(f"{D}/dom-{p}.json"))
    tech = collections.OrderedDict()
    for c in d["crit"]:
        for t in c["t"]:
            k = (t["tech"], t["res"])
            e = tech.setdefault(k, dict(t=t, sc=[], lv=[]))
            e["sc"].append(c["sc"]); e["lv"].append(c["level"])
    issues, err_sc, warn_sc = [], set(), set()
    for (tid, res), e in tech.items():
        t = e["t"]
        tipo = "error" if res == "N" else "warning"
        (err_sc if tipo == "error" else warn_sc).update(e["sc"])
        el = []
        for x in t["x"]:
            s = snip.get(x) or x  # xpath non risolto: si lascia l'xpath
            if s not in el:
                el.append(s)
        issues.append(dict(tipo=tipo, criterio=", ".join(e["sc"]),
            livello="A" if "A" in e["lv"] else "AA", tecnica=tid,
            descrizione=t["title"], elemento=el[:3], occorrenze=t["n"]))
    issues.sort(key=lambda i: i["tipo"] != "error")
    m = info["mauve"]
    key = lambda s: [int(n) for n in s.split(".")]
    note = (f"WCAG 2.1 AA, Desktop Chrome. score = 'Accessibility percentage'; completezza {m['compl']}%. "
            f"Criteri in errore: {', '.join(sorted(err_sc, key=key))}; in avviso: {', '.join(sorted(warn_sc - err_sc, key=key))}. "
            "Occorrenze = segnalazioni per tecnica (da window.json_report della pagina dei risultati). "
            "Snippet ricavati dagli XPath di MAUVE++ sul DOM pubblicato (primi 3 elementi). "
            "Tecniche e occorrenze specifiche della pagina: non sembra il risultato di una pagina vuota. "
            + SAME.get(p, ""))
    return dict(status="ok", score=m["score"], errors=m["errors"], warnings=m["warnings"], issues=issues, note=note)


def clean(s):
    """Separa lo snippet dal testo di suggerimento che AChecker gli accoda."""
    s = s.strip()
    m = re.match(r"<(\w+)", s)
    if m:
        close = s.find(f"</{m.group(1)}>")
        cut = s.find(" ... ")
        if close >= 0 and (cut < 0 or close < cut):
            return s[: close + len(m.group(1)) + 3]
        if cut >= 0:
            return s[: cut + 4]
        gt = s.find(">")
        if gt >= 0:
            return s[: gt + 1]
    return s[:120]


def achecks(p):
    d = json.load(open(f"{D}/achecks-{p}.json"))
    g = collections.OrderedDict()
    for x in d:
        k = (x["pane"], x["id"])
        e = g.setdefault(k, dict(msg=x["msg"], el=[], n=0))
        e["n"] += 1
        s = f"L{x['line']}: {clean(x['rest'] or '')}" if x["line"] else None
        if s and len(e["el"]) < 1:
            e["el"].append(s)
    issues = []
    for (pane, cid), e in g.items():
        sc, lv = checks.get(cid, [None, None])
        issues.append(dict(tipo="error" if pane == "achecker-errors" else "warning",
            criterio=sc, livello=lv, check_id=cid, descrizione=e["msg"], elemento=e["el"], occorrenze=e["n"]))
    ne = sum(1 for x in d if x["pane"] == "achecker-errors")
    note = ("AChecker, WCAG 2.0 AA (Markup). AChecker non dà un punteggio: score null. errors = 'Known problems' "
            "(scheda ERRORS); warnings = 'Potential problems' da verificare a mano (scheda WARNINGS). Criterio WCAG "
            "ricavato dall'ID del controllo (vedi a11y/achecks-checks.json). Snippet: il primo elemento per controllo, "
            "come mostrato da AChecker (gli snippet lunghi sono abbreviati da AChecker con ' ...').")
    return dict(status="ok", score=None, errors=ne, warnings=len(d) - ne, issues=issues, note=note)


def ac(p):
    note = ("Strumento abbandonato dal lotto 4 (regola di LOOP.md: stesso blocco 'You have reached the daily "
            "limit for scanning websites' per 3 iterazioni consecutive). Anche per questo lotto l'utente ha "
            "indicato che il limite giornaliero è esaurito. URL non inviata; limite d'uso non aggirato.")
    return dict(status="skipped", score=None, errors=None, warnings=None, issues=[], note=note)


def lh(info):
    l = info["lh"]
    return dict(status="ok", score=100, errors=0, warnings=10, issues=[],
        note=("Lighthouse 13.0.1 via ACHECKS (opzione 'WCAG 2.1 AA computer', desktop emulato). score = punteggio "
              "Accessibility. Nessun audit fallito; warnings = 10 'Additional items to manually check' generici. "
              f"Passed audits {l['passed']}, not applicable {l['na']}."))


for p, info in PAGES.items():
    r = dict(url=BASE + p + ".html", template=info["template"], checked_at=info["checked_at"],
        tools=dict(mauve=mauve(p, info), accessibilitychecker=ac(p), achecks=achecks(p), achecks_lighthouse=lh(info)))
    json.dump(r, open(f"{A}/results/{p}.json", "w"), ensure_ascii=False, indent=2)
    print(p, {k: (v["status"], v["score"], v["errors"], v["warnings"]) for k, v in r["tools"].items()})
