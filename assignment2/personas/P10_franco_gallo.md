---
documento: persona_journey_prompts
versione: 3 (personas generiche)
persona: P10
journey: J10
nome: Franco Gallo
descrizione: professore responsabile di una campagna in corso
richiede: 00_contesto_comune_C00.md
modello_consigliato: Claude Opus 5.5 (claude-opus-5-5)
prompt_ids: [P10, J10]
---

# P10 · J10 · Franco Gallo, professore responsabile di una campagna in corso

Questo file contiene i due prompt della persona P10 e del suo journey J10. Il contesto comune non è ripetuto qui: si trova in [00_contesto_comune_C00.md](00_contesto_comune_C00.md).

**Come usarlo**
1. Apri una nuova conversazione con Opus 5.5, incolla il prompt **C00** dal file del contesto comune e allega il template del corso: [scheda_persona.pdf](template/scheda_persona.pdf) per la persona, [scheda_user_journey.pdf](template/scheda_user_journey.pdf) per il journey.
2. Per la persona incolla il prompt **P10**; per il journey usa una nuova conversazione, incolla di nuovo C00 e poi il prompt **J10**. Puoi anche incollare C00 e il prompt singolo nello stesso messaggio.
3. Se la persona P10 è già stata generata, incolla il suo documento dentro `<persona_generata>` del prompt J10; altrimenti lascialo com'è.
4. Facoltativo: controlla l'output con il prompt V00 in [99_verifica_V00.md](99_verifica_V00.md).

Il testo da copiare è quello dentro ciascun blocco di codice.

<!-- BEGIN PROMPT id="P10" tipo="persona" persona="P10" richiede="C00" -->
````text
<prompt id="P10" tipo="persona" richiede="C00">

<obiettivo>
Genera la scheda della persona P10 usando il formato <formato_persona> e le regole del contesto C00. Racconta la persona e il suo rapporto con il crowdfunding in generale, senza riferimenti ad app, piattaforme, enti o progetti reali.
</obiettivo>

<scheda_vincolante>
- Nome: Franco Gallo
- Età: 63
- Città: Torino
- Occupazione: professore ordinario di area veterinaria
- Famiglia: sposato, tre figli adulti, due nipoti
- Vita quotidiana: riunioni, lezioni, commissioni; apicoltore per passione nella casa in collina; legge il giornale su carta
- Valori: responsabilità verso il gruppo di ricerca, reputazione, divulgazione
- Ruolo: promotore; responsabile scientifico di una campagna fittizia sulla salute delle api («AlveareSano»), in corso, al 130% dell'obiettivo con 20 giorni rimasti, cofinanziata dall'università se raggiunge l'obiettivo
- Dispositivo principale: PC fisso con monitor da 27 pollici nello studio; smartphone per email e telefonate
- Familiarità digitale: 2/5. Email, piattaforme per i bandi, presentazioni; delega gli aspetti tecnici a un dottorando; poca pazienza con le interfacce
- Accessibilità e contesto: presbiopia lieve; consulta l'app tra una riunione e l'altra, pochi minuti per volta
- Frequenza d'uso: quotidiana durante la campagna (controlli di 2–3 minuti), quasi nulla dopo
- Motivazione: raggiungere il secondo obiettivo, far capire ai donatori che il cofinanziamento raddoppia i fondi, chiudere con una buona immagine del gruppo
- Archetipo: «il responsabile scientifico con poco tempo»
</scheda_vincolante>

<frustrazioni_da_far_emergere>
Frustrazioni con le app di crowdfunding da trasformare in 3–5 punti personali di «Difficoltà e frustrazioni», senza dettagli tecnici dell'interfaccia (le chiavi tra parentesi quadre rimandano al catalogo di C00 e non vanno riportate):
- [S10, X08, S37] Il successo della campagna che sembra dire ai donatori che non serve più donare.
- [S11, S16] Indicatori di avanzamento e scadenze che si prestano a equivoci.
- [S28, S29] Lamentele dei donatori per pulsanti che sembrano non funzionare.
- [S13, S18, S64] La campagna presentata male nelle anteprime (nome del gruppo, tema, titolo tagliato).
- Poco tempo per imparare uno strumento nuovo.
</frustrazioni_da_far_emergere>

<indicazioni_specifiche>
- È responsabile dell'esperienza dei donatori senza controllare l'interfaccia: subisce i problemi attraverso domande e lamentele degli altri.
- La familiarità bassa non va resa con stereotipi: è un esperto che sa comunicare la ricerca, ma non ha tempo.
- Il raddoppio del cofinanziamento è il suo argomento principale e l'app non lo aiuta a renderlo visibile.
</indicazioni_specifiche>

<controllo_finale>
Prima di rispondere verifica, senza scriverlo: (1) nessun nome di app, piattaforma, ente, università o progetto reale e nessuna chiave Sxx o Xxx nel testo; (2) campi, etichette e ordine identici a <formato_persona>; (3) dati della scheda vincolante rispettati; (4) il profilo descrive la vita della persona, non un'interfaccia.
</controllo_finale>

</prompt>
````
<!-- END PROMPT id="P10" -->

<!-- BEGIN PROMPT id="J10" tipo="journey_map" persona="P10" richiede="C00" -->
````text
<prompt id="J10" tipo="journey_map" persona="P10" richiede="C00">

<obiettivo>
Genera la scheda user journey J10 della persona P10 usando il formato <formato_journey> e le regole del contesto C00. Il percorso si svolge in una generica app di crowdfunding, senza riferimenti ad app, piattaforme, enti o progetti reali.
</obiettivo>

<persona_generata>
[Se la persona P10 è già stata generata, sostituisci questa riga con la sua scheda completa. Altrimenti lascia la riga così: userai la scheda sintetica.]
</persona_generata>

<scheda_sintetica_persona>
Franco Gallo, 63 anni, professore ordinario di area veterinaria, apicoltore per passione. Responsabile della campagna fittizia «AlveareSano», in corso, al 130% con 20 giorni rimasti. PC fisso con monitor grande, smartphone. Familiarità 2/5, delega a un dottorando. Presbiopia lieve, poco tempo. Se la scheda in <persona_generata> è presente, usa i suoi dettagli; in caso di conflitto valgono età, dispositivo, familiarità, accessibilità e frequenza di questa scheda.
</scheda_sintetica_persona>

<scenario>
Le ultime tre settimane della campagna «AlveareSano». Franco controlla ogni giorno la pagina pubblica tra una riunione e l'altra, risponde ai donatori, prepara la comunicazione con l'ufficio stampa e alla fine deve rendicontare. Obiettivo: superare il secondo obiettivo e far capire che la raccolta è ancora utile grazie al cofinanziamento.
</scenario>

<fasi>
Usa queste fasi come colonne. Per ogni fase sono indicati i problemi del catalogo di C00 da far emergere nella riga «Criticità e barriere» (con una soluzione in «Opportunità di miglioramento») e le esperienze positive da usare. Le chiavi non vanno riportate nel documento.
1. Controllo della pagina pubblica e dell'anteprima della campagna. Canale: sito da desktop. Problemi: S64, S13, S18.
2. Monitoraggio quotidiano. Problemi: S11, S16. Positivi: S27, S08.
3. Superamento dell'obiettivo. Problemi: S10, X08, S37.
4. Comunicazione ai donatori e alla stampa. Canali: area riservata [IPOTESI], email, ufficio stampa. Problemi: S30, S34.
5. Gestione delle domande dei donatori. Canali: email, telefono. Problema: S28.
6. Chiusura della campagna e rendicontazione. Problema: S29.
</fasi>

<indicazioni_specifiche>
- Molti touchpoint sono indiretti (donatori, colleghi, ufficio stampa che gli riportano problemi): rendilo esplicito in «Touchpoint e canali».
- Momento critico: fase 3, quando il successo diventa un ostacolo alla raccolta (HEART Engagement dei donatori).
- In «Fonti e ipotesi» indica quali passaggi riguardano l'area riservata dei promotori, marcati [IPOTESI].
</indicazioni_specifiche>

<controllo_finale>
Prima di rispondere verifica, senza scriverlo: (1) nessun nome di app, piattaforma, ente, università o progetto reale e nessuna chiave Sxx o Xxx nel testo; (2) tutti i problemi indicati nelle fasi emergono come criticità vissute; (3) le colonne coincidono con le fasi del front matter; (4) ogni cella di «Emozioni e loro base» ha emozione, punteggio e base; (5) ogni criticità ha un'opportunità corrispondente.
</controllo_finale>

</prompt>
````
<!-- END PROMPT id="J10" -->
