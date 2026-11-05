# Assignment 3 — verifica e correzione dell'accessibilità

**Gruppo A**  
**Componenti:** Andrea Canale · Antonio Fallea · Alexandru Ioan Chindris · Lorenzo Rizzolo  
**Prototipo analizzato:** `assignment2/website/`  
**Data della verifica:** 5 novembre 2026

## Sintesi

È stato analizzato l'intero prototipo ideaBlume, composto da 25 pagine italiane e 25 equivalenti inglesi. Come richiesto dalla specifica, lo strumento automatico principale è stato **[MAUVE++](https://mauve.isti.cnr.it/)**; è stato inoltre usato **[Accessibility Checker](https://www.accessibilitychecker.org/)** sulla homepage. I risultati sono stati confrontati con axe-core, validatori HTML/CSS e test automatici degli stati interattivi.

Il controllo ha prodotto una correzione aggiuntiva reale: il nome accessibile del collegamento-logo non conteneva tutta l'etichetta visibile. Dopo la correzione, la suite locale completa non rileva violazioni axe, errori HTML/CSS, overflow o regressioni funzionali. MAUVE++ continua invece a classificare sei criteri come errori su tutte le pagine e altri due su alcune pagine. L'ispezione delle occorrenze e i controlli incrociati mostrano che si tratta in prevalenza di limitazioni o falsi positivi del validatore; sono pertanto riportati come **segnalazioni residue da verifica manuale**, non cancellati dal resoconto.

## Metodo e strumenti

Il lavoro è stato svolto in cicli: build, analisi, classificazione delle segnalazioni, correzione nel sorgente, nuova build e ripetizione degli stessi controlli. Poiché le pagine sono generate da `tools/build.py`, le modifiche sono state applicate al generatore, ai CSS e al JavaScript sorgente, poi propagate a tutte le 50 pagine.

| Strumento | Configurazione | Copertura e scopo |
|---|---|---|
| **MAUVE++ 4.0.2** | WCAG 2.1, livello AA, desktop/Windows/Chrome | Tutti i 50 URL pubblici, una scansione per pagina; strumento obbligatorio principale |
| **Accessibility Checker** | scansione della pagina pubblica | Homepage; secondo controllo tra gli strumenti indicati nella specifica |
| axe-core 4.10.3 + Playwright 1.56.1 | WCAG 2.0/2.1/2.2 A e AA, tema chiaro e scuro | Tutte le pagine locali e stati interattivi |
| html-validate 9.7.1 | regole strutturali e di accessibilità | Tutti i 50 HTML generati |
| Stylelint 16.25.0 | parsing dei fogli di stile | Tre CSS condivisi |
| Script locali | contrasto, link, dati, responsive e percorsi | Controlli complementari e regressioni |

La scansione esterna ha riguardato il sito pubblicato all'indirizzo `https://andreock.github.io/hci_gruppo_a/`. Al momento del controllo la pubblicazione corrispondeva alla versione precedente alle correzioni locali di questo assignment. Per questo i risultati MAUVE++ costituiscono la baseline esterna completa; dopo la pubblicazione del ramo aggiornato occorre ripetere la stessa scansione per ottenere il confronto esterno definitivo.

## Copertura

Sono state esaminate home, elenco progetti, ricerca, 404, dieci pagine progetto, donazione e conferma, programma, come funziona, proponi, candidatura, collaborazione, contatti, FAQ, chi siamo e accessibilità, in italiano e inglese. La tabella completa dei 50 URL e dei punteggi MAUVE++ è in [`risultati_mauve.md`](risultati_mauve.md).

I controlli locali coprono inoltre menu mobile aperto e chiuso, toggletip, ricerca con e senza risultati, filtri e ordinamento, FAQ aperte e filtrate, tema chiaro e scuro, cambio lingua, moduli vuoti e con errori, donazione in cinque passi, campagna conclusa, ritorno con i pulsanti del browser e apertura diretta tramite `file://`.

## Risultati degli strumenti richiesti

### MAUVE++

Sulle 50 pagine la percentuale di accessibilità varia dall'89% al 96%, con media **92,7%**; la completezza varia dall'84% al 93%, con media **88,1%**. MAUVE++ ha classificato come errori sei criteri su tutte le pagine:

- 1.1.1 Contenuti non testuali;
- 1.3.1 Informazioni e relazioni;
- 1.4.1 Uso del colore;
- 1.4.3 Contrasto minimo;
- 1.4.5 Immagini di testo;
- 2.4.7 Focus visibile.

Su 16 pagine con moduli, filtri o elenchi sono comparsi anche 1.3.5 Identificare lo scopo dell'input e 1.4.10 Reflow. Le occorrenze sono state aperte nel dettaglio e confrontate con DOM, CSS, axe, misure di contrasto e test responsive. La classificazione è riportata nella sezione “Segnalazioni residue”.

### Accessibility Checker

La homepage pubblica ha ottenuto **72/100**, con **1 problema critico**, 52 controlli superati, 22 verifiche manuali e 45 controlli non applicabili. Il problema critico riguardava WCAG 2.5.3, “Label in Name”: il collegamento-logo aveva come nome accessibile `ideaBlume, vai alla home`, mentre l'etichetta visibile includeva anche il payoff. Questo può impedire a chi usa il controllo vocale di attivare l'elemento pronunciando il testo che vede.

La correzione è stata applicata in `tools/build.py` per entrambe le lingue: rimosso l'`aria-label` divergente e aggiunto un testo solo per tecnologie assistive che completa il nome del collegamento senza alterare la grafica. La build e la suite locale sono state poi ripetute. Nuove scansioni immediate sul servizio sono state impedite dal CAPTCHA; la scansione esterna va quindi ripetuta dopo la pubblicazione.

## Problemi rilevati e modifiche

| Problema rilevato | Pagine o elementi interessati | Difficoltà causata | Correzione effettuata | Esito |
|---|---|---|---|---|
| Nome accessibile del logo diverso dall'etichetta visibile, WCAG 2.5.3 | Header di tutte le pagine, IT e EN | I comandi vocali basati sul testo visibile possono non trovare il collegamento | Eliminato l'`aria-label` divergente e completato il nome accessibile con testo nascosto localizzato | **Risolto localmente**; da riconfermare sul sito pubblicato |
| Intestazioni dinamiche inizialmente vuote | Donazione, candidatura, collaborazione, contatti e risultati; IT e EN | Struttura incompleta prima del JavaScript o in caso di errore dello script | Inseriti testi di fallback localizzati | **Risolto**: HTML valido, axe senza violazioni |
| Regioni di ricerca non nominate esplicitamente | Home, ricerca e 404; IT e EN | Landmark omonimi più difficili da distinguere | Aggiunto nome localizzato ai form con `role="search"` | **Risolto** |
| Posizione dell'elenco non ripristinata in modo affidabile | Elenco progetti → progetto → Indietro | Chi usa tastiera o ingrandimento perde il punto raggiunto | Ripristino di filtri e posizione su `pageshow`, usando `sessionStorage` | **Risolto**: posizione iniziale e ripristinata coincidono |
| Due `<br>` usati come spaziatori | Riquadri “Chi può proporre”, IT e EN | Allineamento incoerente e markup presentazionale | Rimossi gli elementi; usato il layout flex già presente | **Risolto** |
| Sei link d'azione alti 21 px | Passi della pagina “Proponi” | Bersaglio più difficile su touch o con ridotta precisione motoria | Impostata altezza minima di 24 px | **Risolto** |
| Test di scorrimento instabile con animazione | Suite dei percorsi | Possibile falso negativo nella verifica | Campionamento reso deterministico con scorrimento istantaneo | **Risolto** |

## Cicli di verifica

| Ciclo | Risultato | Intervento |
|---|---|---|
| 1 — controlli statici | 50 pagine; 329/329 dati; 1.702 link e 422 ancore; 180/180 contrasti | Nessun problema in dati, link e colori del design system |
| 2 — HTML/CSS | Individuati titoli dinamici vuoti e landmark da nominare | Aggiunti fallback e nomi accessibili; separati errori reali da preferenze del linter |
| 3 — axe e percorsi | axe 0; 103/105 percorsi | Corretto ritorno alla posizione e rimosso markup di spaziatura |
| 4 — responsive | Nessun overflow; sei target alti 21 px | Aumentata l'area cliccabile |
| 5 — MAUVE++ e Accessibility Checker | MAUVE++: 50/50 URL; Accessibility Checker: un errore 2.5.3 | Analizzate le occorrenze MAUVE++; corretto il nome accessibile del logo |
| 6 — nuova verifica locale | Validatori e suite senza errori | Nessuna regressione rilevata |

## Esito della nuova verifica locale

| Controllo | Esito |
|---|---:|
| HTML | 50/50 senza errori |
| CSS condivisi | 3/3 senza errori di parsing |
| axe, temi chiaro e scuro | 0 violazioni |
| Errori JavaScript o console | 0 |
| Pagine con numero di `h1` diverso da uno | 0 |
| Percorsi e stati interattivi | 105/105 superati |
| Apertura diretta `file://` | 8/8 superati |
| Contrasti | 180/180 conformi |
| Link e ancore | 1.702 link, 422 ancore, 0 problemi |
| Responsive 320, 375, 768 e 1280 px | nessun overflow |
| Zoom 200% | nessun overflow nelle pagine campione |
| Bersagli interattivi a 375 px | nessun target non esente sotto 24×24 px |

I report tecnici sono in `assignment2/website/docs/verifiche/`, in particolare `axe.md`, `percorsi.md`, `responsive.md`, `contrasti.md`, `link.md` e `dati.md`.

## Segnalazioni residue e verifiche manuali

Non sono state nascoste le segnalazioni che non è corretto “risolvere” modificando indiscriminatamente il codice:

| Segnalazione MAUVE++ | Verifica effettuata | Valutazione ed esito |
|---|---|---|
| 1.1.1 su SVG decorativi con `aria-hidden="true"` | Ispezione del DOM e controllo axe | Gli SVG sono intenzionalmente esclusi dall'albero accessibile e non necessitano di nome. Aggiungerlo introdurrebbe rumore. **Falso positivo probabile; verifica manuale consigliata.** |
| 1.4.3 contrasto | 180 combinazioni misurate nei due temi; axe su tutte le pagine | Tutte le combinazioni controllate rispettano la soglia; il validatore sembra non risolvere correttamente alcune variabili CSS. **Non riprodotto.** |
| 1.4.1 uso del colore | Ispezione di link, pulsanti e stati | I collegamenti sono sottolineati o presentati come pulsanti con forma e testo; lo stato non dipende soltanto dal colore. **Non riprodotto.** |
| 2.4.7 focus visibile | Navigazione da tastiera, screenshot e 105 percorsi | È presente uno stile `:focus-visible` evidente. **Non riprodotto; resta opportuna una prova manuale completa.** |
| 1.4.10 reflow | Viewport 320 px e zoom 200% | Nessun overflow orizzontale rilevato. **Non riprodotto.** |
| 1.3.5 scopo degli input | Ispezione dei moduli | Gli input di dati personali applicabili hanno `autocomplete`; filtri, ricerca e campi di progetto non raccolgono dati personali standardizzati. **Non applicabile alle occorrenze residue.** |
| 1.3.1 e 1.4.5 | Ispezione di struttura e immagini | Gerarchie, label e relazioni superano HTML/axe; non sono usate immagini contenenti testo essenziale. **Non riprodotto; da confermare con lettore di schermo.** |

Restano inoltre necessarie prove con NVDA o VoiceOver, browser diversi da Chromium e persone reali. Gli strumenti automatici, incluso MAUVE++, non dimostrano da soli la piena conformità WCAG.

## Uso dell'intelligenza artificiale

Codex è stato usato per ispezionare il repository, eseguire i validatori, interpretare le segnalazioni, proporre modifiche e ripetere i test. Le indicazioni dell'AI non sono state accettate automaticamente: ogni modifica è stata verificata con build, controllo del codice e test riproducibili. In particolare, i risultati MAUVE++ sono stati mantenuti nel resoconto quando non confermati dagli altri controlli, invece di modificare il sito soltanto per aumentare il punteggio.

## Riproduzione

Dalla directory `assignment2/website/`:

```bash
python3 tools/build.py
python3 tools/verifica-dati.py
python3 tools/verifica-link.py
python3 tools/contrasto.py
npm --prefix tools ci
npm --prefix tools run validate
npm --prefix tools run verify
```

Per il confronto esterno, dopo la pubblicazione aprire MAUVE++, selezionare WCAG 2.1 AA e ripetere una scansione per ciascuno dei 50 URL elencati in `risultati_mauve.md`.
