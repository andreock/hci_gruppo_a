---
documento: persona_journey_prompts
persona: P08
journey: J08
nome: Roberta Galli
descrizione: giornalista scientifica
richiede: 00_contesto_comune_C00.md
modello_consigliato: Claude Opus 5.5 (claude-opus-5-5)
prompt_ids: [P08, J08]
---

# P08 · J08 · Roberta Galli, giornalista scientifica

Questo file contiene i due prompt della persona P08 e del suo journey J08. Il contesto comune non è ripetuto qui: si trova in [00_contesto_comune_C00.md](00_contesto_comune_C00.md).

**Come usarlo**
1. Apri una nuova conversazione con Opus 5.5 e incolla il prompt **C00** dal file del contesto comune.
2. Per la persona incolla il prompt **P08**; per il journey usa una nuova conversazione, incolla di nuovo C00 e poi il prompt **J08**. Puoi anche incollare C00 e il prompt singolo nello stesso messaggio.
3. Se la persona P08 è già stata generata, incolla il suo documento dentro `<persona_generata>` del prompt J08; altrimenti lascialo com'è.
4. Facoltativo: controlla l'output con il prompt V00 in [99_verifica_V00.md](99_verifica_V00.md).

Il testo da copiare è quello dentro ciascun blocco di codice.

<!-- BEGIN PROMPT id="P08" tipo="persona" persona="P08" richiede="C00" -->
````text
<prompt id="P08" tipo="persona" richiede="C00">

<obiettivo>
Genera la persona P08 usando il formato <formato_persona> e le regole del contesto C00.
</obiettivo>

<scheda_vincolante>
- Nome: Roberta Galli
- Età: 47
- Città: Torino
- Occupazione: giornalista scientifica freelance per una testata online locale
- Famiglia: sposata, due figli
- Ruolo: visitatrice per lavoro (non dona durante la ricerca; potrebbe farlo a titolo personale in seguito)
- Dispositivo principale: laptop con molte schede aperte e un foglio di calcolo; smartphone per telefonate e foto
- Canali: sito da laptop, sito unito.it, email, telefono, sistema di gestione dei contenuti della testata
- Familiarità digitale: 5/5. Ricerca avanzata, verifica delle fonti, archivi online
- Accessibilità e contesto: nessuna esigenza specifica; lavora con scadenze strette e molte interruzioni
- Frequenza d'uso: occasionale ma intensiva: 2–3 sessioni lunghe nella stessa settimana per un articolo
- Tipo di ricerca: esaustiva (vuole tutti i progetti di tutte le edizioni e i numeri complessivi)
- Motivazione: sta scrivendo l'articolo «Quattro edizioni di Funds TOgether: che cosa ha finanziato il crowdfunding dell'Ateneo»
- Archetipo suggerito: «la giornalista che verifica ogni numero»
</scheda_vincolante>

<problemi_assegnati>
- [S09 · H1 · G3] Testi al futuro, nessuna data, blog fermo al 2021–2022: non sa a quale edizione si riferisce la pagina.
- [X06 · analisi preliminare, da verificare] Nella stessa pagina testo e contatori riportano numeri diversi.
- [S14 · H3 · G3] La guida su unito.it si apre senza avviso in un altro sito e in un'altra scheda.
- [S22 · H7 · G3] «ALTRI» carica 4 progetti per volta senza dire quanti ne restano.
- [S24 · H9 · G2] A fine elenco «ALTRI» sparisce senza messaggio: non è sicura di averli visti tutti.
- [S15 · H3 · G4] Tornando da un progetto perde la posizione e i progetti caricati.
- [S21 · H7 · G3] Non può filtrare per edizione né ordinare.
- [S20 · H7 · G3] Manca «Torna su» nelle pagine lunghe.
- [S13 · H2 · G2] I nomi dei gruppi non permettono di capire quali siano dell'Ateneo.
- [S30 · H2 · G2] In BRIGHT gli aggiornamenti precedono la presentazione del progetto.
- [S28 · H1 · G3] «Contatta il progettista» non dà feedback per diversi secondi.
- [S25 · H10 · G2] Nessun contatto UniTo di riferimento nella pagina.
- [S66 · LG8 · G1] Il blog in homepage non mostra articoli né date.
</problemi_assegnati>

<aspetti_positivi_da_includere>
- [S27 · positivo] Nei progetti conclusi ci sono gli aggiornamenti dopo la fine della campagna: materiale prezioso per l'articolo.
- [S08 · positivo] Le card riassumono percentuale, raccolto e donatori.
</aspetti_positivi_da_includere>

<indicazioni_specifiche>
- Il suo bisogno è di tipo esaustivo e di verifica: mostra come il sito supporta male la ricerca esaustiva rispetto a quella conosciuta.
- Rappresenta anche un canale indiretto del servizio: il suo articolo porterà nuovi visitatori, quindi gli errori che trova possono amplificarsi.
- Mostra l'attenzione divisa (telefonate, scadenze) e come la perdita di stato ([S15]) peggiora l'effetto delle interruzioni.
</indicazioni_specifiche>

<controllo_finale>
Prima di rispondere verifica, senza scriverlo: (1) il front matter è completo e problemi_citati contiene esattamente gli ID citati nel testo; (2) ogni problema assegnato è citato almeno una volta; (3) i dati della scheda vincolante sono rispettati; (4) titoli e ordine delle sezioni sono identici a <formato_persona>.
</controllo_finale>

</prompt>
````
<!-- END PROMPT id="P08" -->

<!-- BEGIN PROMPT id="J08" tipo="journey_map" persona="P08" richiede="C00" -->
````text
<prompt id="J08" tipo="journey_map" persona="P08" richiede="C00">

<obiettivo>
Genera la journey map J08 della persona P08 usando il formato <formato_journey> e le regole del contesto C00.
</obiettivo>

<persona_generata>
[Se la persona P08 è già stata generata, sostituisci questa riga con il suo documento completo. Altrimenti lascia la riga così: userai la scheda sintetica.]
</persona_generata>

<scheda_sintetica_persona>
Roberta Galli, 47 anni, Torino. Giornalista scientifica freelance. Laptop con molte schede e un foglio di calcolo, smartphone per telefonare. Familiarità 5/5. Lavora con scadenze strette e interruzioni. Ricerca esaustiva per un articolo. Se il documento in <persona_generata> è presente, usa i suoi dettagli; in caso di conflitto valgono età, dispositivo, familiarità, accessibilità e frequenza di questa scheda.
</scheda_sintetica_persona>

<scenario>
Una settimana di lavoro, con consegna dell'articolo il venerdì. Roberta parte dalla pagina partner UniTo e vuole ricostruire tutte le edizioni di Funds TOgether: quanti progetti, quanto raccolto, quali risultati, e intervistare almeno un gruppo di ricerca. Obiettivo: pubblicare un articolo con dati verificati e link corretti.
</scenario>

<fasi>
1. Raccolta di informazioni sull'iniziativa. Canali: sito da laptop, unito.it. Problemi: [S09 · H1 · G3], [X06 · analisi preliminare, da verificare], [S14 · H3 · G3].
2. Ricognizione dei progetti conclusi. Problemi: [S22 · H7 · G3], [S24 · H9 · G2], [S15 · H3 · G4], [S21 · H7 · G3], [S20 · H7 · G3]. Positivo: [S08 · positivo].
3. Approfondimento di un caso (BRIGHT). Problemi: [S30 · H2 · G2], [S13 · H2 · G2]. Positivo: [S27 · positivo].
4. Contatto con le fonti. Canali: sito, email, telefono. Problemi: [S28 · H1 · G3], [S25 · H10 · G2].
5. Verifica dei numeri. Canali: foglio di calcolo, sito, unito.it. Problemi: [X06 · analisi preliminare, da verificare], [S66 · LG8 · G1].
6. Pubblicazione dell'articolo con link al sito. Canale: sistema di gestione dei contenuti della testata. Riflessione: i lettori atterreranno su una pagina con [S09 · H1 · G3].
</fasi>

<indicazioni_specifiche>
- Usa il modello del berrypicking per descrivere come la risposta si costruisce progressivamente tra Ginger, unito.it e le fonti dirette.
- Momento critico: fase 5, quando i numeri non coincidono e deve decidere quale fonte citare (fiducia, HEART Happiness). Altro momento: fase 2, perdita di stato dopo un'interruzione.
- Nelle note per il team indica che l'articolo è un touchpoint indiretto per futuri donatori.
</indicazioni_specifiche>

<controllo_finale>
Prima di rispondere verifica, senza scriverlo: (1) front matter completo e problemi_citati uguale agli ID citati; (2) tutti i problemi elencati nelle fasi sono citati; (3) le fasi della tabella coincidono con il front matter; (4) i punteggi della curva emotiva coincidono con la riga Emozioni; (5) ogni difficoltà ha un'opportunità corrispondente.
</controllo_finale>

</prompt>
````
<!-- END PROMPT id="J08" -->
