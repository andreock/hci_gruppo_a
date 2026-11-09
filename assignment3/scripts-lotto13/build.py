"""Lotto 13: costruisce a11y/results/<slug>.json dai dati grezzi in a11y/tmp-lotto13/.
Come scripts-lotto12/build.py; le pagine en/ usano lo slug 'en-<nome>' (nota del lotto 6) per non sovrascrivere le IT."""
import json, collections, os, re

A = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(A, "tmp-lotto13")
BASE = "https://andreock.github.io/hci_gruppo_a/anteprime/assignment3/"
checks = json.load(open(f"{A}/achecks-checks.json"))

PAGES = {
    "en-progetto-aria-aperta": dict(path="en/progetto-aria-aperta.html", template="scheda", checked_at="2026-11-09T14:38:00+01:00",
        mauve=dict(score=93, errors=8, warnings=5, compl=88),
        lh=dict(passed=29, na=31)),
    "en-candidatura": dict(path="en/candidatura.html", template="form", checked_at="2026-11-09T14:40:00+01:00",
        mauve=dict(score=92, errors=8, warnings=5, compl=85),
        lh=dict(passed=24, na=36)),
    "en-collabora": dict(path="en/collabora.html", template="form", checked_at="2026-11-09T14:42:00+01:00",
        mauve=dict(score=92, errors=8, warnings=5, compl=85),
        lh=dict(passed=24, na=36)),
}

_S = ("Versione inglese di %s: stesso riepilogo della pagina IT (%s: %s) "
      "e stesse occorrenze per tecnica (%s). Non sembra un risultato duplicato: l'URL nel report è quello inglese e "
      "gli snippet sono in inglese.")
SAME = {
    "en-progetto-aria-aperta": _S % ("progetto-aria-aperta.html", "lotto 4", "93%, 8 errori, 5 avvisi, completezza 88%", "F73 7, C28 12, C21 17, F96 14"),
    "en-candidatura": _S % ("candidatura.html", "lotto 5", "92%, 8 errori, 5 avvisi, completezza 85%", "H98 7, C38 2, C21 10, F96 18"),
    "en-collabora": _S % ("collabora.html", "lotto 5", "92%, 8 errori, 5 avvisi, completezza 85%", "H98 5, C38 1, C21 8, F96 15"),
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
