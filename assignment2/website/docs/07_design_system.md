# 07 · Design system di ideaBlume (versione 2)

La versione 2 è un **redesign visivo** del sito: stessa architettura, stessi contenuti, stesse classi CSS e stesse interazioni della versione 1, con un linguaggio grafico più attuale (tipografia espressiva, superfici in rilievo, angoli arrotondati, tema scuro). Le motivazioni sono in `decisioni.md` (D-35–D-39).

Gli stili sono in `css/ideablume.css`; i font in `css/font.css` (server) e `css/font-locali.css` (apertura da `file://`, generato dalla build). Questo documento spiega i token, i componenti e il problema che ciascuno risolve. I contrasti sono calcolati da `tools/contrasto.py`, che legge i colori direttamente dal CSS per **entrambi i temi**: i valori qui sotto vengono da `docs/verifiche/contrasti.md`, non sono scritti a mano.

## 1. Principi

1. **Mai solo il colore** (WCAG 1.4.1; P-022, P-028, P-040; persona P05 con deuteranopia): ogni stato ha testo, icona e colore; i link restano sottolineati.
2. **Contrasto prima dell'estetica** (P-034): testo ≥ 4,5:1, componenti e focus ≥ 3:1, **in tema chiaro e in tema scuro**. Nessuna delle 75 coppie × 2 temi è sotto soglia.
3. **Leggibile da lontano e con poca attenzione** (P-076; P01, P07, P10): corpo del testo 18 px, mai sotto 16 px nei testi informativi, interlinea 1,6, righe di massimo 68 caratteri.
4. **Bersagli grandi** (P01, P12; WCAG 2.5.8): comandi principali alti almeno 44 px (i pulsanti grandi 52 px), comandi secondari almeno 36 px, voci del menu mobile 48 px.
5. **Nessuna richiesta a terzi**: i font open source sono ospitati nel sito (nessun CDN, nessun tracciamento), le icone sono SVG in linea (P-087).
6. **Funziona senza JavaScript dove possibile**: accordion con `details`/`summary`, indice con ancore; senza JavaScript i font si caricano comunque (`<noscript>`).
7. **Rilievo con moderazione**: le superfici in rilievo (card bianche con ombra su una pagina leggermente tinta) separano i blocchi senza bordi pesanti; le ombre non portano informazione.

## 2. Colori

Il colore principale resta il **viola prugna** (`#5b2c90`, leggermente più saturo della versione 1), lontano dall'arancione di IdeaGinger e dal rosso dell'Ateneo. Il **verde** è riservato all'avanzamento della raccolta, il **giallo** del fiore (`--c-accent`) alla decorazione, ai numeri sulla fascia scura e al focus su sfondo scuro.

| Token | Chiaro | Scuro | Uso |
|---|---|---|---|
| `--c-ink` | `#1b1525` | `#f2eef8` | Testo principale, anello di focus |
| `--c-ink-muted` | `#554e66` | `#b9b0c9` | Testo secondario, suggerimenti |
| `--c-page` | `#f8f6fb` | `#120e19` | Sfondo della pagina |
| `--c-bg` | `#ffffff` | `#1b1525` | Card, campi, riquadri in rilievo |
| `--c-surface` / `--c-surface-2` | `#f3eff9` / `#e9e2f4` | `#211a2e` / `#2c2340` | Sezioni tinte, intestazioni di tabella |
| `--c-border` | `#e4ddee` | `#30283f` | Bordi decorativi di card e riquadri (non portano informazione) |
| `--c-border-strong` | `#776f8d` | `#8d83a3` | Bordi di campi e controlli (componenti: ≥ 3:1) |
| `--c-brand` | `#5b2c90` | `#c9a8f5` | Link, pulsanti principali, voce corrente |
| `--c-brand-dark` | `#43206b` | `#e2d1fb` | Passaggio del mouse (nel tema scuro più chiaro) |
| `--c-brand-soft` | `#efe7fa` | `#2a1f3f` | Riquadri informativi, scelta selezionata, etichette |
| `--c-on-brand` | `#ffffff` | `#1b1028` | Testo sui pulsanti principali |
| `--c-hero-1` / `--c-hero-2` | `#e9dcfb` / `#fff0c4` | `#2c1d48` / `#2a2210` | Sfumature dell'hero (il testo sopra è verificato) |
| `--c-progress` / `--c-track` | `#1d7356` / `#e6e0ee` | `#4cc59a` / `#342b47` | Barra di avanzamento: raccolto / mancante |
| `--c-st-*` | come v1 | toni chiari su fondi scuri | I quattro stati delle campagne |
| `--c-error*`, `--c-success*`, `--c-warning*`, `--c-info*` | come v1 | toni chiari su fondi scuri | Messaggi; `warning` anche per «[DA VERIFICARE]» |
| `--c-footer-*` | `#ffffff`, `#cfc3df`, `#d7c0f7` su `#1f1230` | su `#0c0911` | Piè di pagina e fascia dei numeri |
| `--c-promo-*` | `#5b2c90` → `#2a1545`, testo bianco | `#4a2479` → `#1d0f30` | Riquadro di invito in fondo alla home |
| `--c-focus` / `--c-focus-on-dark` | `#1b1525` / `#ffd34e` | `#f2eef8` / `#ffd34e` | Anello di focus su sfondo chiaro / scuro |

**Tema scuro.** Si attiva da solo quando il sistema operativo lo chiede (`prefers-color-scheme: dark`); non c'è un interruttore, per non aggiungere un comando all'intestazione. Tutti i colori passano dai token, quindi ogni componente cambia insieme. Le illustrazioni dei progetti (fondi chiari) vengono leggermente attenuate (`--img-filter`) per non abbagliare.

Per la **deuteranopia** (P05) verde «raggiunto» e rosso-bruno «non raggiunto» possono sembrare simili: i quattro stati hanno icone diverse (cerchio vuoto, spunta, quadrato pieno, croce) e il testo è sempre presente.

## 3. Rapporti di contrasto

Calcolati con la formula della luminanza relativa di WCAG 2.2 su 75 coppie realmente usate, per ciascun tema; risultato completo in `docs/verifiche/contrasti.md`. Sintesi:

| Coppia | Chiaro | Scuro | Soglia |
|---|---|---|---|
| Testo principale su card | 17,79:1 | 15,55:1 | 4,5:1 |
| Testo secondario | 7,87:1 | 8,57:1 | 4,5:1 |
| Testo dell'hero sulla sfumatura viola / sottotitolo | 13,63:1 / 6,55:1 | — | 4,5:1 |
| Link e pulsante secondario | 9,51:1 | 8,81:1 | 4,5:1 |
| Testo del pulsante principale | 9,51:1 | 9,04:1 | 4,5:1 |
| Percentuale raggiunta (verde) | 5,77:1 | 8,27:1 | 4,5:1 |
| Badge «In corso» / «Conclusa · non raggiunto» | 7,53 / 7,44:1 | 8,26 / 8,44:1 | 4,5:1 |
| Errore sotto il campo | 6,82:1 | 8,07:1 | 4,5:1 |
| Avviso e segnaposto «[DA VERIFICARE]» | 7,37:1 | 10,31:1 | 4,5:1 |
| Piè di pagina: testo / numeri gialli della fascia | 17,68 / 12,36:1 | — | 4,5:1 |
| Testo del riquadro di invito | 9,51:1 | — | 4,5:1 |
| Bordo di campi e controlli | 4,73:1 | 5,00:1 | 3:1 |
| Barra: raccolto su mancante | 4,47:1 | 6,17:1 | 3:1 |
| Anello di focus su card e campi | 17,79:1 | 15,55:1 | 3:1 |

Valori più bassi: testo 5,67:1 (chiaro) e 6,18:1 (scuro), entrambi per il testo chiaro della fascia scura nella zona della sfumatura viola; componenti e focus 3,62:1 (bordo del campo di ricerca sulla sfumatura dell'hero) e 3,37:1 (anello del link «Salta al contenuto» nel tema scuro). Confronto con IdeaGinger (P-034): titoli arancioni 2,46:1, pulsante verde 2,09:1, footer ~2:1.

**Bordi delle card.** Nella versione 1 le card avevano un bordo ≥ 3:1. Nella versione 2 il bordo è decorativo (`--c-border`) e la card si distingue per il fondo bianco in rilievo e l'ombra. Non serve un bordo a contrasto perché la card non è un controllo: il controllo è il titolo-link, sottolineato al passaggio del mouse, e al focus l'intera card riceve l'anello di focus a 3 px (WCAG 1.4.11 e 2.4.7 restano soddisfatti).

## 4. Tipografia

- **Caratteri**: **Inter** (testo e interfaccia, molto leggibile anche piccolo, cifre chiare) e **Bricolage Grotesque** (titoli, cifre grandi, marchio: dà al sito un carattere riconoscibile). Entrambi open source (SIL OFL 1.1, licenze in `fonts/`), variabili, sottoinsieme latino, circa 90 KB in tutto in `woff2`.
- **Caricamento**: su server i due file sono precaricati e le `@font-face` sono scritte in linea nel `<head>` (nessuna richiesta bloccante in più); `font-display: swap` mostra subito il testo con un carattere di riserva dalle metriche corrette (`Inter Fallback`, CLS 0 nelle misure). Da `file://` i browser bloccano i file di font: lo script nel `<head>` carica allora `css/font-locali.css`, con i font incorporati. Se un font non arriva, il sito usa i caratteri di sistema senza perdere nulla.
- **Scala**:

| Elemento | Mobile | Desktop | Peso |
|---|---|---|---|
| `h1` dell'hero | 38 px | fino a 68 px | 750 |
| `h1` delle pagine | 36 px | 48 px | 750 |
| `h2` | 28 px | 34 px | 700 |
| `h3` | 22 px | 24 px | 700 |
| Corpo | 18 px | 18 px | 400 |
| Testo introduttivo (`.lead`) | 19 px | 21 px | 400 |
| Note, legende, badge | 15–16 px | 15–16 px | 500–700 |

- Badge, metadati delle card ed etichette sono a 15 px (`.9375rem`): sono sempre accompagnati da testo più grande che dice la stessa cosa (titolo, stato, importo). Il corpo del testo e i testi informativi restano a 18 e 16 px.
- **Interlinea** 1,6 per il testo, 1,15 per i titoli; titoli con `text-wrap: balance`, paragrafi con `text-wrap: pretty`.
- Unità in `rem`: il testo segue lo zoom e le impostazioni del browser (WCAG 1.4.4).

## 5. Spaziature, forme e griglia

- Scala a base 4 px: `--s-1` 4 · `--s-2` 8 · `--s-3` 12 · `--s-4` 16 · `--s-5` 24 · `--s-6` 32 · `--s-7` 48 · `--s-8` 64 · `--s-9` 96 px.
- **Raggi**: 10 px (campi, badge), 16 px (riquadri, ricompense, FAQ), 24 px (card, riquadro di stato), 32 px (riquadro di invito); pulsanti, etichette e ricerca a pillola.
- **Ombre** su tre livelli (`--shadow-sm`, `--shadow`, `--shadow-lg`) tinte di viola nel tema chiaro, nere nel tema scuro.
- Contenitore massimo 1216 px; margini laterali 16 px su mobile, 32 px da 600 px.
- Punti di rottura: **600 px** (2 colonne di card), **900 px** (menu orizzontale, intestazione fissa, passi della home su 3 colonne), **1024 px** (3 colonne di card, hero a due colonne, colonna laterale nella pagina progetto, filtri su 3 colonne).
- Nessuno scorrimento orizzontale fino a 320 px (WCAG 1.4.10).

## 6. Componenti

| Componente | Classe | Comportamento e accessibilità | Problemi risolti |
|---|---|---|---|
| Link «Salta al contenuto» | `.skip-link` | Primo elemento focalizzabile, visibile al focus, porta a `main` | P-017 |
| Intestazione | `.site-header`, `.brand` | Fondo semitrasparente sfocato. Da 900 px la riga del marchio scorre via e **la riga del menu resta fissa in alto**; `scroll-padding-top` evita che il focus finisca sotto l'intestazione (WCAG 2.4.11). Su telefono: marchio, lingua («EN»/«IT» con icona) e «Menu» su una riga, ricerca sempre visibile sotto (D-25, D-36) | P-001, P-010, P-005 |
| Marchio | `.brand__mark` | Il fiore è SVG in linea colorato dai token (si adatta al tema scuro); ruota al passaggio del mouse | — |
| Ricerca | `.search-form` | Un'unica «pillola» con icona, campo e pulsante «Cerca»; il focus del campo evidenzia tutta la pillola | P-005 |
| Menu principale | `.main-nav`, `.nav-toggle` | 7 voci a pillola, nessuna tendina; su mobile pulsante «Menu» con `aria-expanded`, Esc chiude; voce corrente con `aria-current`, fondo e sottolineatura | P-008, P-009, P-085 |
| Briciole di pane | `.breadcrumb` | `nav` con `aria-label`, separatori disegnati in CSS, ultima voce `aria-current="page"` | P-016 |
| Link | `a` | Sempre sottolineati (sottolineatura tenue che si intensifica al passaggio del mouse); esterni con «(sito esterno)» e freccia | P-014, P-011 |
| Link con freccia | `.link-arrow` | Link isolati («Tutti i progetti», «Come funziona nel dettaglio») con freccia che si sposta al passaggio del mouse; alti 44 px | P-074 |
| Pulsanti | `.btn`, `--secondary`, `--ghost`, `--light`, `--large`, `--small`, `--block` | A pillola; altezza ≥ 44 px (grande 52 px, piccolo 36 px); leggero sollevamento al passaggio del mouse; `aria-busy` mostra l'attesa | P-039 |
| Hero della home | `.hero`, `.eyebrow`, `.hero__chips`, `.hero__feature` | Due colonne su desktop: titolo, ricerca grande, due azioni, tre punti chiave con spunta; a destra il **progetto in evidenza** (campagna non ancora riuscita più vicina alla scadenza), con una card vera e cliccabile | P-001, P-003, P-005 |
| Card di progetto | `.card` | Un solo link (titolo) esteso a tutta la card; al passaggio del mouse si solleva e l'immagine si ingrandisce appena; anello di focus su tutta la card | P-029, P-038, P-030, P-026 |
| Badge di stato | `.status--open`, `--reached`, `--done`, `--failed` | Icona SVG diversa per stato + testo + colore + bordo | P-022, P-024, P-028, P-040 |
| Etichetta | `.tag`, `.count-pill` | Categoria, programma, numero di elementi accanto ai titoli | P-030 |
| Barra di avanzamento | `.progress` | Non interattiva, `aria-hidden` (il valore è scritto accanto); oltre il 100% resta piena | P-028, P-050 |
| Riquadro di stato | `.statusbox` | Card in rilievo; cifra raccolta grande in Bricolage, percentuale in verde, righe sostenitori/inizio/scadenza con separatori, «Sostieni» a tutta larghezza | P-022, P-024, P-030 |
| Riquadro informativo | `.infobox` | Fondo viola chiaro con barra a sinistra: soglie e raddoppio, costi, regole | P-048, P-053, P-071 |
| Segnaposto | `.placeholder` | Evidenzia «[DA VERIFICARE con l'Ateneo]», anche quando va a capo | Regola 5 del prompt |
| Indice della pagina | `.toc` | Card con lista numerata di ancore, su due colonne da 600 px | P-049, P-074 |
| Gruppo di ricerca | `.team` | Persone in piccole card su due colonne: nome in evidenza, ruolo sotto | P-030 |
| Ricompense | `.rewards`, `.reward` | Una card per ricompensa: prezzo grande, titolo, persone che l'hanno scelta, posti; donazione libera con bordo tratteggiato | P-042, P-045, P-065 |
| Spiegazione a comparsa | `.toggletip` | `button` con «?», `aria-expanded`, pannello sotto il pulsante, Esc chiude | P-044 |
| Accordion | `.accordion` + `details` | Nativo, funziona senza JS; una card per domanda; «+» che ruota in «×» all'apertura; risposta aperta da ancora evidenziata | P-075 |
| Campi di modulo | `.field`, `.choice`, `.input-euro` | Etichetta sempre visibile sopra il campo, suggerimento sotto l'etichetta, «facoltativo» esplicito; menu a tendina con freccia uniforme; radio e caselle native in riquadri cliccabili | P-059, P-067, P-073 |
| Errori | `.field--error`, `.field-error` | Bordo rosso + icona «!» + testo che dice come correggere | P-054, P-077 |
| Avvisi | `.alert--error`, `--success`, `--warning`, `--info` | Fondo tenue, barra colorata a sinistra, titolo colorato, testo scuro | P-054, P-057 |
| Indicatore dei passi | `.steps` | Pillole numerate, passo corrente con `aria-current="step"` evidenziato, passi completati con spunta | P-057 |
| Riepilogo della donazione | `.summary` | Card con `dl` e totale separato da una linea spessa | P-057, P-063 |
| Tabelle | `table`, `.table-wrap` | Card con bordo arrotondato, scorrevole su mobile; `caption`, `th`, numeri allineati a destra | P-045, P-036 |
| Passi numerati | `.howto`, `.howto--cards` | Numeri in cerchio collegati da una linea verticale; nella home tre card affiancate | P-074, P-069 |
| Numeri complessivi | `.band`, `.figures` | Fascia scura a tutta larghezza con cifre grandi in giallo; statica (nessun carosello) | P-036, P-037 |
| Riquadro di invito | `.promo` | Sfumatura viola con fiore decorativo; pulsante chiaro | — |
| Filtri | `.filters` | Card con etichette visibili, modulo `GET` che funziona anche senza JS; conteggio in `role="status"` | P-031, P-032 |
| Piè di pagina | `.site-footer` | Marchio, blocco «Aiuto» uguale in ogni pagina, titoli delle colonne in maiuscoletto, nota «prototipo»; focus giallo | P-034, P-080 |
| «Torna su» | `.back-to-top` | Link testuale alla cima del contenuto | P-015 |

### Componenti non usati

- **Schede a comparsa (tab)**: si è scelto l'**indice con ancore** (funziona senza JavaScript, link condivisibili a una sezione, stampa completa, contenuto trovabile con la ricerca del browser).
- **Caroselli**: esclusi (P-037). Le liste di progetti sono griglie che vanno a capo.
- **Framework CSS (Tailwind, Bootstrap) e librerie JS di interfaccia**: valutati per il redesign e scartati (D-35).

## 7. Icone e immagini

- Segno del marchio: un fiore stilizzato originale (cinque petali, centro giallo), SVG in linea nell'intestazione e nel piè di pagina; `img/ideablume-segno.svg` resta come favicon. Le decorazioni grandi (dietro il progetto in evidenza e nel riquadro di invito) usano la sua sagoma come maschera CSS incorporata. Tutto decorativo: il nome «ideaBlume» è sempre scritto in testo.
- Icone dell'interfaccia (lente, freccia, spunta, globo, menu): SVG in linea a tratto arrotondato, `aria-hidden="true"`; il significato è sempre nel testo accanto.
- Illustrazioni dei progetti: SVG leggeri generati per il prototipo, con dimensioni dichiarate (`width`/`height`) e `loading="lazy"` sotto la piega. Testo alternativo descrittivo nella pagina del progetto, vuoto nelle card (P-012).

## 8. Movimento e stampa

- Transizioni brevi (150–500 ms) su card, pulsanti, frecce, accordion e marchio; il badge «sostenitori finora» dell'hero oscilla lentamente (solo da 1100 px). Con `prefers-reduced-motion: reduce` tutte le animazioni sono disattivate.
- Nessuna animazione di comparsa allo scorrimento: il contenuto è sempre visibile subito (niente testo trasparente durante le verifiche di contrasto, niente attese per chi legge).
- Stili di stampa: intestazione, menu e pulsanti nascosti, ombre e fondi tolti; utile per il riepilogo della donazione e della richiesta di collaborazione (P12, J12-F6).
