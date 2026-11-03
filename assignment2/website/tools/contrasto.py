#!/usr/bin/env python3
"""Calcola i rapporti di contrasto WCAG 2.2 delle coppie di colori del design system.

Legge i token da css/ideablume.css per il tema chiaro (tra i segni @tema-chiaro e @tema-scuro)
e per il tema scuro (gli stessi token, sovrascritti tra @tema-scuro e @fine-temi), controlla
le coppie elencate in COPPIE in entrambi i temi e scrive docs/verifiche/contrasti.md.
Esce con codice 1 se una coppia non raggiunge la soglia.
Uso (dalla cartella website/):  python3 tools/contrasto.py
"""
import re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
CSS = ROOT / "css" / "ideablume.css"
OUT = ROOT / "docs" / "verifiche" / "contrasti.md"

SOGLIE = {"testo": 4.5, "testo grande": 3.0, "componente": 3.0, "focus": 3.0}

# (primo piano, sfondo, tipo, dove si usa)
COPPIE = [
    ("ink", "bg", "testo", "Testo principale su card e riquadri"),
    ("ink", "page", "testo", "Testo principale sullo sfondo della pagina"),
    ("ink-muted", "page", "testo", "Testo secondario sullo sfondo della pagina"),
    ("brand", "page", "testo", "Link sullo sfondo della pagina"),
    ("ink", "hero-1", "testo", "Testo dell'hero sulla sfumatura pesca"),
    ("ink", "hero-2", "testo", "Testo dell'hero sulla sfumatura miele"),
    ("ink-muted", "hero-1", "testo", "Testo secondario dell'hero sulla sfumatura pesca"),
    ("ink-muted", "hero-2", "testo", "Testo secondario dell'hero sulla sfumatura miele"),
    ("brand", "hero-1", "testo", "Link dell'hero sulla sfumatura pesca"),
    ("brand", "hero-2", "testo", "Link dell'hero sulla sfumatura miele"),
    ("progress", "bg", "testo", "Percentuale raggiunta nel riquadro di stato"),
    ("accent", "footer-bg", "testo", "Numeri della fascia «I numeri di ideaBlume»"),
    ("accent", "promo-from", "testo", "Numeri della fascia, nella zona della sfumatura"),
    ("footer-muted", "promo-from", "testo", "Testo della fascia e del piè di pagina nella zona della sfumatura"),
    ("footer-accent", "footer-bg", "testo", "Marchio nel piè di pagina"),
    ("promo-fg", "promo-from", "testo", "Testo del riquadro di invito (inizio sfumatura)"),
    ("promo-fg", "promo-to", "testo", "Testo del riquadro di invito (fine sfumatura)"),
    ("promo-from", "promo-fg", "testo", "Pulsante chiaro del riquadro di invito"),
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
    ("on-primary", "primary", "testo", "Testo del pulsante normale (ricerca, invio moduli)"),
    ("on-primary", "primary-hover", "testo", "Pulsante normale al passaggio del mouse"),
    ("on-cta", "cta", "testo", "Testo del pulsante «Sostieni il progetto»"),
    ("on-cta", "cta-hover", "testo", "Pulsante «Sostieni il progetto» al passaggio del mouse e durante il pagamento"),
    ("on-brand", "brand", "testo", "Testo su fondo del marchio: selezione del testo"),
    ("on-brand", "brand-dark", "testo", "Testo su fondo del marchio scuro"),
    ("ink", "bg", "testo", "Testo della card della ricompensa"),
    ("ink", "brand-soft", "testo", "Testo della ricompensa selezionata"),
    ("ink-muted", "brand-soft", "testo", "Nota della ricompensa selezionata"),
    ("brand-dark", "surface", "testo", "Etichette nelle sezioni tinte"),
    ("secondary", "page", "testo", "Conferme in verde sullo sfondo della pagina"),
    ("secondary", "bg", "testo", "Conferme in verde sulle card"),
    ("st-open-fg", "st-open-bg", "testo", "Badge «In corso»"),
    ("st-reached-fg", "st-reached-bg", "testo", "Badge «Obiettivo raggiunto»"),
    ("st-done-fg", "st-done-bg", "testo", "Badge «Conclusa · obiettivo raggiunto»; pulsante disattivato"),
    ("st-failed-fg", "st-failed-bg", "testo", "Badge «Conclusa · obiettivo non raggiunto»"),
    ("error", "bg", "testo", "Messaggio di errore sotto il campo"),
    ("error", "error-bg", "testo", "Titolo del riepilogo errori"),
    ("ink", "error-bg", "testo", "Testo del riepilogo errori"),
    ("success", "success-bg", "testo", "Messaggio di conferma"),
    ("ink", "success-bg", "testo", "Testo nella conferma"),
    ("warning", "warning-bg", "testo", "Avviso"),
    ("ink", "warning-bg", "testo", "Testo negli avvisi; risposta FAQ evidenziata"),
    ("info", "info-bg", "testo", "Avviso informativo"),
    ("ink", "info-bg", "testo", "Testo negli avvisi informativi"),
    ("footer-fg", "footer-bg", "testo", "Testo e link del piè di pagina"),
    ("footer-muted", "footer-bg", "testo", "Nota nel piè di pagina"),
    ("footer-bg", "footer-fg", "testo", "Pulsante «Scrivici» nel piè di pagina"),
    ("bg", "ink", "testo", "Link «Salta al contenuto»; «?» delle spiegazioni a comparsa"),
    ("on-brand", "brand", "testo", "Numero del passo corrente; numeri di «Come funziona»"),
    ("on-secondary", "secondary", "componente", "Spunta dei passi completati"),
    ("on-error", "error", "componente", "Icona «!» degli errori"),
    ("border-strong", "bg", "componente", "Bordo di campi e controlli"),
    ("border-strong", "page", "componente", "Bordo del campo di ricerca sullo sfondo della pagina"),
    ("border-strong", "hero-1", "componente", "Bordo del campo di ricerca nell'hero"),
    ("secondary", "page", "componente", "Spunte dell'hero"),
    ("secondary", "hero-2", "componente", "Spunte dell'hero sulla sfumatura miele"),
    ("cta", "page", "componente", "Pulsante «Sostieni il progetto» sullo sfondo della pagina"),
    ("cta", "bg", "componente", "Pulsante «Sostieni il progetto» sulla card"),
    ("cta", "brand-soft", "componente", "Bordo della ricompensa selezionata"),
    ("brand", "page", "componente", "Icona dell'interruttore del tema"),
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
    ("focus", "bg", "focus", "Anello di focus su card e campi"),
    ("focus", "page", "focus", "Anello di focus sullo sfondo della pagina"),
    ("focus", "hero-1", "focus", "Anello di focus nell'hero"),
    ("focus-on-dark", "promo-from", "focus", "Anello di focus nel riquadro di invito"),
    ("focus", "surface", "focus", "Anello di focus nei riquadri"),
    ("focus", "brand-soft", "focus", "Anello di focus nell'hero e nei riquadri informativi"),
    ("focus", "warning-bg", "focus", "Anello di focus su risposta FAQ evidenziata"),
    ("focus-on-dark", "footer-bg", "focus", "Anello di focus nel piè di pagina"),
    ("focus-skip", "ink", "focus", "Anello di focus del link «Salta al contenuto»"),
]

def tokens():
    """Restituisce {"chiaro": {...}, "scuro": {...}}; il tema scuro eredita i token che non ridefinisce."""
    css = CSS.read_text(encoding="utf-8")
    leggi = lambda testo: {n: v.lower() for n, v in re.findall(r"--c-([a-z0-9-]+):\s*(#[0-9a-fA-F]{6})", testo)}
    chiaro = leggi(css[css.index("@tema-chiaro:"):css.index("@tema-scuro:")])
    scuro = dict(chiaro, **leggi(css[css.index("@tema-scuro:"):css.index("@fine-temi")]))
    return {"chiaro": chiaro, "scuro": scuro}

def lum(hexc):
    r, g, b = (int(hexc[i:i + 2], 16) / 255 for i in (1, 3, 5))
    f = lambda c: c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b)

def ratio(a, b):
    la, lb = sorted((lum(a), lum(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)

def main():
    temi = tokens()
    it = lambda x, d: f"{x:.{d}f}".replace(".", ",")
    testo = ["# Contrasti del design system", "",
             "Generato da `tools/contrasto.py` a partire dai token di `css/ideablume.css`, per il tema chiaro e per il tema scuro",
             "(il tema predefinito è quello chiaro; quello scuro si sceglie con l'interruttore nell'intestazione).",
             "Soglie WCAG 2.2: testo normale 4,5:1 (1.4.3); testo grande, componenti dell'interfaccia e indicatori di focus 3:1 (1.4.11).", ""]
    errori_tot = 0
    for tema, t in temi.items():
        get = lambda k: k if k.startswith("#") else t[k]
        nome = lambda k: k if k.startswith("#") else f"`--c-{k}` {t[k]}"
        righe, errori = [], 0
        for fg, bg, tipo, dove in COPPIE:
            r = ratio(get(fg), get(bg))
            ok = r >= SOGLIE[tipo]
            errori += not ok
            righe.append(f"| {nome(fg)} | {nome(bg)} | {tipo} | {it(SOGLIE[tipo], 1)}:1 | **{it(r, 2)}:1** | {'sì' if ok else '**NO**'} | {dove} |")
            if not ok:
                print(f"  NO  [{tema}] {fg} su {bg}: {r:.2f} < {SOGLIE[tipo]} ({dove})")
        testo += [f"## Tema {tema}", "", "| Primo piano | Sfondo | Tipo | Soglia | Rapporto | Supera | Dove si usa |",
                  "|---|---|---|---|---|---|---|"] + righe + ["", f"Coppie controllate: {len(COPPIE)} · sotto soglia: {errori}.", ""]
        errori_tot += errori
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(testo), encoding="utf-8")
    print(f"{len(COPPIE)} coppie × {len(temi)} temi, {errori_tot} sotto soglia -> {OUT.relative_to(ROOT)}")
    return 1 if errori_tot else 0


if __name__ == "__main__":
    sys.exit(main())
