# Contrasti del design system

Generato da `tools/contrasto.py` a partire dai token di `css/ideablume.css`.
Soglie WCAG 2.2: testo normale 4,5:1 (1.4.3); testo grande, componenti dell'interfaccia e indicatori di focus 3:1 (1.4.11).

| Primo piano | Sfondo | Tipo | Soglia | Rapporto | Supera | Dove si usa |
|---|---|---|---|---|---|---|
| `--c-ink` #1c1a22 | `--c-bg` #ffffff | testo | 4,5:1 | **17,21:1** | sì | Testo principale |
| `--c-ink` #1c1a22 | `--c-surface` #f6f3fa | testo | 4,5:1 | **15,67:1** | sì | Testo in sezioni e riquadri |
| `--c-ink` #1c1a22 | `--c-surface-2` #eee8f5 | testo | 4,5:1 | **14,34:1** | sì | Intestazioni di tabella, riquadri annidati |
| `--c-ink` #1c1a22 | `--c-brand-soft` #f1eaf8 | testo | 4,5:1 | **14,64:1** | sì | Testo nell'hero e nei riquadri informativi |
| `--c-ink-muted` #4b4757 | `--c-bg` #ffffff | testo | 4,5:1 | **8,98:1** | sì | Testo secondario, suggerimenti dei campi |
| `--c-ink-muted` #4b4757 | `--c-surface` #f6f3fa | testo | 4,5:1 | **8,18:1** | sì | Testo secondario nei riquadri |
| `--c-ink-muted` #4b4757 | `--c-surface-2` #eee8f5 | testo | 4,5:1 | **7,48:1** | sì | Testo secondario nei riquadri annidati |
| `--c-ink-muted` #4b4757 | `--c-brand-soft` #f1eaf8 | testo | 4,5:1 | **7,64:1** | sì | Sottotitolo nell'hero |
| `--c-brand` #5a2d82 | `--c-bg` #ffffff | testo | 4,5:1 | **9,85:1** | sì | Link, titoli in colore, pulsante secondario |
| `--c-brand` #5a2d82 | `--c-surface` #f6f3fa | testo | 4,5:1 | **8,97:1** | sì | Link nei riquadri |
| `--c-brand` #5a2d82 | `--c-brand-soft` #f1eaf8 | testo | 4,5:1 | **8,38:1** | sì | Voce di menu corrente, link nei riquadri informativi |
| `--c-brand-dark` #44205f | `--c-brand-soft` #f1eaf8 | testo | 4,5:1 | **11,04:1** | sì | Link e menu al passaggio del mouse, etichette di categoria |
| `--c-brand-dark` #44205f | `--c-bg` #ffffff | testo | 4,5:1 | **12,98:1** | sì | Link al passaggio del mouse |
| `--c-on-brand` #ffffff | `--c-brand` #5a2d82 | testo | 4,5:1 | **9,85:1** | sì | Testo del pulsante principale |
| `--c-on-brand` #ffffff | `--c-brand-dark` #44205f | testo | 4,5:1 | **12,98:1** | sì | Pulsante principale al passaggio del mouse |
| `--c-st-open-fg` #0f4c8a | `--c-st-open-bg` #e7f0fa | testo | 4,5:1 | **7,53:1** | sì | Badge «In corso» |
| `--c-st-reached-fg` #1d5e37 | `--c-st-reached-bg` #e3f3e8 | testo | 4,5:1 | **6,74:1** | sì | Badge «Obiettivo raggiunto» |
| `--c-st-done-fg` #3a3646 | `--c-st-done-bg` #eceaf0 | testo | 4,5:1 | **9,80:1** | sì | Badge «Conclusa · obiettivo raggiunto»; pulsante disattivato |
| `--c-st-failed-fg` #8a2b10 | `--c-st-failed-bg` #fbebe5 | testo | 4,5:1 | **7,44:1** | sì | Badge «Conclusa · obiettivo non raggiunto» |
| `--c-error` #b0211a | `--c-bg` #ffffff | testo | 4,5:1 | **6,82:1** | sì | Messaggio di errore sotto il campo |
| `--c-error` #b0211a | `--c-error-bg` #fdecea | testo | 4,5:1 | **5,96:1** | sì | Titolo del riepilogo errori |
| `--c-ink` #1c1a22 | `--c-error-bg` #fdecea | testo | 4,5:1 | **15,05:1** | sì | Testo del riepilogo errori |
| `--c-success` #1d5e37 | `--c-success-bg` #e3f3e8 | testo | 4,5:1 | **6,74:1** | sì | Messaggio di conferma |
| `--c-ink` #1c1a22 | `--c-success-bg` #e3f3e8 | testo | 4,5:1 | **14,96:1** | sì | Testo nella conferma |
| `--c-warning` #6a4a00 | `--c-warning-bg` #fff4d1 | testo | 4,5:1 | **7,37:1** | sì | Avviso e segnaposto [DA VERIFICARE] |
| `--c-ink` #1c1a22 | `--c-warning-bg` #fff4d1 | testo | 4,5:1 | **15,66:1** | sì | Testo negli avvisi; risposta FAQ evidenziata |
| `--c-info` #0f4c8a | `--c-info-bg` #e7f0fa | testo | 4,5:1 | **7,53:1** | sì | Avviso informativo |
| `--c-ink` #1c1a22 | `--c-info-bg` #e7f0fa | testo | 4,5:1 | **14,95:1** | sì | Testo negli avvisi informativi |
| `--c-footer-fg` #ffffff | `--c-footer-bg` #2b1840 | testo | 4,5:1 | **16,06:1** | sì | Testo e link del piè di pagina |
| `--c-footer-muted` #d9cfe6 | `--c-footer-bg` #2b1840 | testo | 4,5:1 | **10,72:1** | sì | Nota «prototipo» nel piè di pagina |
| `--c-footer-bg` #2b1840 | `--c-footer-fg` #ffffff | testo | 4,5:1 | **16,06:1** | sì | Pulsante «Scrivici» nel piè di pagina |
| #ffffff | `--c-ink` #1c1a22 | testo | 4,5:1 | **17,21:1** | sì | Link «Salta al contenuto»; «?» delle spiegazioni a comparsa |
| #ffffff | `--c-brand` #5a2d82 | testo | 4,5:1 | **9,85:1** | sì | Numero del passo corrente; numeri di «Come funziona» |
| #ffffff | `--c-progress` #1f6b57 | componente | 3,0:1 | **6,37:1** | sì | Spunta dei passi completati |
| #ffffff | `--c-error` #b0211a | componente | 3,0:1 | **6,82:1** | sì | Icona «!» degli errori |
| `--c-border-strong` #6e6680 | `--c-bg` #ffffff | componente | 3,0:1 | **5,42:1** | sì | Bordo di campi, card, riquadri |
| `--c-border-strong` #6e6680 | `--c-surface` #f6f3fa | componente | 3,0:1 | **4,93:1** | sì | Bordo dei campi nei riquadri dei filtri |
| `--c-progress` #1f6b57 | `--c-track` #e4dfea | componente | 3,0:1 | **4,86:1** | sì | Parte raccolta della barra rispetto alla parte mancante |
| `--c-progress` #1f6b57 | `--c-bg` #ffffff | componente | 3,0:1 | **6,37:1** | sì | Barra piena rispetto allo sfondo |
| `--c-border-strong` #6e6680 | `--c-track` #e4dfea | componente | 3,0:1 | **4,14:1** | sì | Contorno della barra (la traccia ha anche un bordo) |
| `--c-brand` #5a2d82 | `--c-bg` #ffffff | componente | 3,0:1 | **9,85:1** | sì | Bordo del pulsante secondario e della scelta selezionata |
| `--c-error` #b0211a | `--c-bg` #ffffff | componente | 3,0:1 | **6,82:1** | sì | Bordo dei campi con errore |
| `--c-st-open-fg` #0f4c8a | `--c-bg` #ffffff | componente | 3,0:1 | **8,67:1** | sì | Bordo dei badge sullo sfondo della card |
| `--c-st-reached-fg` #1d5e37 | `--c-bg` #ffffff | componente | 3,0:1 | **7,75:1** | sì | Bordo dei badge sullo sfondo della card |
| `--c-st-done-fg` #3a3646 | `--c-bg` #ffffff | componente | 3,0:1 | **11,69:1** | sì | Bordo dei badge sullo sfondo della card |
| `--c-st-failed-fg` #8a2b10 | `--c-bg` #ffffff | componente | 3,0:1 | **8,63:1** | sì | Bordo dei badge sullo sfondo della card |
| `--c-focus` #1c1a22 | `--c-bg` #ffffff | focus | 3,0:1 | **17,21:1** | sì | Anello di focus su sfondo bianco |
| `--c-focus` #1c1a22 | `--c-surface` #f6f3fa | focus | 3,0:1 | **15,67:1** | sì | Anello di focus nei riquadri |
| `--c-focus` #1c1a22 | `--c-brand-soft` #f1eaf8 | focus | 3,0:1 | **14,64:1** | sì | Anello di focus nell'hero e nei riquadri informativi |
| `--c-focus` #1c1a22 | `--c-warning-bg` #fff4d1 | focus | 3,0:1 | **15,66:1** | sì | Anello di focus su risposta FAQ evidenziata |
| `--c-focus-on-dark` #ffd34e | `--c-footer-bg` #2b1840 | focus | 3,0:1 | **11,23:1** | sì | Anello di focus nel piè di pagina |
| `--c-focus-on-dark` #ffd34e | `--c-ink` #1c1a22 | focus | 3,0:1 | **12,03:1** | sì | Anello di focus del link «Salta al contenuto» |

Coppie controllate: 52 · sotto soglia: 0.
