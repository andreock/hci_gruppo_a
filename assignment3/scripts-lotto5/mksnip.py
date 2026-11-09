"""Genera scripts-lotto5/snip-<p>.js con gli XPath unici di MAUVE++ (uso: python3 -I mksnip.py <a11y-dir> <p>...)."""
import json, sys, os
A = sys.argv[1]
TPL = open(os.path.join(A, "scripts-lotto4/snip-progetto-alveari-sani.js")).read()
i0 = TPL.index("const xs = ") + len("const xs = "); i1 = TPL.index("; const out")
for p in sys.argv[2:]:
    d = json.load(open(f"{A}/tmp-lotto5/mauve-{p}.json"))
    xs = sorted({x for c in d["crit"] for t in c["t"] for x in t["x"]})
    open(f"{A}/scripts-lotto5/snip-{p}.js", "w").write(TPL[:i0] + json.dumps(xs) + TPL[i1:])
    print(p, len(xs))
