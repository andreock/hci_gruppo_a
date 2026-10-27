---
documento: persona_journey_prompts
versione: 3 (personas generiche)
persona: P08
journey: J08
nome: Roberta Galli
descrizione: giornalista scientifica che verifica ogni numero
richiede: 00_contesto_comune_C00.md
modello_consigliato: Claude Opus 5.5 (claude-opus-5-5)
prompt_ids: [P08, J08]
---

# P08 · J08 · Roberta Galli, giornalista scientifica che verifica ogni numero

Questo file contiene i due prompt della persona P08 e del suo journey J08. Il contesto comune non è ripetuto qui: si trova in [00_contesto_comune_C00.md](00_contesto_comune_C00.md).

**Come usarlo**
1. Apri una nuova conversazione con Opus 5.5, incolla il prompt **C00** dal file del contesto comune e allega il template del corso: [scheda_persona.pdf](template/scheda_persona.pdf) per la persona, [scheda_user_journey.pdf](template/scheda_user_journey.pdf) per il journey.
2. Per la persona incolla il prompt **P08**; per il journey usa una nuova conversazione, incolla di nuovo C00 e poi il prompt **J08**. Puoi anche incollare C00 e il prompt singolo nello stesso messaggio.
3. Se la persona P08 è già stata generata, incolla il suo documento dentro `<persona_generata>` del prompt J08; altrimenti lascialo com'è.
4. Facoltativo: controlla l'output con il prompt V00 in [99_verifica_V00.md](99_verifica_V00.md).

Il testo da copiare è quello dentro ciascun blocco di codice.

<!-- BEGIN PROMPT id="P08" tipo="persona" persona="P08" richiede="C00" -->
````text
<prompt id="P08" tipo="persona" richiede="C00">

<obiettivo>
Genera la scheda della persona P08 usando il formato <formato_persona> e le regole del contesto C00. Racconta la persona e il suo rapporto con il crowdfunding in generale, senza riferimenti ad app, piattaforme, enti o progetti reali.
</obiettivo>

<scheda_vincolante>
- Nome: Roberta Galli
- Età: 47
- Città: Torino
- Occupazione: giornalista scientifica freelance per una testata online locale
- Famiglia: sposata, due figli alle medie
- Vita quotidiana: lavora da casa con scadenze strette, telefonate continue, corre al mattino, legge saggi di divulgazione, modera un piccolo festival della scienza
- Valori: precisione, verifica delle fonti, servizio ai lettori
- Ruolo: visitatrice per lavoro; potrebbe donare a titolo personale in seguito
- Dispositivo principale: laptop con molte schede aperte e un foglio di calcolo; smartphone per telefonate e foto
- Familiarità digitale: 5/5. Ricerca avanzata, verifica delle fonti, archivi online
- Accessibilità e contesto: nessuna esigenza specifica; molte interruzioni
- Frequenza d'uso: occasionale ma intensiva: 2–3 sessioni lunghe nella stessa settimana per un articolo
- Tipo di ricerca: esaustiva (vuole tutti i progetti di tutte le edizioni e i numeri complessivi)
- Motivazione: sta scrivendo un articolo sulle prime quattro edizioni del programma di crowdfunding per la ricerca dell'università della sua città
- Archetipo: «la giornalista che verifica ogni numero»
</scheda_vincolante>

<frustrazioni_da_far_emergere>
Frustrazioni con le app di crowdfunding da trasformare in 3–5 punti personali di «Difficoltà e frustrazioni», senza dettagli tecnici dell'interfaccia (le chiavi tra parentesi quadre rimandano al catalogo di C00 e non vanno riportate):
- [S09, X06, S66] Pagine senza date e numeri che non coincidono.
- [S22, S24, S21] Elenchi che si caricano a pezzi, senza filtri, senza sapere se li ha visti tutti.
- [S15, S20] Perdere il punto dopo ogni interruzione.
- [S28, S25] Contatti difficili da trovare o che sembrano non funzionare.
- [S13, S30] Non capire chi c'è dietro un progetto e trovare le notizie prima della presentazione.
</frustrazioni_da_far_emergere>

<indicazioni_specifiche>
- Il suo bisogno è esaustivo e di verifica: mostra la differenza tra ricerca esaustiva e ricerca conosciuta.
- Il suo articolo sarà un canale indiretto verso nuovi donatori: gli errori che trova possono amplificarsi.
- Mostra l'attenzione divisa (telefonate, scadenze) e come la perdita di stato peggiora l'effetto delle interruzioni.
</indicazioni_specifiche>

<controllo_finale>
Prima di rispondere verifica, senza scriverlo: (1) nessun nome di app, piattaforma, ente, università o progetto reale e nessuna chiave Sxx o Xxx nel testo; (2) campi, etichette e ordine identici a <formato_persona>; (3) dati della scheda vincolante rispettati; (4) il profilo descrive la vita della persona, non un'interfaccia.
</controllo_finale>

</prompt>
````
<!-- END PROMPT id="P08" -->

<!-- BEGIN PROMPT id="J08" tipo="journey_map" persona="P08" richiede="C00" -->
````text
<prompt id="J08" tipo="journey_map" persona="P08" richiede="C00">

<obiettivo>
Genera la scheda user journey J08 della persona P08 usando il formato <formato_journey> e le regole del contesto C00. Il percorso si svolge in una generica app di crowdfunding, senza riferimenti ad app, piattaforme, enti o progetti reali.
</obiettivo>

<persona_generata>
[Se la persona P08 è già stata generata, sostituisci questa riga con la sua scheda completa. Altrimenti lascia la riga così: userai la scheda sintetica.]
</persona_generata>

<scheda_sintetica_persona>
Roberta Galli, 47 anni, Torino. Giornalista scientifica freelance. Laptop con molte schede e un foglio di calcolo, smartphone per telefonare. Familiarità 5/5. Scadenze strette e interruzioni. Ricerca esaustiva per un articolo. Se la scheda in <persona_generata> è presente, usa i suoi dettagli; in caso di conflitto valgono età, dispositivo, familiarità, accessibilità e frequenza di questa scheda.
</scheda_sintetica_persona>

<scenario>
Una settimana di lavoro, con consegna dell'articolo il venerdì. Roberta parte dalla pagina del programma di crowdfunding dell'università su un'app e vuole ricostruire tutte le edizioni: quanti progetti, quanto raccolto, quali risultati, e intervistare almeno un gruppo di ricerca. Obiettivo: pubblicare un articolo con dati verificati e link corretti.
</scenario>

<fasi>
Usa queste fasi come colonne. Per ogni fase sono indicati i problemi del catalogo di C00 da far emergere nella riga «Criticità e barriere» (con una soluzione in «Opportunità di miglioramento») e le esperienze positive da usare. Le chiavi non vanno riportate nel documento.
1. Raccolta di informazioni sul programma. Canali: sito da laptop, sito dell'università. Problemi: S09, X06, S14.
2. Ricognizione dei progetti conclusi. Problemi: S22, S24, S15, S21, S20. Positivo: S08.
3. Approfondimento di un progetto concluso. Problemi: S30, S13. Positivo: S27 (aggiornamenti dopo la fine della campagna).
4. Contatto con le fonti. Canali: sito, email, telefono. Problemi: S28, S25.
5. Verifica dei numeri. Canali: foglio di calcolo, sito. Problemi: X06, S66.
6. Pubblicazione dell'articolo con il link al programma. Canale: sistema editoriale della testata. Riflessione: i lettori arriveranno su una pagina senza date (S09).
</fasi>

<indicazioni_specifiche>
- Usa il modello del berrypicking: la risposta si costruisce passando tra app, sito dell'università e fonti dirette.
- Momenti critici: fase 5, numeri che non coincidono (fiducia, HEART Happiness); fase 2, perdita di stato dopo un'interruzione.
- In «Fonti e ipotesi» nota che l'articolo è un touchpoint indiretto per futuri donatori.
</indicazioni_specifiche>

<controllo_finale>
Prima di rispondere verifica, senza scriverlo: (1) nessun nome di app, piattaforma, ente, università o progetto reale e nessuna chiave Sxx o Xxx nel testo; (2) tutti i problemi indicati nelle fasi emergono come criticità vissute; (3) le colonne coincidono con le fasi del front matter; (4) ogni cella di «Emozioni e loro base» ha emozione, punteggio e base; (5) ogni criticità ha un'opportunità corrispondente.
</controllo_finale>

</prompt>
````
<!-- END PROMPT id="J08" -->
