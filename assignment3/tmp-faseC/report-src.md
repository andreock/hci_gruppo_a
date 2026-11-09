# Report audit di accessibilità – ideaBlume (anteprima assignment3)

Sito verificato: `https://andreock.github.io/hci_gruppo_a/anteprime/assignment3/` (anteprima del branch assignment3, 25 pagine IT + 25 EN).
Periodo: 2026-11-09, lotti 1–17 (vedi `log.md`). Dati per pagina in `results/<slug>.json`, elenco completo dei problemi in `issues.csv`.

## 1. Sintesi

- **Pagine verificate: 50 su 50.** Tutte hanno almeno un risultato valido. MAUVE++, AChecker e Lighthouse (via ACHECKS) hanno dato risultati su tutte le 50 pagine.
- **Nessuna pagina è rimasta non verificabile.** C'è però un limite: su `cerca.html` ed `en/cerca.html` i risultati della ricerca sono generati via JavaScript. MAUVE++ e AChecker hanno valutato solo lo stato iniziale, senza risultati, quindi le schede dei risultati non sono state valutate.
- **AccessibilityChecker ha una copertura parziale: 3 pagine su 50.** Ha dato risultati su `/`, `chi-siamo.html` e `come-funziona.html`: punteggio 90, 0 "Critical Issues" e 22 verifiche manuali generiche. Su `progetti.html` ha dato "error" dopo tre timeout. Sulle altre 46 pagine è "skipped": dal lotto 2 il sito ha risposto "You have reached the daily limit for scanning websites". Il limite non è stato aggirato e dopo 3 iterazioni consecutive con lo stesso blocco lo strumento è stato abbandonato (lotto 4).
- Nessun file non HTML da verificare (`non-html.md`).
- Riepilogo dei punteggi:
  - **MAUVE++** (WCAG 2.1 AA): dall'89% al 96%; da 6 a 8 criteri in errore per pagina.
  - **AChecker** (WCAG 2.0 AA): 2 o 3 "known problems" per pagina; da 55 a 147 "potential problems" da verificare a mano.
  - **Lighthouse 13.0.1**: 100 su tutte le 50 pagine, nessun audit fallito.

| Strumento | ok | skipped | error |
|---|---|---|---|
| MAUVE++ | 50 | 0 | 0 |
| AChecker (ACHECKS) | 50 | 0 | 0 |
| Lighthouse (via ACHECKS) | 50 | 0 | 0 |
| AccessibilityChecker | 3 | 46 | 1 |

Le versioni IT ed EN della stessa pagina danno risultati quasi identici: stesso riepilogo e stesse occorrenze per tecnica in MAUVE++, mentre AChecker trova al massimo 1–2 avvisi di differenza. In pratica le pagine distinte sono 25, ciascuna verificata nelle due lingue.

## 2. Problemi per criterio WCAG

Ordinati per numero di pagine con errore, poi per pagine coinvolte. "Errore" indica un problema certo per lo strumento: le "known problems" di AChecker e gli errori di MAUVE++. "Avviso" indica un punto da verificare a mano: i "potential problems" di AChecker e gli avvisi di MAUVE++. Lighthouse non compare in tabella perché non ha alcun audit fallito. Tra i suoi audit "informative" c'è solo `aria-allowed-role`, senza criterio WCAG (vedi §5).

{{CRITERI}}

### 2.1 Dettaglio degli errori (in ordine di priorità)

1. **1.3.1 Info e correlazioni (A): tabelle con più righe o colonne di intestazione.** È **l'unico problema confermato da due strumenti sugli stessi elementi**, quindi ha la priorità più alta. Coinvolge 22 pagine: la tabella "Uso dei fondi" delle 10 schede progetto e la tabella "Progetti del programma per anno" di `programma.html`, in IT ed EN.
   - AChecker lo segnala come errore (#245): mancano `id`/`headers` sulle celle.
   - MAUVE++ lo segnala come avviso sulle stesse `<table>` (F46, H73).
   - AChecker aggiunge sulle stesse tabelle gli avvisi #111, #137, #231 e #242.
2. **1.4.3 Contrasto minimo (AA), G18: MAUVE++ su 50 pagine, 150 occorrenze.** In tutte le pagine sono segnalati `<span class="vh">Passa a: </span>`, che è testo visivamente nascosto, e `<span class="theme-toggle__testo">Tema scuro</span>` nell'header. Ci sono poi casi per pagina: su `progetti.html`, per esempio, 11 occorrenze sulle etichette `tag tag--programma`. Solo MAUVE++ lo rileva.
3. **2.4.7 Focus visibile (AA), G195 e F78: MAUVE++ su 50 pagine.** L'elemento segnalato è sempre `<a class="skip-link" href="#main">`. Solo MAUVE++ lo rileva.
4. **1.1.1 Contenuti non testuali (A), ARIA6: MAUVE++ su 50 pagine, 370 occorrenze.** Gli elementi segnalati sono gli `<svg class="brand__mark">` e `<svg class="icon">`, che nello snippet hanno già `aria-hidden="true" focusable="false"`, cioè sono decorativi. Solo MAUVE++ lo rileva, come errore. AChecker dà su 1.1.1 solo avvisi generici sulle immagini.
5. **1.4.1 Uso del colore (A), F73: MAUVE++ su 50 pagine, 148 occorrenze.** MAUVE++ segnala link non distinguibili senza il colore, tutti in stile bottone (`a.btn`). Su ogni pagina c'è il "Scrivici"/"Write to us" del footer, a cui si aggiungono i bottoni nel contenuto: fino a 8 occorrenze sulle schede in corso. AChecker su 1.4.1 dà solo avvisi generici (#86 `<script>`, #55 `<input>`).
6. **1.4.4 Ridimensionamento del testo (AA), AChecker #116: uso di `<b>` su 50 pagine, 2 occorrenze ciascuna.** È il marchio `idea<b>Blume</b>` nell'header e nel footer. Solo AChecker lo rileva come errore. MAUVE++ su 1.4.4 dà un avviso diverso (C28, dimensioni dei contenitori in `em`).
7. **1.3.1 / 1.4.5, G140: MAUVE++ su 50 pagine.** L'elemento segnalato è l'elemento radice `<html>`. Non indica un elemento preciso: va verificato a mano che la separazione tra struttura e presentazione regga, per esempio con i CSS disattivati.
8. **1.3.5 Identificare lo scopo degli input (AA), H98, e 1.4.10 Reflow (AA), C38: MAUVE++ su 16 pagine.** Le pagine sono `candidatura`, `collabora`, `contatti`, `progetti` e le 4 schede in corso (`alveari-sani`, `aria-aperta`, `clima-giovani`, `neonati-virus`), in IT ed EN. Le schede in corso contengono il form "scrivi" con `textarea#sc-msg`.
   - H98 colpisce anche campi che non riguardano dati personali, come `textarea` di messaggio, `select` del ruolo e titolo del progetto. Colpisce anche `k-telefono`, che ha già `autocomplete="tel"`. Va quindi verificato campo per campo quali richiedono davvero `autocomplete`.
   - C38 segnala i contenitori `div.field`.

## 3. Problemi di template (riportati una sola volta)

Questi problemi compaiono con lo stesso elemento su tutte (o quasi tutte) le 50 pagine. Dipendono da componenti comuni: correggerli una volta li risolve su tutto il sito.

| Componente | Problema | Criterio | Strumento | Pagine |
|---|---|---|---|---|
| Header e footer, logo `svg.brand__mark` e icone `svg.icon` (`aria-hidden="true"`) | ARIA6, errore | 1.1.1 A | MAUVE++ | 50 |
| Header e footer, marchio `idea<b>Blume</b>` | #116 `<b>`, errore | 1.4.4 AA | AChecker | 50 |
| Skip link `a.skip-link` "Salta al contenuto" | G195/F78 focus visibile, errore | 2.4.7 AA | MAUVE++ | 50 |
| Header, interruttore tema (`span.vh` "Passa a:", `span.theme-toggle__testo`) | G18 contrasto, errore | 1.4.3 AA | MAUVE++ | 50 |
| Header, interruttore tema e `span.vh` | C21 interlinea e C28 contenitori in `em`, avvisi | 1.4.12 / 1.4.4 AA | MAUVE++ | 50 |
| Footer, bottone "Scrivici"/"Write to us" (`a.btn`) | F73 link distinguibile solo col colore, errore | 1.4.1 A | MAUVE++ | 50 |
| Elemento radice `<html>` | G140, errore | 1.3.1 / 1.4.5 | MAUVE++ | 50 |
| `header.site-header`, `footer.site-footer`, `nav#menu-principale` | ARIA11 landmark, avviso | 1.3.1 / 2.4.1 A | MAUVE++ | 50 (footer 47) |
| `div.site-header__bar` (aria-label) | F96 etichetta nel nome, avviso | 2.5.3 A | MAUVE++ | 50 |
| Intera pagina, controlli generici | #54 titolo, #86/#87/#89 `<script>`, #28 skip link, #184 mappa del sito, #276 e #131, #19 testo dei link, #42/#43/#44 intestazioni, avvisi | vari | AChecker | 50 |
| `<body>` delle pagine EN (controllo su tutto il documento) | #110 lingua delle parti, avviso | 3.1.2 AA | AChecker | 25 (solo EN) |

Problemi di componente, non presenti su ogni pagina:
- **Tabella "Uso dei fondi"** (template scheda, 10 schede × 2 lingue) e tabella di `programma`: vedi §2.1 punto 1.
- **Form** (`candidatura`, `collabora`, `contatti`, `donazione`, form "scrivi" delle schede in corso, ricerca di `progetti`):
  - H98 e C38 (errori MAUVE++);
  - ARIA19 e G199 (avvisi MAUVE++ sui messaggi di errore e di stato);
  - #267, #268, #269, #272, #246 e #265 (avvisi generici AChecker sui form, 24 pagine);
  - H44 e G162 sulle checkbox privacy e sul radio `m-bonifico` (avvisi MAUVE++).
- **Immagini delle card** (`/`, `progetti`): F30, avviso, su `img alt=""`. **Immagine principale delle schede**: H67, avviso.
- **Risultati della ricerca** (`cerca`): Lighthouse, audit informative `aria-allowed-role`, `role="status"` su `<h2 class="result-count">`.

## 4. Le 10 pagine con più problemi

Le pagine sono ordinate per numero di occorrenze di errore. Si sommano gli errori MAUVE++ e le "known problems" di AChecker. A parità di occorrenze, conta il numero di tecniche o controlli in errore.

{{TOP10}}

Gli errori in più rispetto alle altre pagine vengono da tre fonti: le etichette `tag` delle card (G18) su `progetti`, le card e i bottoni della home (ARIA6, F73, G18) e, sulle schede in corso, il form "scrivi" (H98, C38) e la tabella "Uso dei fondi" (#245).

Tabella completa per pagina:

{{PAGINE}}

## 5. Discrepanze tra strumenti (da verificare a mano)

Lighthouse dà 100 su tutte le pagine, senza audit falliti. AccessibilityChecker, sulle 3 pagine verificate, non trova "Critical Issues". **Nessuno degli errori di MAUVE++ o AChecker è quindi confermato da questi due strumenti.** Tra MAUVE++ e AChecker solo il problema delle tabelle (1.3.1) coincide sugli stessi elementi. Tutti gli altri sono rilevati da un solo strumento:

| Problema | Rilevato da | Non rilevato da | Cosa verificare a mano |
|---|---|---|---|
| 1.4.3 contrasto (G18) su `span.vh`, `theme-toggle__testo` e `tag` | MAUVE++ | AChecker, Lighthouse | Misurare il contrasto nei temi chiaro e scuro. `span.vh` è testo visivamente nascosto, quindi il contrasto non dovrebbe applicarsi. |
| 2.4.7 focus visibile sullo skip link (G195/F78) | MAUVE++ | AChecker, Lighthouse | Navigare con Tab dall'inizio della pagina e controllare che lo skip link compaia con un indicatore di focus visibile. |
| 1.1.1 ARIA6 sugli `svg` con `aria-hidden="true"` | MAUVE++ | AChecker, Lighthouse | Confermare che gli `svg` siano decorativi e che il loro testo accessibile sia fornito dall'elemento genitore (link del logo, bottoni). |
| 1.4.1 F73 sui link `a.btn` | MAUVE++ | AChecker, Lighthouse | Controllare che i bottoni siano riconoscibili anche senza colore (forma, bordo, sottolineatura al focus o hover). |
| 1.4.4 `<b>` nel marchio (#116) | AChecker | MAUVE++, Lighthouse | Ingrandire il testo al 200% e controllare che il marchio resti leggibile. Valutare se `<b>` ha solo funzione stilistica. |
| 1.3.1 / 1.4.5 G140 su `<html>` | MAUVE++ | AChecker, Lighthouse | Disattivare i CSS e controllare che ordine e struttura del contenuto restino comprensibili. |
| 1.3.5 H98 sui campi dei form | MAUVE++ | AChecker, Lighthouse | Controllare quali campi raccolgono dati personali dell'utente (nome, email, telefono) e che abbiano un `autocomplete` corretto. `k-telefono` ha già `autocomplete="tel"`. |
| 1.4.10 C38 su `div.field` | MAUVE++ | AChecker, Lighthouse | Controllare il reflow a 320 px CSS (zoom 400%) sui form. |
| Avvisi AChecker generici (#28 skip link mancante, #184 mappa del sito, #19 testo dei link, ecc.) | AChecker | MAUVE++, Lighthouse | Il #28 contraddice MAUVE++, che trova lo skip link su tutte le pagine. Gli altri sono controlli euristici da confermare caso per caso. |
| `aria-allowed-role` su `<h2 role="status">` (`cerca`) | Lighthouse (informative, peso 0) | MAUVE++ (che su `cerca` dà G199 come avviso), AChecker | Controllare che l'annuncio del numero di risultati arrivi allo screen reader e che non rompa la struttura delle intestazioni. |
| AccessibilityChecker: 0 problemi critici | AccessibilityChecker (3 pagine) | – | Copertura troppo bassa per un confronto: il limite giornaliero ha impedito le altre 46 pagine. |

## 6. Nota finale

I validatori automatici coprono solo una parte dei criteri WCAG. Molti dei risultati sopra sono euristiche ("potential problems", avvisi) o possibili falsi positivi, e un punteggio di 100 in Lighthouse non garantisce la conformità. Servono anche verifiche manuali:
- **navigazione da tastiera**: ordine del focus, focus visibile, skip link, menu, interruttore del tema, form e messaggi di errore, assenza di trappole;
- **screen reader** (NVDA/JAWS, VoiceOver): nomi accessibili, landmark, annunci di `role="status"`/`alert`, tabelle "Uso dei fondi", risultati della ricerca generati via JavaScript;
- **contrasto nel contesto reale**: tema chiaro e scuro, stati hover e focus, testo sopra le immagini;
- **zoom e reflow**: testo al 200%, larghezza di 320 px;
- **contenuti e lingua**: titoli, testo dei link e lingua delle parti nelle pagine EN.
