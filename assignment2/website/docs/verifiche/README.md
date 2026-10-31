# Verifiche tecniche (Fase 4)

Data: 31/10/2026. Ambiente: macOS, Google Chrome 156 (via Playwright 1.56), axe-core 4.10.3, Lighthouse 12.8.2, Python 3.15. Tutti gli script sono in `tools/` e si possono rieseguire (vedi `README.md` del sito).

## Sintesi

| Verifica | Strumento | Risultato | Dettaglio |
|---|---|---|---|
| Accessibilità automatica, 58 pagine IT + EN | `tools/verifica-pagine.js` (axe-core, regole WCAG 2.0/2.1/2.2 A e AA) | **0 violazioni** (critiche, gravi, moderate, minori); 0 errori JS; un solo `h1` per pagina; titoli univoci ≤ 60 caratteri | `axe.md`, `axe.json` |
| Contrasto | `tools/contrasto.py` | **52 coppie su 52** sopra soglia (testo min. 5,96:1; componenti min. 4,14:1) | `contrasti.md` |
| Link e ancore | `tools/verifica-link.py` | **1.950 link interni e 486 ancore, 0 problemi**; nessun link interno in nuova scheda; nessuna risorsa esterna | `link.md` |
| Coerenza dei dati e dei testi | `tools/verifica-dati.py` | **385 controlli su 385** (budget, sostenitori, stati, contatori, ordine delle sezioni, lessico, nota «prototipo», nessun giorno negativo fino al 2030) | `dati.md`, `segnaposto.md` |
| Percorsi interattivi e tastiera | `tools/percorsi.js` | **52 controlli su 52** | `percorsi.md`, `screenshot/tastiera-*.png`, `donazione-*.png` |
| Uso senza server | `tools/verifica-file.js` | **8 su 8** da `file://` (filtri, ricerca, donazione, dati conservati, inglese) | `percorsi.md` (ultima sezione) |
| Responsive, zoom, daltonismo, aree cliccabili | `tools/responsive.js` | nessuno scorrimento orizzontale a 320/375/768/1280 px né con zoom 200%; nessun bersaglio sotto 24 px; pulsanti principali 44 px | `responsive.md`, `screenshot/*-320.jpg` … `*-1280.jpg`, `progetti-deuteranopia.jpg` |
| Prestazioni mobile | `tools/prestazioni.js` (Lighthouse) | **100/100/100/100** su home, elenco, progetto, donazione; LCP 1,6–1,9 s; CLS 0; TBT 0 ms | `prestazioni.md` |

## Problemi trovati dalle verifiche e corretti

Le verifiche non sono state una formalità: hanno trovato difetti reali, corretti prima di chiudere.

| Problema trovato | Strumento | Correzione |
|---|---|---|
| Nelle FAQ 21 link identici «Link a questa risposta» (stesso difetto di P-011 su IdeaGinger) | `verifica-link.py` | Testo nascosto con la domanda: ogni link ha un nome distinto |
| CLS 0,30 su elenco e pagina progetto: il menu mobile veniva nascosto dallo script dopo il primo disegno | Lighthouse | Menu nascosto via CSS fin dall'inizio (classe `js` impostata nell'`<head>`) |
| CLS 0,59 sulla donazione: titolo e modulo costruiti dallo script spostavano il piè di pagina | Lighthouse | Contenuto invisibile ma con spazio riservato finché lo script è pronto, con rete di sicurezza di 2,5 s |
| Pagine FAQ e progetto senza i testi per i messaggi: errori di validazione vuoti (un modulo poteva essere inviato senza controlli) | `percorsi.js` | Testi dell'interfaccia separati in `data/testi-*.js`, caricati in tutte le pagine |
| Ricerca per sottostringa: «api» trovava anche «capire», «rapido» (7 risultati) | screenshot di `percorsi.js` | Ricerca per inizio di parola (2 risultati pertinenti) |
| Pulsante «Menu» visibile anche su desktop | screenshot | Specificità della regola CSS |
| Link isolati alti 18–21 px | `responsive.js` | Area cliccabile di almeno 24 px |
| Link `rel="alternate"` con indirizzo relativo (SEO 91) | Lighthouse | Rimosso; il selettore di lingua ha `hreflang` e `lang` |
| Importi scritti in due forme («6.000 €» e «€ 6.000») | revisione di `segnaposto.md` | Una sola forma in tutto il sito |

## Criteri WCAG 2.2 verificati a mano o con test mirati

axe-core controlla automaticamente solo una parte dei criteri. Per gli altri:

| Criterio | Come è stato verificato | Esito |
|---|---|---|
| 1.1.1 Contenuti non testuali | Revisione: illustrazioni con `alt` descrittivo nella pagina progetto e `alt=""` nelle card; icone SVG `aria-hidden` con testo accanto | conforme |
| 1.3.1 Informazioni e correlazioni | Revisione del markup generato: `fieldset`/`legend`, `label for`, tabelle con `caption` e `th`, liste, landmark | conforme |
| 1.3.2 Sequenza significativa | A 375 px l'ordine del DOM è quello visivo (titolo → stato → contenuto); screenshot `*-375.jpg` | conforme |
| 1.3.5 Scopo degli input | `autocomplete` su nome, cognome, email, telefono, organizzazione (`percorsi.js` controlla l'email) | conforme |
| 1.4.1 Uso del colore | Simulazione deuteranopia e acromatopsia (`progetti-deuteranopia.jpg`); ogni stato ha testo e icona | conforme |
| 1.4.3, 1.4.11 Contrasto | `contrasto.py` su tutti i token | conforme |
| 1.4.4 Ridimensionamento del testo | Zoom 200% simulato (640 px CSS, densità 2): nessuna perdita | conforme |
| 1.4.10 Reflow | 320 px su 8 pagine | conforme |
| 1.4.12 Spaziatura del testo | Unità relative, nessuna altezza fissa sui contenitori di testo (revisione del CSS) | conforme (non testato con il bookmarklet) |
| 1.4.13 Contenuto su hover o focus | Spiegazioni a comparsa solo al clic, chiudibili con Esc (`percorsi.js`) | conforme |
| 2.1.1, 2.1.2 Tastiera, nessuna trappola | Percorso completo solo da tastiera (`percorsi.js`) | conforme |
| 2.4.1 Salta blocchi | Primo Tab = «Salta al contenuto» | conforme |
| 2.4.3 Ordine del focus | Percorso da tastiera; a menu chiuso le voci non ricevono il focus | conforme |
| 2.4.4 Scopo del link | `verifica-link.py`: nessun testo uguale verso destinazioni diverse | conforme |
| 2.4.6 Intestazioni ed etichette | Revisione; un `h1` per pagina (script) | conforme |
| 2.4.7, 2.4.11 Focus visibile e non coperto | Screenshot `tastiera-*.png`; nessun elemento fisso nell'interfaccia | conforme |
| 2.5.3 Etichetta nel nome | I nomi accessibili iniziano con il testo visibile («Scegli € 50: …») | conforme |
| 2.5.8 Dimensione dei bersagli | `responsive.js` a 375 px | conforme |
| 3.1.1, 3.1.2 Lingua | `lang` sulla pagina e sui commenti in altra lingua; selettore con `lang` | conforme |
| 3.2.3, 3.2.4, 3.2.6 Navigazione, identificazione e aiuto coerenti | Intestazione, menu e blocco «Aiuto» generati da un'unica funzione | conforme |
| 3.3.1, 3.3.3 Identificazione e suggerimenti per gli errori | Messaggi vicino al campo, con la correzione da fare (`percorsi.js`) | conforme |
| 3.3.2 Etichette o istruzioni | Etichette sempre visibili; «facoltativo» esplicito | conforme |
| 3.3.7 Inserimento ridondante | Dati conservati tornando indietro e ricaricando (`percorsi.js`) | conforme |
| 4.1.2 Nome, ruolo, valore | `aria-expanded`, `aria-invalid`, `aria-current` verificati da `percorsi.js` | conforme per i casi testati |
| 4.1.3 Messaggi di stato | Conteggi, conferme e «Link copiato» in `role="status"` | conforme |

## Verifiche non eseguite

- **Screen reader reali** (NVDA, VoiceOver): non disponibili nell'ambiente. Nomi, ruoli e stati sono stati controllati con Playwright e axe; resta da fare un test con P03 come guida.
- **Firefox e Safari**: i browser in cache di Playwright non corrispondono alla versione installata; le verifiche automatiche sono state fatte solo con Chrome. Il codice usa solo API standard (`sessionStorage`, `URLSearchParams`, `history.pushState`, `details`), ma un controllo manuale con Safari su iPhone (P03, P07) resta consigliato.
- **INP** reale: Lighthouse in laboratorio non lo misura; il TBT è 0 ms.
- **Pubblicazione su GitHub Pages**: simulata con un server statico in una sottocartella; la 404 a qualunque profondità usa una logica attiva solo su `*.github.io`, quindi va provata dopo la pubblicazione.
