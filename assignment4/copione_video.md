# Copione video · Assignment 4 · Gruppo A

**Durata prevista: circa 9 minuti.** Il video segue l'ordine della relazione e ogni parte ha un solo speaker.

> **Attenzione:** i valori tra `[QUADRE]` vengono dalle sessioni con gli utenti. Oggi i CSV in `dati/` contengono ancora il dataset sintetico di collaudo: completate queste parti solo con i dati reali. Sono invece già definitivi, perché misurati sul sito, i task, le misure del re-design e le modifiche implementate.

## 1. Andrea Canale: introduzione e metodo (~2 min)

*A schermo: home di ideaBlume, poi la tabella dei partecipanti nella relazione.*

> Ciao, siamo il Gruppo A: Andrea Canale, Antonio Fallea, Alexandru Ioan Chindris e Lorenzo Rizzolo. In questo video presentiamo il test di usabilità su **ideaBlume**, il prototipo di crowdfunding per la ricerca dell'Università di Torino che abbiamo progettato nell'Assignment 2 e reso accessibile nell'Assignment 3.
>
> Fin qui avevamo valutato il sito con euristiche, personas e strumenti automatici. Questa volta l'abbiamo fatto provare a utenti veri, con un test "in svendita" alla Steve Krug: poche persone, compiti concreti, think-aloud e nessun laboratorio.
>
> Siamo in quattro, quindi abbiamo coinvolto **otto utenti**, da Utente 1 a Utente 8, tutti anonimi. Abbiamo cercato profili diversi: età da [FASCIA MIN] a [FASCIA MAX], competenza digitale da [MIN] a [MAX] su 5, e familiarità col crowdfunding che va da [chi non l'aveva mai sentito] a [chi aveva già donato]. [N] sessioni si sono svolte in presenza e [N] da remoto, su notebook, desktop e smartphone, registrando schermo e voce con OBS [o la piattaforma di videoconferenza] dopo aver raccolto il consenso.
>
> In ogni sessione c'erano due di noi. Il **facilitatore** leggeva il copione e consegnava i task senza mai dire dove cliccare. L'**osservatore** cronometrava, contava errori, aiuti e blocchi e annotava i commenti. Ognuno di noi ha condotto due sessioni e ne ha osservate due. Gli utenti hanno provato la versione dell'Assignment 3, così da misurare il sito prima del re-design.

## 2. Antonio Fallea: task e risultati quantitativi (~2 min)

*A schermo: i cartoncini dei task dal kit, poi la tabella sessioni e i grafici della relazione.*

> Abbiamo dato quattro task, descrivendo sempre l'obiettivo e mai il percorso:
>
> - **T1, esplorare le campagne**: trovare la raccolta aperta più lontana dal suo obiettivo. La risposta è "Aria aperta", con 2.350 euro su 5.000.
> - **T2, approfondire un progetto**: capire come verranno usati i fondi e che cosa succede alla donazione se l'obiettivo non viene raggiunto.
> - **T3, donare**: 30 euro al progetto sulle api, con la ricompensa, in forma anonima e con Satispay.
> - **T4, proporre un'idea** come rappresentante di un'associazione.
>
> Per ogni utente e task abbiamo registrato l'esito (successo, successo con aiuto o fallimento), il tempo, gli errori, le richieste di aiuto e i blocchi. Il tempo limite è tre volte quello di un esperto: per esempio 3 minuti per T1 e 7 per T3.
>
> In tutto il tasso di successo autonomo è stato [X]%. Il task più facile è stato [T?], completato da [N] utenti su 8 in un tempo medio di [X] secondi. Il più difficile è stato **[T?]**, con [N] fallimenti e [N] richieste di aiuto.

*(Commentare il grafico: chi ha faticato di più, e se il dispositivo, cioè smartphone o computer, ha fatto differenza.)*

## 3. Alexandru Ioan Chindris: dati qualitativi, SUS e problemi (~2 min)

*A schermo: le citazioni, il grafico SUS, la tabella dei problemi con la gravità.*

> Oltre ai numeri ascoltavamo quello che gli utenti dicevano ad alta voce. Le frasi più ricorrenti sono state: *"[CITAZIONE REALE 1]"*, *"[CITAZIONE REALE 2]"*.
>
> Alla fine ogni utente ha compilato il questionario **SUS**. Il punteggio medio è [X] su 100, quindi [sopra o sotto] la soglia di 68, con valori da [MIN] a [MAX]. Nella breve intervista finale a molti sono piaciuti [TEMA], mentre le critiche più frequenti riguardavano [TEMA].
>
> Abbiamo poi messo insieme i problemi e li abbiamo classificati con la scala di gravità di Nielsen da 0 a 4, combinando impatto e persistenza. Teniamo distinte due fonti. Sette problemi li avevamo già trovati con un'ispezione dei quattro percorsi e il test ci ha detto quanto contano davvero. Altri sono emersi solo dal test.
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
