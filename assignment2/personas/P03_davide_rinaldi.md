---
documento: persona_journey_prompts
versione: 3 (personas generiche)
persona: P03
journey: J03
nome: Davide Rinaldi
descrizione: donatore non vedente esperto di screen reader
richiede: 00_contesto_comune_C00.md
modello_consigliato: Claude Opus 5.5 (claude-opus-5-5)
prompt_ids: [P03, J03]
---

# P03 · J03 · Davide Rinaldi, donatore non vedente esperto di screen reader

Questo file contiene i due prompt della persona P03 e del suo journey J03. Il contesto comune non è ripetuto qui: si trova in [00_contesto_comune_C00.md](00_contesto_comune_C00.md).

**Come usarlo**
1. Apri una nuova conversazione con Opus 5.5, incolla il prompt **C00** dal file del contesto comune e allega il template del corso: [scheda_persona.pdf](template/scheda_persona.pdf) per la persona, [scheda_user_journey.pdf](template/scheda_user_journey.pdf) per il journey.
2. Per la persona incolla il prompt **P03**; per il journey usa una nuova conversazione, incolla di nuovo C00 e poi il prompt **J03**. Puoi anche incollare C00 e il prompt singolo nello stesso messaggio.
3. Se la persona P03 è già stata generata, incolla il suo documento dentro `<persona_generata>` del prompt J03; altrimenti lascialo com'è.
4. Facoltativo: controlla l'output con il prompt V00 in [99_verifica_V00.md](99_verifica_V00.md).

Il testo da copiare è quello dentro ciascun blocco di codice.

<!-- BEGIN PROMPT id="P03" tipo="persona" persona="P03" richiede="C00" -->
````text
<prompt id="P03" tipo="persona" richiede="C00">

<obiettivo>
Genera la scheda della persona P03 usando il formato <formato_persona> e le regole del contesto C00. Racconta la persona e il suo rapporto con il crowdfunding in generale, senza riferimenti ad app, piattaforme, enti o progetti reali.
</obiettivo>

<scheda_vincolante>
- Nome: Davide Rinaldi
- Età: 39
- Città: Torino
- Occupazione: funzionario amministrativo in un ente pubblico
- Famiglia: vive con la compagna e un cane guida
- Vita quotidiana: volontario in un'associazione che promuove l'accessibilità dell'istruzione, ascolta audiolibri e podcast, fa tandem in bicicletta nel fine settimana
- Valori: autonomia, inclusione, diritto allo studio
- Ruolo: donatore; dona 3–4 volte l'anno online a cause legate all'accessibilità e all'istruzione
- Dispositivo principale: PC Windows con screen reader NVDA e Firefox a casa; iPhone con VoiceOver fuori casa
- Familiarità digitale: 5/5 con le tecnologie assistive. Naviga per titoli, link e punti di riferimento (landmark), usa l'elenco dei link, sintesi vocale ad alta velocità; riconosce subito un sito poco accessibile
- Accessibilità: cecità totale dalla nascita; usa solo tastiera e sintesi vocale
- Frequenza d'uso: prima volta sull'app; dona online più volte l'anno
- Motivazione: dalla mailing list dell'associazione scopre un progetto di ricerca sulla matematica accessibile alle persone cieche e vuole sostenerlo; se non è possibile, vuole sostenere un altro progetto di ricerca in corso
- Archetipo: «l'esperto di accessibilità che mette alla prova il servizio»
</scheda_vincolante>

<frustrazioni_da_far_emergere>
Frustrazioni con le app di crowdfunding da trasformare in 3–5 punti personali di «Difficoltà e frustrazioni», senza dettagli tecnici dell'interfaccia (le chiavi tra parentesi quadre rimandano al catalogo di C00 e non vanno riportate):
- [S35] Pagine con immagini non descritte e titoli che non hanno senso letti ad alta voce.
- [S17] Elementi cliccabili che lo screen reader non riesce a nominare.
- [S29] Informazioni affidate solo a colori o simboli (come lo stato di una campagna).
- [S15, S67] Perdere il punto o restare bloccato nei menu quando si naviga da tastiera.
- [S65, S68] Elenchi di link tutti uguali e parole lette due volte.
</frustrazioni_da_far_emergere>

<indicazioni_specifiche>
- Descrivi con precisione come usa lo screen reader (tasti, strategie, velocità) e come giudica l'affidabilità di un servizio dalla sua accessibilità.
- Non presentarlo come una persona fragile: è un utente esperto, efficiente e critico; le difficoltà nascono dalle interfacce.
- Per lui affordance e signifier visivi (effetti al passaggio del mouse, colori, pallini) non esistono: conta ciò che è nel codice (ruoli, nomi, stati).
</indicazioni_specifiche>

<controllo_finale>
Prima di rispondere verifica, senza scriverlo: (1) nessun nome di app, piattaforma, ente, università o progetto reale e nessuna chiave Sxx o Xxx nel testo; (2) campi, etichette e ordine identici a <formato_persona>; (3) dati della scheda vincolante rispettati; (4) il profilo descrive la vita della persona, non un'interfaccia.
</controllo_finale>

</prompt>
````
<!-- END PROMPT id="P03" -->

<!-- BEGIN PROMPT id="J03" tipo="journey_map" persona="P03" richiede="C00" -->
````text
<prompt id="J03" tipo="journey_map" persona="P03" richiede="C00">

<obiettivo>
Genera la scheda user journey J03 della persona P03 usando il formato <formato_journey> e le regole del contesto C00. Il percorso si svolge in una generica app di crowdfunding, senza riferimenti ad app, piattaforme, enti o progetti reali.
</obiettivo>

<persona_generata>
[Se la persona P03 è già stata generata, sostituisci questa riga con la sua scheda completa. Altrimenti lascia la riga così: userai la scheda sintetica.]
</persona_generata>

<scheda_sintetica_persona>
Davide Rinaldi, 39 anni, Torino. Funzionario in un ente pubblico, non vedente dalla nascita. PC Windows con NVDA e Firefox, iPhone con VoiceOver. Familiarità 5/5 con le tecnologie assistive: naviga per titoli, link e landmark. Volontario per l'accessibilità dell'istruzione. Prima volta sull'app. Se la scheda in <persona_generata> è presente, usa i suoi dettagli; in caso di conflitto valgono età, dispositivo, familiarità, accessibilità e frequenza di questa scheda.
</scheda_sintetica_persona>

<scenario>
Una sera, alla scrivania di casa. Davide riceve dalla mailing list dell'associazione il link a un progetto di ricerca sulla matematica accessibile, pubblicato su un'app di crowdfunding. Obiettivo: sostenerlo e, se non è più possibile, trovare e sostenere con 30 € un altro progetto di ricerca in corso, usando solo tastiera e screen reader.
</scenario>

<fasi>
Usa queste fasi come colonne. Per ogni fase sono indicati i problemi del catalogo di C00 da far emergere nella riga «Criticità e barriere» (con una soluzione in «Opportunità di miglioramento») e le esperienze positive da usare. Le chiavi non vanno riportate nel documento.
1. Scoperta nella mailing list. Canale: email.
2. Esplorazione della pagina del progetto. Canale: sito da desktop con NVDA. Problemi: S35, S33.
3. Capire se si può ancora donare (la campagna è conclusa). Problema: S29.
4. Ricerca di un altro progetto, passando dalla homepage e dall'elenco dei progetti. Problemi: S67, S65, S68, S17, S15.
5. Donazione a un progetto in corso. Positivo: S27 (pulsanti ben etichettati). Problema: S41 (l'errore compare dopo l'invio e va ritrovato con lo screen reader).
6. Resoconto all'associazione: scrive alla mailing list che cosa ha funzionato e che cosa no. Canale: email. Problema: S74 (accessibilità complessiva mediocre).
</fasi>

<indicazioni_specifiche>
- Nelle azioni e nei touchpoint indica come Davide interagisce (es. «tasto H per i titoli», «elenco dei link»), non come vedrebbe la pagina un utente vedente.
- Momento critico: fase 3, quando lo stato «concluso» non gli viene comunicato (golfo della valutazione).
- In «Fonti e ipotesi» nota il rischio di credibilità di un progetto sull'accessibilità presentato in una pagina non accessibile (HEART Happiness).
</indicazioni_specifiche>

<controllo_finale>
Prima di rispondere verifica, senza scriverlo: (1) nessun nome di app, piattaforma, ente, università o progetto reale e nessuna chiave Sxx o Xxx nel testo; (2) tutti i problemi indicati nelle fasi emergono come criticità vissute; (3) le colonne coincidono con le fasi del front matter; (4) ogni cella di «Emozioni e loro base» ha emozione, punteggio e base; (5) ogni criticità ha un'opportunità corrispondente.
</controllo_finale>

</prompt>
````
<!-- END PROMPT id="J03" -->
