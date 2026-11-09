"""Lotto 10: costruisce a11y/results/<slug>.json dai dati grezzi in a11y/tmp-lotto10/.
Come scripts-lotto9/build.py; le pagine en/ usano lo slug 'en-<nome>' (nota del lotto 6) per non sovrascrivere le IT."""
import json, collections, os, re

A = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(A, "tmp-lotto10")
BASE = "https://andreock.github.io/hci_gruppo_a/anteprime/assignment3/"
checks = json.load(open(f"{A}/achecks-checks.json"))

PAGES = {
    "en-chi-siamo": dict(path="en/chi-siamo.html", template="contenuto", checked_at="2026-11-09T13:55:00+01:00",
        mauve=dict(score=94, errors=6, warnings=3, compl=92),
        lh=dict(passed=23, na=37)),
    "en-come-funziona": dict(path="en/come-funziona.html", template="contenuto", checked_at="2026-11-09T13:56:00+01:00",
        mauve=dict(score=94, errors=6, warnings=3, compl=91),
        lh=dict(passed=22, na=38)),
    "en-programma": dict(path="en/programma.html", template="contenuto", checked_at="2026-11-09T13:57:00+01:00",
        mauve=dict(score=94, errors=6, warnings=3, compl=91),
        lh=dict(passed=24, na=36)),
}

SAME = {
    "en-chi-siamo": ("Versione inglese di chi-siamo.html: stesso riepilogo della pagina IT (lotto 1: 94%, 6 errori, "
        "3 avvisi). Non sembra un risultato duplicato: XPath e occorrenze sono quelli della pagina inglese (F73 3)."),
    "en-come-funziona": ("Versione inglese di come-funziona.html: stesso riepilogo della pagina IT (lotto 2: 94%, "
        "6/3). Le occorrenze cambiano rispetto a en/chi-siamo (F73 1 invece di 3)."),
    "en-programma": ("Versione inglese di programma.html: stesso riepilogo della pagina IT (lotto 2: 94%, 6/3). "
        "Riepilogo uguale anche alle altre due pagine EN del lotto, ma i controlli no: qui compaiono F46 e H73 "
        "(tabelle, 1.3.1) e F96 ha 5 occorrenze invece di 3."),
}

def mauve(p, info):
    d = json.load(open(f"{D}/mauve-{p}.json"))
    assert d["url"] == BASE + PAGES[p]["path"], d["url"]
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


def lh(p, info):
    l = info["lh"]
    issues, extra = [], ""
    return dict(status="ok", score=100, errors=0, warnings=10 + len(issues), issues=issues,
        note=("Lighthouse 13.0.1 via ACHECKS (opzione 'WCAG 2.1 AA computer', desktop emulato). score = punteggio "
              "Accessibility. Nessun audit fallito; 10 'Additional items to manually check' generici. "
              f"Passed audits {l['passed']}, not applicable {l['na']}." + extra))


LH_EXTRA = {}

for p, info in PAGES.items():
    r = dict(url=BASE + info["path"], template=info["template"], checked_at=info["checked_at"],
        tools=dict(mauve=mauve(p, info), accessibilitychecker=ac(p), achecks=achecks(p), achecks_lighthouse=lh(p, info)))
    r['tools']['achecks_lighthouse']['note'] += LH_EXTRA.get(p, '')
    json.dump(r, open(f"{A}/results/{p}.json", "w"), ensure_ascii=False, indent=2)
    print(p, {k: (v["status"], v["score"], v["errors"], v["warnings"]) for k, v in r["tools"].items()})
