# 07 · Design system di ideaBlume (versione 3)

La versione 3 sostituisce la palette viola con una **palette calda da campagna di raccolta fondi** e introduce la **scelta tra tema chiaro e tema scuro**: stessa architettura e stesse classi CSS della versione 2. Le motivazioni sono in `decisioni.md` (D-35–D-41).

Gli stili sono in `css/ideablume.css`; i font in `css/font.css` (server) e `css/font-locali.css` (apertura da `file://`, generato dalla build). Questo documento spiega i token, i componenti e il problema che ciascuno risolve. I contrasti sono calcolati da `tools/contrasto.py`, che legge i colori direttamente dal CSS per **entrambi i temi**: i valori qui sotto vengono da `docs/verifiche/contrasti.md`, non sono scritti a mano.

## 1. Principi

1. **Mai solo il colore** (WCAG 1.4.1; P-022, P-028, P-040; persona P05 con deuteranopia): ogni stato ha testo, icona e colore; i link restano sottolineati.
2. **Contrasto prima dell'estetica** (P-034): testo ≥ 4,5:1, componenti e focus ≥ 3:1, **in tema chiaro e in tema scuro**. Nessuna delle 90 coppie × 2 temi è sotto soglia.
3. **Leggibile da lontano e con poca attenzione** (P-076; P01, P07, P10): corpo del testo 18 px, mai sotto 16 px nei testi informativi, interlinea 1,6, righe di massimo 68 caratteri.
4. **Bersagli grandi** (P01, P12; WCAG 2.5.8): comandi principali alti almeno 44 px (i pulsanti grandi 52 px), comandi secondari almeno 36 px, voci del menu mobile 48 px.
5. **Nessuna richiesta a terzi**: i font open source sono ospitati nel sito (nessun CDN, nessun tracciamento), le icone sono SVG in linea (P-087).
6. **Funziona senza JavaScript dove possibile**: accordion con `details`/`summary`, indice con ancore; senza JavaScript i font si caricano comunque (`<noscript>`).
7. **Rilievo con moderazione**: le superfici in rilievo (card bianche con ombra su una pagina leggermente tinta) separano i blocchi senza bordi pesanti; le ombre non portano informazione.

## 2. Colori

Il tono è caldo e accogliente: ispira fiducia e invita a donare senza aggressività. Il fondo crema e la prugna bruna fanno da base tranquilla; l'**arancio terracotta** è riservato all'azione di donare e all'avanzamento, così resta il punto più visibile della pagina; il **verde bosco** indica solo ciò che è confermato o raggiunto.

| Ruolo | Nome | Chiaro | Scuro | Uso | Contrasto chiaro / scuro |
|---|---|---|---|---|---|
| Primario (`--c-ink`, `--c-primary`, `--c-footer-bg`) | Prugna bruna | `#3b1d2a` | `#f8efe6` (fondo `#140d0b` nel piè di pagina) | Testi principali, testi dell'intestazione, piè di pagina, pulsanti normali | 13,99:1 / 15,96:1 sulla pagina |
| Accento CTA (`--c-cta`, `--c-progress`) | Arancio terracotta | `#bf4a12` | `#f58b4a` | «Sostieni il progetto», pagamento, barra di avanzamento | testo sul pulsante 5,00:1 / 7,31:1 |
| Secondario (`--c-secondary`) | Verde bosco | `#24603f` | `#7fd6a3` | Badge «obiettivo raggiunto», icone di conferma | 6,42:1 / 8,17:1 sul badge |
| Sfondo (`--c-page`) | Crema | `#fbf6ee` | `#1c1412` | Sfondo della pagina | — |
| Superficie (`--c-bg`) | Panna | `#fffdf9` | `#271c19` | Card delle ricompense, box dei finanziatori, campi | testo 14,82:1 / 14,59:1 |
| Testo secondario (`--c-ink-muted`) | Moka | `#66544a` | `#cdbcae` | Descrizioni, note legali, suggerimenti | 6,66:1 / 9,84:1 sulla pagina |
| Supporto: evidenziazioni (`--c-accent`, `--c-warning-bg`) | Giallo miele | `#f4b93e` | `#f4b93e` | Cuore del fiore, numeri sulla fascia scura, risposta FAQ evidenziata | 8,50:1 / — sul fondo scuro |
| Supporto: avvisi ed errori (`--c-error`) | Rosso mattone | `#a3271a` | `#ff9e8c` | Errori dei moduli, avvisi bloccanti | 6,25:1 / 8,02:1 sul suo fondo |
| Supporto: sezioni informative (`--c-info`, `--c-st-open-*`) | Blu petrolio | `#1d5b73` | `#8fcbe0` | Riquadri informativi, badge «In corso» | 6,40:1 / 7,80:1 sul suo fondo |

Derivati: `--c-brand` (`#a33f0f` / `#ffb27a`) è l'accento scurito per link e marchio, perché regge il testo piccolo anche sui fondi tinti; `--c-brand-soft` (`#fbeadd` / `#3a2318`) è il fondo della scelta selezionata e dei riquadri del raddoppio; `--c-warning` (`#7a4d00` / `#f7cf77`) è il miele scurito per il testo degli avvisi.

**Bianco su arancio.** Il bianco non basta sull'arancio vivo: 2,45:1 su `#f28c28`, 2,80:1 su `#f97316`, 3,58:1 su `#e8590c`. Per questo nel tema chiaro l'accento è scurito fino al terracotta `#bf4a12`, che con il bianco arriva a 5,00:1 e resta caldo. Nel tema scuro l'arancio può tornare vivo (`#f58b4a`), ma il testo diventa scuro (`#2a1205`, 7,31:1): il bianco su quel colore sarebbe sotto 2,5:1.

### Abbinamenti (chiaro / scuro)

- **Pulsante «Sostieni il progetto»** (`.btn--cta`): sfondo `#bf4a12` / `#f58b4a`; testo `#ffffff` / `#2a1205`; bordo uguale allo sfondo. Al passaggio del mouse: `#9e3b0c` / `#ffa66e`.
- **Pulsante normale** (`.btn`): sfondo `#3b1d2a` / `#f8efe6`; testo `#fff8f0` / `#2a1a17`; bordo uguale allo sfondo.
- **Barra di avanzamento**: parte raccolta `#bf4a12` / `#f58b4a`; parte mancante `#eadfd3` / `#4a3a33`; nessun bordo (3,80:1 / 4,46:1 tra le due parti); il dato è sempre scritto accanto in cifre.
- **Card ricompensa selezionata** (`.choice:has(input:checked)`): sfondo `#fbeadd` / `#3a2318`; testo `#3b1d2a` / `#f8efe6`; bordo `#bf4a12` / `#f58b4a` (4,26:1 / 6,05:1) più il pallino del controllo.
- **Badge «Obiettivo raggiunto»**: sfondo `#e3f2e6` / `#15301f`; testo e icona `#24603f` / `#7fd6a3`; bordo dello stesso colore del testo.

**Tema chiaro e scuro.** Il tema predefinito è quello chiaro, anche se il sistema operativo è in scuro. L'interruttore è nell'intestazione, accanto alla lingua: la scelta è salvata in `localStorage` (`ib-tema`) e vale per tutte le pagine e le lingue; uno script nel `<head>` la applica prima del primo disegno, così non c'è lampeggio. Senza JavaScript il tema è quello chiaro e l'interruttore è nascosto. Tutti i colori passano dai token, quindi ogni componente cambia insieme. Le illustrazioni dei progetti, disegnate con la stessa palette, vengono leggermente attenuate (`--img-filter`) per non abbagliare.

Per la **deuteranopia** (P05) arancio e verde possono sembrare simili: i quattro stati hanno icone diverse (cerchio vuoto, spunta, quadrato pieno, croce) e il testo è sempre presente; la barra è affiancata dalle cifre.

## 3. Rapporti di contrasto

Calcolati con la formula della luminanza relativa di WCAG 2.2 su 90 coppie realmente usate, per ciascun tema; risultato completo in `docs/verifiche/contrasti.md`. Nessuna coppia è sotto soglia. Oltre alla tabella della sezione 2:

| Coppia | Chiaro | Scuro | Soglia |
|---|---|---|---|
| Link sullo sfondo della pagina | 5,96:1 | 10,28:1 | 4,5:1 |
| Testo del pulsante normale | 14,29:1 | 14,68:1 | 4,5:1 |
| Badge «In corso» / «Conclusa · non raggiunto» | 6,40 / 7,07:1 | 7,80 / 8,66:1 | 4,5:1 |
| Errore sotto il campo | 7,22:1 | 8,31:1 | 4,5:1 |
| Avviso | 6,42:1 | 9,85:1 | 4,5:1 |
| Piè di pagina: testo | 14,49:1 | 18,51:1 | 4,5:1 |
| Pulsante «Sostieni il progetto» rispetto alla pagina | 4,64:1 | 7,49:1 | 3:1 |

Confronto con IdeaGinger (P-034): titoli arancioni 2,46:1, pulsante verde 2,09:1, footer ~2:1.

**Bordi delle card.** Il bordo delle card è decorativo (`--c-border`): la card si distingue per il fondo in rilievo e l'ombra. Non serve un bordo a contrasto perché la card non è un controllo: il controllo è il titolo-link, sottolineato al passaggio del mouse, e al focus l'intera card riceve l'anello di focus a 3 px (WCAG 1.4.11 e 2.4.7 restano soddisfatti).

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
| Pulsanti | `.btn`, `--cta` (azione di donare), `--secondary`, `--ghost`, `--light`, `--large`, `--small`, `--block` | A pillola; altezza ≥ 44 px (grande 52 px, piccolo 36 px); leggero sollevamento al passaggio del mouse; `aria-busy` mostra l'attesa | P-039 |
| Hero della home | `.hero`, `.eyebrow`, `.hero__chips`, `.hero__feature` | Due colonne su desktop: titolo, ricerca grande, due azioni, tre punti chiave con spunta; a destra il **progetto in evidenza** (campagna non ancora riuscita più vicina alla scadenza), con una card vera e cliccabile | P-001, P-003, P-005 |
| Card di progetto | `.card` | Un solo link (titolo) esteso a tutta la card; al passaggio del mouse si solleva e l'immagine si ingrandisce appena; anello di focus su tutta la card | P-029, P-038, P-030, P-026 |
| Badge di stato | `.status--open`, `--reached`, `--done`, `--failed` | Icona SVG diversa per stato + testo + colore + bordo | P-022, P-024, P-028, P-040 |
| Etichetta | `.tag`, `.count-pill` | Categoria, programma, numero di elementi accanto ai titoli | P-030 |
| Barra di avanzamento | `.progress` | Non interattiva, `aria-hidden` (il valore è scritto accanto); oltre il 100% resta piena | P-028, P-050 |
| Riquadro di stato | `.statusbox` | Card in rilievo; cifra raccolta grande in Bricolage, percentuale in verde, righe sostenitori/inizio/scadenza con separatori, «Sostieni» a tutta larghezza | P-022, P-024, P-030 |
| Riquadro informativo | `.infobox` | Fondo viola chiaro con barra a sinistra: soglie e raddoppio, costi, regole | P-048, P-053, P-071 |
| Interruttore del tema | `.theme-toggle` | Icona di luna o sole e, da 1200 px, il testo del tema verso cui si passa; area di 44 px | D-41 |
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
| Piè di pagina | `.site-footer` | Marchio, blocco «Aiuto» uguale in ogni pagina, titoli delle colonne in maiuscoletto, nota sul servizio; focus giallo miele | P-034, P-080 |
| «Torna su» | `.back-to-top` | Link testuale alla cima del contenuto | P-015 |

### Componenti non usati

- **Schede a comparsa (tab)**: si è scelto l'**indice con ancore** (funziona senza JavaScript, link condivisibili a una sezione, stampa completa, contenuto trovabile con la ricerca del browser).
- **Caroselli**: esclusi (P-037). Le liste di progetti sono griglie che vanno a capo.
- **Framework CSS (Tailwind, Bootstrap) e librerie JS di interfaccia**: valutati per il redesign e scartati (D-35).

## 7. Icone e immagini

- Segno del marchio: un fiore stilizzato originale (cinque petali, centro giallo), SVG in linea nell'intestazione e nel piè di pagina; `img/ideablume-segno.svg` resta come favicon. Le decorazioni grandi (dietro il progetto in evidenza e nel riquadro di invito) usano la sua sagoma come maschera CSS incorporata. Tutto decorativo: il nome «ideaBlume» è sempre scritto in testo.
- Icone dell'interfaccia (lente, freccia, spunta, globo, menu): SVG in linea a tratto arrotondato, `aria-hidden="true"`; il significato è sempre nel testo accanto.
- Illustrazioni dei progetti: SVG leggeri generati dalla build, con dimensioni dichiarate (`width`/`height`) e `loading="lazy"` sotto la piega. Testo alternativo descrittivo nella pagina del progetto, vuoto nelle card (P-012).

## 8. Movimento e stampa

- Transizioni brevi (150–500 ms) su card, pulsanti, frecce, accordion e marchio; il badge «sostenitori finora» dell'hero oscilla lentamente (solo da 1100 px). Con `prefers-reduced-motion: reduce` tutte le animazioni sono disattivate.
- Nessuna animazione di comparsa allo scorrimento: il contenuto è sempre visibile subito (niente testo trasparente durante le verifiche di contrasto, niente attese per chi legge).
- Stili di stampa: intestazione, menu e pulsanti nascosti, ombre e fondi tolti; utile per il riepilogo della donazione e della richiesta di collaborazione (P12, J12-F6).
