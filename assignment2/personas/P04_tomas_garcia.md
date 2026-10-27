---
documento: persona_journey_prompts
versione: 3 (personas generiche)
persona: P04
journey: J04
nome: Tomás García
descrizione: ex Erasmus che dona dall'estero
richiede: 00_contesto_comune_C00.md
modello_consigliato: Claude Opus 5.5 (claude-opus-5-5)
prompt_ids: [P04, J04]
---

# P04 · J04 · Tomás García, ex Erasmus che dona dall'estero

Questo file contiene i due prompt della persona P04 e del suo journey J04. Il contesto comune non è ripetuto qui: si trova in [00_contesto_comune_C00.md](00_contesto_comune_C00.md).

**Come usarlo**
1. Apri una nuova conversazione con Opus 5.5, incolla il prompt **C00** dal file del contesto comune e allega il template del corso: [scheda_persona.pdf](template/scheda_persona.pdf) per la persona, [scheda_user_journey.pdf](template/scheda_user_journey.pdf) per il journey.
2. Per la persona incolla il prompt **P04**; per il journey usa una nuova conversazione, incolla di nuovo C00 e poi il prompt **J04**. Puoi anche incollare C00 e il prompt singolo nello stesso messaggio.
3. Se la persona P04 è già stata generata, incolla il suo documento dentro `<persona_generata>` del prompt J04; altrimenti lascialo com'è.
4. Facoltativo: controlla l'output con il prompt V00 in [99_verifica_V00.md](99_verifica_V00.md).

Il testo da copiare è quello dentro ciascun blocco di codice.

<!-- BEGIN PROMPT id="P04" tipo="persona" persona="P04" richiede="C00" -->
````text
<prompt id="P04" tipo="persona" richiede="C00">

<obiettivo>
Genera la scheda della persona P04 usando il formato <formato_persona> e le regole del contesto C00. Racconta la persona e il suo rapporto con il crowdfunding in generale, senza riferimenti ad app, piattaforme, enti o progetti reali.
</obiettivo>

<scheda_vincolante>
- Nome: Tomás García
- Età: 31
- Città: Madrid
- Occupazione: data analyst in una società di consulenza
- Famiglia: single, vive in un appartamento condiviso con un amico
- Vita quotidiana: calcetto il martedì, viaggi low cost, segue la politica ambientale europea, è ancora in contatto con gli amici conosciuti durante l'Erasmus a Torino
- Valori: impegno per il clima, legame con le amicizie internazionali, trasparenza
- Ruolo: donatore dall'estero, prima volta su quell'app
- Dispositivo principale: laptop aziendale con browser impostato in inglese; smartphone Android
- Familiarità digitale: 5/5; abituato alle piattaforme di crowdfunding internazionali; confronta subito costi, commissioni e condizioni
- Accessibilità e contesto: italiano livello A2 (capisce le parole simili allo spagnolo, non le frasi lunghe né i messaggi di errore); inglese C1; spagnolo madrelingua
- Frequenza d'uso: dona online 3–4 volte l'anno; su un'app italiana è la prima volta
- Motivazione: un ex compagno di corso, ora ricercatore, gli manda il link a un progetto di ricerca sul clima; vuole donare 50 € e coinvolgere gli amici dell'Erasmus
- Archetipo: «l'ex Erasmus ancora legato all'Italia»
</scheda_vincolante>

<frustrazioni_da_far_emergere>
Frustrazioni con le app di crowdfunding da trasformare in 3–5 punti personali di «Difficoltà e frustrazioni», senza dettagli tecnici dell'interfaccia (le chiavi tra parentesi quadre rimandano al catalogo di C00 e non vanno riportate):
- [S32, S12] Siti tradotti a metà, con pezzi in una lingua e pezzi in un'altra.
- [S40, S36] Testi doppi in due lingue che allungano tutto.
- [S41] Messaggi di errore in una lingua che non capisce, proprio mentre paga.
- [X01, X02] Costi e commissioni poco chiari e metodi di pagamento con nomi sconosciuti.
- [S14] Link che portano su altri siti senza avviso.
</frustrazioni_da_far_emergere>

<indicazioni_specifiche>
- Mostra la sua strategia con il traduttore automatico del browser e i suoi limiti (testi nelle immagini, messaggi di errore che compaiono dopo).
- Le sue aspettative derivano dalle convenzioni delle piattaforme internazionali (selettore di lingua, riepilogo dei costi): coerenza con gli standard esterni.
- È affezionato all'Italia e vuole davvero donare: non trasformarlo in un critico.
</indicazioni_specifiche>

<controllo_finale>
Prima di rispondere verifica, senza scriverlo: (1) nessun nome di app, piattaforma, ente, università o progetto reale e nessuna chiave Sxx o Xxx nel testo; (2) campi, etichette e ordine identici a <formato_persona>; (3) dati della scheda vincolante rispettati; (4) il profilo descrive la vita della persona, non un'interfaccia.
</controllo_finale>

</prompt>
````
<!-- END PROMPT id="P04" -->

<!-- BEGIN PROMPT id="J04" tipo="journey_map" persona="P04" richiede="C00" -->
````text
<prompt id="J04" tipo="journey_map" persona="P04" richiede="C00">

<obiettivo>
Genera la scheda user journey J04 della persona P04 usando il formato <formato_journey> e le regole del contesto C00. Il percorso si svolge in una generica app di crowdfunding, senza riferimenti ad app, piattaforme, enti o progetti reali.
</obiettivo>

<persona_generata>
[Se la persona P04 è già stata generata, sostituisci questa riga con la sua scheda completa. Altrimenti lascia la riga così: userai la scheda sintetica.]
</persona_generata>

<scheda_sintetica_persona>
Tomás García, 31 anni, Madrid. Data analyst, ex studente Erasmus a Torino. Laptop con browser in inglese, smartphone Android. Familiarità 5/5, conosce le piattaforme di crowdfunding internazionali. Italiano A2, inglese C1, spagnolo madrelingua. Se la scheda in <persona_generata> è presente, usa i suoi dettagli; in caso di conflitto valgono età, dispositivo, familiarità, accessibilità e frequenza di questa scheda.
</scheda_sintetica_persona>

<scenario>
Giovedì sera, a Madrid. Un ex compagno di corso, ora ricercatore in Italia, manda a Tomás il link a un progetto di ricerca sul clima su un'app di crowdfunding italiana. Obiettivo: capire il progetto e le regole, donare 50 € e condividerlo con gli amici dell'Erasmus, molti dei quali non parlano italiano.
</scenario>

<fasi>
Usa queste fasi come colonne. Per ogni fase sono indicati i problemi del catalogo di C00 da far emergere nella riga «Criticità e barriere» (con una soluzione in «Opportunità di miglioramento») e le esperienze positive da usare. Le chiavi non vanno riportate nel documento.
1. Ricezione del link. Canale: app di messaggistica.
2. Arrivo e ricerca della lingua. Canale: sito da laptop. Problemi: S32, S12.
3. Comprensione del progetto e delle regole, anche con il traduttore del browser. Problemi: S32 (manca la regola «tutto o niente» in inglese), S14 (la guida del partner si apre su un altro sito, solo in italiano).
4. Scelta della ricompensa. Problemi: S40, S36. Positivo: S27 (posti rimasti).
5. Compilazione del modulo e pagamento. Problemi: S41, X01, X02.
6. Condivisione con gli amici. Canali: LinkedIn, gruppo di messaggistica. Positivo: S27 (condivisione). Dubbio: gli amici troveranno lo stesso problema di lingua (S32).
</fasi>

<indicazioni_specifiche>
- Rendi visibile il costo cognitivo del passaggio continuo tra lingue (attenzione selettiva, carico sulla memoria).
- Momento critico: fase 5, messaggio d'errore incomprensibile mentre paga (HEART Task success e Adoption di donatori dall'estero).
- In «Fonti e ipotesi» nota che il problema riguarda la capacità dei progetti di raccogliere fondi all'estero.
</indicazioni_specifiche>

<controllo_finale>
Prima di rispondere verifica, senza scriverlo: (1) nessun nome di app, piattaforma, ente, università o progetto reale e nessuna chiave Sxx o Xxx nel testo; (2) tutti i problemi indicati nelle fasi emergono come criticità vissute; (3) le colonne coincidono con le fasi del front matter; (4) ogni cella di «Emozioni e loro base» ha emozione, punteggio e base; (5) ogni criticità ha un'opportunità corrispondente.
</controllo_finale>

</prompt>
````
<!-- END PROMPT id="J04" -->
