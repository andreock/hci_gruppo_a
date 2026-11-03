# Percorsi interattivi

Generato da `tools/percorsi.js` il 03/11/2026, 10:28:29 (Playwright + Google Chrome, server statico locale con il sito in una sottocartella).

**66 controlli superati su 66.**

| # | Controllo | Esito | Nota |
|---|---|---|---|
| 1 | Il primo Tab porta a «Salta al contenuto» | superato |  |
| 2 | Il campo di ricerca nell'intestazione è raggiungibile da tastiera | superato |  |
| 3 | La ricerca «api» trova i progetti sulle api (per inizio di parola, non «capire») | superato | 2 progetti per «api» |
| 4 | Il risultato «Alveari sani» si raggiunge con Tab (link con nome significativo) | superato | Alveari sani: monitorare la salute delle api del Piemonte |
| 5 | «Sostieni il progetto» si raggiunge da tastiera | superato |  |
| 6 | La spiegazione «tutto o niente» si apre con Invio | superato |  |
| 7 | La spiegazione si chiude con Esc | superato |  |
| 8 | La donazione si apre con il progetto nella URL | superato |  |
| 9 | Indicatore dei passi: passo 1 di 5 | superato |  |
| 10 | Importo sotto il minimo: errore in linea quando si lascia il campo | superato | L'importo minimo è € 5: scrivi 5 o più. |
| 11 | Il campo con errore ha aria-invalid e aria-describedby | superato |  |
| 12 | L'errore sparisce appena l'importo è corretto | superato |  |
| 13 | Invio porta al passo 2 e il focus va al titolo del passo | superato |  |
| 14 | Il riepilogo mostra 20 € | superato |  |
| 15 | Con un errore compare il riepilogo in testa e riceve il focus | superato |  |
| 16 | Il riepilogo contiene il link al campo Email | superato |  |
| 17 | Il campo email usa type=email e autocomplete=email | superato |  |
| 18 | Nessuna scelta di visibilità preselezionata | superato |  |
| 19 | Con Indietro del browser si torna al passo 2 e i dati sono ancora lì | superato |  |
| 20 | Anche dopo aver ricaricato la pagina i dati restano | superato |  |
| 21 | La commissione è mostrata accanto al metodo | superato |  |
| 22 | Il riepilogo finale mostra commissione e totale prima della conferma | superato | ProgettoAlveari sani: monitorare la salute delle api del PiemonteRicompensaDonazione liberaDonazione€ 20Commissione del pagamento€ 0,71Totale€ 20,71Metodo di pa |
| 23 | Nessun campo per numeri di carta | superato |  |
| 24 | La conferma mostra il codice di riferimento | superato |  |
| 25 | Il filtro aggiorna la URL | superato |  |
| 26 | Il conteggio dice quanti progetti sono mostrati | superato | Mostrati 7 di 13 progetti |
| 27 | Tornando indietro i filtri restano | superato |  |
| 28 | Tornando indietro la posizione nella pagina resta | superato | 900 → 900 |
| 29 | Una URL filtrata condivisa mostra solo le campagne in corso con obiettivo raggiunto | superato |  |
| 30 | Con filtri senza risultati compare un messaggio con alternative | superato |  |
| 31 | Ricerca senza risultati: messaggio e suggerimenti | superato |  |
| 32 | La ricerca tollera singolare e plurale («veterinaria» trova Scienze Veterinarie) | superato |  |
| 33 | La ricerca trova anche la pagina del programma | superato |  |
| 34 | A menu chiuso le voci non sono raggiungibili | superato |  |
| 35 | Invio apre il menu e aria-expanded diventa true | superato |  |
| 36 | Esc chiude il menu e il focus torna al pulsante | superato |  |
| 37 | Il pulsante del menu misura almeno 44×44 px | superato | 48×44 |
| 38 | Aprendo faq.html#faq-tutto-o-niente la risposta è aperta | superato |  |
| 39 | La ricerca nelle FAQ filtra e annuncia il numero | superato |  |
| 40 | In inglese l'errore sull'importo è in inglese | superato |  |
| 41 | Il selettore di lingua porta alla stessa pagina in inglese con gli stessi filtri | superato |  |
| 42 | La pagina inglese ha lang=en | superato |  |
| 43 | Campagna conclusa: nessun link per donare né campo importo | superato |  |
| 44 | Campagna conclusa: stato scritto in testo | superato |  |
| 45 | Donazione su campagna conclusa aperta da URL: spiegazione invece del modulo | superato |  |
| 46 | Donazione senza progetto: spiegazione e link, nessun reindirizzamento | superato |  |
| 47 | «Scrivi al gruppo» mostra subito un indicatore di invio | superato |  |
| 48 | …poi una conferma con i tempi di risposta | superato |  |
| 49 | Candidatura vuota: riepilogo errori | superato |  |
| 50 | I consensi sono caselle di spunta native | superato |  |
| 51 | Spuntando il consenso l'errore sparisce | superato |  |
| 52 | Senza una scelta salvata il tema è chiaro, anche con il sistema in scuro | superato | rgb(251, 246, 238) |
| 53 | L'interruttore dice verso quale tema si passa | superato | Passa a:
Tema scuro |
| 54 | Da tastiera si passa al tema scuro | superato | rgb(28, 20, 18) |
| 55 | Il pulsante propone ora il tema chiaro | superato | Passa a:
Tema chiaro |
| 56 | Il colore della barra del browser segue il tema | superato |  |
| 57 | La scelta resta valida cambiando pagina | superato |  |
| 58 | La scelta resta valida cambiando lingua | superato |  |
| 59 | Il tema scuro scelto resta valido dopo aver ricaricato la pagina | superato |  |
| 60 | Si può tornare al tema chiaro e la scelta resta | superato | rgb(251, 246, 238) |
| 61 | Senza JavaScript il tema è chiaro e l'interruttore è nascosto | superato | rgb(251, 246, 238) |
| 62 | A 320 px marchio, lingua, tema e menu stanno su una riga | superato | [12,12,12,12] |
| 63 | A 320 px l'interruttore del tema è largo e alto almeno 44 px | superato | 44×44 |
| 64 | A 375 px marchio, lingua, tema e menu stanno su una riga | superato | [12,12,12,12] |
| 65 | A 375 px l'interruttore del tema è largo e alto almeno 44 px | superato | 44×44 |
| 66 | Nessun errore JavaScript durante i percorsi | superato |  |

Screenshot del percorso da tastiera e della donazione: `docs/verifiche/screenshot/tastiera-*.png`, `donazione-*.png`, `menu-mobile-375.png`.

## Senza server (file://)

Generato da `tools/verifica-file.js`: le stesse funzioni aprendo i file direttamente dal disco, come nello zip della consegna.

| Controllo | Esito |
|---|---|
| file:// · i filtri si applicano dalla URL | superato |
| file:// · la ricerca funziona | superato |
| file:// · la donazione si apre con il progetto | superato |
| file:// · si passa al passo 2 (history.pushState) | superato |
| file:// · i dati restano tornando avanti e indietro (sessionStorage) | superato |
| file:// · versione inglese e FAQ aperta da ancora | superato |
| file:// · le date relative sono ricalcolate | superato |
| file:// · nessun errore JavaScript | superato |
