"""Genera scripts-lotto8/nav-<p>.js (apre la pagina e mette gli XPath MAUVE++ in window.__xs);
lo snippet si legge poi con scripts-lotto8/snip.js (mappa XPath -> HTML), salvato in tmp-lotto8/dom-<p>.json.
uso: python3 -I mknav.py <dir a11y> <pagina>..."""
import json, sys
A = sys.argv[1]
BASE = "https://andreock.github.io/hci_gruppo_a/anteprime/assignment3/"
for p in sys.argv[2:]:
    d = json.load(open(f"{A}/tmp-lotto8/mauve-{p}.json"))
    xs = sorted({x for c in d["crit"] for t in c["t"] for x in t["x"]})
    open(f"{A}/scripts-lotto8/nav-{p}.js", "w").write(
        'async (page) => { await page.goto("%s%s.html", { waitUntil: "load" }); '
        'await page.evaluate((xs) => { window.__xs = xs; }, %s); return page.url(); }' % (BASE, p, json.dumps(xs)))
