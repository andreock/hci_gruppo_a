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

| Criterio | Liv. | Pagine con errore | Pagine coinvolte (errori o avvisi) | Strumenti (pagine) | Occ. errori | Occ. avvisi |
|---|---|---|---|---|---|---|
| 1.1.1 | A | 50 | 50 | AChecker (avviso): 24; MAUVE++ (avviso): 30; MAUVE++ (errore): 50 | 370 | 176 |
| 1.3.1 | A | 50 | 50 | AChecker (avviso): 50; AChecker (errore): 22; MAUVE++ (avviso): 50; MAUVE++ (errore): 50 | 72 | 876 |
| 1.4.1 | A | 50 | 50 | AChecker (avviso): 50; MAUVE++ (errore): 50 | 148 | 345 |
| 1.4.3 | AA | 50 | 50 | MAUVE++ (errore): 50 | 150 | 0 |
| 1.4.4 | AA | 50 | 50 | AChecker (errore): 50; MAUVE++ (avviso): 50 | 100 | 278 |
| 1.4.5 | AA | 50 | 50 | AChecker (avviso): 24; MAUVE++ (errore): 50 | 50 | 50 |
| 2.4.7 | AA | 50 | 50 | MAUVE++ (errore): 50 | 100 | 0 |
| 1.3.5 | AA | 16 | 18 | MAUVE++ (avviso): 2; MAUVE++ (errore): 16 | 48 | 2 |
| 1.4.10 | AA | 16 | 16 | MAUVE++ (errore): 16 | 40 | 0 |
| 1.3.3 | A | 0 | 50 | AChecker (avviso): 50 | 0 | 50 |
| 1.4.12 | AA | 0 | 50 | MAUVE++ (avviso): 50 | 0 | 858 |
| 2.1.1 | A | 0 | 50 | AChecker (avviso): 50 | 0 | 165 |
| 2.3.1 | A | 0 | 50 | AChecker (avviso): 50 | 0 | 165 |
| 2.4.1 | A | 0 | 50 | AChecker (avviso): 50; MAUVE++ (avviso): 50 | 0 | 590 |
| 2.4.2 | A | 0 | 50 | AChecker (avviso): 50 | 0 | 50 |
| 2.4.4 | A | 0 | 50 | AChecker (avviso): 50 | 0 | 1866 |
| 2.4.5 | AA | 0 | 50 | AChecker (avviso): 50 | 0 | 50 |
| 2.4.6 | AA | 0 | 50 | AChecker (avviso): 50 | 0 | 862 |
| 2.5.3 | A | 0 | 50 | MAUVE++ (avviso): 50 | 0 | 682 |
| 3.2.3 | AA | 0 | 50 | AChecker (avviso): 50 | 0 | 74 |
| 3.2.4 | AA | 0 | 50 | AChecker (avviso): 50 | 0 | 50 |
| 4.1.2 | A | 0 | 28 | MAUVE++ (avviso): 28 | 0 | 44 |
| 3.3.2 | A | 0 | 26 | AChecker (avviso): 26; MAUVE++ (avviso): 6 | 0 | 188 |
| 3.1.2 | AA | 0 | 25 | AChecker (avviso): 25 | 0 | 25 |
| 3.3.1 | A | 0 | 24 | AChecker (avviso): 24 | 0 | 24 |
| 3.3.3 | AA | 0 | 24 | AChecker (avviso): 24 | 0 | 24 |
| 3.3.4 | AA | 0 | 24 | AChecker (avviso): 24 | 0 | 48 |
| 4.1.3 | AA | 0 | 24 | MAUVE++ (avviso): 24 | 0 | 58 |
| 1.2.1 | A | 0 | 4 | MAUVE++ (avviso): 4 | 0 | 30 |

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

| # | Pagina | Template | Occorrenze di errore (MAUVE++ + AChecker) | Tecniche/controlli in errore | MAUVE++ % | Criteri in errore MAUVE++ | Errori AChecker | Avvisi AChecker |
|---|---|---|---|---|---|---|---|---|
| 1 | `en/progetti.html` | elenco | 40 | 9 | 90 | 8 | 2 | 147 |
| 2 | `progetti.html` | elenco | 40 | 9 | 90 | 8 | 2 | 146 |
| 3 | `en/` | home | 34 | 7 | 89 | 6 | 2 | 112 |
| 4 | `/` | home | 34 | 7 | 89 | 6 | 2 | 111 |
| 5 | `en/progetto-alveari-sani.html` | scheda | 28 | 10 | 93 | 8 | 3 | 109 |
| 6 | `progetto-alveari-sani.html` | scheda | 28 | 10 | 93 | 8 | 3 | 108 |
| 7 | `en/progetto-clima-giovani.html` | scheda | 27 | 10 | 93 | 8 | 3 | 107 |
| 8 | `en/progetto-neonati-virus.html` | scheda | 27 | 10 | 93 | 8 | 3 | 107 |
| 9 | `progetto-clima-giovani.html` | scheda | 27 | 10 | 93 | 8 | 3 | 106 |
| 10 | `progetto-neonati-virus.html` | scheda | 27 | 10 | 93 | 8 | 3 | 106 |

Gli errori in più rispetto alle altre pagine vengono da tre fonti: le etichette `tag` delle card (G18) su `progetti`, le card e i bottoni della home (ARIA6, F73, G18) e, sulle schede in corso, il form "scrivi" (H98, C38) e la tabella "Uso dei fondi" (#245).

Tabella completa per pagina:

| Pagina | Template | MAUVE++ % | MAUVE++ err/avv | AChecker err/avv | Lighthouse | AccessibilityChecker |
|---|---|---|---|---|---|---|
| `/` | home | 89 | 6/5 | 2/111 | 100 | 90 (0 critici) |
| `404.html` | errore | 91 | 6/4 | 2/64 | 100 | skipped |
| `accessibilita.html` | contenuto | 91 | 6/3 | 2/55 | 100 | skipped |
| `candidatura.html` | form | 92 | 8/5 | 2/92 | 100 | skipped |
| `cerca.html` | ricerca | 91 | 6/4 | 2/72 | 100 | skipped |
| `chi-siamo.html` | contenuto | 94 | 6/3 | 2/88 | 100 | 90 (0 critici) |
| `collabora.html` | form | 92 | 8/5 | 2/86 | 100 | skipped |
| `come-funziona.html` | contenuto | 94 | 6/3 | 2/83 | 100 | 90 (0 critici) |
| `contatti.html` | form | 91 | 8/4 | 2/76 | 100 | skipped |
| `donazione-conferma.html` | conferma | 89 | 6/3 | 2/58 | 100 | skipped |
| `donazione.html` | form | 94 | 6/5 | 2/117 | 100 | skipped |
| `en/` | home | 89 | 6/5 | 2/112 | 100 | skipped |
| `en/404.html` | errore | 91 | 6/4 | 2/62 | 100 | skipped |
| `en/accessibilita.html` | contenuto | 91 | 6/3 | 2/56 | 100 | skipped |
| `en/candidatura.html` | form | 92 | 8/5 | 2/93 | 100 | skipped |
| `en/cerca.html` | ricerca | 91 | 6/4 | 2/73 | 100 | skipped |
| `en/chi-siamo.html` | contenuto | 94 | 6/3 | 2/89 | 100 | skipped |
| `en/collabora.html` | form | 92 | 8/5 | 2/87 | 100 | skipped |
| `en/come-funziona.html` | contenuto | 94 | 6/3 | 2/84 | 100 | skipped |
| `en/contatti.html` | form | 91 | 8/4 | 2/77 | 100 | skipped |
| `en/donazione-conferma.html` | conferma | 89 | 6/3 | 2/59 | 100 | skipped |
| `en/donazione.html` | form | 94 | 6/5 | 2/118 | 100 | skipped |
| `en/faq.html` | contenuto | 96 | 6/3 | 2/84 | 100 | skipped |
| `en/progetti.html` | elenco | 90 | 8/5 | 2/147 | 100 | skipped |
| `en/progetto-alveari-sani.html` | scheda | 93 | 8/5 | 3/109 | 100 | skipped |
| `en/progetto-aria-aperta.html` | scheda | 93 | 8/5 | 3/106 | 100 | skipped |
| `en/progetto-clima-giovani.html` | scheda | 93 | 8/5 | 3/107 | 100 | skipped |
| `en/progetto-dialetti-archivio.html` | scheda | 94 | 6/4 | 3/90 | 100 | skipped |
| `en/progetto-matematica-accessibile.html` | scheda | 94 | 6/4 | 3/91 | 100 | skipped |
| `en/progetto-neonati-virus.html` | scheda | 93 | 8/5 | 3/107 | 100 | skipped |
| `en/progetto-plastica-batteri.html` | scheda | 94 | 6/4 | 3/91 | 100 | skipped |
| `en/progetto-rifugi-frane.html` | scheda | 94 | 6/4 | 3/89 | 100 | skipped |
| `en/progetto-robot-anziani.html` | scheda | 94 | 6/4 | 3/90 | 100 | skipped |
| `en/progetto-scienza-doposcuola.html` | scheda | 94 | 6/4 | 3/90 | 100 | skipped |
| `en/programma.html` | contenuto | 94 | 6/3 | 3/85 | 100 | skipped |
| `en/proponi.html` | contenuto | 94 | 6/3 | 2/102 | 100 | skipped |
| `faq.html` | contenuto | 96 | 6/3 | 2/83 | 100 | skipped |
| `progetti.html` | elenco | 90 | 8/5 | 2/146 | 100 | error |
| `progetto-alveari-sani.html` | scheda | 93 | 8/5 | 3/108 | 100 | skipped |
| `progetto-aria-aperta.html` | scheda | 93 | 8/5 | 3/105 | 100 | skipped |
| `progetto-clima-giovani.html` | scheda | 93 | 8/5 | 3/106 | 100 | skipped |
| `progetto-dialetti-archivio.html` | scheda | 94 | 6/4 | 3/89 | 100 | skipped |
| `progetto-matematica-accessibile.html` | scheda | 94 | 6/4 | 3/90 | 100 | skipped |
| `progetto-neonati-virus.html` | scheda | 93 | 8/5 | 3/106 | 100 | skipped |
| `progetto-plastica-batteri.html` | scheda | 94 | 6/4 | 3/90 | 100 | skipped |
| `progetto-rifugi-frane.html` | scheda | 94 | 6/4 | 3/88 | 100 | skipped |
| `progetto-robot-anziani.html` | scheda | 94 | 6/4 | 3/89 | 100 | skipped |
| `progetto-scienza-doposcuola.html` | scheda | 94 | 6/4 | 3/89 | 100 | skipped |
| `programma.html` | contenuto | 94 | 6/3 | 3/84 | 100 | skipped |
| `proponi.html` | contenuto | 94 | 6/3 | 2/101 | 100 | skipped |

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
