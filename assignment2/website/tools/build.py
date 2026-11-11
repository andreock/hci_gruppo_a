#!/usr/bin/env python3
"""Genera il sito statico ideaBlume (italiano nella radice, inglese in en/).

Fonti:  data/sito.json, data/progetti.json, i18n/it.json, i18n/en.json
Uscita: *.html, en/*.html, data/ib-dati.js, img/progetti/*.svg, css/font-locali.css
Uso (dalla cartella website/):  python3 tools/build.py
La data di riferimento è oggi; si può forzare con IB_OGGI=AAAA-MM-GG (utile per i test).
Solo libreria standard: nessuna dipendenza da installare.
"""
import base64
import datetime as dt
import hashlib
import html
import json
import os
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITO = json.loads((ROOT / "data/sito.json").read_text(encoding="utf-8"))
PROGETTI = json.loads((ROOT / "data/progetti.json").read_text(encoding="utf-8"))
I18N = {l: json.loads((ROOT / f"i18n/{l}.json").read_text(encoding="utf-8")) for l in ("it", "en")}
OGGI = dt.date.fromisoformat(os.environ["IB_OGGI"]) if os.environ.get("IB_OGGI") else dt.date.today()
LINGUE = ("it", "en")
E = html.escape


# ---------------------------------------------------------------- utilità
class ChiaveMancante(Exception):
    pass


def t(lang, path):
    """Restituisce la stringa di traduzione; si ferma se manca (requisito R-110)."""
    cur = I18N[lang]
    for k in path.split("."):
        if isinstance(cur, dict) and k in cur:
            cur = cur[k]
        elif isinstance(cur, list) and k.isdigit():
            cur = cur[int(k)]
        else:
            raise ChiaveMancante(f"[{lang}] chiave mancante: {path}")
    return cur


def data_da(spec):
    """'AAAA-MM-GG' oppure 'rel:N' (N giorni da oggi)."""
    if spec.startswith("rel:"):
        return OGGI + dt.timedelta(days=int(spec[4:]))
    return dt.date.fromisoformat(spec)


def fmt_data(d, lang, lunga=False):
    if lang == "it":
        return f"{d.day} {t('it', 'mesi')[d.month - 1]} {d.year}" if lunga else d.strftime("%d/%m/%Y")
    return f"{d.day} {t('en', 'mesi')[d.month - 1]} {d.year}"


def time_tag(spec, lang, lunga=False):
    """<time> con data-rel per le date relative: il browser le ricalcola da oggi (D-24, D-27)."""
    d = data_da(spec)
    rel = f' data-rel="{spec[4:]}"' if spec.startswith("rel:") else ""
    lng = ' data-lunga="1"' if lunga else ""
    return f'<time datetime="{d.isoformat()}"{rel}{lng}>{fmt_data(d, lang, lunga)}</time>'


def euro(x, lang):
    intero = abs(x - round(x)) < 1e-9
    if lang == "it":
        s = f"{x:,.0f}" if intero else f"{x:,.2f}"
        s = s.replace(",", "X").replace(".", ",").replace("X", ".")
        return f"€ {s}"
    s = f"{x:,.0f}" if intero else f"{x:,.2f}"
    return f"€{s}"


def perc(x):
    return f"{round(x)}%"


def ctx_base(lang):
    c = SITO["contatti"]
    r = SITO["regole"]
    tel = f'<a href="tel:{c["telefono"].replace(" ", "")}">{c["telefono_visibile"]}</a>'
    mail = lambda k: f'<a href="mailto:{c[k]}">{c[k]}</a>'
    return {
        "min": euro(r["minimo_libero"], lang), "tetto": euro(r["tetto_cofinanziamento"], lang),
        "dmin": str(r["durata_min_giorni"]), "dmax": str(r["durata_max_giorni"]),
        "tel": c["telefono_visibile"], "tel_link": tel, "orari": c["orari"][lang],
        "giorni": str(c["risposta_giorni"]), "indirizzo": c["indirizzo"],
        "email_aiuto_link": mail("email_aiuto"), "email_programma_link": mail("email_programma"),
        "email_collaborazioni_link": mail("email_collaborazioni"), "email_programma": mail("email_programma"),
        "metodi": ", ".join(m["nome"][lang] for m in SITO["metodi_pagamento"]),
        "edizione": str(SITO["bando"]["edizione"]), "candidature": SITO["bando"]["periodo"][lang],
        "scadenza_bando": SITO["bando"]["scadenza"][lang],
    }


def fmt(s, lang, **extra):
    """Sostituisce {link:url|testo}, {ext:url|testo} e {variabile}."""
    ctx = ctx_base(lang)
    ctx.update(extra)
    s = re.sub(r"\{link:([^|}]+)\|([^}]+)\}", lambda m: f'<a href="{E(m.group(1))}">{m.group(2)}</a>', s)
    s = re.sub(r"\{ext:([^|}]+)\|([^}]+)\}",
               lambda m: f'<a href="{E(m.group(1))}" class="ext">{m.group(2)} <span class="vh">{t(lang, "common.external")}</span></a>', s)

    def var(m):
        k = m.group(1)
        if k not in ctx:
            raise ChiaveMancante(f"[{lang}] variabile non definita: {{{k}}} in «{s[:60]}…»")
        return str(ctx[k])
    return re.sub(r"\{([a-z_]+)\}", var, s)


# ---------------------------------------------------------------- progetti
def calcola(p):
    """Campi derivati di un progetto: un'unica funzione per tutto il sito (R-022)."""
    inizio, scad = data_da(p["inizio"]), data_da(p["scadenza"])
    perc_ = 100 * p["raccolto"] / p["obiettivo"]
    raggiunto = p["raccolto"] >= p["obiettivo"]
    giorni = (scad - OGGI).days
    if giorni < 0:
        stato = "done" if raggiunto else "failed"
    else:
        stato = "reached" if raggiunto else "open"
    cofin = min(p["obiettivo"], SITO["regole"]["tetto_cofinanziamento"]) if (p["programma"] and raggiunto) else 0
    sost = sum(r["scelte"] for r in p["ricompense"]) + p["libere"]
    return dict(inizio=inizio, scadenza=scad, perc=perc_, raggiunto=raggiunto, giorni=giorni, stato=stato,
                cofin=cofin, totale=p["raccolto"] + cofin, sostenitori=sost, aperto=giorni >= 0)


for p in PROGETTI:
    p["_"] = calcola(p)
PER_SLUG = {p["slug"]: p for p in PROGETTI}

ICONE = {
    "open": '<svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><circle cx="8" cy="8" r="6" fill="none" stroke="currentColor" stroke-width="2"/></svg>',
    "reached": '<svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M3 8.5l3.2 3L13 4.5" fill="none" stroke="currentColor" stroke-width="2.4"/></svg>',
    "done": '<svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><rect x="3" y="3" width="10" height="10" fill="currentColor"/></svg>',
    "failed": '<svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M4 4l8 8M12 4l-8 8" stroke="currentColor" stroke-width="2.4"/></svg>',
}


def stato_html(p, lang):
    """Badge di stato: icona + testo + colore, mai giorni negativi (R-021)."""
    c = p["_"]
    k = c["stato"]
    if k in ("open", "reached"):
        n = c["giorni"]
        chiave = k if n > 1 else f"{k}_{n}"
        testo = fmt(t(lang, f"status.{chiave}"), lang, n=str(n), data=time_tag(p["scadenza"], lang))
    else:
        testo = E(t(lang, f"status.{k}"))
    return f'<span class="status status--{k}">{ICONE[k]}<span>{testo}</span></span>'


def org(p, lang):
    return fmt(t(lang, "card.org"), lang, gruppo=E(p["gruppo"]), dip=E(SITO["dipartimenti"][p["dipartimento"]][lang]))


def progress(p):
    w = min(100, p["_"]["perc"])
    return f'<div class="progress" aria-hidden="true"><div class="progress__bar" style="width:{w:.0f}%"></div></div>'


def url_progetto(p):
    return f'progetto-{p["slug"]}.html'


def etichette(p, lang):
    """Tema, anno e, se c'è, programma dell'Ateneo: le pillole in cima a card e pagine di progetto."""
    prog = f'<span class="tag tag--programma">{E(t(lang, "card.programma"))}</span>' if p["programma"] else ""
    return (f'<p class="card__meta"><span class="tag">{E(SITO["categorie"][p["categoria"]][lang])}</span>'
            f'<span class="tag tag--neutro">{E(fmt(t(lang, "card.anno"), lang, anno=p["anno"]))}</span>{prog}</p>')


def card(p, lang, prefix, h="h3", li=True, cls=""):
    c = p["_"]
    attrs = (f'data-slug="{p["slug"]}" data-stato="{c["stato"]}" data-cat="{p["categoria"]}" data-dip="{p["dipartimento"]}" '
             f'data-anno="{p["anno"]}" data-prog="{"si" if p["programma"] else "no"}" data-perc="{c["perc"]:.1f}" '
             f'data-scadenza="{p["scadenza"]}" data-inizio="{p["inizio"]}"')
    if not li:
        return card(p, lang, prefix, h, cls=cls)[len(f"<li {attrs}>"):-len("</li>")]
    return f'''<li {attrs}><article class="card{cls}">
  <div class="card__media"><img src="{prefix}img/progetti/{p["slug"]}.svg" alt="" width="320" height="180" loading="lazy"></div>
  <div class="card__body">
    {etichette(p, lang)}
    <{h} class="card__title"><a href="{url_progetto(p)}">{E(p["titolo"][lang])}</a></{h}>
    <p class="card__org">{org(p, lang)}</p>
    <p>{stato_html(p, lang)}</p>
    {progress(p)}
    <p class="card__figures">{fmt(t(lang, "card.raised"), lang, raccolto=euro(p["raccolto"], lang), obiettivo=euro(p["obiettivo"], lang), perc=perc(c["perc"]))} · {fmt(t(lang, "card.supporters"), lang, n=c["sostenitori"])}</p>
  </div>
</article></li>'''


def ordina_default(ps):
    aperti = sorted([p for p in ps if p["_"]["aperto"]], key=lambda p: p["_"]["scadenza"])
    chiusi = sorted([p for p in ps if not p["_"]["aperto"]], key=lambda p: p["_"]["scadenza"], reverse=True)
    return aperti + chiusi


# ---------------------------------------------------------------- illustrazioni SVG
TEMI = {
    "api": ("#fdf0cf", '<rect x="120" y="70" width="80" height="70" rx="6" fill="#7a4d00"/><rect x="128" y="80" width="64" height="8" fill="#f4b93e"/><rect x="128" y="96" width="64" height="8" fill="#f4b93e"/><rect x="128" y="112" width="64" height="8" fill="#f4b93e"/><circle cx="210" cy="60" r="9" fill="#3b1d2a"/><ellipse cx="206" cy="52" rx="7" ry="4" fill="#fff"/><circle cx="95" cy="55" r="7" fill="#3b1d2a"/><rect x="200" y="125" width="18" height="12" fill="#2f6b4f"/>'),
    "cuore": ("#e3eff2", '<path d="M110 120 h100 v20 h-100z" fill="#1d5b73"/><path d="M115 120 q45 -50 90 0" fill="none" stroke="#1d5b73" stroke-width="6"/><path d="M160 30 l40 14 v28 c0 26 -18 40 -40 48 c-22 -8 -40 -22 -40 -48 v-28z" fill="none" stroke="#8f3a12" stroke-width="5"/>'),
    "fiore": ("#e3f2e6", '<rect x="0" y="140" width="320" height="40" fill="#2f6b4f"/><g fill="#8f3a12"><circle cx="100" cy="95" r="14"/><circle cx="122" cy="95" r="14"/><circle cx="111" cy="77" r="14"/><circle cx="111" cy="113" r="14"/></g><circle cx="111" cy="95" r="9" fill="#f4b93e"/><rect x="108" y="110" width="6" height="32" fill="#24603f"/><circle cx="215" cy="70" r="8" fill="#3b1d2a"/><ellipse cx="210" cy="62" rx="7" ry="4" fill="#fff"/>'),
    "sole": ("#fdf0cf", '<circle cx="110" cy="85" r="34" fill="#f4b93e" stroke="#7a4d00" stroke-width="4"/><g stroke="#7a4d00" stroke-width="5"><line x1="110" y1="30" x2="110" y2="42"/><line x1="110" y1="128" x2="110" y2="140"/><line x1="55" y1="85" x2="67" y2="85"/><line x1="153" y1="85" x2="165" y2="85"/></g><rect x="185" y="55" width="90" height="60" rx="14" fill="#fff" stroke="#8f3a12" stroke-width="4"/><circle cx="215" cy="80" r="4" fill="#3b1d2a"/><circle cx="245" cy="80" r="4" fill="#3b1d2a"/><path d="M215 95 q15 10 30 0" fill="none" stroke="#3b1d2a" stroke-width="3"/>'),
    "aria": ("#e3eff2", '<rect x="70" y="80" width="120" height="70" fill="#8f3a12"/><path d="M60 82 l70 -40 l70 40z" fill="#6e2b0d"/><rect x="115" y="110" width="30" height="40" fill="#fff"/><rect x="205" y="110" width="24" height="18" rx="3" fill="#2f6b4f"/><line x1="217" y1="128" x2="217" y2="150" stroke="#3b1d2a" stroke-width="3"/><g fill="#fff" stroke="#1d5b73" stroke-width="3"><ellipse cx="240" cy="55" rx="30" ry="14"/><ellipse cx="275" cy="80" rx="22" ry="10"/></g>'),
    "chip": ("#fbeadd", '<rect x="90" y="45" width="140" height="90" rx="10" fill="#fff" stroke="#8f3a12" stroke-width="5"/><g stroke-width="6" fill="none"><path d="M110 70 h100" stroke="#2f6b4f"/><path d="M110 90 h100" stroke="#1d5b73"/><path d="M110 110 h100" stroke="#a3271a"/></g><g fill="#f4b93e" stroke="#3b1d2a" stroke-width="2"><circle cx="110" cy="70" r="6"/><circle cx="110" cy="90" r="6"/><circle cx="110" cy="110" r="6"/></g>'),
    "formula": ("#f7e6d8", '<text x="60" y="100" font-family="serif" font-size="40" fill="#3b1d2a">∫ f(x) dx</text><g fill="#8f3a12"><circle cx="230" cy="70" r="7"/><circle cx="250" cy="70" r="7"/><circle cx="230" cy="90" r="7"/><circle cx="250" cy="110" r="7"/><circle cx="270" cy="90" r="7"/></g>'),
    "acqua": ("#e3eff2", '<path d="M0 110 q40 -20 80 0 t80 0 t80 0 t80 0 v70 h-320z" fill="#1d5b73"/><path d="M0 130 q40 -20 80 0 t80 0 t80 0 t80 0" fill="none" stroke="#fff" stroke-width="3"/><g fill="#f4b93e"><circle cx="70" cy="150" r="5"/><circle cx="160" cy="160" r="4"/><circle cx="250" cy="148" r="5"/></g><g fill="#2f6b4f"><ellipse cx="120" cy="60" rx="18" ry="9"/><ellipse cx="200" cy="50" rx="18" ry="9"/></g>'),
    "voce": ("#fbe9e4", '<rect x="140" y="40" width="40" height="70" rx="20" fill="#a3271a"/><path d="M125 95 q35 40 70 0" fill="none" stroke="#3b1d2a" stroke-width="5"/><line x1="160" y1="125" x2="160" y2="145" stroke="#3b1d2a" stroke-width="5"/><g fill="none" stroke="#8f3a12" stroke-width="4"><path d="M210 60 q15 15 0 30"/><path d="M225 50 q25 25 0 50"/><path d="M110 60 q-15 15 0 30"/><path d="M95 50 q-25 25 0 50"/></g>'),
    "provetta": ("#e3f2e6", '<rect x="120" y="30" width="34" height="110" rx="17" fill="#fff" stroke="#3b1d2a" stroke-width="4"/><rect x="124" y="90" width="26" height="46" rx="13" fill="#2f6b4f"/><circle cx="215" cy="90" r="32" fill="none" stroke="#8f3a12" stroke-width="7"/><line x1="238" y1="113" x2="265" y2="140" stroke="#8f3a12" stroke-width="9"/>'),
    "uva": ("#f7e6d8", '<g fill="#8f3a12"><circle cx="120" cy="70" r="14"/><circle cx="148" cy="70" r="14"/><circle cx="134" cy="94" r="14"/><circle cx="106" cy="94" r="14"/><circle cx="162" cy="94" r="14"/><circle cx="120" cy="118" r="14"/><circle cx="148" cy="118" r="14"/><circle cx="134" cy="140" r="14"/></g><path d="M134 56 q10 -20 30 -22" fill="none" stroke="#24603f" stroke-width="5"/><rect x="225" y="40" width="20" height="90" rx="10" fill="#fff" stroke="#3b1d2a" stroke-width="4"/><circle cx="235" cy="135" r="16" fill="#a3271a" stroke="#3b1d2a" stroke-width="4"/><rect x="231" y="80" width="8" height="50" fill="#a3271a"/>'),
    "montagna": ("#e3eff2", '<path d="M20 160 l100 -120 l60 70 l40 -40 l90 90z" fill="#4f443e"/><path d="M120 40 l25 30 l-15 -5 l-10 10 l-10 -10 l-15 5z" fill="#fff"/><path d="M150 70 l10 25 l-12 15 l8 20" fill="none" stroke="#f4b93e" stroke-width="5"/><rect x="225" y="115" width="34" height="26" fill="#a3271a"/><path d="M220 117 l22 -16 l22 16z" fill="#8f3a12"/>'),
    "robot": ("#fbeadd", '<rect x="115" y="55" width="90" height="70" rx="16" fill="#fff" stroke="#8f3a12" stroke-width="5"/><circle cx="142" cy="85" r="9" fill="#3b1d2a"/><circle cx="178" cy="85" r="9" fill="#3b1d2a"/><path d="M142 105 q18 12 36 0" fill="none" stroke="#3b1d2a" stroke-width="4"/><line x1="160" y1="55" x2="160" y2="35" stroke="#8f3a12" stroke-width="4"/><circle cx="160" cy="32" r="6" fill="#f4b93e"/><rect x="125" y="125" width="70" height="25" rx="6" fill="#8f3a12"/>'),
}


def scrivi_svg():
    out = ROOT / "img/progetti"
    out.mkdir(parents=True, exist_ok=True)
    for p in PROGETTI:
        bg, corpo = TEMI[p["immagine"]["tema"]]
        svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 180" width="320" height="180">'
               f'<rect width="320" height="180" fill="{bg}"/>{corpo}</svg>\n')
        (out / f'{p["slug"]}.svg').write_text(svg, encoding="utf-8")


# ---------------------------------------------------------------- impaginazione comune
# Segno del marchio in linea: i colori vengono dal CSS, così si adatta anche al tema scuro.
SEGNO = ('<svg class="{cls}" viewBox="0 0 48 48" width="{w}" height="{w}" aria-hidden="true" focusable="false">'
         '<g class="segno__petali">' + "".join(
             f'<ellipse cx="24" cy="11" rx="7" ry="10" transform="rotate({a} 24 24)"/>' for a in (0, 72, 144, 216, 288))
         + '</g><circle class="segno__cuore" cx="24" cy="24" r="7.5"/></svg>')
ICONA_CERCA = ('<svg class="icon" viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false">'
               '<circle cx="11" cy="11" r="7" fill="none" stroke="currentColor" stroke-width="2.4"/>'
               '<path d="M16.5 16.5L21 21" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/></svg>')
ICONA_FRECCIA = ('<svg class="icon" viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false">'
                 '<path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>')
ICONA_LUNA = ('<svg class="icon" viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false">'
              '<path d="M20 14.5A8.5 8.5 0 0 1 9.5 4a8.5 8.5 0 1 0 10.5 10.5z" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round"/></svg>')
ICONA_SOLE = ('<svg class="icon" viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false">'
              '<circle cx="12" cy="12" r="4.2" fill="none" stroke="currentColor" stroke-width="2.2"/>'
              '<path d="M12 2.5v2.5M12 19v2.5M2.5 12H5M19 12h2.5M5.3 5.3L7 7M17 17l1.7 1.7M5.3 18.7L7 17M17 7l1.7-1.7" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>')
ICONA_SPUNTA = ('<svg class="icon" viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false">'
                '<path d="M5 12.5l4.5 4.5L19 7.5" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>')


def form_cerca(lang, id_, extra_cls=""):
    """Campo di ricerca con pulsante (etichetta nascosta: il pulsante «Cerca» la rende esplicita, D-25)."""
    return f'''<form class="search-form{extra_cls}" role="search" action="cerca.html" method="get">
      <label class="vh" for="{id_}">{E(t(lang, "common.search_label"))}</label>
      {ICONA_CERCA.replace('class="icon"', 'class="icon search-form__icon"')}
      <input id="{id_}" name="q" type="search" placeholder="{E(t(lang, "common.search_placeholder"))}" autocomplete="off">
      <button class="btn" type="submit">{E(t(lang, "common.search_btn"))}</button>
    </form>'''


NAV = ["home", "progetti", "chi-siamo", "come-funziona", "programma", "proponi", "faq", "contatti"]
NAV_URL = {"home": "index.html", "progetti": "progetti.html", "programma": "programma.html", "come-funziona": "come-funziona.html",
           "proponi": "proponi.html", "chi-siamo": "chi-siamo.html", "faq": "faq.html", "contatti": "contatti.html"}


def header(lang, file, nav_corrente, prefix):
    altra = t(lang, "altra_lingua")
    href_altra = f"en/{file}" if lang == "it" else f"../{file}"
    voci = "".join(
        f'<li><a href="{NAV_URL[k]}"{" aria-current=\"page\"" if k == nav_corrente else ""}>{E(t(lang, "nav." + k))}</a></li>'
        for k in NAV)
    return f'''<a class="skip-link" href="#main">{E(t(lang, "common.skip"))}</a>
<header class="site-header">
  <div class="container site-header__bar">
    <a class="brand" href="index.html" aria-label="{E(t(lang, "common.brand_home"))}">
      {SEGNO.format(cls="brand__mark", w=36)}
      <span><span class="brand__name">idea<b>Blume</b></span><span class="brand__tagline">{E(t(lang, "tagline"))}</span></span>
    </a>
    <a class="lang-switch" href="{href_altra}" lang="{altra}" hreflang="{altra}" data-lang-switch><svg class="icon" viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><g fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.6 2.8 3.8 5.8 3.8 9s-1.2 6.2-3.8 9c-2.6-2.8-3.8-5.8-3.8-9S9.4 5.8 12 3z"/></g></svg><span class="lang-switch__long">{E(t(lang, "common.lang_switch"))}</span><span class="lang-switch__short" aria-hidden="true">{altra.upper()}</span><span class="vh"> – {E(t(lang, "common.lang_switch_label"))}</span></a>
    <button class="theme-toggle js-only" type="button" data-tema-toggle>
      <span class="theme-toggle__verso theme-toggle__verso--scuro">{ICONA_LUNA}<span class="vh">{E(t(lang, "common.theme_to"))} </span><span class="theme-toggle__testo">{E(t(lang, "common.theme_dark"))}</span></span>
      <span class="theme-toggle__verso theme-toggle__verso--chiaro">{ICONA_SOLE}<span class="vh">{E(t(lang, "common.theme_to"))} </span><span class="theme-toggle__testo">{E(t(lang, "common.theme_light"))}</span></span>
    </button>
    <button class="btn btn--secondary nav-toggle js-only" type="button" aria-expanded="false" aria-controls="menu-principale" data-nav-toggle>
      <svg width="20" height="20" viewBox="0 0 20 20" aria-hidden="true" focusable="false"><path d="M2 5h16M2 10h16M2 15h16" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/></svg>
      <span data-nav-label>{E(t(lang, "common.menu"))}</span>
    </button>
  </div>
  <nav class="main-nav container" id="menu-principale" aria-label="{E(t(lang, "common.menu_label"))}">
    <ul class="main-nav__list">{voci}</ul>
  </nav>
</header>'''


def footer(lang, prefix):
    c = SITO["contatti"]
    f = lambda k: E(t(lang, "footer." + k))
    n = lambda k: E(t(lang, "nav." + k))
    return f'''<footer class="site-footer">
  <div class="container">
    <p class="site-footer__brand">{SEGNO.format(cls="brand__mark", w=40)}<span><span class="brand__name">idea<b>Blume</b></span><span class="brand__tagline">{E(t(lang, "tagline"))}</span></span></p>
    <div class="site-footer__cols">
      <section aria-labelledby="ft-aiuto">
        <h2 id="ft-aiuto">{f("help_title")}</h2>
        <p>{f("phone")}: <a href="tel:{c["telefono"].replace(" ", "")}">{c["telefono_visibile"]}</a><br>{E(c["orari_brevi"][lang])}<br>
        {f("email")}: <a href="mailto:{c["email_aiuto"]}">{c["email_aiuto"]}</a><br></p>
        <a class="btn" href="contatti.html#scrivici">{f("write")}</a>
      </section>
      <nav aria-labelledby="ft-esplora"><h2 id="ft-esplora">{f("explore")}</h2><ul>
        <li><a href="progetti.html">{n("progetti")}</a></li><li><a href="programma.html">{n("programma")}</a></li>
        <li><a href="come-funziona.html">{n("come-funziona")}</a></li><li><a href="faq.html">{n("faq")}</a></li></ul></nav>
      <nav aria-labelledby="ft-promotori"><h2 id="ft-promotori">{f("promoters")}</h2><ul>
        <li><a href="proponi.html">{n("proponi")}</a></li><li><a href="candidatura.html">{f("candidatura")}</a></li>
        <li><a href="collabora.html">{f("collabora")}</a></li></ul></nav>
      <nav aria-labelledby="ft-info"><h2 id="ft-info">{f("info")}</h2><ul>
        <li><a href="chi-siamo.html">{n("chi-siamo")}</a></li><li><a href="contatti.html">{n("contatti")}</a></li></ul></nav>
    </div>
    <p class="site-footer__note">{t(lang, "footer.note")}</p>
  </div>
</footer>'''


def breadcrumb(lang, voci):
    if not voci:
        return ""
    items = [f'<li><a href="index.html">{E(t(lang, "common.home"))}</a></li>']
    for label, url in voci[:-1]:
        items.append(f'<li><a href="{url}">{E(label)}</a></li>')
    items.append(f'<li><span aria-current="page">{E(voci[-1][0])}</span></li>')
    return f'<nav class="breadcrumb container" aria-label="{E(t(lang, "common.breadcrumb_label"))}"><ol>{"".join(items)}</ol></nav>'


def pagina(lang, file, titolo, corpo, nav=None, briciole=None, dati=False, extra_head="", main_class="container", attesa=False):
    prefix = "" if lang == "it" else "../"
    # Pagine costruite dallo script: contenuto invisibile (non assente) finché è pronto, per non spostare il layout (CLS).
    # Rete di sicurezza: se lo script non parte, il contenuto compare comunque dopo 2,5 s.
    ATTESA = (' setTimeout(function () { var m = document.querySelector("[data-attesa]"); if (m) m.removeAttribute("data-attesa"); }, 2500);'
              if attesa else "")
    script_dati = f'<script src="{prefix}data/testi-{lang}.js"></script>\n' + (f'<script src="{prefix}data/ib-dati.js"></script>\n' if dati else "")
    return f'''<!doctype html>
<html lang="{lang}" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(titolo)}</title>
<meta name="description" content="{E(t(lang, "tagline"))}">
<meta name="theme-color" content="#fbf6ee">
<link rel="icon" href="{prefix}img/ideablume-segno.svg" type="image/svg+xml">
<link rel="stylesheet" href="{prefix}css/ideablume.css">
<script>document.documentElement.className = "js";{TEMA_JS}{font_js(prefix)}{ATTESA}</script>
<noscript><link rel="stylesheet" href="{prefix}css/font.css"></noscript>
{extra_head}</head>
<body data-pagina="{file[:-5]}" data-oggi-build="{OGGI.isoformat()}">
{header(lang, file, nav, prefix)}
{breadcrumb(lang, briciole or [])}
<main id="main" class="{main_class}" tabindex="-1"{' data-attesa' if attesa else ''}>
{corpo}
</main>
{footer(lang, prefix)}
{script_dati}<script src="{prefix}js/ideablume.js"></script>
</body>
</html>
'''


# Applica il tema prima del primo disegno: scuro solo se scelto da chi visita, altrimenti chiaro.
TEMA_JS = (' (function () { var s = null; try { s = localStorage.getItem("ib-tema"); } catch (e) {}'
           ' document.documentElement.setAttribute("data-theme", s === "dark" ? "dark" : "light"); })();')


def font_js(prefix):
    """Sceglie il foglio dei font: da file:// i browser bloccano i file di font, quindi si usa la versione
    con i font incorporati; su un server si usano i file .woff2, precaricati."""
    locali = f'<link rel="stylesheet" href="{prefix}css/font-locali.css">'
    # Su un server le @font-face vanno in linea (stesso contenuto di css/font.css): nessuna richiesta bloccante in più.
    regole = re.sub(r"/\*.*?\*/", "", (ROOT / "css/font.css").read_text(encoding="utf-8"), flags=re.S)
    regole = re.sub(r"\s+", " ", regole.replace("../fonts/", f"{prefix}fonts/")).strip()
    server = (f'<link rel="preload" href="{prefix}fonts/inter.woff2" as="font" type="font/woff2" crossorigin>'
              f'<link rel="preload" href="{prefix}fonts/bricolage-grotesque.woff2" as="font" type="font/woff2" crossorigin>'
              f'<style>{regole}</style>')
    return f' document.write(location.protocol === "file:" ? \'{locali}\' : \'{server}\');'


def scrivi_font_locali():
    """css/font-locali.css: le stesse @font-face di css/font.css con i font incorporati (data URI)."""
    css = (ROOT / "css/font.css").read_text(encoding="utf-8")

    def incorpora(m):
        dati = base64.b64encode((ROOT / "css" / m.group(1)).read_bytes()).decode("ascii")
        return f'url("data:font/woff2;base64,{dati}")'
    css = re.sub(r'url\("(\.\./fonts/[^"]+\.woff2)"\)', incorpora, css)
    css = "/* Generato da tools/build.py a partire da css/font.css: non modificare a mano. Usato solo da file://. */\n" + css
    (ROOT / "css/font-locali.css").write_text(css, encoding="utf-8")


def indice_pagina(lang, voci, attr=""):
    """Riquadro «In questa pagina»: voci è un elenco di coppie (id della sezione, titolo)."""
    righe = "".join(f'<li><a href="#{i}">{E(l)}</a></li>' for i, l in voci)
    return f'<nav class="toc" aria-labelledby="h-toc"{attr}><h2 id="h-toc">{E(t(lang, "common.toc"))}</h2><ol>{righe}</ol></nav>'


def torna_su(lang):
    return f'<p><a class="back-to-top" href="#main">↑ {E(t(lang, "common.back_to_top"))}</a></p>'


def lista(items, lang, cls="", **kw):
    return f'<ul{f" class=\"{cls}\"" if cls else ""}>' + "".join(f"<li>{fmt(i, lang, **kw)}</li>" for i in items) + "</ul>"


def costi_box(lang, h="h2", id_="costi"):
    g = lambda k: t(lang, "pages.costi." + k)
    return f'''<section class="infobox" id="{id_}" aria-labelledby="{id_}-t">
  <{h} id="{id_}-t">{E(g("title"))}</{h}>
  <p>{fmt(g("donor"), lang)}</p><p>{fmt(g("promoter"), lang)}</p><p>{fmt(g("partner"), lang)}</p>
</section>'''


# ---------------------------------------------------------------- pagine
def totali_sito():
    """Donato, cofinanziato e sostenitori: gli stessi numeri in home e in «Chi siamo» (P-036)."""
    return (sum(p["raccolto"] for p in PROGETTI if p["_"]["raggiunto"] or p["_"]["aperto"]),
            sum(p["_"]["cofin"] for p in PROGETTI if not p["_"]["aperto"]),
            sum(p["_"]["sostenitori"] for p in PROGETTI))


def pg_home(lang):
    g = lambda k: t(lang, "pages.home." + k)
    aperti = ordina_default([p for p in PROGETTI if p["_"]["aperto"]])
    chiusi = [p for p in PROGETTI if not p["_"]["aperto"]]
    raccolto, cofin, sost = totali_sito()
    aggiornamenti = sorted(((data_da(a["data"]), a, p) for p in PROGETTI for a in p["aggiornamenti"]), key=lambda x: x[0], reverse=True)[:3]
    agg_html = "".join(
        f'<li><article class="update"><h3><a href="{url_progetto(p)}#aggiornamenti">{E(a["titolo"][lang])}</a></h3>'
        f'<p class="muted">{E(p["titolo_breve"][lang])} · {time_tag(a["data"], lang, True)}</p><p>{E(a["testo"][lang])}</p></article></li>'
        for _, a, p in aggiornamenti)
    passi = "".join(f'<li><h3>{E(s["t"])}</h3><p>{fmt(s["d"], lang)}</p></li>' for s in g("how"))
    prefix = "" if lang == "it" else "../"
    # Progetto in evidenza: la campagna non ancora riuscita più vicina alla scadenza.
    urgenti = [p for p in aperti if not p["_"]["raggiunto"]] or aperti
    evidenza = min(urgenti, key=lambda p: p["_"]["giorni"]) if urgenti else None
    anno = max(p["anno"] for p in PROGETTI)
    sep = "." if lang == "it" else ","
    sost_txt = f"{sost:,}".replace(",", sep)
    chips = (f'<ul class="hero__chips">'
             f'<li>{ICONA_SPUNTA}<span><strong>{len(aperti)}</strong> {E(g("chip_open"))}</span></li>'
             f'<li>{ICONA_SPUNTA}<span>{E(fmt(g("chip_min"), lang))}</span></li>'
             f'<li>{ICONA_SPUNTA}<span>{E(g("chip_noreg"))}</span></li></ul>')
    feature = (f'<div class="hero__feature"><p class="hero__feature-label" id="h-evidenza">{E(g("chip_label"))}</p>'
               f'{card(evidenza, lang, prefix, "h2", li=False, cls=" card--feature")}'
               f'<p class="hero__badge" aria-hidden="true"><strong>{sost_txt}</strong> {E(g("chip_supp"))}</p></div>') if evidenza else ""
    corpo = f'''<section class="hero" aria-labelledby="titolo-pagina">
  <div class="container hero__grid">
    <div class="hero__text">
      <p class="eyebrow">{E(fmt(g("eyebrow"), lang, anno=anno))}</p>
      <h1 id="titolo-pagina">{E(g("h1"))}</h1>
      <p class="lead">{fmt(g("intro"), lang)}</p>
      {form_cerca(lang, "q-home", " search-form--hero")}
      <p class="btn-row"><a class="btn btn--cta btn--large" href="progetti.html?stato=in-corso">{E(g("cta"))} {ICONA_FRECCIA}</a>
        <a class="btn btn--secondary btn--large" href="come-funziona.html">{E(t(lang, "nav.come-funziona"))}</a></p>
      {chips}
    </div>
    {feature}
  </div>
</section>
<section class="section" aria-labelledby="h-aperti">
  <div class="container">
    <div class="section__head">
      <h2 id="h-aperti">{E(g("open_title"))} <span class="count-pill">{len(aperti)}</span></h2>
      <p><a class="link-arrow" href="progetti.html">{E(g("all_link"))} ({len(PROGETTI)}) {ICONA_FRECCIA}</a></p>
    </div>
    <ul class="grid grid--3">{"".join(card(p, lang, prefix) for p in aperti)}</ul>
  </div>
</section>
<section class="section section--tinted" aria-labelledby="h-come">
  <div class="container">
    <div class="section__head">
      <h2 id="h-come">{E(g("how_title"))}</h2>
      <p><a class="link-arrow" href="come-funziona.html">{E(g("how_more"))} {ICONA_FRECCIA}</a></p>
    </div>
    <ol class="howto howto--cards">{passi}</ol>
  </div>
</section>
<section class="section band" aria-labelledby="h-numeri">
  <div class="container">
    <h2 id="h-numeri">{E(g("numbers_title"))}</h2>
    <ul class="figures">
      <li><strong>{len(aperti)}</strong> {E(g("n_open"))}</li>
      <li><strong>{len(chiusi)}</strong> {E(g("n_closed"))}</li>
      <li><strong>{euro(raccolto, lang)}</strong> {E(g("n_raised"))}</li>
      <li><strong>{euro(cofin, lang)}</strong> {E(g("n_cofin"))}</li>
    </ul>
    <p class="small band__note">{fmt(g("numbers_note"), lang, data=fmt_data(OGGI, lang, True))} {sost} {E(g("n_supporters"))}.</p>
  </div>
</section>
<section class="section" aria-labelledby="h-agg">
  <div class="container">
    <h2 id="h-agg">{E(g("updates_title"))}</h2>
    <ul class="grid grid--3">{agg_html}</ul>
  </div>
</section>
<div class="container">
  <section class="promo" aria-labelledby="h-promo">
    <h2 id="h-promo">{E(g("promo_title"))}</h2>
    <p>{E(g("promo_text"))}</p>
    <p><a class="btn btn--light btn--large" href="proponi.html">{E(g("promo_cta"))} {ICONA_FRECCIA}</a></p>
  </section>
</div>'''
    return pagina(lang, "index.html", g("title"), corpo, nav="home", dati=False, main_class="")


def opzioni(sel_id, label, opts, tutti):
    o = f'<option value="">{E(tutti)}</option>' + "".join(f'<option value="{v}">{E(l)}</option>' for v, l in opts)
    return f'<div class="field"><label for="f-{sel_id}">{E(label)}</label><select id="f-{sel_id}" name="{sel_id}">{o}</select></div>'


def pg_progetti(lang):
    g = lambda k: t(lang, "pages.progetti." + k)
    prefix = "" if lang == "it" else "../"
    aperti = sum(1 for p in PROGETTI if p["_"]["aperto"])
    cats = sorted({p["categoria"] for p in PROGETTI}, key=lambda k: SITO["categorie"][k][lang])
    dips = sorted({p["dipartimento"] for p in PROGETTI}, key=lambda k: SITO["dipartimenti"][k][lang])
    anni = sorted({p["anno"] for p in PROGETTI}, reverse=True)
    ordina = f'''<div class="field"><label for="f-ordina">{E(g("f_ordina"))}</label><select id="f-ordina" name="ordina">
      <option value="">{E(g("o_scadenza"))}</option><option value="recenti">{E(g("o_recenti"))}</option>
      <option value="bisogno">{E(g("o_bisogno"))}</option><option value="percentuale">{E(g("o_percentuale"))}</option></select></div>'''
    corpo = f'''<h1>{E(g("h1"))}</h1>
<div data-didascalia>
  <p><strong>{fmt(g("counts"), lang, open=aperti, closed=len(PROGETTI) - aperti)}</strong></p>
</div>
<form class="filters" action="progetti.html" method="get" aria-labelledby="h-filtri" data-filtri>
  <h2 id="h-filtri" class="vh">{E(g("filters_title"))}</h2>
  <div class="field filters__search"><label for="f-q">{E(t(lang, "common.search_label"))}</label>
    <input id="f-q" name="q" type="search" placeholder="{E(t(lang, "common.search_placeholder"))}" autocomplete="off"></div>
  <div class="filters__grid">
    {opzioni("stato", g("f_stato"), [("in-corso", g("f_stato_open")), ("raggiunto", g("f_stato_reached")), ("conclusi", g("f_stato_closed"))], g("f_stato_all"))}
    {opzioni("categoria", g("f_cat"), [(k, SITO["categorie"][k][lang]) for k in cats], g("f_cat_all"))}
    {opzioni("dip", g("f_dip"), [(k, SITO["dipartimenti"][k][lang]) for k in dips], g("f_dip_all"))}
    {opzioni("anno", g("f_anno"), [(str(a), str(a)) for a in anni], g("f_anno_all"))}
    {opzioni("programma", g("f_prog"), [("si", g("f_prog_si"))], g("f_prog_all"))}
    {ordina}
  </div>
  <p class="btn-row" style="margin-top:1rem"><button class="btn no-js-only" type="submit">{E(g("apply"))}</button>
  <a class="btn btn--ghost" href="progetti.html" data-reset>{E(g("reset"))}</a></p>
</form>
<noscript><p class="alert alert--info">{E(g("noscript"))}</p></noscript>
<p class="result-count" role="status" aria-live="polite" data-conteggio>{fmt(g("count"), lang, n=len(PROGETTI), tot=len(PROGETTI))}</p>
<ul class="grid grid--3" data-elenco>{"".join(card(p, lang, prefix, "h2") for p in ordina_default(PROGETTI))}</ul>
<div data-nessuno hidden><p class="alert alert--warning"><strong>{E(g("none"))}</strong> {fmt(g("none_hint"), lang)}</p></div>
<br />
<p data-fine>{E(g("end"))}</p>
{torna_su(lang)}'''
    return pagina(lang, "progetti.html", g("title"), corpo, nav="progetti", briciole=[(g("h1"), "")], dati=True)


def pg_cerca(lang):
    g = lambda k: t(lang, "pages.cerca." + k)
    cats = "".join(f'<li><a href="progetti.html?categoria={k}">{E(v[lang])}</a></li>' for k, v in SITO["categorie"].items() if any(p["categoria"] == k for p in PROGETTI))
    corpo = f'''<h1>{E(g("h1"))}</h1>
<p>{E(g("intro"))}</p>
{form_cerca(lang, "q-cerca", " search-form--page")}
<noscript><p class="alert alert--info">{fmt(g("noscript"), lang)}</p></noscript>
<h2 class="result-count" role="status" aria-live="polite" data-risultati-titolo>{E(g("empty"))}</h2>
<ul class="grid grid--3" data-risultati></ul>
<div data-nessun-risultato hidden>
  <h3>{E(g("tips_title"))}</h3>
  {lista(g("tips"), lang)}
  <p>{E(g("browse"))}</p><ul class="inline-list">{cats}</ul>
  <p class="btn-row"><a class="btn btn--secondary" href="progetti.html">{E(g("all"))}</a><a class="btn btn--ghost" href="faq.html">{E(g("faq"))}</a></p>
</div>
<section data-pagine-sito hidden aria-labelledby="h-pagine"><h2 id="h-pagine" data-pagine-titolo></h2><ul data-pagine-elenco></ul></section>'''
    return pagina(lang, "cerca.html", g("title"), corpo, nav=None, attesa=True, briciole=[(g("h1"), "")], dati=True)


def nomi_sostenitori(p, n=8):
    pool = SITO["nomi_sostenitori"]
    h = int(hashlib.md5(p["slug"].encode()).hexdigest(), 16)
    return [pool[(h + i * 7) % len(pool)] for i in range(min(n, p["_"]["sostenitori"]))]


def pg_progetto(p, lang):
    g = lambda k: t(lang, "pages.progetto." + k)
    c = p["_"]
    prefix = "" if lang == "it" else "../"
    file = url_progetto(p)
    resp = p["team"][0]
    resp_titolo, _, resp_ruolo = resp["ruolo"][lang].partition(", ")  # «Responsabile scientifica», «professoressa associata di…»
    e = lambda x: euro(x, lang)
    # --- riquadro di stato
    righe = [f'<dt>{E(g("supporters"))}</dt><dd>{c["sostenitori"]}</dd>',
             f'<dt>{E(g("start"))}</dt><dd>{time_tag(p["inizio"], lang)}</dd>',
             f'<dt>{E(g("deadline") if c["aperto"] else g("closed_on"))}</dt><dd>{time_tag(p["scadenza"], lang)}</dd>']
    mancano = f'<p>{fmt(g("missing"), lang, x=e(p["obiettivo"] - p["raccolto"]))}</p>' if not c["raggiunto"] else ""
    if c["aperto"]:
        azione = f'<p><a class="btn btn--cta btn--block" href="donazione.html?progetto={p["slug"]}">{E(g("support"))}</a></p>'
    else:
        azione = (f'<div class="alert alert--info"><h2>{fmt(g("closed_title"), lang, data=time_tag(p["scadenza"], lang))}</h2>'
                  f'<p>{E(p["esito"][lang])}</p></div>'
                  f'<p class="btn-row"><a class="btn" href="#aggiornamenti">{E(g("read_results"))}</a>'
                  f'<a class="btn btn--secondary" href="progetti.html?stato=in-corso">{E(g("see_open"))}</a></p>')
    # --- riquadro obiettivo e raddoppio (unico punto in cui sono spiegate le soglie, R-034)
    so = p.get("secondo_obiettivo")
    seconda = ""
    if so:
        if c["aperto"]:
            seconda = f'<p>{fmt(g("match_second"), lang, importo=e(so["importo"]), scopo=E(so["scopo"][lang]), obiettivo=e(p["obiettivo"]))}</p>'
        elif p["raccolto"] >= so["importo"]:
            seconda = f'<p>{fmt(g("match_second_done"), lang, importo=e(so["importo"]), scopo=E(so["scopo"][lang]))}</p>'
    if p["programma"]:
        cof = min(p["obiettivo"], SITO["regole"]["tetto_cofinanziamento"])
        if c["stato"] == "open":
            testo = f'<p>{fmt(g("match_open"), lang, obiettivo=e(p["obiettivo"]), cofin=e(cof), totale=e(p["obiettivo"] + cof))}</p><p>{E(g("match_example"))}</p>'
        elif c["stato"] == "reached":
            testo = f'<p>{fmt(g("match_reached"), lang, obiettivo=e(p["obiettivo"]), cofin=e(cof))}</p>'
        elif c["stato"] == "done":
            testo = f'<p>{fmt(g("match_done"), lang, cofin=e(c["cofin"]), totale=e(c["totale"]))}</p>'
        else:
            testo = f'<p>{E(g("match_failed"))}</p>'
        testo += f'<p><a class="link-blocco" href="programma.html#raddoppio">{E(g("match_more"))}</a></p>'
        box_t = g("match_title")
    else:
        testo = f'<p>{fmt(g("not_program"), lang)}</p>'
        box_t = g("not_program_title")
    regola = f'''<div class="toggletip" data-toggletip>
      <button class="toggletip__btn" type="button" aria-expanded="false" aria-controls="tt-regola">{E(g("rule_btn"))}</button>
      <div class="toggletip__panel" id="tt-regola" data-toggletip-panel><p>{fmt(g("rule_text"), lang)}</p></div>
    </div>'''
    contatto = f'{p["slug"]}@ideablume.it'
    form_scrivi = f'''<div id="scrivi" data-scrivi hidden>
      <form class="stack" novalidate data-form="scrivi" data-giorni="{SITO["contatti"]["risposta_gruppi_giorni"]}">
        <h2>{E(fmt(g("form_title"), lang, gruppo=p["gruppo"]))}</h2>
        <p class="small">{fmt(g("form_intro"), lang, email=f'<a href="mailto:{contatto}">{contatto}</a>')}</p>
        <div class="field"><label for="sc-nome">{E(g("form_name"))}</label><input id="sc-nome" name="nome" type="text" autocomplete="name" required data-err="err_required"></div>
        <div class="field"><label for="sc-email">{E(g("form_email"))}</label><span class="hint" id="sc-email-h">{E(g("form_email_hint"))}</span>
          <input id="sc-email" name="email" type="email" autocomplete="email" inputmode="email" required aria-describedby="sc-email-h"></div>
        <div class="field"><label for="sc-msg">{E(g("form_msg"))}</label><textarea id="sc-msg" name="messaggio" required data-err="err_required" rows="5"></textarea></div>
        <p class="btn-row"><button class="btn" type="submit" data-label-invio="{E(g("form_sending"))}">{E(g("form_send"))}</button>
        <button class="btn btn--ghost" type="button" data-scrivi-annulla>{E(g("form_cancel"))}</button></p>
      </form>
      <div class="alert alert--success" role="status" data-scrivi-ok hidden></div>
    </div>'''
    aside = f'''<aside class="layout-aside__aside stack" aria-labelledby="h-stato">
  <section class="statusbox" aria-labelledby="h-stato">
    <h2 id="h-stato" class="vh">{E(g("status_title"))}</h2>
    <p>{stato_html(p, lang)}</p>
    <p class="statusbox__amount">{e(p["raccolto"])} <span class="small" style="font-weight:400">{E(g("raised"))}</span></p>
    <p class="statusbox__goal">{E(fmt(g("goal"), lang, obiettivo=e(p["obiettivo"])))} · <strong>{E(fmt(g("perc"), lang, perc=perc(c["perc"])))}</strong></p>
    {progress(p).replace('class="progress"', 'class="progress progress--big"')}
    {mancano}
    <dl>{"".join(righe)}</dl>
    {azione}
  </section>
  <section class="infobox" aria-labelledby="h-raddoppio">
    <h2 id="h-raddoppio">{E(box_t)}</h2>
    {testo}{seconda}
    {regola}
  </section>
  <p class="btn-row">
    <button class="btn btn--secondary btn--small js-only" type="button" data-copia data-ok="{E(g("copied"))}" data-ko="{E(g("copy_fail"))}">{E(g("copy"))}</button>
    {'<button class="btn btn--secondary btn--small js-only" type="button" aria-expanded="false" aria-controls="scrivi" data-scrivi-apri>' + E(g("write")) + '</button>' if c["aperto"] else ""}
  </p>
  <p class="small" role="status" data-copia-esito></p>
  <p class="small">{E(g("group_email"))} <a href="mailto:{contatto}">{contatto}</a></p>
  {form_scrivi if c["aperto"] else ""}
</aside>'''
    # --- sezioni in ordine fisso (R-032)
    sezioni = [("presentazione", g("s_presentazione")), ("fondi", g("s_fondi")), ("team", g("s_team")),
               ("ricompense", g("s_ricompense")), ("aggiornamenti", f'{g("s_aggiornamenti")} ({len(p["aggiornamenti"])})'),
               ("commenti", f'{g("s_commenti")} ({len(p["commenti"])})'), ("sostenitori", f'{g("s_sostenitori")} ({c["sostenitori"]})')]
    indice = "".join(f'<li><a href="#{i}">{E(l)}</a></li>' for i, l in sezioni)
    fondi = "".join(f'<tr><td>{E(f["voce"][lang])}</td><td class="num">{e(f["importo"])}</td></tr>' for f in p["fondi"])
    fondi_second = f'<p>{fmt(g("fondi_second"), lang, scopo=E(so["scopo"][lang]))}</p>' if so else ""
    team = "".join(f'<li><strong>{E(m["nome"])}</strong><span class="vh"> · </span>{E(m["ruolo"][lang])}</li>' for m in p["team"])
    # ricompense
    rr = []
    if c["aperto"]:
        rr.append(f'''<li class="reward reward--free"><span class="reward__price">{E(fmt(g("from"), lang, importo=e(SITO["regole"]["minimo_libero"])))}</span>
          <span><span class="reward__title">{E(g("free_title"))}</span><span class="reward__facts">{fmt(g("free_desc"), lang)}</span></span>
          <a class="btn btn--secondary btn--small" href="donazione.html?progetto={p["slug"]}&amp;ricompensa=libera">{E(g("free_btn"))}<span class="vh"> ({E(fmt(g("from"), lang, importo=e(SITO["regole"]["minimo_libero"])))})</span></a></li>''')
    for r in sorted(p["ricompense"], key=lambda r: r["importo"]):
        sc = r["scelte"]
        scelte = g("chosen_0") if sc == 0 else g("chosen_1") if sc == 1 else fmt(g("chosen_n"), lang, n=sc)
        if r["posti"]:
            rest = r["posti"] - sc
            posti = fmt(g("seats"), lang, r=rest, tot=r["posti"]) if rest > 0 else g("sold_out")
        else:
            rest, posti = 1, g("seats_unl")
        btn = ""
        if c["aperto"] and rest > 0:
            btn = (f'<a class="btn btn--secondary btn--small" href="donazione.html?progetto={p["slug"]}&amp;ricompensa={r["id"]}">'
                   f'{E(fmt(g("choose"), lang, importo=e(r["importo"])))}<span class="vh">: {E(r["titolo"][lang])}</span></a>')
        rr.append(f'''<li class="reward"><span class="reward__price">{e(r["importo"])}</span>
          <span><span class="reward__title">{E(r["titolo"][lang])}</span><span class="reward__desc">{E(r["descrizione"][lang])}</span>
          <span class="reward__facts">{E(scelte)} · {E(posti)}</span></span>{btn}</li>''')
    ric_intro = (f'<p>{E(g("rewards_intro"))}</p>' if c["aperto"]
                 else f'<h3>{E(g("rewards_closed_title"))}</h3><p>{E(g("rewards_closed"))}</p>')
    agg = "".join(f'<li><article class="update"><h3>{E(a["titolo"][lang])}</h3><p class="muted">{time_tag(a["data"], lang, True)}</p><p>{E(a["testo"][lang])}</p></article></li>'
                  for a in sorted(p["aggiornamenti"], key=lambda a: data_da(a["data"]), reverse=True)) or f'<li>{E(g("updates_none"))}</li>'
    lingue = t(lang, "nomi_lingue")
    com = "".join(
        f'<li class="comment"><p class="muted small"><strong>{E(cm["autore"])}</strong> · {time_tag(cm["data"], lang, True)}'
        f'{" · " + E(fmt(g("comment_lang"), lang, lingua=lingue[cm["lingua"]])) if cm["lingua"] != lang else ""}</p>'
        f'<p lang="{cm["lingua"]}">{E(cm["testo"])}</p></li>' for cm in sorted(p["commenti"], key=lambda x: data_da(x["data"]), reverse=True))
    nomi = nomi_sostenitori(p)
    altri = c["sostenitori"] - len(nomi)
    corpo = f'''<div class="layout-aside">
<div class="proj-head">
  {etichette(p, lang)}
  <h1>{E(p["titolo"][lang])}</h1>
  <p class="lead">{E(p["sottotitolo"][lang])}</p>
  <dl class="proj-info">
    <dt>{E(g("info_group"))}</dt><dd><strong>{E(p["gruppo"])}</strong></dd>
    <dt>{E(g("info_place"))}</dt><dd>{fmt(g("info_place_value"), lang, dip=E(SITO["dipartimenti"][p["dipartimento"]][lang]))}</dd>
    <dt>{E(resp_titolo)}</dt><dd><strong>{E(resp["nome"])}</strong>{", " + E(resp_ruolo) if resp_ruolo else ""}</dd>
  </dl>
</div>
{aside}
<div class="proj-body">
  <figure class="proj-figure"><img src="{prefix}img/progetti/{p["slug"]}.svg" alt="{E(p["immagine"]["alt"][lang])}" width="640" height="360"></figure>
  <nav class="toc" aria-labelledby="h-indice"><h2 id="h-indice">{E(t(lang, "common.toc"))}</h2><ol>{indice}</ol></nav>
  <section id="presentazione" aria-labelledby="h-presentazione"><h2 id="h-presentazione">{E(g("s_presentazione"))}</h2>
    {"".join(f'<h3>{E(s["t"])}</h3>' + "".join(f"<p>{E(x)}</p>" for x in s["p"]) for s in p["presentazione"][lang])}</section>
  <section id="fondi" aria-labelledby="h-fondi"><h2 id="h-fondi">{E(g("s_fondi"))}</h2>
    <div class="table-wrap"><table><caption>{E(g("fondi_caption"))}</caption>
      <thead><tr><th scope="col">{E(g("fondi_voce"))}</th><th scope="col" class="num">{E(g("fondi_importo"))}</th></tr></thead>
      <tbody>{fondi}</tbody><tfoot><tr><th scope="row">{E(g("fondi_totale"))}</th><td class="num">{e(p["obiettivo"])}</td></tr></tfoot></table></div>
    {fondi_second}</section>
  <section id="team" aria-labelledby="h-team"><h2 id="h-team">{E(g("s_team"))}</h2><ul class="team">{team}</ul></section>
  <section id="ricompense" aria-labelledby="h-ricompense"><h2 id="h-ricompense">{E(g("s_ricompense"))}</h2>{ric_intro}
    <ul class="rewards">{"".join(rr)}</ul></section>
  <section id="aggiornamenti" aria-labelledby="h-aggiornamenti"><h2 id="h-aggiornamenti">{E(sezioni[4][1])}</h2><ul class="plain">{agg}</ul></section>
  <section id="commenti" aria-labelledby="h-commenti"><h2 id="h-commenti">{E(sezioni[5][1])}</h2><p class="small muted">{E(g("comments_note"))}</p><ul class="plain">{com}</ul></section>
  <section id="sostenitori" aria-labelledby="h-sostenitori"><h2 id="h-sostenitori">{E(sezioni[6][1])}</h2>
    <p>{E(g("supporters_intro"))}</p><p>{E(", ".join(nomi))}{" " + E(fmt(g("supporters_more"), lang, n=altri)) if altri > 0 else ""}</p></section>
  {torna_su(lang)}
</div>
</div>'''
    return pagina(lang, file, fmt(g("title"), lang, titolo=E(p["titolo_breve"][lang])), corpo, nav="progetti",
                  briciole=[(t(lang, "nav.progetti"), "progetti.html"), (p["titolo_breve"][lang], "")])


def campo(id_, label, tipo="text", hint=None, opzionale=False, lang="it", attrs="", tag="input"):
    opt = f' <span class="optional">({E(t(lang, "common.optional"))})</span>' if opzionale else ""
    req = "" if opzionale else " required"
    h = f'<span class="hint" id="{id_}-h">{fmt(hint, lang)}</span>' if hint else ""
    desc = f' aria-describedby="{id_}-h"' if hint else ""
    if tag == "textarea":
        ctrl = f'<textarea id="{id_}" name="{id_}"{req}{desc} rows="5" {attrs}></textarea>'
    else:
        ctrl = f'<input id="{id_}" name="{id_}" type="{tipo}"{req}{desc} {attrs}>'
    return f'<div class="field"><label for="{id_}">{E(label)}{opt}</label>{h}{ctrl}</div>'


def select(id_, label, opzioni_, lang, scegli):
    o = f'<option value="">{E(scegli)}</option>' + "".join(f'<option value="{E(v)}">{E(l)}</option>' for v, l in opzioni_)
    return f'<div class="field"><label for="{id_}">{E(label)}</label><select id="{id_}" name="{id_}" required>{o}</select></div>'


def check(id_, label, lang, opzionale=False):
    req = "" if opzionale else " required"
    opt = f' <span class="optional">({E(t(lang, "common.optional"))})</span>' if opzionale else ""
    return f'<div class="field"><label class="choice" for="{id_}"><input id="{id_}" name="{id_}" type="checkbox"{req}><span class="choice__text">{fmt(label, lang)}{opt}</span></label></div>'


def pg_donazione(lang):
    g = lambda k: t(lang, "pages.donazione." + k)
    passi = "".join(f'<li data-passo-ind="{i + 1}">{E(s)}</li>' for i, s in enumerate(g("steps")))
    metodi = "".join(
        f'''<label class="choice" for="m-{m["id"]}"><input id="m-{m["id"]}" type="radio" name="metodo" value="{m["id"]}" required>
        <span class="choice__text">{E(m["nome"][lang])}<small>{E(m["dopo"][lang])}</small><small data-commissione="{m["id"]}"></small></span></label>'''
        for m in SITO["metodi_pagamento"])
    nav = lambda primo=False, ultimo=False: (
        f'<p class="btn-row don-nav">'
        + (f'<a class="btn btn--ghost" href="#" data-torna-progetto>{E(g("back_project"))}</a>' if primo else f'<button class="btn btn--secondary" type="button" data-indietro>← {E(g("back"))}</button>')
        + (f'<button class="btn btn--cta" type="submit" data-paga>{E(g("pay"))}</button>' if ultimo else f'<button class="btn btn--cta" type="submit">{E(g("next"))} →</button>')
        + "</p>")
    corpo = f'''<h1 data-don-titolo>{E(g("h1"))}</h1>
<noscript><p class="alert alert--info">{fmt(g("noscript"), lang)}</p></noscript>
<div data-don-assente hidden><p class="alert alert--info" data-don-assente-testo></p><p class="btn-row" data-don-assente-azioni></p></div>
<div data-don-app hidden>
  <section class="summary" aria-labelledby="h-riepilogo" style="visibility: hidden; display: none;">
    <h2 id="h-riepilogo" class="small" style="margin:0 0 .5rem">{E(g("summary_title"))}</h2>
    <dl><dt>{E(g("sum_project"))}</dt><dd data-sum-progetto></dd>
        <dt>{E(g("sum_reward"))}</dt><dd data-sum-ricompensa></dd>
        <dt>{E(g("sum_amount"))}</dt><dd data-sum-importo></dd></dl>
    <p class="small" style="margin:.5rem 0 0"><a href="#" data-modifica>{E(g("edit"))}</a></p>
  </section>
  <nav aria-label="{E(g("steps_label"))}"><ol class="steps">{passi}</ol></nav>
  <p class="small muted" data-passo-testo aria-live="polite"></p>
  <div class="alert alert--error" role="alert" tabindex="-1" data-errori hidden><h2 data-errori-titolo></h2><ul data-errori-lista></ul></div>
  <form novalidate data-form="donazione">
    <section data-passo="1" aria-labelledby="h-p1">
      <h2 id="h-p1">{E(g("steps")[0])}</h2>
      <fieldset data-gruppo="scelta"><legend>{E(g("s1_legend"))}</legend><div data-scelte></div></fieldset>
      <div class="field" data-campo-importo><label for="importo">{E(g("s1_amount"))}</label><span class="hint" id="importo-h" data-importo-hint></span>
        <div class="input-euro"><span aria-hidden="true">€</span><input id="importo" name="importo" type="text" inputmode="decimal" autocomplete="transaction-amount" required aria-describedby="importo-h"></div></div>
      <div class="infobox"><p>{fmt(g("s1_rule"), lang)}</p><p data-s1-raddoppio></p></div>
      {nav(primo=True)}
    </section>
    <section data-passo="2" aria-labelledby="h-p2" hidden>
      <h2 id="h-p2">{E(g("s2_title"))}</h2>
      <p class="small muted">{E(t(lang, "common.required_note"))}</p>
      {campo("nome", g("s2_name"), lang=lang, attrs='autocomplete="given-name" data-err="err_name"')}
      {campo("cognome", g("s2_surname"), lang=lang, attrs='autocomplete="family-name" data-err="err_surname"')}
      {campo("email", g("s2_email"), "email", g("s2_email_hint"), lang=lang, attrs='autocomplete="email" inputmode="email"')}
      {campo("telefono", g("s2_phone"), "tel", g("s2_phone_hint"), opzionale=True, lang=lang, attrs='autocomplete="tel" inputmode="tel"')}
      <p class="small">{E(g("s2_address_note"))}</p>
      {nav()}
    </section>
    <section data-passo="3" aria-labelledby="h-p3" hidden>
      <h2 id="h-p3">{E(g("s3_title"))}</h2>
      <fieldset data-gruppo="visibilita"><legend>{E(g("s3_legend"))}</legend>
        <label class="choice" for="vis-si"><input id="vis-si" type="radio" name="visibilita" value="si" required><span class="choice__text">{E(g("s3_show"))}<small>{E(g("s3_show_hint"))}</small></span></label>
        <label class="choice" for="vis-no"><input id="vis-no" type="radio" name="visibilita" value="no" required><span class="choice__text">{E(g("s3_anon"))}<small>{E(g("s3_anon_hint"))}</small></span></label>
      </fieldset>
      <p class="infobox">{fmt(g("s3_team"), lang)}</p>
      {check("privacy", g("s3_privacy"), lang)}
      {check("novita", g("s3_news"), lang, opzionale=True)}
      {nav()}
    </section>
    <section data-passo="4" aria-labelledby="h-p4" hidden>
      <h2 id="h-p4">{E(g("steps")[3])}</h2>
      <fieldset data-gruppo="metodo"><legend>{E(g("s4_legend"))}</legend>{metodi}</fieldset>
      <p class="small">{fmt(g("s4_help"), lang)}</p>
      {nav()}
    </section>
    <section data-passo="5" aria-labelledby="h-p5" hidden>
      <h2 id="h-p5">{E(g("s5_title"))}</h2>
      <div class="summary"><dl data-revisione></dl></div>
      <p class="small">{fmt(g("r_fee_note"), lang)}</p>
      <p>{fmt(g("r_refund"), lang)}</p>
      <p class="infobox">{fmt(g("r_receipt"), lang)}</p>
      {nav(ultimo=True)}
    </section>
  </form>
  <p class="small muted">{E(g("saved"))}</p>
</div>'''
    return pagina(lang, "donazione.html", g("title"), corpo, nav="progetti", attesa=True,
                  briciole=[(t(lang, "nav.progetti"), "progetti.html"), (g("h1"), "")], dati=True)


def pg_conferma(lang):
    g = lambda k: t(lang, "pages.conferma." + k)
    corpo = f'''<div data-conferma hidden>
<h1>{E(g("h1"))}</h1>
<p class="alert alert--success"><strong>{E(g("code"))}: <span data-codice></span></strong><br></p>
<div class="summary"><dl data-conferma-riepilogo></dl></div>
<h2>{E(g("next_title"))}</h2>
<ul data-conferma-passi></ul>
<p class="btn-row"><button class="btn btn--secondary" type="button" data-stampa>{E(g("print"))}</button>
<a class="btn btn--ghost" href="#" data-conferma-progetto>{E(g("back"))}</a><a class="btn btn--ghost" href="progetti.html?stato=in-corso">{E(g("more"))}</a></p>
</div>
<div data-conferma-assente><h1>{E(g("h1"))}</h1><p class="alert alert--info">{E(g("missing"))}</p>
<p><a class="btn" href="contatti.html">{E(t(lang, "nav.contatti"))}</a></p></div>'''
    return pagina(lang, "donazione-conferma.html", g("title"), corpo, nav="progetti", attesa=True,
                  briciole=[(t(lang, "nav.progetti"), "progetti.html"), (g("h1"), "")], dati=True)


def pg_programma(lang):
    g = lambda k: t(lang, "pages.programma." + k)
    e = lambda x: euro(x, lang)
    aperti = [p for p in PROGETTI if p["_"]["aperto"] and p["programma"]]
    ultimo = max(aperti, key=lambda p: p["_"]["scadenza"]) if aperti else None
    anno = max(p["anno"] for p in PROGETTI)
    stato_now = fmt(g("status_now"), lang, anno=anno, data=time_tag(ultimo["scadenza"], lang, True) if ultimo else "—")
    fasi = "".join(
        f'<li><h3>{E(f["t"])} <span class="tag">{E(g("phase_now") if i == 3 else g("phase_done"))}</span></h3><p>{fmt(f["d"], lang)}</p></li>'
        for i, f in enumerate(g("phases")))
    anni = sorted({p["anno"] for p in PROGETTI if p["programma"]}, reverse=True)
    righe = ""
    for a in anni:
        ps = [p for p in PROGETTI if p["programma"] and p["anno"] == a]
        righe += (f'<tr><th scope="row"><a href="progetti.html?anno={a}&amp;programma=si">{a}</a></th><td class="num">{len(ps)}</td>'
                  f'<td class="num">{sum(1 for p in ps if p["_"]["raggiunto"])}</td><td class="num">{e(sum(p["raccolto"] for p in ps))}</td>'
                  f'<td class="num">{e(sum(p["_"]["cofin"] for p in ps))}</td><td class="num">{sum(p["_"]["sostenitori"] for p in ps)}</td></tr>')
    toc = [("stato", g("status_title")), ("fasi", g("phases_label")), ("raddoppio", g("match_title")), ("requisiti", g("who_title")),
           ("edizioni", g("editions_title")), ("contatti", g("contact_title"))]
    corpo = f'''<h1>{E(g("h1"))}</h1>
{indice_pagina(lang, toc)}
<section id="stato" class="statusbox" aria-labelledby="h-stato"><h2 id="h-stato">{E(g("status_title"))}</h2>
  <p>{stato_now}</p><p>{fmt(g("status_next"), lang)}</p>
  <p><a class="btn" href="candidatura.html">{E(g("apply_cta"))}</a></p></section>
<section id="fasi" aria-labelledby="h-fasi"><h2 id="h-fasi">{E(g("phases_label"))}</h2><ol class="howto">{fasi}</ol></section>
<section id="raddoppio" aria-labelledby="h-raddoppio"><h2 id="h-raddoppio">{E(g("match_title"))}</h2>{lista(g("match"), lang)}
  <div class="infobox"><h3>{E(g("example_title"))}</h3><p>{E(g("example"))}</p></div></section>
<section id="requisiti" aria-labelledby="h-chi"><h2 id="h-chi">{E(g("who_title"))}</h2><p>{fmt(g("who"), lang)}</p>
  <h3>{E(g("req_title"))}</h3>{lista(g("req"), lang)}

  <h3>{E(g("how_title"))}</h3><p>{fmt(g("how"), lang)}</p>
  <p><a class="btn" href="candidatura.html">{E(g("apply_cta"))}</a></p></section>
<section id="edizioni" aria-labelledby="h-edizioni"><h2 id="h-edizioni">{E(g("editions_title"))}</h2>
  <div class="table-wrap"><table><caption>{E(g("editions_caption"))}</caption>
  <thead><tr><th scope="col">{E(g("e_anno"))}</th><th scope="col" class="num">{E(g("e_progetti"))}</th><th scope="col" class="num">{E(g("e_riusciti"))}</th>
  <th scope="col" class="num">{E(g("e_raccolto"))}</th><th scope="col" class="num">{E(g("e_cofin"))}</th><th scope="col" class="num">{E(g("e_sost"))}</th></tr></thead>
  <tbody>{righe}</tbody></table></div>
  <p class="small muted">{E(g("e_note"))} {E(t(lang, "common.updated"))} {fmt_data(OGGI, lang, True)}.</p></section>
<section id="contatti" aria-labelledby="h-contatti"><h2 id="h-contatti">{E(g("contact_title"))}</h2><p>{fmt(g("contact"), lang)}</p>
  </section>
{torna_su(lang)}'''
    return pagina(lang, "programma.html", g("title"), corpo, nav="programma", briciole=[(t(lang, "nav.programma"), "")])


def passi_howto(items, lang):
    return '<ol class="howto">' + "".join(
        f'<li><h3>{E(s["t"])}</h3><p>{fmt(s["d"], lang)}</p>' + (f'<p><a href="{s["a"]}">{E(s["l"])}</a></p>' if s.get("a") else "") + "</li>" for s in items) + "</ol>"


def pg_come(lang):
    g = lambda k: t(lang, "pages.come." + k)
    ids = ["sostenitori", "promotori", "costi", "dubbi"]
    corpo = f'''<h1>{E(g("h1"))}</h1>
{indice_pagina(lang, zip(ids, g("toc")))}
<section id="sostenitori" aria-labelledby="h-sost"><h2 id="h-sost">{E(g("donor_title"))}</h2>{passi_howto(g("donor"), lang)}</section>
<section id="promotori" aria-labelledby="h-prom"><h2 id="h-prom">{E(g("promoter_title"))}</h2>{passi_howto(g("promoter"), lang)}</section>
{costi_box(lang)}
<section id="dubbi" aria-labelledby="h-dubbi"><h2 id="h-dubbi">{E(g("doubts_title"))}</h2><p>{fmt(g("doubts"), lang)}</p></section>
{torna_su(lang)}'''
    return pagina(lang, "come-funziona.html", g("title"), corpo, nav="come-funziona", briciole=[(t(lang, "nav.come-funziona"), "")])


def pg_proponi(lang):
    g = lambda k: t(lang, "pages.proponi." + k)
    riquadri = lambda chiave, voci: "".join(
        f'<li><section class="statusbox" aria-labelledby="h-{chiave}-{i}"><h3 id="h-{chiave}-{i}">{E(x["t"])}</h3><p>{fmt(x["d"], lang)}</p></section></li>'
        for i, x in enumerate(voci))
    voci = [("chi-puo", g("who_title")), ("ricerca", g("res_path_title")), ("enti", g("ext_path_title")), ("proposta", g("tips_title")),
            ("tempi", g("time_title")), ("gruppi", g("groups_title")), ("dubbi", g("doubts_title"))]
    corpo = f'''<h1>{E(g("h1"))}</h1>
{indice_pagina(lang, voci)}
<section id="chi-puo" aria-labelledby="h-chi"><h2 id="h-chi">{E(g("who_title"))}</h2>
<ul class="grid grid--2 grid--uguale">
  <li><section class="statusbox" aria-labelledby="h-ric"><h3 id="h-ric">{E(g("res_title"))}</h3><p>{E(g("res_text"))}</p>
    <p class="btn-row"><a class="btn" href="candidatura.html">{E(g("res_cta"))}</a></p> <br/><br/></section></li>
  <li><section class="statusbox" aria-labelledby="h-ext"><h3 id="h-ext">{E(g("ext_title"))}</h3><p>{fmt(g("ext_text"), lang)}</p>
    <p class="btn-row"><a class="btn" href="collabora.html">{E(g("ext_cta"))}</a></p></section></li>
</ul></section>
<section id="ricerca" aria-labelledby="h-ricerca"><h2 id="h-ricerca">{E(g("res_path_title"))}</h2><p>{fmt(g("res_path_intro"), lang)}</p>{passi_howto(g("res_path"), lang)}</section>
<section id="enti" aria-labelledby="h-enti"><h2 id="h-enti">{E(g("ext_path_title"))}</h2><p>{fmt(g("ext_path_intro"), lang)}</p>{passi_howto(g("ext_path"), lang)}</section>
<section id="proposta" aria-labelledby="h-proposta"><h2 id="h-proposta">{E(g("tips_title"))}</h2><p>{E(g("tips_intro"))}</p>
<ul class="grid grid--2 grid--uguale">{riquadri("consiglio", g("tips"))}</ul></section>
<section id="tempi" aria-labelledby="h-tempi"><h2 id="h-tempi">{E(g("time_title"))}</h2>{lista(g("time"), lang)}</section>
<section id="gruppi" aria-labelledby="h-gruppi"><h2 id="h-gruppi">{E(g("groups_title"))}</h2><p>{fmt(g("groups_intro"), lang)}</p>
<ul class="grid grid--2 grid--uguale">{riquadri("gruppi", g("groups"))}</ul></section>
<section id="dubbi" aria-labelledby="h-dubbi"><h2 id="h-dubbi">{E(g("doubts_title"))}</h2><p>{fmt(g("doubts"), lang)}</p></section>
{torna_su(lang)}
'''
    return pagina(lang, "proponi.html", g("title"), corpo, nav="proponi", briciole=[(t(lang, "nav.proponi"), "")])


def pg_candidatura(lang):
    g = lambda k: t(lang, "pages.candidatura." + k)
    ruoli = [(r, r) for r in g("f_role_opts")]
    dips = sorted(((k, v[lang]) for k, v in SITO["dipartimenti"].items()), key=lambda x: x[1])
    corpo = f'''<h1>{E(g("h1"))}</h1>
<div class="infobox"><h2>{E(g("before_title"))}</h2>{lista(g("before"), lang)}</div>
<noscript><p class="alert alert--info">{E(t(lang, "common.noscript_generic"))}</p></noscript>
<div class="alert alert--error" role="alert" tabindex="-1" data-errori hidden><h2 data-errori-titolo></h2><ul data-errori-lista></ul></div>
<form novalidate data-form="candidatura" data-salva="ib-candidatura">
  <p class="small muted">{E(t(lang, "common.required_note"))}</p>
  <fieldset><legend class="h3">{E(g("f_person"))}</legend>
    {campo("c-nome", g("f_name"), lang=lang, attrs='autocomplete="name"')}
    {campo("c-email", g("f_email"), "email", g("f_email_hint"), lang=lang, attrs='autocomplete="email" inputmode="email"')}
    {select("c-ruolo", g("f_role"), ruoli, lang, g("f_choose"))}
    {select("c-dip", g("f_dip"), dips, lang, g("f_choose"))}
  </fieldset>
  <fieldset><legend class="h3">{E(g("f_project"))}</legend>
    {campo("c-titolo", g("f_title"), hint=g("f_title_hint"), lang=lang, attrs='maxlength="80" data-conta="80"')}
    {campo("c-obiettivo", g("f_goal"), hint=g("f_goal_hint"), lang=lang, attrs='inputmode="numeric" data-obiettivo')}
    {campo("c-sintesi", g("f_summary"), hint=g("f_summary_hint"), lang=lang, tag="textarea", attrs='data-conta="600"')}
    {campo("c-fondi", g("f_funds"), hint=g("f_funds_hint"), lang=lang, tag="textarea")}
    {campo("c-team", g("f_team"), hint=g("f_team_hint"), lang=lang, tag="textarea")}
  </fieldset>
  {check("c-consenso", g("f_consent"), lang)}
  {check("c-privacy", g("f_privacy"), lang)}
  <p><button class="btn" type="submit">{E(g("f_send"))}</button></p>
</form>
<div data-inviato hidden tabindex="-1"><div class="alert alert--success"><h2>{E(g("sent_title"))}</h2><p data-inviato-testo></p></div>
<h2>{E(g("sent_summary"))}</h2><div class="summary"><dl data-inviato-riepilogo></dl></div>
<p><button class="btn btn--secondary" type="button" data-stampa>{E(t(lang, "common.print"))}</button></p></div>'''
    return pagina(lang, "candidatura.html", g("title"), corpo, nav="proponi",
                  briciole=[(t(lang, "nav.proponi"), "proponi.html"), (g("h1"), "")], dati=True)


def pg_collabora(lang):
    g = lambda k: t(lang, "pages.collabora." + k)
    tipi = [(x, x) for x in g("f_org_types")]
    temi = [(k, v[lang]) for k, v in SITO["categorie"].items()]
    corpo = f'''<h1>{E(g("h1"))}</h1>
<p class="lead">{E(g("intro"))}</p>
<p class="alert alert--success">{g("no_commit")}</p>
<noscript><p class="alert alert--info">{E(t(lang, "common.noscript_generic"))}</p></noscript>
<div class="alert alert--error" role="alert" tabindex="-1" data-errori hidden><h2 data-errori-titolo></h2><ul data-errori-lista></ul></div>
<form novalidate data-form="collabora" data-salva="ib-collabora">
  <p class="small muted">{E(t(lang, "common.required_note"))}</p>
  <fieldset><legend class="h3">{E(g("f_org"))}</legend>
    {campo("k-ente", g("f_org_name"), lang=lang, attrs='autocomplete="organization"')}
    {select("k-tipo", g("f_org_type"), tipi, lang, t(lang, "pages.candidatura.f_choose"))}
    {campo("k-nome", g("f_contact"), lang=lang, attrs='autocomplete="name"')}
    {campo("k-email", g("f_email"), "email", lang=lang, attrs='autocomplete="email" inputmode="email"')}
    {campo("k-telefono", g("f_phone"), "tel", g("f_phone_hint"), opzionale=True, lang=lang, attrs='autocomplete="tel" inputmode="tel"')}
  </fieldset>
  <fieldset><legend class="h3">{E(g("f_idea"))}</legend>
    {campo("k-idea", g("f_idea"), hint=g("f_idea_hint"), lang=lang, tag="textarea", attrs='data-conta="800"')}
    {select("k-tema", g("f_theme"), temi, lang, t(lang, "pages.candidatura.f_choose"))}
    {campo("k-budget", g("f_budget"), hint=g("f_budget_hint"), opzionale=True, lang=lang, attrs='inputmode="numeric"')}
  </fieldset>
  {check("k-privacy", g("f_privacy"), lang)}
  <p><button class="btn" type="submit">{E(g("f_send"))}</button></p>
</form>
<div data-inviato hidden tabindex="-1"><div class="alert alert--success"><h2>{E(g("sent_title"))}</h2><p data-inviato-testo></p><p>{E(g("print_hint"))}</p></div>
<div class="summary"><dl data-inviato-riepilogo></dl></div>
<p><button class="btn btn--secondary" type="button" data-stampa>{E(t(lang, "common.print"))}</button></p></div>'''
    return pagina(lang, "collabora.html", g("title"), corpo, nav="proponi",
                  briciole=[(t(lang, "nav.proponi"), "proponi.html"), (g("h1"), "")], dati=True)


def pg_chi(lang):
    g = lambda k: t(lang, "pages.chi." + k)
    raccolto, cofin, sost = totali_sito()
    tappe = "".join(
        f'<li><h3><span class="storia__anno">{E(x["y"])}</span> {E(x["t"])}</h3><p>{fmt(x["d"], lang, n_progetti=len(PROGETTI), raccolto=euro(raccolto, lang), cofin=euro(cofin, lang), sostenitori=sost)}</p></li>'
        for x in g("story"))
    attivita = "".join(
        f'<li><section class="statusbox" aria-labelledby="h-fare-{i}"><h3 id="h-fare-{i}">{E(x["t"])}</h3><p>{fmt(x["d"], lang)}</p></section></li>'
        for i, x in enumerate(g("what")))
    corpo = f'''<h1>{E(g("h1"))}</h1>
{indice_pagina(lang, [("storia", g("story_title")), ("attivita", g("what_title")), ("soldi", g("money_title")), ("persone", g("people_title")), ("dove", g("contact_title")), ("prossimo", g("next_title"))])}
<section id="storia" aria-labelledby="h-storia"><h2 id="h-storia">{E(g("story_title"))}</h2>
<p>{E(g("story_intro"))}</p>
<ol class="storia">{tappe}</ol></section>
<section id="attivita" aria-labelledby="h-fare"><h2 id="h-fare">{E(g("what_title"))}</h2>
<p>{E(g("what_intro"))}</p>
<ul class="grid grid--2 grid--uguale">{attivita}</ul></section>
<section id="soldi" aria-labelledby="h-soldi"><h2 id="h-soldi">{E(g("money_title"))}</h2>
<p>{fmt(g("money"), lang)}</p><p>{fmt(g("money_no"), lang)}</p></section>
<section id="persone" aria-labelledby="h-persone"><h2 id="h-persone">{E(g("people_title"))}</h2><p>{fmt(g("people"), lang)}</p></section>
<section id="dove" aria-labelledby="h-dove"><h2 id="h-dove">{E(g("contact_title"))}</h2><p>{fmt(g("address"), lang)}<br>{t(lang, "footer.phone")}: {ctx_base(lang)["tel_link"]} · {ctx_base(lang)["email_aiuto_link"]}<br>{fmt(g("hours"), lang)}</p></section>
<section class="infobox" id="prossimo" aria-labelledby="h-prossimo"><h2 id="h-prossimo">{E(g("next_title"))}</h2><p>{E(g("next"))}</p>
<p class="btn-row"><a class="btn" href="progetti.html?stato=in-corso">{E(g("next_projects"))}</a><a class="btn btn--secondary" href="proponi.html">{E(t(lang, "nav.proponi"))}</a></p></section>
{torna_su(lang)}'''
    return pagina(lang, "chi-siamo.html", g("title"), corpo, nav="chi-siamo", briciole=[(t(lang, "nav.chi-siamo"), "")])


def pg_faq(lang):
    g = lambda k: t(lang, "pages.faq." + k)
    blocchi = ""
    for gr in g("groups"):
        argomenti = ""
        for tp in gr["topics"]:
            dom = "".join(
                f'''<details id="{q["id"]}"><summary>{E(q["q"])}</summary><div class="accordion__content">
                <br />
                {"".join(f"<p>{fmt(a, lang)}</p>" for a in q["a"])}
                </div></details>'''
                for q in tp["q"])
            argomenti += f'<h3>{E(tp["t"])}</h3><div class="accordion">{dom}</div>'
        blocchi += f'<section id="{gr["id"]}" aria-labelledby="h-{gr["id"]}" data-faq-gruppo><h2 id="h-{gr["id"]}">{E(gr["t"])}</h2>{argomenti}</section>'
    voci = [(gr["id"], gr["t"]) for gr in g("groups")] + [("non-trovato", g("not_found_title"))]
    corpo = f'''<h1>{E(g("h1"))}</h1>
<div class="field js-only"><label for="faq-cerca">{E(g("search_label"))}</label>
<input id="faq-cerca" type="search" placeholder="{E(g("search_placeholder"))}" aria-describedby="faq-conteggio" data-faq-cerca></div>
<p class="result-count" id="faq-conteggio" role="status" aria-live="polite" data-faq-conteggio></p>
{indice_pagina(lang, voci, " data-faq-indice")}
{blocchi}
<section class="infobox" id="non-trovato" aria-labelledby="h-nf"><h2 id="h-nf">{E(g("not_found_title"))}</h2><p>{fmt(g("not_found"), lang)}</p></section>
<p class="small muted">{E(t(lang, "common.updated"))} {fmt_data(OGGI, lang, True)}</p>
{torna_su(lang)}'''
    return pagina(lang, "faq.html", g("title"), corpo, nav="faq", briciole=[(t(lang, "nav.faq"), "")])


def pg_contatti(lang):
    g = lambda k: t(lang, "pages.contatti." + k)
    sogg = [(s, s) for s in g("f_subjects")]
    corpo = f'''<h1>{E(g("h1"))}</h1>
<div class="grid grid--2" style="list-style:none">
<section class="statusbox" aria-labelledby="h-tel"><h2 id="h-tel">{E(g("phone_title"))}</h2><p>{fmt(g("phone"), lang)}</p></section>
<section class="statusbox" aria-labelledby="h-mail"><h2 id="h-mail">{E(g("email_title"))}</h2>{lista(g("emails"), lang)}<p>{fmt(g("email_time"), lang)}</p></section>
</div>
<h2>{E(g("address_title"))}</h2><p>{fmt(g("address"), lang)}</p>
<section id="scrivici" aria-labelledby="h-scrivici"><h2 id="h-scrivici">{E(g("form_title"))}</h2>
<p>{E(g("form_intro"))}</p>
<div class="alert alert--error" role="alert" tabindex="-1" data-errori hidden><h3 data-errori-titolo></h3><ul data-errori-lista></ul></div>
<form novalidate data-form="contatti" data-giorni="{SITO["contatti"]["risposta_giorni"]}">
  {campo("ct-nome", g("f_name"), lang=lang, attrs='autocomplete="name"')}
  {campo("ct-email", g("f_email"), "email", lang=lang, attrs='autocomplete="email" inputmode="email"')}
  {select("ct-argomento", g("f_subject"), sogg, lang, t(lang, "pages.candidatura.f_choose"))}
  {campo("ct-msg", g("f_msg"), lang=lang, tag="textarea")}
  <p><button class="btn" type="submit" data-label-invio="{E(g("f_sending"))}">{E(g("f_send"))}</button></p>
</form>
<div class="alert alert--success" role="status" tabindex="-1" data-inviato hidden><p data-inviato-testo></p></div>
</section>'''
    return pagina(lang, "contatti.html", g("title"), corpo, nav="contatti", briciole=[(t(lang, "nav.contatti"), "")], dati=True)


def pg_404(lang, radice=False):
    """404 nel modello del sito (R-014). Quella della radice funziona a qualunque profondità su GitHub Pages (D-21)."""
    g = lambda k: t(lang, "pages.404." + k)
    links = list(zip(g("links"), ["index.html", "progetti.html", "faq.html", "contatti.html"]))
    corpo = f'''<h1>{E(g("h1"))}</h1>
<p class="lead">{E(g("text"))}</p>
<p class="small muted" data-indirizzo hidden>{E(g("tried"))} <code data-indirizzo-testo></code></p>
<label for="q-404"><strong>{E(g("search"))}</strong></label>
<form class="search-form search-form--page" role="search" action="cerca.html" method="get">
  {ICONA_CERCA.replace('class="icon"', 'class="icon search-form__icon"')}
  <input id="q-404" name="q" type="search" placeholder="{E(t(lang, "common.search_placeholder"))}">
  <button class="btn" type="submit">{E(t(lang, "common.search_btn"))}</button>
</form>
<h2>{E(g("go"))}</h2>
<ul>{"".join(f'<li><a href="{u}">{E(l)}</a></li>' for l, u in links)}</ul>'''
    head = ""
    if radice:
        # Su GitHub Pages questa pagina può essere servita per /repo/en/qualcosa: fissa la radice e la lingua.
        head = '''<script>
(function () {
  if (!/\\.github\\.io$/.test(location.hostname)) return;   // altrove la pagina è aperta dal suo indirizzo reale
  var p = location.pathname, seg = p.split("/").filter(Boolean), root = "/";
  if (seg.length && seg[0] !== "en" && !/\\.html$/.test(seg[0])) root = "/" + seg[0] + "/";
  if (seg[1] === "anteprime" && seg[2]) root += "anteprime/" + seg[2] + "/";   // anteprima di un branch
  document.write('<base href="' + root + '">');
  var rel = p.indexOf(root) === 0 ? p.slice(root.length) : p;
  if (/^en\\//.test(rel)) location.replace(root + "en/404.html?da=" + encodeURIComponent(p));
})();
</script>
'''
    return pagina(lang, "404.html", g("title"), corpo, nav=None, extra_head=head)


# ---------------------------------------------------------------- dati per JavaScript
def dati_js():
    def prog(p):
        return {k: p[k] for k in ("slug", "programma", "anno", "categoria", "dipartimento", "gruppo", "titolo", "titolo_breve",
                                  "sottotitolo", "obiettivo", "raccolto", "inizio", "scadenza", "libere")} | {
            "secondo_obiettivo": p.get("secondo_obiettivo"),
            "testo": {l: " ".join(s["t"] + " " + " ".join(s["p"]) for s in p["presentazione"][l]) for l in LINGUE},
            "ricompense": [{k: r[k] for k in ("id", "importo", "titolo", "descrizione", "scelte", "posti")} for r in p["ricompense"]],
        }
    pagine = {}
    for l in LINGUE:
        pagine[l] = [
            {"url": "programma.html", "titolo": t(l, "pages.programma.h1"), "testo": " ".join(t(l, "pages.programma.match")) + " funds together cofinanziamento co-funding raddoppio match bando call"},
            {"url": "come-funziona.html", "titolo": t(l, "pages.come.h1"), "testo": " ".join(t(l, "pages.come.toc"))},
            {"url": "proponi.html", "titolo": t(l, "pages.proponi.h1"), "testo": t(l, "pages.proponi.res_text") + " " + t(l, "pages.proponi.ext_text") + " associazione scuola ente association school"},
            {"url": "faq.html", "titolo": t(l, "pages.faq.h1"), "testo": " ".join(q["q"] for gr in t(l, "pages.faq.groups") for tp in gr["topics"] for q in tp["q"])},
            {"url": "chi-siamo.html", "titolo": t(l, "pages.chi.h1"), "testo": t(l, "pages.chi.story_intro") + " " + t(l, "pages.chi.what_intro")},
            {"url": "contatti.html", "titolo": t(l, "pages.contatti.h1"), "testo": "telefono email phone contact contatti orari"},
        ]
    for l in LINGUE:
        testi = {"js": t(l, "js"), "status": t(l, "status"), "card": t(l, "card"), "mesi": t(l, "mesi"),
                 "external": t(l, "common.external"),
                 "don": t(l, "pages.donazione"), "conferma": t(l, "pages.conferma"), "cerca": t(l, "pages.cerca"),
                 "progetti": {k: t(l, "pages.progetti." + k) for k in ("count", "end")}, "faq": {k: t(l, "pages.faq." + k) for k in ("count_n", "count_1", "count_0")},
                 "candidatura": t(l, "pages.candidatura"), "collabora": t(l, "pages.collabora"), "contatti": t(l, "pages.contatti"),
                 "progetto": {k: t(l, "pages.progetto." + k) for k in ("form_sent", "from")}, "ctx": ctx_base(l)}
        (ROOT / f"data/testi-{l}.js").write_text("/* Generato da tools/build.py: non modificare a mano. */\nwindow.IB_TESTI = "
                                               + json.dumps(testi, ensure_ascii=False, separators=(",", ":")) + ";\n", encoding="utf-8")
    out = {"oggi_build": OGGI.isoformat(), "progetti": [prog(p) for p in PROGETTI], "pagine": pagine,
           "sito": {k: SITO[k] for k in ("contatti", "regole", "metodi_pagamento", "categorie", "dipartimenti")}}
    testo = "/* Generato da tools/build.py: non modificare a mano. */\nwindow.IB_DATI = " + json.dumps(out, ensure_ascii=False, separators=(",", ":")) + ";\n"
    (ROOT / "data/ib-dati.js").write_text(testo, encoding="utf-8")


# ---------------------------------------------------------------- avvio
def main():
    scrivi_svg()
    scrivi_font_locali()
    dati_js()
    n = 0
    for lang in LINGUE:
        out = ROOT if lang == "it" else ROOT / "en"
        out.mkdir(exist_ok=True)
        pagine = {
            "index.html": pg_home(lang), "progetti.html": pg_progetti(lang), "cerca.html": pg_cerca(lang),
            "donazione.html": pg_donazione(lang), "donazione-conferma.html": pg_conferma(lang),
            "programma.html": pg_programma(lang), "come-funziona.html": pg_come(lang), "proponi.html": pg_proponi(lang),
            "candidatura.html": pg_candidatura(lang), "collabora.html": pg_collabora(lang), "chi-siamo.html": pg_chi(lang),
            "faq.html": pg_faq(lang), "contatti.html": pg_contatti(lang),
            "404.html": pg_404(lang, radice=(lang == "it")),
        }
        for p in PROGETTI:
            pagine[url_progetto(p)] = pg_progetto(p, lang)
        for nome, contenuto in pagine.items():
            (out / nome).write_text(contenuto, encoding="utf-8")
            n += 1
    (ROOT / ".nojekyll").write_text("", encoding="utf-8")
    print(f"Generate {n} pagine (data di riferimento {OGGI.isoformat()}).")


if __name__ == "__main__":
    try:
        main()
    except ChiaveMancante as exc:
        sys.exit(f"ERRORE: {exc}")
