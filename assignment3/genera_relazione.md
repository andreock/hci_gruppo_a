# Relazione sulla correzione dell'accessibilità (PDF)

## Obiettivo
Produrre `assignment3/relazione/relazione.pdf`: un breve resoconto (indicativamente 10–14 pagine,
appendici escluse) del lavoro di analisi, correzione e nuova verifica dell'accessibilità del
prototipo. Il PDF si genera da un HTML (`assignment3/relazione/relazione.html` + `relazione.css`)
stampato con Chrome headless o Playwright. Lo stile è quello della relazione precedente del gruppo
(`{{PERCORSO_RELAZIONE_PRECEDENTE}}`, es. `docs/relazione.pdf`).

## Voce e onestà
- Scrivi in italiano, in prima persona plurale ("abbiamo analizzato", "abbiamo corretto").
  Il gruppo è l'autore del lavoro. Non raccontare il processo come svolto da un agente e non
  usare formule come "l'agente ha…" o "è stato generato automaticamente…".
- La consegna chiede di documentare l'uso dell'IA. Fallo nella sezione dedicata (§11), come nella
  relazione precedente: quali strumenti, per quali attività, che cosa abbiamo verificato noi.
- Usa solo dati che si trovano nei file. Non inventare numeri, esiti o verifiche manuali.
  Quello che solo il gruppo può sapere (contributi dei componenti, test con screen reader fatti
  a mano, screenshot dei validatori fatti dal gruppo) va lasciato come segnaposto evidenziato
  `[DA COMPLETARE: …]`, con lo stesso stile della relazione precedente.

## Fonti da leggere
- `assignment3/pages.json`, `assignment3/results/`, `assignment3/issues.csv`, `assignment3/REPORT.md`, `assignment3/log.md`: audit
- `assignment3/fixes.json`, `assignment3/fixes-log.md`, `assignment3/FIXES_REPORT.md`: correzioni e falsi positivi
- `git log` e `git show` dei commit `a11y: …`: per ogni correzione, i file modificati e il diff
- La storia git di `assignment3/results/`: il primo audit (PRIMA) e quello dopo le correzioni (DOPO).
  Se la nuova verifica ha sovrascritto i risultati, ricostruisci il PRIMA dal commit precedente.
  Se il DOPO non esiste ancora, fermati e segnalalo: la sezione §9 non si può scrivere senza.
- Eventuali risultati di html-validate, stylelint o W3C Validator, se presenti nei log o nei commit
- `README.md`, `docs/`, `build.py`: per descrivere la struttura del prototipo

## Struttura della relazione
1. **Copertina**: occhiello "Human-Computer Interaction · {{ASSIGNMENT}}", titolo
   "Relazione sull'accessibilità del sito ideaBlume", sottotitolo, poi le etichette GRUPPO, COMPONENTI,
   CORSO, DATA, SITO PUBBLICATO (copia i valori dalla relazione precedente; la data è quella di oggi).
2. **Indice** con numeri di pagina.
3. **Introduzione**: obiettivo e percorso seguito (analisi → correzione → nuova verifica). Massimo mezza pagina.
4. **Strumenti e impostazioni**: MAUVE++ (WCAG 2.1 AA), AccessibilityChecker, ACHECKS/AChecker
   (WCAG 2.0 AA), validazione HTML/CSS e strumenti di sviluppo. Indica le stesse impostazioni usate
   prima e dopo e i limiti di ciascuno strumento (es. MAUVE++ analizza il sorgente HTML).
5. **Pagine analizzate**: copertura dell'intero sito. Riporta il numero di pagine IT ed EN, come le
   abbiamo individuate (sitemap e link interni) e le pagine escluse con il motivo. Aggiungi una tabella
   compatta con pagina, template e strumenti eseguiti. Questo è un criterio di valutazione: rendilo evidente.
6. **Errori, avvisi e verifiche manuali**: spiega come abbiamo distinto le tre categorie. Mostra una
   tabella con i conteggi PRIMA per strumento e categoria, e i problemi ricorrenti di template
   (header, menu, footer) contati una volta sola.
7. **Le principali tipologie di problema**: una sottosezione per tipologia (es. contrasto,
   alternative testuali, struttura dei titoli, etichette dei form, nome accessibile di link e
   pulsanti, lingua, focus e tastiera). Ognuna ha tre blocchi in riquadri: **Che cosa non funziona**,
   **Quali difficoltà causa alle persone** (concreto, citando quando possibile le personas della
   relazione precedente), **Che cosa abbiamo modificato**. Aggiungi un estratto di codice prima/dopo
   preso dal diff (corto, dalla sorgente markdown, template o CSS) e il criterio WCAG.
   Spiega che la correzione è stata fatta una volta nella sorgente comune (template, CSS, i18n) e
   quindi vale per tutte le pagine generate da build.py.
8. **Tabella riassuntiva**, esattamente con queste colonne:
   | Problema rilevato | Pagine o elementi interessati | Correzione effettuata | Esito della nuova verifica |
   Nell'ultima colonna usa un badge "Risolto" / "Parzialmente risolto" / "Non risolto", ricavato dal
   confronto PRIMA/DOPO con lo stesso strumento. Raggruppa per tipologia, non per singola occorrenza.
9. **Falsi positivi e scelte fatte**: per ogni segnalazione scartata spiega perché non era un errore,
   come l'abbiamo verificato e quale strumento la riportava. Elenca anche le scelte progettuali,
   per esempio un colore scelto per rispettare il contrasto restando vicino al brand, l'uso di HTML
   nativo invece di ARIA, o un problema risolto nel generatore invece che pagina per pagina.
   Usa riquadri "Perché" come nella relazione precedente.
10. **Validazione HTML e CSS**: errori trovati, correzioni ed esito. Se mancano dati, metti `[DA COMPLETARE]`.
11. **Nuova verifica**: confronto PRIMA/DOPO per strumento (tabella e un grafico a barre semplice in
    SVG inline), nuovi problemi eventualmente introdotti e controlli sul funzionamento del prototipo
    (build, navigazione, ricerca, donazione, cambio lingua, tastiera).
12. **Errori rimasti e avvisi da verificare**: per ciascuno, perché non è stato risolto (limite dello
    strumento, contenuto che richiede informazioni che non abbiamo, componente esterno) e che cosa
    servirebbe. Includi gli avvisi che richiedono una verifica manuale.
13. **Uso dell'IA**: strumenti usati (Claude Code come supporto per interpretare le segnalazioni,
    raggruppare i problemi e proporre modifiche al codice), che cosa abbiamo controllato noi (diff di
    ogni commit, nuova esecuzione dei validatori, prova del sito) e i limiti incontrati.
    Inserisci `[DA COMPLETARE]` per le verifiche personali del gruppo.
14. **Conclusioni**: massimo 5 righe.
- **Appendice**: elenco completo delle pagine con l'esito per strumento, e i prompt usati (estratti).

## Schermate
Solo per 3–4 correzioni significative (es. contrasto, focus visibile, menu da tastiera):
- genera il sito PRIMA in un `git worktree` sul commit precedente alle correzioni, esegui build.py
  e servilo in locale; genera il sito DOPO dal commit attuale;
- con Playwright cattura lo stesso elemento nei due stati, a 2x, ritagliato sull'area utile;
- impagina le due immagini affiancate con le didascalie "Prima" e "Dopo" e un alt descrittivo.
Non allegare i report completi dei validatori.

## Stile grafico (ripreso dalla relazione precedente)
- Pagina A4, margini circa 18 mm, fondo bianco. Testo #2c1f24, Inter 10–10.5pt, interlinea 1.45.
- Titoli in Bricolage Grotesque ExtraBold, colore #3b1d2a. Il numero di sezione va in arancio #bf4a12,
  con una linea sottile arancio sotto l'H1. Ogni sezione principale inizia su una nuova pagina.
- Copertina: banda superiore bordeaux #3b1d2a (circa il 45% della pagina) con occhiello arancio-oro
  #f4b93e in maiuscoletto, titolo grande in crema #fbf6ee e sottotitolo; sotto, una sottile linea
  arancio #bf4a12 e un fondo crema #fbf6ee con le etichette in maiuscolo arancio e i valori in scuro.
- Tabelle: didascalia "Tabella N." sopra; intestazione #3b1d2a con testo bianco; righe alternate
  #f8f2ea; bordi #d9cbbd sottili. Le righe non si spezzano tra due pagine (`break-inside: avoid`).
- Riquadri: azzurro #e2eff4 con bordo sinistro #1d5b73 (spiegazioni e motivazioni), verde #e3f2e6
  (risolto), pesca #fbeadd (problema), giallo #fdf1d0 con testo #5c3e00 (segnaposto DA COMPLETARE).
- Badge a pillola per esiti e strumenti (verde = risolto, giallo = parziale, pesca = non risolto).
- Codice in monospazio 8.5pt su fondo #f8f2ea.
- Piè di pagina su tutte le pagine tranne la copertina: a sinistra "Gruppo A · Accessibilità del
  sito ideaBlume", a destra "Pagina X di Y", in grigio piccolo. Usa footerTemplate di Chrome con
  pageNumber/totalPages.
- Font: cerca Inter e Bricolage Grotesque in `fonts/` o nei sorgenti della relazione precedente e
  incorporali con @font-face. Se non ci sono, scaricali da Google Fonts nella cartella della relazione.

## Accessibilità del PDF (coerenza con il tema)
- `<html lang="it">`, un solo H1 per sezione e gerarchia dei titoli senza salti, tabelle con `<th scope>`
  e `<caption>`, alt su ogni immagine, contrasto almeno 4.5:1 anche nei badge e nei riquadri.
- PDF taggato (Chrome: `tagged: true` / `--generate-pdf-document-outline`), con titolo nei metadati
  e segnalibri dai titoli.

## Generazione e controllo
1. Scrivi l'HTML e il CSS, poi genera il PDF.
2. Indice: genera una prima volta, ricava il numero di pagina di ogni titolo con `pdftotext`,
   inseriscilo nell'indice e rigenera. Ripeti finché i numeri non cambiano più.
3. Controlli:
   - rendi ogni pagina in PNG e guardale tutte: niente testo tagliato, tabelle spezzate male,
     pagine quasi vuote o orfane, immagini sgranate;
   - `pdffonts`: font incorporati; `pdfinfo`: A4, titolo corretto, taggato;
   - ogni numero nel testo coincide con i file di `assignment3/` (ricontalo con uno script, non a mano);
   - ogni riga della tabella riassuntiva corrisponde a un fix in `fixes.json` e a un commit;
   - cerca nel testo "agente", "Claude ha", "è stato generato" fuori dalla §13 e riformula;
   - elenca alla fine tutti i `[DA COMPLETARE]` rimasti, così il gruppo sa che cosa compilare.
4. Non fare commit né push: lascia i file in `assignment3/relazione/`.
