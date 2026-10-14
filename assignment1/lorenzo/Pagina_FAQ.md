# Stato della UX della pagina "FAQ" di Ideaginger: analisi di massima secondo le 10 euristiche di Nielsen

**Pagina analizzata**: <https://www.ideaginger.it/faq.html> (pagina "FAQ" del sito Ideaginger / GINGER)
**Data**: 14/10/2026
**Come è stata svolta**: lettura del contenuto e della struttura della pagina (testi, titoli, link, testi alternativi, metadati), senza browser interattivo. Resa grafica, colori, comportamento JavaScript, tastiera, zoom e mobile **non sono stati osservati**: dove servono sono indicati con un placeholder.
**Riferimento metodologico**: `checklist_analisi_euristica.md` (sezione 5 per gli elementi da osservare, sezione 3 per la scala di gravità 0–4).

> **Come leggere i placeholder**
> - `[VERIFICA: …]` è un controllo da fare a mano sul sito, che può confermare, modificare o annullare l'osservazione.
> - `[SCREENSHOT: …]` è l'immagine da inserire nel report, con il problema evidenziato.
> - `[GRAVITÀ: x?]` è un valore provvisorio da confermare dopo la verifica (scala Nielsen 0–4). Dove la gravità non ha il punto interrogativo, l'osservazione si basa su ciò che è scritto nella pagina e non dipende dalla resa grafica.
> - Annotare per ogni verifica **browser, dispositivo, risoluzione e data** (checklist, sez. 8).

---

## 1. Che cos'è la pagina e a cosa serve

È la pagina di domande frequenti della piattaforma di crowdfunding Ginger. Serve a due pubblici diversi: **chi vuole lanciare un progetto** (progettisti) e **chi vuole donare** (sostenitori). Struttura rilevata, dall'alto:

1. barra di servizio (Faq, Contatti, Come funziona, Login progettista) e menu principale (icona, logo, Home, Cerca progetti, Lancia una campagna, Partner, Servizi);
2. blocco di navigazione che nel testo estratto precede il contenuto: Progetti (Sostienili ora, Per ispirarti, Tutti), 26 Categorie, 17 SDGs ONU, 25 Partner `[VERIFICA: è visibile a schermo come colonna laterale o compare solo dai menu a tendina "Cerca progetti" e "Partner"?]`;
3. elenco di link di servizio (Come funziona, Condizioni d'uso, Privacy, Cookies, Formazione, Chi Siamo, Contatti, Collaborazioni, FAQ);
4. titolo **FAQ** seguito da **25 domande/risposte** in sequenza, senza raggruppamenti visibili (sul crowdfunding in generale, budget e scadenza, pagamenti e commissioni, ricompense, selezione e fiducia nei progettisti, donazioni);
5. footer (Home, Chi siamo, Collaborazioni, Contatti, Login partner, Condizioni d'uso, Privacy, Cookies, Preferenze cookie, FAQ, social, blog "Il Gingerino", © 2013 - 2026).

Ogni voce è una domanda in forma di titolo seguita da una risposta in prosa, a volte lunga, con qualche elenco puntato (servizi GINGER, materiali per il progetto).

## 2. Giudizio complessivo provvisorio

La pagina **svolge il suo compito principale**: copre quasi tutte le domande che un progettista o un donatore può porsi, con domande scritte in linguaggio naturale e risposte sostanzialmente complete. I problemi principali sono di **organizzazione e efficienza** (25 domande in un'unica sequenza, senza indice, ricerca o separazione tra progettisti e donatori), di **coerenza dei contenuti** (informazioni sulle commissioni ripetute e non allineate, terminologia variabile, refusi) e di **leggibilità** (blocchi di testo molto lunghi, in particolare sulle commissioni di pagamento). Emergono anche aspetti tecnici che incidono sull'accessibilità (zoom bloccato su mobile, titolo della scheda del browser e metadati identici a quelli della home). Molti aspetti dipendono dalla resa a schermo e vanno verificati prima di assegnare le gravità definitive.

---

## 3. Analisi per euristica

### E1. Visibilità dello stato del sistema

**Positivo**
- Il titolo "FAQ" in testa al contenuto e il link "Faq" nella barra di servizio e nel footer rendono chiaro dove ci si trova.
- Le domande sono formulate come titoli, quindi è subito chiaro cosa si sta leggendo e dove inizia ogni risposta.

**Criticità**
- **Titolo della scheda del browser e metadati della home**: nei metadati la pagina riporta lo stesso `title`, la stessa descrizione e lo stesso `canonical` della home ("GINGER: la piattaforma di crowdfunding con il più alto tasso di successo in Italia!"). Chi ha più schede aperte, o trova la pagina tra i preferiti o nei risultati di ricerca, non può riconoscerla come pagina FAQ. `[SCREENSHOT: scheda del browser con il titolo]` `[GRAVITÀ: 2?]`
- **Nessun indicatore di posizione nella pagina**: con 25 voci e una pagina molto lunga l'utente non sa a che punto si trova né quante domande restano. `[GRAVITÀ: 2?]`

### E2. Corrispondenza tra sistema e mondo reale

**Positivo**
- Le domande sono scritte come le farebbe un utente ("Come so che nessuno ruberà la mia idea?", "Cosa succede alla scadenza del progetto?").
- La domanda "Cos'è il crowdfunding?" spiega il concetto partendo dall'etimologia e dall'esempio concreto di chi ha un'idea e chiede sostegno in cambio di una ricompensa.

**Criticità**
- **Gergo non spiegato**: "gingerizzato", "in itinere", "keep it all", "budget", "PayWay", "progettista" e "ricompense" compaiono senza definizione o con spiegazioni parziali. "Keep it all" è accennato dentro la risposta sul budget, senza spiegare cosa cambia per donatore e progettista. `[GRAVITÀ: 2]`
- **"Idea geniale" ripetuto**: tono promozionale ("la tua idea geniale", "una volta gingerizzato") che può risultare poco serio per chi cerca informazioni su un pagamento o su un rimborso. `[GRAVITÀ: 1]`
- **Spiegazioni troppo lunghe per concetti semplici**: la risposta "Cos'è il crowdfunding?" è un unico paragrafo. Chi arriva sul sito per donare non ha bisogno dell'etimologia. `[GRAVITÀ: 1]`

### E3. Controllo e libertà dell'utente

**Positivo**
- Il link a "Come funziona" e a "Contatti" è sempre raggiungibile dalla barra di servizio.

**Criticità**
- **Nessun indice o ancore interne**: per arrivare a una domanda in fondo (ad esempio "Perché PayPal o PayWay hanno rifiutato il mio pagamento?", la numero 25) bisogna scorrere tutta la pagina. Non si può nemmeno condividere o salvare il link a una singola risposta. `[VERIFICA: ogni domanda ha un'ancora nell'URL? Esiste un pulsante "torna su"?]` `[GRAVITÀ: 3]`
- **Link esterno a PayPal**: l'ultima risposta rimanda a una pagina del sito PayPal. `[VERIFICA: si apre nella stessa scheda o in una nuova? L'utente può tornare alla FAQ senza perdere la posizione?]` `[GRAVITÀ: 1?]`
- **Breadcrumb assente**: dato che la pagina non è profonda, il problema è contenuto. `[GRAVITÀ: 1]`
- **Ricerca e filtraggio**: la pagina non offre strumenti per cercare o filtrare le domande. `[GRAVITÀ: 2]`

### E4. Consistenza e standard

**Positivo**
- Tutte le voci hanno la stessa struttura (domanda come titolo, risposta in testo semplice). `[GRAVITÀ: 0]`

**Criticità**
- **Informazioni sulle commissioni non allineate tra due risposte**: la risposta "Viene applicata una commissione alle singole transazioni?" indica per PayPal solo 1,8% + 0,35 €. La risposta "GINGER trattiene una percentuale…?" aggiunge che dal 24/06/2025 PayPal applica 1,2% + 0,35 € per le carte Visa, Mastercard, CUP, Diners e Discover e 3,5% per American Express. Un utente che legge solo la prima ottiene un'informazione incompleta, e chi le legge entrambe non capisce quale vale. `[GRAVITÀ: 3]`
- **Contenuto duplicato**: l'elenco delle carte con commissione PayWay all'1,8% e al 2% è copiato identico in due risposte, ed entrambe ripetono che Ginger non trattiene percentuali. ("Viene applicata una commissione alle singole transazioni?", "GINGER trattiene una percentuale sui soldi che raccolgo? Ottiene qualche diritto sulla proprietà dell’idea?") `[GRAVITÀ: 2]`
- **Terminologia variabile per lo stesso ruolo**: chi lancia il progetto è "progettista", "proponente", "creativo" o "tu"; chi dona è "sostenitore", "finanziatore" o "donatore"; il progetto è "idea", "campagna" o "progetto". `[GRAVITÀ: 2]`
- **Nome del servizio non uniforme**: "GINGER", "ideaginger.it", "Idea Ginger" e "Ginger" compaiono in modo intercambiabile (la prima domanda spiega che GINGER è un team di professionisti e che ideaginger.it è la piattaforma, ma poi le risposte usano i due nomi senza distinguerli). `[GRAVITÀ: 1]`
- **Refusi e errori ortografici**: "modalitè" e "professionalitè" (con la è accentata al posto di "à"), "Si" senza accento nelle risposte affermative ("Si, se in itinere…", "Si, lo staff di GINGER…"), "una commissione addebita al progettista" al posto di "addebitata", "Puoi sotenerli ora" nel titolo del link "Sostienili ora". Minano la credibilità di una pagina che parla di soldi e fiducia. `[GRAVITÀ: 2]`
- **Gerarchia dei titoli**: nel contenuto estratto compaiono prima alcuni titoli `<h3>` ("PROGETTI", "CATEGORIE", "SDGs ONU", "PARTNER") e solo dopo l'unico `<h1>` "FAQ" con le domande come `<h2>`. `[VERIFICA: con un'estensione tipo HeadingsMap o DevTools]` `[GRAVITÀ: 2?]` (rilevante anche per l'accessibilità)
- **Link riconoscibili**: `[VERIFICA: i link nel testo (es. quello a PayPal) sono distinguibili dal testo normale senza passarci sopra? Il cambio di aspetto al passaggio del mouse è chiaro?]` `[GRAVITÀ: 2?]`

### E5. Prevenzione dell'errore

- **Rimborso con addebito delle spese di transazione**: due risposte (commissione sulle transazioni e scadenza) dicono che se il progetto non raggiunge il budget la donazione viene restituita "con l'addebito delle spese di transazione". È un'informazione che un donatore dovrebbe conoscere **prima** di donare, ma è sepolta in una risposta lunga pensata per i progettisti. Il donatore rischia di perdere una piccola parte dell'importo senza saperlo. `[GRAVITÀ: 3]`
- **Modello "tutto o niente" e "keep it all"**: la risposta sul budget presenta insieme il modello standard (fondi restituiti se non si raggiunge l'obiettivo) e il caso particolare "keep it all" valutato dal team. Un donatore non può capire dalla FAQ quale dei due modelli vale per il progetto che sta per sostenere. ("Cos’è il budget?") `[VERIFICA: la pagina progetto indica il modello adottato?]` `[GRAVITÀ: 2]`
- **Domande per donatori e progettisti mescolate**: chi vuole solo donare deve distinguere da solo le risposte che lo riguardano. Il solo accenno a "non serve iscriversi" per donare è dentro la seconda risposta. `[GRAVITÀ: 2]`
- **"Lancia una campagna" non linkato nelle risposte che lo citano**: la risposta "Come faccio a sottoporvi il mio progetto?" dice di entrare nella pagina "Lancia una campagna" dopo aver costruito il proprio Profilo, ma non c'è un link diretto nella risposta. Lo stesso vale per "iscriviti" nella risposta "Come utilizzare ideaginger.it?". `[GRAVITÀ: 2]`
- **Limite alla modifica del progetto**: si può integrare il progetto solo tramite "News", e "modifiche che cambieranno la natura strutturale del progetto" non sono ammesse, senza esempi concreti di cosa sia ammesso e cosa no. Il progettista potrebbe scoprire il limite dopo la pubblicazione. `[GRAVITÀ: 1]`

### E6. Riconoscimento più che ricordo

Positivo:
- Le domande sono titoli ben visibili: l'utente può scorrere e riconoscere quella che gli interessa senza dover ricordare termini tecnici. `[GRAVITÀ: 0]`
- Il link a "Come funziona" in alto rimanda a un contenuto complementare. `[GRAVITÀ: 0]`

Criticità:
- **Nessun raggruppamento per tema o per profilo** (progettista / donatore, pagamenti, ricompense, fiducia): l'utente deve leggere tutti i titoli per capire se la sua domanda è presente. `[GRAVITÀ: 3]`
- **Ordine delle domande non per priorità**: le domande più urgenti per chi sta donando ("Perché PayPal o PayWay hanno rifiutato il mio pagamento?") sono l'ultima voce della pagina, mentre le prime riguardano concetti generali. `[GRAVITÀ: 2]`

### E7. Flessibilità ed efficienza d'uso

- **Nessun filtro, indice o scorciatoia**: per trovare una risposta l'unica strategia è scorrere o usare la ricerca del browser (Ctrl+F). Con 25 domande il costo è moderato, ma cresce con ogni nuova voce. `[GRAVITÀ: 3]`
- **Risposte lunghe nella parte iniziale**: le risposte sulle commissioni, sui benefici e sulla buona fede dei progettisti superano molte righe di testo continuo, senza un riassunto in testa. `[GRAVITÀ: 2]`
- `[VERIFICA – mobile/responsive (DevTools e smartphone reale): lunghezza della pagina, menu hamburger, dimensione dei target touch (almeno 24×24 px), dove finisce il blocco di navigazione laterale]`
- **Navigazione da tastiera:** contenuto raggiungibile solo dopo la navigazione: premendo Tab dall’inizio della pagina, il focus attraversa prima la barra di servizio e il menu, poi l’elenco delle 26 categorie, e solo dopo arriva alle domande della FAQ. Non c’è un collegamento “vai al contenuto” per saltare la navigazione. Chi usa solo la tastiera (o uno screen reader) deve premere Tab decine di volte a ogni apertura della pagina prima di arrivare al contenuto. `[GRAVITÀ: 3]`

### E8. Estetica e design minimalista

Positivo:
- Il testo delle risposte è scritto in modo diretto e senza elementi grafici superflui nella parte di contenuto.
- Qualche elenco puntato (servizi, materiali richiesti per il progetto) rompe la prosa e rende più leggibili i punti chiave. 


Criticità:
- **Muri di testo**: diverse risposte (benefici, buona fede dei progettisti, commissioni, crowdfunding) sono paragrafi molto lunghi, senza grassetti, sottotitoli o elenchi. `[GRAVITÀ: 3]`
- **Elenco di 13 carte ripetuto due volte**: occupa molto spazio e interrompe la lettura della parte che interessa davvero (la percentuale). Basterebbe una tabella con commissioni per metodo di pagamento. `[GRAVITÀ: 2]`


### E9. Aiutare a riconoscere, diagnosticare e uscire dagli errori

Positivo:
- La pagina ha una risposta dedicata ai pagamenti rifiutati, con le cause più comuni (dati inseriti male, credito esaurito, carta non supportata).
- Per segnalare problemi con un progettista viene indicata una mail (ginger@ideaginger.it).

Criticità:
- **Risposta sul pagamento rifiutato incompleta**: spiega i motivi ma non dice cosa fare dopo (riprovare, usare un altro metodo come il bonifico, contattare qualcuno). Il link porta alla guida di PayPal, mentre per PayWay non viene dato nessun riferimento. `[GRAVITÀ: 3]`
- **Nessun contatto per i donatori**: la mail compare solo nella risposta sui progettisti inaffidabili e non nella risposta sui pagamenti. `[GRAVITÀ: 2]`
- **Nessuna chiusura del tipo "Non hai trovato la risposta?"** con un rimando a Contatti in fondo alla lista. `[GRAVITÀ: 2]`
- **Errori nella pagina stessa**: refusi e informazioni non allineate sulle commissioni (vedi E4) possono generare dubbi e richieste di assistenza evitabili. `[GRAVITÀ: 2]`
- **Pagina 404 in inglese**: digitando un indirizzo errato (es. /faqs.html) compare una pagina “Not Found” in inglese, mentre il resto del sito è in italiano. L’utente italiano che sbaglia indirizzo o segue un link rotto trova un messaggio d’errore in una lingua diversa da quella del sito. `[SCREENSHOT: pagina 404]` `[GRAVITÀ: 1–2?]`

### E10. Aiuto e documentazione

Positivo:
- La pagina è già di per sé la documentazione di aiuto, ed è raggiungibile da barra di servizio e footer, con un link a "Come funziona" e "Contatti" accanto.
- Copre un'ampia gamma di temi: commissioni, ricompense, scadenza, rimborsi, visibilità dei sostenitori, selezione dei progetti. 

Criticità:
- **Argomenti utili non presenti** (rilevato dal contenuto): tempi con cui il progettista riceve i fondi dopo la scadenza e tempi del rimborso al donatore, come funziona la donazione con bonifico (passaggi), come ricevere una ricevuta o capire se la donazione è detraibile, come gestire spedizioni e consegna delle ricompense, a chi rivolgersi se la ricompensa non arriva. `[GRAVITÀ: 2]`
- **Nessuna data di ultimo aggiornamento**: la pagina cita una data precisa per le commissioni PayPal (24/06/2025) ma non indica quando è stata aggiornata nel complesso, quindi l'utente non sa se le informazioni sono attuali. `[GRAVITÀ: 2]`
- **Tono di alcune risposte poco pratico**: ad esempio "Come so che nessuno ruberà la mia idea?" risponde con un ragionamento generale ma non con una tutela concreta (a chi spetta la proprietà dei contenuti, cosa fa Ginger se qualcuno copia un progetto). `[GRAVITÀ: 1]`
- **Collegamenti incrociati scarsi**: le risposte non rimandano tra loro (ad esempio da "Cos'è il budget?" a "Cosa succede alla scadenza del progetto?") né a pagine di approfondimento come "Come funziona" o "Condizioni d'uso". `[GRAVITÀ: 1]`

---