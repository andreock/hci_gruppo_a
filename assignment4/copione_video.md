# Copione video · Assignment 4 · Gruppo A

**Durata prevista: circa 9 minuti.** Il video segue l'ordine della relazione e ogni parte ha un solo speaker.

> **Attenzione:** i valori tra `[QUADRE]` vengono dalle sessioni con gli utenti. Oggi i CSV in `dati/` contengono ancora il dataset sintetico di collaudo: completate queste parti solo con i dati reali. Sono invece già definitivi, perché misurati sul sito, i task, le misure del re-design e le modifiche implementate.

## 1. Andrea Canale: introduzione, ispezione preliminare e protocollo (~2,5 min)

*A schermo: home di ideaBlume, poi la scheda dell'osservatore del kit (pagina di T3 con le ipotesi) e la tabella dei partecipanti nella relazione.*

> Ciao, siamo il Gruppo A: Andrea Canale, Antonio Fallea, Alexandru Ioan Chindris e Lorenzo Rizzolo. In questo video presentiamo il test di usabilità su **ideaBlume**, il prototipo di crowdfunding per la ricerca dell'Università di Torino che abbiamo progettato nell'Assignment 2 e reso accessibile nell'Assignment 3. Abbiamo seguito l'approccio "in svendita" di Steve Krug: pochi utenti, compiti concreti, think-aloud e nessun laboratorio.
>
> Prima di incontrare gli utenti abbiamo fatto un'**ispezione dei quattro percorsi** che avremmo testato. Per ognuno abbiamo scritto il **percorso ottimale**, cioè il numero minimo di azioni: per esempio 2 per trovare uso dei fondi e regola "tutto o niente", 9 per completare una donazione. Poi lo abbiamo ripercorso passo per passo su telefono e computer, chiedendoci a ogni schermata se l'utente capisce che cosa fare e che cosa succederà. Così abbiamo trovato **sette problemi**, da P1 a P7, e li abbiamo misurati sul sito: larghezze in pixel, clic necessari, passo in cui compare il totale.
>
> Un esempio: su telefono il riepilogo dell'ultimo passo della donazione esce dallo schermo. Gli strumenti automatici dell'Assignment 3 non l'avevano visto, perché analizzavano le pagine così come si caricano, mentre quel passo viene costruito dallo script con i dati inseriti dall'utente. È un limite tipico della valutazione automatica: controlla il codice, non il percorso.
>
> I sette problemi non li abbiamo dati per buoni: sono diventati **ipotesi da verificare**. Nella scheda dell'osservatore ogni task ha le sue ipotesi e le domande su cosa guardare, così durante la sessione si annota subito se il problema si presenta, e il test ci dice quanto conta davvero. Quello che emerge e non era nelle ipotesi lo segniamo a parte come problema nuovo.
>
> Abbiamo anche fissato in anticipo le **regole di conteggio**, per evitare che ogni osservatore decidesse a modo suo. È un **errore** ogni azione che allontana dall'obiettivo, come una pagina o un filtro sbagliato; scorrere e leggere non lo sono. È un **blocco** restare almeno 30 secondi senza azioni utili. Se il facilitatore dà un suggerimento, l'esito è al massimo "successo con aiuto". Il **tempo limite** è tre volte quello di un esperto, che abbiamo cronometrato su di noi: 3 minuti per T1, 7 per T3.
>
> Gli utenti sono **otto**, da Utente 1 a Utente 8, anonimi e con profili diversi: età da [FASCIA MIN] a [FASCIA MAX], competenza digitale da [MIN] a [MAX] su 5, familiarità col crowdfunding da [chi non l'aveva mai sentito] a [chi aveva già donato]. [N] sessioni in presenza e [N] da remoto, registrate dopo il consenso. In ogni sessione un **facilitatore** consegnava i task senza dire dove cliccare e un **osservatore** compilava la scheda; ognuno di noi ha condotto due sessioni e ne ha osservate due. Gli utenti hanno provato la versione dell'Assignment 3, cioè il sito prima del re-design.

## 2. Antonio Fallea: task e risultati quantitativi (~1,5 min)

*A schermo: i cartoncini dei task dal kit, poi la tabella sessioni e i grafici della relazione.*

> Abbiamo dato quattro task, descrivendo sempre l'obiettivo e mai il percorso:
>
> - **T1, esplorare le campagne**: trovare la raccolta aperta più lontana dal suo obiettivo. La risposta è "Aria aperta", con 2.350 euro su 5.000.
> - **T2, approfondire un progetto**: capire come verranno usati i fondi e che cosa succede alla donazione se l'obiettivo non viene raggiunto.
> - **T3, donare**: 30 euro al progetto sulle api, con la ricompensa, in forma anonima e con Satispay.
> - **T4, proporre un'idea** come rappresentante di un'associazione.
>
> Per ogni utente e task abbiamo registrato l'esito (successo, successo con aiuto o fallimento), il tempo, gli errori, le richieste di aiuto e i blocchi, con le regole che ha appena descritto Andrea.
>
> In tutto il tasso di successo autonomo è stato [X]%. Il task più facile è stato [T?], completato da [N] utenti su 8 in un tempo medio di [X] secondi. Il più difficile è stato **[T?]**, con [N] fallimenti e [N] richieste di aiuto.

*(Commentare il grafico: chi ha faticato di più, e se il dispositivo, cioè smartphone o computer, ha fatto differenza.)*

## 3. Alexandru Ioan Chindris: dati qualitativi, SUS e problemi (~2 min)

*A schermo: le citazioni, il grafico SUS, la tabella dei problemi con la gravità.*

> Oltre ai numeri ascoltavamo quello che gli utenti dicevano ad alta voce. Le frasi più ricorrenti sono state: *"[CITAZIONE REALE 1]"*, *"[CITAZIONE REALE 2]"*.
>
> Alla fine ogni utente ha compilato il questionario **SUS**. Il punteggio medio è [X] su 100, quindi [sopra o sotto] la soglia di 68, con valori da [MIN] a [MAX]. Nella breve intervista finale a molti sono piaciuti [TEMA], mentre le critiche più frequenti riguardavano [TEMA].
>
> Abbiamo poi confrontato le ipotesi dell'ispezione con quello che è successo nelle sessioni e classificato i problemi con la scala di gravità di Nielsen da 0 a 4, combinando impatto e persistenza.
>
> - **Gravità 3**: P1, su telefono il riepilogo della donazione esce dallo schermo. P2, il totale con la commissione si scopre solo all'ultimo passo. P3, la regola "tutto o niente" è nascosta dietro un pulsante. P6, i moduli per chi propone non dicono a chi sono rivolti.
> - **Gravità 2**: P4, la percentuale nelle schede è poco leggibile. P5, i filtri occupano la prima schermata. P7, su telefono l'intestazione spinge in basso il modulo.
> - [Eventuali problemi nuovi dal test, con la loro gravità.]

*(Una citazione per T2 e una per T3 vanno bene. Rivedete le gravità con i dati reali: un problema che nessuno ha incontrato va abbassato.)*

## 4. Lorenzo Rizzolo: re-design e conclusioni (~3 min)

*A schermo: le schermate prima/dopo della relazione oppure, meglio, una demo dal vivo sulla versione assignment4.*

> Passiamo al re-design. Per ogni problema mostriamo il prima e il dopo.
>
> **Donazione (T3).** Il problema più sentito era il costo nascosto (P2). Adesso c'è un riquadro **"La tua donazione"** sempre visibile, che aggiorna donazione, commissione e totale a ogni scelta: il totale si legge dal passo 1 invece che dal passo 5. Su computer è una colonna laterale, su telefono una striscia sotto l'indicatore dei passi.

*(Demo: scegliere 30 euro e mostrare l'intervallo da 30 a 30,89 euro, poi scegliere Satispay e mostrare la cifra esatta.)*

> Su telefono il riepilogo usciva dallo schermo (P1): la pagina era larga 416 pixel su 375 e 8 valori erano tagliati. Ora i valori vanno a capo e non se ne perde nessuno. Abbiamo anche ridotto l'indicatore dei passi da 136 a 40 pixel (P7).
>
> **Pagina progetto (T2).** La regola "tutto o niente" (P3) adesso è scritta sotto il pulsante "Sostieni il progetto": se l'obiettivo non viene raggiunto, la donazione viene restituita. Prima serviva un clic, ora nessuno.
>
> **Elenco progetti (T1).** La percentuale ora è accanto alla barra, a 18 pixel in grassetto (P4). Ricerca e ordinamento sono in vista e gli altri filtri sono compatti (P5): su telefono la prima scheda parte da 583 pixel invece che da 1047, quindi i progetti si vedono già nella prima schermata.
>
> **Proporre un'idea (T4).** La candidatura e il modulo di collaborazione hanno ora un avviso **"Per chi è questo modulo"** che rimanda all'altro (P6). In Contatti, se si sceglie "Proporre un progetto", compare un suggerimento con i due moduli.
>
> Dopo le modifiche abbiamo verificato che i quattro task si completano ancora, che axe-core non trova violazioni su 50 pagine in entrambi i temi, che tutti i 105 percorsi funzionano e che non c'è scorrimento orizzontale tra 320 e 1280 pixel.
>
> In conclusione, il test ci ha mostrato cose che euristiche e strumenti automatici non vedevano, soprattutto sulla fiducia nei pagamenti e sulla chiarezza di chi può proporre un progetto. Come passo successivo faremmo un secondo giro rapido con tre persone nuove sulla versione aggiornata. Grazie per l'attenzione.

## Consigli per la registrazione

- Ogni speaker registra la propria parte col microfono e la condivisione schermo su OBS, poi si montano i pezzi.
- Lorenzo fa la demo dal vivo sulla versione `…/anteprime/assignment4/`, che rende meglio delle schermate statiche.
- Non leggete il testo parola per parola: usatelo come traccia.
