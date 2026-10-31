# 07 · Design system di ideaBlume

Tutti gli stili sono in un unico file, `css/ideablume.css` (un solo foglio di stile: meno richieste, P-087). Questo documento spiega i token, i componenti e il problema che ciascuno risolve. I contrasti sono calcolati da `tools/contrasto.py`, che legge i colori direttamente dal CSS: i valori qui sotto non sono scritti a mano.

## 1. Principi

1. **Mai solo il colore** (WCAG 1.4.1; P-022, P-028, P-040; persona P05 con deuteranopia): ogni stato ha testo, icona e colore.
2. **Contrasto prima dell'estetica** (P-034: arancione 2,46:1, verde 2,09:1, footer 2:1 su IdeaGinger): testo ≥ 4,5:1, componenti e focus ≥ 3:1. Nessuna coppia del sistema è sotto soglia.
3. **Leggibile da lontano e con poca attenzione** (P-076; P01, P07, P10): corpo del testo 18 px, mai sotto 16 px, interlinea 1,6, righe di massimo 70 caratteri.
4. **Bersagli grandi** (P01, P12; WCAG 2.5.8): comandi principali alti almeno 44 px, comandi secondari almeno 36 px, voci del menu mobile 48 px.
5. **Nessuna risorsa esterna**: caratteri di sistema, icone in SVG o in testo, nessun CDN (P-087).
6. **Funziona senza JavaScript dove possibile**: accordion con `details`/`summary`, indice con ancore invece di schede a comparsa.

## 2. Colori

Il colore principale è un **prugna** (`#5a2d82`), lontano dall'arancione di IdeaGinger e dal rosso istituzionale dell'Ateneo, per non imitare né l'uno né l'altro (regola 4 del prompt). Il **verde** è riservato all'avanzamento della raccolta, il **giallo** al focus su sfondo scuro e ai segnaposto da verificare.

| Token | Valore | Uso |
|---|---|---|
| `--c-ink` | `#1c1a22` | Testo principale, anello di focus |
| `--c-ink-muted` | `#4b4757` | Testo secondario, suggerimenti |
| `--c-bg` | `#ffffff` | Sfondo della pagina |
| `--c-surface` | `#f6f3fa` | Sezioni e riquadri |
| `--c-surface-2` | `#eee8f5` | Intestazioni di tabella, riquadri annidati |
| `--c-border` | `#d8d1e3` | Separatori decorativi (non portano informazione) |
| `--c-border-strong` | `#6e6680` | Bordi di campi, card, riquadri (componenti: ≥ 3:1) |
| `--c-brand` | `#5a2d82` | Link, pulsanti principali, voce corrente |
| `--c-brand-dark` | `#44205f` | Passaggio del mouse, stato premuto |
| `--c-brand-soft` | `#f1eaf8` | Hero, riquadri informativi, scelta selezionata |
| `--c-progress` / `--c-track` | `#1f6b57` / `#e4dfea` | Barra di avanzamento: raccolto / mancante |
| `--c-st-open-*` | `#0f4c8a` su `#e7f0fa` | Stato «In corso» |
| `--c-st-reached-*` | `#1d5e37` su `#e3f3e8` | Stato «Obiettivo raggiunto · raccolta ancora aperta» |
| `--c-st-done-*` | `#3a3646` su `#eceaf0` | Stato «Conclusa · obiettivo raggiunto»; pulsante disattivato |
| `--c-st-failed-*` | `#8a2b10` su `#fbebe5` | Stato «Conclusa · obiettivo non raggiunto» |
| `--c-error*` | `#b0211a` su `#fdecea` | Errori |
| `--c-success*` | `#1d5e37` su `#e3f3e8` | Conferme |
| `--c-warning*` | `#6a4a00` su `#fff4d1` | Avvisi, segnaposto «[DA VERIFICARE]» |
| `--c-info*` | `#0f4c8a` su `#e7f0fa` | Informazioni |
| `--c-footer-*` | `#ffffff`, `#d9cfe6` su `#2b1840` | Piè di pagina |
| `--c-focus` / `--c-focus-on-dark` | `#1c1a22` / `#ffd34e` | Anello di focus su sfondo chiaro / scuro |

Per la **deuteranopia** (P05) verde «raggiunto» e rosso-bruno «non raggiunto» possono sembrare simili: per questo i quattro stati hanno icone diverse (cerchio vuoto, spunta, quadrato pieno, croce) e il testo è sempre presente. La verifica con la simulazione del daltonismo è prevista nella Fase 4.

## 3. Rapporti di contrasto

Calcolati con la formula della luminanza relativa di WCAG 2.2 su 52 coppie realmente usate; risultato completo in `docs/verifiche/contrasti.md`. Sintesi:

| Coppia | Rapporto | Soglia |
|---|---|---|
| Testo principale su bianco | 17,21:1 | 4,5:1 |
| Testo secondario su bianco / su riquadri | 8,98:1 / 7,48–8,18:1 | 4,5:1 |
| Link (prugna) su bianco / su riquadro prugna chiaro | 9,85:1 / 8,38:1 | 4,5:1 |
| Testo bianco sul pulsante principale | 9,85:1 (12,98:1 al passaggio del mouse) | 4,5:1 |
| Badge «In corso» / «Obiettivo raggiunto» / «Conclusa · raggiunto» / «Conclusa · non raggiunto» | 7,53 / 6,74 / 9,80 / 7,44:1 | 4,5:1 |
| Errore su bianco / su sfondo errore | 6,82:1 / 5,96:1 | 4,5:1 |
| Avviso e segnaposto | 7,37:1 | 4,5:1 |
| Piè di pagina: testo / nota | 16,06:1 / 10,72:1 | 4,5:1 |
| Bordo di campi e card su bianco / su riquadro | 5,42:1 / 4,93:1 | 3:1 |
| Barra: raccolto su mancante / su bianco | 4,86:1 / 6,37:1 | 3:1 |
| Contorno della barra | 4,14:1 | 3:1 |
| Anello di focus su bianco / riquadri / hero | 17,21 / 15,67 / 14,64:1 | 3:1 |
| Anello di focus giallo sul piè di pagina | 11,23:1 | 3:1 |

Il valore più basso tra i testi è 5,96:1 (errore su sfondo errore); tra i componenti 4,14:1. Confronto con IdeaGinger (P-034): titoli arancioni 2,46:1, pulsante verde 2,09:1, grigio 2,85:1, footer ~2:1.

## 4. Tipografia

- **Caratteri**: `system-ui` e alternative di sistema. Nessun font da scaricare (nessun blocco del rendering: su IdeaGinger i font costavano 700 ms, `01_inventario_fonti.md` §3.1).
- **Scala** (rapporto ~1,2, più ampio su desktop):

| Elemento | Mobile | Desktop | Peso |
|---|---|---|---|
| `h1` | 30 px | 40 px | 700 |
| `h2` | 24 px | 28 px | 700 |
| `h3` | 21 px | 22 px | 700 |
| `h4` | 18 px | 18 px | 700 |
| Corpo | 18 px | 18 px | 400 |
| Testo introduttivo (`.lead`) | 20 px | 20 px | 400 |
| Note, legende, badge (`small`) | 16 px | 16 px | 400–700 |

- **Interlinea** 1,6 per il testo, 1,25 per i titoli; **lunghezza della riga** massimo 70 caratteri (`--measure`).
- Le cifre importanti (raccolto, percentuale) sono grandi e in grassetto (P10 con presbiopia, J10-F1).
- Unità in `rem`: il testo segue lo zoom e le impostazioni del browser (WCAG 1.4.4).

## 5. Spaziature e griglia

- Scala a base 4 px: `--s-1` 4 · `--s-2` 8 · `--s-3` 12 · `--s-4` 16 · `--s-5` 24 · `--s-6` 32 · `--s-7` 48 · `--s-8` 64 px.
- Contenitore massimo 1200 px; margini laterali 16 px su mobile, 24 px da 600 px.
- Punti di rottura: **600 px** (2 colonne di card, filtri su 2 colonne), **900 px** (menu orizzontale, ricerca nell'intestazione), **1024 px** (3 colonne di card, colonna laterale fissa nella pagina progetto, filtri su una riga).
- Nessuno scorrimento orizzontale fino a 320 px (WCAG 1.4.10): le tabelle larghe stanno in `.table-wrap` scorrevole, il resto va a capo.

## 6. Componenti

| Componente | Classe | Comportamento e accessibilità | Problemi risolti |
|---|---|---|---|
| Link «Salta al contenuto» | `.skip-link` | Primo elemento focalizzabile, visibile al focus, porta a `main` | P-017 |
| Intestazione | `.site-header`, `.brand` | Logo come unico link alla home; tagline sotto il nome; ricerca; lingua | P-001, P-010, P-005 |
| Menu principale | `.main-nav`, `.nav-toggle` | 7 voci, nessuna tendina; su mobile pulsante «Menu» con `aria-expanded`, Esc chiude, voci nascoste non focalizzabili; voce corrente con `aria-current` e sottolineatura | P-008, P-009, P-085 |
| Briciole di pane | `.breadcrumb` | `nav` con `aria-label`, ultima voce `aria-current="page"` | P-016 |
| Link | `a` | Sempre sottolineati nel testo; esterni con «(sito esterno)» e freccia `.ext` | P-014, P-011 |
| Pulsanti | `.btn`, `--secondary`, `--ghost`, `--small`, `--block` | Altezza ≥ 44 px (piccolo 36 px); `aria-busy` mostra un indicatore di attesa; disattivato con colori dello stato «concluso» | P-039 |
| Card di progetto | `.card` | Un solo link (titolo) esteso a tutta la card; bordo, ombra e sottolineatura al passaggio del mouse; anello di focus su tutta la card | P-029, P-038, P-030, P-026 |
| Badge di stato | `.status--open`, `--reached`, `--done`, `--failed` | Icona SVG diversa per stato + testo + colore + bordo | P-022, P-024, P-028, P-040 |
| Etichetta di categoria | `.tag` | Tema del progetto sulla card | P-030 |
| Barra di avanzamento | `.progress` | Non interattiva, nascosta agli screen reader (`aria-hidden`) perché il valore è già scritto accanto in testo; oltre il 100% resta piena | P-028, P-050 |
| Riquadro di stato | `.statusbox` | Cifre grandi, `dl` con obiettivo, sostenitori, scadenza in data | P-022, P-024, P-030 |
| Riquadro informativo | `.infobox` | Soglie e raddoppio, costi, regole: bordo spesso a sinistra | P-048, P-053, P-071 |
| Segnaposto | `.placeholder` | Evidenzia «[DA VERIFICARE con l'Ateneo]» | Regola 5 del prompt |
| Indice della pagina | `.toc` | `nav` con lista di ancore, su due colonne da 600 px | P-049, P-074 |
| Ricompense | `.rewards`, `.reward` | Righe uniformi: prezzo, titolo, persone che l'hanno scelta, posti; donazione libera evidenziata | P-042, P-045, P-065 |
| Spiegazione a comparsa | `.toggletip` | `button` con «?», `aria-expanded`, pannello sotto il pulsante, Esc chiude | P-044 |
| Accordion | `.accordion` + `details` | Nativo, funziona senza JS; segno +/− visibile; risposta aperta da ancora evidenziata | P-075 |
| Campi di modulo | `.field`, `.choice`, `.input-euro` | Etichetta sempre visibile sopra il campo, suggerimento sotto l'etichetta, «facoltativo» esplicito; radio e caselle native grandi in riquadri cliccabili | P-059, P-067, P-073 |
| Errori | `.field--error`, `.field-error` | Bordo rosso + icona «!» + testo che dice come correggere; nascosto (`hidden`) quando il valore è corretto | P-054, P-077 |
| Avvisi | `.alert--error`, `--success`, `--warning`, `--info` | Bordo e titolo colorati, testo scuro; riepilogo errori con link ai campi | P-054, P-057 |
| Indicatore dei passi | `.steps` | Lista ordinata, passo corrente con `aria-current="step"`, passi completati con spunta | P-057 |
| Riepilogo della donazione | `.summary` | `dl` con totale separato da una linea spessa | P-057, P-063 |
| Tabelle | `table`, `.table-wrap` | `caption`, intestazioni `th`, numeri allineati a destra; budget e numeri delle edizioni in testo | P-045, P-036 |
| Passi numerati | `.howto` | Numeri grandi; ogni passo ha il link all'azione | P-074, P-069 |
| Numeri complessivi | `.figures` | Griglia statica (nessun carosello), calcolati dai dati | P-036, P-037 |
| Filtri | `.filters` | Etichette visibili, modulo `GET` che funziona anche senza JS; conteggio dei risultati in `role="status"` | P-031, P-032 |
| Piè di pagina | `.site-footer` | Blocco «Aiuto» uguale in ogni pagina; nota «prototipo»; focus giallo | P-034, P-080 |
| «Torna su» | `.back-to-top` | Link testuale alla cima del contenuto | P-015 |

### Componenti non usati

- **Schede a comparsa (tab)**: il prompt le cita come alternativa all'indice. Si è scelto l'**indice con ancore**: funziona senza JavaScript, permette di condividere il link a una sezione e di stampare la pagina intera; con le schede il contenuto nascosto non si trova con la ricerca del browser.
- **Caroselli**: esclusi (P-037). Le liste di progetti sono griglie che vanno a capo.

## 7. Icone e immagini

- Segno del marchio: `img/ideablume-segno.svg`, un fiore stilizzato originale (cinque petali prugna, centro giallo). Decorativo: il nome «ideaBlume» è sempre scritto accanto in testo.
- Icone di stato: SVG in linea con `aria-hidden="true"`; il significato è nel testo.
- Illustrazioni dei progetti: SVG leggeri generati per il prototipo, con dimensioni dichiarate (`width`/`height`) per evitare spostamenti del layout (CLS) e `loading="lazy"` sotto la piega. Testo alternativo descrittivo nella pagina del progetto, vuoto nelle card (l'immagine è decorativa lì: il titolo dice già tutto, P-012).

## 8. Movimento e stampa

- Transizioni brevi (150 ms) solo su card e pulsanti; con `prefers-reduced-motion: reduce` tutte le animazioni sono disattivate.
- Stili di stampa: intestazione, menu e pulsanti nascosti; utile per il riepilogo della donazione e della richiesta di collaborazione (P12, J12-F6).
