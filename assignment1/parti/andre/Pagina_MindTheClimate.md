# Stato della UX della pagina progetto "Mind the Climate" su Ideaginger: analisi di massima secondo le 10 euristiche di Nielsen

**Pagina analizzata**: <https://www.ideaginger.it/progetti/mind-the-climate.html> (scheda di un progetto Funds TOgether dell'Università di Torino)
**Data**: 12/10/2026
**Come è stata svolta**: lettura del contenuto e della struttura della pagina (testi, titoli, link, testi alternativi), senza browser interattivo. Resa grafica, colori, comportamento JavaScript, percorso di donazione dopo il pulsante SOSTIENI, tastiera, zoom e mobile **non sono stati osservati**: dove servono sono indicati con un placeholder.
**Riferimento metodologico**: `checklist_analisi_euristica.md` (sezione 5 per gli elementi da osservare, sezione 3 per la scala di gravità 0–4). Stesso formato di `ux_nielsen_progetti_unito.md`.

> **Come leggere i placeholder**
> - `[VERIFICA: …]` è un controllo da fare a mano sul sito, che può confermare, modificare o annullare l'osservazione.
> - `[SCREENSHOT: …]` è l'immagine da inserire nel report, con il problema evidenziato.
> - `[GRAVITÀ: x?]` è un valore provvisorio da confermare dopo la verifica (scala Nielsen 0–4).
> - Annotare per ogni verifica **browser, dispositivo, risoluzione e data** (checklist, sez. 8).
> - **Non completare pagamenti** né inviare il modulo di contatto: fermarsi alla schermata di scelta del metodo di pagamento.

---

<!-- ## 1. Che cos'è la pagina e a cosa serve

È la scheda del progetto **Mind the Climate** (app per studiare l'effetto del clima sulla salute mentale), una delle cinque campagne Funds TOgether 2026. Deve permettere di capire il progetto, valutarne la credibilità e **donare scegliendo una ricompensa**. Struttura rilevata, dall'alto:

1. header del sito e **breadcrumb**: Home › Progetti › Università di Torino › Mind the Climate;
2. intestazione: titolo (`h1`), proponente "Mind the Climate - UniTO", "Scade il 18/11/2026", "O tutto o niente!" (con tooltip), categorie, SDG 3 e 13, video YouTube;
3. **box di stato**: "38 % RACCOLTO", "€ 2.690 raccolti su € 7.000", "97 sostenitori", "-37 giorni", pulsante **"Sostieni il progetto"** (ancora alle ricompense);
4. **schede**: Progetto · News 1 · Commenti 12 · Sostenitori 97 · Condividi;
5. descrizione lunga (circa 1.500–1.800 parole) organizzata in **domande e risposte** come sottotitoli, con infografiche numerate 01–06, sezione budget e soglie;
6. **ricompense** (10, da FAI TU con minimo 5 € a 1.000 €), testi bilingui IT/EN, ciascuna con pulsante **SOSTIENI**;
7. "Conosci il progettista" (presentazione del team di 4 ricercatrici e ricercatori) e "Contatta il progettista";
8. footer.

## 2. Giudizio complessivo provvisorio

È una pagina **ricca e curata nei contenuti**: il tono a domande e risposte rende accessibile un progetto di ricerca, il budget spiega come verranno usati i fondi, il team è presentato in modo trasparente e le ricompense sono numerose e descritte. Rispetto alla lista dei progetti ha un orientamento migliore (breadcrumb, `h1`, scadenza in chiaro). I problemi principali riguardano la **chiarezza dei numeri chiave** (obiettivo di 7.000 € nel box ma 14.000 € nel testo, giorni con segno negativo, effetto del raddoppio UniTo non visibile nel box), la **lunghezza della pagina** (le ricompense e il pulsante per donare sono molto in basso) e l'**accessibilità** (infografiche senza testo alternativo). Il percorso di donazione dopo SOSTIENI va osservato a mano: è la parte con più peso per l'utente sostenitore.

--- -->

## 3. Analisi per euristica

### E1. Visibilità dello stato del sistema

**Positivo**
- Box di stato completo: percentuale, raccolto su obiettivo, sostenitori, giorni, e scadenza esplicita "Scade il 18/11/2026" nell'intestazione. `[GRAVITÀ: 0]`
- Breadcrumb presente: l'utente sa di trovarsi in un progetto dell'Università di Torino. `[GRAVITÀ: 0]`
- Le ricompense indicano quanti le hanno già scelte e quante ne restano. `[GRAVITÀ: 0]`
- Ogni sottosezione(news, commenti, ...) ha il numero di risorse presenti in essa.
- La sottosezione attiva viene evidenziata tra le schede in modo da renderla esplicita

**Criticità**
- **"-37 giorni"** accanto a una scadenza tra 37 giorni: il segno meno fa pensare a una campagna scaduta. Lo stesso problema compare nella lista progetti dove però è più grave in quanto manca la data di scadenza. `[GRAVITÀ: 2]`
- **Effetto del cofinanziamento non visibile nel box**: UniTo raddoppia le donazioni se si raggiungono 7.000 €, ma il box mostra solo 2.690 € su 7.000 € e non indica né la soglia di sblocco né il valore raddoppiato. Questo è un problema se l'utente non conosce tutta la storia del progetto FundsTo. Chi ha scritto la panoramica del progetto l'ha però specificato, riduciamo quindi la gravità per questo singolo articolo. `[GRAVITÀ: 1]`
- Quando vogliamo contattare un progettista, la pagina risponde molto lentamente prima di mostrare i contatti, come se non avesse preso il click: `[GRAVITÀ: 3]`
### E2. Corrispondenza tra sistema e mondo reale

**Positivo**
- Testo a **domande e risposte** dal punto di vista del lettore ("Wow! Posso sapere come spenderete questi soldi?", "Posso anche usare l'app, vero?"): segue il modello mentale di chi valuta se donare. `[GRAVITÀ: 0]`
- "O tutto o niente!" spiegato con un tooltip. `[GRAVITÀ: 0]`
- Mind the Climate indicato come progettista
- Ogni livello di sostegno viene spiegato chiaramente

**Criticità**
- **Termini non spiegati**: "co-design", "dashboard", "badge", "DSA" (nella biografia), "FAI TU" (nome della ricompensa libera, che non dice che si tratta di una donazione a importo libero). Sono termini ormai noti ma che per qualcuno potrebbero dare problemi.`[GRAVITÀ: 1]`
- La sezione news porta alla versione in inglese del progetto mandando in confusione l'utente sulla sezione notizie che vorrebbe visitare. `[GRAVITÀ: 3]`
<!-- - **Schwa (ə)** usato estesamente ("abituatə", "Cittadinə ricercatorə"): scelta inclusiva dal punto di vista del genere, ma può rallentare la lettura e alcuni screen reader lo leggono male o lo saltano. Da segnalare in modo neutro, come tema di accessibilità più che di usabilità. `[VERIFICA: lettura con uno screen reader (NVDA/VoiceOver)]` `[GRAVITÀ: 1?]` -->
### E3. Controllo e libertà dell'utente

**Positivo**
- Breadcrumb cliccabile per risalire alla lista UniTo. `[GRAVITÀ: 0]`
- Il video su YouTube è controllabile dall'utente
- L'utente può navigare liberamente nelle sottosezioni e il selettore delle sezioni è sticky che rende agevole la navigazione
<!-- - Il breadcrumb è presente anche nella pagina sostieni -->

**Criticità**:
<!-- - Il breadcrumb nella pagina sostieni non si ricorda la posizione di scroll -->
- La lista dei livelli di donazione è molto lunga, per l'utente può essere frustrante cercare il livello che vuole sottoscrivere. BIsognerebbe compattare la lista e renderla controllabile dall'utente. `[GRAVITÀ: 3]`
- Non c'è un modo per tornare all'inizio della pagina. `[GRAVITÀ: 3]`
### E4. Consistenza e standard

**Positivo**
- Ricompense con struttura uniforme (immagine, titolo, testo, contatori, pulsante). `[GRAVITÀ: 0]`
- La struttura della pagina è consistente con le altre pagine dei progetti

**Criticità**
- **Contatori delle ricompense non uniformi**: per le ricompense più alte manca il numero di sostenitori (probabilmente zero, non mostrato). `[GRAVITÀ: 1]`
- La versione in inglese, mostra semplicemente la panoramica del progetto in inglese ma il resto del sito rimane in Italiano con qualche sovrapposizione di testo inglese. Inoltre mancano diverse parti rispetto alla versione in italiano come gli obiettivi di sostenibilità e la formula tutto o niente`[GRAVITÀ: 5]`

![[Screenshot 2026-10-12 alle 23.11.07.png]]
- I tooltip sembrano dei link(il browser gli interpreta come tali) ma in realtà non portano da nessuna parte. Sia quelli degli obiettivi di sostenibilità che quelli tutto o niente.
### E5. Prevenzione dell'errore

**Positivo**:
- **Scelta della ricompensa sotto i vincoli**: Il sistema impone in vincolo di importo minimo in base al livello stabilito.  `[GRAVITÀ: 0]`

**Criticità**
- **Anonimato**: il testo dice che il nome comparirà sul sito "se lo vorrai". Tuttavia di default non è spuntata la casella del donatore anonimo, bisognerebbe forzare il controllo con dei pulsanti radio si/no in modo da obbligare il donatore ad effettuare una scelta `[GRAVITÀ: 3]`

### E6. Riconoscimento più che ricordo

**Positivo**
- Ogni ricompensa ripete cosa include. `[GRAVITÀ: 0]`

**Criticità**
- **Informazioni utili per donare lontane dal punto di decisione**: raddoppio UniTo, soglie e uso dei fondi stanno nella descrizione, le ricompense molto più in basso. Chi arriva alle ricompense deve ricordarsi cosa ha letto prima. `[GRAVITÀ: 3]`
<!-- - **Sottotitoli a domanda** molto discorsivi ("Che figo, un Citizen Scientist! Non vedo l'ora!..."): piacevoli alla lettura, ma poco efficaci per la scansione rapida, perché non dicono subito l'argomento della sezione (budget, team, uso dei dati). `[GRAVITÀ: 1?]` -->

### E7. Flessibilità ed efficienza d'uso

Positivo:
- **"copia link"** e condivisione su 9 canali: buone scorciatoie per chi vuole diffondere il progetto. `[GRAVITÀ: 0]`
- La pagina è responsiva e funziona bene sul mobile

Criticità:
- **Pagina molto lunga** senza indice né ancore verso le sezioni principali (budget, ricompense, team): chi vuole solo donare deve affidarsi al pulsante "Sostieni il progetto". `[GRAVITÀ: 4]`
- Non esistono shortcut per cambiare sezione nella pagina
- Cliccare sul gauge del goal delle donazioni riporta nuovamente alla stessa pagina ricaricandola inutilmente.
- `[VERIFICA – mobile/responsive: dove finisce il box di stato? Il pulsante per donare resta raggiungibile (sticky)? Le schede si leggono su schermo stretto? Target touch di almeno 24×24 px]`

### E8. Estetica e design minimalista

Positivo:
- C'è gerarchia tra i titoli e le varie sezioni. Sono in grassetto le parole più importanti. L'interlinea è buono
- Ci sono le infografiche che aiutano la comprensione del testo e aggiungono dettagli

Criticità:
- **Densità di contenuto**: Ci sono molte informazioni nel testo e mancano riassunti e indici in modo che l'utente possa andare alla sezione che più gli interessa. `[GRAVITÀ: 4]`
- Il contrasto dei titoli in arancione chiaro è basso: 2.5:1, sarebbe meglio cercare di aumentarlo per migliorare la leggibilità. Anche il testo bianco dentro i pulsanti verdi hanno troppo poco contrasto.
- **Testi misti IT/EN** nelle ricompense: utili per un pubblico internazionale, ma raddoppiano la lunghezza di ogni blocco, sarebbe meglio usare un'internazionalizzazione completa del sito che invece manca. `[GRAVITÀ: 3]`
### E9. Aiutare a riconoscere, diagnosticare e uscire dagli errori

Positivo:
- Nel caso della donazione libera, la pagina mostra un errore chiaro se non si immette almeno il valore minimo.
![[Screenshot 2026-10-12 alle 23.08.28.png]]
<!--- Nel caso provassimo a fare una donazione con email invalida, il sistema lo riconosce e dà un feedback all'utente
![[Screenshot 2026-10-12 alle 23.17.00.png]] 
- Nella sezione FAQ ci sono alcuni aiuti in caso di pagamento fallito -->
Criticità:
- I messaggi di errore mostrati non hanno un equivalente in inglese `[GRAVITÀ: 5]`
- I messaggi mostrati non danno un feedback immediato all'utente ma appaiono solo dopo aver premuto il pulsante di invio del form. `[GRAVITÀ: 1]`
### E10. Aiuto e documentazione

**Positivo**
- La descrizione anticipa le domande del sostenitore (uso dei fondi, uso dei dati, cosa ne ricava il territorio, chi è il team). `[GRAVITÀ: 0]`
- Tooltip su "O tutto o niente!". `[GRAVITÀ: 0]`

**Criticità**
<!-- - **Nessun aiuto vicino ai pulsanti di donazione**: FAQ e "Come funziona" sono solo nell'header e nel footer; non c'è un rimando a metodi di pagamento, commissioni, rimborso o ricevuta nel punto in cui si decide di donare. `[GRAVITÀ: 3]` -->

---
