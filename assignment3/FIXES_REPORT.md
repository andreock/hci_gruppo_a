# Rapporto delle correzioni di accessibilità

Data: 2026-11-09 · Branch `assignment3` · Fonti: `a11y/issues.csv` (MAUVE++, AccessibilityChecker, ACHECKS/Lighthouse), elenco dei fix in `a11y/fixes.json`, registro in `a11y/fixes-log.md`.

Gli HTML sono generati da `tools/build.py` e sono in `.gitignore`: ogni correzione è stata fatta nelle sorgenti. Il diff degli HTML è stato controllato confrontandoli con una copia presa prima di ogni build (`a11y/fix-F0x-prima/`, `a11y/chiusura-prima/`). Ogni build è stata lanciata con `IB_OGGI=2026-11-05`, così `data/ib-dati.js` non cambia.

## Fix completati

| Fix | Criterio | Correzione | File modificati | Pagine | Commit |
|---|---|---|---|---|---|
| F01 Indicatore di focus del link «Salta al contenuto» | 2.4.7 (AA) | `outline: 3px solid var(--c-focus-skip)` dichiarato su `.skip-link:focus`; token `--c-focus-skip` scurito per arrivare almeno a 3:1 sullo sfondo della pagina (chiaro #f4b93e → #bc830b, 3,05:1; scuro #a33f0f → #b64611, 3,34:1) | `css/ideablume.css`, `tools/contrasto.py`, `docs/verifiche/contrasti.md` | tutte le 50 | 78cbbec |
| F02 Marchio `idea<b>Blume</b>` con `<b>` usato solo per lo stile | 1.4.4 (AA), AChecker #116 | `<b>` → `<span class="brand__accent">` nell'header e nel footer; selettori CSS aggiornati, aspetto invariato | `tools/build.py`, `css/ideablume.css`, `docs/verifiche/anteprima-design-system.html` | tutte le 50 | 1541ed1 |
| F03 `role="status"` sull'`<h2>` dei risultati di ricerca | 1.3.1 / 4.1.2 (A) | `role="status"` spostato su un `<div>` che contiene l'`<h2>`; tolto `aria-live`, ridondante; JS invariato | `tools/build.py` | cerca.html, en/cerca.html | 6e864be |
| Chiusura: limiti noti della dichiarazione | — | Nel limite su nomi, ruoli e stati è stato aggiunto che anche l'annuncio dei messaggi di stato non è ancora stato provato con uno screen reader (IT ed EN) | `data/sito.json` | accessibilita.html, en/accessibilita.html | e8a3ae1 |

Verifiche fatte per ogni fix: diff degli HTML generati (cambiano solo le righe attese), `html-validate` senza errori, `stylelint` senza errori quando è stato toccato il CSS, `tools/contrasto.py` senza coppie sotto soglia.

## Falsi positivi

| Id | Segnalazione | Motivo per cui è stata scartata |
|---|---|---|
| FP01 | MAUVE++ ARIA6: SVG senza etichetta (1.1.1) | Gli `svg.brand__mark` e `svg.icon` hanno `aria-hidden="true"` e `focusable="false"` e sono accompagnati da testo visibile o `.vh`: sono decorativi |
| FP02 | MAUVE++ G18: contrasto (1.4.3) | Ricalcolato sui token: `span.vh` è nascosto visivamente; gli altri elementi segnalati vanno da 5,6:1 a 16:1. MAUVE non risolve sfondi trasparenti, `color-mix` e `backdrop-filter`. `contrasto.py`: 180/180 coppie conformi |
| FP03 | MAUVE++ F73, AChecker #86/#55: link distinti solo dal colore (1.4.1) | Sono pulsanti `a.btn` isolati, con sfondo pieno o bordo da 2 px e forma a pillola, non link dentro un testo; i `.btn--ghost` sono anche sottolineati |
| FP04 | MAUVE++ G140: struttura e presentazione (1.3.1, 1.4.5) | È un controllo manuale ancorato a `<html>`. Le pagine usano HTML semantico e un solo CSS esterno, e non ci sono immagini di testo |
| FP05 | AChecker #245 e altri, MAUVE++ F46/H73: tabelle senza id/headers (1.3.1) | Le tabelle hanno un solo livello di intestazioni per asse, `th scope` e `<caption>`: la tecnica H63 basta, quindi id/headers (H43) sarebbe ridondante |
| FP06 | MAUVE++ H98: autocomplete mancante (1.3.5) | I campi con dati personali hanno già `autocomplete`. Quelli segnalati (messaggi, titolo, budget, filtri, select di categorie) non rientrano tra le finalità previste dal criterio 1.3.5 |
| FP07 | MAUVE++ C38: reflow di `div.field` (1.4.10) | Label a blocco, campi `width:100%` con `max-width`: nessuno scorrimento orizzontale a 320 px e con zoom al 200% (`tools/responsive.js`) |
| FP08 | AChecker #110: lingua delle parti nelle pagine EN (3.1.2) | Già rispettato: il link della lingua ha `lang="it"` e i commenti in italiano hanno `<p lang="it">` |
| FP09 | MAUVE++ G199/ARIA19/ARIA5: messaggi di stato (4.1.3) | Già rispettato: gli errori hanno `role="alert"`, le conferme `role="status"`. I moduli di ricerca della home e della 404 portano a un'altra pagina |
| FP10 | Avvisi generici da verificare a mano (AChecker «potential problems», MAUVE++ warning) | Sono richieste di controllo manuale, non errori; sul markup risultano rispettati (dettagli in `fixes.json`). Le parti che richiedono uno screen reader sono elencate più sotto |

## Fix da decidere

Nessuno. Nessun fix ha richiesto informazioni che il gruppo non avesse già (contenuto delle immagini, trascrizioni, scelte del brand). L'unico cambio di colore (F01) è il token dell'anello di focus dello skip link. Il gruppo può comunque confermare che la tonalità più scura (#bc830b chiaro, #b64611 scuro) vada bene per il brand.

## Verifiche manuali ancora necessarie

1. **Verifica nel browser dei tre fix**: il permesso per Playwright è stato negato, quindi non è stata fatta.
   - F01: premere Tab al caricamento della pagina, nel tema chiaro e nel tema scuro, e controllare che l'anello attorno a «Salta al contenuto» si veda.
   - F02: controllare che «Blume» abbia ancora il colore d'accento nell'header e nel footer.
   - F03: dopo una ricerca, controllare che il numero di risultati venga annunciato.
2. **Screen reader (NVDA + Firefox, VoiceOver + Safari)**:
   - l'annuncio di `role="status"` nella ricerca (cerca.html, IT/EN) e nelle conferme dei moduli;
   - lo spostamento del focus e la lettura dei riepiloghi di errore con `role="alert"`;
   - nella navigazione per intestazioni, l'`<h2>` dei risultati di ricerca deve comparire;
   - la lettura di `aria-expanded` nel menu mobile e nei toggletip, e di `aria-current` nella navigazione;
   - il cambio di lingua sui commenti `lang="it"` delle pagine EN.
3. **Tastiera**: il percorso completo (ricerca → progetto → donazione → conferma) va ripetuto dopo F01, controllando che il focus si veda su tutti i controlli. `tools/percorsi.js` lo copre in automatico ma non giudica quanto il focus sia visibile.
4. **Ingrandimento e comandi vocali**: provare zoom al 400% e ingranditore di sistema, e comandi vocali (Voice Control/Dragon) sui pulsanti, perché il nome visibile deve coincidere con quello accessibile (2.5.3).
5. **Nuovo audit**: le 50 pagine in `a11y/pages.json` sono in "todo". Va lanciato di nuovo il loop di audit (MAUVE++, AChecker, ACHECKS) per confermare che le segnalazioni di F01, F02 e F03 non ci siano più.
