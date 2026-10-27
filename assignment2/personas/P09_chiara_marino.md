---
documento: persona_journey_prompts
versione: 3 (personas generiche)
persona: P09
journey: J09
nome: Chiara Marino
descrizione: ricercatrice alla prima campagna
richiede: 00_contesto_comune_C00.md
modello_consigliato: Claude Opus 5.5 (claude-opus-5-5)
prompt_ids: [P09, J09]
---

# P09 · J09 · Chiara Marino, ricercatrice alla prima campagna

Questo file contiene i due prompt della persona P09 e del suo journey J09. Il contesto comune non è ripetuto qui: si trova in [00_contesto_comune_C00.md](00_contesto_comune_C00.md).

**Come usarlo**
1. Apri una nuova conversazione con Opus 5.5, incolla il prompt **C00** dal file del contesto comune e allega il template del corso: [scheda_persona.pdf](template/scheda_persona.pdf) per la persona, [scheda_user_journey.pdf](template/scheda_user_journey.pdf) per il journey.
2. Per la persona incolla il prompt **P09**; per il journey usa una nuova conversazione, incolla di nuovo C00 e poi il prompt **J09**. Puoi anche incollare C00 e il prompt singolo nello stesso messaggio.
3. Se la persona P09 è già stata generata, incolla il suo documento dentro `<persona_generata>` del prompt J09; altrimenti lascialo com'è.
4. Facoltativo: controlla l'output con il prompt V00 in [99_verifica_V00.md](99_verifica_V00.md).

Il testo da copiare è quello dentro ciascun blocco di codice.

<!-- BEGIN PROMPT id="P09" tipo="persona" persona="P09" richiede="C00" -->
````text
<prompt id="P09" tipo="persona" richiede="C00">

<obiettivo>
Genera la scheda della persona P09 usando il formato <formato_persona> e le regole del contesto C00. Racconta la persona e il suo rapporto con il crowdfunding in generale, senza riferimenti ad app, piattaforme, enti o progetti reali.
</obiettivo>

<scheda_vincolante>
- Nome: Chiara Marino
- Età: 32
- Città: Torino
- Occupazione: assegnista di ricerca in ecologia; dottorato concluso da due anni, contratto in scadenza tra 18 mesi
- Famiglia: convive con il compagno
- Vita quotidiana: laboratorio e campionamenti all'aperto, didattica, trekking e birdwatching nel fine settimana, legge la sera
- Valori: ricerca utile alla città, divulgazione, indipendenza
- Ruolo: promotrice; vuole lanciare la sua prima campagna di crowdfunding, partecipando al programma che la sua università ha con un'app
- Dispositivo principale: laptop macOS con Safari; iPhone per l'email
- Familiarità digitale: 4/5. Banche dati, piattaforme per i bandi, social; nessuna esperienza di crowdfunding né di marketing
- Accessibilità e contesto: tempo frammentato; legge a pezzi, spesso la sera
- Frequenza d'uso: prima visita esplorativa, poi uso intensivo nelle settimane della candidatura
- Motivazione: finanziare i campionamenti di un progetto sugli impollinatori in città, circa 8.000 €; un collega le ha parlato del programma
- Archetipo: «la ricercatrice alla prima campagna»
</scheda_vincolante>

<frustrazioni_da_far_emergere>
Frustrazioni con le app di crowdfunding da trasformare in 3–5 punti personali di «Difficoltà e frustrazioni», senza dettagli tecnici dell'interfaccia (le chiavi tra parentesi quadre rimandano al catalogo di C00 e non vanno riportate):
- [S09, S25, X07] Non trovare scadenze, requisiti e un contatto, come invece accade nei bandi.
- [S52, S54, S53] Guide lunghe, senza titoli e con testi piccoli, da leggere a pezzi.
- [S46, S48] Gergo del marketing e nomi diversi per la stessa cosa.
- [S49] Costi scoperti tardi.
- [S51, S50, S55] Moduli di registrazione che fanno perdere tempo.
</frustrazioni_da_far_emergere>

<indicazioni_specifiche>
- Il suo modello mentale è quello del bando di ricerca (requisiti, scadenze, modulistica, ufficio di riferimento), non quello di un servizio commerciale: mostra il divario tra modello mentale e modello concettuale.
- Il tempo frammentato rende cruciali indici, titoli e possibilità di riprendere.
- Distingui ciò che riguarda l'app in generale da ciò che riguarda il programma dell'università.
</indicazioni_specifiche>

<controllo_finale>
Prima di rispondere verifica, senza scriverlo: (1) nessun nome di app, piattaforma, ente, università o progetto reale e nessuna chiave Sxx o Xxx nel testo; (2) campi, etichette e ordine identici a <formato_persona>; (3) dati della scheda vincolante rispettati; (4) il profilo descrive la vita della persona, non un'interfaccia.
</controllo_finale>

</prompt>
````
<!-- END PROMPT id="P09" -->

<!-- BEGIN PROMPT id="J09" tipo="journey_map" persona="P09" richiede="C00" -->
````text
<prompt id="J09" tipo="journey_map" persona="P09" richiede="C00">

<obiettivo>
Genera la scheda user journey J09 della persona P09 usando il formato <formato_journey> e le regole del contesto C00. Il percorso si svolge in una generica app di crowdfunding, senza riferimenti ad app, piattaforme, enti o progetti reali.
</obiettivo>

<persona_generata>
[Se la persona P09 è già stata generata, sostituisci questa riga con la sua scheda completa. Altrimenti lascia la riga così: userai la scheda sintetica.]
</persona_generata>

<scheda_sintetica_persona>
Chiara Marino, 32 anni, Torino. Assegnista di ricerca in ecologia. Laptop macOS con Safari, iPhone per l'email. Familiarità 4/5, nessuna esperienza di crowdfunding. Tempo frammentato, legge la sera. Vuole lanciare una campagna nel programma della sua università. Se la scheda in <persona_generata> è presente, usa i suoi dettagli; in caso di conflitto valgono età, dispositivo, familiarità, accessibilità e frequenza di questa scheda.
</scheda_sintetica_persona>

<scenario>
Tre sere nell'arco di una settimana, a casa dopo il laboratorio. Un collega ha nominato il programma di crowdfunding dell'università su un'app. Chiara vuole capire se può candidare il suo progetto sugli impollinatori, entro quando, a chi rivolgersi e quanto costa. Obiettivo: sapere con certezza come candidarsi e creare il profilo da promotrice.
</scenario>

<fasi>
Usa queste fasi come colonne. Per ogni fase sono indicati i problemi del catalogo di C00 da far emergere nella riga «Criticità e barriere» (con una soluzione in «Opportunità di miglioramento») e le esperienze positive da usare. Le chiavi non vanno riportate nel documento.
1. Scoperta dell'opportunità. Canali: riunione, email, sito dell'app. Problema: S09.
2. Capire il programma dell'università. Canali: sito dell'app, sito dell'università. Problemi: S25, S14, X07.
3. Studiare regole e costi. Problemi: S52, S54, S53, S46, S48, S49.
4. Cercare il passo successivo. Problemi: S47, X07. Positivi: S44, S58.
5. Registrazione come promotrice. Canale: modulo di registrazione. Problemi: S51, S50, S55.
6. Preparazione della candidatura: contatto con l'ufficio dell'università o con l'app e prime bozze. Canali: email, telefono. Tutto [IPOTESI].
</fasi>

<indicazioni_specifiche>
- Il journey si sviluppa su più sessioni: indica dove Chiara deve ricominciare da capo.
- Momento critico: fase 3, la scoperta tardiva della quota di pubblicazione e il dubbio se valga anche nel programma dell'università (HEART Adoption dei promotori).
- In «Fonti e ipotesi» proponi una domanda da verificare con l'ufficio dell'università, senza dare risposte inventate.
</indicazioni_specifiche>

<controllo_finale>
Prima di rispondere verifica, senza scriverlo: (1) nessun nome di app, piattaforma, ente, università o progetto reale e nessuna chiave Sxx o Xxx nel testo; (2) tutti i problemi indicati nelle fasi emergono come criticità vissute; (3) le colonne coincidono con le fasi del front matter; (4) ogni cella di «Emozioni e loro base» ha emozione, punteggio e base; (5) ogni criticità ha un'opportunità corrispondente.
</controllo_finale>

</prompt>
````
<!-- END PROMPT id="J09" -->
