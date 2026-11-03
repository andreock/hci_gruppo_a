# 05 · Tracciabilità problema → requisito → soluzione

Documento centrale della consegna, aggiornato alla fine della Fase 5 (31/10/2026). Generato da `tools/genera-tracciabilita.py` a partire da `02_problemi_consolidati.md`, `03_bisogni_personas.md`, `04_requisiti.md` e `tools/soluzioni.py`. Le verifiche rimandano ai report in `docs/verifiche/` («percorsi #n» = controllo n di `percorsi.md`) e a `08_verifica_personas.md`.

Le sigle delle fonti sono spiegate in `02_problemi_consolidati.md`. La colonna «Personas e journey» riporta i punti di dolore `Jxx-Fn` di `03_bisogni_personas.md` e, tra parentesi, le personas i cui bisogni (`Bxx-n`) citano il problema.

## 1. Problema → soluzione

| ID problema | Problema (sintesi) | Fonte in assignment1 | Euristica di Nielsen | Criterio WCAG | Gravità | Personas e journey coinvolti | Requisito (R-xxx) | Soluzione adottata | Dove | Verifica | Stato |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P-001 | Nella parte alta non c'è una frase che dica che cos'è il servizio (homepage) o il programma (pagina… | GA s59; A1-P16 r17; AN-PR:57 | LG1 / H8 | — | 4 | J01-F2, J07-F2, J12-F1 | R-001 | Frase iniziale su che cos'è ideaBlume e chi lo gestisce; frase di sintesi in apertura del programma | `index.html` (hero), `programma.html` | screenshot `home-1280/375`; 08 J01-F2, J12-F1 | risolto |
| P-002 | Titolo della finestra lungo (83 caratteri, troncato su Google), marchio con nomi diversi («GINGER», «Idea… | GA s60; A2-P03 r4; LZ-FAQ:43, :77 | LG2 / H1 / H4 | 2.4.2 | 1 | J01-F1 | R-013 | Titoli «Pagina – ideaBlume», univoci, ≤ 60 caratteri; un solo nome del marchio | `tools/build.py` `pagina()` | `axe.md`: 0 titoli lunghi, 0 duplicati | risolto |
| P-003 | «Chi siamo» è solo nel footer | GA s61 | LG3 | — | 3 | J06-F1, J12-F2 (P01) | R-001, R-016, R-088 | «Chi siamo» nel menu principale e nella prima frase della home | intestazione, `index.html`, `chi-siamo.html` | screenshot `home-1280`; 08 J06-F1 | risolto |
| P-004 | Nella prima schermata i servizi per chi lancia campagne (academy, podcast, campaign manager, blog) vengono… | GA s62 | LG4 | — | 2 | J07-F2, J12-F1 | R-002 | Progetti in corso subito dopo la frase iniziale; ingresso per chi propone in fondo | `index.html` | screenshot `home-1280`; 08 J07-F2 | risolto |
| P-005 | Nessun campo di ricerca visibile | GA s63 | LG5 / H7 | — | 1 | J07-F3, J12-F2 | R-003 | Campo di ricerca con etichetta in home, nei filtri della pagina Progetti e in «Cerca» (D-43) | `index.html`, `progetti.html`, `cerca.html` | percorsi #2–3 | risolto |
| P-006 | La ricerca senza risultati mostra una pagina vuota, senza messaggio né suggerimenti | A1-P18 r19; AN-PR:119 | H9 | 4.1.3 | 3 | — | R-004, R-096 | Risultati con conteggio annunciato; «Nessun progetto per …» con suggerimenti, temi e link; trova anche le pagine del sito; tollera singolare e plurale | `cerca.html`, `js/ideablume.js` | percorsi #31–33 e «veterinaria» | risolto |
| P-007 | Per ritrovare il programma bisogna ricordare che UniTo è un «Partner» e cercarlo tra 25 nomi in ordine non… | A1-P12 r13 | H6 | — | 2 | — | R-005 | Il programma è una voce di primo livello con il suo nome; la ricerca lo trova | menu, `programma.html` | percorsi #33 | risolto |
| P-008 | Menu e tendine con oltre 70 voci | GA s67; A2-P01 r2; A2-P06 r7 | LG9 / H3 / H1 | 2.1.1, 1.4.13 | 2 | J03-F4, J11-F5, J12-F2 | R-005, R-006 | Menu di 8 voci senza tendine; menu mobile con `aria-expanded`, Esc, focus restituito, voci nascoste non focalizzabili; voci alte 48 px | intestazione, CSS `.main-nav`, JS menu | percorsi #34–37 | risolto |
| P-009 | Né la barra né il menu indicano la sezione in cui ci si trova | A2-P02 r3 | H1 | 2.4.8 (AAA) | 2 | — | R-007 | `aria-current="page"` e sottolineatura spessa sulla voce corrente | `header()` | screenshot `programma-1280` | risolto |
| P-010 | Una piccola icona «casa» senza etichetta duplica il logo che porta alla home | GA s19; AN-PR:94 | H6 | 1.1.1, 2.4.4 | 1 | J12-F2 | R-008 | Il logo ha un nome accessibile e la voce «Home» del menu è scritta per esteso: nessuna icona senza etichetta (D-44) | `header()` | `link.md`, `axe.md` | risolto |
| P-011 | Link con testo generico ripetuto | GA s65; A2-P10 r11; LZ-CF:136 | LG7 / H4 | 2.4.4 | 2 | J03-F4 | R-010 | Nessun link generico ripetuto; testo nascosto distintivo dove il testo visibile si ripete (FAQ, ricompense) | tutte le pagine | `link.md`: 0 testi uguali verso destinazioni diverse (trovato e corretto nelle FAQ) | risolto |
| P-012 | Il testo alternativo delle icone delle categorie ripete l'etichetta accanto | GA s68 | LG10 | 1.1.1 | 1 | J03-F4 | R-040, R-098 | Icone e illustrazioni decorative con `alt=""` o `aria-hidden` | card, icone di stato | `axe.md` (image-alt) | risolto |
| P-013 | Il blog in homepage è solo un invito, senza articoli né date | GA s66; LZ-FAQ:140 | LG8 / H10 | — | 1 | J08-F5 | R-017, R-089 | «Ultimi aggiornamenti dai progetti» datati in home; data di aggiornamento su FAQ, programma, accessibilità | `index.html`, `faq.html`, `programma.html` | screenshot `home-1280` | risolto |
| P-014 | Link interni aperti in una nuova scheda («Scopri tutti i progetti!» | GA s14; A1-P07 r8; A2-P05 r6; AL R-P07:208; LZ-FAQ:64 | H3 | 3.2.5 (AAA, buona pratica) | 3 | J01-F4, J04-F3, J08-F1, J09-F2 | R-009 | Link interni sempre nella stessa scheda; link esterni dichiarati (il sito non ne ha) | tutte le pagine | `link.md`: 0 `target=_blank` | risolto |
| P-015 | Nelle pagine lunghe manca un pulsante «Torna su» | GA s20, s38; AN-MC:74 | H7 | — | 3 | J07-F4, J08-F2, J11-F5 | R-012 | «Torna su» in fondo alle pagine lunghe | `torna_su()` in `build.py` | `responsive.md` | risolto |
| P-016 | Nelle pagine informative manca il breadcrumb | LZ-CF:64; LZ-FAQ:65 | H3 | 2.4.8 (AAA) | 1 | — | R-011 | Briciole di pane in tutte le pagine interne | `breadcrumb()` in `build.py` | `axe.md`; screenshot | risolto |
| P-017 | Manca un link «Salta al contenuto» | LZ-FAQ:105; LZ-CF:106 | H7 | 2.4.1 | 3 | — | R-090 | «Salta al contenuto» come primo elemento focalizzabile | intestazione | percorsi #1; `tastiera-01-salta.png` | risolto |
| P-018 | Su smartphone una colonna di nove link (condizioni, privacy, cookie…) precede il contenuto | A2-P16 r17 | H8 | — | 1 | — | R-121 | Su mobile il contenuto segue intestazione e briciole; nessuna colonna di link prima del contenuto | layout | screenshot `*-375`; residuo V-04 (gravità 1) | risolto |
| P-019 | La pagina 404 è fuori dal modello del sito (niente logo, menu, ricerca, footer) e non ha il meta viewport | A1-P10 r11 | H4 | 1.4.10 | 2 | — | R-014, R-094 | 404 nel modello del sito, responsive, in IT ed EN; funziona a qualunque profondità su GitHub Pages | `404.html`, `en/404.html` | `axe.md`, `responsive.md`; da provare dopo la pubblicazione | risolto |
| P-020 | Il messaggio 404 è in inglese in un sito italiano, con refusi («Opps!», «adress»), e offre solo il ritorno… | A1-P19 r20; AN-PR:117; LZ-CF:126; LZ-FAQ:130; `assignment1/lorenzo/screen_faq/cmf_e9_404.png` | H9 | 3.1.1 | 2 | — | R-014 | Messaggio chiaro nella lingua giusta, indirizzo richiesto, ricerca, link a home, progetti, FAQ, contatti | `404.html` | `axe.md` | risolto |
| P-021 | Non si capisce se il programma è attivo | GA s9; A1-P01 r2 | H1 | — | 3 | J06-F2, J08-F1, J08-F6, J09-F1 | R-070 | Stato attuale con fase e data di fine delle campagne, fasi evidenziate; date del prossimo bando | `programma.html#stato` | 08 J06-F2, J09-F1 | risolto |
| P-022 | Le campagne in corso oltre il 100% (MILK-ACT 181%, RePatch 109%) non hanno l'etichetta «obiettivo raggiunto» | GA s10; AN-PR:46 | H1 | 1.4.1 | 3 | J01-F4, J05-F3, J10-F2 | R-021, R-030, R-093 | Badge «Obiettivo raggiunto · puoi ancora sostenerlo per N giorni (scade il …)» con icona e testo | card, riquadro di stato | `dati.md`; percorsi #29 | risolto |
| P-023 | Stato contraddittorio | AL A-P01:68 | H1 | — | 3 | — | R-022, R-030, R-131 | Stato calcolato da un'unica funzione (Python per le pagine, JS per le date dimostrative) | `calcola()` in `build.py` e `ideablume.js` | `dati.md`: stato coerente con il raccolto | risolto |
| P-024 | I giorni rimanenti sono scritti come numero negativo («-36 giorni») | GA s11; A1-P04 r5; AN-PR:45; AN-MC:48; AL R-P04:83 | H2 | — | 2 | J01-F4, J02-F6, J05-F3, J05-F6 | R-021, R-030 | Giorni mai negativi; scadenza con data; ultimo giorno esplicito | `status` in `i18n/*.json` | `dati.md`: nessun giorno negativo dal 2026 al 2030 | risolto |
| P-025 | Termini inglesi e gergo non spiegati | GA s12; A1-P06 r7; AN-PR:56; AN-MC:60 | H2 | 3.1.3 (AAA) | 2 | J01-F3, J04-F2, J07-F3, J11-F2 | R-083 | Lessico controllato senza gergo; «Le parole di ideaBlume» nelle FAQ; versione inglese completa | `i18n/*.json`, `faq.html#parole` | `dati.md`: nessun termine escluso | risolto |
| P-026 | I nomi dei promotori nelle card sono eterogenei («by Departments & Dragons», «by Team GaIA») | GA s13; AN-PR:58, :92 | H2 / H6 | — | 2 | J06-F2, J08-F3, J10-F1 | R-020, R-043 | Formula unica «Gruppo X · Dipartimento di …, Università di Torino» e responsabile scientifico | card, pagina progetto | `dati.md`; 08 J10-F1 | risolto |
| P-027 | Tornando da un progetto con Indietro la pagina riparte dall'inizio e i progetti caricati con «Altri»… | GA s15; AN-PR:66 | H3 | — | 4 | J03-F4, J05-F2, J05-F6, J08-F2 | R-024 | Filtri nella URL; posizione di scorrimento salvata e ripristinata | `progetti.html`, `js/ideablume.js` | percorsi #27–28 | risolto |
| P-028 | Barre di avanzamento poco chiare (blu e rosso) | GA s16; AN-PR:75, :111 | H4 | 1.4.1 | 2 | J05-F1 | R-020, R-021, R-026, R-027, R-093 | Barra a un colore su sfondo neutro, non interattiva; contatori in corso/conclusi; stato su tutte le card | card, `progetti.html` | `contrasti.md` (4,86:1); `dati.md` | risolto |
| P-029 | Al passaggio del mouse le card non sembrano cliccabili | GA s17; AN-PR:77 | H4 | 2.4.4, 4.1.2 | 4 | J03-F4 | R-023 | Un solo link (il titolo) esteso a tutta la card; hover e focus evidenti | card | percorsi #4; `tastiera-03-card-focus.png` | risolto |
| P-030 | Le card non indicano tema o categoria | GA s18; AN-PR:93 | H6 | — | 2 | J05-F2, J10-F1 | R-020 | Tema sulla card e filtro per tema | card, filtri | percorsi #25 | risolto |
| P-031 | Nessun filtro (categoria, obiettivo ONU, edizione) né ordinamento (scadenza) | GA s21; A1-P14 r15; AN-PR:67, :98 | H7 | — | 3 | J05-F2, J08-F2 | R-024 | Filtri per stato, tema, dipartimento, anno, programma; 4 ordinamenti | `progetti.html` | percorsi #25–30 | risolto |
| P-032 | «Altri» carica quattro progetti alla volta e non dice quanti ne restano (13 conclusi, se ne vedono 4) | GA s22; A1-P14 r15; AN-PR:99 | H7 | — | 3 | J05-F2, J08-F2 | R-025 | Tutti i progetti in una griglia con «Mostrati N di M progetti» | `progetti.html` | percorsi #26 | risolto |
| P-033 | A fine elenco «Altri» scompare senza dire che i progetti sono finiti | GA s24; AN-PR:116 | H9 | — | 2 | J05-F2, J08-F2 | R-025 | «Hai visto tutti i progetti di questa selezione» | `progetti.html` | percorsi #30 | risolto |
| P-034 | Contrasto insufficiente | GA s23; AN-PR:112; AN-MC:124; AL A-P10:198; A2-P09 r10 | H8 (GA) / H6 (AL) / H4 (A2) | 1.4.3, 1.4.11 | 4 | J01-F2, J05-F1 | R-092 | Palette con tutti i contrasti verificati da script | `css/ideablume.css` | `contrasti.md` (52/52) | risolto |
| P-035 | La pagina del programma non dice chi può candidarsi, entro quando, con quale modulo né chi contattare | GA s25; A1-P20 r21; AN-PR:127 | H10 | — | 2 | J06-F2, J08-F4, J09-F2, J12-F3 | R-071 | Chi può candidarsi, requisiti, come e quando, a chi scrivere; contatti dell'Ufficio | `programma.html`, `proponi.html` | 08 J09-F2, J12-F3 | risolto |
| P-036 | Numeri complessivi del programma incoerenti | AN-PR:74 | H4 | — | 2 | J06-F2, J08-F1, J08-F5 | R-026, R-073, R-131 | Numeri calcolati dai dati, con data di aggiornamento | `index.html`, `programma.html` | `dati.md` | risolto |
| P-037 | Su smartphone i caroselli di contatori e progetti scorrono di lato senza frecce né pallini (si vedono 2… | GA s71; AN-PR:78, :79 | — (mobile) / H4 | — | 3 | J02-F6, J07-F3, J11-F3 | R-028, R-097, R-120 | Nessun carosello: griglie che vanno a capo | CSS `.grid` | `responsive.md` (320–1280 px) | risolto |
| P-038 | I titoli dei progetti nelle card sono troncati («RePatch \| il cerotto per il cuore …») e la parte… | GA s64; A1-P13 r14 | LG6 / H6 | — | 3 | J07-F2, J10-F1 | R-020 | Titoli interi su più righe; stato su ogni card al posto di nomi evocativi delle sezioni | card, filtri | `responsive.md` | risolto |
| P-039 | «Contatta il progettista» mostra i contatti dopo diversi secondi senza indicatore di caricamento | GA s28; AN-MC:50 | H1 | 4.1.3 | 3 | J02-F3, J08-F4, J10-F4, J11-F5 | R-039, R-096 | Email del gruppo subito visibile; «Scrivi al gruppo» con indicatore e conferma con tempi di risposta | pagina progetto, JS | percorsi #47–48 | risolto |
| P-040 | Sulle campagne concluse resta il box «SOSTIENI» con ricompense e prezzi, il campo «FAI TU» è ancora… | GA s29; A1-P02 r3; AL R-P02:93 | H1 | 1.4.1 | 3 | J03-F3, J05-F3, J10-F5 | R-021, R-038, R-059, R-093 | Campagne concluse: «Raccolta conclusa il …», esito, ricompense in sola lettura, nessun campo importo; donazione da URL spiegata | pagine dei progetti conclusi, `donazione.html` | percorsi #43–45; `dati.md` | risolto |
| P-041 | Gli aggiornamenti («Nuovo obiettivo», «Secondo obiettivo») vengono prima della presentazione del progetto,… | GA s30; A1-P05 r6 | H2 | — | 2 | J08-F3, J10-F6 | R-032 | Ordine fisso: presentazione prima degli aggiornamenti | pagina progetto | `dati.md`: ordine delle sezioni | risolto |
| P-042 | Le 10 ricompense sono un lungo elenco verticale (immagine, testo bilingue, contatori) non comprimibile né… | GA s31; AN-MC:73 | H3 | — | 3 | J02-F4 | R-036 | Ricompense in righe compatte e confrontabili | `#ricompense` | screenshot `progetto-*` | risolto |
| P-043 | La versione inglese è parziale | GA s32; AN-MC:61, :83 | H4 | 3.1.1, 3.1.2 | 4 | J04-F2, J04-F3, J04-F6, J11-F2 | R-110 | Inglese completo dagli stessi modelli; la build si ferma se manca una traduzione | `en/`, `i18n/en.json` | percorsi #40–42 | risolto |
| P-044 | Le spiegazioni a comparsa («O tutto o niente!», obiettivi di sostenibilità) sembrano link e puntano a «#» | GA s33; A1-P21 r22; AN-MC:86; LZ-CF:85 | H4 / H10 | 1.4.13, 4.1.2 | 1 | J03-F2, J11-F5 (P04) | R-035, R-041 | Spiegazioni come pulsanti con `aria-expanded` ed Esc; regola anche nel riquadro e nel modulo | pagina progetto, JS | percorsi #6–7 | risolto |
| P-045 | Le ricompense più alte non mostrano quante persone le hanno scelte | GA s34; AN-MC:82; A1-P09 r10 | H4 | 1.1.1 (budget in immagine) | 1 | — | R-032, R-036 | Sempre persone che l'hanno scelta (anche 0) e posti; ordine crescente; uso dei fondi in tabella testuale in posizione fissa | pagina progetto | `dati.md` | risolto |
| P-046 | Immagini informative senza testo alternativo, titoli vuoti, `h4` usati per impaginare immagini, salti di… | GA s35; AL A-P09:188; LZ-FAQ:79 | H4 | 1.1.1, 1.3.1, 2.4.6 | 3 | J03-F2 | R-040, R-090 | Un solo `h1`, titoli in ordine, alt descrittivi, nessun titolo vuoto | tutte le pagine | `axe.md`: 0 violazioni | risolto |
| P-047 | Nel box «SOSTIENI» italiano e inglese sono disposti in modo diverso in ogni progetto | GA s36 | H4 | — | 2 | J04-F4, J11-F1 | R-111 | Una lingua per volta; stessa impaginazione delle ricompense | pagina progetto | `dati.md` | risolto |
| P-048 | Il cofinanziamento dell'Ateneo (raddoppio a obiettivo raggiunto) non è mostrato dove si dona | GA s37; AN-MC:49, :101; AN-PR:126 | H6 | — | 3 | J05-F4, J10-F3 | R-029, R-034, R-072, R-084 | Riquadro «Obiettivo e raddoppio» accanto a «Sostieni» con esempio e link alle regole; frase nel passo 1 della donazione; introduzione all'elenco | progetto, donazione, elenco | 08 J05-F4, J10-F3 | risolto |
| P-049 | La pagina del progetto è molto lunga (fino a 18.030 px su mobile), densa, senza indice né ancore verso le… | GA s38; AN-MC:111, :112, :123 | H7 | 2.4.5 | 4 | J02-F3, J07-F4 | R-033 | Indice «In questa pagina» con ancore | pagina progetto | `link.md` (ancore) | risolto |
| P-050 | La barra dell'obiettivo è cliccabile e ricarica la stessa pagina | GA s39; AN-MC:113 | H7 | — | 1 | J11-F5 | R-027, R-031 | Barra non interattiva, nascosta agli screen reader, cifre scritte accanto | card, riquadro di stato | `axe.md` | risolto |
| P-051 | Testi duplicati in italiano e inglese | GA s40; A1-P17 r18; AL A-P02:108, A-P15:279; AN-MC:125 | H8 | 3.1.2 | 2 | J04-F4, J11-F1 | R-111, R-113 | Una lingua per volta; `lang` sui commenti scritti in un'altra lingua | tutte le pagine | `axe.md`; D-28 | risolto |
| P-052 | Su desktop il comando per sostenere è sotto la piega (a 924 px) e non resta visibile scorrendo | A1-P15 r16 | H7 | — | 2 | — | R-042 | «Sostieni» nella prima schermata (desktop) e subito dopo il titolo (mobile); pulsanti di scelta anche nelle ricompense | pagina progetto | screenshot `progetto-1280/375` | risolto (colonna fissa scartata: più alta dello schermo) |
| P-053 | Più soglie non spiegate | GA s30; AN-MC:32 (commento); AL:320 (positivo: in MILK-ACT il rilancio è spiegato nel testo) | H1 / H2 | — | n.d. | J05-F3, J10-F2 | R-034, R-072 | Soglie in un solo riquadro: obiettivo, raddoppio, secondo obiettivo con cifra e scopo | pagina progetto | 08 J10-F2 | risolto |
| P-054 | Gli errori del modulo (per esempio importo sotto il minimo) compaiono solo dopo l'invio e solo in… | GA s41; AN-MC:135, :136 | H9 | 3.3.1, 3.3.3, 3.1.2 | 4 | J01-F5, J02-F5, J03-F5, J04-F5, J06-F5, J07-F5, J11-F4 | R-035, R-052, R-096, R-110 | Validazione all'uscita dal campo con la correzione, nella lingua della pagina; riepilogo errori con focus; regola «tutto o niente» nel modulo | `donazione.html`, JS | percorsi #10–16, #40 | risolto |
| P-055 | Il nome del donatore diventa pubblico se non si spunta «donatore anonimo», che non è selezionata in partenza | GA s42; AN-MC:93 | H5 | — | 2 | J06-F5 | R-054 | Due scelte obbligatorie senza preselezione, con spiegazione | donazione, passo 3 | percorsi #18 | risolto |
| P-056 | Anche scegliendo l'anonimato il promotore riceve nome, email e importo del donatore | **Solo** C00 (X03, «analisi preliminare»): **non trovato in nessun file di assignment1**. Da verificare | — | — | n.d. | J06-F5 | R-054 | Detto prima dell'invio che il gruppo riceve nome ed email | donazione passo 3, FAQ | 08 J06-F5 | risolto |
| P-057 | Il checkout non indica i passi né l'effetto di «DONA ADESSO!» (in realtà reindirizza a PayPal/Satispay o… | A1-P03 r4; AL A-P14:264 | H1 / H5 | — | 3 | — | R-050, R-060 | Indicatore dei 5 passi; riepilogo sempre in alto anche su mobile; pulsante «Simula il pagamento» | `donazione.html` | percorsi #9, #22; screenshot `donazione-375` | risolto |
| P-058 | Dal modulo non si può cambiare ricompensa né annullare | A1-P08 r9 | H3 | — | 2 | — | R-051 | «Modifica» nel riepilogo, «Indietro», «Torna al progetto» | `donazione.html` | percorsi #19 | risolto |
| P-059 | Il modulo di donazione non previene gli errori | A1-P11 r12; AL A-P12:234 | H5 | 1.3.1, 1.3.5, 3.3.2, 4.1.2 | 3 | — | R-053 | `required`, `type`, `autocomplete`, `inputmode`, `label`, `fieldset` | `donazione.html` | `axe.md`; percorsi #17 | risolto |
| P-060 | I radio dei metodi di pagamento hanno come etichetta solo un'icona | AL A-P13:249 | H6 | 1.3.1, 4.1.2 | 3 | — | R-053, R-098 | Radio dei metodi con etichetta testuale completa | donazione, passo 4 | `axe.md` (label) | risolto |
| P-061 | Aprendo direttamente l'indirizzo del checkout si viene reindirizzati alla homepage senza spiegazione | AL A-P11:224; WCV `donazione_wcv_*.png` (il filmstrip mostra la homepage) | H3 | 2.4.2 | 2 | — | R-059 | URL autosufficiente con progetto e ricompensa; senza contesto spiegazione e link; titolo specifico | `donazione.html` | percorsi #8, #46 | risolto |
| P-062 | I metodi di pagamento cambiano da una pagina all'altra («carte di credito, PayPal, Satispay e bonifico» in… | LZ-CF:73; A1-P22 r23 (la proposta chiede «metodi di pagamento aggiornati»); `valutazione_antofallea.pdf` p. 28 | H4 | — | 2 | J04-F5 | R-055 | Metodi da un'unica fonte dati, con nomi comprensibili | `data/sito.json` | `dati.md`: metodi uguali in FAQ e donazione | risolto |
| P-063 | Le commissioni di pagamento sono a carico del donatore e, se la campagna fallisce, la donazione viene… | LZ-FAQ:74, :75, :84, :116 | H5 / H4 | — | 2 | J04-F5, J06-F3 | R-056 | Commissione stimata per metodo e totale nel riepilogo; destino in caso di rimborso | donazione passi 4–5, FAQ | percorsi #21–22 | risolto |
| P-064 | Non è chiaro se la donazione è detraibile né che ricevuta si ottiene | LZ-FAQ:139 | H10 | — | 2 | J06-F6 | R-057 | Riquadro «Ricevuta e detraibilità» nel modulo, nella conferma e nelle FAQ | donazione, conferma, FAQ | 08 J06-F6 | risolto |
| P-065 | La ricompensa a importo libero si chiama «FAI TU», un nome che non dice che è una donazione libera | AN-MC:60; A1-P08 r9 | H2 | — | 1 | J01-F5, J02-F4, J07-F5 (P11) | R-037 | «Donazione libera · da € 5» uguale in tutti i progetti | pagina progetto, donazione | `dati.md` | risolto |
| P-066 | La risposta FAQ sul pagamento rifiutato spiega i motivi ma non che cosa fare dopo (riprovare, altro… | LZ-FAQ:126 | H9 | — | 3 | — | R-062 | FAQ «Il pagamento non è andato a buon fine» con passi e contatto, collegata dal passo 4 | FAQ, donazione | `link.md` | risolto |
| P-067 | I consensi del modulo di registrazione sembrano caselle di spunta ma sono `button` senza ruolo né stato | GA s45; AL A-P04:138 | H1 | 1.3.1, 4.1.2 | 2 | J12-F4 | R-077, R-098 | Caselle di spunta native con etichetta | moduli | percorsi #50 | risolto |
| P-068 | Gergo non spiegato per i promotori | GA s46; LZ-CF:50, :51; LZ-FAQ:53 | H2 | 3.1.3 (AAA) | 2 | J09-F3, J12-F3 (P01) | R-083 | Lessico senza gergo; «Le parole di ideaBlume» nelle FAQ | `i18n/*.json`, `faq.html#parole` | `dati.md` | risolto |
| P-069 | Le pagine nominano il passo successivo senza link («Lancia una campagna», «iscriviti») | GA s47; LZ-CF:62, :63, :86, :139; LZ-FAQ:87, :142 | H3 | 2.4.4 | 2 | J06-F3, J09-F4, J12-F3 | R-015, R-081 | Ogni passo di «Come funziona» ha il link all'azione; rimandi tra FAQ e Come funziona | `come-funziona.html`, `faq.html` | `link.md` | risolto |
| P-070 | Lo stesso concetto ha nomi diversi | GA s48; LZ-CF:72, :76; LZ-FAQ:76, :85; A2-P07 r8 | H4 | 3.2.4 | 1 | J06-F3, J09-F3, J12-F3 | R-084 | Lessico unico controllato da script; importi in una sola forma | `i18n/*.json` | `dati.md`; residuo V-05 (gravità 1) | risolto |
| P-071 | La quota di 350 € + IVA per pubblicare compare una sola volta, in fondo a un paragrafo, a ~4.000 px, in… | GA s49; LZ-CF:74, :82, :84; A2-P15 r16; A2-P04 r5 | H5 / H8 | — | 4 | J09-F3, J12-F3 | R-075 | Riquadro «Quanto costa» per primo in «Proponi» e identico in Programma e Come funziona | `proponi.html`, `programma.html`, `come-funziona.html` | screenshot `proponi-1280` | risolto |
| P-072 | Il modulo di registrazione non usa i controlli del browser | GA s50; AL A-P05:148 | H5 | 1.3.5, 3.3.1 | 2 | J09-F5, J12-F4 | R-053, R-077 | Controlli nativi del browser e autocompletamento | candidatura, collaborazione, contatti | `axe.md`; percorsi #49 | risolto |
| P-073 | Nel modulo di registrazione le etichette sono solo segnaposto | GA s51; AL A-P03:123 | H6 | 1.3.1, 3.3.2, 4.1.2 | 3 | J09-F5, J12-F4 | R-077 | Etichette sempre visibili sopra i campi | tutti i moduli | `axe.md` (label) | risolto |
| P-074 | «Come funziona» è un testo continuo (5.763 px) senza titoli né indice | GA s52; A2-P14 r15; LZ-CF:41, :95, :96, :105, :115 | H7 | 1.1.1, 1.3.1, 2.4.6 | 3 | J01-F3, J07-F4, J09-F3 | R-081 | «Come funziona» con indice, titoli e passi numerati | `come-funziona.html` | screenshot | risolto |
| P-075 | Le 25 FAQ sono un'unica lista | GA s53; A1-P22 r23; LZ-FAQ:44, :63, :66, :86, :97, :98, :102; LZ-CF:52 | H7 / H10 | — | 3 | J06-F3, J09-F3, J12-F3 | R-081, R-082 | FAQ per destinatario e argomento, ricerca interna, accordion, ancore | `faq.html` | percorsi #38–39 | risolto |
| P-076 | In «Come funziona» alcuni paragrafi importanti, comprese le informazioni sui costi, hanno un corpo molto… | GA s54 | H8 | 1.4.12 (spaziatura), leggibilità | 4 | J01-F3, J09-F3, J12-F3 | R-075, R-099 | Corpo 18 px, mai sotto 16 px; costi in un riquadro evidente | CSS | `07_design_system.md` | risolto |
| P-077 | Il messaggio di errore resta visibile anche dopo aver corretto il campo, fino al nuovo invio | GA s55; AL A-P06:158 | H9 | 3.3.1 | 2 | J09-F5, J12-F4 | R-052, R-077 | L'errore sparisce appena il campo è valido | JS | percorsi #12, #51 | risolto |
| P-078 | Il pulsante «Lancia una campagna» porta alla registrazione generica, mentre il programma con l'Ateneo ha… | AN-PR:83; LZ-CF:75; A1-P20 r21 | H5 / H4 | — | 3 | J09-F2, J09-F4 | R-074 | «Candidati al programma» distinto da «Proponi una collaborazione»; nessuna registrazione generica | `proponi.html`, `programma.html` | 08 J09-F2, J09-F4 | risolto |
| P-079 | Mancano le informazioni per pianificare una candidatura | LZ-CF:83, :137, :138; LZ-FAQ:88 | H5 / H10 | — | 3 | — | R-078 | Fasi, durata delle campagne, tempi di risposta | `programma.html`, `proponi.html` | 08 | risolto |
| P-080 | Orari di contatto diversi tra «Come funziona» (9:30–16:30) e «Contatti» (9:30–13 e 14–16:30) | A2-P11 r12; LZ-CF:123; LZ-FAQ:127, :128 | H4 / H9 | 3.2.6 | 2 | J01-F6, J11-F6, J12-F5 | R-016, R-061, R-085 | Contatti, orari e tempi di risposta da un'unica fonte; blocco «Aiuto» uguale in ogni pagina | piè di pagina, `data/sito.json` | `dati.md` | risolto |
| P-081 | Il numero di telefono nel testo non è cliccabile (la mail sì) | LZ-CF:104 | H7 | — | 2 | — | R-085 | Telefono come link `tel:` | piè di pagina, contatti | `link.md` | risolto |
| P-082 | Risposte FAQ lunghe e senza struttura («muri di testo»), tono promozionale («idea geniale»), spiegazioni… | LZ-FAQ:54, :55, :103, :115, :141 | H8 / H2 | — | 3 | — | R-086, R-099 | Risposte che iniziano con la risposta in una frase, brevi | `faq.html` | revisione | risolto |
| P-083 | Refusi ed errori ortografici in pagine che parlano di soldi e fiducia («modalitè», «Si» senza accento,… | LZ-FAQ:78 | H4 | — | 2 | — | R-087 | Testi rivisti | `i18n/*.json` | revisione | risolto |
| P-084 | «Tasso di successo superiore al 90%, il più alto in Italia» senza fonte, periodo né metodo di calcolo | LZ-CF:53 | H2 | — | 1 | — | R-086 | Nessun dato senza fonte; numeri calcolati dai dati | tutte le pagine | `dati.md` | risolto |
| P-085 | Con il menu hamburger chiuso il focus passa su un link vuoto, sull'hamburger senza nome e sulle voci del… | AL A-P07:168 | H1 | 2.4.3, 2.4.7, 2.4.11 | 3 | J03-F6, J11-F5 | R-006, R-091 | Focus visibile di 3 px (17:1); voci del menu chiuso non focalizzabili | CSS, JS | percorsi #34; `tastiera-*.png` | risolto |
| P-086 | Controlli senza nome accessibile | AL A-P08:178; LZ-CF:125 | H6 | 4.1.2, 2.4.4 | 3 |  (P03) | R-010, R-098 | Tutti i controlli con nome accessibile | tutte le pagine | `axe.md` (button-name, link-name, label) | risolto |
| P-087 | Da smartphone nessuna pagina supera i Core Web Vitals (LCP 3,4 s contro 2,5 s | GA s72–s78; WCV (tutti gli 8 report; valori in `01_inventario_fonti.md` §3.1) | — (misura) | — | n.d. | J02-F2, J02-F5, J03-F6, J11-F3 | R-120, R-122, R-123 | Pagine leggere, nessuna risorsa esterna, SVG con dimensioni, nessuno spostamento del layout | tutto il sito | `prestazioni.md`: 100/100/100/100, LCP ≤ 1,9 s, CLS 0 | risolto |
| P-088 | Catalogo dei partner | A2-P08 r9; A2-P12 r13; A2-P13 r14 | H6 / H7 / H4 | — | 3 | — | R-005 | Il nuovo sito è dedicato a un solo ente (Università di Torino): non ha un catalogo di partner. Il principio sottostante (ogni sezione ha un indirizzo proprio, condivisibile) vale comunque ed è coperto dai requisiti sugli URL | — | — | non applicabile |
| P-089 | Le immagini di «Come funziona» sono caricate con indirizzi `http` invece di `https` | LZ-CF:77 | H4 | — | 1 | — | — | Riguarda l'infrastruttura del fornitore, non l'interazione. Nel prototipo tutte le risorse sono locali con URL relative | — | — | non applicabile |
| P-090 | Il metadato `twitter:site` indica `@nytimes` | LZ-CF:78 | H4 | — | 1 | — | — | Osservazione tecnica collaterale (la fonte stessa la definisce «da segnalare a parte»); il prototipo non pubblica metadati per i social | — | — | non applicabile |

## 2. Requisito → origine

Ogni requisito deriva da almeno un problema o da un bisogno di una persona (o da un vincolo della consegna).

| Requisito | Area | Priorità | Origine (problemi, bisogni, journey, vincoli) | Problemi collegati |
|---|---|---|---|---|
| R-001 | Navigazione e homepage | M | P-001, P-003; B01-1, B06-1, B07-1, B12-1; J01-F2, J06-F1, J07-F2, J12-F1 | P-001, P-003 |
| R-002 | Navigazione e homepage | M | P-004; J07-F2 | P-004 |
| R-003 | Navigazione e homepage | M | P-005; B07-2; J07-F3 | P-005 |
| R-004 | Navigazione e homepage | M | P-006 | P-006 |
| R-005 | Navigazione e homepage | M | P-007, P-008, P-088 (principio); B12-2; J12-F2 | P-007, P-008, P-088 |
| R-006 | Navigazione e homepage | M | P-008, P-085; B03-4, B11-3; J03-F4, J11-F5 | P-008, P-085 |
| R-007 | Navigazione e homepage | S | P-009 | P-009 |
| R-008 | Navigazione e homepage | M | P-010 | P-010 |
| R-009 | Navigazione e homepage | M | P-014; J01-F4, J04-F3, J08-F1, J09-F2 | P-014 |
| R-010 | Navigazione e homepage | M | P-011, P-086 | P-011, P-086 |
| R-011 | Navigazione e homepage | M | P-016 | P-016 |
| R-012 | Navigazione e homepage | S | P-015; J07-F4, J08-F2, J11-F5 | P-015 |
| R-013 | Navigazione e homepage | M | P-002; J01-F1 | P-002 |
| R-014 | Navigazione e homepage | M | P-019, P-020 | P-019, P-020 |
| R-015 | Navigazione e homepage | M | P-069; checklist di `Istruzioni.md` | P-069 |
| R-016 | Navigazione e homepage | S | P-003, P-080; J06-F1, J12-F2 | P-003, P-080 |
| R-017 | Navigazione e homepage | C | P-013; B08-1 | P-013 |
| R-020 | Elenco dei progetti | M | P-038, P-026, P-030, P-028; B05-2, B10-1; J05-F2, J10-F1 | P-026, P-028, P-030, P-038 |
| R-021 | Elenco dei progetti | M | P-022, P-024, P-028, P-040; B01-4, B05-1, B10-2; J01-F4, J05-F3, J10-F2 | P-022, P-024, P-028, P-040 |
| R-022 | Elenco dei progetti | M | P-023 | P-023 |
| R-023 | Elenco dei progetti | M | P-029; J03-F4 | P-029 |
| R-024 | Elenco dei progetti | M | P-031, P-027; B05-2, B05-3, B08-2; J05-F2, J08-F2 | P-027, P-031 |
| R-025 | Elenco dei progetti | M | P-032, P-033; J05-F2, J08-F2 | P-032, P-033 |
| R-026 | Elenco dei progetti | M | P-036, P-028; B06-2, B08-1; J06-F2, J08-F5 | P-028, P-036 |
| R-027 | Elenco dei progetti | M | P-028, P-050; J05-F1 | P-028, P-050 |
| R-028 | Elenco dei progetti | M | P-037; J02-F6, J07-F3, J11-F3 | P-037 |
| R-029 | Elenco dei progetti | S | P-048 | P-048 |
| R-030 | Pagina del progetto | M | P-022, P-023, P-024; B01-4, B05-4; J01-F4, J05-F3 | P-022, P-023, P-024 |
| R-031 | Pagina del progetto | M | P-050 | P-050 |
| R-032 | Pagina del progetto | M | P-041, P-045; B08-3; J08-F3 | P-041, P-045 |
| R-033 | Pagina del progetto | M | P-049; B02-2, B07-3; J02-F3, J07-F4 | P-049 |
| R-034 | Pagina del progetto | M | P-048, P-053; B05-5, B10-2, B10-3; J05-F4, J10-F2, J10-F3 | P-048, P-053 |
| R-035 | Pagina del progetto | M | P-044, P-054; J04-F3, J06-F5 | P-044, P-054 |
| R-036 | Pagina del progetto | M | P-042, P-045; B02-3; J02-F4, J04-F4 | P-042, P-045 |
| R-037 | Pagina del progetto | M | P-065; B01-5, B02-3, B07-4; J01-F5, J02-F4, J07-F5 | P-065 |
| R-038 | Pagina del progetto | M | P-040; B03-3, B10-5; J03-F3, J05-F3, J10-F5 | P-040 |
| R-039 | Pagina del progetto | M | P-039; B10-4; J02-F3, J08-F4, J10-F4 | P-039 |
| R-040 | Pagina del progetto | M | P-046, P-012; J03-F2 | P-012, P-046 |
| R-041 | Pagina del progetto | M | P-044; J03-F2, J11-F5 | P-044 |
| R-042 | Pagina del progetto | S | P-052 | P-052 |
| R-043 | Pagina del progetto | M | P-026; B06-2, B10-1; J06-F2, J08-F3 | P-026 |
| R-044 | Pagina del progetto | S | S27 (positivo da conservare); B04-6, B07-5 | — (bisogno di persona o vincolo) |
| R-045 | Pagina del progetto | C | B10-6; J10-F6 | — (bisogno di persona o vincolo) |
| R-050 | Donazione (checkout simulato) | M | P-057; J01-F5, J02-F5 | P-057 |
| R-051 | Donazione (checkout simulato) | M | P-058; B02-4; J02-F5, J02-F6 | P-058 |
| R-052 | Donazione (checkout simulato) | M | P-054, P-077; B01-6, B03-5, B04-1, B07-4, B11-2; J01-F5, J03-F5, J04-F5, J07-F5, J11-F4 | P-054, P-077 |
| R-053 | Donazione (checkout simulato) | M | P-059, P-060, P-072; B09-6 | P-059, P-060, P-072 |
| R-054 | Donazione (checkout simulato) | M | P-055, P-056; B06-4; J06-F5 | P-055, P-056 |
| R-055 | Donazione (checkout simulato) | M | P-062; B04-4; J04-F5 | P-062 |
| R-056 | Donazione (checkout simulato) | M | P-063; B04-3, B06-3; J04-F5, J06-F3 | P-063 |
| R-057 | Donazione (checkout simulato) | M | P-064; B06-5; J06-F6 | P-064 |
| R-058 | Donazione (checkout simulato) | M | Obiettivo (prototipo didattico) | — (bisogno di persona o vincolo) |
| R-059 | Donazione (checkout simulato) | M | P-061, P-040 | P-040, P-061 |
| R-060 | Donazione (checkout simulato) | M | P-057; J02-F5 | P-057 |
| R-061 | Donazione (checkout simulato) | S | J01-F6; B01-6; P-080 | P-080 |
| R-062 | Donazione (checkout simulato) | S | P-066 | P-066 |
| R-070 | Programma con l'Ateneo e percorso di chi propone un progetto | M | P-021; B06-2, B08-1, B09-1; J06-F2, J08-F1, J08-F6, J09-F1 | P-021 |
| R-071 | Programma con l'Ateneo e percorso di chi propone un progetto | M | P-035; B09-2, B12-3; J06-F2, J08-F4, J09-F2, J12-F3 | P-035 |
| R-072 | Programma con l'Ateneo e percorso di chi propone un progetto | M | P-048, P-053; B10-3; J10-F3 | P-048, P-053 |
| R-073 | Programma con l'Ateneo e percorso di chi propone un progetto | M | P-036; J08-F5 | P-036 |
| R-074 | Programma con l'Ateneo e percorso di chi propone un progetto | M | P-078; B09-2; J09-F2, J09-F4 | P-078 |
| R-075 | Programma con l'Ateneo e percorso di chi propone un progetto | M | P-071, P-076; B09-3, B12-3; J09-F3, J12-F3 | P-071, P-076 |
| R-076 | Programma con l'Ateneo e percorso di chi propone un progetto | M | B12-3, B12-4; J12-F3, J12-F4, J12-F5 (P12) | — (bisogno di persona o vincolo) |
| R-077 | Programma con l'Ateneo e percorso di chi propone un progetto | M | P-067, P-072, P-073, P-077; B09-6, B12-4; J09-F5, J12-F4 | P-067, P-072, P-073, P-077 |
| R-078 | Programma con l'Ateneo e percorso di chi propone un progetto | S | P-079 | P-079 |
| R-079 | Programma con l'Ateneo e percorso di chi propone un progetto | C | B11-5; J11-F1, J11-F6 (P11) | — (bisogno di persona o vincolo) |
| R-080w | Programma con l'Ateneo e percorso di chi propone un progetto | W | `Istruzioni.md` §4 («non sono richiesti account reali»); `da_rivedere_P10-P12.md` §2.3 | — (bisogno di persona o vincolo) |
| R-081 | Aiuto, contenuti e contatti | M | P-074, P-069, P-075; B01-3, B09-4, B09-5; J01-F3, J09-F3, J09-F4 | P-069, P-074, P-075 |
| R-082 | Aiuto, contenuti e contatti | M | P-075; B06-3, B09-4, B12-3; J06-F3, J09-F3, J12-F3 | P-075 |
| R-083 | Aiuto, contenuti e contatti | M | P-025, P-068; B01-3, B04-3; J01-F3, J04-F2, J09-F3 | P-025, P-068 |
| R-084 | Aiuto, contenuti e contatti | M | P-070, P-048; B06-3, B09-3 | P-048, P-070 |
| R-085 | Aiuto, contenuti e contatti | M | P-080, P-081; B01-6, B06-6; J01-F6, J11-F6, J12-F5 | P-080, P-081 |
| R-086 | Aiuto, contenuti e contatti | S | P-082, P-084; B07-3 | P-082, P-084 |
| R-087 | Aiuto, contenuti e contatti | S | P-083 | P-083 |
| R-088 | Aiuto, contenuti e contatti | M | P-003; B06-1, B12-1 | P-003 |
| R-089 | Aiuto, contenuti e contatti | C | P-013 | P-013 |
| R-090 | Accessibilità trasversale (obiettivo WCAG 2.2 AA) | M | P-017, P-046; B03-1 | P-017, P-046 |
| R-091 | Accessibilità trasversale (obiettivo WCAG 2.2 AA) | M | P-085; B03-4, B11-3; J03-F4, J11-F5 | P-085 |
| R-092 | Accessibilità trasversale (obiettivo WCAG 2.2 AA) | M | P-034; B01-2; J01-F2, J05-F1 | P-034 |
| R-093 | Accessibilità trasversale (obiettivo WCAG 2.2 AA) | M | P-022, P-028, P-040; B05-1; J05-F1, J05-F3 | P-022, P-028, P-040 |
| R-094 | Accessibilità trasversale (obiettivo WCAG 2.2 AA) | M | P-019; B01-2 | P-019 |
| R-095 | Accessibilità trasversale (obiettivo WCAG 2.2 AA) | M | B01-2, B12-2 (P01, P12) | — (bisogno di persona o vincolo) |
| R-096 | Accessibilità trasversale (obiettivo WCAG 2.2 AA) | M | P-039, P-054, P-006 | P-006, P-039, P-054 |
| R-097 | Accessibilità trasversale (obiettivo WCAG 2.2 AA) | M | P-037 | P-037 |
| R-098 | Accessibilità trasversale (obiettivo WCAG 2.2 AA) | M | P-086, P-012, P-067, P-060 | P-012, P-060, P-067, P-086 |
| R-099 | Accessibilità trasversale (obiettivo WCAG 2.2 AA) | S | P-076, P-082; B01-2, B07-3 (P01, P07, P04) | P-076, P-082 |
| R-100 | Accessibilità trasversale (obiettivo WCAG 2.2 AA) | S | J03-F6, J11-F6 | — (bisogno di persona o vincolo) |
| R-110 | Multilingua | M | P-043, P-054; B04-1, B11-1; J04-F2, J04-F5, J11-F2, J11-F4 | P-043, P-054 |
| R-111 | Multilingua | M | P-051, P-047; B04-2; J04-F4 | P-047, P-051 |
| R-112 | Multilingua | M | J04-F6, J11-F2; B04-6 | — (bisogno di persona o vincolo) |
| R-113 | Multilingua | M | P-051 (frasi inglesi senza `lang`) | P-051 |
| R-120 | Mobile e prestazioni | M | `Istruzioni.md` §4 (versione desktop richiesta); checkpoint 1 (responsive su mobile e desktop); P-087, P-037 | P-037, P-087 |
| R-121 | Mobile e prestazioni | M | P-018 | P-018 |
| R-122 | Mobile e prestazioni | M | P-087; B02-1, B11-4; J02-F2, J11-F3 | P-087 |
| R-123 | Mobile e prestazioni | M | P-087 | P-087 |
| R-130 | Vincoli di consegna, dati e onestà del prototipo | M | `Istruzioni.md` §7 B («non devono essere richiesti server»); checkpoint 1 (D-21) | — (bisogno di persona o vincolo) |
| R-131 | Vincoli di consegna, dati e onestà del prototipo | M | P-036, P-023 | P-023, P-036 |
| R-132 | Vincoli di consegna, dati e onestà del prototipo | M | Regole generali del prompt; regola 4 di C00 (non inventare dati presentati come reali) | — (bisogno di persona o vincolo) |
| R-133 | Vincoli di consegna, dati e onestà del prototipo | M | `Istruzioni.md` §4; checkpoint 1 (D-23) | — (bisogno di persona o vincolo) |
| R-134 | Vincoli di consegna, dati e onestà del prototipo | M | Obiettivo del prompt; `Istruzioni.md` §4 | — (bisogno di persona o vincolo) |
| R-135 | Vincoli di consegna, dati e onestà del prototipo | M | Vincolo di stack del prompt | — (bisogno di persona o vincolo) |
| R-136 | Vincoli di consegna, dati e onestà del prototipo | M | Regola 4 del prompt | — (bisogno di persona o vincolo) |

## 3. Matrice personas × aree del sito

Soluzioni del sito che rispondono ai bisogni di ciascuna persona (dettaglio e prove in `08_verifica_personas.md`).

| Persona | Navigazione e home | Elenco | Pagina progetto | Donazione | Programma e promotori | Aiuto | Accessibilità | Multilingua | Mobile e prestazioni |
|---|---|---|---|---|---|---|---|---|---|
| P01 | Frase iniziale, testo 18 px, bersagli 44 px | Stato in testo, mai giorni negativi | Riquadro di stato, «Donazione libera · da € 5» | Errori in linea, riepilogo, conferma con codice | — | Parole spiegate nelle FAQ, telefono nel piè di pagina | Contrasti, zoom 200% | — | — |
| P02 | Ricerca in home e nei filtri di Progetti | Griglia senza caroselli | Stato e «Sostieni» sotto il titolo, indice, «Scrivi al gruppo» | Dati salvati, validazione in linea | — | — | Bersagli ampi | — | Lighthouse mobile 100, 97 KB |
| P03 | «Salta al contenuto», menu con Esc | Card con un solo link | Spiegazioni come pulsanti, campagne concluse senza controlli | Riepilogo errori con focus | — | FAQ con `details` | axe 0 violazioni, dichiarazione di accessibilità | `lang` sui commenti | — |
| P04 | Selettore di lingua | — | Ricompense in una lingua | Errori in inglese, commissioni nel riepilogo | — | FAQ e parole in inglese | — | 25 pagine inglesi complete | — |
| P05 | — | Filtri, ordinamento «Più lontani dall'obiettivo», posizione conservata | Raddoppio accanto a «Sostieni», secondo obiettivo | — | Numeri delle edizioni | — | Stato con testo e icona (deuteranopia) | — | — |
| P06 | «Chi siamo» nel menu e nella prima frase | Contatori coerenti | Gruppo e responsabile, uso dei fondi | Anonimato esplicito, ricevuta, rimborso | Stato del programma con date | FAQ per destinatario, «Quanto costa» | — | — | — |
| P07 | Progetti nella prima schermata, ricerca | Titoli interi | Indice, paragrafi brevi | Minimo accanto al campo | — | — | Corpo 18 px | — | Mobile 375 px |
| P08 | Aggiornamenti datati | Filtro per anno, URL condivisibili, fine elenco | Ordine fisso delle sezioni, resoconti | — | Tabella delle edizioni con data | — | — | — | — |
| P09 | — | — | — | — | Requisiti, «Candidati al programma», modulo con etichette | «Come funziona» per passi, FAQ promotori | Caselle native | — | — |
| P10 | — | Card con gruppo e dipartimento | Badge «obiettivo raggiunto · raccolta aperta», secondo obiettivo, «Scrivi al gruppo» | — | Regola del raddoppio oltre l'obiettivo | Indicazioni per i gruppi | Cifre a 32 px | — | — |
| P11 | Menu con Esc | — | Barra non cliccabile, feedback immediato | Errori in inglese | — | «Contenuti in due lingue», «Problema del sito» | Focus visibile | Inglese completo | Mobile veloce |
| P12 | Frase iniziale, menu con voci da 48 px | Progetto d'esempio con il territorio | — | — | «Sei un ente esterno?», «Proponi una collaborazione», «Quanto costa» | FAQ «Siamo un'associazione…» | Bersagli ≥ 24 px, campi da 44 px | — | — |

## 4. Sintesi della copertura

| Gravità | Problemi | Risolti | Parziali | Non risolti | Non applicabili |
|---|---|---|---|---|---|
| 4 | 9 | 9 | 0 | 0 | 0 |
| 3 | 30 | 29 | 0 | 0 | 1 |
| 2 | 33 | 33 | 0 | 0 | 0 |
| 1 | 15 | 13 | 0 | 0 | 2 |
| n.d. | 3 | 3 | 0 | 0 | 0 |
| **Totale** | **90** | **87** | **0** | **0** | **3** |

- **Parziali**: nessuno.
- **Non applicabili** (P-088, P-089, P-090): catalogo dei partner (il sito ha un solo ente), risorse `http` e metadato social del fornitore; motivazioni nella tabella 1.
- **Non risolti**: nessuno.
- Problemi coperti da almeno un requisito: 88 su 90; senza requisito: P-089, P-090 (non applicabili).
- Requisiti: 102, tutti con un'origine documentata (tabella 2).
- Residui emersi dalla valutazione euristica del nuovo sito (`09_valutazione_euristica.md`): nessun problema di gravità 3 o 4; un problema di gravità 2 aperto (V-03, ripresa della donazione su un altro dispositivo).
