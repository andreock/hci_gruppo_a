# Stato della UX della pagina "Progetti" UniTo su Ideaginger: analisi di massima secondo le 10 euristiche di Nielsen

**Pagina analizzata**: <https://www.ideaginger.it/partner-progetti/universita-di-torino.html> (scheda "Progetti" della sezione partner Università di Torino)
**Data**: 12/10/2026
**Come è stata svolta**: lettura del contenuto e della struttura della pagina (testi, titoli, link, testi alternativi), senza browser interattivo. Resa grafica, colori, comportamento JavaScript, tastiera, zoom e mobile **non sono stati osservati**: dove servono sono indicati con un placeholder.
**Riferimento metodologico**: `checklist_analisi_euristica.md` (sezione 5 per gli elementi da osservare, sezione 3 per la scala di gravità 0–4).

> **Come leggere i placeholder**
> - `[VERIFICA: …]` è un controllo da fare a mano sul sito, che può confermare, modificare o annullare l'osservazione.
> - `[SCREENSHOT: …]` è l'immagine da inserire nel report, con il problema evidenziato.
> - `[GRAVITÀ: x?]` è un valore provvisorio da confermare dopo la verifica (scala Nielsen 0–4).
> - Annotare per ogni verifica **browser, dispositivo, risoluzione e data** (checklist, sez. 8).

---

<!--## 1. Che cos'è la pagina e a cosa serve

È l'elenco dei progetti di crowdfunding dell'Università di Torino (programma **Funds TOgether**) ospitati sulla piattaforma Ginger. Struttura rilevata, dall'alto:

1. barra di servizio (Faq, Contatti, Come funziona, Login progettista) e menu principale (Home, Cerca progetti, Lancia una campagna, Partner, Servizi);
2. banner UniTo con due schede, **Partnership** e **Progetti**;
3. titolo "Università di Torino" e contatori (18 progetti, €343.000+ raccolti, 2.900+ donatori, 100% successo, 369% overfunding);
4. sezione **PROGETTI IN CORSO** (5 card) e **PROGETTI CONCLUSI** (4 card visibili) con pulsante **"Altri"**;
5. colonna laterale con Progetti, 26 Categorie, 17 SDG ONU, elenco Partner;
6. footer.

Ogni card mostra: percentuale ("118 % RACCOLTO"), raccolto su obiettivo, numero di donatori, giorni (solo in corso), titolo, autore ("by …"), badge "OBIETTIVO RAGGIUNTO!" (solo conclusi).

## 2. Giudizio complessivo provvisorio

La pagina **svolge il suo compito principale**: elenca i progetti, separa quelli attivi da quelli conclusi e mostra per ognuno i dati essenziali della raccolta in forma compatta e coerente. I problemi principali sono di **orientamento e contesto** (la pagina non spiega cos'è Funds TOgether né dice in quale scheda ci si trova), di **chiarezza dei dati di stato** (giorni con segno negativo, progetti "in corso" già oltre il 100%, contatori che non corrispondono alle card visibili) e di **efficienza nella ricerca** (nessun filtro né ordinamento, titoli troncati). Molti aspetti dipendono dalla resa a schermo e vanno verificati prima di assegnare le gravità definitive.

--- -->

## 3. Analisi per euristica

### E1. Visibilità dello stato del sistema

**Positivo**
- Le due sezioni "PROGETTI IN CORSO" / "PROGETTI CONCLUSI" comunicano subito lo stato delle campagne. `[GRAVITÀ: 0]`
- Ogni card riassume lo stato della raccolta (%, importo su obiettivo, donatori). `[GRAVITÀ: 0]`
- **Scheda attiva riconoscibile**: Le schede "Partnership" e "Progetti" vengono marcate sulla barra in modo evidente.  `[GRAVITÀ: 0]`

**Criticità**
- **Giorni rimanenti con segno negativo**: le card mostrano "-36 giorni", "-29 giorni", mentre la scadenza nelle schede (es. MILK-ACT 17/11/2026) indica che mancano circa 36 giorni. Il segno meno fa pensare a una campagna scaduta. `[SCREENSHOT: card con i giorni]` `[GRAVITÀ: 2]` Sarebbe meglio scrivere: Giorni mancanti 36 o qualcosa di più chiaro del semplice segno meno
- **Progetti "in corso" oltre il 100%** (MILK-ACT 118%, RePatch 109%): non c'è un segnale che l'obiettivo minimo è già stato raggiunto, mentre i conclusi hanno il badge "OBIETTIVO RAGGIUNTO!". Inoltre lo stato per i progetti in corso, è comunicato solo attraverso il colore `[GRAVITÀ: 4]`
	- ![[Screenshot 2026-10-12 alle 17.33.40.png|639]]
	- ![[Screenshot 2026-10-12 alle 17.33.21.png]]
<!-- - **Stato comunicato col colore?** `[VERIFICA: barre di avanzamento o badge usano solo il colore? Contrasto sufficiente?]` TODO: Metterlo nel punto 6 se mancante -->
### E2. Corrispondenza tra sistema e mondo reale

**Positivo**
- Linguaggio comprensibile per i progetti: "raccolto", "donatori", "progetti in corso / conclusi". `[GRAVITÀ: 0]`

**Criticità**
- **"OVERFUNDING"**, **"SUCCESSO**, **"369%"** nei contatori: termine tecnico del crowdfunding non spiegato a un pubblico generico e non si capisce il contesto. `[GRAVITÀ: 2]`
- **"Funds TOgether" non compare** in questa pagina: chi arriva dal nome dell'iniziativa (es. da unito.it o dai social) non trova conferma di essere nel posto giusto anche se è presente "Università di Torino" a inizio pagina. `[GRAVITÀ: 1]`
- **Autori eterogenei** ("by VIRMOLAB - UniTo", "by Departments & Dragons", "by Team GaIA"): non sempre si capisce che si tratta di gruppi di ricerca dell'Ateneo soprattutto nei progetti passati. `[GRAVITÀ: 2]`
### E3. Controllo e libertà dell'utente

**Positivo:**
- Quando carichiamo nuovi progetti, la pagina scrolla in automatico nella nuova riga creata dove sono stati caricati i nuovi progetti

**Criticità:**
<!-- - **Breadcrumb assente** in questa pagina (le schede progetto invece la hanno: Home / Progetti / Università di Torino / …). Il ritorno è affidato al logo, a "HOME" e alle schede. Dato che la pagina è poco profonda, il problema è contenuto. `[GRAVITÀ: 1?]` -->
- La pagina non ricorda la posizione di scroll quando un utente ci ritorna(ad esempio dopo aver visitato un progetto). Inoltre non mantiene caricati i progetti già conclusi dopo averne caricati di nuovi tramite il pulsante altro: `[GRAVITÀ: 4]` 
- **Menu a tendina** "Cerca progetti" e "Partner" esiste globalmente ma non per il singolo dipartimento di UniTo. Non è possibile vedere tutti i progetti di UniTo in un unica pagina ed eventualmente dividerli per sottocategoria(arte, eventi, start-up, ...). `[GRAVITÀ: 3]` 
### E4. Consistenza e standard

**Positivo**
- Card con struttura uniforme e stessi campi per tutti i progetti anche quelli conclusi. `[GRAVITÀ: 0]`

**Criticità**
- **Contatori incoerenti con il contenuto**: la pagina dichiara 18 progetti ma nella sezione precedente si parlava di 13 progetti nelle precedenti edizioni, conviene specificare che nell'ultima edizione sono stati aggiunti 5 progetti così da chiarire la situazione. `[GRAVITÀ: 2]`
- I gauge sono di colore blu e rosso, tuttavia tipicamente si dovrebbe usare rosso e verde per indicare quanto si è raggiunto e quanto manca(oltre ad usare chip obiettivo raggiunto per migliorare l'accessibilità). Non è chiara a primo impatto questa scelta di colori. `[GRAVITÀ: 3]`![[Screenshot 2026-10-12 alle 18.29.33.png]]
<!--- **Gerarchia dei titoli**: nella pagina compaiono solo `<h2>` (titolo pagina, sezioni e ogni card allo stesso livello), nessun `<h1>` rilevato. `[VERIFICA: con un'estensione tipo HeadingsMap o DevTools]` `[GRAVITÀ: 2?]` (rilevante anche per l'accessibilità) TODO: La pagina è un po' spoglia e non si capisce bene di cosa si parla se non si capisce il contesto-->
- **Link riconoscibili**: Non si capisce benissimo a primo impatto che la card sia cliccabile quando ci si va sopra. Una soluzione utile sarebbe sopraelevarla in 3D così da rendere immediatamente riconoscibile che sia un elemento cliccabile. `[GRAVITÀ: 3]` 
- Nel caso della visualizzazione mobile, ci sono un carosello per i contatori e due caroselli che permettono di navigare tra i progetti in corso e conclusi, tuttavia la mancanza di frecce o un indicatore di posizione del carosello non lo rendono comprensibile e c'è il rischio che l'utente vedendo solo due progetti, non capisca che si possano scorrere.`[GRAVITÀ: 5]` 
- Sempre nella visualizzazione mobile, i caroselli per i progetti conclusi contengono solo 4 entità, le altre andranno caricate con il pulsante "Altri" che farà apparire altri caroselli. Questo non è consistente dato che si potrebbe usare un singolo carosello. `[GRAVITÀ: 2]` ![[Screenshot 2026-10-12 alle 18.50.39.png|252]]
### E5. Prevenzione dell'errore

- **Rischio di scelta sbagliata**: con il segno negativo sui giorni e la mancanza di un badge per i progetti in corso già finanziati, l'utente può scartare progetti ancora aperti o non capire se la sua donazione serve. (come già detto in E1)
- **"LANCIA UNA CAMPAGNA" nel menu**: da questa pagina un ricercatore UniTo può pensare di candidarsi lì, mentre porta alla registrazione generica Ginger e non al percorso di selezione dell'Ateneo, a meno che un ricercatore UniTo non riceva indicazioni ufficiali da parte dell'ateneo, la registrazione a FundsTo potrebbe risultare poco chiara a meno di visitare prima la pagina Partnership che a metà ha un collegamento verso il sito ufficiale UniTo che spiega il bando. Il link "Lancia una campagna" dovrebbe dichiarare che non è il modo per partecipare a FundsTo oppure dovrebbe rimandare alla pagina UniTo per le partnership con UniTo  `[GRAVITÀ: 3]`

### E6. Riconoscimento più che ricordo

Positivo:
- Le card hanno tutte lo stesso formato e rimandano a pagine che hanno lo stesso template in modo che l'utente sappia riconoscere che si tratta di un progetto
- Ci sono delle immagini per ogni progetto che lo rendono riconoscibile

Criticità:
- Nella pagina progetti, non ci sono chiari riferimenti al logo di UniTo, c'è un'unica immagine appena si apre il sito che però appare confusionaria a primo impatto. `[GRAVITÀ: 2]`![[Screenshot 2026-10-12 alle 18.28.46.png]]
- **Nessuna informazione sul tema** nella card (categoria, breve descrizione): per scegliere tra progetti bisogna ricordare o aprire ciascuno. `[GRAVITÀ: 3]`
- **Icona senza testo** nel menu principale (prima del logo). Rimanda alla home ma è piccola e non si capisce, inoltre è duplicata rispetto al logo del sito che rimanda anche lui alla home. `[GRAVITÀ: 2]`

### E7. Flessibilità ed efficienza d'uso

- **Nessun filtro né ordinamento** (per tema, stato, percentuale, scadenza): con 9 progetti visibili il costo è basso, ma cresce con i 18 dichiarati. `[GRAVITÀ: 3]`
- **Caricamento progressivo "Altri"** invece di mostrare tutto o paginare: per vedere tutti i conclusi servono clic ripetuti. `[GRAVITÀ: 5]`
<!-- - **Colonna laterale molto lunga nella navbar** (26 categorie, 17 SDG, ~25 partner) che non serve a chi è già nella sezione UniTo. Non ci interessa qui, metterlo nell'analisi della home-->
- `[VERIFICA – mobile/responsive (DevTools e smartphone reale): disposizione delle card, menu hamburger, dimensione dei target touch (almeno 24×24 px), dove finisce la colonna laterale]`

### E8. Estetica e design minimalista

Positivo:
- Il design delle card riassume molto bene il progetto sebbene manchino alcuni dettagli come suggerito in precedenza
- Il design è responsivo e usa navbar hamburger a comparsa nel caso del mobile

Criticità:
<!-- - **Rumore attorno al contenuto principale nella navbar**: barra di servizio, menu, scritta di ricerca, colonna con oltre 60 link e footer circondano 9 card. Troppi elementi `[VERIFICA: impressione a schermo, proporzione tra contenuto e navigazione]` `[GRAVITÀ: 1–2?]` -->
- **Contatori**: cinque numeri di effetto ("100% successo", "369% overfunding") utili come rassicurazione, ma ripetuti anche nella scheda Partnership. Bisognerebbe lasciarli in un solo punto(suggeriamo nella scheda progetti). `[GRAVITÀ: 2]`
- Il contrasto degli elementi in blu è buono(circa 6:1), tuttavia il colore arancione chiaro dei titolo è molto chiaro su sfondo bianco ed ha un contrasto di circa 2.5:1 che lo rendono leggibile ma con un po' di fatica. Stesso discorso per il pulsante "Altri" che ha contrasto 2.09:1. Stesso discorso per i chip "Obiettivo Raggiunto" che si fermano a contrasto 3.55:1 non raggiungendo Il limite minimo per una buona lettura di 4:1. Pessimo il contrasto del footer che si ferma a 2:1 rendendo molto difficile la lettura delle sezioni oltre ai titoli delle sezioni molto piccoli. `[GRAVITÀ: 4]`
<!-- - Da mobile la sezione cerca progetti della navbar ha troppa trasparenza e rende difficile la lettura e l'utilizzo della funzionalità -->

### E9. Aiutare a riconoscere, diagnosticare e uscire dagli errori
- Quando non ci sono più progetti da caricare, il pulsante "Altri" scompare senza dare informazioni che siamo arrivati alla fine dei progetti. L'utente deve intuirlo. `[GRAVITÀ: 2]`
- La pagina 404 Not Found è in inglese mentre il sito principale è in italiano. Permette inoltre di tornare alla home del sito ma non alla pagina precedente. `[GRAVITÀ: 1]`
	- ![[Screenshot 2026-10-12 alle 18.28.01.png]]
- Quando andiamo nella ricerca globale e inseriamo un progetto non esistente, non ci viene notificato ma appare semplicemente una pagina vuota.  `[GRAVITÀ: 5]`
	- ![[Screenshot 2026-10-12 alle 18.27.29.png]]
### E10. Aiuto e documentazione
Positivo:
- Sopra la navbar c'è un rimando a FAQ e come funziona oltre ai contatti

Criticità:
- **Nessun testo introduttivo** del progetto FundsTo: non si spiega che UniTo **raddoppia i fondi** dei progetti che raggiungono l'obiettivo (informazione presente solo nella scheda Partnership e nelle schede progetto), il rimando a come funzione FundsTO, né il modello "tutto o niente" in caso non venga raggiunto l'obiettivo. È un'informazione che motiva la donazione e andrebbe vicina alla lista. `[GRAVITÀ: 2]`, questo è un problema solo se arrivi alla pagina senza aver letto Partnership e Come Funziona interamente.
- Nessun contatto UniTo in questa pagina. `[GRAVITÀ: 2]`

---
