# 02 · Problemi consolidati di assignment1

Tutti i problemi rilevati in assignment1 su IdeaGinger × Università di Torino, **deduplicati**: quando più componenti del gruppo hanno rilevato lo stesso problema, compare una sola riga che cita tutte le fonti. Ogni problema delle fonti compare in una riga; quelli scartati o non applicabili sono nell'area J con il motivo.

## Come leggere la tabella

**Sigle delle fonti** (percorsi relativi alla radice del repository):

| Sigla | File | Come si cita |
|---|---|---|
| GA | `assignment1/assignment1_gruppoA.pdf` (presentazione di gruppo, 82 slide) | `GA s23` = slide 23 |
| A1 | `assignment1/parti/antofallea/problemi_antofallea.csv` (= `valutazione_antofallea.pdf`) | `A1-P07 r8` = ID P07, riga 8 del CSV |
| A2 | `assignment1/parti/antofallea2/problemi_antofallea2.csv` (= `valutazione_antofallea2.pdf`) | `A2-P11 r12` |
| AL | `assignment1/alex/README.md` | `AL A-P07:168` = problema A-P07, riga 168 |
| AN-PR | `assignment1/parti/andre/Pagina_Progetti.md` | `AN-PR:66` = riga 66 |
| AN-MC | `assignment1/parti/andre/Pagina_MindTheClimate.md` | `AN-MC:93` |
| LZ-CF | `assignment1/lorenzo/Pagina_ComeFunziona.md` | `LZ-CF:82` |
| LZ-FAQ | `assignment1/lorenzo/Pagina_FAQ.md` | `LZ-FAQ:63` |
| WCV | `assignment1/web_core_vitals/*.png` | nome del file |
| C00 | `assignment2/00_contesto_comune_C00.md`, catalogo | chiave `Sxx` / `Xxx` |

**Euristiche**: H1–H10 di Nielsen (H1 visibilità dello stato, H2 corrispondenza con il mondo reale, H3 controllo e libertà, H4 coerenza e standard, H5 prevenzione degli errori, H6 riconoscimento anziché ricordo, H7 flessibilità ed efficienza, H8 design estetico e minimalista, H9 riconoscere e correggere gli errori, H10 aiuto e documentazione). LG1–LG10 sono le linee guida NN/g per la homepage usate in GA s57–s68.

**Gravità**: scala 0–4 usata nelle fonti. Le scale non sono identiche: in GA (s3) 3 = «importante» e 4 = «grave»; in AL 3 = «grave» e 4 = «critico». andre usa in alcuni punti il valore **5**, fuori scala: è riportato come «5 (fuori scala)» e non entra nel valore consolidato. Il segno «?» indica un valore provvisorio nella fonte.

**Gravità consolidata** (colonna «G»): il valore di GA quando il problema è in una slide (è la valutazione concordata dal gruppo); altrimenti il massimo dei valori validi delle fonti. Quando le fonti divergono, la colonna «Gravità nelle fonti» le riporta tutte. «n.d.» = la fonte non assegna una gravità.

**WCAG**: criterio WCAG 2.2 pertinente, indicato da chi scrive questo documento quando la fonte non lo cita (le fonti lo citano solo in AL e in parte in LZ). AA salvo indicazione.

---

## A · Homepage, navigazione e orientamento

| ID | Descrizione | Pagina valutata | Euristica | WCAG | G | Gravità nelle fonti | Fonti | C00 |
|---|---|---|---|---|---|---|---|---|
| P-001 | Nella parte alta non c'è una frase che dica che cos'è il servizio (homepage) o il programma (pagina partner UniTo, scheda Progetti): il nuovo visitatore non capisce dove si trova | Homepage; Partner UniTo › Partnership e Progetti | LG1 / H8 | — | 4 | 4 (GA); 1 (A1-P16); 1 (AN-PR) | GA s59; A1-P16 r17; AN-PR:57 | S59 |
| P-002 | Titolo della finestra lungo (83 caratteri, troncato su Google), marchio con nomi diversi («GINGER», «Idea Ginger», «ideaginger.it»); «Servizi», «Collaborazioni» e FAQ hanno lo stesso titolo della home | Homepage, Servizi, Collaborazioni, FAQ | LG2 / H1 / H4 | 2.4.2 | 1 | 1 (GA); 1 (A2-P03); 2? (LZ-FAQ:43); 1 (LZ-FAQ:77) | GA s60; A2-P03 r4; LZ-FAQ:43, :77 | S60 |
| P-003 | «Chi siamo» è solo nel footer: non si capisce chi gestisce il servizio | Homepage | LG3 | — | 3 | 3 (GA) | GA s61 | S61 |
| P-004 | Nella prima schermata i servizi per chi lancia campagne (academy, podcast, campaign manager, blog) vengono prima dei progetti da sostenere | Homepage | LG4 | — | 2 | 2 (GA) | GA s62 | S62 |
| P-005 | Nessun campo di ricerca visibile: «Cerca progetti» apre un elenco di categorie | Homepage, menu | LG5 / H7 | — | 1 | 1 (GA) | GA s63 | S63 |
| P-006 | La ricerca senza risultati mostra una pagina vuota, senza messaggio né suggerimenti; il nome dell'iniziativa («funds together») non dà risultati | Ricerca progetti | H9 | 4.1.3 | 3 | 3 (A1); 5 (fuori scala, AN-PR) | A1-P18 r19; AN-PR:119 | — |
| P-007 | Per ritrovare il programma bisogna ricordare che UniTo è un «Partner» e cercarlo tra 25 nomi in ordine non alfabetico; il nome dell'iniziativa non compare in nessun menu | Menu «Partner» | H6 | — | 2 | 2 (A1) | A1-P12 r13 | — |
| P-008 | Menu e tendine con oltre 70 voci; il pannello «Partner» continua oltre lo schermo senza segnale; da tastiera le tendine non si chiudono con Esc e il pannello si chiude solo con una X senza etichetta | Homepage, menu globale | LG9 / H3 / H1 | 2.1.1, 1.4.13 | 2 | 2 (GA); 2 (A2-P01); 1 (A2-P06) | GA s67; A2-P01 r2; A2-P06 r7 | S67 |
| P-009 | Né la barra né il menu indicano la sezione in cui ci si trova | Menu, pagine partner | H1 | 2.4.8 (AAA) | 2 | 2 (A2) | A2-P02 r3 | — |
| P-010 | Una piccola icona «casa» senza etichetta duplica il logo che porta alla home | Menu principale | H6 | 1.1.1, 2.4.4 | 1 | 1 (GA); 2 (AN-PR) | GA s19; AN-PR:94 | S19 |
| P-011 | Link con testo generico ripetuto: «Vai alla pagina» 25 volte; tre link «qui» verso destinazioni diverse; l'invito «Scopri i servizi aggiuntivi!» non è un link | Homepage (partner), Come funziona | LG7 / H4 | 2.4.4 | 2 | 2 (GA); 2 (A2-P10); 2? (LZ-CF) | GA s65; A2-P10 r11; LZ-CF:136 | S65 |
| P-012 | Il testo alternativo delle icone delle categorie ripete l'etichetta accanto: lo screen reader la legge due volte | Homepage | LG10 | 1.1.1 | 1 | 1 (GA) | GA s68 | S68 |
| P-013 | Il blog in homepage è solo un invito, senza articoli né date; la FAQ non ha una data di ultimo aggiornamento | Homepage, FAQ | LG8 / H10 | — | 1 | 1 (GA); 2 (LZ-FAQ:140) | GA s66; LZ-FAQ:140 | S66 |
| P-014 | Link interni aperti in una nuova scheda («Scopri tutti i progetti!»: il tasto Indietro non funziona); link esterni (unito.it, gingeracademy.it, PayPal, social, Condizioni d'uso, versione inglese di VIBE) senza avviso | Partner UniTo, Servizi, pagine progetto, registrazione, FAQ | H3 | 3.2.5 (AAA, buona pratica) | 3 | 3 (GA); 2 (A1-P07); 2 (A2-P05); 2 (AL R-P07); 1? (LZ-FAQ:64) | GA s14; A1-P07 r8; A2-P05 r6; AL R-P07:208; LZ-FAQ:64 | S14 |
| P-015 | Nelle pagine lunghe manca un pulsante «Torna su» | Partner UniTo › Progetti, pagine progetto | H7 | — | 3 | 3 (GA); 3 (AN-MC:74) | GA s20, s38; AN-MC:74 | S20 |
| P-016 | Nelle pagine informative manca il breadcrumb | Come funziona, FAQ | H3 | 2.4.8 (AAA) | 1 | 1 (LZ-CF); 1 (LZ-FAQ) | LZ-CF:64; LZ-FAQ:65 | — |
| P-017 | Manca un link «Salta al contenuto»: con Tab si attraversano barra, menu e 26 categorie prima di arrivare al contenuto | FAQ (verificato), Come funziona (stesso template) | H7 | 2.4.1 | 3 | 3? (LZ-FAQ:105); 3? (LZ-CF:106) | LZ-FAQ:105; LZ-CF:106 | — |
| P-018 | Su smartphone una colonna di nove link (condizioni, privacy, cookie…) precede il contenuto | Come funziona, Collaborazioni (mobile) | H8 | — | 1 | 1 (A2) | A2-P16 r17 | — |
| P-019 | La pagina 404 è fuori dal modello del sito (niente logo, menu, ricerca, footer) e non ha il meta viewport: su smartphone il testo è minuscolo | Pagina 404 | H4 | 1.4.10 | 2 | 2 (A1) | A1-P10 r11 | — |
| P-020 | Il messaggio 404 è in inglese in un sito italiano, con refusi («Opps!», «adress»), e offre solo il ritorno alla home | Pagina 404 (raggiunta con un indirizzo digitato male, es. `/faqs.html`) | H9 | 3.1.1 | 2 | 2 (A1); 1 (AN-PR); 1–2? (LZ-CF); 1–2? (LZ-FAQ) | A1-P19 r20; AN-PR:117; LZ-CF:126; LZ-FAQ:130; `assignment1/lorenzo/screen_faq/cmf_e9_404.png` | — |

## B · Elenco dei progetti e pagina del programma

| ID | Descrizione | Pagina valutata | Euristica | WCAG | G | Gravità nelle fonti | Fonti | C00 |
|---|---|---|---|---|---|---|---|---|
| P-021 | Non si capisce se il programma è attivo: la pagina usa il futuro («verranno selezionati»), non ha date di candidatura né di campagna, il blog collegato propone articoli del 2021–2022 | Partner UniTo › Partnership e Progetti | H1 | — | 3 | 3 (GA); 3 (A1) | GA s9; A1-P01 r2 | S09 |
| P-022 | Le campagne in corso oltre il 100% (MILK-ACT 181%, RePatch 109%) non hanno l'etichetta «obiettivo raggiunto»: lo stato è affidato al colore; il donatore non capisce se la sua donazione serve ancora | Partner UniTo › Progetti | H1 | 1.4.1 | 3 | 3 (GA); 4 (AN-PR) | GA s10; AN-PR:46 | S10 |
| P-023 | Stato contraddittorio: VIBE mostra 64% e «€ 2.995 su € 4.700» e subito sotto l'etichetta «obiettivo raggiunto» | Progetto VIBE | H1 | — | 3 | 3 (AL) | AL A-P01:68 | — (vicino a S10) |
| P-024 | I giorni rimanenti sono scritti come numero negativo («-36 giorni»): la campagna sembra scaduta | Partner UniTo › Progetti, ricerca, MILK-ACT, Mind the Climate, VIBE | H2 | — | 2 | 2 (GA); 2 (A1); 2 (AN-PR); 2 (AN-MC); 2 (AL) | GA s11; A1-P04 r5; AN-PR:45; AN-MC:48; AL R-P04:83 | S11 |
| P-025 | Termini inglesi e gergo non spiegati: «Overfunding», «100% SUCCESSO», «369% OVERFUNDING», «by», «Partnership», «Checkout», «Notes backer», «i gloriosi GINGERs», «FAI TU», «co-design»; traduzione incompleta con testi italiani e inglesi uno sotto l'altro | Partner UniTo, checkout, Mind the Climate | H2 | 3.1.3 (AAA) | 2 | 2 (GA); 1 (A1-P06); 2 (AN-PR); 1 (AN-MC) | GA s12; A1-P06 r7; AN-PR:56; AN-MC:60 | S12 |
| P-026 | I nomi dei promotori nelle card sono eterogenei («by Departments & Dragons», «by Team GaIA»): non si capisce che sono gruppi di ricerca UniTo; nella pagina Progetti non c'è un riferimento chiaro all'Ateneo | Partner UniTo › Progetti | H2 / H6 | — | 2 | 2 (GA); 2 (AN-PR:58); 2 (AN-PR:92) | GA s13; AN-PR:58, :92 | S13 |
| P-027 | Tornando da un progetto con Indietro la pagina riparte dall'inizio e i progetti caricati con «Altri» spariscono | Partner UniTo › Progetti | H3 | — | 4 | 4 (GA); 4 (AN-PR) | GA s15; AN-PR:66 | S15 |
| P-028 | Barre di avanzamento poco chiare (blu e rosso); il contatore «18 progetti» non distingue attive e concluse; il chip «Obiettivo raggiunto» c'è solo sulle concluse; le card concluse si riconoscono solo dal titolo di sezione; i contatori sono ripetuti in due schede | Partner UniTo › Progetti e Partnership | H4 | 1.4.1 | 2 | 2 (GA); 3 (AN-PR:75); 2 (AN-PR:111) | GA s16; AN-PR:75, :111 | S16 |
| P-029 | Al passaggio del mouse le card non sembrano cliccabili; non hanno un nome accessibile per lo screen reader | Partner UniTo › Progetti | H4 | 2.4.4, 4.1.2 | 4 | 4 (GA); 3 (AN-PR) | GA s17; AN-PR:77 | S17 |
| P-030 | Le card non indicano tema o categoria: per scegliere bisogna aprire ogni progetto | Partner UniTo › Progetti | H6 | — | 2 | 2 (GA); 3 (AN-PR) | GA s18; AN-PR:93 | S18 |
| P-031 | Nessun filtro (categoria, obiettivo ONU, edizione) né ordinamento (scadenza); nessuna vista per sottocategoria dei progetti UniTo | Partner UniTo › Progetti | H7 | — | 3 | 3 (GA); 2 (A1-P14); 3 (AN-PR:67); 3 (AN-PR:98) | GA s21; A1-P14 r15; AN-PR:67, :98 | S21 |
| P-032 | «Altri» carica quattro progetti alla volta e non dice quanti ne restano (13 conclusi, se ne vedono 4) | Partner UniTo › Progetti | H7 | — | 3 | 3 (GA); 2 (A1-P14); 5 (fuori scala, AN-PR:99) | GA s22; A1-P14 r15; AN-PR:99 | S22 |
| P-033 | A fine elenco «Altri» scompare senza dire che i progetti sono finiti | Partner UniTo › Progetti | H9 | — | 2 | 2 (GA, intestazione) / 1 (GA, testo); 2 (AN-PR) | GA s24; AN-PR:116 | S24 |
| P-034 | Contrasto insufficiente: titoli arancioni ~2,5:1 (`#F28C00` 2,46:1), pulsanti verdi con testo bianco (`#00D018` 2,09:1), «Altri» 2,09:1, grigio `#999999` 2,85:1 (2,43:1 su `#EDEDED`), chip «Obiettivo raggiunto!» 3,5:1 con testo piccolo, footer ~2:1 con titoli piccoli, 14 nomi di partner su 25 sotto 4,5:1, testo bianco su arancione in «Servizi» | Partner UniTo, pagine progetto, checkout, registrazione, menu Partner, Servizi | H8 (GA) / H6 (AL) / H4 (A2) | 1.4.3, 1.4.11 | 4 | 4 (GA); 4 (AN-PR); 3 (AL); 2 (A2) | GA s23; AN-PR:112; AN-MC:124; AL A-P10:198; A2-P09 r10 | S23 |
| P-035 | La pagina del programma non dice chi può candidarsi, entro quando, con quale modulo né chi contattare; nessun contatto UniTo nella pagina; l'unico rimando è una guida su unito.it | Partner UniTo › Partnership; «Lancia una campagna»; Come funziona e FAQ | H10 | — | 2 | 2 (GA); 3 (A1-P20); 2 (AN-PR:127) | GA s25; A1-P20 r21; AN-PR:127 | S25 |
| P-036 | Numeri complessivi del programma incoerenti: la pagina dichiara 18 progetti, ma nella sezione precedente parla di 13 progetti delle edizioni precedenti | Partner UniTo › Progetti e Partnership | H4 | — | 2 | 2 (AN-PR) | AN-PR:74 | X06 |
| P-037 | Su smartphone i caroselli di contatori e progetti scorrono di lato senza frecce né pallini (si vedono 2 contatori su 5 e 2 progetti per fila); «Altri» aggiunge una nuova fila con un altro «Altri» invece di allungare quella esistente | Partner UniTo (mobile) | — (mobile) / H4 | — | 3 | 3 (GA); 5 (fuori scala, AN-PR:78); 2 (AN-PR:79) | GA s71; AN-PR:78, :79 | S71 |
| P-038 | I titoli dei progetti nelle card sono troncati («RePatch \| il cerotto per il cuore …») e la parte tagliata è spesso quella che dice di cosa parla; la sezione dei progetti conclusi si chiama «Per ispirarti» | Homepage, Partner UniTo › Progetti, ricerca | LG6 / H6 | — | 3 | 3 (GA); 1 (A1) | GA s64; A1-P13 r14 | S64 |

## C · Pagina del progetto

| ID | Descrizione | Pagina valutata | Euristica | WCAG | G | Gravità nelle fonti | Fonti | C00 |
|---|---|---|---|---|---|---|---|---|
| P-039 | «Contatta il progettista» mostra i contatti dopo diversi secondi senza indicatore di caricamento: sembra non aver preso il clic | Mind the Climate | H1 | 4.1.3 | 3 | 3 (GA); 3 (AN-MC) | GA s28; AN-MC:50 | S28 |
| P-040 | Sulle campagne concluse resta il box «SOSTIENI» con ricompense e prezzi, il campo «FAI TU» è ancora scrivibile e focalizzabile, lo stato è un pallino rosso senza legenda | BRIGHT, Fai Brillare la Ricerca!, MatematIcA | H1 | 1.4.1 | 3 | 3 (GA); 3 (A1); 3 (AL) | GA s29; A1-P02 r3; AL R-P02:93 | S29 |
| P-041 | Gli aggiornamenti («Nuovo obiettivo», «Secondo obiettivo») vengono prima della presentazione del progetto, che inizia ~3.700 px più in basso | BRIGHT | H2 | — | 2 | 2 (GA); 2 (A1) | GA s30; A1-P05 r6 | S30 |
| P-042 | Le 10 ricompense sono un lungo elenco verticale (immagine, testo bilingue, contatori) non comprimibile né confrontabile | Pagine progetto | H3 | — | 3 | 3 (GA); 3 (AN-MC) | GA s31; AN-MC:73 | S31 |
| P-043 | La versione inglese è parziale: cambia solo la panoramica, il resto resta in italiano con testi sovrapposti; mancano «tutto o niente» e obiettivi di sostenibilità; la scheda News porta alla versione inglese | Mind the Climate, MILK-ACT, VIBE | H4 | 3.1.1, 3.1.2 | 4 | 4 (GA); 3 (AN-MC:61); 5 (fuori scala, AN-MC:83) | GA s32; AN-MC:61, :83 | S32 |
| P-044 | Le spiegazioni a comparsa («O tutto o niente!», obiettivi di sostenibilità) sembrano link e puntano a «#»; la regola che decide il rimborso è spiegata solo lì, al futuro anche a campagna chiusa; il «perché» del tutto o niente è rimandato a un contatto | Mind the Climate, BRIGHT, Fai Brillare la Ricerca!, MILK-ACT; Come funziona | H4 / H10 | 1.4.13, 4.1.2 | 1 | 1 (GA); 2 (A1-P21); 2 (LZ-CF) | GA s33; A1-P21 r22; AN-MC:86; LZ-CF:85 | S33 |
| P-045 | Le ricompense più alte non mostrano quante persone le hanno scelte; ordine di ricompense e sezioni diverso da progetto a progetto; l'uso dei fondi non ha una collocazione fissa ed è a volte un grafico in immagine | Mind the Climate, BRIGHT, Fai Brillare la Ricerca! | H4 | 1.1.1 (budget in immagine) | 1 | 1 (GA); 1 (AN-MC); 2 (A1-P09) | GA s34; AN-MC:82; A1-P09 r10 | S34 |
| P-046 | Immagini informative senza testo alternativo, titoli vuoti, `h4` usati per impaginare immagini, salti di livello, due `h1` (registrazione) o nessuno (checkout), titoli `h3` prima dell'`h1` nella FAQ | MatematIcA, VIBE, registrazione, checkout, FAQ | H4 | 1.1.1, 1.3.1, 2.4.6 | 3 | 3 (GA); 3 (AL); 2? (LZ-FAQ) | GA s35; AL A-P09:188; LZ-FAQ:79 | S35 |
| P-047 | Nel box «SOSTIENI» italiano e inglese sono disposti in modo diverso in ogni progetto | Mind the Climate, MatematIcA | H4 | — | 2 | 2 (GA) | GA s36 | S36 |
| P-048 | Il cofinanziamento dell'Ateneo (raddoppio a obiettivo raggiunto) non è mostrato dove si dona; raddoppio, soglie e uso dei fondi sono nella descrizione, lontani dalle ricompense; l'elenco dei progetti non ha un testo che spieghi raddoppio e «tutto o niente» | Mind the Climate, MILK-ACT, Partner UniTo › Progetti | H6 | — | 3 | 3 (GA); 1 (AN-MC:49); 3 (AN-MC:101); 2 (AN-PR:126) | GA s37; AN-MC:49, :101; AN-PR:126 | S37 |
| P-049 | La pagina del progetto è molto lunga (fino a 18.030 px su mobile), densa, senza indice né ancore verso le sezioni | Pagine progetto | H7 | 2.4.5 | 4 | 4 (GA); 4 (AN-MC:111); 4 (AN-MC:123) | GA s38; AN-MC:111, :112, :123 | S38 |
| P-050 | La barra dell'obiettivo è cliccabile e ricarica la stessa pagina | Mind the Climate | H7 | — | 1 | 1 (GA) | GA s39; AN-MC:113 | S39 |
| P-051 | Testi duplicati in italiano e inglese: ogni ricompensa ripete il testo nelle due lingue; in MatematIcA ogni fascia compare due volte; il modulo di donazione è bilingue riga per riga; le frasi inglesi non hanno `lang="en"` | Mind the Climate, MatematIcA, checkout MILK-ACT | H8 | 3.1.2 | 2 | 2 (GA); 2 (A1-P17); 2 (AL A-P02); 2 (AL A-P15); 3 (AN-MC) | GA s40; A1-P17 r18; AL A-P02:108, A-P15:279; AN-MC:125 | S40 |
| P-052 | Su desktop il comando per sostenere è sotto la piega (a 924 px) e non resta visibile scorrendo; finita la descrizione bisogna risalire | MILK-ACT | H7 | — | 2 | 2 (A1) | A1-P15 r16 | — |
| P-053 | Più soglie non spiegate: dopo il 100% compare un «nuovo obiettivo» o «secondo obiettivo» senza dire rispetto a quale cifra; in Mind the Climate l'obiettivo è 7.000 € nel riquadro e 14.000 € nel testo | BRIGHT, Mind the Climate | H1 / H2 | — | n.d. | n.d. (osservazione in una parte commentata di AN-MC) | GA s30; AN-MC:32 (commento); AL:320 (positivo: in MILK-ACT il rilancio è spiegato nel testo) | X08 |

## D · Donazione (checkout)

| ID | Descrizione | Pagina valutata | Euristica | WCAG | G | Gravità nelle fonti | Fonti | C00 |
|---|---|---|---|---|---|---|---|---|
| P-054 | Gli errori del modulo (per esempio importo sotto il minimo) compaiono solo dopo l'invio e solo in italiano, mentre il modulo è bilingue; la regola «tutto o niente» non è richiamata nel modulo | Tutti i progetti attivi, modulo di donazione | H9 | 3.3.1, 3.3.3, 3.1.2 | 4 | 4 (GA); 5 (fuori scala, AN-MC:135); 1 (AN-MC:136) | GA s41; AN-MC:135, :136 | S41 |
| P-055 | Il nome del donatore diventa pubblico se non si spunta «donatore anonimo», che non è selezionata in partenza | Mind the Climate › modulo di donazione | H5 | — | 2 | 2 (GA); 3 (AN-MC) | GA s42; AN-MC:93 | S42 |
| P-056 | Anche scegliendo l'anonimato il promotore riceve nome, email e importo del donatore | — | — | — | n.d. | n.d. | **Solo** C00 (X03, «analisi preliminare»): **non trovato in nessun file di assignment1**. Da verificare | X03 |
| P-057 | Il checkout non indica i passi né l'effetto di «DONA ADESSO!» (in realtà reindirizza a PayPal/Satispay o mostra le coordinate del bonifico); l'importo compare solo in cima; su mobile il riepilogo «Stai sostenendo» arriva dopo il pulsante di invio | Checkout MILK-ACT | H1 / H5 | — | 3 | 2 (A1-P03); 3 (AL A-P14) | A1-P03 r4; AL A-P14:264 | — |
| P-058 | Dal modulo non si può cambiare ricompensa né annullare: nessun «Modifica» o «Torna al progetto»; il minimo dell'importo è legato alla ricompensa scelta (15 €) | Checkout MILK-ACT | H3 | — | 2 | 2 (A1) | A1-P08 r9 | — |
| P-059 | Il modulo di donazione non previene gli errori: campi obbligatori `(*)` non dichiarati al browser (`required=false`), email `type="text"` senza controllo, importo e nome senza `label`, note senza `id`, nessun `autocomplete`, nessun metodo preselezionato, reCAPTCHA in fondo | Checkout MILK-ACT | H5 | 1.3.1, 1.3.5, 3.3.2, 4.1.2 | 3 | 2 (A1-P11); 3 (AL A-P12) | A1-P11 r12; AL A-P12:234 | — |
| P-060 | I radio dei metodi di pagamento hanno come etichetta solo un'icona: lo screen reader non sa quale metodo sta scegliendo | Checkout MILK-ACT | H6 | 1.3.1, 4.1.2 | 3 | 3 (AL) | AL A-P13:249 | — |
| P-061 | Aprendo direttamente l'indirizzo del checkout si viene reindirizzati alla homepage senza spiegazione; il titolo della scheda resta quello generico della home | Checkout MILK-ACT | H3 | 2.4.2 | 2 | 2 (AL) | AL A-P11:224; WCV `donazione_wcv_*.png` (il filmstrip mostra la homepage) | — |
| P-062 | I metodi di pagamento cambiano da una pagina all'altra («carte di credito, PayPal, Satispay e bonifico» in Come funziona; «PayPal, PayWay e bonifico», senza Satispay, nelle FAQ); «PayWay» è un nome tecnico poco familiare | Come funziona, FAQ, checkout | H4 | — | 2 | 2 (LZ-CF) | LZ-CF:73; A1-P22 r23 (la proposta chiede «metodi di pagamento aggiornati»); `valutazione_antofallea.pdf` p. 28 | X01 |
| P-063 | Le commissioni di pagamento sono a carico del donatore e, se la campagna fallisce, la donazione viene restituita «con l'addebito delle spese di transazione»: l'informazione è sepolta nelle FAQ per progettisti; due risposte danno commissioni diverse (PayPal 1,8% + 0,35 € e, dal 24/06/2025, 1,2% + 0,35 € / 3,5%); l'elenco di 13 carte è ripetuto due volte | FAQ | H5 / H4 | — | 2 | 2 (LZ-FAQ:84); 2 (LZ-FAQ:74); 2 (LZ-FAQ:75); 2 (LZ-FAQ:116) | LZ-FAQ:74, :75, :84, :116 | X02 |
| P-064 | Non è chiaro se la donazione è detraibile né che ricevuta si ottiene; mancano anche tempi del rimborso, passaggi del bonifico, spedizione delle ricompense e a chi rivolgersi se non arrivano | FAQ | H10 | — | 2 | 2 (LZ-FAQ) | LZ-FAQ:139 | X04 |
| P-065 | La ricompensa a importo libero si chiama «FAI TU», un nome che non dice che è una donazione libera; il minimo varia da progetto a progetto (5 € in Mind the Climate; nel checkout MILK-ACT il minimo coincide con la ricompensa, 15 €) | Mind the Climate, MILK-ACT | H2 | — | 1 | 1 (AN-MC) | AN-MC:60; A1-P08 r9 | X05 |
| P-066 | La risposta FAQ sul pagamento rifiutato spiega i motivi ma non che cosa fare dopo (riprovare, altro metodo, chi contattare); per PayWay nessun riferimento | FAQ | H9 | — | 3 | 3 (LZ-FAQ) | LZ-FAQ:126 | — |

## E · Percorso di chi vuole candidare un progetto

| ID | Descrizione | Pagina valutata | Euristica | WCAG | G | Gravità nelle fonti | Fonti | C00 |
|---|---|---|---|---|---|---|---|---|
| P-067 | I consensi del modulo di registrazione sembrano caselle di spunta ma sono `button` senza ruolo né stato: lo screen reader non dice se sono selezionati | Registrazione area progettisti | H1 | 1.3.1, 4.1.2 | 2 | 2 (GA); 3 (AL A-P04) | GA s45; AL A-P04:138 | S45 |
| P-068 | Gergo non spiegato per i promotori: «campaign manager», «call di consulenza», «fee di accesso», «territoriale», «profit e non profit», «gingerizzato», «in itinere», «keep it all», «budget», «PayWay» | Come funziona, FAQ | H2 | 3.1.3 (AAA) | 2 | 2 (GA); 2 (LZ-CF:50); 1 (LZ-CF:51); 2 (LZ-FAQ:53) | GA s46; LZ-CF:50, :51; LZ-FAQ:53 | S46 |
| P-069 | Le pagine nominano il passo successivo senza link («Lancia una campagna», «iscriviti»); il link «commissioni» apre le Condizioni d'uso; «Come funziona» non termina con un'azione; il link ai partner porta ai corsi; FAQ e Come funziona non si richiamano e le risposte non si collegano tra loro | Come funziona, FAQ | H3 | 2.4.4 | 2 | 2 (GA); 2? (LZ-CF:62, :63); 2 (LZ-CF:86); 1 (LZ-CF:139); 2 (LZ-FAQ:87); 1 (LZ-FAQ:142) | GA s47; LZ-CF:62, :63, :86, :139; LZ-FAQ:87, :142 | S47 |
| P-070 | Lo stesso concetto ha nomi diversi: «Prende ciò che raccoglie» / «keep it all»; «Tutto o Niente!» / «O tutto o niente»; donatore / sostenitore / finanziatore; progettista / proponente / creativo; tre ingressi diversi per la formazione («Formazione», «Pacchetti», «Management»); la FAQ presenta insieme i due modelli senza dire quale vale per un progetto | Come funziona, FAQ, Servizi | H4 | 3.2.4 | 1 | 1 (GA); 2 (LZ-CF:72); 1 (LZ-CF:76); 2 (LZ-FAQ:76); 2 (LZ-FAQ:85); 2 (A2-P07) | GA s48; LZ-CF:72, :76; LZ-FAQ:76, :85; A2-P07 r8 | S48 |
| P-071 | La quota di 350 € + IVA per pubblicare compare una sola volta, in fondo a un paragrafo, a ~4.000 px, in corpo 14,4 px; non è citata nelle FAQ (dove sembra che pubblicare sia gratuito) né in «Servizi», che non indica servizi e prezzi; non si sa se è rimborsata se la campagna fallisce | Come funziona, FAQ, Servizi | H5 / H8 | — | 4 | 4 (GA); 3 (LZ-CF:82); 3 (LZ-CF:74); 2 (LZ-CF:84); 2 (A2-P15); 2 (A2-P04) | GA s49; LZ-CF:74, :82, :84; A2-P15 r16; A2-P04 r5 | S49 |
| P-072 | Il modulo di registrazione non usa i controlli del browser: campi non obbligatori, email `type="text"`, `autocomplete="off"` anche su email e password | Registrazione area progettisti | H5 | 1.3.5, 3.3.1 | 2 | 2 (GA); 2 (AL A-P05) | GA s50; AL A-P05:148 | S50 |
| P-073 | Nel modulo di registrazione le etichette sono solo segnaposto: spariscono mentre si scrive e lo screen reader non legge il nome del campo | Registrazione area progettisti | H6 | 1.3.1, 3.3.2, 4.1.2 | 3 | 3 (GA); 3 (AL A-P03) | GA s51; AL A-P03:123 | S51 |
| P-074 | «Come funziona» è un testo continuo (5.763 px) senza titoli né indice: i nomi dei sette passi sono solo nelle illustrazioni, con testo alternativo uguale al nome del file («900-pixel-hai-u»); nessun indicatore di posizione | Come funziona | H7 | 1.1.1, 1.3.1, 2.4.6 | 3 | 3 (GA); 2 (A2-P14); 3 (LZ-CF:95); 2? (LZ-CF:41); 2 (LZ-CF:105); 2? (LZ-CF:115) | GA s52; A2-P14 r15; LZ-CF:41, :95, :96, :105, :115 | S52 |
| P-075 | Le 25 FAQ sono un'unica lista: domande per donatori e promotori mescolate, nessun gruppo, indice, ricerca o ancora condivisibile, ordine non per priorità; «Come funziona» si rivolge solo a chi lancia una campagna; nessuna domanda sul cofinanziamento del partner | FAQ, Come funziona | H7 / H10 | — | 3 | 3 (GA); 2 (A1-P22); 3 (LZ-FAQ:63, :97, :102); 2 (LZ-FAQ:44, :66, :86, :98); 2 (LZ-CF:52) | GA s53; A1-P22 r23; LZ-FAQ:44, :63, :66, :86, :97, :98, :102; LZ-CF:52 | S53 |
| P-076 | In «Come funziona» alcuni paragrafi importanti, comprese le informazioni sui costi, hanno un corpo molto piccolo e dimensioni diverse senza motivo | Come funziona | H8 | 1.4.12 (spaziatura), leggibilità | 4 | 4 (GA) | GA s54 | S54 |
| P-077 | Il messaggio di errore resta visibile anche dopo aver corretto il campo, fino al nuovo invio | Registrazione area progettisti | H9 | 3.3.1 | 2 | 2 (GA); 2 (AL A-P06) | GA s55; AL A-P06:158 | S55 |
| P-078 | Il pulsante «Lancia una campagna» porta alla registrazione generica, mentre il programma con l'Ateneo ha una selezione separata spiegata solo su unito.it; «Come funziona» e FAQ descrivono il percorso di candidatura in due modi diversi | Menu, Partner UniTo, Come funziona, FAQ | H5 / H4 | — | 3 | n.d. (AN-PR:83); 2 (LZ-CF:75); 3 (A1-P20) | AN-PR:83; LZ-CF:75; A1-P20 r21 | X07 |
| P-079 | Mancano le informazioni per pianificare una candidatura: se il corso di formazione è obbligatorio, quanto costa e dura; tempi dal primo contatto alla pubblicazione; durata della consulenza; servizi aggiuntivi e costi; che cosa si può modificare dopo la pubblicazione; il quadro è sparso tra più siti | Come funziona, FAQ | H5 / H10 | — | 3 | 3 (LZ-CF:83); 2 (LZ-CF:137); 2 (LZ-CF:138); 1 (LZ-FAQ:88) | LZ-CF:83, :137, :138; LZ-FAQ:88 | — |

## F · Aiuto, contatti e contenuti informativi

| ID | Descrizione | Pagina valutata | Euristica | WCAG | G | Gravità nelle fonti | Fonti | C00 |
|---|---|---|---|---|---|---|---|---|
| P-080 | Orari di contatto diversi tra «Come funziona» (9:30–16:30) e «Contatti» (9:30–13 e 14–16:30); nessun tempo di risposta della mail; il contatto per i donatori non c'è nelle risposte sui pagamenti; la FAQ non chiude con «Non hai trovato la risposta?» | Come funziona, Contatti, FAQ | H4 / H9 | 3.2.6 | 2 | 1 (A2-P11); 1 (LZ-CF:123); 2 (LZ-FAQ:127); 2 (LZ-FAQ:128) | A2-P11 r12; LZ-CF:123; LZ-FAQ:127, :128 | — |
| P-081 | Il numero di telefono nel testo non è cliccabile (la mail sì): da smartphone va copiato a mano | Come funziona | H7 | — | 2 | 2? (LZ-CF) | LZ-CF:104 | — |
| P-082 | Risposte FAQ lunghe e senza struttura («muri di testo»), tono promozionale («idea geniale»), spiegazioni lunghe per concetti semplici, risposte poco pratiche | FAQ | H8 / H2 | — | 3 | 3 (LZ-FAQ:115); 2 (LZ-FAQ:103); 1 (LZ-FAQ:54, :55, :141) | LZ-FAQ:54, :55, :103, :115, :141 | — |
| P-083 | Refusi ed errori ortografici in pagine che parlano di soldi e fiducia («modalitè», «Si» senza accento, «addebita», «sotenerli») | FAQ | H4 | — | 2 | 2 (LZ-FAQ) | LZ-FAQ:78 | — |
| P-084 | «Tasso di successo superiore al 90%, il più alto in Italia» senza fonte, periodo né metodo di calcolo | Come funziona | H2 | — | 1 | 1 (LZ-CF) | LZ-CF:53 | — |

## G · Accessibilità trasversale (oltre a quanto già nelle aree precedenti)

| ID | Descrizione | Pagina valutata | Euristica | WCAG | G | Gravità nelle fonti | Fonti | C00 |
|---|---|---|---|---|---|---|---|---|
| P-085 | Con il menu hamburger chiuso il focus passa su un link vuoto, sull'hamburger senza nome e sulle voci del pannello non visibile; nessun indicatore visivo del focus | MatematIcA, VIBE, MILK-ACT (mobile 390 × 844) | H1 | 2.4.3, 2.4.7, 2.4.11 | 3 | 3 (AL) | AL A-P07:168 | — |
| P-086 | Controlli senza nome accessibile: ricerca globale annunciata solo con un glifo, hamburger `javascript:void(0)` senza nome, campi «donazione libera» senza label e con `id` duplicato; link con testo vuoto prima di «FAQ» | MatematIcA, VIBE, MILK-ACT, Come funziona | H6 | 4.1.2, 2.4.4 | 3 | 3 (AL); 1 (LZ-CF) | AL A-P08:178; LZ-CF:125 | — |

Altri problemi di accessibilità sono nelle aree precedenti: P-010, P-012, P-017, P-029, P-034, P-046, P-059, P-060, P-067, P-073.

## I · Mobile e prestazioni

| ID | Descrizione | Pagina valutata | Euristica | WCAG | G | Gravità nelle fonti | Fonti | C00 |
|---|---|---|---|---|---|---|---|---|
| P-087 | Da smartphone nessuna pagina supera i Core Web Vitals (LCP 3,4 s contro 2,5 s; FCP 2,3 s; TTFB 1,6 s); Lighthouse mobile: prestazioni 39–68, accessibilità 64–77; le pagine più lente sono quella del progetto (41) e la donazione (39); in laboratorio LCP fino a 34,1 s (Mind the Climate) e CLS 0,478 | Partnership, Progetti, Mind the Climate, Donazione | — (misura) | — | n.d. | n.d. (slide di misura, senza gravità) | GA s72–s78; WCV (tutti gli 8 report; valori in `01_inventario_fonti.md` §3.1) | S74 |

Il problema dei caroselli su mobile è P-037; la colonna di link prima del contenuto è P-018; la 404 senza viewport è P-019; il riepilogo dopo il pulsante su mobile è in P-057.

## J · Problemi scartati o non applicabili al nuovo sito

Compaiono qui per completezza: la tracciabilità li riporta con lo stato «non applicabile» e il motivo.

| ID | Descrizione | Pagina valutata | Euristica | WCAG | G | Gravità nelle fonti | Fonti | Motivo |
|---|---|---|---|---|---|---|---|---|
| P-088 | Catalogo dei partner: il menu «Partner» mostra solo nomi (né tipo, né territorio, né bando aperto); non esiste una pagina dei partner con indirizzo e filtro; «Partner» e «Collaborazioni» sono due elenchi scollegati con nomi scritti in modo diverso | Menu Partner, Collaborazioni | H6 / H7 / H4 | — | 3 | 3 (A2-P12); 2 (A2-P13); 2 (A2-P08) | A2-P08 r9; A2-P12 r13; A2-P13 r14 | Il nuovo sito è dedicato a un solo ente (Università di Torino): non ha un catalogo di partner. Il principio sottostante (ogni sezione ha un indirizzo proprio, condivisibile) vale comunque ed è coperto dai requisiti sugli URL |
| P-089 | Le immagini di «Come funziona» sono caricate con indirizzi `http` invece di `https` | Come funziona | H4 | — | 1 | 1? (LZ-CF) | LZ-CF:77 | Riguarda l'infrastruttura del fornitore, non l'interazione. Nel prototipo tutte le risorse sono locali con URL relative |
| P-090 | Il metadato `twitter:site` indica `@nytimes` | Come funziona | H4 | — | 1 | 1 (LZ-CF) | LZ-CF:78 | Osservazione tecnica collaterale (la fonte stessa la definisce «da segnalare a parte»); il prototipo non pubblica metadati per i social |

### Osservazioni delle fonti non considerate problemi

- `LZ-FAQ:80`: «Link riconoscibili» è un segnaposto `[VERIFICA: …]` mai verificato. Nessun problema registrato; il nuovo design system sottolinea comunque i link nel testo.
- `AN-PR` sezioni 1–2, `AN-PR:65` (breadcrumb assente nella pagina Progetti), `AN-PR:76` (gerarchia dei titoli), `AN-PR:100`, `AN-PR:110`, `AN-PR:113`; `AN-MC:62` (schwa), `AN-MC:72`, `AN-MC:102`, `AN-MC:131`, `AN-MC:144`: osservazioni **commentate dall'autore** (`<!-- -->`), quindi ritirate dalla valutazione. Unica eccezione: il dato numerico di `AN-MC:32` (7.000 € contro 14.000 €), usato come evidenza di X08 perché la chiave esiste nel catalogo C00.

## Aspetti positivi da conservare

Le fonti segnalano anche che cosa funziona. Il nuovo sito li mantiene:

| Chiave | Aspetto positivo | Fonte |
|---|---|---|
| S08 | Card con percentuale, importo su obiettivo e donatori; campagne in corso e concluse separate; linguaggio chiaro («raccolto», «donatori»); card nello stesso formato | GA s8; AN-PR:40–42, :53, :71 |
| S27 | Riquadro di stato con scadenza esplicita; schede di sezione con il numero di elementi e scheda attiva evidenziata; breadcrumb; ricompense uniformi con importo minimo e posti rimasti; «Copia link» e condivisione; parole chiave in grassetto e infografiche; descrizione che anticipa le domande (uso dei fondi, uso dei dati, team); errore chiaro sotto il minimo | GA s27; AN-MC:41–45, :54, :66–68, :107, :119, :129, :140 |
| S44 | FAQ scritte come domande; mail, telefono e orari ben visibili; tre modi per iniziare; nel modulo l'errore porta il focus sul campo | GA s44; AL §5 «Aspetti positivi osservati» |
| S58 | «Lancia una campagna» ben visibile nel menu principale; voci del menu che iniziano con la parola chiave | GA s58 |
| S70 | Su smartphone pagina progetto in una colonna leggibile, riepilogo prima del video, pulsante «Sostieni il progetto» visibile, barra delle sezioni fissa | GA s70 |
| — | Quattro fasi del programma chiare (Formazione, Selezione, Accompagnamento, Raccolta e raddoppio); VIBE spiega l'uso dei fondi in modo concreto | `valutazione_antofallea.pdf` p. 30, 32; AL §5 |

## Sintesi numerica

90 problemi consolidati da circa 190 osservazioni delle fonti (54 slide-problema di GA, 22 + 16 problemi dei CSV, 15 problemi e 3 ricorrenze di AL, ~45 criticità di andre e ~70 di lorenzo).

| Area | Totale | G4 | G3 | G2 | G1 | n.d. |
|---|---|---|---|---|---|---|
| A · Homepage e navigazione | 20 | 1 | 5 | 7 | 7 | 0 |
| B · Elenco progetti e programma | 18 | 3 | 7 | 8 | 0 | 0 |
| C · Pagina del progetto | 15 | 2 | 5 | 4 | 3 | 1 |
| D · Donazione | 13 | 1 | 4 | 6 | 1 | 1 |
| E · Percorso del promotore | 13 | 2 | 5 | 5 | 1 | 0 |
| F · Aiuto e contatti | 5 | 0 | 1 | 3 | 1 | 0 |
| G · Accessibilità trasversale | 2 | 0 | 2 | 0 | 0 | 0 |
| I · Mobile e prestazioni | 1 | 0 | 0 | 0 | 0 | 1 |
| J · Scartati / non applicabili | 3 | 0 | 1 | 0 | 2 | 0 |
| **Totale** | **90** | **9** | **30** | **33** | **15** | **3** |

Nota: il totale dei problemi della presentazione di gruppo (57 in GA s80) non coincide con le 54 slide-problema, come già segnalato in `assignment2/README.md`. Questo documento usa le slide, non il grafico.
