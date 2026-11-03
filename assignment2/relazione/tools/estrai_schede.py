#!/usr/bin/env python3
"""Estrae una tantum il testo delle 24 schede HTML in schede/personas.md e schede/journeys.md.

Il testo non viene riscritto: cambia solo l'impaginazione. Dopo l'estrazione i due file .md
sono la fonte della relazione e si possono correggere a mano.
"""
import html, pathlib, re, subprocess
from html.parser import HTMLParser

BASE = pathlib.Path(__file__).resolve().parent.parent
REPO = BASE.parent.parent
A2 = "assignment2/personas/"
# P07-P09: revisione del 31/10/2026 delle sole schede persona.
REVISIONE = "d3e3440"
CAMPI = ["Nome convenzionale e descrizione del profilo", "Scenario e obiettivo principale", "Attività e comportamenti",
         "Bisogni e aspettative", "Bisogni informativi", "Obiettivi e motivazioni", "Difficoltà e frustrazioni",
         "Fiducia: che cosa la favorisce (+) e che cosa la riduce (−)", "Contesto e vincoli di utilizzo",
         "Competenze e strumenti digitali", "Esigenze di accessibilità", "Frase rappresentativa e provenienza",
         "Fonti ed evidenze disponibili", "Ipotesi da verificare e informazioni mancanti",
         "Frase rappresentativa", "Elementi da considerare nel progetto", "Aspetti da verificare con utenti"]
SOTTO = {"Bisogni informativi", "Fiducia: che cosa la favorisce (+) e che cosa la riduce (−)"}
SCARTA = re.compile(r"^(Compilate gli spazi|Per le citazioni, distinguete|Nominate le fasi|Cristina Gena|Human-Computer Interaction|Scheda persona|Scheda user journey|P\d\d · Scheda|J\d\d · Scheda|Emozioni: specificate se dichiarate)")


def testo_blocchi(sorgente):
    s = re.sub(r"<!--.*?-->", " ", sorgente, flags=re.S)
    s = re.sub(r"<(head|style|script|title|xml)\b.*?</\1>", " ", s, flags=re.S | re.I)
    s = re.sub(r"data:[a-z/+\-0-9]+;base64,[A-Za-z0-9+/=]+", "", s)
    s = re.sub(r"\s+", " ", s)
    s = re.sub(r"</?(p|div|li|tr|td|th|h\d|br|section|ul|ol|table|header|footer|figure|blockquote)\b[^>]*>", "\n", s, flags=re.I)
    s = re.sub(r"<[^>]+>", "", s)
    s = html.unescape(s).replace(" ", " ")
    return [re.sub(r"\s+", " ", r).strip() for r in s.split("\n") if r.strip()]


class Tabella(HTMLParser):
    def __init__(self):
        super().__init__()
        self.righe, self.cella, self.prof, self.dentro = [], None, 0, False
    def handle_starttag(self, t, a):
        if t == "table":
            self.prof += 1
        if self.prof == 1 and t == "tr":
            self.righe.append([])
        if self.prof == 1 and t in ("td", "th"):
            self.cella = [""]
            self.righe[-1].append(self.cella)
        if self.cella is not None and t in ("p", "li", "br", "div"):
            self.cella.append("")
    def handle_endtag(self, t):
        if t == "table":
            self.prof -= 1
            self.cella = None
        if t in ("td", "th"):
            self.cella = None
    def handle_data(self, d):
        if self.cella is not None:
            self.cella[-1] += d


def leggi(rel, commit=None):
    if commit:
        return subprocess.run(["git", "show", f"{commit}:{A2}{rel}"], cwd=REPO, capture_output=True, check=True).stdout.decode("utf-8", "replace")
    return (REPO / A2 / rel).read_text(encoding="utf-8", errors="replace")


def lista(righe):
    pul = [re.sub(r"^[•·\-–]\s*", "", r).strip() for r in righe]
    pul = [r for r in pul if r and not SCARTA.match(r)]
    if len(pul) == 1:
        return [pul[0]]
    return ["- " + r for r in pul]


def persona(rel, ident, commit=None):
    righe = testo_blocchi(leggi(rel, commit))
    testo = "\n".join(righe)
    # Intestazione: tutto ciò che precede il primo campo
    i0 = next(i for i, r in enumerate(righe) if r.startswith(CAMPI[0][:20]))
    testa = " ".join(righe[:i0])
    data = re.search(r"Data/versione:\s*(.*?)(?=\s*Servizio|\s*$)", testa)
    serv = re.search(r"Servizio o progetto:\s*(.*?)(?=\s*Tipo:|\s*P\d\d ·|\s*$)", testa)
    extra = re.search(r"(P\d\d · .*—.*)$", testa)
    tipo = "Proto-persona" if re.search(r"☒\s*Proto-persona", testa) else ""
    campi, cur = {}, None
    ordine = []
    for r in righe[i0:]:
        trovato = next((c for c in CAMPI if r == c or r.startswith(c + " ")), None)
        if trovato:
            cur = trovato
            ordine.append(cur)
            campi[cur] = []
            resto = r[len(trovato):].strip()
            if resto:
                campi[cur].append(resto)
        elif cur:
            campi[cur].append(r)
    nome = re.match(r"(?:•\s*)?([^,—(]+?),\s*\d+", campi[CAMPI[0]][0]) or re.match(r"(?:•\s*)?([A-ZÀ-Ú][\wà-ú]+)", campi[CAMPI[0]][0])
    return ident, data.group(1).strip() if data else "", serv.group(1).strip() if serv else "", tipo, ordine, campi, extra.group(1).strip() if extra else ""


def scrivi_persona(ident, titolo, data, serv, tipo, ordine, campi, extra):
    o = [":::persona", f"### {ident} · {titolo}", "", ":::meta", f"{data} · {serv}" + (f" · {tipo}" if tipo else "") + (f" · {extra}" if extra else ""), ":::", ""]
    aperto = False
    for c in ordine:
        if c in SOTTO:
            o += ["", f"**{c}**", ""] + lista(campi[c]) + [""]
            continue
        if aperto:
            o += [":::", ""]
        o += [f":::campo | {c}"] + lista(campi[c]) + [""]
        aperto = True
    o += [":::", ":::", ""]
    return "\n".join(o)


def journey(rel, ident, titolo):
    src = leggi(rel)
    righe = testo_blocchi(src)
    pulita = re.sub(r"<(head|style|script|title|xml)\b.*?</\1>", " ", re.sub(r"<!--.*?-->", " ", src, flags=re.S), flags=re.S | re.I)
    t = Tabella()
    t.feed(pulita)
    cella = lambda c: " ¶ ".join(x for x in (re.sub(r"\s+", " ", html.unescape(y).replace(" ", " ")).strip() for y in c) if x).replace("|", "/")
    tab = [[cella(c) for c in r] for r in t.righe if r]
    i_dim = next(i for i, r in enumerate(righe) if r == "Dimensione")
    testa = " ".join(righe[:i_dim])
    testa = re.sub(r"Nominate le fasi.*$", "", testa)
    testa = re.sub(r"^.*?(?=Gruppo:)", "", testa)
    # dopo la tabella
    ultima = tab[-1][-1].split(" ¶ ")[-1]
    coda = []
    for i, r in enumerate(righe):
        if r == ultima or r.endswith(ultima):
            coda = righe[i + 1:]
    coda = [c for c in coda if not SCARTA.match(c)]
    o = [":::journey", f"### {ident} · {titolo}", "", ":::meta"] + testa_journey(testa) + [":::", ""]
    o.append("| " + " | ".join(tab[0]) + " |")
    o.append("|" + "---|" * len(tab[0]))
    for r in tab[1:]:
        o.append("| " + " | ".join(r) + " |")
    o.append("")
    intest = [c for c in coda if c.startswith("Fonti e ipotesi")]
    coda = [c for c in coda if not c.startswith("Fonti e ipotesi")]
    if coda:
        o += ["**" + (intest[0] if intest else "Fonti e ipotesi") + "**", ""] + lista(coda)
    o += ["", ":::", ""]
    return "\n".join(o)


def testa_journey(testa):
    """Intestazione del journey su righe etichettate; delle caselle resta il valore spuntato."""
    t = re.sub(r"\s*·\s*(?=(Data/versione|Servizio|Scenario e obiettivo|Fine|Fine del percorso|Base):)", " ", testa)
    et = ["Gruppo", "Data/versione", "Servizio", "Mappa", "Base", "Persona", "Scenario e obiettivo", "Inizio del percorso", "Inizio", "Fine del percorso", "Fine"]
    parti = re.split(r"(?:^|\s)(" + "|".join(re.escape(e) for e in et) + r"):\s*", t)
    v = {}
    for k in range(1, len(parti) - 1, 2):
        v[parti[k]] = parti[k + 1].strip()
    for k in ("Mappa", "Base"):
        if k in v:
            scelto = re.findall(r"☒\s*([^☐☒]+)", v[k])
            v[k] = ", ".join(x.strip() for x in scelto) or "—"
    r = [f"**Persona:** {v.get('Persona', '')} · **Versione:** {v.get('Data/versione', '')} · **Servizio:** {v.get('Servizio', '')}",
         f"**Mappa:** {v.get('Mappa', '')} · **Base:** {v.get('Base', '')}",
         f"**Scenario e obiettivo:** {v.get('Scenario e obiettivo', '')}",
         f"**Inizio:** {v.get('Inizio del percorso', v.get('Inizio', ''))} · **Fine:** {v.get('Fine del percorso', v.get('Fine', ''))}"]
    out = []
    for x in r:
        out += [x, ""]
    return out


def main():
    P = ["P01_giuseppe_ferrero.html", "P02_sara_colombo.html", "P03_davide_rinaldi.html", "P04_tomas_garcia_scheda_persona.html",
         "P05_Luca_Moretti_scheda_persona.html", "P06_Elena_Conti_scheda_persona.html", "P07_giulia_esposito_persona.html",
         "P08_roberta_galli_persona.html", "P09_chiara_marino_persona.html", "P10_franco_gallo_persona.html",
         "P11_amir_haddad_persona.html", "P12_maria_lombardi_persona.html"]
    J = ["J01_giuseppe_ferrero.html", "J02_sara_colombo.html", "J03_davide_rinaldi.html", "J04_Tomas_Garcia_user_journey.html",
         "J05_Luca_Moretti_user_journey.html", "J06_Elena_Conti_user_journey.html", "J07_giulia_esposito_journey.html",
         "J08_roberta_galli_journey.html", "J09_chiara_marino_journey.html", "J10_franco_gallo_journey.html",
         "J11_amir_haddad_journey.html", "J12_maria_lombardi_journey.html"]
    NOMI = ["Giuseppe Ferrero", "Sara Colombo", "Davide Rinaldi", "Tomás García", "Luca Moretti", "Elena Conti", "Giulia Esposito",
            "Roberta Galli", "Chiara Marino", "Franco Gallo", "Amir Haddad", "Maria Lombardi"]
    out = []
    for k, (f, n) in enumerate(zip(P, NOMI), 1):
        commit = REVISIONE if 7 <= k <= 9 else None
        ident, data, serv, tipo, ordine, campi, extra = persona("personas/" + f, f"P{k:02d}", commit)
        attesi = 9 if 7 <= k <= 9 else 12
        if len([c for c in ordine if c not in SOTTO]) < attesi:
            print("Campi mancanti", ident, ordine)
        out.append(scrivi_persona(ident, n, data, serv, tipo, ordine, campi, extra))
    (BASE / "schede" / "personas.md").write_text("\n".join(out), encoding="utf-8")
    out = [journey("journey/" + f, f"J{k:02d}", n) for k, (f, n) in enumerate(zip(J, NOMI), 1)]
    (BASE / "schede" / "journeys.md").write_text("\n".join(out), encoding="utf-8")


if __name__ == "__main__":
    main()
