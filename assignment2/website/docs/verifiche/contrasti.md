# Contrasti del design system

Generato da `tools/contrasto.py` a partire dai token di `css/ideablume.css`, per il tema chiaro e per il tema scuro
(il tema scuro si attiva quando il sistema operativo lo richiede: `prefers-color-scheme: dark`).
Soglie WCAG 2.2: testo normale 4,5:1 (1.4.3); testo grande, componenti dell'interfaccia e indicatori di focus 3:1 (1.4.11).

## Tema chiaro

| Primo piano | Sfondo | Tipo | Soglia | Rapporto | Supera | Dove si usa |
|---|---|---|---|---|---|---|
| `--c-ink` #1b1525 | `--c-bg` #ffffff | testo | 4,5:1 | **17,79:1** | sì | Testo principale su card e riquadri |
| `--c-ink` #1b1525 | `--c-page` #f8f6fb | testo | 4,5:1 | **16,57:1** | sì | Testo principale sullo sfondo della pagina |
| `--c-ink-muted` #554e66 | `--c-page` #f8f6fb | testo | 4,5:1 | **7,33:1** | sì | Testo secondario sullo sfondo della pagina |
| `--c-brand` #5b2c90 | `--c-page` #f8f6fb | testo | 4,5:1 | **8,86:1** | sì | Link sullo sfondo della pagina |
| `--c-ink` #1b1525 | `--c-hero-1` #e9dcfb | testo | 4,5:1 | **13,63:1** | sì | Testo dell'hero sulla sfumatura viola |
| `--c-ink` #1b1525 | `--c-hero-2` #fff0c4 | testo | 4,5:1 | **15,68:1** | sì | Testo dell'hero sulla sfumatura gialla |
| `--c-ink-muted` #554e66 | `--c-hero-1` #e9dcfb | testo | 4,5:1 | **6,03:1** | sì | Testo secondario dell'hero sulla sfumatura viola |
| `--c-ink-muted` #554e66 | `--c-hero-2` #fff0c4 | testo | 4,5:1 | **6,94:1** | sì | Testo secondario dell'hero sulla sfumatura gialla |
| `--c-brand` #5b2c90 | `--c-hero-1` #e9dcfb | testo | 4,5:1 | **7,29:1** | sì | Link dell'hero sulla sfumatura viola |
| `--c-brand` #5b2c90 | `--c-hero-2` #fff0c4 | testo | 4,5:1 | **8,39:1** | sì | Link dell'hero sulla sfumatura gialla |
| `--c-progress` #1d7356 | `--c-bg` #ffffff | testo | 4,5:1 | **5,77:1** | sì | Percentuale raggiunta nel riquadro di stato |
| `--c-accent` #ffd34e | `--c-footer-bg` #1f1230 | testo | 4,5:1 | **12,36:1** | sì | Numeri della fascia «I numeri di ideaBlume» |
| `--c-accent` #ffd34e | `--c-promo-from` #5b2c90 | testo | 4,5:1 | **6,65:1** | sì | Numeri della fascia, nella zona della sfumatura |
| `--c-footer-muted` #cfc3df | `--c-promo-from` #5b2c90 | testo | 4,5:1 | **5,67:1** | sì | Testo della fascia e del piè di pagina nella zona della sfumatura |
| `--c-footer-accent` #d7c0f7 | `--c-footer-bg` #1f1230 | testo | 4,5:1 | **10,76:1** | sì | Marchio nel piè di pagina |
| `--c-promo-fg` #ffffff | `--c-promo-from` #5b2c90 | testo | 4,5:1 | **9,51:1** | sì | Testo del riquadro di invito (inizio sfumatura) |
| `--c-promo-fg` #ffffff | `--c-promo-to` #2a1545 | testo | 4,5:1 | **16,26:1** | sì | Testo del riquadro di invito (fine sfumatura) |
| `--c-promo-from` #5b2c90 | `--c-promo-fg` #ffffff | testo | 4,5:1 | **9,51:1** | sì | Pulsante chiaro del riquadro di invito |
| `--c-ink` #1b1525 | `--c-surface` #f3eff9 | testo | 4,5:1 | **15,69:1** | sì | Testo in sezioni e riquadri |
| `--c-ink` #1b1525 | `--c-surface-2` #e9e2f4 | testo | 4,5:1 | **14,10:1** | sì | Intestazioni di tabella, riquadri annidati |
| `--c-ink` #1b1525 | `--c-brand-soft` #efe7fa | testo | 4,5:1 | **14,81:1** | sì | Testo nell'hero e nei riquadri informativi |
| `--c-ink-muted` #554e66 | `--c-bg` #ffffff | testo | 4,5:1 | **7,87:1** | sì | Testo secondario, suggerimenti dei campi |
| `--c-ink-muted` #554e66 | `--c-surface` #f3eff9 | testo | 4,5:1 | **6,94:1** | sì | Testo secondario nei riquadri |
| `--c-ink-muted` #554e66 | `--c-surface-2` #e9e2f4 | testo | 4,5:1 | **6,24:1** | sì | Testo secondario nei riquadri annidati |
| `--c-ink-muted` #554e66 | `--c-brand-soft` #efe7fa | testo | 4,5:1 | **6,55:1** | sì | Sottotitolo nell'hero |
| `--c-brand` #5b2c90 | `--c-bg` #ffffff | testo | 4,5:1 | **9,51:1** | sì | Link, titoli in colore, pulsante secondario |
| `--c-brand` #5b2c90 | `--c-surface` #f3eff9 | testo | 4,5:1 | **8,39:1** | sì | Link nei riquadri |
| `--c-brand` #5b2c90 | `--c-brand-soft` #efe7fa | testo | 4,5:1 | **7,92:1** | sì | Voce di menu corrente, link nei riquadri informativi |
| `--c-brand-dark` #43206b | `--c-brand-soft` #efe7fa | testo | 4,5:1 | **10,55:1** | sì | Link e menu al passaggio del mouse, etichette di categoria |
| `--c-brand-dark` #43206b | `--c-bg` #ffffff | testo | 4,5:1 | **12,67:1** | sì | Link al passaggio del mouse |
| `--c-on-brand` #ffffff | `--c-brand` #5b2c90 | testo | 4,5:1 | **9,51:1** | sì | Testo del pulsante principale |
| `--c-on-brand` #ffffff | `--c-brand-dark` #43206b | testo | 4,5:1 | **12,67:1** | sì | Pulsante principale al passaggio del mouse |
| `--c-st-open-fg` #0f4c8a | `--c-st-open-bg` #e7f0fa | testo | 4,5:1 | **7,53:1** | sì | Badge «In corso» |
| `--c-st-reached-fg` #1d5e37 | `--c-st-reached-bg` #e3f3e8 | testo | 4,5:1 | **6,74:1** | sì | Badge «Obiettivo raggiunto» |
| `--c-st-done-fg` #3a3646 | `--c-st-done-bg` #eceaf0 | testo | 4,5:1 | **9,80:1** | sì | Badge «Conclusa · obiettivo raggiunto»; pulsante disattivato |
| `--c-st-failed-fg` #8a2b10 | `--c-st-failed-bg` #fbebe5 | testo | 4,5:1 | **7,44:1** | sì | Badge «Conclusa · obiettivo non raggiunto» |
| `--c-error` #b0211a | `--c-bg` #ffffff | testo | 4,5:1 | **6,82:1** | sì | Messaggio di errore sotto il campo |
| `--c-error` #b0211a | `--c-error-bg` #fdecea | testo | 4,5:1 | **5,96:1** | sì | Titolo del riepilogo errori |
| `--c-ink` #1b1525 | `--c-error-bg` #fdecea | testo | 4,5:1 | **15,55:1** | sì | Testo del riepilogo errori |
| `--c-success` #1d5e37 | `--c-success-bg` #e3f3e8 | testo | 4,5:1 | **6,74:1** | sì | Messaggio di conferma |
| `--c-ink` #1b1525 | `--c-success-bg` #e3f3e8 | testo | 4,5:1 | **15,46:1** | sì | Testo nella conferma |
| `--c-warning` #6a4a00 | `--c-warning-bg` #fff4d1 | testo | 4,5:1 | **7,37:1** | sì | Avviso e segnaposto [DA VERIFICARE] |
| `--c-ink` #1b1525 | `--c-warning-bg` #fff4d1 | testo | 4,5:1 | **16,19:1** | sì | Testo negli avvisi; risposta FAQ evidenziata |
| `--c-info` #0f4c8a | `--c-info-bg` #e7f0fa | testo | 4,5:1 | **7,53:1** | sì | Avviso informativo |
| `--c-ink` #1b1525 | `--c-info-bg` #e7f0fa | testo | 4,5:1 | **15,45:1** | sì | Testo negli avvisi informativi |
| `--c-footer-fg` #ffffff | `--c-footer-bg` #1f1230 | testo | 4,5:1 | **17,68:1** | sì | Testo e link del piè di pagina |
| `--c-footer-muted` #cfc3df | `--c-footer-bg` #1f1230 | testo | 4,5:1 | **10,55:1** | sì | Nota «prototipo» nel piè di pagina |
| `--c-footer-bg` #1f1230 | `--c-footer-fg` #ffffff | testo | 4,5:1 | **17,68:1** | sì | Pulsante «Scrivici» nel piè di pagina |
| `--c-bg` #ffffff | `--c-ink` #1b1525 | testo | 4,5:1 | **17,79:1** | sì | Link «Salta al contenuto»; «?» delle spiegazioni a comparsa |
| `--c-on-brand` #ffffff | `--c-brand` #5b2c90 | testo | 4,5:1 | **9,51:1** | sì | Numero del passo corrente; numeri di «Come funziona» |
| `--c-on-progress` #ffffff | `--c-progress` #1d7356 | componente | 3,0:1 | **5,77:1** | sì | Spunta dei passi completati |
| `--c-on-error` #ffffff | `--c-error` #b0211a | componente | 3,0:1 | **6,82:1** | sì | Icona «!» degli errori |
| `--c-border-strong` #776f8d | `--c-bg` #ffffff | componente | 3,0:1 | **4,73:1** | sì | Bordo di campi e controlli |
| `--c-border-strong` #776f8d | `--c-page` #f8f6fb | componente | 3,0:1 | **4,40:1** | sì | Bordo del campo di ricerca sullo sfondo della pagina |
| `--c-border-strong` #776f8d | `--c-hero-1` #e9dcfb | componente | 3,0:1 | **3,62:1** | sì | Bordo del campo di ricerca nell'hero |
| `--c-progress` #1d7356 | `--c-page` #f8f6fb | componente | 3,0:1 | **5,38:1** | sì | Spunte dell'hero |
| `--c-border-strong` #776f8d | `--c-surface` #f3eff9 | componente | 3,0:1 | **4,17:1** | sì | Bordo dei campi nei riquadri dei filtri |
| `--c-progress` #1d7356 | `--c-track` #e6e0ee | componente | 3,0:1 | **4,47:1** | sì | Parte raccolta della barra rispetto alla parte mancante |
| `--c-progress` #1d7356 | `--c-bg` #ffffff | componente | 3,0:1 | **5,77:1** | sì | Barra piena rispetto allo sfondo |
| `--c-border-strong` #776f8d | `--c-track` #e6e0ee | componente | 3,0:1 | **3,66:1** | sì | Contorno della barra (la traccia ha anche un bordo) |
| `--c-brand` #5b2c90 | `--c-bg` #ffffff | componente | 3,0:1 | **9,51:1** | sì | Bordo del pulsante secondario e della scelta selezionata |
| `--c-error` #b0211a | `--c-bg` #ffffff | componente | 3,0:1 | **6,82:1** | sì | Bordo dei campi con errore |
| `--c-st-open-fg` #0f4c8a | `--c-bg` #ffffff | componente | 3,0:1 | **8,67:1** | sì | Bordo dei badge sullo sfondo della card |
| `--c-st-reached-fg` #1d5e37 | `--c-bg` #ffffff | componente | 3,0:1 | **7,75:1** | sì | Bordo dei badge sullo sfondo della card |
| `--c-st-done-fg` #3a3646 | `--c-bg` #ffffff | componente | 3,0:1 | **11,69:1** | sì | Bordo dei badge sullo sfondo della card |
| `--c-st-failed-fg` #8a2b10 | `--c-bg` #ffffff | componente | 3,0:1 | **8,63:1** | sì | Bordo dei badge sullo sfondo della card |
| `--c-focus` #1b1525 | `--c-bg` #ffffff | focus | 3,0:1 | **17,79:1** | sì | Anello di focus su card e campi |
| `--c-focus` #1b1525 | `--c-page` #f8f6fb | focus | 3,0:1 | **16,57:1** | sì | Anello di focus sullo sfondo della pagina |
| `--c-focus` #1b1525 | `--c-hero-1` #e9dcfb | focus | 3,0:1 | **13,63:1** | sì | Anello di focus nell'hero |
| `--c-focus-on-dark` #ffd34e | `--c-promo-from` #5b2c90 | focus | 3,0:1 | **6,65:1** | sì | Anello di focus nel riquadro di invito |
| `--c-focus` #1b1525 | `--c-surface` #f3eff9 | focus | 3,0:1 | **15,69:1** | sì | Anello di focus nei riquadri |
| `--c-focus` #1b1525 | `--c-brand-soft` #efe7fa | focus | 3,0:1 | **14,81:1** | sì | Anello di focus nell'hero e nei riquadri informativi |
| `--c-focus` #1b1525 | `--c-warning-bg` #fff4d1 | focus | 3,0:1 | **16,19:1** | sì | Anello di focus su risposta FAQ evidenziata |
| `--c-focus-on-dark` #ffd34e | `--c-footer-bg` #1f1230 | focus | 3,0:1 | **12,36:1** | sì | Anello di focus nel piè di pagina |
| `--c-focus-skip` #ffd34e | `--c-ink` #1b1525 | focus | 3,0:1 | **12,43:1** | sì | Anello di focus del link «Salta al contenuto» |

Coppie controllate: 75 · sotto soglia: 0.

## Tema scuro

| Primo piano | Sfondo | Tipo | Soglia | Rapporto | Supera | Dove si usa |
|---|---|---|---|---|---|---|
| `--c-ink` #f2eef8 | `--c-bg` #1b1525 | testo | 4,5:1 | **15,55:1** | sì | Testo principale su card e riquadri |
| `--c-ink` #f2eef8 | `--c-page` #120e19 | testo | 4,5:1 | **16,65:1** | sì | Testo principale sullo sfondo della pagina |
| `--c-ink-muted` #b9b0c9 | `--c-page` #120e19 | testo | 4,5:1 | **9,18:1** | sì | Testo secondario sullo sfondo della pagina |
| `--c-brand` #c9a8f5 | `--c-page` #120e19 | testo | 4,5:1 | **9,44:1** | sì | Link sullo sfondo della pagina |
| `--c-ink` #f2eef8 | `--c-hero-1` #2c1d48 | testo | 4,5:1 | **13,34:1** | sì | Testo dell'hero sulla sfumatura viola |
| `--c-ink` #f2eef8 | `--c-hero-2` #2a2210 | testo | 4,5:1 | **13,76:1** | sì | Testo dell'hero sulla sfumatura gialla |
| `--c-ink-muted` #b9b0c9 | `--c-hero-1` #2c1d48 | testo | 4,5:1 | **7,35:1** | sì | Testo secondario dell'hero sulla sfumatura viola |
| `--c-ink-muted` #b9b0c9 | `--c-hero-2` #2a2210 | testo | 4,5:1 | **7,58:1** | sì | Testo secondario dell'hero sulla sfumatura gialla |
| `--c-brand` #c9a8f5 | `--c-hero-1` #2c1d48 | testo | 4,5:1 | **7,56:1** | sì | Link dell'hero sulla sfumatura viola |
| `--c-brand` #c9a8f5 | `--c-hero-2` #2a2210 | testo | 4,5:1 | **7,79:1** | sì | Link dell'hero sulla sfumatura gialla |
| `--c-progress` #4cc59a | `--c-bg` #1b1525 | testo | 4,5:1 | **8,27:1** | sì | Percentuale raggiunta nel riquadro di stato |
| `--c-accent` #ffd34e | `--c-footer-bg` #0c0911 | testo | 4,5:1 | **13,81:1** | sì | Numeri della fascia «I numeri di ideaBlume» |
| `--c-accent` #ffd34e | `--c-promo-from` #4a2479 | testo | 4,5:1 | **8,07:1** | sì | Numeri della fascia, nella zona della sfumatura |
| `--c-footer-muted` #c4b9d4 | `--c-promo-from` #4a2479 | testo | 4,5:1 | **6,18:1** | sì | Testo della fascia e del piè di pagina nella zona della sfumatura |
| `--c-footer-accent` #d7c0f7 | `--c-footer-bg` #0c0911 | testo | 4,5:1 | **12,02:1** | sì | Marchio nel piè di pagina |
| `--c-promo-fg` #ffffff | `--c-promo-from` #4a2479 | testo | 4,5:1 | **11,54:1** | sì | Testo del riquadro di invito (inizio sfumatura) |
| `--c-promo-fg` #ffffff | `--c-promo-to` #1d0f30 | testo | 4,5:1 | **18,05:1** | sì | Testo del riquadro di invito (fine sfumatura) |
| `--c-promo-from` #4a2479 | `--c-promo-fg` #ffffff | testo | 4,5:1 | **11,54:1** | sì | Pulsante chiaro del riquadro di invito |
| `--c-ink` #f2eef8 | `--c-surface` #211a2e | testo | 4,5:1 | **14,67:1** | sì | Testo in sezioni e riquadri |
| `--c-ink` #f2eef8 | `--c-surface-2` #2c2340 | testo | 4,5:1 | **12,92:1** | sì | Intestazioni di tabella, riquadri annidati |
| `--c-ink` #f2eef8 | `--c-brand-soft` #2a1f3f | testo | 4,5:1 | **13,44:1** | sì | Testo nell'hero e nei riquadri informativi |
| `--c-ink-muted` #b9b0c9 | `--c-bg` #1b1525 | testo | 4,5:1 | **8,57:1** | sì | Testo secondario, suggerimenti dei campi |
| `--c-ink-muted` #b9b0c9 | `--c-surface` #211a2e | testo | 4,5:1 | **8,08:1** | sì | Testo secondario nei riquadri |
| `--c-ink-muted` #b9b0c9 | `--c-surface-2` #2c2340 | testo | 4,5:1 | **7,12:1** | sì | Testo secondario nei riquadri annidati |
| `--c-ink-muted` #b9b0c9 | `--c-brand-soft` #2a1f3f | testo | 4,5:1 | **7,40:1** | sì | Sottotitolo nell'hero |
| `--c-brand` #c9a8f5 | `--c-bg` #1b1525 | testo | 4,5:1 | **8,81:1** | sì | Link, titoli in colore, pulsante secondario |
| `--c-brand` #c9a8f5 | `--c-surface` #211a2e | testo | 4,5:1 | **8,31:1** | sì | Link nei riquadri |
| `--c-brand` #c9a8f5 | `--c-brand-soft` #2a1f3f | testo | 4,5:1 | **7,61:1** | sì | Voce di menu corrente, link nei riquadri informativi |
| `--c-brand-dark` #e2d1fb | `--c-brand-soft` #2a1f3f | testo | 4,5:1 | **10,79:1** | sì | Link e menu al passaggio del mouse, etichette di categoria |
| `--c-brand-dark` #e2d1fb | `--c-bg` #1b1525 | testo | 4,5:1 | **12,49:1** | sì | Link al passaggio del mouse |
| `--c-on-brand` #1b1028 | `--c-brand` #c9a8f5 | testo | 4,5:1 | **9,04:1** | sì | Testo del pulsante principale |
| `--c-on-brand` #1b1028 | `--c-brand-dark` #e2d1fb | testo | 4,5:1 | **12,81:1** | sì | Pulsante principale al passaggio del mouse |
| `--c-st-open-fg` #93c5fd | `--c-st-open-bg` #132842 | testo | 4,5:1 | **8,26:1** | sì | Badge «In corso» |
| `--c-st-reached-fg` #86e0aa | `--c-st-reached-bg` #11301f | testo | 4,5:1 | **9,04:1** | sì | Badge «Obiettivo raggiunto» |
| `--c-st-done-fg` #d6d0e2 | `--c-st-done-bg` #2b2638 | testo | 4,5:1 | **9,73:1** | sì | Badge «Conclusa · obiettivo raggiunto»; pulsante disattivato |
| `--c-st-failed-fg` #ffab91 | `--c-st-failed-bg` #3b1c13 | testo | 4,5:1 | **8,44:1** | sì | Badge «Conclusa · obiettivo non raggiunto» |
| `--c-error` #ff8f87 | `--c-bg` #1b1525 | testo | 4,5:1 | **8,07:1** | sì | Messaggio di errore sotto il campo |
| `--c-error` #ff8f87 | `--c-error-bg` #3b1517 | testo | 4,5:1 | **7,30:1** | sì | Titolo del riepilogo errori |
| `--c-ink` #f2eef8 | `--c-error-bg` #3b1517 | testo | 4,5:1 | **14,06:1** | sì | Testo del riepilogo errori |
| `--c-success` #86e0aa | `--c-success-bg` #11301f | testo | 4,5:1 | **9,04:1** | sì | Messaggio di conferma |
| `--c-ink` #f2eef8 | `--c-success-bg` #11301f | testo | 4,5:1 | **12,52:1** | sì | Testo nella conferma |
| `--c-warning` #ffd479 | `--c-warning-bg` #33280b | testo | 4,5:1 | **10,31:1** | sì | Avviso e segnaposto [DA VERIFICARE] |
| `--c-ink` #f2eef8 | `--c-warning-bg` #33280b | testo | 4,5:1 | **12,67:1** | sì | Testo negli avvisi; risposta FAQ evidenziata |
| `--c-info` #93c5fd | `--c-info-bg` #132842 | testo | 4,5:1 | **8,26:1** | sì | Avviso informativo |
| `--c-ink` #f2eef8 | `--c-info-bg` #132842 | testo | 4,5:1 | **13,02:1** | sì | Testo negli avvisi informativi |
| `--c-footer-fg` #ffffff | `--c-footer-bg` #0c0911 | testo | 4,5:1 | **19,76:1** | sì | Testo e link del piè di pagina |
| `--c-footer-muted` #c4b9d4 | `--c-footer-bg` #0c0911 | testo | 4,5:1 | **10,57:1** | sì | Nota «prototipo» nel piè di pagina |
| `--c-footer-bg` #0c0911 | `--c-footer-fg` #ffffff | testo | 4,5:1 | **19,76:1** | sì | Pulsante «Scrivici» nel piè di pagina |
| `--c-bg` #1b1525 | `--c-ink` #f2eef8 | testo | 4,5:1 | **15,55:1** | sì | Link «Salta al contenuto»; «?» delle spiegazioni a comparsa |
| `--c-on-brand` #1b1028 | `--c-brand` #c9a8f5 | testo | 4,5:1 | **9,04:1** | sì | Numero del passo corrente; numeri di «Come funziona» |
| `--c-on-progress` #0c1a14 | `--c-progress` #4cc59a | componente | 3,0:1 | **8,32:1** | sì | Spunta dei passi completati |
| `--c-on-error` #1b0606 | `--c-error` #ff8f87 | componente | 3,0:1 | **8,86:1** | sì | Icona «!» degli errori |
| `--c-border-strong` #8d83a3 | `--c-bg` #1b1525 | componente | 3,0:1 | **5,00:1** | sì | Bordo di campi e controlli |
| `--c-border-strong` #8d83a3 | `--c-page` #120e19 | componente | 3,0:1 | **5,36:1** | sì | Bordo del campo di ricerca sullo sfondo della pagina |
| `--c-border-strong` #8d83a3 | `--c-hero-1` #2c1d48 | componente | 3,0:1 | **4,29:1** | sì | Bordo del campo di ricerca nell'hero |
| `--c-progress` #4cc59a | `--c-page` #120e19 | componente | 3,0:1 | **8,85:1** | sì | Spunte dell'hero |
| `--c-border-strong` #8d83a3 | `--c-surface` #211a2e | componente | 3,0:1 | **4,72:1** | sì | Bordo dei campi nei riquadri dei filtri |
| `--c-progress` #4cc59a | `--c-track` #342b47 | componente | 3,0:1 | **6,17:1** | sì | Parte raccolta della barra rispetto alla parte mancante |
| `--c-progress` #4cc59a | `--c-bg` #1b1525 | componente | 3,0:1 | **8,27:1** | sì | Barra piena rispetto allo sfondo |
| `--c-border-strong` #8d83a3 | `--c-track` #342b47 | componente | 3,0:1 | **3,73:1** | sì | Contorno della barra (la traccia ha anche un bordo) |
| `--c-brand` #c9a8f5 | `--c-bg` #1b1525 | componente | 3,0:1 | **8,81:1** | sì | Bordo del pulsante secondario e della scelta selezionata |
| `--c-error` #ff8f87 | `--c-bg` #1b1525 | componente | 3,0:1 | **8,07:1** | sì | Bordo dei campi con errore |
| `--c-st-open-fg` #93c5fd | `--c-bg` #1b1525 | componente | 3,0:1 | **9,86:1** | sì | Bordo dei badge sullo sfondo della card |
| `--c-st-reached-fg` #86e0aa | `--c-bg` #1b1525 | componente | 3,0:1 | **11,23:1** | sì | Bordo dei badge sullo sfondo della card |
| `--c-st-done-fg` #d6d0e2 | `--c-bg` #1b1525 | componente | 3,0:1 | **11,84:1** | sì | Bordo dei badge sullo sfondo della card |
| `--c-st-failed-fg` #ffab91 | `--c-bg` #1b1525 | componente | 3,0:1 | **9,73:1** | sì | Bordo dei badge sullo sfondo della card |
| `--c-focus` #f2eef8 | `--c-bg` #1b1525 | focus | 3,0:1 | **15,55:1** | sì | Anello di focus su card e campi |
| `--c-focus` #f2eef8 | `--c-page` #120e19 | focus | 3,0:1 | **16,65:1** | sì | Anello di focus sullo sfondo della pagina |
| `--c-focus` #f2eef8 | `--c-hero-1` #2c1d48 | focus | 3,0:1 | **13,34:1** | sì | Anello di focus nell'hero |
| `--c-focus-on-dark` #ffd34e | `--c-promo-from` #4a2479 | focus | 3,0:1 | **8,07:1** | sì | Anello di focus nel riquadro di invito |
| `--c-focus` #f2eef8 | `--c-surface` #211a2e | focus | 3,0:1 | **14,67:1** | sì | Anello di focus nei riquadri |
| `--c-focus` #f2eef8 | `--c-brand-soft` #2a1f3f | focus | 3,0:1 | **13,44:1** | sì | Anello di focus nell'hero e nei riquadri informativi |
| `--c-focus` #f2eef8 | `--c-warning-bg` #33280b | focus | 3,0:1 | **12,67:1** | sì | Anello di focus su risposta FAQ evidenziata |
| `--c-focus-on-dark` #ffd34e | `--c-footer-bg` #0c0911 | focus | 3,0:1 | **13,81:1** | sì | Anello di focus nel piè di pagina |
| `--c-focus-skip` #9b6ad8 | `--c-ink` #f2eef8 | focus | 3,0:1 | **3,37:1** | sì | Anello di focus del link «Salta al contenuto» |

Coppie controllate: 75 · sotto soglia: 0.
