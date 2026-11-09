"""Genera scripts-lotto5/nav-<p>.js: apre la pagina e mette gli XPath MAUVE++ in window.__xs."""
import json, sys
A = sys.argv[1]
BASE = "https://andreock.github.io/hci_gruppo_a/anteprime/assignment3/"
for p in sys.argv[2:]:
    d = json.load(open(f"{A}/tmp-lotto5/mauve-{p}.json"))
    xs = sorted({x for c in d["crit"] for t in c["t"] for x in t["x"]})
    open(f"{A}/scripts-lotto5/nav-{p}.js", "w").write(
        'async (page) => { await page.goto("%s%s.html", { waitUntil: "load" }); '
        'await page.evaluate((xs) => { window.__xs = xs; }, %s); return page.url(); }' % (BASE, p, json.dumps(xs)))
