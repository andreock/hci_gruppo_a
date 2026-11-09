"""Genera scripts-lotto15/nav-<slug>.js (apre la pagina e mette gli XPath MAUVE++ in window.__xs).
uso: python3 -I mknav.py <dir a11y> <slug>=<percorso>..."""
import json, sys
A = sys.argv[1]
BASE = "https://andreock.github.io/hci_gruppo_a/anteprime/assignment3/"
for arg in sys.argv[2:]:
    s, path = arg.split("=", 1)
    d = json.load(open(f"{A}/tmp-lotto15/mauve-{s}.json"))
    xs = sorted({x for c in d["crit"] for t in c["t"] for x in t["x"]})
    open(f"{A}/scripts-lotto15/nav-{s}.js", "w").write(
        'async (page) => { await page.goto("%s%s", { waitUntil: "load" }); '
        'await page.evaluate((xs) => { window.__xs = xs; }, %s); return page.url(); }' % (BASE, path, json.dumps(xs)))
