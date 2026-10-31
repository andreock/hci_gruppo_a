# 08 · Verifica con personas e journey

Ogni punto di dolore dei 12 journey (`03_bisogni_personas.md`, codici `Jxx-Fn`) è stato ripercorso sul nuovo sito con il dispositivo e le esigenze della persona. Le prove rimandano a:
- `percorsi.md #n`: controllo numero *n* di `docs/verifiche/percorsi.md`, eseguito automaticamente;
- `screenshot/…`: file in `docs/verifiche/screenshot/`;
- `axe.md`, `link.md`, `dati.md`, `responsive.md`, `prestazioni.md`, `contrasti.md`: altri report in `docs/verifiche/`;
- file e funzione del codice dove serve.

**Stati**: **risolto** (con prova), **parziale** (risolto in parte, motivo indicato), **non risolto** (motivo indicato).

Limite di metodo: è un **cognitive walkthrough** del gruppo con strumenti automatici, non un test con utenti reali. Le personas sono proto-personas: le conclusioni vanno confermate con test di usabilità (vedi `09_valutazione_euristica.md` §4).

## Condizioni simulate per persona

| Persona | Condizioni usate nella verifica |
|---|---|
| P01 Giuseppe | Zoom al 200% (`screenshot/progetto-zoom200.jpg`, `donazione-zoom200.jpg`), aree cliccabili a 375 px (`responsive.md`), testo in italiano |
| P02 Sara | Viewport 375 px, Lighthouse mobile con 4G lento simulato (`prestazioni.md`), interruzione e ripresa del modulo (`percorsi.md #19–20`) |
| P03 Davide | Solo tastiera, nomi e stati accessibili (`percorsi.md #1–24`, `axe.md`) |
| P04 Tomás | Interfaccia in inglese (`en/`), errori in inglese (`percorsi.md #40`) |
| P05 Luca | 1280 px, simulazione di deuteranopia (`screenshot/progetti-deuteranopia.jpg`) |
| P06 Elena | 1280 px, lettura di Chi siamo, Programma, FAQ, riepilogo della donazione |
| P07 Giulia | 375 px (iPhone), testi brevi, indice, importo minimo |
| P08 Roberta | 1280 px, filtri per anno, URL condivisibili, numeri del programma (`dati.md`) |
| P09 Chiara | Laptop, «Come funziona», FAQ per promotori, modulo di candidatura |
| P10 Franco | 1280 px con zoom 125–200%, pagina di una campagna oltre il 100% (`progetto-alveari-sani.html`) |
| P11 Amir | Tastiera, inglese, smartphone (`percorsi.md #34–42`, `prestazioni.md`) |
| P12 Maria | 375 px e PC, aree cliccabili, modulo «Proponi una collaborazione» |

---

## P01 · Giuseppe Ferrero (tablet, presbiopia, prima donazione)

| Codice | Punto di dolore | Che cosa succede ora su ideaBlume | Stato | Prova |
|---|---|---|---|---|
| J01-F1 | Titolo troncato nei risultati, nome del servizio incoerente | Titoli brevi e univoci «Pagina – ideaBlume», massimo 60 caratteri; un solo nome del marchio | risolto | `axe.md` (titoli ≤ 60, nessun duplicato) |
| J01-F2 | Home che non spiega il servizio; testo piccolo e poco contrastato | La prima frase dice che cos'è ideaBlume e chi lo gestisce; corpo 18 px; contrasto minimo del testo 5,96:1 | risolto | `screenshot/home-1280.jpg`, `home-375.jpg`; `contrasti.md` |
| J01-F3 | «Come funziona» continuo, piccolo, con termini inglesi | Indice, passi numerati con link all'azione, glossario in italiano, telefono nel piè di pagina di ogni pagina | risolto | `come-funziona.html`; `dati.md` (nessun termine escluso) |
| J01-F4 | Oltre 100%, giorni negativi, nuove schede | Badge «Obiettivo raggiunto · puoi ancora sostenerlo per 20 giorni (scade il …)»; giorni mai negativi; tutti i link interni nella stessa scheda | risolto | `dati.md` (stati fino al 2030), `link.md` (0 `target=_blank`) |
| J01-F5 | Errore solo dopo l'invio; ricompensa «obbligata» | Errore all'uscita dal campo con la correzione da fare; «Donazione libera · da € 5» è la prima scelta | risolto | `percorsi.md #10–12`; `screenshot/donazione-errore-importo.png` |
| J01-F6 | Senza riferimento umano dubita dell'esito | Conferma con codice di riferimento, riepilogo stampabile, che cosa succede dopo, telefono e orari | parziale | `percorsi.md #24`; `screenshot/donazione-conferma.png`. L'email di conferma è solo annunciata: il prototipo non invia email |

Zoom al 200%: nessuno scorrimento orizzontale, testi e pulsanti interi (`responsive.md`). Pulsanti principali alti 44 px.

## P02 · Sara Colombo (smartphone, pause brevi, una mano)

| Codice | Punto di dolore | Che cosa succede ora | Stato | Prova |
|---|---|---|---|---|
| J02-F2 | Contenuto principale dopo diversi secondi sul 4G | Pagina progetto: LCP 1,7 s, 97 KB, nessun font o script esterno (IdeaGinger: 34,1 s) | risolto | `prestazioni.md` |
| J02-F3 | Pagina lunga; contatto senza indicatore | Riquadro di stato e «Sostieni» subito sotto il titolo; indice a 7 voci; «Scrivi al gruppo» con indicatore e conferma | risolto | `screenshot/progetto-375.jpg`; `percorsi.md #47–48` |
| J02-F4 | Ricompense lunghe, importo libero non riconoscibile | Lista compatta, prima voce «Donazione libera · da € 5» | risolto | `progetto-neonati-virus.html#ricompense` |
| J02-F5 | Modulo lento, errore tardivo, dati persi | Validazione in linea; dati salvati a ogni tasto, anche ricaricando o tornando indietro | risolto | `percorsi.md #10, #19, #20` |
| J02-F6 | Giorni negativi; carosello senza indicatori; reinserire i dati sul laptop | Scadenza con data; nessun carosello. Sul laptop i dati **non** ci sono: restano solo nella scheda in cui sono stati scritti | parziale | `dati.md`; D-17 (nessun account). Riprendere da un altro dispositivo richiederebbe un account o un link con i dati, esclusi dal prototipo |

## P03 · Davide Rinaldi (NVDA, solo tastiera)

| Codice | Punto di dolore | Che cosa succede ora | Stato | Prova |
|---|---|---|---|---|
| J03-F2 | Immagini senza descrizione, titoli vuoti, tooltip come link | Illustrazione con alt descrittivo; titoli in ordine; «Che cosa significa “tutto o niente”?» è un pulsante con `aria-expanded`, Esc chiude | risolto | `axe.md` (0 violazioni); `percorsi.md #6–7` |
| J03-F3 | Stato solo a colore; controlli attivi su campagna conclusa | «Conclusa · obiettivo raggiunto» in testo; nessun campo importo né link per donare; spiegazione anche se si apre la donazione dalla URL | risolto | `percorsi.md #43–45` |
| J03-F4 | Menu senza Esc; link uguali; card senza nome; posizione persa | Menu con Esc e focus restituito; ogni card ha un solo link con il titolo; nessun link generico ripetuto; filtri e posizione conservati | risolto | `percorsi.md #4, #27–28, #34–36`; `link.md` |
| J03-F5 | Errore dopo l'invio, senza focus | Riepilogo degli errori in testa con link ai campi, riceve il focus; messaggi collegati con `aria-describedby` | risolto | `percorsi.md #11, #15–16`; `screenshot/donazione-riepilogo-errori.png` |
| J03-F6 | Accessibilità complessiva mediocre | Lighthouse accessibilità 100 (IdeaGinger 64–77); dichiarazione di accessibilità con canale di segnalazione | risolto per i test automatici | `prestazioni.md`; `accessibilita.html`. **Da confermare con NVDA reale** (`verifiche/README.md`) |

## P04 · Tomás García (italiano A2, inglese C1)

| Codice | Punto di dolore | Che cosa succede ora | Stato | Prova |
|---|---|---|---|---|
| J04-F2 | Solo la descrizione tradotta; gergo non spiegato | 29 pagine inglesi complete (menu, stato, ricompense, regole, errori, FAQ); glossario in inglese | risolto | `screenshot/home-en-1280.jpg`; `tools/build.py` si ferma se manca una traduzione |
| J04-F3 | «Tutto o niente» assente in inglese; guida su altro sito senza avviso | Regola spiegata nel riquadro accanto a «Support this project»; nessun link esterno non dichiarato | risolto | `en/progetto-clima-giovani.html`; `link.md` |
| J04-F4 | Ricompense in due lingue, disposte in modo diverso | Una lingua per volta; stessa struttura delle ricompense in tutti i progetti | risolto | `dati.md` (ordine delle sezioni), `en/progetto-*.html` |
| J04-F5 | Errore solo in italiano; metodi incoerenti; commissioni nascoste | Errori in inglese; metodi da un'unica fonte uguali in FAQ e donazione; commissione e totale nel riepilogo | risolto | `percorsi.md #21–22, #40`; `dati.md` (metodi) |
| J04-F6 | Il link condiviso apre la versione italiana | Le pagine inglesi hanno un indirizzo proprio (`en/…`): il link copiato resta in inglese; il selettore conserva filtri e ancora | risolto | `percorsi.md #41` |

## P05 · Luca Moretti (deuteranopia, confronto metodico)

| Codice | Punto di dolore | Che cosa succede ora | Stato | Prova |
|---|---|---|---|---|
| J05-F1 | Barre solo a colore; contrasto basso; contatore unico | Stato in testo con icona diversa; barra non interattiva con le cifre scritte; contatori «6 in corso · 7 conclusi» | risolto | `screenshot/progetti-deuteranopia.jpg`, `progetti-achromatopsia.jpg` |
| J05-F2 | Card senza tema; niente filtri; «Altri» opaco; posizione persa | Tema e anno su ogni card; filtri per stato, tema, dipartimento, anno e programma; «Più lontani dall'obiettivo»; «Mostrati N di 13»; posizione conservata | risolto | `percorsi.md #25–30` |
| J05-F3 | Oltre 100% senza etichetta; giorni negativi; concluse attive; «nuovo obiettivo» ambiguo | Badge testuali; secondo obiettivo con cifra e scopo nel riquadro «Obiettivo e raddoppio» | risolto | `progetto-alveari-sani.html` |
| J05-F4 | Raddoppio non visibile dove si dona | Riquadro accanto a «Sostieni» con esempio numerico; frase anche nel passo 1 della donazione | risolto | `screenshot/progetto-1280.jpg` |
| J05-F6 | Posizione persa; giorni negativi al ritorno | Filtri nella URL (si può salvare tra i preferiti) e posizione conservata | risolto | `percorsi.md #27–29` |

## P06 · Elena Conti (fiducia e privacy)

| Codice | Punto di dolore | Che cosa succede ora | Stato | Prova |
|---|---|---|---|---|
| J06-F1 | «Chi siamo» solo in fondo | Nella prima frase della home e nel menu principale | risolto | `screenshot/home-1280.jpg` |
| J06-F2 | Programma senza date; numeri incoerenti; promotori informali; nessun contatto | Stato attuale con data di fine delle campagne; tabella delle edizioni calcolata dai dati; «Gruppo · Dipartimento, Università di Torino» e responsabile; contatto dell'Ufficio. Le date del prossimo bando sono segnaposto | parziale | `programma.html`; `dati.md`. Le date reali del bando non sono nelle fonti (D-16) |
| J06-F3 | FAQ miste; due nomi per la stessa modalità; «commissioni» porta alle condizioni d'uso; rimborso nascosto | FAQ divise e con ricerca; lessico unico; riquadro «Quanto costa»; rimborso spiegato nel riepilogo della donazione | risolto | `percorsi.md #38–39`; `dati.md` (termini esclusi) |
| J06-F5 | «Tutto o niente» non nel modulo; anonimato non preselezionato; dati al promotore | Regola nel passo 1 e nel riepilogo; due scelte obbligatorie senza preselezione; spiegazione di che cosa riceve il gruppo (segnaposto) | risolto (informazione da confermare) | `percorsi.md #18` |
| J06-F6 | Ricevuta e detraibilità non spiegate | Riquadro «Ricevuta e detraibilità» nel modulo e nella conferma, con segnaposto | parziale | Le fonti non dicono se la donazione è detraibile (D-14) |

## P07 · Giulia Esposito (iPhone, DSA)

| Codice | Punto di dolore | Che cosa succede ora | Stato | Prova |
|---|---|---|---|---|
| J07-F2 | Scopo assente; servizi prima dei progetti; titoli troncati; stato ambiguo | Frase iniziale; progetti in corso subito dopo; titoli interi; stato testuale | risolto | `screenshot/home-375.jpg` |
| J07-F3 | Nessuna ricerca; carosello senza indicatori; inglese non spiegato | Ricerca nell'intestazione, anche su mobile; griglia senza caroselli; glossario | risolto | `percorsi.md #2–3` |
| J07-F4 | Pagina senza indice; testo continuo | Indice «In questa pagina», paragrafi brevi, «Torna su» | risolto | `screenshot/progetto-375.jpg` |
| J07-F5 | Errore sul minimo solo dopo l'invio | Minimo scritto accanto al campo; errore all'uscita dal campo | risolto | `percorsi.md #10` |

## P08 · Roberta Galli (giornalista, ricerca esaustiva)

| Codice | Punto di dolore | Che cosa succede ora | Stato | Prova |
|---|---|---|---|---|
| J08-F1 | Stato temporale assente; numeri discordanti; cambio di sito | Stato attuale con date; numeri calcolati da un'unica fonte con data di aggiornamento; nessun link esterno non dichiarato | risolto | `dati.md`; `link.md` |
| J08-F2 | Caricamento opaco; fine non dichiarata; stato perso; niente filtri né «Torna su» | Filtro per anno e stato conclusi; conteggio; messaggio di fine; posizione conservata; «Torna su» | risolto | `percorsi.md #25–30` |
| J08-F3 | Aggiornamenti prima del contesto; gruppo non attribuito | Ordine fisso: presentazione → fondi → team → ricompense → aggiornamenti | risolto | `dati.md` (ordine delle sezioni) |
| J08-F4 | Nessun feedback; nessun contatto UniTo | Email del gruppo visibile; modulo con indicatore e conferma; contatti dell'Ufficio | risolto | `percorsi.md #47–48` |
| J08-F5 | Dati discordanti; blog senza date | Tabella delle edizioni con data di aggiornamento; aggiornamenti dei progetti datati in home | risolto | `programma.html#edizioni` |
| J08-F6 | I lettori arriveranno su una pagina senza date | Pagina del programma con stato e date; URL stabili e filtrabili da citare | risolto | `percorsi.md #29` |

## P09 · Chiara Marino (ricercatrice che si candida)

| Codice | Punto di dolore | Che cosa succede ora | Stato | Prova |
|---|---|---|---|---|
| J09-F1 | Nessuna data di candidatura | La pagina dice in che fase è l'edizione; le date del bando 2027 sono segnaposto evidenti | parziale | Le date non sono nelle fonti (D-16) |
| J09-F2 | Requisiti e contatto assenti; percorso ambiguo | «Chi può candidarsi», «Requisiti», «Come e quando», «A chi scrivere»; pulsante «Candidati al programma» distinto dalla collaborazione | risolto | `programma.html#requisiti`; `proponi.html` |
| J09-F3 | Testo continuo, piccolo, gergo, quota nascosta | Indice e passi; corpo 18 px; FAQ «Per chi propone»; glossario; «Quanto costa» come primo riquadro di «Proponi» (cifra da confermare) | risolto (cifra da confermare) | `proponi.html`, `come-funziona.html#costi` |
| J09-F4 | Passo citato senza link; registrazione generica | Ogni passo di «Come funziona» ha il suo link; nessuna registrazione generica | risolto | `link.md` |
| J09-F5 | Etichette che spariscono; niente controlli del browser; errore che resta | Etichette sopra i campi, `type`/`autocomplete`, caselle native, errori che spariscono, contatore dei caratteri, bozza salvata tra le sessioni della scheda | risolto | `percorsi.md #49–51`; `axe.md` |

## P10 · Franco Gallo (responsabile di una campagna al 130%)

| Codice | Punto di dolore | Che cosa succede ora | Stato | Prova |
|---|---|---|---|---|
| J10-F1 | Titolo tagliato; tema e dipartimento assenti; cifre piccole | Titolo intero, tema, «Gruppo ApiLab · Dipartimento di Scienze Veterinarie, Università di Torino»; raccolto a 32 px | risolto | `screenshot/progetto-1280.jpg` (per alveari: `progetto-alveari-sani.html`) |
| J10-F2 | Oltre 100% letto come chiuso; nuovo obiettivo senza scopo | «Obiettivo raggiunto · puoi ancora sostenerlo per 20 giorni»; secondo obiettivo € 9.000 «per aggiungere due apiari» | risolto | `progetto-alveari-sani.html` |
| J10-F3 | Cofinanziamento non vicino a «Sostieni» | Riquadro accanto al pulsante; regola oltre l'obiettivo spiegata (da confermare) | risolto (regola da confermare) | D-10 |
| J10-F4 | Il donatore non sa se il messaggio è partito | «Scrivi al gruppo» con indicatore e tempi di risposta | risolto | `percorsi.md #47–48` |
| J10-F5 | Controlli attivi a campagna chiusa | Nessun controllo; «Raccolta conclusa il …», «Leggi il resoconto», «Scopri i progetti in corso» | risolto | `percorsi.md #43–44` |
| J10-F6 | Senza resoconto i donatori non sanno com'è finita | I progetti conclusi hanno un resoconto con le spese negli aggiornamenti. La pubblicazione passa dall'Ufficio (nessuna area riservata) e l'avviso ai sostenitori non è simulato | parziale | `progetto-matematica-accessibile.html#aggiornamenti`; D-17 |

## P11 · Amir Haddad (comunicazione, tastiera, pubblico estero)

| Codice | Punto di dolore | Che cosa succede ora | Stato | Prova |
|---|---|---|---|---|
| J11-F1 | Nessuna indicazione per scrivere in due lingue | «Per i gruppi con una campagna in corso»: campi separati IT/EN, lunghezze consigliate | risolto | `come-funziona.html#gruppi` |
| J11-F2 | Parti non tradotte; lingue mescolate | Inglese completo; commenti marcati con `lang` e con «Comment in Italian» | risolto | `percorsi.md #40–42`; D-28 |
| J11-F3 | Pagina lenta da smartphone; caroselli | Lighthouse mobile 100; nessun carosello | risolto | `prestazioni.md` |
| J11-F4 | Errori in italiano dopo l'invio; regola non ricordata | Errori in linea nella lingua; regola nel passo 1 | risolto | `percorsi.md #40` |
| J11-F5 | Menu senza Esc; focus poco visibile; elementi che sembrano link; pulsanti senza riscontro | Esc, focus a 3 px (17:1), pulsanti veri per le spiegazioni, barra non cliccabile, indicatore «Invio in corso…» | risolto | `percorsi.md #6–7, #34–36, #47`; `screenshot/tastiera-*.png` |
| J11-F6 | Nessun canale per le segnalazioni | Modulo contatti con argomento «Problema del sito» e tempi di risposta | risolto (invio simulato) | `contatti.html#scrivici` |

## P12 · Maria Lombardi (associazione esterna, tremore)

| Codice | Punto di dolore | Che cosa succede ora | Stato | Prova |
|---|---|---|---|---|
| J12-F1 | La home non dice che cos'è il sito né chi lo gestisce | Frase d'apertura e «Chi siamo» | risolto | `screenshot/home-375.jpg` |
| J12-F2 | «Chi siamo» nascosto; nessun esempio con il territorio; menu fitto | «Chi siamo» nel menu; voci del menu mobile alte 48 px; progetto d'esempio con le associazioni di quartiere | risolto | `screenshot/menu-mobile-375.png`; `proponi.html#esempi` |
| J12-F3 | Requisiti per enti esterni assenti; costi tardi; gergo; FAQ uniche | «Sei un ente esterno?» con «Proponi una collaborazione»; «Quanto costa» per primo (gratuito per gli enti); FAQ «Siamo un'associazione…» | risolto | `proponi.html`; `faq.html#faq-enti` |
| J12-F4 | Etichette che spariscono, caselle piccole, errori che restano | Etichette visibili, campi alti 44 px, caselle in riquadri cliccabili, errori in linea; «Inviare non impegna l'ente» in evidenza | risolto | `collabora.html`; `responsive.md` |
| J12-F5 | Tempi di risposta non indicati | La conferma dice «entro 10 giorni lavorativi» e il recapito (tempi da confermare) | risolto (tempi da confermare) | `collabora.html` dopo l'invio |
| J12-F6 | Nessuna garanzia per il direttivo | Riepilogo della proposta stampabile | risolto | pulsante «Stampa» nella conferma |

---

## Sintesi

| Stato | Punti di dolore |
|---|---|
| Risolto | 52 |
| Risolto, con un'informazione da confermare o un limite dichiarato | 6 (J03-F6 da confermare con screen reader reale; J06-F5, J09-F3, J10-F3, J12-F5 con segnaposto; J11-F6 invio simulato) |
| Parziale | 6 (J01-F6, J02-F6, J06-F2, J06-F6, J09-F1, J10-F6) |
| Non risolto | 0 |
| **Totale** | **64** (tutti i punti di dolore di `03_bisogni_personas.md`) |

I casi parziali hanno due cause, entrambe dichiarate: informazioni che le fonti non contengono (date del bando, detraibilità) e funzioni escluse dal prototipo (account, invio di email, ripresa su un altro dispositivo).
