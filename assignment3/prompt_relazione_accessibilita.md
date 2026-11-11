# Relazione sulla correzione dell'accessibilità (PDF)

## Obiettivo
Produrre `a11y/relazione/relazione.pdf`: un breve resoconto (indicativamente 10–14 pagine,
appendici escluse) per l'Assignment 3. Il resoconto copre l'analisi dell'accessibilità
dell'intero prototipo ideaBlume (25 pagine IT + 25 EN), le correzioni e la nuova verifica.
Il PDF si genera da un HTML (`a11y/relazione/relazione.html` + `relazione.css`) stampato con
Chrome headless o Playwright, nello stile della relazione precedente del gruppo
(`{{PERCORSO_RELAZIONE_PRECEDENTE}}`). La relazione sostituisce e integra
`resoconto_accessibilita.md` e `risultati_mauve.md`: non è un documento da affiancare a loro.

## Riferimenti git (fonte di verità per le modifiche)
- Il commit `5a6bddc8bc943b9f60ce149e27ce49286b1ddc1d` introduce l'Assignment 3.
- **PRIMA** = il suo parent: `BASE=$(git rev-parse 5a6bddc8bc943b9f60ce149e27ce49286b1ddc1d^)`.
  È lo stato del prototipo alla fine dell'Assignment 2, su cui è stata fatta la baseline.
- **DOPO** = `HEAD`.
- Tutto il lavoro dell'Assignment 3 è nell'intervallo `$BASE..HEAD`. Comincia così:
  ```bash
  git log --reverse --format='%h %ad %s' --date=short $BASE..HEAD
  git diff --stat $BASE HEAD
  git diff --stat $BASE HEAD -- ':!*.html'                 # solo le sorgenti
  git diff $BASE HEAD -- tools/ css/ js/ i18n/ data/ docs/ '*.md'
  ```
  Se il prototipo sta in una sottocartella (es. `assignment2/website/`), applica i percorsi relativi a
  quella cartella.
- Se lo stato di lavoro non è pulito (`git status`), fermati e segnalalo: la relazione deve descrivere
  solo modifiche registrate in commit.
- Ogni correzione citata nella relazione deve corrispondere a modifiche visibili nel diff
  `$BASE..HEAD`. Indica l'hash breve del commit (o dei commit) che la introduce. Se una correzione
  descritta nel resoconto o in `fixes.json` non compare nel diff, non presentarla come fatta:
  annotala in `riconciliazione.md` e trattala come punto aperto.
- Assegna ogni commit a un ciclo. Il **ciclo 1** è il lavoro documentato nel resoconto (fino al
  5 novembre: correzione del logo per il criterio 2.5.3, fallback dei titoli dinamici, nomi dei
  landmark di ricerca, ripristino della posizione, rimozione dei `<br>`, bersagli a 24 px). Il
  **ciclo 2** sono i commit `a11y: …` del loop. Basati su data, messaggio e contenuto del commit.
  Se un commit è ambiguo, annotalo.
- Coerenza della build: in un worktree pulito su `HEAD`, esegui `tools/build.py` e controlla che non
  produca differenze. Se ne produce, alcune modifiche sono state fatte direttamente sugli HTML generati:
  segnalalo in `riconciliazione.md`.

## Voce e onestà
- Scrivi in italiano, in prima persona plurale ("abbiamo analizzato", "abbiamo corretto").
  Il gruppo è l'autore del lavoro. Non raccontare il processo come svolto da un agente e non usare
  formule come "l'agente ha…" o "è stato generato automaticamente…". Converti anche il passivo
  impersonale del resoconto precedente ("è stato analizzato") nella voce del gruppo.
- La consegna chiede di documentare l'uso dell'IA. Fallo nella sezione dedicata (§13).
- Usa solo dati presenti nei file o nella storia git. Non inventare numeri, esiti o verifiche manuali.
  Quello che solo il gruppo può sapere va lasciato come segnaposto evidenziato `[DA COMPLETARE: …]`.

## Fonti

### Primo ciclo (5 novembre 2026): documentazione precedente
Individua nel repository i file (probabilmente sotto `assignment2/website/` o `docs/`):
- `resoconto_accessibilita.md`: metodo, strumenti e versioni, copertura, risultato di Accessibility
  Checker sulla home (72/100, un errore critico WCAG 2.5.3 sul logo), correzioni del primo ciclo,
  cicli di verifica 1–6, esito locale, segnalazioni residue di MAUVE++ e uso di Codex.
- `risultati_mauve.md`: baseline MAUVE++ 4.0.2 (WCAG 2.1 AA, pagina singola, desktop/Windows/
  Chrome) sulle 50 pagine pubblicate. Contiene accessibilità e completezza per pagina, i 6 criteri
  segnalati su tutte le pagine (1.1.1, 1.3.1, 1.4.1, 1.4.3, 1.4.5, 2.4.7) e i 2 su 16 pagine
  (1.3.5, 1.4.10).
- `docs/verifiche/`: `axe.md`, `percorsi.md`, `responsive.md`, `contrasti.md`, `link.md`, `dati.md`.
- I comandi di riproduzione: `tools/build.py`, `tools/verifica-*.py`, `tools/contrasto.py` e gli
  script npm `validate` e `verify`.

### Secondo ciclo: loop di audit e correzione
- `a11y/pages.json`, `a11y/results/`, `a11y/issues.csv`, `a11y/REPORT.md`, `a11y/log.md`: audit
  con MAUVE++, AccessibilityChecker e ACHECKS su tutte le pagine.
- `a11y/fixes.json`, `a11y/fixes-log.md`, `a11y/FIXES_REPORT.md`: correzioni, falsi positivi e
  fix da decidere.

### PRIMA e DOPO
**Validatori online (sito pubblicato)**
- PRIMA: per MAUVE++, `risultati_mauve.md`. Prima di usarlo, controlla che la data della scansione e
  la versione pubblicata a quella data corrispondano a `$BASE`. Il resoconto dice che la pubblicazione
  era precedente alle correzioni: se non corrisponde, annotalo. Per AccessibilityChecker e ACHECKS, la
  prima esecuzione del loop (se è stata sovrascritta, ricostruiscila con `git log -p -- a11y/results/`).
  Per AccessibilityChecker sulla home vale anche il 72/100 del resoconto.
- DOPO: la scansione più recente in `a11y/results/` fatta dopo la pubblicazione di `HEAD`, con gli
  stessi strumenti e le stesse impostazioni (MAUVE++ WCAG 2.1 AA, desktop/Windows/Chrome).
  Controlla con le date (`checked_at` e data dei commit) che sia successiva all'ultimo commit di
  correzione. Se non lo è, o manca, gli esiti online vanno segnati "da riconfermare online" con
  `[DA COMPLETARE]` e la mancanza va elencata nella §12.

**Controlli locali (riproducibili da git)**
- Crea due worktree temporanei:
  ```bash
  git worktree add /tmp/a11y-prima $BASE
  git worktree add /tmp/a11y-dopo  HEAD
  ```
- In entrambi esegui `tools/build.py`, poi gli stessi controlli: html-validate, Stylelint, axe +
  Playwright (`npm --prefix tools run validate` / `verify`), `verifica-dati.py`, `verifica-link.py`,
  `contrasto.py`. Se in `$BASE` uno script non esiste ancora, usa la versione di `HEAD` sugli HTML di
  `$BASE` e scrivilo nella relazione ("controllo eseguito con la suite attuale sulla versione
  precedente").
- Salva gli output in `a11y/relazione/dati/prima/` e `a11y/relazione/dati/dopo/`. Sono i numeri
  delle tabelle PRIMA/DOPO locali della §11.
- Alla fine rimuovi i worktree (`git worktree remove`).

### Riconciliazione tra le fonti (obbligatoria prima di scrivere)
Prepara `a11y/relazione/riconciliazione.md` (uso interno, non va nel PDF) con una riga per criterio
o problema: che cosa dicono il resoconto, risultati_mauve, il loop e il diff git, e quale
classificazione finale adottiamo, con i commit.
- Se il diff mostra che abbiamo corretto un problema che il resoconto classificava come
  "non riprodotto" o "falso positivo probabile" (es. 1.4.3 contrasto, 2.4.7 focus, 1.1.1 SVG),
  nella relazione dillo esplicitamente: la classificazione è stata rivista, con l'evidenza e il commit.
- Se il loop conferma un falso positivo, unisci le motivazioni delle due fonti.
- Se due numeri non coincidono, usa il dato più recente e verificabile e annota la discrepanza.
- Il resoconto dice che Accessibility Checker è stato usato solo sulla home. Spiega che nel secondo
  ciclo abbiamo esteso AccessibilityChecker e ACHECKS a tutte le pagine.
- Segnala le modifiche presenti nel diff ma non documentate da nessuna fonte. Se riguardano
  l'accessibilità, vanno descritte; se sono altro (contenuti, refactoring, test), basta una riga nella §11.

## Struttura della relazione
1. **Copertina**: occhiello "Human-Computer Interaction · Assignment 3", titolo "Relazione
   sull'accessibilità del sito ideaBlume", sottotitolo, poi GRUPPO (Gruppo A), COMPONENTI (Andrea
   Canale · Antonio Fallea · Alexandru Ioan Chindris · Lorenzo Rizzolo), CORSO (Human-Computer
   Interaction · a.a. 2026/27), DATA (oggi), SITO PUBBLICATO (https://andreock.github.io/hci_gruppo_a/).
2. **Indice** con numeri di pagina.
3. **Introduzione**: obiettivo e percorso in due cicli (analisi → correzione → nuova verifica, ripetuto).
   Massimo mezza pagina. Aggiungi una piccola figura del flusso, come la Figura 1 della relazione precedente.
4. **Strumenti e impostazioni**: una tabella con strumento, versione, configurazione, copertura,
   ciclo e scopo. Gli strumenti sono MAUVE++ 4.0.2 (strumento principale), AccessibilityChecker,
   ACHECKS/AChecker (WCAG 2.0 AA), axe-core 4.10.3 + Playwright 1.56.1, html-validate 9.7.1,
   Stylelint 16.25.0 e gli script locali. Indica i limiti di ciascuno (es. MAUVE++ non risolve sempre
   le variabili CSS, ACHECKS segue WCAG 2.0, i CAPTCHA impediscono scansioni immediate).
5. **Pagine analizzate**: le 50 pagine, come le abbiamo individuate e una tabella compatta per
   tipologia di pagina × IT/EN × strumenti eseguiti, più gli stati interattivi verificati in locale
   (menu mobile, filtri, FAQ, temi, moduli con errori, donazione in 5 passi, `file://`). La copertura è
   un criterio di valutazione: rendila evidente.
6. **Errori, avvisi e verifiche manuali**: come abbiamo distinto le tre categorie per ogni strumento.
   MAUVE++ distingue criteri segnalati e verifiche manuali; AccessibilityChecker distingue problemi
   critici, controlli superati, manuali e non applicabili; ACHECKS distingue known, likely e potential
   problems. Aggiungi una tabella PRIMA per strumento e categoria e i problemi di template contati una
   volta sola.
7. **Le principali tipologie di problema**: una sottosezione per tipologia, con i problemi di entrambi i
   cicli. Ognuna ha tre riquadri: **Che cosa non funziona**, **Quali difficoltà causa alle persone**
   (concreto, citando quando possibile le personas della relazione precedente, es. Davide con NVDA o
   Giuseppe con l'ingrandimento), **Che cosa abbiamo modificato**. Aggiungi un breve estratto prima/dopo
   preso da `git diff $BASE HEAD` sulla sorgente (`tools/build.py`, CSS, JS, markdown, i18n, mai
   sull'HTML generato), il criterio WCAG e l'hash del commit come badge. Spiega che la correzione
   è stata fatta nella sorgente comune e quindi vale per tutte le 50 pagine generate.
8. **Tabella riassuntiva**, esattamente con queste 4 colonne:
   | Problema rilevato | Pagine o elementi interessati | Correzione effettuata | Esito della nuova verifica |
   Nell'ultima colonna usa un badge "Risolto" / "Parzialmente risolto" / "Non risolto", con una nota
   breve sugli strumenti che lo confermano ("Risolto · MAUVE++ e axe"). Un problema confermato solo in
   locale e non sul sito pubblicato è "Parzialmente risolto · da riconfermare online". Raggruppa per
   tipologia. Non includere voci che non sono problemi di accessibilità del sito (es. il test di
   scorrimento instabile): vanno nella §11.
9. **Falsi positivi e scelte fatte**: parti dalla tabella "Segnalazioni residue" del resoconto (1.1.1
   su SVG `aria-hidden`, 1.4.3, 1.4.1, 2.4.7, 1.4.10, 1.3.5, 1.3.1, 1.4.5) e aggiornala secondo la
   riconciliazione. Per ognuna indica lo strumento che la riporta, la verifica fatta, la valutazione e
   l'eventuale revisione. Usa riquadri "Perché" per le scelte: per esempio non aggiungere un nome agli
   SVG decorativi, non modificare il sito solo per alzare il punteggio, intervenire su `build.py`
   invece che pagina per pagina, preferire HTML nativo ad ARIA, scegliere colori vicini al brand.
10. **Validazione HTML e CSS**: html-validate e Stylelint PRIMA (`$BASE`) e DOPO (`HEAD`), con i numeri
    presi dagli output in `dati/`. Indica gli errori reali corretti e le preferenze del linter non
    applicate, con il motivo.
11. **Nuova verifica**:
    - online: confronto PRIMA/DOPO per strumento, con una tabella e un grafico a barre semplice in
      SVG inline (per MAUVE++ la media di accessibilità e completezza e i criteri segnalati per pagina);
    - locale: la tabella "Esito della nuova verifica" con PRIMA (`$BASE`) e DOPO (`HEAD`) affiancati
      (HTML, CSS, axe temi chiaro e scuro, console, h1, percorsi, `file://`, contrasti, link e ancore,
      responsive, zoom 200%, bersagli);
    - nuovi problemi eventualmente introdotti e funzionamento del prototipo (build senza differenze,
      percorsi e stati interattivi superati);
    - una tabella compatta dei cicli di verifica che unisca i cicli 1–6 del resoconto e il loop;
    - in una riga, le modifiche del diff che non riguardano l'accessibilità (test, refactoring).
12. **Errori rimasti e avvisi da verificare**: per ciascuno, perché non è stato risolto e che cosa
    servirebbe. Includi le verifiche manuali ancora necessarie: NVDA o VoiceOver, browser non Chromium,
    persone reali. Ricorda che gli strumenti automatici non dimostrano da soli la conformità.
13. **Uso dell'IA**: nel primo ciclo Codex (ispezione del repository, esecuzione dei validatori,
    interpretazione delle segnalazioni, proposte di modifica, ripetizione dei test); nel secondo ciclo
    Claude Code (scansioni ripetute con i tre validatori, raggruppamento dei problemi, proposte di
    correzione). Spiega che cosa abbiamo verificato noi: diff di ogni commit, build, test riproducibili,
    nuove scansioni, segnalazioni non confermate mantenute invece di "aggiustare" il punteggio.
    Inserisci `[DA COMPLETARE]` per le verifiche personali del gruppo.
14. **Conclusioni**: massimo 5 righe.
- **Appendice A**: tabella delle 50 pagine con PRIMA e DOPO per MAUVE++ (accessibilità, completezza,
  criteri segnalati) e l'esito degli altri due strumenti, in corpo piccolo.
- **Appendice B**: elenco dei commit `$BASE..HEAD` (hash breve, data, messaggio, ciclo) e i comandi di
  riproduzione, compresi i comandi git per ricreare PRIMA e DOPO.
- **Appendice C**: estratti dei prompt usati.

## Schermate
Solo per 3–4 correzioni significative (es. il nome del logo nell'albero di accessibilità, il contrasto,
il focus visibile, i bersagli a 24 px):
- servi in locale i due worktree (`/tmp/a11y-prima` e `/tmp/a11y-dopo`, già compilati) su due porte diverse;
- con Playwright cattura lo stesso elemento nei due stati, a 2x, ritagliato sull'area utile. Per il
  logo puoi mostrare l'albero di accessibilità (`page.accessibility.snapshot()`) prima e dopo come
  piccolo riquadro di codice;
- impagina le due immagini affiancate con le didascalie "Prima (versione Assignment 2)" e
  "Dopo (Assignment 3)" e un alt descrittivo.
Non allegare i report completi dei validatori.

## Stile grafico (ripreso dalla relazione precedente)
- Pagina A4, margini circa 18 mm, fondo bianco. Testo #2c1f24, Inter 10–10.5pt, interlinea 1.45.
- Titoli in Bricolage Grotesque ExtraBold, colore #3b1d2a. Il numero di sezione va in arancio #bf4a12,
  con una linea sottile arancio sotto l'H1. Ogni sezione principale inizia su una nuova pagina.
- Copertina: banda superiore bordeaux #3b1d2a (circa il 45% della pagina) con occhiello arancio-oro
  #f4b93e, titolo grande in crema #fbf6ee e sottotitolo; sotto, una linea arancio #bf4a12 e un fondo
  crema #fbf6ee con le etichette in maiuscolo arancio e i valori in scuro.
- Tabelle: didascalia "Tabella N." sopra; intestazione #3b1d2a con testo bianco; righe alternate
  #f8f2ea; bordi #d9cbbd sottili; `break-inside: avoid` sulle righe.
- Riquadri: azzurro #e2eff4 con bordo sinistro #1d5b73 (spiegazioni e motivazioni), verde #e3f2e6
  (risolto), pesca #fbeadd (problema), giallo #fdf1d0 con testo #5c3e00 (segnaposto DA COMPLETARE).
- Badge a pillola per esiti, strumenti, cicli ("Ciclo 1", "Ciclo 2") e hash dei commit (monospazio).
- Codice in monospazio 8.5pt su fondo #f8f2ea; nei diff, righe rimosse su fondo pesca e aggiunte su fondo verde.
- Piè di pagina su tutte le pagine tranne la copertina: a sinistra "Gruppo A · Accessibilità del
  sito ideaBlume", a destra "Pagina X di Y" (footerTemplate di Chrome con pageNumber/totalPages).
- Font: cerca Inter e Bricolage Grotesque in `fonts/` o nei sorgenti della relazione precedente e
  incorporali con @font-face. Se non ci sono, scaricali da Google Fonts nella cartella della relazione.

## Accessibilità del PDF
- `<html lang="it">` (con `lang="en"` sui termini inglesi lunghi), gerarchia dei titoli senza salti,
  tabelle con `<th scope>` e `<caption>`, alt su ogni immagine, contrasto almeno 4.5:1 anche nei badge.
- PDF taggato (Chrome `tagged: true`), con titolo nei metadati e segnalibri dai titoli.

## Generazione e controllo
1. Prima i riferimenti git e i controlli locali PRIMA/DOPO, poi `riconciliazione.md`, poi l'HTML e
   il CSS, infine il PDF.
2. Indice: genera, ricava le pagine dei titoli con `pdftotext`, inseriscile e rigenera finché i numeri
   non cambiano più.
3. Controlli:
   - rendi ogni pagina in PNG e guardale tutte: niente testo tagliato, tabelle spezzate male, pagine
     quasi vuote, immagini sgranate;
   - `pdffonts`: font incorporati; `pdfinfo`: A4, titolo corretto, taggato;
   - ricalcola con uno script ogni numero citato dai file sorgente e dagli output in `dati/` (medie
     MAUVE++ 92,7% e 88,1%, conteggi, pagine) e verifica che coincida;
   - ogni riga della tabella riassuntiva deve avere almeno un commit in `$BASE..HEAD` che la giustifica,
     e ogni estratto di codice deve essere presente in quel diff;
   - nessuna classificazione del resoconto deve essere contraddetta senza spiegazione
     (confronta con `riconciliazione.md`);
   - cerca nel testo "agente", "Claude ha", "Codex ha", "è stato generato" fuori dalla §13 e riformula;
   - elenca alla fine tutti i `[DA COMPLETARE]` rimasti, così il gruppo sa che cosa compilare.
4. Rimuovi i worktree temporanei. Non fare commit né push: lascia i file in `a11y/relazione/`.
