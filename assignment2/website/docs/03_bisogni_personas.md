# 03 · Bisogni delle personas e punti di dolore dei journey

Fonti: schede persona in `assignment2/personas/personas/` e journey in `assignment2/personas/journey/` (versione di riferimento stabilita in `01_inventario_fonti.md` §5); chiavi dei problemi assegnate a ogni fase nei prompt `assignment2/personas/Pxx_*.md` (blocco `<fasi>`).

Le personas sono **proto-personas** costruite dal gruppo a partire dalla valutazione euristica, senza ricerca diretta con utenti (lo dichiarano tutte le schede). I bisogni qui sotto sono quindi ipotesi di progetto, da validare.

## 1. Corrispondenza chiavi C00 → problemi consolidati

| Chiave | P-xxx | Chiave | P-xxx | Chiave | P-xxx | Chiave | P-xxx |
|---|---|---|---|---|---|---|---|
| S09 | P-021 | S22 | P-032 | S37 | P-048 | S59 | P-001 |
| S10 | P-022 | S23 | P-034 | S38 | P-049 | S60 | P-002 |
| S11 | P-024 | S24 | P-033 | S39 | P-050 | S61 | P-003 |
| S12 | P-025 | S25 | P-035 | S40 | P-051 | S62 | P-004 |
| S13 | P-026 | S28 | P-039 | S41 | P-054 | S63 | P-005 |
| S14 | P-014 | S29 | P-040 | S42 | P-055 | S64 | P-038 |
| S15 | P-027 | S30 | P-041 | S45 | P-067 | S65 | P-011 |
| S16 | P-028 | S31 | P-042 | S46 | P-068 | S66 | P-013 |
| S17 | P-029 | S32 | P-043 | S47 | P-069 | S67 | P-008 |
| S18 | P-030 | S33 | P-044 | S48 | P-070 | S68 | P-012 |
| S19 | P-010 | S34 | P-045 | S49 | P-071 | S71 | P-037 |
| S20 | P-015 | S35 | P-046 | S50 | P-072 | S74 | P-087 |
| S21 | P-031 | S36 | P-047 | S51 | P-073 | X01–X08 | P-062, P-063, P-056, P-064, P-065, P-036, P-078, P-053 |
|  |  |  |  | S52–S55 | P-074, P-075, P-076, P-077 |  |  |

## 2. Quadro delle personas

| ID | Persona | Ruolo | Dispositivo | Fam. digitale | Esigenze di accessibilità o contesto | Motto (sintesi del gruppo) |
|---|---|---|---|---|---|---|
| P01 | Giuseppe Ferrero, 71, Moncalieri | Donatore alla prima esperienza | Tablet Android 10" con carattere ingrandito, nessun PC | 2/5 | Presbiopia, tocchi imprecisi | «Aiuto volentieri, ma prima voglio capire dove vanno i soldi.» |
| P02 | Sara Colombo, 34, Torino | Donatrice occasionale | Smartphone Android di 4 anni, 4G debole; laptop la sera | 3/5 | Situazionale: pause di 2–5 minuti, una mano, stanchezza, attenzione divisa | «Se mi fido, voglio poter donare prima che finisca la pausa.» |
| P03 | Davide Rinaldi, 39, Torino | Donatore | PC Windows + Firefox + NVDA; iPhone + VoiceOver | 5/5 con tecnologie assistive | Cieco dalla nascita: solo tastiera e sintesi vocale | «L'accessibilità mi permette di scegliere, non soltanto di entrare.» |
| P04 | Tomás García, 31, Madrid | Donatore dall'estero | Laptop aziendale (browser in inglese), smartphone Android | 5/5 | Linguistica: italiano A2, inglese C1, spagnolo L1 | «Dono volentieri, ma prima voglio capire cosa sto pagando.» |
| P05 | Luca Moretti, 52, Asti | Donatore abituale e metodico | PC desktop 24" in ufficio; smartphone per controlli | 3/5 | Daltonismo (deuteranopia) | «Prima di dare un euro, voglio capire chi ne ha davvero bisogno.» |
| P06 | Elena Conti, 58, Torino | Donatrice attenta a fiducia e privacy | PC desktop con due monitor | 4/5 | Nessuna specifica; occhiali progressivi, ingrandisce la pagina | «Prima di donare leggo tutto: se qualcosa non torna, non dono.» |
| P07 | Giulia Esposito, 20, studentessa UniTo | Donatrice, piccolo importo | iPhone, Safari | 4/5 social, 2/5 testi lunghi e moduli | Dislessia (DSA): usa la lettura vocale di iOS | «Se capisco subito a cosa serve, anche cinque euro e un link contano.» |
| P08 | Roberta Galli, 47, Torino | Visitatrice: giornalista scientifica | Laptop, molte schede | 5/5 | Attenzione divisa, interruzioni, ricerca esaustiva | «Se non posso ricostruire la fonte, non posso pubblicare il numero.» |
| P09 | Chiara Marino, 32, Torino | Promotrice: assegnista UniTo che si candida | Laptop macOS + Safari; iPhone per email | 4/5 | Tempo frammentato, lettura in più sessioni | «Per candidarmi mi servono requisiti, scadenza e un referente, non solo una registrazione.» |
| P10 | Franco Gallo, 63, Torino | Promotore: responsabile di una campagna in corso | PC fisso con monitor 27" | 2/5 | Presbiopia lieve (zoom 125%), pochi minuti per volta | «Siamo al 130%, ma devo spiegare a tutti che serve ancora donare.» |
| P11 | Amir Haddad, 27, Torino | Promotore: comunicazione della campagna | Laptop Linux + Firefox; Android + Chrome | 5/5 | Usa quasi solo la tastiera; italiano B2 | «Porto donatori dall'estero: il sito deve parlare anche la loro lingua.» |
| P12 | Maria Lombardi, 49, Torino | Partner esterna (associazione) che cerca un contatto con UniTo | Smartphone Android; vecchio PC Windows con schermo piccolo | 2/5 | Tremore essenziale lieve alle mani | «So organizzare il quartiere; non so a quale porta bussare in Università.» |

## 3. Bisogni e punti di dolore per persona

Per ogni persona: i **bisogni concreti** che il sito deve soddisfare e i **punti di dolore del journey** (fase, criticità, opportunità indicata nel journey, problemi collegati). I punti di dolore hanno un codice `Jxx-Fn` e diventeranno gli scenari di verifica della Fase 5.

### P01 · Giuseppe Ferrero (J01: donare 50 € a una ricerca sui neonati, dal tablet)

Bisogni:
- B01-1 Capire subito che cos'è il sito e chi lo gestisce (P-001, P-003).
- B01-2 Leggere testi grandi e contrastati; toccare bersagli ampi (P-034, P-076).
- B01-3 Spiegazioni in italiano semplice, senza gergo (P-025, P-068).
- B01-4 Stato della raccolta senza ambiguità: niente percentuali oltre il 100% non spiegate, niente giorni negativi (P-022, P-024).
- B01-5 Donare una somma senza dover scegliere una «ricompensa» (modello mentale dell'offerta) (P-065).
- B01-6 Errori segnalati subito, riepilogo prima di pagare, conferma con un riferimento da conservare e un numero da chiamare (P-054, P-080).

| Codice | Fase | Criticità nel journey | Opportunità indicata | Problemi |
|---|---|---|---|---|
| J01-F1 | Scoperta (motore di ricerca) | Titolo troncato, nome del servizio non coerente | Titolo breve, nome coerente | P-002 |
| J01-F2 | Orientamento in homepage | Non spiega il servizio; contrasto e dimensioni ostacolano la lettura | Frase iniziale, gestore visibile, testo grande, contrasto ≥ 4,5:1 | P-001, P-034 |
| J01-F3 | Capire la donazione («Come funziona») | Testo continuo, piccolo, con termini inglesi | Indice, paragrafi brevi, glossario, telefono sempre visibile | P-074, P-076, P-025 |
| J01-F4 | Valutare il progetto | Oltre 100%, giorni negativi e aperture in nuove schede confondono stato e tasto Indietro | Stato testuale, data comprensibile, link interni nella stessa scheda | P-022, P-024, P-014 |
| J01-F5 | Donare | Errore solo dopo l'invio; ricompensa «obbligata» | Validazione immediata, importo libero evidente, riepilogo | P-054, P-065 |
| J01-F6 | Dopo la donazione | Senza riferimento umano dubita dell'esito | Conferma con codice, contatti con orari e tempi di risposta | P-080 |

### P02 · Sara Colombo (J02: donare 20 € durante una pausa, finire dal laptop)

Bisogni:
- B02-1 Pagina leggera che mostri subito il contenuto principale su 4G (P-087).
- B02-2 Capire in pochi secondi scopo, affidabilità e stato; sommario per saltare alle sezioni (P-049).
- B02-3 Importo libero riconoscibile, senza premio obbligatorio, con minimo esplicito (P-042, P-065).
- B02-4 Errori immediati; dati conservati se si interrompe; riprendere da un altro dispositivo con un link (P-054).
- B02-5 Feedback immediato a ogni clic (P-039).
- B02-6 Comandi grandi, usabili con una mano.

| Codice | Fase | Criticità | Opportunità | Problemi |
|---|---|---|---|---|
| J02-F2 | Primo caricamento | Contenuto principale dopo diversi secondi sulla rete debole | Pagina leggera, contenuto essenziale prima | P-087 |
| J02-F3 | Valutazione rapida | Pagina molto lunga; il contatto non mostra caricamento | Sommario con ancore; contatto con stato di caricamento | P-049, P-039 |
| J02-F4 | Scelta della ricompensa | Lista lunga, non confrontabile; importo libero non riconoscibile | Opzioni compatte; «Dona un importo libero» con minimo esplicito | P-042, P-065 |
| J02-F5 | Tentativo e interruzione | Modulo lento, errore dopo l'invio, dati non salvati [IPOTESI] | Validazione in linea, bozza salvata, link di ripresa | P-054, P-087 |
| J02-F6 | Ripresa sul laptop | Giorni negativi; carosello senza indicatori; deve reinserire i dati [IPOTESI] | Scadenza in data naturale; frecce e pallini; ripresa con riepilogo | P-024, P-037 |

### P03 · Davide Rinaldi (J03: sostenere una ricerca accessibile o un'alternativa attiva con NVDA)

Bisogni:
- B03-1 Struttura semantica: titoli in ordine, landmark, link descrittivi (P-046, P-011, P-012).
- B03-2 Nome, ruolo e stato accessibili per ogni controllo, compresi card, menu, spiegazioni a comparsa (P-029, P-044, P-086).
- B03-3 Stato della campagna in testo («conclusa», «in corso») e controlli di donazione disattivati quando la raccolta è chiusa (P-040).
- B03-4 Menu chiudibili con Esc, focus gestito, posizione e risultati conservati tornando all'elenco (P-008, P-027).
- B03-5 Errori associati al campo, annunciati, con riepilogo e focus (P-054).
- B03-6 Un canale per segnalare problemi di accessibilità.

| Codice | Fase | Criticità | Opportunità | Problemi |
|---|---|---|---|---|
| J03-F2 | Esplorazione del progetto | Immagini senza descrizione, titoli vuoti, tooltip annunciati come link | Titoli gerarchici, alt pertinenti, spiegazioni come pulsanti con nome e stato | P-046, P-044 |
| J03-F3 | Verifica dello stato | Stato affidato a colore o simbolo; ricompense e importo attivi nella campagna conclusa | «Campagna conclusa» annunciata; controlli disattivati e spiegazione | P-040 |
| J03-F4 | Ricerca di un'alternativa | Menu non chiudibile con Esc; link uguali; card senza nome; posizione persa | Menu con Esc; link descrittivi; card nominate; posizione conservata | P-008, P-011, P-012, P-029, P-027 |
| J03-F5 | Donazione | Errore dopo l'invio, senza focus | Validazione immediata; riepilogo errori con focus e link ai campi | P-054 |
| J03-F6 | Resoconto all'associazione | Accessibilità complessiva mediocre riduce la credibilità | Test con tastiera e screen reader; dichiarazione di accessibilità; canale di feedback | P-087 (accessibilità 64–77), P-085 |

### P04 · Tomás García (J04: capire e donare 50 € dall'estero, condividere con amici non italiani)

Bisogni:
- B04-1 Tutto il percorso in inglese, dalla scheda alla conferma, compresi errori e regole (P-043, P-054).
- B04-2 Una sola lingua visibile, ricompense impaginate allo stesso modo in ogni progetto (P-051, P-047).
- B04-3 Regole («tutto o niente», cofinanziamento) e costi totali prima di pagare; sapere cosa succede se l'obiettivo non viene raggiunto (P-063, P-044).
- B04-4 Metodi di pagamento con nomi noti e coerenti (P-062).
- B04-5 Link esterni annunciati (P-014).
- B04-6 Link di condivisione che conserva la lingua scelta.

| Codice | Fase | Criticità | Opportunità | Problemi |
|---|---|---|---|---|
| J04-F2 | Arrivo e ricerca della lingua | Solo la descrizione è tradotta; «overfunding», «100% successo» non spiegati | Traduzione completa; glossario nella lingua scelta | P-043, P-025 |
| J04-F3 | Progetto e regole | «Tutto o niente» assente in inglese; guida del partner su altro sito senza avviso | Regole tradotte vicino al pulsante; avviso e icona sui link esterni | P-043, P-014 |
| J04-F4 | Scelta della ricompensa | Testi ripetuti in due lingue, disposti diversamente tra progetti | Una lingua; impaginazione uguale; minimo e posti rimasti visibili | P-051, P-047 |
| J04-F5 | Modulo e pagamento | Errore dopo l'invio, solo in italiano; nessun richiamo al «tutto o niente»; metodi incoerenti; commissioni non rimborsate solo nelle FAQ | Validazione in tempo reale nella lingua; riepilogo con commissioni e rimborso; metodi coerenti | P-054, P-062, P-063 |
| J04-F6 | Condivisione | Il link condiviso apre la versione italiana [IPOTESI] | Link che conserva la lingua | P-043 |

### P05 · Luca Moretti (J05: confrontare le campagne e dare 100 € a quella che ne ha più bisogno, poi seguirla)

Bisogni:
- B05-1 Stato leggibile senza distinguere i colori: testo e icona per «in corso», «obiettivo raggiunto», «conclusa» (P-028, P-022, P-040).
- B05-2 Tema su ogni card; filtri e ordinamento per scadenza e percentuale; confronto senza aprire tutti i progetti (P-030, P-031).
- B05-3 Sapere quanti progetti restano e quando l'elenco è finito; tornare all'elenco nello stesso punto (P-032, P-033, P-027).
- B05-4 Cifre e scadenze univoche: nessun giorno negativo, soglie spiegate, quanto manca in euro (P-024, P-053).
- B05-5 Vedere il raddoppio dell'Ateneo dove si decide (P-048).
- B05-6 Ritrovare il progetto sostenuto nelle settimane successive, anche da smartphone.

| Codice | Fase | Criticità | Opportunità | Problemi |
|---|---|---|---|---|
| J05-F1 | Esplorazione dell'elenco | Barre distinte solo dal colore; contrasto basso; contatore che non separa attive e concluse | Etichette e icone accanto a ogni barra; contrasto adeguato; contatori separati | P-028, P-034 |
| J05-F2 | Confronto | Card senza tema; nessun filtro/ordinamento; «Altri» opaco e senza fine; posizione persa | Tema sulle card; filtri e ordinamento; conteggio e fine elenco; ritorno nella stessa posizione | P-030, P-031, P-032, P-033, P-027 |
| J05-F3 | Verifica di stato e bisogno | Oltre 100% senza etichetta; giorni negativi; concluse con ricompense attive; «nuovo obiettivo» ambiguo | Etichetta testuale; scadenze in parole; concluse disattivate; soglie in una riga | P-022, P-024, P-040, P-053 |
| J05-F4 | Decisione | Il raddoppio dell'Ateneo non compare dove si dona | «Se l'obiettivo viene raggiunto, l'Ateneo raddoppia», con la cifra che manca | P-048 |
| J05-F6 | Monitoraggio | Posizione persa; giorni negativi | Ritorno nella stessa posizione; «Mancano 12 giorni», «Conclusa da 36 giorni» | P-027, P-024 |

### P06 · Elena Conti (J06: 300 € anonimi con ricevuta, solo se tutto è trasparente)

Bisogni:
- B06-1 Sapere chi gestisce il servizio, dalla prima schermata (P-003).
- B06-2 Programma con date, numeri coerenti da un'unica fonte, promotori con nome completo e ruolo, chi contattare (P-021, P-036, P-026, P-035).
- B06-3 Regole economiche in un solo posto, con un solo nome per ogni concetto; link diretti (P-075, P-070, P-069, P-063).
- B06-4 Controllo sui propri dati: anonimato come scelta esplicita, sapere cosa riceve il promotore (P-055, P-056).
- B06-5 Ricevuta e detraibilità spiegate prima e dopo la donazione (P-064).
- B06-6 Un contatto diretto con orari.

| Codice | Fase | Criticità | Opportunità | Problemi |
|---|---|---|---|---|
| J06-F1 | Affidabilità del servizio | «Chi siamo» solo in fondo | Frase in homepage e link a «Chi siamo» in alto | P-003 |
| J06-F2 | Verifica del programma | Futuro senza date; numeri che non coincidono; promotori informali; nessun contatto | Date in evidenza; numeri da un'unica fonte; nome e ruolo del promotore; «Chi può candidarsi» con contatti | P-021, P-036, P-026, P-035 |
| J06-F3 | Regole economiche | FAQ mista senza ricerca; due nomi per la stessa modalità; «commissioni» porta alle condizioni d'uso; commissioni trattenute anche in caso di fallimento | FAQ divise con ricerca; un solo nome; link diretto; rimborso spiegato accanto all'importo | P-075, P-070, P-069, P-063 |
| J06-F5 | Donazione e privacy | Nessun richiamo al «tutto o niente»; anonimato non preselezionato; il promotore riceve comunque i dati | Richiamo nel modulo; anonimato esplicito; dire prima quali dati riceve il promotore | P-054, P-055, P-056 |
| J06-F6 | Ricevuta e documentazione | Detraibilità e ricevuta non spiegate | Sezione «Ricevuta e detraibilità» nel modulo e nella conferma | P-064 |

### P07 · Giulia Esposito (J07: trovare un progetto UniTo, donare 5–10 €, condividerlo)

Bisogni:
- B07-1 Capire subito di che sito si tratta e trovare i progetti nella prima schermata (P-001, P-004).
- B07-2 Ricerca testuale visibile; titoli completi e stato «concluso» chiaro (P-005, P-038).
- B07-3 Testi brevi, titoli, grassetti, indice; struttura che la lettura vocale di iOS legge bene (P-049, P-074).
- B07-4 Sapere il minimo donabile prima di iniziare; errore immediato se l'importo è troppo basso (P-054, P-065).
- B07-5 Caroselli con indicatori (P-037); condivisione facile.

| Codice | Fase | Criticità | Opportunità | Problemi |
|---|---|---|---|---|
| J07-F2 | Prima impressione | Scopo assente; servizi prima dei progetti; titoli e stato ambigui | Tagline; progetti in prima schermata; titoli completi e badge «Concluso» | P-001, P-004, P-038 |
| J07-F3 | Ricerca dei progetti | Nessuna ricerca; carosello senza indicatori; inglese non spiegato | Ricerca sempre visibile; indicatori; glossario | P-005, P-037, P-025 |
| J07-F4 | Lettura e regole | Pagina senza indice; testo continuo | Indice con ancore, «Torna su», sezioni con titoli | P-049, P-074, P-015 |
| J07-F5 | Donazione piccola | Errore sul minimo solo dopo l'invio; importo libero e minimo poco chiari | Minimo vicino al campo; validazione in linea | P-054, P-065 |

### P08 · Roberta Galli (J08: ricostruire edizioni, progetti e risultati per un articolo)

Bisogni:
- B08-1 Sapere a quale edizione e periodo si riferiscono pagine e numeri; numeri coerenti con data di aggiornamento (P-021, P-036, P-013).
- B08-2 Vedere tutti i progetti, con filtri per edizione e stato, totale e fine elenco, posizione conservata, «Torna su» (P-031, P-032, P-033, P-027, P-015).
- B08-3 Presentazione del progetto prima degli aggiornamenti; gruppo attribuito chiaramente a UniTo (P-041, P-026).
- B08-4 Contatto con feedback immediato; referente UniTo con email e telefono (P-039, P-035).
- B08-5 URL stabili e condivisibili (filtri nella URL), link esterni dichiarati (P-014).

| Codice | Fase | Criticità | Opportunità | Problemi |
|---|---|---|---|---|
| J08-F1 | Informazioni sull'iniziativa | Stato temporale assente; numeri discordanti; cambio di sito non annunciato | Date e stato della call; fonte unica; link esterno segnalato | P-021, P-036, P-014 |
| J08-F2 | Progetti conclusi | Caricamento opaco; fine non dichiarata; stato perso; filtri assenti; niente «Torna su» | Paginazione con totale; messaggio finale; stato persistente; filtri; «Torna su» | P-032, P-033, P-027, P-031, P-015 |
| J08-F3 | Caso di un progetto concluso | Aggiornamenti prima del contesto; gruppo non attribuito a UniTo | Descrizione prima delle notizie; «Gruppo – Dipartimento UniTo» | P-041, P-026 |
| J08-F4 | Contatto con le fonti | Nessun feedback; nessun contatto UniTo | Indicatore di caricamento; referente con email e telefono | P-039, P-035 |
| J08-F5 | Verifica dei numeri | Dati discordanti; blog senza articoli e date | Contatori coerenti con data di aggiornamento | P-036, P-013 |
| J08-F6 | Pubblicazione | I lettori arriveranno su una pagina senza date | Pagina del programma aggiornata e datata | P-021 |

### P09 · Chiara Marino (J09: candidare un progetto sugli impollinatori)

Bisogni:
- B09-1 Stato del bando e scadenza visibili (P-021).
- B09-2 Requisiti, modulo, ufficio di riferimento; percorso del programma distinto dalla registrazione generica (P-035, P-078).
- B09-3 Costi chiari prima di registrarsi; termini spiegati; un solo nome per concetto (P-071, P-068, P-070).
- B09-4 «Come funziona» con indice e titoli; FAQ per promotori; testo leggibile (P-074, P-075, P-076).
- B09-5 Ogni passo nominato ha il suo link (P-069).
- B09-6 Modulo con etichette persistenti, controlli nativi, errori che spariscono quando il campo è corretto (P-073, P-072, P-077).
- B09-7 Riprendere tra più sessioni (indirizzi stabili, sezioni con ancore).

| Codice | Fase | Criticità | Opportunità | Problemi |
|---|---|---|---|---|
| J09-F1 | Scoperta | Nessuna data di candidatura | Stato della call e scadenza | P-021 |
| J09-F2 | Capire il programma | Requisiti e contatto assenti; cambio di sito non avvisato; percorso ambiguo | Pagina di candidatura con requisiti, scadenza, modulo, referente | P-035, P-014, P-078 |
| J09-F3 | Regole e costi | Testo continuo; testo piccolo; FAQ miste; gergo; nomi incoerenti; quota nascosta | Indice e titoli; corpo leggibile; FAQ per promotori; glossario; costi in evidenza | P-074, P-076, P-075, P-068, P-070, P-071 |
| J09-F4 | Passo successivo | Passo citato non linkato; registrazione generica | Un unico pulsante «Candidati al programma» | P-069, P-078 |
| J09-F5 | Registrazione | Etichette che spariscono; niente controlli del browser; errore che resta | Etichette persistenti, `type`/`autocomplete`/`required`, errore che si rimuove | P-073, P-072, P-077 |

### P10 · Franco Gallo (J10, To-be: tenere viva una campagna oltre il 100% e rendicontare)

Bisogni:
- B10-1 Card con titolo intero, tema, «Gruppo · Dipartimento UniTo», stato testuale, cifre grandi (P-038, P-030, P-026).
- B10-2 Stato «Obiettivo raggiunto · raccolta ancora aperta» e nuovo obiettivo con cifra e scopo (P-022, P-053).
- B10-3 Cofinanziamento spiegato accanto a «Sostieni», con un esempio; regola chiara oltre il 100% (P-048).
- B10-4 «Scrivi al gruppo» con conferma immediata e tempi di risposta (P-039).
- B10-5 Campagna conclusa senza equivoci: data, totale, cofinanziamento, «Leggi i risultati» (P-040).
- B10-6 Resoconto finale negli aggiornamenti (percorso «seguire un progetto già sostenuto»).

| Codice | Fase | Criticità | Opportunità | Problemi |
|---|---|---|---|---|
| J10-F1 | Controllo della pagina pubblica | Titolo tagliato; tema e dipartimento assenti; cifre piccole | Titolo intero, tema, gruppo e dipartimento, cifre grandi | P-038, P-030, P-026 |
| J10-F2 | Superamento dell'obiettivo | Percentuale oltre il 100% non spiegata; «nuovo obiettivo» senza scopo | Badge «Obiettivo raggiunto · raccolta ancora aperta»; nuovo obiettivo con cifra e scopo | P-022, P-053 |
| J10-F3 | Rilancio | Cofinanziamento non vicino a «Sostieni» | Riquadro del cofinanziamento con esempio e link alle regole | P-048 |
| J10-F4 | Domande dei donatori | Non si sa se il messaggio è partito né quando arriva la risposta | «Scrivi al gruppo» con conferma e tempi; FAQ della campagna | P-039 |
| J10-F5 | Chiusura | Pulsante e campo importo ancora attivi | «Campagna conclusa» con data e totale; «Leggi i risultati» | P-040 |
| J10-F6 | Resoconto | Senza resoconto i donatori non sanno com'è finita | Resoconto in «Aggiornamenti» | P-041 (ordine delle sezioni) |

### P11 · Amir Haddad (J11, To-be: promuovere la campagna anche all'estero)

Bisogni:
- B11-1 Selettore IT/EN che traduce tutto il percorso, modulo e messaggi compresi; una lingua per volta (P-043, P-051, P-054).
- B11-2 Regole e importo minimo vicino al campo, nella lingua scelta (P-054, P-065).
- B11-3 Menu con Esc, focus visibile, elementi che non sembrano link quando non lo sono, feedback al clic (P-008, P-085, P-044, P-039, P-050).
- B11-4 Pagine leggere su smartphone; caroselli con indicatori (P-087, P-037).
- B11-5 Indicazioni per i team su contenuti in due lingue e un canale per segnalare problemi [IPOTESI].

| Codice | Fase | Criticità | Opportunità | Problemi |
|---|---|---|---|---|
| J11-F1 | Contenuti bilingui | Nessuna indicazione su come scrivere in due lingue | Guida «Contenuti in due lingue» per i team | P-051, P-047 |
| J11-F2 | Verifica della versione inglese | Parti non tradotte; lingue mescolate; termini tecnici | Selettore IT/EN completo; glossario | P-043, P-025 |
| J11-F3 | Promozione sui social | Scheda lenta da smartphone; caroselli senza indicatori | Immagini leggere; frecce o pallini | P-087, P-037 |
| J11-F4 | Assistenza ai donatori stranieri | Errori dopo l'invio e in italiano; regola non ricordata | Validazione in linea nella lingua; regole accanto al campo | P-054 |
| J11-F5 | Verifica da tastiera e smartphone | Menu senza Esc; focus poco visibile; elementi che sembrano link; pulsanti senza riscontro | Esc, focus visibile, link e pulsanti distinguibili, feedback immediato | P-008, P-085, P-044, P-050, P-039, P-015 |
| J11-F6 | Report al gruppo | Nessun canale né tempi per le segnalazioni [IPOTESI] | «Segnala un problema» con conferma e tempi | P-080 |

### P12 · Maria Lombardi (J12, To-be: capire se un'associazione può collaborare e chi contattare)

Bisogni:
- B12-1 Frase d'apertura su che cos'è il sito e chi lo gestisce; «Chi siamo» nel menu (P-001, P-003).
- B12-2 Menu breve con voci grandi e distanziate; bersagli ≥ 44 px (P-008).
- B12-3 Pagina «Chi può proporre un progetto» con una sezione per enti esterni, costi in evidenza, glossario, FAQ divise (P-035, P-071, P-068, P-075).
- B12-4 Modulo breve con etichette visibili, campi grandi, errori in linea che spariscono, nota «inviare non vi impegna», tempi di risposta (P-073, P-077, P-080).
- B12-5 Esempi di progetti con scuole e territorio; riepilogo stampabile per il direttivo.

| Codice | Fase | Criticità | Opportunità | Problemi |
|---|---|---|---|---|
| J12-F1 | Scoperta | La home non dice che cos'è il sito e chi lo gestisce | Frase d'apertura; «Chi siamo» in alto | P-001, P-004 |
| J12-F2 | Chi gestisce il sito | «Chi siamo» in fondo; niente esempi con il territorio; menu fitto | «Chi siamo» nel menu; progetti con il territorio; menu breve con voci grandi | P-003, P-008, P-010, P-005 |
| J12-F3 | Chi può proporre, costi, regole | Requisiti per enti esterni assenti; costi in piccolo o tardi; gergo; FAQ in un'unica lista | «Chi può proporre» con «Enti esterni», costi in evidenza, glossario, FAQ per pubblico | P-035, P-071, P-076, P-068, P-075, P-070, P-069 |
| J12-F4 | Richiesta di collaborazione | Etichette che spariscono; caselle piccole; errori che restano; non sa cosa succede dopo | Etichette visibili, campi grandi, errori in linea, «inviare non vi impegna» | P-073, P-072, P-067, P-077 |
| J12-F5 | Contatto con l'ufficio | Tempi di risposta non indicati | Conferma con tempi, numero e referente | P-080 |
| J12-F6 | Decisione del direttivo | Nessuna garanzia sui tempi [IPOTESI] | Riepilogo stampabile della richiesta | — (bisogno della persona) |

## 4. Bisogni trasversali emersi

| Bisogno | Personas | Problemi |
|---|---|---|
| Capire subito che cos'è il servizio e chi lo gestisce | P01, P06, P07, P12 | P-001, P-003 |
| Stato della campagna in testo, mai solo con il colore | P01, P03, P05, P10 | P-022, P-024, P-028, P-040 |
| Cofinanziamento e soglie spiegati dove si dona | P05, P10, P04 | P-048, P-053 |
| Validazione in linea nella lingua della pagina | P01, P02, P03, P04, P07, P11 | P-054 |
| Versione inglese completa | P04, P11 | P-043, P-051 |
| Orientamento: indice, «Torna su», posizione conservata | P02, P03, P05, P07, P08 | P-015, P-027, P-049 |
| Percorso del promotore con requisiti, costi e contatti | P09, P12 | P-035, P-071, P-078 |
| Testi grandi, contrasto alto, bersagli ampi | P01, P10, P12, P05 | P-034, P-076 |
| Tastiera e screen reader | P03, P11 | P-008, P-029, P-044, P-085, P-086 |
| Trasparenza su dati, commissioni e ricevuta | P04, P06 | P-055, P-056, P-063, P-064 |
| Continuità tra dispositivi e sessioni (link stabili, dati conservati) | P02, P08, P09, P12 | P-027, P-061 |
