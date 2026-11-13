"""Definizione unica dei 4 task: la usano sia il kit da stampare sia la relazione."""

URL_TEST = "https://andreock.github.io/hci_gruppo_a/anteprime/assignment3/"
URL_DOPO = "https://andreock.github.io/hci_gruppo_a/anteprime/assignment4/"
DATI_FINTI = "Maria Rossi · maria.rossi@example.com · telefono 011 555 0100"

TASK = [
    {
        "id": "T1", "titolo": "Esplorare le campagne", "percorso": "Esplorazione dell'elenco dei progetti",
        "scenario": "Hai sentito parlare di ideaBlume, il sito con cui l'Università di Torino raccoglie fondi per la ricerca. "
                    "Vuoi dare una mano a chi ne ha più bisogno: tra le raccolte ancora aperte, trova quella che è più indietro "
                    "rispetto alla cifra che deve raggiungere. Dimmi di quale progetto si tratta e quanto ha raccolto finora.",
        "successo": "L'utente indica «Aria aperta» (sensori per lo smog vicino alle scuole) e la cifra raccolta, € 2.350 su € 5.000 (47%).",
        "ottimale": "Home → Progetti → Stato «In corso» → Ordina per «Più lontani dall'obiettivo» → primo risultato (3 azioni). "
                    "È valido anche il confronto a occhio delle 4 schede in corso nella home.",
        "errori": "Indicare un progetto concluso; indicare il progetto con la scadenza più vicina; scambiare la cifra raccolta con l'obiettivo.",
        "osservare": ["Usa l'elenco «Progetti» o resta sulla home?", "Usa l'ordinamento, i filtri oppure confronta le schede a occhio?",
                      "Capisce la differenza tra «in corso», «obiettivo raggiunto» e «conclusa»?", "Legge la percentuale o la cifra in euro? La trova subito nelle schede? (ipotesi P4)",
                      "Aprendo l'elenco vede subito dei progetti o solo i filtri? Quanto scorre? (ipotesi P5)"],
    },
    {
        "id": "T2", "titolo": "Approfondire un progetto", "percorso": "Lettura della pagina di un progetto",
        "scenario": "Un'amica ti ha consigliato il progetto che studia i virus respiratori nei neonati. Prima di decidere se donare "
                    "vuoi capire due cose: per che cosa verranno spesi i soldi e che cosa succede alla tua donazione se la raccolta "
                    "non arriva alla cifra prevista. Trova queste informazioni e raccontamele.",
        "successo": "L'utente apre «Proteggere i neonati dai virus respiratori», cita almeno due voci di spesa della tabella "
                    "«Come useremo i fondi» (reagenti € 3.800, kit per i tamponi € 1.500, analisi statistica € 2.000, guida e incontri € 700) "
                    "e dice che la donazione viene restituita (regola «tutto o niente»).",
        "ottimale": "Home → scheda del progetto in evidenza → indice «Come useremo i fondi» (2 azioni); la regola «tutto o niente» "
                    "è nel riquadro «Stato della raccolta», dentro una spiegazione che si apre con un clic.",
        "errori": "Aprire un altro progetto; rispondere a memoria senza trovare l'informazione; confondere il raddoppio dell'Ateneo con la restituzione.",
        "osservare": ["Come arriva al progetto: scheda in evidenza, ricerca, elenco?", "Usa l'indice «In questa pagina» o scorre?",
                      "Apre la spiegazione «Che cosa significa tutto o niente?» o cerca altrove (FAQ, Come funziona)? (ipotesi P3)",
                      "Capisce il raddoppio dell'Ateneo senza che gli venga chiesto?"],
    },
    {
        "id": "T3", "titolo": "Simulare una donazione", "percorso": "Donazione in 5 passi",
        "scenario": "Hai deciso di sostenere il progetto sulle api del Piemonte con 30 euro, e ti piacerebbe ricevere in cambio ciò che "
                    "il gruppo offre per questa cifra. Non vuoi che il tuo nome sia visibile sul sito e paghi con Satispay. "
                    "Usa i dati scritti sul cartoncino, non i tuoi. Completa la donazione e dimmi quanto hai speso in tutto.",
        "successo": "L'utente arriva alla pagina di conferma con il codice di riferimento, con ricompensa «Adotta un'arnia virtuale», "
                    "nome «Anonimo», metodo Satispay, e dice il totale: € 30,89 (€ 30 + € 0,89 di commissione).",
        "ottimale": "Pagina «Alveari sani» → «Scegli € 30» → 5 passi (importo, dati, privacy, pagamento, riepilogo) → «Paga ora» (9 clic più 3 campi).",
        "errori": "Donazione libera senza ricompensa; nome lasciato visibile; metodo di pagamento diverso; rispondere «30 euro» senza notare la commissione; "
                  "errori di validazione all'invio di un passo.",
        "osservare": ["Parte dalla ricompensa o dal pulsante «Sostieni il progetto»?", "A quale passo scopre la commissione e il totale? Come reagisce? (ipotesi P2)",
                      "Se usa un telefono o una finestra stretta: legge tutto il riepilogo finale o è tagliato? (ipotesi P1, P7)",
                      "Lascia campi vuoti? Capisce i messaggi d'errore? (ipotesi P8)",
                      "Capisce la scelta tra nome visibile e donazione anonima?", "Si accorge di essere arrivato alla fine (conferma, codice)?",
                      "Usa «Indietro» o «Modifica»? I dati restano?"],
    },
    {
        "id": "T4", "titolo": "Proporre un'idea", "percorso": "Proposta di collaborazione da un ente esterno",
        "scenario": "Fai parte di un'associazione di quartiere, «Acqua Chiara», che vorrebbe far analizzare la qualità dell'acqua delle "
                    "fontane della zona con l'aiuto dell'università. Scopri se un'associazione come la tua può portare un'idea su ideaBlume e, "
                    "se sì, invia la proposta. Poi dimmi entro quando dovreste ricevere una risposta.",
        "successo": "L'utente invia il modulo di collaborazione per enti esterni, vede «Proposta ricevuta» e riferisce il tempo di risposta: 10 giorni lavorativi.",
        "ottimale": "Home → «Proponi un progetto» → «Proponi una collaborazione» → modulo (5 campi obbligatori e consenso) → «Invia la proposta» (4 clic più i campi).",
        "errori": "Compilare la candidatura al programma (riservata a chi fa ricerca in UniTo); usare il modulo «Scrivici» dei contatti; "
                  "concludere che un'associazione non può proporre.",
        "osservare": ["Dove cerca per prima cosa: menu, home, footer, contatti?", "Distingue «candidatura» (ricercatori) da «collaborazione» (enti)? Finisce nel modulo sbagliato o in «Contatti»? (ipotesi P6)",
                      "Legge la pagina «Proponi un progetto» o va subito al primo pulsante?", "Trova il tempo di risposta nella conferma?"],
    },
]

SUS = [
    "Penso che mi piacerebbe usare questo sito frequentemente.",
    "Ho trovato il sito inutilmente complesso.",
    "Ho trovato il sito facile da usare.",
    "Penso che avrei bisogno dell'aiuto di una persona esperta per usare questo sito.",
    "Ho trovato le varie funzioni del sito ben integrate.",
    "Ho trovato troppe incoerenze nel sito.",
    "Penso che la maggior parte delle persone imparerebbe a usare questo sito molto rapidamente.",
    "Ho trovato il sito molto macchinoso da usare.",
    "Mi sono sentito/a molto sicuro/a nell'usare il sito.",
    "Ho dovuto imparare molte cose prima di riuscire a usare il sito.",
]

DEFINIZIONI = [
    ("Tempo", "Secondi tra la fine della lettura del task ad alta voce e il momento in cui l'utente dice di aver finito (o rinuncia). Si misura con il cronometro o sulla registrazione."),
    ("Esito", "S = completato da solo, con la risposta giusta, entro il tempo limite. A = completato dopo un suggerimento del facilitatore. F = non completato: rinuncia, tempo limite superato oppure risposta sbagliata data come definitiva."),
    ("Errore", "Ogni azione che allontana dall'obiettivo: pagina o link sbagliato, filtro o opzione sbagliata, dato inserito nel campo sbagliato, invio di un modulo con errori di validazione. Passare il mouse, scorrere e leggere non sono errori."),
    ("Richiesta di aiuto", "L'utente chiede in modo esplicito al facilitatore che cosa fare. Si conta anche se il facilitatore risponde solo «Tu che cosa faresti?». Se viene dato un suggerimento, l'esito è al massimo A."),
    ("Blocco", "Almeno 30 secondi senza azioni utili, oppure una frase come «non so come andare avanti»."),
    ("Facilità percepita (SEQ)", "Subito dopo ogni task: «Quanto è stato facile?» da 1 (molto difficile) a 7 (molto facile)."),
]
