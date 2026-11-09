# Audit di accessibilità: loop su tutte le pagine del sito

## Obiettivo
Verificare l'accessibilità di TUTTE le pagine di {{SITO}} (es. https://www.esempio.it)
con tre validatori online, usando il browser:
1. MAUVE++: https://mauve.isti.cnr.it (WCAG 2.1 livello AA)
2. AccessibilityChecker: https://www.accessibilitychecker.org
3. ACHECKS / AChecker: https://achecks.org/achecker

Ogni iterazione elabora un piccolo lotto di pagine, salva i risultati e si ferma.
Lo stato si trova solo nei file sotto `a11y/`: non contare sulla memoria delle iterazioni precedenti.

## File di stato
- `a11y/pages.json`: [{url, template, status: "todo"|"done"|"error", tries}]
- `a11y/results/<slug>.json`: risultati della singola pagina
- `a11y/log.md`: una riga per iterazione
- `a11y/REPORT.md` e `a11y/issues.csv`: output finale
- `a11y/DONE`: va creato solo a lavoro concluso

## Ogni iterazione

### 0. Controllo
- Se esiste `a11y/DONE`, rispondi "Audit completato" e termina.
- Se `a11y/pages.json` non esiste, esegui la Fase A. Se restano pagine "todo" (o "error" con tries < 3), esegui la Fase B. Altrimenti esegui la Fase C.

### Fase A: scoperta delle pagine (solo la prima volta)
1. Leggi robots.txt e tutti i sitemap dichiarati, compresi i sitemap index annidati, /sitemap.xml e /sitemap_index.xml.
2. Completa l'elenco con un crawl dei link interni partendo dalla home: stesso dominio, profondità massima {{PROFONDITA}} (default 5), inclusi menu, header e footer.
3. Normalizza gli URL: togli #frammenti e parametri di tracking (utm_*, gclid, fbclid), unifica lo slash finale, elimina i duplicati.
4. Escludi le aree riservate o di login, le varianti di filtro e ordinamento e le paginazioni oltre la pagina 3.
   Elenca a parte in `a11y/non-html.md` i file non HTML (PDF, documenti): vanno verificati anche loro, ma con altri strumenti.
5. Assegna a ogni pagina un "template" (home, articolo, elenco, scheda, form, ecc.) in base all'URL e alla struttura del markup.
6. Salva `pages.json`, scrivi il totale in `log.md` e termina l'iterazione.

### Fase B: validazione di un lotto
Prendi le prime {{LOTTO}} pagine da fare (default 3). Per ogni pagina e per ciascuno dei tre strumenti:
1. Apri lo strumento, inserisci l'URL nel campo di verifica della singola pagina, avvia il test e attendi il risultato (timeout di 3 minuti).
   - MAUVE++: modalità pagina singola, WCAG 2.1 livello AA. MAUVE++ analizza il codice HTML/CSS. Se il risultato sembra quello di una pagina vuota, o è identico per URL diversi (contenuto generato via JavaScript), scrivilo in "note".
   - AccessibilityChecker: verifica gratuita della singola URL.
   - ACHECKS: AChecker (WCAG 2.0 AA). Se viene proposto anche Lighthouse, registralo come risultato separato.
2. Estrai i dati: punteggio (se c'è), numero di errori e di avvisi o punti da verificare a mano. Per ogni problema estrai il criterio WCAG (es. 1.1.1), il livello, la descrizione, il selettore o lo snippet dell'elemento e il numero di occorrenze.
3. Salva `a11y/results/<slug>.json` in questo formato:
   {url, template, checked_at, tools: {mauve, accessibilitychecker, achecks}}
   Ogni strumento ha la forma {status: "ok"|"skipped"|"error", score, errors, warnings, issues: [...], note}.
4. Aspetta almeno 20 secondi tra due invii allo stesso strumento.
5. Aggiorna `pages.json`: "done" se almeno uno strumento ha restituito risultati, altrimenti "error" con tries + 1.
   Aggiungi a `log.md` una riga con data, pagine elaborate, pagine rimanenti ed eventuali blocchi.

### Fase C: report finale
Scrivi `a11y/REPORT.md` in italiano con:
- Sintesi: pagine verificate sul totale, pagine non verificabili e il motivo.
- Problemi raggruppati per criterio WCAG, ordinati per numero di pagine coinvolte, indicando quali strumenti li hanno rilevati. Un problema confermato da più strumenti ha priorità più alta.
- Problemi di template (header, footer, menu, banner dei cookie), riportati una volta sola invece che per ogni pagina.
- Le 10 pagine con più problemi.
- Le discrepanze tra strumenti (problemi rilevati da uno solo), da verificare a mano.
- Una nota finale: i validatori automatici coprono solo una parte dei criteri WCAG. Servono anche verifiche manuali (navigazione da tastiera, screen reader, contrasto nel contesto reale).
Genera anche `a11y/issues.csv` con le colonne url, strumento, criterio, livello, descrizione, elemento, occorrenze. Poi crea `a11y/DONE`.

## Regole
- È solo un audit: non modificare il codice del sito.
- Non aggirare CAPTCHA, login o limiti d'uso. Se uno strumento chiede di accedere, mostra un CAPTCHA o ha esaurito le verifiche gratuite, segnalo come "skipped" con il motivo e prosegui con gli altri.
  Se lo stesso blocco si ripete per 3 iterazioni consecutive, smetti di usare quello strumento e scrivilo in `log.md`.
- Non inventare dati: se un valore non è leggibile, lascia null e spiega il motivo in "note".
- Ogni iterazione elabora un solo lotto, senza superare {{LOTTO}} pagine.
