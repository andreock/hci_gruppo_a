# Correzione degli errori di accessibilità

## Contesto
Gli HTML nella radice del progetto e in `en/` sono GENERATI da `build.py` a partire da file
markdown, template e stringhe di traduzione (`i18n/`, `data/`). Il loop di audit li ha
verificati con MAUVE++, AccessibilityChecker e ACHECKS. I risultati sono in:
- `a11y/REPORT.md`: sintesi e priorità
- `a11y/issues.csv`: url, strumento, criterio, livello, descrizione, elemento, occorrenze
- `a11y/results/<slug>.json`: dettaglio per pagina

## Regola fondamentale
Non modificare MAI direttamente i file .html generati: alla build successiva le modifiche
andrebbero perse. Ogni correzione va fatta nella sorgente corrispondente:
- testo, titoli, alt delle immagini, link → il file markdown della pagina
- struttura comune (head, lang, header, menu, footer, skip link, landmark) → il template usato da build.py
- etichette ed elementi ripetuti in più lingue → `i18n/` (correggi sia IT sia EN)
- contrasto, focus visibile, dimensioni, spaziatura, reflow → `css/`
- widget interattivi (ricerca, form di donazione, menu mobile) → `js/` e il relativo markup nel template
- dati strutturati usati nelle pagine (es. elenco dei progetti) → `data/`
- trasformazioni sbagliate fatte dal generatore (es. heading saltati, tabelle senza th, immagini senza alt) → `build.py` stesso

## Ogni iterazione

### 0. Controllo e preparazione
- Se esiste `a11y/FIXES_DONE`, rispondi "Correzioni completate" e termina.
- Se `a11y/fixes.json` non esiste, svolgi la preparazione:
  1. Leggi README.md, `build.py` (cercalo anche in `tools/`) e `docs/` per capire dove stanno
     i markdown, quali template vengono usati, come si gestiscono le due lingue e come si lancia la build.
  2. Esegui la build una volta su un working tree pulito e verifica con `git status` che non
     produca differenze. Se ne produce, fermati e segnalalo: significa che gli HTML versionati
     non corrispondono alle sorgenti.
  3. Leggi `issues.csv` e raggruppa i problemi in "fix": un fix è una causa unica, anche se si
     presenta su molte pagine (es. "manca lo skip link nel template" vale per tutte le pagine).
     Per ogni fix individua il file sorgente responsabile, risalendo dall'HTML generato alla sorgente.
  4. Ordina i fix per priorità: prima i problemi di template/CSS/i18n che toccano molte pagine,
     poi quelli segnalati da più strumenti, poi livello A prima di AA, poi le pagine con più errori.
  5. Scarta come "falso positivo" i problemi che non si riproducono sul markup reale, spiegando il
     motivo. Due casi tipici: un elemento nascosto ma accessibile agli screen reader, oppure un
     avviso di "verifica manuale" che risulta già rispettato.
  6. Salva `a11y/fixes.json`:
     [{id, titolo, criterio_wcag, livello, strumenti, pagine, file_sorgente,
       status: "todo"|"done"|"falso_positivo"|"da_decidere", note}]
     Poi termina l'iterazione.

### 1. Correzione (un fix per iterazione)
Prendi il primo fix con status "todo".
1. Leggi il file sorgente e l'HTML generato di almeno una delle pagine coinvolte.
2. Applica la correzione minima nella sorgente, nel rispetto delle WCAG 2.1 AA. Preferisci HTML
   semantico nativo ad ARIA: usa ARIA solo dove l'HTML non basta, e mai in modo ridondante.
3. Testi alternativi: scrivi un alt che descriva il significato dell'immagine nel contesto della
   pagina, oppure alt="" se è decorativa. Se non riesci a capire che cosa mostra l'immagine,
   non inventare nulla: metti il fix in "da_decidere" con la domanda da fare.
4. Contrasto: ricalcola il rapporto (minimo 4.5:1 per il testo normale, 3:1 per il testo grande e
   per i componenti dell'interfaccia) e scegli il colore più vicino a quello originale che lo
   rispetti. Cambia la variabile CSS, non i singoli punti in cui il colore è usato.
5. Lingue: se il problema compare anche nella versione inglese, correggi anche quella (markdown EN
   o `i18n/`). Controlla che `lang` sia corretto su `<html>` e sui passaggi in un'altra lingua.
6. Lancia `build.py`.
7. Verifica:
   - con `git diff` sugli HTML generati, che siano cambiate solo le parti attese;
   - `npx html-validate` sui file toccati (usa `.htmlvalidate.json`) e `npx stylelint "css/**/*.css"`
     se hai modificato il CSS, quando gli strumenti sono già installati o installabili;
   - che il problema non compaia più nelle pagine coinvolte, leggendo il markup generato;
   - se hai modificato il JS, che il widget funzioni da tastiera (Tab, Shift+Tab, Invio, Esc),
     abbia un focus visibile e annunci correttamente gli stati (aria-expanded, aria-live).
8. Se la verifica fallisce, annulla le modifiche di questo fix (`git checkout` dei file toccati),
   annota il motivo e lascia il fix in "todo" con tries + 1. Dopo 3 tentativi mettilo in "da_decidere".
9. Se la verifica passa: imposta il fix a "done" e fai un commit dedicato, con un messaggio del tipo
   `a11y: <titolo> (WCAG <criterio>)`. Il commit deve includere le sorgenti e gli HTML rigenerati.
10. In `a11y/pages.json` del loop di audit, rimetti a "todo" le pagine coinvolte, così che il
    prossimo audit le verifichi di nuovo.
11. Aggiungi una riga a `a11y/fixes-log.md` con data, fix, file modificati e pagine coinvolte.

### 2. Chiusura (quando non restano fix "todo")
Scrivi `a11y/FIXES_REPORT.md` in italiano con:
- i fix completati, con i file modificati e i commit;
- i falsi positivi e il motivo per cui sono stati scartati;
- i fix "da_decidere", ciascuno con la domanda precisa da fare (es. il contenuto di
  un'immagine, una scelta di colore del brand);
- le verifiche manuali ancora necessarie.
Aggiorna `accessibilita.html` (tramite la sua sorgente markdown, sia IT sia EN): non inserire
dichiarazioni di conformità, ma se la pagina elenca i limiti noti, aggiorna l'elenco.
Poi crea `a11y/FIXES_DONE`.

## Regole
- Non modificare direttamente gli HTML generati; non toccare `.idea/` e `.DS_Store`.
- Non cambiare contenuti, testi o design oltre a quanto serve per il singolo criterio.
- Un fix per iterazione e un commit per fix. Non fare push.
- Non inventare informazioni: quando un fix richiede conoscenze che non hai (contenuto delle
  immagini, trascrizioni di video, testo dei link ambigui), mettilo in "da_decidere".
