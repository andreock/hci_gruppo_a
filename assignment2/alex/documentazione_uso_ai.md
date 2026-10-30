# Documentazione dell'uso dell'AI e delle revisioni

## Ambito

Sono state sviluppate tre proto-personas ipotetiche (P01-P03) e tre user journey as-is (J01-J03). Il materiale non sostituisce ricerca con utenti: trasforma problemi di usabilità già individuati dal gruppo in ipotesi progettuali da verificare.

## Strumento e informazioni fornite

- Strumento: OpenAI Codex, modello GPT-5.
- Attività: generazione e revisione dei contenuti; controllo di coerenza tra persona e journey; verifica dei campi richiesti; produzione delle schede HTML.
- Contesto fornito: obiettivo dell'Assignment 2, catalogo dei problemi dell'analisi euristica, regole di genericità, template ufficiali del corso e schede vincolanti P01-P03.
- Vincoli principali: nessun riferimento a un servizio di crowdfunding reale; proto-personas chiaramente dichiarate; sei fasi per journey; emozioni da -2 a +2; ogni barriera associata a una soluzione; celle concise.

## Prompt principale usato

> Genera e raffina la scheda della proto-persona indicata usando esclusivamente i campi del template ufficiale. Mantieni invariati età, ruolo, dispositivo, familiarità digitale, accessibilità e frequenza. Trasforma i problemi assegnati in esperienze personali, senza citare ID interni o servizi reali. Costruisci poi un journey as-is coerente, con azioni, touchpoint, pensieri, emozioni motivate, barriere e opportunità concrete. Segnala come ipotesi tutto ciò che non deriva dal catalogo.

## Iterazione 1 - problemi individuati

| Documento | Esempio della prima formulazione | Problema | Richiesta di revisione |
|---|---|---|---|
| P01 | «Giuseppe è poco capace con la tecnologia.» | Formulazione stereotipata e centrata sul deficit. | Descrivere competenze, strategie e contesto; attribuire le difficoltà all'interfaccia. |
| J01 | «La pagina è confusa.» | Criticità generica, non osservabile e senza legame con una soluzione. | Esplicitare percentuali oltre il 100%, giorni negativi e apertura inattesa dei link. |
| P02 | «Sara vuole una donazione veloce.» | Non mostra attenzione divisa, rete debole e passaggio tra dispositivi. | Rendere visibili pause, una mano, interruzione e ripresa serale. |
| J02 | «Riprende sul laptop.» | Mancava la continuità cross-device e non era marcata come ipotesi. | Indicare dati da reinserire [IPOTESI] e collegarli a una soluzione di salvataggio. |
| P03 | «Davide ha bisogno di un sito semplice.» | Semplificazione paternalistica; non valorizza l'esperienza con tecnologie assistive. | Specificare navigazione per H, landmark, elenco link e sintesi ad alta velocità. |
| J03 | «Non vede il pallino rosso.» | Descrizione visiva impropria rispetto all'interazione con screen reader. | Descrivere lo stato non annunciato nel codice e il conseguente golfo della valutazione. |

## Iterazione 2 - raffinamenti applicati

### P01 e J01

- Il profilo è stato spostato dall'idea di «anziano inesperto» a quella di ex insegnante curioso, prudente e capace di strategie autonome.
- Il modello mentale di offerta o bonifico è stato contrapposto alla «ricompensa» per motivare una scelta progettuale concreta: importo libero evidente.
- La curva emotiva scende nella comprensione e nel pagamento, poi recupera grazie a conferma e contatto umano.
- La versione finale sostituisce «pagina confusa» con dati osservabili e soluzioni corrispondenti.

Prima: «Non capisce i numeri e si blocca.»

Finale: «Oltre 100%, giorni negativi e aperture inattese confondono lo stato e il tasto Indietro», associato a stato testuale, data naturale e ritorno preservato.

### P02 e J02

- Le difficoltà sono state trattate come limitazioni situazionali, non come incapacità personale.
- Il journey è diventato multicanale: social, smartphone, messaggistica, laptop ed email.
- Il momento di abbandono è legato a lentezza, errore tardivo e fine della pausa; la ripresa richiede continuità tra dispositivi.
- La versione finale distingue chiaramente importo libero e ricompense.

Prima: «Sara abbandona perché ha fretta.»

Finale: «Modulo lento ed errore soltanto dopo l'invio; i dati non sono salvati [IPOTESI]», associato a validazione immediata, bozza e link di ripresa.

### P03 e J03

- Il profilo è stato riscritto come utente esperto e critico, precisando scorciatoie e strategie di navigazione.
- Le barriere sono espresse in termini semantici: nomi accessibili, ruoli, stati, focus, gerarchia e alternative testuali.
- Il momento più critico è la campagna conclusa che conserva controlli attivi senza annunciare lo stato.
- È stato esplicitato il rischio reputazionale di un progetto sull'accessibilità presentato in modo inaccessibile.

Prima: «Davide non riesce a vedere che la campagna è finita.»

Finale: «Stato affidato a colore o simbolo; ricompense e importo restano attivi nella campagna conclusa», associato a etichetta annunciata e controlli disabilitati.

## Controllo finale

- Tutte le schede usano i campi e l'ordine dei template ufficiali.
- Età, dispositivi, familiarità, accessibilità e frequenza corrispondono alle schede vincolanti.
- Ogni journey contiene sei fasi coerenti con la persona.
- Ogni cella delle emozioni contiene emozione, punteggio e base ipotizzata.
- Ogni criticità ha una opportunità di miglioramento corrispondente.
- Le ipotesi non derivate dal catalogo sono marcate `[IPOTESI]`.
- Non sono riportati ID interni dell'analisi euristica nei documenti finali.
- Le tre personas restano differenziate per obiettivi, contesto, competenze e ostacoli.
