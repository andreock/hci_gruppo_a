---
documento: persona_journey_prompts
persona: P03
journey: J03
nome: Davide Rinaldi
descrizione: donatore non vedente
richiede: 00_contesto_comune_C00.md
modello_consigliato: Claude Opus 5.5 (claude-opus-5-5)
prompt_ids: [P03, J03]
---

# P03 · J03 · Davide Rinaldi, donatore non vedente

Questo file contiene i due prompt della persona P03 e del suo journey J03. Il contesto comune non è ripetuto qui: si trova in [00_contesto_comune_C00.md](00_contesto_comune_C00.md).

**Come usarlo**
1. Apri una nuova conversazione con Opus 5.5 e incolla il prompt **C00** dal file del contesto comune.
2. Per la persona incolla il prompt **P03**; per il journey usa una nuova conversazione, incolla di nuovo C00 e poi il prompt **J03**. Puoi anche incollare C00 e il prompt singolo nello stesso messaggio.
3. Se la persona P03 è già stata generata, incolla il suo documento dentro `<persona_generata>` del prompt J03; altrimenti lascialo com'è.
4. Facoltativo: controlla l'output con il prompt V00 in [99_verifica_V00.md](99_verifica_V00.md).

Il testo da copiare è quello dentro ciascun blocco di codice.

<!-- BEGIN PROMPT id="P03" tipo="persona" persona="P03" richiede="C00" -->
````text
<prompt id="P03" tipo="persona" richiede="C00">

<obiettivo>
Genera la persona P03 usando il formato <formato_persona> e le regole del contesto C00.
</obiettivo>

<scheda_vincolante>
- Nome: Davide Rinaldi
- Età: 39
- Città: Torino
- Occupazione: funzionario amministrativo in un ente pubblico
- Famiglia: vive con la compagna
- Ruolo: donatore; dona 3–4 volte l'anno online a cause legate all'accessibilità e all'istruzione
- Dispositivo principale: PC Windows con screen reader NVDA e Firefox (a casa); iPhone con VoiceOver fuori casa
- Canali: mailing list di un'associazione, sito da desktop con screen reader, email, telefono
- Familiarità digitale: 5/5 con le tecnologie assistive. Naviga per titoli, per link e per punti di riferimento (landmark), usa l'elenco dei link di NVDA, sintesi vocale ad alta velocità; riconosce subito un sito poco accessibile
- Accessibilità: cecità totale dalla nascita; usa solo la tastiera e la sintesi vocale
- Frequenza d'uso: prima visita su Ginger
- Impegno: volontario in un'associazione che promuove l'accessibilità dell'istruzione
- Motivazione: nella mailing list dell'associazione legge di «MatematIcA senza barriere», progetto UniTo sulla matematica accessibile, e vuole sostenerlo; se non è possibile, vuole sostenere un altro progetto UniTo in corso
- Archetipo suggerito: «l'esperto di accessibilità che mette alla prova il sito»
</scheda_vincolante>

<problemi_assegnati>
- [S35 · H4 · G3] Proprio la pagina di un progetto sull'accessibilità ha immagini senza testo alternativo, titoli vuoti e h4 usati per formattare: la navigazione per titoli diventa inaffidabile.
- [S29 · H1 · G3] Il progetto è concluso, ma il box «SOSTIENI» con prezzi e campo «FAI TU» è ancora presente e lo stato è affidato solo a un pallino rosso senza legenda (che lo screen reader, senza testo, non può annunciare).
- [S33 · H4/H10 · G1] «O tutto o niente!» e gli obiettivi di sostenibilità vengono annunciati come link ma non portano da nessuna parte.
- [S17 · H4 · G4] Nell'elenco dei progetti UniTo le card non hanno aria-label: non capisce quali elementi portano ai progetti né come si chiamano.
- [S15 · H3 · G4] Tornando indietro da un progetto perde la posizione e i progetti caricati con «ALTRI»: deve ripetere tutta la navigazione da tastiera.
- [S67 · LG9 · G2] Nel menu della homepage le tendine con oltre 70 voci non si chiudono con Esc e la X non si raggiunge da tastiera.
- [S65 · LG7 · G2] Nell'elenco dei link sente 25 volte «Vai alla pagina» e non sa quale porti al partner UniTo.
- [S68 · LG10 · G1] Le icone delle categorie vengono lette due volte.
- [S74 · prestazioni] Il punteggio Lighthouse di accessibilità resta tra 64 e 77 su tutte le pagine del percorso.
</problemi_assegnati>

<aspetti_positivi_da_includere>
- [S27 · positivo] Nelle pagine progetto pulsanti e icone hanno attributi ARIA: alcune parti funzionano bene, il che rende più evidente dove il sito non funziona.
</aspetti_positivi_da_includere>

<indicazioni_specifiche>
- Descrivi con precisione come usa lo screen reader (tasti, strategie, velocità) e come valuta l'affidabilità di un sito dalla sua accessibilità.
- Non presentarlo come una persona fragile: è un utente esperto, efficiente e critico; le difficoltà nascono dal sito.
- Collega i problemi al fatto che per lui affordance e signifier visivi (hover, colori, pallini) non esistono: conta solo ciò che è nel codice (ruoli, nomi, stati).
</indicazioni_specifiche>

<controllo_finale>
Prima di rispondere verifica, senza scriverlo: (1) il front matter è completo e problemi_citati contiene esattamente gli ID citati nel testo; (2) ogni problema assegnato è citato almeno una volta; (3) i dati della scheda vincolante sono rispettati; (4) titoli e ordine delle sezioni sono identici a <formato_persona>.
</controllo_finale>

</prompt>
````
<!-- END PROMPT id="P03" -->

<!-- BEGIN PROMPT id="J03" tipo="journey_map" persona="P03" richiede="C00" -->
````text
<prompt id="J03" tipo="journey_map" persona="P03" richiede="C00">

<obiettivo>
Genera la journey map J03 della persona P03 usando il formato <formato_journey> e le regole del contesto C00.
</obiettivo>

<persona_generata>
[Se la persona P03 è già stata generata, sostituisci questa riga con il suo documento completo. Altrimenti lascia la riga così: userai la scheda sintetica.]
</persona_generata>

<scheda_sintetica_persona>
Davide Rinaldi, 39 anni, Torino. Funzionario in un ente pubblico, non vedente dalla nascita. PC Windows con NVDA e Firefox, iPhone con VoiceOver. Familiarità 5/5 con le tecnologie assistive: naviga per titoli, link e landmark. Volontario in un'associazione per l'accessibilità dell'istruzione. Prima visita su Ginger. Se il documento in <persona_generata> è presente, usa i suoi dettagli; in caso di conflitto valgono età, dispositivo, familiarità, accessibilità e frequenza di questa scheda.
</scheda_sintetica_persona>

<scenario>
Una sera, alla scrivania di casa. Davide riceve dalla mailing list dell'associazione il link alla pagina di «MatematIcA senza barriere». Obiettivo: sostenere quel progetto e, se non è più possibile, trovare e sostenere con 30 € un altro progetto UniTo in corso, usando solo tastiera e screen reader.
</scenario>

<fasi>
1. Scoperta nella mailing list. Canale: email.
2. Esplorazione della pagina di MatematIcA. Canale: sito da desktop con NVDA. Problemi: [S35 · H4 · G3], [S33 · H4/H10 · G1].
3. Capire se si può ancora donare. Problema: [S29 · H1 · G3].
4. Ricerca di un altro progetto UniTo, passando dalla homepage e dall'elenco dei progetti. Problemi: [S67 · LG9 · G2], [S65 · LG7 · G2], [S68 · LG10 · G1], [S17 · H4 · G4], [S15 · H3 · G4].
5. Donazione a un progetto in corso. Positivo: [S27 · positivo] attributi ARIA dei pulsanti. Problema: [S41 · H9 · G4] l'errore compare solo dopo l'invio e va ritrovato con lo screen reader.
6. Resoconto all'associazione: scrive alla mailing list che cosa ha funzionato e che cosa no. Canale: email. Riferimento: [S74 · prestazioni] punteggi di accessibilità tra 64 e 77.
</fasi>

<indicazioni_specifiche>
- Nella riga «Touchpoint» e nelle azioni indica come Davide interagisce (es. «tasto H per i titoli», «elenco link NVDA»), non come vedrebbe la pagina un utente vedente.
- Momento critico: fase 3, quando lo stato «concluso» non gli è comunicato. Collegalo al golfo della valutazione.
- Nelle note per il team evidenzia l'ironia del progetto sull'accessibilità reso su una pagina non accessibile come rischio di credibilità per la piattaforma (indicatore HEART Happiness).
</indicazioni_specifiche>

<controllo_finale>
Prima di rispondere verifica, senza scriverlo: (1) front matter completo e problemi_citati uguale agli ID citati; (2) tutti i problemi elencati nelle fasi sono citati; (3) le fasi della tabella coincidono con il front matter; (4) i punteggi della curva emotiva coincidono con la riga Emozioni; (5) ogni difficoltà ha un'opportunità corrispondente.
</controllo_finale>

</prompt>
````
<!-- END PROMPT id="J03" -->
