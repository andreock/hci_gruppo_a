#!/usr/bin/env python3
"""Calcola i rapporti di contrasto WCAG 2.2 delle coppie di colori del design system.

Legge i token da css/ideablume.css, controlla le coppie elencate in COPPIE e scrive
docs/verifiche/contrasti.md. Esce con codice 1 se una coppia non raggiunge la soglia.
Uso (dalla cartella website/):  python3 tools/contrasto.py
"""
import re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
CSS = ROOT / "css" / "ideablume.css"
OUT = ROOT / "docs" / "verifiche" / "contrasti.md"

SOGLIE = {"testo": 4.5, "testo grande": 3.0, "componente": 3.0, "focus": 3.0}

# (primo piano, sfondo, tipo, dove si usa)
COPPIE = [
    ("ink", "bg", "testo", "Testo principale"),
    ("ink", "surface", "testo", "Testo in sezioni e riquadri"),
    ("ink", "surface-2", "testo", "Intestazioni di tabella, riquadri annidati"),
    ("ink", "brand-soft", "testo", "Testo nell'hero e nei riquadri informativi"),
    ("ink-muted", "bg", "testo", "Testo secondario, suggerimenti dei campi"),
    ("ink-muted", "surface", "testo", "Testo secondario nei riquadri"),
    ("ink-muted", "surface-2", "testo", "Testo secondario nei riquadri annidati"),
    ("ink-muted", "brand-soft", "testo", "Sottotitolo nell'hero"),
    ("brand", "bg", "testo", "Link, titoli in colore, pulsante secondario"),
    ("brand", "surface", "testo", "Link nei riquadri"),
    ("brand", "brand-soft", "testo", "Voce di menu corrente, link nei riquadri informativi"),
    ("brand-dark", "brand-soft", "testo", "Link e menu al passaggio del mouse, etichette di categoria"),
    ("brand-dark", "bg", "testo", "Link al passaggio del mouse"),
    ("on-brand", "brand", "testo", "Testo del pulsante principale"),
    ("on-brand", "brand-dark", "testo", "Pulsante principale al passaggio del mouse"),
    ("st-open-fg", "st-open-bg", "testo", "Badge «In corso»"),
    ("st-reached-fg", "st-reached-bg", "testo", "Badge «Obiettivo raggiunto»"),
    ("st-done-fg", "st-done-bg", "testo", "Badge «Conclusa · obiettivo raggiunto»; pulsante disattivato"),
    ("st-failed-fg", "st-failed-bg", "testo", "Badge «Conclusa · obiettivo non raggiunto»"),
    ("error", "bg", "testo", "Messaggio di errore sotto il campo"),
    ("error", "error-bg", "testo", "Titolo del riepilogo errori"),
    ("ink", "error-bg", "testo", "Testo del riepilogo errori"),
    ("success", "success-bg", "testo", "Messaggio di conferma"),
    ("ink", "success-bg", "testo", "Testo nella conferma"),
    ("warning", "warning-bg", "testo", "Avviso e segnaposto [DA VERIFICARE]"),
    ("ink", "warning-bg", "testo", "Testo negli avvisi; risposta FAQ evidenziata"),
    ("info", "info-bg", "testo", "Avviso informativo"),
    ("ink", "info-bg", "testo", "Testo negli avvisi informativi"),
    ("footer-fg", "footer-bg", "testo", "Testo e link del piè di pagina"),
    ("footer-muted", "footer-bg", "testo", "Nota «prototipo» nel piè di pagina"),
    ("footer-bg", "footer-fg", "testo", "Pulsante «Scrivici» nel piè di pagina"),
    ("#ffffff", "ink", "testo", "Link «Salta al contenuto»; «?» delle spiegazioni a comparsa"),
    ("#ffffff", "brand", "testo", "Numero del passo corrente; numeri di «Come funziona»"),
    ("#ffffff", "progress", "componente", "Spunta dei passi completati"),
    ("#ffffff", "error", "componente", "Icona «!» degli errori"),
    ("border-strong", "bg", "componente", "Bordo di campi, card, riquadri"),
    ("border-strong", "surface", "componente", "Bordo dei campi nei riquadri dei filtri"),
    ("progress", "track", "componente", "Parte raccolta della barra rispetto alla parte mancante"),
    ("progress", "bg", "componente", "Barra piena rispetto allo sfondo"),
    ("border-strong", "track", "componente", "Contorno della barra (la traccia ha anche un bordo)"),
    ("brand", "bg", "componente", "Bordo del pulsante secondario e della scelta selezionata"),
    ("error", "bg", "componente", "Bordo dei campi con errore"),
    ("st-open-fg", "bg", "componente", "Bordo dei badge sullo sfondo della card"),
    ("st-reached-fg", "bg", "componente", "Bordo dei badge sullo sfondo della card"),
    ("st-done-fg", "bg", "componente", "Bordo dei badge sullo sfondo della card"),
    ("st-failed-fg", "bg", "componente", "Bordo dei badge sullo sfondo della card"),
    ("focus", "bg", "focus", "Anello di focus su sfondo bianco"),
    ("focus", "surface", "focus", "Anello di focus nei riquadri"),
    ("focus", "brand-soft", "focus", "Anello di focus nell'hero e nei riquadri informativi"),
    ("focus", "warning-bg", "focus", "Anello di focus su risposta FAQ evidenziata"),
    ("focus-on-dark", "footer-bg", "focus", "Anello di focus nel piè di pagina"),
    ("focus-on-dark", "ink", "focus", "Anello di focus del link «Salta al contenuto»"),
]

def tokens():
    t = {}
    for name, val in re.findall(r"--c-([a-z0-9-]+):\s*(#[0-9a-fA-F]{6})", CSS.read_text(encoding="utf-8")):
        t[name] = val.lower()
    return t

def lum(hexc):
    r, g, b = (int(hexc[i:i + 2], 16) / 255 for i in (1, 3, 5))
    f = lambda c: c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b)

def ratio(a, b):
    la, lb = sorted((lum(a), lum(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)

def main():
    t = tokens()
    get = lambda k: k if k.startswith("#") else t[k]
    righe, errori = [], 0
    for fg, bg, tipo, dove in COPPIE:
        r = ratio(get(fg), get(bg))
        ok = r >= SOGLIE[tipo]
        errori += not ok
        nome = lambda k: k if k.startswith("#") else f"`--c-{k}` {t[k]}"
        it = lambda x, d: f"{x:.{d}f}".replace(".", ",")
        righe.append(f"| {nome(fg)} | {nome(bg)} | {tipo} | {it(SOGLIE[tipo], 1)}:1 | **{it(r, 2)}:1** | {'sì' if ok else '**NO**'} | {dove} |")
    testo = ["# Contrasti del design system", "",
             "Generato da `tools/contrasto.py` a partire dai token di `css/ideablume.css`.",
             "Soglie WCAG 2.2: testo normale 4,5:1 (1.4.3); testo grande, componenti dell'interfaccia e indicatori di focus 3:1 (1.4.11).", "",
             "| Primo piano | Sfondo | Tipo | Soglia | Rapporto | Supera | Dove si usa |", "|---|---|---|---|---|---|---|"]
    testo += righe
    testo += ["", f"Coppie controllate: {len(COPPIE)} · sotto soglia: {errori}.", ""]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(testo), encoding="utf-8")
    print(f"{len(COPPIE)} coppie, {errori} sotto soglia -> {OUT.relative_to(ROOT)}")
    for fg, bg, tipo, dove in COPPIE:
        r = ratio(get(fg), get(bg))
        if r < SOGLIE[tipo]:
            print(f"  NO  {fg} su {bg}: {r:.2f} < {SOGLIE[tipo]} ({dove})")
    return 1 if errori else 0

if __name__ == "__main__":
    sys.exit(main())
