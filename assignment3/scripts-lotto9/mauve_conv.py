"""Converte window.json_report di MAUVE++ nel formato 'crit' usato nei lotti precedenti.
uso: python3 -I mauve_conv.py <rep.json> <out.json>"""
import json, sys

d = json.load(open(sys.argv[1]))
url = d["contextInfo"]["evalInfo"]["url"]
crit = []
for g in d["results"]["pageReport"][0]["gdl"]:
    for c in g["criterion"]:
        ts = []
        for cp in c["checkpoints"]:
            for e in cp["err"]:
                xs = [l["xpathPointer"] for l in (e.get("errInfo") or {}).get("errLine", [])]
                ts.append(dict(tech=cp["id"], res="N" if cp["checkpointsresult"] == "N" else "W",
                               title=cp["summary"], n=e["occurrence"], x=xs))
        if ts:
            crit.append(dict(sc=c["idcriterion"], level=c["level"], res=c["criterionresult"],
                             fail=c["occfail"], ct=c["occcanttell"], t=ts))
json.dump(dict(url=url, crit=crit), open(sys.argv[2], "w"), ensure_ascii=False, indent=2)
types = sorted({e["type"] for g in d["results"]["pageReport"][0]["gdl"] for c in g["criterion"]
                for cp in c["checkpoints"] for e in cp["err"]})
print(url, len(crit), "criteri con segnalazioni; tipi err:", types)
for c in crit:
    print(c["sc"], c["level"], c["res"], [(t["tech"], t["res"], t["n"]) for t in c["t"]])
