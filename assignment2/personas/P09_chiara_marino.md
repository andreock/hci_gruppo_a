---
documento: persona_journey_prompts
persona: P09
journey: J09
nome: Chiara Marino
descrizione: ricercatrice UniTo alla prima campagna
richiede: 00_contesto_comune_C00.md
modello_consigliato: Claude Opus 5.5 (claude-opus-5-5)
prompt_ids: [P09, J09]
---

# P09 · J09 · Chiara Marino, ricercatrice UniTo alla prima campagna

Questo file contiene i due prompt della persona P09 e del suo journey J09. Il contesto comune non è ripetuto qui: si trova in [00_contesto_comune_C00.md](00_contesto_comune_C00.md).

**Come usarlo**
1. Apri una nuova conversazione con Opus 5.5 e incolla il prompt **C00** dal file del contesto comune.
2. Per la persona incolla il prompt **P09**; per il journey usa una nuova conversazione, incolla di nuovo C00 e poi il prompt **J09**. Puoi anche incollare C00 e il prompt singolo nello stesso messaggio.
3. Se la persona P09 è già stata generata, incolla il suo documento dentro `<persona_generata>` del prompt J09; altrimenti lascialo com'è.
4. Facoltativo: controlla l'output con il prompt V00 in [99_verifica_V00.md](99_verifica_V00.md).

Il testo da copiare è quello dentro ciascun blocco di codice.

<!-- BEGIN PROMPT id="P09" tipo="persona" persona="P09" richiede="C00" -->
````text
<prompt id="P09" tipo="persona" richiede="C00">

<obiettivo>
Genera la persona P09 usando il formato <formato_persona> e le regole del contesto C00.
</obiettivo>

<scheda_vincolante>
- Nome: Chiara Marino
- Età: 32
- Città: Torino
- Occupazione: assegnista di ricerca in ecologia in un dipartimento UniTo di scienze della vita; dottorato concluso da due anni
- Famiglia: convive con il compagno
- Ruolo: promotrice; vuole candidare un progetto alla prossima edizione di Funds TOgether
- Dispositivo principale: laptop macOS con Safari; iPhone per l'email
- Canali: email d'Ateneo, sito Ginger, sito unito.it, telefono, modulo di registrazione all'area progettisti
- Familiarità digitale: 4/5. Banche dati, piattaforme per i bandi, social; nessuna esperienza di crowdfunding né di marketing
- Accessibilità e contesto: tempo frammentato tra laboratorio, campionamenti e didattica; legge a pezzi, spesso la sera
- Frequenza d'uso: prima visita esplorativa, poi uso intensivo nelle settimane della candidatura
- Motivazione: finanziare i campionamenti di un progetto (fittizio) sugli impollinatori in città, circa 8.000 €; ha saputo di Funds TOgether da un collega
- Archetipo suggerito: «la ricercatrice alla prima campagna»
</scheda_vincolante>

<problemi_assegnati>
- [S09 · H1 · G3] Nessuna data di candidatura: non sa se è in tempo.
- [S25 · H10 · G2] La pagina UniTo non dice chi può candidarsi, entro quando, con quale modulo né chi contattare.
- [S14 · H3 · G3] «Scopri la guida dell'iniziativa» la porta su unito.it senza avviso.
- [X07 · analisi preliminare, da verificare] La pagina unito.it non contiene un bando; «Lancia una campagna» porta alla registrazione generica di Ginger, che non è il percorso di un ricercatore UniTo.
- [S52 · H7 · G3] «Come funziona» è un testo continuo senza titoli né indice.
- [S54 · H8 · G4] Testi piccoli e disomogenei, comprese le informazioni sui costi.
- [S53 · H7 · G3] Le FAQ mescolano domande per donatori e progettisti.
- [S46 · H2 · G2] «Campaign manager», «call di consulenza», «fee di accesso» non spiegati.
- [S48 · H4 · G1] Due nomi diversi per la stessa modalità di raccolta.
- [S49 · H5 · G4] La quota di 350 € + IVA è nascosta in fondo a un paragrafo: non sa se vale anche per i progetti UniTo.
- [S47 · H3 · G2] La FAQ cita «Lancia una campagna» senza link.
- [S51 · H6 · G3] Nel modulo di registrazione le etichette spariscono mentre scrive.
- [S50 · H5 · G2] Il modulo non usa i controlli del browser (autocompletamento disattivato).
- [S55 · H9 · G2] Il messaggio di errore resta anche dopo la correzione.
</problemi_assegnati>

<aspetti_positivi_da_includere>
- [S44 · positivo] «Come funziona» offre tre modi per iniziare (mail, telefono, profilo) e i contatti all'inizio e alla fine.
- [S58 · positivo] «LANCIA UNA CAMPAGNA» è ben visibile nel menu principale.
</aspetti_positivi_da_includere>

<indicazioni_specifiche>
- Il suo modello mentale è quello del bando di ricerca (requisiti, scadenze, modulistica, ufficio di riferimento), non quello di una piattaforma commerciale: mostra il divario tra modello mentale e modello concettuale del servizio.
- Il tempo frammentato rende cruciali indici, titoli e possibilità di riprendere la lettura.
- Distingui ciò che riguarda Ginger in generale da ciò che riguarda il percorso specifico UniTo.
</indicazioni_specifiche>

<controllo_finale>
Prima di rispondere verifica, senza scriverlo: (1) il front matter è completo e problemi_citati contiene esattamente gli ID citati nel testo; (2) ogni problema assegnato è citato almeno una volta; (3) i dati della scheda vincolante sono rispettati; (4) titoli e ordine delle sezioni sono identici a <formato_persona>.
</controllo_finale>

</prompt>
````
<!-- END PROMPT id="P09" -->

<!-- BEGIN PROMPT id="J09" tipo="journey_map" persona="P09" richiede="C00" -->
````text
<prompt id="J09" tipo="journey_map" persona="P09" richiede="C00">

<obiettivo>
Genera la journey map J09 della persona P09 usando il formato <formato_journey> e le regole del contesto C00.
</obiettivo>

<persona_generata>
[Se la persona P09 è già stata generata, sostituisci questa riga con il suo documento completo. Altrimenti lascia la riga così: userai la scheda sintetica.]
</persona_generata>

<scheda_sintetica_persona>
Chiara Marino, 32 anni, Torino. Assegnista di ricerca in ecologia a UniTo. Laptop macOS con Safari, iPhone per l'email. Familiarità 4/5, nessuna esperienza di crowdfunding. Tempo frammentato, legge la sera. Vuole candidare un progetto a Funds TOgether. Se il documento in <persona_generata> è presente, usa i suoi dettagli; in caso di conflitto valgono età, dispositivo, familiarità, accessibilità e frequenza di questa scheda.
</scheda_sintetica_persona>

<scenario>
Tre sere nell'arco di una settimana, a casa dopo il laboratorio. Un collega ha nominato Funds TOgether durante una riunione. Chiara vuole capire se può candidare il suo progetto sugli impollinatori, entro quando, a chi rivolgersi e quanto costa. Obiettivo: arrivare a sapere con certezza come candidarsi e aprire il profilo sulla piattaforma.
</scenario>

<fasi>
1. Scoperta dell'opportunità. Canali: riunione, email d'Ateneo, sito Ginger. Problema: [S09 · H1 · G3].
2. Capire la partnership UniTo. Canali: sito Ginger, unito.it. Problemi: [S25 · H10 · G2], [S14 · H3 · G3], [X07 · analisi preliminare, da verificare].
3. Studiare regole e costi. Problemi: [S52 · H7 · G3], [S54 · H8 · G4], [S53 · H7 · G3], [S46 · H2 · G2], [S48 · H4 · G1], [S49 · H5 · G4].
4. Cercare il passo successivo. Problemi: [S47 · H3 · G2], [X07 · analisi preliminare, da verificare]. Positivi: [S44 · positivo], [S58 · positivo].
5. Registrazione all'area progettisti. Canale: modulo di registrazione. Problemi: [S51 · H6 · G3], [S50 · H5 · G2], [S55 · H9 · G2].
6. Preparazione della candidatura: contatto con l'ufficio UniTo o con Ginger e prime bozze. Canali: email, telefono. Tutto [IPOTESI]: l'area riservata e la selezione d'Ateneo non sono state analizzate.
</fasi>

<indicazioni_specifiche>
- Il journey si sviluppa su più sessioni: indica dove Chiara deve ricominciare da capo perché le pagine non hanno indice o non conservano lo stato.
- Momento critico: fase 3, la scoperta tardiva della quota di 350 € + IVA e il dubbio se riguardi i progetti UniTo (HEART Adoption per i promotori).
- Nelle note per il team proponi una domanda da verificare con l'ufficio UniTo sul rapporto tra quota Ginger e cofinanziamento d'Ateneo, senza dare una risposta inventata.
</indicazioni_specifiche>

<controllo_finale>
Prima di rispondere verifica, senza scriverlo: (1) front matter completo e problemi_citati uguale agli ID citati; (2) tutti i problemi elencati nelle fasi sono citati; (3) le fasi della tabella coincidono con il front matter; (4) i punteggi della curva emotiva coincidono con la riga Emozioni; (5) ogni difficoltà ha un'opportunità corrispondente.
</controllo_finale>

</prompt>
````
<!-- END PROMPT id="J09" -->
