import json, collections, os
D = os.path.dirname(os.path.abspath(__file__))
A = os.path.dirname(D)
BASE = "https://andreock.github.io/hci_gruppo_a/anteprime/assignment3/"
snip = json.load(open(f"{D}/snip-programma.json"))
snip.update({
    "//html/body/main/section[1]/ul/li[1]/section/p[2]/a": "<a class=\"btn\" href=\"candidatura.html\">Candidati al programma</a>",
    "//html/body/main/section[1]/ul/li[2]/section/p[2]/a": "<a class=\"btn\" href=\"collabora.html\">Proponi una collaborazione</a>",
})
checks = json.load(open(f"{A}/achecks-checks.json"))

PAGES = {
    "come-funziona": dict(checked_at="2026-11-09T12:10:00+01:00",
        mauve=dict(score=94, errors=6, warnings=3, compl=91),
        ac=dict(status="ok", score=90, errors=0, warnings=22, passed=40, na=58),
        lh=dict(passed=22, na=38, retry=True)),
    "programma": dict(checked_at="2026-11-09T12:17:00+01:00",
        mauve=dict(score=94, errors=6, warnings=3, compl=91),
        ac=dict(status="skipped"),
        lh=dict(passed=24, na=36, retry=False)),
    "proponi": dict(checked_at="2026-11-09T12:20:00+01:00",
        mauve=dict(score=94, errors=6, warnings=3, compl=93),
        ac=dict(status="skipped"),
        lh=dict(passed=23, na=37, retry=False)),
}
TEMPLATE = {"come-funziona": "contenuto", "programma": "contenuto", "proponi": "contenuto"}


def mauve(p, info):
    d = json.load(open(f"{D}/mauve-{p}.json"))
    assert d["url"] == BASE + p + ".html", d["url"]
    # una voce per tecnica (stessa tecnica su più criteri -> criteri uniti), come nel lotto 1
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
            s = snip.get(x)
            if s is None:
                s = x  # xpath non risolto: si lascia l'xpath
            if s not in el:
                el.append(s)
        issues.append(dict(tipo=tipo, criterio=", ".join(e["sc"]),
            livello="A" if "A" in e["lv"] else "AA", tecnica=tid,
            descrizione=t["title"], elemento=el[:3], occorrenze=t["n"]))
    issues.sort(key=lambda i: i["tipo"] != "error")
    m = info["mauve"]
    note = (f"WCAG 2.1 AA, Desktop Chrome. score = 'Accessibility percentage'; completezza {m['compl']}%. "
            f"Criteri in errore: {', '.join(sorted(err_sc))}; in avviso: {', '.join(sorted(warn_sc - err_sc))}. "
            "Occorrenze = segnalazioni per tecnica (dal report JSON della pagina). "
            "Snippet ricavati dagli XPath di MAUVE++ sul DOM pubblicato (primi 3 elementi). "
            "I contatori di riepilogo (6 errori, 3 avvisi) coincidono con quelli di altre pagine, ma le tecniche e "
            "le occorrenze variano da pagina a pagina: non sembra il risultato di una pagina vuota.")
    return dict(status="ok", score=m["score"], errors=m["errors"], warnings=m["warnings"], issues=issues, note=note)


def clean(s):
    """Separa lo snippet dal testo di suggerimento che AChecker gli accoda."""
    import re
    s = s.strip()
    m = re.match(r"<(\w+)", s)
    if m:
        close = s.find(f"</{m.group(1)}>")
        cut = s.find(" ... ")
        if close >= 0 and (cut < 0 or close < cut):
            return s[: close + len(m.group(1)) + 3]
        if cut >= 0:
            return s[: cut + 4]
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
    nw = len(d) - ne
    note = ("AChecker, WCAG 2.0 AA (Markup). AChecker non dà un punteggio: score null. errors = 'Known problems' "
            "(scheda ERRORS); warnings = 'Potential problems' da verificare a mano (scheda WARNINGS). Criterio WCAG "
            "ricavato dall'ID del controllo (vedi a11y/achecks-checks.json). Snippet: il primo elemento per controllo, "
            "come mostrato da AChecker (gli snippet lunghi sono abbreviati da AChecker con ' ...').")
    return dict(status="ok", score=None, errors=ne, warnings=nw, issues=issues, note=note)


def ac(info):
    a = info["ac"]
    if a["status"] == "skipped":
        return dict(status="skipped", score=None, errors=None, warnings=None, issues=[],
            note="Scansione non eseguita: il sito mostra 'Scan unavailable – You have reached the daily limit for "
                 "scanning websites'. Limite d'uso gratuito, non aggirato.")
    return dict(status="ok", score=a["score"], errors=a["errors"], warnings=a["warnings"], issues=[],
        note=(f"Scansione gratuita della singola URL (WCAG 2.2, 138 criteri). score = punteggio 'WCAG & ADA compliance' "
              f"su 100. errors = 'Critical Issues'. warnings = 'Required Manual Audits': {a['warnings']} procedure manuali "
              f"generiche, non legate a elementi della pagina; la versione gratuita mostra solo i titoli. "
              f"Passed audits {a['passed']}, not applicable {a['na']}."))


def lh(info):
    l = info["lh"]
    note = ("Lighthouse 13.0.1 via ACHECKS (opzione 'WCAG 2.1 AA computer', desktop emulato). score = punteggio "
            "Accessibility. Nessun audit fallito; warnings = 10 'Additional items to manually check' generici. "
            f"Passed audits {l['passed']}, not applicable {l['na']}.")
    if l["retry"]:
        note += " Il primo invio si è chiuso senza risultato (modulo azzerato); riuscito al secondo tentativo."
    return dict(status="ok", score=100, errors=0, warnings=10, issues=[], note=note)


for p, info in PAGES.items():
    r = dict(url=BASE + p + ".html", template=TEMPLATE[p], checked_at=info["checked_at"],
        tools=dict(mauve=mauve(p, info), accessibilitychecker=ac(info), achecks=achecks(p), achecks_lighthouse=lh(info)))
    json.dump(r, open(f"{A}/results/{p}.json", "w"), ensure_ascii=False, indent=2)
    print(p, {k: (v["status"], v["errors"], v["warnings"]) for k, v in r["tools"].items()})
