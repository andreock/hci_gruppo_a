# Contrasti del design system

Generato da `tools/contrasto.py` a partire dai token di `css/ideablume.css`, per il tema chiaro e per il tema scuro
(il tema predefinito è quello chiaro; quello scuro si sceglie con l'interruttore nell'intestazione).
Soglie WCAG 2.2: testo normale 4,5:1 (1.4.3); testo grande, componenti dell'interfaccia e indicatori di focus 3:1 (1.4.11).

## Tema chiaro

| Primo piano | Sfondo | Tipo | Soglia | Rapporto | Supera | Dove si usa |
|---|---|---|---|---|---|---|
| `--c-ink` #3b1d2a | `--c-bg` #fffdf9 | testo | 4,5:1 | **14,82:1** | sì | Testo principale su card e riquadri |
| `--c-ink` #3b1d2a | `--c-page` #fbf6ee | testo | 4,5:1 | **13,99:1** | sì | Testo principale sullo sfondo della pagina |
| `--c-ink-muted` #66544a | `--c-page` #fbf6ee | testo | 4,5:1 | **6,66:1** | sì | Testo secondario sullo sfondo della pagina |
| `--c-brand` #a33f0f | `--c-page` #fbf6ee | testo | 4,5:1 | **5,96:1** | sì | Link sullo sfondo della pagina |
| `--c-ink` #3b1d2a | `--c-hero-1` #fbe3cf | testo | 4,5:1 | **12,18:1** | sì | Testo dell'hero sulla sfumatura pesca |
| `--c-ink` #3b1d2a | `--c-hero-2` #fdf0cf | testo | 4,5:1 | **13,29:1** | sì | Testo dell'hero sulla sfumatura miele |
| `--c-ink-muted` #66544a | `--c-hero-1` #fbe3cf | testo | 4,5:1 | **5,79:1** | sì | Testo secondario dell'hero sulla sfumatura pesca |
| `--c-ink-muted` #66544a | `--c-hero-2` #fdf0cf | testo | 4,5:1 | **6,32:1** | sì | Testo secondario dell'hero sulla sfumatura miele |
| `--c-brand` #a33f0f | `--c-hero-1` #fbe3cf | testo | 4,5:1 | **5,19:1** | sì | Link dell'hero sulla sfumatura pesca |
| `--c-brand` #a33f0f | `--c-hero-2` #fdf0cf | testo | 4,5:1 | **5,66:1** | sì | Link dell'hero sulla sfumatura miele |
| `--c-progress` #bf4a12 | `--c-bg` #fffdf9 | testo | 4,5:1 | **4,92:1** | sì | Percentuale raggiunta nel riquadro di stato |
| `--c-accent` #f4b93e | `--c-footer-bg` #3b1d2a | testo | 4,5:1 | **8,50:1** | sì | Numeri della fascia «I numeri di ideaBlume» |
| `--c-accent` #f4b93e | `--c-promo-from` #7a3010 | testo | 4,5:1 | **5,25:1** | sì | Numeri della fascia, nella zona della sfumatura |
| `--c-footer-muted` #e6d6c8 | `--c-promo-from` #7a3010 | testo | 4,5:1 | **6,56:1** | sì | Testo della fascia e del piè di pagina nella zona della sfumatura |
| `--c-footer-accent` #f7c9a0 | `--c-footer-bg` #3b1d2a | testo | 4,5:1 | **9,90:1** | sì | Marchio nel piè di pagina |
| `--c-promo-fg` #ffffff | `--c-promo-from` #7a3010 | testo | 4,5:1 | **9,30:1** | sì | Testo del riquadro di invito (inizio sfumatura) |
| `--c-promo-fg` #ffffff | `--c-promo-to` #3b1d2a | testo | 4,5:1 | **15,05:1** | sì | Testo del riquadro di invito (fine sfumatura) |
| `--c-promo-from` #7a3010 | `--c-promo-fg` #ffffff | testo | 4,5:1 | **9,30:1** | sì | Pulsante chiaro del riquadro di invito |
| `--c-ink` #3b1d2a | `--c-surface` #f7efe4 | testo | 4,5:1 | **13,20:1** | sì | Testo in sezioni e riquadri |
| `--c-ink` #3b1d2a | `--c-surface-2` #f0e6d9 | testo | 4,5:1 | **12,20:1** | sì | Intestazioni di tabella, riquadri annidati |
| `--c-ink` #3b1d2a | `--c-brand-soft` #fbeadd | testo | 4,5:1 | **12,84:1** | sì | Testo nell'hero e nei riquadri informativi |
| `--c-ink-muted` #66544a | `--c-bg` #fffdf9 | testo | 4,5:1 | **7,05:1** | sì | Testo secondario, suggerimenti dei campi |
| `--c-ink-muted` #66544a | `--c-surface` #f7efe4 | testo | 4,5:1 | **6,28:1** | sì | Testo secondario nei riquadri |
| `--c-ink-muted` #66544a | `--c-surface-2` #f0e6d9 | testo | 4,5:1 | **5,81:1** | sì | Testo secondario nei riquadri annidati |
| `--c-ink-muted` #66544a | `--c-brand-soft` #fbeadd | testo | 4,5:1 | **6,11:1** | sì | Sottotitolo nell'hero |
| `--c-brand` #a33f0f | `--c-bg` #fffdf9 | testo | 4,5:1 | **6,31:1** | sì | Link, titoli in colore, pulsante secondario |
| `--c-brand` #a33f0f | `--c-surface` #f7efe4 | testo | 4,5:1 | **5,62:1** | sì | Link nei riquadri |
| `--c-brand` #a33f0f | `--c-brand-soft` #fbeadd | testo | 4,5:1 | **5,47:1** | sì | Voce di menu corrente, link nei riquadri informativi |
| `--c-brand-dark` #7a3010 | `--c-brand-soft` #fbeadd | testo | 4,5:1 | **7,93:1** | sì | Link e menu al passaggio del mouse, etichette di categoria |
| `--c-brand-dark` #7a3010 | `--c-bg` #fffdf9 | testo | 4,5:1 | **9,16:1** | sì | Link al passaggio del mouse |
| `--c-on-primary` #fff8f0 | `--c-primary` #3b1d2a | testo | 4,5:1 | **14,29:1** | sì | Testo del pulsante normale (ricerca, invio moduli) |
| `--c-on-primary` #fff8f0 | `--c-primary-hover` #57293d | testo | 4,5:1 | **11,14:1** | sì | Pulsante normale al passaggio del mouse |
| `--c-on-cta` #ffffff | `--c-cta` #bf4a12 | testo | 4,5:1 | **5,00:1** | sì | Testo del pulsante «Sostieni il progetto» |
| `--c-on-cta` #ffffff | `--c-cta-hover` #9e3b0c | testo | 4,5:1 | **6,81:1** | sì | Pulsante «Sostieni il progetto» al passaggio del mouse e durante il pagamento |
| `--c-on-brand` #ffffff | `--c-brand` #a33f0f | testo | 4,5:1 | **6,41:1** | sì | Testo su fondo del marchio: selezione del testo |
| `--c-on-brand` #ffffff | `--c-brand-dark` #7a3010 | testo | 4,5:1 | **9,30:1** | sì | Testo su fondo del marchio scuro |
| `--c-ink` #3b1d2a | `--c-bg` #fffdf9 | testo | 4,5:1 | **14,82:1** | sì | Testo della card della ricompensa |
| `--c-ink` #3b1d2a | `--c-brand-soft` #fbeadd | testo | 4,5:1 | **12,84:1** | sì | Testo della ricompensa selezionata |
| `--c-ink-muted` #66544a | `--c-brand-soft` #fbeadd | testo | 4,5:1 | **6,11:1** | sì | Nota della ricompensa selezionata |
| `--c-brand-dark` #7a3010 | `--c-surface` #f7efe4 | testo | 4,5:1 | **8,16:1** | sì | Etichette nelle sezioni tinte |
| `--c-secondary` #24603f | `--c-page` #fbf6ee | testo | 4,5:1 | **6,92:1** | sì | Conferme in verde sullo sfondo della pagina |
| `--c-secondary` #24603f | `--c-bg` #fffdf9 | testo | 4,5:1 | **7,33:1** | sì | Conferme in verde sulle card |
| `--c-st-open-fg` #1d5b73 | `--c-st-open-bg` #e3eff2 | testo | 4,5:1 | **6,40:1** | sì | Badge «In corso» |
| `--c-st-reached-fg` #24603f | `--c-st-reached-bg` #e3f2e6 | testo | 4,5:1 | **6,42:1** | sì | Badge «Obiettivo raggiunto» |
| `--c-st-done-fg` #4f443e | `--c-st-done-bg` #efe8e1 | testo | 4,5:1 | **7,76:1** | sì | Badge «Conclusa · obiettivo raggiunto»; pulsante disattivato |
| `--c-st-failed-fg` #8f2b1c | `--c-st-failed-bg` #fbe9e4 | testo | 4,5:1 | **7,07:1** | sì | Badge «Conclusa · obiettivo non raggiunto» |
| `--c-error` #a3271a | `--c-bg` #fffdf9 | testo | 4,5:1 | **7,22:1** | sì | Messaggio di errore sotto il campo |
| `--c-error` #a3271a | `--c-error-bg` #fbe9e4 | testo | 4,5:1 | **6,25:1** | sì | Titolo del riepilogo errori |
| `--c-ink` #3b1d2a | `--c-error-bg` #fbe9e4 | testo | 4,5:1 | **12,81:1** | sì | Testo del riepilogo errori |
| `--c-success` #24603f | `--c-success-bg` #e3f2e6 | testo | 4,5:1 | **6,42:1** | sì | Messaggio di conferma |
| `--c-ink` #3b1d2a | `--c-success-bg` #e3f2e6 | testo | 4,5:1 | **12,98:1** | sì | Testo nella conferma |
| `--c-warning` #7a4d00 | `--c-warning-bg` #fdf0cf | testo | 4,5:1 | **6,42:1** | sì | Avviso |
| `--c-ink` #3b1d2a | `--c-warning-bg` #fdf0cf | testo | 4,5:1 | **13,29:1** | sì | Testo negli avvisi; risposta FAQ evidenziata |
| `--c-info` #1d5b73 | `--c-info-bg` #e3eff2 | testo | 4,5:1 | **6,40:1** | sì | Avviso informativo |
| `--c-ink` #3b1d2a | `--c-info-bg` #e3eff2 | testo | 4,5:1 | **12,83:1** | sì | Testo negli avvisi informativi |
| `--c-footer-fg` #fffaf3 | `--c-footer-bg` #3b1d2a | testo | 4,5:1 | **14,49:1** | sì | Testo e link del piè di pagina |
| `--c-footer-muted` #e6d6c8 | `--c-footer-bg` #3b1d2a | testo | 4,5:1 | **10,62:1** | sì | Nota nel piè di pagina |
| `--c-footer-bg` #3b1d2a | `--c-footer-fg` #fffaf3 | testo | 4,5:1 | **14,49:1** | sì | Pulsante «Scrivici» nel piè di pagina |
| `--c-bg` #fffdf9 | `--c-ink` #3b1d2a | testo | 4,5:1 | **14,82:1** | sì | Link «Salta al contenuto»; «?» delle spiegazioni a comparsa |
| `--c-on-brand` #ffffff | `--c-brand` #a33f0f | testo | 4,5:1 | **6,41:1** | sì | Numero del passo corrente; numeri di «Come funziona» |
| `--c-on-secondary` #ffffff | `--c-secondary` #24603f | componente | 3,0:1 | **7,45:1** | sì | Spunta dei passi completati |
| `--c-on-error` #ffffff | `--c-error` #a3271a | componente | 3,0:1 | **7,34:1** | sì | Icona «!» degli errori |
| `--c-border-strong` #8a7568 | `--c-bg` #fffdf9 | componente | 3,0:1 | **4,28:1** | sì | Bordo di campi e controlli |
| `--c-border-strong` #8a7568 | `--c-page` #fbf6ee | componente | 3,0:1 | **4,05:1** | sì | Bordo del campo di ricerca sullo sfondo della pagina |
| `--c-border-strong` #8a7568 | `--c-hero-1` #fbe3cf | componente | 3,0:1 | **3,52:1** | sì | Bordo del campo di ricerca nell'hero |
| `--c-secondary` #24603f | `--c-page` #fbf6ee | componente | 3,0:1 | **6,92:1** | sì | Spunte dell'hero |
| `--c-secondary` #24603f | `--c-hero-2` #fdf0cf | componente | 3,0:1 | **6,58:1** | sì | Spunte dell'hero sulla sfumatura miele |
| `--c-cta` #bf4a12 | `--c-page` #fbf6ee | componente | 3,0:1 | **4,64:1** | sì | Pulsante «Sostieni il progetto» sullo sfondo della pagina |
| `--c-cta` #bf4a12 | `--c-bg` #fffdf9 | componente | 3,0:1 | **4,92:1** | sì | Pulsante «Sostieni il progetto» sulla card |
| `--c-cta` #bf4a12 | `--c-brand-soft` #fbeadd | componente | 3,0:1 | **4,26:1** | sì | Bordo della ricompensa selezionata |
| `--c-brand` #a33f0f | `--c-page` #fbf6ee | componente | 3,0:1 | **5,96:1** | sì | Icona dell'interruttore del tema |
| `--c-border-strong` #8a7568 | `--c-surface` #f7efe4 | componente | 3,0:1 | **3,82:1** | sì | Bordo dei campi nei riquadri dei filtri |
| `--c-progress` #bf4a12 | `--c-track` #eadfd3 | componente | 3,0:1 | **3,80:1** | sì | Parte raccolta della barra rispetto alla parte mancante |
| `--c-progress` #bf4a12 | `--c-bg` #fffdf9 | componente | 3,0:1 | **4,92:1** | sì | Barra piena rispetto allo sfondo |
| `--c-border-strong` #8a7568 | `--c-track` #eadfd3 | componente | 3,0:1 | **3,31:1** | sì | Contorno della barra (la traccia ha anche un bordo) |
| `--c-brand` #a33f0f | `--c-bg` #fffdf9 | componente | 3,0:1 | **6,31:1** | sì | Bordo del pulsante secondario e della scelta selezionata |
| `--c-error` #a3271a | `--c-bg` #fffdf9 | componente | 3,0:1 | **7,22:1** | sì | Bordo dei campi con errore |
| `--c-st-open-fg` #1d5b73 | `--c-bg` #fffdf9 | componente | 3,0:1 | **7,39:1** | sì | Bordo dei badge sullo sfondo della card |
| `--c-st-reached-fg` #24603f | `--c-bg` #fffdf9 | componente | 3,0:1 | **7,33:1** | sì | Bordo dei badge sullo sfondo della card |
| `--c-st-done-fg` #4f443e | `--c-bg` #fffdf9 | componente | 3,0:1 | **9,27:1** | sì | Bordo dei badge sullo sfondo della card |
| `--c-st-failed-fg` #8f2b1c | `--c-bg` #fffdf9 | componente | 3,0:1 | **8,17:1** | sì | Bordo dei badge sullo sfondo della card |
| `--c-focus` #3b1d2a | `--c-bg` #fffdf9 | focus | 3,0:1 | **14,82:1** | sì | Anello di focus su card e campi |
| `--c-focus` #3b1d2a | `--c-page` #fbf6ee | focus | 3,0:1 | **13,99:1** | sì | Anello di focus sullo sfondo della pagina |
| `--c-focus` #3b1d2a | `--c-hero-1` #fbe3cf | focus | 3,0:1 | **12,18:1** | sì | Anello di focus nell'hero |
| `--c-focus-on-dark` #f4b93e | `--c-promo-from` #7a3010 | focus | 3,0:1 | **5,25:1** | sì | Anello di focus nel riquadro di invito |
| `--c-focus` #3b1d2a | `--c-surface` #f7efe4 | focus | 3,0:1 | **13,20:1** | sì | Anello di focus nei riquadri |
| `--c-focus` #3b1d2a | `--c-brand-soft` #fbeadd | focus | 3,0:1 | **12,84:1** | sì | Anello di focus nell'hero e nei riquadri informativi |
| `--c-focus` #3b1d2a | `--c-warning-bg` #fdf0cf | focus | 3,0:1 | **13,29:1** | sì | Anello di focus su risposta FAQ evidenziata |
| `--c-focus-on-dark` #f4b93e | `--c-footer-bg` #3b1d2a | focus | 3,0:1 | **8,50:1** | sì | Anello di focus nel piè di pagina |
| `--c-focus-skip` #f4b93e | `--c-ink` #3b1d2a | focus | 3,0:1 | **8,50:1** | sì | Anello di focus del link «Salta al contenuto» |

Coppie controllate: 90 · sotto soglia: 0.

## Tema scuro

| Primo piano | Sfondo | Tipo | Soglia | Rapporto | Supera | Dove si usa |
|---|---|---|---|---|---|---|
| `--c-ink` #f8efe6 | `--c-bg` #271c19 | testo | 4,5:1 | **14,59:1** | sì | Testo principale su card e riquadri |
| `--c-ink` #f8efe6 | `--c-page` #1c1412 | testo | 4,5:1 | **15,96:1** | sì | Testo principale sullo sfondo della pagina |
| `--c-ink-muted` #cdbcae | `--c-page` #1c1412 | testo | 4,5:1 | **9,84:1** | sì | Testo secondario sullo sfondo della pagina |
| `--c-brand` #ffb27a | `--c-page` #1c1412 | testo | 4,5:1 | **10,28:1** | sì | Link sullo sfondo della pagina |
| `--c-ink` #f8efe6 | `--c-hero-1` #3a2318 | testo | 4,5:1 | **12,89:1** | sì | Testo dell'hero sulla sfumatura pesca |
| `--c-ink` #f8efe6 | `--c-hero-2` #33270c | testo | 4,5:1 | **12,87:1** | sì | Testo dell'hero sulla sfumatura miele |
| `--c-ink-muted` #cdbcae | `--c-hero-1` #3a2318 | testo | 4,5:1 | **7,95:1** | sì | Testo secondario dell'hero sulla sfumatura pesca |
| `--c-ink-muted` #cdbcae | `--c-hero-2` #33270c | testo | 4,5:1 | **7,94:1** | sì | Testo secondario dell'hero sulla sfumatura miele |
| `--c-brand` #ffb27a | `--c-hero-1` #3a2318 | testo | 4,5:1 | **8,30:1** | sì | Link dell'hero sulla sfumatura pesca |
| `--c-brand` #ffb27a | `--c-hero-2` #33270c | testo | 4,5:1 | **8,29:1** | sì | Link dell'hero sulla sfumatura miele |
| `--c-progress` #f58b4a | `--c-bg` #271c19 | testo | 4,5:1 | **6,85:1** | sì | Percentuale raggiunta nel riquadro di stato |
| `--c-accent` #f4b93e | `--c-footer-bg` #140d0b | testo | 4,5:1 | **10,86:1** | sì | Numeri della fascia «I numeri di ideaBlume» |
| `--c-accent` #f4b93e | `--c-promo-from` #7a3010 | testo | 4,5:1 | **5,25:1** | sì | Numeri della fascia, nella zona della sfumatura |
| `--c-footer-muted` #d4c3b5 | `--c-promo-from` #7a3010 | testo | 4,5:1 | **5,44:1** | sì | Testo della fascia e del piè di pagina nella zona della sfumatura |
| `--c-footer-accent` #f7c9a0 | `--c-footer-bg` #140d0b | testo | 4,5:1 | **12,65:1** | sì | Marchio nel piè di pagina |
| `--c-promo-fg` #ffffff | `--c-promo-from` #7a3010 | testo | 4,5:1 | **9,30:1** | sì | Testo del riquadro di invito (inizio sfumatura) |
| `--c-promo-fg` #ffffff | `--c-promo-to` #2a130d | testo | 4,5:1 | **17,54:1** | sì | Testo del riquadro di invito (fine sfumatura) |
| `--c-promo-from` #7a3010 | `--c-promo-fg` #ffffff | testo | 4,5:1 | **9,30:1** | sì | Pulsante chiaro del riquadro di invito |
| `--c-ink` #f8efe6 | `--c-surface` #2f231f | testo | 4,5:1 | **13,38:1** | sì | Testo in sezioni e riquadri |
| `--c-ink` #f8efe6 | `--c-surface-2` #3a2c27 | testo | 4,5:1 | **11,77:1** | sì | Intestazioni di tabella, riquadri annidati |
| `--c-ink` #f8efe6 | `--c-brand-soft` #3a2318 | testo | 4,5:1 | **12,89:1** | sì | Testo nell'hero e nei riquadri informativi |
| `--c-ink-muted` #cdbcae | `--c-bg` #271c19 | testo | 4,5:1 | **9,00:1** | sì | Testo secondario, suggerimenti dei campi |
| `--c-ink-muted` #cdbcae | `--c-surface` #2f231f | testo | 4,5:1 | **8,25:1** | sì | Testo secondario nei riquadri |
| `--c-ink-muted` #cdbcae | `--c-surface-2` #3a2c27 | testo | 4,5:1 | **7,26:1** | sì | Testo secondario nei riquadri annidati |
| `--c-ink-muted` #cdbcae | `--c-brand-soft` #3a2318 | testo | 4,5:1 | **7,95:1** | sì | Sottotitolo nell'hero |
| `--c-brand` #ffb27a | `--c-bg` #271c19 | testo | 4,5:1 | **9,40:1** | sì | Link, titoli in colore, pulsante secondario |
| `--c-brand` #ffb27a | `--c-surface` #2f231f | testo | 4,5:1 | **8,62:1** | sì | Link nei riquadri |
| `--c-brand` #ffb27a | `--c-brand-soft` #3a2318 | testo | 4,5:1 | **8,30:1** | sì | Voce di menu corrente, link nei riquadri informativi |
| `--c-brand-dark` #ffd0ab | `--c-brand-soft` #3a2318 | testo | 4,5:1 | **10,37:1** | sì | Link e menu al passaggio del mouse, etichette di categoria |
| `--c-brand-dark` #ffd0ab | `--c-bg` #271c19 | testo | 4,5:1 | **11,74:1** | sì | Link al passaggio del mouse |
| `--c-on-primary` #2a1a17 | `--c-primary` #f8efe6 | testo | 4,5:1 | **14,68:1** | sì | Testo del pulsante normale (ricerca, invio moduli) |
| `--c-on-primary` #2a1a17 | `--c-primary-hover` #fff8f0 | testo | 4,5:1 | **15,84:1** | sì | Pulsante normale al passaggio del mouse |
| `--c-on-cta` #2a1205 | `--c-cta` #f58b4a | testo | 4,5:1 | **7,31:1** | sì | Testo del pulsante «Sostieni il progetto» |
| `--c-on-cta` #2a1205 | `--c-cta-hover` #ffa66e | testo | 4,5:1 | **9,21:1** | sì | Pulsante «Sostieni il progetto» al passaggio del mouse e durante il pagamento |
| `--c-on-brand` #2a1205 | `--c-brand` #ffb27a | testo | 4,5:1 | **10,02:1** | sì | Testo su fondo del marchio: selezione del testo |
| `--c-on-brand` #2a1205 | `--c-brand-dark` #ffd0ab | testo | 4,5:1 | **12,52:1** | sì | Testo su fondo del marchio scuro |
| `--c-ink` #f8efe6 | `--c-bg` #271c19 | testo | 4,5:1 | **14,59:1** | sì | Testo della card della ricompensa |
| `--c-ink` #f8efe6 | `--c-brand-soft` #3a2318 | testo | 4,5:1 | **12,89:1** | sì | Testo della ricompensa selezionata |
| `--c-ink-muted` #cdbcae | `--c-brand-soft` #3a2318 | testo | 4,5:1 | **7,95:1** | sì | Nota della ricompensa selezionata |
| `--c-brand-dark` #ffd0ab | `--c-surface` #2f231f | testo | 4,5:1 | **10,76:1** | sì | Etichette nelle sezioni tinte |
| `--c-secondary` #7fd6a3 | `--c-page` #1c1412 | testo | 4,5:1 | **10,40:1** | sì | Conferme in verde sullo sfondo della pagina |
| `--c-secondary` #7fd6a3 | `--c-bg` #271c19 | testo | 4,5:1 | **9,52:1** | sì | Conferme in verde sulle card |
| `--c-st-open-fg` #8fcbe0 | `--c-st-open-bg` #12303b | testo | 4,5:1 | **7,80:1** | sì | Badge «In corso» |
| `--c-st-reached-fg` #7fd6a3 | `--c-st-reached-bg` #15301f | testo | 4,5:1 | **8,17:1** | sì | Badge «Obiettivo raggiunto» |
| `--c-st-done-fg` #dccfc3 | `--c-st-done-bg` #352a25 | testo | 4,5:1 | **9,11:1** | sì | Badge «Conclusa · obiettivo raggiunto»; pulsante disattivato |
| `--c-st-failed-fg` #ffa995 | `--c-st-failed-bg` #3a1712 | testo | 4,5:1 | **8,66:1** | sì | Badge «Conclusa · obiettivo non raggiunto» |
| `--c-error` #ff9e8c | `--c-bg` #271c19 | testo | 4,5:1 | **8,31:1** | sì | Messaggio di errore sotto il campo |
| `--c-error` #ff9e8c | `--c-error-bg` #3a1712 | testo | 4,5:1 | **8,02:1** | sì | Titolo del riepilogo errori |
| `--c-ink` #f8efe6 | `--c-error-bg` #3a1712 | testo | 4,5:1 | **14,09:1** | sì | Testo del riepilogo errori |
| `--c-success` #7fd6a3 | `--c-success-bg` #15301f | testo | 4,5:1 | **8,17:1** | sì | Messaggio di conferma |
| `--c-ink` #f8efe6 | `--c-success-bg` #15301f | testo | 4,5:1 | **12,53:1** | sì | Testo nella conferma |
| `--c-warning` #f7cf77 | `--c-warning-bg` #33270c | testo | 4,5:1 | **9,85:1** | sì | Avviso |
| `--c-ink` #f8efe6 | `--c-warning-bg` #33270c | testo | 4,5:1 | **12,87:1** | sì | Testo negli avvisi; risposta FAQ evidenziata |
| `--c-info` #8fcbe0 | `--c-info-bg` #12303b | testo | 4,5:1 | **7,80:1** | sì | Avviso informativo |
| `--c-ink` #f8efe6 | `--c-info-bg` #12303b | testo | 4,5:1 | **12,23:1** | sì | Testo negli avvisi informativi |
| `--c-footer-fg` #fffaf3 | `--c-footer-bg` #140d0b | testo | 4,5:1 | **18,51:1** | sì | Testo e link del piè di pagina |
| `--c-footer-muted` #d4c3b5 | `--c-footer-bg` #140d0b | testo | 4,5:1 | **11,24:1** | sì | Nota nel piè di pagina |
| `--c-footer-bg` #140d0b | `--c-footer-fg` #fffaf3 | testo | 4,5:1 | **18,51:1** | sì | Pulsante «Scrivici» nel piè di pagina |
| `--c-bg` #271c19 | `--c-ink` #f8efe6 | testo | 4,5:1 | **14,59:1** | sì | Link «Salta al contenuto»; «?» delle spiegazioni a comparsa |
| `--c-on-brand` #2a1205 | `--c-brand` #ffb27a | testo | 4,5:1 | **10,02:1** | sì | Numero del passo corrente; numeri di «Come funziona» |
| `--c-on-secondary` #0c1f14 | `--c-secondary` #7fd6a3 | componente | 3,0:1 | **9,86:1** | sì | Spunta dei passi completati |
| `--c-on-error` #2a0a05 | `--c-error` #ff9e8c | componente | 3,0:1 | **9,20:1** | sì | Icona «!» degli errori |
| `--c-border-strong` #a08c7e | `--c-bg` #271c19 | componente | 3,0:1 | **5,17:1** | sì | Bordo di campi e controlli |
| `--c-border-strong` #a08c7e | `--c-page` #1c1412 | componente | 3,0:1 | **5,65:1** | sì | Bordo del campo di ricerca sullo sfondo della pagina |
| `--c-border-strong` #a08c7e | `--c-hero-1` #3a2318 | componente | 3,0:1 | **4,57:1** | sì | Bordo del campo di ricerca nell'hero |
| `--c-secondary` #7fd6a3 | `--c-page` #1c1412 | componente | 3,0:1 | **10,40:1** | sì | Spunte dell'hero |
| `--c-secondary` #7fd6a3 | `--c-hero-2` #33270c | componente | 3,0:1 | **8,39:1** | sì | Spunte dell'hero sulla sfumatura miele |
| `--c-cta` #f58b4a | `--c-page` #1c1412 | componente | 3,0:1 | **7,49:1** | sì | Pulsante «Sostieni il progetto» sullo sfondo della pagina |
| `--c-cta` #f58b4a | `--c-bg` #271c19 | componente | 3,0:1 | **6,85:1** | sì | Pulsante «Sostieni il progetto» sulla card |
| `--c-cta` #f58b4a | `--c-brand-soft` #3a2318 | componente | 3,0:1 | **6,05:1** | sì | Bordo della ricompensa selezionata |
| `--c-brand` #ffb27a | `--c-page` #1c1412 | componente | 3,0:1 | **10,28:1** | sì | Icona dell'interruttore del tema |
| `--c-border-strong` #a08c7e | `--c-surface` #2f231f | componente | 3,0:1 | **4,74:1** | sì | Bordo dei campi nei riquadri dei filtri |
| `--c-progress` #f58b4a | `--c-track` #4a3a33 | componente | 3,0:1 | **4,46:1** | sì | Parte raccolta della barra rispetto alla parte mancante |
| `--c-progress` #f58b4a | `--c-bg` #271c19 | componente | 3,0:1 | **6,85:1** | sì | Barra piena rispetto allo sfondo |
| `--c-border-strong` #a08c7e | `--c-track` #4a3a33 | componente | 3,0:1 | **3,37:1** | sì | Contorno della barra (la traccia ha anche un bordo) |
| `--c-brand` #ffb27a | `--c-bg` #271c19 | componente | 3,0:1 | **9,40:1** | sì | Bordo del pulsante secondario e della scelta selezionata |
| `--c-error` #ff9e8c | `--c-bg` #271c19 | componente | 3,0:1 | **8,31:1** | sì | Bordo dei campi con errore |
| `--c-st-open-fg` #8fcbe0 | `--c-bg` #271c19 | componente | 3,0:1 | **9,31:1** | sì | Bordo dei badge sullo sfondo della card |
| `--c-st-reached-fg` #7fd6a3 | `--c-bg` #271c19 | componente | 3,0:1 | **9,52:1** | sì | Bordo dei badge sullo sfondo della card |
| `--c-st-done-fg` #dccfc3 | `--c-bg` #271c19 | componente | 3,0:1 | **10,86:1** | sì | Bordo dei badge sullo sfondo della card |
| `--c-st-failed-fg` #ffa995 | `--c-bg` #271c19 | componente | 3,0:1 | **8,97:1** | sì | Bordo dei badge sullo sfondo della card |
| `--c-focus` #f8efe6 | `--c-bg` #271c19 | focus | 3,0:1 | **14,59:1** | sì | Anello di focus su card e campi |
| `--c-focus` #f8efe6 | `--c-page` #1c1412 | focus | 3,0:1 | **15,96:1** | sì | Anello di focus sullo sfondo della pagina |
| `--c-focus` #f8efe6 | `--c-hero-1` #3a2318 | focus | 3,0:1 | **12,89:1** | sì | Anello di focus nell'hero |
| `--c-focus-on-dark` #f4b93e | `--c-promo-from` #7a3010 | focus | 3,0:1 | **5,25:1** | sì | Anello di focus nel riquadro di invito |
| `--c-focus` #f8efe6 | `--c-surface` #2f231f | focus | 3,0:1 | **13,38:1** | sì | Anello di focus nei riquadri |
| `--c-focus` #f8efe6 | `--c-brand-soft` #3a2318 | focus | 3,0:1 | **12,89:1** | sì | Anello di focus nell'hero e nei riquadri informativi |
| `--c-focus` #f8efe6 | `--c-warning-bg` #33270c | focus | 3,0:1 | **12,87:1** | sì | Anello di focus su risposta FAQ evidenziata |
| `--c-focus-on-dark` #f4b93e | `--c-footer-bg` #140d0b | focus | 3,0:1 | **10,86:1** | sì | Anello di focus nel piè di pagina |
| `--c-focus-skip` #a33f0f | `--c-ink` #f8efe6 | focus | 3,0:1 | **5,64:1** | sì | Anello di focus del link «Salta al contenuto» |

Coppie controllate: 90 · sotto soglia: 0.
