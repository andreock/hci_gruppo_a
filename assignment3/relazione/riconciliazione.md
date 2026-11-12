# Riconciliazione delle fonti (uso interno, non va nel PDF)

Preparata il 12/11/2026 prima di scrivere `relazione.html`. I riferimenti § seguono la numerazione della relazione: §2 strumenti, §5 tipologie, §8 validazione HTML/CSS, §9 nuova verifica, §10 punti aperti, §11 uso dell'IA.
Le fonti sono: resoconto (`resoconto_accessibilita.md`), risultati MAUVE++ (`risultati_mauve.md`), loop di audit (`REPORT.md`, `results/`, `issues.csv`, `log.md`), loop di correzione (`fixes.json`, `fixes-log.md`, `FIXES_REPORT.md`) e diff git `adc8f85..f2b73cf`.

## 0. Riferimenti e stato

| Voce | Valore |
|---|---|
| Commit dell'Assignment 3 | `5a6bddc` (2026-11-05 11:53) |
| PRIMA (`$BASE`) | `adc8f85` «Refactor journeys», 2026-11-05 10:31 |
| DOPO (`HEAD`) | `f2b73cf` «Update», 2026-11-11 11:05 |
| Stato di lavoro all'inizio | pulito (`git status`: nessuna modifica) |
| Prototipo | `assignment2/website/` (percorsi relativi a questa cartella) |
| Cartella `a11y/` del prompt | corrisponde ad `assignment3/` (il `.gitignore` del sito esclude `a11y/`: il loop è nato in `website/a11y/` ed è stato poi spostato). La relazione è in `assignment3/relazione/` |
| `{{PERCORSO_RELAZIONE_PRECEDENTE}}` | il segnaposto nel prompt non era compilato. Abbiamo usato `assignment2/relazione/` (`relazione.html`, `assets/stile.css`, `tools/genera_pdf.js`) |

## 1. Commit e cicli

| Commit | Data | Messaggio | Ciclo | Note |
|---|---|---|---|---|
| `5a6bddc` | 2026-11-05 | Assignment 3 | Ciclo 1 | Un unico commit con **tutte** le correzioni del ciclo 1, il resoconto, `risultati_mauve.md`, la configurazione dei linter, gli script npm e i report in `docs/verifiche/`. Le singole correzioni del ciclo 1 non hanno un hash separato. Contiene anche la rimozione di `assignment2/alex/` (pulizia, non riguarda il sito) |
| `6367c65` | 2026-11-09 11:27 | Add for branch deploy | Ciclo 2, preparazione (**ambiguo**) | Workflow con anteprime per branch e una riga in `build.py` (base della 404 nelle anteprime). È infrastruttura: rende pubblicabile l'anteprima su cui gira il loop. Non è una correzione di accessibilità |
| `78cbbec` | 2026-11-09 23:05 | a11y: Indicatore di focus del link «Salta al contenuto» (WCAG 2.4.7) | Ciclo 2 | F01 |
| `1541ed1` | 2026-11-09 23:08 | a11y: Marchio ideaBlume senza `<b>` presentazionale (WCAG 1.4.4) | Ciclo 2 | F02 |
| `6e864be` | 2026-11-09 23:09 | a11y: Intestazione dei risultati di ricerca senza role="status" (WCAG 1.3.1) | Ciclo 2 | F03 |
| `e8a3ae1` | 2026-11-09 23:11 | a11y: Limiti noti della dichiarazione di accessibilità aggiornati dopo le correzioni | Ciclo 2 | Chiusura (contenuto della dichiarazione) |
| `0e06454` | 2026-11-09 23:18 | Add relazione new | Ciclo 2 (dati) | Dati del loop: `results/`, `tmp-lotto*/`, `scripts-*`, report, copie degli HTML prima dei fix. Nessuna modifica al sito |
| `f2b73cf` | 2026-11-11 | Update | Documentazione (**ambiguo**) | `assignment2/relazione/04_verifica_V00.md` (+79, Assignment 2), `.gitignore` del sito, prompt della relazione. Nessuna modifica al sito pubblicato |

## 2. Pubblicazioni e scansioni online

| Scansione | Sito | Versione pubblicata | Data | Verifica |
|---|---|---|---|---|
| MAUVE++ 50/50 (`risultati_mauve.md`) e AccessibilityChecker sulla home (72/100) | produzione `https://andreock.github.io/hci_gruppo_a/` | `main` = `adc8f85` = `$BASE` | 5/11 (data del resoconto) | Su `main` dopo `adc8f85` ci sono solo `cbb6bc8` (9/11) e `ec0483d` (11/11). Il CSS servito oggi in produzione è identico byte per byte a quello di `$BASE`. **Corrisponde a `$BASE`.** Non è verificabile l'ora esatta della pubblicazione rispetto alla scansione |
| Loop di audit: MAUVE++ 50/50, AChecker 50/50, Lighthouse 50/50, AccessibilityChecker 3/50 | anteprima `.../anteprime/assignment3/` | `6367c65` = `$BASE` + ciclo 1 + workflow | 9/11, `checked_at` dalle 11:00 alle 15:04 | L'anteprima esiste solo dal push di `6367c65` (commit delle 11:27). I `checked_at` del lotto 1 (11:00) sono quindi **arrotondati**. I commit del ciclo 2 sono delle 23:05–23:11: **tutte le scansioni del loop sono precedenti al ciclo 2.** Per il ciclo 1 il loop è un DOPO, per il ciclo 2 è un PRIMA |
| Dopo il ciclo 2 | anteprima | `HEAD` | — | **Nessuna scansione online.** `pages.json` è tutto «todo» (rimesso a todo dal loop di correzione). Il 12/11 abbiamo verificato che le 50 pagine servite dall'anteprima coincidono con la build di `HEAD`: differiscono solo per la data di riferimento della build (9/11 o 11/11), e CSS e JS sono identici. **Esiti online del ciclo 2 da riconfermare** |
| Produzione oggi | produzione | `ec0483d` (`main`) | 11/11 | **Non contiene le correzioni dell'Assignment 3** (ha ancora `idea<b>Blume</b>`). Inoltre `ec0483d` rimuove la pagina `accessibilita.html` da `main`: la produzione ha oggi 24+24 pagine. Fuori da `$BASE..HEAD`, ma va detto: la versione corretta è solo sull'anteprima finché `assignment3` non viene unito a `main` |

## 3. Riconciliazione per problema

| # | Problema / criterio | Resoconto (ciclo 1) | risultati_mauve | Loop (audit + fix) | Diff git | Classificazione adottata | Commit |
|---|---|---|---|---|---|---|---|
| 1 | 2.5.3 nome del logo diverso dall'etichetta visibile | Errore critico di AccessibilityChecker sulla home (72/100). Risolto localmente, da riconfermare | — | AccessibilityChecker sull'anteprima (ciclo 1 incluso): 90/100, 0 critici su home, chi-siamo e come-funziona. MAUVE++ F96 (avviso 2.5.3) resta su `div.site-header__bar` come verifica manuale | `build.py`: `aria-label` rimosso, aggiunto `<span class="vh"> — vai alla home</span>`. i18n `brand_home_suffix` IT/EN | **Risolto · AccessibilityChecker (online, 3 pagine) e albero di accessibilità locale**. Riconfermato online, ma solo su 3 pagine: il template è comune | `5a6bddc` |
| 2 | Intestazioni dinamiche vuote (`empty-heading`) e `section` senza nome (`unique-landmark`) | Risolto, HTML valido | — | — | `build.py`: testi di fallback in donazione, candidatura, collabora, contatti, cerca (`h-pagine`) | **Risolto · html-validate** (PRIMA 12 errori in 10 file, DOPO 0). Pubblicato sull'anteprima (build verificata) | `5a6bddc` |
| 3 | Regioni di ricerca senza nome | Risolto | — | — | `build.py`: `aria-label` sui `form role="search"` (home, cerca, 404) | **Risolto · albero di accessibilità** (`search` → `search "Cerca un progetto"`). Non è un errore per html-validate o axe: è un miglioramento (una sola regione `search` per pagina) | `5a6bddc` |
| 4 | Posizione dell'elenco non ripristinata tornando indietro | Risolto (103/105 → 105/105) | — | — | `js/ideablume.js`: ripristino su `pageshow` con `e.persisted` (back-forward cache) | **Parzialmente risolto**. Con la suite attuale il test passa **anche su PRIMA** (945 → 945, sia con `percorsi.js` di `$BASE` sia con quello di `HEAD`). L'errore del ciclo 3 dipendeva dal test instabile (riga 7). Il codice nuovo riguarda la back-forward cache, che il test non esercita: va provato a mano | `5a6bddc` |
| 5 | Due `<br>` come spaziatori in «Proponi» | Risolto | — | — | `build.py`: `<br/><br/>` rimossi | **Risolto · percorsi e html-validate** (PRIMA «pulsanti allineati» NO e `void-style` 72; DOPO OK e 68) | `5a6bddc` |
| 6 | Sei link d'azione alti 21 px («Proponi») | Risolto | — | — | CSS `.howto > li > p > a:only-child { min-height: 24px }` | **Risolto · responsive.js** (PRIMA 6 bersagli 21 px, DOPO 0; misurati 29 px). Criterio 2.5.8 (WCAG 2.2), non coperto da MAUVE++ 2.1 | `5a6bddc` |
| 7 | Test di scorrimento instabile | Risolto | — | — | `tools/percorsi.js` | **Non è un problema del sito**: solo una riga nella §9.4 | `5a6bddc` |
| 8 | 2.4.7 focus visibile (MAUVE++ G195/F78 sullo skip link, 50 pagine) | **«Non riprodotto; resta opportuna una prova manuale»** | 2.4.7 su 50/50 | F01: su `:focus` era dichiarato solo `outline-color`; anello #f4b93e su crema 1,65:1 (tema scuro 2,83:1) | CSS: `outline: 3px solid var(--c-focus-skip)`, token #bc830b / #b64611; `contrasto.py` + coppia «focus-skip su page» | **Classificazione rivista**: il resoconto la riteneva non riprodotta, ma l'anello non raggiungeva 3:1 sullo sfondo adiacente. `contrasto.py` di HEAD su PRIMA: 2 coppie sotto soglia; su DOPO 0. **Parzialmente risolto · da riconfermare online (MAUVE++)**. Contrasto sul fondo scuro del link: 8,50 → 4,58 (chiaro) e 5,64 → 4,77 (scuro), sempre ≥ 3:1 | `78cbbec` |
| 9 | 1.4.4 `<b>` nel marchio (AChecker #116, 2 per pagina × 50) | — (AChecker non usato nel ciclo 1) | — | F02 | `build.py` + CSS `.brand__accent` | **Parzialmente risolto · da riconfermare online (AChecker)**. Locale: 0 `<b>Blume` nei 50 HTML (PRIMA 100). Screenshot del marchio prima/dopo identici al pixel. Va detto che il ridimensionamento del testo non era compromesso: è un controllo sul markup presentazionale | `1541ed1` |
| 10 | 1.3.1 / 4.1.2 `role="status"` sull'`<h2>` dei risultati (Lighthouse `aria-allowed-role`, informativo, cerca IT/EN) | — | — | F03 | `build.py`: `<div role="status"><h2 …>` | **Parzialmente risolto · da riconfermare online (Lighthouse)**. Locale: nell'albero di accessibilità l'`h2` torna intestazione di livello 2 dentro la regione `status`. L'annuncio va provato con NVDA/VoiceOver | `6e864be` |
| 11 | 1.1.1 ARIA6 su SVG `aria-hidden` | Falso positivo probabile | 1.1.1 su 50/50 | FP01, confermato | nessuna modifica | **Falso positivo (confermato da due analisi)** | — |
| 12 | 1.4.3 G18 contrasto del testo | Non riprodotto (180/180, MAUVE++ non risolve le variabili CSS) | 1.4.3 su 50/50 | FP02: `span.vh` nascosto; gli altri da 5,6:1 a 16:1; MAUVE++ non risolve sfondi trasparenti, `color-mix`, `backdrop-filter` | `contrasto.py` + 1 coppia (anello di focus, non testo) | **Falso positivo per il testo.** Da precisare che il «180/180» del ciclo 1 non comprendeva l'anello dello skip link sullo sfondo della pagina: la nuova coppia (riga 8) l'ha trovato. Oggi 182 misure (91 × 2) | — (`78cbbec` per la coppia nuova) |
| 13 | 1.4.1 F73 su `a.btn` | Non riprodotto | 1.4.1 su 50/50 | FP03 (anche AChecker #86/#55, avvisi) | nessuna | **Falso positivo** | — |
| 14 | 1.4.10 C38 su `div.field` | Non riprodotto | 1.4.10 su 16 | FP07 | nessuna | **Falso positivo**: responsive 0 overflow in PRIMA e DOPO | — |
| 15 | 1.3.5 H98 | Non applicabile alle occorrenze residue | 1.3.5 su 16 | FP06 | nessuna | **Falso positivo / non applicabile** | — |
| 16 | 1.3.1 e 1.4.5 G140 su `<html>` | Non riprodotto, da confermare con lettore di schermo | su 50/50 | FP04 | nessuna | **Verifica manuale ancorata a `<html>`**, non un errore localizzato | — |
| 17 | 1.3.1 tabelle senza id/headers (AChecker #245, MAUVE++ F46/H73) | — | — | FP05: `th scope` + `caption` bastano (H63) | nessuna | **Falso positivo**. È l'unica segnalazione confermata da due strumenti sugli stessi elementi: va spiegata | — |
| 18 | 3.1.2 lingua delle parti (AChecker #110, EN) | — | — | FP08 | nessuna | **Già rispettato** | — |
| 19 | 4.1.3 messaggi di stato (MAUVE++ G199/ARIA19/ARIA5) | — | — | FP09 | nessuna | **Già rispettato**; manca la prova con lettore di schermo | — |
| 20 | Avvisi generici (AChecker potential, MAUVE++ warning) | — | verifiche manuali per pagina | FP10 | nessuna | **Verifiche manuali**, non errori | — |
| 21 | Dichiarazione di accessibilità: limiti noti | — | — | Chiusura del loop | `data/sito.json` IT/EN | Aggiornamento di contenuto, **non un problema**: citato nella §9.4 e nella §10 | `e8a3ae1` |

## 4. Discrepanze numeriche

- **Medie MAUVE++**: ricalcolate da `risultati_mauve.md`, 92,68% e 88,12%, che arrotondate danno 92,7% e 88,1% come nel resoconto ✓. Loop (anteprima dopo il ciclo 1): 92,72% e 88,00%. Le differenze per pagina sono di ±1 punto su 20 pagine, senza una direzione costante (per esempio candidatura +1 e donazione −1). Non le attribuiamo alle correzioni.
- **Criteri segnalati per pagina**: identici tra baseline e loop (6 su 34 pagine, 8 su 16; in totale 332).
- **Verifiche manuali MAUVE++**: si riducono su home (6→5), cerca (6→4) e 404 (5→4), IT ed EN. Sono le pagine con il `form role="search"` a cui abbiamo dato un nome nel ciclo 1, ma la baseline non registra il dettaglio per criterio: non lo diamo per certo.
- **Percorsi**: il resoconto riporta 103/105 al ciclo 3. Rieseguendo oggi su PRIMA otteniamo 104/105, sia con il `percorsi.js` di `$BASE` (2 esecuzioni) sia con quello di `HEAD`. L'unico NO è «Proponi: pulsanti allineati». Il secondo errore del ciclo 3 (posizione) era intermittente.
- **axe PRIMA**: la prima esecuzione ha dato 1 violazione `color-contrast` (serious) su `404.html`, sugli elementi dell'header. Due esecuzioni successive danno 0. La consideriamo un artefatto della transizione di tema (attesa di 350 ms nello script), non un problema del sito. DOPO: 0 in due esecuzioni.
- **Contrasti**: con la versione di `$BASE` di `contrasto.py`, 90 coppie × 2 = 180/180. Con quella di `HEAD`, 91 × 2 = 182: PRIMA 2 sotto soglia, DOPO 0.
- **AccessibilityChecker**: il resoconto dice «solo sulla home». Nel loop abbiamo provato a estenderlo a tutte le 50 pagine, ma il limite giornaliero gratuito ha fermato lo strumento: 3 ok, 1 errore (timeout su progetti), 46 saltate. Non diciamo che l'estensione sia riuscita.
- **ACHECKS**: nel ciclo 1 non era stato usato. Nel loop ha coperto 50/50 pagine (AChecker WCAG 2.0 AA più Lighthouse 13.0.1). L'interfaccia di achecks.org mostra due schede, «Errors» (known problems) e «Warnings» (potential problems); i *likely problems* non compaiono separati. Totali: 122 known (100 per #116 e 22 per #245) e 4.574 potential.
- **Timestamp del lotto 1** (11:00): sono precedenti al commit che crea l'anteprima (11:27), quindi arrotondati.
- **FIXES_REPORT**: dice «verifica nel browser non eseguita (permesso Playwright negato)». Per la relazione (12/11) abbiamo fatto la verifica in Chromium con Playwright: anello visibile in entrambi i temi, marchio invariato, `h2` nell'albero di accessibilità. Restano da fare le prove con lettore di schermo.

## 5. Modifiche nel diff non documentate (o solo in parte)

| Modifica | Commit | Riguarda l'accessibilità? | Dove nella relazione |
|---|---|---|---|
| `.htmlvalidate.json` (recommended meno 6 regole stilistiche) e `.stylelintrc.json` (solo parsing) | `5a6bddc` | Sì, indirettamente: decide che cosa conta come errore | §8 |
| `<h2 id="h-pagine">` con testo di fallback in cerca | `5a6bddc` | Sì (rientra nei «titoli dinamici») | §5.2 |
| Script `validate` e `verify`, dipendenze html-validate e Stylelint in `package.json` | `5a6bddc` | Strumenti | §2, App. B |
| `CHROME_PATH` e `/usr/bin/chromium` negli script Playwright, `prestazioni.js` | `5a6bddc` | No (portabilità) | riga in §9.4 |
| Report rigenerati in `docs/verifiche/` e screenshot | `5a6bddc` | Documentazione | riga in §9.4 |
| Rimozione di `assignment2/alex/` | `5a6bddc` | No (pulizia del repository) | riga in §9.4 |
| `data/ib-dati.js` con data di build 11-03 → 11-05 | `5a6bddc` | No | riga in §9.4 |
| Workflow delle anteprime e base della 404 | `6367c65` | No (infrastruttura) | riga in §9.4 |
| `docs/verifiche/anteprima-design-system.html` (`<b>` → span) | `1541ed1` | Coerenza della documentazione | non citata (documentazione) |
| `assignment2/relazione/04_verifica_V00.md`, prompt della relazione | `f2b73cf` | No | riga in §9.4 |

## 6. Coerenza della build

- In un worktree pulito di `HEAD`, `IB_OGGI=2026-11-05 python3 tools/build.py` genera 50 pagine e `git status` resta vuoto ✓. Senza `IB_OGGI` cambia solo `data/ib-dati.js` (data di riferimento).
- Lo stesso vale per `$BASE` con `IB_OGGI=2026-11-03` ✓.
- Gli HTML generati sono in `.gitignore`: nessuna modifica fatta a mano sugli HTML è registrata nei commit. L'unico HTML tracciato è `docs/verifiche/anteprima-design-system.html`, modificato a mano in `1541ed1`: è documentazione, non è generato da `build.py`.
- Gli HTML nella copia di lavoro principale (`assignment2/website/*.html`) **non** coincidono con la build di `HEAD`: sono una build precedente (hanno ancora `aria-label` sul logo e `<b>`). Non sono tracciati e non influiscono sulla relazione, ma prima di consegnare lo zip va rilanciata la build.
