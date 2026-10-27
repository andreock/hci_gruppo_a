---
documento: persona_journey_prompts
persona: P04
journey: J04
nome: Tomás García
descrizione: donatore dall'estero
richiede: 00_contesto_comune_C00.md
modello_consigliato: Claude Opus 5.5 (claude-opus-5-5)
prompt_ids: [P04, J04]
---

# P04 · J04 · Tomás García, donatore dall'estero

Questo file contiene i due prompt della persona P04 e del suo journey J04. Il contesto comune non è ripetuto qui: si trova in [00_contesto_comune_C00.md](00_contesto_comune_C00.md).

**Come usarlo**
1. Apri una nuova conversazione con Opus 5.5 e incolla il prompt **C00** dal file del contesto comune.
2. Per la persona incolla il prompt **P04**; per il journey usa una nuova conversazione, incolla di nuovo C00 e poi il prompt **J04**. Puoi anche incollare C00 e il prompt singolo nello stesso messaggio.
3. Se la persona P04 è già stata generata, incolla il suo documento dentro `<persona_generata>` del prompt J04; altrimenti lascialo com'è.
4. Facoltativo: controlla l'output con il prompt V00 in [99_verifica_V00.md](99_verifica_V00.md).

Il testo da copiare è quello dentro ciascun blocco di codice.

<!-- BEGIN PROMPT id="P04" tipo="persona" persona="P04" richiede="C00" -->
````text
<prompt id="P04" tipo="persona" richiede="C00">

<obiettivo>
Genera la persona P04 usando il formato <formato_persona> e le regole del contesto C00.
</obiettivo>

<scheda_vincolante>
- Nome: Tomás García
- Età: 31
- Città: Madrid
- Occupazione: data analyst in una società di consulenza
- Famiglia: single
- Legame con UniTo: ha fatto l'Erasmus all'Università di Torino; è rimasto in contatto con alcuni ex compagni, uno dei quali ora è ricercatore UniTo
- Ruolo: donatore dall'estero, prima visita
- Dispositivo principale: laptop aziendale con Chrome impostato in inglese; smartphone Android
- Canali: app di messaggistica, sito da laptop, traduttore automatico del browser, PayPal, LinkedIn
- Familiarità digitale: 5/5; abituato a piattaforme di crowdfunding internazionali; confronta subito costi, commissioni e condizioni
- Accessibilità e contesto: italiano livello A2 (capisce le parole simili allo spagnolo, non le frasi lunghe né i messaggi di errore); inglese C1; spagnolo madrelingua
- Frequenza d'uso: prima visita; se coinvolto, torna per seguire gli aggiornamenti
- Motivazione: l'ex compagno gli manda il link a Mind the Climate; il clima è un tema che gli sta a cuore; vuole donare 50 € e condividere il progetto con gli amici conosciuti in Erasmus
- Archetipo suggerito: «l'ex Erasmus ancora legato a Torino»
</scheda_vincolante>

<problemi_assegnati>
- [S32 · H4 · G4] Passando all'inglese cambia solo la panoramica del progetto (rimanda alla sezione News); il resto resta in italiano; mancano SDG e formula «tutto o niente».
- [S12 · H2 · G2] Il sito non ha una traduzione completa e anche la pagina UniTo che spiega l'iniziativa non ha una versione inglese.
- [S14 · H3 · G3] «Scopri la guida dell'iniziativa» lo porta su unito.it senza avviso, su una pagina solo in italiano.
- [S40 · H8 · G2] Ogni ricompensa ripete il testo in italiano e in inglese: la lista diventa lunghissima.
- [S36 · H4 · G2] Nel box «SOSTIENI» l'inglese è in una posizione diversa in ogni progetto.
- [S41 · H9 · G4] Gli errori del modulo compaiono dopo l'invio e solo in italiano: non capisce che cosa correggere.
- [X01 · analisi preliminare, da verificare] «PayWay» è un nome che non conosce; le pagine non concordano sui metodi di pagamento.
- [X02 · analisi preliminare, da verificare] Le commissioni sono a carico del donatore e restano trattenute anche in caso di rimborso; l'informazione è solo nelle FAQ in italiano.
</problemi_assegnati>

<aspetti_positivi_da_includere>
- [S27 · positivo] Condivisione su vari canali e «Copia link»; ogni ricompensa dice quanti posti restano.
</aspetti_positivi_da_includere>

<indicazioni_specifiche>
- Mostra la strategia di aggiramento con il traduttore automatico del browser e i suoi limiti (testi nelle immagini, messaggi di errore dinamici, termini come «FAI TU»).
- Le sue aspettative derivano dalle convenzioni delle piattaforme internazionali (selettore di lingua, valuta, riepilogo dei costi): usa il concetto di coerenza con gli standard esterni (H4).
- Non trasformarlo in un critico del sito: è affezionato a Torino e vuole davvero donare.
</indicazioni_specifiche>

<controllo_finale>
Prima di rispondere verifica, senza scriverlo: (1) il front matter è completo e problemi_citati contiene esattamente gli ID citati nel testo; (2) ogni problema assegnato è citato almeno una volta; (3) i dati della scheda vincolante sono rispettati; (4) titoli e ordine delle sezioni sono identici a <formato_persona>.
</controllo_finale>

</prompt>
````
<!-- END PROMPT id="P04" -->

<!-- BEGIN PROMPT id="J04" tipo="journey_map" persona="P04" richiede="C00" -->
````text
<prompt id="J04" tipo="journey_map" persona="P04" richiede="C00">

<obiettivo>
Genera la journey map J04 della persona P04 usando il formato <formato_journey> e le regole del contesto C00.
</obiettivo>

<persona_generata>
[Se la persona P04 è già stata generata, sostituisci questa riga con il suo documento completo. Altrimenti lascia la riga così: userai la scheda sintetica.]
</persona_generata>

<scheda_sintetica_persona>
Tomás García, 31 anni, Madrid. Data analyst, ex studente Erasmus a Torino. Laptop con Chrome in inglese, smartphone Android. Familiarità 5/5, conosce le piattaforme di crowdfunding internazionali. Italiano A2, inglese C1, spagnolo madrelingua. Prima visita. Se il documento in <persona_generata> è presente, usa i suoi dettagli; in caso di conflitto valgono età, dispositivo, familiarità, accessibilità e frequenza di questa scheda.
</scheda_sintetica_persona>

<scenario>
Giovedì sera, a Madrid. Un ex compagno di corso, ora ricercatore UniTo, manda a Tomás il link a Mind the Climate con un messaggio in inglese. Tomás apre il link dal laptop. Obiettivo: capire il progetto e le regole, donare 50 € e condividere il progetto con gli amici conosciuti in Erasmus, sapendo che molti di loro non parlano italiano.
</scenario>

<fasi>
1. Ricezione del link. Canale: app di messaggistica.
2. Arrivo e ricerca della lingua. Canale: sito da laptop. Problemi: [S32 · H4 · G4], [S12 · H2 · G2].
3. Comprensione del progetto e delle regole, anche con il traduttore del browser. Problemi: [S32 · H4 · G4] (mancano SDG e «tutto o niente» in inglese), [S14 · H3 · G3].
4. Scelta della ricompensa. Problemi: [S40 · H8 · G2], [S36 · H4 · G2]. Positivo: [S27 · positivo] posti rimasti.
5. Compilazione del modulo e pagamento. Problemi: [S41 · H9 · G4], [X01 · analisi preliminare, da verificare], [X02 · analisi preliminare, da verificare].
6. Condivisione con la rete internazionale. Canali: LinkedIn, gruppo di messaggistica. Positivo: [S27 · positivo] condivisione. Dubbio: gli amici troveranno lo stesso problema di lingua ([S32 · H4 · G4]).
</fasi>

<indicazioni_specifiche>
- Rendi visibile il costo cognitivo del passaggio continuo tra lingue (attenzione selettiva e carico sulla memoria).
- Momento critico: fase 5, messaggio d'errore incomprensibile nel punto in cui sta pagando. Collegalo agli indicatori HEART Task success e Adoption (nuovi donatori dall'estero).
- Nelle note per il team indica che il problema non riguarda solo Tomás ma la capacità dei progetti di raccogliere fondi all'estero (osservazione già presente in slide 12).
</indicazioni_specifiche>

<controllo_finale>
Prima di rispondere verifica, senza scriverlo: (1) front matter completo e problemi_citati uguale agli ID citati; (2) tutti i problemi elencati nelle fasi sono citati; (3) le fasi della tabella coincidono con il front matter; (4) i punteggi della curva emotiva coincidono con la riga Emozioni; (5) ogni difficoltà ha un'opportunità corrispondente.
</controllo_finale>

</prompt>
````
<!-- END PROMPT id="J04" -->
